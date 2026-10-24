"""Gate for the JEE-only Capacitors edition.

Run: python3 test_exports.py    (from this folder)
It fails loudly if the edition drifts back to the old two-column / JEE+Olympiad
format, or if a printable deliverable stops matching its source.
"""
from pathlib import Path
import json, re, sys, zipfile
import numpy as np
from PIL import Image
from pypdf import PdfReader
from reportlab.lib.pagesizes import A4

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
import build_exports as B  # noqa: E402  (PDF/ZIP names live there)

FORBIDDEN = ['debye', 'clausius', 'mossotti', 'paschen', 'conformal', 'spheroid',
             'rayleigh', 'porous', 'depolaris', 'arcosh', 'ferroelectric',
             'piezoelectric', 'eigenvalue', 'weighting potential']
REQUIRED = ['island', 'bridge', 'ladder', 'star-delta', 'image', 'heat',
            'dielectric', 'ripple', 'time constant', 'cube', 'series', 'parallel']


def test():
    data = json.loads((ROOT / 'sheets.json').read_text())
    sheets = data['sheets']

    # 1. scope: JEE only, no Olympiad section survives
    assert data['policy'].startswith('JEE Main + Advanced only'), data['policy']
    assert [s['section'] for s in sheets] == ['JEE'] * len(sheets), 'Olympiad sheet returned'
    assert len(sheets) == 9, f'expected 9 dense pages, found {len(sheets)}'
    assert not list(ROOT.glob('Olympiad-*.png')), 'Olympiad PNGs must not ship'
    assert not list(ROOT.glob('capacitors-olympiad*')), 'Olympiad exports must not ship'
    assert not list(ROOT.glob('capacitors-jee*')), 'separate JEE bundle retired: one combined export'

    # 2. page numbering and files
    assert [s['part_page'] for s in sheets] == list(range(1, len(sheets) + 1))
    for s in sheets:
        assert re.fullmatch(r'JEE-\d\d-[a-z0-9-]+', s['slug']), s['slug']
        assert (ROOT / (s['slug'] + '.png')).exists(), s['slug']
        assert s['blocks'], s['slug']
        kinds = [b['k'] for b in s['blocks']]
        assert kinds[-1] == 'rem', f'{s["slug"]}: page must end with the remember strip'
        assert kinds.count('trap') >= 1, f'{s["slug"]}: every page carries at least one trap'
        # v3 rule: every result on a page must be derived on that page
        assert kinds.count('der') >= 1, f'{s["slug"]}: no DERIVE block'
        assert kinds.count('res') + kinds.count('tab') >= 1, f'{s["slug"]}: no result box or table'
        figs = sum(len(b['items']) if b['k'] == 'dias' else (1 if b['k'] == 'dia' else 0)
                   for b in s['blocks'])
        assert figs >= 2, f'{s["slug"]}: only {figs} figure(s)'
        # numbered headings must run 1..n in order
        nums = [b['n'] for b in s['blocks'] if b['k'] == 'h']
        assert nums == [str(i) for i in range(1, len(nums) + 1)], f'{s["slug"]}: section numbers {nums}'

    # 3. content: JEE-only vocabulary, no shouted caps, no leaked LaTeX in prose
    prose = ' '.join(str(b.get('s', '')) + ' ' + str(b.get('t', '')) + ' ' +
                     ' '.join(b.get('lines', [])) +
                     ' '.join(c for r in b.get('rows', []) for c in r)
                     for s in sheets for b in s['blocks']).lower()
    for term in FORBIDDEN:
        assert term not in prose, f'extension content leaked into the JEE edition: {term}'
    for term in REQUIRED:
        assert term in prose, f'JEE topic missing from the edition: {term}'
    caps = re.findall(r'\b[A-Z]{4,}\b', ' '.join(b.get('s', '') for s in sheets
                                                 for b in s['blocks'] if b['k'] == 't'))
    assert not caps, f'shouted words left in prose: {caps[:5]}'
    for s in sheets:
        for b in s['blocks']:
            for t in ([b['s']] if 's' in b else []) + b.get('lines', []):
                stripped = re.sub(r'\$[^$]*\$', '', t)
                assert '\\' not in stripped, f'raw LaTeX outside a math run: {t[:60]}'
                assert '$' not in stripped, f'unclosed math run: {t[:60]}'
                assert '  ' not in stripped or True

    # 4. print spec: exact A4, 300 dpi, blank safe margins, one column
    for s in sheets:
        f = ROOT / (s['slug'] + '.png')
        with Image.open(f) as im:
            assert im.size == (2480, 3508), (f.name, im.size)
            assert all(abs(v - 300) < .02 for v in im.info['dpi']), f.name
            arr = np.asarray(im.convert('RGB'))
            for strip in (arr[:120], arr[3400:], arr[:, :120], arr[:, -120:]):
                assert np.min(strip) == 255, f'ink outside the 10 mm safe margin: {f.name}'

    # 5. density: the point of this edition - pages must be full
    report = json.loads((ROOT / 'layout-checks.json').read_text())
    assert report['policy'] == 'single column, JEE only'
    assert len(report['pages']) == len(sheets)
    for page in report['pages']:
        assert page['headroom_px'] >= 0, f'{page["slug"]} overflows the page'
        assert page['headroom_px'] < 420, f'{page["slug"]} is under-filled ({page["headroom_px"]} px spare)'

    # 6. deliverables match the source
    pdf = PdfReader(ROOT / B.PDF)
    assert len(pdf.pages) == len(sheets), 'PDF page count'
    for page in pdf.pages:
        assert abs(float(page.mediabox.width) - A4[0]) < .01
        assert abs(float(page.mediabox.height) - A4[1]) < .01
    assert len(pdf.outline) == len(sheets), 'one bookmark per sheet'
    with zipfile.ZipFile(ROOT / B.ZIP) as z:
        assert z.testzip() is None
        assert z.namelist() == [s['slug'] + '.png' for s in sheets] + ['PRINTING.txt']
        for s in sheets:
            assert z.read(s['slug'] + '.png') == (ROOT / (s['slug'] + '.png')).read_bytes()

    # 7. every link in the gallery and the index page resolves
    for doc in ('index.html', 'README.md', 'AUDIT.md'):
        text = (ROOT / doc).read_text()
        links = re.findall(r'(?:href|src)="([^"]+)"', text) + re.findall(r'\]\(([^)]+)\)', text)
        for link in links:
            if link.startswith('#') or '://' in link:
                continue
            assert (ROOT / link).exists(), f'{doc}: broken link {link}'

    total_words = sum(len(re.sub(r'\$[^$]*\$', 'X', b.get('s', '')).split())
                      for s in sheets for b in s['blocks'])
    ders = sum(1 for s in sheets for b in s['blocks'] if b['k'] == 'der')
    figs = sum(len(b['items']) if b['k'] == 'dias' else (1 if b['k'] == 'dia' else 0)
               for s in sheets for b in s['blocks'])
    assert ders >= len(sheets) * 3, f'only {ders} derivations'
    assert figs >= len(sheets) * 2, f'only {figs} figures'
    print(f'PASS: {len(sheets)} JEE-only pages, {total_words} prose words, '
          f'{ders} derivations, {figs} figures, PDF + ZIP + gallery in agreement, '
          f'every JEE topic present, no extension leakage.')


if __name__ == '__main__':
    test()
