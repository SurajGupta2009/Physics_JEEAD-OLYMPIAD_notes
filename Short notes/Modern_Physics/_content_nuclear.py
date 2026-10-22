"""Part B content: nuclear physics, appended after the X-ray pages.

Ten JEE sheets (16-25) and ten Olympiad sheets (16-25), so the edition reads in
the order of its four sources: atomic structure, the photon, X-rays, nuclei.
Every number here was recomputed from the source's own data; see SOURCE-AUDIT.md.
"""
from layout import Sheet

KJ = 'MODERN PHYSICS  /  PART I: JEE MAIN + ADVANCED'
KO = 'MODERN PHYSICS  /  PART II: OLYMPIAD + EXTENSIONS'


def build_jee(start, total):
    S = []
    n = start

    # =============================================================== NUCLEAR 1
    s = Sheet(f'JEE-{n:02}-nuclear-size', 'Why does every nucleus have the same density?',
              'Add nucleons and the ball grows, but the stuff inside never gets denser. What fixes the size?',
              KJ, n, total, 'source: Nuclear-physics.md  §3.1-3.2, E2, Q1-Q2',
              'R = 1.2 A^1/3 fm is the statement that nuclear matter is incompressible',
              scale=1e6)
    s.move('A saturated force makes a fixed-volume ball', [
        ('p', 'The strong force is attractive at 1–2 fm, gone by about 3 fm, and charge-independent. Because it is short-range, each nucleon binds only its neighbours: doubling A doubles the binding, not the binding per nucleon. Constant energy per nucleon means constant volume per nucleon.'),
        ('m', r'V=Av=\frac{4}{3}\pi R^3\ \Rightarrow\ R=R_0A^{1/3},\quad R_0=1.2\ \mathrm{fm}'),
        ('n', 'the cube root is the whole content: density, not radius, is the invariant'),
    ])
    s.move('Read the density off the constant', [
        ('p', 'Substituting the fitted radius gives a density with no A in it. That is why the answer to "carbon or uranium?" is "neither, they are the same" — a fact worth carrying into any estimate.'),
        ('m', r'\rho=\frac{3m_N}{4\pi R_0^3}=2.3\times10^{17}\ \mathrm{kg/m^3}'),
        ('n', 'a 5 cm³ teaspoon of it weighs 1.2×10¹² kg — a mountain in a spoon'),
    ])
    s.move('What the numbers actually are', [
        ('p', 'Carbon-12 has R = 2.75 fm, uranium-238 has R = 7.44 fm: only 2.7 times bigger for twenty times the nucleons. The nucleus occupies 10⁻¹² of the atom\u2019s volume, yet holds 99.97 % of its mass.'),
        ('m', r'R_{12}=1.2(12)^{1/3}=2.75\ \mathrm{fm},\qquad R_{238}=1.2(238)^{1/3}=7.44\ \mathrm{fm}'),
        ('n', 'the electron cloud is 10⁵ times wider, and almost all of the atom is empty'),
    ])
    s.chip('key', 'size and density', [('m', r'R=1.2A^{1/3}\ \mathrm{fm}'), ('m', r'\rho=2.3\times10^{17}\ \mathrm{kg/m^3}'),
                                      ('p', 'Same for every nucleus.')])
    s.chip('gate', 'where the law is soft', [('p', 'Liquid-drop mean radius. Halo nuclei and the surface fuzz bend it at the few-percent level.'),
                                             ('p', 'It says nothing about shape: deformed nuclei have two radii.')])
    s.chip('trap', 'the two confusions', [('p', 'Saying density falls as A grows (it does not), and taking R ∝ A instead of A^1/3.')])
    s.figure('nuclear_size')
    S.append(s); n += 1

    # =============================================================== NUCLEAR 2
    s = Sheet(f'JEE-{n:02}-binding-curve', 'Where does the missing mass go?',
              'Weigh a nucleus and its parts: the whole is lighter. The difference is what holds it together.',
              KJ, n, total, 'source: §3.3, 4.1-4.2, E1, Q3',
              'B = Δm c², 1 u = 931.5 MeV, and B/A peaks at iron near 8.8 MeV',
              scale=1e8)
    s.move('Weigh the parts, weigh the whole', [
        ('p', 'Take Z protons and N neutrons apart, then assemble them. The assembly is lighter by Δm, and that mass went out as the energy that bound it. Conversely, Δm c² is the energy you must pay to take it apart again.'),
        ('m', r'B=\left[Zm_H+Nm_n-M_{\mathrm{atom}}\right]c^2,\qquad 1\ \mathrm{u}=931.5\ \mathrm{MeV}'),
        ('n', 'atomic masses are used throughout: the electron bookkeeping cancels for the nucleus'),
    ])
    s.move('Two numbers set the scale', [
        ('p', 'The deuteron is barely bound: 2.22 MeV for two nucleons, 1.11 each. Helium-4 is the first tight package: 28.3 MeV, 7.07 per nucleon — a factor 6.4 jump that explains why fusing past hydrogen pays so much.'),
        ('m', r'\Delta m_d=0.002388\ \mathrm{u}\Rightarrow B=2.22\ \mathrm{MeV},\qquad B/A=1.11'),
        ('m', r'\Delta m_{He}=0.030377\ \mathrm{u}\Rightarrow B=28.3\ \mathrm{MeV},\qquad B/A=7.07'),
    ])
    s.move('The curve is the decision-maker', [
        ('p', 'Plot B/A against A and every energy question becomes "which way does this move the nucleons?". Fusion climbs the left slope toward iron; fission climbs the right slope toward the same summit. Anything that moves nucleons up the curve releases the difference.'),
        ('m', r'\mathrm{fission:}\ 7.6\to8.5\ \mathrm{MeV/nucleon}\ \Rightarrow\ \sim200\ \mathrm{MeV}'),
        ('n', 'iron has nothing to gain — hence the endpoint of stellar burning'),
    ])
    s.chip('key', 'the two lines', [('m', r'B=\Delta m\,c^2'), ('m', r'1\ \mathrm{u}=931.5\ \mathrm{MeV}'),
                                    ('p', 'B/A: 1.1 (d) → 7.1 (He) → 8.8 (Fe) → 7.6 (U).')])
    s.chip('insight', 'why the peak', [('p', 'Short-range attraction grows as A, Coulomb repulsion as Z². Below iron the surface tax dominates; above it the Coulomb tax does.')])
    s.chip('trap', 'the sign', [('p', 'Using bare proton masses instead of hydrogen atoms in a beta problem, or calling the mass defect a loss of nucleons.')])
    s.figure('binding_curve')
    S.append(s); n += 1

    # =============================================================== NUCLEAR 3
    s = Sheet(f'JEE-{n:02}-valley', 'Why does the valley of stability bend?',
              'Light nuclei want equal protons and neutrons. Heavy ones want extra neutrons. The liquid drop says why.',
              KJ, n, total, 'source: §3.4, 4.6, E12, Q26',
              'Coulomb grows as Z², surface as A^2/3, so Z0 = A/(2 + 0.0154 A^2/3)',
              scale=1e8)
    s.move('Five terms, five physical reasons', [
        ('p', 'Volume buys binding for every nucleon; surface taxes the ones at the edge; Coulomb punishes every proton pair; asymmetry punishes N ≠ Z because the two Fermi seas must be filled to the same height; pairing rewards even numbers.'),
        ('m', r'B=a_vA-a_sA^{2/3}-a_c\frac{Z^2}{A^{1/3}}-a_a\frac{(N-Z)^2}{A}+\delta'),
        ('n', 'typical coefficients 15.8, 18.3, 0.71, 23.2, 12 MeV'),
    ])
    s.move('Maximise over Z at fixed A', [
        ('p', 'Only the Coulomb and asymmetry terms care about Z once A is fixed. Setting the derivative to zero gives the valley floor: the most stable Z for that mass number.'),
        ('m', r'Z_0=\frac{A}{2+\frac{a_c}{2a_a}A^{2/3}}=\frac{A}{2+0.0154A^{2/3}}'),
        ('n', 'A = 100 gives 42.9; A = 238 gives 92.0 — uranium sits on its own floor'),
    ])
    s.move('Off the floor, beta decay is the traffic', [
        ('p', 'A nucleus with too many neutrons converts one into a proton; too few, the reverse. The valley is the map and beta decay is the traffic that moves every nucleus toward the floor.'),
        ('m', r'\beta^-:\ n\to p+e^-+\bar\nu_e\qquad \beta^+:\ p\to n+e^++\nu_e'),
        ('n', 'A never changes in beta decay; only Z does'),
    ])
    s.chip('key', 'the floor', [('m', r'Z_0=\frac{A}{2+0.0154A^{2/3}}'),
                                ('p', 'Light nuclei: N ≈ Z. Heavy: N/Z ≈ 1.5.')])
    s.chip('gate', 'liquid drop only', [('p', 'Shell closures dent and bump the floor — the model is the trend, not the detail.'),
                                        ('p', 'Beyond bismuth no configuration is fully stable.')])
    s.chip('trap', 'which way', [('p', 'Neutron-rich nuclei go β⁻ (Z up). Proton-rich go β⁺ or EC (Z down). Getting this backwards is the most common slip.')])
    s.figure('stability_valley')
    S.append(s); n += 1

    # =============================================================== NUCLEAR 4
    s = Sheet(f'JEE-{n:02}-q-value', 'Why does the alpha carry almost all the energy?',
              'Two bodies leave a decay at rest. Momentum must cancel, so the light one takes the lion\u2019s share.',
              KJ, n, total, 'source: §3.5-3.6, 4.3, E3, Q4-Q5',
              'Q from masses, then K_alpha = (A-4)Q/A — momentum fixes the split',
              scale=1e6)
    s.move('Q is one subtraction', [
        ('p', 'For any decay, Q = (mass in − mass out)c². Positive Q means it can happen; it says nothing about how fast. With atomic masses the electrons cancel, so the arithmetic is one line.'),
        ('m', r'Q=(M_{\mathrm{parent}}-M_{\mathrm{daughter}}-M_\alpha)c^2'),
        ('n', 'alpha decay of U-238: Q = 4.27 MeV, which is why it can happen at all'),
    ])
    s.move('Momentum splits Q inversely to mass', [
        ('p', 'The parent was at rest, so the two products leave back to back with equal momentum. Kinetic energy goes as p²/2m, so the lighter body takes the larger share — the same rule as a recoiling gun.'),
        ('m', r'K_\alpha=\frac{A-4}{A}Q,\qquad K_{\mathrm{daughter}}=\frac{4}{A}Q'),
        ('n', 'U-238: 4.20 MeV to the alpha, 0.07 MeV to the recoiling thorium'),
    ])
    s.move('Discrete energies, because levels are discrete', [
        ('p', 'The alpha can leave the daughter in its ground state or in an excited one; each branch has its own Q, so the alpha spectrum is a set of sharp lines, not a continuum. Any leftover excitation leaves later as a gamma.'),
        ('m', r'Q_{\mathrm{branch}}=Q_0-E_{\mathrm{ex}},\qquad E_\gamma=E_{\mathrm{ex}}'),
        ('n', 'this is the nuclear analogue of an atomic line spectrum'),
    ])
    s.chip('key', 'the split', [('m', r'Q=(m_{\mathrm{in}}-m_{\mathrm{out}})c^2'), ('m', r'K_\alpha=\frac{A-4}{A}Q'),
                                ('p', 'Lighter product takes the larger share.')])
    s.chip('gate', 'two bodies only', [('p', 'The formula assumes the parent was at rest and only two products leave.'),
                                       ('p', 'Beta decay is three bodies — hence its continuous spectrum.')])
    s.chip('trap', 'what Q is not', [('p', 'Q is not the alpha kinetic energy (multiply by (A−4)/A), and a positive Q does not mean an instant decay.')])
    s.figure('alpha_split')
    S.append(s); n += 1

    # =============================================================== NUCLEAR 5
    s = Sheet(f'JEE-{n:02}-beta', 'How can a beta spectrum be continuous?',
              'Alpha lines are sharp. Beta electrons arrive with every energy from zero to an endpoint. Something is missing.',
              KJ, n, total, 'source: §3.7, 3.8, E4-E5',
              'a third particle carries the rest; the endpoint is where it carries nothing',
              scale=1e6)
    s.move('Three bodies, not two', [
        ('p', 'In beta decay the nucleus emits an electron and an antineutrino. With three bodies leaving, the energy can be shared in a continuum of ways: every electron energy from zero up to the endpoint Q is allowed, and the neutrino takes the remainder.'),
        ('m', r'n\to p+e^-+\bar\nu_e\qquad p\to n+e^++\nu_e'),
        ('n', 'the endpoint E₀ = Q is where the neutrino gets nothing'),
    ])
    s.move('The electron rule, in one line each', [
        ('p', 'Atomic masses include the electrons, and that changes the bookkeeping between the two beta signs. For β⁻ the daughter has one more electron, which the atomic mass already counts. For β⁺ the positron is an extra particle and the atom has one electron too few.'),
        ('m', r'Q_{\beta^-}=(M_P-M_D)c^2,\qquad Q_{\beta^+}=(M_P-M_D-2m_e)c^2'),
        ('n', 'C-14: 0.156 MeV. N-13: 2.220 − 1.022 = 1.20 MeV'),
    ])
    s.move('Gamma and conversion finish the job', [
        ('p', 'The daughter often stays excited. It can emit a photon of the level gap (gamma), or hand the same energy to an orbital electron (internal conversion), which then leaves with the gap minus its binding. Both carry the same information: the nuclear level diagram.'),
        ('m', r'E_\gamma=E_{\mathrm{ex}},\qquad K_e=E_{\mathrm{ex}}-B_{\mathrm{shell}}'),
        ('n', 'long-lived excited states are isomers; they decay later with the same energy'),
    ])
    s.chip('key', 'the two rules', [('m', r'Q_{\beta^-}=(M_P-M_D)c^2'), ('m', r'Q_{\beta^+}=(M_P-M_D-2m_e)c^2'),
                                    ('p', 'A is unchanged in both.')])
    s.chip('gate', 'spectrum shape', [('p', 'The endpoint is exact; the shape near zero depends on the Coulomb pull on the emitted electron.'),
                                      ('p', 'Neutrino mass is ~1 eV, invisible at MeV resolution.')])
    s.chip('trap', 'the classic trio', [('p', 'Giving the electron all of Q. Changing A by one. Forgetting the 2m_e for β⁺.')])
    s.figure('beta_spectrum')
    S.append(s); n += 1

    # =============================================================== NUCLEAR 6
    s = Sheet(f'JEE-{n:02}-decay-law', 'What does a half-life actually measure?',
              'Each nucleus has a fixed chance per second of dying. From that one assumption the whole calculus follows.',
              KJ, n, total, 'source: §3.9, 4.4, E8, Q9-Q11',
              'N = N₀e^{−λt}, T½ = ln2/λ, τ = 1.443 T½ — and λ is intensive',
              scale=1e6)
    s.move('A memoryless probability gives an exponential', [
        ('p', 'Assume every nucleus has the same chance λ dt of decaying in the next dt, however long it has already lived. Then dN = −λN dt integrates to an exponential, and the same λ governs the activity, because activity is λ times the number present.'),
        ('m', r'N=N_0e^{-\lambda t},\qquad A_{\mathrm{ct}}=\lambda N,\qquad T_{1/2}=\frac{\ln2}{\lambda}'),
        ('n', 'the log plot is a straight line of slope −λ; that is how half-lives are measured'),
    ])
    s.move('Mean life is not half-life', [
        ('p', 'The average lifetime is the integral of t over the decay distribution, and it comes out 1/λ — larger than the half-life by 1/ln2. The nucleus that survives longest is not the typical one.'),
        ('m', r'\tau=\frac{1}{N_0}\int_0^\infty t\,(-dN)=\frac{1}{\lambda}=1.443\,T_{1/2}'),
        ('n', 'C-14: T½ 5730 y, τ 8270 y; Ra-226: 1600 y and 2310 y'),
    ])
    s.move('Three things λ is not', [
        ('p', 'λ does not depend on how many nuclei you have, on temperature, or on chemistry — with one exception: electron capture needs a bound electron, so extreme ionisation can shift it.'),
        ('m', r'\lambda=\lambda_1+\lambda_2+\dots,\qquad f_i=\frac{\lambda_i}{\lambda}'),
        ('n', 'two decay modes add their constants; the branching fraction is the ratio'),
    ])
    s.chip('key', 'the three', [('m', r'N=N_0e^{-\lambda t}'), ('m', r'A_{\mathrm{ct}}=\lambda N'),
                                ('m', r'\tau=1/\lambda=1.443T_{1/2}')])
    s.chip('insight', 'why λ is stable', [('p', 'Nuclear decay is a tunnelling or weak process at the MeV scale; room temperature is 25 meV. The ratio is 4×10⁷, so nothing ordinary can move it. Halving the sample halves A but leaves λ untouched.')])
    s.chip('trap', 'the missing ln 2', [('p', 'Writing e^{−t/T½} for e^{−λt}: at one half-life that gives 37 %, not 50 %. The exponent must carry ln 2.')])
    s.figure('decay_curve')
    S.append(s); n += 1

    # =============================================================== NUCLEAR 7
    s = Sheet(f'JEE-{n:02}-dating', 'How do you date a bone?',
              'A living thing keeps its radiocarbon topped up. When it dies the clock starts, and the ratio is the hand.',
              KJ, n, total, 'source: §3.11, E7, Q12',
              't = (T½/ln2) ln(A₀/A): three assumptions, one logarithm',
              scale=1e6)
    s.move('The clock is an exchange that stops', [
        ('p', 'Cosmic rays keep the atmospheric ¹⁴C/¹²C ratio roughly fixed. Living tissue exchanges carbon, so it matches the atmosphere; death stops the exchange and the ¹⁴C already inside decays away.'),
        ('m', r'\frac{A}{A_0}=e^{-\lambda t}\ \Rightarrow\ t=\frac{T_{1/2}}{\ln2}\ln\frac{A_0}{A}'),
        ('n', '10 disintegrations per minute per gram against 15 gives 3350 years'),
    ])
    s.move('The range is set by counting, not by physics', [
        ('p', 'After ten half-lives one nucleus in a thousand is left, and counting statistics dominate. That is why the ceiling is about 50 000 years, and why rocks need longer-lived clocks.'),
        ('m', r't_{10}=10(5730)=5.7\times10^4\ \mathrm{y},\qquad \frac{\sigma}{N}=\frac{1}{\sqrt{N}}'),
        ('n', 'K–Ar: 1.25 Gyr; U–Pb: 4.47 Gyr — same logarithm, different constant'),
    ])
    s.move('The assumptions you must state', [
        ('p', 'Constant production, a closed sample, and a known initial ratio. The last is the weak link, so tree rings calibrate the raw ratio; the isochron method removes it by plotting one ratio against another.'),
        ('m', r'\frac{^{87}\mathrm{Sr}}{^{86}\mathrm{Sr}}=\left(\frac{^{87}\mathrm{Sr}}{^{86}\mathrm{Sr}}\right)_0+\frac{^{87}\mathrm{Rb}}{^{86}\mathrm{Sr}}\left(e^{\lambda t}-1\right)'),
        ('n', 'a straight line whose slope is the age — the intercept absorbs the unknown start'),
    ])
    s.chip('key', 'the clock', [('m', r't=\frac{T_{1/2}}{\ln2}\ln\frac{A_0}{A}'), ('p', 'C-14: 5730 y, range to ~50 ka.'),
                                ('p', 'K–Ar, U–Pb for rock.')])
    s.chip('gate', 'when it fails', [('p', 'Open samples, contamination, fossil fuel (dead carbon), and dates near the limit where the count is a handful.')])
    s.chip('trap', 'the ratio inverted', [('p', 'Using A/A₀ instead of A₀/A flips the sign of the age. Check that a smaller activity gives a positive age.')])
    s.figure('dating_curve')
    S.append(s); n += 1

    # =============================================================== NUCLEAR 8
    s = Sheet(f'JEE-{n:02}-chains', 'Why does a decay chain settle into a fixed ratio?',
              'A daughter fed by its parent has two clocks. When one is much slower, the other just follows.',
              KJ, n, total, 'source: §3.10, 4.5, Q14-Q15, Q18',
              'secular: A₂ = A₁; transient: A₂/A₁ = λ₂/(λ₂−λ₁)',
              scale=1e6)
    s.move('Two clocks in one equation', [
        ('p', 'The daughter is produced at rate λ₁N₁ and destroyed at rate λ₂N₂. Solving the pair with a daughter that starts at zero gives a rise-and-fall: the daughter activity climbs, peaks, then locks onto the parent\u2019s decay.'),
        ('m', r'\frac{dN_2}{dt}=\lambda_1N_1-\lambda_2N_2\ \Rightarrow\ A_2=\frac{\lambda_2}{\lambda_2-\lambda_1}A_1\left(1-e^{-(\lambda_2-\lambda_1)t}\right)'),
        ('n', 'the bracket is the approach to equilibrium; after a few daughter half-lives it is one'),
    ])
    s.move('Name the regime before doing arithmetic', [
        ('p', 'If the parent is far longer-lived, the ratio settles at one: secular equilibrium, the state of old radium samples. If it is only somewhat longer-lived, the ratio settles at a number above one: transient equilibrium, and the chain decays with the parent\u2019s clock.'),
        ('m', r'\mathrm{secular}:\ \frac{A_2}{A_1}\to1,\qquad \mathrm{transient}:\ \frac{A_2}{A_1}\to\frac{\lambda_2}{\lambda_2-\lambda_1}'),
        ('n', 'λ₂ = 3λ₁ gives a ratio of 3/2; the daughter is always the more active one'),
    ])
    s.move('Peak time and branching', [
        ('p', 'The daughter activity peaks where its derivative vanishes; after that it inherits the parent\u2019s slope. If a nuclide has two decay modes, the constants add and each branch takes its share of the decays.'),
        ('m', r't_{\max}=\frac{\ln(\lambda_2/\lambda_1)}{\lambda_2-\lambda_1},\qquad \lambda=\lambda_a+\lambda_b,\quad f_a=\frac{\lambda_a}{\lambda}'),
        ('n', 'the long-term tempo always belongs to the longest-lived member present'),
    ])
    s.chip('key', 'the regimes', [('p', 'Secular: parent ≫ daughter, ratio 1.'), ('p', 'Transient: ratio λ₂/(λ₂−λ₁).'),
                                  ('p', 'No equilibrium if the parent is the shorter one.')])
    s.chip('gate', 'what the formulas assume', [('p', 'Closed system, no daughter at t = 0, and a single decay path for each nuclide.')])
    s.chip('trap', 'which is parent', [('p', 'Comparing half-lives backwards. The longer-lived isotope is the one that sets the chain\u2019s pace.')])
    s.figure('equilibrium')
    S.append(s); n += 1

    # =============================================================== NUCLEAR 9
    s = Sheet(f'JEE-{n:02}-fission', 'Where does a gigawatt come from?',
              'One fission releases 200 MeV. Multiply by the fission rate and a gram of uranium outruns a tonne of coal.',
              KJ, n, total, 'source: §3.12, E10-E11, Q16-Q17',
              '200 MeV per fission: 8.2×10¹⁰ J per gram, 3.1×10¹⁹ fissions per second per GW',
              scale=1e8)
    s.move('The energy budget of one split', [
        ('p', 'A thermal neutron leaves U-236 excited above its fission barrier; the drop necks and Coulomb wins. The fragments fly apart with most of the energy; the rest arrives later as neutrons, betas and gammas.'),
        ('m', r'^{235}\mathrm{U}+n\to{}^{236}\mathrm{U}^*\to X+Y+2n+200\ \mathrm{MeV}'),
        ('n', '≈165 MeV fragments, 5 MeV neutrons, 20 MeV betas and gammas (delayed), 10 MeV neutrinos lost'),
    ])
    s.move('Convert to engineering units', [
        ('p', 'Divide 200 MeV into a gram of U-235: 8.2×10¹⁰ J, about 3.4 tonnes of coal. A gigawatt thermal plant therefore burns about a kilogram a day.'),
        ('m', r'\frac{10^9}{200\times1.602\times10^{-13}}=3.1\times10^{19}\ \mathrm{s^{-1}},\qquad \frac{8.6\times10^{13}}{8.2\times10^{10}}=1.05\ \mathrm{kg/day}'),
        ('n', 'the reactor\u2019s daily meal fits in a pocket; the waste does not'),
    ])
    s.move('The chain needs a multiplication factor', [
        ('p', 'k compares neutrons in one generation with the last. Below one the fire dies, at one it is steady, above one it rises. A reactor is designed to sit at k = 1 with delayed neutrons giving the control loop time to act; a bomb is prompt-critical by construction.'),
        ('m', r'k<1\ \mathrm{subcritical},\qquad k=1\ \mathrm{steady},\qquad k>1\ \mathrm{rising}'),
        ('n', 'moderator slows, control rods absorb, coolant carries heat, shielding guards the outside'),
    ])
    s.chip('key', 'the arithmetic', [('p', '200 MeV per fission.'), ('p', '8.2×10¹⁰ J per gram of U-235.'),
                                     ('p', '3.1×10¹⁹ fissions per second per GW thermal.')])
    s.chip('gate', 'k and the reactor', [('p', 'A power reactor cannot detonate like a weapon: dilute fuel, delayed neutrons, negative feedbacks.'),
                                         ('p', 'That is not a claim that accidents are impossible.')])
    s.chip('trap', 'the two units', [('p', 'Confusing thermal and electrical power (factor ≈3), and quoting 200 MeV per *nucleus* as if all the fuel fissioned.')])
    s.figure('fission_energy')
    S.append(s); n += 1

    # =============================================================== NUCLEAR 10
    s = Sheet(f'JEE-{n:02}-fusion', 'Why is the Sun not ten billion kelvin?',
              'Protons repel hard. Classical physics demands an impossible temperature; the Sun runs on the tail of a distribution.',
              KJ, n, total, 'source: §3.13, OL2, OL11, Q21-Q25',
              'the Coulomb barrier needs 8×10⁹ K classically; tunnelling plus the Maxwell tail makes 1.5×10⁷ K enough',
              scale=1e6)
    s.move('The barrier is real and it is large', [
        ('p', 'Two protons at 2 fm sit on a Coulomb hill of 0.72 MeV. Setting k_BT equal to it gives 8×10⁹ K — the classical answer, five hundred times the core.'),
        ('m', r'U=\frac{ke^2}{2\ \mathrm{fm}}=0.72\ \mathrm{MeV}\ \Rightarrow\ T=\frac{U}{k_B}\approx8\times10^9\ \mathrm{K}'),
        ('n', 'that is the roll-over temperature, not the operating temperature'),
    ])
    s.move('Tunnelling and the Maxwell tail meet in the middle', [
        ('p', 'The reaction rate is the product of how many particles have energy E (a falling exponential) and how likely they are to tunnel through the barrier (a rising one). The product peaks at the Gamow energy, far above k_BT and far below the barrier.'),
        ('m', r'E_0=\left(\frac{E_G(k_BT)^2}{4}\right)^{1/3}\approx6\ \mathrm{keV}\ \ \mathrm{at}\ 15\ \mathrm{MK}'),
        ('n', 'the Sun burns at 1.5×10⁷ K because its particles tunnel, not because they climb'),
    ])
    s.move('The chain, and what it pays', [
        ('p', 'The p–p chain fuses four protons in three steps; the first is weak and slow, and it sets the Sun\u2019s clock. The 26.7 MeV appears as light and neutrinos.'),
        ('m', r'4p\to{}^4\mathrm{He}+2e^++2\nu+26.7\ \mathrm{MeV},\qquad \dot m=\frac{L}{c^2}=4.3\times10^9\ \mathrm{kg/s}'),
        ('n', 'only 0.7 % of the fused mass becomes energy — and that is still 4 million tonnes a second'),
    ])
    s.chip('key', 'the three numbers', [('p', 'Barrier 0.72 MeV at 2 fm.'), ('p', 'Core 1.5×10⁷ K, Gamow peak ~6 keV.'),
                                        ('p', '26.7 MeV per helium; 4.3×10⁹ kg/s lost.')])
    s.chip('gate', 'when the chain applies', [('p', 'p–p dominates cool stars; the CNO cycle takes over above ~1.7×10⁷ K with carbon as catalyst.'),
                                              ('p', 'Both give the same net energy.')])
    s.chip('trap', 'the one-step Sun', [('p', 'Four protons do not collide at once. Treating the chain as a single reaction loses the weak first step that sets the lifetime.')])
    s.figure('fusion_barrier')
    S.append(s)

    return S


def build_oly(start, total):
    S = []
    n = start

    # =============================================================== OLY NUCLEAR 1
    s = Sheet(f'Olympiad-{n:02}-geiger-nuttall', 'Why does a factor of two in energy swing a half-life by 10²⁴?',
              'Alpha decay spans thirty orders of magnitude in lifetime, yet the energies differ by a factor of two.',
              KO, n, total, 'source: OL1, §3.6',
              'log T is linear in 1/√E: the tunnelling exponent is the amplifier',
              scale=1e6)
    s.move('A barrier the alpha cannot climb', [
        ('p', 'An alpha inside a heavy nucleus faces a Coulomb hill tens of MeV high while carrying only 4–9 MeV: classically it never leaves. It tunnels, with an exponent set by barrier width and height.'),
        ('m', r'\log_{10}\lambda\approx a-\frac{bZ}{\sqrt{E}}'),
        ('n', 'E in MeV, and the second term is of order 40 — an exponent, not a correction'),
    ])
    s.move('Two nuclides show the amplifier', [
        ('p', 'U-238 emits 4.27 MeV alphas and lives 4.5×10⁹ years; Po-212 emits 8.95 MeV alphas and lives 0.3 µs. The argument 1/√E changes by 30 %, and the lifetime changes by twenty-four decades.'),
        ('m', r'\frac{1}{\sqrt{4.27}}=0.484,\qquad \frac{1}{\sqrt{8.95}}=0.334\ \mathrm{MeV^{-1/2}}'),
        ('n', 'a 30 % change in the argument, a 10²⁴ change in the answer: exponential amplification'),
    ])
    s.move('The straight line, and what it is good for', [
        ('p', 'For isotopes of one element, log T against 1/√E is the Geiger–Nuttall line. Its slope grows with Z, so an unknown alpha energy lands on one element\u2019s line and not another\u2019s.'),
        ('m', r'\log_{10}T_{1/2}=A+\frac{BZ}{\sqrt{E}}'),
        ('n', 'Gamow explained in 1928 what Geiger and Nuttall had measured in 1911'),
    ])
    s.chip('key', 'the law', [('m', r'\log\lambda=a-bZ/\sqrt{E}'), ('p', 'Same-Z isotopes: one straight line.'),
                              ('p', 'Slope ∝ Z.')])
    s.chip('gate', 'what it ignores', [('p', 'Prefactors from nuclear structure, angular momentum hindrance, and deformation.'),
                                       ('p', 'It is a systematics law, not a rate calculation.')])
    s.chip('trap', 'the axis', [('p', 'Plotting log T against E rather than 1/√E destroys the line — and the physics is in that choice of axis.')])
    s.figure('geiger_nuttall')
    S.append(s); n += 1

    # =============================================================== OLY NUCLEAR 2
    s = Sheet(f'Olympiad-{n:02}-fission-barrier', 'Why does U-235 fission with slow neutrons and U-238 not?',
              'Same element, one neutron apart, completely different behaviour. The answer is a pairing bonus of 0.8 MeV.',
              KO, n, total, 'source: OL3, §3.4, Q27',
              'the barrier is ~6 MeV for both; pairing decides who clears it',
              scale=1e8)
    s.move('Deforming the drop costs surface and saves Coulomb', [
        ('p', 'Stretch the drop and its surface area grows (a cost) while the protons move apart (a gain). The barrier is the hump between: the drop must be pushed over it before Coulomb can run away.'),
        ('m', r'B_f\approx4\pi R^2\gamma\left(1-\frac{Z^2}{2A}\right)'),
        ('n', 'the barrier falls as the fissility Z²/A grows; it vanishes near Z²/A ≈ 50'),
    ])
    s.move('Fissility is 36.0 for U-235 and 35.6 for U-238', [
        ('p', 'Both sit far below the limit, so neither fissions on its own. What decides is the excitation energy supplied by the captured neutron, compared with the barrier height.'),
        ('m', r'\frac{Z^2}{A}=\frac{92^2}{235}=36.0,\qquad \frac{92^2}{238}=35.6'),
        ('n', 'the difference is small; the pairing term is what actually flips the outcome'),
    ])
    s.move('One pairing term, two destinies', [
        ('p', 'Adding a neutron to U-235 makes even–even U-236, which collects a pairing bonus of about 12/√236 ≈ 0.8 MeV on top of the neutron\u2019s binding. U-238 plus a neutron makes odd–even U-239 with no bonus, so only a fast neutron\u2019s kinetic energy closes the gap.'),
        ('m', r'E^*_{236}\approx6.5\ \mathrm{MeV}>B_f,\qquad E^*_{239}\approx4.8\ \mathrm{MeV}<B_f'),
        ('n', 'thermal neutrons for U-235, fast neutrons for U-238 — one line of liquid-drop arithmetic'),
    ])
    s.chip('key', 'the numbers', [('p', 'Barrier ≈ 6 MeV for both.'), ('p', 'Excitation 6.5 vs 4.8 MeV.'),
                                  ('p', 'Fissility 36.0 vs 35.6.')])
    s.chip('insight', 'why even–even pays', [('p', 'Nucleons pair with opposite spins; an unpaired nucleon costs energy. Even–even nuclei are the tightly bound ones.')])
    s.chip('trap', 'the fissility shortcut', [('p', 'Using Z²/A alone to predict which isotope fissions. It sets the barrier\u2019s trend, not the outcome for one neutron.')])
    s.figure('fission_barrier')
    S.append(s); n += 1

    # =============================================================== OLY NUCLEAR 3
    s = Sheet(f'Olympiad-{n:02}-valley-floor', 'Can you derive the valley rather than remember it?',
              'Maximise the liquid-drop binding over charge at fixed mass. One derivative gives the stability line.',
              KO, n, total, 'source: OL4, §3.4',
              'differentiate B(A,Z): Z₀ = A/(2 + (a_c/2a_a)A^{2/3})',
              scale=1e8)
    s.move('Only two terms care about Z', [
        ('p', 'At fixed A the volume and surface terms are constants, and pairing is a small step. The competition is between the Coulomb term (grows as Z²) and the asymmetry term (grows as (A−2Z)²).'),
        ('m', r'\frac{\partial B}{\partial Z}=-2a_c\frac{Z}{A^{1/3}}-2a_a\frac{2(A-2Z)}{A}=0'),
        ('n', 'the asymmetry term is written so that N − Z = A − 2Z'),
    ])
    s.move('Solve it', [
        ('p', 'Rearranging gives the floor explicitly. Small A returns Z = A/2; large A pushes the floor toward neutron-rich nuclei because the Coulomb tax grows faster than the asymmetry tax.'),
        ('m', r'Z_0=\frac{4a_aA}{8a_a+a_cA^{2/3}}=\frac{A}{2+\frac{a_c}{2a_a}A^{2/3}}'),
        ('n', 'a_c/2a_a = 0.71/46.4 = 0.0153, the 0.0154 of the formula sheets'),
    ])
    s.move('Test it where the data are', [
        ('p', 'At A = 100 the formula gives 42.9; the stable isobars are Mo and Ru, Z = 42–44. At A = 238 it gives 92.0 and uranium is at 92. The formula is a mean trend: shell closures dent it, which is why the real chart has kinks.'),
        ('m', r'Z_0(100)=42.9,\qquad Z_0(238)=92.0'),
        ('n', 'the liquid drop is the climate; the shells are the weather'),
    ])
    s.chip('key', 'the derivative', [('m', r'Z_0=\frac{A}{2+0.0154A^{2/3}}'), ('p', 'N = Z at small A.'),
                                     ('p', 'N/Z → 1.5 at A = 238.')])
    s.chip('gate', 'what is dropped', [('p', 'Pairing\u2019s derivative is ignored and shell effects are absent, so the formula misses magic-number nuclei by several units of Z.')])
    s.chip('trap', 'differentiating A', [('p', 'Treating A as a variable. The valley is defined at fixed A — that is the whole point of an isobar.')])
    s.figure('valley_floor')
    S.append(s); n += 1

    # =============================================================== OLY NUCLEAR 4
    s = Sheet(f'Olympiad-{n:02}-transient', 'How long does a daughter take to peak?',
              'Solve the two-step chain properly, then read the equilibrium and the peak time off the solution.',
              KO, n, total, 'source: OL5, §3.10',
              'A₂ peaks at ln(λ₂/λ₁)/(λ₂−λ₁), then follows the parent',
              scale=1e6)
    s.move('Solve the pair with an empty daughter', [
        ('p', 'Substitute the parent\u2019s exponential into the daughter\u2019s equation and integrate with N₂(0) = 0. The result is a difference of two exponentials: the daughter\u2019s own decay minus the parent\u2019s supply.'),
        ('m', r'N_2(t)=\frac{\lambda_1N_1(0)}{\lambda_2-\lambda_1}\left(e^{-\lambda_1t}-e^{-\lambda_2t}\right)'),
        ('n', 'when λ₂ > λ₁ the second exponential dies first and the parent survives'),
    ])
    s.move('Late times leave one exponential', [
        ('p', 'After the daughter\u2019s own transient has died away, the bracket approaches e^{−λ₁t} and the ratio of activities becomes a constant. That constant is the equilibrium, and it is 1 in the secular limit.'),
        ('m', r'\frac{A_2}{A_1}\to\frac{\lambda_2}{\lambda_2-\lambda_1}\ \to\ 1\ \ \mathrm{as}\ \lambda_1\ll\lambda_2'),
        ('n', 'transient ratio 1.5 when λ₂ = 3λ₁; secular ratio 1 when the parent is very long-lived'),
    ])
    s.move('Differentiate again for the peak', [
        ('p', 'Setting the derivative of N₂ to zero gives the time of maximum daughter activity. It is the crossing of the two exponentials — the moment the daughter\u2019s production and decay balance at their largest.'),
        ('m', r't_{\max}=\frac{\ln(\lambda_2/\lambda_1)}{\lambda_2-\lambda_1}'),
        ('n', 'the peak matters for a generator: elute the daughter at the maximum, not later'),
    ])
    s.chip('key', 'the three results', [('m', r'N_2(t)\propto e^{-\lambda_1t}-e^{-\lambda_2t}'),
                                        ('m', r'A_2/A_1=\lambda_2/(\lambda_2-\lambda_1)'),
                                        ('m', r't_{\max}=\ln(\lambda_2/\lambda_1)/(\lambda_2-\lambda_1)')])
    s.chip('gate', 'limits behave', [('p', 't → 0: N₂ → 0 with zero slope.'), ('p', 'λ₁ → 0: ratio → 1, secular.'), ('p', 'Dimensions: t_max is a time.')])
    s.chip('trap', 'which exponential', [('p', 'Subtracting the parent from the daughter (sign flip) gives a negative activity. The daughter term always decays faster.')])
    s.figure('transient_peak')
    S.append(s); n += 1

    # =============================================================== OLY NUCLEAR 5
    s = Sheet(f'Olympiad-{n:02}-solar-neutrinos', 'How many solar neutrinos cross your thumbnail each second?',
              'The Sun\u2019s luminosity fixes its fusion rate, and the fusion rate fixes the neutrino flux at Earth.',
              KO, n, total, 'source: OL6, §3.13',
              'L/26.7 MeV gives 1.8×10³⁸ neutrinos per second; 6×10¹⁴ m⁻²s⁻¹ at Earth',
              scale=1e6)
    s.move('Luminosity counts helium nuclei', [
        ('p', 'Every 26.7 MeV released corresponds to one helium nucleus made and two neutrinos emitted. Dividing the luminosity by that energy gives the helium rate directly, with no model of the core needed.'),
        ('m', r'\dot N_{\mathrm{He}}=\frac{3.83\times10^{26}}{26.7\times1.602\times10^{-13}}=8.9\times10^{37}\ \mathrm{s^{-1}}'),
        ('n', 'twice that many neutrinos: the chain emits two per helium'),
    ])
    s.move('Spread them over a sphere', [
        ('p', 'At Earth the flux is that rate divided by 4π times the astronomical unit squared. The number is enormous, and it is the number every solar-neutrino experiment had to explain.'),
        ('m', r'\phi_\nu=\frac{1.8\times10^{38}}{4\pi(1.496\times10^{11})^2}=6.4\times10^{14}\ \mathrm{m^{-2}s^{-1}}'),
        ('n', 'through one square centimetre: 6×10¹⁰ per second, through a thumbnail every second'),
    ])
    s.move('The detected flux is a third of this', [
        ('p', 'The measured flux on Earth is about a third of the prediction, and the resolution is neutrino oscillation: electron neutrinos convert into muon and tau flavours on the way out. The total flux is right; only the flavour mix changes.'),
        ('m', r'\phi_{\nu_e}\approx\frac{1}{3}\phi_\nu\ \ \mathrm{(oscillated)},\qquad \phi_{\mathrm{total}}\ \mathrm{conserved}'),
        ('n', 'a flux measurement is a flavour measurement, not a luminosity test'),
    ])
    s.chip('key', 'the chain of division', [('p', 'L → helium rate → neutrino rate → flux at 1 AU.'), ('p', '26.7 MeV and two neutrinos per helium.')])
    s.chip('gate', 'the assumptions', [('p', 'Steady Sun, p–p chain dominant (CNO is a few per cent), and no neutrino loss inside the Sun.')])
    s.chip('trap', 'one neutrino or two', [('p', 'Counting one neutrino per helium halves the flux; the chain emits two, one per positron annihilation step.')])
    s.figure('neutrino_flux')
    S.append(s); n += 1

    # =============================================================== OLY NUCLEAR 6
    s = Sheet(f'Olympiad-{n:02}-reactor-day', 'How much fuel does a reactor eat in a day?',
              'A gigawatt is a mass rate in disguise, and ten half-lives is an engineering unit of forgetfulness.',
              KO, n, total, 'source: OL7, §3.12',
              '1.05 kg per day per GW thermal; ten half-lives leaves 0.1 %',
              scale=1e8)
    s.move('Energy per day, then mass per day', [
        ('p', 'A gigawatt thermal for a day is 8.6×10¹³ J. Dividing by the energy released per gram of U-235 gives about a kilogram — the whole fuel bill of a large reactor fits in a briefcase.'),
        ('m', r'E_{\mathrm{day}}=10^9(86400)=8.6\times10^{13}\ \mathrm{J},\qquad m=\frac{8.6\times10^{13}}{8.2\times10^{10}}=1.05\ \mathrm{kg}'),
        ('n', 'at 33 % efficiency an electrical gigawatt needs three times that, about 3.2 kg/day'),
    ])
    s.move('Why a kilogram is not a gram', [
        ('p', 'Only the U-235 fissions; natural uranium is 0.7 % U-235, and a reactor enriches it to a few per cent. The mass of uranium consumed is therefore tens of times the mass fissioned, and most of the spent fuel is still uranium.'),
        ('m', r'm_{\mathrm{U}}\approx\frac{1.05}{0.04}\approx26\ \mathrm{kg/day}\ \ \mathrm{fed}'),
        ('n', 'at 4 % enrichment; the difference between burned and fed is the fuel cycle'),
    ])
    s.move('Ten half-lives is the storage shorthand', [
        ('p', 'Each half-life removes a factor two; ten of them remove a factor 1024. That is why "store it for ten half-lives" is the phrase in waste policy: it turns an alarming activity into a small fraction, without ever reaching zero.'),
        ('m', r'2^{-10}=9.8\times10^{-4}\approx0.1\,\%'),
        ('n', 'a 30-year isotope stored 300 years is ten half-lives — 0.1 % of the original activity'),
    ])
    s.chip('key', 'the numbers', [('p', '1.05 kg fissioned per GW·day (thermal).'), ('p', '≈26 kg of 4 % fuel fed per day.'),
                                  ('p', '2⁻¹⁰ ≈ 0.1 %.')])
    s.chip('gate', 'what this ignores', [('p', 'Burn-up, conversion ratio, decay heat, and the activity of the fission products — second-order for fuel mass, first-order for safety.')])
    s.chip('trap', 'thermal versus electric', [('p', 'Quoting 1.05 kg/day for a 1 GW *electric* plant. At 33 % efficiency it is three times that.')])
    s.figure('reactor_day')
    S.append(s); n += 1

    # =============================================================== OLY NUCLEAR 7
    s = Sheet(f'Olympiad-{n:02}-counting', 'How long must you count to know the rate to 1 %?',
              'Radioactive counts arrive like coin flips. The square-root tax sets every measurement time in the lab.',
              KO, n, total, 'source: OL8, §3.14, Q19, Q28',
              'σ = √N, so 1 % needs 10⁴ counts and four times the time halves the error',
              scale=1e6)
    s.move('Poisson statistics in one line', [
        ('p', 'Counts in a fixed window are independent events with a fixed mean, so the variance equals the mean. The absolute uncertainty is √N and the fractional uncertainty is 1/√N — the only error bar that gets relatively smaller as you count more.'),
        ('m', r'\sigma_N=\sqrt{N},\qquad \frac{\sigma_N}{N}=\frac{1}{\sqrt{N}}'),
        ('n', '10 000 counts carry 1 %; 100 counts carry 10 %'),
    ])
    s.move('Plan the time backwards from the precision', [
        ('p', 'At 100 counts per minute, 1 % needs 10 000 counts, which is 100 minutes. A weak sample at 1 count per minute needs 10 000 minutes — a week of counting for the same sentence.'),
        ('m', r'N=\left(\frac{1}{\epsilon}\right)^2=10^4\ \mathrm{for}\ \epsilon=1\,\%,\qquad t=\frac{N}{r}'),
        ('n', 'to halve the error you need four times the counts, hence four times the time'),
    ])
    s.move('Dead time and background bend the rule', [
        ('p', 'A Geiger counter is blind for a short dead time after each pulse, so at high rates it undercounts; the correction is n/(1 − nτ_d). Background counts add in quadrature, so a weak source must be counted with and without.'),
        ('m', r'n_{\mathrm{true}}=\frac{n_{\mathrm{obs}}}{1-n_{\mathrm{obs}}\tau_d},\qquad \sigma_{\mathrm{net}}=\sqrt{N_s+2N_b}'),
        ('n', 'at 1 % dead time and 10⁴ counts per second the correction is already 1 %'),
    ])
    s.chip('key', 'the tax', [('m', r'\sigma/N=1/\sqrt{N}'), ('p', '1 % → 10⁴ counts.'), ('p', '4× time halves the error.')])
    s.chip('gate', 'when Poisson holds', [('p', 'Independent decays, a stable rate, and a window short compared with the half-life.')])
    s.chip('trap', 'the doubled background', [('p', 'Subtracting background without adding its uncertainty — the net error is √(N_s + 2N_b), not √N_s.')])
    s.figure('counting_stats')
    S.append(s); n += 1

    # =============================================================== OLY NUCLEAR 8
    s = Sheet(f'Olympiad-{n:02}-isochron', 'How do you date a rock without knowing what it started with?',
              'Plot one isotope ratio against another. Every mineral of the same rock falls on one line, and the slope is the age.',
              KO, n, total, 'source: OL9, §3.11',
              'slope = e^{λt} − 1; the intercept absorbs the unknown initial daughter',
              scale=1e6)
    s.move('Write the daughter as initial plus produced', [
        ('p', 'The daughter isotope present now is whatever was there at birth plus what the parent has since produced. Dividing by a stable reference isotope turns abundances into ratios that can be measured precisely.'),
        ('m', r'\frac{D}{S}=\left(\frac{D}{S}\right)_0+\frac{P}{S}\left(e^{\lambda t}-1\right)'),
        ('n', 'D/S and P/S are measured; the unknowns are the intercept and the slope'),
    ])
    s.move('The line removes the unknown', [
        ('p', 'Different minerals in one rock have different P/S but the same age and the same initial D/S. Plotting D/S against P/S gives a straight line for every mineral: its slope is e^{λt} − 1 and its intercept is the initial ratio.'),
        ('m', r'\mathrm{slope}=e^{\lambda t}-1\ \Rightarrow\ t=\frac{\ln(1+\mathrm{slope})}{\lambda}'),
        ('n', 'scatter off the line is the diagnostic: it says the rock was disturbed'),
    ])
    s.move('Read an age off a slope', [
        ('p', 'For Rb–Sr, λ = 1.42×10⁻¹¹ per year. A slope of 0.05 gives ln(1.05)/λ = 3.4×10⁹ years, which is the age of an Archean rock.'),
        ('m', r't=\frac{\ln1.05}{1.42\times10^{-11}}=3.4\times10^9\ \mathrm{y}'),
        ('n', 'the same arithmetic as carbon dating, with a different constant and no initial-ratio guess'),
    ])
    s.chip('key', 'the line', [('p', 'D/S against P/S.'), ('p', 'Slope = e^{λt} − 1.'), ('p', 'Intercept = initial ratio.')])
    s.chip('gate', 'the isochron assumptions', [('p', 'One age for all minerals, one initial ratio, a closed system since formation.')])
    s.chip('trap', 'the model age', [('p', 'Using a single mineral and an assumed initial ratio gives a model age, not an isochron age. It is only as good as the assumption.')])
    s.figure('isochron')
    S.append(s); n += 1

    # =============================================================== OLY NUCLEAR 9
    s = Sheet(f'Olympiad-{n:02}-neutron-waves', 'Why do slow neutrons diffract from crystals?',
              'The same wave logic as the electron: compare the wavelength with the spacing. The spacing that matters is the lattice\u2019s.',
              KO, n, total, 'source: OL10, links Part 23 and Part 25',
              '1.8 Å neutrons match atomic spacings; inside a nucleus the same wave sees a point',
              scale=1e6)
    s.move('A thermal neutron has an angstrom wavelength', [
        ('p', 'A 25 meV neutron has λ = h/√(2mE) = 1.8 Å — the scale of atomic planes. That is why neutron diffraction needs no accelerator.'),
        ('m', r'\lambda=\frac{h}{\sqrt{2m_nE}}=1.8\ \mathrm{\AA}\ \ \mathrm{at}\ 25\ \mathrm{meV}'),
        ('n', 'the same formula as the electron\u2019s 1.226/√V nm, with the neutron mass and energy'),
    ])
    s.move('Two rulers, one formula', [
        ('p', 'Inside a nucleus the nucleon spacing is about 1.8 fm, a thousand times smaller. A thermal neutron with a 1.8 Å wave cannot resolve that structure — it sees the whole nucleus as a point scatterer. The physics did not change; the ratio λ/d did.'),
        ('m', r'd_{\mathrm{nucleon}}\approx\left(\frac{1}{0.17\ \mathrm{fm^{-3}}}\right)^{1/3}\approx1.8\ \mathrm{fm}\ \ll\ \lambda'),
        ('n', 'high-energy electrons (pm waves) are needed to see inside a nucleus, for exactly this reason'),
    ])
    s.move('Why neutrons rather than X-rays', [
        ('p', 'X-rays scatter from electrons, so hydrogen is nearly invisible. Neutrons scatter from nuclei, so light atoms show and isotopes contrast — same Bragg law, a different probe.'),
        ('m', r'2d\sin\theta=n\lambda\ \ \mathrm{(Bragg)},\qquad \lambda=1.8\ \mathrm{\AA}\ \Rightarrow\ \theta\ \mathrm{of\ order}\ 10^{\circ}'),
        ('n', 'magnetic moments also scatter neutrons, which is why they map spin structures'),
    ])
    s.chip('key', 'the comparison', [('p', 'λ(25 meV) = 1.8 Å.'), ('p', 'Lattice spacing ≈ 1.8 Å → diffraction.'),
                                     ('p', 'Nucleon spacing 1.8 fm → point scatterer.')])
    s.chip('gate', 'when diffraction works', [('p', 'λ comparable to the spacing. Much shorter gives a point image; much longer gives no Bragg condition at all.')])
    s.chip('trap', 'mixing the rulers', [('p', 'Using a thermal neutron to probe nuclear structure, or an MeV neutron to probe a crystal — the wavelength is wrong in both directions.')])
    s.figure('neutron_waves')
    S.append(s); n += 1

    # =============================================================== OLY NUCLEAR 10
    s = Sheet(f'Olympiad-{n:02}-solar-lifetime', 'How long can the Sun keep shining?',
              'Ten per cent of its hydrogen, 0.7 per cent of the mass of that fuel, and a luminosity you can measure.',
              KO, n, total, 'source: OL11, OL12, §3.13',
              '0.07 × 0.1 M☉ × 0.007c² / L ≈ 10 Gyr; and the drop says where the table ends',
              scale=1e6)
    s.move('Count the fuel, then the energy per gram', [
        ('p', 'Only the core hydrogen burns, and only 0.7 % of the fused mass becomes energy. Multiplying the available mass by 0.007c² gives the total energy budget; dividing by the luminosity gives the lifetime.'),
        ('m', r'E\approx0.1(0.7M_\odot)(0.007c^2)=8.7\times10^{43}\ \mathrm{J}'),
        ('n', 'the numbers: 10 % of the hydrogen, 70 % hydrogen by mass, 0.7 % mass-to-energy'),
    ])
    s.move('Divide by the luminosity', [
        ('p', 'The Sun radiates 3.83×10²⁶ W, so the budget lasts about 7×10⁹ years on the main sequence — and the independent mass-loss rate L/c² times that lifetime returns the burned mass, a useful cross-check.'),
        ('m', r't=\frac{8.7\times10^{43}}{3.83\times10^{26}}=2.3\times10^{17}\ \mathrm{s}\approx7\times10^9\ \mathrm{y}'),
        ('n', 'the Sun is middle-aged; the first weak step in the p–p chain, not the fuel, sets the pace'),
    ])
    s.move('The same liquid drop says where the table ends', [
        ('p', 'The fission barrier vanishes when the Coulomb gain from deformation beats twice the surface cost, near Z²/A ≈ 50. With A ≈ 2.5Z that is Z ≈ 125; shell corrections prop up superheavies a little beyond, but not indefinitely.'),
        ('m', r'\frac{Z^2}{A}\approx50,\quad A\approx2.5Z\ \Rightarrow\ Z\approx125'),
        ('n', 'bismuth (83) is the last fully stable element; beyond it, alpha decay is the leak'),
    ])
    s.chip('key', 'the budget', [('p', '10 % of the hydrogen is available.'), ('p', '0.007 of the mass becomes energy.'),
                                 ('p', 'L = 3.83×10²⁶ W → ≈7×10⁹ y.')])
    s.chip('gate', 'what is left out', [('p', 'Mass loss, core mixing, the red-giant phase, and the fact that the last of the hydrogen burns inefficiently.')])
    s.chip('trap', 'all the hydrogen', [('p', 'Using the whole mass, or the whole hydrogen, in the budget overestimates the lifetime by a factor of ten.')])
    s.figure('solar_budget')
    S.append(s)

    return S
