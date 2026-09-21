# Wave Optics — from basics to Olympiad

> **Portable Markdown edition:** [Wave-optics.md](Wave-optics.md) is the GitHub-friendly reading copy with standard Markdown math, collapsible solutions and local SVG diagrams in `assets/figures/`. The original [Wave-optics.html](Wave-optics.html) remains available for the interactive offline view and printing.

A self-contained course on **superposition, interference, diffraction and polarisation**, written for
**JEE Advanced** and the **physics olympiad track (NSEP → INPhO → IPhO, plus IOPT)**. The complete course
is in `Wave-optics.html`; it works offline from `file://`: no CDN, no MathJax, no fonts, no network.

```
open wave-optics/Wave-optics.md        ← start here (coverage map, how to study, the 12 parts)
```

or, to use the interactive features (theme switch, table of contents, progress ticks, solved-question
tracking in `localStorage`):

```
cd wave-optics && python3 -m http.server 8000
```

## What is in the folder

`Wave-optics.html` is the only HTML file in this folder, and it is the interactive edition: front matter, twelve
parts, the paper, its solutions and the formula sheet, in reading order. `assets/` holds only the local
stylesheet and scripts needed to render it offline. The twelve parts are also kept as separate source
files under the repository's git-ignored `scratch/wave/parts/`, assembled by `scratch/build.py`; the built
HTML file is the deliverable, and the per-topic gate checks the built file.

## Coverage — the Cengage chapter as the floor

The specification was *at least everything in the Cengage Wave Optics chapter* (book pp. 2.1–2.95), plus
the olympiad material that chapter does not reach. Every numbered topic in the Cengage contents list is
mapped to a section of this file in part 0's coverage table: Huygens' wave theory and wavefronts, the
Huygens construction, superposition and the conditions for interference, coherent sources, thin-film
interference, Young's double slit (bright and dark fringe positions, fringe width and the angular fringe
width, maximum order, shape of the fringes, white light including the wavelengths missing at a point, the
slab/liquid/unequal-slit cases, rays off the principal axis and oblique incidence, a source off the central line,
geometrical and optical paths, displacement of the fringes), Fresnel's biprism, Lloyd's mirror and the
phase change on reflection, the solved examples, and the exercise sets as the model for part 10's paper.

| part | what it covers |
|---|---|
| 0 | coverage map, how to study, notation, the two currencies (phase and path) |
| 1 | waves, the wavefront, Huygens' construction, superposition, coherence, intensity |
| 2 | Young's double slit in every standard case: fringe width, order limits, white light, slabs, oblique sources |
| 3 | thin films: the reflected and transmitted conditions, wedges, Newton's rings, antireflection coatings |
| 4 | Fresnel's biprism, Lloyd's mirror, Fresnel's mirrors, the Michelson interferometer |
| 5 | diffraction: Fresnel and Fraunhofer regimes, the single slit, N slits, gratings, resolution, crystals |
| 6 | polarisation: Malus, Brewster, scattering, double refraction, wave plates, optical activity |
| 7 | the wave toolkit: coherence measured, Fourier pairs, Fresnel coefficients, evanescent waves, Fabry–Perot, Abbe |
| 8 | measurement: wavelength, thickness, index, displacement; five olympiad problems worked; instruments |
| 9 | the playbook: triage, phase bookkeeping, drawing discipline, the trap catalogue, the number sheet |
| 10 | the paper: 36 questions, seven sections, 143 marks, three hours |
| 11 | full solutions to all 36, with a check on every number, and the answer key |
| 12 | the three-page formula sheet |

Deliberately **not** covered here, with reasons: quantum optics (photon statistics and single-photon
interference), partial-coherence theory with mutual coherence functions, the Maxwell-equation derivation of
the Fresnel coefficients, biaxial crystal optics, nonlinear optics and fibre mode theory, and computer
FFTs. `topics.json` records the same list.

## The teaching contract

* **Concepts before formulas, formulas before problems.** Each section opens with *why the quantity
  exists*, then derives, then applies. Boxed results carry their validity conditions — a formula without
  its conditions is a trap, and the `.trap` boxes name the classic mistakes before the reader can make them.
* **Every worked number is checked**, usually against a limit (μ → 1, t → 0, d = a, λ → 0) or by an
  independent route. Part 9 collects the checks into a procedure, and parts 10–11 mark the paper the way
  it will actually be marked.
* **Questions are interleaved with the theory**, each followed by a collapsible full solution: 100
  in-chapter questions, then the 36-question paper, then 36 worked paper solutions (136 distinct, 172 question blocks).
* **Phase bookkeeping is taught as an algorithm** — five steps, with a cross drawn at every reflection off
  a denser medium — because a lost λ/2 is the single commonest error in the subject.
* **Diagrams over prose wherever geometry does the work** — 27 inline SVG figures, drawn to the same scale
  as the numbers in the text.
* **Olympiad material is derived, not cited**: coherence length and the visibility curve, Fresnel
  coefficients and the degree of polarisation, the evanescent-wave penetration depth and frustrated total
  internal reflection, many-beam interference and the Fabry–Perot finesse, and the Abbe resolution limit —
  the parts a JEE-only treatment omits.

## Layout of the code

```
wave-optics/
├── Wave-optics.html            the complete course (parts 0–12, 27 figures, 172 question blocks)
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
reads `textContent`, no HTML tags may appear inside a math span — one `<m>` per formula, never
`$`-delimited runs inside a single `<m>`.

### Checking this topic

```bash
cd wave-optics
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

## Audit record — plan.md PART 4 (repository integration, 2026-09-21)

This note-set was audited against `plan.md` §2 PART 4 (Cengage floor + harmonisation with parts 1–3). Findings and
what was done, all in `Wave-optics.html` (the Markdown is regenerated from it by `tools/html_to_markdown.py`):

| finding | action |
|---|---|
| no pedagogical link to the string/sound/EM wave notes (plan §2 PART 4.1) | new **§1.1.1** "One equation, three mechanisms", with the wave-lineage table, the inheritance/non-inheritance list and the boundary-flip box that ties §3.2 and §4.2 to a fixed end on a string |
| the part 0 coverage table pointed at stale section numbers (superposition, maximum order, fringe shape, white light, optical path, reflection phase) | every row re-pointed at the section that actually carries the material; two wrong inline pointers (§7.4 → §7.3, §7.8 → §4.7, §7.2 → §7.1, §5.4 → §5.2, §5.7 → §5.5, §2.11 → §2.7.1, an audit rule mis-cited to §4.9 → §8.7) corrected |
| white-light YDSE covered band overlap but not the *missing wavelengths at a point* (plan §2 PART 4.2) | §2.6 now derives absent $\lambda = 2\Delta/(2m-1)$ and bright $\lambda = \Delta/m$ with a worked example, plus **Q13** |
| oblique incidence was promised in the part 2 lead and the coverage table but never derived | new **§2.7.5** with $\Delta = d(\sin\theta-\sin\alpha)$, the one-fringe tilt $\tan\alpha = \lambda/d$, the asymmetric order limit and its $2n_{\max}+1$ invariant, a trap box and **Q14**; §2.7 is now "five cases" |
| $\beta = \lambda D/d$ and $\theta = \lambda/d$ were quoted without their boundary domain (house rule: every boxed formula states one) | §2.3 now states that the fringes are equally spaced in $\sin\theta$, and gives the exact statement next to the paraxial one |
| "1 cm of glass ≈ 5000 extra waves" in the numbers-to-memorise table is wrong: $0.5\,\text{cm}/600\,\text{nm} = 8333$ | replaced with the checked number (8300, at 600 nm) |
| the formula sheet called $y = A\cos(\omega t-kx)$ "the wave equation" | §12.1 now gives $\partial^{2}\psi/\partial t^{2} = v^{2}\partial^{2}\psi/\partial x^{2}$ with the three speeds and their conditions, and the sinusoid is labelled a travelling-wave solution |
| the plan's cross-topic registry | `topics.json` now carries `string-waves`, `sound-waves` and `electromagnetic-waves` as `planned` with the scope each owes; `CURRICULUM.md` gained the wave-sequence section |

Not covered by this audit, and still true of the note: the Fresnel coefficients are stated, not derived from Maxwell's
boundary conditions — that derivation is owned by the future `electromagnetic-waves/` note-set, whose registry entry
records the hand-off. `python3 tools/check_all.py` is green (27 figures, 172 question blocks, 100 solution panels).
