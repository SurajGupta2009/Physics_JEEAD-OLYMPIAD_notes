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
 data=json.loads((ROOT/'sheets.json').read_text());check(len(data)==77,'page count')
 check([p['section'] for p in data]==['JEE']*58+['Olympiad']*19,'reading order')
 check(len({p['slug'] for p in data})==77,'unique filenames')
 check(sum(len(p['cards']) for p in data)==308,'card count')
 check(sum(len(p['diagrams']) for p in data)==154,'diagram count')
 check(sum(k=='m' for p in data for c in p['cards'] for k,s in c['items'])==514,'math block count')
 cmap=FT2Font(str(ROOT/'fonts/PatrickHand-Regular.ttf')).get_charmap()
 for p in data:
  prose=[p['title'],p['subtitle'],p['source'],p['takeaway']]+[c['title'] for c in p['cards']]+[s for c in p['cards'] for k,s in c['items'] if k!='m']
  check(all(ord(ch) in cmap or ch=='\n' for text in prose for ch in text),'font coverage '+p['slug'])
 for section,count in [('JEE',58),('Olympiad',19)]:
  rows=[p for p in data if p['section']==section]
  check([p['part_page'] for p in rows]==list(range(1,count+1)),'numbering '+section)
  check({str(p.relative_to(ROOT)) for p in ROOT.glob(section+'-*.png')}=={p['slug']+'.png' for p in rows},'stale/missing pages')
 for p in data:
  im=Image.open(ROOT/(p['slug']+'.png'));check(im.size==(2480,3508),'dimensions')
  check(all(abs(d-300)<.1 for d in im.info['dpi']),'DPI')
  check(im.mode=='P','indexed PNG')
  rgb=im.convert('RGB');white=Image.new('RGB',rgb.size,'white');bounds=ImageChops.difference(rgb,white).getbbox()
  check(bounds and bounds[0]>=125 and bounds[1]>=125 and bounds[2]<=2356 and bounds[3]<=3383,'safe margin '+p['slug'])
 layout=json.loads((ROOT/'layout-checks.json').read_text());check(len(layout['cards'])==308,'layout manifest')
 for c in layout['cards']:
  check(c['used_px']<c['available_px']-12,'card overflow '+c['card'])
  check(c['body_pt']==11.52 and c['explanation_pt']==11.04,'body text never shrunk')
 for label,rows in [('All',data),('JEE',data[:58]),('Olympiad',data[58:])]:
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
 html=(ROOT/'index.html').read_text();check(html.count('<article ')==77,'gallery count')
 for url in re.findall(r'(?:href|src)=[\"\']([^\"\']+)',html):
  path=urlsplit(url)
  if path.scheme or not path.path:continue
  check((ROOT/unquote(path.path)).is_file(),'gallery link '+url)
 # Representative physical identities, independently evaluated numerically.
 mu0=4e-7*math.pi;e=1.602176634e-19;me=9.1093837015e-31;mp=1.67262192369e-27;hbar=1.054571817e-34;c=2.99792458e8;kB=1.380649e-23
 near('electron gyroradius 1e6 m/s in 1 mT (mm)',me*1e6/(e*1e-3)*1e3,5.686,rel=1e-3)
 near('electron period in 1 mT (ns)',2*math.pi*me/(e*1e-3)*1e9,35.75,rel=1e-3)
 near('electron cyclotron GHz per T',e/(2*math.pi*me)/1e9,27.99,rel=1e-3)
 near('proton cyclotron MHz per T',e/(2*math.pi*mp)/1e6,15.23,rel=1e-3)
 near('selector speed m/s for E=1e5 B=0.1',1e5/.1,1e6,rel=1e-12)
 near('strip deflection sin(phi)=d/r',5/6.958,.7186,rel=1e-2)
 near('strip crossing time ns',math.asin(5/6.958)*mp/(e*.3)*1e9,27.9,rel=2e-2)
 near('strip half-period return ns',math.pi*mp/(e*.3)*1e9,109.4,rel=1e-3)
 near('spectrometer r for U-238 (m)',1/.5*math.sqrt(2*238*1.66053906660e-27*1e4/e),.4445,rel=1e-3)
 near('isotope fractional radius half rule',(math.sqrt(238)-math.sqrt(235))/math.sqrt(238),.5*3/238,rel=2e-2)
 near('cyclotron proton f at 1.5 T (MHz)',e*1.5/(2*math.pi*mp)/1e6,22.86,rel=1e-3)
 near('cyclotron Kmax 27 MeV J',(e*1.5*.5)**2/(2*mp),4.31e-12,rel=2e-2)
 near('cyclotron turns at 50 kV',26.9e6*e/(2*e*5e4),269,rel=2e-2)
 near('loss cone degrees for mirror ratio 10',math.degrees(math.asin(1/math.sqrt(10))),18.43,rel=1e-3)
 near('mirror invariant reflection B/B0',1/math.sin(math.radians(30))**2,4,rel=1e-12)
 near('Hall copper microvolts',10*1.0/(8.5e28*e*1e-3)*1e6,.7343,rel=1e-2)
 near('Hall semiconductor volts',.01*.5/(1e21*e*1e-4),.3121,rel=1e-2)
 near('drift speed E/B',1e4/.1,1e5,rel=1e-12)
 near('electron cycloid radius micrometre',me*1e4/(e*.1**2)*1e6,5.686,rel=1e-3)
 near('cycloid arch height micrometre',2*me*1e4/(e*.1**2)*1e6,11.37,rel=1e-3)
 near('cycloid top speed',2*1e4/.1,2e5,rel=1e-12)
 near('Thomson q/m for y=2cm B=0.1 L=0.5',2*.02*1e4/(.1**2*.5**2),1.6e5,rel=1e-6)
 near('300 Br rule momentum 45 MeV/c',300*1.5*.1,45,rel=1e-12)
 near('moving charge B equals vE/c2 (T)',1e-7*e*1e6/.01**2,1e6*(8.9875517923e9*e/.01**2)/c**2,rel=1e-6)
 near('finite wire 60-60 field (uT)',1e-7*10/.1*math.sqrt(3)*1e6,17.32,rel=1e-2)
 near('infinite wire 10 A 10 cm (uT)',2e-7*10/.1*1e6,20.0,rel=1e-3)
 near('semi-infinite end half rule',2e-7*10/.1/2*1e6,10.0,rel=1e-3)
 near('square centre coefficient',4*(2*math.sin(math.pi/4)),2*2*math.sqrt(2),rel=1e-9)
 near('hexagon centre coefficient',6/(4*math.pi*(math.sqrt(3)/2)),math.sqrt(3)/math.pi,rel=1e-9)
 near('loop centre B 5 A 20 cm (uT)',mu0*5/(2*.2)*1e6,15.71,rel=1e-3)
 near('quarter arc is quarter loop',mu0*5*(math.pi/2)/(4*math.pi*.2)/(mu0*5/(2*.2)),.25,rel=1e-9)
 near('loop axis at x=R coefficient',(.2**2)/((.2**2+.2**2)**1.5)/(1/.2),1/(2*math.sqrt(2)),rel=1e-9)
 near('loop axial exact at x=20R',mu0*5*.2**2/(2*(16.04)**1.5),1.956e-9,rel=1e-3,absolute=1e-15)
 near('solenoid interior n=1000 1A mT',mu0*1000*1e3,1.257,rel=1e-3)
 near('solenoid end half-rule factor',2*(5/math.sqrt(.05**2+5**2))/(2*2.5/math.sqrt(.05**2+2.5**2))*.5,.4999,rel=1e-2)
 near('toroid mid-gap field 500 turns 2 A 15 cm (uT)',mu0*500*2/(2*math.pi*.15)*1e6,1333.3,rel=1e-3)
 near('ampere circulation 2 A enclosed (uT m)',mu0*2*1e6,2.513,rel=1e-3)
 near('thick wire B at half radius',mu0*(10*.25)/(2*math.pi*.5)*1e6,1.0,rel=1e-3)
 near('sheet field mu0 K/2 for K=300 (mT)',mu0*300/2*1e3,.1885,rel=1e-3)
 near('hole field 0.5 mu0 J d',.5*mu0*2e6*.01,12.566e-3,rel=1e-4)
 near('chord force semicircle 2IRB',2*1.5*.2*.3,.18,rel=1e-12)
 near('couple equals mu B sin theta',1.5*(2*.2*.1)*.3*math.sin(1.0),1.5*(.04)*.3*math.sin(1.0),rel=1e-12)
 near('U-gradient torque identity',-( -1.5*.04*.3*math.cos(1.0+1e-6)+1.5*.04*.3*math.cos(1.0-1e-6))/(2e-6),-1.5*.04*.3*math.sin(1.0),rel=1e-5)
 near('parallel wire force per metre 100 A 10 cm (mN/m)',mu0/(2*math.pi)*100*100/.1*1e3,20.0,rel=1e-3)
 near('1 T pressure in atmospheres',1/(2*mu0)/1.01325e5,3.927,rel=1e-3)
 near('1 T solenoid 10 cm2 end force (N)',1/(2*mu0)*1e-3,397.9,rel=1e-3)
 near('3 T hoop stress (MPa)',9/(2*mu0)/1e6,3.581,rel=1e-3)
 near('ring gyromagnetic ratio Q/2m', (1e-6*2*math.pi*100*.1**2/2)/(.01*.1**2*2*math.pi*100),1e-6/(2*.01),rel=1e-9)
 near('Bohr magneton',e*hbar/(2*me),9.274e-24,rel=1e-6)
 near('rotating disc centre field B=mu0 sigma omega R/2',mu0*2e-6*50*.4/2,2.513e-11,rel=1e-3)
 near('magnetised sphere interior (T)',2/3*mu0*1e6,.8378,rel=1e-3)
 near('sphere moment M V (A m2)',1e6*4/3*math.pi*.01**3,4.1888,rel=1e-3)
 near('sphere pole exterior continuity',mu0/(4*math.pi)*2*(1e6*4/3*math.pi*.01**3)/.01**3,2/3*mu0*1e6,rel=1e-6)
 near('sphere versus cylinder interior ratio',2/3,2/3,rel=1e-12)
 near('water Larmor susceptibility',-mu0*3.3e28*10*e**2*(0.07e-9)**2/(6*me),-9.47e-6,rel=5e-2)
 near('paramagnetic x at 1 K 1 T',9.274e-24/(kB*1),.6717,rel=1e-3)
 near('Curie chi scales as 1/T ratio',1/300/(1/100),1/3,rel=1e-12)
 near('dipole coupling kelvin 0.25 nm',mu0/(4*math.pi)*9.274e-24**2/(0.25e-9)**3/kB,.0399,rel=2e-2)
 near('exchange Tc zJ/3',8*.05*e/(3*kB),1548,rel=2e-2)
 near('hysteresis loss 20 kg 50 Hz (W)',150*50*20/7650,19.6,rel=2e-2)
 near('filled core B = mu_r mu0 nI (T)',2000*mu0*500,1.257,rel=1e-3)
 near('earth BH at dip 60 (uT)',48*math.cos(math.radians(60)),24.0,rel=1e-6)
 near('earth BV at dip 60 (uT)',48*math.sin(math.radians(60)),41.57,rel=1e-4)
 near('dip-latitude lambda for dip 60 (deg)',math.degrees(math.atan(math.tan(math.radians(60))/2)),40.89,rel=1e-3)
 near('earth dipole moment (1e22 A m2)',30e-6*(6.37e6)**3/1e-7/1e22,7.75,rel=2e-2)
 near('Gauss method mu (A m2)',math.sqrt((4*math.pi**2*6e-6/16)*(math.tan(math.radians(30))*.008/2e-7)),.5847,rel=1e-2)
 near('Gauss method BH (uT)',math.sqrt((4*math.pi**2*6e-6/16)/(math.tan(math.radians(30))*.008/2e-7))*1e6,25.33,rel=1e-2)
 near('core current estimate (GA)',(30e-6*(6.37e6)**3/1e-7)/(math.pi*3.5e6**2)/1e9,2.03,rel=3e-2)
 near('Helmholtz B factor 8/(5 sqrt5)',8/(5*math.sqrt(5)),.71554,rel=1e-5)
 near('Helmholtz field 100 turns 20 cm 1 A (mT)',8/(5*math.sqrt(5))*mu0*100/.2*1e3,.450,rel=1e-3)
 near('Helmholtz uniform length for 0.1 per cent (cm)',2*.17*20,6.8,rel=2e-2)
 near('synchrotron radius 1 GeV 1 T (m)',(1e9*e/c)/(e*1),3.336,rel=1e-3)
 near('synchrotron revolution MHz',c/(2*math.pi*3.336)/1e6,14.29,rel=1e-2)
 near('cyclotron wrong by gamma factor',1958*14.29,27980,rel=1e-2)
 near('belt gyration period at L=2 (ms)',2*math.pi*mp/(e*(31e-6/8))*1e3,17.2,rel=2e-2)
 near('Fermi reflections to double K', (math.sqrt(2)-1)/2*c/1e4,6213,rel=2e-2)
 near('two-carrier Ge RH room (e-3 m3/C)',(1e21*.19**2-1e20*.39**2)/(e*(1e21*.19+1e20*.39)**2),2.49e-3,rel=2e-2)
 near('two-carrier Ge intrinsic (e-3 m3/C)',(3e20*.19**2-3e20*.39**2)/(e*(3e20*.19+3e20*.39)**2),-7.17e-3,rel=2e-2)
 near('levitation height (cm)',(3*mu0*1/(32*math.pi*.0075*9.81))**.25*100,2.668,rel=2e-2)
 near('levitation force balance',3*mu0/(2*math.pi*(2*(3*mu0/(32*math.pi*.0075*9.81))**.25)**4),.0075*9.81,rel=1e-2)
 near('lightning channel B (T)',mu0*3e4/(2*math.pi*.005),1.2,rel=1e-3)
 near('pinch pressure (Pa)',1.2**2/(2*mu0),5.73e5,rel=1e-2)
 near('slab support field (T)',math.sqrt(2*mu0*2*9.81/4e-4),.347,rel=2e-2)
 near('F_m/F_e at 1e6 m/s',(1e6/c)**2,1.113e-5,rel=1e-3)
 near('quadrature wire convergence',1e-7*10/.1*math.sqrt(3)*2/2,1e-7*10/.1*math.sqrt(3),rel=1e-9)
 omega=2*math.pi*50;L=50e-3;C=10e-6;R=20
 near('LCR XL 50 mH 50 Hz (ohm)',omega*L,15.71,rel=1e-2)
 near('LCR XC 10 uF 50 Hz (ohm)',1/(omega*C),318.3,rel=1e-2)
 near('LCR Z (ohm)',math.sqrt(R*R+(omega*L-1/(omega*C))**2),302.6,rel=2e-2)
 near('LCR I for 230 V (A)',230/math.sqrt(R*R+(omega*L-1/(omega*C))**2),0.760,rel=2e-2)
 near('LCR resonance Hz',1/(2*math.pi*math.sqrt(L*C)),225.1,rel=1e-2)
 near('radio C for 1 MHz 200 uH (pF)',1/((2*math.pi*1e6)**2*200e-6)*1e12,126.7,rel=1e-2)
 near('radio Q 200 uH 5 ohm 1 MHz',2*math.pi*1e6*200e-6/5,251.3,rel=1e-2)
 near('RL kick 10 mH 2 A in 1 us (kV)',10e-3*2/1e-6/1e3,20.0,rel=1e-9)
 near('LC omega0 1 mH 1 uF (krad/s)',1/math.sqrt(1e-3*1e-6)/1e3,31.62,rel=1e-2)
 near('LC I0 10 V 1 mH 1 uF (A)',10*math.sqrt(1e-6/1e-3),0.3162,rel=1e-2)
 near('rectified sine mean 2/pi',2/math.pi,0.6366,rel=1e-4)
 near('sine rms 1/root2',1/math.sqrt(2),0.7071,rel=1e-4)
 near('transformer 230/12 ratio',230/12,19.17,rel=1e-2)
 near('reflected 6 ohm at n=19.2 (kohm)',(230/12)**2*6,2204,rel=1e-2)
 near('transmission loss ratio 11 vs 220 kV',(220/11)**2,400,rel=1e-9)
 near('rails coasting tau 100 g 0.1 ohm (s)',.1*.1/(.5**2*.2**2),1.0,rel=1e-9)
 near('rails terminal speed hanging 50 g (m/s)',.05*9.81*.1/(.5**2*.2**2),4.905,rel=1e-2)
 near('rails coasting heat 100 g at 2 m/s (J)',.5*.1*2**2,.20,rel=1e-9)
 near('disc EMF 0.5 T 300 rad/s 10 cm (V)',.5*300*.1**2/2,.75,rel=1e-9)
 near('betatron orbit field half average',.5,.5,rel=1e-12)
 near('betatron 36 MeV orbit in 0.5 T (m)',(36e6*1.602176634e-19/2.99792458e8)/(1.602176634e-19*.5),0.2402,rel=1e-2)
 near('coax speed 1/sqrt(LC) with L C = 1/c2 (m/s)',1/math.sqrt(3.2e-7*35e-12*1e0),2.988e8,rel=5e-2)
 near('coax Z0 96 ohm b/a',60*math.log(3.5),75.2,rel=1e-2)
 near('Wien beta at omega RC = 1',1/3,1/3,rel=1e-9)
 near('max power ratio at RL = Rs',4*1/(1+1)**2,1.0,rel=1e-9)
 near('LCR phi tan at 50 Hz',math.degrees(math.atan((omega*L-1/(omega*C))/R)),-86.17,rel=1e-2)
 source=ROOT.parents[1]/'magnetism/Magnetism.md'
 check(hashlib.sha256(source.read_bytes()).hexdigest()=='86d3deb0ac086e68b20644eaf24626a87c18510aad8843b1575d62d7a00f9bba','magnetism source unchanged')
 source2=ROOT.parents[1]/'emi-ac/Emi-ac.md'
 check(hashlib.sha256(source2.read_bytes()).hexdigest()=='7699e1bef3a7926819c5b60a7ba0703f960fcb5a29dcced4dcebd38a06ce998e','emi-ac source unchanged')
 for file in ROOT.glob('*.md'):
  for url in re.findall(r'\]\(([^)\n]+)\)',file.read_text()):
   path=urlsplit(url)
   if path.scheme or not path.path:continue
   target=file.parent/unquote(path.path)
   if target.resolve()==(ROOT/'verification-results.json').resolve():continue
   check(target.is_file(),'documentation link '+url)
 assets=json.loads((ROOT/'asset-manifest.json').read_text())
 for name,details in assets.items():
  content=(ROOT/name).read_bytes();check(len(content)==details['bytes'] and hashlib.sha256(content).hexdigest()==details['sha256'],'asset manifest '+name)
 check(len({d for p in data for d in p['diagrams']})==154,'unique diagram identifiers')
 report={'assertions':checks,'physics_model_checks':len(models),'pages':77,'JEE':58,'Olympiad':19,'cards':308,'diagrams':154,'math_blocks':514,'numerical_models':models}
 (ROOT/'verification-results.json').write_text(json.dumps(report,indent=2)+'\n')
 print(f'PASS: {checks} assertions; {len(models)} representative physics/model checks; 77 PNGs; 3 ZIPs; 3 PDFs. Not exhaustive certification.')
if __name__=='__main__':main()
