#!/usr/bin/env python3
"""Remaining seven course chapters: deterministic native schematic companions.

Original brief IDs, including gaps and D100, are retained. Regeneration
replaces manual scene edits. No exporters or remote/raster assets are used.
"""
import json,math,re,sys,random
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from tools.build_excalidraw_current_magnetism_emi import (
 Scene,scene_file,ROOT,INK,MUTED,BLUE,RED,GREEN,ORANGE,PURPLE,GRID,WHITE,
 label,curve,arc,axes,graph,panel,footer,resistor,cap,coil,symbol)
TOPICS={'photoelectric-effect':13,'atomic-structure':13,'x-rays':13,'nuclear-physics':16,
        'semiconductors':18,'communication-systems':12,'special-relativity':12}
BRIEF=re.compile(r'^> \[!abstract\] DIAGRAM (D\d+\.(\d+)) · ([^\n]+)\n((?:>[^\n]*\n)*)',re.M)

def plot(s,functions,a=0,b=5,xlabel='x',ylabel='normalised y',ticks=None):
    axes(s,150,620,1020,380,xlabel,'')
    label(s,60,196,ylabel,MUTED,19,320)
    for fn,c in functions:graph(s,fn,a,b,150,620,1000,330,c)
    for t in ticks or [a,(a+b)/2,b]:label(s,140+1000*(t-a)/(b-a),640,f'{t:g}',INK,18,110)

def level(s,y,t,x=200,w=800,c=INK):
    s.line(x,y,x+w,y,c,2);label(s,x+w+10,y-15,t,c,20,240)

def ladder(s,energies,x=150,w=500,y=620,h=340,e_range=None):
    lo,hi=(min(energies),max(energies)) if e_range is None else e_range
    return [y-h*(e-lo)/(hi-lo) for e in energies]

def chain(s,names,x=70,y=340,w=1260):
    step=w/len(names)
    for i,t in enumerate(names):
        xx=x+i*step;s.rect(xx,y,step-25,85,BLUE,'#edf4fb',1)
        label(s,xx+10,y+16,t,INK,18,step-42)
        if i<len(names)-1:s.arrow(xx+step-25,y+42,xx+step,y+42,BLUE,2)

def nucleus(s,x,y):
    for i,(dx,dy) in enumerate([(-30,0),(0,0),(30,0),(-15,-26),(15,-26),(-15,26),(15,26)]):
        s.ellipse(x+dx-13,y+dy-13,26,26,RED if i%2 else BLUE,'#faeceb' if i%2 else '#edf4fb',2)

def diode(s,a,b,y):
    mid=(a+b)/2;s.line(a,y,mid-18,y);s.line(mid+18,y,b,y)
    curve(s,[(mid-18,y-20),(mid+18,y),(mid-18,y+20),(mid-18,y-20)],BLUE)
    s.line(mid+18,y-23,mid+18,y+23,BLUE,3)

def bragg(s):
    for yy in [355,485]:s.line(220,yy,1170,yy,INK,2)
    for xx,yy in [(520,355),(710,485)]:
        s.arrow(xx-280,yy-170,xx,yy,BLUE,3);s.arrow(xx,yy,xx+280,yy-170,GREEN,3)
    s.arrow(1080,355,1080,485,RED,2);label(s,1100,410,'d',RED)
    arc(s,520,355,80,0,math.atan2(170,280),ORANGE);label(s,600,320,'θ',ORANGE)
    footer(s,'Bragg condition: 2d sinθ = mλ; θ is the glancing angle measured from the planes.',
           'The two path projections each contribute d sinθ; reflections add constructively at integer m.')

def modern(n,s):
    if n==1:
        peak=lambda t:1/(4.965114*t)
        norm=lambda u,t:(.016/(u**5*math.expm1(1/(u*t))))/(.016/(peak(t)**5*math.expm1(1/(peak(t)*t))))
        plot(s,[(lambda u,t=t:norm(u,t),c) for t,c in [(1,BLUE),(1.25,GREEN),(1.5,RED)]],.05,1.6,'λ (arbitrary units, T₁<T₂<T₃)','normalised spectral radiance')
        for t,c in [(1,BLUE),(1.25,GREEN),(1.5,RED)]:
            u=peak(t);s.dot(150+1000*(u-.05)/1.55,620-330*norm(u,t),5,c)
        label(s,930,215,'peaks shift left as T rises: λ_max T = b',INK,21,430)
        label(s,930,265,'classical λ⁻⁴: diverges →',PURPLE,21,420)
        footer(s,'Planck Bλ = 2hc²/[λ⁵(exp(hc/λkT)−1)]; each curve is normalised to its own maximum.',
               'Curves are scaled model shapes, not laboratory data. Rayleigh–Jeans diverges toward short λ; the visible band is not marked here.')
    elif n==3:
        for pts,c in zip([[(150,620),(150+167,520),(150+500,520),(1150,520)],
                          [(150,620),(150+167,480),(150+500,480),(1150,480)]],[BLUE,RED]):curve(s,pts,c,3)
        curve(s,[(150,620),(1150,620)],PURPLE,3,True)
        for x,t in [(-1,'−V_s'),(0,'0'),(1,'+V')]:label(s,150+1000*(x+2)/6-30,650,t,INK,19,170)
        label(s,250,435,'I',BLUE);label(s,250,395,'2I',RED);label(s,900,565,'below threshold: I = 0',PURPLE,19,420)
        footer(s,'Same frequency ⇒ common stopping potential −V_s; larger intensity raises the saturation plateau.',
               'Below-threshold illumination gives no one-photon emission. Piecewise slopes are schematic, not a fitted electron-energy distribution.')
    elif n==4:
        for x in [100,770]:
            s.rect(x,425,540,115,GRID,'#edf4fb')
            for xx in range(x+30,x+540,65):s.dot(xx,440,9,BLUE)
        s.arrow(160,250,340,425,ORANGE,3);s.arrow(340,425,560,220,RED,3)
        label(s,140,200,'hf > φ',ORANGE);label(s,350,180,'K_max = hf − φ',RED)
        for xx in [830,970]:s.arrow(xx,240,1050,425,ORANGE,3)
        s.line(895,395,935,435,RED,6);s.line(935,395,895,435,RED,6)
        label(s,830,170,'each hf < φ: no escape',INK,22,490)
        footer(s,'Einstein’s one-photon model: one absorbed photon transfers hf to one electron.',
               'Multiphoton emission requires intense fields; the classic low-intensity experiment shows no photon pooling.')
    elif n==7:
        for x,cycles,ok in [(150,3,True),(850,3.4,False)]:
            s.line(x,370,x+700,370,GRID,2,'dashed')
            pts=[(x+700*i/400,370-90*math.sin(2*math.pi*cycles*i/400)) for i in range(401)]
            curve(s,pts,GREEN if ok else RED,3)
            if ok:s.arrow(x+700,300,x,300,BLUE,2);label(s,x+200,215,'ends meet in phase: C = 2πr = 3λ',BLUE,19,520)
            else:s.line(x+700,240,x+700,500,ORANGE,2);label(s,x+300,205,'seam mismatch: not an allowed state',ORANGE,19,520)
            label(s,x+140,430,'unrolled circumference (phase φ = 2πs/λ)',INK,18,440)
        footer(s,'Single-valued matter wave on a ring: 2πr = nλ, and p = h/λ gives pr = nℏ.',
               'The unrolled sine is a phase diagram; the electron orbit itself is not a physical sinusoidal path.')
    elif n==8:
        axes(s,140,455,520,220,'x','')
        graph(s,lambda u:math.exp(-u*u/2)*math.cos(8*u),-4,4,140,355,500,120)
        s.arrow(300,470,400,470,GRID,2);s.arrow(400,470,300,470,GRID,2);label(s,332,478,'Δx',INK,19,120)
        axes(s,820,585,470,250,'k − k₀','')
        graph(s,lambda u:math.exp(-u*u),-4,4,820,585,450,200,RED)
        s.arrow(960,600,1100,600,RED,2);s.arrow(1100,600,960,600,RED,2);label(s,1000,608,'Δk',RED,19,120)
        label(s,60,196,'Re ψ',MUTED,19,200);label(s,700,196,'|Ã(k)|',MUTED,19,200)
        footer(s,'A narrow position envelope needs a broad range of wave numbers: Δp = ℏΔk.',
               'For a minimum-uncertainty Gaussian using probability standard deviations, σ_x σ_k = ½.')
    elif n==9:
        x=lambda u:170+980*(u-.6)/4.9;y=lambda E:500-130*E
        s.arrow(150,500,1180,500,INK,2);s.arrow(170,640,170,350,INK,2)
        label(s,1090,525,'r / a₀',INK,20,160);label(s,60,330,'E / 13.6 eV',INK,19,420)
        for fn,c in [(lambda u:1/u**2,BLUE),(lambda u:-2/u,RED),(lambda u:1/u**2-2/u,GREEN)]:
            curve(s,[(x(.6+4.9*i/300),y(fn(.6+4.9*i/300))) for i in range(301)],c,3)
        s.dot(x(1),y(-1),6,GREEN);label(s,x(1)+16,y(-1)-46,'minimum at a₀: −13.6 eV',GREEN,20,420)
        label(s,760,420,'blue: kinetic; red: potential; green: total',INK,20,520)
        footer(s,'K = ℏ²/(2m_er²), U = −ke²/r; the trial total energy has its minimum at the Bohr radius.',
               'Heuristic localisation estimate whose minimum agrees with the exact ground-state energy; the electron is not a point on an orbit.')
    elif n==10:
        s.rect(90,300,250,90,BLUE,'#edf4fb');label(s,110,330,'electron gun\n54 eV beam',INK,18,220)
        s.arrow(340,345,540,345,ORANGE,3)
        s.rect(540,255,400,190,GRID,'#fbfaf6')
        for yy in [285,335,385,435]:s.line(555,yy,925,yy,INK,2)
        for xx in range(580,926,70):
            for yy in [285,335,385,435]:s.dot(xx,yy,6,BLUE)
        s.arrow(600,240,800,120,RED,3);s.arrow(820,120,880,300,GREEN,3)
        label(s,470,140,'detector sweeps angle',GREEN,19,300)
        arc(s,1030,300,90,math.pi*.8,math.pi*1.5,ORANGE)
        label(s,1075,205,'θ_B from the planes',ORANGE,19,240)
        s.arrow(1000,205,1000,455,RED,2);label(s,1008,320,'d',RED)
        s.arrow(1090,455,1220,455,INK,2);s.arrow(1090,455,1090,300,INK,2);label(s,1095,470,'intensity',INK,18,200)
        graph(s,lambda u:.9*math.exp(-((u-65)/22)**2)+.35,10,120,1090,455,130,150,BLUE)
        footer(s,'2d sinθ_B = mλ with λ_dB ≈ 0.167 nm at 54 eV; θ_B is the angle from the atomic plane.',
               'Report the detector/apparatus angle with its definition; grazing and scattering angles differ by 90° in some figures.')
    elif n==11:
        rng=random.Random(2311)
        for i,count in enumerate([60,160,400]):
            x=95+440*i;panel(s,x,170,380,470,['early arrivals','emerging bands','resolved pattern'][i])
            for j in range(count):
                while True:
                    u=rng.random()
                    if rng.random()<.12+.88*math.cos(5*math.pi*u)**2:break
                s.dot(x+30+320*u,250+330*rng.random(),1.8,BLUE)
        footer(s,'Each detection is one whole electron. Repeated independent arrivals sample the interference probability.',
               'Native dot counts are reduced illustrative samples, not the literal 100 / 3,000 / 100,000 counts in the brief.')
    elif n==12:
        chain(s,['photon →\ncathode','dynode 1\ngain 3','dynode 2\ngain 3','dynode 3\ngain 3','anode\npulse'],y=270)
        for i,c in enumerate([1,3,9,27]):
            for j in range(c):s.dot(200+i*290+(j%9)*12,475+(j//9)*18,3,BLUE)
        footer(s,'An incident photon can release one photoelectron; secondary emission multiplies charge at dynodes.',
               'Ideal gain = δ^N; δ = 3, N = 3 gives 27 electrons per initial photoelectron. Detection efficiency is separate.')
    elif n==13:
        axes(s,150,500,1020,200,'log₁₀(λ / m)','')
        label(s,60,196,'log₁₀(E / eV)',MUTED,19,300)
        label(s,180,250,'E(eV) = 1.23984×10⁻⁶ / λ(m); logarithmic scales have slope −1',BLUE,24,1100)
        chain(s,['radio','microwave','IR','visible','UV','X / γ'],y=390)
        footer(s,'1240 nm ≈ 1 eV; 0.124 nm ≈ 10 keV; 400–700 nm corresponds to about 3.10–1.77 eV.',
               'Spectrum blocks are ordered schematic bands, not equal logarithmic intervals; X/γ labels overlap by origin.')
    elif n==14:
        for x,t in [(120,'light: λ = 550 nm'),(790,'electron: 100 kV, λ ≈ 3.70 pm')]:
            panel(s,x,175,560,500,t);s.rect(x+200,285,140,210,BLUE,'#edf4fb');coil(s,x+80,x+470,550,'lens system')
        footer(s,'Diffraction scales with wavelength / numerical aperture; 0.1 nm is far below visible-light resolution.',
               'Electron wavelength permits finer detail, but lens aberrations, specimen and instrumentation still limit resolution.')
    elif n==15:
        s.rect(355,185,660,465,BLUE,'#edf4fb');s.ellipse(585,315,200,200,GRID,WHITE)
        for i in range(-2,3):
            for j in range(-2,3):s.dot(685+110*i,415+85*j,7,BLUE)
        label(s,605,365,'gun aperture',INK)
        footer(s,'LEED: low-energy electron diffraction samples surface periodicity; reciprocal-lattice spots form an array.',
               'For fixed electron energy and geometry, larger real-space lattice spacing gives closer reciprocal spots.')
    elif n==16:
        level(s,600,'E₁');level(s,395,'E₂: metastable');level(s,230,'E₃')
        s.arrow(300,600,300,230,BLUE,3);s.arrow(620,230,620,395,GRID,3);s.arrow(850,395,850,600,RED,3)
        label(s,160,300,'pump',BLUE);label(s,640,290,'fast nonradiative',INK);label(s,460,450,'inversion N₂ > N₁',GREEN)
        s.arrow(860,480,1100,480,RED,2);s.arrow(860,525,1100,525,RED,2)
        footer(s,'Pump populates E₃; rapid relaxation stores population in metastable E₂.',
               'Stimulated E₂ → E₁ emission duplicates the stimulating photon’s mode; three-level inversion requires strong pumping.')
    else:raise ValueError(n)

def atomic(n,s):
    if n==2:
        nucleus(s,720,410);curve(s,[(160,220),(450,220),(600,245),(650,310),(625,390),(500,485),(210,585)],BLUE)
        s.arrow(160,220,400,220,BLUE,3);s.arrow(500,485,210,585,BLUE,3)
        s.line(160,410,650,410,GRID,1,'dashed');s.arrow(350,410,350,220,RED,2);label(s,370,300,'impact b',RED)
        s.arrow(720,410,635,335,GREEN,2);label(s,795,280,'r_min',GREEN)
        footer(s,'Repulsive Coulomb scattering: b = [kZze²/(2K)] cot(θ/2). Asymptotes define θ.',
               'Schematic trajectory, not a numerically integrated hyperbola; only head-on incidence has r_min = kZze²/K.')
    elif n==3:
        chain(s,['α source','thin Au foil\n≈ 400 nm','mostly forward','rare backward'],y=230)
        for y in range(390,580,20):s.arrow(200,y,950,y,GRID,1)
        s.arrow(670,510,360,620,RED,4)
        footer(s,'Historical order of magnitude: about one in 8,000 deflected through angles exceeding 90°.',
               'Reduced schematic tracks, not 8,000 native dots; large-angle events reveal concentrated positive charge.')
    elif n==4:
        pts=[]
        for i in range(501):t=12*math.pi*i/500;r=200*(1-i/600);pts.append((370+r*math.cos(t),420+r*math.sin(t)))
        curve(s,pts,BLUE);nucleus(s,370,420)
        s.rect(800,275,430,75,GRID,'#edf4fb');label(s,820,230,'classical: continuous frequencies',INK)
        for xx in [850,950,1130]:s.line(xx,480,xx,580,RED,5)
        footer(s,'Classical accelerating charge radiates: orbital energy falls and the orbit shrinks.',
               'Observed discrete lines require quantised energy differences; spiral is illustrative, not time-resolved dynamics.')
    elif n==6:
        energies=[-13.6,-3.4,-1.511,-.85,-.544,-.378,0.0];ys=ladder(s,energies,x=200,w=760)
        for i,yy in enumerate(ys):
            if i<3:label(s,975,yy-14,f'{energies[i]:g} eV',INK,18,150)
        label(s,975,ys[6]-14,'0 eV (limit)',INK,18,180);label(s,975,ys[5]+30,'n = 4, 5, 6 … crowd here',MUTED,17,260)
        for x0,target,c,name in [(330,0,BLUE,'Lyman → n=1'),(600,1,RED,'Balmer → n=2'),(840,2,GREEN,'Paschen → n=3')]:
            for j in range(target+1,min(target+4,6)):s.arrow(x0+(j-target)*20,ys[j],x0+(j-target)*20,ys[target],c,2)
            label(s,x0-60,690,name,c,18,260)
        footer(s,'E_n = −13.6 eV/n²; levels crowd toward the ionisation limit E = 0.',
               'Downward arrows emit photons with energy E_initial − E_final; the ladder is drawn to scale in energy.')
    elif n==9:
        for i,(z,er) in enumerate([(1,(-13.6,0)),(2,(-54.4,0)),(3,(-122.4,0))]):
            x=110+445*i;label(s,x,180,['H','He⁺','Li²⁺'][i],BLUE,25,250)
            ys=ladder(s,[-13.6*z*z/j**2 for j in [1,2,3]],x=x,w=215,e_range=er)
            for yy,e in zip(ys,[-13.6*z*z,-3.4*z*z,-1.511*z*z]):
                label(s,x+215,yy-16,f'{e:g} eV',INK,17,180)
            s.arrow(x+100,ys[1],x+100,ys[0],RED,3)
            label(s,x,600,f'2→1: {121.6/z**2:.1f} nm',INK,20,400)
        footer(s,'Hydrogen-like ions: E_n ∝ −Z²/n²; each panel uses its own vertical energy scale.',
               'Ground energies: −13.6, −54.4, −122.4 eV; reduced-mass corrections are omitted.')
    elif n==8:
        dip=lambda u:(.15+.02*u)*(1-.72*sum(math.exp(-((u-4.9*k)/.45)**2) for k in range(1,6)))
        plot(s,[(dip,BLUE)],0,25,'accelerating V','collector current (schematic)',[0,4.9,9.8,19.6,24.5])
        s.dot(150+1000*4.9/25,620-330*dip(4.9),6,RED)
        label(s,270,250,'first dip at 4.9 V: energy lost to excite Hg',RED,20,760)
        footer(s,'Adjacent mercury current dips are separated by about 4.9 V; excitation energy ≈ 4.9 eV.',
               'Emission wavelength hc/ΔE ≈ 253 nm. Contact potentials shift the first dip; positions shown are schematic.')
    elif n==10:moseley(s)
    elif n==11:
        level(s,420,'B = 0: degenerate',150,300)
        for m,c in [(-1,BLUE),(0,INK),(1,RED)]:
            s.line(450,420,1000,420-m*110,c,3);label(s,1040,420-m*110,f'm_l = {m}',c)
        footer(s,'Normal Zeeman model: ΔE = m_l μ_B B; Δm = 0, ±1 gives three photon-frequency components.',
               'Triplet statement assumes the simple normal effect; spin and anomalous Zeeman structure require additional levels.')
    elif n==12:
        plot(s,[(lambda n:(n**3/2*(1/(n-1)**2-1/n**2)-1)*2,BLUE)],5,80,'n','2 × fractional frequency difference',[5,20,40,80])
        footer(s,'For n→n−1: ν_transition / ν_orbit(n) = n³[1/(n−1)²−1/n²]/2 → 1.',
               'Fractional difference falls ≈ 3/(2n); the plotted quantity is twice that difference to fit the scaled axis.')
    elif n==13:
        for y in [230,405,580]:
            for i,c in enumerate([PURPLE,BLUE,GREEN,ORANGE,RED]):s.rect(230+i*190,y,190,70,c,c,1)
        for xx in [380,510,780,1050]:
            s.line(xx,230,xx,300,WHITE,7);s.line(xx,405,xx,475,INK,7)
        label(s,70,240,'emission',INK,20,150);label(s,70,415,'absorption',INK,20,150);label(s,70,590,'continuum',INK,20,160)
        footer(s,'Line positions coincide for transitions between the same levels; absorption needs population in the lower level.',
               'Background bands are schematic colour order, not spectrometer-calibrated wavelengths.')
    elif n==14:
        plot(s,[(lambda z:(1-z/2.3),BLUE)],0,2.3,'log₁₀(K / MeV)','log-scaled closest approach',[0,1,2.3])
        label(s,300,255,'Head-on Au: r_min(fm) ≈ 227.5 / K(MeV)',RED,24,860)
        footer(s,'Log-log slope −1. Au nuclear radius ≈ 1.2×197^(1/3) = 7.0 fm; intersection K ≈ 32 MeV.',
               'Curve uses a scaled logarithmic ordinate; finite nuclear size and nuclear forces invalidate pure Coulomb scattering there.')
    elif n==15:
        plot(s,[(lambda u:.85*math.exp(-((u-656.28)/.025)**2)+.5*math.exp(-((u-656.10)/.025)**2),BLUE)],655.95,656.42,'λ / nm','relative intensity',[656.10,656.28])
        footer(s,'Reduced mass moves the deuterium line to shorter wavelength; Hα isotope separation ≈ 0.18 nm.',
               'Illustrative air-wavelength centres and arbitrary peak heights; resolution needs λ/Δλ ≳ 3,650.')
    elif n==16:
        rows=[(3,656.47,'656.1'),(4,486.27,'486.1'),(5,434.17,'434.0'),(6,410.29,'410.1')]
        label(s,120,205,'n',BLUE,22,80);label(s,300,205,'Bohr vacuum λ / nm',BLUE,22,320);label(s,740,205,'measured / nm',BLUE,22,300);label(s,1040,205,'difference',BLUE,22,220)
        for i,(nn,calc,meas) in enumerate(rows):
            y=260+i*95;s.line(110,y-8,1260,y-8,GRID,2)
            label(s,120,y,str(nn),INK,22,80);label(s,300,y,f'{calc:.2f}',INK,22,320);label(s,740,y,meas,INK,22,300)
            label(s,1040,y,f'{calc-float(meas):+.2f} nm',RED,22,220)
        footer(s,'Rounded measured air wavelengths differ from vacuum Bohr predictions by about 0.2–0.4 nm.',
               'Do not claim four-decimal or sub-0.1 nm agreement from these rounded source values; air/vacuum conventions must be matched first.')
    else:raise ValueError(n)

def moseley(s):
    plot(s,[(lambda z:(z-1)/69,BLUE)],1,70,'atomic number Z','√f / scaled unit',[1,29,43,61,70])
    for z,t in [(11,'Na'),(19,'K'),(26,'Fe'),(29,'Cu'),(42,'Mo'),(79,'Au')]:
        s.dot(150+1000*(z-1)/69,620-330*(z-1)/69,5,RED);label(s,150+1000*(z-1)/69-20,600-330*(z-1)/69,t,RED,17,90)
    footer(s,'Kα model: f ≈ (3Rc/4)(Z−1)², so √f is linear in Z with intercept near Z = 1.',
           'Points are placed on the ideal line for illustration; they are not measured data. Screening is approximate.')

def spectrum(s):
    def continuum(l,cut):return .65*(1-cut/l)/l**2 if l>=cut else 0
    plot(s,[(lambda l:continuum(l,.5)+.55*math.exp(-((l-1.54)/.025)**2)+.3*math.exp(-((l-1.39)/.025)**2),BLUE),
            (lambda l:.35*continuum(l,2),RED)],.4,4,'λ / Å','relative spectral intensity',[.5,1.39,1.54,2,4])
    footer(s,'Cu: Kα ≈ 1.54 Å, Kβ ≈ 1.39 Å. λ_min = hc/(eV); line positions do not move when voltage changes.',
           'Schematic continuum/line strengths; lower voltage chosen below the Cu K-shell excitation threshold ≈ 8.98 kV.')

def pair(s):
    s.arrow(130,410,600,410,ORANGE,4);nucleus(s,640,410)
    s.arrow(660,410,950,265,BLUE,3);s.arrow(660,410,950,555,RED,3);s.arrow(670,430,1100,430,GREEN,2)
    label(s,880,230,'e⁻',BLUE);label(s,880,580,'e⁺',RED);label(s,1020,460,'nuclear recoil',GREEN)
    footer(s,'Stationary nucleus M: E_γ,threshold = 2m_ec²(1 + m_e/M) ≈ 1.022 MeV for heavy nuclei.',
           'At threshold products share the CM velocity in the lab; diverging arrows depict above-threshold momenta, not exact threshold.')

def xrays(n,s):
    if n==1:
        s.rect(170,180,1040,475,BLUE,'#edf4fb',2,True);coil(s,230,390,410,'heated cathode')
        s.line(860,290,960,525,INK,7);label(s,830,240,'W anode',INK)
        for y in [350,410,470]:s.arrow(400,y,900,410,BLUE,3)
        for x in [1030,1150,1260]:s.arrow(900,410,x,600,RED,3)
        label(s,430,550,'vacuum; electron beam',BLUE);label(s,1040,630,'X-ray window',RED)
        label(s,210,150,'high-voltage supply accelerates the electrons (filament heats the cathode)',ORANGE,20,900)
        footer(s,'Filament heats cathode; high voltage accelerates electrons onto a tungsten focal spot.',
               'Anode cooling / rotation spreads heat; bremsstrahlung and characteristic radiation leave through a window.')
    elif n in (3,15):spectrum(s)
    elif n==4:
        ys=ladder(s,[-8.98,-.93,-.08],x=200,w=800)
        for a,b,x,t,c in [(2,0,420,'Kβ ≈ 8.90 keV',BLUE),(1,0,650,'Kα ≈ 8.05 keV',RED),(2,1,880,'Lα ≈ 0.85 keV',GREEN)]:
            s.arrow(x,ys[a],x,ys[b],c,3);label(s,x-110,675,t,c,18,360)
        footer(s,'Kβ and Kα fill the initial K-shell vacancy; Lα fills a later L-shell vacancy in the cascade.',
               'Simplified Cu shell binding energies; fine structure and Auger competition are not resolved.')
    elif n==5:moseley(s)
    elif n==6:
        plot(s,[(lambda x:2**(-x),BLUE),(lambda x:2**(-2*x),RED)],0,5,'x / HVL_tissue','I/I₀',[0,1,2,3,5])
        footer(s,'I = I₀e^(−μx); half-value layer ln2/μ, quarter-value at twice the HVL.',
               'Red curve uses twice the attenuation coefficient. Monochromatic narrow-beam model; real beams harden with depth.')
    elif n==7:bragg(s)
    elif n==8:
        s.arrow(110,405,610,405,BLUE,3);s.dot(620,405,9,RED)
        for r in [90,170,240]:
            arc(s,1030,405,r,c=BLUE,ry=r*.7);s.line(620,405,1030,405-r*.7,GRID);s.line(620,405,1030,405+r*.7,GRID)
        footer(s,'Random crystallite orientations produce diffraction cones; a flat detector intersects them as rings.',
               'Each ring corresponds to an allowed d-spacing / reflection family; order and overlapping families need indexing.')
    elif n==9:
        s.rect(360,255,410,410,GRID,'#fbfaf6',2)
        for i in range(3):
            for j in range(3):s.ellipse(400+i*160,290+j*160,44,44,BLUE if (i+j)%2 else RED,WHITE,2)
        s.arrow(360,700,770,700,INK,2);label(s,520,710,'a (conventional cell edge)',INK,20,420)
        s.arrow(400,240,444,240,GREEN,3);label(s,380,205,'nearest Na–Cl spacing = a/2',GREEN,20,520)
        footer(s,'Rock-salt conventional cell contains four formula units; density = 4M/(N_A a³).',
               'Not every plane family has spacing a/2: cubic d_hkl = a/√(h²+k²+l²), subject to reflection selection rules.')
    elif n==10:
        for i,theta in enumerate([0,90,135]):
            shift=2.42631*(1-math.cos(math.radians(theta)));x=100+i*440
            axes(s,x,585,340,270,'Δλ / pm','')
            graph(s,lambda u:.6*math.exp(-(u/.16)**2)+(.8 if theta else 0)*math.exp(-((u-shift)/.16)**2),-.5,5,x,585,320,190,BLUE)
            label(s,x,210,f'θ = {theta}°; shift {shift:.2f} pm',RED,19,420)
        label(s,60,196,'relative intensity (per panel, offset)',MUTED,18,320)
        footer(s,'Compton: Δλ = h/(m_ec)(1−cosθ); 90° gives 2.426 pm, 135° gives 4.142 pm.',
               'Unshifted component can arise from tightly bound / coherent scattering; arbitrary peak heights, not measured data.')
    elif n in (13,16):
        chain(s,['photoelectric\nenergy quantum','Bragg\nwave interference','Compton\nphoton momentum','pair creation\nrest energy'],y=280)
        label(s,150,480,'E = hf; p = h/λ; Δλ = λ_C(1−cosθ); pair threshold ≈ 1.022 MeV',BLUE,25,1250)
        footer(s,'Energy regions overlap and depend on material; these blocks are experiments, not universal dominance bands.',
               'Thomson / Rayleigh are low-energy scattering limits; Klein–Nishina gives free-electron high-energy scattering.')
    elif n==14:pair(s)
    else:raise ValueError(n)

def nuclear(n,s):
    if n==1:
        pts=[(400+80*i,300+80*j) for j in range(3) for i in range(4)]
        for i,(x,y) in enumerate(pts):
            s.ellipse(x-25,y-25,50,50,RED if i%3==0 else BLUE,WHITE,2)
            if i%4!=3:s.line(x+25,y,x+55,y,GREEN,4)
            if i<8:s.line(x,y+25,x,y+55,GREEN,4)
        for a,b in [(0,3),(0,6),(0,9),(3,6),(3,9),(6,9)]:s.arrow(*pts[a],*pts[b],RED,1.5)
        label(s,860,335,'green: short-range attraction',GREEN,22,470);label(s,860,420,'red: every proton pair repels',RED,22,470)
        footer(s,'Strong residual nuclear attraction saturates because its range is short; Coulomb repulsion does not.',
               'Packed nucleon drawing is schematic. Nuclear forces are not literal adhesive bonds or a classical static lattice.')
    elif n==2:
        plot(s,[(lambda x:1.2*x/8,BLUE)],0,6.5,'A^(1/3)','R / 8 fm',[0,2,4,6])
        for A,t in [(12,'C'),(56,'Fe'),(197,'Au'),(238,'U')]:
            x=A**(1/3);s.dot(150+1000*x/6.5,620-330*1.2*x/8,5,RED);label(s,150+1000*x/6.5,580-330*1.2*x/8,t,RED,20,100)
        footer(s,'R ≈ r₀A^(1/3), r₀ ≈ 1.2 fm. Nearly constant nucleon number density follows.',
               'Points illustrate the radius law, not measured charge radii; small nuclei and surface diffuseness produce deviations.')
    elif n==4:
        s.line(300,300,1000,250,INK,4);s.line(670,275,670,570,INK,3)
        for x,y in [(340,310),(950,265)]:s.line(x,y,x,470);s.line(x-140,470,x+140,470,INK,3)
        for i in range(6):s.dot(240+35*i,445,10,BLUE)
        nucleus(s,950,425);label(s,160,530,'separate nucleons: larger mass',BLUE,22,620);label(s,815,540,'bound nucleus',RED,22,450)
        footer(s,'Binding B = [Zm_p + Nm_n − M_nucleus]c² > 0; release B during formation.',
               'The assembled nucleus is lighter. Supply B to dismantle it into free nucleons at rest.')
    elif n==5:
        for i,(A,Z) in enumerate([(56,26),(238,92)]):
            x=100+i*670;axes(s,x,430,520,220,'term','')
            vals=[15.8,-18.3*A**(-1/3),-.714*Z*(Z-1)/A**(4/3),-23.2*(A-2*Z)**2/A**2,12/A**1.5]
            for j,(v,t) in enumerate(zip(vals,['volume','surface','Coulomb','asym.','pair'])):
                xx=x+25+95*j;s.rect(xx,min(430,430-v*12),55,abs(v)*12+1,BLUE if v>0 else RED,'#edf4fb' if v>0 else '#faeceb')
                label(s,xx-10,610,t,INK,16,110)
            label(s,x+60,150,f'A={A}, Z={Z}',INK,21,300);label(s,x+60,178,f'B/A≈{sum(vals):.2f} MeV',INK,19,300)
        label(s,60,196,'contribution / A (MeV)',MUTED,19,300)
        footer(s,'Illustrative liquid-drop coefficients: 15.8, 18.3, 0.714, 23.2 MeV; even-even pairing +12/√A MeV.',
               'Bars show contribution per nucleon; pairing is tiny on this scale. Empirical fits use different coefficients.')
    elif n in (6,12):
        axes(s,200,620,900,410,'N (neutrons)','')
        label(s,60,196,'Z (protons)',MUTED,19,200)
        if n==6:
            curve(s,[(200+6*z,620-4*z) for z in range(91)],GRID,dash=True)
            curve(s,[(200+6*(z+.006*z*z),620-4*z) for z in range(91)],BLUE,6)
            s.arrow(760,450,700,410,RED,3);label(s,770,395,'β⁻: N−1, Z+1',RED,20,430)
            s.arrow(650,280,710,320,GREEN,3);label(s,735,270,'β⁺ / EC: N+1, Z−1',GREEN,20,490)
        else:
            pts=[(1000,240),(940,300),(900,340),(880,300),(820,360),(760,420),(700,480),(640,540),(600,500)]
            curve(s,pts,BLUE,3)
            for p in pts:s.dot(*p,5,BLUE)
            label(s,1005,215,'²³⁸U',RED);label(s,300,570,'… → ²⁰⁶Pb (stable)',GREEN)
        footer(s,'Axes explicitly N horizontal, Z vertical: α = (−2,−2); β⁻ = (−1,+1); β⁺ / EC = (+1,−1).',
               'Stable heavy nuclei need N > Z. A full ²³⁸U → ²⁰⁶Pb chain has eight α and six β⁻ decays.')
    elif n==7:
        level(s,230,'parent',160,450);level(s,445,'daughter excited',770,380);level(s,590,'daughter ground',770,380)
        s.arrow(420,230,880,445,BLUE,3);s.arrow(530,230,1020,590,RED,3);s.arrow(1130,445,1130,590,GREEN,3)
        s.arrow(360,650,180,650,RED,3);s.arrow(390,650,570,650,BLUE,3);label(s,215,660,'m_α = 4u: larger speed',MUTED,17,300)
        footer(s,'Parent at rest: daughter and α momenta are equal and opposite, not inversely sized.',
               'K_α = Q M_D/(M_D+m_α); K_D = Q m_α/(M_D+m_α). Excited daughter reduces α energy then emits γ.')
    elif n==8:
        panel(s,90,170,560,500,'in matter');panel(s,720,170,560,500,'in a magnetic field B ⊗')
        s.dot(160,415,10,INK)
        curve(s,[(160,415),(300,370),(420,350)],RED,6)
        curve(s,[(160,415),(300,435),(430,440),(560,500)],BLUE,2)
        s.arrow(160,415,560,415,ORANGE,2)
        for x,t in [(330,'paper'),(470,'foil'),(590,'lead')]:
            s.rect(x,250,18,330,GRID,'#edf4fb');label(s,x-20,675,t,INK,18,120)
        s.dot(790,415,10,INK)
        curve(s,[(790,415),(880,455),(990,470)],RED,5)
        curve(s,[(790,415),(870,380),(960,390),(1060,440)],BLUE,2)
        s.arrow(790,415,1240,415,ORANGE,2)
        label(s,770,220,'α: small curvature; β: large opposite curvature',INK,18,470)
        footer(s,'Charged α: dense short tracks; β: thin scattered tracks; neutral γ is seen through secondary charged particles.',
               'Penetration depends on energy and material. In B, α and β⁻ bend oppositely; curvature also depends on p/|q|.')
    elif n==9:
        plot(s,[(lambda u:8*math.sqrt(u)*(1-u)**2/2.293,BLUE)],0,1,'electron K / endpoint','relative counts',[0,.2,.4,.6,.8,1])
        footer(s,'Illustrative allowed nonrelativistic β spectrum ∝ √K (Q−K)²; vanishes at the endpoint.',
               'Electron and antineutrino share Q minus recoil. Mean energy is not universally 0.3Q; Coulomb and mass effects matter.')
    elif n==11:
        for i,(lp,ld,t) in enumerate([(.01,1,'secular: λ_D ≫ λ_P'),(.2,1,'transient: λ_D > λ_P')]):
            x=100+670*i;axes(s,x,590,520,340,'t (scaled)','')
            graph(s,lambda t:math.exp(-lp*t),0,15,x,590,500,260,BLUE)
            graph(s,lambda t:ld/(ld-lp)*(math.exp(-lp*t)-math.exp(-ld*t)),0,15,x,590,500,260,RED)
            label(s,x,180,t,INK,21,590)
        label(s,60,196,'A / A_P(0)',MUTED,19,200)
        footer(s,'Initially pure parent, 100% branch to daughter: A_D = A_P(0) λ_D(e^(−λ_Pt)−e^(−λ_Dt))/(λ_D−λ_P).',
               'Transient late-time ratio A_D/A_P = λ_D/(λ_D−λ_P) > 1: daughter lies above parent, not below.')
    elif n==13:
        plot(s,[(lambda t:2**(-t/5730),BLUE)],0,50000,'age / yr','A / A_modern',[0,5730,20000,50000])
        footer(s,'Ideal ¹⁴C clock: A/A₀ = 2^(−t/5730 yr); at 50 ka ratio ≈ 0.00236.',
               'Practical limits depend on contamination and background; atmospheric variations require measured calibration, not invented wiggles.')
    elif n==14:
        for i,k in enumerate([.7,1,1.5]):
            x=80+445*i;axes(s,x,580,350,310,'generation','')
            for j in range(7):s.rect(x+15+45*j,580-35*min(k**j,5),25,35*min(k**j,5)+1,BLUE,'#edf4fb')
            label(s,x,170,f'k = {k}',RED,23,300)
        label(s,60,196,'relative population',MUTED,19,240)
        footer(s,'Mean generation size N_g = N₀k^g: subcritical decreases, critical stays steady, supercritical grows.',
               'Population bars are expected counts; stochastic chains can die out even when their mean multiplication is above one.')
    elif n==15:
        s.rect(130,190,530,485,INK,'#edf4fb',3,True);label(s,160,210,'shielding / containment',INK,22)
        for i in range(5):s.rect(220+i*60,340,24,230,RED,'#faeceb')
        for i in range(4):s.rect(255+i*60,275,15,205,BLUE,'#edf4fb')
        chain(s,['heat\nexchanger','steam\nturbine','generator'],x=720,y=330,w=620)
        curve(s,[(620,430),(700,430),(700,560),(530,560)],GREEN,4)
        label(s,150,625,'fuel; moderator; absorbing control rods',INK,20,600)
        footer(s,'Fuel fissions; moderator slows neutrons; control rods absorb them; coolant transports heat.',
               'Schematic thermal reactor, not a universal design: fast reactors and other systems use different component choices.')
    elif n==16:
        axes(s,110,450,520,260,'r','')
        curve(s,[(140,560),(230,560),(238,300),(275,255),(340,300),(430,350),(540,398),(620,425)],BLUE,3)
        s.line(130,385,620,385,RED,2,'dashed');label(s,150,350,'few-MeV α energy: below the barrier summit',RED,19,430)
        s.arrow(600,385,270,385,ORANGE,2);label(s,150,545,'deep nuclear well',BLUE,19,260)
        label(s,60,196,'V (scaled)',MUTED,19,200)
        axes(s,810,580,450,310,'E / kT','')
        graph(s,lambda u:15*math.exp(-u-4/math.sqrt(u)),.05,6,810,580,430,270,GREEN)
        label(s,60+760,196,'scaled thermal × tunnelling',MUTED,19,300)
        footer(s,'Short-range attractive nuclear well plus repulsive Coulomb barrier; sub-barrier reaction requires tunnelling.',
               'Gamow window is the competition exp(−E/kT) × exp(−√(E_G/E)); right graph is a chosen dimensionless example.')
    elif n==18:
        s.rect(120,190,1120,470,'#eef2f6','#fbfcfe',2)
        s.dot(200,420,10,INK);label(s,150,455,'source',INK,19,120)
        for ang,l in [(-55,150),(-35,190),(-18,170)]:
            a=math.radians(ang)
            curve(s,[(200,420),(200+l*math.cos(a),420+l*math.sin(a))],RED,6)
        pts=[(200,420)]
        rng=random.Random(26)
        for i in range(14):pts.append((pts[-1][0]+62,pts[-1][1]+rng.choice([-26,-14,0,16,30])))
        curve(s,pts[:10],BLUE,1.5);curve(s,[pts[9],(pts[9][0]+70,pts[9][1]+40),(pts[9][0]+150,pts[9][1]+55)],BLUE,1.5)
        for x,y in [(760,340),(900,420),(1050,300)]:curve(s,[(x,y),(x+34,y-30),(x+58,y-6),(x+86,y-34)],ORANGE,1)
        label(s,600,235,'alpha: short, thick, straight',RED,19,320)
        label(s,760,280,'beta: long, thin, kinked',BLUE,19,300)
        label(s,760,320,'delta-ray wisps near gamma interactions',ORANGE,19,420)
        s.arrow(1120,620,1240,620,GRID,2);label(s,1080,630,'B curves betas visibly',MUTED,18,300)
        footer(s,'Charged particles ionise the supersaturated vapour and leave droplet tracks; gamma rays reveal themselves through secondary electrons.',
               'Schematic chamber sketch, not a photograph reproduction; track lengths and delta-ray density depend on energy and gas.')
    elif n==17:
        chain(s,['p + p','d + e⁺ + νₑ','³He + γ\n(add p)','⁴He + 2p\n(two ³He)'],y=300)
        label(s,200,510,'First two stages occur twice; the last returns two protons.',BLUE,24,1100)
        footer(s,'Net: 4p → ⁴He + 2e⁺ + 2νₑ, with about 26.7 MeV including positron annihilation energy.',
               'Neutrinos carry away part of this energy; the weak initial p+p reaction controls the solar timescale.')
    else:raise ValueError(n)


def semiconductor(n,s):
    if n==1:
        s.arrow(140,500,1220,500,INK,2)
        for p in range(-8,23,2):
            x=140+1050*(p+8)/30;s.line(x,495,x,505,INK,1)
            if p%4==0:label(s,x-16,515,f'10^{p}',MUTED,15,120)
        for t,lo,hi,c in [('conductors',-8,-5,BLUE),('semiconductors',-5,5,GREEN),('insulators',5,22,RED)]:
            x=140+1050*(lo+8)/30;w=1050*(hi-lo)/30;s.rect(x,340,w,100,c,'#edf4fb')
            label(s,x+8,300,f'{t}',c,19,220)
        label(s,60,196,'resistivity ρ / Ω m (log scale)',MUTED,19,420)
        footer(s,'Broad schematic ranges only: copper ≈ 1.7×10⁻⁸ Ω m; intrinsic Si ≈ 10³ Ω m near room temperature.',
               'Temperature, doping, humidity and purity change resistivity enormously; material classes do not have sharp boundaries.')
    elif n==2:
        plot(s,[(lambda u:.3+.4*u,BLUE),(lambda u:.9*math.exp(-2*u),GREEN),(lambda u:.9*math.exp(-5*u),RED)],0,1,'increasing T','normalised R')
        footer(s,'Metal: phonon scattering usually increases R; intrinsic semiconductor: carrier generation can dominate and reduce R.',
               'NTC thermistor example is steeper; normalised trends are illustrative, not a universal ordering or extrapolation to T = 0.')
    elif n in (3,4,7):
        if n==3:
            for i,(t,gap,ins) in enumerate([('metal: partial band',0,False),('semiconductor: ~1 eV',100,False),('insulator: ~5 eV',195,True)]):
                x=80+445*i;panel(s,x,170,410,500,t)
                s.rect(x+50,470,310,110,BLUE,'#edf4fb');s.rect(x+50,360-gap,310,110,RED,'#faeceb')
                rows=5 if not ins else 4
                for j in range(rows):s.dot(x+85+j*50,525,5,BLUE)
            footer(s,'Bands contain many states; electron promotion leaves a valence-band hole.',
                   'Insets are not to a common energy scale; real gaps are ~1.1 eV (Si) and ~9 eV (SiO₂), and band structure is more complex.')
        elif n==4:
            s.rect(170,480,1040,100,BLUE,'#edf4fb');s.rect(170,225,1040,100,RED,'#faeceb')
            s.arrow(420,510,420,275,GREEN,3);s.arrow(950,275,950,510,RED,3)
            label(s,260,390,'generation (photon / phonon)',GREEN);label(s,760,390,'recombination (photon / phonon)',RED)
            s.dot(430,500,6,BLUE);s.ellipse(935,290,20,20,WHITE,RED,2)
            footer(s,'Electron promotion leaves a valence-band hole; equilibrium generation balances recombination.',
                   'Band diagrams omit the density of states and the detailed k-space structure; arrows are illustrative transitions.')
        else:
            for i in range(12):s.line(150+i*38,240,150+i*38,600,GRID,1)
            for j in range(9):s.line(150,240+j*45,570,240+j*45,GRID,1)
            arc(s,300,420,165,c=BLUE);s.dot(300,420,10,RED)
            for yy,t,c in [(285,'conduction band edge',BLUE),(330,'donor level: −26 meV',GREEN),(590,'valence band edge',BLUE)]:
                s.line(700,yy,1180,yy,c,3);label(s,700,yy-26,t,c,19,480)
            label(s,120,655,'Bohr-like orbit radius a* ≈ 2.4 nm over a 0.54 nm lattice cell',INK,20,740)
            footer(s,'Bands contain many states; a shallow donor is described by a hydrogen-like effective-mass model.',
                   'Dielectric screening and light effective mass make the donor orbit large. Band sketches are not to a common quantitative scale.')
    elif n==5:
        for row,hole in enumerate([1,2,3]):
            y=260+150*row
            for i in range(7):s.ellipse(240+130*i,y,34,34,BLUE,WHITE if i==hole else BLUE)
            if row<2:s.arrow(240+130*(hole+1),y+58,240+130*hole,y+58,BLUE,3)
        footer(s,'Successive frames: a neighbouring valence electron fills the vacancy; the hole moves in the opposite direction.',
               'Hole charge is effectively +e. It is an unoccupied electronic state, not a free positive ion moving through the lattice.')
    elif n==6:
        for x,t in [(150,'P donor in Si'),(820,'B acceptor in Si')]:
            panel(s,x,180,510,480,t)
            for i in range(3):
                for j in range(3):s.dot(x+120+100*i,300+100*j,15,BLUE)
            s.dot(x+220,400,22,RED)
        s.arrow(390,400,540,300,GREEN,3);s.ellipse(1068,352,22,22,WHITE,RED,2)
        footer(s,'Pentavalent donor provides a weakly bound electron; trivalent acceptor accepts an electron, leaving a mobile hole.',
               'Ionised donor is positive; ionised acceptor negative. Doped bulk remains nearly charge neutral overall.')
    elif n in (8,9):
        if n==8:
            panel(s,180,230,490,370,'n side: fixed donors +');panel(s,670,230,490,370,'p side: fixed acceptors −')
            for i in range(4):label(s,470,305+60*i,'+',RED,28);label(s,810,305+60*i,'−',BLUE,28)
            for y in [330,410,490]:s.arrow(560,y,760,y,GREEN,3)
            label(s,500,645,'E points n → p; potential decreases n → p',GREEN,23,750)
        else:
            axes(s,180,300,1040,140,'x','');axes(s,180,475,1040,140,'x','');axes(s,180,650,1040,140,'x','')
            label(s,60,196,'ρ (charge density)',MUTED,19,260);label(s,60,372,'E (field)',MUTED,19,180);label(s,60,548,'V (potential)',MUTED,19,220)
            curve(s,[(180,300),(400,300),(400,210),(680,210),(680,390),(960,390),(960,300),(1220,300)],RED)
            curve(s,[(180,475),(400,475),(680,375),(960,475),(1220,475)],GREEN)
            curve(s,[(180+1040*i/240,650-100*(1/(1+math.exp((180+1040*i/240-540)/60)))) for i in range(241)],BLUE)
        footer(s,'Abrupt symmetric depletion model: n left, p right. Positive donor charge → negative acceptor charge.',
               'dE/dx = ρ/ε, E = −dV/dx. V is electrostatic potential; electron energy −eV rises toward the p side.')
    elif n==10:
        plot(s,[(lambda u:.02*math.expm1(4*u) if u>=0 else -.015-(.6*((-u-2)/.5)**2 if u<-2 else 0),BLUE)],-2.5,.9,'V (illustrative)','I (scaled)')
        footer(s,'Forward Shockley I = I_s(exp(V/(ηV_T))−1); V_T ≈ 25.9 mV at 300 K.',
               'Ideal η=1 gives ≈60 mV per current decade. Reverse breakdown is schematic; 0.7 V is not a fixed turn-on law.')
    elif n in (11,12):
        if n==11:
            axes(s,180,290,1000,200,'t','');axes(s,180,520,1000,140,'t','');axes(s,180,700,1000,110,'t','')
            graph(s,math.sin,0,6*math.pi,180,290,980,150,BLUE)
            graph(s,lambda t:max(0,math.sin(t)),0,6*math.pi,180,520,980,105,RED)
            def smoothed(steps=1400,rc=.55):
                ts=[6*math.pi*i/steps for i in range(steps+1)];out=[];v=0
                for t in ts:
                    rect=max(0,math.sin(t));v=rect if rect>v else v*math.exp(-(ts[1]-ts[0])/rc);out.append((t,v))
                return out
            pts=smoothed();curve(s,[(180+980*p[0]/(6*math.pi),700-80*p[1]) for p in pts],GREEN,2)
            label(s,60,196,'input',MUTED,18,150);label(s,60,421,'half-wave',MUTED,18,200);label(s,60,616,'smoothed: ripple ΔV',MUTED,18,320)
            label(s,60,745,'Half-wave rectification recharges once per cycle; capacitor discharge dV/dt ≈ −I_load/C.',INK,20,1260)
            label(s,60,782,'For small ripple: ΔV ≈ I_load/(fC). The smoothed trace is an RC envelope model, not a solved diode waveform.',INK,20,1260)
        else:
            def vdiode(x,y):
                curve(s,[(x-20,y+22),(x,y-22),(x+20,y+22),(x-20,y+22)],BLUE)
                s.line(x-20,y-22,x+20,y-22,BLUE,3)
            s.line(380,200,1060,200,INK,3);label(s,1085,190,'+ rail',RED,20,120)
            s.line(380,560,1060,560,INK,3);label(s,1085,550,'− rail',BLUE,20,120)
            for x in [520,800]:
                s.line(x,200,x,258);vdiode(x,285);s.line(x,312,x,418);vdiode(x,445);s.line(x,472,x,560)
            s.line(520,470-470+470,520,470) if False else None
            s.line(520,385,800,385,GRID,1)
            s.rect(590,630,300,60,GRID,'#edf4fb',2);label(s,608,646,'AC source (midpoints)',INK,20,270)
            s.line(520,385,520,630);s.line(800,385,800,630)
            label(s,520,300,'all four diodes point up',MUTED,18,320)
            resistor(s,1010,1140,380,'R_L');s.line(1060,200,1060,366);s.line(1060,394,1060,560);label(s,1145,340,'load',INK,19,120)
            label(s,900,290,'DC output',GREEN,20,200)
            graph(s,math.sin,0,4*math.pi,180,600,420,60,BLUE)
            graph(s,lambda t:abs(math.sin(t)),0,4*math.pi,660,600,420,60,GREEN)
            label(s,180,505,'input sine',BLUE,18,200);label(s,700,505,'full-wave output: all humps positive',GREEN,18,430)
            footer(s,'The four diodes steer both half-cycles through the load in the same direction.',
                   'Two diode drops in each path. Full-wave ripple recharge frequency is 2f; ΔV ≈ I_load/(2fC).')
    elif n==13:
        s.line(150,300,300,300);resistor(s,300,650,300,'R_s');s.line(650,300,1180,300)
        s.line(780,300,780,600);s.line(1100,300,1100,430)
        s.line(1076,430,1124,430,BLUE,3);s.line(1076,478,1124,478,BLUE,3)
        s.line(1076,430,1100,454,BLUE,3);s.line(1124,478,1100,454,BLUE,3);label(s,1132,440,'Zener diode (reverse)',BLUE,18,300)
        s.rect(1080,478,40,90,INK,WHITE);s.line(1100,568,1100,600);s.line(150,600,1180,600)
        label(s,120,225,'V_in',BLUE);label(s,880,225,'V_out ≈ V_Z',RED);label(s,700,640,'Zener cathode at the output node; anode grounded',BLUE,19,620)
        footer(s,'I_R = (V_in−V_Z)/R_s = I_L + I_Z. The Zener is reverse biased and shunts excess current.',
               'Check minimum I_Z at low input / maximum load; maximum I_Z and dissipation at high input / minimum load.')
    elif n==14:
        chain(s,['1.9 eV\n653 nm red','2.26 eV\n549 nm green','2.6 eV\n477 nm blue','3.4 eV\n365 nm UV'],y=300)
        s.arrow(120,520,1220,520,INK,2);label(s,120,540,'400 nm  ←  wavelength  →  700 nm (visible region; the 3.4 eV emitter is ultraviolet)',MUTED,18,1100)
        footer(s,'Approximate photon relation λ(nm) = 1240/E_photon(eV); materials and alloy composition set the gap.',
               'Gap alone does not ensure an efficient LED: direct/indirect structure, dopants and transition mechanisms matter.')
    elif n==15:
        panel(s,90,185,585,470,'Reverse-biased photodiode');panel(s,725,185,585,470,'Solar cell: no external bias')
        chain(s,['photon','e⁻–hole','meter'],x=110,y=320,w=550)
        axes(s,790,535,440,250,'V','')
        graph(s,lambda u:.1*math.expm1(3*u)-.8,0,1,790,470,390,120,RED)
        label(s,830,595,'I < 0, V > 0: delivered power',GREEN,19,420);label(s,740,300,'I (passive sign)',MUTED,18,240)
        footer(s,'Illumination adds a photocurrent: I = I_s(exp(V/(ηV_T))−1) − I_ph in the passive sign convention.',
               'Photodiode often uses reverse bias; a solar cell drives a load in the fourth quadrant without a bias supply.')
    elif n==16:
        s.rect(190,260,250,310,BLUE,'#edf4fb');s.rect(480,260,60,310,RED,'#faeceb');s.rect(595,260,520,310,BLUE,'#edf4fb')
        label(s,200,215,'n⁺ emitter',BLUE,20,200);label(s,470,215,'p base (thin)',RED,20,180);label(s,700,215,'n collector',BLUE,20,220)
        s.arrow(300,420,1050,420,BLUE,4);label(s,320,470,'electron flow →',BLUE)
        s.arrow(1080,650,850,650,RED,3);s.arrow(400,650,170,650,RED,3);s.arrow(560,730,560,600,RED,3)
        label(s,600,700,'conventional currents: I_C, I_B in; I_E out',RED,19,520)
        footer(s,'Forward-active npn: V_B > V_E (BE forward), V_C > V_B (BC reverse); base thin and lightly doped.',
               'Conventional currents satisfy I_E = I_C + I_B; electron flow is opposite to conventional current.')
    elif n==17:
        axes(s,150,610,1010,380,'V_CE / V_CC','')
        graph(s,lambda x:1-x,0,1,150,610,1000,330,RED)
        for a in [.2,.45,.7]:graph(s,lambda x,a=a:a*(1-math.exp(-25*x)),0,1,150,610,1000,330,BLUE)
        s.dot(700,610-330*.45,6,GREEN);label(s,730,430,'Q-point (schematic)',GREEN)
        label(s,60,196,'I_C / (V_CC/R_C)',MUTED,19,300)
        footer(s,'Load line: V_CE = V_CC − I_C R_C. Increasing base drive raises collector current and lowers collector voltage.',
               'Switch: cutoff near I_C=0; saturation often V_CE≈0.2 V, device-dependent. Include base-current limiting resistance.')
    elif n==18:
        chain(s,['A, B','XOR → sum S','AND → carry C'],y=230)
        for i,t in enumerate(['A B | S C','0 0 | 0 0','0 1 | 1 0','1 0 | 1 0','1 1 | 0 1']):label(s,270,375+55*i,t,BLUE,25,380)
        label(s,780,390,'S = A ⊕ B\nC = A · B\nA + B = S + 2C',RED,25,460)
        footer(s,'AND: both 1; OR: either 1; NOT: invert; NAND/NOR invert AND/OR; XOR: inputs differ.',
               'Half-adder shown with a complete four-row table. Gate blocks are editable functional symbols, not an IEC/ANSI glyph catalogue.')
    else:raise ValueError(n)

def communication(n,s):
    if n==1:
        chain(s,['source','transmitter','channel','receiver','destination'],y=300)
        s.arrow(300,470,430,470,GRID,2);label(s,100,465,'noise / interference injected in the channel',RED,20,620)
        footer(s,'Information flows source → transmitter → channel → receiver → destination; noise enters in the channel.',
               'Two-way links add a duplexer and reverse-direction blocks; a channel may be a cable, free space or an optical fibre.')
    elif n==2:
        plot(s,[(lambda f:math.exp(-((f-1000)/1500)**2)*(.6+.4*math.cos(f/220)),BLUE)],0,4000,'audio frequency / Hz','relative amplitude')
        for f,t in [(300,'~300 Hz'),(3400,'~3.4 kHz')]:s.line(150+1000*f/4000,300,150+1000*f/4000,620,GRID,2,'dashed');label(s,150+1000*f/4000-40,250,t,INK,20,260)
        footer(s,'Speech/music occupies roughly 300 Hz–3.4 kHz; this extent sets the sideband bandwidth needed for AM.',
               'Frequency axis linear and the shape illustrative: a real voice spectrum has formants and varies with time.')
    elif n in (3,4):
        # Local-coordinate schematic; the Earth is a shallow arc so nothing runs off-canvas.
        def ground(y0):
            curve(s,[(120+1100*i/40,y0+90*(i/40)**2) for i in range(41)],INK,2)
        if n==3:
            ground(330);s.rect(120,250,1160,40,GRID,'#edf4fb');label(s,140,210,'ionosphere: partially ionised layer',INK,21,620)
            s.dot(300,430,9,RED);label(s,268,455,'transmitter',RED,19,220)
            s.arrow(300,425,700,300,BLUE,2);s.arrow(700,300,1060,368,BLUE,2)
            label(s,520,270,'sky wave refracted back to Earth',BLUE,19,480)
            label(s,520,520,'ground wave; skip distance measured to the first return',GREEN,20,760)
            s.dot(1060,380,9,GREEN);label(s,1010,405,'receiver',GREEN,19,200)
        else:
            ground(330);label(s,140,210,'line-of-sight: horizon distance sets the range',INK,21,720)
            s.line(300,560,300,400,BLUE,5);s.line(900,560,900,320,BLUE,7)
            s.line(300,400,760,560,GREEN,2);s.line(900,320,1160,520,GREEN,2)
            label(s,470,430,'d ≈ √(2Rh₁) + √(2Rh₂)',INK,23,620)
            label(s,285,600,'h',BLUE,20,60);label(s,890,600,'4h',BLUE,20,80)
        footer(s,'Radio horizon for height h is d ≈ √(2Rh); taller masts extend line-of-sight range.',
               'Ground curvature and the fourth-thirds Earth-radius refraction are engineering conventions; treat as an estimate.')
    elif n==5:
        s.arrow(140,500,1220,500,INK,2);label(s,60,196,'amplitude (schematic bands)',MUTED,19,380)
        for fc,c in [(600,BLUE),(800,GREEN),(1000,RED)]:
            x=140+1080*fc/1200;s.rect(x-45,330,90,170,c,c)
            label(s,x-95,270,f'{fc} kHz',c,19,190);label(s,x-95,300,'4 kHz wide',MUTED,17,190)
        label(s,140,540,'non-overlapping FDM bands; guard bands between channels are not drawn',MUTED,19,900)
        footer(s,'FDM stacks non-overlapping modulated bands so several channels share one wideband medium.',
               'Channel spacing must exceed the message bandwidth to leave guard bands; band heights are illustrative.')
    elif n==6:
        for i,(mu,c) in enumerate([(.5,BLUE),(1,GREEN),(1.3,RED)]):
            axes(s,150,180+i*190,1000,120,'t','')
            graph(s,lambda t,m=mu:(1+m*math.sin(.3*t))*math.sin(6*t),0,6*math.pi,150,220+i*190,1000,55,c,steps=900)
            curve(s,[(150+1000*j/200,220+i*190-55*(1+mu*math.sin(.3*(1000*j/200)*6*math.pi/1000))) for j in range(201)],c,1.5,True)
            label(s,1160,180+i*190,f'μ = {mu}'+(' (over-modulated)' if mu>1 else ''),c,20,220)
        footer(s,'s(t) = A_c[1 + μ cos(2πf_m t)] cos(2πf_c t) with μ = A_m/A_c; envelope shown dashed.',
               'μ > 1 clips the envelope and creates sideband splatter; illustrative envelope and carrier frequencies are schematic.')
    elif n==7:
        axes(s,150,240,1000,120,'t','')
        graph(s,lambda t:math.sin(.3*t),0,8*math.pi,150,240,1000,90,INK,steps=700)
        label(s,890,150,'message f_m',INK,19,200)
        axes(s,150,520,1000,150,'t','')
        graph(s,lambda t:math.sin(4.5*t+3*math.cos(.3*t)),0,8*math.pi,150,520,1000,120,BLUE,steps=2400)
        label(s,150,660,'constant amplitude; instantaneous frequency f_c ± Δf',BLUE,19,520)
        footer(s,'Carrier frequency swings between f_c − Δf and f_c + Δf at the message rate; amplitude stays fixed.',
               'For a single tone, Carson’s rule estimates bandwidth ≈ 2(Δf + f_m); the drawing is exaggerated for legibility.')
    elif n==8:
        diode(s,170,330,300);cap(s,330,520,300,'C');resistor(s,520,760,300,'R')
        s.line(760,300,760,430);s.line(170,430,760,430);s.line(330,430,330,300,GRID,2)
        axes(s,170,600,900,90,'t','');graph(s,lambda t:(1+.6*math.sin(.3*t))*math.sin(5*t),0,12,170,600,880,80,BLUE,steps=1200)
        label(s,60,196,'input AM',MUTED,18,180)
        footer(s,'Diode conducts on positive peaks; R discharges C slowly, following the AM envelope.',
               'Avoid both extremes: 1/f_c ≪ RC ≪ 1/f_m. Too small RC follows the carrier; too large RC lags the envelope.')
    elif n==9:
        chain(s,['antenna','RF amplifier','mixer','IF amplifier\n455 kHz','detector','audio → speaker'],y=300)
        s.arrow(390,250,390,190,GRID,3);label(s,250,150,'local oscillator f_LO',GRID,20,420)
        label(s,120,520,'f_IF = f_LO − f_RF (high-side injection illustrated); image frequency also reaches the mixer.',INK,21,1250)
        footer(s,'Mixing translates every incoming station to a common IF, where fixed narrowband filtering is efficient.',
               'Image rejection, mixer spurs and oscillator stability are practical design limits; 455 kHz is a common AM IF.')
    elif n==10:
        plot(s,[(lambda u:math.log2(1+10**(u/10))/10,BLUE)],-10,40,'S/N / dB','C/B (bit/s/Hz), 0 to 10',[0,10,20,30])
        for sn,t in [(0,'1'),(20,'≈6.66'),(30,'≈9.97')]:
            x=150+1000*(sn+10)/50;y=620-330*math.log2(1+10**(sn/10))/12;s.dot(x,y,6,RED);label(s,x-30,y-60,f'{sn} dB → {t}',RED,19,320)
        footer(s,'Shannon–Hartley: C/B = log₂(1 + S/N) for a band-limited additive white-Gaussian channel.',
               'Capacity is an upper bound achievable with suitable coding and long blocks, not a promise about a particular modem.')
    elif n==11:
        chain(s,['mic','pre-emphasis','VCO','frequency\nmultiplier','power amp','antenna'],y=230)
        s.arrow(200,150,200,215,GRID,2);label(s,60,105,'carrier oscillator',GRID,19,330)
        chain(s,['antenna','RF amp','limiter','discriminator','de-emphasis','audio → speaker'],y=430)
        footer(s,'Transmitter: voltage-controlled oscillator deviates the carrier; receiver recovers the message after limiting.',
               'Limiter suppresses amplitude noise, discriminator converts frequency deviation to voltage; exact order varies by design.')
    elif n==12:
        axes(s,200,540,960,260,'frequency','')
        s.line(600,540,600,230,BLUE,5);label(s,545,185,'carrier A_c at f_c',BLUE,19,300)
        for dx,t in [(-150,'lower sideband f_c − f_m'),(150,'upper sideband f_c + f_m')]:
            s.line(600+dx,540,600+dx,380,RED,4);label(s,600+dx-140,330,t,RED,19,340)
        s.arrow(450,570,750,570,GREEN,2);label(s,470,590,'bandwidth 2f_m',GREEN,20,320)
        label(s,350,240,'sideband height μA_c/2; carrier height A_c',MUTED,19,560)
        footer(s,'AM with a single sinusoidal tone: carrier plus two sidebands; total average power = P_c(1 + μ²/2).',
               'Sidebands carry the information; they appear only while the message is present, while the carrier is always there.')
    else:raise ValueError(n)

def relativity(n,s):
    if n==1:
        s.rect(110,255,150,80,GRID,'#edf4fb');label(s,120,220,'source',INK,20,200)
        s.line(596,271,644,319,INK,3);label(s,648,300,'half-silvered mirror',INK,19,340)
        s.arrow(260,295,596,295,ORANGE,3)
        s.arrow(628,280,1060,280,BLUE,2);s.arrow(1060,310,632,310,GREEN,2)
        s.rect(1072,235,26,90,INK,WHITE);label(s,1010,200,'M₁, arm L',INK,19,250)
        s.arrow(620,285,620,130,BLUE,2);s.arrow(652,130,652,282,GREEN,2)
        s.rect(580,104,80,26,INK,WHITE);label(s,500,70,'M₂, arm L',INK,19,250)
        s.arrow(640,330,640,460,RED,2);s.rect(540,460,200,80,GRID,'#edf4fb')
        label(s,556,486,'detector / eyepiece',INK,20,320)
        label(s,60,600,'expected aether-drift shift ΔN ≈ (2L/λ)(v²/c²) — with L≈11 m, λ≈590 nm, v≈30 km/s this is ≈0.4 fringe; observed < 0.01',RED,20,1200)
        footer(s,'Recombination at the half-silvered mirror lets the two round trips interfere.',
               'The null result constrains a preferred frame; arm lengths are drawn short and the beam paths are schematic.')
    elif n==2:
        s.rect(220,260,760,44,GRID,'#edf4fb');label(s,230,222,'train, passenger at midpoint',BLUE,20,560)
        s.rect(150,330,900,44,'#ffffff',WHITE,2);label(s,160,382,'platform, observer at midpoint',INK,20,520)
        for x,c in [(220,RED),(980,RED)]:
            for r,al in [(55,.22),(120,.12),(195,.06)]:s.ellipse(x-r,350-r,2*r,2*r,c,c,1)
        s.arrow(990,250,1080,250,GREEN,3);label(s,990,205,'v',GREEN)
        footer(s,'Platform frame: both flashes reach the midpoint together ⇒ simultaneous strikes.',
               'Train frame: the passenger moves toward the front strike, so front light arrives first ⇒ not simultaneous in that frame.')
    elif n==3:
        panel(s,120,180,420,450,'clock in S′ (at rest)');s.line(230,230,230,540,BLUE,3);s.line(430,230,430,540,BLUE,3)
        for i in range(5):s.line(230,250+i*70,430,250+i*70,ORANGE,2)
        panel(s,600,180,690,450,'clock moving in S')
        for xx in [660,920,1180]:s.line(xx,230,xx,540,BLUE,3)
        s.line(660,300,1180,470,ORANGE,2);s.line(660,470,1180,300,ORANGE,2,'dashed')
        s.line(660,470,1180,470,GRID,2);label(s,860,520,'half-trip: vΔt/2',INK,19,300)
        footer(s,'c²Δt²/4 = L² + v²Δt²/4 ⇒ Δt = γ·2L/c with γ = 1/√(1 − v²/c²).',
               'Light speed is c in every inertial frame; only the moving clock’s proper time is dilated.')
    elif n==4:
        panel(s,110,180,585,470,'Earth frame');panel(s,735,180,585,470,'muon frame')
        for x,t in [(150,'15 km'),(780,'15 km / γ = 0.95 km')]:
            s.line(x,260,x,600,GRID,2);label(s,x+20,300,t,INK,20,300)
        label(s,220,470,'v = 0.998c, γ ≈ 15.8\nlifetime ×γ ≈ 34.8 μs\ntravels ≈ 10.4 km before decaying',BLUE,20,470)
        label(s,770,470,'atmosphere contracted\nrest lifetime 2.2 μs\n0.95 km only: reaches ground',GREEN,20,560)
        footer(s,'Both frames agree the muon reaches sea level: they disagree about which quantity is dilated.',
               'The numbers are the standard illustrative set; real muons have a distribution of speeds and decay proper times.')
    elif n==5:
        plot(s,[(lambda u:u+.6,GRID),(lambda u:(u+.6)/(1+.6*u),BLUE)],0,1,'u′/c (with v = 0.6c)','u/c')
        label(s,700,255,'dashed Galilean; solid relativistic',INK,20,470)
        s.dot(150+1000*.6/1.6,620-330*(1.2/1.96),6,RED)
        footer(s,'Relativistic addition u = (u′ + v)/(1 + u′v/c²) keeps every result at or below c.',
               'With u′ = c the result is c for any sublight v; low-speed agreement is first-order in v/c.')
    elif n==6:
        s.line(300,600,900,600,BLUE,3);s.line(300,600,300,220,RED,3);s.line(300,220,900,600,GREEN,3)
        label(s,560,620,'pc',BLUE);label(s,235,400,'mc²',RED);label(s,560,370,'E',GREEN)
        footer(s,'E² = (pc)² + (mc²)²; photon m = 0 gives E = pc; at rest E = mc².',
               'The triangle is a relation among magnitudes, not a spatial picture of momentum direction; for massive particles v = pc²/E.')
    elif n==7:
        # log vertical scale: γ from 1 to 11
        pts=[(150+1000*u/1,620-330*math.log10(1/math.sqrt(1-u*u))/math.log10(11)) for u in [i/1000 for i in range(1,1000)]]
        axes(s,150,620,1020,380,'v/c','')
        label(s,60,196,'γ (log scale, 1 to 11)',MUTED,19,300)
        curve(s,pts,BLUE,3)
        for v,t,dy in [(.140,'1.01',-40),(.866,'2',-40),(.99,'7.09',-40),(.995,'10',-40)]:
            g=1/math.sqrt(1-v*v);x=150+1000*v;y=620-330*math.log10(g)/math.log10(11);s.dot(x,y,6,RED);label(s,x-40,y+dy,t,RED,19,200)
        footer(s,'γ = 1/√(1 − v²/c²) stays near 1 for slow motion and diverges as v → c. Vertical axis is logarithmic.',
               'Exact points: γ=2 at v=(√3/2)c≈0.866c; γ=7.09 at 0.99c; γ=10 at 0.995c.')
    elif n==8:
        s.arrow(300,690,300,150,INK,2);s.arrow(150,690,1240,690,INK,2);label(s,900,655,'space',INK)
        s.line(300,650,900,250,GREEN,3);s.line(900,250,1240,480,RED,3)
        for yy in [650,470,290]:s.line(300,yy,1240,yy,GRID,1,'dashed')
        label(s,830,200,'turnaround',GREEN);label(s,1040,430,'B returns',RED)
        footer(s,'A stays on Earth (vertical world line); B travels out at 0.8c, turns and returns.',
               'A measures 5 y each way (proper 10 y); B’s proper time is 6 y in the ideal instant-turn case. Tilted slices during the turn are the seat of the asymmetry.')
    elif n==9:
        plot(s,[(lambda u:u/7.02,GRID),(lambda u:u/math.sqrt(1-u*u)/7.02,BLUE)],0,.99,'v/c','p/(mc), scaled to p(0.99c) = 1')
        label(s,700,290,'dashed Newtonian p = mv; solid p = γmv',INK,20,560)
        footer(s,'Relativistic momentum diverges as v → c; the two expressions agree for v ≪ c.',
               'p/(mc) = γv/c = 1 at v = (1/√2)c ≈ 0.707c, where γ = √2, independent of particle mass.')
    elif n==10:
        s.arrow(120,400,620,400,ORANGE,5);label(s,300,340,'E_γ ≥ 1.022 MeV',ORANGE,22,400);nucleus(s,660,400)
        s.arrow(690,400,980,270,BLUE,3);s.arrow(690,400,980,530,RED,3)
        label(s,930,225,'e⁻ + e⁺: 2m_ec² = 1.022 MeV',BLUE,20,420)
        footer(s,'Stationary heavy nucleus M absorbs momentum recoil: E_γ,th = 2m_ec²(1 + m_e/M) ≈ 1.022 MeV.',
               'In the CM frame threshold products are at rest; energy and momentum must both be conserved, so a lone photon cannot pair-produce in vacuum.')
    elif n==11:
        s.ellipse(320,520,360,360,BLUE,'#edf4fb',2);label(s,430,660,'Earth',INK,20,200)
        s.ellipse(760,220,54,54,GRID,WHITE);label(s,700,150,'GPS satellite, 20,200 km altitude',INK,20,480)
        s.line(320,520,760,247,GRID,1,'dashed')
        s.arrow(730,290,730,430,GREEN,3);label(s,742,330,'SR: clock runs slow, −7.2 μs/day',GREEN,19,420)
        s.arrow(800,430,800,290,RED,3);label(s,812,370,'GR: clock runs fast, +45.9 μs/day',RED,19,420)
        label(s,200,185,'net +38.7 μs/day; frequency offset before launch',INK,22,700)
        footer(s,'Net correction ≈ +38.7 μs/day; the transmitted clock frequency is offset before launch.',
               'Signs and magnitudes depend on the chosen orbit and definitions; an uncorrected 38.7 μs/day offset corresponds to about 11.6 km/day of positioning error.')
    elif n==12:
        panel(s,110,180,585,470,'barn frame: pole contracted');panel(s,735,180,585,470,'pole frame: barn contracted')
        s.rect(180,340,420,70,GRID,'#edf4fb');s.rect(215,330,360,20,BLUE,BLUE)
        label(s,300,470,'both barn doors close together\nat the same time: pole fits',INK,20,530)
        s.rect(800,300,320,60,RED,'#faeceb');s.rect(760,265,430,20,BLUE,BLUE)
        label(s,780,470,'front door opens before\nback door closes: pole fits,\nbut the events are not simultaneous',GREEN,20,620)
        footer(s,'Contract each frame in its own coordinates: length contraction and simultaneity change together.',
               'The paradox dissolves once relative simultaneity is applied; no single frame shows the pole in two places at once.')
    else:raise ValueError(n)

DRAW={'photoelectric-effect':modern,'atomic-structure':atomic,'x-rays':xrays,
      'nuclear-physics':nuclear,'semiconductors':semiconductor,
      'communication-systems':communication,'special-relativity':relativity}

BRIEF=re.compile(r'^> \[!abstract\] DIAGRAM (D\d+\.(\d+)) · ([^\n]+)\n((?:>[^\n]*\n)*)',re.M)

def main():
    only=[a for a in sys.argv[1:] if not a.startswith('-')]
    for slug,fn in DRAW.items():
        if only and slug not in only:continue
        name=slug.capitalize()+'.md';master=ROOT/slug/name
        text=master.read_text()
        matches=[m for m in BRIEF.finditer(text) if m.group(4).count('*Show:*')]
        assert matches,f'{slug}: no DIAGRAM briefs found'
        mp=ROOT/slug/'figures.json';manifest=json.loads(mp.read_text());drawings=[]
        for m in matches:
            ident,title,raw=m.group(1),m.group(3),m.group(0);num=int(m.group(2))
            block=re.sub(r'(?:> \*\*Companion:\*\*[^\n]*\n)+$','',raw)
            assert block.count('DIAGRAM ')==1,f'{ident}: brief block absorbed a neighbouring brief'
            scene=Scene(ident);fn(num,scene);assert scene.elements,f'{ident}: empty scene'
            stem,rel=scene_file(slug,ident,title,scene)
            sr=re.search(r'\*Search:\* ([^\n]*)',m.group(4))
            search=sr[1].strip() if sr else f'{slug} DIAGRAM {ident}'
            embed=f'![[../_obsidian/excalidraw/{stem}|900]]'
            if embed in text:
                # The companion block is already in place; never touch it again, so
                # regeneration stays byte-identical no matter how often it runs.
                block=raw
            else:
                start=text.index(raw);rest=text[start+len(raw):]
                text=text[:start]+block+f'> **Companion:** native editable scene `{stem}.excalidraw.md`; this brief has no SVG source.\n\n{embed}\n'+rest
            drawings.append(dict(id=ident,kind='excalidraw',title=title,
                show='Native scene drawn from the original DIAGRAM brief; editable primitives, no raster or SVG source.',
                search=search,file=rel,source=f'{slug}/{name} · {ident} brief'))
        series=sorted({d['id'].split('.')[0] for d in drawings})
        manifest.update(drawings=drawings,renderer='obsidian-excalidraw-plugin@2.27.3',
            drawing_numbering=f"Original DIAGRAM ids preserved with gaps ({', '.join(series)} series); scenes drawn from briefs, not converted from SVG.")
        master.write_text(text);mp.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
        print(f'{slug}: {len(drawings)} native brief scenes')

if __name__=='__main__':main()
