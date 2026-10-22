"""Visual probe: page thumbnails and figure-contact sheets.

    python3 _probe.py page JEE-01-work-sign ...     # full-page thumbnails
    python3 _probe.py crop JEE-01-work-sign ...     # top/bottom half crops
    python3 _probe.py figs key key ...              # 6 figures per image
"""
import sys
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from PIL import Image

ROOT = Path(__file__).resolve().parent
OUT = ROOT / '_probe_out'
OUT.mkdir(exist_ok=True)


def thumbs(names, tag='page'):
    ims = [Image.open(ROOT / f'{n}.png') for n in names]
    w = 620
    hs = [int(im.height * w / im.width) for im in ims]
    cols = 1 if len(ims) == 1 else 2
    rows = (len(ims) + cols - 1) // cols
    fig = plt.figure(figsize=(cols * w / 100, sum(hs[:rows]) / 100 * 1.0 + 0.2), dpi=100)
    fig.patch.set_facecolor('0.86')
    y = 1.0
    for i, (im, h) in enumerate(zip(ims, hs)):
        r, c = divmod(i, cols)
        ax = fig.add_axes([c / cols, 1 - (r + 1) * (1 / rows), 1 / cols, 1 / rows])
        ax.imshow(im.resize((w, int(im.height * w / im.width))))
        ax.set_axis_off()
    p = OUT / f'{tag}.png'
    fig.savefig(p, facecolor=fig.get_facecolor())
    plt.close(fig)
    print(p)


def crops(names):
    ims = []
    for n in names:
        im = Image.open(ROOT / f'{n}.png')
        top = im.crop((0, 0, im.width, im.height // 2)).resize((900, im.height // 2 * 900 // im.width))
        bot = im.crop((0, im.height // 2, im.width, im.height)).resize((900, im.height // 2 * 900 // im.width))
        ims += [top, bot]
    w = 900
    fig = plt.figure(figsize=(w / 100, sum(i.height for i in ims) / 100), dpi=100)
    ax = fig.add_axes([0, 0, 1, 1]); ax.set_axis_off()
    canvas = Image.new('RGB', (w, sum(i.height for i in ims)), 'white')
    y = 0
    for i in ims:
        canvas.paste(i, (0, y)); y += i.height
    ax.imshow(canvas)
    p = OUT / 'crops.png'
    fig.savefig(p, facecolor='w')
    plt.close(fig)
    print(p)


def figs(keys):
    import diagrams
    fig = plt.figure(figsize=(13, 8.6), dpi=100)
    fig.patch.set_facecolor('white')
    for i, k in enumerate(keys):
        r, c = divmod(i, 2)
        ax = fig.add_axes([c / 2 + .01, 1 - (r + 1) / 3 + .01, 1 / 2 - .02, 1 / 3 - .02])
        try:
            diagrams.figure(ax, k)
        except Exception as e:
            ax.text(.5, .5, f'{k}\n{e}', ha='center', va='center', fontsize=7)
        ax.set_title(k, fontsize=8)
    p = OUT / 'figs.png'
    fig.savefig(p, facecolor='w')
    plt.close(fig)
    print(p)


if __name__ == '__main__':
    mode, rest = sys.argv[1], sys.argv[2:]
    {'page': thumbs, 'crop': crops, 'figs': figs}[mode](rest)
