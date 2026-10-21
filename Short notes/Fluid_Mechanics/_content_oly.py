"""Part II content: Olympiad and beyond-syllabus extensions.

Same page grammar as Part I, but each page starts from a model the JEE version
does not have time to build, and ends with where that model fails.
"""
from layout import Sheet

K = 'FLUID MECHANICS  /  PART II: OLYMPIAD + EXTENSIONS'


def build(total):
    S = []

    # ---------------------------------------------------------------- 1
    s = Sheet('Olympiad-01-drain', 'Why does a tank empty in finite time but a capillary never does?',
              'Two drain laws with the same geometry. The exponent on h decides whether the clock ever stops.',
              K, 1, total, 'source: OL1, Q15, C10',
              'inertial drain ends at T; viscous drain has an infinite tail')
    s.move('Inertial drain: integrate sqrt(h)', [
        ('p', 'With a sharp orifice the outflow is a√(2gh). Separating −A dh/dt = a√(2gh) and integrating from H to 0 gives a finite time, because h^−1/2 is integrable at the origin.'),
        ('m', r'T=\frac{A}{a}\sqrt{\frac{2H}{g}},\qquad h(t)=H\left(1-\frac{t}{T}\right)^2', '(10.1)'),
        ('n', 'A/a = 100, H = 1.25 m: T = 50.5 s, and the tank is exactly empty at T'),
    ])
    s.move('Viscous drain: integrate 1/h', [
        ('p', 'Replace the hole by a long capillary. Poiseuille gives an outflow proportional to h, so the equation becomes dh/dt = −h/τ and the height decays exponentially. The last centimetre takes as long as the first 63 percent.'),
        ('m', r'h=He^{-t/\tau},\qquad \tau=\frac{8\eta L A}{\pi r^4\rho g}'),
    ])
    s.move('Where the descriptions cross', [
        ('p', 'Write the viscous outflow speed as kh and the inertial one as √(2gh). Equating them fixes the height at which neither dominates.'),
        ('m', r'h^*=\frac{2g}{k^2}=\frac{128\,\eta^2L^2}{\rho^2gr^4}'),
        ('n', 'glycerine, r = 0.5 mm, L = 0.2 m: h* = 1.2×10⁷ m — no bench column ever reaches it'),
    ])
    s.move('The honest regime check for water', [
        ('p', 'For water the same formula gives h* ≈ 5 m, but at those speeds a half-millimetre tube has Re of order 10³, so the true late regime is turbulent, not laminar. The clean inertial/laminar pair is a teaching model; say which pair you are using.'),
        ('n', 'C10: the exponent of h in the rate law decides whether the drain ever finishes'),
    ])
    s.chip('key', 'two clocks', [('m', r'T=\frac{A}{a}\sqrt{2H/g}'), ('m', r'h=He^{-t/\tau}'), ('m', r'h^*=128\eta^2L^2/\rho^2gr^4')])
    s.chip('gate', 'when each holds', [('p', 'Orifice: quasi-steady, a ≪ A, sharp edge.'), ('p', 'Capillary: laminar Poiseuille, Re ≲ 2000.'), ('p', 'Water in a fine tube often ends turbulent instead.')])
    s.chip('trap', 'overreach', [('p', 'Presenting the exponential as the true late behaviour of water.'), ('p', 'Forgetting the tank area A in τ.')])
    s.figure('drain_two_regimes')
    S.append(s)

    # ---------------------------------------------------------------- 2
    s = Sheet('Olympiad-02-paraboloid', 'Three ways to derive the rotating surface',
              'Newton, energy and Bernoulli give the same paraboloid. Agreement is the point, not the algebra.',
              K, 2, total, 'source: OL2, C9, §3.4',
              'one surface, three languages: force, potential, pressure integral')
    s.move('(a) Force balance on an element', [
        ('p', 'For a surface element of mass m, the normal force balances weight and the centrifugal pseudo-force. Dividing the horizontal equation by the vertical one gives the slope of the surface.'),
        ('m', r'\tan\alpha=\frac{dz}{dr}=\frac{\omega^2r}{g}'),
    ])
    s.move('(b) Equipotential argument', [
        ('p', 'In the rotating frame the effective potential per unit mass is Φ = gz − ½ω²r². A static fluid cannot sustain tangential stress, so ∇p is parallel to ∇Φ; on a free surface p is constant, hence Φ is constant.'),
        ('m', r'\Phi=gz-\frac{1}{2}\omega^2r^2=\text{const}'),
        ('n', 'this is the deep reason the force balance could be integrated at all'),
    ])
    s.move('(c) Bernoulli with a centrifugal head', [
        ('p', 'Integrate the pressure differential in the rotating frame between any two points. The result is the rotating-frame Bernoulli, and setting p = p₀ recovers the same surface.'),
        ('m', r'dp=\rho\omega^2r\,dr-\rho g\,dz\ \Rightarrow\ p-\frac{1}{2}\rho\omega^2r^2+\rho gz=\text{const}'),
    ])
    s.move('Numbers, and what volume conservation adds', [
        ('p', 'A bucket of radius 0.30 m spins at 4 s⁻¹. The rim-to-centre difference is 7.35 cm; since the paraboloid holds half the circumscribed cylinder, the centre drops 3.7 cm and the rim rises 3.7 cm relative to the rest level.'),
        ('m', r'\Delta z=\frac{\omega^2R^2}{2g}=0.0735\ \mathrm{m}'),
        ('n', 'C9: all three arguments survive linear acceleration, with −a replacing the centrifugal field'),
    ])
    s.chip('key', 'one result, three routes', [('m', r'z=z_0+\omega^2r^2/2g'), ('m', r'p-\frac{1}{2}\rho\omega^2r^2+\rho gz=\text{const}'), ('p', 'volume: centre drop = rim rise')])
    s.chip('trap', 'false shortcuts', [('p', 'Treating the centrifugal term as a real potential in the lab frame.'), ('p', 'Forgetting volume conservation when the vessel is closed.')])
    s.chip('check', 'limits', [('p', 'ω -> 0: flat surface.'), ('p', 'r -> 0: vertex at z₀.'), ('p', 'linear acceleration: planes, not paraboloids.')])
    s.figure('paraboloid_three_ways')
    S.append(s)

    # ---------------------------------------------------------------- 3
    s = Sheet('Olympiad-03-raindrop', 'Where does Stokes drag hand over to quadratic drag?',
              'One crossover radius decides whether a droplet drifts or a raindrop hits.',
              K, 3, total, 'source: OL3, E9, §3.13',
              'set Re = 1 with the Stokes speed: r* ≈ 40 µm, v* ≈ 0.19 m/s')
    s.move('Two terminal-velocity laws', [
        ('p', 'Balance the same net weight against two different drag laws. Stokes is linear in v; the quadratic law is proportional to v². Each gives a different scaling with radius.'),
        ('m', r'v_t=\frac{2r^2\rho_w g}{9\eta}\ \ (\text{Re}\lesssim1),\qquad v_t=\sqrt{\frac{8r\rho_w g}{3C_d\rho_a}}\ \ (\text{large Re})'),
    ])
    s.move('Find the crossover by making Stokes fail', [
        ('p', 'The Stokes answer destroys itself when Re reaches 1. Substitute the Stokes speed into Re = ρa v 2r/η and solve for the radius.'),
        ('m', r'r^{*3}=\frac{9\eta^2}{4\rho_a\rho_w g}\ \Rightarrow\ r^*\approx4\times10^{-5}\ \mathrm{m},\quad v^*\approx0.19\ \mathrm{m/s}'),
        ('n', 'at r* the two drag laws are both of order the same size, so neither is accurate'),
    ])
    s.move('A millimetre drop', [
        ('p', 'A 2 mm drop in the quadratic formula falls at about 9.9 m/s. Measured drops of that size fall at 6.5 to 9 m/s because they deform and wobble, raising the drag. State the deformation caveat.'),
        ('m', r'v_t=\sqrt{\frac{8(2\times10^{-3})(1000)(9.8)}{3(0.44)(1.2)}}\approx9.9\ \mathrm{m/s}'),
    ])
    s.move('What it means for weather', [
        ('p', 'Mist stays up for hours at centimetres per second; rain arrives at about 10 m/s. The vacuum estimate √(2gh) from a cloud at 2 km would give 200 m/s, which is why atmospheric viscosity is the only reason rain is weather rather than shrapnel.'),
        ('n', 'same physics, ten orders of magnitude in settling time'),
    ])
    s.chip('key', 'crossover', [('m', r'r^*=4\times10^{-5}\ \mathrm{m}'), ('m', r'v^*\approx0.19\ \mathrm{m/s}'), ('p', 'mist: r < r*; rain: r > r*')])
    s.chip('gate', 'what each law assumes', [('p', 'Stokes: rigid sphere, Re ≲ 1, no walls.'), ('p', 'Quadratic: fixed C_d, turbulent wake, no deformation.'), ('p', 'Real drops: deformation lowers the speed.')])
    s.chip('trap', 'one number', [('p', 'Quoting a Stokes speed for a raindrop: Re ≈ 16 says the answer is wrong by a factor of order two.')])
    s.figure('raindrop')
    S.append(s)

    # ---------------------------------------------------------------- 4
    s = Sheet('Olympiad-04-young-laplace', 'Young-Laplace from virtual work, and the film that refuses to exist',
              'A soap film between two rings has zero pressure difference, so it must have zero mean curvature. That is harder than it sounds.',
              K, 4, total, 'source: OL4, C11, §3.15',
              'equate pressure work to surface work; minimal surfaces have existence limits')
    s.move('Push a patch out by dn', [
        ('p', 'A small patch of area A with principal radii r₁ and r₂ is displaced along its normal by δn. Its area grows because each radius grows, and the swept volume is Aδn. At equilibrium the pressure work equals the surface work.'),
        ('m', r'\delta A=A\,\delta n\left(\frac{1}{r_1}+\frac{1}{r_2}\right),\qquad \Delta p\,\delta V=\gamma\,\delta A'),
        ('m', r'\Delta p=\gamma\left(\frac{1}{r_1}+\frac{1}{r_2}\right)', '(3.18)'),
    ])
    s.move('The film between two rings', [
        ('p', 'Both sides see the same air, so Δp = 0 and the mean curvature vanishes. The surface of revolution with zero mean curvature is a catenoid, a minimal surface.'),
        ('m', r'r(z)=r_{min}\cosh\left(\frac{z}{r_{min}}\right),\qquad r(\pm d/2)=R'),
    ])
    s.move('Existence has a limit', [
        ('p', 'A catenoid spanning rings of radius R exists only while d/R is below about 1.33. Beyond that the film snaps into two flat discs: a minimal surface, but not a stable one, and for larger separations not a solution at all.'),
        ('m', r'\frac{d}{R}\lesssim1.33'),
        ('n', 'C11: a saddle has equal and opposite curvatures, so Δp = 0 even though the film is curved'),
    ])
    s.move('Why this is more than a curiosity', [
        ('p', 'The same argument gives the shape of soap films on any wire, the pressure inside a Plateau border, and the reason foam coarsens. It is also the cleanest example of the difference between a stationary surface and a stable one.'),
    ])
    s.chip('key', 'curvature', [('m', r'\Delta p=\gamma(1/r_1+1/r_2)'), ('m', r'\Delta p\,\delta V=\gamma\,\delta A'), ('p', 'zero mean curvature: catenoid')])
    s.chip('trap', 'existence vs stability', [('p', 'Assuming a stationary surface is stable.'), ('p', 'Forgetting that a bubble has two surfaces while a film patch has two sides of one surface.')])
    s.chip('check', 'limits', [('p', 'sphere: r₁ = r₂ = r -> 2γ/r'), ('p', 'cylinder: r₂ -> ∞ -> γ/r'), ('p', 'plane: both infinite -> 0')])
    s.figure('young_laplace_patch')
    S.append(s)

    # ---------------------------------------------------------------- 5
    s = Sheet('Olympiad-05-drop-strider', 'Measuring gamma with a tap, and why no elephant walks on water',
              'Two kitchen-table experiments that expose the length-versus-volume scaling of surface forces.',
              K, 5, total, 'source: OL5, C12, §3.14',
              'support scales as L, weight as L³: small is a superpower')
    s.move('Tate\'s law and its correction', [
        ('p', 'A drop detaches when its weight equals the pull of the neck ring. A hundred drops of 3.1 g from a 1 mm tube give a naive value of 0.048 N/m, about two thirds of water\'s true value.'),
        ('m', r'\gamma_{naive}=\frac{mg}{2\pi r}=0.048\ \mathrm{N/m}'),
    ])
    s.move('Why the naive value is low', [
        ('p', 'Part of the neck never falls: it drains back onto the tip, so the fallen drop carries only a fraction f ≈ 0.66 of the ideal ring weight. Dividing by f recovers 0.073 N/m. The correction is not a fudge; it is the mass balance of the pinch-off.'),
        ('m', r'\gamma=\frac{\gamma_{naive}}{f}=\frac{0.048}{0.66}=0.073\ \mathrm{N/m}'),
    ])
    s.move('The water strider', [
        ('p', 'Each leg dents the surface; the tension acts along both contact edges, so the upward force is about 2γℓ. Six legs with 0.24 m of total contact support 3.6 g, against a body mass of 0.01 to 0.1 g.'),
        ('m', r'F\approx2\gamma\ell=2(0.0728)(0.24)=0.035\ \mathrm{N}'),
        ('n', 'C12: support is a line integral, weight is a volume; the ratio is L⁻²'),
    ])
    s.move('The scaling argument', [
        ('p', 'A hundredfold larger animal has a hundredfold longer contact line but a millionfold weight. Surface support becomes irrelevant at large L, which is why the trick belongs exclusively to small animals and thin films.'),
    ])
    s.chip('key', 'two measurements', [('m', r'\gamma_{naive}=mg/2\pi r'), ('m', r'\gamma=\gamma_{naive}/f'), ('m', r'F\approx2\gamma\ell')])
    s.chip('check', 'orders of magnitude', [('p', 'water strider: 0.035 N vs 10⁻⁴ N weight'), ('p', 'drop method: 0.073 N/m recovered'), ('p', 'correction f ≈ 0.66, not 1')])
    s.chip('trap', 'scaling', [('p', 'Scaling contact length with body length and forgetting that mass scales as volume.'), ('p', 'Using the tube radius instead of the neck radius in Tate\'s law.')])
    s.figure('drop_strider')
    S.append(s)

    # ---------------------------------------------------------------- 6
    s = Sheet('Olympiad-06-tree', 'How high can a tree suck water?',
              'Capillarity gives 6 m, suction gives 10 m, and redwoods are 100 m. The resolution is a different state of the liquid.',
              K, 6, total, 'source: OL6, §3.16, §3.10',
              'the 10 m limit is on suction with p ≥ 0; tension is a different regime')
    s.move('Capillary rise in a xylem vessel', [
        ('p', 'A vessel of radius 2.5 µm lifts water 5.9 m by surface tension alone. That is a tall tree already, but not a redwood.'),
        ('m', r'h=\frac{2\gamma}{\rho g r}=\frac{2(0.0728)}{(1000)(9.8)(2.5\times10^{-6})}=5.9\ \mathrm{m}'),
    ])
    s.move('The suction ceiling', [
        ('p', 'A pump at the top can at best reduce the pressure to zero. That limits a lift to the barometer height, about 10.3 m. This is the number that appears in every "why can\'t trees be tall" answer, and it is not the relevant limit.'),
        ('m', r'h_{max}=\frac{p_0}{\rho g}\approx10.3\ \mathrm{m}'),
    ])
    s.move('Tension: the missing state', [
        ('p', 'Transpiration pull puts the xylem water under tension, at negative gauge pressure of order 1 MPa. The hydrogen-bonded column hangs from the leaves like a rope, held by cohesion, rather than being pushed from below. Measured trees exceed 110 m.'),
        ('m', r'p_{top}\approx-1\ \mathrm{MPa}\ \Rightarrow\ h\approx100\ \mathrm{m}'),
        ('n', 'the true ceiling is cavitation: once a bubble nucleates, the column breaks'),
    ])
    s.move('Why the barometer argument does not apply', [
        ('p', 'The 10.3 m limit constrains a pressure difference with p ≥ 0 on the supply side. A metastable liquid under tension has p < 0, and the argument that produced 10.3 m simply does not describe that state.'),
        ('n', 'same equation, different branch of the physics'),
    ])
    s.chip('key', 'three ceilings', [('p', 'capillary: 5.9 m at 2.5 µm'), ('p', 'suction: 10.3 m'), ('p', 'tension: beyond 100 m, cavitation-limited')])
    s.chip('trap', 'the standard error', [('p', 'Using p₀/ρg as a universal height limit for trees.'), ('p', 'Forgetting that xylem water is under negative pressure, not zero.')])
    s.chip('num', 'recall', [('p', 'p₀/ρg = 10.3 m water'), ('p', '1 MPa ≈ 102 m of water'), ('p', 'xylem radius ≈ 2.5-50 µm')])
    s.figure('tree_suction')
    S.append(s)

    # ---------------------------------------------------------------- 7
    s = Sheet('Olympiad-07-shallow-wave', 'Why does a shallow-water wave travel at sqrt(gh)?',
              'Go to the frame of the bump: the flow becomes steady and the whole derivation is continuity plus momentum.',
              K, 7, total, 'source: OL7, §3.17',
              'v = sqrt(gh) is one line; the first correction explains steepening')
    s.move('The wave frame', [
        ('p', 'A bump of height η moves over depth h. Sit on the bump: upstream water approaches at speed c with depth h, and leaves over the crest at c′ with depth h + η. Continuity relates the two.'),
        ('m', r'c\,h=c\,' + "'" + r'(h+\eta)'),
    ])
    s.move('Momentum through the bump', [
        ('p', 'The pressure thrust on a section is ½ρgh² per unit width; the momentum flux is ρc²h. Balancing the upstream and crest sections gives a quadratic for c, which solves to a product form.'),
        ('m', r'\frac{1}{2}\rho gh^2+\rho c^2h=\frac{1}{2}\rho g(h+\eta)^2+\rho c\,' + "'" + r'^2(h+\eta)'),
        ('m', r'c^2=g(h+\eta)\left(1+\frac{\eta}{2h}\right)=gh\left(1+\frac{\eta}{h}\right)\left(1+\frac{\eta}{2h}\right)'),
    ])
    s.move('Expand to first order', [
        ('p', 'For a small bump the correction is three quarters of η/h. Larger bumps travel faster, so a crest catches up with the crest ahead of it: the wave steepens. This is the seed of the hydraulic jump and of a breaking wave.'),
        ('m', r'c\approx\sqrt{gh}\left(1+\frac{3\eta}{4h}\right)'),
        ('n', 'η -> 0 recovers the classical result exactly'),
    ])
    s.move('Where the model dies', [
        ('p', 'The derivation assumes η ≪ h ≪ λ: small amplitude and long wavelength. Short waves feel the vertical acceleration and become dispersive; steep waves break. The hand-off is to the wave chapters, where the same speed appears as the long-wavelength limit.'),
    ])
    s.chip('key', 'shallow water', [('m', r'c=\sqrt{gh}'), ('m', r'c\approx\sqrt{gh}(1+3\eta/4h)'), ('p', 'wave frame: steady flow')])
    s.chip('gate', 'validity', [('p', 'η ≪ h (small amplitude)'), ('p', 'h ≪ λ (long wavelength)'), ('p', 'no dissipation, no steep front')])
    s.chip('check', 'dimensions and limits', [('p', '√(gh) has units m/s'), ('p', 'deeper water -> faster wave'), ('p', 'bigger bump -> faster crest -> steepening')])
    s.figure('shallow_wave')
    S.append(s)

    # ---------------------------------------------------------------- 8
    s = Sheet('Olympiad-08-sprinkler', 'Which way does a reverse sprinkler turn?',
              'The answer is decided by an idealisation, not by a formula: reversibility says no torque, dissipation says a small one.',
              K, 8, total, 'source: OL8, §3.11',
              'ejection is ordered-to-ordered; suction is ordered-to-disordered')
    s.move('Ejection is straightforward', [
        ('p', 'Water leaves the nozzles with tangential momentum. The reaction on the arms is opposite the outflow, so the sprinkler rotates against the jets. The torque is the rate of angular momentum carried away.'),
        ('m', r'\tau=\dot m\,r v_{\theta}'),
    ])
    s.move('Suction, in the ideal limit', [
        ('p', 'As suction starts, water is accelerated toward the nozzles and the head receives a brief torque toward the inflow. In steady ideal flow the inflow pattern is time-independent, the assembly\'s angular momentum is constant, and the net torque vanishes.'),
        ('m', r'\tau_{ideal}=0\ \text{(steady, inviscid, symmetric)}'),
        ('n', 'the pressure field at the inlet balances the momentum flux exactly'),
    ])
    s.move('What real fluids add', [
        ('p', 'Viscous dissipation in the inner vortices breaks the symmetry of the pressure recovery, leaving a small steady torque toward the suction direction. Low-friction experiments see exactly that slow creep.'),
        ('n', 'the arrow of the effect is the arrow of dissipation'),
    ])
    s.move('The lesson', [
        ('p', 'Ejection converts ordered motion into ordered motion and is reversible in the ideal limit. Suction converts ordered inflow into disordered internal motion, and the irreversibility is what produces a torque. The problem is a test of whether you can name the idealisation that decides an answer.'),
    ])
    s.chip('key', 'two cases', [('p', 'ejection: torque against the jets'), ('p', 'ideal suction: zero steady torque'), ('p', 'real suction: small torque toward the inflow')])
    s.chip('trap', 'the wrong symmetry', [('p', 'Assuming time-reversal symmetry makes the two cases identical.'), ('p', 'Quoting a formula when the question is about an idealisation.')])
    s.chip('insight', 'carry this', [('p', 'Reversibility is an assumption you can test by asking what dissipates.'), ('p', 'The entropy bookkeeping belongs to thermodynamics.')])
    s.figure('sprinkler')
    S.append(s)

    # ---------------------------------------------------------------- 9
    s = Sheet('Olympiad-09-rotating-energy', 'Where does the energy come from in a rotating frame?',
              'A centrifugal head looks like a free pump. The motor pays for it, and the two ledgers must agree.',
              K, 9, total, 'source: OL9, OL2',
              'pseudo-work in the rotating frame = motor work in the lab frame')
    s.move('The pressure difference that drives the flow', [
        ('p', 'In a rotating U-tube at equal heights, the rotating-frame Bernoulli gives a pressure difference set by the centrifugal head. The liquid is pushed outward, from small r to large r.'),
        ('m', r'p_2-p_1=\frac{1}{2}\rho\omega^2(r_2^2-r_1^2)'),
    ])
    s.move('The kinetic energy gained', [
        ('p', 'A mass m moving from r₁ to r₂ gains lab-frame tangential speed from ωr₁ to ωr₂. The gain is fixed by the geometry and the rotation rate.'),
        ('m', r'\Delta K=\frac{1}{2}m\omega^2(r_2^2-r_1^2)'),
        ('n', 'm = 0.10 kg, ω = 10 s⁻¹, r = 0.10 -> 0.30 m: ΔK = 0.40 J'),
    ])
    s.move('Who pays', [
        ('p', 'In the lab frame the fluid\'s angular momentum grows as it moves outward. Something must supply the torque: the motor, holding ω constant against the reaction of the outward-moving liquid. Without the motor, ω would sag.'),
        ('m', r'W_{motor}=\Delta K\quad(\text{rigid tube, constant }\omega)'),
    ])
    s.move('The audit closes', [
        ('p', 'The rotating-frame "centrifugal work" is the motor\'s work in disguise. If your energy account in the rotating frame does not include the motor, it cannot balance; if it does, the two frames agree.'),
    ])
    s.chip('key', 'rotating energy', [('m', r'p-\frac{1}{2}\rho\omega^2r^2+\rho gz=\text{const}'), ('m', r'\Delta K=\frac{1}{2}m\omega^2(r_2^2-r_1^2)'), ('p', 'motor work = ΔK')])
    s.chip('trap', 'free lunch', [('p', 'Treating the centrifugal head as an energy source with no torque reaction.'), ('p', 'Forgetting that the moment of inertia of the system grows as liquid moves out.')])
    s.chip('check', 'bookkeeping', [('p', 'ω = 0: no head, no gain.'), ('p', 'r₁ = r₂: no gain.'), ('p', 'motor off: ω sags as I grows.')])
    s.figure('rotating_energy')
    S.append(s)

    # ---------------------------------------------------------------- 10
    s = Sheet('Olympiad-10-viscometer', 'Reconstruct a real measurement: glycerine\'s viscosity by Stokes',
              'An experiment is a prediction plus the checks that say the prediction is allowed. This one closes to 6.5 s.',
              K, 10, total, 'source: OL10, E9',
              'v_t = 0.038 m/s, wall-corrected 0.031 m/s, t = 6.5 s over 20 cm')
    s.move('Design the experiment', [
        ('p', 'Steel spheres of radius 2.0 mm fall through glycerine in a 4 cm cylinder. Time the passage between two marks 20 cm apart, in the middle of the column so the sphere has reached terminal speed.'),
        ('m', r'v_t=\frac{2r^2(\rho-\sigma)g}{9\eta}=\frac{2(4\times10^{-6})(6540)(9.8)}{13.5}=0.038\ \mathrm{m/s}'),
    ])
    s.move('Correct for the walls', [
        ('p', 'The cylinder is only ten sphere radii across, so the walls slow the sphere. The Ladenburg correction converts the measured speed into the unbounded value.'),
        ('m', r'v_{true}=v_{meas}\left(1+2.4\frac{r}{R}\right)\ \Rightarrow\ v_{meas}=\frac{0.0380}{1.24}=0.0307\ \mathrm{m/s}'),
        ('n', 'time over 20 cm: t = 0.20/0.0307 = 6.5 s'),
    ])
    s.move('Two regime checks', [
        ('p', 'First, Re = σv(2r)/η = 0.10, so Stokes is honest. Second, the timing window excludes the entry and exit regions where the sphere is still accelerating or feeling the ends.'),
        ('m', r'\text{Re}=\frac{(1260)(0.0307)(4\times10^{-3})}{1.5}=0.10'),
    ])
    s.move('The fingerprint, and the error budget', [
        ('p', 'Doubling the radius quadruples the terminal speed: the r² signature confirms the regime. The dominant error is temperature, since glycerine\'s viscosity falls by roughly a factor of two for a 10 °C rise.'),
        ('n', 'state the temperature with the viscosity, or the measurement is not reproducible'),
    ])
    s.chip('key', 'the prediction', [('m', r'v_t=2r^2\Delta\rho g/9\eta'), ('m', r'v_{true}=v_{meas}(1+2.4r/R)'), ('p', 't = 6.5 s over 20 cm')])
    s.chip('gate', 'before you trust it', [('p', 'Re ≲ 1'), ('p', 'wall correction applied'), ('p', 'timed in the middle third'), ('p', 'temperature recorded')])
    s.chip('trap', 'error budget', [('p', 'Ignoring the wall correction: 24% here.'), ('p', 'Timing from the release point, where the sphere is still accelerating.'), ('p', 'Quoting η without its temperature.')])
    s.figure('viscometer')
    S.append(s)

    # ---------------------------------------------------------------- 11
    s = Sheet('Olympiad-11-regime-map', 'Where does this chapter stop being true?',
              'Six tools cover the syllabus. Five failure modes bound them, and each has a name and a hand-off.',
              K, 11, total, 'source: §9-§10.1, T1-T8, C9-C12',
              'triage by what the fluid is doing; then check which assumption you just used')
    s.move('The triage tree', [
        ('p', 'At rest or rigidly accelerated: hydrostatics with g or g_eff. Floating or level-changing: Archimedes plus the displaced-volume ledger. Short device with speeds: continuity and Bernoulli, gates named. Long narrow pipe: Poiseuille network. Jet or thrust: momentum flux. Millimetre scale: the gamma family.'),
        ('n', 'six boxes, six equations; the tool is chosen before the algebra starts'),
    ])
    s.move('Five ways the model dies', [
        ('p', 'Turbulence beyond Re of a few thousand destroys the quantitative force of Bernoulli and Poiseuille. Unsteady free surfaces slosh and jump, and past a jump they dissipate. Compressibility matters when the speed approaches √(B/ρ), about 1480 m/s in water. Non-Newtonian fluids break the linear stress law. Below a micron, no-slip itself fails.'),
        ('m', r'c_s=\sqrt{B/\rho}\approx1480\ \mathrm{m/s}\ \text{in water}'),
    ])
    s.move('What each failure hands off to', [
        ('p', 'Container elasticity goes to the elasticity chapter; equations of state to thermodynamics; wave kinematics to string and sound waves; radiation pressure to electromagnetic waves. The shallow-water bridge hands its long-wavelength limit to the wave chapters.'),
        ('n', 'the hand-off is part of the answer, not an apology'),
    ])
    s.move('The last audit', [
        ('p', 'Every pressure labelled absolute or gauge. Displaced volume drawn, not assumed. Bernoulli gates named if used. Re printed with every Stokes number. The factor two audited on every film. g_eff consistent. Units in every substitution. One limit checked per item. Centre of pressure not confused with centroid. Answer magnitude sane.'),
        ('n', 'ten checks; each one has caught a real exam error in this chapter'),
    ])
    s.chip('key', 'the map', [('p', 'statics -> p = ρgh'), ('p', 'float -> F_b = ρfVg'), ('p', 'flow -> Bernoulli, four gates'), ('p', 'pipe -> Poiseuille network'), ('p', 'jet -> ρav²'), ('p', 'mm scale -> 2γ/r, Jurin')])
    s.chip('trap', 'overreach', [('p', 'Using a formula outside the regime printed beside it.'), ('p', 'Quoting a number without its check.'), ('p', 'Pretending a model is exact because the algebra closed.')])
    s.chip('check', 'final audit', [('p', 'abs/gauge labelled'), ('p', 'V_disp drawn'), ('p', 'gates named'), ('p', 'Re printed'), ('p', 'factor 2 counted'), ('p', 'one limit checked')])
    s.figure('regime_map')
    S.append(s)

    return S
