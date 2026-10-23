"""Analytic schematics and quantitative plots for all 18 Units, Dimensions & Errors sheets (36 panels).

Every panel is generated purely from analytic formulas and synthetic statistical distributions in numpy + matplotlib:
no raster images, screenshots, or external network assets are used.
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, FancyArrowPatch

I = '#153149'   # deep ink navy
T = '#087d7d'   # primary teal
R = '#a43232'   # warning crimson
G = '#b57b14'   # warm gold accent
L = '#d6e8e4'   # soft rule/grid teal
P = '#eef7f5'   # pale card fill


def _clean_canvas(ax):
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5.2)
    ax.axis('off')


def _style_plot(ax, xlabel='', ylabel=''):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_linewidth(1.1)
    ax.spines['bottom'].set_linewidth(1.1)
    ax.tick_params(labelsize=8.2, colors=I)
    ax.grid(True, color='#e4eeec', lw=0.7, zorder=0)
    if xlabel:
        ax.set_xlabel(xlabel, fontsize=8.8, labelpad=2)
    if ylabel:
        ax.set_ylabel(ylabel, fontsize=8.8, labelpad=3)


def _arr(ax, p0, p1, color=I, lw=1.6, ms=12, ls='-'):
    ax.add_patch(FancyArrowPatch(
        p0, p1, arrowstyle='->', mutation_scale=ms,
        lw=lw, linestyle=ls, color=color, shrinkA=0, shrinkB=0, zorder=4
    ))


def _txt(ax, x, y, s, color=I, fs=8.3, ha='left', va='center'):
    ax.text(x, y, s, color=color, fontsize=fs, ha=ha, va=va, zorder=5)


def figure(ax, key):
    # =========================================================================
    # JEE-01: SI 2019 seven constants & CGS conversion powers
    # =========================================================================
    if key == 'si_constants_wheel':
        _clean_canvas(ax)
        cx, cy = 4.9, 2.6
        ax.add_patch(Circle((cx, cy), 0.85, fc=P, ec=T, lw=1.8))
        _txt(ax, cx, cy, '2019 SI\n7 exact\nconstants', I, fs=7.8, ha='center')
        nodes = [
            ('s  <- Cs-133', 0), ('m  <- c', 51.4), ('kg <- h', 102.8),
            ('A  <- e', 154.3), ('K  <- k_B', 205.7), ('mol <- N_A', 257.1), ('cd <- K_cd', 308.6),
        ]
        for lab, deg in nodes:
            ang = np.deg2rad(deg)
            rx = cx + 2.85 * np.cos(ang)
            ry = cy + 1.88 * np.sin(ang)
            ax.plot([cx + 0.9 * np.cos(ang), rx * 0.72 + cx * 0.28],
                    [cy + 0.65 * np.sin(ang), ry * 0.72 + cy * 0.28], color=L, lw=1.3)
            ax.add_patch(Rectangle((rx - 0.95, ry - 0.35), 1.9, 0.7, fc='white', ec=T, lw=1.2))
            _txt(ax, rx, ry, lab, I, fs=6.7, ha='center')
        return 'All seven SI base units fixed since 2019 by exact physical constants'

    if key == 'cgs_scaling_bars':
        _style_plot(ax, '', 'log10(SI / CGS)')
        xs = np.array([0, 1, 2, 3, 4])
        vals = [5, 7, 1, 1, 4]
        cols = [T, R, G, T, I]
        ax.bar(xs, vals, width=0.5, color=cols, zorder=3)
        ax.set_xlim(-0.6, 4.6)
        ax.set_ylim(0, 8.2)
        ax.set_xticks(xs)
        ax.set_xticklabels(['N/dyne', 'J/erg', 'Pa/Ba', 'Pa s/P', 'T/G'], fontsize=7.8)
        for x0, v0 in zip(xs, vals):
            _txt(ax, x0, v0 + 0.42, f'10^{v0}', I, fs=8.0, ha='center')
        return 'Memorisable powers of ten when converting SI quantities into CGS units'

    # =========================================================================
    # JEE-02: Mechanics & thermal dimensional structure
    # =========================================================================
    if key == 'mech_dim_grid':
        _style_plot(ax, '', 'power in [M L T]')
        x = np.arange(5)
        w = 0.24
        m_e = [1, 1, 1, -1, 1]
        l_e = [1, 2, -1, 3, -1]
        t_e = [-2, -2, -2, -2, -1]
        ax.bar(x - w, m_e, width=w, color=T, label='M power')
        ax.bar(x, l_e, width=w, color=G, label='L power')
        ax.bar(x + w, t_e, width=w, color=R, label='T power')
        ax.axhline(0, color=I, lw=0.8)
        ax.set_xlim(-0.6, 4.6)
        ax.set_ylim(-2.8, 3.8)
        ax.set_xticks(x)
        ax.set_xticklabels(['Force F', 'Energy E', 'Press. p', 'Grav. G', 'Visc. eta'], fontsize=7.6)
        ax.legend(loc='upper right', frameon=True, fontsize=7.3)
        return 'Exponent signatures [M^a L^b T^c] for five foundational mechanics quantities'

    if key == 'twin_pairs_chart':
        _clean_canvas(ax)
        rows = [
            (4.15, '[M L^2 T^-2]', 'Work / Energy  ==  Torque (scalar vs vector)'),
            (3.15, '[M L^-1 T^-2]', 'Pressure == Stress == Y, B, G == Energy dens.'),
            (2.15, '[M L^2 T^-1]', 'Angular momentum L == Planck h == Action S'),
            (1.15, '[T^-1]', 'Frequency f == Angular vel. w == dv / dy'),
        ]
        for yy, dim, desc in rows:
            ax.add_patch(Rectangle((0.35, yy - 0.36), 2.55, 0.72, fc=P, ec=T, lw=1.2))
            _txt(ax, 1.62, yy, dim, T, fs=6.9, ha='center')
            _txt(ax, 2.95, yy, desc, I, fs=7.8)
        return 'High-frequency exam twins: identical dimensions never imply identical physics'

    # =========================================================================
    # JEE-03: Electromagnetism dimensional shortcuts
    # =========================================================================
    if key == 'rc_lc_shortcuts':
        _clean_canvas(ax)
        cards = [
            (0.4, 3.1, 4.3, 1.5, 'Time [T] combinations:\n  R C ,   L / R ,   sqrt(L C)', P, T),
            (5.1, 3.1, 4.5, 1.5, 'Speed [L T^-1] combinations:\n  E / B ,   1 / sqrt(mu0 eps0)', P, T),
            (0.4, 0.85, 4.3, 1.5, 'Energy [M L^2 T^-2] blocks:\n  q V ,  C V^2 ,  L I^2 ,  Phi_B I', '#fdf4df', G),
            (5.0, 0.85, 4.65, 1.5, 'Impedance & Stress:\n sqrt(mu0/eps0)=[R], B^2/mu0=[p]', '#fbeaea', R),
        ]
        for x0, y0, w, h, s, fc, ec in cards:
            ax.add_patch(Rectangle((x0, y0), w, h, fc=fc, ec=ec, lw=1.4))
            _txt(ax, x0 + 0.16, y0 + h / 2, s, I, fs=5.8)
        return 'Shortcut composite clusters: cancel [A] immediately without expanding eps0 or mu0'

    if key == 'em_exponent_bars':
        _style_plot(ax, '', 'power [M L T A]')
        x = np.arange(4)
        w = 0.19
        vals = {
            'M': ([1, -1, 1, -1], T),
            'L': ([2, -2, 2, -3], G),
            'T': ([-3, 4, -2, 4], R),
            'A': ([-2, 2, -2, 2], I),
        }
        for idx, (lb, (arr_v, col)) in enumerate(vals.items()):
            ax.bar(x + (idx - 1.5) * w, arr_v, width=w, color=col, label=lb)
        ax.axhline(0, color=I, lw=0.8)
        ax.set_xlim(-0.6, 3.6)
        ax.set_ylim(-3.8, 5.2)
        ax.set_xticks(x)
        ax.set_xticklabels(['Resist. R', 'Cap. C', 'Induct. L', 'Perm. eps0'], fontsize=7.6)
        ax.legend(loc='upper left', ncol=4, frameon=True, fontsize=7.1)
        return 'Exact [M, L, T, A] exponent bars for R, C, L and vacuum permittivity eps0'

    # =========================================================================
    # JEE-04: Principle of homogeneity & transcendental arguments
    # =========================================================================
    if key == 'vanderwaals_balance':
        _clean_canvas(ax)
        ax.add_patch(Rectangle((0.6, 2.95), 8.8, 1.35, fc='#fff6cf', ec=G, lw=1.5))
        _txt(ax, 5.0, 3.62, '( P  +  a / V^2 )   ( V  -  b )   =   n R T', I, fs=10.2, ha='center')
        _arr(ax, (2.25, 2.85), (2.25, 1.85), T, lw=1.6)
        _arr(ax, (5.25, 2.85), (5.25, 1.85), R, lw=1.6)
        _txt(ax, 2.25, 1.32, '[a / V^2] = [P]\n=> [a] = [M L^5 T^-2]', T, fs=8.1, ha='center')
        _txt(ax, 5.25, 1.32, '[b] = [V]\n=> [b] = [L^3]', R, fs=8.1, ha='center')
        _txt(ax, 8.15, 1.32, '[a b / R T]\n= [V] = [L^3]', I, fs=8.1, ha='center')
        return 'Van der Waals homogeneity check: additive partners share identical dimensions'

    if key == 'transcendental_gate':
        _clean_canvas(ax)
        ax.add_patch(Rectangle((0.5, 2.85), 9.0, 1.5, fc=P, ec=T, lw=1.5))
        _txt(ax, 5.0, 3.6, 'exp(u), ln(u), sin(u), cos(u)  =>  [u] = [1]',
             I, fs=7.2, ha='center')
        _txt(ax, 0.7, 1.85, 'VALID: ln(P/P0) = ln P - ln P0  (dimensionless ratio!)', T, fs=7.9)
        _txt(ax, 0.7, 0.95, 'INVALID: y = A sin(w t - x)   because [w t] = [1] while [x] = [L] !', R, fs=8.0)
        return 'Power series u + u^2/2! + ... crashes unless argument u is pure dimensionless [1]'

    # =========================================================================
    # JEE-05: Scaling derivations & Planck/custom base systems
    # =========================================================================
    if key == 'exponent_matrix':
        _clean_canvas(ax)
        ax.add_patch(Rectangle((0.5, 2.8), 9.0, 1.55, fc=P, ec=I, lw=1.4))
        _txt(ax, 5.0, 3.58, '[L] = [c]^x[G]^y[h]^z = [LT^-1]^x[M^-1L^3T^-2]^y[ML^2T^-1]^z',
             I, fs=5.2, ha='center')
        _txt(ax, 1.2, 1.85, 'M:  -y + z = 0  =>  z = y', T, fs=8.2)
        _txt(ax, 1.2, 1.05, 'T:  -x - 2y - z = 0  =>  x = -3y', T, fs=8.2)
        _txt(ax, 5.5, 1.45, 'L:  x + 3y + 2z = 2y = 1\n=>  l_P = sqrt( G h / c^3 ) ~ 1.6e-35 m', R, fs=8.2)
        return 'Changing base units to (c, G, h): three linear equations determine x, y, z uniquely'

    if key == 'sedov_curve':
        _style_plot(ax, 'scaled time  t / t0', 'blast radius  R / R0')
        t = np.linspace(0.02, 3.0, 260)
        ax.plot(t, t ** 0.4, color=T, lw=2.3, label='E0:  R ~ (E t^2 / rho)^(1/5)')
        ax.plot(t, (2.0 * (t ** 2)) ** 0.2, color=R, lw=2.0, ls='--', label='doubled energy 2 E0 (+14.9% only!)')
        ax.set_xlim(0, 3.0)
        ax.set_ylim(0, 2.05)
        ax.legend(loc='lower right', frameon=True, fontsize=7.4)
        return 'Sedov-Taylor shock wave: doubling explosion energy raises radius R by only 2^(1/5)'

    # =========================================================================
    # JEE-06: Significant figures & rounding mechanics
    # =========================================================================
    if key == 'sigfig_anatomy':
        _clean_canvas(ax)
        _txt(ax, 5.0, 4.15, '0 . 0  0   5   6   0   x   10^3', I, fs=12.5, ha='center')
        _txt(ax, 2.55, 2.95, 'leading zeros:\nNOT significant', R, fs=8.1, ha='center')
        _txt(ax, 5.05, 2.95, '5, 6, trailing 0 after dot:\nALL 3 SIGNIFICANT', T, fs=8.1, ha='center')
        _txt(ax, 7.65, 2.95, '10^k multiplier:\n0 impact on count', G, fs=8.1, ha='center')
        _txt(ax, 5.0, 1.05, 'Whole number 1200 m -> ambiguous! Write 1.2 x 10^3 (2 sf) or 1.200 x 10^3 (4 sf)',
             I, fs=7.9, ha='center')
        return 'Anatomy of significant digits: leading zeros locate the decimal; trailing decimal zeros count'

    if key == 'add_vs_mult':
        _clean_canvas(ax)
        ax.add_patch(Rectangle((0.4, 0.8), 4.35, 3.6, fc=P, ec=T, lw=1.4))
        ax.add_patch(Rectangle((5.15, 0.8), 4.45, 3.6, fc='#fdf4df', ec=G, lw=1.4))
        _txt(ax, 2.57, 3.85, 'ADD / SUBTRACT:\nfewest DECIMAL PLACES', T, fs=7.6, ha='center')
        _txt(ax, 2.57, 2.05, '12.5  (1 dec. place)\n+ 0.345  (3 dec.)\n= 12.845 -> 12.8 !', I, fs=7.1, ha='center')
        _txt(ax, 7.37, 3.85, 'MULTIPLY / DIVIDE:\nfewest TOTAL SIG FIGS', R, fs=7.6, ha='center')
        _txt(ax, 7.37, 2.05, '2.5  (2 sig figs)\nx 4.00 / 1.50 (3 sf)\n= 6.667 -> 6.7 !', I, fs=7.1, ha='center')
        return 'Two distinct rounding laws: decimal-column alignment for +/- vs total digits for x / div'

    # =========================================================================
    # JEE-07: Error types, precision vs accuracy & 1/sqrt(n)
    # =========================================================================
    if key == 'target_triad':
        _clean_canvas(ax)
        np.random.seed(7)
        cases = [
            (1.9, 'systematic bias:\nprecise, inaccurate', 0.55, 0.48, 0.11, R),
            (5.0, 'random scatter:\naccurate, noisy', 0.02, -0.02, 0.42, G),
            (8.1, 'calibrated + n >> 1:\naccurate & precise', 0.0, 0.0, 0.10, T),
        ]
        for cx, lab, dx, dy, sp, col in cases:
            for rad in (1.15, 0.72, 0.30):
                ax.add_patch(Circle((cx, 3.0), rad, fill=False, ec='#bed8d3', lw=1.0))
            pts_x = cx + dx + sp * np.array([-0.8, 0.7, -0.3, 0.5, 0.1, -0.5])
            pts_y = 3.0 + dy + sp * np.array([0.5, -0.6, -0.7, 0.8, -0.1, 0.2])
            ax.plot(pts_x, pts_y, 'o', color=col, ms=4.8)
            _txt(ax, cx, 0.88, lab, col, fs=7.9, ha='center')
        return 'Accuracy means unbiased mean; precision means tight cluster (small random scatter)'

    if key == 'sem_sqrt_n':
        _style_plot(ax, 'sample count  n', 'sigma_mean / sigma')
        n = np.arange(1, 51)
        ax.plot(n, 1.0 / np.sqrt(n), color=T, lw=2.3)
        ax.plot([1, 4, 16, 25], [1.0, 0.5, 0.25, 0.2], 'o', color=R, ms=5)
        ax.set_xlim(0, 50)
        ax.set_ylim(0, 1.12)
        _txt(ax, 12, 0.72, 'halving random error needs 4x trials;\n10x gain needs 100x trials!', I, fs=8.0)
        return 'Standard error of the mean falls as 1/sqrt(n) — never removing systematic offset'

    # =========================================================================
    # JEE-08: Catastrophic cancellation & parallel-resistor correlated differential
    # =========================================================================
    if key == 'cancellation_blowup':
        _style_plot(ax, 'ratio  B / A   (with 1% error on each)', 'rel. error in (A - B)  (%)')
        b = np.linspace(0.0, 0.96, 260)
        rel_pct = 100.0 * (0.01 + 0.01 * b) / (1.0 - b)
        ax.semilogy(b, rel_pct, color=R, lw=2.3)
        ax.set_xlim(0, 0.98)
        ax.set_ylim(1, 100)
        _txt(ax, 0.12, 32, 'as B -> A, (dA + dB)/|A - B| explodes!', R, fs=8.1)
        return 'Catastrophic cancellation: subtracting nearly equal numbers destroys relative precision'

    if key == 'parallel_resistor_trap':
        _style_plot(ax, 'ratio  R2 / R1   (1% error each)', 'dR_eq / R_eq  (%)')
        r = np.linspace(0.2, 5.0, 240)
        true_err = 1.0  # for equal relative errors e1 = e2 = 1%, (R/(R1))*1% + (R/R2)*1% == 1% ALWAYS!
        wrong_err = np.full_like(r, 3.0)  # naive d(R1 R2/(R1+R2)) = dR1/R1 + dR2/R2 + (dR1+dR2)/(R1+R2) = 3%!
        ax.plot(r, np.full_like(r, true_err), color=T, lw=2.3, label='exact: dR/R = (R/R1)e1 + (R/R2)e2 = 1%')
        ax.plot(r, wrong_err, color=R, lw=2.0, ls='--', label='wrong numerator+denominator rule = 3%!')
        ax.set_xlim(0.2, 5.0)
        ax.set_ylim(0, 3.8)
        ax.legend(loc='center right', frameon=True, fontsize=7.2)
        return 'Repeating symbols trap: differentiate 1/R = 1/R1 + 1/R2 directly -> 3x smaller true bound!'

    # =========================================================================
    # JEE-09: Vernier calliper scale reading & zero errors
    # =========================================================================
    if key == 'vernier_scale':
        _clean_canvas(ax)
        # Main scale from 2.0 cm (20 mm) to 3.5 cm (35 mm): reading = 2.37 cm (23.7 mm)
        x0, scale = 1.25, 0.51
        ax.add_patch(Rectangle((0.5, 2.75), 9.0, 1.35, fc='#f6faf9', ec=I, lw=1.4))
        for mm in range(16):
            xx = x0 + mm * scale
            h_tick = 0.55 if mm % 5 == 0 else 0.32
            ax.plot([xx, xx], [2.75, 2.75 + h_tick], color=I, lw=1.2)
        _txt(ax, x0, 3.62, '2.0 cm', I, fs=8.0, ha='center')
        _txt(ax, x0 + 5 * scale, 3.62, '2.5 cm', I, fs=8.0, ha='center')
        _txt(ax, x0 + 10 * scale, 3.62, '3.0 cm', I, fs=8.0, ha='center')
        # Vernier zero sits at 3.7 mm past 2.0 cm => 2.37 cm! 10 VSD = 9 MSD (0.9 mm step)
        ax.add_patch(Rectangle((x0 + 3.4 * scale, 1.35), 9.6 * scale, 1.4, fc='#e8f4f2', ec=T, lw=1.4))
        for k in range(11):
            xv = x0 + (3.7 + 0.9 * k) * scale
            col = R if k == 7 else T
            lw0 = 2.2 if k == 7 else 1.1
            ax.plot([xv, xv], [2.75, 2.30], color=col, lw=lw0)
        xc = x0 + (3.7 + 0.9 * 7) * scale
        _txt(ax, xc, 0.82, '7th mark aligns -> 2.30 + 7(0.01) = 2.37 cm', R, fs=8.2, ha='center')
        return 'Drawn to exact scale: MSR = 2.3 cm + 7 x 0.01 cm = 2.37 cm (before zero offset)'

    if key == 'zero_error_pair':
        _clean_canvas(ax)
        ax.add_patch(Rectangle((0.4, 0.8), 4.35, 3.6, fc=P, ec=T, lw=1.4))
        ax.add_patch(Rectangle((5.15, 0.8), 4.45, 3.6, fc='#fbeaea', ec=R, lw=1.4))
        _txt(ax, 2.57, 3.75, 'POSITIVE zero error (+e0)\nvernier 0 RIGHT of main 0', T, fs=7.1, ha='center')
        _txt(ax, 2.57, 2.0, 'instrument OVER-READS\n=> SUBTRACT |e0|:\nx_true = x_raw - (+|e0|)', I, fs=7.1, ha='center')
        _txt(ax, 7.37, 3.75, 'NEGATIVE zero error (-|e0|)\nvernier 0 LEFT of main 0', R, fs=7.1, ha='center')
        _txt(ax, 7.37, 2.0, 'instrument UNDER-READS\n=> ADD |e0|:\nx_true = x_raw - (-|e0|)', I, fs=7.1, ha='center')
        return 'Closed-jaw check: algebraic rule x_true = x_raw - e0 works identically for BOTH signs'

    # =========================================================================
    # JEE-10: Screw gauge sleeve + Searle wire Young modulus budget
    # =========================================================================
    if key == 'micrometer_sleeve':
        _clean_canvas(ax)
        ax.add_patch(Rectangle((0.9, 1.5), 4.2, 2.2, fc='#f6faf9', ec=I, lw=1.5))
        ax.plot([1.3, 5.1], [2.6, 2.6], color=I, lw=1.6)
        for m in range(7):
            xx = 1.5 + m * 0.55
            ax.plot([xx, xx], [2.6, 3.05], color=I, lw=1.2)
            if m < 6:
                ax.plot([xx + 0.275, xx + 0.275], [2.6, 2.25], color=T, lw=1.0)
        _txt(ax, 1.5, 3.35, '0', I, fs=7.8, ha='center')
        _txt(ax, 3.15, 3.35, '3 mm', I, fs=7.8, ha='center')
        # Thimble beveled edge right after 3.0 mm mark, reading 22 on circular scale
        ax.add_patch(Rectangle((4.95, 0.95), 2.55, 3.3, fc='#e4f1ef', ec=T, lw=1.6))
        for dy, lb in [(-0.8, '20'), (0.0, '22 <- ref'), (0.8, '25')]:
            ax.plot([4.95, 5.4], [2.6 + dy, 2.6 + dy], color=R if dy == 0 else I, lw=1.5)
            _txt(ax, 5.38, 2.6 + dy, lb, R if dy == 0 else I, fs=5.9)
        _txt(ax, 5.0, 0.42, 'Raw = 3.00 + 22(0.01) = 3.22 mm;  if e0 = +0.04 mm -> true = 3.18 mm', I, fs=7.9, ha='center')
        return 'Screw gauge (pitch 0.5 mm, 50 div -> LC = 0.01 mm): corrected E10 reading = 3.18 mm'

    if key == 'wire_error_pie':
        _style_plot(ax, '', 'share of  dY / Y  (%)')
        xs = np.array([0, 1, 2, 3])
        vals = [0.2, 0.1, 2.0, 0.8]  # typical Searle apparatus: M(0.2%), L(0.1%), 2 dd/d (2.0%), dl/l (0.8%)
        cols = [T, T, R, G]
        ax.bar(xs, vals, width=0.5, color=cols, zorder=3)
        ax.set_xlim(-0.6, 3.6)
        ax.set_ylim(0, 2.45)
        ax.set_xticks(xs)
        ax.set_xticklabels(['dM / M', 'dL / L', '2 dd / d', 'd(dl) / dl'], fontsize=7.8)
        _txt(ax, 2.0, 2.16, 'diameter dominates!', R, fs=8.0, ha='center')
        return 'Searle wire Y = 4MgL / (pi d^2 dl): thin diameter d enters squared so 2 dd/d dominates'

    # =========================================================================
    # JEE-11: Pendulum linearisation & oleic monolayer
    # =========================================================================
    if key == 'pendulum_linearise':
        _style_plot(ax, 'pendulum length  L  (m)', 'T^2  (s^2)')
        L_pts = np.array([0.25, 0.50, 0.75, 1.00, 1.25])
        T2 = (4 * np.pi ** 2 / 9.81) * L_pts
        err = np.array([0.16, 0.18, 0.20, 0.22, 0.24])
        ax.errorbar(L_pts, T2, yerr=err, fmt='o', color=R, ecolor=R, capsize=3, ms=5, label='measured T^2 +- d(T^2)')
        ll = np.linspace(0, 1.38, 120)
        ax.plot(ll, 4.024 * ll, color=T, lw=2.1, label='best line: slope = 4 pi^2 / g')
        ax.set_xlim(0, 1.4)
        ax.set_ylim(0, 5.9)
        ax.legend(loc='upper left', frameon=True, fontsize=7.4)
        return 'Linearising T = 2 pi sqrt(L/g) as T^2 vs L converts curve-fitting into one slope'

    if key == 'oleic_monolayer':
        _clean_canvas(ax)
        ax.add_patch(Circle((1.65, 2.8), 0.42, fc='#fbe4b4', ec=G, lw=1.6))
        _txt(ax, 1.65, 1.85, 'drop volume V\n= 10^-3 cm^3', I, fs=7.5, ha='center')
        _arr(ax, (2.35, 2.8), (4.25, 2.8), T, lw=2.0)
        _txt(ax, 3.30, 3.45, 'spreads thin', T, fs=7.2, ha='center')
        ax.add_patch(Rectangle((4.5, 2.45), 4.7, 0.65, fc='#fbe4b4', ec=G, lw=1.5))
        ax.add_patch(Rectangle((4.5, 1.35), 4.7, 1.1, fc='#e1f1f6', ec=T, lw=1.1))
        _txt(ax, 6.85, 3.65, 'monolayer area A = pi R^2 = 7.85e3 cm^2', I, fs=8.0, ha='center')
        _txt(ax, 6.85, 0.82, 'd = V / A = 1.27 nm  (~ 1 molecular chain length)', R, fs=8.0, ha='center')
        return 'Oleic-acid monolayer experiment: macroscopic volume & diameter reveal nanometre size'

    # =========================================================================
    # JEE-12: Error workflow & multi-oscillation timing gain 1/N vs 1/sqrt(N)
    # =========================================================================
    if key == 'error_triage':
        _clean_canvas(ax)
        boxes = [
            (0.4, 3.25, 2.85, 1.3, 'Sum / Diff  Z = A +- B\ndZ = dA + dB (abs!)', P, T),
            (3.52, 3.25, 2.95, 1.3, 'Power  A^p B^q / C^r\ndZ/Z = sum |p_i| dX/X', P, T),
            (6.72, 3.25, 2.95, 1.3, 'Coupled 1/R=1/R1+1/R2\ndR/R^2 = sum dRi/Ri^2', '#fbeaea', R),
            (0.4, 0.9, 4.4, 1.3, 'Instrument reading:\nTrue = MSR + k*LC - e0', '#fdf4df', G),
            (5.15, 0.9, 4.4, 1.3, 'Sample of n trials:\nMean +- s / sqrt(n)', '#fdf4df', G),
        ]
        for x0, y0, w, h, s, fc, ec in boxes:
            ax.add_patch(Rectangle((x0, y0), w, h, fc=fc, ec=ec, lw=1.4))
            _txt(ax, x0 + w / 2, y0 + h / 2, s, I, fs=5.6, ha='center')
        return 'Five core JEE error rules side by side — pick structure BEFORE differentiating'

    if key == 'precision_vs_effort':
        _style_plot(ax, 'number of swings  N', 'rel. timing error')
        N = np.arange(1, 51)
        ax.semilogy(N, 1.0 / np.sqrt(N), color=G, lw=2.1, ls='--', label='N separate 1-swing runs  ~ 1/sqrt(N)')
        ax.semilogy(N, 1.0 / N, color=T, lw=2.3, label='1 continuous N-swing run  ~ 1/N !')
        ax.set_xlim(1, 50)
        ax.set_ylim(0.015, 1.2)
        ax.legend(loc='upper right', frameon=True, fontsize=7.3)
        return 'Crucial lab insight: timing N consecutive swings divides reaction error by FULL N!'

    # =========================================================================
    # Olympiad-01: Buckingham Pi nullspace & capillary-gravity waves
    # =========================================================================
    if key == 'dim_matrix_rank':
        _clean_canvas(ax)
        ax.add_patch(Rectangle((0.45, 2.65), 9.1, 1.85, fc=P, ec=T, lw=1.4))
        _txt(ax, 5.0, 3.58,
             'n variables, rank(D) = r independent powers\n'
             '=> p = n - r groups: F(Pi_1,...,Pi_p) = 0',
             I, fs=5.4, ha='center')
        _txt(ax, 0.65, 1.55, 'WATCH: r = rank(D), NOT blind symbol count (e.g. M T^-2 locked)!', R, fs=7.7)
        _txt(ax, 0.65, 0.72, 'Bohr (E, m_e, e, eps0, hbar): n=5, r=4 => p=1 => E ~ m_e e^4/(eps0^2 hbar^2)', T, fs=7.5)
        return 'Buckingham Pi theorem via rank of the exponent matrix D (nullspace dimension n - r)'

    if key == 'capillary_gravity_v':
        _style_plot(ax, 'wavelength  lambda  (cm)', 'speed  v  (cm/s)')
        lam = np.linspace(0.25, 8.0, 300)
        g0, rho0, gam0 = 980.0, 1.0, 72.8
        k = 2 * np.pi / lam
        v = np.sqrt(g0 / k + (gam0 / rho0) * k)
        ax.plot(lam, v, color=T, lw=2.3, label='total  sqrt(g/k + gamma k/rho)')
        ax.plot(lam, np.sqrt(g0 / k), color=G, lw=1.5, ls='--', label='gravity  sqrt(g/k)')
        ax.plot(lam, np.sqrt((gam0 / rho0) * k), color=R, lw=1.5, ls=':', label='capillary  sqrt(gamma k/rho)')
        ax.set_xlim(0.25, 8.0)
        ax.set_ylim(15, 62)
        _txt(ax, 2.0, 20.0, 'min 23.1 cm/s at 1.73 cm (water)', I, fs=7.7)
        ax.legend(loc='upper right', frameon=True, fontsize=7.1)
        return 'Two dimensionless groups (n=5, r=3 -> p=2): crossover at capillary length 2 pi sqrt(gamma/rho g)'

    # =========================================================================
    # Olympiad-02: Reynolds drag curve & Froude ship scaling
    # =========================================================================
    if key == 'drag_crisis_re':
        _style_plot(ax, 'log10(Reynolds number Re)', 'log10(drag coeff. C_D)')
        lre = np.linspace(-1, 5.5, 260)
        re_v = 10 ** lre
        cd = 24.0 / re_v + 0.47 * (1.0 - np.exp(-re_v / 60.0))
        ax.plot(lre, np.log10(cd), color=T, lw=2.3)
        ax.set_xlim(-1, 5.5)
        ax.set_ylim(-0.8, 2.6)
        _txt(ax, -0.7, 1.9, 'Stokes: C_D = 24/Re\nF ~ eta r v', R, fs=7.9)
        _txt(ax, 2.7, 0.2, 'inertial plateau C_D ~ 0.47\nF ~ rho r^2 v^2', T, fs=7.9)
        return 'Sphere drag across six decades of Re = rho v d / eta bridges Stokes to quadratic drag'

    if key == 'model_similarity':
        _style_plot(ax, 'scale factor  L_model / L_ship', 'speed  v_m / v_p')
        s = np.linspace(0.01, 1.0, 220)
        ax.plot(s, np.sqrt(s), color=T, lw=2.3, label='Froude match  v_m/v_p = sqrt(s)')
        ax.plot(s, 1.0 / np.clip(s, 0.25, 1.0), color=R, lw=1.9, ls='--', label='same fluid Re match  ~ 1/s')
        ax.set_xlim(0, 1.0)
        ax.set_ylim(0, 4.2)
        ax.legend(loc='upper right', frameon=True, fontsize=7.3)
        return 'Why ship tanks cannot match Froude AND Reynolds simultaneously in water'

    # =========================================================================
    # Olympiad-03: Ordinary least squares & x-spread leverage
    # =========================================================================
    if key == 'ols_residuals':
        _style_plot(ax, 'input  x', 'response  y')
        xs = np.array([1.0, 2.0, 3.0, 4.0])
        ys = np.array([2.1, 3.9, 6.2, 7.8])
        ax.errorbar(xs, ys, yerr=0.2, fmt='o', color=R, capsize=3, ms=5, label='P30 data (sigma_y = 0.2)')
        xx = np.linspace(0.5, 4.5, 120)
        ax.plot(xx, 0.15 + 1.94 * xx, color=T, lw=2.2, label='OLS: y = 0.15 + 1.94 x')
        ax.plot(2.5, 5.0, 's', color=G, ms=6, label='centroid (x_bar, y_bar) = (2.5, 5.0)')
        ax.set_xlim(0.5, 4.5)
        ax.set_ylim(1.0, 9.2)
        ax.legend(loc='upper left', frameon=True, fontsize=7.1)
        return 'Paper P30 fit: OLS line passes strictly through centroid (2.5, 5.0) with b = 1.94 +- 0.09'

    if key == 'leverage_spread':
        _style_plot(ax, 'x-range ratio  Delta_X / X0', 'sigma_b / sigma_b0')
        dx = np.linspace(0.4, 3.0, 220)
        ax.plot(dx, 1.0 / dx, color=T, lw=2.3)
        ax.set_xlim(0.4, 3.0)
        ax.set_ylim(0, 2.65)
        _txt(ax, 1.05, 1.85, 'sigma_b = sigma_y / sqrt(S_xx) ~ 1 / Delta_X\nspread points WIDE along x!', I, fs=8.0)
        return 'Design lever for straight-line slopes: doubling x-span halves slope uncertainty sigma_b'

    # =========================================================================
    # Olympiad-04: Chi-square regimes & inverse-variance weighting
    # =========================================================================
    if key == 'chi2_regimes':
        _clean_canvas(ax)
        cols_box = [
            (0.35, 'chi^2 / nu  <<  1', 'sigma_i TOO BIG\n(overestimated)', G),
            (3.55, 'chi^2 / nu  ~  1', 'CONSISTENT FIT\nnu +- sqrt(2 nu)', T),
            (6.75, 'chi^2 / nu  >>  1', 'WRONG MODEL or\nsigma_i too small!', R),
        ]
        for x0, top, body, col in cols_box:
            ax.add_patch(Rectangle((x0, 1.0), 2.8, 3.35, fc='white', ec=col, lw=1.6))
            ax.add_patch(Rectangle((x0, 3.45), 2.8, 0.9, fc=P, ec=col, lw=1.2))
            _txt(ax, x0 + 1.4, 3.9, top, col, fs=6.5, ha='center')
            _txt(ax, x0 + 1.4, 2.2, body, I, fs=5.7, ha='center')
        return 'Diagnostic meaning of reduced chi-square chi^2_nu = chi^2 / (n - p)'

    if key == 'weighted_mean_demo':
        _style_plot(ax, 'measurement value', '')
        vals = [9.72, 9.83, 9.806]
        errs = [0.12, 0.04, 0.015]
        ys = [3, 2, 1]
        for v, e, y0, lb in zip(vals, errs, ys, ['Run A (+-0.12)', 'Run B (+-0.04)', 'Run C (+-0.015)']):
            ax.errorbar(v, y0, xerr=e, fmt='o', color=T, capsize=4, ms=5)
            _txt(ax, 9.56, y0, lb, I, fs=7.8)
        w = 1.0 / np.array(errs) ** 2
        wm = np.sum(w * vals) / np.sum(w)
        we = 1.0 / np.sqrt(np.sum(w))
        ax.errorbar(wm, 0.25, xerr=we, fmt='s', color=R, capsize=4, ms=6)
        _txt(ax, 9.56, 0.25, 'Weighted mean', R, fs=7.9)
        ax.axvline(wm, color=R, lw=1.0, ls=':')
        ax.set_xlim(9.54, 9.92)
        ax.set_ylim(-0.3, 3.6)
        ax.set_yticks([])
        return 'Inverse-variance weighting w_i = 1/sigma_i^2 pulls combined estimate to sharpest run'

    # =========================================================================
    # Olympiad-05: Poisson counting & optimal signal/background time split
    # =========================================================================
    if key == 'poisson_vs_gauss':
        _style_plot(ax, 'count  k', 'probability  P(k)')
        k1 = np.arange(0, 12)
        
        p3 = np.array([3.0 ** k * np.exp(-3.0) / float(np.prod(np.arange(1, k + 1))) for k in k1])
        k2 = np.arange(5, 30)
        p16 = np.array([16.0 ** k * np.exp(-16.0) / float(np.prod(np.arange(1, k + 1))) for k in k2])
        ax.bar(k1, p3, width=0.55, color=G, alpha=0.75, label='Poisson lambda = 3 (skew)')
        ax.plot(k2, p16, 'o-', color=T, ms=3.5, lw=1.8, label='lambda = 16 -> Gauss N(16, 4^2)')
        ax.set_xlim(-0.8, 29)
        ax.set_ylim(0, 0.26)
        ax.legend(loc='upper right', frameon=True, fontsize=7.3)
        return 'Poisson counts converge to Gaussian mean N and standard deviation sqrt(N) for N >> 10'

    if key == 'optimal_split':
        _style_plot(ax, 'on-source time fraction  f = t_on / T', 'rel. error in net rate')
        f = np.linspace(0.12, 0.92, 240)
        # R_tot = 250, R_b = 50 => optimal f* = sqrt(250)/(sqrt(250)+sqrt(50)) = sqrt(5)/(sqrt(5)+1) = 0.691
        sig = np.sqrt(250.0 / f + 50.0 / (1.0 - f)) / 200.0
        ax.plot(f, sig, color=T, lw=2.3)
        f_opt = np.sqrt(5.0) / (np.sqrt(5.0) + 1.0)
        ax.axvline(f_opt, color=R, lw=1.2, ls='--')
        ax.set_xlim(0.1, 0.95)
        ax.set_ylim(0.095, 0.22)
        _txt(ax, 0.28, 0.19, 'min at t_on/t_off = sqrt(R_tot / R_b) = 2.24', R, fs=7.9)
        return 'Optimal beam-time allocation between gross rate R_tot = 250/s and background R_b = 50/s'

    # =========================================================================
    # Olympiad-06: 0.1% g-budget & finite-amplitude pendulum shift
    # =========================================================================
    if key == 'pendulum_budget_bars':
        _style_plot(ax, '', 'share of  dg / g  (%)')
        xs = np.array([0, 1, 2, 3])
        vals = [0.050, 0.014, 0.015, 0.079]
        cols = [T, G, T, R]
        ax.bar(xs, vals, width=0.5, color=cols, zorder=3)
        ax.axhline(0.100, color=R, lw=1.3, ls='--', label='target ceiling  0.100%')
        ax.set_xlim(-0.6, 3.6)
        ax.set_ylim(0, 0.125)
        ax.set_xticks(xs)
        ax.set_xticklabels(['dL / L', '2 dT / T', 'amp 2*th^2/16', 'Total worst'], fontsize=7.5)
        ax.legend(loc='upper left', frameon=True, fontsize=7.4)
        return 'OL5 experimental budget (L = 2.000 m, N = 50 swings, theta_0 = 2 deg): 0.079% < 0.1%!'

    if key == 'amplitude_shift':
        _style_plot(ax, 'launch amplitude  theta_0  (deg)', 'dT / T0  (%)')
        deg = np.linspace(0, 25, 220)
        rad = np.deg2rad(deg)
        shift_pct = 100.0 * (rad ** 2) / 16.0
        ax.plot(deg, shift_pct, color=T, lw=2.3)
        ax.axhline(0.02, color=R, lw=1.2, ls='--', label='0.02% ceiling -> theta_0 <= 3.3 deg')
        ax.set_xlim(0, 25)
        ax.set_ylim(0, 1.32)
        ax.legend(loc='upper left', frameon=True, fontsize=7.4)
        return 'Anharmonic pendulum period drift +theta_0^2 / 16 (theta_0 MUST be in radians!)'

    raise KeyError(f'Unknown diagram key: {key!r}')
