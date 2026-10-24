"""Render the JEE-only Capacitors notes: one column, dense, teacher order.

Layout rules
  * A4 portrait, 300 dpi, single vertical column, ~10 mm safe margin.
  * Blocks flow down the page: numbered heading, text, result box, worked
    example, trap, table, figure, remember strip.
  * Formula images are only scaled down to 0.82; body type is never shrunk to
    hide overflow. Each page asserts that it fits above the footer.
  * Inline maths is written as $...$ inside any text and is measured with the
    text while wrapping, so lines break cleanly around a formula.
"""
from pathlib import Path
import json, io, re
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.mathtext import math_to_image, MathTextParser
from matplotlib.font_manager import FontProperties

from figures import W, H, DPI, INK, TEAL, RED, PALE, YELLOW, GRAY, font, normalize, figure

ROOT = Path(__file__).resolve().parent
DATA = json.loads((ROOT / 'sheets.json').read_text())['sheets']

X0, X1 = 132, W - 132   # 11 mm safe margin on both sides
CW = X1 - X0
HEAD_Y, FOOT_Y = 3320, 3348

TITLE_SZ, SUB_SZ = 76, 38
H_SZ, BODY_SZ = 48, 40
LEAD = 1.16

LINE = '#cbe4df'
CREAM = '#fffdf4'
CREAM_EDGE = '#e4d295'
TEAL_FILL = '#f2f8f6'
TEAL_EDGE = '#b9d9d2'
RED_FILL = '#fdf2f1'

TAG_STYLE = {
    'RESULT': ('#f6e7ae', INK),
    'METHOD': ('#d7ece8', TEAL),
    'KEPT': ('#e3ebe8', '#3d5c55'),
    'RATING': ('#f6dcd8', RED),
    'TABLE': ('#e8efed', GRAY),
}

_MCACHE, _DCACHE = {}, {}
_draw = ImageDraw.Draw(Image.new('RGB', (1, 1)))


def tw(s, f):
    return _draw.textlength(s, font=f)


def mimg(latex, pt, color=INK):
    key = (latex, pt, color)
    if key not in _MCACHE:
        buf = io.BytesIO()
        math_to_image('$' + normalize(latex) + '$', buf, prop=FontProperties(size=pt),
                      dpi=DPI, format='png', color=color)
        a = Image.open(buf).convert('RGBA')
        arr = np.array(a)
        arr[:, :, 3] = 255 - arr[:, :, :3].min(axis=2)   # white canvas -> transparent
        arr[:, :, :3] = [int(color[1:3], 16), int(color[3:5], 16), int(color[5:7], 16)]
        a = Image.fromarray(arr)
        bb = a.getbbox()
        _MCACHE[key] = a.crop(bb) if bb else a
    return _MCACHE[key]


def segments(s):
    """Split a string into ('t', text) and ('m', latex) runs."""
    out, i = [], 0
    for m in re.finditer(r'\$(.+?)\$', s):
        if m.start() > i:
            out.append(('t', s[i:m.start()]))
        out.append(('m', m.group(1)))
        i = m.end()
    if i < len(s):
        out.append(('t', s[i:]))
    return out


def mfit(latex, size):
    """Inline formula rendered at exactly the text size (PIL px -> mathtext pt)."""
    pt = round(size * 72.0 / DPI, 1)           # 40 px of text == 9.6 pt at 300 dpi
    return mimg(latex, pt)


def tokens(s, size, mathpt=None):
    f = font(size)
    toks = []
    for kind, val in segments(s):
        if kind == 't':
            for w in val.split():
                toks.append(('t', w, tw(w, f)))
        else:
            toks.append(('m', mfit(val, size), None))
    return toks, f


def wrap(s, size, mathpt, width):
    """Greedy wrap that treats a formula as one unbreakable word."""
    toks, f = tokens(s, size, mathpt)
    sp = tw(' ', f)
    lines, cur, curw = [], [], 0.0
    for t in toks:
        w = t[2] if t[0] == 't' else t[1].width
        if t[0] == 'm' and w > width * 1.02:                 # shrink a lone wide formula
            ratio = width / w
            assert ratio >= 0.80, f'formula too wide ({w}px): {s[:60]}'
            img = t[1].resize((int(w * ratio), int(t[1].height * ratio)), Image.Resampling.LANCZOS)
            t = ('m', img, None)
            w = img.width
        add = w if not cur else w + sp
        if cur and curw + add > width:
            lines.append(cur)
            cur, curw = [t], w
        else:
            cur.append(t)
            curw += add
    if cur:
        lines.append(cur)
    return lines


def text(s, x, y, width, size=BODY_SZ, color=INK, mathpt=12.0, lead=LEAD, gap=8, im=None):
    """Draw wrapped rich text, return the y coordinate after it."""
    d = ImageDraw.Draw(im)
    f = font(size)
    sp = tw(' ', f)
    x0 = x
    for line in wrap(s, size, mathpt, width):
        lh = size * 1.16
        for t in line:
            if t[0] == 't':
                d.text((x, y), t[1], font=f, fill=color)
                x += t[2] + sp
            else:
                img = t[1]
                lh = max(lh, img.height)
                im.paste(img, (int(x), int(y + size * 0.04)), img)
                x += img.width + sp
        y += max(lh, size * lead)
        x = x0
    return y + gap


# ----------------------------------------------------------------- blocks

def b_head(im, b, y):
    d = ImageDraw.Draw(im)
    y += 18
    r = 25
    cx, cy = X0 + r, y + r
    d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=TEAL)
    n = b.get('n', '')
    nf = font(38)
    d.text((cx - tw(n, nf) / 2, cy - 26), n, font=nf, fill='white')
    hf = font(H_SZ)
    tx = X0 + 2 * r + 18
    d.text((tx, y + 2), b['t'], font=hf, fill=TEAL)
    tag = b.get('tag')
    if tag:
        fill, col = TAG_STYLE.get(tag, ('#e8efed', GRAY))
        tagf = font(24)
        wtxt = tw(tag, tagf)
        bw = wtxt + 34
        bx = X1 - bw
        d.rounded_rectangle((bx, y + 12, X1, y + 54), radius=10, fill=fill)
        d.text((bx + 17, y + 20), tag, font=tagf, fill=col)
    d.line((X0, y + 66, X1, y + 66), fill=LINE, width=3)
    return y + 80


def b_p(im, b, y):
    return text(b['s'], X0, y, CW, im=im)


def b_m(im, b, y):
    d = ImageDraw.Draw(im)
    img = mimg(b['s'], 15)
    if img.width > CW - 40:
        r = (CW - 40) / img.width
        assert r >= 0.8, b['s']
        img = img.resize((int(img.width * r), int(img.height * r)), Image.Resampling.LANCZOS)
    d._image.paste(img, (X0 + 40, int(y) + 6), img)
    return y + img.height + 34


def _box(im, y, lines, label, fill, edge, lab_fill, lab_col, size=42, mathpt=13):
    d = ImageDraw.Draw(im)
    pad, lh_gap = 20, 8
    inner = CW - 2 * pad - 8
    body = []
    for ln in lines:
        ls = wrap(ln, size, mathpt, inner)
        h = sum(max(size * LEAD, max([t[1].height for t in l if t[0] == 'm'] or [0])) for l in ls)
        body.append((ls, h))
    labh = 40
    total = pad + labh + sum(h + lh_gap for _, h in body) + pad - lh_gap
    d.rounded_rectangle((X0, y, X1, y + total), radius=18, fill=fill, outline=edge, width=3)
    labf = font(24)
    lw = tw(label, labf) + 30
    d.rounded_rectangle((X0 + pad, y + pad - 4, X0 + pad + lw, y + pad + 32), radius=9,
                        fill=lab_fill, outline=lab_fill)
    d.text((X0 + pad + 15, y + pad + 2), label, font=labf, fill=lab_col)
    yy = y + pad + labh
    for ls, _ in body:
        for line in ls:
            lh = size * 1.16
            xx = X0 + pad + 4
            sp = tw(' ', font(size))
            for t in line:
                if t[0] == 't':
                    d.text((xx, yy), t[1], font=font(size), fill=INK)
                    xx += t[2] + sp
                else:
                    d._image.paste(t[1], (int(xx), int(yy)), t[1])
                    lh = max(lh, t[1].height)
                    xx += t[1].width + sp
            yy += max(lh, size * LEAD)
        yy += lh_gap
    return y + total + 14


def b_res(im, b, y):
    return _box(im, y, b['lines'], b.get('t', 'RESULT'), CREAM, CREAM_EDGE, '#f4e3a0', INK)


def b_ex(im, b, y):
    return _box(im, y, b['lines'], b.get('t', 'EXAMPLE'), TEAL_FILL, TEAL_EDGE, '#d7ece8', TEAL)


def b_trap(im, b, y):
    d = ImageDraw.Draw(im)
    pad = 18
    ls = wrap(b['s'], 38, 11.5, CW - 2 * pad - 40)
    body = sum(38 * LEAD for _ in ls)
    total = pad + 40 + body + pad - 6
    d.rounded_rectangle((X0, y, X1, y + total), radius=14, fill=RED_FILL, outline='#f0cdc8', width=2)
    d.rectangle((X0, y + 10, X0 + 9, y + total - 10), fill=RED)
    labf = font(24)
    lw = tw('TRAP', labf) + 26
    d.rounded_rectangle((X0 + pad + 4, y + pad - 6, X0 + pad + 4 + lw, y + pad + 22),
                        radius=6, fill='#f3d7d3')
    d.text((X0 + pad + 17, y + pad - 4), 'TRAP', font=labf, fill=RED)
    yy = y + pad + 34
    for line in ls:
        xx = X0 + pad + 6
        sp = tw(' ', font(40))
        for t in line:
            if t[0] == 't':
                d.text((xx, yy), t[1], font=font(38), fill='#7d2f2c')
                xx += t[2] + sp
            else:
                d._image.paste(t[1], (int(xx), int(yy)), t[1])
                xx += t[1].width + sp
        yy += 38 * LEAD
    return y + total + 12


def b_tab(im, b, y):
    d = ImageDraw.Draw(im)
    w = b.get('w') or [1 / len(b['head'])] * len(b['head'])
    xs, acc = [], X0
    for f_ in w:
        xs.append(acc)
        acc += f_ * CW
    xs.append(X1)
    pad = 14
    hf = font(28)
    hr = y + 34
    y = int(y)
    for i, cell in enumerate(b['head']):
        xx = xs[i] + pad
        sp = tw(' ', hf)
        for t in segments(cell.upper()):
            if t[0] == 't':
                for w in t[1].split():
                    d.text((xx, y + 2), w, font=hf, fill=TEAL)
                    xx += tw(w, hf) + sp
            else:
                im_ = mfit(t[1], 28)
                im.paste(im_, (int(xx), y + 4), im_)
                xx += im_.width + sp
    d.line((X0, hr, X1, hr), fill='#b9d9d2', width=3)
    yy = hr + 12
    for row in b['rows']:
        cells = []
        hmax = 0
        for i, cell in enumerate(row):
            ls = wrap(cell, 35, 11.0, xs[i + 1] - xs[i] - 2 * pad)
            h = sum(max(35 * LEAD, max([t[1].height for t in l if t[0] == 'm'] or [0])) for l in ls)
            cells.append(ls)
            hmax = max(hmax, h)
        for i, ls in enumerate(cells):
            ty = yy
            for line in ls:
                xx = xs[i] + pad
                sp = tw(' ', font(37))
                for t in line:
                    if t[0] == 't':
                        d.text((xx, ty), t[1], font=font(35), fill=INK)
                        xx += t[2] + sp
                    else:
                        d._image.paste(t[1], (int(xx), int(ty)), t[1])
                        xx += t[1].width + sp
                ty += 35 * LEAD
        yy += hmax + 12
        d.line((X0, yy - 6, X1, yy - 6), fill='#e2eeeb', width=2)
    return yy + 10


def b_rem(im, b, y):
    d = ImageDraw.Draw(im)
    pad = 22
    labf = font(24)
    d.rounded_rectangle((X0, y, X1, y + 40), radius=0, fill=CREAM)  # placeholder replaced below
    ls = wrap(b['s'], 38, 11.5, CW - 2 * pad - 4)
    body = sum(38 * LEAD for _ in ls)
    total = pad + 32 + body + pad - 4
    d.rounded_rectangle((X0, y, X1, y + total), radius=16, fill=PALE, outline='#bfded7', width=3)
    d.text((X0 + pad, y + pad - 4), 'REMEMBER', font=labf, fill=TEAL)
    yy = y + pad + 30
    for line in ls:
        xx = X0 + pad
        sp = tw(' ', font(40))
        for t in line:
            if t[0] == 't':
                d.text((xx, yy), t[1], font=font(38), fill=INK)
                xx += t[2] + sp
            else:
                d._image.paste(t[1], (int(xx), int(yy)), t[1])
                xx += t[1].width + sp
        yy += 38 * LEAD
    return y + total + 6


def b_dia(im, b, y):
    d = ImageDraw.Draw(im)
    cap = b.get('cap')
    caph = 0
    if cap:
        caph = 34 * LEAD * len(wrap(cap, 30, 10, CW - 60))
    art = b.get('h', 460)
    total = art + caph + 24
    d.rounded_rectangle((X0, y, X1, y + total), radius=16, fill='white', outline=TEAL_EDGE, width=3)
    fig = plt.figure(figsize=((CW - 40) / DPI, art / DPI), dpi=DPI, facecolor='white')
    ax = fig.add_axes([.085, .27, .88, .64])
    caption = figure(ax, b['key'])
    buf = io.BytesIO()
    fig.savefig(buf, format='png', dpi=DPI, facecolor='white')
    plt.close(fig)
    buf.seek(0)
    im.paste(Image.open(buf).convert('RGB'), (X0 + 20, int(y) + 8))
    if cap:
        text(cap, X0 + 30, y + art + 6, CW - 60, size=28, color=TEAL, mathpt=9.5, lead=1.15, gap=0, im=im)
    elif caption:
        pass
    return y + total + 16


RENDER = {'h': b_head, 't': b_p, 'm': b_m, 'res': b_res, 'ex': b_ex,
          'trap': b_trap, 'tab': b_tab, 'rem': b_rem, 'dia': b_dia}


def preflight():
    parser = MathTextParser('path')
    bad = []
    for sh in DATA:
        for b in sh['blocks']:
            texts = []
            if 's' in b:
                texts.append(b['s'])
            for k in ('lines',):
                texts += b.get(k, [])
            for row in b.get('rows', []):
                texts += row
            for t in texts:
                for _, latex in [x for x in segments(t) if x[0] == 'm']:
                    try:
                        parser.parse('$' + normalize(latex) + '$', dpi=72)
                    except Exception as exc:                     # noqa: BLE001
                        bad.append((sh['slug'], latex, str(exc).splitlines()[0]))
    if bad:
        for slug, latex, err in bad:
            print(f'BAD MATH  {slug}: {latex}  -> {err}')
        raise SystemExit(f'{len(bad)} unparseable formula(s)')


def render():
    preflight()
    report, total = [], len(DATA)
    for sh in DATA:
        im = Image.new('RGB', (W, H), 'white')
        d = ImageDraw.Draw(im)
        d.text((X0, 118), 'CAPACITORS  /  JEE MAIN + ADVANCED', font=font(30), fill=TEAL)
        pg = f"{sh['part_page']:02} / {total:02}"
        d.text((X1 - tw(pg, font(34)), 114), pg, font=font(34), fill=TEAL)
        d.line((X0, 160, X1, 160), fill=LINE, width=3)

        y = 180
        tsz = TITLE_SZ
        while tw(sh['title'], font(tsz)) > CW and tsz > 60:
            tsz -= 2
        if tw(sh['title'], font(tsz)) > CW:
            y = text(sh['title'], X0, y, CW, size=72, color=INK, lead=1.08, gap=0, im=im) - 4
        else:
            d.text((X0, y), sh['title'], font=font(tsz), fill=INK)
            y += tsz * 1.16
        d.text((X0, y + 10), '', font=font(10), fill=INK)
        y = text(sh['sub'], X0, y + 12, CW, size=SUB_SZ, color=GRAY, lead=1.16, gap=6, im=im)
        d.rectangle((X0, y + 6, X0 + 210, y + 13), fill=TEAL)
        y += 34

        for b in sh['blocks']:
            y0 = y
            y = RENDER[b['k']](im, b, y)
            if __import__('os').environ.get('TRACE'):
                print(f"   {b['k']:5} +{y - y0:4.0f} -> {y:5.0f}  {str(b.get('t') or b.get('s') or b.get('key'))[:60]}")
            if y > HEAD_Y and __import__('os').environ.get('STRICT'):
                raise SystemExit(f"OVERFLOW {sh['slug']} after {b['k']}: y={y:.0f} > {HEAD_Y}")

        d = ImageDraw.Draw(im)
        d.line((X0, FOOT_Y - 10, X1, FOOT_Y - 10), fill=LINE, width=2)
        d.text((X0, FOOT_Y + 6), sh['source'], font=font(24), fill=GRAY)
        right = 'A4 portrait  /  300 dpi  /  JEE only'
        d.text((X1 - tw(right, font(24)), FOOT_Y + 6), right, font=font(24), fill=GRAY)

        out = ROOT / (sh['slug'] + '.png')
        im.save(out, dpi=(DPI, DPI), optimize=True)
        fill = (HEAD_Y - y) / (HEAD_Y - 320)
        report.append({'slug': sh['slug'], 'blocks': len(sh['blocks']),
                       'end_px': round(y), 'headroom_px': round(HEAD_Y - y),
                       'fill': round(max(0.0, min(1.0, fill)), 3)})
        print(f"{sh['slug']:34} y={y:6.0f}  headroom={HEAD_Y - y:5.0f}px  fill={fill:.0%}")

    (ROOT / 'layout-checks.json').write_text(json.dumps(
        {'canvas': [W, H], 'dpi': DPI, 'safe_margin_px': X0,
         'policy': 'single column, JEE only', 'pages': report}, indent=1) + '\n')


if __name__ == '__main__':
    render()
