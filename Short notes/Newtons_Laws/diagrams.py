"""Native analytical diagrams for the Newton's-laws short notes.

Rule of the sheet: one wide figure per page, at most two panels, at most six
labels per panel, every label placed in whitespace rather than on the drawing.
Everything here is a closed-form curve or a labelled free-body diagram: force
triangles, friction ramps, constraint geometries, T(theta) curves. No
decorative imagery.
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, Ellipse, Arc, Polygon, Wedge, FancyArrowPatch
from matplotlib.ticker import NullFormatter

I = '#153149'
T = '#087d7d'
R = '#a43232'
PALE = '#eff8f5'
YEL = '#fff2b8'
G = '#516875'
GOLD = '#8a6a10'
WATER = '#e8f3f8'
HG = '#c9d2d7'


def txt(ax, x, y, s, color=I, **kw):
    kw.setdefault('fontsize', 8.6)
    ax.text(x, y, s, color=color, **kw)


def _fit(ax, s, fs, x, y, color, va):
    fig = ax.figure
    for f in (fs, fs - .6, fs - 1.2, fs - 1.8, fs - 2.4):
        t = ax.text(x, y, s, transform=ax.transAxes, fontsize=f, color=color,
                    ha='center', va=va)
        bb = t.get_window_extent(fig.canvas.get_renderer())
        ab = ax.get_window_extent()
        if bb.x0 >= ab.x0 + 1 and bb.x1 <= ab.x1 - 1:
            return
        t.remove()
    t = ax.text(x, y, s, transform=ax.transAxes, fontsize=fs - 2.4, color=color,
                ha='center', va=va)


def head(ax, s, color=T):
    """Panel title above the frame when the panel carries axes."""
    if ax.axison:
        ax.annotate(s, xy=(.5, 1), xycoords='axes fraction', xytext=(0, 7),
                    textcoords='offset points', ha='center', va='bottom',
                    fontsize=9.0, color=color)
    else:
        _fit(ax, s, 9.0, .5, .99, color, 'top')


def foot(ax, s, color=G):
    _fit(ax, s, 7.4, .5, .01, color, 'bottom')


def arrow(ax, a, b, c=T, lw=1.5, style='->', ms=8):
    ax.annotate('', xy=b, xytext=a,
                arrowprops=dict(arrowstyle=style, color=c, lw=lw, shrinkA=0,
                                shrinkB=0, mutation_scale=ms))


def panel(fig, rect, xlim=(0, 10), ylim=(0, 4.6), equal=False):
    a = fig.add_axes(rect)
    a.axis('off')
    a.set_xlim(*xlim)
    a.set_ylim(*ylim)
    if equal:
        a.set_aspect('equal', adjustable='box')
    return a


def axes2(a, xlabel, ylabel):
    """Axis furniture placed in points, not axes fractions."""
    a.axis('on')
    a.spines[['top', 'right']].set_visible(False)
    a.tick_params(labelsize=7.0, length=3, pad=2)
    a.grid(alpha=.12, lw=.7)
    a.annotate(xlabel, xy=(.5, 0), xycoords='axes fraction', xytext=(0, -19),
               textcoords='offset points', ha='center', va='top',
               fontsize=7.8, color=I)
    a.annotate(ylabel, xy=(0, .5), xycoords='axes fraction', xytext=(-30, 0),
               textcoords='offset points', ha='center', va='center',
               rotation=90, fontsize=7.8, color=I)


def dimx(ax, x0, x1, y, label, color=I, fs=8.2):
    arrow(ax, (x0, y), (x1, y), color, 1.0, '<->', 6)
    ax.text((x0 + x1) / 2, y + .10, label, ha='center', fontsize=fs, color=color)


def dimy(ax, x, y0, y1, label, side='right', color=I, fs=8.2):
    arrow(ax, (x, y0), (x, y1), color, 1.0, '<->', 6)
    ax.text(x + (.14 if side == 'right' else -.14), (y0 + y1) / 2, label,
            ha='left' if side == 'right' else 'right', va='center', fontsize=fs, color=color)


def incline(ax, x0, x1, y0, theta, lw=2.2, fill='#f2f6f5'):
    """Right-triangle ramp with its base at y0, apex at x1."""
    h = (x1 - x0) * np.tan(np.radians(theta))
    ax.add_patch(Polygon([(x0, y0), (x1, y0), (x1, y0 + h)], closed=True,
                         fc=fill, ec=I, lw=lw, zorder=1))
    return h


def block(ax, cx, cy, w, h, fc='#fdf0bd', ec=GOLD, lw=1.4, z=3):
    ax.add_patch(Rectangle((cx - w / 2, cy - h / 2), w, h, fc=fc, ec=ec,
                           lw=lw, zorder=z))


def force(ax, p, q, color=R, lw=1.6, label=None, fs=8.0, off=(.16, .05), ha='left'):
    arrow(ax, p, q, color, lw)
    if label:
        ax.text(q[0] + off[0], q[1] + off[1], label, fontsize=fs, color=color, ha=ha)


def dashed(ax, p, q, color=HG, lw=1.0):
    ax.plot([p[0], q[0]], [p[1], q[1]], color=color, lw=lw, ls=(0, (4, 3)), zorder=1)


# ===================================================================== JEE
def _frame_choice(fig):
    """Same ball, two frames: one keeps the first law, one invents a force."""
    a = panel(fig, [.04, .46, .44, .46], xlim=(0, 10), ylim=(0, 4.6))
    a.add_patch(Rectangle((.6, 1.55), 8.2, .30, fc='#f2f6f5', ec=I, lw=1.4))
    a.add_patch(Circle((5.0, 2.25), .34, fc='#fdf0bd', ec=GOLD, lw=1.3))
    a.text(5.0, 3.35, 'no force, no acceleration', fontsize=8.0, color=T, ha='center')
    a.text(5.0, .85, 'a room that is not accelerating', fontsize=7.8, color=G, ha='center')
    head(a, 'inertial frame')

    b = panel(fig, [.54, .46, .44, .46], xlim=(0, 10), ylim=(0, 4.6))
    b.add_patch(Rectangle((.6, 1.55), 8.2, .30, fc='#f2f6f5', ec=I, lw=1.4))
    b.add_patch(Circle((3.6, 2.25), .34, fc='#fdf0bd', ec=GOLD, lw=1.3))
    arrow(b, (3.6, 2.25), (5.9, 2.25), R, 1.5)
    b.text(6.05, 2.05, 'drifts forward', fontsize=7.8, color=R)
    arrow(b, (9.3, 3.05), (7.7, 3.05), T, 1.4)
    b.text(7.5, 2.72, 'car brakes', fontsize=7.6, color=T, ha='right')
    b.text(5.0, .85, 'the car frame', fontsize=7.8, color=G, ha='center')
    head(b, 'non-inertial frame')

    c = panel(fig, [.10, .17, .52, .24])
    axes2(c, 'time  (s)', 'ball velocity  (m/s)')
    t = np.linspace(0, 4, 200)
    c.plot(t, np.full_like(t, 2.0), color=T, lw=2.2)
    c.plot(t, 2.0 + 0.55 * t ** 2, color=R, lw=2.2)
    c.text(.25, 2.45, 'ground frame', fontsize=7.6, color=T)
    c.text(1.35, 8.4, 'car frame', fontsize=7.6, color=R)
    c.set_xlim(0, 4); c.set_ylim(0, 11)
    c.set_yticks([0, 2, 4, 6, 8, 10])
    head(c, 'the velocity the ball appears to have')

    d = panel(fig, [.70, .13, .28, .28])
    d.axis('off')
    for k, line in enumerate(('the first law is not',
                              'a force statement;',
                              'it is the definition',
                              'of the frame you',
                              'are allowed to use')):
        d.text(.2, 4.10 - k * .62, line, fontsize=8.2, color=I)
    d.text(.2, 4.10 - 5 * .62 - .25, 'pick the frame first', fontsize=8.2, color=T)
    return 'Pick the frame first: in an inertial frame a force-free body keeps its velocity'


def _second_law_impulse(fig):
    a = panel(fig, [.09, .18, .40, .68])
    axes2(a, 'time  (ms)', 'force  (N)')
    t = np.linspace(0, 6, 400)
    F = 900 * np.exp(-((t - 3) / .55) ** 2)
    a.fill_between(t, 0, F, color='#fdf0bd', zorder=1)
    a.plot(t, F, color=R, lw=2.0)
    a.text(.22, 920, 'area = impulse', fontsize=8.2, color=GOLD)
    a.text(.22, 790, r'$J=\int F\,dt=\Delta p$', fontsize=8.6, color=GOLD)
    a.set_ylim(0, 1000); a.set_xlim(0, 6)
    head(a, 'a real hit is a pulse, not a number')

    b = panel(fig, [.58, .18, .36, .68])
    axes2(b, 'time  (ms)', 'momentum  (kg m/s)')
    p = np.cumsum(F) * (t[1] - t[0]) * 1e-3
    b.plot(t, p, color=T, lw=2.2)
    b.plot([3], [np.interp(3, t, p)], 'o', ms=5, color=R, zorder=5)
    b.annotate('slope = F', xy=(2.55, .18), xytext=(.30, .70), fontsize=8.2, color=T,
               arrowprops=dict(arrowstyle='->', color=T, lw=.8))
    b.text(4.05, .42, r'$\Delta p=J$', fontsize=8.4, color=R)
    b.set_xlim(0, 6); b.set_ylim(0, 1.12)
    head(b, 'the curve of momentum is what F shapes')
    return 'F = dp/dt is the general law; F = ma is the fixed-mass shortcut, and the impulse is the area'


def _third_law_pairs(fig):
    a = panel(fig, [.02, .06, .50, .88], xlim=(0, 5.6), ylim=(0, 4.6), equal=True)
    a.add_patch(Rectangle((.35, 1.45), 4.80, .24, fc='#f2f6f5', ec=I, lw=1.4))
    block(a, 1.95, 2.05, 1.45, .94)
    a.plot([2.68, 3.55], [2.05, 2.05], color=HG, lw=1.0, ls=(0, (3, 2)))
    a.add_patch(Circle((3.62, 2.05), .09, fc=I, ec=I))
    arrow(a, (3.62, 2.05), (3.62, 3.30), T, 1.9)
    a.text(3.74, 3.24, 'N', fontsize=8.8, color=T)
    arrow(a, (3.62, 2.05), (3.62, .80), R, 1.9)
    a.text(3.74, .80, 'W', fontsize=8.8, color=R)
    arrow(a, (.95, 1.33), (.95, .50), T, 1.5)
    a.text(.78, .52, 'N', fontsize=8.0, color=T, ha='right')
    a.text(.40, .16, 'on the table', fontsize=7.0, color=G)
    a.text(.40, 4.16, 'forces on the block', fontsize=7.8, color=I)
    a.text(.40, 3.82, 'N up, W down: not a pair', fontsize=7.8, color=R)

    c = panel(fig, [.55, .06, .43, .88], xlim=(0, 5.6), ylim=(0, 4.6), equal=True)
    c.add_patch(Rectangle((.55, 2.95), 1.15, .62, fc='#fdf0bd', ec=GOLD, lw=1.4))
    c.add_patch(Ellipse((2.55, 1.05), 4.6, .85, fc='#e7f4f1', ec=T, lw=1.3))
    c.text(2.55, .82, 'Earth', fontsize=8.0, color=T, ha='center')
    arrow(c, (2.05, 2.95), (2.05, 2.05), R, 1.7)
    c.text(3.95, 2.55, 'on the block', fontsize=7.4, color=R, ha='center')
    arrow(c, (1.35, 1.40), (1.35, 2.32), GOLD, 1.7)
    c.text(3.95, 1.55, 'on the Earth', fontsize=7.4, color=GOLD, ha='center')
    c.text(2.55, 4.18, 'the same size, opposite', fontsize=7.2, color=G, ha='center')
    c.text(.55, 4.16, 'the third-law pair', fontsize=7.8, color=I)
    c.text(.55, 3.82, 'of the block\u2019s weight', fontsize=7.8, color=I)
    c.text(.55, .22, 'equal, opposite, different bodies', fontsize=7.2, color=G)
    return 'Equal and opposite, but never on the same body: the normal force is a contact pair, not a weight pair'


def _fbd_incline(fig):
    a = panel(fig, [.02, .06, .56, .88], xlim=(0, 7.4), ylim=(0, 4.6), equal=True)
    th = 30.0
    x0, x1, y0 = .45, 6.55, .55
    h = (x1 - x0) * np.tan(np.radians(th))
    a.add_patch(Polygon([(x0, y0), (x1, y0), (x1, y0 + h)], closed=True,
                        fc='#f2f6f5', ec=I, lw=2.0, zorder=1))
    a.plot([x0, x1 + .55], [y0, y0], color=I, lw=1.6)

    # the block sits on the hypotenuse, tilted with it
    s_ = 3.30
    bx = x0 + s_ * np.cos(np.radians(th))
    by = y0 + s_ * np.sin(np.radians(th))
    bw, bh = .95, .52
    ux, uy = np.cos(np.radians(th)), np.sin(np.radians(th))
    nx, ny = -uy, ux
    corners = []
    for du, dn in ((-bw / 2, 0), (bw / 2, 0), (bw / 2, bh), (-bw / 2, bh)):
        corners.append((bx + du * ux + dn * nx, by + du * uy + dn * ny))
    a.add_patch(Polygon(corners, closed=True, fc='#fdf0bd', ec=GOLD, lw=1.6, zorder=4))
    c = (bx - .05, by + bh * .5)

    # weight, normal, friction from the block centre
    force(a, c, (c[0], c[1] - 1.72), R, 1.9, 'mg', off=(.12, -.34))
    force(a, c, (c[0] + 1.45 * nx, c[1] + 1.45 * ny), T, 1.9, 'N', off=(.10, .10))
    force(a, (bx - .45 * ux + .16 * nx, by - .45 * uy + .16 * ny),
          (bx - 1.55 * ux + .16 * nx, by - 1.55 * uy + .16 * ny), G, 1.8,
          'f', off=(-.24, -.10))

    # component guides
    dashed(a, (c[0], c[1] - 1.72), (c[0] - 1.6 * ux, c[1] - 1.72 + 1.6 * uy))
    a.add_patch(Arc(c, 1.5, 1.5, theta1=270 - th, theta2=270, color=R, lw=.9))
    a.text(c[0] + .30, c[1] - 1.02, r'$\theta$', fontsize=7.6, color=R)

    a.add_patch(Arc((x0 + .30, y0), 1.5, 1.5, theta1=0, theta2=th, color=I, lw=1.1))
    a.text(x0 + 1.05, y0 + .22, r'$\theta$', fontsize=8.6, color=I)
    a.text(x0 + .05, 4.30, 'isolate, then rotate the axes', fontsize=7.6, color=G)

    d = panel(fig, [.63, .10, .34, .80], xlim=(0, 10), ylim=(0, 4.6))
    d.axis('off')
    d.text(.2, 3.10, r'$mg\sin\theta-f=ma$', fontsize=9.2, color=T)
    d.text(.2, 2.30, r'$N=mg\cos\theta$', fontsize=9.2, color=T)
    d.text(.2, 1.35, 'axes along the acceleration', fontsize=8.0, color=I)
    d.text(.2, .85, 'decouple the two equations', fontsize=8.0, color=I)
    d.text(.2, .15, r'$N\ne mg$ unless $\theta=0$', fontsize=8.4, color=R)
    return 'Isolate the body, draw only external forces, put the axes along the acceleration'


def _apparent_weight(fig):
    a = panel(fig, [.09, .16, .55, .70])
    axes2(a, r'lift acceleration  $a/g$', r'scale reading  $N/mg$')
    x = np.linspace(-1.15, 1.6, 300)
    a.plot(x, 1 + x, color=T, lw=2.2)
    a.axhline(1, color=HG, lw=.9, ls=(0, (3, 3)))
    a.axhline(0, color=HG, lw=.9)
    a.plot([0], [1], 'o', ms=5, color=G, zorder=5)
    a.plot([1], [2], 'o', ms=5, color=R, zorder=5)
    a.plot([-1], [0], 'o', ms=5.5, color=R, zorder=5)
    a.annotate('at rest', xy=(0, 1), xytext=(-.90, 1.42), fontsize=7.6, color=G,
               arrowprops=dict(arrowstyle='->', color=G, lw=.8))
    a.annotate(r'up at $g/2$:  $3mg/2$', xy=(.5, 1.5), xytext=(-.40, 2.35),
               fontsize=7.6, color=R, arrowprops=dict(arrowstyle='->', color=R, lw=.8))
    a.annotate('free fall: zero', xy=(-1, 0), xytext=(-1.10, .62), fontsize=7.6, color=R,
               arrowprops=dict(arrowstyle='->', color=R, lw=.8))
    a.set_xlim(-1.2, 1.6); a.set_ylim(-.25, 2.75)
    head(a, 'the scale reads the normal force')

    b = panel(fig, [.70, .12, .28, .78], xlim=(0, 10), ylim=(0, 4.6))
    b.axis('off')
    for k, (lab, val, c) in enumerate((('at rest', r'$N=mg$', G),
                                       ('accelerating up', r'$N=m(g+a)$', T),
                                       ('accelerating down', r'$N=m(g-a)$', T),
                                       ('free fall', r'$N=0$', R))):
        y = 4.05 - k * 1.02
        b.text(.2, y + .26, lab, fontsize=7.6, color=c)
        b.text(.2, y - .22, val, fontsize=8.8, color=c)
    b.text(.2, .32, 'the weight never changes', fontsize=7.0, color=G)
    return 'Weight never changes; the reading is the normal force, and free fall makes it zero'


def _lami_triangle(fig):
    a = panel(fig, [.03, .08, .44, .84], xlim=(0, 6.0), ylim=(0, 5.0), equal=True)
    o = (3.0, 2.15)
    dirs = [90, 205, 330]
    ends = [(o[0] + 1.85 * np.cos(np.radians(t)), o[1] + 1.85 * np.sin(np.radians(t)))
            for t in dirs]
    for t, e, c in zip(dirs, ends, (R, T, GOLD)):
        arrow(a, o, e, c, 1.9)
    a.text(ends[0][0] + .22, ends[0][1] + .06, r'$F_1$', fontsize=9.2, color=R)
    a.text(ends[1][0] - .05, ends[1][1] - .30, r'$F_2$', fontsize=9.2, color=T, ha='right')
    a.text(ends[2][0] + .14, ends[2][1] - .30, r'$F_3$', fontsize=9.2, color=GOLD)
    a.add_patch(Arc(o, 1.15, 1.15, theta1=90, theta2=205, color=I, lw=1.1))
    a.text(o[0] - .88, o[1] + .92, r'$\alpha_1$', fontsize=8.2, color=I)
    a.add_patch(Circle(o, .07, fc=I, ec=I))
    head(a, 'three forces on one point')

    b = panel(fig, [.50, .08, .40, .84], xlim=(0, 6.0), ylim=(0, 5.0), equal=True)
    P1 = (3.05, 3.90); P2 = (4.85, 1.10); P3 = (1.25, 1.10)
    b.add_patch(Polygon([P1, P2, P3], closed=True, fc='#eef5f3', ec=T, lw=1.8))
    for P, lab, off in ((P1, r'$F_1$', (0, .30)), (P2, r'$F_2$', (.24, -.20)),
                        (P3, r'$F_3$', (-.28, -.20))):
        b.text(P[0] + off[0], P[1] + off[1], lab, fontsize=9.0, color=I)
    b.text(3.05, .30, 'head to tail, it closes', fontsize=7.4, color=G, ha='center')
    b.text(.05, 4.72, r'$F_1/\sin\alpha_1=F_2/\sin\alpha_2=F_3/\sin\alpha_3$',
           fontsize=8.6, color=T)
    return 'Three forces, one point, zero sum: the vector triangle obeys the sine rule'


def _friction_ramp(fig):
    a = panel(fig, [.08, .16, .58, .70])
    axes2(a, 'applied force  F  (N)', 'friction  f  (N)')
    us, uk = .60, .43
    Fc = 6.0
    a.plot([0, Fc], [0, us * 10], color=T, lw=2.2)
    a.plot([Fc, Fc], [us * 10, uk * 10], color=T, lw=2.2)
    a.plot([Fc, 10], [uk * 10, uk * 10], color=T, lw=2.2)
    a.plot([0, 10], [us * 10, us * 10], color=HG, lw=.9, ls=(0, (4, 3)))
    a.plot([0, 10], [uk * 10, uk * 10], color=HG, lw=.9, ls=(0, (4, 3)))
    a.plot([Fc], [us * 10], 'o', ms=5.5, color=R, zorder=5)
    a.text(.15, us * 10 + .22, r'$\mu_s N$', fontsize=8.4, color=R)
    a.text(.15, uk * 10 + .22, r'$\mu_k N$', fontsize=8.4, color=R)
    a.text(2.55, 1.35, r'$f=F$', fontsize=8.4, color=T)
    a.text(2.55, .72, 'static: it adapts', fontsize=7.2, color=G)
    a.text(6.9, uk * 10 + .55, 'kinetic: a fixed value', fontsize=7.6, color=T)
    a.text(6.9, 2.6, 'slip', fontsize=8.4, color=R)
    a.annotate('about to slip', xy=(Fc, us * 10), xytext=(1.6, 7.0), fontsize=7.4,
               color=R, arrowprops=dict(arrowstyle='->', color=R, lw=.8))
    a.set_xlim(0, 10); a.set_ylim(0, 7.6)
    head(a, 'friction is a range, then a plateau')

    b = panel(fig, [.70, .12, .28, .78], xlim=(0, 10), ylim=(0, 4.6))
    b.axis('off')
    rows = (('static', 'f adjusts to hold', r'$f\leq\mu_sN$', T),
            ('at the limit', 'about to slip', r'$f=\mu_sN$', R),
            ('sliding', 'fixed by the surfaces', r'$f=\mu_kN$', G))
    for k, (t1, t2, f, c) in enumerate(rows):
        y = 4.15 - k * 1.42
        b.text(.2, y, t1, fontsize=8.2, color=c)
        b.text(.2, y - .40, t2, fontsize=7.0, color=I)
        b.text(.2, y - .84, f, fontsize=8.4, color=c)
    return 'Static friction is an inequality with a ceiling; kinetic friction is a value'


def _friction_direction(fig):
    a = panel(fig, [.02, .08, .30, .86], xlim=(0, 4.2), ylim=(0, 4.6), equal=True)
    a.add_patch(Rectangle((.25, .85), 3.70, .22, fc='#f2f6f5', ec=I, lw=1.2))
    block(a, 1.55, 1.45, .95, .60)
    arrow(a, (2.12, 1.72), (3.25, 1.72), T, 1.7)
    a.text(3.35, 1.58, 'F', fontsize=8.6, color=T)
    arrow(a, (1.12, 1.30), (.35, 1.30), R, 1.6)
    a.text(.30, 1.52, 'f', fontsize=8.4, color=R)
    a.text(.25, 3.62, 'pushed on the floor', fontsize=8.0, color=T)
    a.text(.25, 3.24, 'it would slide right,', fontsize=7.2, color=G)
    a.text(.25, 2.95, 'so f points left', fontsize=7.2, color=G)

    b = panel(fig, [.35, .08, .30, .86], xlim=(0, 4.2), ylim=(0, 4.6), equal=True)
    b.add_patch(Rectangle((.25, .85), 3.70, .22, fc='#f2f6f5', ec=I, lw=1.2))
    arrow(b, (.45, .55), (3.55, .55), T, 1.4)
    b.text(3.62, .38, 'belt', fontsize=7.4, color=T)
    block(b, 1.75, 1.45, .95, .60)
    arrow(b, (2.30, 1.32), (3.20, 1.32), R, 1.6)
    b.text(2.15, 1.72, 'f', fontsize=8.4, color=R)
    b.text(.25, 3.62, 'on a moving belt', fontsize=8.0, color=T)
    b.text(.25, 3.24, 'the block lags behind,', fontsize=7.2, color=G)
    b.text(.25, 2.95, 'so f points forward', fontsize=7.2, color=G)

    c = panel(fig, [.68, .08, .30, .86], xlim=(0, 4.2), ylim=(0, 4.6), equal=True)
    th = 28.0
    c.add_patch(Polygon([(.25, .75), (3.95, .75), (3.95, .75 + 3.70 * np.tan(np.radians(th)))],
                        closed=True, fc='#f2f6f5', ec=I, lw=1.4))
    ux, uy = np.cos(np.radians(th)), np.sin(np.radians(th))
    px, py = .25 + 1.95 * ux, .75 + 1.95 * uy
    nx, ny = -uy, ux
    corners = []
    for du, dn in ((-.48, 0), (.48, 0), (.48, .34), (-.48, .34)):
        corners.append((px + du * ux + dn * nx, py + du * uy + dn * ny))
    c.add_patch(Polygon(corners, closed=True, fc='#fdf0bd', ec=GOLD, lw=1.4))
    arrow(c, (px + .35 * ux, py + .35 * uy), (px + 1.45 * ux, py + 1.45 * uy), T, 1.6)
    c.text(px + 1.10 * ux + .18, py + 1.10 * uy + .20, 'v', fontsize=8.4, color=T)
    arrow(c, (px - .35 * ux, py - .35 * uy), (px - 1.30 * ux, py - 1.30 * uy), R, 1.6)
    c.text(px - 1.10 * ux - .42, py - 1.10 * uy - .30, 'f', fontsize=8.4, color=R)
    c.text(.25, 3.62, 'sliding up a ramp', fontsize=8.0, color=T)
    c.text(.25, 3.24, 'friction acts down', fontsize=7.2, color=G)
    c.text(.25, 2.95, 'the slope', fontsize=7.2, color=G)

    a.text(.02, .05, 'static friction opposes the tendency to slip; kinetic friction opposes the slip itself',
           fontsize=0.1, color='white')
    return 'Friction is about relative slip at the contact, not about the body\u2019s motion in the room'


def _stacked_blocks(fig):
    a = panel(fig, [.02, .06, .48, .88], xlim=(0, 5.2), ylim=(0, 4.6), equal=True)
    a.add_patch(Rectangle((.20, .55), 4.75, .16, fc='#f2f6f5', ec=I, lw=1.2))
    block(a, 2.05, 1.15, 2.60, .86, '#fdf0bd', GOLD)
    block(a, 2.05, 1.98, 1.45, .66, '#f6dedb', R)
    arrow(a, (3.10, 1.22), (4.45, 1.22), T, 1.8)
    a.text(4.55, 1.08, 'F', fontsize=8.6, color=T)
    arrow(a, (1.78, 1.80), (2.38, 1.80), R, 1.5)
    a.text(2.47, 1.86, 'f on m', fontsize=7.6, color=R)
    arrow(a, (2.30, 1.36), (1.70, 1.36), R, 1.5)
    a.text(1.62, 1.10, 'f on M', fontsize=7.6, color=R, ha='right')
    a.text(1.18, 2.02, r'$m$', fontsize=8.8, color=R, ha='right')
    a.text(.62, 1.10, r'$M$', fontsize=8.8, color=GOLD, ha='right')
    a.text(.2, .16, 'table frictionless', fontsize=7.4, color=G)
    head(a, 'the friction that drags the top block')

    b = panel(fig, [.58, .20, .38, .66])
    axes2(b, 'push  F  (N)', 'common acceleration  (m/s$^2$)')
    F = np.linspace(0, 30, 300)
    b.plot(F, np.minimum(F / 3.0, 2.94), color=T, lw=2.2)
    b.plot([8.82, 30], [2.94, 2.94], color=HG, lw=1.0, ls=(0, (4, 3)))
    b.plot([8.82], [2.94], 'o', ms=5.5, color=R, zorder=5)
    b.annotate(r'$F_{\max}=\mu_sg(M+m)$', xy=(8.82, 2.94), xytext=(10.5, 1.45),
               fontsize=7.8, color=R, arrowprops=dict(arrowstyle='->', color=R, lw=.8))
    b.text(12.5, .42, 'the top block slips: a stops', fontsize=7.4, color=G)
    b.set_xlim(0, 30); b.set_ylim(0, 3.4)
    head(b, 'together only up to a point')
    return 'The top block is driven by friction alone, so it caps the whole system at a = mu_s g'


def _min_pull(fig):
    a = panel(fig, [.10, .20, .50, .66])
    axes2(a, 'pull angle  (degrees)', 'force needed  (N)')
    mu, m, g = .5, 2.0, 9.8
    th = np.linspace(0, 75, 300)
    F = mu * m * g / (np.cos(np.radians(th)) + mu * np.sin(np.radians(th)))
    a.plot(th, F, color=T, lw=2.2)
    best = np.degrees(np.arctan(mu))
    a.plot([best], [mu * m * g / np.hypot(1, mu)], 'o', ms=5.5, color=R, zorder=5)
    a.annotate(r'$\theta=\tan^{-1}\mu$', xy=(best, 8.77), xytext=(33, 7.9),
               fontsize=8.0, color=R, arrowprops=dict(arrowstyle='->', color=R, lw=.8))
    a.text(33.5, 7.35, r'$F_{\min}=\mu mg/\sqrt{1+\mu^2}$', fontsize=8.0, color=R)
    a.axhline(mu * m * g, color=HG, lw=1.0, ls=(0, (4, 3)))
    a.text(2.0, mu * m * g + .55, r'$\mu mg$ (horizontal pull)', fontsize=7.4, color=G)
    a.set_xlim(0, 75); a.set_ylim(6.8, 12)
    head(a, 'pulling up relieves the normal force')

    b = panel(fig, [.66, .10, .32, .80], xlim=(0, 10), ylim=(0, 4.6), equal=True)
    b.add_patch(Rectangle((.8, .75), 8.4, .20, fc='#f2f6f5', ec=I, lw=1.2))
    block(b, 4.3, 1.35, 3.0, 1.00)
    P = (5.55, 2.05)
    ang = np.radians(34)
    Q = (P[0] + 2.3 * np.cos(ang), P[1] + 2.3 * np.sin(ang))
    arrow(b, P, Q, T, 1.9)
    b.text(Q[0] + .10, Q[1] - .06, 'F', fontsize=8.6, color=T)
    b.plot([P[0], P[0] + 1.5], [P[1], P[1]], color=HG, lw=1.0, ls=(0, (3, 2)))
    b.add_patch(Arc(P, 1.7, 1.7, theta1=0, theta2=34, color=I, lw=1.1))
    b.text(P[0] + 1.25, P[1] + .30, r'$\theta$', fontsize=8.4, color=I)
    arrow(b, (3.30, 1.35), (3.30, 2.55), G, 1.6)
    b.text(3.42, 2.42, 'N', fontsize=8.4, color=G)
    arrow(b, (4.30, 1.35), (4.30, .05), R, 1.6)
    b.text(4.42, .18, 'mg', fontsize=8.4, color=R)
    b.text(.8, 3.60, r'$N=mg-F\sin\theta$', fontsize=8.8, color=I)
    b.text(.8, 3.02, r'$f=\mu N$', fontsize=8.8, color=I)
    return 'Tilting the pull up steals normal force from the floor, and the best tilt is exactly arctan(mu)'


def _movable_pulley(fig):
    a = panel(fig, [.02, .08, .54, .84], xlim=(0, 6.4), ylim=(0, 5.5), equal=True)
    a.plot([.4, 5.6], [4.32, 4.32], color=I, lw=2.2)
    for x in (1.6, 4.6):
        a.plot([x, x], [4.32, 3.98], color=I, lw=1.4)
    a.add_patch(Circle((1.6, 3.64), .34, fc='white', ec=I, lw=1.4))
    a.add_patch(Circle((4.6, 3.64), .34, fc='white', ec=I, lw=1.4))
    a.add_patch(Circle((3.10, 2.10), .38, fc='white', ec=T, lw=1.7))
    a.plot([1.6, 3.10 - .38], [3.30, 2.10], color=I, lw=1.4)
    a.plot([3.10 + .38, 4.6], [2.10, 3.30], color=I, lw=1.4)
    a.plot([3.10, 3.10], [1.72, 1.35], color=I, lw=1.4)
    block(a, 3.10, 1.05, 1.05, .58, '#fdf0bd', GOLD)
    a.plot([1.6, 1.6], [3.30, 1.35], color=T, lw=1.4)
    block(a, 1.55, 1.05, 1.05, .58, '#f6dedb', R)
    a.text(1.10, .55, r'$m_1$', fontsize=8.8, color=R)
    a.text(3.70, .55, r'$m_2$', fontsize=8.8, color=GOLD)
    dimy(a, 5.55, 1.35, 4.32, r'$x_1$', 'right', T, 7.8)
    dimy(a, 6.15, 2.10, 4.32, r'$x_2$', 'right', GOLD, 7.8)
    a.text(.45, .12, r'$x_1+2x_2=\mathrm{const}$', fontsize=8.6, color=I)
    head(a, 'one string, three segments')

    b = panel(fig, [.62, .20, .36, .64])
    axes2(b, r'$a$ of the free end  (m/s$^2$)', r'$a$ of the pulley  (m/s$^2$)')
    x = np.linspace(-3, 3, 200)
    b.plot(x, -x / 2, color=T, lw=2.2)
    b.plot([0], [0], 'o', ms=4.5, color=G)
    b.text(1.15, -1.45, r'$a_2=-a_1/2$', fontsize=8.4, color=T)
    b.set_xlim(-3, 3); b.set_ylim(-1.9, 1.9)
    head(b, 'differentiate twice')
    return 'The string length is x1 + 2x2, so the free end accelerates twice as hard as the pulley'


def _wedge_constraint(fig):
    a = panel(fig, [.02, .08, .62, .86], xlim=(0, 7.6), ylim=(0, 4.6), equal=True)
    th = 33.0
    ux, uy = np.cos(np.radians(th)), np.sin(np.radians(th))
    x0, y0 = .70, .75
    L = 5.4
    a.add_patch(Polygon([(x0, y0), (x0 + L, y0 + L * np.tan(np.radians(th))),
                         (x0 + L, y0)], closed=True, fc='#f2f6f5', ec=I, lw=1.8))
    a.plot([x0 - .35, x0 + L + .45], [y0, y0], color=I, lw=1.4)
    t = 2.55
    P = (x0 + t * ux, y0 + t * uy)
    bw, bh = .98, .52
    nx, ny = -uy, ux
    corners = [(P[0] + du * ux + dn * nx, P[1] + du * uy + dn * ny)
               for du, dn in ((-bw / 2, 0), (bw / 2, 0), (bw / 2, bh), (-bw / 2, bh))]
    a.add_patch(Polygon(corners, closed=True, fc='#fdf0bd', ec=GOLD, lw=1.5, zorder=4))
    arrow(a, (P[0] + .55 * ux, P[1] + .55 * uy),
          (P[0] - 1.55 * ux, P[1] - 1.55 * uy), T, 1.8)
    a.text(P[0] - 1.70 * ux, P[1] - 1.70 * uy - .32, 's', fontsize=9.0, color=T)
    arrow(a, (1.10, .30), (5.60, .30), R, 1.7)
    a.text(5.70, .14, r'$x_w$', fontsize=8.6, color=R)
    a.text(x0 + .10, 4.16, 'the block slides down the face', fontsize=7.6, color=G)
    a.text(x0 + .10, 3.80, 'while the wedge runs right', fontsize=7.6, color=G)

    b = panel(fig, [.66, .12, .32, .78], xlim=(0, 10), ylim=(0, 4.6))
    b.axis('off')
    b.text(.2, 3.75, r'$x_b=x_w-s\cos\theta$', fontsize=9.0, color=T)
    b.text(.2, 3.05, r'$y_b=y_0-s\sin\theta$', fontsize=9.0, color=T)
    b.text(.2, 2.20, 'one constraint links', fontsize=7.8, color=I)
    b.text(.2, 1.80, 'the two coordinates', fontsize=7.8, color=I)
    b.text(.2, 1.40, 'differentiate twice for a', fontsize=7.4, color=I)
    b.text(.2, .45, r'$a_b\neq a_w$', fontsize=9.0, color=R)
    return 'A contact is a geometric constraint: it links coordinates before it links forces'


def _pseudo_frame(fig):
    a = panel(fig, [.02, .10, .50, .82], xlim=(0, 7.0), ylim=(0, 4.6), equal=True)
    a.add_patch(Rectangle((1.05, 1.00), 4.70, 1.85, fc='white', ec=I, lw=1.6))
    a.add_patch(Rectangle((1.05, 2.62), 4.70, .16, fc='#f2f6f5', ec=I, lw=1.2))
    a.add_patch(Circle((2.05, .92), .26, fc='#f2f6f5', ec=I, lw=1.3))
    a.add_patch(Circle((4.75, .92), .26, fc='#f2f6f5', ec=I, lw=1.3))
    P = (4.55, 2.62)
    ang = np.radians(30)
    B = (P[0] - 1.55 * np.sin(ang), P[1] - 1.55 * np.cos(ang))
    a.plot([P[0], B[0]], [P[1], B[1]], color=I, lw=1.5)
    a.add_patch(Circle(B, .19, fc='#fdf0bd', ec=GOLD, lw=1.3, zorder=5))
    a.plot([P[0], P[0]], [P[1], P[1] - 1.05], color=HG, lw=.9, ls=(0, (3, 2)))
    a.add_patch(Arc(P, 1.30, 1.30, theta1=240, theta2=270, color=I, lw=1.0))
    a.text(P[0] - .62, P[1] - .78, r'$\theta$', fontsize=8.4, color=I)
    arrow(a, (2.20, .34), (5.40, .34), T, 1.7)
    a.text(5.50, .18, r'$a_0$', fontsize=8.6, color=T)
    a.text(1.15, 4.16, 'accelerating car: the bob hangs askew', fontsize=7.8, color=G)

    b = panel(fig, [.56, .10, .20, .82], xlim=(0, 4.4), ylim=(0, 4.6), equal=True)
    O = (2.55, 2.25)
    T_end = (O[0] + 1.65 * np.sin(np.radians(31)), O[1] + 1.65 * np.cos(np.radians(31)))
    arrow(b, O, T_end, GOLD, 1.8)
    b.text(T_end[0] + .12, T_end[1] + .02, r'$T$', fontsize=8.6, color=GOLD)
    arrow(b, O, (O[0] - 1.45, O[1]), R, 1.7)
    b.text(O[0] - 1.50, O[1] + .18, r'$ma_0$', fontsize=8.6, color=R, ha='right')
    arrow(b, O, (O[0], O[1] - 1.55), I, 1.7)
    b.text(O[0] + .14, O[1] - 1.62, r'$mg$', fontsize=8.6, color=I)
    b.add_patch(Circle(O, .10, fc=I, ec=I))
    b.plot([O[0], O[0]], [O[1], O[1] + 1.55], color=HG, lw=.9, ls=(0, (3, 2)))
    b.add_patch(Arc(O, 1.15, 1.15, theta1=59, theta2=90, color=I, lw=1.0))
    b.text(O[0] - .22, O[1] + .70, r'$\theta$', fontsize=8.2, color=I, ha='right')

    c = panel(fig, [.79, .12, .20, .80], xlim=(0, 10), ylim=(0, 4.6))
    c.axis('off')
    c.text(.2, 3.62, r'$\tan\theta=a_0/g$', fontsize=9.2, color=T)
    c.text(.2, 2.90, r'$g_{\mathrm{eff}}=\sqrt{g^2+a_0^2}$', fontsize=8.8, color=T)
    c.text(.2, 2.05, 'in the car frame', fontsize=7.4, color=I)
    c.text(.2, 1.65, 'add the pseudo force', fontsize=7.4, color=I)
    c.text(.2, .80, 'the string lines up', fontsize=7.4, color=G)
    c.text(.2, .42, 'with g_eff', fontsize=7.4, color=G)
    return 'In an accelerating frame, add -ma and then use ordinary equilibrium'


def _centripetal_sources(fig):
    fig.text(.5, .93, r'$\sum F_{\mathrm{inward}}=mv^2/R$', fontsize=9.6, color=T, ha='center')
    fig.text(.5, .885, 'the resultant is named, not added', fontsize=7.8, color=G, ha='center')

    a = panel(fig, [.03, .10, .29, .66], xlim=(0, 5.0), ylim=(0, 5.0), equal=True)
    a.add_patch(Circle((2.5, 2.5), 1.75, fc='none', ec=HG, lw=1.0, ls=(0, (4, 3))))
    a.add_patch(Circle((2.5, 2.5), .07, fc=I, ec=I))
    a.add_patch(Circle((4.25, 2.5), .22, fc='#fdf0bd', ec=GOLD, lw=1.3, zorder=5))
    arrow(a, (4.05, 2.5), (2.70, 2.5), R, 1.7)
    a.text(3.20, 2.66, r'$T$', fontsize=8.8, color=R)
    a.plot([2.5, 4.25], [2.5, 2.5], color=I, lw=1.0)
    a.text(2.5, .55, 'seen from above', fontsize=7.2, color=G, ha='center')
    head(a, 'string')

    b = panel(fig, [.35, .10, .29, .66], xlim=(0, 5.0), ylim=(0, 5.0), equal=True)
    th = 20.0
    b.plot([.35, 4.75], [.80, .80 + 4.40 * np.tan(np.radians(th))], color=I, lw=2.0)
    b.plot([.15, 4.85], [.80, .80], color=HG, lw=.9, ls=(0, (4, 3)))
    ux, uy = np.cos(np.radians(th)), np.sin(np.radians(th))
    P = (.62 + 2.30 * ux, .80 + 2.30 * uy + .02)
    bw, bh = 1.05, .50
    nx, ny = -uy, ux
    corners = [(P[0] + du * ux + dn * nx, P[1] + du * uy + dn * ny)
               for du, dn in ((-bw / 2, 0), (bw / 2, 0), (bw / 2, bh), (-bw / 2, bh))]
    b.add_patch(Polygon(corners, closed=True, fc='#f6dedb', ec=R, lw=1.4, zorder=4))
    C = (P[0], P[1] + .25 * ny)
    arrow(b, C, (C[0] + 1.55 * nx, C[1] + 1.55 * ny), T, 1.8)
    b.text(C[0] + 1.70 * nx, C[1] + 1.70 * ny, r'$N$', fontsize=8.8, color=T)
    arrow(b, C, (C[0], C[1] - 1.30), I, 1.8)
    b.text(C[0] + .14, C[1] - 1.28, r'$mg$', fontsize=8.2, color=I)
    head(b, 'bank')

    c = panel(fig, [.67, .10, .30, .66], xlim=(0, 5.0), ylim=(0, 5.0), equal=True)
    tt = np.linspace(0, np.pi, 200)
    c.plot(2.5 + 2.1 * np.cos(tt), 1.55 + 1.95 * np.sin(tt), color=I, lw=2.0)
    c.add_patch(Circle((2.5, 3.42), .26, fc='#f6dedb', ec=R, lw=1.3, zorder=5))
    arrow(c, (2.5, 3.68), (2.5, 4.55), T, 1.5)
    c.text(2.66, 4.18, r'$N$', fontsize=8.4, color=T)
    arrow(c, (2.5, 3.16), (2.5, 2.20), I, 1.7)
    c.text(2.62, 2.22, r'$mg$', fontsize=8.4, color=I)
    c.text(2.5, .50, r'$mg-N=mv^2/R$', fontsize=8.6, color=R, ha='center')
    head(c, 'hill crest')
    return 'Centripetal force is the name of the inward resultant, never an extra arrow'


def _banked_design(fig):
    a = panel(fig, [.02, .08, .50, .86], xlim=(0, 6.6), ylim=(0, 5.6), equal=True)
    th = 22.0
    ux, uy = np.cos(np.radians(th)), np.sin(np.radians(th))
    V = (.75, .80)
    a.plot([V[0], 6.10], [V[1], V[1] + 5.35 * np.tan(np.radians(th))], color=I, lw=2.4)
    a.plot([V[0], 4.40], [V[1], V[1]], color=HG, lw=1.0, ls=(0, (4, 3)))
    P = (V[0] + 2.15 * ux, V[1] + 2.15 * uy)
    bw, bh = 1.20, .58
    nx, ny = -uy, ux
    corners = [(P[0] + du * ux + dn * nx, P[1] + du * uy + dn * ny)
               for du, dn in ((-bw / 2, 0), (bw / 2, 0), (bw / 2, bh), (-bw / 2, bh))]
    a.add_patch(Polygon(corners, closed=True, fc='#f6dedb', ec=R, lw=1.4, zorder=4))
    C = (P[0], P[1] + .29 * ny)
    arrow(a, C, (C[0] + 1.75 * nx, C[1] + 1.75 * ny), T, 1.9)
    a.text(C[0] + 1.90 * nx, C[1] + 1.90 * ny, r'$N$', fontsize=8.8, color=T)
    arrow(a, C, (C[0], C[1] - 1.62), I, 1.9)
    a.text(C[0] + .12, C[1] - 1.68, r'$mg$', fontsize=8.6, color=I)
    a.add_patch(Arc(V, 1.45, 1.45, theta1=0, theta2=th, color=I, lw=1.1))
    a.text(V[0] + .80, V[1] + .14, r'$\theta$', fontsize=8.4, color=I)
    a.text(.40, 5.34, r'$N\cos\theta=mg$', fontsize=9.0, color=T)
    a.text(.40, 4.80, r'$N\sin\theta=mv^2/R$', fontsize=9.0, color=T)
    a.text(.40, 4.28, r'$v^2=Rg\tan\theta$', fontsize=9.0, color=R)

    b = panel(fig, [.56, .18, .40, .68])
    axes2(b, 'bank angle  (degrees)', 'design speed  (m/s)')
    thd = np.linspace(0, 45, 300)
    for R_, c, lab in ((50, T, 'R = 50 m'), (100, GOLD, 'R = 100 m')):
        b.plot(thd, np.sqrt(R_ * 9.8 * np.tan(np.radians(thd))), color=c, lw=2.2, label=lab)
    b.legend(frameon=False, fontsize=7.6, loc='upper left')
    b.set_xlim(0, 45); b.set_ylim(0, 32)
    head(b, 'steeper bank, faster design speed')
    return 'With no friction there is exactly one speed that needs no friction at all'


def _banked_band(fig):
    a = panel(fig, [.10, .18, .56, .68])
    axes2(a, r'friction coefficient  $\mu$', 'speed range  (m/s)')
    th, R_ = np.radians(15), 50.0
    mu = np.linspace(0, .8, 300)
    vmax = np.sqrt(R_ * 9.8 * (np.sin(th) + mu * np.cos(th)) / (np.cos(th) - mu * np.sin(th)))
    vmin = np.sqrt(R_ * 9.8 * np.clip(np.sin(th) - mu * np.cos(th), 0, None) /
                   (np.cos(th) + mu * np.sin(th)))
    a.plot(mu, vmax, color=R, lw=2.0)
    a.plot(mu, vmin, color=T, lw=2.0)
    a.fill_between(mu, vmin, vmax, color='#fdf0bd', alpha=.55)
    a.text(.05, 23, r'$v_{\max}$', fontsize=8.6, color=R)
    a.text(.05, 3.0, r'$v_{\min}$', fontsize=8.6, color=T)
    a.text(.30, 12.5, 'allowed range', fontsize=8.0, color=GOLD)
    a.set_xlim(0, .8); a.set_ylim(0, 30)
    head(a, 'friction widens the design speed into a band')

    b = panel(fig, [.72, .12, .26, .78], xlim=(0, 10), ylim=(0, 4.6))
    b.axis('off')
    rows = ((r'$v_{\min}$', 'friction must point', 'up the slope', T),
            (r'$v_0$', 'friction is zero', 'at the design speed', G),
            (r'$v_{\max}$', 'friction must point', 'down the slope', R))
    for k, (f, l1, l2, c) in enumerate(rows):
        y = 3.95 - k * 1.28
        b.text(.2, y, f, fontsize=9.0, color=c)
        b.text(.2, y - .46, l1, fontsize=7.2, color=I)
        b.text(.2, y - .82, l2, fontsize=7.2, color=I)
    b.text(.2, .28, 'narrow band at small mu', fontsize=7.0, color=G)
    return 'Friction does not set the design speed; it allows a range of speeds around it'


def _conical_pendulum(fig):
    a = panel(fig, [.04, .08, .44, .86], xlim=(0, 10), ylim=(0, 5.30), equal=True)
    a.plot([1.2, 8.4], [4.20, 4.20], color=I, lw=2.0)
    a.plot([4.8, 4.8], [4.20, 1.10], color=HG, lw=1.0, ls=(0, (4, 3)))
    a.plot([4.8, 4.8 + 2.55 * np.sin(np.radians(35))],
           [4.20, 4.20 - 2.55 * np.cos(np.radians(35))], color=I, lw=1.5)
    a.add_patch(Circle((4.8 + 2.55 * np.sin(np.radians(35)),
                        4.20 - 2.55 * np.cos(np.radians(35))), .22,
                       fc='#fdf0bd', ec=GOLD, lw=1.2))
    a.add_patch(Ellipse((4.8, 1.10), 2.9, .38, fc='none', ec=T, lw=1.0, ls=(0, (4, 3))))
    a.add_patch(Arc((4.8, 4.20), 1.5, 1.5, theta1=270, theta2=270 + 35, color=I, lw=1.0))
    a.text(5.05, 3.42, r'$\theta$', fontsize=8.2, color=I)
    dimy(a, 7.95, 1.10, 4.20, r'$L\cos\theta$', 'right', G, 7.6)
    a.text(5.75, 1.18, r'$r=L\sin\theta$', fontsize=8.0, color=T)
    a.text(1.35, .35, r'$T\cos\theta=mg$', fontsize=8.2, color=I)
    head(a, r'the bob rides a cone of half-angle $\theta$')

    b = panel(fig, [.56, .20, .40, .66])
    axes2(b, r'angle from vertical  $\theta$  (degrees)', 'period  (s)')
    th = np.linspace(0, 70, 200)
    b.plot(th, 2 * np.pi * np.sqrt(1.0 * np.cos(np.radians(th)) / 9.8), color=T, lw=2.2)
    b.plot([0], [2 * np.pi * np.sqrt(1 / 9.8)], 'o', ms=5, color=G, zorder=5)
    b.annotate('simple pendulum', xy=(0, 2.006), xytext=(12, 2.14), fontsize=7.4, color=G,
               arrowprops=dict(arrowstyle='->', color=G, lw=.8))
    b.set_xlim(0, 70); b.set_ylim(1.4, 2.25)
    head(b, 'it shortens as the cone opens')
    return 'The vertical component carries the weight, so the period depends on L cos(theta), never on mass'


def _vertical_circle_string(fig):
    a = panel(fig, [.04, .06, .52, .86], xlim=(0, 10), ylim=(0, 5.2), equal=True)
    C = (4.6, 2.50)
    R_ = 1.65
    a.add_patch(Circle(C, R_, fc='none', ec=HG, lw=1.4, ls=(0, (3, 3))))
    a.plot([C[0]], [C[1]], 'o', ms=3, color=I)
    a.plot([C[0], C[0]], [C[1], C[1] - R_], color=HG, lw=.9, ls=(0, (2, 2)))
    a.plot([C[0], C[0] + R_ * np.sin(np.radians(55))],
           [C[1], C[1] - R_ * np.cos(np.radians(55))], color=HG, lw=.9, ls=(0, (2, 2)))
    a.add_patch(Arc(C, 1.0, 1.0, theta1=270, theta2=325, color=I, lw=1.0))
    a.text(C[0] + .38, C[1] - .82, r'$\theta$', fontsize=8.0, color=I)
    for phi, lab, off in ((0, r'$6mg$', (0, -.52)), (90, r'$3mg$', (.30, -.10)),
                          (180, r'$0$', (.28, .10))):
        x = C[0] + R_ * np.sin(np.radians(phi))
        y = C[1] - R_ * np.cos(np.radians(phi))
        a.add_patch(Circle((x, y), .18, fc='#fdf0bd', ec=GOLD, lw=1.2, zorder=4))
        a.text(x + off[0], y + off[1], lab, fontsize=8.4, color=R)
    a.text(.35, 4.85, 'a string at the limiting speed', fontsize=7.8, color=T)
    a.text(.35, .45, r'$T(\theta)=3mg(1+\cos\theta)$', fontsize=8.6, color=I)
    a.text(.35, .05, r'$v_{\mathrm{bot}}=\sqrt{5gR}$', fontsize=8.2, color=G)

    b = panel(fig, [.60, .18, .37, .68])
    axes2(b, r'angle from the bottom  $\theta$  (degrees)', r'tension  $T/mg$')
    th = np.linspace(0, 180, 300)
    b.plot(th, 3 * (1 + np.cos(np.radians(th))), color=T, lw=2.2)
    b.axhline(0, color=HG, lw=.9)
    b.plot([180], [0], 'o', ms=5, color=R, zorder=5)
    b.annotate(r'$T=0$ at the top', xy=(180, 0), xytext=(96, 1.05), fontsize=7.6, color=R,
               arrowprops=dict(arrowstyle='->', color=R, lw=.8))
    b.set_xlim(0, 180); b.set_ylim(-.4, 6.4)
    b.set_xticks([0, 60, 120, 180])
    head(b, 'tension falls all the way up')
    return 'At the limiting launch the string is just taut at the top: six mg at the bottom, zero at the top'


def _vertical_circle_rod(fig):
    a = panel(fig, [.04, .06, .50, .86], xlim=(0, 10), ylim=(0, 5.2), equal=True)
    C = (4.6, 2.55)
    R_ = 1.65
    a.add_patch(Circle(C, R_, fc='none', ec=HG, lw=1.4, ls=(0, (3, 3))))
    a.add_patch(Circle(C, .09, fc=I, ec=I))
    for phi, lab, off in ((0, r'$5mg$', (0, -.52)), (90, r'$2mg$', (.30, -.10)),
                          (180, r'$-mg$', (.30, .06))):
        x = C[0] + R_ * np.sin(np.radians(phi))
        y = C[1] - R_ * np.cos(np.radians(phi))
        a.plot([C[0], x], [C[1], y], color=I, lw=2.0)
        a.add_patch(Circle((x, y), .18, fc='#fdf0bd', ec=GOLD, lw=1.2, zorder=4))
        a.text(x + off[0], y + off[1], lab, fontsize=8.4, color=R)
    a.text(.35, 4.85, 'launched at just enough speed to reach the top', fontsize=7.6, color=T)
    a.text(.35, .50, r'$N(\theta)=mg(2+3\cos\theta)$', fontsize=8.6, color=I)
    a.text(.35, .10, 'a rod can push as well as pull', fontsize=7.4, color=G)

    b = panel(fig, [.58, .18, .39, .68])
    axes2(b, r'angle from the bottom  $\theta$  (degrees)', r'radial force  $N/mg$')
    th = np.linspace(0, 180, 300)
    N = 2 + 3 * np.cos(np.radians(th))
    b.plot(th, N, color=T, lw=2.2)
    b.axhline(0, color=HG, lw=.9)
    b.plot([131.8], [0], 'o', ms=5, color=R, zorder=5)
    b.annotate(r'rod pushes beyond $131^\circ$', xy=(131.8, 0), xytext=(24, -1.35),
               fontsize=7.4, color=R, arrowprops=dict(arrowstyle='->', color=R, lw=.8))
    b.set_xlim(0, 180); b.set_ylim(-1.6, 5.4)
    b.set_xticks([0, 60, 120, 180])
    head(b, r'it flips sign where $\cos\theta=-2/3$')
    return 'A rod needs no minimum speed at the top, and past 131 degrees it stops pulling and starts pushing'


def _system_vs_parts(fig):
    a = panel(fig, [.03, .10, .46, .82], xlim=(0, 10), ylim=(0, 4.6), equal=True)
    a.add_patch(Rectangle((.55, .95), 8.75, .18, fc='#f2f6f5', ec=I, lw=1.2))
    block(a, 3.60, 1.85, 2.30, 1.30, '#fdf0bd', GOLD)
    block(a, 6.05, 1.85, 1.75, 1.30, '#f6dedb', R)
    a.add_patch(Rectangle((2.05, 1.15), 5.85, 2.42, fc='none', ec=T, lw=1.5, ls=(0, (5, 3))))
    arrow(a, (1.05, 1.85), (2.42, 1.85), T, 1.7)
    a.text(1.12, 2.02, 'F', fontsize=8.8, color=T)
    a.text(3.60, 1.72, r'$m_1$', fontsize=8.8, color=GOLD, ha='center')
    a.text(6.05, 1.72, r'$m_2$', fontsize=8.8, color=R, ha='center')
    a.text(2.05, .55, 'the dashed box is the system', fontsize=7.4, color=T)
    head(a, 'one box, internal forces cancel')

    b = panel(fig, [.54, .18, .42, .68])
    axes2(b, r'mass ratio  $m_2/m_1$', 'contact force  (N)')
    r = np.linspace(.05, 4, 300)
    b.plot(r, 20 * r / (1 + r), color=T, lw=2.2)
    b.axhline(20, color=HG, lw=.9, ls=(0, (4, 3)))
    b.text(.15, 20.5, 'all of it', fontsize=7.4, color=G)
    b.plot([1], [10], 'o', ms=5, color=R, zorder=5)
    b.annotate(r'equal masses: half', xy=(1, 10), xytext=(1.55, 6.0), fontsize=7.4, color=R,
               arrowprops=dict(arrowstyle='->', color=R, lw=.8))
    b.set_xlim(0, 4); b.set_ylim(0, 24)
    head(b, 'F = 20 N on the pair')
    return 'Use the system for the acceleration, then isolate one body for the force between them'


# ================================================================ OLYMPIAD
def _falling_chain(fig):
    a = panel(fig, [.04, .12, .44, .80], xlim=(0, 10), ylim=(0, 4.6), equal=True)
    a.add_patch(Rectangle((1.0, .55), 4.6, .30, fc='#f2f6f5', ec=I, lw=1.3))
    for k in range(9):
        a.add_patch(Ellipse((2.0 + k * .34, .95 + (k % 2) * .12), .30, .17,
                            fc='#fdf0bd', ec=GOLD, lw=.9))
    for k in range(12):
        a.add_patch(Ellipse((5.85, 1.10 + k * .22), .34, .16, fc='#e7f4f1', ec=T, lw=.9))
    a.text(5.10, 3.60, 'chain', fontsize=7.4, color=T)
    arrow(a, (6.55, 3.75), (6.55, 1.55), T, 1.5)
    a.text(6.70, 3.55, 'v', fontsize=8.4, color=T)
    a.text(1.0, .18, 'landed length x', fontsize=7.4, color=G)
    head(a, 'the pile grows as the chain lands')

    b = panel(fig, [.56, .18, .40, .68])
    axes2(b, r'fraction landed  $x/L$', r'scale reading  $F/mg$')
    x = np.linspace(0, 1, 200)
    b.plot(x, 3 * x, color=R, lw=2.2)
    b.plot(x, x, color=HG, lw=1.0, ls=(0, (4, 3)))
    b.plot(x, 2 * x, color=HG, lw=1.0, ls=(0, (2, 2)))
    b.text(.52, .30, r'weight  $x/L$', fontsize=7.4, color=G, rotation=0)
    b.text(.62, 1.72, r'momentum flux  $2x/L$', fontsize=7.4, color=G)
    b.plot([1], [3], 'o', ms=5, color=R, zorder=5)
    b.annotate(r'$3mg$ when all of it has landed', xy=(1, 3), xytext=(.30, 3.22),
               fontsize=7.6, color=R, arrowprops=dict(arrowstyle='->', color=R, lw=.8))
    b.text(.06, 2.72, 'stopping it adds twice its weight', fontsize=7.4, color=G)
    b.set_xlim(0, 1.05); b.set_ylim(0, 3.6)
    head(b, 'three times the weight, not twice')
    return 'A landing chain must be stopped as well as held: the scale reads 3x the landed weight'


def _rocket_ratio(fig):
    a = panel(fig, [.10, .20, .52, .66])
    axes2(a, r'mass ratio  $m_0/m_f$', r'$\Delta v/v_e$')
    r = np.linspace(1, 20, 300)
    a.semilogx(r, np.log(r), color=T, lw=2.2)
    for rv, lab in ((2, r'$\ln 2=0.69$'), (np.e ** 3, r'$3$ at $e^3\approx20$')):
        a.semilogx([rv], [np.log(rv)], 'o', ms=5, color=R, zorder=5)
        a.annotate(lab, xy=(rv, np.log(rv)), xytext=(rv * 1.25, np.log(rv) - .55),
                   fontsize=7.6, color=R,
                   arrowprops=dict(arrowstyle='->', color=R, lw=.8))
    a.set_xlim(1, 20); a.set_ylim(0, 3.2)
    head(a, 'the cost of speed is logarithmic')

    b = panel(fig, [.68, .12, .30, .80], xlim=(0, 10), ylim=(0, 4.6))
    txt(b, .2, 3.85, r'$m\,dv=-v_e\,dm$', fontsize=9.0, color=I)
    txt(b, .2, 3.15, r'$\Delta v=v_e\ln\frac{m_0}{m_f}$', fontsize=9.4, color=T)
    txt(b, .2, 2.20, '9 km/s at 3 km/s exhaust:', fontsize=7.6, color=G)
    txt(b, .2, 1.80, r'$m_0/m_f=e^{3}\approx20$', fontsize=8.6, color=R)
    txt(b, .2, 1.05, '95 % of the launch mass', fontsize=7.6, color=G)
    txt(b, .2, .70, 'is propellant', fontsize=7.6, color=G)
    return 'Every extra km/s costs exponentially in mass: the rocket equation is a budget, not a force'


def _capstan(fig):
    a = panel(fig, [.04, .12, .44, .80], xlim=(0, 10), ylim=(0, 4.6), equal=True)
    a.add_patch(Circle((5.0, 2.20), 1.00, fc='#f2f6f5', ec=I, lw=1.7))
    th = np.linspace(200, 520, 300)
    a.plot(5.0 + 1.24 * np.cos(np.radians(th)), 2.20 + 1.24 * np.sin(np.radians(th)),
           color=T, lw=2.2)
    arrow(a, (3.95, 3.30), (3.35, 3.95), R, 1.5)
    a.text(2.92, 3.72, r'$T_2$', fontsize=8.6, color=R)
    arrow(a, (6.05, .55), (6.75, .05), T, 1.5)
    a.text(6.85, .20, r'$T_1$', fontsize=8.6, color=T)
    a.add_patch(Arc((5.0, 2.20), 2.9, 2.9, theta1=205, theta2=350, color=I, lw=1.0))
    a.text(5.30, 3.42, r'$\theta$', fontsize=8.2, color=I)
    a.text(.35, .30, 'the rope grips harder as it wraps', fontsize=7.2, color=G)
    head(a, 'a rope around a bollard')

    b = panel(fig, [.56, .18, .40, .68])
    axes2(b, r'wrap angle  $\theta$  (rad)', r'tension ratio  $T_2/T_1$')
    th = np.linspace(0, 4 * np.pi, 400)
    for mu, c in ((.1, G), (.3, T), (.5, R)):
        b.plot(th, np.exp(mu * th), color=c, lw=2.0)
        b.text(4 * np.pi - .10, np.exp(mu * 4 * np.pi) * (1.16 if mu == .5 else 1.28),
               r'$\mu=%.1f$' % mu, fontsize=7.4, color=c, ha='right')
    b.set_yscale('log')
    b.set_xlim(0, 4 * np.pi); b.set_ylim(1, 900)
    b.set_yticks([1, 10, 100])
    b.set_yticklabels(['1', '10', '100'])
    b.set_xticks([0, np.pi, 2 * np.pi, 3 * np.pi, 4 * np.pi])
    b.set_xticklabels(['0', r'$\pi$', r'$2\pi$', r'$3\pi$', r'$4\pi$'])
    b.annotate(r'$e^{\mu\theta}$', xy=(2 * np.pi, np.exp(.3 * 2 * np.pi)), xytext=(1.1, 40),
               fontsize=9.0, color=I,
               arrowprops=dict(arrowstyle='->', color=I, lw=.8))
    head(b, 'exponential in the wrap')
    return 'Every radian of wrap multiplies the grip by e to the mu theta'


def _sand_belt(fig):
    a = panel(fig, [.03, .50, .94, .40], xlim=(0, 10), ylim=(0, 3.0))
    a.add_patch(Rectangle((.8, .55), 8.4, .28, fc='#f2f6f5', ec=I, lw=1.4))
    for x in (1.6, 3.4, 5.2, 7.0):
        arrow(a, (x, .69), (x + .95, .69), T, 1.3)
    for k in range(7):
        a.add_patch(Circle((2.55 + k * .26, 2.35 - k * .16), .105, fc=GOLD, ec=GOLD))
    arrow(a, (2.77, 2.72), (2.77, 1.10), GOLD, 1.3)
    a.text(2.98, 2.42, r'$\dot m$', fontsize=8.6, color=GOLD)
    a.text(8.55, 1.02, r'$v$', fontsize=8.6, color=T)
    a.text(.85, .10, 'the sand lands with no horizontal momentum', fontsize=7.4, color=G)
    head(a, 'sand dropped on a moving belt')

    b = panel(fig, [.10, .10, .36, .30])
    axes2(b, '', 'power / mdot v$^2$')
    b.bar([0, 1, 2], [.5, .5, 1.0], color=[T, R, GOLD], width=.62)
    b.set_xlim(-.62, 2.62)
    b.set_xticks([0, 1, 2])
    b.set_xticklabels(['keeps', 'heat', 'belt'])
    b.set_ylim(0, 1.15)
    b.set_yticks([0, .25, .5, .75, 1.0])
    head(b, 'same units of mdot v squared', color=G)

    c = panel(fig, [.56, .10, .40, .34], xlim=(0, 10), ylim=(0, 2.6))
    c.axis('off')
    txt(c, .1, 2.05, r'$F=\dot m v$', fontsize=9.4, color=T)
    txt(c, .1, 1.30, r'$P=Fv=\dot m v^2$', fontsize=9.4, color=GOLD)
    txt(c, .1, .55, r'$\dot K=\frac{1}{2}\dot m v^2$', fontsize=9.0, color=I)
    c.text(1.05, .10, 'the missing half is heat', fontsize=7.8, color=R)
    return 'Accelerating arriving mass costs twice the kinetic energy: the other half is friction heat'


def _bead_hoop(fig):
    a = panel(fig, [.03, .10, .42, .84], xlim=(0, 10), ylim=(0, 5.4), equal=True)
    a.add_patch(Circle((4.4, 2.20), 1.65, fc='none', ec=I, lw=1.6))
    a.plot([4.4, 4.4], [4.30, .10], color=HG, lw=1.0, ls=(0, (4, 3)))
    for sgn in (-1, 1):
        x = 4.4 + 1.65 * np.sin(np.radians(38)) * sgn
        y = 2.20 + 1.65 * np.cos(np.radians(38))
        a.add_patch(Circle((x, y), .18, fc='#f6dedb', ec=R, lw=1.2))
    a.add_patch(Circle((4.4, .55), .18, fc='#dfe9e6', ec=G, lw=1.2))
    a.add_patch(Arc((4.4, 2.20), .95, .95, theta1=270, theta2=308, color=I, lw=.9))
    a.text(4.70, 1.55, r'$\theta$', fontsize=8.2, color=I)
    arrow(a, (4.4, 4.45), (5.70, 4.45), T, 1.2, '<->', 6)
    a.text(5.82, 4.30, r'$\omega$', fontsize=8.6, color=T)
    a.text(4.62, .18, r'$\theta=0$', fontsize=7.4, color=G)
    head(a, 'the hoop spins about its vertical diameter')

    b = panel(fig, [.54, .18, .42, .68])
    axes2(b, r'spin  $\omega/\omega_c$', r'equilibrium angle  $\theta$  (degrees)')
    om = np.linspace(1, 3, 300)
    b.plot(om, np.degrees(np.arccos(1 / om ** 2)), color=T, lw=2.2)
    b.plot([1, 3], [0, 0], color=G, lw=2.0, ls=(0, (4, 3)))
    b.plot([1], [0], 'o', ms=5, color=G, zorder=5)
    b.annotate('bottom is stable below $\\omega_c$', xy=(1.05, 0), xytext=(1.25, 34),
               fontsize=7.4, color=G, arrowprops=dict(arrowstyle='->', color=G, lw=.8))
    b.text(1.75, 62, 'two off-axis positions', fontsize=7.6, color=T)
    b.set_xlim(1, 3); b.set_ylim(0, 90)
    head(b, 'a pitchfork in the equilibrium')
    return 'Below the critical spin the bead sits at the bottom; above it the bottom becomes unstable and two new seats appear'


def _chain_lift(fig):
    a = panel(fig, [.04, .12, .44, .80], xlim=(0, 10), ylim=(0, 4.6), equal=True)
    a.add_patch(Rectangle((3.6, .55), 2.6, .35, fc='#f2f6f5', ec=I, lw=1.3))
    for k in range(6):
        a.add_patch(Ellipse((3.85 + k * .38, .95), .32, .16, fc='#dfe9e6', ec=G, lw=.8))
    a.plot([4.6, 4.6], [1.10, 3.55], color=GOLD, lw=2.6)
    arrow(a, (4.6, 3.55), (4.6, 4.10), T, 1.5)
    a.text(4.80, 3.62, 'v constant', fontsize=7.8, color=T)
    a.text(2.05, 3.30, 'lifted length x', fontsize=7.6, color=G)
    head(a, 'a chain pulled up from a heap')

    b = panel(fig, [.58, .18, .38, .68])
    axes2(b, 'lifted length  x  (m)', 'force  (N)')
    lam, v, g = 0.4, 1.5, 9.8
    x = np.linspace(0, 3, 200)
    b.plot(x, lam * g * x, color=G, lw=1.8, ls=(0, (4, 3)))
    b.plot(x, lam * v ** 2 * np.ones_like(x), color=T, lw=1.8, ls=(0, (4, 3)))
    b.plot(x, lam * g * x + lam * v ** 2, color=R, lw=2.3)
    b.text(.30, 10.8, r'$F=\lambda gx+\lambda v^2$', fontsize=8.2, color=R)
    b.text(.30, 9.4, r'weight only, $\lambda gx$', fontsize=7.2, color=G)
    b.annotate(r'momentum flux $\lambda v^2$', xy=(1.85, lam * v ** 2), xytext=(1.70, 4.2),
               fontsize=7.2, color=T, arrowprops=dict(arrowstyle='->', color=T, lw=.8))
    b.set_xlim(0, 3); b.set_ylim(0, 14)
    head(b, 'a constant offset above the weight')
    return 'Lifting at constant speed still costs an extra momentum-flux force, lambda v squared'


def _turntable(fig):
    a = panel(fig, [.03, .08, .44, .86], xlim=(0, 10), ylim=(0, 5.6), equal=True)
    a.add_patch(Circle((4.6, 2.20), 2.55, fc='#f2f6f5', ec=I, lw=1.4))
    a.add_patch(Circle((4.6, 2.20), .12, fc=I, ec=I))
    a.plot([4.6, 4.6], [2.20, 3.15], color=I, lw=1.3)
    a.add_patch(Rectangle((4.35, 3.15), .50, .34, fc='#f6dedb', ec=R, lw=1.2))
    arrow(a, (4.6, 2.20), (7.0, 2.20), HG, 1.0, '<->', 6)
    a.text(5.55, 2.32, 'r', fontsize=8.2, color=G)
    a.add_patch(Arc((4.6, 2.20), 4.2, 4.2, theta1=25, theta2=100, color=T, lw=1.4))
    a.text(6.35, 3.35, r'$\omega$', fontsize=8.6, color=T)
    head(a, 'top view: block tied to the axis')

    b = panel(fig, [.55, .18, .42, .68])
    axes2(b, r'radius  r  (m)', r'required friction  (N)')
    om, m, mu = 4.0, .5, .3
    r = np.linspace(0, 1.2, 300)
    b.plot(r, m * om ** 2 * r, color=T, lw=2.2)
    b.axhline(mu * m * 9.8, color=R, lw=1.6, ls=(0, (4, 3)))
    b.text(.05, mu * m * 9.8 + .35, r'$\mu mg$ cap', fontsize=7.6, color=R)
    rc = mu * 9.8 / om ** 2
    b.plot([rc], [mu * m * 9.8], 'o', ms=5.5, color=R, zorder=5)
    b.annotate(r'slips beyond $r_c=\mu g/\omega^2$', xy=(rc, mu * m * 9.8), xytext=(.30, 4.30),
               fontsize=7.4, color=R, arrowprops=dict(arrowstyle='->', color=R, lw=.8))
    b.set_xlim(0, 1.2); b.set_ylim(0, 6.2)
    head(b, 'friction supplies the centripetal force')
    return 'A block on a turntable stays only while friction can supply m omega squared r'


def _staging(fig):
    a = panel(fig, [.16, .24, .42, .62])
    axes2(a, '', r'ideal $\Delta v$  (km/s)')
    a.bar([0, 1], [3.22, 3.62], color=[G, T], width=.55)
    a.text(0, 3.30, '3.22', fontsize=8.4, color=G, ha='center')
    a.text(1, 3.70, '3.62', fontsize=8.4, color=T, ha='center')
    a.set_xlim(-.62, 1.62)
    a.set_xticks([0, 1]); a.set_xticklabels(['one stage', 'two stages'], fontsize=7.4)
    a.set_ylim(0, 4.3)
    head(a, 'same fuel, same structure, 0.4 km/s more')

    b = panel(fig, [.66, .12, .32, .80], xlim=(0, 10), ylim=(0, 4.6))
    txt(b, .2, 3.95, 'stage 1', fontsize=7.8, color=T)
    txt(b, .2, 3.55, '1000 → 600 kg', fontsize=8.0, color=I)
    txt(b, .2, 3.15, 'Δv = 1.02 km/s', fontsize=8.0, color=T)
    txt(b, .2, 2.55, 'drop 50 kg', fontsize=7.8, color=G)
    txt(b, .2, 2.15, '550 → 150 kg', fontsize=8.0, color=I)
    txt(b, .2, 1.75, 'Δv = 2.60 km/s', fontsize=8.0, color=T)
    txt(b, .2, 1.15, 'single stage', fontsize=7.8, color=G)
    txt(b, .2, .75, '1000 → 200 kg', fontsize=8.0, color=I)
    return 'Staging wins by throwing away dead structure before the next burn, not by burning harder'


def _impulse_window(fig):
    a = panel(fig, [.10, .20, .54, .66])
    axes2(a, 'time  (ms)', 'force on the ball  (N)')
    t = np.linspace(-.5, 2.5, 400)
    Fb = 1000 * np.exp(-((t - .5) / .22) ** 2)
    a.plot(t, Fb, color=R, lw=2.2)
    a.axhline(1.42, color=G, lw=1.6, ls=(0, (4, 3)))
    a.fill_between(t, 0, Fb, color='#fbeceb')
    a.text(.75, 720, 'bat', fontsize=8.2, color=R)
    a.annotate('weight = 1.4 N', xy=(1.30, 1.42), xytext=(1.28, 105),
               fontsize=7.6, color=G, arrowprops=dict(arrowstyle='->', color=G, lw=.8))
    a.set_ylim(0, 1100); a.set_xlim(-.5, 2.5)
    head(a, 'same window, two forces, 700 times apart')

    b = panel(fig, [.70, .12, .28, .80], xlim=(0, 10), ylim=(0, 4.6))
    txt(b, .2, 3.85, r'$J_{\rm bat}=1$ N s', fontsize=8.4, color=R)
    txt(b, .2, 3.15, r'$J_g=1.4\times10^{-3}$ N s', fontsize=8.4, color=G)
    txt(b, .2, 2.45, 'ratio 0.14 %', fontsize=8.4, color=I)
    txt(b, .2, 1.60, 'so gravity is dropped', fontsize=7.6, color=G)
    txt(b, .2, 1.20, 'for the duration', fontsize=7.6, color=G)
    txt(b, .2, .50, 'of the hit', fontsize=7.6, color=G)
    return 'A force that is huge for a millisecond makes gravity irrelevant; that is the whole impulse approximation'


def _hitch_turns(fig):
    a = panel(fig, [.10, .20, .54, .66])
    axes2(a, 'turns around the carabiner', r'tension ratio  $T_2/T_1$')
    N = np.linspace(0, 3, 300)
    a.plot(N, np.exp(.3 * 2 * np.pi * N), color=T, lw=2.2)
    a.plot([1.22], [10], 'o', ms=5.5, color=R, zorder=5)
    a.annotate('10:1 at 1.22 turns', xy=(1.22, 10), xytext=(1.32, 2.4),
               fontsize=7.6, color=R, arrowprops=dict(arrowstyle='->', color=R, lw=.8))
    a.annotate('3 turns: 287:1', xy=(3, 287), xytext=(1.55, 200), fontsize=7.6, color=R,
               arrowprops=dict(arrowstyle='->', color=R, lw=.8))
    a.set_yscale('log')
    a.set_xlim(0, 3); a.set_ylim(1, 400)
    a.set_yticks([1, 10, 100])
    a.set_yticklabels(['1', '10', '100'])
    head(a, 'mu = 0.3, one wrap is a factor 6.6')

    b = panel(fig, [.72, .12, .26, .80], xlim=(0, 10), ylim=(0, 4.6))
    b.axis('off')
    txt(b, .2, 3.85, r'$T_2=T_1e^{\mu\theta}$', fontsize=8.6, color=T)
    txt(b, .2, 3.05, r'$\theta=2\pi N$', fontsize=8.2, color=I)
    txt(b, .2, 2.30, 'friction does the', fontsize=7.6, color=G)
    txt(b, .2, 1.95, 'holding, the hand', fontsize=7.6, color=G)
    txt(b, .2, 1.60, 'only sets the load', fontsize=7.6, color=G)
    txt(b, .2, .85, 'works for any rope', fontsize=7.6, color=G)
    txt(b, .2, .50, 'diameter', fontsize=7.6, color=G)
    return 'A friction hitch holds because tension decays exponentially along the wrap, not because you grip harder'


def _virtual_work(fig):
    a = panel(fig, [.02, .08, .58, .86], xlim=(0, 7.4), ylim=(0, 5.0), equal=True)
    th = 32.0
    ux, uy = np.cos(np.radians(th)), np.sin(np.radians(th))
    x0, y0 = .70, .70
    L = 5.20
    a.add_patch(Polygon([(x0, y0), (x0 + L, y0), (x0 + L, y0 + L * np.tan(np.radians(th)))],
                        closed=True, fc='#f2f6f5', ec=I, lw=1.8))
    a.plot([x0 - .35, x0 + L + .45], [y0, y0], color=I, lw=1.4)
    t = 2.10
    P = (x0 + t * ux, y0 + t * uy)
    bw, bh = 1.00, .52
    nx, ny = -uy, ux
    corners = [(P[0] + du * ux + dn * nx, P[1] + du * uy + dn * ny)
               for du, dn in ((-bw / 2, 0), (bw / 2, 0), (bw / 2, bh), (-bw / 2, bh))]
    a.add_patch(Polygon(corners, closed=True, fc='#fdf0bd', ec=GOLD, lw=1.5, zorder=4))
    arrow(a, (P[0] + .45 * ux, P[1] + .45 * uy),
          (P[0] - 1.45 * ux, P[1] - 1.45 * uy), T, 1.8)
    mid = (P[0] - .45 * ux + .42 * uy, P[1] - .45 * uy - .42 * ux)
    a.text(mid[0] - .30, mid[1] - .26, r'$\delta s$', fontsize=9.0, color=T)
    arrow(a, (1.00, .28), (5.10, .28), R, 1.7)
    a.text(5.20, .12, r'$\delta x_w$', fontsize=8.6, color=R)
    a.text(x0 + .05, 4.72, 'the contact slides, it does not rub', fontsize=7.6, color=G)

    b = panel(fig, [.64, .10, .34, .84], xlim=(0, 10), ylim=(0, 4.6))
    b.axis('off')
    b.text(.2, 3.92, r'$\delta W=N\cdot\delta s=0$', fontsize=9.2, color=T)
    b.text(.2, 3.42, r'$N\perp\delta s$', fontsize=8.8, color=T)
    b.text(.2, 2.55, 'a normal force does no', fontsize=7.6, color=I)
    b.text(.2, 2.18, 'work when the sliding is', fontsize=7.6, color=I)
    b.text(.2, 1.81, 'along the surface', fontsize=7.6, color=I)
    b.text(.2, .95, 'so the constraint never', fontsize=7.6, color=G)
    b.text(.2, .58, 'appears in the work', fontsize=7.6, color=G)
    return 'Internal contact forces do no work along the constraint, which is why virtual work can skip them'


def _rope_table(fig):
    a = panel(fig, [.04, .12, .44, .80], xlim=(0, 10), ylim=(0, 5.2), equal=True)
    a.add_patch(Rectangle((.50, 2.30), 5.20, .22, fc='#f2f6f5', ec=I, lw=1.4))
    a.plot([.85, 5.55], [2.72, 2.72], color=GOLD, lw=3.2, solid_capstyle='butt')
    a.plot([5.62, 5.62], [2.72, .85], color=GOLD, lw=3.2, solid_capstyle='butt')
    a.text(2.40, 2.92, 'lying on the table', fontsize=7.4, color=G)
    a.text(5.05, 1.05, 'the hanging part', fontsize=7.4, color=GOLD, ha='center')
    dimy(a, 6.85, .85, 2.72, r'$x$', 'right', T, 8.6)
    dimx(a, .85, 5.62, 1.75, 'length L', G, 7.4)
    head(a, 'the hanging part pulls, the rest drags')

    b = panel(fig, [.58, .18, .38, .68])
    axes2(b, r'fraction hanging  $x/L$', r'acceleration  (m/s$^2$)')
    x = np.linspace(0, 1, 300)
    for mu, c, lab in ((0, T, r'$\mu=0$'), (.2, GOLD, r'$\mu=0.2$'), (.4, R, r'$\mu=0.4$')):
        b.plot(x, 9.8 * (x - mu * (1 - x)), color=c, lw=2.0)
        b.text(.02, 9.8 * (-mu) + .35, lab, fontsize=7.2, color=c)
    b.axhline(0, color=HG, lw=.9)
    b.plot([.4 / 1.4], [0], 'o', ms=4.5, color=I, zorder=5)
    b.annotate(r'starts moving at $x/L=\mu/(1+\mu)$', xy=(.4 / 1.4, 0), xytext=(.30, -3.6),
               fontsize=7.2, color=I, arrowprops=dict(arrowstyle='->', color=I, lw=.8))
    b.set_xlim(0, 1); b.set_ylim(-5.2, 10.2)
    head(b, 'friction holds it until enough hangs')
    return 'A rope over an edge accelerates only once the hanging fraction beats friction on the rest'


def _effective_g(fig):
    a = panel(fig, [.03, .14, .44, .76], xlim=(0, 10), ylim=(0, 4.6), equal=True)
    o = (3.0, 3.40)
    arrow(a, o, (3.0, 1.55), G, 1.7)
    a.text(3.15, 2.35, 'g', fontsize=8.4, color=G)
    arrow(a, o, (5.05, 3.40), T, 1.7)
    a.text(4.35, 3.55, r'$a_0$', fontsize=8.4, color=T)
    arrow(a, o, (5.05, 1.55), R, 1.9)
    a.text(4.75, 1.30, r'$g_{\rm eff}$', fontsize=8.4, color=R)
    a.plot([5.05, 5.05], [1.55, 3.40], color=HG, lw=1.0, ls=(0, (3, 3)))
    a.plot([3.0, 5.05], [1.55, 1.55], color=HG, lw=1.0, ls=(0, (3, 3)))
    a.add_patch(Arc((3.0, 3.40), 1.2, 1.2, theta1=270, theta2=270 + 100, color=I, lw=1.0))
    a.text(3.35, 2.85, r'$\phi$', fontsize=8.0, color=I)
    head(a, 'gravity and the frame add as vectors')

    b = panel(fig, [.56, .20, .40, .66])
    axes2(b, r'frame acceleration  $a_0/g$', r'period ratio  $T/T_0$')
    x = np.linspace(0, 3, 300)
    b.plot(x, (1 + x ** 2) ** (-.25), color=T, lw=2.2)
    b.plot([1], [(2) ** -.25], 'o', ms=5, color=R, zorder=5)
    b.annotate(r'$a_0=g$: period shrinks by 0.84', xy=(1, (2) ** -.25), xytext=(1.15, .88),
               fontsize=7.4, color=R, arrowprops=dict(arrowstyle='->', color=R, lw=.8))
    b.set_xlim(0, 3); b.set_ylim(.35, 1.05)
    head(b, 'the pendulum speeds up as the car pulls away')
    return 'Inside an accelerating frame, gravity is replaced by a longer vector tilted by arctan(a0/g)'


def _wedge_liftoff(fig):
    a = panel(fig, [.02, .10, .50, .84], xlim=(0, 8.2), ylim=(0, 5.2), equal=True)
    th = 30.0
    ux, uy = np.cos(np.radians(th)), np.sin(np.radians(th))
    x0, y0, L = .80, .80, 5.30
    a.add_patch(Polygon([(x0, y0), (x0 + L, y0), (x0 + L, y0 + L * np.tan(np.radians(th)))],
                        closed=True, fc='#f2f6f5', ec=I, lw=1.8))
    a.plot([x0 - .35, x0 + L + .45], [y0, y0], color=I, lw=1.4)
    t = 2.35
    P = (x0 + t * ux, y0 + t * uy)
    bw, bh = 1.00, .52
    nx, ny = -uy, ux
    corners = [(P[0] + du * ux + dn * nx, P[1] + du * uy + dn * ny)
               for du, dn in ((-bw / 2, 0), (bw / 2, 0), (bw / 2, bh), (-bw / 2, bh))]
    a.add_patch(Polygon(corners, closed=True, fc='#fdf0bd', ec=GOLD, lw=1.5, zorder=4))
    C = (P[0], P[1] + .26 * ny)
    arrow(a, C, (C[0] - 1.45, C[1] + .22), T, 1.8)
    a.text(C[0] - 1.55, C[1] + .48, r'$ma_0$', fontsize=8.6, color=T, ha='right')
    dashed(a, C, (C[0] + 1.05 * nx, C[1] + 1.05 * ny))
    a.text(C[0] + 1.10 * nx, C[1] + 1.10 * ny, r'$N$', fontsize=8.6, color=G)
    arrow(a, (1.55, .32), (.28, .32), R, 1.8)
    a.text(.75, .06, r'$a_0$', fontsize=8.6, color=R)
    a.text(2.30, 4.72, 'the wedge is yanked to the left', fontsize=7.6, color=G)
    a.text(2.30, 4.34, 'the block keeps going: N falls', fontsize=7.6, color=G)

    b = panel(fig, [.58, .18, .38, .68])
    axes2(b, r'wedge acceleration  $a_0/g$', r'normal force  $N/mg$')
    x = np.linspace(0, 2.6, 300)
    N = np.cos(np.radians(30)) - x * np.sin(np.radians(30))
    b.plot(x, N, color=T, lw=2.2)
    b.axhline(0, color=HG, lw=.9)
    b.plot([1 / np.tan(np.radians(30))], [0], 'o', ms=5.5, color=R, zorder=5)
    b.annotate(r'$a_0=g\cot\theta=1.73g$', xy=(1.80, -.12), xytext=(.55, -.58),
               fontsize=7.4, color=R, arrowprops=dict(arrowstyle='->', color=R, lw=.8))
    b.axvline(1.73, color=R, lw=.9, ls=(0, (3, 3)))
    b.set_xlim(0, 2.6); b.set_ylim(-.75, 1.05)
    b.set_yticks([-.75, -.5, -.25, 0, .25, .5, .75, 1.0])
    head(b, 'contact dies when the normal reaches zero')
    return 'If the wedge is pulled out from under the block, the normal force falls to zero at a0 = g cot(theta)'


def _turntable_limit(fig):
    a = panel(fig, [.10, .20, .54, .66])
    axes2(a, r'angular speed  $\omega$  (rad/s)', r'largest stable radius  (m)')
    mu, g = .3, 9.8
    w = np.linspace(.8, 8, 300)
    a.plot(w, mu * g / w ** 2, color=T, lw=2.2)
    a.plot([2.42], [.5], 'o', ms=5, color=R, zorder=5)
    a.annotate('r = 0.5 m at 2.4 rad/s', xy=(2.42, .5), xytext=(2.9, 1.55),
               fontsize=7.4, color=R, arrowprops=dict(arrowstyle='->', color=R, lw=.8))
    a.set_xlim(.8, 8); a.set_ylim(0, 2.4)
    head(a, 'the outer edge always slips first')

    b = panel(fig, [.70, .12, .28, .80], xlim=(0, 10), ylim=(0, 4.6))
    txt(b, .2, 3.80, r'$m\omega^2r\leq\mu_smg$', fontsize=8.4, color=T)
    txt(b, .2, 3.05, r'$\omega_{\max}=\sqrt{\mu_sg/r}$', fontsize=8.6, color=I)
    txt(b, .2, 2.20, 'mass cancels', fontsize=7.6, color=G)
    txt(b, .2, 1.60, 'so a coin and a', fontsize=7.6, color=G)
    txt(b, .2, 1.25, 'brick slip together', fontsize=7.6, color=G)
    txt(b, .2, .55, 'if placed at the same r', fontsize=7.6, color=G)
    return 'Without a string, friction alone must supply m omega squared r, so the limit is independent of mass'


def _atwood_incline(fig):
    a = panel(fig, [.02, .06, .52, .90], xlim=(0, 8.6), ylim=(0, 5.8), equal=True)
    th = 30.0
    ux, uy = np.cos(np.radians(th)), np.sin(np.radians(th))
    x0, y0, L = .70, .80, 4.90
    a.add_patch(Polygon([(x0, y0), (x0 + L, y0), (x0 + L, y0 + L * np.tan(np.radians(th)))],
                        closed=True, fc='#f2f6f5', ec=I, lw=1.8))
    a.plot([x0, x0 + L], [y0, y0 + L * np.tan(np.radians(th))], color=I, lw=2.0)
    top = (x0 + L, y0 + L * np.tan(np.radians(th)))
    a.add_patch(Circle(top, .22, fc='white', ec=I, lw=1.4, zorder=5))
    t = 2.60
    P = (x0 + t * ux, y0 + t * uy)
    bw, bh = 1.00, .52
    nx, ny = -uy, ux
    corners = [(P[0] + du * ux + dn * nx, P[1] + du * uy + dn * ny)
               for du, dn in ((-bw / 2, 0), (bw / 2, 0), (bw / 2, bh), (-bw / 2, bh))]
    a.add_patch(Polygon(corners, closed=True, fc='#fdf0bd', ec=GOLD, lw=1.5, zorder=4))
    a.text(P[0] - .05, P[1] + .70, r'$m_1$', fontsize=8.8, color=GOLD, ha='center')
    a.plot([P[0] + .50 * ux, top[0]], [P[1] + .52 * uy, top[1] - .20], color=I, lw=1.3)
    a.plot([top[0] + .10, top[0] + .10], [top[1] - .22, 2.30], color=I, lw=1.3)
    block(a, top[0] + .10, 2.05, .78, .58, '#f6dedb', R)
    a.text(top[0] + .55, 1.90, r'$m_2$', fontsize=8.8, color=R)
    a.text(x0 + .10, .42, r'rough ramp, friction $\mu$', fontsize=7.4, color=G)
    a.text(x0 + .10, 5.44, 'one mass on the ramp, one hanging', fontsize=7.6, color=T)

    b = panel(fig, [.60, .18, .36, .68])
    axes2(b, r'mass ratio  $m_2/m_1$', r'acceleration  (m/s$^2$)')
    sn, cs, mu = np.sin(np.radians(30)), np.cos(np.radians(30)), .25
    r = np.linspace(.05, 3, 600)
    up = 9.8 * (r - sn + mu * cs) / (r + 1)
    down = 9.8 * (r - sn - mu * cs) / (r + 1)
    b.plot(r, up, color=G, lw=1.6, ls=(0, (4, 3)))
    b.plot(r, down, color=T, lw=2.3)
    b.axhline(0, color=HG, lw=.9)
    b.fill_between(r, down, up, color='#fdf0bd', alpha=.6)
    b.text(1.62, 2.55, 'm1 runs up the ramp', fontsize=7.2, color=R)
    b.text(.42, -2.75, 'm1 runs down the ramp', fontsize=7.2, color=T)
    b.text(.16, .62, 'static band', fontsize=7.2, color=GOLD)
    b.set_xlim(0, 3); b.set_ylim(-4.2, 4.2)
    head(b, 'three regimes, one formula')
    return 'Add friction to the Atwood-on-a-ramp and the acceleration crosses zero at two different mass ratios'


# ================================================== PART I, SECOND BATCH
def _energy_shortcut(fig):
    a = panel(fig, [.04, .10, .48, .84], xlim=(0, 10), ylim=(0, 5.4), equal=True)
    C = (4.9, 2.60)
    R_ = 1.75
    a.add_patch(Circle(C, R_, fc='none', ec=I, lw=1.8))
    a.plot([C[0], C[0]], [C[1] + R_, C[1] - R_], color=HG, lw=1.0, ls=(0, (4, 3)))
    for phi, lab, off in ((0, r'$v_0$', (0, -.48)), (90, r'$v$', (.30, -.10)),
                          (180, r'$v_{\mathrm{top}}$', (.30, .10))):
        x = C[0] + R_ * np.sin(np.radians(phi))
        y = C[1] - R_ * np.cos(np.radians(phi))
        a.add_patch(Circle((x, y), .20, fc='#fdf0bd', ec=GOLD, lw=1.2, zorder=4))
        a.text(x + off[0], y + off[1], lab, fontsize=8.6, color=R)
    a.add_patch(Arc(C, 1.15, 1.15, theta1=270, theta2=320, color=I, lw=1.0))
    a.text(C[0] + .42, C[1] - .92, r'$\theta$', fontsize=8.2, color=I)
    a.text(.35, 4.95, r'energy gives $v(\theta)$, the radial equation gives $T$', fontsize=7.6, color=T)
    a.text(.35, .28, r'$v^2(\theta)=v_0^2-2gR(1+\cos\theta)$', fontsize=8.4, color=I)

    b = panel(fig, [.56, .18, .40, .68])
    axes2(b, r'angle from the bottom  $\theta$  (degrees)', r'speed  $v/\sqrt{gR}$')
    th = np.linspace(0, 180, 300)
    for k, c in ((3.0, R), (2.2, T), (1.6, G)):
        v2 = k ** 2 - 2 * (1 + np.cos(np.radians(th)))
        b.plot(th, np.sqrt(np.clip(v2, 0, None)), color=c, lw=2.0)
        b.text(6, np.sqrt(max(v2[0], .01)) + .06, r'$v_0=%.1f$' % k, fontsize=7.0, color=c)
    b.axhline(1.0, color=HG, lw=.9, ls=(0, (3, 3)))
    b.text(6, 1.10, r'taut limit $v=\sqrt{gR}$', fontsize=7.0, color=G)
    b.set_xlim(0, 180); b.set_ylim(0, 3.2)
    b.set_xticks([0, 60, 120, 180])
    head(b, 'slower launch, shorter arc')
    return 'Energy gives the speed at every angle in one line, and the radial equation does the rest'


def _rough_table_pulley(fig):
    a = panel(fig, [.02, .10, .52, .84], xlim=(0, 8.4), ylim=(0, 5.4), equal=True)
    a.add_patch(Rectangle((.55, 1.55), 4.60, .24, fc='#f2f6f5', ec=I, lw=1.4))
    block(a, 2.10, 2.05, 1.55, .78, '#fdf0bd', GOLD)
    a.add_patch(Circle((5.35, 2.05), .20, fc='white', ec=I, lw=1.4, zorder=5))
    a.plot([2.90, 5.35], [2.05, 2.05], color=I, lw=1.3)
    a.plot([5.55, 5.55], [2.05, 1.05], color=I, lw=1.3)
    block(a, 5.55, .80, .62, .50, '#f6dedb', R)
    a.text(5.95, .62, r'$M$', fontsize=8.6, color=R)
    a.text(1.45, 2.55, r'$m$', fontsize=8.8, color=GOLD)
    arrow(a, (3.05, 2.42), (4.10, 2.42), G, 1.5)
    a.text(3.12, 2.60, r'$T$', fontsize=8.4, color=G)
    arrow(a, (1.20, 1.72), (.30, 1.72), R, 1.6)
    a.text(.60, 1.90, r'$f=\mu_kN$', fontsize=8.0, color=R)
    a.text(.55, .75, 'rough table, hanging mass', fontsize=7.4, color=G)
    head(a, 'one string, two different jobs')

    b = panel(fig, [.60, .20, .36, .66])
    axes2(b, r'friction coefficient  $\mu$', r'acceleration  (m/s$^2$)')
    mu = np.linspace(0, .8, 300)
    for M, c, lab in ((2.0, T, 'M = 2 kg'), (3.0, GOLD, 'M = 3 kg')):
        b.plot(mu, 9.8 * (M - mu * 3.0) / (3.0 + M), color=c, lw=2.0, label=lab)
    b.axhline(0, color=HG, lw=.9)
    b.legend(frameon=False, fontsize=7.2, loc='upper right')
    b.set_xlim(0, .8)
    head(b, 'm = 3 kg on the table')
    return 'On the table friction is the brake, on the string it is the drive: separate books'


def _accelerating_incline(fig):
    a = panel(fig, [.02, .10, .52, .84], xlim=(0, 8.4), ylim=(0, 5.4), equal=True)
    th = 30.0
    ux, uy = np.cos(np.radians(th)), np.sin(np.radians(th))
    x0, y0, L = .70, .80, 5.10
    a.add_patch(Polygon([(x0, y0), (x0 + L, y0), (x0 + L, y0 + L * np.tan(np.radians(th)))],
                        closed=True, fc='#f2f6f5', ec=I, lw=1.8))
    a.plot([x0 - .35, x0 + L + .45], [y0, y0], color=I, lw=1.4)
    t = 2.35
    P = (x0 + t * ux, y0 + t * uy)
    bw, bh = 1.00, .52
    nx, ny = -uy, ux
    corners = [(P[0] + du * ux + dn * nx, P[1] + du * uy + dn * ny)
               for du, dn in ((-bw / 2, 0), (bw / 2, 0), (bw / 2, bh), (-bw / 2, bh))]
    a.add_patch(Polygon(corners, closed=True, fc='#fdf0bd', ec=GOLD, lw=1.5, zorder=4))
    arrow(a, (x0 + .40, .30), (4.40, .30), T, 1.7)
    a.text(4.52, .14, r'$a_0$', fontsize=8.6, color=T)
    C = (P[0], P[1] + .26 * ny)
    arrow(a, C, (C[0] + 1.45 * nx, C[1] + 1.45 * ny), T, 1.8)
    a.text(C[0] + 1.60 * nx, C[1] + 1.60 * ny, r'$N$', fontsize=8.6, color=T)
    arrow(a, C, (C[0] - 1.45 * ux, C[1] - 1.45 * uy), R, 1.5)
    a.text(C[0] - 1.62 * ux, C[1] - 1.62 * uy, r'$mg$', fontsize=8.4, color=R, ha='right')
    a.text(x0 + .10, 4.94, 'the ramp itself is accelerating', fontsize=7.6, color=G)

    b = panel(fig, [.58, .18, .38, .68])
    axes2(b, r'ramp acceleration  $a_0/g$', r'normal force  $N/mg$')
    x = np.linspace(0, 2.0, 300)
    b.plot(x, np.cos(np.radians(30)) + x * np.sin(np.radians(30)), color=T, lw=2.2)
    b.plot([0, 2.0], [np.cos(np.radians(30))] * 2, color=HG, lw=1.0, ls=(0, (4, 3)))
    b.plot([np.tan(np.radians(30))], [np.cos(np.radians(30)) + np.tan(np.radians(30)) * np.sin(np.radians(30))],
           'o', ms=5.5, color=R, zorder=5)
    b.annotate(r'$a_0=g\tan\theta$: block rides along', xy=(.577, 1.155), xytext=(.66, .55),
               fontsize=7.2, color=R, arrowprops=dict(arrowstyle='->', color=R, lw=.8))
    b.text(.05, 1.35, r'$N=mg(\cos\theta+\frac{a_0}{g}\sin\theta)$', fontsize=8.0, color=I)
    b.set_xlim(0, 2.0); b.set_ylim(.4, 1.7)
    head(b, 'accelerating the ramp loads the block')
    return 'Push the ramp into the block and N rises; the block rides at rest when a0 = g tan(theta)'


def _measure_mu(fig):
    a = panel(fig, [.02, .10, .31, .84], xlim=(0, 4.4), ylim=(0, 5.4), equal=True)
    th = 26.0
    a.add_patch(Polygon([(.35, 1.00), (3.95, 1.00), (3.95, 1.00 + 3.60 * np.tan(np.radians(th)))],
                        closed=True, fc='#f2f6f5', ec=I, lw=1.6))
    ux, uy = np.cos(np.radians(th)), np.sin(np.radians(th))
    P = (.35 + 2.05 * ux, 1.00 + 2.05 * uy)
    nx, ny = -uy, ux
    corners = [(P[0] + du * ux + dn * nx, P[1] + du * uy + dn * ny)
               for du, dn in ((-.45, 0), (.45, 0), (.45, .32), (-.45, .32))]
    a.add_patch(Polygon(corners, closed=True, fc='#fdf0bd', ec=GOLD, lw=1.4))
    a.add_patch(Arc((.35, 1.00), 1.3, 1.3, theta1=0, theta2=th, color=I, lw=1.0))
    a.text(.95, 1.10, r'$\theta_s$', fontsize=8.2, color=I)
    a.text(.35, .42, 'tilt until it slides', fontsize=7.2, color=G)
    a.text(.35, 4.95, r'$\mu_s=\tan\theta_s$', fontsize=9.0, color=T)

    b = panel(fig, [.35, .10, .31, .84], xlim=(0, 4.4), ylim=(0, 5.4), equal=True)
    b.add_patch(Rectangle((.30, 1.00), 3.90, .22, fc='#f2f6f5', ec=I, lw=1.4))
    block(b, 1.40, 1.55, .95, .55, '#fdf0bd', GOLD)
    arrow(b, (1.95, 1.72), (3.10, 1.72), T, 1.6)
    b.text(3.20, 1.58, r'$v$', fontsize=8.4, color=T)
    b.plot([1.90, 3.65], [1.42, 1.42], color=R, lw=1.6, ls=(0, (4, 3)))
    b.text(2.35, 1.52, 'stopping distance d', fontsize=7.2, color=R)
    b.text(.30, 4.95, r'$\mu_k=v^2/(2gd)$', fontsize=9.0, color=T)
    b.text(.30, .42, 'brake and measure d', fontsize=7.2, color=G)

    c = panel(fig, [.68, .10, .30, .84], xlim=(0, 4.4), ylim=(0, 5.4), equal=True)
    c.add_patch(Rectangle((.30, 1.00), 3.90, .22, fc='#f2f6f5', ec=I, lw=1.4))
    block(c, 1.55, 1.55, 1.05, .55, '#fdf0bd', GOLD)
    arrow(c, (2.15, 1.62), (3.35, 1.62), T, 1.6)
    c.text(2.28, 1.80, r'$F$', fontsize=8.4, color=T)
    c.text(.36, 1.42, r'$f_k$', fontsize=8.2, color=R)
    arrow(c, (1.20, 1.30), (.38, 1.30), R, 1.4)
    c.text(.30, 4.95, r'$F=\mu_kmg$ at steady v', fontsize=8.4, color=T)
    c.text(.30, .42, 'drag at constant speed', fontsize=7.2, color=G)
    return 'Three independent measurements of one number: tilt, brake, drag'


def _chain_table(fig):
    a = panel(fig, [.02, .10, .50, .84], xlim=(0, 8.6), ylim=(0, 5.4), equal=True)
    a.add_patch(Rectangle((.50, 2.55), 3.85, .22, fc='#f2f6f5', ec=I, lw=1.4))
    a.plot([4.35, 4.35], [2.55, .70], color=I, lw=1.6)
    a.plot([3.30, 4.32], [2.86, 2.86], color=GOLD, lw=3.2, solid_capstyle='butt')
    a.plot([4.45, 4.45], [2.86, 1.35], color=GOLD, lw=3.2, solid_capstyle='butt')
    a.plot([.50, 3.30], [2.86, 2.86], color=GOLD, lw=1.2, ls=(0, (3, 2)))
    a.plot([.50, 3.30], [2.55, 2.55], color=GOLD, lw=1.2, ls=(0, (3, 2)))
    dimx(a, .55, 3.28, 2.20, 'sliding part', G, 7.2)
    dimy(a, 5.35, 1.35, 2.86, r'$x$', 'right', T, 8.6)
    a.text(4.62, 1.58, 'hanging', fontsize=7.2, color=GOLD)
    a.text(.50, .30, r'$a=\frac{gx}{L}$', fontsize=9.6, color=I)
    head(a, 'as x grows, the drive grows')

    b = panel(fig, [.56, .20, .40, .66])
    axes2(b, r'fraction over the edge  $x/L$', r'acceleration  $a/g$')
    x = np.linspace(0, 1, 300)
    b.plot(x, x, color=T, lw=2.2)
    b.fill_between(x, 0, x, color='#fdf0bd', alpha=.5)
    b.plot([1], [1], 'o', ms=5.5, color=R, zorder=5)
    b.text(.52, .30, r'$a=gx/L$', fontsize=9.0, color=I)
    b.annotate('free fall at x = L', xy=(1, 1), xytext=(.30, .84), fontsize=7.2, color=R,
               arrowprops=dict(arrowstyle='->', color=R, lw=.8))
    b.set_xlim(0, 1.05); b.set_ylim(0, 1.15)
    head(b, 'a linear ramp, not a constant')
    return 'The hanging weight grows while the sliding mass stays the same, so the acceleration grows with x'


def _wedge_carry(fig):
    a = panel(fig, [.02, .10, .52, .84], xlim=(0, 8.4), ylim=(0, 5.4), equal=True)
    th = 30.0
    ux, uy = np.cos(np.radians(th)), np.sin(np.radians(th))
    x0, y0, L = .70, .80, 5.10
    a.add_patch(Polygon([(x0, y0), (x0 + L, y0), (x0 + L, y0 + L * np.tan(np.radians(th)))],
                        closed=True, fc='#f2f6f5', ec=I, lw=1.8))
    a.plot([x0 - .35, x0 + L + .45], [y0, y0], color=I, lw=1.4)
    t = 2.55
    P = (x0 + t * ux, y0 + t * uy)
    bw, bh = 1.00, .52
    nx, ny = -uy, ux
    corners = [(P[0] + du * ux + dn * nx, P[1] + du * uy + dn * ny)
               for du, dn in ((-bw / 2, 0), (bw / 2, 0), (bw / 2, bh), (-bw / 2, bh))]
    a.add_patch(Polygon(corners, closed=True, fc='#fdf0bd', ec=GOLD, lw=1.5, zorder=4))
    arrow(a, (x0 + .40, .28), (4.50, .28), T, 1.8)
    a.text(4.62, .12, r'$a_0=g\tan\theta$', fontsize=8.6, color=T)
    C = (P[0], P[1] + .26 * ny)
    arrow(a, C, (C[0] + 1.35 * nx, C[1] + 1.35 * ny), G, 1.7)
    a.text(C[0] + 1.52 * nx, C[1] + 1.52 * ny, r'$N$', fontsize=8.6, color=G)
    arrow(a, C, (C[0], C[1] - 1.25), R, 1.6)
    a.text(C[0] + .14, C[1] - 1.24, r'$mg$', fontsize=8.4, color=R)
    dashed(a, C, (C[0] - 1.20, C[1]))
    a.text(P[0] + .10, P[1] + .78, 'at rest on the ramp', fontsize=7.4, color=T)

    b = panel(fig, [.58, .18, .38, .68])
    axes2(b, r'ramp acceleration  $a_0/g$', r'net force along the face  $/mg$')
    x = np.linspace(0, 1.6, 300)
    b.plot(x, np.sin(np.radians(30)) - x * np.cos(np.radians(30)), color=T, lw=2.2)
    b.axhline(0, color=HG, lw=.9)
    b.axvline(np.tan(np.radians(30)), color=R, lw=1.0, ls=(0, (3, 3)))
    b.plot([np.tan(np.radians(30))], [0], 'o', ms=5.5, color=R, zorder=5)
    b.text(1.06, .16, 'rides along', fontsize=7.2, color=R)
    b.text(.05, .30, 'slides down', fontsize=7.2, color=G)
    b.text(.30, -.34, 'slides up', fontsize=7.2, color=T)
    b.set_xlim(0, 1.6); b.set_ylim(-.55, .55)
    head(b, 'the residual slides the block one way or the other')
    return 'At a0 = g tan(theta) the pseudo force exactly replaces the downhill pull of gravity'


def _slack_angle(fig):
    a = panel(fig, [.02, .06, .54, .90], xlim=(0, 7.6), ylim=(0, 5.6), equal=True)
    C = (3.55, 2.75)
    R_ = 2.05
    a.add_patch(Circle(C, R_, fc='none', ec=HG, lw=1.4, ls=(0, (3, 3))))
    a.plot([C[0], C[0]], [C[1], C[1] - R_], color=I, lw=1.5)
    th = 115
    a.add_patch(Arc(C, 1.55, 1.55, theta1=270, theta2=270 + th, color=I, lw=1.1))
    a.text(C[0] + .72 * np.sin(np.radians(40)), C[1] - .72 * np.cos(np.radians(40)),
           r'$\theta_0$', fontsize=8.8, color=I)
    x = C[0] + R_ * np.sin(np.radians(th))
    y = C[1] - R_ * np.cos(np.radians(th))
    a.plot([C[0], x], [C[1], y], color=I, lw=1.3, ls=(0, (3, 2)))
    a.add_patch(Circle((x, y), .22, fc='#f6dedb', ec=R, lw=1.3, zorder=5))
    a.plot([C[0] - .16, C[0] + .16], [C[1], C[1]], color=I, lw=1.0)
    arrow(a, (x, y), (x + 1.25, y + .70), T, 1.4)
    a.text(x + 1.05, y + .95, r'$v$', fontsize=8.4, color=T)
    a.annotate('T = 0 here', xy=(x, y), xytext=(x - 2.25, y + 1.05), fontsize=7.6,
               color=R, arrowprops=dict(arrowstyle='->', color=R, lw=.9))
    a.annotate(r'launch $v_0$', xy=(C[0] - .06, C[1] - R_), xytext=(1.55, .18),
               fontsize=7.6, color=G, arrowprops=dict(arrowstyle='->', color=G, lw=.9))
    a.text(.25, 5.30, 'the string cannot push, so it lets go', fontsize=7.8, color=T)

    b = panel(fig, [.60, .18, .36, .68])
    axes2(b, r'launch speed  $v_0/\sqrt{gR}$', r'slack angle  $\theta_0$  (degrees)')
    v = np.linspace(0, np.sqrt(5), 300)
    c = v ** 2 / 3 - 2 / 3
    th = np.degrees(np.arccos(np.clip(c, -1, 1)))
    b.plot(v, th, color=T, lw=2.2)
    b.axvline(np.sqrt(5), color=R, lw=1.0, ls=(0, (3, 3)))
    b.text(1.30, 42, r'$v_0=\sqrt{5gR}$', fontsize=7.2, color=R)
    b.text(.20, 122, 'slackens', fontsize=7.2, color=T)
    b.set_xlim(0, 2.6); b.set_ylim(0, 190)
    head(b, 'lower launch, earlier slack')
    return 'The slack angle is where T reaches zero, and it approaches 131 degrees as the launch gets slow'


def _bounce_series(fig):
    a = panel(fig, [.03, .08, .50, .86], xlim=(0, 8.6), ylim=(0, 5.2), equal=True)
    a.plot([.30, 8.30], [.55, .55], color=I, lw=1.8)
    x0, y0 = .55, 4.55
    a.add_patch(Circle((x0, y0), .15, fc='#fdf0bd', ec=GOLD, lw=1.1))
    hs = 4.00
    x = x0
    a.plot([x, x + .35], [y0, .55], color=T, lw=1.4)
    x += .35
    yprev = .55
    for i in range(5):
        h = hs * (0.64 ** i)
        seg = .55 + 1.05 * np.sqrt(h / hs)
        xs = np.linspace(0, 1, 40)
        a.plot(x + xs * seg, .55 + h * 4 * xs * (1 - xs), color=T, lw=1.4)
        if i < 4:
            a.plot([x + seg, x + seg + .10], [.55, .55], color=HG, lw=.8, ls=(0, (2, 2)))
        x += seg + .10
    a.text(.32, 4.95, r'height after bounce $i$:  $e^{2i}h$', fontsize=7.8, color=T)
    a.text(.32, .22, 'distance and time are both geometric series', fontsize=7.2, color=G)

    b = panel(fig, [.58, .20, .38, .66])
    axes2(b, r'restitution  $e$', r'multiple of the first drop')
    e = np.linspace(0, .96, 300)
    b.plot(e, (1 + e ** 2) / (1 - e ** 2), color=T, lw=2.2, label='total distance / h')
    b.plot(e, (1 + e) / (1 - e), color=GOLD, lw=2.0, label='total time / t0')
    b.legend(frameon=False, fontsize=7.2, loc='upper left')
    b.set_xlim(0, .96); b.set_ylim(0, 20)
    head(b, 'both blow up as e approaches 1')
    return 'A bouncing ball is an infinite series with a finite sum: both distance and time close up in e'

def _wedge_momentum(fig):
    a = panel(fig, [.04, .52, .92, .42], xlim=(0, 10), ylim=(0, 3.4))
    a.plot([.40, 9.60], [.40, .40], color=I, lw=1.8)
    tri = [(3.05, .40), (7.05, .40), (7.05, 2.98)]
    a.add_patch(Polygon(tri, closed=True, fc='#eef3f2', ec=I, lw=1.5))
    ang = np.degrees(np.arctan2(2.98 - .40, 7.05 - 3.05))
    px, py, w, h = 4.55, .40 + (4.55 - 3.05) * (2.58 / 4.00), .86, .40
    t = np.radians(ang); c, sn = np.cos(t), np.sin(t)
    rot = [(px + qx * c - qy * sn, py + qx * sn + qy * c)
           for qx, qy in [(0, 0), (w, 0), (w, h), (0, h)]]
    a.add_patch(Polygon(rot, closed=True, fc='#fdf0bd', ec=GOLD, lw=1.4, zorder=4))
    arrow(a, (px + .30 * c, py + .30 * sn), (px - .95, py - .62), T, 1.6)
    a.text(px - 1.28, py - .95, r'$v_{\mathrm{rel}}$', fontsize=8.0, color=T)
    arrow(a, (7.20, .18), (8.55, .18), R, 1.6)
    a.text(7.24, -.10, r'$v_w$', fontsize=8.0, color=R)
    a.plot([px, px], [py, .40], color=G, lw=.9, ls=(0, (2, 2)))
    a.text(.45, 3.12, r'$m\,v_{bx}+M\,v_w=0$ at every instant', fontsize=8.4, color=I)

    b = panel(fig, [.12, .16, .43, .24])
    axes2(b, '', 'momentum')
    b.bar([0, 1, 2], [0.24, -0.24, 0.0], color=[GOLD, T, G], width=.52)
    b.set_ylim(-.38, .38); b.set_yticks([-.3, -.15, 0, .15, .3])
    b.set_xlim(-.62, 2.62)
    b.set_xticks([0, 1, 2]); b.set_xticklabels(['block', 'wedge', 'total'], fontsize=7.2)
    b.axhline(0, color=I, lw=.8)
    head(b, 'the pair is isolated horizontally', color=T)
    c = panel(fig, [.60, .16, .36, .24], xlim=(0, 3.2), ylim=(0, 1.6))
    c.axis('off')
    txt(c, .10, 1.15, 'the table force is vertical', color=G, fontsize=7.6)
    txt(c, .10, .74, 'so only the horizontal', color=G, fontsize=7.6)
    txt(c, .10, .33, 'component is conserved', color=G, fontsize=7.6)
    return 'No external horizontal force means the recoil is exactly the block horizontal momentum, reversed'


def _stage_split(fig):
    a = panel(fig, [.10, .20, .52, .66])
    axes2(a, r'fraction of fuel in stage 1', r'ideal  $\Delta v$  (km/s)')
    f = np.linspace(.02, .98, 300)
    dv = 2.0 * (np.log(1000.0 / (1000.0 - 800.0 * f)) + np.log((950.0 - 800.0 * f) / 150.0))
    a.plot(f, dv, color=T, lw=2.3)
    a.plot([.50], [3.620], 'o', ms=6.0, color=R, zorder=5)
    a.annotate('equal split  3.62', xy=(.50, 3.620), xytext=(.56, 3.520), fontsize=7.4,
               color=R, arrowprops=dict(arrowstyle='->', color=R, lw=.8))
    a.axhline(3.219, color=G, lw=1.1, ls=(0, (3, 3)))
    a.text(.62, 3.245, 'all fuel in stage 1  3.22', fontsize=7.2, color=G)
    a.set_xlim(0, 1); a.set_ylim(3.10, 3.80)
    head(a, 'less fuel in stage one is better, all the way')

    b = panel(fig, [.68, .12, .30, .76], xlim=(0, 10), ylim=(0, 4.6))
    b.axis('off')
    txt(b, .2, 4.00, 'this model', color=T, fontsize=8.2)
    txt(b, .2, 3.55, '50 kg dry each', color=G, fontsize=7.4)
    txt(b, .2, 2.95, 'little fuel first', color=T, fontsize=8.0)
    txt(b, .2, 2.55, '3.69 km/s', color=I, fontsize=8.6)
    txt(b, .2, 1.85, 'single stage', color=G, fontsize=8.0)
    txt(b, .2, 1.45, '3.22 km/s', color=I, fontsize=8.6)
    txt(b, .2, .70, 'an interior optimum', color=G, fontsize=7.2)
    txt(b, .2, .32, 'needs heavier stage one', color=G, fontsize=7.2)
    return 'In this ideal model less fuel in stage one is always better: the gain is the dropped dry mass'

def _limits_model(fig):
    a = panel(fig, [.03, .10, .52, .82], xlim=(0, 10), ylim=(0, 5.0))
    a.axis('off')
    a.add_patch(Rectangle((.40, .55), 9.10, 3.55, fc='#fdf6e3', ec='#e0cd93', lw=1.6))
    a.text(4.95, 3.78, 'Newtonian mechanics: exact here', fontsize=9.0, color=GOLD, ha='center')
    a.text(1.85, 3.00, 'slow', fontsize=8.2, color=G, ha='center')
    a.text(4.95, 3.00, 'macroscopic', fontsize=8.2, color=G, ha='center')
    a.text(8.05, 3.00, 'weak gravity', fontsize=8.2, color=G, ha='center')
    arrow(a, (4.20, 1.95), (2.30, 1.95), T, 1.7)
    a.text(2.25, 2.28, r'$v\to c$', fontsize=8.6, color=T, ha='center')
    arrow(a, (5.70, 1.95), (7.60, 1.95), R, 1.7)
    a.text(7.55, 2.28, r'$S\to\hbar$', fontsize=8.6, color=R, ha='center')
    arrow(a, (4.95, 2.55), (4.95, 1.15), G, 1.7)
    a.text(5.20, 1.55, r'$\Phi/c^{2}\to1$', fontsize=8.6, color=G)
    a.text(.40, 4.45, 'the fence is a specification, not a failure', fontsize=8.0, color=T)

    b = panel(fig, [.57, .10, .42, .80], xlim=(0, 10), ylim=(0, 5.0))
    b.axis('off')
    txt(b, .10, 4.45, 'what replaces it', color=T, fontsize=8.2)
    entries = [(T, r'$v\to c$', 'special relativity', 'clocks, lengths, $E=mc^{2}$'),
               (R, r'$S\to\hbar$', 'quantum mechanics', 'action in units of $\hbar$'),
               (G, r'$\Phi/c^{2}\to1$', 'general relativity', 'gravity is geometry')]
    y = 4.05
    for col, sym, name, note in entries:
        txt(b, .10, y, sym, color=col, fontsize=8.4)
        txt(b, .10, y - .55, name, color=I, fontsize=7.8)
        txt(b, .10, y - 1.00, note, color=G, fontsize=7.0)
        y -= 1.35
    return 'Newton is exact inside a fence, and knowing where the fence is is what makes the model honest'

def _rolling_contact(fig):
    a = panel(fig, [.04, .10, .44, .84], xlim=(0, 5.6), ylim=(0, 5.4), equal=True)
    C = (2.80, 2.90)
    R_ = 1.55
    a.add_patch(Circle(C, R_, fc='#f2f6f5', ec=I, lw=1.8))
    a.add_patch(Circle(C, .10, fc=I, ec=I))
    a.plot([C[0], C[0]], [C[1], C[1] - R_], color=HG, lw=1.0, ls=(0, (3, 2)))
    a.plot([C[0], C[0] + R_], [C[1], C[1]], color=HG, lw=1.0, ls=(0, (3, 2)))
    a.add_patch(Circle((C[0], C[1] - R_), .10, fc=R, ec=R, zorder=6))
    a.text(C[0] + .14, C[1] - R_ - .34, r'$v_p=0$', fontsize=8.0, color=R)
    arrow(a, (C[0] + .25, C[1] + 1.05), (C[0] + 1.45, C[1] + 1.05), T, 1.5)
    a.text(C[0] + 1.55, C[1] + .92, r'$v_{cm}$', fontsize=8.2, color=T)
    a.add_patch(Arc(C, 1.4, 1.4, theta1=20, theta2=110, color=GOLD, lw=1.4))
    a.text(C[0] + .55, C[1] + .58, r'$\omega$', fontsize=8.4, color=GOLD)
    a.text(.30, .35, r'$v_{cm}=\omega R$', fontsize=9.0, color=I)
    head(a, 'the contact point is instantaneously at rest')

    b = panel(fig, [.54, .18, .42, .68])
    axes2(b, r'drive force  $F$  (arb. units)', r'friction at contact')
    F = np.linspace(0, 10, 300)
    b.plot(F, .22 * F, color=T, lw=2.2)
    b.plot([10 * .45], [.22 * 4.5], 'o', ms=5.5, color=R, zorder=5)
    b.annotate(r'limits at $\mu_sN$', xy=(4.5, .99), xytext=(.55, 1.35),
               fontsize=7.4, color=R, arrowprops=dict(arrowstyle='->', color=R, lw=.8))
    b.text(5.6, .38, 'then it slips', fontsize=7.4, color=G)
    b.set_xlim(0, 10); b.set_ylim(0, 1.7)
    head(b, 'rolling uses static friction')
    return 'A rolling wheel does not slide, so the friction at the contact is static and the contact point is at rest'


def _four_shortcuts(fig):
    a = panel(fig, [.03, .52, .44, .42], xlim=(0, 5.0), ylim=(0, 2.4))
    a.axis('off')
    txt(a, .10, 1.95, '1  system equation', color=T, fontsize=8.8)
    txt(a, .10, 1.35, r'$\sum F_{\mathrm{ext}}=Ma_{\mathrm{cm}}$', color=I, fontsize=9.4)
    txt(a, .10, .62, 'a always, internal forces never', color=G, fontsize=7.2)

    b = panel(fig, [.52, .52, .45, .42], xlim=(0, 5.0), ylim=(0, 2.4))
    b.axis('off')
    txt(b, .10, 1.95, '2  differentiate the constraint', color=T, fontsize=8.8)
    txt(b, .10, 1.35, 'length → velocity → acceleration', color=I, fontsize=8.4)
    txt(b, .10, .62, 'never guess the ratio', color=G, fontsize=7.2)

    c = panel(fig, [.03, .06, .44, .40], xlim=(0, 5.0), ylim=(0, 2.4))
    c.axis('off')
    txt(c, .10, 1.95, '3  energy for the speed', color=T, fontsize=8.8)
    txt(c, .10, 1.35, r'$v^2(\theta)=v_0^2-2gR(1+\cos\theta)$', color=I, fontsize=8.2)
    txt(c, .10, .62, 'then one radial equation for T', color=G, fontsize=7.2)

    d = panel(fig, [.52, .06, .45, .40], xlim=(0, 5.0), ylim=(0, 2.4))
    d.axis('off')
    txt(d, .10, 1.95, '4  one vector of gravity', color=T, fontsize=8.8)
    txt(d, .10, 1.35, r'$g_{\mathrm{eff}}=\sqrt{g^2+a_0^2}$', color=I, fontsize=9.2)
    txt(d, .10, .62, 'then solve a static problem', color=G, fontsize=7.2)
    return 'Four shortcuts, one theme: replace a hard dynamics question with a smaller one'


def _monkey_rope(fig):
    a = panel(fig, [.02, .06, .52, .88], xlim=(0, 8.0), ylim=(0, 6.0), equal=True)
    a.plot([1.10, 6.70], [5.45, 5.45], color=I, lw=2.4)
    a.plot([3.90, 3.90], [5.45, 5.15], color=I, lw=1.4)
    a.add_patch(Circle((3.90, 4.88), .27, fc='white', ec=I, lw=1.6))
    a.plot([3.30, 3.30], [4.88, 1.55], color=GOLD, lw=1.7)
    a.plot([4.50, 4.50], [4.88, 1.55], color=GOLD, lw=1.7)
    a.add_patch(Circle((3.30, 1.30), .25, fc='#fdf0bd', ec=GOLD, lw=1.3, zorder=5))
    block(a, 4.50, 1.18, .62, .55, '#f6dedb', R)
    a.text(2.35, 1.72, 'monkey, m', fontsize=7.8, color=GOLD, ha='right')
    a.text(4.50, 1.18, 'm', fontsize=7.6, color=R, ha='center', va='center')
    a.text(4.50, .62, 'counterweight', fontsize=7.6, color=R, ha='center')
    a.annotate('', xy=(2.55, 2.25), xytext=(2.55, 1.30),
               arrowprops=dict(arrowstyle='-|>', color=T, lw=1.8))
    a.text(2.37, 2.38, r'$a$', fontsize=9.0, color=T, ha='center')
    a.annotate('', xy=(5.85, 2.25), xytext=(5.85, 1.30),
               arrowprops=dict(arrowstyle='-|>', color=T, lw=1.8))
    a.text(6.03, 2.38, r'$a$', fontsize=9.0, color=T, ha='center')
    a.plot([2.20, 6.35], [1.30, 1.30], color=HG, lw=.9, ls=(0, (3, 2)))
    a.text(1.10, 5.80, 'equal masses, one rope, one tension', fontsize=7.8, color=G)
    a.text(.55, .28, r'$T-mg=ma$ on both sides, so $a_1=a_2$', fontsize=8.2, color=I)

    b = panel(fig, [.58, .18, .38, .66])
    axes2(b, r'climb rate  $u$  (m/s)', r'common acceleration  $a$  (m/s$^2$)')
    u = np.linspace(0, 3, 300)
    b.plot(u, np.zeros_like(u), color=T, lw=2.6)
    b.plot([0], [0], 'o', ms=6, color=R, zorder=5)
    b.text(.28, .16, 'a = 0 for every climb rate', fontsize=7.6, color=T)
    b.set_xlim(0, 3); b.set_ylim(-.6, .6)
    head(b, 'they rise together, whatever the monkey does')
    return 'Equal masses on one rope accelerate together: the monkey cannot outclimb its own counterweight'

def figure(ax, key):
    fig = ax.figure
    ax.axis('off')
    build = {
        # Part I — JEE Main + Advanced
        'inertial_frames': _frame_choice,
        'second_law': _second_law_impulse,
        'third_law': _third_law_pairs,
        'fbd_incline': _fbd_incline,
        'apparent_weight': _apparent_weight,
        'lami': _lami_triangle,
        'friction_static': _friction_ramp,
        'friction_direction': _friction_direction,
        'stacked_blocks': _stacked_blocks,
        'min_pull': _min_pull,
        'movable_pulley': _movable_pulley,
        'wedge_constraint': _wedge_constraint,
        'pseudo_frame': _pseudo_frame,
        'centripetal_source': _centripetal_sources,
        'banked_design': _banked_design,
        'banked_band': _banked_band,
        'conical': _conical_pendulum,
        'circle_string': _vertical_circle_string,
        'circle_rod': _vertical_circle_rod,
        'system_parts': _system_vs_parts,
        # Part II — Olympiad / extensions
        'falling_chain': _falling_chain,
        'rocket_ratio': _rocket_ratio,
        'capstan': _capstan,
        'sand_belt': _sand_belt,
        'bead_hoop': _bead_hoop,
        'chain_lift': _chain_lift,
        'turntable': _turntable,
        'staging': _staging,
        'impulse_window': _impulse_window,
        'hitch_turns': _hitch_turns,
        'virtual_work': _virtual_work,
        'rope_table': _rope_table,
        'effective_g': _effective_g,
        'wedge_liftoff': _wedge_liftoff,
        'turntable_limit': _turntable_limit,
        'atwood_incline': _atwood_incline,
        'energy_shortcut': _energy_shortcut,
        'rough_table_pulley': _rough_table_pulley,
        'accelerating_incline': _accelerating_incline,
        'measure_mu': _measure_mu,
        'chain_table': _chain_table,
        'wedge_carry': _wedge_carry,
        'slack_angle': _slack_angle,
        'bounce_series': _bounce_series,
        'wedge_momentum': _wedge_momentum,
        'stage_split': _stage_split,
        'limits_model': _limits_model,
        'rolling_contact': _rolling_contact,
        'four_shortcuts': _four_shortcuts,
        'monkey_rope': _monkey_rope,
    }[key](fig)
    return build
