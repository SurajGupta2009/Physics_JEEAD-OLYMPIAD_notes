# Kinematics — JEE and Olympiad short notes

A compact, teacher-style PNG study set for **one-dimensional motion, projectiles, relative velocity and circular kinematics**, with carefully fenced drag, pursuit and rotating-Earth extensions. The two repository chapters are references, not a fixed outline: the short notes use a learning-first order and add corrected explanations where needed. Neither detailed chapter is edited.

## At a glance

- **Part I — JEE Main + Advanced:** 26 A4 sheets, `JEE-01`–`JEE-26`
- **Part II — Olympiad / specialised extensions:** 10 A4 sheets, `Olympiad-01`–`Olympiad-10`
- **36 sheets total:** 144 concept cards and 72 labelled diagram/graph panels
- Each PNG is **2480 × 3508 px, A4 portrait, 300 DPI**; print one image per page using **Fit to page**, not Fill/Crop.
- Main prose is fixed at 11.52 pt equivalent; explanations at 11.04 pt. Overflow is a build failure, never hidden by shrinking text.

## Downloads

| File | Contents |
|---|---|
| [`kinematics-all-pngs.zip`](kinematics-all-pngs.zip) | Primary download: all 36 PNG sheets, JEE first |
| [`kinematics-short-notes.pdf`](kinematics-short-notes.pdf) | Combined A4 PDF, one sheet per page, bookmarked |
| [`kinematics-jee-pngs.zip`](kinematics-jee-pngs.zip) / [`kinematics-jee.pdf`](kinematics-jee.pdf) | Part I only |
| [`kinematics-olympiad-pngs.zip`](kinematics-olympiad-pngs.zip) / [`kinematics-olympiad.pdf`](kinematics-olympiad.pdf) | Part II only |
| [`index.html`](index.html) | Offline gallery with individual PNG downloads |

The PNGs are also available directly in this folder. Coverage and classification are in [`SCOPE.md`](SCOPE.md); corrections and assumptions are in [`SOURCE-AUDIT.md`](SOURCE-AUDIT.md); checks actually run are in [`VERIFICATION.md`](VERIFICATION.md); print settings are in [`PRINTING.md`](PRINTING.md).

## Part I — JEE Main + Advanced

| Sheet | Focus |
|---|---|
| 01 | Position, path, displacement, distance and frames |
| 02 | Average and instantaneous velocity; speed |
| 03 | Acceleration, sign logic and speeding up/slowing down |
| 04 | x-t, v-t and a-t graph slopes and areas |
| 05 | Derivation and validity of constant-acceleration equations |
| 06 | Free fall and vertical throws |
| 07 | nth-second displacement and reversal caveat |
| 08 | Variable acceleration a(t), a(v), a(x) |
| 09 | v dv/dx, branches and turning points |
| 10 | Relative motion and catch-up on a line |
| 11 | Piecewise motion, braking and reaction distance |
| 12 | Projectile components and independence |
| 13 | Horizontal launch from a height |
| 14 | Equal-height time, maximum height and range |
| 15 | Trajectory, velocity direction and speed at a height |
| 16 | Complementary-angle range twins and maximum range |
| 17 | Unequal launch/landing heights and impact velocity |
| 18 | Projectile range on an inclined plane |
| 19 | Safety envelope and reachable region |
| 20 | Relative velocity in two dimensions |
| 21 | River crossing, drift and aim |
| 22 | Aircraft and wind, with sign-audited vectors |
| 23 | Angular displacement, speed, period and frequency |
| 24 | Derivation of centripetal and tangential acceleration |
| 25 | Curvature and normal acceleration |
| 26 | Method map, validity fences and final checks |

## Part II — Olympiad / specialised extensions

The boundary is relevance and additional modelling, not difficulty; no claim is made that an extension can never appear in JEE.

1. Independent-variable selection for variable-acceleration laws and physical branches.
2. Linear drag, exact transient, terminal speed and limiting behaviour.
3. Quadratic drag, signed force law, terminal speed and hyperbolic-tangent solution.
4. Reaction time plus braking, with speed-scaling checks.
5. Linear-drag projectile components and finite landing-event calculation.
6. Constant horizontal deceleration as an explicit simplified headwind model.
7. Moving-target interception with gravity: position equality and physical-root checks.
8. First-order Coriolis deflection estimate with stated latitude and flight-time assumptions.
9. Planar pursuit: a specified initial geometry, line-of-sight ODE, and a finite-capture bound for a faster pursuer; no unsupported universal closed form.
10. Newtonian/vacuum/smooth-path validity limits.

## Corrections carried into this edition

- The 1-D source's perpendicular-car example is treated as a 2-D relative-velocity problem; its initial separation-growth rate is `10 sqrt(2) m/s`, not the unrelated same-line `20 m/s` case.
- The 1-D source's `t = 2 s` example has `v = -3 m/s` and `a = 0`: the speed is at an extremum at that instant, not undergoing nonzero instantaneous deceleration.
- The aircraft/wind answer is sign-corrected: a wind blowing east requires a westward air-velocity component for a due-north ground track.
- The source's mixed-g curvature example is not reused; this edition states a single `g` convention wherever a numerical curvature is calculated.
- Infinite-time horizontal displacement under linear drag is not called a finite projectile range; range is evaluated at the actual landing event.
- The under-specified source pursuit power law is not copied. The extension gives a fully stated geometry and derives the governing ODE and capture bound.
- An independent recomputation caught and fixed a factor-of-ten decimal slip in the draft Coriolis example before release: the stated parameters give about 10.3 m, not 1.03 m.

See [`SOURCE-AUDIT.md`](SOURCE-AUDIT.md) for derivations, limits, unresolved assumptions and source hashes.

## Rebuild

From this folder, using Python 3.11+:

```bash
python -m pip install -r requirements.txt
python author_content.py
python render_sheets.py
python build_exports.py
python test_exports.py
```

All authoring, diagrams and exports are offline. The original source files are inputs for reference only and are not rewritten by the scripts. The packaged Patrick Hand font is licensed under SIL OFL; see `fonts/OFL.txt`.
