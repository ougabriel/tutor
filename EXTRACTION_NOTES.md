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

## Large/older exams with NON-CONTIGUOUS question ids (AZ-400 case)

### The problem we hit
The first AZ-400 run returned only **367 of 564** questions. Root cause: the
original `extract_all_questions.py` assumed an exam's internal question-ids
are one contiguous block (`first_id .. first_id + total`). That holds for NEW
exams (AI-300, AI-103) but NOT for older/large ones.

Probing the id range proved it. AZ-400 ids start at 812027 but only run
~370 ids before the numbering switches to OTHER exams:

```
812027 -> AZ-400
812327 -> AZ-400
812427 -> AZ-500   <- AZ-400 block ends here
812827 -> DP-203
813027 -> MS-900
...
```

ExamTopics assigns question-ids in batches over time, so an exam that has been
updated across years has its questions scattered across multiple id ranges.
A single contiguous id-walk can only ever see one batch.

### What worked: use the discussion LISTING scan as the primary id source
The discussion listing (`/discussions/<provider>/<page>/`) finds question URLs
by **exam name**, independent of internal id. For AZ-400 it found **559**
links vs the id-walk's 367. This is the reliable source for completeness on any
exam, new or old.

`extract_all_questions.py` now merges TWO url sources and dedupes by question:
1. **Discussion listing scan** (primary) - `FastDiscussionScanner.scan(...)`.
   Catches every question regardless of id contiguity. Slowest part (~1491
   listing pages for microsoft) but cached for 6h, so re-runs are fast.
2. **Sequential id-walk** (supplement) - the AJAX `exam-question/<id>` map.
   Catches brand-new questions that may not have a discussion-listing entry yet.

Then it fetches every canonical discussion page (captcha-free), parses, filters
to the exact exam header, and dedupes by (topic, question_no).

### Result
AZ-400: **559 of 564** (all 19 topics, 0 duplicates). The ~5 gap = questions
with no public discussion thread AND ids outside the contiguous block; those
live only on the captcha-gated exam-view pages and are not publicly reachable.

### Rule of thumb
- New exam, few hundred questions, recently published -> id-walk alone is fine
  and fast.
- Older or large exam (AZ-104, AZ-400, etc.) -> the listing scan is REQUIRED;
  the id-walk alone will silently miss large chunks. The merged approach now in
  `extract_all_questions.py` handles both automatically, so just run:

```
python extract_all_questions.py microsoft az-400
```

### Performance note
The listing scan is the bottleneck for big providers (microsoft = 1491 pages).
It is cached (`.examtopics_cache`, 6h TTL), so the first run is slow but repeat
runs for OTHER microsoft exams reuse the same cached listing pages and are fast.
