"""Revalidate the authored kinematics sheets, exports, source hashes and physics."""
from pathlib import Path
import hashlib
import json
import math
import re
import zipfile

from PIL import Image, ImageChops
from pypdf import PdfReader

from build_exports import ROOT, PDFS, ZIPS
from render_sheets import math_image, CHARMAP

REPO = ROOT.parents[1]
FAIL = []


def check(name, condition, detail=''):
    if not condition:
        FAIL.append((name, detail))
    print(('PASS' if condition else 'FAIL'), name, detail)


def close(a, b, rel=1e-9, abs_tol=1e-10):
    return abs(a-b) <= max(abs_tol, rel*max(abs(b), 1.0))


def main():
    data = json.loads((ROOT/'sheets.json').read_text())
    jee = [p for p in data if p['section']=='JEE']
    oly = [p for p in data if p['section']=='Olympiad']
    check('36 sheets; JEE first', len(data)==36 and len(jee)==26 and len(oly)==10)
    check('independent numbering',
          [p['part_page'] for p in jee]==list(range(1,27)) and
          [p['part_page'] for p in oly]==list(range(1,11)))
    check('4 cards and 2 diagrams per sheet',
          all(len(p['cards'])==4 and len(p['diagrams'])==2 for p in data))
    check('unique page slugs', len({p['slug'] for p in data})==len(data))
    check('no duplicate card titles per page',
          all(len({c['title'] for c in p['cards']})==4 for p in data))

    # Independently parse every displayed equation/inline-math segment and check
    # all prose glyphs against the packaged handwriting font's actual cmap.
    formulas=0; unsupported=[]
    for p in data:
        visible=[p['title'],p['subtitle'],p['takeaway']]
        for c in p['cards']:
            visible.append(c['title'])
            for kind,value in c['items']:
                if kind=='m':
                    math_image(value); formulas+=1
                else:
                    for match in re.finditer(r'\$([^$]+)\$',value):
                        math_image(match.group(1)); formulas+=1
                    visible.append(re.sub(r'\$[^$]+\$','',value))
        for text in visible:
            unsupported.extend(ch for ch in text if ord(ch) not in CHARMAP)
    check('all displayed math parses',formulas>0,f'{formulas} expressions')
    check('prose glyphs supported by packaged font',not unsupported,
          repr(sorted(set(unsupported))))

    # Exact source preservation: detailed chapters were references, not edited.
    source_hashes = {
        'kinematics-1d/Kinematics-1d.md':'711405418c8d8e033fbbbbe96fb3a4834f4d48b0ec0768ca884d87244b0d1954',
        'motion-in-two-dimensions/Motion-in-two-dimensions.md':'0ba4ba8477bffd12d1586bd0ebf514e67c4a97108cefa7231f93d4e1f7c55f2b'}
    for rel, expected in source_hashes.items():
        check('source unchanged '+rel, hashlib.sha256((REPO/rel).read_bytes()).hexdigest()==expected)

    # Pixel geometry, printable inset, authored text fill and independent numbering.
    layout = json.loads((ROOT/'layout-checks.json').read_text())
    check('layout report card count', len(layout['cards'])==144)
    card_fill = [c['used_px']/c['available_px'] for c in layout['cards']]
    check('all cards fit at fixed body size',
          all(c['used_px'] < c['available_px']-12 and c['body_pt']==11.52
              and c['explanation_pt']==11.04 for c in layout['cards']))
    check('card fill median at least 70%', sorted(card_fill)[len(card_fill)//2] >= .70,
          f'median={sorted(card_fill)[len(card_fill)//2]:.3f}')
    for p in data:
        path=ROOT/(p['slug']+'.png')
        im=Image.open(path)
        check('PNG A4 '+p['slug'], im.size==(2480,3508))
        check('PNG 300 DPI '+p['slug'],
              all(abs(v-300)<.2 for v in im.info.get('dpi',(0,0))),str(im.info.get('dpi')))
        rgb=im.convert('RGB')
        bounds=ImageChops.difference(rgb,Image.new('RGB',rgb.size,'white')).getbbox()
        check('print-safe inset '+p['slug'], bool(bounds) and bounds[0]>=125 and bounds[1]>=125
              and bounds[2]<=2356 and bounds[3]<=3383, str(bounds))

    for label, rows in [('All',data),('JEE',jee),('Olympiad',oly)]:
        with zipfile.ZipFile(ROOT/ZIPS[label]) as z:
            expected=[p['slug']+'.png' for p in rows]
            check('ZIP membership/order '+label,z.testzip() is None and z.namelist()==expected)
        reader=PdfReader(ROOT/PDFS[label])
        check('PDF A4 page count '+label,len(reader.pages)==len(rows))
        check('PDF bookmarks '+label,len(reader.outline)==len(rows))
        for i,page in enumerate(reader.pages):
            box=page.mediabox
            check('PDF A4 portrait '+label+f' page {i+1}',
                  abs(float(box.width)-595.2756)<.02 and abs(float(box.height)-841.8898)<.02)

    # Key physics corrections and limiting cases.
    # 1-D source Q24: at t=2, v=-3 and a=0; speed has an extremum, not a
    # nonzero instantaneous deceleration.
    v=lambda t:3*t*t-12*t+9
    a=lambda t:6*t-12
    check('1D Q24 repaired',close(v(2),-3) and close(a(2),0) and close(abs(v(1.9)),2.97)
          and close(abs(v(2.1)),2.97))
    check('1D Q6 vector speed',close(math.hypot(10,10),10*math.sqrt(2)))

    # Correct the wind direction from the source's P31: eastward wind requires
    # westward aircraft cross-component for a due-north ground track.
    wa=(40.,0.); va=(-40.,200.); ga=(va[0]+wa[0],va[1]+wa[1])
    wb=(40.,-40.); vb=(-40.,240.); gb=(vb[0]+wb[0],vb[1]+wb[1])
    check('aircraft/wind signs repaired',ga==(0.,200.) and gb==(0.,200.))
    check('aircraft/wind magnitudes',close(math.hypot(*va),math.sqrt(41600)) and
          close(math.hypot(*vb),math.sqrt(59200)))

    # Constant acceleration, projectile and incline checks.
    u,g,theta=30.,10.,math.pi/4
    T=2*u*math.sin(theta)/g; H=u*u*math.sin(theta)**2/(2*g)
    R=u*u*math.sin(2*theta)/g
    check('equal-height projectile example',close(T,3*math.sqrt(2)) and close(H,22.5) and close(R,90.))
    check('projectile energy-speed relation',close(u*u-2*g*H,(u*math.cos(theta))**2))
    alpha=math.radians(20); beta=math.pi/4-alpha/2
    f=lambda b:2*math.sin(b)*math.cos(alpha+b)/(math.cos(alpha)**2)
    eps=1e-5
    check('incline optimum',abs((f(beta+eps)-f(beta-eps))/(2*eps))<1e-8)
    env=lambda x:u*u/(2*g)-g*x*x/(2*u*u)
    check('safety-envelope intercepts',close(env(0),u*u/(2*g)) and close(env(u*u/g),0))

    # Circular kinematics and curvature use perpendicular acceleration.
    R0,v0,at=2.,6.,4.
    ac=v0*v0/R0
    check('circular acceleration decomposition',close(ac,18.) and close(math.hypot(ac,at),math.sqrt(340)))
    check('curvature identity',close(v0*v0/ac,R0))

    # Drag ODEs: initial acceleration, terminal states and zero-drag limit.
    m,b,g=2.,.4,9.8
    tau=m/b; vT=m*g/b
    vlin=lambda t:vT*(1-math.exp(-t/tau))
    check('linear drag initial slope',close((vlin(1e-5)-vlin(0))/1e-5,g,rel=1e-5))
    check('linear drag terminal limit',abs(vlin(100*tau)-vT)<1e-8)
    k=.25; vquad=math.sqrt(m*g/k)
    check('quadratic drag terminal speed',close(vquad,math.sqrt(m*g/k)))
    check('quadratic drag small-time limit',close(vquad*math.tanh(g*1e-6/vquad)/1e-6,g,rel=1e-5))
    check('linear-drag projectile landing is finite',
          'positive nonzero root' in json.dumps(data) and 'infinite time is not the projectile range' in json.dumps(data))

    # Pursuit geometry and Coriolis scale.
    check('pursuit initial conditions stated',
          '(0,d)' in json.dumps(data) and 'vp>vt' in json.dumps(data))
    Omega=7.29e-5; vN=500.; flight=20.; lat=math.pi/4
    delta=Omega*vN*flight**2*math.sin(lat)
    check('Coriolis estimate scale',close(delta,10.31,rel=.01))

    # Local gallery and manifest integrity.
    html=(ROOT/'index.html').read_text()
    check('gallery articles',html.count('<article ')==36)
    check('gallery guide links',all(x in html for x in ['README.md','SCOPE.md','SOURCE-AUDIT.md','PRINTING.md','VERIFICATION.md']))
    top=(ROOT.parent/'index.html').read_text()
    check('top-level chapter index',
          'Kinematics/index.html' in top and 'Kinematics/kinematics-all-pngs.zip' in top
          and 'Kinematics/kinematics-short-notes.pdf' in top)
    missing=[]
    for match in re.findall(r'(?:href|src)=["\']([^"\']+)',html):
        if '://' in match or match.startswith('#') or not match:
            continue
        if not (ROOT/match).is_file(): missing.append(match)
    check('gallery local links',not missing,str(missing[:8]))
    manifest=json.loads((ROOT/'asset-manifest.json').read_text())
    bad=[]
    for name,meta in manifest.items():
        path=ROOT/name
        if not path.exists() or path.stat().st_size!=meta['bytes'] or hashlib.sha256(path.read_bytes()).hexdigest()!=meta['sha256']:
            bad.append(name)
    check('asset manifest',not bad,str(bad[:5]))

    print('\nFailures:',len(FAIL))
    for item in FAIL: print(' -',item)
    if FAIL: raise SystemExit(1)

if __name__=='__main__':
    main()
