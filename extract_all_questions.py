"""Extract ALL questions for an ExamTopics exam (captcha-free).

The official /exams/<provider>/<exam>/view/N/ pages gate pages 2+ behind a
reCAPTCHA. This tool avoids that wall entirely by using two public,
un-gated endpoints:

  1. Exam-view page 1  -> gives the total question count and the first
     question's internal id (data-id). ExamTopics assigns these ids
     sequentially per exam, so the full id range is known.
  2. /ajax/discussion/exam-question/<question_id> -> maps each question id
     to its discussion id (no captcha).
  3. /discussions/<provider>/view/<discussion_id>-x/ -> the canonical
     question page with full text, choices and the community most-voted
     answer (no captcha).

Result is written to "<EXAM> questions.txt", sorted by topic / question.

Usage:
    python extract_all_questions.py microsoft ai-103
    python extract_all_questions.py microsoft az-104
"""
import json
import re
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from html import unescape
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

from examtopics.matching import display_slug, normalize_provider
from examtopics.settings import BASE_URL, DEFAULT_RETRIES, DEFAULT_TIMEOUT_MS, REQUEST_HEADERS
from examtopics.cache import HtmlCache
from examtopics.http_client import HttpFetcher
from examtopics.fast_scanner import FastDiscussionScanner
from examtopics.matching import build_page_numbers
from examtopics.settings import (
    DEFAULT_CACHE_DIR,
    DEFAULT_CACHE_TTL_SECONDS,
    DEFAULT_DELAY_RANGE,
    DEFAULT_REQUEST_WORKERS,
)

WORKERS = 12
TIMEOUT = DEFAULT_TIMEOUT_MS // 1000

_thread_local = threading.local()
_session_cookies = None


def _session() -> requests.Session:
    sess = getattr(_thread_local, "session", None)
    if sess is None:
        sess = requests.Session()
        sess.headers.update(REQUEST_HEADERS)
        if _session_cookies:
            sess.cookies.update(_session_cookies)
        _thread_local.session = sess
    return sess


def get(url: str, *, referer: str = None, xhr: bool = False) -> requests.Response:
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


def discover_range(provider, exam):
    """Return (first_question_id, total_questions) from exam-view page 1."""
    url = exam_view_url(provider, exam, 1)
    html = get(url).text
    ids = [int(x) for x in re.findall(r'question-body"\s+data-id="(\d+)"', html)]
    total = None
    m = re.search(r"out of\s+(\d+)\s+questions", html, re.I)
    if m:
        total = int(m.group(1))
    if not ids:
        raise RuntimeError("Could not read question ids from exam page 1")
    return min(ids), total, url


def discussion_id_for(qid, referer):
    url = f"{BASE_URL}/ajax/discussion/exam-question/{qid}"
    r = get(url, referer=referer, xhr=True)
    if r.status_code != 200:
        return None
    m = re.search(r'data-discussion-id="(\d+)"', r.text)
    return m.group(1) if m else None


def _br_text(node) -> str:
    for br in node.find_all("br"):
        br.replace_with("\n")
    text = unescape(node.get_text())
    return "\n".join(ln.strip() for ln in text.splitlines() if ln.strip())


def parse_question_page(html, url, expected_exam):
    soup = BeautifulSoup(html, "html.parser")
    hdr = soup.select_one(".question-discussion-header")
    htext = re.sub(r"\s+", " ", hdr.get_text(" ", strip=True)) if hdr else ""

    exam_m = re.search(r"Microsoft's\s+([A-Za-z0-9\-]+)", htext) or re.search(
        r"from\s+\w+'s\s+([A-Za-z0-9\-]+)", htext
    )
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

    suggested = None
    sc = soup.select_one(".voted-answers-tally script")
    if sc:
        try:
            data = json.loads(sc.string or "[]")
            suggested = next(
                (e.get("voted_answers") for e in data if e.get("is_most_voted")),
                data[0].get("voted_answers") if data else None,
            )
        except (json.JSONDecodeError, TypeError, KeyError):
            pass

    return {
        "url": url,
        "exam": found_exam,
        "topic": topic,
        "question_no": question_no,
        "question": question_text,
        "choices": choices,
        "suggested": suggested,
    }


def sort_key(item):
    def to_int(v):
        return v if isinstance(v, int) else 1 << 30

    return (to_int(item.get("topic")), to_int(item.get("question_no")))


def format_question(item):
    topic = item.get("topic") if item.get("topic") is not None else "?"
    qno = item.get("question_no") if item.get("question_no") is not None else "?"
    lines = [
        "=" * 70,
        f"Topic {topic} - Question {qno}",
        item["url"],
        "=" * 70,
        "",
        item["question"] or "(question text not found)",
        "",
    ]
    for letter, text in item["choices"]:
        lines.append(f"{letter}. {text}" if letter else f"- {text}")
    if item["choices"]:
        lines.append("")
    if item.get("suggested"):
        lines.append(f"Suggested Answer (community most voted): {item['suggested']}")
        lines.append("")
    return "\n".join(lines)


def main():
    global _session_cookies
    if len(sys.argv) < 3:
        print("Usage: python extract_all_questions.py <provider> <exam-code>")
        print("Example: python extract_all_questions.py microsoft ai-103")
        return

    provider = normalize_provider(sys.argv[1])
    exam = sys.argv[2].strip().lower()
    exam_label = display_slug(sys.argv[2]).upper()

    # Warm a session (cookies) against exam page 1, and discover id range.
    warm = requests.Session()
    warm.headers.update(REQUEST_HEADERS)
    warm.get(exam_view_url(provider, exam, 1), timeout=TIMEOUT)
    _session_cookies = warm.cookies

    first_id, total, referer = discover_range(provider, exam)
    if not total:
        total = 0
    print(f"Exam {exam_label}: first question id {first_id}, {total} questions total.")

    # ----- URL SOURCE 1: discussion listing scan -----------------------------
    # The discussion listing finds question URLs by exam name regardless of
    # their internal id, so it works even when an exam's question-ids are not
    # contiguous (true for older/large exams like AZ-400). This is the primary
    # source for completeness.
    cache = HtmlCache(Path(DEFAULT_CACHE_DIR), DEFAULT_CACHE_TTL_SECONDS)
    listing_fetcher = HttpFetcher(
        timeout=TIMEOUT, retries=DEFAULT_RETRIES, cache=cache, refresh_cache=False
    )
    scanner = FastDiscussionScanner(provider, listing_fetcher, delay_range=DEFAULT_DELAY_RANGE)
    listing_urls = []
    try:
        total_pages = scanner.get_num_pages()
        page_numbers = build_page_numbers(total_pages, 1, None, None)
        print(f"Scanning {len(page_numbers)} discussion listing pages for {exam_label}...")
        listing_urls = scanner.scan(page_numbers, exam, workers=DEFAULT_REQUEST_WORKERS)
        print(f"Listing scan found {len(listing_urls)} discussion links.")
    except Exception as exc:  # noqa: BLE001
        print(f"Listing scan failed ({exc}); relying on id-walk only.")

    # ----- URL SOURCE 2: sequential id-walk ----------------------------------
    # Catches questions that have no discussion-listing entry (e.g. brand-new
    # questions). Walk the contiguous id block starting at first_id.
    span = (total + 10) if total else 80
    candidate_ids = list(range(first_id, first_id + span))

    qid_to_did = {}

    def map_one(qid):
        return qid, discussion_id_for(qid, referer)

    if candidate_ids:
        with ThreadPoolExecutor(max_workers=WORKERS) as ex:
            futs = {ex.submit(map_one, qid): qid for qid in candidate_ids}
            with tqdm(total=len(futs), desc="Mapping IDs", unit="q") as pbar:
                for fut in as_completed(futs):
                    qid, did = fut.result()
                    if did:
                        qid_to_did[qid] = did
                    pbar.update(1)

    # Merge both URL sources, deduped by canonical discussion URL.
    all_urls = set()
    for url in listing_urls:
        all_urls.add(url)
    for did in qid_to_did.values():
        all_urls.add(f"{BASE_URL}/discussions/{provider}/view/{did}-x/")
    print(f"Total candidate question URLs: {len(all_urls)}")

    # ----- Fetch + parse each question page (captcha-free) -------------------
    results = {}

    def fetch_one(url):
        r = get(url, referer=referer)
        if r.status_code != 200:
            return None
        return parse_question_page(r.text, r.url, exam_label)

    with ThreadPoolExecutor(max_workers=WORKERS) as ex:
        futs = {ex.submit(fetch_one, url): url for url in all_urls}
        with tqdm(total=len(futs), desc="Fetching Questions", unit="q") as pbar:
            for fut in as_completed(futs):
                try:
                    item = fut.result()
                    if item and item.get("exam") and item["exam"].upper() == exam_label:
                        key = (item["topic"], item["question_no"])
                        results[key] = item
                except Exception as exc:  # noqa: BLE001
                    print(f"\nFailed: {exc}")
                pbar.update(1)

    unique = sorted(results.values(), key=sort_key)

    out_path = Path(f"{exam_label} questions.txt")
    with out_path.open("w", encoding="utf-8") as fh:
        fh.write(f"{exam_label} - Extracted Questions ({len(unique)} of {total})\n")
        fh.write("Source: ExamTopics question/discussion pages\n\n")
        for it in unique:
            fh.write(format_question(it))
            fh.write("\n")

    print(f"\nDone. Wrote {len(unique)} questions to {out_path.name}")


if __name__ == "__main__":
    main()
