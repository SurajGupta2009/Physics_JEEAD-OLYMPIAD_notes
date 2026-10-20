# Rigid body dynamics — print-ready short notes

**23 A4 portrait sheets: 19 JEE Main + Advanced, then 4 Olympiad / specialised extensions.**

## Downloads

| Selection | PNG-only ZIP | Exact A4 PDF |
|---|---|---|
| Part I — JEE (19) | [JEE PNGs](rigid-body-dynamics-jee-pngs.zip) | [JEE PDF](rigid-body-dynamics-jee.pdf) |
| Part II — extensions (4) | [Extension PNGs](rigid-body-dynamics-olympiad-pngs.zip) | [Extension PDF](rigid-body-dynamics-olympiad.pdf) |
| All — JEE first (23) | [All PNGs](rigid-body-dynamics-all-pngs.zip) | [Combined PDF](rigid-body-dynamics-short-notes.pdf) |

Open the [offline gallery](index.html) for individual-image downloads and separate part downloads. ZIPs contain only their selected PNGs. PDFs have one image per exact A4 page and one ordered bookmark per sheet.

- [Coverage checklist and relevance-based classification](SCOPE.md)
- [Source audit, corrections and unresolved assumptions](SOURCE-AUDIT.md)
- [Print instructions](PRINTING.txt)
- [Detailed original chapter](../../rotational-mechanics/Rotational-mechanics.md) — unchanged

## Print and design

Every PNG is **2480 × 3508 pixels**, RGB, **300 DPI** metadata; 125 px safe margins (~10.6 mm). PDF pages are exactly **210 × 297 mm**. Raster proportions differ from exact A4 only by pixel rounding. Use **A4, portrait, one sheet per page, Fit to page—not Fill/Crop**. Colour is recommended.

Prose uses Patrick Hand under the [SIL Open Font License](fonts/OFL.txt), included locally. Body type is 48 px (11.52 pt at 300 DPI), warnings/explanations 46 px (11.04 pt). Mathematics uses sharp Computer Modern mathtext at nominal 12 pt, with a bounded width fit no smaller than 10 pt. Nothing overflows by shrinking body text. Navy notes, teal explanations/headings, pale-yellow results, red conditions/traps; white background. Read top-left, top-right, bottom-left, bottom-right, then diagrams and reminder.

## Page index

| Part / local page | Image | Source locations |
|---|---|---|
| JEE 01 | [Rigid motion: geometry first](JEE/01-kinematics.png) | §§2, 3.1–3.2; D8.1 |
| JEE 02 | [MOI I: rods, plates & axes](JEE/02-moi-rods-plates.png) | §§3.3–3.4; D8.2; added JEE MOI derivations |
| JEE 03 | [MOI II: rings, discs & annuli](JEE/03-moi-circular.png) | §3.3; E1; Q1; added circular-lamina derivations |
| JEE 04 | [MOI III: cylinders & spheres](JEE/04-moi-solids.png) | §3.3; D8.2; added standard 3-D MOI derivations |
| JEE 05 | [MOI IV: composites & integrations](JEE/05-moi-composites.png) | §§3.3–3.4; Q18; added JEE integral/composite applications |
| JEE 06 | [Shift axes, do not guess](JEE/06-axis-theorems.png) | §3.4; E1; Q1, Q16; D8.3 |
| JEE 07 | [Torque, work & massive pulleys](JEE/07-torque-energy.png) | §3.5; Part 8 traps 10, 12; Q5, Q13 |
| JEE 08 | [Angular momentum: choose O](JEE/08-angular-momentum.png) | §§3.6–3.7; E5, E10; Q11; D8.6 |
| JEE 09 | [Rolling is a velocity constraint](JEE/09-rolling-geometry.png) | §3.8; C5; §§7.1–7.3; D8.5 |
| JEE 10 | [Inclines: friction sets the regime](JEE/10-incline.png) | §3.8; E2; Q2, Q4, Q17, Q25; P27 |
| JEE 11 | [Slipping: follow the contact speed](JEE/11-slip-to-roll.png) | §3.9; E4; Q8, Q19; OL1; P29; D8.8 |
| JEE 12 | [Driven rollers & spool reversal](JEE/12-driven-rolling.png) | E9; Q24; OL4; P35 (corrected) |
| JEE 13 | [Unwinding strings & energy](JEE/13-yoyo.png) | OL2; P31 (corrected); Part 8 trap 12 |
| JEE 14 | [Impact first, swing second](JEE/14-collisions.png) | §3.10; E3; §§8–9.6; P28; D8.9, D8.12 |
| JEE 15 | [Impulses: free bodies & hinges](JEE/15-free-impacts.png) | §3.10; Parts 7–9; added core impulse/restitution derivations |
| JEE 16 | [Equilibrium, slipping & tipping](JEE/16-equilibrium.png) | §3.11; E8; Q9; C12; D8.10 |
| JEE 17 | [Energy, reactions & curved rolling](JEE/17-energy-contact.png) | Q10; §§3.8, 3.10; added support/loop applications |
| JEE 18 | [Rigid-body oscillations: SHM link](JEE/18-oscillations.png) | E7; Q7, Q20; OL6; P30, P32 |
| JEE 19 | [Sliding rod & final JEE checks](JEE/19-sliding-rod.png) | OL3; P33 (corrected); Parts 7–9, 13–14 |
| Olympiad 01 | [Beyond scalar inertia](Olympiad/01-tensor.png) | §3.6; OL8 (corrected); §10.2 |
| Olympiad 02 | [Gyroscopes: torque turns L](Olympiad/02-gyroscopes.png) | §3.12; E6; OL7; P36; §§4.2, 9.2 (corrected) |
| Olympiad 03 | [Flywheel limits: add a material law](Olympiad/03-flywheel.png) | Q13 (core on JEE 04); OL10; P34 |
| Olympiad 04 | [Open systems & missing constraints](Olympiad/04-model-boundaries.png) | OL5; OL9; §10.2; Part 14 |

## Rebuild

From this folder, in a Python virtual environment:

```sh
python -m pip install -r requirements.txt
python author_content.py
python render_sheets.py
python build_exports.py
python test_exports.py
```

`author_content.py` and `revise_content.py` are the editable teaching text; `sheets.json` is its generated render manifest. `diagrams.py` and `extra_diagrams.py` contain native, computed diagrams/graphs. Rendering uses no network or image-generation model. The included font makes the notes portable. Dependency ranges are in `requirements.txt`; versions used for the supplied files are in `BUILD-ENVIRONMENT.txt`.

## What was checked

- All displayed formulas pre-parsed; all 92 cards checked for line width and vertical overflow, no body-type shrinkage. Formula fitting has a hard lower bound.
- All 46 diagram panels checked for text extending beyond panel bounds. Graphs are computed, not hand-sketched approximations. Bounds checks do not guarantee no internal label overlap; visual review was also performed.
- Every PNG checked for dimensions, DPI and white outer 120 px (~10.16 mm) on all sides.
- All three ZIPs checked byte-for-byte for PNG membership, order and CRC integrity; no other files are included.
- All three PDFs checked for page count, exact A4 media boxes, bookmark destinations/order, and **actual embedded raster bytes** against the corresponding PNG. This checks image order, not only labels.
- Gallery and these documentation links checked locally; gallery has no network dependencies. HTML printing is secondary to the verified PDF exports.
- Independent representative numerical/conservation checks cover spin-up, backspin/reversal, top-pull friction, spool winding, yo-yo tension, collision loss, overhang, sliding-rod detachment, pendulum, dumbbell direction, elastic-disc energy, numerically integrated MOIs, free-target restitution and contact limits. See [verification.json](verification.json).
- Visual review of all pages and enlarged diagram panels; source audit records original ambiguities and corrections. This is **not exhaustive certification of every source exercise**, nor validation of real carpet, peg-contact or dissipative-top models.

The revised edition replaces the original 14-sheet JEE set in place. It has **19 JEE sheets, 231 displayed equations and 76 JEE concept/derivation cards**. Four dedicated MOI sheets cover standard axes, derivations and unfamiliar-shape methods. New free-impact and energy/contact sheets fill gaps. Existing sheets have additional derivations, results and limiting checks. Body type is unchanged; tighter paragraph/equation spacing and fuller cards make the notes denser. The average occupied JEE card height is about 83% of its available height (including headings and padding), compared with about 70% in the earlier set; this is a layout measure, not a literal ink-coverage percentage. Existing capacitor notes and all original detailed chapter content are preserved; this is the only rigid-body short-note edition in this folder.
