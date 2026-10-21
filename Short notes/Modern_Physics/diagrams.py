"""Native analytical diagrams for the modern-physics short notes.

Rule of the sheet: one wide figure per page, at most two panels, at most six
labels per panel, every label placed in whitespace rather than on the drawing.
Everything here is a closed-form curve or a labelled geometry: level ladders,
spectra, kinematics triangles, log scales. No decorative imagery.
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
    """Axis furniture placed in points, not axes fractions.

    A fraction of the panel height is a different number of pixels on a tall
    band and a short one; offsets in points keep the label clear of the tick
    numbers whatever the band height turns out to be.
    """
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


def beaker(ax, x0, x1, y0, y1, lw=2.0):
    ax.plot([x0, x0], [y0, y1], color=I, lw=lw)
    ax.plot([x1, x1], [y0, y1], color=I, lw=lw)
    ax.plot([x0, x1], [y0, y0], color=I, lw=lw)


def waterpoly(ax, pts, fc=WATER, ec='none', lw=0, z=0):
    ax.add_patch(Polygon(pts, closed=True, fc=fc, ec=ec, lw=lw, zorder=z))


from matplotlib.patches import FancyArrowPatch

TICK = dict(labelsize=7.4, length=3, pad=2)


def ladder(ax, x, levels, w=0.9, color=I, lw=1.8):
    for y in levels:
        ax.plot([x - w / 2, x + w / 2], [y, y], color=color, lw=lw)


def down_arrow(ax, x, y0, y1, color=T, lw=1.2, ls='-'):
    arrow(ax, (x, y0), (x, y1), color, lw, '-|>', 6)


def logaxis(ax, xlabel, ylabel, logx=True, logy=False):
    ax.axis('on')
    if logx:
        ax.set_xscale('log')
    if logy:
        ax.set_yscale('log')
    ax.spines[['top', 'right']].set_visible(False)
    ax.tick_params(**TICK)
    ax.grid(alpha=.12, lw=.7, which='both')
    ax.annotate(xlabel, xy=(.5, 0), xycoords='axes fraction', xytext=(0, -21),
                textcoords='offset points', ha='center', va='top',
                fontsize=7.6, color=I)
    if ylabel:
        ax.annotate(ylabel, xy=(0, .5), xycoords='axes fraction', xytext=(-28, 0),
                    textcoords='offset points', ha='center', va='center',
                    rotation=90, fontsize=7.6, color=I)


# ------------------------------------------------------------ 01 Thomson/Rutherford
def _thomson_vs_rutherford(fig):
    a = panel(fig, [.02, .04, .45, .90], xlim=(0, 10), ylim=(0, 4.6))
    a.add_patch(Circle((5.0, 2.35), 1.15, fc='#f4e6e4', ec=R, lw=1.2, alpha=.8))
    for e in ((4.5, 2.6), (5.4, 2.1), (4.8, 1.9), (5.5, 2.7), (5.1, 2.35)):
        a.add_patch(Circle(e, .09, fc=I, ec='none'))
    for y in (3.35, 2.75, 2.15, 1.55):
        arrow(a, (.5, y), (7.6, y + .06), '#9fc7d3', 1.0, '-|>', 6)
    txt(a, 7.0, 3.55, 'all nearly straight', fontsize=7.8, color=G)
    txt(a, .4, .35, 'Thomson: charge spread over 10^-10 m', fontsize=8.0, color=I)
    head(a, 'a soft cloud cannot turn a fast alpha')

    b = panel(fig, [.52, .04, .45, .90], xlim=(0, 10), ylim=(0, 4.6))
    b.add_patch(Circle((5.0, 2.3), .16, fc=R, ec='none'))
    for y in (3.6, 3.1, 2.55):
        arrow(b, (.6, y), (4.75, 2.35 + (y - 2.55) * .18), '#9fc7d3', 1.0, '-|>', 6)
        arrow(b, (5.25, 2.35 + (y - 2.55) * .18), (9.3, y + .05), '#9fc7d3', 1.0, '-|>', 6)
    ts = np.linspace(0, 1, 60)
    b.plot(1.0 + 3.9 * ts, 1.35 + .55 * ts ** 2, color=T, lw=1.6)
    b.plot(1.0 + 3.9 * ts, 1.35 + .55 * (1 - ts) ** 2, color=T, lw=1.6)
    arrow(b, (2.2, 1.42), (1.05, 2.85), T, 1.4, '-|>', 7)
    txt(b, 1.15, 3.15, 'back-scatter: 1 in 8000', fontsize=7.8, color=T)
    txt(b, .4, .35, 'Rutherford: one point charge, sin^-4 law', fontsize=8.0, color=I)
    head(b, 'a point charge can turn it around')
    return 'Same beam, two predictions: the rare back-scatter is the test that decides'


# --------------------------------------------------------------- 02 closest approach
def _closest_approach(fig):
    """Rutherford hyperbola with the nucleus at the inner focus.

    The perpendicular from the focus to the incoming asymptote is b; the vertex
    of the hyperbola is r_min. Both come off the drawn curve, so the picture and
    the algebra cannot drift apart.
    """
    a = panel(fig, [.03, .04, .44, .90], xlim=(0, 10), ylim=(0, 4.6), equal=True)
    e, p_ = 2.0, 3.0
    phi = np.linspace(-2.06, 2.06, 700)          # stops just short of the asymptote
    r = p_ / (1 + e * np.cos(phi))
    P = np.stack([r * np.cos(phi), r * np.sin(phi)])
    d = P[:, 1] - P[:, 0]
    ang = np.arctan2(d[1], d[0])
    Rm = np.array([[np.cos(-ang), -np.sin(-ang)], [np.sin(-ang), np.cos(-ang)]])
    Q = Rm @ P                                   # incoming asymptote now horizontal
    ox, oy, sc = 2.45, 1.20, .74
    X, Y = ox + sc * Q[0], oy + sc * Q[1]
    keep = (X > -.3) & (X < 10.3) & (Y > -.3) & (Y < 4.9)
    a.plot(X[keep], Y[keep], color=T, lw=1.7)
    ya = oy + sc * Q[1, 0]
    a.plot([.12, ox], [ya, ya], color=G, lw=.9, ls=(0, (5, 4)))
    a.annotate('', xy=(ox, oy + .05), xytext=(ox, ya + .02),
               arrowprops=dict(arrowstyle='<->', color=G, lw=.9))
    a.add_patch(Circle((ox, oy), .11, fc=R, ec='none'))
    txt(a, ox - .60, (oy + ya) / 2 - .12, r'$b$', fontsize=9.2, color=G)
    i = int(np.argmin(np.hypot(X - ox, Y - oy)))
    a.plot([ox, X[i]], [oy, Y[i]], color=R, lw=.8)
    txt(a, X[i] - 1.05, Y[i] + .30, r'$r_{min}$', fontsize=8.8, color=R)
    j = int(.86 * (len(X) - 1))
    a.annotate('deflected through ' + r'$\theta$', xy=(X[j], Y[j]),
               xytext=(X[j] - 1.9, Y[j] + 1.05), fontsize=8.2, color=T,
               arrowprops=dict(arrowstyle='->', color=T, lw=.9))
    txt(a, .18, ya - .42, 'incoming asymptote: the path if there were no force',
        fontsize=7.6, color=G)
    txt(a, .18, 4.20, 'the alpha rides a Coulomb hyperbola', fontsize=8.4, color=T)

    b = panel(fig, [.50, .20, .48, .68])
    logaxis(b, r'alpha energy  $K$  (MeV)', r'$r_{min}$  (fm)')
    K = np.logspace(.5, 2, 200)
    b.loglog(K, 2 * 79 * 1.44e-3 / K * 1e3, color=T, lw=2.0)
    b.axvline(32, color=R, lw=1.2, ls=(0, (4, 3)))
    b.text(1.0, 5.0, 'nuclear surface reached', fontsize=7.4, color=R)
    b.plot([5], [2 * 79 * 1.44e-3 / 5 * 1e3], 'o', ms=6, color=GOLD, zorder=5)
    b.annotate('5 MeV: 45 fm', xy=(5, 45), xytext=(6.5, 200), fontsize=7.8,
               color=GOLD, arrowprops=dict(arrowstyle='->', color=GOLD, lw=.9))
    b.set_xlim(.5, 100); b.set_ylim(1.5, 500)
    return 'r_min is a head-on upper bound on the nuclear size, not a radius measurement'


# ------------------------------------------------------------- 03 standing wave
def _standing_wave(fig):
    a = panel(fig, [.02, .04, .45, .90], xlim=(0, 10), ylim=(0, 4.6), equal=True)
    th = np.linspace(0, 2 * np.pi, 600)
    a.plot(5.0 + 1.95 * np.cos(th), 1.95 + 1.95 * np.sin(th), color='#cfe1dc', lw=1.0)
    a.plot(5.0 + 1.60 * np.cos(th), 1.95 + 1.60 * np.sin(th), color=T, lw=2.0)
    for k in range(3):
        ang = k * 2 * np.pi / 3
        a.add_patch(Circle((5.0 + 1.60 * np.cos(ang), 1.95 + 1.60 * np.sin(ang)),
                           .075, fc=R, ec='none'))
    txt(a, 5.0, 4.28, '3 whole wavelengths close in phase', fontsize=8.0,
        color=T, ha='center')
    txt(a, .35, .55, r'$2\pi r=n\lambda$', fontsize=9.6)

    b = panel(fig, [.52, .04, .45, .90], xlim=(0, 10), ylim=(0, 4.6), equal=True)
    b.plot(5.0 + 1.95 * np.cos(th), 1.95 + 1.95 * np.sin(th), color='#cfe1dc', lw=1.0)
    th2 = np.linspace(0, 2 * np.pi, 600)
    rr = 1.60 * (1 + .10 * np.cos(2.6 * th2))
    b.plot(5.0 + rr * np.cos(th2), 1.95 + rr * np.sin(th2), color=R, lw=2.0)
    b.plot([5.0 + 1.60, 6.55], [1.95, 1.95], color=R, lw=1.1, ls=(0, (4, 3)))
    b.add_patch(Circle((7.55, 3.55), .55, fc='none', ec=R, lw=1.1))
    b.plot([7.15, 7.95], [3.95, 3.15], color=R, lw=1.5)
    b.plot([7.15, 7.95], [3.15, 3.95], color=R, lw=1.5)
    txt(b, 5.0, 4.28, 'fractional n: destructive overlap', fontsize=8.0, color=R, ha='center')
    txt(b, .35, .55, 'no closed wave, no orbit', fontsize=8.4, color=R)
    return 'Bohr quantisation is a standing-wave condition: L = n h-bar is 2 pi r = n lambda'


# ---------------------------------------------------------------- 04 Bohr ledger
def _bohr_ledger(fig):
    a = panel(fig, [.03, .10, .94, .80], xlim=(0, 10), ylim=(-16.4, 5.2))
    lev = [(1, -13.6, 0.53), (2, -3.40, 2.12), (3, -1.51, 4.76)]
    for n, e, r in lev:
        a.plot([.9, 3.9], [e, e], color=I, lw=2.0)
        a.plot([4.9, 7.2], [e, e], color='#cfe1dc', lw=1.6)
        txt(a, 4.0, e - .30, f'n={n}', fontsize=8.4, color=G)
        txt(a, 7.32, e - .30, f'r={r:.2f} A', fontsize=8.0, color=T)
        txt(a, 8.95, e - .30, f'{e:g} eV', fontsize=8.0, color=G)
    a.plot([.9, 3.9], [0, 0], color=R, lw=1.2, ls=(0, (4, 3)))
    txt(a, 4.0, -.30, 'n=inf', fontsize=8.4, color=R)
    txt(a, 8.95, -.30, '0', fontsize=8.0, color=R)
    a.annotate('', xy=(1.9, -3.40), xytext=(1.9, -13.6),
               arrowprops=dict(arrowstyle='-|>', color=R, lw=1.6))
    txt(a, .95, -8.9, '121.6 nm', fontsize=8.2, color=R)
    a.annotate('', xy=(3.1, -1.51), xytext=(3.1, -3.40),
               arrowprops=dict(arrowstyle='-|>', color=T, lw=1.6))
    txt(a, 3.2, -2.45, '656 nm', fontsize=8.2, color=T)
    txt(a, .9, 3.05, r'$E_n=-13.6\,Z^2/n^2$ eV', fontsize=9.4)
    txt(a, 4.0, 3.05, 'level', fontsize=7.8, color=G)
    txt(a, 7.2, 3.05, 'radius', fontsize=7.8, color=T)
    txt(a, 8.8, 3.05, 'energy', fontsize=7.8, color=G)
    head(a, 'one ladder: radius, energy and the two visible arrows')
    return 'One formula per column: radius grows as n squared, binding falls as 1/n squared'


# -------------------------------------------------------------- 05 series
def _spectrum_series(fig):
    a = panel(fig, [.03, .18, .94, .62], xlim=(80, 2000), ylim=(-.1, 4.6))
    a.set_xscale('log')
    a.axis('off')
    series = [('Lyman  n->1', 1, [121.6, 102.6, 97.3, 95.0, 93.8], 3.6, T),
              ('Balmer  n->2', 2, [656.3, 486.1, 434.0, 410.2, 397.0], 2.5, R),
              ('Paschen  n->3', 3, [1875, 1282, 1094, 1005, 954], 1.4, GOLD)]
    for name, nf, lines, y, c in series:
        a.axhline(y, color='#dfe9ea', lw=.8, xmin=0, xmax=1)
        for w in lines:
            a.plot([w, w], [y - .30, y + .30], color=c, lw=2.4)
        a.text(84, y + .42, name, fontsize=8.0, color=c)
    a.axvspan(380, 750, color='#fff6d6', alpha=.55, zorder=0)
    a.text(470, 1.02, 'visible', fontsize=7.6, color=GOLD)
    for w in (656.3, 486.1, 434.0):
        a.text(w, .55, f'{w:.0f}', fontsize=7.2, color=R, ha='center')
    a.set_ylim(0, 4.6)
    head(a, 'one ladder, three series, one visible window')
    return 'Every series is the same Rydberg rule with a different finishing rung'


# --------------------------------------------------------------- 06 excitation
def _excitation_ladder(fig):
    a = panel(fig, [.03, .10, .40, .84], xlim=(0, 10), ylim=(-.2, 4.6))
    ys = [0.0, 1.6, 2.6, 3.2, 3.55]
    for i, (y, lab) in enumerate(zip(ys, ['n=1', 'n=2', 'n=3', 'n=4', 'n=inf'])):
        a.plot([1.6, 4.6], [y, y], color=I, lw=1.8)
        txt(a, 4.75, y - .13, lab, fontsize=7.8, color=G)
    for y, e in zip(ys[1:], ['10.2 eV', '12.09', '12.75', '13.6']):
        txt(a, 1.65, y + .10, e, fontsize=7.4, color=T)
    arrow(a, (.55, -.05), (.55, 2.62), R, 1.8, '-|>', 8)
    txt(a, .65, 1.15, '12.5 eV', fontsize=8.2, color=R, rotation=90)
    a.plot([.75, 4.6], [2.60, 2.60], color=R, lw=1.0, ls=(0, (4, 3)))
    txt(a, .55, 3.95, 'stops at n=3', fontsize=8.2, color=R)
    txt(a, .55, .45, 'a 12.5 eV electron', fontsize=8.0)
    txt(a, .55, 4.35, 'electron beam: any gift up to full', fontsize=7.8, color=G)

    b = panel(fig, [.52, .12, .44, .80], xlim=(0, 10), ylim=(0, 4.6))
    for k, (lab, col, dy) in enumerate([('11.0 eV photon', R, 1.5),
                                       ('12.2 eV photon', T, 2.6)]):
        b.add_patch(Polygon([(.8 + k * 4.4, dy - .5),
                                                          (3.4 + k * 4.4, dy - .5),
                                                          (3.4 + k * 4.4, dy + .5),
                                                          (.8 + k * 4.4, dy + .5)],
                                                         closed=True, fc='none', ec=col, lw=1.3))
        txt(b, .95 + k * 4.4, dy + .68, lab, fontsize=7.8, color=col)
    txt(b, .95, .62, 'too small: nothing', fontsize=7.6, color=R)
    txt(b, 5.55, 2.15, 'fits: n=3', fontsize=7.8, color=T)
    txt(b, .6, 3.7, 'photon: all or nothing', fontsize=8.2, color=G)
    txt(b, .6, .25, 'the toll is 10.2 eV; surplus becomes kinetic energy', fontsize=7.6, color=G)
    return 'Electrons may pay in part; photons must pay in full - that is the excitation asymmetry'


# ------------------------------------------------------------- 07 hydrogenic
def _hydrogenic_scaling(fig):
    a = panel(fig, [.03, .10, .45, .80], xlim=(0, 10), ylim=(-135, 34))
    for x, z, name, c in ((2.0, 1, 'H', T), (4.9, 4, 'He+', GOLD), (7.8, 9, 'Li2+', R)):
        for n in (1, 2, 3):
            e = -13.6 * z / n ** 2
            a.plot([x - 1.05, x + 1.05], [e, e], color=c, lw=1.8)
        txt(a, x - 1.05, -13.6 * z - 15, f'{13.6*z:.0f} eV', fontsize=8.0, color=c)
        txt(a, x - 1.05, 14, name, fontsize=9.4, color=c)
    a.annotate('', xy=(1.9, -3.4), xytext=(1.9, -13.6),
               arrowprops=dict(arrowstyle='-|>', color=T, lw=1.3))
    txt(a, .25, -9.4, '10.2 eV', fontsize=7.6, color=T)
    a.annotate('', xy=(4.8, -13.6), xytext=(4.8, -54.4),
               arrowprops=dict(arrowstyle='-|>', color=GOLD, lw=1.3))
    txt(a, 3.35, -36, '40.8 eV', fontsize=7.6, color=GOLD)
    a.annotate('', xy=(7.7, -30.6), xytext=(7.7, -122.4),
               arrowprops=dict(arrowstyle='-|>', color=R, lw=1.3))
    txt(a, 8.1, -80, r'$Z^2$', fontsize=9.0, color=R)
    head(a, 'same ladder, stretched by Z squared')

    b = panel(fig, [.53, .10, .43, .82], xlim=(0, 10), ylim=(0, 4.6))
    b.add_patch(Circle((3.0, 2.5), 1.45, fc='none', ec=T, lw=1.6))
    b.add_patch(Circle((3.0, 2.5), .10, fc=I, ec='none'))
    b.add_patch(Circle((7.2, 2.5), 1.45, fc='none', ec=GOLD, lw=1.6, ls=(0, (5, 3))))
    b.add_patch(Circle((7.2, 2.5), .10, fc=I, ec='none'))
    txt(b, 1.85, .65, 'H: 0.529 A', fontsize=8.2, color=T)
    txt(b, 5.75, .65, 'D: 0.529 A', fontsize=8.2, color=GOLD)
    txt(b, 2.75, 3.95, r'$\mu=\frac{m_eM}{m_e+M}$', fontsize=9.4)
    txt(b, .35, 4.35, 'the nucleus is not nailed down', fontsize=8.6, color=T)
    foot(b, 'mass moves the ladder by 0.05 %')
    return 'Z squared deepens the ladder; the reduced mass shifts every rung by a part in 10^4'


# ---------------------------------------------------------- 08 quantum numbers
def _quantum_numbers(fig):
    a = panel(fig, [.03, .10, .40, .84], xlim=(0, 10), ylim=(0, 4.6))
    rows = [(3, '3s', 1), (3, '3p', 3), (3, '3d', 5), (2, '2s', 1), (2, '2p', 3), (1, '1s', 1)]
    for i, (n, lab, cnt) in enumerate(rows):
        y = 4.1 - i * .55
        txt(a, .5, y, lab, fontsize=8.2, color=T)
        for k in range(cnt):
            a.add_patch(Rectangle((1.5 + k * .62, y - .16), .46, .32, fc='#e7f4f1', ec=T, lw=.9))
            a.add_patch(Circle((1.73 + k * .62, y), .05, fc=I, ec='none'))
        txt(a, 1.5 + cnt * .62 + .2, y, f'{2*cnt}', fontsize=7.4, color=G)
    txt(a, 6.1, 4.1, 'orbitals', fontsize=7.6, color=G)
    txt(a, 8.6, 4.1, 'e- slots', fontsize=7.6, color=G)
    txt(a, .45, .25, 'n, l, m_l, m_s: 2n^2 states in shell n', fontsize=7.8, color=G)

    b = panel(fig, [.52, .12, .44, .80], xlim=(0, 10), ylim=(0, 4.6))
    b.plot([1.0, 4.6], [2.3, 2.3], color=I, lw=2.0)
    txt(b, 1.0, 1.85, 'B = 0', fontsize=8.0, color=G)
    for k, (ml, dy) in enumerate([(-1, -1.0), (0, 0), (1, 1.0)]):
        b.plot([6.2, 9.4], [2.3 + dy, 2.3 + dy], color=T, lw=1.8)
        txt(b, 9.5, 2.3 + dy - .12, f'm={ml}', fontsize=7.6, color=T)
        b.plot([4.6, 6.2], [2.3, 2.3 + dy], color='#cfe1dc', lw=.8)
    txt(b, 6.2, 4.1, r'$\Delta E=m_l\mu_BB$', fontsize=8.6)
    txt(b, 1.0, .45, 'a magnetic field fans one level into three', fontsize=7.8, color=G)
    return 'The Bohr ladder is one quantum number; the other three decide which lines exist'


# ------------------------------------------------------------------ 09 photon
def _photon_packet(fig):
    a = panel(fig, [.03, .10, .44, .84], xlim=(0, 10), ylim=(0, 4.6))
    x = np.linspace(0, 10, 800)
    env = np.exp(-((x - 5.0) / 1.5) ** 2)
    a.plot(x, 2.3 + 1.5 * env * np.sin(10 * x), color=T, lw=1.4)
    a.plot(x, 2.3 + 1.5 * env, color='#cfe1dc', lw=1.0, ls=(0, (4, 3)))
    a.plot(x, 2.3 - 1.5 * env, color='#cfe1dc', lw=1.0, ls=(0, (4, 3)))
    txt(a, 5.1, .55, r'$E=hf,\quad p=h/\lambda$', fontsize=9.6)
    txt(a, .55, 4.15, 'one quantum: energy and momentum together', fontsize=7.8, color=G)
    head(a, 'a photon is a counted packet')

    b = panel(fig, [.53, .12, .43, .80], xlim=(0, 10), ylim=(0, 4.6))
    b.add_patch(Rectangle((1.2, 1.9), .28, 1.9, fc='#e7f4f1', ec=T, lw=1.2))
    for k, y in enumerate((2.2, 2.7, 3.2, 3.6)):
        arrow(b, (.4, y), (1.18, y), GOLD, 1.2)
    for k, y in enumerate((2.2, 2.7, 3.2, 3.6)):
        arrow(b, (1.48, y), (2.3, y), T, 1.2)
    txt(b, .35, 3.95, 'flux n = I / hf', fontsize=7.8, color=GOLD)
    txt(b, 2.45, 2.55, 'one photon, one electron', fontsize=7.6, color=T)
    txt(b, 4.6, 3.95, r'$F=\frac{P}{c}(1+R)$', fontsize=9.0)
    txt(b, 4.6, 3.15, r'$n_{vol}=\frac{I}{hfc}$', fontsize=8.4, color=G)
    txt(b, 4.6, .55, 'brighter means more packets, not bigger ones', fontsize=7.8, color=G)
    return 'Photon bookkeeping: energy per packet, and packets per second'


# ------------------------------------------------------------ 10 photoelectric
def _photoelectric_curve(fig):
    a = panel(fig, [.09, .18, .44, .72])
    axes2(a, r'frequency  $f$  ($10^{14}$ Hz)', r'$K_{max}$  (eV)')
    f = np.linspace(0, 12, 200)
    for phi, c, lab in ((2.28, T, 'Na  phi=2.28'), (4.3, R, 'Zn  phi=4.3')):
        f0 = phi / 4.1357
        kmax = 4.1357e-15 * f * 1e14 - phi
        a.plot(f, np.clip(kmax, 0, None), color=c, lw=2.0)
        if 4 < f0 < 12:
            a.plot([f0], [0], 'o', ms=4, color=c, zorder=5)
            a.text(f0 + .12, .20, f'{f0:.1f}', fontsize=7.0, color=c)
    a.set_xlim(4, 12); a.set_ylim(0, 3.1)
    a.set_xticks([4, 6, 8, 10, 12])
    a.text(4.25, 2.72, r'slope $=h/e$ for every metal', fontsize=8.0, color=G)
    a.text(7.15, 1.55, 'Na', fontsize=8.2, color=T)
    a.text(10.35, .18, 'Zn', fontsize=8.2, color=R)
    head(a, 'K_max = hf - phi')

    b = panel(fig, [.53, .10, .43, .82], xlim=(0, 10), ylim=(0, 4.6))
    b.add_patch(Rectangle((.8, .8), 4.2, 2.9, fc='#f7fafa', ec=I, lw=1.4))
    b.plot([.8, 5.0], [1.35, 1.35], color=T, lw=3.0)
    for k, x in enumerate((1.6, 2.4, 3.2, 4.0)):
        arrow(b, (x, 1.55), (x + .35, 2.55), T, 1.1, '-|>', 6)
    arrow(b, (5.2, 3.15), (4.35, 3.15), GOLD, 1.6, '-|>', 7)
    txt(b, 5.35, 3.0, r'$hf$', fontsize=8.6, color=GOLD)
    txt(b, 1.0, 4.05, 'one photon in, one electron out', fontsize=7.8, color=G)
    txt(b, 5.7, 2.1, r'$K_{max}=hf-\phi$', fontsize=9.0)
    txt(b, 5.7, 1.25, r'$\phi$ = escape toll', fontsize=8.2, color=G)
    txt(b, .8, .45, 'deeper electrons lose more on the way out', fontsize=7.6, color=G)
    return 'Einstein equation: the photon pays a toll, the rest becomes kinetic energy'


# --------------------------------------------------------------- 11 stopping
def _stopping_graph(fig):
    a = panel(fig, [.09, .16, .44, .74])
    axes2(a, r'collector voltage  $V$  (V)', r'photocurrent  $I$')
    v = np.linspace(-2.0, 6, 400)
    for scale, c, lab in ((1.0, T, 'I'), (2.2, R, '2I')):
        cur = scale * (1 - np.exp(-(v + 1.5).clip(0) * 1.2))
        cur[v < -1.5] = 0
        a.plot(v, cur, color=c, lw=2.0)
        a.text(4.4, scale * .86, lab, fontsize=8.2, color=c)
    a.axvline(-1.5, color=G, lw=.9, ls=(0, (4, 3)))
    a.text(-1.45, 1.55, r'$-V_s$', fontsize=8.4, color=G)
    a.set_xlim(-2.2, 6); a.set_ylim(0, 2.45)
    a.text(-1.9, 2.2, 'same cutoff, two plateaux', fontsize=7.8, color=G)
    head(a, 'intensity moves the height, not the edge')

    b = panel(fig, [.55, .16, .41, .78])
    axes2(b, r'frequency  $f$', r'$V_s$  (V)')
    f = np.linspace(4, 12, 100)
    b.plot(f, 4.1357e-15 * f * 1e14 - 2.28, color=T, lw=2.0)
    b.axhline(0, color=G, lw=.8)
    b.plot([5.51], [0], 'o', ms=5, color=R, zorder=5)
    b.text(5.2, .55, r'$f_0=\phi/h$', fontsize=7.8, color=R)
    b.text(6.2, 2.1, r'slope $=h/e$', fontsize=8.2, color=T)
    b.set_xlim(4, 12); b.set_ylim(-.6, 3.2)
    return 'Plot V_s against f: slope h/e, intercept -phi/e - Millikan measured h this way'


# ----------------------------------------------------------------- 12 photocell
def _photocell_iv(fig):
    a = panel(fig, [.03, .12, .46, .80], xlim=(0, 10), ylim=(0, 4.6))
    a.add_patch(Rectangle((1.0, 1.15), 7.6, 2.55, fc='#f9fbfb', ec=I, lw=1.2))
    a.plot([2.3, 2.3], [1.55, 3.35], color=T, lw=3.0)
    a.plot([7.2, 7.2], [1.55, 3.35], color=G, lw=3.0)
    for y in (1.85, 2.3, 2.75):
        arrow(a, (2.4, y), (6.9, y + .05), GOLD, 1.0, '-|>', 6)
    txt(a, 2.45, 3.45, 'emitter', fontsize=7.6, color=T)
    txt(a, 6.55, 3.45, 'collector', fontsize=7.6, color=G)
    a.plot([2.3, 1.4, 1.4, 3.6], [1.55, 1.55, .55, .55], color=I, lw=1.2)
    a.plot([7.2, 8.4, 8.4, 3.6], [1.55, 1.55, .55, .55], color=I, lw=1.2)
    a.plot([3.6, 3.6], [.35, .75], color=I, lw=1.6)
    a.plot([3.35, 3.85], [.75, .75], color=I, lw=1.6)
    a.plot([3.35, 3.85], [.35, .35], color=I, lw=1.6)
    txt(a, 4.1, .72, 'variable V', fontsize=7.6)
    a.add_patch(Circle((8.4, 2.45), .38, fc='white', ec=I, lw=1.0))
    txt(a, 8.24, 2.32, 'A', fontsize=8.0)
    txt(a, .6, 4.32, 'one battery measures both cutoff and rate', fontsize=7.8, color=G)

    b = panel(fig, [.54, .08, .42, .84], xlim=(0, 10), ylim=(0, 4.6))
    heads = ('knob', 'current', r'$V_s$')
    widths = (.35, 4.3, 8.0)
    for h, x in zip(heads, widths):
        txt(b, x, 4.05, h, fontsize=7.6, color=G)
    rows = [('intensity up', 'up', 'same'),
            ('frequency up', 'down a little', 'up'),
            ('voltage up', 'saturates', 'same')]
    for i, row in enumerate(rows):
        y = 3.35 - i * 1.15
        b.plot([.3, 9.7], [y - .42, y - .42], color='#e4edee', lw=.8)
        for j, (cell, x) in enumerate(zip(row, widths)):
            txt(b, x, y, cell, fontsize=7.4,
                color=(I if j == 0 else (T if j == 1 else R)))
    txt(b, .35, .55, 'fixed I, higher f: fewer, richer photons', fontsize=7.4, color=G)
    txt(b, .35, .12, 'so the current dips while the cutoff climbs', fontsize=7.4, color=G)
    return 'The photocell separates rate (intensity) from energy (frequency) with one battery'


# ---------------------------------------------------------------- 13 de Broglie
def _debroglie_scale(fig):
    """One log axis carrying everything from a cricket ball to green light.

    The three quantum landmarks sit within a factor of two of each other, so
    they share one bracket instead of three labels on top of one another.
    """
    a = panel(fig, [.10, .26, .84, .56])
    logaxis(a, r'wavelength  $\lambda$  (m)', '')
    a.set_yticks([])
    a.set_xticks([1e-35, 1e-30, 1e-25, 1e-20, 1e-15, 1e-10, 1e-5])
    a.set_xlim(1e-35, 1e-5); a.set_ylim(0, 4.6)
    for lam, lab, c, y, ha, dx in (
            (1e-34, 'cricket ball\n10⁻³⁴ m', R, 2.9, 'left', 1.6),
            (5.5e-7, 'green light\n5.5×10⁻⁷ m', G, 2.9, 'right', .55)):
        a.axvline(lam, color=c, lw=1.4, ls=(0, (4, 3)))
        a.text(lam * dx if ha == 'left' else lam * dx, y, lab, fontsize=7.6,
               color=c, ha=ha, va='center', linespacing=1.35)
    a.annotate('', xy=(1.4e-10, 1.55), xytext=(1.4e-10, .55),
               arrowprops=dict(arrowstyle='<->', color=T, lw=.9))
    a.axvline(1.4e-10, color=T, lw=1.2, ls=(0, (4, 3)))
    a.text(3e-11, 1.05,
           'atom spacing, 100 V electron, thermal neutron —\nall near 10⁻¹⁰ m',
           fontsize=7.6, color=T, va='center', ha='right', linespacing=1.4)
    a.text(1.5e-34, .30, 'classical: no interface this fine', fontsize=7.4, color=G)
    a.text(1e-21, 3.9, '24 decades of nothing', fontsize=7.4, color='#8fa3ad',
           ha='center')
    return 'The same formula covers a cricket ball and an electron; only the ratio to the slit decides'


# ------------------------------------------------------------- 14 Davisson-Germer
def _davisson_germer(fig):
    a = panel(fig, [.03, .08, .50, .86], xlim=(0, 10), ylim=(0, 4.6))
    for y in (1.0, 1.55, 2.1, 2.65, 3.2):
        a.plot([4.4, 8.4], [y, y], color='#cfe1dc', lw=1.0)
        for x in np.arange(4.5, 8.4, .5):
            a.add_patch(Circle((x, y), .04, fc='#b9c6cb', ec='none'))
    a.plot([.6, 4.2], [3.9, 2.6], color=I, lw=1.4)
    arrow(a, (3.0, 3.15), (4.3, 2.7), T, 1.5, '-|>', 7)
    txt(a, .55, 4.15, '54 V electrons', fontsize=7.8, color=T)
    a.plot([5.2, 8.6], [2.9, 4.1], color=R, lw=1.3)
    arrow(a, (7.2, 3.6), (8.5, 4.05), R, 1.3, '-|>', 7)
    txt(a, 7.0, 4.3, 'detector at 65 deg', fontsize=7.6, color=R)
    a.plot([4.75, 4.75], [1.55, 2.1], color=G, lw=1.0)
    a.annotate('', xy=(3.6, 3.05), xytext=(3.6, 2.2),
               arrowprops=dict(arrowstyle='<->', color=G, lw=.9))
    txt(a, 2.95, 2.55, r'$\theta$', fontsize=8.4, color=G)
    txt(a, 8.55, 2.35, r'$d$', fontsize=8.0, color=G)
    txt(a, .55, .45, r'$2d\sin\theta=n\lambda$', fontsize=9.2)
    head(a, 'a crystal is the grating for matter waves')

    b = panel(fig, [.58, .18, .38, .70])
    axes2(b, r'angle (deg)', 'intensity')
    th = np.linspace(0, 90, 400)
    i = 0.25 + np.exp(-((th - 65) / 7) ** 2) + .35 * np.exp(-((th - 25) / 12) ** 2)
    b.plot(th, i, color=T, lw=1.8)
    b.set_xlim(0, 90); b.set_ylim(0, 1.6)
    b.text(48, 1.35, 'first-order lobe', fontsize=7.6, color=T)
    return 'Davisson-Germer: the 65 degree lobe sits where 2d sin(theta) = lambda predicts'


# -------------------------------------------------------------- 15 uncertainty
def _uncertainty_well(fig):
    a = panel(fig, [.03, .10, .44, .84], xlim=(0, 10), ylim=(0, 4.6))
    x = np.linspace(0, 10, 700)
    a.plot(x, 2.7 + 1.2 * np.exp(-((x - 5) / 1.9) ** 2) * np.sin(9 * x), color=T, lw=1.2)
    a.plot(x, 2.7 + 1.2 * np.exp(-((x - 5) / 1.9) ** 2), color='#cfe1dc', lw=.9, ls=(0, (4, 3)))
    a.annotate('', xy=(3.1, 4.15), xytext=(6.9, 4.15),
               arrowprops=dict(arrowstyle='<->', color=G, lw=.9))
    txt(a, 4.85, 4.25, r'$\Delta x$', fontsize=8.4, color=G)
    txt(a, .6, 3.55, 'localise it', fontsize=7.8, color=G)
    x2 = np.linspace(0, 10, 300)
    a.plot(x2, .95 + .75 * np.exp(-((x2 - 5) / .55) ** 2) * np.sin(22 * x2), color=R, lw=1.1)
    txt(a, .6, .35, 'narrow packet: many momenta', fontsize=7.8, color=R)

    b = panel(fig, [.53, .16, .43, .76])
    axes2(b, r'radius $r$  ($10^{-10}$ m)', 'energy (eV)')
    r = np.linspace(.25, 4, 300)
    kin = 3.81 / r ** 2
    pot = -27.2 / r
    b.plot(r, kin, color=G, lw=1.6, ls=(0, (4, 3)))
    b.plot(r, pot, color=T, lw=1.6, ls=(0, (4, 3)))
    b.plot(r, kin + pot, color=R, lw=2.2)
    b.plot([.529], [-13.6], 'o', ms=6, color=GOLD, zorder=5)
    b.annotate('a0, -13.6 eV', xy=(.529, -13.6), xytext=(1.25, -4),
               fontsize=8.0, color=GOLD, arrowprops=dict(arrowstyle='->', color=GOLD, lw=.9))
    b.text(2.4, 26, 'hbar^2 / 2mr^2', fontsize=7.6, color=G)
    b.text(2.6, -22, '-ke^2 / r', fontsize=7.6, color=T)
    b.set_xlim(0, 4); b.set_ylim(-40, 60)
    return 'Squeezing costs kinetic energy: the sum has a floor, and that floor is the atom'
# --------------------------------------------------------- 16 X-ray continuous
def _xray_continuous(fig):
    a = panel(fig, [.09, .16, .44, .74])
    axes2(a, r'wavelength  $\lambda$  (pm)', 'intensity')
    for V, c, lab, off in ((30, T, '30 kV', .00), (50, R, '50 kV', .30)):
        lm = 1.24e6 / (V * 1e3)
        lam = np.linspace(lm, 140, 500)
        y = (1 - np.exp(-(lam - lm) / (6 + off))) * np.exp(-(lam - lm) / 55)
        a.plot(lam, y, color=c, lw=2.0)
        a.axvline(lm, color=c, lw=.9, ls=(0, (3, 3)), ymax=.55)
        a.text(lm - 2, -.12, f'{lm:.1f}', fontsize=7.2, color=c, ha='center')
        a.text(90, y[-1] * .92, lab, fontsize=7.8, color=c)
    a.set_xlim(0, 140); a.set_ylim(0, 1.15)
    a.text(58, 1.0, r'$\lambda_{min}=hc/eV$', fontsize=8.6)
    head(a, 'voltage sets the edge, target sets the height')

    b = panel(fig, [.55, .10, .42, .82], xlim=(0, 10), ylim=(0, 4.6))
    b.add_patch(Rectangle((.8, 1.2), 5.0, 2.2, fc='#f8fbfb', ec=I, lw=1.3))
    b.add_patch(Circle((1.6, 1.8), .35, fc=GOLD, ec=I, lw=1.0))
    b.plot([1.95, 4.6], [1.8, 2.9], color=T, lw=1.4)
    arrow(b, (4.4, 2.85), (5.1, 3.15), T, 1.3, '-|>', 6)
    txt(b, 2.2, 1.45, 'e- at eV', fontsize=7.6, color=T)
    txt(b, 4.9, 3.3, 'one photon, at most eV', fontsize=7.6, color=T)
    txt(b, .9, 3.6, 'the braking electron cannot give more than it has', fontsize=7.6, color=G)
    txt(b, 6.3, 2.4, r'$\lambda_{min}=\frac{1240}{V}\ $nm', fontsize=8.6)
    txt(b, 6.3, 1.55, r'$=\frac{1.24\times10^6}{V}$ pm', fontsize=8.2, color=G)
    txt(b, .9, .45, 'target Z changes brightness, never the cutoff', fontsize=7.6, color=G)
    return 'Duane-Hunt: the shortest X-ray is one electron spending everything at once'


# ------------------------------------------------------- 17 X-ray characteristic
def _xray_characteristic(fig):
    a = panel(fig, [.09, .16, .44, .74])
    axes2(a, r'wavelength  $\lambda$  (pm)', 'intensity')
    lam = np.linspace(20, 160, 600)
    y = (1 - np.exp(-(lam - 24) / 8)) * np.exp(-(lam - 24) / 60)
    a.plot(lam, .85 * y, color=G, lw=1.8)
    for x, h, c, lab in ((154, .55, R, 'Ka'), (139, .26, GOLD, 'Kb')):
        a.plot([x, x], [0, h + .18], color=c, lw=2.2)
        a.text(x + 2.5, h + .12, lab, fontsize=8.0, color=c)
    a.axvline(24, color=G, lw=.8, ls=(0, (3, 3)), ymax=.35)
    a.text(28, .12, r'$\lambda_{min}$', fontsize=7.6, color=G)
    a.set_xlim(15, 165); a.set_ylim(0, 1.05)
    head(a, 'lines ride on the bremsstrahlung hump')

    b = panel(fig, [.55, .10, .42, .82], xlim=(0, 10), ylim=(0, 4.6))
    ys = {'K': 2.2, 'L': 3.15, 'M': 3.7}
    for k, y in ys.items():
        b.plot([1.4, 4.4], [y, y], color=I, lw=1.8)
        txt(b, 4.55, y - .12, k, fontsize=8.2, color=G)
    b.annotate('', xy=(2.3, 2.2), xytext=(2.3, 4.35),
               arrowprops=dict(arrowstyle='-|>', color=G, lw=1.2))
    txt(b, 2.4, 4.2, 'ejected e-', fontsize=7.4, color=G)
    b.annotate('', xy=(3.1, 2.2), xytext=(3.1, 3.15),
               arrowprops=dict(arrowstyle='-|>', color=R, lw=1.5))
    txt(b, 3.2, 2.55, 'Ka', fontsize=8.0, color=R)
    b.annotate('', xy=(3.7, 2.2), xytext=(3.7, 3.7),
               arrowprops=dict(arrowstyle='-|>', color=GOLD, lw=1.4))
    txt(b, 3.8, 3.0, 'Kb', fontsize=8.0, color=GOLD)
    txt(b, 1.4, 1.45, 'Cu: K binds 9 keV, Ka = 8.0 keV', fontsize=7.6, color=G)
    txt(b, 5.4, 2.6, r'$E_{K\alpha}=\frac{3}{4}(13.6)(Z-1)^2$ eV', fontsize=8.4)
    txt(b, 5.4, 1.6, r'$\sqrt{f}\propto(Z-1)$', fontsize=8.4, color=T)
    txt(b, 5.4, .75, 'the vacancy must be affordable: V > 9 kV', fontsize=7.6, color=G)
    return 'Characteristic lines are the atom fingerprint; Moseley turned them into a periodic table ruler'


# ----------------------------------------------------------------- 18 absorption
def _absorption_curve(fig):
    a = panel(fig, [.09, .16, .44, .74])
    axes2(a, r'thickness  $x$  (mm)', r'$I/I_0$')
    x = np.linspace(0, 5, 400)
    a.plot(x, np.exp(-np.log(2) * x / .12), color=R, lw=2.0)
    a.plot(x, np.exp(-np.log(2) * x / .45), color=T, lw=2.0)
    for k in (1, 2, 3):
        a.axhline(.5 ** k, color='#dfe9ea', lw=.8, xmax=.92)
        a.axvline(.12 * k, color='#dfe9ea', lw=.8, ymax=.5 ** k)
    a.text(.18, .78, 'lead', fontsize=7.8, color=R)
    a.text(1.1, .45, 'bone', fontsize=7.8, color=T)
    a.text(1.9, .95, r'$x_{1/2}=\ln 2/\mu$', fontsize=8.4)
    a.set_xlim(0, 5); a.set_ylim(0, 1.02)
    head(a, 'every layer removes the same fraction')

    b = panel(fig, [.55, .10, .42, .82], xlim=(0, 10), ylim=(0, 4.6))
    b.add_patch(Rectangle((.8, 1.3), 5.2, 1.5, fc='#f3f6f6', ec=G, lw=1.0))
    b.add_patch(Polygon([(2.2, 1.3), (2.7, 2.8), (3.4, 2.8), (3.9, 1.3)],
                        closed=True, fc='white', ec=T, lw=1.0))
    b.plot([.4, 8.1], [2.05, 2.05], color=GOLD, lw=1.2, ls=(0, (4, 3)))
    txt(b, .5, 2.95, 'beam', fontsize=7.6, color=GOLD)
    txt(b, 2.1, .85, 'bone absorbs more', fontsize=7.4, color=T)
    b.add_patch(Rectangle((8.2, 1.2), 1.2, 1.8, fc='#dfe9ea', ec=I, lw=.9))
    for y in (1.5, 1.9, 2.3, 2.7):
        b.add_patch(Circle((8.8, y), .05, fc=I, ec='none'))
    txt(b, 7.5, 3.25, 'shadow', fontsize=7.4, color=I)
    txt(b, .8, 4.2, r'$\mu\propto Z^3\!-\!Z^4$, falls with $E$', fontsize=8.2)
    txt(b, .8, .35, 'contrast and dose are the same curve, read two ways', fontsize=7.4, color=G)
    return 'Exponential attenuation: the radiograph is a map of mu times thickness'


# --------------------------------------------------------------------- 19 Bragg
def _bragg_geometry(fig):
    a = panel(fig, [.03, .08, .52, .86], xlim=(0, 10), ylim=(0, 4.6))
    for y in (1.35, 2.35, 3.35):
        a.plot([.5, 8.6], [y, y], color='#cfe1dc', lw=1.2)
        for x in np.arange(.8, 8.6, .55):
            a.add_patch(Circle((x, y), .055, fc='#b9c6cb', ec='none'))
    for y0, off in ((2.35, 0), (3.35, 0)):
        a.plot([.4, 4.0], [y0 - 1.15, y0], color=I, lw=1.2)
        a.plot([4.0, 8.0], [y0, y0 + 1.25], color=I, lw=1.2)
    a.plot([4.0, 4.0], [2.35, 3.35], color=R, lw=1.0, ls=(0, (3, 2)))
    a.annotate('', xy=(5.4, 2.6), xytext=(5.4, 1.6),
               arrowprops=dict(arrowstyle='<->', color=G, lw=1.0))
    txt(a, 5.55, 2.0, r'$d$', fontsize=8.4, color=G)
    a.add_patch(Arc((4.0, 2.35), 1.2, 1.2, theta1=0, theta2=42, color=T, lw=1.1))
    txt(a, 4.55, 2.6, r'$\theta$', fontsize=8.2, color=T)
    txt(a, .5, 4.25, 'glancing angle, measured from the plane', fontsize=7.8, color=T)
    txt(a, .5, .55, r'$2d\sin\theta=n\lambda$', fontsize=9.6)

    b = panel(fig, [.60, .17, .37, .74])
    axes2(b, r'$n$', r'$\sin\theta$')
    d, lam = 282, 154
    ns = np.arange(1, 5)
    b.plot(ns, ns * lam / (2 * d), 'o-', ms=5, color=T, lw=1.5)
    b.axhline(1.0, color=R, lw=1.0, ls=(0, (4, 3)))
    b.text(1.15, 1.03, 'no order beyond n=3', fontsize=7.4, color=R)
    b.set_xlim(.8, 4.2); b.set_ylim(0, 1.25)
    return 'Bragg: path difference 2d sin(theta); orders stop when sin(theta) would exceed one'


# ------------------------------------------------------------------- 20 Compton
def _compton_kinematics(fig):
    a = panel(fig, [.03, .08, .46, .86], xlim=(0, 10), ylim=(0, 4.6))
    a.plot([.4, 4.4], [3.0, 3.0], color=GOLD, lw=1.8)
    arrow(a, (3.6, 3.0), (4.4, 3.0), GOLD, 1.8, '-|>', 7)
    txt(a, .5, 3.2, r'$\lambda$', fontsize=8.4, color=GOLD)
    a.plot([4.6, 8.2], [2.95, 1.65], color=T, lw=1.6)
    arrow(a, (7.4, 1.95), (8.2, 1.65), T, 1.6, '-|>', 7)
    txt(a, 7.0, 2.35, r"$\lambda'$", fontsize=8.4, color=T)
    a.plot([4.6, 6.6], [2.95, 1.35], color=R, lw=1.6)
    arrow(a, (6.1, 1.6), (6.65, 1.33), R, 1.6, '-|>', 7)
    txt(a, 6.0, 1.05, 'recoil e-', fontsize=7.8, color=R)
    a.add_patch(Arc((4.6, 2.95), 1.5, 1.5, theta1=-58, theta2=0, color=G, lw=1.0))
    txt(a, 5.55, 2.55, r'$\theta$', fontsize=8.2, color=G)
    a.add_patch(Arc((4.6, 2.95), 2.6, 2.6, theta1=-72, theta2=-58, color=R, lw=1.0))
    txt(a, 5.6, 1.55, r'$\phi$', fontsize=8.2, color=R)
    a.add_patch(Circle((4.6, 2.95), .08, fc=I, ec='none'))
    txt(a, .5, .55, r'$\Delta\lambda=\frac{h}{m_ec}(1-\cos\theta)$', fontsize=9.2)

    b = panel(fig, [.53, .17, .43, .74])
    axes2(b, r'scattering angle $\theta$ (deg)', r'$\Delta\lambda$ (pm)')
    th = np.linspace(0, 180, 300)
    b.plot(th, 2.426 * (1 - np.cos(np.radians(th))), color=T, lw=2.2)
    for ang in (90, 180):
        b.plot([ang], [2.426 * (1 - np.cos(np.radians(ang)))], 'o', ms=5, color=R, zorder=5)
    b.text(96, 1.0, '2.43 pm', fontsize=7.6, color=R)
    b.text(120, 4.1, '4.86 pm', fontsize=7.6, color=R)
    b.set_xlim(0, 180); b.set_ylim(0, 5.4)
    return 'Compton: the shift depends on angle alone - absolute, never a percentage'


# ----------------------------------------------------------- 21 correspondence
def _correspondence_plot(fig):
    a = panel(fig, [.10, .18, .38, .72])
    axes2(a, r'principal quantum number $n$', r'$f_{transition}/f_{orbit}-1$')
    n = np.linspace(6, 120, 400)
    a.semilogy(n, 1.5 / n, color=T, lw=2.2)
    a.semilogy([10, 100], [1.5 / 10, 1.5 / 100], 'o', ms=5, color=R, zorder=5)
    a.text(12, .19, 'n=10: 15 %', fontsize=7.6, color=R)
    a.text(46, .017, 'n=100: 1.5 %', fontsize=7.6, color=R)
    a.set_xlim(0, 120)
    head(a, 'the gap closes as 1/n')

    b = panel(fig, [.56, .10, .40, .82], xlim=(0, 10), ylim=(0, 4.6))
    b.add_patch(Rectangle((.8, 2.0), 1.35, 1.15, fc='#e7f4f1', ec=T, lw=1.2))
    txt(b, .95, 2.42, 'quantum', fontsize=7.6, color=T)
    b.add_patch(Rectangle((4.0, 2.0), 1.9, 1.15, fc='#fdf0bd', ec=GOLD, lw=1.2))
    txt(b, 4.15, 2.42, 'n ~ 10', fontsize=7.6, color=GOLD)
    b.add_patch(Rectangle((7.2, 2.0), 2.2, 1.15, fc='#f6dedb', ec=R, lw=1.2))
    txt(b, 7.35, 2.42, 'classical', fontsize=7.6, color=R)
    arrow(b, (2.2, 2.57), (3.95, 2.57), G, 1.2, '-|>', 6)
    arrow(b, (5.95, 2.57), (7.15, 2.57), G, 1.2, '-|>', 6)
    txt(b, .8, 3.55, 'an orbit that is a good antenna', fontsize=7.8, color=G)
    txt(b, .8, 1.35, r'$f_{orbit}=6.58\times10^9$ Hz at n=100', fontsize=7.8, color=T)
    txt(b, .8, .85, r'$f_{photon}=6.68\times10^9$ Hz', fontsize=7.8, color=G)
    txt(b, .8, .35, 'the same number, to 1.5 percent', fontsize=7.6, color=G)
    return 'Correspondence: for large n the photon frequency melts into the orbital frequency'


# ---------------------------------------------------------------- 22 exotic atoms
def _exotic_atoms(fig):
    a = panel(fig, [.09, .19, .88, .71])
    logaxis(a, r'ground-state radius  (m)', '')
    a.set_yticks([])
    items = [(5.29e-11, 'hydrogen', T, 4.05),
             (1.06e-10, 'positronium', G, 3.35),
             (2.56e-13, 'muonic H', R, 4.05),
             (1.2e-14, 'proton', G, 3.35)]
    for r, lab, c, y in items:
        a.plot([r, r], [0, y - .35], color=c, lw=1.6, ls=(0, (4, 3)))
        a.text(r, y, lab, fontsize=8.2, color=c, ha='center')
    a.axvspan(1e-15, 7e-15, color='#f6dedb', alpha=.5)
    a.text(1.6e-15, 1.35, 'nuclear size', fontsize=7.6, color=R)
    a.set_xlim(5e-16, 1e-9); a.set_ylim(0, 4.6)
    a.text(7e-13, .55, 'the muon orbit sits inside the nucleus', fontsize=7.6, color=R)
    head(a, 'mass sets the ruler: 207 times heavier, 207 times smaller')
    return 'Exotic atoms are scaling tests: replace the electron mass by the reduced mass'


# ----------------------------------------------------------------- 23 collapse
def _collapse_spiral(fig):
    a = panel(fig, [.03, .08, .44, .86], xlim=(0, 10), ylim=(0, 4.6), equal=True)
    t = np.linspace(0, 6.5 * np.pi, 900)
    r = 3.3 * np.exp(-.115 * t)
    a.plot(5 + r * np.cos(t), 2.3 + r * np.sin(t), color=T, lw=1.4)
    a.add_patch(Circle((5, 2.3), .10, fc=R, ec='none'))
    txt(a, 5.9, 2.9, 'spiral in, radiating all the time', fontsize=7.6, color=T)
    txt(a, .4, .40, r'$\tau=1.6\times10^{-11}$ s from a0', fontsize=8.8)

    b = panel(fig, [.52, .22, .44, .66])
    axes2(b, 'wavelength', 'intensity')
    lam = np.linspace(0, 10, 400)
    b.plot(lam, .55 * np.exp(-((lam - 5) / 3.2) ** 2) + .05, color=R, lw=1.8)
    for x in (3.2, 4.6, 6.1):
        b.plot([x, x], [0, .85], color=T, lw=2.0)
    b.set_xticks([]); b.set_yticks([])
    b.text(.4, .95, 'observed: three sharp lines', fontsize=7.8, color=T)
    b.text(4.2, .35, 'classical: one continuous smear', fontsize=7.8, color=R)
    head(b, 'a dying atom cannot be line-bright')
    return 'The classical atom lives 16 ps and glows a continuum; real atoms do neither'


# --------------------------------------------------------------- 24 Franck-Hertz
def _franck_hertz(fig):
    a = panel(fig, [.09, .16, .44, .74])
    axes2(a, r'accelerating voltage  $V$  (V)', 'collector current')
    V = np.linspace(0, 15, 900)
    cur = (V / 15) ** 1.4 * (0.62 + .38 * np.cos(2 * np.pi * V / 4.9))
    a.plot(V, cur, color=T, lw=1.8)
    for k in (1, 2):
        a.annotate('', xy=(4.9 * k, .18), xytext=(4.9 * k, .62),
                   arrowprops=dict(arrowstyle='-|>', color=R, lw=1.0))
        a.text(4.9 * k - .4, .68, f'{4.9*k:.1f} V', fontsize=7.4, color=R)
    a.set_xlim(0, 15); a.set_ylim(0, 1.3)
    head(a, 'current dips every 4.9 V')

    b = panel(fig, [.55, .10, .41, .82], xlim=(0, 10), ylim=(0, 4.6))
    b.plot([1.2, 4.8], [1.6, 1.6], color=I, lw=1.8)
    b.plot([1.2, 4.8], [3.3, 3.3], color=I, lw=1.8)
    txt(b, 4.95, 1.48, 'ground', fontsize=7.6, color=G)
    txt(b, 4.95, 3.18, '4.9 eV', fontsize=7.6, color=G)
    arrow(b, (.55, 1.72), (.55, 4.1), T, 1.6, '-|>', 7)
    txt(b, .65, 2.75, 'e- beam', fontsize=7.6, color=T, rotation=90)
    b.annotate('', xy=(2.4, 3.3), xytext=(2.4, 1.6),
               arrowprops=dict(arrowstyle='-|>', color=R, lw=1.4))
    txt(b, 2.5, 2.35, 'inelastic', fontsize=7.6, color=R)
    txt(b, 1.2, .95, 'the electron keeps only the remainder', fontsize=7.4, color=G)
    txt(b, 1.2, 4.25, 'mercury: first excited level at 4.9 eV', fontsize=7.6, color=G)
    txt(b, 5.6, 3.4, r'$K=eV-4.9$', fontsize=8.6)
    txt(b, 5.6, 2.5, 'repeats every 4.9 V', fontsize=8.0, color=G)
    txt(b, 5.6, 1.5, 'levels exist, seen as voltage teeth', fontsize=7.6, color=G)
    return 'Franck-Hertz turns a level diagram into a current-voltage curve with teeth at 4.9 V'


# -------------------------------------------------------------- 25 waiting time
def _waiting_time(fig):
    a = panel(fig, [.10, .18, .38, .72])
    logaxis(a, r'intensity  (W/m$^2$)', r'waiting time  (s)')
    I = np.logspace(-9, 2, 300)
    a.loglog(I, 3.2e-19 / (I * 1e-20), color=T, lw=2.2)
    a.axhline(1e-9, color=R, lw=1.2, ls=(0, (4, 3)))
    a.text(1e-8, 3e-9, 'observed: below 1 ns', fontsize=7.6, color=R)
    a.plot([1e-3], [3.2e4], 'o', ms=6, color=GOLD, zorder=5)
    a.annotate('9 hours at 1 mW/m^2', xy=(1e-3, 3.2e4), xytext=(1e-8, 1e6),
               fontsize=7.6, color=GOLD, arrowprops=dict(arrowstyle='->', color=GOLD, lw=.9))
    a.set_ylim(1e-10, 1e9)
    head(a, 'waves: dim light should need hours')

    b = panel(fig, [.56, .10, .40, .82], xlim=(0, 10), ylim=(0, 4.6))
    b.add_patch(Circle((2.6, 2.6), 1.25, fc='#fdf0bd', ec=GOLD, lw=1.2))
    for k in range(9):
        ang = k * .7
        b.add_patch(Circle((2.6 + 1.0 * np.cos(ang), 2.6 + 1.0 * np.sin(ang)), .05,
                           fc=GOLD, ec='none'))
    txt(b, 1.15, .95, 'wave: energy spread thin', fontsize=7.6, color=GOLD)
    b.add_patch(Circle((7.2, 2.6), .16, fc=T, ec='none'))
    arrow(b, (5.6, 3.4), (7.0, 2.75), T, 1.4, '-|>', 6)
    txt(b, 5.3, 3.6, 'photon: one lump', fontsize=7.6, color=T)
    txt(b, 5.9, 1.35, 'arrives whole, absorbed whole', fontsize=7.6, color=G)
    txt(b, .6, 4.2, 'the argument that kills the wave picture', fontsize=7.6, color=G)
    return 'Classical waiting time at dim light is hours; the observed delay is nanoseconds'


# ----------------------------------------------------------- 26 matter wave speeds
def _matter_wave_speeds(fig):
    a = panel(fig, [.03, .12, .46, .82], xlim=(0, 10), ylim=(0, 4.6))
    v = np.linspace(.012, .99, 400)
    a.plot(v, 1 / v, color=T, lw=2.0)
    a.plot([0, 1], [0, 1], color=R, lw=2.0)
    a.axhline(1, color=G, lw=.8, ls=(0, (4, 3)))
    a.set_xlim(0, 1); a.set_ylim(0, 4.2)
    txt(a, .55, 2.6, r'$v_p=c^2/v$', fontsize=8.8, color=T)
    txt(a, .55, .55, r'$v_g=v$', fontsize=8.8, color=R)
    txt(a, .06, 3.9, 'phase speed is not a signal', fontsize=7.6, color=G)
    txt(a, .06, 1.12, r'$v=c$ line', fontsize=7.4, color=G)
    head(a, 'two speeds, one particle')

    b = panel(fig, [.55, .10, .41, .82], xlim=(0, 10), ylim=(0, 4.6))
    x = np.linspace(0, 10, 600)
    a1 = np.sin(1.1 * x - 2.0)
    a2 = np.sin(1.45 * x - 2.0)
    b.plot(x, 2.9 + .42 * a1, color='#cfe1dc', lw=1.0)
    b.plot(x, 2.9 + .42 * a2, color='#cfe1dc', lw=1.0)
    b.plot(x, 2.9 + .42 * (a1 + a2), color=T, lw=1.4)
    b.plot(x, 1.2 + .42 * np.exp(-((x - 5) / 1.8) ** 2) * np.cos(1.25 * x - 2), color=R, lw=1.2)
    txt(b, .4, 3.9, 'two waves beat into a packet', fontsize=7.8, color=G)
    txt(b, .4, .45, 'the envelope travels at v_g, the crests at v_p', fontsize=7.6, color=G)
    return 'Matter wave: v_p v_g = c squared; only the group speed carries the particle'


# --------------------------------------------------------- 27 Compton invariant
def _compton_invariant(fig):
    a = panel(fig, [.03, .08, .50, .86], xlim=(0, 10), ylim=(0, 4.6), equal=True)
    a.annotate('', xy=(4.9, 3.5), xytext=(1.2, 1.3),
               arrowprops=dict(arrowstyle='-|>', color=GOLD, lw=1.8))
    a.annotate('', xy=(8.2, 3.0), xytext=(4.9, 3.5),
               arrowprops=dict(arrowstyle='-|>', color=T, lw=1.8))
    a.annotate('', xy=(6.2, .8), xytext=(4.9, 3.5),
               arrowprops=dict(arrowstyle='-|>', color=R, lw=1.8))
    txt(a, 1.4, 1.05, r'$p_\gamma$', fontsize=8.6, color=GOLD)
    txt(a, 7.5, 3.2, r"$p'_\gamma$", fontsize=8.6, color=T)
    txt(a, 6.35, .55, r'$p_e$', fontsize=8.6, color=R)
    a.add_patch(Arc((4.9, 3.5), 2.3, 2.3, theta1=-38, theta2=0, color=G, lw=1.0))
    txt(a, 6.0, 3.05, r'$\theta$', fontsize=8.2, color=G)
    txt(a, .5, 4.3, 'close the triangle with four-momenta', fontsize=7.8, color=G)
    txt(a, .5, .45, r"$p_\gamma=p'_\gamma+p_e$  (four-vectors)", fontsize=8.6)

    b = panel(fig, [.57, .10, .39, .82], xlim=(0, 10), ylim=(0, 4.6))
    txt(b, .4, 3.9, 'square the electron line:', fontsize=8.0, color=G)
    txt(b, .4, 3.15, r"$(p_\gamma-p'_\gamma)^2=m_e^2c^2$", fontsize=8.6)
    txt(b, .4, 2.25, r"$2p\cdot p'=2m_e^2c^2$", fontsize=8.4)
    txt(b, .4, 1.35, r'$\Rightarrow\ \Delta\lambda=\frac{h}{m_ec}(1-\cos\theta)$', fontsize=8.8, color=R)
    txt(b, .4, .55, 'two lines, no trigonometry', fontsize=7.8, color=G)
    head(b, 'the invariant route')
    return 'One invariant replaces three conservation equations: the Compton shift falls out in two lines'


# ------------------------------------------------------------ 28 inverse Compton
def _inverse_compton(fig):
    a = panel(fig, [.03, .10, .50, .84], xlim=(0, 10), ylim=(0, 4.6))
    arrow(a, (.6, 1.4), (4.2, 1.4), GOLD, 1.8, '-|>', 7)
    txt(a, .7, 1.6, r'soft photon $\epsilon$', fontsize=8.0, color=GOLD)
    a.add_patch(Circle((5.2, 2.3), .34, fc='#e7f4f1', ec=T, lw=1.4))
    txt(a, 4.75, 2.75, r'$e^-$, $\gamma\gg1$', fontsize=8.0, color=T)
    arrow(a, (3.6, 2.9), (4.85, 2.45), T, 1.4, '-|>', 6)
    arrow(a, (5.55, 2.55), (9.2, 3.4), R, 1.9, '-|>', 8)
    txt(a, 7.6, 3.55, r"$\epsilon'\approx\gamma^2\epsilon$", fontsize=8.8, color=R)
    txt(a, .6, 4.25, 'a fast electron boosts a soft photon', fontsize=7.8, color=G)
    txt(a, .6, .55, 'the mirror moves toward the light: double Doppler', fontsize=7.6, color=G)

    b = panel(fig, [.57, .16, .39, .76])
    logaxis(b, r'electron Lorentz factor $\gamma$', r"$\epsilon'/\epsilon$")
    g = np.logspace(0, 3, 200)
    b.loglog(g, g ** 2, color=R, lw=2.2)
    b.plot([1e3], [1e6], 'o', ms=5, color=GOLD, zorder=5)
    b.text(60, 3e5, 'gamma squared', fontsize=8.0, color=R)
    b.text(1.3, 12, 'radio photon -> X-ray at gamma=1000', fontsize=7.2, color=G)
    b.set_xlim(1, 1e3); b.set_ylim(1, 1e7)
    return 'Inverse Compton: the same kinematics run backwards, and astrophysics uses it'


# -------------------------------------------------------------- 29 Moseley line
def _moseley_line(fig):
    a = panel(fig, [.10, .18, .55, .72])
    axes2(a, r'atomic number $Z$', r'$\sqrt{f}$  ($10^{8}$ Hz$^{1/2}$)')
    Z = np.arange(20, 48)
    f = 2.47e15 * (Z - 1) ** 2
    a.plot(Z, np.sqrt(f) / 1e8, color=T, lw=1.8)
    for z, lab in ((26, 'Fe'), (29, 'Cu'), (30, 'Zn'), (42, 'Mo')):
        a.plot([z], [np.sqrt(2.47e15 * (z - 1) ** 2) / 1e8], 'o', ms=5, color=R, zorder=5)
        a.text(z - .4, np.sqrt(2.47e15 * (z - 1) ** 2) / 1e8 + 1.4, lab, fontsize=7.6, color=R)
    for z in (43, 61):
        a.axvline(z, color=G, lw=.8, ls=(0, (3, 3)), ymax=.25)
    a.text(33, 44, 'gaps = missing elements', fontsize=7.6, color=G)
    a.set_xlim(18, 48); a.set_ylim(0, 95)
    head(a, 'sqrt(f) is a straight edge in Z')

    b = panel(fig, [.70, .10, .27, .82], xlim=(0, 10), ylim=(0, 4.6))
    txt(b, .4, 3.8, r'$E_{K\alpha}=\frac{3}{4}(13.6)(Z-1)^2$', fontsize=8.0)
    txt(b, .4, 2.9, 'one K electron', fontsize=7.8, color=G)
    txt(b, .4, 2.45, 'screens the nucleus', fontsize=7.8, color=G)
    txt(b, .4, 1.55, 'L lines use', fontsize=7.8, color=G)
    txt(b, .4, 1.1, r'$b\approx7.4$', fontsize=8.2, color=R)
    txt(b, .4, .45, 'so the constant is line-specific', fontsize=7.4, color=G)
    return 'Moseley: the K-alpha frequency is a ruler for Z, with the missing elements as gaps'


# -------------------------------------------------------------- 30 pair threshold
def _pair_threshold(fig):
    a = panel(fig, [.04, .30, .92, .46])
    a.axis('off')
    a.plot([.5, 9.5], [2.0, 2.0], color=G, lw=1.6)
    for e, lab, c in ((1.022, '1.022 MeV: threshold', R), (2.0, '2 MeV', T),
                      (5.0, '5 MeV', GOLD)):
        x = .5 + 9.0 * (np.log10(e) - np.log10(.5)) / (np.log10(8) - np.log10(.5))
        a.plot([x, x], [1.75, 2.25], color=c, lw=1.6)
        a.text(x, 2.42, lab, fontsize=7.6, color=c, ha='center')
    a.text(.55, 1.35, r'$E_\gamma>2m_ec^2=1.022$ MeV', fontsize=8.8)
    a.text(.55, 2.9, 'photon energy', fontsize=8.0, color=G)

    b = panel(fig, [.10, .10, .80, .58], xlim=(0, 10), ylim=(0, 4.6))
    b.plot([.8, 4.4], [2.3, 2.3], color=GOLD, lw=1.8)
    arrow(b, (3.6, 2.3), (4.4, 2.3), GOLD, 1.8, '-|>', 7)
    txt(b, .9, 2.55, r'$\gamma$', fontsize=9.0, color=GOLD)
    b.add_patch(Rectangle((4.55, 1.9), .5, .8, fc='#dfe9ea', ec=I, lw=1.2))
    txt(b, 4.35, 1.55, 'nucleus takes recoil', fontsize=7.4, color=G)
    ts = np.linspace(0, 1, 60)
    b.plot(5.1 + 2.2 * ts, 2.55 + .9 * ts ** 2, color=R, lw=1.8)
    b.plot(5.1 + 2.2 * ts, 2.05 - .9 * ts ** 2, color=T, lw=1.8)
    txt(b, 7.3, 3.45, 'e+', fontsize=9.0, color=R)
    txt(b, 7.3, .75, 'e-', fontsize=9.0, color=T)
    txt(b, 5.2, 4.1, r'$K_{pair}=E_\gamma-1.022$ MeV, shared', fontsize=8.4)
    return 'Pair production needs 1.022 MeV and a nucleus to carry the momentum'


def figure(ax, key):
    fig = ax.figure
    ax.axis('off')
    build = {
        'thomson_vs_rutherford': _thomson_vs_rutherford,
        'closest_approach': _closest_approach,
        'standing_wave': _standing_wave,
        'bohr_ledger': _bohr_ledger,
        'spectrum_series': _spectrum_series,
        'excitation_ladder': _excitation_ladder,
        'hydrogenic_scaling': _hydrogenic_scaling,
        'quantum_numbers': _quantum_numbers,
        'photon_packet': _photon_packet,
        'photoelectric_curve': _photoelectric_curve,
        'stopping_graph': _stopping_graph,
        'photocell_iv': _photocell_iv,
        'debroglie_scale': _debroglie_scale,
        'davisson_germer': _davisson_germer,
        'uncertainty_well': _uncertainty_well,
        'xray_continuous': _xray_continuous,
        'xray_characteristic': _xray_characteristic,
        'absorption_curve': _absorption_curve,
        'bragg_geometry': _bragg_geometry,
        'compton_kinematics': _compton_kinematics,
        'correspondence_plot': _correspondence_plot,
        'exotic_atoms': _exotic_atoms,
        'collapse_spiral': _collapse_spiral,
        'franck_hertz': _franck_hertz,
        'waiting_time': _waiting_time,
        'matter_wave_speeds': _matter_wave_speeds,
        'compton_invariant': _compton_invariant,
        'inverse_compton': _inverse_compton,
        'moseley_line': _moseley_line,
        'pair_threshold': _pair_threshold,
    }
    if key not in build:
        raise ValueError(key)
    return build[key](fig)
