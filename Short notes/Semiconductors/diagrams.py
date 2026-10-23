"""36 pure-NumPy analytic physics & electronic-device diagrams for Semiconductors (18 sheets x 2 panels)."""
import numpy as np
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Circle, Rectangle, Polygon

I = '#153149'
T = '#087d7d'
R = '#9b3a3a'
G = '#2d7a4f'
W = '#f7e6b7'
S = '#edf5f4'
BD = '#bbd9d4'
GR = '#d8e6e4'

CAPTIONS = {
    'resistivity_axis': '30-order logarithmic resistivity axis from copper to fused quartz',
    'rho_vs_temp': 'Opposite temperature laws: scattering in metals vs pair creation in Si',
    'band_comparison': 'Allowed valence/conduction bands and forbidden gap across solids',
    'intrinsic_vs_temp': 'Exponential thermal growth of intrinsic carrier density ni(T)',
    'doped_band_levels': 'Shallow donor Ed and acceptor Ea levels inside the forbidden gap',
    'drift_diffusion_currents': 'Drift vs concentration-gradient diffusion currents and Einstein relation',
    'pn_depletion_layout': 'Depletion space-charge dipole and opposing drift-diffusion balance',
    'pn_charge_field_pot': 'Aligned space charge rho(x), electric field E(x), and barrier hill V(x)',
    'diode_iv_full': 'Full junction diode I-V characteristic from Zener breakdown to knee',
    'decade_ladder_semilog': 'Room-temperature semilog ladder: 59.5 mV per decade of forward current',
    'rectifier_waveforms': 'Half-wave, full-wave, and capacitor-filtered sawtooth ripple waveforms',
    'bridge_rectifier_circuit': 'Four-diode full-wave bridge rectifier path and double-drop arithmetic',
    'zener_regulator': 'Zener shunt voltage regulator and two-sided worst-case resistor squeeze',
    'solar_photodiode_quadrants': 'Illuminated p-n junction across Quadrant III (sensor) and IV (PV cell)',
    'npn_current_flow': 'Asymmetric doping and thin-base electron transport in an NPN transistor',
    'bjt_output_loadline': 'Collector family IC(VCE), DC load line, active Q-point, and saturation wall',
    'ce_amplifier_transfer': 'Common-emitter voltage transfer curve Vout(Vin) and 180-deg phase inversion',
    'bjt_switch_driver': 'Hard-saturated NPN lamp/relay switch with 2x base-current overdrive',
    'diode_bjt_gates': 'Diode OR/AND hardware realisations and six standard Boolean gate outputs',
    'logic_timing_waveforms': 'Digital pulse-train timing trace through NAND and XOR gates',
    'nand_universal_map': 'Universal gate synthesis table: exact minimum NAND and NOR gate counts',
    'half_adder_circuit': 'Half adder combinational circuit generating Sum (XOR) and Carry (AND)',
    'led_bandgap_spectrum': 'Direct-gap photon wavelength lam = 1240 / Eg across LED materials',
    'multi_diode_solver': 'Systematic open-circuit ranking protocol for multi-diode networks',
    'bohr_donor_scaling': 'Dielectric-screened effective-mass Bohr orbit of phosphorus in silicon',
    'carrier_freezeout_intrinsic': 'Three temperature regimes of doped silicon: freeze-out, extrinsic, intrinsic',
    'boltzmann_hill_injection': 'Bias modulation of conduction-band barrier hill q(V0 - V) across a junction',
    'varactor_capacitance': 'Depletion width W(VR), varactor Cj(VR), and linear 1/Cj^2 extraction',
    'hall_slab_geometry': 'Hall effect slab geometry: Lorentz deflection names carrier sign and density',
    'bandgap_reference_ptat': 'Cancelling CTAT (-2 mV/K) and PTAT (+2 mV/K) slopes in a 1.22 V reference',
    'shockley_queisser_curve': 'Single-junction Shockley-Queisser limit (~33.7% near Eg = 1.34 eV)',
    'shaded_panel_bypass': 'Series PV string current collapse under shading vs bypass-diode step recovery',
    'shot_vs_thermal_noise': 'Quantum shot noise floor sqrt(2eI) vs Johnson-Nyquist resistor noise',
    'led_loadline_stability': 'Why LEDs need a series resistor: linear load line vs exponential runaway',
    'quantum_tunnelling_wall': 'WKB gate-oxide tunnelling probability and high-k HfO2 scaling rescue',
    'cmos_power_scaling': 'Dynamic CV^2f vs subthreshold leakage trade-off across CMOS supply scaling',
}


def _clean_plot(ax, xlabel='', ylabel=''):
    ax.set_facecolor('white')
    for sp in ('top', 'right'):
        ax.spines[sp].set_visible(False)
    for sp in ('left', 'bottom'):
        ax.spines[sp].set_color(I)
        ax.spines[sp].set_linewidth(1.1)
    ax.tick_params(colors=I, labelsize=7.4, length=3)
    if xlabel:
        ax.set_xlabel(xlabel, color=I, fontsize=8.0, labelpad=3)
    if ylabel:
        ax.set_ylabel(ylabel, color=I, fontsize=8.0, labelpad=3)
    ax.grid(True, color=GR, lw=0.6, ls='--')


def _schem(ax, xlim=(0, 10), ylim=(0, 5.4)):
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.axis('off')


def _arr(ax, p0, p1, col=I, lw=1.4, style='->', ms=10, ls='-'):
    ax.add_patch(FancyArrowPatch(
        p0, p1, arrowstyle=style, mutation_scale=ms,
        lw=lw, linestyle=ls, color=col, shrinkA=0, shrinkB=0,
    ))


def _txt(ax, x, y, s, col=I, fs=7.5, ha='left', va='center'):
    ax.text(x, y, s, color=col, fontsize=fs, ha=ha, va=va)


def _box(ax, x, y, w, h, fc=S, ec=T, lw=1.2, r=0.12):
    ax.add_patch(FancyBboxPatch(
        (x, y), w, h, boxstyle=f'round,pad=0.02,rounding_size={r}',
        facecolor=fc, edgecolor=ec, lw=lw,
    ))


def figure(ax, key):
    # ------------------------------------------------------------------ JEE 01
    if key == 'resistivity_axis':
        _schem(ax, (0, 10), (0, 5.4))
        def xm(lr):
            return 0.6 + (lr + 9.0) / 28.0 * 8.8
        ax.add_patch(Rectangle((xm(-9), 2.35), xm(-4) - xm(-9), 0.75, fc='#d9eee9', ec=T, lw=1.1))
        ax.add_patch(Rectangle((xm(-4), 2.35), xm(4) - xm(-4), 0.75, fc=W, ec=R, lw=1.1))
        ax.add_patch(Rectangle((xm(4), 2.35), xm(19) - xm(4), 0.75, fc=S, ec=I, lw=1.1))
        _txt(ax, 0.5 * (xm(-9) + xm(-4)), 2.72, 'Metals', T, fs=7.6, ha='center')
        _txt(ax, 0.5 * (xm(-4) + xm(4)), 2.72, 'Semiconductors', R, fs=7.6, ha='center')
        _txt(ax, 0.5 * (xm(4) + xm(19)), 2.72, 'Insulators', I, fs=7.6, ha='center')
        _arr(ax, (0.45, 2.0), (9.65, 2.0), I, lw=1.25)
        for lr, lbl in [(-8, '10^-8'), (-4, '10^-4'), (0, '1'), (4, '10^4'), (10, '10^10'), (17, '10^17')]:
            xx = xm(lr)
            ax.plot([xx, xx], [1.88, 2.12], color=I, lw=1.1)
            _txt(ax, xx, 1.52, lbl, I, fs=7.1, ha='center')
        _txt(ax, 5.0, 0.85, 'Resistivity rho (ohm.m) spanning 30 orders at 300 K', I, fs=7.4, ha='center')
        pins = [(-7.77, 'Cu 1.7e-8', 4.35, T), (-1.34, 'Doped Si', 3.7, R),
                (3.36, 'Pure Si 2300', 4.45, R), (12.0, 'Glass 10^12', 3.75, I), (17.5, 'Quartz 10^18', 4.45, I)]
        for lr, lb, yt, col in pins:
            xx = xm(lr)
            ax.plot([xx, xx], [3.12, yt - 0.28], color=col, lw=1.0, ls=':')
            _txt(ax, xx, yt, lb, col, fs=7.0, ha='center')

    elif key == 'rho_vs_temp':
        _clean_plot(ax, 'Temperature T (K)', 'rho(T) / rho(300 K)')
        T_k = np.linspace(240, 460, 300)
        rho_cu = 1.0 + 0.0039 * (T_k - 300.0)
        rho_si = (300.0 / T_k) ** 1.5 * np.exp(4.2 * (300.0 / T_k - 1.0))
        rho_ntc = np.exp(6.8 * (300.0 / T_k - 1.0))
        ax.plot(T_k, rho_cu, color=I, lw=1.8, label='Metal (alpha > 0)')
        ax.plot(T_k, np.clip(rho_si, 0, 3.6), color=T, lw=1.9, label='Intrinsic Si (alpha < 0)')
        ax.plot(T_k, np.clip(rho_ntc, 0, 3.6), color=R, lw=1.7, ls='--', label='NTC thermistor')
        ax.set_xlim(240, 465)
        ax.set_ylim(0.0, 4.1)
        ax.legend(frameon=False, fontsize=7.0, loc='upper right')

    # ------------------------------------------------------------------ JEE 02
    elif key == 'band_comparison':
        _schem(ax, (0, 10), (0, 5.4))
        cols = [(1.7, 'Metal', 0.0), (5.0, 'Semiconductor', 1.1), (8.3, 'Insulator', 1.8)]
        for cx, name, gap in cols:
            _txt(ax, cx, 5.04, name, I, fs=7.8, ha='center')
            if gap == 0.0:
                ax.add_patch(Rectangle((cx - 1.05, 1.35), 2.1, 1.45, fc='#cfe8e5', ec=T, lw=1.2))
                ax.add_patch(Rectangle((cx - 1.05, 2.35), 2.1, 1.45, fc=S, ec=I, lw=1.1, fill=False))
                _txt(ax, cx, 0.78, 'Overlap (Eg = 0)', T, fs=7.0, ha='center')
            else:
                ax.add_patch(Rectangle((cx - 1.05, 1.15), 2.1, 0.85, fc='#cfe8e5', ec=T, lw=1.15))
                ax.add_patch(Rectangle((cx - 1.05, 1.15 + 0.85 + gap), 2.1, 0.8, fc=W, ec=R, lw=1.15))
                _txt(ax, cx, 1.57, 'VB (full)', I, fs=6.9, ha='center')
                _txt(ax, cx, 1.15 + 0.85 + gap + 0.4, 'CB', R, fs=7.0, ha='center')
                lbl = 'Eg ~ 1.1 eV (Si)' if gap < 1.6 else 'Eg ~ 5.5 eV (C)'
                _txt(ax, cx, 0.65, lbl, R if gap < 1.6 else I, fs=7.0, ha='center')
                _txt(ax, cx, 2.0 + 0.5 * gap, 'Gap', I, fs=6.9, ha='center')

    elif key == 'intrinsic_vs_temp':
        _clean_plot(ax, 'Temperature T (K)', 'log10 [ ni / ni(300K) ]')
        Tk = np.linspace(260, 600, 300)
        kB = 8.617333e-5
        si = np.log10((Tk / 300.0) ** 1.5 * np.exp((1.12 / (2 * kB)) * (1 / 300.0 - 1 / Tk)))
        ge = np.log10((Tk / 300.0) ** 1.5 * np.exp((0.66 / (2 * kB)) * (1 / 300.0 - 1 / Tk)))
        ga = np.log10((Tk / 300.0) ** 1.5 * np.exp((1.42 / (2 * kB)) * (1 / 300.0 - 1 / Tk)))
        ax.plot(Tk, ge, color=R, lw=1.7, ls='--', label='Ge (0.66 eV)')
        ax.plot(Tk, si, color=T, lw=2.0, label='Si (1.12 eV)')
        ax.plot(Tk, ga, color=I, lw=1.7, ls=':', label='GaAs (1.42 eV)')
        ax.axhline(4.82, color=G, lw=0.95, ls=':')
        ax.set_xlim(260, 605)
        ax.set_ylim(-2.5, 6.2)
        ax.legend(frameon=False, fontsize=7.0, loc='lower right')
        _txt(ax, 355, 5.28, 'Si hits Nd=10^21 at ~560 K', G, fs=6.9, ha='center')

    # ------------------------------------------------------------------ JEE 03
    elif key == 'doped_band_levels':
        _schem(ax, (0, 10), (0, 5.4))
        for cx, ttl, lvl_y, lvl_lbl, col in [
            (2.5, 'n-type (Pentavalent P)', 3.42, 'Ed (45 meV below Ec)', R),
            (7.5, 'p-type (Trivalent B)', 1.98, 'Ea (45 meV above Ev)', T),
        ]:
            _txt(ax, cx, 4.92, ttl, I, fs=7.7, ha='center')
            ax.add_patch(Rectangle((cx - 1.85, 3.85), 3.7, 0.72, fc=W, ec=R, lw=1.15))
            ax.add_patch(Rectangle((cx - 1.85, 0.85), 3.7, 0.72, fc='#cfe8e5', ec=T, lw=1.15))
            ax.plot([cx - 1.65, cx + 1.65], [lvl_y, lvl_y], color=col, lw=1.3, ls='--')
            _txt(ax, cx, 4.21, 'Conduction Band Ec', R, fs=7.0, ha='center')
            _txt(ax, cx, 1.21, 'Valence Band Ev', T, fs=7.0, ha='center')
            _txt(ax, cx, 2.7, lvl_lbl, col, fs=7.0, ha='center')
        _txt(ax, 5.0, 0.35, 'Neutral crystal: n + Na- = p + Nd+  and  n.p = ni^2', I, fs=7.2, ha='center')

    elif key == 'drift_diffusion_currents':
        _schem(ax, (0, 10), (0, 5.4))
        _box(ax, 0.45, 2.95, 9.1, 1.95, fc=S, ec=T, lw=1.15)
        _txt(ax, 0.9, 4.45, 'DRIFT (E right ->):', I, fs=7.4)
        _arr(ax, (4.3, 4.45), (6.3, 4.45), R, lw=1.5)
        _txt(ax, 6.65, 4.45, 'h+ v_p -> J_p ->', R, fs=7.2)
        _arr(ax, (6.3, 3.55), (4.3, 3.55), T, lw=1.5)
        _txt(ax, 0.9, 3.55, 'e- moves <-, J_n ALSO ->', T, fs=7.2)
        _box(ax, 0.45, 0.55, 9.1, 1.95, fc='#fdf8ea', ec=R, lw=1.15)
        _txt(ax, 0.9, 2.02, 'DIFFUSION (dn/dx < 0 right):', I, fs=7.4)
        _txt(ax, 0.9, 1.15, 'Jn = +e Dn dn/dx   |   Jp = -e Dp dp/dx   |   D/mu = kT/e = 25.9 mV', R, fs=7.05)

    # ------------------------------------------------------------------ JEE 04
    elif key == 'pn_depletion_layout':
        _schem(ax, (0, 10), (0, 5.4))
        ax.add_patch(Rectangle((0.6, 1.35), 4.4, 2.8, fc='#eef6f5', ec=T, lw=1.2))
        ax.add_patch(Rectangle((5.0, 1.35), 4.4, 2.8, fc='#fdf4ea', ec=R, lw=1.2))
        ax.add_patch(Rectangle((3.5, 1.35), 3.0, 2.8, fc='white', ec=I, lw=1.1, ls='--'))
        _txt(ax, 2.0, 4.55, 'p-side (Na)', T, fs=7.8, ha='center')
        _txt(ax, 8.0, 4.55, 'n-side (Nd)', R, fs=7.8, ha='center')
        for yv in (1.95, 2.75, 3.55):
            for xv in (3.95, 4.6):
                _txt(ax, xv, yv, '-', T, fs=9.0, ha='center')
            for xv in (5.4, 6.05):
                _txt(ax, xv, yv, '+', R, fs=8.5, ha='center')
        _arr(ax, (6.25, 0.88), (3.75, 0.88), I, lw=1.5)
        _txt(ax, 5.0, 0.4, 'Built-in field E_bi: n -> p  (J_drift + J_diff = 0)', I, fs=7.2, ha='center')

    elif key == 'pn_charge_field_pot':
        _clean_plot(ax, 'Position x across depletion layer', 'Normalized profile')
        x = np.linspace(-2.0, 2.0, 400)
        rho = np.where((x >= -1.0) & (x < 0.0), -0.8, np.where((x >= 0.0) & (x <= 1.0), 0.8, 0.0))
        E = np.where(np.abs(x) <= 1.0, -(1.0 - np.abs(x)), 0.0)
        V = np.where(x < -1.0, 0.0, np.where(x > 1.0, 1.0,
            np.where(x < 0.0, 0.5 * (x + 1.0) ** 2, 1.0 - 0.5 * (1.0 - x) ** 2)))
        ax.plot(x, rho, color=T, lw=1.7, label='rho(x) / eN')
        ax.plot(x, E, color=R, lw=1.8, ls='--', label='E(x) / Emax (<0)')
        ax.plot(x, V, color=I, lw=1.9, label='V(x) / V0 (0 -> V0)')
        ax.set_xlim(-2.0, 2.0)
        ax.set_ylim(-1.25, 2.15)
        ax.legend(frameon=False, fontsize=6.9, loc='upper left')

    # ------------------------------------------------------------------ JEE 05
    elif key == 'diode_iv_full':
        _clean_plot(ax, 'Bias voltage V (V)', 'Diode current I (arb.)')
        vf = np.linspace(0, 0.82, 200)
        If = 0.03 * (np.exp(vf / 0.14) - 1.0)
        vr = np.linspace(-6.0, 0.0, 200)
        Ir = -0.18 - 8.5 * np.exp((-5.2 - vr) / 0.16) * (vr < -4.7)
        ax.plot(vf * 6.0, If, color=T, lw=2.0, label='Forward (x6 V zoom)')
        ax.plot(vr, np.clip(Ir, -10.0, 0.5), color=R, lw=1.9, label='Reverse & Zener Vz')
        ax.axhline(0, color=I, lw=0.7)
        ax.axvline(0, color=I, lw=0.7)
        ax.set_xlim(-6.2, 5.2)
        ax.set_ylim(-9.8, 10.5)
        ax.legend(frameon=False, fontsize=7.0, loc='upper left')
        _txt(ax, -2.5, -5.0, 'Vz breakdown\n(-I spikes!)', R, fs=7.0, ha='center')
        _txt(ax, 2.0, 6.2, 'Knee ~ 0.7 V (Si)\n0.3 V (Ge)', T, fs=7.0, ha='center')

    elif key == 'decade_ladder_semilog':
        _clean_plot(ax, 'Forward voltage V (V)', 'log10 [ I (mA) ]')
        v = np.linspace(0.48, 0.78, 200)
        lgI = (v - 0.60) / 0.0595
        ax.plot(v, lgI, color=T, lw=2.0, label='Ideal eta=1 (59.5 mV/dec)')
        ax.plot(v, (v - 0.60) / 0.119, color=R, lw=1.7, ls='--', label='Recomb. eta=2 (119 mV/dec)')
        pts = [(0.60, 0.0), (0.66, 1.0), (0.72, 2.0)]
        for vx, ly in pts:
            ax.plot(vx, ly, 'o', color=I, ms=4.5)
        ax.set_xlim(0.48, 0.79)
        ax.set_ylim(-2.2, 3.3)
        ax.legend(frameon=False, fontsize=6.9, loc='upper left')
        _txt(ax, 0.70, -1.1, '0.60V -> 1 mA\n0.66V -> 10 mA\n0.72V -> 100 mA', I, fs=6.9, ha='center')

    # ------------------------------------------------------------------ JEE 06
    elif key == 'rectifier_waveforms':
        _clean_plot(ax, 'Phase wt / pi', 'Output V / Vp')
        th = np.linspace(0, 3.0 * np.pi, 600)
        x = th / np.pi
        fw = np.abs(np.sin(th))
        hw = np.maximum(0.0, np.sin(th))
        u = (x - 0.5) % 1.0
        smooth = np.maximum(fw, 1.0 - 0.28 * u)
        ax.plot(x, hw, color=I, lw=1.2, ls=':', label='Half-wave (Vp/pi)')
        ax.plot(x, fw, color=T, lw=1.6, ls='--', label='Full-wave (2Vp/pi)')
        ax.plot(x, smooth, color=R, lw=2.0, label='C-filter (dV=I/2fC)')
        ax.set_xlim(0, 3.0)
        ax.set_ylim(-0.08, 1.78)
        ax.legend(frameon=False, fontsize=6.8, loc='upper right', ncol=2)

    elif key == 'bridge_rectifier_circuit':
        _schem(ax, (0, 10), (0, 5.4))
        pts = [(2.6, 2.7), (4.5, 4.4), (6.4, 2.7), (4.5, 1.0)]
        ax.add_patch(Polygon(pts, closed=True, fill=False, ec=T, lw=1.6))
        _txt(ax, 1.1, 2.7, 'AC Vin', I, fs=7.7, ha='center')
        ax.plot([1.85, 2.6], [2.7, 2.7], color=I, lw=1.3)
        ax.plot([4.5, 4.5], [4.4, 4.85], color=R, lw=1.3)
        ax.plot([4.5, 8.2], [4.85, 4.85], color=R, lw=1.3)
        ax.plot([8.2, 8.2], [4.38, 4.85], color=R, lw=1.3)
        ax.plot([8.2, 8.2], [2.7, 3.22], color=R, lw=1.3)
        ax.plot([6.4, 8.2], [2.7, 2.7], color=R, lw=1.3)
        _box(ax, 7.65, 3.25, 1.1, 1.1, fc=W, ec=R, lw=1.2)
        _txt(ax, 8.2, 3.8, 'RL // C', R, fs=7.2, ha='center')
        _txt(ax, 3.25, 3.95, 'D1', T, fs=7.4)
        _txt(ax, 5.55, 3.95, 'D2', T, fs=7.4)
        _txt(ax, 3.25, 1.45, 'D4', T, fs=7.4)
        _txt(ax, 5.55, 1.45, 'D3', T, fs=7.4)
        _txt(ax, 5.0, 0.35, '2 series diodes ON each half-cycle => Vp_out = Vp - 2*0.7V; PIV = Vp', I, fs=7.05, ha='center')

    # ------------------------------------------------------------------ JEE 07
    elif key == 'zener_regulator':
        _schem(ax, (0, 10), (0, 5.4))
        ax.plot([0.8, 2.3], [3.8, 3.8], color=I, lw=1.4)
        _box(ax, 2.3, 3.45, 1.8, 0.7, fc=W, ec=R, lw=1.25)
        _txt(ax, 3.2, 3.8, 'Rs', R, fs=7.9, ha='center')
        ax.plot([4.1, 8.2], [3.8, 3.8], color=I, lw=1.4)
        ax.plot([5.5, 5.5], [1.3, 2.08], color=T, lw=1.5)
        ax.plot([5.5, 5.5], [3.02, 3.8], color=T, lw=1.5)
        _box(ax, 5.0, 2.1, 1.0, 0.9, fc=S, ec=T, lw=1.25)
        _txt(ax, 5.5, 2.55, 'Vz', T, fs=7.8, ha='center')
        ax.plot([8.2, 8.2], [1.3, 2.08], color=I, lw=1.4)
        ax.plot([8.2, 8.2], [3.02, 3.8], color=I, lw=1.4)
        _box(ax, 7.7, 2.1, 1.0, 0.9, fc='#fdf8ea', ec=I, lw=1.2)
        _txt(ax, 8.2, 2.55, 'RL', I, fs=7.8, ha='center')
        ax.plot([0.8, 8.8], [1.3, 1.3], color=I, lw=1.3)
        _txt(ax, 1.2, 4.35, 'Vin', I, fs=7.7)
        _txt(ax, 4.75, 4.35, 'IR = IZ + IL', R, fs=7.3)
        _txt(ax, 5.0, 0.55, 'Squeeze: Rs <= (Vin,min - Vz)/(IL,max + IZ,min);  PZ,max at IL = 0!', I, fs=7.05, ha='center')

    elif key == 'solar_photodiode_quadrants':
        _clean_plot(ax, 'Junction voltage V (V)', 'Current I (mA)')
        v = np.linspace(-0.8, 0.66, 300)
        dark = 0.05 * (np.exp(v / 0.095) - 1.0)
        illum1 = dark - 3.6
        illum2 = dark - 7.0
        ax.plot(v, np.clip(dark, -11, 8), color=I, lw=1.7, label='Dark I-V')
        ax.plot(v, np.clip(illum1, -11, 8), color=T, lw=1.8, ls='--', label='Light 1x')
        ax.plot(v, np.clip(illum2, -11, 8), color=R, lw=2.0, label='Light 2x (Solar)')
        ax.axhline(0, color=I, lw=0.8)
        ax.axvline(0, color=I, lw=0.8)
        ax.set_xlim(-0.82, 0.68)
        ax.set_ylim(-11.2, 14.0)
        ax.legend(frameon=False, fontsize=6.9, loc='upper left')
        _txt(ax, -0.42, -9.3, 'Q-III: Photodiode', T, fs=6.9, ha='center')
        _txt(ax, 0.34, -9.3, 'Q-IV: Solar cell', R, fs=6.9, ha='center')

    # ------------------------------------------------------------------ JEE 08
    elif key == 'npn_current_flow':
        _schem(ax, (0, 10), (0, 5.4))
        ax.add_patch(Rectangle((1.1, 1.7), 2.7, 2.1, fc=W, ec=R, lw=1.25))
        ax.add_patch(Rectangle((3.8, 1.7), 1.1, 2.1, fc=S, ec=T, lw=1.25))
        ax.add_patch(Rectangle((4.9, 1.7), 3.9, 2.1, fc='#eef6f5', ec=I, lw=1.25))
        _txt(ax, 2.45, 2.75, 'n++ Emitter\n(heavy)', R, fs=7.3, ha='center')
        _txt(ax, 4.35, 2.75, 'p\nthin', T, fs=7.1, ha='center')
        _txt(ax, 6.85, 2.75, 'n Collector\n(wide area)', I, fs=7.3, ha='center')
        _arr(ax, (0.35, 4.35), (2.2, 4.35), R, lw=1.5)
        _txt(ax, 1.3, 4.88, 'IE = IB + IC', R, fs=7.4, ha='center')
        _arr(ax, (7.4, 4.35), (9.55, 4.35), I, lw=1.5)
        _txt(ax, 8.45, 4.88, 'IC = alpha IE = beta IB', I, fs=7.3, ha='center')
        _arr(ax, (4.35, 0.65), (4.35, 1.62), T, lw=1.4)
        _txt(ax, 6.65, 0.85, 'Small IB (~1-2% recomb.) controls IC!', T, fs=7.2, ha='center')

    elif key == 'bjt_output_loadline':
        _clean_plot(ax, 'Collector voltage VCE (V)', 'Current IC (mA)')
        vce = np.linspace(0, 10, 250)
        for ib, col, lb in [(20, T, 'IB=20 uA'), (40, I, 'IB=40 uA'), (60, R, 'IB=60 uA')]:
            ic = (ib * 0.1) * (1.0 - np.exp(-vce / 0.18)) * (1.0 + 0.012 * vce)
            ax.plot(vce, ic, color=col, lw=1.6, label=lb)
        ax.plot([0, 10], [8.0, 0.0], color=G, lw=1.9, ls='--', label='Load line VCC/RC')
        ax.plot(5.0, 4.0, 'o', color=G, ms=5.5)
        ax.set_xlim(0, 10.4)
        ax.set_ylim(0, 12.8)
        ax.legend(frameon=False, fontsize=6.8, loc='upper right', ncol=2)
        _txt(ax, 3.85, 3.25, 'Q-point', G, fs=7.1, ha='center')
        _txt(ax, 1.9, 9.6, 'Sat: VCE~0.2V', R, fs=6.9, ha='center')

    # ------------------------------------------------------------------ JEE 09
    elif key == 'ce_amplifier_transfer':
        _clean_plot(ax, 'Input base voltage Vin (V)', 'Output Vout (V)')
        vin = np.linspace(0, 2.2, 300)
        vout = np.where(vin < 0.6, 10.0,
               np.where(vin > 1.4, 0.2, 10.0 - 9.8 * (vin - 0.6) / 0.8))
        ax.plot(vin, vout, color=T, lw=2.1)
        ax.axvspan(0.6, 1.4, color=W, alpha=0.35)
        ax.set_xlim(0, 2.2)
        ax.set_ylim(-0.3, 11.2)
        _txt(ax, 0.3, 8.3, 'Cutoff\nVout=VCC', I, fs=7.0, ha='center')
        _txt(ax, 1.81, 7.8, 'Active: -gm RC\n(180 deg inv!)', R, fs=6.9, ha='center')
        _txt(ax, 1.82, 1.8, 'Saturation\nVCE ~ 0.2 V', T, fs=7.0, ha='center')

    elif key == 'bjt_switch_driver':
        _schem(ax, (0, 10), (0, 5.4))
        _box(ax, 0.6, 1.8, 2.2, 1.5, fc=S, ec=T, lw=1.2)
        _txt(ax, 1.7, 2.55, 'MCU 5V\nRB <= 4.3k', T, fs=7.3, ha='center')
        _arr(ax, (2.84, 2.55), (4.56, 2.55), T, lw=1.4)
        _box(ax, 4.6, 1.55, 1.9, 2.0, fc=W, ec=R, lw=1.3)
        _txt(ax, 5.55, 2.55, 'NPN ON\nVCE=0.2V', R, fs=7.4, ha='center')
        _box(ax, 4.6, 4.1, 1.9, 0.9, fc='#eef6f5', ec=I, lw=1.2)
        _txt(ax, 5.55, 4.55, 'Lamp 100mA', I, fs=7.2, ha='center')
        ax.plot([5.55, 5.55], [3.58, 4.08], color=I, lw=1.4)
        _txt(ax, 8.2, 3.2, 'VCC = 5.0 V\nLamp gets 4.8 V!\nForce IB > IC/beta', I, fs=7.2, ha='center')
        _txt(ax, 5.0, 0.6, 'Rule: NEVER trust exact beta — overdrive IB by 2x to guarantee saturation!', R, fs=7.05, ha='center')

    # ------------------------------------------------------------------ JEE 10
    elif key == 'diode_bjt_gates':
        _schem(ax, (0, 10), (0, 5.4))
        _box(ax, 0.45, 0.85, 4.3, 3.8, fc=S, ec=T, lw=1.2)
        _txt(ax, 2.6, 4.15, 'Diode OR vs AND', T, fs=7.8, ha='center')
        _txt(ax, 2.6, 3.1, 'OR: Anodes at A, B;\ncathodes + pull-DOWN R', I, fs=7.2, ha='center')
        _txt(ax, 2.6, 1.7, 'AND: Cathodes at A, B;\nanodes + pull-UP R to +V', R, fs=7.2, ha='center')
        _box(ax, 5.25, 0.85, 4.3, 3.8, fc='#fdf8ea', ec=R, lw=1.2)
        _txt(ax, 7.4, 4.15, '6 Core Gate Outputs', R, fs=7.8, ha='center')
        _txt(ax, 7.4, 2.95, 'AND: 0,0,0,1  | NAND: 1,1,1,0\nOR:  0,1,1,1  | NOR:  1,0,0,0', I, fs=7.1, ha='center')
        _txt(ax, 7.4, 1.65, 'XOR: 0,1,1,0  (odd 1s)\nXNOR: 1,0,0,1 (equality!)', T, fs=7.1, ha='center')

    elif key == 'logic_timing_waveforms':
        _clean_plot(ax, 'Clock time slot t', 'Stacked logic levels')
        t = np.linspace(0, 4, 800)
        A = np.where((t >= 2.0), 1.0, 0.0)
        B = np.where(((t >= 1.0) & (t < 2.0)) | (t >= 3.0), 1.0, 0.0)
        Y_nand = 1.0 - A * B
        Y_xor = np.abs(A - B)
        ax.plot(t, A * 0.7 + 3.2, color=I, lw=1.7)
        ax.plot(t, B * 0.7 + 2.15, color=T, lw=1.7)
        ax.plot(t, Y_nand * 0.7 + 1.1, color=R, lw=1.8)
        ax.plot(t, Y_xor * 0.7 + 0.05, color=G, lw=1.8)
        ax.set_xlim(-0.62, 4.15)
        ax.set_ylim(-0.15, 4.3)
        ax.set_yticks([])
        _txt(ax, -0.5, 3.55, 'A', I, fs=7.4)
        _txt(ax, -0.5, 2.5, 'B', T, fs=7.4)
        _txt(ax, -0.55, 1.45, 'NAND', R, fs=7.1)
        _txt(ax, -0.5, 0.4, 'XOR', G, fs=7.1)

    # ------------------------------------------------------------------ JEE 11
    elif key == 'nand_universal_map':
        _schem(ax, (0, 10), (0, 5.4))
        rows = [
            (4.35, 'NOT(A) = NAND(A, A)           ->  1 NAND  |  1 NOR', I),
            (3.45, 'AND(A, B) = NOT(NAND(A,B))    ->  2 NAND  |  3 NOR', T),
            (2.55, 'OR(A, B)  = NAND(A\', B\')      ->  3 NAND  |  2 NOR', R),
            (1.65, 'XOR(A, B) = optimal 2-level   ->  4 NAND  |  5 NOR', G),
            (0.75, 'XNOR(A,B) = dual symmetry     ->  5 NAND  |  4 NOR', I),
        ]
        _box(ax, 0.4, 0.3, 9.2, 4.75, fc=S, ec=T, lw=1.2)
        for yv, s, col in rows:
            _txt(ax, 5.0, yv, s, col, fs=7.35, ha='center')

    elif key == 'half_adder_circuit':
        _schem(ax, (0, 10), (0, 5.4))
        _txt(ax, 0.7, 3.9, 'A', I, fs=8.1)
        _txt(ax, 0.7, 1.6, 'B', I, fs=8.1)
        ax.plot([1.15, 3.38], [3.9, 3.9], color=I, lw=1.4)
        ax.plot([1.15, 3.38], [1.6, 1.6], color=T, lw=1.4)
        ax.plot([2.2, 2.2], [3.9, 2.1], color=I, lw=1.2, ls=':')
        ax.plot([2.2, 3.38], [2.1, 2.1], color=I, lw=1.2, ls=':')
        ax.plot([2.7, 2.7], [1.6, 3.4], color=T, lw=1.2, ls=':')
        ax.plot([2.7, 3.38], [3.4, 3.4], color=T, lw=1.2, ls=':')
        _box(ax, 3.4, 3.15, 2.2, 1.05, fc=S, ec=T, lw=1.3)
        _txt(ax, 4.5, 3.68, 'XOR Gate', T, fs=7.8, ha='center')
        _box(ax, 3.4, 1.32, 2.2, 1.05, fc=W, ec=R, lw=1.3)
        _txt(ax, 4.5, 1.85, 'AND Gate', R, fs=7.8, ha='center')
        _arr(ax, (5.64, 3.68), (6.9, 3.68), T, lw=1.4)
        _arr(ax, (5.64, 1.85), (6.9, 1.85), R, lw=1.4)
        _txt(ax, 7.1, 3.68, 'Sum S = A xor B', T, fs=7.5)
        _txt(ax, 7.1, 1.85, 'Carry C = A . B', R, fs=7.5)
        _txt(ax, 5.0, 0.52, '1 + 1 = 10_2  (C=1, S=0);  Full Adder = 2 Half Adders + 1 OR gate!', I, fs=7.1, ha='center')

    # ------------------------------------------------------------------ JEE 12
    elif key == 'led_bandgap_spectrum':
        _clean_plot(ax, 'Band gap Eg (eV)', 'Wavelength lam (nm)')
        eg = np.linspace(1.1, 3.5, 300)
        lam = 1240.0 / eg
        ax.plot(eg, lam, color=T, lw=2.0)
        pts = [
            (1.12, 1107, (1.22, 1140, 'left'), 'Si (IR, indirect!)', I),
            (1.42, 873, (1.52, 915, 'left'), 'GaAs (IR)', G),
            (1.90, 653, (2.02, 700, 'left'), 'GaAsP (Red)', R),
            (2.25, 551, (2.37, 595, 'left'), 'GaP (Green)', G),
            (2.64, 470, (2.75, 505, 'left'), 'InGaN (Blue)', T),
        ]
        for x0, y0, (tx, ty, ha), lb, col in pts:
            ax.plot(x0, y0, 'o', color=col, ms=4.6)
            ax.text(tx, ty, lb, color=col, fontsize=6.9, ha=ha, va='center')
        ax.set_xlim(1.0, 3.65)
        ax.set_ylim(310, 1250)

    elif key == 'multi_diode_solver':
        _schem(ax, (0, 10), (0, 5.4))
        _box(ax, 0.45, 3.3, 9.1, 1.55, fc=S, ec=T, lw=1.2)
        _txt(ax, 5.0, 4.35, '4-Step Multi-Diode Circuit Protocol', T, fs=7.9, ha='center')
        _txt(ax, 5.0, 3.72, '1. Open all diodes -> rank open-circuit anode-cathode voltages V_open', I, fs=7.1, ha='center')
        _box(ax, 0.45, 0.65, 9.1, 2.25, fc='#fdf8ea', ec=R, lw=1.2)
        _txt(ax, 5.0, 2.38, '2. Turn ON diode with LARGEST positive V_open first (0.7 V source)', R, fs=7.1, ha='center')
        _txt(ax, 5.0, 1.72, '3. Re-compute node voltages -> check whether 2nd diode also exceeds 0.7 V', I, fs=7.1, ha='center')
        _txt(ax, 5.0, 1.06, '4. Verify EVERY ON diode has I > 0 and EVERY OFF diode has V < V_knee!', G, fs=7.1, ha='center')

    # ------------------------------------------------------------- OLYMPIAD 01
    elif key == 'bohr_donor_scaling':
        _schem(ax, (0, 10), (0, 5.4))
        cx, cy = 2.65, 2.85
        for gx in np.linspace(1.1, 4.2, 5):
            ax.plot([gx, gx], [1.3, 4.4], color=GR, lw=0.8)
        for gy in np.linspace(1.3, 4.4, 5):
            ax.plot([1.1, 4.2], [gy, gy], color=GR, lw=0.8)
        ax.add_patch(Circle((cx, cy), 1.4, fill=False, ec=T, lw=1.7, ls='--'))
        ax.add_patch(Circle((cx, cy), 0.16, fc=R, ec=R))
        _txt(ax, cx, 0.65, 'a* = 2.4 nm (~4.4 Si cells)', T, fs=7.2, ha='center')
        _box(ax, 5.05, 0.7, 4.5, 4.15, fc=S, ec=I, lw=1.2)
        _txt(ax, 7.3, 4.35, 'Scaled Hydrogenic Model', I, fs=7.6, ha='center')
        _txt(ax, 7.3, 3.05, 'Ed = 13.6 (m*/m) / kappa^2\nSi:P calc = 26 meV ~ kT\nMeasured = 45 meV (x1.7)', R, fs=7.1, ha='center')
        _txt(ax, 7.3, 1.35, 'GaAs: Ed = 5.5 meV,\na* = 10.2 nm (shallow!)', T, fs=7.1, ha='center')

    elif key == 'carrier_freezeout_intrinsic':
        _clean_plot(ax, 'Inverse temperature 1000 / T (K^-1)', 'log10 [ n (m^-3) ]')
        invT = np.linspace(1.2, 12.0, 400)
        T_arr = 1000.0 / invT
        ni = 1.5e16 * (T_arr / 300.0) ** 1.5 * np.exp((1.12 / (2 * 8.617e-5)) * (1 / 300.0 - 1 / T_arr))
        nd_ion = 1.0e21 / (1.0 + 0.5 * np.exp((0.045 / (8.617e-5 * T_arr)) - 5.5))
        n_tot = 0.5 * (nd_ion + np.sqrt(nd_ion ** 2 + 4.0 * ni ** 2))
        ax.plot(invT, np.log10(n_tot), color=T, lw=2.1)
        ax.axvline(1.79, color=R, lw=1.0, ls='--')
        ax.axvline(7.5, color=I, lw=1.0, ls=':')
        ax.set_xlim(1.2, 12.0)
        ax.set_ylim(18.0, 23.6)
        _txt(ax, 3.1, 22.8, 'Intrinsic <1.8\n(T > 560 K)', R, fs=6.9, ha='center')
        _txt(ax, 4.9, 21.65, 'Extrinsic plateau n ~ Nd', T, fs=7.0, ha='center')
        _txt(ax, 9.8, 21.8, 'Freeze-out\n(T < 120 K)', I, fs=6.9, ha='center')

    # ------------------------------------------------------------- OLYMPIAD 02
    elif key == 'boltzmann_hill_injection':
        _clean_plot(ax, 'Distance x across junction', 'Band edge Ec(x) (arb.)')
        x = np.linspace(-2, 2, 300)
        s = 0.5 * (1.0 - np.tanh(1.8 * x))
        ax.plot(x, 1.0 * s, color=I, lw=1.9, label='Equil: q V0')
        ax.plot(x, 0.55 * s, color=T, lw=1.9, ls='--', label='Forward: q(V0 - V)')
        ax.plot(x, 1.55 * s, color=R, lw=1.9, ls=':', label='Reverse: q(V0 + V)')
        ax.set_xlim(-2, 2)
        ax.set_ylim(-0.12, 1.82)
        ax.legend(frameon=False, fontsize=6.9, loc='upper right')
        _txt(ax, 1.15, 0.45, 'exp(V/VT) flood!', T, fs=7.0, ha='center')

    elif key == 'varactor_capacitance':
        _clean_plot(ax, 'Reverse bias VR (V)', 'Normalized W and Cj')
        vr = np.linspace(0, 8.0, 300)
        v0 = 0.7
        c_norm = np.sqrt(v0 / (v0 + vr))
        w_norm = np.sqrt((v0 + vr) / v0)
        inv_c2 = (v0 + vr) / v0
        ax.plot(vr, c_norm, color=T, lw=2.0, label='Cj / C0 ~ (V0+VR)^(-1/2)')
        ax.plot(vr, w_norm, color=R, lw=1.8, ls='--', label='W / W0 ~ (V0+VR)^(+1/2)')
        ax.plot(vr, inv_c2 * 0.3, color=I, lw=1.6, ls=':', label='0.3*(C0/Cj)^2 linear!')
        ax.set_xlim(0, 8.0)
        ax.set_ylim(0, 6.6)
        ax.legend(frameon=False, fontsize=6.8, loc='upper left')

    # ------------------------------------------------------------- OLYMPIAD 03
    elif key == 'hall_slab_geometry':
        _schem(ax, (0, 10), (0, 5.4))
        _box(ax, 1.45, 1.55, 7.1, 2.35, fc=S, ec=T, lw=1.35)
        _arr(ax, (0.35, 2.72), (1.38, 2.72), R, lw=1.6)
        _arr(ax, (8.62, 2.72), (9.65, 2.72), R, lw=1.6)
        _txt(ax, 0.85, 3.3, 'I_x', R, fs=7.8, ha='center')
        _txt(ax, 5.0, 3.32, 'B_z (x): Lorentz pushes BOTH e- & h+ SAME side!', I, fs=6.9, ha='center')
        _txt(ax, 5.0, 2.15, 'n-type (-), p-type (+): VH SIGN NAMES CARRIER!', T, fs=6.9, ha='center')
        _txt(ax, 5.0, 0.72, 'VH = I B / (n e t),     RH = -/+ 1/(n e),     mu_H = |RH| sigma', R, fs=7.3, ha='center')

    elif key == 'bandgap_reference_ptat':
        _clean_plot(ax, 'Temperature T (K)', 'Voltage (V)')
        Tk = np.linspace(220, 420, 250)
        vbe = 0.72 - 0.0020 * (Tk - 300.0)
        ptat = 0.50 + 0.0020 * (Tk - 300.0)
        vref = vbe + ptat
        ax.plot(Tk, vbe, color=R, lw=1.8, ls='--', label='CTAT: VBE (-2 mV/K)')
        ax.plot(Tk, ptat, color=T, lw=1.8, ls=':', label='PTAT: K*VT (+2 mV/K)')
        ax.plot(Tk, vref, color=I, lw=2.2, label='Vref = 1.22 V flat')
        ax.set_xlim(220, 420)
        ax.set_ylim(0.25, 2.15)
        ax.legend(frameon=False, fontsize=6.8, loc='upper right', ncol=2)

    # ------------------------------------------------------------- OLYMPIAD 04
    elif key == 'shockley_queisser_curve':
        _clean_plot(ax, 'Band gap Eg (eV)', 'Max 1-sun efficiency (%)')
        eg = np.linspace(0.4, 3.2, 300)
        eta = 33.7 * np.exp(-((eg - 1.34) / 0.86) ** 2) * (1.0 - 0.12 * np.maximum(0.0, 1.1 - eg))
        ax.plot(eg, eta, color=T, lw=2.1)
        ax.plot(1.12, 32.0, 'o', color=R, ms=5)
        ax.plot(1.34, 33.7, 's', color=I, ms=5)
        ax.set_xlim(0.4, 3.2)
        ax.set_ylim(0, 39.5)
        _txt(ax, 1.34, 36.8, 'SQ peak ~33.7% (1.34 eV)', I, fs=7.0, ha='center')
        _txt(ax, 0.72, 30.0, 'Si 1.12 eV', R, fs=7.0, ha='center')
        _txt(ax, 2.55, 23.5, 'Sub-gap photons\ntransparent loss', I, fs=6.9, ha='center')

    elif key == 'shaded_panel_bypass':
        _clean_plot(ax, 'Panel string voltage V (V)', 'String current I (A)')
        v = np.linspace(0, 18.5, 400)
        clean = 8.0 * (1.0 - np.exp((v - 18.0) / 1.1))
        bypass = np.where(v < 11.4,
                          8.0 * (1.0 - 0.06 * np.exp((v - 11.4) / 0.8)),
                          2.2 * (1.0 - np.exp((v - 17.5) / 1.0)))
        nobyp = 2.0 * (1.0 - np.exp((v - 17.0) / 1.2))
        ax.plot(v, np.clip(clean, 0, 9), color=G, lw=1.7, ls=':', label='Unshaded 3-block')
        ax.plot(v, np.clip(bypass, 0, 9), color=T, lw=2.0, label='With bypass diode')
        ax.plot(v, np.clip(nobyp, 0, 9), color=R, lw=1.7, ls='--', label='No bypass (hotspot!)')
        ax.set_xlim(0, 18.8)
        ax.set_ylim(0, 14.8)
        ax.legend(frameon=False, fontsize=6.8, loc='upper right', ncol=2)

    # ------------------------------------------------------------- OLYMPIAD 05
    elif key == 'shot_vs_thermal_noise':
        _clean_plot(ax, 'log10 [ Photocurrent I (A) ]', 'log10 [ in (A/rtHz) ]')
        lgI = np.linspace(-10, -2, 300)
        I_a = 10.0 ** lgI
        shot = np.log10(np.sqrt(2.0 * 1.602e-19 * I_a))
        th10k = np.full_like(lgI, np.log10(np.sqrt(4.0 * 1.381e-23 * 300.0 / 1e4)))
        th1m = np.full_like(lgI, np.log10(np.sqrt(4.0 * 1.381e-23 * 300.0 / 1e6)))
        ax.plot(lgI, shot, color=R, lw=2.0, label='Shot sqrt(2eI)')
        ax.plot(lgI, th10k, color=I, lw=1.6, ls='--', label='Johnson RL=10k')
        ax.plot(lgI, th1m, color=T, lw=1.6, ls=':', label='Johnson RL=1M')
        ax.set_xlim(-10, -2)
        ax.set_ylim(-17.0, -9.8)
        ax.legend(frameon=False, fontsize=6.9, loc='lower right')

    elif key == 'led_loadline_stability':
        _clean_plot(ax, 'LED forward voltage V (V)', 'Current I (mA)')
        v = np.linspace(1.6, 2.35, 300)
        i_led = 20.0 * np.exp((v - 2.0) / 0.045)
        ax.plot(v, np.clip(i_led, 0, 50), color=R, lw=2.0, label='2.0V Red LED I-V')
        ax.plot(v, (5.0 - v) / 0.150, color=T, lw=1.9, label='5V + 150 ohm line')
        ax.axvline(2.05, color=I, lw=1.2, ls=':', label='Direct V drive!')
        ax.plot(2.0, 20.0, 'o', color=I, ms=5)
        ax.set_xlim(1.6, 2.35)
        ax.set_ylim(0, 82)
        ax.legend(frameon=False, fontsize=6.8, loc='upper left', ncol=2)

    # ------------------------------------------------------------- OLYMPIAD 06
    elif key == 'quantum_tunnelling_wall':
        _clean_plot(ax, 'Gate oxide d_ox (nm)', 'log10 [ T_WKB ]')
        d = np.linspace(0.8, 5.0, 300)
        lgT = -11.4 * d / np.log(10.0)
        ax.plot(d, lgT, color=R, lw=2.1, label='SiO2 WKB leakage')
        ax.plot(d, -11.4 * (d * 2.8) / np.log(10.0) * 0.45, color=T, lw=1.8, ls='--', label='High-k HfO2 rescue')
        ax.axvline(1.5, color=I, lw=1.0, ls=':')
        ax.set_xlim(0.8, 5.0)
        ax.set_ylim(-26.0, 2.5)
        ax.legend(frameon=False, fontsize=6.9, loc='upper right')
        _txt(ax, 1.62, -22.5, 'd_ox < 1.5 nm: OFF leaks!', I, fs=7.0)

    elif key == 'cmos_power_scaling':
        _clean_plot(ax, 'Supply voltage VDD (V)', 'Chip power P (W)')
        vdd = np.linspace(0.4, 1.3, 300)
        pdyn = 0.5 * 1e9 * 1e9 * 1e-15 * vdd ** 2
        pleak = 95.0 * np.exp((0.75 - vdd) * 2.1) * vdd
        ptot = pdyn + pleak
        ax.plot(vdd, pdyn, color=T, lw=1.9, label='Dynamic ~ VDD^2')
        ax.plot(vdd, pleak, color=R, lw=1.7, ls='--', label='Subthreshold leak')
        ax.plot(vdd, ptot, color=I, lw=2.1, label='Total chip power')
        ax.set_xlim(0.4, 1.3)
        ax.set_ylim(0, 950)
        ax.legend(frameon=False, fontsize=6.9, loc='upper left')
    else:
        raise KeyError(f'Unknown diagram key: {key}')
    return CAPTIONS[key]
