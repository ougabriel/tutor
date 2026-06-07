"""Extract ALL exam questions WITH full answer evidence (captcha-free).

Builds on the question-id walk used by extract_all_questions.py, but for each
question it also gathers every answer signal available so the correct answer
can be judged with confidence:

  * Official "Correct Answer"  - from the ungated exam-view page 1 (only the
    first few questions are visible to anonymous users; the rest are gated).
  * Community most-voted answer - from the per-question vote tally JSON.
  * Answer consensus tally       - counts every comment's "Selected Answer: X".
  * Top comments                 - author, selected answer, upvotes, the
    "Most Voted" badge, and the reasoning / reference links they posted.

Outputs:
  * "<EXAM> answers.txt"        - human-readable report with full evidence.
  * "<EXAM> answers.csv"        - one row per question: official, community,
                                  consensus pick, agreement, confidence.

Usage:
    python extract_with_evidence.py microsoft ai-300
"""
import csv
import json
import re
import sys
import threading
import time
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from html import unescape
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

from examtopics.matching import display_slug, normalize_provider
from examtopics.settings import BASE_URL, DEFAULT_RETRIES, DEFAULT_TIMEOUT_MS, REQUEST_HEADERS

WORKERS = 10
TIMEOUT = DEFAULT_TIMEOUT_MS // 1000
MAX_COMMENTS = 6  # top comments to include as evidence

_thread_local = threading.local()
_cookies = None


def _session():
    sess = getattr(_thread_local, "session", None)
    if sess is None:
        sess = requests.Session()
        sess.headers.update(REQUEST_HEADERS)
        if _cookies:
            sess.cookies.update(_cookies)
        _thread_local.session = sess
    return sess


def get(url, *, referer=None, xhr=False):
    headers = {}
    if referer:
        headers["Referer"] = referer
    if xhr:
        headers["X-Requested-With"] = "XMLHttpRequest"
    last = None
    for attempt in range(1, DEFAULT_RETRIES + 1):
        try:
            return _session().get(url, headers=headers, timeout=TIMEOUT)
        except Exception as exc:  # noqa: BLE001
            last = exc
            time.sleep(attempt)
    raise RuntimeError(f"GET failed {url}: {last}")


def exam_view_url(provider, exam, page=1):
    if page <= 1:
        return f"{BASE_URL}/exams/{provider}/{exam}/view/"
    return f"{BASE_URL}/exams/{provider}/{exam}/view/{page}/"


def _br_text(node):
    for br in node.find_all("br"):
        br.replace_with("\n")
    return "\n".join(ln.strip() for ln in unescape(node.get_text()).splitlines() if ln.strip())


def official_answers_page1(provider, exam):
    """Map (topic, question_no) -> official correct answer for ungated page 1."""
    html = get(exam_view_url(provider, exam, 1)).text
    soup = BeautifulSoup(html, "html.parser")
    answers = {}
    first_id = None
    total = None
    m = re.search(r"out of\s+(\d+)\s+questions", html, re.I)
    if m:
        total = int(m.group(1))
    ids = [int(x) for x in re.findall(r'question-body"\s+data-id="(\d+)"', html)]
    if ids:
        first_id = min(ids)
    for card in soup.select(".exam-question-card"):
        hdr = card.select_one(".card-header")
        htext = hdr.get_text(" ", strip=True) if hdr else ""
        qn = re.search(r"Question #?\s*:?\s*(\d+)", htext)
        tp = re.search(r"Topic\s*(\d+)", htext)
        ans_el = card.select_one(".question-answer .correct-answer")
        if qn and ans_el:
            img = ans_el.find("img")
            ans = f"[image: {img.get('src')}]" if img else ans_el.get_text(" ", strip=True)
            key = (int(tp.group(1)) if tp else None, int(qn.group(1)))
            answers[key] = ans
    return answers, first_id, total


def discussion_id_for(qid, referer):
    r = get(f"{BASE_URL}/ajax/discussion/exam-question/{qid}", referer=referer, xhr=True)
    if r.status_code != 200:
        return None
    m = re.search(r'data-discussion-id="(\d+)"', r.text)
    return m.group(1) if m else None


def parse_comment(c):
    user_el = c.select_one(".comment-username, .title-username, [class*='username']")
    sel_el = c.select_one(".comment-selected-answers")
    content_el = c.select_one(".comment-content")
    up_el = c.select_one(".upvote-count")
    most = bool(c.select_one(".most-voted-answer-badge"))

    selected = None
    if sel_el:
        m = re.search(r"Selected Answer:\s*([A-Z]+)", sel_el.get_text(" ", strip=True))
        selected = m.group(1) if m else None

    upvotes = 0
    if up_el:
        try:
            upvotes = int(re.sub(r"\D", "", up_el.get_text()) or 0)
        except ValueError:
            upvotes = 0

    return {
        "user": user_el.get_text(strip=True) if user_el else "anonymous",
        "selected": selected,
        "upvotes": upvotes,
        "most_voted": most,
        "content": re.sub(r"\s+", " ", content_el.get_text(" ", strip=True)) if content_el else "",
    }


def parse_question_page(html, url):
    soup = BeautifulSoup(html, "html.parser")
    hdr = soup.select_one(".question-discussion-header")
    htext = re.sub(r"\s+", " ", hdr.get_text(" ", strip=True)) if hdr else ""

    exam_m = re.search(r"from\s+\w+'s\s+([A-Za-z0-9\-]+)", htext)
    found_exam = exam_m.group(1) if exam_m else None
    q = re.search(r"Question #:\s*(\d+)", htext)
    t = re.search(r"Topic #:\s*(\d+)", htext)
    question_no = int(q.group(1)) if q else None
    topic = int(t.group(1)) if t else None

    body = soup.select_one(".question-body .card-text") or soup.select_one(".question-body")
    question_text = _br_text(body) if body else ""

    choices = []
    for item in soup.select(".question-choices-container li.multi-choice-item"):
        letter_el = item.select_one(".multi-choice-letter")
        letter = ""
        if letter_el:
            letter = letter_el.get("data-choice-letter") or letter_el.get_text(strip=True).rstrip(".")
            letter_el.extract()
        choices.append((letter.strip(), item.get_text(" ", strip=True)))

    # community most-voted from tally json
    community = None
    community_votes = None
    sc = soup.select_one(".voted-answers-tally script")
    if sc:
        try:
            data = json.loads(sc.string or "[]")
            entry = next((e for e in data if e.get("is_most_voted")), data[0] if data else None)
            if entry:
                community = entry.get("voted_answers")
                community_votes = entry.get("vote_count")
        except (json.JSONDecodeError, TypeError):
            pass

    # comments (top-level only for the tally, but capture all selected answers)
    comments = [parse_comment(c) for c in soup.select(".comment-container")]
    comments = [c for c in comments if c["selected"] or c["content"]]

    # consensus from comment selected answers
    tally = Counter(c["selected"] for c in comments if c["selected"])
    consensus = tally.most_common(1)[0][0] if tally else None

    return {
        "url": url,
        "exam": found_exam,
        "topic": topic,
        "question_no": question_no,
        "question": question_text,
        "choices": choices,
        "community": community,
        "community_votes": community_votes,
        "comment_tally": dict(tally),
        "consensus": consensus,
        "comments": comments,
    }


def sort_key(item):
    def to_int(v):
        return v if isinstance(v, int) else 1 << 30

    return (to_int(item.get("topic")), to_int(item.get("question_no")))


def best_answer_and_confidence(item, official):
    key = (item["topic"], item["question_no"])
    off = official.get(key)
    comm = item["community"]
    cons = item["consensus"]
    votes = item["community_votes"] or 0
    comment_support = item["comment_tally"].get(cons, 0) if cons else 0

    # Decide the most-supported answer.
    candidates = [a for a in [off, comm, cons] if a]
    pick = None
    if off:
        pick = off
    elif comm:
        pick = comm
    elif cons:
        pick = cons

    # Agreement check across available signals (ignoring image answers).
    letters = {a for a in [off, comm, cons] if a and re.fullmatch(r"[A-Z]+", a)}
    agree = len(letters) <= 1

    # Confidence heuristic.
    if off and comm and off == comm:
        conf = "HIGH (official + community agree)"
    elif off and not comm:
        conf = "HIGH (official answer)"
    elif comm and cons and comm == cons and (votes >= 3 or comment_support >= 3):
        conf = "MEDIUM-HIGH (strong community consensus)"
    elif comm or cons:
        if votes >= 5 or comment_support >= 5:
            conf = "MEDIUM (community, well supported)"
        elif letters and not agree:
            conf = "LOW (signals disagree)"
        else:
            conf = "LOW (few votes)"
    else:
        conf = "NONE (no answer data / image answer)"

    return pick, off, comm, cons, agree, conf


def format_block(item, official):
    pick, off, comm, cons, agree, conf = best_answer_and_confidence(item, official)
    topic = item.get("topic") if item.get("topic") is not None else "?"
    qno = item.get("question_no") if item.get("question_no") is not None else "?"
    L = []
    L.append("=" * 78)
    L.append(f"Topic {topic} - Question {qno}")
    L.append(item["url"])
    L.append("=" * 78)
    L.append("")
    L.append(item["question"] or "(question text not found)")
    L.append("")
    for letter, text in item["choices"]:
        L.append(f"{letter}. {text}" if letter else f"- {text}")
    if item["choices"]:
        L.append("")
    L.append("-" * 40 + " ANSWER EVIDENCE " + "-" * 21)
    L.append(f"Official answer (ExamTopics): {off if off else 'gated / not available'}")
    cv = f" ({item['community_votes']} votes)" if item["community_votes"] else ""
    L.append(f"Community most-voted:         {comm if comm else 'no votes'}{cv}")
    if item["comment_tally"]:
        tally_str = ", ".join(f"{k}:{v}" for k, v in sorted(item["comment_tally"].items()))
        L.append(f"Comment selected-answer tally: {tally_str}")
    L.append(f"==> Best-supported answer: {pick if pick else 'UNDETERMINED'}   |   Confidence: {conf}")
    if not agree:
        L.append("    NOTE: answer signals disagree - verify manually.")
    L.append("")
    if item["comments"]:
        L.append("Top comments (evidence):")
        ranked = sorted(item["comments"], key=lambda c: (c["most_voted"], c["upvotes"]), reverse=True)
        for c in ranked[:MAX_COMMENTS]:
            tag = " [MOST VOTED]" if c["most_voted"] else ""
            sel = f"answer {c['selected']}" if c["selected"] else "no answer marked"
            L.append(f"  - {c['user']} ({sel}, {c['upvotes']} upvotes){tag}")
            if c["content"]:
                L.append(f"      {c['content'][:500]}")
        L.append("")
    return "\n".join(L)


def main():
    global _cookies
    if len(sys.argv) < 3:
        print("Usage: python extract_with_evidence.py <provider> <exam-code>")
        return

    provider = normalize_provider(sys.argv[1])
    exam = sys.argv[2].strip().lower()
    exam_label = display_slug(sys.argv[2]).upper()

    warm = requests.Session()
    warm.headers.update(REQUEST_HEADERS)
    warm.get(exam_view_url(provider, exam, 1), timeout=TIMEOUT)
    _cookies = warm.cookies
    referer = exam_view_url(provider, exam, 1)

    official, first_id, total = official_answers_page1(provider, exam)
    if not first_id:
        print("Could not determine question id range.")
        return
    print(f"Exam {exam_label}: first id {first_id}, {total} questions, "
          f"{len(official)} official answers visible (page 1).")

    span = (total + 6) if total else 80
    candidate_ids = list(range(first_id, first_id + span))

    # qid -> discussion id
    qid_to_did = {}
    with ThreadPoolExecutor(max_workers=WORKERS) as ex:
        futs = {ex.submit(discussion_id_for, qid, referer): qid for qid in candidate_ids}
        with tqdm(total=len(futs), desc="Mapping IDs", unit="q") as pbar:
            for fut in as_completed(futs):
                qid = futs[fut]
                did = fut.result()
                if did:
                    qid_to_did[qid] = did
                pbar.update(1)

    results = {}

    def fetch_one(qid, did):
        r = get(f"{BASE_URL}/discussions/{provider}/view/{did}-x/", referer=referer)
        if r.status_code != 200:
            return None
        return parse_question_page(r.text, r.url)

    with ThreadPoolExecutor(max_workers=WORKERS) as ex:
        futs = {ex.submit(fetch_one, qid, did): qid for qid, did in qid_to_did.items()}
        with tqdm(total=len(futs), desc="Fetching Evidence", unit="q") as pbar:
            for fut in as_completed(futs):
                qid = futs[fut]
                try:
                    item = fut.result()
                    if item and item.get("exam") and item["exam"].upper() == exam_label:
                        results[qid] = item
                except Exception as exc:  # noqa: BLE001
                    print(f"\nFailed qid {qid}: {exc}")
                pbar.update(1)

    items = sorted(results.values(), key=sort_key)
    seen, unique = set(), []
    for it in items:
        key = (it["topic"], it["question_no"])
        if key in seen:
            continue
        seen.add(key)
        unique.append(it)

    # Report
    txt_path = Path(f"{exam_label} answers.txt")
    with txt_path.open("w", encoding="utf-8") as fh:
        fh.write(f"{exam_label} - Questions with Answer Evidence ({len(unique)} of {total})\n")
        fh.write("Sources: official answer (page 1 only), community vote tally, "
                 "and per-comment selected answers with upvotes.\n\n")
        for it in unique:
            fh.write(format_block(it, official))
            fh.write("\n")

    # CSV summary
    csv_path = Path(f"{exam_label} answers.csv")
    with csv_path.open("w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["topic", "question", "official", "community", "community_votes",
                    "comment_consensus", "best_answer", "agreement", "confidence", "url"])
        for it in unique:
            pick, off, comm, cons, agree, conf = best_answer_and_confidence(it, official)
            w.writerow([it["topic"], it["question_no"], off or "", comm or "",
                        it["community_votes"] or "", cons or "", pick or "",
                        "agree" if agree else "DISAGREE", conf, it["url"]])

    # Console confidence summary
    counts = Counter()
    for it in unique:
        _, _, _, _, _, conf = best_answer_and_confidence(it, official)
        counts[conf.split(" ")[0]] += 1
    print(f"\nDone. Wrote {len(unique)} questions to {txt_path.name} and {csv_path.name}")
    print("Confidence breakdown:", dict(counts))


if __name__ == "__main__":
    main()
