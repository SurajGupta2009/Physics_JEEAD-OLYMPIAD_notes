"""Run from any directory after author/render/export. Checks are representative, not a proof of every line."""
from pathlib import Path
import hashlib,json,math,re,zipfile
from urllib.parse import unquote,urlsplit
from PIL import Image,ImageChops
from pypdf import PdfReader
from matplotlib.ft2font import FT2Font
import numpy as np
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
 data=json.loads((ROOT/'sheets.json').read_text());check(len(data)==37,'page count')
 check([p['section'] for p in data]==['JEE']*29+['Olympiad']*8,'reading order')
 check(len({p['slug'] for p in data})==37,'unique filenames')
 check(sum(len(p['cards']) for p in data)==148,'card count')
 check(sum(len(p['diagrams']) for p in data)==74,'diagram count')
 check(sum(k=='m' for p in data for c in p['cards'] for k,s in c['items'])==257,'math block count')
 cmap=FT2Font(str(ROOT/'fonts/PatrickHand-Regular.ttf')).get_charmap()
 for p in data:
  prose=[p['title'],p['subtitle'],p['source'],p['takeaway']]+[c['title'] for c in p['cards']]+[s for c in p['cards'] for k,s in c['items'] if k!='m']
  check(all(ord(ch) in cmap or ch=='\n' for text in prose for ch in text),'font coverage '+p['slug'])
 for section,count in [('JEE',29),('Olympiad',8)]:
  rows=[p for p in data if p['section']==section]
  check([p['part_page'] for p in rows]==list(range(1,count+1)),'numbering '+section)
  check({str(p.relative_to(ROOT)) for p in ROOT.glob(section+'-*.png')}=={p['slug']+'.png' for p in rows},'stale/missing pages')
 for p in data:
  im=Image.open(ROOT/(p['slug']+'.png'));check(im.size==(2480,3508),'dimensions')
  check(all(abs(d-300)<.1 for d in im.info['dpi']),'DPI')
  check(im.mode=='P','indexed PNG')
  rgb=im.convert('RGB');white=Image.new('RGB',rgb.size,'white');bounds=ImageChops.difference(rgb,white).getbbox()
  check(bounds and bounds[0]>=125 and bounds[1]>=125 and bounds[2]<=2356 and bounds[3]<=3383,'safe margin '+p['slug'])
 layout=json.loads((ROOT/'layout-checks.json').read_text());check(len(layout['cards'])==148,'layout manifest')
 for c in layout['cards']:
  check(c['used_px']<c['available_px']-12,'card overflow '+c['card'])
  check(c['body_pt']==11.52 and c['explanation_pt']==11.04,'body text never shrunk')
 for label,rows in [('All',data),('JEE',data[:29]),('Olympiad',data[29:])]:
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
 html=(ROOT/'index.html').read_text();check(html.count('<article ')==37,'gallery count')
 for url in re.findall(r'(?:href|src)=[\"\']([^\"\']+)',html):
  path=urlsplit(url)
  if path.scheme or not path.path:continue
  check((ROOT/unquote(path.path)).is_file(),'gallery link '+url)
 # Representative physical identities, independently evaluated numerically.
 k=8.9875517923e9;eps=1/(4*math.pi*k);e=1.602176634e-19
 near('electrons per microcoulomb',1e-6/e,6.241509e12,rel=1e-6)
 near('ke2 in eV nm',k*e*1e9,1.439965,rel=1e-6)
 f0=k*(2e-6)**2/.1**2
 near('triangle equal signs force N',math.sqrt(3)*f0,6.226)
 v=np.array([-f0,0])+f0*np.array([.5,math.sqrt(3)/2])
 near('mixed triangle angle degrees',math.degrees(math.atan2(v[1],v[0])),120,rel=1e-10)
 near('square central equilibrium ratio',-(1+2*math.sqrt(2))/4,-.95710678,rel=1e-7)
 near('like-charge null distance fraction',1/(1+math.sqrt(4)),1/3,rel=1e-12)
 near('third equilibrium charge q1=1 q2=4',-4/(1+2)**2,-4/9,rel=1e-12)
 near('ring maximum axial coordinate',1/math.sqrt(2),.70710678,rel=1e-7)
 near('ring maximum field coefficient',(.5**.5)/(1+.5)**1.5,2/(3*math.sqrt(3)),rel=1e-12)
 near('ring particle period seconds',2*math.pi*math.sqrt(5e-6*.08**3/(k*2e-9*40e-9)),.3749)
 near('finite rod E N/C',2*k*1e-8*.5/(.3*math.sqrt(.5**2+.3**2)),514)
 near('end-on rod E N/C',k*1e-8/(.3*1.3),230)
 near('infinite line overestimate fraction',math.sqrt(101)/10-1,.00498756,rel=1e-6)
 near('semicircle field coefficient',2/math.pi,.63661977,rel=1e-7)
 near('full ring field coefficient',2*math.sin(math.pi),0)
 near('disc far-field limit',2*1e6*(1-1000/math.sqrt(1000**2+1)),1,rel=1e-5)
 near('axial dipole far-field correction',(1-1/100)**(-2)-1,.02030405,rel=1e-6)
 near('equatorial exact midpoint coefficient',1/(.5**2)**1.5,8,rel=1e-12)
 near('dipole rotation aligned-to-opposite',math.cos(0)-math.cos(math.pi),2,rel=1e-12)
 near('beam exit deflection metres',5000*.05**2/(4*1000),.003125,rel=1e-12)
 near('beam screen deflection metres',5000*.05/(2*1000)*(.275+.05/2),.0375,rel=1e-12)
 near('electron 1 keV speed m/s',math.sqrt(2*e*1000/9.1093837e-31),1.87554e7,rel=1e-5)
 side=math.atan(1/3)/(2*math.pi);end=math.atan(4/3)/(4*math.pi)
 near('cube mid-edge side-face fraction',side,.05120819117,rel=1e-9)
 near('cube mid-edge end-face fraction',end,.07379180883,rel=1e-9)
 near('cube mid-edge total solid-angle fraction',2*side+2*end,.25,rel=1e-12)
 check(abs(side-end)>.02,'edge faces must not be falsely equivalent')
 near('cube corner far-face fraction',1/24,.04166666667,rel=1e-9)
 # Direct surface-flux quadrature checks the analytic edge fractions.
 u,w=np.polynomial.legendre.leggauss(64);ys=(u+1)/2;ws=w/2
 Y,Z=np.meshgrid(ys,ys);W=np.outer(ws,ws)
 near('edge opposite-face direct flux',float(np.sum(W/(1+Y**2+(Z-.5)**2)**1.5))/(4*math.pi),side,rel=1e-10)
 near('edge end-face direct flux',float(np.sum(.5*W/(Y**2+Z**2+.25)**1.5))/(4*math.pi),end,rel=1e-10)
 near('sphere volume field from enclosed charge',(.4**3)/.4**2,.4,rel=1e-12)
 near('uniform sphere central potential ratio',1+1/2,1.5,rel=1e-12)
 near('sphere half-field external radius',math.sqrt(2),1.41421356,rel=1e-7)
 near('linear radial density enclosed fraction',.6**4,.1296,rel=1e-12)
 near('slab interior potential continuity',-.5, -1*(1-.5),rel=1e-12)
 near('slab interior field derivative',-((-(.3+1e-5)**2/2)-(-(.3-1e-5)**2/2))/(2e-5),.3,rel=1e-9)
 near('three-charge triangle pair energy coefficient',1+1+1,3,rel=1e-12)
 near('square pair energy coefficient',4+2/math.sqrt(2),4+math.sqrt(2),rel=1e-12)
 near('joined-sphere final voltage',.02*3000/(.02+.06),750,rel=1e-12)
 near('joined-sphere retained energy fraction',.02/(.02+.06),.25,rel=1e-12)
 near('uniform solid self-energy shell assembly',3*float(np.sum(ws*ys**4)),.6,rel=1e-12)
 near('uniform solid inside field energy',.5*float(np.sum(ws*ys**4)),.1,rel=1e-12)
 near('alpha gold closest approach fm',2*79*k*e*1e9/5,45.5029,rel=1e-5)
 near('image electron energy eV at 1nm',k*e/(4e-9),.359991,rel=1e-5)
 near('image electron force N at 1nm',k*e**2/(4e-18),5.76769e-11,rel=1e-5,absolute=1e-18)
 # Analytic image density integrates to -q after s=tan(theta).
 th=(u+1)*math.pi/4;wh=w*math.pi/4
 near('ground-plane integrated induced charge ratio',-float(np.sum(wh*np.sin(th))),-1,rel=1e-12)
 d=2.;h=1e-5
 energy=lambda x:-1/(2*(x*x-1))
 near('sphere-image energy derivative equals force',-(energy(d+h)-energy(d-h))/(2*h),-d/(d*d-1)**2,rel=1e-9)
 near('soap bubble zero-overpressure charge nC',8*math.pi*math.sqrt(2*eps*.025*.02**3)*1e9,47.3)
 near('water Rayleigh 1mm nC',8*math.pi*math.sqrt(eps*.072*.001**3)*1e9,.6346)
 near('drop endpoint threshold ratio',.5*math.sqrt((2-2**(2/3))/(2**(2/3)-1)),.41905082744,rel=1e-5)
 near('dielectric sphere alpha epsilon factor',(3-1)/(3+2),.4,rel=1e-12)
 near('quadrupole asymptotic potential coefficient',1000**3*(1/(1000-1)+1/(1000+1)-2/1000),2,rel=1e-5)
 # Ring numerical integrals check the inward in-plane field and saddle signs.
 phi=np.linspace(0,2*np.pi,20000,endpoint=False);s=.001
 es=np.mean((s-np.cos(phi))/(1+s*s-2*s*np.cos(phi))**1.5)
 near('ring in-plane E_s/s is NEGATIVE one-half',float(es/s),-.5,rel=1e-5)
 near('ring Hessian trace',-.5-.5+1,0)
 # Unit cube corner integral: split cube into three pyramids, integrate radial scale analytically.
 U,V=np.meshgrid(ys,ys)
 cube=1.5*float(np.sum(W/np.sqrt(1+U**2+V**2)))
 near('cube corner potential coefficient',cube,1.19003868199,rel=1e-10)
 near('cube centre potential coefficient',2*cube,2.38007736398,rel=1e-10)
 near('one-metre dome charge mC',3e6/k*1e3,.333795,rel=1e-5)
 near('one-metre dome field energy J',(3e6)**2/(2*k),500.693,rel=1e-5)
 source=ROOT.parents[1]/'electrostatics/Electrostatics.md'
 check(hashlib.sha256(source.read_bytes()).hexdigest()=='6033c09818b9df2bd81ee993cc4cb417c445349d74d9a5a007fa9c48561aef29','detailed source unchanged')
 for file in ROOT.glob('*.md'):
  for url in re.findall(r'\]\(([^)\n]+)\)',file.read_text()):
   path=urlsplit(url)
   if path.scheme or not path.path:continue
   target=file.parent/unquote(path.path)
   # The verification report itself is an output of this successful test run.
   if target.resolve()==(ROOT/'verification-results.json').resolve():continue
   check(target.is_file(),'documentation link '+url)
 assets=json.loads((ROOT/'asset-manifest.json').read_text())
 for name,details in assets.items():
  content=(ROOT/name).read_bytes();check(len(content)==details['bytes'] and hashlib.sha256(content).hexdigest()==details['sha256'],'asset manifest '+name)
 check(len({d for p in data for d in p['diagrams']})==74,'unique diagram identifiers')
 report={'assertions':checks,'physics_model_checks':len(models),'pages':37,'JEE':29,'Olympiad':8,'cards':148,'diagrams':74,'math_blocks':257,'numerical_models':models}
 (ROOT/'verification-results.json').write_text(json.dumps(report,indent=2)+'\n')
 print(f'PASS: {checks} assertions; {len(models)} representative physics/model checks; 37 PNGs; 3 ZIPs; 3 PDFs. Not exhaustive certification.')
if __name__=='__main__':main()
