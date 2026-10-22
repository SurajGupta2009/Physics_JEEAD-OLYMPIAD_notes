"""COM & collision panels: labelled schematics and compact diagnostic graphs."""
import numpy as np
from matplotlib.patches import Circle, Rectangle

I = '#153149'
T = '#087d7d'
R = '#a43232'


def txt(a, x, y, s, **kw):
    a.text(x, y, s, color=kw.pop('color', I), fontsize=kw.pop('fontsize', 8.5), **kw)


def arr(a, p, q, c=T):
    a.annotate('', xy=q, xytext=p, arrowprops=dict(arrowstyle='->', color=c, lw=1.6))


def line(a, p, q, **kw):
    a.plot([p[0], q[0]], [p[1], q[1]], color=kw.pop('color', I), lw=kw.pop('lw', 1.5), **kw)


def circ(a, x, y, r, ec=T, fill=False, fc='none', alpha=1.0):
    a.add_patch(Circle((x, y), r, fill=fill, fc=fc, ec=ec, lw=1.6, alpha=alpha))


def dot(a, x, y, c=R, r=.08):
    a.add_patch(Circle((x, y), r, color=c, zorder=5))


def plain(a):
    a.axis('off')
    a.set(xlim=(-3.1, 3.1), ylim=(-1.85, 1.85))
    a.set_aspect('equal')


def graph(a, x, y, xlab, ylab, label=None):
    a.axis('on')
    a.plot(x, y, color=T, lw=2, label=label)
    a.set_xlabel(xlab, fontsize=8.5)
    a.set_ylabel(ylab, fontsize=8.5)
    a.spines[['top', 'right']].set_visible(False)
    a.tick_params(labelsize=7.5)
    a.grid(alpha=.15)
    if label:
        a.legend(fontsize=7.5, loc='best', framealpha=.92)


def schematic(a, key):
    txt(a, -2.95, 1.56, SCHEM[key][0], fontsize=9, fontweight='bold')
    if key == 'bodies':
        line(a, (-2.75, -.25), (-1.25, -.25), lw=2.4)
        dot(a, -2.0, -.25)
        txt(a, -2.85, -.82, 'rod: COM at L/2')
        circ(a, -.1, .12, .52)
        dot(a, -.1, .12)
        txt(a, -.75, .92, 'ring: centre')
        circ(a, 1.85, .12, .62, fill=True, fc=T, alpha=.16)
        dot(a, 1.85, .12)
        txt(a, 1.25, .95, 'disc: centre')
        txt(a, -2.85, -1.52, 'symmetry axes pin every red COM dot')
    elif key == 'hole':
        circ(a, -.45, .05, 1.18, fill=True, fc=T, alpha=.12)
        circ(a, .45, .42, .44, ec=R, fill=True, fc='white', alpha=1.0)
        dot(a, -.45, .05, T, .07)
        dot(a, -.68, -.12, R, .08)
        arr(a, (-.45, .05), (-1.35, -.58), R)
        txt(a, .95, .75, 'cavity (-m)')
        txt(a, -2.85, -1.52, 'negative cavity shifts COM opposite cut')
    elif key in ('explosion', 'recoil'):
        dot(a, 0, .05)
        arr(a, (0, .05), (-1.85, .92), T)
        arr(a, (0, .05), (1.85, .92), T)
        arr(a, (0, .05), (0, -1.08), R)
        txt(a, -2.75, 1.02, 'm1 v1')
        txt(a, 1.88, 1.02, 'm2 v2')
        txt(a, .22, -1.05, 'm3 v3')
        txt(a, -2.85, -1.56, 'sum of fragment momenta equals M v_cm')
    elif key in ('impulse', 'impapprox'):
        circ(a, -1.65, .12, .38)
        line(a, (.75, -1.05), (.75, 1.15), lw=2.6)
        arr(a, (-1.18, .12), (.58, .12), R)
        txt(a, -2.75, .85, 'ball m, speed u')
        txt(a, 1.0, .65, 'wall')
        txt(a, -2.85, -1.48, 'impulse J = area under F(t) = delta p')
    elif key in ('classify', 'coll1d', 'collcases'):
        circ(a, -1.8, .22, .34)
        circ(a, -.92, .22, .34, R)
        arr(a, (-2.75, .22), (-2.18, .22))
        arr(a, (-.54, .22), (.22, .22), R)
        txt(a, .45, .38, 'line of impact')
        txt(a, -2.85, -.72, 'approach u1 - u2')
        txt(a, .35, -.72, 'separate v2 - v1')
        line(a, (-2.85, -1.18), (2.85, -1.18), ls=':', lw=1)
        txt(a, -2.85, -1.56, 'v2 - v1 = e (u1 - u2) along impact line')
    elif key in ('eloss', 'defo', 'traps'):
        for x, c in [(-2.15, T), (-.65, '#b7950b'), (.85, R)]:
            a.add_patch(Rectangle((x, -.68), .72, 1.38, fc=c, ec='none', alpha=.42))
        txt(a, -2.12, .88, 'K_cm')
        txt(a, -.72, .88, 'e^2 K_rel')
        txt(a, .95, .88, 'K_loss')
        arr(a, (-1.35, .02), (.78, .02))
        txt(a, -2.85, -1.48, 'K_loss = (1 - e^2) K_rel, with K_cm intact')
    elif key in ('oblique', 'ninety', 'scatter'):
        circ(a, -1.55, .38, .34)
        circ(a, .08, -.08, .34, R)
        arr(a, (-1.12, .28), (-.34, .05))
        line(a, (-2.35, -1.05), (2.45, 1.22), ls=':', lw=1.3)
        arr(a, (.42, .05), (1.52, .95))
        arr(a, (.42, -.22), (1.52, -1.02), R)
        txt(a, -2.85, -1.54, 'normal component changes; tangent stays intact')
    elif key == 'pendulum':
        line(a, (-1.45, 1.25), (-1.45, .28))
        a.add_patch(Rectangle((-1.72, -.02), .54, .44, fc=T, ec='none', alpha=.45))
        dot(a, -1.45, .20, R, .09)
        txt(a, -2.85, -.65, '1) hit: conserve p')
        arr(a, (.55, .25), (1.65, 1.02), R)
        txt(a, .25, -.65, '2) swing: conserve E')
        txt(a, -2.85, -1.52, 'never equate bullet KE directly to (m+M)gh')
    elif key == 'spring':
        a.add_patch(Rectangle((-2.4, -.35), .7, .7, fc=T, ec='none', alpha=.42))
        a.add_patch(Rectangle((1.4, -.35), .7, .7, fc=R, ec='none', alpha=.42))
        for k in range(8):
            line(a, (-1.7 + k * .39, -.2 if k % 2 else .2), (-1.31 + k * .39, .2 if k % 2 else -.2), lw=1.1)
        arr(a, (-1.0, .65), (1.1, .65))
        txt(a, -.95, .82, 'common v_cm at max x')
        txt(a, -2.85, -1.48, 'max deformation at shared velocity v_cm')
    elif key == 'cmframe':
        arr(a, (-2.1, -.35), (-.35, -.35))
        arr(a, (-.25, -.35), (.85, .68))
        arr(a, (-.25, -.35), (.85, -1.12), R)
        txt(a, -1.55, -.05, 'v_cm')
        txt(a, .95, .72, 'v1 = v_cm + v1*')
        txt(a, .95, -1.22, 'v2 = v_cm + v2*')
    elif key in ('belt', 'hopper'):
        line(a, (-2.55, -.35), (2.55, -.35), lw=2.5)
        arr(a, (-2.0, -.68), (1.9, -.68))
        txt(a, -.85, -.12, 'belt speed v')
        for x in [-1.7, -.7, .3, 1.3]:
            dot(a, x, .68, R, .065)
            arr(a, (x, .58), (x, -.22), R)
        txt(a, -2.85, 1.05, 'vertical feed: u_x = 0')
        txt(a, -2.85, -1.50, 'F_ext = m_dot v; half power goes to heat')
    elif key == 'rocket':
        a.add_patch(Rectangle((-.8, -.42), 1.4, .84, fc=T, ec='none', alpha=.42))
        arr(a, (-1.0, 0), (-2.55, 0), R)
        arr(a, (.8, 0), (2.45, 0))
        txt(a, -.72, .68, 'rocket m, v')
        txt(a, -2.85, .32, 'exhaust v_e')
        txt(a, 1.15, .32, 'thrust v_e dm/dt')
        txt(a, -2.85, -1.48, 'm dv/dt = F_ext + v_e (-dm/dt)')
    elif key == 'flux':
        line(a, (-2.1, 1.05), (-2.1, -1.05), lw=2.4)
        for y in [-.75, -.25, .25, .75]:
            circ(a, -1.25, y, .09, R)
        arr(a, (-.95, .55), (-2.0, .55))
        txt(a, -.75, .52, 'stream speed v')
        txt(a, -2.85, -1.50, 'control surface force = weight + m_dot delta v')
    elif key == 'boat':
        a.add_patch(Rectangle((-2.35, -.52), 1.5, .36, fc=T, ec='none', alpha=.42))
        a.add_patch(Rectangle((.55, -.52), 1.5, .36, fc=T, ec='none', alpha=.42))
        dot(a, -1.95, -.05)
        dot(a, 1.75, -.05)
        arr(a, (-.65, .42), (.45, .42))
        arr(a, (.45, -.02), (-.65, -.02), R)
        txt(a, -2.85, .95, 'F_ext,x = 0 => x_cm fixed')
        txt(a, -2.85, -1.48, 'boat recoil b = m d / (m + M)')
    elif key == 'bounces':
        line(a, (-2.8, -1.05), (2.8, -1.05), lw=1.8)
        for i, h in enumerate([1.55, .99, .63, .40]):
            line(a, (-2.15 + i * 1.25, -1.02), (-2.15 + i * 1.25, -1.02 + h), color=R, lw=2.4)
        txt(a, -.25, .92, 'h_n = e^(2n) h_0')
        txt(a, -2.85, -1.54, 'rebound heights form a geometric series')
    elif key in ('wall', 'platform'):
        line(a, (.35, -1.05), (.35, 1.05), lw=2.6)
        circ(a, -1.65, .22, .34)
        arr(a, (-1.15, .22), (.18, .22))
        arr(a, (.28, .78), (-.75, .78), R)
        txt(a, .55, .68, 'wall u_w')
        txt(a, -2.85, .95, 'shift to moving-wall frame')
        txt(a, -2.85, -1.50, 'v_after - u_w = -e (v_before - u_w)')
    elif key == 'chain3':
        line(a, (-2.5, -1.05), (2.4, -1.05), lw=2.2)
        a.add_patch(Rectangle((-1.15, -.98), 1.85, .22, fc=T, ec='none', alpha=.38))
        for i in range(5):
            dot(a, -1.45 + i * .12, .95 - i * .36, R, .065)
        arr(a, (-.45, -.25), (-.45, -.82), R)
        txt(a, .15, .58, 'v = sqrt(2 g x)')
        txt(a, -2.85, -1.52, 'scale force = landed weight + lambda v^2 = 3 lambda g x')
    elif key == 'fold':
        line(a, (-2.7, .65), (-.3, .65), lw=2.2)
        line(a, (-.3, .65), (-.3, .98), lw=2.2)
        a.plot([-.3, -.3, .45, .45], [.98, -.78, -.78, .98], color=R, lw=2)
        arr(a, (.85, .45), (.85, -.55))
        txt(a, 1.05, -.15, 'y')
        txt(a, -2.85, -1.48, 'smooth overhang or fold: track active mass')
    elif key == 'peg':
        circ(a, 0, .92, .26)
        line(a, (-.22, .80), (-1.55, -.62), lw=2)
        line(a, (.22, .80), (1.35, -.42), lw=2)
        for i in range(4):
            dot(a, -.48 - i * .24, .48 - i * .25, R, .06)
        for i in range(2):
            dot(a, .45 + i * .35, .52 - i * .25, R, .06)
        txt(a, -2.85, -1.48, 'sides x and L-x: peg contact vanishes at 0.854 L')
    elif key == 'staging':
        for x, c in [(-2.25, T), (-.72, '#b7950b'), (.82, R)]:
            a.add_patch(Rectangle((x, -.42), .92, .88, fc=c, ec='none', alpha=.42))
        arr(a, (-1.25, 0), (-.8, 0))
        arr(a, (.28, 0), (.74, 0))
        txt(a, -2.85, .82, 'stage 1 -> drop dead mass -> stage 2')
        txt(a, -2.85, -1.48, 'delta v adds v_e ln(R_i) across each stage')
    elif key == 'jet':
        line(a, (-2.7, .42), (-.65, .42), lw=3, color=T)
        a.add_patch(Rectangle((-.5, -.68), .2, 1.38, fc=R, ec='none', alpha=.5))
        arr(a, (-2.45, .42), (-.65, .42))
        arr(a, (.05, 0), (.95, 0), R)
        txt(a, 1.05, -.08, 'plate u')
        txt(a, -2.85, -1.48, 'F = rho A (v - u)^2, peak power at u = v/3')
    elif key == 'relativ':
        circ(a, -1.55, .15, .34)
        arr(a, (-2.75, .15), (-1.95, .15))
        txt(a, -2.75, .78, 'particle speed v')
        txt(a, -.55, .42, 'p = gamma m v')
        txt(a, -.55, -.28, 'gamma = 1 / sqrt(1 - v^2/c^2)')
        txt(a, -2.85, -1.48, 'conserve total (E/c, p); E^2 - p^2 c^2 invariant')
    elif key in ('route', 'ledger', 'integrate'):
        txt(a, -2.85, .92, '1) pick system + isolated axis')
        txt(a, -2.85, .34, '2) short pulse => impulse / momentum')
        txt(a, -2.85, -.24, '3) smooth stage => energy + constraints')
        txt(a, -2.85, -.82, '4) open flux => F_ext + u_rel dm/dt')
        txt(a, -2.85, -1.48, 'verify dimensions, e = 0 and e = 1 limits')


def graph_panel(a, key):
    x = np.linspace(0, 1, 200)
    if key in ('bodies', 'boat'):
        graph(a, x, x / (.25 + x), 'mass ratio m / M_0', 'COM shift fraction', 'm / (M_0 + m)')
    elif key == 'hole':
        r = np.linspace(.02, .88, 200)
        graph(a, r, -.5 * r * r / (1 - r * r), 'cavity radius ratio r / R', 'COM shift / d', 'negative-mass law')
    elif key in ('explosion', 'recoil'):
        m = np.linspace(.4, 5, 200)
        graph(a, m, 6 / m, 'fragment mass m (kg)', 'recoil speed |v| = p / m', 'equal momentum')
    elif key in ('impulse', 'impapprox'):
        t = np.linspace(0, 1, 200)
        f = np.where(t < .5, 80 * t, 80 * (1 - t))
        graph(a, t, f, 'contact time t / T', 'contact force F(t)', 'pulse area = J')
        a.fill_between(t, 0, f, color=T, alpha=.18)
    elif key in ('classify', 'coll1d', 'collcases'):
        e = np.linspace(0, 1, 200)
        graph(a, e, e, 'approach speed (norm.)', 'separation speed', 'e = 1 (elastic)')
        a.plot(e, .6 * e, color=R, ls='--', label='e = 0.6 (inelastic)')
        a.legend(fontsize=7.5)
    elif key in ('eloss', 'defo', 'traps'):
        e = np.linspace(0, 1, 200)
        graph(a, e, 1 - e ** 2, 'restitution e', 'K_loss / K_rel', '1 - e^2')
    elif key in ('oblique', 'ninety', 'scatter'):
        th = np.linspace(0, np.pi / 2, 200)
        graph(a, np.degrees(th), np.cos(th), 'deflection angle theta_1 (deg)', 'v_1 / u', 'equal-mass elastic')
    elif key == 'pendulum':
        v = np.linspace(0, 5, 200)
        graph(a, v, v * v / 20, 'post-impact speed V (m/s)', 'rise height h (m)', 'h = V^2 / (2g)')
    elif key == 'spring':
        m = np.linspace(.05, 5, 200)
        graph(a, m, np.sqrt(m / (m + 1)), 'projectile mass ratio m / M', 'x_max / x_fixed', 'sqrt(M / (m + M))' if False else 'sqrt(m / (m + M))')
    elif key == 'cmframe':
        th = np.linspace(0, 2 * np.pi, 200)
        graph(a, 1 + .5 * np.cos(th), .5 * np.sin(th), 'v_1x (lab)', 'v_1y (lab)', 'CM velocity circle')
        a.set_aspect('equal')
    elif key in ('belt', 'hopper'):
        t = np.linspace(0, 10, 200)
        graph(a, t, 5 / (1 + .1 * t), 'time t (s)', 'smooth cart speed v(t)', 'M_0 v_0 / (M_0 + mu t)')
    elif key == 'rocket':
        r = np.linspace(1, 20, 200)
        graph(a, r, np.log(r), 'mass ratio m_0 / m_f', 'delta v / v_e', 'ln(m_0 / m_f)')
    elif key == 'flux':
        z = np.linspace(0, 1, 200)
        graph(a, z, 3 * z, 'landed fraction x / L', 'scale reading F / mg', '3 x / L')
    elif key == 'bounces':
        n = np.arange(0, 8)
        graph(a, n, .8 ** n, 'bounce number n', 'ratio (e = 0.8)', 'speed ratio e^n')
        a.plot(n, .8 ** (2 * n), color=R, label='height ratio e^(2n)')
        a.legend(fontsize=7.5)
    elif key in ('wall', 'platform'):
        v = np.linspace(-5, 10, 200)
        graph(a, v, -5 - .8 * (v + 5), 'incident lab velocity u', 'rebound lab velocity v', 'u_w = -5, e = 0.8')
    elif key == 'chain3':
        z = np.linspace(0, 1, 200)
        graph(a, z, 3 * z, 'fallen fraction x / L', 'pan force F / mg', 'peaks at 3 mg')
    elif key == 'peg':
        z = np.linspace(.5, 1, 200)
        graph(a, z, 1 - 2 * (2 * z - 1) ** 2, 'long side x / L', 'peg normal N / mg', 'zero at x = 0.854 L')
        a.axhline(0, color=R, ls='--')
    elif key == 'staging':
        n = np.arange(1, 6)
        graph(a, n, np.log(1 + n * .65), 'stage count N', 'scaled delta v', 'staging gain')
    elif key == 'jet':
        u = np.linspace(0, 1, 200)
        graph(a, u, (1 - u) ** 2 * u, 'vane speed u / v', 'power P / (rho A v^3)', 'max 4/27 at u = v/3')
        a.axvline(1 / 3, color=R, ls='--')
    elif key == 'fold':
        y = np.linspace(0, 1, 200)
        graph(a, y, y * y, 'overhang fraction y / L', 'v^2 / (g L)', 'smooth table slide')
    elif key == 'relativ':
        v = np.linspace(0, .95, 200)
        graph(a, v, 1 / np.sqrt(1 - v * v), 'speed beta = v / c', 'Lorentz factor gamma', '1 / sqrt(1 - beta^2)')
    else:
        e = np.linspace(0, 1, 200)
        graph(a, e, (1 + e) / 2, 'restitution e', 'impulse / (2 mu u_rel)', '(1 + e) / 2')


SCHEM = {
    'bodies': ('Symmetric bodies & COM markers',),
    'hole': ('Composite plate with negative-mass cavity',),
    'explosion': ('Internal explosion: COM trajectory continues',),
    'impulse': ('Short-duration contact force & impulse area',),
    'recoil': ('Zero-momentum recoil of fragments',),
    'classify': ('Approach, contact & restitution phase',),
    'coll1d': ('Head-on 1D collision along line of centres',),
    'collcases': ('Special mass ratios in 1D impact',),
    'eloss': ('Konig split: CM energy vs lost relative KE',),
    'defo': ('Deformation impulse J_d & restitution e J_d',),
    'oblique': ('2D smooth impact: tangent vs normal axis',),
    'ninety': ('Equal-mass elastic impact: 90-degree exit',),
    'pendulum': ('Two-stage ballistic pendulum sequence',),
    'spring': ('Blocks coupled by a massless spring',),
    'cmframe': ('Zero-momentum CM frame vector addition',),
    'belt': ('Conveyor belt loading vertical sand stream',),
    'rocket': ('Rocket thrust from exhaust momentum flux',),
    'flux': ('Open control volume momentum-flux balance',),
    'boat': ('Man-boat recoil at fixed horizontal COM',),
    'bounces': ('Geometric rebound ladder on horizontal floor',),
    'wall': ('Ball rebounding off a translating heavy wall',),
    'chain3': ('Falling chain landing on a weighing pan',),
    'scatter': ('Lab deflection angle bound for heavy striker',),
    'peg': ('Flexible chain slipping over a smooth peg',),
    'staging': ('Multi-stage rocket discarding dead structure',),
    'jet': ('High-speed liquid jet striking a moving vane',),
    'fold': ('Chain overhang & folded-strand kinematics',),
    'relativ': ('Relativistic momentum & 4-momentum conservation',),
    'hopper': ('Translating cart under vertical mass addition',),
    'route': ('Master problem-routing decision sequence',),
    'ledger': ('Conservation ledger across impact stages',),
    'integrate': ('Synthesis workflow: impulse, energy & flux',),
    'impapprox': ('Impulse approximation during brief jerk',),
    'platform': ('Bounces on an accelerating or moving platform',),
    'traps': ('Energy partition & common exam traps',),
}

THEME_BASE = {k: k for k in SCHEM}

CAP = {
    ('bodies', 'a'): 'Symmetric bodies place the COM right on symmetry intersections',
    ('bodies', 'b'): 'Two-body COM position shifts smoothly toward the heavier mass',
    ('hole', 'a'): 'Treat any cutout as negative mass superposed on the whole body',
    ('hole', 'b'): 'Cavity COM displacement grows rapidly as hole radius approaches R',
    ('explosion', 'a'): 'Internal forces scatter fragments while the COM path stays parabolic',
    ('explosion', 'b'): 'Equal impulse gives lighter fragments proportionally higher speed',
    ('impulse', 'a'): 'Wall impact reverses normal momentum through contact force F(t)',
    ('impulse', 'b'): 'Linear impulse J equals the signed area under the F(t) pulse',
    ('impapprox', 'a'): 'String jerk or bat strike dominates finite gravity during delta t',
    ('impapprox', 'b'): 'Peak force scales inversely with contact duration at fixed J',
    ('recoil', 'a'): 'Zero initial momentum forces fragment momentum vectors to close',
    ('recoil', 'b'): 'Light recoil partner carries most of the kinetic energy p^2/(2m)',
    ('classify', 'a'): 'Restitution compares post-impact separation to pre-impact approach',
    ('classify', 'b'): 'Separation speed scales linearly with approach speed for fixed e',
    ('coll1d', 'a'): 'Measure all velocities with sign along one chosen impact axis',
    ('coll1d', 'b'): 'Elastic limit preserves relative speed while e < 1 damps rebound',
    ('collcases', 'a'): 'Equal elastic masses swap velocities along the line of impact',
    ('collcases', 'b'): 'Restitution e interpolates between sticking (0) and bounce (1)',
    ('eloss', 'a'): 'Centre-of-mass kinetic energy K_cm survives every internal impact',
    ('eloss', 'b'): 'Fractional loss of relative kinetic energy equals 1 - e^2',
    ('defo', 'a'): 'Peak compression occurs precisely when both bodies share speed v_cm',
    ('defo', 'b'): 'Restitution returns fraction e^2 of maximum deformation energy',
    ('traps', 'a'): 'Separate conserved K_cm from dissipatable relative energy K_rel',
    ('traps', 'b'): 'Perfectly inelastic impact loses 100% of K_rel, never K_cm',
    ('oblique', 'a'): 'Project velocities onto contact normal n and smooth tangent t',
    ('oblique', 'b'): 'Post-impact speed ratio cos(theta_1) for equal-mass elastic hit',
    ('ninety', 'a'): 'Stationary equal-mass elastic target exits at 90 deg to striker',
    ('ninety', 'b'): 'Striker speed drops as u cos(theta_1) with deflection angle',
    ('scatter', 'a'): 'Heavy striker m_1 > m_2 cannot deflect beyond arcsin(m_2 / m_1)',
    ('scatter', 'b'): 'CM velocity circle bounds the maximum laboratory scattering angle',
    ('pendulum', 'a'): 'Split ballistic pendulum cleanly into impact then smooth swing',
    ('pendulum', 'b'): 'Post-collision rise height scales quadratically with shared speed V',
    ('spring', 'a'): 'Spring compression peaks when relative velocity passes through zero',
    ('spring', 'b'): 'Free recoil reduces peak spring compression by factor sqrt(m/(m+M))',
    ('cmframe', 'a'): 'In the CM frame momenta cancel and impact simply scales and rotates',
    ('cmframe', 'b'): 'Lab final velocity tips lie on a circle centred at v_cm',
    ('belt', 'a'): 'Driving a sand belt at constant speed requires force m_dot v',
    ('belt', 'b'): 'Smooth cart catching vertical rain slows as M_0 v_0 / (M_0 + mu t)',
    ('hopper', 'a'): 'Vertical leak leaves smooth cart speed unchanged; vertical load slows it',
    ('hopper', 'b'): 'Velocity decay of frictionless cart accumulating vertical mass',
    ('rocket', 'a'): 'Exhaust speed v_e relative to rocket sets thrust v_e (-dm/dt)',
    ('rocket', 'b'): 'Tsiolkovsky logarithmic velocity gain across mass ratio m_0 / m_f',
    ('flux', 'a'): 'Momentum flux across control surface adds rate m_dot delta v',
    ('flux', 'b'): 'Scale force combines static landed weight with impact momentum flux',
    ('boat', 'a'): 'With zero horizontal drag, walking distance d shifts boat by m d/(m+M)',
    ('boat', 'b'): 'COM fraction tracks mass ratio between walker and boat',
    ('bounces', 'a'): 'Each floor bounce multiplies speed by e and apex height by e^2',
    ('bounces', 'b'): 'Speed decays as e^n while rebound height decays twice as fast e^(2n)',
    ('wall', 'a'): 'Apply restitution strictly to velocities measured relative to wall',
    ('wall', 'b'): 'Approaching heavy wall boosts ball lab speed by (1 + e)|u_w| + e u',
    ('platform', 'a'): 'Accelerating floor shifts effective gravity to g_eff = g + a_p',
    ('platform', 'b'): 'Moving boundary velocity jump from relative restitution rule',
    ('chain3', 'a'): 'Falling chain links hit pan at sqrt(2gx), adding 2 lambda g x flux',
    ('chain3', 'b'): 'Scale reading climbs linearly to 3 mg right as the top link lands',
    ('fold', 'a'): 'Folded chain release loses mechanical energy at inelastic bend',
    ('fold', 'b'): 'Smooth overhang speed squared grows as y^2 / L from gravity work',
    ('peg', 'a'): 'Longer side accelerates chain faster until normal force hits zero',
    ('peg', 'b'): 'Peg contact vanishes at x / L = (1 + 1/sqrt(2))/2 = 0.854',
    ('staging', 'a'): 'Jettisoning empty tanks avoids accelerating dead structural mass',
    ('staging', 'b'): 'Cumulative delta v rises by resetting mass ratio at each stage',
    ('jet', 'a'): 'Moving vane intercepts mass rate rho A (v - u), not rho A v',
    ('jet', 'b'): 'Mechanical power extracted by flat vane peaks at u = v / 3',
    ('relativ', 'a'): 'Relativistic momentum carries factor gamma = 1/sqrt(1 - v^2/c^2)',
    ('relativ', 'b'): 'Lorentz factor diverges rapidly as particle speed approaches c',
    ('route', 'a'): 'Classify every question by impulse window, constraints and flux',
    ('route', 'b'): 'Normal impulse scales linearly with 1 + e across collision regimes',
    ('ledger', 'a'): 'Audit momentum, angular momentum about hinge, and energy stagewise',
    ('ledger', 'b'): 'Impulse fraction (1 + e)/2 bridges inelastic and elastic limits',
    ('integrate', 'a'): 'Combine stagewise conservation laws without mixing time windows',
    ('integrate', 'b'): 'Restitution factor controls both impulse and energy recovery',
}


def figure(a, key):
    theme, side = key.rsplit('-', 1)
    base = THEME_BASE.get(theme, 'bodies')
    if side == 'a':
        plain(a)
        schematic(a, base)
    else:
        graph_panel(a, base)
    return CAP.get((theme, side), 'COM & collision analysis panel')
