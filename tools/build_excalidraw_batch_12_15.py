#!/usr/bin/env python3
"""Build editable Excalidraw scenes for Mechanics Part 12 and electrostatics Parts 13–15.

The repository consolidates the three electrostatics plan parts into one master
chapter (D13.1–D13.26); this batch therefore creates 14 D12 scenes and 26 D13
scenes. Each native scene is embedded below its original DIAGRAM brief and
recorded in the chapter's figures.json.

Run from the repository root:
    python3 tools/build_excalidraw_batch_12_15.py
"""
from __future__ import annotations

import json
import math
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools.build_excalidraw_batch import (  # noqa: E402
    BLUE, GREEN, GRID, INK, MUTED, ORANGE, PALE_BLUE, PALE_GREEN,
    PALE_ORANGE, PALE_RED, PALE_TEAL, PURPLE, RED, TEAL, WHITE,
    Scene, hatch_polygon, panel, polyline, scene_file,
)


def arc(s: Scene, cx: float, cy: float, r: float, start: float, stop: float,
        color: str = PURPLE, sw: float = 2, steps: int = 28,
        dash: str = "solid") -> None:
    pts = [(cx + r * math.cos(t), cy - r * math.sin(t))
           for t in [start + (stop - start) * i / steps for i in range(steps + 1)]]
    polyline(s, pts, color, sw, dash)


def axes(s: Scene, x0: float, y0: float, x1: float, y1: float,
         xlabel: str, ylabel: str, color: str = INK) -> None:
    s.arrow(x0, y0, x1, y0, color, 1.8)
    s.arrow(x0, y0, x0, y1, color, 1.8)
    s.text(x1 - 18, y0 + 8, xlabel, 15, color, 100)
    s.text(x0 - 36, y1 - 23, ylabel, 15, color, 80)


def charge(s: Scene, x: float, y: float, sign: str, color: str = BLUE,
           radius: float = 18, size: int = 18) -> None:
    s.ellipse(x - radius, y - radius, 2 * radius, 2 * radius, color, WHITE, 2)
    s.text(x - radius, y - size * .62, sign, size, color, 2 * radius, "center")


def vec(s: Scene, p: tuple[float, float], q: tuple[float, float],
        label: str = "", color: str = BLUE, sw: float = 2.5,
        label_dx: float = 7, label_dy: float = -22, size: int = 15) -> None:
    s.arrow(p[0], p[1], q[0], q[1], color, sw)
    if label:
        s.text(q[0] + label_dx, q[1] + label_dy, label, size, color, 150)


def dot_path(s: Scene, pts: list[tuple[float, float]], color: str = BLUE,
             sw: float = 2.4, dash: str = "solid") -> None:
    polyline(s, pts, color, sw, dash)


def cscene(key: str, title: str, subtitle: str = "") -> Scene:
    s = Scene(key)
    s.title(title, subtitle or None)
    return s


# ── PART 12 · ELASTICITY ──────────────────────────────────────────────────────

def d121() -> Scene:
    s = cscene("D12.1", "Reading the ductile stress–strain curve",
               "Landmarks are material limits; the initial slope is Young's modulus.")
    x0, y0, x1, y1 = 170, 720, 1040, 168
    axes(s, x0, y0, x1, y1, "strain ε", "stress σ")
    def p(u: float, v: float) -> tuple[float, float]:
        return x0 + u * (x1 - x0), y0 - v * (y0 - y1)
    ductile = [p(*q) for q in [(0,0),(.035,.18),(.13,.52),(.18,.57),(.23,.60),
                                (.31,.61),(.39,.60),(.65,.77),(.80,.95),(.88,.82),(.95,.65)]]
    # Recoverable elastic energy is the area under the straight Hooke segment.
    tri = [p(0,0), p(.13,.52), p(.13,0)]
    hatch_polygon(s, tri, PALE_GREEN, 12)
    dot_path(s, ductile, BLUE, 3)
    brittle = [p(*q) for q in [(0,0),(.018,.25),(.05,.61),(.082,.88),(.095,.98)]]
    dot_path(s, brittle, RED, 2.5, "dashed")
    marks = [("P · proportional",.13,.52,BLUE,-50,-40),
             ("E · elastic limit",.18,.57,PURPLE,7,-38),
             ("Y · yield",.31,.61,ORANGE,-35,-43),
             ("U · ultimate",.80,.95,TEAL,-48,-42),
             ("F · fracture",.95,.65,RED,-122,8)]
    for label,u,v,col,dx,dy in marks:
        xx,yy=p(u,v); s.dot(xx,yy,5,col); s.text(xx+dx,yy+dy,label,14,col,150)
    xx,yy=p(.07,.30); s.text(xx+4,yy+10,"recoverable elastic energy",14,GREEN,210)
    s.text(755,608,"ductile steel",14,BLUE,115)
    s.text(270,218,"brittle",14,RED,70)
    s.text(1090,220,"initial slope = Y",17,GREEN,190)
    s.text(1090,278,"Yield is not fracture",16,INK,220)
    s.text(1090,335,"Design below yield\n(with a safety factor).",15,MUTED,240)
    s.text(1090,426,"Brittle: steep curve,\nlittle plastic strain",14,RED,230)
    return s


def d122() -> Scene:
    s = cscene("D12.2", "Three moduli, three deformation experiments",
               "The modulus is a material property; stiffness also depends on geometry.")
    specs = [(35,132,420,575,"YOUNG'S MODULUS · Y"),
             (500,132,420,575,"BULK MODULUS · B"),
             (965,132,420,575,"SHEAR MODULUS · G")]
    for x,y,w,h,head in specs: panel(s,x,y,w,h,head)
    # Tension wire and lateral contraction.
    s.rect(145,310,205,82,BLUE,PALE_BLUE,2)
    s.rect(158,321,179,60,BLUE,"transparent",1.2)
    s.arrow(150,350,85,350,ORANGE,3); s.arrow(345,350,410,350,ORANGE,3)
    s.text(215,267,"F",17,ORANGE,30); s.text(215,405,"ΔL",17,BLUE,45)
    s.arrow(180,315,180,338,RED,1.8); s.arrow(180,387,180,365,RED,1.8)
    s.text(101,468,"σ = F/A",18,INK,120); s.text(101,507,"ε = ΔL/L",18,INK,150)
    s.text(101,559,"Y = σ/ε",23,GREEN,160)
    # Hydrostatic compression: dashed original cube, shrunken solid cube.
    s.rect(610,302,195,150,GRID,"transparent",1.5)
    s.rect(632,319,150,118,BLUE,PALE_BLUE,2)
    for xx in [670,707,744]:
        s.arrow(xx,274,xx,312,ORANGE,2); s.arrow(xx,481,xx,444,ORANGE,2)
    for yy in [350,395]:
        s.arrow(584,yy,626,yy,ORANGE,2); s.arrow(833,yy,790,yy,ORANGE,2)
    s.text(628,250,"pressure p on all faces",15,ORANGE,230)
    s.text(554,503,"B = −Δp/(ΔV/V)",19,GREEN,245)
    s.text(554,544,"volume decreases",15,MUTED,180)
    # Simple shear: top shifts right, bottom fixed; opposing tangential forces.
    s.rect(1072,310,200,150,GRID,"transparent",1.4)
    dot_path(s,[(1072,310),(1272,310),(1245,452),(1072,452),(1072,310)],BLUE,2.8)
    s.arrow(1110,310,1170,310,ORANGE,3); s.arrow(1240,452,1180,452,ORANGE,3)
    s.text(1140,269,"F",16,ORANGE,28); s.text(1172,470,"γ",20,PURPLE,30)
    s.text(1030,514,"τ = F/A",18,INK,130); s.text(1030,554,"γ = shear angle",16,INK,190)
    s.text(1030,599,"G = τ/γ",23,GREEN,150)
    return s


def d123() -> Scene:
    s = cscene("D12.3", "A series rod carries equal force, not equal stress",
               "The thinner segment has the larger stress because σ = F/A.")
    # Joined rod; area steps down at the weld.
    s.rect(115,335,360,132,BLUE,PALE_BLUE,2.5)
    s.rect(475,368,380,66,TEAL,PALE_TEAL,2.5)
    s.line(475,323,475,478,INK,1.5,"dashed")
    vec(s,(115,400),(45,400),"F",ORANGE,3,-26,-26,18)
    vec(s,(855,400),(925,400),"F",ORANGE,3,7,-26,18)
    s.text(250,376,"A₁, L₁, Y₁",17,BLUE,170)
    s.text(585,382,"A₂ < A₁, L₂, Y₂",17,TEAL,230)
    s.text(310,490,"ΔL₁ = FL₁/(A₁Y₁)",15,BLUE,230)
    s.text(570,457,"ΔL₂ = FL₂/(A₂Y₂)",15,TEAL,240)
    panel(s,985,178,350,470,"STRESS ALONG THE ROD")
    s.text(1015,242,"σ₁ = F/A₁",16,BLUE,180)
    s.rect(1045,285,82,88,BLUE,PALE_BLUE,1.5)
    s.text(1190,242,"σ₂ = F/A₂",16,TEAL,180)
    s.rect(1198,285,82,146,TEAL,PALE_TEAL,1.5)
    s.text(1014,475,"same internal F",15,INK,200)
    s.text(1014,518,"thin segment: larger σ",16,RED,240)
    s.text(74,630,"Series compatibility: total extension is ΔL₁ + ΔL₂.",17,GREEN,700)
    return s


def d124() -> Scene:
    s = cscene("D12.4", "Thermal stress: expand freely, then restore the length",
               "Heating against rigid walls creates compression σ = YαΔT.")
    panel(s,45,145,620,430,"FREE ROD · NO STRESS")
    s.rect(150,300,320,70,BLUE,PALE_BLUE,2)
    s.rect(150,300,375,70,BLUE,"transparent",1.8,False,0)
    s.line(470,282,525,282,GRID,1.4,"dashed")
    s.arrow(470,391,525,391,TEAL,2.3); s.text(387,408,"αLΔT",18,TEAL,105)
    s.text(150,249,"initial length L",16,INK,155)
    s.text(165,464,"Dashed edge = free expanded end",15,MUTED,310)
    panel(s,700,145,660,430,"BETWEEN RIGID WALLS · COMPRESSED BACK")
    s.rect(825,300,340,70,BLUE,PALE_BLUE,2)
    for yy in range(268,405,16):
        s.line(780,yy,815,yy+14,GRID,1); s.line(1175,yy,1210,yy+14,GRID,1)
    s.line(785,254,785,424,INK,5); s.line(1205,254,1205,424,INK,5)
    s.arrow(820,334,875,334,RED,3); s.arrow(1170,334,1115,334,RED,3)
    s.text(945,247,"reaction F",16,RED,115)
    s.text(814,416,"compress back by αLΔT",16,PURPLE,260)
    s.text(705,630,"Inset: rail expansion gaps prevent the restraint force building up.",16,INK,620)
    # Rail sleepers and a small expansion gap.
    s.line(780,700,1275,700,INK,4)
    for xx in range(805,1260,54): s.rect(xx,710,28,20,ORANGE,PALE_ORANGE,1)
    s.line(1015,680,1015,724,RED,2,"dashed"); s.text(1025,674,"gap",13,RED,45)
    return s


def d125() -> Scene:
    s = cscene("D12.5", "Torsion twists the surface; material at large radius matters most",
               "For a circular shaft: θ = TL/(GJ), with J = ∫r² dA.")
    panel(s,38,142,670,545,"SHAFT UNDER TORQUE")
    # Cylindrical shaft shown in perspective.
    s.ellipse(116,287,100,180,TEAL,PALE_TEAL,2)
    s.ellipse(502,287,100,180,TEAL,PALE_TEAL,2)
    s.line(166,287,552,287,TEAL,2); s.line(166,467,552,467,TEAL,2)
    s.line(166,377,552,377,GRID,1.5,"dashed")
    dot_path(s,[(166,377),(250,355),(335,324),(425,303),(552,287)],PURPLE,3)
    s.arrow(106,364,66,318,ORANGE,3); s.arrow(612,384,655,428,ORANGE,3)
    s.text(323,243,"length L",16,INK,100); s.text(172,490,"surface line rotates by θ",14,PURPLE,215)
    # Deformed small surface square and strain.
    dot_path(s,[(229,551),(356,551),(377,631),(248,631),(229,551)],BLUE,2.5)
    dot_path(s,[(229,551),(356,551),(384,618),(257,638),(229,551)],TEAL,2.1,"dashed")
    s.text(250,648,"γ ≈ Rθ/L",17,GREEN,125); s.text(285,523,"surface element",13,MUTED,130)
    panel(s,740,142,640,545,"SAME AREA · HOLLOW PUTS MATERIAL FARTHER OUT")
    # Equal-area circular sections and their polar second moments.
    s.ellipse(820,294,134,134,BLUE,PALE_BLUE,2.5)
    s.text(824,478,"solid: J/A = Rₛ²/2",16,BLUE,230)
    s.ellipse(1052,266,190,190,TEAL,PALE_TEAL,2.5)
    s.ellipse(1080,294,134,134,WHITE,WHITE,1)
    s.ellipse(1080,294,134,134,TEAL,"transparent",2)
    s.text(1038,478,"annulus: J/A = (Rₒ²+Rᵢ²)/2",15,TEAL,300)
    s.text(797,550,"Equal area: Rₛ² = Rₒ²−Rᵢ²",16,INK,270)
    s.text(797,592,"hollow: J/A exceeds solid by Rᵢ²",15,GREEN,315)
    return s


def d126() -> Scene:
    s = cscene("D12.6", "A falling mass reaches maximum extension by energy balance",
               "The dynamic extension exceeds the static mg/k point; at h=0 it is 2mg/k.")
    panel(s,42,145,720,545,"FORCE–EXTENSION GRAPH")
    x0,y0,x1,y1=115,595,690,235
    axes(s,x0,y0,x1,y1,"extension x","force")
    # F=kx and mg; use illustrative units with x_s=0.36 and Δ=0.72.
    xs, xd = .36, .72
    def gx(x): return x0+x*(x1-x0)
    def gy(f): return y0-f*(y0-y1)
    s.line(gx(0),gy(0),gx(.9),gy(.9),BLUE,3)
    s.text(580,276,"F=kx",17,BLUE,70)
    s.line(x0,gy(xs),x1,gy(xs),ORANGE,2.5,"dashed")
    s.text(127,gy(xs)-26,"mg",16,ORANGE,50)
    s.line(gx(xs),y0,gx(xs),gy(xs),PURPLE,1.8,"dashed")
    s.dot(gx(xs),gy(xs),5,PURPLE); s.text(gx(xs)-35,y0+12,"mg/k",14,PURPLE,70)
    s.line(gx(xd),y0,gx(xd),gy(xd),RED,1.8,"dashed")
    s.dot(gx(xd),gy(xd),5,RED); s.text(gx(xd)-10,y0+12,"Δ",15,RED,34)
    hatch_polygon(s,[(gx(0),gy(0)),(gx(xd),gy(xd)),(gx(xd),gy(0))],PALE_BLUE,12)
    s.text(315,424,"½kΔ²",17,BLUE,80)
    s.text(95,174,"Triangle under F=kx = stored elastic energy",15,INK,390)
    panel(s,800,145,580,545,"FALL DISTANCE × WEIGHT")
    s.rect(895,304,128,198,ORANGE,PALE_ORANGE,1.6)
    s.text(907,354,"mg",20,ORANGE,80)
    s.text(888,520,"h + Δ",16,INK,90)
    s.text(1054,323,"mg(h+Δ)",20,ORANGE,160)
    s.text(1054,371,"= ½kΔ²",20,BLUE,130)
    s.text(1054,443,"static: mg/k",16,PURPLE,140)
    s.text(1054,483,"drop from rest: Δ > mg/k",15,RED,245)
    s.line(865,587,1310,587,GRID,1.3)
    s.text(860,610,"h = 0 inset: Δ = 2mg/k",18,GREEN,270)
    return s


def d127() -> Scene:
    s = cscene("D12.7", "Bending: strain and stress change sign at the neutral axis",
               "For small curvature, ε = y/R and σ = Yy/R.")
    panel(s,38,144,800,555,"BENT BEAM SEGMENT")
    # Concentric arcs are cross-sections of fibres; neutral axis is the middle arc.
    cx,cy=360,465
    arc(s,cx,cy,245,.14,1.18,INK,5)
    arc(s,cx,cy,205,.14,1.18,BLUE,3,dash="dashed")
    arc(s,cx,cy,165,.14,1.18,TEAL,4)
    arc(s,cx,cy,125,.14,1.18,TEAL,4)
    s.text(118,248,"compressed fibres",15,BLUE,170)
    s.text(118,580,"stretched fibres",15,TEAL,170)
    s.text(458,280,"R to neutral axis",15,INK,160)
    # inward arrows in top segment, outward arrows in lower segment
    for xx in [277,351,425]:
        s.arrow(xx,318,xx+13,318,BLUE,2.2); s.arrow(xx,578,xx+20,578,TEAL,2.2)
    s.line(145,464,580,464,PURPLE,1.7,"dashed")
    s.text(154,435,"neutral axis: ε=0",15,PURPLE,160)
    s.arrow(560,464,624,464,ORANGE,2.5); s.text(592,436,"y",15,ORANGE,35)
    panel(s,890,144,470,555,"LINEAR STRESS THROUGH DEPTH")
    s.line(1020,256,1020,601,INK,2)
    s.line(1020,256,790,345,BLUE,3)
    # Signed triangular stress profile: compression is negative above, tension positive below.
    dot_path(s,[(1020,256),(790,345),(1020,430)],BLUE,2.6)
    dot_path(s,[(1020,430),(1250,516),(1020,601)],TEAL,2.6)
    s.line(990,430,1270,430,GRID,1.2,"dashed")
    s.text(800,300,"compression −",13,BLUE,140)
    s.text(1180,532,"tension +",13,TEAL,110)
    s.text(1130,410,"y=0",14,PURPLE,55)
    s.text(1048,615,"σ ∝ y",17,GREEN,80)
    return s


def d128() -> Scene:
    s = cscene("D12.8", "Cantilever bending and the I-beam's geometric advantage",
               "End load: δ = FL³/(3YI); the moment is largest at the clamp.")
    panel(s,35,145,810,560,"CANTILEVER · END LOAD F")
    # Undeformed reference and deflected beam.
    s.rect(125,260,430,34,GRID,WHITE,1.5)
    xvals=[125+i*430/50 for i in range(51)]
    pts=[(x,278+120*((x-125)/430)**2) for x in xvals]
    dot_path(s,pts,BLUE,4)
    s.rect(104,247,25,72,INK,INK,1)
    s.arrow(555,346,555,435,ORANGE,3); s.text(570,389,"F",18,ORANGE,30)
    s.text(362,431,"δ = FL³/(3YI)",18,GREEN,230)
    s.text(113,334,"deflected curve",14,BLUE,145)
    # Moment triangle beneath: M(x)=F(L-x).
    s.line(140,594,565,594,INK,1.5)
    dot_path(s,[(140,594),(140,506),(565,594)],PURPLE,2.5)
    s.text(141,610,"M=FL at clamp",14,PURPLE,150)
    s.text(474,610,"M=0",14,PURPLE,48)
    panel(s,890,145,490,560,"EQUAL AREA SECTIONS")
    # I-profile: two 140×28 flanges plus a 30×144 web; square area is matched.
    s.rect(966,310,110,110,BLUE,PALE_BLUE,2)
    s.text(974,435,"square",15,BLUE,90)
    s.rect(1155,265,140,28,TEAL,PALE_TEAL,1.5)
    s.rect(1210,293,30,144,TEAL,PALE_TEAL,1.5)
    s.rect(1155,437,140,28,TEAL,PALE_TEAL,1.5)
    s.text(1183,481,"I-section",15,TEAL,100)
    s.text(945,532,"equal area A ≈ 1.22×10⁴",14,INK,250)
    s.text(945,559,"I_I/I_square ≈ 5.4",15,GREEN,205)
    s.arrow(1052,594,1250,594,GREEN,3)
    s.text(1032,622,"same metal · about 5× stiffer",14,GREEN,290)
    return s


def d129() -> Scene:
    s = cscene("D12.9", "An asymmetric interatomic well links bonds to elasticity",
               "The local curvature Uʺ(r₀) is a bond spring; the broad asymmetry causes thermal expansion.")
    panel(s,58,142,930,585,"BOND POTENTIAL U(r)")
    x0,y0,x1,y1=142,641,930,223
    axes(s,x0,y0,x1,y1,"separation r","potential U")
    # Morse-like asymmetric well: repulsive wall, minimum, long attractive tail.
    pts=[]
    rmin,rmax=.98,2.62
    for i in range(181):
        r=rmin+(rmax-rmin)*i/180
        u=(1-math.exp(-3.2*(r-1.25)))**2-1
        xx=x0+(r-rmin)/(rmax-rmin)*(x1-x0); yy=y0-(u+1.15)/2.45*(y0-y1)
        pts.append((xx,yy))
    dot_path(s,pts,BLUE,3)
    r0=1.25
    x_min=x0+(r0-rmin)/(rmax-rmin)*(x1-x0); y_min=y0-(0+1.15)/2.45*(y0-y1)
    y_zero=y0-(1.15/2.45)*(y0-y1)
    s.dot(x_min,y_min,6,RED); s.line(x_min,y0,x_min,y_min,GRID,1.3,"dashed")
    s.line(x0,y_zero,x1,y_zero,GRID,1.1,"dashed"); s.text(x1-65,y_zero-22,"U=0",13,MUTED,45)
    s.text(x_min-28,y_min+15,"r₀",16,RED,38)
    s.arrow(x_min-75,y_zero,x_min-75,y_min,ORANGE,2); s.text(x_min-122,(y_min+y_zero)/2,"D",17,ORANGE,32)
    # Local parabolic tangent/fit near the minimum.
    parab=[(x,y_min+0.8*(x-x_min)**2/42) for x in range(int(x_min-95),int(x_min+96),5)]
    dot_path(s,parab,TEAL,2.5,"dashed")
    s.text(x_min+88,y_min+28,"slope 0; curvature Uʺ(r₀)",14,TEAL,235)
    s.text(650,290,"small-strain harmonic region",14,GREEN,210)
    s.text(706,498,"asymmetry → thermal expansion",14,PURPLE,230)
    panel(s,1020,170,345,480,"BOND SPRING")
    s.text(1052,270,"k_bond = Uʺ(r₀)",20,GREEN,250)
    s.text(1052,335,"steep repulsion\nsoft attraction",16,INK,230)
    s.text(1052,426,"Near r₀: parabolic\nenergy → Hooke law",15,TEAL,240)
    s.text(1052,520,"At higher temperature,\nthe longer-r side is\nexplored more often.",15,PURPLE,250)
    return s


def d1210() -> Scene:
    s = cscene("D12.10", "Material selection on a log–log Ashby-style map",
               "Guide-line slopes expose specific-modulus indices without ranking by density alone.")
    panel(s,45,145,910,590,"YOUNG'S MODULUS Y AGAINST DENSITY ρ · LOG–LOG")
    x0,y0,x1,y1=150,656,860,242
    axes(s,x0,y0,x1,y1,"density ρ (log)","Young's modulus Y (log)")
    for i in range(1,5):
        xx=x0+i*(x1-x0)/5; yy=y0-i*(y0-y1)/5
        s.line(xx,y0,xx,y1,GRID,0.8,"dashed"); s.line(x0,yy,x1,yy,GRID,0.8,"dashed")
    # Blobs in the usual approximate material regions.
    blobs=[(235,367,90,68,BLUE,PALE_BLUE,"foams"),
           (397,483,106,74,ORANGE,PALE_ORANGE,"polymers"),
           (590,330,112,88,TEAL,PALE_TEAL,"metals"),
           (735,275,96,80,PURPLE,"#f0ecf7","ceramics")]
    for x,y,w,h,col,fill,label in blobs:
        s.ellipse(x,y,w,h,col,fill,1.6); s.text(x+8,y+h+4,label,14,col,120)
    # approximate material points
    materials=[("rubber",222,423,RED),("steel",615,395,BLUE),("Al",570,440,ORANGE),("CFRP",706,315,GREEN)]
    for label,x,y,col in materials:
        s.dot(x,y,6,col); s.text(x+8,y-19,label,14,col,85)
    # Tie-index Y/rho: slope 1. Beam-index sqrt(Y)/rho: slope 2.
    dot_path(s,[(330,552),(760,370)],GREEN,2.5,"dashed")
    dot_path(s,[(390,603),(650,347)],PURPLE,2.5,"dashed")
    s.text(700,386,"slope 1: Y/ρ",14,GREEN,125)
    s.text(520,325,"slope 2: √Y/ρ",14,PURPLE,130)
    panel(s,990,172,370,500,"READ THE INDEX")
    s.text(1020,265,"tie: Y/ρ",20,GREEN,160)
    s.text(1020,319,"constant index → slope 1",14,INK,250)
    s.text(1020,391,"beam: √Y/ρ",20,PURPLE,200)
    s.text(1020,445,"constant index → slope 2",14,INK,250)
    s.text(1020,530,"Foams ≪ polymers < metals\nand ceramics in Y; density\nchanges the best choice.",15,MUTED,290)
    return s


def d1211() -> Scene:
    s = cscene("D12.11", "Poisson contraction accompanies longitudinal extension",
               "For a small tensile strain ε, Δr/r = −σ ε and ΔV/V = (1−2σ)ε.")
    panel(s,45,150,820,540,"WIRE BEFORE AND AFTER TENSION")
    s.rect(130,290,280,80,GRID,"transparent",2)
    s.rect(130,290,390,68,BLUE,PALE_BLUE,2)
    s.arrow(150,260,115,260,ORANGE,2.5); s.arrow(500,260,545,260,ORANGE,2.5)
    s.text(267,225,"ΔL",17,BLUE,45); s.text(130,406,"before · L",15,MUTED,105)
    s.text(342,406,"after · L+ΔL",15,BLUE,140)
    s.text(151,477,"lateral radius decreases",15,RED,220)
    panel(s,900,150,455,300,"CROSS-SECTION")
    s.ellipse(1000,230,155,155,GRID,"transparent",2)
    s.ellipse(1021,251,113,113,BLUE,PALE_BLUE,2)
    s.dot(1078,308,4,INK)
    s.arrow(1080,231,1155,231,ORANGE,1.8); s.text(1158,220,"r",14,ORANGE,24)
    s.arrow(1080,252,1135,252,BLUE,1.8); s.text(1138,245,"r+Δr",13,BLUE,60)
    s.text(952,410,"Δr = −σ r ΔL/L",17,BLUE,210)
    s.text(97,586,"Volume strain = ε + 2(−σε) = (1−2σ)ε",18,GREEN,510)
    s.text(97,631,"σ = −ε_lat/ε_long",16,INK,210)
    return s


def d1212() -> Scene:
    s = cscene("D12.12", "A hanging rod's own weight loads each section by the material below",
               "At height x from the free end, F(x)=ρAgx and dΔ=ρgx dx/Y.")
    panel(s,40,145,570,570,"HANGING ROD · x MEASURED UP FROM FREE END")
    s.line(320,230,320,635,BLUE,20)
    s.rect(255,198,130,22,INK,INK,1)
    s.text(340,252,"fixed",14,INK,55)
    # Local slice and x origin.
    s.line(264,402,376,402,RED,3); s.line(264,435,376,435,RED,3)
    s.arrow(320,635,320,663,ORANGE,2); s.text(332,637,"x=0",14,ORANGE,48)
    s.arrow(220,418,220,334,PURPLE,2); s.text(182,365,"dx",14,PURPLE,38)
    s.text(78,470,"load below = ρAgx",16,BLUE,205)
    s.text(78,510,"dΔ = ρg x dx/Y",16,GREEN,190)
    panel(s,660,145,700,570,"TENSION RISES LINEARLY TO mg")
    x0,y0,x1,y1=770,608,1280,262
    axes(s,x0,y0,x1,y1,"height x","tension F")
    s.line(x0,y0,x1,y1,BLUE,3)
    s.line(x0,y0,x1,y0,GRID,1.1,"dashed")
    s.text(1250,236,"mg",15,BLUE,42); s.text(752,620,"0",13,INK,20)
    hatch_polygon(s,[(x0,y0),(x1,y1),(x1,y0)],PALE_BLUE,14)
    s.text(930,506,"area = ∫F dx",15,GREEN,125)
    s.text(849,670,"mean load = mg/2  ⇒  ΔL = ρgL²/(2Y)",17,GREEN,370)
    return s


def d1213() -> Scene:
    s = cscene("D12.13", "Seawater density rises with depth through compressibility",
               "Linear estimate: ρ(d)/ρ₀ = 1 + ρ₀gd/B; at 4 km the increase is about 1.8%.")
    panel(s,48,145,930,590,"SEAWATER · ρ₀ ≈ 1025 kg m⁻³, B = 2.2 GPa")
    x0,y0,x1,y1=170,655,880,252
    axes(s,x0,y0,x1,y1,"depth d (km)","ρ/ρ₀")
    # map d=0..10 km, rho/rho0=1..1.05
    def xy(d: float, ratio: float) -> tuple[float,float]:
        return x0+d/10*(x1-x0), y0-(ratio-1)/.05*(y0-y1)
    s.line(x0,y0,x1,y0,GRID,1,"dashed")
    for km in [2,4,6,8,10]:
        xx=x0+km/10*(x1-x0); s.line(xx,y0,xx,y1,GRID,0.9,"dashed")
        s.text(xx-10,y0+9,str(km),12,MUTED,25)
    rho0,g,B=1025,9.8,2.2e9
    linear=[]
    for i in range(101):
        d=10000*i/100
        ratio=1+rho0*g*d/B
        linear.append(xy(d/1000,ratio))
    dot_path(s,linear,BLUE,3)
    nonlinear=[]
    for i in range(101):
        d=10000*i/100
        # illustrative mild upward curvature to flag breakdown of the constant-B approximation
        ratio=(1-rho0*g*d/B)**-1
        nonlinear.append(xy(d/1000,ratio))
    dot_path(s,nonlinear,ORANGE,2.4,"dashed")
    d4=1+rho0*g*4000/B; px,py=xy(4,d4)
    s.dot(px,py,6,RED); s.text(px+10,py-30,"4 km: +1.8%",15,RED,125)
    s.text(705,289,"linear B approximation",14,BLUE,180)
    s.text(684,338,"dashed: correction when B varies",13,ORANGE,230)
    s.text(203,674,"0 km",13,INK,50); s.text(827,674,"10 km",13,INK,60)
    return s


def d1214() -> Scene:
    s = cscene("D12.14", "Thin-cylinder pressure creates hoop and longitudinal stress",
               "A diametral cut gives σθ=pr/t; an end-cap cut gives σL=pr/(2t).")
    panel(s,40,145,650,570,"LONGITUDINAL CUT · HOOP STRESS")
    # Half-cylinder free body and cut rectangle.
    s.ellipse(130,270,115,190,BLUE,PALE_BLUE,2)
    s.line(187,270,520,270,BLUE,2); s.line(187,460,520,460,BLUE,2)
    s.ellipse(520,270,115,190,BLUE,PALE_BLUE,2)
    s.line(187,270,520,270,GRID,1,"dashed"); s.line(187,460,520,460,GRID,1,"dashed")
    s.text(250,235,"cylinder length L",15,INK,160)
    # Pressure arrows on projected rectangle push outward; wall tension resists.
    for xx in [260,330,400,470]: s.arrow(xx,347,xx,293,ORANGE,1.8)
    s.text(250,304,"p on projected area 2rL",14,ORANGE,200)
    s.arrow(230,265,230,225,TEAL,2.4); s.arrow(482,265,482,225,TEAL,2.4)
    s.text(305,492,"two cut walls: σθ tL each",15,TEAL,230)
    s.text(222,549,"p(2rL)=2σθtL  ⇒  σθ=pr/t",18,GREEN,350)
    s.text(238,594,"lengthwise crack follows the generator",14,RED,260)
    panel(s,730,145,650,570,"END-CAP CUT · LONGITUDINAL STRESS")
    s.ellipse(855,242,350,160,BLUE,PALE_BLUE,2.5)
    s.ellipse(855,242,350,160,TEAL,"transparent",1.2)
    s.text(940,204,"closed end cap",15,INK,150)
    # Pressure resultant on cap, balanced by hoop ring cross section.
    s.arrow(1028,266,1028,214,ORANGE,2.7); s.arrow(1028,374,1028,426,ORANGE,2.7)
    s.text(1125,300,"pπr²",16,ORANGE,75)
    s.ellipse(935,467,170,135,TEAL,PALE_TEAL,2)
    s.ellipse(970,493,100,83,WHITE,WHITE,1)
    s.ellipse(970,493,100,83,TEAL,"transparent",2)
    s.text(1120,505,"ring area = 2πrt",14,TEAL,150)
    s.text(770,625,"pπr²=σL(2πrt)  ⇒  σL=pr/(2t)",18,GREEN,380)
    return s


# ── ELECTROSTATICS · plan Parts 13–15 consolidated in the D13 master ──────────

def d131() -> Scene:
    s = cscene("D13.1", "Three ways to charge a body: electrons move",
               "Friction transfers, contact shares, induction separates and grounds charge.")
    # Three clearly separated rows.
    rows=[150,360,575]
    labels=["FRICTION", "CONDUCTION", "INDUCTION"]
    for y,lbl in zip(rows,labels):
        s.text(34,y+37,lbl,14,PURPLE,102)
        s.line(144,y+98,1380,y+98,GRID,1)
    # Friction: cloth electron transfer to rod.
    s.text(174,rows[0],"before",13,MUTED,50); s.text(596,rows[0],"after",13,MUTED,40)
    s.rect(226,rows[0]+32,145,38,BLUE,PALE_BLUE,2); s.text(252,rows[0]+38,"rod",15,BLUE,45)
    s.ellipse(416,rows[0]+22,150,58,ORANGE,PALE_ORANGE,2); s.text(459,rows[0]+39,"cloth",15,ORANGE,55)
    s.arrow(440,rows[0]+4,345,rows[0]+4,RED,2.6); s.text(366,rows[0]-3,"e⁻",14,RED,30)
    s.rect(620,rows[0]+32,145,38,BLUE,PALE_BLUE,2); s.text(675,rows[0]+38,"−",19,BLUE,20)
    s.ellipse(812,rows[0]+22,150,58,ORANGE,PALE_ORANGE,2); s.text(875,rows[0]+39,"+",19,ORANGE,20)
    s.text(1018,rows[0]+34,"cloth → rod: e⁻",15,INK,180)
    # Conduction: negative sphere touches neutral sphere; electrons spread.
    s.text(174,rows[1],"contact",13,MUTED,55)
    s.ellipse(255,rows[1]+24,88,88,BLUE,PALE_BLUE,2); s.text(282,rows[1]+55,"−",22,BLUE,28)
    s.ellipse(470,rows[1]+24,88,88,TEAL,PALE_TEAL,2); s.text(498,rows[1]+55,"0",18,TEAL,24)
    s.arrow(340,rows[1]+70,454,rows[1]+70,RED,2.6); s.text(377,rows[1]+42,"e⁻ flow",14,RED,75)
    s.ellipse(700,rows[1]+24,88,88,BLUE,PALE_BLUE,2); s.ellipse(914,rows[1]+24,88,88,BLUE,PALE_BLUE,2)
    for xx,yy in [(725,rows[1]+52),(757,rows[1]+80),(938,rows[1]+53),(973,rows[1]+83)]: s.text(xx,yy,"−",14,BLUE,20)
    s.text(1040,rows[1]+50,"same sign on both",15,INK,190)
    # Induction sequence: polarization, earth connection, remove earth, remove rod.
    centers=[265,505,755,1045]
    stages=["1 · polarize","2 · ground","3 · disconnect earth","4 · remove rod"]
    for cx,stage in zip(centers,stages):
        s.text(cx-62,rows[2],stage,13,MUTED,150)
    # negative rod at left for the first two stages
    s.rect(183,rows[2]+42,36,64,RED,PALE_RED,1.5); s.text(187,rows[2]+62,"−",17,RED,20)
    for j,cx in enumerate(centers):
        s.ellipse(cx-28,rows[2]+40,82,70,TEAL,PALE_TEAL,2)
        if j < 3:
            for yy in [rows[2]+55,rows[2]+78]: s.text(cx-21,yy,"+",13,RED,18)
            for yy in [rows[2]+55,rows[2]+78]: s.text(cx+25,yy,"−",13,BLUE,18)
        else:
            for xx,yy in [(cx-11,rows[2]+54),(cx+21,rows[2]+81)]: s.text(xx,yy,"+",14,RED,18)
    # Earth path and electron drain in stage 2; rod absent at last stage.
    s.line(505,rows[2]+109,505,rows[2]+125,INK,2); s.line(480,rows[2]+125,530,rows[2]+125,INK,2)
    s.arrow(533,rows[2]+87,573,rows[2]+87,RED,2); s.text(574,rows[2]+69,"e⁻ to earth",12,RED,80)
    s.text(1138,rows[2]+60,"final sphere: +",14,GREEN,150)
    return s


def d132() -> Scene:
    s = cscene("D13.2", "Coulomb's law is a vector law on a pair",
               "r₁₂ = r₂−r₁ points from charge 1 to 2; the action–reaction forces match.")
    for x,head,sign1,sign2,col in [(42,"LIKE CHARGES · REPEL","+q₁","+q₂",BLUE),
                                    (722,"UNLIKE CHARGES · ATTRACT","+q₁","−q₂",RED)]:
        panel(s,x,150,650,525,head)
        p1=(x+190,410); p2=(x+440,410)
        charge(s,*p1,sign1,col,22); charge(s,*p2,sign2,ORANGE if sign2[0]=='−' else col,22)
        s.arrow(p1[0],p1[1],p2[0],p2[1],PURPLE,1.8,"arrow",None)
        s.text(x+275,373,"r₁₂ = r₂ − r₁",14,PURPLE,170)
        # Force on 2 and on 1 are equal and opposite for each sign pair.
        if sign2[0]=="+":
            vec(s,p1,(p1[0]-105,p1[1]),"F₂₁",ORANGE,2.8,-8,-25)
            vec(s,p2,(p2[0]+105,p2[1]),"F₁₂",BLUE,2.8,4,-25)
        else:
            vec(s,p1,(p1[0]+92,p1[1]),"F₂₁",ORANGE,2.8,0,-25)
            vec(s,p2,(p2[0]-92,p2[1]),"F₁₂",BLUE,2.8,-55,-25)
        s.text(x+116,548,"|F₁₂| = |F₂₁| = k|q₁q₂|/r²",17,GREEN,390)
        s.text(x+116,593,"F₁₂ = kq₁q₂ r̂₁₂/r²",17,INK,335)
    return s


def d133() -> Scene:
    s = cscene("D13.3", "Coulomb's torsion balance measures a tiny force",
               "At equilibrium κθ = Fℓ; doubling separation reduces the angle to one quarter.")
    panel(s,48,145,905,555,"TOP VIEW · FIBRE SUSPENDED HORIZONTAL ROD")
    # fibre and rod
    s.line(480,240,480,338,INK,3); s.ellipse(470,229,20,20,INK,INK,1)
    s.line(250,350,710,350,BLUE,6)
    s.ellipse(222,322,56,56,TEAL,PALE_TEAL,2); s.text(240,340,"q",16,TEAL,20)
    s.ellipse(682,322,56,56,GRID,WHITE,2); s.text(701,341,"cw",12,MUTED,40)
    # fixed charge beside the pith ball and force
    s.ellipse(176,411,54,54,ORANGE,PALE_ORANGE,2); s.text(192,428,"Q",16,ORANGE,22)
    s.arrow(225,345,258,340,PURPLE,2.5); s.text(255,304,"F",17,PURPLE,24)
    arc(s,480,350,76,math.pi,math.pi+.42,RED,2.5); s.text(395,390,"θ",17,RED,30)
    s.arrow(465,236,495,236,INK,1.5); s.text(503,225,"fibre · κ",14,INK,90)
    s.text(310,491,"torque: κθ = Fℓ",19,GREEN,210)
    s.text(310,535,"F ∝ 1/r²  ⇒  θ ∝ 1/r²",16,INK,245)
    panel(s,1000,170,365,470,"INVERSE-SQUARE TEST")
    s.text(1035,265,"r → 2r",21,BLUE,120)
    s.arrow(1085,315,1260,315,BLUE,2.4); s.text(1120,330,"separation",14,MUTED,120)
    s.text(1035,406,"F → F/4",21,ORANGE,140)
    s.text(1035,478,"θ → θ/4",21,RED,140)
    s.text(1035,550,"Measure twist; infer\nthe electrostatic force.",15,MUTED,250)
    return s


def d134() -> Scene:
    s = cscene("D13.4", "Field-line patterns encode source, sign and symmetry",
               "Lines leave positive charge, enter negative charge, and crowd where |E| is large.")
    cards=[(36,140,"(a) + POINT CHARGE"),(727,140,"(b) DIPOLE"),
           (36,450,"(c) TWO + CHARGES"),(727,450,"(d) UNIFORM SHEET")]
    for x,y,h in cards: panel(s,x,y,650,275,h)
    # positive point: evenly spaced rays.
    cx,cy=360,285; charge(s,cx,cy,"+",BLUE,16)
    for a in [i*math.pi/4 for i in range(8)]:
        s.arrow(cx+24*math.cos(a),cy+24*math.sin(a),cx+115*math.cos(a),cy+115*math.sin(a),BLUE,1.8)
    # dipole field: two charges, symmetric representative curves from + to -.
    cx,cy=1050,285; charge(s,cx-80,cy,"+",BLUE,15); charge(s,cx+80,cy,"−",RED,15)
    for h in [-85,-50,50,85]:
        # cubic Bezier-like curves bowed around and into the negative charge
        pts=[]
        for i in range(31):
            t=i/30
            x=cx-65+130*t
            y=cy+h*math.sin(math.pi*t)*(1 if h>0 else 1)
            pts.append((x,y))
        dot_path(s,pts,TEAL,1.6)
    s.arrow(cx-7,cy,cx+7,cy,TEAL,2)
    # two like charges: outward lines bend away; mark midpoint null.
    cx,cy=360,592; c1=(cx-72,cy); c2=(cx+72,cy)
    charge(s,*c1,"+",BLUE,15); charge(s,*c2,"+",BLUE,15)
    for yoff in [-78,-46,46,78]:
        side=1 if yoff>0 else -1
        dot_path(s,[(c1[0]-8,cy+yoff*.2),(cx-125,cy+yoff*.8),(cx-150,cy+yoff*1.25)],BLUE,1.7)
        dot_path(s,[(c2[0]+8,cy+yoff*.2),(cx+125,cy+yoff*.8),(cx+150,cy+yoff*1.25)],BLUE,1.7)
    s.line(cx,cy-105,cx,cy+105,GRID,1,"dashed"); s.text(cx-19,cy-11,"×",21,RED,28)
    s.text(cx-52,cy+98,"E=0 midway",12,RED,100)
    # Uniform sheet: arrows perpendicular on both sides.
    cx,cy=1050,592; s.line(cx,cy-95,cx,cy+95,ORANGE,5)
    for yy in [cy-70,cy-25,cy+25,cy+70]:
        s.arrow(cx-24,yy,cx-132,yy,ORANGE,2); s.arrow(cx+24,yy,cx+132,yy,ORANGE,2)
    s.text(cx-48,cy-118,"+ charged sheet",14,ORANGE,125)
    return s


def d135() -> Scene:
    s = cscene("D13.5", "Ring symmetry cancels transverse field components",
               "Opposite elements add along the axis: dEₓ = k dq x/(x²+R²)^(3/2).")
    # perspective ring as ellipse
    s.ellipse(160,260,390,165,BLUE,"transparent",2.6)
    s.line(355,342,890,342,INK,2,"dashed")
    s.dot(355,342,5,INK); s.text(332,357,"O",14,INK,24)
    s.dot(890,342,7,RED); s.text(900,325,"P",17,RED,30); s.text(625,356,"axis x",15,INK,80)
    # opposite charge elements and vectors to P
    qtop=(355,260); qbot=(355,425)
    s.dot(*qtop,6,ORANGE); s.dot(*qbot,6,ORANGE)
    s.text(226,232,"dq",14,ORANGE,34); s.text(225,423,"dq",14,ORANGE,34)
    s.line(*qtop,890,342,GRID,1.3); s.line(*qbot,890,342,GRID,1.3)
    vec(s,(808,311),(866,326),"dE(top)",BLUE,2,4,-25,14)
    vec(s,(808,373),(866,358),"dE(bottom)",BLUE,2,4,4,14)
    s.text(611,264,"s = √(x²+R²)",15,PURPLE,165)
    s.arrow(806,325,854,325,TEAL,1.8); s.arrow(806,359,854,359,TEAL,1.8)
    s.arrow(854,326,854,342,RED,1.7); s.arrow(854,358,854,342,RED,1.7)
    s.text(747,393,"dE⊥ cancels",14,RED,125); s.text(819,300,"dEₓ adds",14,GREEN,100)
    panel(s,1010,178,360,475,"SYMMETRY PAIR")
    s.text(1040,268,"E⊥ = 0",22,RED,130)
    s.text(1040,332,"Eₓ = kQx/s³",20,GREEN,190)
    s.text(1040,399,"s = √(x²+R²)",17,INK,180)
    s.text(1040,482,"The ring is not a point\nunless x ≫ R.",15,MUTED,220)
    s.ellipse(1087,550,105,50,BLUE,"transparent",1.8)
    s.text(1098,613,"axis view",12,MUTED,75)
    return s


def d136() -> Scene:
    s = cscene("D13.6", "A finite charged rod contributes perpendicular and parallel field",
               "Resolve each dq field at P; the parallel component points toward the smaller-angle end.")
    panel(s,42,145,790,555,"FINITE UNIFORM ROD")
    yrod=520; xL=145; xR=660; P=(395,245)
    s.line(xL,yrod,xR,yrod,BLUE,7); s.dot(*P,7,RED); s.text(P[0]-8,P[1]-27,"P",17,RED,25)
    s.line(P[0],P[1]+7,P[0],yrod,GRID,1.5,"dashed"); s.text(P[0]+8,370,"d",15,GRID,28)
    # element and endpoint rays
    el=(480,yrod); s.dot(*el,6,ORANGE); s.text(el[0]+8,el[1]-12,"dl",14,ORANGE,35)
    s.line(*P,xL,yrod,MUTED,1.7); s.line(*P,xR,yrod,MUTED,1.7); s.line(*P,*el,PURPLE,2)
    # Angles from the downward perpendicular: left β=42° < right α=44°.
    beta=math.atan2(P[0]-xL,yrod-P[1]); alpha=math.atan2(xR-P[0],yrod-P[1])
    arc(s,P[0],P[1],70,-math.pi/2,-math.pi/2-beta,TEAL,1.8)
    arc(s,P[0],P[1],70,-math.pi/2+alpha,-math.pi/2,PURPLE,1.8)
    s.text(P[0]-52,P[1]+48,"β",16,TEAL,25); s.text(P[0]+28,P[1]+49,"α",16,PURPLE,25)
    # Element distance and angle θ measured from the perpendicular.
    theta=math.atan2(el[0]-P[0],yrod-P[1])
    arc(s,P[0],P[1],42,-math.pi/2,-math.pi/2+theta,ORANGE,1.5)
    s.text(P[0]+16,P[1]+34,"θ",14,ORANGE,22); s.text(438,374,"s",14,PURPLE,22)
    # For the longer right-hand span, the smaller-angle left end sets E∥ to the left.
    s.arrow(P[0],P[1],P[0],P[1]-82,BLUE,2.8); s.text(P[0]+10,P[1]-78,"E⊥",16,BLUE,50)
    s.arrow(P[0],P[1],P[0]-110,P[1],GREEN,2.8); s.text(P[0]-100,P[1]+8,"E∥",16,GREEN,45)
    s.arrow(P[0],P[1],P[0]-70,P[1]-83,ORANGE,2.8); s.text(P[0]-105,P[1]-93,"E",17,ORANGE,30)
    s.text(102,608,"β < α ⇒ E∥ toward the left (smaller-angle end)",15,GREEN,480)
    panel(s,880,185,470,425,"GEOMETRY FOR dq")
    s.text(920,278,"s² = d² + ℓ²",20,INK,210)
    s.text(920,345,"dE = kλ dℓ/s²",18,BLUE,210)
    s.text(920,412,"resolve dE into E⊥, E∥",16,TEAL,240)
    s.text(920,500,"Do not replace the rod\nby a point charge unless\nthe far-field limit applies.",15,MUTED,330)
    return s


def d137() -> Scene:
    s = cscene("D13.7", "Build a uniformly charged disc from concentric rings",
               "Each ring contributes on-axis field; the disc tends to σ/(2ε₀) at x=0 and kQ/x² far away.")
    panel(s,32,140,410,570,"TOP VIEW · ANNULAR ELEMENT")
    s.ellipse(100,255,260,260,BLUE,PALE_BLUE,2)
    s.ellipse(155,310,150,150,WHITE,WHITE,1)
    s.ellipse(145,300,170,170,TEAL,"transparent",2.5)
    s.ellipse(155,310,150,150,BLUE,"transparent",1.4)
    s.arrow(230,390,350,390,ORANGE,2); s.text(272,365,"r",16,ORANGE,30)
    s.arrow(322,341,337,330,RED,2); s.text(337,309,"dr",14,RED,35)
    s.text(116,539,"dQ = σ(2πr dr)",16,GREEN,205)
    panel(s,468,140,425,570,"SIDE VIEW · ON-AXIS FIELD")
    s.ellipse(525,330,280,100,BLUE,"transparent",2)
    s.line(665,295,665,560,INK,1.6,"dashed"); s.dot(665,330,5,ORANGE)
    s.dot(665,520,7,RED); s.text(676,505,"P(x)",15,RED,65)
    s.arrow(665,365,665,486,BLUE,2.4); s.text(678,405,"dEₓ",14,BLUE,50)
    s.text(526,578,"Eₓ = (σ/2ε₀)[1 − x/√(x²+R²)]",14,GREEN,340)
    panel(s,920,140,450,570,"Eₓ AGAINST DISTANCE")
    x0,y0,x1,y1=1000,603,1320,262
    axes(s,x0,y0,x1,y1,"x/R","E/E(0)")
    pts=[]
    for i in range(101):
        q=4*i/100; pts.append((x0+q/4*(x1-x0),y0-(1-q/math.sqrt(1+q*q))*(y0-y1)))
    dot_path(s,pts,BLUE,2.8)
    s.text(1003,245,"1",13,INK,15); s.text(1232,545,"∝1/x²",14,ORANGE,65)
    s.text(975,634,"σ/(2ε₀) at x=0",13,GREEN,145)
    return s


def d138() -> Scene:
    s = cscene("D13.8", "Two infinite sheets: superpose their fields region by region",
               "Each sheet contributes σ/(2ε₀); direction changes across the sheet.")
    for x,title,signs,vals in [(38,"+σ AND −σ",("+σ","−σ"),("0","σ/ε₀","0")),
                               (722,"+σ AND +σ",("+σ","+σ"),("σ/ε₀","0","σ/ε₀"))]:
        panel(s,x,145,655,555,title)
        sx1,sx2=x+250,x+385
        s.line(sx1,250,sx1,590,ORANGE,5); s.line(sx2,250,sx2,590,BLUE,5)
        s.text(sx1-35,217,signs[0],15,ORANGE,60); s.text(sx2-35,217,signs[1],15,BLUE,60)
        # sample arrows from each sheet in left, middle, right regions
        sample=[x+140,(sx1+sx2)/2,x+540]
        for idx,xx in enumerate(sample):
            if signs[0]=="+σ": d1=-1 if xx<sx1 else 1
            else: d1=1 if xx<sx1 else -1
            if signs[1]=="+σ": d2=-1 if xx<sx2 else 1
            else: d2=1 if xx<sx2 else -1
            for yy in [312,386,460]:
                s.arrow(xx,yy,xx+d1*38,yy,ORANGE,1.8)
                s.arrow(xx,yy+25,xx+d2*38,yy+25,BLUE,1.8)
            s.text(xx-34,514,"sum →",13,INK,60)
            s.text(xx-32,545,vals[idx],17,GREEN,75)
        s.text(x+28,615,"orange = field of left sheet; blue = field of right sheet",12,MUTED,430)
    return s


def d139() -> Scene:
    s = cscene("D13.9", "A symmetric arc's transverse field cancels at its centre",
               "For positive λ, E = (2kλ/R) sin(θ₀/2) along the bisector, away from the arc.")
    panel(s,38,145,800,550,"ARC OF ANGLE θ₀")
    O=(410,485); R=205; a0=math.radians(55); a1=math.pi-a0
    arc(s,O[0],O[1],R,a0,a1,BLUE,4)
    s.dot(*O,7,INK); s.text(O[0]-17,O[1]+18,"O",15,INK,22)
    # symmetric elements at ±φ around the vertical bisector
    phi=math.radians(24)
    top=(O[0]+R*math.cos(math.pi/2-phi),O[1]-R*math.sin(math.pi/2-phi))
    bot=(O[0]+R*math.cos(math.pi/2+phi),O[1]-R*math.sin(math.pi/2+phi))
    s.dot(*top,6,ORANGE); s.dot(*bot,6,ORANGE)
    s.line(*O,*top,GRID,1.4); s.line(*O,*bot,GRID,1.4)
    # At O the paired fields point down-left and down-right: horizontal parts cancel.
    s.arrow(O[0],O[1],O[0]-82,O[1]+48,TEAL,2.4)
    s.arrow(O[0],O[1],O[0]+82,O[1]+48,TEAL,2.4)
    s.text(O[0]-120,O[1]+38,"dE",14,TEAL,35); s.text(O[0]+85,O[1]+38,"dE",14,TEAL,35)
    s.arrow(O[0]-18,O[1]+72,O[0]-64,O[1]+72,RED,1.7)
    s.arrow(O[0]+18,O[1]+72,O[0]+64,O[1]+72,RED,1.7)
    s.text(O[0]-200,O[1]+125,"transverse parts cancel",13,RED,200)
    s.arrow(O[0],O[1]+12,O[0],O[1]+102,GREEN,2.5); s.text(O[0]+12,O[1]+72,"resultant",14,GREEN,90)
    # chord of arc endpoints
    A=(O[0]+R*math.cos(a0),O[1]-R*math.sin(a0)); B=(O[0]+R*math.cos(a1),O[1]-R*math.sin(a1))
    s.line(*A,*B,PURPLE,1.8,"dashed"); s.text(378,318,"chord = 2R sin(θ₀/2)",13,PURPLE,220)
    panel(s,880,180,485,465,"SEMICIRCLE")
    arc(s,1122,353,112,0,math.pi,BLUE,2.8)
    s.line(1010,353,1234,353,GRID,1.3,"dashed")
    s.dot(1122,353,4,INK)
    s.arrow(1122,353,1122,463,GREEN,2.8); s.text(1135,407,"E=2kλ/R",17,GREEN,135)
    s.text(925,521,"For a semicircle θ₀=π,\nsin(θ₀/2)=1.",16,INK,240)
    return s


def d1310() -> Scene:
    s = cscene("D13.10", "A conductor's surface field is twice the local patch field",
               "The patch and the rest cancel inside; they add to σ/ε₀ just outside.")
    panel(s,52,155,1280,535,"MAGNIFIED POSITIVE SURFACE PATCH")
    # conductor to left; patch is vertical boundary
    s.rect(250,270,300,240,PALE_TEAL,TEAL,2)
    s.line(550,270,550,510,ORANGE,6)
    s.text(323,390,"conductor",18,TEAL,130)
    s.text(523,232,"surface charge σ",14,ORANGE,150)
    # On the inside: local field points left, rest field right, equal magnitude.
    vec(s,(385,325),(290,325),"E_patch=σ/2ε₀",RED,2.5,-65,-25,14)
    vec(s,(385,390),(480,390),"E_rest=σ/2ε₀",BLUE,2.5,6,-25,14)
    s.text(318,445,"inside sum = 0",17,GREEN,150)
    # On the outside both components point right.
    vec(s,(718,325),(820,325),"E_patch",RED,2.5,4,-24,14)
    vec(s,(718,390),(820,390),"E_rest",BLUE,2.5,4,-24,14)
    vec(s,(718,474),(950,474),"E_out=σ/ε₀",GREEN,3,6,-25,16)
    s.text(1030,325,"patch's sheet field",14,RED,170)
    s.text(1030,390,"rest of conductor",14,BLUE,170)
    s.text(1030,475,"outside total",14,GREEN,125)
    return s


def d1311() -> Scene:
    s = cscene("D13.11", "A uniform field torques a dipole but does not translate it",
               "τ = pE sinθ; U(θ)=−pE cosθ has a stable minimum at 0 and unstable maximum at π.")
    panel(s,35,150,790,555,"DIPOLE IN UNIFORM E")
    for yy in [260,340,420,500,580]: s.arrow(88,yy,300,yy,GRID,1.4)
    p1=(348,467); p2=(470,347)
    charge(s,*p1,"−q",RED,20); charge(s,*p2,"+q",BLUE,20)
    s.line(*p1,*p2,PURPLE,2.5); s.text(390,390,"p",18,PURPLE,25)
    vec(s,p2,(p2[0]+110,p2[1]),"+qE",BLUE,2.8,4,-22)
    vec(s,p1,(p1[0]-110,p1[1]),"−qE",RED,2.8,-55,-22)
    s.arrow(p2[0]+28,p2[1],p2[0]+28,p1[1],TEAL,1.5); s.text(p2[0]+35,(p2[1]+p1[1])/2-8,"d sinθ",13,TEAL,75)
    arc(s,348,467,70,0,math.atan2(120,122),ORANGE,1.8); s.text(405,439,"θ",16,ORANGE,25)
    s.text(109,610,"net force = 0; opposite forces make a couple",15,GREEN,420)
    panel(s,870,150,495,555,"ORIENTATION ENERGY")
    x0,y0,x1,y1=960,581,1300,273
    axes(s,x0,y0,x1,y1,"θ","U")
    pts=[]
    for i in range(101):
        th=math.pi*i/100; pts.append((x0+th/math.pi*(x1-x0),y0-((1-math.cos(th))/2)*(y0-y1)))
    # shift curve to represent -cos: minimum at θ=0, maximum at π
    pts=[(x,y0-(.5-.5*math.cos(math.pi*(x-x0)/(x1-x0)))*(y0-y1)) for x,y in pts]
    dot_path(s,pts,BLUE,2.8)
    s.dot(x0,y0,5,GREEN); s.dot(x1,y1,5,RED)
    s.text(x0+8,y0+9,"0 stable",13,GREEN,90); s.text(x1-75,y1-24,"π unstable",13,RED,100)
    s.text(1010,232,"U = −pE cosθ",16,INK,175)
    return s


def d1312() -> Scene:
    s = cscene("D13.12", "A dipole feels a net force toward stronger field",
               "The +q force is larger on the strong-field side; neutral paper polarizes in the same gradient.")
    panel(s,40,150,845,555,"ALIGNED DIPOLE IN A FIELD GRADIENT")
    # Field lines converge to the right, showing increasing field strength.
    for yy in [245,310,375,440,505,570]:
        dot_path(s,[(105,yy),(360,yy),(550,yy+8),(700,yy+20)],GRID,1.3)
        s.arrow(115,yy,260,yy,GRID,1.3)
        s.arrow(460,yy+4,565,yy+12,GRID,1.5)
        s.arrow(665,yy+16,725,yy+21,GRID,1.7)
    charge(s,410,395,"−q",RED,20); charge(s,535,395,"+q",BLUE,20)
    s.line(430,395,515,395,PURPLE,2); s.text(466,364,"p →",15,PURPLE,60)
    vec(s,(535,395),(690,395),"F₊=qE₊",BLUE,2.7,4,-26,14)
    vec(s,(410,395),(350,395),"F₋=qE₋",RED,2.3,-68,-26,14)
    s.arrow(438,480,660,480,GREEN,3); s.text(480,492,"net force → stronger E",15,GREEN,190)
    panel(s,930,175,440,475,"INDUCED DIPOLE · COMB + PAPER")
    s.rect(1000,288,38,145,INK,INK,1)
    for yy in [305,345,385,425]: s.text(1004,yy,"−",13,WHITE,22)
    s.text(978,255,"negatively charged comb",13,INK,200)
    s.rect(1153,315,130,78,PALE_ORANGE,ORANGE,1.8,True)
    for yy in [329,357,379]:
        s.text(1163,yy,"+",13,RED,18); s.text(1257,yy,"−",13,BLUE,18)
    s.arrow(1044,355,1135,355,ORANGE,2.4); s.text(1070,325,"attraction",13,ORANGE,82)
    s.text(1000,486,"near induced + is attracted\nmore strongly than far induced −",15,MUTED,340)
    return s


def d1313() -> Scene:
    s = cscene("D13.13", "Three-charge equilibrium depends on geometry and sign",
               "The zero-field point for like charges lies between them, nearer the smaller charge.")
    panel(s,30,140,440,570,"(a) COLLINEAR CHARGES")
    s.line(90,340,410,340,INK,1.5)
    charge(s,145,340,"+q₁",BLUE,19); charge(s,345,340,"+q₂",TEAL,19)
    s.dot(207,340,6,RED); s.text(182,296,"E=0",14,RED,55)
    s.text(120,390,"nearer smaller |q|",13,MUTED,155)
    s.line(90,540,410,540,INK,1.5)
    charge(s,245,540,"+q",BLUE,19); charge(s,335,540,"−4q",RED,19)
    s.dot(155,540,6,ORANGE); s.text(113,495,"outside zero",13,ORANGE,100)
    s.text(75,612,"opposite signs: zero beyond smaller |q|",12,MUTED,330)
    panel(s,495,140,430,570,"(b) SQUARE · ONE CORNER CHARGE")
    a=230; cx,cy=710,405
    corners=[(cx-a/2,cy-a/2),(cx+a/2,cy-a/2),(cx+a/2,cy+a/2),(cx-a/2,cy+a/2)]
    for px,py in corners: charge(s,px,py,"+q",BLUE,15)
    charge(s,cx,cy,"Q",RED,17)
    p=corners[0]
    vec(s,p,(p[0]-73,p[1]),"F₁",ORANGE,2.2,-18,-23,12)
    vec(s,p,(p[0],p[1]-73),"F₂",ORANGE,2.2,6,-20,12)
    vec(s,p,(p[0]-55,p[1]-55),"F₃",ORANGE,2.2,-32,-24,12)
    vec(s,p,(p[0]+45,p[1]+45),"F_Q inward",GREEN,2.5,4,40,12)
    s.text(535,594,"choose Q<0 to balance outward corner repulsion",12,MUTED,345)
    s.text(568,623,"Q = −(1/√2 + 1/4)q",13,GREEN,210)
    panel(s,950,140,430,570,"(c) EQUILATERAL TRIANGLE")
    A=(1165,270); B=(1050,545); C=(1280,545); Gc=(1165,453)
    dot_path(s,[A,B,C,A],BLUE,2.5)
    for px,py in [A,B,C]: charge(s,px,py,"+q",BLUE,17)
    charge(s,*Gc,"Q",RED,17)
    s.line(A[0],A[1],Gc[0],Gc[1],PURPLE,1.5,"dashed")
    s.text(1005,594,"Q = −q/√3",14,GREEN,150)
    s.text(1010,616,"centroid is equidistant from all vertices",12,MUTED,320)
    return s


def d1314() -> Scene:
    s = cscene("D13.14", "Electric fields deflect both a pendulum and an electron",
               "A uniform field adds a constant force; the electron exits with a tangent velocity.")
    panel(s,32,145,630,560,"CHARGED PENDULUM · HORIZONTAL E")
    # Uniform horizontal field lines and pivot/bob.
    for yy in [245,305,365,425,485]: s.arrow(72,yy,220,yy,GRID,1.3)
    pivot=(350,230); bob=(453,430)
    s.dot(*pivot,6,INK); s.line(*pivot,*bob,INK,2.5); charge(s,*bob,"+q",BLUE,20)
    vec(s,bob,(bob[0],bob[1]+110),"mg",RED,2.5,7,75,14)
    vec(s,bob,(bob[0]+108,bob[1]),"qE",ORANGE,2.5,7,-25,14)
    vec(s,bob,(bob[0]-60,bob[1]-113),"T",PURPLE,2.5,-35,-24,14)
    s.line(pivot[0],pivot[1]+45,pivot[0],pivot[1]+112,GRID,1.3,"dashed")
    arc(s,pivot[0],pivot[1],80,-math.pi/2,math.atan2(pivot[1]-bob[1],bob[0]-pivot[0]),TEAL,1.8)
    s.text(375,317,"θ₀",15,TEAL,35)
    s.arrow(bob[0]+28,bob[1]+18,bob[0]+93,bob[1]+84,GRID,1.8); s.text(529,525,"g_eff",13,MUTED,68)
    s.text(86,579,"tan θ₀ = qE/mg",17,GREEN,180)
    panel(s,690,145,690,560,"ELECTRON BETWEEN DEFLECTING PLATES")
    s.rect(770,255,395,18,RED,PALE_RED,1.4); s.rect(770,427,395,18,BLUE,PALE_BLUE,1.4)
    s.text(778,220,"+ plate",14,RED,75); s.text(778,457,"− plate",14,BLUE,70)
    for xx in [820,910,1000,1090]: s.arrow(xx,283,xx,410,GRID,1.2)
    # electron bends upward between plates then continues tangent to screen.
    s.dot(790,342,7,INK); s.text(774,319,"e⁻",13,INK,30)
    pts=[]
    for i in range(41):
        t=i/40; pts.append((790+320*t,342-82*t*t))
    dot_path(s,pts,BLUE,3)
    exitp=pts[-1]; s.arrow(exitp[0],exitp[1],1250,180,ORANGE,2.7)
    s.line(1110,260,1250,180,PURPLE,1.5,"dashed"); s.text(1115,222,"back-extrapolated",12,PURPLE,120)
    s.line(1260,170,1260,510,INK,3); s.arrow(1290,342,1290,259,RED,2.2); s.text(1300,291,"Y",15,RED,28)
    s.text(1210,480,"screen",13,INK,55); s.text(1190,520,"D",14,INK,24)
    return s


def d1315() -> Scene:
    s = cscene("D13.15", "Electric flux counts projected area, not surface area",
               "Φ = EA cosθ; the normal makes angle θ with E.")
    panel(s,55,145,1280,555,"TILTED SURFACE IN A UNIFORM FIELD")
    for yy in [250,315,380,445,510,575]: s.arrow(115,yy,490,yy,GRID,1.6)
    # parallelogram face tilted relative to its normal and projected area
    face=[(610,365),(866,236),(866,408),(610,537)]
    dot_path(s,face+[face[0]],BLUE,3)
    # Surface normal rotated up-right; horizontal field points right.
    s.arrow(735,365,825,365,ORANGE,2.5); s.text(775,335,"E",16,ORANGE,25)
    s.arrow(735,365,796,470,PURPLE,2.7); s.text(799,463,"n̂",16,PURPLE,30)
    arc(s,735,365,60,0,-math.atan2(105,61),TEAL,2); s.text(786,402,"θ",16,TEAL,24)
    s.text(645,548,"area A",15,BLUE,80)
    # perpendicular projection (same number of field lines, smaller face-on width)
    projection=[(1000,295),(1100,295),(1100,485),(1000,485),(1000,295)]
    dot_path(s,projection,GRID,1.7,"dashed")
    s.text(965,515,"projected area A cosθ",14,GRID,205)
    s.arrow(865,365,994,365,RED,1.8); s.text(881,338,"projection",12,RED,80)
    s.text(1012,374,"A cosθ",15,GRID,82)
    s.text(170,642,"Φ = E·A = EA cosθ",22,GREEN,275)
    s.text(915,642,"Same field lines cross both surfaces.",15,INK,320)
    return s


def d1316() -> Scene:
    s = cscene("D13.16", "The solid-angle cone proves Gauss's flux rule",
               "Opposite intersections contribute equal |dΩ| with opposite outward signs.")
    panel(s,35,145,655,555,"CHARGE INSIDE · ONE CONE CUTS TWICE")
    # A lumpy closed surface and an interior charge; opposite rays cut two patches.
    q=(345,425); charge(s,*q,"+q",RED,17)
    s.ellipse(145,240,510,350,BLUE,"transparent",2.4)
    s.line(q[0],q[1],605,365,PURPLE,2); s.line(q[0],q[1],610,397,PURPLE,2)
    s.line(q[0],q[1],180,485,PURPLE,2); s.line(q[0],q[1],184,516,PURPLE,2)
    s.dot(606,382,5,ORANGE); s.dot(182,500,5,ORANGE)
    s.text(555,331,"near patch r₁",13,ORANGE,110); s.text(94,532,"far patch r₂",13,ORANGE,100)
    s.arrow(606,382,650,350,TEAL,2); s.arrow(182,500,138,542,TEAL,2)
    s.text(555,408,"acute α: outward flux",12,GREEN,135)
    s.text(89,562,"obtuse α: inward flux",12,RED,140)
    s.text(245,620,"dΦ = (q/4πε₀)dΩ",16,INK,210)
    panel(s,720,145,655,555,"CHARGE OUTSIDE · ENTRY AND EXIT CANCEL")
    s.ellipse(900,260,360,300,BLUE,"transparent",2.4)
    charge(s,815,414,"+q",RED,17)
    s.line(815,395,1280,330,PURPLE,2); s.line(815,431,1280,467,PURPLE,2)
    # Mark both actual intersections on the two rays; arrows point away from q.
    for x,y in [(903,383),(1237,336),(903,438),(1248,465)]: s.dot(x,y,5,ORANGE)
    s.arrow(880,386,920,381,TEAL,2); s.arrow(1200,341,1245,335,TEAL,2)
    s.arrow(880,434,923,437,TEAL,2); s.arrow(1212,462,1255,466,TEAL,2)
    s.text(868,359,"entry: −dΩ",13,RED,105); s.text(1160,486,"exit: +dΩ",13,GREEN,100)
    s.text(830,595,"net flux = 0 for an external charge",16,INK,280)
    return s


def d1317() -> Scene:
    s = cscene("D13.17", "A cavity charge induces equal-and-opposite conductor charge",
               "The metal has E=0; an earthed outer surface carries no exterior field.")
    panel(s,30,145,865,555,"ISOLATED SPHERICAL CONDUCTOR WITH OFF-CENTRE CAVITY")
    # outer sphere, offset cavity, charge, induced charges
    s.ellipse(260,235,450,390,BLUE,PALE_BLUE,2.5)
    s.ellipse(365,332,205,188,WHITE,WHITE,1)
    s.ellipse(365,332,205,188,TEAL,"transparent",2)
    charge(s,430,412,"+q",RED,18)
    # inner induced negative charge crowded near +q and sparse opposite side
    for x,y in [(389,378),(399,399),(400,433),(420,454),(482,372),(515,397),(526,430),(507,466)]:
        s.text(x,y,"−",13,BLUE,18)
    # outer + charge and radial field lines
    for a in [i*math.pi/4 for i in range(8)]:
        px=485+220*math.cos(a); py=430+186*math.sin(a)
        s.text(px-5,py-7,"+",12,ORANGE,18)
        s.arrow(px,py,px+45*math.cos(a),py+38*math.sin(a),ORANGE,1.5)
    gaussian=[(485+160*math.cos(2*math.pi*i/80),430+150*math.sin(2*math.pi*i/80)) for i in range(81)]
    dot_path(s,gaussian,PURPLE,1.6,"dashed")
    s.text(570,535,"Gaussian surface in metal: Φ=0",13,PURPLE,220)
    s.text(76,609,"inner surface: −q  ·  outer surface: +q (isolated neutral conductor)",14,INK,470)
    panel(s,930,145,445,555,"OUTER SURFACE EARTHED")
    s.ellipse(1080,272,180,180,BLUE,PALE_BLUE,2.5)
    s.ellipse(1120,310,100,102,WHITE,WHITE,1)
    s.ellipse(1120,310,100,102,TEAL,"transparent",2)
    charge(s,1169,360,"+q",RED,15)
    for xx,yy in [(1132,330),(1197,333),(1131,382),(1199,385)]: s.text(xx,yy,"−",11,BLUE,15)
    s.line(1260,330,1315,330,INK,2); s.line(1315,330,1315,395,INK,2)
    s.line(1296,395,1334,395,INK,2); s.line(1302,402,1328,402,INK,2)
    s.text(995,495,"earth supplies −q; outer charge = 0",14,GREEN,320)
    s.text(995,545,"no field lines outside",15,INK,200)
    return s


def d1318() -> Scene:
    s = cscene("D13.18", "Flux through a corner-charge cube by eight-cube symmetry",
               "A far face of the original cube carries q/(24ε₀); a disc flux is a solid-angle fraction.")
    panel(s,30,145,690,555,"ONE CUBE AND THE 2×2×2 CONSTRUCTION")
    # One small cube: the charge is at a corner; three adjacent faces contain it.
    A=(92,338); B=(240,338); C=(240,486); D=(92,486); shift=(48,-36)
    A2=(A[0]+shift[0],A[1]+shift[1]); B2=(B[0]+shift[0],B[1]+shift[1]); C2=(C[0]+shift[0],C[1]+shift[1]); D2=(D[0]+shift[0],D[1]+shift[1])
    for p,q in [(A,B),(B,C),(C,D),(D,A),(A,A2),(B,B2),(C,C2),(D,D2),(A2,B2),(B2,C2),(C2,D2)]: s.line(*p,*q,BLUE,2)
    charge(s,*A,"q",RED,14)
    s.text(63,523,"three faces through q: Φ=0",12,RED,200)
    s.text(64,550,"three opposite faces: q/(24ε₀) each",12,GREEN,230)
    s.text(82,590,"the cube's total flux is q/(8ε₀)",12,INK,220)
    # Eight small cubes form a larger block with q at the common central vertex.
    F=(365,338); G=(575,338); H=(575,548); I=(365,548); sh=(70,-54)
    F2=(F[0]+sh[0],F[1]+sh[1]); G2=(G[0]+sh[0],G[1]+sh[1]); H2=(H[0]+sh[0],H[1]+sh[1]); I2=(I[0]+sh[0],I[1]+sh[1])
    for p,q in [(F,G),(G,H),(H,I),(I,F),(F,F2),(G,G2),(H,H2),(I,I2),(F2,G2),(G2,H2),(H2,I2),(I2,F2)]: s.line(*p,*q,TEAL,2)
    # Subdivide the visible front and side faces into 2×2 cells.
    for xx in [470]:
        s.line(xx,338,xx,548,GRID,1.2); s.line(xx+70,284,xx+70,494,GRID,1.2)
    for yy in [443]:
        s.line(365,yy,575,yy,GRID,1.2); s.line(435,yy-54,645,yy-54,GRID,1.2)
    s.line(470,338,540,284,GRID,1.2); s.line(470,443,540,389,GRID,1.2)
    qcenter=(505,416); charge(s,*qcenter,"q",RED,13)
    s.text(393,584,"q at the centre; symmetry gives q/ε₀ total flux",11,INK,275)
    s.text(398,610,"each large face: q/(6ε₀) = 4 small faces × q/(24ε₀)",10,GREEN,290)
    panel(s,755,145,620,555,"DISC SEEN UNDER SOLID ANGLE Ω")
    # Charge, disk, cone and half-angle.
    q=(845,418); charge(s,*q,"q",RED,17)
    s.ellipse(1130,303,165,230,BLUE,PALE_BLUE,2)
    s.line(q[0]+20,q[1],1190,302,PURPLE,2); s.line(q[0]+20,q[1],1190,533,PURPLE,2)
    s.line(1190,302,1190,533,BLUE,3)
    s.line(q[0]+35,q[1],1190,q[1],GRID,1.2,"dashed")
    arc(s,q[0]+25,q[1],72,0,math.atan2(q[1]-302,1190-q[0]-25),TEAL,1.8)
    s.text(905,376,"θ",15,TEAL,24); s.text(1027,392,"x",15,INK,25)
    s.text(920,574,"cosθ = x/√(x²+R²)",15,GREEN,225)
    s.text(920,615,"Φ = qΩ/(4πε₀)",16,INK,190)
    return s


def d1319() -> Scene:
    s = cscene("D13.19", "The radial electrostatic field does zero net work around a loop",
               "Circular arcs contribute zero; the two radial legs cancel exactly.")
    panel(s,38,145,820,555,"TWO RADII + TWO CIRCULAR ARCS")
    O=(380,430); r1,r2=95,210
    charge(s,*O,"+q",RED,18)
    # quarter-annular loop with radial connector lines.
    a0,a1=math.radians(20),math.radians(105)
    arc(s,O[0],O[1],r1,a0,a1,TEAL,2.5); arc(s,O[0],O[1],r2,a0,a1,TEAL,2.5)
    p1=(O[0]+r1*math.cos(a0),O[1]-r1*math.sin(a0)); p2=(O[0]+r2*math.cos(a0),O[1]-r2*math.sin(a0))
    p3=(O[0]+r2*math.cos(a1),O[1]-r2*math.sin(a1)); p4=(O[0]+r1*math.cos(a1),O[1]-r1*math.sin(a1))
    s.line(*p1,*p2,TEAL,2.5); s.line(*p3,*p4,TEAL,2.5)
    s.text(500,236,"r₂",15,TEAL,30); s.text(431,345,"r₁",15,TEAL,30)
    # E radial and path tangents on the arcs
    for a in [math.radians(40),math.radians(76)]:
        px=O[0]+r2*math.cos(a); py=O[1]-r2*math.sin(a)
        s.arrow(px,py,px+55*math.cos(a),py-55*math.sin(a),BLUE,1.8)
    s.text(540,401,"E ⟂ dl on arcs",14,BLUE,155)
    s.arrow(p1[0],p1[1],p1[0]+42*math.cos(a0),p1[1]-42*math.sin(a0),ORANGE,2)
    s.arrow(p3[0],p3[1],p3[0]-42*math.cos(a1),p3[1]+42*math.sin(a1),ORANGE,2)
    s.text(139,603,"radial work: +kq(1/r₁−1/r₂) and the return −same",14,GREEN,470)
    panel(s,895,170,475,485,"ANY CLOSED PATH")
    # arbitrary wavy loop and radial decomposition cue
    dot_path(s,[(1000,420),(1040,335),(1110,365),(1185,325),(1250,400),(1230,490),(1145,520),(1050,495),(1000,420)],PURPLE,2.5)
    charge(s,1125,420,"+q",RED,15)
    s.text(960,558,"For radial E(r), only dr enters ∫E·dl.",15,INK,350)
    s.text(960,599,"∮ E·dl = 0  ⇒  electrostatic E is conservative",14,GREEN,390)
    return s


def d1320() -> Scene:
    s = cscene("D13.20", "Equipotentials cross electric-field lines at right angles",
               "Equal-potential contours crowd where |E| is large; a field line is −∇V.")
    panels=[(30,145,"(a) POINT CHARGE"),(493,145,"(b) DIPOLE"),(956,145,"(c) TWO LIKE CHARGES")]
    for x,y,h in panels: panel(s,x,y,430,555,h)
    # point charge concentric equipotentials and radial E
    cx,cy=245,415
    for r in [44,82,122]: s.ellipse(cx-r,cy-r,2*r,2*r,TEAL,"transparent",1.5)
    charge(s,cx,cy,"+",RED,14)
    for a in [0,math.pi/2,math.pi,3*math.pi/2]:
        s.arrow(cx+35*math.cos(a),cy+35*math.sin(a),cx+145*math.cos(a),cy+145*math.sin(a),BLUE,1.8)
    s.text(92,615,"concentric V; radial E",13,INK,180)
    # Dipole: small closed equipotentials and field curves from + to −.
    cx,cy=708,420; charge(s,cx-70,cy,"+",BLUE,14); charge(s,cx+70,cy,"−",RED,14)
    for r in [28,46,62]:
        s.ellipse(cx-70-r,cy-r,2*r,2*r,TEAL,"transparent",1.25)
        s.ellipse(cx+70-r,cy-r,2*r,2*r,TEAL,"transparent",1.25)
    for h in [-92,-62,62,92]:
        pts=[(cx-58+116*i/32,cy+h*math.sin(math.pi*i/32)) for i in range(33)]
        dot_path(s,pts,BLUE,1.5)
    s.arrow(cx-9,cy,cx+10,cy,BLUE,1.8)
    s.line(cx,275,cx,565,PURPLE,2,"dashed"); s.text(cx-38,585,"V=0",13,PURPLE,60)
    s.text(536,615,"dipole contours crossed by field lines",12,INK,300)
    # Two like charges: paired equipotential lobes touch at the neutral saddle.
    cx,cy=1170,420; charge(s,cx-72,cy,"+",BLUE,14); charge(s,cx+72,cy,"+",BLUE,14)
    s.ellipse(cx-142,cy-92,142,184,TEAL,"transparent",2)
    s.ellipse(cx,cy-92,142,184,TEAL,"transparent",2)
    for r in [34,52]:
        s.ellipse(cx-72-r,cy-r,2*r,2*r,TEAL,"transparent",1.2)
        s.ellipse(cx+72-r,cy-r,2*r,2*r,TEAL,"transparent",1.2)
    s.dot(cx,cy,5,RED); s.text(cx-12,cy+14,"E=0",11,RED,45)
    for yy in [cy-54,cy+54]:
        s.arrow(cx-18,yy,cx-63,yy,BLUE,1.4); s.arrow(cx+18,yy,cx+63,yy,BLUE,1.4)
    for a in [math.pi/4,3*math.pi/4,5*math.pi/4,7*math.pi/4]:
        s.arrow(cx-72+24*math.cos(a),cy+24*math.sin(a),cx-72+65*math.cos(a),cy+65*math.sin(a),BLUE,1.3)
        s.arrow(cx+72+24*math.cos(a),cy+24*math.sin(a),cx+72+65*math.cos(a),cy+65*math.sin(a),BLUE,1.3)
    s.text(1012,615,"figure-eight equipotential through the saddle",12,INK,330)
    return s


def d1321() -> Scene:
    s = cscene("D13.21", "Assembling four equal charges stores pairwise work",
               "The total energy is the sum over six pairs: (4+√2)kq²/a.")
    panel(s,38,145,745,565,"SQUARE · SIX PAIR INTERACTIONS")
    pts=[(215,290),(535,290),(535,570),(215,570)]
    dot_path(s,pts+[pts[0]],BLUE,2.5)
    for i,(x,y) in enumerate(pts,1):
        s.dot(x,y,23,BLUE); s.text(x-9,y-13,str(i),16,WHITE,18)
    # all six pairs: four sides and two diagonals
    for i,j in [(0,1),(1,2),(2,3),(3,0)]: s.line(*pts[i],*pts[j],GRID,1.8)
    s.line(*pts[0],*pts[2],PURPLE,2,"dashed"); s.line(*pts[1],*pts[3],PURPLE,2,"dashed")
    for x,y in pts: s.text(x-15,y+32,"q",13,INK,20)
    s.text(300,263,"a",14,TEAL,30); s.text(374,420,"a√2",14,PURPLE,55)
    panel(s,820,145,560,565,"WORK AS EACH CHARGE ARRIVES")
    lines=["1:  W₁ = 0",
           "2:  W₂ = kq²/a",
           "3:  W₃ = kq²/a + kq²/(√2 a)",
           "4:  W₄ = 2kq²/a + kq²/(√2 a)"]
    for i,t in enumerate(lines): s.text(870,245+i*64,t,16,INK,430)
    s.line(864,517,1334,517,GRID,1.4)
    s.text(870,552,"U = Σ pairs = (4+√2)kq²/a",20,GREEN,395)
    return s


def d1322() -> Scene:
    s = cscene("D13.22", "Connected conductors share potential, not surface charge density",
               "Q₁/Q₂=R₁/R₂ but σ₁/σ₂=R₂/R₁; the smaller sphere's field is more crowded.")
    panel(s,35,150,900,550,"TWO SPHERES JOINED BY A THIN WIRE")
    s.line(358,365,622,365,INK,5)
    s.ellipse(116,275,240,190,BLUE,PALE_BLUE,2.5)
    s.ellipse(610,320,100,100,TEAL,PALE_TEAL,2.5)
    s.text(184,480,"R₁ large",15,BLUE,100); s.text(607,438,"R₂ small",14,TEAL,100)
    # More charge resides on the larger sphere overall, but its surface density is lower.
    for x,y in [(160,320),(218,300),(270,326),(194,380),(278,410),(150,408),(225,438),(315,385)]:
        s.text(x,y,"+",13,ORANGE,20)
    for x,y in [(646,339),(674,339),(646,390),(674,390)]: s.text(x,y,"+",12,ORANGE,18)
    # Radial field lines emerge from both equipotential spheres.
    c1=(236,370); c2=(660,370)
    for a in [i*math.pi/4 for i in range(8)]:
        p=(c1[0]+124*math.cos(a),c1[1]+98*math.sin(a))
        q=(c1[0]+170*math.cos(a),c1[1]+135*math.sin(a))
        s.arrow(*p,*q,BLUE,1.3)
    for a in [i*math.pi/4 for i in range(8)]:
        p=(c2[0]+53*math.cos(a),c2[1]+53*math.sin(a))
        q=(c2[0]+86*math.cos(a),c2[1]+86*math.sin(a))
        s.arrow(*p,*q,TEAL,1.6)
    s.text(80,570,"same V on both",16,GREEN,140)
    s.text(80,613,"Q₁/Q₂ = R₁/R₂",16,INK,180)
    s.text(355,613,"σ₁/σ₂ = R₂/R₁",16,INK,190)
    panel(s,975,180,400,455,"POINTED CONDUCTOR")
    dot_path(s,[(1080,550),(1095,445),(1130,365),(1188,285),(1245,365),(1280,445),(1295,550)],BLUE,3)
    for y in [350,400,450,500]:
        s.arrow(1188,y,1188,y-70,ORANGE,1.8)
    s.text(1030,585,"field lines crowd at sharp tips",15,ORANGE,270)
    return s


def d1323() -> Scene:
    s = cscene("D13.23", "Grounding or joining concentric shells changes the charge ledger",
               "The field in the gap depends on the inner-shell charge; conductor constraints set the rest.")
    cases=[(28,150,"(a) ISOLATED · INNER q, OUTER Q"),
           (710,150,"(b) OUTER SHELL EARTHED"),
           (28,445,"(c) INNER SPHERE EARTHED"),
           (710,445,"(d) SHELLS JOINED BY WIRE")]
    for x,y,h in cases: panel(s,x,y,650,260,h)
    def shell_panel(x: int,y:int,field:bool=True):
        cx,cy=x+280,y+145
        s.ellipse(cx-94,cy-70,188,140,TEAL,"transparent",2.2)
        s.ellipse(cx-42,cy-32,84,64,BLUE,PALE_BLUE,1.8)
        if field:
            for dy in [-34,0,34]: s.arrow(cx+52,cy+dy,cx+84,cy+dy,ORANGE,1.5)
        return cx,cy
    # (a)
    cx,cy=shell_panel(28,150,True); s.text(cx-14,cy-12,"q",13,RED,25); s.text(399,226,"Vₐ=kq/a+kQ/b",13,INK,170); s.text(399,261,"Vᵦ=k(q+Q)/b",13,INK,170)
    # (b) outer grounded, net outer charge -q
    cx,cy=shell_panel(710,150,True); s.text(cx-14,cy-12,"q",13,RED,25); s.text(1085,226,"Qouter=−q",14,GREEN,120); s.text(1085,261,"Vᵦ=0; no outside field",12,INK,190)
    # (c) inner grounded, outer remains isolated Q
    cx,cy=shell_panel(28,445,True); s.text(cx-25,cy-12,"−Qa/b",11,RED,55); s.text(395,521,"inner charge = −Qa/b",13,GREEN,190); s.text(395,556,"Vₐ=0",14,INK,60)
    # (d) joined conductor: charge migrates to outside
    cx,cy=shell_panel(710,445,False); s.text(cx-14,cy-12,"0",13,MUTED,22); s.line(cx+94,cy,cx+150,cy,INK,2); s.text(1080,521,"all net charge on outer",13,GREEN,190); s.text(1080,556,"no field in gap",14,INK,120)
    return s


def d1324() -> Scene:
    s = cscene("D13.24", "A grounded plane is replaced by a mirror image charge",
               "Image −q lies h below the plane; the real charge is attracted with kq²/(4h²).")
    panel(s,35,145,890,560,"REAL CHARGE ABOVE AN EARTHED PLANE")
    yplane=475; s.line(92,yplane,865,yplane,INK,4)
    for xx in range(110,855,24): s.line(xx,yplane+5,xx-12,yplane+18,GRID,1)
    s.text(104,492,"grounded conductor",14,INK,155)
    real=(440,286); image=(440,665)
    charge(s,*real,"+q",RED,19)
    image_outline=[(image[0]+19*math.cos(2*math.pi*i/40),image[1]+19*math.sin(2*math.pi*i/40)) for i in range(41)]
    dot_path(s,image_outline,BLUE,1.8,"dashed")
    s.text(image[0]-8,image[1]-12,"−",16,BLUE,18)
    s.text(470,278,"real",14,RED,42); s.text(470,652,"image (dashed)",13,BLUE,115)
    s.line(real[0],real[1],image[0],image[1],PURPLE,1.5,"dashed")
    s.arrow(real[0]+32,real[1]+18,real[0]+32,real[1]+105,ORANGE,2.8); s.text(480,351,"F=kq²/(4h²)",15,ORANGE,140)
    s.arrow(440,real[1]+27,440,yplane-8,TEAL,2); s.text(453,372,"h",15,TEAL,25)
    # representative field lines that meet the grounded plane normally
    for dx in [-190,-115,115,190]:
        pts=[]
        for i in range(31):
            t=i/30
            x=real[0]+dx*math.sin(math.pi*t/2)
            y=real[1]+(yplane-real[1])*t + 28*math.sin(math.pi*t)*(1 if dx>0 else -1)
            pts.append((x,y))
        dot_path(s,pts,BLUE,1.7)
    panel(s,960,175,415,480,"INDUCED SURFACE CHARGE")
    x0,y0,x1,y1=1010,520,1325,280
    axes(s,x0,y0,x1,y1,"ρ/h","σ(ρ)")
    pts=[]
    for i in range(101):
        q=3*i/100; val=-(1+q*q)**-1.5
        pts.append((x0+q/3*(x1-x0),y0+(-val)*112))
    dot_path(s,pts,RED,2.7)
    s.text(1035,553,"σ(ρ)=−qh/[2π(ρ²+h²)^(3/2)]",13,RED,300)
    s.text(1020,590,"σ(0)=−q/(2πh²)",14,INK,180)
    return s


def d1325() -> Scene:
    s = cscene("D13.25", "Electrostatic pressure can balance a soap bubble's surface tension",
               "For two interfaces, 4γ/R = σ²/(2ε₀), giving Q=8π√(2ε₀γR³).")
    panel(s,35,150,650,555,"PRESSURES ON A CHARGED BUBBLE")
    s.ellipse(160,270,350,290,BLUE,PALE_BLUE,3)
    s.ellipse(173,283,324,264,TEAL,"transparent",1.7)
    for a in [i*math.pi/4 for i in range(8)]:
        x=335+140*math.cos(a); y=415+112*math.sin(a)
        s.arrow(x,y,x-42*math.cos(a),y-36*math.sin(a),ORANGE,2)
        s.arrow(x+8*math.cos(a),y+7*math.sin(a),x+48*math.cos(a),y+42*math.sin(a),RED,2)
    s.text(116,560,"inward: 4γ/R",16,ORANGE,140)
    s.text(422,560,"outward: σ²/(2ε₀)",15,RED,200)
    s.text(143,610,"double surface tension",13,MUTED,180)
    panel(s,730,150,650,555,"BALANCED STATE")
    s.ellipse(880,280,300,250,TEAL,PALE_TEAL,2.5)
    for a in [i*math.pi/4 for i in range(8)]:
        x=1030+138*math.cos(a); y=405+110*math.sin(a)
        s.arrow(x,y,x+65*math.cos(a),y+52*math.sin(a),BLUE,1.8)
    s.text(840,564,"radial E outside; p_e = ε₀E²/2",15,BLUE,260)
    s.text(812,610,"Q = 8π√(2ε₀γR³)",20,GREEN,305)
    return s


def d1326() -> Scene:
    s = cscene("D13.26", "Superposition makes the overlap field uniform",
               "Equal and opposite uniform charge densities cancel in the overlap, leaving a constant field.")
    panel(s,32,150,665,550,"TWO OVERLAPPING CHARGED CYLINDERS · CROSS-SECTION")
    # shifted equal circles, overlap shaded by cross-hatching
    c1=(290,420); c2=(405,420); R=165
    s.ellipse(c1[0]-R,c1[1]-R,2*R,2*R,BLUE,PALE_BLUE,2.2)
    s.ellipse(c2[0]-R,c2[1]-R,2*R,2*R,RED,PALE_RED,2.2)
    s.ellipse(c1[0]-R,c1[1]-R,2*R,2*R,BLUE,"transparent",1.3)
    s.ellipse(c2[0]-R,c2[1]-R,2*R,2*R,RED,"transparent",1.3)
    s.dot(*c1,5,BLUE); s.dot(*c2,5,RED)
    s.text(c1[0]-33,c1[1]-10,"+ρ",15,BLUE,42); s.text(c2[0]-29,c2[1]-10,"−ρ",15,RED,42)
    s.arrow(c1[0],c1[1]+210,c2[0],c2[1]+210,PURPLE,2); s.text(319,635,"d",14,PURPLE,25)
    # only crescent regions retain net charge; uniform arrows fill overlap.
    for yy in [365,405,445,485]: s.arrow(330,yy,378,yy,ORANGE,1.7)
    s.text(130,220,"net +ρ crescent",12,BLUE,120); s.text(490,220,"net −ρ crescent",12,RED,120)
    s.text(242,581,"overlap: E = ρd/(2ε₀), constant",13,GREEN,245)
    panel(s,730,150,650,550,"OFF-CENTRE CAVITY IN A UNIFORM SPHERE")
    s.ellipse(875,245,390,360,BLUE,PALE_BLUE,2.3)
    # cavity offset to the right
    s.ellipse(1045,325,175,170,WHITE,WHITE,1)
    s.ellipse(1045,325,175,170,TEAL,"transparent",2)
    s.ellipse(875,245,390,360,BLUE,"transparent",1.4)
    s.dot(1070,425,5,BLUE); s.dot(1132,410,5,RED)
    s.text(1034,437,"O",13,BLUE,18); s.text(1141,396,"O_c",13,RED,42)
    for yy in [315,360,405,450,495,540]: s.arrow(923,yy,1016,yy,ORANGE,1.8)
    for yy in [350,390,430,470]: s.arrow(1067,yy,1122,yy-13,PURPLE,1.8)
    s.arrow(1070,425,1132,410,PURPLE,2.3); s.text(1090,387,"d",14,PURPLE,24)
    s.text(893,621,"E_cavity = ρd/(3ε₀) along O → O_c",14,GREEN,320)
    return s


TOPIC_INFO = {
    "elasticity": ("Elasticity.md", 12),
    "electrostatics": ("Electrostatics.md", 13),
}

BUILDERS = [
    ("elasticity", "D12.1", "The stress–strain curve with six landmarks", d121),
    ("elasticity", "D12.2", "The three modulus geometries", d122),
    ("elasticity", "D12.3", "Composite rod in series and stress distribution", d123),
    ("elasticity", "D12.4", "Thermal stress: free expansion versus forced length", d124),
    ("elasticity", "D12.5", "Torsion of a circular shaft and hollow-versus-solid sections", d125),
    ("elasticity", "Falling weight on a wire: force and energy", d126),
    ("elasticity", "Neutral axis and fibre strains in bending", d127),
    ("elasticity", "Cantilever deflection and I-beam comparison", d128),
    ("elasticity", "Interatomic potential well and linear region", d129),
    ("elasticity", "Material property chart: Young modulus versus density", d1210),
    ("elasticity", "Poisson contraction of a pulled wire", d1211),
    ("elasticity", "Element of a rod under its own weight", d1212),
    ("elasticity", "Density of seawater against depth", d1213),
    ("elasticity", "Hoop and longitudinal stresses in a thin cylinder", d1214),
    ("electrostatics", "Three charging mechanisms with electron transfer", d131),
    ("electrostatics", "Coulomb's law on a charge pair with unit vector", d132),
    ("electrostatics", "The Coulomb torsion balance", d133),
    ("electrostatics", "Field-line patterns for point charge, dipole, like charges and sheet", d134),
    ("electrostatics", "Electric field on the axis of a charged ring", d135),
    ("electrostatics", "Field of a finite line charge with endpoint angles", d136),
    ("electrostatics", "The uniformly charged disc built from rings", d137),
    ("electrostatics", "Two charged sheets: field in three regions", d138),
    ("electrostatics", "Field of a charged arc at its centre", d139),
    ("electrostatics", "Conductor surface field: patch and rest", d1310),
    ("electrostatics", "Dipole in a uniform electric field", d1311),
    ("electrostatics", "Dipole in a non-uniform field", d1312),
    ("electrostatics", "Three-charge equilibrium geometries", d1313),
    ("electrostatics", "Charged pendulum and deflecting plates", d1314),
    ("electrostatics", "Electric flux through a tilted area", d1315),
    ("electrostatics", "The solid-angle cone argument for Gauss's law", d1316),
    ("electrostatics", "Charge in a cavity: induced conductor charges", d1317),
    ("electrostatics", "Eight-cube construction and disc solid angle", d1318),
    ("electrostatics", "Closed-loop work in a point-charge field", d1319),
    ("electrostatics", "Equipotential contours and electric-field lines", d1320),
    ("electrostatics", "Assembling four charges at square corners", d1321),
    ("electrostatics", "Two connected spheres at equal potential", d1322),
    ("electrostatics", "Concentric shells: four charge and grounding cases", d1323),
    ("electrostatics", "Method of images for a grounded plane", d1324),
    ("electrostatics", "Electrostatic pressure on a charged bubble", d1325),
    ("electrostatics", "Uniform overlap field and the off-centre spherical cavity", d1326),
]


def update_note_and_manifest(topic: str, records: list[tuple[str, str, str]]) -> None:
    master_name, _part = TOPIC_INFO[topic]
    master = ROOT / topic / master_name
    source = master.read_text(encoding="utf-8").splitlines()
    by_id = {diagram_id: (title, slug) for diagram_id, title, slug in records}
    i = 0
    while i < len(source):
        match = re.match(r"^> \[!abstract\] DIAGRAM (D\d+\.\d+) · ", source[i])
        if not match or match.group(1) not in by_id:
            i += 1
            continue
        diagram_id = match.group(1)
        j = i + 1
        while j < len(source) and source[j].startswith(">"):
            j += 1
        while j < len(source) and source[j] == "":
            j += 1
        embed = f"![[../_obsidian/excalidraw/{by_id[diagram_id][1]}|900]]"
        if j >= len(source) or source[j] != embed:
            source[j:j] = [embed, ""]
            j += 2
        i = j
    master.write_text("\n".join(source) + "\n", encoding="utf-8")

    manifest_path = ROOT / topic / "figures.json"
    if manifest_path.is_file():
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    else:
        manifest = {"slug": topic, "policy": "docs/obsidian-plugin-workflow.md §2", "figures": []}
    drawings = []
    note_lines = master.read_text(encoding="utf-8").splitlines()
    for diagram_id, title, slug in records:
        header = f"> [!abstract] DIAGRAM {diagram_id} ·"
        start = next(i for i, line in enumerate(note_lines) if line.startswith(header))
        block = []
        for line in note_lines[start + 1:]:
            if not line.startswith(">"):
                if block:
                    break
                continue
            block.append(line)
        show = next((line.split("*Show:*", 1)[1].strip() for line in block if "*Show:*" in line), "")
        search = next((line.split("*Search:*", 1)[1].strip() for line in block if "*Search:*" in line), "")
        drawings.append({
            "id": diagram_id, "kind": "excalidraw", "title": title,
            "show": show, "search": search,
            "file": f"_obsidian/excalidraw/{slug}.md",
            "source": f"{topic}/{master_name} · {diagram_id}",
        })
    manifest["renderer"] = "obsidian-excalidraw-plugin@2.27.3"
    manifest["drawings"] = drawings
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def expanded_builders():
    """Yield (topic, diagram-id, title, builder), deriving ids for concise rows."""
    for row in BUILDERS:
        if len(row) == 4:
            yield row
            continue
        topic, title, builder = row
        part = TOPIC_INFO[topic][1]
        prefix = f"d{part}"
        suffix = builder.__name__[len(prefix):]
        if not suffix.isdigit():
            raise ValueError(f"cannot derive a diagram number from {builder.__name__}")
        yield topic, f"D{part}.{int(suffix)}", title, builder


def main() -> None:
    by_topic: dict[str, list[tuple[str, str, str]]] = {}
    expanded = list(expanded_builders())
    for topic, diagram_id, title, builder in expanded:
        slug, _path = scene_file(topic, diagram_id, title, builder())
        by_topic.setdefault(topic, []).append((diagram_id, title, slug))
    for topic, records in by_topic.items():
        update_note_and_manifest(topic, records)
        print(f"{topic}: embedded {len(records)} scenes")
    print(f"Generated and embedded {len(expanded)} editable Excalidraw scenes for Parts 12–15.")


if __name__ == "__main__":
    main()
