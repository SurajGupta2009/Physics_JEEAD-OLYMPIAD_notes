"""Part I content: JEE Main + Advanced core of Newton's laws.

Every page is a Sheet: a question as the title, numbered moves down the main
column, evidence and warnings in the right-hand rail, one wide figure.
Sources: newtons-laws/Newtons-laws.md  §3.1-3.13, C1-C12, E1-E10, Q1-Q25.
"""
from layout import Sheet

K = "NEWTON'S LAWS  /  PART I: JEE MAIN + ADVANCED"
SRC = 'source: Newtons-laws.md '


def build(total):
    S = []

    # ============================================================ 1 FRAMES
    s = Sheet('JEE-01-inertial-frames', 'What is a force, really?',
              'The first law is recited as "a body keeps moving unless pushed". Why is it a definition of the frame rather than a law about forces?',
              K, 1, total, SRC + '§3.1, C1, C2',
              'pick the frame first: a force is what an inertial frame says it is',
              stage='frame')
    s.move('A frame you are allowed to use', [
        ('p', 'An inertial frame is one in which a body with no net force keeps a constant velocity. That is a test you can run with a puck on a level air table, and it is also a definition: the first law selects the frames in which F = ma may be written.'),
        ('p', 'So the law is not "motion needs a push". It is "no push means no change", and only in the right room.'),
    ])
    s.move('The same ball in two books', [
        ('p', 'In the ground frame the ball on a table has zero net force and zero acceleration. In the frame of a braking car the same ball drifts forward although nothing touched it: the frame invented a force.'),
        ('p', 'Add the pseudo force −ma₀ and the bookkeeping is repaired, which is what the last section of this part does properly.'),
        ('n', 'a frame that needs a fix-up force to explain free motion is not inertial'),
    ])
    s.move('How to detect one without looking out', [
        ('p', 'A plumb line hangs off vertical, a water surface tilts, a pendulum swings with a changed period. No sealed box can distinguish "I am accelerating" from "a uniform gravitational field appeared" — that is the equivalence principle speaking.'),
        ('m', r'a_{\mathrm{frame}}\ne0\ \Rightarrow\ \mathrm{pseudo forces appear in every equation}'),
    ])
    s.chip('def', 'inertial frame', [
        ('p', 'A frame in which a force-free body has constant velocity, and in which F = ma holds without correction terms.'),
    ])
    s.chip('trap', 'the first law is not F = 0 at rest', [
        ('p', 'A body moving uniformly has zero net force. Rest is not privileged; constant velocity is.'),
    ])
    s.chip('check', 'one-line test', [
        ('p', 'If you had to invent a force to explain a motion, you are in a non-inertial frame or you forgot an interaction.'),
    ])
    s.figure('inertial_frames')
    S.append(s)

    # ============================================================ 2 SECOND LAW
    s = Sheet('JEE-02-second-law', 'Is F = ma the law, or a special case?',
              'Rockets, falling chains and conveyor belts all have mass entering or leaving. Which form of Newton\'s second law survives all three?',
              K, 2, total, SRC + '§3.2, C3, OL2, OL4',
              'F = dp/dt is the law; F = ma is the fixed-mass shorthand',
              stage='one')
    s.move('The statement that always holds', [
        ('p', 'Force is the rate of change of momentum. For a fixed mass this collapses to ma, which is why the textbook form works almost everywhere — and why it fails exactly where mass is changing.'),
        ('m', r'\vec F=\frac{d\vec p}{dt}=m\vec a+\vec v\frac{dm}{dt}'),
    ])
    s.move('A hit is an area, not a number', [
        ('p', 'In a collision the force is a pulse lasting a millisecond or less. What survives is its integral: the impulse, equal to the momentum change. The area under an F–t graph is the whole story.'),
        ('m', r'\vec J=\int_{t_1}^{t_2}\vec F\,dt=\Delta\vec p'),
        ('n', 'if the pulse is 1000 N for 1 ms, J = 1 N s whether or not you know its shape'),
    ])
    s.move('When mass arrives already moving', [
        ('p', 'Sand dropped on a belt has zero horizontal momentum; the belt must give it v. The force is ṁv, not ma, because dm/dt is doing the work.'),
        ('m', r'F=\frac{dp}{dt}=\dot m\,v\qquad\mathrm{for\ mass\ arriving\ from\ rest}'),
        ('n', 'the same term appears as λv² when a chain is picked up off the floor'),
    ])
    s.chip('key', 'three forms', [
        ('m', r'\vec F=m\vec a'),
        ('m', r'\vec F=\frac{d\vec p}{dt}'),
        ('m', r'\vec J=\Delta\vec p'),
        ('p', 'Use the second whenever mass changes; the first is a corollary.'),
    ])
    s.chip('trap', 'which mass', [
        ('p', 'In F = ma, m is the mass being accelerated right now. For a rocket it is m(t), and the exhaust momentum must be counted separately.'),
    ])
    s.chip('num', 'feel the scale', [
        ('p', '1000 N for 1 ms = 1 N·s'),
        ('p', 'a 0.145 kg ball reversed at 7 m/s needs 2 N·s'),
        ('p', 'ṁ = 2 kg/s at 3 m/s needs 6 N'),
    ])
    s.figure('second_law')
    S.append(s)

    # ============================================================ 3 THIRD LAW
    s = Sheet('JEE-03-third-law', 'Why is the normal force not the reaction to weight?',
              'Equal and opposite sounds like a pair. What extra conditions turn two forces into a third-law pair?',
              K, 3, total, SRC + '§3.3, C4, E1',
              'a pair needs two bodies and one interaction; N and mg are neither',
              stage='one')
    s.move('Four conditions, not two', [
        ('p', 'A third-law pair is equal in magnitude, opposite in direction, of the same type, and acts on two different bodies. It comes from one interaction, so it dies when the interaction dies.'),
        ('p', 'Push hard on a wall and the wall pushes back just as hard — until you let go, when both forces vanish together.'),
    ])
    s.move('The block on the table', [
        ('p', 'The table pushes the block up with N. The block pushes the table down with an equal N. That is the pair. The block\'s weight pairs with the block pulling the Earth up, a force nobody draws.'),
        ('m', r'N_{\mathrm{on block}}\ \leftrightarrow\ N_{\mathrm{on table}}'),
        ('m', r'mg_{\mathrm{on block}}\ \leftrightarrow\ mg_{\mathrm{on Earth}}'),
        ('n', 'N and mg act on the same body and are different in type: never a pair'),
    ])
    s.move('Why they cancel only sometimes', [
        ('p', 'On a table at rest, N = mg and the two cancel, which hides their different origins. In a lift accelerating upward N > mg, and in free fall N = 0 while mg is unchanged.'),
        ('m', r'N-mg=ma\ \Rightarrow\ N=m(g+a)'),
    ])
    s.chip('def', 'third-law pair', [
        ('p', 'Same type, equal size, opposite direction, different bodies, one interaction.'),
    ])
    s.chip('trap', 'the popular wrong pair', [
        ('p', 'N and mg are not a pair: same body, different interaction. They balance only when a = 0.'),
    ])
    s.chip('check', 'name both bodies', [
        ('p', 'Say the sentence out loud: "the table pushes the block, the block pushes the table." If the two names are not different, it is not a pair.'),
    ])
    s.figure('third_law')
    S.append(s)

    # ============================================================ 4 FBD
    s = Sheet('JEE-04-free-body', 'How do you draw a diagram that never lies?',
              'Six forces, one acceleration. What procedure makes the equations fall out in one pass?',
              K, 4, total, SRC + '§3.4, C5, E3',
              'isolate one body, name every agent, put the axes along the acceleration',
              stage='one')
    s.move('Isolate exactly one body', [
        ('p', 'Draw the body alone. Every contact becomes a normal and possibly a friction; every rope becomes a tension along the rope; every mass gets its weight. Nothing else is allowed in.'),
        ('p', 'If you cannot name the agent that exerts a force, erase the force. "Centrifugal" and "the force of motion" fail this test immediately.'),
    ])
    s.move('Choose axes along the acceleration', [
        ('p', 'On an incline the acceleration is along the slope, so resolve along and perpendicular to it. The two equations then decouple: one gives N, the other gives a.'),
        ('m', r'mg\sin\theta-f=ma'),
        ('m', r'N=mg\cos\theta'),
        ('n', 'N is less than mg on a slope, equal to mg only on level ground'),
    ])
    s.move('The two errors that survive to the exam', [
        ('p', 'Counting the centripetal force as an extra arrow, and counting the pseudo force without declaring a non-inertial frame. Both add a force that is already the resultant.'),
        ('n', 'also: a force on the body you did not isolate belongs somewhere else'),
    ])
    s.chip('gate', 'the five steps', [
        ('p', '1 isolate  2 contacts  3 ropes  4 weight  5 axes along a'),
        ('p', 'Then write ΣF = ma twice, on the two axes.'),
    ])
    s.chip('trap', 'double counting', [
        ('p', 'Centripetal force is the name of the inward resultant, not a fifth arrow. Add it and you have solved 2mv²/R = 2mv²/R.'),
    ])
    s.chip('check', 'sanity pass', [
        ('p', 'Zero acceleration must reproduce the statics answer. Set a = 0 and see.'),
    ])
    s.figure('fbd_incline')
    S.append(s)

    # ============================================================ 5 APPARENT WEIGHT
    s = Sheet('JEE-05-apparent-weight', 'What does a weighing scale actually measure?',
              'In a lift the scale reads more, less, or nothing at all. Which force is it reporting?',
              K, 5, total, SRC + '§3.5, C6, E4',
              'weight never changes; the reading is the normal force',
              stage='contact')
    s.move('The four standard forces', [
        ('p', 'Weight mg, always vertically down, always the same mg. Normal N, perpendicular to the surface, can only push. Tension T, along the string, can only pull. Spring force kx, toward the natural length.'),
        ('p', 'None of these is defined by a formula that always holds: N is whatever the constraint requires, up to the point where contact is lost.'),
    ])
    s.move('The scale reads N, not mg', [
        ('p', 'A spring scale measures the force squeezing it, which is the normal force on your feet. Apply Newton to the person:'),
        ('m', r'N-mg=ma\ \Rightarrow\ N=m(g+a)'),
        ('m', r'\mathrm{lift up: }m(g+a)\quad \mathrm{free fall: }0'),
        ('n', 'accelerating down at a < g gives a reading of m(g − a), still positive'),
    ])
    s.move('Weightless is not gravity-free', [
        ('p', 'An astronaut in orbit still feels 8.7 m/s² of gravity. Everything around falls with the same acceleration, so nothing presses and N = 0. The scale cannot tell weightlessness from free fall, because they are the same thing.'),
    ])
    s.chip('key', 'reading on a scale', [
        ('m', r'N=m(g+a)\ \mathrm{(up positive)}'),
        ('p', 'up at g/2 reads 1.5 mg; down at g/2 reads 0.5 mg'),
    ])
    s.chip('trap', '"my weight changed"', [
        ('p', 'mg is fixed by mass and the local field. Only N changes. A scale reads N.'),
    ])
    s.chip('num', 'quick numbers', [
        ('p', 'a = g: double weight, zero weight'),
        ('p', 'a = g/3 up: 1.33 mg'),
        ('p', 'spring balance in a lift reads the tension, not mg'),
    ])
    s.figure('apparent_weight')
    S.append(s)

    # ============================================================ 6 LAMI
    s = Sheet('JEE-06-lami', 'Three forces, no acceleration: why does the triangle close?',
              'A lamp hangs on two wires. When is the sine rule faster than resolving components?',
              K, 6, total, SRC + '§3.6, C7, E5',
              'three forces in equilibrium close a triangle, and the sine rule reads it',
              stage='contact')
    s.move('Equilibrium is a vector statement', [
        ('p', 'Zero net force means the three arrows, placed head to tail, return to the start. That closed triangle is the whole content of the equilibrium condition; components are just one way to read it.'),
        ('m', r'\vec F_1+\vec F_2+\vec F_3=0'),
    ])
    s.move('Lami is the sine rule in disguise', [
        ('p', 'In the force triangle, side F₁ is opposite the angle between F₂ and F₃. The sine rule then gives all three ratios at once.'),
        ('m', r'\frac{F_1}{\sin\alpha_1}=\frac{F_2}{\sin\alpha_2}=\frac{F_3}{\sin\alpha_3}'),
        ('n', 'α₁ is the angle between F₂ and F₃ — the one opposite F₁'),
    ])
    s.move('Where it stops working', [
        ('p', 'Four or more forces: the polygon still closes, but there is no single sine-rule shortcut. A couple or a body with size: force equilibrium alone is not enough, and moments must be added.'),
    ])
    s.chip('key', 'Lami', [
        ('m', r'\frac{F_1}{\sin\alpha_1}=\frac{F_2}{\sin\alpha_2}=\frac{F_3}{\sin\alpha_3}'),
        ('p', 'each force over the sine of the angle opposite it'),
    ])
    s.chip('trap', 'which angle', [
        ('p', 'The angle is between the other two forces, not between the force and the horizontal. Using the complement gives a wrong ratio that looks plausible.'),
    ])
    s.chip('gate', 'when to reach for it', [
        ('p', 'Exactly three forces, all concurrent, body at rest or moving uniformly. Otherwise resolve.'),
    ])
    s.figure('lami')
    S.append(s)

    # ============================================================ 7 STATIC FRICTION
    s = Sheet('JEE-07-static-friction', 'Is friction equal to mu N?',
              'A 20 N block sits on a rough floor while you push with 3 N and it does not move. What is the friction force?',
              K, 7, total, SRC + '§3.7, C8, E6',
              'static friction is an inequality with a ceiling, not a number',
              stage='contact')
    s.move('Static friction is a range', [
        ('p', 'A block that has not started to slide has zero acceleration, so friction must exactly cancel the push. It takes whatever value is needed, from zero up to a ceiling set by the surfaces.'),
        ('m', r'0\le f_s\le\mu_s N'),
        ('n', 'push with 3 N and it does not move: f_s = 3 N, not μN'),
    ])
    s.move('At the ceiling it lets go', [
        ('p', 'Increase the push and f rises with it, one for one, until f reaches μ_s N. That instant is the threshold of slipping, and the angle at which a ramp reaches it is the angle of repose.'),
        ('m', r'\mu_s=\tan\theta_{\mathrm{repose}}'),
    ])
    s.move('Kinetic friction is a value', [
        ('p', 'Once sliding, the force drops to a fixed μ_k N, usually a little below the static maximum. That drop is why a pushed wardrobe suddenly lurches, and why a car\'s ABS tries to stay just under the threshold.'),
        ('m', r'f_k=\mu_k N\qquad \mu_k<\mu_s\ \mathrm{usually}'),
    ])
    s.chip('key', 'the three statements', [
        ('m', r'f_s\le\mu_sN,\quad f_s=\mu_sN\ \mathrm{at slip}'),
        ('m', r'f_k=\mu_kN'),
        ('m', r'\mu_s=\tan\theta_{\mathrm{repose}}'),
    ])
    s.chip('trap', 'f = mu N on a stationary body', [
        ('p', 'This is the single most common error in the chapter. On a body that is not slipping, friction is found from equilibrium, then checked against μ_s N.'),
    ])
    s.chip('num', 'check these', [
        ('p', 'μ_s = 0.6 on 2 kg: ceiling 11.8 N'),
        ('p', 'push 6 N: f = 6 N, still static'),
        ('p', 'push 13 N: it slides with f = μ_k N'),
    ])
    s.figure('friction_static')
    S.append(s)

    # ============================================================ 8 FRICTION DIRECTION
    s = Sheet('JEE-08-friction-direction', 'Which way does friction point?',
              'A block is dropped on a moving belt and another slides up a ramp. Both are moving, yet friction points in opposite senses. Why?',
              K, 8, total, SRC + '§3.8, C9, Q6',
              'friction opposes relative slip at the contact, not motion in the room',
              stage='contact')
    s.move('Compare the two surfaces, not the body', [
        ('p', 'Friction acts at the interface. What matters is the velocity of the block relative to the surface it touches. If the block lags, friction drags it forward; if it leads, friction holds it back.'),
        ('m', r'\vec f\ \mathrm{opposes}\ \vec v_{\mathrm{block}}-\vec v_{\mathrm{surface}}'),
    ])
    s.move('Three standard pictures', [
        ('p', 'Pushed on a floor: the block would slide right, friction points left. Dropped on a belt: the belt runs forward under it, friction points forward and the block speeds up. Sliding up a ramp: friction points down the slope.'),
        ('n', 'on the belt the block\'s speed increases, so friction does positive work on it'),
    ])
    s.move('Where this bites', [
        ('p', 'Walk forward: the floor pushes you forward by friction. Accelerate a car: the road pushes the driving wheels forward. Brake: the same friction points backward on the car. In each case compare the tyre contact patch with the road.'),
    ])
    s.chip('gate', 'the one question', [
        ('p', 'What is the velocity of this body relative to the surface it touches? Friction points opposite to that.'),
    ])
    s.chip('trap', 'opposing the motion in the room', [
        ('p', 'On an accelerating belt, on a turning car, on a walker: friction often points along the motion. It always opposes slip.'),
    ])
    s.chip('check', 'sign of work', [
        ('p', 'Friction can do positive work on one body and equal negative work on the other. The pair together always removes mechanical energy into heat.'),
    ])
    s.figure('friction_direction')
    S.append(s)

    # ============================================================ 9 MIN PULL
    s = Sheet('JEE-09-min-pull', 'Why is the easiest pull not horizontal?',
              'Dragging a crate is easier with the rope tilted up. Why, and exactly how much less force is needed?',
              K, 9, total, SRC + '§3.7-3.8, E6, E7',
              'tilting up trades normal force for drive, and the best tilt is arctan mu',
              stage='contact')
    s.move('The trade', [
        ('p', 'Pulling at angle θ upward reduces the normal force to mg − F sinθ, so it reduces the friction ceiling. But only the horizontal part F cosθ drives the crate. The two effects fight, so there is an optimum.'),
        ('m', r'N=mg-F\sin\theta,\qquad f=\mu N'),
        ('m', r'F\cos\theta=\mu(mg-F\sin\theta)'),
    ])
    s.move('Minimise the force', [
        ('p', 'Solve for F as a function of θ and minimise. The denominator cosθ + μ sinθ peaks at tanθ = μ, which fixes both the angle and the smallest force.'),
        ('m', r'F(\theta)=\frac{\mu mg}{\cos\theta+\mu\sin\theta}'),
        ('m', r'\theta^{*}=\tan^{-1}\mu,\qquad F_{\min}=\frac{\mu mg}{\sqrt{1+\mu^{2}}}'),
        ('n', 'μ = 0.5 on 2 kg: 26.6° and 8.77 N instead of 9.8 N'),
    ])
    s.move('The other use of the same algebra', [
        ('p', 'Let θ grow to 90° and the crate lifts instead of sliding. The angle of repose is the mirror idea: on a ramp, tanθ ≤ μ_s keeps a block still without any external pull.'),
        ('n', 'both results come from setting the friction ceiling equal to the driving component'),
    ])
    s.chip('key', 'minimum pull', [
        ('m', r'\tan\theta=\mu'),
        ('m', r'F_{\min}=\mu mg/\sqrt{1+\mu^2}'),
        ('p', 'the saving is only about 11 % at μ = 0.5, but it is free'),
    ])
    s.chip('num', 'worked', [
        ('p', 'm = 2 kg, μ = 0.5, g = 9.8'),
        ('p', 'horizontal: F = 9.8 N'),
        ('p', 'at 26.6°: F = 8.77 N'),
    ])
    s.chip('trap', 'two sign errors', [
        ('p', 'N = mg − F sinθ (not plus) when you pull upward. And the friction term uses this reduced N, not mg.'),
    ])
    s.figure('min_pull')
    S.append(s)

    # ============================================================ 10 STACKED
    s = Sheet('JEE-10-stacked-blocks', 'When do two stacked blocks stop moving together?',
              'You push the lower block of a stack. What limits how hard you can push before the top one slips?',
              K, 10, total, SRC + '§3.9, C10, E2, Q8',
              'the top block is driven by friction alone, so it caps the whole system',
              stage='linked')
    s.move('Look at the top block first', [
        ('p', 'The only horizontal force on the upper block is friction from the lower one. Its acceleration is therefore f/m, and it can never exceed μ_s g, no matter how hard you push below.'),
        ('m', r'a_{\mathrm{top}}=\frac{f}{m}\le\mu_s g'),
    ])
    s.move('While they move together', [
        ('p', 'Treat the pair as one body: a = F/(M + m). That is consistent with the top block only while the friction needed stays under the ceiling.'),
        ('m', r'F\le\mu_s g(M+m)'),
        ('m', r'\mu_s=0.3,\ m=1\ \mathrm{kg},\ M=2\ \mathrm{kg}\ \Rightarrow\ F_{\max}=8.82\ \mathrm{N}'),
    ])
    s.move('After the break', [
        ('p', 'The top block keeps accelerating at μ_s g while the bottom one accelerates faster. The relative acceleration is constant, so the top block slides backward relative to the bottom — it is not "left behind" by inertia, it is dragged at a fixed maximum rate.'),
    ])
    s.chip('key', 'the two numbers', [
        ('m', r'F_{\max}=\mu_s g(M+m)'),
        ('m', r'a_{\max}=\mu_s g'),
        ('p', 'the ceiling is set by the upper block, never by the push'),
    ])
    s.chip('trap', 'pushing vs pulling', [
        ('p', 'Which block you push changes the answer: the limit above is for a push on the lower block. Repaint the free-body diagram for the other case.'),
    ])
    s.chip('check', 'limit case', [
        ('p', 'Set μ_s = 0 and the pair cannot move together at all: the top block stays put while the bottom slides out.'),
    ])
    s.figure('stacked_blocks')
    S.append(s)

    # ============================================================ 11 SYSTEM
    s = Sheet('JEE-11-system-vs-parts', 'System or single body: which do you solve?',
              'Two blocks are pushed together. How do you get both the common acceleration and the force between them, without solving twice?',
              K, 11, total, SRC + '§3.9-3.10, E2, Q9',
              'use the system for the acceleration, then isolate one body for the internal force',
              stage='linked')
    s.move('The system first', [
        ('p', 'Internal forces come in third-law pairs, so they cancel inside a system. A single equation then gives the acceleration of the whole thing.'),
        ('m', r'a=\frac{F}{m_1+m_2}'),
    ])
    s.move('Then isolate the far body', [
        ('p', 'Pick the body that has the fewest forces — usually the one you are not pushing. The contact force is its only horizontal force, so it reads off directly.'),
        ('m', r'N_{\mathrm{contact}}=m_2a=\frac{Fm_2}{m_1+m_2}'),
        ('n', 'equal masses: each carries half. A very light front block carries almost nothing.'),
    ])
    s.move('Why the same trick keeps working', [
        ('p', 'Ropes, wedges and stacked blocks all obey it: sum over the system to get a, then cut the system where the unknown force lives. The cut replaces the interaction with the unknown.'),
        ('n', 'with three bodies you may need two cuts, but the recipe is unchanged'),
    ])
    s.chip('gate', 'the recipe', [
        ('p', '1 system for a  2 isolate for N  3 check with the other body'),
    ])
    s.chip('key', 'contact force', [
        ('m', r'N=\frac{Fm_2}{m_1+m_2}'),
        ('p', 'N is not F unless the front block is the whole mass'),
    ])
    s.chip('trap', 'adding contact forces to the system', [
        ('p', 'Inside the dashed box the contact forces cancel. If you kept them, you would double count and halve the acceleration.'),
    ])
    s.figure('system_parts')
    S.append(s)

    # ============================================================ 12 ATWOOD
    s = Sheet('JEE-12-atwood-ramp', 'Atwood on a ramp: where does the motion change hands?',
              'One mass hangs, one sits on a rough 30° ramp. Over what range of mass ratio does nothing move at all?',
              K, 12, total, SRC + '§3.9-3.10, E8, Q11',
              'friction turns one crossing point into a band of mass ratios',
              stage='linked')
    s.move('The clean Atwood machine', [
        ('p', 'Same tension both sides, same magnitude of acceleration. Adding the two equations eliminates T and gives the standard pair of results.'),
        ('m', r'a=\frac{(m_1-m_2)g}{m_1+m_2},\qquad T=\frac{2m_1m_2g}{m_1+m_2}'),
    ])
    s.move('Put one of them on a ramp', [
        ('p', 'Only the component along the slope drives the ramp mass, so sinθ replaces 1 for that side. Add friction and it enters with ±, depending on which way the block is about to slide.'),
        ('m', r'a=\frac{(m_2-m_1\sin\theta)g}{m_1+m_2}\pm\frac{\mu m_1g\cos\theta}{m_1+m_2}'),
    ])
    s.move('The static band', [
        ('p', 'At rest, friction can supply up to μ m₁ g cosθ in either direction. That gives two thresholds, one for sliding up and one for sliding down, and between them the system is frozen.'),
        ('m', r'\sin\theta-\mu\cos\theta\le\frac{m_2}{m_1}\le\sin\theta+\mu\cos\theta'),
        ('n', 'θ = 30°, μ = 0.25: the band is 0.28 to 0.72'),
    ])
    s.chip('key', 'the three formulas', [
        ('m', r'a=\frac{(m_1-m_2)g}{m_1+m_2}'),
        ('m', r'T=\frac{2m_1m_2g}{m_1+m_2}'),
        ('m', r'\mathrm{band: }\sin\theta\mp\mu\cos\theta'),
    ])
    s.chip('num', 'the worked band', [
        ('p', 'θ = 30°, μ_s = 0.25'),
        ('p', '0.5 − 0.217 = 0.28 to 0.5 + 0.217 = 0.72'),
    ])
    s.chip('trap', 'T = m g', [
        ('p', 'T equals the hanging weight only when the system is in equilibrium. Otherwise T is found from either body after a is known.'),
    ])
    s.figure('atwood_incline')
    S.append(s)

    # ============================================================ 13 MOVABLE PULLEY
    s = Sheet('JEE-13-movable-pulley', 'Why does the free end move twice as far?',
              'A rope runs over a fixed pulley, round a movable one, and is anchored. What links the accelerations, and what links the tensions?',
              K, 13, total, SRC + '§3.10, C11, E8',
              'the length constraint gives the accelerations; one string gives the tension',
              stage='linked')
    s.move('Write the length, then differentiate', [
        ('p', 'Let x₁ be the segment that ends at the free mass and x₂ the length of each of the two strands holding the movable pulley. The total length is fixed.'),
        ('m', r'x_1+2x_2=\mathrm{const}\ \Rightarrow\ a_1=-2a_2'),
        ('n', 'the free end must move twice as far, and accelerate twice as hard'),
    ])
    s.move('One string, one tension', [
        ('p', 'A massless frictionless pulley cannot support a tension difference, so the rope tension is the same everywhere. The movable pulley therefore feels 2T upward against the weight hanging on it.'),
        ('m', r'm_1g-T=m_1a_1,\qquad m_2g-2T=m_2a_2'),
    ])
    s.move('Solve with the constraint', [
        ('p', 'Substitute a₂ = −a₁/2 and eliminate T. The free mass always wins the sign argument, because its weight is compared with twice the other weight.'),
        ('m', r'a_1=\frac{2(2m_1-m_2)g}{4m_1+m_2}'),
        ('n', 'equal masses: free end falls at 2g/5, movable pulley rises at g/5'),
    ])
    s.chip('key', 'constraint pair', [
        ('m', r'x_1+2x_2=\mathrm{const}'),
        ('m', r'a_1=-2a_2,\qquad T\ \mathrm{uniform}'),
    ])
    s.chip('num', 'equal masses', [
        ('p', 'm₁ = m₂ = m'),
        ('p', 'a₁ = 2g/5 down, a₂ = g/5 up'),
        ('p', 'T = 3mg/5'),
    ])
    s.chip('trap', 'sign of the constraint', [
        ('p', 'Decide once which direction is positive for each body. The printed solutions of this chapter are inconsistent about it; the magnitudes 2 : 1 are not.'),
    ])
    s.figure('movable_pulley')
    S.append(s)

    # ============================================================ 14 WEDGE MOVE -> PSEUDO
    s = Sheet('JEE-14-pseudo-force', 'Should you ever add a force that is not there?',
              'In a braking bus a hanging pendulum swings forward. Add a pseudo force, or stay in the ground frame?',
              K, 14, total, SRC + '§3.11, C12, E9',
              'a pseudo force is frame bookkeeping, not an interaction',
              stage='pseudo')
    s.move('The recipe for an accelerating frame', [
        ('p', 'If the frame accelerates at a₀, every body in it behaves as if an extra force −ma₀ acted. Add that one term and Newton\'s laws work again, with no other changes.'),
        ('m', r'\vec F_{\mathrm{real}}+(-m\vec a_0)=m\vec a_{\mathrm{frame}}'),
    ])
    s.move('The pendulum in the car', [
        ('p', 'In the car frame the bob is at rest with three forces: weight down, pseudo force backward, tension along the string. Resolving gives the hang angle and the tension immediately.'),
        ('m', r'\tan\theta=\frac{a_0}{g},\qquad T=m\sqrt{g^2+a_0^2}'),
    ])
    s.move('The ground frame must agree', [
        ('p', 'In the ground frame the bob accelerates forward at a₀. The only real forces are T and mg, and their resultant is horizontal. The same θ falls out — a good check that you have not mixed frames.'),
        ('m', r'T\sin\theta=ma_0,\qquad T\cos\theta=mg'),
        ('n', 'if the two frames disagree, one of them has a force that does not exist'),
    ])
    s.chip('key', 'effective gravity', [
        ('m', r'\vec g_{\mathrm{eff}}=\vec g-\vec a_0'),
        ('m', r'\tan\theta=a_0/g'),
    ])
    s.chip('trap', 'mixing frames', [
        ('p', 'The classic disaster: a pseudo force in one equation and ground-frame reasoning in the next. Choose a frame, write it at the top of the page, and stay there.'),
    ])
    s.chip('check', 'the two-frame test', [
        ('p', 'Solve once each way. Any disagreement is an algebra error, never new physics.'),
    ])
    s.figure('pseudo_frame')
    S.append(s)

    # ============================================================ 15 CENTRIPETAL
    s = Sheet('JEE-15-centripetal-source', 'Is centripetal force a new force?',
              'A ball on a string, a car on a bank, a car over a crest. Which real force points inward in each case?',
              K, 15, total, SRC + '§3.12, C12, Q15',
              'centripetal force is the inward resultant, never an extra arrow',
              stage='spin')
    s.move('It is a name, not an interaction', [
        ('p', 'Circular motion at constant speed needs a resultant of mv²/R pointing at the centre. That resultant is produced by whatever real forces happen to point inward. Writing it as an extra force double counts the physics.'),
        ('m', r'\sum F_{\mathrm{inward}}=\frac{mv^{2}}{R}=m\omega^{2}R'),
    ])
    s.move('Three suppliers', [
        ('p', 'A ball on a string: the tension. A car on a bank: the horizontal component of the normal force. A car crossing a hill crest: the difference between weight and normal force, which is why the car feels light.'),
        ('m', r'\mathrm{crest: }mg-N=\frac{mv^{2}}{R}'),
        ('n', 'at the speed √(gR) the normal force reaches zero and the car leaves the road'),
    ])
    s.move('When the supplier quits', [
        ('p', 'A string cannot push, so if the required inward force exceeds the tension available the string goes slack. A tyre cannot pull downward, so on a crest it simply loses contact. The condition is always "the required inward force must be available".'),
    ])
    s.chip('def', 'centripetal force', [
        ('p', 'The inward component of the resultant, of magnitude mv²/R. It is supplied by real forces; it is not one of them.'),
    ])
    s.chip('trap', 'the extra arrow', [
        ('p', 'Draw mv²/R on the free-body diagram and every equation becomes wrong by that amount. Put it on the other side of the equals sign.'),
    ])
    s.chip('check', 'availability test', [
        ('p', 'Compute the inward force required. Compare it with the largest inward force the contact can supply. If required > available, contact is lost.'),
    ])
    s.figure('centripetal_source')
    S.append(s)

    # ============================================================ 16 BANKED DESIGN
    s = Sheet('JEE-16-banked-design', 'Why are racetrack corners banked?',
              'With no friction at all, is there still a speed at which a car can take a banked curve?',
              K, 16, total, SRC + '§3.12, E10, Q17',
              'a bank turns normal force into centripetal force without any friction',
              stage='spin')
    s.move('Resolve vertically and radially', [
        ('p', 'On a frictionless bank the only forces are weight and the normal, which is tilted. Tilt means it has an inward component, and that component is the centripetal force.'),
        ('m', r'N\cos\theta=mg,\qquad N\sin\theta=\frac{mv^{2}}{R}'),
    ])
    s.move('Divide: the mass disappears', [
        ('p', 'Dividing the two equations removes both m and N, leaving the design speed. Every vehicle, from a bicycle to a truck, needs the same speed for a frictionless passage.'),
        ('m', r'v_0^{2}=Rg\tan\theta'),
        ('n', 'R = 50 m, θ = 22°: v₀ = 14 m/s, about 50 km/h'),
    ])
    s.move('Why real roads still need friction', [
        ('p', 'Traffic does not travel at exactly v₀. Below it the car tends to slide down the bank, above it up the bank, and friction has to supply the difference. That is the width of the band on the next sheet.'),
        ('m', r'N=\frac{mg}{\cos\theta}\ >\ mg'),
    ])
    s.chip('key', 'design speed', [
        ('m', r'v_0=\sqrt{Rg\tan\theta}'),
        ('m', r'\tan\theta=\frac{v_0^2}{Rg}'),
    ])
    s.chip('num', 'typical corner', [
        ('p', 'R = 50 m, θ = 22°, g = 9.8'),
        ('p', 'v₀ = 14.0 m/s = 50.5 km/h'),
    ])
    s.chip('trap', 'N = mg on a bank', [
        ('p', 'The normal force is larger than mg on a bank: N = mg/cosθ. Using N = mg understates the available friction as well.'),
    ])
    s.figure('banked_design')
    S.append(s)

    # ============================================================ 17 BANKED BAND
    s = Sheet('JEE-17-banked-band', 'How much slower or faster can you take the bank?',
              'Friction turns one design speed into a range. What are the two limits, and what sets them?',
              K, 17, total, SRC + '§3.12, E10, Q18',
              'friction widens a single design speed into a band of allowed speeds',
              stage='spin')
    s.move('Two limits, one derivation', [
        ('p', 'At the maximum speed the car is about to slide outward, so friction points down the slope. At the minimum it is about to slide inward, so friction points up the slope. Resolve both cases the same way.'),
        ('m', r'v_{\max}^{2}=\frac{Rg(\sin\theta+\mu\cos\theta)}{\cos\theta-\mu\sin\theta}'),
        ('m', r'v_{\min}^{2}=\frac{Rg(\sin\theta-\mu\cos\theta)}{\cos\theta+\mu\sin\theta}'),
    ])
    s.move('The three regimes', [
        ('p', 'Below v_min friction points up the slope; at v₀ it is exactly zero; above v₀ it points down. The same formulas cover all three, and v_min is set to zero once μ exceeds tanθ.'),
        ('n', 'if μ > tanθ the car can stand still on the bank with the brakes off'),
    ])
    s.move('Reading the formulas safely', [
        ('p', 'The denominator of v_max vanishes at μ = cotθ, where no speed is safe. That is not a curiosity: it is why very steep banks are only used with high-grip tyres and why ice on a banked road is so dangerous.'),
    ])
    s.chip('key', 'the band', [
        ('m', r'v_{\max}^{2}=\frac{Rg(\sin\theta+\mu\cos\theta)}{\cos\theta-\mu\sin\theta}'),
        ('m', r'v_{\min}^{2}=\frac{Rg(\sin\theta-\mu\cos\theta)}{\cos\theta+\mu\sin\theta}'),
    ])
    s.chip('trap', 'sign in the denominator', [
        ('p', 'The two denominators differ: cosθ − μ sinθ for the fast limit, cosθ + μ sinθ for the slow one. Swapping them still gives plausible numbers.'),
    ])
    s.chip('check', 'set mu = 0', [
        ('p', 'Both formulas must collapse to v₀ = √(Rg tanθ). If they do not, the algebra is wrong.'),
    ])
    s.figure('banked_band')
    S.append(s)

    # ============================================================ 18 CONICAL
    s = Sheet('JEE-18-conical-pendulum', 'Why does a conical pendulum ignore the mass?',
              'A bob whirled on a string traces a horizontal circle. What actually sets the period?',
              K, 18, total, SRC + '§3.12, Q19',
              'the vertical component carries the weight, so only L cos theta enters the period',
              stage='spin')
    s.move('Separate vertical from radial', [
        ('p', 'The string makes a constant angle θ with the vertical. Vertically there is no acceleration; radially the horizontal component of the tension is the centripetal force.'),
        ('m', r'T\cos\theta=mg,\qquad T\sin\theta=m\omega^{2}(L\sin\theta)'),
    ])
    s.move('Divide and read off the period', [
        ('p', 'The sinθ cancels, and so does the mass. What survives is that the bob behaves like a simple pendulum of length L cosθ — the vertical drop from the support to the plane of the circle.'),
        ('m', r'\omega^{2}=\frac{g}{L\cos\theta},\qquad T_p=2\pi\sqrt{\frac{L\cos\theta}{g}}'),
        ('n', 'a faster whirl means a larger θ, not a different length'),
    ])
    s.move('The two limits', [
        ('p', 'As θ → 0 the circle shrinks and the period tends to the ordinary pendulum 2π√(L/g). As θ → 90° the required ω diverges, which is why you cannot whirl a bob into a horizontal circle.'),
    ])
    s.chip('key', 'the result', [
        ('m', r'T_p=2\pi\sqrt{\frac{L\cos\theta}{g}}'),
        ('m', r'\cos\theta=\frac{g}{\omega^{2}L}'),
    ])
    s.chip('trap', 'using L sin theta', [
        ('p', 'The radius is L sinθ, but the period uses the vertical drop L cosθ. Mixing them gives a period that grows with θ instead of shrinking.'),
    ])
    s.chip('num', 'a check', [
        ('p', 'L = 1 m, θ = 60°: T = 2π√(0.5/9.8) = 1.42 s'),
        ('p', 'the simple pendulum would give 2.01 s'),
    ])
    s.figure('conical')
    S.append(s)

    # ============================================================ 19 VERTICAL STRING
    s = Sheet('JEE-19-vertical-circle-string', 'What is the slowest a ball can go round a vertical loop?',
              'A ball on a string is whirled in a vertical circle. Why must it be fast at the bottom, and what happens at the top?',
              K, 19, total, SRC + '§3.12, Q20, Q21',
              'the string can only pull, so at the top it must still be taut',
              stage='spin')
    s.move('The string can pull but not push', [
        ('p', 'At the top both the tension and the weight point downward, toward the centre. At the limiting speed the tension just reaches zero and the weight alone supplies mv²/R.'),
        ('m', r'T+mg=\frac{mv^{2}}{R}\ \Rightarrow\ v_{\mathrm{top,min}}=\sqrt{gR}'),
    ])
    s.move('Energy carries that back to the bottom', [
        ('p', 'Going from the bottom to the top costs 2mgR. Put in the minimum top speed and the required launch speed falls out; then the tension at any angle follows from the radial equation.'),
        ('m', r'v_{\mathrm{bot,min}}=\sqrt{5gR}'),
        ('m', r'T(\theta)=3mg(1+\cos\theta)'),
        ('n', 'θ measured from the bottom: 6mg at the bottom, 0 at the top'),
    ])
    s.move('Losing the string', [
        ('p', 'Launch slower than √(5gR) and the string slackens before the top. The ball then moves as a projectile inside the circle, and it re-tensions with a jerk if the geometry brings it back to the string.'),
        ('n', 'the slack angle is where T = 0 and the radial equation still holds'),
    ])
    s.chip('key', 'the limiting launch', [
        ('m', r'v_{\mathrm{top}}=\sqrt{gR}'),
        ('m', r'v_{\mathrm{bot}}=\sqrt{5gR}'),
        ('m', r'T(\theta)=3mg(1+\cos\theta)'),
    ])
    s.chip('num', 'the six and the zero', [
        ('p', 'T_bottom = 6mg, T_top = 0'),
        ('p', 'at the horizontal position T = 3mg'),
    ])
    s.chip('trap', 'v_top = 0', [
        ('p', 'Zero speed at the top is the rod condition, not the string condition. On a string the ball must still be moving fast enough for mg to supply mv²/R.'),
    ])
    s.figure('circle_string')
    S.append(s)

    # ============================================================ 20 VERTICAL ROD
    s = Sheet('JEE-20-vertical-circle-rod', 'Why can a bead on a rod stop at the top?',
              'A bead threaded on a light rod is given just enough speed to reach the highest point. What is different from the string?',
              K, 20, total, SRC + '§3.12, Q22, E6',
              'a rod pushes as well as pulls, so it needs no minimum speed at the top',
              stage='spin')
    s.move('A rod is a two-sided constraint', [
        ('p', 'The rod can exert a force toward the centre or away from it. That means v can fall to zero at the top without the constraint failing, and the threshold √(gR) simply disappears.'),
        ('m', r'N+mg=\frac{mv^{2}}{R}\quad \mathrm{with }N\ \mathrm{of either sign}'),
    ])
    s.move('Energy fixes the speed everywhere', [
        ('p', 'Give the bead just enough to reach the top, v_top = 0, so v_bot = √(4gR) = 2√(gR). Then the radial equation gives N at any angle, with cosθ measured from the bottom.'),
        ('m', r'N(\theta)=mg(2+3\cos\theta)'),
        ('n', '5mg at the bottom, −mg at the top: the rod is pulling, not pushing'),
    ])
    s.move('The sign flip', [
        ('p', 'Set N = 0 and cosθ = −2/3, which is 131.8°. Below that the rod pushes outward; above it the rod pulls inward. The bead is never in danger of leaving the circle.'),
    ])
    s.chip('key', 'rod results', [
        ('m', r'v_{\mathrm{bot,min}}=2\sqrt{gR}'),
        ('m', r'N(\theta)=mg(2+3\cos\theta)'),
        ('m', r'N=0\ \mathrm{at}\ \cos\theta=-2/3'),
    ])
    s.chip('trap', 'string and rod mixed', [
        ('p', 'The exam favourite: check whether the constraint can push. If it can, the top speed may be zero; if it cannot, the minimum is √(gR).'),
    ])
    s.chip('num', 'sign check', [
        ('p', 'bottom: N = 5mg (outward, rod pushes)'),
        ('p', 'top: N = −mg (inward, rod pulls)'),
    ])
    s.figure('circle_rod')
    S.append(s)

    # ============================================================ 21 ENERGY SHORTCUT
    s = Sheet('JEE-21-energy-shortcut', 'Why is energy faster than forces in a vertical circle?',
              'The tangential equation has a sin theta in it and the radial equation has a v squared. How do you avoid integrating at all?',
              K, 21, total, SRC + 'Part 7.3, Q23, P31',
              'energy gives the speed at every angle; the radial equation gives the tension',
              stage='spin')
    s.move('Two equations, two different jobs', [
        ('p', 'The radial equation relates T and v at one instant. It says nothing about how v changes with angle. For that, use energy: weight is conservative, so the speed at any height follows from the launch speed.'),
        ('m', r'v^{2}(\theta)=v_0^{2}-2gR(1+\cos\theta)'),
        ('n', 'θ is measured from the bottom, so the rise is R(1 + cosθ)'),
    ])
    s.move('Then one radial equation finishes it', [
        ('p', 'Substitute the speed into the radial relation. The tension now comes out as a function of angle with no integration anywhere.'),
        ('m', r'T(\theta)=m\frac{v^{2}(\theta)}{R}-mg\cos\theta'),
        ('m', r'T(\theta)=\frac{mv_0^{2}}{R}-mg(2+3\cos\theta)'),
        ('n', 'this single formula contains the string results 6mg and 0 at the two ends'),
    ])
    s.move('Why the tangential route is a trap', [
        ('p', 'You could write the tangential equation a_t = −g sinθ and integrate it with v dv = a_t R dθ. It gives the same answer, in three times the lines and with one more place to lose a sign.'),
        ('n', 'the energy route also tells you at a glance which launches are too slow'),
    ])
    s.chip('key', 'the pair', [
        ('m', r'v^{2}=v_0^{2}-2gR(1+\cos\theta)'),
        ('m', r'T=\frac{mv^{2}}{R}-mg\cos\theta'),
    ])
    s.chip('num', 'a check with v0 = 8 m/s', [
        ('p', 'R = 1 m, m = 0.5 kg'),
        ('p', 'bottom T = 37 N, side 22 N, top 7 N'),
    ])
    s.chip('trap', 'the sign of mg cos theta', [
        ('p', 'At the top the weight points inward, so the radial equation is T + mg = mv²/R. Written with cosθ from the bottom, that is exactly the minus sign above.'),
    ])
    s.figure('energy_shortcut')
    S.append(s)

    # ============================================================ 22 ROUGH TABLE PULLEY
    s = Sheet('JEE-22-rough-table-pulley', 'What changes when the table is rough?',
              'A block on a rough table is tied over a pulley to a hanging mass. Everything is the same as the smooth case except one term. Which one?',
              K, 22, total, SRC + '§3.9, Q6, Q17',
              'on the table friction is the brake; on the string it is the drive',
              stage='linked')
    s.move('Both bodies, one string', [
        ('p', 'The tension is the same throughout and the magnitudes of the accelerations match. For the table block the tension pulls forward and friction holds back; for the hanging mass the weight pulls down and the tension up.'),
        ('m', r'T-\mu_k m g=ma,\qquad Mg-T=Ma'),
    ])
    s.move('Eliminate T', [
        ('p', 'Adding the two equations removes the tension and gives the acceleration directly. Friction enters only once, as a subtraction from the drive.'),
        ('m', r'a=\frac{(M-\mu_k m)g}{M+m}'),
        ('n', 'set μ_k = 0 and the standard smooth result returns at once'),
    ])
    s.move('The two thresholds', [
        ('p', 'At rest the system stays put while M g ≤ μ_s m g. That gives a maximum hanging mass. Once moving, the acceleration is positive only if M > μ_k m, which is a slightly lower threshold.'),
        ('m', r'M_{\max}=\mu_s m\quad\text{(static)},\qquad M>\mu_k m\quad\text{(moves)}'),
    ])
    s.chip('key', 'the result', [
        ('m', r'a=\frac{(M-\mu_k m)g}{M+m}'),
        ('m', r'T=\frac{Mm(1+\mu_k)g}{M+m}'),
    ])
    s.chip('num', 'worked', [
        ('p', 'm = 3 kg, M = 2 kg, μ_k = 0.4'),
        ('p', 'a = (2 − 1.2)(9.8)/5 = 1.57 m/s²'),
        ('p', 'T = 16.5 N, below the hanging weight'),
    ])
    s.chip('trap', 'which mu', [
        ('p', 'Use μ_s only for the "does it start?" question and μ_k once it moves. Mixing them gives a system that accelerates from rest with the kinetic value.'),
    ])
    s.figure('rough_table_pulley')
    S.append(s)

    # ============================================================ 23 ACCELERATING INCLINE
    s = Sheet('JEE-23-accelerating-incline', 'Can an accelerating ramp hold a block still?',
              'A block sits on a frictionless ramp that is itself accelerating horizontally. Is there a ramp acceleration at which the block does not slide at all?',
              K, 23, total, SRC + '§3.11, Q22, P29',
              'accelerate the ramp at g tan theta and the pseudo force replaces gravity along the face',
              stage='pseudo')
    s.move('Work in the ramp frame', [
        ('p', 'The block feels weight down, normal perpendicular to the face, and the pseudo force backward. Resolve along the face: the two driving terms are the downhill part of gravity and the uphill part of the pseudo force.'),
        ('m', r'ma_{\mathrm{rel}}=mg\sin\theta-ma_0\cos\theta'),
    ])
    s.move('Set the relative acceleration to zero', [
        ('p', 'One line gives the balanced ramp acceleration. It depends on nothing but the angle — not on m, not on g separately.'),
        ('m', r'a_0=g\tan\theta'),
        ('n', 'θ = 30°: a₀ = 5.66 m/s² holds the block in place'),
    ])
    s.move('Then the normal force', [
        ('p', 'Resolve perpendicular to the face. Both the weight component and the pseudo component push the block into the ramp, so accelerating the ramp into the block increases N rather than threatening contact.'),
        ('m', r'N=mg\cos\theta+ma_0\sin\theta>0'),
        ('n', 'this is a stability threshold, not a loss-of-contact threshold'),
    ])
    s.chip('key', 'the balance', [
        ('m', r'a_0=g\tan\theta'),
        ('m', r'N=m(g\cos\theta+a_0\sin\theta)'),
    ])
    s.chip('trap', 'confusing with liftoff', [
        ('p', 'Pushing the ramp into the block raises N. Pulling the ramp away lowers it. Only the second case has a liftoff threshold, and it is a different formula.'),
    ])
    s.chip('num', 'the two angles', [
        ('p', 'θ = 30°: hold at 5.66 m/s²'),
        ('p', 'θ = 45°: hold at 9.8 m/s²'),
    ])
    s.figure('accelerating_incline')
    S.append(s)

    # ============================================================ 24 MEASURING MU
    s = Sheet('JEE-24-measuring-mu', 'How do you measure friction without a force meter?',
              'Friction coefficients are quoted to two digits. Which three independent experiments produce them, and what does each one assume?',
              K, 24, total, SRC + '§3.7-3.8, Q1, Q18',
              'three routes to one number: tilt, brake, and drag at constant speed',
              stage='contact')
    s.move('The tilt measures the static coefficient', [
        ('p', 'Raise one end of a plank until the block just starts to slide. At that instant the drive mg sinθ and the ceiling μ_s mg cosθ are equal, so the coefficient is the tangent of the angle.'),
        ('m', r'\mu_s=\tan\theta_s'),
        ('n', 'μ_s = 0.4 means θ_s = 21.8°, easy to read on a protractor'),
    ])
    s.move('The skid measures the kinetic one', [
        ('p', 'Lock the wheels or slide a box and measure the stopping distance from a known speed. The deceleration is μ_k g, so the coefficient follows from kinematics alone.'),
        ('m', r'\mu_k=\frac{v^{2}}{2gd}'),
    ])
    s.move('The drag measures it a third way', [
        ('p', 'Pull at constant speed and the applied force equals the kinetic friction, so the coefficient is the ratio of two forces. This is the only one of the three that needs no kinematics, and the only one that reads the coefficient at speed.'),
        ('m', r'\mu_k=\frac{F}{mg}'),
        ('n', 'do it at several speeds: real friction is not perfectly constant'),
    ])
    s.chip('key', 'three formulas', [
        ('m', r'\mu_s=\tan\theta_s'),
        ('m', r'\mu_k=v^{2}/(2gd)'),
        ('m', r'\mu_k=F/(mg)'),
    ])
    s.chip('num', 'the same surface', [
        ('p', 'tilt: θ_s = 22° gives 0.40'),
        ('p', 'skid from 10 m/s in 13.0 m: 0.39'),
        ('p', 'drag at steady speed: 0.39'),
    ])
    s.chip('trap', 'the tilt measures mu_s only', [
        ('p', 'A sliding block on the same plank is no longer at the static limit; the tangent of the angle is then just a lower bound on μ_s.'),
    ])
    s.figure('measure_mu')
    S.append(s)

    # ============================================================ 25 CHAIN ON TABLE
    s = Sheet('JEE-25-chain-over-edge', 'Why does a chain accelerate faster as it falls?',
              'A chain hangs over a table edge with length l already off. The driving weight grows as more falls, but the mass being accelerated does not. What motion results?',
              K, 25, total, SRC + '§3.9, Q25, P32',
              'the hanging weight grows while the sliding mass stays the same, so a grows with x',
              stage='linked')
    s.move('Write the force with x in it', [
        ('p', 'The hanging part has weight λxg and the whole chain has mass λL. Friction is ignored here. The acceleration therefore depends on position, which means the motion is not uniform.'),
        ('m', r'a=\frac{\lambda xg}{\lambda L}=\frac{gx}{L}'),
    ])
    s.move('Integrate instead of using a constant-a formula', [
        ('p', 'Use v dv = a dx. The result is a difference of squares, not a linear ramp in time, and it shows the speed saturating only when the last link leaves.'),
        ('m', r'v\,dv=\frac{g}{L}x\,dx\ \Rightarrow\ v^{2}=\frac{g}{L}\left(x^{2}-l^{2}\right)'),
        ('m', r'v_{x=L}=\sqrt{\frac{g}{L}\left(L^{2}-l^{2}\right)}'),
        ('n', 'set l = 0 and the speed is √(gL) — the classic result'),
    ])
    s.move('The same idea with friction', [
        ('p', 'Add μ times the normal force on the part still on the table and the drive becomes x − μ(L − x). The acceleration can start negative: the chain then waits until enough hangs over.'),
    ])
    s.chip('key', 'the motion', [
        ('m', r'a=gx/L'),
        ('m', r'v^{2}=\frac{g}{L}(x^{2}-l^{2})'),
    ])
    s.chip('num', 'a check', [
        ('p', 'L = 2 m, l = 0.5 m'),
        ('p', 'v at the end = √(9.8(3.75)/2) = 4.3 m/s'),
    ])
    s.chip('trap', 'constant acceleration', [
        ('p', 'Using a = gx/L as a constant with s = ½at² gives the wrong speed and the wrong time. The acceleration is a function of position.'),
    ])
    s.figure('chain_table')
    S.append(s)

    # ============================================================ 26 WEDGE CARRY
    s = Sheet('JEE-26-wedge-carry', 'How hard must you push a wedge to carry its block?',
              'A block rests on a smooth wedge. Accelerate the wedge horizontally and the block can stay put. What is the required acceleration, and what keeps it there?',
              K, 26, total, SRC + '§3.11, Q22, P29',
              'at a0 = g tan theta the pseudo force exactly replaces the downhill pull',
              stage='pseudo')
    s.move('The two ways to hold the block', [
        ('p', 'On a fixed smooth wedge the block slides down, because nothing balances mg sinθ. Accelerating the wedge adds a pseudo force whose uphill component can balance it exactly.'),
        ('m', r'ma_0\cos\theta=mg\sin\theta\ \Rightarrow\ a_0=g\tan\theta'),
    ])
    s.move('What the rider feels', [
        ('p', 'The normal force rises, because the pseudo force also presses the block into the face. That is not a coincidence: the same push that replaces gravity along the slope also loads the contact.'),
        ('m', r'N=\frac{mg}{\cos\theta}'),
        ('n', 'a 1 kg block on a 30° wedge at the balance point presses with 11.3 N, not 8.5 N'),
    ])
    s.move('The applied force on the whole system', [
        ('p', 'Treat wedge plus block as one body. The external push must accelerate the total mass at a₀, and the internal normal does not appear at all.'),
        ('m', r'F=(M+m)g\tan\theta'),
    ])
    s.chip('key', 'the balance', [
        ('m', r'a_0=g\tan\theta'),
        ('m', r'N=mg/\cos\theta'),
        ('m', r'F=(M+m)g\tan\theta'),
    ])
    s.chip('num', 'worked', [
        ('p', 'M = 4 kg, m = 1 kg, θ = 30°'),
        ('p', 'a₀ = 5.66 m/s², F = 28.3 N'),
    ])
    s.chip('trap', 'pushing the wedge the other way', [
        ('p', 'Reverse the acceleration and the pseudo force now adds to the downhill pull: no speed can hold the block. Direction is part of the answer.'),
    ])
    s.figure('wedge_carry')
    S.append(s)

    return S
