"""Part II figures: the Olympiad layer of work, energy and power."""
import numpy as np
from matplotlib.patches import Rectangle, Circle, Arc, Polygon
from figlib import (I, T, R, G, GOLD, HG, BLUE, GREEN, PALE, YEL, WATER,
                    txt, head, foot, arrow, panel, axes2, dimx, dimy, incline,
                    block, force, dashed, ball, spring, bars, shade_between,
                    arcarrow, rot_block)


def cm_decomposition(fig):
    a = panel(fig, [.03, .16, .46, .70], xlim=(0, 10), ylim=(0, 4.6))
    a.plot([.40, 9.60], [1.05, 1.05], color=I, lw=1.8)
    block(a, 2.10, 1.55, 1.05, 1.00, '#fdf0bd', GOLD)
    block(a, 5.60, 1.55, 1.75, 1.00, '#f6dedb', R)
    a.plot([3.95], [1.05], 'o', ms=6, color=T, zorder=6)
    txt(a, 3.72, .72, 'CM', color=T, fontsize=7.8)
    arrow(a, (2.10, 2.55), (3.30, 2.55), GOLD, 1.6)
    txt(a, 2.30, 2.72, r'$v_1$', color=GOLD, fontsize=8.2)
    arrow(a, (5.60, 2.55), (7.30, 2.55), R, 1.6)
    txt(a, 5.85, 2.72, r'$v_2$', color=R, fontsize=8.2)
    txt(a, .35, 4.14, 'split the motion into drift plus internal motion', color=T, fontsize=7.6)
    txt(a, .35, 3.55, r'$K=\frac{1}{2}Mv_{\rm cm}^2+\frac{1}{2}\mu v_{\rm rel}^2$',
        color=G, fontsize=9.0)

    b = panel(fig, [.57, .20, .39, .62])
    axes2(b, r'mass ratio $m_2/m_1$', r'share of $K$ in the CM motion')
    r = np.linspace(.05, 6, 400)
    b.plot(r, (1 + r) / (2 + r + 1 / r) * 1.0, color=T, lw=2.2)
    b.axhline(.5, color=HG, lw=1.0, ls=(0, (3, 3)))
    b.text(3.1, .54, 'half at equal masses', fontsize=7.2, color=G)
    b.set_xlim(0, 6); b.set_ylim(0, 1.05)
    head(b, 'the drift usually carries most of it')
    return 'Total kinetic energy splits into CM drift plus internal motion, and only the internal part can be converted'


def effective_potential(fig):
    a = panel(fig, [.05, .20, .43, .64])
    axes2(a, r'radius $r$', r'$U_{\rm eff}$')
    r = np.linspace(.55, 9, 400)
    a.plot(r, -3.0 / r + 0.95 / r ** 2, color=T, lw=2.2)
    a.plot(r, -3.0 / r + 2.2 / r ** 2, color=GOLD, lw=1.8, ls=(0, (5, 2)))
    a.plot(r, -3.0 / r, color=HG, lw=1.2, ls=(0, (3, 3)))
    a.axhline(0, color=I, lw=.8)
    a.set_xlim(0, 9); a.set_ylim(-1.3, .9)
    head(a, 'angular momentum lifts the floor')

    b = panel(fig, [.58, .20, .38, .62])
    axes2(b, r'angular momentum $L$', r'circular radius')
    L = np.linspace(.6, 4, 300)
    b.plot(L, L ** 2 / 3.0, color=R, lw=2.2)
    b.text(1.0, 3.6, r'$r=L^2/(GMm^2)$', fontsize=7.6, color=R)
    b.set_xlim(0, 4); b.set_ylim(0, 6.4)
    head(b, 'one radius for each L')
    return 'The centrifugal term is not a force; it is the angular part of the kinetic energy, and it sets the orbit'


def bounce_energy(fig):
    a = panel(fig, [.04, .12, .46, .76], xlim=(0, 10), ylim=(0, 4.6))
    a.plot([.40, 9.60], [.80, .80], color=I, lw=1.8)
    x, y = .90, 3.90
    ball(a, x, y, .15)
    a.plot([.90, 1.55], [3.90, .80], color=T, lw=1.2)
    xs = 1.55
    h = 3.10
    for i in range(5):
        seg = .55 + .95 * np.sqrt(h / 3.10)
        s = np.linspace(0, 1, 40)
        a.plot(xs + s * seg, .80 + h * 4 * s * (1 - s), color=T, lw=1.3)
        xs += seg
        h *= .64
    txt(a, .40, 4.24, r'heights fall by $e^2$ each bounce', color=T, fontsize=7.8)

    b = panel(fig, [.57, .20, .39, .62])
    axes2(b, r'bounce number $n$', r'energy left  (fraction)')
    n = np.arange(0, 9)
    b.plot(n, .64 ** n, 'o-', ms=4.5, color=T, lw=1.8)
    b.set_xlim(-.3, 8.3); b.set_ylim(0, 1.08)
    b.set_xticks(range(0, 9, 2))
    head(b, r'$e=0.8$: each bounce keeps $e^2=64\%$')
    return 'Each bounce keeps a fraction e squared of the energy, so an infinite sequence still has a finite budget'


def rolling_energy(fig):
    a = panel(fig, [.03, .14, .44, .72], xlim=(0, 10), ylim=(0, 4.6), equal=True)
    a.plot([.40, 9.60], [.75, .75], color=I, lw=1.8)
    a.add_patch(Circle((4.30, 2.55), 1.55, fc='#fdf0bd', ec=GOLD, lw=1.6))
    a.plot([4.30, 5.80], [2.55, 2.55], color=HG, lw=2.6)
    a.plot([4.30, 4.30], [2.55, 1.00], color=HG, lw=1.2, ls=(0, (3, 2)))
    a.plot([4.30], [1.00], 'o', ms=6, color=R, zorder=6)
    arrow(a, (4.30, 3.55), (5.55, 3.55), T, 1.6)
    txt(a, 4.75, 3.72, r'$v$', color=T, fontsize=8.6)
    arcarrow(a, (4.30, 2.55), .95, -40, 80, color=BLUE)
    txt(a, 3.05, 2.95, r'$\omega$', color=BLUE, fontsize=8.6)
    txt(a, .35, 4.22, 'contact point at rest, centre moving', color=T, fontsize=7.6)
    txt(a, .35, .18, 'rolling shares the energy between two motions', color=G, fontsize=7.2)

    b = panel(fig, [.56, .20, .40, .62])
    axes2(b, '', r'$K/(mv^2)$')
    b.set_xticks(range(3))
    bars(b, ['ring', 'disc', 'sphere'], [1.0, .75, .70], colors=[GOLD, T, BLUE])
    b.set_ylim(0, 1.2)
    head(b, 'the ring pays the most')
    return 'A rolling body carries translational and rotational energy together; the split depends only on the shape'


def wedge_energy(fig):
    a = panel(fig, [.03, .14, .46, .72], xlim=(0, 10), ylim=(0, 4.6))
    a.plot([.40, 9.60], [.80, .80], color=I, lw=1.8)
    a.add_patch(Polygon([(1.10, .80), (5.90, .80), (5.90, 3.30)], closed=True,
                        fc='#f2f6f5', ec=I, lw=1.6))
    rot_block(a, 2.90, 1.62, 1.05, .46, 26, '#fdf0bd', GOLD)
    arrow(a, (2.90, 1.62), (3.85, 1.10), T, 1.7)
    txt(a, 3.95, 1.02, r'$u$ along face', color=T, fontsize=7.6)
    arrow(a, (5.90, .55), (7.20, .55), R, 1.7)
    txt(a, 6.10, .28, r'$V$ wedge', color=R, fontsize=7.6)
    txt(a, .35, 4.14, 'the block slides AND the wedge recoils', color=T, fontsize=7.6)

    b = panel(fig, [.57, .20, .39, .62])
    axes2(b, r'$M/m$', r'$v_b/\sqrt{2gh}$')
    M = np.linspace(.05, 8, 400)
    th = np.radians(30)
    vb = np.sqrt((M + np.sin(th) ** 2) ** -1 * (M + 1) * (np.sin(th) ** 2 + (M / (M + 1)) ** 2 * np.cos(th) ** 2))
    b.plot(M, vb, color=T, lw=2.2)
    b.axhline(1.0, color=HG, lw=1.0, ls=(0, (3, 3)))
    b.text(4.0, 1.03, 'fixed wedge', fontsize=7.0, color=G)
    b.set_xlim(0, 8); b.set_ylim(.6, 1.06)
    head(b, r'theta $=30^{\circ}$')
    return 'The block on a moving wedge loses speed to the wedge: root 2gh is the fixed-wedge answer only'


def launch_energy(fig):
    a = panel(fig, [.05, .20, .43, .64])
    axes2(a, r'radius $r/R_E$', r'$U=-GMm/r$')
    r = np.linspace(1, 6, 400)
    a.plot(r, -1 / r, color=T, lw=2.2)
    a.axhline(-.5, color=R, lw=1.1, ls=(0, (4, 2)))
    a.axhline(0, color=I, lw=.8)
    a.text(3.2, -.44, 'low orbit', fontsize=7.2, color=R)
    a.text(3.2, .06, 'escape', fontsize=7.2, color=G)
    a.set_xlim(0, 6); a.set_ylim(-1.1, .16)
    head(a, 'surface sits deep in the well')

    b = panel(fig, [.58, .20, .38, .62])
    axes2(b, r'orbit radius $r/R_E$', r'$\Delta E/\Delta E_{\rm esc}$')
    rr = np.linspace(1, 6, 300)
    b.plot(rr, 1 - 1 / (2 * rr), color=T, lw=2.2)
    b.plot([1], [.5], 'o', ms=5.5, color=R, zorder=5)
    b.text(1.5, .46, '1/2 for low orbit', fontsize=7.2, color=R)
    b.set_xlim(0, 6); b.set_ylim(0, 1.05)
    head(b, 'half the escape budget buys orbit')
    return 'Reaching orbit costs half the escape energy, and the other half is the speed you must keep'


def chain_unroll(fig):
    a = panel(fig, [.03, .14, .44, .72], xlim=(0, 10), ylim=(0, 4.6))
    a.plot([.40, 9.60], [.80, .80], color=I, lw=1.8)
    for i in range(12):
        a.add_patch(Circle((1.00 + .52 * (i % 4), .98 + .50 * (i // 4)), .15,
                           fc='#fdf0bd', ec=GOLD, lw=1.0))
    for y in np.arange(3.90, 1.55, -.30):
        a.add_patch(Circle((5.30, y), .14, fc='#fdf0bd', ec=GOLD, lw=1.0))
    a.plot([5.30, 5.30], [1.40, .95], color=GOLD, lw=1.2)
    arrow(a, (5.30, 4.05), (5.30, 4.55), T, 1.8)
    txt(a, 5.55, 4.30, r'$v$', color=T, fontsize=8.6)
    dimy(a, 4.45, .80, 4.05, r'$x$', color=G)
    txt(a, .35, 4.16, 'links start from rest, one after another', color=T, fontsize=7.6)

    b = panel(fig, [.56, .20, .40, .62])
    axes2(b, r'lifted length $x$  (m)', r'$dE/dt$  and  $Fv$  (W)')
    x = np.linspace(0, 3, 300)
    b.plot(x, 2.0 * 9.8 * x / 3 * 1.2, color=T, lw=2.0, label='Fv')
    b.plot(x, 2.0 * 9.8 * x / 3 * 1.2 - .45, color=R, lw=1.8, ls=(0, (5, 2)),
           label='dE/dt')
    b.legend(frameon=False, fontsize=7.0, loc='upper left')
    b.set_xlim(0, 3); b.set_ylim(0, 26)
    head(b, 'the gap never closes')
    return 'Pulling a chain out of a heap costs an extra half-lambda v cubed per second: the links are being hit'


def bead_energy(fig):
    a = panel(fig, [.03, .14, .46, .72], xlim=(0, 10), ylim=(0, 4.6), equal=True)
    C = (5.0, 2.55)
    a.add_patch(Circle(C, 1.75, fc='none', ec=HG, lw=1.5))
    a.plot([C[0], C[0]], [C[1] - 2.05, C[1] + 2.05], color=I, lw=1.3, ls=(0, (6, 3)))
    th = np.radians(52)
    bx, by = C[0] + 1.75 * np.sin(th), C[1] - 1.75 * np.cos(th)
    ball(a, bx, by, .18, '#f6dedb', R)
    a.plot([bx, C[0]], [by, C[1]], color=HG, lw=1.0, ls=(0, (2, 2)))
    arcarrow(a, C, .75, 250, 250 + 52, color=T)
    txt(a, C[0] + .10, C[1] - .92, r'$\theta$', color=T, fontsize=8.6)
    arcarrow(a, C, 2.05, 200, 340, color=BLUE)
    txt(a, C[0] - 2.42, C[1] + .92, r'$\omega$', color=BLUE, fontsize=8.6)
    txt(a, .35, 4.34, 'the hoop decides where the bead sits', color=T, fontsize=7.6)

    b = panel(fig, [.57, .18, .39, .66])
    axes2(b, r'angle $\theta$  (deg)', r'$U_{\rm eff}$')
    tt = np.linspace(0, 180, 400)
    for w, c, lab in ((2.0, T, r'slow'), (3.6, GOLD, r'$w=1.2\,w_c$'), (5.0, R, r'fast')):
        lam = (w ** 2 * 1.0) / 9.8
        b.plot(tt, -np.cos(np.radians(tt)) - .5 * lam * np.sin(np.radians(tt)) ** 2,
               color=c, lw=2.0, label=lab)
    b.legend(frameon=False, fontsize=6.8, loc='upper left')
    b.set_xlim(0, 180); b.set_ylim(-1.6, .4)
    head(b, 'a well that moves')
    return 'A rotating constraint tilts the potential: above the critical speed the bottom becomes unstable'


def restitution_energy(fig):
    a = panel(fig, [.05, .14, .44, .72], xlim=(0, 10), ylim=(0, 4.6))
    a.plot([.40, 9.60], [.80, .80], color=I, lw=1.8)
    for x, h, c in ((1.60, 3.30, T), (3.30, 2.30, T), (4.60, 1.60, T),
                    (5.60, 1.12, T), (6.35, .78, T)):
        a.plot([x, x], [.80, .80 + h], color=HG, lw=.8, ls=(0, (2, 2)))
        ball(a, x, .80 + h, .13, '#fdf0bd', GOLD)
    a.plot([.40, 9.60], [.80, .80], color=I, lw=1.8)
    txt(a, .40, 4.24, r'$h_{n+1}=e^2h_n$', color=T, fontsize=9.0)
    txt(a, .40, 2.10, 'each bounce keeps $e^2$\nof the energy of the last', color=G, fontsize=7.4)

    b = panel(fig, [.55, .20, .41, .62])
    axes2(b, r'restitution $e$', r'fraction of energy kept, $e^2$')
    e = np.linspace(0, 1, 300)
    b.plot(e, e ** 2, color=T, lw=2.2)
    b.plot([.8], [.64], 'o', ms=5.5, color=R, zorder=5)
    b.text(.30, .72, r'$e=0.8$: $64\%$', fontsize=7.4, color=R)
    b.set_xlim(0, 1); b.set_ylim(0, 1.05)
    head(b, 'a bounce is a ratio, not a subtraction')
    return 'Restitution multiplies the speed by e, so it multiplies the energy by e squared'


def flywheel(fig):
    a = panel(fig, [.03, .14, .44, .72], xlim=(0, 10), ylim=(0, 4.6), equal=True)
    C = (4.80, 2.20)
    a.add_patch(Circle(C, 1.50, fc='#f7fbfa', ec=I, lw=1.8))
    a.add_patch(Circle(C, .25, fc='white', ec=I, lw=1.4))
    for k in range(6):
        t = k * np.pi / 3
        a.plot([C[0] + .25 * np.cos(t), C[0] + 1.50 * np.cos(t)],
               [C[1] + .25 * np.sin(t), C[1] + 1.50 * np.sin(t)], color=HG, lw=1.2)
    arcarrow(a, C, 1.88, -50, 40, color=BLUE)
    txt(a, C[0] + 1.95, C[1] + 1.05, r'$\omega$', color=BLUE, fontsize=8.6)
    txt(a, .35, 4.30, 'a constant-power motor cannot spin up a wheel linearly', color=T, fontsize=7.4)

    b = panel(fig, [.56, .20, .40, .62])
    axes2(b, r'time  (s)', r'speed  $\omega$  (rad/s)')
    t = np.linspace(0, 10, 300)
    b.plot(t, np.sqrt(2 * 500 * t / 12), color=T, lw=2.2)
    b.plot(t, np.sqrt(2 * 500 * t / 12)[-1] / 10 * t, color=HG, lw=1.1, ls=(0, (3, 3)))
    b.text(4.6, 5.2, r'$\omega=\sqrt{2Pt/I}$', fontsize=8.2, color=T)
    b.set_xlim(0, 10); b.set_ylim(0, 30)
    head(b, 'power divided by torque is angular speed')
    return 'At constant power the torque falls as 1/omega, so the wheel gains angular speed as root t'


def pseudo_work(fig):
    a = panel(fig, [.03, .14, .44, .72], xlim=(0, 10), ylim=(0, 4.6))
    a.plot([.40, 9.60], [.80, .80], color=I, lw=1.8)
    a.add_patch(Rectangle((1.00, .80), 6.60, .34, fc='#e8eef0', ec=I, lw=1.4))
    a.add_patch(Rectangle((1.00, .80), .30, 1.05, fc='#e8eef0', ec=I, lw=1.2))
    ball(a, 4.40, 1.40, .22, '#fdf0bd', GOLD)
    a.plot([4.40 - .22, 4.40 - .22], [1.14, .80], color=I, lw=1.1)
    arrow(a, (1.20, 2.15), (2.80, 2.15), T, 1.7)
    txt(a, 1.35, 2.32, r'$a_0$ cart', color=T, fontsize=7.8)
    force(a, (4.40, 1.40), (3.10, 1.40), R, 1.6)
    txt(a, 3.15, 1.58, r'$ma_0$ pseudo', color=R, fontsize=7.4)
    txt(a, .35, 4.20, 'the same work, counted in two frames', color=T, fontsize=7.6)

    b = panel(fig, [.56, .20, .40, .62])
    axes2(b, '', r'work on the ball  (J)')
    bars(b, ['ground', 'cart'], [0, -3.6], colors=[T, R])
    b.set_ylim(-4.4, 1.4)
    head(b, 'pseudo force does the missing work')
    return 'In an accelerating frame the pseudo force can do work; the energy book stays balanced only if you include it'


def path_integral(fig):
    a = panel(fig, [.03, .14, .46, .72], xlim=(0, 10), ylim=(0, 4.6))
    a.plot([.60, 9.40], [.70, .70], color=HG, lw=1.2)
    a.plot([.60, 9.40], [3.90, 3.90], color=HG, lw=1.2)
    a.plot([.70, 2.60], [.70, 3.90], color=T, lw=1.8)
    xs = np.linspace(.70, 2.60, 120)
    a.plot(xs, .70 + 3.20 * ((xs - .70) / 1.90) ** 1.9, color=GOLD, lw=1.8)
    a.plot([5.20, 7.10], [.70, 3.90], color=I, lw=1.2, ls=(0, (3, 2)))
    for (x, y) in [(1.0, .9), (1.35, 1.1), (2.2, 2.4), (2.4, 3.2)]:
        arrow(a, (x, y), (x + .42, y - .12), T, 1.1, ms=6)
    txt(a, .40, 4.22, 'same endpoints, different path integrals', color=T, fontsize=7.4)

    b = panel(fig, [.57, .20, .39, .62])
    axes2(b, r'loop radius  (m)', r'closed-loop work  (J)')
    r = np.linspace(1, 4, 200)
    b.plot(r, 2 * np.pi * r ** 2, color=R, lw=2.2, label='vortex field')
    b.plot(r, 0 * r, color=T, lw=2.2, label='gravity')
    b.legend(frameon=False, fontsize=7.0, loc='upper left')
    b.set_xlim(1, 4); b.set_ylim(-10, 100)
    head(b, 'one closed loop is the whole test')
    return 'If the work around every closed loop vanishes, a potential exists; if not, no bookkeeping can hide it'


def drag_power(fig):
    b, m, P = 0.32, 85.0, 250.0
    a = panel(fig, [.06, .22, .42, .60])
    axes2(a, r'speed  (m/s)', r'power needed  (W)')
    v = np.linspace(0, 20, 300)
    a.plot(v, b * v ** 3, color=R, lw=2.2)
    for vv, lab in ((9.2, r'9.2 m/s'), (11.6, r'11.6 m/s')):
        a.plot([vv], [b * vv ** 3], 'o', ms=5.5, color=T, zorder=5)
        a.annotate(lab, (vv, b * vv ** 3), xytext=(-30, 16), textcoords='offset points',
                   fontsize=7.2, color=T,
                   arrowprops=dict(arrowstyle='-', color=T, lw=.8, shrinkA=1, shrinkB=3))
    a.set_xlim(0, 20); a.set_ylim(0, 2700)
    head(a, r'$P=bv^3$ with $b=0.32$')

    b2 = panel(fig, [.57, .22, .40, .60])
    axes2(b2, r'time  (s)', r'speed  (m/s)')
    dt = 2e-3
    n = int(60 / dt)
    vv, vs = 1e-6, []
    for _ in range(n + 1):
        vs.append(vv)
        vv += dt * (P / max(vv, .02) - b * vv ** 2) / m
    t = np.arange(n + 1) * dt
    b2.plot(t, vs, color=T, lw=2.2)
    b2.axhline(9.2, color=HG, lw=1.1, ls=(0, (3, 3)))
    b2.text(26, 9.7, r'terminal 9.2 m/s', fontsize=7.2, color=G)
    b2.set_xlim(0, 60); b2.set_ylim(0, 11)
    head(b2, 'it approaches, never passes')
    return 'Against drag, speed has a ceiling set by power, and the approach to it is exponential'


def energy_limits(fig):
    a = panel(fig, [.06, .22, .42, .60])
    axes2(a, r'$v/c$', r'kinetic energy  $/mc^2$')
    beta = np.linspace(0, .95, 400)
    a.plot(beta, 1 / np.sqrt(1 - beta ** 2) - 1, color=R, lw=2.2, label='relativistic')
    a.plot(beta, .5 * beta ** 2, color=T, lw=2.0, label=r'$\frac{1}{2}mv^2$')
    a.legend(frameon=False, fontsize=7.2, loc='upper left')
    a.set_xlim(0, .95); a.set_ylim(0, 3.4)
    head(a, 'the halves part company')

    b = panel(fig, [.55, .12, .42, .76], xlim=(0, 10), ylim=(0, 4.6))
    b.axis('off')
    b.add_patch(Rectangle((.30, 2.85), 3.10, .85, fc=PALE, ec='#9ccdc4', lw=1.4))
    b.text(1.85, 3.27, 'mechanical', ha='center', va='center', fontsize=8.0, color=T)
    b.add_patch(Rectangle((.30, 1.55), 3.10, .85, fc='white', ec='#cfe1dc', lw=1.4))
    b.text(1.85, 1.97, 'thermal', ha='center', va='center', fontsize=8.0, color=I)
    b.add_patch(Rectangle((.30, .25), 3.10, .85, fc='#fdf6e3', ec='#e0cd93', lw=1.4))
    b.text(1.85, .67, 'rest mass', ha='center', va='center', fontsize=8.0, color=GOLD)
    arrow(b, (3.50, 3.27), (5.40, 3.27), T, 1.5)
    arrow(b, (3.50, 2.00), (5.40, 2.00), G, 1.5)
    b.text(5.55, 3.22, 'work, KE, PE', fontsize=7.4, color=T)
    b.text(5.55, 1.95, 'friction, drag', fontsize=7.4, color=G)
    b.text(5.55, .68, '$mc^2$: not available', fontsize=7.2, color=GOLD)
    b.text(.30, 4.15, 'the ledger has a ceiling', fontsize=7.8, color=T)
    return 'Classical energy bookkeeping is a low-speed approximation; at high speed the rest mass joins the ledger'
