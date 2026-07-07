// Renders the exam client-side from the JSON payload and collects responses.
// Answer key never reaches the browser; grading happens server-side on submit.

const QUESTIONS = JSON.parse(document.getElementById("exam-data").textContent);
const root = document.getElementById("exam-root");
const responses = {}; // questionId -> answer (shape depends on type)

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

function updateProgress() {
  const answered = Object.keys(responses).filter((k) => {
    const v = responses[k];
    if (Array.isArray(v)) return v.length > 0;
    if (v && typeof v === "object") return Object.keys(v).length > 0;
    return v !== undefined && v !== "";
  }).length;
  document.getElementById("progress").textContent =
    `${answered} / ${QUESTIONS.length} answered`;
}

function header(q) {
  const tag = q.is_pbq ? "PBQ" : (q.multi ? "Multiple response" : "Multiple choice");
  return el("div", { class: "q-head" },
    el("span", { class: "q-num" }, `Question ${q.number}`),
    el("span", { class: "q-tag" }, tag),
    el("span", { class: "q-dom" }, `Domain ${q.domain} · ${q.objective}`)
  );
}

function renderChoice(q) {
  const wrap = el("div", { class: "q-options" });
  q.options.forEach((o) => {
    const input = el("input", {
      type: q.multi ? "checkbox" : "radio",
      name: q.id,
      value: o.id,
    });
    input.addEventListener("change", () => {
      if (q.multi) {
        const set = new Set(responses[q.id] || []);
        input.checked ? set.add(o.id) : set.delete(o.id);
        responses[q.id] = [...set];
      } else {
        responses[q.id] = o.id;
      }
      updateProgress();
    });
    const label = el("label", { class: "opt-choice" }, input, el("span", {}, o.text));
    wrap.appendChild(label);
  });
  return wrap;
}

// Build a <select> of target options for matching / categorize PBQs.
function selectFor(options, placeholder, onChange) {
  const sel = el("select", { class: "pbq-select" });
  sel.appendChild(el("option", { value: "" }, placeholder));
  options.forEach((o) => sel.appendChild(el("option", { value: o.id }, o.text)));
  sel.addEventListener("change", () => onChange(sel.value));
  return sel;
}

function renderMatching(q) {
  responses[q.id] = {};
  const wrap = el("div", { class: "pbq" });
  q.prompts.forEach((p) => {
    const row = el("div", { class: "pbq-row" },
      el("span", { class: "pbq-prompt" }, p.text),
      selectFor(q.targets, "— choose —", (val) => {
        if (val) responses[q.id][p.id] = val; else delete responses[q.id][p.id];
        updateProgress();
      })
    );
    wrap.appendChild(row);
  });
  return wrap;
}

function renderCategorize(q) {
  responses[q.id] = {};
  const wrap = el("div", { class: "pbq" });
  q.items.forEach((it) => {
    const row = el("div", { class: "pbq-row" },
      el("span", { class: "pbq-prompt" }, it.text),
      selectFor(q.categories, "— choose category —", (val) => {
        if (val) responses[q.id][it.id] = val; else delete responses[q.id][it.id];
        updateProgress();
      })
    );
    wrap.appendChild(row);
  });
  return wrap;
}

function renderOrdering(q) {
  // Candidate assigns a position (1..n) to each item via a select; we then
  // sort by chosen position to produce the ordered id list.
  const positions = q.items.map((_, i) => ({ id: String(i + 1), text: String(i + 1) }));
  const picks = {}; // itemId -> position string
  const wrap = el("div", { class: "pbq" });

  function recompute() {
    const ordered = Object.entries(picks)
      .filter(([, pos]) => pos)
      .sort((a, b) => Number(a[1]) - Number(b[1]))
      .map(([iid]) => iid);
    responses[q.id] = ordered;
    updateProgress();
  }

  q.items.forEach((it) => {
    const row = el("div", { class: "pbq-row" },
      selectFor(positions, "#", (val) => { picks[it.id] = val; recompute(); }),
      el("span", { class: "pbq-prompt" }, it.text)
    );
    wrap.appendChild(row);
  });
  return wrap;
}

function renderQuestion(q) {
  const card = el("article", { class: "q-card", id: `q-${q.id}` });
  card.appendChild(header(q));
  if (q.stem) card.appendChild(el("p", { class: "q-stem" }, q.stem));

  if (q.type === "multiple_choice" || q.type === "multiple_response") {
    card.appendChild(renderChoice(q));
  } else if (q.type === "pbq_matching") {
    card.appendChild(renderMatching(q));
  } else if (q.type === "pbq_categorize") {
    card.appendChild(renderCategorize(q));
  } else if (q.type === "pbq_ordering") {
    card.appendChild(el("p", { class: "pbq-hint" }, "Assign a position number to each item (1 = first)."));
    card.appendChild(renderOrdering(q));
  }
  return card;
}

QUESTIONS.forEach((q) => root.appendChild(renderQuestion(q)));
updateProgress();

// ---- Timer (counts down from the exam's time limit, like the real exam) ----
const timerEl = document.getElementById("timer");
let remaining = (parseInt(timerEl.dataset.minutes, 10) || 90) * 60;
const timerId = setInterval(() => {
  remaining -= 1;
  const m = String(Math.floor(remaining / 60)).padStart(2, "0");
  const s = String(remaining % 60).padStart(2, "0");
  timerEl.textContent = `${m}:${s}`;
  if (remaining <= 300) timerEl.classList.add("warn");
  if (remaining <= 0) { clearInterval(timerId); submitExam(); }
}, 1000);

// ---- Submit ----
async function submitExam() {
  clearInterval(timerId);
  const btn = document.getElementById("submit-btn");
  btn.disabled = true;
  btn.textContent = "Grading…";
  const res = await fetch("/submit", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ responses }),
  });
  const data = await res.json();
  if (data.redirect) window.location = data.redirect;
}

document.getElementById("submit-btn").addEventListener("click", () => {
  const answered = Object.keys(responses).length;
  if (answered < QUESTIONS.length &&
      !confirm(`You've answered ${answered} of ${QUESTIONS.length}. Submit anyway? Unanswered questions count as incorrect.`)) {
    return;
  }
  submitExam();
});
