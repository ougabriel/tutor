"""Harvest question-body image URLs for every question and save a map.

ExamTopics stores HOTSPOT / drag-drop / exhibit images on its CDN
(https://img.examtopics.com/<exam>/imageN.png). These are referenced inside
the .question-body of each discussion page. This script reads the discussion
URLs already present in each "<EXAM> questions.txt", fetches each page
(cached), extracts the question-body image URLs, and writes
question_images.json keyed by "<EXAM>|T<topic>|Q<question>".

build_mock_exam.py then embeds these images inline so image-based questions
are complete and usable.

Run from the mock-exam folder:
    python harvest_images.py
"""
import json
import re
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

# scraper package lives in the repo root (parent of this folder)
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from examtopics.settings import REQUEST_HEADERS  # noqa: E402

OUT = "question_images.json"
WORKERS = 10
TIMEOUT = 45

_tl = threading.local()


def sess():
    s = getattr(_tl, "s", None)
    if s is None:
        s = requests.Session()
        s.headers.update(REQUEST_HEADERS)
        _tl.s = s
    return s


def get(url):
    last = None
    for attempt in range(1, 4):
        try:
            return sess().get(url, timeout=TIMEOUT)
        except Exception as exc:  # noqa: BLE001
            last = exc
            time.sleep(attempt)
    raise RuntimeError(f"GET failed {url}: {last}")


def parse_questions_file(path: Path):
    """Yield (exam_label, topic, question_no, url) for each question block."""
    raw = path.read_text(encoding="utf-8")
    exam = path.name.replace(" questions.txt", "").strip()
    SEP = "=" * 70
    chunks = raw.split(SEP)
    i = 0
    while i < len(chunks):
        header = chunks[i]
        m = re.search(r"Topic\s+(\d+)\s*-\s*Question\s+(\d+)", header)
        um = re.search(r"(https?://\S+)", header)
        if m and um:
            yield exam, int(m.group(1)), int(m.group(2)), um.group(1)
        i += 1


def extract_images(html: str):
    soup = BeautifulSoup(html, "html.parser")
    body = soup.select_one(".question-body")
    if not body:
        return []
    urls = []
    for img in body.select("img"):
        src = img.get("src") or img.get("data-src") or ""
        src = src.strip()
        if src and ("img.examtopics" in src or "/assets/media" in src or src.lower().endswith((".png", ".jpg", ".jpeg", ".gif"))):
            if src not in urls:
                urls.append(src)
    # also capture answer-area images (drag-drop answers are often images)
    return urls


def main():
    files = sorted(Path(".").glob("* questions.txt"))
    if not files:
        print("No '<EXAM> questions.txt' files found.")
        return

    tasks = []
    for f in files:
        for exam, topic, qno, url in parse_questions_file(f):
            tasks.append((exam, topic, qno, url))
    print(f"Checking {len(tasks)} questions for images...")

    images = {}

    def work(task):
        exam, topic, qno, url = task
        # normalize to the -x slug form so it resolves
        slug_url = re.sub(r"(/view/\d+)(-[^/]*)?/?$", r"\1-x/", url)
        try:
            r = get(slug_url)
            if r.status_code != 200:
                return None
            imgs = extract_images(r.text)
            if imgs:
                return (f"{exam}|T{topic}|Q{qno}", imgs)
        except Exception:
            return None
        return None

    with ThreadPoolExecutor(max_workers=WORKERS) as ex:
        futs = {ex.submit(work, t): t for t in tasks}
        with tqdm(total=len(futs), desc="Scanning images", unit="q") as pbar:
            for fut in as_completed(futs):
                res = fut.result()
                if res:
                    images[res[0]] = res[1]
                pbar.update(1)

    Path(OUT).write_text(json.dumps(images, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"\nWrote {OUT}: {len(images)} questions have images "
          f"({sum(len(v) for v in images.values())} image URLs total).")


if __name__ == "__main__":
    main()
