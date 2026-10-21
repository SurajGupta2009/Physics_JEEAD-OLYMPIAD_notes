# Source audit — `fluid-mechanics/Fluid-mechanics.md`

The source file is **not edited**. This page records what was recomputed, what did
not survive, and what was not checked. Line numbers refer to the source as it stands
in this repository.

## 1. Method

1. Read the whole file: theory (§3.1–§3.19), the worked exemplars E1–E10, the
   25-question exercise set with solutions, the ten Olympiad items OL1–OL10, the
   toolkit and trap tables, the formula sheet, and the 36-question paper with its
   answer key.
2. Recomputed every formula in the theory and formula sheet from its own definitions
   (dimensions, sign, and the limit in which it should reduce).
3. Recomputed the arithmetic of every worked exemplar and Olympiad item, and the
   answer key entries that the sheets actually quote.
4. Where a printed number did not follow, reworked it from the stated data and used
   the reworked value on the sheet. The source keeps its original text.

## 2. Corrections carried onto the sheets

### 2.1 Exemplar E10 — capillary energies are a factor of ten too small (source line 780)

Printed: `U_g = 3.37×10⁻⁷ J`, adhesion release `6.8×10⁻⁷ J`.

With the stated data (`r = 5×10⁻⁴ m`, `h = 0.0297 m`):
`U_g = ½ρgh²πr² = ½·1000·9.8·(0.0297)²·π(5×10⁻⁴)² = 3.39×10⁻⁶ J`, and
`2πrhγcosθ = 6.79×10⁻⁶ J`. The printed pair has the correct **ratio** (the release is
twice the gain) but both values are ten times too small — a dropped factor of ten in
`h²πr²`. The sheet prints `3.4×10⁻⁶ J` and `6.8×10⁻⁶ J` and keeps the factor-two
argument, which is the point of the example.

### 2.2 Bubble coalescence — arithmetic slip changes the answer (source line 980)

The solution conserves `pV` isothermally. For the first bubble it correctly writes
`pV = (4γ/r)(4/3)πr³ = (16/3)πγr²`. For the second, of radius `3r`, it evaluates
`(4γ/3r)·(4/3)π(3r)³` as `16πγr²`; the bracket is `36πr³`, so the product is
`48πγr²`. Summing and matching the final bubble `(16/3)πγR²` then gives
`R² = 10r²`, i.e. **`R = √10 r ≈ 3.16r`**, not the printed `R = 2r`. The sheet uses
`√10 r`; the source is unchanged.

### 2.3 Exemplar E5(b) — answer right, wording ambiguous (source line 604)

The printed `a = 4.08 m/s²` is correct for the instant the tank floor is first
exposed (surface from the front-bottom corner to the back-top corner, slope 2.5/6).
The surrounding sentence implies volume conservation still holds at that instant; it
does not — water has been spilling since `a = 1.63 m/s²`. The sheet states the
spilling interval explicitly and keeps both numbers.

### 2.4 Siphon limit is an idealisation, not an error

The `10.3 m` ceiling is `p₀/ρg` with vapour pressure set to zero. At 20 °C water's
vapour pressure is 2.3 kPa, so the practical ceiling is about `10.1 m`. The sheet says
"about 10.3 m, less vapour pressure"; the source's number is not silently changed.

## 3. Checked and found consistent

* **Hydrostatics.** `dp/dy = −ρg`; `p = p₀ + ρgh`; the shrinking-wedge argument;
  gauge/absolute bookkeeping; `0.76 m Hg = 101.3 kPa`; water barometer `10.34 m`.
* **Manometry.** The step rule and E2 `7.83×10⁴ Pa`; Pascal lift `F₂/F₁ = A/a`
  with `F₁d₁ = F₂d₂` (E3 `392 N`, `1960 J`).
* **Plane and curved surfaces.** `F = p_cA`, `h_cp = h_c + I_c/(Ah_c)` (rectangle
  from the surface: `2H/3`); projection theorem; E4 `F_H = 5.88×10⁴ N`,
  `F_V = 2.52×10⁴ N`, `F = 6.4×10⁴ N` at `23.3°`.
* **Rigid-body motion.** `tanθ = a/g`; `z = z₀ + ω²r²/2g` by force balance,
  equipotential and centrifugal head; volume conservation (centre drop = half the
  rim rise); OL2 numbers `7.35 cm`, `3.7 cm`; the pump/balloon direction along
  `−g_eff` (E6).
* **Buoyancy.** Archimedes twice; `V_sub/V = ρ_b/ρ_f`; `BM = I/V`; the four-case
  ice ledger; E7 `3 mm` fall.
* **Bernoulli.** The derivation's work terms and signs; the four gates; the head
  form; E8 `Δp = 1470 Pa`, `v₁ = 0.443 m/s`, `Q = 1.77×10⁻³ m³/s` with
  `A₁ = 4×10⁻³ m²`, `A₂ = 10⁻³ m²` (the printed areas and answer are consistent).
* **Torricelli and draining.** `v = √(2gh/(1−(a/A)²))`; `x = 2√(h(H−h))`, maximum
  `H` at `h = H/2`; `T = (A/a)√(2H/g)`; Q13–Q15 (`1.2 m`, `6.26 m/s`,
  `5.2×10⁴ Pa`, `50.5 s`).
* **Momentum flux.** `ρav²` for a stopped jet, `ρa(v−u)²` for a moving plate,
  `1−cosφ` for a deflected jet.
* **Viscosity.** Shell balance `τ = rΔp/2L`; the parabolic profile;
  `Q = πR⁴Δp/8ηL`; `R = 8ηL/πR⁴`; the `16:1` split and `1/17` in the parallel
  example; Stokes `v_t = 2r²(ρ−σ)g/9η`; `Re = ρvD/η`; E9 `1.21 m/s`, `Re ≈ 16`
  (the source correctly calls Stokes invalid there); OL3 `r* ≈ 4×10⁻⁵ m`,
  `9.9 m/s` at 2 mm.
* **Surface tension.** `γ = F/2L` for a film and `γ = W/ΔA` (two faces);
  `2γ/r` drop, `4γ/r` bubble, `γ/r` jet; Jurin `h = 2γcosθ/ρgr`; short tube
  `hR = h′R′`; Q22 `4/3`, Q23 `−1.07 cm`; Q24 `0.058 N`, Q25 `8.2×10⁻⁶ J`.
* **Olympiad items.** OL1 `T = 50.5 s`, `τ = 8ηLA/(πr⁴ρg)`, `h* = 128η²L²/(ρ²gr⁴)`;
  OL4 catenoid limit `d/R ≲ 1.33`; OL5 Tate `0.048` naive → `0.073 N/m`,
  strider `0.035 N`; OL6 `5.9 m` capillary, `10.3 m` suction; OL7
  `c ≈ √(gh)(1+3η/4h)`; OL9 `ΔK = 0.40 J`; OL10 `v_t = 0.0380 m/s`,
  `v_meas = 0.0307 m/s`, `6.5 s`, `Re = 0.10`.
* **Limits.** Bulk modulus `B = 2.2 GPa` gives `≈5 %` at 11 km and
  `√(B/ρ) ≈ 1480 m/s`; `ω→0`, `r→0`, `η→0`, `γ→0` limits all reduce correctly.
* **Constants.** `p₀ = 1.013×10⁵ Pa`, `ρ_w = 1000`, `ρ_Hg = 13.6×10³`,
  `γ_w = 0.0728 N/m`, `η_w = 10⁻³`, `η_air = 1.8×10⁻⁵`, glycerine `1260`/`1.5`.

## 4. What was **not** verified

* The 36-question paper (source Part 11) was read for topic coverage and its answer
  key was spot-checked against the sheet numbers, but the paper was **not re-solved
  end to end**. A wrong distractor or an ambiguous stem there would not be caught.
* Individual answers Q1–Q25 were checked only where a sheet quotes the number
  (Q12–Q15, Q19–Q25); the remainder were read, not independently recomputed.
* The Cengage chapter that the source cites is not in this repository, so nothing
  was checked against the printed book — only against the file.
* Figures were checked for clipping, overlap and label collisions by rendering and
  inspection; they were not checked against the source's figure list one by one.
* `test_exports.py` recomputes 24 representative values. That is a smoke test, not a
  proof of every printed number on all 30 sheets.
