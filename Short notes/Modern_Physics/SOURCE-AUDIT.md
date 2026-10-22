# Source audit — atomic structure, the photon, X-rays, nuclei

The four source files are **not edited**. This page records what was read, what was
recomputed, what did not survive, and what was not checked. Section numbers refer to
the files as they stand in this repository.

## 1. Method

1. Read each file whole, not just the theory: `Atomic-structure.md` (Part 24, theory
   §3.1–§3.12, exemplars E1–E12, traps 1–11, OL1–OL12, formula sheet, paper),
   `Photoelectric-effect.md` (Part 23, §3.2–§3.12, the exemplars, traps and the
   Olympiad items), `X-rays.md` (Part 25, §3.1–§3.12, E1–E12, traps 1–10, the
   Olympiad set), and `Nuclear-physics.md` (Part 26, theory §3.1–§3.14, worked
   exemplars E1–E12, practice Q1–Q28, traps 1–11, OL1–OL12, and the 36-question
   paper read for coverage).
2. Recomputed every formula in the theory and formula sheets from its own
   definitions — dimensions, sign, and the limit in which it must reduce to the
   classical or non-relativistic case.
3. Recomputed the arithmetic of the worked exemplars and the Olympiad items whose
   numbers appear on a sheet.
4. Where a number did not follow from its own data, it was reworked here and the
   reworked value printed. The source keeps its original text.

## 2. Corrections and decisions carried onto the sheets

### 2.1 Compton recoil energy — my own arithmetic error, corrected before shipping

The first render of `Olympiad-05-compton` printed
`K_e = 100·2(0.196)/(1 + 2(0.196)) = 56 keV`. The bracket is right but the division
was dropped: `100 × 0.392/1.392 = 28.2 keV`. The sheet now prints **28 keV** and the
back-scatter note says the transfer stays well below the photon energy. Rechecking
the neighbouring cases: 90° gives `16.4 keV` and 180° at 200 keV gives `88 keV`, so
the factor-two slip would have been visible in any comparison — this is exactly the
kind of error the recomputation pass exists to catch.

### 2.2 Duane–Hunt written with `hc/e` in volts and with `1.24×10⁶` in pm

Both forms on the sheets are the same statement: `λ_min = hc/eV` and
`λ_min = 1.24×10⁶/V pm`. The constant is `1.2398×10⁶ pm·V`; the sheets use
`1.24×10⁶`, which is inside the printed precision of every example (0.02 %).
No correction was needed, but the rounding is deliberate and consistent across
`Olympiad-01`, `Olympiad-02` and `JEE-02`.

### 2.3 Moseley's screening constant is written `(Z − 1)`, not `(Z − σ)`

The Kα line uses `b = 1` because one K electron remains to screen the nucleus. The
sheets say so and warn that L lines need a different `b ≈ 7.4`. Writing the law as
`√f = √(3cR/4)(Z − 1)` is therefore a model with a stated assumption, not a
universal fit; `Olympiad-09` prints the assumption on the sheet.

### 2.4 "Intensity does not change `K_max`" is an idealisation with a stated caveat

At very high intensity a metal surface heats, and thermionic emission adds a current
with its own energy distribution. The sheets keep the ideal statement (it is the one
the exam tests), and `JEE-12` says explicitly that the battery measures energy per
electron while the ammeter measures electrons per second — not that the ammeter is
immune to the metal getting hot.

### 2.5 The classical collapse time is quoted with its assumption

`τ = 1.6×10⁻¹¹ s` follows from Larmor radiation with the electron on a circular
orbit of radius `a₀`. It is a classical estimate, not a measured lifetime; the sheet
says so and uses it only to make the point that the spiral is slow (`~10⁵` turns).

### 2.6 Nuclear: the beta-plus endpoint and the electron rule

`Nuclear-physics.md` E5 asks for the positron endpoint of N-13 with atomic masses
13.005739 u and 13.003355 u. The Q value must keep the `2m_e` term, because the
daughter's atomic mass counts one electron fewer than the parent's plus the emitted
positron:

`Q = (13.005739 − 13.003355 − 2(0.000549))(931.5) = 1.20 MeV`.

The sheet prints 1.20 MeV and states the rule rather than the number alone, because
this is the one place in the chapter where an arithmetic slip is invisible: without
the `2m_e` the answer would be 2.22 MeV, which is larger than the parent–daughter
mass difference could ever allow. Verified against the source's stated answer.

### 2.7 Nuclear: pairing, not fissility, decides thermal fission

The source's OL3 explains why U-235 fissions with thermal neutrons and U-238 does
not. The fissilities are 36.0 and 35.6 — far below the `Z²/A ≈ 50` limit for a
vanishing barrier — so fissility alone cannot decide anything. The sheet therefore
leans on the excitation ledger (6.5 MeV for even–even U-236 against 4.8 MeV for
odd–even U-239, with a pairing bonus of 12/√236 ≈ 0.78 MeV) and says explicitly that
`Z²/A` sets the trend, not the outcome. That is the source's own physics, made
load-bearing on the page.

### 2.8 Nuclear: "ten half-lives" is a rule of thumb, and is labelled as one

Ten half-lives leave 0.098 %, not zero. The sheet says 0.1 % and calls it engineering
shorthand; it does not claim the activity vanishes. Similarly `1.05 kg per GW·day`
is the *fissioned* mass: the fed mass at 4 % enrichment is ≈26 kg, a distinction the
sheet draws on `Olympiad-21`.

### 2.9 Nuclear: the 200 MeV ledger in the source sums to 205

`Nuclear-physics.md` §3.x splits the fission energy as fragments ≈165, neutrons ≈5,
betas and gammas ≈25, neutrinos ≈10 MeV. Those add to 205, not the 200 MeV the same
paragraph and the rest of the chapter use. The sheet keeps the 200 MeV total and
prints 20 MeV for the beta/gamma share (165 + 5 + 20 + 10 = 200), which is also the
usual textbook split: ≈190 MeV recoverable, ≈10 MeV carried off by antineutrinos.
The source figure is not edited; this is the rework noted here.

## 3. Checked and found consistent

* **Rutherford.** `θ ≈ kZe²/KR` for a spread charge; `tan(θ/2) = kZe²/mv²b = r_h/2b`
  with `r_h = 2kZe²/K`; `f = πb²nt`; `b₉₀ = 22.8 fm`; `r_min = 45.5 fm` at 5 MeV on
  gold; `K_fail ≈ 32 MeV` for `R = 7 fm`; the `sin⁻⁴(θ/2)` normalisation
  `(r_h/4)²`.
* **Bohr model.** Closure `2πr = nλ` gives `mvr = nħ`; force balance gives
  `r_n = n²ħ²/m_eke² = 0.529 n²/Z Å`; `v_n = 2.19×10⁶ Z/n m/s`;
  `E_n = −13.6 Z²/n² eV`; `K = −E`, `U = 2E`. Hydrogen `n = 3`: `r = 4.76 Å`,
  `v = 7.29×10⁵ m/s`, `λ = 9.97 Å`, and `3λ = 2πr` to four figures.
* **Spectra.** `1/λ = R(1/n_f² − 1/n_i²)`; Hα 656.3 nm, Lyman α 121.6 nm,
  Balmer edge 364.6 nm; the five series named by `n_f = 1…5`.
* **Excitation.** 10.2 / 12.09 / 12.75 eV for `n = 2, 3, 4`; electron impact can
  transfer part of its energy, a photon cannot; the 12.5 eV comparison on JEE-06.
* **Scaling.** `E ∝ Z²μ`, `r ∝ 1/(Zμ)`: He⁺ −54.4 eV / 0.265 Å; Li²⁺ −122.4 eV /
  0.176 Å; Li²⁺ 2→1 at 13.5 nm; muonic hydrogen 256 fm and −2.81 keV; positronium
  1.06 Å, −6.8 eV, 243 nm.
* **Quantum numbers.** `n, l, m_l, m_s`; `l < n`; `Δl = ±1`; `μ_B = eħ/2m_e =
  5.79×10⁻⁵ eV/T`; the `2n²` count per shell.
* **Photons.** `E = hf = hc/λ`; 550 nm ↔ 2.25 eV; `n = P/hf`; `p = h/λ`;
  radiation pressure `(P/c)(1+R)`; `100 W` at `2 m` → `1.99 W/m²`.
* **Photoelectric effect.** The five facts; `K_max = hf − φ`, `eV_s = K_max`;
  `λ₀ = 1240/φ nm`; Na `φ = 2.28 eV` → 544 nm, 400 nm gives `K_max = 0.82 eV`;
  slope `h/e = 4.14×10⁻¹⁵ V·s`; Zn `φ = 4.3 eV` → 288 nm and 0.66 eV at 250 nm.
* **Matter waves.** `λ = h/p = 1.226/√V nm`; 100 V → 1.23 Å; 100 kV → 3.88 pm
  (non-relativistic); Davisson–Germer 54 V → 1.67 Å at the 50° peak;
  NaCl `d = 282 pm`, first order at 15.8° for 154 pm.
* **Uncertainty estimate.** `E(r) = ħ²/2m_er² − ke²/r` minimised at `a₀`;
  the two terms at `r = 0.5 Å` are 15.3 and −28.8 eV, sum −13.5 eV against the exact
  −13.6 eV.
* **X-ray continuum.** `λ_min = hc/eV`; 100 kV → 12.4 pm; the edge moves with
  voltage and not with target `Z`; the hump's shape is the electron energy loss.
* **Characteristic lines.** `E_Kα = ¾(13.6)(Z−1)² eV`; Cu 8.0 keV / 155 pm, Mo
  72 pm, Ag 57 pm; thresholds 9, 20, 70 kV; the L-series screening warning.
* **Absorption.** `I = I₀e^{−μx}`; `μ ∝ Z³/E³`; lead at 100 keV `x½ = 0.123 mm`,
  `0.82 mm` for 1 % transmission; the apron range 0.25–0.5 mm is qualified as
  scatter protection, not beam protection.
* **Bragg.** `2d sinθ = nλ` with `θ` from the plane; `N_A = M/2ρd³ = 6.02×10²³`
  from NaCl data; orders stop when `sinθ > 1` (no fourth order for that `λ`).
* **Compton.** `Δλ = (h/m_ec)(1 − cosθ) = 2.426(1 − cosθ) pm`;
  90° → 16.4 keV, 180° → 28 keV at 100 keV; the invariant form
  `m_ec²(1/ε′ − 1/ε) = 1 − cosθ`; the unshifted peak explained by whole-atom recoil.
* **Pair production.** Threshold `2m_ec² = 1.022 MeV`; `2 MeV → 0.98 MeV` shared;
  momentum balance needs a nucleus; the `e⁺`/`e⁻` opposite curvature in a field.
* **Inverse Compton.** `ε′ ≈ 4γ²ε` in the Thomson regime; `γ = 10³`,
  `ε = 6×10⁻⁴ eV` → `2.4 keV`; the `γ²` scaling and its failure when
  `γε ≳ m_ec²`.
* **Correspondence.** `f_ph/f_orb = 1 + 3/2n`; 15 % at `n = 10`, 1.5 % at `n = 100`;
  `n = 100` numbers 6.58 vs 6.68 GHz.
* **Franck–Hertz.** Dips every 4.9 V for mercury; the collector current is the
  derivative-like signature; contact potential shifts the first dip, not the spacing.
* **Nuclear size.** `R = 1.2A^{1/3}` fm: 2.75 fm for C-12, 7.44 fm for U-238;
  `ρ = 3m/4πR³ = 2.3×10¹⁷ kg/m³` for every `A`, which is the point of the `A^{1/3}`;
  the nucleus is ~10⁻¹² of the atom's volume.
* **Binding.** `B = (Zm_H + Nm_n − m_atom)c²`; `1 u = 931.5 MeV`; deuteron 2.224 MeV
  (1.112 MeV per nucleon), He-4 28.30 MeV (7.07), Fe-56 492.3 MeV (8.79), U-238
  1801.7 MeV (7.57); B/A peaks near `A = 56` and not at the heaviest nucleus.
* **Semi-empirical mass formula.** 15.8, 17.8→18.3 volume/surface at `A = 100`–`240`,
  0.71 Coulomb, 23.2 asymmetry, `δ = ±12/√A`; `Z₀ = A/(2 + 0.0154A^{2/3})` gives
  42.9 for `A = 100` and 92.0 for `A = 238`; the same stationary point reappears as
  `a_c/2a_a = 0.0153` on `Olympiad-18`.
* **Alpha decay.** U-238 `Q = 4.27 MeV` from masses, `K_α = (A−4)Q/A = 4.20 MeV`,
  daughter recoil 0.07 MeV; `Q > 0` is necessary but not sufficient (the barrier
  still has to be crossed).
* **Beta decay.** C-14 `Q_β⁻ = 0.156 MeV`; N-13 `Q_β⁺ = 1.20 MeV` with the `2m_e`
  term; the spectrum is continuous because three bodies share the energy; the
  endpoint is where the neutrino takes nothing.
* **Decay law.** `N = N₀e^{−λt}`, `T½ = ln2/λ`, `τ = T½/ln2 = 1.443T½`;
  `λ` is intensive — halving the sample halves both `N` and `A`; C-14 dating
  10 → 15 dpm/g gives 3350 y; the three assumptions (closed system, known `A₀`,
  live exchange) are stated on the sheet.
* **Chains.** Secular `A₂ = A₁` and transient `A₂/A₁ = λ₂/(λ₂−λ₁) = 1.5` for
  18 h/6 h; `t_max = ln(λ₂/λ₁)/(λ₂−λ₁) = 14.3 h`; `N₂` starts at zero, so the
  daughter's own decay makes it peak before the parent is gone.
* **Fission.** `200 MeV` per event → `8.2×10¹⁰ J/g`, `3.1×10¹⁹` fissions per GW·s,
  `1.05 kg/day` at 1 GW thermal and `3.2 kg/day` at 33 % efficiency; U-235 thermal
  fission needs the `n + U-235 → U-236*` step and the 6.5 MeV excitation.
* **Fusion.** D–T `Q = 17.6 MeV`; Coulomb barrier `kZe²/R ≈ 0.72 MeV` classically
  needs `8.4×10⁹ K`; the Gamow peak at `1.5×10⁷ K` sits near `E₀ ≈ 6 keV`, which is
  the Maxwell tail times the tunnelling probability; p–p chain 26.7 MeV per He-4.
* **Geiger–Nuttall.** `log λ = a − bZ/√E`; 0.484 vs 0.334 MeV^(−1/2) over 24 decades;
  `λ₂₁₂/λ₂₃₈ = 4.7×10²³` for a factor 2.1 in alpha energy.
* **Fission barrier.** `B_f ≈ 6 MeV` from the surface–Coulomb difference; U-236
  excitation 6.5 MeV against U-239's 4.8 MeV; fissility 36.0 and 35.6 against the
  `Z²/A ≈ 50` limit at which the barrier vanishes; `Z ≈ 125` from that criterion.
* **Solar neutrinos and lifetime.** `L/26.7 MeV` → 8.9×10³⁷ He/s (1.8×10³⁸ ν/s),
  `6.4×10¹⁴ m⁻²s⁻¹` at 1 AU; `0.1 × 0.7 × 0.007 M☉c² = 8.8×10⁴³ J` → `7.3×10⁹ y`
  at the present luminosity; the drop in `L` after core hydrogen exhaustion is
  stated as the reason the estimate is a ceiling.
* **Counting statistics.** `σ = √N`, 1 % needs 10⁴ counts, four times the time halves
  the error; dead time and background are named as corrections, not modelled.
* **Neutron waves.** `λ = h/√(2mE)`: 25 meV → 1.81 Å; the inverse, `λ = 1 fm` →
  `pc = 1241 MeV`, so `E_k = 616 MeV` (the non-relativistic `h²/2mλ²` says 818 MeV and
  is wrong here). `√(2mE)` is used only where it is valid; the steep energy–wavelength
  trade is the point of the sheet. Bragg geometry reused from `Olympiad-04`.
* **Limits.** `v_phase = c²/v` exceeds `c` while `v_group = v` does not;
  `v_p v_g = c²`; `λ_dB → 0` as `m → ∞`; `Z = 1` reduces every hydrogenic formula to
  hydrogen; `θ → 0` in `Δλ` gives the forward, unshifted photon.

## 4. What was **not** verified

* The exercise sets and the end-of-chapter papers in the four source files were read
  for topic coverage and their answer keys spot-checked where a sheet quotes a number;
  they were **not re-solved end to end**. A wrong distractor or ambiguous stem there
  would not be caught.
* The Cengage chapters the sources cite are not in this repository, so nothing was
  checked against the printed books — only against the files.
* Figures were checked for clipping, overlap and missing glyphs by rendering every
  page and auditing every text object against the canvas; they were not checked
  against the sources' figure lists one by one, and the physics of each curve was
  checked only at the points labelled on it.
* `test_exports.py` recomputes 69 representative values across all four topics. That
  is a smoke test, not a proof of every printed number on all 50 sheets. The nuclear
  block (29 checks) exercises every sheet in Part B at least once, but a wrong digit
  in a number that is not one of those 69 would survive.
* Reactor engineering — delayed neutrons, feedback coefficients, burn-up, decay heat —
  and the shell model are named where they bear on a number and were **not** derived.
  `Z²/A ≈ 50` is quoted as a liquid-drop criterion; the shell corrections that move
  the real limit are outside this edition.
* Relativistic corrections to the Bohr ladder (fine structure) are mentioned once on
  JEE-08 and were not derived anywhere in the set.
