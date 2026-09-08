# Capacitors — from basics to Olympiad

A self-contained HTML course on **capacitance, dielectrics and capacitive networks**, written for
**JEE Advanced** and the **physics olympiad track (NSEP → INPhO → IPhO, plus IOPT)**. Every page works
offline from `file://`: no CDN, no MathJax, no fonts, no build step.

```
open capacitors/index.html          ← start here (course map, how to study, the IOQM/NSEP note)
```

or, to browse with the interactive features (theme switch, progress ticks, solved-question tracking):

```
cd capacitors && python3 -m http.server 8000
```

## What is in the folder

| file | what it covers | figures | questions |
| --- | --- | --- | --- |
| `index.html` | course map, how to use the notes, syllabus mapping, the IOQM-vs-INPhO note | 1 | — |
| `01-foundations.html` | charge, Coulomb, field, potential, work, superposition, Gauss's law, conductors vs insulators, the method of images (motivated, not just stated) | 6 | 10 + drill |
| `02-capacitance.html` | why `C` is constant, parallel plates, coaxial and spherical geometry, isolated conductors, slab insertion, fringing and the guard ring, interleaved plates | 2 | 10 + drill |
| `03-energy-and-force.html` | `C = 2U/V²`, field-energy density, force from `½V²dC/dx`, the two sign conventions, pull-in, the two-capacitor paradox, self-energy | 2 | 10 + drill |
| `04-combinations.html` | series/parallel (proved, with their failure modes), charge sharing, bridges, symmetry folding, Δ–Y, the cube, infinite ladders, three-terminal thinking | 3 | 8 + drill |
| `05-dielectrics.html` | polarisation, bound charge, `D`, slab problems, Clausius–Mossotti, local field, voids and stress, losses and heating, Debye relaxation, ferroelectrics, piezo/pyro, breakdown and Paschen | 8 | 10 + drill |
| `06-networks-and-transients.html` | DC steady state as an algorithm, `τ = R_th C` proved, charge through a branch, the exact one-half loss, multi-capacitor eigen-time-constants, compensated dividers, relaxation oscillators, leakage and Warburg diffusion, sinusoidal steady state | 4 | 10 + drill |
| `07-advanced-topics.html` | capacitance/inductance matrices and node elimination, Green's reciprocity and the Ramo theorem, monotonicity theorems, images as a method, the spheroid family and depolarising factors, conformal mapping and corner singularities, MEMS pull-in as a fold, the Rayleigh limit and the Taylor cone | 5 | 7 + drill |
| `08-playbook.html` | triage flowchart, the twelve moves, 25 traps with the one-line reply, numbers to own, a 15-question timed drill with reasons | 1 | 15 |
| `09-olympiad-paper.html` | **the paper: 36 questions** in four sections (12 single-correct, 6 multiple-correct, 8 numerical, 10 long), with a coverage map and marking scheme | — | 36 |
| `10-olympiad-solutions.html` | complete solutions to all 36, marks distributed, with the check that verifies each answer | — | 36 |
| `11-formula-sheet.html` | the whole course on three printable A4 pages (2-column, `Ctrl-P` → PDF) | — | — |

## The teaching contract

* **Concepts before formulas, formulas before problems.** Each chapter opens with *why the quantity exists*, then
  derives, then applies. Nothing is stated as a rule to memorise without its derivation or its failure mode.
* **Every step's reasoning is written down.** The `.why` boxes are the "but *why* is that true?" answer, and the
  `.trap` boxes name the mistake before the reader can make it.
* **Questions interleaved with the theory**, not parked at the end: each is followed by a collapsible full solution.
* **Diagrams over prose wherever geometry does the work** — 31 inline SVG figures, drawn so that the field lines,
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
