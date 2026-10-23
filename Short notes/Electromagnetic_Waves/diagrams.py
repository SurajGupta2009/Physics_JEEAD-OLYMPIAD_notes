"""Analytic schematics and quantitative plots for all 18 Electromagnetic Waves sheets (36 panels).

Every panel is generated purely from Maxwell/wave equations in numpy + matplotlib:
no raster images, screenshots, or external network assets are used.
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, FancyArrowPatch, Arc, Polygon, Wedge

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


def _txt(ax, x, y, s, color=I, fs=8.4, ha='left', va='center'):
    ax.text(x, y, s, color=color, fontsize=fs, ha=ha, va=va, zorder=5)


def figure(ax, key):
    # =========================================================================
    # JEE-01: Ampere paradox & displacement current
    # =========================================================================
    if key == 'ampere_surfaces':
        _clean_canvas(ax)
        # Lead wires & capacitor plates
        ax.plot([0.6, 4.3], [2.6, 2.6], color=I, lw=2.2)
        ax.plot([5.9, 9.4], [2.6, 2.6], color=I, lw=2.2)
        _arr(ax, (1.1, 2.95), (2.5, 2.95), R, lw=1.8)
        _txt(ax, 1.8, 3.42, 'Ic', R, fs=9.2, ha='center')
        ax.add_patch(Rectangle((4.3, 1.05), 0.22, 3.1, fc='#cfe5e1', ec=I, lw=1.5))
        ax.add_patch(Rectangle((5.68, 1.05), 0.22, 3.1, fc='#cfe5e1', ec=I, lw=1.5))
        for yy in (1.55, 2.25, 2.95, 3.65):
            _arr(ax, (4.65, yy), (5.55, yy), T, lw=1.2)
        _txt(ax, 5.1, 4.55, 'dE/dt in gap: Id = Ic', T, fs=8.5, ha='center')
        # Amperian loop C around left wire + flat S1 vs bulging S2
        t = np.linspace(0, 2 * np.pi, 160)
        ax.plot(3.15 + 0.32 * np.cos(t), 2.6 + 1.18 * np.sin(t), color=I, lw=1.8)
        _txt(ax, 3.15, 0.92, 'loop C: S1 cuts wire', I, fs=8.2, ha='center')
        th = np.linspace(-np.pi / 2, np.pi / 2, 120)
        ax.plot(3.15 + 2.02 * np.cos(th), 2.6 + 1.18 * np.sin(th), color=G, lw=1.7, ls='--')
        _txt(ax, 7.65, 4.15, 'bulging S2 cuts gap', G, fs=8.3, ha='center')
        _txt(ax, 7.65, 1.18, 'same rim -> same B loop', I, fs=8.2, ha='center')
        return 'One Amperian rim C spanned by flat surface S1 (Ic) or gap surface S2 (Id)'

    if key == 'flux_circuit':
        _style_plot(ax, 'wt  (rad)', 'normalised signal')
        t = np.linspace(0, 2 * np.pi, 300)
        ax.plot(t, np.sin(t), color=T, lw=2.0, label='flux Phi_E / Phi_0')
        ax.plot(t, np.cos(t), color=R, lw=1.9, ls='--', label='Id / I0 = d(Phi_E)/d(wt)')
        ax.set_xlim(0, 2 * np.pi)
        ax.set_ylim(-1.35, 1.55)
        ax.set_xticks([0, np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi])
        ax.set_xticklabels(['0', 'pi/2', 'pi', '3pi/2', '2pi'])
        ax.legend(loc='upper right', frameon=True, fontsize=7.6)
        return 'Sinusoidal plate voltage: displacement current leads electric flux by pi/2'

    # =========================================================================
    # JEE-02: Gap magnetic field & dielectric split
    # =========================================================================
    if key == 'gap_b_profile':
        _style_plot(ax, 'radial ratio  r / a', 'B_phi / B(a)')
        r1 = np.linspace(0, 1.0, 80)
        r2 = np.linspace(1.0, 3.5, 160)
        ax.plot(r1, r1, color=T, lw=2.2)
        ax.plot(r2, 1.0 / r2, color=R, lw=2.2)
        ax.axvline(1.0, color=I, lw=1.0, ls=':')
        ax.set_xlim(0, 3.5)
        ax.set_ylim(0, 1.25)
        _txt(ax, 0.22, 0.86, 'inside: ~ r', T, fs=8.2)
        _txt(ax, 1.65, 0.86, 'outside: ~ 1/r', R, fs=8.2)
        _txt(ax, 1.08, 1.12, 'peak at rim r = a', I, fs=7.9)
        return 'Gap magnetic field rises linearly inside the plate radius and falls as 1/r outside'

    if key == 'dielectric_split':
        _style_plot(ax, 'dielectric constant  kappa', 'fraction of total  Ic')
        k = np.linspace(1.0, 8.0, 200)
        ax.plot(k, 1.0 / k, color=T, lw=2.1, label='vacuum part  1/kappa')
        ax.plot(k, 1.0 - 1.0 / k, color=R, lw=2.1, label='polarisation  1 - 1/kappa')
        ax.axhline(1.0, color=I, lw=1.0, ls=':')
        ax.set_xlim(1, 8)
        ax.set_ylim(0, 1.28)
        ax.legend(loc='center right', frameon=True, fontsize=7.6)
        return 'Vacuum displacement vs bound polarisation current share in a filled capacitor'

    # =========================================================================
    # JEE-03: Maxwell four laws & constitutive map
    # =========================================================================
    if key == 'four_laws_geometry':
        _clean_canvas(ax)
        # Left: closed Gaussian box
        ax.add_patch(Rectangle((0.9, 1.3), 2.6, 2.3, fc=P, ec=T, lw=1.8))
        _arr(ax, (3.5, 2.45), (4.45, 2.45), T, lw=1.6)
        _arr(ax, (2.2, 3.6), (2.2, 4.45), T, lw=1.6)
        _txt(ax, 2.2, 2.45, 'rho_f inside\nrho_B = 0', I, fs=7.1, ha='center')
        _txt(ax, 2.2, 0.72, 'closed surface: Gauss laws', T, fs=8.2, ha='center')
        # Right: open surface with Stokes rim
        th = np.linspace(0, 2 * np.pi, 160)
        ax.fill(7.35 + 1.55 * np.cos(th), 2.35 + 0.92 * np.sin(th), color='#f7f3e3', zorder=1)
        ax.plot(7.35 + 1.55 * np.cos(th), 2.35 + 0.92 * np.sin(th), color=R, lw=1.9)
        _arr(ax, (7.35, 2.45), (7.35, 4.35), I, lw=1.7)
        _txt(ax, 7.62, 4.15, 'dB/dt  or  J + dD/dt', I, fs=7.9)
        _txt(ax, 7.35, 0.72, 'open surface rim: Faraday & Ampere', R, fs=8.2, ha='center')
        return 'Gauss laws integrate over closed volumes; curl laws integrate around open rims'

    if key == 'constitutive_map':
        _style_plot(ax, 'relative permittivity  eps_r', 'index n  or  Z / Z0')
        er = np.linspace(1.0, 9.0, 200)
        ax.plot(er, np.sqrt(er), color=T, lw=2.1, label='n = sqrt(eps_r)  (mu_r = 1)')
        ax.plot(er, 1.0 / np.sqrt(er), color=R, lw=2.1, label='Z / Z0 = 1 / sqrt(eps_r)')
        ax.set_xlim(1, 9)
        ax.set_ylim(0, 3.3)
        ax.legend(loc='upper left', frameon=True, fontsize=7.6)
        return 'Nonmagnetic dielectrics raise refractive index n while lowering wave impedance Z'

    # =========================================================================
    # JEE-04: Wave equations & refractive wavelength
    # =========================================================================
    if key == 'refractive_wavelength':
        _clean_canvas(ax)
        ax.add_patch(Rectangle((4.8, 0.7), 4.7, 3.7, fc='#e7f3f1', ec=T, lw=1.3))
        ax.plot([4.8, 4.8], [0.55, 4.55], color=I, lw=1.8)
        z1 = np.linspace(0.5, 4.8, 220)
        z2 = np.linspace(4.8, 9.4, 300)
        lam0 = 2.0
        n = 1.65
        ax.plot(z1, 2.55 + 1.05 * np.sin(2 * np.pi * (z1 - 4.8) / lam0), color=T, lw=2.0)
        ax.plot(z2, 2.55 + 0.82 * np.sin(2 * np.pi * n * (z2 - 4.8) / lam0), color=R, lw=2.0)
        _txt(ax, 2.4, 4.35, 'vacuum: v = c, lambda_0', T, fs=7.1, ha='center')
        _txt(ax, 7.15, 4.35, 'medium: lambda = lambda_0 / n', R, fs=7.0, ha='center')
        _txt(ax, 5.0, 0.30, 'same frequency f across stationary boundary', I, fs=7.3, ha='center')
        return 'Entering a medium of index n compresses wavelength while preserving frequency f'

    if key == 'speed_vs_index':
        _style_plot(ax, 'relative permittivity  eps_r', 'phase speed  v / c')
        er = np.linspace(1.0, 9.0, 200)
        ax.plot(er, 1.0 / np.sqrt(er), color=T, lw=2.1, label='nonmagnetic  mu_r = 1')
        ax.plot(er, 1.0 / np.sqrt(4.0 * er), color=R, lw=2.0, ls='--', label='magnetic  mu_r = 4')
        ax.set_xlim(1, 9)
        ax.set_ylim(0, 1.12)
        ax.legend(loc='upper right', frameon=True, fontsize=7.6)
        return 'Phase speed v = c / sqrt(mu_r eps_r): both constitutive factors enter equally'

    # =========================================================================
    # JEE-05: Plane-wave phase & right-handed triad
    # =========================================================================
    if key == 'triad_wave':
        _clean_canvas(ax)
        _arr(ax, (0.7, 2.4), (9.4, 2.4), I, lw=1.7)
        _txt(ax, 9.45, 2.0, '+z (k)', I, fs=8.4, ha='right')
        z = np.linspace(1.0, 8.8, 220)
        s = np.sin(2 * np.pi * (z - 1.0) / 3.9)
        ey = 2.4 + 1.55 * s
        bx = z + 0.48 * s
        by = 2.4 - 0.52 * s
        ax.plot(z, ey, color=T, lw=2.2)
        ax.plot(bx, by, color=R, lw=2.0, ls='--')
        for zc in np.linspace(1.3, 8.5, 13):
            sc = np.sin(2 * np.pi * (zc - 1.0) / 3.9)
            ax.plot([zc, zc], [2.4, 2.4 + 1.55 * sc], color=T, lw=0.85)
            ax.plot([zc, zc + 0.48 * sc], [2.4, 2.4 - 0.52 * sc], color=R, lw=0.85)
        _txt(ax, 2.1, 4.45, 'E along +x (in phase)', T, fs=8.3)
        _txt(ax, 5.7, 0.82, 'B = (k_hat x E)/v along +y', R, fs=8.3)
        return 'Single travelling plane wave: E and B oscillate in phase and cross into +k'

    if key == 'triad_cross':
        _clean_canvas(ax)
        o = (2.7, 1.65)
        _arr(ax, o, (2.7, 4.45), T, lw=2.2, ms=14)
        _arr(ax, o, (1.05, 0.62), R, lw=2.2, ms=14)
        _arr(ax, o, (5.55, 1.65), G, lw=2.3, ms=14)
        _txt(ax, 2.95, 4.45, 'E_hat', T, fs=9.2)
        _txt(ax, 0.72, 0.98, 'B_hat', R, fs=9.2)
        _txt(ax, 5.72, 1.65, 'k_hat  (E x B)', G, fs=9.0)
        _txt(ax, 6.05, 3.85, 'E . B = 0', I, fs=8.6)
        _txt(ax, 6.05, 3.10, 'E . k_hat = B . k_hat = 0', I, fs=8.4)
        _txt(ax, 6.05, 2.35, 'E0 = v B0   (not c if n > 1)', R, fs=8.2)
        return 'Right-handed triad: reversing BOTH E and B half a cycle later keeps S forward'

    # =========================================================================
    # JEE-06: Polarisation states & Malus law
    # =========================================================================
    if key == 'lissajous_states':
        _clean_canvas(ax)
        phi = np.linspace(0, 2 * np.pi, 240)
        specs = [
            (2.0, 'linear\ndelta = 0', np.cos(phi), np.cos(phi), T),
            (5.0, 'circular\ndelta = pi/2', np.cos(phi), np.sin(phi), R),
            (8.0, 'elliptical\ndelta = pi/3', np.cos(phi), 0.72 * np.cos(phi + np.pi / 3), G),
        ]
        for cx, lab, ex, ey, col in specs:
            ax.plot([cx - 1.15, cx + 1.15], [2.85, 2.85], color=L, lw=1.0)
            ax.plot([cx, cx], [1.7, 4.0], color=L, lw=1.0)
            ax.plot(cx + 0.92 * ex, 2.85 + 0.92 * ey, color=col, lw=2.1)
            _txt(ax, cx, 0.88, lab, col, fs=8.2, ha='center')
        return 'Tip trajectory of E in the transverse xy-plane for three phase differences'

    if key == 'malus_curve':
        _style_plot(ax, 'analyser angle  theta  (deg)', 'transmitted  I / I0')
        th = np.linspace(0, 180, 240)
        r = np.deg2rad(th)
        ax.plot(th, np.cos(r) ** 2, color=T, lw=2.2, label='single analyser: cos^2(theta)')
        ax.plot(th, 0.25 * np.sin(2 * r) ** 2, color=R, lw=1.9, ls='--', label='crossed + middle sheet at theta')
        ax.set_xlim(0, 180)
        ax.set_ylim(0, 1.15)
        ax.set_xticks([0, 45, 90, 135, 180])
        ax.legend(loc='upper right', frameon=True, fontsize=7.3)
        return 'Malus law cos^2(theta) vs inserting a third polariser between crossed sheets'

    # =========================================================================
    # JEE-07: Poynting theorem & instant equipartition
    # =========================================================================
    if key == 'poynting_box':
        _clean_canvas(ax)
        ax.add_patch(Rectangle((2.5, 1.35), 4.2, 2.4, fc=P, ec=I, lw=1.8))
        _txt(ax, 4.6, 2.55, 'stored u = uE + uB\nwork:  J_f . E', I, fs=8.6, ha='center')
        for y0 in (1.95, 3.15):
            _arr(ax, (1.1, y0), (2.4, y0), T, lw=1.8)
            _arr(ax, (6.8, y0), (8.2, y0), R, lw=1.8)
        _txt(ax, 1.75, 4.22, 'S_in', T, fs=8.8, ha='center')
        _txt(ax, 7.5, 4.22, 'S_out', R, fs=8.8, ha='center')
        _txt(ax, 4.8, 0.68, '-du/dt = div S + J_f . E  (energy ledger)', I, fs=8.3, ha='center')
        return 'Poynting balance: field energy loss equals outward Poynting flux plus Ohmic work'

    if key == 'energy_cycle':
        _style_plot(ax, 'phase  kz - wt  (rad)', 'u / u_max')
        p = np.linspace(0, 2 * np.pi, 300)
        s2 = np.sin(p) ** 2
        ax.plot(p, s2, color=T, lw=2.2, label='total  u = eps E^2')
        ax.plot(p, 0.5 * s2, color=R, lw=1.8, ls='--', label='uE = uB = u / 2')
        ax.axhline(0.5, color=G, lw=1.3, ls=':', label='cycle mean  <u> = u_max / 2')
        ax.set_xlim(0, 2 * np.pi)
        ax.set_ylim(0, 1.32)
        ax.set_xticks([0, np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi])
        ax.set_xticklabels(['0', 'pi/2', 'pi', '3pi/2', '2pi'])
        ax.legend(loc='upper right', frameon=True, fontsize=7.2)
        return 'Travelling wave: uE and uB peak and vanish together, never trading back and forth'

    # =========================================================================
    # JEE-08: Peak/RMS & inverse-square spreading
    # =========================================================================
    if key == 'inverse_square':
        _style_plot(ax, 'distance ratio  r / r0', 'relative size')
        r = np.linspace(1.0, 5.0, 240)
        ax.plot(r, 1.0 / r, color=T, lw=2.2, label='field amplitude  E0 ~ 1/r')
        ax.plot(r, 1.0 / (r ** 2), color=R, lw=2.2, label='intensity  I ~ 1/r^2')
        ax.set_xlim(1, 5)
        ax.set_ylim(0, 1.12)
        ax.legend(loc='upper right', frameon=True, fontsize=7.8)
        return 'Isotropic far field: doubling r halves E0 and B0, while intensity quarters'

    if key == 'peak_rms_bars':
        _style_plot(ax, '', 'ratio to  E_rms^2 / Z')
        xs = np.array([0, 1, 2, 3])
        vals = [1.0, 1.0, 0.5, 2.0]
        cols = [T, T, G, R]
        ax.bar(xs, vals, width=0.52, color=cols, zorder=3)
        ax.set_xlim(-0.6, 3.6)
        ax.set_ylim(0, 2.45)
        ax.set_xticks(xs)
        ax.set_xticklabels(['E0^2/(2Z)', 'E_rms^2/Z', '<uE> v', 'wrong E0^2/Z'], fontsize=7.6)
        _txt(ax, 3.0, 2.16, '2x error!', R, fs=8.0, ha='center')
        return 'Peak vs RMS bookkeeping: omit the 1/2 only when squaring E_rms, never E0'

    # =========================================================================
    # JEE-09: Momentum & oblique radiation pressure
    # =========================================================================
    if key == 'oblique_sail':
        _clean_canvas(ax)
        ax.plot([4.6, 4.6], [0.65, 4.55], color=I, lw=3.0)
        ax.plot([1.2, 4.6], [2.6, 2.6], color=I, lw=1.0, ls=':')
        _arr(ax, (1.5, 4.15), (4.52, 2.64), T, lw=2.0)
        _arr(ax, (4.52, 2.56), (1.5, 1.05), R, lw=2.0)
        _arr(ax, (4.7, 2.6), (7.0, 2.6), G, lw=2.2, ms=14)
        _arr(ax, (4.95, 2.2), (4.95, 0.95), R, lw=1.7)
        _txt(ax, 2.2, 4.25, 'incident p_in', T, fs=8.3)
        _txt(ax, 1.8, 0.72, 'specular R p_out', R, fs=8.3)
        _txt(ax, 7.18, 2.6, 'F_n ~ (1+R)cos^2(theta)', G, fs=8.3)
        _txt(ax, 5.2, 1.45, 'F_t ~ (1-R)sin(theta)cos(theta)', R, fs=8.0)
        _txt(ax, 3.25, 2.92, 'theta', I, fs=8.2)
        return 'Two cosines on a flat sail: area projection cos(theta) times normal transfer'

    if key == 'pressure_angle':
        _style_plot(ax, 'incidence angle  theta  (deg)', 'stress / (I / c)')
        th = np.linspace(0, 90, 220)
        r = np.deg2rad(th)
        ax.plot(th, 2.0 * np.cos(r) ** 2, color=T, lw=2.2, label='mirror P_n = 2 cos^2(theta)')
        ax.plot(th, np.cos(r) ** 2, color=G, lw=2.0, label='black P_n = cos^2(theta)')
        ax.plot(th, np.sin(r) * np.cos(r), color=R, lw=1.8, ls='--', label='black shear  sin(theta)cos(theta)')
        ax.set_xlim(0, 90)
        ax.set_ylim(0, 2.25)
        ax.set_xticks([0, 30, 45, 60, 90])
        ax.legend(loc='upper right', frameon=True, fontsize=7.2)
        return 'Normal pressure and tangential shear vs incidence angle theta from normal'

    # =========================================================================
    # JEE-10: Electromagnetic spectrum & photon scale
    # =========================================================================
    if key == 'spectrum_ladder':
        _clean_canvas(ax)
        bands = [
            ('Radio', 0.4, 1.75, '#dceee9'),
            ('Micro', 1.75, 3.05, '#eff6d8'),
            ('IR', 3.05, 4.35, '#fbe8d4'),
            ('Vis', 4.35, 5.25, '#e2f0fb'),
            ('UV', 5.25, 6.55, '#ebe2f8'),
            ('X-ray', 6.55, 8.05, '#f9e2e2'),
            ('Gam.', 8.05, 9.55, '#f3d9dc'),
        ]
        for nm, x0, x1, fc in bands:
            ax.add_patch(Rectangle((x0, 2.05), x1 - x0, 1.35, fc=fc, ec=I, lw=1.0))
            _txt(ax, 0.5 * (x0 + x1), 2.72, nm, I, fs=7.8, ha='center')
        cuts = [(1.75, '1 m'), (3.05, '1 mm'), (4.35, '700 nm'),
                (5.25, '400 nm'), (6.55, '10 nm'), (8.05, '0.01 nm')]
        for xx, lb in cuts:
            ax.plot([xx, xx], [1.75, 2.05], color=I, lw=1.0)
            _txt(ax, xx, 1.42, lb, T, fs=7.2, ha='center')
        _arr(ax, (0.6, 4.15), (9.35, 4.15), R, lw=1.7)
        _txt(ax, 5.0, 4.55, 'increasing f and E_gamma = h f   (all travel at c in vacuum)', R, fs=8.2, ha='center')
        _txt(ax, 7.6, 0.68, 'X and gamma overlap by source mechanism', I, fs=7.9, ha='center')
        return 'Adopted classroom wavelength cutoffs along the continuous vacuum EM spectrum'

    if key == 'photon_energy_line':
        _style_plot(ax, 'log10(lambda_0 / m)', 'log10(E_gamma / eV)')
        lg_lam = np.linspace(-12, 1, 100)
        lg_e = np.log10(1.24e-6) - lg_lam
        ax.plot(lg_lam, lg_e, color=T, lw=2.2)
        pts = [(-9.92, '100 keV\nX / gamma'), (-6.70, '6.2 eV\nUV'), (-6.30, '2.5 eV\nVis')]
        for lx, lb in pts:
            ey = np.log10(1.24e-6) - lx
            ax.plot(lx, ey, 'o', color=R, ms=5)
        _txt(ax, -9.5, 5.2, '100 keV (0.0124 nm)', R, fs=7.8)
        _txt(ax, -5.8, 1.5, 'E_gamma = 1240 eV nm / lambda_0', I, fs=8.0)
        ax.set_xlim(-12.2, 1.2)
        ax.set_ylim(-7.5, 6.8)
        return 'Exact inverse scaling E_gamma = hc / lambda_0 across thirteen wavelength decades'

    # =========================================================================
    # JEE-11: LC oscillator & Hertzian dipole pattern
    # =========================================================================
    if key == 'dipole_lobes':
        _clean_canvas(ax)
        cx, cy = 4.6, 2.55
        _arr(ax, (cx, 0.65), (cx, 4.55), I, lw=1.8)
        _txt(ax, cx + 0.2, 4.5, 'dipole axis p(t)', I, fs=8.2)
        th = np.linspace(0, 2 * np.pi, 360)
        rr = 2.45 * (np.sin(th) ** 2)
        ax.plot(cx + rr * np.sin(th), cy + rr * np.cos(th), color=T, lw=2.2)
        _txt(ax, 7.35, 2.55, 'max broadside\ntheta = 90 deg', T, fs=8.1)
        _txt(ax, 1.35, 4.05, 'zero on axis\ntheta = 0, 180', R, fs=8.1)
        _txt(ax, 5.0, 0.42, 'I(r,theta) ~ sin^2(theta) / r^2', I, fs=8.0, ha='center')
        return 'Hertzian electric dipole pattern: maximum broadside, zero along the oscillation axis'

    if key == 'omega4_scaling':
        _style_plot(ax, 'scaled distance  k r', 'log10 |E_field|  (arb.)')
        kr = np.linspace(0.25, 6.0, 260)
        ax.plot(kr, np.log10(1.0 / kr ** 3), color=G, lw=2.0, ls='--', label='static / near  ~ 1/(kr)^3')
        ax.plot(kr, np.log10(1.0 / kr), color=T, lw=2.2, label='radiation zone  ~ 1/(kr)')
        ax.axvline(1.0, color=R, lw=1.1, ls=':')
        ax.set_xlim(0.25, 6.0)
        ax.set_ylim(-2.6, 2.1)
        _txt(ax, 1.15, 1.45, 'crossover kr ~ 1', R, fs=7.9)
        ax.legend(loc='lower left', frameon=True, fontsize=7.4)
        return 'Near-field terms die as 1/r^3; only the 1/r acceleration field escapes to infinity'

    # =========================================================================
    # JEE-12: Master triage & benchmark scales
    # =========================================================================
    if key == 'triage_map':
        _clean_canvas(ax)
        boxes = [
            (0.4, 3.3, 2.8, 1.25, 'Capacitor / gap?\nId = dPhi_E/dt * eps', P, T),
            (3.6, 3.3, 2.8, 1.25, 'Field formula?\nk . E = 0, B = k x E/v', P, T),
            (6.8, 3.3, 2.8, 1.25, 'Power / RMS?\nI = E_rms^2 / Z', P, T),
            (0.4, 0.9, 2.8, 1.25, 'Flat sail force?\nP_hit = I A cos(theta)', '#fdf4df', G),
            (3.6, 0.9, 2.8, 1.25, 'Sphere / mirror?\nintegrate vector dF', '#fdf4df', G),
            (6.8, 0.9, 2.8, 1.25, 'Interface / band?\nf fixed; lambda_0 = c/f', '#fbeaea', R),
        ]
        for x0, y0, w, h, s, fc, ec in boxes:
            ax.add_patch(Rectangle((x0, y0), w, h, fc=fc, ec=ec, lw=1.4))
            _txt(ax, x0 + w / 2, y0 + h / 2, s, I, fs=5.7, ha='center')
        return 'Six-way JEE triage: identify the model before writing any equation'

    if key == 'unit_scales':
        _style_plot(ax, '', 'log10(value in SI units)')
        xs = np.array([0, 1, 2, 3])
        vals = [np.log10(377), np.log10(1360), np.log10(4.53e-6), np.log10(3.33e-9)]
        cols = [T, G, R, I]
        ax.bar(xs, vals, width=0.5, color=cols, zorder=3)
        ax.axhline(0, color=I, lw=0.8)
        ax.set_xlim(-0.6, 3.6)
        ax.set_ylim(-10.5, 4.8)
        ax.set_xticks(xs)
        ax.set_xticklabels(['Z0 (Ohm)', 'Solar I', 'Solar I/c (Pa)', '1 W/c (N)'], fontsize=7.5)
        return 'Order-of-magnitude anchors: Z0 ~ 377 Ohm, sunlight ~ 1.4 kW/m^2, 1 W/c ~ 3.3 nN'

    # =========================================================================
    # Olympiad-01: Capacitor Poynting inflow & coaxial cable
    # =========================================================================
    if key == 'cap_poynting_vectors':
        _clean_canvas(ax)
        ax.add_patch(Circle((4.5, 2.6), 1.65, fc=P, ec=I, lw=1.8))
        for ang in np.linspace(0, 2 * np.pi, 9)[:-1]:
            r_out, r_in = 2.45, 1.75
            _arr(ax, (4.5 + r_out * np.cos(ang), 2.6 + r_out * np.sin(ang)),
                 (4.5 + r_in * np.cos(ang), 2.6 + r_in * np.sin(ang)), R, lw=1.7)
        th = np.linspace(0, 1.65 * np.pi, 120)
        ax.plot(4.5 + 1.05 * np.cos(th), 2.6 + 1.05 * np.sin(th), color=T, lw=1.6, ls='--')
        _txt(ax, 4.5, 2.6, 'E out (+z)\nB_phi CCW', I, fs=8.1, ha='center')
        _txt(ax, 7.45, 3.85, 'S = E x H points\nRADIALLY INWARD', R, fs=8.3)
        _txt(ax, 7.45, 1.35, 'flux * (2 pi a d) = V Ic', T, fs=8.3)
        return 'Charging capacitor top view: field energy enters radially through the cylindrical rim'

    if key == 'coax_field_power':
        _style_plot(ax, 'radial position  r / a', 'normalised profile')
        r = np.linspace(1.0, 4.0, 220)
        ax.plot(r, 1.0 / r, color=T, lw=2.1, label='E(r) and B(r)  ~ 1/r')
        ax.plot(r, 1.0 / (r ** 2), color=R, lw=2.1, label='Poynting flux  S_z ~ 1/r^2')
        ax.set_xlim(1, 4)
        ax.set_ylim(0, 1.15)
        ax.legend(loc='upper right', frameon=True, fontsize=7.6)
        return 'Coaxial TEM line: fields fall as 1/r between conductors a and b, carrying total V I'

    # =========================================================================
    # Olympiad-02: Curved surfaces & stellar beta ratio
    # =========================================================================
    if key == 'sphere_annulus':
        _clean_canvas(ax)
        cx, cy, R0 = 4.65, 2.55, 1.55
        ax.add_patch(Circle((cx, cy), R0, fc=P, ec=I, lw=1.8))
        th = np.deg2rad(42)
        px, py = cx - R0 * np.cos(th), cy + R0 * np.sin(th)
        _arr(ax, (0.55, py), (px, py), T, lw=1.9)
        _arr(ax, (px, py), (px - 1.5 * np.cos(2 * th), py + 1.5 * np.sin(2 * th)), R, lw=1.9)
        ax.plot([cx, px - 0.9 * np.cos(th)], [cy, py + 0.9 * np.sin(th)], color=I, lw=1.1, ls=':')
        _txt(ax, 0.58, py - 0.44, 'incident ray', T, fs=7.5)
        _txt(ax, 0.55, 4.30, 'reflected (2 theta)', R, fs=7.5)
        _txt(ax, 6.45, 3.65, 'black: int sin cos = 1/2', I, fs=7.5)
        _txt(ax, 6.45, 2.65, 'mirror: 2 int sin cos^3 = 1/2', T, fs=7.5)
        _txt(ax, 6.45, 1.65, 'BOTH: F = I pi a^2 / c', R, fs=7.7)
        return 'Illuminated sphere zone: local specular scatter equals full black-sphere drag'

    if key == 'stellar_beta':
        _style_plot(ax, 'grain radius  a  (um)', 'F_rad / F_grav  =  beta')
        a = np.linspace(0.25, 3.0, 240)
        ax.plot(a, 0.6 / a, color=T, lw=2.2, label='solar-type grain  beta ~ 1/a')
        ax.axhline(1.0, color=R, lw=1.2, ls='--', label='blow-out threshold  beta = 1')
        ax.axvline(0.6, color=G, lw=1.1, ls=':')
        ax.set_xlim(0.25, 3.0)
        ax.set_ylim(0, 2.65)
        _txt(ax, 0.72, 1.45, 'a < a_crit:\nblown out', R, fs=7.3)
        ax.legend(loc='upper right', frameon=True, fontsize=7.5)
        return 'Radiation-to-gravity ratio beta cancels distance r^2 and scales inversely with radius a'

    # =========================================================================
    # Olympiad-03: Wave impedance & interface matching
    # =========================================================================
    if key == 'interface_jump':
        _clean_canvas(ax)
        ax.add_patch(Rectangle((5.0, 0.65), 4.4, 3.85, fc='#e7f3f1', ec=T, lw=1.2))
        ax.plot([5.0, 5.0], [0.55, 4.65], color=I, lw=2.0)
        _arr(ax, (1.2, 3.55), (4.7, 3.55), T, lw=2.0)
        _arr(ax, (4.7, 1.65), (1.2, 1.65), R, lw=2.0)
        _arr(ax, (5.3, 2.65), (8.8, 2.65), G, lw=2.1)
        _txt(ax, 2.7, 4.05, 'Ei,  Hi = +Ei / Z1', T, fs=8.3, ha='center')
        _txt(ax, 2.55, 1.05, 'Er, Hr = -Er/Z1 (flip!)', R, fs=7.0, ha='center')
        _txt(ax, 7.1, 3.35, 'Et = Ei + Er', G, fs=8.3, ha='center')
        _txt(ax, 7.1, 1.85, 'Ht = +Et / Z2', I, fs=8.3, ha='center')
        return 'Normal-incidence matching: tangential E and H stay continuous; reflected H flips sign'

    if key == 'rt_vs_ratio':
        _style_plot(ax, 'impedance ratio  Z2 / Z1', 'power fraction  R, T')
        z = np.linspace(0.2, 5.0, 300)
        r_p = ((z - 1.0) / (z + 1.0)) ** 2
        t_p = 4.0 * z / ((z + 1.0) ** 2)
        ax.plot(z, r_p, color=R, lw=2.1, label='reflected power  R')
        ax.plot(z, t_p, color=T, lw=2.1, label='transmitted power  T = 1 - R')
        ax.axvline(1.0, color=G, lw=1.1, ls=':')
        ax.set_xlim(0.2, 5.0)
        ax.set_ylim(0, 1.15)
        _txt(ax, 1.12, 0.16, 'Z2 = Z1 => R = 0', G, fs=7.5)
        ax.legend(loc='center right', frameon=True, fontsize=7.5)
        return 'Power reflection R and transmission T vs impedance ratio Z2/Z1 (always R + T = 1)'

    # =========================================================================
    # Olympiad-04: Standing wave at mirror & isotropic u/3
    # =========================================================================
    if key == 'standing_nodes':
        _style_plot(ax, 'distance from mirror  z / lambda', 'envelope / max')
        z = np.linspace(-1.25, 0.0, 300)
        ax.plot(z, np.abs(np.sin(2 * np.pi * z)), color=T, lw=2.2, label='|E| env  ~ |sin(kz)|')
        ax.plot(z, np.abs(np.cos(2 * np.pi * z)), color=R, lw=2.0, ls='--', label='c|B| env  ~ |cos(kz)|')
        ax.axvline(0.0, color=I, lw=2.5)
        ax.set_xlim(-1.25, 0.06)
        ax.set_ylim(0, 1.28)
        ax.legend(loc='upper left', frameon=True, fontsize=7.5)
        return 'Perfect mirror at z = 0 forces an E node and a B antinode (magnetic stress 2 I / c)'

    if key == 'isotropic_hemisphere':
        _style_plot(ax, 'angle  theta  (deg)', 'cos^2 * sin')
        th = np.linspace(0, 90, 240)
        r = np.deg2rad(th)
        y = (np.cos(r) ** 2) * np.sin(r)
        ax.plot(th, y, color=T, lw=2.2)
        ax.fill_between(th, 0, y, color='#dff0ec', zorder=1)
        ax.set_xlim(0, 90)
        ax.set_ylim(0, 0.46)
        ax.set_xticks([0, 30, 45, 60, 90])
        _txt(ax, 42, 0.36, 'integral 0..pi/2 = 1/3  ->  P = u / 3', I, fs=8.1)
        return 'Angular weight cos^2(theta) sin(theta) peaks at 35.3 deg and integrates to 1/3'

    # =========================================================================
    # Olympiad-05: Skin depth & plasma dispersion
    # =========================================================================
    if key == 'skin_decay':
        _style_plot(ax, 'depth into conductor  z / delta', 'E(z, 0) / E0')
        z = np.linspace(0, 4.5, 300)
        ax.plot(z, np.exp(-z) * np.cos(z), color=T, lw=2.2, label='instantaneous E')
        ax.plot(z, np.exp(-z), color=R, lw=1.7, ls='--', label='envelope  exp(-z / delta)')
        ax.plot(z, -np.exp(-z), color=R, lw=1.2, ls=':')
        ax.set_xlim(0, 4.5)
        ax.set_ylim(-1.15, 1.25)
        ax.legend(loc='upper right', frameon=True, fontsize=7.5)
        return 'Good conductor (k = (1+i)/delta): wave decays by 1/e in one skin depth delta'

    if key == 'plasma_dispersion':
        _style_plot(ax, 'wavenumber  c k / w_p', 'frequency  w / w_p')
        ck = np.linspace(0, 3.0, 240)
        ax.plot(ck, np.sqrt(1.0 + ck ** 2), color=T, lw=2.3, label='plasma  w = sqrt(w_p^2 + c^2 k^2)')
        ax.plot(ck, ck, color=R, lw=1.7, ls='--', label='vacuum light line  w = c k')
        ax.axhline(1.0, color=G, lw=1.1, ls=':')
        ax.set_xlim(0, 3.0)
        ax.set_ylim(0, 3.4)
        _txt(ax, 1.55, 0.55, 'evanescent below w_p', G, fs=7.9)
        ax.legend(loc='upper left', frameon=True, fontsize=7.3)
        return 'Collisionless plasma dispersion: v_p > c above cutoff w_p while group speed v_g = c^2/v_p < c'

    # =========================================================================
    # Olympiad-06: Moving mirror Doppler & parallel-plate waveguide
    # =========================================================================
    if key == 'moving_mirror':
        _clean_canvas(ax)
        ax.add_patch(Rectangle((6.3, 0.85), 0.35, 3.5, fc='#cfe5e1', ec=I, lw=1.8))
        _arr(ax, (6.2, 4.15), (4.85, 4.15), G, lw=2.0)
        _txt(ax, 5.5, 4.62, 'mirror speed u', G, fs=8.3, ha='center')
        z_in = np.linspace(0.7, 6.2, 240)
        z_rf = np.linspace(0.7, 6.2, 340)
        ax.plot(z_in, 3.05 + 0.42 * np.sin(2 * np.pi * z_in / 1.9), color=T, lw=1.9)
        ax.plot(z_rf, 1.65 + 0.48 * np.sin(2 * np.pi * z_rf / 0.95), color=R, lw=1.9)
        _txt(ax, 2.3, 3.72, 'incident f', T, fs=8.2)
        _txt(ax, 2.3, 0.92, "reflected f' = f (1 + beta)/(1 - beta)", R, fs=8.2)
        return 'Advancing mirror compresses reflected crests twice: double Doppler boost (1+beta)/(1-beta)'

    if key == 'waveguide_modes':
        _style_plot(ax, 'frequency ratio  w / w_c', 'speed / c')
        w = np.linspace(1.06, 4.0, 260)
        vg = np.sqrt(1.0 - 1.0 / (w ** 2))
        vp = 1.0 / vg
        ax.plot(w, vp, color=R, lw=2.1, label='phase speed  v_p / c > 1')
        ax.plot(w, vg, color=T, lw=2.1, label='group / energy speed  v_g / c < 1')
        ax.axhline(1.0, color=I, lw=1.0, ls=':')
        ax.set_xlim(1.0, 4.0)
        ax.set_ylim(0, 3.2)
        ax.legend(loc='upper right', frameon=True, fontsize=7.5)
        return 'Guided TE_1 mode above cutoff w_c = pi c / b: exact product law v_p v_g = c^2'

    raise KeyError(f'Unknown diagram key: {key!r}')
