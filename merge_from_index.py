"""Merge questions discovered by discover_ajax.py into the mock-exam files.

Reads qid_index.json (built by discover_ajax.py), finds the entries for the
requested exam that are NOT already present in
"mock-exam/<EXAM> questions.txt", fetches only those discussion pages, parses
them, and rewrites the exam file with everything sorted by topic/question.

Usage:
    python merge_from_index.py AI-300 [SC-200 ...]
    python merge_from_index.py --all
"""
import json
import re
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from tqdm import tqdm

import extract_all_questions as ex
from examtopics.settings import BASE_URL

INDEX = Path("qid_index.json")
MOCK = Path("mock-exam")
SEP = "=" * 70


def parse_existing(path: Path):
    """Return {(topic, question): full_block_text} for an exam file."""
    if not path.exists():
        return {}
    raw = path.read_text(encoding="utf-8")
    chunks = raw.split(SEP)
    out = {}
    i = 0
    while i < len(chunks):
        header = chunks[i]
        m = re.search(r"Topic\s+(\d+)\s*-\s*Question\s+(\d+)", header)
        if m and i + 1 < len(chunks):
            key = (int(m.group(1)), int(m.group(2)))
            out[key] = (header.strip("\n"), chunks[i + 1].strip("\n"))
            i += 2
        else:
            i += 1
    return out


def fetch_one(did, exam_label):
    url = f"{BASE_URL}/discussions/microsoft/view/{did}-x/"
    try:
        r = ex.get(url)
        if r.status_code != 200:
            return None
        return ex.parse_question_page(r.text, r.url, exam_label)
    except Exception:  # noqa: BLE001
        return None


def do_exam(exam_label, index):
    path = MOCK / f"{exam_label} questions.txt"
    existing = parse_existing(path)

    wanted = {}
    for qid, (exam, topic, question, did) in index.items():
        if exam == exam_label and did:
            wanted[(topic, question)] = did

    missing = {k: v for k, v in wanted.items() if k not in existing}
    print(f"\n=== {exam_label} ===")
    print(f"  local: {len(existing)}   indexed: {len(wanted)}   to fetch: {len(missing)}")
    if not missing:
        print("  nothing new.")
        return 0

    # warm a session/cookies
    ex._session_cookies = None
    referer = f"{BASE_URL}/exams/microsoft/{exam_label.lower()}/view/"
    got = {}
    with ThreadPoolExecutor(max_workers=12) as pool:
        futs = {pool.submit(fetch_one, did, exam_label): key
                for key, did in missing.items()}
        with tqdm(total=len(futs), desc=f"Fetching {exam_label}", unit="q") as pbar:
            for fut in as_completed(futs):
                item = fut.result()
                if item and item.get("exam", "").upper() == exam_label:
                    got[(item["topic"], item["question_no"])] = item
                pbar.update(1)

    print(f"  fetched OK: {len(got)}")
    if not got:
        return 0

    # build new file: existing blocks + newly formatted blocks, sorted
    blocks = dict(existing)
    for key, item in got.items():
        text = ex.format_question(item)
        parts = text.split(SEP)
        # format_question emits: SEP header SEP body
        if len(parts) >= 3:
            blocks[key] = (parts[1].strip("\n"), parts[2].strip("\n"))

    ordered = sorted(blocks)
    out = []
    out.append(f"{exam_label} - Extracted Questions ({len(ordered)})")
    out.append("Source: ExamTopics question/discussion pages")
    out.append("")
    for key in ordered:
        header, body = blocks[key]
        out.append(SEP)
        out.append(header)
        out.append(SEP)
        out.append(body)
        out.append("")
    path.write_text("\n".join(out), encoding="utf-8")
    print(f"  wrote {path.name}: {len(existing)} -> {len(ordered)} (+{len(ordered)-len(existing)})")
    return len(ordered) - len(existing)


def main():
    if not INDEX.exists():
        print("qid_index.json not found - run discover_ajax.py first.")
        return
    index = {k: tuple(v) for k, v in json.loads(INDEX.read_text(encoding="utf-8")).items()}

    args = sys.argv[1:]
    if not args:
        print(__doc__)
        return

    if args[0] == "--all":
        labels = sorted({v[0] for v in index.values()})
        # only exams we actually track locally
        local = {p.name.replace(" questions.txt", "") for p in MOCK.glob("* questions.txt")}
        labels = [l for l in labels if l in local]
    else:
        labels = [a.upper() for a in args]

    total = 0
    for label in labels:
        total += do_exam(label, index)
    print(f"\nTOTAL new questions merged: {total}")


if __name__ == "__main__":
    main()
