# Capacitors — from basics to Olympiad

> **Portable Markdown edition:** [Capacitors.md](Capacitors.md) is the GitHub-friendly reading copy with standard Markdown math, collapsible solutions and local SVG diagrams in `assets/figures/`. The original [Capacitors.html](Capacitors.html) remains available for the interactive offline view and printing.

A self-contained course on **capacitance, dielectrics and capacitive networks**, written for
**JEE Advanced** and the **physics olympiad track (NSEP → INPhO → IPhO, plus IOPT)**. The portable course is in `Capacitors.md`; it works
offline from `file://`: no CDN, no MathJax, no fonts, no build step.

```
open capacitors/Capacitors.md             ← start here (course map, how to study, the IOQM/NSEP note)
```

or, to browse with the interactive features (theme switch, progress ticks, solved-question tracking):

```
cd capacitors && python3 -m http.server 8000
```

## What is in the folder

`Capacitors.html` is the only HTML file in this folder. It contains the overview, all theory sections,
the Olympiad paper, complete solutions, and the formula sheet in reading order: 150 question blocks
(78 in-chapter ones each with a folded solution, the 36-question paper, and its 36 mirrored solutions).
The `assets/` folder
contains only the local stylesheet and scripts needed to render it offline.

## Coverage — the Cengage chapter as the floor

The Cengage volume's **Capacitor and Capacitance** is chapter 4 (book pp. 4.1–4.36). Every numbered contents entry
of that chapter is mapped to a section of `Capacitors.html` in the file's own **Cengage coverage map** (front
matter, right after *Syllabus coverage*). Three items were added or made explicit so that the floor is genuinely
covered rather than merely implied:

| added for the Cengage floor | where |
|---|---|
| the Kirchhoff sign convention for capacitors, written once: node potentials as unknowns, $q_i=C(V_i-V_j)$, algebraic charge sums at floating nodes, charges (not currents) conserved | §4.3, box *The sign convention* |
| energy in a combination: which capacitor holds the joules — $U_i/U=C_{\text{eq}}/C_i$ in series and $C_i/C_{\text{eq}}$ in parallel, with the series-string breakdown warning | §4.2, box *Energy in a combination* |
| effect of a dielectric on every parameter, both constraints (battery disconnected vs connected): $C, Q, V, E, \sigma, U$, cell work, force, safe voltage | §3.4, table *Dielectric inserted: every parameter, both constraints* |

## Order and conventions (the house rules this file follows)

The file is one long document with a strict, checkable order, so that a new chapter or section can be dropped in
without upsetting anything else:

* **Numbering is contiguous across levels.** Every chapter numbers its sections $n.1, n.2, \ldots$ in document
  order, whether the heading is an `<h2>` or a sub-topic heading — chapter 1 runs 1.1 … 1.10 with 1.3 and 1.6 as
  sub-headings, and nothing is skipped.
* **Every chapter closes the same way.** Questions (folded solutions) → a one-line drill → a "chapter in six lines"
  summary box → a numbered **Checkpoint** list. Chapters 1–4 keep their questions interleaved and number only the
  checkpoint/drill; chapters 5–8 park them under a numbered *Questions* heading. Both patterns are allowed; what is
  not allowed is an unnumbered closing block, which is why 5.12–5.14, 6.9–6.11, 7.9–7.11 and 8.6 exist.
* **Every question has a solution.** A `<div class="q">` is always followed by a `<details class="sol">`, in-chapter
  and in the fifteen-question drill alike; the paper's 36 questions are solved under the same numbers in chapter 10.
* **Equation labels (`data-tag`) are unique within a chapter**, and the answer key covers all four sections of the
  paper, Section D by headline result.
* **Cross-references use the section numbers** (§5.6), never page numbers; the section numbers are stable
  because inserting a section renumbers only its own chapter.

## The teaching contract

* **Concepts before formulas, formulas before problems.** Each chapter opens with *why the quantity exists*, then
  derives, then applies. Nothing is stated as a rule to memorise without its derivation or its failure mode.
* **Every step's reasoning is written down.** The `.why` boxes are the "but *why* is that true?" answer, and the
  `.trap` boxes name the mistake before the reader can make it.
* **Questions interleaved with the theory**, not parked at the end: each is followed by a collapsible full solution.
* **Diagrams over prose wherever geometry does the work** — 32 inline SVG figures, drawn so that the field lines,
  the charges and the dimensions sit in the same picture.
* **The last chapter is a real paper**: 36 questions covering every section, at INPhO standard with JEE-format
  sections, plus a separate solutions file.

## Layout of the code

```
capacitors/
├── assets/
│   ├── notes.css     design system: light/dark themes, callout boxes, figure/table/question styles, print CSS
│   ├── notes.js      TOC builder, scroll-spy, theme + print + "expand all", solved-question progress (localStorage),
│   │                 deep-link scroll, SVG arrow markers, prev/next from a single PAGES list
│   └── tex.js        the math renderer: a small LaTeX subset compiled to HTML+CSS (fractions, roots, scripts,
│                     brackets, matrices/aligned/cases, ~130 symbols, arrows, \boxed, \underbrace)
├── tools/
│   ├── check.py      validator: tag balance (incl. inside SVG), `<m>` balance, raw `<`/newlines inside math,
│   │                 every \command cross-checked against tex.js, link + anchor resolution, figure/caption parity
│   ├── mathfix.py    idempotent normaliser for common authoring slips — run it *before* check.py
│   └── test-tex.js   30 unit tests for the renderer (`node tools/test-tex.js`)
└── *.html            the twelve pages
```

Math is written as plain LaTeX inside `<m>…</m>` for inline and `<div class="eqd" data-tag="…">…</div>` for
display (add class `key` to box a result). Because `tex.js` reads `textContent`, no HTML tags may appear inside a
math span and `<` must be written `&lt;`.

### Editing a page

```bash
cd capacitors
python3 tools/mathfix.py            # normalise authoring slips (idempotent)
python3 tools/check.py              # ALL GOOD, or a list of problems
node tools/test-tex.js              # if you touched assets/tex.js
```

`check.py` exits non-zero if anything is wrong, so it is safe to wire into a pre-commit hook. New symbols or
commands belong in `assets/tex.js` (`SYM`, `FUN`, `SP`); the validator reads them from there, so nothing else needs
updating.

## Adding a chapter to this topic

```bash
cp ../_templates/chapter.html 12-noise-and-measurement.html   # then fill the {{placeholders}}
python3 tools/mathfix.py && python3 tools/setpages.py && python3 tools/check.py
cd .. && python3 tools/check_all.py --update                  # recount the registry
```

One file per chapter, and one card appended at the end of `index.html`'s chapter list: the
navigation, the breadcrumb and this folder's counts are all generated from the files, so nothing
else needs editing. The rules for working here alongside other writers (and other agents) are in
[../CONTRIBUTING.md](../CONTRIBUTING.md); the layout contract is in [../STRUCTURE.md](../STRUCTURE.md).

### What the next chapter should inherit

Chapter 11 is the terminal page: the index's progress board, the prev/next chain and the formula
sheet all assume it is last. If you add chapters, keep `09`/`10`/`11` as the paper, its solutions
and the sheet — put new material before them and renumber the tail in one mechanical commit
(`CONTRIBUTING.md` §5). Nothing in the tooling needs to change: `setpages.py` sorts by `NN`.
