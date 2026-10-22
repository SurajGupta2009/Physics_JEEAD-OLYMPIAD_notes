# Kinematics export verification

**Run date:** 2026-10-22. Rebuild/test commands ran in the repository's `.venv`; no detailed source chapter was modified.

## Authored and rendered content

- 36 portrait sheets: **26 JEE Main + Advanced** followed by **10 Olympiad/specialised extensions**, with independent visible numbering.
- **144 cards** (four per sheet) and **72 diagram/diagnostic panels** (two per sheet).
- All 219 standalone and inline displayed math expressions in the generated content parsed through the renderer's MathText path. Prose characters in card text and page headings were covered by the packaged Patrick Hand font character map; unsupported glyphs: **0**.
- All cards fit at their fixed body sizes (11.52 pt equivalent prose; 11.04 pt explanations); no overflow was repaired by shrinking text. The filled-card median is 77.6% (recorded in `layout-checks.json`).
- Each PNG is 2480 × 3508 px, with embedded resolution 299.9994 DPI (nominal 300 DPI). Non-white content bounds were consistent across the set: `(125, 134, 2356, 3377)` in the 2480 × 3508 canvas, leaving approximately 124 px or 10.5 mm at the tightest edge.
- Visual inspections included JEE-01, JEE-22, JEE-25 and Olympiad-05, Olympiad-08 and Olympiad-09. Inline equations remained typeset and legible; the sampled card layouts fit; the aircraft correction graph is within its axes; and the pursuit schematic and numerical RK4 path depict the stated geometry without label overlap.

## Independent checks

`test_exports.py` completed with **0 failures**. It checks:

- counts, section ordering, independent numbering, unique slugs, four unique-titled cards and two diagrams per sheet;
- rendering/parse of equation content and font glyph coverage;
- SHA-256 preservation of both detailed source chapters;
- fixed card typography, layout fit and a minimum 70% median card fill;
- every PNG's dimensions, DPI metadata and print-safe inset;
- each ZIP's CRC integrity, exact PNG-only membership and JEE-first order;
- all three PDFs' page counts, A4 portrait page boxes and ordered bookmarks;
- independently recomputed checks for the source's relative-speed and acceleration examples, aircraft/wind signs and magnitudes, equal-height projectile results and energy, inclined-plane optimum, safety-envelope intercepts, circular/curvature identities, linear and quadratic drag limits, pursuit initial conditions, and the Coriolis numerical scale;
- the offline gallery's 36 articles, local links, top-level chapter-index links and generated-asset byte/hash manifest.

The physics checks are selected independent checks, not an exhaustive formal proof of every displayed result. Corrected source disagreements, the first-order assumptions, and model limits are explained in `SOURCE-AUDIT.md`.

## Deliverable set

- Three PNG-only ZIPs: combined (36), JEE (26), Olympiad (10).
- Three A4 PDFs with matching sheet counts and bookmarks; combined PDF is JEE first.
- Offline `index.html`, plus the top-level `Short notes/index.html` entry.

For printing use A4 portrait, one sheet per page, **Fit to page**—not Fill/Crop. See `PRINTING.md`.
