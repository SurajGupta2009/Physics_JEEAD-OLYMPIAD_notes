"""Render teacher-authored elasticity content into exact A4 PNGs (2480x3508, 300 dpi).

Dependencies: Pillow, matplotlib, numpy. No network or image model is used.
The prose font is Patrick Hand (SIL OFL); equations are native mathtext; every
diagram is drawn from analytic geometry in diagrams.py, not a generated picture.
"""
from pathlib import Path
import json, re, io
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.mathtext import math_to_image, MathTextParser
from matplotlib.font_manager import FontProperties, fontManager
from matplotlib.ft2font import FT2Font

ROOT = Path(__file__).resolve().parent
FONT = ROOT/'fonts/PatrickHand-Regular.ttf'
fontManager.addfont(str(FONT))
plt.rcParams.update({'font.family':['Patrick Hand','DejaVu Sans'],'font.size':12,
                     'mathtext.fontset':'cm','axes.labelcolor':'#153149',
                     'text.color':'#153149','axes.edgecolor':'#153149'})
W,H,DPI = 2480,3508,300
INK='#153149'; TEAL='#087d7d'; RED='#a43232'; PALE='#eff8f5'; YELLOW='#fff2b8'; GRAY='#516875'
DATA = json.loads((ROOT/'sheets.json').read_text())
REPORT=[]
CHARMAP=FT2Font(str(FONT)).get_charmap()

def font(size): return ImageFont.truetype(str(FONT),size)

def _rm(m):
    # mathtext drops spaces inside \mathrm; escape them so words stay readable
    return r'\mathrm{'+m.group(1).replace(' ',r'\ ')+'}'

def normalize(s):
    s=re.sub(r'\\sqrt([0-9])',r'\\sqrt{\1}',s)
    s=re.sub(r'\\(le|ge)(?![A-Za-z])',r'\\\1q',s)
    s=re.sub(r'\\(?:text|hbox|textrm)\{([^{}]*)\}',_rm,s)
    s=s.replace(r'\hbox',r'\mathrm')
    s=re.sub(r'\\(?:tfrac|dfrac)\s*',r'\\frac',s)
    s=re.sub(r'\\(mathcal|mathbf|mathrm)\s+([A-Za-z])',r'\\\1{\2}',s)
    # single-token fraction arguments, e.g. \frac12 -> \frac{1}{2}
    s=re.sub(r'\\frac\s*([A-Za-z0-9])\s*([A-Za-z0-9])',r'\\frac{\1}{\2}',s)
    return s

def lines_for(s,f,width):
    out=[]; d=ImageDraw.Draw(Image.new('RGB',(1,1)))
    for para in s.split('\n'):
        line=''
        for word in para.split():
            cand=(line+' '+word).strip()
            if d.textlength(cand,font=f)>width and line:
                out.append(line); line=word
            else: line=cand
        out.append(line)
    return out

def paragraph(im,s,x,y,width,size=48,color=INK,leading=56):
    assert all(ord(c) in CHARMAP or c=='\n' for c in s), f'Unsupported prose glyph: {s}'
    f=font(size); d=ImageDraw.Draw(im)
    for line in lines_for(s,f,width):
        assert d.textlength(line,font=f)<=width+1, f'Unwrappable line: {line}'
        d.text((x,y),line,font=f,fill=color); y+=leading
    return y

MATH_CACHE={}
def math_image(s):
    key=normalize(s)
    if key not in MATH_CACHE:
        b=io.BytesIO()
        math_to_image('$'+key+'$',b,prop=FontProperties(size=12),dpi=DPI,format='png',color=INK)
        a=Image.open(b).convert('RGBA')
        arr=np.array(a); arr[:,:,3]=255-arr[:,:,:3].min(axis=2); arr[:,:,:3]=[21,49,73]
        a=Image.fromarray(arr)
        bbox=a.getbbox(); a=a.crop(bbox) if bbox else a
        MATH_CACHE[key]=a
    return MATH_CACHE[key].copy()

def card(im,c,x,y,width=1090,height=1050):
    d=ImageDraw.Draw(im)
    d.rounded_rectangle((x,y,x+width,y+height),radius=24,fill='white',outline='#bbd9d4',width=3)
    d.rounded_rectangle((x,y,x+width,y+94),radius=24,fill=PALE)
    d.rectangle((x,y+55,x+width,y+94),fill=PALE)
    titlefont=font(56)
    while d.textlength(c['title'],font=titlefont)>width-60 and titlefont.size>46:
        titlefont=font(titlefont.size-2)
    assert d.textlength(c['title'],font=titlefont)<=width-60, c['title']
    d.text((x+28,y+12),c['title'],font=titlefont,fill=TEAL)
    yy=y+106; bodyw=width-64
    for kind,s in c['items']:
        if kind=='m':
            a=math_image(s)
            if a.width>bodyw:
                ratio=bodyw/a.width
                assert ratio>=.82, f'Equation too wide: {c["title"]}: {s}'
                a=a.resize((bodyw,round(a.height*ratio)),Image.Resampling.LANCZOS)
            d.rounded_rectangle((x+26,yy-5,x+width-26,yy+a.height+15),radius=9,fill=YELLOW)
            im.paste(a,(x+38,yy+3),a); yy+=a.height+24
        else:
            fs=46 if kind in ('why','trap') else 48
            lead=53 if kind in ('why','trap') else 56
            label='WHY / ' if kind=='why' else 'WATCH / ' if kind=='trap' else ''
            color=TEAL if kind=='why' else RED if kind=='trap' else INK
            yy=paragraph(im,label+s,x+32,yy,bodyw,size=fs,color=color,leading=lead)+10
    used=yy-y
    assert used<height-12, f'CARD OVERFLOW ({used}px > {height}px): {c["title"]}'
    REPORT.append({'card':c['title'],'used_px':round(used),'available_px':height,
                   'body_pt':11.52,'explanation_pt':11.04})

from diagrams import figure

def diagram(im,key,x,y,width=1090,height=610):
    fig=plt.figure(figsize=(width/DPI,(height-75)/DPI),dpi=DPI,facecolor='white')
    ax=fig.add_axes([.23,.34,.72,.55]); caption=figure(ax,key)
    if not ax.axison: ax.set_position([.035,.08,.93,.80])
    else: ax.set_aspect('auto')
    fig.canvas.draw(); renderer=fig.canvas.get_renderer()
    artists=list(ax.texts)+[ax.xaxis.label,ax.yaxis.label]
    if ax.axison:
        artists += [t for t in ax.get_xticklabels() if ax.get_xlim()[0]<=t.get_position()[0]<=ax.get_xlim()[1]]
        artists += [t for t in ax.get_yticklabels() if ax.get_ylim()[0]<=t.get_position()[1]<=ax.get_ylim()[1]]
    for art in artists:
        if not art.get_visible() or not art.get_text(): continue
        bb=art.get_window_extent(renderer)
        assert bb.x0>=-1 and bb.y0>=-1 and bb.x1<=width+1 and bb.y1<=height-74, \
            f'Diagram text clipped: {key}: {art.get_text()!r} {bb}'
    if ax.axison:
        ticks=[t.get_window_extent(renderer) for t in ax.get_xticklabels() if t.get_visible() and t.get_text() and ax.get_xlim()[0]<=t.get_position()[0]<=ax.get_xlim()[1]]
        for left,right in zip(ticks,ticks[1:]):
            assert left.x1+2<right.x0, f'Overlapping x tick labels: {key}'
        leg=ax.get_legend()
        if leg:
            bb=leg.get_window_extent(renderer)
            assert bb.x0>=-1 and bb.y0>=-1 and bb.x1<=width+1 and bb.y1<=height-74, f'Legend clipped: {key}'
    b=io.BytesIO(); fig.savefig(b,format='png',dpi=DPI,facecolor='white'); plt.close(fig)
    a=Image.open(b).convert('RGB'); im.paste(a,(x,y+75))
    d=ImageDraw.Draw(im); d.rounded_rectangle((x,y,x+width,y+height),radius=18,outline='#bbd9d4',width=3)
    f=font(40); caplines=lines_for(caption,f,width-45)
    assert len(caplines)<=2, f'Caption too long: {key}'
    for j,line in enumerate(caplines): d.text((x+22,y+10+j*43),line,font=f,fill=TEAL)

def render():
    REPORT.clear()
    counts={k:sum(p['section']==k for p in DATA) for k in ('JEE','Olympiad')}
    parser=MathTextParser('path')
    for p in DATA:
        for c in p['cards']:
            for kind,s in c['items']:
                if kind=='m': parser.parse('$'+normalize(s)+'$',dpi=72)
    for i,p in enumerate(DATA,1):
        im=Image.new('RGB',(W,H),'white'); d=ImageDraw.Draw(im)
        label='PART I: JEE MAIN + ADVANCED' if p['section']=='JEE' else 'PART II: OLYMPIAD / EXTENSIONS'
        d.text((125,125),'ELASTICITY  /  '+label,font=font(30),fill=TEAL)
        d.text((2130,122),f"{p['part_page']:02}/{counts[p['section']]:02}",font=font(44),fill=TEAL)
        fs=88
        while d.textlength(p['title'],font=font(fs))>W-258: fs-=1
        assert fs>=66, p['title']
        d.text((129,165),p['title'],font=font(fs),fill=INK)
        d.line((125,270,W-125,270),fill=TEAL,width=5)
        assert len(lines_for(p['subtitle'],font(45),W-258))<=2, f'Subtitle too long: {p["slug"]}'
        paragraph(im,p['subtitle'],129,290,W-258,size=45,leading=54)
        for c,(xx,yy) in zip(p['cards'],[(125,398),(1265,398),(125,1456),(1265,1456)]):
            card(im,c,xx,yy)
        for key,xx in zip(p['diagrams'],[125,1265]):
            diagram(im,key,xx,2548)
        d=ImageDraw.Draw(im); d.rounded_rectangle((125,3188,W-125,3352),radius=20,fill=PALE)
        paragraph(im,'REMEMBER / '+p['takeaway'],150,3207,W-300,size=45,leading=52)
        d.text((125,3341),p['source'],font=font(26),fill=GRAY)
        d.text((1790,3341),'A4 portrait  /  300 DPI  /  2480 x 3508',font=font(26),fill=GRAY)
        out=ROOT/(p['slug']+'.png'); out.parent.mkdir(parents=True,exist_ok=True)
        # 256-colour adaptive palette: visually indistinguishable on this flat
        # artwork, about 2.4x smaller, and it lets the PDFs embed the indices
        # losslessly instead of expanding every page to RGB.
        im=im.quantize(colors=256,method=Image.MEDIANCUT,dither=Image.NONE)
        im.save(out,dpi=(DPI,DPI),optimize=True)
        print(f"{i:02}/{len(DATA)}  {p['slug']}.png",flush=True)
    expected={p['slug']+'.png' for p in DATA}
    for section in ('JEE','Olympiad'):
        for old in ROOT.glob(section+'-[0-9][0-9]-*.png'):
            if old.name not in expected: old.unlink()
    (ROOT/'layout-checks.json').write_text(json.dumps({'canvas':[W,H],'dpi':DPI,
        'safe_margin_px':125,'cards':REPORT},indent=2)+'\n')

if __name__=='__main__': render()
