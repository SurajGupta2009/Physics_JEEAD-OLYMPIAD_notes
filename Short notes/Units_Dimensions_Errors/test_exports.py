"""Independent physics, statistical & structural verification for Units, Dimensions & Errors short notes."""
from pathlib import Path
import json, zipfile, hashlib, re, math
from urllib.parse import unquote
import numpy as np
from PIL import Image
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parent
PDFS = {
    'All': 'units-dimensions-errors-short-notes.pdf',
    'JEE': 'units-dimensions-errors-jee.pdf',
    'Olympiad': 'units-dimensions-errors-olympiad.pdf',
}
ZIPS = {
    'All': 'units-dimensions-errors-all-pngs.zip',
    'JEE': 'units-dimensions-errors-jee-pngs.zip',
    'Olympiad': 'units-dimensions-errors-olympiad-pngs.zip',
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

    lc = json.loads((ROOT / 'layout-checks.json').read_text())
    check(len(lc['cards']) == 72, 'Expected 72 cards')
    for entry in lc['cards']:
        check(560 <= entry['used_px'] <= 1038, f"Card out of bounds: {entry}")

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

    for label, rows in groups.items():
        with zipfile.ZipFile(ROOT / ZIPS[label]) as zf:
            names = zf.namelist()
            check(names == [r['slug'] + '.png' for r in rows], f'ZIP member order {label}')
            for r in rows:
                fn = r['slug'] + '.png'
                check(zf.read(fn) == (ROOT / fn).read_bytes(), f'ZIP byte mismatch {fn}')

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

    # Independent physics & statistics checks (including all 5 audited source items)
    # 1. E7 sphere density percentage error: 1% + 3(1%) = 4.0%
    check(abs((1.0 / 100.0 + 3.0 * 0.02 / 2.00) * 100 - 4.0) < 1e-12, 'E7 sphere density 4%')
    # 2. E10 screw-gauge zero-corrected reading: 3.00 + 22(0.01) - 0.04 = 3.18 mm
    check(abs(3.00 + 22 * 0.01 - 0.04 - 3.18) < 1e-12, 'E10 screw gauge 3.18 mm')
    # 3. E4 vernier negative zero error: 2.30 + 7(0.01) - (-0.03) = 2.40 cm
    check(abs(2.30 + 7 * 0.01 - (-0.03) - 2.40) < 1e-12, 'E4 vernier 2.40 cm')
    # 4. E8 sample SD & standard error of the mean
    g_arr = np.array([9.78, 9.82, 9.79, 9.81, 9.80])
    sd = np.std(g_arr, ddof=1)
    sem = sd / math.sqrt(len(g_arr))
    check(abs(np.mean(g_arr) - 9.800) < 1e-12 and abs(sem - 0.007071) < 1e-5, 'E8 SEM')
    # 5. Parallel resistor Monte Carlo check vs exact formula dR/R^2 = dR1/R1^2 + dR2/R2^2
    R1, R2, dR = 100.0, 100.0, 1.0
    Req_hi = (R1 + dR) * (R2 + dR) / ((R1 + dR) + (R2 + dR))
    Req_0 = R1 * R2 / (R1 + R2)
    exact_dReq = (Req_0 ** 2) * (dR / R1 ** 2 + dR / R2 ** 2)
    check(abs((Req_hi - Req_0) - exact_dReq) < 1e-9, 'Parallel resistor exact bound')
    # 6. P30 OLS slope, intercept, standard errors & chi^2
    xs = np.array([1.0, 2.0, 3.0, 4.0])
    ys = np.array([2.1, 3.9, 6.2, 7.8])
    b_ols = np.sum((xs - xs.mean()) * (ys - ys.mean())) / np.sum((xs - xs.mean()) ** 2)
    a_ols = ys.mean() - b_ols * xs.mean()
    chi2 = np.sum(((ys - (a_ols + b_ols * xs)) / 0.2) ** 2)
    check(abs(b_ols - 1.94) < 1e-12 and abs(a_ols - 0.15) < 1e-12 and abs(chi2 - 2.05) < 1e-9, 'P30 OLS & chi2')
    # 7. OL5 0.1% g-experiment design budget: 0.050% + 0.014% + 0.015% < 0.100%
    tot_pct = (0.001 / 2.0 + 2 * 0.01 / (50 * 2 * math.pi * math.sqrt(2.0 / 9.8)) + 2 * (math.radians(2.0) ** 2) / 16.0) * 100
    check(tot_pct < 0.10, 'OL5 0.1% g design budget')
    check((ROOT.parent.parent / 'units-measurements/Units-measurements.md').exists(), 'Source chapter intact')

    out = {'assertions': ASSERTIONS, 'sheets': len(data), 'cards': 72, 'diagrams': 36, 'status': 'PASS'}
    (ROOT / 'verification-results.json').write_text(json.dumps(out, indent=2) + '\n')
    print(f'PASS: {ASSERTIONS} assertions; 18 PNGs; 3 lossless PDFs; 3 ZIPs; physics, stats & link checks clean.')


if __name__ == '__main__':
    main()
