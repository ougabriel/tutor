"""Discover ExamTopics questions by scanning the question-id space via the
captcha-free ajax discussion endpoint.

Why this exists
---------------
extract_all_questions.py finds question URLs two ways:
  1. the public discussion *listing* (incomplete - it only surfaces a subset)
  2. a sequential id-walk of first_id .. first_id + total + 10

Question ids are global across ALL exams and are assigned in creation order,
so one exam's questions are scattered across several id blocks. The narrow
id-walk therefore misses every question added after the original batch.

/ajax/discussion/exam-question/<qid> is captcha-free and returns
    data-title="Exam AI-300 topic 2 question 7 discussion"
    data-discussion-id="404555"
so a single cheap request identifies the exam, topic, question number AND the
discussion id. Scanning the id range once builds a complete index for every
exam at the same time.

Writes qid_index.json:  {"<qid>": ["EXAM", topic, question, discussion_id]}

Usage:
    python discover_ajax.py <start_qid> <end_qid> [stride]

A stride > 1 samples the range instead of scanning it exhaustively. Question
ids for one exam arrive in contiguous blocks, so a coarse stride pass cheaply
locates the blocks; the windows around the hits can then be filled in densely.
"""
import json
import re
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import requests
from tqdm import tqdm

from examtopics.settings import BASE_URL, REQUEST_HEADERS

OUT = Path("qid_index.json")
WORKERS = 24
TIMEOUT = 45

TITLE_RE = re.compile(
    r'data-title="Exam\s+([A-Za-z0-9\-]+)\s+topic\s+(\d+)\s+question\s+(\d+)', re.I
)
DID_RE = re.compile(r'data-discussion-id="(\d+)"')

REFERER = f"{BASE_URL}/exams/microsoft/ai-300/view/"

_tl = threading.local()


def sess() -> requests.Session:
    s = getattr(_tl, "s", None)
    if s is None:
        s = requests.Session()
        s.headers.update(REQUEST_HEADERS)
        _tl.s = s
    return s


def probe(qid):
    """Return (qid, exam, topic, question, discussion_id) or None."""
    url = f"{BASE_URL}/ajax/discussion/exam-question/{qid}"
    for attempt in range(1, 4):
        try:
            r = sess().get(
                url,
                timeout=TIMEOUT,
                headers={"Referer": REFERER, "X-Requested-With": "XMLHttpRequest"},
            )
            if r.status_code != 200:
                return None
            m = TITLE_RE.search(r.text)
            if not m:
                return None
            d = DID_RE.search(r.text)
            return (qid, m.group(1).upper(), int(m.group(2)), int(m.group(3)),
                    d.group(1) if d else None)
        except Exception:  # noqa: BLE001
            time.sleep(attempt)
    return None


def main():
    if len(sys.argv) < 3:
        print("Usage: python discover_ajax.py <start_qid> <end_qid>")
        return
    start, end = int(sys.argv[1]), int(sys.argv[2])
    stride = int(sys.argv[3]) if len(sys.argv) > 3 else 1

    index = {}
    if OUT.exists():
        index = json.loads(OUT.read_text(encoding="utf-8"))
        print(f"Loaded existing index with {len(index)} entries.")

    todo = [q for q in range(start, end + 1, stride) if str(q) not in index]
    print(f"Scanning {len(todo)} question ids ({start}..{end} stride {stride}) via ajax...",
          flush=True)

    done = 0
    with ThreadPoolExecutor(max_workers=WORKERS) as ex:
        futs = {ex.submit(probe, q): q for q in todo}
        with tqdm(total=len(futs), desc="Probing ids", unit="id") as pbar:
            for fut in as_completed(futs):
                v = fut.result()
                if v:
                    index[str(v[0])] = [v[1], v[2], v[3], v[4]]
                done += 1
                if done % 2000 == 0:
                    OUT.write_text(json.dumps(index), encoding="utf-8")
                pbar.update(1)

    OUT.write_text(json.dumps(index), encoding="utf-8")

    from collections import Counter
    c = Counter(v[0] for v in index.values())
    print(f"\nIndex now has {len(index)} mapped question ids.")
    print("Top exams in index:")
    for exam, n in c.most_common(25):
        print(f"  {exam:<14} {n}")


if __name__ == "__main__":
    main()
