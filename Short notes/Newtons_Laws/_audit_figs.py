"""Check every figure at the real band size: text inside the canvas, no clipping."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from layout import DPI, W, M, CARRY_Y, FIG_MIN_Y
import diagrams

width = W - 2 * M
height = CARRY_Y - 24 - FIG_MIN_Y
KEYS = ['inertial_frames', 'second_law', 'third_law', 'fbd_incline',
        'apparent_weight', 'lami', 'friction_static', 'friction_direction',
        'stacked_blocks', 'min_pull', 'movable_pulley', 'wedge_constraint',
        'pseudo_frame', 'centripetal_source', 'banked_design', 'banked_band',
        'conical', 'circle_string', 'circle_rod', 'system_parts',
        'falling_chain', 'rocket_ratio', 'capstan', 'sand_belt', 'bead_hoop',
        'chain_lift', 'turntable', 'staging', 'impulse_window', 'hitch_turns',
        'virtual_work', 'rope_table', 'effective_g', 'wedge_liftoff',
        'turntable_limit', 'atwood_incline',
        'energy_shortcut', 'rough_table_pulley', 'accelerating_incline',
        'measure_mu', 'chain_table', 'wedge_carry',
        'slack_angle', 'bounce_series', 'wedge_momentum', 'stage_split',
        'limits_model', 'rolling_contact', 'four_shortcuts',
        'monkey_rope']
bad = 0
for key in KEYS:
    fig = plt.figure(figsize=(width / DPI, (height - 78) / DPI), dpi=DPI, facecolor='white')
    ax = fig.add_axes([.03, .05, .94, .84])
    ax.axis('off')
    diagrams.figure(ax, key)
    fig.canvas.draw()
    r = fig.canvas.get_renderer()
    issues = []
    lt = [t for t in fig.texts if t.get_text()]
    for a in [fig] + list(fig.axes):
        if a is fig:
            arts = lt
        else:
            arts = list(a.texts) + [a.xaxis.label, a.yaxis.label]
        if a is not fig and a.axison:
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
        for t, bb in issues:
            print('   ', repr(t), bb)
print(f'figures with issues: {bad} of {len(KEYS)}')
