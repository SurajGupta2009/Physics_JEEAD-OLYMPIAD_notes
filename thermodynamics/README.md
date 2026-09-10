# Thermodynamics — from basics to Olympiad

A self-contained HTML course on **heat, work, and the accounts between**: kinetic theory, the two laws,
engines, entropy, real gases and radiation — written for **JEE (Main & Advanced)** and the **physics olympiad
track (NSEP → INPhO → IPhO)**. It works offline from `file://`: no CDN, no MathJax, no fonts, no build step.

```
open thermodynamics/Thermodynamics.html   ← the whole course, one file (also served as the topic entry)
```

or, to browse with the interactive features (theme switch, progress ticks, solved-question tracking):

```
cd thermodynamics && python3 -m http.server 8000
```

## What is in the folder

`Thermodynamics.html` is the **only** HTML file. Everything lives inside it, in reading order: the overview, the
**expandable mind-map**, chapters 1–8 (theory with questions interleaved), the full-length Olympiad paper
(36 questions · 245 marks · 3 h), its line-by-line solutions, and the printable formula sheet — the stylesheet
and the TeX renderer are inlined too, so the file is portable on its own. `assets/` keeps copies used by the
tooling; `tools/` holds the validators (`check.py`, `mathfix.py`, `setpages.py`, `test-tex.js`).

## The mind-map layout

The page opens with a map: the root node is the course, one branch per chapter, each labelled with what it
covers and its size (`N Q · M fig · K boxes`). Clicking a branch opens that chapter *in place* — the full
theory, every figure and every question with its collapsible solution — and the top bar offers *Expand all*,
*Collapse all* and *Print / PDF* (printing opens every chapter and every solution first, and the map itself
never prints). Collapsed, the eleven nodes are a revision outline; expanded, they are the whole course.

## The teaching contract

* **Concepts before formulas, formulas before problems.** Each chapter opens with *why the quantity exists*,
  then derives, then applies; every key equation is printed with its validity clause beside it.
* **The ledger method.** First-law problems are worked as books of Q, W, ΔU (ΔS from ch 6 on) with the row sums
  checked; no answer is submitted before its check line.
* **Questions interleaved with the theory**, each with a collapsible solution that explains the distractors,
  not just the right option.
* **Diagrams over prose wherever geometry does the work** — 34 inline SVG figures: the tiling that proves
  entropy's exactness, the two skies of the hydrostatic equation, the isotherm loop with its Maxwell tie line.
* **No external references.** Numbers in the worked examples are computed in-file; the constant shelf (ch 8 §3)
  is the only "look-up" allowed, and it is meant to be memorised.

## Validation

```
cd thermodynamics
python3 tools/mathfix.py      # idempotent: flattens multi-line math spans
python3 tools/setpages.py     # regenerates assets/pages.js from the files on disk
node    tools/test-tex.js     # renderer unit tests
python3 tools/check.py         # tag balance, math rules, links, figures — ALL GOOD
```

From the repo root, `python3 tools/check_all.py` validates this folder together with the registry
(`topics.json`) and the root README table.
