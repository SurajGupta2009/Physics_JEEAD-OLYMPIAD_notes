"""Offline exports. One lossless 8-bit indexed PNG stream per exact A4 PDF page."""
from pathlib import Path
from html import escape
import io, json, struct, zipfile, hashlib, sys, platform
from importlib.metadata import version
from PIL import Image
from pypdf import PdfWriter
from pypdf.generic import NameObject, NumberObject, ArrayObject, ByteStringObject, DictionaryObject
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader

ROOT = Path(__file__).resolve().parent
BASE = 'com-collisions'
PDFS = {'All': BASE + '-short-notes.pdf', 'JEE': BASE + '-jee.pdf', 'Olympiad': BASE + '-olympiad.pdf'}
ZIPS = {'All': BASE + '-all-pngs.zip', 'JEE': BASE + '-jee-pngs.zip', 'Olympiad': BASE + '-olympiad-pngs.zip'}


def _png_chunks(raw):
    pos = 8
    ihdr = None
    idat = bytearray()
    while pos < len(raw):
        ln, ctype = struct.unpack('>I4s', raw[pos:pos + 8])
        chunk = raw[pos + 8:pos + 8 + ln]
        if ctype == b'IHDR':
            ihdr = struct.unpack('>IIBBBBB', chunk)
        elif ctype == b'IDAT':
            idat.extend(chunk)
        elif ctype == b'IEND':
            break
        pos += 12 + ln
    return ihdr, bytes(idat)


def build():
    data = json.loads((ROOT / 'sheets.json').read_text())
    groups = {part: [p for p in data if p['section'] == part] for part in ('JEE', 'Olympiad')}
    stub_buf = io.BytesIO()
    Image.new('RGB', (1, 1), 'white').save(stub_buf, format='PNG')
    stub_reader = ImageReader(stub_buf)

    for label, rows in [('All', data), *groups.items()]:
        pdf_path = ROOT / PDFS[label]
        pdf = canvas.Canvas(str(pdf_path), pagesize=A4, pageCompression=1)
        pdf.setTitle(f'COM & Collisions \u2014 {label} \u2014 {len(rows)} A4 sheets')
        for p in rows:
            pdf.bookmarkPage(p['slug'])
            pdf.addOutlineEntry(f"{p['section']} {p['part_page']:02}: {p['title']}", p['slug'], level=0)
            pdf.drawImage(stub_reader, 0, 0, width=A4[0], height=A4[1])
            pdf.showPage()
        pdf.save()

        writer = PdfWriter(clone_from=pdf_path)
        for page, row in zip(writer.pages, rows):
            png_file = ROOT / (row['slug'] + '.png')
            raw = png_file.read_bytes()
            ihdr, idat = _png_chunks(raw)
            w, h, bpc, ctype, _comp, _flt, ilace = ihdr
            assert (w, h, bpc, ctype, ilace) == (2480, 3508, 8, 3, 0)
            im = Image.open(io.BytesIO(raw))
            palette = bytes(im.getpalette())
            objs = page['/Resources']['/XObject'].get_object()
            images = [v.get_object() for v in objs.values() if v.get_object().get('/Subtype') == '/Image']
            assert len(images) == 1
            obj = images[0]
            obj._data = idat
            obj[NameObject('/Width')] = NumberObject(w)
            obj[NameObject('/Height')] = NumberObject(h)
            obj[NameObject('/Filter')] = NameObject('/FlateDecode')
            obj[NameObject('/DecodeParms')] = DictionaryObject({
                NameObject('/Predictor'): NumberObject(15),
                NameObject('/Colors'): NumberObject(1),
                NameObject('/BitsPerComponent'): NumberObject(8),
                NameObject('/Columns'): NumberObject(w),
            })
            obj[NameObject('/ColorSpace')] = ArrayObject([
                NameObject('/Indexed'),
                NameObject('/DeviceRGB'),
                NumberObject(len(palette) // 3 - 1),
                ByteStringObject(palette),
            ])
            obj[NameObject('/BitsPerComponent')] = NumberObject(8)
            if '/Decode' in obj:
                del obj['/Decode']
        tmp = pdf_path.with_suffix('.tmp.pdf')
        writer.write(tmp)
        tmp.replace(pdf_path)

        with zipfile.ZipFile(ROOT / ZIPS[label], 'w', zipfile.ZIP_DEFLATED) as z:
            for p in rows:
                z.write(ROOT / (p['slug'] + '.png'), p['slug'] + '.png')

    style = (
        '@font-face{font-family:Hand;src:url(fonts/PatrickHand-Regular.ttf)}'
        '*{box-sizing:border-box}body{margin:0;background:#f4f7f5;color:#153149;font:17px/1.6 system-ui}'
        'main,header,footer{max-width:1050px;margin:auto;padding:25px}'
        'h1,h2,h3{font-family:Hand,cursive;line-height:1.1}h1{font-size:65px}h2{font-size:44px}h3{font-size:30px;margin:0}'
        'a{color:#087d7d}nav{display:flex;flex-wrap:wrap;gap:12px}'
        'article{background:white;border:1px solid #bbd9d4;border-radius:10px;overflow:hidden;margin:28px 0}'
        'article header{padding:15px}img{width:100%;height:auto;display:block}'
        '.button{display:inline-block;padding:12px;background:#087d7d;color:white;border-radius:6px;text-decoration:none;margin:5px}'
        'section{scroll-margin-top:20px}'
        '@media print{body,main{margin:0;padding:0;background:white;max-width:none}'
        'body>header,footer,section>h2,section>p,section>nav,article header{display:none}'
        'article{border:0;margin:0;border-radius:0;break-after:page}img{width:210mm;height:297mm}}'
        '@page{size:A4 portrait;margin:0}'
    )
    h = (
        f'<!doctype html><html lang="en"><head><meta charset="utf-8">'
        f'<meta name="viewport" content="width=device-width,initial-scale=1">'
        f'<title>COM and collisions \u2014 short notes</title><style>{style}</style></head><body><header>'
        f'<p>{len(groups["JEE"])} JEE + {len(groups["Olympiad"])} specialised extension sheets \u00b7 A4 \u00b7 300 DPI</p>'
        f'<h1>COM and collisions</h1><p>Complete Part I before Part II. One self-contained revision sheet per syllabus topic.</p>'
    )
    for label in ['All', 'JEE', 'Olympiad']:
        h += f'<a class="button" download href="{ZIPS[label]}">{label} PNG ZIP</a><a class="button" download href="{PDFS[label]}">{label} PDF</a>'
    h += (
        '<p>A4 portrait \u00b7 one sheet per page \u00b7 Fit to page, not Fill/Crop.</p>'
        '<nav><a href="SCOPE.md">Coverage &amp; classification</a><a href="SOURCE-AUDIT.md">Source corrections</a>'
        '<a href="README.md">Rebuild &amp; index</a><a href="PRINTING.md">Printing</a></nav></header><main>'
    )
    for part, rows in groups.items():
        title = 'Part I \u2014 JEE Main + Advanced' if part == 'JEE' else 'Part II \u2014 Olympiad / specialised extensions'
        h += f'<section id="{part}"><h2>{title}</h2><p>{len(rows)} sheets, independent numbering.</p><nav>'
        h += ''.join(f'<a href="#{part}-{p["part_page"]}">{p["part_page"]:02} {escape(p["title"])}</a>' for p in rows) + '</nav>'
        for p in rows:
            name = p['slug'] + '.png'
            title_s = escape(p['title'])
            h += (
                f'<article id="{part}-{p["part_page"]}"><header><p>{part} {p["part_page"]:02}/{len(rows):02}</p>'
                f'<h3>{title_s}</h3><p>{escape(p["subtitle"])}</p><a download href="{name}">Download individual PNG</a></header>'
                f'<a href="{name}"><img loading="lazy" src="{name}" width="2480" height="3508" alt="{part}: {title_s}"></a></article>'
            )
        h += '</section>'
    h += '</main><footer>Primary source: <a href="../../centre-of-mass-momentum/Centre-of-mass-momentum.md">Centre-of-mass-momentum.md</a>. Original chapter unchanged. Patrick Hand, SIL OFL.</footer></body></html>'
    (ROOT / 'index.html').write_text(h)
    assets = {p['slug'] + '.png' for p in data} | set(PDFS.values()) | set(ZIPS.values())
    manifest = {
        name: {'bytes': (ROOT / name).stat().st_size, 'sha256': hashlib.sha256((ROOT / name).read_bytes()).hexdigest()}
        for name in sorted(assets)
    }
    (ROOT / 'asset-manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    environment = {
        'python': sys.version,
        'platform': platform.platform(),
        'packages': {name: version(name) for name in ['Pillow', 'matplotlib', 'numpy', 'reportlab', 'pypdf']},
    }
    (ROOT / 'build-environment.json').write_text(json.dumps(environment, indent=2) + '\n')


if __name__ == '__main__':
    build()
    print('exports built')
