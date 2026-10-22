"""Part I figures: work, energy, power — the JEE layer."""
import numpy as np
from matplotlib.patches import Rectangle, Circle, Arc, Polygon
from figlib import (I, T, R, G, GOLD, HG, BLUE, GREEN, PALE, YEL, WATER,
                    txt, head, foot, arrow, panel, axes2, dimx, dimy, incline,
                    block, force, dashed, ball, spring, bars, shade_between,
                    arcarrow, rot_block)


def work_signs(fig):
    a = panel(fig, [.02, .16, .46, .70], xlim=(0, 10), ylim=(0, 4.6))
    a.plot([.40, 9.60], [.80, .80], color=I, lw=1.8)
    block(a, 3.30, 1.24, 1.10, .88, '#fdf0bd', GOLD)
    arrow(a, (3.30, 1.72), (5.55, 2.40), R, 2.0)
    txt(a, 5.62, 2.46, r'$F$', color=R, fontsize=9.4)
    arrow(a, (3.30, .52), (5.80, .52), T, 1.6)
    txt(a, 5.30, .26, r'$d$', color=T, fontsize=9.4)
    a.add_patch(Arc((3.30, 1.72), 2.0, 2.0, theta1=0, theta2=23, color=G, lw=1.2))
    txt(a, 4.42, 1.86, r'$\theta$', color=G, fontsize=9.0)
    txt(a, .30, 4.20, r'$W=Fd\cos\theta$', color=I, fontsize=10.4)
    txt(a, .30, 3.55, 'only the component along d counts', color=G, fontsize=7.6)
    txt(a, .30, .06, r'$W>0$ helps, $W<0$ removes, $W=0$ at $90^{\circ}$',
        color=G, fontsize=7.2)

    b = panel(fig, [.52, .18, .44, .64])
    axes2(b, r'angle between $F$ and $d$  (degrees)', r'work  $Fd\cos\theta$  (J)')
    th = np.linspace(0, 180, 400)
    b.plot(th, 50 * np.cos(np.radians(th)), color=T, lw=2.3)
    b.axhline(0, color=I, lw=.9)
    b.axvline(90, color=HG, lw=1.0, ls=(0, (3, 3)))
    b.fill_between(th[:200], 0, 50 * np.cos(np.radians(th[:200])), color=T, alpha=.12, lw=0)
    b.fill_between(th[200:], 0, 50 * np.cos(np.radians(th[200:])), color=R, alpha=.12, lw=0)
    b.text(28, 40, 'positive', fontsize=7.4, color=T)
    b.text(118, -40, 'negative', fontsize=7.4, color=R)
    b.text(92, 8, r'$90^{\circ}$', fontsize=7.4, color=G)
    b.set_xlim(0, 180); b.set_ylim(-58, 58)
    head(b, 'one curve, two signs')
    return 'Work is F d cos(theta): the component of force along the displacement, signed'


def fx_area(fig):
    a = panel(fig, [.06, .22, .42, .60])
    axes2(a, r'position $x$  (m)', r'force $F_x$  (N)')
    x = np.linspace(0, 3.4, 400)
    f = 12 * np.sin(x * 1.15) * np.exp(-.10 * x)
    a.plot(x, f, color=T, lw=2.3)
    a.axhline(0, color=I, lw=.9)
    a.fill_between(x, 0, f, where=f > 0, color=GREEN, alpha=.18, lw=0)
    a.fill_between(x, 0, f, where=f < 0, color=R, alpha=.18, lw=0)
    a.text(.55, 8.4, 'A+', fontsize=8.0, color=GREEN)
    a.text(2.55, -7.2, 'A-', fontsize=8.0, color=R)
    a.set_xlim(0, 3.4); a.set_ylim(-11, 11)
    head(a, 'work is the signed area')

    b = panel(fig, [.58, .22, .40, .60])
    axes2(b, r'extension $x$  (m)', r'force $F$  (N)')
    xs = np.linspace(0, .30, 200)
    b.plot(xs, 200 * xs, color=R, lw=2.1)
    b.fill_between(xs, 0, 200 * xs, color=R, alpha=.14, lw=0)
    b.plot([.30, .30], [0, 60], color=HG, lw=1, ls=(0, (3, 3)))
    b.text(.155, 44, r'$\frac{1}{2}kx^2$', fontsize=9.0, color=R)
    b.set_xlim(0, .34); b.set_ylim(0, 72)
    head(b, 'a spring: a triangle, not a rectangle')
    return 'Integrate the force along the path; the answer is an area, and areas below the axis subtract'


def force_audit(fig):
    a = panel(fig, [.03, .14, .44, .72], xlim=(0, 10), ylim=(0, 4.6))
    a.add_patch(Polygon([(.60, .60), (9.20, .60), (9.20, 3.30)], closed=True,
                        fc='#f2f6f5', ec=I, lw=1.6))
    th = np.degrees(np.arctan2(2.70, 8.60))
    rot_block(a, 4.70, .60 + (4.70 - .60) * (2.70 / 8.60), 1.15, .50, th, '#fdf0bd', GOLD)
    px, py = 4.70, .60 + (4.70 - .60) * (2.70 / 8.60) + .30
    force(a, (px, py), (px - .20, py + 1.05), T, 1.7, r'$N$', fs=9.0, off=(-.55, .05))
    force(a, (px, py), (px, py - 1.20), R, 1.7, r'$mg$', fs=9.0, off=(.12, -.35))
    force(a, (px - .30, py), (px - 1.35, py + .42), GOLD, 1.6, r'$f$', fs=9.0, off=(-.55, .10))
    force(a, (px + .25, py), (px + 1.20, py + .70), BLUE, 1.6, r'$F$', fs=9.0, off=(.10, .12))
    txt(a, .35, 4.05, 'four forces, four different work budgets', color=T, fontsize=7.8)
    txt(a, .35, .18, r'block sliding down a rough incline', color=G, fontsize=7.2)

    b = panel(fig, [.54, .20, .42, .62])
    axes2(b, '', r'work over the slide  (J)')
    bars(b, ['N', 'mg', 'f', 'net'], [0, 29.4, -10.2, 19.2],
         colors=[HG, GREEN, R, T])
    b.set_ylim(-18, 36)
    head(b, '2 kg block, 3 m of incline, mu 0.2')
    return 'N does nothing on a fixed surface, gravity returns energy it stored, friction only ever removes'


def we_derivation(fig):
    a = panel(fig, [.03, .16, .46, .70], xlim=(0, 10), ylim=(0, 4.6))
    a.axis('off')
    boxes = [(r'$F=ma$', 2.90), (r'$F\,dx=m\,a\,dx$', 1.90),
             (r'$F\,dx=m\,v\,dv$', .90)]
    for s, y in boxes:
        a.add_patch(Rectangle((.55, y), 5.30, .76, fc=PALE, ec='#9ccdc4', lw=1.3))
        a.text(3.20, y + .38, s, ha='center', va='center', fontsize=9.6, color=I)
    for y0, y1 in ((2.68, 2.88), (1.68, 1.88)):
        arrow(a, (3.20, y0), (3.20, y1), T, 1.4)
    txt(a, 6.10, 2.30, 'multiply by dx', color=G, fontsize=7.4)
    txt(a, 6.10, 1.30, 'use a = v dv/dx', color=G, fontsize=7.4)
    a.text(3.20, .38, r'$\int F\,dx=\frac{1}{2}mv^2-\frac{1}{2}mv_0^2$',
           ha='center', fontsize=10.0, color=GOLD)
    a.text(.40, 3.95, 'one line of algebra bridges the two methods', fontsize=7.6, color=T)

    b = panel(fig, [.55, .20, .41, .62])
    axes2(b, r'speed $v$  (m/s)', r'$mv$  (kg m/s)')
    v = np.linspace(0, 8, 300)
    b.plot(v, 2 * v, color=T, lw=2.1)
    b.fill_between(v, 0, 2 * v, color=T, alpha=.13, lw=0)
    b.text(4.4, 5.4, r'$\int mv\,dv$', fontsize=8.6, color=T)
    b.set_xlim(0, 8); b.set_ylim(0, 18)
    head(b, 'the same integral in v')
    return 'Net work equals the change in kinetic energy: Newton integrated once over space'


def ke_frames(fig):
    a = panel(fig, [.02, .14, .46, .72], xlim=(0, 10), ylim=(0, 4.6))
    a.plot([.30, 9.70], [1.05, 1.05], color=I, lw=1.8)
    block(a, 2.30, 1.62, 1.30, .90, '#fdf0bd', GOLD)
    block(a, 7.20, 1.62, 1.60, 1.20, '#e8f3f8', BLUE)
    arrow(a, (2.95, 1.90), (4.10, 1.90), R, 1.8)
    txt(a, 3.20, 2.10, r'$4$ m/s', color=R, fontsize=8.4)
    txt(a, 2.30, .70, 'ground frame', color=G, fontsize=7.6, ha='center')
    arrow(a, (7.20, 2.50), (8.40, 2.50), BLUE, 1.8)
    txt(a, 7.30, 2.70, r'$3$ m/s', color=BLUE, fontsize=8.4)
    txt(a, 7.20, .70, 'train frame', color=G, fontsize=7.6, ha='center')
    txt(a, .30, 4.15, 'the same block, two speeds, two kinetic energies', color=T, fontsize=7.8)
    txt(a, .30, 3.45, r'$K=\frac{1}{2}mv^2$ is frame-dependent', color=G, fontsize=7.8)

    b = panel(fig, [.55, .20, .41, .62])
    axes2(b, '', r'kinetic energy  (J)')
    bars(b, ['ground', 'train'], [8.0, 24.5], colors=[R, BLUE])
    b.set_ylim(0, 28)
    head(b, 'same 1 kg block, same physical event')
    return 'Kinetic energy depends on the frame, so a work statement must name its frame too'


def friction_ledger(fig):
    a = panel(fig, [.03, .14, .44, .72], xlim=(0, 10), ylim=(0, 4.6))
    a.plot([.40, 9.60], [1.00, 1.00], color=I, lw=1.8)
    for x in np.linspace(.7, 9.2, 22):
        a.plot([x, x + .28], [.86, 1.14], color=HG, lw=.9)
    block(a, 2.30, 1.60, 1.20, .90, '#fdf0bd', GOLD)
    force(a, (1.75, 1.42), (.55, 1.42), R, 1.8, r'$f_k$', fs=9.0, off=(-.55, .06))
    arrow(a, (2.95, 2.20), (5.30, 2.20), T, 1.8)
    txt(a, 3.20, 2.38, r'$v$', color=T, fontsize=9.0)
    dimx(a, 2.30, 6.90, .55, r'$d$', color=G)
    txt(a, .35, 4.15, 'friction does negative work on the block', color=T, fontsize=7.8)
    txt(a, .35, 3.50, r'$W_f=-f_kd$, and the same $f_kd$ appears as heat', color=G, fontsize=7.4)

    b = panel(fig, [.55, .20, .41, .62])
    axes2(b, r'distance slid  (m)', r'energy  (J)')
    x = np.linspace(0, 6, 300)
    b.plot(x, 60 - 8 * x, color=T, lw=2.2, label='mechanical')
    b.plot(x, 8 * x, color=R, lw=2.0, label='thermal')
    b.plot(x, 60 + 0 * x, color=HG, lw=1.2, ls=(0, (3, 3)))
    b.legend(frameon=False, fontsize=7.0, loc='center right')
    b.set_xlim(0, 6); b.set_ylim(0, 70)
    head(b, 'the total is flat, the split is not')
    return 'Friction converts mechanical energy into heat at a rate f_k times the sliding distance'


def power_curve(fig):
    a = panel(fig, [.06, .22, .42, .60])
    axes2(a, r'angle between $F$ and $v$  (deg)', r'power  $Fv\cos\theta$  (W)')
    th = np.linspace(0, 180, 400)
    a.plot(th, 400 * np.cos(np.radians(th)), color=T, lw=2.3)
    a.axhline(0, color=I, lw=.9)
    a.axvline(90, color=HG, lw=1, ls=(0, (3, 3)))
    a.set_xlim(0, 180); a.set_ylim(-450, 450)
    head(a, r'$P=\mathbf{F}\cdot\mathbf{v}$')

    b = panel(fig, [.57, .22, .40, .60])
    axes2(b, r'speed  (m/s)', r'power  (kW)')
    v = np.linspace(0, 30, 300)
    for F, c, lab in ((300, T, '300 N'), (500, GOLD, '500 N')):
        b.plot(v, F * v / 1000, color=c, lw=2.0, label=lab)
    b.plot(20, 10, 'o', ms=5, color=R, zorder=5)
    b.annotate('10 kW at 20 m/s', (20, 10), xytext=(12.4, 13.4), fontsize=7.2, color=R,
               arrowprops=dict(arrowstyle='-', color=R, lw=.9,
                               shrinkA=2, shrinkB=3))
    b.legend(frameon=False, fontsize=7.2, loc='upper left')
    b.set_xlim(0, 30); b.set_ylim(0, 16)
    head(b, 'power buys force times speed')
    return 'Power is the rate of doing work, and at fixed speed it is force times velocity'


def constant_power(fig):
    a = panel(fig, [.06, .22, .42, .60])
    axes2(a, r'time  (s)', r'speed  (m/s)')
    t = np.linspace(0, 10, 400)
    a.plot(t, np.sqrt(2 * 800 * t / 1000), color=T, lw=2.3)
    a.plot(t, np.sqrt(2 * 800 * t / 1000)[-1] / 10 * t, color=HG, lw=1.2, ls=(0, (3, 3)))
    a.text(5.4, 2.1, r'$v=\sqrt{2Pt/m}$', fontsize=8.4, color=T)
    a.text(.6, 3.55, 'straight line = constant a', fontsize=7.0, color=G)
    a.set_xlim(0, 10); a.set_ylim(0, 4.2)
    head(a, 'constant power, 800 W on 1 t')

    b = panel(fig, [.57, .22, .40, .60])
    axes2(b, r'speed  (m/s)', r'time to reach it  (s)')
    v = np.linspace(0, 30, 300)
    b.plot(v, 1000 * v ** 2 / (2 * 800), color=R, lw=2.1)
    b.plot([20], [1000 * 400 / 1600], 'o', ms=5, color=T, zorder=5)
    b.annotate('20 m/s: 250 s', (20, 250), xytext=(5.4, 330), fontsize=7.2, color=T,
               arrowprops=dict(arrowstyle='-', color=T, lw=.9,
                               shrinkA=2, shrinkB=3))
    b.set_xlim(0, 30); b.set_ylim(0, 620)
    head(b, r'$t=mv^2/2P$ grows as $v^2$')
    return 'At constant power the speed grows as the square root of time: acceleration must fall'


def loop_test(fig):
    a = panel(fig, [.03, .14, .44, .72], xlim=(0, 10), ylim=(0, 4.6))
    x0, y0, x1, y1 = .90, 3.70, 7.60, .90
    a.plot([x0, x1], [y0, y1], color=T, lw=2.1)
    xs = np.linspace(x0, x1 - 1.0, 200)
    a.plot(xs, .90 + (3.70 - .90) * ((x1 - 1.0 - xs) / (x1 - 1.0 - x0)) ** .45,
           color=GOLD, lw=1.9)
    a.plot([x0, x1 - 2.2], [y0, y0], color=GOLD, lw=1.9)
    a.plot([3.20, 3.20, 5.10, 5.10, x1], [y0, 2.55, 2.55, 1.60, y1],
           color=BLUE, lw=1.7)
    a.plot([x0], [y0], 'o', ms=5.5, color=I, zorder=6)
    a.plot([x1], [y1], 'o', ms=5.5, color=I, zorder=6)
    txt(a, .56, 3.34, r'$A$', color=I, fontsize=9.2)
    txt(a, 7.80, .86, r'$B$', color=I, fontsize=9.2)
    txt(a, 3.05, 1.55, 'straight', color=T, fontsize=7.4)
    txt(a, 1.10, 3.10, 'curved', color=GOLD, fontsize=7.4)
    txt(a, 5.75, 3.25, 'staircase', color=BLUE, fontsize=7.4)
    dimy(a, 7.90, y1, y0, r'$h$', color=G)
    txt(a, .30, 4.24, 'three paths, one work', color=T, fontsize=7.8)

    b = panel(fig, [.55, .18, .41, .64])
    axes2(b, r'height dropped  (m)', r'work by gravity  (J)')
    h = np.linspace(0, 4, 300)
    b.plot(h, 2 * 9.8 * h, color=T, lw=2.2)
    b.text(1.35, 62, r'$W=mgh$', fontsize=8.6, color=T)
    b.set_xlim(0, 4); b.set_ylim(0, 82)
    head(b, 'path-independent, so a potential exists')
    return 'A force is conservative exactly when its work is path-independent: then it has a potential'


def pe_definition(fig):
    a = panel(fig, [.06, .22, .385, .60])
    axes2(a, r'extension $x$  (m)', r'$U$  (J)')
    x = np.linspace(-.3, .3, 300)
    a.plot(x, .5 * 200 * x ** 2, color=T, lw=2.2)
    a.plot([.3], [.5 * 200 * .09], 'o', ms=5, color=R, zorder=5)
    a.plot([-.3, -.3], [0, 9], color=HG, lw=.9, ls=(0, (2, 2)))
    a.plot([.3, .3], [0, 9], color=HG, lw=.9, ls=(0, (2, 2)))
    a.text(-.26, 9.5, r'$-x_0$', fontsize=7.4, color=G)
    a.text(.20, 9.5, r'$+x_0$', fontsize=7.4, color=G)
    a.text(-.05, 6.2, r'$U=\frac{1}{2}kx^2$', fontsize=8.2, color=T)
    a.set_xticks([-.3, -.2, -.1, 0, .1, .2, .3])
    a.set_xlim(-.34, .34); a.set_ylim(0, 10.4)
    head(a, 'the spring well')

    b = panel(fig, [.615, .22, .36, .60])
    axes2(b, r'height above the chosen zero  (m)', r'$U=mgh$  (J)')
    h = np.linspace(0, 5, 100)
    b.plot(h, 2 * 9.8 * h, color=GOLD, lw=2.2)
    b.axvline(0, color=I, lw=.9)
    b.text(.3, 78, 'reference is a choice', fontsize=7.4, color=G)
    b.set_xlim(0, 5); b.set_ylim(0, 104)
    head(b, 'the zero can sit anywhere')
    return 'Potential energy is defined by minus the work a conservative force does: only differences matter'


def spring_work(fig):
    a = panel(fig, [.05, .14, .44, .72], xlim=(0, 10), ylim=(0, 4.6))
    a.plot([.50, 9.50], [.90, .90], color=I, lw=1.8)
    a.add_patch(Rectangle((.50, .90), .55, 1.30, fc='#e8eef0', ec=I, lw=1.4))
    spring(a, (1.05, 1.55), (4.15, 1.55), n=10, amp=.20, color=I, lw=1.6)
    block(a, 4.80, 1.55, 1.00, 1.10, '#fdf0bd', GOLD)
    arrow(a, (5.40, 1.55), (7.40, 1.55), T, 1.8)
    txt(a, 6.20, 1.80, r'$v$', color=T, fontsize=9.0)
    force(a, (1.05, 2.55), (2.55, 2.55), R, 1.7, None)
    txt(a, 2.00, 2.72, 'restoring pull', color=R, fontsize=7.4)
    dimx(a, 1.05, 4.15, .45, r'$x$', color=G)
    txt(a, .35, 4.15, 'stretch it, and the spring fights back', color=T, fontsize=7.8)

    b = panel(fig, [.55, .18, .41, .64])
    axes2(b, r'extension  (cm)', r'stored energy  (J)')
    x = np.linspace(0, 10, 300)
    for k, c, lab in ((200, T, '200 N/m'), (400, R, '400 N/m')):
        b.plot(x, .5 * k * (x / 100) ** 2, color=c, lw=2.0, label=lab)
    b.legend(frameon=False, fontsize=7.2, loc='upper left')
    b.set_xlim(0, 10); b.set_ylim(0, 2.2)
    head(b, 'double the k, double the energy')
    return 'The spring stores half k x squared, because its force averages to half its final value'


def gravity_paths(fig):
    a = panel(fig, [.03, .14, .44, .72], xlim=(0, 10), ylim=(0, 4.6))
    a.plot([.50, 9.50], [.80, .80], color=I, lw=1.8)
    a.plot([1.10, 1.10], [3.80, .80], color=HG, lw=1.0, ls=(0, (3, 3)))
    a.plot([1.10, 8.40], [3.80, .80], color=T, lw=1.9)
    a.plot([1.10, 4.40], [3.80, 3.80], color=GOLD, lw=1.9)
    a.plot([4.40, 4.40], [3.80, .80], color=GOLD, lw=1.9)
    xs = np.linspace(1.10, 8.40, 200)
    a.plot(xs, 3.80 - 3.00 * ((xs - 1.10) / 7.30) ** 2, color=G, lw=1.7, ls=(0, (5, 2)))
    a.plot([1.10], [3.80], 'o', ms=5.5, color=I)
    a.plot([8.40], [.80], 'o', ms=5.5, color=I)
    txt(a, .62, 3.32, r'$A$', fontsize=9.0, color=I)
    txt(a, 8.58, .46, r'$B$', fontsize=9.0, color=I)
    dimy(a, 8.30, .80, 3.80, r'$h$', color=G)
    txt(a, .35, 4.38, 'three paths, one work', color=T, fontsize=7.8)

    b = panel(fig, [.56, .20, .40, .62])
    axes2(b, r'height  (m)', r'$U=mgh$  (J)')
    h = np.linspace(0, 5, 200)
    b.plot(h, 9.8 * h, color=T, lw=2.2)
    b.fill_between(h[:0], 0, 0, color=T)
    b.set_xlim(0, 5); b.set_ylim(0, 52)
    b.text(.5, 40, r'$U$ rises exactly as fast', fontsize=7.4, color=G)
    head(b, 'the height is the whole story')
    return 'For gravity the path is irrelevant, so the energy depends only on the endpoints'


def energy_ledger(fig):
    a = panel(fig, [.04, .20, .44, .64])
    axes2(a, '', r'energy  (J)')
    bars(a, ['K', 'U', 'E'], [70, 10, 80], colors=[R, BLUE, T])
    a.set_ylim(0, 95)
    head(a, 'at the top: mostly potential')

    b = panel(fig, [.56, .20, .40, .62])
    axes2(b, '', r'energy  (J)')
    bars(b, ['K', 'U', 'E'], [10, 70, 80], colors=[R, BLUE, T])
    b.set_ylim(0, 95)
    head(b, 'at the bottom: mostly kinetic')
    return 'Mechanical energy is conserved exactly when no non-conservative force does net work'


def u_landscape(fig):
    a = panel(fig, [.05, .20, .43, .64])
    axes2(a, r'position $x$', r'$U(x)$')
    x = np.linspace(0, 10, 400)
    U = .55 * (x - 2.2) ** 2 - 1.4 * np.cos((x - 2.2) * 1.5) + 1.2
    a.plot(x, U, color=T, lw=2.3)
    E = 5.2
    a.axhline(E, color=R, lw=1.2, ls=(0, (4, 2)))
    a.text(.25, E + .35, r'$E$', fontsize=8.4, color=R)
    idx = np.where(np.diff(np.sign(U - E)) != 0)[0]
    for i in idx[:4]:
        a.plot(x[i], E, 'o', ms=4.5, color=R, zorder=5)
    a.set_xlim(0, 10); a.set_ylim(-2.2, 9.4)
    head(a, r'turning points where $U=E$')

    b = panel(fig, [.57, .20, .39, .62])
    axes2(b, r'position $x$', r'$K=E-U$')
    K = np.clip(E - U, 0, None)
    b.plot(x, K, color=R, lw=2.2)
    b.fill_between(x, 0, K, color=R, alpha=.12, lw=0)
    b.set_xlim(0, 10); b.set_ylim(0, 9.4)
    head(b, 'speed lives in the gap')
    return 'Send a horizontal energy line across the curve: it can only be where the line is above U'


def force_gradient(fig):
    a = panel(fig, [.05, .20, .43, .64])
    axes2(a, r'position $x$', r'$U(x)$')
    x = np.linspace(0, 10, 400)
    U = 2.2 * np.sin(x * .62) + .28 * x
    a.plot(x, U, color=T, lw=2.3)
    for xv in (1.6, 4.9, 8.0):
        i = int(xv / 10 * 399)
        d = np.gradient(U, x)[i]
        a.plot([x[i] - .8, x[i] + .8], [U[i] - .8 * d, U[i] + .8 * d], color=R, lw=1.6)
    a.set_xlim(0, 10); a.set_ylim(-1.6, 5.4)
    head(a, 'the slope is the force, reversed')

    b = panel(fig, [.57, .20, .39, .62])
    axes2(b, r'position $x$', r'$F=-dU/dx$')
    b.plot(x, -np.gradient(U, x), color=R, lw=2.2)
    b.axhline(0, color=I, lw=.9)
    b.set_xlim(0, 10); b.set_ylim(-2.0, 2.0)
    head(b, 'force points downhill')
    return 'The force is minus the gradient of the potential: steep fall means strong pull'


def decision_map(fig):
    a = panel(fig, [.03, .12, .46, .76], xlim=(0, 10), ylim=(0, 4.6))
    a.axis('off')
    rows = [('speed at B', 'energy', T), ('distance travelled', 'energy + friction', T),
            ('does it reach?', 'compare E with U', GOLD),
            ('force at B', 'energy, then radial', BLUE),
            ('time or acceleration', 'forces', R)]
    a.text(.35, 4.28, 'what the question asks decides the method', fontsize=7.8, color=T)
    for i, (q, m, c) in enumerate(rows):
        y = 3.62 - i * .74
        a.add_patch(Rectangle((.30, y), 4.05, .58, fc='white', ec='#cfe1dc', lw=1.2))
        a.text(.45, y + .29, q, va='center', fontsize=7.6, color=I)
        arrow(a, (4.45, y + .29), (5.40, y + .29), c, 1.4)
        a.text(5.55, y + .29, m, va='center', fontsize=7.6, color=c)

    b = panel(fig, [.56, .16, .40, .68], xlim=(0, 10), ylim=(0, 4.6), equal=True)
    C = (5.0, 2.30)
    b.add_patch(Circle(C, 1.55, fc='none', ec=HG, lw=1.3, ls=(0, (3, 3))))
    b.plot([C[0], C[0]], [C[1], C[1] + 1.55], color=I, lw=1.1, ls=(0, (2, 2)))
    ball(b, C[0], C[1] + 1.55, .19, '#f6dedb', R)
    arrow(b, (C[0], C[1] + 1.55), (C[0] + .95, C[1] + 1.55), T, 1.5)
    txt(b, C[0] + 1.02, C[1] + 1.28, r'$v$', color=T, fontsize=8.6)
    arrow(b, (C[0], C[1] + 1.36), (C[0], C[1] + .55), BLUE, 1.5)
    txt(b, C[0] - .55, C[1] + .85, r'$N$', color=BLUE, fontsize=8.6)
    b.text(5.0, .55, 'energy gives the speed,\nthe radial equation gives the force', ha='center',
           fontsize=7.0, color=G)
    head(b, 'the standard pair')
    return 'Energy answers how fast and how far; forces answer how long and how hard'


def system_energy(fig):
    a = panel(fig, [.03, .16, .46, .70], xlim=(0, 10), ylim=(0, 4.6))
    a.plot([.40, 9.60], [1.00, 1.00], color=I, lw=1.8)
    block(a, 2.30, 1.55, 1.10, 1.05, '#fdf0bd', GOLD)
    block(a, 6.50, 1.55, 1.45, 1.05, '#f6dedb', R)
    spring(a, (2.90, 1.55), (5.75, 1.55), n=10, amp=.18, color=I, lw=1.5)
    arrow(a, (2.90, 2.45), (4.00, 2.45), T, 1.6)
    txt(a, 3.10, 2.62, r'$v_1$', color=T, fontsize=8.4)
    arrow(a, (7.30, 2.45), (8.20, 2.45), T, 1.6)
    txt(a, 7.45, 2.62, r'$v_2$', color=T, fontsize=8.4)
    txt(a, .35, 4.15, 'the spring is internal, so it only stores energy', color=T, fontsize=7.6)
    txt(a, .35, 3.55, r'$W_{\rm ext}=\Delta K+\Delta U_s$', color=G, fontsize=8.4)

    b = panel(fig, [.56, .20, .40, .62])
    axes2(b, '', r'kinetic energy  (J)')
    bars(b, ['CM', 'internal', 'total'], [12, 5, 17], colors=[BLUE, GOLD, T])
    b.set_ylim(0, 20)
    head(b, 'the split is not a choice')
    return 'For a system, external work changes the total energy; internal forces only move it around'


def efficiency(fig):
    a = panel(fig, [.03, .14, .46, .72], xlim=(0, 10), ylim=(0, 4.6))
    a.axis('off')
    a.add_patch(Rectangle((.40, 2.70), 2.40, .95, fc=PALE, ec='#9ccdc4', lw=1.4))
    a.text(1.60, 3.17, 'motor', ha='center', va='center', fontsize=8.2, color=T)
    a.add_patch(Rectangle((.40, .85), 2.40, .95, fc='white', ec='#cfe1dc', lw=1.4))
    a.text(1.60, 1.32, 'pump', ha='center', va='center', fontsize=8.2, color=I)
    arrow(a, (1.60, 2.66), (1.60, 1.84), T, 1.6)
    arrow(a, (2.85, 1.32), (4.10, 1.32), T, 1.6)
    a.text(3.30, 1.52, r'$\dot mgh$', fontsize=8.4, color=T)
    arrow(a, (2.85, 3.17), (4.10, 3.17), R, 1.6)
    a.text(3.20, 3.36, 'heat, sound', fontsize=7.4, color=R)
    a.text(.40, 4.12, 'the water gets less than the motor gives', fontsize=7.8, color=T)
    a.text(4.30, 2.10, r'$\eta=\frac{\dot mgh}{P_{\rm in}}$', fontsize=10.0, color=GOLD)

    b = panel(fig, [.57, .20, .39, .62])
    axes2(b, r'flow rate  (kg/s)', r'efficiency  (%)')
    q = np.linspace(0.5, 10, 300)
    b.plot(q, 100 * q / (q + 3.5), color=T, lw=2.2)
    b.set_xlim(0, 10); b.set_ylim(0, 100)
    head(b, 'friction losses matter most at low flow')
    return 'Efficiency is output over input, and every loss is a term you can name'


def chain_energy(fig):
    a = panel(fig, [.03, .14, .44, .72], xlim=(0, 10), ylim=(0, 4.6))
    a.plot([.40, 9.60], [.70, .70], color=I, lw=1.8)
    for i in range(9):
        a.add_patch(Circle((1.05 + .55 * (i % 3), .92 + .52 * (i // 3)), .16,
                           fc='#fdf0bd', ec=GOLD, lw=1.0))
    for y in np.arange(3.90, 1.60, -.30):
        a.add_patch(Circle((4.30, y), .15, fc='#fdf0bd', ec=GOLD, lw=1.0))
    arrow(a, (4.30, 3.95), (4.30, 4.45), T, 1.8)
    txt(a, 4.48, 4.32, r'$v$', color=T, fontsize=8.8)
    force(a, (4.30, 2.60), (5.60, 2.60), R, 1.6)
    txt(a, 5.70, 2.66, r'$F$', color=R, fontsize=8.8)
    dimy(a, 3.55, .70, 4.05, r'$x$', color=G)
    txt(a, 5.95, 3.55, 'mass joins a moving system', color=T, fontsize=7.6)

    b = panel(fig, [.56, .20, .40, .62])
    axes2(b, r'lifted length $x$  (m)', r'pull  $F$  (N)')
    x = np.linspace(0, 3, 300)
    b.plot(x, 2.0 * 9.8 * x / 3 + 0.9, color=T, lw=2.2)
    b.plot([0], [0.9], 'o', ms=5, color=R, zorder=5)
    b.text(.15, 1.35, r'$\lambda v^2$', fontsize=8.0, color=R)
    b.text(1.35, 12.5, r'$\lambda gx$', fontsize=8.0, color=T)
    b.set_xlim(0, 3); b.set_ylim(0, 22)
    head(b, 'weight plus momentum flux')
    return 'A chain lifted at constant speed needs more than its weight: the new links must be accelerated'


def spring_friction(fig):
    a = panel(fig, [.03, .14, .44, .72], xlim=(0, 10), ylim=(0, 4.6))
    a.plot([.40, 9.60], [.95, .95], color=I, lw=1.8)
    for x in np.linspace(.7, 9.2, 24):
        a.plot([x, x + .26], [.82, 1.08], color=HG, lw=.9)
    a.add_patch(Rectangle((.40, .95), .45, 1.10, fc='#e8eef0', ec=I, lw=1.3))
    spring(a, (.85, 1.50), (2.55, 1.50), n=8, amp=.17, color=I, lw=1.5)
    block(a, 3.10, 1.50, .95, .95, '#fdf0bd', GOLD)
    force(a, (2.65, 1.28), (1.85, 1.28), R, 1.5)
    txt(a, 1.80, 1.06, r'$f_k$', color=R, fontsize=8.4)
    arrow(a, (3.60, 2.15), (4.70, 2.15), T, 1.6)
    txt(a, 3.85, 2.32, r'$v$', color=T, fontsize=8.6)
    dimx(a, 1.60, 6.10, .50, r'$d$', color=G)
    txt(a, .35, 4.15, 'launched by a spring, stopped by friction', color=T, fontsize=7.8)

    b = panel(fig, [.56, .20, .40, .62])
    axes2(b, r'distance from release  (m)', r'energy  (J)')
    s = np.linspace(0, 2.4, 300)
    b.plot(s, 9.0 - 4.0 * s, color=T, lw=2.1, label='mechanical')
    b.plot(s, 4.0 * s, color=R, lw=1.9, label='thermal')
    b.legend(frameon=False, fontsize=7.0, loc='center right')
    b.set_xlim(0, 2.4); b.set_ylim(0, 11)
    head(b, 'stored energy becomes heat')
    return 'Where a spring and friction act together, track the stored energy and the heat separately'


def slope_power(fig):
    a = panel(fig, [.03, .16, .44, .70], xlim=(0, 10), ylim=(0, 4.6))
    a.add_patch(Polygon([(.40, .80), (9.60, .80), (9.60, 2.90)], closed=True,
                        fc='#f2f6f5', ec=I, lw=1.6))
    th = 12.5
    cx, cy = 4.40, .80 + (4.40 - .40) * np.tan(np.radians(th)) + .42
    rot_block(a, cx, cy, 1.55, .72, th, '#fdf0bd', GOLD)
    force(a, (cx + .55, cy + .22), (cx + 1.75, cy + .55), R, 1.7)
    txt(a, cx + 1.80, cy + .62, r'$F$', color=R, fontsize=8.6)
    force(a, (cx, cy + .20), (cx - .75, cy - .18), GOLD, 1.5)
    txt(a, cx - 2.05, cy - .40, r'$mg\sin\theta$', color=GOLD, fontsize=7.8)
    arrow(a, (cx + .10, cy + .50), (cx + 1.35, cy + .85), T, 1.5)
    txt(a, cx + .45, cy + 1.00, r'$v$', color=T, fontsize=8.6)
    a.text(.35, 4.12, 'climbing costs power every second you keep going', fontsize=7.6, color=T)

    b = panel(fig, [.56, .20, .40, .62])
    axes2(b, r'speed  (m/s)', r'engine power  (kW)')
    v = np.linspace(0, 30, 300)
    for ang, c, lab in ((0, T, r'$0^{\circ}$'), (5, GOLD, r'$5^{\circ}$'), (10, R, r'$10^{\circ}$')):
        b.plot(v, (500 + 1000 * 9.8 * np.sin(np.radians(ang))) * v / 1000, color=c, lw=2.0,
               label=lab)
    b.legend(frameon=False, fontsize=7.0, loc='upper left', title='grade', title_fontsize=7)
    b.set_xlim(0, 30); b.set_ylim(0, 70)
    head(b, '1 t car, 500 N of drag')
    return 'Climbing at speed v needs mgv sin(theta) just to gain height, before any drag'


def wpe_map(fig):
    a = panel(fig, [.03, .10, .42, .78], xlim=(0, 10), ylim=(0, 4.6))
    a.axis('off')
    tiles = [('work', 'F d cos', 0, 2), ('theorem', r'$W=\Delta K$', 1, 2),
             ('power', r'$F\cdot v$', 0, 1), ('potential', r'$-\int F dx$', 1, 1),
             ('conservation', r'$E$ constant', 0, 0), ('bookkeeping', r'$W_{\rm nc}=\Delta E$', 1, 0)]
    a.text(.30, 4.22, 'six ideas, two of them bookkeeping', fontsize=7.8, color=T)
    for name, f, i, j in tiles:
        x, y = .35 + i * 4.42, .55 + j * 1.18
        a.add_patch(Rectangle((x, y), 4.05, .96, fc=PALE if i == 0 else 'white',
                              ec='#9ccdc4', lw=1.3,
                              ls='-' if i == 0 else (0, (4, 2))))
        a.text(x + .18, y + .74, name, fontsize=7.6, color=T)
        a.text(x + .18, y + .17, f, fontsize=8.8, color=I)

    b = panel(fig, [.56, .16, .40, .68])
    axes2(b, r'position', r'energy')
    x = np.linspace(0, 10, 300)
    b.plot(x, 6 + 0 * x, color=HG, lw=1.2, ls=(0, (3, 3)))
    b.plot(x, 6 - .35 * x, color=R, lw=2.1)
    b.text(.35, 6.45, 'without friction', fontsize=7.2, color=G)
    b.text(4.2, 3.05, 'with friction', fontsize=7.2, color=R)
    b.set_xlim(0, 10); b.set_ylim(0, 9)
    head(b, 'one line for the whole chapter')
    return 'Work is the accounting unit: every result here is a ledger with a named loss term'
