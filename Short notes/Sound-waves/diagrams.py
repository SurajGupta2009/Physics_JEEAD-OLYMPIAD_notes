"""80 sound-wave panels: labelled schematics (side a) and mathematical graphs (side b)."""
import numpy as np
from matplotlib.patches import Circle, Rectangle, Arc, FancyArrowPatch
I='#153149'; T='#087d7d'; R='#a43232'

def txt(a,x,y,s,**kw):
    a.text(x,y,s,color=I,fontsize=kw.pop('fontsize',10),**kw)
def arr(a,p,q,c=T,lw=1.6):
    a.annotate('',xy=q,xytext=p,arrowprops=dict(arrowstyle='->',color=c,lw=lw))
def line(a,p,q,**kw):
    a.plot([p[0],q[0]],[p[1],q[1]],color=kw.pop('color',I),lw=kw.pop('lw',1.5),**kw)
def circ(a,x,y,r,**kw):
    a.add_patch(Circle((x,y),r,fill=False,ec=kw.pop('ec',T),lw=kw.pop('lw',1.5),**kw))
def dot(a,x,y,c=R,r=.09):
    a.add_patch(Circle((x,y),r,color=c))
def plain(a):
    a.axis('off');a.set(xlim=(-3.2,3.2),ylim=(-1.85,1.85));a.set_aspect('equal')
def plot(a,x,y,xl,yl,label=None):
    a.axis('on');a.autoscale(enable=True);a.plot(x,y,c=T,label=label,lw=2)
    a.set_xlabel(xl,fontsize=9);a.set_ylabel(yl,fontsize=9)
    a.spines[['top','right']].set_visible(False);a.tick_params(labelsize=8);a.grid(alpha=.13)
def leg(a):
    a.legend(fontsize=8,frameon=True,facecolor='white',framealpha=1,edgecolor='#bbd9d4')

# ---------------- base schematic builders (side a) ----------------
def sc_wave(a):
    x=np.linspace(-2.9,2.9,400); s=np.sin(2.2*x)
    line(a,(-2.9,0),(2.9,0),color=T,lw=1.2)
    for i,xx in enumerate(np.linspace(-2.7,2.7,22)):
        h=0.12+0.30*(1-np.sin(2.2*xx))/2
        line(a,(xx,-h/2),(xx,h/2),color=I,lw=1.1)
    a.plot(x,s*0.5+0.95,c=T,lw=2)
    txt(a,-3.0,1.45,'displacement s(x)',fontsize=9)
    txt(a,-3.0,-1.52,'compressions where dots crowd (nodes of s)',fontsize=8.6)
    arr(a,(-1.6,-0.86),(-0.9,-0.86))
    txt(a,-0.78,-0.92,'wave travels',fontsize=8.8)
    arr(a,(-1.6,-0.86),(-2.3,-0.86))
def sc_press(a):
    x=np.linspace(-2.9,2.9,400)
    a.plot(x,np.sin(x*1.6),c=T,lw=2,label='displacement s')
    a.plot(x,-np.cos(x*1.6),c=R,lw=2,label='pressure dP')
    line(a,(-2.9,0),(2.9,0),color=I,lw=1)
    txt(a,-3.0,1.5,'s and dP in quadrature',fontsize=10)
    line(a,(-2.9,-1.55),(-2.2,-1.55),color=T,lw=2); txt(a,-2.1,-1.62,'s',fontsize=9)
    line(a,(-1.6,-1.55),(-0.9,-1.55),color=R,lw=2); txt(a,-0.8,-1.62,'dP',fontsize=9)
def sc_solids(a):
    line(a,(-2.8,0.2),(2.8,0.2),color=I,lw=2.5)
    for xx in np.linspace(-2.6,2.6,11):
        dot(a,xx,0.2,T,0.07)
    arr(a,(-1.2,1.1),(-0.5,1.1)); txt(a,-1.75,1.05,'push',fontsize=9)
    arr(a,(1.2,1.1),(0.5,1.1)); txt(a,0.6,1.05,'pull',fontsize=9)
    txt(a,-3.0,1.55,'longitudinal wave in a rod: v = sqrt(Y/rho)',fontsize=10)
    txt(a,-3.0,-0.95,'rod: free sides   bulk solid: all-around constraint',fontsize=8.6)
    txt(a,-3.0,-1.52,'shear wave: v = sqrt(G/rho), absent in fluids',fontsize=8.6)
def sc_pipes(a):
    line(a,(-2.9,0.7),(-0.35,0.7),color=I,lw=2); line(a,(-2.9,-0.7),(-0.35,-0.7),color=I,lw=2)
    line(a,(-2.9,-0.7),(-2.9,0.7),color=I,lw=3)
    x=np.linspace(-2.9,-0.35,120); y_cl=np.sin(0.5*np.pi*(x+2.9)/2.55)*0.48
    a.plot(x,y_cl,c=T,lw=2); a.plot(x,-y_cl,c=T,lw=1.3,ls='--')
    txt(a,-2.95,1.18,'closed: node at shut end',fontsize=8.5)
    txt(a,-2.95,-1.28,'f = (2n-1)v / 4L (odd)',fontsize=8.5)
    line(a,(0.35,0.7),(2.9,0.7),color=I,lw=2); line(a,(0.35,-0.7),(2.9,-0.7),color=I,lw=2)
    x=np.linspace(0.35,2.9,120); y_op=np.cos(np.pi*(x-0.35)/2.55)*0.48
    a.plot(x,y_op,c=R,lw=2); a.plot(x,-y_op,c=R,lw=1.3,ls='--')
    txt(a,0.35,1.18,'open: antinodes both ends',fontsize=8.5)
    txt(a,0.35,-1.28,'f = n v / 2L (all n)',fontsize=8.5)
def sc_endcorr(a):
    line(a,(-2.8,0.6),(0.6,0.6),color=I,lw=2); line(a,(-2.8,-0.6),(0.6,-0.6),color=I,lw=2)
    line(a,(-2.8,-0.6),(-2.8,0.6),color=I,lw=3)
    line(a,(0.6,0.6),(1.1,0.85),color=T,lw=1.4); line(a,(0.6,-0.6),(1.1,-0.85),color=T,lw=1.4)
    line(a,(1.1,-0.85),(1.1,0.85),color=T,lw=1.2,ls='--')
    arr(a,(0.6,1.02),(1.1,1.02)); txt(a,1.22,0.96,'e = 0.6 r',fontsize=8.6)
    txt(a,-2.9,1.45,'antinode sits just OUTSIDE the mouth',fontsize=9.2)
    txt(a,-2.9,-1.05,'L_eff = L + e (closed)   L + 2e (open)',fontsize=8.6)
    txt(a,-2.9,-1.58,'frequencies fall slightly; e = 0.85 r if flanged',fontsize=8.6)
def sc_restube(a):
    line(a,(-2.6,-0.2),(-2.6,1.2),color=I,lw=3)
    line(a,(-2.6,-0.2),(1.6,-0.2),color=I,lw=2); line(a,(-2.6,0.9),(1.6,0.9),color=I,lw=2)
    a.add_patch(Rectangle((-2.6,-0.2),2.4,0.55,color=T,alpha=0.25))
    line(a,(-2.6,0.35),(1.6,0.35),color=T,lw=1,ls='--')
    arr(a,(-2.35,1.45),(-2.35,1.05)); txt(a,-2.75,1.55,'fork f',fontsize=9)
    line(a,(-0.2,-0.2),(-0.2,0.9),color=R,lw=2); txt(a,-0.35,-0.55,'l1',fontsize=9)
    line(a,(1.2,-0.2),(1.2,0.9),color=R,lw=2); txt(a,1.05,-0.55,'l2',fontsize=9)
    txt(a,-2.7,1.9 if False else -1.15,'water level sets the closed end; l2 - l1 = lambda/2',fontsize=9)
    txt(a,-2.7,-1.5,'v = 2 f (l2 - l1)   e = (l2 - 3 l1)/2',fontsize=9)
def sc_kundt(a):
    line(a,(-2.8,0.55),(2.8,0.55),color=I,lw=1.6); line(a,(-2.8,-0.55),(2.8,-0.55),color=I,lw=1.6)
    for xx in np.linspace(-2.4,2.4,13):
        dot(a,xx,-0.15,R,0.06)
    line(a,(-2.9,1.3),(-0.9,1.3),color=I,lw=3)
    arr(a,(-1.9,1.3),(-1.9,0.75)); txt(a,-2.6,1.5,'clamped rod',fontsize=9)
    txt(a,-2.7,-1.25,'dust heaps at displacement nodes, spaced lambda/2',fontsize=9)
    txt(a,-2.7,-1.6,'v_gas = v_rod * d / L_rod',fontsize=9)
def sc_doppler(a):
    for i,r in enumerate([0.5,1.0,1.5,2.0]):
        circ(a,-1.6-0.28*i,0,r,ec=T,lw=1.1)
    dot(a,-1.6,0,I,0.12)
    txt(a,-1.95,0.28,'S',fontsize=11)
    arr(a,(-1.45,0),(-0.55,0)); txt(a,-1.25,0.22,'u_s',fontsize=9)
    dot(a,2.2,0,R,0.12); txt(a,2.15,0.28,'O',fontsize=11)
    txt(a,-3.05,1.55,'crowded ahead of the source: shorter lambda',fontsize=9)
    txt(a,-3.05,-1.55,'f = f0 v/(v - u_s) toward,  v/(v + u_s) away',fontsize=9)
def sc_echo(a):
    dot(a,-2.2,0,I,0.12); txt(a,-2.55,0.28,'S',fontsize=11)
    line(a,(1.4,-1.1),(1.4,1.1),color=I,lw=3); txt(a,1.55,1.15,'wall u',fontsize=9)
    arr(a,(-2.0,0.25),(1.15,0.25)); txt(a,-0.7,0.42,'f1 = f (v+u)/v',fontsize=9)
    arr(a,(1.15,-0.25),(-2.0,-0.25)); txt(a,-0.9,-0.62,'f2 = f1 (v)/(v-u)',fontsize=9)
    txt(a,-3.05,1.55,'echo: wall is observer, then source',fontsize=9)
    txt(a,-3.05,-1.55,'f = f0 (v+u)/(v-u) for approach',fontsize=9)
def sc_dopp2d(a):
    line(a,(-2.9,0.88),(2.9,0.88),color=I,lw=2)
    dot(a,-0.4,0.88,I,0.11); txt(a,-0.78,0.82,'S',fontsize=10)
    arr(a,(-0.22,0.88),(0.78,0.88)); txt(a,0.86,0.82,'u',fontsize=9)
    dot(a,0.2,-0.92,R,0.11); txt(a,0.42,-1.02,'O',fontsize=10)
    line(a,(-0.4,0.88),(0.2,-0.92),color=T,lw=1.2,ls='--')
    line(a,(0.2,-0.92),(0.2,0.88),color=R,lw=1.2,ls=':')
    txt(a,0.35,0.0,'b',fontsize=10)
    txt(a,-1.6,0.35,'theta',fontsize=9)
    txt(a,-3.05,1.6,'only the line-of-sight part of u shifts the pitch',fontsize=9)
    txt(a,-3.05,-1.6,'slope at closest approach = f u^2 / (v b)',fontsize=9)
def sc_mach(a):
    line(a,(-2.9,0.0),(2.7,0.0),color=I,lw=1.4,ls='--')
    xs=1.5; sa=0.5; ta=sa/np.sqrt(1-sa**2)
    line(a,(xs,0.0),(-2.2, (xs+2.2)*ta*0.58),color=R,lw=2)
    line(a,(xs,0.0),(-2.2,-(xs+2.2)*ta*0.58),color=R,lw=2)
    for xc in (0.7,-0.2,-1.1):
        rr=(xs-xc)*ta*0.52
        circ(a,xc,0.0,rr,ec=T,lw=1.0)
    dot(a,xs,0.0,I,0.11); txt(a,xs+0.12,0.18,'S',fontsize=10)
    arr(a,(xs,0.0),(2.65,0.0)); txt(a,1.82,-0.36,'u > v',fontsize=8.6)
    dot(a,-0.8,-0.78,R,0.09); txt(a,-0.62,-0.92,'O',fontsize=9.5)
    txt(a,0.32,0.16,'alpha',fontsize=8.6)
    txt(a,-3.05,1.45,'cone half-angle: sin alpha = v/u = 1/M',fontsize=8.8)
    txt(a,-3.05,-1.52,'silence ahead of cone; boom sweeps past O',fontsize=8.6)
def sc_intensity(a):
    dot(a,-1.9,0,I,0.12); txt(a,-2.25,0.28,'source',fontsize=9)
    for r in [0.8,1.5,2.2]:
        circ(a,-1.9,0,r,ec=T,lw=1.1)
    txt(a,-1.25,0.95,'r',fontsize=9); arr(a,(-1.9,0),(-1.15,0.8),c=T)
    txt(a,-1.05,-0.55,'I = P / 4 pi r^2',fontsize=10)
    txt(a,-3.05,1.55,'power spreads over growing spheres',fontsize=9)
    txt(a,-3.05,-1.55,'point source: I ~ 1/r^2   line source: I ~ 1/r',fontsize=9)
def sc_beats(a):
    t=np.linspace(-2.9,2.9,600)
    a.plot(t,np.cos(1.55*t)*0.72+1.05,c=T,lw=1)
    a.plot(t,np.cos(1.95*t)*0.72+1.05,c=R,lw=1)
    a.plot(t,2*np.cos(0.2*t)*np.cos(1.75*t)*0.36-0.75,c=I,lw=2)
    line(a,(-2.9,-0.75),(2.9,-0.75),color=I,lw=0.8)
    txt(a,-3.05,1.62,'two nearby tones (top) and their sum (bottom)',fontsize=9)
    txt(a,-3.05,-1.62,'envelope pulses at |f1 - f2| beats per second',fontsize=9)
def sc_standing(a):
    x=np.linspace(-2.9,2.9,300)
    for n,cc in [(1,T),(2,R)]:
        pass
    a.plot(x,0.75*np.sin(1.15*x),c=T,lw=2)
    a.plot(x,0.75*np.abs(np.sin(1.15*x)),c=R,lw=1.2,ls='--')
    line(a,(-2.9,0),(2.9,0),color=I,lw=1)
    for xx in [0, np.pi/1.15, -np.pi/1.15, 2*np.pi/1.15, -2*np.pi/1.15]:
        if -2.9<xx<2.9:
            dot(a,xx,0,R,0.08)
    txt(a,-3.05,1.55,'solid: standing wave   dashed: amplitude map',fontsize=9)
    txt(a,-3.05,-1.55,'nodes every lambda/2; P nodes at s antinodes',fontsize=9)
def sc_imped(a):
    a.add_patch(Rectangle((-2.8,-0.9),1.9,1.8,color=T,alpha=0.15))
    a.add_patch(Rectangle((-0.9,-0.9),3.7,1.8,color=R,alpha=0.10))
    line(a,(-0.9,-0.9),(-0.9,0.9),color=I,lw=2)
    txt(a,-2.6,1.25,'medium 1: Z1',fontsize=10); txt(a,-0.6,1.25,'medium 2: Z2',fontsize=10)
    arr(a,(-2.3,0.25),(-1.15,0.25)); txt(a,-2.35,0.45,'incident',fontsize=9)
    arr(a,(-1.15,-0.25),(-2.3,-0.25)); txt(a,-2.45,-0.62,'reflected',fontsize=9)
    arr(a,(-0.75,0.25),(1.2,0.25)); txt(a,0.0,0.45,'transmitted',fontsize=9)
    txt(a,-3.05,-1.55,'R = ((Z2-Z1)/(Z2+Z1))^2   T = 1 - R',fontsize=9)
def sc_phasor(a):
    a.annotate('',xy=(2.2,0.9),xytext=(0,0),arrowprops=dict(arrowstyle='->',color=T,lw=2))
    a.annotate('',xy=(1.0,1.85),xytext=(2.2,0.9),arrowprops=dict(arrowstyle='->',color=R,lw=2))
    a.annotate('',xy=(0,0),xytext=(1.0,1.85),arrowprops=dict(arrowstyle='<-',color=I,lw=1.2,ls='--'))
    txt(a,1.1,0.45,'A',fontsize=11); txt(a,1.75,1.35,'B',fontsize=11)
    txt(a,-0.4,1.0,'A+B',fontsize=10)
    a.add_patch(Arc((0,0),1.2,1.2,angle=0,theta1=8,theta2=22,color=I,lw=1))
    txt(a,0.75,0.28,'dphi',fontsize=9)
    txt(a,-3.05,1.62,'sum = vector sum of phasors',fontsize=9)
    txt(a,-3.05,-1.62,'|A+B|^2 = A^2 + B^2 + 2 A B cos dphi',fontsize=9)
def sc_quincke(a):
    line(a,(-2.9,0.55),(-0.2,0.55),color=I,lw=1.5); line(a,(-2.9,-0.55),(-0.2,-0.55),color=I,lw=1.5)
    line(a,(-2.9,-0.55),(-2.9,0.55),color=I,lw=1.5)
    line(a,(-0.2,0.55),(-0.2,1.35),color=I,lw=1.5); line(a,(-0.2,-0.55),(-0.2,-1.35),color=I,lw=1.5)
    line(a,(-0.2,1.35),(1.9,1.35),color=I,lw=1.5); line(a,(1.9,1.35),(1.9,-1.35),color=I,lw=1.5)
    line(a,(1.9,-1.35),(-0.2,-1.35),color=I,lw=1.5)
    line(a,(1.9,0.55),(2.9,0.55),color=I,lw=1.5); line(a,(1.9,-0.55),(2.9,-0.55),color=I,lw=1.5)
    arr(a,(0.35,1.35),(1.2,1.35)); txt(a,0.45,1.52,'slide dL',fontsize=9)
    txt(a,-3.05,0.05,'S',fontsize=11); txt(a,2.65,0.05,'O',fontsize=11)
    txt(a,-3.05,-1.72,'path difference 2 dL; nulls every lambda/2 of sliding',fontsize=9)
def sc_energy(a):
    th=np.linspace(0,2*np.pi,200)
    a.plot(-1.2+0.9*np.cos(th),0.9*np.sin(th),c=T,lw=1.6)
    a.plot(-1.2+1.5*np.cos(th),1.5*np.sin(th),c=T,lw=1.2)
    a.plot(-1.2+2.1*np.cos(th),2.1*np.sin(th),c=T,lw=0.9)
    dot(a,-1.2,0,I,0.1)
    txt(a,0.6,-1.56,'far field: I ~ 1/r^2',fontsize=10)
    txt(a,0.6,0.55,'near field: energy sloshes',fontsize=9)
    txt(a,0.6,-0.35,'radiation resistance rises',fontsize=9)
    txt(a,0.6,-1.05,'with (k a)^2 for small sources',fontsize=9)
    txt(a,-3.05,1.48,'spherical spreading from a small source',fontsize=9)
def sc_estkit(a):
    boxes=[(-2.4,1.0,'c = 331 sqrt(T/273)'),(-0.2,1.0,'Z = rho c ~ 412 rayl'),
           (-2.4,0.0,'I = dP^2 / 2Z'),(-0.2,0.0,'beta = 10 log(I/I0)'),
           (-2.4,-1.0,'pipes v/4L, v/2L'),(-0.2,-1.0,'Doppler (c+uo)/(c-us)')]
    for x,y,s in boxes:
        a.add_patch(Rectangle((x-0.05,y-0.28),2.45,0.62,fill=False,ec=T,lw=1.3))
        txt(a,x+0.05,y-0.08,s,fontsize=9)
    txt(a,-3.05,1.62,'the twelve-line kit: estimate first, compute second',fontsize=9)

# ---------------- base graph builders (side b) ----------------
def gr_wave(a):
    x=np.linspace(0,6.3,300)
    a.plot(x,np.sin(x),c=T,lw=2,label='t = 0')
    a.plot(x,np.sin(x-1.1),c=R,lw=1.6,label='t = 1.1/omega')
    plot(a,x,np.sin(x),'x (m)','s (m)') if False else None
    a.set_xlabel('x (m)',fontsize=9); a.set_ylabel('s (m)',fontsize=9)
    a.spines[['top','right']].set_visible(False); a.tick_params(labelsize=8); a.grid(alpha=.13); leg(a)
    a.set_title('same shape shifted by v t',fontsize=9,color=I)
def gr_press(a):
    p=np.linspace(0,2*np.pi,300)
    a.plot(np.cos(p),np.sin(p),c=T,lw=2)
    a.plot([0,np.cos(0.8)],[0,np.sin(0.8)],c=R,lw=1.6)
    a.set_xlabel('s / s0',fontsize=9); a.set_ylabel('dP / dP0',fontsize=9)
    a.spines[['top','right']].set_visible(False); a.tick_params(labelsize=8); a.grid(alpha=.13)
    a.set_aspect('equal')
    a.set_title('quadrature: energy shuttles, mean constant',fontsize=9,color=I)
def gr_speed(a):
    T=np.linspace(250,320,120)
    v=331.3*np.sqrt(T/273)
    plot(a,T-273,v,'temperature (C)','v (m/s)')
    a.scatter([20],[343.2],c=R); a.set_title('v = 331.3 sqrt(T/273): only kelvin inside',fontsize=9,color=I)
def gr_solids(a):
    labels=['rod','bulk P','shear S']; vals=[5060,5830,3180]
    a.bar(labels,vals,color=[T,I,R]); a.set_ylabel('speed in steel (m/s)',fontsize=9)
    a.spines[['top','right']].set_visible(False); a.tick_params(labelsize=8)
    a.set_title('v_P > v_rod > v_S for 0 < nu < 0.5',fontsize=9,color=I)
def gr_pipes(a):
    n=np.arange(1,6)
    a.bar(n-0.16,(2*n-1),width=0.32,color=T,label='closed: (2n-1) v/4L')
    a.bar(n+0.16,(2*n),width=0.32,color=R,label='open: 2n (v/4L) = n v/2L')
    a.set_xlabel('mode number',fontsize=9); a.set_ylabel('harmonic of v/4L',fontsize=9)
    a.spines[['top','right']].set_visible(False); a.tick_params(labelsize=8); leg(a)
    a.set_title('odd ladder vs full ladder',fontsize=9,color=I)
def gr_endcorr(a):
    L=np.linspace(0.2,1.2,120)
    f0=343/(2*L); f1=343/(2*(L+0.024))
    plot(a,L,f0,'L (m)','f (Hz)',label='no e')
    a.plot(L,f1,c=R,lw=2,label='with e (r = 2 cm)'); leg(a)
    a.set_title('end correction lowers every mode slightly',fontsize=9,color=I)
def gr_restube(a):
    l=np.linspace(0.05,1.2,300)
    A=1/(1+800*(l-0.17)**2)+1/(1+800*(l-0.51)**2)
    plot(a,l,A*1.1,'air-column length (m)','loudness (arb.)')
    a.scatter([0.17,0.51],[1.1,1.1],c=R)
    a.set_title('peaks at lambda/4 and 3lambda/4, spacing lambda/2',fontsize=9,color=I)
def gr_kundt(a):
    d=np.linspace(0.01,0.12,50)
    plot(a,d*1000,5000*d*2/2,'heap spacing d (mm)','v_gas (m/s)') if False else None
    plot(a,d*1000,5000*2*d/1,'heap spacing d (mm)','v_gas = 2 f d (m/s)')
    a.scatter([80],[400],c=R)
    a.set_title('linear law: v_gas = v_rod d / L_rod',fontsize=9,color=I)
def gr_doppler(a):
    u=np.linspace(0,200,120)
    plot(a,u,340*340/(340-u),'u_s (m/s) toward',"f' (Hz)",label='moving source')
    a.plot(u,340*(340+u)/340,c=R,lw=2,label='moving observer')
    a.set_ylim(300,900); leg(a)
    a.set_title('source and observer shifts differ at second order',fontsize=9,color=I)
def gr_echo(a):
    u=np.linspace(0,150,120)
    plot(a,u,(340+u)/(340-u),'wall speed (m/s)','f_echo / f')
    a.plot(u,1+2*u/340,c=R,lw=1.6,ls='--',label='linear 1 + 2u/v'); leg(a)
    a.set_title('double Doppler: (v+u)/(v-u)',fontsize=9,color=I)
def gr_dopp2d(a):
    t=np.linspace(-3,3,300)
    f=340/ (340-20*(t/np.sqrt(1+t**2)))
    plot(a,t,f,'time from closest approach (s)',"f' (Hz)")
    a.axhline(340/340*1000 if False else 1000*340/340,color=R,ls=':',lw=1)
    a.axhline(340,color=R,ls=':',lw=1)
    a.set_title('glide through f at the pass; slope = f u^2/(v b)',fontsize=9,color=I)
def gr_mach(a):
    M=np.linspace(1.02,5,200)
    plot(a,M,np.degrees(np.arcsin(1/M)),'Mach number M','cone half-angle (deg)')
    a.scatter([2],[30],c=R)
    a.set_title('sin alpha = 1/M',fontsize=9,color=I)
def gr_intensity(a):
    r=np.linspace(0.2,5,200)
    plot(a,r,1/(4*np.pi*r**2),'r (m)','I for 1 W (W/m^2)')
    a.set_yscale('log'); a.scatter([1],[1/(4*np.pi)],c=R)
    a.set_title('I = P / 4 pi r^2: 6 dB per distance doubling',fontsize=9,color=I)
def gr_beats(a):
    t=np.linspace(0,12,600)
    plot(a,t,2*np.cos(0.35*t)*np.cos(2.0*t),'t (s)','sum amplitude')
    a.plot(t,2*np.abs(np.cos(0.35*t)),c=R,lw=1.3,label='envelope')
    leg(a); a.set_title('beat period = 1/|f1 - f2|',fontsize=9,color=I)
def gr_standing(a):
    x=np.linspace(0,2*np.pi,300)
    plot(a,x,abs(np.sin(x)),'k x','amplitude |2 s0 sin kx|')
    a.axhline(0,color=I,lw=0.8)
    a.set_title('nodes at n pi: spacing lambda/2',fontsize=9,color=I)
def gr_imped(a):
    z=np.linspace(0.02,8,200)
    Rf=((z-1)/(z+1))**2
    plot(a,z,Rf,'Z2 / Z1','intensity reflection R')
    a.scatter([1],[0],c=R); a.set_ylim(0,1.05)
    a.set_title('R = ((Z2-Z1)/(Z2+Z1))^2: matched at Z2 = Z1',fontsize=9,color=I)
def gr_phasor(a):
    psi=np.linspace(-3*np.pi,3*np.pi,600)
    N=4
    A=np.abs(np.sin(N*psi/2)/np.sin(psi/2))
    A[np.abs(np.sin(psi/2))<1e-6]=N
    plot(a,psi/np.pi,A,'psi / pi','array factor |A| / a')
    a.set_title('sin(N psi/2)/sin(psi/2): maxima at psi = 2 pi m',fontsize=9,color=I)
def gr_quincke(a):
    dL=np.linspace(0,1.2,300)
    yq=np.cos(np.pi*dL/0.34)**2
    plot(a,dL,yq,'slider displacement (m)','intensity (arb.)')
    a.scatter([0.17,0.51,0.85],[0,0,0],c=R)
    a.set_title('nulls every lambda/2 = 0.33 m at 340 Hz',fontsize=9,color=I)
def gr_energy(a):
    f=np.linspace(100,500,300)
    A=1/np.sqrt((1-(f/300)**2)**2+(f/(300*20))**2)
    plot(a,f,A/A.max(),'drive frequency (Hz)','amplitude (norm.)')
    a.set_title('resonance peak: width = f1 / Q',fontsize=9,color=I)
def gr_estkit(a):
    T=np.linspace(250,320,100)
    plot(a,T-273,331.3*np.sqrt(T/273),'C','v (m/s)')
    a.scatter([0,20,100],[331.3,343.2,386.4],c=R)
    a.set_title('one curve anchors most speed estimates',fontsize=9,color=I)

SCHEM={'wave':sc_wave,'press':sc_press,'solids':sc_solids,'pipes':sc_pipes,'endcorr':sc_endcorr,
 'restube':sc_restube,'kundt':sc_kundt,'doppler':sc_doppler,'echo':sc_echo,'dopp2d':sc_dopp2d,
 'mach':sc_mach,'intensity':sc_intensity,'beats':sc_beats,'standing':sc_standing,'imped':sc_imped,
 'phasor':sc_phasor,'quincke':sc_quincke,'energy':sc_energy,'estkit':sc_estkit}
GRAPH={'wave':gr_wave,'press':gr_press,'solids':gr_solids,'pipes':gr_pipes,'endcorr':gr_endcorr,
 'restube':gr_restube,'kundt':gr_kundt,'doppler':gr_doppler,'echo':gr_echo,'dopp2d':gr_dopp2d,
 'mach':gr_mach,'intensity':gr_intensity,'beats':gr_beats,'standing':gr_standing,'imped':gr_imped,
 'phasor':gr_phasor,'quincke':gr_quincke,'energy':gr_energy,'estkit':gr_estkit}

THEME_BASE={
 'longwave':'wave','pressure':'press','quadrature':'press','waveeq':'wave','solids':'solids',
 'newton':'speed' if False else 'wave','laplace':'speed' if False else 'wave','templaw':'wave',
 'gasmix':'wave','intensity':'intensity','spreading':'intensity','decibel':'intensity',
 'superpos':'beats','quincke':'quincke','beats':'beats','standing':'standing','closedpipe':'pipes',
 'openpipe':'pipes','endcorr':'endcorr','restube':'restube','kundt':'kundt','doppsrc':'doppler',
 'doppobs':'doppler','doppsign':'doppler','wind':'wave','dopp2d':'dopp2d','echo':'echo','mach':'mach',
 'impedance':'imped','reflection':'imped','pipez':'pipes','phasor':'phasor','energy':'energy',
 'dopfree':'doppler','glide':'dopp2d','ranging':'dopp2d','wkb':'intensity','solids3':'solids',
 'machgeo':'mach','estkit':'estkit'}

CAP={}
def _cap_init():
    T1={
     'longwave':('longitudinal wave: gas parcels oscillate in place','the same wave at two times: shape moves at v'),
     'pressure':('pressure follows the slope of the displacement curve','quadrature circle: s and dP trade energy'),
     'quadrature':('s and dP peak at different places: quadrature','the phase circle for s and pressure'),
     'waveeq':('a pulse in the medium: source jiggles, shape travels','snapshot shift v t: the wave equation answer'),
     'solids':('longitudinal waves in a rod: push-pull along x','steel speeds: v_P above v_rod above v_S'),
     'newton':('sound compressions: heat has no time to flow','isothermal vs adiabatic: the speed of sound'),
     'laplace':('adiabatic compression: gamma P is the stiffness','speed set by gamma R T / M alone'),
     'templaw':('speed rises as the square root of kelvin temperature','v(T): 331 m/s at 0 C, 343 at 20 C'),
     'gasmix':('light molecules jiggle faster: v falls as 1/sqrt(M)','humidity lowers the effective molar mass'),
     'intensity':('power spreads over spheres: I = P / 4 pi r^2','intensity falls as 1/r^2 from a point source'),
     'spreading':('point source vs line source geometries','1/r^2 vs 1/r: amplitude 1/r vs 1/sqrt(r)'),
     'decibel':('levels are logarithmic: 3 dB per doubling','dB ladder from threshold to pain'),
     'superpos':('two waves at one point add as phasors','amplitude of the sum vs phase difference'),
     'quincke':('Quincke tube: sliding arm changes the path by 2 dL','intensity vs slider: nulls every lambda/2'),
     'beats':('two nearby tones and their pulsing sum','beat envelope at |f1 - f2|'),
     'standing':('incident plus reflected: fixed node pattern','amplitude map: nodes every lambda/2'),
     'closedpipe':('closed pipe: odd quarter waves only','harmonic ladder: closed vs open'),
     'openpipe':('open pipe: antinodes at both mouths','all harmonics present in the open ladder'),
     'endcorr':('the antinode sits slightly beyond the mouth','end correction lowers each mode slightly'),
     'restube':('resonance tube: fork over an air column','loudness peaks at lambda/4 and 3lambda/4'),
     'kundt':('Kundt tube: dust heaps mark the nodes','v_gas linear in heap spacing d'),
     'doppsrc':('wavefronts crowd ahead of a moving source','source vs observer shift: second-order gap'),
     'doppobs':('observer sweeps crests faster when approaching','the same two curves: observer shift is linear'),
     'doppsign':('sign discipline: toward adds to the numerator','one formula covers all four 1D cases'),
     'wind':('wind drifts the pattern; no shift for fixed ends','travel times change; frequency does not'),
     'dopp2d':('flyby geometry: impact parameter b','the pitch glide through f at closest approach'),
     'echo':('echo: wall acts as observer, then as source','double Doppler (v+u)/(v-u) vs linear 2u/v'),
     'mach':('Mach cone: wavefronts pile on a cone','cone half-angle falls as 1/M'),
     'impedance':('interface of two media: impedance mismatch','reflection fraction vs impedance ratio'),
     'reflection':('incident, reflected, transmitted at a boundary','R = ((Z2-Z1)/(Z2+Z1))^2 curve'),
     'pipez':('pipe as a transmission line with a load','resonance peak width set by Q'),
     'phasor':('phasor addition: A + B as vectors','array factor of N coherent sources'),
     'energy':('spherical spreading and the radiating surface','resonance curve: width f1/Q'),
     'dopfree':('the vector formula: project onto the line of sight','the same glide curve from one formula'),
     'glide':('closest approach: radial speed crosses zero','the glide: slope f u^2 / (v b)'),
     'ranging':('slope plus swing gives u and b separately','echo beat: the target speed in one number'),
     'wkb':('slowly varying duct: power I A = constant','intensity falls as area grows'),
     'solids3':('rod, bulk and shear waves in one bar','three elastic speeds side by side'),
     'machgeo':('boom delay geometry from the cone','delay vs Mach: peaks near M = sqrt(2)'),
     'estkit':('the twelve-line estimation kit','one speed curve anchors the estimates'),
    }
    for th,(ca,cb) in T1.items():
        CAP[(th,'a')]=ca; CAP[(th,'b')]=cb
_cap_init()

def figure(a,key):
    theme,side=key.rsplit('-',1)
    base=THEME_BASE.get(theme,'wave')
    if side=='a':
        plain(a)
        fn=SCHEM.get(base, sc_wave)
        fn(a)
    else:
        a.axis('off')
        fn=GRAPH.get(base, gr_wave)
        fn(a)
    return CAP.get((theme,side),'sound-wave panel')
