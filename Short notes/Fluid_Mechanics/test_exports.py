"""Run after author_content.py and build_exports.py.

Checks page structure and typography, the PNG canvas, the three PDFs and ZIPs,
the gallery links, and a representative set of physics numbers recomputed from
the formulas printed on the sheets.  It is representative, not a proof of every
line on every sheet.
"""
from pathlib import Path
import hashlib, json, math, re, zipfile
from urllib.parse import unquote, urlsplit

from PIL import Image
from pypdf import PdfReader
from matplotlib.ft2font import FT2Font

from build_exports import ROOT, PDFS, ZIPS

checks = 0
models = []


def check(ok, message):
    global checks
    checks += 1
    assert ok, message


def near(name, value, target, rel=.02, absolute=1e-9):
    check(abs(value - target) <= max(absolute, rel * abs(target)), f'{name}: {value} vs {target}')
    models.append({'name': name, 'value': float(value), 'expected': float(target)})


def main():
    data = json.loads((ROOT / 'sheets.json').read_text())['sheets']
    jee = [p for p in data if p['section'] == 'JEE']
    oly = [p for p in data if p['section'] == 'Olympiad']
    check(len(data) == 30, 'page count')
    check((len(jee), len(oly)) == (19, 11), 'part sizes')
    check([p['slug'] for p in data] == [p['slug'] for p in jee + oly], 'reading order')
    check(len({p['slug'] for p in data}) == 30, 'unique slugs')
    check(all(p['slug'].startswith(p['section'] + '-') for p in data), 'section prefix')
    check(all('/' not in p['slug'] for p in data), 'flat filenames')
    for part, rows in (('JEE', jee), ('Olympiad', oly)):
        check([p['page'] for p in rows] == list(range(1, len(rows) + 1)), 'numbering ' + part)
    check(sum(p['moves'] >= 3 for p in data) == 30, 'every sheet has moves')
    check(all(1 <= len(p['figures']) <= 2 for p in data), 'one wide figure per sheet')
    check(len({p['figures'][0] for p in data}) == 30, 'thirty distinct figures')

    import matplotlib
    cmap = FT2Font(str(ROOT / 'fonts/PatrickHand-Regular.ttf')).get_charmap()
    cmap2 = FT2Font(str(Path(matplotlib.get_data_path()) / 'fonts/ttf/DejaVuSans.ttf')).get_charmap()
    for p in data:
        text = p['title'] + p['question'] + p.get('takeaway', '')
        check(all(ord(ch) in cmap or ord(ch) in cmap2 for ch in text if ch != '\n'),
              'title glyphs ' + p['slug'])
        lay = p['layout']
        check(lay[0]['main_px'] <= lay[0]['main_available'], 'main column ' + p['slug'])
        check(lay[1]['margin_px'] <= lay[1]['margin_available'], 'rail ' + p['slug'])
        check(lay[1]['figure_y'] + lay[1]['figure_h'] <= 3220, 'figure band ' + p['slug'])

    for p in data:
        png = ROOT / p['file']
        check(png.stat().st_size > 60_000, 'png bytes ' + p['slug'])
        im = Image.open(png)
        check(im.size == (2480, 3508), 'canvas ' + p['slug'])
        dpi = im.info.get('dpi', (0, 0))
        check(abs(dpi[0] - 300) < 1 and abs(dpi[1] - 300) < 1, 'dpi ' + p['slug'])
        check(im.mode in ('P', 'RGB'), 'png mode ' + p['slug'])
        # safe margin: nothing but background in the outer 90 px frame
        grey = im.convert('L')
        box = grey.crop((0, 0, 2480, 90))
        check(box.getextrema()[1] > 235, 'top margin ' + p['slug'])

    for label, count in (('All', 30), ('JEE', 19), ('Olympiad', 11)):
        pdf = PdfReader(ROOT / PDFS[label])
        check(len(pdf.pages) == count, 'pdf pages ' + label)
        box = pdf.pages[0].mediabox
        check(abs(float(box.width) - 595.28) < 1 and abs(float(box.height) - 841.89) < 1,
              'a4 box ' + label)
        outline = pdf.outline
        check(len(outline) == count, 'pdf bookmarks ' + label)
        check(all('/Title' in o for o in outline), 'bookmark titles ' + label)
        with zipfile.ZipFile(ROOT / ZIPS[label]) as z:
            check(len(z.namelist()) == count, 'zip count ' + label)
            check(all(n.endswith('.png') for n in z.namelist()), 'zip contents ' + label)
    with zipfile.ZipFile(ROOT / ZIPS['All']) as z:
        check(z.namelist() == sorted(z.namelist(), key=lambda n: z.namelist().index(n)),
              'zip order stable')
        check(z.testzip() is None, 'zip crc')

    html = (ROOT / 'index.html').read_text()
    for link in re.findall(r'(?:href|src)="([^"]+)"', html):
        url = urlsplit(link)
        if url.scheme or not url.path or url.path.startswith('#'):
            continue
        check((ROOT / unquote(url.path)).exists(), 'gallery link ' + link)
    check(all(p['file'] in html for p in data), 'every page in the gallery')

    # ---- physics spot checks (independent recomputation) -----------------
    g, rw, rhg = 9.8, 1000.0, 13600.0
    near('p at 10 m, gauge', rw * g * 10, 98_000)
    near('barometer mercury 0.76 m', rhg * g * .76, 101_293, rel=.002)
    near('barometer water height', 101_325 / (rw * g), 10.34, rel=.003)
    near('gate force 3x2 m, top at surface', rw * g * 1.0 * 6.0, 58_800)
    near('centre of pressure 2H/3', 2 * 2 / 3, 1.3333, rel=.001)
    near('surface tilt tan(theta)=a/g', math.degrees(math.atan(2.0 / g)), 11.54, rel=.01)
    near('paraboloid rise w=4,R=.3', 4 ** 2 * .3 ** 2 / (2 * g), .0735, rel=.01)
    near('float fraction 900/1000', 900 / 1000, .9)
    near('ice+stone level drop', ((0.6 - 0.54) / 1000) / 0.02, .003, rel=.02)
    near('Torricelli v, h=0.8 m', math.sqrt(2 * g * .8), 3.96, rel=.002)
    near('range x=2 sqrt(h(H-h))', 2 * math.sqrt(.8 * .45), 1.2, rel=.002)
    near('drain time A/a=100, H=1.25', 100 * math.sqrt(2 * 1.25 / g), 50.5, rel=.005)
    a1, a2, dp = 4e-3, 1e-3, 1470.0
    q = a1 * a2 * math.sqrt(2 * dp / (rw * (a1 ** 2 - a2 ** 2)))
    near('Venturi Q', q * 1e3, 1.77, rel=.02)
    near('jet force, a=1e-4, v=10', rw * 1e-4 * 100, 10.0, rel=.001)
    r, L, dpp, eta = 2e-3, 1.0, 1000.0, 1e-3
    qq = math.pi * r ** 4 * dpp / (8 * eta * L)
    near('Poiseuille Q, r=2 mm', qq * 1e6, 6.28, rel=.01)
    near('Reynolds of that pipe', rw * (qq / (math.pi * r ** 2)) * 2 * r / eta, 2000, rel=.02)
    near('Stokes v_t, 0.1 mm in water', 2 * 1e-8 * rw * g / (9 * eta), .0218, rel=.02)
    near('drop excess pressure 2 gamma/r', 2 * .0728 / 1e-3, 145.6, rel=.002)
    near('bubble excess pressure 4 gamma/r', 4 * .0728 / 1e-3, 291.2, rel=.002)
    near('Jurin h, r=0.5 mm', 2 * .0728 / (rw * g * 5e-4), .0297, rel=.005)
    near('short tube, h=12 cm cut to 9 cm', 12 / 9, 4 / 3, rel=.001)
    near('shallow water c, h=1.5 m', math.sqrt(g * 1.5), 3.83, rel=.002)
    near('hydraulic lift force ratio A/a=5', 5 * 392, 1960, rel=.001)

    (ROOT / 'verification-results.json').write_text(json.dumps(
        {'checks': checks, 'model_checks': len(models), 'models': models,
         'note': 'Representative recomputation of printed formulas, not exhaustive.'},
        indent=2) + '\n')
    print(f'PASS: {checks} assertions; {len(models)} representative physics checks.')
    print('Not exhaustive: see SOURCE-AUDIT.md for what was and was not verified.')


if __name__ == '__main__':
    main()
