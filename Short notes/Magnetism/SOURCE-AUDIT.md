# SOURCE-AUDIT — Magnetism

Primary source: [`../../magnetism/Magnetism.md`](../../magnetism/Magnetism.md) (3,016 lines; SHA-256 `86d3deb0ac086e68b20644eaf24626a87c18510aad8843b1575d62d7a00f9bba`). The detailed chapter is **unchanged**; corrections below are recorded here and applied only in the short-note sheets.

## Method

The chapter's theory (§§3.1–3.38), toolkits, traps, extension sections (§§10.1–10.7) and the OL worked problems were read before writing. Every identity used in the sheets was checked independently: closed forms were re-derived or re-evaluated numerically, and `revalidate.py` re-checks the core results by direct quadrature, numerical differentiation and ODE integration (see `verification-recheck.json`). Checks are representative, not an exhaustive certification of every sentence of the source.

## Correction applied in the sheets

1. **OL3 magnetised-sphere moment (numerical slip).** For a sphere of radius R = 1 cm with uniform M = 10⁶ A/m the source quotes μ = 0.52 A m². Its own formula μ = (4/3)πR³M gives **μ = 4.19 A m²**, and the source's own continuity check (exterior pole dipole field equals the interior ⅔μ₀M) passes only with 4.19 A m²: (μ₀/4π)·2μ/R³ = ⅔μ₀M requires μ = MV. The quoted far-field value 8.4 × 10⁻⁴ T at r = 5R follows the same slip; the corrected value is **6.7 × 10⁻³ T**. (The source numbers correspond to R = 0.5 cm with R = 1 cm stated elsewhere in the same problem.) The sheets use the consistent set; the source is left untouched.

## Checked and confirmed against the source as printed (no correction needed)

2. **OL9 two-carrier Hall values.** Both quoted numbers re-substitute correctly in the source's own formula: germanium at room temperature R_H = +2.5 × 10⁻³ m³ C⁻¹, and intrinsic (n = p = 3 × 10²⁰ m⁻³) R_H = −7.2 × 10⁻³ m³ C⁻¹ (numerator −3.48 × 10¹⁹, denominator 4.85 × 10²¹). A preliminary scratch division in the check pipeline initially disputed the second value by two powers of ten; independent recomputation confirmed the source. The sheets print the source values.

## Clarifications stated explicitly in the sheets (not errors)

3. **Finite-solenoid cosine convention.** The source's B = ½μ₀nI(cos θ₁ + cos θ₂) uses both end angles positive for an interior point. Other texts measure both angles from one direction and subtract. The sheets fix one convention and warn about the other.
4. **Coax-shell formula.** μ₀I(c² − r²)/2πr(c² − b²) applies to the gap of a neutral coax whose return current fills the outer shell; the sheets state the enclosed-current ledger that produces it.
5. **Heart-field scaling.** The source's ~100 pT at 10 cm uses a *current* dipole (A m, field ∝ 1/r² in a conducting volume), not an orbital magnetic dipole (A m², 1/r³). The sheets state both units and powers explicitly, since mixing them is a common error.
6. **OL10 pressure method.** The independent pressure estimate agrees with the image-dipole force only within a factor of about two; the source says so and the sheets repeat the caveat — it is an area estimate, not a second exact method.
7. **Solenoid end field.** μ₀nI/2 at an end is the infinite-solenoid limit approached from inside; the sheets label the finite-length leakage of order R/L.

## Verified as stated (sample of independent checks)

- Lorentz geometry, zero work; r = mv⊥/qB, T = 2πm/qB; electron 28.0 GHz/T, proton 15.2 MHz/T; proton spin 42.6 MHz/T distinguished from orbital frequency.
- Selector v = E/B; strip-crossing sin φ = d/r and half-period return; spectrometer r = √(2mV/q)/B and Δr/r = ½Δm/m (U-235/238 separation 5.6 mm re-computed).
- Cyclotron f = qB/2πm, K = q²B²R²/2m (27 MeV example), 3 % relativistic offset at 27 MeV.
- Mirror invariant μ = mv⊥²/2B; loss cone arcsin√(B₀/B_max) = 18.4° at ratio 10.
- Hall V = IB/nqt: copper 0.73 μV, semiconductor 0.31 V re-computed; carrier-sign logic (same edge, opposite voltage).
- Cycloid x = (E/B)(t − sin ω_c t/ω_c), height 2mE/qB², top speed 2E/B; E×B drift free of q and m; gradient-drift sign and structure.
- Biot–Savart constant μ₀/4π; moving-charge B = v×E/c² with μ₀ε₀ = 1/c² (numeric identity checked).
- Wire μ₀I(sin α + sin β)/4πd with signed end angles; infinite and semi-infinite limits; square 2√2μ₀I/πa and hexagon √3μ₀I/πa at centre (both re-derived).
- Loop μ₀I/2R, arc μ₀Iθ₀/4πR, axis μ₀IR²/2(R²+x²)^{3/2} (peak at centre); N-gon → loop limit.
- Solenoid end = ½ interior; toroid μ₀NI/2πr; Ampère sign convention (5 A out, 3 A in → 2.5 μT m example re-computed).
- Thick wire μ₀Ir/2πa²; sheet μ₀K/2 each side; hole ½μ₀J×d; overlap-gap uniformity.
- Chord theorem; closed-loop zero net force in uniform B; τ = μ×B, U = −μ·B with τ = −dU/dθ checked; galvanometer φ = NABI/κ.
- Parallel-wire force μ₀I₁I₂/2πd (attraction for parallel currents); pressure and energy density B²/2μ₀ (1 T = 3.98 × 10⁵ Pa ≈ 4 atm; 1 T / 10 cm² → 400 N end force).
- Gyromagnetic μ/L = Q/2m for ring/disc; Bohr magneton 9.27 × 10⁻²⁴ A m²; rotating-disc B = μ₀σωR/2.
- Bound current K_b = M×n̂, slab rim I_b = Mt; magnetised sphere B_in = ⅔μ₀M (0.84 T at M = 10⁶ A/m), moment MV = 4.19 A m² (corrected), pole continuity of dipole exterior.
- H = B/μ₀ − M, ∮H·dl = I_free; μ_r = 1 + χ; gapped circuit B ≈ μ₀NI/(g + ℓ/μ_r); saturation cap 2.1 T.
- Larmor shift ω₀ ± eB/2m and χ_dia = −μ₀nZe²⟨r²⟩/6mₑ (water −9.5 × 10⁻⁶ against measured −9 × 10⁻⁶, with the ⟨r²⟩ caveat); Curie tanh law and χ = μ₀nμ²/k_BT; adiabatic demagnetisation T_f = T_i(B_f/B_i).
- Hysteresis loss ∮H dB = loop area (20 W worked example re-computed); exchange estimate kT_c ≈ zJ/3 ≈ 1500 K versus dipole coupling 0.04 K.
- Earth: B_H, B_V, declination; tan θ_dip = 2 tan λ (dip 60° → λ = 41°); μ_⊕ ≈ 8 × 10²² A m² from B_eq = 30 μT; core current 2 × 10⁹ A; Gauss absolute method (μ = 0.58 A m², B_H = 25 μT re-computed).
- Helmholtz d = R, B(0) = (8/5√5)μ₀NI/R = 0.716 μ₀NI/R, flatness coefficient 144/125 verified against the exact axial field; anti-Helmholtz gradient named.
- Two-carrier Hall sign rule nμₙ² = pμ_p²; levitation height (3μ₀μ²/32πmg)^{1/4} = 2.7 cm for a 7.5 g, 1 A m² magnet (re-computed with the mass in kg — the source's 2.7 cm is correct); Fermi gain ≈ 4V/v; synchrotron γ-frequency and 27 keV/turn at 1 GeV, r = 3.3 m; radiation-belt clocks 17 ms / 2 s / 1300 s order.

## Unresolved assumptions (stated, not silently absorbed)

- Ideal uniform fields and thin wires/sheets throughout Part I; fringing named where it limits a formula.
- Linear-media formulas (μ_r constant) exclude ferromagnets, where the hysteresis loop is the model.
- Dipole/Earth formulas assume a centred, aligned dipole plus stated local anomalies; the 11° tilt and secular drift are noted as limits.
- Classical picture of diamagnetism gives the right magnitude and sign but not a quantum derivation; exchange, g = 2 and superconductivity are named with their scales only.
- All checks are representative; they do not certify every sentence or every exam context of the source.
