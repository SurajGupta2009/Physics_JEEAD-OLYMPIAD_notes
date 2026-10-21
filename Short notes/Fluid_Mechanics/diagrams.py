"""Native analytical diagrams for the fluid-mechanics short notes.

Rule of the sheet: one wide figure per page, at most two panels, at most six
labels per panel, every label placed in whitespace rather than on the drawing.
Curves follow the stated model; axes carry names and units.
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, Ellipse, Arc, Polygon, Wedge

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
    a.axis('on')
    a.spines[['top', 'right']].set_visible(False)
    a.tick_params(labelsize=7.6, length=3, pad=2)
    a.grid(alpha=.12, lw=.7)
    a.set_xlabel(xlabel, fontsize=8.2, labelpad=1)
    a.set_ylabel(ylabel, fontsize=8.2, labelpad=1)


def dimx(ax, x0, x1, y, label, color=I, fs=8.2):
    arrow(ax, (x0, y), (x1, y), color, 1.0, '<->', 6)
    ax.text((x0 + x1) / 2, y + .10, label, ha='center', fontsize=fs, color=color)


def dimy(ax, x, y0, y1, label, side='right', color=I, fs=8.2):
    arrow(ax, (x, y0), (x, y1), color, 1.0, '<->', 6)
    ax.text(x + (.14 if side == 'right' else -.14), (y0 + y1) / 2, label,
            ha='left' if side == 'right' else 'right', va='center', fontsize=fs, color=color)


def beaker(ax, x0, x1, y0, y1, lw=2.0):
    ax.plot([x0, x0], [y0, y1], color=I, lw=lw)
    ax.plot([x1, x1], [y0, y1], color=I, lw=lw)
    ax.plot([x0, x1], [y0, y0], color=I, lw=lw)


def waterpoly(ax, pts, fc=WATER, ec='none', lw=0, z=0):
    ax.add_patch(Polygon(pts, closed=True, fc=fc, ec=ec, lw=lw, zorder=z))


# --------------------------------------------------------------- 1. pressure
def _pressure_wedge(fig):
    a = panel(fig, [.02, .06, .30, .86], equal=True, xlim=(.7, 6.9), ylim=(.2, 4.4))
    ax = a
    ax.add_patch(Polygon([(1.2, .9), (5.7, .9), (5.7, 3.6)], closed=True,
                         fc='#f4f9f8', ec=I, lw=1.8))
    arrow(ax, (3.0, .9), (3.0, 1.42), R, 1.3)
    arrow(ax, (5.7, 2.15), (5.18, 2.15), R, 1.3)
    arrow(ax, (3.62, 2.20), (4.02, 1.94), R, 1.3)
    txt(ax, 2.55, 1.20, r'$p$', color=R, fontsize=9.4, ha='right')
    txt(ax, 5.10, 2.36, r'$p$', color=R, fontsize=9.4, ha='right')
    txt(ax, 4.10, 1.82, r'$p$', color=R, fontsize=9.4)
    arrow(ax, (4.45, 1.78), (4.45, 1.26), G, 1.3)
    txt(ax, 4.58, 1.50, r'$\rho g\,dV$', color=G, fontsize=8.4)
    ax.add_patch(Arc((1.2, .9), .8, .8, theta1=0, theta2=30.5, color=T, lw=1.2))
    txt(ax, 1.56, 1.02, r'$\theta$', color=T, fontsize=9.4)
    txt(ax, 2.65, 3.96, 'same p on all three faces', color=T, fontsize=8.2, ha='center')
    foot(ax, r'$\theta\to0$: no face is special')

    b = panel(fig, [.355, .20, .30, .60], xlim=(0, 12), ylim=(0, 210))
    h = np.linspace(0, 12, 200)
    b.plot(h, 101.3 + 9.8 * h, color=I, lw=2.0)
    b.plot(h, 9.8 * h, color=T, lw=2.0, ls='--')
    b.axhline(101.3, color=G, lw=.8, ls=':')
    b.plot([10.34], [202.6], 'o', ms=4, color=R)
    b.annotate(r'$10.3$ m', xy=(10.34, 202.6), xytext=(6.2, 185), fontsize=7.8, color=R,
               arrowprops=dict(arrowstyle='->', color=R, lw=.7))
    b.text(6.4, 40, 'gauge', fontsize=8.0, color=T)
    b.text(2.2, 165, 'absolute', fontsize=8.0, color=I)
    b.text(.15, 108, r'$p_0$', fontsize=8.4, color=G)
    axes2(b, r'depth $h$ (m)', r'$p$ (kPa)')
    b.set_yticks([0, 50, 100, 150, 200])
    b.set_xticks([0, 4, 8, 12])

    c = panel(fig, [.70, .08, .28, .82], xlim=(0, 10), ylim=(0, 10))
    c.axis('off')
    lines = [(8.9, r'$p$ is one number at a point', T),
             (7.4, r'$dp/dy=-\rho g$', I),
             (5.9, r'$p=p_0+\rho g h$', I),
             (4.0, r'$F=p\,A\,\hat n$', I),
             (2.5, 'gauge  =  absolute $-\\,p_0$', G),
             (1.0, 'label every pressure', G)]
    for y, s, col in lines:
        c.text(.2, y, s, fontsize=8.8, color=col)
    return 'Pressure is a scalar that grows with depth; only the area vector gives it a direction'


# --------------------------------------------------------------- 2. manometer
def _manometer_walk(fig):
    a = panel(fig, [.03, .06, .38, .86], equal=True, xlim=(.2, 9.8), ylim=(.1, 4.5))
    ax = a
    # tube walls
    lx0, lx1, rx0, rx1 = 2.0, 2.9, 6.6, 7.5
    bot0, bot1 = .55, 1.45
    for x0, x1, top in ((lx0, lx1, 3.9), (rx0, rx1, 3.9)):
        ax.plot([x0, x0], [bot0, top], color=I, lw=1.8)
        ax.plot([x1, x1], [bot0, top], color=I, lw=1.8)
    ax.plot([lx0, rx1], [bot0, bot0], color=I, lw=1.8)
    ax.plot([lx0, lx1], [3.9, 3.9], color='none')
    # mercury
    hgl, hgr = 2.4, 3.0
    ax.add_patch(Rectangle((lx0, bot1 - .9), 1, 1.0, fc=HG, ec='none', zorder=0))
    ax.add_patch(Rectangle((lx0, bot0), rx1 - lx0, bot1 - bot0 + .9, fc=HG, ec='none', zorder=0))
    ax.add_patch(Rectangle((rx0, bot1 - .9), 1, 1.0, fc=HG, ec='none', zorder=0))
    ax.add_patch(Rectangle((lx0, bot1 - .9), 1, hgl - bot1 + .9, fc=HG, ec='none', zorder=0))
    ax.add_patch(Rectangle((rx0, bot1 - .9), 1, hgr - bot1 + .9, fc=HG, ec='none', zorder=0))
    # water above left mercury
    ax.add_patch(Rectangle((lx0, hgl), 1, 3.3 - hgl, fc='#bcdcea', ec='none', zorder=0))
    # gas above right mercury, capped
    ax.add_patch(Rectangle((rx0, hgr), 1, 3.5 - hgr, fc=PALE, ec='none', zorder=0))
    ax.plot([rx0 - .5, rx1 + .5], [3.55, 3.55], color=I, lw=2.4)
    # levels
    ax.plot([1.2, 8.2], [hgl, hgl], color=R, lw=.8, ls=':')
    ax.plot([1.2, 8.2], [hgr, hgr], color=R, lw=.8, ls=':')
    txt(ax, 6.0, 4.12, r'$p_0$', fontsize=9.4, ha='center')
    txt(ax, 8.05, 4.12, 'gas', fontsize=8.4, color=I, ha='center')
    txt(ax, 1.05, 2.88, 'water', fontsize=8.0, color=G)
    txt(ax, 1.05, 1.05, 'mercury', fontsize=8.0, color=G)
    dimy(ax, 8.55, hgl, hgr, '18 cm')
    dimy(ax, 1.45, hgl, 3.3, '10 cm', side='left')
    foot(ax, r'$p_{gas}=p_0+\rho_w g(0.10)-\rho_{Hg}g(0.18)$')

    b = panel(fig, [.42, .06, .26, .86], equal=True, xlim=(0, 6.2), ylim=(.1, 4.5))
    bx = b
    bx.add_patch(Rectangle((.5, .6), 1.5, 1.5, fc=WATER, ec=I, lw=1.6))
    bx.add_patch(Rectangle((.75, 1.0), .95, .25, fc=HG, ec=I, lw=1.1))
    bx.plot([1.25, 1.25], [1.85, 2.55], color=I, lw=2.2)
    bx.plot([1.25, 1.25], [.35, .6], color=I, lw=2.2)
    arrow(bx, (1.25, 2.6), (1.25, 3.3), R, 1.5)
    txt(bx, 1.36, 3.0, r'$F_1$', fontsize=8.8, color=R)
    # connecting pipe
    bx.plot([2.0, 3.6], [.6, .6], color=I, lw=2.4)
    bx.plot([3.6, 3.6], [.6, 1.0], color=I, lw=2.4)
    bx.add_patch(Rectangle((2.8, .6), 2.6, .5, fc=WATER, ec=I, lw=1.6))
    bx.add_patch(Rectangle((2.95, 1.1), 2.3, .25, fc=HG, ec=I, lw=1.1))
    bx.add_patch(Rectangle((3.4, 1.35), 1.4, .55, fc='#e9edee', ec=I, lw=1.2))
    txt(bx, 4.1, 1.62, r'$M$', fontsize=8.8, ha='center')
    txt(bx, 3.55, .82, r'$A$', fontsize=8.4)
    txt(bx, 1.25, .42, r'$a$', fontsize=8.4, ha='center')
    txt(bx, 3.1, 3.95, r'$F_1d_1=F_2d_2$', fontsize=8.2, ha='center', color=T)
    txt(bx, 3.1, 3.50, 'force multiplied,', fontsize=7.2, ha='center', color=G)
    txt(bx, 3.1, 3.20, 'work unchanged', fontsize=7.2, ha='center', color=G)
    return 'Walk any manometer from an open end: down adds, up subtracts, horizontal costs nothing'


# ------------------------------------------------------------ 3. plane forces
def _plane_force(fig):
    a = panel(fig, [.03, .08, .32, .84], equal=True, xlim=(.2, 8.2), ylim=(.3, 4.4))
    ax = a
    ax.add_patch(Rectangle((.9, .8), 3.4, 2.6, fc=WATER, ec='none'))
    ax.plot([.9, .9], [.8, 3.4], color=I, lw=2.0)
    ax.plot([.9, 4.3], [.8, .8], color=I, lw=2.0)
    ax.plot([.9, 4.3], [3.4, 3.4], color=T, lw=1.8)
    ax.plot([4.3, 4.3], [.8, 3.4], color=I, lw=3.0)
    ax.add_patch(Polygon([(4.3, 3.4), (4.3, .8), (6.0, .8)], closed=True,
                         fc='#fbe9e7', ec=R, lw=1.0))
    arrow(ax, (6.4, 1.42), (4.7, 1.42), R, 1.8)
    txt(ax, 6.50, 1.58, r'$F=p_cA$', fontsize=8.6, color=R)
    ax.plot([4.3, 4.75], [1.67, 1.67], color=I, lw=1.5)
    dimy(ax, .62, .8, 3.4, r'$H$', side='left')
    head(ax, 'pressure grows with depth', T)
    foot(ax, 'the resultant sits below the centroid')

    b = panel(fig, [.38, .08, .30, .84], equal=True, xlim=(0, 10), ylim=(.3, 4.4))
    bx = b
    for x0, topw, lab in ((.7, 1.5, 'straight'), (3.8, 2.5, 'flared'), (7.0, .8, 'tapered')):
        basew = 1.5
        bx.add_patch(Polygon([(x0, .9), (x0 + basew, .9),
                              (x0 + basew - (basew - topw) / 2, 3.5),
                              (x0 + (basew - topw) / 2, 3.5)], closed=True,
                             fc='none', ec=I, lw=1.7))
        bx.add_patch(Polygon([(x0 + .1, .9), (x0 + basew - .1, .9),
                              (x0 + basew - .1 - (basew - topw) / 2 * .9, 3.2),
                              (x0 + .1 + (basew - topw) / 2 * .9, 3.2)], closed=True,
                             fc=WATER, ec='none', zorder=0))
        for k in range(2):
            arrow(bx, (x0 + .35 + k * .5, .9), (x0 + .35 + k * .5, .55), R, 1.3)
        txt(bx, x0 + basew / 2, .40, lab, fontsize=7.4, ha='center')
    txt(bx, 5.0, 3.95, r'same $h$, same base: same $F$', fontsize=8.0, ha='center', color=T)
    return 'Force on a plane face is the centroid pressure times the area, acting below the centroid'


# ------------------------------------------------------------ 4. curved gate
def _curved_gate(fig):
    a = panel(fig, [.02, .06, .36, .86], equal=True, xlim=(.2, 5.6), ylim=(.4, 4.4))
    ax = a
    O = (4.6, 1.0)
    Rr = 1.8
    th = np.linspace(np.pi / 2, np.pi, 90)
    arc = np.c_[O[0] + Rr * np.cos(th), O[1] + Rr * np.sin(th)]
    pts = [(.8, 1.0), (2.8, 1.0)] + [tuple(p) for p in arc[:-1]] + [(4.6, 3.4), (.8, 3.4)]
    waterpoly(ax, pts)
    ax.plot([.8, 4.6], [1.0, 1.0], color=I, lw=2.0)
    ax.plot([.8, .8], [1.0, 3.4], color=I, lw=2.0)
    ax.plot([.8, 4.6], [3.4, 3.4], color=T, lw=1.8)
    ax.add_patch(Wedge(O, Rr, 90, 180, fc='#e3ebee', ec='none', zorder=1))
    ax.plot(arc[:, 0], arc[:, 1], color=I, lw=2.4, zorder=3)
    ax.plot([2.8, 2.8], [1.0, 2.8], color=R, lw=1.0, ls='--')
    ax.plot(*O, 'o', ms=3.6, color=I, zorder=4)
    txt(ax, 4.67, .78, r'$O$', fontsize=9.4)
    dimx(ax, 2.8, 4.6, .62, r'$R$')
    arrow(ax, (1.15, 1.65), (2.80, 1.65), R, 1.8)
    txt(ax, 1.10, 1.86, r'$F_H$', fontsize=9.0, color=R)
    arrow(ax, (3.9, 3.30), (3.9, 2.68), R, 1.8)
    txt(ax, 4.00, 3.05, r'$F_V$', fontsize=9.0, color=R)
    p = (O[0] + Rr * np.cos(1.25 * np.pi), O[1] + Rr * np.sin(1.25 * np.pi))
    arrow(ax, p, O, T, 1.4)
    txt(ax, 2.55, 1.95, r'$F$', fontsize=8.8, color=T)
    head(ax, 'quarter-cylinder gate', T)
    foot(ax, 'forces on the arc are radial')

    b = panel(fig, [.41, .06, .30, .86], equal=True, xlim=(.2, 6.2), ylim=(.4, 4.4))
    bx = b
    bx.add_patch(Rectangle((2.3, .8), 2.9, 3.0, fc=WATER, ec='none'))
    bx.plot([2.3, 2.3], [.8, 3.8], color=I, lw=2.0)
    bx.plot([2.3, 5.2], [3.8, 3.8], color=T, lw=1.8)
    bx.add_patch(Wedge((2.3, 2.3), 1.2, 90, 270, fc='#e3ebee', ec=I, lw=1.8))
    bx.plot([1.1, 1.1], [1.1, 3.5], color=R, lw=1.0, ls='--')
    arrow(bx, (1.60, 2.3), (2.55, 2.3), R, 1.8)
    txt(bx, 3.35, 3.48, r'$F_H=p_c\,\pi R^2$', fontsize=8.0, color=R)
    dimy(bx, 2.70, 2.3, 3.8, r'$h_c$')
    head(bx, 'the projection is a circle', T)
    foot(bx, r'$F_V=\rho g V$ (column weight)')
    return 'Split a curved-face force: horizontal from the projection, vertical from the column weight'


# --------------------------------------------------------- 5. accelerated tank
def _accel_tank(fig):
    a = panel(fig, [.02, .06, .40, .86], equal=True, xlim=(.2, 8.1), ylim=(.3, 4.4))
    ax = a
    waterpoly(ax, [(1.0, .8), (7.0, .8), (7.0, 3.3), (1.0, 2.3)])
    beaker(ax, 1.0, 7.0, .8, 3.7)
    ax.plot([1.0, 7.0], [2.3, 3.3], color=T, lw=2.0)
    ax.plot([1.0, 7.0], [2.8, 2.8], color=G, lw=.9, ls=':')
    txt(ax, 2.0, 2.95, 'rest level', fontsize=7.8, color=G)
    ax.add_patch(Arc((4.0, 2.8), 1.4, 1.4, theta1=0, theta2=8.1, color=T, lw=1.1))
    txt(ax, 4.55, 2.86, r'$\theta$', fontsize=9.2, color=T)
    arrow(ax, (1.4, 1.25), (2.5, 1.25), T, 1.8)
    txt(ax, 1.75, 1.00, r'$a$', fontsize=9.2, color=T)
    dimy(ax, 7.35, 2.8, 3.3, r'$0.5$ m')
    head(ax, r'free surface: $\tan\theta=a/g$', T)
    foot(ax, 'until it spills, the surface pivots about mid-length')

    b = panel(fig, [.46, .06, .50, .86], equal=True, xlim=(0, 12.5), ylim=(.3, 4.4))
    bx = b
    bx.add_patch(Polygon([(1.2, 1.4), (9.8, 1.4), (9.8, 3.0), (7.6, 3.6), (3.4, 3.6), (1.2, 3.0)],
                         closed=True, fc='#f2f6f7', ec=I, lw=1.8))
    for cx in (3.0, 8.4):
        bx.add_patch(Circle((cx, 1.3), .40, fc='#e6ecee', ec=I, lw=1.5))
    bx.plot([6.0, 6.55], [1.45, 2.72], color=G, lw=1.1)
    bx.add_patch(Ellipse((6.85, 3.18), .9, 1.05, angle=30, fc='#fde2e0', ec=R, lw=1.4))
    txt(bx, 6.55, 2.42, 'balloon', fontsize=7.8, color=R)
    arrow(bx, (7.65, 3.35), (8.55, 3.35), R, 1.6)
    txt(bx, 8.10, 3.55, 'with a', fontsize=7.8, color=R, ha='center')
    bx.plot([4.5, 4.28], [3.55, 2.35], color=G, lw=1.5)
    bx.add_patch(Rectangle((4.14, 2.10), .26, .26, fc='#e6ecee', ec=I, lw=1.0))
    arrow(bx, (3.55, 2.45), (2.80, 2.45), G, 1.6)
    txt(bx, 3.20, 2.66, 'against a', fontsize=7.8, color=G, ha='center')
    arrow(bx, (1.3, .62), (2.5, .62), T, 1.8)
    txt(bx, 1.90, .38, r'$\mathbf{a}$', fontsize=9.2, color=T)
    txt(bx, 7.0, .62, r'$\mathbf{g}_{eff}=\mathbf{g}-\mathbf{a}$', fontsize=8.8, ha='center')
    head(bx, 'one vector rule, two answers', T)
    return 'Rigid acceleration is statics with g_eff: the balloon leans with a, a plumb line against it'


# --------------------------------------------------------- 6. rotating vessel
def _rotating_paraboloid(fig):
    a = panel(fig, [.02, .06, .42, .86], equal=True, xlim=(-3.3, 3.3), ylim=(.2, 4.4))
    ax = a
    Rr, z0, rise = 2.6, 1.75, .55
    r = np.linspace(-Rr, Rr, 300)
    z = z0 + rise * (r / Rr) ** 2
    waterpoly(ax, list(zip(r, z)) + [(Rr, .5), (-Rr, .5)])
    ax.plot([-Rr, -Rr], [.5, 3.7], color=I, lw=2.0)
    ax.plot([Rr, Rr], [.5, 3.7], color=I, lw=2.0)
    ax.plot([-Rr, Rr], [.5, .5], color=I, lw=2.0)
    ax.plot(r, z, color=T, lw=2.2)
    ax.plot([-Rr, Rr], [z0 + rise / 2, z0 + rise / 2], color=G, lw=.9, ls=':')
    arrow(ax, (0, 4.05), (-1.3, 4.05), G, 1.2)
    txt(ax, -.55, 4.18, r'$\omega$', fontsize=9.2, color=G)
    dimx(ax, 0, Rr, .22, r'$R$')
    dimy(ax, Rr - .30, z[0], z[-1], r'$\Delta z$', side='left')
    txt(ax, 2.85, z0 + rise / 2 + .12, 'rest', fontsize=7.2, color=G)
    head(ax, 'the free surface is a paraboloid', T)
    foot(ax, r'$z=z_0+\omega^2r^2/2g$')

    b = panel(fig, [.49, .08, .47, .82], xlim=(0, 10), ylim=(0, 10))
    b.axis('off')
    items = [(8.7, r'$z(r)=z_0+\dfrac{\omega^2r^2}{2g}$', I, 10.4),
             (6.4, r'rim rise $=\dfrac{\omega^2R^2}{2g}$', T, 8.8),
             (4.1, r'centre drop $=$ rim rise', T, 8.8),
             (2.2, r'$\omega=4$ s$^{-1}$, $R=0.30$ m', G, 8.6)]
    for y, s, col, fs in items:
        b.text(.2, y, s, fontsize=fs, color=col)
    b.text(.2, .5, r'$\Delta z=7.4$ cm, split $3.7+3.7$', fontsize=8.6, color=G)
    return 'Volume conservation splits the paraboloid: the centre falls exactly as much as the rim rises'


# --------------------------------------------------------------- 7. buoyancy
def _buoyancy(fig):
    a = panel(fig, [.02, .06, .40, .86], equal=True, xlim=(.2, 8.4), ylim=(.3, 4.4))
    ax = a
    ax.add_patch(Rectangle((.8, .7), 6.4, 3.0, fc=WATER, ec='none'))
    ax.plot([.8, 7.2], [3.7, 3.7], color=T, lw=1.6)
    ax.plot([.8, .8], [.7, 3.7], color=I, lw=2.0)
    ax.plot([7.2, 7.2], [.7, 3.7], color=I, lw=2.0)
    ax.plot([.8, 7.2], [.7, .7], color=I, lw=2.0)
    ax.add_patch(Rectangle((2.4, 1.5), 2.2, 2.45, fc='#f6e7c8', ec=I, lw=1.5))
    ax.add_patch(Rectangle((2.4, 1.5), 2.2, 2.0, fc='#ddc99d', ec='none'))
    ax.plot([2.4, 4.6], [3.5, 3.5], color=T, lw=1.4, ls='--')
    arrow(ax, (5.2, 2.55), (5.2, 1.65), G, 1.6)
    txt(ax, 5.3, 2.05, r'$mg$', fontsize=8.6, color=G)
    arrow(ax, (5.2, 1.50), (5.2, 2.40), T, 1.6)
    txt(ax, 5.3, 1.25, r'$F_b$', fontsize=8.8, color=T)
    dimy(ax, 2.15, 1.5, 3.5, r'$V_{disp}$', side='left')
    head(ax, r'$F_b=\rho_fV_{disp}g$', T)
    foot(ax, 'the displaced volume is what the fluid lost')

    b = panel(fig, [.47, .06, .48, .86], equal=True, xlim=(0, 10.6), ylim=(.3, 4.4))
    bx = b
    bx.add_patch(Rectangle((1.6, .95), 2.1, 2.7, fc='#eaf4f8', ec=I, lw=1.7))
    bx.plot([1.0, 2.6], [3.35, 3.35], color=T, lw=1.3, ls='--')
    for x in (2.0, 2.6, 3.2):
        arrow(bx, (x, 3.95), (x, 3.40), R, 1.2)
        arrow(bx, (x, .85), (x, 1.40), R, 1.2)
    txt(bx, 3.6, 1.20, r'$p_2-p_1=\rho g(h_2-h_1)$', fontsize=8.0)
    txt(bx, 3.6, 1.90, r'$F_b=(p_2-p_1)A=\rho gV$', fontsize=8.6, color=T)
    txt(bx, 3.6, 2.60, 'side forces cancel pairwise', fontsize=7.6, color=G)
    txt(bx, 2.35, 4.15, 'Archimedes, twice', fontsize=8.4, color=T, ha='center')
    dimy(bx, .95, .95, 3.35, r'$h_2$', side='left')
    return 'Buoyancy is the pressure integral over the body, equal to the weight of displaced fluid'


# --------------------------------------------------------------- 8. stability
def _stability(fig):
    a = panel(fig, [.03, .07, .35, .86], equal=True, xlim=(-.2, 7.6), ylim=(.2, 4.4))
    ax = a
    ax.add_patch(Polygon([(1.7, 1.45), (5.0, 1.30), (5.2, 2.50), (1.9, 2.65)], closed=True,
                         fc='#f4f8f9', ec=I, lw=1.7))
    ax.plot([0, 7.2], [1.95, 1.95], color=T, lw=1.3, ls='--')
    ax.plot(2.3, 1.60, 'o', ms=4, color=I)
    ax.plot(2.72, 1.58, 'o', ms=4, color=T)
    ax.plot(2.55, 3.35, 'o', ms=4, color=R)
    ax.plot(2.53, 2.62, 'o', ms=3.6, color=I)
    txt(ax, 1.95, 1.40, 'B', fontsize=8.8)
    txt(ax, 2.72, 1.30, "B'", fontsize=8.8, color=T)
    txt(ax, 2.62, 3.46, 'M', fontsize=8.8, color=R)
    txt(ax, 2.62, 2.72, 'G', fontsize=8.8)
    ax.plot([2.55, 2.55], [1.55, 3.35], color=R, lw=.8, ls=':')
    arrow(ax, (4.6, 1.05), (2.9, 1.05), G, 1.1)
    txt(ax, 4.65, .98, 'righting arm', fontsize=7.0, color=G)
    head(ax, r'stable if $M$ is above $G$', T)
    foot(ax, r'$BM=I/V$ sets the margin')

    b = panel(fig, [.41, .07, .27, .86], equal=True, xlim=(0, 10.4), ylim=(.2, 4.4))
    bx = b
    for x0, w, lab, col in ((.4, 2.6, 'wide: stable', T),
                            (3.7, 1.5, 'square', GOLD),
                            (6.8, .8, 'tall', R)):
        bx.add_patch(Rectangle((x0, .9), w, 2.2, fc='#f4f8f9', ec=col, lw=1.5))
        bx.plot([x0 - .2, x0 + w + .2], [2.1, 2.1], color=T, lw=.9, ls='--')
        txt(bx, x0 + w / 2, .45, lab, fontsize=7.2, ha='center', color=col)
    head(bx, 'same mass, different beam', T)
    return 'Stability is a metacentre question: BM = I/V, measured above the centre of buoyancy'


# --------------------------------------------------------------- 9. ice cases
def _ice_cases(fig):
    cases = [('ice alone', 'unchanged', T, .0),
             ('ice + stone', 'falls', R, -.18),
             ('ice + air', 'unchanged', T, .0),
             ('ice in salt water', 'rises', R, .18)]
    for i, (title, verdict, col, d) in enumerate(cases):
        a = panel(fig, [.015 + i * .247, .04, .225, .88], equal=True,
                  xlim=(0, 4.4), ylim=(0, 4.5))
        ax = a
        lvl = 2.5
        ax.add_patch(Rectangle((.5, .5), 3.4, 2.9, fc='none', ec='none'))
        ax.add_patch(Rectangle((.5, .5), 3.4, lvl - .5, fc=WATER if i != 3 else '#dbe9f2',
                               ec='none'))
        ax.plot([.5, .5], [.5, 3.4], color=I, lw=1.6)
        ax.plot([3.9, 3.9], [.5, 3.4], color=I, lw=1.6)
        ax.plot([.5, 3.9], [.5, .5], color=I, lw=1.6)
        ax.plot([.5, 3.9], [lvl, lvl], color=G, lw=.9, ls=':')
        ax.add_patch(Rectangle((1.55, lvl - .72), 1.3, 1.15, fc='#f3f8fa', ec=I, lw=1.2))
        if i == 1:
            ax.plot(2.2, lvl - .50, 'o', ms=4, color=I)
            txt(ax, 2.2, lvl - .95, 'stone', fontsize=6.6, ha='center', color=G)
        if i == 2:
            ax.add_patch(Circle((2.2, lvl + .05), .14, fc='white', ec=I, lw=.9))
            txt(ax, 2.45, lvl + .12, 'air', fontsize=6.6, color=G)
        if i == 3:
            ax.plot([.5, 3.9], [lvl, lvl], color=T, lw=1.4)
        if d:
            ax.plot([.5, 3.9], [lvl + d, lvl + d], color=col, lw=1.3, ls='--')
            arrow(ax, (3.55, lvl), (3.55, lvl + d), col, 1.3, '->', 6)
        txt(ax, 2.2, 4.10, title, fontsize=7.8, ha='center')
        txt(ax, 2.2, .22, verdict, fontsize=7.4, ha='center', color=col)
    return 'The displaced-volume ledger answers every melting-ice variant in one line'


# -------------------------------------------------------- 10. Bernoulli
def _bernoulli_streamtube(fig):
    a = panel(fig, [.02, .03, .48, .90])
    xs = np.linspace(.6, 7.4, 120)
    hw = .55 + .34 * np.cos((xs - .6) / 6.8 * 2 * np.pi) * 0
    top = 3.05 + .55 * np.exp(-((xs - 2.1) / 1.5) ** 2) - .55 * np.exp(-((xs - 5.4) / 1.4) ** 2)
    bot = 1.75 - .45 * np.exp(-((xs - 2.1) / 1.5) ** 2) + .40 * np.exp(-((xs - 5.4) / 1.4) ** 2)
    waterpoly(a, list(zip(xs, top)) + list(zip(xs[::-1], bot[::-1])), WATER)
    a.plot(xs, top, color=I, lw=1.6)
    a.plot(xs, bot, color=I, lw=1.6)
    arrow(a, (1.55, 2.85), (2.55, 2.85), T, 1.4)
    txt(a, 1.22, 2.32, r'$p_1,v_1,A_1$', fontsize=8.4)
    arrow(a, (4.90, 2.55), (5.95, 2.55), T, 1.5)
    txt(a, 4.72, 2.10, r'$p_2,v_2,A_2$', fontsize=8.4)
    a.plot([.70, 7.50], [1.02, 1.02], color=G, lw=1.0, ls=(0, (6, 4)))
    txt(a, .72, .78, 'datum', fontsize=7.8, color=G)
    arrow(a, (2.90, 1.02), (2.90, 2.02), I, .9, '<->', 5)
    txt(a, 3.00, 1.45, r'$y_1$', fontsize=8.0)
    arrow(a, (6.40, 1.02), (6.40, 1.85), I, .9, '<->', 5)
    txt(a, 6.50, 1.35, r'$y_2$', fontsize=8.0)
    txt(a, .45, 4.30, 'work-energy on a streamtube', fontsize=9.2, color=T)
    txt(a, .45, .30, r'$p+\frac{1}{2}\rho v^2+\rho g y=\mathrm{const}$', fontsize=9.4)

    b = panel(fig, [.53, .05, .45, .88])
    tot = 3.10
    for x0, z, p, v, lab in ((1.30, .85, 1.55, .70, '1'), (4.60, .55, .95, 1.60, '2')):
        b.add_patch(Rectangle((x0, z), 1.35, p, fc='#e6f0f2', ec=I, lw=1.2))
        b.add_patch(Rectangle((x0, z + p), 1.35, v, fc='#d3e8ef', ec=I, lw=1.2))
        b.add_patch(Rectangle((x0, z - .55), 1.35, .55, fc='#eef2ee', ec=I, lw=1.2))
        txt(b, x0 + .68, z + p + v / 2, r'$v^2/2g$', fontsize=7.8, ha='center')
        txt(b, x0 + .68, z + p / 2, r'$p/\rho g$', fontsize=7.8, ha='center')
        txt(b, x0 + .68, z - .28, r'$y$', fontsize=7.8, ha='center')
        b.text(x0 + .68, .28, lab, fontsize=9.0, ha='center', color=T)
    b.plot([1.15, 6.10], [tot, tot], color=R, lw=1.2, ls=(0, (5, 4)))
    b.set_ylim(-.45, 4.6)
    txt(b, 3.35, tot + .20, 'total head', fontsize=8.2, color=R)
    txt(b, 1.10, 4.35, 'the split changes, the total does not', fontsize=8.6, color=T)
    return 'Bernoulli is work-energy for a streamtube, drawn as stacked heads'


# ------------------------------------------------------------ 11. venturi, pitot
def _venturi_pitot(fig):
    a = panel(fig, [.02, .03, .46, .90])
    xs = [.5, 3.9, 4.5, 5.1, 5.7, 7.4]
    top = [3.40, 3.40, 3.05, 3.05, 3.40, 3.40]
    bot = [1.90, 1.90, 2.25, 2.25, 1.90, 1.90]
    waterpoly(a, list(zip(xs, top)) + list(zip(xs[::-1], bot[::-1])), WATER)
    for yy in (top, bot):
        a.plot(xs, yy, color=I, lw=1.8)
    a.plot([.5, .5], [1.9, 3.4], color=I, lw=1.8)
    a.plot([7.4, 7.4], [1.9, 3.4], color=I, lw=1.8)
    arrow(a, (1.15, 2.65), (2.45, 2.65), T, 1.5)
    txt(a, 1.15, 2.86, r'$v_1,\ A_1$', fontsize=8.8)
    arrow(a, (4.52, 2.65), (5.08, 2.65), T, 1.5)
    txt(a, 4.30, 2.86, r'$v_2$', fontsize=8.4)
    txt(a, 6.35, 2.95, r'$A_2<A_1$', fontsize=8.4, color=G)
    for x, lev in ((3.70, 1.05), (5.30, 1.32)):
        a.plot([x, x], [lev, 1.90], color='#b9c6cb', lw=3.2)
        a.plot([x, x], [.66, lev], color=HG, lw=11, solid_capstyle='butt')
    a.plot([3.70, 5.30], [.70, .70], color=HG, lw=11, solid_capstyle='butt')
    a.plot([5.44, 5.58], [1.05, 1.05], color=I, lw=1.2)
    a.plot([5.44, 5.58], [1.32, 1.32], color=I, lw=1.2)
    a.plot([5.52, 5.52], [1.05, 1.32], color=I, lw=1.2)
    txt(a, 5.66, 1.14, r'$\Delta h$', fontsize=8.6, va='center')
    txt(a, .45, .18, r'$Q=A_1A_2\sqrt{\frac{2\Delta p}{\rho\,(A_1^2-A_2^2)}}$', fontsize=10.0)
    txt(a, .45, 4.32, 'Venturi: the throat reads the flow', fontsize=9.2, color=T)

    b = panel(fig, [.52, .03, .46, .90])
    for yy in (1.55, 2.20, 3.05):
        b.plot([.4, 3.5], [yy, yy], color='#9fc7d3', lw=1.2)
        arrow(b, (3.0, yy), (3.55, yy), '#9fc7d3', 1.2, '-|>', 7)
    txt(b, .45, 3.28, r'flow $v$,  $p$', fontsize=8.6, color=G)
    b.plot([4.45, 7.4], [2.28, 2.28], color=I, lw=1.8)
    b.plot([4.45, 7.4], [2.62, 2.62], color=I, lw=1.8)
    b.add_patch(Arc((4.45, 2.45), .34, .34, theta1=90, theta2=270, color=I, lw=1.8))
    b.plot([7.4, 7.4], [2.28, 1.05], color=I, lw=1.8)
    b.add_patch(Circle((4.32, 2.45), .085, fc=R, ec='none', zorder=5))
    txt(b, 3.05, 3.95, r'stagnation: $v=0$, $p_0$', fontsize=8.6, color=R)
    arrow(b, (4.35, 3.86), (4.32, 2.60), R, 1.0, '-', 5)
    b.add_patch(Circle((5.6, 2.66), .065, fc=T, ec='none', zorder=5))
    txt(b, 5.75, 2.86, r'$v$, $p$', fontsize=8.4, color=T)
    txt(b, .45, 1.25, r'$p_0-p=\frac{1}{2}\rho v^2$', fontsize=10.0)
    txt(b, .45, .55, r'$=\rho_{Hg}\,g\,\Delta h$', fontsize=10.0, color=G)
    txt(b, 1.60, 4.30, 'Pitot: stop it, read the head', fontsize=9.2, color=T)
    return 'Venturi and pitot are one Bernoulli balance read off a manometer'



# ------------------------------------------------------------- 12. Torricelli
def _torricelli(fig):
    a = panel(fig, [.02, .03, .44, .90])
    a.plot([1.00, 1.00], [1.00, 4.05], color=I, lw=2.2)
    a.plot([1.00, 4.60], [1.00, 1.00], color=I, lw=2.2)
    a.plot([4.60, 4.60], [1.00, 2.02], color=I, lw=2.2)
    a.plot([4.60, 4.60], [2.34, 4.05], color=I, lw=2.2)
    waterpoly(a, [(1.00, 1.00), (4.60, 1.00), (4.60, 3.60), (1.00, 3.60)], WATER)
    a.plot([1.00, 4.60], [3.60, 3.60], color=T, lw=1.6)
    ts = np.linspace(0, 1, 60)
    a.plot(4.60 + 3.15 * ts, 2.18 - 1.00 * ts ** 2, color=T, lw=2.0)
    arrow(a, (5.05, 2.10), (5.80, 1.90), T, 1.4)
    arrow(a, (.72, 1.00), (.72, 3.60), I, 1.0, '<->', 6)
    txt(a, .46, 2.30, r'$H$', fontsize=9.0)
    arrow(a, (1.28, 2.18), (1.28, 3.60), I, 1.0, '<->', 6)
    txt(a, 1.40, 2.86, r'$h$', fontsize=9.0)
    txt(a, 4.95, 2.55, r'$v=\sqrt{2gh}$', fontsize=9.4)
    txt(a, 4.95, .55, r'$x=2\sqrt{h(H-h)}$', fontsize=9.4, color=G)
    txt(a, .45, 4.30, 'Torricelli: depth becomes speed', fontsize=9.2, color=T)

    b = panel(fig, [.50, .21, .40, .64])
    axes2(b, r'$h/H$', r'$x/H$')
    u = np.linspace(0, 1, 200)
    b.plot(u, 2 * np.sqrt(u * (1 - u)), color=T, lw=2.0)
    b.plot([.5], [1.0], 'o', ms=5, color=R)
    b.annotate('max at h=H/2', xy=(.5, 1.0), xytext=(.56, .55), fontsize=8.2,
               color=R, arrowprops=dict(arrowstyle='->', color=R, lw=1.0))
    b.set_xlim(0, 1); b.set_ylim(0, 1.15)
    return 'Torricelli gives the speed; the parabola gives the range'



# ------------------------------------------------------------ 13. jet momentum
def _jet_thrust(fig):
    a = panel(fig, [.02, .03, .48, .90])
    a.add_patch(Polygon([(.35, 3.30), (1.55, 2.95), (1.55, 2.05), (.35, 1.70)],
                        closed=True, fc='#eef2f3', ec=I, lw=1.6))
    a.add_patch(Rectangle((1.55, 2.22), 2.65, .56, fc='#cfe6ef', ec=T, lw=1.0))
    arrow(a, (1.75, 2.50), (3.05, 2.50), T, 1.4)
    txt(a, 1.68, 2.86, r'$v,\ a$', fontsize=9.0)
    a.add_patch(Rectangle((4.20, 1.15), .24, 2.95, fc='#dfe7ea', ec=I, lw=1.6))
    for yy in (1.40, 1.85, 3.20, 3.65):
        arrow(a, (4.95, yy), (5.35, yy), T, 1.0, '-|>', 6)
    arrow(a, (4.62, 2.50), (6.10, 2.50), R, 1.8)
    txt(a, 4.72, 2.72, r'$F=\rho a v^2$', fontsize=9.4, color=R)
    txt(a, 4.35, 4.30, 'jet stopped by a plate', fontsize=9.2, color=T)

    b = panel(fig, [.54, .03, .44, .90])
    b.add_patch(Rectangle((3.55, 1.15), .24, 2.95, fc='#dfe7ea', ec=I, lw=1.6))
    b.add_patch(Rectangle((1.50, 2.22), 2.05, .56, fc='#cfe6ef', ec=T, lw=1.0))
    arrow(b, (1.65, 2.50), (2.85, 2.50), T, 1.4)
    arrow(b, (3.90, 3.55), (4.85, 3.55), I, 1.4, '-|>', 8)
    txt(b, 4.00, 3.72, r'$u$', fontsize=9.0)
    txt(b, 1.55, 2.86, r'$v-u$', fontsize=9.0)
    txt(b, .45, 1.55, r'$F=\rho a (v-u)^2$', fontsize=9.6, color=R)
    txt(b, .45, .85, 'the plate runs away, so less water is turned', fontsize=8.0, color=G)
    return 'A jet pays momentum flux rho a v squared; a moving plate pays less'



# ---------------------------------------------------------- 14. Poiseuille
def _poiseuille_profile(fig):
    a = panel(fig, [.02, .03, .44, .90])
    a.plot([1.20, 6.30], [1.35, 1.35], color=I, lw=1.8)
    a.plot([1.20, 6.30], [3.85, 3.85], color=I, lw=1.8)
    rs = np.linspace(-1, 1, 80)
    a.plot(1.35 + 3.30 * (1 - rs ** 2), 2.60 + 1.05 * rs, color=T, lw=1.8)
    for r0 in (-.75, -.45, -.15, .15, .45, .75):
        arrow(a, (1.35, 2.60 + 1.05 * r0), (1.35 + 3.30 * (1 - r0 ** 2), 2.60 + 1.05 * r0), '#7fb6bd')
    txt(a, 4.95, 3.62, r'$v_{max}$', fontsize=8.6, color=T)
    txt(a, 1.35, 1.10, r'wall: $v=0$', fontsize=8.4, color=G)
    txt(a, 1.35, 4.15, r'axis: $v_{max}=\frac{R^2\Delta p}{4\eta L}$', fontsize=8.4, color=T)
    txt(a, .45, .35, 'the profile is a paraboloid, not a plug', fontsize=8.2, color=G)

    b = panel(fig, [.50, .03, .48, .90])
    b.plot([1.10, 7.30], [1.55, 1.55], color=I, lw=1.6)
    b.plot([1.10, 7.30], [3.75, 3.75], color=I, lw=1.6)
    b.add_patch(Polygon([(1.10, 1.55), (1.10, 3.75), (7.30, 3.75), (7.30, 1.55)],
                        closed=True, fc='#f7fafb', ec='none', zorder=0))
    b.plot([2.20, 6.30], [2.30, 2.30], color=G, lw=1.2, ls=(0, (4, 3)))
    b.plot([2.20, 6.30], [3.05, 3.05], color=G, lw=1.2, ls=(0, (4, 3)))
    arrow(b, (2.55, 2.62), (3.35, 2.62), R, 1.3)
    txt(b, 2.35, 2.20, r'$p_1$', fontsize=9.0, color=R)
    arrow(b, (5.95, 2.62), (5.15, 2.62), R, 1.3)
    txt(b, 5.95, 2.20, r'$p_2$', fontsize=9.0, color=R)
    arrow(b, (4.35, 3.10), (5.15, 3.10), T, 1.2)
    txt(b, 4.30, 3.32, r'$\tau\,2\pi rL$', fontsize=8.8, color=T)
    arrow(b, (6.75, 2.30), (6.75, 3.05), I, 1.0, '<->', 6)
    txt(b, 6.88, 2.66, r'$dr$', fontsize=8.2)
    txt(b, .45, .70, r'$\pi r^2(p_1-p_2)=2\pi rL\,\tau$', fontsize=9.6)
    txt(b, .45, .25, 'then integrate with no slip', fontsize=8.2, color=G)
    return 'Shell balance gives the parabola, then Poiseuille R to the fourth'



# --------------------------------------------------------- 15. hydraulic networks
def _hydraulic_network(fig):
    a = panel(fig, [.02, .03, .46, .90])
    a.add_patch(Rectangle((.80, 2.15), 3.20, .70, fc='#e8f0f2', ec=I, lw=1.4))
    a.add_patch(Rectangle((4.00, 2.35), 3.60, .30, fc='#e8f0f2', ec=I, lw=1.4))
    arrow(a, (1.10, 2.50), (2.10, 2.50), T, 1.2)
    txt(a, .80, 3.10, r'$R_1=\frac{8\eta L}{\pi r^4}$', fontsize=8.4)
    txt(a, 3.95, 3.05, r'$R_2=16R_1$', fontsize=8.4, color=G)
    arrow(a, (7.75, 2.50), (8.55, 2.50), T, 1.2)
    txt(a, 7.60, 2.10, r'$\Delta p$', fontsize=8.6)
    txt(a, .45, .95, 'series: resistances add', fontsize=8.4, color=T)
    txt(a, .45, .35, r'$R=R_1+R_2$', fontsize=9.4)

    b = panel(fig, [.52, .03, .46, .90])
    b.add_patch(Rectangle((.60, 2.30), 1.70, .55, fc='#e8f0f2', ec=I, lw=1.4))
    b.plot([2.30, 3.10], [2.60, 3.45], color=I, lw=1.3)
    b.plot([2.30, 3.10], [2.55, 1.75], color=I, lw=1.3)
    b.plot([3.10, 6.40], [3.45, 3.45], color=I, lw=1.3)
    b.plot([3.10, 6.40], [1.75, 1.75], color=I, lw=1.3)
    b.plot([6.40, 7.20], [3.45, 2.60], color=I, lw=1.3)
    b.plot([6.40, 7.20], [1.75, 2.55], color=I, lw=1.3)
    b.add_patch(Rectangle((7.20, 2.30), 1.40, .55, fc='#e8f0f2', ec=I, lw=1.4))
    txt(b, 3.15, 3.70, r'wide: $16/17$ of $Q$', fontsize=8.2)
    txt(b, 3.15, 1.35, r'narrow: $1/17$', fontsize=8.2, color=R)
    txt(b, .55, .95, 'parallel: same head, R splits as r to the fourth', fontsize=8.0, color=T)
    txt(b, .55, .35, r'$Q_{narrow}/Q=\frac{1}{1+2^4}$', fontsize=9.4)
    return 'Hydraulic Ohm: series add, parallel split as the fourth power of radius'



# -------------------------------------------------------------- 16. Stokes
def _stokes_regime(fig):
    a = panel(fig, [.02, .03, .40, .90], xlim=(.4, 7.7), equal=True)
    a.add_patch(Circle((3.6, 2.45), .62, fc='#e9f2f5', ec=I, lw=1.6))
    arrow(a, (3.25, 2.35), (3.25, 3.95), T, 1.5)
    txt(a, 2.62, 3.55, r'$F_b$', fontsize=9.0, color=T, ha='right')
    arrow(a, (3.95, 2.35), (3.95, 3.95), R, 1.5)
    txt(a, 4.15, 3.42, r'$6\pi\eta rv$', fontsize=8.8, color=R)
    arrow(a, (3.60, 2.10), (3.60, .55), I, 1.8)
    txt(a, 3.72, .95, r'$mg$', fontsize=9.0)
    arrow(a, (5.15, 3.75), (5.15, 1.55), G, 1.2, '-|>', 7)
    txt(a, 5.30, 2.60, r'$v_t$', fontsize=8.8, color=G)
    txt(a, .45, 4.30, 'steady fall: three forces', fontsize=9.2, color=T)

    b = panel(fig, [.46, .19, .50, .70])
    b.axis('on')
    for sp in ('top', 'right'):
        b.spines[sp].set_visible(False)
    b.set_xscale('log'); b.set_yscale('log')
    b.tick_params(labelsize=7.6, length=3, pad=2)
    b.grid(alpha=.12, lw=.7, which='both')
    rr = np.logspace(-6, -2.4, 300)
    g, rho, eta, rhoa, cd = 9.8, 1000., 1.8e-5, 1.2, .44
    v1 = 2 * rr ** 2 * rho * g / (9 * eta)
    v2 = np.sqrt(8 * rr * rho * g / (3 * cd * rhoa))
    b.plot(rr, v1, color=T, lw=2.0)
    b.plot(rr, v2, color=R, lw=2.0)
    b.plot([4e-5], [2 * (4e-5) ** 2 * rho * g / (9 * eta)], 'o', ms=6, color=GOLD, zorder=5)
    b.annotate(r'$r^*\approx40\ \mu$m', xy=(4e-5, 0.19), xytext=(2.2e-6, 3.2),
               fontsize=8.4, color=GOLD,
               arrowprops=dict(arrowstyle='->', color=GOLD, lw=1.0))
    b.text(1.2e-4, 2.2e-2, 'Stokes  $v\\propto r^2$', fontsize=8.4, color=T)
    b.text(1.2e-3, 1.6, 'quadratic', fontsize=8.4, color=R)
    b.set_xlabel(r'radius $r$  (m)', fontsize=8.4, labelpad=1)
    b.set_ylabel(r'$v_t$  (m/s)', fontsize=8.4, labelpad=1)
    b.set_xlim(1e-6, 4e-3); b.set_ylim(1e-4, 40)
    return 'Stokes holds below Re about 1; a rain drop is already quadratic'



# --------------------------------------------------------- 17. surface energy
def _surface_energy(fig):
    a = panel(fig, [.02, .03, .46, .90])
    a.plot([1.10, 1.10], [1.20, 3.90], color=I, lw=2.0)
    a.plot([4.90, 4.90], [1.20, 3.90], color=I, lw=2.0)
    a.plot([1.10, 4.90], [1.20, 1.20], color=I, lw=2.0)
    a.add_patch(Rectangle((1.10, 1.20), 3.80, 1.95, fc='#e3f1f4', ec='none'))
    a.plot([1.10, 4.90], [3.15, 3.15], color=T, lw=2.6)
    arrow(a, (3.00, 3.32), (3.00, 4.10), R, 1.6)
    txt(a, 2.72, 3.95, r'$F$', fontsize=9.6, color=R)
    arrow(a, (5.15, 3.15), (5.15, 3.75), I, 1.0, '<->', 6)
    txt(a, 5.25, 3.45, r'$\Delta x$', fontsize=8.4)
    txt(a, .45, 4.32, 'a film has two faces', fontsize=9.2, color=T)
    txt(a, .45, .70, r'$F=2\gamma L$', fontsize=10.0)
    txt(a, .45, .28, 'pull the wire by dx: work = 2 gamma L dx', fontsize=8.0, color=G)

    b = panel(fig, [.52, .03, .46, .90])
    b.plot([1.20, 6.20], [2.55, 2.55], color=I, lw=3.0)
    for dx in (-.32, .32):
        b.plot([1.20, 6.20], [2.55 + dx, 2.55 + dx], color='#7fb6bd', lw=1.2)
    arrow(b, (3.70, 2.88), (2.70, 2.88), T, 1.2)
    arrow(b, (3.70, 2.22), (2.70, 2.22), T, 1.2)
    txt(b, 2.45, 2.95, r'$\gamma L$', fontsize=8.8, color=T)
    txt(b, 2.45, 1.95, r'$\gamma L$', fontsize=8.8, color=T)
    txt(b, 1.20, 1.55, 'two surfaces, each pulls with gamma L', fontsize=8.2, color=G)
    txt(b, 1.20, 3.75, r'$W=2\gamma\,L\,\Delta x=\gamma\,\Delta A$', fontsize=9.4)
    txt(b, .45, 4.32, 'energy and force agree', fontsize=9.2, color=T)
    return 'Surface energy is the same number as surface tension, counted per face'



# ------------------------------------------------------- 18. excess pressure
def _excess_pressure(fig):
    a = panel(fig, [.02, .05, .30, .86], xlim=(1.0, 6.8), equal=True)
    a.add_patch(Circle((3.9, 3.05), .95, fc='#e8f3f8', ec=T, lw=1.8))
    arrow(a, (3.9, 3.05), (5.15, 3.05), R, 1.2)
    arrow(a, (3.9, 3.05), (2.65, 3.05), R, 1.2)
    txt(a, 3.72, 2.72, r'$\Delta p$', fontsize=8.8, color=R)
    arrow(a, (2.95, 4.15), (3.45, 4.15), T, 1.2)
    arrow(a, (4.85, 4.15), (4.35, 4.15), T, 1.2)
    txt(a, 2.55, 4.02, r'$\gamma$', fontsize=8.6, color=T)
    txt(a, 4.95, 4.02, r'$\gamma$', fontsize=8.6, color=T)
    txt(a, 1.10, 1.55, 'drop: one surface', fontsize=8.6, color=T)
    txt(a, 1.10, 1.00, r'$\Delta p=2\gamma/r$', fontsize=9.6)

    b = panel(fig, [.355, .05, .30, .86], xlim=(1.0, 6.8), equal=True)
    b.add_patch(Circle((3.9, 3.05), .90, fc='#e8f3f8', ec=T, lw=1.6))
    b.add_patch(Circle((3.9, 3.05), 1.01, fc='none', ec=I, lw=1.0))
    arrow(b, (3.9, 3.05), (5.15, 3.05), R, 1.2)
    arrow(b, (3.9, 3.05), (2.65, 3.05), R, 1.2)
    txt(b, 3.72, 2.72, r'$\Delta p$', fontsize=8.8, color=R)
    txt(b, 1.10, 1.55, 'bubble: two surfaces', fontsize=8.6, color=T)
    txt(b, 1.10, 1.00, r'$\Delta p=4\gamma/r$', fontsize=9.6)

    c = panel(fig, [.69, .05, .29, .86], xlim=(1.0, 6.6), equal=True)
    c.add_patch(Rectangle((2.55, 2.00), 3.10, 2.10, fc='#e8f3f8', ec='none'))
    c.add_patch(Arc((2.55, 3.05), .80, 2.10, theta1=90, theta2=270, color=T, lw=1.6))
    c.add_patch(Arc((5.65, 3.05), .80, 2.10, theta1=270, theta2=90, color=T, lw=1.6))
    c.plot([2.55, 5.65], [4.10, 4.10], color=T, lw=1.6)
    c.plot([2.55, 5.65], [2.00, 2.00], color=T, lw=1.6)
    arrow(c, (4.10, 3.05), (4.10, 3.85), R, 1.2)
    txt(c, 4.25, 3.45, r'$\Delta p$', fontsize=8.8, color=R)
    txt(c, 1.10, 1.55, 'jet: one curvature', fontsize=8.6, color=T)
    txt(c, 1.10, 1.00, r'$\Delta p=\gamma/r$', fontsize=9.6)
    return 'Excess pressure counts surfaces and principal curvatures'


# --------------------------------------------------------------- 19. Jurin
def _jurin(fig):
    a = panel(fig, [.02, .03, .46, .90])
    a.plot([1.00, 1.00], [1.20, 3.20], color=I, lw=2.0)
    a.plot([4.40, 4.40], [1.20, 3.20], color=I, lw=2.0)
    a.plot([1.00, 4.40], [1.20, 1.20], color=I, lw=2.0)
    a.add_patch(Rectangle((1.00, 1.20), 3.40, 1.00, fc=WATER, ec='none'))
    a.plot([1.00, 4.40], [2.20, 2.20], color=T, lw=1.4)
    a.plot([2.35, 2.35], [1.45, 4.10], color=I, lw=1.8)
    a.plot([2.85, 2.85], [1.45, 4.10], color=I, lw=1.8)
    a.add_patch(Rectangle((2.35, 1.55), .50, 1.85, fc=WATER, ec='none'))
    a.add_patch(Arc((2.60, 3.40), .50, .26, theta1=0, theta2=180, color=T, lw=1.6))
    arrow(a, (2.60, 3.50), (2.60, 4.02), R, 1.3)
    arrow(a, (2.60, 3.30), (2.60, 2.55), G, 1.3)
    txt(a, 2.48, 3.70, r'$2\pi r\gamma\cos\theta$', fontsize=7.8, color=R, ha='right')
    txt(a, 1.15, 2.90, r'$\rho g\pi r^2h$', fontsize=7.8, color=G)
    a.plot([3.18, 3.18], [2.20, 3.40], color=I, lw=1.0)
    a.plot([3.10, 3.26], [2.20, 2.20], color=I, lw=1.0)
    a.plot([3.10, 3.26], [3.40, 3.40], color=I, lw=1.0)
    txt(a, 3.30, 2.78, r'$h$', fontsize=8.6)
    txt(a, .45, 4.40, 'a narrow tube lifts a tall column', fontsize=9.2, color=T)
    txt(a, .45, .60, 'rim pull balances the column weight', fontsize=8.2, color=G)

    b = panel(fig, [.52, .03, .46, .90])
    b.plot([.70, .70], [1.20, 2.60], color=I, lw=1.8)
    b.plot([3.20, 3.20], [1.20, 2.60], color=I, lw=1.8)
    b.plot([.70, 3.20], [1.20, 1.20], color=I, lw=1.8)
    b.add_patch(Rectangle((.70, 1.20), 2.50, .75, fc=WATER, ec='none'))
    b.plot([.70, 3.20], [1.95, 1.95], color=T, lw=1.2)
    b.plot([1.65, 1.65], [1.35, 2.35], color=I, lw=1.6)
    b.plot([2.15, 2.15], [1.35, 2.35], color=I, lw=1.6)
    b.add_patch(Rectangle((1.65, 1.45), .50, .70, fc=WATER, ec='none'))
    b.add_patch(Arc((1.90, 2.15), .50, .34, theta1=0, theta2=180, color=T, lw=1.6))
    txt(b, .70, 2.95, 'short tube: R grows, h falls', fontsize=8.2, color=T)
    txt(b, .70, .68, r'$hR=h^\prime R^\prime$', fontsize=9.4)

    th = np.deg2rad(28)
    x0, y0, L, wd = 6.05, 1.55, 2.95, .26
    d = np.array([np.cos(th), np.sin(th)]); n = np.array([-np.sin(th), np.cos(th)])
    P0 = np.array([x0, y0])
    corners = [P0 + n * wd, P0 + d * L + n * wd, P0 + d * L - n * wd, P0 - n * wd]
    b.add_patch(Polygon(corners, closed=True, fc='#eef4f5', ec=I, lw=1.6))
    inner = [P0 + n * wd * .75, P0 + d * (L * .55) + n * wd * .75,
             P0 + d * (L * .55) - n * wd * .75, P0 - n * wd * .75]
    b.add_patch(Polygon(inner, closed=True, fc=WATER, ec='none'))
    b.plot([5.30, 9.40], [1.55, 1.55], color=T, lw=1.2)
    b.plot([5.55, 5.55], [1.55, 1.55 + L * np.sin(th)], color=I, lw=1.0)
    b.plot([5.47, 5.63], [1.55, 1.55], color=I, lw=1.0)
    b.plot([5.47, 5.63], [1.55 + L * np.sin(th)] * 2, color=I, lw=1.0)
    txt(b, 5.32, 1.55 + L * np.sin(th) / 2, r'$h$', fontsize=8.6, ha='right')
    txt(b, 5.60, 3.72, 'tilt: same vertical h', fontsize=8.2, color=G)
    return 'Jurin balances rim force against weight; a short tube only changes R'


# ------------------------------------------------------- 20. draining tank
def _drain_two_regimes(fig):
    a = panel(fig, [.02, .06, .33, .86], equal=True, xlim=(0, 5.6), ylim=(.2, 4.4))
    ax = a
    ax.add_patch(Rectangle((1.0, .8), 3.6, 3.1, fc=WATER, ec='none'))
    ax.plot([1.0, 1.0], [.8, 3.9], color=I, lw=2.0)
    ax.plot([4.6, 4.6], [.8, 1.4], color=I, lw=2.0)
    ax.plot([4.6, 4.6], [1.65, 3.9], color=I, lw=2.0)
    ax.plot([1.0, 4.6], [.8, .8], color=I, lw=2.0)
    ax.plot([1.0, 4.6], [3.9, 3.9], color=T, lw=1.4)
    dimy(ax, .75, .8, 3.9, r'$H$', side='left')
    dimx(ax, 1.0, 4.6, .45, r'$A$')
    txt(ax, 4.78, 1.50, r'$a$', fontsize=8.4)
    arrow(ax, (4.75, 1.52), (5.35, 1.52), T, 1.5)
    txt(ax, 1.15, 3.55, r'$h(t)$', fontsize=8.4, color=G)
    head(ax, r'quasi-steady: $a\ll A$', T)

    b = panel(fig, [.39, .20, .57, .62], xlim=(-2, 62), ylim=(-.05, 1.2))
    t = np.linspace(0, 60, 500)
    b.plot(t, np.clip(1 - t / 50.5, 0, None) ** 2, color=I, lw=2.0)
    b.plot(t, np.exp(-t / 18.0), color=T, lw=2.0, ls='--')
    b.plot([50.5], [0], 'o', ms=4, color=I)
    b.annotate(r'$T=\frac{A}{a}\sqrt{\frac{2H}{g}}$', xy=(50.5, 0), xytext=(30, .22),
               fontsize=8.4, arrowprops=dict(arrowstyle='->', color=I, lw=.8))
    b.annotate(r'$h=He^{-t/\tau}$', xy=(18, np.exp(-1)), xytext=(23, .62), fontsize=8.4,
               color=T, arrowprops=dict(arrowstyle='->', color=T, lw=.8))
    b.text(1.0, .06, 'orifice: finite time', fontsize=7.2, color=I)
    b.text(28, .90, 'capillary: never empty', fontsize=7.2, color=T)
    axes2(b, r'time $t$ (s)', r'$h/H$')
    b.set_yticks([0, .25, .5, .75, 1])
    return 'Two drain laws: the square-root law empties in finite time, the exponential never does'


# ------------------------------------------------ 21. paraboloid three ways
def _paraboloid_three_ways(fig):
    a = panel(fig, [.01, .06, .32, .86], equal=True, xlim=(-2.2, 2.2), ylim=(-.6, 4.4))
    ax = a
    r = np.linspace(-2.0, 2.0, 200)
    ax.plot(r, 2.3 + .30 * r ** 2, color=T, lw=1.8)
    ax.add_patch(Rectangle((.9, 2.55), .75, .32, fc='#f6e7c8', ec=I, lw=1.1))
    arrow(ax, (1.28, 2.87), (1.28, 3.62), T, 1.3)
    txt(ax, 1.38, 3.42, r'$N$', fontsize=8.8, color=T)
    arrow(ax, (1.28, 2.55), (1.28, 1.85), G, 1.3)
    txt(ax, 1.38, 1.95, r'$mg$', fontsize=8.8, color=G)
    arrow(ax, (1.28, 2.71), (2.05, 2.71), R, 1.3)
    txt(ax, .35, 2.42, r'$m\omega^2r$', fontsize=8.0, color=R)
    txt(ax, 0, 4.12, '(a) force balance', fontsize=8.0, ha='center', color=T)
    txt(ax, 0, .20, r'$\tan\alpha=\omega^2r/g$', fontsize=8.6, ha='center')

    b = panel(fig, [.335, .06, .30, .86], equal=True, xlim=(-1.6, 1.6), ylim=(-.6, 4.4))
    bx = b
    rr = np.linspace(-1.35, 1.35, 200)
    for c0, cc in zip((.6, 1.35, 2.1), ('#dce9e6',) * 2 + (T,)):
        bx.plot(rr, c0 + .85 * rr ** 2, color=cc, lw=2.4 if cc == T else 1.2)
    bx.text(0, 4.12, '(b) equipotentials', fontsize=8.0, ha='center', color=T)
    bx.text(0, .20, r'$\Phi=gz-\frac{1}{2}\omega^2r^2$', fontsize=8.4, ha='center')

    c = panel(fig, [.66, .06, .32, .86], equal=True, xlim=(-.3, 4.6), ylim=(-.6, 4.4))
    cx = c
    cx.add_patch(Rectangle((.3, 1.6), 3.7, .32, fc='#e8f3f8', ec=I, lw=1.2))
    for x in (.7, 2.1, 3.6):
        arrow(cx, (x, 2.2), (x, 1.68), T, 1.1)
    cx.plot([2.1, 2.1], [1.6, 2.55], color=G, lw=.9, ls=':')
    dimx(cx, .3, 4.0, 1.05, r'$r$')
    txt(cx, 2.1, 2.72, 'axis', fontsize=7.2, color=G, ha='center')
    txt(cx, 2.1, 4.12, '(c) centrifugal head', fontsize=8.0, ha='center', color=T)
    txt(cx, 2.1, .20, r'$p-\frac{1}{2}\rho\omega^2r^2=$ const', fontsize=8.0, ha='center')
    return 'The rotating free surface is a paraboloid: Newton, energy and centrifugal head agree'


# ------------------------------------------------------------- 22. raindrop
def _raindrop(fig):
    a = panel(fig, [.03, .06, .46, .86], equal=True, xlim=(-.4, 8.8), ylim=(.2, 4.4))
    ax = a
    ax.plot([.3, 8.4], [1.0, 1.0], color=G, lw=.9)
    for x, rad, lab in ((1.2, .10, 'mist'), (2.9, .17, 'drizzle'), (4.9, .30, '2 mm drop')):
        ax.add_patch(Circle((x, 1.0 + rad + .05), rad, fc='#dcedf5', ec=I, lw=1.2))
        txt(ax, x, 1.75, lab, fontsize=7.4, ha='center', color=G)
    txt(ax, .4, 3.15, r'$r<r^*$: Stokes,  $v_t\propto r^2$', fontsize=8.2)
    txt(ax, .4, 2.62, r'$r>r^*$: quadratic,  $v_t\propto\sqrt{r}$', fontsize=8.2)
    txt(ax, .4, 2.08, r'$r^*\approx4\times10^{-5}$ m, $v^*\approx0.19$ m/s', fontsize=7.8, color=T)
    head(ax, r'radius picks the drag law', T)

    b = panel(fig, [.53, .20, .44, .62], xlim=(0, 8), ylim=(0, 1.12))
    t = np.linspace(0, 8, 400)
    b.plot(t, np.tanh(1.2 * t), color=I, lw=2.0)
    b.plot([0, 8], [1, 1], color=T, lw=.9, ls='--')
    b.text(3.6, .86, 'terminal speed', fontsize=7.4, color=T)
    b.annotate(r'vacuum from 2 km: $200$ m/s', xy=(1.0, .95), xytext=(1.6, .38),
               fontsize=7.4, color=R, arrowprops=dict(arrowstyle='->', color=R, lw=.8))
    axes2(b, r'time (s, schematic)', r'$v/v_t$')
    b.set_yticks([0, .5, 1])
    return 'A raindrop never reaches sqrt(2gh): drag sets a terminal speed long before it lands'


# ------------------------------------------------------- 23. Young-Laplace
def _young_laplace_patch(fig):
    a = panel(fig, [.02, .06, .42, .86], equal=True, xlim=(-.4, 7.4), ylim=(.2, 4.4))
    ax = a
    th = np.linspace(-.95, .95, 80)
    ax.plot(2.0 + 1.7 * np.cos(th), 1.9 + 1.7 * np.sin(th), color=T, lw=2.4)
    ax.plot([1.45, 2.65], [.85, .85], color=I, lw=1.2)
    ax.plot([2.05, 2.05], [.95, 1.95], color=G, lw=1.0, ls=':')
    arrow(ax, (2.05, 1.90), (2.95, 2.42), R, 1.4)
    txt(ax, 3.02, 2.30, r'$\delta n$', fontsize=8.8, color=R)
    ax.annotate('', xy=(2.0, 2.05), xytext=(.55, 2.05),
                arrowprops=dict(arrowstyle='<->', color=G, lw=1.0))
    txt(ax, .85, 2.22, r'$r_1$', fontsize=8.6)
    txt(ax, 2.15, 3.55, r'$r_2$', fontsize=8.6)
    txt(ax, 4.3, 3.05, r'$\delta A=A\,\delta n\,(1/r_1+1/r_2)$', fontsize=8.0)
    txt(ax, 4.3, 2.45, r'$\Delta p\,\delta V=\gamma\,\delta A$', fontsize=8.2)
    txt(ax, 4.3, 1.55, r'$\Delta p=\gamma(1/r_1+1/r_2)$', fontsize=8.8, color=T)
    head(ax, 'virtual work on a patch', T)

    b = panel(fig, [.47, .06, .50, .86], equal=True, xlim=(-.2, 9.6), ylim=(.2, 4.4))
    bx = b
    bx.add_patch(Circle((2.0, 3.1), .28, fc='none', ec=I, lw=1.8))
    bx.add_patch(Circle((2.0, 1.1), .28, fc='none', ec=I, lw=1.8))
    z = np.linspace(-1.0, 1.0, 200)
    rr = .55 * np.cosh(z / .55)
    bx.plot(2.0 + rr, 2.1 + z, color=T, lw=1.9)
    bx.add_patch(Circle((6.6, 3.1), .28, fc='none', ec=I, lw=1.8))
    bx.add_patch(Circle((6.6, 1.1), .28, fc='none', ec=I, lw=1.8))
    bx.add_patch(Circle((6.6, 3.1), .28, fc='#e8f3f8', ec=I, lw=1.8))
    bx.add_patch(Circle((6.6, 1.1), .28, fc='#e8f3f8', ec=I, lw=1.8))
    bx.plot([6.6, 6.6], [1.4, 2.8], color=R, lw=1.5)
    bx.plot([6.6, 6.6], [2.8, 2.8], color='none')
    bx.annotate('', xy=(2.9, 2.9), xytext=(2.9, 1.3),
                arrowprops=dict(arrowstyle='<->', color=G, lw=1.0))
    txt(bx, 3.0, 2.0, r'$d$', fontsize=8.4, color=G)
    txt(bx, 2.0, .45, 'catenoid spans', fontsize=7.6, ha='center', color=T)
    txt(bx, 6.6, .45, r'snaps if $d/R>1.33$', fontsize=7.6, ha='center', color=R)
    head(bx, 'zero mean curvature, limited existence', T)
    return 'Young-Laplace from virtual work; a catenoid shows a minimal surface can cease to exist'


# -------------------------------------------------- 24. drop weight, strider
def _drop_strider(fig):
    a = panel(fig, [.02, .06, .32, .86], equal=True, xlim=(-2.4, 2.4), ylim=(.2, 4.4))
    ax = a
    ax.plot([-.55, -.55], [3.2, 4.2], color=I, lw=2.0)
    ax.plot([.55, .55], [3.2, 4.2], color=I, lw=2.0)
    ax.add_patch(Rectangle((-.55, 3.2), 1.1, 1.0, fc=WATER, ec='none'))
    th = np.linspace(0, 2 * np.pi, 200)
    ax.fill(.62 * np.sin(th), 2.45 - .72 * np.cos(th) + .16 * np.cos(2 * th),
            color='#dcedf5', ec=I, lw=1.4)
    ax.plot([-.48, -.20], [2.90, 2.90], color=R, lw=1.3)
    ax.plot([.20, .48], [2.90, 2.90], color=R, lw=1.3)
    arrow(ax, (-1.1, 2.90), (-.55, 2.90), R, 1.2, '<->', 6)
    arrow(ax, (1.1, 2.90), (.55, 2.90), R, 1.2, '<->', 6)
    txt(ax, 0, 3.28, r'$2\pi r\gamma$', fontsize=7.8, ha='center', color=R)
    arrow(ax, (0, 1.45), (0, .72), G, 1.6)
    txt(ax, .12, 1.05, r'$mg$', fontsize=8.6, color=G)
    txt(ax, 0, 4.15, 'Tate: the neck ring holds the drop', fontsize=7.4, ha='center', color=G)
    txt(ax, 0, .30, r'$\gamma_{naive}=mg/2\pi r$', fontsize=8.6, ha='center')

    b = panel(fig, [.38, .06, .60, .86], equal=True, xlim=(0, 14.4), ylim=(.2, 4.4))
    bx = b
    xs = np.linspace(0, 14, 400)
    ys = 1.55 - 1.0 * np.exp(-((xs - 7.2) / 1.35) ** 2)
    bx.plot(xs, ys, color=T, lw=2.2)
    bx.plot([0, 14], [1.55, 1.55], color=T, lw=1.0, ls=':', alpha=.5)
    bx.plot([6.5, 6.85, 7.3], [3.6, 1.35, .60], color=I, lw=2.0)
    bx.plot(6.95, 1.18, 'o', ms=3.6, color=I)
    arrow(bx, (5.5, .80), (6.05, 1.32), R, 1.4)
    arrow(bx, (8.9, .80), (8.35, 1.32), R, 1.4)
    txt(bx, 5.30, .55, r'$\gamma$', fontsize=8.8, color=R)
    txt(bx, 8.90, .55, r'$\gamma$', fontsize=8.8, color=R)
    txt(bx, 7.2, .18, r'contact length $\ell$', fontsize=7.4, ha='center')
    txt(bx, 7.2, 3.95, r'$F\approx2\gamma\ell$', fontsize=9.0, ha='center')
    txt(bx, 7.2, 3.45, r'support $\propto L$, weight $\propto L^3$', fontsize=7.4,
        ha='center', color=G)
    return 'Drop weight gives gamma within a correction; the strider shows support is a line, weight a volume'


# --------------------------------------------------------------- 25. tree
def _tree_suction(fig):
    a = panel(fig, [.02, .06, .40, .86], equal=True, xlim=(0, 8.8), ylim=(.2, 4.4))
    ax = a
    ax.plot([.3, 3.0], [.8, .8], color=I, lw=2.0)
    for x in np.linspace(.35, 2.9, 9):
        ax.plot([x, x + .12], [.8, .62], color=I, lw=.9)
    ax.plot([1.55, 1.55], [.8, 3.95], color='#8a6a44', lw=4.5)
    for yy, ww in ((2.3, 1.2), (3.0, .95), (3.6, .7)):
        ax.plot([1.55, 1.55 - ww], [yy, yy + .32], color='#8a6a44', lw=1.8)
        ax.plot([1.55, 1.55 + ww], [yy, yy + .32], color='#8a6a44', lw=1.8)
    for y, s, col, ls in ((1.45, r'$5.9$ m: capillary', T, '-'),
                          (2.35, r'$10.3$ m: suction', R, '--'),
                          (3.9, r'$100$ m$+$: tension', I, ':')):
        ax.plot([.4, 7.6], [y, y], color=col, lw=.9, ls=ls)
        txt(ax, 4.1, y + .09, s, fontsize=7.2, color=col)
    txt(ax, .45, 4.22, 'three different ceilings', fontsize=8.0, color=T)
    txt(ax, 3.55, .42, 'xylem: 2.5 micron radius', fontsize=7.0, color=G)

    b = panel(fig, [.46, .20, .51, .62], xlim=(0, 130), ylim=(-1.7, .35))
    h = np.linspace(0, 130, 300)
    b.plot(h, -9.8 * h / 1e6, color=I, lw=2.0)
    b.axhline(0, color=G, lw=.8, ls=':')
    b.plot([10.3], [-.10], 'o', ms=4, color=R)
    b.plot([112], [-1.10], 'o', ms=4, color=T)
    b.annotate('p = 0: suction limit', xy=(10.3, -.10), xytext=(24, .05), fontsize=7.4,
               color=R, arrowprops=dict(arrowstyle='->', color=R, lw=.8))
    b.annotate('redwood 112 m: water in tension', xy=(112, -1.10), xytext=(24, -1.45),
               fontsize=7.4, color=T, arrowprops=dict(arrowstyle='->', color=T, lw=.8))
    b.fill_between([10.3, 130], -1.7, 0, color='#eaf4f8', alpha=.55)
    axes2(b, r'height $h$ (m)', r'$p-p_0$ (MPa)')
    b.set_yticks([-1.5, -1, -.5, 0])
    return 'A tree beats capillary and suction limits by holding the water column in tension'


# --------------------------------------------------------- 26. shallow water
def _shallow_wave(fig):
    a = panel(fig, [.02, .06, .48, .86], equal=True, xlim=(0, 9.8), ylim=(.2, 4.4))
    ax = a
    xb = np.linspace(3.0, 6.6, 300)
    top = 2.85 + .65 * np.exp(-((xb - 4.8) / 1.05) ** 2)
    ax.add_patch(Rectangle((.3, .8), 9.2, 2.05, fc=WATER, ec='none'))
    waterpoly(ax, list(zip(xb, top)) + [(6.6, 2.85), (3.0, 2.85)], fc=WATER)
    ax.plot([.3, 3.0], [2.85, 2.85], color=T, lw=2.0)
    ax.plot(xb, top, color=T, lw=2.0)
    ax.plot([6.6, 9.5], [2.85, 2.85], color=T, lw=2.0)
    ax.plot([.3, 9.5], [.8, .8], color=I, lw=2.0)
    arrow(ax, (.7, 2.35), (1.8, 2.35), T, 1.8)
    txt(ax, .75, 2.05, r'$c$', fontsize=9.0)
    arrow(ax, (5.2, 2.35), (6.2, 2.35), T, 1.4)
    txt(ax, 5.25, 2.05, r"$c'$", fontsize=9.0)
    dimy(ax, 2.55, .8, 2.85, r'$h$')
    dimy(ax, 7.1, 2.85, 3.50, r'$\eta$')
    head(ax, 'wave frame: the flow is steady', T)
    foot(ax, r"continuity $ch=c'(h+\eta)$, then momentum")

    b = panel(fig, [.55, .20, .43, .62], xlim=(0, 12), ylim=(0, 11.5))
    h = np.linspace(0, 12, 200)
    b.plot(h, np.sqrt(9.8 * h), color=I, lw=2.0)
    for hh in (1, 4, 9):
        b.plot([hh], [np.sqrt(9.8 * hh)], 'o', ms=3.4, color=T)
    b.annotate(r'$v=\sqrt{gh}$', xy=(9, 9.39), xytext=(2.0, 7.4), fontsize=9.0,
               arrowprops=dict(arrowstyle='->', color=T, lw=.9))
    b.text(1.1, 2.6, '1 m: 3.1 m/s', fontsize=7.0, color=G)
    b.text(6.6, 2.0, '9 m: 9.4 m/s', fontsize=7.0, color=G)
    axes2(b, r'depth $h$ (m)', r'$v$ (m/s)')
    return 'Shallow-water speed sqrt(gh) is continuity plus momentum in the wave frame'


# ------------------------------------------------------------- 27. sprinkler
def _sprinkler(fig):
    a = panel(fig, [.02, .06, .46, .86], equal=True, xlim=(-3.4, 3.4), ylim=(.2, 4.4))
    ax = a
    ax.add_patch(Circle((0, 1.7), .22, fc='#e6ecee', ec=I, lw=1.4))
    for sgn in (-1, 1):
        ax.plot([0, sgn * 2.3], [1.7, 2.6], color=I, lw=2.4)
        ax.add_patch(Circle((sgn * 2.3, 2.6), .14, fc=I))
        arrow(ax, (sgn * 1.6, 2.25), (sgn * 2.9, 2.95), T, 1.6)
        arrow(ax, (sgn * 2.1, 2.45), (sgn * 1.25, 1.85), R, 1.4)
    txt(ax, 2.3, 3.15, 'outflow', fontsize=7.4, color=T, ha='center')
    txt(ax, 2.0, 1.45, r'$-\dot m v$', fontsize=8.0, color=R, ha='center')
    ax.add_patch(Arc((0, 1.7), .9, .9, theta1=10, theta2=80, color=G, lw=1.1))
    txt(ax, .45, 2.10, r'$\tau$', fontsize=8.6, color=G)
    head(ax, 'ejection: reaction torque', T)

    b = panel(fig, [.51, .06, .46, .86], equal=True, xlim=(-3.4, 3.4), ylim=(.2, 4.4))
    bx = b
    bx.add_patch(Circle((0, 1.7), .22, fc='#e6ecee', ec=I, lw=1.4))
    for sgn in (-1, 1):
        bx.plot([0, sgn * 2.3], [1.7, 2.6], color=I, lw=2.4)
        arrow(bx, (sgn * 3.0, 3.0), (sgn * 2.2, 2.55), T, 1.5)
    txt(bx, 0, 3.5, 'suction: ideal torque is zero', fontsize=8.0, ha='center', color=T)
    txt(bx, 0, 1.05, 'inlet pressure balances the momentum', fontsize=7.2,
        ha='center', color=G)
    txt(bx, 0, .55, 'real: dissipation leaves a slow creep', fontsize=7.2,
        ha='center', color=R)
    return 'Ejection makes thrust; ideal suction makes none, and dissipation decides the real answer'


# ------------------------------------------------------ 28. rotating energy
def _rotating_energy(fig):
    a = panel(fig, [.02, .06, .44, .86], equal=True, xlim=(0, 9.6), ylim=(.2, 4.4))
    ax = a
    ax.add_patch(Rectangle((1.2, .8), .8, 2.5, fc=WATER, ec='none'))
    ax.add_patch(Rectangle((1.2, .8), 6.0, .8, fc=WATER, ec='none'))
    ax.add_patch(Rectangle((6.4, .8), .8, 1.9, fc=WATER, ec='none'))
    ax.plot([1.2, 1.2], [.8, 3.4], color=I, lw=2.0)
    ax.plot([2.0, 2.0], [.8, 2.0], color=I, lw=2.0)
    ax.plot([6.4, 6.4], [.8, 2.8], color=I, lw=2.0)
    ax.plot([7.2, 7.2], [.8, 3.4], color=I, lw=2.0)
    ax.plot([1.2, 7.2], [.8, .8], color=I, lw=2.0)
    ax.plot([1.2, 7.2], [1.6, 1.6], color=I, lw=1.2)
    ax.plot([1.2, 2.0], [3.3, 3.3], color=T, lw=2.2)
    ax.plot([6.4, 7.2], [2.7, 2.7], color=T, lw=2.2)
    dimx(ax, 1.6, 4.0, 3.62, r'$r_1$')
    dimx(ax, 1.6, 7.2, 1.20, r'$r_2$')
    arrow(ax, (7.2, 3.65), (8.4, 3.65), G, 1.5)
    txt(ax, 7.5, 3.80, r'$\omega$', fontsize=8.8, color=G)
    txt(ax, 4.2, 4.22, r'$\omega$ held constant by the motor', fontsize=7.8, color=T, ha='center')
    foot(ax, r'$p_2-p_1=\frac{1}{2}\rho\omega^2(r_2^2-r_1^2)$')

    b = panel(fig, [.50, .06, .48, .86], xlim=(0, 10), ylim=(0, 10))
    b.axis('off')
    b.text(.15, 9.4, 'the same 0.40 J, three bookkeepers', fontsize=8.4, color=T)
    for i, (lab, col) in enumerate([('kinetic energy gained', T),
                                    ('work by the motor', G),
                                    ('pseudo-work, rotating frame', GOLD)]):
        y = 7.6 - i * 2.0
        b.add_patch(Rectangle((.15, y - .45), 4.6, .75, fc=col, alpha=.55))
        b.text(.15, y + .48, lab, fontsize=7.6)
        b.text(5.0, y - .15, '0.40 J', fontsize=8.2, color=col)
    b.text(.15, 1.2, 'The pseudo-work is the motor work', fontsize=7.4, color=G)
    b.text(.15, .65, 'seen from the rotating frame.', fontsize=7.4, color=G)
    return 'In a rotating frame the centrifugal head is a pump, and the motor pays for it'


# ----------------------------------------------------------- 29. viscometer
def _viscometer(fig):
    a = panel(fig, [.03, .06, .32, .86], equal=True, xlim=(0, 6.0), ylim=(.2, 4.4))
    ax = a
    ax.add_patch(Rectangle((.8, .5), 3.2, 3.6, fc='#eaf4f8', ec=I, lw=1.8))
    ax.plot([.8, 4.0], [3.6, 3.6], color=T, lw=1.4)
    ax.add_patch(Circle((2.4, 3.15), .28, fc='#cfd8db', ec=I, lw=1.3))
    arrow(ax, (2.4, 2.95), (2.4, 2.20), G, 1.3)
    txt(ax, 2.52, 2.55, r'$v_t$', fontsize=8.2, color=G)
    for y, lab in ((2.65, 'top mark'), (1.15, 'lower mark')):
        ax.plot([1.0, 3.8], [y, y], color=R, lw=.9, ls=':')
        txt(ax, 3.95, y + .12, lab, fontsize=6.6, color=R, ha='right')
    dimy(ax, 4.35, 1.15, 2.65, '20 cm')
    txt(ax, .95, 4.28, 'glycerine, steel spheres', fontsize=7.6, color=T)
    foot(ax, r'$v_{true}=v_{meas}(1+2.4r/R)$')

    b = panel(fig, [.39, .20, .57, .62], xlim=(0, 10), ylim=(0, 1.1))
    t = np.linspace(0, 10, 400)
    b.plot(t, 1 - np.exp(-2.2 * t), color=I, lw=2.0)
    b.plot([0, 10], [1, 1], color=T, lw=.9, ls='--')
    b.axvspan(2.4, 4.4, color=YEL, alpha=.55)
    b.text(2.5, .20, 'time the', fontsize=7.0)
    b.text(2.5, .09, 'middle third', fontsize=7.0)
    b.text(5.8, .62, 'terminal speed', fontsize=7.4, color=T)
    b.text(5.8, .40, r'Re $=0.10$: Stokes honest', fontsize=7.2, color=T)
    axes2(b, r'time (s, schematic)', r'$v/v_t$')
    b.set_yticks([0, .5, 1])
    return 'A viscometer is a prediction plus two regime checks: small Re and a wall correction'


# ------------------------------------------------------------ 30. regime map
def _regime_map(fig):
    a = panel(fig, [.01, .02, .98, .94], xlim=(0, 20), ylim=(0, 5))
    ax = a
    ax.axis('off')
    txt(ax, .12, 4.78, 'what is the fluid doing?', fontsize=8.8, color=T)
    boxes = [
        ('1  at rest / rigid accel', r'$p=\rho g h$;  manometer;  $g_{eff}$', 'hydrostatics'),
        ('2  float / sink / level', r'$F_b=\rho_fV_{disp}g$', 'displaced-volume ledger'),
        ('3  flow, short device', r'$p+\frac{1}{2}\rho v^2+\rho gy$', 'four gates'),
        ('4  long narrow pipe', r'$Q=\pi R^4\Delta p/8\eta L$', 'hydraulic network'),
        ('5  jet / thrust', r'$F=\rho a v^2$', 'momentum flux'),
        ('6  mm scale: drops, tubes', r'$2\gamma/r,\ 4\gamma/r$;  Jurin', 'gamma family'),
    ]
    for i, (h, eq, tag) in enumerate(boxes):
        col, row = i % 3, i // 3
        x = .15 + col * 6.55
        y = 2.75 - row * 1.65
        ax.add_patch(Rectangle((x, y), 6.15, 1.42, fc=PALE, ec='#cfe1dc', lw=1.2))
        txt(ax, x + .22, y + 1.06, h, fontsize=7.8)
        txt(ax, x + .22, y + .60, eq, fontsize=7.6, color=T)
        txt(ax, x + .22, y + .18, r'$\rightarrow$ ' + tag, fontsize=7.0, color=G)
    txt(ax, .12, .42, 'where the model dies:', fontsize=7.2, color=R)
    txt(ax, 2.6, .42, 'turbulence  ·  unsteady surfaces  ·  compressibility  ·  '
        'non-Newtonian  ·  sub-micron no-slip', fontsize=7.0, color=G)
    return 'Six boxes triage every fluid item; each carries its equation and its tool'


def figure(ax, key):
    fig = ax.figure
    ax.axis('off')
    build = {
        'pressure_wedge': _pressure_wedge, 'manometer_walk': _manometer_walk,
        'plane_force': _plane_force, 'curved_gate': _curved_gate,
        'accel_tank': _accel_tank, 'rotating_paraboloid': _rotating_paraboloid,
        'buoyancy': _buoyancy, 'stability': _stability, 'ice_cases': _ice_cases,
        'bernoulli_streamtube': _bernoulli_streamtube, 'venturi_pitot': _venturi_pitot,
        'torricelli': _torricelli, 'jet_thrust': _jet_thrust,
        'poiseuille_profile': _poiseuille_profile, 'hydraulic_network': _hydraulic_network,
        'stokes_regime': _stokes_regime, 'surface_energy': _surface_energy,
        'excess_pressure': _excess_pressure, 'jurin': _jurin,
        'drain_two_regimes': _drain_two_regimes,
        'paraboloid_three_ways': _paraboloid_three_ways, 'raindrop': _raindrop,
        'young_laplace_patch': _young_laplace_patch, 'drop_strider': _drop_strider,
        'tree_suction': _tree_suction, 'shallow_wave': _shallow_wave,
        'sprinkler': _sprinkler, 'rotating_energy': _rotating_energy,
        'viscometer': _viscometer, 'regime_map': _regime_map,
    }
    if key not in build:
        raise ValueError(key)
    return build[key](fig)
