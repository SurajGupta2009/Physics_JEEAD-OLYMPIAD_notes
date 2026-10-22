"""Part I content: work, energy, power and circular kinematics for JEE.

Every page is a Sheet: a question as the title, numbered moves down the main
column, evidence and warnings in the right-hand rail, one wide figure.
Sources: work-energy-power/Work-energy-power.md (Parts 0-9) and
motion-in-two-dimensions/Motion-in-two-dimensions.md §3.7-3.10 for the
circular-kinematics sheets.
"""
from layout import Sheet

K = "WORK, ENERGY, POWER  /  PART I: JEE MAIN + ADVANCED"
KC = "CIRCULAR MOTION  /  PART I: JEE MAIN + ADVANCED"
SRC = 'source: Work-energy-power.md '
SRCC = 'source: Motion-in-two-dimensions.md '


def build(total):
    S = []

    # ============================================================ 1 SIGN
    s = Sheet('JEE-01-work-sign', 'What does it mean to do work?',
              'A porter carries a suitcase along a level platform all day and is exhausted. How much work did he do on the suitcase?',
              K, 1, total, SRC + '§3.1, D6.1, C1',
              'work is the component of force along the displacement, with a sign',
              stage='one')
    s.move('One product, no direction left', [
        ('p', 'Work is a scalar built from two vectors: the force and the displacement. Only the part of the force along the displacement moves energy into or out of the body; the perpendicular part changes direction and earns nothing.'),
        ('m', r'W=\mathbf{F}\cdot\mathbf{d}=Fd\cos\theta'),
        ('n', 'the sign is not a direction: it says whether energy enters or leaves'),
    ])
    s.move('The three signs', [
        ('p', 'Positive work: the force has a component along the motion, so the body speeds up. Negative work: the force opposes the motion, and the body slows. Zero work: the force is perpendicular to the displacement, whatever its size.'),
        ('m', r'\theta<90^{\circ}:W>0\qquad \theta=90^{\circ}:W=0\qquad \theta>90^{\circ}:W<0'),
    ])
    s.move('Work is not effort', [
        ('p', 'The first trap of the chapter: biology and physics use the word differently. A wall pushed for an hour receives zero work; a satellite in a circular orbit is pulled by gravity for ever and gravity does zero work on it each orbit.'),
        ('n', 'if there is no displacement along the force, the work is zero however hard it feels'),
    ])
    s.chip('key', 'the definition', [
        ('m', r'W=Fd\cos\theta'),
        ('p', 'F and d in the same frame, theta measured between them'),
    ])
    s.chip('trap', 'selling effort as work', [
        ('p', 'Holding, pushing a wall, carrying level: zero work. Muscles do internal work, the object does not gain energy.'),
    ])
    s.chip('num', 'a check', [
        ('p', 'F = 50 N at 60° over 4 m'),
        ('p', 'W = 50 x 4 x 0.5 = 100 J'),
    ])
    s.figure('work_signs')
    S.append(s)

    # ============================================================ 2 AREA
    s = Sheet('JEE-02-fx-area', 'When the force changes, what replaces F d?',
              'A spring stiffens as you pull it, and a gas pushes less hard as it expands. What is the work when the force is a curve?',
              K, 2, total, SRC + '§3.2, D6.2, Q1-Q3',
              'integrate the force along the path: the answer is a signed area',
              stage='one')
    s.move('Slice the path', [
        ('p', 'Over a short step the force is nearly constant, so the work is F dx. Adding the slices gives an integral, and the integral of a plotted curve is an area.'),
        ('m', r'W=\int_{x_i}^{x_f}F(x)\,dx=\text{area under the }F\text{-}x\text{ graph}'),
    ])
    s.move('Areas below the axis subtract', [
        ('p', 'A force that reverses sign gives back energy. Pushed out and pulled back, the two areas cancel: the net work is the algebraic sum, not the shaded total.'),
        ('m', r'W_{\mathrm{net}}=\int F\,dx\quad\text{counted with sign, not } \int|F|\,dx'),
    ])
    s.move('The spring sets the template', [
        ('p', 'For F = kx the graph is a straight line from the origin, so the area is a triangle: half the final force times the extension. Every elastic-energy result is this triangle.'),
        ('m', r'W=\int_0^{x}kx\,dx=\frac{1}{2}kx^{2}'),
        ('p', 'Read it as an average: the force runs from 0 to kx, so its average is kx/2.'),
    ])
    s.chip('key', 'variable force', [
        ('m', r'W=\int F\,dx'),
        ('p', 'equivalently the signed area of the F-x graph'),
    ])
    s.chip('gate', 'check the shape first', [
        ('p', 'Rectangle, triangle, or a curve you can integrate? Sketch it before writing any integral.'),
    ])
    s.chip('trap', 'using the peak force', [
        ('p', 'For a linear spring the work uses the average force kx/2, not the final force kx. Using kx doubles every spring answer.'),
    ])
    s.figure('fx_area')
    S.append(s)

    # ============================================================ 3 AUDIT
    s = Sheet('JEE-03-force-audit', 'Which forces actually change the energy?',
              'A block slides down a rough incline. Four forces act. Which of them can put energy in, which can only take it out, and which is powerless?',
              K, 3, total, SRC + '§3.3, D6.9, C2',
              'audit each force separately; the normal force is almost always a zero',
              stage='one')
    s.move('The four standard answers', [
        ('p', 'Gravity, normal, friction and the spring cover nearly every JEE question. Each has a fixed signature: gravity stores and returns, the normal on a fixed surface does nothing, friction only removes, and a spring does both.'),
        ('m', r'W_g=mg(y_i-y_f),\quad W_N=0,\quad W_f=-f_k d,\quad W_s=-\frac{1}{2}kx^{2}'),
    ])
    s.move('Why the normal is usually zero', [
        ('p', 'The normal force is perpendicular to the surface, and on a fixed surface the body slides along it, so the displacement is perpendicular to the normal at every instant. Zero dot product, zero work.'),
        ('p', 'The moment the surface moves, the argument dies. On a wedge that slides, the block displacement is not along the face, the normal is no longer perpendicular to it, and the normal does work. That case is OLY 05.'),
        ('n', 'the normal is a zero only while the surface is at rest'),
    ])
    s.move('Friction is the only one-way street', [
        ('p', 'Kinetic friction opposes the relative sliding, so it always does negative work on each sliding body, and the sum on the pair is negative. That negative work is the heat.'),
        ('m', r'W_f^{\mathrm{pair}}=-f_k\,s_{\mathrm{rel}}'),
        ('n', 'push a block round a closed loop and friction still removes energy; gravity returns all of it'),
    ])
    s.chip('key', 'the ledger of standard forces', [
        ('p', 'gravity: path-free. normal: zero on a fixed surface. friction: negative. spring: returns what it stores.'),
    ])
    s.chip('num', '2 kg, 3 m, 30°, mu 0.2', [
        ('p', 'W_g = +29.4 J, W_N = 0, W_f = −10.2 J'),
        ('p', 'net 19.2 J = change in K'),
    ])
    s.chip('trap', 'counting a force twice', [
        ('p', 'If you use the work-energy theorem, do not also add gravity as a potential. Choose: forces and W_net, or energies and conservation.'),
    ])
    s.figure('force_audit')
    S.append(s)

    # ============================================================ 4 THEOREM
    s = Sheet('JEE-04-we-theorem', 'Why is Newton enough to get the work-energy theorem?',
              'The theorem is usually quoted as a separate principle. Can you derive it from F = ma in one line?',
              K, 4, total, SRC + '§3.4, F6.2, E2',
              'multiply Newton by a displacement: the theorem is Newton integrated once over space',
              stage='one')
    s.move('Convert time into space', [
        ('p', 'Newton says F = ma with a = dv/dt. Multiply both sides by the displacement dx, and use the chain rule to swap the time derivative for a speed derivative.'),
        ('m', r'F\,dx=m\frac{dv}{dt}dx=m\,v\,dv'),
    ])
    s.move('Integrate both sides', [
        ('p', 'The left side accumulates work; the right side accumulates the change in half m v squared. The theorem is therefore not an extra law but a restatement of Newton along a path.'),
        ('m', r'W_{\mathrm{net}}=\int_{v_0}^{v}mv\,dv=\frac{1}{2}mv^{2}-\frac{1}{2}mv_0^{2}=\Delta K'),
    ])
    s.move('What the theorem does and does not say', [
        ('p', 'It relates net work to the change in speed and is a scalar statement: no components, no angles, one number per side. It says nothing about time or direction, which is why the force method still exists.'),
        ('p', 'For a system the net work includes internal work: a spring between two blocks works on both, so internal forces can change the total kinetic energy.'),
        ('n', 'the theorem is exact in Newtonian mechanics, for any force and any path'),
    ])
    s.chip('key', 'the theorem', [
        ('m', r'W_{\mathrm{net}}=\Delta K'),
        ('p', 'one particle; for a system add the internal work'),
    ])
    s.chip('gate', 'when to reach for it', [
        ('p', 'Ask for a speed or a distance and the theorem is usually shorter than F = ma. Ask for a time and it cannot help.'),
    ])
    s.chip('trap', 'W without the net', [
        ('p', 'The theorem needs the work of every force. Work of one force equals the change in K only when it is the only one acting.'),
    ])
    s.figure('we_derivation')
    S.append(s)

    # ============================================================ 5 FRAMES
    s = Sheet('JEE-05-ke-frames', 'Whose kinetic energy is it?',
              'A 1 kg block moves at 4 m/s in the ground frame and 3 m/s in a train. Two observers, two kinetic energies. Is the law broken?',
              K, 5, total, SRC + '§2, C3',
              'kinetic energy is frame-dependent, so a work statement must name its frame',
              stage='frame')
    s.move('Half m v squared is not frame-free', [
        ('p', 'Speed depends on the observer, so kinetic energy does too. A block at rest in a train has 8 J in one frame and 24.5 J in another, and neither observer is wrong.'),
        ('m', r'K_{\mathrm{new}}=K+\mathbf{p}\cdot\mathbf{V}+\frac{1}{2}mV^{2}'),
        ('n', 'the cross term carries the difference between the two frames'),
    ])
    s.move('The theorem survives the change', [
        ('p', 'In each frame the net work computed in that frame equals the change in kinetic energy in that frame. Nothing is violated, but the numbers differ because the forces act through different displacements.'),
        ('p', 'This is why a statement like "the collision released 50 J" needs a frame. Use the centre-of-mass frame and the internal energy is unambiguous; that is the whole point of the CM decomposition in OLY 01.'),
    ])
    s.move('The rule for exams', [
        ('p', 'Fix the frame at the start, write it at the top of the page, and keep the ground frame unless the question names another. Mixing two frames in one energy equation is the single commonest way to lose a JEE Advanced question.'),
        ('n', 'energy differences within one frame are always safe; energies across frames are not'),
    ])
    s.chip('def', 'kinetic energy', [
        ('m', r'K=\frac{1}{2}mv^{2}'),
        ('p', 'a scalar, but relative to a chosen frame'),
    ])
    s.chip('trap', 'mixing frames mid-solution', [
        ('p', 'Add a train-frame energy to a ground-frame work and the answer is meaningless. Name the frame first.'),
    ])
    s.chip('insight', 'why the CM frame is special', [
        ('p', 'In the CM frame the total momentum is zero, so the kinetic energy is purely internal and can all be converted.'),
    ])
    s.figure('ke_frames')
    S.append(s)

    # ============================================================ 6 HEAT
    s = Sheet('JEE-06-friction-heat', 'Where does the energy go when friction stops a block?',
              'A block slides to rest. The work-energy theorem says the kinetic energy vanished. Energy is conserved, so where is it?',
              K, 6, total, SRC + '§3.14, D6.12, Q5',
              'friction turns mechanical energy into heat at f_k times the sliding distance',
              stage='one')
    s.move('The ledger with a heat line', [
        ('p', 'Mechanical energy is not conserved when friction acts, but total energy is. Write the heat as an explicit line in the budget instead of pretending it disappeared.'),
        ('m', r'K_i+U_i=K_f+U_f+Q,\qquad Q=f_k\,d'),
    ])
    s.move('Why d is the sliding distance', [
        ('p', 'The heat is the friction force times the distance the surfaces rub against each other. On a block sliding over a fixed floor that is just the block displacement. On a belt it is not: the belt moves too, and the heat is f_k times the relative displacement.'),
        ('m', r'Q=f_k\,s_{\mathrm{rel}}\quad\text{not}\quad f_k\times(\text{either body displacement})'),
        ('n', 'on a belt the extra heat is exactly the work done by the motor that the block did not get'),
    ])
    s.move('A block that returns', [
        ('p', 'Send a block up a rough incline and let it come back. Gravity returns all its work over the round trip; friction removes energy on both legs, so the return speed is lower. The difference between the two is twice the friction work.'),
        ('m', r'v_{\mathrm{back}}^{2}=v_0^{2}-4\mu_k g\cos\theta\,s'),
    ])
    s.chip('key', 'the heat line', [
        ('m', r'Q=f_k\,d,\qquad K_i+U_i=K_f+U_f+Q'),
        ('p', 'd is the relative sliding distance'),
    ])
    s.chip('num', 'a check', [
        ('p', '2 kg at 6 m/s, mu_k 0.3'),
        ('p', 'd = 36/(2 x 2.94) = 6.1 m, Q = 36 J'),
    ])
    s.chip('trap', 'calling the energy lost', [
        ('p', 'It is not lost: it is thermal energy in the two surfaces. Say so, and the bookkeeping stays honest.'),
    ])
    s.figure('friction_ledger')
    S.append(s)

    # ============================================================ 7 POWER
    s = Sheet('JEE-07-power-definition', 'What is power, and why is it a dot product?',
              'Two motors lift the same load through the same height; one takes twice as long. The work is identical. What differs?',
              K, 7, total, SRC + '§3.5, F6.3, C4',
              'power is work per unit time, and at a given speed it is force times velocity',
              stage='one')
    s.move('Rate, not amount', [
        ('p', 'Power answers how fast energy moves. Average power is work over time; instantaneous power is the derivative, which turns into a dot product once the displacement is written as velocity times time.'),
        ('m', r'\bar{P}=\frac{W}{\Delta t},\qquad P=\frac{dW}{dt}=\mathbf{F}\cdot\mathbf{v}=Fv\cos\theta'),
    ])
    s.move('The engine only feels the component along the motion', [
        ('p', 'Push a cart at an angle and only F cos(theta) drives it, so only that part costs power. Push perpendicular to the motion and the power is zero however hard you push, which is the same statement as zero work.'),
        ('n', 'P = F v is the single most used formula in vehicle and pump problems'),
    ])
    s.move('Units and the horsepower', [
        ('p', 'The watt is one joule per second. The commercial horsepower is 746 W, and the metric horsepower is 735 W; JEE questions mean 746 unless they say otherwise. A kilowatt-hour is 3.6 MJ, which is energy, not power.'),
        ('m', r'1\ \mathrm{hp}=746\ \mathrm{W},\qquad 1\ \mathrm{kWh}=3.6\times10^{6}\ \mathrm{J}'),
    ])
    s.chip('key', 'power', [
        ('m', r'P=\mathbf{F}\cdot\mathbf{v}=Fv\cos\theta'),
        ('p', 'average: W over the interval'),
    ])
    s.chip('gate', 'what the question gives', [
        ('p', 'Work and time: average power. Force and speed: instantaneous power. Neither: you need one of them first.'),
    ])
    s.chip('trap', 'kWh is energy', [
        ('p', 'A 100 W bulb for 5 hours uses 0.5 kWh = 1.8 MJ. The kilowatt-hour is not a unit of power.'),
    ])
    s.figure('power_curve')
    S.append(s)

    # ============================================================ 8 CONST POWER
    s = Sheet('JEE-08-constant-power', 'What happens when the power is held constant?',
              'A car with a 100 kW engine at full throttle does not accelerate at a constant rate. What does its speed do?',
              K, 8, total, SRC + '§3.5, D6.3, Q12',
              'at constant power the acceleration must fall as the speed rises',
              stage='one')
    s.move('Power fixed means force falls', [
        ('p', 'At constant power the driving force is P/v, so as the car speeds up the force shrinks. Newton then gives an acceleration that falls like 1/v, and the speed grows without bound but ever more slowly.'),
        ('m', r'F=\frac{P}{v}\quad\Rightarrow\quad a=\frac{P}{mv}'),
    ])
    s.move('Integrate for the speed', [
        ('p', 'Write a = v dv/dx or use energy directly: the work done in time t is Pt, so the kinetic energy is Pt. That gives the speed as the square root of time, and the time to reach a speed as the square of that speed.'),
        ('m', r'v=\sqrt{\frac{2Pt}{m}},\qquad t=\frac{mv^{2}}{2P}'),
        ('n', 'a constant-power start is not a constant-acceleration start'),
    ])
    s.move('Where it stops being ideal', [
        ('p', 'Real engines reach a torque limit at low speed, so the launch is closer to constant force, and a speed limit at high speed, so the top end is closer to constant speed. The constant-power curve is the middle regime, and it is the one JEE questions use.'),
    ])
    s.chip('key', 'constant power', [
        ('m', r'v=\sqrt{2Pt/m},\qquad t=mv^{2}/(2P)'),
        ('p', 'force P/v, acceleration P/(mv)'),
    ])
    s.chip('num', 'a check', [
        ('p', '800 W on 1000 kg'),
        ('p', 'v(10 s) = 4.0 m/s; 20 m/s needs 250 s'),
    ])
    s.chip('trap', 'applying v = at', [
        ('p', 'Constant acceleration is the wrong model here. Use energy, or integrate a = P/(mv).'),
    ])
    s.figure('constant_power')
    S.append(s)

    # ============================================================ 9 SLOPE
    s = Sheet('JEE-09-slope-power', 'Why does a hill cost so much more than a straight road?',
              'A car cruising at 20 m/s needs 10 kW on the flat. On a 5° climb it needs much more. Where does the extra power go?',
              K, 9, total, SRC + '§3.12, D6.3, Q12, Q15',
              'climbing at speed v costs mgv sin theta just to gain height',
              stage='one')
    s.move('Separate the two jobs', [
        ('p', 'On the flat the engine only fights resistance. On a slope it must also lift the car, and lifting costs power at a rate equal to the weight component along the slope times the speed.'),
        ('m', r'P=(f+mg\sin\theta)\,v'),
    ])
    s.move('Numbers make the point', [
        ('p', 'For a 1000 kg car with 500 N of drag, the flat requirement at 20 m/s is 10 kW. A 5° slope adds 1000 x 9.8 x 0.087 = 855 N, so the power jumps to 27 kW, nearly three times as much for the same speed.'),
        ('m', r'P_{\mathrm{flat}}=10.0\ \mathrm{kW},\quad P_{5^{\circ}}=27.1\ \mathrm{kW}'),
        ('n', 'most of the extra power goes into height, not into speed'),
    ])
    s.move('The same algebra for pumps', [
        ('p', 'A pump lifting water at a volume rate Q to a height h needs rho Q g h of useful power, and more at the shaft because of losses. Divide the useful power by the efficiency to get the input the motor must supply.'),
        ('m', r'P_{\mathrm{useful}}=\rho Qgh,\qquad P_{\mathrm{in}}=\frac{\rho Qgh}{\eta}'),
    ])
    s.chip('key', 'climbing power', [
        ('m', r'P=(f+mg\sin\theta)v'),
        ('p', 'the sine, not the tangent: work is against the weight component'),
    ])
    s.chip('num', 'a check', [
        ('p', '1000 kg, 5°, 20 m/s, f = 500 N'),
        ('p', 'P = (500 + 855) x 20 = 27.1 kW'),
    ])
    s.chip('trap', 'using mg tan theta', [
        ('p', 'The force along a slope is mg sin theta. The tangent appears in banked-road problems, not in climbing power.'),
    ])
    s.figure('slope_power')
    S.append(s)
    # ============================================================ 10 CONSERVATIVE
    s = Sheet('JEE-10-conservative', 'What makes a force conservative?',
              'Gravity and the spring let you keep a potential. Friction does not. What single test separates them?',
              K, 10, total, SRC + '§3.6, D6.5, C5',
              'conservative means the work depends only on the endpoints, so a potential exists',
              stage='one')
    s.move('Two equivalent tests', [
        ('p', 'A force is conservative if its work round every closed loop is zero, equivalently if the work between two points is path-free. The tests imply each other: go out one way and back another and the loop integral is the difference.'),
        ('m', r'\oint\mathbf{F}\cdot d\mathbf{r}=0\quad\Longleftrightarrow\quad W_{A\to B}\ \text{path-free}'),
    ])
    s.move('Which forces pass', [
        ('p', 'Gravity, the spring and every central force f(r) r-hat pass. Friction, drag and any speed-dependent force fail, because reversing the motion keeps the force against the travel.'),
        ('p', 'The failure is not a technicality: a brake cannot store energy at all.'),
        ('n', 'a force that depends on speed can never be conservative'),
    ])
    s.move('Why we care', [
        ('p', 'Only a conservative force has a potential, because only then is the work a difference of a function of position. That is what makes the energy method possible, and why friction is always a separate loss line.'),
        ('m', r'W_{\mathrm{cons}}=-\Delta U\quad\Longleftrightarrow\quad \oint\mathbf{F}\cdot d\mathbf{r}=0'),
    ])
    s.chip('key', 'the test', [
        ('p', 'Loop work zero, or path-independent work. Either one, and a U exists.'),
    ])
    s.chip('gate', 'spot the failure fast', [
        ('p', 'Does the force depend on speed or on the direction of travel? Then it is not conservative.'),
    ])
    s.chip('trap', 'gravity is not always free', [
        ('p', 'Near the Earth U = mgh; far from it U = −GMm/r. Both are conservative, but the linear form is only valid while g is constant.'),
    ])
    s.figure('loop_test')
    S.append(s)

    # ============================================================ 11 POTENTIAL
    s = Sheet('JEE-11-potential-energy', 'Why can the zero of potential energy be anywhere?',
              'A book on a shelf has 20 J of potential energy, or 5 J, or −100 J, depending on where you put the zero. Which is right?',
              K, 11, total, SRC + '§3.7, D6.4, C6',
              'only differences of potential energy are physical, so the zero is yours to choose',
              stage='one')
    s.move('Define it by the work', [
        ('p', 'Potential energy is the work a conservative force would do on the way to the reference point, with a minus sign. Because only differences enter the energy equation, the additive constant is free.'),
        ('m', r'U(x)=-\int_{x_0}^{x}F\,dx+U(x_0)'),
    ])
    s.move('Choose the zero where it simplifies', [
        ('p', 'Put the zero at the lowest point for a pendulum, at the ground for a falling body, at the natural length for a spring. The physics never changes; only the arithmetic does.'),
        ('m', r'U_g=mgh,\qquad U_s=\frac{1}{2}kx^{2},\qquad U_g=-\frac{GMm}{r}'),
        ('n', 'the minus sign in the gravitational form is a choice with U(infinity) = 0'),
    ])
    s.move('The trap: a potential for a non-conservative force', [
        ('p', 'There is no potential energy of friction. If you write one, the same point gets two different values depending on how the body arrived, and the function is not a function. In energy questions friction belongs on the loss line, never inside U.'),
    ])
    s.chip('def', 'potential energy', [
        ('m', r'U=-\int F\,dx'),
        ('p', 'defined only for conservative forces, up to a constant'),
    ])
    s.chip('num', 'the spring well', [
        ('p', 'k = 200 N/m, x = 0.2 m'),
        ('p', 'U = 0.5 x 200 x 0.04 = 4 J'),
    ])
    s.chip('trap', 'a potential for friction', [
        ('p', 'Friction has no U. Write its work as −f_k d on the loss line and the bookkeeping stays truthful.'),
    ])
    s.figure('pe_definition')
    S.append(s)

    # ============================================================ 12 SPRING
    s = Sheet('JEE-12-spring-energy', 'Why is the spring energy half k x squared?',
              'Pull a spring to extension x and the force has grown from zero to kx. Why is the stored energy not kx times x?',
              K, 12, total, SRC + '§3.3, §3.7, E1, Q3',
              'the force is not constant, so the work uses its average, which is half the final value',
              stage='one')
    s.move('The triangle again', [
        ('p', 'The force-extension graph is a straight line from the origin to (x, kx). The work done on the spring is the area of that triangle, which is half the base times the height.'),
        ('m', r'W_{\mathrm{on\ spring}}=\int_0^{x}kx\,dx=\frac{1}{2}kx^{2}=U_s'),
    ])
    s.move('Work by and work on', [
        ('p', 'Stretching: the spring pulls back while you pull out, so the spring does negative work and stores energy. Releasing: the spring pushes in the direction of motion, does positive work, and gives the energy back. The sign flips, the magnitude does not.'),
        ('m', r'W_{\mathrm{spring}}=-\frac{1}{2}kx_f^{2}+\frac{1}{2}kx_i^{2}=-\Delta U_s'),
        ('n', 'a spring is a conservative storage device, not a source'),
    ])
    s.move('The calibration trick', [
        ('p', 'Because U is quadratic, doubling the extension quadruples the energy. This is why a spring scale is linear in force but its stored energy is not, and why a small extra stretch near full compression is expensive.'),
        ('n', 'k doubles, energy doubles; x doubles, energy quadruples'),
    ])
    s.chip('key', 'spring energy', [
        ('m', r'U_s=\frac{1}{2}kx^{2}'),
        ('p', 'work done by the spring is minus the change in U'),
    ])
    s.chip('num', 'a check', [
        ('p', 'k = 500 N/m, compressed 0.1 m'),
        ('p', 'U = 0.5 x 500 x 0.01 = 2.5 J'),
    ])
    s.chip('trap', 'k x, not half k x', [
        ('p', 'kx is the final force, not the average. Using it doubles the energy every time.'),
    ])
    s.figure('spring_work')
    S.append(s)

    # ============================================================ 13 GRAVITY
    s = Sheet('JEE-13-gravity-paths', 'Does the route up a hill change the energy?',
              'Climb a hill by the gentle path or the steep one. The height gained is the same. Is the work by gravity the same?',
              K, 13, total, SRC + '§3.3, D6.4, Q8',
              'gravity charges by height gained, never by distance travelled',
              stage='one')
    s.move('Height is the only variable', [
        ('p', 'The work by gravity is the weight times the vertical drop, whatever the path. A staircase, a ramp and a cable car between the same two points all give the same number.'),
        ('m', r'W_g=mg(y_i-y_f)=-\Delta U_g'),
        ('n', 'the horizontal part of any path is free of gravity work'),
    ])
    s.move('This is why the potential exists', [
        ('p', 'Path independence is exactly the condition for a potential. Gravity therefore gets a function of height, and the energy method needs no path information at all. A frictionless roller coaster is the classic beneficiary.'),
        ('p', 'The same statement for a spring uses extension instead of height, and for the general gravitational field uses 1/r instead of h.'),
    ])
    s.move('Where the linear form breaks', [
        ('p', 'U = mgh assumes g is constant, which fails once the height is a noticeable fraction of the Earth radius. Beyond that, use −GMm/r, and the escape speed follows from setting the total energy to zero. OLY 06 does that arithmetically.'),
        ('m', r'mgh\ \text{valid for}\ h\ll R_E,\qquad U=-\frac{GMm}{r}\ \text{otherwise}'),
    ])
    s.chip('key', 'gravitational work', [
        ('m', r'W_g=-mg\,\Delta h'),
        ('p', 'independent of the path, so U = mgh exists'),
    ])
    s.chip('gate', 'when mgh is enough', [
        ('p', 'Heights under a few kilometres on Earth. Beyond that, or for orbits, switch to −GMm/r.'),
    ])
    s.chip('insight', 'the physical reading', [
        ('p', 'Only the vertical component of a displacement changes gravitational energy, because only that component is along the force.'),
    ])
    s.figure('gravity_paths')
    S.append(s)

    # ============================================================ 14 CONSERVATION
    s = Sheet('JEE-14-energy-conservation', 'When may you write K + U = constant?',
              'Energy conservation is quoted as a law. Under exactly what conditions is the mechanical version true?',
              K, 14, total, SRC + '§3.8, F6.4, E3',
              'mechanical energy is constant exactly when no non-conservative force does net work',
              stage='one')
    s.move('The condition, in one line', [
        ('p', 'Split the net work into conservative and non-conservative parts. The conservative part is minus the change in potential, so what is left over is the change in mechanical energy.'),
        ('m', r'W_{\mathrm{nc}}=\Delta K+\Delta U=\Delta E'),
    ])
    s.move('Reading the condition properly', [
        ('p', 'The right-hand side being zero does not require that no friction exists; it requires that friction does no net work over that interval. A block that goes down and back up the same rough incline has friction work −2f d, so E is not constant even though the endpoints coincide.'),
        ('p', 'Equally, a normal force from a moving surface can do work, and a tension at a peg that does not move cannot. Check the work, not the name of the force.'),
        ('n', 'conservation is a statement about an interval, not about a force list'),
    ])
    s.move('What to write on the sheet', [
        ('p', 'Name the two states, draw the energy bars for each, and put every term that changed on the correct side. If the bars do not balance, a force was missed, and the missing term is almost always friction or a normal on a moving surface.'),
    ])
    s.chip('key', 'conservation', [
        ('m', r'K_i+U_i=K_f+U_f\quad\text{when } W_{\mathrm{nc}}=0'),
        ('p', 'otherwise add W_nc, or subtract f_k d'),
    ])
    s.chip('trap', 'assuming conservation', [
        ('p', 'A rough surface, a motor, or a moving support all break it. Look for the loss term before writing the equals sign.'),
    ])
    s.chip('num', 'a check', [
        ('p', '2 kg from 5 m on a smooth ramp'),
        ('p', 'v = sqrt(2 x 9.8 x 5) = 9.9 m/s, independent of the slope'),
    ])
    s.figure('energy_ledger')
    S.append(s)

    # ============================================================ 15 U GRAPH
    s = Sheet('JEE-15-u-graph', 'What can a potential-energy graph tell you at a glance?',
              'Given U(x) and one number E, how much of the motion do you already know without solving anything?',
              K, 15, total, SRC + '§3.9, D6.5, E5, Q11',
              'the graph is a map: where E crosses U is where the motion turns round',
              stage='one')
    s.move('Draw the energy line', [
        ('p', 'Put a horizontal line at the total energy. The kinetic energy is the gap between the line and the curve, so the particle can only be where the line is above U. The crossings are the turning points, where it stops and reverses.'),
        ('m', r'K=E-U(x)\ge0\quad\Rightarrow\quad \text{allowed where } E\ge U'),
    ])
    s.move('Wells, hills and stability', [
        ('p', 'A minimum of U is a stable equilibrium: displaced, the particle is pushed back. A maximum is unstable. Between them the curve is a hill the particle can cross only if E reaches the top.'),
        ('m', r'\frac{dU}{dx}=0\ \text{and}\ \frac{d^{2}U}{dx^{2}}>0\ \Rightarrow\ \text{stable}'),
        ('n', 'a well is a bound state; a hilltop is a knife edge'),
    ])
    s.move('Reading speed off the graph', [
        ('p', 'At any allowed x the speed is the square root of twice the gap divided by m. So the particle is fastest at the bottom of the well and slowest at the turning points, and the shape of the well is the shape of the motion.'),
        ('m', r'v(x)=\sqrt{\frac{2\left(E-U(x)\right)}{m}}'),
    ])
    s.chip('key', 'the three readings', [
        ('p', 'crossings: turning points. minimum: stable. maximum: unstable.'),
    ])
    s.chip('num', 'a check', [
        ('p', 'U = 3x² − 12x + 9 J'),
        ('p', 'dU/dx = 6x − 12 = 0 at x = 2 m, a minimum: stable'),
    ])
    s.chip('trap', 'calling a flat point stable', [
        ('p', 'dU/dx = 0 alone is only an equilibrium. Check the second derivative, or the local shape if it vanishes.'),
    ])
    s.figure('u_landscape')
    S.append(s)

    # ============================================================ 16 GRADIENT
    s = Sheet('JEE-16-force-gradient', 'How do you get the force back from the energy?',
              'You are given U(x) as a curve. Where is the force large, which way does it point, and where is it zero?',
              K, 16, total, SRC + '§3.13, E8, Q21',
              'force is minus the slope of the potential, so it points downhill',
              stage='one')
    s.move('Undo the definition', [
        ('p', 'Potential energy was defined as minus the integral of the force, so differentiating brings the force back with a minus sign. The force points in the direction in which U falls.'),
        ('m', r'F_x=-\frac{dU}{dx},\qquad \mathbf{F}=-\nabla U'),
    ])
    s.move('Reading the slope', [
        ('p', 'A steep descent means a strong force; a flat region means none. At a minimum the slope is zero, so the force is zero and the particle sits in equilibrium. At the bottom of a well a small displacement produces a restoring force proportional to the displacement, which is the harmonic limit.'),
        ('m', r'U=\frac{1}{2}kx^{2}\ \Rightarrow\ F=-kx'),
        ('n', 'the standard spring force is the gradient of the standard spring energy'),
    ])
    s.move('From a formula, not just a graph', [
        ('p', 'In three dimensions the gradient points along the steepest increase, so the force points the other way. For a central potential U(r) this gives f = −dU/dr along the radius, which is how the inverse-square law is recovered from the gravitational potential.'),
        ('m', r'U=-\frac{GMm}{r}\ \Rightarrow\ F=-\frac{GMm}{r^{2}}\ \text{inward}'),
    ])
    s.chip('key', 'force from energy', [
        ('m', r'F_x=-dU/dx'),
        ('p', 'in 3-D: F = −grad U'),
    ])
    s.chip('num', 'a check', [
        ('p', 'U = 5x² − 10x'),
        ('p', 'F = 10 − 10x N; zero at x = 1 m'),
    ])
    s.chip('trap', 'forgetting the minus', [
        ('p', 'The force pushes the particle toward lower U. Dropping the minus reverses every direction in the answer.'),
    ])
    s.figure('force_gradient')
    S.append(s)

    # ============================================================ 17 DECISION
    s = Sheet('JEE-17-energy-or-force', 'Energy or Newton: which method does the question want?',
              'Two questions about the same loop: what is the speed at the top, and what is the normal force there? One is energy, one is not.',
              K, 17, total, SRC + '§3.10, §9.1, E3',
              'energy answers speed and distance; forces answer time, acceleration and contact force',
              stage='one')
    s.move('What each method delivers', [
        ('p', 'Energy is a scalar relation between two states and gives speeds and distances without any vector work. Newton is a relation between force and acceleration at one instant and gives times, accelerations and contact forces. Neither replaces the other.'),
        ('m', r'W_{\mathrm{net}}=\Delta K\quad\text{vs}\quad \sum\mathbf{F}=m\mathbf{a}'),
    ])
    s.move('The standard combination', [
        ('p', 'For a bead on a loop the usual solution is two steps: energy from the release point to the point of interest for the speed, then the radial equation at that point for the normal force. Do them in that order and the algebra stays linear.'),
        ('m', r'v^{2}=v_0^{2}-2gR(1-\cos\phi)'),
        ('m', r'N=\frac{mv^{2}}{R}+mg\cos\phi'),
        ('n', 'energy first, force second: reversing the order costs a square root in the force equation'),
    ])
    s.move('Questions where energy is a dead end', [
        ('p', 'Anything asking for a time, a rate, or a force at an instant. Energy gives no clock, because it says nothing about how the states are connected in time. A block on a spring has the same energy at two different extensions but reaches them at different times.'),
    ])
    s.chip('gate', 'three-way sort', [
        ('p', 'speed or distance: energy. time or acceleration: forces. force at a point: both, in that order.'),
    ])
    s.chip('trap', 'energy for a time', [
        ('p', 'It cannot give one. Use it for the speed, then integrate or use the force method for the clock.'),
    ])
    s.chip('insight', 'why the pair is standard', [
        ('p', 'Energy removes the vector algebra; the radial equation then uses the speed it produced. Each does what it is good at.'),
    ])
    s.figure('decision_map')
    S.append(s)

    # ============================================================ 18 SYSTEM
    s = Sheet('JEE-18-system-energy', 'What changes when the system has two bodies?',
              'Two blocks joined by a spring are pulled apart. The external work is 20 J, but the kinetic energy rises by only 12 J. Where are the other 8 J?',
              K, 18, total, SRC + '§3.11, D6.9',
              'internal work does not vanish: it moves energy into the spring, not out of the system',
              stage='one')
    s.move('The theorem for a system', [
        ('p', 'For a collection of particles, the net work is external plus internal, and both can change the total kinetic energy. The spring is internal, so it takes energy from the blocks and stores it.'),
        ('m', r'W_{\mathrm{ext}}+W_{\mathrm{int}}=\Delta K_{\mathrm{total}}'),
    ])
    s.move('Internal conservative work is a potential', [
        ('p', 'If the internal force is conservative, its work is minus the change in the internal potential. Move that term to the other side and the bookkeeping becomes external work equals the change in kinetic plus potential.'),
        ('m', r'W_{\mathrm{ext}}=\Delta K+\Delta U_s'),
        ('n', 'this is why a two-block spring problem is one energy equation, not two'),
    ])
    s.move('The moving-wedge warning', [
        ('p', 'Internal forces also include the normal between a block and a moving wedge. That normal does work on the block and equal and opposite work on the wedge, so the pair conserves energy while neither body alone does. Energy questions about a wedge must always be asked of the pair.'),
        ('n', 'for the pair, the normal is internal and cancels; for one body it is an external force that does work'),
    ])
    s.chip('key', 'system bookkeeping', [
        ('m', r'W_{\mathrm{ext}}=\Delta K+\Delta U'),
        ('p', 'with U counting every internal conservative interaction'),
    ])
    s.chip('num', 'the opening question', [
        ('p', '20 J in, 12 J of K'),
        ('p', 'so U_spring rose by 8 J: nothing was lost'),
    ])
    s.chip('trap', 'applying one-body conservation to a pair', [
        ('p', 'The block on a moving wedge does not conserve its own energy. The pair does.'),
    ])
    s.figure('system_energy')
    S.append(s)

    # ============================================================ 19 EFFICIENCY
    s = Sheet('JEE-19-efficiency', 'Why does a pump need more power than the water gains?',
              'A pump lifts 100 kg of water per second through 20 m. The water gains 19.6 kW. The motor is rated 25 kW. Where did the rest go?',
              K, 19, total, SRC + '§3.12, §3.5, Q15',
              'efficiency is output over input, and every loss is a term you can name',
              stage='one')
    s.move('The useful part', [
        ('p', 'The water gains gravitational energy at a rate equal to the mass flow times g times the height. That is the useful output, and it is fixed by the job, not by the machine.'),
        ('m', r'P_{\mathrm{out}}=\dot mgh'),
    ])
    s.move('The input and the ratio', [
        ('p', 'The motor supplies more because of friction in the pipes, turbulence, and the inefficiency of the pump itself. The ratio is the efficiency, and it is always below one for a real machine.'),
        ('m', r'\eta=\frac{P_{\mathrm{out}}}{P_{\mathrm{in}}}=\frac{\dot mgh}{P_{\mathrm{in}}}'),
        ('n', '19.6 kW out of 25 kW in is 78 per cent, which is a normal figure for a good pump'),
    ])
    s.move('The same idea elsewhere', [
        ('p', 'A car engine quotes shaft power, but only the wheel power moves the car; the difference is the drivetrain loss. A power station quotes electrical output, not heat input. Every one of these is the same ratio with different names, and in each case the missing power has a physical address.'),
        ('n', 'efficiency questions are bookkeeping questions with one unknown'),
    ])
    s.chip('key', 'efficiency', [
        ('m', r'\eta=\frac{P_{\mathrm{out}}}{P_{\mathrm{in}}},\qquad P_{\mathrm{in}}=\frac{\dot mgh}{\eta}'),
    ])
    s.chip('num', 'a check', [
        ('p', '100 kg/s through 20 m'),
        ('p', 'P_out = 100 x 9.8 x 20 = 19.6 kW'),
    ])
    s.chip('trap', 'efficiency above one', [
        ('p', 'If your answer exceeds 100 per cent, you have used the input as the output or forgotten a loss term.'),
    ])
    s.figure('efficiency')
    S.append(s)

    # ============================================================ 20 CHAIN
    s = Sheet('JEE-20-chain-work', 'Why does lifting a hanging chain cost more than its weight?',
              'A chain is pulled up from a heap at constant speed. At height x the hanging weight is lambda x g, yet the pull must exceed it. Why?',
              K, 20, total, SRC + '§3.12, F6.2, Q25',
              'new links are accelerated from rest, so the pull carries a momentum-flux term',
              stage='one')
    s.move('Force from momentum, not just weight', [
        ('p', 'The hanging part needs support, and the links leaving the heap must be brought from rest to speed v every second. That is a momentum flux, and it needs a force even though the speed is constant.'),
        ('m', r'F=\lambda xg+\lambda v^{2}'),
    ])
    s.move('The energy version tells the same story', [
        ('p', 'The power delivered is Fv, while the energy actually gained is the rate of increase of gravitational plus kinetic energy. The two differ by half lambda v cubed, which is the energy lost in the inelastic jerk as each link is picked up.'),
        ('m', r'P=Fv=\lambda xgv+\lambda v^{3},\qquad \frac{dE}{dt}=\lambda xgv+\frac{1}{2}\lambda v^{3}'),
        ('n', 'the gap is dissipation, not an algebraic slip'),
    ])
    s.move('Where students lose the mark', [
        ('p', 'Using F = lambda x g alone gives a force that is too small and a work that is too small. Using energy conservation with no loss term gives an answer that is also wrong, in the opposite direction. Both errors come from ignoring the momentum flux.'),
        ('n', 'a chain is the standard reminder that mass can be added to a moving system'),
    ])
    s.chip('key', 'the pull', [
        ('m', r'F=\lambda xg+\lambda v^{2}'),
        ('p', 'weight plus momentum flux, at constant speed'),
    ])
    s.chip('num', 'a check', [
        ('p', 'lambda = 0.8 kg/m, x = 2.5 m, v = 1.2 m/s'),
        ('p', 'F = 19.6 + 1.15 = 20.8 N'),
    ])
    s.chip('trap', 'weight only', [
        ('p', 'The flux term is small at low speed but never zero. It is the entire reason a chain feels heavier than its hanging part.'),
    ])
    s.figure('chain_energy')
    S.append(s)

    # ============================================================ 21 SPRING+FRICTION
    s = Sheet('JEE-21-spring-and-friction', 'A spring launches a block onto a rough floor. How far does it go?',
              'Compress a spring, release it, and let friction stop the block. Two energy stores and one loss. Which equation do you write?',
              K, 21, total, SRC + '§3.14, E6, Q13',
              'stored spring energy equals the friction work, and the loss is the bridge between them',
              stage='one')
    s.move('One equation, three terms', [
        ('p', 'At release everything is stored in the spring. At rest everything has become heat in the floor. Nothing else changes, so the spring energy and the friction work are equal.'),
        ('m', r'\frac{1}{2}kx^{2}=\mu_k mg\,d'),
    ])
    s.move('If the block leaves the spring', [
        ('p', 'The block loses contact when the spring passes its natural length, so the launch speed follows from the stored energy alone. From then on it is a decelerating block, and the stopping distance is that kinetic energy over the friction force.'),
        ('m', r'v^{2}=\frac{kx^{2}}{m},\qquad d=\frac{v^{2}}{2\mu_k g}=\frac{kx^{2}}{2\mu_k mg}'),
        ('n', 'the same d as the single-equation route, which is the check'),
    ])
    s.move('The stopping condition', [
        ('p', 'The block stops before the end of the rough patch only if the friction work available exceeds the stored energy. Otherwise it leaves the rough region still moving, and the answer to "how far" is "the whole patch".'),
        ('m', r'\mu_k mg\,L\ge\frac{1}{2}kx^{2}\ \Rightarrow\ \text{it stops inside}'),
    ])
    s.chip('key', 'the balance', [
        ('m', r'\frac{1}{2}kx^{2}=\mu_k mg\,d'),
        ('p', 'stored energy equals the friction loss'),
    ])
    s.chip('num', 'a check', [
        ('p', 'k = 200, x = 0.1, m = 0.5, mu = 0.1'),
        ('p', '1 J = 0.49 d, so d = 2.04 m'),
    ])
    s.chip('trap', 'forgetting the block leaves the spring', [
        ('p', 'The spring stops pushing at its natural length. Do not keep the spring force acting over the whole slide.'),
    ])
    s.figure('spring_friction')
    S.append(s)

    # ============================================================ 22 MAP
    s = Sheet('JEE-22-wpe-map', 'What is the whole chapter in one picture?',
              'Six ideas, a page of formulas and thirty-six questions. Which ideas actually carry the load?',
              K, 22, total, SRC + 'Part 9.1-9.2, Part 13',
              'work is the unit of account, and every result is a ledger with a named loss',
              stage='one')
    s.move('Six ideas, in order', [
        ('p', 'Work measures energy transfer. The theorem turns work into kinetic energy. Power is its rate. A conservative force allows a potential. Conservation is the special case with no losses. Non-conservative bookkeeping is the general case.'),
        ('m', r'W=\int\mathbf{F}\cdot d\mathbf{r},\quad W=\Delta K,\quad P=\frac{dW}{dt},\quad F=-\frac{dU}{dx}'),
    ])
    s.move('The routing table', [
        ('p', 'Speed from a height: conservation. Distance on a rough surface: theorem with friction. Force at a point on a track: energy then radial equation. Power of a vehicle: F v with the resistance and the slope included. Shape of a potential: differentiate for the force, look for the wells.'),
        ('n', 'if two routes disagree, the difference is a term you forgot to name'),
    ])
    s.move('The discipline', [
        ('p', 'Write the two states, list the energy terms that changed, and put every loss on the correct side. A sheet that balances is finished; a sheet that does not is missing a force, and the missing force is almost always friction or a moving support.'),
    ])
    s.chip('gate', 'routing', [
        ('p', 'speed or distance: energy. time or force: Newton. mixed: energy then the radial equation.'),
    ])
    s.chip('trap', 'double counting', [
        ('p', 'Gravity is either a force doing work or a potential energy. Never both in one equation.'),
    ])
    s.chip('insight', 'the one-line summary', [
        ('p', 'Every problem here is a ledger. Name the terms, sign them, and balance them.'),
    ])
    s.figure('wpe_map')
    S.append(s)

    # ============================================================ 23 OMEGA
    s = Sheet('JEE-23-omega-alpha', 'Why describe rotation with an angle at all?',
              'Two points on a wheel, one near the rim and one near the hub, travel different distances in the same time. What do they share?',
              KC, 23, total, SRCC + '§3.7, C1, Q6',
              'every point shares the angle; only the radius converts it into a distance',
              stage='spin')
    s.move('One angle, many arcs', [
        ('p', 'Angular position is the angle swept by the radius from a reference direction. All points of a rigid wheel share it, so one number describes the whole body. Arc length is the radius times that angle, provided the angle is in radians.'),
        ('m', r'\theta=\frac{s}{R},\qquad s=R\theta'),
    ])
    s.move('Rates', [
        ('p', 'Differentiate: angular velocity is the rate of change of the angle, and tangential speed is radius times angular velocity. The same angular velocity gives a larger speed further out, which is why the rim of a wheel moves faster than the hub.'),
        ('m', r'\omega=\frac{d\theta}{dt},\qquad v=R\omega'),
        ('n', 'radians are required: in degrees the factor pi/180 would have to be carried everywhere'),
    ])
    s.move('Period, frequency and rpm', [
        ('p', 'One revolution is 2 pi radians, so period and frequency follow immediately. Revolutions per minute must be converted before use: divide by 60 and multiply by 2 pi. Using rpm directly in v = R omega is the commonest rotation error.'),
        ('m', r'\omega=\frac{2\pi}{T}=2\pi f,\qquad 120\ \mathrm{rpm}=4\pi\ \mathrm{rad/s}'),
    ])
    s.chip('def', 'the three quantities', [
        ('m', r'\theta,\quad \omega=\dot\theta,\quad \alpha=\dot\omega'),
        ('p', 'all shared by every point of a rigid rotator'),
    ])
    s.chip('num', 'a check', [
        ('p', 'R = 0.5 m at 120 rpm'),
        ('p', 'omega = 12.57 rad/s, v = 6.28 m/s, T = 0.5 s'),
    ])
    s.chip('trap', 'rpm into v = R omega', [
        ('p', 'Convert first: radians per second, not revolutions per minute. One factor of 2 pi and one of 60.'),
    ])
    s.figure('omega_alpha')
    S.append(s)

    # ============================================================ 24 ALPHA
    s = Sheet('JEE-24-alpha-kinematics', 'What are the rotation equations for constant angular acceleration?',
              'A flywheel spins up from rest at a constant 3 rad/s². How many turns does it make in 4 s?',
              KC, 24, total, SRCC + '§3.7, §3.9, Q9',
              'the linear equations with x, v, a replaced by theta, omega, alpha',
              stage='spin')
    s.move('The same three equations', [
        ('p', 'Every constant-acceleration result from one-dimensional motion has a rotational twin, because the derivation never used the fact that x was a length. Replace position by angle, velocity by angular velocity, acceleration by angular acceleration.'),
        ('m', r'\omega=\omega_0+\alpha t,\quad \theta=\omega_0t+\frac{1}{2}\alpha t^{2},\quad \omega^{2}=\omega_0^{2}+2\alpha\theta'),
    ])
    s.move('Use the one without t when t is absent', [
        ('p', 'The third equation is the workhorse of rotation questions: it connects speed, angle and acceleration without the clock. If the question gives an angle and asks for a final angular speed, that is the equation.'),
        ('m', r'\omega^{2}=\omega_0^{2}+2\alpha\theta\quad\text{(no }t\text{)}'),
    ])
    s.move('Count turns, not radians', [
        ('p', 'Questions often ask for revolutions. Convert at the end, dividing the angle by 2 pi, and check the answer is sensible: a wheel at 3 rad/s² from rest makes about half a turn per second squared.'),
        ('n', 'theta in radians for every formula, turns only in the final sentence'),
    ])
    s.chip('key', 'the trio', [
        ('m', r'\omega=\omega_0+\alpha t'),
        ('m', r'\omega^{2}=\omega_0^{2}+2\alpha\theta'),
    ])
    s.chip('num', 'the opening question', [
        ('p', 'alpha = 3 rad/s², t = 4 s'),
        ('p', 'theta = 24 rad = 3.8 turns, omega = 12 rad/s'),
    ])
    s.chip('trap', 'alpha is not constant here', [
        ('p', 'These three are for constant alpha only. If alpha varies, integrate it (see OLY 16).'),
    ])
    s.figure('alpha_kinematics')
    S.append(s)

    # ============================================================ 25 OMEGA VECTOR
    s = Sheet('JEE-25-omega-vector', 'Why is angular velocity a vector?',
              'A wheel can spin about a vertical axis or a horizontal one, and the two are physically different. How does a single number capture that?',
              KC, 25, total, SRCC + '§3.7, §3.9, Q17',
              'omega points along the axis, and v = omega cross r gives the tangential speed',
              stage='spin')
    s.move('Direction along the axis', [
        ('p', 'The scalar omega says how fast; the axis says about what. Put them together with the right-hand rule and angular velocity becomes a vector along the rotation axis. For a fixed axis that is overkill, but for a wheel that tilts it is the only correct bookkeeping.'),
        ('m', r'\mathbf{v}=\boldsymbol{\omega}\times\mathbf{r},\qquad |\mathbf{v}|=\omega r\sin\phi'),
    ])
    s.move('The cross product sorts out the geometry', [
        ('p', 'For a point on a circle the radius and the axis are perpendicular, so the sine is one and the speed is omega r. For a point on the axis the cross product vanishes, so the axis itself does not move. That is exactly what a rigid rotation must do.'),
        ('m', r'\mathbf{v}=\boldsymbol{\omega}\times\mathbf{r}\quad\Rightarrow\quad v_\perp=\omega r_\perp'),
        ('n', 'only the distance from the axis matters, not the distance from the origin'),
    ])
    s.move('Adding angular velocities', [
        ('p', 'Angular velocities about the same axis add as scalars; about different axes they add as vectors, and the order matters. That non-commutativity is why a spinning top precesses instead of simply falling, which is beyond this chapter but explains why the vector was needed.'),
    ])
    s.chip('def', 'the vector', [
        ('m', r'\boldsymbol{\omega}\ \text{along the axis},\qquad \mathbf v=\boldsymbol{\omega}\times\mathbf r'),
    ])
    s.chip('num', 'a check', [
        ('p', 'omega = 4 rad/s about z, r = (0.3, 0, 0) m'),
        ('p', 'v = (0, 1.2, 0) m/s'),
    ])
    s.chip('trap', 'using the distance from the origin', [
        ('p', 'Use the perpendicular distance to the axis. A point on the axis has zero speed however far it is from the origin.'),
    ])
    s.figure('omega_vector')
    S.append(s)

    # ============================================================ 26 CENTRIPETAL
    s = Sheet('JEE-26-centripetal', 'Why is circular motion at constant speed still accelerated?',
              'The speedometer reads a constant 60 km/h on a roundabout. Is the car accelerating, and if so, in which direction?',
              KC, 26, total, SRCC + '§3.8, D4.7, Q5',
              'the speed is constant but the direction turns, so the velocity changes toward the centre',
              stage='spin')
    s.move('Velocity is a vector', [
        ('p', 'Constant speed means the magnitude is fixed, not the direction. On a circle the direction turns continuously, so the velocity vector changes every instant, and a changing velocity is an acceleration by definition.'),
        ('n', 'the acceleration is not along the motion; it is across it'),
    ])
    s.move('Derivation 1: differentiate the vectors', [
        ('p', 'Write the position as R times the radial unit vector and differentiate twice. The radial unit vector rotates at omega, so its derivative points along the tangent, and the second derivative brings back a term pointing inward.'),
        ('m', r'\mathbf{a}=-R\omega^{2}\hat r+R\dot\omega\hat\theta'),
    ])
    s.move('Derivation 2: the velocity triangle', [
        ('p', 'Draw the velocity at two nearby instants. Both have length v, and the angle between them is the angle turned. The change is v times that angle, pointing inward, so the acceleration magnitude is v omega.'),
        ('m', r'a_c=\frac{v^{2}}{R}=\omega^{2}R=v\omega'),
        ('n', 'two independent routes, one result: that is the standard JEE proof requirement'),
    ])
    s.chip('key', 'centripetal acceleration', [
        ('m', r'a_c=\frac{v^{2}}{R}=\omega^{2}R'),
        ('p', 'directed toward the centre, at every instant'),
    ])
    s.chip('num', 'a check', [
        ('p', '90 km/h = 25 m/s on R = 100 m'),
        ('p', 'a_c = 6.25 m/s², about 0.64 g'),
    ])
    s.chip('trap', 'calling it a force', [
        ('p', 'Centripetal acceleration is a kinematic fact. The force that supplies it is whatever happens to point inward: friction, tension, gravity, normal.'),
    ])
    s.figure('centripetal_two_ways')
    S.append(s)

    return S
