"""Precise native matplotlib diagrams; no generated mathematical text."""
import numpy as np
from matplotlib.patches import Circle,Rectangle,Arc,Polygon
INK='#153149'; TEAL='#087d7d'; RED='#a43232'
def arrow(ax,a,b,label=None,color=TEAL):
 ax.annotate('',xy=b,xytext=a,arrowprops=dict(arrowstyle='->',color=color,lw=1.6))
 if label: ax.text((a[0]+b[0])/2+.12,(a[1]+b[1])/2+.14,label,fontsize=11,color=color)
def line(ax,a,b,**kw):ax.plot([a[0],b[0]],[a[1],b[1]],c=INK,**kw)
def text(ax,x,y,s,**kw):ax.text(x,y,s,fontsize=11,**kw)
def plain(ax):ax.set(xlim=(0,10),ylim=(0,5));ax.axis('off');ax.set_aspect('equal')
def wheel(ax,c=(3,2.5),r=1.5):ax.add_patch(Circle(c,r,fill=False,ec=INK,lw=1.7));ax.plot(*c,'o',color=INK,ms=3)
def graph(ax,x,y,xlab,ylab):
 ax.plot(x,y,c=TEAL);ax.set_xlabel(xlab,fontsize=11);ax.set_ylabel(ylab,fontsize=11);ax.spines[['top','right']].set_visible(False);ax.tick_params(labelsize=10);ax.grid(alpha=.15)
def figure(ax,key):
 plain(ax)
 from extra_diagrams import KEYS,figure as extra_figure
 if key in KEYS:return extra_figure(ax,key)
 if key in ['velocity','acceleration']:
  wheel(ax)
  if key=='velocity':
   for r in [.75,1.5]:arrow(ax,(3+r,2.5),(3+r,2.5+r))
   text(ax,5.1,4.25,'rim: R omega');text(ax,5.1,3.25,'r=R/2: R omega/2')
   text(ax,.2,4.2,'Fixed C: v(C)=0');text(ax,5.5,1.2,'CCW omega: +z out')
  else:
   arrow(ax,(4.5,2.5),(3.2,2.5),'normal',RED);arrow(ax,(4.5,2.5),(4.5,4),'tangent');text(ax,5.3,.8,'a(n)=omega² R\na(t)=alpha R')
  return 'Fixed-axis rotation: tangent velocity and inward acceleration'
 if key=='inertia':
  for x,label in [(2,'ring: beta=1'),(7,'disc: beta=1/2')]:
   ax.add_patch(Circle((x,2.8),1.3,fc='none' if x==2 else '#eff8f5',ec=INK));ax.plot(x,2.8,'o',c=TEAL);text(ax,x,0.5,label,ha='center');text(ax,x,4.5,'normal axis out',ha='center')
  return 'Same M and R; different radial mass distributions'
 if key=='inertia_graph':
  ax.clear();r=np.linspace(0,1,200);graph(ax,r,r**4,'r / R','I inside r / I total');ax.set(xticks=[0,.5,1],yticks=[0,.5,1],xlim=(0,1),ylim=(0,1.05));return 'Uniform disc: enclosed inertia rises as (r/R)^4'
 if key=='axes':
  wheel(ax);ax.plot([3,4.5],[2.5,2.5],c=TEAL,ls='--');ax.plot(4.5,2.5,'o',c=RED);text(ax,2.5,2,'C');text(ax,4.6,2,'A');text(ax,3.6,2.8,'R');text(ax,5.5,3.7,'Both axes normal\nto disc plane');text(ax,5.5,1.3,'I(A)=3MR²/2');return 'Disc rim axis parallel to the central normal'
 if key=='lamina':
  ax.add_patch(Rectangle((2,1.2),5,2.5,fc='#eff8f5',ec=INK));arrow(ax,(4.5,2.4),(8.6,2.4),'x');arrow(ax,(4.5,2.4),(4.5,4.7),'y');text(ax,2.1,.4,'z: out of plane at the same O');text(ax,4.5,2,'O');return 'Three common-origin axes; x and y in a lamina'
 if key=='torque':
  line(ax,(2,1),(6,1));arrow(ax,(6,1),(6,4.5),'F');ax.plot(2,1,'o',c=INK);text(ax,1.3,.4,'O');text(ax,3.4,1.4,'d(perp)');text(ax,7,2.3,'tau(z)>0\nCCW');ax.plot([6,6],[.4,4.5],c=RED,ls=':');return 'Torque arm is perpendicular to the force line'
 if key=='pulley':
  wheel(ax,(5,3.6),.85);line(ax,(4.15,3.6),(4.15,1.4));line(ax,(5.85,3.6),(5.85,.9));
  for x,y,s in [(4.15,1.2,'m1'),(5.85,.7,'m2')]:ax.add_patch(Rectangle((x-.45,y-.3),.9,.6,fc='#eff8f5',ec=INK));text(ax,x,y,s,ha='center',va='center')
  text(ax,2.6,2.6,'T1');text(ax,6.1,2.6,'T2');arrow(ax,(7.8,3),(7.8,1),'a');text(ax,1,4.5,'m2 > m1');return 'Massive pulley: T2-T1 supplies the spin torque'
 if key=='momentum':
  ax.plot(2,1,'o',c=INK);text(ax,1.3,.6,'O');ax.plot(6,3,'o',c=TEAL);arrow(ax,(2,1),(6,3),'r(C)');arrow(ax,(6,3),(9,3),'M v(C)');text(ax,4,.4,'L(orbital,z)<0 here');return 'A translating mass can carry orbital angular momentum'
 if key=='disc_couple':
  for x in [2.5,7.5]:wheel(ax,(x,2.6),1.2)
  text(ax,2.5,4.2,'I1, omega1',ha='center');text(ax,7.5,4.2,'I2, omega2',ha='center');arrow(ax,(4,2.6),(6,2.6));text(ax,5,.5,'One common signed final omega',ha='center');return 'Coaxial coupling: conserve total axial L, dissipate KE'
 if key in ['rolling','contact_acc']:
  wheel(ax,(4,2.5));line(ax,(.7,1),(9.2,1));text(ax,3.7,.45,'P')
  if key=='rolling':
   arrow(ax,(4,2.5),(6,2.5),'v');arrow(ax,(4,4),(8,4),'2v');text(ax,7,1.3,'v(P)=0');text(ax,.2,4.5,'CW spin')
  else:arrow(ax,(4,1),(4,3),'a(P)=omega² R');text(ax,6,3.3,'v(P)=0\nbut a(P) is not zero')
  return 'Pure rolling on stationary straight ground'
 if key=='incline':
  t=np.pi/6;u=np.array([np.cos(t),-np.sin(t)]);n=np.array([np.sin(t),np.cos(t)]);c=np.array([4.5,3]);pt=c-1*n
  line(ax,pt-3*u,pt+4*u);wheel(ax,c,1);arrow(ax,c,c+1.6*u);arrow(ax,c,c-2*np.array([0,1]),color=RED);arrow(ax,c,c+1.6*n);arrow(ax,pt,pt-1.7*u);text(ax,6.5,1.9,'+down');text(ax,4.7,.7,'Mg',color=RED);text(ax,5.5,4.4,'N');text(ax,1.2,3.2,'f (uphill)');return 'Free rolling: static friction points up the incline'
 if key=='race':
  ax.clear();names=['solid sphere','solid cylinder','thin shell','hoop'];beta=np.array([.4,.5,2/3,1]);ax.barh(names[::-1],(1/(1+beta))[::-1],color=TEAL);ax.set_xlabel('a / (g sin theta)',fontsize=11);ax.tick_params(labelsize=10);ax.set_xlim(0,.8);return 'Rolling race: beta alone sets normalised acceleration'
 if key=='slip_graph':
  ax.clear();t=np.linspace(0,1.7,300);graph(ax,t,np.where(t<1,1-2*t/7,5/7),'t / t*','speed / v0');ax.plot(t,np.where(t<1,5*t/7,5/7),c=INK,ls='--',label='R omega / v0');ax.axvline(1,c=RED,ls=':');ax.text(.1,.9,'v / v0',fontsize=11);ax.legend(fontsize=10,loc='lower right');ax.set(ylim=(0,1.05),xlim=(0,1.7));return 'No-spin solid sphere: slopes change at t*'
 if key=='slip_loss':
  ax.clear();t=np.linspace(0,1.7,300);graph(ax,t,np.maximum(1-t,0),'t / t*','slip u / v0');ax.axvline(1,c=RED,ls=':');ax.fill_between(t,0,np.maximum(1-t,0),color='#fff2b8');text(ax,.05,.25,'Area gives heat / (mu M g v0 t*)');return 'Slip vanishes continuously; dissipative power then ceases'
 if key=='driven':
  wheel(ax,(3.5,2.5));line(ax,(.7,1),(9,1));arrow(ax,(3.5,4),(7.5,4),'F');arrow(ax,(3.5,1),(5.8,1),'f=F/3');text(ax,6,2.4,'Disc, no slip\na=4F/(3M)');return 'Top-pulled disc: friction is forward, not backward'
 if key=='spool':
  wheel(ax,(3.2,2.5));wheel(ax,(3.2,2.5),.65);line(ax,(.7,1),(9.3,1));phi=np.pi/6;pt=np.array([3.2,2.5])+.65*np.array([np.sin(phi),-np.cos(phi)]);arrow(ax,pt,pt+4*np.array([np.cos(phi),np.sin(phi)]));text(ax,5.5,.45,'Lower-hub tangent');text(ax,5.6,2.5,'phi=30° shown');text(ax,7.3,4.3,'F');text(ax,.5,4.6,'R outer, r hub');return 'Specified winding: hub torque from F is counterclockwise'
 if key=='yoyo':
  wheel(ax,(4,2.2),1.4);wheel(ax,(4,2.2),.5);line(ax,(3.5,2.2),(3.5,4.6));line(ax,(2.8,4.6),(4.2,4.6));arrow(ax,(4,2.2),(4,.3),color=RED);text(ax,4.3,.2,'Mg',color=RED);arrow(ax,(3.5,2.2),(3.5,3.9),'T');text(ax,6,3.6,'Fixed upper end');text(ax,6,1.2,'a downward\na=r alpha');return 'Yo-yo unwinds about hub radius r'
 if key=='yoyo_graph':
  ax.clear();x=np.linspace(0,1,200);graph(ax,x,2*x*x/(1+2*x*x),'r / R','a / g');ax.set(xticks=[0,.5,1],yticks=[0,1/3,2/3],yticklabels=['0','1/3','2/3'],ylim=(0,.72));return 'Solid-disc yo-yo: r/R→0 gives a→0'
 if key=='impact':
  line(ax,(5,4.5),(5,.5),lw=5);ax.plot(5,4.5,'o',c=RED);ax.plot(2,2,'o',c=TEAL);arrow(ax,(2,2),(4.7,2),'m, v');text(ax,5.4,3.4,'d');text(ax,5.5,4.4,'O hinge');text(ax,6.5,1,'Rod length l');return 'Bullet impact: take angular impulse about fixed hinge O'
 if key=='impact_loss':
  ax.clear();x=np.linspace(0,1,200);graph(ax,x,1/(1+3*.1*x*x),'d / l','Q / initial bullet KE');ax.set(ylim=(.7,1.03),xlim=(0,1));text(ax,.05,.75,'m/M = 0.1');return 'Embedding loss decreases with distance from the hinge'
 if key=='ladder':
  line(ax,(8,.5),(8,4.7));line(ax,(.5,.5),(9,.5));a=np.array([3.,.5]);b=np.array([8.,4.4]);line(ax,a,b,lw=3);arrow(ax,(a+b)/2,(5.5,.8),'Mg',RED);arrow(ax,a,a+[0,2],'Ng');arrow(ax,a,a+[2,0]);text(ax,4.8,.12,'f');arrow(ax,b,b+[-2,0],'Nw');text(ax,3.7,1.2,'theta');return 'Smooth wall, rough floor: four forces on the ladder'
 if key=='tipping':
  ax.add_patch(Rectangle((3,1),3,3,fill=False,ec=INK));line(ax,(1,1),(9,1));ax.plot(4.5,2.5,'o',c=TEAL);arrow(ax,(4.5,2.5),(6,1),'effective weight',RED);text(ax,6.2,.45,'edge');text(ax,3.3,.45,'2b');text(ax,2.2,2.3,'h');return 'Tip threshold: effective-weight line reaches a support edge'
 if key=='pendulum':
  o=np.array([4,4.5]);c=o+np.array([1.3,-2.7]);line(ax,o,c);wheel(ax,c,.75);ax.plot(*o,'o',c=RED);arrow(ax,c,c+[0,-1.6],'Mg');text(ax,3.5,4,'O');text(ax,4.1,2.9,'d');ax.plot([4,4],[.7,4.5],c=INK,ls=':');text(ax,4.2,3.8,'theta');text(ax,6.5,2.9,'Restoring torque:\n-Mgd sin(theta)');return 'Physical pendulum: measure theta from downward vertical'
 if key=='bowl':
  th=np.linspace(-np.pi/2,np.pi/2,200);ax.plot(5+3*np.sin(th),4-3*np.cos(th),c=INK);wheel(ax,(5+2.3*np.sin(.4),4-2.3*np.cos(.4)),.7);ax.plot(5,4,'o',c=RED);line(ax,(5,4),(5+2.3*np.sin(.4),4-2.3*np.cos(.4)),ls=':');text(ax,6.1,3.5,'q=R-r');text(ax,1,4.5,'Fixed circular track');return 'The roller centre follows a circle of radius R-r'
 if key=='rod':
  line(ax,(8,.6),(8,4.7));line(ax,(1,.6),(9,.6));line(ax,(3,.6),(8,4.3),lw=4);ax.plot(5.5,2.45,'o',c=TEAL);arrow(ax,(8,4.3),(6.3,4.3),'Nw');arrow(ax,(3,.6),(3,2.2),'Ng');arrow(ax,(5.5,2.45),(5.5,.9),'Mg',RED);text(ax,3.7,1.1,'theta');return 'Smooth wall and floor: bottom can slide horizontally'
 if key=='rod_graph':
  ax.clear();theta0=np.pi/3;t=np.linspace(0,theta0,250);y=.75*np.cos(t)*(3*np.sin(t)-2*np.sin(theta0));graph(ax,t*180/np.pi,y,'theta (degrees above floor)','Nw / (Mg)');star=np.arcsin(2*np.sin(theta0)/3)*180/np.pi;ax.axhline(0,c=INK,lw=.7);ax.axvline(star,c=RED,ls=':');ax.text(8,.2,'Invalid: wall would pull',fontsize=10);ax.set_xlim(0,60);return 'theta0=60°: detachment at 35.264° (motion right to left)'
 if key=='tensor':
  n=np.array([.6,.8]);c=np.array([4,2.5]);line(ax,c-2*n,c+2*n,lw=3);ax.plot([c[0]-2*n[0],c[0]+2*n[0]],[c[1]-2*n[1],c[1]+2*n[1]],'o',c=INK);arrow(ax,c,c+[0,2],'omega');v=np.array([0,1])-n*.8;arrow(ax,c,c+4*v,'L',RED);text(ax,6,1,'L dot n = 0');return 'Oblique dumbbell: subtract the component along the rod'
 if key=='moving_origin':
  ax.plot(2,1,'o',c=INK);ax.plot(7,3,'o',c=TEAL);text(ax,1.5,.5,'A');text(ax,7.35,2.75,'C');arrow(ax,(2,1),(4,1),'v(A)');arrow(ax,(7,3),(7,4.6),'v(C)');line(ax,(2,1),(7,3),ls='--');return 'Moving origins require the angular-momentum transport term'
 if key=='gyro':
  o=np.array([3.,.7]);n=np.array([.6,.8]);line(ax,o,o+4*n,lw=2);arrow(ax,o,o+4*n);text(ax,5.9,3.65,'L ≈ I3 omega3');c=o+2.3*n;arrow(ax,c,c+[0,-1.5],color=RED);text(ax,4.7,.45,'Mg',color=RED);ax.plot([3,3],[.7,4.8],c=INK,ls=':');text(ax,3.1,2,'theta');text(ax,3.25,4.35,'Vertical axis');text(ax,6.0,1.55,'tau: into sheet\nOmega: upward');return 'Gravity turns spin angular momentum around vertical'
 if key=='gyro_graph':
  ax.clear();w=np.linspace(2,10,200);graph(ax,w,1/w,'normalised spin rate','precession / reference');ax.set(ylim=(0,.6));ax.text(3,.45,'Fast-spin domain only',fontsize=11);return 'Inverse-spin trend: do not extrapolate to zero spin'
 if key=='stress':
  wheel(ax,(3,2.5));arrow(ax,(3,2.5),(4.5,2.5),'R');text(ax,5.5,3.8,'Free outer edge');text(ax,5.5,1.5,'Uniform thin disc\nMaximum stress at C');text(ax,1,4.5,'normal spin axis');return 'Elastic disc model: no bore, isotropic, plane stress'
 if key=='flywheel_graph':
  ax.clear();x=np.linspace(0,1,200);graph(ax,x,x*x,'rim speed / allowed rim speed','K / allowed K');ax.set(xlim=(0,1),ylim=(0,1.05),xticks=[0,.5,1],yticks=[0,.5,1]);return 'Both kinetic energy and elastic stress scale as spin squared'
 if key=='carpet':
  wheel(ax,(3,2.8),1.5);line(ax,(.7,1.3),(9,1.3));line(ax,(3,1.35),(9,1.35),lw=3);text(ax,5.3,3.5,'Remaining roll m(R)');text(ax,5.3,2.2,'Deposited carpet');arrow(ax,(3,2.8),(4.5,2.8),'R');text(ax,1,.4,'Mass crosses the rolled-part boundary');return 'Open rolling subsystem: deposition needs a physical law'
 if key=='peg':
  line(ax,(2,3.7),(8,1.5),lw=4);ax.plot(5,2.6,'o',c=RED);text(ax,5.1,3,'Peg P');arrow(ax,(4,3),(4,1.2));text(ax,2.2,2.5,'v(C)');text(ax,1,4.5,'Is contact captured or unilateral?');text(ax,1,.5,'Geometry + impulse rule\n+ later contact test');return 'Peg impact is not automatically a new permanent hinge'
 raise ValueError(key)
