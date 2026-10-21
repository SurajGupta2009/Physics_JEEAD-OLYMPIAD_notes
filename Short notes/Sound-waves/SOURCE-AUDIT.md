# Source audit — sound-waves chapter

Primary source: `sound-waves/Sound-waves.md` (SHA-256 prefix `d2edcf5e`, verified
unchanged). The chapter text was **not modified**; all corrections live in these
sheets and are listed here. Checks are independent recomputations, stated as
representative rather than exhaustive.

## Corrections applied in the sheets

**(a) Resonance-tube length condition (Eq 2.15 / Trap 15).** The source prints
`l₁ = λ/4 + e`, `l₂ = 3λ/4 + e`, but its own boxed result `e = (l₂ − 3l₁)/2` and its
worked Q5 (l₁ = 16.5 cm, l₂ = 50.1 cm, f = 512 Hz → e = 3 mm) require
**l = λ/4 − e**: λ/4 = 16.8 cm and 16.8 − 0.3 = 16.5 ✓, while 16.8 + 0.3 = 17.1 ✗.
The sheets use l = λ/4 − e throughout (JEE end-correction and resonance-tube sheets).

**(b) Paper Q13 (Mach boom delay) — reassessed, answer 25.5 s is correct.** The
source derivation is verbally muddled ("d = h tan α? Actually … Might need more")
but its final line t = h cot α / v_s = 25.5 s matches the exact envelope derivation:
t = h√(M²−1)/(M v) = 10 000·√3/680 = 25.47 s for M = 2, h = 10 km, v = 340 m/s.
An alternative figure of ≈33.3 s sometimes derived for this problem is wrong: it
conflates the jet position at hearing (17.32 km past overhead) with the emission
point. The subtle correct statement (in the sheets): the boom heard at 25.5 s was
emitted at t_e = −t/(M²−1) = −8.5 s, i.e. while the jet was still 5.8 km before
overhead.

**(c) Paper Q16 overtone label.** The source labels 3v/4L = 750 Hz as the "second
overtone" of a closed pipe; by its own Trap 8 the second overtone is 5v/4L. 3v/4L is
the **first** overtone (third harmonic). The numeric answer 750 Hz is fine; the
sheets use correct overtone numbering and flag the trap.

**(d) Section E end-correction exercise.** The text specifies r = 1 cm but the
answer key values (166 Hz / 332 Hz) correspond to r = 2 cm (e = 1.2 cm, L_eff =
1.024 m → 166.0 / 332.0 Hz). At r = 1 cm the same setup gives 168.0 / 336.0 Hz. The
sheets give both rows of the table and state the r-dependence explicitly.

**(e) Worked Q1 amplitude ratio.** The worked example quotes ω/k = 200 while the
stated wave speed is 343 m/s; the source handles the inconsistency openly ("check
units"). The sheets use consistent v = ω/k and note the trap.

**(f) Impedance rounding.** The source quotes "Z_air ≈ 400 rayl"; ρv at 20 C is
412–413 rayl (ρ = 1.204 kg/m³, v = 343.2 m/s). The sheets use ≈412 and mention the
400-rounding convention.

**(g) Glide-slope formula and numbers.** The printed derivative
df′/dt|₀ = −f v_s²/(v b) is correct (independently re-derived), but the surrounding
remark under Eq (4.2) ("cos θ ≈ 1 while approaching") contradicts its own cos θ
parameterisation. The evaluated slope at the source-style example (f = 1000 Hz,
u = 20 m/s, b = 100 m, v = 340 m/s) is **−11.8 Hz/s**; the sheets state this value
and the sign structure (high side before the pass, slope negative through it).

## Open assumptions recorded

- Air density for impedance work: 1.204 kg/m³ at 20 C unless stated (the 400-rayl
  rounding is acknowledged, not used in numeric checks).
- The near-field correction 1/(1 + (d/2r)²) is an idealised point-source dipole
  form; the sheets present it as the exam model and note its limits.
- Kaplan-like listening-arc tables are exact arc-length facts of the printed
  spirals; the sheets use them as reading-train drills only.
- Ends corrections: e = 0.6133r (unflanged) and 0.8216r (flanged) are the exact
  classical constants; the sheets use the exam standards 0.6r and 0.85r and mention
  the precise values once.

## Verification of the source itself

All 3,065 inline-mathtext expressions in the sheets were preflighted through
matplotlib's mathtext parser; the physics model checks in `test_exports.py`
(representative, ~40 assertions) reproduce the source's worked answers (speeds
331.3/343.2 m/s, Newton 280 vs Laplace 331, He/H₂ speeds, intensity chain I → ΔP₀ →
β, Q4/Q5 end-correction chains, Doppler pair 1096.8/1088.2 Hz with 8.5 Hz
asymmetry, echo 1193.5 Hz vs 1176.5 linear, Mach geometry 17.32 km / 25.47 s /
58.82 s / −8.49 s, glide slope 11.76 Hz/s, Kundt 400 m/s, paper Q2/Q9/Q16/Q17/Q20/
Q36) and confirm the corrected forms are the ones present in the delivered sheets.
