# Kinematics source audit

## Primary sources and preservation

The primary sources are the repository chapters [`Kinematics-1d.md`](../../kinematics-1d/Kinematics-1d.md) and [`Motion-in-two-dimensions.md`](../../motion-in-two-dimensions/Motion-in-two-dimensions.md), including their theory and derivations, worked exemplars, concept checks, practice, examiner traps, Olympiad extensions, formula sheets and diagrams. Their source gates both pass (15 blocks each). Both files are left unchanged.

| Source | SHA-256 |
|---|---|
| `kinematics-1d/Kinematics-1d.md` | `711405418c8d8e033fbbbbe96fb3a4834f4d48b0ec0768ca884d87244b0d1954` |
| `motion-in-two-dimensions/Motion-in-two-dimensions.md` | `0ba4ba8477bffd12d1586bd0ebf514e67c4a97108cefa7231f93d4e1f7c55f2b` |

## Corrections / qualifications identified for the short-notes edition

The following discrepancies were independently checked and corrected/qualified in this edition. The detailed source files remain untouched.

| Source location / claim | Audit finding and planned treatment |
|---|---|
| 1-D Q6: cars start together, one east and one north; answer switches to a same-line case | The stated 2-D initial relative-velocity magnitude is `√(10²+10²) = 10√2 m/s`, not the unrelated 1-D closing speed 20 m/s. Since the separation is initially zero, phrase this as the initial rate at which separation grows (or replace with a nonzero initial separation for an ordinary derivative). Do not reuse the source answer. |
| 1-D Q24: at t = 2 s, v = −3 m/s and a = 0, described as “decelerating” | At that instant the speed has zero derivative because `a = 0`; it is neither speeding up nor slowing down instantaneously. Since `a` changes sign there while `v ≠ 0`, `x(t)` has an inflection at `t = 2 s`, but “decelerating” is still wrong. State the computed `v = −3 m/s` and `a = 0` and avoid that label. |
| 1-D variable-a validity, `v dv/dx` | This follows from the chain rule where x is a usable independent variable. Integration gives a relation for v²; choose the physical sign branch and handle turning points piecewise. The expression is not a license to treat arbitrary a(t,v,x) as a function of x alone. |
| 1-D Q21 train: acceleration then cruise then braking | The source’s final-velocity compatibility requires the train to stop and therefore `a₁t₁ = a₂t₂` for positive acceleration magnitudes. State that condition; otherwise the given phases are not fully specified by the solution. |
| 2-D P31 aircraft/wind answer | Sign error: wind **from the west** blows east, so to achieve a due-north ground track the aircraft must point **west of north**, not east. For wind from the northwest (blowing southeast), the crosswind compensation is westward, so the required heading is again west of north; the source's eastward labels are inconsistent with its component equations. Recompute vectors, not just the quoted angles. |
| 2-D P30 curvature values | The source's launch-point estimate uses `g cos 45° ≈ 7.07 m/s²` (g = 10), while its apex estimate uses `g = 9.8 m/s²`; the input does not select one value. Recompute all three points with one stated g. With g = 9.8 m/s², launch/landing `ρ ≈ 130 m`, apex `ρ ≈ 45.9 m`; with g = 10, launch/landing `ρ ≈ 127 m`, apex `ρ = 45 m`. |
| 2-D safety-parabola reachability wording | The envelope gives the maximum height at fixed horizontal x for a fixed launch speed in vacuum. “On or below the envelope is reachable” needs the domain/trajectory convention (forward shots and targets at or above the launch level, with a path segment before landing); it should not be read as permission to count underground points after impact. |
| 2-D relative-velocity aircraft formula | The scalar sine/cosine relations are valid only after defining along-track and cross-track wind components and a signed heading angle. Present the vector equation `v_ground = v_air + v_wind` first; then resolve components for the chosen geometry. |
| 2-D OL1/OL2 linear-drag projectile | The `t → ∞` horizontal integral is not the range of a projectile that has already landed. The source itself notes this for OL2. Do not present the infinite-time integral as a finite-flight range; use a fully specified numerical example with a stated landing event, or keep the analytic component solution and label the range as requiring a landing-time calculation. |
| 2-D OL9 pursuit curve | The stated power-law path is not safe to reuse as a stand-alone result: the initial target position/geometry is not stated, and the quoted exponent/finite-catch claims do not follow from the setup as written. Either derive a valid result for a precisely specified pursuit geometry or omit the formula and retain only the modelling/ODE insight. |
| Duplicate C5 in the 1-D checks and duplicate C1 in the 2-D checks | Editorial duplication; it adds no physics. The short notes use each check at most once. |
| Kinematics draft, OLY-08 numerical Coriolis estimate | Independent recomputation caught a factor-of-ten decimal error before release: `Ω v_N T² sin λ` with `Ω=7.29×10⁻⁵ s⁻¹`, `v_N=500 m/s`, `T=20 s`, and `λ=45°` is about `10.3 m`, not `1.03 m`. The authored card and diagram scale are corrected; the estimate remains first-order with constant northward speed/time and neglected feedback. |

## Independent checks completed for this edition

The standalone test suite independently checks representative signed 1-D and relative-velocity calculations, equal-height projectile roots and limits, the inclined-plane optimum, the envelope intercepts, curvature/normal-acceleration identities, linear/quadratic drag initial and terminal limits, and a Coriolis scale estimate. It also checks sheet counts, numbering, PNG geometry/DPI/printable inset, card fit at fixed body sizes, ZIP ordering and membership, A4 PDF page sizes/bookmarks, gallery links, source hashes, and asset-manifest hashes. The checks are representative, not an exhaustive proof of every line or exercise.

The pursuit extension uses the explicitly stated target path `r_T=(v_T t,0)`, pursuer initial position `(0,d)`, constant pursuer speed `v_P`, and line-of-sight steering. The numerical diagram integrates the coupled pursuer-coordinate ODE with RK4 and plots the pursuer in the same x-y plane as the target. For `v_P>v_T`, the separation derivative is bounded above by `v_T-v_P<0`, so the stated finite-capture upper bound follows. The diagram uses `v_P=2v_T` and `d=1.5` in arbitrary consistent units; it illustrates that setup, not a universal path.

## Assumptions to keep visible

1. The basic projectile formulas assume uniform gravitational acceleration, a locally flat inertial frame, and negligible air resistance. Equal-height `T`, `H`, and `R` formulas need equal launch and landing elevations; otherwise solve the vertical equation and choose the physically relevant root.
2. The standard constant-acceleration equations require acceleration to be constant over the interval. Piecewise-constant motion is solved interval by interval with continuous position and velocity unless an impulse is explicitly introduced.
3. Galilean relative velocities assume speeds small compared with c and a shared time coordinate.
4. Circular kinematics assumes a well-defined path radius at the instant; at a zero-speed cusp or non-smooth path, the usual curvature description can fail.
5. Linear and quadratic drag are idealised laws. Their applicability depends on flow regime, shape and relative air speed; terminal-speed formulas are model-specific.
6. The Coriolis estimate is first-order in Earth's angular speed and assumes a specified local frame and short enough flight that the neglected changes are small.

This is a working audit: it records identified discrepancies and the checks required for the edition. It is not a claim that every exercise in either source chapter has already been exhaustively certified.