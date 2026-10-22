"""Part II content: Olympiad and extension material for Newton's laws.

Each page takes one result that is outside the routine JEE drill — a variable
mass problem, a rotating frame, a friction hitch — and carries it end to end.
Sources: newtons-laws/Newtons-laws.md  §3.9-3.14, OL1-OL10, D5.1-D5.12.
"""
from layout import Sheet

K = "NEWTON'S LAWS  /  PART II: OLYMPIAD + EXTENSIONS"
SRC = 'source: Newtons-laws.md '


def build(total):
    S = []

    # ============================================================ 1 TURNTABLE
    s = Sheet('Olympiad-01-turntable-string', 'Is there friction on a block tied to the axis?',
              'A block on a turntable is tied by a string to the centre and the table spins fast. Is the friction zero, or maximum?',
              K, 1, total, SRC + '§3.12, OL7',
              'the string and friction share one job, so each takes only what it must',
              stage='spin')
    s.move('First ask what the motion needs', [
        ('p', 'The block travels a circle of radius r at angular speed ω, so it needs an inward force mω²r. That requirement is fixed by the kinematics and has nothing to do with which agent supplies it.'),
        ('m', r'F_{\mathrm{in}}=m\omega^{2}r'),
    ])
    s.move('Two suppliers, one budget', [
        ('p', 'Without the string the only inward force is friction, so f = mω²r and the block slips when that exceeds μ_s mg. With a taut string, the string can carry the whole requirement and friction falls to zero.'),
        ('m', r'T+f=m\omega^{2}r'),
        ('n', 'a string that is taut and radial does not need help from friction'),
    ])
    s.move('Both frames must agree', [
        ('p', 'In the rotating frame the block is at rest with a centrifugal term mω²r outward. The string pulls inward, friction adjusts to whatever is left, and equilibrium gives the same answer. The frames agree because they must.'),
    ])
    s.chip('def', 'the budget rule', [
        ('p', 'Compute the required inward force first. Then share it between the agents present, in the order they can act.'),
    ])
    s.chip('trap', '"friction always opposes motion"', [
        ('p', 'Here friction would have to point inward, with the motion, to keep the block in its circle. It is a centripetal supplier, not a drag.'),
    ])
    s.chip('insight', 'why the puzzle exists', [
        ('p', 'Students assume friction must be doing something because the surface is rough and spinning. It is doing nothing: the string has already met the requirement.'),
    ])
    s.figure('turntable')
    S.append(s)

    # ============================================================ 2 LIMIT
    s = Sheet('Olympiad-02-turntable-limit', 'Why does a coin and a brick slip at the same speed?',
              'Two objects of very different mass sit at the same radius on a spinning turntable. Which one slides off first?',
              K, 2, total, SRC + '§3.12, OL7, Q24',
              'the friction limit is proportional to mass, so mass cancels out of the slip condition',
              stage='spin')
    s.move('Set the requirement equal to the ceiling', [
        ('p', 'Contact survives while friction can supply the centripetal requirement. Both sides carry a factor m, so the mass drops out of the inequality entirely.'),
        ('m', r'm\omega^{2}r\le\mu_s mg\ \Rightarrow\ \omega\le\sqrt{\frac{\mu_s g}{r}}'),
    ])
    s.move('So the outer edge goes first', [
        ('p', 'At fixed ω the limit is a radius: everything inside r_c stays, everything outside leaves. That is why a record on a turntable throws the dust at its rim, and why a coin placed further out survives a shorter spin-up.'),
        ('m', r'r_c=\frac{\mu_s g}{\omega^{2}}'),
    ])
    s.move('What breaks the tie', [
        ('p', 'Mass cancels only because both the requirement and the ceiling are proportional to it. Tilt the table, or add a string, or make one object tall enough to topple, and the cancellation is gone.'),
        ('n', 'a tall block topples before it slides: that is a torque condition, not a force one'),
    ])
    s.chip('key', 'the limit', [
        ('m', r'\omega_{\max}=\sqrt{\mu_s g/r}'),
        ('m', r'r_c=\mu_s g/\omega^{2}'),
    ])
    s.chip('num', 'a check', [
        ('p', 'μ_s = 0.3, r = 0.5 m'),
        ('p', 'ω_max = 2.42 rad/s'),
        ('p', 'mass never enters'),
    ])
    s.chip('trap', 'heavier sticks better', [
        ('p', 'It does not. The heavier object needs more inward force, and gets exactly proportionally more friction ceiling.'),
    ])
    s.figure('turntable_limit')
    S.append(s)

    # ============================================================ 3 WEDGE CONSTRAINT
    s = Sheet('Olympiad-03-wedge-constraint', 'Why is the block\'s acceleration not along the face?',
              'A wedge slides on a table and a block slides down its face. You know both motions are linked, but how?',
              K, 3, total, SRC + '§3.10, D5.10, Q24',
              'a contact is a coordinate constraint first and a force second',
              stage='linked')
    s.move('Write the constraint in coordinates', [
        ('p', 'Fix a lab frame. The block\'s horizontal position is the wedge position plus its offset along the face; its height depends only on how far it has slid. One parameter, s, describes the block.'),
        ('m', r'x_b=x_w-s\cos\theta,\qquad y_b=y_0-s\sin\theta'),
    ])
    s.move('Differentiate twice', [
        ('p', 'The constraint is linear in the coordinates, so differentiating twice gives the same relation between accelerations. There is nothing to guess: the accelerations are locked by geometry.'),
        ('m', r'a_{bx}=a_w-a_{s}\cos\theta,\qquad a_{by}=-a_s\sin\theta'),
    ])
    s.move('Then let the forces do their job', [
        ('p', 'Only when the kinematics is written down do the equations close: the normal force is the one unknown interaction, and the wedge\'s own acceleration is driven by its horizontal component. For a smooth wedge and block released from rest,'),
        ('m', r'a_w=-\frac{mg\sin\theta\cos\theta}{M+m\sin^{2}\theta}'),
        ('n', 'the wedge runs opposite to the block\u2019s horizontal slide, and the sign is worth checking'),
    ])
    s.chip('gate', 'the order of operations', [
        ('p', '1 coordinates  2 constraint  3 differentiate  4 forces  5 solve'),
        ('p', 'Writing forces first is what produces the wrong signs.'),
    ])
    s.chip('key', 'results for a smooth wedge', [
        ('m', r'a_{\mathrm{rel}}=\frac{(M+m)g\sin\theta}{M+m\sin^{2}\theta}'),
    ])
    s.chip('trap', 'assuming a_block along the face', [
        ('p', 'In the lab frame the block does not move along the face: the face itself is moving. Only the relative acceleration is along the face.'),
    ])
    s.figure('wedge_constraint')
    S.append(s)

    # ============================================================ 4 EFFECTIVE G
    s = Sheet('Olympiad-04-effective-gravity', 'What is g inside a lift, a car, a centrifuge?',
              'A pendulum in an accelerating vehicle keeps time differently. How much, and in which direction does it hang?',
              K, 4, total, SRC + '§3.11, E9, C12',
              'g_eff is the vector sum of gravity and the frame acceleration, taken with a minus sign',
              stage='pseudo')
    s.move('One vector replaces gravity', [
        ('p', 'In a frame accelerating at a₀ every body feels a pseudo acceleration −a₀. Combine it with g and the pair behaves exactly like a new, stronger, tilted gravity.'),
        ('m', r'\vec g_{\mathrm{eff}}=\vec g-\vec a_0,\qquad |\vec g_{\mathrm{eff}}|=\sqrt{g^{2}+a_0^{2}}'),
    ])
    s.move('Everything follows from the new g', [
        ('p', 'A plumb line hangs along g_eff, a water surface is perpendicular to it, and a pendulum swings with the period set by its magnitude. Nothing else changes.'),
        ('m', r'T=2\pi\sqrt{\frac{L}{g_{\mathrm{eff}}}}=T_0\left(1+\frac{a_0^{2}}{g^{2}}\right)^{-1/4}'),
        ('n', 'at a₀ = g the period is 0.84 T₀ — the same factor as √2 to the power −1/2'),
    ])
    s.move('The lift cases', [
        ('p', 'Upward acceleration adds to g, downward subtracts, free fall zeroes it. In free fall a pendulum does not swing at all, because there is no "down" left inside the cabin.'),
    ])
    s.chip('key', 'vector rule', [
        ('m', r'\vec g_{\mathrm{eff}}=\vec g-\vec a_0'),
        ('m', r'T=T_0\left(1+a_0^{2}/g^{2}\right)^{-1/4}'),
    ])
    s.chip('num', 'the 0.84', [
        ('p', 'a₀ = g: g_eff = 1.414 g'),
        ('p', 'T = 0.84 T₀'),
    ])
    s.chip('trap', 'scalar addition', [
        ('p', 'g and a₀ add as vectors. Only in the lift (vertically aligned) may you add or subtract their magnitudes.'),
    ])
    s.figure('effective_g')
    S.append(s)

    # ============================================================ 5 WEDGE LIFTOFF
    s = Sheet('Olympiad-05-wedge-liftoff', 'When does a block leave a wedge that is pulled away?',
              'The wedge is yanked horizontally out from under a block resting on its face. At what acceleration does contact break?',
              K, 5, total, SRC + '§3.13, Q24, D5.10',
              'contact survives only while the normal force remains positive',
              stage='pseudo')
    s.move('Use the wedge frame', [
        ('p', 'In the wedge frame the block feels its weight, the pseudo force ma₀ opposite the pull, and the normal. Resolve perpendicular to the face: that direction has no acceleration while contact lasts.'),
        ('m', r'N=mg\cos\theta-ma_0\sin\theta'),
    ])
    s.move('Contact dies at N = 0', [
        ('p', 'A normal force cannot be negative. Setting N to zero gives the threshold acceleration, and beyond it the block leaves the surface and becomes a projectile in the lab frame.'),
        ('m', r'a_0=g\cot\theta'),
        ('n', 'θ = 30°: threshold 1.73g'),
    ])
    s.move('The first instant after liftoff', [
        ('p', 'At the threshold the block\'s acceleration perpendicular to the face is exactly the free-fall component, so it just separates. The lab-frame description switches from constrained motion to projectile motion at that instant.'),
    ])
    s.chip('key', 'threshold', [
        ('m', r'N=mg\cos\theta-ma_0\sin\theta'),
        ('m', r'a_0=g\cot\theta\ \mathrm{for liftoff}'),
    ])
    s.chip('trap', 'pulling toward the face', [
        ('p', 'Accelerate the wedge into the block and N rises. Only pulling the surface away from the block can make N fall.'),
    ])
    s.chip('check', 'θ near 90 degrees', [
        ('p', 'A vertical face needs an enormous pull to separate the block: a₀ → 0 as θ → 90°, which is the sense of cotθ.'),
    ])
    s.figure('wedge_liftoff')
    S.append(s)

    # ============================================================ 6 VIRTUAL WORK
    s = Sheet('Olympiad-06-virtual-work', 'Why can you ignore the normal force in a work calculation?',
              'A constraint force can be large, yet contributes nothing to the energy bookkeeping. Why exactly?',
              K, 6, total, SRC + '§3.10, D5.10, Q24',
              'a constraint force perpendicular to the allowed displacement does no work',
              stage='linked')
    s.move('Displacement allowed by the constraint', [
        ('p', 'Give the system a small imaginary displacement that respects the constraints. The normal force is perpendicular to the surface, and the sliding is along it, so the dot product vanishes.'),
        ('m', r'\delta W=N\cdot\delta s=0'),
    ])
    s.move('The wedge, solved without forces', [
        ('p', 'The block stays on the face, so its vertical displacement is zero to first order while it slides. Setting the total virtual work of gravity to zero gives the relation between the wedge displacement and the slide directly.'),
        ('m', r'\delta y_b=\delta x_w\cos\theta-\delta s\sin\theta=0'),
        ('n', 'one equation, and no free-body diagram at all'),
    ])
    s.move('Where the method pays', [
        ('p', 'Linked systems with several constraints: the internal forces never appear, so the number of equations collapses. The price is that you must write the kinematics correctly — the method is intolerant of a wrong sign.'),
    ])
    s.chip('gate', 'when to use it', [
        ('p', 'Equilibrium or energy questions in a linked system, where you want a relation between displacements rather than internal forces.'),
    ])
    s.chip('trap', 'friction is not a constraint force', [
        ('p', 'Friction along the surface does work, and the work is negative. Virtual work only deletes the ideal constraints: normals and taut ropes.'),
    ])
    s.chip('insight', 'the deep reason', [
        ('p', 'Constraint forces are defined to be perpendicular to the allowed motion. That single geometric fact is why energy methods are shorter than force methods.'),
    ])
    s.figure('virtual_work')
    S.append(s)

    # ============================================================ 7 ROPE TABLE
    s = Sheet('Olympiad-07-rope-over-edge', 'At what length does a rope over an edge start to slide?',
              'A rope lies on a rough table with length x hanging over the edge. How much must hang before it moves?',
              K, 7, total, SRC + '§3.9, Q12',
              'the hanging fraction must beat friction on the part still on the table',
              stage='linked')
    s.move('Two weights, one friction', [
        ('p', 'Model the rope as linear density λ. The hanging part pulls with λxg; the part on the table is held by friction up to μλ(L−x)g. Motion begins when the pull beats the ceiling.'),
        ('m', r'\lambda xg=\mu\lambda(L-x)g'),
    ])
    s.move('Solve for the fraction', [
        ('p', 'The density cancels, which is why the answer is a pure geometry statement: a rope starts to slide when the hanging fraction reaches μ/(1+μ).'),
        ('m', r'\frac{x}{L}=\frac{\mu}{1+\mu}'),
        ('n', 'μ = 0.4: a little over 28 % must hang'),
    ])
    s.move('Once it moves', [
        ('p', 'Friction is now kinetic and the driving weight grows as more rope goes over, so the acceleration increases with x. The motion is not uniform, and energy is the easier route to the speed.'),
        ('m', r'a=\frac{g\left[x-\mu_k(L-x)\right]}{L}'),
    ])
    s.chip('key', 'threshold', [
        ('m', r'x/L=\mu_s/(1+\mu_s)'),
    ])
    s.chip('num', 'values', [
        ('p', 'μ_s = 0.2: 16.7 %'),
        ('p', 'μ_s = 0.4: 28.6 %'),
        ('p', 'smooth table: any length moves it'),
    ])
    s.chip('trap', 'using the whole weight', [
        ('p', 'Friction acts only on the part still on the table. Using the full weight λLg overstates the ceiling and predicts no motion.'),
    ])
    s.figure('rope_table')
    S.append(s)

    # ============================================================ 8 FALLING CHAIN
    s = Sheet('Olympiad-08-falling-chain', 'Does a falling chain weigh three times as much?',
              'A chain is dropped so that it lands in a heap on a scale. At the instant the last link lands, what does the scale read?',
              K, 8, total, SRC + '§3.14, OL1 (answer corrected)',
              'a landing chain must be stopped as well as held: three times the landed weight',
              stage='one')
    s.move('Two jobs, two terms', [
        ('p', 'The scale supports the weight of what has already landed and also destroys the momentum of what is arriving. Both are forces on the scale, so they add.'),
        ('m', r'F=\lambda xg+\dot m\,v=\lambda xg+\lambda v^{2}'),
    ])
    s.move('Use free fall to eliminate v', [
        ('p', 'The moving part has fallen a distance x, so v² = 2gx. Substitute and the momentum term becomes twice the weight of the pile, whatever x is.'),
        ('m', r'F=\lambda xg+2\lambda xg=3\lambda xg'),
        ('n', 'at the instant the last link lands, x = L and F = 3mg'),
    ])
    s.move('Why the printed answer says 2mg', [
        ('p', 'The source computes only the momentum flux, or only the weight, at the final instant and reports 2mg. The correct bookkeeping has both terms present simultaneously, so the reading is 3mg. This is the one place where the edition deliberately departs from the source; see SOURCE-AUDIT.'),
    ])
    s.chip('key', 'the two terms', [
        ('m', r'F=\lambda gx+\lambda v^{2}'),
        ('m', r'v^{2}=2gx\ \Rightarrow\ F=3\lambda gx'),
    ])
    s.chip('trap', 'dropping a term at the end', [
        ('p', 'At the final instant neither term vanishes. The pile still has weight and the last link still has momentum to lose.'),
    ])
    s.chip('insight', 'the general pattern', [
        ('p', 'Any process that catches mass gives weight plus momentum flux. The same two terms give 3mg here and λv² in the lifting problem.'),
    ])
    s.figure('falling_chain')
    S.append(s)

    # ============================================================ 9 ROCKET
    s = Sheet('Olympiad-09-rocket-equation', 'Why is the cost of speed logarithmic?',
              'A rocket reaches 9 km/s with an exhaust speed of 3 km/s. Why must it be mostly fuel, and how much?',
              K, 9, total, SRC + '§3.14, OL2',
              'each unit of speed costs a fixed ratio of mass, so speed grows as a logarithm',
              stage='one')
    s.move('Momentum balance in the rocket frame', [
        ('p', 'In the instantaneous rest frame the rocket throws mass backward at v_e. Momentum conservation over one small burn gives the differential relation.'),
        ('m', r'm\,dv=-v_e\,dm\ \Rightarrow\ dv=-v_e\frac{dm}{m}'),
    ])
    s.move('Integrate', [
        ('p', 'The right side integrates to a logarithm, which is the whole reason rockets are staged. Equal steps of speed cost equal ratios of mass, not equal masses.'),
        ('m', r'\Delta v=v_e\ln\frac{m_0}{m_f}'),
        ('m', r'\frac{m_0}{m_f}=e^{\Delta v/v_e}'),
    ])
    s.move('Put in the numbers', [
        ('p', 'Nine kilometres per second with a three kilometre per second exhaust needs a mass ratio of e³ ≈ 20. Nineteen twentieths of the launch mass is propellant, before any structure or payload.'),
        ('m', r'\frac{m_0}{m_f}=e^{3}\approx20'),
        ('n', 'burning half the mass gives only 0.693 v_e, not half of the maximum'),
    ])
    s.chip('key', 'the equation', [
        ('m', r'\Delta v=v_e\ln(m_0/m_f)'),
    ])
    s.chip('num', 'ratios worth knowing', [
        ('p', 'half the mass burned: 0.693 v_e'),
        ('p', '90 % burned: 2.30 v_e'),
        ('p', '99 % burned: 4.61 v_e'),
    ])
    s.chip('trap', 'averaging speeds', [
        ('p', 'You cannot average the exhaust speed over the burn; the rocket is lighter later, so late mass counts more. That is exactly what the logarithm encodes.'),
    ])
    s.figure('rocket_ratio')
    S.append(s)

    # ============================================================ 10 SAND BELT
    s = Sheet('Olympiad-10-sand-conveyor', 'Why does a conveyor belt need twice the power?',
              'Sand falls vertically onto a belt moving at constant speed. The belt\'s motor supplies power. Where does it go?',
              K, 10, total, SRC + '§3.14, OL4',
              'half the power becomes kinetic energy, half is lost to friction while the sand slips',
              stage='one')
    s.move('Force from momentum flux', [
        ('p', 'The sand arrives with no horizontal momentum and leaves with v. The belt must supply momentum at rate ṁv, so the force it exerts is ṁv.'),
        ('m', r'F=\frac{dp}{dt}=\dot m v'),
    ])
    s.move('Power in, energy out', [
        ('p', 'The belt moves at v, so the motor supplies P = Fv = ṁv². But the sand only gains kinetic energy at rate ½ṁv² — the energy equation has a gap.'),
        ('m', r'P_{\mathrm{motor}}=\dot m v^{2},\qquad \dot K=\frac{1}{2}\dot m v^{2}'),
        ('n', 'the missing half is dissipated as the sand slips on the belt before it grips'),
    ])
    s.move('Where the heat comes from', [
        ('p', 'The sand slides relative to the belt until it is up to speed. Kinetic friction at the interface does work on the sand, and the sliding itself generates heat. The bookkeeping closes exactly at half.'),
        ('m', r'Q=\frac{1}{2}\dot m v^{2}'),
    ])
    s.chip('key', 'three rates', [
        ('m', r'F=\dot m v'),
        ('m', r'P=\dot m v^{2}'),
        ('m', r'\dot K=\frac{1}{2}\dot m v^{2}'),
    ])
    s.chip('trap', 'efficiency of 50 % is not a fault', [
        ('p', 'No belt can do better while the sand slips. To approach 100 % you must accelerate the sand gently on a slower belt first.'),
    ])
    s.chip('insight', 'same algebra elsewhere', [
        ('p', 'Rope picked up from the floor, chain landing on a scale, water hitting a wall: all have a momentum-flux force and a factor-of-two energy story.'),
    ])
    s.figure('sand_belt')
    S.append(s)

    # ============================================================ 11 CHAIN LIFT
    s = Sheet('Olympiad-11-chain-lift', 'Why does lifting a chain cost more than its weight?',
              'A chain is pulled up from a heap at constant speed. The force is larger than the weight of the hanging part. By how much?',
              K, 11, total, SRC + '§3.14, OL6',
              'lifting at constant speed still costs a momentum-flux force, lambda v squared',
              stage='one')
    s.move('Two terms again', [
        ('p', 'The lifted length x has weight λxg. New links are being started from rest at the rate λv, and each must be given speed v, so an extra force λv² is needed.'),
        ('m', r'F=\lambda xg+\lambda v^{2}'),
    ])
    s.move('Power and the excess', [
        ('p', 'The power delivered is Fv. Of that, λxgv raises potential energy and λv³ goes into kinetic energy of freshly moving links. Since those links end up with ½λv³ each second, the other half of the flux term is lost to the inelastic jerk.'),
        ('m', r'P=Fv=\lambda xgv+\lambda v^{3},\qquad \dot K_{\mathrm{new}}=\frac{1}{2}\lambda v^{3}'),
    ])
    s.move('Accelerating as well', [
        ('p', 'If v is not constant there is a third term from the changing speed of the already lifted part. Constant speed isolates the momentum flux, which is why textbooks specify it.'),
    ])
    s.chip('key', 'the force', [
        ('m', r'F=\lambda gx+\lambda v^{2}'),
    ])
    s.chip('num', 'a check', [
        ('p', 'λ = 0.4 kg/m, v = 1.5 m/s, x = 3 m'),
        ('p', 'weight 11.8 N, flux 0.9 N, total 12.7 N'),
    ])
    s.chip('trap', 'constant speed means constant force', [
        ('p', 'The force is constant in v but grows with x. A graph of F against x is a straight line offset above the weight line.'),
    ])
    s.figure('chain_lift')
    S.append(s)

    # ============================================================ 12 CAPSTAN
    s = Sheet('Olympiad-12-capstan', 'Why can one hand hold a ship?',
              'A rope takes two turns round a bollard and a small force holds a huge one. What is the law, and where does the ratio come from?',
              K, 12, total, SRC + '§3.14, OL3',
              'every radian of wrap multiplies the grip by e to the mu theta',
              stage='contact')
    s.move('A small element of rope', [
        ('p', 'Take a piece subtending dθ. The tension changes by dT across it, and the normal force on the element is T dθ. Friction can supply at most μ times that normal, so the tension can only change gradually.'),
        ('m', r'dT=\mu T\,d\theta'),
    ])
    s.move('Integrate round the wrap', [
        ('p', 'The differential equation separates, and the solution is exponential in the wrap angle. That is why the effect explodes with turns: 2π radians is already a factor of e^{2πμ}.'),
        ('m', r'\frac{T_2}{T_1}\le e^{\mu\theta},\qquad \theta=2\pi N'),
        ('n', 'μ = 0.3, one turn: a factor of 6.6'),
    ])
    s.move('Why diameter does not matter', [
        ('p', 'The radius cancels out of the derivation: a thin carabiner and a thick bollard hold equally well for the same μ and the same angle. Only the total wrap and the surface matter.'),
    ])
    s.chip('key', 'the capstan law', [
        ('m', r'T_2=T_1e^{\mu\theta}'),
        ('m', r'\theta=2\pi N'),
    ])
    s.chip('num', 'turns', [
        ('p', 'one turn (μ = 0.3): 6.6 : 1'),
        ('p', 'two turns: 43 : 1'),
        ('p', 'three turns: 287 : 1'),
    ])
    s.chip('trap', 'the rope must not slip', [
        ('p', 'The exponential is an upper bound, attained only at the point of slipping. Below it the ratio can be anything smaller.'),
    ])
    s.figure('capstan')
    S.append(s)

    # ============================================================ 13 HITCH
    s = Sheet('Olympiad-13-friction-hitch', 'How does a friction hitch hold a falling climber?',
              'A rope wrapped round a carabiner holds with a small hand force. How many turns does it take to turn 1 into 10, and into 300?',
              K, 13, total, SRC + '§3.14, OL10',
              'the hitch holds because tension decays exponentially along the wrap',
              stage='contact')
    s.move('Same law, inverted', [
        ('p', 'The capstan relation applies unchanged: the hand holds the low-tension end and the load is the high-tension end. Solve for the wrap needed at a given ratio.'),
        ('m', r'\theta=\frac{1}{\mu}\ln\frac{T_2}{T_1},\qquad N=\frac{\theta}{2\pi}'),
    ])
    s.move('Numbers for a real rope', [
        ('p', 'With μ = 0.3, a factor of ten needs 1.22 turns; a factor of 287 needs three. The curve is logarithmic, so the first turn buys most of the available holding power.'),
        ('m', r'N=\frac{\ln 10}{2\pi(0.3)}=1.22\ \mathrm{turns}'),
        ('n', 'three turns at μ = 0.3: e^{5.66} = 287'),
    ])
    s.move('Why hitches fail in the wet', [
        ('p', 'Water or ice drops μ, and the ratio is exponential in μ, so a small loss of grip is a large loss of holding. That is why the same number of turns is safe on dry nylon and marginal on a wet rope.'),
    ])
    s.chip('key', 'turns for a ratio', [
        ('m', r'N=\frac{\ln(T_2/T_1)}{2\pi\mu}'),
    ])
    s.chip('num', 'μ = 0.3', [
        ('p', '10 : 1 at 1.22 turns'),
        ('p', '100 : 1 at 2.44 turns'),
        ('p', '287 : 1 at 3 turns'),
    ])
    s.chip('insight', 'why it feels like magic', [
        ('p', 'The hand only sets the low-tension end. Friction along the wrap does the holding, and it grows exponentially rather than linearly.'),
    ])
    s.figure('hitch_turns')
    S.append(s)

    # ============================================================ 14 STAGING
    s = Sheet('Olympiad-14-staging', 'Why does staging beat one big tank?',
              'Two rockets carry the same fuel and the same structure, but one drops an empty stage. How much speed does that buy?',
              K, 14, total, SRC + '§3.14, OL8',
              'staging wins by throwing away dead structure before the next burn',
              stage='one')
    s.move('The rocket equation is multiplicative', [
        ('p', 'Speed adds across stages while mass ratios multiply. Dropping dry structure raises the mass ratio of the second burn, and the logarithm turns that into extra speed.'),
        ('m', r'\Delta v=v_e\ln\frac{m_{0}}{m_{1}}+v_e\ln\frac{m_{1}^{\prime}}{m_{f}}'),
    ])
    s.move('A worked comparison', [
        ('p', 'Launch 1000 kg with 800 kg of fuel, 100 kg payload and two 50 kg stages, exhaust 2 km/s. One stage must carry both dry masses to the end; two stages drop one of them halfway.'),
        ('m', r'\mathrm{two stages: }2\ln\frac{1000}{600}+2\ln\frac{550}{150}=1.02+2.60=3.62'),
        ('m', r'\mathrm{one stage: }2\ln\frac{1000}{200}=3.22\ \mathrm{km/s}'),
        ('n', '0.40 km/s for free, from the same fuel and the same hardware'),
    ])
    s.move('Why not infinitely many stages', [
        ('p', 'Each stage adds its own dry mass and its own engine. Beyond a few stages the structure you add costs more than the dead mass you drop, so real vehicles settle at two or three.'),
    ])
    s.chip('key', 'the sum', [
        ('m', r'\Delta v=v_e\sum_i\ln\frac{m_{0,i}}{m_{f,i}}'),
    ])
    s.chip('num', 'the worked case', [
        ('p', 'stage 1: 1000 → 600 kg, 1.02 km/s'),
        ('p', 'stage 2: 550 → 150 kg, 2.60 km/s'),
        ('p', 'single stage: 3.22 km/s'),
    ])
    s.chip('trap', 'adding speeds without dropping mass', [
        ('p', 'If the empty stage is carried to the end, staging buys nothing at all. The gain is entirely from the drop.'),
    ])
    s.figure('staging')
    S.append(s)

    # ============================================================ 15 IMPULSE WINDOW
    s = Sheet('Olympiad-15-impulse-window', 'When is it safe to ignore gravity during a hit?',
              'A bat hits a ball for about a millisecond. Gravity never switches off — so why does every solution drop it?',
              K, 15, total, SRC + '§3.14, OL9',
              'a force that is huge for a millisecond makes gravity irrelevant',
              stage='one')
    s.move('Compare impulses, not forces', [
        ('p', 'Gravity acts the whole time, but its impulse over the contact window is tiny compared with the bat\'s. What matters for the velocity change is the integral, so the ratio of impulses is the test.'),
        ('m', r'\frac{J_g}{J_{\mathrm{bat}}}=\frac{mg\,\Delta t}{J_{\mathrm{bat}}}'),
    ])
    s.move('Put in the numbers', [
        ('p', 'A 0.145 kg ball, 1 ms, and a 1 N·s bat impulse: gravity contributes 1.4 mN·s, which is 0.14 % of the total. The error from dropping it is smaller than the timing uncertainty.'),
        ('m', r'J_g=(0.145)(9.8)(10^{-3})=1.4\times10^{-3}\ \mathrm{N\,s}'),
        ('n', '0.14 % — the impulse approximation is quantitative, not a hand wave'),
    ])
    s.move('When it fails', [
        ('p', 'A long contact, a light force, or a slow process: a balloon resting on your hand, a block sliding down a ramp. Then gravity\'s impulse is comparable and must be kept.'),
    ])
    s.chip('gate', 'the test', [
        ('p', 'Compute mg Δt and compare it with the impulse of the external hit. Below about 1 % it is safe to drop.'),
    ])
    s.chip('num', 'the window', [
        ('p', 'm = 0.145 kg, Δt = 1 ms'),
        ('p', 'J_g = 1.4 × 10⁻³ N·s'),
        ('p', 'J_bat = 1 N·s → 0.14 %'),
    ])
    s.chip('trap', 'dropping gravity from the energy', [
        ('p', 'Ignoring gravity during the hit is legitimate. Ignoring the height change of the ball afterwards is not: the same problem may need both.'),
    ])
    s.figure('impulse_window')
    S.append(s)

    # ============================================================ 16 BEAD HOOP
    s = Sheet('Olympiad-16-bead-on-hoop', 'Why does a spinning hoop push its bead up the wire?',
              'A bead slides on a hoop spinning about its vertical diameter. Below a critical spin it sits at the bottom. What happens above it?',
              K, 16, total, SRC + '§3.13, OL5',
              'above the critical spin the bottom becomes unstable and two new seats appear',
              stage='spin')
    s.move('Balance along the wire', [
        ('p', 'In the rotating frame the bead feels weight, the normal from the wire, and the centrifugal term. The wire can only push perpendicular to itself, so the tangential components must cancel.'),
        ('m', r'\sin\theta\left(g-\omega^{2}R\cos\theta\right)=0'),
    ])
    s.move('Read off the two families of solutions', [
        ('p', 'The first factor gives the bottom, always an equilibrium. The second gives a pair of symmetric positions that exist only when the spin is fast enough for the cosine to be less than one.'),
        ('m', r'\cos\theta=\frac{g}{\omega^{2}R},\qquad \omega_c=\sqrt{g/R}'),
        ('n', 'at ω = 2ω_c the bead sits at 75.5° from the bottom'),
    ])
    s.move('Stability, not just equilibrium', [
        ('p', 'Below ω_c the bottom is stable and the off-axis solutions do not exist. Above it the bottom becomes unstable — a pitchfork bifurcation — and the bead climbs to one of the two new seats.'),
        ('m', r'\omega<\sqrt{g/R}\ \Rightarrow\ \theta=0\ \mathrm{stable}'),
    ])
    s.chip('key', 'the equilibria', [
        ('m', r'\cos\theta=g/(\omega^{2}R)'),
        ('m', r'\omega_c=\sqrt{g/R}'),
    ])
    s.chip('num', 'a check', [
        ('p', 'R = 1 m, ω_c = 3.13 rad/s'),
        ('p', 'ω = 2ω_c: cosθ = 0.25, θ = 75.5°'),
    ])
    s.chip('trap', 'calling the bottom unstable below the threshold', [
        ('p', 'It is stable below and unstable above. The word "always" is what makes this question a discriminator.'),
    ])
    s.figure('bead_hoop')
    S.append(s)

    # ============================================================ 17 SLACK ANGLE
    s = Sheet('Olympiad-17-slack-angle', 'At what angle does a slackening string let go?',
              'Launch a ball round a vertical circle too slowly and the string goes limp before the top. Is the release angle predictable?',
              K, 17, total, SRC + '§3.13, Q23, P31(c)',
              'the slack angle is where the tension reaches zero while the radial equation still holds',
              stage='spin')
    s.move('Two conditions at the same instant', [
        ('p', 'At the moment the string slackens the tension is zero and the ball is still on the circle. Both must be true together: T = 0 gives one equation, energy gives the speed at that angle.'),
        ('m', r'\frac{mv^{2}}{R}=mg\cos\theta_0,\qquad v^{2}=v_0^{2}-2gR(1+\cos\theta_0)'),
    ])
    s.move('Eliminate the speed', [
        ('p', 'Substituting removes v and leaves a single equation for the angle. The result is worth remembering: it depends only on the dimensionless launch speed v₀²/(gR).'),
        ('m', r'\cos\theta_0=\frac{v_0^{2}}{3gR}-\frac{2}{3}'),
        ('n', 'v₀ = √(5gR) gives cosθ₀ = 1: the release is exactly at the top'),
    ])
    s.move('What happens next', [
        ('p', 'Past θ₀ the string is slack and the ball is a projectile. It usually re-tensions with a jerk somewhere on the far side, unless the geometry carries it clear. Energy alone cannot tell you which.'),
        ('n', 'the highest point of the projectile arc is not the same as the top of the circle'),
    ])
    s.chip('key', 'slack angle', [
        ('m', r'\cos\theta_0=\frac{v_0^2}{3gR}-\frac{2}{3}'),
        ('p', 'no real solution means the string never slackens'),
    ])
    s.chip('num', 'a check', [
        ('p', 'v₀ = 3 m/s, R = 1 m'),
        ('p', 'cosθ₀ = 0.306 − 0.667 = −0.361, θ₀ = 111°'),
    ])
    s.chip('trap', 'using the top as the release point', [
        ('p', 'The string does not wait until the top. It goes slack wherever T first reaches zero, which for a slow launch is well before the highest point.'),
    ])
    s.figure('slack_angle')
    S.append(s)

    # ============================================================ 18 BOUNCE
    s = Sheet('Olympiad-18-bounce-series', 'How far does a bouncing ball travel before it stops?',
              'A ball is dropped from height h and returns to e squared times that height after each bounce. The bounces are infinite — is the total distance?',
              K, 18, total, SRC + '§3.14, Q21, P34',
              'an infinite number of bounces still sums to a finite distance and a finite time',
              stage='one')
    s.move('Write the series', [
        ('p', 'The first fall is h. Every later bounce contributes a rise and a fall, each shorter by a factor e². The sum is geometric, so a closed form exists.'),
        ('m', r's=h+2h\left(e^{2}+e^{4}+\dots\right)=h\frac{1+e^{2}}{1-e^{2}}'),
    ])
    s.move('The time has its own series', [
        ('p', 'Each flight time scales by e, not e², because time goes as the square root of height. That gives a different ratio and a different closed form.'),
        ('m', r't=t_0\frac{1+e}{1-e},\qquad t_0=\sqrt{\frac{2h}{g}}'),
        ('n', 'e = 0.8, h = 5 m: 46 m and 9 s'),
    ])
    s.move('The two limits', [
        ('p', 'As e → 1 both sums diverge: a perfectly elastic ball bounces forever. As e → 0 the distance tends to h and the time to a single fall, which is the inelastic case. Both limits are physically right, which is a good sign for the formulas.'),
        ('m', r'e\to1:\ s\to\infty,\ t\to\infty\qquad e\to0:\ s\to h,\ t\to t_0'),
    ])
    s.chip('key', 'the two sums', [
        ('m', r's=h\frac{1+e^{2}}{1-e^{2}}'),
        ('m', r't=\sqrt{\frac{2h}{g}}\cdot\frac{1+e}{1-e}'),
    ])
    s.chip('num', 'worked', [
        ('p', 'e = 0.8, h = 5 m, g = 10'),
        ('p', 's = 5(1.64/0.36) = 22.8 m'),
        ('p', 't = 1(1.8/0.2) = 9.0 s'),
    ])
    s.chip('trap', 'summing heights only', [
        ('p', 'Every bounce after the first contributes twice its height, once up and once down. Forgetting the factor of two halves the answer.'),
    ])
    s.figure('bounce_series')
    S.append(s)

    # ============================================================ 19 WEDGE MOMENTUM
    s = Sheet('Olympiad-19-wedge-momentum', 'Is horizontal momentum really conserved on a wedge?',
              'A block slides down a smooth wedge that is free to move on a smooth table. Which quantity is conserved, and how do you check it in one line?',
              K, 19, total, SRC + 'Part 7.1, Q24, P35',
              'no external horizontal force means the recoil is the block horizontal momentum, reversed',
              stage='linked')
    s.move('The system is isolated horizontally', [
        ('p', 'Weight and the table normal are vertical, so nothing external acts horizontally on wedge plus block. The horizontal momentum of the pair is therefore constant, and it starts at zero.'),
        ('m', r'm(v_{bx})+Mv_w=0'),
    ])
    s.move('The constraint supplies the velocities', [
        ('p', 'The block stays on the face, so its horizontal velocity is the wedge velocity plus the horizontal part of its slide. Substituting into the momentum statement gives the wedge recoil directly.'),
        ('m', r'v_{bx}=v_w-v_{\mathrm{rel}}\cos\theta'),
        ('m', r'v_w=\frac{mv_{\mathrm{rel}}\cos\theta}{M+m}'),
        ('n', 'the wedge moves opposite to the block horizontal slide, always'),
    ])
    s.move('Differentiate for the accelerations', [
        ('p', 'Since the relation holds at every instant, differentiating gives the same relation between accelerations. The result matches the force derivation, which is the check the exam wants.'),
        ('m', r'a_w=-\frac{mg\sin\theta\cos\theta}{M+m\sin^{2}\theta}'),
    ])
    s.chip('key', 'the conservation statement', [
        ('m', r'm(a_{\mathrm{rel}}\cos\theta-a_w)=Ma_w'),
        ('p', 'one line, and it fixes the sign of the recoil'),
    ])
    s.chip('num', 'a check', [
        ('p', 'm = 1 kg, M = 4 kg, θ = 30°, g = 9.8'),
        ('p', 'a_w = −1.00 m/s², a_rel = 5.76 m/s²'),
        ('p', 'm a_bx = 1(4.99 − 1.00) = 3.99, M a_w = −4.00'),
    ])
    s.chip('trap', 'vertical momentum is not conserved', [
        ('p', 'The table pushes up, so vertical momentum is not conserved. Only the horizontal component is, and only while the table stays level.'),
    ])
    s.figure('wedge_momentum')
    S.append(s)

    # ============================================================ 20 STAGE SPLIT
    s = Sheet('Olympiad-20-stage-split', 'Where should the fuel go between two stages?',
              'Two stages, 800 kg of fuel, 50 kg of dry structure each. Put 400 kg in each, or 160 in the first and 640 in the second?',
              K, 20, total, SRC + '§3.14, OL8, P28',
              'with fixed dry masses the split has no interior optimum: fuel early is never worth it',
              stage='one')
    s.move('Two burns, two mass ratios', [
        ('p', 'Each burn is its own Tsiolkovsky step. The dry stage dropped between them carries no Δv of its own; it only lowers the mass that the second burn must push.'),
        ('m', r'\Delta v=v_e\ln\frac{1000}{1000-800f}+v_e\ln\frac{950-800f}{150}'),
        ('n', 'f is the fraction of the 800 kg that burns in stage one'),
    ])
    s.move('The curve has no interior peak', [
        ('p', 'Differentiate and the result is monotone: every kilogram moved from stage one to stage two raises the total. Physically, the 50 kg dropped early is worth more the sooner it goes, so an empty first stage is best in this model.'),
        ('m', r'f=0.5:\ 3.62\ \mathrm{km/s},\qquad f=0.2:\ 3.67,\qquad f=0.8:\ 3.50'),
    ])
    s.move('So why does anyone split the fuel?', [
        ('p', 'Because the first stage must lift the rest off the pad, so it needs thrust and therefore propellant, and because gravity losses punish a long slow burn. The ideal Δv model has no such constraint, and the source says exactly this: the optimum depends on the dry-mass model you impose.'),
        ('p', 'What survives is the size of the effect. Staging at all is worth about 0.40 km/s here; moving fuel between the stages within the sensible range is worth about 0.17.'),
    ])
    s.chip('key', 'add the logs', [
        ('m', r'\Delta v=v_e\sum_i\ln\frac{m_{0,i}}{m_{f,i}}'),
        ('p', 'each term is one burn; the drop sits between the terms'),
    ])
    s.chip('num', 'the numbers', [
        ('p', 'equal split 3.62 km/s'),
        ('p', 'little fuel first 3.69, most fuel first 3.22'),
        ('p', 'single stage with the same structure 3.22'),
    ])
    s.chip('insight', 'what staging buys', [
        ('p', 'Not a better engine and not a better fuel. It buys the right to stop carrying an empty tank: 0.40 km/s here.'),
    ])
    s.figure('stage_split')
    S.append(s)

    # ============================================================ 21 MODEL LIMITS
    s = Sheet('Olympiad-21-model-limits', "Where exactly do Newton\u2019s laws stop being true?",
              'Newtonian mechanics is taught as if it were exact. Under what conditions does it fail, and what replaces it?',
              K, 21, total, SRC + '§10.2, Part 9.2',
              'Newton is exact inside a fence, and knowing the fence is what makes the model honest',
              stage='one')
    s.move('Three fences, three replacements', [
        ('p', 'Speeds near c need special relativity; actions near ħ need quantum mechanics; strong gravitational fields need general relativity. Each fence is a statement about a dimensionless ratio becoming of order one.'),
        ('m', r'v/c\ll1,\qquad S/\hbar\gg1,\qquad \Phi/c^{2}\ll1'),
    ])
    s.move('What survives inside the fence', [
        ('p', 'Every result in this edition assumes rigid bodies, inextensible massless strings, and dry friction obeying Amontons\u2019 laws. Real strings stretch, real bodies deform, and real friction depends weakly on speed.'),
        ('p', 'None of those corrections matter for a block on a ramp. All of them matter for a rope in a climbing fall, which is why the capstan numbers are quoted as upper bounds.'),
    ])
    s.move('A model you can state the limits of', [
        ('p', 'The honest statement is not "Newton was wrong". It is "Newton is exact in this regime, and here is the boundary". A solution that names its own assumptions can be checked; one that does not cannot.'),
    ])
    s.chip('gate', 'the three ratios', [
        ('p', 'v/c, S/ħ, and Φ/c². Compute whichever is available and check it is small.'),
    ])
    s.chip('trap', 'quoting friction as exact', [
        ('p', 'μ is empirical. Quoting a friction answer to four figures is a claim about the surface that the surface cannot support.'),
    ])
    s.chip('insight', 'why this is on a formula sheet', [
        ('p', 'The validity column of the source table is the part examiners reward and students skip. Two marks often live there.'),
    ])
    s.figure('limits_model')
    S.append(s)

    # ============================================================ 22 ROLLING
    s = Sheet('Olympiad-22-rolling-contact', 'If a rolling wheel is not sliding, what is friction doing?',
              'A driven wheel has friction at the contact, yet the contact point does not move. How can a force act at a point at rest?',
              K, 22, total, SRC + 'Part 8, Trap 10',
              'a rolling wheel uses static friction; the contact point is instantaneously at rest',
              stage='contact')
    s.move('Pure rolling is a kinematic condition', [
        ('p', 'The contact point has zero velocity because the centre moves forward at ωR while the rim moves backward at ωR. No slip, so the friction is static, and static friction may take any value up to its ceiling.'),
        ('m', r'v_{cm}=\omega R,\qquad v_{\mathrm{contact}}=0'),
    ])
    s.move('So friction can point either way', [
        ('p', 'On a driven wheel the axle pushes forward and friction at the road points forward too, providing the reaction that accelerates the car. On a braked wheel friction points backward. On a freely rolling wheel it is nearly zero.'),
        ('m', r'f\le\mu_sN'),
        ('n', 'the engine does not push the car: the road does, through static friction'),
    ])
    s.move('Where rolling resistance comes from', [
        ('p', 'Rolling resistance is not the same phenomenon. It comes from deformation of the tyre and the road, which moves the normal force forward of the axle and creates a retarding torque. That is why it scales with load and with tyre pressure, not with μ.'),
    ])
    s.chip('def', 'pure rolling', [
        ('p', 'No relative motion at the contact, so v_cm = ωR and the friction is static.'),
    ])
    s.chip('trap', 'mu_k for a rolling wheel', [
        ('p', 'Using kinetic friction on a wheel that is rolling correctly is a category error. Kinetic friction appears only once the wheel is skidding.'),
    ])
    s.chip('insight', 'the strong version', [
        ('p', 'A car accelerates because the road pushes it. The engine only spins the wheels; the interaction with the ground does the rest.'),
    ])
    s.figure('rolling_contact')
    S.append(s)

    # ============================================================ 23 FOUR SHORTCUTS
    s = Sheet('Olympiad-23-four-shortcuts', 'What are the four moves that solve almost every problem here?',
              'The chapter has fourteen sections and one page of results. Which four procedures actually carry the load?',
              K, 23, total, SRC + 'Part 7.1-7.4, Part 9.1',
              'four shortcuts, one theme: replace a hard dynamics question with a smaller one',
              stage='one')
    s.move('System, constraint, energy, frame', [
        ('p', 'Every worked problem in this edition is one of those four. Sum forces over a system to remove internal unknowns; differentiate a length constraint to link accelerations; use energy to get speeds without integrating; change to the accelerating frame to turn dynamics into statics.'),
        ('m', r'\sum F_{\mathrm{ext}}=Ma_{\mathrm{cm}},\qquad x_1+2x_2=\mathrm{const}'),
        ('m', r'\Delta K+\Delta U=W,\qquad \vec g_{\mathrm{eff}}=\vec g-\vec a_0'),
    ])
    s.move('Choosing between them', [
        ('p', 'Keyword routing is the fastest method. Pulley words mean constraint. "Find the force between" means system first, then isolate. "Tension at an angle" means energy plus one radial equation. "In the lift or the car" means change frame.'),
        ('n', 'if two routes disagree, the error is in the algebra, not in the physics'),
    ])
    s.move('The discipline they share', [
        ('p', 'Each shortcut deletes a category of unknown rather than solving for it. That is why they are shorter, and also why they are dangerous: if the deleted unknown was actually needed, the method silently gives an incomplete answer.'),
    ])
    s.chip('gate', 'routing table', [
        ('p', 'incline → resolve; pulley → differentiate; circular → centre; banked → tanθ; accelerating → frame; multi-body → system'),
    ])
    s.chip('trap', 'reaching for the shortcut first', [
        ('p', 'Write the free-body diagram anyway, at least in your head. The shortcut is a compression of that diagram, not a replacement for it.'),
    ])
    s.chip('insight', 'the two-frame habit', [
        ('p', 'Once a frame is chosen, write it at the top of the page. Most sign errors in this chapter are frames that were mixed mid-solution.'),
    ])
    s.figure('four_shortcuts')
    S.append(s)

    # ============================================================ 24 MONKEY
    s = Sheet('Olympiad-24-monkey-rope', 'Can a monkey climb away from its own counterweight?',
              'A monkey and an equal counterweight hang from one rope over a pulley. The monkey climbs. Does the counterweight stay, rise, or fall?',
              K, 24, total, SRC + 'Part 9.3, Q25, P36',
              'equal masses on one rope share one acceleration: the climb rate drops out entirely',
              stage='linked')
    s.move('Write the two equations', [
        ('p', 'Both sides have mass m. The tension is the same on both because the rope is massless and the pulley is ideal. Take upward as positive on each side.'),
        ('m', r'T-mg=ma,\qquad T-mg=ma'),
        ('n', 'identical equations, so the two accelerations are identical'),
    ])
    s.move('The climb rate never enters', [
        ('p', 'The monkey climbing means its centre of mass moves relative to the rope. But the rope and the monkey are not the same body: the tension acts on the monkey, and the monkey pulls the rope down with the same force. The rope still has tension T.'),
        ('m', r'a=\frac{T}{m}-g \quad \text{on both sides, for any } u'),
    ])
    s.move('What actually happens', [
        ('p', 'Whatever the monkey does to the rope, it does the opposite to itself, so the pair moves as one system with the common acceleration set by the external weights. If the monkey hauls on the rope, both rise together; if it lets rope slip, both fall together.'),
        ('n', 'the monkey can change the tension, but not the ratio a/g = T/mg − 1'),
    ])
    s.chip('key', 'the whole result', [
        ('m', r'T-mg=ma \text{ on each side} \Rightarrow a_1=a_2'),
        ('p', 'the climb rate u cancels identically'),
    ])
    s.chip('num', 'a check', [
        ('p', 'm = 5 kg each, monkey climbs at 1 m/s relative to the rope.'),
        ('p', 'T = 2mg = 98 N? No: T = m(g + a), and a is free.'),
        ('p', 'If the monkey grips and does not slip, a = 0 and T = 49 N.'),
    ])
    s.chip('trap', 'thinking the monkey can win', [
        ('p', 'Equal masses on one ideal rope cannot separate. The monkey rises, the counterweight rises, at the same rate — the monkey only closes the distance to the pulley faster.'),
    ])
    s.figure('monkey_rope')
    S.append(s)

    return S
