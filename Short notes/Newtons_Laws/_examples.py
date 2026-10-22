"""Worked-number blocks: one per sheet, appended as the last numbered move.

Each entry is (heading, [blocks]) in the same grammar as the content modules.
The numbers are recomputed from the source's data rather than copied, so a
disagreement with the printed exemplar is a finding, not a typo.
"""

EX = {}

EX['JEE-01-inertial-frames'] = ('A worked test with real numbers', [
    ('p', 'A puck slides on a level air table at 3 m/s while the room is at rest. A second puck is released inside a van braking at 2 m/s². What does each observer measure?'),
    ('m', r'\text{ground: }a=0\quad\text{van: }a=2\ \mathrm{m/s}^2\ \text{forward}'),
    ('n', 'the van observer must invent f = ma = 2m forward; the ground observer invents nothing'),
])

EX['JEE-02-second-law'] = ('A worked impulse budget', [
    ('p', 'A 0.145 kg cricket ball arrives at 30 m/s and leaves at 40 m/s along the same line, contact lasting 1.2 ms. Find the impulse and the mean force.'),
    ('m', r'J=m\Delta v=0.145(40+30)=10.2\ \mathrm{N\,s}'),
    ('m', r'\bar F=\frac{J}{\Delta t}=\frac{10.2}{1.2\times10^{-3}}=8.5\ \mathrm{kN}'),
    ('n', 'the ball’s weight, 1.4 N, is 0.017 % of that: gravity can be dropped during the hit'),
])

EX['JEE-03-third-law'] = ('A worked pair audit', [
    ('p', 'A 2 kg block rests on a table. List the forces on the block and on the table, then pair them.'),
    ('m', r'\text{block: }N=19.6\ \mathrm{N}\uparrow,\ mg=19.6\ \mathrm{N}\downarrow'),
    ('m', r'\text{table: }19.6\ \mathrm{N}\downarrow\ \text{from block},\ 19.6\ \mathrm{N}\uparrow\ \text{from floor}'),
    ('n', 'the third-law partner of N on the block is the 19.6 N push on the table, not mg'),
])

EX['JEE-04-free-body'] = ('A worked incline', [
    ('p', 'A 5 kg block slides down a 30° rough incline with μ_k = 0.2. Find N, the friction, and the acceleration.'),
    ('m', r'N=mg\cos30^\circ=42.4\ \mathrm{N},\qquad f=\mu_kN=8.5\ \mathrm{N}'),
    ('m', r'a=g(\sin30^\circ-\mu_k\cos30^\circ)=9.8(0.5-0.173)=3.2\ \mathrm{m/s}^2'),
    ('n', 'N is 42.4 N, not the 49 N weight: that difference is the whole point of resolving'),
])

EX['JEE-05-apparent-weight'] = ('A worked lift ride', [
    ('p', 'A 60 kg passenger stands on a scale in a lift that accelerates up at 2 m/s², then brakes at 2 m/s². What does the scale read?'),
    ('m', r'N=m(g+a)=60(11.8)=708\ \mathrm{N}'),
    ('m', r'N=m(g-a)=60(7.8)=468\ \mathrm{N}'),
    ('n', 'true weight is 588 N throughout; only the reading changes'),
])

EX['JEE-06-lami'] = ('A worked lamp', [
    ('p', 'A 100 N lamp hangs from two wires making 30° and 60° with the ceiling. Find both tensions by Lami.'),
    ('m', r'\frac{T_1}{\sin120^\circ}=\frac{T_2}{\sin150^\circ}=\frac{100}{\sin90^\circ}'),
    ('m', r'T_1=86.6\ \mathrm{N},\qquad T_2=50.0\ \mathrm{N}'),
    ('n', 'resolving gives the same pair, in twice the lines'),
])

EX['JEE-07-static-friction'] = ('A worked push', [
    ('p', 'A 4 kg crate sits on a floor with μ_s = 0.5. You push with 15 N, then with 25 N. What is the friction each time?'),
    ('m', r'\mu_sN=0.5(39.2)=19.6\ \mathrm{N}'),
    ('m', r'F=15\ \mathrm{N}:\ f=15\ \mathrm{N}\quad F=25\ \mathrm{N}:\ \text{it slides}'),
    ('n', 'at 25 N the friction drops to μ_k N, so the crate accelerates rather than creeping'),
])

EX['JEE-08-friction-direction'] = ('A worked belt', [
    ('p', 'A 2 kg package is dropped on a belt running at 4 m/s, with μ_k = 0.3. How long until it stops slipping, and how far does it travel?'),
    ('m', r'a=\mu_kg=2.94\ \mathrm{m/s}^2,\qquad t=\frac{4}{2.94}=1.36\ \mathrm{s}'),
    ('m', r's_{\mathrm{pkg}}=\tfrac12(4)(1.36)=2.72\ \mathrm{m},\qquad s_{\mathrm{belt}}=5.44\ \mathrm{m}'),
    ('n', 'the belt slides 2.72 m under the package, and that gap is the friction heat'),
])

EX['JEE-09-min-pull'] = ('A worked optimum', [
    ('p', 'A 20 kg crate on μ = 0.4 needs to be dragged. Compare a horizontal pull with the optimum angle.'),
    ('m', r'F_0=\mu mg=78.4\ \mathrm{N}'),
    ('m', r'F_{\min}=\frac{78.4}{\sqrt{1+0.16}}=72.8\ \mathrm{N}\ \text{at}\ 21.8^\circ'),
    ('n', '5.6 N saved, and the crate unloads 27 N of normal force while being pulled'),
])

EX['JEE-10-stacked-blocks'] = ('A worked stack', [
    ('p', 'm = 2 kg on M = 3 kg, μ_s = 0.4 between them, floor frictionless. How hard can you push the lower block?'),
    ('m', r'F_{\max}=\mu_sg(M+m)=0.4(9.8)(5)=19.6\ \mathrm{N}'),
    ('m', r'a_{\max}=\mu_sg=3.92\ \mathrm{m/s}^2'),
    ('n', 'push 19.6 N and the pair moves at 3.92 m/s²; push 25 N and the top one lags'),
])

EX['JEE-11-system-vs-parts'] = ('A worked contact force', [
    ('p', 'F = 30 N pushes m₁ = 2 kg into m₂ = 4 kg on a frictionless floor. Find a and the contact force.'),
    ('m', r'a=\frac{30}{6}=5\ \mathrm{m/s}^2'),
    ('m', r'N=m_2a=20\ \mathrm{N},\qquad\text{check: }30-N=2(5)'),
    ('n', 'the check is one line, and it always catches a wrong mass in the denominator'),
])

EX['JEE-12-atwood-ramp'] = ('A worked Atwood', [
    ('p', 'm₁ = 3 kg on a smooth 30° ramp, m₂ = 2 kg hanging. Find a and T.'),
    ('m', r'a=\frac{(2-3\sin30^\circ)9.8}{5}=\frac{0.5(9.8)}{5}=0.98\ \mathrm{m/s}^2'),
    ('m', r'T=m_2(g-a)=2(8.82)=17.6\ \mathrm{N}'),
    ('n', 'T is 17.6 N while the hanging weight is 19.6 N: they differ by m₂a'),
])

EX['JEE-13-movable-pulley'] = ('A worked movable pulley', [
    ('p', 'm₁ = 4 kg at the free end, m₂ = 3 kg on the movable pulley. Find both accelerations and T.'),
    ('m', r'a_1=\frac{2(8-3)9.8}{16+3}=\frac{98}{19}=5.16\ \mathrm{m/s}^2'),
    ('m', r'a_2=-2.58\ \mathrm{m/s}^2,\qquad T=m_1(g-a_1)=18.6\ \mathrm{N}'),
    ('n', 'the pulley rises at half the rate the free end falls, and 2T balances m₂ only at rest'),
])

EX['JEE-14-pseudo-force'] = ('A worked pendulum in a car', [
    ('p', 'A bob hangs from the roof of a car accelerating at 4.9 m/s². Find the hang angle and the tension per unit mass.'),
    ('m', r'\tan\theta=\frac{4.9}{9.8}=0.5\ \Rightarrow\ \theta=26.6^\circ'),
    ('m', r'T/m=\sqrt{g^2+a_0^2}=10.96\ \mathrm{N/kg}'),
    ('n', 'the same numbers fall out of the ground frame, where T sinθ = ma₀ does the work'),
])

EX['JEE-15-centripetal-source'] = ('A worked crest', [
    ('p', 'A car crosses a hill of radius 40 m at 15 m/s. What fraction of its weight does the road still support?'),
    ('m', r'N=m\left(g-\frac{v^2}{R}\right)=m(9.8-5.63)=4.17m'),
    ('m', r'\frac{N}{mg}=0.43,\qquad v_{\mathrm{lift}}=\sqrt{gR}=19.8\ \mathrm{m/s}'),
    ('n', 'at 19.8 m/s the normal force vanishes and the wheels leave the road'),
])

EX['JEE-16-banked-design'] = ('A worked bank', [
    ('p', 'A curve of radius 80 m is banked for 72 km/h with no friction. Find the angle and the normal force on a 1200 kg car.'),
    ('m', r'\tan\theta=\frac{v^2}{Rg}=\frac{400}{784}=0.51\ \Rightarrow\ \theta=27^\circ'),
    ('m', r'N=\frac{mg}{\cos\theta}=\frac{11760}{0.891}=13.2\ \mathrm{kN}'),
    ('n', 'N exceeds the weight by 12 %, because the bank must also turn the car'),
])

EX['JEE-17-banked-band'] = ('A worked band', [
    ('p', 'Same corner: R = 80 m, θ = 27°, μ = 0.35. Find the fastest and slowest safe speeds.'),
    ('m', r'v_{\max}^2=\frac{784(0.454+0.312)}{0.891-0.159}=820\ \Rightarrow\ 28.6\ \mathrm{m/s}'),
    ('m', r'v_{\min}^2=\frac{784(0.454-0.312)}{0.891+0.159}=106\ \Rightarrow\ 10.3\ \mathrm{m/s}'),
    ('n', 'the design speed sits between them at 20 m/s, as it must'),
])

EX['JEE-18-conical-pendulum'] = ('A worked whirl', [
    ('p', 'A 0.5 m string makes 40° with the vertical. Find the speed of the bob and the tension in a 0.2 kg bob.'),
    ('m', r'T=\frac{mg}{\cos40^\circ}=\frac{1.96}{0.766}=2.56\ \mathrm{N}'),
    ('m', r'v=\sqrt{gL\sin\theta\tan\theta}=\sqrt{9.8(0.5)(0.643)(0.839)}=1.63\ \mathrm{m/s}'),
    ('n', 'the period 2π√(L cosθ/g) = 1.24 s is independent of the mass'),
])

EX['JEE-19-vertical-circle-string'] = ('A worked loop', [
    ('p', 'A 0.4 kg ball on a 0.8 m string is whirled at exactly the limiting speed. Find the launch speed and the tension at the bottom.'),
    ('m', r'v_{\mathrm{bot}}=\sqrt{5gR}=\sqrt{5(9.8)(0.8)}=6.26\ \mathrm{m/s}'),
    ('m', r'T_{\mathrm{bot}}=6mg=6(3.92)=23.5\ \mathrm{N}'),
    ('n', 'the same ball at the top has T = 0 and v = 2.8 m/s, not zero'),
])

EX['JEE-20-vertical-circle-rod'] = ('A worked rod loop', [
    ('p', 'A 0.1 kg bead on a 0.6 m rod is given just enough speed to reach the top. Find the launch speed and N at the horizontal position.'),
    ('m', r'v_{\mathrm{bot}}=2\sqrt{gR}=2\sqrt{5.88}=4.85\ \mathrm{m/s}'),
    ('m', r'N(90^\circ)=2mg=1.96\ \mathrm{N}\ \text{inward}'),
    ('n', 'only half the string’s launch speed, because the rod does not need tension at the top'),
])

# ---------------------------------------------------------------- OLYMPIAD

EX['Olympiad-01-turntable-string'] = ('A worked turntable', [
    ('p', 'm = 0.5 kg at r = 0.4 m on a table spinning at 6 rad/s, string taut to the axis, μ_s = 0.3. Is there friction, and which way?'),
    ('m', r'\text{needed: }m\omega^2r=0.5(36)(0.4)=7.2\ \mathrm{N}'),
    ('m', r'\text{ceiling: }\mu_smg=1.47\ \mathrm{N}'),
    ('n', 'the string alone cannot supply 7.2 N, so friction must add 1.47 N inward — and it slips'),
])

EX['Olympiad-02-turntable-limit'] = ('A worked spin-up', [
    ('p', 'A coin sits at r = 12 cm on a turntable with μ_s = 0.4. At what angular speed does it slide, and does a 2 kg brick at the same radius differ?'),
    ('m', r'\omega_{\max}=\sqrt{\frac{0.4(9.8)}{0.12}}=5.72\ \mathrm{rad/s}'),
    ('m', r'm\ \text{cancels: the brick slides at the same }\omega'),
    ('n', 'the coin reaches the rim first only because it is placed further out, not because it is lighter'),
])

EX['Olympiad-03-wedge-constraint'] = ('A worked wedge', [
    ('p', 'M = 4 kg wedge at 30°, m = 1 kg block, all smooth. Find the wedge acceleration.'),
    ('m', r'a_w=-\frac{mg\sin\theta\cos\theta}{M+m\sin^2\theta}=-\frac{9.8(0.433)}{4.25}'),
    ('m', r'a_w=-1.00\ \mathrm{m/s}^2,\qquad a_{\mathrm{rel}}=\frac{5(9.8)(0.5)}{4.25}=5.76\ \mathrm{m/s}^2'),
    ('n', 'the wedge recoils at 1.0 m/s² while the block slides down the face at 5.8'),
])

EX['Olympiad-04-effective-gravity'] = ('A worked lift', [
    ('p', 'A 1 m pendulum rides a lift accelerating upward at 3 m/s². Find g_eff and the period; repeat for free fall.'),
    ('m', r'g_{\mathrm{eff}}=12.8\ \mathrm{m/s}^2,\qquad T=2\pi\sqrt{1/12.8}=1.76\ \mathrm{s}'),
    ('m', r'\text{free fall: }g_{\mathrm{eff}}=0,\qquad T\to\infty'),
    ('n', 'a pendulum in free fall does not swing at all: there is no preferred down'),
])

EX['Olympiad-05-wedge-liftoff'] = ('A worked liftoff', [
    ('p', 'A 45° wedge is pulled horizontally until the block leaves. Find the threshold and the normal force at a₀ = 0.5g.'),
    ('m', r'a_0=g\cot45^\circ=g=9.8\ \mathrm{m/s}^2'),
    ('m', r'N=mg(\cos45^\circ-0.5\sin45^\circ)=0.354mg'),
    ('n', 'at half the threshold the block still presses with about a third of its weight'),
])

EX['Olympiad-06-virtual-work'] = ('A worked constraint', [
    ('p', 'The block on a 30° wedge is held fixed while the wedge is pushed 2 cm. How far does the block rise, and what force does the wedge feel?'),
    ('m', r'\delta y_b=\delta x_w\tan\theta=2(0.577)=1.15\ \mathrm{cm}'),
    ('m', r'N=\frac{mg\cos\theta}{1+\frac{m}{M}\sin^2\theta}'),
    ('n', 'one constraint, one line, and no free-body diagram was drawn'),
])

EX['Olympiad-07-rope-over-edge'] = ('A worked rope', [
    ('p', 'A 2 m rope with μ_s = 0.3 hangs over a table edge. How much must hang before it moves, and what is the initial acceleration?'),
    ('m', r'\frac{x}{L}=\frac{0.3}{1.3}=0.231\ \Rightarrow\ x=46\ \mathrm{cm}'),
    ('m', r'a=g\left[x-\mu_k(1-x)\right]=9.8(0.231-0.231)=0'),
    ('n', 'at the threshold the acceleration is zero by construction, and then grows with x'),
])

EX['Olympiad-08-falling-chain'] = ('A worked falling chain', [
    ('p', 'A 2 kg chain of length 1 m lands in a heap. What does the scale read at the instant the last link lands?'),
    ('m', r'F=3\lambda Lg=3mg=3(19.6)=58.8\ \mathrm{N}'),
    ('m', r'\text{source answer: }2mg=39.2\ \mathrm{N}'),
    ('n', 'the weight term and the momentum term are both present; the source dropped one'),
])

EX['Olympiad-09-rocket-equation'] = ('A worked burn', [
    ('p', 'A rocket with v_e = 2.5 km/s must reach 7 km/s. What mass ratio is needed, and how much of it can be payload?'),
    ('m', r'\frac{m_0}{m_f}=e^{7/2.5}=e^{2.8}=16.4'),
    ('m', r'\text{payload fraction}\le\frac{1}{16.4}=6.1\ \%'),
    ('n', 'two stages at the same total fuel reach further, because the empty tank is dropped'),
])

EX['Olympiad-10-sand-conveyor'] = ('A worked conveyor', [
    ('p', 'Sand falls at 12 kg/s onto a belt moving at 1.5 m/s. Find the driving force, the motor power, and the heat generated.'),
    ('m', r'F=\dot mv=18\ \mathrm{N},\qquad P=Fv=27\ \mathrm{W}'),
    ('m', r'\dot K=\tfrac12\dot mv^2=13.5\ \mathrm{W},\qquad Q=13.5\ \mathrm{W}'),
    ('n', 'half the motor’s output leaves as heat, every second, forever'),
])

EX['Olympiad-11-chain-lift'] = ('A worked lift', [
    ('p', 'A 0.8 kg/m chain is lifted at 1.2 m/s. Find the force when 2.5 m hangs, and the rate of energy loss.'),
    ('m', r'F=\lambda gx+\lambda v^2=19.6+1.15=20.8\ \mathrm{N}'),
    ('m', r'P_{\mathrm{lost}}=\tfrac12\lambda v^3=0.69\ \mathrm{W}'),
    ('n', 'the extra force is only 6 % of the weight at this speed, but it never goes away'),
])

EX['Olympiad-12-capstan'] = ('A worked bollard', [
    ('p', 'A rope takes two turns round a bollard with μ = 0.25. What load can a 200 N pull hold?'),
    ('m', r'T_2=T_1e^{\mu\theta}=200e^{0.25(4\pi)}=200(23.1)'),
    ('m', r'T_2=4.6\ \mathrm{kN}'),
    ('n', 'a third turn takes it to 22 kN and a fourth to 107 kN: the growth is exponential'),
])

EX['Olympiad-13-friction-hitch'] = ('A worked hitch', [
    ('p', 'A wet rope has μ = 0.18 and must hold 8 kN with a 400 N hand. How many turns are needed?'),
    ('m', r'N=\frac{\ln(20)}{2\pi(0.18)}=\frac{3.00}{1.13}=2.65\ \text{turns}'),
    ('m', r'\text{dry, }\mu=0.3:\ N=1.59\ \text{turns}'),
    ('n', 'wetness costs a whole extra turn, which is why hitches are checked in the rain'),
])

EX['Olympiad-14-staging'] = ('A worked two-stage', [
    ('p', 'Same rocket, but the second stage is only 40 kg dry. How much does the extra 10 kg saved buy?'),
    ('m', r'\Delta v_2=2\ln\frac{540}{140}=2.70\ \mathrm{km/s}'),
    ('m', r'\Delta v=1.02+2.70=3.72\ \mathrm{km/s}\ (\text{was }3.62)'),
    ('n', '10 kg of structure is worth 0.10 km/s: the logarithm makes dry mass expensive'),
])

EX['Olympiad-15-impulse-window'] = ('A worked window', [
    ('p', 'A 0.06 kg tennis ball is in contact with the strings for 4 ms under a 300 N average force. How much does gravity change the answer?'),
    ('m', r'J_{\mathrm{hit}}=1.2\ \mathrm{N\,s},\qquad J_g=2.4\times10^{-3}\ \mathrm{N\,s}'),
    ('m', r'\frac{J_g}{J_{\mathrm{hit}}}=0.2\ \%'),
    ('n', 'a 4 ms contact is still short enough; a 0.2 s contact would not be'),
])

EX['Olympiad-16-bead-on-hoop'] = ('A worked hoop', [
    ('p', 'R = 0.5 m hoop spinning at 6 rad/s. Where does the bead settle, and what happens at 3 rad/s?'),
    ('m', r'\omega_c=\sqrt{g/R}=4.43\ \mathrm{rad/s}'),
    ('m', r'\cos\theta=\frac{9.8}{36(0.5)}=0.544\ \Rightarrow\ \theta=57^\circ'),
    ('n', 'at 3 rad/s, below ω_c, the only stable seat is the bottom'),
])

EX['JEE-21-energy-shortcut'] = ('A worked energy check', [
    ('p', 'A 0.5 kg ball on a 1 m string is launched at 8 m/s. Use energy to find the speed at the top and the tension there.'),
    ('m', r'v_{\mathrm{top}}^{2}=64-4(9.8)(1)=24.8\ \Rightarrow\ v=4.98\ \mathrm{m/s}'),
    ('m', r'T=\frac{0.5(24.8)}{1}-0.5(9.8)=7.5\ \mathrm{N}'),
    ('n', 'the tangential integral would give the same 24.8, in three more lines'),
])

EX['JEE-22-rough-table-pulley'] = ('A worked rough pulley', [
    ('p', 'm = 4 kg on a table with μ_k = 0.3, M = 3 kg hanging. Find a and T.'),
    ('m', r'a=\frac{(3-1.2)9.8}{7}=2.52\ \mathrm{m/s}^2'),
    ('m', r'T=M(g-a)=3(7.28)=21.8\ \mathrm{N}'),
    ('n', 'T is below Mg = 29.4 N, because the hanging mass is accelerating down'),
])

EX['JEE-23-accelerating-incline'] = ('A worked accelerating ramp', [
    ('p', 'A 2 kg block rests on a 35° smooth ramp. Find the ramp acceleration that keeps it there and the normal force then.'),
    ('m', r'a_0=g\tan35^\circ=9.8(0.700)=6.86\ \mathrm{m/s}^2'),
    ('m', r'N=\frac{mg}{\cos35^\circ}=\frac{19.6}{0.819}=23.9\ \mathrm{N}'),
    ('n', 'N is 22 % above the weight; the ramp is being pushed into the block'),
])

EX['JEE-24-measuring-mu'] = ('A worked measurement', [
    ('p', 'A box slides 18 m before stopping from 12 m/s. Find μ_k; then find the tilt angle that would just hold it at rest if μ_s is 15 % larger.'),
    ('m', r'\mu_k=\frac{144}{2(9.8)(18)}=0.41'),
    ('m', r'\mu_s=0.47\ \Rightarrow\ \theta_s=\tan^{-1}0.47=25^\circ'),
    ('n', 'two digits is all the data supports, and all μ is ever good for'),
])

EX['JEE-25-chain-over-edge'] = ('A worked chain', [
    ('p', 'A 1.5 m chain of mass 0.6 kg has 0.4 m hanging. Find the initial acceleration and the speed when it leaves the table.'),
    ('m', r'a=\frac{gx}{L}=\frac{9.8(0.4)}{1.5}=2.61\ \mathrm{m/s}^2'),
    ('m', r'v=\sqrt{\frac{9.8}{1.5}(2.25-0.16)}=3.70\ \mathrm{m/s}'),
    ('n', 'the final speed is close to √(gL) = 3.83 because only 0.4 m was left hanging'),
])

EX['JEE-26-wedge-carry'] = ('A worked carry', [
    ('p', 'A 2 kg block on a 40° wedge is to ride along. Find the required acceleration and the push on a 5 kg wedge.'),
    ('m', r'a_0=9.8\tan40^\circ=8.22\ \mathrm{m/s}^2'),
    ('m', r'F=(5+2)(8.22)=57.6\ \mathrm{N},\qquad N=\frac{19.6}{\cos40^\circ}=25.6\ \mathrm{N}'),
    ('n', 'the push scales with the total mass; the balance angle does not'),
])

EX['Olympiad-17-slack-angle'] = ('A worked slack', [
    ('p', 'A 0.2 kg ball on a 0.9 m string is launched at 4.5 m/s. At what angle does the string slacken, and what is the speed there?'),
    ('m', r'\cos\theta_0=\frac{20.25}{3(9.8)(0.9)}-\frac{2}{3}=0.765-0.667=0.098'),
    ('m', r'\theta_0=84.4^\circ,\qquad v=\sqrt{gR\cos\theta_0}=0.93\ \mathrm{m/s}'),
    ('n', 'the release is just above the horizontal, far below the top'),
])

EX['Olympiad-18-bounce-series'] = ('A worked bounce', [
    ('p', 'A ball dropped from 2 m rebounds to 1.28 m. Find e, the total distance and the total time to rest.'),
    ('m', r'e=\sqrt{1.28/2}=0.8,\qquad s=2\frac{1.64}{0.36}=9.1\ \mathrm{m}'),
    ('m', r't=\sqrt{0.408}\cdot\frac{1.8}{0.2}=0.639(9)=5.8\ \mathrm{s}'),
    ('n', 'the first fall alone takes 0.64 s; the infinite tail adds five more'),
])

EX['Olympiad-19-wedge-momentum'] = ('A worked momentum check', [
    ('p', 'm = 2 kg block, M = 3 kg wedge, θ = 40°, smooth. Find the wedge acceleration and check momentum in one line.'),
    ('m', r'a_w=-\frac{2(9.8)(0.643)(0.766)}{3+2(0.413)}=-\frac{9.65}{3.83}=-2.52\ \mathrm{m/s}^2'),
    ('m', r'a_{\mathrm{rel}}=\frac{5(9.8)(0.643)}{3.83}=8.22\ \mathrm{m/s}^2'),
    ('n', 'check: m(a_rel cosθ + a_w) = 2(6.30 − 2.52) = 7.56 = −M a_w, so the pair stays put'),
])

EX['Olympiad-20-stage-split'] = ('A worked split', [
    ('p', 'Same rocket: 1000 kg, 100 kg payload, two 50 kg dry stages, 800 kg of fuel, v_e = 2 km/s. Put 160 kg in stage one instead of 400.'),
    ('m', r'\Delta v_1=2\ln\frac{1000}{840}=0.35,\qquad \Delta v_2=2\ln\frac{790}{150}=3.32'),
    ('m', r'\text{total } 3.67\ \mathrm{km/s}\ \text{versus } 3.62\ \text{at the equal split}'),
    ('n', 'a small gain, and the single-stage rocket with the same structure gets 3.22'),
])

EX['Olympiad-21-model-limits'] = ('A worked ratio', [
    ('p', 'A proton at 0.1c, a dust grain of 10⁻¹⁵ kg moving at 1 mm/s, and a clock on a neutron star. Which need which theory?'),
    ('m', r'v/c=0.1\ (\gamma=1.005),\qquad S/\hbar\approx10^{19}'),
    ('m', r'\Phi/c^{2}\approx0.2\ \text{at the surface}'),
    ('n', 'a 0.5 % relativistic correction, no quantum correction, and general relativity non-negotiable'),
])

EX['Olympiad-22-rolling-contact'] = ('A worked wheel', [
    ('p', 'A 1200 kg car accelerates at 3 m/s² on μ_s = 0.7 tarmac. What friction does each driven wheel need, and is it available?'),
    ('m', r'f_{\mathrm{total}}=Ma=3600\ \mathrm{N}'),
    ('m', r'\text{available: }\mu_sMg=0.7(11760)=8232\ \mathrm{N}'),
    ('n', '44 % of the available grip, and all of it is static: no sliding anywhere'),
])

EX['Olympiad-23-four-shortcuts'] = ('A worked routing', [
    ('p', 'Two blocks on a wedge, a string between them over a pulley, the wedge accelerating. Which shortcut first?'),
    ('m', r'\text{constraint first (string)},\ \text{then system},\ \text{then frame}'),
    ('n', 'three moves, three unknowns; the FBD-only route needs six equations'),
])

EX['Olympiad-24-monkey-rope'] = ('A worked climb', [
    ('p', 'A 6 kg monkey and a 6 kg counterweight hang over a light pulley. The monkey climbs the rope at 0.5 m/s relative to it. Find both accelerations and the tension.'),
    ('m', r'a_1=a_2 \Rightarrow T-mg=ma \text{ on both sides}'),
    ('m', r'\text{grip without slipping: } a=0,\ T=58.8\ \mathrm{N}'),
    ('n', 'whatever the climb rate, both rise at the same speed: only the distance to the pulley changes'),
])
