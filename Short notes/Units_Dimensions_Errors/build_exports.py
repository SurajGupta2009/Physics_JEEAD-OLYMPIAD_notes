"""Offline exports for Units, Dimensions & Measurement Errors short notes:
three ordered A4 300-DPI lossless PDFs, three PNG-only ZIP bundles, offline HTML gallery, and SHA-256 manifest.
"""
from pathlib import Path
from html import escape
import json, zipfile, zlib, hashlib, sys, platform
from importlib.metadata import version

from PIL import Image
from pypdf import PdfWriter
from pypdf.generic import NameObject, NumberObject, ArrayObject, ByteStringObject
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

ROOT = Path(__file__).resolve().parent
BASE = 'units-dimensions-errors'
PDFS = {
    'All': BASE + '-short-notes.pdf',
    'JEE': BASE + '-jee.pdf',
    'Olympiad': BASE + '-olympiad.pdf',
}
ZIPS = {
    'All': BASE + '-all-pngs.zip',
    'JEE': BASE + '-jee-pngs.zip',
    'Olympiad': BASE + '-olympiad-pngs.zip',
}
TITLES = {
    'All': 'Units, Dimensions & Errors — combined — {n} A4 sheets',
    'JEE': 'Units, Dimensions & Errors — Part I, JEE Main + Advanced — {n} A4 sheets',
    'Olympiad': 'Units, Dimensions & Errors — Part II, Olympiad / extensions — {n} A4 sheets',
}


def _lossless_unique(writer, page, png_path):
    im = Image.open(png_path)
    objs = page['/Resources']['/XObject'].get_object()
    xname = next(iter(objs.keys()))
    obj = objs[xname].get_object().clone(writer)
    obj._data = zlib.compress(im.tobytes(), 9)
    obj[NameObject('/Filter')] = NameObject('/FlateDecode')
    if im.mode == 'P':
        palette = bytes(im.getpalette())
        obj[NameObject('/ColorSpace')] = ArrayObject([
            NameObject('/Indexed'), NameObject('/DeviceRGB'),
            NumberObject(len(palette) // 3 - 1), ByteStringObject(palette),
        ])
    else:
        obj[NameObject('/ColorSpace')] = NameObject('/DeviceRGB')
    obj[NameObject('/BitsPerComponent')] = NumberObject(8)
    for key in ('/DecodeParms', '/Decode'):
        if key in obj:
            del obj[key]
    objs[NameObject(xname)] = writer._add_object(obj)


def build():
    data = json.loads((ROOT / 'sheets.json').read_text())
    groups = {part: [p for p in data if p['section'] == part] for part in ('JEE', 'Olympiad')}
    for label, rows in [('All', data), *groups.items()]:
        pdf_path = ROOT / PDFS[label]
        c = canvas.Canvas(str(pdf_path), pagesize=A4, pageCompression=1)
        c.setTitle(TITLES[label].format(n=len(rows)))
        for p in rows:
            c.bookmarkPage(p['slug'])
            c.addOutlineEntry(f"{p['section']} {p['part_page']:02}: {p['title']}", p['slug'], level=0)
            c.drawImage(str(ROOT / (p['slug'] + '.png')), 0, 0, width=A4[0], height=A4[1])
            c.showPage()
        c.save()

        writer = PdfWriter(clone_from=str(pdf_path))
        for page, row in zip(writer.pages, rows):
            _lossless_unique(writer, page, ROOT / (row['slug'] + '.png'))
        tmp = pdf_path.with_suffix('.tmp.pdf')
        writer.write(tmp)
        tmp.replace(pdf_path)

        with zipfile.ZipFile(ROOT / ZIPS[label], 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as z:
            for p in rows:
                z.write(ROOT / (p['slug'] + '.png'), p['slug'] + '.png')

    style = (
        "@font-face{font-family:Hand;src:url(fonts/PatrickHand-Regular.ttf)}"
        "*{box-sizing:border-box}body{margin:0;background:#f4f7f5;color:#153149;font:17px/1.6 system-ui}"
        "main,header,footer{max-width:1050px;margin:auto;padding:25px}"
        "h1,h2,h3{font-family:Hand,cursive;line-height:1.1}h1{font-size:65px}h2{font-size:44px}h3{font-size:30px;margin:0}"
        "a{color:#087d7d}nav{display:flex;flex-wrap:wrap;gap:12px}"
        "article{background:white;border:1px solid #bbd9d4;border-radius:10px;overflow:hidden;margin:28px 0}"
        "article header{padding:15px}img{width:100%;height:auto;display:block}"
        ".button{display:inline-block;padding:12px;background:#087d7d;color:white;border-radius:6px;text-decoration:none;margin:5px}"
        "section{scroll-margin-top:20px}"
        "@media print{body,main{margin:0;padding:0;background:white;max-width:none}"
        "body>header,footer,section>h2,section>p,section>nav,article header{display:none}"
        "article{border:0;margin:0;border-radius:0;break-after:page}img{width:210mm;height:297mm}}"
        "@page{size:A4 portrait;margin:0}"
    )
    h = (
        '<!doctype html><html lang="en"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1">'
        '<title>Units, Dimensions &amp; Errors — short notes</title><style>' + style + '</style></head><body><header>'
        f'<p>{len(groups["JEE"])} JEE + {len(groups["Olympiad"])} specialised extension sheets · A4 · 300 DPI</p>'
        '<h1>Units, Dimensions &amp; Errors</h1>'
        '<p>Complete Part I before Part II. The boundary is syllabus relevance, not difficulty.</p>'
    )
    for label in ('All', 'JEE', 'Olympiad'):
        h += (f'<a class="button" download href="{ZIPS[label]}">{label} PNG ZIP</a>'
              f'<a class="button" download href="{PDFS[label]}">{label} PDF</a>')
    h += (
        '<p>A4 portrait · one sheet per page · Fit to page, not Fill/Crop.</p>'
        '<nav><a href="SCOPE.md">Coverage &amp; classification</a>'
        '<a href="SOURCE-AUDIT.md">Source audit</a>'
        '<a href="README.md">Rebuild &amp; index</a>'
        '<a href="PRINTING.txt">Printing</a></nav></header><main>'
    )
    for part, rows in groups.items():
        title = 'Part I — JEE Main + Advanced' if part == 'JEE' else 'Part II — Olympiad / specialised extensions'
        h += f'<section id="{part}"><h2>{title}</h2><p>{len(rows)} sheets, independent numbering.</p><nav>'
        h += ''.join(f'<a href="#{part}-{p["part_page"]}">{p["part_page"]:02} {escape(p["title"])}</a>' for p in rows) + '</nav>'
        for p in rows:
            name = p['slug'] + '.png'
            t_esc = escape(p['title'])
            h += (
                f'<article id="{part}-{p["part_page"]}"><header>'
                f'<p>{part} {p["part_page"]:02}/{len(rows):02}</p><h3>{t_esc}</h3>'
                f'<p>{escape(p["subtitle"])}</p>'
                f'<a download href="{name}">Download individual PNG</a></header>'
                f'<a href="{name}"><img loading="lazy" src="{name}" width="2480" height="3508" alt="{part}: {t_esc}"></a></article>'
            )
        h += '</section>'
    h += (
        '</main><footer>Primary source: '
        '<a href="../../units-measurements/Units-measurements.md">units-measurements/Units-measurements.md</a>. '
        'Original chapter unchanged. Patrick Hand, SIL OFL.</footer></body></html>'
    )
    (ROOT / 'index.html').write_text(h)

    assets = {p['slug'] + '.png' for p in data} | set(PDFS.values()) | set(ZIPS.values())
    manifest = {
        name: {
            'bytes': (ROOT / name).stat().st_size,
            'sha256': hashlib.sha256((ROOT / name).read_bytes()).hexdigest(),
        }
        for name in sorted(assets)
    }
    (ROOT / 'asset-manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    environment = {
        'python': sys.version,
        'platform': platform.platform(),
        'packages': {name: version(name) for name in ['Pillow', 'matplotlib', 'numpy', 'reportlab', 'pypdf']},
    }
    (ROOT / 'build-environment.json').write_text(json.dumps(environment, indent=2) + '\n')
    print('Built 3 lossless PDFs, 3 PNG ZIPs, offline gallery, and SHA-256 manifest.')


if __name__ == '__main__':
    build()
