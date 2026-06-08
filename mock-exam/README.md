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
build_answer_key.py            # regenerates the consolidated answer keys
my_answers.json                # Kiro's suggested answers + rationales (answer key)
ANSWER_KEYS.md                 # community vs Kiro answer, all exams, as tables
AI-300 questions.txt           # extracted questions (one menu per exam)
AI-103 questions.txt
AZ-400 questions.txt
AI-300 answer key.txt          # per-exam answer key (community | Kiro)
AI-103 answer key.txt
AZ-400 answer key.txt
AI-300 answers.txt             # answer-evidence report (official/community/comments)
AI-300 answers.csv             # answer summary with confidence per question
generated-AI-300_transcripts/  # course transcripts/notes + ai300_mock_exam.html
generated-AI-103_transcripts/  # course transcripts / notes for AI-103
```

There are two distinct exam pages in this folder:

- `mock_exam.html` — the **ExamTopics-extracted** multi-exam study tool
  (AI-103 / AI-300 / AZ-400 dropdown, community + Kiro answers, grading).
- `generated-AI-300_transcripts/ai300_mock_exam.html` — an **original AI-300
  practice exam** built from the AI-300T00 lecture transcripts and the
  Microsoft Learn blueprint (Sets A/B/C + case studies, timed 50-question mode,
  study mode). Set C is harder, ExamTopics-calibrated practice.

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

## Hosted (Netlify)

Both pages are deployed as separate Netlify sites (account: ougabriel@gmail.com,
team GDG-MPAPE):

| Exam page | Live URL | Site ID |
|-----------|----------|---------|
| ExamTopics multi-exam (`mock_exam.html`) | https://examtopics-exam-prep.netlify.app | `07a30a50-2cbd-488e-9541-d99fd95d4cc0` |
| AI-300 transcript practice (`generated-AI-300_transcripts/ai300_mock_exam.html`) | https://ai300-practice-exam.netlify.app | `251c7a55-0d0b-46af-822d-28448197a800` |

### Redeploy after changes

Each page is a single self-contained HTML file. Copy it into a folder as
`index.html` and deploy to the matching site by ID:

```
# ExamTopics multi-exam page
mkdir deploy-examtopics
copy mock_exam.html deploy-examtopics\index.html
netlify deploy --dir deploy-examtopics --prod --site 07a30a50-2cbd-488e-9541-d99fd95d4cc0

# AI-300 transcript practice page
mkdir deploy-ai300
copy generated-AI-300_transcripts\ai300_mock_exam.html deploy-ai300\index.html
netlify deploy --dir deploy-ai300 --prod --site 251c7a55-0d0b-46af-822d-28448197a800
```

Always deploy with `--site <id>` so the two sites never overwrite each other.
Delete any stray `.netlify/` folder before deploying — the CLI walks up parent
directories and will reuse a link it finds there.

