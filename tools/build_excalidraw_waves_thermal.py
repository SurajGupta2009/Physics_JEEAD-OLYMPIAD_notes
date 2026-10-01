#!/usr/bin/env python3
"""Convert the local SVG figures in course slots 13–15 into *editable*
Excalidraw primitives. No raster or SVG is embedded inside a scene.

The SVGs remain the portable/HTML source of truth. This converter covers their
rectangles, circles, text, lines and sampled Bézier/arcs, inherited CSS colours,
and nested translate/scale transforms. It approximates hatch patterns with grey fill and marker shapes with native
arrowheads; HTML anchor links are not carried into scenes. The original
SVG stays immediately before each native Obsidian embed in the Markdown note.

Run: python3 tools/build_excalidraw_waves_thermal.py
"""
from __future__ import annotations

import json
import math
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools.build_excalidraw_batch import (BLUE, GRID, INK, MUTED, WHITE,
                                          Scene, scene_file)

ROOT = Path(__file__).resolve().parents[1]
# Note: the F-figure part numbers here are historical (string=1, sound=2, thermo=5).
# New D14–D16 IDs continue the drawing series (NOT course or plan-part numbers).
# D13 is already Electrostatics. A source SVG can occur multiple times.
TOPICS = {
    "string-waves": ("String-waves.md", 14),
    "sound-waves": ("Sound-waves.md", 15),
    "thermodynamics": ("Thermodynamics.md", 16),
}
NS = "{http://www.w3.org/2000/svg}"
NUMBER = r"[-+]?(?:\d*\.\d+|\d+\.?\d*)(?:[eE][-+]?\d+)?"
TOKENS = re.compile(r"[MmLlHhVvCcSsQqTtAaZz]|" + NUMBER)
COMMAND = re.compile(r"^[A-Za-z]$")
COLORS = {
    "black": INK, "white": WHITE, "none": "transparent", "transparent": "transparent",
    "currentColor": INK,
}
Matrix = tuple[float, float, float, float, float, float]
IDENTITY: Matrix = (1, 0, 0, 1, 0, 0)


def matmul(a: Matrix, b: Matrix) -> Matrix:
    x,y,z,w,e,f = a; X,Y,Z,W,E,F = b
    return (x*X+z*Y, y*X+w*Y, x*Z+z*W, y*Z+w*W,
            x*E+z*F+e, y*E+w*F+f)


def point(m: Matrix, x: float, y: float) -> tuple[float, float]:
    a,b,c,d,e,f = m
    return a*x+c*y+e, b*x+d*y+f


def matrix_for(transform: str) -> Matrix:
    m = IDENTITY
    for kind, raw in re.findall(r"(translate|scale)\s*\(([^)]+)\)", transform):
        nums = [float(n) for n in re.findall(NUMBER, raw)]
        if kind == 'translate':
            op = (1,0,0,1,nums[0],nums[1] if len(nums)>1 else 0)
        else:
            op = (nums[0],0,0,nums[1] if len(nums)>1 else nums[0],0,0)
        m = matmul(m, op)
    return m


def css_rules(root: ET.Element) -> tuple[dict[str,str], dict[str,dict[str,str]]]:
    style = '\n'.join(n.text or '' for n in root.findall(f'.//{NS}style'))
    style = re.sub(r'/\*.*?\*/', '', style, flags=re.S)
    variables: dict[str,str] = {'--panel2':'#f4f1e8','--line2':'#b7b0a0'}; rules: dict[str,dict[str,str]] = {}
    for selector, body in re.findall(r'([^{}]+)\{([^{}]*)\}',style):
        props = dict(re.findall(r'([\w-]+)\s*:\s*([^;]+)',body))
        for name in selector.strip().split(','):
            name = name.strip()
            if name == ':root':variables.update(props)
            else:rules.setdefault(name,{}).update(props)
    return variables, rules


def resolve(value: str, variables: dict[str,str]) -> str:
    return re.sub(r'var\((--[\w-]+)\)',lambda m:variables.get(m[1],INK),value.strip())


def draw_style(el: ET.Element, parent: dict[str,str], variables: dict[str,str],
               rules: dict[str,dict[str,str]]) -> dict[str,str]:
    props = dict(parent)
    tag = el.tag.removeprefix(NS)
    props.update(rules.get(tag, {}))
    classes=set(el.get('class','').split())
    for selector, values in rules.items():
        bits=selector.split('.')
        if len(bits)>1 and bits[0] in ('',tag) and set(bits[1:])<=classes:
            props.update(values)
    props.update({k:v for k,v in el.attrib.items() if k in ('fill','stroke','stroke-width',
                      'stroke-dasharray','opacity','fill-opacity','stroke-opacity','marker-end','marker-start','font-size','text-anchor')})
    for k,v in re.findall(r'([\w-]+)\s*:\s*([^;]+)',el.get('style','')):
        props[k]=v
    return {k:resolve(v,variables) for k,v in props.items()}


def colour(value: str) -> str:
    return COLORS.get(value, value if value.startswith('#') else ('#e4e4e4' if value.startswith('url(') else INK))


def bezier(a: tuple[float,float], b: tuple[float,float], c: tuple[float,float],
           d: tuple[float,float] | None = None, steps: int = 12) -> list[tuple[float,float]]:
    out=[]
    for i in range(1,steps+1):
        t=i/steps;u=1-t
        if d is None:
            out.append((u*u*a[0]+2*u*t*b[0]+t*t*c[0],
                        u*u*a[1]+2*u*t*b[1]+t*t*c[1]))
        else:
            out.append((u**3*a[0]+3*u*u*t*b[0]+3*u*t*t*c[0]+t**3*d[0],
                        u**3*a[1]+3*u*u*t*b[1]+3*u*t*t*c[1]+t**3*d[1]))
    return out


def arc_points(a: tuple[float,float], b: tuple[float,float], rx: float, ry: float,
               rotation: float, large: int, sweep: int) -> list[tuple[float,float]]:
    """SVG elliptical arc centre parametrisation, sampled into editable line points."""
    if rx == 0 or ry == 0 or a == b:return [b]
    rx,ry=abs(rx),abs(ry);phi=math.radians(rotation);co,si=math.cos(phi),math.sin(phi)
    dx=(a[0]-b[0])/2;dy=(a[1]-b[1])/2
    xp=co*dx+si*dy;yp=-si*dx+co*dy
    ratio=xp*xp/(rx*rx)+yp*yp/(ry*ry)
    if ratio>1:rx*=math.sqrt(ratio);ry*=math.sqrt(ratio)
    num=max(0,rx*rx*ry*ry-rx*rx*yp*yp-ry*ry*xp*xp)
    den=rx*rx*yp*yp+ry*ry*xp*xp
    k=(-1 if large==sweep else 1)*math.sqrt(num/den) if den else 0
    cxp=k*rx*yp/ry;cyp=-k*ry*xp/rx
    cx=co*cxp-si*cyp+(a[0]+b[0])/2;cy=si*cxp+co*cyp+(a[1]+b[1])/2
    u=((xp-cxp)/rx,(yp-cyp)/ry);v=((-xp-cxp)/rx,(-yp-cyp)/ry)
    ang=math.atan2(u[1],u[0]);delta=math.atan2(u[0]*v[1]-u[1]*v[0],u[0]*v[0]+u[1]*v[1])
    if sweep and delta<0:delta+=2*math.pi
    if not sweep and delta>0:delta-=2*math.pi
    steps=max(8,math.ceil(abs(delta)*16/math.pi))
    return [(cx+rx*math.cos(t)*co-ry*math.sin(t)*si,
             cy+rx*math.cos(t)*si+ry*math.sin(t)*co)
            for t in [ang+delta*i/steps for i in range(1,steps+1)]]


def path_polylines(raw: str) -> list[list[tuple[float,float]]]:
    tokens=TOKENS.findall(raw);i=0;cmd='';p=(0.,0.);first=p;previous=None
    control=None;curves=[];points=[]
    sizes={'M':2,'L':2,'H':1,'V':1,'C':6,'S':4,'Q':4,'T':2,'A':7}
    while i<len(tokens):
        if COMMAND.match(tokens[i]):
            cmd=tokens[i];i+=1
            if cmd.upper()=='Z':
                if points and points[-1]!=first:points.append(first)
                if points:curves.append(points)
                points=[];p=first;previous='Z';control=None;cmd=''
                continue
        if not cmd:raise ValueError(f'unsupported SVG path near {tokens[i:i+4]}')
        typ=cmd.upper();n=sizes[typ]
        if i+n>len(tokens) or any(COMMAND.match(v) for v in tokens[i:i+n]):
            raise ValueError(f'incomplete {cmd} in SVG path {raw[:70]}')
        vals=[float(v) for v in tokens[i:i+n]];i+=n;rel=cmd.islower()
        def xy(x: float,y: float) -> tuple[float,float]:
            return (p[0]+x,p[1]+y) if rel else (x,y)
        start=p
        if typ=='M':
            if points:curves.append(points)
            p=xy(*vals);first=p;points=[p];control=None;cmd='l' if rel else 'L'
        elif typ=='L':p=xy(*vals);points.append(p);control=None
        elif typ=='H':p=(p[0]+vals[0] if rel else vals[0],p[1]);points.append(p);control=None
        elif typ=='V':p=(p[0],p[1]+vals[0] if rel else vals[0]);points.append(p);control=None
        elif typ=='Q':
            c=xy(*vals[:2]);p=xy(*vals[2:]);points+=bezier(start,c,p);control=c
        elif typ=='T':
            c=(2*p[0]-control[0],2*p[1]-control[1]) if previous in ('Q','T') and control else p
            p=xy(*vals);points+=bezier(start,c,p);control=c
        elif typ=='C':
            c1=xy(*vals[:2]);c2=xy(*vals[2:4]);p=xy(*vals[4:]);points+=bezier(start,c1,c2,p);control=c2
        elif typ=='S':
            c1=(2*p[0]-control[0],2*p[1]-control[1]) if previous in ('C','S') and control else p
            c2=xy(*vals[:2]);p=xy(*vals[2:]);points+=bezier(start,c1,c2,p);control=c2
        elif typ=='A':
            p=xy(*vals[5:]);points+=arc_points(start,p,*vals[:5]);control=None
        previous=typ
    if points:curves.append(points)
    return curves


def add_path(s: Scene, pts: list[tuple[float,float]], stroke: str, fill: str,
             sw: float, dashed: bool=False, arrow: bool=False, start_arrow: bool=False) -> None:
    if len(pts)<2:return
    xs=[p[0] for p in pts];ys=[p[1] for p in pts];x=min(xs);y=min(ys)
    kind='arrow' if arrow or start_arrow else 'line'
    element=s._base(kind,x,y,max(xs)-x,max(ys)-y,stroke,fill,sw)
    element['points']=[[round(px-x,3),round(py-y,3)] for px,py in pts]
    element['lastCommittedPoint']=None
    element['startBinding']=None;element['endBinding']=None
    element['startArrowhead']='arrow' if start_arrow else None;element['endArrowhead']='arrow' if arrow else None
    if dashed:element['strokeStyle']='dashed'
    s.elements.append(element)


def converted_scene(slug: str, fig: Path, key: str) -> Scene:
    root=ET.parse(fig).getroot(); vb=list(map(float,root.get('viewBox','0 0 800 500').split()))
    if len(vb)!=4:raise ValueError(f'{fig}: missing viewBox')
    # The bigger thermo course map stays a readable portrait drawing.
    scale=min(2.0,1360/vb[2]);offset=(32-vb[0]*scale,126-vb[1]*scale)
    global_matrix:Matrix=(scale,0,0,scale,*offset)
    vars,rules=css_rules(root)
    s=Scene(key);s.title(f'{slug.replace("-"," ").title()} · {fig.stem}',
                         'Editable companion to the local SVG; source figure is retained in the chapter.')
    def walk(el: ET.Element, mat: Matrix, inherited: dict[str,str]):
        tag=el.tag.removeprefix(NS)
        if tag in ('style','defs','marker','pattern'):return
        before=len(s.elements)
        style=draw_style(el,inherited,vars,rules)
        own=matrix_for(el.get('transform',''))
        # SVG transform-origin is only used by thermo fig-005 (0,4) scale.
        origin=el.get('transform-origin')
        if origin and 'scale' in el.get('transform',''):
            ox,oy=(float(v) for v in origin.split())
            own=matmul(matmul((1,0,0,1,ox,oy),own),(1,0,0,1,-ox,-oy))
        mat=matmul(mat,own)
        stroke=colour(style.get('stroke','none'));fill=colour(style.get('fill','black'))
        if tag=='rect' and fill==INK:
            fill='#edf4fb';stroke=BLUE
        if slug=='thermodynamics' and fig.stem=='fig-002' and tag=='text':
            style['fill']=INK
        width=float(style.get('stroke-width','1.6'))*scale
        dashed='stroke-dasharray' in style
        def P(x,y):return point(mat,float(x),float(y))
        if tag=='text':
            x,y=P(el.get('x','0'),el.get('y','0'))
            value=''.join(el.itertext()).strip()
            replacements={
                'the whole course · click a branch':'the whole course',
                'every chapter opens in place':'eleven chapter branches',
                'every Joule-expansion demo':'every throttling process',
                'At M=1, α=90° (plane wave)':'as M → 1⁺, α → 90°',
            }
            for old,new in replacements.items():value=value.replace(old,new)
            if value:
                size=int(max(12,min(26,float(style.get('font-size','13').removesuffix('px'))*scale)))
                # SVG y is the baseline, Excalidraw y is the top.
                text_w=max(80,len(value)*size*.58)
                if style.get('text-anchor')=='middle':x-=text_w/2
                if style.get('text-anchor')=='end':x-=text_w
                s.text(x,y-size*.95,value,size,colour(style.get('fill','black')),text_w)
        elif tag=='rect':
            x,y=P(el.get('x','0'),el.get('y','0'))
            def length(raw: str, view: float) -> float:
                return view*float(raw[:-1])/100 if raw.endswith('%') else float(raw)
            w=length(el.get('width','0'),vb[2])*scale
            h=length(el.get('height','0'),vb[3])*scale
            if w>0 and h>0:s.rect(x,y,w,h,stroke,fill,
                                  max(1,width),bool(el.get('rx')))
        elif tag=='circle':
            cx,cy=P(el.get('cx','0'),el.get('cy','0'));r=float(el.get('r','0'))*scale
            if r>0:s.ellipse(cx-r,cy-r,2*r,2*r,stroke if stroke!='transparent' else fill,fill,max(1,width))
        elif tag=='line':
            p=P(el.get('x1','0'),el.get('y1','0'));q=P(el.get('x2','0'),el.get('y2','0'))
            if p!=q:add_path(s,[p,q],stroke if stroke!='transparent' else INK,'transparent',width,dashed,'marker-end' in style,'marker-start' in style)
        elif tag=='path':
            for curve in path_polylines(el.get('d','')):
                add_path(s,[P(*v) for v in curve],stroke if stroke!='transparent' else fill,
                         fill if curve[0]==curve[-1] else 'transparent',width,dashed,'marker-end' in style,'marker-start' in style)
        else:
            for child in el:walk(child,mat,style)
        if tag not in ('g','a'):
            for element in s.elements[before:]:
                element['opacity']=round(100*float(style.get('opacity','1')))
        if tag=='text' and 'rotate' in el.get('transform',''):
            raise ValueError('Unsupported text rotation')
    for child in root:walk(child,global_matrix,{'fill':'black','stroke':'none'})
    # Reflow long prose below the diagram rather than across adjacent panels.
    # Retain exact wording; free text is independently editable.
    if not (slug=='thermodynamics' and fig.stem=='fig-002'):
        import textwrap
        annotations=[e for e in s.elements[2:] if e['type']=='text' and len(e['text'])>42]
        bottom=max(e['y']+e['height'] for e in s.elements)+24
        for e in annotations:
            value='\n'.join(textwrap.wrap(e['text'],width=98,break_long_words=False))
            e.update(x=60,y=bottom,width=1250,fontSize=20,text=value,originalText=value,
                     height=27*len(value.splitlines())+8)
            bottom+=e['height']+12
    if len(s.elements)<5:raise ValueError(f'{fig}: suspiciously empty conversion')
    return s


def corrected_scene(slug: str, fig: Path, key: str) -> Scene | None:
    """Analytic redraws where the legacy hand-tuned curves violate their labels.

    Keep the legacy assets untouched (other than XML repair). These companions
    correct s/p quadrature, pipe boundary conditions, the beat envelope, and
    tangent forces on a string; they are not literal source reconstructions.
    """
    n=int(fig.stem[4:])
    if (slug,n) not in {('string-waves',1),('sound-waves',1),('sound-waves',5),('sound-waves',8),('thermodynamics',14),('thermodynamics',16),('thermodynamics',34)}:
        return None
    s=Scene(key)
    def curve(fn,a,b,color=BLUE,steps=240,dash=False):
        add_path(s,[(x,fn(x)) for x in [a+(b-a)*i/steps for i in range(steps+1)]],color,'transparent',2.5,dash)
    if slug=='string-waves':
        s.title('Tension acts along the local tangent','Small slopes: vertical resultant = T [∂y/∂x at x + dx − ∂y/∂x at x].')
        s.line(100,450,1200,450);s.arrow(100,450,100,140);s.text(1210,440,'x',22);s.text(70,115,'y',22)
        f=lambda x:240+0.0005*(x-700)**2
        curve(f,170,1140)
        a,b=430,880
        for x,label in [(a,'x'),(b,'x + dx')]:
            s.line(x,450,x,f(x),MUTED,1.4,'dashed');s.dot(x,f(x),5,BLUE);s.text(x-25,465,label,20)
        # Outward forces: minus tangent at the left, plus tangent at the right.
        s.arrow(a,f(a),a-160,f(a)-160*.001*(a-700),'#bd4b4b',3)
        s.arrow(b,f(b),b+160,f(b)+160*.001*(b-700),'#bd4b4b',3)
        s.text(220,340,'T(x)',22,'#bd4b4b');s.text(1045,315,'T(x + dx)',22,'#bd4b4b')
        s.text(520,190,'dm ≈ μ dx',23,BLUE)
        s.text(150,535,'Equal tension magnitudes do not imply zero resultant: the tangent directions differ.',20,INK,1100)
        s.text(150,575,'For constant T and |∂y/∂x| ≪ 1: μ ∂²y/∂t² = T ∂²y/∂x².',20,INK,1100)
    elif slug=='thermodynamics':
        return thermal_correction(n,key)
    elif n==1:
        s.title('Sound: displacement and excess pressure are in quadrature',
                'Snapshot at t = 0 for s(x,t) = s₀ sin(kx − ωt); ΔP = −B ∂s/∂x.')
        a,b=160,1240;k=4*math.pi/(b-a)
        for y,label in [(215,'s'),(410,'ΔP')]:
            s.arrow(a,y,b+30,y,MUTED,1.4);s.text(85,y-10,label,23);s.text(b+40,y-10,'x',20)
        curve(lambda x:215-52*math.sin(k*(x-a)),a,b)
        curve(lambda x:410+52*math.cos(k*(x-a)),a,b,'#bd4b4b')
        s.text(180,125,'s = s₀ sin(kx)',22,BLUE)
        s.text(180,315,'ΔP = −Bk s₀ cos(kx)',22,'#bd4b4b')
        x=a+(b-a)/4
        s.line(x,180,x,465,MUTED,1.2,'dashed')
        s.text(160,510,'At this s = 0 crossing: ∂s/∂x < 0, so ΔP > 0 (compression).',21,INK,1150)
        s.text(160,555,'Displacement node ↔ pressure antinode in a standing wave; phase conventions matter.',20,INK,1150)
    elif n==5:
        s.title('Organ pipes: displacement mode shapes and boundary conditions',
                'Blue and red are distinct displacement harmonics (not displacement versus pressure).')
        a,b=140,820
        for y,closed in [(210,True),(425,False)]:
            s.line(a,y-66,b,y-66,GRID);s.line(a,y+66,b,y+66,GRID)
            s.line(a,y,b,y,MUTED,1,'dashed')
            if closed:s.line(a,y-66,a,y+66,INK,4)
            for mode,color in [(1,BLUE),(3 if closed else 2,'#bd4b4b')]:
                phase=mode*math.pi/(2 if closed else 1)
                curve(lambda x:y-48*(math.sin(phase*(x-a)/(b-a)) if closed else math.cos(phase*(x-a)/(b-a))),a,b,color,dash=color!=BLUE)
        s.text(140,110,'CLOSED–OPEN: s = 0 at the wall; ∂s/∂x = 0 at the open end',21,INK,1120)
        s.text(870,185,'f₁ = v / (4L)',23,BLUE);s.text(870,225,'f₃ = 3v / (4L)',23,'#bd4b4b')
        s.text(140,320,'OPEN–OPEN: ∂s/∂x = 0 at both ends',21,INK,1120)
        s.text(870,400,'f₁ = v / (2L)',23,BLUE);s.text(870,445,'f₂ = v / L',23,'#bd4b4b')
        s.text(140,535,'Pressure: ΔP = −B ∂s/∂x; pressure node at every open end.',21,INK,1130)
        s.text(140,575,'End correction: L_eff = L + e (closed–open), L + 2e (open–open); e ≈ 0.6r.',20,INK,1170)
        s.text(140,615,'Use L_eff in the frequencies. Thin, unflanged tubes; small amplitude, r ≪ λ.',19,MUTED,1170)
    else:
        s.title('Beats: the resultant really follows the envelope',
                'Equal amplitudes, nearby frequencies: s = 2s₀ cos(πΔf t) sin(2πf_avg t).')
        a,b=140,1240;T=2;df=1;avg=12
        time=lambda x:T*(x-a)/(b-a)
        envelope=lambda x:76*math.cos(math.pi*df*time(x))
        s.arrow(a,320,b+35,320,MUTED,1.3);s.text(1290,310,'t',22)
        curve(lambda x:320-envelope(x)*math.sin(2*math.pi*avg*time(x)),a,b,steps=1600)
        for sign in [-1,1]:curve(lambda x:320+sign*abs(envelope(x)),a,b,'#bd4b4b',steps=400,dash=True)
        s.text(150,145,'Upper/lower bounds: ±2s₀ |cos(πΔf t)|',23,'#bd4b4b',1100)
        for t,label in [(0,'loud'),(.5,'zero'),(1,'loud'),(1.5,'zero'),(2,'loud')]:
            x=a+(b-a)*t/T;s.text(x-20,430,label,18,INK,90)
        s.text(140,500,'Here f₁ = 12.5 Hz, f₂ = 11.5 Hz; f_beat = |f₁ − f₂| = 1 Hz.',22,INK,1160)
        s.text(140,545,'Envelope sign reversal is not a new beat: loudness maxima repeat every 1/|Δf|.',20,INK,1160)
    return s


def thermal_correction(n: int, key: str) -> Scene:
    s=Scene(key)
    if n==14:
        s.title('Cycle ledger: heat and work must sum to the same value',
                'Example: monatomic ideal gas, A = (V₀,P₀), B = (V₀,2P₀), C = (2V₀,2P₀).')
        s.arrow(100,430,560,430);s.arrow(100,430,100,140)
        s.text(570,425,'V',22);s.text(70,110,'P',22)
        a,b,c=(220,330),(220,200),(450,200)
        add_path(s,[a,b,c,a],BLUE,'#e9f2fb',2.5)
        s.arrow(*a,*b,BLUE);s.arrow(*b,*c,BLUE);s.arrow(*c,*a,BLUE)
        for pt,label in [(a,'A'),(b,'B'),(c,'C')]:s.text(pt[0]-22,pt[1]-32,label,22)
        rows=[('Leg','ΔU','W by gas','Q in'),('A → B','+1.5','0','+1.5'),
              ('B → C','+3','+2','+5'),('C → A','−4.5','−1.5','−6'),('Cycle','0','+0.5','+0.5')]
        for i,row in enumerate(rows):
            for j,txt in enumerate(row):s.text(650+j*170,170+i*55,txt,21,BLUE if i==0 else INK,170)
        s.text(650,475,'All energies in units P₀V₀.',20,INK,650)
        s.text(100,540,'ΔU = (3/2) Δ(PV); Q = ΔU + W. Straight C → A: W = mean pressure × ΔV.',21,INK,1250)
        s.text(100,590,'Net work = triangle area = ½ P₀V₀ > 0 (clockwise). Heat input occurs on A → B and B → C.',20,INK,1250)
    elif n==16:
        s.title('Isotherm versus adiabat: negative slopes, same starting state',
                'Ideal gas, reversible expansion; illustrative γ = 1.4. Both curves pass through A.')
        a,b=190,1050;bottom=530
        s.arrow(110,bottom,1190,bottom);s.arrow(110,bottom,110,140)
        s.text(1200,520,'V',22);s.text(75,115,'P',22)
        def pos(v,p):return (190+(v-1)*300,bottom-p*320)
        for gamma,color in [(1,BLUE),(1.4,'#bd4b4b')]:
            pts=[pos(v,v**(-gamma)) for v in [1+2.6*i/160 for i in range(161)]]
            add_path(s,pts,color,'transparent',3)
        s.line(*pos(1,0),*pos(1,1.12),MUTED,1.5,'dashed')
        s.line(*pos(1,1),*pos(3.5,1),MUTED,1.5,'dashed')
        s.dot(*pos(1,1),5,INK);s.text(150,170,'A',22)
        s.text(1000,190,'isobar',20,MUTED);s.text(220,125,'isochore',20,MUTED)
        s.text(1000,425,'isotherm',22,BLUE);s.text(1000,490,'adiabat',22,'#bd4b4b')
        s.text(150,580,'At A: (dP/dV)T = −P/V; (dP/dV)S = −γP/V. The adiabat is steeper.',22,INK,1200)
        s.text(150,630,'For the same expansion: W_ad < W_iso; the adiabatic gas cools.',22,INK,1200)
    else:
        s.title('Efficiency comparisons need the correct temperature extremes',
                'A Carnot bound belongs to an engine’s own hot and cold temperatures—not to a neighbour.')
        s.arrow(130,520,1220,520);s.arrow(130,520,130,150)
        s.text(60,125,'η',24)
        vals=[(.07,'Example 8.2',BLUE),(.565,'Otto, r = 8, γ = 1.4','#26865b'),(.5,'Carnot, 600 / 300 K',BLUE),(.782,'Otto extremes bound','#7058a5')]
        for i,(v,label,color) in enumerate(vals):
            x=200+i*250;s.rect(x,520-380*v,150,380*v,color,color)
            s.text(x,520-380*v-36,f'{100*v:.1f}%',22,color)
            s.text(x-20,550,label,18,INK,240)
        s.text(140,625,'Otto: η = 1 − r^(1−γ) ≈ 56.5%; in this example T_max ≈ 1378 K, T_min = 300 K.',20,INK,1200)
        s.text(140,665,'Its extremes bound is 1 − 300/1378 ≈ 78.2%, not 50%. No second-law violation.',20,INK,1200)
    return s


def main() -> None:
    for slug,(name,slot) in TOPICS.items():
        master=ROOT/slug/name
        source=master.read_text(encoding='utf-8')
        originals=list(re.finditer(r'(?m)^!\[([^\n\]]+)\]\((assets/figures/(fig-(\d+)\.svg))\)$',source))
        figures=sorted((ROOT/slug/'assets/figures').glob('fig-*.svg'))
        if {m[4] for m in originals}!={p.stem[4:] for p in figures}:
            raise ValueError(f'{slug}: figures and Markdown references differ')
        manifest_path=ROOT/slug/'figures.json'
        manifest=json.loads(manifest_path.read_text(encoding='utf-8'))
        records=[]
        for fig in figures:
            number=int(fig.stem[4:]);id_=f'D{slot}.{number}'
            match=next(m for m in originals if int(m[4])==number)
            title=match[1]
            corrected=corrected_scene(slug,fig,id_)
            scene=corrected or converted_scene(slug,fig,id_)
            scene_slug,_=scene_file(slug,id_,title,scene)
            embed=f'![[../_obsidian/excalidraw/{scene_slug}|900]]'
            if source.count(embed)==0:
                # Keep the source SVG and caption. An embed is added after its first use only.
                brief=(f'> [!abstract] DIAGRAM {id_} — {title}\n'
                       f'> **Show:** Editable geometry and labels for the local figure above.\n'
                       f'> **Source:** `{slug}/{match[2]}`; original retained.\n'
                       f'> **Read:** {title}.\n')
                source=source.replace(match[0],match[0]+'\n\n'+brief+'\n'+embed,1)
            elif f'DIAGRAM {id_} —' not in source:
                source=source.replace(embed,
                    f'> [!abstract] DIAGRAM {id_} — {title}\n'
                    f'> **Show:** Editable geometry and labels for the local figure above.\n'
                    f'> **Source:** `{slug}/{match[2]}`; original retained.\n'
                    f'> **Read:** {title}.\n\n'+embed,1)
            elif source.count(embed)!=1:
                raise ValueError(f'{slug}: duplicate embed for {id_}')
            if corrected:
                source=re.sub(r'(> \[!abstract\] DIAGRAM '+re.escape(id_)+r' —[^\n]+\n)> \*\*Show:\*\*[^\n]+',
                    r'\1> **Show:** Analytic redraw correcting the legacy sketch; use this scene for geometry and signs.',source)
            records.append({'id':id_,'kind':'excalidraw','title':title,
                            'show':(f'Analytic redraw of {match[2]}; corrects legacy geometry/signs. See builder and retrofit status.' if corrected else f'Editable reconstruction of {match[2]} with reflowed annotations.'),
                            'search':f'Existing reviewed {slug}/{match[2]} (also preserved beside this embed).',
                            'file':f'_obsidian/excalidraw/{scene_slug}.md',
                            'source':f'{slug}/{name} · {match[2]}'})
        master.write_text(source,encoding='utf-8')
        manifest['note']=manifest.get('note','').replace('existing 34 reviewed','existing 35 reviewed')
        manifest['drawing_numbering']='D14–D16 continue the scene series; course slots are 13–15.'
        manifest['renderer']='obsidian-excalidraw-plugin@2.27.3'
        manifest['drawings']=records
        manifest_path.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
        print(f'{slug}: {len(records)} editable scenes, {len(originals)} SVG references; SVGs preserved')


if __name__=='__main__':main()
