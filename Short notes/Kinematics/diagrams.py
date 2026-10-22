"""Analytic, labelled kinematics schematics and diagnostic plots."""
import numpy as np
from matplotlib.patches import Circle, Rectangle

INK = '#153149'
TEAL = '#087d7d'
RED = '#a43232'
GOLD = '#b7950b'

def text(ax, x, y, s, **kw):
    ax.text(x, y, s, color=INK, fontsize=kw.pop('fontsize', 9), **kw)

def arrow(ax, a, b, color=TEAL, label=None, offset=(0.05, 0.08)):
    ax.annotate('', xy=b, xytext=a,
                arrowprops=dict(arrowstyle='->', color=color, lw=1.8))
    if label:
        text(ax, (a[0]+b[0])/2+offset[0], (a[1]+b[1])/2+offset[1], label,
             fontsize=9, ha='center')

def base(ax):
    ax.set_xlim(-3, 3); ax.set_ylim(-1.9, 1.9); ax.axis('off'); ax.set_aspect('equal')

def axes(ax, xlim=(0, 5), ylim=(0, 4), xlabel='t (s)', ylabel='value'):
    ax.set_xlim(*xlim); ax.set_ylim(*ylim)
    ax.set_xlabel(xlabel, fontsize=8); ax.set_ylabel(ylabel, fontsize=8)
    ax.spines[['top','right']].set_visible(False)
    ax.tick_params(labelsize=7, length=2)
    ax.grid(alpha=.15)
    ax.set_xticks(np.linspace(xlim[0], xlim[1], 3))
    ax.set_yticks(np.linspace(ylim[0], ylim[1], 3))

def schematic(ax, theme):
    base(ax)
    if theme == 'position':
        ax.plot([-2.5,2.5],[0,0],color=INK,lw=1.4)
        for x,label in [(-2,'0'),(0,'2'),(2,'5')]:
            ax.plot([x,x],[-.1,.1],color=INK,lw=1); text(ax,x,-.32,label,ha='center')
        CirclePatch=Circle((0,0),.12,color=TEAL); ax.add_patch(CirclePatch)
        arrow(ax,(0,.35),(2,.35),TEAL,'+3 m',(0,.16))
        arrow(ax,(2,.7),(1,.7),RED,'-2 m',(0,.16))
        text(ax,-2.7,1.35,'start x=2; turn at x=5; finish x=3')
        text(ax,-2.7,-1.1,'net +1 m; path length 5 m')
    elif theme == 'velocity':
        ax.plot([-2.6,2.6],[0,0],color=INK,lw=1.2)
        for x,name,v,c in [(-1.4,'A',5,TEAL),(1.2,'B',3,RED)]:
            CirclePatch=Circle((x,.2),.16,fc='white',ec=c,lw=1.8); ax.add_patch(CirclePatch)
            text(ax,x,.72,name,ha='center')
            arrow(ax,(x,.2),(x+v*.18,.2),c,f'{v} m/s',(.12,-.26))
        text(ax,-2.6,-.65,'same frame; v_A/B = 2 m/s')
    elif theme == 'accel':
        CirclePatch=Circle((-1.85,.15),.2,fc='white',ec=TEAL,lw=1.8); ax.add_patch(CirclePatch)
        arrow(ax,(-1.6,.15),(-.45,.15),TEAL,'v > 0',(0,.2))
        arrow(ax,(-1.6,-.3),(-2.65,-.3),RED,'a < 0',(0,-.26))
        text(ax,-1.55,1.15,'opposite: slows down',ha='center')
        CirclePatch=Circle((2.1,.15),.2,fc='white',ec=RED,lw=1.8); ax.add_patch(CirclePatch)
        arrow(ax,(1.85,.15),(.75,.15),RED,'v < 0',(0,.2))
        arrow(ax,(1.85,-.3),(.75,-.3),RED,'a < 0',(0,-.26))
        text(ax,1.45,1.15,'same sign: speeds up',ha='center')
    elif theme == 'graphs':
        text(ax,-2.7,1.4,'x-t: tangent slope = v')
        text(ax,-2.7,.65,'v-t: slope = a; signed area = Δx')
        text(ax,-2.7,-.1,'a-t: signed area = Δv')
        arrow(ax,(-2.5,-.8),(2.4,-.8),TEAL,'time',(0,-.22))
        text(ax,-2.4,-1.5,'integrate downward; differentiate upward')
    elif theme == 'constant-a':
        ax.plot([-2.1,2.2],[0,0],color=INK,lw=1.4)
        ax.plot([-1.6,1.4],[-.9,1.05],color=TEAL,lw=2)
        text(ax,-2.4,1.25,'v-t straight line; slope a')
        ax.fill_between([-1.6,1.4],[0,0],[-.9,1.05],color=TEAL,alpha=.12)
        text(ax,-1.9,-1.45,'area = displacement')
    elif theme == 'freefall':
        ax.plot([0,0],[-1.3,1.25],color=INK,lw=1.8)
        CirclePatch=Circle((0,1.05),.15,fc=GOLD,ec=INK,lw=1); ax.add_patch(CirclePatch)
        arrow(ax,(.5,.8),(.5,-.8),RED,'g downward',(0,0))
        arrow(ax,(1.1,1.0),(2.0,1.0),TEAL,'u',(0,.18))
        text(ax,-2.4,-1.5,'at apex: v=0, acceleration still -g')
    elif theme == 'nth':
        ax.plot([-2.4,2.4],[0,0],color=INK,lw=1.2)
        ax.plot([-2.2,2.2],[-.7,1.0],color=TEAL,lw=2)
        ax.fill_between([-.5,.8],[0,0],[-.02,.44],color=GOLD,alpha=.32)
        text(ax,-2.5,1.35,'shade one interval: [n-1,n] s')
        text(ax,-1.5,-1.2,'signed area; split at v=0 for distance')
    elif theme == 'variable-a':
        arrow(ax,(-2.2,.5),(-.4,.5),TEAL,'a(t)',(0,.18))
        arrow(ax,(-.2,.5),(1.3,.5),TEAL,'integrate',(0,.18))
        arrow(ax,(1.45,.5),(2.7,.5),TEAL,'v(t)',(0,.18))
        arrow(ax,(1.45,-.45),(2.7,-.45),GOLD,'integrate',(0,-.2))
        text(ax,-2.2,-1.1,'insert initial conditions at each step')
    elif theme == 'vdv':
        CirclePatch=Circle((-.7,.1),.9,fill=False,ec=TEAL,lw=1.8); ax.add_patch(CirclePatch)
        arrow(ax,(-.7,.1),(.3,.1),TEAL,'v',(.1,-.26))
        arrow(ax,(-.7,.1),(-.7,1.1),RED,'a(x)',(-.42,.12))
        text(ax,.65,.7,'a = v dv/dx')
        text(ax,.65,.1,'integrate to v²(x)')
        text(ax,.65,-.55,'turn where v² = 0')
    elif theme == 'relative1d':
        ax.plot([-2.6,2.6],[0,0],color=INK,lw=1.2)
        CirclePatch=Circle((-.8,.15),.18,fc='white',ec=TEAL,lw=1.5); ax.add_patch(CirclePatch)
        CirclePatch=Circle((1.0,.15),.18,fc='white',ec=RED,lw=1.5); ax.add_patch(CirclePatch)
        text(ax,-.8,.55,'A'); text(ax,1.0,.55,'B')
        arrow(ax,(-.6,.15),(.35,.15),TEAL,'v_A',(0,.17))
        arrow(ax,(1.2,-.25),(.3,-.25),RED,'v_B',(0,-.18))
        text(ax,-2.3,-1.0,'r=x_A-x_B; approach if r dr/dt < 0')
    elif theme == 'piecewise':
        ax.plot([-2.4,-.8,.7,2.3],[-.8,.9,.9,-.8],color=TEAL,lw=2.2)
        ax.axhline(0,color=INK,lw=1)
        for x in [-.8,.7]: ax.plot([x,x],[-1.0,1.1],ls=':',color=RED,lw=1)
        text(ax,-2.3,1.35,'accelerate | cruise | brake')
        text(ax,-1.9,-1.45,'match x and v at each phase boundary')
    elif theme in ('projectile','horizontal','projectile-general','trajectory','range','elevated','envelope','incline'):
        x=np.linspace(-2.4,2.3,160)
        if theme=='envelope':
            y=.9-.24*x*x
            ax.plot(x,y,color=RED,ls='--',lw=2,label='envelope')
            for th in [.35,.62,.9]:
                ax.plot(x,.7*np.tan(th)-.16*x*x/(np.cos(th)**2),alpha=.55,lw=1.2)
            text(ax,-2.55,1.45,'family of arcs; dashed curve is envelope',fontsize=8)
        elif theme=='incline':
            ax.plot([-2.6,2.6],[-1.0,.9],color=INK,lw=2)
            arrow(ax,(-1.6,-.3),(-.5,.1),TEAL,'launch β above slope',(0,.2))
            ax.plot(np.linspace(-1.6,1.8,80),-.3+.4*np.linspace(-1.6,1.8,80)-.23*np.linspace(-1.6,1.8,80)**2,color=RED,lw=1.7)
            text(ax,-2.5,1.35,'gravity: along slope and normal')
        else:
            y=.8*x-.22*x*x
            ax.plot(x,y,color=TEAL,lw=2)
            ax.plot([x[0],x[-1]],[0,0],color=INK,lw=1)
            arrow(ax,(-2.1,-.75),(-1.1,-.75),TEAL,'v_x',(0,.16))
            arrow(ax,(-2.1,-.75),(-2.1,.2),RED,'v_y',(0,0))
            if theme in ('projectile-general','trajectory','elevated','horizontal'):
                text(ax,-2.5,1.35,'split x/y; share time t')
            elif theme=='range':
                text(ax,-2.5,1.35,'θ and 90°-θ: same range')
            else:
                text(ax,-2.5,1.35,'gravity changes vertical velocity only')
        if theme=='elevated':
            ax.plot([-2.4,2.4],[-1.0,-1.0],color=RED,lw=2)
            text(ax,-2.5,-1.45,'solve y(T)=target height')
    elif theme == 'relative2d':
        arrow(ax,(-1.7,-.7),(.4,1.0),TEAL,'v_A',(0,.1))
        arrow(ax,(-1.7,-.7),(.5,-.6),RED,'v_B',(0,-.15))
        arrow(ax,(.5,-.6),(.4,1.0),GOLD,'v_A/B',(.2,0))
        text(ax,-2.5,-1.4,'vector subtraction, not speed subtraction')
    elif theme == 'river':
        ax.add_patch(Rectangle((-2.5,-.85),5,1.7,fc='#e8f4f8',ec='none'))
        arrow(ax,(-2.2,0),(-1.0,0),TEAL,'boat across',(0,.2))
        arrow(ax,(-2.2,0),(-2.2,1.0),RED,'current',(-.35,.15))
        arrow(ax,(-2.2,0),(-1.0,1.0),GOLD,'ground path',(.35,.06))
        text(ax,.1,.65,'across component sets time')
        text(ax,.1,.1,'along component sets drift')
    elif theme == 'aircraft':
        arrow(ax,(-1.6,-.8),(.2,1.0),TEAL,'desired ground track',(0,.15))
        arrow(ax,(-1.6,-.8),(-2.4,.3),RED,'wind',(0,.12))
        arrow(ax,(-2.4,.3),(.2,1.0),GOLD,'airspeed',(0,.15))
        text(ax,.3,-.55,'v_ground = v_air + wind')
    elif theme == 'circle':
        CirclePatch=Circle((0,0),1.25,fill=False,ec=TEAL,lw=2); ax.add_patch(CirclePatch)
        CirclePatch=Circle((1.25,0),.1,color=RED); ax.add_patch(CirclePatch)
        arrow(ax,(1.25,0),(1.25,1.0),TEAL,'v tangent',(0,.12))
        arrow(ax,(1.25,0),(.25,0),RED,'toward centre',(0,.15))
        text(ax,-2.5,1.45,'arc s = Rθ; v = Rω')
    elif theme == 'circ-accel':
        CirclePatch=Circle((0,0),1.1,fill=False,ec=TEAL,lw=1.8); ax.add_patch(CirclePatch)
        CirclePatch=Circle((1.1,0),.1,color=RED); ax.add_patch(CirclePatch)
        arrow(ax,(1.1,0),(.1,0),RED,'a_c',(0,.18))
        arrow(ax,(1.1,0),(1.1,1.0),TEAL,'a_t',(0,.15))
        arrow(ax,(1.1,0),(.55,.75),GOLD,'a',(0,.12))
        text(ax,-2.4,1.35,'normal and tangential components')
    elif theme == 'curvature':
        x=np.linspace(-2.2,2.2,120); y=.35*x*x
        ax.plot(x,y,color=TEAL,lw=2)
        ax.scatter([0],[0],color=RED,s=22,zorder=5)
        arrow(ax,(0,0),(1.1,0),TEAL,'v tangent',(0,.12))
        arrow(ax,(0,0),(0,1.1),RED,'a_perp',(0,.08))
        text(ax,-2.4,-1.35,'ρ = v² / |a_perp|')
    elif theme == 'drag1d':
        arrow(ax,(-.45,1.0),(-.45,-1.1),RED,'gravity',(-.48,-.1))
        arrow(ax,(-.15,.2),(-.15,1.05),TEAL,'drag up',(-.52,.14))
        text(ax,.45,.8,'falling: drag opposes v')
        text(ax,.45,.15,'terminal: weight = drag')
        text(ax,.45,-.5,'a tends to zero')
    elif theme == 'drag2d':
        ax.plot([-2.2,2.2],[-.9,-.9],color=INK,lw=1.8)
        arrow(ax,(-1.5,1.25),(-.5,.9),TEAL,'launch',(0,.1))
        ax.plot(np.linspace(-1.5,1.6,100),.7*np.sin(np.linspace(0,np.pi,100))-0.75*np.linspace(0,1,100),color=RED,lw=2)
        text(ax,-2.4,-1.4,'drag breaks vacuum symmetry')
    elif theme == 'headwind':
        arrow(ax,(-2.2,0),(2.0,0),TEAL,'launch velocity',(0,.18))
        arrow(ax,(1.7,.6),(.4,.6),RED,'constant headwind force',(0,.14))
        text(ax,-2.3,-.75,'time of flight unchanged if vertical motion is unchanged')
    elif theme == 'intercept':
        CirclePatch=Circle((-.8,0),.12,color=TEAL); ax.add_patch(CirclePatch)
        CirclePatch=Circle((1.5,.7),.15,color=RED); ax.add_patch(CirclePatch)
        arrow(ax,(1.5,.7),(2.5,.7),RED,'target velocity',(0,.15))
        arrow(ax,(-.8,0),(1.2,.55),TEAL,'launch to intercept',(0,.16))
        text(ax,-2.5,-1.15,'solve position equality at a common t')
    elif theme == 'coriolis':
        arrow(ax,(-1.6,-.6),(1.2,-.6),TEAL,'northward path',(0,-.2))
        arrow(ax,(-.85,-.4),(-.85,1.0),RED,'east deflection',(-.55,.16))
        text(ax,.15,.62,'Northern hemisphere')
        text(ax,.15,.05,'first-order estimate only')
    elif theme == 'pursuit':
        ax.plot([-1.2,2.4],[0,0],color=INK,lw=1.2)
        CirclePatch=Circle((0,0),.1,color=RED); ax.add_patch(CirclePatch)
        CirclePatch=Circle((0,1.2),.1,color=TEAL); ax.add_patch(CirclePatch)
        text(ax,-1.15,.18,'target starts at origin')
        text(ax,.12,1.35,'pursuer start')
        arrow(ax,(0,1.1),(0,.15),TEAL,'line of sight',(.22,0))
        arrow(ax,(.2,0),(1.5,0),RED,'target motion',(0,-.18))
        text(ax,-1.2,-1.0,'pursuer velocity aims at current target')
    elif theme == 'model':
        ax.plot([-2.2,2.2],[0,0],color=INK,lw=1.2)
        ax.plot([-2.0,0,2.0],[.1,.1,.1],color=TEAL,lw=3)
        text(ax,-2.4,1.3,'ideal model -> prediction')
        text(ax,-2.4,-.55,'check regime, geometry, initial data')
        text(ax,-2.4,-1.2,'state what breaks the model')
    else:
        text(ax,-2,0,'Kinematics diagram')

def plot(ax, theme):
    if theme in ('position','velocity','accel','graphs','constant-a','freefall','nth','variable-a','vdv','relative1d','piecewise'):
        x=np.linspace(0,5,200)
        if theme=='position':
            axes(ax,(0,5),(0,8),'t (s)','x (m)'); ax.plot(x,1+x+.25*x*x,color=TEAL,lw=2); ax.set_title('x(t): slope is velocity',fontsize=9)
        elif theme=='velocity':
            axes(ax,(0,5),(-2,8),'t (s)','v (m/s)'); ax.plot(x,1+x,color=TEAL,lw=2); ax.set_title('slope gives acceleration',fontsize=9)
        elif theme=='accel':
            axes(ax,(0,5),(-3,3),'t (s)','a (m/s²)'); ax.plot(x,2*np.ones_like(x),color=TEAL,lw=2); ax.axhline(0,color=INK,lw=1)
        elif theme=='graphs':
            axes(ax,(0,5),(-5,5),'t (s)','v (m/s)'); y=4-1.8*x; ax.plot(x,y,color=TEAL,lw=2); ax.fill_between(x,0,y,where=y>=0,color=TEAL,alpha=.18); ax.fill_between(x,0,y,where=y<0,color=RED,alpha=.15); ax.axhline(0,color=INK,lw=1)
        elif theme=='constant-a':
            axes(ax,(0,5),(-1,7),'t (s)','v (m/s)'); ax.plot(x,1+x,color=TEAL,lw=2); ax.fill_between(x,0,1+x,color=TEAL,alpha=.13)
        elif theme=='freefall':
            axes(ax,(0,5),(-6,6),'t (s)','v (m/s)'); ax.plot(x,5-2*x,color=TEAL,lw=2); ax.axhline(0,color=INK,lw=1); ax.scatter([2.5],[0],color=RED,s=22)
        elif theme=='nth':
            axes(ax,(0,5),(-1,8),'t (s)','v (m/s)'); ax.plot(x,1+x,color=TEAL,lw=2); ax.axvspan(2,3,color=GOLD,alpha=.25)
        elif theme=='variable-a':
            axes(ax,(0,5),(0,8),'t (s)','a (m/s²)'); ax.plot(x,.3*x*x,color=TEAL,lw=2)
        elif theme=='vdv':
            xx=np.linspace(-2,2,200); yy=np.sqrt(np.maximum(0,16-4*xx*xx)); axes(ax,(-2,2),(0,4),'x (m)','v (m/s)'); ax.plot(xx,yy,color=TEAL,lw=2); ax.set_title('turning points: v=0',fontsize=9)
        elif theme=='relative1d':
            axes(ax,(0,5),(0,10),'t (s)','gap (m)'); ax.plot(x,8-1.3*x,color=RED,lw=2); ax.axhline(0,color=INK,lw=1)
        elif theme=='piecewise':
            axes(ax,(0,5),(0,8),'t (s)','v (m/s)'); ax.plot([0,1.5,3.5,5],[0,5,5,0],color=TEAL,lw=2.2); ax.fill_between([0,1.5,3.5,5],[0,5,5,0],color=TEAL,alpha=.12)
    elif theme in ('projectile','horizontal','projectile-general','trajectory','range','elevated','envelope','incline','drag2d','headwind'):
        x=np.linspace(0,5,200)
        if theme=='envelope':
            axes(ax,(0,5),(0,5),'x (m)','y (m)'); env=4-.16*x*x; ax.plot(x,env,color=RED,ls='--',lw=2,label='envelope');
            for th in [.35,.65,.9]: ax.plot(x,np.maximum(0,2.6*np.tan(th)-.13*x*x/(np.cos(th)**2)),alpha=.6,lw=1)
            ax.legend(fontsize=7,loc='upper right')
        elif theme=='incline':
            axes(ax,(0,5),(0,4),'slope distance','height'); ax.plot(x,.45*x,color=INK,lw=1.6); ax.plot(x,.6*x-.14*x*x,color=TEAL,lw=2)
        elif theme=='drag2d':
            axes(ax,(0,5),(-1,4),'x (m)','y (m)'); ax.plot(x,2.6*x-.48*x*x,color=TEAL,lw=2,label='vacuum'); ax.plot(x,2.3*x-.51*x*x,color=RED,lw=2,label='drag (schematic)'); ax.legend(fontsize=7)
        elif theme=='headwind':
            axes(ax,(0,5),(-1,4),'t (s)','x (m)'); ax.plot(x,1.6*x,color=TEAL,lw=2,label='no horizontal force'); ax.plot(x,1.6*x-.12*x*x,color=RED,lw=2,label='headwind'); ax.legend(fontsize=7)
        elif theme=='horizontal':
            axes(ax,(0,5),(-5,1),'t (s)','y below launch'); ax.plot(x,-.3*x*x,color=RED,lw=2)
        elif theme=='elevated':
            axes(ax,(0,5),(-2,4),'t (s)','height'); ax.plot(x,1.1*x-.27*x*x,color=TEAL,lw=2); ax.axhline(2,color=RED,ls='--',lw=1)
        else:
            axes(ax,(0,5),(-1,4),'x (m)','y (m)'); ax.plot(x,2.6*x-.48*x*x,color=TEAL,lw=2)
            if theme=='range': ax.axhline(0,color=INK,lw=1)
    elif theme=='relative2d':
        axes(ax,(0,5),(0,8),'t (s)','separation (m)'); ax.plot(np.linspace(0,5),np.sqrt(2)*np.linspace(0,5),color=TEAL,lw=2)
    elif theme=='river':
        axes(ax,(0,5),(0,8),'time (s)','downstream drift (m)'); ax.plot(np.linspace(0,5),np.linspace(0,5)*1.2,color=RED,lw=2,label='aim across'); ax.plot(np.linspace(0,5),np.zeros(50),color=TEAL,lw=2,label='cancel current'); ax.legend(fontsize=7)
    elif theme=='aircraft':
        axes(ax,(0,5),(0,32),'crosswind (km/h)','heading correction (deg)'); w=np.linspace(0,5,100); ax.plot(w,np.degrees(np.arcsin(np.minimum(w/10,.99))),color=TEAL,lw=2); ax.set_title('fixed airspeed 10 km/h',fontsize=8)
    elif theme=='circle':
        axes(ax,(0,5),(0,12),'ω (rad/s)','v (m/s)'); ax.plot(np.linspace(0,5),2*np.linspace(0,5),color=TEAL,lw=2,label='R=2 m'); ax.legend(fontsize=7)
    elif theme=='circ-accel':
        axes(ax,(0,5),(0,30),'speed (m/s)','a_c (m/s²)'); v=np.linspace(0,5,120); ax.plot(v,v*v/2,color=RED,lw=2)
    elif theme=='curvature':
        axes(ax,(0,5),(0,25),'speed (m/s)','ρ (m)'); v=np.linspace(.2,5,120); ax.plot(v,v*v/2,color=TEAL,lw=2,label='|a_perp|=2'); ax.legend(fontsize=7)
    elif theme=='drag1d':
        axes(ax,(0,5),(0,10),'t (s)','downward speed'); t=np.linspace(0,5,150); ax.plot(t,8*(1-np.exp(-t/1.2)),color=TEAL,lw=2,label='linear drag'); ax.axhline(8,color=RED,ls='--',lw=1,label='terminal'); ax.legend(fontsize=7)
    elif theme=='intercept':
        axes(ax,(0,5),(0,8),'time (s)','position'); t=np.linspace(0,5,100); ax.plot(t,1.2*t,color=RED,lw=2,label='target'); ax.plot(t,.8*t+.08*t*t,color=TEAL,lw=2,label='projectile'); ax.legend(fontsize=7)
    elif theme=='coriolis':
        axes(ax,(0,20),(0,11),'flight time (s)','east deflection (m)'); t=np.linspace(0,20,100); delta=7.29e-5*500*np.sin(np.pi/4)*t*t; ax.plot(t,delta,color=TEAL,lw=2); ax.scatter([20],[delta[-1]],color=RED,s=20); ax.set_title('first-order; stated example',fontsize=8)
    elif theme=='pursuit':
        vp, vt, d, dt = 2.0, 1.0, 1.5, .002
        state=np.array([0.0,d]); time=0.0; track=[]
        def rhs(z,t):
            rx=vt*t-z[0]; ry=-z[1]; dist=max(np.hypot(rx,ry),1e-12)
            return np.array([vp*rx/dist,vp*ry/dist])
        target_track=[]; pursuer_track=[]
        for _ in range(2000):
            target_track.append((vt*time,0.0))
            pursuer_track.append(tuple(state))
            rx=vt*time-state[0]; ry=-state[1]
            if np.hypot(rx,ry)<.025: break
            k1=rhs(state,time); k2=rhs(state+dt*k1/2,time+dt/2)
            k3=rhs(state+dt*k2/2,time+dt/2); k4=rhs(state+dt*k3,time+dt)
            state=state+dt*(k1+2*k2+2*k3+k4)/6; time+=dt
        target_track=np.asarray(target_track); pursuer_track=np.asarray(pursuer_track)
        axes(ax,(-.1,1.7),(0,1.7),'x (d=1.5)','y'); ax.plot(target_track[:,0],target_track[:,1],color=RED,ls='--',lw=1.5,label='target'); ax.plot(pursuer_track[:,0],pursuer_track[:,1],color=TEAL,lw=2,label='pursuer'); ax.legend(fontsize=7,loc='upper right'); ax.set_title('RK4 path, v_p=2 v_t',fontsize=8)
    elif theme=='model':
        axes(ax,(0,5),(0,1),'dimensionless speed','gamma - 1'); q=np.linspace(0,.7,100); gam=1/np.sqrt(1-q*q); ax.plot(q,gam-1,color=RED,lw=2)
    else:
        axes(ax)

def figure(ax, key):
    requested, side = key.rsplit('-', 1)
    theme = 'drag2d' if requested == 'dragprojectile' else requested
    if side == 'a':
        schematic(ax, theme)
    else:
        plot(ax, theme)
    caption = 'linear-drag projectile' if requested == 'dragprojectile' else requested.replace('-', ' ')
    return f'{caption}: physical sketch' if side == 'a' else f'{caption}: diagnostic graph'
