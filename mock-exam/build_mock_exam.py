"""Build an interactive mock-exam HTML page from the extracted question files.

Each exam (AI-300, AI-103, ...) becomes its OWN menu entry. Questions are
never mixed between exams. Selecting an exam in the sidebar shows only that
exam's questions.

For each question the page shows:
  * the question text and answer choices
  * the community most-voted answer (from extraction), if any
  * "Kiro's suggested answer" + rationale, loaded from my_answers.json
    (keyed by "<EXAM>|T<topic>|Q<question>"). Questions without an entry are
    shown as "Not yet reviewed".

Usage:
    python build_mock_exam.py
"""
import html
import json
import re
from pathlib import Path

QUESTION_FILE_GLOB = "* questions.txt"
MY_ANSWERS_FILE = "my_answers.json"
OUTPUT_FILE = "mock_exam.html"

SEP = "=" * 70


def parse_questions_file(path: Path):
    """Return (exam_label, [question dicts]) for one '<EXAM> questions.txt'."""
    raw = path.read_text(encoding="utf-8")
    exam_label = path.name.replace(" questions.txt", "").strip()

    # Split on the 70-char separator. Pattern repeats: header, body, header, ...
    chunks = [c for c in raw.split(SEP)]
    questions = []
    # Walk chunks looking for a header chunk (contains "Topic N - Question M")
    i = 0
    while i < len(chunks):
        header = chunks[i]
        m = re.search(r"Topic\s+(\d+)\s*-\s*Question\s+(\d+)", header)
        if m and i + 1 < len(chunks):
            topic = int(m.group(1))
            qno = int(m.group(2))
            url_m = re.search(r"(https?://\S+)", header)
            url = url_m.group(1) if url_m else ""
            body = chunks[i + 1].strip("\n")
            questions.append(parse_body(topic, qno, url, body))
            i += 2
        else:
            i += 1
    questions.sort(key=lambda q: (q["topic"], q["question"]))
    return exam_label, questions


def parse_body(topic, qno, url, body):
    lines = body.split("\n")
    choice_re = re.compile(r"^([A-Z])\.\s+(.*)$")
    suggested_re = re.compile(r"^Suggested Answer.*?:\s*(.+)$", re.I)

    text_lines, choices = [], []
    community = None
    seen_choice = False
    for line in lines:
        sm = suggested_re.match(line.strip())
        if sm:
            community = sm.group(1).strip()
            continue
        cm = choice_re.match(line.strip())
        if cm:
            seen_choice = True
            choices.append({"letter": cm.group(1), "text": cm.group(2).strip()})
            continue
        if not seen_choice:
            text_lines.append(line)

    question_text = "\n".join(text_lines).strip()
    qtype = "multiple-choice"
    head = question_text[:40].upper()
    if not choices:
        if "HOTSPOT" in head or "DRAG DROP" in head or "DRAG-DROP" in head:
            qtype = "hotspot/drag-drop (image answer)"
        else:
            qtype = "no text choices"
    return {
        "topic": topic,
        "question": qno,
        "url": url,
        "text": question_text,
        "choices": choices,
        "community": community,
        "type": qtype,
    }


def load_my_answers():
    p = Path(MY_ANSWERS_FILE)
    if p.exists():
        return json.loads(p.read_text(encoding="utf-8"))
    return {}


def load_images():
    p = Path("question_images.json")
    if p.exists():
        return json.loads(p.read_text(encoding="utf-8"))
    return {}


def answer_key(exam, q):
    return f"{exam}|T{q['topic']}|Q{q['question']}"


def build_html(exams, my_answers, images):
    # exams: list of (label, questions)
    data = {}
    for label, questions in exams:
        data[label] = []
        for q in questions:
            key = answer_key(label, q)
            mine = my_answers.get(key, {})
            data[label].append({
                "key": key,
                "topic": q["topic"],
                "question": q["question"],
                "url": q["url"],
                "text": q["text"],
                "choices": q["choices"],
                "community": q["community"],
                "type": q["type"],
                "images": images.get(key, []),
                "kiro_answer": mine.get("answer"),
                "kiro_rationale": mine.get("rationale"),
            })

    payload = json.dumps(data, ensure_ascii=False)

    return PAGE_TEMPLATE.replace("/*__DATA__*/", payload)


PAGE_TEMPLATE = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Mock Exam</title>
<style>
  :root { --bg:#0f1419; --panel:#1a212b; --panel2:#222c38; --line:#2e3a48;
          --text:#e6edf3; --muted:#8b98a5; --accent:#4c9aff; --good:#3fb950;
          --warn:#d29922; --pick:#1f6feb; }
  * { box-sizing: border-box; }
  body { margin:0; font-family:-apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif;
         background:var(--bg); color:var(--text); display:flex; min-height:100vh; }
  #sidebar { width:240px; background:var(--panel); border-right:1px solid var(--line);
             padding:18px 14px; flex-shrink:0; position:sticky; top:0; height:100vh; overflow:auto; }
  #sidebar h1 { font-size:16px; margin:0 0 16px; }
  .exam-btn { display:block; width:100%; text-align:left; padding:11px 12px; margin-bottom:8px;
              background:var(--panel2); color:var(--text); border:1px solid var(--line);
              border-radius:8px; cursor:pointer; font-size:14px; }
  .exam-btn:hover { border-color:var(--accent); }
  .exam-btn.active { background:var(--pick); border-color:var(--pick); }
  .exam-btn small { display:block; color:var(--muted); margin-top:3px; }
  .exam-btn.active small { color:#cfe2ff; }
  #main { flex:1; padding:26px 34px; max-width:1000px; }
  #exam-title { margin:0 0 4px; font-size:24px; }
  #exam-sub { color:var(--muted); margin:0 0 18px; font-size:13px; }
  .toolbar { display:flex; gap:10px; align-items:center; margin-bottom:18px; flex-wrap:wrap; }
  .toolbar input { background:var(--panel2); border:1px solid var(--line); color:var(--text);
                   padding:8px 10px; border-radius:7px; width:240px; }
  .toolbar button { background:var(--panel2); border:1px solid var(--line); color:var(--text);
                    padding:8px 12px; border-radius:7px; cursor:pointer; }
  .toolbar button:hover { border-color:var(--accent); }
  .qcard { background:var(--panel); border:1px solid var(--line); border-radius:10px;
           padding:18px 20px; margin-bottom:16px; }
  .qhead { display:flex; justify-content:space-between; align-items:center; margin-bottom:10px; }
  .qhead .qid { font-weight:600; color:var(--accent); }
  .qhead .qtype { font-size:11px; color:var(--muted); border:1px solid var(--line);
                  padding:2px 8px; border-radius:20px; }
  .qtext { white-space:pre-wrap; line-height:1.5; margin-bottom:14px; font-size:14px; }
  .qimages { margin:4px 0 14px; }
  .qimages img { max-width:100%; border:1px solid var(--line); border-radius:8px;
                 background:#fff; margin:6px 0; display:block; cursor:zoom-in; }
  .qimages .imglabel { font-size:11px; color:var(--muted); margin-bottom:4px; }
  .choice { padding:9px 12px; border:1px solid var(--line); border-radius:8px; margin-bottom:7px;
            cursor:pointer; font-size:14px; }
  .choice:hover { border-color:var(--accent); }
  .choice.selected { border-color:var(--pick); background:rgba(31,111,235,.15); }
  .choice .ltr { font-weight:700; margin-right:8px; }
  .reveal { margin-top:6px; }
  .reveal button { background:var(--panel2); border:1px solid var(--line); color:var(--text);
                   padding:7px 12px; border-radius:7px; cursor:pointer; font-size:13px; }
  .answers { margin-top:12px; border-top:1px dashed var(--line); padding-top:12px; display:none; }
  .answers.show { display:block; }
  .ans-row { margin-bottom:8px; font-size:14px; }
  .ans-row .lbl { color:var(--muted); display:inline-block; min-width:170px; }
  .pill { display:inline-block; font-weight:700; padding:1px 9px; border-radius:6px; }
  .pill.kiro { background:rgba(63,185,80,.18); color:var(--good); border:1px solid var(--good); }
  .pill.comm { background:rgba(76,154,255,.16); color:var(--accent); border:1px solid var(--accent); }
  .pill.none { background:transparent; color:var(--muted); border:1px solid var(--line); }
  .rationale { font-size:13px; color:#cdd7e0; line-height:1.5; margin-top:6px;
               background:var(--panel2); padding:10px 12px; border-radius:8px; }
  .choice.kiro-correct { border-color:var(--good); background:rgba(63,185,80,.12); }
  .choice.graded-correct { border-color:var(--good); background:rgba(63,185,80,.18); }
  .choice.graded-wrong { border-color:#f85149; background:rgba(248,81,73,.16); }
  .choice .mark { float:right; font-weight:700; }
  .scorebar { display:none; background:var(--panel2); border:1px solid var(--line);
              border-radius:10px; padding:14px 18px; margin-bottom:18px; font-size:15px; }
  .scorebar.show { display:block; }
  .scorebar .pct { font-size:26px; font-weight:700; }
  .scorebar .bd { color:var(--muted); font-size:13px; margin-top:6px; }
  .qcard.q-correct { border-left:4px solid var(--good); }
  .qcard.q-wrong { border-left:4px solid #f85149; }
  .qcard.q-skipped { border-left:4px solid var(--warn); }
  .qcard.q-nokey { border-left:4px solid var(--line); }
  a.src { color:var(--muted); font-size:12px; text-decoration:none; }
  a.src:hover { color:var(--accent); }
  .empty { color:var(--muted); }
  .exam-picker { display:flex; align-items:center; gap:10px; margin-bottom:16px; }
  .exam-picker label { color:var(--muted); font-size:14px; }
  .exam-picker select { background:var(--panel2); color:var(--text); border:1px solid var(--line);
                        border-radius:8px; padding:9px 12px; font-size:15px; min-width:260px; cursor:pointer; }
  .exam-picker select:hover { border-color:var(--accent); }
</style>
</head>
<body>
  <nav id="sidebar">
    <h1>Mock Exams</h1>
    <div id="exam-list"></div>
  </nav>
  <main id="main">
    <div class="exam-picker">
      <label for="exam-select">Choose exam:</label>
      <select id="exam-select"></select>
    </div>
    <h2 id="exam-title"></h2>
    <p id="exam-sub"></p>
    <div class="toolbar">
      <input id="search" placeholder="Filter questions...">
      <button id="reveal-all">Reveal all answers</button>
      <button id="hide-all">Hide all answers</button>
      <button id="grade-btn">Grade exam</button>
      <button id="reset-btn">Reset answers</button>
    </div>
    <div id="scorebar" class="scorebar"></div>
    <div id="questions"></div>
  </main>

<script>
const DATA = /*__DATA__*/;
const examLabels = Object.keys(DATA);
let current = examLabels[0];
const selections = {};   // key -> Set of chosen letters
let graded = false;

function el(tag, cls, html){ const e=document.createElement(tag); if(cls)e.className=cls; if(html!=null)e.innerHTML=html; return e; }
function esc(s){ return (s||"").replace(/[&<>]/g, c=>({"&":"&amp;","<":"&lt;",">":"&gt;"}[c])); }

function renderSidebar(){
  const list = document.getElementById("exam-list");
  list.innerHTML = "";
  examLabels.forEach(label=>{
    const qs = DATA[label];
    const reviewed = qs.filter(q=>q.kiro_answer).length;
    const btn = el("button","exam-btn"+(label===current?" active":""));
    btn.innerHTML = esc(label)+"<small>"+qs.length+" questions &middot; "+reviewed+" reviewed</small>";
    btn.onclick = ()=>{ selectExam(label); };
    list.appendChild(btn);
  });
  const sel = document.getElementById("exam-select");
  if(sel && sel.value !== current) sel.value = current;
}

function populateDropdown(){
  const sel = document.getElementById("exam-select");
  sel.innerHTML = "";
  examLabels.forEach(label=>{
    const opt = document.createElement("option");
    opt.value = label;
    opt.textContent = label + " (" + DATA[label].length + " questions)";
    sel.appendChild(opt);
  });
  sel.value = current;
  sel.onchange = ()=> selectExam(sel.value);
}

function selectExam(label){
  current = label;
  graded = false;
  document.getElementById("scorebar").classList.remove("show");
  renderSidebar();
  renderExam();
}

function renderExam(){
  const qs = DATA[current];
  document.getElementById("exam-title").textContent = current + " — Mock Exam";
  const reviewed = qs.filter(q=>q.kiro_answer).length;
  const comm = qs.filter(q=>q.community).length;
  document.getElementById("exam-sub").textContent =
    qs.length+" questions in this exam only. "+reviewed+" with Kiro's suggested answer, "+comm+" with a community answer.";
  const wrap = document.getElementById("questions");
  wrap.innerHTML = "";
  const filter = document.getElementById("search").value.toLowerCase();
  qs.forEach(q=>{
    const hay = (q.text+" "+(q.choices||[]).map(c=>c.text).join(" ")).toLowerCase();
    if(filter && !hay.includes(filter)) return;
    wrap.appendChild(renderCard(q));
  });
  if(!wrap.children.length){ wrap.appendChild(el("p","empty","No questions match the filter.")); }
}

function renderCard(q){
  const card = el("div","qcard");
  card.dataset.key = q.key;
  const head = el("div","qhead");
  head.appendChild(el("span","qid","Topic "+q.topic+" · Question "+q.question));
  head.appendChild(el("span","qtype",esc(q.type)));
  card.appendChild(head);

  card.appendChild(el("div","qtext",esc(q.text)));

  // Inline images (HOTSPOT / drag-drop / exhibits) pulled from ExamTopics CDN
  if(q.images && q.images.length){
    const wrap = el("div","qimages");
    wrap.appendChild(el("div","imglabel","Exhibit / drag-drop image"+(q.images.length>1?"s":"")+" (click to open full size):"));
    q.images.forEach(src=>{
      const im = el("img");
      im.src = src;
      im.loading = "lazy";
      im.alt = "Question exhibit image";
      im.onclick = ()=>window.open(src, "_blank");
      wrap.appendChild(im);
    });
    card.appendChild(wrap);
  }

  const kiro = (q.kiro_answer||"").toUpperCase();
  const multi = kiro.length > 1; // e.g. "AD" => choose multiple
  const sel = selections[q.key] || new Set();
  (q.choices||[]).forEach(c=>{
    const ch = el("div","choice");
    ch.innerHTML = "<span class='ltr'>"+esc(c.letter)+".</span>"+esc(c.text);
    ch.dataset.letter = c.letter;
    if(sel.has(c.letter)) ch.classList.add("selected");
    ch.onclick = ()=>{
      const s = selections[q.key] || new Set();
      if(multi){
        if(s.has(c.letter)) s.delete(c.letter); else s.add(c.letter);
      } else {
        const had = s.has(c.letter);
        s.clear();
        if(!had) s.add(c.letter);
      }
      selections[q.key] = s;
      // reflect selection in UI
      card.querySelectorAll(".choice").forEach(o=>{
        o.classList.toggle("selected", s.has(o.dataset.letter));
      });
    };
    card.appendChild(ch);
  });

  const reveal = el("div","reveal");
  const btn = el("button",null,"Show answer");
  const ans = el("div","answers");
  btn.onclick = ()=>{
    ans.classList.toggle("show");
    btn.textContent = ans.classList.contains("show") ? "Hide answer" : "Show answer";
    if(kiro){
      card.querySelectorAll(".choice").forEach(ch=>{
        if(kiro.includes(ch.dataset.letter)) ch.classList.toggle("kiro-correct", ans.classList.contains("show"));
      });
    }
  };
  reveal.appendChild(btn);
  card.appendChild(reveal);

  // Kiro answer
  const kr = el("div","ans-row");
  if(q.kiro_answer){
    kr.innerHTML = "<span class='lbl'>Kiro's suggested answer</span> <span class='pill kiro'>"+esc(q.kiro_answer)+"</span>";
  } else {
    kr.innerHTML = "<span class='lbl'>Kiro's suggested answer</span> <span class='pill none'>Not yet reviewed</span>";
  }
  ans.appendChild(kr);
  if(q.kiro_rationale){ ans.appendChild(el("div","rationale",esc(q.kiro_rationale))); }

  // Community answer
  const cr = el("div","ans-row");
  cr.style.marginTop = "10px";
  if(q.community){
    cr.innerHTML = "<span class='lbl'>Community most-voted</span> <span class='pill comm'>"+esc(q.community)+"</span>";
  } else {
    cr.innerHTML = "<span class='lbl'>Community most-voted</span> <span class='pill none'>no votes</span>";
  }
  ans.appendChild(cr);

  if(q.url){ const a=el("a","src","View source discussion ↗"); a.href=q.url; a.target="_blank"; a.style.display="inline-block"; a.style.marginTop="10px"; ans.appendChild(a); }

  card.appendChild(ans);
  return card;
}

document.getElementById("search").addEventListener("input", renderExam);
document.getElementById("reveal-all").onclick = ()=>document.querySelectorAll(".answers").forEach(a=>{a.classList.add("show");});
document.getElementById("hide-all").onclick = ()=>document.querySelectorAll(".answers").forEach(a=>{a.classList.remove("show");});

function setEq(a, b){
  if(a.size !== b.size) return false;
  for(const x of a) if(!b.has(x)) return false;
  return true;
}

function gradeExam(){
  const qs = DATA[current];
  let correct=0, wrong=0, skipped=0, nokey=0, gradable=0;
  qs.forEach(q=>{
    const kiro = (q.kiro_answer||"").toUpperCase();
    const card = document.querySelector('.qcard[data-key="'+CSS.escape(q.key)+'"]');
    if(!kiro){ nokey++; if(card) markCard(card,"q-nokey"); return; }
    gradable++;
    const want = new Set(kiro.split(""));
    const got = selections[q.key] || new Set();
    if(got.size===0){ skipped++; if(card) markCard(card,"q-skipped"); return; }
    const ok = setEq(want, got);
    if(ok) correct++; else wrong++;
    if(card){
      markCard(card, ok?"q-correct":"q-wrong");
      card.querySelectorAll(".choice").forEach(ch=>{
        const l = ch.dataset.letter;
        ch.classList.remove("graded-correct","graded-wrong");
        if(want.has(l)){ ch.classList.add("graded-correct"); addMark(ch,"✓"); }
        if(got.has(l) && !want.has(l)){ ch.classList.add("graded-wrong"); addMark(ch,"✗"); }
      });
      // open the answer panel so rationale shows
      const ans = card.querySelector(".answers"); if(ans) ans.classList.add("show");
    }
  });
  graded = true;
  showScore(correct, wrong, skipped, nokey, gradable);
}

function markCard(card, cls){
  card.classList.remove("q-correct","q-wrong","q-skipped","q-nokey");
  card.classList.add(cls);
}
function addMark(ch, sym){
  if(ch.querySelector(".mark")) return;
  const m = el("span","mark", sym);
  ch.appendChild(m);
}

function showScore(correct, wrong, skipped, nokey, gradable){
  const attempted = correct + wrong;
  const pct = attempted ? Math.round(100*correct/attempted) : 0;
  const bar = document.getElementById("scorebar");
  bar.classList.add("show");
  bar.innerHTML =
    "<span class='pct'>"+pct+"%</span> &nbsp; ("+correct+" / "+attempted+" attempted correct)" +
    "<div class='bd'>"+correct+" correct · "+wrong+" wrong · "+skipped+
    " skipped · "+gradable+" gradable vs Kiro's key · "+nokey+
    " not gradable (image / not reviewed). Score is against Kiro's suggested answers, not the official key.</div>";
  bar.scrollIntoView({behavior:"smooth", block:"nearest"});
}

function resetAnswers(){
  for(const k in selections) delete selections[k];
  graded = false;
  document.getElementById("scorebar").classList.remove("show");
  renderExam();
}

document.getElementById("grade-btn").onclick = gradeExam;
document.getElementById("reset-btn").onclick = resetAnswers;

populateDropdown();
renderSidebar();
renderExam();
</script>
</body>
</html>
"""


def main():
    files = sorted(Path(".").glob(QUESTION_FILE_GLOB))
    if not files:
        print("No '<EXAM> questions.txt' files found.")
        return
    exams = []
    for f in files:
        label, questions = parse_questions_file(f)
        exams.append((label, questions))
        print(f"Parsed {label}: {len(questions)} questions "
              f"({sum(1 for q in questions if q['choices'])} with text choices)")

    my_answers = load_my_answers()
    images = load_images()
    Path(OUTPUT_FILE).write_text(build_html(exams, my_answers, images), encoding="utf-8")
    print(f"Wrote {OUTPUT_FILE} with {len(exams)} exam menu(s). "
          f"{len(images)} questions have inline images.")


if __name__ == "__main__":
    main()
