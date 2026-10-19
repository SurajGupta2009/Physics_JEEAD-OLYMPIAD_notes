"""Render teacher-edited source into exact A4 PNGs (2480x3508, 300 dpi).
Dependencies: Pillow, matplotlib, numpy. No network or image model is needed.
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
DATA=json.loads((ROOT/'sheets.json').read_text())
REPORT=[]

def font(size): return ImageFont.truetype(str(FONT),size)
def normalize(s):
    s=s.replace(r'\sqrt5',r'\sqrt{5}').replace(r'\hbox',r'\mathrm').replace(r'\frac1{',r'\frac{1}{')
    s=re.sub(r'\\(mathcal|mathbf)\s+([A-Za-z])',r'\\\1{\2}',s)
    return re.sub(r'\\(?:tfrac|frac)\s*([A-Za-z0-9])\s*([A-Za-z0-9])',r'\\frac{\1}{\2}',s)
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

def card(im,c,x,y,width=1090,height=1010):
    d=ImageDraw.Draw(im)
    d.rounded_rectangle((x,y,x+width,y+height),radius=24,fill='white',outline='#bbd9d4',width=3)
    d.rounded_rectangle((x,y,x+width,y+94),radius=24,fill=PALE)
    d.rectangle((x,y+55,x+width,y+94),fill=PALE)
    titlefont=font(56)
    assert d.textlength(c['title'],font=titlefont)<width-60,c['title']
    d.text((x+28,y+12),c['title'],font=titlefont,fill=TEAL)
    yy=y+116;bodyw=width-64
    for kind,s in c['items']:
        if kind=='m':
            a=math_image(s)
            # Equations may be modestly reduced, but not below 10 pt equivalent.
            if a.width>bodyw:
                ratio=bodyw/a.width
                assert ratio>=.82, f'Equation too wide: {c["title"]}: {s}'
                a=a.resize((bodyw,round(a.height*ratio)),Image.Resampling.LANCZOS)
            d.rounded_rectangle((x+26,yy-5,x+width-26,yy+a.height+15),radius=9,fill=YELLOW)
            im.paste(a,(x+38,yy+3),a);yy+=a.height+32
        else:
            fs=46 if kind in ('why','trap') else 48
            lead=56 if kind in ('why','trap') else 59
            label='WHY / ' if kind=='why' else 'WATCH / ' if kind=='trap' else ''
            color=TEAL if kind=='why' else RED if kind=='trap' else INK
            yy=paragraph(im,label+s,x+32,yy,bodyw,size=fs,color=color,leading=lead)+15
    used=yy-y
    assert used<height-12, f'CARD OVERFLOW ({used}px): {c["title"]}'
    REPORT.append({'card':c['title'],'used_px':round(used),'available_px':height,'body_pt':11.52,'explanation_pt':11.04})

def tidy(ax,xlabel=None,ylabel=None):
    ax.spines[['top','right']].set_visible(False)
    ax.tick_params(labelsize=9)
    ax.grid(alpha=.13)
    if xlabel:ax.set_xlabel(xlabel,fontsize=10)
    if ylabel:ax.set_ylabel(ylabel,fontsize=10)

def plain(ax,xlim=(0,10),ylim=(0,5)):
    ax.set(xlim=xlim,ylim=ylim);ax.axis('off')

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
        r=np.linspace(.01,3,500);ax.plot(r,1/np.maximum(r,1),color=INK,label='V / (kQ/R)');ax.plot(r,np.where(r<1,0,1/r**2),color=TEAL,label='E / (kQ/R²)');ax.axvline(1,c=RED,ls=':');ax.set(xlim=(0,3),ylim=(-.03,1.12));tidy(ax,'r / R','normalised magnitude');ax.legend(fontsize=10,loc='upper right')
        return 'Conducting sphere: constant V, zero interior E'
    if key=='cavity':
        plain(ax);ax.set_aspect('equal');ax.add_patch(Circle((5,2.5),2.2,fc='#e6efed',ec=INK));ax.add_patch(Circle((5,2.5),1.2,fc='white',ec=INK));ax.text(5,2.5,'+q',ha='center',va='center',fontsize=16,color=RED)
        for t in np.linspace(0,2*np.pi,6,endpoint=False):
            ax.text(5+1.05*np.cos(t),2.5+1.05*np.sin(t),'−',ha='center',va='center',color=RED)
            ax.text(5+2.32*np.cos(t),2.5+2.32*np.sin(t),'+',ha='center',va='center',color=TEAL)
        ax.text(7.5,2.5,'metal\nE = 0',va='center',fontsize=13);ax.text(.2,2,'inner: −q\nouter: +q',fontsize=13)
        return 'Neutral isolated shell with a cavity charge'
    if key in ('plates','metal_slab','polarisation'):
        plain(ax);ax.add_patch(Rectangle((1,.5),.18,4,fc=INK));ax.add_patch(Rectangle((8.5,.5),.18,4,fc=INK))
        ax.text(.9,4.65,'+Q',ha='center');ax.text(8.6,4.65,'−Q',ha='center')
        if key=='metal_slab':
            ax.add_patch(Rectangle((4,.5),1.5,4,fc='#d5dfdf',ec=INK));ax.text(4.75,2.5,'E = 0',ha='center',fontsize=13,rotation=90);ax.text(4.75,.05,'t',ha='center')
        if key=='polarisation':
            ax.add_patch(Rectangle((3,.5),3.5,4,fc=PALE,ec=TEAL))
            for yy in [1.2,2.5,3.8]:
                ax.text(3.1,yy,'−',color=RED);ax.text(6.15,yy,'+',color=RED);arrow(ax,(4,yy),(5.8,yy))
            ax.text(4.75,.0,'bound charges on dielectric',ha='center',fontsize=11)
        else:
            for yy in [1.3,2.5,3.7]:
                if key=='metal_slab':arrow(ax,(1.5,yy),(3.5,yy));arrow(ax,(5.9,yy),(8.1,yy))
                else:arrow(ax,(1.5,yy),(8,yy))
        return {'plates':'Uniform gap field: E = V/d','metal_slab':'Metal removes thickness t from the voltage drop','polarisation':'Dipoles point with E; bound faces oppose it'}[key]
    if key in ('shells','coax'):
        plain(ax);ax.set_aspect('equal')
        for rr in [1.15,2.1]:ax.add_patch(Circle((4.5,2.5),rr,fc='none',ec=INK,lw=1.8))
        arrow(ax,(4.5,2.5),(5.65,2.5),INK);arrow(ax,(4.5,2.5),(3.02,3.98),TEAL)
        ax.text(5,2.15,'a');ax.text(3.5,3.5,'b');ax.text(7,2.3,'E(r) ∝ 1/r²' if key=='shells' else 'E(r) ∝ 1/r',fontsize=13)
        return 'Concentric spheres: cross-section' if key=='shells' else 'Coaxial cylinders: cross-section (length L)'
    if key=='energy_triangle':
        q=np.linspace(0,1,50);ax.plot(q,q,c=INK);ax.fill_between(q,0,q,color='#f6de7b',alpha=.7);ax.text(.62,.3,'area = U',fontsize=14);ax.set(xlim=(0,1.12),ylim=(0,1.15),xticks=[0,1],xticklabels=['0','Q'],yticks=[0,1],yticklabels=['0','V']);tidy(ax,'charge q','charging voltage')
        return 'Charging work is the area under V(q)'
    if key=='fixed_fork':
        plain(ax);ax.text(5,4.4,'What is held fixed?',ha='center',fontsize=18,color=TEAL);arrow(ax,(4.4,3.9),(2,2.9));arrow(ax,(5.6,3.9),(8,2.9));ax.text(2,2.5,'Isolated: Q',ha='center',fontsize=16);ax.text(8,2.5,'Battery: V',ha='center',fontsize=16);ax.text(2,1.2,'minimise U',ha='center',fontsize=15);ax.text(8,1.2,'minimise U − VQ',ha='center',fontsize=15)
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
    if key=='dielectric_layers':
        plain(ax);ax.add_patch(Rectangle((1,2.8),8,1.3,fc='#d5e8e3',ec=INK));ax.add_patch(Rectangle((1,.9),8,1.9,fc='#fff9e1',ec=INK));wire(ax,(1,.85),(9,.85));wire(ax,(1,4.15),(9,4.15));ax.text(6,3.3,'epsilon 1',fontsize=14);ax.text(6,1.8,'epsilon 2',fontsize=14);arrow(ax,(3,3.9),(3,1.1));ax.text(.5,4.45,'+ plate');ax.text(.5,.15,'− plate')
        return 'Series layers: same normal D; voltage drops add'
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
        ax.set(xlim=(0,5),ylim=(0,1.08));tidy(ax,'time / reference tau','normalised value');ax.legend(fontsize=10)
        return {'charging':'Charge rises as current decays','discharge':'Energy decays faster than voltage','two_modes':'Several storage modes need not share one time constant'}[key]
    if key=='coupled_chain':
        plain(ax)
        resistor(ax,(.6,4),(4.6,4),'R');resistor(ax,(4.6,4),(8.6,4),'R')
        cap(ax,(4.6,4),(4.6,.8),'C');cap(ax,(8.6,4),(8.6,.8),'C')
        wire(ax,(.6,.8),(9.2,.8));ax.text(.1,4.2,'Vs',fontsize=12)
        ax.text(4.5,4.55,'V1',fontsize=12);ax.text(8.5,4.55,'V2',fontsize=12)
        return 'Two storage nodes give two relaxation rates'
    if key=='thevenin':
        plain(ax);resistor(ax,(1,4),(6,4),'R1');resistor(ax,(6,4),(6,.8),'R2');cap(ax,(9,4),(9,.8),'C');wire(ax,(6,4),(9,4));wire(ax,(1,.8),(9,.8));ax.add_patch(Circle((1,2.4),.5,fill=False,ec=INK));wire(ax,(1,4),(1,2.9));wire(ax,(1,1.9),(1,.8));ax.text(.1,2.4,'Vs');ax.text(7.6,.15,'0 V');ax.text(7.5,4.45,'Vc')
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
        x=np.linspace(0,.68,350);v2=.23;ax.plot(x,x,c=INK,label='spring x');ax.plot(x,v2/2/(1-x)**2,c=TEAL,label='electric force');roots=np.roots([1,-2,1,-v2/2]);rr=sorted([a.real for a in roots if abs(a.imag)<1e-7 and 0<a.real<.7]);
        for i,r in enumerate(rr):ax.scatter([r],[r],c=RED,s=22);ax.annotate('stable' if i==0 else 'unstable',(r,r),xytext=(r+.02,r-.07),fontsize=11)
        ax.set(xlim=(0,.7),ylim=(0,.85));tidy(ax,'closing displacement x / d0','force / (k d0)');ax.legend(fontsize=10,loc='upper left')
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

def diagram(im,key,x,y,width=1090,height=610):
    # Draw with native vectors and math, then rasterise directly at print resolution.
    fig=plt.figure(figsize=(width/DPI,(height-75)/DPI),dpi=DPI,facecolor='white')
    ax=fig.add_axes([.20,.28,.75,.63]);caption=figure(ax,key)
    b=io.BytesIO();fig.savefig(b,format='png',dpi=DPI,facecolor='white');plt.close(fig)
    a=Image.open(b).convert('RGB');im.paste(a,(x,y+75))
    d=ImageDraw.Draw(im);d.rounded_rectangle((x,y,x+width,y+height),radius=18,outline='#bbd9d4',width=3)
    f=font(40);captionlines=lines_for(caption,f,width-45)
    assert len(captionlines)<=2
    for j,line in enumerate(captionlines):d.text((x+22,y+10+j*43),line,font=f,fill=TEAL)

def render():
    REPORT.clear()
    part_counts={key:sum(p['section']==key for p in DATA) for key in ('JEE','Olympiad')}
    # Preflight every formula before replacing any image.
    parser=MathTextParser('path')
    for p in DATA:
        for c in p['cards']:
            for kind,s in c['items']:
                if kind=='m':parser.parse('$'+normalize(s)+'$',dpi=72)
    for i,p in enumerate(DATA,1):
        im=Image.new('RGB',(W,H),'white');d=ImageDraw.Draw(im)
        label='PART I: JEE MAINS + ADVANCED' if p['section']=='JEE' else 'PART II: OLYMPIAD / EXTENSIONS'
        d.text((125,125),'CAPACITORS  /  '+label,font=font(34),fill=TEAL)
        d.text((2160,125),f"{p['part_page']:02}/{part_counts[p['section']]:02}",font=font(42),fill=TEAL)
        fs=88
        while d.textlength(p['title'],font=font(fs))>W-250:fs-=1
        assert fs>=68
        d.text((125,165),p['title'],font=font(fs),fill=INK)
        d.line((125,270,W-125,270),fill=TEAL,width=5)
        paragraph(im,p['subtitle'],125,290,W-250,size=45,leading=54)
        for c,(xx,yy) in zip(p['cards'],[(125,405),(1265,405),(125,1465),(1265,1465)]):card(im,c,xx,yy)
        for key,xx in zip(p['diagrams'],[125,1265]):diagram(im,key,xx,2540)
        d=ImageDraw.Draw(im);d.rounded_rectangle((125,3200,W-125,3345),radius=20,fill=PALE)
        paragraph(im,'REMEMBER / '+p['takeaway'],150,3221,W-300,size=46,leading=56)
        d.text((125,3348),p['source']+'  |  Concepts from Capacitors.md',font=font(24),fill=GRAY)
        d.text((1740,3348),'A4 portrait  /  300 DPI',font=font(24),fill=GRAY)
        out=ROOT/(p['slug']+'.png');out.parent.mkdir(parents=True,exist_ok=True);im.save(out,dpi=(DPI,DPI),optimize=True)
        print(f"{i:02}/{len(DATA)}  {p['slug']}.png",flush=True)
    (ROOT/'layout-checks.json').write_text(json.dumps({'canvas':[W,H],'dpi':DPI,'safe_margin_px':125,'cards':REPORT},indent=2)+'\n')

if __name__=='__main__':render()
