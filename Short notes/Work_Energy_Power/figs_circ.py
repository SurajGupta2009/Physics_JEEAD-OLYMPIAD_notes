"""Part III figures: the complete circular-motion strand."""
import numpy as np
from matplotlib.patches import Rectangle, Circle, Arc, Polygon
from figlib import (I, T, R, G, GOLD, HG, BLUE, GREEN, PALE, YEL, WATER,
                    txt, head, foot, arrow, panel, axes2, dimx, dimy, incline,
                    block, force, dashed, ball, spring, bars, shade_between,
                    arcarrow, rot_block)


def omega_alpha(fig):
    a = panel(fig, [.03, .12, .46, .76], xlim=(0, 10), ylim=(0, 4.6), equal=True)
    C = (4.60, 2.30)
    a.add_patch(Circle(C, 1.85, fc='none', ec=HG, lw=1.4))
    th = np.radians(52)
    ball(a, C[0] + 1.85 * np.cos(th), C[1] + 1.85 * np.sin(th), .18, '#f6dedb', R)
    a.plot([C[0], C[0] + 1.85 * np.cos(th)], [C[1], C[1] + 1.85 * np.sin(th)],
           color=I, lw=1.3)
    arcarrow(a, C, .95, 10, 52, color=T)
    txt(a, C[0] + .78, C[1] + .55, r'$\theta$', color=T, fontsize=9.0)
    a.plot([C[0], C[0] + 2.25], [C[1], C[1]], color=HG, lw=1.0, ls=(0, (3, 2)))
    arrow(a, (C[0] + 1.85 * np.cos(th), C[1] + 1.85 * np.sin(th)),
          (C[0] + 1.85 * np.cos(th) - .95 * np.sin(th), C[1] + 1.85 * np.sin(th) + .95 * np.cos(th)), T, 1.8)
    txt(a, C[0] + 1.55, C[1] + 2.10, r'$v=\omega R$', color=T, fontsize=8.4)
    a.text(.30, 4.30, 'one angle describes the whole rotation', fontsize=7.6, color=T)

    b = panel(fig, [.56, .18, .40, .68])
    axes2(b, r'time  (s)', r'$\omega$  and  $\alpha$')
    t = np.linspace(0, 5, 300)
    b.plot(t, 1.2 + .9 * t, color=T, lw=2.1, label=r'$\omega$')
    b.plot(t, 0 * t + .9, color=R, lw=2.1, label=r'$\alpha$')
    b.legend(frameon=False, fontsize=7.2, loc='upper left')
    b.set_xlim(0, 5); b.set_ylim(0, 6.6)
    head(b, 'alpha is the slope of omega')
    return 'Angular position, angular velocity and angular acceleration are the rotation of one radius'


def alpha_kinematics(fig):
    a = panel(fig, [.06, .22, .42, .60])
    axes2(a, r'time  (s)', r'angle  $\theta$  (rad)')
    t = np.linspace(0, 5, 300)
    a.plot(t, 1.5 * t + .5 * 1.2 * t ** 2, color=T, lw=2.2)
    a.plot(t, 1.5 * t, color=HG, lw=1.1, ls=(0, (3, 3)))
    a.text(1.2, 12.5, r'$\theta=\omega_0t+\frac{1}{2}\alpha t^2$', fontsize=8.0, color=T)
    a.set_xlim(0, 5); a.set_ylim(0, 22)
    head(a, 'angle grows quadratically')

    b = panel(fig, [.57, .22, .40, .60])
    axes2(b, r'angle turned  (rad)', r'$\omega^2$  (rad$^2$/s$^2$)')
    th = np.linspace(0, 12, 300)
    b.plot(th, 2.25 + 2 * 1.2 * th, color=R, lw=2.2)
    b.text(4.6, 12.0, r'$\omega^2=\omega_0^2+2\alpha\theta$', fontsize=8.0, color=R)
    b.set_xlim(0, 12); b.set_ylim(0, 32)
    head(b, 'the third equation, without t')
    return 'The three constant-alpha equations are the linear ones with x, v, a replaced by theta, omega, alpha'


def omega_vector(fig):
    a = panel(fig, [.03, .12, .46, .76], xlim=(0, 10), ylim=(0, 4.6))
    a.add_patch(Circle((4.70, 1.90), 1.55, fc='none', ec=HG, lw=1.4))
    ball(a, 6.25, 1.90, .16, '#f6dedb', R)
    arrow(a, (4.70, 1.90), (4.70, 4.15), BLUE, 2.2)
    txt(a, 4.95, 3.85, r'$\vec\omega$', color=BLUE, fontsize=9.4)
    arrow(a, (6.25, 1.90), (6.25, 3.05), T, 1.8)
    txt(a, 6.45, 2.95, r'$\vec v$', color=T, fontsize=8.8)
    a.plot([4.70, 6.25], [1.90, 1.90], color=I, lw=1.4)
    txt(a, 5.30, 1.62, r'$\vec r$', color=I, fontsize=8.8)
    a.plot([4.70, 6.25], [1.90, 1.90], color=HG, lw=1.0, ls=(0, (2, 2)))
    txt(a, .30, 4.32, 'the right hand gives the direction along the axis', color=T, fontsize=7.4)

    b = panel(fig, [.57, .18, .39, .68])
    axes2(b, r'time  (s)', r'angle swept  (rad)')
    t = np.linspace(0, 6, 300)
    for w, c, lab in ((1.0, T, r'$\omega=1$'), (2.0, GOLD, r'$2$'), (3.0, R, r'$3$')):
        b.plot(t, w * t, color=c, lw=2.0, label=lab)
    b.legend(frameon=False, fontsize=7.0, loc='upper left')
    b.set_xlim(0, 6); b.set_ylim(0, 19)
    head(b, 'same axis, different rates')
    return 'Angular velocity is a vector along the rotation axis, and v = omega cross r gives the tangential speed'


def centripetal_two_ways(fig):
    a = panel(fig, [.03, .12, .46, .76], xlim=(0, 10), ylim=(0, 4.6), equal=True)
    C = (4.60, 2.20)
    a.add_patch(Circle(C, 1.70, fc='none', ec=HG, lw=1.4))
    for th in (38, 58):
        x, y = C[0] + 1.70 * np.cos(np.radians(th)), C[1] + 1.70 * np.sin(np.radians(th))
        ball(a, x, y, .13, '#f6dedb', R)
    x1, y1 = C[0] + 1.70 * np.cos(np.radians(38)), C[1] + 1.70 * np.sin(np.radians(38))
    x2, y2 = C[0] + 1.70 * np.cos(np.radians(58)), C[1] + 1.70 * np.sin(np.radians(58))
    arrow(a, (x1, y1), (x1 - .85 * np.sin(np.radians(38)), y1 + .85 * np.cos(np.radians(38))), T, 1.6)
    arrow(a, (x2, y2), (x2 - .85 * np.sin(np.radians(58)), y2 + .85 * np.cos(np.radians(58))), T, 1.6)
    arrow(a, ((x1 + x2) / 2 - .10, (y1 + y2) / 2 - .55), ((x1 + x2) / 2 + .05, (y1 + y2) / 2 - 1.35), R, 1.6)
    txt(a, (x1 + x2) / 2 - .85, (y1 + y2) / 2 - 1.30, r'$\Delta v$', color=R, fontsize=8.6)
    a.plot([C[0], x1], [C[1], y1], color=I, lw=1.0, ls=(0, (3, 2)))
    a.plot([C[0], x2], [C[1], y2], color=I, lw=1.0, ls=(0, (3, 2)))
    txt(a, .30, 4.34, r'$\Delta v$ points at the centre for any small turn', color=T, fontsize=7.4)

    b = panel(fig, [.57, .18, .39, .68])
    axes2(b, r'speed  (m/s)', r'$a_c$  (m/s$^2$)')
    v = np.linspace(0, 20, 300)
    for R_, c, lab in ((2, T, '2 m'), (5, GOLD, '5 m'), (10, R, '10 m')):
        b.plot(v, v ** 2 / R_, color=c, lw=2.0, label=lab)
    b.legend(frameon=False, fontsize=7.0, loc='upper left', title='radius', title_fontsize=7)
    b.set_xlim(0, 20); b.set_ylim(0, 45)
    head(b, r'$a_c=v^2/R$: speed is squared, radius divides')
    return 'Centripetal acceleration exists because the direction of velocity turns, even at constant speed'


def at_an(fig):
    a = panel(fig, [.03, .12, .46, .76], xlim=(0, 10), ylim=(0, 4.6), equal=True)
    C = (4.70, 2.25)
    a.add_patch(Circle(C, 1.75, fc='none', ec=HG, lw=1.4))
    ang = 38
    x, y = C[0] + 1.75 * np.cos(np.radians(ang)), C[1] + 1.75 * np.sin(np.radians(ang))
    ball(a, x, y, .17, '#f6dedb', R)
    arrow(a, (x, y), (x - .95, y - .74), BLUE, 1.9)
    txt(a, x - .55, y - 1.05, r'$a_c$', color=BLUE, fontsize=8.6)
    arrow(a, (x, y), (x - .30, y + 1.05), GOLD, 1.9)
    txt(a, x - .05, y + 1.12, r'$a_t$', color=GOLD, fontsize=8.6)
    arrow(a, (x, y), (x - 1.18, y + .45), T, 1.9)
    txt(a, x - 1.55, y + .52, r'$a$', color=T, fontsize=8.8)
    a.plot([C[0], x], [C[1], y], color=I, lw=1.0, ls=(0, (3, 2)))
    txt(a, .30, 4.34, r'$a=\sqrt{a_t^2+a_c^2}$', color=T, fontsize=9.4)

    b = panel(fig, [.57, .18, .39, .68])
    axes2(b, r'time  (s)', r'tilt of $a$ from the radius  (deg)')
    t = np.linspace(0, 4, 300)
    b.plot(t, np.degrees(np.arctan(1.2 / (0.5 + .9 * t) ** 2)), color=T, lw=2.2)
    b.set_xlim(0, 4); b.set_ylim(0, 80)
    head(b, 'as it speeds up, a turns radial')
    return 'When the speed changes, acceleration has two perpendicular parts: one bends, one speeds up'


def alpha_integral(fig):
    a = panel(fig, [.06, .22, .42, .60])
    axes2(a, r'time  (s)', r'$\alpha$  (rad/s$^2$)')
    t = np.linspace(0, 4, 400)
    a.plot(t, 3 * np.exp(-t) * np.cos(1.4 * t), color=R, lw=2.1)
    a.fill_between(t, 0, 3 * np.exp(-t) * np.cos(1.4 * t), color=R, alpha=.12, lw=0)
    a.axhline(0, color=I, lw=.8)
    a.set_xlim(0, 4); a.set_ylim(-1.4, 3.2)
    head(a, 'alpha given as a curve')

    b = panel(fig, [.57, .22, .40, .60])
    axes2(b, r'time  (s)', r'$\omega$  (rad/s)')
    b.plot(t, 1.2 + np.cumsum(3 * np.exp(-t) * np.cos(1.4 * t)) * (t[1] - t[0]), color=T, lw=2.2)
    b.set_xlim(0, 4); b.set_ylim(0, 3.2)
    head(b, 'omega is the area under it')
    return 'When alpha is not constant, integrate it: omega is the area, theta is the area under omega'


def relative_angular(fig):
    a = panel(fig, [.03, .12, .46, .76], xlim=(0, 10), ylim=(0, 4.6), equal=True)
    C = (4.70, 2.25)
    a.add_patch(Circle(C, 1.80, fc='none', ec=HG, lw=1.4))
    for ang, c, lab in ((35, T, 'A'), (120, R, 'B')):
        x, y = C[0] + 1.80 * np.cos(np.radians(ang)), C[1] + 1.80 * np.sin(np.radians(ang))
        ball(a, x, y, .17, '#f6dedb', c)
        txt(a, x + .30, y + .20, lab, color=c, fontsize=8.6)
    arcarrow(a, C, .85, 35, 120, color=G)
    txt(a, C[0] - .10, C[1] + .95, r'$\Delta\theta$', color=G, fontsize=8.4)
    txt(a, .30, 4.34, 'two particles, two angular rates', color=T, fontsize=7.4)

    b = panel(fig, [.57, .18, .39, .68])
    axes2(b, r'time  (s)', r'separation  (rad)')
    t = np.linspace(0, 6, 600)
    sep = np.mod((1.5 - .6) * t, 2 * np.pi)
    b.plot(t, sep, color=T, lw=1.9)
    b.set_xlim(0, 6); b.set_ylim(0, 6.5)
    head(b, r'rate $=|\omega_1-\omega_2|$')
    return 'Separations change at the difference of the angular velocities, and reset once per lap'


def work_radial(fig):
    a = panel(fig, [.03, .12, .46, .76], xlim=(0, 10), ylim=(0, 4.6), equal=True)
    C = (4.90, 2.25)
    a.add_patch(Circle(C, 1.80, fc='none', ec=HG, lw=1.4))
    ang = 42
    x, y = C[0] + 1.80 * np.cos(np.radians(ang)), C[1] + 1.80 * np.sin(np.radians(ang))
    ball(a, x, y, .17, '#f6dedb', R)
    arrow(a, (x, y), (x - 1.10, y - .99), BLUE, 1.9)
    txt(a, x - 1.50, y - 1.10, r'$F_c$', color=BLUE, fontsize=8.6)
    arrow(a, (x, y), (x - .18, y + .92), T, 1.8)
    txt(a, x - .02, y + .99, r'$d\vec s$', color=T, fontsize=8.2)
    a.add_patch(Arc((x, y), .95, .95, theta1=180 + ang, theta2=270 + ang, color=GOLD, lw=1.4))
    txt(a, x - 1.05, y + .42, r'$90^{\circ}$', color=GOLD, fontsize=7.6)
    txt(a, .30, .26, 'the radial force is always perpendicular to the step', color=T, fontsize=7.4)

    b = panel(fig, [.57, .18, .39, .68])
    axes2(b, r'angle round the circle  (deg)', r'work done  (J)')
    th = np.linspace(0, 360, 400)
    b.plot(th, 0 * th, color=BLUE, lw=2.1, label=r'$F_c$: zero')
    b.plot(th, 3.0 * np.radians(th) / 1.0, color=GOLD, lw=2.0, label=r'$F_t$: linear')
    b.legend(frameon=False, fontsize=7.0, loc='upper left')
    b.set_xlim(0, 360); b.set_ylim(0, 20)
    head(b, 'only the tangential part earns work')
    return 'The centripetal force does no work: it is perpendicular to every step, so it never changes the speed'


def vertical_energy(fig):
    a = panel(fig, [.03, .12, .44, .76], xlim=(0, 10), ylim=(0, 4.6), equal=True)
    C = (4.60, 2.60)
    a.add_patch(Circle(C, 1.75, fc='none', ec=HG, lw=1.3, ls=(0, (4, 3))))
    pts = [(C[0], C[1] - 1.75, 'bottom'), (C[0] + 1.75, C[1], 'side'),
           (C[0], C[1] + 1.75, 'top')]
    for x, y, lab in pts:
        ball(a, x, y, .17, '#f6dedb', R)
    txt(a, C[0] - .95, C[1] - 1.60, 'bottom', color=G, fontsize=7.0)
    txt(a, C[0] + 1.95, C[1] - .16, 'side', color=G, fontsize=7.0)
    txt(a, C[0] - 1.05, C[1] + 1.86, 'top', color=G, fontsize=7.0)
    txt(a, .30, -.02, r'$v^2=v_0^2-2gR(1-\cos\phi)$', color=T, fontsize=8.6)

    b = panel(fig, [.55, .20, .41, .62])
    axes2(b, r'angle from the bottom  (deg)', r'speed$^2$  $/gR$')
    ph = np.linspace(0, 360, 400)
    b.plot(ph, 5.0 - 2 * (1 - np.cos(np.radians(ph))), color=T, lw=2.2)
    b.axhline(0, color=I, lw=.8)
    b.axhline(1, color=HG, lw=1.0, ls=(0, (3, 3)))
    b.text(292, 1.28, r'limit $gR$', fontsize=6.8, color=G)
    b.set_xlim(0, 360); b.set_ylim(0, 5.6)
    head(b, r'a full loop at $v_0^2=5gR$')
    return 'In a vertical circle the speed at any angle comes from energy alone; the force only fixes the tension'


def string_vs_rod(fig):
    a = panel(fig, [.05, .22, .41, .60])
    axes2(a, r'angle from the bottom  (deg)', r'tension / mg')
    ph = np.linspace(0, 180, 300)
    a.plot(ph, (5 - 2 * (1 - np.cos(np.radians(ph)))) + np.cos(np.radians(ph)),
           color=T, lw=2.2)
    a.axhline(0, color=I, lw=.8)
    a.plot([180], [0], 'o', ms=5.5, color=R, zorder=5)
    a.text(96, 4.62, r'$T/mg=3+3\cos\phi$', fontsize=7.0, color=G)
    a.set_xlim(0, 180); a.set_ylim(0, 6.4)
    head(a, 'string: tension must stay positive')

    b = panel(fig, [.59, .22, .38, .60])
    axes2(b, r'angle from the bottom  (deg)', r'normal / mg')
    ph2 = np.linspace(0, 180, 300)
    b.plot(ph2, (4 - 2 * (1 - np.cos(np.radians(ph2)))) + np.cos(np.radians(ph2)),
           color=GOLD, lw=2.2)
    b.axhline(0, color=I, lw=.8)
    b.text(62, -2.75, r'rod: $N/mg=2+3\cos\phi$', fontsize=7.0, color=G)
    b.set_xlim(0, 180); b.set_ylim(-3.2, 5.4)
    head(b, 'rod: the sign may change')
    return 'A string can only pull, so it sets a minimum launch speed; a rod can push, so it halves it'


def conical_energy(fig):
    a = panel(fig, [.03, .12, .46, .76], xlim=(0, 10), ylim=(0, 4.6))
    a.plot([.60, 9.40], [4.15, 4.15], color=I, lw=2.2)
    a.plot([5.00, 5.00], [4.15, 2.85], color=GOLD, lw=1.6)
    a.add_patch(Circle((5.00, 2.55), .18, fc='#f6dedb', ec=R, lw=1.3, zorder=5))
    dashed(a, (5.00, 4.15), (5.00, 1.10))
    a.plot([5.00, 6.35], [2.55, 2.55], color=HG, lw=1.1, ls=(0, (2, 2)))
    txt(a, 5.55, 2.72, r'$r=L\sin\theta$', color=G, fontsize=7.6)
    force(a, (5.00, 2.55), (5.00, 1.35), R, 1.6, r'$mg$', fs=8.4, off=(.10, -.30))
    arrow(a, (5.00, 2.55), (5.58, 3.72), BLUE, 1.6)
    txt(a, 5.65, 3.66, r'$T$', color=BLUE, fontsize=8.4)
    arcarrow(a, (5.00, 2.55), .72, -60, 40, color=T)
    txt(a, 5.62, 2.10, r'$v$', color=T, fontsize=8.2)
    txt(a, .30, 4.36, 'the same bob, a different speed, a different cone', color=T, fontsize=7.4)

    b = panel(fig, [.57, .18, .39, .68])
    axes2(b, r'$\omega/\omega_c$', r'$\cos\theta$')
    w = np.linspace(1.02, 3, 300)
    b.plot(w, 1 / w ** 2, color=T, lw=2.2)
    b.axhline(1, color=HG, lw=1.0, ls=(0, (3, 3)))
    b.text(1.8, 1.03, 'flat, slow', fontsize=7.0, color=G)
    b.set_xlim(0, 3); b.set_ylim(0, 1.12)
    head(b, r'$\cos\theta=\omega_c^2/\omega^2$')
    return 'A conical pendulum is a force triangle and an energy statement at once; the period ignores the mass'


def bank_limits(fig):
    a = panel(fig, [.03, .14, .44, .72], xlim=(0, 10), ylim=(0, 4.6))
    a.add_patch(Polygon([(.40, .80), (9.60, .80), (5.20, 3.55)], closed=True,
                        fc='#f2f6f5', ec=I, lw=1.6))
    rot_block(a, 5.70, 2.45, 1.35, .62, -16, '#fdf0bd', GOLD)
    force(a, (5.70, 2.45), (5.35, 3.75), BLUE, 1.6, r'$N$', fs=8.4, off=(-.45, .10))
    force(a, (5.70, 2.45), (5.70, 1.15), R, 1.6, r'$mg$', fs=8.4, off=(.12, -.32))
    arrow(a, (6.20, 2.10), (7.05, 2.30), GOLD, 1.4)
    txt(a, 7.10, 2.28, r'$f$', color=GOLD, fontsize=8.2)
    a.text(.35, 3.95, 'the bank supplies most of the turn', fontsize=7.6, color=T)
    a.text(.35, .18, 'friction only tops it up or trims it', fontsize=7.2, color=G)

    b = panel(fig, [.56, .18, .40, .64])
    axes2(b, r'friction coefficient $\mu$', r'safe speed$^2$  $/Rg$')
    mu = np.linspace(0, 1, 300)
    th = np.radians(25)
    hi = (np.sin(th) + mu * np.cos(th)) / (np.cos(th) - mu * np.sin(th))
    lo = (np.sin(th) - mu * np.cos(th)) / (np.cos(th) + mu * np.sin(th))
    b.plot(mu, hi, color=T, lw=2.1, label=r'$v_{\max}^2$')
    b.plot(mu, np.clip(lo, 0, None), color=R, lw=2.1, label=r'$v_{\min}^2$')
    b.axhline(np.tan(th), color=HG, lw=1.0, ls=(0, (3, 3)))
    b.text(.62, np.tan(th) + .08, 'design', fontsize=6.8, color=G)
    b.legend(frameon=False, fontsize=7.0, loc='upper left')
    b.set_xlim(0, 1); b.set_ylim(0, 3.2)
    head(b, r'$\theta=25^{\circ}$')
    return 'A banked road has a design speed and a band around it; friction widens the band but cannot create it'


def rotor_wall(fig):
    a = panel(fig, [.03, .12, .46, .76], xlim=(0, 10), ylim=(0, 4.6), equal=True)
    a.add_patch(Rectangle((.60, .40), 8.60, 4.00, fc='#f7fbfa', ec=I, lw=1.6))
    a.add_patch(Rectangle((.60, .40), 8.60, .22, fc='#e8eef0', ec=I, lw=1.2))
    a.plot([7.90, 7.90], [.62, 3.95], color=I, lw=2.4)
    block(a, 7.55, 2.30, .55, 1.05, '#f6dedb', R)
    force(a, (7.28, 2.30), (6.30, 2.30), BLUE, 1.7)
    txt(a, 6.35, 2.05, r'$N$', color=BLUE, fontsize=8.8)
    force(a, (7.55, 2.55), (7.55, 3.60), T, 1.6)
    txt(a, 7.70, 3.45, r'$f$', color=T, fontsize=8.4)
    force(a, (7.55, 1.95), (7.55, .95), R, 1.6)
    txt(a, 7.75, 1.15, r'$mg$', color=R, fontsize=8.4)
    a.text(.80, 4.16, 'a wall that spins fast enough replaces the floor', fontsize=7.4, color=T)

    b = panel(fig, [.57, .18, .39, .68])
    axes2(b, r'friction coefficient $\mu$', r'$\omega_{\min}^2 R/g$')
    mu = np.linspace(.05, 1, 300)
    b.plot(mu, 1 / mu, color=T, lw=2.2)
    b.set_xlim(0, 1); b.set_ylim(0, 8)
    head(b, r'$\omega_{\min}=\sqrt{g/(\mu R)}$')
    return 'On the inside of a spinning wall the normal force is the centripetal supply and friction must carry the weight'


def curvature_fit(fig):
    a = panel(fig, [.03, .12, .46, .76], xlim=(0, 10), ylim=(0, 4.6), equal=True)
    xs = np.linspace(.60, 9.20, 300)
    ys = 2.20 + .55 * (xs - 4.80) - .045 * (xs - 4.80) ** 2
    a.plot(xs, ys, color=T, lw=2.4)
    a.add_patch(Circle((4.80, 1.05), 1.15, fc='none', ec=GOLD, lw=1.4, ls=(0, (4, 2))))
    a.plot([4.80], [2.20], 'o', ms=5, color=R, zorder=5)
    a.plot([4.80, 4.80], [2.20, 1.05], color=GOLD, lw=1.0, ls=(0, (2, 2)))
    txt(a, 4.95, 1.55, r'$\rho$', color=GOLD, fontsize=8.6)
    arrow(a, (4.80, 2.20), (5.75, 2.90), T, 1.4)
    txt(a, 5.80, 2.86, r'$v$', color=T, fontsize=8.2)
    a.text(.30, 4.34, 'the best-fitting circle at one point', fontsize=7.4, color=T)

    b = panel(fig, [.57, .18, .39, .68])
    axes2(b, r'launch angle  (deg)', r'$\rho$  (m)')
    th = np.linspace(1, 89, 300)
    v0 = 20.0
    b.plot(th, v0 ** 2 / (9.8 * np.cos(np.radians(th))), color=T, lw=2.0, label='at launch')
    b.plot(th, (v0 * np.cos(np.radians(th))) ** 2 / 9.8, color=GOLD, lw=2.0, label='at apex')
    b.set_yscale('log')
    b.set_xlim(1, 89); b.set_ylim(8, 1400)
    b.set_yticks([10, 100, 1000])
    b.set_yticklabels(['10', '100', '1000'])
    b.plot([45], [400 / (9.8 * .7071)], 'o', ms=5, color=R, zorder=5)
    b.annotate(r'$45^{\circ}$: 57.7 m', (45, 57.7), xytext=(-18, 26), textcoords='offset points',
               fontsize=6.8, color=R,
               arrowprops=dict(arrowstyle='-', color=R, lw=.8, shrinkA=1, shrinkB=3))
    b.legend(frameon=False, fontsize=6.8, loc='upper left')
    head(b, r'$20$ m/s projectile')
    return 'Curvature is the reciprocal of the radius of the circle that matches the path locally'


FIGS = {k: v for k, v in list(globals().items())
        if callable(v) and getattr(v, '__module__', '') == __name__}
