"""Study-notes loading and topic linkage.

Each exam has a notes subpackage under ``exam/notes/`` (e.g.
``exam.notes.aplus_core1``). Every module there exposes a module-level list
called ``NOTES``. A note is a plain dict:

    {
        "domain": int,                 # 1..N, matches the exam's domains
        "topic": str,                  # the section/topic title
        "objective": str,              # e.g. "1.2" (optional, "" if n/a)
        "video": str,                  # related video title (optional)
        "study_topics": [str, ...],    # the question-bank study_topic labels
                                       # this note covers — THIS is the linkage
                                       # that powers "missed topic -> notes"
        "body": str,                   # markdown-ish study notes
        "key_points": [str, ...],      # quick-revision bullet takeaways
    }

The ``study_topics`` list is what ties a note to the quiz engine: the grader
reports performance per question ``study_topic``, and we surface the notes
whose ``study_topics`` include those labels.
"""

from __future__ import annotations

import importlib
import pkgutil

# package name -> list[note]
_CACHE: dict[str, list[dict]] = {}


def _iter_note_modules(package_name: str):
    package = importlib.import_module(package_name)
    for modinfo in pkgutil.iter_modules(package.__path__):
        if modinfo.name.startswith("_"):
            continue
        yield importlib.import_module(f"{package_name}.{modinfo.name}")


def _notes_package(profile) -> str:
    # exam.questions.aplus_core1 -> exam.notes.aplus_core1
    return profile.questions_package.replace(".questions.", ".notes.")


def load_notes(profile) -> list[dict]:
    """Return all notes for an exam, sorted by domain then topic."""
    pkg = _notes_package(profile)
    if pkg in _CACHE:
        return _CACHE[pkg]
    notes: list[dict] = []
    try:
        modules = list(_iter_note_modules(pkg))
    except ModuleNotFoundError:
        modules = []
    for module in modules:
        for n in getattr(module, "NOTES", []):
            notes.append(n)
    notes.sort(key=lambda n: (n.get("domain", 99), n.get("topic", "")))
    _CACHE[pkg] = notes
    return notes


def notes_by_domain(profile) -> dict[int, list[dict]]:
    """Group notes by domain number for browsing."""
    grouped: dict[int, list[dict]] = {}
    for n in load_notes(profile):
        grouped.setdefault(n.get("domain", 99), []).append(n)
    return grouped


def _study_topic_index(profile) -> dict[str, list[dict]]:
    """Map each covered study_topic label -> the notes covering it."""
    index: dict[str, list[dict]] = {}
    for n in load_notes(profile):
        for st in n.get("study_topics", []):
            index.setdefault(st, []).append(n)
    return index


def notes_for_topics(profile, study_topics) -> list[dict]:
    """Return the distinct notes that cover any of the given study_topics.

    ``study_topics`` is the set/list of question ``study_topic`` labels the
    candidate missed. Used to surface "notes that will help" after a quiz and
    to build the per-attempt study guide.
    """
    index = _study_topic_index(profile)
    seen: set[int] = set()
    result: list[dict] = []
    for st in study_topics:
        for note in index.get(st, []):
            key = id(note)
            if key not in seen:
                seen.add(key)
                result.append(note)
    # Also try a loose fallback: if a study_topic has no exact note, match any
    # note whose own topic string is a case-insensitive substring match.
    matched_labels = set(index.keys())
    for st in study_topics:
        if st in matched_labels:
            continue
        low = st.lower()
        for note in load_notes(profile):
            hay = (note.get("topic", "") + " " + " ".join(note.get("study_topics", []))).lower()
            if low in hay or any(w in hay for w in low.split(" / ")):
                if id(note) not in seen:
                    seen.add(id(note))
                    result.append(note)
                break
    result.sort(key=lambda n: (n.get("domain", 99), n.get("topic", "")))
    return result
