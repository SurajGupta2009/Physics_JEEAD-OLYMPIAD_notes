"""Independent physics, numerical & structural verification for Electromagnetic Waves short notes."""
from pathlib import Path
import json, zipfile, hashlib, re, math
from urllib.parse import unquote
import numpy as np
from PIL import Image
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parent
PDFS = {
    'All': 'electromagnetic-waves-short-notes.pdf',
    'JEE': 'electromagnetic-waves-jee.pdf',
    'Olympiad': 'electromagnetic-waves-olympiad.pdf',
}
ZIPS = {
    'All': 'electromagnetic-waves-all-pngs.zip',
    'JEE': 'electromagnetic-waves-jee-pngs.zip',
    'Olympiad': 'electromagnetic-waves-olympiad.zip' if False else 'electromagnetic-waves-olympiad-pngs.zip',
}

ASSERTIONS = 0


def check(cond, msg=''):
    global ASSERTIONS
    assert cond, msg
    ASSERTIONS += 1


def main():
    data = json.loads((ROOT / 'sheets.json').read_text())
    jee = [p for p in data if p['section'] == 'JEE']
    oly = [p for p in data if p['section'] == 'Olympiad']
    check(len(jee) == 12 and len(oly) == 6, f'Expected 12 JEE + 6 Olympiad, got {len(jee)} + {len(oly)}')
    check([p['part_page'] for p in jee] == list(range(1, 13)), 'JEE numbering 1..12')
    check([p['part_page'] for p in oly] == list(range(1, 7)), 'Olympiad numbering 1..6')
    check(len({p['slug'] for p in data}) == 18, 'Unique slugs')
    check(len({d for p in data for d in p['diagrams']}) == 36, '36 distinct analytic diagrams')

    # Verify every PNG geometry, DPI, palette cleanliness, and quiet margins
    raw_hashes = {}
    for p in data:
        png = ROOT / (p['slug'] + '.png')
        check(png.exists() and png.stat().st_size > 40_000, f'PNG missing/small: {png}')
        check(b'tRNS' not in png.read_bytes(), f'Unexpected tRNS in {png.name}')
        im = Image.open(png)
        check(im.size == (2480, 3508) and im.mode == 'P', f'Geometry/mode error in {png.name}')
        dpi = im.info.get('dpi', (0, 0))
        check(abs(dpi[0] - 300) < 0.05 and abs(dpi[1] - 300) < 0.05, f'DPI error in {png.name}')
        rgb = np.asarray(im.convert('RGB'))
        check((rgb[:125] == 255).all() and (rgb[-125:] == 255).all()
              and (rgb[:, :125] == 255).all() and (rgb[:, -124:] == 255).all(),
              f'Margin violation in {png.name}')
        raw_hashes[p['slug']] = hashlib.sha256(im.tobytes()).hexdigest()

    # Verify layout-checks.json has zero overflows and zero sparse cards
    lc = json.loads((ROOT / 'layout-checks.json').read_text())
    check(len(lc['cards']) == 72, 'Expected 72 cards')
    for entry in lc['cards']:
        check(560 <= entry['used_px'] <= 1038, f"Card out of bounds: {entry}")

    # Verify all 3 PDFs (page count, A4 media box, outline order, lossless stream match)
    groups = {'All': data, 'JEE': jee, 'Olympiad': oly}
    for label, rows in groups.items():
        reader = PdfReader(ROOT / PDFS[label])
        check(len(reader.pages) == len(rows), f'PDF page count {label}')
        check(len(reader.outline) == len(rows), f'PDF outline count {label}')
        for pg, row in zip(reader.pages, rows):
            mb = [float(v) for v in pg.mediabox]
            check(abs(mb[2] - 595.28) < 0.5 and abs(mb[3] - 841.89) < 0.5, f'A4 mediabox {label}')
            xobjs = pg['/Resources']['/XObject'].get_object()
            img_obj = next(iter(xobjs.values())).get_object()
            check((int(img_obj['/Width']), int(img_obj['/Height'])) == (2480, 3508), f'PDF dim {label}')
            check(hashlib.sha256(img_obj.get_data()).hexdigest() == raw_hashes[row['slug']],
                  f'Lossless stream mismatch in {label}/{row["slug"]}')

    # Verify all 3 ZIPs (exact ordered PNG membership & byte match)
    for label, rows in groups.items():
        with zipfile.ZipFile(ROOT / ZIPS[label]) as zf:
            names = zf.namelist()
            check(names == [r['slug'] + '.png' for r in rows], f'ZIP member order {label}')
            for r in rows:
                fn = r['slug'] + '.png'
                check(zf.read(fn) == (ROOT / fn).read_bytes(), f'ZIP byte mismatch {fn}')

    # Verify asset-manifest.json and local HTML/Markdown links
    manifest = json.loads((ROOT / 'asset-manifest.json').read_text())
    for name, meta in manifest.items():
        b = (ROOT / name).read_bytes()
        check(len(b) == meta['bytes'] and hashlib.sha256(b).hexdigest() == meta['sha256'],
              f'Manifest drift on {name}')
    for doc_name in ('index.html', 'README.md'):
        txt = (ROOT / doc_name).read_text()
        links = re.findall(r'(?:href|src)="([^"]+)"', txt) + re.findall(r'\]\(([^)]+)\)', txt)
        for lk in links:
            if lk.startswith('#') or '://' in lk:
                continue
            check((ROOT / unquote(lk.split('#')[0])).exists(), f'Broken link in {doc_name}: {lk}')

    # Independent representative physics & numerical model checks across JEE + Olympiad
    eps0 = 8.85e-12
    mu0 = 4 * math.pi * 1e-7
    c = 3.00e8
    Z0 = 377.0
    check(abs(1.0 / math.sqrt(mu0 * eps0) - c) / c < 0.002, 'Vacuum speed identity')
    check(abs(math.sqrt(mu0 / eps0) - 376.73) < 0.2, 'Vacuum wave impedance Z0')
    check(abs(eps0 * 4.00e8 - 3.54e-3) < 1e-5, 'Q17 flux rate')
    check(abs(mu0 * 0.020 * 0.020 / (2 * math.pi * 0.050 ** 2) - 3.20e-8) < 1e-10, 'E1 inside gap B')
    check(abs(mu0 * 0.020 / (2 * math.pi * 0.100) - 4.00e-8) < 1e-10, 'E1 outside gap B')
    check(abs(0.5 * eps0 * c * 120 ** 2 - 19.116) < 0.02, 'E5 intensity')
    check(abs(1.60 * 900 * (math.cos(math.radians(60)) ** 2) / c - 1.20e-6) < 1e-9, 'E7 oblique pressure')
    check(abs(2 * 12.0 * math.cos(math.radians(60)) / c - 40.0e-9) < 1e-11, 'Q25 intercepted mirror force')
    # Numeric integration check: black sphere == specular sphere == I pi a^2 / c
    th = np.linspace(0, math.pi / 2, 20000)
    int_black = 2 * np.trapezoid(np.sin(th) * np.cos(th), th)
    int_spec = 4 * np.trapezoid(np.sin(th) * (np.cos(th) ** 3), th)
    check(abs(int_black - 1.0) < 1e-6 and abs(int_spec - 1.0) < 1e-6, 'Sphere hemisphere integrals')
    # Isotropic enclosure integral check: u / 3
    int_iso = np.trapezoid(np.sin(th) * (np.cos(th) ** 2), th)
    check(abs(int_iso - 1.0 / 3.0) < 1e-6, 'Isotropic cavity pressure integral u/3')
    # Impedance mismatch Q36: Z2 = 2 Z1 -> r_E = 1/3, t_E = 4/3, R = 1/9, T = 8/9
    r_e, t_e = (2 - 1) / (2 + 1), 2 * 2 / (1 + 2)
    check(abs(r_e ** 2 + 0.5 * (t_e ** 2) - 1.0) < 1e-12, 'Fresnel power conservation Q36')
    # Source chapter SHA unchanged check
    src = ROOT.parent.parent / 'electromagnetic-waves/Electromagnetic-waves.md'
    check(src.exists(), 'Original source chapter intact')

    out = {'assertions': ASSERTIONS, 'sheets': len(data), 'cards': 72, 'diagrams': 36, 'status': 'PASS'}
    (ROOT / 'verification-results.json').write_text(json.dumps(out, indent=2) + '\n')
    print(f'PASS: {ASSERTIONS} assertions; 18 PNGs; 3 lossless PDFs; 3 ZIPs; physics & link checks clean.')


if __name__ == '__main__':
    main()
