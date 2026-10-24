"""Regression checks for section relevance, reading order and print-ready exports."""
from pathlib import Path
import json,re,zipfile
import numpy as np
from PIL import Image
from pypdf import PdfReader
from reportlab.lib.pagesizes import A4
from build_exports import PDFS,ZIPS
ROOT=Path(__file__).resolve().parent

def test():
    data=json.loads((ROOT/'sheets.json').read_text())
    sections={part:[p for p in data if p['section']==part] for part in ('JEE','Olympiad')}
    assert [len(sections[k]) for k in ('JEE','Olympiad')]==[11,6]
    assert [p['section'] for p in data]==['JEE']*11+['Olympiad']*6
    files=[p['slug']+'.png' for p in data]
    assert len(files)==17 and len(set(files))==17
    actual={p.name for p in ROOT.glob('*.png')}
    assert actual==set(files),'Stale/missing part images'
    assert not list(ROOT.glob('[0-9][0-9]-*.png')),'Mixed-edition root PNGs should not remain'
    for part,rows in sections.items():
        assert [p['part_page'] for p in rows]==list(range(1,len(rows)+1))
        assert all(p['slug'].startswith(f'{part}-{p["part_page"]:02}-') for p in rows)
    # Explicit requests: old 12 and old 14 are extension-only.
    assert next(p for p in data if p['previous_page']==12)['slug']=='Olympiad-02-ac-and-applications'
    assert next(p for p in data if p['previous_page']==14)['slug']=='Olympiad-05-shape-and-conformal-tools'
    # Guard against re-mixing specialised material into core explanations/formulas.
    core=' '.join(text for p in sections['JEE'] for c in p['cards'] for _,text in c['items']).lower()
    for term in ['debye','clausius','paschen','eigenvalue','arcosh','conformal','rayleigh','spheroid','porous','oscillator','ferroelectric','piezoelectric']:
        assert term not in core,f'Extension content leaked into JEE: {term}'
    assert 'bridge' in core and 'liquid' in core and 'cube' in core and 'branch' in core
    # Parse and inspect all print files.
    for f in files:
        with Image.open(ROOT/f) as im:
            assert im.size==(2480,3508),(f,im.size)
            assert all(abs(v-300)<.02 for v in im.info['dpi'])
            arr=np.asarray(im.convert('RGB'))
            for strip in [arr[:120],arr[-120:],arr[:,:120],arr[:,-120:]]:
                assert np.min(strip)==255,f'Ink outside safe margin: {f}'
    report=json.loads((ROOT/'layout-checks.json').read_text())
    assert len(report['cards'])==4*len(data)
    assert all(p['used_px']<p['available_px']-12 for p in report['cards'])
    for p in data:
        for c in p['cards']:
            if c['title']!='Six quick sanity checks':assert any(k=='why' for k,_ in c['items']),c['title']
    for label,rows in [('All',data),*sections.items()]:
        expected=[p['slug']+'.png' for p in rows]
        pdf=PdfReader(ROOT/PDFS[label]);assert len(pdf.pages)==len(rows)
        assert [item.title for item in pdf.outline]==[f'{p["section"]} {p["part_page"]:02}: {p["title"]}' for p in rows]
        for p in pdf.pages:
            assert abs(float(p.mediabox.width)-A4[0])<.01
            assert abs(float(p.mediabox.height)-A4[1])<.01
        with zipfile.ZipFile(ROOT/ZIPS[label]) as z:
            assert z.testzip() is None
            assert z.namelist()==expected+['PRINTING.txt'],'Wrong ZIP order/membership'
            for f in expected:assert z.read(f)==(ROOT/f).read_bytes()
    html=(ROOT/'index.html').read_text()
    assert html.index('id="JEE"')<html.index('id="Olympiad"')
    for link in re.findall(r'(?:href|src)="([^"]+)"',html):
        if not link.startswith('#'):assert (ROOT/link).exists(),link
    # Representative physics checks independent of layout.
    c1,c2,v1,v2=2e-6,3e-6,100,0
    assert abs((c1*v1+c2*v2)/(c1+c2)-40)<1e-12
    assert abs(.5*c1*c2/(c1+c2)*(v1-v2)**2-.006)<1e-12
    a=np.zeros((6,6));rhs=np.zeros(6)
    for node in range(1,7):
        for neighbour in [node^1,node^2,node^4]:
            a[node-1,node-1]+=1
            if 1<=neighbour<=6:a[node-1,neighbour-1]-=1
            elif neighbour==0:rhs[node-1]+=1
    potentials=np.r_[1,np.linalg.solve(a,rhs),0]
    assert abs(sum(1-potentials[j] for j in [1,2,4])-6/5)<1e-12
    x=(np.sqrt(5)-1)/2;assert abs(x-(1+x)/(2+x))<1e-12
    assert np.allclose(np.linalg.eigvalsh([[2,-1],[-1,1]]),[(3-np.sqrt(5))/2,(3+np.sqrt(5))/2])
    print('PASS: 11 JEE then 6 extension sheets; scope and local numbering; 68 unclipped cards;')
    print('      all PNGs A4/300 DPI with safe margins; 3 PDFs/bookmark orders; 3 ZIPs; gallery; physics checks.')

if __name__=='__main__':test()
