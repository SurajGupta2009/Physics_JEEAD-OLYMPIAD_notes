"""Native analytical diagrams, not generated pictures of mathematical text.
Graphs autoscale separately from schematics; lengths and curves follow stated models.
"""
import numpy as np
from matplotlib.patches import Rectangle,Circle
I='#153149';T='#087d7d';R='#a43232';Y='#fff2b8'
def txt(ax,x,y,s,**kw):ax.text(x,y,s,fontsize=11,color=I,**kw)
def arrow(ax,a,b,c=T):ax.annotate('',xy=b,xytext=a,arrowprops=dict(arrowstyle='->',color=c,lw=1.6))
def box(ax,x,y,w,h,s):
 ax.add_patch(Rectangle((x,y),w,h,ec=T,fc='#eff8f5',lw=1.6));txt(ax,x+w/2,y+h/2,s,ha='center',va='center')
def plain(ax):ax.axis('off');ax.set(xlim=(0,10),ylim=(0,5))
def graph(ax,x,y,xlab,ylab,label=None):
 ax.axis('on');ax.autoscale(enable=True);ax.plot(x,y,c=T,label=label);ax.set_xlabel(xlab,fontsize=11);ax.set_ylabel(ylab,fontsize=11);ax.spines[['top','right']].set_visible(False);ax.tick_params(labelsize=9);ax.grid(alpha=.13)
def legend(ax,**kw):ax.legend(fontsize=9,frameon=False,**kw)
def bars(ax,labels,values,ylab,colors=None):
 ax.axis('on');ax.autoscale(enable=True);ax.bar(labels,values,color=colors or [T,I,R,T]);ax.set_ylabel(ylab,fontsize=11);ax.spines[['top','right']].set_visible(False);ax.tick_params(labelsize=10)
def coexistence(tr=.88):
 def roots(p):return sorted(float(z.real) for z in np.roots([3*p,-p-8*tr,9,-3]) if abs(z.imag)<1e-8 and z.real>1/3)
 def area(p):
  rs=roots(p)
  if len(rs)!=3:return None
  a,b=rs[0],rs[-1];return (8*tr/3)*np.log((3*b-1)/(3*a-1))+3/b-3/a-p*(b-a)
 last=None;bracket=None
 for pp in np.linspace(.1,.95,2000):
  ar=area(pp)
  if ar is not None:
   if last and last[1]*ar<0:bracket=(last[0],pp);break
   last=(pp,ar)
 assert bracket
 lo,hi=bracket
 for _ in range(45):
  mid=(lo+hi)/2
  if area(lo)*area(mid)<=0:hi=mid
  else:lo=mid
 sat=(lo+hi)/2;rs=roots(sat);return rs[0],rs[-1],sat

def figure(ax,key):
 if key=='thermometer':
  x=np.linspace(250,400);graph(ax,x,x/300,'T (K)','P / P(300 K)');ax.scatter([273.15,373.15],np.array([273.15,373.15])/300,c=R);return 'Fixed-volume ideal gas: P is linear in absolute T'
 if key=='heating':
  graph(ax,[0,2.1,35.5,77.3,302.9,304.9],[-10,0,0,100,100,110],'Q supplied (kJ)','T (Celsius)');ax.set_yticks([0,100]);return '0.10 kg water: ice, melt, liquid, boil, steam at 1 atm'
 if key=='pressure-density':
  x=np.linspace(0,3);graph(ax,x,x,'rho / rho0','P / P0','T0');ax.plot(x,2*x,c=R,label='2T0');legend(ax);return 'Same composition: ideal P = rho RT/M'
 if key in ['maxwell','beam']:
  x=np.linspace(0,4,300);graph(ax,x,4/np.sqrt(np.pi)*x*x*np.exp(-x*x),'v / vp(T0)','normalised density','bulk T0')
  if key=='maxwell':ax.plot(x,4/np.sqrt(np.pi)*x*x/2**1.5*np.exp(-x*x/2),c=R,label='bulk 2T0')
  else:ax.plot(x,2*x**3*np.exp(-x*x),c=R,label='effusive beam')
  legend(ax);return 'Equal probability area; higher T broadens the speed curve' if key=='maxwell' else 'Beam distribution is weighted by v: more fast particles'
 if key=='mfp':
  x=np.linspace(.3,3);graph(ax,x,x,'T / T0','lambda / lambda0','fixed P');ax.plot(x,np.ones_like(x),c=R,label='fixed number density');legend(ax);return 'Hard-sphere mean free path depends on number density'
 if key=='dof':bars(ax,['mono','linear\nrigid','nonlinear\nrigid'],[1.5,2.5,3],'CV / R');return 'Active translations and rotations; vibration excluded in these bars'
 if key=='heat-capacity':bars(ax,['isochore','isobar'],[2.5,3.5],r'$Q/(nR\Delta T)$',[T,R]);return 'Rigid diatomic: extra heat at fixed P supplies expansion work'
 if key=='compression':bars(ax,['iso-T\nreversible','adiabatic\nreversible','sudden\ninsulated'],[3.458,3.985,8.314],'work input (kJ)');return '2 mol rigid diatomic, 300 K, compressed to half-volume'
 if key=='reservoirs':
  bars(ax,['hot 400 K','cold 300 K','total'],[-3,4,1],'delta S (J/K)',[R,T,I]);ax.axhline(0,c=I,lw=.8);return '1200 J conducted hot to cold: entropy grows by 1 J/K'
 if key=='finite-engine':
  bars(ax,['cold\nstart','rev.\nfinal','contact\nfinal','hot\nstart'],[293.15,np.sqrt(373.15*293.15),333.15,373.15],'T (K)');ax.set_ylim(280,385);return 'Equal capacities: geometric versus arithmetic mean'
 if key=='availability':bars(ax,['total W','ambient W','useful B'],[5.369,1.008,4.361],'energy (MJ)');return '200 atm, 50 L, ambient T: useful work excludes P0 displacement'
 if key=='processes':
  graph(ax,[1,1],[1,2.8],'V / V0','P / P0','isochore');ax.plot([1,2.8],[1,1],c=R,label='isobar');ax.set(xlim=(.5,3),ylim=(.5,3));legend(ax);return 'Same initial state: vertical fixed V, horizontal fixed P'
 if key=='iso-adiabat':
  v=np.linspace(1,3);graph(ax,v,1/v,'V / V1','P / P1','isotherm');ax.plot(v,v**(-5/3),c=R,label='adiabat, gamma=5/3');legend(ax);return 'Expanding adiabat from a common start lies below isotherm'
 if key=='adiabat-laws':
  v=np.linspace(1,3);graph(ax,v,v**(-.4),'V / V1','T / T1');return 'Reversible ideal-gas adiabat, gamma=1.4: T V^0.4 constant'
 if key=='polytropes':
  v=np.linspace(.8,2.2);graph(ax,v,np.ones_like(v),'V / V0','P / P0','s=0')
  for s,c in [(1,I),(1.2,'#967700'),(1.4,R),(2,'#7b6a96')]:ax.plot(v,v**(-s),c=c,label=f's={s}')
  ax.set_ylim(0,2);ax.legend(fontsize=8,ncol=2,frameon=False,loc='upper right');return 'PV^s constant: every curve passes through the reference state'
 if key=='linear-path':
  v=np.linspace(1,3);graph(ax,v,4-v,'V / V0','P / P0');ax.fill_between(v,0,4-v,color=Y);ax.plot(2,2,'o',c=R);ax.annotate('T maximum',xy=(2,2),xytext=(1.4,3),fontsize=10,arrowprops=dict(arrowstyle='->'));return 'P/P0=4-V/V0: maximum T at V=2V0 on this segment'
 if key=='spring':
  v=np.linspace(0,2);graph(ax,v,1+v,'displacement x / x0','P / P*');ax.fill_between(v,0,1+v,color=Y);return 'Spring-loaded piston: straight P-V line; shaded work area'
 if key=='triangle':
  graph(ax,[6,6,12,6],[150,300,300,150],'V (L)','P (kPa)');ax.fill([6,6,12],[150,300,300],color=Y);arrow(ax,(8,300),(10,300),R);ax.set(xlim=(4,14),ylim=(100,350));return 'Clockwise triangle: +450 J net work; reverse gives -450 J'
 if key=='cycle-ledger':
  v=np.linspace(1,2);graph(ax,[1,1],[1,2],'V / V0','P / P0');ax.plot(v,2/v,c=R);ax.plot([2,1],[1,1],c=T);ax.set(xlim=(.7,2.3),ylim=(.7,2.4));ax.annotate('B to C: T=2T0',xy=(1.6,1.25),xytext=(1.15,2.1),fontsize=9,arrowprops=dict(arrowstyle='->'));return 'Isochore, isotherm, isobar: rigid diatomic eta=9.94%'
 if key=='carnot-ts':
  graph(ax,[1,3,3,1,1],[2,2,1,1,2],'S (scaled)','T (scaled)');ax.fill([1,3,3,1],[2,2,1,1],color=Y);arrow(ax,(1.4,2),(2.6,2),R);ax.set(xlim=(.5,3.5),ylim=(.6,2.4));return 'Carnot T-S rectangle: isotherms horizontal, adiabats vertical'
 if key=='otto':
  v=np.linspace(1,8);graph(ax,v,v**(-1.4),'V / Vmin','P (scaled)');ax.plot(v,2*v**(-1.4),c=R);ax.plot([1,1],[1,2],c=T);ax.plot([8,8],[8**(-1.4),2*8**(-1.4)],c=T);return 'Otto: two adiabats, two fixed-volume heat-transfer legs'
 if key=='stirling':
  v=np.linspace(1,3);graph(ax,v,2/v,'V / Vmin','P (scaled)','hot isotherm');ax.plot(v,1/v,c=R,label='cold isotherm');ax.plot([1,1],[1,2],c=I);ax.plot([3,3],[1/3,2/3],c=I);legend(ax);return 'Stirling: two isotherms joined by regenerative isochores'
 if key=='entropy-path':
  graph(ax,[1,1,2.6],[1,2,2],'S (scaled)','T (scaled)');ax.plot([1,2.6],[1,2],c=R,ls='--');ax.set(xlim=(.6,3),ylim=(.5,2.5));return 'Different reversible comparison routes, same endpoint delta S'
 if key=='entropy-free':
  v=np.linspace(1,4);graph(ax,v,np.log(v),'V2 / V1',r'$\Delta S/(nR)$');return 'Ideal insulated free expansion: Q=0, positive delta S'
 if key=='radiation':
  x=np.linspace(.5,2);graph(ax,x,x**4-1,'T / T0',r'$P_{net}/(\epsilon\sigma AT_0^4)$');ax.axhline(0,c=I,lw=.8);return 'Net grey-body radiation changes sign at T=T0'
 if key=='cooling':
  t=np.linspace(0,4);graph(ax,t,np.exp(-t),'t / tau',r'$\Delta T/\Delta T_i$');return 'Newton cooling: temperature excess decays exponentially'
 if key=='cooling-log':
  t=np.linspace(0,4);graph(ax,t,-t,'t / tau',r'$\ln(\Delta T/\Delta T_i)$');return 'Straight log-excess plot tests a constant-coefficient model'
 if key=='gas-spring':
  v=np.linspace(.75,1.3);graph(ax,v,1/v,'V / V0','P / P0','isothermal');ax.plot(v,v**(-1.4),c=R,label='adiabatic');legend(ax);return 'Near equilibrium, adiabatic stiffness is gamma times larger'
 if key=='counting':
  import math
  k=np.arange(21);graph(ax,k,np.array([math.comb(20,int(i))/2**20 for i in k]),'number on left (N=20)','probability');return 'Binomial multiplicity peaks near half, not all-left'
 if key=='mode-capacity':
  t=np.linspace(.05,3,250);x=1/t;graph(ax,t,x*x*np.exp(-x)/(1-np.exp(-x))**2,'T / vibrational theta','CV,vibration / R');return 'One harmonic vibration: capacity rises from zero towards R'
 if key=='escape-tail':
  x=np.linspace(0,10);graph(ax,x,(1+x)*np.exp(-x),'Jeans parameter Lambda',r'$\Gamma_J/(\nu\bar v/4)$');ax.set_yscale('log');return 'Jeans flux is exponentially sensitive to mass and temperature'
 if key=='atmosphere':
  z=np.linspace(0,20);graph(ax,z,np.exp(-z/8.4),'height z (km)','P / P0');return 'Isothermal atmosphere: exponential pressure, scale height 8.4 km'
 if key=='lapse':
  z=np.linspace(0,10);graph(ax,z,288-9.8*z,'height z (km)','T (K)','dry 9.8 K/km');ax.plot(z,288-6*z,c=R,label='illustrative moist 6 K/km');legend(ax);return 'Same base T: latent heat makes moist cooling gentler'
 if key in ['vdw','critical']:
  v=np.linspace(.37 if key=='vdw' else .5,5 if key=='vdw' else 3,600);tr=.88 if key=='vdw' else 1
  graph(ax,v,8*tr/(3*v-1)-3/v**2,'v / vc','P / Pc');ax.set_ylim(-.1 if key=='vdw' else 0,2)
  if key=='vdw':
   a,b,sat=coexistence(tr);ax.plot([a,b],[sat,sat],c=R,ls='--');return 'Subcritical vdW: dashed coexistence line solves equal areas'
  ax.plot(1,1,'o',c=R);return 'Critical isotherm: horizontal inflection at v/vc=P/Pc=1'
 if key=='inversion':
  x=np.linspace(.4,3);graph(ax,x,2/x-1,'RTb / a','CP muJT / b');ax.axhline(0,c=I,lw=.8);return 'Dilute vdW: positive muJT cools on pressure reduction'
 if key=='photon':
  v=np.linspace(1,5);graph(ax,v,v**(-1/3),'V / Vi','T / Ti');return 'Reversible photon expansion: T V^(1/3) stays constant'
 if key=='albedo':
  a=np.linspace(0,.8);graph(ax,a,(1361*(1-a)/(4*5.67e-8))**.25,'albedo','effective T (K)');return 'Black-body planet: more reflection gives lower effective T'
 if key=='blowdown':
  pp=np.geomspace(1/200,1);graph(ax,pp,pp**(2/7),'P / Pi','T / Ti');ax.set_xscale('log');return 'Ideal insulated tank: T/Ti=(P/Pi)^(2/7), gamma=1.4'
 plain(ax)
 if key=='equilibrium':
  for x,s in [(.3,'A'),(4,'C'),(7.7,'B')]:box(ax,x,2,2,1.2,s+'\nT = T*')
  arrow(ax,(2.4,2.6),(3.8,2.6));arrow(ax,(6.1,2.6),(7.5,2.6));txt(ax,5,4.1,'C is the common thermometer',ha='center');txt(ax,5,.6,'Diathermal contacts; zero net heat at equilibrium',ha='center');return 'Zeroth law: compare A and B through thermometer C'
 if key=='hole':
  ax.set_aspect('equal')
  for x,scale,s in [(2,1,'before'),(7,1.25,'heated')]:
   w,h,r=3*scale,2.6*scale,.65*scale
   ax.add_patch(Rectangle((x-w/2,2.5-h/2),w,h,ec=I,fc='#eff8f5'));ax.add_patch(Circle((x,2.5),r,ec=T,fc='white',lw=2));arrow(ax,(x,2.5),(x+r,2.5));txt(ax,x,.4,s,ha='center')
  txt(ax,5,4.4,'Every length expands by the same factor',ha='center');return 'The hole expands as if filled with the same material'
 if key=='bimetal':
  ax.set_aspect('equal');th=np.linspace(.25,1.2,100)
  for rad,c in [(3.2,R),(2.8,T)]:ax.plot(1+rad*np.sin(th),3.8-rad*np.cos(th),c=c,lw=5)
  txt(ax,5.3,3.8,'Higher alpha:\nlonger OUTER arc');txt(ax,5.3,1.3,'Lower alpha:\nshorter INNER arc');arrow(ax,(5.2,3.4),(3.404,1.688));arrow(ax,(5.2,1),(3.104,1.952));return 'Heated bonded layers bend; arcs have a common centre'
 if key=='mixing':
  box(ax,.4,1.3,2.5,2,'hot\nC1, T1');box(ax,7.1,1.3,2.5,2,'cold\nC2, T2');arrow(ax,(3.2,2.3),(6.8,2.3));txt(ax,5,3.7,'Heat flows hot to cold',ha='center');txt(ax,5,.3,'Insulated composite; final common Tf',ha='center');return 'Energy lost by hot material is gained by cold material'
 if key=='collision':
  ax.plot([7,7],[.4,4.5],c=I,lw=4);arrow(ax,(2,3.5),(6.7,3.5));arrow(ax,(6.7,1.6),(2,1.6));txt(ax,3,3.9,'incoming +m vx');txt(ax,3,.7,'outgoing -m vx');txt(ax,7.3,2.5,'wall');return 'Elastic wall hit transfers normal momentum 2m|vx|'
 if key=='mixture-capacity':
  box(ax,.3,1.7,3,1.7,'1 mol Ar\nCV,total = 1.5 R');box(ax,6.5,1.7,3.2,1.7,'1 mol O2\nCV,total = 2.5 R');txt(ax,4.9,2.5,'+',ha='center');txt(ax,5,.6,'Total CV=4R; total CP=6R; gamma=1.50',ha='center');return 'Sum extensive capacities before forming their ratio'
 if key=='piston':
  ax.plot([2,2,6,6],[4.3,.7,.7,4.3],c=I);ax.add_patch(Rectangle((2,2.6),4,.3,fc=I));txt(ax,4,1.5,'gas P, V, T',ha='center');arrow(ax,(4,3),(4,4.5));txt(ax,2.6,4.15,'P A');arrow(ax,(5.2,4.6),(5.2,3.2),R);txt(ax,6.1,3.7,'load + atm');arrow(ax,(.4,1.6),(1.8,1.6));txt(ax,.5,2.2,'Q in');return 'Quasistatic piston: upward gas force balances external load'
 if key=='boundary':
  box(ax,2,.8,6,3.5,'Closed system\nU stored');arrow(ax,(.2,3.3),(1.8,3.3));txt(ax,.2,3.8,'Q in');arrow(ax,(8.1,2),(9.8,2));txt(ax,8.1,2.7,'W out');txt(ax,5,.1,'delta U = Q - W',ha='center');return 'Heat and work cross the boundary; U belongs to the state'
 if key=='poly-signs':
  txt(ax,.3,4.2,'EXPANSION; gamma = 1.4')
  for y,a,b in [(3.2,'s < 1','T rises, Q in'),(2.3,'1 < s < 1.4','T falls, Q in'),(1.4,'s = 1.4','Q = 0'),(.5,'s > 1.4','T falls, Q out')]:txt(ax,.5,y,a);txt(ax,5,y,b)
  return 'Negative path capacity does not mean negative material CV'
 if key=='free-expansion':
  ax.add_patch(Rectangle((.7,.9),8.6,3.1,ec=I,fc='none',lw=2));ax.plot([5,5],[.9,4],c=R,ls='--');txt(ax,2.8,2.6,'gas\nV1, T1',ha='center');txt(ax,7.2,2.6,'vacuum',ha='center');arrow(ax,(4,1.5),(6.5,1.5));txt(ax,5,.2,'Rigid insulated outer wall: Q=0, W=0',ha='center');return 'Partition removed; gas irreversibly fills a larger volume'
 if key in ['engine','fridge']:
  box(ax,.4,3.4,2.8,1,'hot bath Th');box(ax,.4,.3,2.8,1,'cold bath Tc');box(ax,5,1.7,2,1.5,'device')
  if key=='engine':arrow(ax,(3.3,3.8),(5,2.8));arrow(ax,(5,2),(3.3,.9));arrow(ax,(7.1,2.5),(9.5,2.5));txt(ax,8,3,'W out')
  else:arrow(ax,(3.3,.9),(5,2));arrow(ax,(5,2.8),(3.3,3.8));arrow(ax,(9.5,2.5),(7.1,2.5));txt(ax,8,3,'W in')
  txt(ax,3.6,3.7,'Qh');txt(ax,3.6,.5,'Qc');return 'Engine: hot-side heat in, work out, remaining heat to cold' if key=='engine' else 'Fridge or pump: same flows, different useful heat output'
 if key=='cascade':
  box(ax,.1,3.5,2.5,1,'600 K source');box(ax,3.7,3.5,2.5,1,'350 K house');box(ax,7.3,3.5,2.5,1,'300 K outside');box(ax,.4,1,2,1.2,'engine');box(ax,4,1,2,1.2,'pump');arrow(ax,(2.6,1.6),(3.8,1.6));txt(ax,3.1,.5,'500 J work',ha='center');txt(ax,.2,2.7,'1000 J in');txt(ax,3.5,2.7,'3500 J delivered');txt(ax,7,1.5,'outside net:\n2500 J out');return 'Three reservoirs: the outside supplies additional net heat'
 if key=='conduction':
  box(ax,.5,1.4,3,1.8,'layer 1\nR1');box(ax,3.5,1.4,5,1.8,'layer 2\nR2');txt(ax,.5,3.8,'Th');txt(ax,3.5,3.8,'Tj');txt(ax,8.5,3.8,'Tc');arrow(ax,(1,.6),(8,.6));txt(ax,5,.05,'same steady heat rate in series',ha='center');return 'Each series temperature drop equals heat rate times resistance'
 if key=='balloon':
  ax.set_aspect('equal');ax.add_patch(Circle((3.5,3),1.3,ec=T,fc='#eff8f5'));ax.plot([2.5,3,4,4.5],[2.1,.8,.8,2.1],c=I);box(ax,3,.3,1,.5,'');arrow(ax,(6,1),(6,4));txt(ax,6,4.3,'buoyancy',ha='center');arrow(ax,(8,4),(8,1),R);txt(ax,8,.3,'weight',ha='center');return 'Open bottom: same approximate P, hotter air less dense'
 if key=='throttle':
  box(ax,.4,1.4,3.1,2,'high P1\nh1');box(ax,6.5,1.4,3.1,2,'low P2\nh2');ax.add_patch(Rectangle((4.6,1.2),.8,2.4,ec=I,fc=Y,hatch='///'));arrow(ax,(3.6,2.4),(4.5,2.4));arrow(ax,(5.5,2.4),(6.4,2.4));txt(ax,5,.3,'adiabatic porous plug; no shaft work',ha='center');return 'Steady throttle: h conserved if speed/height changes negligible'
 raise KeyError(key)
