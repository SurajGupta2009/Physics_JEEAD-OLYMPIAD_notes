#!/usr/bin/env python3
"""Local gate for a text-only, Obsidian-first Markdown chapter written under plan.md."""
from __future__ import annotations
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT.parent))  # repo root, for tools/mermaid_lint.py
from tools import mermaid_lint

CFG = json.loads((ROOT / "notes.json").read_text(encoding="utf-8"))
SRC = (ROOT / CFG["master"]).read_text(encoding="utf-8")
errors: list[str] = []

def need(cond: bool, msg: str) -> None:
    if not cond: errors.append(msg)

def contiguous(tag: str, pattern: str, minimum: int) -> int:
    got = [int(n) for n in re.findall(pattern, SRC, re.M)]
    shown = got[:12] + (["..."] if len(got) > 12 else [])
    need(got == list(range(1, len(got) + 1)),
         f"{tag}: numbering must run 1..n with no gaps or repeats (got {shown})")
    need(len(got) >= minimum, f"{tag}: {len(got)} found, requires at least {minimum}")
    return len(got)

need(SRC.startswith("---\n"), "must open with YAML frontmatter block ('---')")
if SRC.startswith("---\n"):
    fm = SRC[4:SRC.find("\n---", 4)]
    for key in ("title:", "part:", "slug:"):
        need(key in fm, f"frontmatter is missing '{key}'")
    need(str(CFG["part"]) in fm, f"frontmatter 'part:' must be {CFG['part']}")

blocks = re.findall(r"^## Part (\d+) · ", SRC, re.M)
need(blocks == [str(i) for i in range(15)],
     f"15 blocks must appear in order (got {blocks})")

n_c = contiguous("concept checks", r"^\*\*C(\d+) — ", CFG["minimums"]["checks"])
n_e = contiguous("worked exemplars", r"^### E(\d+) — ", CFG["minimums"]["exemplars"])
n_q = contiguous("practice questions", r"^#### Q(\d+)\. ", CFG["minimums"]["practice"])
n_ol = contiguous("olympiad problems", r"^### OL(\d+) — ", CFG["minimums"]["olympiad"])

paper = [(int(n), int(m)) for n, m in re.findall(r"^### P(\d+) · (\d+) marks", SRC, re.M)]
need([n for n, _ in paper] == list(range(1, 37)),
     f"paper must have P1..P36 (got {len(paper)})")
marks = sum(m for _, m in paper)
need(marks == CFG["paper"]["marks"],
     f"paper marks sum to {marks}, notes.json says {CFG['paper']['marks']}")
for m, count in CFG["paper"]["sections"].items():
    got = sum(1 for _, mm in paper if mm == int(m))
    need(got == count, f"paper: expected {count} questions worth {m} marks, found {got}")
sections = re.findall(r"^#### Section ([A-D]) · ", SRC, re.M)
need(sections == ["A", "B", "C", "D"], f"paper sections A-D must be present (got {sections})")
need(SRC.count("<details>") >= len(paper), "every paper question needs a collapsible solution")

diags = re.findall(r"^> \[!abstract\] DIAGRAM D(\d+)\.(\d+) · ", SRC, re.M)
need(len(diags) >= CFG["minimums"]["diagrams"],
     f"DIAGRAM briefs: {len(diags)} found, requires at least {CFG['minimums']['diagrams']}")
need(not [p for p, _ in diags if int(p) != CFG["part"]],
     f"DIAGRAM numbers must start with part number ({CFG['part']})")
need(SRC.count("*Show:*") >= len(diags), "every DIAGRAM brief needs a *Show:* line")
need(SRC.count("*Search:*") >= len(diags), "every DIAGRAM brief needs a *Search:* line")

fence = chr(96) * 3
for pattern, why in ((r"!\[", "Markdown image"), (r"<img", "HTML image"),
                     (r"\]\(https?://", "external link")):
    need(not re.search(pattern, SRC), f"media policy: no {why} allowed")
need(not re.search(r"\.(png|jpe?g|gif|webp)\b", SRC, re.I), "media policy: no raster images")
# ── FIGURE system (plan.md §1.2 media policy v2 / docs/obsidian-plugin-workflow.md §2) ──
figs = re.findall(r"^> \[!tip\] FIGURE F(\d+)\.(\d+) · ", SRC, re.M)
need(len(figs) >= CFG["minimums"]["figures"],
     f"FIGURES: {len(figs)} found, requires at least {CFG['minimums']['figures']}")
need(not [p for p, _ in figs if int(p) != CFG["part"]],
     f"FIGURE numbers must start with this part's number ({CFG['part']})")
need(SRC.count("*Why:*") >= len(figs), "every FIGURE needs a '*Why:*' line")
need(SRC.count("*Data:*") >= len(figs), "every FIGURE needs a '*Data:*' line")
need(SRC.count("*Read:*") >= len(figs), "every FIGURE needs a '*Read:*' line")
mm = re.findall(fence + r"mermaid[ \t]*\n([A-Za-z0-9_-]+)", SRC)
kinds = {"flowchart", "graph", "mindmap", "xychart-beta", "quadrantChart",
         "sequenceDiagram", "stateDiagram-v2", "stateDiagram", "classDiagram",
         "pie", "erDiagram", "gitGraph", "gantt", "journey"}
need(all(k in kinds for k in mm), f"unknown mermaid kind: {sorted(set(mm) - kinds)}")
need(len(mm) >= len(figs), "every FIGURE needs a ```mermaid block")
for _msg in mermaid_lint.lint(SRC):
    need(False, f"mermaid: {_msg}")

callouts = re.findall(r"^> \[!([a-z]+)\]", SRC, re.M)
need(len(callouts) >= CFG["minimums"]["callouts"],
     f"callouts: {len(callouts)} found, requires at least {CFG['minimums']['callouts']}")
need(not [c for c in callouts if c not in CFG["callout_types"]],
     f"unknown callout type: {sorted(set(callouts) - set(CFG['callout_types']))}")
bold_box = re.findall(r"^> \*\*(Definition|Why|Condition|Check|Trap|Insight|Hand-off|Exam note|Numbers|History|Example)\.\*\*", SRC, re.M)
need(not bold_box, f"use Obsidian callout form instead of bold-label boxes: {bold_box[:3]}")
need(not re.search(r"<summary>.*?</summary>\n(?!\n)", SRC, re.S), "blank line after </summary>")
need(not re.search(r"[^\n]\n</details>", SRC), "blank line before </details>")
for m in re.finditer(r"\$\$(.*?)\$\$", SRC, re.S):
    need(not re.search(r"\n\s*\n", m.group(1)), "no blank line inside $$ block")
for m in re.finditer(r"(?<![\\$])\$(?!\$)([^\n$]*)(?<!\\)\$(?!\$)", SRC):
    tex = m.group(1)
    need(tex == tex.strip(), f"no space inside dollars: {tex[:40]!r}")
need(not re.search(r"\\\(|\\\[", SRC), r"use $/$$ not \(\)\[\]")
need("\\tag" not in SRC and "\\label" not in SRC, "no \\tag or \\label")
table_pipes = []
for line in SRC.split("\n"):
    if line.startswith("|"):
        for tex in re.findall(r"(?<![\\$])\$(?!\$)([^\n$]*)(?<!\\)\$(?!\$)", line):
            if "|" in tex.replace("\\|", ""):
                table_pipes.append(tex[:40])
need(not table_pipes, f"escape pipe in table maths: {table_pipes[:3]}")
tags, inside = [], False
for line in SRC.split("\n"):
    if line.startswith(fence): inside = not inside; continue
    if inside or line.lstrip().startswith("#"): continue
    if re.search(r"(?<!\S)#[A-Za-z][A-Za-z0-9_/-]*", line):
        tags.append(line[:60])
need(not tags, f"no #hashtags in prose: {tags[:3]}")

need(not re.search(r"TODO|FIXME|\{\{[A-Z_]+\}\}", SRC), "unfinished placeholder")
need(not re.search(r"\?\s*no:", SRC), "thinking-out-loud fragment")
need(SRC.count("<details>") == SRC.count("</details>"), "details mismatch")
need(SRC.count("<summary>") == SRC.count("</summary>"), "summary mismatch")
need(len(SRC.split()) >= CFG["minimums"]["words"],
     f"only {len(SRC.split())} words, requires at least {CFG['minimums']['words']}")

body = re.sub(fence + r".*?" + fence, "", SRC, flags=re.S)
displays = re.findall(r"\$\$(.*?)\$\$", body, re.S)
rest = re.sub(r"\$\$.*?\$\$", "", body, flags=re.S)
inline = re.findall(r"(?<![\\$])\$(?!\$)([^\n$]*)(?<!\\)\$(?!\$)", rest)
need(rest.count("$") % 2 == 0, "unbalanced single-dollar delimiters")
need(body.count("$$") % 2 == 0, "unbalanced display-math delimiters")
for tex in displays + inline:
    depth = 0
    for tok in re.findall(r"(?<!\\)[{}]", tex):
        depth += 1 if tok == "{" else -1
        if depth < 0: break
    need(depth == 0, f"unbalanced braces in: {tex[:60]!r}")

if errors:
    print("\n".join(f"FAIL: {e}" for e in errors))
    sys.exit(1)
print(f"ALL GOOD: 15 blocks · C×{n_c} E×{n_e} Q×{n_q} OL×{n_ol} · "
      f"paper {len(paper)} Q / {marks} marks · {len(diags)} DIAGRAM briefs · "
      f"{len(figs)} FIGURES (mermaid) · {len(callouts)} callouts · no raster images")
