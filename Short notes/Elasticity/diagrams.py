"""Native analytical diagrams for the elasticity short notes.

Every curve follows the stated model and carries axis names/units; schematic
geometry is labelled and drawn from vector primitives at print resolution.
Kept deliberately spare: no label is placed where another can collide.
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, Ellipse, Arc, Polygon

I='#153149'; T='#087d7d'; R='#a43232'; PALE='#eff8f5'; YEL='#fff2b8'; G='#516875'
GOLD='#8a6a10'; GOLDF='#fff9e1'

def txt(ax,x,y,s,color=I,**kw):
    kw.setdefault('fontsize',10); ax.text(x,y,s,color=color,**kw)
def note(ax,x,y,s,color=G,**kw):
    kw.setdefault('fontsize',8.4); ax.text(x,y,s,color=color,**kw)
def arrow(ax,a,b,c=T,lw=1.5,style='->',ms=8):
    ax.annotate('',xy=b,xytext=a,arrowprops=dict(arrowstyle=style,color=c,lw=lw,shrinkA=0,shrinkB=0,mutation_scale=ms))
def plain(ax):
    ax.axis('off'); ax.set(xlim=(0,10),ylim=(0,5))
def disc(ax,x,y,r,fc='#e6efed',ec=I,lw=1.3):
    ax.add_patch(Ellipse((x,y),2*r,2*r*1.34,fc=fc,ec=ec,lw=lw))
def wall(ax,x0,x1,y,up=True,n=7):
    ax.plot([x0,x1],[y,y],color=I,lw=2.2)
    for x in np.linspace(x0+.05,x1-.05,n):
        ax.plot([x,x+.13],[y,y+(.20 if up else -.20)],color=I,lw=1.1)
def dimx(ax,x0,x1,y,label):
    arrow(ax,(x0,y),(x1,y),I,1.0,'<->',7); txt(ax,(x0+x1)/2,y+.12,label,ha='center',fontsize=8.6)
def dimy(ax,x,y0,y1,label,sign=1):
    arrow(ax,(x,y0),(x,y1),I,1.0,'<->',7); txt(ax,x+sign*.10,(y0+y1)/2,label,ha='left' if sign>0 else 'right',va='center',fontsize=8.6)
def graph(ax):
    ax.axis('on'); ax.spines[['top','right']].set_visible(False)
    ax.tick_params(labelsize=8.2); ax.grid(alpha=.13,lw=.7)

def figure(ax,key):
    KNOWN=('stress_modes','stress_strain','stress_strain_zoom','modulus_bar','poisson_wire','poisson_bounds',
           'series_composite','parallel_wires','hanger_angle','self_weight','sag_wire','thermal_stress',
           'bulk_water','bulk_gas','torsion_shaft','torsion_j','energy_area','sudden_load','drop_curve',
           'drop_energy','bending_axis','section_props','cantilever','beam_cases','decision_map',
           'quick_numbers','atomic_well','potential_cubic','alpha_scale','rod_mass_impact','wave_transit',
           'constant_stress','taper_profile','cantilever_integrated','buckling','euler_modes','ibeam',
           'hooke_limit','hysteresis','hoop_stress','vessel_crack','wave_speeds','ashby','s_shadow')
    if key not in KNOWN: return _extra(ax,key)
    if key=='stress_modes':
        plain(ax)
        for xx in (3.35,6.70): ax.plot([xx,xx],[.55,4.7],color='#cfe1dc',lw=1)
        txt(ax,1.60,4.80,'TENSION: Y',ha='center',color=T)
        wall(ax,.55,2.65,4.45)
        ax.add_patch(Rectangle((1.05,1.25),.50,3.20,fc='none',ec=G,lw=1.0,ls='--'))
        ax.add_patch(Rectangle((1.13,.95),.34,3.50,fc='#e6efed',ec=I,lw=1.4))
        arrow(ax,(1.30,.80),(1.30,.44),R); txt(ax,1.39,.66,'F',color=R,fontsize=8.6)
        dimy(ax,1.92,.95,4.45,'L'); dimy(ax,2.24,.95,1.25,'dL')
        note(ax,2.90,.28,'F/A and dL/L',ha='center',fontsize=7.4)
        txt(ax,5.00,4.80,'PRESSURE: B',ha='center',color=T)
        ax.add_patch(Rectangle((4.35,2.10),1.30,1.25,fc='#e6efed',ec=I,lw=1.4))
        ax.add_patch(Rectangle((4.50,2.25),1.00,.95,fc='none',ec=G,lw=1.0,ls='--'))
        arrow(ax,(5.00,3.58),(5.00,3.36),R); arrow(ax,(5.00,1.86),(5.00,2.08),R)
        arrow(ax,(4.12,2.72),(4.34,2.72),R); arrow(ax,(5.88,2.72),(5.66,2.72),R)
        txt(ax,5.55,3.44,'p',color=R,fontsize=8.8)
        note(ax,5.00,.55,'p and dV/V',ha='center',fontsize=7.8)
        txt(ax,8.20,4.80,'SHEAR: G',ha='center',color=T)
        ax.add_patch(Rectangle((7.20,1.40),1.65,1.40,fc='none',ec=G,lw=1.0,ls='--'))
        ax.add_patch(Polygon([[7.20,1.40],[8.85,1.40],[9.30,2.80],[7.65,2.80]],closed=True,fc='#e6efed',ec=I,lw=1.4))
        arrow(ax,(7.80,3.04),(9.25,3.04),R); txt(ax,8.50,3.16,'F',color=R,fontsize=8.8,ha='center')
        arrow(ax,(8.80,1.20),(7.35,1.20),R); txt(ax,8.05,1.02,'F',color=R,fontsize=8.8,ha='center')
        ax.add_patch(Arc((8.85,1.40),.70,.94,theta1=74,theta2=90,color=R,lw=1.1))
        txt(ax,9.14,1.84,r'$\gamma$',color=R,fontsize=9.2)
        note(ax,8.20,.55,'F/A and gamma',ha='center',fontsize=7.8)
        return 'The three deformation modes and the modulus each one defines'
    if key=='stress_strain':
        graph(ax); ax.set_xlim(0,18); ax.set_ylim(0,510)
        e1=np.linspace(0,.125,20); ax.plot(e1,2000*e1,color=I,lw=2.3)
        ax.plot([.125,1.25],[250,262],color=I,lw=2.3)
        e2=np.linspace(1.25,11,120); ax.plot(e2,262+195*(1-np.exp(-(e2-1.25)/3.4)),color=I,lw=2.3)
        e3=np.linspace(11,17,80); ax.plot(e3,452-140*((e3-11)/6)**1.5,color=I,lw=2.3)
        ax.plot([17],[320],marker='x',ms=8,mew=2.2,color=R)
        eb=np.linspace(0,.42,20); ax.plot(eb,285*eb/.42,color=R,lw=1.9,ls='--')
        ax.plot([.42],[285],marker='x',ms=7,mew=2,color=R)
        for n,(px,py) in enumerate([(0.125,250),(1.7,258),(10.6,450),(16.6,318)],1):
            ax.plot([px],[py],'o',ms=9,color=T)
            ax.text(px,py,str(n),ha='center',va='center',fontsize=7.2,color='white')
        ax.text(5.4,486,'mild steel',fontsize=8.6,color=I)
        ax.text(0.55,152,'glass',fontsize=8.2,color=R)
        ax.set_xlabel('strain  ε  (%)',fontsize=9.2); ax.set_ylabel('stress  σ  (MPa)',fontsize=9.2)
        ax.set_xticks([0,2,4,6,8,10,12,14,16]); ax.set_yticks([0,100,200,300,400,500])
        return '1 proportional limit, 2 yield, 3 ultimate, 4 fracture; steel vs glass'
    if key=='stress_strain_zoom':
        graph(ax); ax.set_xlim(0,.22); ax.set_ylim(0,344)
        e=np.linspace(0,.18,50)
        ax.plot(e,2000*e,color=I,lw=2.2,label='steel 200 GPa')
        ax.plot(e,700*e,color=T,lw=2.0,label='aluminium 70 GPa')
        ax.plot([.05,.05],[0,318],color=G,lw=.9,ls=':'); ax.plot([.15,.15],[0,318],color=G,lw=.9,ls=':')
        arrow(ax,(.05,332),(.15,332),G,1.0,'<->',7)
        ax.text(.10,338,r'$\Delta\varepsilon=0.10\%$',ha='center',fontsize=7.8,color=G)
        arrow(ax,(.163,88),(.163,290),G,1.0,'<->',7)
        ax.text(.168,190,r'$\Delta\sigma$',va='center',fontsize=8.2,color=G)
        ax.text(.002,140,r'slope $=\Delta\sigma/\Delta\varepsilon=Y$',fontsize=8.2,color=I)
        ax.set_xlabel('strain  ε  (%)',fontsize=9.0); ax.set_ylabel('stress  σ  (MPa)',fontsize=9.0)
        ax.legend(fontsize=7.8,frameon=False,loc='lower right',bbox_to_anchor=(1.0,.06))
        ax.set_xticks([0,.05,.10,.15,.20])
        return 'Slope ds/de = Y = 2.0e11 Pa; the F-x slope k is not Y'
    if key=='modulus_bar':
        graph(ax); ax.set_xscale('log'); ax.set_xlim(1e-4,1e5); ax.set_ylim(-.7,5.7)
        names=['rubber','wood','bone','concrete','aluminium','steel']; vals=[.005,10,15,30,70,200]
        cols=[R,'#9a7d55','#b08d57',G,T,I]
        ax.barh(names,vals,color=cols,height=.55)
        for y,v in enumerate(vals): ax.text(v*1.3,y,f'{v:g} GPa',va='center',fontsize=8.4,color=I)
        ax.set_xlabel("Young's modulus  Y  (GPa, log scale)",fontsize=9.0)
        return 'Order-of-magnitude smell test: solids 10-200 GPa, rubber 10^-3 GPa'
    if key=='poisson_wire':
        plain(ax)
        wall(ax,.75,2.60,4.45)
        ax.add_patch(Rectangle((1.25,1.25),.50,3.20,fc='none',ec=G,lw=1.0,ls='--'))
        ax.add_patch(Rectangle((1.33,1.00),.34,3.45,fc='#e6efed',ec=I,lw=1.4))
        arrow(ax,(1.50,.88),(1.50,.58),R); txt(ax,1.34,.66,'F',color=R,fontsize=8.4,ha='right')
        dimy(ax,2.10,1.00,4.45,'L'); dimy(ax,2.30,1.00,1.25,'dL')
        disc(ax,4.00,3.25,.68)
        ax.add_patch(Ellipse((4.00,3.25),1.52,1.52*1.34,fc='none',ec=G,lw=1.0,ls='--'))
        arrow(ax,(4.00,3.25),(4.62,3.25),I,1.0); txt(ax,4.32,3.38,'r',color=I,fontsize=8.2)
        arrow(ax,(4.00,3.25),(4.00,3.89),G,1.0); txt(ax,4.06,3.68,'r-dr',color=G,fontsize=7.4)
        note(ax,2.55,1.62,'dashed = unloaded',fontsize=7.4)
        txt(ax,5.55,4.28,r'$\nu=-\varepsilon_{\rm lat}/\varepsilon_{\rm long}$',fontsize=9.0)
        txt(ax,5.55,3.55,r'$\Delta r=-\nu r\,\Delta L/L$',fontsize=9.0)
        txt(ax,5.55,2.82,r'$\Delta V/V=(1-2\nu)\varepsilon$',fontsize=9.0)
        note(ax,1.62,.28,'dL needs no Poisson factor',color=R,fontsize=7.4)
        return 'Poisson contraction: lateral strain is -nu times longitudinal strain'
    if key=='poisson_bounds':
        graph(ax); nu=np.linspace(-.995,.49,600)
        ax.plot(nu,1/(3*(1-2*nu)),color=I,lw=2.0,label=r'$B/Y$')
        ax.plot(nu,1/(2*(1+nu)),color=T,lw=2.0,label=r'$G/Y$')
        ax.axvline(.5,color=R,ls=':',lw=1.3); ax.axvline(-1,color=R,ls=':',lw=1.3)
        ax.axvspan(-1,.5,color='#eef6f3',alpha=.6)
        ax.plot([.29],[1/(3*(1-2*.29))],'o',ms=4.5,color=I)
        ax.annotate('steel 0.29',(.29,1/(3*(1-2*.29))),xytext=(-.55,7.4),fontsize=8.0,
                    arrowprops=dict(arrowstyle='->',lw=.8,color=I))
        ax.text(.46,15.0,r'$B\to\infty$',ha='right',fontsize=8.6,color=R)
        ax.set_xlim(-1.02,.55); ax.set_ylim(0,20)
        ax.set_xlabel('Poisson ratio  ν',fontsize=9.0); ax.set_ylabel('modulus / Y',fontsize=9.0)
        ax.legend(fontsize=8.0,frameon=False,loc='upper left')
        return 'Stable solids need -1 < nu < 0.5; B diverges as nu tends to 0.5'
    if key=='series_composite':
        plain(ax)
        wall(ax,.35,1.75,4.55)
        ax.add_patch(Rectangle((.95,3.55),3.35,1.00,fc='#e6efed',ec=I,lw=1.3))
        ax.add_patch(Rectangle((4.30,3.76),3.90,.58,fc=GOLDF,ec=I,lw=1.3))
        ax.plot([4.30,4.30],[3.45,4.15],color=I,lw=1.0)
        arrow(ax,(.95,3.30),(.55,3.30),R); txt(ax,.60,3.40,'F',color=R,fontsize=8.4,ha='left')
        arrow(ax,(8.20,3.30),(8.60,3.30),R); txt(ax,8.55,3.40,'F',color=R,fontsize=8.4,ha='right')
        txt(ax,2.60,4.04,'steel',ha='center',fontsize=8.2)
        txt(ax,6.25,4.04,'copper',ha='center',fontsize=8.2)
        txt(ax,4.95,2.95,r'$\Delta L=F\left(\dfrac{L_1}{A_1Y_1}+\dfrac{L_2}{A_2Y_2}\right)$',ha='center',fontsize=9.6)
        ax.plot([1.0,9.2],[.95,.95],color=I,lw=1.2)
        ax.add_patch(Rectangle((1.5,.95),1.7,.95,fc='#cfe8e1',ec=T,lw=1.1))
        ax.add_patch(Rectangle((4.0,.95),1.7,.48,fc='#f6e2a8',ec=GOLD,lw=1.1))
        txt(ax,2.35,2.05,r'$\sigma_1=F/A_1$',ha='center',fontsize=8.4,color=T)
        txt(ax,4.85,1.56,r'$\sigma_2=F/A_2$',ha='center',fontsize=8.4,color=GOLD)
        note(ax,6.30,1.60,'thin side:',color=R,fontsize=7.8)
        note(ax,6.30,1.34,'higher stress',color=R,fontsize=7.8)
        return 'Series composite: common force, extensions add, stress steps with 1/A'
    if key=='parallel_wires':
        plain(ax)
        wall(ax,.90,8.10,4.55)
        ax.plot([1.60,1.60],[1.33,4.55],color=I,lw=1.8)
        ax.plot([7.00,7.00],[1.33,4.55],color=I,lw=3.0)
        ax.add_patch(Rectangle((.95,1.05),6.70,.28,fc='#e6efed',ec=I,lw=1.3))
        txt(ax,1.36,2.85,'k1',fontsize=8.8,rotation=90,ha='center')
        txt(ax,7.24,2.85,'k2',fontsize=8.8,rotation=90,ha='center')
        arrow(ax,(4.80,.95),(4.80,.35),R); txt(ax,4.63,.60,'2000 N',color=R,fontsize=8.2,ha='right')
        txt(ax,3.30,2.40,r'$F_1/F_2=k_1/k_2$',ha='center',fontsize=10.0,color=T)
        note(ax,3.30,1.85,'equal extensions',ha='center',color=T,fontsize=8.2)
        note(ax,1.60,.75,'1.0 mm dia',ha='center',fontsize=7.4)
        note(ax,7.00,.75,'2.0 mm dia',ha='center',fontsize=7.4)
        note(ax,4.80,4.26,'rigid bar',ha='center',fontsize=7.8)
        return 'Parallel wires under a rigid bar: equal extensions, load splits as stiffness'
    if key=='hanger_angle':
        plain(ax)
        wall(ax,1.10,8.90,4.55)
        A=np.array([1.40,4.55]); B=np.array([8.60,4.55]); M=np.array([5.00,1.55])
        ax.plot([A[0],M[0]],[A[1],M[1]],color=I,lw=2.2); ax.plot([B[0],M[0]],[B[1],M[1]],color=I,lw=2.2)
        disc(ax,M[0],M[1],.20); txt(ax,M[0],M[1],'m',ha='center',va='center',fontsize=8.4)
        arrow(ax,(5.0,1.24),(5.0,.62),R); txt(ax,5.16,.84,'mg',color=R,fontsize=8.4)
        ax.add_patch(Arc(A,1.10,1.47,theta1=-30,theta2=0,color=R,lw=1.0))
        txt(ax,A[0]+1.16,A[1]-.44,r'$\theta$',color=R,fontsize=8.4)
        txt(ax,2.36,2.92,'T',color=T,fontsize=9.2); txt(ax,7.50,2.92,'T',color=T,fontsize=9.2)
        note(ax,5.0,.24,'theta measured from the horizontal',ha='center',fontsize=7.8)
        return 'Angled hanger: tension mg/(2 sin theta), not mg/2 unless theta = 90 degrees'
    if key=='self_weight':
        plain(ax)
        wall(ax,3.00,4.80,4.55)
        ax.add_patch(Rectangle((3.40,.60),.36,3.95,fc='#e6efed',ec=I,lw=1.3))
        ax.add_patch(Rectangle((3.40,2.10),.36,.22,fc='#f6e2a8',ec=GOLD,lw=1.0))
        dimy(ax,3.16,.60,4.55,'L',-1); dimy(ax,4.06,.60,2.10,'x',+1)
        arrow(ax,(3.38,2.21),(2.92,2.21),R); txt(ax,2.88,2.33,'F(x)',color=R,ha='right',fontsize=8.2)
        note(ax,4.22,2.42,'element dx',color=GOLD,fontsize=7.8)
        note(ax,3.58,.28,'x from free end',ha='center',fontsize=7.6)
        ax.plot([6.15,6.15],[.60,4.55],color=I,lw=1.2); ax.plot([6.15,8.60],[4.55,4.55],color=I,lw=1.2)
        ax.plot([6.15,8.60],[.60,4.55],color=T,lw=1.8)
        for yy in [1.1,2.0,2.9,3.8]:
            arrow(ax,(6.15,yy),(6.15+2.45*(yy-.60)/3.95,yy),T,lw=.8)
        txt(ax,7.35,4.68,r'$F=\rho A g x$',ha='center',fontsize=8.8,color=T)
        note(ax,6.05,.36,'0',ha='center'); note(ax,8.62,.42,'mg',ha='left')
        return 'Self-weight: F(x) ramps from 0 to mg, so the integral gives half the end-load value'
    if key=='sag_wire':
        plain(ax)
        wall(ax,.55,1.65,4.40); wall(ax,8.35,9.45,4.40)
        A=np.array([1.10,4.40]); B=np.array([8.90,4.40]); M=np.array([5.00,2.55])
        ax.plot([A[0],M[0]],[A[1],M[1]],color=I,lw=2.2); ax.plot([B[0],M[0]],[B[1],M[1]],color=I,lw=2.2)
        ax.plot([A[0],B[0]],[A[1],B[1]],color=G,lw=1.0,ls='--')
        disc(ax,M[0],M[1],.19); txt(ax,M[0],M[1],'m',ha='center',va='center',fontsize=8.2)
        arrow(ax,(5.0,2.32),(5.0,1.70),R); txt(ax,5.16,1.92,'mg',color=R,fontsize=8.2)
        dimy(ax,5.58,2.55,4.40,'y',+1)
        note(ax,3.05,4.56,'l',ha='center',fontsize=8.4,color=I); note(ax,6.95,4.56,'l',ha='center',fontsize=8.4,color=I)
        ax.add_patch(Arc(A,1.30,1.74,theta1=-36,theta2=0,color=R,lw=1.0)); txt(ax,2.26,4.04,r'$\theta$',color=R,fontsize=8.2)
        txt(ax,5.0,.78,r'$y=l\,(mg/YA)^{1/3}$',ha='center',fontsize=10.4)
        note(ax,5.0,.34,'sag exaggerated for the drawing',ha='center',fontsize=7.6)
        return 'Straight wire with a midpoint load: sag grows as F^(1/3), not linearly'
    if key=='thermal_stress':
        plain(ax)
        txt(ax,2.70,4.74,'free expansion: no stress',ha='center',color=T,fontsize=8.8)
        wall(ax,.20,.75,3.55,up=False)
        ax.add_patch(Rectangle((.75,3.32),3.90,.44,fc='#e6efed',ec=I,lw=1.3))
        ax.add_patch(Rectangle((.75,3.32),4.80,.44,fc='none',ec=G,lw=1.0,ls='--'))
        txt(ax,4.95,4.02,'alpha L dT',fontsize=8.2,color=I,ha='left')
        txt(ax,2.70,2.86,'constrained: stress appears',ha='center',color=T,fontsize=8.8)
        wall(ax,.20,.75,1.20,up=False); wall(ax,4.75,5.30,1.20,up=False)
        ax.add_patch(Rectangle((.75,1.08),4.00,.40,fc='#f6e2a8',ec=I,lw=1.3))
        arrow(ax,(.42,1.48),(.73,1.48),R); arrow(ax,(5.08,1.48),(4.77,1.48),R)
        txt(ax,2.70,.66,r'$\sigma_{\rm th}=Y\alpha\Delta T$',ha='center',fontsize=9.6)
        note(ax,2.90,.26,'L cancels: bolt and rail agree',ha='center',fontsize=7.6)
        txt(ax,6.45,3.55,'heating',fontsize=8.4); txt(ax,6.45,3.20,'compression',fontsize=8.4,color=R)
        txt(ax,6.45,2.40,'cooling',fontsize=8.4); txt(ax,6.45,2.05,'tension',fontsize=8.4,color=R)
        note(ax,6.45,1.35,'reaction, not dT,',fontsize=7.6); note(ax,6.45,1.08,'sets the sign',fontsize=7.6)
        return 'Thermal stress: expand freely, then compress back to the constraint'
    if key=='bulk_water':
        graph(ax); d=np.linspace(0,10,200)
        ax.plot(d,1+d*1000*9.8*1000/2.2e9,color=T,lw=2.2,label=r'$\rho_0(1+\rho_0gd/B)$')
        ax.plot([4],[1.018],'o',ms=5,color=R)
        ax.annotate('4 km: 1.018',(4,1.018),xytext=(4.5,.998),fontsize=8.0,color=R,
                    arrowprops=dict(arrowstyle='->',color=R,lw=.8))
        ax.set_xlabel('depth  d  (km)',fontsize=9.0); ax.set_ylabel('density ratio',fontsize=9.0)
        ax.legend(fontsize=7.8,frameon=False,loc='upper left'); ax.set_ylim(.995,1.055)
        return 'Water is 1.8 % denser at 4 km: small, but not zero'
    if key=='bulk_gas':
        graph(ax); p=np.linspace(1,4,50)
        ax.plot(p,p,color=I,lw=2.0,label=r'isothermal $B=p$')
        ax.plot(p,1.4*p,color=T,lw=2.0,label=r'adiabatic $B=\gamma p$')
        ax.set_xlabel('pressure  p  (arbitrary units)',fontsize=9.0)
        ax.set_ylabel('bulk modulus  B',fontsize=9.0)
        ax.legend(fontsize=8.0,frameon=False,loc='upper left'); ax.set_xlim(1,4); ax.set_ylim(0,6)
        return 'A gas has no single B: the process chooses isothermal p or adiabatic gamma p'
    if key=='torsion_shaft':
        plain(ax)
        ax.plot([1.2,5.9],[3.05,3.05],color=G,lw=.9,ls='--')
        ax.plot([1.2,5.9],[1.55,2.55],color=I,lw=1.3)
        ax.add_patch(Rectangle((1.2,1.35),.28,1.85,fc='#e6efed',ec=I,lw=1.2))
        ax.add_patch(Rectangle((5.6,1.35),.28,1.85,fc='#e6efed',ec=I,lw=1.2))
        ax.add_patch(Arc((1.20,3.05),.55,1.40,theta1=-90,theta2=90,color=R,lw=1.0))
        txt(ax,.92,3.34,r'$\theta$',color=R,fontsize=8.4,ha='center')
        for yy in [2.9,2.5,2.1,1.7]:
            ax.plot([1.48,5.6],[yy,yy],color='#dfe9e6',lw=.6)
        ax.plot([1.48,5.9],[3.28,2.72],color=R,lw=1.0,ls=':')
        txt(ax,3.40,3.56,'a painted line twists',ha='center',fontsize=7.6,color=R)
        note(ax,3.40,.90,'gamma = r theta / L',ha='center',fontsize=7.4)
        ax.text(6.30,3.45,r'$\theta=TL/(GJ)$',fontsize=9.0)
        ax.text(6.30,2.75,r'$J=\pi R^4/2$',fontsize=9.0)
        ax.text(6.30,2.15,r'$C=GJ/L$',fontsize=9.0)
        note(ax,6.30,1.62,'hollow: more J/kg',fontsize=7.2)
        return 'Torsion: shear strain grows with radius; J = pi R^4 / 2'
    if key=='torsion_j':
        graph(ax); r=np.linspace(0,1,300)
        ax.plot(r,r**3,color=I,lw=2.0,label=r'$r^3$ inside J')
        ax.plot(r,r,color=G,lw=1.2,ls='--',label=r'$r$ inside area')
        ax.fill_between(r,0,r**3,color='#d6ece6')
        ax.axvline(.7,color=R,ls=':',lw=1.0)
        ax.text(.02,.86,'core r < 0.7R:',fontsize=7.6,color=R)
        ax.text(.02,.75,'34 % of J, 49 % of A',fontsize=7.6,color=R)
        ax.set_xlabel('radius  r / R',fontsize=9.0); ax.set_ylabel('normalised weight',fontsize=9.0)
        ax.legend(fontsize=7.6,frameon=False,loc='center right'); ax.set_xlim(0,1.02); ax.set_ylim(0,1.05)
        return 'J weights area by r^2: the core contributes little stiffness but much mass'
    if key=='energy_area':
        graph(ax); x=np.linspace(0,1,100)
        ax.plot(x,x,color=I,lw=1.9); ax.fill_between(x,0,x,color=YEL,alpha=.9)
        arrow(ax,(.55,0),(.55,.55),T,1.0,'<->',7); txt(ax,.60,.24,'x',fontsize=8.0,color=T)
        txt(ax,.44,.72,'energy = Fx/2',fontsize=8.2,color=I)
        note(ax,.05,.93,'a rectangle Fx would overcount',fontsize=7.2)
        ax.set_xlabel('extension',fontsize=9.0); ax.set_ylabel('force',fontsize=9.0)
        ax.set_xticks([0,1]); ax.set_yticks([0,1]); ax.set_xticklabels(['0','x']); ax.set_yticklabels(['0','F'])
        return 'Linear spring: stored energy is the triangle, not the rectangle'
    if key=='sudden_load':
        graph(ax); D=np.linspace(0,2.4,400)
        ax.plot(D,D,color=G,lw=1.1,ls='--')
        ax.axhline(1.0,color=R,lw=1.2)
        ax.fill_between([0,2.0],[1,1],color=YEL,alpha=.9)
        ax.axvline(1.0,color=I,lw=.7,ls=':'); ax.axvline(2.0,color=T,lw=.7,ls=':')
        ax.plot([1],[1],'o',ms=4.5,color=I); ax.plot([2],[1],'o',ms=4.5,color=T)
        ax.text(1.04,1.22,'static',fontsize=7.4,color=I)
        ax.text(2.04,1.22,'peak',fontsize=7.4,color=T)
        ax.text(.05,1.42,'mg',fontsize=7.6,color=R)
        ax.text(1.86,2.30,'kx',fontsize=7.6,color=G)
        note(ax,.05,.24,'shaded = work done by mg',fontsize=7.2)
        ax.set_xlabel(r'extension  $\Delta/(mg/k)$',fontsize=8.8)
        ax.set_ylabel(r'force $/mg$',fontsize=8.8)
        ax.set_xlim(0,2.4); ax.set_ylim(0,2.6)
        return 'Sudden release: energy balance gives twice the static extension'
    if key=='drop_curve':
        graph(ax); D=np.linspace(0,2.2,300)
        ax.plot(D,D,color=G,lw=1.1,ls='--',label=r'$k\Delta$')
        ax.plot(D,1.0+D,color=R,lw=1.4,label=r'$mg$ (constant)')
        ax.set_xlim(0,2.2); ax.set_ylim(0,4.0)
        ax.fill_between(D[D<1.85],D[D<1.85],1.0+D[D<1.85],color='#f6e2a8',alpha=.85)
        ax.axhline(1.0,color=I,lw=.8,ls=':')
        ax.plot([1.85],[1.85],'o',ms=4.5,color=T)
        ax.annotate('meet: energy\ncloses here',(1.85,1.85),xytext=(.35,2.7),fontsize=7.6,color=T,
                    arrowprops=dict(arrowstyle='->',color=T,lw=.8))
        note(ax,1.05,1.16,'mg',fontsize=7.4,color=I)
        ax.set_xlabel('extension  Δ',fontsize=8.8); ax.set_ylabel('force',fontsize=8.8)
        ax.set_yticks([0,1]); ax.set_yticklabels(['0','mg'])
        ax.legend(fontsize=7.4,frameon=False,loc='lower right')
        return 'The drop solutions are where stored area equals the work shaded between the lines'
    if key=='drop_energy':
        graph(ax)
        bars=['mg(h+d)','k d^2/2','mgh']
        vals=[1.0,1.0,0.97]
        ax.bar(bars,vals,color=[GOLD,T,'#cfe8e1'],width=.5)
        for i,v in enumerate(vals): ax.text(i,v+.04,f'{v:.2f}',ha='center',fontsize=8.4,color=I)
        ax.set_ylim(0,1.30); ax.set_yticks([0,1]); ax.set_ylabel('energy / reference',fontsize=8.4)
        ax.tick_params(axis='x',labelsize=7.8)
        txt(ax,2.0,1.05,'h >> d',fontsize=7.6,color=G,ha='center')
        return 'Drop: mg(h + d) equals the stored k d^2 / 2'
    if key=='bending_axis':
        plain(ax)
        xs=np.linspace(0,6.6,160); yc=3.50-.28*np.sin(xs/6.6*np.pi)
        top=yc+.62; bot=yc-.62
        ax.fill_between(xs,bot,top,color='#eef4f2')
        ax.plot(xs,top,color=I,lw=1.2); ax.plot(xs,bot,color=I,lw=1.2)
        ax.plot(xs,yc,color=G,lw=1.1,ls='--')
        for x in (0.8,2.4,4.0,5.6):
            i=int(x/6.6*159); ax.plot([x,x],[bot[i],top[i]],color=I,lw=.9)
        txt(ax,0.90,4.35,'top: compression',fontsize=7.8,color=R)
        txt(ax,0.90,1.55,'bottom: tension',fontsize=7.8,color=T)
        txt(ax,0.90,2.34,'neutral axis',fontsize=7.2,color=G)
        txt(ax,7.05,3.95,r'$M=YI/R$',fontsize=9.0)
        txt(ax,7.05,3.25,r'$I=\int y^{2}dA$',fontsize=9.0)
        txt(ax,7.05,2.60,r'$\sigma=Yy/R$',fontsize=9.0)
        note(ax,7.05,2.05,'y from the axis',fontsize=7.6)
        return 'Bending: strain grows with distance y from the neutral axis'
    if key=='section_props':
        plain(ax)
        ax.add_patch(Rectangle((.4,2.4),1.6,1.2,fc='#e6efed',ec=I,lw=1.2))
        txt(ax,1.20,3.72,'b',ha='center',fontsize=8.4); txt(ax,.28,3.00,'h',fontsize=8.4,ha='right')
        txt(ax,1.20,1.92,r'$I=bh^3/12$',ha='center',fontsize=8.6)
        txt(ax,1.20,4.52,'rectangle',ha='center',fontsize=8.2,color=T)
        ax.add_patch(Circle((4.8,3.0),.55,fc='#e6efed',ec=I,lw=1.2))
        arrow(ax,(4.8,3.0),(5.35,3.0),I,1.0); txt(ax,5.08,3.14,'R',fontsize=8.2)
        txt(ax,4.8,1.92,r'$I=\pi R^4/4$',ha='center',fontsize=8.6)
        txt(ax,4.8,4.52,'bending',ha='center',fontsize=8.2,color=T)
        ax.add_patch(Circle((7.6,3.0),.55,fc='none',ec=I,lw=1.2))
        txt(ax,7.6,1.92,r'$J=\pi R^4/2$',ha='center',fontsize=8.6)
        txt(ax,7.6,4.52,'torsion',ha='center',fontsize=8.2,color=T)
        note(ax,4.20,1.30,'geometry first, material second',ha='center',fontsize=7.4)
        return 'The same circle has I = pi R^4/4 in bending and J = pi R^4/2 in torsion'
    if key=='cantilever':
        graph(ax); x=np.linspace(0,1,200)
        ax.plot(x,0.0*x,color=G,lw=1.0,ls='--')
        ax.plot(x,-(x**2*(3-x))/2,color=I,lw=2.0)
        ax.plot([0,0],[-.06,.10],color=I,lw=3)
        arrow(ax,(1.0,0),(1.18,0),R,1.3); ax.text(1.20,-.12,'F',color=R,fontsize=8.4)
        ax.plot([1.0,1.0],[0,-1.0],color=G,lw=.7,ls=':')
        ax.text(-.02,-1.08,r'$-FL^3/3YI$',fontsize=7.4,color=G,ha='left')
        ax.text(.28,-.40,r'$\delta(x)=\dfrac{Fx^2(3L-x)}{6YI}$',fontsize=8.0,color=I)
        ax.text(.46,.11,'unloaded',fontsize=7.2,color=G)
        ax.set_xlabel('x / L from the built-in end',fontsize=8.6)
        ax.set_ylabel(r'$\delta/(FL^3/YI)$',fontsize=8.6)
        ax.set_xlim(0,1.25); ax.set_ylim(-1.20,.22); ax.set_xticks([0,.5,1]); ax.set_yticks([-1,0])
        return 'Cantilever: tip deflection FL^3/3YI, growing as the cube of length'
    if key=='beam_cases':
        graph(ax); t=np.linspace(0,1,300)
        ax.plot(t,-t**2*(3-t)/6,color=I,lw=2.0)
        ax.plot(t,-t**2*(6-4*t+t**2)/24,color=T,lw=1.7)
        ax.plot([.5],[-1/48],'o',ms=5,color=R)
        ax.text(.545,-.010,'1/48',fontsize=7.4,color=R)
        ax.text(.10,-.245,'simply supported,',fontsize=7.2,color=R)
        ax.text(.10,-.285,'centre load: 1/48',fontsize=7.2,color=R)
        ax.text(1.02,-.345,r'$1/3$  cantilever',fontsize=7.6,color=I)
        ax.text(1.02,-.135,r'$1/8$  uniform $w$',fontsize=7.6,color=T)
        ax.set_xlabel('x / L',fontsize=8.6)
        ax.set_ylabel(r'$\delta\,/\,(FL^3/YI)$',fontsize=8.6)
        ax.set_xlim(0,1.34); ax.set_ylim(-.375,.035)
        ax.set_yticks([-.3,-.2,-.1,0])
        return 'Same load: the cantilever tip sags 16x more than a simply supported centre'
    if key=='decision_map':
        plain(ax)
        txt(ax,5.0,4.62,'name the mode first',ha='center',fontsize=9.2,color=T)
        boxes=[(1.5,'PULL','Y, k=YA/L'),(3.83,'SQUEEZE','B, dV/V'),
               (6.17,'SHEAR','G, TL/GJ'),(8.5,'BEND','Y, I, M=YI/R')]
        for x,top,sub in boxes:
            ax.add_patch(Rectangle((x-1.05,2.55),2.10,.95,fc=PALE,ec=T,lw=1.1))
            txt(ax,x,3.18,top,ha='center',fontsize=8.0,color=T)
            txt(ax,x,2.79,sub,ha='center',fontsize=6.8)
            arrow(ax,(5.0,4.34),(x,3.52),T,1.0)
        ax.add_patch(Rectangle((1.35,.95),7.3,.85,fc=YEL,ec=GOLD,lw=1.1))
        txt(ax,5.0,1.56,'static, sudden or dropped? thermal?',ha='center',fontsize=7.2)
        txt(ax,5.0,1.22,'the constraint writes the extra equation',ha='center',fontsize=6.8,color=G)
        return 'Triage: mode, then section, then load history, then the formula'
    if key=='quick_numbers':
        graph(ax); ax.set_axis_off()
        rows=[('Y steel',r'$2.0\times10^{11}$ Pa'),('G steel',r'$8.0\times10^{10}$ Pa'),
              ('yield, mild steel',r'$2.5\times10^{8}$ Pa'),('alpha steel',r'$1.2\times10^{-5}$ K$^{-1}$'),
              ('nu steel',r'$0.29$'),('B water',r'$2.2\times10^{9}$ Pa')]
        for i,(a,b) in enumerate(rows):
            y=4.4-.72*i
            txt(ax,0.4,y,a,fontsize=8.6)
            txt(ax,5.9,y,b,fontsize=8.6,color=T)
            ax.plot([.35,9.0],[y-.24,y-.24],color='#dfe9e6',lw=.8)
        return 'Numbers worth carrying into the exam'
    if key=='atomic_well':
        graph(ax); r=np.linspace(.82,2.4,400)
        U=-1.0/(r**12)+2*1.0/(r**6)
        ax.plot(r,np.minimum(U,2.05),color=I,lw=1.9)
        ax.plot([.82,2.4],[0,0],color=G,lw=.9)
        rr=np.linspace(.87,1.16,100); kk=72
        ax.plot(rr,np.minimum(-1+0.5*kk*(rr-1)**2,2.05),color=T,lw=1.4,ls='--')
        ax.plot([1],[-1],'o',ms=4,color=R)
        ax.text(1.02,-1.22,r'$r_0$',fontsize=8.2,color=R)
        arrow(ax,(1.62,0),(1.62,1.0),I,1.0,'<->',7); ax.text(1.66,.48,'D',fontsize=8.4,color=I)
        ax.text(1.08,1.76,'harmonic near the base',fontsize=6.8,color=T)
        ax.text(1.80,1.00,'asymmetric tail:',fontsize=6.8,color=R)
        ax.text(1.80,.80,'thermal expansion',fontsize=6.8,color=R)
        ax.set_xlabel(r'separation  r  ($r_0$ units)',fontsize=8.6)
        ax.set_ylabel(r'potential $U$',fontsize=8.6)
        ax.set_xlim(.8,2.4); ax.set_ylim(-1.35,2.05)
        return 'Well curvature sets Y; well asymmetry sets thermal expansion'
    if key=='potential_cubic':
        graph(ax); s=np.linspace(-.55,.85,300)
        U=0.5*s**2-(1/6)*1.2*s**3
        ax.plot(s,U,color=I,lw=1.9,label='asymmetric well')
        ax.plot(s,0.5*s**2,color=G,lw=1.1,ls='--',label='parabola')
        ax.axhline(0,color=G,lw=.8)
        ax.set_xlabel(r'displacement  s / $r_0$',fontsize=8.6)
        ax.set_ylabel(r'$U(s)$ (scaled)',fontsize=8.6)
        ax.legend(fontsize=7.6,frameon=False,loc='upper left')
        ax.set_xlim(-.55,.85); ax.set_ylim(0,.65)
        return 'A cubic term makes the well softer outward and the mean separation drift'
    if key=='alpha_scale':
        graph(ax); D=np.linspace(.8,6,200)
        ax.plot(D,1.45e-5*(3/D),color=T,lw=2.0)
        ax.plot([3],[1.45e-5],'o',ms=4.5,color=R)
        ax.annotate('3 eV bond',(3,1.45e-5),xytext=(3.4,1.22e-5),fontsize=7.4,color=R,
                    arrowprops=dict(arrowstyle='->',color=R,lw=.7))
        ax.set_xlabel('bond depth  D  (eV)',fontsize=8.6)
        ax.set_ylabel(r'$\alpha$  ($10^{-5}$ K$^{-1}$)',fontsize=8.4)
        ax.set_yticks([0.5e-5,1.0e-5,1.5e-5]); ax.set_yticklabels(['0.5','1.0','1.5'])
        ax.set_ylim(.4e-5,1.62e-5); ax.set_xlim(.8,6)
        return 'Deeper well, smaller expansion: alpha about k_B / 2D'
    if key=='rod_mass_impact':
        graph(ax)
        bars=['M alone','M + m/2','M + m']
        vals=[2.7,6.2,10.7]
        ax.bar(bars,vals,color=[G,T,'#cfe8e1'],width=.5)
        for i,v in enumerate(vals): ax.text(i,v+.16,f'{v:.1f}',ha='center',fontsize=8.4,color=I)
        ax.set_ylabel('extension  (mm)',fontsize=8.6); ax.set_ylim(0,12.4)
        ax.tick_params(axis='x',labelsize=7.8)
        return 'Rod weight at half displacement: 6.2 mm, against 10.7 mm if all of m is added'
    if key=='wave_transit':
        graph(ax); t=np.logspace(-3,3,300); tr=0.4
        ax.semilogx(t,1+tr/(t+tr),color=I,lw=1.9)
        ax.axvline(tr,color=R,ls='--',lw=1.0)
        ax.axhline(1.0,color=G,ls=':',lw=1.0)
        ax.text(70,1.10,'static limit',fontsize=7.4,color=T)
        ax.text(tr*1.18,1.86,'L/c',fontsize=8.0,color=R)
        ax.text(1.15e-3,1.42,'impact',fontsize=7.6,color=T)
        ax.set_xlabel('load rise time  (ms)',fontsize=8.6)
        ax.set_ylabel('peak / static',fontsize=8.6)
        ax.set_xlim(1e-3,1e3); ax.set_ylim(0.95,2.05)
        ax.set_yticks([1.0,1.5,2.0])
        return 'The static-shape energy method needs loading long compared with L/c'
    if key=='constant_stress':
        graph(ax); x=np.linspace(0,6,200)
        ax.plot(x,np.exp(x/2.2),color=T,lw=2.0,label=r'$A_0e^{x/\lambda}$')
        ax.plot(x,np.ones_like(x),color=G,lw=1.1,ls='--',label='prismatic')
        ax.plot([2.2],[np.exp(1)],'o',ms=4,color=R)
        ax.text(2.36,1.72,r'$x=\lambda$',fontsize=8.2,color=R)
        ax.set_xlabel('depth x below the load',fontsize=8.6)
        ax.set_ylabel(r'$A/A_0$',fontsize=8.6)
        ax.set_xlim(0,5.95); ax.set_ylim(0,15); ax.legend(fontsize=7.6,frameon=False,loc='upper left')
        return 'Constant stress needs an exponential flare; lambda = sigma0/(rho g)'
    if key=='taper_profile':
        plain(ax)
        for cx,lam,lab in [(2.45,2.30,'long $\\lambda$'),(7.10,1.22,'short $\\lambda$')]:
            y=np.linspace(0,3.20,160); w=.13*np.exp(y/lam); yy=4.15-y
            ax.fill_betweenx(yy,cx-w,cx+w,color='#e6efed',alpha=.7)
            ax.plot(cx-w,yy,color=I,lw=1.2); ax.plot(cx+w,yy,color=I,lw=1.2)
            ax.plot([cx-w[0],cx+w[0]],[4.15,4.15],color=I,lw=1.2)
            arrow(ax,(cx,4.78),(cx,4.22),R,1.1,'-|>',9)
            txt(ax,cx+.14,4.60,'W',color=R,fontsize=8.0)
            wall(ax,cx-1.75,cx+1.75,.95,up=False)
            note(ax,cx,.35,lab,ha='center',fontsize=7.8,color=T)
        note(ax,4.85,2.30,'same stress,\ndifferent profile',ha='center',fontsize=7.2)
        return 'Constant stress: a short decay length needs a violent flare'
    if key=='cantilever_integrated':
        graph(ax); x=np.linspace(0,1,200)
        ax.plot(x,-(x**2*(3-x))/2,color=I,lw=1.9)
        ax.plot(x,-(x*(2-x))/2,color=T,lw=1.2,ls='--')
        ax.plot(x,-(1-x),color=G,lw=1.2,ls=':')
        txt(ax,.84,-.98,r'$\delta$',color=I,fontsize=8.0)
        txt(ax,.05,-.235,'slope',color=T,fontsize=7.2)
        txt(ax,.60,-.78,'moment',color=G,fontsize=7.2)
        ax.set_xlabel('x / L',fontsize=8.6); ax.set_ylabel('normalised',fontsize=8.6)
        ax.set_xlim(0,1.02); ax.set_ylim(-1.16,.10); ax.set_yticks([-1,-.5,0])
        return 'Integrate twice: slope from the moment, deflection from the slope'
    if key=='buckling':
        graph(ax); c=np.logspace(0,2.4,200)
        ax.loglog(c,1/c**2,color=I,lw=2.0)
        ax.axhline(1.0,color=R,lw=1.2)
        ax.axvline(1.0,color=R,lw=.7,ls=':')
        ax.fill_between(c,1/c**2,1.0,where=1/c**2<1.0,color='#eaf3f0',alpha=.9)
        ax.text(14,0.05,'buckling governs',fontsize=7.6,color=T)
        ax.text(1.3,1.32,'yield governs',fontsize=7.6,color=R)
        ax.text(1.7,0.30,r'$P_{cr}=\pi^{2}YI/L^{2}$',fontsize=8.2,color=I)
        ax.set_xlabel(r'slenderness  $L/R$',fontsize=8.6)
        ax.set_ylabel(r'$P/P_{\rm yield}$',fontsize=8.6)
        ax.set_xlim(1,250); ax.set_ylim(.004,8)
        return 'The column fails at the smaller of buckling and yield'
    if key=='euler_modes':
        plain(ax)
        for i,(lab,amp) in enumerate([('pinned',.55),('fixed-free',.40),('fixed-fixed',.75)]):
            x0=.9+3.1*i; y0=1.20; L=2.7
            ys=np.linspace(0,L,120)
            if i==0: yy=y0+amp*np.sin(np.pi*ys/L); mult='1'
            elif i==1: yy=y0+amp*(1-np.cos(np.pi*ys/(2*L))); mult='0.25'
            else: yy=y0+amp*(1-np.cos(2*np.pi*ys/L))/2; mult='4'
            wall(ax,x0-.35,x0+.35,y0,n=5)
            ax.plot(x0+(yy-y0),ys,color=T,lw=1.5)
            ax.plot([x0,x0],[y0,y0+L],color=G,lw=.7,ls=':')
            txt(ax,x0,L+1.55,lab,ha='center',fontsize=7.6,color=T)
            txt(ax,x0,L+1.25,mult,ha='center',fontsize=7.6,color=I)
        txt(ax,5.0,4.75,'Euler load multiplier',ha='center',fontsize=8.0,color=G)
        return 'End conditions change the Euler load by the factor shown'
    if key=='ibeam':
        plain(ax)
        ax.add_patch(Rectangle((1.30,1.95),.95,2.85,fc='#e6efed',ec=I,lw=1.4))
        txt(ax,1.78,4.99,'rectangle 20x40',ha='center',fontsize=7.2,color=T)
        dimy(ax,.98,1.95,4.80,'40',sign=-1)
        ax.add_patch(Rectangle((5.10,4.40),2.40,.33,fc='#e6efed',ec=I,lw=1.3))
        ax.add_patch(Rectangle((5.10,1.95),2.40,.33,fc='#e6efed',ec=I,lw=1.3))
        ax.add_patch(Rectangle((6.10,2.28),.40,2.12,fc='#e6efed',ec=I,lw=1.3))
        txt(ax,6.30,4.99,'I-section, same area',ha='center',fontsize=7.2,color=T)
        ax.plot([1.20,7.95],[3.375,3.375],color=G,lw=.9,ls='--')
        note(ax,4.62,3.10,'NA',fontsize=7.2)
        txt(ax,.55,1.42,'I/A = 133 mm^2',fontsize=7.2)
        txt(ax,.55,1.06,'equal depth: 530',fontsize=6.8,color=T)
        txt(ax,.55,.72,'depth alone gives 4x',fontsize=6.6,color=R)
        txt(ax,4.75,1.42,'flanges: Ad^2',fontsize=6.8,color=T)
        txt(ax,4.75,1.06,'not bh^3/12, so the',fontsize=6.6)
        txt(ax,4.75,.72,'profile adds the last 1.9x',fontsize=6.6,color=I)
        ax.set_ylim(.35,5.25)
        return 'An I-section puts area where y is large; compare at equal depth and area'
    if key=='s_shadow':
        plain(ax)
        cx,cy,RR,r=2.92,2.20,2.12,1.17
        ax.add_patch(Circle((cx,cy),RR,fc='white',ec=I,lw=1.3))
        ax.add_patch(Circle((cx,cy),r,fc='#fdf0d5',ec=GOLD,lw=1.1))
        S=np.array([cx,cy+RR])
        ax.plot([S[0]],[S[1]],'*',ms=11,color=R)
        txt(ax,cx+.24,S[1]+.06,'source',fontsize=7.2,color=R)
        U=[]
        for sgn in (1,-1):
            th=np.arccos(r/RR)
            ct=np.array([-np.sin(sgn*th),np.cos(th)])
            Tt=np.array([cx,cy])+r*ct
            dv=Tt-S; dv/=np.linalg.norm(dv)
            b=2*float((S-np.array([cx,cy]))@dv)
            Uu=S-b*dv; U.append(Uu)
            ax.plot([S[0],Uu[0]],[S[1],Uu[1]],color=I,lw=1.0)
        a1=np.degrees(np.arctan2(U[0][1]-cy,U[0][0]-cx))
        a2=np.degrees(np.arctan2(U[1][1]-cy,U[1][0]-cx))
        ax.add_patch(Arc((cx,cy),2*(RR+.10),2*(RR+.10),theta1=min(a1,a2),theta2=max(a1,a2),
                         color='#cfe1dc',lw=7))
        txt(ax,6.05,1.10,'S shadow',ha='left',fontsize=7.4,color=T)
        txt(ax,cx,cy-.05,'liquid core',ha='center',fontsize=7.2,color=GOLD)
        txt(ax,cx,cy-.45,'G = 0',ha='center',fontsize=7.2,color=GOLD)
        txt(ax,6.05,3.62,'grazing rays',fontsize=7.2,color=I)
        txt(ax,6.05,3.32,'mark the edge',fontsize=7.2,color=I)
        arrow(ax,(5.96,3.55),(5.06,2.80),G,.9,'->',7)
        txt(ax,6.05,2.36,'core radius 0.55 R',fontsize=7.2,color=G)
        return 'The S shadow: rays that would cross the liquid core never arrive'
    if key=='hooke_limit':
        graph(ax); e=np.linspace(-.03,.03,300)
        ax.plot(e,1e3*(e+ (e**2)/.06*3),color=I,lw=1.8,label='with cubic term')
        ax.plot(e,1e3*e,color=G,lw=1.1,ls='--',label='Hooke')
        ax.set_xlabel('strain  ε',fontsize=8.6); ax.set_ylabel('stress (arbitrary)',fontsize=8.6)
        ax.axhline(0,color=G,lw=.7)
        ax.legend(fontsize=7.4,frameon=False,loc='upper left')
        ax.set_xlim(-.03,.03); ax.set_ylim(-80,90)
        return 'The cubic correction is tension-compression asymmetric, and tiny before yield'
    if key=='hysteresis':
        graph(ax); th=np.linspace(0,2*np.pi,300)
        ax.plot(2.2+1.3*np.cos(th),1.6+.55*np.sin(th),color=I,lw=1.7)
        arrow(ax,(3.42,1.72),(3.38,1.94),T,1.1)
        arrow(ax,(0.98,1.48),(1.02,1.26),G,1.1)
        txt(ax,2.2,2.36,'loading',fontsize=7.8,color=T,ha='center')
        txt(ax,2.2,.86,'unloading',fontsize=7.8,color=G,ha='center')
        txt(ax,2.2,1.62,'loop area',fontsize=7.6,color=R,ha='center')
        txt(ax,2.2,1.44,'= heat',fontsize=7.6,color=R,ha='center')
        ax.set_xlabel('strain',fontsize=8.8); ax.set_ylabel('stress',fontsize=8.8)
        ax.set_xticks([0.9,3.5]); ax.set_xticklabels(['0','max']); ax.set_yticks([1.05,2.15]); ax.set_yticklabels(['0','max'])
        ax.set_xlim(.8,3.6); ax.set_ylim(.8,2.5)
        return 'Hysteresis: unloading returns by a different curve; the loop is lost energy'
    if key=='hoop_stress':
        plain(ax)
        ax.add_patch(Rectangle((.75,1.45),3.90,1.75,fc='#eff6f4',ec=I,lw=1.4))
        ax.add_patch(Rectangle((.75,1.45),.18,1.75,fc='#dfe9e6',ec=I,lw=1.0))
        ax.add_patch(Rectangle((4.47,1.45),.18,1.75,fc='#dfe9e6',ec=I,lw=1.0))
        for yy in [1.80,2.32,2.84]:
            arrow(ax,(.98,yy),(4.42,yy),T,lw=.9)
        arrow(ax,(.93,3.42),(4.47,3.42),I,1.0,'<->',7)
        txt(ax,2.70,3.52,'2r',ha='center',fontsize=7.6)
        arrow(ax,(5.28,.72),(4.74,1.44),G,.85,'->',6)
        note(ax,5.34,.62,'wall t,  t << r',fontsize=6.8)
        txt(ax,2.70,1.10,'p acts on the cut face 2rL',ha='center',fontsize=7.2,color=T)
        txt(ax,5.35,3.42,r'$\sigma_{\rm hoop}=pr/t$',fontsize=8.8)
        txt(ax,5.35,2.72,r'$\sigma_{\rm long}=pr/(2t)$',fontsize=8.8)
        note(ax,5.35,2.14,'hoop wins: the crack',fontsize=7.2)
        note(ax,5.35,1.88,'runs lengthwise',fontsize=7.2)
        txt(ax,2.70,.55,'two walls carry it',ha='center',fontsize=7.2,color=G)
        return 'Hoop stress by a diametral cut: pr/t, twice the longitudinal stress'
    if key=='vessel_crack':
        plain(ax)
        ax.add_patch(Rectangle((.55,1.55),4.10,1.90,fc='#eff6f4',ec=I,lw=1.4))
        ax.add_patch(Rectangle((.55,1.55),4.10,.16,fc='#dfe9e6',ec=I,lw=.9))
        ax.add_patch(Rectangle((.55,3.29),4.10,.16,fc='#dfe9e6',ec=I,lw=.9))
        ax.plot([2.10,3.05],[1.63,1.63],color=R,lw=2.6)
        ax.text(2.55,1.15,'crack along a generator',ha='center',fontsize=7.6,color=R)
        txt(ax,2.55,2.45,'p',ha='center',fontsize=9.0,color=T)
        txt(ax,5.35,3.30,r'$\sigma_{\rm hoop}=pr/t$',fontsize=8.8)
        txt(ax,5.35,2.62,r'$\sigma_{\rm long}=pr/2t$',fontsize=8.8)
        note(ax,5.35,2.10,'thin wall: t << r',fontsize=7.4)
        note(ax,5.35,1.82,'gun barrel: not thin',fontsize=7.4)
        return 'Hoop stress is twice longitudinal: the vessel splits lengthwise'
    if key=='wave_speeds':
        graph(ax)
        names=['rod','bulk P','steel S']
        vals=[5.1,5.8,3.2]
        ax.bar(names,vals,color=[T,I,G],width=.5)
        for i,v in enumerate(vals): ax.text(i,v+.18,f'{v:.1f}',ha='center',fontsize=8.2,color=I)
        ax.set_ylim(0,7.6)
        for i in range(3): ax.text(i,7.0,'',ha='center')
        ax.text(0,-1.15,'Y/rho',ha='center',fontsize=6.8,color=T)
        ax.text(1,-1.15,'(B+4G/3)/rho',ha='center',fontsize=6.2,color=T)
        ax.text(2,-1.15,'G/rho',ha='center',fontsize=6.8,color=T)
        ax.set_ylabel('speed  (km/s)',fontsize=8.4)
        ax.set_xticks([0,1,2]); ax.set_xticklabels(['rod','bulk P','steel S'],fontsize=8.0)
        ax.tick_params(axis='x',length=0,pad=16)
        return 'Rod, bulk-P and S speeds use different moduli: 5.1, 5.8, 3.2 km/s'
    if key=='ashby':
        graph(ax); ax.set_xscale('log'); ax.set_yscale('log')
        rho=np.logspace(2,4,50)
        ax.plot(rho,1e-4*rho,color=G,lw=1.0,ls='--')
        ax.plot(rho,4e-8*rho**2,color=T,lw=1.0,ls=':')
        ax.text(6.0e2,7e-2,'Y/rho',fontsize=7.2,color=G)
        ax.text(3.2e3,6.0,'Y^.5/rho',fontsize=7.2,color=T)
        pts=[(7800,2.0e2,'steel',.62,1.8),(2700,7.0e1,'al',1.5,1.4),(1600,1.5e2,'CFRP',.55,1.6),
             (1300,1.0e-2,'silk',1.4,.55),(1100,3.0e-3,'rubber',1.4,.5),(600,1.0e1,'wood',1.4,1.3)]
        for x,y,lab,fx,fy in pts:
            ax.plot([x],[y],'o',ms=4.2,color=R)
            ax.text(x*fx,y*fy,lab,fontsize=7.2,color=I)
        ax.set_xlim(3e2,1.2e4); ax.set_ylim(1e-3,6e2)
        ax.set_xlabel(r'density  $\rho$  (kg m$^{-3}$)',fontsize=8.6)
        ax.set_ylabel(r'$Y$  (GPa)',fontsize=8.6)
        return 'Materials chart: stiffness and density are independent axes'
    raise ValueError(key)

def _extra(ax,key):
    if key=='specific_strength':
        graph(ax)
        labels=['steel','aluminium','CFRP','silk']
        ss=[3.2e4,7.4e4,9.4e5,7.7e5]
        sm=[2.6e7,2.6e7,9.4e7,7.7e6]
        x=np.arange(len(labels))
        ax.bar(x-.18,ss,width=.34,color=T,label='strength/density')
        ax.bar(x+.18,sm,width=.34,color=I,label='modulus/density')
        ax.set_yscale('log'); ax.set_xticks(x); ax.set_xticklabels(labels,fontsize=7.8)
        ax.set_ylabel('specific value (m^2/s^2)',fontsize=7.6)
        ax.legend(fontsize=6.8,frameon=False,loc='upper center',bbox_to_anchor=(.5,1.24),ncol=2)
        ax.set_ylim(1e4,4e8)
        return 'Cable ranks by strength/density; a light stiff beam by modulus/density'
    if key=='transformed_section':
        plain(ax)
        ax.add_patch(Rectangle((.55,2.40),2.7,1.00,fc='#e6efed',ec=I,lw=1.2))
        ax.add_patch(Rectangle((3.25,2.40),1.5,1.00,fc=GOLDF,ec=I,lw=1.2))
        ax.plot([.35,5.0],[2.90,2.90],color=G,lw=.9,ls='--')
        txt(ax,1.90,2.78,'steel',ha='center',fontsize=7.6)
        txt(ax,4.00,2.78,'copper',ha='center',fontsize=7.6)
        arrow(ax,(2.05,3.62),(1.75,3.10),R,1.0); txt(ax,2.15,3.58,'axis moves toward steel',fontsize=6.6,color=R)
        note(ax,.55,2.10,'dashed: geometric centre',fontsize=6.8)
        ax.add_patch(Rectangle((5.6,2.40),1.5,1.00,fc=GOLDF,ec=I,lw=1.1))
        ax.add_patch(Rectangle((7.1,2.40),3.0,1.00,fc='#e6efed',ec=I,lw=1.1,alpha=.7))
        txt(ax,8.60,2.78,'n x copper',ha='center',fontsize=7.0)
        txt(ax,5.60,3.62,'transformed section',ha='center',fontsize=7.0,color=T)
        note(ax,.55,1.55,'widen the weaker material by n = Y2/Y1,',fontsize=7.0)
        note(ax,.55,1.28,'then apply the one-material formulas',fontsize=7.0)
        ax.set_xlim(0,10.4)
        return 'A composite beam becomes one material if the weak side is widened by n'
    if key=='stress_element':
        plain(ax)
        ax.add_patch(Rectangle((2.7,2.05),2.6,1.9,fc='#eff6f4',ec=I,lw=1.3))
        arrow(ax,(5.3,2.55),(6.10,2.55),R,1.2); arrow(ax,(2.7,2.55),(1.90,2.55),R,1.2)
        arrow(ax,(4.00,3.95),(4.00,4.60),T,1.2); arrow(ax,(4.00,2.05),(4.00,1.40),T,1.2)
        arrow(ax,(5.30,3.60),(6.10,3.60),I,1.0); arrow(ax,(2.70,2.40),(1.90,2.40),I,1.0)
        txt(ax,6.14,2.50,r'$\sigma_x$',color=R,fontsize=8.2)
        txt(ax,4.06,4.68,r'$\sigma_y$',color=T,fontsize=8.2)
        txt(ax,6.14,3.54,r'$\tau_{xy}$',color=I,fontsize=7.8)
        txt(ax,1.62,2.72,r'$\sigma_x$',color=R,fontsize=8.2,ha='right')
        txt(ax,4.06,1.22,r'$\sigma_y$',color=T,fontsize=8.2,ha='center')
        note(ax,2.70,.62,'three numbers fix the state',fontsize=7.6)
        ax.set_xlim(.9,7.4); ax.set_ylim(.3,5.0)
        return 'Plane stress: sigma_x, sigma_y and tau_xy, with the sign convention fixed once'
    if key=='mohr':
        ax.axis('off')
        bx=ax.figure.add_axes([.045,.14,.46,.77]); graph(bx)
        bx.set_aspect('equal',adjustable='box')
        sx,sy,txy=80.,20.,30.
        c=(sx+sy)/2; rr=np.hypot((sx-sy)/2,txy)
        th=np.linspace(0,2*np.pi,400)
        bx.plot(c+rr*np.cos(th),rr*np.sin(th),color=I,lw=1.8)
        bx.plot([sx,sy],[txy,-txy],color=T,lw=1.0,ls='--')
        bx.plot([sx,sy],[txy,-txy],'o',ms=4,color=T)
        bx.axhline(0,color=G,lw=.9)
        bx.axvline(c,color=R,lw=.7,ls=':')
        bx.plot([c+rr,c-rr],[0,0],'o',ms=3.6,color=R)
        bx.text(c+rr+2,9,r'$\sigma_1$',fontsize=8.0,color=R,ha='left')
        bx.text(c-rr-2,9,r'$\sigma_2$',fontsize=8.0,color=R,ha='right')
        bx.text(c+5,-14,'$\\tau_{\\max}=R$',fontsize=7.4,color=I,ha='left')
        bx.text(sx-3,txy+8,r'$(\sigma_x,\tau_{xy})$',fontsize=7.0,color=T,ha='right')
        bx.set_xlabel(r'$\sigma$  (MPa)',fontsize=8.2); bx.set_ylabel(r'$\tau$  (MPa)',fontsize=8.2)
        bx.set_xlim(-16,114); bx.set_ylim(-58,58)
        bx.set_xticks([0,25,50,75,100]); bx.set_yticks([-50,-25,0,25,50])
        ax.text(.600,.90,'given',fontsize=7.6,color=T,transform=ax.transAxes)
        ax.text(.600,.815,r'$\sigma_x=80$ MPa',fontsize=8.0,color=I,transform=ax.transAxes)
        ax.text(.600,.735,r'$\sigma_y=20$ MPa',fontsize=8.0,color=I,transform=ax.transAxes)
        ax.text(.600,.655,r'$\tau_{xy}=30$ MPa',fontsize=8.0,color=I,transform=ax.transAxes)
        ax.text(.600,.525,'centre',fontsize=7.6,color=T,transform=ax.transAxes)
        ax.text(.600,.44,r'$C=50$ MPa',fontsize=8.0,color=I,transform=ax.transAxes)
        ax.text(.600,.325,'radius',fontsize=7.6,color=T,transform=ax.transAxes)
        ax.text(.600,.24,r'$R=42.4$ MPa',fontsize=8.0,color=I,transform=ax.transAxes)
        ax.text(.600,.115,r'$\sigma_1=92.4$ MPa',fontsize=8.0,color=R,transform=ax.transAxes)
        ax.text(.600,.035,r'$\sigma_2=7.6$ MPa',fontsize=8.0,color=R,transform=ax.transAxes)
        return 'Mohr circle to scale: principal stresses are where the circle meets the axis'
    raise ValueError(key)
