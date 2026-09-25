#!/usr/bin/env python3
"""Deterministic Mermaid-block linter for this vault's figure grammar.

Validates the subset of Mermaid the notes actually use (see
docs/obsidian-plugin-workflow.md §2): flowchart/graph, mindmap, xychart-beta and
quadrantChart. It is deliberately *not* a full Mermaid parser. It checks the shapes that
have genuinely broken in-vault — obsolete `xychart-beta` bracket axes (rejected by the
Mermaid >= 10 bundled with Obsidian, rendering as an error box) and mindmap roots whose
label carries bare parentheses — plus fence/balance hygiene, so a future mistake fails
the gate instead of only the reader's screen.

Pure stdlib, offline, no node. ``lint(text) -> list[str]`` ([] == clean).
"""
from __future__ import annotations

import re
from typing import Iterable, List, Tuple

FENCE = "```"
KINDS = {"flowchart", "graph", "mindmap", "xychart-beta", "quadrantChart"}

_NUM = r"[-+]?\d+(?:\.\d+)?"
_ARROW = _NUM + r"\s*-->\s*" + _NUM


def extract_blocks(text: str) -> Iterable[Tuple[int, str]]:
    """Yield ``(line_number, body)`` for every ```mermaid … ``` fence.

    ``line_number`` is the 1-based line of the fence so error messages locate the block.
    """
    lines = text.split("\n")
    i = 0
    while i < len(lines):
        if lines[i].rstrip() == FENCE + "mermaid":
            buf: List[str] = []
            j = i + 1
            while j < len(lines) and lines[j].rstrip() != FENCE:
                buf.append(lines[j])
                j += 1
            yield i + 1, "\n".join(buf)
            i = j + 1
        else:
            i += 1


def _balanced(line: str) -> bool:
    for a, b in (("[", "]"), ("{", "}"), ("(", ")"), ('"', '"')):
        if line.count(a) != line.count(b):
            return False
    return True


def _split_brackets(content: str) -> List[str]:
    parts, buf, quote = [], "", None
    for ch in content:
        if ch in "\"'":
            quote = ch if quote is None else (None if quote == ch else quote)
            buf += ch
        elif ch == "," and quote is None:
            parts.append(buf.strip())
            buf = ""
        else:
            buf += ch
    if buf.strip():
        parts.append(buf.strip())
    return parts


def lint(text: str) -> List[str]:
    problems: List[str] = []
    for ln, body in extract_blocks(text):
        if not body.strip():
            problems.append(f"line {ln}: empty ```mermaid block")
            continue
        first = body.strip().split("\n")[0].strip().split()[0]
        if first not in KINDS:
            problems.append(
                f"line {ln}: unknown mermaid kind {first!r} (allowed: {sorted(KINDS)})")
            continue
        if "$" in body or "\\" in body:
            problems.append(
                f"line {ln}: LaTeX inside a mermaid block renders literally — "
                "move math to the *Why:*/*Data:*/*Read:* lines")
        if first == "mindmap":
            problems.extend(_lint_mindmap(ln, body))
        elif first == "xychart-beta":
            problems.extend(_lint_xychart(ln, body))
        else:  # flowchart / graph / quadrantChart
            for k, line in enumerate(body.split("\n"), start=ln + 1):
                if line.strip() and not line.strip().startswith("%%") and not _balanced(line):
                    problems.append(
                        f"line {k}: unbalanced brackets/quotes in mermaid line {line.strip()[:60]!r}")
    return problems


def _lint_mindmap(ln: int, body: str) -> List[str]:
    problems: List[str] = []
    lines = [l for l in body.split("\n") if l.strip()]
    if len(lines) < 2 or not lines[1].strip().startswith("root("):
        problems.append(f"line {ln}: mindmap needs a root((label)) on its first node line")
        return problems
    m = re.match(r"^root\(\((.*)\)\)\s*$", lines[1].strip())
    if not m:
        problems.append(f"line {ln}: malformed mindmap root line {lines[1].strip()[:50]!r}")
        return problems
    label = m.group(1).strip()
    if label and label[0] not in "\"'" and ("(" in label or ")" in label):
        problems.append(
            f"line {ln}: mindmap root label contains bare parentheses "
            f"{label[:40]!r} — quote it, e.g. root((\"{label}\"))")
    return problems


def _lint_xychart(ln: int, body: str) -> List[str]:
    problems: List[str] = []
    for k, raw in enumerate(body.split("\n"), start=ln + 1):
        line = raw.strip()
        if not line or line.startswith("%%"):
            continue
        m = re.match(r"^(x-axis|y-axis)(.*)$", line)
        if not m:
            continue
        axis, rest = m.group(1), m.group(2).strip()
        label = ""
        if rest.startswith('"'):
            lm = re.match(r'^"([^"]*)"\s*(.*)$', rest)
            if lm:
                label, rest = lm.group(1), lm.group(2).strip()
            else:
                problems.append(f"line {k}: unterminated axis label in {line[:50]!r}")
                continue
        shown = f'{axis} "{label}" ' if label else f"{axis} "

        if rest.startswith("["):
            inside = rest[1:rest.rfind("]")] if "]" in rest else rest[1:]
            entries = _split_brackets(inside)
            all_quoted = all(e.startswith(('"', "'")) for e in entries)
            if axis == "y-axis":
                problems.append(
                    f"line {k}: y-axis bracket list {rest[:40]!r} is obsolete — "
                    "a y-axis must be a numeric range 'y-axis min --> max'")
            elif all_quoted:
                # a categorical tick list on the x-axis is legal Mermaid 10/11.
                continue
            elif len(entries) == 2 and all(re.fullmatch(_NUM, e) for e in entries):
                problems.append(
                    f"line {k}: numeric bracket range {rest[:40]!r} is obsolete — "
                    f"use x-axis {entries[0]} --> {entries[1]}")
            else:
                problems.append(
                    f"line {k}: x-axis bracket list {rest[:40]!r} is not a two-point "
                    f"arrow range — use x-axis <min> --> <max> or an all-quoted tick list")
            continue

        if not re.fullmatch(_ARROW, rest):
            problems.append(
                f"line {k}: {shown}{rest[:40]!r} is not a numeric range — "
                f"use {axis} <min> --> <max> (Mermaid >= 10)")

    return problems


if __name__ == "__main__":
    import sys
    from pathlib import Path
    for path in sys.argv[1:]:
        for msg in lint(Path(path).read_text(encoding="utf-8")):
            print(f"{path}: {msg}")
