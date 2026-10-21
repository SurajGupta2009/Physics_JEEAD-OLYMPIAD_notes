"""74 native page-specific mathematical graphs and labelled geometrical schematics."""
import numpy as np
from matplotlib.patches import Circle,Rectangle,Arc
I='#153149';T='#087d7d';R='#a43232'
def txt(a,x,y,s,**kw):a.text(x,y,s,color=I,fontsize=kw.pop('fontsize',11),**kw)
def arr(a,p,q,c=T):a.annotate('',xy=q,xytext=p,arrowprops=dict(arrowstyle='->',color=c,lw=1.6))
def line(a,p,q,**kw):a.plot([p[0],q[0]],[p[1],q[1]],color=kw.pop('color',I),**kw)
def circ(a,x,y,r,**kw):a.add_patch(Circle((x,y),r,fill=False,ec=kw.pop('ec',T),lw=kw.pop('lw',1.6),**kw))
def dot(a,x,y,c=R):a.add_patch(Circle((x,y),.12,color=c))
def plain(a):a.axis('off');a.set(xlim=(-3,3),ylim=(-1.75,1.75));a.set_aspect('equal')
def plot(a,x,y,xl,yl,label=None):
 a.axis('on');a.autoscale(enable=True);a.plot(x,y,c=T,label=label);a.set_xlabel(xl,fontsize=11);a.set_ylabel(yl,fontsize=11);a.spines[['top','right']].set_visible(False);a.tick_params(labelsize=9);a.grid(alpha=.13)
def leg(a):a.legend(fontsize=9,frameon=True,facecolor='white',framealpha=1,edgecolor='#bbd9d4')
def bars(a,labels,values,yl):
 a.axis('on');a.autoscale(enable=True);a.bar(labels,values,color=[T,I,R,T]);a.set_ylabel(yl,fontsize=11);a.spines[['top','right']].set_visible(False);a.tick_params(labelsize=9)
def into_page(a,x,y,s='B'):txt(a,x,y,r'$\otimes$ '+s,ha='center',fontsize=14)
def figure(a,key):
 slug,side=key.rsplit('-',1);plain(a)
 if side=='b':
  x=np.linspace(.05,3,200)
  if slug=='lorentz':
   th=np.linspace(0,np.pi,150);plot(a,th,np.sin(th),'angle v to B (rad)',r'$F/(|q|vB)$');return 'Magnetic force peaks perpendicular and vanishes parallel to B'
  if slug=='circle':
   v=np.linspace(0,2,120);plot(a,v,v,'v / v0','r / r0 and T / T0','radius r');a.plot(v,np.ones_like(v),c=R,label='period T');leg(a);return 'Radius grows with speed; the period stays fixed'
  if slug=='selector':
   v=np.linspace(.4,1.6,120);plot(a,v,1/v,'v / (E/B)','forces (norm.)','F_E constant');a.plot(v,v,c=R,label='F_B proportional to v');a.set_ylim(.4,1.7);leg(a);return 'Forces cross at v = E/B: slower bends one way, faster the other'
  if slug=='regions':
   r=np.linspace(.05,3,160);t=np.where(r>1,np.arcsin(np.minimum(1,1/r)),np.pi);plot(a,r,t,'r / d',r'$t/(m/qB)$');return 'Time in the strip: crossing branch then a jump to the half turn'
  if slug=='spectrometer':
   m=np.linspace(1,4,120);plot(a,m,np.sqrt(m),'m / m0','r / r0');a.scatter([1,4],np.sqrt([1,4]),c=R);return 'Radius grows as the square root of mass at fixed q, V and B'
  if slug=='cyclotron':
   n=np.arange(0,280,40);plot(a,n,2*n,'turns',r'$K/(qV_0)$');return 'Energy grows by 2qV0 per turn: linear until the exit radius'
  if slug=='mirror':
   z=np.linspace(0,3,150);B=1+.12*z**2;plot(a,z,B,'z / z0','B and v_par','B increasing');a.plot(z,1/np.sqrt(B),c=R,label='v_par falls as 1/sqrt(B)');leg(a);return 'Invariant mu: parallel speed falls until reflection where B = B0/sin^2(theta0)'
  if slug=='hall':
   n=np.logspace(20,29,80);vh=1/(n*1.6e-19*1e-3);plot(a,n,vh,'n (m^-3)',r'$V_H$ at $IB/t=1$');a.set_xscale('log');a.set_yscale('log');a.scatter([8.5e28],[0.73e-6],c=R);a.scatter([1e21],[0.31],c=R);return 'Hall voltage is inversely proportional to carrier density'
  if slug=='drifts':
   t=np.linspace(0,2*np.pi,200);x=t-np.sin(t);y=1-np.cos(t);plot(a,x,y,'x / r_c','y / r_c');return 'Cycloid from rest: cusps every period, arch height 2 r_c'
  if slug=='tracks':
   b=np.linspace(.1,3,120);plot(a,b,300*b,'B (T)','p [MeV/c]');return '300 Br rule at r = 1 m: momentum is linear in the field'
  if slug=='biot':
   th=np.linspace(0,np.pi,150);plot(a,th,np.sin(th),'angle element to r','dB factor');return 'Biot-Savart weight: sin theta vanishes for elements along the line of sight'
  if slug=='wire':
   d=np.linspace(.1,3,160);plot(a,d,1/d,'d (normalised)',r'$B/( \mu_0 I/2\pi d_0)$','infinite wire');a.plot(d,.5/d,c=R,label='semi-infinite end');a.set_ylim(0,6);leg(a);return 'Same 1/d falloff; the end-on wire is half the infinite field'
  if slug=='loop':
   xx=np.linspace(-3,3,200);plot(a,xx,1/(1+xx*xx)**1.5,'x / R',r'$B/B(0)$','on axis');return 'Loop axis field: maximum at centre, dipole 1/x^3 tail far away'
  if slug=='solenoid':
   z=np.linspace(-6,6,240);th1=np.arctan2(1,z+6);th2=np.arctan2(1,6-z);plot(a,z,(np.cos(th1)+np.cos(th2))/2,'z / R',r'$B/(\mu_0 nI)$','finite solenoid');a.axhline(1,c=R,ls='--');return 'End field falls to half of the interior value at the winding'
  if slug=='moment':
   r=np.linspace(1,4,120);plot(a,r,2/r**3,'r / r0','scaled B','axial, 2 mu/r^3');a.plot(r,1/r**3,c=R,label='equatorial, mu/r^3');a.set_ylim(0,2.2);leg(a);return 'Dipole field: axial component twice equatorial at the same distance'
  if slug=='ampere':
   r=np.linspace(.5,3,120);plot(a,r,np.ones_like(r),'Amperian radius / r0',r'$\oint B\,dl/(\mu_0 I)$');return 'Circulation is independent of radius: the loop law in one picture'
  if slug=='ampere-apps':
   r=np.linspace(0,3,240);B=np.where(r<1,r,1/np.maximum(r,.01));plot(a,r,B,'r / a',r'$B/( \mu_0 I/2\pi a)$','thick wire');return 'Inside linear growth, outside 1/r: one continuous B(r)'
  if slug=='overlap':
   xx=np.linspace(-1.2,1.2,120);plot(a,xx,np.ones_like(xx),'position across gap',r'$B/(\mu_0 J d/2)$');a.set_ylim(0,2);return 'Field in the overlap gap is uniform and transverse to J'
  if slug=='force-current':
   th=np.linspace(0,np.pi,150);plot(a,th,np.sin(th),'angle wire to B (rad)',r'$F/(ILB)$');return 'Force peaks when wire is perpendicular to B and vanishes when parallel'
  if slug=='torque-loop':
   th=np.linspace(0,np.pi,150);plot(a,th,-np.cos(th),'theta (rad)','U / mu B','U / mu B');a.plot(th,np.sin(th),c=R,label='torque magnitude');leg(a);return 'Aligned loop sits at the energy minimum; torque vanishes there too'
  if slug=='wires-force':
   d=np.linspace(.2,3,120);plot(a,d,1/d,'separation / d0',r'$(F/L)/(F_0/L)$');return 'Force per length falls as 1/d: same currents, half distance, double force'
  if slug=='pressure':
   B=np.linspace(0,3,120);plot(a,B,B*B/(2*4e-7)/1e5,'B (T)','pressure (atm)');a.scatter([1,3],[4,36],c=R);return 'Magnetic pressure grows as B squared: 4 atm at 1 T, 36 atm at 3 T'
  if slug=='gyromagnetic':
   Rr=np.linspace(.2,2,120);plot(a,Rr,np.ones_like(Rr),'body radius (normalised)',r'$(\mu/L)/(Q/2m)$');a.set_ylim(0,2);return 'The gyromagnetic ratio Q/2m is independent of size and speed'
  if slug=='magnet-matter':
   bars(a,['plate N=1','sphere N=1/3','rod N=0'],[0,2/3,1],r'$B_{in}/(\mu_0 M)$');return 'Demagnetising factor sets the interior field of uniform magnetisation'
  if slug=='BHM':
   H=np.linspace(0,2,140);plot(a,H,H,'H / H0',r'$B/(\mu_0\mu_r H_0)$','linear medium');a.plot(H,2*(1-np.exp(-H)),c=R,label='iron, saturating');leg(a);return 'Linear media keep constant mu_r; iron bends towards saturation'
  if slug=='dia-para':
   xx=np.linspace(0,3,140);plot(a,xx,np.tanh(xx),'x = mu B / kT',r'$M/(n\mu)$','tanh alignment');a.plot(xx,xx,c=R,label='weak-field slope 1');a.set_ylim(0,3);leg(a);return 'Paramagnetic alignment: linear at small x, saturated at large x'
  if slug=='ferro':
   H=np.linspace(-2,2,300);B=1.2*np.tanh(1.3*H+.35);plot(a,H,B,'H (normalised)',r'$B$ (normalised)','branch with remanence');a.plot(H,1.2*np.tanh(1.3*H-.35),c=R,label='return branch');leg(a);return 'Hysteresis loop: remanence at H=0 and coercivity at B=0'
  if slug=='circuits':
   g=np.linspace(.01,1,120);plot(a,g,1/(g+.05),'gap width / ell',r'$B/(\mu_0 NI/\ell)$');return 'Gap-dominated circuit: B falls roughly as the inverse gap width'
  if slug=='earth':
   lam=np.linspace(0,np.pi/2,120);plot(a,lam,np.degrees(np.arctan(2*np.tan(lam))),'magnetic latitude (deg)','dip angle (deg)');return 'Dip angle grows from 0 at the equator to 90 at the pole'
  if slug=='relativity':
   v=np.linspace(.01,.3,120);plot(a,v,v*v,'v / c',r'$F_m/F_e$ at $v_1{=}v_2$');return 'Magnetic force is smaller than electric by v squared over c squared'
  if slug=='helmholtz':
   z=np.linspace(-1,1,160);b1=1/((1+(z-.5)**2)**1.5)+1/((1+(z+.5)**2)**1.5);b2=1/((1+(z-.8)**2)**1.5)+1/((1+(z+.8)**2)**1.5);plot(a,z,b1/b1.max(),'z / R',r'$B/B(0)$','spacing d = R');a.plot(z,b2/b2.max(),c=R,label='spacing d = 1.6 R');leg(a);return 'Only d = R flattens the midpoint; wider spacing gives a dip'
  if slug=='sphere':
   bars(a,['outside pole','inside','outside equator'],[2/3,2/3,-1/3],r'$B/(\mu_0 M)$');return 'Sphere field: uniform inside, dipole outside with a tangential jump'
  if slug=='pressure-apps':
   B=np.linspace(0,4,120);plot(a,B,B*B/(2*4e-7)/1e6,'B (T)','stress (MPa)');a.scatter([3,8.3],[3.58,27.4],c=R);return 'Hoop stress from B squared: 3.6 MPa at 3 T, 27 MPa at 8.3 T'
  if slug=='cycloid-fermi':
   t=np.linspace(0,2*np.pi,200);plot(a,t-np.sin(t),1-np.cos(t),'x / r_c','y / r_c','cycloid');a.plot(t-.5*np.sin(t),1-.5*np.cos(t),c=R,label='curtate');a.plot(t-1.5*np.sin(t),1-1.5*np.cos(t),c=I,label='prolate');a.set_ylim(-1.2,3);leg(a);return 'Wheel-point distance sets cycloid family: curtate, cusped or looping'
  if slug=='clocks':
   labs=['gyration 17 ms','bounce 2 s','drift 1300 s'];vals=[.017,2,1300];bars(a,labs,np.log10(vals),'log10 seconds');return 'Three clocks separated by two orders each make adiabatic invariants'
  if slug=='hall-levitation':
   x=np.linspace(.2,3,140);RH=(1-x**2)/(1+x)**2;plot(a,x,RH,'n mu_n^2 / p mu_p^2',r'$R_H$ (normalised)');a.axhline(0,c=I,lw=.8);a.axvline(1,c=R,ls='--');return 'Two-carrier Hall sign flips when n mu_n squared overtakes p mu_p squared'
  if slug=='estimates':
   lam=np.linspace(0,np.pi/2,120);plot(a,lam,np.sqrt(1+3*np.sin(lam)**2),'magnetic latitude (rad)',r'$B/B_{eq}$');return 'Dipole field strength grows from equator to pole by up to a factor two'
  raise KeyError(key)
 # First panel: labelled physical geometry.
 if slug=='lorentz':
  dot(a,0,0);arr(a,(0,0),(1.2,0),R);txt(a,1.3,0,'v',ha='center');into_page(a,0,1.1);arr(a,(0,0),(0,-1.15),T);txt(a,.25,-1,'F = q v x B',ha='center');txt(a,0,-1.35,'q > 0: thumb first, sign second',ha='center');return 'Right hand along v, curl to B, thumb gives force; flip for negative q'
 if slug=='circle':
  circ(a,0,0,1);dot(a,1,0);arr(a,(1,0),(1.35,.75),R);txt(a,1.55,.85,'v',ha='center');arr(a,(1,0),(0,0),T);txt(a,.42,-.12,'r = mv/qB');into_page(a,0,1.45);return 'Uniform B into page: force keeps turning v without changing speed'
 if slug=='selector':
  line(a,(-2,-1),(2,-1),lw=3);line(a,(-2,1),(2,1),lw=3);arr(a,(-2.6,0),(-2,0));txt(a,-1.6,1.25,'E up between plates');into_page(a,0,0);line(a,(-2.2,0),(2.4,0),color=R,lw=2);txt(a,2.5,0,'undeflected at v = E/B',ha='center');return 'Crossed E and B: one chosen speed passes straight through'
 if slug=='regions':
  line(a,(-1.2,-1.4),(-1.2,1.4),ls='--');line(a,(1.2,-1.4),(1.2,1.4),ls='--');txt(a,0,1.6,'field strip width d',ha='center');line(a,(-1.2,0),(0,0),color=R,lw=2);a.add_patch(Arc((0,1.1),2.2,2.2,theta1=200,theta2=250,ec=T,lw=2));arr(a,(0,1.1),(0,0));txt(a,.25,.5,'r');txt(a,-.2,-1.6,'centre lies on the perpendicular at entry',ha='center');return 'Three-region method: arc centred on the perpendicular to v at entry'
 if slug=='spectrometer':
  line(a,(-2.5,-.8),(-1.2,-.8),lw=2);txt(a,-1.9,-1.25,'accelerate V');a.add_patch(Arc((-1.2,0),1.6,1.6,theta1=-90,theta2=90,ec=T,lw=2));arr(a,(-.4,.1),(-.4,1.15),T);txt(a,.35,.6,'semicircle: r from V and B',ha='center');txt(a,-1.9,1.3,'detector at 2r',ha='center');return 'Spectrometer: acceleration then a semicircle onto a detector'
 if slug=='cyclotron':
  circ(a,-.6,0,1);circ(a,.6,0,1);line(a,(-.6,-1),(-.6,1),lw=2);line(a,(.6,-1),(.6,1),lw=2);txt(a,0,1.35,'gap: alternating V0',ha='center');a.add_patch(Arc((-.6,0),.6,.6,theta1=90,theta2=270,ec=R,lw=1.5));a.add_patch(Arc((.6,0),1,1,theta1=-90,theta2=90,ec=R,lw=1.5));txt(a,0,-1.3,'growing spiral, fixed period',ha='center');return 'Cyclotron dees: each gap crossing adds energy at fixed frequency'
 if slug=='mirror':
  for z,x0 in [(-1.2,.9),(.4,.75),(1.6,.5)]:
   for s in [-1,1]:line(a,(z,s*x0),(z+.9,s*x0*.55),color=T,lw=1)
  z=np.linspace(-1.5,.7,80);a.plot(z,.42*np.cos(2.2*z),c=R);a.plot(z,-.42*np.cos(2.2*z),c=R);txt(a,1.9,0,'throat',ha='center');txt(a,0,-1.35,'reflects at B = B0/sin^2(theta0)',ha='center');return 'Converging field lines squeeze the helix until it reflects'
 if slug=='hall':
  a.add_patch(Rectangle((-1.2,-.7),2.4,1.4,fc='#eff8f5',ec=T));arr(a,(-1.9,0),(-1.25,0),R);txt(a,-2.15,.25,'I',ha='center');into_page(a,0,1.15);arr(a,(-.2,.25),(-.2,.75),T);txt(a,.35,.85,'q v x B');txt(a,-1.05,-.35,'- - -',ha='center');txt(a,1.05,-.35,'+ + +',ha='center');txt(a,0,-1.35,'same edge, opposite voltage',ha='center');return 'Hall plate: carriers pile on one edge until q E_H balances q v B'
 if slug=='drifts':
  t=np.linspace(0,2*np.pi,160);a.plot(-1.8+(t-np.sin(t))*.33,-.6+(1-np.cos(t))*.42,c=R);line(a,(-2.2,-.6),(1.7,-.6),ls='--');arr(a,(1.75,-.6),(2.4,-.6),T);txt(a,2.45,-.85,'drift E/B',ha='center');circ(a,-.6,.22,.42);txt(a,0,-1.35,'wheel radius r_c: cusps at rest',ha='center');return 'Crossed fields from rest trace a cycloid carried at the drift speed'
 if slug=='tracks':
  line(a,(-2.4,0),(-.9,0),color=R,lw=2);a.add_patch(Arc((-.9,1.1),2.2,2.2,theta1=200,theta2=250,ec=T,lw=2));line(a,(.1,1.05),(2.3,1.05),color=R,lw=2);arr(a,(-.9,1.1),(-.9,0));txt(a,-.62,.5,'r = p/qB');txt(a,1.5,.7,'straight outside',ha='center');return 'Track curvature inside B measures momentum; tangents fix the entry'
 if slug=='biot':
  line(a,(-1.6,-.7),(-.9,-.45),color=R,lw=4);arr(a,(-1.25,-.58),(-1.05,-.2),R);txt(a,-1.15,-.05,'I dl',ha='center');dot(a,1.2,.5,I);txt(a,1.35,.62,'P');line(a,(-1.05,-.48),(1.2,.5),ls='--');txt(a,.1,.15,'r');arr(a,(1.2,.5),(1.2,1.35),T);txt(a,1.55,1.3,'dB',ha='center');return 'Biot-Savart element: dB is perpendicular to both I dl and r'
 if slug=='wire':
  line(a,(-1.8,-1.2),(-1.8,1.2),color=R,lw=3);dot(a,0,.6,I);txt(a,.15,.72,'P');line(a,(-1.8,.6),(0,.6),ls='--');txt(a,-.9,.72,'d');line(a,(-1.8,-1.2),(0,.6),ls='--');line(a,(-1.8,1.2),(0,.6),ls='--');txt(a,-1.35,-.15,r'$\beta$',ha='center');txt(a,-1.35,1.05,r'$\alpha$',ha='center');return 'Finite wire: field from the two end angles alpha and beta at P'
 if slug=='loop':
  a.add_patch(Arc((0,0),1.6,1.6,theta1=0,theta2=360,ec=T,lw=2));line(a,(-2.3,0),(2.6,0));txt(a,1.05,.85,'R');dot(a,2.1,0,I);txt(a,2.15,.2,'P(x)');arr(a,(.8,.8),(1.05,1.05),R);txt(a,1.25,1.15,'dB',ha='center');txt(a,0,-1.5,'transverse parts cancel; net field is axial',ha='center');return 'Loop axis: every element is at distance sqrt(R^2 + x^2) from P'
 if slug=='solenoid':
  for z in np.linspace(-1.8,1.8,9):
   circ(a,z,0,.28);arr(a,(z,.28),(z,.75),T)
  line(a,(-2.4,-1.1),(2.4,-1.1),ls='--');txt(a,0,1.35,'uniform B inside; about half at the end face',ha='center');txt(a,2.55,-.7,'n turns/m',ha='center');return 'Solenoid: stacked loops give a uniform interior field and zero outside ideal'
 if slug=='moment':
  a.add_patch(Arc((0,0),1.5,1.5,theta1=0,theta2=360,ec=T,lw=2));arr(a,(0,.75),(.35,1.05),R);txt(a,.55,1.15,'I',ha='center');arr(a,(0,0),(0,1.5),T);txt(a,.18,.75,'mu');txt(a,0,-1.45,'fingers along I: thumb is mu',ha='center');return 'Loop moment mu = N I A with the right-hand area vector'
 if slug=='ampere':
  line(a,(-2.2,0),(2.2,0),lw=3);txt(a,2.3,0,'I out');circ(a,0,0,1.05,ls='--');arr(a,(1.05,0),(.75,.35),T);txt(a,.35,.55,'path C');txt(a,0,-1.5,'loop direction sets the sign of enclosed current',ha='center');return 'Amperian loop around a wire: circulation counts threaded current'
 if slug=='ampere-apps':
  circ(a,0,0,1.15,ec=T);circ(a,0,0,.55,ec=R);txt(a,0,0,'J',ha='center');arr(a,(.55,0),(.9,0),T);txt(a,1.35,.15,'r inside');arr(a,(1.15,0),(1.8,0),T);txt(a,2.1,.15,'r outside');return 'Thick wire: enclosed fraction grows as r squared inside, full current outside'
 if slug=='overlap':
  circ(a,-.35,0,1.15,ec=T);circ(a,.35,0,1.15,ec=R);txt(a,-1.8,.9,'+J cylinder');txt(a,1.15,.9,'-J cylinder');txt(a,0,0,'gap d',ha='center');arr(a,(-.35,0),(.35,0),T);return 'Overlap trick: two opposite uniform cylinders leave a uniform-field gap'
 if slug=='force-current':
  a.add_patch(Arc((0,0),1.7,1.7,theta1=200,theta2=340,ec=T,lw=3));line(a,(-1.6,.58),(1.6,.58),ls='--');arr(a,(-1.6,.58),(1.6,.58),R);txt(a,0,.85,'chord I L',ha='center');arr(a,(0,-.85),(0,-1.5),T);txt(a,.25,-1.25,'F = I L x B',ha='center');into_page(a,2.3,0);return 'Curved wire in uniform B feels the force of its straight chord'
 if slug=='torque-loop':
  line(a,(-1,-.7),(1,-.7),lw=2);line(a,(-1,.7),(1,.7),lw=2);line(a,(-1,-.7),(-1,.7),lw=2);line(a,(1,-.7),(1,.7),lw=2);arr(a,(-1,.7),(-1,1.35),R);arr(a,(1,.7),(1,1.35),R);arr(a,(-1,-.7),(-1,-1.35),R);arr(a,(1,-.7),(1,-1.35),R);arr(a,(0,0),(2.1,0),T);txt(a,2.2,0,'B');txt(a,0,-1.65,'displaced forces: couple mu x B',ha='center');return 'Loop in uniform B: net force zero, torque turns the plane toward alignment'
 if slug=='wires-force':
  line(a,(-1,-1.1),(-1,1.1),lw=3);line(a,(1,-1.1),(1,1.1),lw=3);txt(a,-1,1.3,'I1 out',ha='center');txt(a,1,1.3,'I2 out',ha='center');arr(a,(-.85,0),(-.2,0),R);arr(a,(.85,0),(.2,0),R);txt(a,0,.3,'parallel currents attract',ha='center');txt(a,0,-1.5,'same direction: attraction; opposite: repulsion',ha='center');return 'Two parallel wires: each feels the field of the other only'
 if slug=='pressure':
  a.add_patch(Rectangle((-1.3,-.8),2.6,1.6,ec=T,fc='none'));txt(a,0,0,'B inside',ha='center')
  for yy in [-.6,0,.6]:arr(a,(-1.3,yy),(-2,yy),R);arr(a,(1.3,yy),(2,yy),R)
  txt(a,0,1.35,'windings pushed outward with B^2/2mu0',ha='center');txt(a,0,-1.35,'field lines pull the two halves together',ha='center');return 'Solenoid hoop stress: the field presses on the current that confines it'
 if slug=='gyromagnetic':
  a.add_patch(Arc((0,0),1.4,1.4,theta1=0,theta2=360,ec=T,lw=2));arr(a,(0,.7),(.4,1.1),R);txt(a,.55,1.2,'I',ha='center');arr(a,(0,0),(0,1.45),T);txt(a,.18,.7,'mu');txt(a,0,-1.5,'same mu/L = Q/2m for ring, disc and sphere',ha='center');return 'Rotating charge: moment and angular momentum share the ratio Q/2m'
 if slug=='magnet-matter':
  a.add_patch(Rectangle((-1.3,-.9),2.6,1.8,fc='#eff8f5',ec=T));txt(a,0,0,'M up',ha='center')
  for xx in np.linspace(-1,1,6):circ(a,xx,.55,.16,ec=R);circ(a,xx,-.55,.16,ec=R)
  arr(a,(1.55,0),(1.55,.9),T);txt(a,1.75,.5,'K_b',ha='center');txt(a,0,-1.45,'bulk cancels; rim current survives',ha='center');return 'Uniformly magnetised slab: surface bound current K_b = M cross n'
 if slug=='BHM':
  line(a,(-2.2,-1),(2.2,-1),lw=3);line(a,(-2.2,1),(2.2,1),lw=3)
  for xx in np.linspace(-1.8,1.8,8):circ(a,xx,0,.3,ec=T)
  arr(a,(-2.5,0),(-2.2,0),R);txt(a,-2.75,.2,'I');txt(a,0,1.45,'free current sets H; core scales B',ha='center');return 'Filled solenoid: free current fixes H while the material scales B'
 if slug=='dia-para':
  circ(a,0,0,.8);arr(a,(.8,0),(1.3,0),R);txt(a,1.45,0,'v');arr(a,(0,0),(0,1.15),T);txt(a,.2,1.2,'mu');into_page(a,-1.7,.6);txt(a,-1.7,-.2,'applied B',ha='center');txt(a,0,-1.5,'orbit shift opposes B: Larmor',ha='center');return 'Atomic orbit in applied B: frequency shifts by the Larmor amount'
 if slug=='ferro':
  H=np.linspace(-2,2,200);a.plot(H,1.2*np.tanh(1.3*H+.35),c=T);a.plot(H,1.2*np.tanh(1.3*H-.35),c=R);a.set(xlim=(-2,2),ylim=(-1.6,1.6));a.spines[['top','right']].set_visible(False);a.set_xlabel('H',fontsize=11);a.set_ylabel('B',fontsize=11);a.tick_params(labelsize=9);txt(a,0,1.25,'remanence',ha='center');txt(a,-.75,0,'coercivity');txt(a,1.55,-1.2,'loop area = loss/cycle',ha='center');return 'Domains wall motion leaves B lagging H: the hysteresis loop'
 if slug=='circuits':
  line(a,(-2,-1.2),(-2,1.2),lw=3);line(a,(-2,1.2),(.8,1.2),lw=3);line(a,(-2,-1.2),(.8,-1.2),lw=3);line(a,(1.2,1.2),(2,1.2),lw=3);line(a,(1.2,-1.2),(2,-1.2),lw=3);line(a,(2,1.2),(2,-1.2),lw=3);txt(a,1,.7,'gap g',ha='center');txt(a,-2.6,0,'N I',ha='center');txt(a,-.6,0,'iron core',ha='center');return 'Magnetic circuit: ampere-turns drive flux through iron and gap in series'
 if slug=='earth':
  circ(a,0,0,1.1);line(a,(-.35,-1.2),(.35,1.2),ls='--');arr(a,(0,0),(1.9,0),R);txt(a,2,0,'B_H');arr(a,(0,0),(1.2,-1.05),R);txt(a,1.35,-1.2,'B_V');arr(a,(1.2,-1.05),(1.9,0),T);txt(a,1.75,-.45,'dip');txt(a,0,1.55,'tilted dipole at the centre, about 11 degrees',ha='center');return 'Station field components: B_H horizontal, B_V vertical, dip their angle'
 if slug=='relativity':
  dot(a,-1.2,0,I);dot(a,1.2,0,I);arr(a,(-1.2,0),(-.2,0),R);arr(a,(1.2,0),(2.2,0),R);txt(a,-.55,.25,'v1');txt(a,1.95,.25,'v2');arr(a,(-1.2,0),(-1.2,1),T);txt(a,-.95,1.05,'E and B of 1 act on 2',ha='center');txt(a,0,-1.5,r'$F_m=F_e\,v_1v_2/c^2$',ha='center');return 'Two moving charges: the magnetic term is the relativistic residue'
 if slug=='helmholtz':
  circ(a,-1,0,1.15,ec=T);circ(a,1,0,1.15,ec=T);line(a,(-1,-1.15),(1,-1.15),ls='--');txt(a,0,-1.45,'d = R',ha='center');txt(a,0,1.55,'flat midpoint region between the coils',ha='center');arr(a,(-.35,0),(.35,0),R);txt(a,0,.25,'flat to (z/R)^4',ha='center');return 'Helmholtz spacing d = R cancels the quadratic term at the centre'
 if slug=='sphere':
  circ(a,0,0,1.15);arr(a,(0,-.5),(0,.5),R);txt(a,.2,0,'M')
  for th in np.linspace(.3,np.pi-.3,5):circ(a,1.15*np.cos(th),1.15*np.sin(th),.1,ec=T)
  txt(a,0,1.55,'K_b = M sin theta on the surface',ha='center');txt(a,0,-1.6,'inside B = 2/3 mu0 M uniform; dipole outside',ha='center');return 'Uniformly magnetised sphere: surface current of a rotating shell'
 if slug=='pressure-apps':
  circ(a,0,0,1.05);txt(a,0,0,'plasma\nI',ha='center')
  for th in np.linspace(.3,np.pi-.3,5):arr(a,(1.35*np.cos(th),1.35*np.sin(th)),(1.05*np.cos(th),1.05*np.sin(th)),R)
  txt(a,0,1.7,'pinch pressure compresses channel',ha='center');return 'Current channel pinched by its own magnetic pressure'
 if slug=='cycloid-fermi':
  circ(a,-.75,.45,.45);dot(a,-.75,0,I);arr(a,(-.3,.45),(.2,.45),T);txt(a,.35,.45,'vd',ha='center');t=np.linspace(0,2*np.pi,120);a.plot(-2.3+(t-np.sin(t))*.28,-.7+(1-np.cos(t))*.3,c=R);txt(a,1.35,-1.15,'wheel point traces the cycloid',ha='center');return 'Rolling wheel picture: the gyration centre drifts at E cross B over B squared'
 if slug=='clocks':
  z=np.linspace(-2.2,2.2,120);a.plot(z,.55*(1-(z/2.2)**2),c=T);a.plot(z,-.55*(1-(z/2.2)**2),c=T);a.plot(z,.12*np.cos(4*z),c=R);txt(a,0,1.15,'three clocks on one field line',ha='center');return 'One trapped particle keeps three clocks: gyration, bounce, drift'
 if slug=='hall-levitation':
  a.add_patch(Rectangle((-1.4,-1.2),2.8,.5,fc='#eff8f5',ec=T));a.add_patch(Rectangle((-.7,.7),1.4,.7,fc='#eff8f5',ec=R));txt(a,0,1.05,'magnet',ha='center');txt(a,0,-.95,'superconductor',ha='center');arr(a,(-.7,.55),(-.7,.15),T);arr(a,(.7,.55),(.7,.15),T);txt(a,0,.35,'image dipole repels',ha='center');return 'Levitation: a perfect diamagnet reflects the dipole into an opposite image'
 if slug=='estimates':
  circ(a,-1.2,0,.28);txt(a,-1.2,.5,'magnet',ha='center');circ(a,1.2,0,.28);txt(a,1.2,.5,'compass',ha='center');line(a,(-.92,0),(.92,0),ls='--');txt(a,0,-.35,'d');arr(a,(1.2,0),(1.75,.5),R);txt(a,1.95,.55,'theta');txt(a,0,-1.5,'oscillation: product; deflection: ratio',ha='center');return 'Absolute measurement: magnet oscillation plus compass deflection at distance d'
 raise KeyError(key)
