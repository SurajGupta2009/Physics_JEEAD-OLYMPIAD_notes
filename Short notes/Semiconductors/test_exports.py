"""Independent physics, numerical & structural verification for Semiconductors short notes."""
from pathlib import Path
import json, zipfile, hashlib, re, math
from urllib.parse import unquote
import numpy as np
from PIL import Image
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parent
PDFS = {
    'All': 'semiconductors-short-notes.pdf',
    'JEE': 'semiconductors-jee.pdf',
    'Olympiad': 'semiconductors-olympiad.pdf',
}
ZIPS = {
    'All': 'semiconductors-all-pngs.zip',
    'JEE': 'semiconductors-jee-pngs.zip',
    'Olympiad': 'semiconductors-olympiad-pngs.zip',
}

ASSERTIONS = 0


def check(cond, msg=''):
    global ASSERTIONS
    assert cond, msg
    ASSERTIONS += 1


def main():
    global ASSERTIONS
    ASSERTIONS = 0
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

    # Verify layout-checks.json has zero overflows and zero sparse cards across all 72 cards
    lc = json.loads((ROOT / 'layout-checks.json').read_text())
    check(len(lc['cards']) == 72, 'Expected 72 cards')
    for entry in lc['cards']:
        check(560 <= entry['used_px'] <= 1038, f'Card out of bounds: {entry}')

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

    # Independent representative semiconductor physics & numerical checks across JEE + Olympiad
    e_q, k_B = 1.602176634e-19, 1.380649e-23
    VT_300 = k_B * 300.0 / e_q
    # 1. Mass-action & n-type Si conductivity (Nd = 1e22 m^-3, ni = 1.5e16 m^-3, mu_e = 0.135)
    ni, Nd, mu_e, mu_h = 1.5e16, 1.0e22, 0.135, 0.048
    p0 = ni ** 2 / Nd
    sigma = e_q * (Nd * mu_e + p0 * mu_h)
    check(abs(p0 - 2.25e10) < 1e3 and abs(sigma - 216.29) < 0.05, 'Mass-action & conductivity check')
    # 2. Einstein relation D_e / mu_e = k_B T / e = 25.85 mV at 300 K
    De = mu_e * VT_300
    check(abs(VT_300 * 1e3 - 25.852) < 0.01 and abs(De * 1e4 - 34.90) < 0.05, 'Einstein relation check')
    # 3. Full-wave bridge rectifier mean DC & RMS form factor
    th = np.linspace(0, math.pi, 200000)
    v_dc = np.trapezoid(np.sin(th), th) / math.pi
    v_rms = math.sqrt(np.trapezoid(np.sin(th) ** 2, th) / math.pi)
    check(abs(v_dc - 2.0 / math.pi) < 1e-10 and abs(v_rms - 1.0 / math.sqrt(2.0)) < 1e-10,
          'Bridge rectifier DC/RMS integral check')
    # 4. BJT saturation clamp check (Q23: VCC = 5 V, RC = 1 kOhm, beta = 100, IB = 100 uA, VCE_sat = 0.2 V)
    VCC, RC, beta, IB, VCE_sat = 5.0, 1000.0, 100.0, 100e-6, 0.2
    IC_actual = min(beta * IB, (VCC - VCE_sat) / RC)
    check(beta * IB > (VCC - VCE_sat) / RC and abs(IC_actual * 1e3 - 4.8) < 1e-9, 'BJT saturation clamp check')
    # 5. Boolean De Morgan & 1-bit full-adder exhaustive 8-row truth-table verification
    for A in (0, 1):
        for B in (0, 1):
            check((1 - (A & B)) == ((1 - A) | (1 - B)), 'De Morgan NAND')
            check((1 - (A | B)) == ((1 - A) & (1 - B)), 'De Morgan NOR')
            for Cin in (0, 1):
                s = A ^ B ^ Cin
                cout = (A & B) | (Cin & (A ^ B))
                check(A + B + Cin == 2 * cout + s, 'Full-adder arithmetic identity')
    # 6. Hall effect carrier extraction & ambipolar zero condition p * mu_h^2 = n * mu_e^2
    I_h, B_h, t_h, VH = 10e-3, 0.5, 0.5e-3, 62e-3
    n_hall = I_h * B_h / (e_q * VH * t_h)
    p_zero_ratio = (mu_e / mu_h) ** 2
    check(abs(n_hall - 1.007e21) < 1e19 and abs(p_zero_ratio - 7.91) < 0.02, 'Hall metrology check')
    # 7. Shot vs Johnson-Nyquist thermal noise crossover I_cross = 2 k_B T / (e R_L)
    RL = 10e3
    I_cross = 2 * k_B * 300.0 / (e_q * RL)
    S_shot = 2 * e_q * I_cross
    S_therm = 4 * k_B * 300.0 / RL
    check(abs(I_cross * 1e6 - 5.170) < 0.01 and abs(S_shot - S_therm) < 1e-36, 'Shot/thermal noise crossover')

    summary = {'status': 'PASS', 'assertions': ASSERTIONS, 'sheets': len(data), 'cards': len(lc['cards'])}
    (ROOT / 'test-results.json').write_text(json.dumps(summary, indent=2) + '\n')
    print(f'PASS: {ASSERTIONS} structural, pixel, lossless PDF, and semiconductor physics assertions verified!')


def test_semiconductors_exports():
    main()


if __name__ == '__main__':
    main()
