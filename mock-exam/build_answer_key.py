"""Generate a consolidated answer key per exam.

For every question it lists:
  - Community most-voted answer (from "<EXAM> questions.txt")
  - Kiro's suggested answer (from my_answers.json), if reviewed

Outputs "<EXAM> answer key.txt" and a combined "ANSWER_KEYS.md".

Usage:
    python build_answer_key.py
"""
import json
import re
from pathlib import Path

from build_mock_exam import parse_questions_file  # reuse the parser

MY_ANSWERS = "my_answers.json"


def load_my_answers():
    p = Path(MY_ANSWERS)
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else {}


def main():
    my = load_my_answers()
    files = sorted(Path(".").glob("* questions.txt"))
    if not files:
        print("No '<EXAM> questions.txt' files found.")
        return

    md_lines = ["# Answer Keys", "",
                "Community = ExamTopics community most-voted answer (from discussion pages).",
                "Kiro = Kiro's suggested answer (Microsoft Learn reasoning; study aid, not official).",
                "A blank means no data (no community votes, or not yet reviewed).", ""]

    for f in files:
        exam, questions = parse_questions_file(Path(f))
        rows = []
        agree = disagree = both = 0
        for q in questions:
            key = f"{exam}|T{q['topic']}|Q{q['question']}"
            comm = q.get("community") or ""
            mine = (my.get(key) or {}).get("answer") or ""
            if comm and mine:
                both += 1
                cu = re.sub(r"[^A-Z]", "", comm.upper())
                mu = re.sub(r"[^A-Z]", "", mine.upper())
                if cu and mu:
                    if cu == mu:
                        agree += 1
                    else:
                        disagree += 1
            rows.append((q["topic"], q["question"], comm, mine))

        # per-exam text file
        out = Path(f"{exam} answer key.txt")
        with out.open("w", encoding="utf-8") as fh:
            fh.write(f"{exam} - Answer Key ({len(rows)} questions)\n")
            fh.write("Format: Topic.Question | Community | Kiro\n")
            fh.write("=" * 50 + "\n\n")
            for t, qn, comm, mine in rows:
                fh.write(f"T{t} Q{qn:<3} | community: {comm or '-':<5} | Kiro: {mine or '-'}\n")

        print(f"{exam}: {len(rows)} questions, "
              f"{sum(1 for r in rows if r[2])} community, "
              f"{sum(1 for r in rows if r[3])} Kiro "
              f"(of {both} with both: {agree} agree, {disagree} differ)")

        # markdown table section
        md_lines.append(f"## {exam}")
        md_lines.append("")
        md_lines.append("| Topic | Q | Community | Kiro |")
        md_lines.append("|------:|--:|:---------:|:----:|")
        for t, qn, comm, mine in rows:
            md_lines.append(f"| {t} | {qn} | {comm or '—'} | {mine or '—'} |")
        md_lines.append("")

    Path("ANSWER_KEYS.md").write_text("\n".join(md_lines), encoding="utf-8")
    print("\nWrote per-exam '<EXAM> answer key.txt' files and ANSWER_KEYS.md")


if __name__ == "__main__":
    main()
