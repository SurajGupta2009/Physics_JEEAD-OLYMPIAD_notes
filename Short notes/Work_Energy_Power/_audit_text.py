"""Overlap audit: renders every figure in its page slot and reports pairs of
text objects whose bounding boxes intersect. Text-on-text collisions are the
one defect the bounds audit cannot see."""
import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import diagrams
from layout import DPI, W, M, CARRY_Y, FIG_MIN_Y

width, height = W - 2 * M, CARRY_Y - 24 - FIG_MIN_Y


def boxes(key):
    fig = plt.figure(figsize=(width / DPI, (height - 78) / DPI), dpi=DPI, facecolor='white')
    ax = fig.add_axes([.03, .05, .94, .84]); ax.axis('off')
    diagrams.figure(ax, key)
    fig.canvas.draw()
    out = []
    for t in fig.findobj(plt.Text):
        s = t.get_text().strip()
        if not s or not t.get_visible():
            continue
        bb = t.get_window_extent()
        if bb.width > 0 and bb.height > 0:
            out.append((s, bb))
    plt.close(fig)
    return out


def main(keys):
    total = 0
    for key in keys:
        bs = boxes(key)
        hits = []
        for i in range(len(bs)):
            for j in range(i + 1, len(bs)):
                a, b = bs[i][1], bs[j][1]
                ox = min(a.x1, b.x1) - max(a.x0, b.x0)
                oy = min(a.y1, b.y1) - max(a.y0, b.y0)
                if ox > 4 and oy > 4:
                    hits.append((round(ox), round(oy), bs[i][0], bs[j][0]))
        if hits:
            total += 1
            print(f'{key}: {len(hits)}')
            for ox, oy, s1, s2 in sorted(hits, reverse=True)[:6]:
                print(f'   {ox}x{oy}  {s1[:44]!r}  vs  {s2[:44]!r}')
    print(f'figures with text collisions: {total} of {len(keys)}')


if __name__ == '__main__':
    main(sys.argv[1:] or list(diagrams.KEYS))
