# Elasticity — handwritten-style short notes

**8 JEE sheets + 9 Olympiad/extension sheets = 17 A4 pages.** Every page is a
2480 × 3508 px, 300 DPI portrait PNG; the PDFs are exact A4 reproductions.

Primary source: [`elasticity/Elasticity.md`](../../elasticity/Elasticity.md)
(1513 lines, unchanged). This folder is generated from the editable data in
`sheets.json`; nothing here edits the source chapter.

## Deliverables

| What | File |
|---|---|
| Combined PNG ZIP (**primary download**) | [`elasticity-all-pngs.zip`](elasticity-all-pngs.zip) |
| JEE-only PNG ZIP | [`elasticity-jee-pngs.zip`](elasticity-jee-pngs.zip) |
| Extension-only PNG ZIP | [`elasticity-olympiad-pngs.zip`](elasticity-olympiad-pngs.zip) |
| Combined A4 PDF, JEE first, bookmarked | [`elasticity-short-notes.pdf`](elasticity-short-notes.pdf) |
| JEE A4 PDF | [`elasticity-jee.pdf`](elasticity-jee.pdf) |
| Extension A4 PDF | [`elasticity-olympiad.pdf`](elasticity-olympiad.pdf) |
| Gallery / print view | [`index.html`](index.html) |
| Coverage and classification | [`SCOPE.md`](SCOPE.md) |
| Source corrections and open assumptions | [`SOURCE-AUDIT.md`](SOURCE-AUDIT.md) |
| Print settings | [`PRINTING.txt`](PRINTING.txt) |
| What was actually checked | [`VERIFICATION.md`](VERIFICATION.md) |

PNGs and PDFs sit directly in this folder, matching the other chapters under
`Short notes/`.

## Part I — JEE Main + Advanced (8 sheets)

| # | Sheet | Cards |
|---|---|---|
| 01 | [Elasticity: the material answers back](JEE-01-material-response.png) | What elasticity is · The four bookkeeping pairs · Reading a stress–strain curve · The elastic region is tiny |
| 02 | [Y, B, G and what Poisson ties together](JEE-02-moduli-bulk-shear.png) | Poisson ratio defined · Derive Y = 3B(1 − 2ν) · Derive Y = 2G(1 + ν) · Why −1 < ν < 0.5 |
| 03 | [The extension family: rods as springs](JEE-03-extension-family.png) | Rod as a spring · Series: common force · Parallel: common extension · Self-weight: integrate, do not average |
| 04 | [Composite bars and thermal stress](JEE-04-composite-thermal.png) | Thermal strain and stress · Gaps, partial constraint and the rail · Two-material composite bar · Shrink fits and a quarter turn |
| 05 | [Elastic energy, sudden loads and drops](JEE-05-energy-impact.png) | Stored energy · Sudden application: the factor 2 · Drop from height h · Rivets, bolts and double shear |
| 06 | [Torsion, bending and section properties](JEE-06-torsion-bending.png) | Torsion of a circular shaft · Which section is stiffer per kilogram · Bending: neutral axis and curvature · Cantilever and the I-beam |
| 07 | [Yield, fatigue and choosing a material](JEE-07-plasticity-materials.png) | Beyond the linear law · Specific strength and specific modulus · Buckling versus crushing · Fracture, fatigue and safety factors |
| 08 | [JEE toolkit: triage, traps and limit checks](JEE-08-exam-toolkit.png) | Five-step triage · The four different twos · Numbers and units worth carrying · Scaling laws worth memorising |

## Part II — Olympiad / specialised extensions (9 sheets)

| # | Sheet | Why it is Part II |
|---|---|---|
| 01 | [Why Y is 10^11 Pa: the interatomic spring](Olympiad-01-atomic-spring.png) | Pair potentials and bond curvature: additional theory, not a supplied-data derivation |
| 02 | [Thermal expansion as the asymmetry of a well](Olympiad-02-thermal-expansion-well.png) | Boltzmann averaging of an anharmonic well; the classical estimate α ≈ k_B/2D |
| 03 | [The falling weight with the rod own mass](Olympiad-03-falling-weight-rod-mass.png) | Distributed-mass energy ledger and the L/c validity condition |
| 04 | [The constant-stress rod and the limits of height](Olympiad-04-constant-stress-rod.png) | Exponential taper, crushing length and the tree-height ceilings |
| 05 | [Bending integrated: slope, deflection and supports](Olympiad-05-cantilever-beam-theory.png) | Double integration and support cases beyond the one cantilever formula |
| 06 | [Euler buckling: an eigenvalue, not a deflection](Olympiad-06-buckling-columns.png) | Eigenvalue argument, effective length and hollow sections |
| 07 | [What an I-beam buys, and the thin-walled vessel](Olympiad-07-ibeam-hoop.png) | Fair section comparison, vessel cuts, silk scaling |
| 08 | [Two wave speeds and what an earthquake transmits](Olympiad-08-seismic-waves.png) | P/S speeds, the S shadow and the liquid outer core |
| 09 | [Plane stress, principal axes and Mohr circle](Olympiad-09-multiaxial.png) | Plane-stress transformation, added as an extension; not claimed to be impossible in JEE |

The classification is by relevance and prerequisite, not difficulty. See
[`SCOPE.md`](SCOPE.md) for the rationale sheet by sheet, and for what is *not*
covered.

## Rebuild

```bash
pip install -r requirements.txt          # Pillow, matplotlib, numpy, reportlab, pypdf
python author_content.py                 # content modules -> sheets.json
python render_sheets.py                  # sheets.json -> 17 PNGs + layout-checks.json
python build_exports.py                  # 3 PDFs (bookmarked) + 3 ZIPs + index.html + manifest
python test_exports.py                   # structure, layout, archive, PDF, link and model checks
```

`author_content.py` executes `_content_jee.py` and `_content_oly.py`, then
asserts every sheet has four cards, one `why` and one `trap` per card, and fills
the part/page labels. `render_sheets.py` refuses to ship a card whose text
overflows its box or an equation that is too wide, so a green render is a layout
check, not just a file-count check.

`_measure.py` prints rendered card heights and `_wide.py` lists equations close
to the width limit; `_preview_diagrams.py` renders individual figures and a
contact sheet for eyeballing. They are development aids, not deliverables.

## Format and conventions

- A4 portrait 2480 × 3508 px, nominal 300 DPI, safe margin 125 px (10.6 mm).
- Body 11.52 pt equivalent, explanations 11.04 pt — fixed, never shrunk to fit.
- Navy prose, teal headings/explanations, yellow key results, red warnings.
- Equations are typeset by matplotlib mathtext, which is why the source uses
  `\frac{1}{2}` rather than `\tfrac` and explicit rows rather than matrices.
- Patrick Hand (SIL OFL) is bundled in `fonts/`; the font has no `→` or `µ`
  glyph, so sheets use `$\rightarrow$` and `\mu`.

## Scope note

This is a study edition, not an official syllabus audit. It reproduces the
chapter's physics with corrections recorded in [`SOURCE-AUDIT.md`](SOURCE-AUDIT.md),
and it deliberately adds the plane-stress/Mohr extension flagged as such.
