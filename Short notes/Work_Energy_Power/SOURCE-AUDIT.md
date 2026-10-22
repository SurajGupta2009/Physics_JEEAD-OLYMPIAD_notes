# Source audit — what was recomputed, what was corrected, what was not checked

Source of record: `work-energy-power/Work-energy-power.md` (1574 lines), built from
Cengage *Mechanics II* ch 2 §2.24–2.26 and *Mechanics I* ch 1 §1.17–1.19.
The Markdown was **not edited**. The source gate
`python3 tools/check.py`, run from `work-energy-power/`, returned ALL GOOD before
any content was written.

## 1. Corrections to the source

The physics in the 14 core sections and in OL1–OL10 was checked result by result.
**No wrong formula was found in the sections this edition uses.** The source is
internally consistent on every result that a sheet reproduces. Three things did
have to be handled rather than copied:

### 1.1 The source mixes g = 10 and g = 9.8

The worked solutions in Part 5 and OL9 use `g = 10 m/s²` (line 586:
`W_g = 2 × 10 × 2.5 = 50 J`; line 1139: `t₀ = sqrt(2h/g) = sqrt(2) = 1.414 s`).
This edition uses `g = 9.8 m/s²` on every sheet, so a student checking a number
against the source will see a small difference.

The only place where the difference is visible in a printed answer is OL9's
bounce time: the source's `g = 10` gives `t = 4.24 s` for `h = 10 m, e = 0.5`;
at `g = 9.8` the same formula gives `t = 4.29 s`. **OLY 03 prints 4.29 s**, and
`s = 16.7 m` — the distance is `g`-free and agrees exactly.

### 1.2 Two source answers are unfinished

* **Q1, line 1488** — the answer starts correctly
  (`½kx² = mgd sin30° + μ_k mg cos30° · d`, `d = 0.74 m`) but part (b) breaks down
  mid-sentence: *"…this is getting complicated. The key: the block has PE mgh' at
  the top …"*, and the return journey is never completed. **JEE 21 avoids the
  source's own numbers here** and uses its own spring-launch data
  (`k = 400 N/m`, `Δx = 0.15 m`, `μ_k = 0.25`, `m = 1.2 kg` → `d = 1.53 m`),
  which is checked from scratch in `test_exports.py`.
* **Q19, line 903** — the exact friction loss round a rough loop is correctly
  identified as an integral of `μ_k(mg cos θ + mv²/R)` and then abandoned for
  the estimate `μ_k·mg·2πR`. That is an honest estimate, not an answer, and no
  sheet presents it as exact.

### 1.3 A result quoted without its range (OL8, line 1133)

The source states the bead-on-hoop equilibria correctly —
`θ = ±cos⁻¹(g/ω²R)` for `ω²R > g` — but does not say what happens at
`ω = sqrt(g/R)` itself, where the two new equilibria merge with `θ = 0` and the
bottom changes from stable to unstable through a pitchfork. **OLY 08** states the
critical speed `ω_c = sqrt(g/R)` as the threshold and prints one number above it,
so the sheet cannot be read as "the bead always climbs".

## 2. Corrections to my own first draft

These were caught during the visual and numerical review of the rendered pages,
and are listed because the first draft was already on disk:

| Sheet | First draft | Corrected | Why |
|---|---|---|---|
| JEE 17, OLY 19 | `N = mv²/R − mg cos φ` | `N = mv²/R + mg cos φ` | with `φ` from the bottom, gravity's inward radial component is `mg cos φ`, so it *adds* at the bottom and subtracts at the top. The sign error made the top normal too small by `2mg`. |
| JEE 17 worked block | top normal `= 5.88 + 2.94 = 8.8 N` | `5.88 − 2.94 = 2.9 N` | consequence of the same sign. At `3R` above the bottom of an `R = 0.5 m` loop the bead is *just* above the `gR` threshold, so the normal is small, not large. |
| JEE 10 worked block | `∮F·dr = 3 J` | `|∮F·dr| = 3 J` | a circulation is a signed quantity; writing it equal to a positive number hides which way the arrows go. |
| OLY 04 | disc bottom speed `4.83 m/s` | `5.11 m/s` | `sqrt(2gh/(1+½))` with `h = 2 m` is `5.11`; `4.83` is the value for `I/mR² = 0.68`, which is no standard body. |
| OLY 06 | `ΔE = 3.2 × 10⁶ J/kg, about 30.6 MJ/kg` | `ΔE = 3.3 × 10⁷ J/kg = 33 MJ/kg` | the two numbers mixed `GM/R` with `GM/(2r)` and lost a factor of ten on the surface term. |
| OLY 14 | `γ = 1.51`, `K = 261 keV`, classical `44 %` low | `γ = 1.34`, `K = 175 keV`, classical `35 %` low | `γ` at `v = 0.667c` is `1.342`, not `1.51`; `0.51` was the `1/√(1−β²) − 1` value for `β = 0.855`. |
| OLY 17 | 200 m track used as a 200 m radius: `ω = 0.030`, `T = 838 s` | `R = 200/2π = 31.8 m`, `ω = 0.188`, `T = 133 s` | a track length is a circumference. Using it as the radius understated both ω and the meeting time by a factor `2π`. |

The figures that encode the same formulas were corrected with them: the
`vertical_energy` and `string_vs_rod` curves now start at `5gR` and `4gR`
respectively, the disc bar in `rolling_energy` reads `0.75`, and the
`curvature_fit` panel shows the whole range of both radii instead of a flat line.

## 3. What was independently recomputed

`test_exports.py` re-derives **every printed answer** from its own formula, not
from the sheet text. The 122 model checks in `verification-results.json` include:

* Part I: the crate work (590 J), the incline audit (98 / −42.4 J, 4.72 m/s),
  the braking force over 55 m (4.36 kN), the friction slide and its 0.27 K
  warming, the constant-power pair (2.83 and 5.66 m/s at 5 and 20 s, 250 s to
  20 m/s), the climb power (45.7 kW of which 30.7 kW is the slope), the loop
  test (3 J), the spring launch (2.30 J, 4.29 m/s), the U(x) turning points
  (−2 and 6 m, 11.3 m/s at the well), the spring pair split, the pump efficiency
  (0.653), the chain pull and its 1.02 W loss, the spring-plus-friction slide
  (1.53 m), the incline-plus-spring compression (0.317 m), 300 rpm in rad/s and
  m/s, the spin-up (α = 2.0, θ = 96 rad), ω × r, and the roundabout
  (2.60 m/s², μ = 0.27).
* Part II: the CM split (3 m/s, 18 J, 6 J lost), the effective potential at
  7000 km (−5.69, +2.85 × 10⁷ J/kg), the bounce series (0.80, 8.2 m, 5.45 s;
  and the source's 10 m case at g = 9.8), the three rolling bodies
  (5.29 / 5.11 / 4.43 m/s), the wedge (`u = 3.39`, `V = 0.587`,
  `v_b = 2.90 m/s`), the launch budget (6.26 − 2.94 = 3.3 × 10⁷ J/kg, 53 % of
  escape), the chain unroll (28.0 N, 3.4 W of 42), the hoop (`ω_c = 4.95`,
  `θ = 11.4°`), restitution (0.60, 36 % kept), the flywheel (`ω(6 s) = 21.2`,
  `t(40) = 21.3 s`), the pseudo work (0.20 J, 1.41 m/s), the vanishing curl of
  `(2xy, x²)` and its `U = −x²y`, the drag ceiling (9.2 and 11.6 m/s, +26 % for
  double power), the relativistic pair (γ = 1.342, 175 vs 114 keV, 35 %), the
  tangential/normal pair (8.10, 8.64 m/s², 20.3°), the exponential spin-down
  (5.05 rad/s, 31.3 rad), the lap time (838 s), the tension at 60° (15.8 N),
  both loop thresholds (3.13 m/s at the top of a half-metre loop; `gR = 4.9`),
  the string and rod minima (6.64 and 5.94 m/s; `6mg` at the bottom), the
  conical pendulum (3.40 N, 1.84 m/s, 2.05 s), the banked band
  (31.0 m/s and `v_min = 0` once `μ > tan 15°`), the rotor (9.04 m/s, 1.14 kN),
  and both radii of curvature (37.4 and 83.2 m at 25 m/s, 40°).

`_audit_figs.py` renders each of the 50 figures in its exact page slot and checks
every text object against the canvas: **0 of 50 with issues**. `_audit_text.py`
additionally checks text-on-text collisions in the same slot and reports
**0 of 50**. Neither can detect wrong physics — the visual pass did that, and it
is what found the six figure defects listed in §2.

## 4. What was NOT checked

* No claim that every sentence on all 50 sheets agrees with the source page by
  page. The chapter inventory in `SCOPE.md` is the map of what was taken where.
* No claim that a student can solve every problem in P1–P36 from these sheets.
  The paper was used to choose difficulty, not reproduced.
* The plots are checked for containment and collisions, not for being the best
  possible illustration. Two panels (the `wpe_map` tile diagram and the
  `decision_map` pair) are deliberately schematic.
* Style: the sheets use `g = 9.8 m/s²` throughout, two significant figures for
  most answers, and three where a comparison needs them. That is a house style,
  not a claim about precision — see the `quoting five figures` trap card on
  OLY 14.
