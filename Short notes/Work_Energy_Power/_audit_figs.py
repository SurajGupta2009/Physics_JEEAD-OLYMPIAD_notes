"""Check that no text of any figure falls outside the sheet canvas.

Renders every figure into the exact slot it will occupy on a page and walks the
text objects, so a label parked past the right edge or above the title fails
here instead of on the printed page.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from layout import DPI, W, M, CARRY_Y, FIG_MIN_Y
import diagrams

width = W - 2 * M
height = CARRY_Y - 24 - FIG_MIN_Y

KEYS = list(diagrams.KEYS)
bad = 0
for key in KEYS:
    fig = plt.figure(figsize=(width / DPI, (height - 78) / DPI), dpi=DPI,
                     facecolor='white')
    ax = fig.add_axes([.03, .05, .94, .84])
    ax.axis('off')
    diagrams.figure(ax, key)
    fig.canvas.draw()
    r = fig.canvas.get_renderer()
    for t in fig.findobj(matplotlib.text.Text):
        if not t.get_text().strip() or not t.get_visible():
            continue
        bb = t.get_window_extent(r)
        if bb.x0 < -1 or bb.y0 < -1 or bb.x1 > width + 1 or bb.y1 > height - 77:
            bad += 1
            print(f'{key}: {t.get_text()!r} at Bbox({bb.x0:.0f},{bb.y0:.0f},'
                  f'{bb.x1:.0f},{bb.y1:.0f})')
    plt.close(fig)

print(f'figures with issues: {bad} of {len(KEYS)}')
