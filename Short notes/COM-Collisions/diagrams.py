"""COM & collision panels: labelled schematics and compact diagnostic graphs."""
import numpy as np
from matplotlib.patches import Circle, Rectangle
I='#153149'; T='#087d7d'; R='#a43232'

def txt(a,x,y,s,**kw): a.text(x,y,s,color=I,fontsize=kw.pop('fontsize',9),**kw)
def arr(a,p,q,c=T): a.annotate('',xy=q,xytext=p,arrowprops=dict(arrowstyle='->',color=c,lw=1.6))
def line(a,p,q,**kw): a.plot([p[0],q[0]],[p[1],q[1]],color=kw.pop('color',I),lw=kw.pop('lw',1.5),**kw)
def circ(a,x,y,r,ec=T): a.add_patch(Circle((x,y),r,fill=False,ec=ec,lw=1.6))
def dot(a,x,y,c=R,r=.08): a.add_patch(Circle((x,y),r,color=c))
def plain(a): a.axis('off');a.set(xlim=(-3.1,3.1),ylim=(-1.8,1.8));a.set_aspect('equal')
def graph(a,x,y,xlab,ylab,label=None):
    a.axis('on');a.plot(x,y,color=T,lw=2,label=label);a.set_xlabel(xlab,fontsize=8);a.set_ylabel(ylab,fontsize=8)
    a.spines[['top','right']].set_visible(False);a.tick_params(labelsize=7);a.grid(alpha=.13)
    if label:a.legend(fontsize=7,loc='best',framealpha=.9)

def schematic(a,key):
    txt(a,-2.9,1.55,SCHEM[key][0],fontsize=9)
    if key=='bodies':
        line(a,(-2.5,-.8),(-1.1,-.8));txt(a,-2.5,-1.2,'rod: COM at L/2')
        circ(a,-.2,.1,.55);dot(a,-.2,.1);txt(a,-.9,1.0,'ring: centre')
        circ(a,1.7,.1,.7);dot(a,1.7,-.15);txt(a,1.15,1.0,'disc: centre')
        txt(a,-2.8,-1.55,'symmetry pins the red COM dots')
    elif key=='hole':
        circ(a,-.5,0,1.35);circ(a,.55,.45,.5,R);dot(a,-.5,0,T,.07);arr(a,(.55,.45),(1.45,1.1),R)
        txt(a,-2.2,-1.45,'negative hole shifts COM away')
    elif key in ('explosion','recoil'):
        dot(a,0,0);arr(a,(0,0),(-2,1),T);arr(a,(0,0),(2,1),T);arr(a,(0,0),(0,-1.4),R)
        txt(a,-2.8,1.3,'m1 v1');txt(a,1.6,1.3,'m2 v2');txt(a,.2,-1.5,'m3 v3')
        txt(a,-2.8,-1.55,'vector momenta sum to M v_cm')
    elif key in ('impulse','impapprox'):
        circ(a,-1.7,.15,.4);line(a,(.7,-1.2),(.7,1.2),lw=2.4);arr(a,(-1.2,.15),(.55,.15),R)
        txt(a,-2.7,.95,'ball m, speed u');txt(a,.95,.8,'wall');txt(a,-2.7,-1.3,'J = area under F(t)')
    elif key in ('classify','coll1d','collcases'):
        circ(a,-1.8,.2,.34);circ(a,-.95,.2,.34,R);arr(a,(-2.7,.2),(-2.15,.2));arr(a,(-.6,.2),(.15,.2),R)
        txt(a,.45,.35,'line of impact');txt(a,-2.7,-.75,'approach u1-u2');txt(a,.4,-.75,'separate at e times speed')
        line(a,(-2.8,-1.2),(2.8,-1.2),ls=':',lw=1)
    elif key in ('eloss','defo','traps'):
        for x,c in [(-1.8,T),(-.7,'#b7950b'),(.4,R)]:a.add_patch(Rectangle((x,-.7),.62,1.5,fc=c,ec='none',alpha=.4))
        txt(a,-1.85,1.05,'K_cm');txt(a,-.78,1.05,'e^2 K_rel');txt(a,.35,1.05,'lost');arr(a,(-1.05,0),(.25,0))
        txt(a,-2.7,-1.3,'K_loss = (1-e^2) K_rel')
    elif key in ('oblique','ninety','scatter'):
        circ(a,-1.6,.4,.35);circ(a,.1,-.1,.35,R);arr(a,(-1.15,.32),(-.38,.05));line(a,(-2.4,-1.2),(2.5,1.4),ls=':',lw=1.3)
        arr(a,(.4,.05),(1.5,1.0));arr(a,(.4,-.25),(1.5,-1.15),R)
        txt(a,-2.8,-1.55,'normal changes; tangent survives')
    elif key=='pendulum':
        line(a,(-1.4,1.35),(-1.4,.3));a.add_patch(Rectangle((-1.65,.0),.5,.45,fc=T,ec='none',alpha=.45));dot(a,-1.4,.22,R,.1)
        txt(a,-2.9,-.55,'1 collision: momentum');arr(a,(.8,.4),(1.7,1.15),R);txt(a,.1,-.8,'2 swing: energy')
    elif key=='spring':
        a.add_patch(Rectangle((-2.4,-.35),.7,.7,fc=T,ec='none',alpha=.4));a.add_patch(Rectangle((1.4,-.35),.7,.7,fc=R,ec='none',alpha=.4))
        for k in range(8):line(a,(-1.7+k*.39,-.2 if k%2 else .2),(-1.31+k*.39,.2 if k%2 else -.2),lw=1)
        arr(a,(-1,0),(1.2,0));txt(a,-2.6,-1.0,'collision then spring energy')
    elif key=='cmframe':
        arr(a,(-2,-.4),(-.35,-.4));arr(a,(-.25,-.4),(.9,.65));arr(a,(-.25,-.4),(.9,-1.25),R)
        txt(a,-1.45,-.1,'v_cm');txt(a,1.0,.8,'v1 = v_cm + v1*');txt(a,1.0,-1.5,'v2 = v_cm + v2*')
    elif key in ('belt','hopper'):
        line(a,(-2.5,-.3),(2.5,-.3),lw=2.4);arr(a,(-2,-.3),(2,-.3));txt(a,-.8,.1,'belt speed v')
        for x in [-1.7,-.7,.3,1.3]:dot(a,x,.9,R,.07)
        txt(a,-2.8,1.35,'sand arrives with zero horizontal speed');txt(a,-2.7,-1.2,'F = m_dot v; loading slows cart')
    elif key=='rocket':
        a.add_patch(Rectangle((-.8,-.45),1.4,.9,fc=T,ec='none',alpha=.4));arr(a,(-1,0),(-2.6,0),R);arr(a,(.8,0),(2.5,0))
        txt(a,-1.0,.8,'rocket m,v');txt(a,-2.9,.35,'exhaust');txt(a,1.3,.35,'thrust');txt(a,-2.8,-1.3,'m dv = -v_e dm')
    elif key=='flux':
        line(a,(-2.2,1.2),(-2.2,-1.2),lw=2.3)
        for y in [-.8,-.25,.3,.85]:circ(a,-2.2,y,.1,R)
        arr(a,(-1.8,.65),(-.6,.65));txt(a,-.5,.8,'incoming v');txt(a,-2.7,-1.5,'weight + momentum flux')
    elif key=='boat':
        a.add_patch(Rectangle((-2.2,-.55),1.5,.38,fc=T,ec='none',alpha=.4));a.add_patch(Rectangle((.5,-.55),1.5,.38,fc=T,ec='none',alpha=.4))
        dot(a,-1.2,-.15);dot(a,1.5,-.15);arr(a,(-.5,.3),(.4,.3));arr(a,(.4,-.1),(-.5,-.1),R)
        txt(a,-2.8,1.0,'horizontal COM stays fixed');txt(a,-2.8,-1.3,'man walks d; boat recoils')
    elif key=='bounces':
        line(a,(-2.8,-1.15),(2.8,-1.15),lw=1.8)
        for i,h in enumerate([1.4,1.0,.62,.35]):line(a,(-2.2+i*1.25,-1.1),(-2.2+i*1.25,-1.1+h),color=R,lw=2)
        txt(a,-2.8,1.45,'height ratio = e^2');txt(a,-2.7,-1.55,'geometric bounce ladder')
    elif key in ('wall','platform'):
        line(a,(.2,-1.25),(.2,1.25),lw=2.4);circ(a,-1.7,.35,.35);arr(a,(-1.15,.35),(-.15,.35));arr(a,(.15,1.0),(-.7,1.0),R)
        txt(a,-2.8,1.5,'use speed relative to wall');txt(a,-2.8,-1.3,'v_after - v_w = -e(v_before-v_w)')
    elif key=='chain3':
        line(a,(-2.5,-1.15),(2.4,-1.15),lw=2.2)
        a.add_patch(Rectangle((-1.15,-1.05),1.9,.23,fc=T,ec='none',alpha=.35))
        for i in range(5):dot(a,-1.45+i*.12,1.08-i*.39,R,.07)
        arr(a,(-.45,-.35),(-.45,-.88),R)
        txt(a,.15,.65,'v = sqrt(2gx)');txt(a,.9,-.7,'landed weight + flux')
    elif key=='fold':
        line(a,(-2.7,.7),(-.3,.7),lw=2.2);line(a,(-.3,.7),(-.3,1.05),lw=2.2)
        a.plot([-.3,-.3,.45,.45],[1.05,-.8,-.8,1.05],color=R,lw=2)
        arr(a,(.8,.45),(.8,-.55));txt(a,1.0,-.65,'y');txt(a,-2.6,-1.3,'both hanging strands share speed v')
    elif key=='peg':
        circ(a,0,1.0,.28);line(a,(-.18,.85),(-1.55,-.65),lw=2);line(a,(.18,.85),(1.5,-.65),lw=2)
        for i in range(4):dot(a,-.48-i*.24,.5-i*.26,R,.065)
        for i in range(2):dot(a,.45+i*.35,.58-i*.27,R,.065)
        txt(a,-2.6,-1.25,'lengths x and L-x; a = g(2x-L)/L')
    elif key=='staging':
        for x,c in [(-2.2,T),(-.7,'#b7950b'),(.8,R)]:a.add_patch(Rectangle((x,-.5),.9,1.0,fc=c,ec='none',alpha=.4))
        arr(a,(-1.2,0),(-.8,0));arr(a,(.3,0),(.7,0));txt(a,-2.7,1.35,'burn, discard, burn');txt(a,-2.7,-1.2,'mass ratio resets at each stage')
    elif key=='jet':
        line(a,(-2.7,.55),(-.65,.55),lw=3,color=T);a.add_patch(Rectangle((-.5,-.7),.18,1.5,fc=R,ec='none',alpha=.5))
        arr(a,(-2.5,.55),(-.65,.55));arr(a,(.1,-.8),(.1,.5),R);txt(a,.4,.5,'plate u');txt(a,-2.7,-1.3,'F = rho A (v-u)^2')
    elif key=='relativ':
        circ(a,-1.4,.2,.35);arr(a,(-2.6,.2),(-1.85,.2));txt(a,-2.6,.8,'particle v');txt(a,-.4,.4,'p = gamma m v');txt(a,-.4,-.3,'gamma = 1/sqrt(1-v^2/c^2')
    elif key in ('route','ledger','integrate'):
        txt(a,-2.8,1.35,'choose system and time window');txt(a,-2.8,.65,'COM -> definition / symmetry');txt(a,-2.8,.05,'collision -> momentum + e');txt(a,-2.8,-.55,'flux -> m_dot times delta v');txt(a,-2.8,-1.25,'audit signs, energy, limits')

def graph_panel(a,key):
    x=np.linspace(0,1,200)
    if key in ('bodies','boat'):
        graph(a,x,x/(.25+x),'mass ratio','COM fraction','weighted average')
    elif key=='hole':
        r=np.linspace(.02,.9,200);graph(a,r,-.5*r*r/(1-r*r),'hole radius r','COM shift','negative mass')
    elif key in ('explosion','recoil'):
        m=np.linspace(.4,5,200);graph(a,m,6/m,'fragment mass m','speed p/m','fixed momentum')
    elif key in ('impulse','impapprox'):
        t=np.linspace(0,1,200);f=np.where(t<.5,80*t,80*(1-t));graph(a,t,f,'contact time','force F','pulse area = J');a.fill_between(t,0,f,color=T,alpha=.18)
    elif key in ('classify','coll1d','collcases'):
        e=np.linspace(0,1,200);graph(a,e,e,'approach speed (scaled)','separation speed','e = 1');a.plot(e,.6*e,color=R,ls='--',label='e = 0.6');a.legend(fontsize=7)
    elif key in ('eloss','defo','traps'):
        e=np.linspace(0,1,200);graph(a,e,1-e**2,'restitution e','K_loss / K_rel','1 - e^2')
    elif key in ('oblique','ninety','scatter'):
        th=np.linspace(0,np.pi/2,200);graph(a,np.degrees(th),np.cos(th),'deflection angle (deg)','v1/u','equal-mass elastic')
    elif key=='pendulum':
        v=np.linspace(0,5,200);graph(a,v,v*v/20,'shared speed V','rise h','V^2 / 2g')
    elif key=='spring':
        m=np.linspace(.05,5,200);graph(a,m,2*np.sqrt(1/(m+1)),'shooter mass m','x_el / x_in','boundary m = 3M');a.axhline(1,color=R,ls='--')
    elif key=='cmframe':
        th=np.linspace(0,2*np.pi,200);graph(a,1+.5*np.cos(th),.5*np.sin(th),'v1x','v1y','CM circle locus');a.set_aspect('equal')
    elif key in ('belt','hopper'):
        t=np.linspace(0,10,200);graph(a,t,5/(1+.05*t),'time t','cart speed v','loading slows cart')
    elif key=='rocket':
        r=np.linspace(1,20,200);graph(a,r,np.log(r),'mass ratio m0/mf','delta v / v_e','ln(m0/mf)')
    elif key=='flux':
        z=np.linspace(0,1,200);graph(a,z,3*z,'landed length x','scale force','3 lambda x g')
    elif key=='bounces':
        n=np.arange(0,8);graph(a,n,.8**n,'bounce n','speed ratio','e^n');a.plot(n,.8**(2*n),color=R,label='height ratio e^(2n)');a.legend(fontsize=7)
    elif key in ('wall','platform'):
        v=np.linspace(-5,10,200);graph(a,v,-5-.8*(v+5),'incident lab v','outgoing lab v','moving-wall law')
    elif key=='chain3':
        z=np.linspace(0,1,200);graph(a,z,3*z,'landed length / L','force / mg','three-times-weight')
    elif key=='peg':
        z=np.linspace(.5,1,200);graph(a,z,1-2*(2*z-1)**2,'long side x / L','peg force / mg','contact falls to zero');a.axhline(0,color=R,ls='--')
    elif key=='staging':
        n=np.arange(1,6);graph(a,n,np.log(1+n*.65),'number of stages','delta v (scaled)','staging gain')
    elif key=='jet':
        u=np.linspace(0,1,200);graph(a,u,(1-u)**2*u,'plate speed u/v','power / (rho A v^3)','peak at u = 1/3');a.axvline(1/3,color=R,ls='--')
    elif key=='fold':
        y=np.linspace(0,1,200);graph(a,y,y*y,'fold depth y / L','v^2 / (gL)','energy: v^2 = 2gy^2/L')
    elif key=='relativ':
        v=np.linspace(0,.95,200);graph(a,v,1/np.sqrt(1-v*v),'speed v/c','gamma','relativistic correction')
    else:
        t=np.linspace(0,1,200);graph(a,t,t*t,'position x','response','diagnostic curve')

SCHEM={k:(k,) for k in ['bodies','hole','explosion','impulse','recoil','classify','eloss','defo','oblique','pendulum','spring','cmframe','belt','rocket','flux','boat','bounces','wall','chain3','scatter','peg','staging','jet','fold','relativ','hopper','route','ledger','integrate','impapprox','platform','coll1d','collcases','ninety','traps']}
SCHEM.update({'bodies':('COM markers for standard symmetric bodies',),'hole':('cut material is a negative-mass patch',),'explosion':('fragments recoil around fixed COM motion',),'impulse':('contact pulse transfers momentum',),'recoil':('opposite fragment momenta balance',),'classify':('approach, contact, separation',),'eloss':('initial KE splits into CM, relative, loss',),'defo':('deformation then restitution impulses',),'oblique':('normal and tangent at contact',),'ninety':('equal-mass elastic exit paths',),'pendulum':('collision stage then swing stage',),'spring':('blocks separate and compress a spring',),'cmframe':('lab velocity = CM + relative velocity',),'belt':('sand lands on a moving belt',),'rocket':('rocket ejects exhaust opposite thrust',),'flux':('mass crosses a control surface',),'boat':('man walks; boat recoils',),'bounces':('successive rebound heights',),'wall':('ball meets a moving wall',),'chain3':('falling chain impacts a scale',),'scatter':('projectile and target scatter',),'peg':('chain hangs over a smooth peg',),'staging':('burn, discard empty stage, burn again',),'jet':('water jet strikes a moving plate',),'fold':('folded chain passes a table edge',),'relativ':('relativistic momentum at high speed',),'hopper':('cart collects or leaks sand',),'route':('choose system, axis and time window',)})

THEME_BASE={
 'bodies':'bodies','hole':'hole','explosion':'explosion','impulse':'impulse','recoil':'recoil','classify':'classify','coll1d':'coll1d','collcases':'collcases','eloss':'eloss','defo':'defo','oblique':'oblique','ninety':'ninety','pendulum':'pendulum','spring':'spring','cmframe':'cmframe','belt':'belt','rocket':'rocket','flux':'flux','boat':'boat','bounces':'bounces','wall':'wall','traps':'traps','route':'route','ledger':'ledger','chain3':'chain3','scatter':'scatter','impapprox':'impapprox','platform':'platform','peg':'peg','staging':'staging','jet':'jet','fold':'fold','relativ':'relativ','hopper':'hopper','integrate':'integrate'}
CAP={}
for k in THEME_BASE:
    CAP[(k,'a')]=(k.replace('3',' three')+': labelled physical setup')[:58]
    CAP[(k,'b')]=(k.replace('3',' three')+': limiting curve / diagnostic')[:58]
CAP[('chain3','a')]='falling chain: landed length x, speed and flux'
CAP[('fold','a')]='fold at edge: equal hanging strands, descent y'
CAP[('peg','a')]='chain over peg: unequal sides x and L-x'
def figure(a,key):
    theme,side=key.rsplit('-',1);base=THEME_BASE.get(theme,'bodies')
    if side=='a':plain(a);schematic(a,base)
    else:graph_panel(a,base)
    return CAP.get((theme,side),'COM & collision panel')
