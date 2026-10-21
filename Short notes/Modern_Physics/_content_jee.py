"""Part I content: JEE Main + Advanced core of modern physics.

Every page is a Sheet: a question as the title, numbered moves down the main
column, evidence and warnings in the right-hand rail, one wide figure.
Sources: atomic-structure/, photoelectric-effect/, x-rays/, nuclear-physics/.
"""
from layout import Sheet

K = 'MODERN PHYSICS  /  PART I: JEE MAIN + ADVANCED'


def build(total):
    S = []

    # ============================================================ ATOMIC 1
    s = Sheet('JEE-01-rutherford', 'Why did one alpha in eight thousand come back?',
              'A pudding atom should never turn a fast alpha around. What did the bounces actually prove?',
              K, 1, total, 'source: Atomic-structure.md  §3.1-3.3, E1-E2',
              'the rare back-scatter is the measurement: charge sits in a nucleus, not a cloud',
              scale=5e6)
    s.move('Predict first, then look', [
        ('p', 'Thomson spread the positive charge through a sphere of radius about 10⁻¹⁰ m. An alpha inside it feels a field growing linearly from the centre and peaking at kZe/R² at the surface. Work out the impulse before looking at the data: that is what makes this a test.'),
        ('m', r'\theta\sim\frac{kZe^2}{K\,R},\qquad \theta\lesssim 1^{\circ}'),
        ('n', 'multiple scattering averages out further: the pudding predicts a straight beam'),
    ])
    s.move('The impulse budget of a soft charge', [
        ('p', 'A 5 MeV alpha spends about 10⁻¹⁸ s inside the atom, and the largest available force in that time gives a transverse momentum far below its own: a fraction of a degree. To turn it 90° the charge must sit inside 10⁻¹⁴ m, where the force is a hundred times larger.'),
        ('m', r'f=\pi b^2nt:\quad b_{\mathrm{90^{\circ}}}\approx 2.3\times10^{-14}\ \mathrm{m}\ \Rightarrow\ f\approx\frac{1}{8000}'),
        ('n', 'f is the fraction of nuclei’s cross-sectional area the foil presents'),
    ])
    s.move('What the one-in-eight-thousand means', [
        ('p', 'The observed fraction is an area measurement. Invert f = πb²nt and the angle-90° impact parameter falls out: nucleus tens of fm, atom 10⁵ fm — a marble in an empty cathedral.'),
        ('n', 'r_min is an upper bound on nuclear size while the force stays Coulomb — it is not a radius'),
    ])
    s.chip('key', 'the two numbers', [('m', r'r_{\min}=\frac{2kZe^2}{K}'),
                                     ('m', r'\tan\frac{\theta}{2}=\frac{kZe^2}{mv^2b}'),
                                     ('p', 'f = πb²nt is an area ratio, not a force')])
    s.chip('trap', 'what r_min is not', [('p', 'It is not the nuclear radius. It is a head-on upper bound, valid only while the force is pure Coulomb.'),
                                         ('p', 'Large-angle scattering does not mean contact: it means small b.')])
    s.chip('num', 'carry these', [('p', '1 in 8000 back-scattered (gold, ~90°)'),
                                  ('p', 'kZe² for gold = 114 eV nm'),
                                  ('p', 'nuclear scale few fm; atom 10⁵ fm')])
    s.figure('thomson_vs_rutherford')
    S.append(s)

    # ============================================================ ATOMIC 2
    s = Sheet('JEE-02-closest-approach', 'How close can an alpha get before the law breaks?',
              'Rutherford’s formula held at every angle measured. Where must it stop, and what stops it?',
              K, 2, total, 'source: §3.2-3.3, OL12; Nuclear-physics.md §3.1',
              'r_min shrinks as 1/K until it reaches the nuclear surface — that is where new physics starts',
              scale=5e6)
    s.move('The hyperbola, in one line', [
        ('p', 'A Coulomb encounter is a conic section. The impact parameter b is the miss distance the alpha would have had with no force at all; the scattering angle follows from angular momentum plus the impulse integral.'),
        ('m', r'\tan\frac{\theta}{2}=\frac{kZe^2}{mv^2b}=\frac{r_h}{2b},\qquad r_h=\frac{2kZe^2}{K}'),
        ('n', 'b → 0 gives back-scatter; b → ∞ gives a straight track'),
    ])
    s.move('Invert it and you have a ruler', [
        ('p', 'Because the angle depends on b only through the ratio r_h/2b, measuring θ measures b. The fraction scattered beyond a given angle is then the area of the disk πb² times the areal density of nuclei, nt.'),
        ('m', r'\frac{d\sigma}{d\Omega}=\left(\frac{r_h}{4}\right)^2\frac{1}{\sin^4(\theta/2)}'),
        ('n', 'the sin⁻⁴ law: halving the angle multiplies the count sixteenfold'),
    ])
    s.move('Where the Coulomb picture must fail', [
        ('p', 'Set r_min equal to the nuclear radius. Above that beam energy the alpha touches the nuclear surface, the potential stops being 1/r, and the measured distribution departs from sin⁻⁴. Natural alphas at 5–8 MeV probe only the clean Coulomb regime; accelerators above a few tens of MeV see the deviation.'),
        ('m', r'K_{\mathrm{fail}}=\frac{2kZe^2}{R}\approx32\ \mathrm{MeV}\ \ (\mathrm{gold}, R\approx7\ \mathrm{fm})'),
    ])
    s.chip('key', 'the geometry', [('m', r'\tan(\theta/2)=r_h/2b'), ('m', r'r_h=2kZe^2/K'),
                                   ('p', 'At 90°: b = r_h/2, always.')])
    s.chip('gate', 'when the formula holds', [('p', 'Pure Coulomb, point nucleus, no recoil, non-relativistic alpha.'),
                                              ('p', 'All four fail at high energy or high Z.')])
    s.chip('trap', 'angle convention', [('p', 'θ is measured from the incoming direction, not from the normal to the foil.')])
    s.figure('closest_approach')
    S.append(s)

    # ============================================================ ATOMIC 3
    s = Sheet('JEE-03-standing-wave', 'Why is angular momentum n times h-bar?',
              'Bohr postulated it. de Broglie’s wave makes it a closure condition on a circle.',
              K, 3, total, 'source: §3.4-3.5, OL2; Photoelectric-effect.md §3.8',
              'an orbit is allowed when the electron’s wave closes on itself in phase',
              scale=13.6)
    s.move('A wave on a ring either closes or cancels', [
        ('p', 'Put a de Broglie wave on a circle. If a whole number of wavelengths fits the circumference it meets itself in phase and stands; if not, it destroys itself. That single condition is the quantisation.'),
        ('m', r'2\pi r=n\lambda=n\frac{h}{p}\ \Rightarrow\ pr=n\hbar'),
        ('n', 'on a circle, pr is exactly the angular momentum — nothing else had to be assumed'),
    ])
    s.move('Add the force, get the atom', [
        ('p', 'Two equations now: closure and Coulomb force balance. Eliminate v between them and every hydrogen number follows with no adjustable constant.'),
        ('m', r'\frac{mv^2}{r}=\frac{ke^2}{r^2},\qquad mvr=n\hbar'),
        ('m', r'r_n=\frac{n^2\hbar^2}{m_eke^2}=0.529\,\frac{n^2}{Z}\ \mathrm{\mathring{A}}'),
    ])
    s.move('The same algebra gives speed and energy', [
        ('p', 'Substituting back gives the speed and, with E = K + U, the ladder. K = −E and U = 2E, so the virial relation is a free check on every result.'),
        ('m', r'v_n=\frac{kZe^2}{n\hbar}=2.19\times10^6\frac{Z}{n}\ \mathrm{m/s}'),
        ('m', r'E_n=-\frac{m_ek^2Z^2e^4}{2\hbar^2n^2}=-13.6\frac{Z^2}{n^2}\ \mathrm{eV}'),
        ('n', 'K = −E and U = 2E, so the electron is always more kinetic than bound'),
    ])
    s.chip('key', 'the closure', [('m', r'2\pi r=n\lambda'), ('m', r'L=n\hbar'),
                                  ('p', 'One condition replaces a postulate.')])
    s.chip('insight', 'why it is exact', [('p', 'The condition fixes the shape of the wave, and the Coulomb force fixes its scale. Two equations, two unknowns, no fitting.')])
    s.chip('trap', 'the two-pi slip', [('p', 'L = nh/(2π) = nℏ, never nh. And λ = h/p, not h/mv with a different v.')])
    s.figure('standing_wave')
    S.append(s)

    # ============================================================ ATOMIC 4
    s = Sheet('JEE-04-bohr-ladder', 'What does the hydrogen ladder actually look like?',
              'Thirty years of spectroscopy in one diagram. Read it as a table, not a picture.',
              K, 4, total, 'source: §3.5-3.6, E3-E4, E9',
              'radius as n², binding as 1/n², and 13.6(1/n_f² − 1/n_i²) eV per arrow',
              scale=13.6)
    s.move('Three columns, one formula each', [
        ('p', 'Every hydrogenic quantity is a power of n. The radius grows as n², the speed falls as 1/n, and the binding energy falls as 1/n². Write them as three columns and the page becomes a lookup table rather than a derivation.'),
        ('m', r'r_n=0.529\frac{n^2}{Z}\ \mathrm{\mathring{A}},\quad v_n=2.19\times10^6\frac{Z}{n},\quad E_n=-13.6\frac{Z^2}{n^2}\ \mathrm{eV}'),
    ])
    s.move('The gap, not the level, is what you see', [
        ('p', 'A photon carries the difference between two levels. Using hc = 1240 eV nm, a gap in eV converts to a wavelength by one division, which is the whole arithmetic of the chapter.'),
        ('m', r'\frac{1}{\lambda}=RZ^2\left(\frac{1}{n_f^2}-\frac{1}{n_i^2}\right),\qquad \lambda=\frac{1240}{\Delta E}'),
        ('n', 'R = 1.097×10⁷ m⁻¹; hcR = 13.6 eV, so the two forms are the same statement'),
    ])
    s.move('Bound means negative', [
        ('p', 'Zero energy is the electron at rest at infinity. A bound electron therefore has negative total energy, and its ionisation energy is the positive quantity −E_n. Excitation energy is the difference of two levels; ionisation always ends at zero.'),
        ('m', r'\mathrm{IE}_n=-E_n=\frac{13.6\,Z^2}{n^2}\ \mathrm{eV},\qquad \mathrm{IP}\ (\mathrm{volts})=\mathrm{IE}\ (\mathrm{eV})'),
        ('n', 'for a singly charged electron the two numbers coincide; for an alpha they do not'),
    ])
    s.chip('key', 'the ladder', [('m', r'E_n=-13.6\,Z^2/n^2'), ('m', r'\lambda=1240/\Delta E\ \mathrm{(nm,eV)}'),
                                 ('p', 'r ∝ n², v ∝ 1/n, |E| ∝ 1/n²')])
    s.chip('check', 'instant audits', [('p', 'Ground state must return −13.6 eV at Z = 1.'), ('p', 'A gap must be smaller than the ionisation energy it sits under.')])
    s.chip('trap', 'signs and units', [('p', 'Subtracting two excited levels when asked to ionise — ionisation ends at 0 eV.'),
                                       ('p', 'Plugging a wavelength in nm into hc = 1240 eV nm the wrong way round.')])
    s.figure('bohr_ledger')
    S.append(s)

    # ============================================================ ATOMIC 5
    s = Sheet('JEE-05-series', 'Which series is which, and why five names?',
              'Lyman, Balmer, Paschen, Brackett, Pfund: one formula, five finishing rungs.',
              K, 5, total, 'source: §3.6, E4, E9; Q-bank series items',
              'the series is named by its lower level: n_f = 1, 2, 3, 4, 5',
              scale=1.89)
    s.move('Fix the lower level and the family appears', [
        ('p', 'Everything that lands on n = 1 is Lyman (ultraviolet), on n = 2 is Balmer (the visible one), on n = 3 is Paschen (infrared), then Brackett and Pfund further out. The formula does not change; only n_f does.'),
        ('m', r'\frac{1}{\lambda}=R\left(\frac{1}{n_f^2}-\frac{1}{n_i^2}\right),\qquad n_i>n_f'),
    ])
    s.move('The two ends of any series', [
        ('p', 'The longest wavelength in a series is the smallest step, n_f + 1 → n_f. The shortest is the limit n_i → ∞, which is the ionisation edge of that lower level. Every series therefore runs from a line to a continuum edge.'),
        ('m', r'\lambda_{\max}=\frac{1}{R}\frac{n_f^2(n_f+1)^2}{2n_f+1},\qquad \lambda_{\min}=\frac{n_f^2}{R}'),
        ('n', 'Balmer: 656 nm down to the 365 nm edge, which is why it is the visible one'),
    ])
    s.move('What the eye can and cannot see', [
        ('p', 'Only Balmer overlaps the 380–750 nm window, and only its first three lines are comfortably visible. Lyman is vacuum ultraviolet; Paschen is infrared. This is not an accident of hydrogen — it is why stellar spectra are classified by which series is strong.'),
        ('n', 'a hydrogen discharge looks pink because Hα at 656 nm dominates the visible output'),
    ])
    s.chip('key', 'the five names', [('p', 'Lyman 1, Balmer 2, Paschen 3, Brackett 4, Pfund 5.'),
                                     ('p', 'Only Balmer is visible.'), ('m', r'\lambda_{\min}=n_f^2/R')])
    s.chip('trap', 'counting the wrong thing', [('p', '“Lines in the Balmer series from n = 5” is four (5→2, 4→2, 3→2 plus the 5→... no: 5→2, 4→2, 3→2 = three). Total lines from n = 5 is ten.')])
    s.chip('num', 'bench numbers', [('p', 'Hα 656.3 nm · Hβ 486.1 · Hγ 434.0 · Hδ 410.2'),
                                    ('p', 'Lyman α 121.6 nm · Balmer edge 364.6 nm')])
    s.figure('spectrum_series')
    S.append(s)

    # ============================================================ ATOMIC 6
    s = Sheet('JEE-06-excitation', 'What can a 12.5 eV electron do that a 12.5 eV photon cannot?',
              'Same energy, different menu. The rule about who may pay in part is worth marks every year.',
              K, 6, total, 'source: §3.7, E7-E8; traps 6-9',
              'electrons may hand over part of their energy; photons must be absorbed whole',
              scale=11.5)
    s.move('The electron menu', [
        ('p', 'A bombarding electron can transfer any amount up to its whole kinetic energy, because it keeps the remainder as its own motion. So every level with excitation energy below the beam energy is reachable.'),
        ('m', r'E_{\mathrm{exc}}=13.6\left(1-\frac{1}{n^2}\right)\mathrm{eV}:\ 10.2,\ 12.09,\ 12.75'),
        ('n', 'a 12.5 eV beam reaches n = 2 and n = 3, and stops short of n = 4'),
    ])
    s.move('The photon menu', [
        ('p', 'A photon is created or absorbed as one unit. It cannot give 10.2 eV and carry 2.3 eV away, so a 12.5 eV photon is not absorbed by the 10.2 eV transition at all — it simply passes. Resonance is a matching condition, not a threshold.'),
        ('m', r'hf=E_i-E_f\quad \mathrm{exactly}'),
        ('n', 'this is why the absorption spectrum has dark lines at precise wavelengths only'),
    ])
    s.move('Above the ionisation limit', [
        ('p', 'Once the photon energy exceeds the binding energy the electron is freed and the surplus becomes kinetic energy. The spectrum changes character: discrete lines below the limit, a continuum above it. The ionisation edge is the last line of a series.'),
        ('m', r'K_{\max}=hf-\mathrm{IE},\qquad hf>\mathrm{IE}'),
    ])
    s.chip('key', 'the asymmetry', [('m', r'E_{\mathrm{exc}}=13.6(1-n^{-2})'),
                                    ('p', 'Electron: any gift up to full. Photon: all or nothing.')])
    s.chip('trap', 'three classics', [('p', 'Letting an 11 eV photon excite the 10.2 eV level.'), ('p', 'Forgetting the cascade: exciting n = 3 gives three lines, not one.'), ('p', 'Confusing excitation energy with ionisation energy.')])
    s.chip('num', 'hydrogen thresholds', [('p', 'n=2: 10.2 eV / 121.6 nm'), ('p', 'n=3: 12.09 eV / 102.6 nm'), ('p', 'ionisation: 13.6 eV / 91.2 nm')])
    s.figure('excitation_ladder')
    S.append(s)

    # ============================================================ ATOMIC 7
    s = Sheet('JEE-07-hydrogenic', 'How far does Z² scaling carry you?',
              'He⁺, Li²⁺, muonic hydrogen and positronium are the same atom with two numbers changed.',
              K, 7, total, 'source: §3.8, E5-E6, OL5',
              'charge scales everything by Z², mass by the reduced mass — nothing else changes',
              scale=13.6)
    s.move('Charge: divide the radius, square the energy', [
        ('p', 'A nucleus of charge Ze pulls harder, so the orbit shrinks as 1/Z while every energy multiplies by Z². He⁺ therefore has a ground state at −54.4 eV and an orbit of 0.265 Å; Li²⁺ has −122.4 eV.'),
        ('m', r'r_n\propto\frac{1}{Z},\qquad E_n\propto Z^2,\qquad \lambda\propto\frac{1}{Z^2}'),
        ('n', 'the 2 → 1 line of Li²⁺ is 13.5 nm, deep in the soft X-ray'),
    ])
    s.move('Mass: the nucleus is not nailed down', [
        ('p', 'The electron and nucleus orbit their common centre of mass, and every mass-dependent result takes the reduced mass μ = m_eM/(m_e+M). For hydrogen the correction is 0.05 %; for deuterium it shifts Hα by 0.18 nm, which is how deuterium was found.'),
        ('m', r'R_M=R_\infty\frac{\mu}{m_e},\qquad \Delta\lambda/\lambda\approx\frac{m_e}{2M}'),
    ])
    s.move('Exotic atoms are scaling tests', [
        ('p', 'Replace the electron with a muon and μ ≈ 207 m_e: the atom shrinks by 207 and binds 207 times harder, so its orbit sits inside the nucleus and its levels measure nuclear size. Positronium has μ = m_e/2, so it is twice as big and half as bound.'),
        ('m', r'a_\mu=\frac{0.529\ \mathrm{\AA}}{207}=256\ \mathrm{fm},\qquad E_1=-2.81\ \mathrm{keV}'),
        ('n', 'positronium: 1.06 Å, −6.8 eV, and every wavelength doubled'),
    ])
    s.chip('key', 'the two dials', [('m', r'r\propto n^2/Z'), ('m', r'E\propto Z^2/n^2'),
                                    ('p', 'and m_e → μ for any mass-dependent quantity')])
    s.chip('trap', 'forgetting Z', [('p', 'Using −13.6/n² for He⁺. Every energy carries Z², every radius 1/Z.'),
                                    ('p', 'Using m_e where the reduced mass belongs — the whole point of exotic atoms.')])
    s.chip('num', 'scaled ground states', [('p', 'H −13.6 eV, 0.529 Å'), ('p', 'He⁺ −54.4 eV, 0.265 Å'), ('p', 'Li²⁺ −122.4 eV, 0.176 Å')])
    s.figure('hydrogenic_scaling')
    S.append(s)

    # ============================================================ ATOMIC 8
    s = Sheet('JEE-08-quantum-numbers', 'What are the other three numbers for?',
              'Bohr gave one integer. Spectroscopy needs four, and each one explains a different splitting.',
              K, 8, total, 'source: §3.10, E7, E11',
              'n sets the energy; l, m_l, m_s decide which transitions are allowed and how they split',
              scale=1.89)
    s.move('The numbers and their counts', [
        ('p', 'For a given n, l runs 0…n−1, m_l runs −l…+l, and m_s is ±½. Counting states gives 2n² per shell, which is the periodic-table arithmetic in one line.'),
        ('m', r'n:\ 1,2,\dots;\quad l<n;\quad -l\le m_l\le l;\quad m_s=\pm\frac{1}{2}'),
        ('n', 'shell n holds 2n² states: 2, 8, 18, 32'),
    ])
    s.move('A field turns one level into a fan', [
        ('p', 'An orbiting electron is a current loop with magnetic moment μ_B per unit ℏ. A field B splits a level into 2l+1 components spaced by μ_B B, which is why a line seen in a magnetic field becomes a triplet.'),
        ('m', r'\Delta E=m_l\mu_BB,\qquad \mu_B=5.79\times10^{-5}\ \mathrm{eV/T}'),
        ('n', 'at 1 T the Hα line splits by 0.02 nm: small, but resolvable with a grating'),
    ])
    s.move('Selection rules decide which lines exist', [
        ('p', 'Not every pair of levels radiates: a photon carries one unit of angular momentum, so Δl = ±1 and Δm_l = 0, ±1. That is why some transitions are bright, others forbidden, and why the number of lines from a cascade is smaller than the number of level pairs.'),
        ('m', r'\Delta l=\pm1,\qquad \Delta m_l=0,\pm1'),
    ])
    s.chip('key', 'counts and splits', [('m', r'N=n(n-1)/2'), ('m', r'\Delta E=m_l\mu_BB'),
                                        ('p', '2n² states in shell n')])
    s.chip('gate', 'what this model ignores', [('p', 'Spin-orbit fine structure (10⁻⁴ eV) is named, not derived.'), ('p', 'The anomalous factor g ≈ 2 is outside the syllabus.')])
    s.chip('trap', 'reading the question', [('p', 'If it says “orbital only”, use m_lμ_BB and do not double for spin.')])
    s.figure('quantum_numbers')
    S.append(s)

    # ============================================================ PHOTON 1
    s = Sheet('JEE-09-photon', 'What exactly is in a beam of light?',
              'Counting coins: energy per photon, photons per second, and the push they give.',
              K, 9, total, 'source: Photoelectric-effect.md §3.4, E1, E6-E7',
              'a beam is n photons per second, each carrying hf and momentum h/λ',
              scale=2.1)
    s.move('Energy per photon', [
        ('p', 'One quantum carries hf, which in the units of this chapter is 1240 divided by the wavelength in nanometres. That single conversion does most of the numerical work in the chapter.'),
        ('m', r'E=hf=\frac{hc}{\lambda}=\frac{1240}{\lambda\ [\mathrm{nm}]}\ \mathrm{eV}'),
        ('n', 'green light at 550 nm: 2.25 eV; a 100 keV X-ray: 0.0124 nm'),
    ])
    s.move('Photons per second, and per cubic metre', [
        ('p', 'Divide the beam power by the energy per photon. Spread over a sphere, the intensity falls as 1/r², so the flux does too; inside the beam the number density is the flux divided by c.'),
        ('m', r'\dot N=\frac{P}{hf},\qquad n=\frac{I}{hf},\qquad n_{\mathrm{vol}}=\frac{I}{hfc}'),
        ('n', 'a 100 W sodium lamp at 589 nm emits 3×10²⁰ photons per second'),
    ])
    s.move('A beam pushes', [
        ('p', 'Each photon arrives with momentum h/λ and leaves with either none (absorbed) or the reverse (reflected). The force is the momentum delivered per second, which is P/c or 2P/c. This is radiation pressure, derived here by counting rather than by fields.'),
        ('m', r'F=\frac{P}{c}(1+R),\qquad p_{\mathrm{rad}}=\frac{I}{c}\ (1+R)'),
        ('n', 'the force from a 1 W reflected beam is 6.7 nN — a microgram’s weight'),
    ])
    s.chip('key', 'the three lines', [('m', r'E=1240/\lambda\ \mathrm{(eV,nm)}'), ('m', r'p=h/\lambda'),
                                      ('m', r'F=P(1+R)/c')])
    s.chip('trap', 'massive-photon thinking', [('p', 'Using p = E/c for an electron. That relation is for massless particles; electrons take p = √(2mK).'),
                                               ('p', 'Forgetting the factor 2 when a surface reflects.')])
    s.chip('num', 'one-line conversions', [('p', 'hc = 1240 eV nm = 1.99×10⁻²⁵ J m'), ('p', '1 eV = 1.602×10⁻¹⁹ J'), ('p', 'h = 6.63×10⁻³⁴ J s')])
    s.figure('photon_packet')
    S.append(s)

    # ============================================================ PHOTON 2
    s = Sheet('JEE-10-photoelectric', 'Why does brighter light not give faster electrons?',
              'Five experimental facts, and the two that no wave theory can survive.',
              K, 10, total, 'source: §3.2-3.5, E2-E3, E10',
              'intensity sets the number of electrons; frequency sets their maximum energy',
              scale=1.8)
    s.move('The five facts', [
        ('p', 'There is a threshold frequency below which nothing is emitted at any intensity. Emission is instantaneous, within about a nanosecond. Current is proportional to intensity. Maximum kinetic energy grows with frequency and ignores intensity. The stopping potential is therefore a function of frequency alone.'),
        ('n', 'three of the five are also what a wave predicts — they are decoys, not discriminators'),
    ])
    s.move('Einstein’s one line', [
        ('p', 'One photon is absorbed by one electron. The electron pays a toll φ to escape the surface and keeps the rest as kinetic energy. Nothing about intensity appears here, which is why the maximum energy ignores it.'),
        ('m', r'K_{\max}=hf-\phi,\qquad eV_s=K_{\max}'),
        ('n', 'if hf < φ the right-hand side is negative and the answer is “no emission”'),
    ])
    s.move('The graph that measured Planck’s constant', [
        ('p', 'Plot stopping potential against frequency. Every metal gives the same slope h/e and a different intercept −φ/e. Millikan’s measurements of that slope agreed with the blackbody value of h, which is the cross-check that made the photon unavoidable.'),
        ('m', r'V_s=\frac{h}{e}f-\frac{\phi}{e},\qquad f_0=\frac{\phi}{h}'),
        ('n', 'slope 4.14×10⁻¹⁵ V s for every metal ever measured'),
    ])
    s.chip('key', 'the balance', [('m', r'K_{\max}=hf-\phi'), ('m', r'eV_s=hf-\phi'),
                                  ('p', 'threshold λ₀ = 1240/φ (nm, eV)')])
    s.chip('trap', 'four automatic zeros', [('p', 'Brighter light raising V_s.'), ('p', 'Writing K_max = hf and forgetting the toll.'),
                                            ('p', 'Expecting emission at threshold with energy: at λ₀ electrons emerge with zero.')])
    s.chip('num', 'work functions', [('p', 'Na 2.28 eV · Zn 4.3 eV · Cs 1.9 eV · Pt 5.6 eV')])
    s.figure('photoelectric_curve')
    S.append(s)

    # ============================================================ PHOTON 3
    s = Sheet('JEE-11-stopping', 'How do you read a photocurrent graph?',
              'Two plateaux, one cutoff. Learn which knob moves which feature.',
              K, 11, total, 'source: §3.5-3.6, E10; traps 3, 8-9',
              'the cutoff marks the fastest electron; the plateau marks how many there are',
              scale=2.0)
    s.move('One curve, three features', [
        ('p', 'Sweep the collector voltage. At large negative voltage the current is zero — even the fastest electron is turned back. Raise the voltage, electrons are collected, and at large positive voltage every emitted electron is collected: the current saturates.'),
        ('m', r'eV_s=K_{\max},\qquad I_{\mathrm{sat}}\propto\ \mathrm{emission\ rate}'),
        ('n', 'the saturation plateau is a collection limit, not a quantum effect'),
    ])
    s.move('Doubling the intensity', [
        ('p', 'Twice the photons means twice the electrons, so the plateau doubles. But each electron still gets the same photon energy, so the cutoff stays exactly where it was. Two curves, one edge.'),
        ('n', 'any answer that moves the cutoff with intensity contradicts the whole experiment'),
    ])
    s.move('Raising the frequency instead', [
        ('p', 'At fixed intensity, higher frequency means fewer photons per second — each carries more energy — so the current actually falls slightly while the cutoff climbs. This is the subtle row that examiners use to separate people who track photons from people who track watts.'),
        ('m', r'n=\frac{I}{hf}:\quad f\uparrow\ \Rightarrow\ n\downarrow\ \mathrm{at\ fixed}\ I'),
    ])
    s.chip('key', 'read the graph', [('m', r'eV_s=K_{\max}'), ('p', 'Left intercept: −V_s. Plateau height: rate. Slope of V_s vs f: h/e.')])
    s.chip('gate', 'assumptions', [('p', 'One photon per electron; clean surface with a single φ; no field emission; no space charge.')])
    s.chip('trap', 'saturation is not quantum', [('p', 'Citing the saturation current as evidence for photons. It is geometry — every emitted electron collected.')])
    s.figure('stopping_graph')
    S.append(s)

    # ============================================================ PHOTON 4
    s = Sheet('JEE-12-photocell', 'What does a photocell measure, and what does it not?',
              'A battery and an ammeter separate two quantities that classical physics could not.',
              K, 12, total, 'source: §3.2, §3.6, §3.12; E2',
              'the battery measures energy per electron; the ammeter measures electrons per second',
              scale=2.3)
    s.move('The apparatus is a filter', [
        ('p', 'An evacuated tube holds an emitter and a collector. Light ejects electrons from the emitter; a variable voltage either helps them across or turns them back. The ammeter reads how many arrive, the voltmeter tells you at what retarding voltage they stop.'),
        ('n', 'evacuated matters: in air the electrons collide with molecules within micrometres'),
    ])
    s.move('Three knobs, three different answers', [
        ('p', 'Intensity, frequency and collector voltage each move one feature and leave the others alone. That independence is the experimental content of the photon model, and it is why the photocell is a measuring instrument rather than a demonstration.'),
        ('m', r'I_{\mathrm{sat}}\propto I,\qquad V_s=\frac{hf-\phi}{e}'),
    ])
    s.move('Where the ideal picture leaks', [
        ('p', 'Real photocells have a spread of work functions, so the knee is soft rather than sharp. Very high intensity brings space-charge limiting; very high frequency makes the window absorb. None of these changes the threshold logic; they change the shape of the knee.'),
        ('n', 'a soft knee is not evidence against quantisation — it is a dirty surface'),
    ])
    s.chip('key', 'what each knob does', [('p', 'intensity → plateau'), ('p', 'frequency → cutoff'), ('p', 'collector voltage → collection only')])
    s.chip('insight', 'why it matters', [('p', 'The same device is a light meter, a night-vision tube and a solar cell’s front end: one photon in, one electron out.')])
    s.chip('trap', 'current versus frequency', [('p', 'At fixed intensity, higher f gives fewer photons and a slightly lower current — not a higher one.')])
    s.figure('photocell_iv')
    S.append(s)

    # ============================================================ MATTER 1
    s = Sheet('JEE-13-debroglie', 'Do electrons have a wavelength?',
              'If light can be a particle, matter can be a wave. The only question is how big.',
              K, 13, total, 'source: §3.7, E5; Photoelectric-effect.md §3.7',
              'λ = h/p: large for electrons at a few volts, absurdly small for anything you can hold',
              scale=100)
    s.move('The hypothesis, and its one-line consequence', [
        ('p', 'Attach to any particle the same relation that photons obey. For an electron accelerated from rest through V volts, the kinetic energy fixes the momentum, and the wavelength follows.'),
        ('m', r'\lambda=\frac{h}{p}=\frac{h}{\sqrt{2m_e eV}}=\frac{1.226}{\sqrt{V}}\ \mathrm{nm}'),
        ('n', '100 V gives 0.123 nm — the spacing of atoms, which is why crystals diffract electrons'),
    ])
    s.move('Why you never see a cricket ball diffract', [
        ('p', 'A 0.15 kg ball at 30 m/s has λ ≈ 10⁻³⁴ m. Wave behaviour appears only when the wavelength is comparable to the geometry it meets, so a ball needs slits 10⁻³⁴ m apart. The classical world is the limit λ ≪ every dimension.'),
        ('m', r'\lambda_{\mathrm{ball}}=\frac{6.63\times10^{-34}}{(0.15)(30)}=1.5\times10^{-34}\ \mathrm{m}'),
    ])
    s.move('Electron microscopes are the practical payoff', [
        ('p', 'Resolution is limited by the wavelength used. At 10 kV an electron has λ = 0.012 nm, four orders finer than green light, so the same lens geometry can in principle resolve viral structure. Aberrations eat most of that gain; they do not remove it.'),
        ('n', 'slow electrons (tens of eV) have wavelengths of a few ångström — ideal for surfaces'),
    ])
    s.chip('key', 'the bridge', [('m', r'\lambda=h/p'), ('m', r'\lambda=1.226/\sqrt{V}\ \mathrm{nm}'),
                                 ('p', 'p = √(2mK) non-relativistic; p = √(K² + 2mKc²)/c exact')])
    s.chip('trap', 'the four percent', [('p', 'The square-root formula is wrong above about 3 kV by more than 1 %.'), ('p', 'And p = E/c is only for massless particles.')])
    s.chip('num', 'bench wavelengths', [('p', '100 V: 0.123 nm · 10 kV: 0.0123 nm'), ('p', 'thermal neutron: 0.18 nm · green light: 550 nm')])
    s.figure('debroglie_scale')
    S.append(s)

    # ============================================================ MATTER 2
    s = Sheet('JEE-14-davisson-germer', 'Was the electron wave ever actually seen?',
              'Two experiments in 1927 turned a hypothesis into a measurement: a crystal and a detector.',
              K, 14, total, 'source: §3.10, E11; X-rays.md §3.7 (Bragg)',
              'the diffraction angle follows 2d sinθ = nλ, and λ is exactly h/p',
              scale=54)
    s.move('A crystal is a grating with ångström spacing', [
        ('p', 'Atoms in a crystal sit 1–3 Å apart, which is the wavelength of a 50–150 V electron. The crystal therefore acts as a three-dimensional grating, and reflected beams appear only at angles where the path difference between successive planes is a whole number of wavelengths.'),
        ('m', r'2d\sin\theta=n\lambda'),
        ('n', 'θ is the glancing angle, measured from the plane — not from the normal'),
    ])
    s.move('The 1927 numbers', [
        ('p', 'Davisson and Germer fired 54 V electrons at nickel and found a strong lobe at 65° from the incident beam. With the known plane spacing of 0.91 Å, Bragg predicts a wavelength of 1.65 Å; de Broglie gives 1.67 Å. The two agree to the accuracy of the day.'),
        ('m', r'\lambda_{\mathrm{Bragg}}=2(0.91)\sin65^{\circ}=1.65\ \mathrm{\mathring{A}}'),
        ('m', r'\lambda_{\mathrm{deB}}=\frac{1.226}{\sqrt{54}}=1.67\ \mathrm{\mathring{A}}'),
    ])
    s.move('What followed', [
        ('p', 'The same logic runs today as LEED in every surface lab, and as electron diffraction in structural biology. Slow electrons are used deliberately: a long wavelength both diffracts strongly and penetrates only a few atomic layers, so the pattern is a picture of the surface.'),
        ('n', 'slower electrons diffract more, not less — lower energy means longer wavelength'),
    ])
    s.chip('key', 'the pair', [('m', r'2d\sin\theta=n\lambda'), ('m', r'\lambda=h/p'),
                               ('p', 'Bragg gives the wavelength from geometry; de Broglie predicts it from voltage.')])
    s.chip('gate', 'why the peak is sharp', [('p', 'Constructive interference over thousands of planes; a small angle error destroys the sum.')])
    s.chip('trap', 'angle and order', [('p', 'Writing 2d cosθ, or calling the second observed peak n = 1.'), ('p', 'Forgetting that the detector angle is 2θ.')])
    s.figure('davisson_germer')
    S.append(s)

    # ============================================================ MATTER 3
    s = Sheet('JEE-15-uncertainty', 'Why does the electron not fall into the nucleus?',
              'A classical orbiting charge radiates and dies in picoseconds. Something holds the atom up.',
              K, 15, total, 'source: §3.9, E9, E12; OL3',
              'confinement costs momentum; the ground state is where that cost stops paying',
              scale=13.6)
    s.move('A localised particle cannot have a definite momentum', [
        ('p', 'A pure sine has a perfect wavelength and no position. To localise a particle you superpose many waves; the narrower the packet, the wider the spread of momenta.'),
        ('m', r'\Delta x\,\Delta p\gtrsim\frac{\hbar}{2}'),
        ('n', 'a statement about waves, not about clumsy equipment; squeeze further and the kinetic term wins'),
    ])
    s.move('Minimise the total energy', [
        ('p', 'Confine an electron to radius r: its momentum is at least ℏ/r, so the kinetic term grows as 1/r² while the Coulomb well deepens as −1/r. The sum has a minimum, and that minimum is the hydrogen atom.'),
        ('m', r'E(r)\approx\frac{\hbar^2}{2m_er^2}-\frac{ke^2}{r}'),
        ('m', r'r_{\min}=\frac{\hbar^2}{m_eke^2}=0.529\ \mathrm{\AA},\qquad E_{\min}=-13.6\ \mathrm{eV}'),
    ])
    s.move('Two more payoffs you will use', [
        ('p', 'A particle in a small box keeps a minimum energy even at zero temperature — why helium stays liquid and nucleons stay energetic. And a state living only τ seconds has an energy width ℏ/τ, the natural width of every spectral line.'),
        ('m', r'K_{\min}\approx\frac{\hbar^2}{2mL^2},\qquad \Delta E\sim\frac{\hbar}{\tau}'),
    ])
    s.chip('key', 'the three uses', [('m', r'\Delta x\Delta p\gtrsim\hbar/2'), ('m', r'E(r)=\hbar^2/2mr^2-ke^2/r'),
                                     ('p', 'Confinement, zero-point energy, natural linewidth.')])
    s.chip('insight', 'why it is exact here', [('p', 'For the hydrogen ground state the estimate saturates the bound, so it returns a₀ and −13.6 eV exactly. Do not expect that for every state.')])
    s.chip('trap', 'the missing half', [('p', 'Writing ΔxΔp ≥ ℏ, or L = nh. The bound is ℏ/2 and L = nℏ.')])
    s.figure('uncertainty_well')
    S.append(s)

    return S
