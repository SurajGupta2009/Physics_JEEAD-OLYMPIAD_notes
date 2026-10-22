"""Shared drawing vocabulary for the work-energy-power figures.

One wide figure per sheet, at most two panels, at most six labels per panel.
Everything is a closed-form curve, a shaded area, a labelled free-body diagram
or an energy ledger: no decorative imagery, no sampled noise.
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, Ellipse, Arc, Polygon, Wedge

I = '#153149'
T = '#087d7d'
R = '#a43232'
PALE = '#eff8f5'
YEL = '#fff2b8'
G = '#516875'
GOLD = '#8a6a10'
WATER = '#e8f3f8'
HG = '#c9d2d7'
BLUE = '#2f6f9f'
GREEN = '#4a7c3f'


def txt(ax, x, y, s, color=I, **kw):
    kw.setdefault('fontsize', 8.6)
    ax.text(x, y, s, color=color, **kw)


def _fit(ax, s, fs, x, y, color, va):
    fig = ax.figure
    for f in (fs, fs - .6, fs - 1.2, fs - 1.8, fs - 2.4):
        t = ax.text(x, y, s, transform=ax.transAxes, fontsize=f, color=color,
                    ha='center', va=va)
        bb = t.get_window_extent(fig.canvas.get_renderer())
        ab = ax.get_window_extent()
        if bb.x0 >= ab.x0 + 1 and bb.x1 <= ab.x1 - 1:
            return
        t.remove()
    ax.text(x, y, s, transform=ax.transAxes, fontsize=fs - 2.4, color=color,
            ha='center', va=va)


def head(ax, s, color=T):
    """Panel title above the frame when the panel carries axes."""
    if ax.axison:
        ax.annotate(s, xy=(.5, 1), xycoords='axes fraction', xytext=(0, 7),
                    textcoords='offset points', ha='center', va='bottom',
                    fontsize=9.0, color=color)
    else:
        _fit(ax, s, 9.0, .5, .99, color, 'top')


def foot(ax, s, color=G):
    _fit(ax, s, 7.4, .5, .01, color, 'bottom')


def arrow(ax, a, b, c=T, lw=1.5, style='->', ms=8):
    ax.annotate('', xy=b, xytext=a,
                arrowprops=dict(arrowstyle=style, color=c, lw=lw, shrinkA=0,
                                shrinkB=0, mutation_scale=ms))


def panel(fig, rect, xlim=(0, 10), ylim=(0, 4.6), equal=False):
    # Keep every panel inside the printed band: the y-axis label hangs ~26 pt to
    # the left, and the last tick label ~40 px to the right of the frame.
    x, y, w, h = rect
    x = max(x, .075)
    if x + w > .925:
        x = max(.075, .925 - w)
    a = fig.add_axes([x, y, w, h])
    a.axis('off')
    a.set_xlim(*xlim)
    a.set_ylim(*ylim)
    if equal:
        a.set_aspect('equal', adjustable='box')
    return a


def axes2(a, xlabel, ylabel):
    """Axis furniture placed in points, not axes fractions."""
    a.axis('on')
    a.spines[['top', 'right']].set_visible(False)
    a.tick_params(labelsize=7.0, length=3, pad=2)
    a.grid(alpha=.12, lw=.7)
    a.annotate(xlabel, xy=(.5, 0), xycoords='axes fraction', xytext=(0, -19),
               textcoords='offset points', ha='center', va='top',
               fontsize=7.8, color=I)
    a.annotate(ylabel, xy=(0, .5), xycoords='axes fraction', xytext=(-26, 0),
               textcoords='offset points', ha='center', va='center',
               rotation=90, fontsize=7.8, color=I)


def dimx(ax, x0, x1, y, label, color=I, fs=8.2):
    arrow(ax, (x0, y), (x1, y), color, 1.0, '<->', 6)
    ax.text((x0 + x1) / 2, y + .10, label, ha='center', fontsize=fs, color=color)


def dimy(ax, x, y0, y1, label, side='right', color=I, fs=8.2):
    arrow(ax, (x, y0), (x, y1), color, 1.0, '<->', 6)
    ax.text(x + (.14 if side == 'right' else -.14), (y0 + y1) / 2, label,
            ha='left' if side == 'right' else 'right', va='center', fontsize=fs, color=color)


def incline(ax, x0, x1, y0, theta, lw=2.2, fill='#f2f6f5'):
    """Right-triangle ramp with its base at y0, apex at x1."""
    h = (x1 - x0) * np.tan(np.radians(theta))
    ax.add_patch(Polygon([(x0, y0), (x1, y0), (x1, y0 + h)], closed=True,
                         fc=fill, ec=I, lw=lw, zorder=1))
    return h


def block(ax, cx, cy, w, h, fc='#fdf0bd', ec=GOLD, lw=1.4, z=3):
    ax.add_patch(Rectangle((cx - w / 2, cy - h / 2), w, h, fc=fc, ec=ec,
                           lw=lw, zorder=z))


def force(ax, p, q, color=R, lw=1.6, label=None, fs=8.0, off=(.16, .05), ha='left'):
    arrow(ax, p, q, color, lw)
    if label:
        ax.text(q[0] + off[0], q[1] + off[1], label, fontsize=fs, color=color, ha=ha)


def dashed(ax, p, q, color=HG, lw=1.0):
    ax.plot([p[0], q[0]], [p[1], q[1]], color=color, lw=lw, ls=(0, (3, 2)))


def ball(ax, cx, cy, r=None, fc='#fdf0bd', ec=GOLD, lw=1.3, z=5):
    ax.add_patch(Circle((cx, cy), r or .22, fc=fc, ec=ec, lw=lw, zorder=z))


def spring(ax, p, q, n=9, amp=.16, color=I, lw=1.5, z=4):
    """Zig-zag between two points (used for horizontal or vertical springs)."""
    p, q = np.array(p, float), np.array(q, float)
    d = q - p
    L = np.hypot(*d)
    u = d / L
    nrm = np.array([-u[1], u[0]])
    t = np.linspace(0, 1, 2 * n + 3)
    off = np.zeros_like(t)
    off[1:-1] = amp * np.where(np.arange(2 * n + 1) % 2 == 0, 1, -1)
    pts = p[None, :] + np.outer(t, d) + np.outer(off, nrm)
    ax.plot(pts[:, 0], pts[:, 1], color=color, lw=lw, solid_joinstyle='miter', zorder=z)


def bars(ax, keys, vals, colors=None, width=.62, labels=True, fmt=None):
    """Signed bar chart with the zero line, used for every energy ledger."""
    colors = colors or [T] * len(vals)
    xs = np.arange(len(vals))
    ax.bar(xs, vals, color=colors, width=width, zorder=3)
    ax.axhline(0, color=I, lw=.9, zorder=4)
    ax.set_xticks(xs)
    ax.set_xticklabels(keys, fontsize=7.2)
    if fmt is None:
        fmt = '{:.0f}' if all(float(v).is_integer() for v in vals) else '{:.2f}'
    if labels:
        for x, v in zip(xs, vals):
            ax.text(x, v + (.03 if v >= 0 else -.03) * max(abs(np.array(vals)).max(), 1),
                    fmt.format(v), ha='center',
                    va='bottom' if v >= 0 else 'top', fontsize=7.0, color=G)
    ax.set_xlim(-.62, len(vals) - .38)
    ax.spines[['top', 'right']].set_visible(False)
    ax.tick_params(labelsize=7.0, length=3, pad=2)
    ax.grid(alpha=.12, lw=.7, axis='y')


def shade_between(ax, x, y1, y2, color=T, alpha=.16):
    ax.fill_between(x, y1, y2, color=color, alpha=alpha, lw=0, zorder=2)


def arcarrow(ax, c, r, t1, t2, color=T, lw=1.6, ms=9):
    ax.add_patch(Arc(c, 2 * r, 2 * r, theta1=t1, theta2=t2, color=color, lw=lw, zorder=4))
    th = np.radians(t2)
    p = (c[0] + r * np.cos(th), c[1] + r * np.sin(th))
    th2 = np.radians(t2 + 4)
    q = (c[0] + r * np.cos(th2), c[1] + r * np.sin(th2))
    arrow(ax, p, q, color, lw, ms=ms)


def rot_block(ax, cx, cy, w, h, deg, fc='#fdf0bd', ec=GOLD, lw=1.4, z=4):
    t = np.radians(deg)
    c, s = np.cos(t), np.sin(t)
    pts = [(cx + qx * c - qy * s, cy + qx * s + qy * c)
           for qx, qy in [(-w / 2, -h / 2), (w / 2, -h / 2), (w / 2, h / 2), (-w / 2, h / 2)]]
    ax.add_patch(Polygon(pts, closed=True, fc=fc, ec=ec, lw=lw, zorder=z))
