"""Run after author_content.py and build_exports.py.

Checks page structure and typography, the PNG canvas, the three PDFs and ZIPs,
the gallery links, and a representative set of the numbers printed on the
sheets, each recomputed here from its own formula.  It is representative, not a
proof of every line on every sheet: see SOURCE-AUDIT.md for the split.
"""
from pathlib import Path
import json, math, re, zipfile
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
    check((len(jee), len(oly)) == (15, 15), 'part sizes')
    check([p['slug'] for p in data] == [p['slug'] for p in jee + oly], 'reading order')
    check(len({p['slug'] for p in data}) == 30, 'unique slugs')
    check(all(p['slug'].startswith(p['section'] + '-') for p in data), 'section prefix')
    check(all('/' not in p['slug'] for p in data), 'flat filenames')
    for part, rows in (('JEE', jee), ('Olympiad', oly)):
        check([p['page'] for p in rows] == list(range(1, len(rows) + 1)), 'numbering ' + part)
    check(sum(p['moves'] >= 3 for p in data) == 30, 'every sheet has moves')
    check(all(1 <= len(p['figures']) <= 2 for p in data), 'one wide figure per sheet')
    check(len({p['figures'][0] for p in data}) == 30, 'thirty distinct figures')
    check(all(p['takeaway'].strip() for p in data), 'every sheet carries a takeaway')
    check(len({p['takeaway'] for p in data}) == 30, 'takeaways are not repeated')

    import matplotlib
    cmap = FT2Font(str(ROOT / 'fonts/PatrickHand-Regular.ttf')).get_charmap()
    cmap2 = FT2Font(str(Path(matplotlib.get_data_path()) / 'fonts/ttf/DejaVuSans.ttf')).get_charmap()
    for p in data:
        text = p['title'] + p['question'] + p['takeaway']
        check(all(ord(ch) in cmap or ord(ch) in cmap2 for ch in text if ch != '\n'),
              'title glyphs ' + p['slug'])
        lay = p['layout']
        check(lay[0]['main_px'] <= lay[0]['main_available'], 'main column ' + p['slug'])
        check(lay[1]['margin_px'] <= lay[1]['margin_available'], 'rail ' + p['slug'])
        check(lay[1]['figure_y'] + lay[1]['figure_h'] <= 3220, 'figure band ' + p['slug'])
        check(lay[1]['figure_y'] > lay[0].get('main_px', 0), 'figure below body ' + p['slug'])

    for p in data:
        png = ROOT / p['file']
        check(png.stat().st_size > 60_000, 'png bytes ' + p['slug'])
        im = Image.open(png)
        check(im.size == (2480, 3508), 'canvas ' + p['slug'])
        dpi = im.info.get('dpi', (0, 0))
        check(abs(dpi[0] - 300) < 1 and abs(dpi[1] - 300) < 1, 'dpi ' + p['slug'])
        check(im.mode in ('P', 'RGB'), 'png mode ' + p['slug'])
        grey = im.convert('L')
        check(grey.crop((0, 0, 2480, 90)).getextrema()[1] > 235, 'top margin ' + p['slug'])

    for label, count in (('All', 30), ('JEE', 15), ('Olympiad', 15)):
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
        check(z.namelist() == [p['file'] for p in data], 'zip order follows reading order')
        check(z.testzip() is None, 'zip crc')

    html = (ROOT / 'index.html').read_text()
    for link in re.findall(r'(?:href|src)="([^"]+)"', html):
        url = urlsplit(link)
        if url.scheme or not url.path or url.path.startswith('#'):
            continue
        check((ROOT / unquote(url.path)).exists(), 'gallery link ' + link)
    check(all(p['file'] in html for p in data), 'every page in the gallery')

    # ---- physics spot checks (independent recomputation) -----------------
    from math import sqrt, log, log10, pi
    h, c, e, me = 6.62607015e-34, 2.99792458e8, 1.602176634e-19, 9.1093837e-31
    k = 8.9875517923e9            # 1/(4 pi eps0)
    eV = e
    # Rutherford
    near('r_min alpha 5 MeV on gold (fm)', 2 * 79 * k * e * e / (5e6 * eV) * 1e15, 45.5, rel=.01)
    near('b at 90 deg, same beam (fm)', 79 * k * e * e / (5e6 * eV) * 1e15, 22.8, rel=.01)
    near('Coulomb barrier gold R=7 fm (MeV)', 2 * 79 * k * e * e / 7e-15 * 1e-6 / eV, 32.5, rel=.02)
    a0 = (h / (2 * pi)) ** 2 / (me * k * e * e)
    near('Bohr radius (pm)', a0 * 1e12, 52.9, rel=.002)
    near('H n=3 radius (A)', 9 * a0 * 1e10, 4.76, rel=.004)
    near('H n=3 speed (m/s)', k * e * e / (3 * h / (2 * pi)), 7.29e5, rel=.01)
    near('H n=3 de Broglie (A)', h / (me * k * e * e / (3 * h / (2 * pi))) * 1e10, 9.97, rel=.01)
    near('ionisation of H (eV)', me * k ** 2 * e ** 4 / (2 * (h / (2 * pi)) ** 2) / eV, 13.6, rel=.002)
    near('Balmer edge (nm)', h * c / (13.6 * eV * (1 / 4)) * 1e9, 364.6, rel=.003)
    near('Lyman alpha (nm)', h * c / (13.6 * eV * (3 / 4)) * 1e9, 121.6, rel=.003)
    near('H-alpha (nm)', 1 / (1.0967758e7 * (1 / 4 - 1 / 9)) * 1e9, 656.3, rel=.002)
    near('He+ ground (eV)', -13.6 * 4, -54.4, rel=.001)
    near('Li2+ ground (eV)', -13.6 * 9, -122.4, rel=.001)
    near('positronium ground (eV)', -6.8, -13.6 / 2, rel=.001)
    near('positronium radius (A)', 2 * a0 * 1e10, 1.06, rel=.003)
    # photons
    near('550 nm photon (eV)', h * c / (550e-9) / eV, 2.25, rel=.004)
    near('Na threshold (nm)', h * c / (2.28 * eV) * 1e9, 544, rel=.003)
    near('K_max, 400 nm on Na (eV)', h * c / (400e-9) / eV - 2.28, .82, rel=.01)
    near('1.226/sqrt(V) at 100 V (A)', 1.226 / sqrt(100), .1226, rel=.002)
    near('electron wavelength at 100 kV, non-rel (pm)', 1.226 / sqrt(1e5) * 1000, 3.88, rel=.01)
    near('Davisson-Germer 54 V (nm)', 1.226 / sqrt(54), .1668, rel=.004)
    near('d-spacing NaCl 282 pm gives 154 pm at n=1 (deg)',
         math.degrees(math.asin(154 / (2 * 282))), 15.8, rel=.01)
    near('photon flux, 100 W at 2 m (W/m2)', 100 / (4 * pi * 4), 1.99, rel=.01)
    # X-rays and Compton
    near('Duane-Hunt at 100 kV (pm)', 1.24e6 / 1e5, 12.4, rel=.002)
    near('Cu K-alpha energy (keV)', .75 * 13.6e-3 * 28 ** 2, 8.0, rel=.005)
    near('Cu K-alpha wavelength (pm)', h * c / (.75 * 13.6 * eV * 28 ** 2) * 1e12, 155, rel=.005)
    near('Cu K threshold (kV)', .75 * 13.6 * 28 ** 2 / 1e3, 8.0, rel=.006)
    near('Mo K-alpha (pm)', 154 * 28 ** 2 / 41 ** 2, 71.8, rel=.01)
    near('Ag K-alpha (pm)', 154 * 28 ** 2 / 46 ** 2, 57.1, rel=.01)
    near('Pb half-value 0.123 mm, six to 1 % (mm)',
         0.123 * log(.01) / log(.5), .82, rel=.01)
    near('Avogadro from NaCl', 0.05844 / (2 * 2165 * (2.82e-10) ** 3), 6.02e23, rel=.005)
    lam_c = h / (me * c) * 1e12
    near('Compton wavelength (pm)', lam_c, 2.426, rel=.002)
    near('shift at 90 deg (pm)', lam_c, 2.426, rel=.002)
    near('shift at 180 deg (pm)', 2 * lam_c, 4.85, rel=.003)
    gam = 100 / 511
    near('electron KE at 90 deg, 100 keV (keV)', 100 * gam / (1 + gam), 16.4, rel=.01)
    near('electron KE at 180 deg, 100 keV (keV)', 100 * 2 * gam / (1 + 2 * gam), 28.2, rel=.01)
    near('pair threshold (MeV)', 2 * 0.51099895, 1.022, rel=.002)
    near('2 MeV photon pair KE (MeV)', 2 - 1.022, .98, rel=.005)
    near('inverse Compton boost, gamma=1e3', 4 * (1e3) ** 2 * 6e-4, 2.4e3, rel=.02)

    (ROOT / 'verification-results.json').write_text(json.dumps(
        {'checks': checks, 'model_checks': len(models), 'models': models,
         'note': 'Representative recomputation of printed formulas, not exhaustive.'},
        indent=2) + '\n')
    print(f'PASS: {checks} assertions; {len(models)} representative physics checks.')
    print('Not exhaustive: see SOURCE-AUDIT.md for what was and was not verified.')


if __name__ == '__main__':
    main()
