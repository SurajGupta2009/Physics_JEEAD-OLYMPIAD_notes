# Elasticity source audit

## Primary source and preservation

The repository's [`elasticity/Elasticity.md`](../../elasticity/Elasticity.md)
(1513 lines) is the primary source: theory, derivations, worked examples E1–E10,
the olympiad layer OL1–OL10, practice paper P1–P36 with solutions, the formula
sheet, the traps list and the checkpoint. It was read in full before authoring.

It is **unchanged**. No editor, formatter or exporter was run over it:

- Markdown SHA-256: `0d0488c88e006c8409d6014319567eeec9652f1c84de0cc44cabd9d30c0bcea8`

`elasticity/README.md` was also read for its coverage floor, its list of results
derived beyond the book, its Olympiad layer, and its stated omissions.

## Corrections and clarifications applied to this edition

These are places where the source's wording was ambiguous, internally
inconsistent, or where a number needed re-deriving. In every case the source
file is left as it is and the sheet carries the corrected statement.

| Item | Source wording | Treatment here |
|---|---|---|
| Sudden load, inelastic limit | "the elastic formula overestimates the extension" (implicitly, after yield) | A yielded bar stores less energy for the same peak force, so the elastic energy equation *underestimates* the extension. Sheet OL3 states the underestimate. |
| Free-rail cycling | "a year of daily cycles does not accumulate" | True only while the rail is free to breathe. A welded rail accumulates locked-in stress at installation temperature. Sheet JEE-04 qualifies the claim. |
| "Doubling the radius quarters the twist" | Used as a limit check in the source formula sheet | θ ∝ R⁻⁴, so doubling the radius divides the twist by **sixteen**, not four. The limit check on JEE-08 uses R⁻⁴ with the right factor. |
| Self-weight "equivalent to half the weight hung at the end" | Correct, but phrased as a coincidence | Presented as the exact integral of a triangular force distribution: δ = mgL/2AY = ρgL²/2Y. |
| Tube buckling at equal mass | Source gives 3.5× without saying which radius is held | Restated as equal **area**: R = 1.5 cm against r = 1.0 cm, r_in from R² − r² = const, giving 3.5×. |
| Seismic Poisson ratio | "ν about 0.24" from v_P, v_S | Recomputed from v_P² = (B + 4G/3)/ρ and v_S² = G/ρ: B = 5.3 × 10¹⁰ Pa, ν = 0.242. |
| "S-wave shadow at 103°" | Quoted as the boundary of the shadow | Used as a **representative** value for a core of radius 0.55 R; the true shadow edge depends on the velocity profile. The figure is scaled to that ratio and labelled so. |
| Tree limits | "hydraulic limit near 100 m, fifty times nearer than lambda" | λ_wood ≈ 7 km and the hydraulic ceiling ≈ 100 m differ by ~70×, not 50×. Sheet OL4 says seventy. |
| S-wave shadow vs P shadow | Both called "the shadow zone" in places | Kept distinct: a fluid core transmits P but not S, so the two shadows are different and the S gap is the diagnostic. |
| Constant-strain taper | Implied as a rival design target only | Given its own profile A ∝ exp(ρgx/2Y) and a numerical check that the flare at ordinary heights is about 1 %, so the model is not oversold. |
| Hysteresis "loop = heat" | Stated without qualification | Loop area is energy dissipated per cycle; the sheet adds that elastic after-effect is a separate, recoverable effect. |
| "Stiffness per kilogram" for sections | Used loosely for the I-beam | Replaced with the fair **equal depth and equal area** comparison (factor 1.9), and the arithmetic is shown. |
| Silk "wins by 24" | Ratio of specific strengths only | Kept, together with the opposite ranking on specific modulus (steel better by ~3), so the comparison is not one-sided. |

## Numerical values re-derived during authoring

Every number printed on a sheet was recomputed rather than copied. The
independent recomputation lives in `test_exports.py` (26 model checks); the
values that differ from a literal reading of the source are listed above.

Representative chain: Y = 2.0 × 10¹¹ Pa, G = 8.0 × 10¹⁰ Pa, ρ = 7800 kg m⁻³,
α = 1.2 × 10⁻⁵ K⁻¹, σ_y ≈ 2.5 × 10⁸ Pa. From these:

- Y = 3B(1 − 2ν) with ν = 0.29 gives B = 1.59 × 10¹¹ Pa, consistent with the
  1.6 × 10¹¹ Pa quoted on OL1.
- Cantilever 20 × 40 mm, L = 1 m, F = 200 N: I = 1.067 × 10⁻⁷ m⁴,
  δ = 3.1 mm — agrees with the source.
- Euler load for R = 1 cm, L = 2 m: 3.88 kN against 78.5 kN yield, ratio 20.
- Hoop/longitudinal = 2 by the two free-body cuts, independent of p, r, t.

## Assumptions that remain unresolved

1. **ν range** −1 < ν < 0.5 is the isotropic, positive-definite elasticity
   bound. Auxetic and anisotropic materials can fall outside the *apparent*
   range measured along one axis; the sheet says "admissible for an isotropic
   solid" and does not claim universality.
2. **Thin-wall vessel** results assume t ≪ r and a uniform membrane stress.
   The Lamé gradient is named as out of scope, not derived.
3. **Buckling** κ values (1, 2, 0.5, 0.7) are idealised end conditions. Real
   frames with sidesway need effective lengths from a code table; the sheet
   says so instead of pretending the four numbers are exhaustive.
4. **Seismic speeds** assume an isotropic, homogeneous, linear-elastic medium.
   Layering, anisotropy and attenuation all change the inversion; the numbers
   are representative averages, not a survey.
5. **The interatomic estimates** (Y ≈ D/r₀³, α ≈ k_B/2D) are order-of-magnitude
   results from a simple pair potential. They fail for rubber (entropy
   elasticity), for Invar (compensated expansion) and for strongly directional
   bonds. Both sheets carry that warning.
6. **Wave-transit criterion** t ≫ L/c is a necessary condition for the
   quasi-static energy method, not a sufficient one: a compliant support or a
   contact resonance can still invalidate it.
7. **Mohr circle** is an added extension, not source material. It is flagged as
   such in `sheets.json` and in `SCOPE.md`, and no claim is made that it cannot
   be examined in JEE.

## What this audit is not

It is not a line-by-line certification of all 1513 source lines, and it is not
a claim that every exercise in the chapter has been independently solved. It
records what was checked: the equations reproduced on the 17 sheets, the
numbers on them, the limiting cases named on them, and the specific source
statements above.
