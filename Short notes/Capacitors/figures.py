"""Shared drawing primitives and figure library for the Capacitors note sheets.

Rendering helpers are imported by render_sheets.py; figure(key) draws one diagram
with matplotlib at print resolution. No network access is needed.
"""
from pathlib import Path
import json, re, io, textwrap
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.mathtext import math_to_image, MathTextParser
from matplotlib.font_manager import FontProperties, fontManager
from matplotlib.patches import Circle, Rectangle, Arc

ROOT=Path(__file__).resolve().parent
FONT=ROOT/'fonts/PatrickHand-Regular.ttf'
fontManager.addfont(str(FONT))
plt.rcParams.update({'font.family':['Patrick Hand','DejaVu Sans'],'font.size':12,'mathtext.fontset':'cm',
                     'axes.labelcolor':'#153149','text.color':'#153149','axes.edgecolor':'#153149'})
W,H,DPI=2480,3508,300
INK='#153149'; TEAL='#087d7d'; RED='#a43232'; PALE='#eff8f5'; YELLOW='#fff2b8'; GRAY='#516875'

def font(size): return ImageFont.truetype(str(FONT),size)
def normalize(s):
    s=s.replace(r'\sqrt5',r'\sqrt{5}').replace(r'\hbox',r'\mathrm').replace(r'\frac1{',r'\frac{1}{')
    s=re.sub(r'\\(mathcal|mathbf)\s+([A-Za-z])',r'\\\1{\2}',s)
    s=re.sub(r'\\(?:tfrac|dfrac|frac)\s*([A-Za-z0-9])\s*([A-Za-z0-9])',r'\\frac{\1}{\2}',s)
    return re.sub(r'\\(?:tfrac|dfrac|frac)\s*([A-Za-z0-9])\s*(?=\{)',r'\\frac{\1}',s)
def lines_for(s,f,width):
    # Explicit newlines and word wrapping; never shrink body type to hide overflow.
    out=[]
    d=ImageDraw.Draw(Image.new('RGB',(1,1)))
    for paragraph in s.split('\n'):
        line=''
        for word in paragraph.split():
            candidate=(line+' '+word).strip()
            if d.textlength(candidate,font=f)>width and line:out.append(line);line=word
            else:line=candidate
        out.append(line)
    return out

def paragraph(im,s,x,y,width,size=48,color=INK,leading=59):
    f=font(size);d=ImageDraw.Draw(im)
    for line in lines_for(s,f,width):
        assert d.textlength(line,font=f)<=width+1, f'Unwrappable line: {line}'
        d.text((x,y),line,font=f,fill=color);y+=leading
    return y

MATH_CACHE={}
def math_image(s):
    if s not in MATH_CACHE:
        b=io.BytesIO()
        math_to_image('$'+normalize(s)+'$',b,prop=FontProperties(size=12),dpi=DPI,format='png',color=INK)
        a=Image.open(b).convert('RGBA')
        # math_to_image has an opaque white canvas: make its white pixels transparent.
        arr=np.array(a);arr[:,:,3]=255-arr[:,:,:3].min(axis=2)
        arr[:,:,:3]=[21,49,73]
        a=Image.fromarray(arr)
        bbox=a.getbbox();a=a.crop(bbox) if bbox else a
        MATH_CACHE[s]=a
    return MATH_CACHE[s].copy()

def tidy(ax,xlabel=None,ylabel=None):
    ax.spines[['top','right']].set_visible(False)
    ax.tick_params(labelsize=9)
    ax.grid(alpha=.13)
    if xlabel:ax.set_xlabel(xlabel,fontsize=10)
    if ylabel:ax.set_ylabel(ylabel,fontsize=10)

def plain(ax,xlim=(0,10),ylim=(0,5)):
    ax.set(xlim=xlim,ylim=ylim);ax.axis('off')

def wide(ax,H=10):
    # square data units that fill the wide figure: circles stay circles at any art height
    f=ax.figure;bb=ax.get_position()
    ar=(f.get_figwidth()*bb.width)/(f.get_figheight()*bb.height)
    ax.set(xlim=(0,H*ar),ylim=(0,H));ax.set_aspect('equal');ax.axis('off')
    return H*ar

def arrow(ax,a,b,c=TEAL,lw=1.6):
    ax.annotate('',xy=b,xytext=a,arrowprops=dict(arrowstyle='->',color=c,lw=lw))
def wire(ax,a,b):ax.plot([a[0],b[0]],[a[1],b[1]],color=INK,lw=1.5)
def cap(ax,a,b,label='C'):
    a=np.array(a,dtype=float);b=np.array(b,dtype=float);mid=(a+b)/2;u=(b-a)/np.linalg.norm(b-a);v=np.array([-u[1],u[0]])
    p=mid-.12*u;q=mid+.12*u
    wire(ax,a,p);wire(ax,q,b)
    wire(ax,p-.24*v,p+.24*v);wire(ax,q-.24*v,q+.24*v)
    ax.text(*(mid+.38*v),label,ha='center',va='center',fontsize=12)
def resistor(ax,a,b,label='R'):
    a=np.array(a,dtype=float);b=np.array(b,dtype=float);u=(b-a)/np.linalg.norm(b-a);v=np.array([-u[1],u[0]]);mid=(a+b)/2
    p=mid-.42*u;q=mid+.42*u;wire(ax,a,p);wire(ax,q,b)
    pts=np.array([p-.14*v,q-.14*v,q+.14*v,p+.14*v,p-.14*v]);ax.plot(pts[:,0],pts[:,1],color=INK,lw=1.3)
    ax.text(*(mid+.4*v),label,ha='center',fontsize=12)

def figure(ax,key):
    if key=='sphere_fields':
        r=np.linspace(.01,3,500)
        ax.plot(r,1/np.maximum(r,1),color=INK,label='V')
        ax.plot(r,np.where(r<1,0,1/r**2),color=TEAL,label='E')
        ax.axvline(1,c=RED,ls=':',lw=.9)
        ax.set(xlim=(0,3),ylim=(-.03,1.12));tidy(ax,'r / R','V or E (scaled)')
        ax.legend(fontsize=8,loc='center right',frameon=False,title='both in kQ/R units',
                  title_fontsize=7.5,handlelength=1.2)
        return 'Conducting sphere: constant V, zero interior E'
    if key=='cavity':
        R=wide(ax); g=ax; cx,cy=5.2,5.0
        g.add_patch(Circle((cx,cy),4.5,fc='#e6efed',ec=INK,lw=1.2))
        g.add_patch(Circle((cx,cy),2.3,fc='white',ec=INK,lw=1.2))
        g.text(cx,cy,'+q',ha='center',va='center',fontsize=8,color=RED)
        for t in np.linspace(0,2*np.pi,7,endpoint=False):
            g.text(cx+2.0*np.cos(t),cy+2.0*np.sin(t),'-',ha='center',va='center',color=RED,fontsize=8)
        for t in np.linspace(0,2*np.pi,9,endpoint=False):
            g.text(cx+4.72*np.cos(t),cy+4.72*np.sin(t),'+',ha='center',va='center',color=TEAL,fontsize=8)
        g.text(12.5,7.4,'no field in the metal, so the',fontsize=6.5,color=INK)
        g.text(12.5,6.3,'wall must cancel +q exactly;',fontsize=6.5,color=INK)
        g.text(12.5,5.2,'the outside then sees only',fontsize=6.5,color=INK)
        g.text(12.5,4.1,'the total charge of the shell.',fontsize=6.5,color=INK)
        return 'Neutral shell, +q in the cavity: -q on the wall, +q outside, E=0 in the metal'
    if key in ('shells','coax'):
        R=wide(ax); g=ax; cx,cy=5.2,5.0
        g.add_patch(Circle((cx,cy),3.9,fc='none',ec=INK,lw=1.2))
        g.add_patch(Circle((cx,cy),1.95,fc='#f2faf8',ec=INK,lw=1.2))
        g.text(cx,cy,'+Q',ha='center',va='center',fontsize=7,color=RED)
        g.annotate('',xy=(cx+3.7,cy),xytext=(cx+2.1,cy),arrowprops=dict(arrowstyle='->',color=TEAL,lw=1))
        for yy,lab in ((-1.75,'a'),(1.75,'b')):
            g.plot([cx,cx+3.9],[cy+yy,cy+yy],color=GRAY,lw=.55)
            g.text(cx+4.15,cy+yy,lab,va='center',fontsize=6.5,color=GRAY)
        g.text(cx,0.35,'outer shell' if key=='shells' else 'outer conductor',ha='center',fontsize=6,color=GRAY)
        g.text(12.5,7.4,'field lives only between',fontsize=6.5,color=TEAL)
        g.text(12.5,6.4,'a and b:',fontsize=6.5,color=TEAL)
        g.text(12.5,4.9,r'$E=kQ/r^2$' if key=='shells' else r'$E=\lambda/2\pi\varepsilon_0r$',fontsize=8,color=INK)
        if key=='shells':
            g.text(12.5,3.5,'zero inside;',fontsize=6.5,color=GRAY)
            g.text(12.5,2.5,r'$kQ/r^2$ outside',fontsize=6.5,color=GRAY)
        else:
            g.text(12.5,3.5,'zero inside and outside;',fontsize=6.5,color=GRAY)
            g.text(12.5,2.5,'length L cancels in C',fontsize=6.5,color=GRAY)
        return 'Concentric spheres: E between a and b' if key=='shells' else 'Coaxial cylinders: E between a and b'
    if key in ('plates','metal_slab','polarisation'):
        plain(ax)
        ax.add_patch(Rectangle((1.6,.7),.35,3.9,fc=INK,ec=INK))
        ax.add_patch(Rectangle((8.05,.7),.35,3.9,fc=INK,ec=INK))
        ax.text(1.78,4.55,'+',ha='center',fontsize=11,color=RED)
        ax.text(8.22,4.55,'-',ha='center',fontsize=11,color=TEAL)
        if key=='metal_slab':
            ax.add_patch(Rectangle((3.9,.9),2.2,3.2,fc='#dfe5e8',ec=INK,lw=1.1,hatch='///'))
            ax.text(5.0,2.5,'metal',ha='center',va='center',fontsize=10,bbox=dict(fc='#dfe5e8',ec='none',pad=1))
            for yy in (1.3,2.5,3.7):
                arrow(ax,(2.15,yy),(3.75,yy),TEAL,.9); arrow(ax,(6.3,yy),(7.95,yy),TEAL,.9)
            ax.text(5.0,.2,'E = 0 inside; the drop is over (d - t)',ha='center',fontsize=9,color=GRAY)
        elif key=='polarisation':
            for xx in np.arange(3.3,6.6,1.15):
                for yy in (1.55,2.45,3.35):
                    ax.plot([xx,xx+.5],[yy,yy],color=GRAY,lw=1.3)
                    ax.text(xx-.2,yy,'-',ha='center',va='center',fontsize=7.5,color=TEAL)
                    ax.text(xx+.65,yy,'+',ha='center',va='center',fontsize=7.5,color=RED)
            ax.text(3.6,4.55,'bound -',ha='center',fontsize=8,color=TEAL)
            ax.text(6.4,4.55,'bound +',ha='center',fontsize=8,color=RED)
        else:
            for yy in (1.1,1.9,2.7,3.5,4.3): arrow(ax,(2.15,yy),(7.9,yy),TEAL,.9)
            ax.text(5.0,.35,'E = V/d, uniform between the plates',ha='center',fontsize=9,color=GRAY)
        return {'plates':'Uniform gap field: E = V/d',
                'metal_slab':'A metal slab removes thickness t from the voltage drop',
                'polarisation':'Dipoles line up with E; bound faces oppose it'}[key]
    if key=='energy_triangle':
        q=np.linspace(0,1,50);ax.plot(q,q,c=INK);ax.fill_between(q,0,q,color='#f6de7b',alpha=.7);ax.text(.62,.3,'area = U',fontsize=14);ax.set(xlim=(0,1.12),ylim=(0,1.15),xticks=[0,1],xticklabels=['0','Q'],yticks=[0,1],yticklabels=['0','V']);tidy(ax,'charge q','charging voltage')
        return 'Charging work is the area under V(q)'
    if key=='fixed_fork':
        plain(ax); ax.set(xlim=(0,10), ylim=(0,5))
        ax.plot([5,5],[1.3,4.2],color='#c9d6da',lw=.9)
        ax.text(5,4.75,'What is held fixed?',ha='center',fontsize=9.5,color=TEAL)
        ax.text(2.5,3.85,'Isolated',ha='center',fontsize=8.5,color=TEAL)
        ax.text(2.5,3.15,'Q cannot change',ha='center',fontsize=8,color=INK)
        ax.text(2.5,2.25,'minimise U',ha='center',fontsize=8,color=INK)
        ax.text(2.5,1.45,r'$F=-dU/dx$',ha='center',fontsize=8.5,color=INK)
        ax.text(7.5,3.85,'Battery connected',ha='center',fontsize=8.5,color=TEAL)
        ax.text(7.5,3.15,'V is pinned',ha='center',fontsize=8,color=INK)
        ax.text(7.5,2.25,'minimise U - VQ',ha='center',fontsize=8,color=INK)
        ax.text(7.5,1.45,r'$F=-d\Pi/dx$',ha='center',fontsize=8.5,color=INK)
        return 'Choose the correct energy before taking a derivative'
    if key=='insertion':
        plain(ax);wire(ax,(1,1),(9,1));wire(ax,(1,4),(9,4));ax.add_patch(Rectangle((.3,1.15),4,2.7,fc='#cbe9e2',ec=TEAL));ax.text(2.5,2.3,'K',fontsize=18);ax.annotate('',(4.3,.5),(1,.5),arrowprops=dict(arrowstyle='<->',color=INK));ax.text(2.6,.1,'inserted x',ha='center');arrow(ax,(4.7,2.5),(7.4,2.5));ax.text(6.2,2.9,'force inward',ha='center');ax.text(9.2,2.4,'d')
        return 'Insertion increases filled overlap area and C'
    if key=='liquid':
        plain(ax);ax.add_patch(Rectangle((.4,.2),9.2,1.2,fc='#d9efed',ec='none'));wire(ax,(3,.5),(3,4.8));wire(ax,(6,.5),(6,4.8));ax.add_patch(Rectangle((3.05,1.4),2.9,2,fc='#b9ded7'));ax.annotate('',(7.2,3.4),(7.2,1.4),arrowprops=dict(arrowstyle='<->',color=INK));ax.text(7.5,2.3,'h');ax.annotate('',(3,4.3),(6,4.3),arrowprops=dict(arrowstyle='<->',color=INK));ax.text(4.5,4.45,'d',ha='center');ax.text(4.5,2,'liquid K',ha='center');ax.text(.5,1.55,'reservoir',fontsize=11)
        return 'Electric work lifts liquid against gravity'
    if key=='series_parallel':
        plain(ax);cap(ax,(.5,3.7),(4,3.7),'C1');cap(ax,(4,3.7),(9.5,3.7),'C2');ax.text(.1,4.2,'series: neutral middle node',fontsize=12)
        wire(ax,(1,.3),(1,2.1));wire(ax,(9,.3),(9,2.1));cap(ax,(1,2),(9,2),'C1');cap(ax,(1,.4),(9,.4),'C2');ax.text(5,1.1,'parallel: same two nodes',ha='center',fontsize=12)
        return 'Topology, not drawing orientation, defines the grouping'
    if key=='floating_node':
        plain(ax);cap(ax,(.5,2.5),(5,2.5),'C1');cap(ax,(5,2.5),(9.5,2.5),'C2');ax.scatter([5],[2.5],c=TEAL);ax.text(.3,3.5,'VA');ax.text(9.3,3.5,'VB');ax.text(5,3.5,'Vi',ha='center');ax.text(5,1,'qi = C1(Vi − VA) + C2(Vi − VB)',ha='center',fontsize=14)
        return 'Add signed plate charges to conserve island charge'
    if key=='bridge':
        plain(ax);a=(.8,2.5);b=(9.2,2.5);x=(5,4.4);y=(5,.6)
        for p,q,label in [(a,x,'C1'),(x,b,'C2'),(a,y,'C3'),(y,b,'C4'),(x,y,'C5')]:cap(ax,p,q,label)
        for p,t in [(a,'A'),(b,'B'),(x,'X'),(y,'Y')]:ax.text(p[0],p[1]+.35,t,ha='center',color=TEAL)
        return 'Balance means VX = VY, so bridge voltage vanishes'
    if key in ('ladder','pore'):
        plain(ax);wire(ax,(.5,.6),(9.5,.6))
        for i in range(3):
            x=.5+3*i
            (cap if key=='ladder' else resistor)(ax,(x,3.8),(x+2.7,3.8),'C' if key=='ladder' else 'r dx')
            cap(ax,(x+2.7,3.8),(x+2.7,.6),'C' if key=='ladder' else 'c dx')
        ax.text(9.3,4.3,'…',fontsize=20)
        return 'Repeated capacitive ladder stages' if key=='ladder' else 'Distributed resistance delays access to deep pore walls'
    if key=='sp_compact':
        # geometry only: the captions below the box carry the two formulas
        plain(ax); ax.set(xlim=(0,10), ylim=(0,10))
        ax.text(.3,9.4,'SERIES: one path',fontsize=7,color=TEAL)
        ax.plot([1.0,3.4],[7.4,7.4],color=INK,lw=1.1)
        cap(ax,(3.4,7.4),(6.0,7.4),''); ax.plot([6.0,6.8],[7.4,7.4],color=INK,lw=1.1)
        ax.plot([6.8,9.0],[7.4,7.4],color=INK,lw=1.1)
        cap(ax,(6.8,7.4),(9.0,7.4),'')
        ax.scatter([6.8],[7.4],s=16,c=RED,zorder=5)
        ax.text(.75,7.4,'A',ha='right',va='center',fontsize=7,color=TEAL)
        ax.text(9.2,7.4,'B',ha='left',va='center',fontsize=7,color=TEAL)
        ax.text(4.7,5.4,'C1',ha='center',fontsize=7)
        ax.text(7.9,5.4,'C2',ha='center',fontsize=7)
        ax.text(7.1,8.9,'island',ha='center',fontsize=6.5,color=RED)
        ax.text(.3,3.4,'PARALLEL: two nodes',fontsize=7,color=TEAL)
        ax.plot([1.0,9.0],[2.3,2.3],color=INK,lw=1.1)
        ax.plot([1.0,9.0],[0.6,0.6],color=INK,lw=1.1)
        cap(ax,(3.6,2.3),(3.6,0.6),''); cap(ax,(6.4,2.3),(6.4,0.6),'')
        ax.text(3.1,1.45,'C1',ha='right',va='center',fontsize=7)
        ax.text(6.9,1.45,'C2',ha='left',va='center',fontsize=7)
        ax.text(.75,1.45,'A',ha='right',va='center',fontsize=7,color=TEAL)
        ax.text(9.2,1.45,'B',ha='left',va='center',fontsize=7,color=TEAL)
        return 'Series: the middle island fixes the charge. Parallel: the two nodes fix the voltage.'
    if key=='slab_cases':
        # one plate rule, three gaps; axes-fraction layout so it never clips
        ax.set(xlim=(0,1), ylim=(0,1)); ax.axis('off'); T=ax.transAxes
        def bar(x,y0,y1,w=.007): ax.add_patch(Rectangle((x-w/2,y0),w,y1-y0,fc=INK,transform=T,clip_on=False))
        for cx,title,formula,fill in [(.17,'vacuum',r'$C=\varepsilon_0A/d$',None),
                                      (.50,'dielectric slab',r'$C=\dfrac{\varepsilon_0A}{d-t+t/K}$','K'),
                                      (.83,'metal slab',r'$C=\varepsilon_0A/(d-t)$','metal')]:
            g=.085                      # half-gap in axes fraction
            bar(cx-g,.24,.80); bar(cx+g,.24,.80)
            ax.text(cx-g,.855,'+Q',ha='center',fontsize=6.5,color=RED,transform=T)
            ax.text(cx+g,.855,'-Q',ha='center',fontsize=6.5,color=TEAL,transform=T)
            if fill=='K':
                ax.add_patch(Rectangle((cx-.048,.27),.096,.505,fc='#fff3c9',ec=TEAL,lw=.9,transform=T))
                ax.text(cx,.50,'K',ha='center',va='center',fontsize=8,color=TEAL,transform=T)
            elif fill=='metal':
                ax.add_patch(Rectangle((cx-.048,.27),.096,.505,fc='#d5dfdf',ec=INK,lw=.9,transform=T))
                ax.text(cx,.50,'E = 0',ha='center',va='center',fontsize=6.5,color=INK,transform=T)
            for yy in (.36,.52,.68):
                if fill=='metal':
                    ax.annotate('',xy=(cx-.050,yy),xytext=(cx-g+.005,yy),xycoords=T,
                                arrowprops=dict(arrowstyle='->',color=INK,lw=.8))
                    ax.annotate('',xy=(cx+g-.005,yy),xytext=(cx+.050,yy),xycoords=T,
                                arrowprops=dict(arrowstyle='->',color=INK,lw=.8))
                else:
                    ax.annotate('',xy=(cx+g-.005,yy),xytext=(cx-g+.005,yy),xycoords=T,
                                arrowprops=dict(arrowstyle='->',color=INK,lw=.8))
            ax.text(cx,.955,title,ha='center',fontsize=6.5,color=TEAL,transform=T)
            ax.text(cx,.06,formula,ha='center',fontsize=8,color=INK,transform=T)
        return 'One rule for every gap: replace the filled thickness t by t/K'
    if key=='dielectric_layers':
        plain(ax); ax.set(xlim=(0,10), ylim=(0,5))
        ax.text(2.5,4.72,'layers  ->  series',ha='center',fontsize=12,color=TEAL)
        ax.add_patch(Rectangle((.7,2.95),3.6,1.0,fc='#d5e8e3',ec=INK))
        ax.add_patch(Rectangle((.7,1.95),3.6,1.0,fc='#fff3c9',ec=INK))
        wire(ax,(.7,4.2),(4.3,4.2)); wire(ax,(.7,1.7),(4.3,1.7))
        ax.text(3.1,3.45,'K1',ha='center',va='center',fontsize=11)
        ax.text(3.1,2.45,'K2',ha='center',va='center',fontsize=11)
        ax.annotate('',xy=(1.05,2.05),xytext=(1.05,3.85),arrowprops=dict(arrowstyle='->',color=INK,lw=1.1))
        ax.text(1.2,2.95,'D',fontsize=9,color=INK,va='center')
        ax.text(2.5,.55,'same D, voltages add',ha='center',fontsize=8,color=GRAY)
        ax.text(7.5,4.72,'patches  ->  parallel',ha='center',fontsize=12,color=TEAL)
        ax.add_patch(Rectangle((5.8,1.95),1.5,2.25,fc='#d5e8e3',ec=INK))
        ax.add_patch(Rectangle((7.3,1.95),1.9,2.25,fc='#fff3c9',ec=INK))
        wire(ax,(5.8,4.2),(9.2,4.2)); wire(ax,(5.8,1.7),(9.2,1.7))
        ax.text(6.55,3.1,'K1',ha='center',va='center',fontsize=11)
        ax.text(8.25,3.1,'K2',ha='center',va='center',fontsize=11)
        ax.text(7.5,.55,'same V, charges add',ha='center',fontsize=8,color=GRAY)
        return 'Layers share the normal D and add voltages; patches share the voltage and add charges'
    if key=='debye':
        z=np.logspace(-2,2,300);ks=6;ki=2;ax.semilogx(z,ki+(ks-ki)/(1+z*z),c=INK,label="K′");ax.semilogx(z,(ks-ki)*z/(1+z*z),c=TEAL,label='K double-prime');ax.axvline(1,color=RED,ls=':');ax.set(ylim=(0,6.5));tidy(ax,'omega tau','relative permittivity');ax.legend(fontsize=11)
        return 'Loss lags the response; K double-prime peaks at 1'
    if key=='paschen':
        x=np.logspace(-.6,1.3,250);z=x/(np.log(x)+2);ax.semilogx(x,z,c=TEAL);ax.set(yticks=[],xticks=[]);tidy(ax,'pressure × gap','breakdown voltage');ax.text(.7,.7,'qualitative\nclassical-gas trend',transform=ax.transAxes,ha='center',fontsize=12)
        return 'Paschen minimum is not a universal microgap rule'
    if key in ('charging','discharge','two_modes'):
        t=np.linspace(0,5,250)
        if key=='charging':ax.plot(t,1-np.exp(-t),c=TEAL,label='Vc / E');ax.plot(t,np.exp(-t),c=INK,label='iR / E');ax.axvline(1,c=RED,ls=':')
        elif key=='discharge':ax.plot(t,np.exp(-t),c=TEAL,label='V / V0');ax.plot(t,np.exp(-2*t),c=INK,label='U / U0')
        else:ax.plot(t,.6*np.exp(-t/.4)+.4*np.exp(-t/2),c=TEAL,label='two modes');ax.plot(t,np.exp(-t),c=INK,ls='--',label='one mode (comparison)')
        ax.set(xlim=(0,5),ylim=(0,1.1));tidy(ax,'time / (RC)','fraction of final')
        ax.legend(fontsize=7.5,loc='center right',frameon=False,handlelength=1.4)
        ax.axhline(.63,c=GRAY,ls=':',lw=.6)
        return {'charging':'Charge rises as current decays','discharge':'Energy decays faster than voltage','two_modes':'Several storage modes need not share one time constant'}[key]
    if key=='coupled_chain':
        plain(ax)
        resistor(ax,(.6,4),(4.6,4),'R');resistor(ax,(4.6,4),(8.6,4),'R')
        cap(ax,(4.6,4),(4.6,.8),'C');cap(ax,(8.6,4),(8.6,.8),'C')
        wire(ax,(.6,.8),(9.2,.8));ax.text(.1,4.2,'Vs',fontsize=12)
        ax.text(4.5,4.55,'V1',fontsize=12);ax.text(8.5,4.55,'V2',fontsize=12)
        return 'Two storage nodes give two relaxation rates'
    if key=='thevenin':
        plain(ax); ax.set(xlim=(0,10), ylim=(0,5.6))
        ax.add_patch(Circle((1.15,3.0),.42,fill=False,ec=INK,lw=1.2))
        ax.text(1.15,2.35,'Vs',ha='center',fontsize=8.5)
        wire(ax,(1.15,3.42),(1.15,4.5)); wire(ax,(1.15,4.5),(3.2,4.5))
        resistor(ax,(3.2,4.5),(6.4,4.5),'R1')
        wire(ax,(6.4,4.5),(8.5,4.5)); resistor(ax,(6.4,4.5),(6.4,1.9),'R2')
        cap(ax,(8.5,4.5),(8.5,1.9),'C')
        wire(ax,(6.4,1.9),(8.5,1.9)); wire(ax,(1.15,2.58),(1.15,1.9)); wire(ax,(1.15,1.9),(6.4,1.9))
        ax.text(8.5,5.0,'Vc',ha='center',fontsize=9,color=TEAL)
        ax.text(3.4,4.9,'R1 and R2 make the source seen by C',ha='center',fontsize=7.5,color=GRAY)
        return 'C sees the divider voltage and R1 parallel R2'
    if key=='bode':
        z=np.logspace(-2,2,300);ax.semilogx(z,-10*np.log10(1+z*z),c=TEAL);ax.axvline(1,color=RED,ls=':');ax.axhline(-3.01,color=RED,ls=':',alpha=.5);ax.set(ylim=(-43,3));tidy(ax,'frequency / cutoff','gain (dB)');ax.text(.35,-32,'−20 dB / decade',fontsize=13)
        return 'RC low-pass across C: one pole, one time constant'
    if key=='oscillator':
        l=np.log(2);t=np.linspace(0,l,100)
        for i in range(2):ax.plot(t+2*i*l,1-2/3*np.exp(-t),c=TEAL);ax.plot(t+(2*i+1)*l,2/3*np.exp(-t),c=INK)
        ax.axhline(1/3,c=RED,ls=':');ax.axhline(2/3,c=RED,ls=':');ax.set(ylim=(.2,.8),yticks=[1/3,2/3],yticklabels=['Vlo','Vhi']);tidy(ax,'time / RC','Vc / Vs')
        return 'Threshold switching repeats charge and discharge'
    if key=='image_plane':
        plain(ax);wire(ax,(.5,2.5),(9.5,2.5));ax.scatter([5,5],[4.3,.7],c=[TEAL,RED]);ax.text(5.3,4.3,'q (real)');ax.text(5.3,.7,'−q (image)');ax.text(1,2.75,'ground: V = 0');ax.annotate('',(4.5,4.3),(4.5,2.5),arrowprops=dict(arrowstyle='<->',color=INK));ax.text(4,3.4,'h');ax.annotate('',(4.5,2.5),(4.5,.7),arrowprops=dict(arrowstyle='<->',color=INK));ax.text(4,1.5,'h')
        return 'Real-image separation is 2h'
    if key=='image_sphere':
        plain(ax);ax.set_aspect('equal');ax.add_patch(Circle((3,2.5),2,fill=False,ec=INK,lw=1.7));wire(ax,(3,2.5),(9,2.5));ax.scatter([3.67,9],[2.5,2.5],c=[RED,TEAL]);ax.text(3.8,2.8,"q′",fontsize=14);ax.text(9,2.85,'q',fontsize=14);ax.text(3.1,1.5,"r′ = a²/d",fontsize=12);ax.text(6,1.3,'d > a',fontsize=14);arrow(ax,(3,2.5),(2,4.2),INK);ax.text(1.5,4.1,'a')
        return 'Image lies inside sphere; real charge is outside'
    if key=='wedge':
        plain(ax);origin=np.array([1.,2.5]);beta=.72;r0=1.3;r=8
        for t in [-beta/2,beta/2]:wire(ax,origin+r0*np.array([np.cos(t),np.sin(t)]),origin+r*np.array([np.cos(t),np.sin(t)]))
        for rr in [2,4,6]:ax.add_patch(Arc(origin,2*rr,2*rr,theta1=-beta*90/np.pi,theta2=beta*90/np.pi,color=TEAL,lw=1.2))
        ax.text(3,2.6,'beta',fontsize=12);ax.text(8,4.2,'V');ax.text(8,.7,'0');ax.text(5,2,'circular field lines',fontsize=12)
        return 'Wedge: E falls as 1/r away from the apex'
    if key=='pull_in':
        x=np.linspace(0,.66,350);v2=.23
        ax.plot(x,x,c=INK,lw=1.2,label='spring pull kx')
        ax.plot(x,v2/2/(1-x)**2,c=TEAL,lw=1.2,label='electric pull')
        roots=np.roots([1,-2,1,-v2/2]);rr=sorted([a.real for a in roots if abs(a.imag)<1e-7 and 0<a.real<.7])
        for i,r in enumerate(rr):
            ax.scatter([r],[r],c=RED,s=14,zorder=5)
        if len(rr)==2:
            ax.annotate('stable',(rr[0],rr[0]),xytext=(rr[0]-.04,rr[0]-.22),fontsize=8,color=INK)
            ax.annotate('unstable',(rr[1],rr[1]),xytext=(rr[1]-.19,rr[1]+.16),fontsize=8,color=INK)
        ax.set(xlim=(0,.66),ylim=(0,.95));tidy(ax,'closing x / d','force / kd')
        ax.legend(fontsize=7,loc='upper left',frameon=False)
        return 'Fixed V: lower-x crossing stable; higher-x unstable'
    if key=='drop':
        plain(ax);ax.set_aspect('equal');ax.add_patch(Circle((5,2.5),1.5,fc='#e0f0ec',ec=TEAL))
        for t in np.linspace(0,2*np.pi,8,endpoint=False):
            v=np.array([np.cos(t),np.sin(t)]);arrow(ax,np.array([5,2.5])+1.6*v,np.array([5,2.5])+2.35*v,TEAL);ax.text(*(np.array([5,2.5])+1.25*v),'+',ha='center',va='center',color=RED)
        ax.text(5,2.5,'R',ha='center',fontsize=18);ax.text(.1,2.4,'surface\ntension',fontsize=12)
        return 'Electric stress destabilises; surface tension stabilises'
    if key=='master_map':
        plain(ax);ax.text(5,4.5,'Choose the model',ha='center',fontsize=18,color=TEAL)
        for xx,label,sub in [(1.5,'Geometry','Gauss + integrate'),(5,'Network','island charges'),(8.5,'Motion / time','energy / RC')]:
            arrow(ax,(5,3.9),(xx,2.8));ax.text(xx,2.25,label,ha='center',fontsize=14);ax.text(xx,1.2,sub.replace('Gauss + integrate','Gauss +\nintegrate').replace('island charges','island\ncharges'),ha='center',fontsize=10)
        return 'Pick a physical method before doing algebra'
    if key=='drill':
        plain(ax);ax.text(.3,4,'Quick self-test',fontsize=18,color=TEAL);ax.text(.3,2.9,'2 µF at 100 V + 3 µF at 0 V',fontsize=11);ax.text(.3,1.8,'Same polarity: Vf = 40 V',fontsize=11);ax.text(.3,.7,'Heat = 6 mJ. Can you derive both?',fontsize=11)
        return 'Charge sets the final voltage; energy sets the heat'
    raise ValueError(key)
