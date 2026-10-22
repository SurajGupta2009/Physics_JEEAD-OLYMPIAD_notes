"""Part II content: the Olympiad layer of work, energy and power."""
from layout import Sheet

K = "WORK, ENERGY, POWER  /  PART II: OLYMPIAD + EXTENSIONS"
KC = "CIRCULAR MOTION  /  PART II: OLYMPIAD + EXTENSIONS"
SRC = 'source: Work-energy-power.md '
SRCC = 'source: Motion-in-two-dimensions.md '


def build(total):
    S = []

    # ============================================================ 1 CM SPLIT
    s = Sheet('Olympiad-01-cm-split', 'How much of the energy is actually available?',
              'Two blocks collide. The total kinetic energy is 100 J, but only part of it can become heat or deformation. Which part?',
              K, 1, total, SRC + 'OL1, §3.11',
              'split the kinetic energy into drift of the centre of mass plus internal motion',
              stage='linked')
    s.move('Two pieces of one number', [
        ('p', 'Write each velocity as the centre-of-mass velocity plus a velocity relative to it. The cross terms cancel because the total momentum in the CM frame is zero, and the kinetic energy separates into two independent pieces.'),
        ('m', r'K=\frac{1}{2}Mv_{\mathrm{cm}}^{2}+K_{\mathrm{rel}},\qquad M=m_1+m_2'),
    ])
    s.move('The internal part is the reducible one', [
        ('p', 'No internal force can change the CM velocity, so the drift energy is untouchable from inside. Everything a collision, an explosion or a spring can convert comes from the relative part, and that is why the reduced mass appears in every collision formula.'),
        ('m', r'K_{\mathrm{rel}}=\frac{1}{2}\mu v_{\mathrm{rel}}^{2},\qquad \mu=\frac{m_1m_2}{m_1+m_2}'),
        ('n', 'a perfectly inelastic collision converts exactly K_rel into heat'),
    ])
    s.move('The two limits to remember', [
        ('p', 'Equal masses moving toward each other at the same speed: the CM is at rest and all the energy is internal, so all of it can be lost. A light particle hitting a heavy one at rest: almost all the energy is drift, so very little can be converted, which is why a bullet heats a wall far more easily than a ping-pong ball heats a block.'),
        ('m', r'm_1=m_2:\ K_{\mathrm{rel}}=\frac{1}{2}K_{\mathrm{tot}},\qquad m_1\ll m_2:\ K_{\mathrm{rel}}\approx\frac{m_1}{m_2}K_{\mathrm{tot}}'),
    ])
    s.chip('key', 'the decomposition', [
        ('m', r'K=\frac{1}{2}Mv_{\rm cm}^{2}+\frac{1}{2}\mu v_{\rm rel}^{2}'),
    ])
    s.chip('num', 'a check', [
        ('p', '2 kg at 3 m/s meets 1 kg at rest'),
        ('p', 'mu = 2/3, K_rel = 3 J of the 9 J total'),
    ])
    s.chip('insight', 'why reduced mass appears', [
        ('p', 'It is the mass that carries the internal motion. Every two-body collision formula is a one-body formula with mu in place of m.'),
    ])
    s.figure('cm_decomposition')
    S.append(s)

    # ============================================================ 2 EFFECTIVE POTENTIAL
    s = Sheet('Olympiad-02-effective-potential', 'Why does angular momentum keep a planet out of the Sun?',
              'Gravity pulls inward with nothing to oppose it. Why does a planet not simply fall in?',
              K, 2, total, SRC + 'OL2, §3.9',
              'the angular term is a repulsive barrier made of kinetic energy, not a force',
              stage='one')
    s.move('Separate the two motions', [
        ('p', 'In a central field the angular momentum is constant, so the angular part of the kinetic energy is fixed by the radius alone. Move it to the other side of the energy equation and it behaves like an extra potential.'),
        ('m', r'E=\frac{1}{2}m\dot r^{2}+U_{\mathrm{eff}}(r),\qquad U_{\mathrm{eff}}=U(r)+\frac{L^{2}}{2mr^{2}}'),
    ])
    s.move('Read the effective curve', [
        ('p', 'The added term is positive and falls as 1/r squared, so it dominates at small radii and creates a minimum when combined with an attractive potential. The minimum is the circular orbit; a small radial oscillation around it is an ellipse.'),
        ('m', r'\frac{dU_{\mathrm{eff}}}{dr}=0\ \Rightarrow\ r_0=\frac{L^{2}}{GMm^{2}}'),
        ('n', 'no force pushes outward: the barrier is the cost of conserving angular momentum'),
    ])
    s.move('Where it is genuinely useful', [
        ('p', 'The same construction gives the critical angular momentum below which a particle falls in, the turning points of a comet, and the stability condition for a circular orbit. It also explains the bead on a rotating hoop (OLY 08), which is the same trick in a rotating frame.'),
    ])
    s.chip('key', 'effective potential', [
        ('m', r'U_{\rm eff}=U(r)+\frac{L^{2}}{2mr^{2}}'),
        ('p', 'the angular part of K, rewritten as a barrier'),
    ])
    s.chip('num', 'a check', [
        ('p', 'Earth: L = 2.66e40, GMm² gives r = 1.5e11 m'),
        ('p', 'the minimum of U_eff reproduces the orbit radius'),
    ])
    s.chip('trap', 'calling it a centrifugal force', [
        ('p', 'In an inertial frame there is no outward force. The barrier is energy bookkeeping; the only force is inward.'),
    ])
    s.figure('effective_potential')
    S.append(s)

    # ============================================================ 3 BOUNCE
    s = Sheet('Olympiad-03-bouncing-ball', 'How far does a bouncing ball travel before it stops?',
              'A ball is dropped from h and returns to e²h after each bounce. The bounces are infinite; is the total distance infinite too?',
              K, 3, total, SRC + 'OL3, OL9',
              'two geometric series, one for distance and one for time, both with finite sums',
              stage='one')
    s.move('Write the two series', [
        ('p', 'The first fall is h. Every later bounce contributes a rise and a fall, each shorter by e squared. The flight time scales by e rather than e squared, because time goes as the square root of height.'),
        ('m', r's=h\frac{1+e^{2}}{1-e^{2}},\qquad t=\sqrt{\frac{2h}{g}}\cdot\frac{1+e}{1-e}'),
    ])
    s.move('The energy view', [
        ('p', 'Each impact multiplies the speed by e and therefore the kinetic energy by e squared. The energy lost per bounce is a fixed fraction of what is left, so the sequence is geometric and the total lost before rest is exactly the initial mgh.'),
        ('m', r'E_{n}=e^{2n}mgh,\qquad \sum E_{\mathrm{lost}}=mgh'),
        ('n', 'the ball never gets negative energy: the sum is bounded by the initial store'),
    ])
    s.move('Why the time is finite while the bounces are not', [
        ('p', 'The bounce count diverges but the durations shrink faster than the count grows. The series converges to a finite time, so the ball comes to rest in finite time after infinitely many bounces, which is the standard counterexample to "infinitely many events need infinite time".'),
        ('m', r't_0\left(1+2e+2e^{2}+\dots\right)=t_0\frac{1+e}{1-e}'),
    ])
    s.chip('key', 'the closed forms', [
        ('m', r's=h\frac{1+e^{2}}{1-e^{2}},\qquad t=\sqrt{\frac{2h}{g}}\cdot\frac{1+e}{1-e}'),
    ])
    s.chip('num', 'a check', [
        ('p', 'h = 10 m, e = 0.5'),
        ('p', 's = 16.7 m, t = 4.29 s'),
    ])
    s.chip('trap', 'the factor of two', [
        ('p', 'Every bounce after the first contributes twice its height, once up and once down.'),
    ])
    s.figure('bounce_energy')
    S.append(s)

    # ============================================================ 4 ROLLING
    s = Sheet('Olympiad-04-rolling-energy', 'Why does a rolling ball beat a sliding block downhill?',
              'A ball and a block are released from the same height on the same slope. The block has no friction, the ball rolls. Which arrives first?',
              K, 4, total, SRC + 'OL4',
              'a rolling body spends part of its energy on rotation, so it descends more slowly',
              stage='one')
    s.move('Two kinetic terms', [
        ('p', 'A rolling body translates and rotates at once. With the rolling condition the rotation is fixed by the speed, so the total kinetic energy is a fixed multiple of half m v squared.'),
        ('m', r'K=\frac{1}{2}mv^{2}+\frac{1}{2}I\omega^{2}=\frac{1}{2}mv^{2}\left(1+\frac{I}{mR^{2}}\right)'),
    ])
    s.move('The shape sets the multiple', [
        ('p', 'A ring has I = mR squared, so it carries twice the energy of a sliding block at the same speed and is the slowest. A disc gives three quarters, a solid sphere seven tenths. The order of arrival downhill is always sphere, disc, ring, regardless of mass and radius.'),
        ('m', r'K:\ \frac{1}{2}mv^{2}\ (\text{slide}),\ \frac{3}{4}mv^{2}\ (\text{disc}),\ \frac{7}{10}mv^{2}\ (\text{sphere}),\ mv^{2}\ (\text{ring})'),
        ('n', 'the ratio I/mR squared is the only thing that matters'),
    ])
    s.move('Where the energy goes on a slope', [
        ('p', 'Energy conservation from height h gives the speed at the bottom with the same factor in the denominator. Static friction does the work that spins the body up, but it does no net work on the rolling body because the contact point does not slip.'),
        ('m', r'v^{2}=\frac{2gh}{1+I/(mR^{2})}'),
    ])
    s.chip('key', 'rolling energy', [
        ('m', r'K=\frac{1}{2}mv^{2}\left(1+\frac{I}{mR^{2}}\right)'),
    ])
    s.chip('num', 'a check', [
        ('p', 'solid sphere from 1.4 m'),
        ('p', 'v = sqrt(2 x 9.8 x 1.4 / 1.4) = 4.43 m/s'),
    ])
    s.chip('trap', 'adding friction work', [
        ('p', 'Static friction at a non-slipping contact does no work on the rolling body. Do not subtract f d from its energy.'),
    ])
    s.figure('rolling_energy')
    S.append(s)

    # ============================================================ 5 WEDGE
    s = Sheet('Olympiad-05-block-on-wedge', 'Why is the block on a moving wedge slower than sqrt(2gh)?',
              'A block slides down a smooth wedge that is free to slide on a smooth table. The textbook answer sqrt(2gh) must be wrong. Why?',
              K, 5, total, SRC + 'OL5, §3.11',
              'the wedge takes a share of the energy, so the block cannot have all of it',
              stage='linked')
    s.move('Two unknowns, two equations', [
        ('p', 'Horizontal momentum is conserved for the pair, and mechanical energy is conserved for the pair. Those two equations determine the wedge speed and the relative sliding speed; the block ground speed then follows from the vector sum.'),
        ('m', r'u^{2}=\frac{2gh(M+m)}{M+m\sin^{2}\theta},\qquad V=\frac{mu\cos\theta}{M+m}'),
    ])
    s.move('The error the source warns about', [
        ('p', 'Treating u as the block speed is the standard mistake. u is measured along the face relative to the wedge; the ground speed is the vector sum of u and V, and is smaller for a finite wedge.'),
        ('m', r'v_b^{2}=u^{2}\left(\sin^{2}\theta+\left(\frac{M}{M+m}\right)^{2}\cos^{2}\theta\right)'),
        ('n', 'the block ground speed is below sqrt(2gh) for every finite M'),
    ])
    s.move('The two limits', [
        ('p', 'An infinitely heavy wedge cannot recoil and the block recovers sqrt(2gh). A massless wedge carries almost no energy, so the block again approaches the same speed. The deficit peaks when the masses are comparable.'),
        ('m', r'M\to\infty:\ v_b\to\sqrt{2gh},\qquad M\to0:\ v_b\to\sqrt{2gh}'),
    ])
    s.chip('key', 'the pair', [
        ('m', r'mgh=\frac{1}{2}MV^{2}+\frac{1}{2}mv_b^{2}'),
        ('p', 'plus horizontal momentum conservation'),
    ])
    s.chip('num', 'a check', [
        ('p', 'm = 1, M = 4, theta = 30°, h = 0.5 m'),
        ('p', 'u = 1.60 m/s, V = 0.28 m/s, v_b = 1.15 m/s'),
    ])
    s.chip('trap', 'one-body energy', [
        ('p', 'The block alone does not conserve energy: the normal force does work on it because the face moves.'),
    ])
    s.figure('wedge_energy')
    S.append(s)

    # ============================================================ 6 LAUNCH
    s = Sheet('Olympiad-06-satellite-launch', 'How much energy does it take to reach orbit?',
              'Escape needs the full well depth. Orbit needs less, but not as little as you might hope. What fraction?',
              K, 6, total, SRC + 'OL6',
              'low orbit costs half the escape energy, and the other half is the speed you keep',
              stage='one')
    s.move('The two energies', [
        ('p', 'The energy at rest on the surface is minus GMm over R. The energy of a circular orbit is minus GMm over twice r, which is the virial relation for a circular orbit. The difference is what the rocket must supply.'),
        ('m', r'E_{\mathrm{orbit}}-E_{\mathrm{surface}}=GMm\left(\frac{1}{R}-\frac{1}{2r}\right)'),
    ])
    s.move('The ratio that surprises', [
        ('p', 'For a low orbit, r is close to R and the bracket is about one over twice R. The escape energy is GMm over R. So orbit costs half of escape, and the remaining half is the kinetic energy the satellite keeps in orbit, not a loss.'),
        ('m', r'\frac{\Delta E_{\mathrm{orbit}}}{\Delta E_{\mathrm{escape}}}=\frac{1}{2}-\frac{R}{2r}'),
        ('n', 'the orbital speed is 1/sqrt(2) of the escape speed, which is the same statement'),
    ])
    s.move('Why it matters', [
        ('p', 'Reaching orbit is not mainly about height; it is mostly about the horizontal speed. A sounding rocket that reaches 400 km with no horizontal speed has done far less than a satellite at the same height, which is why launch vehicles pitch over early.'),
    ])
    s.chip('key', 'the ratio', [
        ('m', r'\Delta E_{\rm orbit}=\frac{GMm}{2R}\ \text{(low orbit)},\qquad = \frac{1}{2}\Delta E_{\rm esc}'),
    ])
    s.chip('num', 'a check', [
        ('p', 'Earth: v_esc = 11.2 km/s, v_orbit = 7.9 km/s'),
        ('p', 'ratio of energies: 1/sqrt(2) squared = 0.5'),
    ])
    s.chip('trap', 'counting the orbital KE as wasted', [
        ('p', 'It is stored, not lost: bringing the satellite down returns it. Only the drag losses are gone.'),
    ])
    s.figure('launch_energy')
    S.append(s)

    # ============================================================ 7 CHAIN
    s = Sheet('Olympiad-07-chain-unroll', 'Where does the missing half of the work go?',
              'A chain is pulled off a table at constant speed v. The power delivered is F v, but the energy in the chain grows more slowly. Where is the difference?',
              K, 7, total, SRC + 'OL7',
              'links are jerked into motion inelastically, and the lost half is heat',
              stage='one')
    s.move('The two rates', [
        ('p', 'The force must support the hanging weight and supply the momentum flux. Multiply by v to get the power delivered, and compare it with the rate of change of the mechanical energy.'),
        ('m', r'P=Fv=\lambda xgv+\lambda v^{3},\qquad \dot E=\lambda xgv+\frac{1}{2}\lambda v^{3}'),
    ])
    s.move('The difference is the collision', [
        ('p', 'Each link is at rest and then shares the speed v of a moving system. That is a perfectly inelastic capture, and half the energy invested in the capture is unavoidably lost, exactly as in any inelastic collision.'),
        ('m', r'\dot Q=\frac{1}{2}\lambda v^{3}'),
        ('n', 'the loss scales as v cubed, so fast pulling is disproportionately wasteful'),
    ])
    s.move('The same ledger as the rocket', [
        ('p', 'Both the chain and the rocket are open systems: mass crosses the boundary, and the momentum flux must be included. The chain is the inelastic limit of the rocket, with the links being captured instead of expelled.'),
    ])
    s.chip('key', 'the audit', [
        ('m', r'F=\lambda xg+\lambda v^{2},\qquad \dot Q=\frac{1}{2}\lambda v^{3}'),
    ])
    s.chip('num', 'a check', [
        ('p', 'lambda = 2 kg/m, x = 2, v = 1 m/s'),
        ('p', 'F = 41.2 N, loss 1 W of the 41.2 W delivered'),
    ])
    s.chip('insight', 'the general rule', [
        ('p', 'Mass captured by a moving system always costs a factor of two: half to motion, half to heat.'),
    ])
    s.figure('chain_unroll')
    S.append(s)

    # ============================================================ 8 BEAD
    s = Sheet('Olympiad-08-bead-on-hoop', 'Why does a spinning hoop make the bead climb?',
              'A bead slides freely on a smooth hoop spinning about its vertical diameter. At high enough speed it leaves the bottom. Where does the energy come from?',
              K, 8, total, SRC + 'OL8',
              'the hoop does work on the bead, and in the rotating frame that is one effective potential',
              stage='spin')
    s.move('Two contributions, one curve', [
        ('p', 'Gravity favours the bottom and the rotation favours the equator, because the bead must be further from the axis to have a large radius at high angular speed. Adding the two produces an effective potential whose shape depends on omega.'),
        ('m', r'U_{\mathrm{eff}}(\theta)=-mgR\cos\theta-\frac{1}{2}m\omega^{2}R^{2}\sin^{2}\theta'),
    ])
    s.move('The threshold', [
        ('p', 'Setting the derivative to zero gives the bottom and, for fast enough rotation, a pair of side positions. The condition for the side positions to exist is that the rotational term beats gravity at the bottom.'),
        ('m', r'\omega>\omega_c=\sqrt{\frac{g}{R}},\qquad \cos\theta_0=\frac{g}{\omega^{2}R}'),
        ('n', 'below the critical speed the only stable seat is the bottom'),
    ])
    s.move('Where the energy comes from', [
        ('p', 'The hoop is driven, so it does work on the bead through the normal force, which has a component along the bead motion once the hoop is rotating. Energy is supplied by the motor, and the bead settles where the effective potential is lowest.'),
    ])
    s.chip('key', 'the result', [
        ('m', r'\omega_c=\sqrt{g/R},\qquad \cos\theta_0=g/(\omega^{2}R)'),
    ])
    s.chip('num', 'a check', [
        ('p', 'R = 0.5 m, omega = 6 rad/s'),
        ('p', 'omega_c = 4.43, theta = 57°'),
    ])
    s.chip('trap', 'energy conservation in the lab frame', [
        ('p', 'The bead alone does not conserve energy. Use the effective potential, or include the work done by the hoop.'),
    ])
    s.figure('bead_energy')
    S.append(s)

    # ============================================================ 9 RESTITUTION
    s = Sheet('Olympiad-09-restitution', 'What does the coefficient of restitution actually measure?',
              'Two balls drop from the same height onto the same floor and bounce to different heights. What single number separates them?',
              K, 9, total, SRC + 'OL3, OL9, §3.14',
              'e is the ratio of relative speeds, so energy is multiplied by e squared per impact',
              stage='one')
    s.move('Define it on speeds', [
        ('p', 'The coefficient of restitution is the ratio of separation speed to approach speed along the normal. It is a property of the pair of surfaces and the impact speed, not of the mass.'),
        ('m', r'e=\frac{v_{\mathrm{sep}}}{v_{\mathrm{app}}},\qquad 0\le e\le1'),
    ])
    s.move('What it does to energy', [
        ('p', 'Since energy goes as speed squared, one bounce multiplies the mechanical energy by e squared. That is why the rebound height is e squared times the drop height, and why a bouncy ball is specified by its rebound ratio rather than by a force.'),
        ('m', r'\frac{h_{n+1}}{h_n}=e^{2},\qquad \frac{K_{n+1}}{K_n}=e^{2}'),
        ('n', 'e is a ratio of speeds; the energy ratio is its square'),
    ])
    s.move('The two extremes', [
        ('p', 'e = 1 is elastic: no energy lost, the ball returns to the same height for ever. e = 0 is perfectly inelastic: the ball stays on the floor, and all the kinetic energy becomes heat and sound. Real balls sit between 0.6 and 0.9.'),
        ('n', 'a superball at e = 0.9 keeps 81 per cent of its energy per bounce'),
    ])
    s.chip('def', 'restitution', [
        ('m', r'e=v_{\rm sep}/v_{\rm app}'),
        ('p', 'no mass, no height: a property of the impact'),
    ])
    s.chip('num', 'a check', [
        ('p', 'drops 2 m, rebounds 1.28 m'),
        ('p', 'e = sqrt(1.28/2) = 0.8, energy kept 64 per cent'),
    ])
    s.chip('trap', 'e as an energy ratio', [
        ('p', 'It is not. Energy scales as its square, so a rebound to half the height means e = 0.71, not 0.5.'),
    ])
    s.figure('restitution_energy')
    S.append(s)

    # ============================================================ 10 FLYWHEEL
    s = Sheet('Olympiad-10-flywheel', 'Who pays for the kinetic energy of a flywheel?',
              'A motor of constant power spins up a flywheel. The angular speed grows, but not linearly. Why, and who supplies the difference?',
              K, 10, total, SRC + 'OL10',
              'at constant power the torque falls as one over omega, so the spin-up slows as root t',
              stage='spin')
    s.move('Power into rotation', [
        ('p', 'The rotational kinetic energy is half I omega squared, so its derivative gives the power. That is the rotational twin of P = F v, with torque in place of force and omega in place of speed.'),
        ('m', r'P=\frac{d}{dt}\left(\frac{1}{2}I\omega^{2}\right)=I\omega\dot\omega=\tau\omega'),
    ])
    s.move('Integrate', [
        ('p', 'With P constant the differential equation separates and gives omega proportional to the square root of time. The torque falls as one over omega, which is why a constant-power motor is slow at the start and cannot spin a wheel up evenly.'),
        ('m', r'\omega=\sqrt{\frac{2Pt}{I}},\qquad \tau=\frac{P}{\omega}'),
        ('n', 'the same structure as v = sqrt(2Pt/m) for a car'),
    ])
    s.move('Where the energy sits', [
        ('p', 'All the work done by the motor ends up in the wheel: none is lost if the bearing is ideal. The question in the title is answered by the motor, and the only subtlety is the non-uniform rate at which it is delivered.'),
    ])
    s.chip('key', 'constant-power spin-up', [
        ('m', r'\omega=\sqrt{2Pt/I}'),
        ('p', 'and torque = P/omega'),
    ])
    s.chip('num', 'a check', [
        ('p', 'I = 12 kg m², P = 500 W'),
        ('p', 'omega(10 s) = sqrt(833) = 28.9 rad/s'),
    ])
    s.chip('trap', 'using tau = I alpha with constant tau', [
        ('p', 'Constant power is not constant torque. Set tau = P/omega and solve the differential equation.'),
    ])
    s.figure('flywheel')
    S.append(s)

    # ============================================================ 11 PSEUDO WORK
    s = Sheet('Olympiad-11-pseudo-work', 'Can a force that is not there do work?',
              'A ball hangs in an accelerating cart. In the cart frame it swings backward and gains speed. Which force did the work?',
              K, 11, total, SRC + '§3.4, §3.10',
              'in an accelerating frame the pseudo force does work, and the frame energy book stays closed',
              stage='frame')
    s.move('Two frames, two accounts', [
        ('p', 'In the ground frame the tension does the work that changes the ball speed; the pseudo force does not exist. In the cart frame the ball moves backward along the pseudo force, which does positive work equal to m a times that displacement.'),
        ('m', r'W_{\mathrm{pseudo}}=\int(-m\mathbf{a}_0)\cdot d\mathbf{r}'),
    ])
    s.move('Why the frame version still balances', [
        ('p', 'In a uniformly accelerating frame the pseudo force is constant and uniform, so it has a potential m a dot r and the energy book closes. In a rotating frame the pseudo forces include Coriolis, which is velocity-dependent and does no work, and centrifugal, which does and has a potential.'),
        ('m', r'U_{\mathrm{cf}}=-\frac{1}{2}m\omega^{2}r_{\perp}^{2}'),
        ('n', 'the bead on the hoop is the standard consumer of that potential'),
    ])
    s.move('The exam rule', [
        ('p', 'You may use energy in an accelerating frame only if you include the pseudo potential. Most students forget it and get a speed that is too large. The safe route is to compute energy in the inertial frame and forces in whichever frame is easier.'),
    ])
    s.chip('key', 'pseudo potential', [
        ('m', r'U_{\rm pseudo}=-m\mathbf{a}_0\cdot\mathbf{r}'),
        ('p', 'centrifugal: −half m omega squared r squared'),
    ])
    s.chip('trap', 'Coriolis in an energy equation', [
        ('p', 'Coriolis is perpendicular to the velocity, so it does no work and has no potential. Only the uniform and centrifugal parts enter energy.'),
    ])
    s.chip('insight', 'the safe habit', [
        ('p', 'Energy in the inertial frame, forces in the convenient frame. Mixing the two is where signs go wrong.'),
    ])
    s.figure('pseudo_work')
    S.append(s)

    # ============================================================ 12 PATH INTEGRAL
    s = Sheet('Olympiad-12-path-integral', 'Is one closed loop enough to prove a force is conservative?',
              'You are handed a force field and one closed loop. If the loop integral vanishes, may you conclude that a potential exists?',
              K, 12, total, SRC + '§3.6, §3.13',
              'one loop proves nothing; every loop must vanish, which is what the curl tests',
              stage='one')
    s.move('What the definition demands', [
        ('p', 'Conservatism is a statement about all paths between any two points. A single loop that happens to close is a single data point; the field could still fail elsewhere.'),
        ('m', r'\oint\mathbf{F}\cdot d\mathbf{r}=0\ \text{for every loop}'),
    ])
    s.move('The local test', [
        ('p', 'For a force field in three dimensions the loop condition is equivalent to the curl vanishing everywhere in a simply connected region. In two dimensions that is the single condition that the cross derivative matches.'),
        ('m', r'\nabla\times\mathbf{F}=0\quad\Longleftrightarrow\quad \partial_xF_y=\partial_yF_x'),
        ('n', 'a vortex field passes no loop, and its curl is not zero'),
    ])
    s.move('Why this matters in mechanics', [
        ('p', 'Every potential energy you use in this chapter was licensed by that test. Gravity, the spring and the uniform field pass; friction and drag fail because they depend on the direction of travel or on speed, so no function of position can reproduce them.'),
    ])
    s.chip('gate', 'the two tests', [
        ('p', 'global: all loop integrals zero. local: curl zero in a simply connected region.'),
    ])
    s.chip('num', 'a check', [
        ('p', 'F = (−y, x): curl = 2, loop work = 2 x area'),
        ('p', 'nonzero for every loop: not conservative'),
    ])
    s.chip('trap', 'one loop as proof', [
        ('p', 'A vanishing loop integral on a convenient circle proves nothing about the rest of the plane.'),
    ])
    s.figure('path_integral')
    S.append(s)
    # ============================================================ 13 DRAG
    s = Sheet('Olympiad-13-drag-power', 'Why does doubling speed need eight times the power?',
              'A cyclist at 20 km/h is comfortable. At 40 km/h the same rider is exhausted. Why is the cost not twice?',
              K, 13, total, SRC + '§3.5, §3.12, §10.2',
              'air resistance grows as the square of speed, and power as its cube',
              stage='one')
    s.move('The force law', [
        ('p', 'At everyday speeds the drag force is proportional to the square of the speed. The power needed to overcome it is force times speed, so it goes as the cube.'),
        ('m', r'f=bv^{2},\qquad P=bv^{3}'),
    ])
    s.move('The top speed', [
        ('p', 'At constant speed the drive equals the drag, so a fixed power sets a maximum speed proportional to the cube root of the power. Four times the power buys only 1.6 times the speed, which is why the land speed record is so expensive.'),
        ('m', r'v_{\max}=\left(\frac{P}{b}\right)^{1/3}'),
        ('n', 'the cube root is the sting: 100 kW for a car means about 55 m/s with b = 0.6'),
    ])
    s.move('The approach to the top', [
        ('p', 'With a constant driving force the speed approaches terminal speed exponentially, and with constant power it approaches the ceiling from below without ever reaching it. Either way the last few metres per second cost most of the time.'),
        ('m', r'v(t)=v_\infty\left(1-e^{-t/\tau}\right)\quad\text{(constant drive)}'),
    ])
    s.chip('key', 'drag power', [
        ('m', r'f=bv^{2},\qquad P=bv^{3}'),
    ])
    s.chip('num', 'a check', [
        ('p', 'b = 0.6, P = 100 kW'),
        ('p', 'v_max = (100000/0.6)^(1/3) = 55 m/s'),
    ])
    s.chip('trap', 'linear scaling', [
        ('p', 'Doubling speed quadruples the force and multiplies the power by eight. Linear intuition is wrong here by a factor of eight.'),
    ])
    s.figure('drag_power')
    S.append(s)

    # ============================================================ 14 LIMITS
    s = Sheet('Olympiad-14-energy-limits', 'Where does the energy bookkeeping stop working?',
              'The chapter treats mechanical energy as exact. At what speed, and at what scale, does the ledger need new terms?',
              K, 14, total, SRC + '§10.2',
              'the classical ledger is a low-speed approximation, and the rest mass joins it at high speed',
              stage='one')
    s.move('Two fences', [
        ('p', 'Special relativity replaces half m v squared by (gamma minus one) m c squared once v is a noticeable fraction of c. Quantum mechanics makes the energy spectrum discrete once the action is comparable to h bar. Inside both fences the classical ledger is exact.'),
        ('m', r'K=(\gamma-1)mc^{2}\approx\frac{1}{2}mv^{2}\ \text{for }v\ll c'),
    ])
    s.move('What survives', [
        ('p', 'The work-energy theorem survives both revolutions: work still equals the change in kinetic energy, with the relativistic kinetic energy. What does not survive is the formula half m v squared, and with it every classical estimate above about a tenth of the speed of light.'),
        ('m', r'W=\Delta K\ \text{always};\quad K=\frac{1}{2}mv^{2}\ \text{only at low speed}'),
        ('n', 'the theorem is more general than the formula it was derived from'),
    ])
    s.move('The practical boundary', [
        ('p', 'For a car, a satellite, a bullet, even a spacecraft at 10 km/s, gamma differs from one by less than one part in ten million. The relativistic correction is worth computing for electrons, for particle accelerators, and for nothing in this chapter.'),
    ])
    s.chip('gate', 'the ratio to check', [
        ('p', 'Compute v/c. Below 0.1, classical is safe to a fraction of a per cent.'),
    ])
    s.chip('trap', 'quoting five figures', [
        ('p', 'With g given to two figures and friction coefficients guessed, four-figure energy answers are a claim the data cannot support.'),
    ])
    s.chip('insight', 'what the chapter really teaches', [
        ('p', 'Not the formulas, but the habit: name the store, name the loss, and check the ledger balances.'),
    ])
    s.figure('energy_limits')
    S.append(s)

    # ============================================================ 15 TANGENTIAL + NORMAL
    s = Sheet('Olympiad-15-tangential-normal', 'What if the speed changes as well as the direction?',
              'A car on a curve brakes while turning. What is the total acceleration, and at what angle does it point?',
              KC, 15, total, SRCC + '§3.9, D4.8, D4.12, Q17',
              'two perpendicular components: one changes the speed, one changes the direction',
              stage='spin')
    s.move('Split the acceleration', [
        ('p', 'Resolve along the tangent and the normal. The tangential part is the rate of change of speed; the normal part is v squared over R. They are perpendicular, so the magnitudes add in quadrature.'),
        ('m', r'a_t=\frac{dv}{dt},\qquad a_n=\frac{v^{2}}{R},\qquad a=\sqrt{a_t^{2}+a_n^{2}}'),
    ])
    s.move('The direction is not radial', [
        ('p', 'When a tangential component exists the total acceleration is tilted away from the centre, by an angle whose tangent is a_t over a_n. Only at constant speed does it point exactly at the centre.'),
        ('m', r'\tan\phi=\frac{a_t}{a_n}'),
        ('n', 'braking on a curve means the acceleration points backward and inward'),
    ])
    s.move('The reverse question', [
        ('p', 'Given the total acceleration and one component, recover the other and then the radius. This is the standard numerical form: a car has 13 m/s squared total and 5 m/s squared tangential at 10 m/s, so the normal part is 12 and the radius is 8.3 m.'),
        ('m', r'a_n=\sqrt{a^{2}-a_t^{2}},\qquad R=\frac{v^{2}}{a_n}'),
    ])
    s.chip('key', 'the two components', [
        ('m', r'a_t=\dot v,\qquad a_n=v^{2}/R'),
    ])
    s.chip('num', 'a check', [
        ('p', 'v = 10, a_t = 5, a = 13'),
        ('p', 'a_n = 12, R = 8.3 m'),
    ])
    s.chip('trap', 'using R from the total acceleration', [
        ('p', 'Only the normal component sets the radius. The tangential part does not bend the path at all.'),
    ])
    s.figure('at_an')
    S.append(s)

    # ============================================================ 16 VARIABLE ALPHA
    s = Sheet('Olympiad-16-variable-alpha', 'What if the angular acceleration is not constant?',
              'A wheel slows under a torque that falls with time. The three rotation equations fail. What replaces them?',
              KC, 16, total, SRCC + '§3.9, Q9',
              'integrate: omega is the area under alpha, theta the area under omega',
              stage='spin')
    s.move('Back to the definitions', [
        ('p', 'When alpha varies, go back to the derivatives. Integrating alpha over time gives the change in omega, and integrating omega gives the change in angle. Each integral is an area under a graph.'),
        ('m', r'\omega=\omega_0+\int_0^{t}\alpha\,dt,\qquad \theta=\theta_0+\int_0^{t}\omega\,dt'),
    ])
    s.move('The other chain', [
        ('p', 'If alpha is given as a function of the angle instead of the time, use the rotational twin of v dv/dx. It removes the clock and often turns a hard integral into an easy one.'),
        ('m', r'\omega\,d\omega=\alpha\,d\theta\quad\Rightarrow\quad \frac{1}{2}\omega^{2}=\int\alpha\,d\theta'),
        ('n', 'the same trick as a = v dv/dx, in rotation'),
    ])
    s.move('A worked shape', [
        ('p', 'For a wheel slowing under friction with alpha proportional to minus omega, the solution is exponential decay of the angular speed: each second removes the same fraction of what is left. That is the rotational analogue of linear drag.'),
        ('m', r'\alpha=-k\omega\ \Rightarrow\ \omega=\omega_0e^{-kt}'),
    ])
    s.chip('key', 'the integrals', [
        ('m', r'\omega=\int\alpha\,dt,\qquad \theta=\int\omega\,dt'),
    ])
    s.chip('gate', 'choose the variable', [
        ('p', 'alpha of time: integrate over t. alpha of angle: use omega d omega = alpha d theta.'),
    ])
    s.chip('trap', 'reusing omega_0 + alpha t', [
        ('p', 'That equation assumes constant alpha. Check before writing it, and if alpha is a function, integrate.'),
    ])
    s.figure('alpha_integral')
    S.append(s)

    # ============================================================ 17 RELATIVE ANGULAR
    s = Sheet('Olympiad-17-relative-angular', 'How fast do two points on a wheel separate?',
              'Two particles move on the same circle at different angular rates. How often do they meet, and what is their relative speed?',
              KC, 17, total, SRCC + '§3.7, Q19',
              'relative angular rate is the difference, and relative speed is that times the radius',
              stage='spin')
    s.move('Subtract the rates', [
        ('p', 'Both particles share the same circle, so their separation angle changes at the difference of the angular velocities. Meetings happen once per full relative revolution, which gives a period of 2 pi over the difference.'),
        ('m', r'\omega_{\mathrm{rel}}=\omega_1-\omega_2,\qquad T_{\mathrm{meet}}=\frac{2\pi}{|\omega_1-\omega_2|}'),
    ])
    s.move('Relative speed along the circle', [
        ('p', 'The separation grows along the arc, so the arc grows at the relative angular rate times the radius. For two independent particles on one circle this is the closing speed along the track; for two points of one rigid wheel the rates are equal and the gap never changes.'),
        ('m', r'v_{\mathrm{rel}}=R\,|\omega_1-\omega_2|'),
        ('n', 'a rigid wheel spins its points together: a shared rate means a fixed gap'),
    ])
    s.move('The same idea across frames', [
        ('p', 'If the whole circle is also rotating, add or subtract the frame rate first. This is the rotational version of relative velocity, and it is what makes gear trains and pulleys tractable: the contact points share a velocity, not a rate.'),
    ])
    s.chip('key', 'relative rotation', [
        ('m', r'T_{\rm meet}=2\pi/|\omega_1-\omega_2|'),
    ])
    s.chip('num', 'a check', [
        ('p', 'omega = 1.5 and 0.6 rad/s'),
        ('p', 'T_meet = 2 pi / 0.9 = 7.0 s'),
    ])
    s.chip('trap', 'adding the rates', [
        ('p', 'Same-direction rotation subtracts. Adding gives the answer for opposite directions.'),
    ])
    s.figure('relative_angular')
    S.append(s)

    # ============================================================ 18 WORK RADIAL
    s = Sheet('Olympiad-18-work-radial', 'If the centripetal force is always inward, how does anything speed up?',
              'On a vertical circle gravity has a tangential component; the tension never does. Which force changes the speed, and which only bends the path?',
              KC, 18, total, SRCC + '§3.8, §3.9',
              'a radial force does no work, so only the tangential component can change the speed',
              stage='spin')
    s.move('Perpendicular means zero work', [
        ('p', 'The centripetal force is along the radius and the displacement is along the tangent, so the dot product vanishes at every instant. It therefore cannot change the kinetic energy, which is why a car on a flat curve keeps a constant speed while its velocity turns.'),
        ('m', r'W_c=\int\mathbf{F}_c\cdot d\mathbf{r}=0'),
    ])
    s.move('Who speeds the body up', [
        ('p', 'Only the tangential component does work. On a vertical circle that is the tangential part of gravity, m g sin of the angle from the lowest point, so the work done by gravity is exactly minus the change in m g h. On a banked curve it is friction along the path.'),
        ('m', r'm\frac{dv}{dt}=F_{\mathrm{tangential}}=mg\sin\phi'),
    ])
    s.move('Why the two equations are separate', [
        ('p', 'The radial equation fixes the force needed for the instantaneous geometry; the tangential equation fixes how the speed evolves. Solving them in that order is the standard approach, and it is the reason energy can replace the tangential equation entirely.'),
        ('n', 'energy handles the tangential direction; the radial equation handles the normal one'),
    ])
    s.chip('key', 'the split', [
        ('p', 'radial: sets the path, no work. tangential: sets the speed, does the work.'),
    ])
    s.chip('trap', 'tension doing work', [
        ('p', 'For a string of fixed length the tension is perpendicular to the motion and does no work. A string that changes length, or a peg that moves, can.'),
    ])
    s.chip('insight', 'the energy shortcut', [
        ('p', 'Because the radial force is powerless, the whole tangential problem collapses to conservation of mechanical energy.'),
    ])
    s.figure('work_radial')
    S.append(s)

    # ============================================================ 19 VERTICAL ENERGY
    s = Sheet('Olympiad-19-vertical-circle-energy', 'What speed does a bead have at the top of a loop?',
              'A bead is released from rest at height h above the bottom of a smooth vertical loop. How fast is it at the top, and when does it leave the track?',
              KC, 19, total, SRCC + '§3.9, §3.10',
              'energy gives the speed at every angle; the track condition decides whether it stays on',
              stage='spin')
    s.move('Energy from the release point', [
        ('p', 'With no friction the speed at any angle follows from the height dropped. Measuring the angle from the bottom, the height gained is R times one minus cosine, and the speed follows directly.'),
        ('m', r'v^{2}=v_0^{2}-2gR\left(1-\cos\phi\right)'),
    ])
    s.move('The track condition', [
        ('p', 'For a bead on the inside of a track the normal must stay positive. Setting it to zero gives the minimum speed at each angle, and the most demanding point is the top, where gravity already supplies the whole centripetal requirement.'),
        ('m', r'N=\frac{mv^{2}}{R}+mg\cos\phi\ \ge0'),
        ('n', 'at the top cos phi = −1, so N = m v squared / R − m g'),
    ])
    s.move('The two thresholds', [
        ('p', 'For a full loop without leaving the track the top speed must satisfy v squared at least g R, which needs a release height of two and a half radii above the bottom. For a bead on a rod, or a bead threaded on a wire, there is no such condition and the minimum is only the height of the top.'),
        ('m', r'h_{\min}=2.5R\ \text{(track)},\qquad h_{\min}=2R\ \text{(rod)}'),
    ])
    s.chip('key', 'the pair', [
        ('m', r'v^{2}=v_0^{2}-2gR(1-\cos\phi)'),
        ('m', r'N=\frac{mv^{2}}{R}+mg\cos\phi'),
    ])
    s.chip('num', 'a check', [
        ('p', 'R = 0.8 m, released from rest at 2.5R'),
        ('p', 'v_top = sqrt(gR) = 2.8 m/s, N = 0 there'),
    ])
    s.chip('trap', 'using v = 0 at the top', [
        ('p', 'A bead on the inside of a track needs sqrt(gR) at the top, not zero. Zero is the rod answer.'),
    ])
    s.figure('vertical_energy')
    S.append(s)

    # ============================================================ 20 STRING VS ROD
    s = Sheet('Olympiad-20-string-vs-rod', 'Why must a string be launched faster than a rod?',
              'The same mass, radius and release height. On a string it must be launched at sqrt(5gR); on a rod, sqrt(4gR) is enough. Where does the difference come from?',
              KC, 20, total, SRCC + '§3.9, §4.1',
              'a string can only pull, so its tension must stay positive; a rod can push',
              stage='spin')
    s.move('The constraint is one-sided', [
        ('p', 'A string can pull but not push, so the tension must remain non-negative everywhere. A rod can supply either sign, so the only requirement is that the bead reaches the top with enough speed to keep going.'),
        ('m', r'T\ge0\ \text{(string)},\qquad N\ \text{any sign (rod)}'),
    ])
    s.move('Both boundary cases', [
        ('p', 'At the top of a string loop the tension just vanishes at the limiting speed, giving v squared equal to g R there and 5 g R at the bottom by energy. For a rod the limiting speed at the top is zero, which gives 4 g R at the bottom.'),
        ('m', r'v_{\mathrm{bot}}=\sqrt{5gR}\ \text{(string)},\qquad \sqrt{4gR}\ \text{(rod)}'),
        ('n', 'the factor sqrt(5/4) = 1.12 in speed is a factor 1.25 in energy'),
    ])
    s.move('What the tension does along the way', [
        ('p', 'For the string at the limiting launch speed the tension is zero at the top and 6 m g at the bottom. For the rod the normal force changes sign somewhere above the horizontal, and the bead is being pushed inward there rather than pulled.'),
        ('m', r'T_{\mathrm{bot}}=6mg\ \text{(string, limiting)},\qquad N_{\mathrm{top}}=-mg\ \text{(rod, limiting)}'),
    ])
    s.chip('key', 'the two minima', [
        ('m', r'v_{\rm bot}\ge\sqrt{5gR}\ \text{(string)},\quad \ge\sqrt{4gR}\ \text{(rod)}'),
    ])
    s.chip('num', 'a check', [
        ('p', 'R = 0.8 m: string 6.26 m/s, rod 4.85 m/s'),
        ('p', 'tensions at the bottom: 6mg and 5mg for the two limits'),
    ])
    s.chip('trap', 'the source 3mg', [
        ('p', 'The bottom tension at the limiting speed is 6mg, not 3mg. See the source audit for the corrected figure.'),
    ])
    s.figure('string_vs_rod')
    S.append(s)

    # ============================================================ 21 CONICAL
    s = Sheet('Olympiad-21-conical-pendulum', 'Why does a conical pendulum ignore the mass?',
              'A bob whirls in a horizontal circle on a string of length L at angle theta. The tension depends on the mass, yet the period does not. Why?',
              KC, 21, total, SRCC + '§3.7, §3.9',
              'the two force equations both carry m, so it cancels out of the geometry and the period',
              stage='spin')
    s.move('Two equations at once', [
        ('p', 'Vertically the vertical component of the tension balances the weight. Horizontally the horizontal component supplies the centripetal force. Divide one by the other and the mass and the tension both disappear.'),
        ('m', r'T\cos\theta=mg,\qquad T\sin\theta=\frac{mv^{2}}{L\sin\theta}'),
    ])
    s.move('What survives', [
        ('p', 'The division leaves the angle fixed by the speed, and the period depends only on the vertical length of the string. Every bob on the same string length and the same angle has the same period, whatever its mass.'),
        ('m', r'v^{2}=gL\sin\theta\tan\theta,\qquad T=2\pi\sqrt{\frac{L\cos\theta}{g}}'),
        ('n', 'the vertical projection L cos theta is the length that matters'),
    ])
    s.move('The limits', [
        ('p', 'As the angle goes to zero the motion becomes a small planar pendulum with period 2 pi root L over g. As the angle approaches 90 degrees the required speed diverges and the period falls to zero: the string becomes horizontal only at infinite speed.'),
        ('m', r'\theta\to0:\ T\to2\pi\sqrt{L/g},\qquad \theta\to90^{\circ}:\ v\to\infty'),
    ])
    s.chip('key', 'the conical pendulum', [
        ('m', r'T=2\pi\sqrt{L\cos\theta/g},\qquad v=\sqrt{gL\sin\theta\tan\theta}'),
    ])
    s.chip('num', 'a check', [
        ('p', 'L = 0.5 m, theta = 40°, m = 0.2 kg'),
        ('p', 'T = 1.24 s, v = 1.63 m/s, tension 2.56 N'),
    ])
    s.chip('trap', 'using L in the period', [
        ('p', 'The period uses L cos theta, the vertical drop, not the string length.'),
    ])
    s.figure('conical_energy')
    S.append(s)

    # ============================================================ 22 BANKED
    s = Sheet('Olympiad-22-banked-limits', 'What is the slowest safe speed on a banked corner?',
              'Banking is designed for one speed. Too fast and the car slides up; too slow and it slides down. What sets both limits?',
              KC, 22, total, SRCC + '§3.9, §3.10',
              'friction can only widen the band around the design speed; it cannot create one',
              stage='spin')
    s.move('Design speed', [
        ('p', 'With no friction the normal force alone must supply the centripetal force, and resolving along and perpendicular to the bank gives the design condition.'),
        ('m', r'\tan\theta=\frac{v_0^{2}}{Rg}'),
    ])
    s.move('The two extremes', [
        ('p', 'At the maximum speed friction points down the slope, helping the bank turn the car. At the minimum it points up the slope, stopping the car sliding down. Both come from the same resolution with the sign of friction flipped.'),
        ('m', r'v_{\max}^{2}=Rg\frac{\sin\theta+\mu\cos\theta}{\cos\theta-\mu\sin\theta}'),
        ('m', r'v_{\min}^{2}=Rg\frac{\sin\theta-\mu\cos\theta}{\cos\theta+\mu\sin\theta}'),
    ])
    s.move('Read the structure', [
        ('p', 'Both reduce to tan theta when mu vanishes, the design speed. The maximum grows without bound as mu approaches cot theta, while the minimum falls to zero once mu exceeds tan theta.'),
        ('m', r'\mu>\tan\theta\ \Rightarrow\ v_{\min}=0'),
        ('n', 'the band is asymmetric: friction helps much more at the fast end'),
    ])
    s.chip('key', 'the band', [
        ('m', r'v_{\max}^{2}=Rg\frac{\sin\theta+\mu\cos\theta}{\cos\theta-\mu\sin\theta}'),
        ('p', 'and the min with the signs flipped'),
    ])
    s.chip('num', 'a check', [
        ('p', 'R = 80, theta = 27°, mu = 0.35'),
        ('p', 'v: 10.3 to 28.6 m/s, design 20 m/s'),
    ])
    s.chip('trap', 'one formula for both', [
        ('p', 'The friction direction flips at the design speed. Using one form for both limits gives a wrong minimum.'),
    ])
    s.figure('bank_limits')
    S.append(s)

    # ============================================================ 23 ROTOR
    s = Sheet('Olympiad-23-rotor-wall', 'How does a wall of death hold a rider up?',
              'A rider circles the inside of a vertical cylinder. The wall is vertical and there is no floor under the tyres. What holds the weight?',
              KC, 23, total, SRCC + '§3.8, §3.9',
              'the normal provides the centripetal force, and static friction on the vertical wall carries the weight',
              stage='spin')
    s.move('Two perpendicular jobs', [
        ('p', 'The normal force is horizontal, points at the axis, and provides the centripetal force. Friction is vertical and holds the weight. Neither can do the other job, so the two equations are independent.'),
        ('m', r'N=\frac{mv^{2}}{R},\qquad f=mg'),
    ])
    s.move('The minimum speed', [
        ('p', 'Static friction has a ceiling proportional to the normal. Substituting the two equations gives the minimum speed at which the wall can still hold the rider, and it falls as the friction coefficient grows.'),
        ('m', r'\mu_s\frac{mv^{2}}{R}\ge mg\quad\Rightarrow\quad v_{\min}=\sqrt{\frac{gR}{\mu_s}}'),
        ('n', 'a smaller cylinder, or a stickier wall, lowers the required speed'),
    ])
    s.move('Why the rider feels heavy', [
        ('p', 'At the minimum speed the friction is exactly at its limit, so any bump or lean that reduces the normal drops the rider. That is why the manoeuvre is done at well above the minimum, and why the normal force on the rider can be several times the weight.'),
    ])
    s.chip('key', 'the rotor', [
        ('m', r'v_{\min}=\sqrt{gR/\mu_s}'),
        ('p', 'normal horizontal, friction vertical'),
    ])
    s.chip('num', 'a check', [
        ('p', 'R = 4 m, mu_s = 0.4'),
        ('p', 'v_min = sqrt(98) = 9.9 m/s, about 36 km/h'),
    ])
    s.chip('trap', 'friction supplying the centre', [
        ('p', 'On a vertical wall friction cannot point at the axis. The normal does that; friction is vertical.'),
    ])
    s.figure('rotor_wall')
    S.append(s)

    # ============================================================ 24 CURVATURE
    s = Sheet('Olympiad-24-curvature', 'How tight is a curve that is not a circle?',
              'A projectile path, a roller-coaster dip, a road bend: none is a circle. What is the radius at a point?',
              KC, 24, total, SRCC + '§3.10, Q16',
              'the radius of curvature is the circle that matches the path locally, and v squared over it is the normal acceleration',
              stage='spin')
    s.move('Define it by the normal acceleration', [
        ('p', 'At any point of any smooth path there is one circle that matches it to second order. Its radius is the radius of curvature, and the normal component of acceleration is v squared over that radius.'),
        ('m', r'\rho=\frac{v^{2}}{a_\perp}'),
    ])
    s.move('Projectile values worth knowing', [
        ('p', 'At the apex the velocity is horizontal and the whole of g is normal, so the radius is v squared over g with the horizontal speed. At launch the normal component is g cos theta, which gives a larger radius.'),
        ('m', r'\rho_{\mathrm{apex}}=\frac{v_0^{2}\cos^{2}\theta}{g},\qquad \rho_{\mathrm{launch}}=\frac{v_0^{2}}{g\cos\theta}'),
        ('n', 'for a vertical launch the path is straight and the radius is infinite'),
    ])
    s.move('The general formula', [
        ('p', 'For a path given as y of x, the radius follows from the first and second derivatives. A straight line has zero second derivative and infinite radius; a sharp bend has a large second derivative and a small radius.'),
        ('m', r'\rho=\frac{\left(1+y_{x}^{2}\right)^{3/2}}{\left|y_{xx}\right|}'),
        ('n', 'at the apex of a parabola y double dash is g over v_x squared, which reproduces the result above'),
    ])
    s.chip('key', 'curvature', [
        ('m', r'\rho=v^{2}/a_\perp'),
        ('p', 'and rho = (1 + y_x^2)^(3/2) / |y_xx| for a graph'),
    ])
    s.chip('num', 'a check', [
        ('p', '20 m/s at 45°: apex rho = 200/9.8 = 20.4 m'),
        ('p', 'launch rho = 400/(9.8 x 0.707) = 57.7 m'),
    ])
    s.chip('trap', 'using the full speed at the apex', [
        ('p', 'The apex speed is v0 cos theta, not v0. Using v0 overstates the radius by 1/cos² theta.'),
    ])
    s.figure('curvature_fit')
    S.append(s)
    return S

    return S
