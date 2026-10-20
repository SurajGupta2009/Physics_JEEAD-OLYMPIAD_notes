"""Offline exports. One lossless source PNG per exact A4 PDF page."""
from pathlib import Path
from html import escape
import json,zipfile
from reportlab import rl_config
rl_config.useA85 = 0  # Lossless binary PDF streams; avoid ASCII85 size overhead.
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
ROOT=Path(__file__).resolve().parent
BASE='rigid-body-dynamics'
PDFS={'All':BASE+'-short-notes.pdf','JEE':BASE+'-jee.pdf','Olympiad':BASE+'-olympiad.pdf'}
ZIPS={'All':BASE+'-all-pngs.zip','JEE':BASE+'-jee-pngs.zip','Olympiad':BASE+'-olympiad-pngs.zip'}
def build():
 data=json.loads((ROOT/'sheets.json').read_text())
 groups={part:[p for p in data if p['section']==part] for part in ('JEE','Olympiad')}
 for label,rows in [('All',data),*groups.items()]:
  pdf=canvas.Canvas(str(ROOT/PDFS[label]),pagesize=A4,pageCompression=1)
  pdf.setTitle(f'Rigid body dynamics — {label} — {len(rows)} A4 sheets')
  for p in rows:
   pdf.bookmarkPage(p['slug']);pdf.addOutlineEntry(f"{p['section']} {p['part_page']:02}: {p['title']}",p['slug'],level=0)
   pdf.drawImage(str(ROOT/(p['slug']+'.png')),0,0,width=A4[0],height=A4[1]);pdf.showPage()
  pdf.save()
  with zipfile.ZipFile(ROOT/ZIPS[label],'w',zipfile.ZIP_DEFLATED) as z:
   # PNGs only; archive insertion order is the reading order, including in All.
   for p in rows:z.write(ROOT/(p['slug']+'.png'),p['slug']+'.png')
 style="""@font-face{font-family:Hand;src:url(fonts/PatrickHand-Regular.ttf)}*{box-sizing:border-box}body{margin:0;background:#f4f7f5;color:#153149;font:17px/1.6 system-ui}main,header,footer{max-width:1050px;margin:auto;padding:25px}h1,h2,h3{font-family:Hand,cursive;line-height:1.1}h1{font-size:65px}h2{font-size:44px}h3{font-size:30px;margin:0}a{color:#087d7d}nav{display:flex;flex-wrap:wrap;gap:12px}article{background:white;border:1px solid #bbd9d4;border-radius:10px;overflow:hidden;margin:28px 0}article header{padding:15px}img{width:100%;height:auto;display:block}.button{display:inline-block;padding:12px;background:#087d7d;color:white;border-radius:6px;text-decoration:none;margin:5px}section{scroll-margin-top:20px}@media print{body,main{margin:0;padding:0;background:white;max-width:none}body>header,footer,section>h2,section>p,section>nav,article header{display:none}article{border:0;margin:0;border-radius:0;break-after:page}img{width:210mm;height:297mm}}@page{size:A4 portrait;margin:0}"""
 h=f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Rigid body dynamics — short notes</title><style>{style}</style></head><body><header><p>{len(groups["JEE"])} JEE + {len(groups["Olympiad"])} specialised extension sheets · A4 · 300 DPI</p><h1>Rigid body dynamics</h1><p>Complete Part I before Part II. The boundary is relevance, not difficulty.</p>'
 for label in ['All','JEE','Olympiad']:
  h+=f'<a class="button" download href="{ZIPS[label]}">{label} PNG ZIP</a><a class="button" download href="{PDFS[label]}">{label} PDF</a>'
 h+='<p>A4 portrait · one sheet per page · Fit to page, not Fill/Crop.</p><nav><a href="SCOPE.md">Coverage &amp; classification</a><a href="SOURCE-AUDIT.md">Source corrections</a><a href="README.md">Rebuild &amp; index</a><a href="PRINTING.txt">Printing</a></nav></header><main>'
 for part,rows in groups.items():
  title='Part I — JEE Main + Advanced' if part=='JEE' else 'Part II — Olympiad / specialised extensions'
  h+=f'<section id="{part}"><h2>{title}</h2><p>{len(rows)} sheets, independent numbering.</p><nav>'
  h+=''.join(f'<a href="#{part}-{p["part_page"]}">{p["part_page"]:02} {escape(p["title"])}</a>' for p in rows)+'</nav>'
  for p in rows:
   name=p['slug']+'.png';title=escape(p['title'])
   h+=f'<article id="{part}-{p["part_page"]}"><header><p>{part} {p["part_page"]:02}/{len(rows):02}</p><h3>{title}</h3><p>{escape(p["subtitle"])}</p><a download href="{name}">Download individual PNG</a></header><a href="{name}"><img loading="lazy" src="{name}" width="2480" height="3508" alt="{part}: {title}"></a></article>'
  h+='</section>'
 h+='</main><footer>Primary source: <a href="../../rotational-mechanics/Rotational-mechanics.md">Rotational-mechanics.md</a>. Original chapter unchanged. Patrick Hand, SIL OFL.</footer></body></html>'
 (ROOT/'index.html').write_text(h)
 print('Built three PDFs with ordered bookmarks, three PNG-only ZIPs, and an offline gallery.')
if __name__=='__main__':build()
