# Modern physics, part A — coverage and classification

Primary sources, all unedited in this repository:

- `../../atomic-structure/Atomic-structure.md` (Part 24)
- `../../photoelectric-effect/Photoelectric-effect.md` (Part 23)
- `../../x-rays/X-rays.md` (Part 25)

`nuclear-physics/Nuclear-physics.md` (Part 26) is the fourth source of this edition
and is **not** covered here yet; it is the second delivery of the same folder and
will extend the page map below rather than replace it. The Cengage chapters these
files cite are the book floor behind them; the printed books are not in this
repository, so nothing is claimed about material that exists only on paper.

## The rule used to split the pages

Part I is everything a JEE Main + Advanced candidate is expected to own: the
Rutherford evidence and its failure point, the Bohr ladder and its de Broglie
justification, the series names, electron-impact excitation, Z² and reduced-mass
scaling, the four quantum numbers, the photon budget, the five photoelectric facts
and their graphs, the photocell, de Broglie waves, Davisson–Germer, and the
minimum-energy estimate behind the size of atoms.

Part II is the same physics pushed further: the continuous and characteristic
X-ray spectrum with thresholds, attenuation and contrast, Bragg reflection, Compton
scattering and its invariant derivation, the inverse-Compton boost, pair production,
Moseley's law as an ordering tool, the classical collapse time, the correspondence
principle, exotic atoms as scaling tests, the Franck–Hertz curve, the waiting-time
paradox, and the two speeds of a matter wave.

The boundary is **relevance and prerequisite**, not difficulty. Nothing in Part II
is claimed to be impossible in a JEE Advanced paper — Compton scattering, Bragg
reflection, Moseley's law and the X-ray cutoff all appear in JEE material. Conversely
no Part I sheet claims to be sufficient for every JEE question: this is a short-note
set, not a question bank.

## Page map

### Part I — JEE Main + Advanced (15 sheets)

| # | Question on the sheet | Core result |
|---|---|---|
| 01 | Why did one alpha in eight thousand come back? | Thomson impulse estimate, `θ ≈ kZe²/KR`, `f = πb²nt`, `b₉₀ ≈ 2.3×10⁻¹⁴ m` |
| 02 | How close can an alpha get before the law breaks? | `tan(θ/2) = r_h/2b`, `r_min = 2kZe²/K`, `K_fail ≈ 32 MeV` for gold |
| 03 | Why is angular momentum n times h-bar? | closure `2πr = nλ` plus Coulomb balance, `r_n = n²ħ²/m_eke²` |
| 04 | What does the hydrogen ladder actually look like? | `r_n ∝ n²`, `E_n = −13.6Z²/n² eV`, 13.6(1/n_f² − 1/n_i²) |
| 05 | Which series is which, and why five names? | series named by the lower level; Hα 656.3, Lyman α 121.6, Balmer edge 364.6 nm |
| 06 | What can a 12.5 eV electron do that a 12.5 eV photon cannot? | partial energy transfer; 10.2 / 12.09 / 12.75 eV thresholds |
| 07 | How far does Z² scaling carry you? | `E ∝ Z²μ`, `r ∝ 1/(Zμ)`; He⁺, Li²⁺, muonic H, positronium |
| 08 | What are the other three numbers for? | n, l, m_l, m_s; selection rules Δl = ±1; `μ_B = 5.79×10⁻⁵ eV/T` |
| 09 | What exactly is in a beam of light? | `n = P/hf` packets per second, each with `p = h/λ`; radiation pressure `(P/c)(1+R)` |
| 10 | Why does brighter light not give faster electrons? | five facts, `K_max = hf − φ`, `eV_s = K_max`, `λ₀ = 1240/φ` |
| 11 | How do you read a photocurrent graph? | cutoff at `−V_s`, plateau ∝ intensity, slope `h/e` for every metal |
| 12 | What does a photocell measure, and what does it not? | battery reads energy per electron, ammeter reads electrons per second |
| 13 | Do electrons have a wavelength? | `λ = h/p`, `λ = 1.226/√V nm`, 100 kV → 3.88 pm non-relativistic |
| 14 | Was the electron wave ever actually seen? | `2d sinθ = nλ`, 54 V → 1.67 Å, NaCl 154/282 pm at 15.8° |
| 15 | Why does the electron not fall into the nucleus? | `E(r) ≈ ħ²/2m_er² − ke²/r`, minimum at `a₀`; `ΔxΔp ≳ ħ/2` |

### Part II — Olympiad / specialised extensions (15 sheets)

| # | Question on the sheet | Core result |
|---|---|---|
| 01 | How does a tube voltage become a shortest wavelength? | `λ_min = hc/eV = 1.24×10⁶/V pm`, independent of the target |
| 02 | When do the sharp lines appear? | `E_Kα = ¾(13.6)(Z−1)² eV`; thresholds Cu 9, Mo 20, W 70 kV |
| 03 | Why does a radiograph show bone and not skin? | `I = I₀e^{−μx}`, `μ ∝ Z³/E³`, half-value layer, lead apron |
| 04 | How do you measure an atom with a wavelength? | Bragg law written from the plane; `N_A = M/2ρd³ ≈ 6.02×10²³` |
| 05 | What happens when a photon hits an electron? | `Δλ = 2.426(1 − cosθ) pm`; 16.4 keV at 90°, 28 keV at 180° for 100 keV |
| 06 | Can the Compton shift be derived without trigonometry? | `m_ec²(1/ε′ − 1/ε) = 1 − cosθ` from one invariant |
| 07 | How does a fast electron brighten a dull photon? | `ε′ ≈ 4γ²ε`; keV photons from microwave seeds |
| 08 | When does a photon stop being a photon? | threshold 1.022 MeV in a nuclear field; 2 MeV → 0.98 MeV shared |
| 09 | How did a straight line predict missing elements? | `√f ∝ (Z − b)`; copper 154 pm → silver 57 pm |
| 10 | How long would a classical atom live? | `τ ≈ 1.6×10⁻¹¹ s` from `a₀`, spiral of ~10⁵ turns |
| 11 | Why does quantum mechanics become classical for large n? | `f_ph/f_orb = 1 + 3/2n`; 15 % at n = 10, 1.5 % at n = 100 |
| 12 | What if the electron weighed 207 times more? | every mass-dependent result takes the reduced mass: 256 fm, −2.81 keV |
| 13 | Can you see energy levels without looking at light? | Franck–Hertz dips every 4.9 V; the collector current is a level diagram |
| 14 | How long should a wave take to eject an electron? | `3×10⁴ s` predicted at 1 mW/m² against ≤ 10⁻⁹ s observed |
| 15 | Which speed does a matter wave travel at? | `v_phase = c²/v` (harmless), `v_group = v` (the particle), `v_p v_g = c²` |

## What is deliberately absent

- Nuclear physics: binding energy, radioactivity, fission and fusion are Part B of
  this edition and are not on these 30 pages.
- Relativistic quantum mechanics, the Dirac equation, and fine structure beyond the
  one-line `α²` correction mentioned on JEE-08.
- Experimental apparatus detail beyond what changes a number on a sheet.
- A question bank. Each sheet is a short note with one worked number, not a
  problem set; the source files carry the exercises and their answers.
