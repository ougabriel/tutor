# ExamTopics Full-Question Extraction — Findings

Notes on how to reliably pull **all** questions for an exam, captcha-free.
Written after getting full sets for AI-300 (60/60) and AI-103 (65/65).

## TL;DR

Don't fight the reCAPTCHA on the exam-view pages. Reach the same content
through the site's own (un-gated) discussion AJAX endpoint, walking the
sequential question-id range.

Use: `extract_all_questions.py <provider> <exam-code>`

```
.venv\Scripts\python.exe extract_all_questions.py microsoft ai-300
.venv\Scripts\python.exe extract_all_questions.py microsoft ai-103
```

Output: `<EXAM> questions.txt`

## The three data sources and their catches

1. **Exam-view pages** — `/exams/<provider>/<exam>/view/<N>/`
   - Page 1 is ungated and lists the first 4 questions WITH the official
     "Correct Answer", plus the total question count
     ("Viewing questions 1-4 out of 60 questions").
   - Pages 2..last are blocked by a **Google reCAPTCHA** ("I am not a robot",
     `captcha-container` in the HTML). This is a real anti-bot access control.
   - Tried and FAILED to get past it: plain requests, cookies + Referer,
     Camoufox stealth browser (headless AND visible), in-session navigation
     from page 1. The captcha triggers after a couple of view-page requests
     per session and does not reliably clear. DO NOT try to defeat it.

2. **Discussion listing scan** — what the original `main.py` tool does.
   - Captcha-free, but only finds questions that already have a community
     discussion thread AND show up in the provider listing.
   - Coverage depends on community activity: AI-300 -> 26 found, brand-new
     AI-103 -> only 1 found. Incomplete for newer exams.

3. **Discussion AJAX + canonical discussion pages** — THE WORKING PATH.
   - Captcha-free. Gets every question regardless of discussion activity.

## The working method (no captcha bypass)

The exam page's "Discussion" button calls an internal endpoint the site uses
for its own UI. It is not captcha-gated (the front-end depends on it):

```
GET /ajax/discussion/exam-question/<question_id>
    headers: Referer = the exam view URL, X-Requested-With = XMLHttpRequest
```

Key facts that make this work:

- **Question ids are sequential per exam.** Ungated page 1 gives the first
  id (from `question-body data-id="..."`) and the total count. So the full
  range is known: e.g. AI-300 = 992206..992265 (60), AI-103 = 1000629..1000693 (65).
- The AJAX response contains `data-discussion-id="<id>"`, mapping each
  question id to its discussion id.
- The canonical discussion page is captcha-free and has the full question:
  ```
  /discussions/<provider>/view/<discussion_id>-x/
  ```
  The `-x` slug is wrong on purpose; the server 302-redirects to the correct
  canonical URL (a bare `/view/<id>/` returns 404, so always append `-<slug>`).

### Pipeline
1. GET exam-view page 1 (ungated) -> first question id + total count + cookies.
2. For each id in the sequential range -> AJAX endpoint -> discussion id.
3. GET `/discussions/<provider>/view/<discussion_id>-x/` -> parse question.
4. Keep only rows whose header exam matches (filters out ids that spill into
   the next exam's range), sort by topic/question, write to file.

## Parsing reference (HTML structure)

- Header: `.question-discussion-header` text contains
  `Question #: N` and `Topic #: M`, and `Microsoft's <EXAM>`.
- Question text: `.question-body .card-text` (convert `<br>` to newlines).
- Choices: `.question-choices-container li.multi-choice-item`, letter in
  `.multi-choice-letter[data-choice-letter]`.
- Community answer: `.voted-answers-tally script` (JSON), entry with
  `is_most_voted: true`, field `voted_answers`.

## Known limitations (data, not tooling)

- HOTSPOT / drag-and-drop questions have image/diagram answers, not A/B/C/D
  text — so they show full question text but no letter choices.
- "Suggested Answer" is the COMMUNITY most-voted choice from the discussion,
  not the official ExamTopics answer (that one is login/contributor gated).
  Newer exams have few or no votes (AI-103 had ~1).
- The official "Correct Answer" only appears on exam-view page 1 (4 questions)
  for anonymous users.

## Don'ts

- Don't try to solve/bypass the reCAPTCHA — it's an access control.
- Don't rely on the discussion *listing* scan for completeness on new exams.
- Don't use bare `/view/<id>/` (404). Always append a slug, e.g. `<id>-x/`.

## Files

- `extract_all_questions.py` — the working full extractor (method #3).
- `extract_from_discussions.py` — listing-scan method (#2), captcha-free but
  incomplete on new exams.
- `extract_questions.py` — exam-view method (#1) with interactive captcha
  solving; kept for reference but not recommended.

## Answer evidence (how to confirm correct answers)

Use: `extract_with_evidence.py <provider> <exam-code>`
Outputs `<EXAM> answers.txt` (full evidence) and `<EXAM> answers.csv` (summary).

There are four answer signals, gathered per question:

1. **Official "Correct Answer"** (`.question-answer .correct-answer`) — the
   authoritative answer, but only on the ungated exam-view **page 1** (first
   ~4 questions for anonymous users). Gated for the rest.
2. **Community most-voted** — from `.voted-answers-tally` JSON
   (`voted_answers`, `vote_count`, `is_most_voted`). Captcha-free, per question.
3. **Comment selected-answer tally** — every comment's
   `.comment-selected-answers` ("Selected Answer: X"), counted for consensus.
4. **Top comments** — author, selected answer, `.upvote-count`,
   `.most-voted-answer-badge`, and `.comment-content` (reasoning + reference
   links, often to Microsoft Learn).

### Validation result (why community answers are trustworthy)
On every AI-300 question where BOTH the official answer and a community vote
were visible, they matched (Q1 B=B, Q2 D=D). So where the official answer is
gated, the community most-voted answer is a reliable stand-in — strongest when
vote_count is high and the comment tally agrees.

### Confidence levels emitted
- HIGH        — official answer present (optionally confirmed by community).
- MEDIUM-HIGH — no official, but strong community consensus (>=3 votes/comments).
- LOW         — few votes, or signals disagree (flagged "DISAGREE").
- NONE        — no votes and no comments (question has no community activity).

### Important data reality
For a NEW exam like AI-300, most questions have NO comments/votes at all
(verified: "no comments" + 0 comment containers). So ~45/60 came back NONE.
This is not fixable by scraping — the evidence does not exist yet publicly.
The official answers for those are behind the contributor/login paywall.
The DOP-C02-style older exams will have far more comment evidence.

### The honest bottom line on "confirming" answers
- ~4 questions: confirmed by ExamTopics' own official answer.
- ~6 questions: strong community consensus (multiple votes + agreeing comments).
- ~5 questions: weak/low-confidence community signal.
- ~45 questions: no public answer evidence exists (no votes, no comments,
  official answer paywalled). These genuinely cannot be confirmed from public
  data and need a logged-in contributor account or manual subject-matter review.
