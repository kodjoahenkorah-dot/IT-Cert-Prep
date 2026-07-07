// Study Mode: one question at a time, untimed, with immediate feedback.
// Each answer is graded by POST /study/grade so the explanation shows at once.

const QUESTIONS = JSON.parse(document.getElementById("study-data").textContent);
const root = document.getElementById("study-root");

// Per-question state: { answer, graded:bool, correct:bool }
const state = QUESTIONS.map(() => ({ answer: undefined, graded: false, correct: false }));
let current = 0;
let correctCount = 0;

function el(tag, attrs = {}, ...children) {
  const node = document.createElement(tag);
  for (const [k, v] of Object.entries(attrs)) {
    if (k === "class") node.className = v;
    else if (k === "html") node.innerHTML = v;
    else node.setAttribute(k, v);
  }
  for (const c of children) {
    if (c == null) continue;
    node.appendChild(typeof c === "string" ? document.createTextNode(c) : c);
  }
  return node;
}

function header(q) {
  const tag = q.is_pbq ? "PBQ" : (q.multi ? "Multiple response" : "Multiple choice");
  return el("div", { class: "q-head" },
    el("span", { class: "q-num" }, `Question ${q.number}`),
    el("span", { class: "q-tag" }, tag),
    el("span", { class: "q-dom" }, `Domain ${q.domain} · ${q.objective}`)
  );
}

function selectFor(options, placeholder, value, onChange) {
  const sel = el("select", { class: "pbq-select" });
  sel.appendChild(el("option", { value: "" }, placeholder));
  options.forEach((o) => {
    const opt = el("option", { value: o.id }, o.text);
    if (o.id === value) opt.selected = true;
    sel.appendChild(opt);
  });
  sel.addEventListener("change", () => onChange(sel.value));
  return sel;
}

// Auto-grade the instant the answer is complete:
//   multiple_choice  -> as soon as an option is clicked
//   multiple_response-> as soon as the required number of options is selected
//   matching/categorize -> when every prompt/item has an assignment
//   ordering         -> when every item has a position
function maybeAutoGrade(q, st) {
  if (st.graded) return;
  const a = st.answer;
  let complete = false;
  if (q.type === "multiple_choice") complete = a !== undefined && a !== "";
  else if (q.type === "multiple_response") complete = Array.isArray(a) && a.length >= (q.n_correct || 2);
  else if (q.type === "pbq_matching") complete = a && Object.keys(a).length === q.prompts.length;
  else if (q.type === "pbq_categorize") complete = a && Object.keys(a).length === q.items.length;
  else if (q.type === "pbq_ordering") complete = Array.isArray(a) && a.length === q.items.length;
  if (complete) checkAnswerCached(q, st);
}

function renderInputs(q, st, disabled) {
  if (q.type === "multiple_choice" || q.type === "multiple_response") {
    const wrap = el("div", { class: "q-options" });
    q.options.forEach((o) => {
      const input = el("input", { type: q.multi ? "checkbox" : "radio", name: q.id, value: o.id });
      if (disabled) input.disabled = true;
      const chosen = q.multi ? (st.answer || []).includes(o.id) : st.answer === o.id;
      if (chosen) input.checked = true;
      input.addEventListener("change", () => {
        if (q.multi) {
          const set = new Set(st.answer || []);
          input.checked ? set.add(o.id) : set.delete(o.id);
          st.answer = [...set];
        } else {
          st.answer = o.id;
        }
        maybeAutoGrade(q, st);
      });
      wrap.appendChild(el("label", { class: "opt-choice" }, input, el("span", {}, o.text)));
    });
    return wrap;
  }
  if (q.type === "pbq_matching") {
    if (!st.answer) st.answer = {};
    const wrap = el("div", { class: "pbq" });
    q.prompts.forEach((p) => {
      wrap.appendChild(el("div", { class: "pbq-row" },
        el("span", { class: "pbq-prompt" }, p.text),
        selectFor(q.targets, "— choose —", st.answer[p.id], (val) => {
          if (val) st.answer[p.id] = val; else delete st.answer[p.id];
          maybeAutoGrade(q, st);
        })));
    });
    return wrap;
  }
  if (q.type === "pbq_categorize") {
    if (!st.answer) st.answer = {};
    const wrap = el("div", { class: "pbq" });
    q.items.forEach((it) => {
      wrap.appendChild(el("div", { class: "pbq-row" },
        el("span", { class: "pbq-prompt" }, it.text),
        selectFor(q.categories, "— choose category —", st.answer[it.id], (val) => {
          if (val) st.answer[it.id] = val; else delete st.answer[it.id];
          maybeAutoGrade(q, st);
        })));
    });
    return wrap;
  }
  if (q.type === "pbq_ordering") {
    if (!st.answer) st.answer = [];
    const positions = q.items.map((_, i) => ({ id: String(i + 1), text: String(i + 1) }));
    const picks = {};
    st.answer.forEach((iid, idx) => { picks[iid] = String(idx + 1); });
    const wrap = el("div", { class: "pbq" });
    function recompute() {
      st.answer = Object.entries(picks).filter(([, p]) => p)
        .sort((a, b) => Number(a[1]) - Number(b[1])).map(([iid]) => iid);
    }
    q.items.forEach((it) => {
      wrap.appendChild(el("div", { class: "pbq-row" },
        selectFor(positions, "#", picks[it.id], (val) => { picks[it.id] = val; recompute(); maybeAutoGrade(q, st); }),
        el("span", { class: "pbq-prompt" }, it.text)));
    });
    return wrap;
  }
}

// Build the feedback block from the server's grade_one() detail payload.
function renderFeedback(q, result) {
  const box = el("div", { class: `study-feedback ${result.is_correct ? "ok" : "no"}` });
  box.appendChild(el("div", { class: "study-verdict" },
    result.is_correct ? "✓ Correct" : "✗ Not quite"));

  const d = result.detail;
  if (q.type === "multiple_choice" || q.type === "multiple_response") {
    const ul = el("ul", { class: "opt-list" });
    d.options.forEach((o) => {
      const li = el("li", { class: `opt ${o.correct ? "is-correct" : ""} ${o.chosen ? "is-chosen" : ""}` });
      let mark = "•";
      if (o.correct && o.chosen) mark = "✓ your answer (correct)";
      else if (o.correct) mark = "✓ correct answer";
      else if (o.chosen) mark = "✗ you chose this";
      li.appendChild(el("span", { class: "opt-mark" }, mark));
      li.appendChild(el("span", { class: "opt-text" }, o.text));
      li.appendChild(el("span", { class: "opt-rationale" }, o.rationale));
      ul.appendChild(li);
    });
    box.appendChild(ul);
  } else {
    const table = el("table", { class: "pbq-review" });
    const head = q.type === "pbq_ordering" ? ["#", "Your answer", "Correct", "Why"]
      : [(q.type === "pbq_matching" ? "Prompt" : "Item"), "Your answer", "Correct", "Why"];
    table.appendChild(el("tr", {}, ...head.map((h) => el("th", {}, h))));
    d.rows.forEach((row) => {
      const tr = el("tr", { class: row.ok ? "ok" : "no" });
      const first = q.type === "pbq_ordering" ? String(row.position)
        : (q.type === "pbq_matching" ? row.prompt : row.item);
      tr.appendChild(el("td", {}, first));
      tr.appendChild(el("td", { class: row.ok ? "" : "cell-no" }, row.yours));
      tr.appendChild(el("td", { class: "cell-ok" }, row.correct));
      tr.appendChild(el("td", { class: "why" }, row.rationale));
      table.appendChild(tr);
    });
    box.appendChild(table);
  }

  box.appendChild(el("div", { class: "explanation" },
    el("strong", {}, "Explanation: "), result.explanation));
  return box;
}

function hasAnswer(st) {
  const v = st.answer;
  if (Array.isArray(v)) return v.length > 0;
  if (v && typeof v === "object") return Object.keys(v).length > 0;
  return v !== undefined && v !== "";
}

// Grade one question, cache its feedback node so re-renders don't refetch.
async function checkAnswerCached(q, st) {
  if (!hasAnswer(st)) { alert("Choose an answer first (or skip with Next)."); return; }
  const res = await fetch("/study/grade", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ id: q.id, answer: st.answer }),
  });
  const result = await res.json();
  st.graded = true;
  st.correct = result.is_correct;
  st.feedbackNode = renderFeedback(q, result);
  if (result.is_correct) correctCount += 1;
  document.getElementById("score").textContent = `${correctCount} correct`;
  render();
}

function renderQ() {
  root.innerHTML = "";
  const q = QUESTIONS[current];
  const st = state[current];
  const card = el("article", { class: "q-card" });
  card.appendChild(header(q));
  if (q.stem) card.appendChild(el("p", { class: "q-stem" }, q.stem));
  if (q.type === "pbq_ordering")
    card.appendChild(el("p", { class: "pbq-hint" }, "Assign a position number to each item (1 = first)."));
  card.appendChild(renderInputs(q, st, st.graded));

  if (!st.graded) {
    // Answers grade themselves the moment they're complete — no button needed.
    const hint = q.multi
      ? `Select ${q.n_correct || "all"} answers — grading is instant once you've chosen.`
      : (q.is_pbq ? "Grading is instant once every part is filled in."
                  : "Click an answer — grading is instant.");
    card.appendChild(el("p", { class: "pbq-hint" }, hint));
  } else if (st.feedbackNode) {
    card.appendChild(st.feedbackNode);
  }
  root.appendChild(card);

  document.getElementById("progress").textContent = `${current + 1} / ${QUESTIONS.length}`;
  document.getElementById("prev-btn").disabled = current === 0;
  const next = document.getElementById("next-btn");
  next.textContent = current === QUESTIONS.length - 1 ? "Finish" : "Next →";
}

document.getElementById("prev-btn").addEventListener("click", () => {
  if (current > 0) { current -= 1; renderQ(); }
});
document.getElementById("next-btn").addEventListener("click", () => {
  if (current < QUESTIONS.length - 1) { current += 1; renderQ(); }
  else window.location = "/study";
});

renderQ();
