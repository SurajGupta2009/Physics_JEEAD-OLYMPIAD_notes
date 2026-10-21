# Fluid mechanics — handwritten-style short notes

30 A4 sheets (2480 × 3508 px, 300 DPI): **19 JEE Main + Advanced** sheets numbered
`01/19 … 19/19`, and **11 Olympiad / extension** sheets numbered `01/11 … 11/11`.
The two parts are numbered independently. Each sheet is one page: a titled question,
numbered moves with equations and prose, a right-hand rail of definition / key-result
/ gate / trap / numbers cards, one wide analytical figure, and a `KEEP` line.

## What is in the box

| File | What it is |
|---|---|
| `JEE-*.png`, `Olympiad-*.png` | the 30 sheets |
| `fluid-mechanics-all-pngs.zip` | all 30 PNGs, reading order |
| `fluid-mechanics-jee-pngs.zip`, `…-olympiad-pngs.zip` | the two parts |
| `fluid-mechanics-short-notes.pdf` | all 30, A4, one sheet per page, bookmarked |
| `fluid-mechanics-jee.pdf`, `…-olympiad.pdf` | the two parts, bookmarked |
| `index.html` | offline gallery with per-sheet download links |
| `SCOPE.md` | page map and the Part I / Part II classification rule |
| `SOURCE-AUDIT.md` | what was recomputed, the three corrections, the gaps |
| `PRINTING.txt` | one-page print settings |
| `sheets.json` | per-sheet manifest, including the pixel report |
| `layout-checks.json`, `asset-manifest.json`, `verification-results.json` | build evidence |

## The layout (and how it differs from the Elasticity edition)

Elasticity used a card grid: short cards, one idea each, many boxes. That is easy to
skim but it hides the *argument*. Fluid mechanics is a chain — statics → Bernoulli →
viscosity → surfaces — so the fluid sheet is built as a **numbered argument**:

1. **A question as the title.** The page answers something, it does not announce a
   topic ("Why does depth, not shape, set the pressure?").
2. **A numbered left spine.** Moves are numbered 1…5 and joined by a rule, so the
   reading order is explicit and the derivation cannot be read out of sequence.
3. **Prose between the equations.** Each move is a paragraph, not a bullet: the
   sentence says *why* the next equation is true, and what it costs.
4. **A right rail of small cards** with fixed roles — `DEFINE`, `KEY RESULT`,
   `GATE`, `TRAP`, `NUMBERS`, `CHECK`, `INSIGHT`. The rail is a margin, not a second
   column: it does not compete with the argument.
5. **One wide analytical figure per page**, drawn natively (axes, units, labelled
   vectors), never a screenshot.
6. **`KEEP /` line** at the foot: the one sentence to remember.

The change from the Elasticity grid is deliberate: fewer boxes, longer reasoning,
a figure that spreads across the page width, and a fixed place for the three things
a candidate actually needs at revision time (the result, the gate, the trap).

## Rebuild

```bash
pip install --break-system-packages -r requirements.txt
python3 author_content.py      # sheets.json + 30 PNGs (~45 s)
python3 build_exports.py       # 3 PDFs, 3 ZIPs, index.html, manifests
python3 test_exports.py        # structure, PDF/ZIP, layout, 24 physics spot checks
python3 test_structure.py      # run from "Short notes/" — repo-level link check
```

`author_content.py` is the only renderer: it builds `Sheet` objects in
`_content_jee.py` / `_content_oly.py`, attaches worked-number blocks from
`_examples.py`, runs `layout.preflight`, draws each page and writes `sheets.json`.
`--dry-run` parses and preflights without writing images.

Content is editable: prose and equations live in the two `_content_*.py` files,
figures in `diagrams.py` (one function per key, returning its caption), typography
in `layout.py`.

## What the checks actually prove

`python3 test_exports.py` prints something like
`PASS: 426 assertions; 23 representative physics checks.` It checks:

* 30 pages, 19 + 11 split, independent numbering, unique flat filenames;
* every page 2480 × 3508 at 300 DPI, quiet outer margin;
* main column and rail inside their measured limits, figure band above the `KEEP`
  strip (`layout-checks.json` is the same data);
* every PDF is A4 with one sheet per page and one bookmark per sheet, in order;
* every ZIP holds exactly the right PNGs; every gallery link resolves;
* 24 numbers recomputed from the printed formulas (hydrostatics, gate force,
  paraboloid, ice, Torricelli, Venturi, Poiseuille, Reynolds, Stokes, Laplace,
  Jurin, shallow water).

It does **not** prove that every sentence is right, that every figure is
mis-collision-free at 100 %, or that the notes are complete. `SOURCE-AUDIT.md`
lists what was recomputed and what was not; treat the sheets as short notes, not as
a textbook.

## Sources and licensing

Primary source: [`../../fluid-mechanics/Fluid-mechanics.md`](../../fluid-mechanics/Fluid-mechanics.md),
left unchanged. The Cengage chapter it follows is the book floor; it is not in this
repository. Typeface: Patrick Hand (SIL OFL, `fonts/`), with DejaVu Sans fallback for
Greek, subscripts and relation signs. Figures: matplotlib, native vector drawing.

Not exhaustive. See `SOURCE-AUDIT.md`.
