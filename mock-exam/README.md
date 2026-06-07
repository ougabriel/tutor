# Mock Exam (study tool)

Self-contained, offline study page built from the questions extracted by the
ExamTopics scraper (in the repo root). It is intentionally separated from the
scraper so the two concerns stay clean:

- **repo root** = the ExamTopics scraper + question/answer extractors.
- **this folder** = the offline mock-exam study tool and its data.

## Contents

```
mock_exam.html                 # open this in a browser - no server needed
build_mock_exam.py             # regenerates mock_exam.html from the data files
my_answers.json                # Kiro's suggested answers + rationales (answer key)
AI-300 questions.txt           # extracted questions (one menu per exam)
AI-103 questions.txt
AI-300 answers.txt             # answer-evidence report (official/community/comments)
AI-300 answers.csv             # answer summary with confidence per question
generated-AI-300_transcripts/  # course transcripts / notes for AI-300
generated-AI-103_transcripts/  # course transcripts / notes for AI-103
```

## Use

Just open `mock_exam.html` in any browser.

- Pick an exam from the dropdown (or sidebar). Each exam is its own menu;
  questions are never mixed between exams.
- Select answers, then click **Grade exam** to score against the suggested key.
- "Show answer" reveals Kiro's suggested answer + rationale and the community
  most-voted answer.

## Regenerate the page

After editing `my_answers.json` or adding more `<EXAM> questions.txt` files to
this folder, rebuild:

```
python build_mock_exam.py
```

It auto-discovers every `* questions.txt` in this folder and gives each its own
menu. Open the refreshed `mock_exam.html` (hard-refresh with Ctrl+F5 if the
browser shows a cached copy).

## Notes on answers

- "Kiro's suggested answer" is reasoning-based (Microsoft Learn knowledge), not
  an official ExamTopics key. Treat it as a study aid.
- HOTSPOT / drag-drop questions have image-based answers, so they show the
  question text but no letter key and are not graded.
- See `../EXTRACTION_NOTES.md` for how the questions and answer evidence were
  obtained.
