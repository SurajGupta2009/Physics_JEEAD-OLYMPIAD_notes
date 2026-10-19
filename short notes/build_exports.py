"""Build separate JEE and Olympiad exports, with the combined set always JEE first."""
from pathlib import Path
from html import escape
import json, zipfile
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

ROOT=Path(__file__).resolve().parent
PARTS=('JEE','Olympiad')
PDFS={'All':'capacitors-short-notes.pdf','JEE':'capacitors-jee.pdf','Olympiad':'capacitors-olympiad.pdf'}
ZIPS={'All':'capacitors-a4-pngs.zip','JEE':'capacitors-jee-pngs.zip','Olympiad':'capacitors-olympiad-pngs.zip'}

STYLE='''
@font-face{font-family:Patrick;src:url('fonts/PatrickHand-Regular.ttf')}*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;background:#f3f5f0;color:#153149;font:16px/1.6 system-ui,sans-serif}header,main,footer{max-width:1040px;margin:auto;padding:32px 24px}
header{padding-top:52px}.eyebrow{text-transform:uppercase;letter-spacing:.15em;font-size:12px;color:#087d7d;font-weight:700}
h1{font:clamp(42px,7vw,72px)/1.1 Patrick,cursive;margin:20px 0}h1 em{font-style:normal;color:#087d7d}.intro{max-width:810px;color:#516875}
.button{display:inline-block;background:#087d7d;color:white;border-radius:8px;padding:12px 18px;text-decoration:none;margin:8px 8px 8px 0}.secondary{background:#dceee9;color:#153149}
nav{display:flex;flex-wrap:wrap;gap:7px;margin-top:18px}nav a{font-size:12px;text-decoration:none;color:#31545e;background:white;border:1px solid #cbded9;padding:6px 10px;border-radius:16px}
.part-head{padding:22px 0 30px;scroll-margin-top:18px}.part-head h2{font:40px/1.15 Patrick,cursive;margin:8px 0}.part-head p{color:#516875}
article{background:white;border:1px solid #cbded9;border-radius:12px;margin-bottom:32px;overflow:hidden;scroll-margin-top:16px}.label{display:flex;align-items:center;gap:16px;padding:14px 20px;background:#eff8f5}.label span{font-size:12px;color:#087d7d;white-space:nowrap}.label h3{flex:1;font:27px/1.2 Patrick,cursive;margin:0}.label a{font-size:12px;color:#087d7d;white-space:nowrap}.caption{margin:12px 20px;color:#516875;font-size:14px}img{display:block;width:100%;height:auto}a{color:#087d7d}footer{font-size:13px;color:#516875}
@media(max-width:600px){header,main,footer{padding:20px 10px}.label{padding:10px;gap:8px}.label h3{font-size:21px}.label a{font-size:11px}}
@page{size:A4 portrait;margin:0}@media print{header,footer,.label,.caption,.part-head{display:none}body,main{margin:0;padding:0;background:white;max-width:none}article{border:0;border-radius:0;margin:0;break-after:page;width:210mm;height:297mm}article:last-child{break-after:auto}img{width:210mm;height:297mm}}
'''

def build():
    data=json.loads((ROOT/'sheets.json').read_text())
    groups={part:[p for p in data if p['section']==part] for part in PARTS}
    assert [p['section'] for p in data]==['JEE']*len(groups['JEE'])+['Olympiad']*len(groups['Olympiad'])
    for p in data:
        with Image.open(ROOT/(p['slug']+'.png')) as im:
            assert im.size==(2480,3508)
            assert all(abs(v-300)<.02 for v in im.info['dpi'])
            im.verify()
    instructions='''CAPACITORS: JEE FIRST, OLYMPIAD SECOND

Part I: JEE/ (11 sheets). Read these first for the capacitor chapter.
Part II: Olympiad/ (6 sheets). Optional specialised extensions after the JEE core.
The distinction is relevance to this chapter's JEE preparation, not difficulty.
Each part has its own page numbers, PNG ZIP and exact-A4 PDF.
The combined exports contain JEE first, then Olympiad.

Every PNG is 2480 x 3508 pixels with 300 DPI metadata.
Print A4 portrait, one image per page. Select Fit to page, not Fill/Crop.
Keep photo cropping and automatic landscape rotation off.
Artwork includes approximately 10 mm safe margins.
For predictable pagination use the PDF. Colour is recommended.
Teal WHY lines explain physical meaning; red WATCH lines mark conditions/traps.

Scope nuance: basic AC and impedance are JEE topics elsewhere in the syllabus.
Specialised filters, probe compensation and oscillators are placed in this
extension set rather than interrupting the capacitor-chapter reading sequence.
This is a study grouping, not a guarantee about what can never appear in an exam.
'''
    (ROOT/'PRINTING.txt').write_text(instructions)
    for label,selection in [('All',data),*groups.items()]:
        pdf=canvas.Canvas(str(ROOT/PDFS[label]),pagesize=A4,pageCompression=1)
        pdf.setTitle(f'Capacitors — {label} — {len(selection)} A4 sheets')
        pdf.setAuthor('Physics JEE Advanced / Olympiad Notes')
        for p in selection:
            pdf.bookmarkPage(p['slug'])
            pdf.addOutlineEntry(f"{p['section']} {p['part_page']:02}: {p['title']}",p['slug'],level=0)
            pdf.drawImage(str(ROOT/(p['slug']+'.png')),0,0,width=A4[0],height=A4[1]);pdf.showPage()
        pdf.save()
        with zipfile.ZipFile(ROOT/ZIPS[label],'w',zipfile.ZIP_DEFLATED) as z:
            for p in selection:
                relative=p['slug']+'.png';z.write(ROOT/relative,relative)
            z.writestr('PRINTING.txt',instructions)
    descriptions={
        'JEE':'Part I — JEE Mains + Advanced: core capacitor ideas and useful applications, including harder derivable problems. No specialised extension sheet is needed to finish this part.',
        'Olympiad':'Part II — Olympiad / extensions: microscopic models, specialised AC circuits, coupled dynamics, matrix/image/conformal tools and instability theory. Read after Part I.'}
    sections=[]
    for part in PARTS:
        rows=groups[part];n=len(rows)
        nav=''.join(f'<a href="#{part}-{p["part_page"]}">{p["part_page"]:02} {escape(p["title"])}</a>' for p in rows)
        section=f'''<section aria-labelledby="{part}-title"><div class="part-head" id="{part}">
<div class="eyebrow">{n} sheets · own page numbering · A4 portrait</div>
<h2 id="{part}-title">{'Part I · JEE' if part=='JEE' else 'Part II · Olympiad / Extensions'}</h2>
<p>{escape(descriptions[part])}</p>
<a class="button" href="{ZIPS[part]}" download>Download {part} PNGs · ZIP</a>
<a class="button secondary" href="{PDFS[part]}" download>{part} A4 PDF</a><nav>{nav}</nav></div>'''
        for p in rows:
            name=p['slug']+'.png';i=p['part_page']
            section+=f'''<article id="{part}-{i}"><div class="label"><span>{part} {i:02} / {n:02}</span>
<h3>{escape(p['title'])}</h3><a href="{name}" download>Download PNG</a></div>
<p class="caption">{escape(p['subtitle'])}</p><a href="{name}" target="_blank" rel="noopener" aria-label="Open {part} sheet {i} full size">
<img src="{name}" width="2480" height="3508" alt="{part} A4 capacitor notes: {escape(p['title'])}" loading="lazy"></a></article>'''
        sections.append(section+'</section>')
    html='''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Capacitors · JEE first, Olympiad second</title><style>'''+STYLE+'''</style></head><body><header>
<div class="eyebrow">11 JEE sheets + 6 extension sheets · 300 DPI</div><h1>Capacitors.<br><em>JEE first. Explore next.</em></h1>
<p class="intro">Complete the JEE-focused capacitor revision before opening the separate Olympiad / extension part. This is a relevance-based split, not an easy-versus-hard split: useful difficult applications remain in JEE.</p>
<a class="button" href="#JEE">Start Part I · JEE</a><a class="button secondary" href="#Olympiad">Go to extensions</a>
<p><a href="capacitors-a4-pngs.zip" download>Combined PNG ZIP</a> · <a href="capacitors-short-notes.pdf" download>Combined A4 PDF</a> · <a href="SCOPE.md">What moved, and why</a></p>
<p class="intro"><strong>Print:</strong> A4 portrait · one image per page · Fit to page, not Fill/Crop. Every PNG is 2480 × 3508 at 300 DPI. Explanations, colours and diagram labels are preserved.</p></header><main>'''+''.join(sections)+'''</main><footer>
Basic AC remains relevant to JEE in its own chapter; specialised circuit applications here are kept in the extension sequence, as requested. The grouping does not predict every possible examination question.<br>
Based on <a href="../capacitors/Capacitors.md">Capacitors.md</a>. Full proofs and the practice paper remain in the original chapter.
<a href="PRINTING.txt">Print instructions</a> · <a href="README.md">Index and rebuild instructions</a> · Patrick Hand (SIL OFL).
</footer></body></html>'''
    (ROOT/'index.html').write_text(html)
    rows='\n'.join(f'| {p["section"]} {p["part_page"]:02} | [{p["title"]}]({p["slug"]}.png) | {p["source"]} |' for p in data)
    readme='''# Capacitors — JEE first, Olympiad second

**17 A4 portrait PNGs: 11 JEE sheets followed by 6 Olympiad/extension sheets.**
Handwritten-style prose, teacher explanations, accurate equations, colours, labelled diagrams and graphs are preserved.

## Downloads

| Part | PNG bundle | A4 PDF |
|---|---|---|
| **Part I: JEE — read first** | [11 JEE PNGs](capacitors-jee-pngs.zip) | [JEE PDF](capacitors-jee.pdf) |
| Part II: Olympiad / extensions | [6 extension PNGs](capacitors-olympiad-pngs.zip) | [Extension PDF](capacitors-olympiad.pdf) |
| Combined — JEE then Olympiad | [All 17 PNGs](capacitors-a4-pngs.zip) | [Combined PDF](capacitors-short-notes.pdf) |

- [Offline gallery, grouped by part](index.html)
- [Scope decisions and old-page mapping](SCOPE.md)
- [Printing instructions](PRINTING.txt)
- [Detailed chapter](../capacitors/Capacitors.md)

The PNGs live in **`JEE/`** and **`Olympiad/`**, with independent page numbering and a visible part label on every sheet. Combined exports put all JEE pages first. The previous mixed edition has been replaced, not left beside the new edition to confuse the reading order.

## How the boundary was chosen

**Relevance, not toughness.** JEE retains core electrostatics, capacitance, dielectrics, energy, force, charge conservation, networks and ordinary RC applications. Harder but useful applications such as bridges, cube networks, ladders and liquid rise stay there. Breakdown ratings are brought into the JEE checklist.

Specialised microscopic response, dispersive materials, compensation/oscillators, coupled RC eigenmodes, capacitance matrices, reciprocity, exact image/conformal tools, spheroids, porous electrodes and instability theory go in the extension part. Previous **page 12 is now Olympiad 02**, and **page 14 is now Olympiad 05**. Mixed pages were actually edited: basic branch charge stays in JEE, matrix dynamics moves out; exact two-wire formulas move out, ordinary connected-sphere reasoning stays in.

This is a **chapter-focused study grouping**, not a claim that every extension topic is absent from the entire JEE syllabus. In particular AC impedance belongs in JEE's AC chapter; specialised filters, compensated probes and threshold circuits are kept here as extras. See `SCOPE.md`.

## Print specification

Every PNG is **2480 × 3508 at 300 DPI**, A4 portrait proportions, with approximately 10 mm safe margins. Body text is 11.5 pt equivalent, explanations 11 pt, equations nominally 12 pt with occasional width fitting down to 10 pt. PDF media boxes are exact A4, 210 × 297 mm.

Print **A4, portrait, one sheet per page, Fit to page / printable area**. Do not select photo-style Fill/Crop. Colour is recommended; labels retain meaning in grayscale.

## Page index

| Part / local page | PNG | Source |
|---|---|---|
'''+rows+'''

## Rebuild and test

```sh
python -m pip install -r "short notes/requirements.txt"
python "short notes/render_sheets.py"
python "short notes/build_exports.py"
python "short notes/test_exports.py"
```

`sheets.json` contains editable content, section assignment, independent numbering and old-page mapping. `render_sheets.py` checks formula parsing, text width and overflow without shrinking body type. `layout-checks.json` records every card. Export tests cover dimensions, DPI, safe margins, ordering, section membership, ZIP contents, local links, A4 PDF page boxes and representative physics.

These are conceptual short notes, not every worked exercise; the detailed source retains derivations and the complete paper/solutions. Patrick Hand is under the SIL Open Font License in `fonts/OFL.txt`.
'''
    (ROOT/'README.md').write_text(readme)
    counts={part:len(rows) for part,rows in groups.items()}
    print(f'Built {len(data)} sheets in order {counts}; separate and combined PDFs/ZIPs; grouped gallery.')

if __name__=='__main__':build()
