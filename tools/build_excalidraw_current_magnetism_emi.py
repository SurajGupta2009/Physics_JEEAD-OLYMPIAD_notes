#!/usr/bin/env python3
"""Native editable diagrams for course slots 19–21. Standard library only.

Current Electricity: D19 companions to 26 retained SVGs. Magnetism: existing
D16 briefs (30). EMI/AC: existing D20 briefs (22). IDs are chapter-local;
Magnetism's D16 does not rename or overwrite Thermodynamics' D16 companions.
Regeneration overwrites manual scene edits. No HTML exporter is invoked.
"""
from __future__ import annotations
import json
import math
import re
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from tools.build_excalidraw_batch import Scene, scene_file, INK, BLUE, RED, GREEN, ORANGE, PURPLE, TEAL, MUTED, GRID, WHITE
from tools.build_excalidraw_waves_thermal import ROOT, add_path
from tools.build_excalidraw_heat_capacitors import converted_scene

TOPICS={'current-electricity':('Current-electricity.md',19,26),
        'magnetism':('Magnetism.md',16,30),'emi-ac':('Emi-ac.md',20,22)}
TAU=2*math.pi


def label(s,x,y,t,c=INK,size=20,w=560):s.text(x,y,t,size,c,w)
def curve(s,pts,c=BLUE,sw=2.5,dash=False):add_path(s,pts,c,'transparent',sw,dash)
def arc(s,x,y,r,a=0,b=TAU,c=BLUE,arrow=False,ry=None):
    ry=r if ry is None else ry
    pts=[(x+r*math.cos(t),y-ry*math.sin(t)) for t in [a+(b-a)*i/100 for i in range(101)]]
    curve(s,pts,c)
    if arrow:s.arrow(*pts[-4],*pts[-1],c,2.5)
    return pts

def field(s,x,y,w,h,out=False,step=75):
    for xx in range(int(x)+25,int(x+w),step):
        for yy in range(int(y)+25,int(y+h),step):symbol(s,xx,yy,out,GRID,6)

def symbol(s,x,y,out=True,c=BLUE,r=12):
    s.ellipse(x-r,y-r,2*r,2*r,c,'transparent',1.5)
    if out:s.dot(x,y,2.4,c)
    else:s.line(x-r*.6,y-r*.6,x+r*.6,y+r*.6,c,1.5);s.line(x-r*.6,y+r*.6,x+r*.6,y-r*.6,c,1.5)

def panel(s,x,y,w,h,title):
    s.rect(x,y,w,h,GRID,WHITE,1,True);label(s,x+18,y+12,title,BLUE,21,w-36)

def footer(s,*lines):
    for i,t in enumerate(lines):label(s,70,740+i*37,t,INK,20,1280)

def axes(s,x=100,y=650,w=500,h=280,xlabel='x',ylabel='y'):
    s.arrow(x,y,x+w,y,INK,1.5);s.arrow(x,y,x,y-h,INK,1.5)
    label(s,x+w+10,y-12,xlabel,INK,18,160);label(s,x-5,y-h-35,ylabel,INK,18,450)

def graph(s,fn,a,b,x,y,w,h,c=BLUE,steps=240):
    pts=[(x+w*i/steps,y-h*fn(a+(b-a)*i/steps)) for i in range(steps+1)]
    curve(s,pts,c);return pts

def resistor(s,a,b,y,t='R'):
    mid=(a+b)/2;s.line(a,y,mid-35,y);s.rect(mid-35,y-14,70,28,INK,WHITE,2);s.line(mid+35,y,b,y)
    label(s,mid-25,y-48,t,INK,19,160)

def cap(s,a,b,y,t='C'):
    mid=(a+b)/2;s.line(a,y,mid-10,y);s.line(mid+10,y,b,y)
    s.line(mid-10,y-27,mid-10,y+27,BLUE,3);s.line(mid+10,y-27,mid+10,y+27,BLUE,3);label(s,mid-12,y-60,t,BLUE,19,200)

def coil(s,a,b,y,t='L'):
    s.line(a,y,a+15,y);s.line(b-15,y,b,y)
    width=b-a-30
    for i in range(7):arc(s,a+15+(i+.5)*width/7,y,width/14,math.pi,0,BLUE,ry=18)
    label(s,a+width/2-15,y-56,t,BLUE,19,250)

def battery(s,x,y,h=100):
    s.line(x,y-h/2,x,y-12);s.line(x,y+12,x,y+h/2)
    s.line(x-28,y-12,x+28,y-12,INK,3);s.line(x-15,y+12,x+15,y+12,INK,3)
    label(s,x+35,y-28,'+',RED,20,40);label(s,x+35,y+10,'−',BLUE,20,40)

def loop_field(s,x,y,w=390,h=155):
    for xx in range(int(x),int(x+w)+1,45):symbol(s,xx,y,True,BLUE,7);symbol(s,xx,y+h,False,BLUE,7)
    for yy in [y+40,y+80,y+120]:s.arrow(x+15,yy,x+w-15,yy,BLUE,2)
    label(s,x+80,y+h+25,'B inside →',BLUE)

def magnet(s,x,y,w=220,h=65):
    s.rect(x,y,w/2,h,BLUE,'#e9f2fb');s.rect(x+w/2,y,w/2,h,RED,'#faeceb')
    label(s,x+30,y+20,'S',BLUE,23);label(s,x+w-50,y+20,'N',RED,23)
    s.arrow(x+25,y+h/2,x+w-25,y+h/2,GREEN,2)
    for hh in [60,95]:
        curve(s,[(x+w,y+h/2),(x+w+30,y-hh),(x+w/2,y-hh-25),(x-30,y-hh),(x,y+h/2)],BLUE)
        s.arrow(x+w*.6,y-hh-25,x+w*.4,y-hh-25,BLUE,2)
        curve(s,[(x,y+h/2),(x-30,y+h+hh),(x+w/2,y+h+hh+25),(x+w+30,y+h+hh),(x+w,y+h/2)],BLUE)
        s.arrow(x+w*.6,y+h+hh+25,x+w*.4,y+h+hh+25,BLUE,2)


def magnetic(n,title):
    s=Scene(f'magnetism:D16.{n}');s.title(title,'Magnetism · editable geometry; arrows use conventional current and the stated sign of charge.')
    if n==1:
        for i,(I,t) in enumerate([(0,'No current'),(1,'Current north'),(-1,'Current south')]):
            x=70+435*i;panel(s,x,135,410,520,t)
            s.ellipse(x+95,265,210,210,GRID,WHITE);label(s,x+170,225,'N (Earth)',GREEN)
            s.line(x+200,190,x+200,540,INK,3)
            if I:s.arrow(x+200,440 if I>0 else 270,x+200,270 if I>0 else 440,ORANGE,4)
            # Wire above compass. North current gives west B at compass below it.
            s.arrow(x+200,370,x+200-95*I,290 if I==0 else 325,RED,4)
            if I:s.arrow(x+200,370,x+200-110*I,370,BLUE,2)
            label(s,x+30,575,'needle follows B_Earth + B_wire',INK,18,370)
        footer(s,'Wire is above the horizontal compass. Reverse I → reverse the transverse deflection.', 'Grip rule: thumb along I; curled fingers give the circulation of B.')
    elif n==2:
        for i,t in enumerate(['Positive charge','Wire grip rule','Negative charge']):panel(s,60+i*435,135,410,540,t)
        for x,sgn in [(260,1),(1130,-1)]:
            s.arrow(x-120,390,x+100,390,GREEN,3);label(s,x+65,420,'v →',GREEN)
            symbol(s,x,300,True,BLUE,22);label(s,x-60,230,'B out (⊙)',BLUE)
            s.arrow(x,390,x,390+sgn*145,RED,3);label(s,x-130,580,'F = q(v × B)',RED)
        symbol(s,700,380,True,ORANGE,20);arc(s,700,380,115,0,TAU*.9,BLUE,True)
        label(s,560,565,'I out → B anticlockwise',INK,19)
        footer(s,'v × B: +x × +z = −y. Apply the sign of q only after taking the cross product.', '⊙ points toward you; ⊗ points away. Force is perpendicular to v and B.')
    elif n==3:
        panel(s,60,130,580,570,'Circular motion: B out of page');field(s,80,180,540,380,True)
        arc(s,345,395,150);symbol(s,345,395,True)
        for a in [0,math.pi/2,math.pi,3*math.pi/2]:
            x=345+150*math.cos(a);y=395-150*math.sin(a)
            s.arrow(x,y,x+65*math.sin(a),y+65*math.cos(a),GREEN,3)
            s.arrow(x,y,345+85*math.cos(a),395-85*math.sin(a),RED,2)
        label(s,95,590,'q > 0: clockwise; q < 0: anticlockwise',INK,20,520)
        panel(s,690,130,650,570,'Helix: parallel speed is unchanged')
        pts=[(750+520*t,385+65*math.sin(8*math.pi*t)) for t in [i/500 for i in range(501)]];curve(s,pts)
        s.arrow(750,385,1290,385,GRID,2);s.arrow(850,540,980,540,GREEN,2);label(s,820,570,'pitch p = v∥ T',GREEN)
        label(s,740,210,'B →; v = v∥ + v⊥',BLUE,22)
        footer(s,'r = m v⊥/(|q|B); T = 2πm/(|q|B); pitch = 2πm v∥/(|q|B).', 'B changes direction of velocity, not speed: F · v = 0.')
    elif n==4:
        field(s,160,225,1050,350);s.rect(160,190,1030,14,BLUE,'#e9f2fb');s.rect(160,590,1030,14,RED,'#faeceb')
        s.arrow(180,400,1170,400,GREEN,3);label(s,760,410,'v = E/B: straight',GREEN)
        graph(s,lambda t:t*t,0,1,200,400,860,150,BLUE);graph(s,lambda t:-t*t,0,1,200,400,860,150,RED)
        label(s,840,215,'faster: magnetic side',BLUE);label(s,840,560,'slower: electric side',RED)
        s.arrow(520,400,520,295,BLUE,3);s.arrow(520,400,520,505,RED,3)
        label(s,555,280,'q v B ↑',BLUE);label(s,555,480,'q E ↓',RED)
        s.line(1190,225,1190,382,INK,4);s.line(1190,418,1190,575,INK,4)
        footer(s,'Positive charge enters rightward, E down, B into the page. F_y = q(vB − E).', 'The null speed E/B is independent of charge and mass; field regions must overlap.')
    elif n==5:
        for i,(r,d) in enumerate([(180,140),(100,140)]):
            x=100+450*i;panel(s,x,150,420,500,'r > d: cross strip' if i==0 else 'r < d: return through entry')
            field(s,x+55,225,d,340);s.line(x+55,225,x+55,585,INK);s.line(x+55+d,225,x+55+d,585,INK)
            # entry moving right, B into, positive charge bends up
            cx=x+55;cy=480-r;end=math.asin(d/r) if r>d else math.pi
            pts=[(cx+r*math.sin(t),cy+r*math.cos(t)) for t in [end*j/100 for j in range(101)]]
            curve(s,pts);s.arrow(cx-35,480,cx+35,480,GREEN,2)
            ex,ey=pts[-1];s.arrow(ex,ey,ex+60*math.cos(end),ey-60*math.sin(end),GREEN,2)
            label(s,x+20,595,'sin φ = d/r' if i==0 else 'semicircle: t = πm/(qB)',INK,18,390)
        panel(s,1010,150,335,500,'Circular field patch')
        s.ellipse(1055,280,220,220,GRID,'#e9f2fb');curve(s,[(1055,390),(1090,360),(1130,335),(1180,330),(1235,360)],BLUE)
        label(s,1030,540,'Radial entry: exit is radial',INK,18,310)
        footer(s,'Find the orbit centre perpendicular to the entry velocity; trace the first boundary crossing.', 'Use the swept arc angle: t = φ/ω_c, not the straight-line flight time.')
    elif n==6:
        field(s,100,150,540,430,True);arc(s,340,380,210,-math.pi/2,math.pi/2,GRID);arc(s,320,380,210,math.pi/2,3*math.pi/2,GRID)
        s.line(325,180,325,580,GRID);s.line(345,180,345,580,GRID)
        pts=[(335+(15+8*t)*math.cos(t),380+(15+8*t)*math.sin(t)) for t in [i*4*math.pi/600 for i in range(601)]];curve(s,pts,RED)
        label(s,170,615,'Dees: B out; gap accelerates',BLUE)
        axes(s,760,490,500,230,'t','gap voltage')
        graph(s,lambda t:math.cos(t),0,4*math.pi,760,375,470,90)
        for i in range(5):s.dot(760+470*i/4,375-90*(-1)**i,5,RED)
        label(s,780,565,'Crossings every T/2',RED)
        footer(s,'f_RF = |q|B/(2πm), nonrelativistic. Each gap crossing gains energy; curvature radius grows.', 'Spiral is schematic: semicircles in the dees, electric acceleration confined to the gap.')
    elif n==7:
        for off in [-150,-85,85,150]:curve(s,[(100,375+off),(420,375+off*.85),(760,375+off*.45),(1050,375+off*.3)],BLUE)
        pts=[(130+750*t,375+(60-45*t)*math.sin(28*math.pi*t)) for t in [i/700 for i in range(701)]];curve(s,pts,RED)
        s.arrow(890,375,750,375,RED,3);label(s,710,210,'F∥ = −μ dB/ds',RED)
        label(s,130,565,'B grows → v⊥ grows, v∥ falls',INK,22)
        s.arrow(1140,400,1310,400,INK);s.line(1140,400,1300,310,ORANGE);s.line(1140,400,1300,490,ORANGE)
        label(s,1080,525,'loss cone',ORANGE,20,250)
        footer(s,'Adiabatic invariant μ = mv⊥²/(2B). Reflection when sin²θ₀ ≥ B₀/B_max.', 'The loss cone contains small pitch angles: these particles can reach the high-field throat.')
    elif n==8:
        for i,holes in enumerate([False,True]):
            x=85+650*i;panel(s,x,150,580,515,'Electrons' if not holes else 'Positive holes')
            field(s,x+50,240,450,270,True);s.rect(x+70,260,420,200,INK,'transparent')
            s.arrow(x+160,340,x+340,340,GREEN,3);label(s,x+185,210,'I → ; B out',GREEN)
            s.arrow(x+280,390,x+150 if not holes else x+400,390,ORANGE,3)
            s.arrow(x+275,350,x+275,450,RED,3)
            label(s,x+80,495,'front edge (−y): '+('− − −' if not holes else '+ + +'),RED,20)
            s.arrow(x+430,285 if not holes else 430,x+430,430 if not holes else 285,BLUE,2)
            label(s,x+395,555,'E_H',BLUE)
        footer(s,'Both carrier types are pushed to the same edge, but the accumulated charge changes sign.', 'In equilibrium E_H = −v_d × B. The Hall-voltage sign identifies the carrier sign.')
    elif n==9:
        axes(s,110,560,1100,360,'x','y');field(s,130,180,1000,330,True)
        for factor,c in [(1,BLUE),(.65,GREEN),(1.25,RED)]:
            pts=[(140+75*(t-factor*math.sin(t)),540-75*(1-factor*math.cos(t))) for t in [i*4*math.pi/500 for i in range(501)]];curve(s,pts,c)
        arc(s,470,465,75);s.arrow(430,640,630,640,ORANGE,3);label(s,650,620,'v_E = E × B / B² →',ORANGE)
        footer(s,'E up, B out: drift is rightward. Blue: release from rest gives cusps and height 2r_c.', 'Green/red show different initial gyration amplitudes: curtate/prolate trajectories.')
    elif n==10:
        s.rect(100,290,1140,200,GRID,'transparent');s.rect(280,260,410,10,BLUE,'#e9f2fb');s.rect(280,515,410,10,RED,'#faeceb')
        field(s,300,300,350,190);s.line(1170,190,1170,620,INK,4)
        s.arrow(120,390,1150,390,GREEN,3);curve(s,[(120,390),(300,390),(480,355),(690,285),(1150,175)],RED)
        s.dot(1170,390,7,GREEN);s.dot(1170,175,7,RED)
        label(s,120,570,'electron beam →',INK);label(s,760,430,'crossed fields: null',GREEN);label(s,760,225,'electric only',RED)
        footer(s,'With E down and B into the page, electric force on an electron is up; magnetic force is down.', 'Null gives v = E/B. Combine with electric deflection or magnetic curvature to obtain e/m.')
    elif n==11:
        field(s,110,150,1120,500)
        pts=[(630+(260-12*t)*math.cos(t),385-(260-12*t)*math.sin(t)) for t in [i*3.5*math.pi/600 for i in range(601)]];curve(s,pts,RED)
        s.arrow(*pts[300],*pts[310],RED,3);s.rect(220,370,30,240,GRID,'#e4e4e4')
        label(s,940,170,'B into page',BLUE);label(s,940,225,'q > 0 bends CCW',RED)
        label(s,920,480,'radius shrinks',INK)
        footer(s,'Track direction follows energy loss toward smaller r; then v × B determines the charge sign.', 'p⊥ [MeV/c] ≈ 300 |z| B[T] r[m]. A material plate increases curvature through energy loss.')
    elif n in (12,13):
        s.arrow(300,650,300,180,ORANGE,4);label(s,190,200,'I ↑',ORANGE)
        s.dot(900,420,6);label(s,920,425,'P',INK);symbol(s,900,370,False,BLUE,20)
        s.line(300,420,900,420,GRID,2,'dashed');label(s,540,445,'d',INK)
        if n==12:
            s.arrow(300,530,300,470,RED,5);s.arrow(300,500,900,420,GREEN,3)
            label(s,450,510,'r from element to P',GREEN);label(s,150,550,'I dℓ',RED)
            s.dot(300,140,5);label(s,350,140,'on axis: dB = 0',BLUE)
            footer(s,'dB = (μ₀/4π) I dℓ × r / r³. At P to the right of an upward current, B is into the page.', 'Magnitude includes sinθ; the source element and field point must be distinguished.')
        else:
            s.line(300,230,900,420,GREEN);s.line(300,620,900,420,GREEN)
            arc(s,900,420,90,math.pi-.31,math.pi+.32,ORANGE)
            label(s,720,340,'α',ORANGE);label(s,720,470,'β',ORANGE)
            footer(s,'B = μ₀I(sinα + sinβ)/(4πd), for endpoints on opposite sides of the perpendicular foot.', 'Angles are measured at P from the perpendicular, not from the wire; signed angles handle other cases.')
    elif n==14:
        for i,t in enumerate(['Arc + radial leads','Arc + tangent leads','Two concentric arcs','Arc + chord']):panel(s,55+335*i,140,315,530,t)
        for i in range(4):
            x=210+335*i;arc(s,x,400,105,0,math.pi,BLUE,True);s.dot(x,400,5);symbol(s,x,460,True)
            if i==0:s.line(x-135,400,x-105,400,INK);s.line(x+105,400,x+135,400,INK)
            if i==1:s.arrow(x-105,400,x-105,570,INK);s.arrow(x+105,570,x+105,400,INK)
            if i==2:arc(s,x,400,65,math.pi,0,RED,True);s.line(x-105,400,x-65,400);s.line(x+65,400,x+105,400)
            if i==3:s.line(x-85,340,x+85,340,RED,3)
            label(s,x-140,580,['radial: zero at O','leads: signs by I','subtract opposite senses','finite-wire contribution'][i],INK,17,280)
        footer(s,'Arc: B = μ₀Iφ/(4πR); a radial segment gives zero at the centre. Add signed contributions.', 'The chord must not pass through the observation point. Geometry fixes the lead contribution signs.')
    elif n==15:
        loop_field(s,100,280,500,170)
        curve(s,[(600,370),(670,200),(350,160),(50,200),(100,370)],BLUE);s.arrow(420,160,310,160,BLUE)
        curve(s,[(600,370),(670,570),(350,610),(50,570),(100,370)],BLUE);s.arrow(420,610,310,610,BLUE)
        for r in [95,125,155]:arc(s,1040,380,r,0,TAU*.95,BLUE,True)
        s.ellipse(860,200,360,360,GRID,'transparent');s.ellipse(970,310,140,140,GRID,WHITE)
        label(s,950,615,'Toroid: B = μ₀NI/(2πr)',BLUE)
        footer(s,'Long solenoid: B ≈ μ₀nI inside; return flux closes outside. Ideal toroid confines B to its winding.', 'Finite-solenoid end corrections depend on the observation point; external field is not uniformly R/L.')
    elif n in (16,24):
        panel(s,60,140,620,550,'Electric dipole' if n==16 else 'Bar magnet');panel(s,710,140,620,550,'Magnetic dipole / solenoid')
        if n==16:
            s.dot(235,385,14,BLUE);s.dot(480,385,14,RED);label(s,210,410,'−q',BLUE);label(s,460,410,'+q',RED)
            s.arrow(450,385,265,385,BLUE,3);s.arrow(270,560,460,560,GREEN,3);label(s,350,590,'p →',GREEN)
            for off in [-120,120]:curve(s,[(480,385),(500,385+off),(350,385+off*1.4),(210,385+off),(235,385)],BLUE)
        else:magnet(s,230,350,260)
        loop_field(s,850,310,340,140);label(s,970,530,'μ →',GREEN);s.arrow(900,560,1170,560,GREEN,3)
        footer(s,'External far fields have the dipole form. Inside a current loop B is along μ; inside an electric dipole E opposes p.', 'Magnetic field lines close: inside a magnet B runs S → N, outside N → S.')
    elif n==17:
        symbol(s,340,385,True,ORANGE,20);arc(s,340,385,130,0,TAU*.95,BLUE,True)
        pts=[(340+(185+25*math.sin(3*t))*math.cos(t),385-(185+25*math.sin(3*t))*math.sin(t)) for t in [i*TAU/200 for i in range(201)]];curve(s,pts,GREEN)
        s.ellipse(590,250,135,220,RED,'transparent');label(s,540,535,'no enclosed I: zero',RED,18,350)
        arc(s,1040,385,170,0,TAU*.95,BLUE,True);symbol(s,980,385,True,ORANGE);symbol(s,1090,385,False,RED)
        label(s,910,580,'+5 A − 3 A = +2 A',INK)
        footer(s,'∮B · dℓ = μ₀I_enclosed. Anticlockwise traversal chooses an outward normal.', 'An irregular loop gives the same circulation; only symmetry permits taking B outside the integral.')
    elif n==18:
        for x in [350,980]:
            s.ellipse(x-160,210,320,320,BLUE,'#e9f2fb');s.ellipse(x-30,295,130,130,RED,WHITE)
            symbol(s,x-70,350,True,BLUE);symbol(s,x+35,360,False,RED)
            s.arrow(x,560,x+65,560,INK);label(s,x+15,590,'d →',INK)
            for xx in [x,x+35,x+70]:s.arrow(xx,410,xx,325,GREEN,2)
        label(s,175,155,'+J cylinder plus −J cylinder',BLUE);label(s,860,155,'off-centre cavity',BLUE)
        footer(s,'Inside overlap: B = (μ₀/2) J × d, uniform; d points from the +J axis to the −J axis.', 'For J out of the page and d to the right, the cavity field is upward. Subtract vectors, not magnitudes.')
    elif n==19:
        magnet(s,150,350,330);magnet(s,750,350,150);magnet(s,1080,350,150)
        s.ellipse(360,190,180,410,PURPLE,'transparent');label(s,185,615,'closed surface around an end',PURPLE)
        label(s,795,615,'Each cut piece has N and S.',INK)
        footer(s,'∮B · dA = 0: a surface enclosing one apparent pole still has equal flux entering and leaving.', 'Cutting a magnet does not isolate a magnetic charge; each piece retains closed field lines.')
    elif n==20:
        field(s,140,190,1000,440);arc(s,390,460,190,math.pi,0,BLUE,True)
        s.arrow(200,460,580,460,GREEN,3)
        for a in [.4,.9,1.5,2.1,2.6]:
            x=390+190*math.cos(a);y=460-190*math.sin(a);s.arrow(x,y,x-45*math.cos(a),y+45*math.sin(a),RED)
        s.arrow(390,460,390,620,RED,4);label(s,650,330,'F = I (r_exit − r_entry) × B',RED,24,630)
        label(s,650,405,'Same endpoints → same net force',INK,21)
        footer(s,'Uniform B: integrate I dℓ × B using the endpoint displacement. A closed loop has zero net force.', 'Zero net force does not mean zero torque: opposite side forces can form a couple.')
    elif n==21:
        s.arrow(130,380,630,380,BLUE,3);label(s,190,310,'uniform B →',BLUE)
        s.line(350,250,500,520,INK,4);s.arrow(425,385,540,310,GREEN,3);label(s,520,280,'n̂',GREEN)
        symbol(s,350,250,True,RED,17);symbol(s,500,520,False,RED,17)
        s.ellipse(825,235,350,330,GRID,WHITE);s.ellipse(930,300,140,190,INK,'#e4e4e4')
        for a in [0,.6,1.2,2,2.6,3.2,4,5]:s.arrow(1000+80*math.cos(a),395+95*math.sin(a),1000+150*math.cos(a),395+155*math.sin(a),BLUE,2)
        label(s,790,600,'radial gap: coil sides stay ⟂ B',BLUE,20)
        footer(s,'τ = μ × B; |τ| = NIAB sinθ. θ is between the area normal and B.', 'Moving-coil galvanometer: radial B makes torque NIAB; torsion κφ balances it.')
    elif n==22:
        for i,same in enumerate([True,False]):
            x=160+640*i;panel(s,x-80,140,570,520,'Same currents: attract' if same else 'Opposite currents: repel')
            for xx,direction in [(x,1),(x+310,1 if same else -1)]:s.arrow(xx,530 if direction>0 else 250,xx,250 if direction>0 else 530,ORANGE,4)
            symbol(s,x+310,380,False,BLUE,16)
            s.arrow(x+310,400,x+220 if same else x+420,400,RED,4)
            label(s,x+45,575,'B₁ at wire 2: into page',BLUE,18,430)
        footer(s,'F/L = μ₀|I₁I₂|/(2πd). Use the field of the other wire, not the wire’s self-field.', 'Same conventional-current directions attract; opposite directions repel.')
    elif n==23:
        loop_field(s,200,270,900,230)
        for xx in [300,550,800,1050]:s.arrow(xx,270,xx,180,RED,3);s.arrow(xx,500,xx,590,RED,3)
        s.rect(635,260,30,250,PURPLE,'#eee8f7');s.arrow(570,390,625,390,GREEN,3);s.arrow(725,390,675,390,GREEN,3)
        footer(s,'Magnetic pressure = B²/(2μ₀). The winding expands radially; separated axial halves attract.', 'Surface force uses the average field across the current sheet: field of the rest = B/2.')
    elif n==25:
        for row in range(3):
            for col in range(5):arc(s,180+95*col,275+95*row,40,0,TAU*.93,BLUE,True)
        s.rect(125,220,490,300,ORANGE,'transparent',3);label(s,120,580,'interior shared currents cancel',INK)
        loop_field(s,840,270,360,210)
        footer(s,'Uniform M: bound volume current ∇×M = 0, surface current K_b = M × n̂ survives.', 'A uniformly magnetised cylinder is equivalent to a surface solenoid; rim current of a slab I_b = Mt.')
    elif n==26:
        for x,d in [(340,1),(1000,-1)]:
            field(s,x-200,200,400,340)
            arc(s,x,385,140,0,d*TAU*.95,BLUE,True);symbol(s,x,385,True,RED,22)
            label(s,x-160,580,'Δμ opposes applied B',RED)
        footer(s,'Larmor response: Δμ = −(e²⟨ρ²⟩/4m) B for each electron orbit in the simple bound-orbit model.', 'Opposite initial senses both contribute an induced moment against B: diamagnetism.')
    elif n==27:
        for i in range(4):
            x=70+320*i;panel(s,x,140,290,220,['Closure domains','Wall motion','Rotation','Saturation'][i])
            for j in range(4):
                a=(TAU*j/4)*(1-i/3);xx=x+60+55*j
                s.arrow(xx,270,xx+38*math.cos(a),270-38*math.sin(a),BLUE,3)
        axes(s,170,645,450,205,'H','B');axes(s,820,645,420,205,'H','B')
        graph(s,lambda x:math.tanh(2*x),0,2,170,645,430,170)
        for shift,c in [(-.28,BLUE),(.28,RED)]:graph(s,lambda x:math.tanh(3*(x-shift)),-1,1,830,550,390,90,c)
        label(s,1080,395,'remanence at H = 0',INK,18,280)
        footer(s,'Magnetisation changes by domain-wall motion and rotation; saturation aligns moments.', 'Loop area ∮H dB is hysteresis loss per unit volume. Soft materials have small coercivity.')
    elif n==28:
        magnet(s,160,330,280);s.rect(650,335,160,35,INK,'#e4e4e4');s.arrow(670,353,530,353,RED,3)
        label(s,600,235,'iron: toward stronger B',RED)
        s.dot(690,540,15,TEAL);s.arrow(710,540,840,540,TEAL,3);label(s,540,595,'diamagnet: toward weaker B',TEAL)
        s.rect(990,210,70,340,INK,'#e4e4e4');s.rect(1220,210,70,340,INK,'#e4e4e4');s.rect(990,210,300,65,INK,'#e4e4e4');s.rect(970,575,340,45,INK,'#e4e4e4')
        s.arrow(1025,530,1025,580,BLUE,3);s.arrow(1255,580,1255,530,BLUE,3)
        footer(s,'A weak induced dipole responds to the gradient of B². Sign of susceptibility determines attraction or repulsion.', 'Lifting force is approximately B²A/(2μ₀) per pole face; count both gaps when appropriate.')
    elif n==29:
        s.ellipse(120,200,440,440,GRID,'#e9f2fb');s.line(340,155,340,690,INK,2,'dashed')
        s.arrow(390,600,290,245,BLUE,3);label(s,190,160,'geographic north',INK);label(s,375,260,'dipole S nearby',BLUE)
        s.arrow(770,320,1230,320,GREEN,3);s.arrow(770,320,1230,560,BLUE,3);s.arrow(1230,320,1230,560,RED,3)
        label(s,900,270,'B_H',GREEN);label(s,1050,475,'B',BLUE);label(s,1240,425,'B_V',RED)
        arc(s,770,320,100,-.48,0,ORANGE);label(s,890,345,'dip',ORANGE)
        footer(s,'B_H = B cos(dip), B_V = B sin(dip). In the northern hemisphere the field generally dips downward.', 'Declination is the horizontal angle from true north to magnetic north; Earth’s dipole axis is tilted ≈11°.')
    elif n==30:
        for row in range(2):
            y=270+280*row
            for i in range(12):label(s,140+i*85,y,'+',RED,24,40)
            for i in range(12+row*2):label(s,140+i*(85 if row==0 else 73),y+55,'−',BLUE,24,40)
            s.dot(680,y+140,9,RED);s.arrow(680,y+140,680,y+85,GREEN,3)
            label(s,80,y-60,'Lab: neutral wire, I →' if row==0 else 'Test-charge rest frame: net negative wire',INK,22,1200)
            if row==0:s.arrow(700,y+140,840,y+140,RED,3)
        footer(s,'Lab: positive test charge moves parallel to I and is attracted magnetically.', 'Charge frame: λ′ = −γv I/c² < 0, so attraction is electric. Density sketches are schematic, not fixed-spacing claims.')
    else:raise ValueError(n)
    return s


def induction(n,title):
    s=Scene(f'emi-ac:D20.{n}');s.title(title,'Induction & AC · positive circulation and area normal are paired by the right-hand rule.')
    if n==1:
        for i,theta in enumerate([0,60,90,180]):
            x=180+330*i;panel(s,x-125,155,290,480,f'θ = {theta}°')
            arc(s,x,390,95,0,TAU,BLUE,ry=max(10,95*abs(math.cos(math.radians(theta)))))
            s.arrow(x,390,x+80*math.sin(math.radians(theta)),390-120*math.cos(math.radians(theta)),GREEN,3)
            s.arrow(x-80,560,x-80,235,BLUE,3);label(s,x-50,560,['BA','BA/2','0','−BA'][i],RED,24,200)
        footer(s,'Φ = B · A = BA cosθ; θ is between B and the oriented area normal, not the plane.', 'Reversing the chosen normal changes the flux sign and the positive loop circulation together.')
    elif n==2:
        for i,t in enumerate(['Magnet approaches','Magnet recedes','Primary current grows','Loop rotates']):
            x=65+335*i;panel(s,x,145,315,520,t);arc(s,x+160,385,85,0,TAU*.95,BLUE,True,ry=125)
            if i<2:
                s.rect(x+15,355,75,50,RED,'#faeceb');label(s,x+26,363,'N',RED,22,40)
                s.arrow(x+40 if i==0 else x+105,440,x+105 if i==0 else x+40,440,GREEN,3)
                label(s,x+20,565,'Φ grows' if i==0 else 'Φ falls',INK,20,280)
            elif i==2:coil(s,x+10,x+85,350);label(s,x+20,565,'switch: ΔI₁ → ΔΦ₂',INK,18,280)
            else:s.arrow(x+160,385,x+230,290,GREEN,3);label(s,x+20,565,'changing orientation',INK,18,280)
        footer(s,'Induced current opposes the change in linked flux, not necessarily the applied field itself.', 'Approach/recede reverse the current. No relative motion or current change → no induction.')
    elif n==3:
        field(s,130,150,1100,500);s.line(140,250,1130,250);s.line(140,590,1130,590)
        s.line(920,250,920,590,ORANGE,7);s.arrow(950,425,1100,425,GREEN,4)
        label(s,925,205,'+',RED,26);label(s,925,600,'−',BLUE,26)
        s.arrow(875,455,875,340,RED,3);s.arrow(1020,320,1020,520,BLUE,3)
        label(s,630,315,'q(v × B) ↑',RED);label(s,1060,330,'E ↓',BLUE,20,230)
        s.line(140,250,140,365);s.line(140,465,140,590);resistor(s,90,190,415)
        s.arrow(730,250,490,250,RED,3);s.arrow(140,295,140,350,RED,3)
        footer(s,'v right, B into the page: positive carriers are pushed up, so the rod’s top is positive.', 'EMF = Blv; E_inside = −v × B. Closed rails carry anticlockwise current and magnetic drag opposes motion.')
    elif n==4:
        s.rect(270,170,45,480,INK,'#e4e4e4');s.rect(555,170,45,480,INK,'#e4e4e4')
        s.rect(385,320,100,160,INK,'#e9f2fb');label(s,414,335,'S',BLUE,24);label(s,414,435,'N',RED,24)
        arc(s,435,250,140,0,TAU*.9,BLUE,True,ry=25);arc(s,435,550,140,0,-TAU*.9,RED,True,ry=25)
        s.arrow(660,360,660,505,GREEN,4);s.arrow(735,505,735,360,RED,4)
        label(s,665,530,'mg ↓; drag ↑',INK)
        axes(s,900,560,350,240,'t','v');graph(s,lambda t:1-math.exp(-t),0,5,900,560,340,210)
        footer(s,'Magnet’s N pole is below: approaching lower ring presents N upward; upper ring presents N downward.', 'Both induced forces oppose descent. Linear-drag model: v_t = mg/K, τ = m/K; timing depends on apparatus.')
    elif n==5:
        panel(s,60,135,400,540,'Rotating rod');panel(s,490,135,400,540,'Rotating loop');panel(s,920,135,400,540,'Loop leaving field')
        s.dot(170,450,7);s.line(170,450,395,260,INK,4)
        for t in [.3,.6,.9]:
            x=170+225*t;y=450-190*t;s.arrow(x,y,x+65*t,y+77*t,GREEN,3)
        label(s,90,570,'dEMF = Bωr dr',INK,20,340)
        axes(s,530,515,300,180,'ωt','Φ and EMF')
        graph(s,math.cos,0,TAU,530,420,285,70,BLUE);graph(s,math.sin,0,TAU,530,420,285,70,RED)
        field(s,950,240,160,300);s.rect(1020,295,225,230,INK,'transparent',3);s.arrow(1110,565,1260,565,GREEN,3)
        label(s,945,605,'only inside vertical side: Blv',INK,17,350)
        footer(s,'Pivoted rod: EMF = ½BωL². Rotating loop: Φ = BA cosωt, EMF = BAω sinωt.', 'A translating closed loop entirely inside uniform B has zero total motional EMF; partial overlap does not.')
    elif n==6:
        panel(s,65,140,625,530,'Resistive rails + hanging mass');panel(s,735,140,595,530,'Capacitive rails: effective inertia')
        for x in [90,770]:
            s.line(x,290,x+500,290);s.line(x,510,x+500,510);s.line(x+300,290,x+300,510,ORANGE,5)
            s.arrow(x+320,400,x+470,400,GREEN,3);field(s,x+30,300,450,200)
        resistor(s,90,215,400);s.line(90,290,90,400);s.line(90,400,90,510)
        s.line(390,400,660,400);arc(s,660,420,20);s.line(680,420,680,600);s.rect(645,600,70,45,INK,WHITE)
        cap(s,770,920,400);s.line(770,290,770,400);s.line(770,400,770,510)
        label(s,120,555,'rod: T →, magnetic drag ←',INK,19,540)
        label(s,780,555,'F = (m + CB²l²)a',BLUE,22,530)
        footer(s,'Resistive circuit: magnetic drag = B²l²v/R; hanging mass has mg − T = M a.', 'Capacitor: q = CBlv, i = CBla, so electrical storage adds effective mass CB²l².')
    elif n==7:
        for x in [355,1040]:
            s.ellipse(x-140,240,280,280,GRID,'#e9f2fb');symbol(s,x,380,True,BLUE,22)
            for r in [70,120,200]:arc(s,x,380,r,0,-TAU*.94,RED,True)
        label(s,100,155,'Inside: |E| = r |dB/dt|/2',RED,22,620);label(s,790,155,'Outside: |E| = R² |dB/dt|/(2r)',RED,22,650)
        s.dot(1240,380,8,GREEN);s.arrow(1240,380,1240,445,GREEN,3)
        footer(s,'B out of the page and increasing → induced E circulates clockwise, including outside where B = 0.', 'The induced electric field is nonconservative: ∮E · dℓ = −dΦ_B/dt.')
    elif n==8:
        arc(s,340,400,190);symbol(s,340,400,True,BLUE,20);arc(s,340,400,190,0,-TAU*.94,RED,True)
        label(s,150,650,'electron acceleration is opposite E',RED,20,600)
        axes(s,790,600,440,280,'r/R','B/B_orbit')
        # 3−2(r/R)^2 gives weighted mean 2 and edge value 1.
        graph(s,lambda u:(3-2*u*u)/3,0,1,790,600,420,270)
        s.line(790,420,1210,420,ORANGE,2,'dashed');label(s,820,375,'mean = 2 B_orbit',ORANGE)
        label(s,1060,515,'edge = B_orbit',BLUE,18,300)
        footer(s,'Fixed orbit condition: ⟨B⟩_area = 2 B_orbit; p = e B_orbit R.', 'Profile illustrates only the 2:1 flux condition, not stable orbit focusing (edge field index n = 4).')
    elif n==9:
        s.rect(220,250,470,270,INK,'#f4f6f9');field(s,470,160,330,420)
        arc(s,450,380,100,0,TAU*.95,RED,True,ry=70);s.arrow(710,420,840,420,GREEN,3);s.arrow(560,560,390,560,RED,4)
        label(s,165,620,'motion →; induced magnetic force ←',INK,20,650)
        s.rect(910,220,270,290,INK,'transparent');arc(s,1040,365,100,0,TAU*.9,RED,True)
        for i in range(8):s.rect(1230+i*15,220,10,290,GRID,WHITE)
        label(s,905,570,'solid core',INK,20,300);label(s,1160,620,'lamination interrupts loops',BLUE,18,250)
        footer(s,'Eddy currents oppose entry and dissipate I²R heat; the braking energy comes from mechanical work.', 'Thin insulated laminations suppress transverse loops; classical eddy loss scales with thickness².')
    elif n==10:
        for x,t in [(100,'slip rings: AC'),(710,'commutator: rectified')]:
            s.rect(x+75,225,200,120,INK,'transparent');s.arrow(x+165,390,x+165,190,GREEN,3)
            label(s,x+40,150,t,BLUE,22,580);axes(s,x,620,500,190,'ωt','output')
        graph(s,math.sin,0,2*TAU,100,530,470,65,BLUE)
        graph(s,lambda t:abs(math.sin(t)),0,2*TAU,710,620,470,130,RED)
        footer(s,'Generator: mechanical work supplies electrical output; commutation reverses connection every half-turn.', 'Motor: V = iR + back EMF, back EMF = kω; i = (V − kω)/R. Starting current is V/R.')
    elif n==11:
        arc(s,665,385,210);symbol(s,665,385,False,BLUE,26)
        label(s,620,420,'dΦ/dt',BLUE,20,300);s.dot(665,175,6);s.dot(665,595,6)
        curve(s,[(665,175),(220,175),(220,595),(665,595)],GREEN);curve(s,[(665,175),(1110,175),(1110,595),(665,595)],RED)
        label(s,190,355,'meter path 1',GREEN);label(s,900,355,'meter path 2',RED)
        label(s,390,440,'R₁',INK);label(s,850,440,'R₂',INK)
        footer(s,'For the same endpoints, two lead routes enclosing changing flux can give different signed readings.', 'Their difference is the EMF around the combined contour; define probe polarity and lead path before numbers.')
    elif n==12:
        loop_field(s,100,260,430,220);s.rect(310,270,40,200,RED,'#faeceb')
        label(s,110,570,'one turn: Φ; N turns: Λ = NΦ',BLUE,21,600)
        s.rect(790,245,480,45,INK,'#e4e4e4');s.rect(790,500,480,45,INK,'#e4e4e4');s.rect(980,290,35,210,ORANGE,'#fbf0e3')
        for y in [330,390,450]:symbol(s,950,y,True,BLUE)
        label(s,800,180,'coaxial annulus, a < r < b',INK,22);label(s,1010,600,'flux strip ℓ dr',ORANGE,20,320)
        footer(s,'Λ = NΦ = LI, not N²Φ. Long solenoid L = μ₀N²A/ℓ.', 'Coax external inductance: dΦ = μ₀Iℓ dr/(2πr); L = μ₀ℓ ln(b/a)/(2π), ignoring internal flux.')
    elif n==13:
        loop_field(s,130,285,480,180);s.rect(300,250,150,250,RED,'transparent',3)
        label(s,150,580,'inner flux also links outer coil',BLUE,21,650)
        arc(s,1030,395,190,0,TAU,BLUE,ry=55);arc(s,1030,395,55,0,TAU,RED,ry=190)
        label(s,840,615,'perpendicular centred axes: M = 0',INK,20,490)
        footer(s,'For overlapping coaxial solenoids: M = μ₀ n₁ N₂ A₁ when the outer turns enclose the inner area.', 'Perpendicular symmetric coils have zero net mutual flux by symmetry; M₁₂ = M₂₁.')
    elif n==14:
        s.line(130,250,1130,250);s.line(130,570,1130,570)
        battery(s,130,410,320);s.line(1130,250,1130,570)
        s.rect(460,235,400,30,WHITE,WHITE,0);resistor(s,450,640,250);s.line(640,250,690,250);coil(s,690,900,250)
        # source top positive, current rightward; diode reverse-biased during supply
        s.line(690,250,690,430);s.line(900,250,900,430);s.line(690,430,760,430);s.line(830,430,900,430)
        s.line(760,405,760,455,RED,3);curve(s,[(830,405),(760,430),(830,455),(830,405)],RED)
        label(s,650,465,'flyback diode: right → left only',RED,20,600)
        s.arrow(710,320,850,320,GREEN,3);label(s,600,170,'i grows: inductor opposes rise',INK,20,680)
        footer(s,'Closing: i = (V/R)(1 − e^(−tR/L)). Inductor current cannot jump with finite applied voltage.', 'Opening: polarity reverses to sustain i. The reverse-biased flyback diode provides a safe decay path.')
    elif n==15:
        loop_field(s,100,240,520,240);s.rect(340,250,50,220,RED,'#faeceb')
        label(s,130,590,'dU = [B²/(2μ₀)] A dx',RED,23,640)
        axes(s,830,580,420,310,'I','flux linkage Λ')
        curve(s,[(830,580),(1220,285),(1220,580),(830,580)],BLUE)
        s.arrow(830,580,1220,285,BLUE,3);label(s,1050,220,'Λ = LI',BLUE,23)
        label(s,860,490,'linear coenergy = ∫Λ dI = ½LI²',INK,20,450)
        footer(s,'Field energy density = B²/(2μ₀); at 1.5 T it is about 0.895 MJ m⁻³.', 'The energy triangle uses Λ versus I, not back EMF versus I: EMF depends on dI/dt.')
    elif n==16:
        for x in [160,480]:
            coil(s,x,x+200,300);s.dot(x+15,265,6,RED)
        s.arrow(160,350,360,350,GREEN,3);s.arrow(480,350,680,350,GREEN,3)
        label(s,130,450,'Both enter dots: L₁ + L₂ + 2M',BLUE,23,700)
        label(s,130,500,'Opposite dot signs: L₁ + L₂ − 2M',RED,23,700)
        axes(s,860,590,360,280,'gap x','M');graph(s,lambda x:math.exp(-x),0,3,860,590,350,230)
        s.arrow(900,220,1050,220,GREEN,3);s.arrow(1220,220,1070,220,GREEN,3)
        footer(s,'Dot convention describes the relative winding polarity, not a permanently positive voltage terminal.', 'At fixed aiding currents: F_x = I₁I₂ dM/dx; M decreases with separation, so force tends to close the gap.')
    elif n==17:
        for i,(q,j) in enumerate([(1,0),(0,1),(-1,0),(0,-1)]):
            x=75+335*i;panel(s,x,140,300,535,f'phase {90*i}°')
            cap(s,x+30,x+270,290);coil(s,x+30,x+270,480)
            s.line(x+30,290,x+30,480);s.line(x+270,290,x+270,480)
            label(s,x+70,350,f'q/Q = {q}',RED,23,210)
            if j:s.arrow(x+80 if j>0 else x+230,530,x+230 if j>0 else x+80,530,BLUE,3)
            label(s,x+50,590,'energy in C' if q else 'energy in L',INK,19,250)
        footer(s,'q = Q cosω₀t, ω₀ = 1/√(LC). Current is a quarter-cycle shifted; energy swaps between C and L.', 'Mechanical twin: capacitor charge ↔ spring displacement, current ↔ velocity, L ↔ mass.')
    elif n==18:
        for i,phase in enumerate([0,-math.pi/2,math.pi/2]):
            x=90+440*i;panel(s,x-30,140,415,520,['R: in phase','L: i lags','C: i leads'][i])
            axes(s,x,470,330,180,'ωt','v (red), i (blue)')
            graph(s,math.sin,0,TAU,x,395,315,90,RED)
            graph(s,lambda t:math.sin(t+phase),0,TAU,x,395,315,90,BLUE)
            label(s,x,570,['Z = R','X_L = ωL','X_C = 1/(ωC)'][i],INK,22,370)
        footer(s,'Using v = V₀ sinωt: i_R ∝ sinωt, i_L ∝ −cosωt, i_C ∝ cosωt.', 'Reactance magnitudes: inductive increases with ω, capacitive decreases; impedance includes phase.')
    elif n==19:
        for i,t in enumerate(['Series RC','Series RL','Series RLC']):
            x=200+450*i;panel(s,x-135,160,405,485,t)
            s.arrow(x,425,x+160,425,GREEN,3);label(s,x+125,455,'I, V_R',GREEN,18,230)
            up=[-120,120,100][i];s.arrow(x+160,425,x+160,425-up,BLUE,3)
            s.arrow(x,425,x+160,425-up,RED,4);label(s,x-40,560,'V = vector sum',RED,19,350)
            if i==2:s.arrow(x+220,425,x+220,290,BLUE,2);s.arrow(x+220,425,x+220,475,PURPLE,2)
        footer(s,'Reference current along +x: V_L leads by +90° (up), V_C lags by −90° (down).', 'tanφ = (X_L − X_C)/R; |Z| = √[R² + (X_L − X_C)²]. Draw signed reactances before adding.')
    elif n==20:
        axes(s,100,600,670,340,'ωt','p/(V₀I₀)')
        phi=math.pi/3;graph(s,lambda t:math.sin(t)*math.sin(t-phi),0,2*TAU,100,500,650,200,RED)
        s.line(100,450,750,450,GREEN,2,'dashed');label(s,120,220,'mean = ½cosφ = ¼',GREEN)
        s.arrow(920,565,1260,565,GREEN,3);s.arrow(1260,565,1260,300,BLUE,3);s.arrow(920,565,1260,300,RED,3)
        label(s,1080,590,'P (W)',GREEN);label(s,1280,425,'Q (var)',BLUE,20,140);label(s,1020,380,'S (VA)',RED)
        footer(s,'p(t) = V₀I₀[cosφ − cos(2ωt − φ)]/2; negative lobes mean energy returned to the source.', 'P = V_rms I_rms cosφ; S² = P² + Q². A parallel capacitor offsets positive inductive reactive power.')
    elif n==21:
        s.rect(330,190,480,390,INK,'#f4f6f9');s.rect(440,270,260,230,INK,WHITE)
        coil(s,170,410,380,'Np');coil(s,730,990,380,'Ns')
        s.arrow(540,225,720,225,BLUE,3);label(s,450,140,'common core flux Φ(t)',BLUE,23,660)
        label(s,880,520,'load Z_s',INK,22)
        label(s,90,645,'station → step-up → line → step-down → load',GREEN,24,1250)
        footer(s,'Ideal: V_s/V_p = N_s/N_p; I_s/I_p = N_p/N_s; input reflected impedance = (N_p/N_s)² Z_s.', 'Line loss = I²R. For fixed transmitted power, increasing voltage by 20× reduces line loss by 400×.')
    elif n==22:
        for x,t,fn in [(100,'half-wave',lambda u:max(0,math.sin(u))),(760,'full-wave',lambda u:abs(math.sin(u)))]:
            label(s,x,160,t,BLUE,23);axes(s,x,440,510,210,'ωt','rectified output')
            graph(s,fn,0,2*TAU,x,440,480,160,BLUE)
        pts=[(140+1050*t,585+50*((t*8)%1)) for t in [i/799 for i in range(800)]];curve(s,pts,RED)
        label(s,150,655,'Smoothing capacitor: fast recharge, slow decay between successive peaks',RED,21,1200)
        footer(s,'Bridge full-wave recharge rate = 2f; small ripple ΔV ≈ I_load/(2fC). Half-wave uses f instead.', 'The silicon 0.7 V drop is a rough operating approximation, not a universal sharp threshold.')
    else:raise ValueError(n)
    return s


def current(n):
    """Analytic replacements for misleading curve shapes or circuit symbols."""
    s=Scene(f'current-electricity:D19.{n}')
    if n in (12,20):
        s.title('Maximum load power occurs at resistance matching','Linear Thevenin source with fixed open-circuit EMF and positive internal resistance.')
        axes(s,150,620,1000,350,'R_load / R_source','P_load / P_max')
        graph(s,lambda z:4*z/(1+z)**2,0,8,150,620,980,300)
        s.dot(150+980/8,320,6,RED);label(s,180,220,'Match: R_load = R_source',RED,24,1000)
        footer(s,'P_load = V_th² R_load/(R_source + R_load)²; P_max = V_th²/(4R_source).', 'At matching, efficiency is 50%. Larger load resistance improves efficiency but reduces delivered power.')
    elif n==13:
        s.title('Power ledger: fractions and total power are different','Same cell EMF ε and internal resistance r; bar widths show absolute power in units ε²/r.')
        for i,z in enumerate([1,3,1/3]):
            y=210+155*i;total=1000/(1+z);load=total*z/(1+z)
            s.rect(210,y,load,65,GREEN,'#e8f4ec');s.rect(210+load,y,total-load,65,RED,'#faeceb')
            label(s,70,y+15,f'R/r = {z:.3g}',INK,21,180)
            label(s,230,y+80,f'load {100*z/(1+z):.0f}%; internal {100/(1+z):.0f}%; total εI changes',INK,19,1000)
        footer(s,'εI = I²R + I²r. The fractions change and the absolute chemical power changes too.', 'Do not use equal total bar widths for unequal currents unless explicitly normalising each row.')
    elif n==17:
        s.title('RC charging: voltage rises, current decays','Normalised curves use the same time scale τ = RC; current and voltage have different physical units.')
        axes(s,150,620,1000,360,'t/τ','V_C/ε (blue), i/(ε/R) (red)')
        graph(s,lambda t:1-math.exp(-t),0,5,150,620,980,300,BLUE);graph(s,lambda t:math.exp(-t),0,5,150,620,980,300,RED)
        for t in [1,2,3,5]:s.line(150+980*t/5,620,150+980*t/5,320,GRID,1,'dashed');label(s,150+980*t/5,650,str(t),INK,18,70)
        footer(s,'V_C = ε(1 − e^(−t/τ)), i = (ε/R)e^(−t/τ); at τ: V_C = 0.632ε.', 'At 5τ, charge is 99.33% of its final value. Capacitor voltage is continuous across a finite-resistance switch.')
    elif n==25:
        s.title('Thermistor thermal stability: compare heating and cooling rates','Local exponential NTC model R(T) = R₀e^(−βΔT); constant heat-loss conductance G_th.')
        axes(s,150,620,1000,340,'u = βΔT','normalised power')
        graph(s,lambda u:.22*math.exp(u),0,2.2,150,620,980,120,RED)
        graph(s,lambda u:u,0,2.2,150,620,980,120,BLUE)
        label(s,800,240,'heating ∝ exp(u)',RED);label(s,800,290,'cooling ∝ u',BLUE)
        footer(s,'C_th dT/dt = V²/R(T) − G_th(T−T₀). Stability requires derivative of net heating < 0.', 'For this model the low-temperature intersection is stable; the high-temperature intersection is unstable.')
    else:return None
    return s


def main():
    for slug,(name,part,count) in TOPICS.items():
        master=ROOT/slug/name;source=master.read_text()
        manifest_path=ROOT/slug/'figures.json'
        manifest=json.loads(manifest_path.read_text()) if manifest_path.exists() else {'slug':slug,'policy':'docs/obsidian-plugin-workflow.md §2','figures':[]}
        drawings=[]
        if slug=='current-electricity':
            matches=list(re.finditer(r'(?m)^!\[([^\n\]]+)\]\((assets/figures/fig-(\d+)\.svg)\)$',source))
            assert {int(m[3]) for m in matches}==set(range(1,count+1))
        else:
            matches=list(re.finditer(r'(?m)^> \[!abstract\] DIAGRAM (D\d+\.(\d+)) · ([^\n]+)\n((?:>[^\n]*\n)*)',source))
            assert [int(m[2]) for m in matches]==list(range(1,count+1))
        for n in range(1,count+1):
            id_=f'D{part}.{n}'
            if slug=='current-electricity':
                m=next(m for m in matches if int(m[3])==n);title=m[1]
                scene=current(n) or converted_scene(slug,ROOT/slug/m[2],f'{slug}:{id_}')
                show='Editable companion; analytic curve corrections are described in the retrofit status.'
                search=f'Local SVG source {slug}/{m[2]}';origin=f'{slug}/{name} · {m[2]}'
            else:
                m=matches[n-1];title=m[3]
                show=re.search(r'> \*Show:\* (.*)',m[4])[1];search=re.search(r'> \*Search:\* (.*)',m[4])[1]
                scene=magnetic(n,title) if slug=='magnetism' else induction(n,title)
                origin=f'{slug}/{name} · {id_}'
            stem,file=scene_file(slug,id_,title,scene);embed=f'![[../_obsidian/excalidraw/{stem}|900]]'
            if source.count(embed)>1:raise ValueError(f'duplicate {embed}')
            if embed not in source:
                if slug=='current-electricity':
                    block=(f'\n\n> [!abstract] DIAGRAM {id_} — {title}\n> **Show:** {show}\n> **Source:** `{slug}/{m[2]}`; retained.\n> **Read:** {title.rstrip(".")}.\n\n{embed}')
                    source=source.replace(m[0],m[0]+block,1)
                else:source=source.replace(m[0],m[0]+'\n'+embed+'\n',1)
            drawings.append(dict(id=id_,kind='excalidraw',title=title,show=show,search=search,file=file,source=origin))
        if slug!='current-electricity':
            # Mermaid source lives in the master; keep exact identifiers/titles for provenance.
            manifest['figures']=[dict(id=m[1],kind='mermaid',title=m[2],source=f'{slug}/{name}')
                for m in re.finditer(r'^> \[!tip\] FIGURE (F\d+\.\d+) · ([^\n]+)',source,re.M)]
        manifest.update(drawings=drawings,renderer='obsidian-excalidraw-plugin@2.27.3',
                        drawing_numbering='Chapter-local IDs: Current Electricity D19; existing Magnetism D16 and EMI/AC D20 briefs retained. Always qualify by topic slug.')
        master.write_text(source);manifest_path.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
        print(f'{slug}: {count} native editable scenes')


if __name__=='__main__':main()
