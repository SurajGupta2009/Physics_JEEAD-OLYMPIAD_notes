"""Print/export regression checks and independent representative physics checks."""
from pathlib import Path
import json,re,zipfile,hashlib
import numpy as np
from PIL import Image
from pypdf import PdfReader
from reportlab.lib.pagesizes import A4
from build_exports import PDFS,ZIPS
ROOT=Path(__file__).resolve().parent

def physics():
 checks=[]
 def check(name,condition):
  assert condition,name
  checks.append(name)
 beta=.4;g=10;mu=.3;R=.1;v0=10
 check('sphere incline E2',np.isclose(g*.5/(1+beta),25/7) and np.isclose(beta/(1+beta)*np.tan(np.pi/6),.1649572198))
 alpha=mu*g/(beta*R);ts=v0/(mu*g+alpha*R)
 check('corrected E4',np.isclose(alpha,75) and np.isclose(ts,20/21))
 vf=v0-mu*g*ts;wf=alpha*ts
 check('slip transition continuity',np.isclose(vf,wf*R) and np.isclose(vf,50/7))
 check('slip energy loss',np.isclose(.5*v0*v0-.5*(1+beta)*vf*vf,v0*v0/7))
 # General initial states, including backspin, overspin, reversal and rest.
 for v,wR in [(10,-5),(10,20),(10,-25),(10,-30),(-2,4)]:
  u=v-wR;s=np.sign(u);t=abs(u)/(mu*g*(1+1/beta));v1=v-s*mu*g*t;w1=wR+s*mu*g*t/beta
  loss=.5*(v*v+beta*wR*wR)-.5*(v1*v1+beta*w1*w1)
  check(f'signed slip v={v}, Rw={wR}',np.isclose(v1,w1) and np.isclose(loss,beta*u*u/(2*(1+beta))))
 # Solve Newton-Euler independently, with clockwise alpha=a/R.
 # [M,-1; I/R,R] [a,f] = [F,Fh]
 M=2.;F=3.;R=.2;I=.5*M*R*R
 a,f=np.linalg.solve([[M,-1],[I/R,R]],[F,F*R])
 check('E9 friction sign and acceleration',np.isclose(a,4*F/(3*M)) and np.isclose(f,F/3))
 r=.05
 for phi in [0,np.arccos(r/R),np.pi/2]:
  a,f=np.linalg.solve([[M,-1],[I/R,R]],[F*np.cos(phi),-F*r])
  check(f'spool geometry {phi:.4f}',np.isclose(a,F*(np.cos(phi)-r/R)/(M*(1+I/(M*R*R)))))
 # yoyo [M,1; I/r,-r] [a,T] = [Mg,0]
 for r in [.001,.1,.2]:
  a,T=np.linalg.solve([[M,1],[I/r,-r]],[M*g,0])
  check(f'yoyo balance r={r}',np.isclose(a,M*g*r*r/(M*r*r+I)) and np.isclose(T,M*g*I/(M*r*r+I)))
 i0=1/3;m=.01;d=.5
 check('E3 exact angular speed',np.isclose(m*400*d/(i0+m*d*d),5.9553349876))
 ds=np.linspace(0,1,101);q=.5*m*400**2*i0/(i0+m*ds*ds)
 check('P28 loss monotone',np.all(np.diff(q)<0))
 check('coaxial signed coupling',np.isclose((2*10+3*(-5))/5,1))
 check('overhang 4, 10, million',np.allclose([.5*np.sum(1/np.arange(1,n+1,dtype=float)) for n in [4,10,1000000]],[25/24,1.46448412698,7.19636336143]))
 # Independent rod check from differentiated COM geometry and energy.
 th0=np.pi/3;l=1;th=np.linspace(.01,th0-.01,100)
 w2=3*g/l*(np.sin(th0)-np.sin(th));al=-3*g/(2*l)*np.cos(th)
 ax=-l/2*(np.cos(th)*w2+np.sin(th)*al)
 formula=3*g/4*np.cos(th)*(3*np.sin(th)-2*np.sin(th0))
 star=np.arcsin(2*np.sin(th0)/3)
 check('rod normal from kinematics',np.allclose(ax,formula) and np.isclose(star*180/np.pi,35.2643896828))
 check('rod speed at contact loss',np.isclose(l*l/4*3*g/l*(np.sin(th0)-np.sin(star)),g*l*np.sin(th0)/4))
 check('pendulum optimum',np.isclose((.5+(.5**.5)**2)/(.5**.5),2**.5))
 check('flywheel stress estimate',np.isclose(2*500e6/(7800*3.3),38850.03885003885))
 n=np.array([.6,.8,0]);omega=np.array([0,1.,1.]);L=omega-n*np.dot(omega,n)
 check('dumbbell direction',np.isclose(np.dot(L,n),0) and not np.allclose(np.cross(L,omega),0))
 # Numerical mass integrals verify coefficients independently of printed expressions.
 x=np.linspace(-1,1,20001)
 check('rod transverse coefficient',np.isclose(np.trapezoid(x*x/2,x),1/3,rtol=1e-7))
 # Unit-radius sphere: slice inertia divided by slice mass.
 mass=np.trapezoid(1-x*x,x);iner=np.trapezoid(.5*(1-x*x)**2,x)
 check('solid sphere disc integration',np.isclose(iner/mass,2/5,rtol=1e-7))
 theta=np.linspace(0,np.pi,20001)
 check('thin sphere angular integration',np.isclose(.5*np.trapezoid(np.sin(theta)**3,theta),2/3,rtol=1e-7))
 r=np.linspace(0,1,20001)
 check('cone axial disc integration',np.isclose(np.trapezoid(.5*r**4,r)/np.trapezoid(r*r,r),3/10,rtol=1e-7))
 for n in [0,2,8]:
  ratio=np.trapezoid(r**(n+3),r)/np.trapezoid(r**(n+1),r)
  check(f'radial density exponent {n}',np.isclose(ratio,(n+2)/(n+4),rtol=1e-7))
 check('nonuniform rod centre inertia',np.isclose(np.trapezoid((r-2/3)**2*2*r,r),1/18,rtol=1e-7))
 a=.4;b=1.2
 check('thick sphere shell',np.isclose((2/3)*np.trapezoid(np.linspace(a,b,20001)**4,np.linspace(a,b,20001))/np.trapezoid(np.linspace(a,b,20001)**2,np.linspace(a,b,20001)),2/5*(b**5-a**5)/(b**3-a**3),rtol=1e-7))
 # A solid cylinder's transverse inertia is slice diameter inertia + z-shift.
 R=.6;l=1.7;z=np.linspace(-l/2,l/2,20001)
 check('cylinder transverse slices',np.isclose(np.trapezoid(R*R/4+z*z,z)/l,(3*R*R+l*l)/12,rtol=1e-7))
 # Free target impact: restitutive contact speed and energy loss from final velocities.
 for e in [0,.4,1]:
  m=.2;M=2;I=.6;b=.3;v=5;D=1/m+1/M+b*b/I;J=(1+e)*v/D
  vm=v-J/m;V=J/M;w=J*b/I
  check(f'free target restitution e={e}',np.isclose(V+w*b-vm,e*v))
  check(f'free target heat e={e}',np.isclose(.5*m*v*v-(.5*m*vm*vm+.5*M*V*V+.5*I*w*w),(1-e*e)*v*v/(2*D)))
 check('rod centre of percussion',np.isclose((1/3)/(.5),2/3))
 check('loop ideal contact bound',np.isclose(2*(2.7-2)/(1+.4),1))
 # No-spin E4 COM displacement, separately integrated.
 check('slipping COM displacement',np.isclose(10*(20/21)-1.5*(20/21)**2,400/49))
 check('source retained unchanged',hashlib.sha256((ROOT/'../../rotational-mechanics/Rotational-mechanics.md').resolve().read_bytes()).hexdigest()=='0c92e817bb00ed19607edce22f5891ebdf8c218600bacac68aa1895070d362fb')
 return checks

def test():
 data=json.loads((ROOT/'sheets.json').read_text());assert len(data)==23
 assert [p['section'] for p in data]==['JEE']*19+['Olympiad']*4
 groups={part:[p for p in data if p['section']==part] for part in ['JEE','Olympiad']}
 for part,rows in groups.items():assert [p['part_page'] for p in rows]==list(range(1,len(rows)+1))
 expected=[p['slug']+'.png' for p in data]
 assert {str(p.relative_to(ROOT)) for part in groups for p in (ROOT/part).glob('*.png')}==set(expected)
 for f in expected:
  with Image.open(ROOT/f) as im:
   assert im.size==(2480,3508)
   assert all(abs(d-300)<.02 for d in im.info['dpi'])
   arr=np.array(im)
   for strip in [arr[:120],arr[-120:],arr[:,:120],arr[:,-120:]]:assert np.all(strip==255),f
 layout=json.loads((ROOT/'layout-checks.json').read_text())
 assert len(layout['cards'])==92
 assert np.mean([c['used_px']/c['available_px'] for c in layout['cards'][:76]])>.80
 assert sum(k=='m' for p in groups['JEE'] for c in p['cards'] for k,t in c['items'])>=220
 assert all(any(k=='why' for k,t in c['items']) for p in groups['JEE'] for c in p['cards'])
 assert all(c['used_px']<c['available_px']-12 for c in layout['cards'])
 core=' '.join(t for p in groups['JEE'] for c in p['cards'] for _,t in c['items']).lower()
 for token in ['poisson','sleeping','plane-stress','i_{ij}']:assert token not in core
 for token in ['backspin','spool','yo-yo','pendulum','wall']:assert token in core
 for label,rows in [('All',data),*groups.items()]:
  names=[p['slug']+'.png' for p in rows]
  with zipfile.ZipFile(ROOT/ZIPS[label]) as z:
   assert z.namelist()==names and z.testzip() is None
   for name in names:assert z.read(name)==(ROOT/name).read_bytes()
  pdf=PdfReader(ROOT/PDFS[label]);assert len(pdf.pages)==len(rows)
  assert [i.title for i in pdf.outline]==[f'{p["section"]} {p["part_page"]:02}: {p["title"]}' for p in rows]
  for i,(pg,name) in enumerate(zip(pdf.pages,names)):
   assert abs(float(pg.mediabox.width)-A4[0])<.01 and abs(float(pg.mediabox.height)-A4[1])<.01
   assert pdf.get_destination_page_number(pdf.outline[i])==i
   # Verify the actual embedded page raster, not just the bookmark label.
   images=list(pg.images);assert len(images)==1
   with Image.open(ROOT/name) as original:
    assert images[0].image.convert('RGB').tobytes()==original.convert('RGB').tobytes()
 html=(ROOT/'index.html').read_text();assert html.index('id="JEE"')<html.index('id="Olympiad"')
 checks=physics()
 report=dict(pages=23,jee=19,extensions=4,png_dimensions=[2480,3508],dpi=300,safe_margin_test_px=120,cards_checked=92,pdfs_checked=3,zips_checked=3,embedded_pdf_images_verified=46,physics_checks=checks,limits='Representative physics checks; not exhaustive certification of the source paper. Diagram bounds checked during render; visual review separately documented in README.')
 report['jee_displayed_equations']=sum(k=='m' for p in groups['JEE'] for c in p['cards'] for k,t in c['items'])
 report['jee_mean_card_height_fraction']=float(np.mean([c['used_px']/c['available_px'] for c in layout['cards'][:76]]))
 (ROOT/'verification.json').write_text(json.dumps(report,indent=2)+'\n')
 for file in ['index.html','README.md','SCOPE.md','SOURCE-AUDIT.md']:
  s=(ROOT/file).read_text()
  links=re.findall(r'(?:href|src)="([^"]+)"',s)+re.findall(r'\]\(([^)]+)\)',s)
  for link in links:
   if link.startswith(('#','https:','http:')):continue
   assert (ROOT/link.split('#')[0]).exists(),(file,link)
 print('PASS: all 23 PNGs, 92 cards, 3 PDFs with bookmarks and exact embedded-image order, 3 PNG-only ZIPs, local links; '+str(len(checks))+' representative physics/source checks.')
if __name__=='__main__':test()
