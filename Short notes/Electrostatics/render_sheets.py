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
from matplotlib.ft2font import FT2Font
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
CHARMAP=FT2Font(str(FONT)).get_charmap()

def font(size): return ImageFont.truetype(str(FONT),size)
def normalize(s):
    s=re.sub(r'\\sqrt([0-9])',r'\\sqrt{\1}',s)
    s=re.sub(r'\\(le|ge)(?![A-Za-z])',r'\\\1q',s)
    s=s.replace(r'\sqrt5',r'\sqrt{5}').replace(r'\hbox',r'\mathrm').replace(r'\frac1{',r'\frac{1}{')
    s=re.sub(r'\\(mathcal|mathbf|mathrm)\s+([A-Za-z])',r'\\\1{\2}',s)
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

def paragraph(im,s,x,y,width,size=48,color=INK,leading=56):
    assert all(ord(c) in CHARMAP or c=='\n' for c in s), f'Unsupported prose glyph: {s}'
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

def card(im,c,x,y,width=1090,height=1040):
    d=ImageDraw.Draw(im)
    d.rounded_rectangle((x,y,x+width,y+height),radius=24,fill='white',outline='#bbd9d4',width=3)
    d.rounded_rectangle((x,y,x+width,y+94),radius=24,fill=PALE)
    d.rectangle((x,y+55,x+width,y+94),fill=PALE)
    titlefont=font(56)
    assert d.textlength(c['title'],font=titlefont)<width-60,c['title']
    d.text((x+28,y+12),c['title'],font=titlefont,fill=TEAL)
    yy=y+106;bodyw=width-64
    for kind,s in c['items']:
        if kind=='m':
            a=math_image(s)
            # Equations may be modestly reduced, but not below 10 pt equivalent.
            if a.width>bodyw:
                ratio=bodyw/a.width
                assert ratio>=.82, f'Equation too wide: {c["title"]}: {s}'
                a=a.resize((bodyw,round(a.height*ratio)),Image.Resampling.LANCZOS)
            d.rounded_rectangle((x+26,yy-5,x+width-26,yy+a.height+15),radius=9,fill=YELLOW)
            im.paste(a,(x+38,yy+3),a);yy+=a.height+24
        else:
            fs=46 if kind in ('why','trap') else 48
            lead=53 if kind in ('why','trap') else 56
            label='WHY / ' if kind=='why' else 'WATCH / ' if kind=='trap' else ''
            color=TEAL if kind=='why' else RED if kind=='trap' else INK
            yy=paragraph(im,label+s,x+32,yy,bodyw,size=fs,color=color,leading=lead)+10
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

from diagrams import figure

def diagram(im,key,x,y,width=1090,height=610):
    # Draw with native vectors and math, then rasterise directly at print resolution.
    fig=plt.figure(figsize=(width/DPI,(height-115)/DPI),dpi=DPI,facecolor='white')
    ax=fig.add_axes([.23,.34,.72,.55]);caption=figure(ax,key)
    if not ax.axison: ax.set_position([.035,.08,.93,.80])
    else: ax.set_aspect('auto')
    fig.canvas.draw()
    renderer=fig.canvas.get_renderer()
    for artist in list(ax.texts)+([ax.xaxis.label,ax.yaxis.label]+[t for t in ax.get_xticklabels() if ax.get_xlim()[0]<=t.get_position()[0]<=ax.get_xlim()[1]]+[t for t in ax.get_yticklabels() if ax.get_ylim()[0]<=t.get_position()[1]<=ax.get_ylim()[1]] if ax.axison else []):
        if not artist.get_visible() or not artist.get_text(): continue
        bb=artist.get_window_extent(renderer)
        assert bb.x0>=0 and bb.y0>=0 and bb.x1<=width and bb.y1<=height-115, f'Diagram text clipped: {key}: {artist.get_text()} {bb}'
    if ax.axison:
        ticks=[t.get_window_extent(renderer) for t in ax.get_xticklabels() if t.get_visible() and t.get_text()]
        for left,right in zip(ticks,ticks[1:]):
            assert left.x1+2<right.x0, f'Overlapping x tick labels: {key}'
        leg=ax.get_legend()
        if leg:
            bb=leg.get_window_extent(renderer)
            assert bb.x0>=0 and bb.y0>=0 and bb.x1<=width and bb.y1<=height-115, f'Legend clipped: {key}'
    b=io.BytesIO();fig.savefig(b,format='png',dpi=DPI,facecolor='white');plt.close(fig)
    a=Image.open(b).convert('RGB');im.paste(a,(x,y+115))
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
        label='PART I: JEE MAIN + ADVANCED' if p['section']=='JEE' else 'PART II: OLYMPIAD / EXTENSIONS'
        d.text((125,125),'ELECTROSTATICS  /  '+label,font=font(30),fill=TEAL)
        d.text((2160,125),f"{p['part_page']:02}/{part_counts[p['section']]:02}",font=font(42),fill=TEAL)
        fs=88
        while d.textlength(p['title'],font=font(fs))>W-258:fs-=1
        assert fs>=68
        d.text((129,165),p['title'],font=font(fs),fill=INK)
        d.line((125,270,W-125,270),fill=TEAL,width=5)
        paragraph(im,p['subtitle'],129,290,W-258,size=45,leading=54)
        for c,(xx,yy) in zip(p['cards'],[(125,405),(1265,405),(125,1465),(1265,1465)]):card(im,c,xx,yy)
        for key,xx in zip(p['diagrams'],[125,1265]):diagram(im,key,xx,2540)
        d=ImageDraw.Draw(im);d.rounded_rectangle((125,3200,W-125,3345),radius=20,fill=PALE)
        paragraph(im,'REMEMBER / '+p['takeaway'],150,3221,W-300,size=46,leading=56)
        d.text((125,3340),p['source'],font=font(28),fill=GRAY)
        d.text((1740,3340),'A4 portrait  /  300 DPI',font=font(28),fill=GRAY)
        out=ROOT/(p['slug']+'.png');out.parent.mkdir(parents=True,exist_ok=True);im.quantize(colors=96,dither=Image.Dither.NONE).save(out,dpi=(DPI,DPI),optimize=True)
        print(f"{i:02}/{len(DATA)}  {p['slug']}.png",flush=True)
    expected={p['slug']+'.png' for p in DATA}
    for section in ('JEE','Olympiad'):
        for old in ROOT.glob(section+'-[0-9][0-9]-*.png'):
            if str(old.relative_to(ROOT)) not in expected: old.unlink()
    (ROOT/'layout-checks.json').write_text(json.dumps({'canvas':[W,H],'dpi':DPI,'safe_margin_px':125,'cards':REPORT},indent=2)+'\n')

if __name__=='__main__':render()
