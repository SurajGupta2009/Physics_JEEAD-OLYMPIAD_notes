"""Offline exports: three ordered A4 PDFs and three PNG-only ZIPs, plus the gallery.

Each PDF page is exactly one source PNG drawn over the full A4 media box, so a
"Fit to page" print is a 1:1 reproduction of the sheet.  The PNG pixel stream is
re-used losslessly inside the PDF (RGB or indexed, whichever the renderer wrote).
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
BASE = 'elasticity'
PDFS = {'All': BASE + '-short-notes.pdf',
        'JEE': BASE + '-jee.pdf',
        'Olympiad': BASE + '-olympiad.pdf'}
ZIPS = {'All': BASE + '-all-pngs.zip',
        'JEE': BASE + '-jee-pngs.zip',
        'Olympiad': BASE + '-olympiad-pngs.zip'}

TITLES = {'All': 'Elasticity — combined — {n} A4 sheets',
          'JEE': 'Elasticity — Part I, JEE Main + Advanced — {n} A4 sheets',
          'Olympiad': 'Elasticity — Part II, Olympiad / extensions — {n} A4 sheets'}


def _lossless(page, png_path):
    """Replace reportlab's RGB expansion with the raw source samples, deflated."""
    im = Image.open(png_path)
    objs = page['/Resources']['/XObject'].get_object()
    images = [v.get_object() for v in objs.values()
              if v.get_object().get('/Subtype') == '/Image']
    assert len(images) == 1, png_path
    obj = images[0]
    obj._data = zlib.compress(im.tobytes(), 9)
    obj[NameObject('/Filter')] = NameObject('/FlateDecode')
    if im.mode == 'P':
        palette = bytes(im.getpalette())
        obj[NameObject('/ColorSpace')] = ArrayObject([
            NameObject('/Indexed'), NameObject('/DeviceRGB'),
            NumberObject(len(palette) // 3 - 1), ByteStringObject(palette)])
    else:
        assert im.mode == 'RGB', (png_path, im.mode)
        obj[NameObject('/ColorSpace')] = NameObject('/DeviceRGB')
    obj[NameObject('/BitsPerComponent')] = NumberObject(8)
    for key in ('/DecodeParms', '/Decode'):
        if key in obj:
            del obj[key]


def build():
    data = json.loads((ROOT / 'sheets.json').read_text())
    groups = {part: [p for p in data if p['section'] == part]
              for part in ('JEE', 'Olympiad')}
    for label, rows in [('All', data), *groups.items()]:
        pdf = canvas.Canvas(str(ROOT / PDFS[label]), pagesize=A4, pageCompression=1)
        pdf.setTitle(TITLES[label].format(n=len(rows)))
        for p in rows:
            pdf.bookmarkPage(p['slug'])
            pdf.addOutlineEntry(
                f"{p['section']} {p['part_page']:02}: {p['title']}",
                p['slug'], level=0)
            pdf.drawImage(str(ROOT / (p['slug'] + '.png')), 0, 0,
                          width=A4[0], height=A4[1])
            pdf.showPage()
        pdf.save()

        path = ROOT / PDFS[label]
        writer = PdfWriter(clone_from=str(path))
        for page, row in zip(writer.pages, rows):
            _lossless(page, ROOT / (row['slug'] + '.png'))
        tmp = path.with_suffix('.tmp.pdf')
        writer.write(tmp)
        tmp.replace(path)

        with zipfile.ZipFile(ROOT / ZIPS[label], 'w', zipfile.ZIP_DEFLATED) as z:
            for p in rows:
                z.write(ROOT / (p['slug'] + '.png'), p['slug'] + '.png')

    style = """@font-face{font-family:Hand;src:url(fonts/PatrickHand-Regular.ttf)}*{box-sizing:border-box}body{margin:0;background:#f4f7f5;color:#153149;font:17px/1.6 system-ui}main,header,footer{max-width:1050px;margin:auto;padding:25px}h1,h2,h3{font-family:Hand,cursive;line-height:1.1}h1{font-size:65px}h2{font-size:44px}h3{font-size:30px;margin:0}a{color:#087d7d}nav{display:flex;flex-wrap:wrap;gap:12px}article{background:white;border:1px solid #bbd9d4;border-radius:10px;overflow:hidden;margin:28px 0}article header{padding:15px}img{width:100%;height:auto;display:block}.button{display:inline-block;padding:12px;background:#087d7d;color:white;border-radius:6px;text-decoration:none;margin:5px}section{scroll-margin-top:20px}@media print{body,main{margin:0;padding:0;background:white;max-width:none}body>header,footer,section>h2,section>p,section>nav,article header{display:none}article{border:0;margin:0;border-radius:0;break-after:page}img{width:210mm;height:297mm}}@page{size:A4 portrait;margin:0}"""
    h = ('<!doctype html><html lang="en"><head><meta charset="utf-8">'
         '<meta name="viewport" content="width=device-width,initial-scale=1">'
         '<title>Elasticity — short notes</title><style>' + style + '</style></head><body><header>'
         f'<p>{len(groups["JEE"])} JEE + {len(groups["Olympiad"])} specialised extension sheets · A4 · 300 DPI</p>'
         '<h1>Elasticity</h1>'
         '<p>Complete Part I before Part II. The boundary is relevance, not difficulty.</p>')
    for label in ('All', 'JEE', 'Olympiad'):
        h += (f'<a class="button" download href="{ZIPS[label]}">{label} PNG ZIP</a>'
              f'<a class="button" download href="{PDFS[label]}">{label} PDF</a>')
    h += ('<p>A4 portrait · one sheet per page · Fit to page, not Fill/Crop.</p>'
          '<nav><a href="SCOPE.md">Coverage &amp; classification</a>'
          '<a href="SOURCE-AUDIT.md">Source corrections</a>'
          '<a href="README.md">Rebuild &amp; index</a>'
          '<a href="PRINTING.txt">Printing</a></nav></header><main>')
    for part, rows in groups.items():
        title = ('Part I — JEE Main + Advanced' if part == 'JEE'
                 else 'Part II — Olympiad / specialised extensions')
        h += (f'<section id="{part}"><h2>{title}</h2>'
              f'<p>{len(rows)} sheets, independent numbering.</p><nav>')
        h += ''.join(f'<a href="#{part}-{p["part_page"]}">{p["part_page"]:02} '
                     f'{escape(p["title"])}</a>' for p in rows) + '</nav>'
        for p in rows:
            name = p['slug'] + '.png'
            title = escape(p['title'])
            h += (f'<article id="{part}-{p["part_page"]}"><header>'
                  f'<p>{part} {p["part_page"]:02}/{len(rows):02}</p><h3>{title}</h3>'
                  f'<p>{escape(p["subtitle"])}</p>'
                  f'<a download href="{name}">Download individual PNG</a></header>'
                  f'<a href="{name}"><img loading="lazy" src="{name}" width="2480" '
                  f'height="3508" alt="{part}: {title}"></a></article>')
        h += '</section>'
    h += ('</main><footer>Primary source: '
          '<a href="../../elasticity/Elasticity.md">elasticity/Elasticity.md</a>. '
          'Original chapter unchanged. Patrick Hand, SIL OFL.</footer></body></html>')
    (ROOT / 'index.html').write_text(h)

    assets = {p['slug'] + '.png' for p in data} | set(PDFS.values()) | set(ZIPS.values())
    manifest = {name: {'bytes': (ROOT / name).stat().st_size,
                       'sha256': hashlib.sha256((ROOT / name).read_bytes()).hexdigest()}
                for name in sorted(assets)}
    (ROOT / 'asset-manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    environment = {'python': sys.version, 'platform': platform.platform(),
                   'packages': {name: version(name) for name in
                                ['Pillow', 'matplotlib', 'numpy', 'reportlab', 'pypdf']}}
    (ROOT / 'build-environment.json').write_text(json.dumps(environment, indent=2) + '\n')
    print('Built three PDFs with ordered bookmarks, three PNG-only ZIPs, and an offline gallery.')


if __name__ == '__main__':
    build()
