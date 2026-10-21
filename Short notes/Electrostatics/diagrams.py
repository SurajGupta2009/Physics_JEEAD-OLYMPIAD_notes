"""74 native page-specific mathematical graphs and labelled geometrical schematics."""
import numpy as np
from matplotlib.patches import Circle,Rectangle,Arc
I='#153149';T='#087d7d';R='#a43232';Y='#fff2b8'
def txt(a,x,y,s,**kw):a.text(x,y,s,color=I,fontsize=11,**kw)
def arr(a,p,q,c=T):a.annotate('',xy=q,xytext=p,arrowprops=dict(arrowstyle='->',color=c,lw=1.6))
def line(a,p,q,**kw):a.plot([p[0],q[0]],[p[1],q[1]],color=kw.pop('color',I),**kw)
def charge(a,x,y,label,c=R):
 a.add_patch(Circle((x,y),.14,color=c));txt(a,x,y+.22,label,ha='center')
def circle(a,x,y,r,**kw):a.add_patch(Circle((x,y),r,fill=False,ec=T,lw=1.6,**kw))
def plain(a):a.axis('off');a.set(xlim=(-3,3),ylim=(-1.75,1.75));a.set_aspect('equal')
def plot(a,x,y,xl,yl,label=None):
 a.axis('on');a.autoscale(enable=True);a.plot(x,y,c=T,label=label);a.set_xlabel(xl,fontsize=11);a.set_ylabel(yl,fontsize=11);a.spines[['top','right']].set_visible(False);a.tick_params(labelsize=9);a.grid(alpha=.13)
def leg(a):a.legend(fontsize=9,frameon=True,facecolor='white',framealpha=1,edgecolor='#bbd9d4')
def bars(a,labels,values,yl):
 a.axis('on');a.autoscale(enable=True);a.bar(labels,values,color=[T,I,R,T]);a.set_ylabel(yl,fontsize=11);a.spines[['top','right']].set_visible(False);a.tick_params(labelsize=9)
def fields(a,dipole=False,contour=False):
 x=np.linspace(-2.7,2.7,110);z=np.linspace(-1.6,1.6,90);X,Z=np.meshgrid(x,z);ex=np.zeros_like(X);ez=ex.copy();v=ex.copy()
 for yy,q in [(-.7,-1 if dipole else 1),(.7,1)]:
  rr=np.maximum(X*X+(Z-yy)**2,.0196);ex+=q*X/rr**1.5;ez+=q*(Z-yy)/rr**1.5;v+=q/np.sqrt(rr)
 if contour:a.contour(X,Z,v,levels=[-3,-2,-1,-.5,.5,1,2,3] if dipole else [1,1.5,2,2.5,3,4,5],colors=T,linewidths=1)
 else:a.streamplot(x,z,ex,ez,color=T,density=.65,linewidth=.9,arrowsize=1)
 charge(a,0,-.7,'-q' if dipole else '+q',T if dipole else R);charge(a,0,.7,'+q');a.set(xlim=(-2.7,2.7),ylim=(-1.6,1.6))
def figure(a,key):
 slug,side=key.rsplit('-',1);plain(a)
 if side=='b':
  x=np.linspace(.05,3,200)
  if slug=='charge':
   n=np.arange(-4,5);plot(a,n,n,'signed electron deficit n','q / e');a.scatter(n,n,c=R);return 'Allowed net charges are integer multiples of e'
  if slug=='coulomb':plot(a,x,1/x**2,'r / r0','F / F(r0)');a.set_ylim(0,5);return 'Fixed charges: inverse-square force, not inverse distance'
  if slug=='equilibrium':
   x=np.linspace(.05,.95,240);plot(a,x,1/x**2-4/(1-x)**2,'x / L','E / (kq/L squared)');a.axhline(0,c=I,lw=.8);a.set_ylim(-40,40);a.scatter([1/3],[0],c=R);return '+q at 0, +4q at L: field null is at L/3'
  if slug=='field-density':fields(a,True);return 'Dipole field lines: from positive to negative source'
  if slug=='ring':
   x=np.linspace(-3,3,240);plot(a,x,x/(1+x*x)**1.5,'x / R','scaled E and V','E / (kQ/R squared)');a.plot(x,1/np.sqrt(1+x*x),c=R,label='V / (kQ/R)');leg(a);return 'Ring axis: E is odd, V even; E peaks at |x|/R=1/sqrt(2)'
  if slug=='rod':
   plot(a,x,2/(x*np.sqrt(1+x*x)),'d / L','E / (k lambda/L)','finite rod, length 2L');a.plot(x,2/x,c=R,label='infinite line');a.set_ylim(0,12);leg(a);return 'Finite rod converges to an infinite line only for d much less than L'
  if slug=='arc':
   th=np.linspace(.15,2*np.pi,180);plot(a,th,2*np.sin(th/2)/th,'arc angle (rad)','E / (kQ/R squared)');return 'Arc comparison at FIXED total charge Q: lambda changes with angle'
  if slug=='disc':
   plot(a,x,1-x/np.sqrt(1+x*x),'x / R','scaled E and V','E / (sigma/2epsilon0)');a.plot(x,np.sqrt(1+x*x)-x,c=R,label='V / (sigma R/2epsilon0)');leg(a);return 'Positive side of disc: finite field limit and continuous potential'
  if slug=='dipole-field':fields(a,True,True);return 'Dipole equipotentials: zero mid-plane is not a zero-field region'
  if slug=='dipole-action':
   th=np.linspace(0,np.pi,150);plot(a,th,-np.cos(th),'theta (rad)',r'$U/(pE),\quad |\tau|/(pE)$','U / pE');a.plot(th,np.sin(th),c=R,label='torque magnitude / pE');leg(a);return 'Aligned is the rotational energy minimum; anti-aligned is a maximum'
  if slug=='motion':
   plot(a,np.linspace(-1,1),1-np.linspace(-1,1),'qV / K0','K / K0');return 'Static field energy: K + qV stays constant; physical K is nonnegative'
  if slug=='mechanics':
   charge(a,-1,-.7,'q');charge(a,1,-.7,'q');line(a,(0,1.4),(-1,-.7));line(a,(0,1.4),(1,-.7));arr(a,(-1,-.7),(-2,-.7));arr(a,(1,-.7),(2,-.7));txt(a,0,-1.3,'separation = 2 ell sin(theta)',ha='center');txt(a,0,1.45,'common support',ha='center');return 'Equal bobs: horizontal repulsion and symmetric string geometry'
  if slug=='flux':
   charge(a,-2,0,'q');line(a,(-2,0),(1.5,1.1));line(a,(-2,0),(1.5,-1.1));a.add_patch(Arc((1.5,0),.65,2.2,theta1=-90,theta2=90,ec=T,lw=2));txt(a,1.95,0,'disc',ha='center');txt(a,-.3,.15,'solid angle',ha='center');return 'Open-surface flux from a point charge is kq times signed solid angle'
  if slug=='flux-cube':
   f=[np.arctan(1/3)/(2*np.pi),np.arctan(4/3)/(4*np.pi)];bars(a,['x=a, y=a\neach','z=0, z=a\neach'],f,'flux / (q/epsilon0)');return 'Mid-edge source: two pairs of unequal face fluxes; total fraction 1/4'
  if slug=='gauss':
   a.add_patch(Rectangle((-1.3,-.65),2.6,1.3,ec=T,fc='none',ls='--'));line(a,(-2,0),(2,0),color=R,lw=2);arr(a,(0,.65),(0,1.3));arr(a,(0,-.65),(0,-1.3));txt(a,1.5,.8,'curved wall',ha='center');txt(a,0,.15,'line charge lambda',ha='center');return 'Cylindrical Gaussian surface: curved wall contributes; caps do not'
  if slug=='spheres':
   r=np.linspace(0,3,240);vs=np.where(r<1,1,1/np.maximum(r,.001));vb=np.where(r<1,(3-r*r)/2,1/np.maximum(r,.001));plot(a,r,vs,'r / R','V / (kQ/R)','shell');a.plot(r,vb,c=R,label='uniform solid');leg(a);return 'Potential continuous at R; solid centre is 3/2 of its surface value'
  if slug=='cavity-superposition':
   r=np.linspace(0,1,120);plot(a,r,r,'r / R','E / E(R)','uniform rho');a.plot(r,r*r,c=R,label='rho proportional to r');leg(a);return 'Normalised interior fields: radial charge density changes the power'
  if slug=='cylinders':
   r=np.linspace(.1,3,400);e=np.where((r>1)&(r<2),1/r,0);plot(a,r,e,'r / a  (b=2a)',r'$E/(\lambda/2\pi\varepsilon_0a)$');return 'Neutral ideal coax: gap field only; one-sided jumps at conductor faces'
  if slug=='sheets':
   for x0 in [-1,1]:a.add_patch(Rectangle((x0-.18,-1.15),.36,2.3,fc='#eff8f5',ec=T))
   txt(a,-2.2,.3,'outer\n(S/2)',ha='center');txt(a,-.42,.1,'+D/2',ha='center');txt(a,.42,.1,'-D/2',ha='center');txt(a,2.2,.3,'outer\n(S/2)',ha='center');txt(a,0,-1.5,'S=Q1+Q2; D=Q1-Q2; equal large areas',ha='center');return 'Four face-charge ledger: isolated plates, no imposed external field'
  if slug=='slab':
   x=np.linspace(-3,3,240);v=np.where(abs(x)<1,-x*x/2,-abs(x)+.5);plot(a,x,v,'x / a',r'$\Delta V/(\rho a^2/\varepsilon_0)$');return 'Uniform slab potential: parabola inside, straight branches outside'
  if slug=='conductor':
   x=np.linspace(-2,2,150);plot(a,x,x*x/2,'sigma / sigma0',r'$P/(\sigma_0^2/\varepsilon_0)$');return 'Electrical pressure is outward and independent of the sign of charge'
  if slug=='conducting-cavity':
   circle(a,0,0,1.25);circle(a,0,0,.7);txt(a,0,0,'empty\ncavity\nE = 0',ha='center',va='center');txt(a,0,1.45,'equipotential metal wall',ha='center');
   for yy in [-.8,0,.8]:arr(a,(-2.7,yy),(-1.5,yy))
   txt(a,-2.1,-1.3,'external field',ha='center');return 'Empty closed cavity: outer polarisation shields the interior'
  if slug=='potential':
   x=np.linspace(-2,2);plot(a,x,-x,'x / x0','[V(x)-V(0)] / (E x0)');return 'Uniform field along +x: potential falls linearly as x increases'
  if slug=='potential-distributions':fields(a,False,True);return 'Like-charge equipotentials: scalar addition, not vector cancellation'
  if slug=='gradient':
   x=np.linspace(-1.7,1.7);plot(a,x,x*x,'x / x0','normalised V and Ex','V = x squared');a.plot(x,-2*x,c=R,label='Ex = -2x');leg(a);return 'Derivative sign: a rising potential produces a field toward lower x'
  if slug=='mutual-energy':
   plot(a,x,1/x,'separation / r0','U / (k q squared/r0)','like signs');a.plot(x,-1/x,c=R,label='unlike signs');a.set_ylim(-5,5);leg(a);return 'Pair interaction energy: force is minus its separation derivative'
  if slug=='sharing':bars(a,['initial','final','released'],[1,.25,.75],'energy / initial energy');return '2 cm sphere at 3000 V joined to neutral 6 cm sphere: 75% leaves field store'
  if slug=='concentric':
   r=np.linspace(.2,3,240);v=np.where(r<1,.5,np.where(r<2,1/r-.5,0));plot(a,r,v,'r / a   (b=2a)','V / (kq/a)');return 'Inner charged sphere and grounded outer shell: V=0 outside b'
  if slug=='self-energy':
   r=np.linspace(.01,1,150);plot(a,r,r**5/10,'r / R',r'$U_{\rm in}/(kQ^2/R)$');return 'Uniform solid: interior energy to r grows as r to the fifth power'
  if slug=='laplace':
   t=np.linspace(0,2,150);plot(a,t,np.cos(t),'omega_z t',r'$u/u_0$','axial oscillation');a.plot(t,np.cosh(t/np.sqrt(2)),c=R,label='transverse growth');leg(a);return 'u0 is initial displacement: stable axial vs unstable transverse motion'
  if slug=='image-plane':
   s=np.linspace(0,3,150);plot(a,s,-1/(1+s*s)**1.5,'lateral radius / h',r'$\sigma/(q/2\pi h^2)$');return 'Grounded plane: induced charge density peaks beneath the real source'
  if slug=='image-sphere':
   d=np.linspace(1.15,4,180);fg=-d/(d*d-1)**2;fi=fg+1/d**3;plot(a,d,fg,'d / R',r'$F/(kq^2/R^2)$','grounded');a.plot(d,fi,c=R,label='isolated neutral');a.set_ylim(-8,.2);leg(a);return 'Both spheres polarise; grounding and neutrality give different forces'
  if slug=='pressure-bubble':
   r=np.linspace(.55,2,150);plot(a,r,1/r,'R / R0',r'$P/P_0$','capillary, fixed gamma');a.plot(r,1/r**4,c=R,label='electrical, fixed Q');leg(a);return 'Pressure scales differ: capillary R^-1 versus electrical R^-4'
  if slug=='drops':
   z=np.linspace(0,1.1,180);du=(2**(2/3)-2)+4*z*z*(2**(2/3)-1);plot(a,z,du,'q / Q_R(r)',r'$\Delta U/(4\pi\gamma r^2)$');a.axhline(0,c=I,lw=.8);a.axvline(.419,c=R,ls='--');return 'Two far-separated drops to one sphere: endpoint-energy threshold about 0.419'
  if slug=='multipoles':
   r=np.linspace(1,5,150);plot(a,r,1/r,'r / r0','normalised potential','monopole');a.plot(r,1/r**2,c=R,label='dipole');a.plot(r,1/r**3,c=I,label='quadrupole');leg(a);return 'Successive multipoles fall faster; coefficients and angular factors differ'
  if slug=='offaxis':bars(a,['corner','centre'],[1.19004,2.38008],'V / (k rho L squared)');return 'Uniform cube: centre/corner potential ratio two from scaling and tiling'
  if slug=='measurements':
   r=np.linspace(0,.5,100);plot(a,r,-r/3,'r / R',r'$E/(\delta kQ/R^2)$');return 'Perturbed inverse square: leading field inside a uniformly charged shell'
  raise KeyError(key)
 # First panel: labelled physical geometry.
 if slug=='charge':
  a.add_patch(Rectangle((-2.5,-.8),.35,1.6,fc=R));txt(a,-2.35,1,'negative rod',ha='center');circle(a,.15,0,.85);txt(a,-.35,.1,'+ +',ha='center');txt(a,.65,.1,'- -',ha='center');line(a,(1,0),(2,0));arr(a,(1.2,0),(2,0));txt(a,2,-.45,'Earth',ha='center');txt(a,.3,-1.25,'disconnect Earth BEFORE removing rod',ha='center');return 'Induction: negative rod expels electrons while Earth is connected'
 if slug=='coulomb':
  h=np.sqrt(3);charge(a,-1,-.65,'+q');charge(a,1,-.65,'+q');charge(a,0,h-.65,'-q',T);line(a,(-1,-.65),(1,-.65));line(a,(-1,-.65),(0,h-.65));arr(a,(-1,-.65),(-2,-.65));arr(a,(-1,-.65),(-.5,.216));arr(a,(-1,-.65),(-1.5,.216),R);txt(a,-2.2,.5,'resultant',ha='center');return 'Mixed triangle: left positive charge has resultant up and left (120 degrees)'
 if slug=='equilibrium':
  charge(a,-2,0,'+q1');charge(a,2,0,'+q2');charge(a,-.5,0,'negative q3',T);arr(a,(-.5,-.6),(-1.4,-.6));arr(a,(-.5,-.6),(.4,-.6));txt(a,0,1.15,'balance all THREE if none is fixed',ha='center');return 'Three-charge equilibrium: field null fixes position, outer balance fixes q3'
 if slug=='field-density':
  circle(a,-.4,0,1);a.add_patch(Arc((-.4,0),2,2,theta1=20,theta2=65,ec=R,lw=6));line(a,(-.4,0),(.45,.5));txt(a,-.4,0,'O',ha='center');txt(a,1.2,.7,'dq = lambda R dtheta',ha='center');txt(a,1.4,-.4,'R',ha='center');return 'Density bookkeeping: an angular ring element has length R dtheta'
 if slug=='ring':
  a.add_patch(Arc((-1,0),.8,2.4,theta1=0,theta2=360,ec=T,lw=2));line(a,(-2.2,0),(2.5,0));charge(a,1.6,0,'P(x)');line(a,(-1,1.2),(1.6,0),ls='--');txt(a,-.7,.7,'R',ha='center');arr(a,(1.6,0),(2.4,0));txt(a,.3,-1.5,'transverse parts cancel; net E is axial',ha='center');return 'Ring axis: equal source distances, projection cos(angle)=x/distance'
 if slug=='rod':
  line(a,(-2,-.8),(1.5,-.8),color=R,lw=4);charge(a,0,1,'P');line(a,(0,-.8),(0,1),ls='--');line(a,(-2,-.8),(0,1),ls='--');line(a,(1.5,-.8),(0,1),ls='--');txt(a,-2,-1.2,'-a',ha='center');txt(a,1.5,-1.2,'b',ha='center');txt(a,.2,0,'d');txt(a,0,-1.2,'0',ha='center');return 'Unequal rod ends: both parallel and perpendicular field components survive'
 if slug=='arc':
  a.add_patch(Arc((0,-.15),2.4,2.4,theta1=15,theta2=165,ec=R,lw=3));line(a,(0,-.15),(1.16,.16),ls='--');line(a,(0,-.15),(-1.16,.16),ls='--');arr(a,(0,-.15),(0,-1.2));txt(a,.3,-.8,'E');txt(a,0,1.2,'positive arc',ha='center');txt(a,1.65,.25,'R',ha='center');return 'Positive upper arc: at its centre the net electric field points downward'
 if slug=='disc':
  circle(a,-.5,0,1.2);circle(a,-.5,0,.7);a.add_patch(Arc((-.5,0),1.4,1.4,theta1=20,theta2=160,ec=R,lw=4));arr(a,(-.5,0),(.2,0));txt(a,.1,-.3,'s',ha='center');txt(a,1.6,.5,'thin ring');txt(a,1.5,-.2,'dq = 2 pi s sigma ds',ha='center');return 'Disc decomposition: integrate thin concentric rings from s=0 to R'
 if slug=='dipole-field':
  charge(a,0,-.8,'-q',T);charge(a,0,.8,'+q');arr(a,(.5,-.8),(.5,.8));txt(a,.75,0,'p');charge(a,1.8,0,'P on equator',I);arr(a,(1.8,-.2),(1.8,-1));txt(a,-1.2,0,'V = 0\non equator',ha='center');return 'Equatorial field is antiparallel to p even though equatorial V is zero'
 if slug=='dipole-action':
  charge(a,-.8,-.45,'-q',T);charge(a,.8,.45,'+q');line(a,(-.8,-.45),(.8,.45));arr(a,(.8,.45),(2,.45));arr(a,(-.8,-.45),(-2,-.45));arr(a,(-.8,1.3),(1.2,1.3));txt(a,1.45,1.25,'E');txt(a,0,-1.2,'equal opposite forces; nonzero couple',ha='center');return 'Permanent dipole in uniform E: zero resultant, torque toward alignment'
 if slug=='motion':
  line(a,(-2,-1.1),(1,-1.1),lw=3);line(a,(-2,1),(1,1),lw=3);x=np.linspace(-2,1,100);a.plot(x,-.5+.12*(x+2)**2,c=R);a.plot([1,2.4],[.58,1.588],c=R);arr(a,(-2.7,-.5),(-2,-.5));txt(a,-.5,1.3,'uniform E upward; q>0',ha='center');txt(a,1.8,-.8,'drift',ha='center');return 'Parabola inside plates, straight tangent after exit; shown for positive q'
 if slug=='mechanics':
  line(a,(0,1.4),(1,-.8));charge(a,1,-.8,'q>0');arr(a,(1,-.8),(1,-1.6),I);arr(a,(1,-.8),(2,-.8),R);arr(a,(1,-.8),(.5,.3));txt(a,2,-.45,'qE',ha='center');txt(a,1.55,-1.55,'mg');txt(a,-.2,.3,'tension',ha='center');return 'Charged pendulum: three forces, tension along the actual tilted string'
 if slug=='flux':
  a.add_patch(Rectangle((-.8,-.8),1.6,1.6,angle=0,fill=False,ec=T));arr(a,(0,0),(1.8,0));arr(a,(0,0),(1.4,1.2),R);txt(a,2,0,'normal',ha='center');txt(a,1.5,1.35,'E',ha='center');txt(a,-1.7,-1.2,'theta is to the NORMAL',ha='center');return 'Flux uses E dot area vector; angle is measured from the surface normal'
 if slug=='flux-cube':
  for p,q in [((-1,-1),(1,-1)),((1,-1),(1,1)),((1,1),(-1,1)),((-1,1),(-1,-1)),((-.4,-.5),(1.6,-.5)),((1.6,-.5),(1.6,1.5)),((1.6,1.5),(-.4,1.5)),((-.4,1.5),(-.4,-.5))]:line(a,p,q)
  for p in [(-1,-1),(1,-1),(1,1),(-1,1)]:line(a,p,(p[0]+.6,p[1]+.5))
  charge(a,.3,.25,'centre');txt(a,-1.8,1.1,'6 equal faces',ha='center');return 'Cube centre is symmetric under face permutations; an edge midpoint is not'
 if slug=='gauss':
  circle(a,0,0,1.15);charge(a,0,0,'Q');
  for th in np.linspace(0,2*np.pi,8,endpoint=False):arr(a,(1.15*np.cos(th),1.15*np.sin(th)),(1.55*np.cos(th),1.55*np.sin(th)))
  txt(a,2.2,-.3,'E normal\nand constant',ha='center');return 'Spherical Gaussian surface: source rotational symmetry makes E extractable'
 if slug=='spheres':
  r=np.linspace(0,3,240);shell=np.where(r<1,0,1/np.maximum(r,.01)**2);solid=np.where(r<1,r,1/np.maximum(r,.01)**2);plot(a,r,shell,'r / R','E / (kQ/R squared)','shell');a.plot(r,solid,c=R,label='uniform solid');leg(a);return 'Spherical fields: shell jumps at R; uniform volume charge is continuous'
 if slug=='cavity-superposition':
  circle(a,-.3,0,1.45);circle(a,.35,.1,.62);arr(a,(-.3,0),(.35,.1),I);arr(a,(.2,-.1),(.85,0),R);txt(a,-1.8,1.25,'fixed +rho');txt(a,1.7,.3,'hole\nE along a',ha='center');txt(a,0,-1.6,'a: full centre to cavity centre',ha='center');return 'Offset insulating spherical hole: uniform E=rho a/(3 epsilon0)'
 if slug=='cylinders':
  circle(a,0,0,.55);circle(a,0,0,1.25);txt(a,-1.9,-.8,'inner +lambda',ha='center');txt(a,1.9,1,'outer -lambda',ha='center');arr(a,(0,0),(.55,0));txt(a,.32,-.5,'a');line(a,(0,0),(-.88,.88),ls='--');txt(a,-.7,.4,'b');return 'Coaxial cross-section: radial field in the insulating gap, zero in metal'
 if slug=='sheets':
  for xx,s in [(-1,'+sigma'),(1,'-sigma')]:line(a,(xx,-1.1),(xx,1.1),lw=3,color=R if xx<0 else T);txt(a,xx,1.3,s,ha='center')
  for yy in [-.5,.2,.8]:arr(a,(-.6,yy),(.6,yy))
  txt(a,-2.2,0,'E=0',ha='center');txt(a,2.2,0,'E=0',ha='center');txt(a,0,-1.4,'gap E = sigma/epsilon0',ha='center');return 'Equal opposite infinite sheets: fields add inside and cancel outside'
 if slug=='slab':
  x=np.linspace(-3,3,200);plot(a,x,np.clip(x,-1,1),'x / a','Ex / (rho a/epsilon0)');return 'Uniform slab of thickness 2a: odd field, linear inside and constant outside'
 if slug=='conductor':
  a.add_patch(Rectangle((-2.5,-1.3),2.5,2.6,fc='#eff8f5',ec=T));txt(a,-1.3,.9,'metal');txt(a,-1.3,0,'E = 0',ha='center');arr(a,(0,0),(1.8,0));txt(a,1.5,.5,'Eout = sigma/epsilon0',ha='center');txt(a,.3,-1.7,'normal jump; no tangential field',ha='center');return 'Local metal surface: field normal outside; interior field vanishes'
 if slug=='conducting-cavity':
  circle(a,0,0,1.35);circle(a,0,0,.85);charge(a,.35,.15,'q');txt(a,-2,.5,'inner wall\nsum -q',ha='center');txt(a,2.1,-.6,'outer wall\nQc + q',ha='center');txt(a,0,-1.6,'metal net charge = Qc',ha='center');return 'A charge in a closed cavity induces -q inside, leaving Qc+q outside'
 if slug=='potential':
  for rr in [.5,.95,1.4]:circle(a,0,0,rr)
  charge(a,0,0,'+Q');arr(a,(.5,0),(1.7,0));txt(a,2.1,.6,'E outward',ha='center');txt(a,0,-1.6,'V decreases with radius; circles are equipotentials',ha='center');return 'Point charge: radial E is normal to spherical equipotentials'
 if slug=='potential-distributions':
  x=np.linspace(0,3,150);plot(a,x,1/np.sqrt(1+x*x),'x / R','normalised V','ring');a.plot(x,np.sqrt(1+x*x)-x,c=R,label='disc');leg(a);return 'Axial potentials normalised to their own centre values'
 if slug=='gradient':
  x=np.linspace(-1.4,1.4,60);X,Y=np.meshgrid(x,x);a.contour(X,Y,X*X-Y*Y,levels=np.linspace(-1.5,1.5,9),colors=T);arr(a,(0,0),(1,0),R);txt(a,2.0,.7,'V = x*x\nminus y*y',ha='center');return 'A source-free saddle can curve up along one axis and down along another'
 if slug=='mutual-energy':
  for xx,yy in [(-1,-1),(1,-1),(1,1),(-1,1)]:charge(a,xx,yy,'q')
  for p,q in [((-1,-1),(1,-1)),((1,-1),(1,1)),((1,1),(-1,1)),((-1,1),(-1,-1)),((-1,-1),(1,1)),((-1,1),(1,-1))]:line(a,p,q,ls='--')
  txt(a,0,-1.5,'4 side pairs + 2 diagonal pairs',ha='center');return 'Mutual energy counts all unordered pairs once, including diagonals'
 if slug=='sharing':
  circle(a,-1.65,0,.4);circle(a,1.05,0,1.2);line(a,(-1.25,0),(-.15,0));txt(a,-1.65,.65,'R',ha='center');txt(a,1.05,1.45,'3R',ha='center');txt(a,0,-1.5,'far apart approximation: equal V, Q ratio 1:3',ha='center');return 'Connected spheres: schematic wire; the calculation neglects mutual influence'
 if slug=='concentric':
  circle(a,0,0,.55);circle(a,0,0,1.25);txt(a,0,0,'q',ha='center');txt(a,-1.95,.8,'inner radius a',ha='center');txt(a,2.1,-.7,'outer\nradius b\nnet Q',ha='center');return 'Concentric conductor potentials include the other shell constant'
 if slug=='self-energy':
  bars(a,['shell exterior','solid interior','solid total'],[.5,.1,.6],'U / (kQ squared/R)');return 'Same Q and R: solid self-energy exceeds shell self-energy by kQ squared/(10R)'
 if slug=='laplace':
  x=np.linspace(-1,1,150);plot(a,x,1-x*x/2,'displacement / R','V / (kQ/R)','axial near centre');a.plot(x,1+x*x/4,c=R,label='transverse near centre');leg(a);return 'Ring centre expansion: axial downward curvature, half-size transverse upward curvature'
 if slug=='image-plane':
  line(a,(-2.5,0),(2.5,0),lw=3);charge(a,0,1,'real +q');charge(a,0,-1,'image -q',T);line(a,(0,-1),(0,1),ls='--');txt(a,1.7,.3,'ground V=0',ha='center');txt(a,-1.8,-.7,'image only\nnot physical field',ha='center');return 'Grounded plane: mirror -q makes the plane an equipotential'
 if slug=='image-sphere':
  circle(a,-.7,0,1);charge(a,1.6,0,'real q');charge(a,-.27,0,'image q-prime',T);line(a,(-.7,0),(1.6,0),ls='--');txt(a,-.8,1.35,'sphere R, grounded',ha='center');txt(a,0,-1.4,'b = R squared/d; q-prime = -q R/d',ha='center');return 'Grounded sphere: internal mathematical image, exterior physical solution'
 if slug=='pressure-bubble':
  circle(a,0,0,1);line(a,(-1,0),(1,0),ls='--');
  for th in np.linspace(.2,np.pi-.2,5):arr(a,(np.cos(th),np.sin(th)),(1.5*np.cos(th),1.5*np.sin(th)),R)
  txt(a,0,-1.5,'hemisphere force = pressure x projected disc area',ha='center');return 'Radial electrical stress: axial components over a hemisphere add'
 if slug=='drops':
  circle(a,-1.8,.2,.45);circle(a,-.7,.2,.45);arr(a,(0,.2),(.7,.2));circle(a,1.5,.2,2**(1/3)*.45);txt(a,-1.3,-.8,'two: r, q each',ha='center');txt(a,1.5,-.8,'one: 2^(1/3)r, 2q',ha='center');return 'Drop merging conserves volume and total charge, not surface area'
 if slug=='multipoles':
  charge(a,-1.5,0,'+q');charge(a,0,0,'-2q',T);charge(a,1.5,0,'+q');txt(a,0,1,'net Q = 0; net p = 0',ha='center');txt(a,0,-1.1,'first surviving far potential is quadrupolar',ha='center');return 'Symmetric linear quadrupole: monopole and dipole terms cancel'
 if slug=='offaxis':
  s=np.linspace(0,.85,150);phi=np.linspace(0,2*np.pi,3000,endpoint=False);v=np.mean(1/np.sqrt(1+s[:,None]**2-2*s[:,None]*np.cos(phi)),axis=1);plot(a,s,v,'s / R','V / (kQ/R)','in ring plane, z=0');a.plot(s,1/np.sqrt(1+s*s),c=R,label='on axis at z=s');leg(a);return 'Ring centre is a saddle: in-plane V rises while axial V falls'
 if slug=='measurements':
  circle(a,0,0,1.3);circle(a,0,0,.65);txt(a,0,0,'inner\ndetector',ha='center');txt(a,1.9,.9,'outer charged\nshell',ha='center');txt(a,0,-1.6,'look for a small residual, not a large direct force',ha='center');return 'Schematic shell null test: actual inference needs apparatus modelling'
 raise KeyError(key)
