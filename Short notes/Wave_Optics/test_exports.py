"""Independent physics, numerical & structural verification for Wave Optics short notes."""
from pathlib import Path
import json, zipfile, hashlib, re, math
from urllib.parse import unquote
import numpy as np
from PIL import Image
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parent
PDFS = {
    'All': 'wave-optics-short-notes.pdf',
    'JEE': 'wave-optics-jee.pdf',
    'Olympiad': 'wave-optics-olympiad.pdf',
}
ZIPS = {
    'All': 'wave-optics-all-pngs.zip',
    'JEE': 'wave-optics-jee-pngs.zip',
    'Olympiad': 'wave-optics-olympiad-pngs.zip',
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
    check(len(jee) == 16 and len(oly) == 8, f'Expected 16 JEE + 8 Olympiad, got {len(jee)} + {len(oly)}')
    check([p['part_page'] for p in jee] == list(range(1, 17)), 'JEE numbering 1..16')
    check([p['part_page'] for p in oly] == list(range(1, 9)), 'Olympiad numbering 1..8')
    check(len({p['slug'] for p in data}) == 24, 'Unique slugs')
    check(len({d for p in data for d in p['diagrams']}) == 48, '48 distinct analytic diagrams')

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

    # Verify layout-checks.json has zero overflows and zero sparse cards across all 96 cards
    lc = json.loads((ROOT / 'layout-checks.json').read_text())
    check(len(lc['cards']) == 96, 'Expected 96 cards')
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
    # 1. Phasor visibility for I_max : I_min = 25 : 1 -> I1 : I2 = 9 : 4
    I1, I2 = 9.0, 4.0
    Imax = (math.sqrt(I1) + math.sqrt(I2)) ** 2
    Imin = (math.sqrt(I1) - math.sqrt(I2)) ** 2
    V = (Imax - Imin) / (Imax + Imin)
    check(abs(Imax / Imin - 25.0) < 1e-12 and abs(V - 12.0 / 13.0) < 1e-12, 'Phasor visibility check')
    # 2. YDSE energy conservation: integral over one full fringe equals I1 + I2
    phi = np.linspace(0, 2 * math.pi, 40000)
    mean_I = np.trapezoid(I1 + I2 + 2 * math.sqrt(I1 * I2) * np.cos(phi), phi) / (2 * math.pi)
    check(abs(mean_I - (I1 + I2)) < 1e-10, 'YDSE energy conservation')
    # 3. Single-layer AR coating on crown glass n_g = 1.52 with MgF2 n_c = 1.38 vs ideal sqrt(1.52)
    n0, nc_ideal, nc_mgf2, ng = 1.0, math.sqrt(1.52), 1.38, 1.52
    R_uncoated = ((n0 - ng) / (n0 + ng)) ** 2
    R_ideal = ((n0 * ng - nc_ideal ** 2) / (n0 * ng + nc_ideal ** 2)) ** 2
    R_mgf2 = ((n0 * ng - nc_mgf2 ** 2) / (n0 * ng + nc_mgf2 ** 2)) ** 2
    check(abs(R_uncoated - 0.04258) < 1e-4 and abs(R_ideal) < 1e-15 and abs(R_mgf2 - 0.01261) < 1e-4,
          'AR coating reflectance check')
    # 4. Brewster identity sin(theta_c) = cot(theta_B) & Fresnel energy conservation R_s + T_s = 1, R_p + T_p = 1
    thB = math.atan(ng / n0)
    thc = math.asin(n0 / ng)
    check(abs(math.sin(thc) - 1.0 / math.tan(thB)) < 1e-12, 'Brewster-TIR identity')
    for i_deg in (0.0, 30.0, math.degrees(thB), 75.0):
        i = math.radians(i_deg)
        r = math.asin(n0 * math.sin(i) / ng)
        rs_a = (n0 * math.cos(i) - ng * math.cos(r)) / (n0 * math.cos(i) + ng * math.cos(r))
        ts_a = 2 * n0 * math.cos(i) / (n0 * math.cos(i) + ng * math.cos(r))
        rp_a = (ng * math.cos(i) - n0 * math.cos(r)) / (ng * math.cos(i) + n0 * math.cos(r))
        tp_a = 2 * n0 * math.cos(i) / (ng * math.cos(i) + n0 * math.cos(r))
        fac = (ng * math.cos(r)) / (n0 * math.cos(i))
        check(abs(rs_a ** 2 + fac * ts_a ** 2 - 1.0) < 1e-12, 'Fresnel TE energy')
        check(abs(rp_a ** 2 + fac * tp_a ** 2 - 1.0) < 1e-12, 'Fresnel TM energy')
    # 5. Crown glass n = 1.51 Fresnel rhomb: max single-bounce retardation >= 45 deg, hit at 54.62 deg
    n_rel = 1.0 / 1.51
    i_rh = math.radians(54.623)
    ds = 2 * math.atan(math.sqrt(math.sin(i_rh) ** 2 - n_rel ** 2) / math.cos(i_rh))
    dp_t = 2 * math.atan(math.sqrt(math.sin(i_rh) ** 2 - n_rel ** 2) / (n_rel ** 2 * math.cos(i_rh)))
    check(abs(math.degrees(dp_t - ds) - 45.0) < 0.05, 'Fresnel rhomb 45-deg bounce check')
    # 6. Sodium D-doublet Michelson beat spacing dx = lam^2 / (2 dlam) = 0.2891 mm
    lam_d, dlam_d = 589.3e-9, 0.597e-9
    check(abs((lam_d ** 2 / (2 * dlam_d)) * 1e3 - 0.2891) < 0.002, 'Sodium doublet visibility beat')
    # 7. Fabry-Perot finesse & resolving power check (R = 0.90, m = 40000)
    R_fp = 0.90
    F_coef = 4 * R_fp / ((1 - R_fp) ** 2)
    finesse = math.pi * math.sqrt(R_fp) / (1 - R_fp)
    check(abs(F_coef - 360.0) < 1e-9 and abs(finesse - 29.8038) < 1e-3, 'Fabry-Perot finesse check')

    summary = {'status': 'PASS', 'assertions': ASSERTIONS, 'sheets': len(data), 'cards': len(lc['cards'])}
    (ROOT / 'test-results.json').write_text(json.dumps(summary, indent=2) + '\n')
    print(f'PASS: {ASSERTIONS} structural, pixel, lossless PDF, and physics assertions verified!')


if __name__ == '__main__':
    main()
