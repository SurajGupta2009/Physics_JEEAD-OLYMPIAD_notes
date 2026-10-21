# What was actually checked

Verification runs from `test_exports.py` in this folder. The current run is
recorded in `verification-results.json`: **594 assertions, 40 independent
physics/model checks, 17 PNGs, 3 ZIPs, 3 PDFs**. That is a checklist, not a
certificate that every line of physics on all 17 pages is correct.

## Automated checks (all passing)

| Area | Check |
|---|---|
| Structure | 17 sheets, 8 JEE + 9 Olympiad in reading order; unique slugs; 68 cards; 34 diagrams; 136 displayed equations |
| Numbering | Part page counters run 1…8 and 1…9; no stale `JEE-*`/`Olympiad-*` PNGs on disk |
| Images | 2480 × 3508 px; embedded 300 DPI; indexed PNG; content inside the 125 px safe margin on all four sides |
| Layout | Every card's measured text height is below its 1050 px box; body text is exactly 11.52 pt and explanations 11.04 pt on all 68 cards — nothing was shrunk to fit |
| Font coverage | Every prose character in titles, subtitles, card text, traps and takeaways exists in `fonts/PatrickHand-Regular.ttf` |
| ZIPs | CRC test passes; entry order equals reading order (JEE first); bytes identical to the PNGs on disk |
| PDFs | A4 portrait media box (595.28 × 841.89 pt); one image per page; page count and bookmark count equal the sheet count; each bookmark resolves to its own page and carries the sheet title; embedded image stream hashes equal the PNG sample bytes, so the PDF is lossless |
| Links | Every relative `href`/`src` in `index.html` resolves to an existing file |
| Source | SHA-256 of `elasticity/Elasticity.md` unchanged from the value recorded at the start of authoring |
| Manifest | `asset-manifest.json` sizes and SHA-256 values match the files on disk |

## Physics and model checks

Forty numbers are recomputed from the parameters printed on the sheets rather
than compared against rendered text: the Poisson interrelations, the cantilever
tip deflection and support-case ratios (1/3, 1/8, 1/48, 1/192), the Euler/yield
comparison for the 1 cm × 2 m rod, the equal-mass hollow section (3.5×), the
torsion core fractions (0.7⁴ = 24 % of J, 0.7² = 49 % of A), hoop/longitudinal
= 2 and the vessel stresses, the three wave speeds and the crustal inversion
(B = 53 GPa, ν = 0.242), thermal stress and rail numbers, the atomic-spring
estimates, α ≈ k_B/2D, the falling-weight quadratic with and without the rod
mass, the constant-stress decay length, the Mohr circle (R = 42.4,
σ₁ = 92.4, σ₂ = 7.6 MPa) and the specific-strength/specific-modulus rankings.

These are internal-consistency checks: they confirm the arithmetic reproduced
on the sheets is the arithmetic the stated model gives. They do not confirm
that the model is the right one for a real material.

## Visual review

Every page was inspected at full resolution during authoring, and the figures
were additionally rendered on contact sheets and re-checked after each fix.
Corrections made as a result of that review:

- JEE-08 had two cards with overlapping content and a diagram repeated from
  JEE-03; the scaling card and the section-property figure replaced them.
- OL-05's "deflection formulas" schematic was unreadable at page scale and had
  a caption that overstated a factor; replaced by a plotted comparison with the
  1/3, 1/8 and 1/48 lines marked.
- OL-07's I-section drawing had a dimension arrow through the figure and a
  neutral-axis label colliding with the section; redrawn.
- OL-08 reused the hoop-stress figure (already on OL-07); replaced by a new
  S-wave-shadow diagram with rays, core and shadow band drawn from the 0.55 R
  core ratio, and a note that the 103° edge is representative.
- OL-09's Mohr circle was drawn on squashed axes; rebuilt as a square inset with
  a numeric panel, and the principal stresses corrected from 97.7/2.3 (which
  treated the 30 MPa shear as 30 + 30) to 92.4/7.6.
- OL-03's bar chart showed a third bar value that did not follow from the
  stated "add all of m" comparison; the 10.7 mm value was recomputed.
- OL-04's taper schematic had the flare drawn downward and a label in the wrong
  place; redrawn with the load on top.
- JEE-07's "four modes" artwork left the figure area mostly empty; the figure was
  replaced with the contact-piece example used in the text.
- Footer strings overlapped the 125 px safe margin and were moved up 21 px.
- Several label collisions found by eye but not by the clip check: the torsion
  `γ = rθ/L` note, the bending neutral-axis label, the stress-element caption,
  the beam-case legends and the constant-stress taper labels.

## Known limitations

- The clip check asserts that no artist bounding box leaves its panel; it cannot
  detect two labels that overlap each other. Overlaps were caught by eye, not by
  code.
- mathtext has no `\tfrac`, `\Big` or `pmatrix`; the content avoids them rather
  than approximating them badly, so a few formulas are written in a longer form.
- The 300 DPI value is nominal metadata (299.9994 as written by Pillow); the
  pixel dimensions are exact.
- PDF pages are single images, so text inside a PDF is not selectable. The
  editable source is `sheets.json` plus the two content modules.
- Physics verification is as described above: representative checks, not an
  exhaustive proof of every statement.
