"""Extract ALL exam questions from ExamTopics exam-view pages.

Scrapes the official exam pages (/exams/<provider>/<exam>/view/<page>/),
which list every question with its answer choices and the official
"Correct Answer". Writes the result to "<EXAM> questions.txt".

Usage:
    python extract_questions.py microsoft ai-300
    python extract_questions.py amazon aws-certified-devops-engineer-professional-dop-c02
"""
import re
import sys
import time
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from html import unescape
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

from examtopics.browser_scraper import CamoufoxScraper
from examtopics.matching import display_slug, normalize_provider
from examtopics.settings import (
    BASE_URL,
    DEFAULT_RETRIES,
    DEFAULT_TIMEOUT_MS,
    REQUEST_HEADERS,
)

# Use a smaller worker count than the listing scanner: the exam-view pages
# rate-limit more aggressively than the discussion listings.
EXAM_VIEW_WORKERS = 6

# Markers that indicate a genuine anti-bot / captcha wall. We deliberately do
# NOT include "g-recaptcha-response" here because it appears in the normal
# answer-voting form on legitimate exam pages.
HARD_BLOCK_MARKERS = (
    "checking your browser",
    "verify you are human",
    "please complete the security check",
    "cf-chl",
    "access denied",
)

_thread_local = threading.local()


def _session() -> requests.Session:
    session = getattr(_thread_local, "session", None)
    if session is None:
        session = requests.Session()
        session.headers.update(REQUEST_HEADERS)
        _thread_local.session = session
    return session


def fetch_exam_html(url: str) -> str:
    last_error = None
    for attempt in range(1, DEFAULT_RETRIES + 1):
        try:
            response = _session().get(url, timeout=DEFAULT_TIMEOUT_MS // 1000)
            response.raise_for_status()
            lowered = response.text.lower()
            if any(marker in lowered for marker in HARD_BLOCK_MARKERS):
                raise RuntimeError("Blocked by anti-bot/captcha page")
            return response.text
        except Exception as exc:  # noqa: BLE001
            last_error = exc
            if attempt < DEFAULT_RETRIES:
                time.sleep(1.0 * attempt)
    raise RuntimeError(f"Failed to load {url}: {last_error}")


def browser_fetch(scraper, url: str, captcha_wait_s: int = 240) -> str:
    """Load an exam-view page via Camoufox and return its rendered HTML.

    Waits for the question card. If the reCAPTCHA wall appears instead, it
    polls for up to ``captcha_wait_s`` seconds so a human can solve the
    captcha in the visible browser window; as soon as the questions render,
    it returns.
    """
    from playwright.sync_api import TimeoutError as PlaywrightTimeoutError

    page = scraper.page
    page.goto(url, wait_until="domcontentloaded", timeout=DEFAULT_TIMEOUT_MS)
    scraper._remove_popup()

    try:
        page.wait_for_selector(".exam-question-card, .captcha-container", timeout=15_000)
    except PlaywrightTimeoutError:
        pass

    # Captcha wall: wait for the user to solve it in the visible window.
    if page.query_selector(".exam-question-card") is None and page.query_selector(".captcha-container"):
        print(
            f"\n  >> Captcha shown for {url}\n"
            f"     Solve the 'I am not a robot' challenge in the browser window. "
            f"Waiting up to {captcha_wait_s}s..."
        )
        deadline = time.time() + captcha_wait_s
        while time.time() < deadline:
            scraper._remove_popup()
            if page.query_selector(".exam-question-card"):
                break
            time.sleep(2)

    try:
        page.wait_for_load_state("networkidle", timeout=6_000)
    except PlaywrightTimeoutError:
        pass

    return page.content()


def exam_url(provider: str, exam: str, page: int) -> str:
    if page <= 1:
        return f"{BASE_URL}/exams/{provider}/{exam}/view/"
    return f"{BASE_URL}/exams/{provider}/{exam}/view/{page}/"


def parse_total_pages(html: str) -> int:
    text = re.sub(r"\s+", " ", BeautifulSoup(html, "html.parser").get_text(" "))
    match = re.search(r"page\s+\d+\s+out of\s+(\d+)\s+pages", text, re.I)
    if match:
        return int(match.group(1))
    match = re.search(r"Page\s+\d+\s+of\s+(\d+)", text, re.I)
    if match:
        return int(match.group(1))
    return 1


def _br_text(node) -> str:
    for br in node.find_all("br"):
        br.replace_with("\n")
    text = unescape(node.get_text())
    lines = [ln.strip() for ln in text.splitlines()]
    return "\n".join(ln for ln in lines if ln)


def _answer_text(span) -> str:
    """Correct answer may be a letter, text, or an image."""
    img = span.find("img")
    if img:
        return f"[image: {img.get('src', '')}]"
    return span.get_text(" ", strip=True)


def parse_questions_on_page(html: str):
    soup = BeautifulSoup(html, "html.parser")
    questions = []

    for card in soup.select(".exam-question-card"):
        header = card.select_one(".card-header")
        topic = question_no = None
        if header:
            htext = header.get_text(" ", strip=True)
            q = re.search(r"Question\s*#?\s*:?\s*(\d+)", htext)
            t = re.search(r"Topic\s*#?\s*:?\s*(\d+)", htext)
            question_no = q.group(1) if q else None
            topic = t.group(1) if t else None

        body = card.select_one(".question-body")
        question_text = ""
        if body:
            text_node = body.select_one("p.card-text")
            if text_node:
                # exclude the answer paragraph if nested
                question_text = _br_text(text_node)

        choices = []
        for item in card.select(".question-choices-container li.multi-choice-item"):
            letter_el = item.select_one(".multi-choice-letter")
            letter = ""
            if letter_el:
                letter = (
                    letter_el.get("data-choice-letter")
                    or letter_el.get_text(strip=True).rstrip(".")
                )
                letter_el.extract()
            choices.append((letter.strip(), item.get_text(" ", strip=True)))

        correct = None
        ans = card.select_one(".question-answer .correct-answer")
        if ans:
            correct = _answer_text(ans)

        data_id = body.get("data-id") if body else None

        questions.append(
            {
                "topic": topic,
                "question_no": question_no,
                "question": question_text,
                "choices": choices,
                "correct": correct,
                "data_id": data_id,
            }
        )

    return questions


def sort_key(item: dict):
    def to_int(value):
        try:
            return int(value)
        except (TypeError, ValueError):
            return 1 << 30

    return (to_int(item.get("topic")), to_int(item.get("question_no")))


def format_question(item: dict) -> str:
    topic = item.get("topic") or "?"
    qno = item.get("question_no") or "?"
    lines = [
        "=" * 70,
        f"Topic {topic} - Question {qno}",
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
    if item.get("correct"):
        lines.append(f"Correct Answer: {item['correct']}")
        lines.append("")
    return "\n".join(lines)


def main():
    if len(sys.argv) < 3:
        print("Usage: python extract_questions.py <provider> <exam-code-or-slug>")
        print("Example: python extract_questions.py microsoft ai-300")
        return

    provider = normalize_provider(sys.argv[1])
    exam = sys.argv[2].strip().lower()
    exam_label = display_slug(sys.argv[2]).upper()

    # Page 1 is served to plain HTTP. Pages 2+ are gated behind a reCAPTCHA
    # wall for anonymous clients, so we use the Camoufox stealth browser for
    # the remaining pages.
    first_html = fetch_exam_html(exam_url(provider, exam, 1))
    total_pages = parse_total_pages(first_html)
    print(f"Exam {exam_label}: {total_pages} pages to scan.")

    results = {1: parse_questions_on_page(first_html)}

    remaining = list(range(2, total_pages + 1))
    if remaining:
        headless = "--headless" in sys.argv
        print(
            "Fetching remaining pages with Camoufox browser (captcha-gated).\n"
            "A browser window will open. Solve the 'I am not a robot' captcha when\n"
            "it appears; once solved the session is reused for the rest.\n"
        )
        with CamoufoxScraper(headless=headless, timeout_ms=DEFAULT_TIMEOUT_MS, retries=DEFAULT_RETRIES) as scraper:
            for page in tqdm(remaining, desc="Extracting Pages", unit="page"):
                url = exam_url(provider, exam, page)
                try:
                    html = browser_fetch(scraper, url)
                    qs = parse_questions_on_page(html)
                    if not qs:
                        print(f"\nPage {page}: no questions found (still gated?).")
                    results[page] = qs
                except Exception as exc:  # noqa: BLE001
                    print(f"\nFailed page {page}: {exc}")

    all_questions = []
    for page in sorted(results):
        all_questions.extend(results[page])

    # Deduplicate by data_id (fallback to topic/question_no).
    seen = set()
    unique = []
    for q in all_questions:
        key = q.get("data_id") or (q.get("topic"), q.get("question_no"))
        if key in seen:
            continue
        seen.add(key)
        unique.append(q)

    unique.sort(key=sort_key)

    out_path = Path(f"{exam_label} questions.txt")
    with out_path.open("w", encoding="utf-8") as fh:
        fh.write(f"{exam_label} - Extracted Questions ({len(unique)} total)\n\n")
        for item in unique:
            fh.write(format_question(item))
            fh.write("\n")

    print(f"\nDone. Wrote {len(unique)} questions to {out_path.name}")


if __name__ == "__main__":
    main()
