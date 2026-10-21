"""Run from any directory after author/render/export.

Checks covers structure, typography, layout, archives, PDFs, links and a set of
independently recomputed physics numbers. It is representative, not a proof of
every line on every sheet.
"""
from pathlib import Path
import hashlib, json, math, re, zipfile
from urllib.parse import unquote, urlsplit

from PIL import Image, ImageChops
from pypdf import PdfReader
from matplotlib.ft2font import FT2Font

from build_exports import ROOT, PDFS, ZIPS

checks = 0
models = []


def check(ok, message):
    global checks
    checks += 1
    assert ok, message


def near(name, value, target, rel=.02, absolute=1e-8):
    check(abs(value - target) <= max(absolute, rel * abs(target)),
          f'{name}: {value} vs {target}')
    models.append({'name': name, 'value': float(value), 'expected': float(target)})


def main():
    data = json.loads((ROOT / 'sheets.json').read_text())
    check(len(data) == 17, 'page count')
    check([p['section'] for p in data] == ['JEE'] * 8 + ['Olympiad'] * 9, 'reading order')
    check(len({p['slug'] for p in data}) == 17, 'unique filenames')
    check(sum(len(p['cards']) for p in data) == 68, 'card count')
    check(sum(len(p['diagrams']) for p in data) == 34, 'diagram count')
    check(sum(k == 'm' for p in data for c in p['cards'] for k, s in c['items']) == 136,
          'math block count')

    cmap = FT2Font(str(ROOT / 'fonts/PatrickHand-Regular.ttf')).get_charmap()
    for p in data:
        prose = ([p['title'], p['subtitle'], p['source'], p['takeaway']]
                 + [c['title'] for c in p['cards']]
                 + [s for c in p['cards'] for k, s in c['items'] if k != 'm'])
        check(all(ord(ch) in cmap or ch == '\n' for text in prose for ch in text),
              'font coverage ' + p['slug'])

    for section, count in [('JEE', 8), ('Olympiad', 9)]:
        rows = [p for p in data if p['section'] == section]
        check([p['part_page'] for p in rows] == list(range(1, count + 1)),
              'numbering ' + section)
        check(all(p['part_total'] == count for p in rows), 'page totals ' + section)
        check({str(p.relative_to(ROOT)) for p in ROOT.glob(section + '-*.png')}
              == {p['slug'] + '.png' for p in rows}, 'stale/missing pages ' + section)

    for p in data:
        im = Image.open(ROOT / (p['slug'] + '.png'))
        check(im.size == (2480, 3508), 'dimensions ' + p['slug'])
        check(all(abs(d - 300) < .1 for d in im.info['dpi']), 'DPI ' + p['slug'])
        rgb = im.convert('RGB')
        white = Image.new('RGB', rgb.size, 'white')
        bounds = ImageChops.difference(rgb, white).getbbox()
        check(bounds and bounds[0] >= 125 and bounds[1] >= 125
              and bounds[2] <= 2356 and bounds[3] <= 3383,
              'safe margin ' + p['slug'])

    layout = json.loads((ROOT / 'layout-checks.json').read_text())
    check(len(layout['cards']) == 68, 'layout manifest')
    for c in layout['cards']:
        check(c['used_px'] < c['available_px'] - 12, 'card overflow ' + c['card'])
        check(c['body_pt'] == 11.52 and c['explanation_pt'] == 11.04,
              'body text never shrunk: ' + c['card'])

    for label, rows in [('All', data), ('JEE', data[:8]), ('Olympiad', data[8:])]:
        with zipfile.ZipFile(ROOT / ZIPS[label]) as z:
            check(z.testzip() is None, 'zip CRC ' + label)
            check(z.namelist() == [p['slug'] + '.png' for p in rows],
                  'zip reading order ' + label)
            for p in rows:
                check(z.read(p['slug'] + '.png')
                      == (ROOT / (p['slug'] + '.png')).read_bytes(), 'zip bytes ' + label)

        reader = PdfReader(ROOT / PDFS[label])
        check(len(reader.pages) == len(rows), 'PDF page count ' + label)
        check(len(reader.outline) == len(rows), 'bookmark count ' + label)
        for index, (page, p) in enumerate(zip(reader.pages, rows)):
            check(abs(float(page.mediabox.width) - 595.2756) < .01
                  and abs(float(page.mediabox.height) - 841.8898) < .01,
                  'A4 portrait ' + label)
            check(reader.get_destination_page_number(reader.outline[index]) == index,
                  'bookmark destination ' + label)
            check(p['title'] in reader.outline[index].title, 'bookmark title ' + label)
            objs = page['/Resources']['/XObject'].get_object()
            images = [o.get_object() for o in objs.values()
                      if o.get_object().get('/Subtype') == '/Image']
            check(len(images) == 1, 'one sheet/page ' + label)
            obj = images[0]
            im = Image.open(ROOT / (p['slug'] + '.png'))
            check(obj['/Width'] == 2480 and obj['/Height'] == 3508,
                  'PDF resolution ' + label)
            check(hashlib.sha256(obj.get_data()).digest()
                  == hashlib.sha256(im.tobytes()).digest(),
                  'PDF lossless source pixels ' + label)

    html = (ROOT / 'index.html').read_text()
    check(html.count('<article ') == 17, 'gallery count')
    for url in re.findall(r'(?:href|src)=["\']([^"\']+)', html):
        path = urlsplit(url)
        if path.scheme or not path.path:
            continue
        check((ROOT / unquote(path.path)).is_file(), 'gallery link ' + url)

    # Independent recomputation from the parameters printed on the sheets.
    Y, G, rho = 2.0e11, 8.0e10, 7800.0
    near('Poisson relation Y from B and nu', 3 * 1.6e11 * (1 - 2 * .29), Y, rel=.01)
    near('Poisson relation Y from G and nu', 2 * G * (1 + .29), Y, rel=.04)
    near('admissible nu upper bound', .5, .5)
    near('torsion J over I', (math.pi * .01 ** 4 / 2) / (math.pi * .01 ** 4 / 4), 2)
    I_rect = .020 * .040 ** 3 / 12
    near('cantilever tip deflection mm',
         (200 * 1.0 ** 3) / (3 * Y * I_rect) * 1000, 3.1, rel=.02)
    near('cantilever over simply supported centre', (1 / 3) / (1 / 48), 16)
    near('simply supported over fixed-fixed centre', (1 / 48) / (1 / 192), 4)
    near('torsion core fraction of J', .7 ** 4, .24, rel=.01)
    near('torsion core fraction of A', .7 ** 2, .49, rel=.01)
    near('uniform load over end load, same total', (1 / 8) / (1 / 3), .375)
    pcr = math.pi ** 2 * Y * (math.pi * .01 ** 4 / 4) / 2.0 ** 2
    near('Euler load solid rod N', pcr, 3876, rel=.01)
    near('yield load solid rod N', 2.5e8 * math.pi * .01 ** 2, 78540, rel=.01)
    near('buckling over yield', pcr / (2.5e8 * math.pi * .01 ** 2), .049, rel=.03)
    r2, r_out = .01, .015
    r_in = math.sqrt(r_out ** 2 - r2 ** 2)
    near('hollow over solid I, equal mass',
         (r_out ** 4 - r_in ** 4) / r2 ** 4, 3.5, rel=.01)
    near('hoop over longitudinal stress', (2e6 * 1.0 / .005) / (2e6 * 1.0 / (2 * .005)), 2)
    near('thin cylinder hoop stress MPa', 2e6 * 1.0 / .005 / 1e6, 400)
    near('thin sphere stress MPa', 2e6 * 1.0 / (2 * .005) / 1e6, 200)
    near('rod wave speed km/s', math.sqrt(Y / rho) / 1000, 5.06, rel=.02)
    near('shear wave speed km/s', math.sqrt(G / rho) / 1000, 3.20, rel=.02)
    near('bulk P speed km/s',
         math.sqrt((1.6e11 + 4 * G / 3) / rho) / 1000, 5.85, rel=.03)
    rho_c = 2700
    vp, vs = 6000., 3500.
    Bc = rho_c * (vp ** 2 - 4 / 3 * vs ** 2)
    near('crustal bulk modulus GPa', Bc / 1e9, 53.1, rel=.02)
    near('crustal Poisson ratio',
         (vp ** 2 - 2 * vs ** 2) / (2 * (vp ** 2 - vs ** 2)), .242, rel=.02)
    near('thermal stress MPa per K', Y * 1.2e-5 / 1e6, 2.4, rel=.01)
    near('rail breathing length m', 1.2e-5 * 1000 * 40, .48, rel=.01)
    near('rail blocked stress MPa', Y * 1.2e-5 * 40 / 1e6, 96, rel=.01)
    near('sudden load factor', 2, 2)
    near('atomic modulus GPa', 4.8e-19 / (2e-10) ** 3 / 1e9, 60, rel=.02)
    near('interatomic spring N/m', Y * 2e-10, 40, rel=.01)
    near('thermal expansion per K', 1.380649e-23 / (2 * 4.8e-19), 1.44e-5, rel=.02)
    M, m, k, h, g = 10., 40., 1e5, 1e-3, 9.8
    delta = ((M + m / 2) * g
             + math.sqrt(((M + m / 2) * g) ** 2 + 2 * k * M * g * h)) / k
    near('rod-mass drop extension mm', delta * 1000, 6.2, rel=.02)
    near('massless drop extension mm',
         (M * g + math.sqrt((M * g) ** 2 + 2 * k * M * g * h)) / k * 1000, 2.7, rel=.02)
    near('constant-stress decay length m', 2.5e8 / (7800 * 9.8), 3270, rel=.02)
    near('Mohr radius MPa', math.hypot((80 - 20) / 2, 30), 42.4, rel=.01)
    near('Mohr sigma 1 MPa', 50 + math.hypot(30, 30), 92.4, rel=.01)
    near('Mohr sigma 2 MPa', 50 - math.hypot(30, 30), 7.6, absolute=.05)
    near('principal stress trace invariant', 92.4 + 7.6, 100, rel=.02)
    near('specific strength steel m2/s2', 2.5e8 / 7800, 3.2e4, rel=.02)
    near('specific modulus steel m2/s2', Y / 7800, 2.6e7, rel=.02)
    near('silk over steel specific strength', 7.7e5 / 3.2e4, 24, rel=.02)
    near('steel over silk specific modulus', 2.6e7 / 7.7e6, 3.4, rel=.03)

    source = ROOT.parents[1] / 'elasticity/Elasticity.md'
    check(hashlib.sha256(source.read_bytes()).hexdigest()
          == '0d0488c88e006c8409d6014319567eeec9652f1c84de0cc44cabd9d30c0bcea8',
          'detailed source preserved')

    assets = json.loads((ROOT / 'asset-manifest.json').read_text())
    for name, details in assets.items():
        content = (ROOT / name).read_bytes()
        check(len(content) == details['bytes']
              and hashlib.sha256(content).hexdigest() == details['sha256'],
              'asset manifest ' + name)

    report = {'assertions': checks, 'physics_model_checks': len(models),
              'pages': 17, 'JEE': 8, 'Olympiad': 9, 'cards': 68,
              'diagrams': 34, 'math_blocks': 136, 'numerical_models': models}
    (ROOT / 'verification-results.json').write_text(json.dumps(report, indent=2) + '\n')
    print(f'PASS: {checks} assertions; {len(models)} representative physics/model checks; '
          '17 PNGs; 3 ZIPs; 3 PDFs. Not exhaustive certification.')


if __name__ == '__main__':
    main()
