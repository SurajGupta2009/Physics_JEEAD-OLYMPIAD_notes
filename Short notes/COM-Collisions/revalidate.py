"""Structural revalidation of the sound-waves deliverables (representative checks)."""
import json, zipfile, hashlib, sys
from pathlib import Path
from PIL import Image
from pypdf import PdfReader
ROOT = Path(__file__).resolve().parent
FAIL = []

def ok(name, cond, extra=''):
    print(('PASS' if cond else 'FAIL'), name, extra)
    if not cond:
        FAIL.append(name)

data = json.loads((ROOT / 'sheets.json').read_text())
jee = [p for p in data if p['section'] == 'JEE']
oly = [p for p in data if p['section'] == 'Olympiad']
ok('sections present', len(jee) > 0 and len(oly) > 0, f'JEE={len(jee)} Oly={len(oly)}')
ok('JEE numbering 1..n', [p['part_page'] for p in jee] == list(range(1, len(jee) + 1)))
ok('Oly numbering 1..n', [p['part_page'] for p in oly] == list(range(1, len(oly) + 1)))
ok('slugs unique', len({p['slug'] for p in data}) == len(data))
ok('4 cards per page', all(len(p['cards']) == 4 for p in data))
ok('2 diagrams per page', all(len(p['diagrams']) == 2 for p in data))

for p in data[:3] + data[-3:]:
    im = Image.open(ROOT / (p['slug'] + '.png'))
    ok('PNG ' + p['slug'], im.size == (2480, 3508), str(im.size))
    ok('PNG dpi ' + p['slug'], all(abs(d - 300) < 1 for d in im.info.get('dpi', (0, 0))), str(im.info.get('dpi')))

for label, rows in [('com-collisions-all-pngs.zip', data), ('com-collisions-jee-pngs.zip', jee), ('com-collisions-olympiad-pngs.zip', oly)]:
    z = zipfile.ZipFile(ROOT / label)
    names = z.namelist()
    expect = [p['slug'] + '.png' for p in rows]
    ok('zip ' + label + ' order+membership', names == expect, f'{len(names)} files')
    bad = [n for n in names if z.getinfo(n).file_size < 40000]
    ok('zip ' + label + ' file sizes sane', not bad, str(bad[:3]))
    z.close()

for label, rows in [('com-collisions-short-notes.pdf', data), ('com-collisions-jee.pdf', jee), ('com-collisions-olympiad.pdf', oly)]:
    r = PdfReader(str(ROOT / label))
    ok('pdf ' + label + ' pages', len(r.pages) == len(rows), f'{len(r.pages)} pages')
    box = r.pages[0].mediabox
    ok('pdf ' + label + ' A4', abs(float(box.width) - 595.28) < 2 and abs(float(box.height) - 841.89) < 2)

html = (ROOT / 'index.html').read_text()
ok('index has JEE section', 'id="JEE"' in html)
ok('index has Olympiad section', 'id="Olympiad"' in html)
ok('index links all PNGs', all((p['slug'] + '.png') in html for p in data))
missing_links = [n for n in ['SCOPE.md', 'SOURCE-AUDIT.md', 'README.md', 'PRINTING.md'] if n not in html]
ok('index links docs', not missing_links, str(missing_links))

manifest = json.loads((ROOT / 'asset-manifest.json').read_text())
bad = []
for name, meta in manifest.items():
    p = ROOT / name
    if not p.exists() or p.stat().st_size != meta['bytes'] or hashlib.sha256(p.read_bytes()).hexdigest() != meta['sha256']:
        bad.append(name)
ok('asset-manifest fresh', not bad, str(bad[:3]))

src = ROOT.parent.parent / 'centre-of-mass-momentum' / 'Centre-of-mass-momentum.md'
h = hashlib.sha256(src.read_bytes()).hexdigest()
ok('source chapter unchanged (sha prefix)', h.startswith('8ce5e183'), h[:12])

# physics spot re-check embedded in the deliverable text
alltext = json.dumps(data)
ok('corrected chain 3mg present', '3mg' in alltext)
ok('peg contact-loss correction present', '0.854' in alltext)
ok('C9 wall-angle correction present', '63.4' in alltext)
ok('Q18 corrected root present', '1.095' in alltext)

print()
print('structural failures:', len(FAIL), FAIL if FAIL else '(none)')
sys.exit(1 if FAIL else 0)
