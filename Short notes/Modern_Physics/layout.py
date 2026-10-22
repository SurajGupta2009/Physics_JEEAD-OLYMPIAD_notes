"""Layout engine v2 for the modern-physics short-note sheets.

Why this is not the old four-card grid
--------------------------------------
The Elasticity edition put four equal boxes on every page. That format forces
short topics to leave holes and long topics to be trimmed, and it parks the
figures in a strip far from the sentence that needs them.

This engine lays a page out the way a teacher fills a sheet of paper:

    header:  topic  ·  the QUESTION this page answers
    ────────────────────────────────────────────────────────────────
    spine │  main column: the argument, one numbered move at a time
     (1)  │  prose, equations on yellow bars, small check lines
     (2)  │                                   │ margin rail: chips for
     (3)  │                                   │ DEFINE / KEY / GATE /
          │                                   │ TRAP / NUMBER / CHECK
    ────────────────────────────────────────────────────────────────
    figure band: one large figure, or two
    ────────────────────────────────────────────────────────────────
    carry line: the single sentence to leave with

The spine gives an explicit reading order, the margin keeps warnings next to
the step they belong to, and each sheet reserves only as much height as it
uses: a move that needs four lines takes four lines.
"""
from pathlib import Path
import io, json, math, re

import numpy as np
from PIL import Image, ImageDraw, ImageFont
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.mathtext import math_to_image, MathTextParser
from matplotlib.font_manager import FontProperties, fontManager
from matplotlib.ft2font import FT2Font

ROOT = Path(__file__).resolve().parent
FONT = ROOT / 'fonts/PatrickHand-Regular.ttf'
fontManager.addfont(str(FONT))
plt.rcParams.update({'font.family': ['Patrick Hand', 'DejaVu Sans'], 'font.size': 12,
                     'mathtext.fontset': 'cm', 'axes.labelcolor': '#153149',
                     'text.color': '#153149', 'axes.edgecolor': '#153149'})

W, H, DPI = 2480, 3508, 300
M = 125                              # safe margin, 10.6 mm
INK = '#153149'
TEAL = '#087d7d'
RED = '#a43232'
GOLD = '#8a6a10'
GRAY = '#516875'
PALE = '#eff8f5'
YELLOW = '#fff2b8'
REDPALE = '#fbeceb'
TEALPALE = '#e7f4f1'
WATER = '#e8f3f8'

# ----------------------------------------------------------------- geometry
BODY_TOP = 416
BODY_BOTTOM = 2478
SPINE_X = 200
MAIN_X, MAIN_W = 330, 1196
MARG_X, MARG_W = 1580, 780
FIG_MIN_Y = 2310
CARRY_Y = 3220
FOOT_Y = 3388

BODY_SIZE, BODY_LEAD = 45, 56       # 10.8 pt equivalent at 300 dpi
MOVE_SIZE = 51
CHIP_LABEL, CHIP_TITLE, CHIP_SIZE, CHIP_LEAD = 27, 38, 40, 49

CHARMAP = FT2Font(str(FONT)).get_charmap()
FALLBACK = Path(matplotlib.get_data_path()) / 'fonts/ttf/DejaVuSans.ttf'
FBCHARS = FT2Font(str(FALLBACK)).get_charmap()
MATH_CACHE = {}
_FONTS = {}

# Patrick Hand has no Greek letters, subscripts or relation symbols. Those
# glyphs are set in DejaVu Sans at a slightly smaller nominal size so their
# cap height matches the handwriting; equations keep their own CM mathtext.
FB_SCALE = 0.92


def font(size, fallback=False):
    key = (size, fallback)
    if key not in _FONTS:
        _FONTS[key] = ImageFont.truetype(
            str(FALLBACK) if fallback else str(FONT),
            max(1, round(size * FB_SCALE)) if fallback else size)
    return _FONTS[key]


_MEASURE = ImageDraw.Draw(Image.new('RGB', (1, 1)))


def runs(s, size):
    out = []
    for ch in s:
        fb = ord(ch) not in CHARMAP
        assert (not fb) or ord(ch) in FBCHARS, f'No glyph for {ch!r} in either face'
        if out and out[-1][1] == fb:
            out[-1][0] += ch
        else:
            out.append([ch, fb])
    return [(t, font(size, fb)) for t, fb in out]


_SUBS = set('₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎')
_SUPS = set('⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾')
_SUB_TR = str.maketrans('₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎', '0123456789+-=()')
_SUP_TR = str.maketrans('⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾', '0123456789+-=()')


def _script_runs(s):
    out = []
    for ch in s:
        kind = 'sub' if ch in _SUBS else ('sup' if ch in _SUPS else 'norm')
        if out and out[-1][1] == kind:
            out[-1][0] += ch
        else:
            out.append([ch, kind])
    return out


def line_len(s, size):
    total = 0.0
    for seg, kind in _script_runs(s):
        if kind == 'sub':
            f2 = font(max(1, round(size * .64)), fallback=False)
            total += _MEASURE.textlength(seg.translate(_SUB_TR), font=f2)
        elif kind == 'sup':
            f2 = font(max(1, round(size * .64)), fallback=False)
            total += _MEASURE.textlength(seg.translate(_SUP_TR), font=f2)
        else:
            total += sum(_MEASURE.textlength(t, font=f) for t, f in runs(seg, size))
    return total


def draw_line(im, s, x, y, size, color=INK):
    """Set subscripts/superscripts cleanly in Patrick Hand; Greek/math symbols in DejaVu."""
    d = ImageDraw.Draw(im)
    for seg, kind in _script_runs(s):
        if kind == 'sub':
            txt = seg.translate(_SUB_TR)
            f2 = font(max(1, round(size * .64)), fallback=False)
            d.text((x, y + size * .36), txt, font=f2, fill=color)
            x += d.textlength(txt, font=f2)
        elif kind == 'sup':
            txt = seg.translate(_SUP_TR)
            f2 = font(max(1, round(size * .64)), fallback=False)
            d.text((x, y - size * .06), txt, font=f2, fill=color)
            x += d.textlength(txt, font=f2)
        else:
            for t, f in runs(seg, size):
                adv = d.textlength(t, font=f)
                d.text((x, y), t, font=f, fill=color)
                x += adv


def _rm(m):
    return r'\mathrm{' + m.group(1).replace(' ', r'\ ') + '}'


def normalize(s):
    """mathtext lacks \\tfrac/\\Big/pmatrix; also keeps words inside \\text spaced."""
    s = re.sub(r'\\sqrt([0-9])', r'\\sqrt{\1}', s)
    s = re.sub(r'\\(le|ge)(?![A-Za-z])', r'\\\1q', s)
    s = re.sub(r'\\(?:text|hbox|textrm)\{([^{}]*)\}', _rm, s)
    s = s.replace(r'\hbox', r'\mathrm')
    s = re.sub(r'\\(?:tfrac|dfrac)\s*', r'\\frac', s)
    s = re.sub(r'\\(mathcal|mathbf|mathrm)\s+([A-Za-z])', r'\\\1{\2}', s)
    s = re.sub(r'\\frac\s*([A-Za-z0-9])\s*([A-Za-z0-9])', r'\\frac{\1}{\2}', s)
    return s


def lines_for(s, size, width):
    out = []
    for para in s.split('\n'):
        line = ''
        for word in para.split():
            cand = (line + ' ' + word).strip()
            if line_len(cand, size) > width and line:
                out.append(line)
                line = word
            else:
                line = cand
        out.append(line)
    return out


def text_height(s, size, width, leading):
    return len(lines_for(s, size, width)) * leading


def text_block(im, s, x, y, width, size=BODY_SIZE, leading=BODY_LEAD, color=INK):
    for line in lines_for(s, size, width):
        assert line_len(line, size) <= width + 1, f'Unwrappable line: {line}'
        draw_line(im, line, x, y, size, color)
        y += leading
    return y


def math_image(s, size=12.0):
    key = (normalize(s), size)
    if key not in MATH_CACHE:
        b = io.BytesIO()
        math_to_image('$' + key[0] + '$', b, prop=FontProperties(size=size),
                      dpi=DPI, format='png', color=INK)
        a = Image.open(b).convert('RGBA')
        arr = np.array(a)
        arr[:, :, 3] = 255 - arr[:, :, :3].min(axis=2)
        arr[:, :, :3] = [21, 49, 73]
        a = Image.fromarray(arr)
        bbox = a.getbbox()
        MATH_CACHE[key] = a.crop(bbox) if bbox else a
    return MATH_CACHE[key].copy()


def eq_height(tex, width, size=12.0):
    a = math_image(tex, size)
    if a.width > width:
        return round(a.height * width / a.width) + 30
    return a.height + 30


def eq_block(im, tex, x, y, width, tag=None, size=12.0):
    """Equation on a soft yellow bar, optional right-aligned tag like (3.7)."""
    a = math_image(tex, size)
    d = ImageDraw.Draw(im)
    tagw = 0
    h = a.height + 26
    if tag:
        tagw = 110
    inner = width - 26 - tagw
    if a.width > inner:
        ratio = inner / a.width
        assert ratio >= .82, f'Equation too wide ({ratio:.2f}): {tex}'
        a = a.resize((inner, max(1, round(a.height * ratio))), Image.Resampling.LANCZOS)
    h = a.height + 26
    d.rounded_rectangle((x, y, x + width, y + h), radius=8, fill=YELLOW)
    im.paste(a, (x + 18, y + 13), a)
    if tag:
        d.text((x + width - 100, y + 8), tag, font=font(30), fill=GOLD)
    return y + h + 16


def rule(im, x0, x1, y, color=TEAL, width=3):
    ImageDraw.Draw(im).line((x0, y, x1, y), fill=color, width=width)


# ---------------------------------------------------------- energy scale bar
BANDS = [(1e-1, 1e2, '#dcefeb'),      # atomic / optical, eV
         (1e2, 1e5, '#fdf0bd'),       # X-ray, 100 eV - 100 keV
         (1e5, 1e7, '#f6dedb')]       # nuclear, 0.1 - 10 MeV
EV_LO, EV_HI = 1e-1, 1e7


def _ev_label(ev):
    if ev >= 1e6:
        return f'{ev/1e6:g} MeV'
    if ev >= 1e3:
        return f'{ev/1e3:g} keV'
    if ev >= 1:
        return f'{ev:g} eV'
    return f'{ev*1e3:g} meV'


def scale_bar(im, ev, x, y, w=620, h=13):
    """Where this page sits on the chapter's eight-decade energy ladder.

    eV / keV / MeV are three bands of a log axis from 0.1 eV to 10 MeV, with a
    marker and a named label; the bar is the chapter's spine, repeated on every
    page, so the reader always knows which decade the sheet lives in.
    """
    d = ImageDraw.Draw(im)
    lo, hi = math.log10(EV_LO), math.log10(EV_HI)
    for a, b, c in BANDS:
        x0 = x + w * (math.log10(a) - lo) / (hi - lo)
        x1 = x + w * (math.log10(b) - lo) / (hi - lo)
        d.rectangle((x0, y, x1, y + h), fill=c)
    d.rectangle((x, y, x + w, y + h), outline='#cfe1dc', width=2)
    d.text((x, y + h + 4), '0.1 eV', font=font(20), fill='#8fa3ad')
    d.text((x + w - 74, y + h + 4), '10 MeV', font=font(20), fill='#8fa3ad')
    lab = _ev_label(ev)
    t = (math.log10(ev) - lo) / (hi - lo)
    t = min(max(t, 0.015), 0.975)
    mx = x + w * t
    d.polygon([(mx, y - 1), (mx - 8, y - 13), (mx + 8, y - 13)], fill=TEAL)
    tw = d.textlength(lab, font=font(22))
    lx = mx + 12 if mx < x + w * .72 else mx - 12 - tw
    d.text((lx, y - 18), lab, font=font(22), fill=TEAL)


def _banner(section):
    return ('PART I  ·  JEE MAIN + ADVANCED' if section == 'JEE'
            else 'PART II  ·  OLYMPIAD + EXTENSIONS')


# ------------------------------------------------------------------- figure
from diagrams import figure as draw_figure   # noqa: E402


def figure_block(im, key, x, y, width=1090, height=900):
    fig = plt.figure(figsize=(width / DPI, (height - 78) / DPI), dpi=DPI, facecolor='white')
    ax = fig.add_axes([.03, .05, .94, .84])
    caption = draw_figure(ax, key)
    fig.canvas.draw()
    r = fig.canvas.get_renderer()
    for a in fig.axes:
        artists = list(a.texts) + [a.xaxis.label, a.yaxis.label]
        if a.axison:
            artists += [t for t in a.get_xticklabels()
                        if a.get_xlim()[0] <= t.get_position()[0] <= a.get_xlim()[1]]
            artists += [t for t in a.get_yticklabels()
                        if a.get_ylim()[0] <= t.get_position()[1] <= a.get_ylim()[1]]
        for art in artists:
            if not art.get_visible() or not art.get_text():
                continue
            bb = art.get_window_extent(r)
            assert bb.x0 >= -1 and bb.y0 >= -1 and bb.x1 <= width + 1 and bb.y1 <= height - 77, \
                f'Diagram text clipped: {key}: {art.get_text()!r} at {bb}'
    b = io.BytesIO()
    fig.savefig(b, format='png', dpi=DPI, facecolor='white')
    plt.close(fig)
    a = Image.open(b).convert('RGB')
    im.paste(a, (x, y + 78))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle((x, y, x + width, y + height), radius=14, outline='#cfe1dc', width=2)
    for j, line in enumerate(lines_for(caption, 38, width - 40)[:2]):
        draw_line(im, line, x + 20, y + 8 + j * 41, 38, TEAL)
    return y + height


# --------------------------------------------------------------------- page
class Sheet:
    """A page under construction. add_move / add_chip / add_figure, then save()."""

    def __init__(self, slug, title, question, kicker, page_no, page_total,
                 source, carry, section='JEE', scale=10.0):
        self.slug = slug
        self.section = section
        self.scale = scale
        self.title = title
        self.question = question
        self.kicker = kicker
        self.page_no = page_no
        self.page_total = page_total
        self.source = source
        self.carry = carry
        self.moves = []
        self.chips = []
        self.figures = []
        self.report = []

    # -- content -----------------------------------------------------------
    def move(self, heading, blocks):
        """blocks: ('m', tex[, tag]) | ('p', prose) | ('n', one-line aside)"""
        self.moves.append((heading, blocks))
        return self

    def chip(self, kind, title, blocks):
        assert kind in ('def', 'key', 'gate', 'trap', 'num', 'check', 'insight'), kind
        self.chips.append((kind, title, blocks))
        return self

    def figure(self, key):
        self.figures.append(key)
        return self

    # -- measurement -------------------------------------------------------
    def _move_height(self, heading, blocks):
        h = 6
        for b in blocks:
            if b[0] == 'm':
                h += eq_height(b[1], MAIN_W - 20)
            elif b[0] == 'p':
                h += text_height(b[1], BODY_SIZE, MAIN_W, BODY_LEAD) + 12
            elif b[0] == 'n':
                h += text_height(b[1], 38, MAIN_W, 46) + 12
        return h + text_height(heading, MOVE_SIZE, MAIN_W - 60, 58) + 22

    def _chip_height(self, kind, title, blocks):
        h = 20 + CHIP_LEAD + 8                     # padding + title
        for b in blocks:
            if b[0] == 'm':
                h += eq_height(b[1], MARG_W - 44, 10.6)
            else:
                h += text_height(b[1], CHIP_SIZE, MARG_W - 44, CHIP_LEAD) + 8
        return h + 16

    # -- drawing -----------------------------------------------------------
    def save(self):
        im = Image.new('RGB', (W, H), 'white')
        d = ImageDraw.Draw(im)

        # header ----------------------------------------------------------
        d.text((M, 86), self.kicker, font=font(27), fill=TEAL)
        pn = f'{self.page_no:02}/{self.page_total:02}'
        d.text((W - M - d.textlength(pn, font=font(42)), 84), pn, font=font(42), fill=TEAL)
        scale_bar(im, self.scale, M, 148, w=560)
        fs = 78
        while line_len(self.title, fs) > W - 2 * M - 120 and fs > 60:
            fs -= 2
        assert fs >= 60 and line_len(self.title, fs) <= W - 2 * M, \
            f'Title too long: {self.title}'
        draw_line(im, self.title, M, 196, fs, INK)

        qlines = lines_for(self.question, 41, W - 2 * M - 60)
        assert len(qlines) <= 2, f'Question too long: {self.question}'
        d.text((M, 300), '?', font=font(42), fill=TEAL)
        paragraph_end = text_block(im, self.question, M + 42, 300, W - 2 * M - 60,
                                   size=41, leading=49, color=TEAL)
        rule(im, M, W - M, max(404, paragraph_end + 4), width=4)

        # body ------------------------------------------------------------
        body_top = BODY_TOP
        y = body_top
        spine_points = []
        for i, (heading, blocks) in enumerate(self.moves, 1):
            hh = text_height(heading, MOVE_SIZE, MAIN_W - 60, 58)
            # spine marker
            cy = y + 26
            spine_points.append(cy)
            d.ellipse((SPINE_X - 27, cy - 27, SPINE_X + 27, cy + 27),
                      fill='white', outline=TEAL, width=3)
            num = str(i)
            d.text((SPINE_X - d.textlength(num, font=font(34)) / 2, cy - 21),
                   num, font=font(34), fill=TEAL)
            d.line((SPINE_X + 30, cy, MAIN_X - 14, cy), fill='#cfe1dc', width=2)
            y = text_block(im, heading, MAIN_X, y, MAIN_W - 60, size=MOVE_SIZE,
                           leading=58, color=TEAL) + 8
            for b in blocks:
                if b[0] == 'm':
                    y = eq_block(im, b[1], MAIN_X, y, MAIN_W, b[2] if len(b) > 2 else None)
                elif b[0] == 'p':
                    y = text_block(im, b[1], MAIN_X, y, MAIN_W) + 12
                else:
                    y = text_block(im, '→ ' + b[1], MAIN_X, y, MAIN_W, size=38,
                                   leading=46, color=GRAY) + 12
            y += 16
        used = y - body_top
        assert used <= BODY_BOTTOM - body_top, \
            f'MAIN COLUMN OVERFLOW on {self.slug}: {used}px of {BODY_BOTTOM - body_top}px'
        self.report.append({'sheet': self.slug, 'scale_eV': self.scale, 'main_px': round(used),
                            'main_available': BODY_BOTTOM - body_top})

        # spine line, drawn under the markers
        if len(spine_points) > 1:
            d.line((SPINE_X, spine_points[0] + 30, SPINE_X, spine_points[-1] - 30),
                   fill='#cfe1dc', width=3)

        # margin chips ----------------------------------------------------
        my = body_top
        for kind, title, blocks in self.chips:
            ch = self._chip_height(kind, title, blocks)
            assert my + ch <= BODY_BOTTOM, \
                f'MARGIN OVERFLOW on {self.slug} at chip "{title}": {my + ch}px'
            fill, edge, lab = {
                'key': (YELLOW, '#e6cf7a', GOLD),
                'gate': (TEALPALE, '#9ccdc4', TEAL),
                'trap': (REDPALE, '#e3b4b0', RED),
                'def': ('white', '#cfe1dc', TEAL),
                'num': ('white', '#c9d8dc', GRAY),
                'check': (TEALPALE, '#9ccdc4', TEAL),
                'insight': ('#fdf6e3', '#e0cd93', GOLD),
            }[kind]
            d.rounded_rectangle((MARG_X, my, MARG_X + MARG_W, my + ch), radius=14,
                                fill=fill, outline=edge, width=3)
            d.text((MARG_X + 22, my + 14), {'key': 'KEY RESULT', 'gate': 'GATE',
                                            'trap': 'TRAP', 'def': 'DEFINE',
                                            'num': 'NUMBERS', 'check': 'CHECK',
                                            'insight': 'INSIGHT'}[kind],
                   font=font(CHIP_LABEL), fill=lab)
            d.rectangle((MARG_X + 1, my + 52, MARG_X + 5, my + ch - 1), fill=edge)
            cy = my + 48
            cy = text_block(im, title, MARG_X + 22, cy, MARG_W - 44,
                            size=CHIP_TITLE, leading=46, color=lab)
            for b in blocks:
                if b[0] == 'm':
                    cy = eq_block(im, b[1], MARG_X + 20, cy + 2, MARG_W - 40, size=10.6)
                else:
                    cy = text_block(im, b[1], MARG_X + 22, cy, MARG_W - 44,
                                    size=CHIP_SIZE, leading=CHIP_LEAD) + 8
            my += ch + 22
        self.report.append({'sheet': self.slug, 'margin_px': round(my - body_top),
                            'margin_available': BODY_BOTTOM - body_top})

        # figures ---------------------------------------------------------
        assert 1 <= len(self.figures) <= 2, f'{self.slug}: 1-2 figures'
        # the figure band is a fixed slot: every page's diagrams share one
        # canvas size, so type size and label clearance are identical on all 30
        assert y + 26 <= FIG_MIN_Y, (
            f'{self.slug}: body reaches y={y:.0f}, into the figure band at {FIG_MIN_Y}')
        fy = FIG_MIN_Y
        fh = CARRY_Y - 24 - fy
        self.report[-1]['figure_y'] = round(fy)
        self.report[-1]['figure_h'] = round(fh)
        if len(self.figures) == 1:
            figure_block(im, self.figures[0], M, fy, width=W - 2 * M, height=fh)
        else:
            figure_block(im, self.figures[0], M, fy, width=1090, height=fh)
            figure_block(im, self.figures[1], M + 1160, fy, width=1090, height=fh)

        # carry + footer ---------------------------------------------------
        d.rounded_rectangle((M, CARRY_Y, W - M, CARRY_Y + 104), radius=16, fill=PALE)
        text_block(im, 'KEEP  /  ' + self.carry, M + 24, CARRY_Y + 18, W - 2 * M - 50,
                   size=42, leading=50, color=INK)
        d.text((M, FOOT_Y), self.source, font=font(26), fill=GRAY)
        right = 'A4 portrait  /  300 DPI  /  2480 x 3508'
        d.text((W - M - d.textlength(right, font=font(26)), FOOT_Y), right,
               font=font(26), fill=GRAY)

        out = ROOT / (self.slug + '.png')
        assert out.parent.exists(), out
        im = im.quantize(colors=256, method=Image.MEDIANCUT, dither=Image.NONE)
        im.save(out, dpi=(DPI, DPI), optimize=True)
        return out


def preflight(sheets):
    """Parse every equation before spending minutes on rendering."""
    parser = MathTextParser('path')
    for s in sheets:
        for _, blocks in s.moves:
            for b in blocks:
                if b[0] == 'm':
                    parser.parse('$' + normalize(b[1]) + '$', dpi=72)
        for _, _, blocks in s.chips:
            for b in blocks:
                if b[0] == 'm':
                    parser.parse('$' + normalize(b[1]) + '$', dpi=72)
