"""Check every figure at the real band size: text inside the canvas, no clipping."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from layout import DPI, W, M, CARRY_Y, FIG_MIN_Y, BODY_TOP
import diagrams

width = W - 2 * M
height = CARRY_Y - 24 - FIG_MIN_Y
bad = 0
for key in sorted(k for k in diagrams.figure.__code__.co_consts if isinstance(k, str) and '_' in k and k not in ('__main__',)):
    pass
KEYS = ['thomson_vs_rutherford','closest_approach','standing_wave','bohr_ledger','spectrum_series','excitation_ladder','hydrogenic_scaling','quantum_numbers','photon_packet','photoelectric_curve','stopping_graph','photocell_iv','debroglie_scale','davisson_germer','uncertainty_well','xray_continuous','xray_characteristic','absorption_curve','bragg_geometry','compton_kinematics','correspondence_plot','exotic_atoms','collapse_spiral','franck_hertz','waiting_time','matter_wave_speeds','compton_invariant','inverse_compton','moseley_line','pair_threshold']
for key in KEYS:
    fig = plt.figure(figsize=(width / DPI, (height - 78) / DPI), dpi=DPI, facecolor='white')
    ax = fig.add_axes([.03, .05, .94, .84])
    ax.axis('off')
    diagrams.figure(ax, key)
    fig.canvas.draw()
    r = fig.canvas.get_renderer()
    issues = []
    for a in fig.axes:
        arts = list(a.texts) + [a.xaxis.label, a.yaxis.label]
        if a.axison:
            arts += [t for t in a.get_xticklabels() if a.get_xlim()[0] <= t.get_position()[0] <= a.get_xlim()[1]]
            arts += [t for t in a.get_yticklabels() if a.get_ylim()[0] <= t.get_position()[1] <= a.get_ylim()[1]]
        for art in arts:
            if not art.get_visible() or not art.get_text():
                continue
            bb = art.get_window_extent(r)
            if bb.x0 < -1 or bb.y0 < -1 or bb.x1 > width + 1 or bb.y1 > height - 77:
                issues.append((art.get_text(), [round(v) for v in (bb.x0, bb.y0, bb.x1, bb.y1)]))
    plt.close(fig)
    if issues:
        bad += 1
        print(f'{key}: {len(issues)}')
        for t, b in issues[:6]:
            print('   ', repr(t), b)
print('figures with issues:', bad, 'of', len(KEYS))
