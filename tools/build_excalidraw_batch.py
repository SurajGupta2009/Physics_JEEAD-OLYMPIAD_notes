#!/usr/bin/env python3
"""Generate reviewed Excalidraw scene files for a chapter's DIAGRAM briefs.

The batch covers PARTS 1–7 (units, vectors, kinematics, and mechanics). The
scene JSON uses the Excalidraw v2 schema and is stored in native
``.excalidraw.md`` files under the vault's configured ``_obsidian/excalidraw``
folder. Open the vault with the pinned Excalidraw plugin to view/edit and
auto-export SVG previews.

Run from the repository root:
    python3 tools/build_excalidraw_batch.py
"""
from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "_obsidian" / "excalidraw"
INK = "#243447"
MUTED = "#617386"
GRID = "#d6dee8"
BLUE = "#2767a8"
TEAL = "#138a83"
GREEN = "#26865b"
RED = "#bd4b4b"
ORANGE = "#d07a28"
PURPLE = "#7058a5"
PALE_BLUE = "#e9f2fb"
PALE_TEAL = "#e5f5f2"
PALE_GREEN = "#e8f4ec"
PALE_RED = "#faeceb"
PALE_ORANGE = "#fbf0e3"
WHITE = "#ffffff"


class Scene:
    """Small deterministic Excalidraw element builder; no external dependencies."""

    def __init__(self, key: str):
        self.key = key
        self.elements: list[dict] = []
        self.counter = 0

    def _base(self, typ: str, x: float, y: float, w: float, h: float,
              stroke: str = INK, background: str = "transparent",
              stroke_width: float = 2, fill_style: str = "solid") -> dict:
        self.counter += 1
        token = hashlib.sha256(f"{self.key}:{self.counter}".encode()).hexdigest()
        return {
            "id": token[:20], "type": typ, "x": x, "y": y,
            "width": w, "height": h, "angle": 0,
            "strokeColor": stroke, "backgroundColor": background,
            "fillStyle": fill_style, "strokeWidth": stroke_width,
            "strokeStyle": "solid", "roughness": 0, "opacity": 100,
            "groupIds": [], "frameId": None, "roundness": None,
            "seed": int(token[20:28], 16), "version": 1,
            "versionNonce": int(token[28:36], 16), "isDeleted": False,
            "boundElements": None, "updated": 0, "link": None, "locked": False,
        }

    def text(self, x: float, y: float, value: str, size: int = 20,
             color: str = INK, width: float = 300,
             align: str = "left", valign: str = "top") -> None:
        lines = value.split("\n")
        h = max(1, len(lines)) * size * 1.35 + 8
        e = self._base("text", x, y, width, h, stroke=color)
        e.update({
            "fontSize": size, "fontFamily": 2, "text": value,
            "textAlign": align, "verticalAlign": valign,
            "containerId": None, "originalText": value,
            "autoResize": True, "lineHeight": 1.35,
        })
        self.elements.append(e)

    def rect(self, x: float, y: float, w: float, h: float,
             stroke: str = INK, background: str = "transparent",
             sw: float = 2, roundness: bool = False, angle: float = 0) -> None:
        e = self._base("rectangle", x, y, w, h, stroke, background, sw)
        if angle:
            e["angle"] = angle
        if roundness:
            e["roundness"] = {"type": 3}
        self.elements.append(e)

    def ellipse(self, x: float, y: float, w: float, h: float,
                stroke: str = INK, background: str = "transparent",
                sw: float = 2) -> None:
        self.elements.append(self._base("ellipse", x, y, w, h, stroke, background, sw))

    def line(self, x1: float, y1: float, x2: float, y2: float,
             color: str = INK, sw: float = 2, dash: str = "solid") -> None:
        left, top = min(x1, x2), min(y1, y2)
        e = self._base("line", left, top, abs(x2-x1), abs(y2-y1), color, "transparent", sw)
        e["strokeStyle"] = dash
        e["points"] = [[x1-left, y1-top], [x2-left, y2-top]]
        e["lastCommittedPoint"] = None
        e["startBinding"] = None
        e["endBinding"] = None
        e["startArrowhead"] = None
        e["endArrowhead"] = None
        self.elements.append(e)

    def arrow(self, x1: float, y1: float, x2: float, y2: float,
              color: str = BLUE, sw: float = 2.5,
              start: str | None = None, end: str | None = "arrow") -> None:
        left, top = min(x1, x2), min(y1, y2)
        e = self._base("arrow", left, top, abs(x2-x1), abs(y2-y1), color, "transparent", sw)
        e["points"] = [[x1-left, y1-top], [x2-left, y2-top]]
        e["lastCommittedPoint"] = None
        e["startBinding"] = None
        e["endBinding"] = None
        e["startArrowhead"] = start
        e["endArrowhead"] = end
        self.elements.append(e)

    def dot(self, cx: float, cy: float, r: float = 5, color: str = BLUE) -> None:
        self.ellipse(cx-r, cy-r, 2*r, 2*r, color, color, 1)

    def title(self, text: str, subtitle: str | None = None) -> None:
        self.text(38, 24, text, 30, INK, 1250)
        if subtitle:
            self.text(40, 66, subtitle, 16, MUTED, 1250)

    def json(self) -> dict:
        return {
            "type": "excalidraw", "version": 2,
            "source": "https://excalidraw.com",
            "elements": self.elements,
            "appState": {
                "gridSize": None, "viewBackgroundColor": WHITE,
                "currentItemFontFamily": 2,
                "currentItemStrokeColor": INK,
                "currentItemBackgroundColor": "transparent",
                "currentItemFillStyle": "solid", "currentItemStrokeWidth": 2,
                "currentItemStrokeStyle": "solid", "currentItemRoughness": 0,
                "currentItemOpacity": 100,
            },
            "files": {},
        }


def scene_file(topic_slug: str, diagram_id: str, title: str, s: Scene) -> tuple[str, str]:
    slug = f"{topic_slug}-{diagram_id.replace('.', '-')}.excalidraw"
    document = (
        "---\n"
        "excalidraw-plugin: raw\n"
        "excalidraw-autoexport: svg\n"
        "tags: [excalidraw, physics-diagram]\n"
        f"diagram-id: {diagram_id}\n"
        f"title: {json.dumps(title, ensure_ascii=False)}\n"
        "---\n"
        "==⚠ Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠==\n\n"
        "# Text Elements\n%%\n\n# Drawing\n```json\n"
        + json.dumps(s.json(), ensure_ascii=False, indent=2)
        + "\n```\n%%\n"
    )
    path = OUT / f"{slug}.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(document, encoding="utf-8")
    return slug, str(path.relative_to(ROOT))


def d11() -> Scene:
    s = Scene("D1.1"); s.title("The seven SI base units", "Modern SI: each unit is defined by fixing an exact value of a fundamental constant.")
    x0, y0 = 42, 112
    widths = [250, 170, 95, 950]
    headers = ["BASE QUANTITY", "UNIT", "SYMBOL", "MODERN DEFINITION (FIXED CONSTANT)"]
    xs = [x0]
    for w in widths: xs.append(xs[-1] + w)
    row_h = 83; rows = [
        ("Length", "metre", "m", "c = 299,792,458 m s⁻¹ exactly; 1 m is the distance light travels in 1/299,792,458 s."),
        ("Mass", "kilogram", "kg", "h = 6.62607015 × 10⁻³⁴ J s exactly."),
        ("Time", "second", "s", "ΔνCs = 9,192,631,770 Hz exactly."),
        ("Electric current", "ampere", "A", "e = 1.602176634 × 10⁻¹⁹ C exactly."),
        ("Thermodynamic temperature", "kelvin", "K", "kB = 1.380649 × 10⁻²³ J K⁻¹ exactly."),
        ("Amount of substance", "mole", "mol", "NA = 6.02214076 × 10²³ mol⁻¹ exactly."),
        ("Luminous intensity", "candela", "cd", "Kcd = 683 lm W⁻¹ at 540 × 10¹² Hz exactly."),
    ]
    total_w = sum(widths); total_h = row_h * (len(rows)+1)
    s.rect(x0, y0, total_w, total_h, GRID, WHITE, 1)
    s.rect(x0, y0, total_w, row_h, BLUE, PALE_BLUE, 1)
    for x in xs[1:-1]: s.line(x, y0, x, y0+total_h, GRID, 1)
    for i in range(1, len(rows)+1): s.line(x0, y0+i*row_h, x0+total_w, y0+i*row_h, GRID, 1)
    for i, h in enumerate(headers): s.text(xs[i]+10, y0+22, h, 15, BLUE, widths[i]-20)
    for r, row in enumerate(rows):
        yy = y0+(r+1)*row_h+23
        for c, value in enumerate(row):
            s.text(xs[c]+10, yy, value, 16 if c != 3 else 15, INK if c != 2 else TEAL, widths[c]-20)
    return s


def d12() -> Scene:
    s = Scene("D1.2"); s.title("Dimensional homogeneity: every term in a sum must match")
    s.rect(40, 115, 710, 395, GREEN, PALE_GREEN, 2, True)
    s.text(66, 137, "VALID · constant-acceleration displacement", 20, GREEN, 650)
    s.text(76, 198, "s = ut + ½at²", 30, INK, 620)
    labels = [("s", "[L]"), ("ut", "[L T⁻¹][T] = [L]"), ("½at²", "[L T⁻²][T²] = [L]")]
    xx = [92, 285, 507]
    for x, (term, dim) in zip(xx, labels):
        s.rect(x, 273, 175, 112, GREEN, WHITE, 1.5, True)
        s.text(x+10, 292, term, 22, INK, 155, "center")
        s.line(x+12, 328, x+163, 328, GRID, 1)
        s.text(x+10, 342, dim, 15, GREEN, 155, "center")
    s.text(91, 424, "[L] = [L] + [L]  ✓", 21, GREEN, 560)
    s.rect(790, 115, 710, 395, RED, PALE_RED, 2, True)
    s.text(816, 137, "INVALID · the last term has the wrong dimension", 20, RED, 660)
    s.text(828, 198, "s = ut + at", 30, INK, 620)
    bad = [("s", "[L]"), ("ut", "[L T⁻¹][T] = [L]"), ("at", "[L T⁻²][T] = [L T⁻¹]")]
    xx = [842, 1035, 1257]
    for i, (x, (term, dim)) in enumerate(zip(xx, bad)):
        s.rect(x, 273, 175, 112, RED if i == 2 else GRID, WHITE, 1.5, True)
        s.text(x+10, 292, term, 22, INK, 155, "center")
        s.line(x+12, 328, x+163, 328, GRID, 1)
        s.text(x+7, 342, dim, 14, RED if i == 2 else MUTED, 160, "center")
    s.text(842, 424, "[L] = [L] + [L T⁻¹]  ✕", 21, RED, 600)
    return s


def d13() -> Scene:
    s = Scene("D1.3"); s.title("Fractional-error table for Z = A²B/C", "Let eA = ΔA/|A|, eB = ΔB/|B|, eC = ΔC/|C|.")
    x0, y0 = 68, 142; widths = [180, 120, 270, 280, 260]; row_h = 76
    heads = ["VARIABLE", "POWER p", "INPUT FRACTION", "p × INPUT", "SQUARED TERM"]
    xs=[x0]
    for w in widths: xs.append(xs[-1]+w)
    rows=[("A", "2", "eA = ΔA/|A|", "2eA", "4eA²"),
          ("B", "1", "eB = ΔB/|B|", "eB", "eB²"),
          ("C", "−1", "eC = ΔC/|C|", "−eC", "eC²")]
    total=sum(widths); s.rect(x0,y0,total,row_h*4,GRID,WHITE,1)
    s.rect(x0,y0,total,row_h,BLUE,PALE_BLUE,1)
    for x in xs[1:-1]: s.line(x,y0,x,y0+row_h*4,GRID,1)
    for i in range(1,4): s.line(x0,y0+i*row_h,x0+total,y0+i*row_h,GRID,1)
    for i,h in enumerate(heads): s.text(xs[i]+8,y0+25,h,14,BLUE,widths[i]-16)
    for r,row in enumerate(rows):
        for c,v in enumerate(row): s.text(xs[c]+10,y0+(r+1)*row_h+25,v,17,INK,widths[c]-20)
    s.rect(68, 475, 1220, 96, TEAL, PALE_TEAL, 2, True)
    s.text(94, 493, "WORST-CASE BOUND", 15, TEAL, 220)
    s.text(340, 489, "ΔZ/|Z| ≤ 2eA + eB + eC", 22, INK, 880)
    s.rect(68, 600, 1220, 96, PURPLE, "#f0ecf7", 2, True)
    s.text(94, 618, "INDEPENDENT RANDOM ERRORS", 15, PURPLE, 250)
    s.text(390, 614, "σZ/|Z| = √(4eA² + eB² + eC²)", 22, INK, 850)
    s.text(70, 725, "Powers multiply fractional errors; the minus sign reverses the contribution, not its size in quadrature.", 16, MUTED, 1220)
    return s


def d14() -> Scene:
    s = Scene("D1.4"); s.title("Dimensional derivation of a pendulum period", "The small-angle period depends on m, L and g; dimensions determine the exponents, not the factor 2π.")
    # Pendulum sketch
    s.text(62, 125, "MODEL", 16, BLUE, 180)
    s.dot(190, 190, 8, INK); s.line(190,190,295,330,INK,3)
    s.ellipse(275,310,42,42,BLUE,PALE_BLUE,2)
    s.text(304, 316, "m", 18, INK, 40)
    s.text(212, 238, "L", 20, BLUE, 60)
    s.arrow(296,332,296,397,RED,2.5)
    s.text(307, 370, "mg", 16, RED, 70)
    s.text(55, 442, "Parameters: m [M],  L [L],  g [L T⁻²]", 16, MUTED, 360)
    s.line(450,118,450,565,GRID,2)
    s.text(500, 126, "MATCH DIMENSIONS", 16, BLUE, 400)
    s.text(505, 180, "T = k mᵃ Lᵇ gᶜ", 25, INK, 560)
    s.text(505, 238, "[T] = [M]ᵃ [L]ᵇ [L T⁻²]ᶜ", 21, INK, 700)
    s.text(520, 300, "M:  a = 0", 20, TEAL, 330)
    s.text(520, 345, "L:  b + c = 0", 20, TEAL, 330)
    s.text(520, 390, "T:  −2c = 1  ⇒  c = −½", 20, TEAL, 560)
    s.text(520, 435, "⇒  b = ½", 20, TEAL, 330)
    s.rect(500, 492, 740, 74, GREEN, PALE_GREEN, 2, True)
    s.text(526, 512, "T ∝ √(L/g)       (a = 0, b = ½, c = −½)", 21, GREEN, 700)
    return s


def d15() -> Scene:
    s = Scene("D1.5"); s.title("Significant figures: precision is carried by the written digits", "Leading zeros locate the decimal point; trailing zeros after a decimal can carry measured precision.")
    cards=[("0.00123", "3 significant figures", "leading zeros are placeholders", BLUE),
           ("1.23", "3 significant figures", "all three digits count", TEAL),
           ("1.230", "4 significant figures", "the final zero records precision", GREEN),
           ("1.2300", "5 significant figures", "both final zeros record precision", PURPLE),
           ("1230", "AMBIGUOUS", "use scientific notation to state precision", ORANGE)]
    x0=55; w=270; gap=20; y0=150
    for i,(num,label,note,col) in enumerate(cards):
        x=x0+i*(w+gap)
        s.rect(x,y0,w,330,col,WHITE,2,True)
        s.text(x+15,y0+24,f"EXAMPLE {i+1}",14,col,w-30)
        s.text(x+15,y0+90,num,36,INK,w-30,"center")
        s.line(x+18,y0+150,x+w-18,y0+150,GRID,1)
        s.text(x+15,y0+173,label,18,col,w-30,"center")
        s.text(x+22,y0+229,note,15,MUTED,w-44,"center")
    s.text(58, 525, "Precision belongs to the measurement as written—not to the numerical value alone.", 19, INK, 1350)
    return s


def d16() -> Scene:
    s = Scene("D1.6"); s.title("Catastrophic cancellation: subtracting nearly equal numbers", "The same absolute input uncertainty becomes a larger fraction of a shrinking difference.")
    s.rect(55,125,700,140,BLUE,PALE_BLUE,2,True)
    s.text(83,148,"A = 1.234     B = 1.231",26,INK,620)
    s.text(83,200,"A − B = 0.003  · leading digits cancel",21,BLUE,620)
    s.text(835,139,"Place values before subtraction",16,MUTED,550)
    for j,(lab,a,b,diff) in enumerate([("ones","1","1","0"),("tenths","2","2","0"),("hundredths","3","3","0"),("thousandths","4","1","3")] ):
        x=858+j*112
        s.text(x,187,lab,13,MUTED,98,"center")
        s.text(x+20,216,a,20,INK,30,"center")
        s.text(x+20,241,b,20,INK,30,"center")
        s.text(x+20,266,diff,20,TEAL if j==3 else MUTED,30,"center")
    s.text(58, 326, "For four-significant-figure inputs near 1.23, a rounding uncertainty of about 0.0005 per input gives ≈0.001 worst-case uncertainty in the difference.", 16, MUTED, 1360)
    s.text(58, 382, "Difference size", 17, BLUE, 250)
    s.text(780, 382, "Worst-case relative uncertainty (≈0.001 / difference)", 17, RED, 730)
    rows=[("0.030", "≈ 3.3%", 32), ("0.003", "≈ 33%", 170), ("0.0003", "≈ 333%", 520)]
    for i,(d,pct,bw) in enumerate(rows):
        y=425+i*76
        s.text(65,y+8,d,19,INK,150)
        s.rect(250,y,bw,34,RED,PALE_RED,1,True)
        s.text(800,y+5,pct,20,RED,200)
    s.text(58, 675, "Subtracting does not add precision: cancellation can make the relative error dominate the result.", 18, RED, 1320)
    return s


def d17() -> Scene:
    s = Scene("D1.7"); s.title("Standard error of the mean falls as 1/√n", "Independent measurements with population scatter σ:  σₓ̄/σ = 1/√n.")
    xL,yT,xR,yB=110,145,1000,620
    s.line(xL,yB,xR,yB,INK,2); s.line(xL,yB,xL,yT,INK,2)
    s.text(xL+255,yB+28,"Number of independent measurements, n (log scale)",17,INK,520,"center")
    s.text(42,210,"σₓ̄ / σ",16,INK,95)
    # log x positions n = 1,4,10,100,1000; y mapped from 0..1.
    def px(n: float) -> float: return xL + (math.log10(n)/3)*(xR-xL)
    def py(r: float) -> float: return yB - r*(yB-yT)
    for n,label in [(1,"1"),(10,"10"),(100,"100"),(1000,"1000")]:
        x=px(n); s.line(x,yT,x,yB,GRID,1,"dashed"); s.text(x-25,yB+5,label,14,MUTED,50,"center")
    for r in [0,.25,.5,.75,1]:
        y=py(r); s.line(xL,y,xR,y,GRID,1,"dashed"); s.text(xL-50,y-10,f"{r:.2g}",13,MUTED,40,"right")
    points=[(1,1),(4,.5),(10,.316),(100,.1),(1000,.03162)]
    coords=[(px(n),py(v)) for n,v in points]
    for a,b in zip(coords,coords[1:]): s.line(a[0],a[1],b[0],b[1],BLUE,3)
    for (n,v),(x,y) in zip(points,coords):
        s.dot(x,y,7,TEAL); s.text(x+10,y-26,f"n={n}\n{v:.3g}",14,TEAL,90)
    s.rect(1040,170,410,165,ORANGE,PALE_ORANGE,2,True)
    s.text(1060,190,"×4 measurements",15,ORANGE,260)
    s.text(1060,224,"σₓ̄ halves",24,INK,340)
    s.text(1060,290,"1 → 4",18,MUTED,300)
    s.rect(1040,385,410,165,PURPLE,"#f0ecf7",2,True)
    s.text(1060,405,"×10 improvement",15,PURPLE,280)
    s.text(1060,439,"needs ×100 n",24,INK,340)
    s.text(1060,505,"diminishing returns",17,MUTED,300)
    return s


def d18() -> Scene:
    s = Scene("D1.8"); s.title("Three error types on targets", "Accuracy describes closeness to the true value; precision describes the spread of repeated readings.")
    centers=[(280,"SYSTEMATIC", "precise, biased", RED),(760,"RANDOM", "unbiased on average, spread", BLUE),(1240,"GROSS", "cluster + outlier", ORANGE)]
    cy=345; radii=[112,78,44]
    for cx,label,caption,col in centers:
        s.text(cx-165,125,label,20,col,330,"center")
        s.text(cx-190,158,caption,15,MUTED,380,"center")
        for r in radii: s.ellipse(cx-r,cy-r,2*r,2*r,GRID,"transparent",1)
        s.line(cx-8,cy,cx+8,cy,INK,1); s.line(cx,cy-8,cx,cy+8,INK,1)
    # Deliberate systematic cluster: tight, offset from bullseye.
    for dx,dy in [(-12,-10),(-2,-9),(9,-12),(-9,0),(2,2),(11,0),(-3,10),(8,9)]: s.dot(280+dx+45,cy+dy-22,6,RED)
    # Random: broad, symmetric about the true centre.
    for dx,dy in [(-48,-25),(-28,30),(5,-47),(34,-20),(45,24),(16,44),(-43,15),(0,2),(27,4),(-8,40)]: s.dot(760+dx,cy+dy,6,BLUE)
    # Gross: mostly centered cluster plus one unmistakable outlier.
    for dx,dy in [(-13,-10),(-3,-8),(9,-12),(-10,3),(3,2),(12,1),(-2,12),(7,9)]: s.dot(1240+dx,cy+dy,6,ORANGE)
    s.dot(1240+78,cy-52,8,RED)
    s.arrow(1328,290,1364,268,RED,2)
    s.text(1360,240,"outlier",14,RED,90)
    s.text(115, 540, "Tightly grouped but displaced → systematic", 16, RED, 440)
    s.text(580, 540, "Scattered around the true value → random", 16, BLUE, 440)
    s.text(1070, 540, "One reading far from the cluster → gross", 16, ORANGE, 440)
    return s


def d19() -> Scene:
    s = Scene("D1.9"); s.title("Error propagation for Z = A²B/C", "Track each input's fractional uncertainty to the output; choose worst-case addition or statistical quadrature.")
    inputs=[("A", "power +2", "eA = ΔA/|A|", BLUE),
            ("B", "power +1", "eB = ΔB/|B|", TEAL),
            ("C", "power −1", "eC = ΔC/|C|", ORANGE)]
    y=[170,310,450]
    for (name,power,err,col),yy in zip(inputs,y):
        s.rect(65,yy,335,82,col,WHITE,2,True)
        s.text(85,yy+18,f"{name}    {power}",20,col,260)
        s.text(85,yy+48,err,16,INK,280)
        s.arrow(410,yy+42,650,345,col,2)
    s.ellipse(615,292,90,90,BLUE,PALE_BLUE,2)
    s.text(635,321,"Z",26,BLUE,50,"center")
    s.text(770,151,"WORST CASE",16,RED,400)
    s.rect(770,184,680,114,RED,PALE_RED,2,True)
    s.text(800,205,"ΔZ/|Z|  ≤  2eA + eB + eC",22,INK,600)
    s.text(800,252,"Add magnitudes: the sign of an input change may be unknown.",15,MUTED,610)
    s.text(770,330,"INDEPENDENT RANDOM ERRORS",16,PURPLE,460)
    s.rect(770,364,680,114,PURPLE,"#f0ecf7",2,True)
    s.text(800,385,"σZ/|Z|  =  √(4eA² + eB² + eC²)",21,INK,620)
    s.text(800,432,"Combine independent standard uncertainties in quadrature.",15,MUTED,610)
    s.text(770, 540, "A denominator contributes with a negative sign to the signed differential, but its uncertainty magnitude still adds.", 16, INK, 650)
    return s


def d110() -> Scene:
    s = Scene("D1.10"); s.title("Vernier caliper: main-scale reading plus one coincidence", "10 vernier divisions span 9 mm → least count 0.1 mm = 0.01 cm.")
    x0=160; scale=62; ymain=250; yver=415
    s.text(70,132,"MAIN SCALE · millimetres",17,BLUE,420)
    for mm in range(23,35):
        x=x0+(mm-23)*scale
        s.line(x,ymain-26,x,ymain+27,INK,2)
        s.text(x-28,ymain+36,str(mm),14,MUTED,56,"center")
    s.line(x0,ymain,x0+11*scale,ymain,INK,3)
    s.text(70,346,"VERNIER · 10 divisions span 9 mm",17,TEAL,560)
    v0=x0+0.7*scale
    for i in range(11):
        x=v0+i*0.9*scale
        length=42 if i in (0,7,10) else 28
        s.line(x,yver-length/2,x,yver+length/2,TEAL if i==7 else INK,2.5 if i==7 else 1.6)
        if i in (0,7,10): s.text(x-15,yver+31,str(i),13,TEAL if i==7 else MUTED,35,"center")
    s.line(v0,yver,v0+10*0.9*scale,yver,TEAL,2)
    # Highlight seventh vernier mark aligned with the 30 mm main tick.
    xm=x0+7*scale
    s.ellipse(xm-8,yver-8,16,16,GREEN,PALE_GREEN,2)
    s.arrow(v0,ymain-60,v0,ymain-15,BLUE,2)
    s.text(v0-65,ymain-102,"vernier zero\nfalls after 23 mm",15,BLUE,150,"center")
    s.arrow(xm,yver-70,xm,yver-31,GREEN,2)
    s.text(xm-73,yver-124,"7th line coincides\nwith 30 mm mark",15,GREEN,180,"center")
    s.rect(180,520,1110,108,GREEN,PALE_GREEN,2,True)
    s.text(214,540,"Reading = main scale + (coincidence × least count)",18,INK,900)
    s.text(214,578,"2.30 cm + 7 × 0.01 cm = 2.37 cm",22,GREEN,870)
    return s


def d111() -> Scene:
    s = Scene("D1.11"); s.title("Micrometer screw gauge: positive zero error is subtracted", "Illustration: zero error +3 circular divisions; least count 0.01 mm.")
    # Simplified side-view frame, anvil, spindle, sleeve and thimble.
    s.rect(75,160,560,310,INK,"transparent",7,True)
    s.rect(75,160,148,310,BLUE,PALE_BLUE,2,True)
    s.text(100,190,"FRAME",16,BLUE,100,"center")
    s.rect(220,275,45,52,INK,PALE_ORANGE,2)
    s.text(132,340,"anvil",15,MUTED,90,"center")
    s.rect(265,289,205,24,TEAL,PALE_TEAL,2)
    s.text(283,250,"spindle",15,TEAL,130,"center")
    s.rect(465,240,300,120,BLUE,PALE_BLUE,2,True)
    s.text(490,255,"SLEEVE · main scale",16,BLUE,245)
    # main sleeve scale marks
    for i in range(7):
        x=492+i*34
        s.line(x,314,x,338 if i%2==0 else 328,INK,1.5)
        if i%2==0: s.text(x-14,339,str(5+i//2),12,MUTED,30,"center")
    s.line(475,325,751,325,RED,2)
    s.text(472,365,"reference line",13,RED,130)
    # thimble/circular-scale cross-section and scale
    s.rect(765,224,250,152,TEAL,PALE_TEAL,2,True)
    s.text(795,239,"THIMBLE · circular scale",16,TEAL,215)
    s.line(786,320,998,320,INK,2)
    for i in range(11):
        y=275+i*9
        s.line(786,y,812 if i%2==0 else 802,y,INK,1.4)
        s.text(820,y-9,str(i*10),12,MUTED,44)
    # zero displaced +3 divisions relative to reference line
    s.line(786,293,815,293,RED,3)
    s.text(840,279,"0 on circular scale",13,RED,145)
    s.arrow(939,295,939,321,RED,2)
    s.text(880,330,"+3 divisions",14,RED,125)
    s.rect(1070,210,390,205,ORANGE,PALE_ORANGE,2,True)
    s.text(1094,232,"ZERO-ERROR CORRECTION",15,ORANGE,335)
    s.text(1094,278,"zero error = +3 × 0.01 mm",18,INK,340)
    s.text(1094,320,"= +0.03 mm",20,RED,320)
    s.text(1094,365,"correct reading = observed − 0.03 mm",16,TEAL,340)
    s.rect(250,525,1050,90,GREEN,PALE_GREEN,2,True)
    s.text(280,550,"With the jaws closed, the positive offset reads too large: subtract the zero error from every observation.",17,GREEN,990)
    return s


def d112() -> Scene:
    s = Scene("D1.12"); s.title("Linearise a pendulum model: T² versus L is a straight line", "Illustrative ideal data for g = 9.8 m s⁻²; schematic error bars (no measured uncertainties specified).")
    # Panels with axes
    panels=[(55,150,620,455,"T vs L · square-root curve"),(735,150,620,455,"T² vs L · linearised")]
    data=[(.25,1.0035,1.0071),(.50,1.4192,2.0142),(.75,1.7382,3.0213),(1.00,2.0071,4.0284)]
    for x,y,w,h,label in panels:
        s.rect(x,y,w,h,GRID,WHITE,1,True)
        s.text(x+18,y+12,label,18,BLUE,w-36)
        xa,ya,xb,yb=x+76,y+76,x+w-28,y+h-66
        s.line(xa,yb,xb,yb,INK,2); s.line(xa,yb,xa,ya,INK,2)
        for k in range(1,5):
            xx=xa+(xb-xa)*k/4
            s.line(xx,ya,xx,yb,GRID,1,"dashed")
        for k in range(1,5):
            yy=yb-(yb-ya)*k/4
            s.line(xa,yy,xb,yy,GRID,1,"dashed")
        s.text(xa+(xb-xa)/2,yb+32,"L (m)",14,INK,100,"center")
        s.text(x+10,ya+8,"T (s)" if x<700 else "T² (s²)",13,INK,65)
    # left map L 0..1, T 0..2.2
    x,y,w,h,_=panels[0]
    xa,ya,xb,yb=x+76,y+76,x+w-28,y+h-66
    left=[]
    for L,T,_ in data:
        px=xa+L*(xb-xa); py=yb-(T/2.2)*(yb-ya); left.append((px,py))
    # smooth-looking polyline from calculated samples
    for a,b in zip(left,left[1:]): s.line(*a,*b,BLUE,2.8)
    for px,py in left:
        s.line(px-7,py,px+7,py,TEAL,1.3); s.line(px,py-6,px,py+6,TEAL,1.3); s.dot(px,py,5,TEAL)
    s.text(125,523,"T = 2π√(L/g)",15,BLUE,260)
    # right map L 0..1, T^2 0..4.5
    x,y,w,h,_=panels[1]
    xa,ya,xb,yb=x+76,y+76,x+w-28,y+h-66
    right=[]
    for L,T,T2 in data:
        px=xa+L*(xb-xa); py=yb-(T2/4.5)*(yb-ya); right.append((px,py))
    s.line(xa,yb,xb,yb-(4.0284/4.5)*(yb-ya),GREEN,2.8)
    for px,py in right:
        s.line(px-7,py,px+7,py,TEAL,1.3); s.line(px,py-6,px,py+6,TEAL,1.3); s.dot(px,py,5,TEAL)
    s.text(815,523,"T² = (4π²/g)L",15,GREEN,260)
    s.text(810,552,"slope = 4π²/g ≈ 4.03 s² m⁻¹; intercept = 0",14,INK,490)
    return s


def panel(s: Scene, x: float, y: float, w: float, h: float, heading: str) -> None:
    s.rect(x, y, w, h, GRID, WHITE, 1, True)
    s.text(x + 18, y + 12, heading, 18, BLUE, w - 36)


def polyline(s: Scene, pts: list[tuple[float,float]], color: str, sw: float = 2.5, dash: str = "solid") -> None:
    for p,q in zip(pts,pts[1:]): s.line(*p,*q,color,sw,dash)


def hatch_polygon(s: Scene, pts: list[tuple[float,float]], color: str, step: int = 13) -> None:
    """Horizontal scan-line hatch for a simple polygon, useful for signed graph areas."""
    ymin=int(min(y for _,y in pts)); ymax=int(max(y for _,y in pts))
    for y in range(ymin+step,ymax,step):
        xs=[]
        for p,q in zip(pts,pts[1:]+pts[:1]):
            x1,y1=p; x2,y2=q
            if y1==y2: continue
            if min(y1,y2)<y<max(y1,y2): xs.append(x1+(y-y1)*(x2-x1)/(y2-y1))
        xs.sort()
        for i in range(0,len(xs)-1,2): s.line(xs[i],y,xs[i+1],y,color,2)


def d21() -> Scene:
    s = Scene("D2.1")
    s.title("A scalar has magnitude; a vector has magnitude and direction", "A scalar is not an arrow; vector addition is geometrical.")
    panel(s, 60, 135, 390, 195, "SCALAR")
    s.text(100, 190, "Temperature", 23, INK, 300)
    s.text(100, 225, "37 °C", 36, BLUE, 270)
    s.text(100, 278, "Magnitude + unit; no direction.", 16, MUTED, 320)
    panel(s, 490, 135, 840, 195, "VECTOR")
    s.dot(690, 260, 5, INK)
    s.arrow(690, 260, 1060, 260, BLUE, 4)
    s.text(710, 205, "3 m east", 23, BLUE, 300)
    s.text(1090, 240, "direction", 16, MUTED, 180)
    s.text(510, 294, "Displacement: magnitude 3 m, directed east.", 16, MUTED, 750)
    s.text(65, 370, "Two vectors from a common tail: the parallelogram diagonal is their sum.", 18, INK, 1200)
    o = (455, 720); ah = (775, 565); bh = (320, 500); ch = (640, 345)
    s.arrow(*o, *ah, BLUE, 3.2); s.arrow(*o, *bh, TEAL, 3.2)
    s.arrow(*ah, *ch, TEAL, 2.2); s.arrow(*bh, *ch, BLUE, 2.2)
    s.arrow(*o, *ch, GREEN, 4)
    s.dot(*o, 5, INK)
    s.text(600, 630, "a", 22, BLUE, 40); s.text(350, 585, "b", 22, TEAL, 40)
    s.text(545, 510, "a + b", 24, GREEN, 100)
    return s


def d22() -> Scene:
    s = Scene("D2.2")
    s.title("Triangle and parallelogram laws give the same vector sum", "Vector subtraction is addition of the reversed vector.")
    panel(s, 55, 135, 1290, 300, "TRIANGLE LAW · place the tail of b at the head of a")
    o = (300, 370); ah = (600, 240); ch = (930, 370)
    s.arrow(*o, *ah, BLUE, 3.5); s.arrow(*ah, *ch, TEAL, 3.5); s.arrow(*o, *ch, GREEN, 3.5)
    s.dot(*o, 5, INK); s.text(420, 280, "a", 22, BLUE, 45)
    s.text(730, 280, "b", 22, TEAL, 45); s.text(560, 380, "c = a + b", 19, GREEN, 170)
    panel(s, 55, 460, 1290, 345, "PARALLELOGRAM LAW · same-tail vectors a and b")
    o = (430, 730); ah = (625, 545); bh = (850, 730); ch = (1045, 545)
    s.arrow(*o, *ah, BLUE, 3.2); s.arrow(*o, *bh, TEAL, 3.2)
    s.arrow(*ah, *ch, TEAL, 2.4); s.arrow(*bh, *ch, BLUE, 2.4)
    s.arrow(*o, *ch, GREEN, 3.5)
    s.arrow(*bh, *ah, ORANGE, 3)
    s.dot(*o, 5, INK)
    s.text(505, 620, "a", 21, BLUE, 45); s.text(720, 740, "b", 21, TEAL, 45)
    s.text(780, 600, "a + b", 19, GREEN, 90)
    s.text(700, 655, "a − b  (from tip of b to tip of a)", 16, ORANGE, 330)
    return s


def d23() -> Scene:
    s = Scene("D2.3")
    s.title("Resolve a vector into perpendicular components", "For a vector in the first quadrant, θ is measured from +x.")
    ox, oy = 330, 680
    s.arrow(ox, oy, 1110, oy, INK, 2.2); s.arrow(ox, oy, ox, 170, INK, 2.2)
    s.text(1115, 665, "x", 19, INK, 35); s.text(300, 145, "y", 19, INK, 35)
    tip = (900, 330); foot = (900, oy)
    s.arrow(ox, oy, *tip, BLUE, 4)
    s.line(tip[0], tip[1], foot[0], foot[1], MUTED, 2, "dashed")
    s.line(ox, oy, foot[0], foot[1], TEAL, 3)
    s.line(foot[0]-18, foot[1], foot[0]-18, foot[1]-18, MUTED, 1.5)
    s.line(foot[0]-18, foot[1]-18, foot[0], foot[1]-18, MUTED, 1.5)
    s.dot(ox, oy, 5, INK); s.dot(*tip, 5, BLUE)
    s.text(590, 465, "a", 25, BLUE, 45)
    s.text(565, 695, "aₓ = a cos θ", 19, TEAL, 180)
    s.text(915, 470, "aᵧ = a sin θ", 19, TEAL, 200)
    s.text(400, 640, "θ", 22, ORANGE, 40)
    s.text(1115, 285, "a = aₓ î + aᵧ ĵ", 21, GREEN, 235)
    s.text(1115, 330, "aₓ² + aᵧ² = a²", 18, INK, 225)
    return s


def d24() -> Scene:
    s = Scene("D2.4")
    s.title("The dot product measures alignment", "The scalar projection of a onto b is a cos θ; the product is ab cos θ.")
    o = (300, 650); ah = (710, 300); bh = (1010, 650); foot = (710, 650)
    s.arrow(*o, *bh, TEAL, 3.5); s.arrow(*o, *ah, BLUE, 3.5)
    s.line(*ah, *foot, MUTED, 2, "dashed")
    s.arrow(*o, *foot, ORANGE, 3)
    s.line(foot[0]-18, foot[1], foot[0]-18, foot[1]-18, MUTED, 1.5)
    s.line(foot[0]-18, foot[1]-18, foot[0], foot[1]-18, MUTED, 1.5)
    s.dot(*o, 5, INK); s.dot(*ah, 5, BLUE)
    s.text(475, 425, "a", 24, BLUE, 40); s.text(850, 665, "b", 24, TEAL, 40)
    s.text(505, 675, "a cos θ", 19, ORANGE, 135); s.text(370, 600, "θ", 20, PURPLE, 40)
    panel(s, 1035, 205, 300, 320, "DOT PRODUCT")
    s.text(1065, 285, "a · b = ab cos θ", 22, GREEN, 250)
    s.text(1065, 340, "scalar projection of a", 16, INK, 230)
    s.text(1065, 372, "along b = a cos θ", 16, INK, 230)
    s.text(1065, 438, "If θ is acute: positive.\nIf θ = 90°: zero.\nIf θ is obtuse: negative.", 15, MUTED, 245)
    return s


def d25() -> Scene:
    s = Scene("D2.5")
    s.title("Cross product: oriented area and the right-hand rule", "a and b lie in the xy-plane; the order a × b sets the normal direction.")
    o = (190, 690); ah = (790, 690); bh = (410, 390); ch = (1010, 390)
    # Light hatching stays inside the skew parallelogram and makes its area explicit.
    for y in range(410, 681, 22):
        left = o[0] + round((o[1]-y) * (bh[0]-o[0]) / (o[1]-bh[1]))
        s.line(left, y, left + (ah[0]-o[0]), y, "#dcecf7", 2)
    s.line(*o, *ah, INK, 2); s.line(*o, *bh, INK, 2)
    s.line(*ah, *ch, INK, 2); s.line(*bh, *ch, INK, 2)
    s.arrow(*o, *ah, BLUE, 3.5); s.arrow(*o, *bh, TEAL, 3.5)
    s.dot(*o, 5, INK); s.text(470, 710, "a", 23, BLUE, 35); s.text(290, 505, "b", 23, TEAL, 35)
    # Out-of-page normal is a circled dot.
    s.ellipse(1080, 285, 62, 62, PURPLE, "transparent", 3); s.dot(1111, 316, 5, PURPLE)
    s.text(1160, 294, "+z", 21, PURPLE, 90)
    s.text(1060, 380, "a × b", 24, PURPLE, 125)
    s.text(1060, 430, "|a × b| = ab sin θ", 19, INK, 275)
    s.text(1060, 470, "= area of the\nparallelogram", 17, INK, 230)
    s.text(1060, 555, "Right hand: curl from a\ntoward b; thumb points +z.", 16, MUTED, 260)
    return s


def d26() -> Scene:
    s = Scene("D2.6")
    s.title("The scalar triple product is a signed volume", "Schematic projection: b and c span the base; a⊥ is the height.")
    o=(220,690); b=(700,690); c=(420,510); bc=(900,510)
    av=(220,340); ab=(700,340); ac=(420,160); abc=(900,160)
    # The base is lightly hatched; its boundary remains a true parallelogram.
    for y in range(530, 681, 24):
        left=o[0] + round((o[1]-y)*(c[0]-o[0])/(o[1]-c[1]))
        s.line(left,y,left+(b[0]-o[0]),y,"#e7f1fa",2)
    # Wireframe parallelepiped edges.
    for p,q in [(o,b),(o,c),(b,bc),(c,bc),(av,ab),(av,ac),(ab,abc),(ac,abc),(o,av),(b,ab),(c,ac),(bc,abc)]:
        s.line(*p,*q,GRID,2)
    s.arrow(*o,*b,BLUE,3.4); s.arrow(*o,*c,TEAL,3.4); s.arrow(*o,*av,PURPLE,3.4)
    s.dot(*o,5,INK)
    s.text(440,705,"b",21,BLUE,35); s.text(300,580,"c",21,TEAL,35); s.text(230,475,"a",21,PURPLE,35)
    # Perpendicular height is shown dashed from the lifted vertex to the base plane.
    s.line(250,340,250,690,ORANGE,2,"dashed")
    s.text(265,485,"|a⊥|",18,ORANGE,80)
    s.text(965,245,"V = a · (b × c)",23,GREEN,300)
    s.text(965,300,"|V| = |b × c| |a⊥|",20,INK,340)
    s.text(965,365,"Base area = |b × c|",17,TEAL,280)
    s.text(965,415,"Sign records orientation:\n[a,b,c] > 0 for a right-handed\nordered triad.",16,MUTED,350)
    return s


def d27() -> Scene:
    s = Scene("D2.7")
    s.title("Solve a × x = b: one perpendicular component plus a free parallel part", "A solution requires a · b = 0; adding any multiple of a leaves the cross product unchanged.")
    panel(s, 55, 145, 590, 600, "RIGHT-HAND-RULE CHECK · a = +ŷ, x₀ = +ẑ")
    o=(245,600)
    s.arrow(*o,245,340,BLUE,3.5); s.arrow(*o,515,600,TEAL,3.5)
    s.text(260,340,"a = +ŷ",19,BLUE,115); s.text(520,605,"b = +x̂",19,TEAL,115)
    s.ellipse(350,440,58,58,PURPLE,"transparent",3); s.dot(379,469,5,PURPLE)
    s.text(420,448,"x₀ = +ẑ (out of page)",17,PURPLE,200)
    s.text(125,670,"ŷ × ẑ = x̂, so a × x₀ = b",18,GREEN,430)
    panel(s, 680, 145, 665, 600, "SOLUTION FAMILY · locus is parallel to a")
    q=(815,650); x0=(1030,650); xm=(1030,445); xp=(1030,340)
    s.arrow(*q,*x0,ORANGE,3.2); s.text(875,665,"x₀ ⟂ a",17,ORANGE,105)
    s.line(1030,310,1030,705,MUTED,2,"dashed")
    s.arrow(*q,*xm,GREEN,3.5); s.arrow(1120,630,1120,475,BLUE,3)
    s.text(1140,515,"a",20,BLUE,40); s.text(1050,405,"x = x₀ + λa",19,GREEN,180)
    s.text(730,260,"x₀ = (b × a)/|a|²",20,INK,260)
    s.text(730,310,"Necessary: a · b = 0",18,INK,260)
    s.text(730,715,"a × (λa) = 0  ⇒  every λ gives another solution",16,MUTED,510)
    return s


def d28() -> Scene:
    s = Scene("D2.8")
    s.title("Polar unit vectors rotate with the position angle", "At a point on a circle, r̂ is radial and θ̂ is tangent in the direction of increasing θ.")
    cx,cy,r=430,555,220
    s.ellipse(cx-r,cy-r,2*r,2*r,GRID,"transparent",2)
    s.arrow(cx,cy,790,cy,INK,1.8); s.arrow(cx,cy,cx,220,INK,1.8)
    s.text(795,cy-15,"x",17,INK,25); s.text(cx-20,195,"y",17,INK,25)
    theta=math.radians(35); px=cx+r*math.cos(theta); py=cy-r*math.sin(theta)
    tx,ty=-math.sin(theta),-math.cos(theta)
    s.arrow(cx,cy,px,py,BLUE,3.5)
    s.arrow(px,py,px+115*tx,py+115*ty,TEAL,3.5)
    s.dot(px,py,6,INK)
    s.text(535,420,"r̂",22,BLUE,50); s.text(580,280,"θ̂",22,TEAL,60)
    s.text(500,535,"θ",20,ORANGE,35); s.text(268,588,"O",16,INK,30)
    panel(s, 850, 190, 475, 390, "A SMALL INCREASE dθ ROTATES r̂")
    s.text(885,270,"d r̂ = θ̂ dθ",24,BLUE,340)
    s.text(885,335,"Differentiate with respect to time:",17,INK,390)
    s.text(885,385,"d r̂/dt = θ̇ θ̂ = ω θ̂",22,GREEN,390)
    s.text(885,455,"θ̂ is the tangent unit vector\nin the counterclockwise direction.",16,MUTED,390)
    s.text(865,635,"In 3D:  d r̂/dt = ω⃗ × r̂",19,PURPLE,390)
    return s


def d29() -> Scene:
    s = Scene("D2.9")
    s.title("The scalar triple product is a signed volume", "Swapping the orientation of the ordered triad reverses the sign, not the volume magnitude.")
    panel(s, 55, 155, 610, 540, "RIGHT-HANDED ORDERED TRIAD · positive")
    panel(s, 735, 155, 610, 540, "LEFT-HANDED ORDERED TRIAD · negative")
    for ox, sign, color in [(115,1,GREEN),(925,-1,RED)]:
        oy=500; av=(220,0); bv=(0,-165)
        cv=(85,-65) if sign>0 else (-85,65)
        o=(ox+45,oy+35); a=(o[0]+av[0],o[1]+av[1]); b=(o[0]+bv[0],o[1]+bv[1])
        ab=(a[0]+bv[0],a[1]+bv[1]); c=(o[0]+cv[0],o[1]+cv[1])
        ac=(a[0]+cv[0],a[1]+cv[1]); bc=(b[0]+cv[0],b[1]+cv[1]); abc=(ab[0]+cv[0],ab[1]+cv[1])
        # Projected wireframe parallelepiped: a and b span the face; c is the depth edge.
        edges=[(o,a),(o,b),(a,ab),(b,ab),(c,ac),(c,bc),(ac,abc),(bc,abc),(o,c),(a,ac),(b,bc),(ab,abc)]
        for p,q in edges: s.line(*p,*q,GRID,1.8)
        s.arrow(*o,*a,BLUE,3.2); s.arrow(*o,*b,TEAL,3.2); s.arrow(*o,*c,PURPLE,3.2)
        s.text(a[0]+8,a[1]-10,"a",18,BLUE,35); s.text(b[0]-5,b[1]-28,"b",18,TEAL,35)
        s.text(c[0]+5,c[1]-28,"c",18,PURPLE,35)
        # Normal marker fixes which side of the xy-plane c points to.
        cx=ox+330; cy=oy-115
        s.ellipse(cx-25,cy-25,50,50,color,"transparent",3)
        if sign>0:
            s.dot(cx,cy,5,color); ctext="c = +ẑ · out of page"
        else:
            s.line(cx-10,cy-10,cx+10,cy+10,color,3); s.line(cx-10,cy+10,cx+10,cy-10,color,3); ctext="c = −ẑ · into page"
        s.text(ox+105,cy+34,ctext,14,color,230)
        s.text(ox+40,615,"[a,b,c] = a · (b × c)",17,INK,355)
        s.text(ox+145,653,"[a,b,c] > 0" if sign>0 else "[a,b,c] < 0",19,color,190)
    s.text(310,735,"|[a,b,c]| is the parallelepiped volume in either case.",18,INK,770)
    return s


def d210() -> Scene:
    s = Scene("D2.10")
    s.title("Add vectors component by component", "The parallelogram diagonal gives the same result as adding x- and y-components.")
    ox,oy,scale=285,685,82
    xmax=6; ymax=7
    s.arrow(ox,oy,ox+scale*xmax,oy,INK,2); s.arrow(ox,oy,ox,oy-scale*ymax,INK,2)
    for i in range(1,xmax+1):
        x=ox+i*scale; s.line(x,oy-5,x,oy+5,GRID,1); s.text(x-8,oy+12,str(i),12,MUTED,20)
    for j in range(1,ymax+1):
        y=oy-j*scale; s.line(ox-5,y,ox+5,y,GRID,1); s.text(ox-28,y-8,str(j),12,MUTED,20)
    s.text(ox+scale*xmax+10,oy-15,"x",17,INK,25); s.text(ox-15,oy-scale*ymax-30,"y",17,INK,25)
    a=(ox+3*scale,oy-2*scale); b=(ox+1*scale,oy-4*scale); c=(ox+4*scale,oy-6*scale)
    # Dashed component projections land on both axes; the other two sides complete the parallelogram.
    for point in (a,b,c):
        s.line(point[0],point[1],point[0],oy,MUTED,1.2,"dashed")
        s.line(ox,point[1],point[0],point[1],MUTED,1.2,"dashed")
    s.line(a[0],a[1],c[0],c[1],TEAL,2,"dashed")
    s.line(b[0],b[1],c[0],c[1],BLUE,2,"dashed")
    s.arrow(ox,oy,*a,BLUE,3.4); s.arrow(ox,oy,*b,TEAL,3.4); s.arrow(ox,oy,*c,GREEN,4)
    s.text(400,475,"a = (3, 2)",18,BLUE,130); s.text(345,330,"b = (1, 4)",18,TEAL,130)
    s.text(530,225,"c = a + b = (4, 6)",20,GREEN,270)
    panel(s, 885, 245, 420, 330, "COMPONENT SUM")
    s.text(920,325,"cₓ = aₓ + bₓ = 3 + 1 = 4",18,BLUE,350)
    s.text(920,380,"cᵧ = aᵧ + bᵧ = 2 + 4 = 6",18,TEAL,350)
    s.text(920,465,"c = 4 î + 6 ĵ",22,GREEN,300)
    return s


def d211() -> Scene:
    s = Scene("D2.11")
    s.title("Project a onto b: drop a perpendicular from the head of a", "The scalar component is a cos θ; the vector projection points along b.")
    o=(270,655); ah=(700,300); bh=(1040,655); foot=(700,655)
    s.arrow(*o,*bh,TEAL,3.4); s.arrow(*o,*ah,BLUE,3.4)
    s.line(*ah,*foot,MUTED,2,"dashed")
    s.arrow(*o,*foot,ORANGE,3.5)
    s.line(foot[0]-18,foot[1],foot[0]-18,foot[1]-18,MUTED,1.5)
    s.line(foot[0]-18,foot[1]-18,foot[0],foot[1]-18,MUTED,1.5)
    s.dot(*o,5,INK); s.dot(*ah,5,BLUE)
    s.text(465,425,"a",24,BLUE,35); s.text(850,672,"b",23,TEAL,35); s.text(430,682,"θ",20,PURPLE,35)
    s.text(490,690,"a cos θ",18,ORANGE,110)
    panel(s, 1055, 195, 285, 425, "PROJECTION")
    s.text(1078,275,"scalar:",16,MUTED,180)
    s.text(1078,305,"a · b̂ = a cos θ",19,INK,245)
    s.text(1078,385,"vector:",16,MUTED,180)
    s.text(1078,415,"proj_b a = (a · b̂)b̂",18,GREEN,245)
    s.text(1078,470,"= [(a · b)/|b|²] b",17,GREEN,245)
    return s


def d212() -> Scene:
    s = Scene("D2.12")
    s.title("Reversing cross-product order reverses the normal", "The right-hand rule gives equal magnitudes and opposite directions.")
    panel(s, 65, 150, 610, 585, "a × b · OUT OF THE PAGE")
    panel(s, 725, 150, 610, 585, "b × a · INTO THE PAGE")
    for ox, swapped, color in [(180,False,GREEN),(840,True,RED)]:
        oy=560
        s.arrow(ox,oy,ox+290,oy,BLUE,3.5)
        s.arrow(ox,oy,ox,oy-250,TEAL,3.5)
        s.text(ox+300,oy-15,"a",20,BLUE,35)
        s.text(ox-10,oy-280,"b",20,TEAL,35)
        cx=ox+110; cy=oy+45
        s.ellipse(cx-30,cy-30,60,60,color,"transparent",3)
        if not swapped: s.dot(cx,cy,5,color); label="⊙ +z"
        else:
            s.line(cx-11,cy-11,cx+11,cy+11,color,3); s.line(cx-11,cy+11,cx+11,cy-11,color,3); label="⊗ −z"
        s.text(ox+200,oy+40,label,18,color,115)
        s.text(ox+100,645,"|a × b| = |b × a|",18,INK,260)
        s.text(ox+112,685,"b × a = −(a × b)",20,color,250)
    s.text(305,770,"⊙ out of page     ⊗ into page",16,MUTED,420)
    return s


def d31() -> Scene:
    s = Scene("D3.1")
    s.title("Distance is path length; displacement is final minus initial position", "One-dimensional example: start at 2 m, turn at 5 m, finish at 3 m.")
    x0=180; scale=165; y=420
    s.arrow(x0-45,y,x0+6*scale+60,y,INK,2.2)
    s.text(x0+6*scale+66,y-15,"x (m)",18,INK,80)
    for n in range(0,7):
        x=x0+n*scale; s.line(x,y-10,x,y+10,INK,1.5); s.text(x-10,y+18,str(n),15,MUTED,25)
    p2=x0+2*scale; p3=x0+3*scale; p5=x0+5*scale
    s.dot(p2,y,7,BLUE); s.dot(p5,y,7,ORANGE); s.dot(p3,y,7,GREEN)
    s.text(p2-45,y-60,"start x=2",17,BLUE,105)
    s.text(p5-35,y-60,"turn x=5",17,ORANGE,105)
    s.text(p3-45,y+45,"finish x=3",17,GREEN,115)
    s.arrow(p2,350,p5,350,BLUE,3.5); s.arrow(p5,390,p3,390,ORANGE,3.5)
    s.text(495,315,"3 m",17,BLUE,60); s.text(735,395,"2 m back",17,ORANGE,120)
    panel(s, 125, 555, 530, 180, "TOTAL DISTANCE")
    s.text(160,625,"3 m + 2 m = 5 m",23,BLUE,350)
    panel(s, 715, 555, 530, 180, "SIGNED DISPLACEMENT")
    s.text(750,625,"x_f − x_i = 3 − 2 = +1 m",22,GREEN,430)
    return s


def d32() -> Scene:
    s = Scene("D3.2")
    s.title("Instantaneous velocity is the tangent slope of x(t)", "Illustration: x = t². Compare the tangent at t₀=1 with a finite-time secant to t₀+Δt=1.5.")
    xL,yB=170,675; sx,sy=330,105
    s.arrow(xL,yB,xL+2.25*sx,yB,INK,2); s.arrow(xL,yB,xL,yB-4.2*sy,INK,2)
    s.text(xL+2.25*sx+8,yB-14,"t",17,INK,25); s.text(xL-26,yB-4.2*sy-25,"x",17,INK,25)
    for t in [0.5,1,1.5,2]:
        x=xL+t*sx; s.line(x,yB-5,x,yB+5,GRID,1); s.text(x-12,yB+12,str(t),13,MUTED,30)
    curve=[]
    for i in range(17):
        t=2*i/16; curve.append((xL+t*sx,yB-(t*t)*sy))
    for p,q in zip(curve,curve[1:]): s.line(*p,*q,BLUE,3)
    p=(xL+sx,yB-sy); q=(xL+1.5*sx,yB-2.25*sy)
    # Tangent x=2t-1 at t0=1; secant joins t0 and t0+0.5.
    t1,t2=.62,1.38
    s.line(xL+t1*sx,yB-(2*t1-1)*sy,xL+t2*sx,yB-(2*t2-1)*sy,GREEN,2.5)
    s.line(*p,*q,ORANGE,2.5,"dashed")
    s.dot(*p,6,BLUE); s.dot(*q,6,ORANGE)
    s.text(p[0]-52,p[1]+18,"(1, 1)",15,BLUE,75); s.text(q[0]+8,q[1]-18,"(1.5, 2.25)",15,ORANGE,115)
    panel(s, 900, 210, 400, 330, "SLOPES AT t₀ = 1")
    s.text(930,295,"Tangent: v(t₀) = dx/dt = 2",18,GREEN,340)
    s.text(930,350,"Secant: v̄ = Δx/Δt",18,ORANGE,320)
    s.text(930,393,"= (2.25 − 1)/(1.5 − 1) = 2.5",16,ORANGE,345)
    s.text(930,465,"As Δt → 0, the secant slope\napproaches the tangent slope.",16,MUTED,340)
    s.text(315,715,"t (s)",14,INK,80); s.text(195,245,"x(t)=t²",17,BLUE,115)
    return s


def d33() -> Scene:
    s = Scene("D3.3")
    s.title("For constant positive acceleration: x curves, v rises linearly, a is constant", "Illustrative model x=t+t², so v=1+2t and a=2 for t≥0.")
    xL,xR=225,1190; scaleT=(xR-xL)/4
    rows=[(145,315,"x (m)",0,20,"x=t+t²",BLUE),(350,520,"v (m/s)",0,10,"v=1+2t",TEAL),(555,710,"a (m/s²)",0,3,"a=2",PURPLE)]
    for top,bottom,ylab,ymin,ymax,eq,col in rows:
        yAxis=bottom-25; yTop=top+18
        s.arrow(xL,yAxis,xR,yAxis,INK,1.7); s.arrow(xL,yAxis,xL,yTop,INK,1.7)
        s.text(xL-50,yTop-8,ylab,14,INK,80); s.text(xL+12,top+8,eq,16,col,160)
        s.line(xL,yAxis-(yAxis-yTop)*.5,xR,yAxis-(yAxis-yTop)*.5,GRID,1,"dashed")
    # x=t+t^2, t=0..4
    top,bottom=145,315; yAxis=bottom-25; yTop=top+18; h=yAxis-yTop
    pts=[]
    for i in range(17):
        t=4*i/16; val=t+t*t; pts.append((xL+t*scaleT,yAxis-val/20*h))
    for p,q in zip(pts,pts[1:]): s.line(*p,*q,BLUE,2.8)
    # v=1+2t, range 0..10
    top,bottom=350,520; yAxis=bottom-25; yTop=top+18; h=yAxis-yTop
    p=(xL,yAxis-(1/10)*h); q=(xR,yAxis-(9/10)*h); s.line(*p,*q,TEAL,2.8)
    # a=2, range 0..3
    top,bottom=555,710; yAxis=bottom-25; yTop=top+18; h=yAxis-yTop
    yy=yAxis-(2/3)*h; s.line(xL,yy,xR,yy,PURPLE,2.8)
    for t in [0,1,2,3,4]:
        x=xL+t*scaleT; s.line(x,685,x,697,INK,1); s.text(x-8,700,str(t),13,MUTED,20)
    s.text(680,738,"shared time axis t (s)",15,INK,180)
    s.text(1205,230,"slope = v",14,BLUE,160)
    s.text(1205,420,"slope = a",14,TEAL,160)
    s.text(1205,458,"area under v–t = Δx",14,GREEN,185)
    return s


def d35() -> Scene:
    s = Scene("D3.5")
    s.title("The v–t graph derives the constant-acceleration equations", "Straight line from (0,u) to (t,v), with positive constant slope a.")
    o=(250,665); start=(250,505); end=(970,325); foot=(970,665)
    # Hatch the trapezoidal area beneath the velocity graph.
    for y in range(525,660,18):
        frac=(y-505)/(665-505); xright=250+frac*(970-250)
        s.line(255,y,xright,y,"#e5f2eb",2)
    s.arrow(200,665,1110,665,INK,2); s.arrow(250,665,250,230,INK,2)
    s.line(*start,*end,BLUE,3.5); s.line(*start,*o,MUTED,1.5,"dashed"); s.line(*end,*foot,MUTED,1.5,"dashed")
    s.dot(*start,5,BLUE); s.dot(*end,5,BLUE)
    s.text(215,480,"u",20,BLUE,35); s.text(985,305,"v=u+at",19,BLUE,130)
    s.text(970,678,"t",18,INK,25); s.text(225,230,"v",18,INK,25)
    s.text(585,690,"Δt = t",17,INK,90); s.text(215,568,"u",17,MUTED,35)
    s.text(515,570,"rectangle: ut",17,GREEN,150)
    s.text(700,435,"triangle: ½at²",17,ORANGE,190)
    s.text(410,375,"slope = a",18,PURPLE,120)
    panel(s, 1040, 220, 300, 395, "AREA = DISPLACEMENT")
    s.text(1065,300,"s = ½(u+v)t",22,GREEN,250)
    s.text(1065,365,"= ut + ½at²",20,INK,235)
    s.text(1065,440,"Height at time t:",16,MUTED,220)
    s.text(1065,470,"v = u + at",20,BLUE,200)
    s.text(1065,530,"Valid only when a is constant.",15,RED,240)
    return s


def d37() -> Scene:
    s = Scene("D3.7")
    s.title("Variable-acceleration shortcut: change the derivative from t to x", "Use the chain rule when acceleration is given as a function of position.")
    panel(s, 70, 160, 1240, 220, "CHAIN RULE · velocity is a function of position along the trajectory")
    s.text(120,245,"a = dv/dt",27,BLUE,205)
    s.arrow(330,275,420,275,MUTED,2)
    s.text(450,245,"= (dv/dx)(dx/dt)",25,INK,330)
    s.arrow(800,275,880,275,MUTED,2)
    s.text(905,245,"= v dv/dx",27,GREEN,245)
    panel(s, 70, 420, 1240, 300, "INTEGRATE BETWEEN TWO POSITIONS / VELOCITIES")
    s.text(125,500,"v dv = a(x) dx",24,BLUE,280)
    s.text(125,555,"∫ᵤᵛ v dv = ∫ₓ₀ˣ a(ξ) dξ",22,INK,470)
    s.rect(730,505,520,125,GREEN,PALE_GREEN,2,True)
    s.text(765,535,"v²/2 = ∫ a(x) dx + C",23,GREEN,430)
    s.text(765,585,"(equivalently, use definite limits)",15,MUTED,420)
    s.text(125,655,"For constant a: v² = u² + 2a(x−x₀).",18,PURPLE,510)
    return s


def d38() -> Scene:
    s = Scene("D3.8")
    s.title("Relative velocity is the difference of signed velocities", "A is ahead of B and both move right; A pulls away because v_A > v_B.")
    x0=170; scale=175; y=435
    s.arrow(x0-40,y,x0+6*scale,y,INK,2)
    for n in range(0,7):
        x=x0+n*scale; s.line(x,y-9,x,y+9,GRID,1.2); s.text(x-10,y+17,str(n),14,MUTED,25)
    xb=x0+2*scale; xa=x0+5*scale
    s.dot(xb,y,7,TEAL); s.dot(xa,y,7,BLUE)
    s.text(xb-40,y-68,"B at x_B",17,TEAL,115); s.text(xa-55,y-68,"A at x_A",17,BLUE,125)
    s.arrow(xb,y-55,xb+230,y-55,TEAL,3.4); s.text(xb+55,y-93,"v_B = 3 m/s",16,TEAL,145)
    s.arrow(xa,y+58,xa+345,y+58,BLUE,3.4); s.text(xa+75,y+68,"v_A = 5 m/s",16,BLUE,150)
    panel(s, 185, 595, 1040, 155, "SEPARATION AND RELATIVE VELOCITY")
    s.text(225,650,"x_A − x_B is increasing",20,INK,360)
    s.text(670,650,"v_AB = v_A − v_B = 5 − 3 = +2 m/s",20,GREEN,500)
    return s


def d39() -> Scene:
    s = Scene("D3.9")
    s.title("Piecewise motion: slope gives acceleration; area gives displacement", "Illustrative data: +2 m/s² for 2 s, then 0 for 3 s, then −2 m/s² for 2 s.")
    ox,oy=190,660; sx=135; sy=65
    s.arrow(ox,oy,ox+7.5*sx,oy,INK,2); s.arrow(ox,oy,ox,oy-5*sy,INK,2)
    s.text(ox+7.5*sx+5,oy-15,"t (s)",16,INK,65); s.text(ox-45,oy-5*sy-20,"v (m/s)",16,INK,85)
    for t in range(0,8):
        x=ox+t*sx; s.line(x,oy-5,x,oy+5,GRID,1); s.text(x-8,oy+10,str(t),13,MUTED,20)
    pts=[(ox,oy),(ox+2*sx,oy-4*sy),(ox+5*sx,oy-4*sy),(ox+7*sx,oy)]
    colors=[BLUE,TEAL,ORANGE]
    for p,q,col in zip(pts,pts[1:],colors): s.line(*p,*q,col,3.6)
    for p in pts: s.dot(*p,5,INK)
    s.text(250,500,"a₁=+2",16,BLUE,85); s.text(565,360,"a₂=0",16,TEAL,80); s.text(900,500,"a₃=−2",16,ORANGE,90)
    s.text(300,690,"Δt₁=2 s",14,BLUE,90); s.text(615,390,"Δt₂=3 s",14,TEAL,90); s.text(900,690,"Δt₃=2 s",14,ORANGE,90)
    panel(s, 975, 190, 340, 275, "TOTAL DISPLACEMENT")
    s.text(1000,270,"Area = ½(2)(4)\n      + (3)(4)\n      + ½(2)(4)",18,INK,270)
    s.text(1000,395,"= 4 + 12 + 4 = 20 m",19,GREEN,285)
    s.text(1010,500,"Velocity stays non-negative,\nso signed area is displacement.",15,MUTED,285)
    return s


def d310() -> Scene:
    s = Scene("D3.10")
    s.title("The nth-second displacement is the area in a one-second time strip", "Example: u=2 m/s, a=1 m/s²; during the 3rd second, v rises from 4 to 5 m/s.")
    ox,oy=220,665; sx=175; sy=58
    s.arrow(ox,oy,ox+4.2*sx,oy,INK,2); s.arrow(ox,oy,ox,oy-6.5*sy,INK,2)
    s.text(ox+4.2*sx+5,oy-14,"t (s)",16,INK,60); s.text(ox-45,oy-6.5*sy-20,"v (m/s)",16,INK,80)
    for t in range(0,5):
        x=ox+t*sx; s.line(x,oy-5,x,oy+5,GRID,1); s.text(x-8,oy+10,str(t),13,MUTED,20)
    pts=[]
    for t in [0,1,2,3,4]: pts.append((ox+t*sx,oy-(2+t)*sy))
    # Shade the exact trapezoid for the interval 2≤t≤3 with light horizontal hatching.
    x2=ox+2*sx; x3=ox+3*sx; y2=oy-4*sy; y3=oy-5*sy
    for yy in range(y3+8,oy,13):
        if yy<y2:
            xr=x2+(y2-yy)/(y2-y3)*(x3-x2)
        else: xr=x3
        s.line(x2,yy,xr,yy,"#f5e8cd",2)
    for p,q in zip(pts,pts[1:]): s.line(*p,*q,BLUE,3)
    s.line(x2,y2,x2,oy,ORANGE,2,"dashed"); s.line(x3,y3,x3,oy,ORANGE,2,"dashed")
    for p in pts: s.dot(*p,4,BLUE)
    s.text(x2-25,y2-32,"4 m/s",15,BLUE,75); s.text(x3+8,y3-20,"5 m/s",15,BLUE,75)
    s.text(x2+48,oy-95,"3rd-second area",15,ORANGE,170)
    panel(s, 1035, 205, 310, 390, "AREA FROM t=2 TO 3")
    s.text(1060,285,"Δx₃ = ½(4+5)(1 s)",19,GREEN,260)
    s.text(1060,340,"= 4.5 m",22,GREEN,220)
    s.text(1060,415,"General: Δxₙ = u(1 s)\n + ½a(2n−1)(1 s)²",17,INK,255)
    s.text(1060,515,"Here v(t) stays positive, so\ndisplacement equals distance.",15,MUTED,255)
    return s


def d311() -> Scene:
    s = Scene("D3.11")
    s.title("Approaching particles close at the sum of their speed magnitudes", "Correct ordering: A is left of B (x_A < x_B); A moves right and B moves left.")
    x0=190; scale=185; y=430
    s.arrow(x0-60,y,x0+6.2*scale,y,INK,2)
    for n in range(0,7):
        x=x0+n*scale; s.line(x,y-9,x,y+9,GRID,1); s.text(x-9,y+16,str(n),14,MUTED,25)
    xa=x0+2*scale; xb=x0+5*scale
    s.dot(xa,y,7,BLUE); s.dot(xb,y,7,ORANGE)
    s.text(xa-55,y-65,"A at x_A",17,BLUE,120); s.text(xb-50,y-65,"B at x_B",17,ORANGE,120)
    s.arrow(xa,y-58,xa+225,y-58,BLUE,3.5); s.text(xa+58,y-100,"v_A right",16,BLUE,115)
    s.arrow(xb,y-58,xb-185,y-58,ORANGE,3.5); s.text(xb-180,y-100,"v_B left",16,ORANGE,110)
    # Gap bracket indicates x_B - x_A, which is shrinking.
    s.line(xa,y+85,xb,y+85,PURPLE,2); s.line(xa,y+73,xa,y+97,PURPLE,2); s.line(xb,y+73,xb,y+97,PURPLE,2)
    s.text(xa+105,y+93,"d = x_B − x_A",16,PURPLE,175)
    panel(s, 175, 620, 1070, 150, "SIGNED SEPARATION RATE")
    s.text(215,675,"ḋ = v_B(signed) − v_A(signed) = −v_B − v_A",19,INK,575)
    s.text(815,675,"closing speed = v_A + v_B",20,GREEN,380)
    s.text(215,725,"So x_B − x_A decreases at rate v_A + v_B.",16,MUTED,500)
    return s


def d41() -> Scene:
    s=Scene("D4.1"); s.title("Horizontal motion does not change vertical fall", "At equal times, a dropped ball and a horizontally launched ball have the same vertical coordinate.")
    panel(s,55,145,600,575,"DROPPED · x stays fixed")
    panel(s,745,145,600,575,"LAUNCHED HORIZONTALLY · x=v₀t")
    ys=[260,405,565]
    for i,y in enumerate(ys):
        s.dot(260,y,13,ORANGE); s.text(185,y+20,f"t={i}Δt",15,MUTED,100)
        s.dot(940+i*105,y,13,BLUE); s.text(870+i*105,y+20,f"t={i}Δt",15,MUTED,100)
        s.line(265,y,930+i*105,y,GRID,1,"dashed")
    # launch cliff and common vertical scale
    s.line(820,260,820,650,INK,3); s.line(820,650,1260,650,INK,3)
    s.arrow(820,260,925,260,BLUE,3.5)
    s.text(800,680,"same drop: ½g(iΔt)²",16,GREEN,240)
    s.text(115,750,"y_drop(t)=y_launch(t)=y₀−½gt²",21,GREEN,570)
    s.text(840,210,"v₀",17,BLUE,40)
    return s


def d42() -> Scene:
    s=Scene("D4.2"); s.title("Oblique projectile: range, height, time and symmetric velocities", "Ideal flight, same launch and landing height, no air resistance.")
    ox,oy=150,690; u=10; g=10; th=math.radians(40); T=2*u*math.sin(th)/g; R=u*math.cos(th)*T; H=u*u*math.sin(th)**2/(2*g); sx=105; sy=105
    s.arrow(ox-30,oy,ox+R*sx+110,oy,INK,2); s.arrow(ox,oy,ox,oy-330,INK,2)
    s.text(ox+R*sx+115,oy-15,"x",17,INK,25); s.text(ox-20,oy-350,"y",17,INK,25)
    pts=[]
    for i in range(41):
        t=T*i/40; x=u*math.cos(th)*t; y=u*math.sin(th)*t-.5*g*t*t; pts.append((ox+x*sx,oy-y*sy))
    polyline(s,pts,BLUE,3)
    apex=(ox+R*sx/2,oy-H*sy); land=(ox+R*sx,oy)
    s.line(apex[0],apex[1],apex[0],oy,MUTED,1.5,"dashed"); s.line(ox,oy+35,land[0],oy+35,TEAL,2)
    s.text(apex[0]+10,apex[1]-20,"H=v₀²sin²θ/(2g)",16,TEAL,235)
    s.text((ox+land[0])/2-40,oy+42,"R=v₀²sin(2θ)/g",16,TEAL,260)
    s.arrow(ox,oy,ox+245,oy-205,ORANGE,3); s.text(ox+105,oy-190,"v₀ at +θ",16,ORANGE,120)
    s.arrow(apex[0],apex[1],apex[0]+145,apex[1],GREEN,3); s.text(apex[0]+35,apex[1]+20,"v₀cosθ",15,GREEN,110)
    s.arrow(land[0],land[1],land[0]+150,land[1]+126,PURPLE,3); s.text(land[0]-15,land[1]-38,"v₀ at −θ",15,PURPLE,120)
    s.text(55,785,"time axis:  0 ───────────────── T = 2v₀sinθ/g",16,INK,610)
    return s


def d43() -> Scene:
    s=Scene("D4.3"); s.title("Complementary launch angles share a range", "Same launch speed and height: 30° and 60° have equal R; the 45° shot reaches farthest.")
    ox,oy=165,680; u=g=10; sx=92; sy=78
    s.arrow(ox,oy,ox+11*sx,oy,INK,2); s.arrow(ox,oy,ox,oy-360,INK,2)
    s.text(ox+11*sx+8,oy-15,"x",17,INK,25); s.text(ox-24,oy-380,"y",17,INK,25)
    for deg,col,dash in [(30,BLUE,"solid"),(60,ORANGE,"solid"),(45,GREEN,"dashed")]:
        th=math.radians(deg); T=2*u*math.sin(th)/g; R=u*math.cos(th)*T; pts=[]
        for i in range(41):
            t=T*i/40; x=u*math.cos(th)*t; y=u*math.sin(th)*t-.5*g*t*t; pts.append((ox+x*sx,oy-y*sy))
        polyline(s,pts,col,3,dash)
    r=u*u*math.sin(math.radians(60))/g
    s.line(ox+r*sx,oy-8,ox+r*sx,oy+8,PURPLE,2)
    s.text(ox+r*sx-80,oy+25,"same range R",17,PURPLE,150)
    panel(s,1040,180,300,250,"FLIGHT TIMES")
    s.text(1065,260,"T₆₀ = √3 T₃₀",22,ORANGE,240)
    s.text(1065,310,"The steeper 60° shot\nstays airborne longer.",16,MUTED,245)
    s.text(1065,385,"45°: Rmax=v₀²/g",18,GREEN,245)
    return s


def d44() -> Scene:
    s=Scene("D4.4"); s.title("Launching from a height adds flight time and range", "Illustrative cliff launch: h=4 m, v₀=10 m/s, θ=35°, g=10 m/s².")
    cliff=(200,370); ground=660; u=10; g=10; h=4; th=math.radians(35); T=(u*math.sin(th)+math.sqrt((u*math.sin(th))**2+2*g*h))/g; R=u*math.cos(th)*T; sx=54; sy=72
    s.line(95,ground,1260,ground,INK,2.2); s.line(95,ground,95,cliff[1],INK,3); s.line(95,cliff[1],cliff[0],cliff[1],INK,3)
    s.arrow(130,ground,130,cliff[1],PURPLE,2.5); s.text(90,505,"h",19,PURPLE,35)
    pts=[]
    for i in range(41):
        t=T*i/40; x=u*math.cos(th)*t; y=u*math.sin(th)*t-.5*g*t*t; pts.append((cliff[0]+x*sx,cliff[1]-y*sy))
    polyline(s,pts,BLUE,3)
    landing=(cliff[0]+R*sx,ground)
    s.dot(*cliff,6,BLUE); s.dot(*landing,7,RED)
    s.arrow(cliff[0],cliff[1],cliff[0]+190,cliff[1]-135,ORANGE,3); s.text(330,235,"v₀ at θ",17,ORANGE,100)
    s.line(cliff[0],ground+30,landing[0],ground+30,TEAL,2); s.text(530,ground+40,"R_h=v₀cosθ·T_h",17,TEAL,220)
    panel(s,1040,170,300,290,"LONGER FLIGHT")
    s.text(1060,250,"T_h=(v₀sinθ+\n√(v₀²sin²θ+2gh))/g",17,GREEN,260)
    s.text(1060,330,"T_h > 2v₀sinθ/g",18,INK,250)
    s.text(1060,385,"Compared with the same\nlaunch from ground level.",15,MUTED,255)
    return s


def d45() -> Scene:
    s=Scene("D4.5"); s.title("Rain velocity is relative to the observer", "If rain falls vertically at vᵣ and the man walks east at vₘ, the apparent rain comes from ahead.")
    panel(s,55,150,690,570,"GROUND FRAME")
    panel(s,785,150,560,570,"MAN'S FRAME")
    # Man walking east; rain velocity is vertical down in the ground frame.
    s.ellipse(175,280,56,56,INK,PALE_BLUE,2); s.line(203,336,203,460,INK,4); s.line(203,380,155,420,INK,3); s.line(203,380,250,420,INK,3)
    s.line(203,460,165,525,INK,3); s.line(203,460,242,525,INK,3)
    s.arrow(110,585,340,585,BLUE,3.5); s.text(125,600,"vₘ east",17,BLUE,115)
    for x in [390,500,610]:
        s.arrow(x,230,x,365,TEAL,2.8); s.text(x+8,285,"vᵣ",15,TEAL,38)
    s.text(110,210,"rain: vᵣ=(0,−vᵣ)",17,TEAL,220)
    o=(930,560); s.dot(*o,6,INK)
    s.arrow(*o,1070,560,BLUE,3.2); s.text(1010,575,"vₘ",17,BLUE,40)
    s.arrow(*o,930,430,TEAL,3.2); s.text(945,445,"vᵣ",17,TEAL,40)
    s.arrow(*o,790,690,ORANGE,4); s.text(1050,405,"vᵣ/ₘ=(−vₘ,−vᵣ)",16,ORANGE,230)
    s.text(860,250,"tan α = vₘ/vᵣ",20,PURPLE,210)
    # Umbrella shaft leans forward (east) to shield the apparent rain.
    s.line(1110,360,1210,245,PURPLE,4); s.line(1070,380,1170,265,PURPLE,2)
    s.text(1120,210,"tilt forward",15,PURPLE,140)
    s.text(830,650,"Apparent velocity points down-and-back;\nthe incoming rain direction is up-and-forward.",15,MUTED,470)
    return s


def d46() -> Scene:
    s=Scene("D4.6"); s.title("Angular speed sets tangential speed", "For a circle of radius R, arc length s=Rθ and v=Rω when θ is measured in radians.")
    cx,cy,r=455,515,235; theta=math.radians(45); px=cx+r*math.cos(theta); py=cy-r*math.sin(theta)
    s.ellipse(cx-r,cy-r,2*r,2*r,GRID,"transparent",2)
    arc_pts=[(cx+r*math.cos(theta*i/16),cy-r*math.sin(theta*i/16)) for i in range(17)]
    polyline(s,arc_pts,PURPLE,3)
    s.dot(cx,cy,5,INK)
    s.arrow(cx,cy,px,py,BLUE,3); s.dot(px,py,8,ORANGE)
    tx,ty=-math.sin(theta),-math.cos(theta)
    s.arrow(px,py,px+150*tx,py+150*ty,TEAL,4)
    s.text(535,390,"R",19,BLUE,35); s.text(px-35,py-42,"particle",15,ORANGE,95); s.text(px-120,py-105,"v=Rω",19,TEAL,100)
    s.text(625,420,"arc s=Rθ",15,PURPLE,105); s.text(350,495,"θ",21,PURPLE,40)
    # Arc cue, angular-velocity curl, and equation box.
    s.arrow(680,520,665,455,PURPLE,2.2); s.text(690,465,"ω=dθ/dt",19,PURPLE,130)
    panel(s,825,205,490,340,"ARC KINEMATICS")
    s.text(865,290,"s=Rθ",27,BLUE,180)
    s.text(865,355,"v=ds/dt=R dθ/dt",21,INK,360)
    s.text(865,410,"v=Rω",28,GREEN,180)
    s.text(865,480,"v is tangent to the circle; ω is\nangular rate about the centre.",16,MUTED,370)
    return s


def d47() -> Scene:
    s=Scene("D4.7"); s.title("A changing velocity points toward the centre", "For a small turn Δθ, |Δv|≈vΔθ; divide by Δt to obtain a_c=v²/R.")
    cx,cy,r=380,500,190
    s.ellipse(cx-r,cy-r,2*r,2*r,GRID,"transparent",2); s.dot(cx,cy,5,INK); s.text(cx-20,cy+20,"O",15,INK,30)
    t1,t2=math.radians(42),math.radians(28)
    p1=(cx+r*math.cos(t1),cy-r*math.sin(t1)); p2=(cx+r*math.cos(t2),cy-r*math.sin(t2))
    s.dot(*p1,7,BLUE); s.dot(*p2,7,TEAL)
    v=100
    s.arrow(*p1,p1[0]+v*math.sin(t1),p1[1]+v*math.cos(t1),BLUE,3)
    s.arrow(*p2,p2[0]+v*math.sin(t2),p2[1]+v*math.cos(t2),TEAL,3)
    s.text(p1[0]+30,p1[1]+35,"v₁",16,BLUE,40); s.text(p2[0]+15,p2[1]+75,"v₂",16,TEAL,40)
    origin=(720,350); v1tip=(850,495); v2tip=(810,518)
    s.arrow(origin[0],origin[1],v1tip[0],v1tip[1],BLUE,3); s.arrow(origin[0],origin[1],v2tip[0],v2tip[1],TEAL,3)
    s.arrow(v1tip[0],v1tip[1],v2tip[0],v2tip[1],ORANGE,3)
    s.text(855,488,"v₁",16,BLUE,45); s.text(780,520,"v₂",16,TEAL,45); s.text(820,535,"Δv=v₂−v₁",15,ORANGE,100)
    s.text(810,240,"Velocity-vector triangle",17,INK,250)
    s.text(810,625,"|Δv|≈vΔθ",22,ORANGE,220)
    s.text(810,675,"a_c=|Δv|/Δt=vω=v²/R",20,GREEN,360)
    s.text(90,745,"As the two positions approach one another, Δv points radially inward.",17,MUTED,700)
    return s


def d48() -> Scene:
    s=Scene("D4.8"); s.title("Non-uniform circular motion has radial and tangential acceleration", "At the right-hand point, increasing speed means a_t points upward along the tangent.")
    cx,cy,r=440,485,235; p=(cx+r,cy)
    s.ellipse(cx-r,cy-r,2*r,2*r,GRID,"transparent",2); s.dot(cx,cy,5,INK); s.dot(*p,8,ORANGE)
    s.arrow(*p,cx+90,cy,BLUE,4); s.text(520,455,"a_c=v²/R",18,BLUE,120)
    s.arrow(*p,p[0],p[1]-155,TEAL,4); s.text(690,340,"a_t=dv/dt",18,TEAL,140)
    s.arrow(*p,cx+90,p[1]-155,GREEN,4); s.text(550,310,"a=a_c+a_t",19,GREEN,150)
    s.arrow(*p,p[0]+130,p[1]-5,PURPLE,3); s.text(690,500,"v tangent",16,PURPLE,110)
    s.text(820,635,"a_c ⟂ v; a_t is forward\nwhen speed is increasing.",17,MUTED,330)
    return s


def d49() -> Scene:
    s=Scene("D4.9"); s.title("Projectile launched above an inclined plane", "The launch angle β is measured from the slope; the absolute angle is α+β.")
    alpha,beta=math.radians(20),math.radians(35); u=10; g=10; T=2*u*math.sin(beta)/(g*math.cos(alpha)); sx=90; sy=90
    x0,y0=250,650; ramp_end=(1190,y0-(1190-x0)*math.tan(alpha))
    s.line(95,y0+(x0-95)*math.tan(alpha),ramp_end[0],ramp_end[1],INK,3)
    s.text(115,590,"incline α",17,INK,115)
    R=u*math.cos(alpha+beta)*T
    pts=[]
    for i in range(41):
        t=T*i/40; x=u*math.cos(alpha+beta)*t; y=u*math.sin(alpha+beta)*t-.5*g*t*t; pts.append((x0+x*sx,y0-y*sy))
    polyline(s,pts,BLUE,3)
    landing=pts[-1]; s.dot(x0,y0,7,ORANGE); s.dot(*landing,7,RED)
    component_scale=16; launch_len=u*component_scale
    along_len=u*math.cos(beta)*component_scale; normal_len=u*math.sin(beta)*component_scale
    s.arrow(x0,y0,x0+launch_len*math.cos(alpha+beta),y0-launch_len*math.sin(alpha+beta),ORANGE,3.5)
    s.text(x0+45,y0-145,"u at α+β",16,ORANGE,130)
    s.arrow(x0,y0,x0+along_len*math.cos(alpha),y0-along_len*math.sin(alpha),TEAL,2.5)
    s.text(x0+72,y0-83,"u cosβ",15,TEAL,90)
    s.arrow(x0,y0,x0-normal_len*math.sin(alpha),y0-normal_len*math.cos(alpha),PURPLE,2.5)
    s.text(x0-135,y0-115,"u sinβ",15,PURPLE,95)
    off=35; oxn=off*math.sin(alpha); oyn=off*math.cos(alpha)
    range_start=(x0+oxn,y0+oyn); range_end=(landing[0]+oxn,landing[1]+oyn)
    s.line(*range_start,*range_end,TEAL,2)
    s.text((range_start[0]+range_end[0])/2-60,(range_start[1]+range_end[1])/2+24,"range along slope",16,TEAL,190)
    s.text(870,225,"T=2u sinβ/(g cosα)",18,GREEN,280)
    return s


def d410() -> Scene:
    s=Scene("D4.10"); s.title("A river current changes the ground-frame path", "Illustration: river speed 3 m/s, boat speed relative to water 5 m/s, width 10 m.")
    panel(s,55,150,610,560,"A · POINT STRAIGHT ACROSS")
    panel(s,715,150,630,560,"B · AIM UPSTREAM")
    # Banks and current arrows.
    for left,right in [(100,620),(760,1320)]:
        s.line(left,270,right,270,INK,2); s.line(left,610,right,610,INK,2)
        for yy in [335,425,515]: s.arrow(left+25,yy,right-20,yy,TEAL,2.5)
    oA=(220,570); s.dot(*oA,6,BLUE); s.arrow(*oA,220,320,BLUE,3.4); s.text(230,370,"v_b=5",16,BLUE,80)
    s.arrow(*oA,370,320,GREEN,3.5); s.text(345,285,"ground path",15,GREEN,110)
    s.text(130,635,"drift downstream",15,ORANGE,150)
    oB=(900,570); s.dot(*oB,6,BLUE); s.arrow(*oB,750,370,ORANGE,3.4); s.text(755,420,"boat points\nupstream",15,ORANGE,115)
    s.arrow(*oB,900,370,GREEN,3.5); s.text(915,395,"straight\nacross",15,GREEN,95)
    s.arrow(*oB,1050,570,TEAL,2.8); s.text(1000,590,"current vᵣ",15,TEAL,105)
    s.text(1005,240,"v_b sinα=vᵣ",17,PURPLE,150)
    s.text(105,675,"t_A=d/v_b=2.0 s",16,INK,200); s.text(790,675,"t_B=d/(v_b cosα)=2.5 s",16,INK,275)
    return s


def d411() -> Scene:
    s=Scene("D4.11"); s.title("The safety parabola bounds every fixed-speed projectile", "Envelope: y=v₀²/(2g)−gx²/(2v₀²); all launch angles lie on or below it.")
    ox,oy=155,690; sx=88; sy=54; umax=10; g=10
    s.arrow(ox,oy,ox+11*sx,oy,INK,2); s.arrow(ox,oy,ox,oy-330,INK,2)
    s.text(ox+11*sx+8,oy-15,"x",16,INK,25); s.text(ox-25,oy-350,"y",16,INK,25)
    # Envelope from the vertical-launch apex to the farthest horizontal range.
    env=[]
    for i in range(41):
        x=10*i/40; y=5-x*x/20; env.append((ox+x*sx,oy-y*sy))
    polyline(s,env,PURPLE,2.7,"dashed")
    for deg,col in [(30,BLUE),(45,GREEN),(60,ORANGE)]:
        th=math.radians(deg); T=2*umax*math.sin(th)/g; pts=[]
        for i in range(41):
            t=T*i/40; x=umax*math.cos(th)*t; y=umax*math.sin(th)*t-.5*g*t*t; pts.append((ox+x*sx,oy-y*sy))
        polyline(s,pts,col,2.5)
    s.text(230,320,"30°",16,BLUE,50); s.text(545,320,"45°",16,GREEN,50); s.text(760,370,"60°",16,ORANGE,50)
    s.text(445,405,"safety envelope",16,PURPLE,170)
    s.dot(ox,oy-5*sy,5,PURPLE); s.text(ox+15,oy-5*sy-25,"H_env=v₀²/(2g)",16,PURPLE,195)
    s.line(ox+10*sx,oy-5,ox+10*sx,oy+8,RED,2); s.text(ox+10*sx-115,oy+28,"R_max=v₀²/g",16,RED,160)
    return s


def d412() -> Scene:
    s=Scene("D4.12"); s.title("The total acceleration tilts forward from the inward radial direction", "At the rightmost point, inward is left and increasing speed adds an upward tangential component.")
    cx,cy,r=430,495,225; p=(cx+r,cy)
    s.ellipse(cx-r,cy-r,2*r,2*r,GRID,"transparent",2); s.dot(cx,cy,5,INK); s.dot(*p,8,ORANGE)
    s.arrow(*p,cx+70,cy,BLUE,3.5); s.text(520,cy+22,"a_c",17,BLUE,45)
    s.arrow(*p,p[0],p[1]-175,TEAL,3.5); s.text(690,345,"a_t",17,TEAL,45)
    s.arrow(*p,cx+70,p[1]-175,GREEN,4); s.text(545,315,"a",20,GREEN,35)
    phi=math.atan2(175,p[0]-(cx+70))
    phi_arc=[(p[0]+42*math.cos(math.pi-phi*i/16),p[1]-42*math.sin(math.pi-phi*i/16)) for i in range(17)]
    polyline(s,phi_arc,PURPLE,2.2); s.text(p[0]-82,p[1]-58,"φ",22,PURPLE,35)
    s.text(800,545,"tanφ=a_t/a_c",20,PURPLE,200)
    s.text(800,600,"φ is measured from the\ninward radial direction.",16,MUTED,270)
    return s


def d51() -> Scene:
    s=Scene("D5.1"); s.title("Inertial frames need no fictitious force", "The same ball appears different when viewed from a braking car.")
    panel(s,55,150,620,555,"STATIONARY ROOM · inertial frame")
    panel(s,725,150,620,555,"BRAKING CAR · accelerating frame")
    # Table and ball in room.
    s.line(125,560,610,560,INK,5); s.line(165,560,165,630,INK,3); s.line(570,560,570,630,INK,3)
    s.ellipse(340,495,60,60,BLUE,PALE_BLUE,2); s.text(260,410,"ball remains at rest",17,BLUE,190)
    s.text(125,245,"ΣFₓ=0  ⇒  aₓ=0",20,GREEN,260)
    # Braking car: car decelerates leftward while ball continues forward.
    s.line(785,575,1285,575,INK,4); s.line(850,575,900,635,INK,3); s.line(1220,575,1270,635,INK,3)
    s.ellipse(1000,470,60,60,ORANGE,PALE_ORANGE,2); s.arrow(1000,455,1180,455,ORANGE,3.2); s.text(1050,420,"apparent forward slide",16,ORANGE,200)
    s.arrow(1030,500,1135,500,PURPLE,2.8); s.text(1040,510,"F_pseudo",14,PURPLE,90)
    s.arrow(1160,650,920,650,RED,3.3); s.text(985,670,"car acceleration a₀ backward",15,RED,240)
    s.text(790,245,"In car frame add pseudo force\nF_pseudo=−m a₀.",18,PURPLE,340)
    return s


def d52() -> Scene:
    s=Scene("D5.2"); s.title("Action–reaction forces act on different bodies", "Each interaction pair is equal and opposite; neither pair cancels on the block alone.")
    panel(s,55,150,620,555,"EARTH ↔ BLOCK")
    panel(s,725,150,620,555,"TABLE ↔ BLOCK")
    # Gravitational pair.
    s.rect(255,355,200,120,INK,PALE_BLUE,2,True); s.text(270,395,"block",20,INK,75)
    s.ellipse(245,545,220,90,GRID,PALE_ORANGE,2); s.text(320,575,"Earth",20,INK,85)
    s.arrow(355,395,355,465,BLUE,3.5); s.text(370,410,"F_E→b=mg",17,BLUE,130)
    s.arrow(355,545,355,475,TEAL,3.5); s.text(370,500,"F_b→E=mg",16,TEAL,145)
    s.text(90,230,"equal magnitude, opposite direction",16,MUTED,440)
    # Normal pair across contact.
    s.rect(910,435,220,120,INK,PALE_BLUE,2,True); s.text(930,478,"block",20,INK,80)
    s.rect(835,555,370,45,INK,PALE_TEAL,2); s.text(865,610,"table",17,INK,85)
    s.arrow(1020,495,1020,420,BLUE,3.5); s.text(1035,430,"N_table→block",16,BLUE,180)
    s.arrow(1020,555,1020,630,TEAL,3.5); s.text(1040,610,"N_block→table",15,TEAL,175)
    s.text(795,230,"third-law partners belong on separate FBDs",16,MUTED,465)
    return s


def d53() -> Scene:
    s=Scene("D5.3"); s.title("A free-body diagram isolates the block and resolves its weight", "Incline rises to the right; choose +x downhill and +y normal to the plane.")
    panel(s,55,155,510,555,"PHYSICAL SETUP")
    panel(s,610,155,735,555,"ISOLATED BLOCK · FBD")
    # Ramp and a block whose lower face is aligned with the incline.
    incline=math.atan2(220,410); contact=(360,610-(360-105)*math.tan(incline))
    s.line(105,610,515,390,INK,5)
    block_h=70; block_c=(contact[0]-math.sin(incline)*block_h/2,contact[1]-math.cos(incline)*block_h/2)
    s.rect(block_c[0]-60,block_c[1]-block_h/2,120,block_h,BLUE,PALE_BLUE,2,True,angle=-incline)
    s.text(305,430,"block",17,INK,80); s.text(125,625,"rough incline θ",16,MUTED,180)
    # FBD axes and vectors, x downhill-left, y outward/up-left.
    o=(860,495); s.rect(805,450,110,82,BLUE,PALE_BLUE,2,True); s.dot(*o,5,INK)
    s.arrow(*o,690,585,INK,2.2); s.text(660,585,"+x downhill",15,INK,120)
    s.arrow(*o,755,310,INK,2.2); s.text(685,285,"+y normal",15,INK,130)
    s.arrow(*o,860,675,RED,3.7); s.text(875,610,"mg",18,RED,45)
    s.arrow(*o,773,332,TEAL,3.4); s.text(745,330,"N",18,TEAL,35)
    s.arrow(*o,990,425,ORANGE,3.2); s.text(995,400,"f up-slope",15,ORANGE,110)
    s.arrow(*o,785,535,PURPLE,2.5); s.text(650,540,"mg sinθ",16,PURPLE,100)
    s.arrow(*o,935,636,BLUE,2.5); s.text(945,620,"mg cosθ",16,BLUE,115)
    s.text(1010,235,"ΣFₓ=mg sinθ−f=maₓ",18,GREEN,280)
    s.text(1010,280,"ΣFᵧ=N−mg cosθ=maᵧ",17,GREEN,300)
    return s


def d54() -> Scene:
    s=Scene("D5.4"); s.title("Scale reading is the normal force, not always mg", "Three elevator cases: rest, upward acceleration, and free fall.")
    cards=[(55,"AT REST",0),(500,"ACCELERATING UP",1),(945,"FREE FALL",2)]
    for x,label,case in cards:
        panel(s,x,155,400,555,label)
        s.rect(x+125,345,150,170,BLUE,PALE_BLUE,2,True); s.ellipse(x+170,285,60,60,ORANGE,PALE_ORANGE,2)
        s.rect(x+105,520,190,30,INK,PALE_TEAL,2); s.text(x+155,555,"scale",15,INK,80)
        o=(x+200,425)
        if case==0:
            s.arrow(*o,x+200,340,TEAL,3); s.text(x+215,345,"N=mg",18,TEAL,90)
            s.arrow(*o,x+200,510,RED,3); s.text(x+215,480,"mg",17,RED,45)
            s.text(x+90,620,"N=mg",22,GREEN,130)
        elif case==1:
            s.arrow(*o,x+200,315,TEAL,3); s.text(x+215,325,"N",18,TEAL,30)
            s.arrow(*o,x+200,500,RED,3); s.text(x+215,470,"mg",17,RED,45)
            s.arrow(x+325,440,x+325,360,ORANGE,2.7); s.text(x+335,385,"a",17,ORANGE,30)
            s.text(x+75,620,"N=m(g+a)",21,GREEN,190)
        else:
            s.arrow(*o,x+200,500,RED,3); s.text(x+215,470,"mg",17,RED,45)
            s.text(x+70,620,"N=0 · weightless",20,GREEN,250)
    return s


def d55() -> Scene:
    s=Scene("D5.5"); s.title("Static friction adjusts, then drops to kinetic friction", "Idealized dry-friction model with μₖ<μₛ and fixed normal force N.")
    ox,oy=220,650; sx=140; sy=48; Fmax=5; fkin=3
    s.arrow(ox,oy,ox+6.7*sx,oy,INK,2); s.arrow(ox,oy,ox,oy-6.2*sy,INK,2)
    s.text(ox+6.7*sx+6,oy-15,"applied force F",16,INK,135); s.text(ox-60,oy-6.2*sy-15,"friction f",16,INK,85)
    s.line(ox,oy,ox+Fmax*sx,oy-Fmax*sy,BLUE,3.5)
    s.dot(ox+Fmax*sx,oy-Fmax*sy,7,ORANGE)
    s.line(ox+Fmax*sx,oy-Fmax*sy,ox+Fmax*sx,oy-fkin*sy,RED,3)
    s.line(ox+Fmax*sx,oy-fkin*sy,ox+6.1*sx,oy-fkin*sy,TEAL,3.5)
    s.line(ox,oy-fkin*sy,ox+6.1*sx,oy-fkin*sy,GRID,1,"dashed")
    s.text(ox+Fmax*sx-50,oy-Fmax*sy-40,"μₛN",18,ORANGE,70)
    s.text(ox+Fmax*sx+15,oy-fkin*sy+4,"μₖN",18,TEAL,75)
    s.text(280,520,"static: f=F",17,BLUE,110); s.text(965,470,"kinetic: f≈μₖN",17,TEAL,180)
    s.text(870,255,"At breakaway, friction drops\nfrom μₛN to μₖN.",17,MUTED,300)
    return s


def d56() -> Scene:
    s=Scene("D5.6"); s.title("Friction accelerates the top block until it reaches its limit", "Two blocks move together while a≤μₛg; beyond that, the top block slips backward relative to M.")
    s.rect(260,380,440,170,INK,PALE_ORANGE,3,True); s.text(440,450,"M",27,INK,60)
    s.rect(390,255,180,125,BLUE,PALE_BLUE,3,True); s.text(455,300,"m",26,INK,55)
    s.arrow(120,465,250,465,RED,4); s.text(125,425,"F",22,RED,35)
    s.arrow(480,255,600,255,TEAL,3.5); s.text(510,215,"friction on m",15,TEAL,140)
    s.arrow(480,380,360,380,ORANGE,3.5); s.text(320,350,"friction on M",15,ORANGE,140)
    s.arrow(850,390,1060,390,GREEN,3.5); s.text(895,345,"a=F/(M+m)",18,GREEN,170)
    panel(s,780,470,520,245,"NO SLIP CONDITION")
    s.text(810,545,"m a ≤ μₛ m g",23,BLUE,260)
    s.text(810,600,"F_max=(M+m)μₛg",22,GREEN,300)
    s.text(810,660,"Above threshold: m lags,\nslipping left relative to M.",16,RED,350)
    return s


def pulley_scene(key: str, title: str, subtitle: str, movable_mass: str, free_mass: str,
                 movable_coord: str, free_coord: str, constraint: str) -> Scene:
    s=Scene(key); s.title(title,subtitle)
    s.line(145,180,1195,180,INK,5); s.dot(410,180,5,INK); s.text(350,145,"fixed end",15,INK,95)
    # Vertical support strands meet the two tangency points of the movable pulley.
    s.ellipse(520,195,110,110,INK,PALE_BLUE,3); s.dot(575,250,5,INK)
    s.ellipse(410,455,110,110,INK,PALE_ORANGE,3); s.dot(465,510,5,INK)
    # Rope: fixed ceiling anchor, around movable pulley, vertically to the fixed pulley,
    # over its upper half, then down to the free mass.
    rope=[(410,180),(410,510),(422,540),(445,558),(465,565),(485,558),(508,540),(520,510),
          (520,250),(535,210),(575,195),(615,210),(630,250),(630,565)]
    polyline(s,rope,TEAL,3)
    # The attached mass follows the lower pulley; the other mass hangs from the free end.
    s.line(465,565,465,600,INK,3); s.rect(380,600,170,100,BLUE,PALE_BLUE,3,True); s.text(435,635,movable_mass,23,INK,70)
    s.rect(575,565,110,135,ORANGE,PALE_ORANGE,3,True); s.text(600,610,free_mass,23,INK,70)
    s.arrow(300,480,300,600,BLUE,3); s.text(315,515,movable_coord,18,BLUE,95)
    s.arrow(760,450,760,585,ORANGE,3); s.text(775,500,free_coord,18,ORANGE,95)
    panel(s,110,725,1110,90,"STRING-LENGTH CONSTRAINT · downward coordinates")
    s.text(145,765,constraint,20,GREEN,1000)
    return s


def d57() -> Scene:
    return pulley_scene("D5.7","The movable-pulley constraint doubles the free-end acceleration",
        "Downward coordinates: x₁ for the free end carrying m₁; x₂ for the movable pulley carrying m₂.",
        "m₂","m₁","x₂↓","x₁↓","L=x₁+2x₂+const  ⇒  a₁+2a₂=0  ⇒  a₁=−2a₂")


def d58() -> Scene:
    s=Scene("D5.8"); s.title("Friction reverses direction between the two banked-road limits", "Cross-section: the outer edge is higher; inward is down the bank.")
    panel(s,55,150,620,560,"MAXIMUM SPEED")
    panel(s,725,150,620,560,"MINIMUM SPEED")
    bank=math.atan2(205,455); body_w,body_h=140,52
    for ox,high in [(120,True),(790,False)]:
        # The road rises right; the car's lower face lies on the banked surface.
        left=(ox+45,590); right=(ox+500,385); s.line(*left,*right,INK,5)
        s.line(ox+45,610,ox+500,610,GRID,1)
        cx=ox+280; cy=590-(cx-left[0])*math.tan(bank); contact=(cx,cy)
        center=(cx-math.sin(bank)*body_h/2,cy-math.cos(bank)*body_h/2)
        s.rect(center[0]-body_w/2,center[1]-body_h/2,body_w,body_h,BLUE,PALE_BLUE,2,True,angle=-bank)
        o=center
        s.arrow(*o,o[0],o[1]+125,RED,3); s.text(o[0]+8,o[1]+92,"mg",16,RED,45)
        s.arrow(*o,o[0]-math.sin(bank)*145,o[1]-math.cos(bank)*145,TEAL,3); s.text(o[0]-75,o[1]-145,"N",17,TEAL,35)
        fx=o[0]-math.cos(bank)*145 if high else o[0]+math.cos(bank)*145
        fy=o[1]+math.sin(bank)*145 if high else o[1]-math.sin(bank)*145
        s.arrow(*o,fx,fy,ORANGE,3.2); s.text(fx-20,fy+8,"f",17,ORANGE,25)
        s.arrow(*o,o[0]-180,o[1],PURPLE,2.5); s.text(o[0]-205,o[1]+8,"inward",14,PURPLE,70)
        s.text(ox+100,650,"f points down-slope" if high else "f points up-slope",16,ORANGE,200)
    s.text(220,240,"fₛ,max toward centre",17,INK,210); s.text(890,240,"fₛ,min away from centre",17,INK,240)
    s.text(460,760,"v_min ≤ v ≤ v_max",20,GREEN,220)
    return s


def d59() -> Scene:
    s=Scene("D5.9"); s.title("Vertical-circle speed and tension vary with angle", "θ=0 at the bottom; choose v_bottom²=5gR. The string is just taut at θ=π.")
    # Left: tension; right: speed. Normalize by mg and sqrt(gR).
    panels=[(65,190,570,500,"T/(mg)=3(1+cosθ)",BLUE),(755,190,570,500,"v/√(gR)=√(3+2cosθ)",GREEN)]
    for x,y,w,h,label,col in panels:
        panel(s,x,y,w,h,label); ox=x+85; oy=y+h-80; ww=w-120; hh=h-160
        s.arrow(ox,oy,ox+ww,oy,INK,1.8); s.arrow(ox,oy,ox,y+80,INK,1.8)
        pts=[]
        for i in range(41):
            th=math.pi*i/40
            val=3*(1+math.cos(th)) if col==BLUE else math.sqrt(3+2*math.cos(th))
            ymax=6 if col==BLUE else math.sqrt(5)
            pts.append((ox+ww*th/math.pi,oy-hh*val/ymax))
        polyline(s,pts,col,3)
        for i,lab in [(0,"0 bottom"),(20,"π/2"),(40,"π top")]:
            xx=ox+ww*i/40; s.line(xx,oy-5,xx,oy+5,GRID,1); s.text(xx-28,oy+14,lab,12,MUTED,62)
    s.text(200,145,"T falls from 6mg to 0",16,BLUE,200); s.text(895,145,"v_top=√(gR)",16,GREEN,160)
    s.text(585,745,"θ₀=π: limiting slack point (T=0 at the top)",17,PURPLE,390)
    return s


def d510() -> Scene:
    s=Scene("D5.10"); s.title("The wedge constraint is a displacement triangle", "Ramp slopes down-right; s is the block's displacement relative to the wedge, x_w the wedge translation.")
    # Initial and translated wedge profiles.
    s.line(160,350,760,670,INK,4); s.line(760,670,760,350,INK,4); s.line(160,350,760,350,GRID,1)
    s.line(250,390,850,710,MUTED,2,"dashed"); s.line(850,710,850,390,MUTED,2,"dashed")
    theta=math.atan2(320,600); p=(440,350+(440-160)*math.tan(theta))
    block_h=82; block_c=(p[0]+math.sin(theta)*block_h/2,p[1]-math.cos(theta)*block_h/2)
    s.rect(block_c[0]-65,block_c[1]-block_h/2,130,block_h,BLUE,PALE_BLUE,2,True,angle=theta); s.text(415,450,"block",18,INK,80)
    # Relative slide and wedge translation vectors form the ground displacement.
    rel=(610,p[1]+90); wedge=(560,p[1]); ground=(730,p[1]+90)
    s.arrow(*p,*rel,ORANGE,3.5); s.text(525,560,"s along slope",16,ORANGE,130)
    s.arrow(*p,*wedge,TEAL,3.5); s.text(485,460,"x_w",16,TEAL,55)
    s.arrow(*p,*ground,GREEN,3.5); s.text(610,465,"ground Δr",16,GREEN,110)
    s.line(rel[0],rel[1],ground[0],ground[1],MUTED,1.5,"dashed")
    panel(s,885,195,430,415,"COMPONENTS")
    s.text(915,275,"Δx_b=x_w+s cosθ",20,BLUE,340)
    s.text(915,330,"Δy_b=−s sinθ",20,BLUE,300)
    s.text(915,420,"Stay on the wedge:\nblock's position satisfies\nthe translated incline line.",16,MUTED,350)
    s.text(915,545,"Differentiate twice for\nvelocity/acceleration constraints.",15,GREEN,350)
    return s


def d511() -> Scene:
    s=Scene("D5.11"); s.title("Tension always points to the circle centre; weight always points down", "Four positions; centripetal acceleration is inward, not an extra force.")
    cx,cy,r=430,485,200; s.ellipse(cx-r,cy-r,2*r,2*r,GRID,"transparent",2); s.dot(cx,cy,5,INK); s.text(cx-18,cy+18,"O",15,INK,25)
    angles=[("bottom",-90), ("θ=45°",-45), ("side",0), ("top",90)]
    for label,deg in angles:
        th=math.radians(deg); p=(cx+r*math.cos(th),cy-r*math.sin(th)); s.dot(*p,7,BLUE)
        # inward radial tension; weight always down.
        inward=(cx-p[0],cy-p[1]); mag=0.48
        s.arrow(*p,p[0]+mag*inward[0],p[1]+mag*inward[1],TEAL,2.8)
        s.arrow(*p,p[0],p[1]+90,RED,2.8)
        s.text(p[0]-35,p[1]+(38 if deg<0 else -45),label,14,INK,95)
    s.text(780,245,"At top: T and mg both point inward.",18,GREEN,420)
    s.text(780,305,"At bottom: T inward/up; mg outward/down.",18,INK,440)
    s.text(780,380,"At the side, mg is tangential;\nT supplies the radial force.",17,MUTED,420)
    s.text(780,500,"ΣF_radial = mv²/R",22,PURPLE,300)
    s.text(780,555,"Centripetal force means the\nnet inward force, not a new force.",16,RED,400)
    return s


def d512() -> Scene:
    return pulley_scene("D5.12","Two-pulley constraint: the free end moves twice as far",
        "Downward coordinates: x₁ for movable-pulley mass m₁; x₂ for free-end mass m₂.",
        "m₁","m₂","x₁↓","x₂↓","L=2x₁+x₂+const  ⇒  2a₁+a₂=0  ⇒  a₂=−2a₁")


def d61() -> Scene:
    s=Scene("D6.1"); s.title("Work sign comes from force dotted with displacement", "Six short cases; use W=F·d=Fd cosφ.")
    cases=[("Push right",BLUE,"F→  d→","W>0"),("Friction",ORANGE,"f←  d→","W<0"),("Gravity / level",PURPLE,"mg↓  d→","W=0"),("Falling",GREEN,"mg↓  d↓","W>0"),("Lift",TEAL,"F_lifter↑, mg↓  d↑","W_lifter>0; W_g<0"),("Centripetal",RED,"F_c ⟂ v","W=0")]
    for i,(title,col,vecs,result) in enumerate(cases):
        x=55+(i%3)*445; y=150+(i//3)*300
        panel(s,x,y,410,265,title)
        if i==5:
            cx,cy,r=x+205,y+130,42; s.ellipse(cx-r,cy-r,2*r,2*r,GRID,"transparent",1.5); p=(cx+r,cy); s.dot(*p,7,RED)
        else:
            s.rect(x+145,y+90,120,75,INK,PALE_BLUE,2,True)
        s.text(x+34,y+185,vecs,17,col,330)
        s.text(x+65,y+225,result,19,GREEN if "W>0" in result else RED if "W<0" in result else PURPLE,300)
        if i==0: s.arrow(x+265,y+127,x+360,y+127,col,3)
        elif i==1: s.arrow(x+145,y+127,x+50,y+127,col,3)
        elif i==2: s.arrow(x+205,y+125,x+205,y+185,col,3)
        elif i==3: s.arrow(x+205,y+125,x+205,y+185,col,3)
        elif i==4: s.arrow(x+265,y+110,x+265,y+45,BLUE,2.6); s.arrow(x+205,y+140,x+205,y+175,RED,2.6)
        else:
            s.arrow(*p,cx,cy,RED,3); s.arrow(*p,p[0],p[1]-72,BLUE,3)
    return s


def d62() -> Scene:
    s=Scene("D6.2"); s.title("Signed area under F(x) is work", "Areas above the x-axis contribute positive work; areas below contribute negative work.")
    ox,oy=185,465; s.arrow(ox,oy,1190,oy,INK,2); s.arrow(ox,oy,ox,190,INK,2)
    s.text(1195,oy-15,"x",17,INK,25); s.text(ox-22,175,"F",17,INK,25)
    positive=[(ox,oy),(330,335),(480,265),(620,430),(690,oy)]
    negative=[(690,oy),(800,520),(960,575),(1120,480),(1120,oy)]
    hatch_polygon(s,positive,"#cde8d7"); hatch_polygon(s,negative,"#f2d2d0")
    pts=[(ox,oy),(330,335),(480,265),(620,430),(800,520),(960,575),(1120,480)]
    polyline(s,pts,BLUE,3.5)
    s.line(330,335,330,oy,GRID,1,"dashed"); s.line(620,430,620,oy,GRID,1,"dashed"); s.line(800,520,800,oy,GRID,1,"dashed"); s.line(960,575,960,oy,GRID,1,"dashed")
    s.text(405,370,"+W₁",18,GREEN,65); s.text(835,510,"−W₂",18,RED,65)
    s.text(940,260,"W_net=Σ signed areas",21,PURPLE,290)
    s.text(205,650,"W=∫ₓᵢˣᶠ F(x) dx",22,INK,320)
    return s


def d63() -> Scene:
    s=Scene("D6.3"); s.title("Constant power gives an asymptotic top speed", "Qualitative v(t): at the limit, engine force equals resistance and v_max=P/f.")
    panel(s,55,155,570,540,"FORCES ON THE CAR")
    s.rect(190,410,310,120,BLUE,PALE_BLUE,3,True); s.ellipse(230,505,70,70,INK,GRID,2); s.ellipse(405,505,70,70,INK,GRID,2)
    s.arrow(500,455,605,455,TEAL,3.5); s.text(515,415,"F=P/v",18,TEAL,100)
    s.arrow(190,490,90,490,RED,3.5); s.text(105,450,"resistance f",17,RED,110)
    s.text(150,630,"P=Fv; at v_max: F=f",21,GREEN,360)
    # v-t approach to P/f.
    panel(s,700,155,645,540,"SPEED vs TIME")
    ox,oy=790,620; s.arrow(ox,oy,1280,oy,INK,2); s.arrow(ox,oy,ox,260,INK,2)
    s.text(1280,630,"t",16,INK,25); s.text(770,240,"v",16,INK,25)
    vmax=300; s.line(ox,oy-vmax,1270,oy-vmax,GRID,2,"dashed"); s.text(1130,oy-vmax-28,"v_max=P/f",17,GREEN,150)
    curve=[]
    for i in range(41):
        t=i/40; v=vmax*(1-math.exp(-4*t)); curve.append((ox+t*460,oy-v))
    polyline(s,curve,BLUE,3.3)
    return s


def d64() -> Scene:
    s=Scene("D6.4"); s.title("The mechanical-energy ledger is a signed balance", "Illustrative values in joules: 10 J initial, 6 J final, 4 J transferred to thermal energy.")
    # Initial/final stacked columns.
    baseline=670; scale=35
    panel(s,55,155,390,560,"INITIAL")
    panel(s,505,155,390,560,"FINAL + THERMAL")
    panel(s,955,155,390,560,"SIGNED CHANGES")
    x=175; s.rect(x,baseline-6*scale,150,6*scale,RED,PALE_RED,2); s.rect(x,baseline-(6+4)*scale,150,4*scale,BLUE,PALE_BLUE,2)
    s.text(x+35,baseline-6*scale+55,"Kᵢ=6",17,WHITE,90); s.text(x+35,baseline-10*scale+25,"Uᵢ=4",17,INK,90); s.text(135,baseline+20,"Eᵢ=10 J",19,INK,150)
    x=625; s.rect(x,baseline-4*scale,150,4*scale,RED,PALE_RED,2); s.rect(x,baseline-(4+2)*scale,150,2*scale,BLUE,PALE_BLUE,2); s.rect(x,baseline-(4+2+4)*scale,150,4*scale,GREEN,PALE_GREEN,2)
    s.text(x+35,baseline-4*scale+32,"K_f=4",16,WHITE,90); s.text(x+35,baseline-6*scale+10,"U_f=2",15,INK,90); s.text(x+30,baseline-10*scale+30,"Q=4",17,INK,90); s.text(600,baseline+20,"E_f+Q=10 J",18,GREEN,220)
    # Signed changes below/next to a zero line.
    x0=1125; y0=405; s.line(1010,y0,1300,y0,INK,2)
    for xx,label in [(1060,"ΔK=−2"),(1160,"ΔU=−2")]:
        s.rect(xx,y0,65,70,RED,PALE_RED,2); s.text(xx-5,y0+80,label,14,RED,85)
    s.rect(1250,y0,65,140,ORANGE,PALE_ORANGE,2); s.text(1230,y0+150,"W_nc=−4",14,ORANGE,100)
    s.text(1010,260,"ΔK+ΔU=W_nc",20,PURPLE,250)
    s.text(1010,585,"Q=−W_nc=f_kd",18,GREEN,230)
    s.text(115,760,"Kᵢ+Uᵢ = K_f+U_f+Q",21,GREEN,390)
    return s


def d65() -> Scene:
    s=Scene("D6.5"); s.title("Read turning points and stability from U(x)", "For a chosen energy E, K=E−U is the vertical gap; motion is allowed only where E≥U.")
    ox,oy=150,610; s.arrow(ox,oy,1210,oy,INK,2); s.arrow(ox,oy,ox,190,INK,2)
    s.text(1215,oy-15,"x",16,INK,25); s.text(ox-25,175,"U",16,INK,25)
    # Potential well plus hill.
    pts=[(ox,440),(250,500),(350,555),(455,585),(550,565),(640,545),(735,530),(830,520),(920,525),(1020,470),(1130,440)]
    polyline(s,pts,BLUE,3.3)
    E_y=500; s.line(ox,E_y,1165,E_y,ORANGE,2.5,"dashed"); s.text(1130,E_y-28,"E",19,ORANGE,30)
    # Two turning points bound the allowed well; the E−U gap is kinetic energy.
    s.line(250,oy,965,oy,PALE_GREEN,9)
    for xroot,label in [(250,"x₁"),(965,"x₂")]:
        s.line(xroot,E_y,xroot,oy,GRID,1.2,"dashed"); s.dot(xroot,E_y,6,RED); s.text(xroot-16,oy+18,label,15,RED,35)
    s.dot(455,585,7,GREEN); s.text(385,635,"stable min",15,GREEN,95)
    s.dot(830,520,7,PURPLE); s.text(780,300,"unstable max",15,PURPLE,120)
    s.arrow(465,E_y,465,580,TEAL,2.5); s.text(480,530,"K=E−U",16,TEAL,100)
    s.text(430,690,"allowed: E≥U",17,GREEN,155)
    return s


def d66() -> Scene:
    s=Scene("D6.6"); s.title("A real spring departs from Hooke's law near its elastic limit", "Shown: restoring force during extension. The signed area is work done by the spring.")
    ox,oy=180,465; s.arrow(ox,oy,1220,oy,INK,2); s.arrow(ox,oy,ox,190,INK,2)
    s.text(1225,oy-15,"x",17,INK,25); s.text(ox-25,175,"F_s",17,INK,35)
    # Linear restoring segment and nonlinear softening thereafter, below the axis.
    linear=[(ox,oy),(360,oy+90),(540,oy+180)]
    polyline(s,linear,BLUE,3)
    nonlinear=[(540,oy+180),(650,oy+230),(770,oy+266),(890,oy+286)]
    polyline(s,nonlinear,TEAL,3)
    s.line(540,oy-5,540,oy+300,RED,2,"dashed"); s.text(550,oy+300,"elastic limit x_el",15,RED,145)
    # Signed (negative) work area for spring force over positive extension.
    s.line(360,oy,360,oy+90,GRID,1); s.line(540,oy,540,oy+180,GRID,1)
    s.line(365,oy+12,535,oy+12,"#f5e8cd",2); s.line(380,oy+40,520,oy+40,"#f5e8cd",2); s.line(410,oy+70,490,oy+70,"#f5e8cd",2)
    s.text(650,255,"near x=0: F_s=−kx",19,BLUE,230)
    s.text(650,315,"nonlinear: softening\nor stiffening",17,TEAL,210)
    s.text(660,555,"W_spring=∫F_s dx<0\nfor an extension",18,ORANGE,240)
    return s


def d67() -> Scene:
    s=Scene("D6.7"); s.title("Kinetic and potential energy trade off around a vertical circle", "Example: v_bottom²=6gR, U_bottom=0, so E=3mgR at all four positions.")
    positions=[("bottom",0,3,0),("right side",1,2,1),("top",2,1,2),("left side",3,2,1)]
    for i,(label,_,K,U) in enumerate(positions):
        x=80+i*325
        panel(s,x,165,285,550,label)
        # Circle position icon
        cx=x+142; cy=340; r=72; s.ellipse(cx-r,cy-r,2*r,2*r,GRID,"transparent",1.7); s.dot(cx,cy,3,INK)
        angles=[-90,0,90,180]; th=math.radians(angles[i]); p=(cx+r*math.cos(th),cy-r*math.sin(th)); s.dot(*p,7,BLUE)
        # stacked energy bars, each unit mgR has equal height.
        base=650; scale=55; bx=x+75; s.rect(bx,base-K*scale,62,K*scale,RED,PALE_RED,2)
        s.text(bx+5,base-K*scale+15,f"K={K}",14,INK,55)
        if U:
            s.rect(bx+70,base-U*scale,62,U*scale,BLUE,PALE_BLUE,2); s.text(bx+72,base-U*scale+10,f"U={U}",14,INK,58)
        else:
            s.text(bx+72,base-22,"U=0",14,BLUE,55)
        s.text(x+60,675,"K+U=3mgR",16,GREEN,170)
    s.text(110,755,"At equal heights, the side positions have equal K and equal U.",16,MUTED,660)
    return s


def d68() -> Scene:
    s=Scene("D6.8"); s.title("Escape energy and bound radial motion", "For a bound orbit, use the effective potential when angular momentum is nonzero.")
    panel(s,55,165,620,540,"GRAVITATIONAL U(r)")
    panel(s,725,165,620,540,"EFFECTIVE POTENTIAL U_eff(r)")
    # Left plot: U=-4/r, zero-energy escape threshold.
    ox,oy=145,580; s.arrow(ox,oy,620,oy,INK,1.7); s.arrow(ox,oy,ox,260,INK,1.7)
    pts=[]
    for i in range(41):
        r=1+7*i/40; U=-4/r; pts.append((ox+55*r,oy-25*U))
    polyline(s,pts,BLUE,3); s.line(ox,oy-3,615,oy-3,ORANGE,2,"dashed")
    s.text(160,280,"E=0: marginal escape",15,ORANGE,185); s.text(565,590,"r",14,INK,25)
    s.text(250,625,"U→0⁻ as r→∞",15,BLUE,150); s.text(115,240,"U",15,INK,25)
    xR=ox+55; yR=oy-25*(-4)
    s.line(xR,oy,xR,yR,GRID,1.2,"dashed"); s.dot(xR,yR,5,PURPLE); s.text(xR-8,oy+12,"R",14,PURPLE,25)
    s.text(175,470,"v_esc=√(2GM/R)",15,PURPLE,190)
    # Right plot: Ueff=1/r^2-4/r; E=-1 has two roots and a centrifugal wall.
    ox,oy=800,580; s.arrow(ox,oy,1300,oy,INK,1.7); s.arrow(ox,oy,ox,255,INK,1.7)
    pts=[]
    for i in range(61):
        r=0.165+(7.75-0.165)*i/60; U=1/r**2-4/r; pts.append((ox+58*r,oy-25*U))
    polyline(s,pts,GREEN,3); yE=oy-25*(-1); s.line(ox,yE,1290,yE,ORANGE,2,"dashed")
    s.text(1170,yE-25,"E<0",15,ORANGE,55)
    s.text(845,275,"U_eff→+∞ as r→0",14,GREEN,210)
    s.text(1055,320,"E≥0: escapes to ∞",14,MUTED,180); s.text(1055,343,"K∞≥0",14,MUTED,90)
    s.text(865,233,"U_eff=L²/(2mr²) − GMm/r",14,INK,335)
    r1,r2=2-math.sqrt(3),2+math.sqrt(3)
    for r,label,tx in [(r1,"r_min",740),(r2,"r_max",1025)]:
        x=ox+58*r; s.dot(x,yE,5,RED); s.line(x,yE,x,oy,GRID,1,"dashed"); s.text(tx,oy+12,label,13,RED,55)
    s.text(895,670,"two turning points",15,GREEN,160)
    return s


def d69() -> Scene:
    s=Scene("D6.9"); s.title("A moving wedge can do work through its normal force", "The block's ground-frame displacement includes the wedge translation, so it is not perpendicular to N.")
    # Slope down-right; block moves down-right relative to wedge; wedge translates right.
    s.line(155,330,710,650,INK,5); s.line(710,650,710,330,INK,5); s.line(710,650,1240,650,GRID,2)
    theta=math.atan2(320,555); p=(390,330+(390-155)*math.tan(theta)); block_h=70
    block_c=(p[0]+math.sin(theta)*block_h/2,p[1]-math.cos(theta)*block_h/2)
    s.rect(block_c[0]-65,block_c[1]-block_h/2,130,block_h,BLUE,PALE_BLUE,2,True,angle=theta)
    b=p; s.arrow(*p,p[0]+180,p[1]+104,ORANGE,3.5); s.text(500,565,"relative slide s",16,ORANGE,145)
    s.arrow(*p,p[0]+145,p[1],TEAL,3.5); s.text(485,425,"wedge shift x_w",16,TEAL,155)
    s.arrow(*p,p[0]+325,p[1]+104,GREEN,3.5); s.text(660,500,"ground Δr",16,GREEN,110)
    s.arrow(*p,p[0]+120,p[1]-205,PURPLE,3.5); s.text(520,285,"N ⟂ incline",17,PURPLE,125)
    s.text(825,300,"N·s=0",21,INK,110)
    s.text(825,350,"N·Δr=N·x_w",21,GREEN,190)
    s.text(825,410,"=N sinθ·x_w > 0",19,ORANGE,240)
    s.text(825,500,"The normal is perpendicular\nto relative sliding, not to the\nblock's ground-frame motion.",17,MUTED,390)
    return s


def d610() -> Scene:
    s=Scene("D6.10"); s.title("Ground displacement is the sum of wedge and relative motion", "With the slope down-right and wedge moving right, N has a positive horizontal component.")
    theta=math.atan2(360,720); o=(250,420); s_len=300; xw=220
    rel=(o[0]+s_len*math.cos(theta),o[1]+s_len*math.sin(theta)); wedge=(o[0]+xw,o[1]); ground=(rel[0]+xw,rel[1])
    # Triangular wedge, with the block aligned to and resting on its sloping face.
    s.line(130,360,850,720,INK,5); s.line(130,360,130,720,INK,4); s.line(130,720,850,720,INK,4)
    block_h=60; block_c=(o[0]+math.sin(theta)*block_h/2,o[1]-math.cos(theta)*block_h/2)
    s.rect(block_c[0]-55,block_c[1]-block_h/2,110,block_h,BLUE,PALE_BLUE,2,True,angle=theta); s.text(220,385,"block",16,INK,70)
    s.arrow(*o,*rel,ORANGE,3.5); s.text(350,660,"s down incline",17,ORANGE,145)
    s.arrow(*o,*wedge,TEAL,3.5); s.text(335,385,"x_w",17,TEAL,65)
    s.arrow(*o,*ground,GREEN,4); s.text(500,445,"Δr_ground=s+x_w",17,GREEN,180)
    s.line(*rel,*ground,MUTED,1.6,"dashed")
    s.arrow(*o,o[0]+120*math.sin(theta),o[1]-120*math.cos(theta),PURPLE,3.2); s.text(315,285,"N",19,PURPLE,35)
    s.line(o[0],o[1],o[0]+110,o[1],GRID,1.5); s.text(335,425,"θ",17,INK,30)
    panel(s,865,210,450,420,"NORMAL-FORCE WORK")
    s.text(900,290,"N·s=0",20,INK,170)
    s.text(900,345,"N·x_w=N sinθ·x_w",19,GREEN,340)
    s.text(900,415,"W_N=N sinθ x_w",23,PURPLE,320)
    s.text(900,495,"Positive here because both\nN_x and wedge motion point right.",16,MUTED,360)
    return s


def d611() -> Scene:
    s=Scene("D6.11"); s.title("Lifting a chain needs weight support and momentum flux", "At constant upward speed v, each incoming link is accelerated from rest to v.")
    # Coiled chain and rising segment.
    s.line(150,670,1250,670,INK,3); s.ellipse(200,590,210,90,ORANGE,PALE_ORANGE,2)
    s.line(305,590,305,270,TEAL,5); s.rect(250,220,110,55,BLUE,PALE_BLUE,2,True)
    s.arrow(410,520,410,300,BLUE,3.4); s.text(425,370,"v upward",17,BLUE,110)
    s.arrow(520,520,520,620,RED,3); s.text(535,555,"λxg",17,RED,75)
    s.arrow(640,595,640,485,ORANGE,3); s.text(655,515,"λv²",17,ORANGE,75)
    s.text(200,710,"lifted length x=vt",18,INK,190)
    panel(s,775,205,540,430,"REQUIRED PULL")
    s.text(810,295,"F=λxg+λv²",26,GREEN,320)
    s.text(810,365,"weight of moving part",16,RED,250)
    s.text(810,415,"+ momentum rate: (λv)v",16,ORANGE,280)
    s.text(810,485,"At t=0, F=λv²; later the\nlifted weight λxg also grows.",16,MUTED,420)
    return s


def d612() -> Scene:
    s=Scene("D6.12"); s.title("Friction transfers mechanical energy into thermal energy", "Illustrative ledger: E_i=10 J; E_f=6 J; Q=f_kd=4 J.")
    baseline=670; scale=36; cols=[(180,"INITIAL",[("K_i=6",6,RED),("U_i=4",4,BLUE)]),(560,"FINAL MECHANICAL",[("K_f=4",4,RED),("U_f=2",2,BLUE)]),(960,"THERMAL",[("Q=4",4,GREEN)])]
    for x,label,bars in cols:
        panel(s,x-40,170,320,535,label); y=baseline
        for text,val,col in bars:
            h=val*scale; s.rect(x,y-h,125,h,col,PALE_RED if col==RED else PALE_BLUE if col==BLUE else PALE_GREEN,2)
            s.text(x+10,y-h+max(8,h/2-10),text,16,INK,110); y-=h
    s.text(85,740,"K_i+U_i = K_f+U_f+Q = 10 J",22,GREEN,560)
    s.text(700,740,"Q=f_kd=−W_friction",19,ORANGE,330)
    return s


def d71() -> Scene:
    s=Scene("D7.1"); s.title("Centres of mass of standard uniform bodies", "Distances are measured from the indicated reference surface or line.")
    # Rod.
    panel(s,45,145,245,570,"ROD")
    s.line(95,390,240,390,INK,8); s.dot(168,390,7,RED); s.line(95,430,240,430,GRID,1)
    s.text(75,485,"COM: L/2 from either end",15,INK,200)
    # Triangle centroid from base.
    panel(s,315,145,245,570,"TRIANGLE")
    tri=[(370,455),(505,455),(445,250),(370,455)]; polyline(s,tri,BLUE,3)
    s.dot(440,387,7,RED); s.line(440,455,440,387,RED,2,"dashed"); s.text(350,500,"COM: h/3 from base",15,INK,190)
    # Semicircular ring.
    panel(s,585,145,245,570,"SEMICIRCULAR RING")
    c=(705,455); r=85; arc=[(c[0]+r*math.cos(math.pi*i/20),c[1]-r*math.sin(math.pi*i/20)) for i in range(21)]
    polyline(s,arc,TEAL,3); s.line(c[0]-r,c[1],c[0]+r,c[1],INK,2); s.dot(c[0],c[1]-2*r/math.pi,7,RED)
    s.text(610,500,"COM: 2R/π from diameter",14,INK,195)
    # Semicircular lamina.
    panel(s,855,145,245,570,"SEMICIRCULAR DISC")
    c=(975,455); r=85; arc=[(c[0]+r*math.cos(math.pi*i/20),c[1]-r*math.sin(math.pi*i/20)) for i in range(21)]
    polyline(s,arc,BLUE,3); s.line(c[0]-r,c[1],c[0]+r,c[1],INK,2); s.dot(c[0],c[1]-4*r/(3*math.pi),7,RED)
    s.text(875,500,"COM: 4R/(3π) from diameter",14,INK,205)
    # Solid cone.
    panel(s,1125,145,245,570,"SOLID CONE")
    s.line(1175,465,1235,250,BLUE,3); s.line(1235,250,1300,465,BLUE,3); s.ellipse(1175,440,125,50,BLUE,"transparent",2)
    s.dot(1235,411,7,RED); s.line(1235,411,1235,455,RED,1.6,"dashed"); s.text(1145,520,"COM: h/4 from base",15,INK,190)
    return s


def d72() -> Scene:
    s=Scene("D7.2"); s.title("A hole is a negative-mass contribution", "Uniform plate: offset hole of radius r and centre d; the composite COM shifts away from the hole.")
    cx,cy,R=430,470,185; r=128; d=42
    s.ellipse(cx-R,cy-R,2*R,2*R,BLUE,PALE_BLUE,3); s.dot(cx,cy,6,INK); s.text(cx-18,cy+22,"O",15,INK,25)
    s.ellipse(cx+d-r,cy-r,2*r,2*r,RED,WHITE,3); s.dot(cx+d,cy,5,RED)
    s.text(cx+d-30,cy-20,"−M₂",17,RED,70); s.text(cx+95,cy-45,"hole centre d",14,RED,120)
    xcm=cx-(r*r*d)/(R*R-r*r); s.dot(xcm,cy,8,GREEN); s.text(xcm-85,cy+25,"composite COM",15,GREEN,135)
    s.line(cx,cy+48,cx+d,cy+48,ORANGE,2); s.text(cx+8,cy+55,"d",16,ORANGE,25)
    panel(s,790,205,535,430,"SIGNED-MASS BOOKKEEPING")
    s.text(825,290,"M_total=M₁−M₂",23,INK,330)
    s.text(825,355,"x_cm=(M₁·0−M₂d)/(M₁−M₂)",20,GREEN,440)
    s.text(825,430,"=−M₂d/(M₁−M₂)<0",21,GREEN,360)
    s.text(825,510,"The COM moves opposite the\nhole's displacement from O.",17,MUTED,390)
    return s


def d73() -> Scene:
    s=Scene("D7.3"); s.title("An explosion cannot deflect the centre of mass", "If only gravity acts externally, the fragments' COM follows the original projectile parabola.")
    ox,oy=140,670; sx=48; sy=42
    s.arrow(ox,oy,1280,oy,INK,2); s.arrow(ox,oy,ox,180,INK,2)
    pts=[]
    for i in range(41):
        t=4*i/40; x=5*t; y=8*t-2*t*t; pts.append((ox+x*sx,oy-y*sy))
    polyline(s,pts,BLUE,3,"dashed")
    t=2; px=ox+5*t*sx; py=oy-(8*t-2*t*t)*sy
    s.dot(px,py,9,ORANGE); s.text(px-55,py-35,"explosion",16,ORANGE,100)
    # Fragments diverge, while their mass-weighted centre remains at the event point.
    s.arrow(px,py,px-150,py-115,RED,3.2); s.arrow(px,py,px+155,py-40,TEAL,3.2); s.arrow(px,py,px+35,py+125,PURPLE,3.2)
    s.dot(px,py,7,GREEN); s.text(px+15,py+12,"COM",16,GREEN,50)
    s.text(780,245,"ΣF_ext=M a_COM",22,GREEN,270)
    s.text(780,300,"Internal explosion forces cancel\nin the system momentum balance.",17,MUTED,400)
    s.text(230,720,"dashed path = pre- and post-explosion COM trajectory",16,BLUE,470)
    return s


def d74() -> Scene:
    s=Scene("D7.4"); s.title("Impulse is signed area under the force–time curve", "A triangular pulse with F_max=10 N over Δt=2 s has J=10 N·s and average force 5 N.")
    ox,oy=190,650; sx=230; sy=35
    s.arrow(ox,oy,ox+2.8*sx,oy,INK,2); s.arrow(ox,oy,ox,oy-12*sy,INK,2)
    s.text(ox+2.8*sx+5,oy-15,"t (s)",16,INK,65); s.text(ox-55,oy-12*sy-20,"F (N)",16,INK,75)
    s.line(ox+2*sx,oy,ox+2*sx,oy-5*sy,TEAL,2,"dashed")
    s.line(ox,oy,ox+sx,oy-10*sy,BLUE,3.5); s.line(ox+sx,oy-10*sy,ox+2*sx,oy,BLUE,3.5)
    # Same-area rectangle for average force.
    s.line(ox,oy-5*sy,ox+2*sx,oy-5*sy,ORANGE,2.5,"dashed"); s.text(ox+2*sx+12,oy-5*sy-12,"F̄=5 N",16,ORANGE,90)
    s.line(ox,oy,ox+2*sx,oy,GRID,1)
    for t in [0,1,2]: s.text(ox+t*sx-8,oy+12,str(t),13,MUTED,20)
    s.text(450,330,"J=½(2 s)(10 N)=10 N·s",20,GREEN,330)
    s.text(450,380,"J=F̄Δt",18,ORANGE,140)
    return s


def d75() -> Scene:
    s=Scene("D7.5"); s.title("Collision class is set by restitution", "Equal masses; m₁ approaches a stationary m₂ with speed u.")
    cases=[("ELASTIC · e=1",BLUE,0),("INELASTIC · 0<e<1",ORANGE,1),("PERFECTLY INELASTIC · e=0",GREEN,2)]
    for i,(heading,col,case) in enumerate(cases):
        x=55+i*445; panel(s,x,165,410,570,heading)
        s.text(x+25,235,"BEFORE",14,MUTED,75); s.dot(x+140,285,20,BLUE); s.dot(x+280,285,20,TEAL)
        s.arrow(x+140,325,x+240,325,BLUE,3); s.text(x+160,340,"u",15,BLUE,30)
        s.text(x+300,270,"0",14,MUTED,25)
        if case==0:
            s.text(x+25,425,"AFTER",14,MUTED,75); s.dot(x+140,485,20,BLUE); s.dot(x+280,485,20,TEAL)
            s.text(x+125,515,"0",15,MUTED,25); s.arrow(x+280,525,x+390,525,TEAL,3); s.text(x+300,540,"u",15,TEAL,30)
            s.text(x+55,635,"relative speed restored",16,GREEN,260)
        elif case==1:
            s.text(x+25,425,"AFTER",14,MUTED,75); s.dot(x+140,485,20,BLUE); s.dot(x+280,485,20,TEAL)
            s.arrow(x+140,525,x+205,525,BLUE,3); s.arrow(x+280,525,x+380,525,TEAL,3)
            s.text(x+65,600,"v₁=(1−e)u/2",15,BLUE,145); s.text(x+225,630,"v₂=(1+e)u/2",15,TEAL,150)
        else:
            s.text(x+25,425,"AFTER",14,MUTED,75); s.ellipse(x+175,455,85,60,GREEN,PALE_GREEN,2); s.text(x+195,472,"m₁+m₂",15,INK,75)
            s.arrow(x+260,525,x+360,525,GREEN,3); s.text(x+275,540,"u/2",15,GREEN,45)
            s.text(x+60,635,"they move together",16,GREEN,220)
    return s


def d76() -> Scene:
    s=Scene("D7.6"); s.title("For equal masses, final velocities are linear in restitution e", "m₁ starts at u₁; m₂ is at rest. v₁=(1−e)u₁/2 and v₂=(1+e)u₁/2.")
    ox,oy=220,660; sx=800; sy=300
    s.arrow(ox,oy,ox+sx+60,oy,INK,2); s.arrow(ox,oy,ox,oy-sy-30,INK,2)
    s.text(ox+sx+65,oy-15,"e",16,INK,25); s.text(ox-60,oy-sy-35,"v/u₁",16,INK,65)
    s.line(ox,oy-sy,ox+sx,oy,BLUE,3); s.line(ox,oy-sy/2,ox+sx,oy-sy,TEAL,3)
    s.dot(ox,oy-sy/2,6,PURPLE); s.dot(ox+sx,oy,6,BLUE); s.dot(ox+sx,oy-sy,6,TEAL)
    s.text(ox+sx+10,oy-10,"v₁=0",15,BLUE,80); s.text(ox+sx+10,oy-sy,"v₂=u₁",15,TEAL,85)
    s.text(ox+sx/2-80,oy-sy/2-25,"e=0: v₁=v₂=u₁/2",16,PURPLE,220)
    s.text(450,265,"v₂/u₁=(1+e)/2",19,TEAL,200); s.text(770,570,"v₁/u₁=(1−e)/2",19,BLUE,200)
    s.text(230,710,"e=0 perfectly inelastic",14,MUTED,190); s.text(930,710,"e=1 elastic",14,MUTED,110)
    return s


def d77() -> Scene:
    s=Scene("D7.7"); s.title("In an oblique collision, only the line-of-impact components change", "Smooth spheres: tangential components are unchanged; normal components obey momentum and restitution.")
    # Two spheres at contact, horizontal line of centres.
    s.ellipse(350,380,180,180,BLUE,PALE_BLUE,3); s.ellipse(530,380,180,180,TEAL,PALE_TEAL,3)
    s.line(440,470,620,470,PURPLE,2,"dashed"); s.text(455,445,"line of impact n̂",15,PURPLE,175)
    s.line(530,330,530,610,ORANGE,2,"dashed"); s.text(545,340,"tangent t̂",15,ORANGE,105)
    # Incoming velocity of first sphere has normal and tangential pieces; second is at rest.
    s.arrow(440,470,530,375,BLUE,3.4); s.text(445,340,"v₁ before",15,BLUE,100)
    s.arrow(440,470,530,470,PURPLE,2.7); s.text(485,480,"v₁n",14,PURPLE,50)
    s.arrow(440,470,440,375,ORANGE,2.7); s.text(445,380,"v₁t",14,ORANGE,50)
    s.text(770,250,"After contact · components",18,INK,240)
    s.arrow(825,455,825,350,BLUE,3.2); s.text(845,385,"v₁t unchanged",15,BLUE,150)
    s.arrow(825,490,945,490,BLUE,3.2); s.text(830,500,"v₁n′",14,BLUE,55)
    s.arrow(825,550,960,550,TEAL,3.2); s.text(830,560,"v₂n′",14,TEAL,55)
    s.text(770,605,"e=−(v₂n−v₁n)/(u₂n−u₁n)",17,GREEN,330)
    s.text(770,655,"Impulse is along n̂; smooth contact\nprovides no tangential impulse.",15,MUTED,400)
    return s


def d78() -> Scene:
    s=Scene("D7.8"); s.title("Rocket momentum balances rocket plus expelled mass", "Over dt, dm<0; exhaust is ejected backward relative to the rocket (shown with vₑ>v).")
    panel(s,55,165,600,520,"AT TIME t")
    panel(s,745,165,600,520,"AT TIME t+dt")
    # Rocket icons.
    s.rect(180,360,300,115,BLUE,PALE_BLUE,3,True); s.text(280,400,"rocket · mass m",20,INK,200)
    s.arrow(480,420,590,420,BLUE,3.5); s.text(505,385,"v",18,BLUE,35)
    s.rect(845,360,300,115,BLUE,PALE_BLUE,3,True); s.text(925,400,"mass m+dm",20,INK,190)
    s.arrow(1145,420,1250,420,BLUE,3.5); s.text(1160,385,"v+dv",17,BLUE,75)
    s.arrow(845,500,755,500,ORANGE,3.5); s.text(750,520,"−dm>0 exhaust",16,ORANGE,150)
    s.arrow(845,565,740,565,RED,3); s.text(745,580,"lab velocity v−vₑ",15,RED,160)
    s.text(90,610,"p_before=mv",19,INK,185)
    s.text(785,630,"p_after=(m+dm)(v+dv)+(−dm)(v−vₑ)",17,INK,480)
    s.text(300,735,"Momentum conservation (no external impulse) yields the rocket equation.",17,GREEN,820)
    return s


def d79() -> Scene:
    s=Scene("D7.9"); s.title("The centre-of-mass frame removes total momentum", "Equal masses: in the lab, m₁ moves at u and m₂ is at rest; the CM moves at u/2.")
    panel(s,55,155,620,580,"LAB FRAME")
    panel(s,725,155,620,580,"CENTRE-OF-MASS FRAME")
    # Before.
    s.text(95,245,"BEFORE",15,MUTED,80); s.dot(180,325,24,BLUE); s.dot(420,325,24,TEAL); s.arrow(180,380,320,380,BLUE,3.5); s.text(235,390,"u",17,BLUE,35); s.text(425,310,"at rest",14,MUTED,75)
    s.text(95,500,"ELASTIC AFTER",15,MUTED,130); s.dot(180,585,24,BLUE); s.dot(420,585,24,TEAL); s.text(155,625,"0",15,MUTED,20); s.arrow(420,640,560,640,TEAL,3.5); s.text(465,650,"u",17,TEAL,35)
    # CM frame arrows are equal/opposite before and after.
    s.text(765,245,"BEFORE: p₁+p₂=0",15,MUTED,200); s.dot(870,325,24,BLUE); s.dot(1130,325,24,TEAL)
    s.arrow(870,380,980,380,BLUE,3.5); s.arrow(1130,380,1020,380,TEAL,3.5); s.text(900,395,"+u/2",15,BLUE,65); s.text(1045,395,"−u/2",15,TEAL,65)
    s.text(765,500,"AFTER: momenta still cancel",15,MUTED,230); s.dot(870,585,24,BLUE); s.dot(1130,585,24,TEAL)
    s.arrow(870,640,760,640,BLUE,3.5); s.arrow(1130,640,1240,640,TEAL,3.5)
    s.text(780,690,"CM frame: P_total=0 before and after",16,GREEN,380)
    return s


def d710() -> Scene:
    s=Scene("D7.10"); s.title("A falling chain doubles the scale reading at full impact", "Let x be the still-falling length; v²=2gx after falling distance x.")
    s.rect(850,620,400,60,INK,PALE_TEAL,3); s.text(980,685,"scale",17,INK,80)
    # Chain hanging and landed pile.
    for y in range(190,610,24): s.line(1050,y,1050,y+12,ORANGE,4)
    s.ellipse(920,580,260,40,ORANGE,PALE_ORANGE,2)
    s.text(1090,345,"length x\nstill falling",16,ORANGE,130)
    s.arrow(1145,235,1145,385,BLUE,3.4); s.text(1160,295,"v=√(2gx)",16,BLUE,130)
    # Force components on the scale.
    s.arrow(760,500,760,610,RED,3.5); s.text(605,530,"weight: λ(L−x)g",16,RED,155)
    s.arrow(1320,490,1320,610,ORANGE,3.5); s.text(1120,465,"impact: λv²=2λgx",16,ORANGE,190)
    panel(s,85,205,500,430,"SCALE READING")
    s.text(120,295,"F=λ(L−x)g+λv²",22,GREEN,395)
    s.text(120,355,"=λ(L+x)g",25,GREEN,280)
    s.text(120,445,"At x=L: F=2λLg=2mg",20,INK,360)
    s.text(120,520,"Weight of landed links +\nrate of momentum delivered.",16,MUTED,380)
    return s


def d711() -> Scene:
    s=Scene("D7.11"); s.title("A ballistic pendulum has an inelastic impact followed by an energy-conserving swing", "Momentum applies during the short embedding collision; mechanical energy applies during the later rise.")
    panel(s,55,165,620,535,"1 · COLLISION")
    panel(s,725,165,620,535,"2 · SWING")
    # Bullet and block.
    s.rect(410,420,155,110,BLUE,PALE_BLUE,3,True); s.text(455,455,"M",26,INK,45)
    s.arrow(130,475,390,475,RED,3.8); s.text(220,435,"bullet m at u",17,RED,135)
    s.text(100,590,"before: p=mu",18,INK,155); s.text(100,630,"after embed: V=mu/(M+m)",17,GREEN,300)
    # Pendulum after impact.
    ox,oy=1010,295; bob=(1185,490)
    s.line(ox,oy,bob[0],bob[1],INK,3); s.ellipse(bob[0]-60,bob[1]-45,120,90,GREEN,PALE_GREEN,3)
    s.arrow(bob[0],bob[1],bob[0]+125,bob[1]-105,BLUE,3.4); s.text(1190,345,"V",17,BLUE,30)
    bottom_y=oy+math.hypot(bob[0]-ox,bob[1]-oy)
    s.line(ox,oy,ox,bottom_y,GRID,1.5,"dashed"); s.line(bob[0],bob[1],1275,bob[1],GRID,1.2,"dashed")
    s.line(ox,bottom_y,bob[0],bottom_y,GRID,1.2,"dashed"); s.arrow(1275,bottom_y,1275,bob[1],PURPLE,2.5,start="arrow",end="arrow"); s.text(1290,(bottom_y+bob[1])/2,"h",16,PURPLE,25)
    s.text(785,590,"½(M+m)V²=(M+m)gh",19,GREEN,350)
    s.text(785,645,"energy conserved during swing",15,MUTED,290)
    return s


def d712() -> Scene:
    s=Scene("D7.12"); s.title("With no horizontal external force, the man–boat COM stays fixed", "Illustration with boat mass M=2m: for relative walk d, the boat shifts −d/3 and the man +2d/3.")
    panel(s,55,165,610,560,"INITIAL")
    panel(s,725,165,610,560,"AFTER WALKING")
    s.line(95,610,605,610,TEAL,3); s.line(765,610,1275,610,TEAL,3)
    # Initial local coordinates: boat centre 285, man centre 266, COM 279.
    s.rect(165,500,350,60,BLUE,PALE_BLUE,3,True); s.text(270,520,"boat M=2m",16,INK,120)
    s.ellipse(295,395,52,52,ORANGE,PALE_ORANGE,2); s.line(321,447,321,500,ORANGE,4); s.text(275,370,"man m",14,ORANGE,75)
    s.line(334,300,334,675,PURPLE,2,"dashed"); s.text(338,300,"X_cm",15,PURPLE,65)
    # Final local coordinates: boat centre moves 40 px left; man moves 80 px right.
    s.rect(795,500,350,60,BLUE,PALE_BLUE,3,True); s.text(900,520,"boat M=2m",16,INK,120)
    s.ellipse(1045,395,52,52,ORANGE,PALE_ORANGE,2); s.line(1071,447,1071,500,ORANGE,4); s.text(1045,370,"man m",14,ORANGE,75)
    s.line(1004,300,1004,675,PURPLE,2,"dashed"); s.text(1008,300,"same X_cm",15,PURPLE,100)
    # Ghost initial position within the final frame makes the relative walk clear.
    s.ellipse(930,410,42,42,GRID,"transparent",1.5); s.line(951,452,951,500,GRID,2,"dashed")
    s.arrow(970,460,1060,460,ORANGE,3); s.text(985,430,"d_rel right",14,ORANGE,100)
    s.arrow(965,580,925,580,BLUE,3); s.text(895,585,"boat shift left",14,BLUE,100)
    s.text(95,750,"d_boat=−d/3; d_man=+2d/3; X_cm=(m x_man+M x_boat)/(m+M)=constant",18,GREEN,1120)
    return s

BUILDERS = [
    ("units-measurements", "D1.1", "The seven SI base units and their modern definitions", d11),
    ("units-measurements", "D1.2", "The principle of homogeneity as a balance", d12),
    ("units-measurements", "D1.3", "The fractional-error table method", d13),
    ("units-measurements", "D1.4", "Dimensional derivation of the pendulum period", d14),
    ("units-measurements", "D1.5", "The significant-figure rules visualised", d15),
    ("units-measurements", "D1.6", "Catastrophic cancellation: subtracting nearly equal numbers", d16),
    ("units-measurements", "D1.7", "The standard error of the mean vs number of measurements", d17),
    ("units-measurements", "D1.8", "The three error types on a target", d18),
    ("units-measurements", "D1.9", "Error propagation: the product rule", d19),
    ("units-measurements", "D1.10", "The vernier caliper reading", d110),
    ("units-measurements", "D1.11", "The screw gauge with zero error", d111),
    ("units-measurements", "D1.12", "Linearisation of T² vs L for a pendulum", d112),
    ("vectors", "D2.1", "The difference between a vector and a scalar", d21),
    ("vectors", "D2.2", "The triangle and parallelogram laws", d22),
    ("vectors", "D2.3", "Components of a vector in 2D", d23),
    ("vectors", "D2.4", "The dot product as projection", d24),
    ("vectors", "D2.5", "The cross product and the right-hand rule", d25),
    ("vectors", "D2.6", "The scalar triple product as volume", d26),
    ("vectors", "D2.7", "Solving a × x = b", d27),
    ("vectors", "D2.8", "The polar basis and its rotation", d28),
    ("vectors", "D2.9", "The scalar triple product as a signed volume", d29),
    ("vectors", "D2.10", "Vector addition in components", d210),
    ("vectors", "D2.11", "The projection of a vector onto another", d211),
    ("vectors", "D2.12", "Anti-commutativity of the cross product", d212),
    ("kinematics-1d", "D3.1", "Position vs displacement vs distance", d31),
    ("kinematics-1d", "D3.2", "Instantaneous velocity as the tangent slope", d32),
    ("kinematics-1d", "D3.3", "Acceleration and the three graphs", d33),
    ("kinematics-1d", "D3.5", "Deriving the equations from the v-t graph", d35),
    ("kinematics-1d", "D3.7", "The v dv/dx method", d37),
    ("kinematics-1d", "D3.8", "Relative velocity in 1-D", d38),
    ("kinematics-1d", "D3.9", "Piecewise kinematics on a v-t graph", d39),
    ("kinematics-1d", "D3.10", "The nth-second distance", d310),
    ("kinematics-1d", "D3.11", "Relative velocity: two particles approaching", d311),
    ("motion-in-two-dimensions", "D4.1", "Horizontal motion and vertical fall", d41),
    ("motion-in-two-dimensions", "D4.2", "Oblique projectile motion", d42),
    ("motion-in-two-dimensions", "D4.3", "Complementary projectile angles", d43),
    ("motion-in-two-dimensions", "D4.4", "Projectile launched from a height", d44),
    ("motion-in-two-dimensions", "D4.5", "Rain and observer relative velocity", d45),
    ("motion-in-two-dimensions", "D4.6", "Angular velocity and tangential speed", d46),
    ("motion-in-two-dimensions", "D4.7", "Geometric derivation of centripetal acceleration", d47),
    ("motion-in-two-dimensions", "D4.8", "Radial and tangential acceleration", d48),
    ("motion-in-two-dimensions", "D4.9", "Projectile on an inclined plane", d49),
    ("motion-in-two-dimensions", "D4.10", "River crossing and ground-frame velocity", d410),
    ("motion-in-two-dimensions", "D4.11", "Projectile safety parabola", d411),
    ("motion-in-two-dimensions", "D4.12", "Acceleration vector in non-uniform circular motion", d412),
    ("newtons-laws", "D5.1", "Inertial and accelerating frames", d51),
    ("newtons-laws", "D5.2", "Newton's third-law pairs", d52),
    ("newtons-laws", "D5.3", "Incline free-body diagram and components", d53),
    ("newtons-laws", "D5.4", "Apparent weight in an elevator", d54),
    ("newtons-laws", "D5.5", "Static and kinetic friction graph", d55),
    ("newtons-laws", "D5.6", "Two blocks and the no-slip limit", d56),
    ("newtons-laws", "D5.7", "Movable-pulley constraint", d57),
    ("newtons-laws", "D5.8", "Friction on a banked road", d58),
    ("newtons-laws", "D5.9", "Vertical-circle tension and speed", d59),
    ("newtons-laws", "D5.10", "Wedge and block displacement constraint", d510),
    ("newtons-laws", "D5.11", "Forces at four positions in a vertical circle", d511),
    ("newtons-laws", "D5.12", "Two-pulley string constraint", d512),
    ("work-energy-power", "D6.1", "Work sign in six cases", d61),
    ("work-energy-power", "D6.2", "Work as signed area under a force curve", d62),
    ("work-energy-power", "D6.3", "Power-limited top speed", d63),
    ("work-energy-power", "D6.4", "Mechanical-energy ledger and non-conservative work", d64),
    ("work-energy-power", "D6.5", "Potential-energy landscape and turning points", d65),
    ("work-energy-power", "D6.6", "Nonlinear spring force and signed work", d66),
    ("work-energy-power", "D6.7", "Energy split around a vertical circle", d67),
    ("work-energy-power", "D6.8", "Gravitational escape and effective potential", d68),
    ("work-energy-power", "D6.9", "Normal-force work on a block and wedge", d69),
    ("work-energy-power", "D6.10", "Wedge displacement and normal-force work", d610),
    ("work-energy-power", "D6.11", "Lifting a chain at constant speed", d611),
    ("work-energy-power", "D6.12", "Thermal energy in a friction ledger", d612),
    ("centre-of-mass-momentum", "D7.1", "Centres of mass of standard bodies", d71),
    ("centre-of-mass-momentum", "D7.2", "Negative-mass method for a hole", d72),
    ("centre-of-mass-momentum", "D7.3", "Centre of mass after an explosion", d73),
    ("centre-of-mass-momentum", "D7.4", "Impulse as area under a force-time curve", d74),
    ("centre-of-mass-momentum", "D7.5", "Elastic, inelastic and perfectly inelastic collisions", d75),
    ("centre-of-mass-momentum", "D7.6", "Final velocities as functions of restitution", d76),
    ("centre-of-mass-momentum", "D7.7", "Components in an oblique collision", d77),
    ("centre-of-mass-momentum", "D7.8", "Rocket momentum ledger", d78),
    ("centre-of-mass-momentum", "D7.9", "Lab and centre-of-mass frames", d79),
    ("centre-of-mass-momentum", "D7.10", "Falling chain force on a scale", d710),
    ("centre-of-mass-momentum", "D7.11", "Ballistic-pendulum stages", d711),
    ("centre-of-mass-momentum", "D7.12", "Man walking on a boat and fixed centre of mass", d712),
]


def main() -> None:
    for topic_slug, diagram_id, title, builder in BUILDERS:
        slug, path = scene_file(topic_slug, diagram_id, title, builder())
        print(f"{diagram_id}: {path}")
    print(f"\nGenerated {len(BUILDERS)} Excalidraw scenes in {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
