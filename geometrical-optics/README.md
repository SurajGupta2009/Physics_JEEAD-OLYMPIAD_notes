# Geometrical Optics — from basics to Olympiad

A self-contained HTML course on **rays, mirrors, refraction, prisms, lenses and instruments**, written for
**JEE Advanced** and the **physics olympiad track (NSEP → INPhO → IPhO, plus IOPT)**. The complete course
is in `Geometrical-optics.html`; it works offline from `file://`: no CDN, no MathJax, no fonts, no network.

```
open geometrical-optics/Geometrical-optics.html     ← start here (coverage map, how to study, the 12 parts)
```

or, to use the interactive features (theme switch, table of contents, progress ticks, solved-question
tracking in `localStorage`):

```
cd geometrical-optics && python3 -m http.server 8000
```

## What is in the folder

`Geometrical-optics.html` is the only HTML file in this folder, and it is the whole course: front matter,
twelve parts, the paper, its solutions and the formula sheet, in reading order. `assets/` holds only the
local stylesheet and scripts needed to render it offline. The twelve parts are also kept as separate
source files under the repository's git-ignored `scratch/go/parts/`, assembled by `scratch/go/build.py`;
the built HTML file is the deliverable, and the per-topic gate checks the built file.

## Coverage — the Cengage chapter as the floor

The specification was *at least everything in the Cengage Geometrical Optics chapter* (book pp. 1.1–1.180),
plus the olympiad material that chapter does not reach. Every numbered topic in the Cengage contents list
is mapped to a section of this file in part 0's coverage table: basics, plane mirrors, spherical mirrors,
refraction at plane surfaces (laws, deviation, reversibility, the vector form, critical angle and TIR,
apparent shift, slabs, slab + mirror, variable index, travelling microscope), prism and dispersion,
spherical refracting surfaces, lenses, instruments, worked examples, and the exercise sets as the model
for part 10's paper.

| part | what it covers |
|---|---|
| 0 | coverage map, how to study, notation and the sign convention |
| 1 | rays, Fermat's principle, plane mirrors, rotation, multiple images |
| 2 | spherical mirrors: formula, Newton's relation, velocity, the five cases |
| 3 | refraction at plane surfaces: Snell, slab, apparent depth, layered media, graded index |
| 4 | total internal reflection: critical angle, the δ–i graph, fibre, prisms, Snell's window |
| 5 | prisms and dispersion: minimum deviation, the window of emergence, thin prism, achromats |
| 6 | spherical refracting surfaces, lenses, powers, lens systems, silvered and liquid lenses |
| 7 | the eye, defects of vision, camera, magnifier, microscope, telescope, resolution |
| 8 | olympiad machinery: ray equation, matrices, thick lenses, aberrations, rainbows, étendue |
| 9 | the playbook: triage, drawing discipline, the sign algorithm, the trap catalogue, the number sheet |
| 10 | the paper: 36 questions, seven sections, 143 marks, three hours |
| 11 | full solutions to all 36, with a check on every number, and the answer key |
| 12 | the three-page formula sheet |

Deliberately **not** covered here, with reasons: wave optics (a separate note-set, by the scope decision
for this folder), Fresnel coefficients and polarisation on reflection, the evanescent-wave depth beyond
the physical picture in part 4, third-order aberration coefficients and lens-design optimisation beyond
the h²/h³ scalings, and graded-index fibre mode theory. `topics.json` records the same list.

## The teaching contract

* **Concepts before formulas, formulas before problems.** Each section opens with *why the quantity
  exists*, then derives, then applies. Boxed results carry their validity conditions — a formula without
  its conditions is a trap, and the `.trap` boxes name the classic mistakes before the reader can make them.
* **Every worked number is checked**, usually against a limit (μ → 1, the object at infinity, a plane
  mirror recovered from a curved one) or by an independent route. Part 9 collects the checks into a
  procedure, and parts 10–11 mark the paper the way it will actually be marked.
* **Questions are interleaved with the theory**, each followed by a collapsible full solution: 80
  in-chapter questions, then the 36-question paper, then 36 worked paper solutions.
* **Diagrams over prose wherever geometry does the work** — 46 inline SVG figures, drawn to the same
  scale as the numbers in the text; several of them (the aberration and thin-lens comparisons, the
  rainbow, the light cone) are drawn from tables recomputed by hand, so the picture and the prose agree.
* **Olympiad material is derived, not cited**: the ray equation and atmospheric refraction, matrix optics
  with principal planes, spherical aberration from the exact crossing distance, the rainbow angle, and
  the étendue/concentration limit — the parts a JEE-only treatment omits.

## Layout of the code

```
geometrical-optics/
├── Geometrical-optics.html      the complete course (parts 0–12, 46 figures, 152 questions)
├── assets/
│   ├── notes.css               design system: light/dark themes, callout boxes, figure/table/question styles, print CSS
│   ├── notes.js                TOC, scroll-spy, theme + print + "expand all", progress (localStorage), prev/next
│   ├── tex.js                  the math renderer: a small LaTeX subset compiled to HTML+CSS (~130 symbols)
│   └── pages.js                GENERATED by tools/setpages.py — brand, page order, breadcrumbs
└── tools/
    ├── check.py                the per-topic gate: markup, math, links, anchors, figure/caption parity
    ├── mathfix.py              idempotent normaliser for common authoring slips — run it before check.py
    ├── setpages.py             regenerate (or --check) assets/pages.js
    └── test-tex.js             30 unit tests for the renderer
```

Math is written as plain LaTeX inside `<m>…</m>` for inline and
`<div class="eqd" data-tag="…">…</div>` for display (class `key` boxes a result). Because `tex.js`
reads `textContent`, no HTML tags may appear inside a math span.

### Checking this topic

```bash
cd geometrical-optics
python3 tools/mathfix.py            # normalise authoring slips (idempotent)
python3 tools/setpages.py           # regenerate assets/pages.js
python3 tools/check.py              # ALL GOOD, or a list of problems
node tools/test-tex.js              # if you touched assets/tex.js
```

`check.py` exits non-zero if anything is wrong, so it can be wired into a pre-commit hook. The root gate
(`python3 tools/check_all.py`) additionally recomputes the counts recorded in `topics.json`, so after any
rebuild run `python3 tools/check_all.py --update` from the repository root.

The rules for working here alongside other writers (and other agents) are in
[../CONTRIBUTING.md](../CONTRIBUTING.md); the layout contract is in [../STRUCTURE.md](../STRUCTURE.md).
