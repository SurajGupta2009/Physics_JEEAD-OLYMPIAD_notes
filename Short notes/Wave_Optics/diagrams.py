"""Analytic schematics and quantitative plots for all 24 Wave Optics sheets (48 panels).

Every panel is generated purely from Maxwell/Huygens/Fresnel wave equations in numpy + matplotlib:
no raster images, screenshots, or external network assets are used. Uses the exact 8-colour palette
of ``render_sheets.py`` and ASCII ``PatrickHand`` glyph set so indexed PNG export stays razor-sharp.
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, FancyArrowPatch, Arc, Polygon, FancyBboxPatch

I = '#153149'   # deep ink navy
T = '#087d7d'   # primary teal
R = '#a43232'   # warning crimson
G = '#b57b14'   # warm gold accent
L = '#d6e8e4'   # soft rule/grid teal
P = '#eef7f5'   # pale card fill
Y = '#fff6d6'   # pale highlight yellow

_TRAPZ = getattr(np, 'trapezoid', None) or np.trapz


def _j1(x):
    """Exact Bessel J1(x) via 256-point midpoint Fourier integral (pure NumPy, <1e-14 error)."""
    x_arr = np.asarray(x, dtype=float)
    tau = (np.arange(256) + 0.5) * (np.pi / 256.0)
    return np.mean(np.cos(tau[None, :] - x_arr[..., None] * np.sin(tau)[None, :]), axis=-1)


def _fresnel(v):
    """Exact Fresnel integrals (S(v), C(v)) via dense numerical quadrature (pure NumPy)."""
    v_arr = np.asarray(v, dtype=float)
    t = np.linspace(0.0, 1.0, 1601)
    u = v_arr[..., None] * t[None, :]
    du = v_arr / 1600.0
    S = _TRAPZ(np.sin(0.5 * np.pi * u**2), axis=-1) * du
    C = _TRAPZ(np.cos(0.5 * np.pi * u**2), axis=-1) * du
    return S, C


def _clean_canvas(ax):
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5.2)
    ax.axis('off')


def _style_plot(ax, xlabel='', ylabel=''):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_linewidth(1.1)
    ax.spines['left'].set_color(I)
    ax.spines['bottom'].set_linewidth(1.1)
    ax.spines['bottom'].set_color(I)
    ax.tick_params(labelsize=8.0, colors=I)
    ax.grid(True, color='#e4eeec', lw=0.7, zorder=0)
    if xlabel:
        ax.set_xlabel(xlabel, fontsize=8.4, color=I, labelpad=2)
    if ylabel:
        ax.set_ylabel(ylabel, fontsize=8.4, color=I, labelpad=3)


def _arr(ax, p0, p1, color=I, lw=1.55, ms=11, ls='-', style='->'):
    ax.add_patch(FancyArrowPatch(
        p0, p1, arrowstyle=style, mutation_scale=ms,
        lw=lw, linestyle=ls, color=color, shrinkA=0, shrinkB=0, zorder=4
    ))


def _txt(ax, x, y, s, color=I, fs=8.0, ha='left', va='center'):
    ax.text(x, y, s, color=color, fontsize=fs, ha=ha, va=va, zorder=5)


def figure(ax, key):
    # =========================================================================
    # JEE-01: Wavefronts, Huygens Construction & Optical Path
    # =========================================================================
    if key == 'wavefront_types':
        _clean_canvas(ax)
        # 1. Point -> Spherical
        ax.plot(0.65, 2.65, 'o', color=R, ms=5.5, zorder=5)
        _txt(ax, 0.65, 1.35, 'Point S', R, fs=7.8, ha='center')
        for rad in (0.85, 1.5, 2.15):
            ax.add_patch(Arc((0.65, 2.65), 2*rad, 2*rad, angle=0, theta1=-45, theta2=45, color=I, lw=1.4))
        for deg in (-26, 0, 26):
            th = np.deg2rad(deg)
            _arr(ax, (0.65 + 0.3*np.cos(th), 2.65 + 0.3*np.sin(th)),
                 (0.65 + 2.65*np.cos(th), 2.65 + 2.65*np.sin(th)), T, lw=1.2)
        _txt(ax, 1.75, 4.75, 'Spherical (I ~ 1/r^2)', I, fs=7.8, ha='center')

        # 2. Line slit -> Cylindrical
        ax.plot([3.95, 3.95], [1.1, 4.15], color=R, lw=2.6)
        _txt(ax, 3.95, 0.62, 'Line slit', R, fs=7.8, ha='center')
        for xx in (4.65, 5.35, 6.05):
            ax.plot([xx, xx], [1.15, 4.1], color=I, lw=1.35)
            ax.add_patch(Arc((xx - 0.1, 2.62), 0.32, 2.9, angle=0, theta1=-90, theta2=90, color=T, lw=0.8, ls='--'))
        for yy in (1.75, 2.62, 3.5):
            _arr(ax, (4.1, yy), (6.5, yy), T, lw=1.2)
        _txt(ax, 5.2, 4.75, 'Cylindrical (I ~ 1/r)', I, fs=7.8, ha='center')

        # 3. Plane wave
        for xx in (7.35, 8.05, 8.75, 9.45):
            ax.plot([xx, xx], [1.15, 4.1], color=I, lw=1.45)
        for yy in (1.75, 2.62, 3.5):
            _arr(ax, (7.1, yy), (9.85, yy), T, lw=1.2)
        _txt(ax, 8.5, 4.75, 'Plane (I = const)', I, fs=7.8, ha='center')
        _txt(ax, 8.5, 0.62, 'Rays _|_ wavefront', T, fs=7.8, ha='center')
        return 'Spherical, cylindrical and plane wavefronts with orthogonal energy rays'

    if key == 'huygens_refraction':
        _clean_canvas(ax)
        ax.add_patch(Rectangle((0.3, 0.25), 9.4, 2.15, fc=P, ec='none'))
        ax.plot([0.3, 9.7], [2.4, 2.4], color=I, lw=1.5)
        _txt(ax, 0.45, 4.72, 'Medium 1: speed v1 = c / n1', I, fs=7.8)
        _txt(ax, 0.45, 1.88, 'Medium 2: v2 = c/n2 < v1', T, fs=7.7)
        i_rad, r_rad = np.deg2rad(42), np.deg2rad(25)
        A = np.array([3.3, 2.4])
        AC = 3.2
        C = np.array([3.3 + AC, 2.4])
        u_in = np.array([np.sin(i_rad), -np.cos(i_rad)])
        u_rf = np.array([np.sin(r_rad), -np.cos(r_rad)])
        B = C - (AC * np.sin(i_rad)) * u_in
        D = A + (AC * np.sin(r_rad)) * u_rf
        ax.plot([A[0], B[0]], [A[1], B[1]], color=R, lw=1.8)
        _arr(ax, tuple(B), tuple(C), R, lw=1.45)
        _arr(ax, tuple(A - 1.45*u_in), tuple(A), R, lw=1.45)
        ax.add_patch(Arc(tuple(A), 2*AC*np.sin(r_rad), 2*AC*np.sin(r_rad),
                         angle=0, theta1=-95, theta2=-12, color=T, lw=1.2, ls='--'))
        ax.plot([C[0], D[0]], [C[1], D[1]], color=T, lw=1.8)
        _arr(ax, tuple(A), tuple(A + 2.05*u_rf), T, lw=1.45)
        _arr(ax, tuple(C), tuple(C + 1.4*u_rf), T, lw=1.45)
        ax.plot([A[0], A[0]], [0.55, 4.35], color=I, lw=0.8, ls=':')
        _txt(ax, A[0] - 0.45, 2.68, 'A', I, fs=8.1)
        _txt(ax, B[0] + 0.18, B[1] + 0.1, 'B', R, fs=8.1)
        _txt(ax, C[0] + 0.16, 2.68, 'C', I, fs=8.1)
        _txt(ax, D[0] + 0.28, D[1] - 0.35, 'D', T, fs=8.1)
        _txt(ax, 7.35, 4.15, 'BC = v1 dt', R, fs=8.0)
        _txt(ax, 7.35, 3.45, 'AD = v2 dt', T, fs=8.0)
        _txt(ax, 7.45, 1.55, 'sin i / sin r = v1/v2', I, fs=7.9)
        return 'Huygens wavelet envelope proof of Snell refraction n1 sin i = n2 sin r'

    # =========================================================================
    # JEE-02: Superposition, Phasors, Intensity & Coherence
    # =========================================================================
    if key == 'phasor_addition':
        _clean_canvas(ax)
        _arr(ax, (0.7, 0.9), (9.2, 0.9), I, lw=1.0)
        _arr(ax, (1.1, 0.45), (1.1, 4.75), I, lw=1.0)
        O, P1, P2 = (1.1, 0.9), (5.0, 2.0), (7.55, 4.25)
        _arr(ax, O, P1, I, lw=1.85)
        _arr(ax, P1, P2, T, lw=1.85)
        _arr(ax, O, P2, R, lw=2.05)
        ax.plot([P1[0], 7.85], [P1[1], 2.81], color=I, lw=0.95, ls='--')
        _txt(ax, 3.35, 1.02, 'A1 = sqrt(I1)', I, fs=7.9, ha='center')
        _txt(ax, 7.25, 3.32, 'A2 = sqrt(I2)', T, fs=7.9)
        _txt(ax, 3.65, 3.35, 'A_res = sqrt(I)', R, fs=8.2, ha='center')
        _txt(ax, 6.45, 1.95, 'dphi', G, fs=8.1)
        _txt(ax, 5.2, 0.42, 'I = I1 + I2 + 2 sqrt(I1 I2) cos(dphi)', I, fs=8.0, ha='center')
        return 'Rotating phasor triangle adding two co-polarised harmonic waves'

    if key == 'visibility_contrast':
        phi = np.linspace(-2*np.pi, 2*np.pi, 400)
        ax.plot(phi/np.pi, 2.0 + 2.0*np.cos(phi), color=I, lw=1.7, label='I1 = I2 (V = 1.0)')
        ax.plot(phi/np.pi, 2.5 + 1.5*np.cos(phi), color=R, lw=1.5, ls='--', label='I1 = 9 I2 (V = 0.6)')
        ax.axhline(2.0, color=T, lw=1.0, ls=':')
        _txt(ax, -1.0, 4.45, 'Mean <I> = 2 I0', T, fs=7.4, ha='center')
        _style_plot(ax, xlabel='Phase difference dphi / pi', ylabel='Intensity I / I0')
        ax.set_ylim(-0.2, 5.3)
        ax.legend(loc='upper right', fontsize=7.2, frameon=True, facecolor='white', edgecolor=L)
        return 'Fringe contrast drops when unequal beam intensities leave minima non-zero'

    # =========================================================================
    # JEE-03: Young's Double-Slit Experiment (YDSE) Core Laws
    # =========================================================================
    if key == 'ydse_geometry':
        _clean_canvas(ax)
        for y0, y1 in ((0.3, 1.55), (1.95, 3.25), (3.65, 4.9)):
            ax.plot([1.9, 1.9], [y0, y1], color=I, lw=3.0)
        S1, S2, P_pt = (1.9, 3.45), (1.9, 1.75), (8.2, 4.45)
        ax.plot([8.2, 8.2], [0.35, 4.95], color=I, lw=2.2)
        ax.plot([1.9, 8.2], [2.6, 2.6], color=I, lw=0.85, ls=':')
        ax.plot([S1[0], P_pt[0]], [S1[1], P_pt[1]], color=I, lw=1.4)
        ax.plot([S2[0], P_pt[0]], [S2[1], P_pt[1]], color=T, lw=1.4)
        u = np.array([P_pt[0]-S2[0], P_pt[1]-S2[1]], dtype=float)
        u /= np.linalg.norm(u)
        N = np.array(S2) + np.dot(np.array(S1) - np.array(S2), u) * u
        ax.plot([S1[0], N[0]], [S1[1], N[1]], color=R, lw=1.5, ls='--')
        _txt(ax, 1.35, 3.45, 'S1', I, fs=8.2)
        _txt(ax, 1.35, 1.75, 'S2', T, fs=8.2)
        _txt(ax, 1.0, 2.6, 'd', G, fs=8.4)
        _txt(ax, 8.45, 4.42, 'P(y)', R, fs=8.2)
        _txt(ax, 8.45, 2.6, 'O (y=0)', I, fs=8.0)
        _txt(ax, 5.05, 0.55, 'dx = d sin(theta) ~ d y / D  (for D >> d, |y| << D)', R, fs=7.9, ha='center')
        return 'Young double-slit geometry and path difference dx = S2P - S1P'

    if key == 'ydse_intensity':
        y = np.linspace(-2.5, 2.5, 500)
        Irr = 4.0 * np.cos(np.pi * y)**2
        ax.fill_between(y, 0, Irr, color=P)
        ax.plot(y, Irr, color=I, lw=1.65)
        ax.axhline(2.0, color=T, lw=1.0, ls='--')
        _arr(ax, (0.0, 4.3), (1.0, 4.3), R, lw=1.2, style='<->')
        _txt(ax, 0.5, 4.82, 'beta = lam D / d', R, fs=7.5, ha='center')
        _txt(ax, -1.5, 4.55, 'Mean = 2 I0', T, fs=7.4, ha='center')
        _style_plot(ax, xlabel='Screen position y / beta', ylabel='Intensity I / I0')
        ax.set_ylim(0, 5.25)
        return 'Equal-intensity YDSE profile redistributes energy without loss (<I> = 2 I0)'

    # =========================================================================
    # JEE-04: 3D Fringe Surfaces & End-On Circular YDSE
    # =========================================================================
    if key == 'ydse_3d_hyperboloids':
        _clean_canvas(ax)
        cx0, cy0, c = 4.65, 2.55, 1.65
        ax.plot([cx0 - c, cx0 + c], [cy0, cy0], 'o', color=R, ms=5.8, zorder=5)
        _txt(ax, cx0 - c - 0.45, cy0, 'S1', R, fs=8.0, ha='right')
        _txt(ax, cx0 + c + 0.45, cy0, 'S2', R, fs=8.0, ha='left')
        ax.plot([cx0, cx0], [0.35, 4.65], color=I, lw=1.55)
        _txt(ax, cx0 + 0.16, 4.42, 'n=0', I, fs=7.6)
        yv = np.linspace(-2.05, 2.05, 260)
        for idx, a in enumerate((0.48, 0.96, 1.38), 1):
            b = np.sqrt(c**2 - a**2)
            xv = a * np.sqrt(1 + (yv / b)**2)
            col = T if idx % 2 else G
            ax.plot(cx0 + xv, cy0 + yv, color=col, lw=1.25)
            ax.plot(cx0 - xv, cy0 + yv, color=col, lw=1.25)
        ax.plot([0.55, 8.75], [4.65, 4.65], color=I, lw=2.0)
        _txt(ax, 2.05, 4.92, 'Parallel screen: lines', I, fs=7.7, ha='center')
        ax.plot([9.05, 9.05], [0.45, 4.65], color=R, lw=2.1)
        _txt(ax, 8.85, 0.22, 'End-on screen: circles!', R, fs=7.8, ha='right')
        return 'Constant path-difference hyperboloids around S1-S2 sliced two ways'

    if key == 'ydse_circular_end_on':
        _clean_canvas(ax)
        ax.plot([0.4, 5.95], [2.6, 2.6], color=I, lw=0.85, ls=':')
        ax.plot([0.85, 2.15], [2.6, 2.6], 'o', color=R, ms=5.5)
        _txt(ax, 0.85, 1.98, 'S2', R, fs=8.0, ha='center')
        _txt(ax, 2.15, 1.98, 'S1', R, fs=8.0, ha='center')
        _arr(ax, (0.85, 3.12), (2.15, 3.12), I, lw=1.1, style='<->')
        _txt(ax, 1.5, 3.45, 'd', I, fs=8.0, ha='center')
        ax.plot([5.85, 5.85], [0.55, 4.65], color=I, lw=2.2)
        ax.plot([0.85, 5.85], [2.6, 4.25], color=I, lw=1.2)
        ax.plot([2.15, 5.85], [2.6, 4.25], color=T, lw=1.2)
        _txt(ax, 3.35, 0.92, 'dx = d cos(theta)', I, fs=8.0, ha='center')
        _txt(ax, 3.35, 0.35, 'Max order m = d/lam AT O!', R, fs=7.7, ha='center')
        cx, cy = 8.15, 2.75
        for p_idx, col in ((1, I), (2, T), (3, I), (4, T)):
            ax.add_patch(Circle((cx, cy), 0.82*np.sqrt(p_idx), fill=False, lw=1.3, ec=col))
        ax.plot(cx, cy, 'o', color=R, ms=4.5)
        _txt(ax, cx, 0.35, 'Radii r_p ~ sqrt(p)', I, fs=7.8, ha='center')
        return 'End-on screen perpendicular to S1-S2 produces circular fringes'

    # =========================================================================
    # JEE-05: Slabs, Liquids & Slit Widths
    # =========================================================================
    if key == 'ydse_slab_shift':
        _clean_canvas(ax)
        for y0, y1 in ((0.35, 1.55), (1.95, 3.25), (3.65, 4.85)):
            ax.plot([1.65, 1.65], [y0, y1], color=I, lw=2.8)
        ax.add_patch(Rectangle((2.0, 3.05), 0.8, 0.85, fc=P, ec=T, lw=1.5))
        _txt(ax, 2.4, 4.25, 'Slab (mu, t)', T, fs=7.7, ha='center')
        ax.plot([6.95, 6.95], [0.35, 4.85], color=I, lw=2.2)
        ax.plot([1.65, 6.95], [2.6, 2.6], color=I, lw=0.85, ls=':')
        ax.plot([1.65, 6.95], [3.45, 4.05], color=T, lw=1.45)
        ax.plot([1.65, 6.95], [1.75, 4.05], color=I, lw=1.45)
        _arr(ax, (7.28, 2.6), (7.28, 4.05), R, lw=1.5)
        _txt(ax, 7.5, 3.32, 'dy = (mu-1)t D/d', R, fs=7.6)
        _txt(ax, 7.5, 4.35, "New O' (dx=0)", R, fs=7.5)
        _txt(ax, 7.5, 2.38, 'Geom O', I, fs=7.5)
        _txt(ax, 1.15, 3.45, 'S1', T, fs=8.2)
        _txt(ax, 1.15, 1.75, 'S2', I, fs=8.2)
        _txt(ax, 4.3, 0.52, 'Fringe width beta stays UNCHANGED!', I, fs=7.8, ha='center')
        return 'Dielectric plate over S1 shifts the zero-order fringe toward S1'

    if key == 'ydse_liquid_cases':
        _clean_canvas(ax)
        boxes = [
            (0.3, 2.75, 'Full liquid immersion (mu_L)', 'lam -> lam0 / mu_L\nbeta_L = beta_air / mu_L', I, P),
            (5.15, 2.75, 'Slab mu_S inside liquid mu_L', 'dy = (mu_S - mu_L) t D / (mu_L d)\nShift N = (mu_S - mu_L) t / lam0', T, P),
            (0.3, 0.35, 'Unequal widths: I ~ w rule', 'I1 : I2 = w1 : w2\nImax/Imin = (sqrt w1 + sqrt w2)^2 / ...', R, Y),
            (5.15, 0.35, 'Plate swap between S1 & S2', 'Moves from +dy to -dy\nTotal travel = 2 |mu1 - mu2| t D / d', G, Y),
        ]
        for x, y, hd, bd, ec, fc in boxes:
            ax.add_patch(FancyBboxPatch((x, y), 4.55, 1.95, boxstyle='round,pad=0.06', fc=fc, ec=ec, lw=1.3))
            _txt(ax, x + 2.27, y + 1.55, hd, ec, fs=7.7, ha='center')
            _txt(ax, x + 2.27, y + 0.65, bd, I, fs=7.2, ha='center')
        return 'Four high-frequency YDSE medium and slit-width perturbation rules'

    # =========================================================================
    # JEE-06: Oblique Incidence, Dynamic Motion & White Light
    # =========================================================================
    if key == 'ydse_oblique':
        _clean_canvas(ax)
        for y0, y1 in ((0.4, 1.6), (2.0, 3.2), (3.6, 4.8)):
            ax.plot([3.3, 3.3], [y0, y1], color=I, lw=2.8)
        ax.plot([8.2, 8.2], [0.4, 4.85], color=I, lw=2.2)
        ax.plot([0.5, 8.2], [2.6, 2.6], color=I, lw=0.85, ls=':')
        ang = np.deg2rad(18)
        for yh in (1.8, 3.4):
            p0 = np.array([3.3, yh]) - 2.5*np.array([np.cos(ang), np.sin(ang)])
            _arr(ax, tuple(p0), (3.3, yh), R, lw=1.45)
        yc = 2.6 + 4.9*np.tan(ang)
        ax.plot([3.3, 8.2], [3.4, yc], color=I, lw=1.35)
        ax.plot([3.3, 8.2], [1.8, yc], color=T, lw=1.35)
        ax.plot(8.2, yc, 'o', color=R, ms=5.5)
        _txt(ax, 8.42, yc, 'theta0 = +alpha', R, fs=7.8)
        _txt(ax, 1.55, 3.85, 'Incident tilt alpha', R, fs=7.8, ha='center')
        _txt(ax, 5.75, 0.62, 'd sin(theta) - d sin(alpha) = n lam', I, fs=8.0, ha='center')
        return 'Oblique plane incidence shifts central fringe to theta = alpha'

    if key == 'ydse_white_missing':
        y = np.linspace(-2.2, 2.2, 600)
        ax.plot(y, np.cos(np.pi * y * (530.0 / 430.0))**2, color=I, lw=1.25, label='Blue (430 nm)')
        ax.plot(y, np.cos(np.pi * y)**2, color=T, lw=1.35, ls='--', label='Green (530 nm)')
        ax.plot(y, np.cos(np.pi * y * (530.0 / 650.0))**2, color=R, lw=1.45, label='Red (650 nm)')
        ax.axvline(0.0, color=G, lw=1.15, ls=':')
        _txt(ax, 0.1, 1.15, 'Pure white y=0', I, fs=7.4)
        _style_plot(ax, xlabel='Position y / beta_green', ylabel='Rel. intensity')
        ax.set_ylim(0, 1.42)
        ax.legend(loc='upper left', fontsize=7.0, frameon=True, facecolor='white', edgecolor=L)
        return 'Polychromatic YDSE: white central fringe and missing wavelengths at y_P'

    # =========================================================================
    # JEE-07: Parallel Thin Films
    # =========================================================================
    if key == 'thin_film_geometry':
        _clean_canvas(ax)
        ax.add_patch(Rectangle((0.4, 1.45), 9.2, 1.75, fc=P, ec='none'))
        ax.plot([0.4, 9.6], [3.2, 3.2], color=I, lw=1.5)
        ax.plot([0.4, 9.6], [1.45, 1.45], color=I, lw=1.5)
        _txt(ax, 7.9, 3.6, 'Ambient n1', I, fs=7.9)
        _txt(ax, 7.9, 2.32, 'Film (mu, t)', T, fs=8.1)
        _txt(ax, 7.9, 0.9, 'Substrate n3', I, fs=7.9)
        A, B, C = (2.6, 3.2), (4.0, 1.45), (5.4, 3.2)
        _arr(ax, (1.2, 4.75), A, R, lw=1.5)
        _arr(ax, A, (4.0, 4.75), I, lw=1.45)
        ax.plot([A[0], B[0], C[0]], [A[1], B[1], C[1]], color=T, lw=1.6)
        _arr(ax, C, (6.8, 4.75), I, lw=1.45)
        ax.plot([B[0], B[0]], [1.05, 3.45], color=I, lw=0.8, ls=':')
        _txt(ax, 2.15, 3.55, 'A', I, fs=8.1)
        _txt(ax, 4.35, 1.05, 'B', I, fs=8.1)
        _txt(ax, 5.1, 3.55, 'C', I, fs=8.0)
        _txt(ax, 4.25, 4.45, 'Ray 1', I, fs=7.6)
        _txt(ax, 6.9, 4.45, 'Ray 2', I, fs=7.6)
        _txt(ax, 0.55, 0.55, 'Geom OPL = 2 mu t cos r', R, fs=8.0)
        return 'Parallel thin film reflection geometry giving OPL = 2 mu t cos r'

    if key == 'thin_film_cases':
        x = np.linspace(0, 2.15, 400)
        ax.plot(x, np.sin(np.pi * x)**2, color=R, lw=1.65, label='n1 < mu > n3 (soap)')
        ax.plot(x, np.cos(np.pi * x)**2, color=I, lw=1.55, ls='--', label='n1 < mu < n3 (AR coat)')
        ax.plot([0.0], [0.0], 'o', color=R, ms=5.5)
        ax.plot([0.5], [0.0], 'o', color=I, ms=5.5)
        _txt(ax, 0.45, 1.18, 'Soap: 0 at t->0; AR: 0 at lam0/(4 nc)', I, fs=7.0, ha='center')
        _style_plot(ax, xlabel='Round-trip 2 mu t / lam0', ylabel='Norm. R(lam)')
        ax.set_ylim(-0.06, 1.42)
        ax.legend(loc='upper right', fontsize=7.0, frameon=True, facecolor='white', edgecolor=L)
        return 'Opposite vs matching boundary phase jumps swap bright and dark orders'

    # =========================================================================
    # JEE-08: Wedge Films & Newton's Rings
    # =========================================================================
    if key == 'wedge_film':
        _clean_canvas(ax)
        ax.add_patch(Polygon([(0.8, 0.9), (9.1, 0.9), (9.1, 1.45), (0.8, 1.45)], fc=P, ec=I, lw=1.2))
        ax.add_patch(Polygon([(0.8, 1.45), (9.1, 3.05), (8.98, 3.55), (0.68, 1.95)], fc=P, ec=I, lw=1.2))
        ax.add_patch(Rectangle((8.85, 1.45), 0.25, 1.56, fc=R, ec=I, lw=1.0))
        _txt(ax, 9.25, 2.2, 'Wire h', R, fs=7.8)
        for k, xx in enumerate((0.8, 2.35, 3.9, 5.45, 7.0, 8.55)):
            ax.plot([xx, xx], [3.7, 4.35], lw=2.8 if k % 2 == 0 else 1.0, color=I if k % 2 == 0 else G)
        _arr(ax, (2.35, 4.42), (3.9, 4.42), R, lw=1.15, style='<->')
        _txt(ax, 3.12, 4.9, 'beta = lam0 / (2 mu theta)', R, fs=7.5, ha='center')
        _txt(ax, 4.8, 0.35, 'Contact edge x = 0 is DARK; straight equal-thickness Fizeau lines', I, fs=7.7, ha='center')
        return 'Air or liquid wedge film: equal-spacing fringes measure micron thickness h'

    if key == 'newtons_rings':
        _clean_canvas(ax)
        ax.add_patch(Rectangle((0.35, 0.85), 5.2, 0.55, fc=P, ec=I, lw=1.2))
        xs = np.linspace(0.55, 5.35, 200)
        ys = 1.40 + 0.24 * (xs - 2.95)**2
        ax.fill_between(xs, ys, 3.35, facecolor=P, edgecolor=I, lw=1.2)
        ax.plot([2.95, 2.95], [1.4, 4.4], color=I, lw=0.8, ls=':')
        ax.plot([4.5, 4.5], [1.4, 1.4 + 0.24*1.55**2], color=R, lw=1.5)
        _txt(ax, 4.66, 1.68, 't = r^2/(2R)', R, fs=7.6)
        _txt(ax, 2.95, 4.65, 'Radius of curvature R >> r', I, fs=7.8, ha='center')
        _txt(ax, 2.95, 0.35, 'D_n = sqrt(4 n lam0 R / mu0)', T, fs=7.8, ha='center')
        cx, cy = 8.15, 2.75
        ax.add_patch(Circle((cx, cy), 0.14, fc=I, ec=I))
        for n in range(1, 6):
            ax.add_patch(Circle((cx, cy), 0.72*np.sqrt(n), fill=False, lw=1.6 - 0.16*n, ec=I))
        _txt(ax, cx, 0.35, 'Dark centre (r = 0)', R, fs=7.8, ha='center')
        return 'Newton rings: circular equal-thickness fringes crowd outerward as n^(-1/2)'

    # =========================================================================
    # JEE-09: AR Coatings, Biprism, Lloyd Mirror & Billet Split Lens
    # =========================================================================
    if key == 'fresnel_biprism':
        _clean_canvas(ax)
        ax.plot([0.5, 9.1], [2.6, 2.6], color=I, lw=0.8, ls=':')
        ax.plot(1.3, 2.6, 'o', color=R, ms=5.5)
        ax.plot([1.3, 1.3], [3.65, 1.55], 'o', color=I, ms=4.8, mfc='white')
        _txt(ax, 0.85, 2.6, 'S', R, fs=8.2)
        _txt(ax, 0.72, 3.65, 'S1', I, fs=8.0)
        _txt(ax, 0.72, 1.55, 'S2', I, fs=8.0)
        ax.add_patch(Polygon([(4.0, 2.6), (4.4, 4.45), (4.4, 0.75)], fc=P, ec=T, lw=1.5))
        _txt(ax, 4.2, 4.72, 'Biprism (A, mu)', T, fs=7.8, ha='center')
        ax.plot([8.8, 8.8], [0.45, 4.75], color=I, lw=2.2)
        ax.add_patch(Rectangle((8.68, 1.65), 0.24, 1.9, fc=Y, ec=G, lw=1.2))
        ax.plot([1.3, 4.25], [2.6, 3.35], color=R, lw=1.2)
        ax.plot([1.3, 4.25], [2.6, 1.85], color=R, lw=1.2)
        ax.plot([1.3, 8.8], [3.65, 1.65], color=I, lw=1.05, ls='--')
        ax.plot([1.3, 8.8], [1.55, 3.55], color=I, lw=1.05, ls='--')
        _arr(ax, (1.3, 0.55), (4.2, 0.55), I, lw=1.0, style='<->')
        _arr(ax, (4.2, 0.55), (8.8, 0.55), I, lw=1.0, style='<->')
        _txt(ax, 2.75, 0.22, 'a', I, fs=8.0, ha='center')
        _txt(ax, 6.5, 0.22, 'b', I, fs=8.0, ha='center')
        _txt(ax, 9.05, 3.15, 'Overlap', G, fs=7.5)
        return 'Fresnel biprism creates virtual twins d = 2a(mu - 1)A with A in radians'

    if key == 'lloyds_mirror':
        _clean_canvas(ax)
        ax.plot([0.5, 8.4], [2.15, 2.15], color=I, lw=0.8, ls=':')
        ax.plot([3.2, 7.5], [2.15, 2.15], color=T, lw=3.2)
        _txt(ax, 6.2, 1.55, 'Mirror M (pi flip)', T, fs=7.6, ha='center')
        S, Sp, P_pt, Mh = (1.3, 3.25), (1.3, 1.05), (8.4, 4.35), (5.35, 2.15)
        ax.plot(*S, 'o', color=R, ms=5.5)
        ax.plot(*Sp, 'o', color=T, ms=5.2, mfc='white')
        ax.plot([8.4, 8.4], [2.15, 4.85], color=I, lw=2.2)
        ax.plot([S[0], P_pt[0]], [S[1], P_pt[1]], color=R, lw=1.4)
        ax.plot([S[0], Mh[0], P_pt[0]], [S[1], Mh[1], P_pt[1]], color=T, lw=1.4)
        ax.plot([Sp[0], Mh[0]], [Sp[1], Mh[1]], color=T, lw=1.05, ls='--')
        _txt(ax, 0.98, 3.25, 'S (+h)', R, fs=7.8, ha='right')
        _txt(ax, 0.98, 1.05, "S' (-h)", T, fs=7.8, ha='right')
        _txt(ax, 8.6, 2.15, 'DARK (y=0)', R, fs=7.7)
        _txt(ax, 8.6, 4.3, 'P (y > 0)', I, fs=7.8)
        _txt(ax, 4.9, 0.45, 'd = 2h; grazing reflection flips phase by pi so edge is DARK', I, fs=7.7, ha='center')
        return 'Lloyd mirror proves the reflection pi phase jump directly at contact line y = 0'

    # =========================================================================
    # JEE-10: Fraunhofer Single-Slit Diffraction
    # =========================================================================
    if key == 'single_slit_pairing':
        _clean_canvas(ax)
        ax.plot([2.2, 2.2], [0.25, 1.15], color=I, lw=3.4)
        ax.plot([2.2, 2.2], [3.95, 4.95], color=I, lw=3.4)
        ang = np.deg2rad(21)
        u = np.array([np.cos(ang), np.sin(ang)])
        for y0, col in ((3.65, I), (2.25, T), (2.95, I), (1.55, T)):
            p0 = np.array([2.2, y0])
            _arr(ax, tuple(p0), tuple(p0 + 6.3*u), col, lw=1.3)
        pA, pB = np.array([2.2, 3.65]), np.array([2.2, 2.25])
        foot = pB + np.dot(pA - pB, u) * u
        ax.plot([pA[0], foot[0]], [pA[1], foot[1]], color=R, lw=1.5, ls='--')
        _arr(ax, (1.55, 1.15), (1.55, 3.95), I, lw=1.1, style='<->')
        _txt(ax, 1.15, 2.55, 'a', I, fs=8.4)
        _txt(ax, 6.05, 0.55, '(a/2) sin(theta) = lam/2 => a sin(theta) = m lam (DARK!)', R, fs=7.3, ha='center')
        return 'Destructive zone pairing across a single slit of width a (m = +/-1, +/-2, ...)'

    if key == 'single_slit_sinc':
        b = np.linspace(-3.5*np.pi, 3.5*np.pi, 700)
        Irr = np.sinc(b / np.pi)**2
        ax.fill_between(b/np.pi, 0, Irr, color=P)
        ax.plot(b/np.pi, Irr, color=I, lw=1.7)
        _txt(ax, 2.15, 0.82, 'Central width\nWc = 2 lam D / a', R, fs=7.4, ha='center')
        _txt(ax, 1.5, 0.14, '4.72%', T, fs=7.3, ha='center')
        _txt(ax, 2.5, 0.09, '1.65%', G, fs=7.2, ha='center')
        _style_plot(ax, xlabel='beta / pi = (a sin theta) / lam', ylabel='Rel. I / I0')
        ax.set_ylim(0, 1.12)
        return 'Single-slit sinc^2 pattern: central lobe is twice as wide as side lobes'

    # =========================================================================
    # JEE-11: Finite Double-Slit Envelope & Gratings
    # =========================================================================
    if key == 'double_slit_envelope':
        x = np.linspace(-1.35, 1.35, 900)
        env = np.sinc(x)**2
        tot = env * np.cos(4.0 * np.pi * x)**2
        ax.plot(x, env, color=R, lw=1.35, ls='--', label='Sinc^2 envelope')
        ax.fill_between(x, 0, tot, color=P)
        ax.plot(x, tot, color=I, lw=1.3, label='d/a = 4 -> 7 peaks!')
        ax.plot([-1.0, 1.0], [0.0, 0.0], 'o', color=R, ms=5.2)
        _txt(ax, 1.0, 0.22, 'n=+4\nmissing', R, fs=7.1, ha='center')
        _style_plot(ax, xlabel='(a sin theta) / lam', ylabel='Rel. I / 4I0')
        ax.set_ylim(-0.04, 1.38)
        ax.legend(loc='upper left', fontsize=7.0, frameon=True, facecolor='white', edgecolor=L)
        return 'Double slit (d/a = 4): 7 strictly visible bright peaks inside central lobe'

    if key == 'grating_spectra':
        _clean_canvas(ax)
        ax.plot([0.5, 9.7], [1.15, 1.15], color=I, lw=1.5)
        ax.add_patch(Rectangle((0.9, 1.15), 0.28, 2.55, fc=I, ec=I))
        _txt(ax, 1.04, 4.35, 'm=0\nWhite', I, fs=7.4, ha='center')
        ax.add_patch(Rectangle((2.4, 1.15), 1.65, 2.05, fc=P, ec=T, lw=1.3))
        _txt(ax, 3.22, 3.9, 'm=1 isolated\n(400-700 nm)', T, fs=7.3, ha='center')
        ax.add_patch(Rectangle((4.9, 1.15), 3.15, 1.55, fc=P, ec=I, lw=1.3))
        _txt(ax, 5.95, 3.05, 'm=2 (800-1400)', I, fs=7.3, ha='center')
        ax.add_patch(Rectangle((7.15, 1.6), 2.4, 1.65, fc=Y, ec=R, lw=1.3))
        _txt(ax, 8.45, 4.0, 'm=3 overlaps\nm=2 red!', R, fs=7.3, ha='center')
        _txt(ax, 5.1, 0.45, 'Resolving power R = lam / dlam = n N  (3 x 400 = 1200 < 2 x 700 = 1400!)', I, fs=7.5, ha='center')
        return 'Diffraction grating orders, chromatic resolving power nN, and order overlap'

    # =========================================================================
    # JEE-12: Circular Airy Disc, Resolving Power & Pinhole Camera
    # =========================================================================
    if key == 'airy_rayleigh':
        u = np.linspace(-9.0, 12.8, 700)
        def airy(v):
            out = np.ones_like(v)
            nz = np.abs(v) > 1e-6
            out[nz] = (2.0 * _j1(v[nz]) / v[nz])**2
            return out
        u1 = 3.8317
        I1, I2 = airy(u), airy(u - u1)
        ax.plot(u/np.pi, I1, color=I, lw=1.25, ls='--', label='Source 1')
        ax.plot(u/np.pi, I2, color=T, lw=1.25, ls='--', label='Source 2 (1.22 lam/D)')
        ax.plot(u/np.pi, I1 + I2, color=R, lw=1.65, label='Sum (dip = 0.735)')
        _style_plot(ax, xlabel='Angle theta / (lam / D)', ylabel='Intensity I / I0')
        ax.set_ylim(-0.04, 1.44)
        ax.legend(loc='upper left', fontsize=6.9, frameon=True, facecolor='white', edgecolor=L)
        return 'Circular Airy pattern and Rayleigh 26.5% central saddle resolution limit'

    if key == 'pinhole_tradeoff':
        d = np.linspace(0.45, 3.6, 400)
        rg, rd = 0.5 * d, 1.22 / d
        rt = rg + rd
        d_opt = np.sqrt(2.44)
        ax.plot(d, rg, color=I, lw=1.25, ls='--', label='Geom D/2')
        ax.plot(d, rd, color=T, lw=1.25, ls=':', label='Diff 1.22 lam L/D')
        ax.plot(d, rt, color=R, lw=1.7, label='Total spot R_tot')
        ax.plot([d_opt], [0.5*d_opt + 1.22/d_opt], 'o', color=I, ms=5.5)
        _txt(ax, 1.25, 2.95, 'Min at D = sqrt(2.44 lam L)', I, fs=7.1, ha='center')
        _style_plot(ax, xlabel='Pinhole D / sqrt(lam L)', ylabel='Blur R / sqrt(lam L)')
        ax.set_ylim(0, 3.6)
        ax.legend(loc='upper right', fontsize=6.9, frameon=True, facecolor='white', edgecolor=L)
        return 'Optimal pinhole diameter balances geometric blur against Airy diffraction'

    # =========================================================================
    # JEE-13: Polarisation & Malus Stacks
    # =========================================================================
    if key == 'polarisation_states':
        _clean_canvas(ax)
        # 1. Unpolarised
        cx = 1.3
        for deg in range(0, 180, 30):
            th = np.deg2rad(deg)
            _arr(ax, (cx - 0.88*np.cos(th), 2.75 - 0.88*np.sin(th)),
                 (cx + 0.88*np.cos(th), 2.75 + 0.88*np.sin(th)), R, lw=1.1, style='<->')
        _txt(ax, cx, 0.72, 'Unpolarised\n(gives I0 / 2)', I, fs=7.5, ha='center')
        # 2. Linear
        cx = 3.9
        ax.plot([cx - 0.9, cx + 0.9], [2.75, 2.75], color=L, lw=1.0)
        ax.plot([cx, cx], [1.85, 3.65], color=L, lw=1.0)
        _arr(ax, (cx - 0.78, 2.75 - 0.78), (cx + 0.78, 2.75 + 0.78), I, lw=1.8, style='<->')
        _txt(ax, cx, 0.72, 'Linear\n(delta = 0, pi)', I, fs=7.5, ha='center')
        # 3. Circular
        cx = 6.45
        ax.add_patch(Circle((cx, 2.75), 0.86, fill=False, lw=1.7, ec=T))
        _txt(ax, cx, 0.72, 'Circular\n(Ax=Ay, pi/2)', T, fs=7.5, ha='center')
        # 4. Elliptical
        cx = 8.95
        t = np.linspace(0, 2*np.pi, 220)
        ax.plot(cx + 0.88*np.cos(t), 2.75 + 0.55*np.cos(t + 0.95), color=G, lw=1.7)
        _txt(ax, cx, 0.72, 'Elliptical\n(general delta)', G, fs=7.5, ha='center')
        return 'Transverse electric-field trajectories for pure and natural polarisation states'

    if key == 'malus_polaroids':
        _clean_canvas(ax)
        ax.plot([0.4, 9.8], [2.65, 2.65], color=G, lw=1.8)
        _txt(ax, 1.0, 3.35, 'Unpol\nI0', I, fs=7.6, ha='center')
        plates = [
            (2.15, 90, 'P1 (0 deg)', 'I0 / 2', I, P),
            (5.15, 45, 'P2 (theta)', '(I0/2) cos^2', T, P),
            (8.15, 0,  'P3 (90 deg)', '(I0/8) sin^2 2th', R, Y),
        ]
        for x, deg, top, out, ec, fc in plates:
            ax.add_patch(FancyBboxPatch((x - 0.32, 1.35), 0.64, 2.55, boxstyle='round,pad=0.05', fc=fc, ec=ec, lw=1.4))
            th = np.deg2rad(deg)
            _arr(ax, (x - 0.24*np.cos(th), 2.65 - 0.72*np.sin(th)),
                 (x + 0.24*np.cos(th), 2.65 + 0.72*np.sin(th)), ec, lw=1.3, style='<->')
            _txt(ax, x, 4.32, top, ec, fs=7.6, ha='center')
            _txt(ax, x + 1.25, 3.3, out, ec, fs=7.3, ha='center')
        _txt(ax, 5.1, 0.45, 'Peak output at theta = 45 deg: I0 / 8 (unpolarised) vs I_pol / 4 (polarised)', I, fs=7.5, ha='center')
        return 'Three-polaroid analyser train: rotated middle sheet restores blocked light'

    # =========================================================================
    # JEE-14: Brewster Angle & Rayleigh Scattering
    # =========================================================================
    if key == 'brewster_dipole':
        _clean_canvas(ax)
        ax.add_patch(Rectangle((0.3, 0.25), 9.4, 2.2, fc=P, ec='none'))
        ax.plot([0.3, 9.7], [2.45, 2.45], color=I, lw=1.5)
        ax.plot([4.7, 4.7], [0.45, 4.75], color=I, lw=0.85, ls=':')
        O = np.array([4.7, 2.45])
        thB, thr = np.deg2rad(56.3), np.deg2rad(33.7)
        _arr(ax, (O[0] - 2.8*np.sin(thB), O[1] + 2.8*np.cos(thB)), tuple(O), I, lw=1.55)
        _arr(ax, tuple(O), (O[0] + 2.8*np.sin(thB), O[1] + 2.8*np.cos(thB)), T, lw=1.6)
        _arr(ax, tuple(O), (O[0] + 2.8*np.sin(thr), O[1] - 2.8*np.cos(thr)), R, lw=1.6)
        for s in (1.05, 1.75, 2.45):
            pt = O + s*np.array([np.sin(thB), np.cos(thB)])
            ax.plot(pt[0], pt[1], 'o', color=T, ms=4.5)
        _txt(ax, 4.48, 4.05, 'theta_B', I, fs=7.9, ha='right')
        _txt(ax, 4.5, 1.15, 'theta_r', R, fs=7.9, ha='right')
        _txt(ax, 5.85, 2.8, '90 deg', G, fs=7.7)
        _txt(ax, 8.15, 4.25, '100% s-polarised\nreflected beam!', T, fs=7.6, ha='center')
        _txt(ax, 8.15, 0.85, 'Partially p-pol.\ntan theta_B = n2/n1', R, fs=7.6, ha='center')
        return 'Brewster condition theta_B + theta_r = 90 deg zeroes reflected p-component'

    if key == 'rayleigh_sky':
        _clean_canvas(ax)
        ax.add_patch(Circle((1.1, 3.65), 0.46, fc=Y, ec=G, lw=1.4))
        _txt(ax, 1.1, 3.65, 'Sun', G, fs=7.8, ha='center')
        _arr(ax, (1.7, 3.65), (5.1, 3.65), G, lw=1.65)
        ax.plot(5.4, 3.65, 'o', color=I, ms=7.8)
        _txt(ax, 5.4, 4.35, 'Air molecule (d << lam)', I, fs=7.7, ha='center')
        _arr(ax, (5.7, 3.65), (9.45, 3.65), R, lw=1.65)
        _txt(ax, 8.15, 4.3, 'Sunset (0 deg):\nRed, unpolarised', R, fs=7.5, ha='center')
        _arr(ax, (5.4, 3.35), (5.4, 0.85), T, lw=1.65)
        for yd in (2.7, 2.0, 1.35):
            ax.plot(5.4, yd, 'o', color=T, ms=4.6)
        _txt(ax, 2.55, 1.5, 'I_scat ~ 1 / lam^4\nBlue 4.4x Red!', I, fs=7.7, ha='center')
        _txt(ax, 7.95, 1.5, '90 deg overhead:\nLinearly polarised!', T, fs=7.6, ha='center')
        return 'Rayleigh dipole scattering makes the sky blue and linearly polarised at 90 deg'

    # =========================================================================
    # JEE-15: Uniaxial Birefringence & Wave-Plates
    # =========================================================================
    if key == 'uniaxial_wavefronts':
        _clean_canvas(ax)
        t = np.linspace(0, 2*np.pi, 240)
        # Left: Calcite (ne < no -> ve > vo)
        cx, cy = 2.6, 2.6
        ax.plot([cx, cx], [0.75, 4.45], color=I, lw=1.0, ls='--')
        ax.add_patch(Circle((cx, cy), 1.2, fill=False, lw=1.55, ec=I))
        ax.plot(cx + 1.72*np.cos(t), cy + 1.2*np.sin(t), color=R, lw=1.55)
        _txt(ax, cx, 4.72, 'Optic axis', I, fs=7.5, ha='center')
        _txt(ax, cx, 0.32, 'Negative: Calcite (ne < no)', R, fs=7.6, ha='center')
        # Right: Quartz (ne > no -> ve < vo)
        cx = 7.45
        ax.plot([cx, cx], [0.75, 4.45], color=I, lw=1.0, ls='--')
        ax.add_patch(Circle((cx, cy), 1.5, fill=False, lw=1.55, ec=I))
        ax.plot(cx + 1.08*np.cos(t), cy + 1.5*np.sin(t), color=T, lw=1.55)
        _txt(ax, cx, 4.72, 'Optic axis', I, fs=7.5, ha='center')
        _txt(ax, cx, 0.32, 'Positive: Quartz (ne > no)', T, fs=7.6, ha='center')
        return 'Huygens spherical o-surface and ellipsoidal e-surface in uniaxial crystals'

    if key == 'waveplate_ellipses':
        _clean_canvas(ax)
        t = np.linspace(0, 2*np.pi, 240)
        stages = [
            (1.3, 0.0, 'Input 45 deg\n(delta = 0)', I),
            (3.8, np.pi/4, 'delta = pi/4\nElliptical', G),
            (6.3, np.pi/2, 'QWP (pi/2)\nCircular!', T),
            (8.8, np.pi, 'HWP (pi)\nFlipped -45 deg', R),
        ]
        for cx, dlt, lbl, col in stages:
            ax.add_patch(Rectangle((cx - 0.88, 1.65), 1.76, 1.76, fill=False, ec=L, lw=1.0))
            ax.plot(cx + 0.76*np.cos(t), 2.53 + 0.76*np.cos(t + dlt), color=col, lw=1.65)
            _txt(ax, cx, 0.68, lbl, col, fs=7.4, ha='center')
        _txt(ax, 5.05, 4.25, 'Retardation delta = 2 pi |no - ne| t / lam0 on 45-deg linear input', I, fs=7.8, ha='center')
        return 'Evolution of polarisation state through quarter-wave and half-wave retarders'

    # =========================================================================
    # JEE-16: Master Scaling & 5-Step Phase Checklist
    # =========================================================================
    if key == 'scaling_radar':
        _clean_canvas(ax)
        boxes = [
            (0.3, 2.75, 'YDSE / Biprism', 'beta = lam D / d (const)\nIn liquid mu: beta / mu', I, P),
            (5.15, 2.75, "Newton's Rings", 'D_n = sqrt(4 n lam R / mu)\nIn liquid mu: D_n / sqrt(mu)!', T, P),
            (0.3, 0.35, 'Slit vs Airy Disc', 'Central slit = 2 lam D / a\nAiry dark = 1.22 lam / D', R, Y),
            (5.15, 0.35, 'Polaroid / QWP', 'Crossed + 45 deg -> I0 / 8\nP + QWP(45) + A -> I0 / 4', G, Y),
        ]
        for x, y, hd, bd, ec, fc in boxes:
            ax.add_patch(FancyBboxPatch((x, y), 4.55, 1.95, boxstyle='round,pad=0.06', fc=fc, ec=ec, lw=1.3))
            _txt(ax, x + 2.27, y + 1.55, hd, ec, fs=7.8, ha='center')
            _txt(ax, x + 2.27, y + 0.65, bd, I, fs=7.3, ha='center')
        return 'Instant scaling comparison across interference, diffraction and polarisation'

    if key == 'phase_checklist':
        _clean_canvas(ax)
        steps = [
            (0.3, '1. Split', 'Wavefront\nor Amp?', I),
            (2.25, '2. OPL', 'Sum n_i x_i\n(use lam0)', T),
            (4.2, '3. Flips', '+pi per\nrare->dense', R),
            (6.15, '4. Vector', 'e1 . e2\nprojection', G),
            (8.1, '5. Envelope', 'Sinc / Airy\nmissing n?', I),
        ]
        for idx, (x, hd, sub, col) in enumerate(steps):
            ax.add_patch(FancyBboxPatch((x, 1.35), 1.62, 2.35, boxstyle='round,pad=0.06', fc=P, ec=col, lw=1.35))
            _txt(ax, x + 0.81, 3.15, hd, col, fs=7.6, ha='center')
            _txt(ax, x + 0.81, 2.02, sub, I, fs=7.1, ha='center')
            if idx < 4:
                _arr(ax, (x + 1.66, 2.52), (x + 1.91, 2.52), I, lw=1.15)
        _txt(ax, 5.0, 0.55, 'Total dphi = (2 pi / lam0) d_opt + N_dense pi  =>  Bright 2m pi, Dark (2m+1) pi', I, fs=7.5, ha='center')
        return 'Five-step phase bookkeeping checklist for zero sign or half-wave errors'

    # =========================================================================
    # Olympiad-01: Michelson Interferometer & Doublet Beats
    # =========================================================================
    if key == 'michelson_layout':
        _clean_canvas(ax)
        ax.plot([4.3, 5.6], [2.0, 3.3], color=I, lw=2.5)
        ax.plot([6.1, 7.1], [2.15, 3.15], color=T, lw=1.9, ls='--')
        ax.plot([8.85, 8.85], [1.95, 3.35], color=I, lw=3.0)
        ax.plot([4.25, 5.65], [4.65, 4.65], color=R, lw=3.0)
        _arr(ax, (1.0, 2.65), (4.95, 2.65), G, lw=1.55)
        _arr(ax, (4.95, 2.65), (4.95, 4.6), R, lw=1.4, style='<->')
        _arr(ax, (4.95, 2.65), (8.8, 2.65), I, lw=1.4, style='<->')
        _arr(ax, (4.95, 2.65), (4.95, 0.65), T, lw=1.55)
        _txt(ax, 1.0, 3.1, 'Source', I, fs=7.8)
        _txt(ax, 5.95, 4.6, 'Movable M1 (dx)', R, fs=7.7)
        _txt(ax, 8.85, 3.68, 'Fixed M2', I, fs=7.7, ha='center')
        _txt(ax, 3.95, 3.25, 'BS', I, fs=8.0)
        _txt(ax, 6.8, 3.5, 'Compensator C', T, fs=7.5, ha='center')
        _txt(ax, 5.35, 0.72, 'Detector: 2d cos(theta) = m lam', T, fs=7.6)
        return 'Michelson double-pass arms, virtual air plate d, and glass compensator plate C'

    if key == 'doublet_visibility':
        dx = np.linspace(0, 0.62, 700)
        env = np.abs(np.cos(np.pi * dx / 0.289))
        carrier = 0.5 + 0.5 * env * np.cos(2 * np.pi * dx * 38.0)
        ax.plot(dx, carrier, color=L, lw=1.0)
        ax.plot(dx, 0.5 + 0.5*env, color=R, lw=1.65, label='Visibility envelope V(dx)')
        ax.plot(dx, 0.5 - 0.5*env, color=R, lw=1.25, ls='--')
        _arr(ax, (0.1445, 0.08), (0.4335, 0.08), I, lw=1.15, style='<->')
        _txt(ax, 0.46, 1.28, 'Beat dx = 0.289 mm', I, fs=7.1, ha='center')
        _style_plot(ax, xlabel='Mirror travel dx (mm)', ylabel='Norm. signal')
        ax.set_ylim(-0.04, 1.52)
        ax.legend(loc='upper left', fontsize=6.8, frameon=True, facecolor='white', edgecolor=L)
        return 'Sodium D-doublet interferogram beats vanish every 0.289 mm of mirror travel'

    # =========================================================================
    # Olympiad-02: Temporal & Spatial Coherence + Stellar Interferometry
    # =========================================================================
    if key == 'temporal_coherence':
        x = np.linspace(0, 2.6, 500)
        ax.plot(x, np.abs(np.sinc(x)), color=I, lw=1.55, label='Top-hat |sinc|')
        ax.plot(x, np.exp(-(np.pi**2 / (4*np.log(2))) * (x * 0.55)**2), color=T, lw=1.45, ls='--', label='Gaussian line')
        ax.plot(x, np.exp(-np.pi * x * 0.5), color=R, lw=1.4, ls=':', label='Lorentzian line')
        ax.axvline(1.0, color=G, lw=1.0, ls='--')
        _txt(ax, 1.07, 0.44, 'tau_c = 1/dnu\nLc = c tau_c', I, fs=7.3)
        _style_plot(ax, xlabel='Delay tau * dnu = d / Lc', ylabel='Coherence |gamma|')
        ax.set_ylim(-0.03, 1.22)
        ax.legend(loc='upper right', fontsize=6.9, frameon=True, facecolor='white', edgecolor=L)
        return 'Wiener-Khinchin transform pairs spectral line shape with fringe visibility'

    if key == 'stellar_interferometer':
        _clean_canvas(ax)
        ax.plot([1.8, 1.8], [4.55, 0.65], 's', color=R, ms=6.8)
        ax.plot([3.6, 3.6], [3.45, 1.75], 's', color=I, ms=6.2)
        for yy in (4.55, 0.65):
            _arr(ax, (0.35, yy), (1.8, yy), G, lw=1.45)
        ax.plot([1.8, 1.8, 5.4], [4.55, 3.45, 3.45], color=I, lw=1.3)
        ax.plot([1.8, 1.8, 5.4], [0.65, 1.75, 1.75], color=I, lw=1.3)
        ax.add_patch(FancyBboxPatch((5.35, 1.15), 0.25, 2.9, boxstyle='round,pad=0.06', fc=P, ec=T, lw=1.4))
        ax.plot([5.6, 8.8], [3.45, 2.6], color=T, lw=1.35)
        ax.plot([5.6, 8.8], [1.75, 2.6], color=T, lw=1.35)
        ax.plot([8.8, 8.8], [1.45, 3.75], color=I, lw=2.0)
        _arr(ax, (2.35, 0.65), (2.35, 4.55), R, lw=1.15, style='<->')
        _txt(ax, 2.52, 2.6, 'b', R, fs=8.1)
        _txt(ax, 7.65, 4.45, 'Washout: theta_* = 1.22 lam / b', I, fs=7.5, ha='center')
        _txt(ax, 7.55, 0.65, 'Betelgeuse: b = 3.07 m -> 0.047 arcsec', T, fs=7.3, ha='center')
        return 'Michelson periscope stellar interferometer beats atmospheric seeing limits'

    # =========================================================================
    # Olympiad-03: Exact Fresnel Equations & Dielectric Stacks
    # =========================================================================
    if key == 'fresnel_reflectance':
        deg = np.linspace(0, 89.8, 500)
        i = np.deg2rad(deg)
        n1, n2 = 1.0, 1.5
        r = np.arcsin((n1 / n2) * np.sin(i))
        Rs = ((n1*np.cos(i) - n2*np.cos(r)) / (n1*np.cos(i) + n2*np.cos(r)))**2
        Rp = ((n2*np.cos(i) - n1*np.cos(r)) / (n2*np.cos(i) + n1*np.cos(r)))**2
        ax.plot(deg, 100*Rs, color=I, lw=1.65, label='Rs (TE, _|_ plane)')
        ax.plot(deg, 100*Rp, color=R, lw=1.65, label='Rp (TM, || plane)')
        ax.plot(deg, 50*(Rs + Rp), color=T, lw=1.2, ls='--', label='Unpolarised avg')
        ax.plot([56.31], [0.0], 'o', color=R, ms=5.5)
        _txt(ax, 46.0, 56.0, 'Brewster 56.3 deg\n(Rp = 0!)', R, fs=7.1, ha='center')
        _style_plot(ax, xlabel='Incidence angle i (deg)', ylabel='Reflectance (%)')
        ax.set_ylim(-2, 105)
        ax.legend(loc='upper left', fontsize=6.9, frameon=True, facecolor='white', edgecolor=L)
        return 'Exact air-glass (n = 1.50) Fresnel power reflectances Rs(i) and Rp(i)'

    if key == 'multilayer_coatings':
        wl = np.linspace(400, 750, 500)
        nc, ng = 1.38, 1.52
        r1, r2 = (1.0 - nc)/(1.0 + nc), (nc - ng)/(nc + ng)
        dlt = np.pi * (550.0 / wl)
        R_ar = np.abs((r1 + r2*np.exp(2j*dlt)) / (1 + r1*r2*np.exp(2j*dlt)))**2
        nc2 = np.sqrt(ng)
        r1p, r2p = (1.0 - nc2)/(1.0 + nc2), (nc2 - ng)/(nc2 + ng)
        R_id = np.abs((r1p + r2p*np.exp(2j*dlt)) / (1 + r1p*r2p*np.exp(2j*dlt)))**2
        ax.axhline(4.26, color=G, lw=1.2, ls=':', label='Uncoated glass (4.3%)')
        ax.plot(wl, 100*R_ar, color=I, lw=1.65, label='MgF2 AR (1.26% min)')
        ax.plot(wl, 100*R_id, color=T, lw=1.45, ls='--', label='Ideal sqrt(n_g) (0% at 550)')
        _style_plot(ax, xlabel='Wavelength lam (nm)', ylabel='Reflectance (%)')
        ax.set_ylim(-0.15, 6.2)
        ax.legend(loc='upper right', fontsize=6.8, frameon=True, facecolor='white', edgecolor=L)
        return 'Quarter-wave AR spectral curve (550 nm zero explains purple lens tint)'

    # =========================================================================
    # Olympiad-04: TIR Phase Shifts & Evanescent Tunnelling
    # =========================================================================
    if key == 'tir_phase_shift':
        n = 1.0 / 1.51
        tc = np.rad2deg(np.arcsin(n))
        deg = np.linspace(tc + 0.02, 89.9, 500)
        i = np.deg2rad(deg)
        ds = 2.0 * np.rad2deg(np.arctan(np.sqrt(np.sin(i)**2 - n**2) / np.cos(i)))
        dp = 2.0 * np.rad2deg(np.arctan(np.sqrt(np.sin(i)**2 - n**2) / (n**2 * np.cos(i))))
        ax.plot(deg, dp, color=R, lw=1.5, label='delta_p (TM)')
        ax.plot(deg, ds, color=I, lw=1.5, label='delta_s (TE)')
        ax.plot(deg, dp - ds, color=T, lw=1.75, label='dp - ds (Rhomb)')
        ax.axhline(45.0, color=G, lw=1.0, ls='--')
        _txt(ax, 76.0, 68.0, 'Rhomb: 2x45=90 deg', T, fs=6.9, ha='center')
        _style_plot(ax, xlabel='Internal angle i > theta_c (deg)', ylabel='Phase (deg)')
        ax.set_ylim(0, 196)
        ax.legend(loc='upper left', fontsize=6.8, frameon=True, facecolor='white', edgecolor=L)
        return 'TIR phase shifts in crown glass: two 45-deg bounces make an achromatic QWP'

    if key == 'evanescent_ftir':
        _clean_canvas(ax)
        ax.add_patch(Rectangle((0.3, 0.25), 9.4, 1.6, fc=P, ec=I, lw=1.1))
        ax.add_patch(Rectangle((0.3, 3.25), 9.4, 1.6, fc=P, ec=I, lw=1.1))
        _txt(ax, 0.55, 1.15, 'Prism 1 (n1)', I, fs=7.6)
        _txt(ax, 1.2, 4.25, 'Prism 2 (n1)', I, fs=7.8)
        _arr(ax, (1.9, 0.35), (3.8, 1.85), R, lw=1.65)
        _arr(ax, (3.8, 1.85), (5.7, 0.35), R, lw=1.5)
        zy = np.linspace(1.85, 3.25, 160)
        ex = 4.35 + 1.55 * np.exp(-2.1 * (zy - 1.85))
        ax.fill_betweenx(zy, 4.35, ex, color=Y)
        ax.plot(ex, zy, color=T, lw=1.7)
        _arr(ax, (4.65, 3.25), (6.45, 4.72), T, lw=1.55)
        _txt(ax, 7.45, 2.52, '|E| ~ exp(-kappa z)\nT ~ exp(-2 kappa g)', T, fs=7.5, ha='center')
        _arr(ax, (9.2, 1.85), (9.2, 3.25), I, lw=1.1, style='<->')
        _txt(ax, 9.45, 2.55, 'g', I, fs=8.2)
        return 'Evanescent field skin depth and Frustrated TIR optical barrier tunnelling'

    # =========================================================================
    # Olympiad-05: Exact N-Slit Factor & Blazed Gratings
    # =========================================================================
    if key == 'n_slit_pattern':
        N = 6
        g = np.linspace(-0.22*np.pi, 1.22*np.pi, 1200)
        den = np.sin(g)
        Irr = np.where(np.abs(den) < 1e-7, N**2, (np.sin(N*g) / den)**2) / (N**2)
        ax.fill_between(g/np.pi, 0, Irr, color=P)
        ax.plot(g/np.pi, Irr, color=I, lw=1.55)
        _txt(ax, 0.5, 0.3, 'N = 6 slits:\nN-1 = 5 dark zeros\nN-2 = 4 side peaks!', R, fs=7.4, ha='center')
        _style_plot(ax, xlabel='gamma / pi = (d sin theta) / lam', ylabel='Norm. I / N^2 I0')
        ax.set_ylim(-0.03, 1.12)
        return 'Exact N-slit interference factor sharpening principal lines as width ~ 1/N'

    if key == 'blazed_grating':
        _clean_canvas(ax)
        pts = [(0.7, 0.8)]
        for k in range(4):
            x0 = 0.7 + k * 2.15
            pts.extend([(x0, 0.8), (x0 + 1.85, 1.75), (x0 + 1.85, 0.8)])
        pts.append((9.3, 0.8))
        ax.add_patch(Polygon(pts, fc=P, ec=I, lw=1.35))
        nb = np.deg2rad(26.8)
        for k in range(1, 4):
            cx, cy = 0.7 + k*2.15 - 1.15, 1.28
            _arr(ax, (cx - 1.45*np.sin(nb), cy + 2.6*np.cos(nb)), (cx, cy), R, lw=1.5, style='<->')
        _txt(ax, 5.0, 4.45, 'Littrow Blaze (i = theta_m = theta_b):  lam_blaze = 2 d sin(theta_b) / m', I, fs=7.6, ha='center')
        _txt(ax, 8.15, 2.45, 'Sawtooth facet\nsteers energy\nto order m!', T, fs=7.5, ha='center')
        return 'Sawtooth blazed reflection echelle grating concentrates 85% power into order m'

    # =========================================================================
    # Olympiad-06: Fabry-Perot Etalons & Wiener Standing Light Wave
    # =========================================================================
    if key == 'fabry_perot_airy':
        dlt = np.linspace(-0.6*np.pi, 2.6*np.pi, 1500)
        for Refl, col, ls, lbl in (
            (0.25, G, ':', 'R = 0.25 (Finesse 2.1)'),
            (0.70, T, '--', 'R = 0.70 (Finesse 8.8)'),
            (0.93, I, '-', 'R = 0.93 (Finesse 43.3)'),
        ):
            F = 4 * Refl / (1 - Refl)**2
            ax.plot(dlt / (2*np.pi), 1.0 / (1.0 + F * np.sin(0.5*dlt)**2), color=col, lw=1.55, ls=ls, label=lbl)
        _style_plot(ax, xlabel='Resonance order m = delta / (2 pi)', ylabel='Trans. T_FP')
        ax.set_ylim(-0.03, 1.44)
        ax.legend(loc='upper right', fontsize=6.9, frameon=True, facecolor='white', edgecolor=L)
        return 'Fabry-Perot Airy resonances reach T = 100% even when each mirror reflects 99%'

    if key == 'standing_light_wave':
        z = np.linspace(0, 2.5, 600)
        ax.axvline(0.0, color=I, lw=3.0)
        ax.plot(z, np.abs(np.sin(2*np.pi*z)), color=R, lw=1.6, label='|E(z)| node at z=0')
        ax.plot(z, np.abs(np.cos(2*np.pi*z)), color=I, lw=1.25, ls='--', label='|B(z)| antinode z=0')
        ax.plot([0.0, 2.45], [0.12, 0.92], color=T, lw=1.45, label='Wiener tilted film')
        _style_plot(ax, xlabel='Mirror distance z / lam', ylabel='Norm. amp.')
        ax.set_ylim(-0.04, 1.52)
        ax.legend(loc='upper right', fontsize=6.8, frameon=True, facecolor='white', edgecolor=L)
        return 'Wiener 1890 experiment: emulsion blackens at E antinodes, proving E acts on matter'

    # =========================================================================
    # Olympiad-07: Fresnel Zones, Zone Plate & Cornu Spiral
    # =========================================================================
    if key == 'fresnel_zones':
        _clean_canvas(ax)
        cx, cy = 2.55, 2.65
        for m in range(6, 0, -1):
            ax.add_patch(Circle((cx, cy), 0.74*np.sqrt(m), fc=I if m % 2 == 0 else Y, ec=I, lw=0.95))
        _txt(ax, cx, 0.32, 'Zone radii r_m = sqrt(m lam b)', I, fs=7.6, ha='center')
        _arr(ax, (5.3, 4.15), (9.5, 4.15), I, lw=1.65)
        _arr(ax, (9.5, 3.45), (5.45, 3.45), R, lw=1.5)
        _arr(ax, (5.45, 2.75), (9.35, 2.75), I, lw=1.45)
        _arr(ax, (5.3, 1.35), (7.4, 1.35), T, lw=1.85)
        ax.plot([7.4, 7.4], [1.05, 4.25], color=T, lw=0.95, ls=':')
        _txt(ax, 7.4, 4.6, '+A1', I, fs=7.7, ha='center')
        _txt(ax, 8.35, 3.68, '-A2', R, fs=7.5)
        _txt(ax, 7.4, 0.42, 'A_open = A1/2  =>  1-zone I = 4 I0!', T, fs=7.6, ha='center')
        return 'Fresnel half-period zone plate and alternating spiral sum A1 - A2 + A3 - ... = A1/2'

    if key == 'cornu_spiral':
        u = np.linspace(-2.4, 4.4, 700)
        S, C = _fresnel(u)
        I_edge = 0.5 * ((0.5 + C)**2 + (0.5 + S)**2)
        ax.fill_between(u, 0, I_edge, where=(u < 0), color=Y)
        ax.fill_between(u, 0, I_edge, where=(u >= 0), color=P)
        ax.plot(u, I_edge, color=I, lw=1.65)
        ax.axvline(0.0, color=R, lw=1.1, ls='--')
        ax.plot([0.0, 1.217], [0.25, 1.37], 'o', color=R, ms=5.2)
        _txt(ax, -1.25, 0.46, 'Edge v=0:\nI = I0 / 4!', R, fs=7.3, ha='center')
        _txt(ax, 2.35, 1.35, 'Peak 1.37 I0', R, fs=7.3)
        _style_plot(ax, xlabel='Fresnel variable v = y sqrt(2 / lam b)', ylabel='Intensity I / I0')
        ax.set_ylim(0, 1.56)
        return 'Fresnel straight-edge shadow transition: exact I0/4 at geometric edge v = 0'

    # =========================================================================
    # Olympiad-08: Abbe Spatial Filtering, X-Ray Bragg & Sagnac Gyro
    # =========================================================================
    if key == 'abbe_spatial_filter':
        _clean_canvas(ax)
        ax.plot([1.15, 1.15], [1.15, 3.6], color=I, lw=2.3, ls='--')
        ax.add_patch(FancyBboxPatch((4.0, 0.95), 0.3, 2.7, boxstyle='round,pad=0.06', fc=P, ec=T, lw=1.4))
        ax.plot([6.65, 6.65], [0.95, 3.7], color=R, lw=1.5, ls=':')
        ax.plot([9.4, 9.4], [1.15, 3.6], color=I, lw=2.1)
        for yf, col, lbl in ((3.35, I, 'm=+1'), (2.35, R, 'm=0'), (1.35, I, 'm=-1')):
            ax.plot([1.15, 4.15, 6.65, 9.4], [2.35, 2.35 + 0.85*(yf - 2.35), yf, 2.35], color=col, lw=1.05)
            ax.plot(6.65, yf, 'o', color=col, ms=5.0)
            _txt(ax, 7.15, yf + (0.34 if yf > 3 else (-0.36 if yf < 2 else 0.3)), lbl, col, fs=7.2)
        _txt(ax, 1.15, 4.35, 'Object', I, fs=7.5, ha='center')
        _txt(ax, 4.15, 4.48, 'Objective\nNA = n sin u', T, fs=7.2, ha='center')
        _txt(ax, 6.65, 4.48, "Fourier\nPlane F'", R, fs=7.2, ha='center')
        _txt(ax, 9.4, 4.35, 'Image', I, fs=7.5, ha='center')
        _txt(ax, 5.2, 0.35, 'Need >= 2 orders inside aperture  =>  d_min = lam0 / (2 NA)', I, fs=7.5, ha='center')
        return 'Abbe two-step Fourier imaging and spatial filtering in back focal plane F-prime'

    if key == 'bragg_sagnac':
        _clean_canvas(ax)
        for yy in (1.15, 2.35):
            ax.plot([0.45, 4.75], [yy, yy], color=L, lw=1.2)
            for xx in np.linspace(0.75, 4.45, 6):
                ax.plot(xx, yy, 'o', color=I, ms=4.5)
        _arr(ax, (0.7, 3.65), (2.6, 2.35), R, lw=1.35)
        _arr(ax, (2.6, 2.35), (4.5, 3.65), R, lw=1.35)
        _arr(ax, (0.7, 2.45), (2.6, 1.15), T, lw=1.35)
        _arr(ax, (2.6, 1.15), (4.5, 2.45), T, lw=1.35)
        _txt(ax, 2.6, 4.35, 'Bragg: 2 d sin(theta) = n lam', I, fs=7.6, ha='center')
        _txt(ax, 2.6, 0.35, 'theta measured FROM plane!', R, fs=7.4, ha='center')
        cx, cy = 7.95, 2.45
        ax.add_patch(Circle((cx, cy), 1.35, fill=False, lw=1.65, ec=I))
        ax.add_patch(Circle((cx, cy), 1.08, fill=False, lw=1.4, ls='--', ec=R))
        ax.plot([cx - 0.25, cx + 0.25], [cy - 1.52, cy - 1.18], color=I, lw=2.3)
        _txt(ax, cx, cy + 0.1, 'Area A\nOmega', I, fs=7.4, ha='center')
        _txt(ax, cx, 4.35, 'Sagnac Ring Gyro', I, fs=7.7, ha='center')
        _txt(ax, cx, 0.35, 'dPhi = 8 pi Omega.A / (lam0 c)', T, fs=7.3, ha='center')
        return 'Crystal X-ray Bragg reflection (glancing angle!) and rotating Sagnac interferometer'

    raise KeyError(f'Unknown diagram key: {key!r}')
