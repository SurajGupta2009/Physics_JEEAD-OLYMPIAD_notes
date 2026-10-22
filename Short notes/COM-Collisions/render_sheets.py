"""Render teacher-edited COM & Collisions notes into exact A4 PNGs (2480x3508, 300 dpi).
Dependencies: Pillow, matplotlib, numpy. Optional: imagequant for sharp 8-bit palettes.
"""
from pathlib import Path
import json, re, io, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.mathtext import math_to_image, MathTextParser
from matplotlib.font_manager import FontProperties, fontManager
from matplotlib.ft2font import FT2Font

try:
    import imagequant as _iq
except Exception:
    _iq = None

ROOT = Path(__file__).resolve().parent
FONT = ROOT / 'fonts/PatrickHand-Regular.ttf'
FALLBACK_FONT = Path(matplotlib.get_data_path()) / 'fonts/ttf/DejaVuSans.ttf'
fontManager.addfont(str(FONT))
plt.rcParams.update({
    'font.family': ['Patrick Hand', 'DejaVu Sans'],
    'font.size': 12,
    'mathtext.fontset': 'cm',
    'axes.labelcolor': '#153149',
    'text.color': '#153149',
    'axes.edgecolor': '#153149',
})
W, H, DPI = 2480, 3508, 300
INK = '#153149'
TEAL = '#087d7d'
RED = '#a43232'
PALE = '#eff8f5'
YELLOW = '#fff2b8'
GRAY = '#516875'
REPORT = []
CHARMAP = FT2Font(str(FONT)).get_charmap()


def font(size):
    return ImageFont.truetype(str(FONT), size)


def fallback_font(size):
    return ImageFont.truetype(str(FALLBACK_FONT), max(12, round(size * 0.76)))


def normalize(s):
    s = re.sub(r'\\sqrt(\\[A-Za-z]+)', r'\\sqrt{\1}', s)
    s = re.sub(r'\\sqrt\s*([0-9A-Za-z])(?![A-Za-z}])', r'\\sqrt{\1}', s)
    s = re.sub(r'\\(le|ge)(?![A-Za-z])', r'\\\1q', s)
    s = s.replace(r'\sqrt5', r'\sqrt{5}').replace(r'\hbox', r'\mathrm').replace(r'\frac1{', r'\frac{1}{')
    s = re.sub(r'\\(mathcal|mathbf|mathrm)\s+([A-Za-z])', r'\\\1{\2}', s)
    s = re.sub(r'([A-Za-z0-9|)\]}])\\(sin|cos|tan|cot|sec|csc|arcsin|arccos|arctan|sinh|cosh|tanh|ln|log|exp|det|lim|max|min)(?![A-Za-z])', r'\1\\,\2', s)
    return re.sub(r'\\(?:tfrac|frac)\s*([A-Za-z0-9])\s*([A-Za-z0-9])', r'\\frac{\1}{\2}', s)


def lines_for(s, f, width):
    out = []
    d = ImageDraw.Draw(Image.new('RGB', (1, 1)))
    for para in s.split('\n'):
        line = ''
        for word in para.split():
            candidate = (line + ' ' + word).strip()
            if d.textlength(candidate, font=f) > width and line:
                out.append(line)
                line = word
            else:
                line = candidate
        out.append(line)
    return out


def para_units(s):
    units = []
    for part in re.split(r'(\$[^$]+\$)', s):
        if len(part) > 2 and part[0] == '$' and part[-1] == '$':
            units.append(('m', part[1:-1]))
        elif part:
            for w in part.split():
                units.append(('t', w))
    return units


def _word_font(word, f, fb):
    return f if all(ord(c) in CHARMAP for c in word) else fb


def paragraph(im, s, x, y, width, size=48, color=INK, leading=56):
    d = ImageDraw.Draw(im)
    f = font(size)
    fb = fallback_font(size)
    imgs = {}
    for kind, val in para_units(s):
        if kind == 'm' and val not in imgs:
            a = math_image(val)
            if a.width > width:
                ratio = width / a.width
                assert ratio >= .60, f'Inline math too wide: {val}'
                a = a.resize((width, round(a.height * ratio)), Image.Resampling.LANCZOS)
            imgs[val] = a
    space = d.textlength(' ', font=f)
    for block in s.split('\n'):
        line = []
        lw = 0.0
        mh = 0

        def flush(line, lw, mh):
            nonlocal y
            LH = max(leading, mh + 12)
            cx = x
            ty = y + (LH - leading) // 2
            for kind, val in line:
                if kind == 't':
                    wf = _word_font(val, f, fb)
                    dy = 6 if wf is fb else 0
                    d.text((int(cx), int(ty + dy)), val, font=wf, fill=color)
                    cx += d.textlength(val, font=wf) + space
                else:
                    a = imgs[val]
                    iy = int(y + (LH - a.height) // 2)
                    ix = int(cx)
                    d.rounded_rectangle((ix - 5, iy - 4, ix + a.width + 5, iy + a.height + 4), radius=9, fill=YELLOW)
                    im.paste(a, (ix, iy), a)
                    cx += a.width + space
            y += LH

        for kind, val in para_units(block):
            if kind == 't':
                wf = _word_font(val, f, fb)
                w = d.textlength(val, font=wf) + space
                h = round(size * 0.6)
            else:
                w = imgs[val].width + space
                h = imgs[val].height
            if lw + w > width and line:
                flush(line, lw, mh)
                line = []
                lw = 0.0
                mh = 0
            line.append((kind, val))
            lw += w
            mh = max(mh, h)
        if line:
            flush(line, lw, mh)
        elif not block.strip():
            y += leading
    return y


MATH_CACHE = {}


def math_image(s):
    if s not in MATH_CACHE:
        b = io.BytesIO()
        math_to_image('$' + normalize(s) + '$', b, prop=FontProperties(size=12), dpi=DPI, format='png', color=INK)
        a = Image.open(b).convert('RGBA')
        arr = np.array(a)
        arr[:, :, 3] = 255 - arr[:, :, :3].min(axis=2)
        arr[:, :, :3] = [21, 49, 73]
        a = Image.fromarray(arr)
        bbox = a.getbbox()
        a = a.crop(bbox) if bbox else a
        MATH_CACHE[s] = a
    return MATH_CACHE[s].copy()


def card(im, c, x, y, width=1090, height=1040):
    d = ImageDraw.Draw(im)
    d.rounded_rectangle((x, y, x + width, y + height), radius=24, fill='white', outline='#bbd9d4', width=3)
    d.rounded_rectangle((x, y, x + width, y + 94), radius=24, fill=PALE)
    d.rectangle((x, y + 55, x + width, y + 94), fill=PALE)
    titlefont = font(56)
    while d.textlength(c['title'], font=titlefont) > width - 56 and titlefont.size > 38:
        titlefont = font(titlefont.size - 2)
    assert d.textlength(c['title'], font=titlefont) <= width - 56, f'Card title too wide: {c["title"]}'
    d.text((x + 24, y + 12 + (56 - titlefont.size) // 2), c['title'], font=titlefont, fill=TEAL)
    yy = y + 104
    bodyw = width - 58
    for kind, s in c['items']:
        if kind == 'm':
            a = math_image(s)
            if a.width > bodyw:
                ratio = bodyw / a.width
                assert ratio >= .80, f'Equation too wide: {c["title"]}: {s}'
                a = a.resize((bodyw, round(a.height * ratio)), Image.Resampling.LANCZOS)
            d.rounded_rectangle((x + 24, yy - 5, x + width - 24, yy + a.height + 10), radius=9, fill=YELLOW)
            im.paste(a, (x + 36, yy + 2), a)
            yy += a.height + 18
        else:
            fs = 46 if kind in ('why', 'trap', 'check') else 48
            lead = 53 if kind in ('why', 'trap', 'check') else 56
            label = 'WHY / ' if kind == 'why' else 'WATCH / ' if kind == 'trap' else 'CHECK / ' if kind == 'check' else ''
            color = TEAL if kind in ('why', 'check') else RED if kind == 'trap' else INK
            yy = paragraph(im, label + s, x + 30, yy, bodyw, size=fs, color=color, leading=lead) + 8
    used = yy - y
    assert used < height - 10, f'CARD OVERFLOW ({used}px): {c["title"]}'
    REPORT.append({'card': c['title'], 'used_px': round(used), 'available_px': height, 'body_pt': 11.52, 'explanation_pt': 11.04})


from diagrams import figure


def diagram(im, key, x, y, width=1090, height=610):
    fig = plt.figure(figsize=(width / DPI, (height - 115) / DPI), dpi=DPI, facecolor='white')
    ax = fig.add_axes([.23, .34, .72, .55])
    caption = figure(ax, key)
    if not ax.axison:
        ax.set_position([.035, .08, .93, .80])
    else:
        ax.set_aspect('auto')
    fig.canvas.draw()
    renderer = fig.canvas.get_renderer()
    for artist in list(ax.texts) + ([ax.xaxis.label, ax.yaxis.label] + [t for t in ax.get_xticklabels() if ax.get_xlim()[0] <= t.get_position()[0] <= ax.get_xlim()[1]] + [t for t in ax.get_yticklabels() if ax.get_ylim()[0] <= t.get_position()[1] <= ax.get_ylim()[1]] if ax.axison else []):
        if not artist.get_visible() or not artist.get_text():
            continue
        bb = artist.get_window_extent(renderer)
        assert bb.x0 >= 0 and bb.y0 >= 0 and bb.x1 <= width and bb.y1 <= height - 115, f'Diagram text clipped: {key}: {artist.get_text()} {bb}'
    if ax.axison:
        ticks = [t.get_window_extent(renderer) for t in ax.get_xticklabels() if t.get_visible() and t.get_text()]
        for left, right in zip(ticks, ticks[1:]):
            assert left.x1 + 2 < right.x0, f'Overlapping x tick labels: {key}'
        leg = ax.get_legend()
        if leg:
            bb = leg.get_window_extent(renderer)
            assert bb.x0 >= 0 and bb.y0 >= 0 and bb.x1 <= width and bb.y1 <= height - 115, f'Legend clipped: {key}'
    b = io.BytesIO()
    fig.savefig(b, format='png', dpi=DPI, facecolor='white')
    plt.close(fig)
    a = Image.open(b).convert('RGB')
    im.paste(a, (x, y + 115))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle((x, y, x + width, y + height), radius=18, outline='#bbd9d4', width=3)
    f = font(40)
    captionlines = lines_for(caption, f, width - 45)
    assert len(captionlines) <= 2, f'Caption overflow: {caption}'
    for j, line in enumerate(captionlines):
        d.text((x + 22, y + 10 + j * 43), line, font=f, fill=TEAL)


def save_indexed_png(im, out):
    if _iq is not None:
        q = _iq.quantize_pil_image(im, dithering_level=0.0, max_colors=24)
    else:
        q = im.quantize(colors=64, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE)
    pal = list(q.getpalette())
    if len(pal) < 768:
        pal.extend([0] * (768 - len(pal)))
    # Ensure white (255,255,255) sits at palette index 255 for clean 8-bit indexed streams.
    w_idx = None
    for idx in range(256):
        if pal[3 * idx:3 * idx + 3] == [255, 255, 255]:
            w_idx = idx
            break
    arr = np.array(q, dtype=np.uint8)
    if w_idx is not None and w_idx != 255:
        pal[3 * w_idx:3 * w_idx + 3], pal[765:768] = pal[765:768], pal[3 * w_idx:3 * w_idx + 3]
        swapped = arr.copy()
        swapped[arr == w_idx] = 255
        swapped[arr == 255] = w_idx
        arr = swapped
    out_im = Image.fromarray(arr, mode='P')
    out_im.putpalette(pal[:768])
    out_im.save(out, dpi=(DPI, DPI), optimize=True)


def render(only_slugs=None):
    data = json.loads((ROOT / 'sheets.json').read_text())
    REPORT.clear()
    part_counts = {key: sum(p['section'] == key for p in data) for key in ('JEE', 'Olympiad')}
    parser = MathTextParser('path')
    for p in data:
        for c in p['cards']:
            for kind, s in c['items']:
                if kind == 'm':
                    parser.parse('$' + normalize(s) + '$', dpi=72)
    for i, p in enumerate(data, 1):
        if only_slugs and p['slug'] not in only_slugs:
            continue
        im = Image.new('RGB', (W, H), 'white')
        d = ImageDraw.Draw(im)
        label = 'PART I: JEE MAIN + ADVANCED' if p['section'] == 'JEE' else 'PART II: OLYMPIAD / EXTENSIONS'
        d.text((125, 125), 'COM & COLLISIONS  /  ' + label, font=font(30), fill=TEAL)
        d.text((2160, 125), f"{p['part_page']:02}/{part_counts[p['section']]:02}", font=font(42), fill=TEAL)
        fs = 88
        while d.textlength(p['title'], font=font(fs)) > W - 258:
            fs -= 1
        assert fs >= 64, f'Sheet title too long: {p["title"]}'
        d.text((129, 165), p['title'], font=font(fs), fill=INK)
        d.line((125, 270, W - 125, 270), fill=TEAL, width=5)
        paragraph(im, p['subtitle'], 129, 286, W - 258, size=44, leading=52)
        for c, (xx, yy) in zip(p['cards'], [(125, 405), (1265, 405), (125, 1465), (1265, 1465)]):
            card(im, c, xx, yy)
        for key, xx in zip(p['diagrams'], [125, 1265]):
            diagram(im, key, xx, 2540)
        d = ImageDraw.Draw(im)
        d.rounded_rectangle((125, 3200, W - 125, 3345), radius=20, fill=PALE)
        rem_end = paragraph(im, 'REMEMBER / ' + p['takeaway'], 150, 3218, W - 300, size=44, leading=52)
        assert rem_end <= 3342, f'REMEMBER overflow ({rem_end}): {p["slug"]}'
        d.text((125, 3352), p['source'], font=font(28), fill=GRAY)
        d.text((1740, 3352), 'A4 portrait  /  300 DPI', font=font(28), fill=GRAY)
        out = ROOT / (p['slug'] + '.png')
        out.parent.mkdir(parents=True, exist_ok=True)
        save_indexed_png(im, out)
        print(f"{i:02}/{len(data)}  {p['slug']}.png", flush=True)
    if not only_slugs:
        expected = {p['slug'] + '.png' for p in data}
        for section in ('JEE', 'Olympiad'):
            for old in ROOT.glob(section + '-[0-9][0-9]-*.png'):
                if str(old.relative_to(ROOT)) not in expected:
                    old.unlink()
        (ROOT / 'layout-checks.json').write_text(json.dumps({
            'canvas': [W, H], 'dpi': DPI, 'safe_margin_px': 125, 'cards': REPORT,
        }, indent=2) + '\n')


if __name__ == '__main__':
    render(set(sys.argv[1:]) if len(sys.argv) > 1 else None)
