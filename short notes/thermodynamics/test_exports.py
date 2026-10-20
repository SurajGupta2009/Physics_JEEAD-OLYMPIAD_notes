"""Run from any directory after author/render/export. Checks are representative, not a proof of every line."""
from pathlib import Path
import hashlib,json,math,re,zipfile
from urllib.parse import unquote,urlsplit
from PIL import Image,ImageChops
from pypdf import PdfReader
from matplotlib.ft2font import FT2Font
import numpy as np
from diagrams import coexistence
from build_exports import ROOT,PDFS,ZIPS
checks=0
models=[]
def check(ok,message):
 global checks
 checks+=1
 assert ok,message
def near(name,value,target,rel=.02,absolute=1e-8):
 check(abs(value-target)<=max(absolute,rel*abs(target)),f'{name}: {value} vs {target}')
 models.append({'name':name,'value':float(value),'expected':float(target)})
def main():
 data=json.loads((ROOT/'sheets.json').read_text());check(len(data)==28,'page count')
 check([p['section'] for p in data]==['JEE']*21+['Olympiad']*7,'reading order')
 check(len({p['slug'] for p in data})==28,'unique filenames')
 check(sum(len(p['cards']) for p in data)==112,'card count')
 check(sum(len(p['diagrams']) for p in data)==56,'diagram count')
 check(sum(k=='m' for p in data for c in p['cards'] for k,s in c['items'])==248,'math block count')
 cmap=FT2Font(str(ROOT/'fonts/PatrickHand-Regular.ttf')).get_charmap()
 for p in data:
  prose=[p['title'],p['subtitle'],p['source'],p['takeaway']]+[c['title'] for c in p['cards']]+[s for c in p['cards'] for k,s in c['items'] if k!='m']
  check(all(ord(ch) in cmap or ch=='\n' for text in prose for ch in text),'font coverage '+p['slug'])
 for section,count in [('JEE',21),('Olympiad',7)]:
  rows=[p for p in data if p['section']==section]
  check([p['part_page'] for p in rows]==list(range(1,count+1)),'numbering '+section)
  check({str(p.relative_to(ROOT)) for p in (ROOT/section).glob('*.png')}=={p['slug']+'.png' for p in rows},'stale/missing pages')
 for p in data:
  im=Image.open(ROOT/(p['slug']+'.png'));check(im.size==(2480,3508),'dimensions')
  check(all(abs(d-300)<.1 for d in im.info['dpi']),'DPI')
  check(im.mode=='P','indexed PNG')
  rgb=im.convert('RGB');white=Image.new('RGB',rgb.size,'white');bounds=ImageChops.difference(rgb,white).getbbox()
  check(bounds and bounds[0]>=125 and bounds[1]>=125 and bounds[2]<=2356 and bounds[3]<=3383,'safe margin '+p['slug'])
 layout=json.loads((ROOT/'layout-checks.json').read_text());check(len(layout['cards'])==112,'layout manifest')
 for c in layout['cards']:
  check(c['used_px']<c['available_px']-12,'card overflow '+c['card'])
  check(c['body_pt']==11.52 and c['explanation_pt']==11.04,'body text never shrunk')
 for label,rows in [('All',data),('JEE',data[:21]),('Olympiad',data[21:])]:
  with zipfile.ZipFile(ROOT/ZIPS[label]) as z:
   check(z.testzip() is None,'zip CRC')
   check(z.namelist()==[p['slug']+'.png' for p in rows],'zip reading order')
   for p in rows:check(z.read(p['slug']+'.png')==(ROOT/(p['slug']+'.png')).read_bytes(),'zip bytes')
  reader=PdfReader(ROOT/PDFS[label]);check(len(reader.pages)==len(rows),'PDF page count')
  check(len(reader.outline)==len(rows),'bookmark count')
  for index,(page,p) in enumerate(zip(reader.pages,rows)):
   check(abs(float(page.mediabox.width)-595.2756)<.01 and abs(float(page.mediabox.height)-841.8898)<.01,'A4 portrait')
   check(reader.get_destination_page_number(reader.outline[index])==index,'bookmark destination')
   check(p['title'] in reader.outline[index].title,'bookmark title')
   objs=page['/Resources']['/XObject'].get_object()
   images=[o.get_object() for o in objs.values() if o.get_object().get('/Subtype')=='/Image'];check(len(images)==1,'one sheet/page')
   obj=images[0];im=Image.open(ROOT/(p['slug']+'.png'))
   check(obj['/Width']==2480 and obj['/Height']==3508,'PDF resolution')
   check(obj.get_data()==im.tobytes(),'PDF lossless source indices')
   check(obj['/ColorSpace'][3].original_bytes==bytes(im.getpalette()),'PDF lossless source palette')
 html=(ROOT/'index.html').read_text();check(html.count('<article ')==28,'gallery count')
 for url in re.findall(r'(?:href|src)=[\"\']([^\"\']+)',html):
  path=urlsplit(url)
  if path.scheme or not path.path:continue
  check((ROOT/unquote(path.path)).is_file(),'gallery link '+url)
 # Independent numerical/model checks, not comparisons with rendered text.
 R=8.314;k=1.380649e-23;g=1.4;cv=2.5*R
 near('blocked steel stress MPa',200e9*12e-6*10/1e6,24)
 near('tyre fitting rise K',(.999/.998-1)/12e-6,83.5)
 near('nitrogen most-probable speed',math.sqrt(2*R*300/.028),422)
 near('nitrogen mean speed',math.sqrt(8*R*300/(math.pi*.028)),476)
 near('nitrogen rms speed',math.sqrt(3*R*300/.028),517)
 near('lambda 1 atm micrometre',k*273/(math.sqrt(2)*math.pi*(3.7e-10)**2*101325)*1e6,.061)
 near('lambda 10 Pa millimetre',k*273/(math.sqrt(2)*math.pi*(3.7e-10)**2*10)*1e3,.620)
 near('one mol Ar + O2 gamma',(2.5+3.5)/(1.5+2.5),1.5)
 near('open-fridge room mol',101325*60/(R*300),2437)
 near('open-fridge room kelvin rise',150*2400/(101325*60/(R*300)*cv),7.1)
 near('diatomic isochore heat J',cv*100,2079)
 near('diatomic isobar heat J',(cv+R)*100,2910)
 tmono=300/2**(2/3);wmono=1.5*R*(300-tmono)
 near('monatomic double-volume T',tmono,189)
 near('monatomic adiabatic work J',wmono,1384)
 near('monatomic isothermal work J',R*300*math.log(2),1729)
 near('difference is not internal-energy loss',R*300*math.log(2)-wmono,345)
 near('polytrope half-volume T s=1.5',300*math.sqrt(2),424.3)
 near('polytrope path capacity in units R',2.5+1/(1-1.5),.5)
 near('polytrope heat J',.5*R*(300*math.sqrt(2)-300),517)
 near('negative path capacity s=1.2',2.5+1/(1-1.2),-2.5)
 near('sudden half-volume T',300*cv/(cv-R),500)
 near('two mol sudden input J',2*cv*(500-300),8314)
 near('sudden compression entropy J/K',2*cv*math.log(500/300)-2*R*math.log(2),9.714)
 near('three-leg cycle efficiency',(2*math.log(2)-1)/(2.5+2*math.log(2)),.0994)
 near('triangle loop joules',.5*(300-150)*(12-6),450)
 near('Carnot 600/300',1-300/600,.5)
 near('fridge COP',270/(300-270),9)
 near('cascade hot delivery J',500*(350/(350-300)),3500)
 near('Otto compression T',300*8**.4,689)
 near('Otto efficiency',1-8**(-.4),.565)
 near('conduction entropy J/K',1200/300-1200/400,1)
 C=4180;th=373.15;tc=293.15;tm=(th+tc)/2
 near('two kg direct water mixing entropy J/K',C*math.log(323.15/353.15)+C*math.log(323.15/293.15),36)
 near('finite pair reversible maximum J',C*(th+tc-2*math.sqrt(th*tc)),20200)
 near('finite hot body fixed bath maximum J',C*((th-tc)-tc*math.log(th/tc)),38800)
 near('air isothermal stiffness fraction',1/g,.7143)
 near('nitrogen sound m/s',math.sqrt(g*R*300/.028),353)
 near('dry lapse K/km',9.81/(3.5*R/.029)*1000,9.78)
 near('isothermal scale height km',R*288/(.029*9.81)/1000,8.42)
 near('Jeans parameter at six rms',1.5*6**2,54)
 b=R*304/(8*7.39e6);a=27*7.39e6*b*b
 near('vdW b CO2',b,4.28e-5)
 near('vdW a CO2',a,.365)
 near('albedo effective cooling K',(1361*.67/(4*5.67e-8))**.25-(1361*.70/(4*5.67e-8))**.25,-2.8)
 p0=101325;pi=200*p0;vi=.05
 near('tank total reversible work MJ',pi*vi*math.log(200)/1e6,5.369)
 near('tank useful availability MJ',(pi*vi*math.log(200)-(pi-p0)*vi)/1e6,4.361)
 near('ideal tank final kelvin',300*(1/200)**((g-1)/g),66)
 near('77 K marker pressure atm',200*(77/300)**(g/(g-1)),1.72)
 near('sealed heated tank atm',200*320/300,213.3)
 vl,vg,ps=coexistence();tr=.88
 near('vdW coexistence pressure endpoint',8*tr/(3*vl-1)-3/vl**2,ps,rel=1e-9)
 area=(8*tr/3)*math.log((3*vg-1)/(3*vl-1))+3/vg-3/vl-ps*(vg-vl)
 near('vdW Maxwell equal area',area,0,absolute=1e-10)
 source=ROOT.parents[1]/'thermodynamics'
 for name,expected in [('Thermodynamics.md','35d4b65fcfce071b81d7dcf2efdebb79bb78d30b5dc8c5dc84a57ea756ba4541'),('Thermodynamics.html','28673e895d32aaddbc07ab9bb2106a56fc1f3dcd32e885053b03f780c5c8cab0')]:
  check(hashlib.sha256((source/name).read_bytes()).hexdigest()==expected,'detailed source preserved')
 assets=json.loads((ROOT/'asset-manifest.json').read_text())
 for name,details in assets.items():
  content=(ROOT/name).read_bytes();check(len(content)==details['bytes'] and hashlib.sha256(content).hexdigest()==details['sha256'],'asset manifest '+name)
 report={'assertions':checks,'physics_model_checks':len(models),'pages':28,'JEE':21,'Olympiad':7,'cards':112,'diagrams':56,'math_blocks':248,'numerical_models':models}
 (ROOT/'verification-results.json').write_text(json.dumps(report,indent=2)+'\n')
 print(f'PASS: {checks} assertions; {len(models)} representative physics/model checks; 28 PNGs; 3 ZIPs; 3 PDFs. Not exhaustive certification.')
if __name__=='__main__':main()
