#!/usr/bin/env python3
"""Build editable Excalidraw scenes for mechanics Parts 8–11.

Scenes are native Excalidraw v2 JSON in Markdown files under
``_obsidian/excalidraw``. Running this script also embeds each scene directly
under its DIAGRAM brief and refreshes that chapter's figures.json provenance.

Run from the repository root:
    python3 tools/build_excalidraw_batch_8_11.py
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
        color: str = PURPLE, sw: float = 2, steps: int = 28) -> None:
    pts = [(cx + r*math.cos(t), cy - r*math.sin(t))
           for t in [start + (stop-start)*i/steps for i in range(steps+1)]]
    polyline(s, pts, color, sw)


def axes(s: Scene, x0: float, y0: float, x1: float, y1: float,
         xlabel: str, ylabel: str, color: str = INK) -> None:
    s.arrow(x0, y0, x1, y0, color, 1.8)
    s.arrow(x0, y0, x0, y1, color, 1.8)
    s.text(x1-15, y0+8, xlabel, 15, color, 70)
    s.text(x0-28, y1-24, ylabel, 15, color, 65)


def spring(s: Scene, p1: tuple[float,float], p2: tuple[float,float],
           color: str = TEAL, turns: int = 7, amp: float = 12, sw: float = 2.3) -> None:
    x1,y1=p1; x2,y2=p2; dx=x2-x1; dy=y2-y1
    length=math.hypot(dx,dy)
    if length < 1: return
    ux,uy=dx/length,dy/length; nx,ny=-uy,ux
    pad=min(22,length*.12); pts=[(x1,y1),(x1+ux*pad,y1+uy*pad)]
    usable=max(1,length-2*pad)
    for i in range(1,turns*2):
        t=i/(turns*2); side=amp*(1 if i%2 else -1)
        pts.append((x1+ux*(pad+t*usable)+nx*side,
                    y1+uy*(pad+t*usable)+ny*side))
    pts.extend([(x2-ux*pad,y2-uy*pad),(x2,y2)])
    polyline(s,pts,color,sw)


def graph(s: Scene, x0: float, y0: float, w: float, h: float,
          points: list[tuple[float,float]], color: str, sw: float = 2.5) -> None:
    """Plot normalized (x,y) coordinates in [0,1]×[-1,1] from a bottom-left origin."""
    mapped=[(x0+x*w, y0-h*(y+1)/2) for x,y in points]
    polyline(s,mapped,color,sw)


def d81() -> Scene:
    s=Scene("D8.1"); s.title("A spinning disc has a linear velocity field",
        "For rigid rotation, each point moves tangent to its circle and v=ωr.")
    cx,cy,R=430,445,220
    s.ellipse(cx-R,cy-R,2*R,2*R,GRID,"transparent",2)
    s.dot(cx,cy,8,INK); s.text(cx-15,cy+18,"axis",14,INK,55)
    s.line(cx,cy,cx+R,cy,GRID,1.5,"dashed")
    s.text(cx+75,cy+10,"r=R",14,MUTED,65)
    s.line(cx,cy-12,cx+R/2,cy-12,BLUE,1.7,"dashed")
    s.text(cx+36,cy-35,"r=R/2",14,BLUE,80)
    s.dot(cx+R/2,cy,7,TEAL); s.dot(cx+R,cy,7,BLUE)
    s.arrow(cx+R/2,cy,cx+R/2,cy-86,TEAL,3)
    s.text(cx+R/2+13,cy-83,"v=ωR/2",15,TEAL,105)
    s.arrow(cx+R,cy,cx+R,cy-170,BLUE,3)
    s.text(cx+R+12,cy-165,"v=ωR",16,BLUE,100)
    s.text(cx-20,cy+48,"v=0",16,INK,70)
    arc(s,cx,cy,66,.25,1.55,ORANGE,2.6)
    s.text(cx+48,cy-92,"ω",20,ORANGE,35)
    panel(s,780,190,530,480,"SPEED SCALING")
    s.text(825,275,"v(r)=ωr",30,GREEN,360)
    s.text(825,345,"centre: r=0  →  v=0",20,INK,390)
    s.text(825,405,"mid-radius: r=R/2  →  v=ωR/2",19,TEAL,440)
    s.text(825,465,"rim: r=R  →  v=ωR",20,BLUE,390)
    s.text(825,555,"The disc turns as one body, but the\nspeed grows in direct proportion to r.",17,MUTED,410)
    return s


def d82() -> Scene:
    s=Scene("D8.2"); s.title("Six standard moments of inertia",
        "Each value is about the axis drawn; I measures resistance to angular acceleration.")
    cards=[
      ("SLENDER ROD · centre axis", "ML²/12", "rod", "axis ⟂ rod through centre"),
      ("THIN RING · symmetry axis", "MR²", "ring", "axis through centre ⟂ plane"),
      ("SOLID DISC · symmetry axis", "MR²/2", "disc", "axis through centre ⟂ plane"),
      ("SOLID SPHERE · diameter", "2MR²/5", "sphere", "axis through centre"),
      ("HOLLOW SPHERE · diameter", "2MR²/3", "shell", "axis through centre"),
      ("SOLID CYLINDER · symmetry", "MR²/2", "cylinder", "axis along cylinder")]
    for i,(head,val,kind,note) in enumerate(cards):
        col=i%3; row=i//3; x=40+col*445; y=145+row*285
        panel(s,x,y,420,255,head)
        if kind=="rod":
            s.line(x+85,y+115,x+335,y+115,BLUE,7)
            s.line(x+210,y+76,x+210,y+157,RED,2,"dashed"); s.dot(x+210,y+115,5,RED)
            s.text(x+182,y+54,"L",15,INK,35)
        elif kind in ("ring","disc"):
            fill=PALE_BLUE if kind=="disc" else "transparent"
            s.ellipse(x+144,y+52,132,132,BLUE,fill,2.5)
            s.line(x+210,y+118,x+273,y+118,GRID,1.5)
            s.ellipse(x+198,y+106,24,24,RED,WHITE,2); s.dot(x+210,y+118,4,RED)
            s.text(x+281,y+82,"R",15,INK,30); s.text(x+286,y+139,"axis ⊙",12,RED,75)
        elif kind in ("sphere","shell"):
            fill=PALE_TEAL if kind=="sphere" else "transparent"
            s.ellipse(x+145,y+52,132,132,TEAL,fill,2.5)
            s.line(x+145,y+118,x+277,y+118,RED,2,"dashed"); s.dot(x+210,y+118,5,RED)
            s.text(x+278,y+105,"diameter",13,INK,90)
        else:
            s.rect(x+165,y+78,120,80,TEAL,PALE_TEAL,2)
            s.ellipse(x+143,y+78,44,80,TEAL,PALE_TEAL,2)
            s.ellipse(x+263,y+78,44,80,TEAL,PALE_TEAL,2)
            s.line(x+143,y+118,x+307,y+118,RED,2,"dashed")
            s.text(x+309,y+101,"axis",13,INK,48)
        s.text(x+27,y+190,f"I = {val}",22,GREEN,180)
        s.text(x+205,y+196,note,13,MUTED,190)
    return s


def d83() -> Scene:
    s=Scene("D8.3"); s.title("Parallel-axis theorem: shift the axis, add Md²",
        "For a uniform disc, the rim axis is parallel to the central axis and is one radius away.")
    cx,cy,R=440,425,185
    s.ellipse(cx-R,cy-R,2*R,2*R,BLUE,PALE_BLUE,2.5)
    s.ellipse(cx-12,cy-12,24,24,BLUE,WHITE,2); s.dot(cx,cy,4,BLUE)
    s.text(cx-112,cy+20,"CM axis ⊙",15,BLUE,115)
    s.ellipse(cx+R-12,cy-12,24,24,RED,WHITE,2); s.dot(cx+R,cy,4,RED)
    s.text(cx+R+14,cy-22,"rim axis ⊙",15,RED,110)
    s.line(cx,cy,cx+R,cy,PURPLE,3,"dashed")
    s.text(cx+68,cy+12,"d=R",19,PURPLE,80)
    panel(s,790,205,500,415,"DISC ABOUT TWO PARALLEL AXES")
    s.text(845,300,"I_cm = ½MR²",25,BLUE,370)
    s.text(845,365,"I_rim = I_cm + Md²",24,PURPLE,390)
    s.text(845,425,"d=R  ⇒  I_rim = ½MR² + MR²",19,INK,410)
    s.text(845,485,"I_rim = 3MR²/2",26,GREEN,330)
    s.text(845,555,"The shift term is Md², not M d.",17,MUTED,370)
    return s


def d84() -> Scene:
    s=Scene("D8.4"); s.title("Torque is force times the perpendicular moment arm",
        "The pivot-to-point distance r and the perpendicular lever arm d are not generally equal.")
    O=(225,560); P=(485,390); Q=(225,390)
    s.dot(*O,8,INK); s.text(O[0]-25,O[1]+15,"O",18,INK,30)
    s.dot(*P,7,BLUE); s.text(P[0]+10,P[1]-28,"P",17,BLUE,30)
    s.arrow(*O,*P,PURPLE,2.7); s.text(335,438,"r",20,PURPLE,35)
    # Horizontal line of action through P; Q is its perpendicular foot from O.
    s.line(180,390,645,390,GRID,2,"dashed")
    s.arrow(*P,620,390,BLUE,3.5); s.text(568,355,"F",20,BLUE,30)
    s.line(*O,*Q,ORANGE,2.8,"dashed"); s.dot(*Q,5,ORANGE)
    s.text(238,455,"d=r sinθ",16,ORANGE,110)
    # Right-angle marker at the perpendicular foot and angle between r and F.
    s.line(225,410,245,410,INK,1.4); s.line(245,410,245,390,INK,1.4)
    theta=math.atan2(O[1]-P[1],P[0]-O[0])
    arc(s,O[0],O[1],74,0,theta,TEAL,2)
    s.text(286,511,"θ",18,TEAL,30)
    panel(s,770,190,535,430,"MOMENT ABOUT O")
    s.text(825,285,"τ = r × F",28,BLUE,360)
    s.text(825,350,"|τ| = rF sinθ",23,PURPLE,360)
    s.text(825,415,"d = r sinθ",23,ORANGE,300)
    s.text(825,480,"|τ| = Fd",27,GREEN,260)
    s.text(825,550,"Only the component of F perpendicular\nto r produces a turning effect.",17,MUTED,410)
    return s


def d85() -> Scene:
    s=Scene("D8.5"); s.title("Rolling to the right: contact is instantaneously at rest",
        "For no slip, ωR=v; translational and rotational velocities add as vectors.")
    cx,cy,R=430,430,175
    s.ellipse(cx-R,cy-R,2*R,2*R,BLUE,PALE_BLUE,2.5)
    s.dot(cx,cy,7,INK); s.text(cx-25,cy+16,"CM",15,INK,45)
    s.arrow(cx,cy,cx+105,cy,BLUE,3.5); s.text(cx+30,cy-30,"v",19,BLUE,30)
    # Clockwise rotation: rim velocities add at the top and cancel at contact.
    s.dot(cx,cy-R,6,TEAL); s.arrow(cx,cy-R,cx+165,cy-R,TEAL,3)
    s.text(cx+105,cy-R-28,"2v",18,TEAL,45)
    s.dot(cx,cy+R,6,RED); s.text(cx-90,cy+R+15,"v−ωR=0",16,RED,115)
    s.dot(cx+R,cy,6,PURPLE); s.arrow(cx+R,cy,cx+R+72,cy+78,PURPLE,2.8)
    s.text(cx+R+35,cy+88,"√2 v",15,PURPLE,70)
    s.dot(cx-R,cy,6,GREEN); s.arrow(cx-R,cy,cx-R+72,cy-78,GREEN,2.8)
    s.text(cx-R-3,cy-112,"√2 v",15,GREEN,70)
    arc(s,cx,cy,76,1.5,0.25,ORANGE,2.8); s.text(cx+56,cy-99,"ω clockwise",15,ORANGE,125)
    panel(s,790,205,495,390,"NO-SLIP VELOCITY SUM")
    s.text(845,300,"v_contact = v − ωR = 0",22,RED,390)
    s.text(845,365,"v_CM = v",22,BLUE,240)
    s.text(845,425,"v_top = v + ωR = 2v",22,TEAL,370)
    s.text(845,515,"The wheel translates and rotates;\neach point has a different velocity.",17,MUTED,390)
    return s


def d86() -> Scene:
    s=Scene("D8.6"); s.title("A spinning skater pulls in her arms",
        "With negligible external torque, angular momentum stays fixed while internal work raises K.")
    panel(s,55,160,600,520,"ARMS OUT · larger I, slower spin")
    panel(s,735,160,600,520,"ARMS IN · smaller I, faster spin")
    def skater(cx:float,cy:float,arms:float,omega:str):
        s.ellipse(cx-17,cy-177,34,34,INK,PALE_ORANGE,2)
        s.line(cx,cy-143,cx,cy-45,INK,4)
        s.line(cx,cy-110,cx-arms,cy-58,BLUE,4); s.line(cx,cy-110,cx+arms,cy-58,BLUE,4)
        s.line(cx,cy-45,cx-38,cy+35,INK,4); s.line(cx,cy-45,cx+38,cy+35,INK,4)
        arc(s,cx,cy-90,100,.35,2.6,TEAL,2.8)
        s.text(cx-80,cy+90,omega,18,TEAL,190)
    skater(355,425,155,"I₁ large · ω₁ small")
    skater(1035,425,65,"I₂ small · ω₂ large")
    s.text(255,600,"arms extended",15,MUTED,130); s.text(955,600,"arms tucked",15,MUTED,115)
    s.text(480,363,"I₁",18,BLUE,40); s.text(1135,363,"I₂",18,BLUE,40)
    s.text(570,410,"L=Iω",16,PURPLE,70)
    s.text(500,462,"conserved",14,PURPLE,100)
    s.text(455,630,"I₁ω₁ = I₂ω₂",20,GREEN,210)
    s.text(805,630,"K₂ > K₁",20,ORANGE,130)
    s.text(55,735,"The added rotational energy comes from the skater's work pulling her arms inward.",17,MUTED,1060)
    return s


def d87() -> Scene:
    s=Scene("D8.7"); s.title("Who wins the rolling race? The inertia ratio decides",
        "Released together on the same incline: the non-rotating block is fastest; hollow bodies lag.")
    # Ramp descends to the right; all bodies start at the same point.
    s.line(145,260,1220,640,INK,4)
    theta=math.atan2(380,1075)
    start=(180,272)
    # distance order follows a=g sinθ/(1+β); the block has β=0.
    data=[("block · slides",0.0,1010,ORANGE,"rect"),
          ("solid sphere",0.4,865,BLUE,"sphere"),
          ("solid cylinder",0.5,750,TEAL,"cylinder"),
          ("hollow sphere",2/3,630,PURPLE,"hollow"),
          ("hollow cylinder",1.0,505,RED,"ring")]
    for label,beta,x,color,kind in data:
        y=260+(x-145)*380/1075
        if kind=="rect": s.rect(x-32,y-50,64,45,color,PALE_ORANGE,2,True,angle=theta)
        else: s.ellipse(x-30,y-58,60,60,color,"transparent" if kind in ("hollow","ring") else PALE_BLUE,2.4)
        s.text(x-52,y-90,label,15,color,170)
        s.text(x-35,y+23,f"β={beta:.2g}",14,INK,90)
    s.dot(*start,5,INK); s.text(115,225,"same release point",15,MUTED,150)
    panel(s,90,675,1160,80,"ROLLING ACCELERATION")
    s.text(125,705,"a = g sinθ /(1+β),   β=I/(MR²)",20,GREEN,560)
    s.text(725,705,"smaller β → larger a → farther ahead at the same time",16,INK,490)
    return s


def d88() -> Scene:
    s=Scene("D8.8"); s.title("Sliding friction spins the ball up until rolling begins",
        "For t<t*: v falls while ωR rises; after v=ωR, ideal rolling continues without friction.")
    x0,y0,x1,y1=185,625,1210,220
    axes(s,x0,y0,x1,y1,"time t","speed")
    tstar=.52; ytop=y0-305; ymeet=y0-145
    s.line(x0,ytop,x0+tstar*(x1-x0),ymeet,BLUE,3.5)
    s.line(x0,y0,x0+tstar*(x1-x0),ymeet,TEAL,3.5)
    s.line(x0+tstar*(x1-x0),ymeet,x1,ymeet,BLUE,2.8)
    s.line(x0+tstar*(x1-x0),ymeet,x1,ymeet,TEAL,2.8)
    s.dot(x0+tstar*(x1-x0),ymeet,7,RED)
    s.line(x0+tstar*(x1-x0),y0,x0+tstar*(x1-x0),ymeet,GRID,1.4,"dashed")
    s.text(x0+90,ytop-32,"v(t)",18,BLUE,55)
    s.text(x0+80,y0-32,"ωR(t)",18,TEAL,85)
    s.text(x0+tstar*(x1-x0)-25,ymeet-42,"t*",17,RED,30)
    s.text(900,ymeet-38,"v=ωR",16,GREEN,80)
    s.text(220,175,"initial slip: v=v₀,  ωR=0",16,INK,300)
    s.text(790,690,"rolling constraint begins here",16,ORANGE,260)
    s.text(200,715,"Kinetic friction acts left on translation and supplies the clockwise torque.",16,MUTED,840)
    return s


def d89() -> Scene:
    s=Scene("D8.9"); s.title("A bullet embeds in a rod hinged at one end",
        "During the short impact, angular momentum about the hinge is conserved; hinge impulse has zero moment there.")
    # Rod upright, hinged at bottom; bullet hits at distance d.
    hx,hy=360,650; top=(360,235); hit=(360,430)
    s.line(*top,hx,hy,INK,10); s.dot(hx,hy,11,INK); s.text(hx-48,hy+22,"hinge O",16,INK,100)
    s.text(393,315,"uniform rod M,L",17,BLUE,140)
    s.line(hx-35,hy,hx+35,hy,GRID,3); s.line(hx,hy,hx,top[1],GRID,1.3,"dashed")
    s.text(303,525,"d",18,PURPLE,35)
    s.arrow(125,430,hit[0]-16,hit[1],ORANGE,3.5); s.text(170,395,"bullet m, v₀",17,ORANGE,130)
    s.ellipse(hit[0]-18,hit[1]-18,36,36,ORANGE,PALE_ORANGE,2)
    s.line(360,430,360,650,PURPLE,2,"dashed")
    s.arrow(360,430,480,350,GREEN,3.5); s.text(470,327,"ω after impact",16,GREEN,145)
    panel(s,700,200,570,420,"ANGULAR MOMENTUM ABOUT O")
    s.text(750,290,"before:  Lᵢ = m v₀ d",23,ORANGE,420)
    s.text(750,360,"I_rod = ML²/3",21,BLUE,330)
    s.text(750,415,"after:  L_f = (I_rod + md²)ω",21,GREEN,470)
    s.text(750,490,"m v₀ d = (ML²/3 + md²)ω",19,PURPLE,465)
    s.text(750,555,"Mechanical energy is not conserved in the embed.",16,MUTED,440)
    return s


def d810() -> Scene:
    s=Scene("D8.10"); s.title("A ladder at impending tip: the ground normal acts at the edge",
        "At the limiting contact, the ground reaction shifts to the foot edge; friction opposes the slide.")
    # Wall and floor
    s.line(875,230,875,680,INK,5); s.line(185,680,880,680,INK,5)
    foot=(410,680); top=(825,285)
    s.line(*foot,*top,BLUE,9); s.dot(*foot,9,INK)
    s.text(542,445,"ladder, length L",18,BLUE,170)
    # Forces on ladder
    s.arrow(620,480,620,595,RED,3.5); s.text(635,520,"mg",18,RED,45)
    s.dot(*top,7,BLUE); s.arrow(top[0],top[1],top[0]-125,top[1],PURPLE,3.2)
    s.text(700,244,"N_w",17,PURPLE,60)
    s.arrow(*foot,foot[0],foot[1]-125,GREEN,3.5); s.text(420,565,"N_g",17,GREEN,55)
    s.arrow(*foot,foot[0]+132,foot[1],ORANGE,3.2); s.text(485,690,"f",18,ORANGE,25)
    # Centre of mass, angle and limiting resultant.
    cm=((foot[0]+top[0])/2,(foot[1]+top[1])/2); s.dot(*cm,7,RED); s.text(cm[0]+12,cm[1]-22,"COM",15,RED,60)
    arc(s,foot[0],foot[1],90,0,math.atan2(foot[1]-top[1],top[0]-foot[0]),TEAL,2)
    s.text(495,638,"θ",18,TEAL,30)
    panel(s,965,265,365,305,"THRESHOLD")
    s.text(1005,350,"ΣF_x=0",20,INK,170)
    s.text(1005,400,"ΣF_y=0",20,INK,170)
    s.text(1005,455,"Στ_foot=0",20,PURPLE,200)
    s.text(1005,515,"N_g acts at the foot edge",17,GREEN,290)
    return s


def d811() -> Scene:
    s=Scene("D8.11"); s.title("A gyroscope precesses because torque turns L sideways",
        "When τ is perpendicular to L, dL=τdt changes its direction; the spin magnitude is nearly fixed.")
    # Side view: the spin axis is the axle, gravity acts at the centre of mass,
    # and the torque points perpendicular to the page.
    O=(330,570); C=(520,340)
    s.dot(*O,9,INK); s.text(285,590,"pivot",15,INK,60)
    s.line(*O,*C,INK,7); s.ellipse(C[0]-25,C[1]-25,50,50,TEAL,PALE_TEAL,2)
    s.arrow(C[0],C[1],C[0]+82,C[1]-99,BLUE,3.5); s.text(495,257,"L along axle",16,BLUE,120)
    s.arrow(C[0],C[1]+15,C[0],C[1]+115,RED,3.2); s.text(C[0]+13,C[1]+74,"Mg",16,RED,45)
    s.ellipse(422,405,26,26,PURPLE,"transparent",2); s.dot(435,418,4,PURPLE)
    s.text(448,409,"τ out of page",14,PURPLE,110)
    # Cone axis vertical; its projected rim indicates precession around gravity.
    s.line(330,570,330,220,GRID,1.5,"dashed")
    arc(s,330,570,205,.75,2.4,TEAL,2)
    s.text(165,330,"precession cone",15,TEAL,125)
    # Vector differential: dL is perpendicular to the current L; the tip moves sideways.
    panel(s,760,180,555,470,"VECTOR CHANGE IN ANGULAR MOMENTUM")
    ox,oy=875,510
    s.arrow(ox,oy,1095,oy,BLUE,4); s.text(980,476,"L",20,BLUE,30)
    s.arrow(1095,oy,1095,355,PURPLE,3.5); s.text(1110,390,"dL=τdt",17,PURPLE,100)
    s.arrow(ox,oy,1095,355,GREEN,3.2); s.text(930,385,"L+dL",16,GREEN,70)
    s.line(1095,oy,1095,355,GRID,1.2,"dashed")
    s.text(825,575,"dL ⟂ L  ⇒  |L| nearly constant",17,GREEN,300)
    s.text(810,240,"τ points along dL, perpendicular to L",16,MUTED,380)
    return s


def d812() -> Scene:
    s=Scene("D8.12"); s.title("Bullet embeds; the rod then swings upward",
        "Use angular momentum during the impact, then mechanical energy for the later swing.")
    boxes=[(35,"1 · APPROACH"),(485,"2 · EMBED"),(935,"3 · SWING")]
    for x,h in boxes: panel(s,x,175,420,490,h)
    # Stage 1: uniform rod hangs vertically from a top hinge.
    ox,oy=235,285; end1=(235,555); hit1=(235,420)
    s.dot(ox,oy,8,INK); s.line(ox-65,oy,ox+65,oy,INK,4)
    s.line(ox,oy,*end1,BLUE,8); s.text(255,335,"rod M,L",16,BLUE,95)
    s.dot(*hit1,6,RED); s.arrow(65,420,hit1[0]-18,420,ORANGE,3); s.text(90,390,"bullet m, v",15,ORANGE,100)
    s.line(205,oy,205,hit1[1],PURPLE,1.6,"dashed"); s.text(180,342,"d",16,PURPLE,25)
    # Stage 2: just after impact, the bullet is embedded and the rod rotates right.
    ox2,oy2=685,285; length=260; th=math.radians(18)
    end2=(ox2+length*math.sin(th),oy2+length*math.cos(th))
    hit2=(ox2+135*math.sin(th),oy2+135*math.cos(th))
    s.dot(ox2,oy2,8,INK); s.line(ox2-55,oy2,ox2+55,oy2,INK,4); s.line(ox2,oy2,*end2,BLUE,8)
    s.ellipse(hit2[0]-16,hit2[1]-16,32,32,ORANGE,PALE_ORANGE,2)
    arc(s,ox2,oy2,85,-math.pi/2,-math.pi/2+th,PURPLE,2.4); s.text(ox2+58,oy2+65,"ω",17,PURPLE,30)
    s.text(520,570,"m v d = I_total ω",17,GREEN,235)
    s.text(520,600,"I_total=ML²/3+md²",15,MUTED,205)
    # Stage 3: energy carries the combined system to its maximum angle.
    ox3,oy3=1135,285; thmax=math.radians(48); end3=(ox3+220*math.sin(thmax),oy3+220*math.cos(thmax))
    hit3=(ox3+135*math.sin(thmax),oy3+135*math.cos(thmax))
    s.dot(ox3,oy3,8,INK); s.line(ox3-55,oy3,ox3+55,oy3,INK,4); s.line(ox3,oy3,*end3,BLUE,8)
    s.ellipse(hit3[0]-16,hit3[1]-16,32,32,ORANGE,PALE_ORANGE,2)
    s.line(ox3,oy3,ox3,oy3+230,GRID,1.4,"dashed")
    arc(s,ox3,oy3,105,-math.pi/2,-math.pi/2+thmax,TEAL,2); s.text(ox3+55,oy3+72,"θ_max",15,TEAL,75)
    h_bottom=oy3+135; h_top=oy3+135*math.cos(thmax)
    s.arrow(ox3+110,h_bottom,ox3+110,h_top,PURPLE,2); s.text(ox3+121,h_top+7,"h rise",14,PURPLE,60)
    s.text(965,585,"½ I_total ω² = ΔU",17,GREEN,220)
    s.text(45,710,"The hinge impulse is external, but its moment about the hinge is zero during the short collision.",16,MUTED,1110)
    return s


def d91() -> Scene:
    s=Scene("D9.1"); s.title("Shell theorem: equal solid-angle cones cancel in opposite directions",
        "For an interior point P, opposite cone elements have equal dA/r²; their pulls are equal and opposite.")
    cx,cy,R=430,435,205; P=(cx+70,cy)
    s.ellipse(cx-R,cy-R,2*R,2*R,BLUE,"transparent",2.5); s.dot(cx,cy,6,INK)
    s.text(cx-22,cy+16,"O",14,MUTED,25)
    s.dot(*P,8,RED); s.text(P[0]+12,P[1]-12,"P",19,RED,30)
    # Two opposite infinitesimal cones from P intersect the shell in near/far patches.
    # Their boundary rays are collinear through P, so both patches subtend the same dΩ.
    def hit(alpha:float,direction:float)->tuple[float,float]:
        ux,uy=direction*math.cos(alpha),direction*math.sin(alpha)
        qx,qy=P[0]-cx,P[1]-cy; dot=qx*ux+qy*uy
        t=-dot+math.sqrt(dot*dot+R*R-qx*qx-qy*qy)
        return P[0]+t*ux,P[1]+t*uy
    near1=hit(.18,1); near2=hit(-.18,1)
    far1=hit(.18,-1); far2=hit(-.18,-1)
    for q in (near1,near2,far1,far2): s.line(*P,*q,GRID,1.4,"dashed")
    s.line(*near1,*near2,TEAL,5); s.line(*far1,*far2,PURPLE,8)
    s.text(565,308,"near patch dA₁",15,TEAL,130); s.text(180,308,"far patch dA₂",15,PURPLE,125)
    s.line(*P,cx+R,cy,ORANGE,2,"dashed"); s.text(638,450,"r₁",15,ORANGE,35)
    s.line(*P,cx-R,cy,ORANGE,2,"dashed"); s.text(160,450,"r₂>r₁",15,ORANGE,65)
    panel(s,950,200,365,415,"ONE dΩ, TWO DISTANCES")
    s.text(990,285,"dA₁/r₁² = dΩ / |cosα₁|",15,TEAL,300)
    s.text(990,345,"dA₂/r₂² = dΩ / |cosα₂|",15,PURPLE,300)
    s.text(990,415,"|cosα₁|=|cosα₂|",18,BLUE,260)
    s.text(990,465,"dF₁ = dF₂",24,GREEN,180)
    s.text(990,520,"Opposite pulls cancel. The projection\nfactor is essential to the argument.",15,MUTED,300)
    return s


def d92() -> Scene:
    s=Scene("D9.2"); s.title("Inside a uniform sphere g rises linearly; outside it falls as 1/r²",
        "A cavity field follows by superposing the full sphere with a negative-mass sphere.")
    panel(s,45,165,635,530,"FIELD OF A UNIFORM SPHERE")
    x0,y0,x1,y1=120,600,630,255
    axes(s,x0,y0,x1,y1,"r","g")
    Rpx=x0+230
    s.line(x0,y0,Rpx,y0-180,BLUE,3.4)
    pts=[]
    for i in range(1,36):
        r=1+3*i/35; x=Rpx+(x1-Rpx)*i/35; y=y0-180/(r*r)
        pts.append((x,y))
    polyline(s,[(Rpx,y0-180)]+pts,TEAL,3.2)
    s.line(Rpx,y0,Rpx,y0-210,GRID,1.2,"dashed")
    s.text(Rpx-15,y0+12,"R",15,INK,25); s.text(150,355,"g∝r",18,BLUE,65)
    s.text(445,340,"g∝1/r²",17,TEAL,90)
    s.text(125,630,"g(0)=0",14,MUTED,80); s.text(392,630,"GM/R²",14,MUTED,90)
    # Cavity panel: full sphere minus a displaced sphere.
    panel(s,715,165,635,530,"CAVITY BY SUPERPOSITION")
    cx,cy,R=930,425,170; c2=(cx+55,cy-8); r2=61
    s.ellipse(cx-R,cy-R,2*R,2*R,BLUE,PALE_BLUE,2.5)
    s.ellipse(c2[0]-r2,c2[1]-r2,2*r2,2*r2,RED,WHITE,2.2)
    s.dot(cx,cy,6,BLUE); s.text(cx-43,cy+15,"O",15,BLUE,25)
    s.dot(*c2,6,RED); s.text(c2[0]+9,c2[1]-20,"O′",15,RED,35)
    s.arrow(cx,cy,c2[0],c2[1],PURPLE,2.3); s.text(cx+19,cy-28,"a",16,PURPLE,25)
    s.arrow(1140,cy,1220,cy,TEAL,3.3); s.text(1160,cy+13,"g_cav",15,TEAL,70)
    s.text(1010,250,"g_cav = (4πGρ/3) a",18,GREEN,270)
    s.text(1010,535,"Uniform throughout the cavity;\ndirection follows O→O′.",16,MUTED,280)
    return s


def d93() -> Scene:
    s=Scene("D9.3"); s.title("Four distinct ways the local value of g changes",
        "Altitude, depth, latitude and spin rate have different curves and different mechanisms.")
    specs=[("ALTITUDE h/R", "g/g₀", "h/R", lambda x:1/(1+2*x)**2, BLUE, 0.0, 1.0,
             "farther from Earth"),
           ("DEPTH d/R", "g/g₀", "d/R", lambda x:1-x, TEAL, 0.0, 1.0,
             "zero at centre"),
           ("LATITUDE · sin²λ", "g_eff/g_pole", "sin²λ", lambda x:0.9966+0.0034*x, PURPLE, 0.996, 1.001,
             "centrifugal term fades poleward"),
           ("ROTATION · ω/ω_E", "g_eff/g_static", "ω/ω_E", lambda x:1-0.00345*x*x, RED, 0.996, 1.001,
             "centrifugal reduction ∝ω²")]
    for i,(head,ylab,xlab,fn,col,vmin,vmax,note) in enumerate(specs):
        x=45+(i%2)*675; y=150+(i//2)*300
        panel(s,x,y,630,270,head)
        xa,xb=x+75,x+570; ya,yb=y+215,y+64
        axes(s,xa,ya,xb,yb,xlab,ylab)
        pts=[]
        for j in range(41):
            q=j/40; val=fn(q)
            py=ya-(val-vmin)/(vmax-vmin)*(ya-yb)
            pts.append((xa+q*(xb-xa),py))
        polyline(s,pts,col,3)
        s.text(x+95,y+235,note,14,MUTED,350)
    s.text(75,748,"g(h)=g₀[R/(R+h)]²   ·   g(d)=g₀(1−d/R)   ·   g_eff≈g−ω²R cos²λ",16,INK,1200)
    return s


def d94() -> Scene:
    s=Scene("D9.4"); s.title("Kepler's equal-area law: equal times sweep equal areas",
        "The central force conserves angular momentum: periapsis sweeps a larger angle; apoapsis a smaller one.")
    cx,cy,a,b=590,430,310,270; c=math.sqrt(a*a-b*b); ecc=c/a; f=(cx+c,cy)
    pts=[(cx+a*math.cos(2*math.pi*i/180),cy-b*math.sin(2*math.pi*i/180)) for i in range(181)]
    polyline(s,pts,BLUE,3)
    s.dot(*f,10,ORANGE); s.text(f[0]-55,f[1]+20,"central mass",15,ORANGE,105)
    s.dot(cx,cy,4,GRID); s.text(cx-20,cy+15,"centre",14,MUTED,55)
    # Choose symmetric eccentric-anomaly intervals with exactly equal swept area.
    Eperi=.32; target=Eperi-ecc*math.sin(Eperi); lo,hi=0.0,Eperi
    for _ in range(50):
        mid=(lo+hi)/2
        if mid+ecc*math.sin(mid)<target: lo=mid
        else: hi=mid
    Eapo=(lo+hi)/2
    def sector(e0:float,e1:float,color:str,label:str):
        orbit=[]
        for k in range(25):
            E=e0+(e1-e0)*k/24
            orbit.append((cx+a*math.cos(E),cy-b*math.sin(E)))
        polygon=[f]+orbit+[f]
        hatch_polygon(s,polygon,color,9)
        polyline(s,orbit,color,3)
        s.line(*f,*orbit[0],color,1.5); s.line(*f,*orbit[-1],color,1.5)
        midpt=orbit[len(orbit)//2]
        s.text(midpt[0]-70,midpt[1]-32,label,14,color,160)
    sector(-Eperi,Eperi,TEAL,"periapsis · Δθ larger")
    sector(math.pi-Eapo,math.pi+Eapo,PURPLE,"apoapsis · Δθ smaller")
    s.arrow(f[0]+12,f[1]-18,cx+a-15,cy-18,ORANGE,2.5); s.text(f[0]+35,f[1]-43,"r_p",14,ORANGE,45)
    panel(s,985,235,340,360,"SAME Δt")
    s.text(1025,315,"ΔA₁ = ΔA₂",25,GREEN,240)
    s.text(1025,380,"dA/dt = L/(2m)",19,BLUE,250)
    s.text(1025,450,"r² dθ/dt = constant",17,PURPLE,270)
    s.text(1025,515,"Short radius → larger angular\nsweep; long radius → smaller.",15,MUTED,260)
    return s


def d95() -> Scene:
    s=Scene("D9.5"); s.title("Turning points are intersections with the effective potential",
        "Normalized per unit mass (GM=4): changing specific angular momentum ℓ moves the turning radii.")
    x0,y0,x1,y1=125,625,1035,250
    axes(s,x0,y0,x1,y1,"r","U_eff")
    # Three scaled curves with a centrifugal wall and a negative minimum.
    colors=[BLUE,TEAL,PURPLE]; labels=["ℓ₁", "ℓ₂", "ℓ₃"]
    params=[(.8,-2.6),(1.35,-1.15),(1.9,-1.0)]
    for j,(L,E) in enumerate(params):
        pts=[]
        for i in range(100):
            r=.34+8.4*i/99
            U=L*L/(2*r*r)-4/r
            U=max(-3.8,min(1.9,U))
            px=x0+(r/8.8)*(x1-x0); py=y0-((U+4.2)/6.5)*(y0-y1)
            pts.append((px,py))
        polyline(s,pts,colors[j],2.7)
        ey=y0-((E+4.2)/6.5)*(y0-y1)
        s.line(x0,ey,x1,ey,colors[j],1.6,"dashed")
        s.text(x1+15,ey-8,f"E{j+1}",14,colors[j],45)
        s.text(x0+25+j*105,y0+26,labels[j],15,colors[j],40)
        # Mark two roots of L²/(2r²)-4/r=E where they are positive and in range.
        disc=16+2*E*L*L
        if disc>=0 and E<0:
            roots=sorted(((-4-math.sqrt(disc))/(2*E),(-4+math.sqrt(disc))/(2*E)))
            for n,r in enumerate(roots):
                if 0<r<8.8:
                    px=x0+(r/8.8)*(x1-x0); s.dot(px,ey,5,RED)
                    s.text(px-20,y0-4,"rₚ" if n==0 else "rₐ",12,RED,35)
    s.text(1085,330,"same E?",14,MUTED,75)
    s.text(1085,365,"each L has its\nown turning radii",15,INK,145)
    s.text(125,680,"pericentre",14,RED,80); s.text(858,680,"apocentre",14,RED,85)
    s.text(105,730,"At a turning point radial speed is zero; angular momentum fixes the centrifugal barrier.",16,MUTED,1120)
    return s


def d96() -> Scene:
    s=Scene("D9.6"); s.title("Tides are the difference between near-side and far-side gravity",
        "Subtract Earth's centre acceleration: the near side is pulled toward the Moon, the far side away.")
    cx,cy,R=455,430,175; moon=(1000,430)
    # Tide-stretched Earth
    s.ellipse(cx-R,cy-R,2*R,2*R,BLUE,PALE_BLUE,2.5)
    s.ellipse(cx-R-17,cy-R+17,2*R+34,2*R-34,TEAL,"transparent",1.7)
    s.dot(cx,cy,6,INK); s.text(cx-22,cy+18,"Earth",16,INK,70)
    s.ellipse(moon[0]-58,moon[1]-58,116,116,PURPLE,"#eeeaf6",2.5)
    s.text(moon[0]-36,moon[1]-9,"Moon",17,PURPLE,72)
    # Lunar gravitational pulls point to the Moon, but differ in magnitude.
    s.arrow(cx+R+8,cy-65,cx+R+105,cy-65,ORANGE,3); s.text(cx+R+10,cy-96,"near: strong",14,ORANGE,130)
    s.arrow(cx+R,cy,cx+R+75,cy,ORANGE,2.7); s.text(cx+R+8,cy+12,"centre",13,MUTED,65)
    s.arrow(cx-R-8,cy+65,cx-R+38,cy+65,ORANGE,2); s.text(cx-R-115,cy+80,"far: weaker",14,ORANGE,110)
    # Differential pulls relative to Earth's centre.
    s.arrow(cx+R+8,cy+112,cx+R+83,cy+112,TEAL,3); s.text(cx+R+5,cy+122,"tidal →",14,TEAL,100)
    s.arrow(cx-R-8,cy-112,cx-R-75,cy-112,PURPLE,3); s.text(cx-R-108,cy-145,"← tidal",14,PURPLE,100)
    panel(s,815,195,505,435,"DIFFERENTIAL ACCELERATION")
    s.text(860,285,"Δg_near points toward Moon",18,TEAL,375)
    s.text(860,345,"Δg_far points away",18,PURPLE,320)
    s.text(860,415,"two tidal bulges",22,BLUE,260)
    s.text(860,485,"The common acceleration moves\nEarth and Moon together; its\nspatial gradient raises the tides.",16,MUTED,390)
    return s


def d97() -> Scene:
    s=Scene("D9.7"); s.title("Gauss's law inside a uniform sphere",
        "A concentric Gaussian surface encloses M(r/R)³; symmetry makes g constant on it.")
    cx,cy,R=430,420,200; r=120
    s.ellipse(cx-R,cy-R,2*R,2*R,BLUE,PALE_BLUE,2.5)
    s.ellipse(cx-r,cy-r,2*r,2*r,TEAL,PALE_TEAL,2.2)
    # Indicate enclosed mass as shaded interior and radial g arrows on Gaussian surface.
    for ang in [0,.7,1.4,2.1,2.8,3.5,4.2,4.9,5.6]:
        px=cx+r*math.cos(ang); py=cy-r*math.sin(ang)
        s.arrow(px,py,px+32*math.cos(ang),py-32*math.sin(ang),GREEN,2)
    s.text(cx-r+18,cy+8,"M_enc",16,TEAL,75); s.dot(cx,cy,5,INK)
    s.text(cx+R+8,cy-10,"R",16,BLUE,30); s.text(cx+r+5,cy+10,"r",16,TEAL,30)
    panel(s,760,195,555,440,"MASS ENCLOSED AND FLUX")
    s.text(815,285,"M_enc = M(r/R)³",23,TEAL,365)
    s.text(815,355,"∮g·dA = g·4πr²",22,GREEN,365)
    s.text(815,425,"g(r) = GMr/R³",23,BLUE,330)
    s.text(815,500,"All mass outside radius r forms\nspherical shells; each shell's\ninterior field is zero.",16,MUTED,405)
    return s


def d98() -> Scene:
    s=Scene("D9.8"); s.title("The orbital energy ladder: surface, circular orbit, escape",
        "The circular low-orbit energy is −GMm/(2R), so reaching it costs half the surface escape energy.")
    x0,x1=170,1190; levels=[(605,"surface",-2),(390,"low circular orbit",-1),(205,"escape",0)]
    s.line(x0,640,x1,640,GRID,1.5)
    for y,label,_ in levels:
        s.line(x0,y,x1,y,BLUE if y!=205 else GREEN,3)
        s.text(185,y-42,label,17,INK,220)
    s.text(865,580,"E₁=−GMm/R",19,BLUE,260)
    s.text(865,365,"E₂=−GMm/(2R)",19,TEAL,280)
    s.text(865,180,"E₃=0",19,GREEN,100)
    s.arrow(650,595,650,407,ORANGE,3); s.text(670,485,"ΔE=GMm/(2R)",18,ORANGE,240)
    s.arrow(815,380,815,220,PURPLE,3); s.text(835,275,"ΔE=GMm/(2R)",18,PURPLE,240)
    s.arrow(410,595,410,220,RED,2.5); s.text(265,385,"escape from surface:\nGMm/R",17,RED,190)
    s.text(325,705,"zero total energy is the marginal escape threshold",17,MUTED,640)
    return s


def d99() -> Scene:
    s=Scene("D9.9"); s.title("A Hohmann transfer is an ellipse tangent to both circular orbits",
        "Two tangential impulses change speed at periapsis and apoapsis; the coast is a Kepler ellipse.")
    cx,cy=560,440; r1,r2=145,270; a=(r1+r2)/2; e=(r2-r1)/(r2+r1)
    s.ellipse(cx-r2,cy-r2,2*r2,2*r2,GRID,"transparent",1.5)
    s.ellipse(cx-r1,cy-r1,2*r1,2*r1,TEAL,"transparent",2.2)
    # Transfer ellipse has the focus at the central body and periapsis to the right.
    ell=[]
    for i in range(101):
        nu=math.pi*i/100
        rr=a*(1-e*e)/(1+e*math.cos(nu))
        ell.append((cx+rr*math.cos(nu),cy-rr*math.sin(nu)))
    polyline(s,ell,ORANGE,3.2)
    s.dot(cx,cy,9,INK); s.text(cx-70,cy+16,"central mass",15,INK,100)
    s.dot(cx+r1,cy,7,TEAL); s.dot(cx-r2,cy,7,PURPLE)
    s.text(cx+r1-14,cy+20,"r₁",15,TEAL,30); s.text(cx-r2-35,cy+18,"r₂",15,PURPLE,35)
    # At periapsis velocities are upward for a counterclockwise orbit.
    s.arrow(cx+r1,cy,cx+r1,cy-78,BLUE,3); s.text(cx+r1+12,cy-77,"v_c1",14,BLUE,55)
    s.arrow(cx+r1,cy,cx+r1,cy-125,ORANGE,3); s.text(cx+r1+12,cy-122,"v_t1",14,ORANGE,55)
    s.arrow(cx-r2,cy,cx-r2,cy+39,BLUE,3); s.text(cx-r2-76,cy+22,"v_c2",14,BLUE,55)
    s.arrow(cx-r2,cy,cx-r2,cy+23,ORANGE,3); s.text(cx-r2-76,cy+50,"v_t2",14,ORANGE,55)
    s.text(990,250,"burn 1: speed up",16,ORANGE,170)
    s.text(990,295,"burn 2: circularise",16,BLUE,185)
    s.text(990,375,"transfer time = half\nthe ellipse's period",16,MUTED,225)
    return s


def d910() -> Scene:
    s=Scene("D9.10"); s.title("One effective-potential curve separates four orbit types",
        "Specific-energy units: U_eff=ℓ²/(2r²)−GM/r with GM=4, ℓ=√2; the circular orbit is the minimum.")
    x0,y0,x1,y1=175,590,1240,255
    axes(s,x0,y0,x1,y1,"r","U_eff")
    pts=[]
    for i in range(100):
        r=.17+7.8*i/99; U=1/r**2-4/r
        U=max(-4.4,min(7,U))
        px=x0+(r/8)*(x1-x0); py=y0-((U+4.6)/12)*(y0-y1)
        pts.append((px,py))
    polyline(s,pts,BLUE,3.2)
    # energy lines: minimum, bound, parabolic, hyperbolic
    energies=[(-4,"E_min · circular",GREEN),( -1,"E_min<E<0 · ellipse",TEAL),(0,"E=0 · parabola",ORANGE),(1,"E>0 · hyperbola",RED)]
    for E,label,col in energies:
        yy=y0-((E+4.6)/12)*(y0-y1)
        s.line(x0,yy,x1,yy,col,1.8,"dashed")
        s.text(850,yy-24,label,15,col,245)
    r0=.5; px=x0+(r0/8)*(x1-x0); py=y0-((-4+4.6)/12)*(y0-y1)
    s.dot(px,py,7,PURPLE); s.line(px,py,px,y0,GRID,1,"dashed"); s.text(px-14,y0+10,"r₀",15,PURPLE,30)
    # E=-1 roots are the two radial turning points.
    for r,label in [(2-math.sqrt(3),"r_min"),(2+math.sqrt(3),"r_max")]:
        qx=x0+(r/8)*(x1-x0); qy=y0-((-1+4.6)/12)*(y0-y1)
        s.dot(qx,qy,5,RED)
    s.text(300,665,"two turning radii",15,RED,150)
    return s


def d911() -> Scene:
    s=Scene("D9.11"); s.title("The five Lagrange points in the rotating Sun–Earth frame",
        "L1, L2 and L3 lie on the line of centres; L4 and L5 complete equilateral triangles.")
    sun=(490,430); earth=(865,430); r=375
    s.ellipse(sun[0]-r,sun[1]-r,2*r,2*r,GRID,"transparent",1.4)
    s.line(sun[0]-r,sun[1],sun[0]+r,sun[1],GRID,1.2,"dashed")
    s.ellipse(sun[0]-42,sun[1]-42,84,84,ORANGE,PALE_ORANGE,2.5); s.text(sun[0]-27,sun[1]-8,"Sun",17,ORANGE,55)
    s.ellipse(earth[0]-25,earth[1]-25,50,50,BLUE,PALE_BLUE,2.5); s.text(earth[0]-35,earth[1]+37,"Earth",15,BLUE,65)
    pts={"L1":(833,430),"L2":(906,430),"L3":(sun[0]-r,430),
         "L4":(sun[0]+r/2,430-r*math.sqrt(3)/2),
         "L5":(sun[0]+r/2,430+r*math.sqrt(3)/2)}
    for label,p in pts.items():
        s.dot(*p,8,PURPLE)
        dx=12 if label in ("L1","L2","L4") else -45
        dy=-25 if label not in ("L5",) else 10
        s.text(p[0]+dx,p[1]+dy,label,17,PURPLE,45)
    s.line(sun[0],sun[1],pts["L4"][0],pts["L4"][1],TEAL,1.5,"dashed")
    s.line(earth[0],earth[1],pts["L4"][0],pts["L4"][1],TEAL,1.5,"dashed")
    s.line(sun[0],sun[1],pts["L5"][0],pts["L5"][1],TEAL,1.5,"dashed")
    s.line(earth[0],earth[1],pts["L5"][0],pts["L5"][1],TEAL,1.5,"dashed")
    s.text(960,275,"L4/L5 are ±60°\nfrom the Sun–Earth line",17,TEAL,260)
    s.text(960,360,"L1: between the bodies",15,MUTED,225)
    s.text(960,400,"L2: beyond Earth",15,MUTED,200)
    s.text(960,440,"L3: opposite the Sun",15,MUTED,220)
    s.text(960,530,"Rotating frame: each point\nco-rotates with Earth.",16,INK,240)
    return s


def d912() -> Scene:
    s=Scene("D9.12"); s.title("A gravity assist trades the planet's orbital energy with the spacecraft",
        "In Jupiter's frame the asymptotic speed is unchanged; vector addition in the Sun frame can raise it.")
    panel(s,45,165,620,510,"JUPITER FRAME")
    j=(355,420); s.ellipse(j[0]-45,j[1]-45,90,90,PURPLE,"#eeeaf6",2.5); s.text(j[0]-34,j[1]-8,"Jupiter",14,PURPLE,70)
    # Hyperbolic flyby path bends the relative velocity direction.
    path=[(90,300),(175,320),(245,360),(285,418),(300,475),(350,505),(425,500),(510,465),(585,430)]
    polyline(s,path,TEAL,3)
    s.arrow(175,320,260,385,BLUE,3); s.text(150,275,"u_in",16,BLUE,55)
    s.arrow(470,480,555,445,GREEN,3); s.text(520,485,"u_out",16,GREEN,65)
    s.text(100,560,"|u_in| = |u_out|",18,INK,200)
    s.text(100,600,"direction changes, speed does not",15,MUTED,260)
    panel(s,705,165,645,510,"SUN FRAME · VELOCITIES ADD")
    ox,oy=790,555; scale=65
    # Planet velocity points right; choose a turn with positive Δu along V_J.
    s.arrow(ox,oy,ox+150,oy,ORANGE,3.5); s.text(ox+50,oy+12,"V_J",17,ORANGE,55)
    # Initial velocity resultant and relative vector triangle.
    i_end=(ox+150-95,oy-90); f_end=(ox+150+95,oy-90)
    s.arrow(ox,oy,*i_end,BLUE,3); s.text(i_end[0]-35,i_end[1]-30,"v_in=V_J+u_in",15,BLUE,140)
    s.arrow(ox,oy,*f_end,GREEN,3); s.text(f_end[0]-25,f_end[1]-30,"v_out=V_J+u_out",15,GREEN,150)
    s.line(ox+150,oy,*i_end,BLUE,2,"dashed"); s.line(ox+150,oy,*f_end,GREEN,2,"dashed")
    s.text(790,270,"|u_in|=|u_out|",16,INK,180)
    s.text(790,320,"v_out²−v_in² = 2V_J·(u_out−u_in)",16,PURPLE,450)
    s.text(790,390,"gain case: Δu has a component\nalong Jupiter's motion",16,TEAL,350)
    s.text(790,635,"The tiny energy gained by the spacecraft is lost by the planet's orbit.",15,MUTED,510)
    return s


def d101() -> Scene:
    s=Scene("D10.1"); s.title("In SHM, displacement, velocity and acceleration are phase-shifted sinusoids",
        "With x=A sin(ωt), velocity leads x by π/2 and acceleration is opposite to x.")
    rows=[("x/A",BLUE,lambda t:math.sin(t)),
          ("v/(Aω)",TEAL,lambda t:math.cos(t)),
          ("a/(Aω²)",RED,lambda t:-math.sin(t))]
    for i,(label,color,fn) in enumerate(rows):
        y=185+i*178; x0,x1=180,1250; base=y+88; amp=56
        s.line(x0,base,x1,base,GRID,1.2); s.line(x0,y+10,x0,y+153,INK,1.5)
        pts=[]
        for j in range(121):
            t=2*math.pi*j/120; px=x0+(x1-x0)*j/120; py=base-amp*fn(t)
            pts.append((px,py))
        polyline(s,pts,color,3)
        s.text(60,y+64,label,17,color,110)
        for q,lab in [(0,"0"),(math.pi/2,"π/2"),(math.pi,"π"),(3*math.pi/2,"3π/2"),(2*math.pi,"2π")]:
            px=x0+(x1-x0)*q/(2*math.pi); s.line(px,base-5,px,base+5,GRID,1)
            if i==2: s.text(px-17,base+12,lab,12,MUTED,45)
    s.text(850,155,"v leads x by 90°",16,TEAL,180)
    s.text(850,505,"a is 180° out of phase with x",16,RED,245)
    return s


def d102() -> Scene:
    s=Scene("D10.2"); s.title("One rotating phasor generates all three SHM variables",
        "The vertical projection is x; v is a quarter-turn ahead and a points opposite x.")
    cx,cy,R=430,445,205; phi=math.radians(48)
    P=(cx+R*math.cos(phi),cy-R*math.sin(phi)); proj=(cx,P[1])
    s.ellipse(cx-R,cy-R,2*R,2*R,GRID,"transparent",2)
    s.line(cx-R-30,cy,cx+R+40,cy,GRID,1.5); s.line(cx,cy-R-35,cx,cy+R+35,GRID,1.5)
    s.dot(cx,cy,6,INK); s.line(cx,cy,*P,BLUE,4); s.dot(*P,8,BLUE)
    s.text(P[0]+8,P[1]-22,"A",17,BLUE,30)
    s.line(*P,*proj,TEAL,2,"dashed"); s.dot(*proj,6,TEAL)
    s.text(cx+10,P[1]+8,"x=A sinφ",16,TEAL,120)
    # velocity phasor is rotated +90°; acceleration points opposite x-phasor.
    V=(cx+115*math.cos(phi+math.pi/2),cy-115*math.sin(phi+math.pi/2))
    s.arrow(cx,cy,*V,PURPLE,3.1); s.text(V[0]-85,V[1]-20,"v phasor",15,PURPLE,100)
    A=(cx-145*math.cos(phi),cy+145*math.sin(phi))
    s.arrow(cx,cy,*A,RED,3); s.text(A[0]-25,A[1]+8,"a",17,RED,30)
    arc(s,cx,cy,70,0,phi,ORANGE,2); s.text(cx+52,cy-42,"φ=ωt",15,ORANGE,65)
    panel(s,800,205,500,390,"PHASE RELATIONS")
    s.text(850,295,"x = A sinφ",23,BLUE,280)
    s.text(850,365,"v = Aω cosφ",23,PURPLE,310)
    s.text(850,435,"a = −Aω² sinφ",23,RED,330)
    s.text(850,515,"v leads x by π/2; a is antiparallel to x.",16,MUTED,395)
    return s


def d103() -> Scene:
    s=Scene("D10.3"); s.title("Kinetic and potential energy trade as the oscillator moves",
        "For amplitude A, total energy E=½kA² is constant between the turning points.")
    x0,y0,x1,y1=190,610,1220,230
    axes(s,x0,y0,x1,y1,"x/A","energy / E")
    # x/A from -1 to 1; map x coordinate to graph interval.
    def X(q): return x0+(q+1)*(x1-x0)/2
    U=[]; K=[]
    for i in range(101):
        q=-1+2*i/100; px=X(q); pyU=y0-(q*q)*(y0-y1); pyK=y0-(1-q*q)*(y0-y1)
        U.append((px,pyU)); K.append((px,pyK))
    polyline(s,U,BLUE,3.4); polyline(s,K,RED,3.4)
    s.line(x0,y1,x1,y1,GREEN,2.4,"dashed")
    for q in (-1,0,1):
        px=X(q); s.line(px,y0,px,y0+8,GRID,1.3); s.text(px-13,y0+13,str(q),13,MUTED,30)
    s.text(980,310,"E=U+K=constant",17,GREEN,190)
    s.text(1040,410,"U=½kx²",17,BLUE,110); s.text(1040,500,"K=E−U",17,RED,100)
    s.dot(X(-1),y1,6,BLUE); s.dot(X(1),y1,6,BLUE); s.dot(X(0),y0,6,BLUE)
    s.text(350,678,"turning points: K=0",15,MUTED,220); s.text(600,678,"equilibrium: U=0, K=E",15,MUTED,240)
    return s


def d104() -> Scene:
    s=Scene("D10.4"); s.title("Springs in series soften; springs in parallel stiffen",
        "Series: the same force acts and extensions add. Parallel: the same extension acts and forces add.")
    panel(s,45,160,620,500,"SERIES · same F, extensions add")
    panel(s,735,160,620,500,"PARALLEL · same x, forces add")
    # End-to-end springs with a light connector and a load at the free end.
    s.line(150,280,150,440,INK,5)
    spring(s,(150,360),(285,360),BLUE); s.dot(285,360,4,INK)
    spring(s,(285,360),(420,360),TEAL)
    s.rect(420,330,52,60,BLUE,PALE_BLUE,2); s.text(438,348,"m",15,INK,25)
    s.arrow(473,360,555,360,ORANGE,2.8); s.text(505,329,"F",16,ORANGE,25)
    s.text(190,315,"k₁",16,BLUE,35); s.text(333,315,"k₂",16,TEAL,35)
    s.arrow(174,405,273,405,PURPLE,1.8); s.text(200,412,"x₁",14,PURPLE,35)
    s.arrow(303,405,405,405,PURPLE,1.8); s.text(330,412,"x₂",14,PURPLE,35)
    s.text(135,550,"1/k_eq=1/k₁+1/k₂",18,GREEN,345)
    s.text(135,590,"F₁=F₂=F;  x=x₁+x₂",16,INK,270)
    # Parallel springs share both a fixed support and a movable bar.
    s.line(820,285,820,525,INK,5); s.line(1220,285,1220,525,INK,5)
    spring(s,(820,340),(1220,340),BLUE,turns=8,amp=13); spring(s,(820,465),(1220,465),TEAL,turns=8,amp=13)
    s.line(1220,300,1220,505,INK,5); s.text(930,295,"k₁",16,BLUE,35); s.text(930,420,"k₂",16,TEAL,35)
    s.arrow(1245,390,1320,390,ORANGE,2.8); s.text(1270,360,"F₁+F₂",15,ORANGE,70)
    s.text(825,550,"k_eq=k₁+k₂",18,GREEN,260)
    s.text(825,590,"x₁=x₂=x",17,INK,190)
    return s


def d105() -> Scene:
    s=Scene("D10.5"); s.title("A pendulum's tangential weight component restores it toward equilibrium",
        "Only for small θ does sinθ≈θ, making the arc-coordinate force linear in displacement.")
    pivot=(465,205); L=270; th=math.radians(36); bob=(pivot[0]+L*math.sin(th),pivot[1]+L*math.cos(th))
    s.dot(*pivot,8,INK); s.line(pivot[0],pivot[1],pivot[0],pivot[1]+L+40,GRID,1.3,"dashed")
    s.line(*pivot,*bob,INK,3.5); s.ellipse(bob[0]-29,bob[1]-29,58,58,BLUE,PALE_BLUE,2.5)
    s.text(bob[0]+34,bob[1]+3,"m",17,BLUE,35)
    arc(s,pivot[0],pivot[1],85,math.pi/2-th,math.pi/2,TEAL,2.4)
    s.text(pivot[0]+29,pivot[1]+95,"θ",18,TEAL,30); s.text(365,315,"L",18,INK,25)
    s.arrow(bob[0],bob[1]+22,bob[0],bob[1]+132,RED,3.2); s.text(bob[0]+12,bob[1]+87,"mg",16,RED,45)
    # Tension points toward pivot; tangential restoring component up-left along arc.
    s.arrow(bob[0]-10,bob[1]-5,pivot[0]+35,pivot[1]+70,PURPLE,2.8); s.text(590,405,"T",16,PURPLE,25)
    tan=(-math.cos(th),math.sin(th)); s.arrow(bob[0],bob[1],bob[0]+tan[0]*115,bob[1]+tan[1]*115,GREEN,3)
    s.text(bob[0]-115,bob[1]+95,"−mg sinθ",16,GREEN,110)
    panel(s,780,205,530,395,"SMALL-ANGLE LIMIT")
    s.text(835,295,"x=Lθ",24,BLUE,170)
    s.text(835,355,"F_t=−mg sinθ",22,GREEN,280)
    s.text(835,415,"≈−mgθ=−(mg/L)x",21,PURPLE,360)
    s.text(835,485,"k_eff=mg/L",20,ORANGE,220)
    s.text(835,540,"The linear restoring law is a local approximation.",16,MUTED,400)
    return s


def d106() -> Scene:
    s=Scene("D10.6"); s.title("Lissajous figures encode frequency ratio and phase difference",
        "x=sin(ωx t), y=sin(ωy t+δ); changing the ratio or δ changes the closed curve.")
    ratios=[1,2,3]; phases=[0,math.pi/4,math.pi/2]
    for row,ratio in enumerate(ratios):
        for col,delta in enumerate(phases):
            x=35+col*455; y=135+row*207; panel(s,x,y,430,185,f"ωy/ωx={ratio}  ·  δ={['0','π/4','π/2'][col]}")
            xa,ya=x+215,y+111; scale=61
            s.line(x+100,ya,x+330,ya,GRID,1); s.line(xa,y+60,xa,y+166,GRID,1)
            pts=[]
            for i in range(361):
                t=2*math.pi*i/360
                xx=math.sin(t); yy=math.sin(ratio*t+delta)
                pts.append((xa+scale*xx,ya-scale*yy))
            polyline(s,pts,BLUE if row==0 else TEAL if row==1 else PURPLE,2.4)
    return s


def d107() -> Scene:
    s=Scene("D10.7"); s.title("Damping lowers and broadens the resonance peak",
        "The driven amplitude peaks near ω₀; stronger damping shifts the peak slightly below ω₀.")
    x0,y0,x1,y1=180,640,1225,220
    axes(s,x0,y0,x1,y1,"ω/ω₀","A (scaled)")
    curves=[(.08,BLUE,"light · Q≈6.25"),(.22,TEAL,"medium"),(.48,PURPLE,"heavy")]
    maxA=6.0
    for zeta,color,label in curves:
        pts=[]
        for i in range(161):
            r=2.0*i/160
            A=1/math.sqrt((1-r*r)**2+(2*zeta*r)**2)
            A=min(maxA,A)
            pts.append((x0+r/2*(x1-x0),y0-A/maxA*(y0-y1)))
        polyline(s,pts,color,3)
    # ω0 reference and approximate peak shift for the three dampings.
    xw=x0+.5*(x1-x0); s.line(xw,y0,xw,y1,GRID,1.4,"dashed"); s.text(xw-20,y0+10,"ω₀",15,INK,40)
    s.text(905,270,"light damping: sharp, tall peak",15,BLUE,250)
    s.text(905,305,"heavy damping: broad, low peak",15,PURPLE,250)
    s.text(905,340,"Q=ω₀/(2γ)",18,GREEN,160)
    s.text(905,380,"ω_peak<ω₀ when damping is finite",15,MUTED,275)
    return s


def d108() -> Scene:
    s=Scene("D10.8"); s.title("Coupled pendulums have in-phase and out-of-phase normal modes",
        "For equal bobs, the spring is relaxed in the in-phase mode and stretched in the out-of-phase mode.")
    panel(s,50,175,620,480,"IN PHASE · spring relaxed")
    panel(s,730,175,620,480,"OUT OF PHASE · spring stretched")
    for x0,mode,color in [(170,"ω_in=√(g/L)",BLUE),(850,"ω_out=√(g/L+2k/m)",PURPLE)]:
        ceiling_y=275; pivots=[x0,x0+310]; L=205; bob_centres=[]
        for j,p in enumerate(pivots):
            th=math.radians(25 if mode.startswith("ω_in") or j==0 else -25)
            bob=(p+L*math.sin(th),ceiling_y+L*math.cos(th)); bob_centres.append(bob)
            s.dot(p,ceiling_y,5,INK); s.line(p,ceiling_y,*bob,INK,2.5)
            s.ellipse(bob[0]-25,bob[1]-25,50,50,color,PALE_BLUE,2)
        # Link the bobs: common-mode displacement leaves their separation unchanged;
        # opposite displacements stretch the coupling spring.
        if mode.startswith("ω_in"):
            s.line(*bob_centres[0],*bob_centres[1],GRID,2,"dashed")
        else:
            spring(s,bob_centres[0],bob_centres[1],ORANGE,turns=7,amp=9)
        s.text(x0-20,560,mode,17,GREEN if mode.startswith("ω_in") else PURPLE,260)
    s.text(235,610,"x₁=x₂",17,BLUE,90); s.text(935,610,"x₁=−x₂",17,PURPLE,95)
    return s


def d109() -> Scene:
    s=Scene("D10.9"); s.title("An SHM state traces an ellipse in velocity–displacement space",
        "The x–v ellipse has semiaxes A and Aω; its area is πA²ω=2πE/(mω).")
    x0,y0,x1,y1=250,455,1010,245
    s.arrow(x0,y0,x1,y0,INK,1.8); s.arrow(x0,y0,x0,y1,INK,1.8)
    s.text(x1-10,y0+10,"x",16,INK,25); s.text(x0-25,y1-18,"v",16,INK,25)
    A=300; V=155; cx=(x0+x1)/2; cy=y0
    pts=[(cx+A*math.cos(2*math.pi*i/240),cy-V*math.sin(2*math.pi*i/240)) for i in range(241)]
    polyline(s,pts,BLUE,3.2)
    s.line(cx-A,cy,cx+A,cy,GRID,1.3,"dashed"); s.line(cx,cy-V,cx,cy+V,GRID,1.3,"dashed")
    s.text(cx-A-12,cy+10,"−A",14,MUTED,35); s.text(cx+A-8,cy+10,"A",14,MUTED,25)
    s.text(cx+10,cy-V-8,"Aω",14,MUTED,45)
    s.dot(cx+A*.55,cy-V*.84,7,TEAL); s.text(cx+A*.55+10,cy-V*.84-22,"one oscillator state",15,TEAL,145)
    panel(s,1040,220,300,390,"ENERGY")
    s.text(1075,315,"E=½mω²A²",20,GREEN,220)
    s.text(1075,380,"area(x,v)",18,BLUE,145)
    s.text(1075,425,"=πA²ω",19,BLUE,150)
    s.text(1075,480,"=2πE/(mω)",18,PURPLE,190)
    s.text(1075,545,"For canonical phase space (x,p),\narea=2πE/ω.",15,MUTED,240)
    return s


def d1010() -> Scene:
    s=Scene("D10.10"); s.title("A ballistic pendulum has two distinct conservation stages",
        "Momentum/angular momentum applies during impact; mechanical energy applies during the later swing.")
    xs=[45,490,935]; headings=["1 · APPROACH","2 · EMBED","3 · SWING UP"]
    for x,h in zip(xs,headings): panel(s,x,165,415,500,h)
    # stage 1 block suspended from a string
    s.line(315,245,315,350,INK,3); s.rect(280,350,70,70,BLUE,PALE_BLUE,2,True)
    s.arrow(95,385,260,385,ORANGE,3.2); s.text(105,350,"bullet m, speed v",15,ORANGE,145)
    s.text(118,470,"block M at rest",15,BLUE,120)
    # stage 2 embedded body at bottom
    s.line(700,245,700,350,INK,3); s.rect(665,350,70,70,BLUE,PALE_BLUE,2,True)
    s.ellipse(710,360,25,25,ORANGE,PALE_ORANGE,1.8)
    s.arrow(750,380,845,380,TEAL,2.8); s.text(750,400,"V₀",15,TEAL,40)
    s.text(520,490,"mv=(M+m)V₀",17,GREEN,205)
    s.text(520,525,"about pivot: m v L",15,PURPLE,180)
    # stage 3 swings to height h
    piv=(1105,245); bob=(1215,415)
    s.dot(*piv,6,INK); s.line(piv[0],piv[1],piv[0],435,GRID,1.3,"dashed")
    s.line(*piv,*bob,INK,3); s.rect(bob[0]-34,bob[1]-34,68,68,BLUE,PALE_BLUE,2,True)
    s.ellipse(bob[0]+10,bob[1]-18,24,24,ORANGE,PALE_ORANGE,1.8)
    s.arrow(1270,435,1270,330,PURPLE,2.5); s.text(1280,365,"h",16,PURPLE,25)
    s.text(965,530,"½(M+m)V₀²=(M+m)gh",17,GREEN,330)
    s.text(45,710,"The swing's rise determines the speed immediately after the inelastic collision.",16,MUTED,950)
    return s


def d1011() -> Scene:
    s=Scene("D10.11"); s.title("A real pendulum's period grows with release amplitude",
        "The small-angle value T₀ is approached near zero; the period diverges as θ₀→180°.")
    x0,y0,x1,y1=190,625,1230,225
    axes(s,x0,y0,x1,y1,"θ₀","T/T₀")
    def agm(a:float,b:float)->float:
        for _ in range(30):
            a,b=(a+b)/2,math.sqrt(a*b)
        return (a+b)/2
    pts=[]
    for i in range(150):
        deg=170*i/149; half=math.radians(deg/2)
        # Exact period ratio for an ideal pendulum: T/T0=1/AGM(1,cos(theta0/2)).
        T=1/agm(1,math.cos(half))
        pts.append((x0+deg/180*(x1-x0),y0-(T-1)/2.25*(y0-y1)))
    polyline(s,pts,BLUE,3.2)
    s.line(x0,y0,x1,y0,GRID,1,"dashed")
    for deg,T,label in [(0,1,"1"),(90,1.18,"≈1.18"),(170,2.44,"≈2.44")]:
        px=x0+deg/180*(x1-x0); py=y0-(T-1)/2.25*(y0-y1)
        s.dot(px,py,6,RED); s.text(px-25,py-28,label,14,RED,60)
    s.text(230,665,"linear SHM limit",15,MUTED,130); s.text(920,285,"near-separatrix growth",15,PURPLE,180)
    return s


def d1012() -> Scene:
    s=Scene("D10.12"); s.title("A torsion pendulum is SHM in angle",
        "A twisted wire supplies restoring torque τ=−κφ, giving T=2π√(I/κ).")
    # suspended disk with a torsion wire
    s.line(430,190,430,405,INK,4); s.rect(414,180,32,18,INK,INK,1)
    s.ellipse(310,405,240,92,BLUE,PALE_BLUE,3)
    s.ellipse(410,430,40,40,TEAL,PALE_TEAL,2)
    s.text(392,480,"disk I",17,BLUE,75)
    s.arrow(580,445,650,445,ORANGE,3); s.text(595,413,"twist φ",16,ORANGE,80)
    arc(s,430,450,105,.1,1.15,PURPLE,2.8)
    s.arrow(540,447,482,420,GREEN,3); s.text(505,397,"restoring τ",15,GREEN,105)
    panel(s,760,205,530,390,"ANGULAR OSCILLATOR")
    s.text(815,295,"τ=−κφ",26,GREEN,210)
    s.text(815,360,"I φ¨ + κφ = 0",23,BLUE,310)
    s.text(815,430,"ω=√(κ/I)",22,PURPLE,240)
    s.text(815,495,"T=2π√(I/κ)",23,ORANGE,260)
    return s


def d111() -> Scene:
    s=Scene("D11.1"); s.title("Pressure is continuous at a density interface; its slope changes",
        "With depth positive downward, dp/dh=ρg; the denser lower layer gives the steeper p(h) segment.")
    # Two-layer vessel
    xL,xR=170,520; top=210; interface=430; bottom=650
    s.line(xL,top,xL,bottom,INK,4); s.line(xR,top,xR,bottom,INK,4); s.line(xL,bottom,xR,bottom,INK,4)
    s.line(xL,interface,xR,interface,GRID,1.5,"dashed")
    s.rect(xL+3,top+4,xR-xL-6,interface-top-4,"transparent",PALE_BLUE,1)
    s.rect(xL+3,interface,xR-xL-6,bottom-interface,"transparent",PALE_TEAL,1)
    s.text(xL+35,top+65,"ρ₁",19,BLUE,40); s.text(xL+35,interface+85,"ρ₂>ρ₁",19,TEAL,85)
    s.text(xR+12,interface-8,"h₁",15,INK,35); s.text(xR+12,bottom-8,"h₂",15,INK,35)
    s.text(100,top-28,"surface p₀",15,INK,100)
    # p horizontal, depth h downward
    panel(s,690,175,655,520,"p vs depth h")
    xa,ya=790,245; xb,yb=1275,620
    s.arrow(xa,ya,xb,ya,INK,1.8); s.arrow(xa,ya,xa,yb,INK,1.8)
    s.text(xb-5,ya-25,"p",16,INK,25); s.text(xa-25,yb-5,"h ↓",15,INK,45)
    pts=[(xa,ya),(xa+175,ya+160),(xa+420,ya+370)]
    polyline(s,pts,BLUE,3.2); s.dot(*pts[1],6,RED)
    s.text(xa+185,ya+138,"interface: p continuous",14,RED,180)
    s.text(xa+55,ya+60,"slope set by ρ₁",14,BLUE,135)
    s.text(xa+300,ya+300,"steeper: ρ₂g",14,TEAL,110)
    s.text(150,708,"p(h)=p₀+ρ₁gh₁+ρ₂g(h−h₁) below the interface",17,GREEN,580)
    return s


def d112() -> Scene:
    s=Scene("D11.2"); s.title("Hydrostatic pressure at a base depends on depth, not vessel shape",
        "Equal free-surface heights give equal bottom pressure; the walls carry the differing weight of liquid.")
    base_y=610; widths=[205,205,205]; xs=[175,600,1025]
    shapes=[[(0,0),(205,0),(205,260),(0,260)],
            [(0,0),(205,0),(175,260),(30,260)],
            [(75,0),(130,0),(205,260),(0,260)]]
    labels=["cylinder","narrows upward","widens upward"]
    for x,poly,label in zip(xs,shapes,labels):
        pts=[(x+dx,base_y-dy) for dx,dy in poly]
        polyline(s,pts+pts[:1],BLUE,3)
        surf=base_y-205
        s.line(x+8,surf,x+197,surf,TEAL,1.5,"dashed")
        s.line(x-20,base_y,x+225,base_y,INK,4)
        s.arrow(x+102,base_y-8,x+102,base_y-110,PURPLE,2.5)
        s.text(x+34,base_y+20,label,15,INK,150)
        s.text(x+55,base_y-182,"same h",13,TEAL,75)
        s.text(x+53,base_y-35,"p₀+ρgh",14,PURPLE,90)
    # Side-wall force components highlighted on widening vessel.
    s.arrow(788,450,814,500,ORANGE,2.5); s.arrow(850,450,824,500,ORANGE,2.5)
    s.text(770,400,"wall forces",14,ORANGE,100)
    s.text(330,170,"A₁",16,BLUE,35); s.text(760,170,"A₂",16,BLUE,35); s.text(1180,170,"A₃",16,BLUE,35)
    s.text(370,720,"p_bottom=p₀+ρgh in all three",19,GREEN,430)
    return s


def d113() -> Scene:
    s=Scene("D11.3"); s.title("A hydraulic press trades displacement for force",
        "Pascal's law multiplies force by A/a, while incompressibility makes the large piston move less.")
    # Narrow and wide pistons are connected by one fluid-filled lower passage.
    s.line(270,245,270,445,INK,5); s.line(330,245,330,445,INK,5)
    s.line(520,225,520,445,INK,5); s.line(660,225,660,445,INK,5)
    s.line(270,445,660,445,INK,5)
    s.rect(270,222,60,25,BLUE,PALE_BLUE,2); s.rect(520,202,140,25,TEAL,PALE_TEAL,2)
    s.line(270,247,270,430,BLUE,2); s.line(330,247,330,430,BLUE,2)
    s.line(520,227,520,430,TEAL,2); s.line(660,227,660,430,TEAL,2)
    s.line(330,430,520,430,BLUE,2)
    s.arrow(300,170,300,220,ORANGE,3); s.text(230,145,"F₁ down",16,ORANGE,90)
    s.arrow(590,270,590,207,GREEN,3); s.text(605,230,"F₂ up",16,GREEN,80)
    s.text(272,260,"area a",14,BLUE,65); s.text(525,240,"area A≫a",14,TEAL,95)
    s.line(340,265,340,365,GRID,1.4,"dashed"); s.line(675,245,675,365,GRID,1.4,"dashed")
    s.text(345,310,"d₁",15,BLUE,35); s.text(680,292,"d₂",15,TEAL,35)
    panel(s,745,200,545,415,"CONSERVATION OF VOLUME + WORK")
    s.text(800,290,"a d₁ = A d₂",23,BLUE,260)
    s.text(800,360,"F₁/a = F₂/A",23,TEAL,280)
    s.text(800,430,"F₂=F₁ A/a",26,GREEN,250)
    s.text(800,500,"F₁d₁ = F₂d₂",23,PURPLE,280)
    return s


def d114() -> Scene:
    s=Scene("D11.4"); s.title("Resolve the force on a curved gate by projecting the surface",
        "The horizontal component uses the vertical projection; the vertical component is the weight of water above.")
    panel(s,40,175,630,485,"HORIZONTAL COMPONENT")
    # quarter-circle gate with water on left
    cx,cy,R=460,565,200
    pts=[(cx-R,cy)]+[(cx-R*math.cos(math.pi*i/32),cy-R*math.sin(math.pi*i/32)) for i in range(33)]
    polyline(s,pts,BLUE,5)
    s.line(cx-R,cy,cx,cy,BLUE,5); s.line(cx-R,cy-R,cx-R,cy,INK,2,"dashed")
    for y in [390,440,490,540]: s.arrow(cx-R-110,y,cx-R-12,y,TEAL,2.1)
    s.text(90,285,"water pressure",15,TEAL,150)
    s.arrow(cx-R-60,470,cx-R-60,555,PURPLE,3); s.text(cx-R-50,510,"F_H",17,PURPLE,50)
    s.text(280,610,"curved gate",15,BLUE,120)
    s.text(72,630,"F_H = force on vertical projection",15,GREEN,275)
    panel(s,710,175,640,485,"VERTICAL COMPONENT + RESULTANT")
    # water column over the curved gate
    s.rect(840,300,190,245,GRID,PALE_BLUE,1.5)
    s.ellipse(1050,420,150,150,BLUE,"transparent",4)
    s.line(1050,495,1200,495,BLUE,4); s.line(1050,495,1050,420,BLUE,4)
    s.arrow(930,315,930,505,RED,3); s.text(945,410,"W_water",16,RED,85)
    s.dot(1125,495,7,INK); s.text(1135,500,"hinge",14,INK,50)
    s.arrow(1125,495,1260,495,TEAL,3); s.text(1190,465,"F_H",15,TEAL,45)
    s.arrow(1125,495,1125,585,PURPLE,3); s.text(1138,530,"F_V",15,PURPLE,45)
    s.arrow(1125,495,1210,580,GREEN,3); s.text(1210,580,"F",17,GREEN,30)
    s.text(755,610,"F_V = weight of imaginary water above gate (downward)",14,GREEN,430)
    return s


def d115() -> Scene:
    s=Scene("D11.5"); s.title("A rotating liquid settles into a paraboloid",
        "The free-surface slope balances centrifugal acceleration horizontally against gravity vertically.")
    # cylindrical vessel cross-section and parabolic surface
    s.line(145,260,145,650,INK,4); s.line(715,260,715,650,INK,4); s.line(145,650,715,650,INK,4)
    pts=[]
    for i in range(61):
        r=-1+2*i/60; pts.append((430+250*r,455-150*r*r))
    polyline(s,pts,BLUE,4)
    s.text(350,300,"z=z₀+ω²r²/(2g)",18,BLUE,230)
    # fluid element at radius r
    p=(570,455-150*(140/250)**2); s.dot(*p,8,TEAL); s.text(p[0]+10,p[1]-20,"ρ",16,TEAL,30)
    s.arrow(p[0],p[1],p[0]+100,p[1],ORANGE,3); s.text(p[0]+40,p[1]-25,"ρ ω²r",14,ORANGE,80)
    s.arrow(p[0],p[1],p[0],p[1]+95,RED,3); s.text(p[0]+10,p[1]+58,"ρg",15,RED,40)
    # tangent slope
    s.line(p[0]-60,p[1]-35,p[0]+60,p[1]+35,TEAL,2,"dashed")
    s.text(570,605,"dz/dr=ω²r/g",15,TEAL,135)
    for y in [590,625]: s.line(180,y,680,y,GRID,1,"dashed")
    panel(s,800,220,485,375,"ROTATING-FRAME BALANCE")
    s.text(850,315,"∇p/ρ = ω²r r̂ − g ẑ",19,GREEN,365)
    s.text(850,385,"free surface: p=p₀",20,BLUE,250)
    s.text(850,450,"ω=0 → flat surface",18,MUTED,260)
    s.text(850,515,"larger r → larger z",18,PURPLE,260)
    return s


def d116() -> Scene:
    s=Scene("D11.6"); s.title("A floating body's metacentre predicts whether it rights itself",
        "For small heel, M above G gives a restoring couple; for a fully submerged body, stability requires G below B.")
    panel(s,40,170,850,500,"FLOATING BODY · small heel θ")
    # Horizontal waterline and a body rotated slightly clockwise in the page.
    s.line(95,455,825,455,BLUE,2.2)
    angle=math.radians(10); cx,cy=450,500
    local=[(-180,-50),(180,-50),(140,100),(-140,100)]
    hull=[(cx+x*math.cos(angle)-y*math.sin(angle),cy+x*math.sin(angle)+y*math.cos(angle)) for x,y in local]
    polyline(s,hull+[hull[0]],INK,4)
    G=(450,500); B=(450,545); Bp=(475,545); M=(475,360)
    s.line(G[0],G[1],M[0],M[1],GRID,1.4,"dashed")
    s.dot(*G,8,RED); s.text(G[0]-26,G[1]-30,"G",17,RED,25)
    s.dot(*B,7,BLUE); s.text(B[0]-25,B[1]+10,"B",16,BLUE,25)
    s.dot(*Bp,8,TEAL); s.text(Bp[0]+10,Bp[1]+8,"B′",16,TEAL,35)
    s.dot(*M,8,PURPLE); s.text(M[0]+8,M[1]-14,"M",17,PURPLE,30)
    s.line(M[0],M[1],Bp[0],Bp[1],GRID,1.3,"dashed")
    s.arrow(G[0],G[1],G[0],G[1]+110,RED,3); s.text(G[0]+12,G[1]+62,"W",16,RED,30)
    s.arrow(Bp[0],Bp[1],Bp[0],Bp[1]-112,TEAL,3); s.text(Bp[0]+12,Bp[1]-95,"B_uoy",15,TEAL,65)
    arc(s,G[0],G[1],72,math.pi/2,math.pi/2-angle,ORANGE,2); s.text(492,417,"θ",16,ORANGE,25)
    s.text(130,625,"M above G ⇒ separated W and buoyancy lines give a restoring couple",15,GREEN,410)
    panel(s,925,170,415,500,"FULLY SUBMERGED")
    s.rect(1035,325,210,190,GRID,PALE_BLUE,2,True)
    s.dot(1140,385,8,BLUE); s.text(1155,370,"B",16,BLUE,25)
    s.dot(1140,455,8,RED); s.text(1155,442,"G below B",15,RED,100)
    s.arrow(1140,380,1140,340,GREEN,2.7); s.text(1152,342,"F_B",14,GREEN,45)
    s.arrow(1140,460,1140,500,RED,2.7); s.text(1152,475,"W",14,RED,25)
    s.text(980,560,"stable if G lies below B",16,GREEN,260)
    return s


def d117() -> Scene:
    s=Scene("D11.7"); s.title("Bernoulli follows from pressure work plus gravitational and kinetic energy",
        "A fluid slug moves from section 1 to 2 through a steady streamtube; continuity links the two speeds.")
    # curved narrowing streamtube
    upper=[(120,300),(300,265),(500,295),(700,355),(940,365)]
    lower=[(120,520),(300,565),(500,525),(700,450),(940,430)]
    polyline(s,upper,BLUE,3); polyline(s,lower,BLUE,3)
    s.text(155,315,"A₁",18,BLUE,35); s.text(875,385,"A₂<A₁",17,BLUE,80)
    # velocity arrows and shaded slugs
    for y in [350,395,455]: s.arrow(175,y,245,y,TEAL,2)
    for y in [385,405,425]: s.arrow(790,y,910,y,GREEN,2.5)
    s.rect(255,354,100,120,TEAL,PALE_TEAL,1.6,True)
    s.rect(690,366,55,82,GREEN,PALE_GREEN,1.6,True)
    s.arrow(255,340,355,340,ORANGE,2); s.text(272,317,"v₁Δt",15,ORANGE,65)
    s.arrow(690,350,745,350,ORANGE,2); s.text(682,326,"v₂Δt",15,ORANGE,70)
    s.arrow(125,425,240,425,PURPLE,3); s.text(145,395,"p₁",16,PURPLE,30)
    s.arrow(940,400,830,400,PURPLE,3); s.text(880,370,"p₂",16,PURPLE,30)
    s.line(120,620,940,620,GRID,1.5); s.line(290,565,290,620,GRID,1,"dashed"); s.line(795,450,795,620,GRID,1,"dashed")
    s.text(270,630,"y₁",15,INK,35); s.text(775,630,"y₂",15,INK,35)
    panel(s,1010,205,305,390,"ENERGY / VOLUME")
    s.text(1050,295,"p₁+½ρv₁²+ρgy₁",16,BLUE,250)
    s.text(1050,345,"= p₂+½ρv₂²+ρgy₂",16,GREEN,250)
    s.text(1050,435,"A₁v₁=A₂v₂",19,PURPLE,200)
    s.text(1050,510,"steady · incompressible\n· non-viscous",15,MUTED,230)
    return s


def d118() -> Scene:
    s=Scene("D11.8"); s.title("A siphon is limited by the absolute pressure at its crest",
        "The top pressure falls as the crest rises; vapor formation breaks the continuous liquid column.")
    # Reservoir, tube crest, descending outlet
    s.line(130,540,470,540,INK,4); s.line(130,540,130,680,INK,4); s.line(130,680,720,680,INK,4)
    s.line(130,390,470,390,BLUE,1.6,"dashed"); s.text(145,360,"free surface p₀",15,BLUE,120)
    tube=[(430,390),(430,255),(600,255),(600,610),(700,610)]
    polyline(s,tube,TEAL,7)
    s.arrow(455,390,455,290,TEAL,2.2); s.arrow(585,290,585,540,TEAL,2.2); s.arrow(610,610,685,610,TEAL,2.2)
    s.dot(515,255,7,RED); s.text(475,215,"crest",15,RED,55)
    s.arrow(570,390,570,255,PURPLE,2.2); s.text(580,315,"h",17,PURPLE,30)
    s.arrow(700,610,700,680,ORANGE,2.2); s.text(710,640,"outlet",14,ORANGE,55)
    panel(s,795,190,515,440,"BERNOULLI AT CREST")
    s.text(845,285,"p_top=p₀−ρgh−½ρv²",21,BLUE,390)
    s.text(845,360,"absolute p_top > p_vapor",19,GREEN,330)
    s.text(845,430,"h_max≈(p₀−p_v)/(ρg)\n      − v²/(2g)",18,PURPLE,380)
    s.text(845,525,"Near 10.3 m for water at sea level\nonly when the speed-head correction is small.",15,MUTED,405)
    return s


def d119() -> Scene:
    s=Scene("D11.9"); s.title("Two holes at complementary heights send jets to the same range",
        "For a water surface H above the ground, a hole at height y launches with v=√[2g(H−y)].")
    # Tank and water surface
    xL,xR=150,420; ground=625; Hpx=390; surface=ground-Hpx
    s.line(xL,surface,xR,surface,BLUE,2); s.line(xL,230,xL,ground,INK,4); s.line(xR,230,xR,ground,INK,4); s.line(xL,ground,xR,ground,INK,4)
    s.rect(xL+3,surface,xR-xL-6,ground-surface,"transparent",PALE_BLUE,1)
    ys=[ground-145,ground-245]
    landing=xR+285
    for idx,y in enumerate(ys):
        s.dot(xR,y,6,RED); s.arrow(xR,y,xR+66,y,TEAL,2.5)
        depth=(ground-y)
        # jet trajectory reaches the ground at equal x=2 sqrt(y(H-y)); schematically curved.
        pts=[]
        for j in range(31):
            t=j/30; px=xR+(landing-xR)*t; py=y+(ground-y)*t*t
            pts.append((px,py))
        polyline(s,pts,BLUE if idx==0 else PURPLE,2.6)
        s.text(xR-75,y-20,"y₁" if idx==0 else "y₂",15,RED,30)
    s.line(landing,ground-10,landing,ground+10,INK,1.5); s.text(landing-45,ground+20,"same landing",14,INK,100)
    s.text(115,surface-28,"H",16,BLUE,25); s.text(365,ground-230,"H−y",14,MUTED,60)
    panel(s,770,205,535,420,"HORIZONTAL RANGE")
    s.text(820,295,"t=√(2y/g)",21,TEAL,250)
    s.text(820,365,"v=√[2g(H−y)]",20,BLUE,300)
    s.text(820,435,"x=2√[y(H−y)]",22,GREEN,300)
    s.text(820,505,"y and H−y are interchangeable:\ncomplementary hole heights give equal range.",16,MUTED,420)
    return s


def d1110() -> Scene:
    s=Scene("D11.10"); s.title("Jet momentum determines force on fixed, tilted and moving plates",
        "The incoming mass flux and the velocity change—not pressure alone—set the force.")
    panels=[(35,"NORMAL · FIXED"),(490,"TILTED · FIXED"),(945,"MOVING WITH JET")]
    for x,h in panels: panel(s,x,170,420,475,h)
    # Normal plate
    s.arrow(95,380,265,380,BLUE,3.2); s.text(105,345,"ρ,a,v",15,BLUE,80)
    s.line(300,300,300,480,INK,7)
    for yy,dx in [(330,90),(380,115),(430,90)]: s.arrow(305,yy,305+dx,yy,TEAL,2.2)
    s.arrow(240,520,360,520,ORANGE,3); s.text(260,490,"F=ρav²",16,ORANGE,95)
    # A plate at angle θ to the jet; its normal momentum change scales as sinθ.
    s.arrow(535,380,680,380,BLUE,3.2); s.line(695,400,845,470,INK,7)
    s.arrow(685,382,635,360,TEAL,2.2); s.arrow(685,382,640,405,TEAL,2.2)
    s.arrow(695,400,745,314,PURPLE,3); s.text(750,318,"normal",14,PURPLE,70)
    arc(s,695,400,58,0,-math.radians(25),ORANGE,2); s.text(720,365,"θ",15,ORANGE,25)
    s.text(535,520,"F_N=ρav² sinθ",16,GREEN,180)
    # moving plate: relative speed v-u
    s.arrow(995,380,1185,380,BLUE,3.2); s.text(1005,345,"water speed v",14,BLUE,105)
    s.rect(1190,290,25,180,INK,PALE_ORANGE,2)
    s.arrow(1115,510,1250,510,ORANGE,3); s.text(1140,478,"plate u",14,ORANGE,70)
    s.text(990,540,"relative speed v−u",15,TEAL,150)
    s.text(990,575,"F=ρa(v−u)²",17,GREEN,160)
    return s


def d1111() -> Scene:
    s=Scene("D11.11"); s.title("Poiseuille flow is parabolic, with zero speed at the wall",
        "A cylindrical shell balances the pressure drop with viscous shear; no slip gives v(R)=0.")
    panel(s,35,170,810,495,"PIPE SEGMENT · SHELL OF RADIUS r")
    # Longitudinal pipe with parabolic profile arrows
    xL,xR=110,720; yT,yB=295,500
    s.line(xL,yT,xR,yT,INK,3); s.line(xL,yB,xR,yB,INK,3)
    for y,scale in [(330,45),(365,80),(398,115),(432,80),(466,45)]:
        s.arrow(235,y,235+scale,y,TEAL,2.1)
    s.rect(430,345,145,72,BLUE,PALE_BLUE,1.8,True)
    s.text(458,365,"shell",15,BLUE,65); s.text(458,389,"r, dr",14,INK,55)
    s.arrow(xL+5,400,xL+100,400,PURPLE,2.8); s.text(115,367,"p₁",16,PURPLE,30)
    s.arrow(xR-5,400,xR-100,400,PURPLE,2.8); s.text(680,367,"p₂<p₁",15,PURPLE,70)
    s.arrow(450,345,530,345,ORANGE,2); s.arrow(450,417,530,417,ORANGE,2)
    s.text(110,530,"v(r)=Δp(R²−r²)/(4ηL)",19,GREEN,365)
    s.text(515,530,"v=0 at wall",15,RED,115)
    # Cross-section profile inset
    panel(s,900,190,400,435,"CROSS-SECTION")
    cx,cy,R=1100,420,130
    s.ellipse(cx-R,cy-R,2*R,2*R,BLUE,"transparent",2.3)
    s.dot(cx,cy,7,TEAL); s.text(cx+12,cy-14,"v_max",14,TEAL,65)
    for dx in [-90,-60,-30,30,60,90]:
        yy=cy-math.sqrt(R*R-dx*dx); length=105*(1-(dx/R)**2)
        s.arrow(cx+dx,yy,cx+dx+length,yy,TEAL,2)
    s.text(1050,570,"parabolic profile",15,MUTED,140)
    return s


def d1112() -> Scene:
    s=Scene("D11.12"); s.title("Terminal speed is force balance; drag law changes with Reynolds number",
        "At terminal speed mg=F_b+F_d. A sphere passes from Stokes drag to a plateau, then a drag crisis.")
    panel(s,35,175,430,480,"FALLING SPHERE")
    s.ellipse(205,330,105,105,BLUE,PALE_BLUE,2.5)
    s.arrow(255,440,255,565,RED,3.5); s.text(270,500,"mg",17,RED,40)
    s.arrow(220,330,220,230,TEAL,3); s.text(165,245,"F_b",16,TEAL,45)
    s.arrow(290,330,290,230,PURPLE,3); s.text(305,245,"F_d",16,PURPLE,45)
    s.text(120,605,"terminal: a≈0",17,GREEN,160)
    panel(s,500,175,845,480,"DRAG COEFFICIENT C_d vs REYNOLDS NUMBER")
    x0,y0,x1,y1=590,585,1260,270
    axes(s,x0,y0,x1,y1,"log₁₀ Re","log₁₀ C_d")
    pts=[]
    for i in range(161):
        q=i/160; logRe=-2+8*q; Re=10**logRe
        if Re<1: Cd=24/Re
        elif Re<1000: Cd=24/Re*(1+0.15*Re**.687)
        elif logRe<5.45: Cd=.44
        else:
            drop=1/(1+math.exp(-(logRe-5.55)*9))
            Cd=.44*(1-drop)+.12*drop
        Cd=max(.1,min(200,Cd)); xx=x0+q*(x1-x0)
        yy=y0-(math.log10(Cd)+1)/(math.log10(200)+1)*(y0-y1)
        pts.append((xx,yy))
    polyline(s,pts,BLUE,3)
    crisis_x=x0+(5.55+2)/8*(x1-x0)
    s.line(crisis_x,y0,crisis_x,y1,GRID,1,"dashed")
    s.text(640,390,"Stokes: C_d=24/Re",14,TEAL,150)
    s.text(900,520,"inertial plateau ≈0.44",14,PURPLE,180)
    s.text(1045,365,"drag crisis\nnear Re≈3×10⁵",14,RED,145)
    s.arrow(1145,415,crisis_x-4,505,RED,1.8)
    return s


def d1113() -> Scene:
    s=Scene("D11.13"); s.title("Contact angle decides whether a meniscus is concave or convex",
        "Measure θ through the liquid: wetting water has θ<90°, while mercury on glass has θ>90°.")
    panels=[(55,"WATER · WETS GLASS"),(735,"MERCURY · NON-WETTING")]
    for x,h in panels: panel(s,x,175,610,490,h)
    # Tube cross-sections. At the left wall show the tangent and angle through liquid.
    for x,wet,color in [(170,True,BLUE),(850,False,RED)]:
        s.line(x,285,x,560,INK,5); s.line(x+260,285,x+260,560,INK,5)
        if wet:
            men=[(x,390),(x+45,420),(x+130,438),(x+215,420),(x+260,390)]
            tangent_end=(x+85,438); tang_angle=math.atan2(48,85)
            angle_start=-math.pi/2; angle_stop=-tang_angle
            label="θ<90°"
        else:
            men=[(x,430),(x+30,394),(x+95,365),(x+150,365),(x+220,398),(x+260,430)]
            tangent_end=(x+30,394); angle_start=-math.pi/2; angle_stop=math.radians(50)
            label="θ≈140°"
        polyline(s,men,color,4)
        if wet:
            s.arrow(x+108,505,x+24,505,TEAL,2.2)
            s.text(x+105,478,"adhesion to wall",13,TEAL,130)
        else:
            s.arrow(x+28,505,x+112,505,ORANGE,2.2)
            s.text(x+45,478,"cohesion inward",13,ORANGE,130)
        contact=men[0]
        s.line(contact[0],contact[1],contact[0],contact[1]+90,GRID,1.5,"dashed")
        s.line(*contact,*tangent_end,ORANGE,2.2,"dashed")
        arc(s,contact[0],contact[1],47,angle_start,angle_stop,PURPLE,2)
        s.text(x+42,contact[1]+(20 if wet else -45),label,15,PURPLE,80)
        s.text(x+30,585,"adhesion dominates" if wet else "cohesion dominates",15,TEAL if wet else RED,180)
    s.text(250,700,"dashed line: tangent at the contact",14,ORANGE,190); s.text(895,700,"θ is measured through the liquid",14,ORANGE,200)
    return s


def d1114() -> Scene:
    s=Scene("D11.14"); s.title("A soap bubble has two interfaces, so its excess pressure is doubled",
        "At a circular cut, each surface supplies a surface-tension force; a liquid drop has only one surface.")
    panel(s,45,175,625,490,"SOAP BUBBLE · TWO SURFACES")
    cx,cy,R=330,415,135
    s.ellipse(cx-R,cy-R,2*R,2*R,TEAL,PALE_TEAL,3)
    s.ellipse(cx-R+14,cy-R+14,2*(R-14),2*(R-14),BLUE,WHITE,1.7)
    s.line(cx,cy,cx+R,cy,GRID,1.5,"dashed"); s.text(cx+45,cy-25,"r",16,INK,25)
    s.text(cx-40,cy-10,"Δp",18,PURPLE,45)
    s.text(90,590,"two γ surfaces: 2γ·2πr",18,TEAL,265)
    s.text(90,625,"Δp·πr² = 4πrγ  ⇒  Δp=4γ/r",18,GREEN,350)
    panel(s,725,175,625,490,"LIQUID DROP · ONE SURFACE")
    cx,cy,R=1005,415,135
    s.ellipse(cx-R,cy-R,2*R,2*R,BLUE,PALE_BLUE,2.8)
    s.line(cx,cy,cx+R,cy,GRID,1.5,"dashed"); s.text(cx+48,cy-25,"r",16,INK,25)
    s.text(cx-40,cy-10,"Δp",18,PURPLE,45)
    s.text(780,590,"one γ surface: γ·2πr",18,BLUE,250)
    s.text(780,625,"Δp·πr² = 2πrγ  ⇒  Δp=2γ/r",18,GREEN,350)
    return s


def d1115() -> Scene:
    s=Scene("D11.15"); s.title("A short capillary flattens its meniscus instead of overflowing",
        "For the same liquid and temperature, Laplace pressure gives hR=h′R′; the constrained meniscus has R′>R.")
    panel(s,50,180,610,475,"LONG TUBE · JURIN HEIGHT")
    panel(s,735,180,610,475,"SHORT TUBE · FLATTER MENISCUS")
    base=590
    # Long tube: a curved concave meniscus supports the full rise h.
    x=250; level=365
    s.line(x,245,x,base,INK,4); s.line(x+100,245,x+100,base,INK,4)
    s.rect(x+3,level+12,94,base-level-12,"transparent",PALE_BLUE,1)
    polyline(s,[(x,level),(x+22,level+16),(x+50,level+21),(x+78,level+16),(x+100,level)],BLUE,3)
    s.line(x-35,base,x+135,base,TEAL,1.5,"dashed")
    s.arrow(x+125,base-4,x+125,level+5,PURPLE,2.5); s.text(x+137,460,"h",16,PURPLE,25)
    s.text(x+18,315,"curved meniscus",14,BLUE,130); s.text(x+28,level+36,"R",15,TEAL,25)
    # Short tube reaches the rim before the full capillary height; curvature relaxes.
    x=960; top=415
    s.line(x,top,x,base,INK,4); s.line(x+100,top,x+100,base,INK,4)
    s.rect(x+3,top+12,94,base-top-12,"transparent",PALE_BLUE,1)
    polyline(s,[(x,top),(x+25,top+6),(x+50,top+8),(x+75,top+6),(x+100,top)],TEAL,3)
    s.line(x-35,base,x+135,base,TEAL,1.5,"dashed")
    s.arrow(x+125,base-4,x+125,top+5,PURPLE,2.5); s.text(x+137,485,"h′<h",15,PURPLE,55)
    s.text(x+12,370,"flatter cap",14,TEAL,95); s.text(x+30,top+18,"R′>R",14,TEAL,55)
    s.text(180,690,"same liquid: hR=h′R′",20,GREEN,350)
    s.text(790,690,"short rise is balanced by weaker Laplace pressure",15,MUTED,440)
    return s


def d1116() -> Scene:
    s=Scene("D11.16"); s.title("Choose the fluid tool from the state of motion and the geometry",
        "Pressure-at-rest, narrow viscous flow, Bernoulli and momentum flux answer different questions.")
    # Boxes and arrows flow left-to-right/downward
    s.rect(70,210,235,72,BLUE,PALE_BLUE,2,True); s.text(95,235,"fluid at rest?",18,INK,190,"center")
    s.arrow(305,246,410,246,TEAL,2.4); s.text(338,216,"yes",14,TEAL,35)
    s.rect(410,210,260,72,GREEN,PALE_GREEN,2,True); s.text(432,235,"hydrostatics / manometer",15,INK,220,"center")
    s.arrow(188,282,188,380,ORANGE,2.4); s.text(202,325,"no",14,ORANGE,30)
    s.rect(70,380,235,78,TEAL,PALE_TEAL,2,True); s.text(90,405,"long narrow pipe?",16,INK,195,"center")
    s.arrow(305,419,410,419,PURPLE,2.4); s.text(338,390,"yes",14,PURPLE,35)
    s.rect(410,380,260,78,ORANGE,PALE_ORANGE,2,True); s.text(438,403,"Poiseuille",18,INK,200,"center")
    s.arrow(188,458,188,555,RED,2.4); s.text(202,500,"no",14,RED,30)
    s.rect(70,555,235,85,PURPLE,"#f0ecf7",2,True); s.text(90,579,"Bernoulli gates all pass?",15,INK,195,"center")
    s.arrow(305,580,410,535,GREEN,2.4); s.text(333,545,"yes",14,GREEN,35)
    s.rect(410,490,260,72,GREEN,PALE_GREEN,2,True); s.text(435,514,"Bernoulli + continuity",16,INK,220,"center")
    s.arrow(305,615,410,655,RED,2.4); s.text(333,635,"no",14,RED,30)
    s.rect(410,615,260,78,RED,PALE_RED,2,True); s.text(435,636,"momentum flux / full dynamics",14,INK,220,"center")
    panel(s,760,190,555,480,"FAST TRIAGE")
    s.text(810,280,"Q2 · pressure / manometer",17,BLUE,320)
    s.text(810,345,"Q19 · viscous pipe flow",17,ORANGE,300)
    s.text(810,410,"Q12 · streamline energy",17,GREEN,310)
    s.text(810,475,"Q16 · jet force",17,RED,260)
    s.text(810,555,"If a model gate fails, do not use its shortcut.",16,MUTED,420)
    return s


def d1117() -> Scene:
    s=Scene("D11.17"); s.title("The fluid-mechanics toolkit: route the givens to the right law",
        "Each toolbox has a model gate; use momentum or full dynamics when the Bernoulli assumptions fail.")
    nodes=[(55,185,"hydrostatics","p=p₀+ρgh",PURPLE),(425,130,"buoyancy / stability","F_B=ρgV",TEAL),
           (900,130,"continuity + Bernoulli","Av=const",BLUE),(1050,390,"momentum flux","F=ṁΔv",ORANGE),
           (775,625,"viscosity","Poiseuille / Stokes",RED),(250,625,"surface tension","Young–Laplace / capillary",GREEN)]
    hub=(700,390)
    for x,y,head,eq,col in nodes:
        s.line(hub[0],hub[1],x+142,y+50,GRID,1.4,"dashed")
    s.ellipse(575,330,250,120,BLUE,PALE_BLUE,2.5); s.text(625,374,"identify the model",18,INK,170,"center")
    for x,y,head,eq,col in nodes:
        s.rect(x,y,285,100,col,WHITE,2,True)
        s.text(x+16,y+15,head,17,col,250); s.text(x+16,y+58,eq,15,INK,250)
    s.text(820,535,"Bernoulli gates",15,BLUE,115)
    s.text(820,560,"steady · incompressible · inviscid · along a streamline",13,MUTED,420)
    return s


def d1118() -> Scene:
    s=Scene("D11.18"); s.title("A draining tank: Torricelli gives a square law, viscous flow an exponential",
        "For an orifice, √h falls linearly; a laminar capillary drain has dh/dt∝−h.")
    # Tank section
    s.line(110,210,110,575,INK,4); s.line(330,210,330,575,INK,4); s.line(110,575,330,575,INK,4)
    s.line(110,300,330,300,BLUE,1.8,"dashed"); s.text(120,272,"h(t)",16,BLUE,55)
    s.arrow(330,500,420,500,TEAL,2.8); s.text(340,468,"orifice",14,TEAL,65)
    s.arrow(330,525,415,525,PURPLE,2.8); s.text(340,535,"v=√(2gh)",14,PURPLE,95)
    s.text(145,615,"tank area A",15,INK,105)
    # h(t) graph
    panel(s,500,175,820,510,"HEIGHT h(t) / h₀")
    x0,y0,x1,y1=585,590,1250,255
    s.arrow(x0,y0,x1,y0,INK,1.7); s.arrow(x0,y0,x0,y1,INK,1.7)
    s.text(x1-12,y0+9,"t/T",14,INK,45); s.text(x0-35,y1-15,"h/h₀",14,INK,50)
    tor=[]; vis=[]
    for i in range(101):
        q=i/100; tor.append((x0+q*(x1-x0),y0-(1-q)**2*(y0-y1)))
        vis.append((x0+q*(x1-x0),y0-math.exp(-3*q)*(y0-y1)))
    polyline(s,tor,BLUE,3); polyline(s,vis,ORANGE,3)
    s.text(900,365,"orifice: (1−t/T)²",15,BLUE,170)
    s.text(850,485,"viscous capillary: e^(−t/τ)",15,ORANGE,220)
    lo,hi=.1,1.0
    for _ in range(40):
        mid=(lo+hi)/2
        if (1-mid)**2>math.exp(-3*mid): lo=mid
        else: hi=mid
    qstar=(lo+hi)/2; px=x0+qstar*(x1-x0); py=y0-(1-qstar)**2*(y0-y1)
    s.dot(px,py,6,RED); s.text(px+10,py-30,"crossing h*",14,RED,100)
    return s


def d1119() -> Scene:
    s=Scene("D11.19"); s.title("The rotating-bucket paraboloid has three equivalent derivations",
        "At ω=4 rad s⁻¹ and R=0.30 m, the centre-to-edge rise is ω²R²/(2g)=7.35 cm.")
    # Main bowl cross-section
    s.line(100,250,100,600,INK,4); s.line(580,250,580,600,INK,4); s.line(100,600,580,600,INK,4)
    pts=[(120+440*i/60,500-170*((-1+2*i/60)**2)) for i in range(61)]
    polyline(s,pts,BLUE,3.5); s.line(120,500,560,500,GRID,1.2,"dashed")
    s.text(195,315,"z=z₀+ω²r²/(2g)",17,BLUE,220)
    s.arrow(560,500,560,330,ORANGE,2.5); s.text(465,370,"Δz=7.35 cm",14,ORANGE,110)
    # three mini-derivation cards
    cards=[(660,175,"(a) FORCE BALANCE","N, mg, mω²r","surface slope = ω²r/g"),
           (900,175,"(b) EFFECTIVE POTENTIAL","Φ=gz−½ω²r²","surface is Φ=constant"),
           (1140,175,"(c) CENTRIFUGAL HEAD","Δp=½ρω²R²","ρgΔz=Δp")]
    for x,y,h,a,b in cards:
        panel(s,x,y,215,415,h); s.text(x+17,y+100,a,15,TEAL,185); s.text(x+17,y+195,b,14,INK,185)
    s.text(650,650,"The same free surface follows from Newton's law, an effective potential, or pressure head.",15,MUTED,670)
    return s


def d1120() -> Scene:
    s=Scene("D11.20"); s.title("Surface tension lifts a strider and holds a pendant drop",
        "At contact lines, γ acts tangent to the interface; the vertical components support weight.")
    panel(s,40,175,625,490,"WATER STRIDER · DENTED SURFACE")
    # waterline with a shallow V-shaped dent
    s.line(90,415,245,415,BLUE,3); s.line(245,415,320,475,BLUE,3); s.line(320,475,395,415,BLUE,3); s.line(395,415,610,415,BLUE,3)
    # leg and symmetric surface tension vectors
    s.line(320,345,320,468,INK,7); s.ellipse(295,325,50,25,TEAL,PALE_TEAL,2)
    s.arrow(245,415,185,350,ORANGE,3); s.arrow(395,415,455,350,ORANGE,3)
    s.text(130,325,"γ tangent",14,ORANGE,90); s.text(450,325,"γ tangent",14,ORANGE,90)
    s.arrow(320,350,320,255,RED,3.2); s.text(333,280,"weight",15,RED,65)
    s.text(105,565,"2γℓ sinα balances the load",17,GREEN,310)
    panel(s,710,175,640,490,"PENDANT DROP · TATE'S METHOD")
    # Drop hanging from capillary tip with neck
    s.line(970,245,970,320,INK,8); s.line(1090,245,1090,320,INK,8)
    s.ellipse(992,300,76,38,TEAL,PALE_TEAL,2)
    s.ellipse(995,325,70,130,BLUE,PALE_BLUE,2.5)
    s.ellipse(1007,315,46,23,ORANGE,PALE_ORANGE,2)
    s.arrow(1030,335,1030,430,RED,3); s.text(1045,390,"mg",16,RED,35)
    s.arrow(1095,318,1190,318,GREEN,3); s.text(1135,290,"2πrγ",16,GREEN,65)
    s.text(1120,385,"neck radius r",14,ORANGE,100)
    s.text(775,565,"detachment: drop weight ≈ 2πrγ",17,GREEN,320)
    return s


TOPIC_INFO={
    "rotational-mechanics":("Rotational-mechanics.md",8),
    "gravitation":("Gravitation.md",9),
    "simple-harmonic-motion":("Simple-harmonic-motion.md",10),
    "fluid-mechanics":("Fluid-mechanics.md",11),
}
BUILDERS=[
 ("rotational-mechanics","D8.1","The velocity field of a spinning disc",d81),
 ("rotational-mechanics","D8.2","Moment of inertia of six standard bodies",d82),
 ("rotational-mechanics","D8.3","The parallel-axis theorem geometry",d83),
 ("rotational-mechanics","D8.4","Torque about a point with the moment arm",d84),
 ("rotational-mechanics","D8.5","The rolling wheel's velocity field with the contact point at rest",d85),
 ("rotational-mechanics","D8.6","The spinning skater: angular momentum conservation",d86),
 ("rotational-mechanics","D8.7","The rolling race: five bodies at the same time",d87),
 ("rotational-mechanics","D8.8","The slipping-to-rolling phase diagram",d88),
 ("rotational-mechanics","D8.9","A rod struck by a bullet",d89),
 ("rotational-mechanics","D8.10","The ladder problem's force diagram with the incipient-tip normal force",d810),
 ("rotational-mechanics","D8.11","A gyroscope with L, torque and the precession cone",d811),
 ("rotational-mechanics","D8.12","The collision-then-roll transition: bullet embeds in rod",d812),
 ("gravitation","D9.1","The shell theorem cone construction",d91),
 ("gravitation","D9.2","Field inside a uniform sphere and the cavity",d92),
 ("gravitation","D9.3","The four g-variation curves on one plate",d93),
 ("gravitation","D9.4","A Kepler ellipse with focus, radii and equal-area sectors",d94),
 ("gravitation","D9.5","The effective-potential turning points for several angular momenta",d95),
 ("gravitation","D9.6","The tide-raising differential-pull diagram",d96),
 ("gravitation","D9.7","Gauss's law Gaussian surface for a uniform sphere",d97),
 ("gravitation","D9.8","Energy ladder for orbital transfers",d98),
 ("gravitation","D9.9","Hohmann transfer: the tangential ellipse",d99),
 ("gravitation","D9.10","The effective-potential curve for gravitational orbits",d910),
 ("gravitation","D9.11","The Lagrange points of the Sun-Earth system",d911),
 ("gravitation","D9.12","The gravity-assist slingshot in the Sun's frame",d912),
 ("simple-harmonic-motion","D10.1","SHM sinusoidal waveform: x, v and a",d101),
 ("simple-harmonic-motion","D10.2","The SHM phasor diagram",d102),
 ("simple-harmonic-motion","D10.3","Energy versus displacement in SHM",d103),
 ("simple-harmonic-motion","D10.4","Series and parallel spring configurations",d104),
 ("simple-harmonic-motion","D10.5","Simple pendulum with restoring-force decomposition",d105),
 ("simple-harmonic-motion","D10.6","Lissajous figures for common frequency ratios",d106),
 ("simple-harmonic-motion","D10.7","Resonance curve: amplitude versus driving frequency",d107),
 ("simple-harmonic-motion","D10.8","The two normal modes of coupled pendulums",d108),
 ("simple-harmonic-motion","D10.9","The SHM velocity–displacement ellipse and its area",d109),
 ("simple-harmonic-motion","D10.10","The ballistic pendulum: collision then swing",d1010),
 ("simple-harmonic-motion","D10.11","The nonlinear pendulum: period versus amplitude",d1011),
 ("simple-harmonic-motion","D10.12","The torsion pendulum",d1012),
 ("fluid-mechanics","D11.1","Pressure-depth graph for a two-layer liquid",d111),
 ("fluid-mechanics","D11.2","Hydrostatic paradox vessels",d112),
 ("fluid-mechanics","D11.3","The hydraulic press and displacement trade",d113),
 ("fluid-mechanics","D11.4","Curved-gate forces by projection",d114),
 ("fluid-mechanics","D11.5","The rotating fluid paraboloid",d115),
 ("fluid-mechanics","D11.6","Metacentric stability of a floating body",d116),
 ("fluid-mechanics","D11.7","Bernoulli streamtube derivation",d117),
 ("fluid-mechanics","D11.8","Siphon pressure at the highest point",d118),
 ("fluid-mechanics","D11.9","Two draining-tank holes with equal range",d119),
 ("fluid-mechanics","D11.10","Jet force on flat, inclined and moving plates",d1110),
 ("fluid-mechanics","D11.11","Poiseuille profile and viscous shell",d1111),
 ("fluid-mechanics","D11.12","Terminal velocity and drag regimes",d1112),
 ("fluid-mechanics","D11.13","Meniscus shapes and contact angle",d1113),
 ("fluid-mechanics","D11.14","Soap-bubble cross-section and excess pressure",d1114),
 ("fluid-mechanics","D11.15","Capillary rise in a short tube",d1115),
 ("fluid-mechanics","D11.16","Decision tree for fluid-pressure tools",d1116),
 ("fluid-mechanics","D11.17","Fluid-mechanics toolkit map",d1117),
 ("fluid-mechanics","D11.18","Draining tank: variable-height curves",d1118),
 ("fluid-mechanics","D11.19","Rotating-bucket derivations",d1119),
 ("fluid-mechanics","D11.20","Water strider and pendant-drop force balance",d1120),
]


def update_note_and_manifest(topic:str, records:list[tuple[str,str,str]]) -> None:
    master_name,part=TOPIC_INFO[topic]; master=ROOT/topic/master_name
    source=master.read_text(encoding="utf-8").splitlines()
    by_id={}
    for diagram_id,title,slug in records: by_id[diagram_id]=(title,slug)
    i=0
    while i<len(source):
        match=re.match(r"^> \[!abstract\] DIAGRAM (D\d+\.\d+) · ",source[i])
        if not match:
            i+=1; continue
        diagram_id=match.group(1)
        if diagram_id not in by_id:
            i+=1; continue
        j=i+1
        while j<len(source) and source[j].startswith(">"):
            j+=1
        while j<len(source) and source[j]=="": j+=1
        embed=f"![[../_obsidian/excalidraw/{by_id[diagram_id][1]}|900]]"
        if j>=len(source) or source[j]!=embed:
            source[j:j]=[embed,""]
            j+=2
        i=j
    master.write_text("\n".join(source)+"\n",encoding="utf-8")
    manifest_path=ROOT/topic/"figures.json"
    if manifest_path.is_file():
        manifest=json.loads(manifest_path.read_text(encoding="utf-8"))
    else:
        manifest={"slug":topic,"policy":"docs/obsidian-plugin-workflow.md §2","figures":[]}
    drawings=[]
    for diagram_id,title,slug in records:
        # Locate the original two brief fields; preserve their exact prose.
        note=master.read_text(encoding="utf-8")
        header=f"> [!abstract] DIAGRAM {diagram_id} ·"
        start=next(i for i,line in enumerate(note.splitlines()) if line.startswith(header))
        block=[]
        for line in note.splitlines()[start+1:]:
            if not line.startswith(">"):
                if block: break
                continue
            block.append(line)
        show=next((line.split("*Show:*",1)[1].strip() for line in block if "*Show:*" in line),"")
        search=next((line.split("*Search:*",1)[1].strip() for line in block if "*Search:*" in line),"")
        drawings.append({"id":diagram_id,"kind":"excalidraw","title":title,
                         "show":show,"search":search,
                         "file":f"_obsidian/excalidraw/{slug}.md",
                         "source":f"{topic}/{master_name} · {diagram_id}"})
    manifest["renderer"]="obsidian-excalidraw-plugin@2.27.3"
    manifest["drawings"]=drawings
    manifest_path.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")


def main()->None:
    by_topic={}
    for topic,diagram_id,title,builder in BUILDERS:
        slug,_=scene_file(topic,diagram_id,title,builder())
        by_topic.setdefault(topic,[]).append((diagram_id,title,slug))
    for topic,records in by_topic.items():
        update_note_and_manifest(topic,records)
        print(f"{topic}: embedded {len(records)} scenes")
    print(f"Generated and embedded {len(BUILDERS)} editable Excalidraw scenes for Parts 8–11.")

if __name__=="__main__":
    main()
