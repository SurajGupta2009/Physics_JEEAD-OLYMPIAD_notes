"""Part II content: Olympiad / extension layer of modern physics.

X-rays and the photon's momentum take the first half; the second half is the
places where the quantum picture had to replace a classical one, derived rather
than asserted. Sources: x-rays/, atomic-structure/, photoelectric-effect/.
"""
from layout import Sheet

K = 'MODERN PHYSICS  /  PART II: OLYMPIAD + EXTENSIONS'


def build(total):
    S = []

    # ============================================================ X-RAY 1
    s = Sheet('Olympiad-01-xray-continuous', 'How does a tube voltage become a shortest wavelength?',
              'One electron, one photon, and a sharp edge that measures h/e.',
              K, 1, total, 'source: X-rays.md  §3.1-3.2, E1-E2, OL5',
              'λ_min = hc/eV: the edge depends on voltage alone, never on the target',
              scale=5e4)
    s.move('Making X-rays is thermionic emission plus a cliff', [
        ('p', 'A filament boils electrons off; tens of kilovolts accelerate them into a heavy target; they brake in the nuclear field and radiate. Only about one per cent of the electron power becomes X-rays — the rest heats the anode, which is why the anode rotates.'),
        ('m', r'\eta\approx10^{-9}ZV:\quad \mathrm{W},\ 100\ \mathrm{kV}\ \Rightarrow\ 0.7\ \%'),
        ('n', 'a 700 W dental tube radiates a few watts and must dump the other 695 W'),
    ])
    s.move('The cutoff is an energy statement', [
        ('p', 'A braking electron may shed any fraction of its energy, so the spectrum is continuous. But no photon can carry more than the whole electron energy, and that bound is reached when one electron gives everything in one collision.'),
        ('m', r'hf_{\max}=eV\ \Rightarrow\ \lambda_{\min}=\frac{hc}{eV}=\frac{1.24\times10^6}{V\ [\mathrm{V}]}\ \mathrm{pm}'),
        ('n', '30 kV → 41.3 pm; 50 kV → 24.8 pm; 100 kV → 12.4 pm'),
    ])
    s.move('Why the edge is sharp and the tail is soft', [
        ('p', 'The short-wavelength edge is a kinematic extreme: nothing can be shorter, so the distribution starts abruptly there. The long-wavelength side fades because soft photons are reabsorbed in the target and the window before they escape.'),
        ('n', 'changing the target changes brightness roughly as Z, never the edge'),
    ])
    s.chip('key', 'the tube in three lines', [('m', r'\lambda_{\min}=hc/eV'), ('m', r'\eta\approx10^{-9}ZV'),
                                              ('p', 'edge from V, height from Z and mA')])
    s.chip('trap', 'two confusions', [('p', 'Applying λ_min to a characteristic line — it bounds only the continuous spectrum.'),
                                      ('p', 'Thinking higher Z shifts the edge. It raises the hump.')])
    s.chip('num', 'tube bench', [('p', '1.24×10⁶ pm·V rule'), ('p', 'tungsten Z = 74, melting point 3422 °C'), ('p', '1 % efficiency at 100 kV')])
    s.figure('xray_continuous')
    S.append(s)

    # ============================================================ X-RAY 2
    s = Sheet('Olympiad-02-xray-characteristic', 'When do the sharp lines appear?',
              'A spectrum has two parts with two different masters: voltage and the atom.',
              K, 2, total, 'source: §3.3-3.4, E3-E4',
              'the hump is bremsstrahlung; the spikes need a vacancy, so they need a threshold voltage',
              scale=8e3)
    s.move('Two mechanisms in one spectrum', [
        ('p', 'Braking radiation gives the continuous hump, cut off at hc/eV. Separately a fast electron can eject an inner one; the vacancy refills from above and the photon carries a level difference — a sharp, element-specific line.'),
        ('m', r'E_{K\alpha}=E_L-E_K,\qquad E_{K\beta}=E_M-E_K'),
        ('n', 'the lines sit where the atom says; the hump sits where the voltage says'),
    ])
    s.move('The threshold logic examiners test', [
        ('p', 'A K line needs a K vacancy, and making one costs at least the K binding energy. Below that voltage the lines are absent however large the current; above it they appear and grow.'),
        ('m', r'V_{\mathrm{th}}=\frac{E_K}{e}:\quad \mathrm{Cu}\ 9\ \mathrm{kV},\ \mathrm{Mo}\ 20\ \mathrm{kV},\ \mathrm{W}\ 70\ \mathrm{kV}'),
        ('n', 'no lines means below threshold, not a failed tube'),
    ])
    s.move('Screened hydrogen, and Moseley', [
        ('p', 'The falling L electron sees a nucleus of charge Z screened by the one remaining K electron, so the transition is hydrogenic arithmetic with (Z − 1) for Z. The square root linearises it: a straight line in Z — how Moseley ordered the elements.'),
        ('m', r'E_{K\alpha}=\frac{3}{4}(13.6)(Z-1)^2\ \mathrm{eV},\qquad \sqrt{f}=\sqrt{\frac{3}{4}cR}\,(Z-1)'),
        ('n', 'copper: 8.0 keV predicted, 155 pm against a measured 154 pm'),
    ])
    s.chip('key', 'line and threshold', [('m', r'E_{K\alpha}=\frac{3}{4}(13.6)(Z-1)^2'), ('m', r'\sqrt{f}\propto(Z-1)'),
                                         ('p', 'V_th = E_K/e; below it, no lines')])
    s.chip('gate', 'what the shielded form assumes', [('p', 'One K electron left, so it works for K lines of heavy atoms.'), ('p', 'L lines need b ≈ 7.4, so the constant is line-specific.')])
    s.chip('trap', 'the two masters', [('p', 'Raising current brightens both parts; raising voltage moves the edge and can switch lines on. Neither moves a line’s wavelength.')])
    s.figure('xray_characteristic')
    S.append(s)

    # ============================================================ X-RAY 3
    s = Sheet('Olympiad-03-absorption', 'Why does a radiograph show bone and not skin?',
              'Attenuation is exponential, and the exponent is roughly Z cubed.',
              K, 3, total, 'source: §3.5, E5, OL8',
              'I = I₀e^{−μx}: contrast comes from μ, and μ is a steep function of Z and E',
              scale=1e5)
    s.move('A fixed fraction per layer', [
        ('p', 'Every additional slice of material removes the same fraction of what is left, because it presents the same number of absorbers. That sentence is the differential equation, and its solution is the exponential.'),
        ('m', r'I=I_0e^{-\mu x},\qquad x_{1/2}=\frac{\ln2}{\mu}'),
        ('n', 'lead at 100 keV: x½ = 0.12 mm, so μ = 58 cm⁻¹'),
    ])
    s.move('Why bone casts a shadow', [
        ('p', 'Photoelectric absorption scales roughly as Z³–Z⁴ and falls with photon energy. Calcium (Z = 20) against carbon and oxygen (Z = 6, 8) is therefore a contrast of order twenty in μ, which the film records as a shadow. Barium and iodine meals exploit the same appetite.'),
        ('n', 'soft X-rays give better contrast and more dose: one curve read two ways'),
    ])
    s.move('The engineering trade', [
        ('p', 'The same μ that creates contrast also deposits energy, and the energy deposited per unit mass is the dose. Thicker patients need harder beams, harder beams give less contrast, and the compromise is what a radiology protocol is. Computed tomography is this law inverted numerically over many projections.'),
        ('m', r'\mathrm{dose}\propto\int\mu\,\Phi\,dt'),
    ])
    s.chip('key', 'the law', [('m', r'I=I_0e^{-\mu x}'), ('m', r'x_{1/2}=\ln2/\mu'),
                               ('p', 'μ rises as Z³–Z⁴, falls with E')])
    s.chip('gate', 'narrow beam only', [('p', 'μ is measured with a narrow beam and a narrow detector. A broad beam collects scattered photons and needs a build-up factor.')])
    s.chip('num', 'half-value layers', [('p', 'Pb 0.12 mm at 100 keV'), ('p', 'Al a few mm at 50 keV'), ('p', 'tissue ~ cm at 50 keV')])
    s.figure('absorption_curve')
    S.append(s)

    # ============================================================ X-RAY 4
    s = Sheet('Olympiad-04-bragg', 'How do you measure an atom with a wavelength?',
              'Bragg’s law turns angles into spacings — and spacings into Avogadro’s number.',
              K, 4, total, 'source: §3.6-3.8, E6-E8, OL12',
              '2d sinθ = nλ with θ from the plane: an angle, a wavelength, and a lattice constant',
              scale=8e3)
    s.move('Only a crystal is fine enough', [
        ('p', 'A grating resolves structure of order its own spacing. Visible light (500 nm) sees atomic planes (0.3 nm) as a smooth surface — the ratio is 10³ too coarse for any Bragg angle. X-rays at 100 pm match the spacing, so the crystal becomes the grating.'),
        ('n', 'Laue’s 1912 spots proved both that X-rays are waves and that crystals are lattices'),
    ])
    s.move('The path difference, with the angle made foolproof', [
        ('p', 'Two rays strike successive planes at glancing angle θ. The lower one travels an extra d sinθ going in and the same coming out. Constructive interference needs that total to be a whole number of wavelengths.'),
        ('m', r'2d\sin\theta=n\lambda,\qquad n\le\frac{2d}{\lambda}'),
        ('n', 'θ is measured from the plane; the detector sits at 2θ from the beam'),
    ])
    s.move('From a spacing to Avogadro', [
        ('p', 'In rock salt the cubic cell alternates ions, so each ion pair owns a volume 2d³ where d is the neighbouring-ion spacing. A balance gives the same volume as M/ρN_A, and equating them yields Avogadro’s number from a wavelength and an angle.'),
        ('m', r'N_A=\frac{M}{2\rho d^3}=\frac{0.05844}{2(2165)(2.82\times10^{-10})^3}'),
        ('m', r'=6.02\times10^{23}\ \mathrm{mol^{-1}}'),
        ('n', 'the missing reflections are structure-factor information, not experimental error'),
    ])
    s.chip('key', 'the law and its use', [('m', r'2d\sin\theta=n\lambda'), ('m', r'd=\frac{n\lambda}{2\sin\theta}'),
                                          ('m', r'N_A=M/2\rho d^3')])
    s.chip('trap', 'the convention', [('p', 'θ from the plane, so the path difference is 2d sinθ. Writing 2d cosθ is the single most common error in this topic.'), ('p', 'And the detector angle is 2θ.')])
    s.chip('num', 'NaCl bench', [('p', 'd = 282 pm, a = 564 pm'), ('p', 'ρ = 2165 kg/m³, M = 58.44 g/mol')])
    s.figure('bragg_geometry')
    S.append(s)

    # ============================================================ X-RAY 5
    s = Sheet('Olympiad-05-compton', 'What happens when a photon hits an electron?',
              'Billiards with light: the shift is absolute, angle-only, and independent of everything else.',
              K, 5, total, 'source: §3.9-3.11, E9-E12',
              'Δλ = 2.426(1 − cosθ) pm: an absolute shift, never a percentage',
              scale=1e5)
    s.move('The experiment that classical physics cannot survive', [
        ('p', 'Compton scattered 100 pm X-rays off graphite and found two peaks at every angle: one at the original wavelength, one shifted by an amount that grows with angle and depends on nothing else. Classical electrodynamics predicts a single unshifted line at every angle.'),
        ('n', 'the unshifted peak is whole-atom recoil off tightly bound electrons — not an error'),
    ])
    s.move('Conservation closes the triangle', [
        ('p', 'Write energy and both momentum components, eliminate the electron angle, and use the relativistic energy-momentum relation. What falls out is a shift that depends only on the scattering angle and one constant with the dimensions of length.'),
        ('m', r'\Delta\lambda=\frac{h}{m_ec}(1-\cos\theta)=2.426(1-\cos\theta)\ \mathrm{pm}'),
        ('n', '0° → 0; 90° → 2.43 pm; 180° → 4.86 pm, the maximum'),
    ])
    s.move('The electron takes the rest', [
        ('p', 'Whatever the photon loses, the electron gains as kinetic energy. Writing x = hf/m_ec², the recoil energy has a clean closed form, and the electron always goes forward of the perpendicular — it can never come back.'),
        ('m', r'K_e=hf\frac{x(1-\cos\theta)}{1+x(1-\cos\theta)},\qquad \tan\phi=\frac{1}{(1+x)\tan(\theta/2)}'),
    ])
    s.chip('key', 'the shift', [('m', r'\Delta\lambda=\frac{h}{m_ec}(1-\cos\theta)'), ('p', 'λ_C = 2.426 pm, a fundamental length'), ('p', 'Absolute shift; the fraction varies with λ.')])
    s.chip('trap', 'three misreadings', [('p', 'Treating Δλ as a percentage of λ.'), ('p', 'Explaining the unshifted peak as failure of the model.'), ('p', 'Using p = E/c for the recoil electron.')])
    s.chip('num', 'the scale', [('p', 'visible light: shift 10⁻⁵ of λ — invisible'), ('p', '100 keV: shift is 2 % of λ'), ('p', '1 MeV: shift is 30 % of λ')])
    s.figure('compton_kinematics')
    S.append(s)

    # ============================================================ X-RAY 6
    s = Sheet('Olympiad-06-compton-invariant', 'Can the Compton shift be derived without trigonometry?',
              'Yes — square the four-momentum of the electron and the algebra collapses.',
              K, 6, total, 'source: OL2 (invariant route)',
              'one invariant replaces three conservation equations and two eliminands',
              scale=1e5)
    s.move('Four-vectors make conservation linear', [
        ('p', 'Energy and the three momentum components are one object. Conservation of four-momentum is then a single vector equation: the incoming photon equals the outgoing photon plus the recoil electron.'),
        ('m', r'p_\gamma=p_\gamma^{\prime}+p_e\ \Rightarrow\ p_e=p_\gamma-p_\gamma^{\prime}'),
    ])
    s.move('Square it and use the mass shell', [
        ('p', 'The electron’s four-momentum squared is m_e²c², a number every frame agrees on. The photon’s is zero. Expanding the square leaves only the dot product of the two photon momenta, which in the lab frame is a product of energies and a cosine.'),
        ('m', r'(p_\gamma-p_\gamma^{\prime})^2=m_e^2c^2\ \Rightarrow\ 2p_\gamma\!\cdot p_\gamma^{\prime}=2m_e^2c^2'),
        ('m', r'\frac{1}{\lambda^{\prime}}-\frac{1}{\lambda}=\frac{1-\cos\theta}{\lambda_C}'),
        ('n', 'two lines of algebra, no recoil angle, no trigonometric identities'),
    ])
    s.move('Why this route is worth learning', [
        ('p', 'The scalar derivation needs three conservation equations and one elimination. The invariant route needs one equation. When a problem has several bodies and several angles, squaring a four-momentum difference is almost always the shortest path — and it generalises to pair production and to any two-body decay.'),
        ('n', 'same answer, but the method scales where the trigonometry does not'),
    ])
    s.chip('key', 'the invariant', [('m', r'p_e=p_\gamma-p_\gamma^{\prime}'), ('m', r'p^2=m^2c^2'),
                                    ('p', 'Square first, ask questions later.')])
    s.chip('insight', 'why thresholds are higher', [('p', 'In a fixed-target collision the products must carry the target’s momentum, so the centre-of-mass energy is √s, not the beam energy plus the target mass.')])
    s.chip('trap', 'mixing frames', [('p', 'The dot product p·p′ must be evaluated in one frame. Using the lab energies but a centre-of-mass angle is the standard error.')])
    s.figure('compton_invariant')
    S.append(s)

    # ============================================================ X-RAY 7
    s = Sheet('Olympiad-07-inverse-compton', 'How does a fast electron brighten a dull photon?',
              'The Compton event run backwards, and the reason radio galaxies shine in X-rays.',
              K, 7, total, 'source: §3.11, OL4',
              'a photon bouncing off a relativistic electron gains of order γ² in energy',
              scale=1e3)
    s.move('Run the collision backwards', [
        ('p', 'In Compton scattering a photon hands energy to an electron. If the electron is already moving fast and the photon meets it head-on, the photon gains energy instead. In the electron’s frame this is ordinary Compton scattering; transform back and the photon is boosted.'),
        ('m', r'\epsilon^{\prime}\approx\gamma^2\epsilon\quad(\gamma\epsilon\ll m_ec^2)'),
        ('n', 'a radio photon at γ = 1000 becomes a keV photon: radio galaxies glow in X-rays'),
    ])
    s.move('The moving-mirror picture', [
        ('p', 'Treat the electron as a mirror approaching the light. One Doppler shift takes the photon into the electron frame, a second takes it back out. Two shifts of order γ give the square.'),
        ('m', r'\frac{\epsilon^{\prime}}{\epsilon}=\frac{1+\beta}{1-\beta}\approx4\gamma^2\ \ (\beta\to1)'),
        ('n', 'the same factor 4γ² that appears in synchrotron and in the Doppler beaming of jets'),
    ])
    s.move('Where it matters, and where it stops', [
        ('p', 'Inverse Compton sets the X-ray output of jets, of the cosmic microwave background seen by hot cluster gas, and of any source with relativistic electrons and a soft photon bath. Once γε approaches m_ec² the process enters the Klein-Nishina regime and the cross-section falls — that is where the simple boost stops.'),
        ('n', 'the Sunyaev-Zel’dovich effect is this process on the microwave background'),
    ])
    s.chip('key', 'the boost', [('m', r"\epsilon'\approx\gamma^2\epsilon"), ('m', r'\propto4\gamma^2\ \mathrm{at}\ \beta\to1'),
                                ('p', 'two Doppler shifts, not one')])
    s.chip('gate', 'when it fails', [('p', 'γε ≳ m_ec²: recoil matters, the cross-section drops (Klein-Nishina).'), ('p', 'Also assumes an isotropic soft photon bath in the electron frame.')])
    s.chip('trap', 'one shift only', [('p', 'Using 2γ instead of 4γ². The photon is boosted twice: in and out.')])
    s.figure('inverse_compton')
    S.append(s)

    # ============================================================ X-RAY 8
    s = Sheet('Olympiad-08-pair-production', 'When does a photon stop being a photon?',
              'Above 1.022 MeV it can become matter — but never in empty space.',
              K, 8, total, 'source: §3.11, E12; X-rays.md synthesis table',
              'E > 2m_ec² and a third body: energy alone is not enough, momentum must balance',
              scale=1.022e6)
    s.move('The threshold is a rest-mass statement', [
        ('p', 'Creating an electron-positron pair costs 2m_ec² = 1.022 MeV of rest energy before any kinetic energy. A photon below that energy cannot do it, whatever the material.'),
        ('m', r'E_{\min}=2m_ec^2=1.022\ \mathrm{MeV},\qquad K_{\mathrm{pair}}=E_\gamma-1.022\ \mathrm{MeV}'),
        ('n', 'a 2 MeV photon leaves 0.98 MeV to share between the two particles'),
    ])
    s.move('Why empty space is forbidden', [
        ('p', 'In free space, energy and momentum cannot both be conserved by one photon splitting into two equal-mass particles: in the centre-of-mass frame the photon has momentum but the pair would have none. A nucleus (or an electron) must take the recoil.'),
        ('m', r'p_\gamma\neq p_++p_-\ \mathrm{in\ any\ frame\ with}\ E_\gamma=2m_ec^2'),
        ('n', 'the same reason a single photon cannot produce a single electron'),
    ])
    s.move('The three experiments that complete the photon', [
        ('p', 'Photoelectric effect proves the energy comes in quanta. Diffraction proves the wave. Compton proves the momentum. Pair production closes the circle: at high enough energy the quantum can be converted into the very particles whose mass it never had.'),
        ('n', 'in a bubble chamber a photon leaves no track until it converts — then two curly ones appear'),
    ])
    s.chip('key', 'the threshold', [('m', r'2m_ec^2=1.022\ \mathrm{MeV}'), ('m', r'K=E_\gamma-1.022'),
                                    ('p', 'needs a third body for momentum')])
    s.chip('trap', 'free-space conversion', [('p', 'Allowing γ → e⁺e⁻ with nothing else present. Momentum conservation forbids it in every frame.')])
    s.chip('insight', 'the photon, completed', [('p', 'Energy quantum (photoelectric), wave (diffraction), momentum (Compton), convertibility (pair production). Four experiments, one object.')])
    s.figure('pair_threshold')
    S.append(s)

    # ============================================================ X-RAY 9
    s = Sheet('Olympiad-09-moseley', 'How did a straight line predict missing elements?',
              'Moseley plotted √f against Z in 1913 and the periodic table became a measurement.',
              K, 9, total, 'source: §3.4, OL6; Atomic-structure.md §3.9',
              '√f ∝ (Z − b): every element is a point on one line, and gaps mean missing elements',
              scale=8e3)
    s.move('Why the line is straight', [
        ('p', 'Kα is a 2 → 1 transition in a nucleus screened by the one remaining K electron. The energy carries (Z − 1)², so the frequency carries it too, and its square root is linear in Z.'),
        ('m', r'f=\frac{3}{4}cR(Z-1)^2\ \Rightarrow\ \sqrt{f}=\sqrt{\frac{3}{4}cR}\,(Z-1)'),
        ('n', 'slope √(3cR/4) = 4.97×10⁷ (Hz)^{1/2} per unit Z'),
    ])
    s.move('What the intercept tells you', [
        ('p', 'The straight line does not pass through the origin: it hits √f = 0 at Z = 1, not Z = 0. That offset is the shielding constant, and the same trick with L lines gives b ≈ 7.4 because more electrons screen.'),
        ('m', r'b_{K\alpha}\approx1,\qquad b_{L\alpha}\approx7.4'),
        ('n', 'Moseley’s “a and b” are exactly the slope and the shield'),
    ])
    s.move('The prediction that found four elements', [
        ('p', 'Because the line is monotonic and every element must sit on it, a gap in the sequence is a missing element rather than a gap in nature. Elements 43, 61, 72 and 75 were identified this way before they were isolated — technetium, promethium, hafnium, rhenium.'),
        ('n', 'it also settled the ordering: Z, not atomic weight, is the periodic variable'),
    ])
    s.chip('key', 'Moseley', [('m', r'\sqrt{f}=a(Z-b)'), ('p', 'Kα: b ≈ 1; Lα: b ≈ 7.4'), ('p', 'Z is the ordering variable, not mass.')])
    s.chip('insight', 'what it changed', [('p', 'Before 1913 the periodic table was a chemical pattern with guessed gaps. After it, the gaps were places with a known X-ray address.')])
    s.chip('trap', 'one line, one constant', [('p', 'Using a Kα value of b for an L line, or treating b as universal.')])
    s.figure('moseley_line')
    S.append(s)

    # ============================================================ ATOMIC EXT
    s = Sheet('Olympiad-10-collapse', 'How long would a classical atom live?',
              'Sixteen picoseconds, and a continuous spectrum while it dies. That is the crisis.',
              K, 10, total, 'source: Atomic-structure.md §3.3, OL3',
              'τ ∝ r³: the collapse is a slow spiral, not a plunge, and it radiates every frequency',
              scale=13.6)
    s.move('An accelerating charge radiates', [
        ('p', 'Larmor’s formula gives the power radiated by an accelerating charge. For an electron in a circular orbit the acceleration is v²/r, so the power climbs steeply as the orbit shrinks — which makes the collapse accelerate as it proceeds.'),
        ('m', r'P=\frac{e^2a^2}{6\pi\varepsilon_0c^3},\qquad a=\frac{ke^2}{m_er^2}'),
    ])
    s.move('Integrate the energy loss', [
        ('p', 'The orbital energy is −ke²/2r, so losing energy means losing radius. Substituting gives a separable equation whose integral is a lifetime proportional to the cube of the starting radius.'),
        ('m', r'\frac{dE}{dt}=-P\ \Rightarrow\ r^2\dot r=-\frac{2C}{ke^2}\ \Rightarrow\ \tau=\frac{ke^2r_0^3}{6C}'),
        ('m', r'\tau(a_0)=1.6\times10^{-11}\ \mathrm{s}'),
        ('n', 'τc ≈ 5 mm: a slow spiral of ten million orbits, not a plunge'),
    ])
    s.move('Two predictions that both fail', [
        ('p', 'The atom should live 16 ps, and while dying its orbital frequency should sweep continuously upward, emitting a continuum from infrared to X-rays. Real atoms live forever and emit sharp lines. Both failures are fixed by the same assumption: stationary states.'),
        ('n', 'the stability and the line spectrum are one problem, not two'),
    ])
    s.chip('key', 'the collapse', [('m', r'P=e^2a^2/6\pi\varepsilon_0c^3'), ('m', r'\tau=ke^2r_0^3/6C'),
                                   ('p', '16 ps from a₀; a continuum, not lines')])
    s.chip('insight', 'why it is a spiral', [('p', 'τc ≈ 5 mm is five orders larger than the atom, so the electron completes ~10⁷ orbits while dying. The “instant collapse” story is wrong in scale.')])
    s.chip('trap', 'the wrong lifetime', [('p', 'Quoting 10⁻⁸ s — that is an excited-state lifetime, not the classical collapse. The collapse is 10⁻¹¹ s.')])
    s.figure('collapse_spiral')
    S.append(s)

    # ============================================================ ATOMIC EXT 2
    s = Sheet('Olympiad-11-correspondence', 'Why does quantum mechanics become classical for large n?',
              'Expand the level spacing and the photon frequency turns into the orbital frequency.',
              K, 11, total, 'source: §3.10, OL4',
              'for large n the gap closes as 1/n, and the photon frequency equals the orbit frequency to 1.5 %',
              scale=13.6)
    s.move('A large orbit is a classical antenna', [
        ('p', 'An electron on a big orbit radiates at its orbital frequency. Quantum mechanics says it radiates at the energy gap divided by h. For the two to agree, the gap must approach the orbital energy spacing — which is what a Taylor expansion shows.'),
        ('m', r'\Delta E=\frac{A}{n^2}\left[(1-1/n)^{-2}-1\right]\approx\frac{2A}{n^3}\left(1+\frac{3}{2n}\right)'),
        ('m', r'f_{\mathrm{photon}}=f_{\mathrm{orbit}}\left(1+\frac{3}{2n}\right)'),
    ])
    s.move('Check the numbers at n = 100', [
        ('p', 'The correction is 1.5 %. At n = 10 it is 15 %, and the quantum world is visibly non-classical. The ratio approaches one from above, monotonically, and the limit is the statement that quantum mechanics contains classical mechanics.'),
        ('m', r'n=100:\ f_{\mathrm{orb}}=6.58\times10^9\ \mathrm{Hz},\ f_{\mathrm{ph}}=6.68\times10^9\ \mathrm{Hz}'),
        ('n', 'Rydberg atoms at n ~ 100 are used as sensors precisely because they are almost classical'),
    ])
    s.move('Why this is more than a curiosity', [
        ('p', 'Correspondence is the consistency condition any new theory must satisfy: reduce to the old one where it works. Bohr used it to guess selection rules before the full theory existed.'),
    ])
    s.chip('key', 'the limit', [('m', r'\Delta E/h=f_{\mathrm{orb}}(1+3/2n)'), ('p', 'Correction falls as 1/n'), ('p', 'Consistency condition, not a coincidence')])
    s.chip('gate', 'what it does not say', [('p', 'It does not say the classical trajectory is recovered for every state — only for coherent, large-n ones.')])
    s.chip('num', 'bench', [('p', 'n = 10: 15 % · n = 100: 1.5 % · n = 150: 1 %')])
    s.figure('correspondence_plot')
    S.append(s)

    # ============================================================ ATOMIC EXT 3
    s = Sheet('Olympiad-12-exotic-atoms', 'What if the electron weighed 207 times more?',
              'Muonic hydrogen is a nuclear ruler; positronium is a hydrogen twice as big.',
              K, 12, total, 'source: §3.8, OL5; Nuclear-physics.md preview',
              'every mass-dependent result takes μ: 207 times heavier, 207 times smaller',
              scale=2.8e3)
    s.move('The substitution is the whole physics', [
        ('p', 'The two-body problem reduces to one body of reduced mass μ orbiting a fixed centre. Every result of the Bohr derivation then goes through unchanged with m_e replaced by μ, so the radius scales as 1/μ and the binding as μ.'),
        ('m', r'\mu=\frac{m_1m_2}{m_1+m_2},\qquad a\propto\frac{1}{\mu},\qquad E\propto\mu'),
    ])
    s.move('Muonic hydrogen: an atom the size of a nucleus', [
        ('p', 'A muon is 207 times the electron mass, so the ground orbit is 256 fm — inside the nuclear charge distribution of a proton. The levels therefore shift by a measurable fraction, and comparing them with the point-nucleus prediction measures the proton radius.'),
        ('m', r'a_\mu=\frac{0.529\ \mathrm{\AA}}{207}=256\ \mathrm{fm},\qquad E_1=-2.81\ \mathrm{keV}'),
        ('n', 'this is the “proton radius puzzle”: muonic and electronic measurements disagreed for a decade'),
    ])
    s.move('Positronium: half the mass, twice the size', [
        ('p', 'Two equal masses give μ = m/2, so the “atom” is twice as big and half as bound, and every wavelength doubles. It also annihilates — the ground state lives 125 ps — which makes it a laboratory for QED rather than for chemistry.'),
        ('m', r'a=1.06\ \mathrm{\AA},\qquad E_1=-6.8\ \mathrm{eV},\qquad \lambda_{2\to1}=243\ \mathrm{nm}'),
    ])
    s.chip('key', 'exotic scaling', [('m', r'\mu=m_1m_2/(m_1+m_2)'), ('m', r'a\propto1/\mu,\ E\propto\mu'),
                                     ('p', 'E·a is invariant.')])
    s.chip('insight', 'why muonic atoms measure radii', [('p', 'The wavefunction overlaps the nucleus, so the level depends on the charge distribution rather than on a point charge.')])
    s.chip('trap', 'using m_e', [('p', 'Computing muonic hydrogen with the electron mass gives an answer wrong by 207 — and the proton-radius claim wrong by 207 too.')])
    s.figure('exotic_atoms')
    S.append(s)

    # ============================================================ ATOMIC EXT 4
    s = Sheet('Olympiad-13-franck-hertz', 'Can you see energy levels without looking at light?',
              'Yes: fire electrons at atoms and watch the current develop teeth.',
              K, 13, total, 'source: Photoelectric-effect.md §3.5; Atomic-structure.md §3.7',
              'a dip every 4.9 V in mercury is a level diagram measured with an ammeter',
              scale=4.9)
    s.move('The experiment in one sentence', [
        ('p', 'Electrons accelerate through mercury vapour toward a grid. If the vapour had no internal structure they would gain energy continuously and the current would rise smoothly. Instead it dips periodically: at certain energies an electron can hand 4.9 eV to an atom and keep only the remainder, so it no longer has enough to reach the collector.'),
        ('n', 'elastic collisions dominate below 4.9 eV; inelastic ones switch on exactly at it'),
    ])
    s.move('Why the dips repeat', [
        ('p', 'After an inelastic collision the electron restarts from near rest. It therefore needs another 4.9 eV of free path before it can excite again, so the collector current dips at every multiple of the threshold voltage.'),
        ('m', r'V_{\mathrm{dip}}=n\,(4.9\ \mathrm{V}),\qquad n=1,2,3'),
        ('n', 'the spacing, not the position, is the measurement: it is insensitive to contact potentials'),
    ])
    s.move('What it proves that spectroscopy does not', [
        ('p', 'Optical spectroscopy sees the photons that come out; Franck-Hertz sees the energy that goes in. Together they close the book: the levels are real, they are discrete, and they are the same levels whether you excite them with electrons or with light. It also shows that excitation costs a quantum, not a continuous trickle.'),
        ('n', 'the mercury atom then emits 254 nm ultraviolet as it de-excites — the same 4.9 eV'),
    ])
    s.chip('key', 'the measurement', [('m', r'\Delta V=4.9\ \mathrm{V}\ (\mathrm{Hg})'), ('p', 'dips at nΔV'), ('p', 'inelastic threshold = level spacing')])
    s.chip('gate', 'why the vapour pressure matters', [('p', 'Too little vapour and the electrons never collide; too much and they scatter many times before the grid. The window is narrow, which is why the original experiment was delicate.')])
    s.chip('trap', 'reading the first dip', [('p', 'The first dip is shifted by the contact potential difference between the electrodes. Only the spacing is reliable.')])
    s.figure('franck_hertz')
    S.append(s)

    # ============================================================ PHOTON EXT
    s = Sheet('Olympiad-14-waiting-time', 'How long should a wave take to eject an electron?',
              'Give classical physics its best case, then compare with the clock.',
              K, 14, total, 'source: Photoelectric-effect.md §3.3, E8; OL1',
              'hours at moonlight intensity versus nanoseconds observed: thirteen orders of magnitude',
              scale=2.0)
    s.move('Give the wave picture every advantage', [
        ('p', 'Assume the light is spread evenly, that an atom absorbs perfectly over its own cross-section, and that nothing is lost. Then the time to accumulate the escape energy is the energy needed divided by the power intercepted.'),
        ('m', r't=\frac{\phi}{IA}=\frac{3.2\times10^{-19}}{(10^{-3})(10^{-20})}=3.2\times10^{4}\ \mathrm{s}'),
        ('n', 'about nine hours at a milliwatt per square metre — and a century at 10⁻⁸ W/m²'),
    ])
    s.move('The clock says otherwise', [
        ('p', 'The measured delay between switching on the light and the first electrons is below a nanosecond at every intensity tested, including beams so dim that the wave estimate runs to hours. No accumulation time exists.'),
        ('m', r't_{\mathrm{observed}}\lesssim10^{-9}\ \mathrm{s}\quad\mathrm{vs}\quad t_{\mathrm{wave}}\sim10^{4}\ \mathrm{s}'),
        ('n', 'the ratio is 10¹³; this is not a discrepancy of factors of two'),
    ])
    s.move('Why the argument is decisive rather than rhetorical', [
        ('p', 'The estimate is deliberately generous. Even if the atom’s cross-section were a hundred times larger the wait would be minutes, and even at sunlight intensity it would be milliseconds. Any single-photon process removes the difficulty: the energy arrives concentrated in one quantum, so there is nothing to accumulate.'),
        ('n', 'the only escape for the wave picture is a collective absorption mechanism, which nobody has ever observed'),
    ])
    s.chip('key', 'the comparison', [('m', r't=\phi/IA'), ('p', '10⁴ s predicted, 10⁻⁹ s observed'), ('p', 'one photon, one electron removes the problem')])
    s.chip('insight', 'why thresholds follow', [('p', 'If energy arrives in quanta, then a quantum smaller than the toll simply cannot pay it — however many arrive. That is the threshold, and it needs no extra assumption.')])
    s.chip('trap', 'intensity vs energy', [('p', 'Saying “more intense light has more energy per photon”. Intensity is photons per area per second; the energy per photon is fixed by frequency.')])
    s.figure('waiting_time')
    S.append(s)

    # ============================================================ PHOTON EXT 2
    s = Sheet('Olympiad-15-matter-wave-speeds', 'Which speed does a matter wave travel at?',
              'Two speeds, one particle, and a product that is always c².',
              K, 15, total, 'source: §3.9, OL2',
              'phase speed c²/v exceeds c harmlessly; group speed v carries everything',
              scale=5.11e5)
    s.move('Two velocities from one dispersion relation', [
        ('p', 'A wave has a phase velocity ω/k and a group velocity dω/dk. For a matter wave the first is the speed of the crests and the second the speed of the envelope — the packet that actually represents the particle.'),
        ('m', r'v_p=\frac{\omega}{k}=\frac{E}{p},\qquad v_g=\frac{d\omega}{dk}=\frac{dE}{dp}'),
    ])
    s.move('Substitute the relativistic dispersion relation', [
        ('p', 'With E² = p²c² + m²c⁴, differentiating gives dE/dp = pc²/E. Dividing E by p gives the reciprocal, so the two speeds multiply to c². The group velocity comes out exactly the particle speed.'),
        ('m', r'v_p=\frac{c^2}{v}>c,\qquad v_g=v,\qquad v_pv_g=c^2'),
        ('n', 'a single infinite sine carries no information, so v_p > c violates nothing'),
    ])
    s.move('Why this is not a loophole', [
        ('p', 'Signal speed is the speed of a change in the envelope, which is the group velocity. For a free particle that is v < c. For light in a plasma the phase velocity also exceeds c while the group velocity is below it — the same structure, and the same reason no message outruns light.'),
        ('n', 'a wave packet with sharp edges spreads; its front still moves at v_g'),
    ])
    s.chip('key', 'two speeds', [('m', r'v_p=E/p=c^2/v'), ('m', r'v_g=dE/dp=v'), ('m', r'v_pv_g=c^2')])
    s.chip('gate', 'when v_p > c is fine', [('p', 'Phase velocity is a property of a mathematical surface of constant phase, not of a physical object. No energy, no information.')])
    s.chip('trap', 'the photon limit', [('p', 'For m → 0 both speeds tend to c, and the distinction collapses. Do not carry the formula past that limit as if v_p were meaningful.')])
    s.figure('matter_wave_speeds')
    S.append(s)

    return S
