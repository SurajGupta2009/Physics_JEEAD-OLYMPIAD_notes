#!/usr/bin/env python3
"""Course slots 22–24: additive native companions to retained SVGs.

Run from repository root. Regeneration overwrites manual scene edits.
Geometry is inherited from the source SVG, not independently physics-certified.
"""
import json,re,sys,math
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from tools.build_excalidraw_heat_capacitors import converted_scene
from tools.build_excalidraw_batch import scene_file,Scene,INK,BLUE,RED,GREEN
from tools.build_excalidraw_waves_thermal import add_path
from tools.build_excalidraw_waves_thermal import ROOT

TOPICS={'electromagnetic-waves':('Electromagnetic-waves.md',21,7),
        'geometrical-optics':('Geometrical-optics.md',22,46),
        'wave-optics':('Wave-optics.md',23,28)}


def corrected_scene(slug,fig,id_):
    s=Scene(id_)
    if (slug,fig.stem) in [('geometrical-optics','fig-046'),('wave-optics','fig-028')]:
        geo=slug=='geometrical-optics'
        s.title('Choose the optical model before calculating','Read the element, the geometry, the sign convention and the observable.')
        cards=([
            ('Plane mirror','Image by symmetry; rotation gives 2θ.\nFor two mirrors, check angle and object position\nbefore counting images.'),
            ('Curved mirror','1/v + 1/u = 1/f; f = R/2 (paraxial).\nm = −v/u. Use Cartesian signs consistently.'),
            ('Interface / slab','Snell: n₁ sin i = n₂ sin r.\nNear-normal apparent depth; lateral shift.\nTIR only from higher to lower index.'),
            ('Prism','δ = i + e − A; at minimum, i = e.\nn_rel = sin[(A+δ_min)/2] / sin(A/2).\nThin prism: δ ≈ (n_rel − 1)A.'),
            ('Lens / system','1/v − 1/u = 1/f (Cartesian convention).\nPowers add for thin lenses in contact.\nThe first image is the next element’s object.'),
            ('Instrument','Magnification is an angle ratio.\nResolution depends on aperture / diffraction.\nDistinguish relaxed eye and near-point viewing.')
        ] if geo else [
            ('Two coherent sources','Δ = d sinθ; paraxial β = λD/d.\nMeasure D from the effective source plane.\nUnequal amplitudes reduce visibility.'),
            ('Thin film','Geometric optical path difference 2nt cos r.\nCount phase reversals at both reflections.\nOne extra π flip exchanges bright and dark.'),
            ('Single slit / aperture','a sinθ = mλ: minima for nonzero integer m.\nThe central maximum is at θ = 0.\nCircular aperture: Rayleigh angle ≈ 1.22λ/D.'),
            ('Grating','d sinθ = mλ: principal maxima.\nResolving power |m|N (ideal conditions).\nCheck missing orders and |mλ/d| ≤ 1.'),
            ('Polarisation','Malus: I = I_in cos²θ for polarised input.\nUnpolarised input loses half at first polariser.\nBrewster: tanθ_B = n₂/n₁.'),
            ('Coherence / instruments','Visibility depends on spectrum and ΔL.\nMichelson mirror shift x gives path change 2x.\nSeparate magnification from resolution.')
        ])
        for i,(title,body) in enumerate(cards):
            x=70+(i%2)*665;y=170+(i//2)*175
            s.rect(x,y,625,150,BLUE,'#edf4fb',1)
            s.text(x+18,y+12,title,23,BLUE,580);s.text(x+18,y+53,body,19,INK,580)
        s.text(80,735,'Write the path, phase or imaging equation symbolically first; then substitute units and signs.',22,INK,1280)
        return s
    if slug=='wave-optics' and fig.stem in ('fig-009','fig-011','fig-026'):
        coherence=fig.stem=='fig-026';unequal=fig.stem=='fig-011'
        s.title('Visibility for a rectangular optical spectrum' if coherence else 'Two-source interference: analytic intensity',
                'Explicit normalisation and assumptions; corrected companion to the retained legacy sketch.')
        s.arrow(150,570,1220,570,INK);s.arrow(150,570,150,180,INK)
        if coherence:
            fn=lambda z:abs(math.sin(math.pi*z)/(math.pi*z)) if z else 1
            xmin,xmax=-3,3; curves=[(fn,BLUE)]
            s.text(60,130,'Visibility V',22,INK,400);s.text(1040,610,'ΔL / L_c',22,INK,350)
            s.text(100,680,'Flat spectral density over Δν: V = |sinc(πΔνΔL/c)|; L_c = c/Δν ≈ λ²/Δλ.',22,BLUE,1250)
            s.text(100,725,'Zeros at nonzero integer ΔL/L_c; side lobes lie between. Other spectral shapes give other envelopes.',21,INK,1250)
        else:
            xmin,xmax=-2,2;curves=[(lambda z:(1+math.cos(2*math.pi*z))/2,BLUE)]
            if unequal:curves.append((lambda z:(5+4*math.cos(2*math.pi*z))/9,RED))
            s.text(60,130,'I / I_max (each curve)',22,INK,500);s.text(1050,610,'δ / (2π)',22,INK,280)
            s.text(100,680,'Equal amplitudes: I = 4I₀ cos²(δ/2); exact zeros at odd multiples of π.',22,BLUE,1250)
            s.text(100,725,'Red: amplitudes 2:1 ⇒ I/I_max = (5 + 4cosδ)/9, minimum 1/9.' if unequal else
                   'δ = 2πd sinθ/λ; paraxial screen coordinate y ≈ Dθ gives fringe spacing λD/d.',22,RED if unequal else INK,1250)
        for fn,c in curves:
            pts=[(150+1020*i/480,570-330*fn(xmin+(xmax-xmin)*i/480)) for i in range(481)]
            add_path(s,pts,c,'transparent',3)
        for t in range(xmin,xmax+1):s.text(150+1020*(t-xmin)/(xmax-xmin)-10,590,str(t),18,INK,90)
        for v in [0,.5,1]:s.text(95,560-330*v,str(v),18,INK,80)
        return s
    if slug=='geometrical-optics' and fig.stem=='fig-043':
        s.title('Spherical mirror: marginal rays focus nearer the pole','Exact reflection geometry; R = 20 cm. Blue incident rays and red reflected rays share each surface point.')
        R=20;pole=1100;scale=35;y0=500
        s.arrow(180,y0,1220,y0,INK);s.text(1130,530,'pole',20,INK,150)
        pts=[(pole-scale*R+scale*R*math.cos(a),y0-scale*R*math.sin(a)) for a in [-.4+.8*i/160 for i in range(161)]]
        add_path(s,pts,INK,'transparent',3)
        for h in [2,4,6]:
            a=math.asin(h/R);x=R*math.cos(a);focus=R-R/(2*math.cos(a))
            hit=(pole-scale*R+scale*x,y0-scale*h);cross=pole-scale*focus
            s.arrow(230,hit[1],*hit,BLUE,3);s.arrow(*hit,cross,y0,RED,3)
            s.dot(cross,y0,4,RED)
        s.dot(pole-scale*R/2,y0,5,GREEN);s.text(620,580,'paraxial focus: R/2 = 10 cm from pole',22,GREEN,650)
        s.text(100,680,'For height h: distance from pole = R − R²/[2√(R² − h²)].',23,INK,1250)
        s.text(100,725,'h = 6, 4, 2 cm ⇒ 9.52, 9.79, 9.95 cm. Longitudinal aberration ≈ h²/(4R).',22,BLUE,1250)
        return s
    if slug=='geometrical-optics' and fig.stem=='fig-045':
        s.title('The Sun is extended: finite image and finite concentration','Solar angular diameter θ_s ≈ 0.533° ≈ 0.0093 rad; angular radius α ≈ 0.267°.')
        s.line(90,390,1220,390,INK);s.ellipse(580,205,40,370,BLUE,'#edf4fb',2)
        s.line(1110,320,1110,460,RED,4);s.text(1080,490,'image diameter',20,RED,300)
        # Thin lens at x=600: x-axis ray slope maps to image height f*slope.
        for slope,c in [(-.13,BLUE),(.13,GREEN)]:
            for h in [-130,0,130]:
                hit=(600,390+h);s.arrow(170,hit[1]-430*slope,*hit,c,2)
                s.arrow(*hit,1110,390+510*slope,c,2)
        s.text(80,130,'Two opposite solar limbs → two image points (angles exaggerated)',22,INK,1250)
        s.text(460,590,'aperture D; focal length f; f-number N = f/D',22,INK,800)
        s.text(80,680,'d_image ≈ fθ_s = 0.0093f; ideal paraxial area ratio ≈ (D/d_image)² = 1/(0.0093N)².',22,BLUE,1300)
        s.text(80,725,'f/2 gives about 2,900×. In air, the separate étendue limit is 1/sin²α ≈ 46,000×.',22,INK,1300)
        return s
    if slug!='wave-optics' or fig.stem!='fig-015':return None
    s.title('Quarter-wave antireflection coating','Normal incidence; lossless film; n₀ < n_f < n_s. Both reflected rays acquire a π phase flip.')
    s.rect(110,280,440,105,BLUE,'#edf4fb');s.line(110,385,550,385,INK,3)
    s.text(115,210,'air n₀ = 1',22);s.text(115,305,'film n_f = √(n₀n_s)',22,BLUE,380)
    s.text(115,410,'substrate n_s = 1.5',22,INK,380)
    s.arrow(300,160,300,280,BLUE,3);s.arrow(340,280,340,160,RED,3)
    s.arrow(480,385,480,160,GREEN,3)
    s.text(90,480,'Separate arrows distinguish the two returning beams;\nat normal incidence they actually overlap.',20,INK,550)
    s.arrow(740,570,1260,570,INK);s.arrow(740,570,740,210,INK)
    s.text(750,175,'Reflectance R (%)',21,INK,350);s.text(1090,605,'λ / λ₀',22,INK,250)
    # Exact single-film Fresnel result: zero at λ₀ for the matched film.
    n0,ns=1,1.5;nf=math.sqrt(n0*ns)
    a=(n0-nf)/(n0+nf);b=(nf-ns)/(nf+ns)
    def reflectance(x):
        phase=complex(math.cos(math.pi/x),math.sin(math.pi/x))
        return abs((a+b*phase)/(1+a*b*phase))**2
    points=[(740+500*i/240,570-300*reflectance(.5+1.5*i/240)/.04) for i in range(241)]
    add_path(s,points,BLUE,'transparent',3)
    s.line(740,270,1240,270,RED,2,'dashed');s.text(865,235,'bare interface: 4%',20,RED,370)
    for x in [.5,1,1.5,2]:s.text(740+500*(x-.5)/1.5-10,580,str(x),18,INK,70)
    s.text(80,680,'2n_f t = λ₀/2 ⇒ phase difference π at λ₀. Equal reflected amplitudes give R(λ₀) = 0.',22,BLUE,1250)
    s.text(80,725,'Thus t = λ₀/(4n_f). Real coatings can retain reflection if indices, thickness or incidence differ.',21,INK,1250)
    return s


LABEL_FIXES={
 ('geometrical-optics','fig-045'):{'θs = 0.267°':'θs = 0.533° (diameter)'},
 ('geometrical-optics','fig-043'):{'crossings at 8.5, 8.9, 9.9 cm from the pole':'crossings at 9.52, 9.79, 9.95 cm from the pole'},
 ('wave-optics','fig-006'):{'Iₓₐₖ/Iₘₐₓ':'I_min/I_max'},
 ('wave-optics','fig-009'):{'θ = (2n−1)λ/2d':'sin θ = (2n−1)λ/2d','θ = nλ/d':'sin θ = nλ/d'},
 ('wave-optics','fig-013'):{'nails':'bands','collimated glass plates':'nearly parallel glass plates'},
 ('wave-optics','fig-016'):{'≈ 2aA for a thin prism':'(A in radians; small-angle approximation)'},
 ('wave-optics','fig-017'):{'D = mirror-to-screen distance':'D = source-plane to screen distance'},
 ('wave-optics','fig-019'):{'half-width λD/a':'angular half-width ≈ λ/a'},
 ('wave-optics','fig-026'):{'lₜ = λ²/Δλ: first disappearance':'Rectangular spectrum: first zero L_c ≈ λ²/Δλ',
    '2lₜ: fringes back, weaker':'Beyond L_c: weaker side lobes; zeros at multiples',
    'the measured fringes: sharp near ΔL = 0, gone once the two wave trains no longer overlap':'Visibility depends on the spectral line shape; a rectangular spectrum gives |sinc(πΔL/L_c)|.'},
}

def companion(slug,fig,id_):
    scene=corrected_scene(slug,fig,id_) or converted_scene(slug,fig,id_)
    bottom=max(e['y']+e['height'] for e in scene.elements)+24
    for e in scene.elements:
        if e['type']!='text':continue
        text=e['text']
        for a,b in LABEL_FIXES.get((slug,fig.stem),{}).items():text=text.replace(a,b)
        if text!=e['text']:
            import textwrap
            text='\n'.join(textwrap.wrap(text.replace('\n',' '),width=98,break_long_words=False))
            e.update(x=60,y=bottom,width=1250,fontSize=20,text=text,originalText=text,height=27*len(text.splitlines())+8,angle=0)
            bottom+=e['height']+12
    return scene

def main():
    for slug,(name,part,count) in TOPICS.items():
        master=ROOT/slug/name;source=master.read_text()
        matches=list(re.finditer(r'(?m)!\[([^\n\]]+)\]\((assets/figures/fig-(\d+)\.svg)\)$',source))
        assert len(matches)==count and {int(m[3]) for m in matches}==set(range(1,count+1))
        mp=ROOT/slug/'figures.json';manifest=json.loads(mp.read_text());drawings=[]
        for n in range(1,count+1):
            m=next(m for m in matches if int(m[3])==n);id_=f'D{part}.{n}'
            scene=companion(slug,ROOT/slug/m[2],id_)
            stem,file=scene_file(slug,id_,m[1],scene)
            show=('Analytic redraw correcting the legacy sketch; original retained.' if corrected_scene(slug,ROOT/slug/m[2],id_) else 'Editable SVG companion; selected label corrections documented in retrofit status; full physics audit pending.')
            embed=f'![[../_obsidian/excalidraw/{stem}|900]]'
            block=(f'> [!abstract] DIAGRAM {id_} — {m[1]}\n> **Show:** {show}\n'
                   f'> **Source:** `{slug}/{m[2]}`; original retained.\n'
                   f'> **Read:** {m[1].rstrip(".")}.\n\n{embed}')
            if embed not in source:source=source.replace(m[0],m[0]+'\n\n'+block,1)
            else:
                pattern=r'> \[!abstract\] DIAGRAM '+re.escape(id_)+r' —[^\n]*\n(?:(?:>[^\n]*|)\n)*'+re.escape(embed)
                source,hits=re.subn(pattern,lambda _:block,source)
                assert hits==1
            drawings.append(dict(id=id_,kind='excalidraw',title=m[1],show=show,
                                 search=f'Local source: {slug}/{m[2]}',file=file,
                                 source=f'{slug}/{name} · {m[2]}'))
        manifest.update(drawings=drawings,renderer='obsidian-excalidraw-plugin@2.27.3',
                        drawing_numbering='D21 EM Waves, D22 Geometrical Optics, D23 Wave Optics continue the drawing series; course slots 22–24.')
        master.write_text(source);mp.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
        print(f'{slug}: {count} native SVG companions')

if __name__=='__main__':main()
