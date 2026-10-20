"""Additional exact-geometry diagrams for dense JEE MOI/impulse revision."""
import numpy as np
from matplotlib.patches import Circle,Rectangle,Wedge,Ellipse
from diagrams import line,arrow,text,graph,INK,TEAL,RED
KEYS={'rod_axes','plate_axes','circular_axes','semicircle','cylinder_axes','sphere_slice','disc_hole','density_graph','eccentric_impulse','percussion','falling_rod','rolling_loop'}
def figure(ax,key):
 if key=='rod_axes':
  line(ax,(1.5,2.5),(8.5,2.5),lw=4)
  for x,label in [(1.5,'end axis'),(5,'C axis')]:
   ax.plot([x,x],[.8,4.3],c=TEAL,ls='--');text(ax,x-.7,4.55,label)
  text(ax,4.7,1.7,'C');text(ax,5.5,.5,'rod length l');text(ax,6,3.2,'d=l/2 to end');return 'Rod: both marked axes are perpendicular to its length'
 if key=='plate_axes':
  ax.add_patch(Rectangle((2,1.1),5,2.5,fc='#eff8f5',ec=INK));arrow(ax,(4.5,2.35),(8.7,2.35),'x');arrow(ax,(4.5,2.35),(4.5,4.55),'y');ax.plot(4.5,2.35,'o',c=RED);text(ax,7.3,3.4,'b');text(ax,3.1,.5,'a');text(ax,5.2,1.5,'z out at C');return 'Rectangle axes: a along x; b along y; z normal'
 if key=='circular_axes':
  for x,fill in [(2.4,'none'),(7.4,'#eff8f5')]:
   ax.add_patch(Circle((x,2.6),1.35,fc=fill,ec=INK));ax.plot(x,2.6,'o',c=TEAL);ax.plot([x-1.35,x+1.35],[2.6,2.6],c=INK,ls='--');line(ax,(x-1.7,3.95),(x+1.7,3.95))
  text(ax,1,4.5,'in-plane tangent');text(ax,6.3,4.5,'in-plane tangent');text(ax,1,.4,'ring, z out at O');text(ax,6,.4,'disc, z out at O');return 'Diameter dashed; tangent solid; normal axis shown by a dot'
 if key=='semicircle':
  ax.add_patch(Wedge((3,1.1),2.8,0,180,fc='#eff8f5',ec=INK));line(ax,(.2,1.1),(5.8,1.1));line(ax,(3,1.1),(3,4.3),ls='--');ax.plot(3,1.1,'o',c=INK);cy=1.1+4*2.8/(3*np.pi);ax.plot(3,cy,'o',c=RED);text(ax,3.25,.5,'O');text(ax,3.25,cy,'C');text(ax,6,3,'disc: OC=4R/(3 pi)');text(ax,6,1.8,'wire: OC=2R/pi');return 'Half-disc and half-wire: their COMs are not at O'
 if key=='cylinder_axes':
  line(ax,(2,1.5),(7,1.5));line(ax,(2,3.5),(7,3.5));
  for x in [2,7]:ax.add_patch(Ellipse((x,2.5),.8,2,fill=False,ec=INK))
  ax.plot([.6,8.5],[2.5,2.5],c=TEAL,ls='--');ax.plot([4.5,4.5],[.5,4.5],c=RED,ls='--');text(ax,5.2,4.2,'transverse');text(ax,7.6,2.8,'axial');text(ax,3.3,.6,'length l');text(ax,.6,3.5,'R');return 'Cylinder: distinguish central longitudinal and transverse axes'
 if key=='sphere_slice':
  ax.add_patch(Circle((3,2.5),1.9,fill=False,ec=INK));x=.7;h=np.sqrt(1.9**2-x*x);ax.add_patch(Rectangle((3+x-.08,2.5-h),.16,2*h,fc='#b6ded6',ec=TEAL));arrow(ax,(.5,2.5),(6,2.5));text(ax,5.5,2.7,'x');text(ax,6.3,3.8,'s²=R²-x²');text(ax,6.3,1.9,'slice is a disc');text(ax,3.95,4.4,'s');return 'Sphere sliced normal to a diameter: dI = dm s² / 2'
 if key=='disc_hole':
  o=np.array([3.,2.5]);R=1.8;a=.65;d=1.05;mh=a*a/(R*R);xc=-mh*d/(1-mh)
  ax.add_patch(Circle(o,R,fc='#eff8f5',ec=INK));ax.add_patch(Circle(o+[d,0],a,fc='white',ec=RED));ax.plot(*o,'o',c=INK);ax.plot(o[0]+xc,o[1],'o',c=TEAL);text(ax,2.4,2,'C');text(ax,3.1,2.8,'O');text(ax,4.1,2.5,'hole',ha='center',va='center');text(ax,6,3.7,'same material density');text(ax,6,1.8,'C shifts away\nfrom the hole');return 'Off-centre hole: subtract mass AND its shifted inertia'
 if key=='density_graph':
  ax.clear();n=np.linspace(-1.9,12,300);graph(ax,n,(n+2)/(n+4),'density exponent n','I(z) / (MR²)');ax.axhline(1,c=RED,ls=':');ax.scatter([0],[.5],c=INK);ax.set(xlim=(-2,12),ylim=(0,1.07));ax.text(1,.35,'uniform disc: n=0',fontsize=11);return 'Radial density r^n: more rim weighting increases axial MOI'
 if key=='eccentric_impulse':
  line(ax,(5,.7),(5,4.3),lw=4);ax.plot(5,2.5,'o',c=TEAL);text(ax,5.3,2.5,'C');arrow(ax,(1,3.8),(4.7,3.8),'J');ax.plot([6.5,6.5],[2.5,3.8],c=RED);text(ax,6.8,3,'b');arrow(ax,(5,2.5),(8,2.5),'V(C)');text(ax,1.3,.4,'smooth support: no horizontal impulse');return 'Impulse above C: translation right and clockwise spin'
 if key=='percussion':
  line(ax,(4,4.4),(4,.6),lw=4);ax.plot(4,4.4,'o',c=RED);text(ax,4.4,4.4,'O hinge');ax.plot(4,2.5,'o',c=TEAL);text(ax,4.4,2.5,'C: d=l/2');y=4.4-3.8*2/3;arrow(ax,(.8,y),(3.7,y),'J');text(ax,5.3,1,'b=2l/3\nfor zero hinge impulse');return 'Uniform end-hinged rod: centre of percussion at 2l/3'
 if key=='falling_rod':
  o=np.array([2.,4.2]);end=o+np.array([6.,-3.]);line(ax,o,end,lw=4);ax.plot(*o,'o',c=RED);ax.plot([2,8],[4.2,4.2],c=INK,ls='--');c=(o+end)/2;arrow(ax,c,c+[0,-1.8],color=RED);text(ax,c[0]+.2,.7,'Mg');text(ax,2.1,4.6,'fixed O');text(ax,3.3,3.9,'theta');text(ax,7,2.8,'length l');return 'Hinged rod falls through theta below its initial horizontal'
 if key=='rolling_loop':
  o=np.array([4.,2.5]);R=2.;r=.4;q=R-r;ax.add_patch(Circle(o,R,fill=False,ec=INK));c=o+[0,q];ax.add_patch(Circle(c,r,fc='#eff8f5',ec=TEAL));ax.plot(*o,'o',c=INK);line(ax,o,c,ls='--');text(ax,4.2,3,'q=R-r');arrow(ax,c,c+[0,-1.5],color=RED);text(ax,6.7,4.3,'N, Mg: inward');text(ax,6.7,3,'at top:\nv² >= gq');text(ax,6.7,1.5,'check friction\nelsewhere too');return 'Inside loop: the COM follows radius R-r, not R'
 raise ValueError(key)
