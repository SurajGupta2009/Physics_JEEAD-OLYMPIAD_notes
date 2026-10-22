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
  if slug=='flux':
   th=np.linspace(0,np.pi,120);plot(a,th,np.cos(th),'angle normal to B (rad)',r'$\Phi/BA$');return 'Flux through the loop: BA face-on, zero edge-on, negative when reversed'
  if slug=='faraday':
   t=np.linspace(0,2*np.pi,200);plot(a,t,np.cos(t),'time (rad)',r'$\Phi$ and $\mathrm{EMF}$','flux');a.plot(t,-np.sin(t),c=R,label='EMF = -dPhi/dt');leg(a);return 'Flux and EMF a quarter-cycle apart: peak EMF where flux vanishes'
  if slug=='motional':
   v=np.linspace(0,2,100);plot(a,v,v,'rod speed v / v0',r'$\mathrm{EMF}/(Blv_0)$');return 'Motional EMF grows linearly with speed: the rod is a battery of Blv'
  if slug=='lenz':
   t=np.linspace(0,3,160);plot(a,t,np.exp(-t),'t / tau',r'$v/v_0$','coasting rod');return 'Lenz drag decays the speed exponentially: tau = mR over B squared l squared'
  if slug=='rails':
   t=np.linspace(0,3,160);plot(a,t,1-np.exp(-t),'t / tau','speed (normalised)','driven to terminal');a.plot(t,np.exp(-t),c=R,label='coasting to rest');leg(a);return 'The rod family: one time constant, decay or approach seen from two ends'
  if slug=='machines':
   t=np.linspace(0,2*np.pi,200);plot(a,t,np.sin(t),'rotor angle (rad)',r'$\mathrm{EMF}$ and $\Phi$','EMF = sin');a.plot(t,np.cos(t),c=R,label='flux = cos');leg(a);return 'Rotating coil: EMF largest at zero flux, zero at maximum flux'
  if slug=='attachments':
   t=np.linspace(0,3,160);plot(a,t,np.minimum(t,1.2),'t (normalised)','speed (normalised)','capacitor: constant a');a.plot(t,1-np.exp(-t),c=R,label='resistor: terminal speed');a.plot(t,np.ones_like(t),ls='--',c=I,lw=.8);leg(a);return 'Resistor gives a terminal speed; capacitor gives constant acceleration; inductor gives SHM'
  if slug=='induced-E':
   r=np.linspace(0,3,240);E=np.where(r<1,r/2,.5/np.maximum(r,.01));plot(a,r,E,'r / R',r'$E/(R\,\dot B/2)$','induced E');return 'Induced E grows linearly inside the solenoid and falls as 1/r outside: peak at the winding'
  if slug=='betatron':
   r=np.linspace(.02,2,200);B=np.where(r<1,1.6-.6*r,1/r);plot(a,r,B,'r / R',r'$B/\langle B\rangle$','orbit field profile');a.axhline(.5,c=R,ls='--');return 'Betatron poles: average field inside is twice the field on the orbit (dashed 2:1)'
  if slug=='eddy':
   t=np.linspace(0,3,160);plot(a,t,np.exp(-t),'t / tau','v / v0','copper');a.plot(t,np.exp(-2*t),c=R,label='aluminium, half rho/sigma');leg(a);return 'Eddy braking is exponential; the material ratio rho_m over sigma sets the time'
  if slug=='motors':
   t=np.linspace(0,3,160);plot(a,t,4+20*np.exp(-t),'t / tau','I (A)','starting motor');a.axhline(24,c=R,ls='--');return 'Start-up current falls from V/R = 24 A to the running 4 A as back-EMF builds'
  if slug=='voltmeter':
   bars(a,['leads left','leads right'],[0.9,-0.1],'voltmeter reading (V)');return 'Two voltmeters on the same points read different path integrals when flux is changing'
  if slug=='inductance':
   N=np.linspace(1,3,100);plot(a,N,N*N,'turns N / N0',r'$L/L_0$','same shape');return 'Inductance grows as N squared: N makes the field and N links it'
  if slug=='compute-L':
   b=np.linspace(1.1,8,120);plot(a,b,np.log(b),'b / a',r"$L'/(\mu_0/2\pi)$",'coax cable');return 'Cable inductance per length grows only logarithmically with the outer radius'
  if slug=='mutual':
   k=np.linspace(0,1,100);plot(a,k,k,'coupling k',r'$M/\sqrt{L_1L_2}$','perfect bound');return 'Mutual inductance is k times the geometric mean: 1 on a shared core, 0 perpendicular'
  if slug=='RL':
   t=np.linspace(0,3,160);plot(a,t,1-np.exp(-t),'t / tau','i / i_final and V_L / V','current rise');a.plot(t,np.exp(-t),c=R,label='inductor voltage');leg(a);return 'RL transient: current rises as the inductor voltage falls; same exponential both ways'
  if slug=='energy-mag':
   bars(a,['electric at 3 MV/m','magnetic at 1 T'],[np.log10(40),np.log10(4e5)],'log10 u (J/m3)');return 'Magnetic storage beats electric by five decades: breakdown limits air, not tesla'
  if slug=='analogy':
   t=np.linspace(0,3,160);plot(a,t,1-np.exp(-t),'t / tau','response','circuit i(t) and mass v(t)');a.plot(t,t*np.exp(-t)*1.4,c=R,label='LC analogue peaks then falls');leg(a);return 'Mechanical twins: mass is inductance, spring is capacitance, dashpot is resistance'
  if slug=='LC':
   t=np.linspace(0,2*np.pi,200);plot(a,t,np.cos(t)**2,'time (rad)','energy (normalised)','capacitor energy');a.plot(t,np.sin(t)**2,c=R,label='inductor energy');leg(a);return 'Energy sloshes between C and L at twice the circuit frequency; the sum stays constant'
  if slug=='ac-rms':
   t=np.linspace(0,2*np.pi,240);plot(a,t,np.abs(np.sin(t)),'time (rad)','|sin| and sin squared','rectified sine, mean 0.637');a.plot(t,np.sin(t)**2,c=R,label='sin squared, mean 0.5');leg(a);return 'RMS is the root of the mean of the square: 0.707 against the rectified mean 0.637'
  if slug=='reactance':
   w=np.logspace(-1,1,120);plot(a,w,w,r'$\omega/\omega_0$','X (normalised)',r'$X_L=\omega L$');a.plot(w,1/w,c=R,label=r'$X_C=1/\omega C$');a.set_xscale('log');a.set_yscale('log');leg(a);return 'Reactances cross at resonance: L blocks high frequencies, C blocks low'
  if slug=='phasors':
   t=np.linspace(0,2*np.pi,240);plot(a,t,np.sin(t),'time (rad)','sinusoids','I reference');a.plot(t,np.sin(t-np.pi/2),c=R,label='V_L, lags I');a.plot(np.nan,np.nan,c=T,label='sum is another sinusoid');leg(a);return 'Two sinusoids of one frequency add to a sinusoid: the phasor sum'
  if slug=='LCR':
   w=np.linspace(.3,3,200);Z=np.sqrt(1+(2*(w-1/w))**2);plot(a,w,Z,r'$\omega/\omega_0$',r'$Z/R$','series LCR');a.axhline(1,c=R,ls='--');return 'Impedance dips to R at resonance where the reactances cancel exactly'
  if slug=='resonance':
   w=np.linspace(.5,1.5,240);plot(a,w,1/np.sqrt(1+4*(w-1/w)**2),r'$\omega/\omega_0$',r'$I/I_{\max}$','Q = 2');a.plot(w,1/np.sqrt(1+25*(w-1/w)**2),c=R,label='Q = 5');a.plot(w,1/np.sqrt(1+100*(w-1/w)**2),c=I,label='Q = 10');leg(a);return 'Resonance curves sharpen with Q; half-power points sit omega0/Q apart'
  if slug=='power':
   t=np.linspace(0,2*np.pi,240);p=np.sin(t)*np.sin(t-np.pi/3);plot(a,t,p,'time (rad)','p(t) / (V0 I0 / 2)','instantaneous power');a.axhline(.5,c=R,ls='--');return 'Instantaneous power pulses at 2 omega about the mean P = VI cos phi (dashed)'
  if slug=='parallel':
   w=np.linspace(.3,3,200);plot(a,w,np.sqrt(1+(2*(w-1/w))**2),r'$\omega/\omega_0$',r'$I_{\rm line}/(V/R)$','parallel tank');return 'Parallel LC at resonance: line current minimum, impedance maximum: anti-resonance'
  if slug=='complex':
   w=np.linspace(.3,3,200);plot(a,w,np.sqrt(1+(2*(w-1/w))**2),r'$\omega/\omega_0$',r'$|\tilde Z|/R$ and $\phi$','|Z| / R');a.plot(w,np.arctan2(2*(w-1/w),1),c=R,label='phase phi');leg(a);return 'Complex impedance: magnitude and argument in one picture; phi flips sign at resonance'
  if slug=='transformer':
   n=np.linspace(.2,3,120);plot(a,n,n*n,'turns ratio n = Np/Ns',r'$Z_p/Z_s$','reflected impedance');return 'Impedance reflects as the square of the turns ratio: the matching principle'
  if slug=='rectifiers':
   t=np.linspace(0,2*np.pi,240);plot(a,t,np.abs(np.sin(t)),'time (rad)','output (normalised)','full-wave humps');a.axhline(2/np.pi,c=R,ls='--');return 'Full-wave output with its DC average 2/pi; a smoothing capacitor rides the humps'
  if slug=='faraday-disc':
   w=np.linspace(0,2,100);plot(a,w,w,'disc speed omega / omega0',r'$\mathrm{EMF}/(B\omega_0 a^2/2)$');return 'The disc EMF is linear in spin rate: half B omega a squared'
  if slug=='betatron-2':
   r=np.linspace(.3,2,120);plot(a,r,np.full_like(r,.5),'r / R',r'$B_{\rm orb}/\langle B\rangle$','canonical momentum result');a.axhline(1,c=R,ls='--');return 'Conserved canonical momentum forces B_orb = half the average field at every radius'
  if slug=='tube-braking':
   t=np.linspace(0,4,160);plot(a,t,1-np.exp(-t),'t / tau','v / v_terminal','magnet in tube');return 'The falling magnet approaches a terminal speed of tenths of a metre per second'
  if slug=='sc-flux':
   L=np.linspace(.4,1.6,120);plot(a,L,1/L,'L / L0',r'$I/I_0$','constant flux');return 'Flux conservation: squash the ring and the current rises as 1/L while energy rises'
  if slug=='tether-launcher':
   bars(a,['ring kinetic','ring heat'],[np.log10(.24),np.log10(16)],'log10 energy (J)');return 'The coil launcher is 1.5 per cent efficient: most pulse energy heats the ring'
  if slug=='switch-drag':
   v=np.linspace(0,4,160);plot(a,v,v/(1+v*v),'v / v_peak','drag F (normalised)','induction drag');return 'Drag rises linearly, peaks near v = wR/L, then falls: the general brake law'
  if slug=='cable':
   x=np.linspace(0,3,200);plot(a,x,np.minimum(x,1),'position x / vt','voltage (normalised)','step at time t');a.plot(x,np.minimum(np.maximum(x-1,0),1),c=R,label='step at time 2t');leg(a);return 'A step travels at v = 1/root(L prime C prime); an open end reflects it with the same sign'
  if slug=='driven-lcr':
   t=np.linspace(0,12,400);env=np.exp(-.18*t);plot(a,t,env*np.cos(1.05*t),'t (normalised)','i (normalised)','transient + steady');a.plot(t,env,c=R,label='decay envelope');a.plot(t,-env,c=R);leg(a);return 'Near resonance the transient beats against the steady state before settling'
  if slug=='maxpower':
   RL=np.linspace(.1,4,160);plot(a,RL,4*RL/(1+RL)**2,r'$R_L/R_s$','P (normalised)','P / P_max');return 'Maximum power at R_L = R_s; half the source power is wasted there'
  if slug=='radio-wien':
   x=np.logspace(-1,1,160);plot(a,x,1/np.sqrt(9+(x-1/x)**2),r'$\omega RC$',r'$|\beta|$','Wien transfer');return 'The Wien network balances at omega RC = 1 where beta = 1/3 with zero phase'
  if slug=='emi-estimates':
   f=np.logspace(3,6,120);plot(a,f,1/np.sqrt(f),'frequency (Hz)','delta (normalised)','delta ~ 1 / sqrt(f)');return 'Skin depth falls as 1/root(frequency): iron pans heat at 25 kHz, aluminium reflects'
  raise KeyError(key)
 # First panel: labelled physical geometry.
 if slug=='lorentz':
  dot(a,0,0);arr(a,(0,0),(1.2,0),R);txt(a,1.3,0,'v',ha='center');into_page(a,0,1.1);arr(a,(0,0),(0,-1.15),T);txt(a,1.05,-0.92,'F = q v x B',ha='left');txt(a,0,-1.52,'q > 0: thumb first, sign second',ha='center');return 'Right hand along v, curl to B, thumb gives force; flip for negative q'
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
  a.add_patch(Arc((0,0),1.6,1.6,theta1=0,theta2=360,ec=T,lw=2));line(a,(-2.3,0),(2.6,0));txt(a,.52,.45,'R');dot(a,2.1,0,I);txt(a,2.15,.22,'P(x)');arr(a,(.8,.8),(1.05,1.05),R);txt(a,1.32,1.2,'dB',ha='center');txt(a,0,-1.5,'transverse parts cancel; net field is axial',ha='center');return 'Loop axis: every element is at distance sqrt(R^2 + x^2) from P'
 if slug=='solenoid':
  for z in np.linspace(-1.8,1.8,9):
   circ(a,z,0,.28);arr(a,(z,.28),(z,.75),T)
  line(a,(-2.4,-1.1),(2.4,-1.1),ls='--');txt(a,0,1.35,'uniform B inside; about half at the end face',ha='center');txt(a,2.55,-.7,'n turns/m',ha='center');return 'Solenoid: stacked loops give a uniform interior field and zero outside ideal'
 if slug=='moment':
  a.add_patch(Arc((0,0),1.5,1.5,theta1=0,theta2=360,ec=T,lw=2));arr(a,(0,.75),(.35,1.05),R);txt(a,.55,1.15,'I',ha='center');arr(a,(0,0),(0,1.5),T);txt(a,.18,.75,'mu');txt(a,0,-1.45,'fingers along I: thumb is mu',ha='center');return 'Loop moment mu = N I A with the right-hand area vector'
 if slug=='ampere':
  line(a,(-2.2,0),(2.2,0),lw=3);txt(a,2.3,0,'I out');circ(a,0,0,1.05,ls='--');arr(a,(1.05,0),(.75,.35),T);txt(a,.35,.55,'path C');txt(a,0,-1.5,'loop direction sets the sign of enclosed current',ha='center');return 'Amperian loop around a wire: circulation counts threaded current'
 if slug=='ampere-apps':
  circ(a,0,0,1.15,ec=T);circ(a,0,0,.55,ec=R);txt(a,0,0,'J',ha='center');arr(a,(0,0),(.52,.18),R);txt(a,-.95,.75,'r inside');arr(a,(0,-.15),(1.75,-.15),T);txt(a,1.85,-.45,'r outside');return 'Thick wire: enclosed fraction grows as r squared inside, full current outside'
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
 if slug=='flux':
  a.add_patch(Rectangle((-.9,-.5),1.8,1.0,fill=0,ec=I,lw=2));arr(a,(-1.6,1.2),(-.3,.3),R);a.text(-2.2,.85,'B',color=R,fontsize=12);arr(a,(.9,.5),(2.2,1.4),I);a.text(1.0,1.55,'n',color=I,fontsize=12);line(a,(-1.6,1.2),(1.3,1.45),color=R,ls='--',lw=1.2);a.text(0,-1.25,r'$\Phi = BA\cos\theta$',color=I,fontsize=12,ha='center');return 'Loop flux: the angle between the field and the normal decides everything'
 if slug=='faraday':
  a.add_patch(Rectangle((2.0,-.45),.55,.9,fill=1,fc=R,ec='k'));a.text(2.27,.7,'N',color=R,fontsize=12,ha='center');arr(a,(1.9,.2),(.95,.2),R);[line(a,(x,-.5),(x,.5),lw=2) for x in (1.2,1.4,1.6)];a.text(1.4,-1.0,'coil',color=I,fontsize=11,ha='center');line(a,(1.4,-.55),(1.4,-1.35),lw=1.6);line(a,(.85,-1.35),(2.0,-1.35),lw=1.6);a.add_patch(Arc((1.4,-1.35),1.15,.7,angle=0,theta1=200,theta2=340,ec=T,lw=2));a.text(1.4,-1.72,'galvanometer',color=T,fontsize=11,ha='center');return 'The magnet drives the flux; the meter sees only the rate of change'
 if slug=='motional':
  line(a,(-2.6,-.85),(2.6,-.85),lw=3);line(a,(-2.6,.85),(2.6,.85),lw=3);line(a,(0,-.85),(0,.85),lw=4,color=R);arr(a,(0,1.05),(1.5,1.05),R);a.text(.55,1.35,'v',color=R,fontsize=12,ha='center');[a.text(x,y,r'$\otimes$',ha='center',fontsize=11) for x,y in ((-1.8,-.35),(-1.8,.35),(1.2,-.35),(1.2,.35))];a.text(2.05,.55,'+',color=I,fontsize=16,ha='center');a.text(2.05,-.75,'-',color=I,fontsize=16,ha='center');a.text(-2.2,-1.35,r'$\mathrm{EMF} = Blv$',color=T,fontsize=12);return 'A moving rod in a B field: charge is driven along it like a battery'
 if slug=='lenz':
  a.add_patch(Rectangle((-.8,-.7),1.6,1.4,fill=0,ec=I,lw=2));th=np.linspace(0,2*np.pi,64);a.plot(-.55+.22*np.cos(th),.22*np.sin(th),c=R,lw=2);a.add_patch(Rectangle((2.05,-.4),.55,.8,fill=1,fc=R,ec='k'));a.text(2.32,.62,'N',color=R,fontsize=12,ha='center');arr(a,(1.95,.05),(.95,.05),R);a.add_patch(Arc((0,0),1.6,1.4,angle=0,theta1=215,theta2=325,ec=T,lw=2));arr(a,(-.55,-.52),(-1.35,-.52),T);a.text(-1.35,-1.25,'induced I opposes the change',color=T,fontsize=11);return 'Lenz law: the induced current always pushes back against what produced it'
 if slug=='rails':
  line(a,(-2.6,-.75),(2.6,-.75),lw=3);line(a,(-2.6,.75),(2.6,.75),lw=3);line(a,(.4,-.75),(.4,.75),lw=4,color=R);arr(a,(.4,.95),(1.7,.95),R);a.text(.85,1.28,'v',color=R,fontsize=12,ha='center');line(a,(-2.6,.75),(-2.6,-.75),lw=3);a.text(-2.85,0,'R',color=I,fontsize=12,ha='center');[a.text(x,y,r'$\otimes$',ha='center',fontsize=11) for x,y in ((-1.6,-.3),(-1.6,.3),(1.4,-.3),(1.4,.3))];arr(a,(-.15,0),(-1.35,0),T);a.text(-1.15,.35,r'$F = BIl$',color=T,fontsize=11);return 'Rails close the circuit: current flows, and the rod feels the drag force'
 if slug=='machines':
  a.add_patch(Circle((0,0),1.35,fill=0,ec=I,lw=1.6));line(a,(0,0),(1.35,0),lw=4,color=R);a.text(1.55,.2,'rod',color=R,fontsize=11);a.add_patch(Arc((0,0),1.7,1.7,angle=0,theta1=30,theta2=90,ec=T,lw=2));arr(a,(1.2,1.05),(.55,1.42),T);a.text(1.35,1.55,r'$\omega$',color=T,fontsize=12);a.add_patch(Circle((0,0),.18,fill=1,fc=I,ec=I));line(a,(0,0),(0,-1.75),lw=1.6);a.text(-2.2,1.35,r'$\mathrm{EMF} = \frac{1}{2}B\omega a^2$',color=T,fontsize=11);return 'A rotating rod sweeps area at rate half B omega a squared: the disc generator'
 if slug=='attachments':
  line(a,(-2.6,-.75),(2.6,-.75),lw=3);line(a,(-2.6,.75),(2.6,.75),lw=3);line(a,(.4,-.75),(.4,.75),lw=4,color=R);arr(a,(.4,.95),(1.7,.95),R);a.text(.85,1.28,'v',color=R,fontsize=12,ha='center');line(a,(-2.6,.75),(-2.6,-.75),lw=3);line(a,(-2.15,.35),(-2.15,-.35),lw=4);line(a,(-2.65,.35),(-2.65,-.35),lw=4);a.text(-2.85,0,'C',color=I,fontsize=12,ha='center');[a.text(x,y,r'$\otimes$',ha='center',fontsize=11) for x,y in ((-1.4,-.3),(-1.4,.3),(1.5,-.3),(1.5,.3))];a.text(-1.15,-1.35,'rails + capacitor: a = const',color=T,fontsize=11);return 'Swap the terminal element and the whole motion changes: R, C or L'
 if slug=='induced-E':
  a.add_patch(Circle((0,0),1.15,fill=0,ec=I,lw=2));[a.text(x,y,r'$\otimes$',ha='center',fontsize=11) for x,y in ((-.5,-.5),(-.5,.5),(.5,-.5),(.5,.5))];a.add_patch(Arc((0,0),2.2,2.2,angle=0,theta1=0,theta2=360,ec=T,lw=2));arr(a,(0,1.1),(.95,.55),T);a.text(.25,1.42,r'$E_\theta$',color=T,fontsize=12);a.text(0,-1.55,r'$E = \frac{1}{2} r \,\mathrm{dB}/\mathrm{dt}$ inside',color=T,fontsize=11,ha='center');return 'A changing B field makes electric loops even with no wire present'
 if slug=='betatron':
  a.add_patch(Circle((0,0),1.3,fill=0,ec=I,lw=1.6,ls='--'));a.add_patch(Circle((0,0),.75,fill=0,ec=T,lw=1.6));[a.text(x,y,r'$\otimes$',ha='center',fontsize=10) for x,y in ((-1.9,-.9),(-1.9,.9),(1.9,-.9),(1.9,.9),(-.3,-.3),(-.3,.3),(.3,-.3),(.3,.3))];a.add_patch(Arc((0,0),1.7,1.7,angle=0,theta1=20,theta2=80,ec=T,lw=2));arr(a,(1.15,1.1),(.3,1.45),T);a.text(1.25,1.52,r'$E_\theta$',color=T,fontsize=11);a.text(1.55,.35,'orbit',color=I,fontsize=10);a.text(0,-1.55,r'$B_{\rm orb} = \frac{1}{2}\langle B\rangle$',color=T,fontsize=11,ha='center');return 'Betatron: induced E accelerates the beam while the 2:1 rule holds the orbit'
 if slug=='eddy':
  a.add_patch(Rectangle((-2.2,-1.0),4.4,2.0,fill=0,ec=I,lw=2));[a.text(x,.55,r'$\uparrow$',ha='center',fontsize=10,color=I) for x in np.linspace(-1.8,1.8,7)];a.text(2.35,.75,'B up',color=I,fontsize=10);th=np.linspace(0,2*np.pi,40);a.plot(-1.35+.55*np.cos(th),-.15+.45*np.sin(th),c=T,lw=2);a.plot(.55+.55*np.cos(th),-.15+.45*np.sin(th),c=T,lw=2);a.text(-1.35,-1.5,'eddy loops',color=T,fontsize=10,ha='center');a.text(1.35,-1.5,'drag opposes motion',color=T,fontsize=10,ha='center');return 'Eddy currents circulate in bulk metal; slots break the loops and brake less'
 if slug=='motors':
  line(a,(-2.4,-1.0),(-2.4,1.0),lw=3);line(a,(-1.9,-1.0),(-1.9,1.0),lw=3);a.text(-2.85,0,'V',color=I,fontsize=12,ha='center');line(a,(-1.9,1.0),(1.2,1.0),lw=2);line(a,(-2.4,-1.0),(1.2,-1.0),lw=2);a.add_patch(Rectangle((1.2,-.55),1.5,1.1,fill=0,ec=T,lw=2));a.text(1.95,.05,'M',color=T,fontsize=14,ha='center');a.text(1.95,-.95,r'$\mathrm{EMF}_b = k\omega$',color=T,fontsize=11,ha='center');line(a,(2.7,-.55),(2.7,-1.0),lw=2);line(a,(2.7,-1.0),(1.2,-1.0),lw=2);return 'A motor is a generator running backwards: back-EMF limits the current'
 if slug=='voltmeter':
  th=np.linspace(0,2*np.pi,48);a.plot(1.1*np.cos(th),.85*np.sin(th),c=I,lw=2);[a.text(x,y,r'$\otimes$',ha='center',fontsize=10) for x,y in ((-.55,-.28),(-.55,.28),(.55,-.28),(.55,.28))];line(a,(-1.1,.35),(-2.1,.35),lw=1.8);line(a,(-2.1,.35),(-2.1,-.35),lw=1.8);line(a,(-2.1,-.35),(-1.1,-.35),lw=1.8);line(a,(1.1,.35),(2.1,.35),lw=1.8);line(a,(2.1,.35),(2.1,-.35),lw=1.8);line(a,(2.1,-.35),(1.1,-.35),lw=1.8);a.text(-2.15,0,'R',color=I,fontsize=11,ha='center');a.text(2.15,0,'R',color=I,fontsize=11,ha='center');a.text(0,-1.5,r'$V = \int E\cdot dl$ is path dependent',color=T,fontsize=11,ha='center');return 'Two paths around a changing flux: Kirchhoff is not enough, Faraday is'
 if slug=='inductance':
  line(a,(-2.3,.2),(-2.3,-.8),lw=3);line(a,(-1.95,.2),(-1.95,-.8),lw=3);a.text(-2.85,-.3,'A',color=I,fontsize=11,ha='center');line(a,(-2.3,.2),(1.9,.2),lw=2);line(a,(-1.95,-.8),(1.9,-.8),lw=2);[line(a,(x,.2),(x+.35,-.8),lw=3,color=R) for x in (-1.0,-.2,.6,1.4)];a.text(1.15,1.25,'N turns',color=R,fontsize=11,ha='center');line(a,(1.9,.2),(1.9,-.8),lw=3,color=R);line(a,(-2.55,-.3),(1.2,-.3),lw=1.4,ls='--');a.text(.2,-.62,r'$\Phi = LI$',color=T,fontsize=12,ha='center');return 'One turn owns flux Phi = LI; N turns own N times it: the N squared law'
 if slug=='compute-L':
  a.add_patch(Circle((0,0),1.35,fill=0,ec=I,lw=2));a.add_patch(Circle((0,0),.55,fill=1,fc='0.85',ec=I,lw=2));a.text(0,0,r'$\otimes$',ha='center',fontsize=12);[a.text(x,y,r'$\otimes$',ha='center',fontsize=10) for x,y in ((2.1,0),(-2.1,0),(0,1.5),(0,-1.5))];arr(a,(0,0),(.52,0),T);a.text(.3,.28,'a',color=T,fontsize=11,ha='center');arr(a,(0,0),(1.32,0),T);a.text(1.05,.28,'b',color=T,fontsize=11,ha='center');a.text(-2.5,1.5,'inner I out',color=I,fontsize=10);a.text(1.5,-1.55,'return I back',color=I,fontsize=10);return 'Coax: flux between the conductors stores the inductance per metre'
 if slug=='mutual':
  a.add_patch(Rectangle((-1.9,-.35),3.8,.7,fill=1,fc='0.85',ec=I,lw=1.6));[line(a,(x,.35),(x+.3,-.35),lw=3,color=R) for x in (-1.4,-.7,0)];[line(a,(x,.35),(x+.3,-.35),lw=3,color=T) for x in (.7,1.4)];a.text(-1.4,1.0,'coil 1',color=R,fontsize=11,ha='center');a.text(1.35,1.0,'coil 2',color=T,fontsize=11,ha='center');a.text(0,-1.25,r'$M = k\sqrt{L_1L_2}$',color=I,fontsize=12,ha='center');return 'Shared flux on a core links the coils; perpendicular ones decouple'
 if slug=='RL':
  line(a,(-2.3,-.85),(-2.3,.85),lw=3);line(a,(-1.85,-.85),(-1.85,.85),lw=3);a.text(-2.85,0,'V',color=I,fontsize=12,ha='center');line(a,(-1.85,.85),(2.0,.85),lw=2);line(a,(-2.3,-.85),(2.0,-.85),lw=2);a.add_patch(Rectangle((2.0,-.2),.7,.4,fill=1,fc=R,ec=I));a.text(2.35,-.62,'R',color=R,fontsize=11,ha='center');line(a,(2.7,.2),(2.7,.85),lw=2);line(a,(2.7,-.2),(2.7,-.85),lw=2);[a.add_patch(Arc((x,.55),.8,.6,angle=0,theta1=0,theta2=180,ec=T,lw=2)) for x in (0.2,1.0)];a.text(1.0,1.35,'L',color=T,fontsize=11,ha='center');a.text(.2,-1.5,r'$\tau = L/R$',color=T,fontsize=12,ha='center');return 'The inductor fights change: current takes L/R seconds to make up its mind'
 if slug=='energy-mag':
  a.add_patch(Rectangle((-2.4,-.7),4.8,1.4,fill=0,ec=I,lw=2));[line(a,(x,-.7),(x,.7),lw=3,color=R) for x in np.linspace(-1.9,1.9,6)];[line(a,(-1.9,y),(1.9,y),lw=1.4,color=T,ls='--') for y in (-.35,0,.35)];a.text(0,1.15,r'$u_B = B^2/2\mu_0$',color=T,fontsize=12,ha='center');a.text(0,-1.35,'energy lives in the field, not the wire',color=I,fontsize=10,ha='center');return 'The whole stored energy sits in the field volume between the windings'
 if slug=='analogy':
  a.add_patch(Rectangle((-2.75,-.6),1.0,1.0,fill=1,fc='0.85',ec=I));a.text(-2.25,.75,'m',color=I,fontsize=11,ha='center');line(a,(-1.75,-.1),(-.7,-.1),lw=3);a.text(-1.25,.35,'k',color=I,fontsize=11,ha='center');line(a,(-.7,-.6),(-.7,.4),lw=2);a.text(-.5,-.3,'damping',color=I,fontsize=9);line(a,(.7,.85),(2.75,.85),lw=2);line(a,(.7,-.85),(2.75,-.85),lw=2);line(a,(.7,.85),(.7,-.85),lw=2);line(a,(2.75,.85),(2.75,-.85),lw=2);a.add_patch(Rectangle((1.05,-.2),.55,.4,fill=1,fc=R,ec=I));a.text(1.3,-.62,'R',color=R,fontsize=10,ha='center');[a.add_patch(Arc((x,-.2),.35,.4,angle=90,theta1=0,theta2=180,ec=T,lw=2)) for x in (1.8,2.15)];a.text(1.95,.4,'L',color=T,fontsize=10,ha='center');a.text(0,-1.5,r'$m \leftrightarrow L$, $k \leftrightarrow 1/C$',color=I,fontsize=11,ha='center');return 'Mass-spring-dashpot and RLC share one differential equation'
 if slug=='LC':
  line(a,(-2.4,-.9),(-2.4,.9),lw=3);line(a,(-1.95,-.9),(-1.95,.9),lw=3);a.text(-2.85,0,'C',color=I,fontsize=12,ha='center');line(a,(-1.95,.9),(1.7,.9),lw=2);line(a,(-2.4,-.9),(1.7,-.9),lw=2);[a.add_patch(Arc((x,.55),.8,.7,angle=0,theta1=0,theta2=180,ec=T,lw=2)) for x in (1.0,1.4)];a.text(1.55,1.35,'L',color=T,fontsize=11,ha='center');line(a,(1.7,.9),(2.4,.9),lw=2);line(a,(1.7,-.9),(2.4,-.9),lw=2);a.text(2.05,0,'L',color=T,fontsize=10,ha='center');a.text(0,-1.55,r'$\omega_0 = 1/\sqrt{LC}$',color=T,fontsize=12,ha='center');return 'The LC tank: charge and current swap places omega0 times a second'
 if slug=='ac-rms':
  a.add_patch(Circle((0,0),1.2,fill=0,ec=I,lw=2));[a.text(x,y,r'$\otimes$',ha='center',fontsize=10) for x,y in ((-2.1,-.7),(-2.1,.7),(2.1,-.7),(2.1,.7))];line(a,(0,0),(.85,.85),lw=4,color=R);a.add_patch(Arc((0,0),1.55,1.55,angle=0,theta1=35,theta2=95,ec=T,lw=2));arr(a,(1.1,1.0),(.5,1.33),T);a.text(1.3,1.5,r'$\omega$',color=T,fontsize=12);line(a,(0,0),(0,-1.35),lw=1.6);line(a,(0,-1.35),(-2.4,-1.35),lw=1.6);line(a,(0,-1.35),(2.4,-1.35),lw=1.6);a.text(-2.3,-1.68,'V = V0 sin wt',color=I,fontsize=10);return 'The generator coil: EMF follows the sine of the rotor angle'
 if slug=='reactance':
  [(a.add_patch(Rectangle((xx,-.7),1.25,1.4,fill=0,ec=cx,lw=2)),a.text(xx+.62,.05,lb,color=cx,fontsize=10,ha='center')) for xx,lb,cx in ((-2.15,'XR = R',R),(-.35,'XL = wL',T),(1.55,'XC = 1/wC',I))];a.text(0,-1.5,r'$\tilde Z = R + j\omega L + 1/(j\omega C)$',color=I,fontsize=11,ha='center');return 'Three elements, three rules: R blocks nothing, L the fast, C the slow'
 if slug=='phasors':
  arr(a,(0,0),(2.2,0),I);a.text(1.0,-.38,r'$V_R \parallel I$',color=I,fontsize=10,ha='center');arr(a,(0,0),(0,1.45),R);a.text(.25,1.15,r'$V_L$',color=R,fontsize=11);arr(a,(0,0),(0,-1.05),T);a.text(.25,-1.25,r'$V_C$',color=T,fontsize=11);arr(a,(0,0),(1.5,1.05),R);a.text(1.55,1.25,r'$V = V_R + V_L + V_C$',color=I,fontsize=10);return 'Phasor picture: horizontal resistive, vertical reactive, lengths at omega'
 if slug=='LCR':
  line(a,(-2.5,-.9),(2.5,-.9),lw=2);line(a,(-2.5,-.9),(-2.5,.9),lw=2);line(a,(2.5,-.9),(2.5,.9),lw=2);line(a,(-2.5,.9),(2.5,.9),lw=2);a.add_patch(Rectangle((-1.55,-1.05),1.1,.3,fill=1,fc=R,ec=I));a.text(-1.0,-1.42,'R',color=R,fontsize=11,ha='center');[a.add_patch(Arc((x,1.25),.9,.7,angle=0,theta1=0,theta2=180,ec=T,lw=2)) for x in (0.0,.45)];a.text(.55,1.5,'L',color=T,fontsize=10,ha='center');line(a,(1.45,1.05),(1.45,.75),lw=2);line(a,(1.95,1.05),(1.95,.75),lw=2);a.text(1.95,1.5,'C',color=I,fontsize=10,ha='center');a.text(-2.6,0,'V',color=I,fontsize=11,ha='center');return 'Series LCR: one current, three voltages, one phase angle'
 if slug=='resonance':
  line(a,(-2.5,-.85),(2.5,-.85),lw=2);line(a,(-2.5,-.85),(-2.5,.85),lw=2);line(a,(2.5,-.85),(2.5,.85),lw=2);line(a,(-2.5,.85),(2.5,.85),lw=2);a.add_patch(Rectangle((-1.7,-1.0),1.05,.3,fill=1,fc=R,ec=I));a.text(-1.85,-1.30,'R',color=R,fontsize=10,ha='center');[a.add_patch(Arc((x,1.2),.9,.7,angle=0,theta1=0,theta2=180,ec=T,lw=2)) for x in (-.15,.35)];a.text(.95,1.5,'L',color=T,fontsize=10,ha='center');line(a,(1.45,1.05),(1.45,.72),lw=2);line(a,(1.95,1.05),(1.95,.72),lw=2);a.text(2.15,1.5,'C',color=I,fontsize=10,ha='center');a.text(0,-1.72,r'$\omega_0 = 1/\sqrt{LC}$, $Q = \omega_0L/R$',color=T,fontsize=11,ha='center');return 'At resonance the source sees pure R; Q decides the sharpness'
 if slug=='power':
  arr(a,(0,0),(2.3,0),I);a.text(1.0,-.38,r'$P = VI\cos\phi$',color=I,fontsize=10,ha='center');arr(a,(0,0),(0,1.5),R);a.text(.25,1.15,r'$Q = VI\sin\phi$',color=R,fontsize=10);arr(a,(0,0),(1.7,1.15),T);a.text(1.75,1.35,'S = VI',color=T,fontsize=10);a.text(-2.5,-1.45,'power triangle: watts out, vars sloshing',color=I,fontsize=9);return 'Real power does work; reactive power just sloshes between source and field'
 if slug=='parallel':
  line(a,(-2.4,.95),(2.4,.95),lw=2);line(a,(-2.4,-.95),(2.4,-.95),lw=2);line(a,(-2.4,.95),(-2.4,-.95),lw=2);a.text(-2.85,0,'V',color=I,fontsize=11,ha='center');line(a,(-1.2,.95),(-1.2,-.95),lw=2);a.add_patch(Rectangle((-.7,-.95),.45,1.9,fill=0,ec=I,lw=1.6));a.text(-1.55,.25,'R',color=I,fontsize=10,ha='center');line(a,(0,.95),(0,-.95),lw=2);[a.add_patch(Arc((0,y),.65,.45,angle=90,theta1=0,theta2=180,ec=T,lw=2)) for y in (-.5,-.1)];a.text(-.55,.4,'L',color=T,fontsize=10,ha='center');line(a,(1.2,.95),(1.2,-.95),lw=2);line(a,(.95,.5),(1.45,.5),lw=2);line(a,(.95,.15),(1.45,.15),lw=2);a.text(1.75,.35,'C',color=I,fontsize=10,ha='center');a.text(0,-1.55,'three branch currents add as phasors',color=I,fontsize=9,ha='center');return 'Parallel RLC: branch currents share V but not phase'
 if slug=='complex':
  line(a,(-2.5,0),(2.5,0),lw=2);line(a,(0,-1.5),(0,1.5),lw=2);a.text(2.55,-.3,'R',color=I,fontsize=11);a.text(.15,1.55,'X',color=I,fontsize=11);arr(a,(0,0),(1.9,1.05),T);a.text(1.95,1.25,r'$\tilde Z$',color=T,fontsize=12);a.add_patch(Arc((0,0),1.3,1.3,angle=0,theta1=0,theta2=29,ec=R,lw=1.6));a.text(1.05,.25,r'$\phi$',color=R,fontsize=11);a.text(-2.3,-1.25,r'$\tilde Z = R + jX$',color=I,fontsize=11);return 'Impedance is a complex number: real part dissipates, imaginary stores'
 if slug=='transformer':
  a.add_patch(Rectangle((-1.7,-.85),3.4,1.7,fill=1,fc='0.85',ec=I,lw=1.6));[line(a,(x,.85),(x+.35,-.85),lw=3,color=R) for x in (-1.35,-.85,-.35)];[line(a,(x,.85),(x+.35,-.85),lw=3,color=T) for x in (.55,1.05,1.55)];a.text(-1.35,1.3,'Np',color=R,fontsize=11,ha='center');a.text(1.35,1.3,'Ns',color=T,fontsize=11,ha='center');a.text(0,-1.5,r'$V_s/V_p = N_s/N_p = n$',color=I,fontsize=11,ha='center');return 'Shared flux forces the volts-per-turn to match on both windings'
 if slug=='rectifiers':
  line(a,(-2.4,1.15),(-1.2,1.15),lw=2);line(a,(-2.4,-1.15),(-1.2,-1.15),lw=2);a.text(-2.9,1.15,'AC',color=I,fontsize=10);[(a.add_patch(Rectangle((dxx,dyy),.34,.34,fill=0,ec=R,lw=1.6)),a.text(dxx+.17,dyy+.12,'D',color=R,fontsize=9,ha='center')) for dxx,dyy in ((-1.05,.6),(-1.05,-.95),(1.0,.6),(1.0,-.95))];line(a,(-.71,.78),(-.71,-.78),lw=2);line(a,(1.34,.78),(1.34,-.78),lw=2);line(a,(-.71,.78),(1.0,.78),lw=2);line(a,(-.71,-.78),(1.0,-.78),lw=2);line(a,(1.34,.78),(2.2,.78),lw=2);line(a,(1.34,-.78),(2.2,-.78),lw=2);line(a,(2.2,.45),(2.2,.78),lw=2);line(a,(2.2,-.45),(2.2,-.78),lw=2);line(a,(1.85,.45),(2.55,.45),lw=2);line(a,(1.85,.1),(2.55,.1),lw=2);a.text(2.75,.3,'C',color=I,fontsize=11,ha='center');a.text(0,-1.62,'four diodes steer both half-cycles one way',color=I,fontsize=9,ha='center');return 'Bridge rectifier plus capacitor: chop, steer, smooth'
 if slug=='faraday-disc':
  a.add_patch(Circle((0,0),1.35,fill=0,ec=I,lw=2));[a.text(x,y,r'$\otimes$',ha='center',fontsize=10) for x,y in ((-.65,-.5),(-.65,.5),(.65,-.5),(.65,.5))];line(a,(0,0),(.95,.95),lw=4,color=R);a.text(1.15,1.1,'rod',color=R,fontsize=10);a.add_patch(Arc((0,0),1.7,1.7,angle=0,theta1=25,theta2=85,ec=T,lw=2));arr(a,(1.2,1.0),(.55,1.38),T);a.text(1.35,1.52,r'$\omega$',color=T,fontsize=11);a.add_patch(Circle((0,0),.14,fill=1,fc=I,ec=I));a.add_patch(Circle((.95,.95),.16,fill=1,fc=T,ec=T));a.text(-2.4,-1.5,r'$\mathrm{EMF} = \frac{1}{2}B\omega a^2$',color=T,fontsize=11);return 'Faraday disc: every radius is a rod, all in parallel'
 if slug=='betatron-2':
  a.add_patch(Circle((0,0),1.25,fill=0,ec=I,lw=1.6,ls='--'));[a.text(x,y,r'$\otimes$',ha='center',fontsize=10) for x,y in ((-.45,-.35),(-.45,.35),(.45,-.35),(.45,.35))];a.add_patch(Arc((0,0),1.7,1.7,angle=0,theta1=25,theta2=80,ec=T,lw=2));arr(a,(1.2,1.05),(.35,1.4),T);a.text(-2.35,1.45,r'$p = e\Phi/2\pi r$',color=T,fontsize=11);a.text(.65,1.5,'orbit',color=I,fontsize=9);a.text(0,-1.6,r'$B_{\rm orb} = \frac{1}{2}\langle B \rangle$ for $r = 2R_p$',color=T,fontsize=10,ha='center');return 'Canonical momentum in a symmetric betatron keeps the orbit fixed'
 if slug=='tube-braking':
  line(a,(-.75,-1.5),(-.75,1.5),lw=3);line(a,(.75,-1.5),(.75,1.5),lw=3);a.add_patch(Rectangle((-.45,-.15),.9,.6,fill=1,fc=R,ec='k'));arr(a,(.15,-.55),(.15,-1.15),R);a.text(.35,-.85,'v',color=R,fontsize=11);[a.add_patch(Arc((0,y),1.5,.35,angle=0,theta1=0,theta2=180,ec=T,lw=1.6)) for y in (-1.25,-.95,.6,.9)];a.text(-2.55,1.2,'eddy braking',color=T,fontsize=10);a.text(-2.55,-1.55,'v_term = mgR / (klB)^2',color=T,fontsize=10);return 'A magnet falls through a conducting tube at a crawl: terminal velocity law'
 if slug=='sc-flux':
  a.add_patch(Arc((0,0),2.6,2.6,angle=0,theta1=0,theta2=360,ec=I,lw=6));a.add_patch(Arc((0,0),2.0,2.0,angle=0,theta1=0,theta2=360,ec='w',lw=1.6));th=np.linspace(0,2*np.pi,60);a.plot(1.15*np.cos(th),1.15*np.sin(th),c=T,lw=1.6,ls='--');arr(a,(-.75,1.02),(-1.25,.75),R);a.text(0,1.55,'I',color=R,fontsize=12,ha='center');a.text(0,-1.62,r'$LI + \Phi_{\rm ext} = \rm const$',color=T,fontsize=11,ha='center');return 'Superconducting ring: flux is frozen; current appears to hold it'
 if slug=='tether-launcher':
  [a.add_patch(Arc((x,-.2),.6,1.2,angle=90,theta1=0,theta2=180,ec=I,lw=2)) for x in (-1.35,-1.05,-.75,-.45)];line(a,(-2.3,-.8),(-2.3,.4),lw=2);line(a,(.3,-.8),(.3,.4),lw=2);a.text(-2.65,-.2,'I1',color=I,fontsize=10);a.add_patch(Arc((-.9,.85),1.9,1.0,angle=0,theta1=0,theta2=360,ec=R,lw=2));arr(a,(-.9,1.35),(-.9,1.68),R);a.text(.55,1.5,'F up',color=R,fontsize=11);a.text(0,-1.55,'fast pulse launches the ring: 1.5 % efficient',color=T,fontsize=9,ha='center');return 'Coil launcher: mutual inductance gradient drives the ring skyward'
 if slug=='switch-drag':
  [a.add_patch(Arc((x,-.3),.6,1.2,angle=90,theta1=0,theta2=180,ec=I,lw=2)) for x in (-1.35,-1.05,-.75,-.45)];a.add_patch(Rectangle((.7,-.15),1.0,.55,fill=1,fc=R,ec='k'));arr(a,(.65,.12),(-.15,.12),R);a.text(.2,.55,'v',color=R,fontsize=11,ha='center');arr(a,(1.7,-.12),(2.45,-.12),T);a.text(2.0,.35,'Fd',color=T,fontsize=10);a.text(-2.5,-1.55,'drag opposes the relative motion',color=T,fontsize=9);return 'A magnet crossing a coil feels drag that peaks at v = wR/L and fades'
 if slug=='cable':
  a.add_patch(Rectangle((-2.6,-1.15),4.2,2.3,fill=0,ec=I,lw=2));a.add_patch(Rectangle((-2.6,-.45),4.2,.9,fill=1,fc='0.85',ec=I,lw=1.6));line(a,(-2.6,-1.15),(-3.0,-1.15),lw=2);line(a,(-2.6,1.15),(-3.0,1.15),lw=2);a.text(-2.95,0,'V0',color=I,fontsize=10);[a.text(x,0,r'$\otimes$',ha='center',fontsize=10) for x in (-1.6,-.6,.4,1.4)];a.text(1.7,-1.5,r"$v = 1/\sqrt{L'C'}$",color=T,fontsize=10);a.text(1.7,1.55,'dielectric',color=I,fontsize=9);return 'Coax cable: fields travel as a step at v = c/root(kappa)'
 if slug=='driven-lcr':
  line(a,(-2.4,-.9),(-2.4,.9),lw=2);line(a,(-2.4,0),(-2.75,0),lw=1.6);a.text(-3.0,0,'~',color=I,fontsize=11,ha='center');line(a,(-2.4,.9),(1.9,.9),lw=2);line(a,(-2.4,-.9),(1.9,-.9),lw=2);a.add_patch(Rectangle((-1.7,-1.05),1.1,.3,fill=1,fc=R,ec=I));a.text(-1.85,-1.32,'R',color=R,fontsize=10,ha='center');[a.add_patch(Arc((x,1.25),.9,.7,angle=0,theta1=0,theta2=180,ec=T,lw=2)) for x in (-.1,.4)];a.text(1.0,1.5,'L',color=T,fontsize=10,ha='center');line(a,(1.35,1.05),(1.35,.72),lw=2);line(a,(1.8,1.05),(1.8,.72),lw=2);a.text(2.15,1.5,'C',color=I,fontsize=10,ha='center');a.text(0,-1.72,r'$i = I_0\sin(\omega t + \phi)$ steady state',color=T,fontsize=10,ha='center');return 'Driven LCR: transient dies, steady state stays; watch near resonance'
 if slug=='maxpower':
  line(a,(-2.3,-.8),(-2.3,.8),lw=2);line(a,(-1.85,-.8),(-1.85,.8),lw=2);a.text(-2.85,0,'V',color=I,fontsize=11,ha='center');line(a,(-1.85,.8),(-.2,.8),lw=2);line(a,(-2.3,-.8),(-.2,-.8),lw=2);a.add_patch(Rectangle((-.2,-1.05),1.0,.3,fill=1,fc=R,ec=I));a.text(.3,-1.42,'Rs',color=R,fontsize=10,ha='center');line(a,(.8,.8),(2.2,.8),lw=2);line(a,(.8,-.8),(2.2,-.8),lw=2);a.add_patch(Rectangle((2.2,-.35),.55,.7,fill=0,ec=T,lw=2));a.text(2.48,-.75,'RL',color=T,fontsize=10,ha='center');line(a,(2.75,.35),(2.75,.8),lw=2);line(a,(2.75,-.35),(2.75,-.8),lw=2);a.text(0,1.55,r'$P_L$ peaks at $R_L = R_s$',color=T,fontsize=11,ha='center');return 'Matched load: half the power is lost inside the source, by design'
 if slug=='radio-wien':
  line(a,(-2.6,1.1),(-.4,1.1),lw=2);line(a,(-2.6,-1.1),(-.4,-1.1),lw=2);line(a,(-2.6,1.1),(-2.6,-1.1),lw=2);a.text(-3.05,0,'V',color=I,fontsize=10);line(a,(-.4,1.1),(-.4,.35),lw=2);a.add_patch(Rectangle((-.62,-.05),.45,.3,fill=1,fc=R,ec=I));a.text(-1.15,.15,'R',color=R,fontsize=9);line(a,(-.4,-.05),(-.4,-1.1),lw=2);line(a,(-.4,.35),(1.0,.35),lw=2);line(a,(.75,.35),(.75,.05),lw=2);line(a,(1.0,.35),(1.0,.05),lw=2);a.text(.35,-.25,'C',color=I,fontsize=9,ha='center');line(a,(1.0,.35),(1.0,1.1),lw=2);line(a,(-.4,-.45),(1.0,-.45),lw=2);a.add_patch(Rectangle((.3,-.65),.45,.3,fill=1,fc=R,ec=I));a.text(.15,-.85,'R',color=R,fontsize=9);line(a,(1.0,-.45),(1.0,-1.1),lw=2);line(a,(1.0,1.1),(2.6,1.1),lw=2);line(a,(1.0,-1.1),(2.6,-1.1),lw=2);a.text(1.9,0,r'$\beta = 1/3$',color=T,fontsize=11,ha='center');return 'Wien network: at omega RC = 1 the output is a third of the input, in phase'
 if slug=='emi-estimates':
  a.add_patch(Rectangle((-2.2,-1.1),4.4,2.2,fill=0,ec=I,lw=2));a.add_patch(Rectangle((-2.2,-1.1),.35,2.2,fill=1,fc=R,ec=I));a.add_patch(Rectangle((1.85,-1.1),.35,2.2,fill=1,fc=R,ec=I));[line(a,(-1.85,y),(1.85,y),lw=1.4,color=T,ls='--') for y in (-.55,0,.55)];a.text(0,0,r'$J = J_0 e^{-x/\delta}$',color=T,fontsize=12,ha='center');a.text(-1.05,-1.5,r'$\delta = \sqrt{2\rho/\mu\omega}$',color=I,fontsize=11);return 'Skin depth: current crowds into a thin shell; estimate before you compute'
 raise KeyError(key)
