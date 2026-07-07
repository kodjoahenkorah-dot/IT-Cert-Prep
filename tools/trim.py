"""One-off maintenance helper: trim a question file to keep only its first N
questions, preserving the source formatting of the kept questions.

Used to land each exam bank on an EXACT target total after generating a slight
overshoot. Run via: python -m tools.trim <file.py> <keep_n>
"""

from __future__ import annotations

import ast
import sys


def keep_first_n(path: str, keep: int) -> int:
    """Rewrite ``path`` so its module-level QUESTIONS list keeps only the first
    ``keep`` elements. Returns the new count. Preserves the exact source text of
    the kept question dicts (only drops the trailing ones).
    """
    src = open(path, "r", encoding="utf-8").read()
    tree = ast.parse(src)
    qlist = None
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for t in node.targets:
                if isinstance(t, ast.Name) and t.id == "QUESTIONS":
                    qlist = node.value
    if qlist is None or not isinstance(qlist, (ast.List, ast.Tuple)):
        raise ValueError(f"No QUESTIONS list found in {path}")

    elts = qlist.elts
    if keep >= len(elts):
        return len(elts)  # nothing to trim

    lines = src.splitlines(keepends=True)

    def offset(lineno: int, col: int) -> int:
        return sum(len(lines[i]) for i in range(lineno - 1)) + col

    # Cut from the start of the first dropped element to the end of the last
    # kept element, leaving the list's closing bracket intact.
    last_keep = elts[keep - 1]
    first_drop = elts[keep]
    end_keep = offset(last_keep.end_lineno, last_keep.end_col_offset)
    start_drop = offset(first_drop.lineno, first_drop.col_offset)

    new_src = src[:end_keep] + ",\n" + src[start_drop + 0 :]
    # Remove the dropped elements: everything from start_drop up to the closing
    # bracket of the list. Find the list's end.
    list_end = offset(qlist.end_lineno, qlist.end_col_offset)  # position of ']'
    new_src = src[:end_keep] + ",\n" + src[list_end - 1 :]

    # Validate it still parses and has exactly `keep` questions.
    mod = ast.parse(new_src)
    cnt = None
    for node in ast.walk(mod):
        if isinstance(node, ast.Assign) and any(
            isinstance(t, ast.Name) and t.id == "QUESTIONS" for t in node.targets
        ):
            cnt = len(node.value.elts)
    if cnt != keep:
        raise ValueError(f"Trim produced {cnt} questions, expected {keep}")

    open(path, "w", encoding="utf-8").write(new_src)
    return keep


if __name__ == "__main__":
    path, keep = sys.argv[1], int(sys.argv[2])
    print(f"{path}: kept {keep_first_n(path, keep)} questions")
