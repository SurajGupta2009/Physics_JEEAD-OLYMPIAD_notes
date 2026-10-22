# Modern physics — handwritten-style short notes

50 A4 sheets (2480 × 3508 px, 300 DPI): **25 JEE Main + Advanced** sheets numbered
`01/25 … 25/25`, and **25 Olympiad / extension** sheets numbered `01/25 … 25/25`.
The two parts are numbered independently. Each sheet is one page: a titled question,
numbered moves with equations and prose, a right-hand rail of key-result / gate /
trap / numbers cards, one wide analytical figure, and a `KEEP` line.

**The complete modern-physics edition**, in the order the chapter was built:

1. atomic structure — Rutherford, Bohr, spectra, excitation, Z² scaling, quantum
   numbers (JEE 01–08);
2. the photon and the photoelectric effect — the packet budget, the five facts, the
   graphs, the photocell, de Broglie, Davisson–Germer, the uncertainty estimate
   (JEE 09–15);
3. X-rays and Compton scattering — continuum and characteristic lines, absorption,
   Bragg, the Compton shift, pair production, Moseley (Olympiad 01–09);
4. nuclear physics — size and density, binding, the valley, alpha and beta decay,
   the decay law, dating, chains, fission and fusion (JEE 16–25), then
   Geiger–Nuttall, the fission barrier, the valley-floor derivation, transient
   equilibrium, solar neutrinos, reactor arithmetic, counting statistics, the
   isochron, neutron diffraction and the Sun's lifetime (Olympiad 16–25).

Part A (atomic, photon, X-rays) and Part B (nuclear) were delivered separately and
share one layout, one build and one test pass; they are not two editions.

## What is in the box

| File | What it is |
|---|---|
| `JEE-*.png`, `Olympiad-*.png` | the 50 sheets |
| `modern-physics-all-pngs.zip` | all 50 PNGs, reading order |
| `modern-physics-jee-pngs.zip`, `…-olympiad-pngs.zip` | the two parts |
| `modern-physics-short-notes.pdf` | all 50, A4, one sheet per page, bookmarked |
| `modern-physics-jee.pdf`, `…-olympiad.pdf` | the two parts, bookmarked |
| `index.html` | offline gallery with per-sheet download links |
| `SCOPE.md` | page map and the Part I / Part II classification rule |
| `SOURCE-AUDIT.md` | what was recomputed, the corrections, the gaps |
| `PRINTING.txt` | one-page print settings |
| `sheets.json` | per-sheet manifest, including the pixel report |
| `layout-checks.json`, `asset-manifest.json`, `verification-results.json` | build evidence |

## The layout

Same numbered-argument page as the Fluid mechanics edition, with two additions that
this chapter needed:

1. **A question as the title.** The page answers something ("Why did one alpha in
   eight thousand come back?"), it does not announce a topic.
2. **A numbered left spine.** Moves are numbered 1…4 and joined by a rule, so a
   derivation cannot be read out of sequence.
3. **Prose between the equations.** Each move is a paragraph: the sentence says why
   the next equation is true and what it costs.
4. **A right rail** of small cards with fixed roles — `KEY RESULT`, `DEFINE`,
   `GATE`, `TRAP`, `NUMBERS`, `INSIGHT`, `CHECK`. A margin, not a second column.
5. **An energy scale bar** beside the running head. Every page carries the chapter's
   eight-decade ladder (0.1 eV → 10 MeV, banded at eV / keV / MeV) with a marker at
   the energy that page is really about, so the reader always knows which regime the
   sheet lives in: 13.6 eV for the Bohr pages, 5 MeV for the alpha pages, 100 keV for
   Compton, 1.02 MeV for pair production.
6. **One wide analytical figure per page**, drawn natively with axes, units and
   labelled vectors — never a screenshot.
7. **`KEEP /` line** at the foot: the one sentence to remember.

Every sheet's figure band is a fixed 886 px slot: the diagrams on all 50 pages share
one canvas size, so the type size and the label clearance are identical throughout.

## Rebuild

```bash
pip install --break-system-packages -r requirements.txt
python3 author_content.py      # sheets.json + 50 PNGs (~80 s)
python3 build_exports.py       # 3 PDFs, 3 ZIPs, index.html, manifests
python3 test_exports.py        # structure, PDF/ZIP, layout, 69 physics spot checks
python3 test_structure.py      # run from "Short notes/" — repo-level link check
```

`author_content.py` is the only renderer: it builds `Sheet` objects in
`_content_jee.py` / `_content_oly.py` / `_content_nuclear.py`, attaches worked-number blocks from
`_examples.py`, runs `layout.preflight`, draws each page and writes `sheets.json`.
`--dry-run` parses and preflights every equation without writing images.

Content is editable: prose and equations live in the three `_content_*.py` files,
figures in `diagrams.py` (one function per key, returning its caption), typography in
`layout.py`. `_audit_figs.py` renders every figure at the real band size and fails if
any text object falls outside the canvas — it is the guard that keeps axis labels
from being clipped.

## What the checks actually prove

`python3 test_exports.py` prints something like
`PASS: 767 assertions; 69 representative physics checks.` It checks:

* 50 pages, 25 + 25 split, independent numbering, unique flat filenames, distinct
  figures and distinct takeaways;
* every page 2480 × 3508 at 300 DPI, quiet outer margin;
* main column and rail inside their measured limits, figure band above the `KEEP`
  strip, figure slot exactly 886 px (`layout-checks.json` is the same data);
* every PDF is A4 with one sheet per page and one bookmark per sheet, in order;
* every ZIP holds exactly the right PNGs, in reading order; every gallery link
  resolves;
* 69 numbers recomputed from the printed formulas: the Rutherford `r_min`, `b₉₀`
  and Coulomb barrier, the Bohr radius and hydrogen `n = 3` triplet, the Balmer edge
  and Lyman α, He⁺ / Li²⁺ / positronium, the photon budget at 550 nm, sodium's
  threshold, `1.226/√V`, Davisson–Germer, the Duane–Hunt edge, Cu/Mo/Ag Kα, the lead
  half-value layer, Avogadro from NaCl, the Compton shift and recoil energies, the
  pair threshold, the inverse-Compton `4γ²` boost; then the nuclear radius and
  density, deuteron and He-4 binding, `Z₀` at `A = 100` and `238`, the U-238 and
  Po-210 alpha energies, the C-14 and N-13 beta `Q`, Tc-99m activity, the C-14 age,
  the transient ratio and peak time, fissions and fuel mass per GW·day, the
  Coulomb barrier and Gamow peak, the solar helium and neutrino rates, the solar
  lifetime, counts for a 1 % measurement, the isochron age, the thermal-neutron
  wavelength (non-relativistic and the relativistic 1 fm case), the Geiger–Nuttall
  decade span, the pairing term and `a_c/2a_a`.

It does **not** prove that every sentence is right, that the notes are complete, or
that a reader will find every figure obvious. `SOURCE-AUDIT.md` lists what was
recomputed and what was not; treat the sheets as short notes, not as a textbook.

## Sources and licensing

Primary sources, all unchanged:
[`atomic-structure/Atomic-structure.md`](../../atomic-structure/Atomic-structure.md),
[`photoelectric-effect/Photoelectric-effect.md`](../../photoelectric-effect/Photoelectric-effect.md),
[`x-rays/X-rays.md`](../../x-rays/X-rays.md),
[`nuclear-physics/Nuclear-physics.md`](../../nuclear-physics/Nuclear-physics.md).
The Cengage chapters they follow are
the book floor; they are not in this repository. Typeface: Patrick Hand (SIL OFL,
`fonts/`), with DejaVu Sans fallback for Greek, subscripts and relation signs.
Figures: matplotlib, native vector drawing.

Not exhaustive. See `SOURCE-AUDIT.md`.
