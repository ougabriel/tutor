"""Scrape exam questions via ExamTopics DISCUSSION pages (captcha-free).

The official /exams/.../view/N/ pages are gated behind a reCAPTCHA for
anonymous users. The per-question discussion pages are NOT gated, so this
script:

  1. Scans the provider discussion listing for the given exam code.
  2. Fetches each matching discussion page (pooled HTTP, cached).
  3. Extracts the question text, answer choices, and the community
     most-voted answer.
  4. Writes "<EXAM> questions.txt", sorted by topic / question number.

Usage:
    python extract_from_discussions.py microsoft ai-103
    python extract_from_discussions.py amazon DOP-C02
"""
import json
import re
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from html import unescape
from pathlib import Path

from bs4 import BeautifulSoup
from tqdm import tqdm

from examtopics.cache import HtmlCache
from examtopics.fast_scanner import FastDiscussionScanner
from examtopics.http_client import HttpFetcher
from examtopics.matching import (
    build_page_numbers,
    display_slug,
    extract_topic_question,
    normalize_provider,
)
from examtopics.settings import (
    DEFAULT_CACHE_DIR,
    DEFAULT_CACHE_TTL_SECONDS,
    DEFAULT_DELAY_RANGE,
    DEFAULT_REQUEST_WORKERS,
    DEFAULT_RETRIES,
    DEFAULT_TIMEOUT_MS,
)


def build_fetcher(cache: HtmlCache) -> HttpFetcher:
    return HttpFetcher(
        timeout=DEFAULT_TIMEOUT_MS // 1000,
        retries=DEFAULT_RETRIES,
        cache=cache,
        refresh_cache=False,
    )


def _br_text(node) -> str:
    for br in node.find_all("br"):
        br.replace_with("\n")
    text = unescape(node.get_text())
    lines = [ln.strip() for ln in text.splitlines()]
    return "\n".join(ln for ln in lines if ln)


def parse_discussion(html: str, url: str) -> dict:
    soup = BeautifulSoup(html, "html.parser")

    topic = question_no = None
    header = soup.select_one(".question-discussion-header")
    if header:
        htext = header.get_text(" ", strip=True)
        q = re.search(r"Question #:\s*(\d+)", htext)
        t = re.search(r"Topic #:\s*(\d+)", htext)
        question_no = int(q.group(1)) if q else None
        topic = int(t.group(1)) if t else None

    if topic is None or question_no is None:
        tq = extract_topic_question(url)
        topic = topic if topic is not None else (tq[0] if tq[0] < 10**9 else None)
        question_no = question_no if question_no is not None else (tq[1] if tq[1] < 10**9 else None)

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
    for script in soup.select(".voted-answers-tally script"):
        try:
            data = json.loads(script.string or "[]")
        except (json.JSONDecodeError, TypeError):
            continue
        for entry in data:
            if entry.get("is_most_voted"):
                suggested = entry.get("voted_answers")
                break
        if suggested is None and data:
            suggested = data[0].get("voted_answers")
        if suggested:
            break

    return {
        "url": url,
        "topic": topic,
        "question_no": question_no,
        "question": question_text,
        "choices": choices,
        "suggested": suggested,
    }


def sort_key(item: dict):
    def to_int(value):
        return value if isinstance(value, int) else 1 << 30

    return (to_int(item.get("topic")), to_int(item.get("question_no")))


def format_question(item: dict) -> str:
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
        prefix = f"{letter}. " if letter else "- "
        lines.append(f"{prefix}{text}")
    if item["choices"]:
        lines.append("")
    if item.get("suggested"):
        lines.append(f"Suggested Answer (community most voted): {item['suggested']}")
        lines.append("")
    return "\n".join(lines)


def main():
    if len(sys.argv) < 3:
        print("Usage: python extract_from_discussions.py <provider> <exam-code>")
        print("Example: python extract_from_discussions.py microsoft ai-103")
        return

    provider = normalize_provider(sys.argv[1])
    exam_code = sys.argv[2].strip()
    exam_label = display_slug(exam_code).upper()

    cache = HtmlCache(Path(DEFAULT_CACHE_DIR), DEFAULT_CACHE_TTL_SECONDS)
    fetcher = build_fetcher(cache)

    # 1. Scan discussion listings for matching question links.
    scanner = FastDiscussionScanner(provider, fetcher, delay_range=DEFAULT_DELAY_RANGE)
    total_pages = scanner.get_num_pages()
    page_numbers = build_page_numbers(total_pages, 1, None, None)
    print(f"Scanning {len(page_numbers)} discussion pages for {exam_label}...")
    links = scanner.scan(page_numbers, exam_code, workers=DEFAULT_REQUEST_WORKERS)
    print(f"Found {len(links)} discussion links.")
    if not links:
        print("No discussion links found; nothing to extract.")
        return

    # 2. Extract question content from each discussion page.
    results = {}

    def work(url):
        return parse_discussion(fetcher.fetch_html(url), url)

    with ThreadPoolExecutor(max_workers=DEFAULT_REQUEST_WORKERS) as executor:
        futures = {executor.submit(work, url): url for url in links}
        with tqdm(total=len(futures), desc="Extracting Questions", unit="q") as pbar:
            for future in as_completed(futures):
                url = futures[future]
                try:
                    results[url] = future.result()
                except Exception as exc:  # noqa: BLE001
                    print(f"\nFailed for {url}: {exc}")
                pbar.update(1)

    items = sorted(results.values(), key=sort_key)

    out_path = Path(f"{exam_label} questions.txt")
    with out_path.open("w", encoding="utf-8") as fh:
        fh.write(f"{exam_label} - Extracted Questions ({len(items)} total)\n")
        fh.write("Source: ExamTopics discussion pages (community answers)\n\n")
        for item in items:
            fh.write(format_question(item))
            fh.write("\n")

    print(f"\nDone. Wrote {len(items)} questions to {out_path.name}")


if __name__ == "__main__":
    main()
