"""Worked-number blocks: one per sheet, appended as the last numbered move.

Each entry is (heading, [blocks]) in the same grammar as the content modules.
Every number is recomputed from the source's data rather than copied, and the
same numbers are re-derived independently in test_exports.py.
"""

EX = {}

EX['JEE-01-work-sign'] = ('A worked pair of pulls', [
    ('p', 'A 20 kg crate is dragged 6 m by a 120 N rope at 35° above the horizontal, with friction 50 N. Find the work of the rope, of friction, and the net work.'),
    ('m', r'W_F=120(6)\cos35^\circ=590\ \mathrm{J}'),
    ('m', r'W_f=-50(6)=-300\ \mathrm{J},\qquad W_{\mathrm{net}}=290\ \mathrm{J}'),
    ('n', 'gravity and the normal do nothing: both are vertical, the displacement is horizontal'),
])

EX['JEE-02-fx-area'] = ('A worked area', [
    ('p', 'A force F = 6x N acts from x = 0 to x = 2 m, then falls linearly to zero at x = 4 m. Find the total work.'),
    ('m', r'W_1=\int_0^2 6x\,dx=12\ \mathrm{J},\qquad W_2=\tfrac{1}{2}(12)(2)=12\ \mathrm{J}'),
    ('m', r'W=24\ \mathrm{J}\ \text{(the two areas add, } F \text{ never reversed)}'),
    ('n', 'the second part is a triangle: 12 N at the start of it, zero at the end'),
])

EX['JEE-03-force-audit'] = ('A worked audit', [
    ('p', 'A 5 kg block slides 4 m down a 30° incline with mu_k = 0.25. Find the work of each force and the final speed from rest.'),
    ('m', r'W_g=5(9.8)(4)(0.5)=98\ \mathrm{J},\qquad W_f=-0.25(42.4)(4)=-42.4\ \mathrm{J}'),
    ('m', r'W_{\mathrm{net}}=55.6\ \mathrm{J}\ \Rightarrow\ v=\sqrt{2(55.6)/5}=4.72\ \mathrm{m/s}'),
    ('n', 'the normal does zero work on a fixed incline, however large it is'),
])

EX['JEE-04-we-theorem'] = ('A worked theorem', [
    ('p', 'A 1200 kg car at 20 m/s brakes to rest in 55 m. Find the average braking force, then the work done.'),
    ('m', r'W_{\mathrm{net}}=0-\tfrac{1}{2}(1200)(400)=-240\ \mathrm{kJ}'),
    ('m', r'\bar F=\frac{240000}{55}=4.36\ \mathrm{kN}\ \text{backward}'),
    ('n', 'no time was needed; the theorem is the shortest route to a force when distances are given'),
])

EX['JEE-05-ke-frames'] = ('A worked frame shift', [
    ('p', 'A 2 kg ball moves at 5 m/s in the ground frame; a train moves at 3 m/s the same way. Compare the kinetic energies and the work to stop it in each frame.'),
    ('m', r'K_{\mathrm{ground}}=25\ \mathrm{J},\qquad K_{\mathrm{train}}=\tfrac{1}{2}(2)(2)^{2}=4\ \mathrm{J}'),
    ('m', r'W_{\mathrm{stop}}=-25\ \mathrm{J}\ \text{vs}\ -4\ \mathrm{J}\ \text{depending on the frame}'),
    ('n', 'both are correct: the stopping distance differs between the frames too'),
])

EX['JEE-06-friction-heat'] = ('A worked heat budget', [
    ('p', 'A 3 kg block at 8 m/s slides on mu_k = 0.35 until it stops. Find the distance, the heat, and the temperature rise of a 0.4 kg steel slider taking half the heat (c = 450 J/kg K).'),
    ('m', r'd=\frac{64}{2(0.35)(9.8)}=9.3\ \mathrm{m},\qquad Q=96\ \mathrm{J}'),
    ('m', r'\Delta T=\frac{48}{0.4(450)}=0.27\ \mathrm{K}'),
    ('n', 'all 96 J is still there, just no longer mechanical'),
])

EX['JEE-07-power-definition'] = ('A worked power pair', [
    ('p', 'A crane lifts 800 kg through 15 m in 20 s. Find the average power, and the instantaneous power at a steady 0.75 m/s.'),
    ('m', r'\bar P=\frac{800(9.8)(15)}{20}=5.88\ \mathrm{kW}'),
    ('m', r'P=Fv=7840(0.75)=5.88\ \mathrm{kW}'),
    ('n', 'they agree because the speed is constant: average equals instantaneous for uniform motion'),
])

EX['JEE-08-constant-power'] = ('A worked spin-up', [
    ('p', 'A 1500 kg car with a 60 kW engine starts from rest at constant power. Find the speed at 5 s, 20 s, and the time to 30 m/s.'),
    ('m', r'v(5)=\sqrt{2(60000)(5)/1500}=20\ \mathrm{m/s}'),
    ('m', r'v(20)=40\ \mathrm{m/s},\qquad t(30)=\frac{1500(900)}{2(60000)}=11.3\ \mathrm{s}'),
    ('n', 't grows as v squared, so the last 10 m/s needs more time than the first 20'),
])

EX['JEE-09-slope-power'] = ('A worked climb', [
    ('p', 'A 1200 kg car climbs a 6° slope at 25 m/s against 600 N of drag. Find the power at the wheels and the extra power the slope costs.'),
    ('m', r'P=(600+1200(9.8)\sin6^\circ)(25)'),
    ('m', r'=(600+1230)(25)=45.8\ \mathrm{kW}'),
    ('n', 'the slope alone is 30.8 kW of it, two thirds of the total'),
])

EX['JEE-10-conservative'] = ('A worked loop test', [
    ('p', 'A force F = (3y, 0) N acts in the plane. Compute the work round the unit square from the origin and decide.'),
    ('m', r'\left|\oint F\cdot dr\right|=3(1)(1)=3\ \mathrm{J}\neq0'),
    ('m', r'\partial_xF_y-\partial_yF_x=0-3=-3\neq0\ \text{so no potential}'),
    ('n', 'the two tests agree, as they must: the field is not a gradient'),
])

EX['JEE-11-potential-energy'] = ('A worked zero shift', [
    ('p', 'A 2 kg book sits 1.5 m above a table, which is 0.9 m above the floor. Find U relative to the table and to the floor, and the change if it falls to the table.'),
    ('m', r'U_{\mathrm{table}}=0,\qquad U_{\mathrm{floor}}=29.4\ \mathrm{J},\qquad U_{\mathrm{floor,book}}=47.0\ \mathrm{J}'),
    ('m', r'W_g=mg(1.5)=29.4\ \mathrm{J}\ \text{whichever zero is chosen}'),
    ('n', 'only the difference is physical, so the zero is a convenience'),
])

EX['JEE-12-spring-energy'] = ('A worked spring', [
    ('p', 'A spring of k = 320 N/m is compressed 12 cm and launches a 0.25 kg ball. Find the stored energy and the launch speed.'),
    ('m', r'U=\tfrac{1}{2}(320)(0.12)^{2}=2.30\ \mathrm{J}'),
    ('m', r'v=\sqrt{2(2.30)/0.25}=4.29\ \mathrm{m/s}'),
    ('n', 'the force at full compression is 38.4 N, but the average that did the work was 19.2 N'),
])

EX['JEE-13-gravity-paths'] = ('A worked path comparison', [
    ('p', 'A 70 kg hiker climbs 800 m of altitude along a 2.4 km trail. Compare the work against gravity with the work if the trail were 1.2 km.'),
    ('m', r'W=mg\Delta h=70(9.8)(800)=549\ \mathrm{kJ}'),
    ('m', r'\text{half the trail length: the same } 549\ \mathrm{kJ}'),
    ('n', 'the trail length sets the effort, not the gravitational work'),
])

EX['JEE-14-energy-conservation'] = ('A worked conservation', [
    ('p', 'A 0.6 kg ball is released from rest at the top of a 2.2 m ramp and leaves horizontally. Find its speed at the bottom and the horizontal distance after a 1.4 m drop.'),
    ('m', r'v=\sqrt{2(9.8)(2.2)}=6.57\ \mathrm{m/s}'),
    ('m', r't=\sqrt{2(1.4)/9.8}=0.535\ \mathrm{s},\qquad x=3.51\ \mathrm{m}'),
    ('n', 'energy gives the speed, kinematics gives the range: the usual division of labour'),
])

EX['JEE-15-u-graph'] = ('A worked well', [
    ('p', 'A particle of 0.5 kg moves in U(x) = 2x² − 8x J. It is released from rest at x = 6 m. Find the turning points and the maximum speed.'),
    ('m', r'E=U(6)=24\ \mathrm{J},\qquad 2x^{2}-8x=24\ \Rightarrow\ x=-2,\ 6\ \mathrm{m}'),
    ('m', r'v_{\max}=\sqrt{2(24-(-8))/0.5}=11.3\ \mathrm{m/s}\ \text{at } x=2\ \mathrm{m}'),
    ('n', 'the well is at 2 m, the turning points are the two roots, and the motion is bounded'),
])

EX['JEE-16-force-gradient'] = ('A worked gradient', [
    ('p', 'For U(x) = x³ − 3x J, find the force, the equilibria, and their stability.'),
    ('m', r'F=-(3x^{2}-3)=3-3x^{2}\ \mathrm{N},\qquad x=\pm1\ \mathrm{m}'),
    ('m', r'U_{xx}=6x:\ \text{stable at } x=1,\ \text{unstable at } x=-1'),
    ('n', 'at x = 1 the force pushes back toward 1 for small displacements'),
])

EX['JEE-17-energy-or-force'] = ('A worked combination', [
    ('p', 'A 0.3 kg bead slides from rest at 3R above the bottom of a smooth loop of radius 0.5 m. Find the speed and the normal at the top.'),
    ('m', r'v^{2}=2(9.8)(3-2)(0.5)=9.8\ \Rightarrow\ v=3.13\ \mathrm{m/s}'),
    ('m', r'N=\frac{0.3(9.8)}{0.5}-0.3(9.8)=5.88-2.94=2.9\ \mathrm{N}'),
    ('n', 'energy first, radial second: both steps are one line'),
])

EX['JEE-18-system-energy'] = ('A worked pair', [
    ('p', 'Two blocks, 1 kg and 2 kg, are joined by a spring (k = 200 N/m) and pulled apart so the spring stretches 0.2 m from natural length. Released from rest, find the total kinetic energy when the stretch is 0.1 m.'),
    ('m', r'U_i=\tfrac{1}{2}(200)(0.04)=4.0\ \mathrm{J},\qquad U_f=\tfrac{1}{2}(200)(0.01)=1.0\ \mathrm{J}'),
    ('m', r'K_{\mathrm{total}}=3.0\ \mathrm{J}\ \text{shared between the two blocks}'),
    ('n', 'the pair conserves energy; neither block does on its own'),
])

EX['JEE-19-efficiency'] = ('A worked pump', [
    ('p', 'A pump raises 0.05 m³/s of water through 12 m. The motor draws 9 kW. Find the efficiency.'),
    ('m', r'P_{\mathrm{out}}=1000(0.05)(9.8)(12)=5.88\ \mathrm{kW}'),
    ('m', r'\eta=5.88/9=0.65'),
    ('n', 'a third of the electrical input ends up as heat in the water and the pipes'),
])

EX['JEE-20-chain-work'] = ('A worked chain', [
    ('p', 'A 3 m chain of 6 kg is lifted from a heap at a steady 0.8 m/s. Find the force when 2 m is up, and the power at that instant.'),
    ('m', r'F=\lambda xg+\lambda v^{2}=2(9.8)(2)+2(0.64)=40.5\ \mathrm{N}'),
    ('m', r'P=Fv=32.4\ \mathrm{W},\qquad \lambda v^{3}=1.0\ \mathrm{W}\ \text{of it is lost}'),
    ('n', 'the flux term is small at this speed but it never vanishes'),
])

EX['JEE-21-spring-and-friction'] = ('A worked launch', [
    ('p', 'A 1.2 kg block is launched by a spring of k = 400 N/m compressed 15 cm on a floor with mu_k = 0.25. Find the sliding distance after release.'),
    ('m', r'\tfrac{1}{2}(400)(0.0225)=4.5\ \mathrm{J}=0.25(1.2)(9.8)d'),
    ('m', r'd=\frac{4.5}{2.94}=1.53\ \mathrm{m}'),
    ('n', 'the block leaves the spring at its natural length; the friction acts over the whole 1.53 m'),
])

EX['JEE-22-wpe-map'] = ('A worked routing', [
    ('p', 'A 2 kg block slides 5 m down a 35° rough incline and then compresses a spring of k = 800 N/m. mu_k = 0.2. Find the compression.'),
    ('m', r'E_{\mathrm{avail}}=2(9.8)(5\sin35^\circ)-0.2(2)(9.8\cos35^\circ)(5)'),
    ('m', r'=56.2-16.1=40.1\ \mathrm{J}\ \Rightarrow\ x=\sqrt{2(40.1)/800}=0.32\ \mathrm{m}'),
    ('n', 'one energy equation with a friction line, no forces resolved twice'),
])

EX['JEE-23-omega-alpha'] = ('A worked wheel', [
    ('p', 'A wheel of radius 0.35 m spins at 300 rpm. Find omega, the rim speed, the period, and the angle turned in 3 s.'),
    ('m', r'\omega=300(2\pi)/60=31.4\ \mathrm{rad/s},\qquad v=11.0\ \mathrm{m/s}'),
    ('m', r'T=0.20\ \mathrm{s},\qquad \theta=94.2\ \mathrm{rad}=15\ \text{turns}'),
    ('n', 'the rim moves at 40 km/h while the hub is at rest'),
])

EX['JEE-24-alpha-kinematics'] = ('A worked spin-up', [
    ('p', 'A disc accelerates uniformly from 4 rad/s to 20 rad/s in 8 s. Find alpha, the angle turned, and the turns.'),
    ('m', r'\alpha=\frac{20-4}{8}=2.0\ \mathrm{rad/s^{2}}'),
    ('m', r'\theta=\frac{20^{2}-4^{2}}{2(2)}=96\ \mathrm{rad}=15.3\ \text{turns}'),
    ('n', 'the no-time equation was the shorter route: 96 rad directly'),
])

EX['JEE-25-omega-vector'] = ('A worked cross product', [
    ('p', 'A disc spins at 12 rad/s about the z axis. Find the velocity of the point r = (0.4, 0.3, 0) m.'),
    ('m', r'\mathbf v=\boldsymbol{\omega}\times\mathbf r=(0,0,12)\times(0.4,0.3,0)=(-3.6,4.8,0)'),
    ('m', r'v=6.0\ \mathrm{m/s},\qquad r_\perp=0.5\ \mathrm{m}'),
    ('n', 'v = omega r_perp with the perpendicular distance, which is the check'),
])

EX['JEE-26-centripetal'] = ('A worked roundabout', [
    ('p', 'A car takes a 60 m radius roundabout at 45 km/h. Find the centripetal acceleration and the friction coefficient needed.'),
    ('m', r'v=12.5\ \mathrm{m/s},\qquad a_c=\frac{156}{60}=2.60\ \mathrm{m/s^{2}}'),
    ('m', r'\mu=\frac{a_c}{g}=0.27'),
    ('n', 'below a dry-road 0.7, above an icy 0.1: the number decides the story'),
])

# ---------------------------------------------------------------- OLYMPIAD

EX['Olympiad-01-cm-split'] = ('A worked split', [
    ('p', 'A 3 kg block at 4 m/s hits a 1 kg block at rest and they stick. Find the CM speed, the CM energy, and the energy lost.'),
    ('m', r'V=\frac{12}{4}=3\ \mathrm{m/s},\qquad K_{\mathrm{cm}}=\tfrac{1}{2}(4)(9)=18\ \mathrm{J}'),
    ('m', r'K_i=24\ \mathrm{J}\ \Rightarrow\ \text{lost }6\ \mathrm{J},\ \text{which is } K_{\mathrm{rel}}'),
    ('n', 'the 18 J of drift survives the collision untouched'),
])

EX['Olympiad-02-effective-potential'] = ('A worked barrier', [
    ('p', 'A satellite orbits at 7000 km from the Earth centre. Find the effective potential at that radius per unit mass, and compare the two terms.'),
    ('m', r'-\frac{GM}{r}=-5.69\times10^{7}\ \mathrm{J/kg}'),
    ('m', r'+\frac{v^{2}}{2}=+2.85\times10^{7}\ \mathrm{J/kg}'),
    ('n', 'the sum is minus half the magnitude: the virial relation for a circular orbit'),
])

EX['Olympiad-03-bouncing-ball'] = ('A worked bounce', [
    ('p', 'A ball dropped from 1.8 m rebounds to 1.15 m. Find e, the total distance and the total time.'),
    ('m', r'e=\sqrt{1.15/1.8}=0.80,\qquad s=1.8\frac{1.64}{0.36}=8.2\ \mathrm{m}'),
    ('m', r't=\sqrt{0.367}\cdot 9=0.606(9)=5.45\ \mathrm{s}'),
    ('n', 'one bounce is over in 0.6 s; the infinite tail takes five more'),
])

EX['Olympiad-04-rolling-energy'] = ('A worked roll', [
    ('p', 'A solid sphere, a disc and a ring roll from rest down a 2 m high slope. Find each bottom speed.'),
    ('m', r'v=\sqrt{\frac{2gh}{1+I/mR^{2}}}:\ 5.29,\ 5.11,\ 4.43\ \mathrm{m/s}'),
    ('m', r'\text{sphere } (2/5),\ \text{disc } (1/2),\ \text{ring } (1)'),
    ('n', 'all three take the same time only if the slope is long enough to reach these speeds'),
])

EX['Olympiad-05-block-on-wedge'] = ('A worked wedge', [
    ('p', 'm = 1 kg, M = 4 kg, theta = 30°, released from 0.5 m up the face. Find both speeds at the bottom of the face.'),
    ('m', r'u^{2}=\frac{2(9.8)(0.5)(5)}{4.25}=11.5\ \Rightarrow\ u=3.39\ \mathrm{m/s}'),
    ('m', r'V=\frac{1(3.39)(0.866)}{5}=0.59\ \mathrm{m/s}'),
    ('n', 'the block drops 0.5 m but its ground speed is only 2.9 m/s, below the 3.1 m/s fixed-wedge value'),
])

EX['Olympiad-06-satellite-launch'] = ('A worked launch', [
    ('p', 'Find the energy to lift 1 kg from the Earth surface to a 400 km orbit, and compare it with escape.'),
    ('m', r'\Delta E=GM\left(\frac{1}{R}-\frac{1}{2r}\right)=6.26\times10^{7}-2.94\times10^{7}'),
    ('m', r'=3.3\times10^{7}\ \mathrm{J/kg}=33\ \mathrm{MJ/kg}'),
    ('n', 'escape from the same point is 62.5 MJ/kg, so orbit costs just over half'),
])

EX['Olympiad-07-chain-unroll'] = ('A worked unroll', [
    ('p', 'A 4 kg, 2 m chain lies coiled on a table. It is pulled up at a steady 1.5 m/s. Find the pull and the loss rate when 1.2 m is up.'),
    ('m', r'F=\lambda xg+\lambda v^{2}=2(9.8)(1.2)+2(2.25)=28.0\ \mathrm{N}'),
    ('m', r'\dot Q=\tfrac{1}{2}\lambda v^{3}=3.4\ \mathrm{W}\ \text{of the } 42\ \mathrm{W}\ \text{delivered}'),
    ('n', '8 per cent is lost in the jerk at this speed, and it grows as v cubed'),
])

EX['Olympiad-08-bead-on-hoop'] = ('A worked hoop', [
    ('p', 'A bead on a 0.4 m hoop which spins at 5 rad/s. Find the critical speed and the equilibrium angle.'),
    ('m', r'\omega_c=\sqrt{9.8/0.4}=4.95\ \mathrm{rad/s}'),
    ('m', r'\cos\theta=\frac{9.8}{25(0.4)}=0.98\ \Rightarrow\ \theta=11^\circ'),
    ('n', 'just above the threshold the bead sits very close to the bottom'),
])

EX['Olympiad-09-restitution'] = ('A worked restitution', [
    ('p', 'A ball falls 3 m and rebounds to 1.08 m. Find e and the fraction of energy kept.'),
    ('m', r'e=\sqrt{1.08/3}=0.60'),
    ('m', r'\frac{K_f}{K_i}=e^{2}=0.36'),
    ('n', 'it loses nearly two thirds of its energy at one impact'),
])

EX['Olympiad-10-flywheel'] = ('A worked flywheel', [
    ('p', 'A flywheel of I = 8 kg m² is spun by a 300 W motor from rest. Find omega at 6 s and the time to 40 rad/s.'),
    ('m', r'\omega=\sqrt{2(300)(6)/8}=21.2\ \mathrm{rad/s}'),
    ('m', r't=\frac{8(1600)}{2(300)}=21.3\ \mathrm{s}'),
    ('n', 'the last 20 rad/s takes three times as long as the first 20'),
])

EX['Olympiad-11-pseudo-work'] = ('A worked frame', [
    ('p', 'A 0.2 kg ball hangs in a cart accelerating at 4 m/s². It swings 0.25 m backward relative to the cart. Find the pseudo work and the ball speed in the cart frame.'),
    ('m', r'W_{\mathrm{pseudo}}=ma_0d=0.2(4)(0.25)=0.20\ \mathrm{J}'),
    ('m', r'v=\sqrt{2(0.20)/0.2}=1.41\ \mathrm{m/s}'),
    ('n', 'in the ground frame the tension did that work instead'),
])

EX['Olympiad-12-path-integral'] = ('A worked curl', [
    ('p', 'Test F = (2xy, x²) N for conservatism, and find its potential.'),
    ('m', r'\partial_xF_y=2x=\partial_yF_x\ \text{so the curl vanishes}'),
    ('m', r'U=-x^{2}y+\text{const}'),
    ('n', 'a vanishing curl plus a simply connected region is the licence for a potential'),
])

EX['Olympiad-13-drag-power'] = ('A worked drag', [
    ('p', 'A cyclist and bike of 85 kg push 250 W. With b = 0.32, find the top speed on the flat.'),
    ('m', r'250=0.32v^{3}\ \Rightarrow\ v=(781)^{1/3}=9.2\ \mathrm{m/s}'),
    ('m', r'\text{at } 500\ \mathrm{W}:\ v=11.6\ \mathrm{m/s}'),
    ('n', 'twice the power buys 26 per cent more speed, which is the whole story of cycling'),
])

EX['Olympiad-14-energy-limits'] = ('A worked ratio', [
    ('p', 'An electron at 2.0e8 m/s: what fraction of its kinetic energy does the classical formula miss?'),
    ('m', r'\gamma=1.34,\qquad K=(\gamma-1)mc^{2}=0.342(511)=175\ \mathrm{keV}'),
    ('m', r'\tfrac{1}{2}mv^{2}=114\ \mathrm{keV}\ \text{: classical is } 35\ \%\ \text{low}'),
    ('n', 'at v/c = 0.67 the classical formula is no longer an approximation, it is wrong'),
])

EX['Olympiad-15-tangential-normal'] = ('A worked curve', [
    ('p', 'A car at 18 m/s brakes at 3 m/s² while on a 40 m radius curve. Find the total acceleration and its angle from the radius.'),
    ('m', r'a_n=\frac{324}{40}=8.1\ \mathrm{m/s^{2}},\qquad a=\sqrt{9+65.6}=8.64\ \mathrm{m/s^{2}}'),
    ('m', r'\phi=\tan^{-1}\frac{3}{8.1}=20.3^\circ'),
    ('n', 'the car is slowing and turning at once, and the vector says which dominates'),
])

EX['Olympiad-16-variable-alpha'] = ('A worked decay', [
    ('p', 'A wheel slows with alpha = −0.8 omega rad/s². From 25 rad/s, find omega at 2 s and the total angle before stopping.'),
    ('m', r'\omega=25e^{-1.6}=5.05\ \mathrm{rad/s}'),
    ('m', r'\theta=\frac{\omega_0}{k}=\frac{25}{0.8}=31.3\ \mathrm{rad}=5.0\ \text{turns}'),
    ('n', 'an exponential spin-down never quite stops, but the angle converges'),
])

EX['Olympiad-17-relative-angular'] = ('A worked meeting', [
    ('p', 'Two runners on a 200 m track go at 6 and 4.5 m/s the same way. The track length, not the radius, is given. When do they next meet?'),
    ('m', r'R=\frac{200}{2\pi}=31.8\ \mathrm{m},\quad \omega_1=0.188,\ \omega_2=0.141\ \mathrm{rad/s}'),
    ('m', r'T_{\mathrm{meet}}=\frac{2\pi}{0.0471}=133\ \mathrm{s}=2.2\ \text{min}'),
    ('n', 'opposite ways the rates add: they then meet every 19 s'),
])

EX['Olympiad-18-work-radial'] = ('A worked split', [
    ('p', 'A 0.5 kg bead on a 0.6 m string is at 4 m/s when the string makes 60° with the vertical, moving up. Find the tangential acceleration and the tension.'),
    ('m', r'a_t=g\sin60^\circ=8.49\ \mathrm{m/s^{2}}'),
    ('m', r'T=\frac{0.5(16)}{0.6}+0.5(9.8)\cos60^\circ=13.3+2.45=15.8\ \mathrm{N}'),
    ('n', 'gravity does the speeding up or slowing down; the string only bends the path'),
])

EX['Olympiad-19-vertical-circle-energy'] = ('A worked loop', [
    ('p', 'A 0.2 kg bead is released from rest 1.5 m above the bottom of a 0.5 m loop. Find the speed at the top and say whether it stays on.'),
    ('m', r'v^{2}=2(9.8)(1.5-1.0)=9.8\ \Rightarrow\ v=3.13\ \mathrm{m/s}'),
    ('m', r'v_{\mathrm{top,min}}^{2}=gR=4.9\ \text{: }9.8>4.9,\ \text{it stays on}'),
    ('n', 'the margin is exactly a factor of two in v squared'),
])

EX['Olympiad-20-string-vs-rod'] = ('A worked comparison', [
    ('p', 'A 0.2 kg ball on a 0.9 m string is whirled in a vertical circle. Find the minimum bottom speed and the tension there.'),
    ('m', r'v_{\mathrm{bot}}=\sqrt{5(9.8)(0.9)}=6.64\ \mathrm{m/s}'),
    ('m', r'T_{\mathrm{bot}}=6mg=11.8\ \mathrm{N}'),
    ('n', 'a rod would need only 5.94 m/s, and a bottom force of 5mg'),
])

EX['Olympiad-21-conical-pendulum'] = ('A worked whirl', [
    ('p', 'A 1.2 m string carries a 0.3 kg bob at 30° to the vertical. Find the tension, speed and period.'),
    ('m', r'T=\frac{0.3(9.8)}{\cos30^\circ}=3.40\ \mathrm{N}'),
    ('m', r'v=\sqrt{9.8(1.2)\sin30^\circ\tan30^\circ}=1.84\ \mathrm{m/s}'),
    ('m', r'T_{\mathrm{period}}=2\pi\sqrt{1.2(0.866)/9.8}=2.05\ \mathrm{s}'),
    ('n', 'the same string at 60° would need 2.4 times the speed and swing faster'),
])

EX['Olympiad-22-banked-limits'] = ('A worked band', [
    ('p', 'A 120 m radius corner is banked at 15° with mu_s = 0.45. Find both speed limits.'),
    ('m', r'v_{\max}^{2}=1176\frac{0.259+0.435}{0.966-0.117}=963\ \Rightarrow\ 31.0\ \mathrm{m/s}'),
    ('m', r'v_{\min}^{2}=1176\frac{0.259-0.435}{0.966+0.117}<0\ \Rightarrow\ v_{\min}=0'),
    ('n', 'mu exceeds tan 15° = 0.268, so the car can stand still on the bank'),
])

EX['Olympiad-23-rotor-wall'] = ('A worked rotor', [
    ('p', 'A 70 kg rider circles a 5 m radius wall of death at mu_s = 0.6. Find the minimum speed and the normal force then.'),
    ('m', r'v_{\min}=\sqrt{9.8(5)/0.6}=9.04\ \mathrm{m/s}'),
    ('m', r'N=\frac{70(81.7)}{5}=1.14\ \mathrm{kN},\qquad f=686\ \mathrm{N}'),
    ('n', 'at the minimum speed the friction is exactly at its ceiling'),
])

EX['Olympiad-24-curvature'] = ('A worked curvature', [
    ('p', 'A projectile is launched at 25 m/s at 40°. Find the radius of curvature at the apex and at launch.'),
    ('m', r'\rho_{\mathrm{apex}}=\frac{625\cos^{2}40^\circ}{9.8}=37.3\ \mathrm{m}'),
    ('m', r'\rho_{\mathrm{launch}}=\frac{625}{9.8\cos40^\circ}=83.2\ \mathrm{m}'),
    ('n', 'the path bends hardest where it is least steep and slowest in the horizontal'),
])
