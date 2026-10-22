# -*- coding: utf-8 -*-
"""Author the complete COM & collisions short notes (source: centre-of-mass-momentum/Centre-of-mass-momentum.md)."""
import json, math

HEAD = dict(color='navy', bg='#e8f4f8', accent='#1f6f8b')
WHY = dict(color='teal', bg='#e6f7f4', accent='#148f77')
CHK = dict(color='teal', bg='#e6f7f4', accent='#148f77')
WARN = dict(color='red', bg='#fdecea', accent='#c0392b')
CH = dict(color='yellow', bg='#fff8e1', accent='#b7950b')
FN = dict(color='navy', bg='#f0f8ff', accent='#1f6f8b')
_K = 2 * math.pi / 0.7
SN = ['CM']
JN = ['OLY']
for _i in range(1, 25):
    SN.append('CM-%02d' % _i)
for _i in range(1, 12):
    JN.append('OLY-%02d' % _i)


def CX(level, theme, title, items):
    return dict(level=level, theme=theme, title=title, items=items)


def CHUNK(chunk):
    bad = [it for it in chunk if isinstance(it, tuple) and len(it) == 2 and it[0] == 'D']
    assert len(bad) <= 2, chunk[0]['title']
    assert len(chunk) == 4, chunk[0]['title']
    assert chunk[0]['level'] == 'h2'
    for c in chunk:
        for it in c['items']:
            if isinstance(it, tuple):
                assert it[0] in ('WHY', 'CHECK', 'FN', 'D'), (c['title'], it[0])
                if it[0] == 'D':
                    assert isinstance(it[1], str)
            else:
                assert isinstance(it, str) and it.strip()
                assert len(it) <= 3200, (c['title'], len(it))
                assert it.count('\\n') <= 3, (c['title'], it.count('\\n'))
    out = list(chunk)
    for c, it in zip(out, chunk):
        body = [x for x in c['items'] if isinstance(x, str)]
        text = '\\n'.join(body)
        for tgt in (c, it):
            if isinstance(tgt, dict):
                tgt['_used'] = max(tgt.get('_used', 0), len(text) / (520 * int(c['level'][-1])))
    return out


def DES(t, *ts):
    return [CX('h3', HEAD, t, list(ts))]


def DH(t, *ts):
    return [CX('h4', CH, t, list(ts))]


def TEA(t, *ts):
    return [CX('h5', WARN, t, list(ts))]


COM = []


def ADD(slug, cards, summary):
    assert slug in SN or slug in JN, slug
    COM.append(dict(sheet=slug, summary=summary, cards=cards))


# ---------------------------------------------------- CM-01 what the centre of mass is
ADD('CM-01', CHUNK([
    CX('h2', HEAD, "The centre of mass: the mass-weighted average position",
       ["For $n$ particles the centre of mass (COM) is $\\mathbf{R} = \\dfrac{1}{M}\\sum_{i=1}^{n} m_i \\mathbf{r}_i$ with $M = \\sum m_i$. Component form: $X_{cm} = \\sum m_i x_i / M$, $Y_{cm} = \\sum m_i y_i / M$.",
          "For a continuous body $\\mathbf{R} = \\frac{1}{M}\\int \\mathbf{r}\\,dm$, integrated over the body with $dm = \\rho\\,dV$ (or $\\lambda\\,dl$, $\\sigma\\,dA$ for line/surface mass). The COM is unique, independent of the coordinate origin (shift both sides of the definition and $\\mathbf{R}$ shifts with them), and transforms like a position vector. Always pick the origin so that symmetry kills one or both integrals before integrating.",
          "Worked habits: place the origin ON a symmetry axis; use the standard-bodies table below as building blocks; cut composite bodies into pieces with known COMs and average those. For a body with a hole, the fastest route is negative mass (CM-02).",
          ("WHY", "the COM is the one point whose motion answers to external forces alone - it is the reduction of a complicated system to one particle for the purpose of the momentum ledger (CM-03).")]),
     CX('h3', HEAD, "Physical meaning and symmetry shortcuts",
       ["Physical meaning: $\\mathbf{R}$ is the point whose motion answers to external forces alone (CM-03). For any system at all - a gas cloud, a gymnast mid-flight, an exploded shell - the mass-weighted mean position is the one point whose trajectory is simple. The COM may lie in empty space: for a uniform ring it is at the centre, for a boomerang it may be off the body entirely. Nothing requires mass to exist at the COM. Symmetry shortcuts: an axis of symmetry forces the COM onto that axis; two symmetry axes force it to their intersection; a plane of symmetry forces it into that plane. A uniform body with a centre of symmetry has its COM at that centre.",
          "Discrete systems: $X_{cm} = (m_1x_1 + m_2x_2 + \\cdots)/M$. Two masses $m_1, m_2$ at separation $d$: the COM divides the line joining them in the RATIO $m_2 : m_1$ - it sits closer to the heavier mass. Composite bodies: cut into pieces with known COMs and average.",
          "Trap: the COM of a body is NOT necessarily inside it; and it is not the geometric centre unless the body is uniform AND symmetric. A ring with a bead glued on has its COM pulled toward the bead; shift to the negative-mass picture the moment a cut appears (CM-02).",
          ("CHECK", "centroid by vertices: triangle $(0,0), (b,0), (0,h)$ has centroid $(b/3, h/3)$; the distance from the base is $h/3$ and from the $x = 0$ side it is $b/3$ - the medians rule. Four equal masses at the corners of a square give the square centre.")]),
     CX('h3', CH, "Standard shapes table (memorise; each is a two-line integral to re-derive)",
       ["Standard results (memorise; each is a two-line integral to re-derive): uniform rod length $L$: midpoint, $L/2$ from either end. Uniform triangle: the centroid, intersection of the medians, at distance $h/3$ from any side (i.e. one-third of the altitude from each base). Semicircular ring of radius $R$: $y_{cm} = 2R/\\pi \\approx 0.637R$ from the diameter. Semicircular disc: $y_{cm} = 4R/(3\\pi) \\approx 0.424R$ from the diameter. Solid hemisphere: $3R/8 = 0.375R$ from the flat face. Hollow hemisphere (shell): $R/2$ from the flat face. Solid cone of height $h$: $h/4$ from the base (i.e. $3h/4$ from the apex). Uniform circular arc subtending angle $\\theta$ at the centre: $x_{cm} = R\\sin(\\theta/2)/(\\theta/2)$ from the centre along the bisector.",
          "Line distributions: uniform rod on the $x$-axis from $0$ to $L$: $dm = (M/L)dx$, $X_{cm} = \\frac{1}{M}\\int_0^L \\frac{M}{L}x\\,dx = L/2$. Semicircular ring by angle: $dm = (M/\\pi)d\\phi$, $y = R\\sin\\phi$: $y_{cm} = \\frac{1}{M}\\int_0^\\pi \\frac{M}{\\pi}R\\sin\\phi\\,d\\phi = \\frac{2R}{\\pi}$. Semicircular disc by shells: $dm = (2M/R^2) r\\,dr$ half-rings, each at $y = 2r/\\pi$: integrate to $4R/(3\\pi)$.",
          ("FN", "the table values are the standard-exam vocabulary: every composite COM problem reduces to these blocks plus the weighted average.")]),
     CX('h3', CH, "Why the table values sit where they do",
       ["WHY the ring beats the disc ($2/\\pi > 4/(3\\pi)$) because the ring puts all its mass at radius $R$, so the average height above the diameter is larger than for the disc where interior mass pulls the average down. The shell hemisphere ($R/2$) sits higher than the solid one ($3R/8$) for the same reason. The cone's $h/4$ reflects the $r^2$ mass weighting toward the base.",
          "CHECK sanity of every table entry: all distances are positive, less than the body size, and shrink correctly with the body. Arc limit: as $\\theta \\to 0$, $\\sin(\\theta/2)/(\\theta/2) \\to 1$ and the arc becomes a point mass at radius $R$; as $\\theta \\to \\pi$ the arc becomes a semicircular ring and $R\\sin(\\pi/2)/(\\pi/2) = 2R/\\pi$ exactly matches the table.",
          ("CHECK", "self-audit before any exam submit: units (length), symmetry argument stated, and the result moves the right way when a mass grows.")]),
]), "Definition R = (1/M) sum m_i r_i; standard bodies table; symmetry; discrete and continuous drills.")

# ---------------------------------------------------- CM-02 holes and negative mass
ADD('CM-02', CHUNK([
    CX('h2', HEAD, "The negative-mass trick: cutting a hole is adding a negative piece",
       ["To find the COM of a body with a hole, SUPERPOSE: treat the holed body as the full solid body PLUS a negative-mass piece filling the hole. $M\\mathbf{R} = M_1\\mathbf{r}_1 - M_2\\mathbf{r}_2$ so $\\mathbf{R} = \\dfrac{M_1\\mathbf{r}_1 - M_2\\mathbf{r}_2}{M_1 - M_2}$, with $M_2$ the mass the removed material would have had. The result is algebraically identical to integrating the remaining body, and far faster.",
          "Classic (source E1-family): uniform disc of radius $R$, mass $M_1$; a hole of radius $R/2$ is cut with its centre at $R/2$ from the disc centre. Densities match, so $M_2 = M_1/4$ (mass scales with area). Set the disc centre at the origin and the hole centre at $R/2$: $X = \\frac{M_1(0) - (M_1/4)(R/2)}{M_1 - M_1/4} = \\frac{-M_1R/8}{3M_1/4} = -\\frac{R}{6}$. The COM sits on the OPPOSITE side of the disc centre, at $R/6$ - it never lies inside the hole; it shifts AWAY from the cut.",
          "General recipe: (1) choose an origin at a symmetry point of the FULL body; (2) compute $M_2$ from area/volume ratios; (3) plug into the formula with the SIGNED mass; (4) sanity-check the direction: the COM always moves away from the removed material. Equivalent viewpoint: keep the hole positive and subtract - the superposition is exact because the mass distribution is additive.",
          ("WHY", "the trick works because $\\int_{body\\setminus hole} = \\int_{body} - \\int_{hole}$ linearity: mass, first moments, and the COM definition are all linear in the mass distribution. It is the same reason superposition works for fields."),
          ("CHECK", "limits: $M_2 \\to 0$ gives $R \\to \\mathbf{r}_1$ (no cut, no shift); $M_2 \\to M_1$ (cut everything) gives a vanishing denominator - the formula correctly refuses. For the $R/2$-hole disc, shift $R/6$ is less than $R/2$ ✓ between centre and hole edge; check by symmetry that the COM stays on the centre-hole line.")]),
     CX('h3', CH, "Composite bodies: cut, place, average",
       ["E1-style worked numbers (source E1): a plate made of two pieces: piece A mass 2 kg with COM at (1, 2) cm, piece B mass 3 kg with COM at (3, 1) cm: $X = (2(1) + 3(3))/5 = 2.2$ cm... precisely $11/5 = 2.2$; $Y = (2(2) + 3(1))/5 = 7/5 = 1.4$ cm. Source E1 prints 2.21 and 1.07 for its own geometry - the method is identical: weighted average of piece COMs.",
          "L-shape from three identical squares of side $a$: place the corner at the origin; square COMs at $(a/2, a/2)$, $(3a/2, a/2)$, $(a/2, 3a/2)$: $X_{cm} = (0.5a + 1.5a + 0.5a)/3 = 5a/6$ and $Y_{cm} = (0.5a + 0.5a + 1.5a)/3 = 5a/6$. The COM sits at $(5a/6, 5a/6)$ from the outer corner, on the diagonal symmetry line.",
          "Composite discipline: never integrate what you can look up. The exam plate problems are always two standard shapes glued or one shape cut; the negative-mass trick handles cuts, the weighted average handles gluing.",
          ("CHECK", "L-tromino sanity: the COM must lie on the diagonal symmetry line $x = y$ ✓ ($5a/6 = 5a/6$); and inside the bounding square ✓.")]),
     CX('h3', CH, "Drills: holes, plates, and three-mass systems",
       ["(a) Uniform rod of length $L$ with the left third removed: full rod COM $L/2$; removed piece mass $M/3$ at $L/6$: $X = \\frac{M(L/2) - (M/3)(L/6)}{2M/3} = \\frac{L/2 - L/18}{2/3} = \\frac{8L/18}{2/3} = \\frac{2L}{3}$. The remaining two-thirds has its COM at $2L/3$ from the left end ✓ (uniform rod from $L/3$ to $L$ has midpoint $2L/3$ ✓).",
          "(b) Disc radius $R$ with a concentric hole of radius $R/2$: $X = 0$ by symmetry (the negative-mass formula gives $0/3M/4 = 0$ ✓). (c) Three masses 1, 2, 3 kg at the vertices of an equilateral triangle of side 2 m: $X = (1(0) + 2(2) + 3(1))/6 = 7/6$ m; $Y = (0 + 0 + 3\\sqrt{3})/6 = \\sqrt{3}/2$ m... with vertices $(0,0), (2,0), (1,\\sqrt{3})$ ✓.",
          ("CHECK", "drill (a) is the composite standard check: a uniform rod's COM is its midpoint whatever the slice ✓; drill (c) sits inside the triangle's bounding box ✓ and is pulled toward the 3 kg corner ✓.")]),
     CX('h3', CH, "Shift the origin: the invariance habit",
       ["The COM formula is origin-independent in the right way: shift all coordinates by $\\mathbf{a}$ and $\\mathbf{R}$ shifts by $\\mathbf{a}$; the PHYSICAL answer (the location of the COM in the body) is unchanged. Exam habit: set the origin at the largest symmetry point; compute; translate only if the question asked for a specific frame.",
          "Two-mass shortcut: $\\mathbf{R} = \\frac{m_1\\mathbf{r}_1 + m_2\\mathbf{r}_2}{m_1+m_2}$ can always be written $\\mathbf{r}_1 + \\frac{m_2}{m_1+m_2}(\\mathbf{r}_2 - \\mathbf{r}_1)$: the COM lies a fraction $\\frac{m_2}{m_1+m_2}$ of the way from mass 1 to mass 2. This single sentence answers most discrete-COM geometry questions.",
          ("CHECK", "the fraction form: for equal masses it gives the midpoint ✓; for $m_2 \\to 0$ the COM stays at $\\mathbf{r}_1$ ✓; for $m_1 \\to 0$ it goes to $\\mathbf{r}_2$ ✓.")]),
]), "Negative-mass hole trick, composite averaging, origin invariance, drills.")

# ---------------------------------------------------- CM-03 motion of the COM
ADD('CM-03', CHUNK([
    CX('h2', HEAD, "M a_cm = F_ext: the only equation of motion for a system",
       ["Newton's second law for a SYSTEM: $M\\mathbf{a}_{cm} = \\mathbf{F}_{ext}$ - internal forces cancel in third-law pairs and can never accelerate the COM. Proof in one line: $M\\ddot{\\mathbf{R}} = \\sum m_i\\ddot{\\mathbf{r}}_i = \\sum \\mathbf{F}_i = \\sum \\mathbf{F}_i^{ext} + \\sum_{pairs}(\\mathbf{f}_{ij}+\\mathbf{f}_{ji}) = \\sum \\mathbf{F}_i^{ext}$. Consequences: a system at rest with no external resultant force has a fixed COM forever; a moving system's COM continues on a straight line (source E2: the COM of an exploding shell follows the original parabola - gravity never noticed the explosion).",
          "Explosions and recoil (source E2, Q2): a shell of mass $M$ bursts into fragments; the COM continues along the pre-burst trajectory. If a 4 kg mass moving east at 6 m/s explodes into 2 kg moving west at 3 m/s... momentum: $24 = 2(-3) + 2v$: $v = 15$ m/s east for the other 2 kg piece. Source Q2 answer: the 2 kg piece moves at 6 m/s west and the COM keeps going - the exact numbers per the source's configuration; the ledger is always $\\sum m_i \\mathbf{v}_i = M\\mathbf{v}_{cm}$ = conserved.",
          "Statics via COM: if the COM hangs directly below the suspension point, the net torque about the suspension is zero and the body is in equilibrium. Tension/string problems: the string's line passes through the COM of the hanging system (source Q25-family statics).",
          ("WHY", "the internal forces cancel PAIRWISE - no cancellation is ever lost no matter how violent the explosion or how complicated the contact. This is why the COM path is the invariant of every collision and explosion problem."),
          ("CHECK", "E2 audit: projectile motion of the COM continues unaffected; if your fragment trajectories give a COM that leaves the parabola, momentum was mis-accounted. Q2 numbers: total p before $= 24$ kg m/s east; after $= 2(-3) + 2(15) = 24$ ✓.")]),
     CX('h3', HEAD, "Conservation of momentum: the conditions",
       ["$\\sum \\mathbf{p}_{before} = \\sum \\mathbf{p}_{after}$ holds when the net external IMPULSE over the interaction vanishes: (1) no external forces at all, or (2) external forces cancel, or (3) the collision is so brief that $\\int \\mathbf{F}_{ext} dt \\approx 0$ over the contact (the standard exam licence). Momentum is a VECTOR: conserve component by component; a wall's normal force can kill the perpendicular component while the parallel component survives (CM-21).",
          "System choice matters: pick the system so that the interesting forces are internal. Bullet + block: momentum conserved (gravity/normal cancel over the brief contact). Block + Earth (pendulum swing): momentum NOT conserved (the pivot pulls), but energy is. State the system before writing the equation - examiners award the statement.",
          "The COM fixed-point theorem: if total momentum is zero (initially at rest), the COM stays put no matter the internal rearrangement - man on boat (CM-19), explosion at rest (CM-05), spring release (CM-14).",
          ("CHECK", "each conservation claim must name its axis: 'horizontal momentum conserved' because the floor's normal and gravity are vertical. Silent assumptions lose marks.")]),
     CX('h3', CH, "COM motion drills",
       ["(a) 3 kg and 5 kg connected by a compressed spring on a smooth floor, released: $3v_1 + 5v_2 = 0$: velocities are in the ratio $5:3$ opposite. (b) A man at one end of a 4 kg boat walks to the other end: the COM of man\\boat stays fixed horizontally (CM-19). (c) A ball falls and bounces elastically off the floor: during the bounce the floor's external impulse changes the SYSTEM momentum (Earth + ball conserves it); the ball alone does not.",
          "(d) Rocket in free space: no external force, so $v_{cm}$ of rocket\\exhaust is constant; the exhaust's momentum balances the rocket's gain (CM-17). (e) Explosion of a 6 kg projectile at the top of its flight into 2 kg and 4 kg: both pieces fall with $g$; the COM stays on the original parabola (source E2).",
          ("CHECK", "drill (a): $v_1 = -5v_2/3$ - the light piece moves faster in the inverse ratio ✓; total p zero before and after ✓.")]),
     CX('h3', CH, "Traps specific to the system law",
       ["Trap: $M a_{cm} = F_{ext}$ does NOT say each piece follows $F_{ext}$; it says the average does. Trap: 'internal forces are always small' - no, they can be huge; they simply cancel. Trap: using the law across a time when an external impulse acts (the pendulum pivot, the wall, friction): the COM accelerates then and momentum is not conserved.",
          "Trap: forgetting a mass in $M$ (the classic half-included hanging chain - count only what moves... for chains use the flux ledger CM-18 instead). Trap: treating $v_{cm}$ as the velocity of every part after an explosion - only the MEAN is that.",
          ("CHECK", "the 30-second audit for any problem: what is the system? what external forces act? does their impulse matter on this time scale? then choose conservation or not.")]),
]), "System form of Newton 2; conservation conditions; explosion/recoil; traps.")

# ---------------------------------------------------- CM-05 conservation of momentum scenarios
ADD('CM-05', CHUNK([
    CX('h2', HEAD, "The standard conservation scenarios (source Q2, Q17, Q22, P22, P26)",
       ["Scenario 1 - explosion/recoil at rest: total p = 0 stays 0; fragment momenta are equal and opposite. 4 kg at rest explodes into 2.5 kg and 1.5 kg: $2.5v_1 = -1.5v_2$: speeds in the ratio $1.5 : 2.5 = 3 : 5$. Scenario 2 - projectile explosion at the top (source E2): horizontal momentum conserved through the burst; gravity sets the COM parabola. Scenario 3 - two skaters push apart (source Q17-family): $m_1v_1 = -m_2v_2$ in the COM sense; speeds inverse to masses.",
          "Scenario 4 - bullet into block (P22): $m v_0 = (m + M)V$; the pair then swings (CM-13). Scenario 5 - ball off a wedge on a smooth floor: horizontal momentum conserved; the wedge recoils so that $m v_x + M V = $ const; the COM stays fixed horizontally (CM-19). Scenario 6 - collision on a smooth surface with frictionless supports (P26): conserve the free component; name the constrained one.",
          "Scenario 7 - man on boat (Q10, E8): fixed COM displacements. Scenario 8 - spring released between blocks (Q18, corrected): zero total momentum + spring energy = shared KE (CM-14). Every one of these is 'choose the system, kill the internal forces, project on the free axis'.",
          ("WHY", "conservation is not a formula but a BOOKKEEPING CHOICE: system, axis, time window. Made correctly, the rest is arithmetic; made silently, the classic errors (energy across collisions, momentum across swings) appear."),
          ("CHECK", "Q2 audit: before $= 24$ kg m/s; after: piece 1 west at 3 m/s carries $-6$; the 2 kg piece must carry $+30$: $v = 15$ m/s east; COM speed before and after is the same $6$ m/s for a4 kg system... $24/4 = 6$ ✓ unchanged ✓.")]),
     CX('h3', HEAD, "Momentum with external forces present: the impulse window",
       ["When external forces act, momentum conservation still applies if the external IMPULSE over the window is negligible: collision contact times (ms) make gravity's $mg\\Delta t$ tiny - the exam licence. When the window is long (swing, slide), momentum is NOT conserved but energy may be. The two-stage protocol (CM-13) is this dichotomy in action.",
          "Friction window: a block sliding on a rough floor has momentum destroyed by $\\mu mg t$; if the problem asks for speeds after a slide, use work-energy instead. Explosion on a rough surface: conserve momentum THROUGH the explosion (brief), then let friction work on each piece separately.",
          "Water/rocket windows: variable-mass problems use the $dt$ ledger (CM-16/17) - momentum of the chosen system plus flux terms; never mix the flux ledger with the closed-system shortcut silently.",
          ("CHECK", "window audit: state 'contact time is short so external impulse is negligible' before using conservation - that sentence is the licence.")]),
     CX('h3', CH, "Choosing the system: worked contrasts",
       ["(a) Ball bounces off the floor: system = ball alone: floor impulse external, momentum not conserved. System = ball + Earth: conserved (and huge mass makes the recoil unmeasurable). (b) Bullet through block (Q19): system = bullet + block: horizontal p conserved through the passage ✓; energy is not (1045 J to heat).",
          "(c) Two blocks and a spring on ice: system = both + spring: p conserved, and mechanical energy conserved (smooth spring) - the rare case where BOTH hold. (d) Cart under a hopper (OLY-10): system = cart + dropped sand column: horizontal p conserved; the loading force $\\dot m v$ is internal to the widened system.",
          ("CHECK", "one-liner test: 'could an external force deliver a noticeable impulse during the event?' If yes and you used conservation, the answer is wrong.")]),
     CX('h3', CH, "Conservation drills",
       ["(a) 5 kg cart at 4 m/s picks up 5 kg dropped from rest: $v = 20/10 = 2$ m/s. (b) 3 kg at 6 east collides and sticks to 2 kg at 4 west: $18 - 8 = 10 = 5v$: $v = 2$ m/s east. (c) 0.5 kg ball at 10 hits 1.5 kg at rest, $e = 0.5$: $v_2 = (1.5)(0.5)(10)/2 = 3.75$... precisely $v_2 = (1+e)m_1u_1/(m_1+m_2) = 1.5(0.5)(10)/2 = 3.75$ m/s; $v_1 = (0.5-0.75)10/2 = -1.25$ m/s (rebounds).",
          "(d) Two ice skaters 60 and 90 kg push to relative 3 m/s: $60v_1 = 90v_2$, $v_1 + v_2 = 3$: $v_2 = 1.2$, $v_1 = 1.8$ m/s.",
          ("CHECK", "drill (c) energy: $K_i = 25$; $K_f = 0.5(0.5)(1.56) + 0.5(1.5)(14.06) = 0.39 + 10.55 = 10.94$ J; loss $= 14.06 = \\frac{1}{2}(0.375)(25)(1-0.25)$... $\\mu = 0.375$, $u_{rel} = 10$: $\\frac{1}{2}(0.375)(100)(0.75) = 14.06$ ✓.")]),
]), "Eight standard scenarios; impulse windows; system choice; drills.")

# ---------------------------------------------------- CM-06 classifying collisions and restitution
ADD('CM-06', CHUNK([
    CX('h2', HEAD, "Elastic, inelastic, sticking: one number e prices every collision",
       ["Definitions: ELASTIC = kinetic energy conserved, $e = 1$. PERFECTLY INELASTIC = the bodies stick (maximum KE loss consistent with momentum), $e = 0$. INELASTIC = anything between, $0 < e < 1$. SUPERELASTIC = $e > 1$ with a released spring/explosive - possible, and energy GAINS. The coefficient of RESTITUTION measures speeds along the line of impact: $e = \\dfrac{v_{sep}}{v_{app}} = \\dfrac{v_2 - v_1}{u_1 - u_2}$ (1-D; see CM-11 for the 2-D projection).",
          "Why $e$ is about speeds not velocities: it is defined on the components along the common normal at contact. For smooth bodies the tangential components are untouched; friction is the only channel across (source trap). Material dependence: $e$ varies with speed and temperature; the exam treats it as a given constant per problem. Energy is a derived quantity here: $e$ and momentum decide the outcome; energy then reports the bill (CM-09).",
          "Sticking = the INELASTIC limit: after contact the bodies share $v_{cm}$ - the only outcome consistent with zero separation speed and momentum conservation. Perfectly inelastic is NOT 'maximum energy destroyed' in one number - it is 'minimum final KE' subject to the momentum ledger; the lost amount is exactly $K_{rel}$ (CM-09).",
          ("WHY", "the separation/definition choice makes the whole classification one dimensionless number; every exam question about 'what kind of collision' reduces to (i) what is $e$ and (ii) where is the line of impact."),
          ("CHECK", "limits: $e = 0 \\Rightarrow v_2 = v_1 = v_{cm}$ ✓; $e = 1 \\Rightarrow$ energy conserved ✓ (verify with the master formulas of CM-07); $e > 1 \\Rightarrow$ post-collision KE exceeds pre - flag it as superelastic rather than erroring.")]),
     CX('h3', HEAD, "The line of impact (source C1-C2 family)",
       ["For SPHERES the line of impact is the line joining centres at the moment of contact. The plane of contact is perpendicular to it. $e$ applies along the line of impact ONLY. For a smooth wall the line of impact is the wall normal. For rough bodies or spinning balls, tangential impulses exist and $e$ no longer closes the system alone - the problem needs friction data.",
          "Angle traps (source C9, corrected): a ball bouncing off a smooth wall leaves at angle $\\theta_r$ with $\\tan\\theta_r = \\tan\\theta_i / e$ from the normal - MORE grazing for $e < 1$; equal angles iff $e = 1$. The mirrored-bounce picture is the elastic-only special case (full correction in CM-22).",
          "2-D bookkeeping (CM-11): project velocities onto the line of impact, apply momentum + $e$ there, leave tangential components unchanged, recompose. The whole of oblique-collision theory is this three-step recipe.",
          ("CHECK", "draw the contact configuration FIRST: the line of impact is geometry, not choice. A wrong line poisons every later equation.")]),
     CX('h3', HEAD, "Impulse of deformation and impulse of reformation (Cengage 1.22 addition)",
       ["Every direct impact has two phases. DEFORMATION: the bodies squish to a common velocity $v_{cm}$; the impulse so far is $J_d = \\mu u_{rel}$ (exactly what kills the relative velocity). REFORMATION: elastic recovery pushes them apart with impulse $J_r = e\\,\\mu u_{rel}$. Total contact impulse on each body along the line: $J = (1+e)\\mu u_{rel}$.",
          "Energy reading: at maximum deformation ALL the relative KE $\\frac{1}{2}\\mu u_{rel}^2$ is stored; recovery returns the fraction $e^2$; what never returns is $\\frac{1}{2}\\mu u_{rel}^2(1-e^2)$. Sticking ($e = 0$) has no reformation phase at all; elastic ($e = 1$) has $J_r = J_d$ and returns everything.",
          "Why $J_d = \\mu u_{rel}$ is pure mechanics: at max deformation both bodies share $v_{cm}$ (momentum fixes it whatever the contact law); the impulse that took $(u_1, u_2) \\to (v_{cm}, v_{cm})$ is $m_1(v_{cm} - u_1) = -\\mu u_{rel}$. Only $J_r = e J_d$ is the material's business.",
          ("CHECK", "2 kg at 5 into 3 kg rest, $e = 0.6$: $J_d = 6$, $J_r = 3.6$, $J = 9.6$ N s; velocities $v_1 = 0.2$, $v_2 = 3.2$; impulse on 3 kg $= 9.6$ ✓ matches $J$.")]),
     CX('h3', CH, "Classification drills and traps",
       ["(a) 1 kg at 8 sticks to 3 kg at rest: $v_{cm} = 2$; lost $= K_{rel} = \\frac{1}{2}(0.75)(64) = 24$ J; $K_i = 32$, $K_f = 8$: loss 24 ✓ ($e = 0$). (b) Same masses elastic: $v_1 = -4$, $v_2 = 4$; energy conserved ✓. (c) $e = 0.7$ version: $v_1 = (1-2.1)8/4 = -2.2$; $v_2 = 1.7(1)(8)/4 = 3.4$; $e$-check $(3.4+2.2)/8 = 0.7$ ✓.",
          "Trap: 'inelastic means the bodies stick' - only PERFECTLY inelastic does. Trap: using $e$ for energy directly - $e$ is a speed ratio; energy scales as $e^2$. Trap: applying $e$ to the full speed in 2-D instead of the normal component.",
          ("CHECK", "drill (a) fraction: equal masses lose exactly HALF the KE when sticking ($K_{cm} = K_{rel}$ split) ✓ - a favourite true/false.")]),
]), "Restitution definition and scope; line of impact; deformation/reformation impulses; drills.")

# ---------------------------------------------------- CM-07 the 1-D master formulas
ADD('CM-07', CHUNK([
    CX('h2', HEAD, "The pair that prices every 1-D collision",
       ["Momentum: $m_1u_1 + m_2u_2 = m_1v_1 + m_2v_2$. Restitution: $v_2 - v_1 = -e(u_1 - u_2)$. Solve the pair for the master formulas: $v_1 = \\dfrac{(m_1 - e m_2)u_1 + (1+e)m_2 u_2}{m_1 + m_2}$ and $v_2 = \\dfrac{(1+e)m_1 u_1 + (m_2 - e m_1)u_2}{m_1 + m_2}$. Valid in 1-D (or along the line of impact in 2-D) for fixed masses; $e$ given; no external impulse.",
          "Memory anchors: the shooter's own mass enters its numerator with MINUS $e$ times the target's; the target's velocity is dragged in with $+(1+e)$; the denominator is always the total mass. Limits: $e = 0$ gives both velocities $= v_{cm}$ ✓; $e = 1$, $m_1 = m_2$ gives $v_1 = u_2$, $v_2 = u_1$ (the exchange) ✓; $m_2 \\gg m_1$ gives $v_1 \\approx -u_1 + 2u_2$ (the wall) ✓.",
          "Relative-velocity form: $v_{rel} = -e\\,u_{rel}$ with $u_{rel} = u_1 - u_2$ - one line, sign-sensitive. Combined with $v_{cm}$ fixed by momentum, this reconstructs both velocities faster than the formulas when $u_2 = 0$ or masses are equal. The CM frame (CM-15) is the same pair in geometric dress.",
          ("WHY", "the pair is complete: two equations, two unknowns. $e$ is the only place material physics enters; everything else is conservation. Any collision answer that violates either equation is simply wrong."),
          ("CHECK", "three-invariant audit for every computed answer: (1) signed momentum, (2) $e = (v_2-v_1)/(u_1-u_2)$, (3) energy ledger (CM-09). The trio catches sign slips, mis-multiplied factors, and wrong-mass errors.")]),
     CX('h3', CH, "Worked with the invariants: the P32 set (source)",
       ["2 kg at 5 m/s hits 3 kg at $-2$ m/s with $e = 0.5$ (source P32). Momentum: $10 - 6 = 4$. Master: $v_1 = \\frac{(2-1.5)(5) + 1.5(3)(-2)}{5} = \\frac{2.5 - 9}{5} = -1.3$ m/s; $v_2 = \\frac{1.5(2)(5) + (3-1)(-2)}{5} = \\frac{15 - 4}{5} = 2.2$ m/s. Invariant 1: $2(-1.3) + 3(2.2) = -2.6 + 6.6 = 4$ ✓. Invariant 2: $(2.2 + 1.3)/(5 + 2) = 3.5/7 = 0.5$ ✓. Invariant 3: $K_i = \\frac{1}{2}(2)(25) + \\frac{1}{2}(3)(4) = 31$ J; $K_f = \\frac{1}{2}(2)(1.69) + \\frac{1}{2}(3)(4.84) = 8.95$ J; loss $= 22.05$ J, exactly $\\frac{1}{2}(1.2)(49)(1-0.25) = 22.05$ from the CM-09 formula.",
          "Arithmetic discipline: the factor $(1+e)$ multiplies the WHOLE $m_2u_2$ term ($1.5 \\times 3 \\times (-2) = -9$, not $-15$); one dropped factor here produced the source's Q18 slip family. Write the numerator terms with their factors before multiplying.",
          ("CHECK", "if any of the three invariants fails, recompute - do not adjust the answer to fit. The three together pin the solution uniquely.")]),
     CX('h3', CH, "Drill set (each: compute, then audit)",
       ["(a) 2 kg at 5 vs 2 kg rest, $e = 1$: $v_1 = 0$, $v_2 = 5$ (exchange). (b) Same with $e = 0.5$: $v_1 = 1.25$, $v_2 = 3.75$; $e$-check $2.5/5 = 0.5$ ✓. (c) 3 kg at 4 vs 3 kg at $-4$, $e = 1$: $v_1 = -4$, $v_2 = 4$ (equal masses swap in the CM: they reverse). (d) 0.5 kg at 12 vs 1.5 kg rest, $e = 0.8$: $v_1 = (0.5-1.2)12/2 = -4.2$; $v_2 = 1.8(0.5)(12)/2 = 5.4$; check $(5.4+4.2)/12 = 0.8$ ✓.",
          '(b2) 0.2 kg at 10 m/s vs 0.3 kg at rest, $e = 0.8$: $v_1 = (0.2-0.24)10/0.5 = -0.8$ m/s (rebounds); $v_2 = 1.8(0.2)(10)/0.5 = 7.2$ m/s; audit: $p = 2$ both sides; $e = (7.2+0.8)/10 = 0.8$; $K_{loss} = 10 - (0.064 + 7.776) = 2.16 = \\frac{1}{2}(0.12)(100)(0.36)$ - the momentum, restitution and loss checks agree.',
          ("CHECK", "drill (d) energy: $K_i = 36$; $K_f = 4.41 + 21.87 = 26.28$; loss $= 9.72 = \\frac{1}{2}(0.375)(144)(1-0.64) = 9.72$ ✓.")]),
     CX('h3', CH, "When the master formulas are the wrong tool",
       ["Two contacts at once (a wedge between two balls): solve the constraints together or sequentially with clear stages. Variable mass: use the flux ledger (CM-16). Extended bodies with spin: angular impulse needed (rigid-body chapter). Explosions: $e$ is meaningless (no contact) - use momentum + energy release. 2-D: project first (CM-11).",
          "The formulas also fail if $e$ is velocity-dependent (real materials at high speed): then the problem must give $e$ at the relevant speed or an energy loss directly. State the constant-$e$ assumption when using them.",
          ("CHECK", "tool-selection audit: does the problem have ONE contact, two fixed masses, and a stated $e$? If yes use the masters; if not, fall back to first principles.")]),
]), "Master formulas 3.7a/b; three-invariant audit; P32 worked; drills.")

# ---------------------------------------------------- CM-08 special cases of 1-D collisions
ADD('CM-08', CHUNK([
    CX('h2', HEAD, "Special cases worth recognising on sight",
       ["CASE 1 - equal masses, elastic ($e = 1$): VELOCITIES EXCHANGE: $v_1 = u_2$, $v_2 = u_1$ (source E3). One stops if the other was at rest - in 1-D only; in 2-D the equal-mass elastic result is the 90-degree separation (CM-12). CASE 2 - equal masses, any $e$: $v_1 = \\frac{(1-e)}{2}u_1 + \\frac{(1+e)}{2}u_2$ and vice versa - the symmetric split.",
          "CASE 3 - heavy target ($m_2 \\gg m_1$): $v_1 \\approx (1-e)u_2 - e u_1 + $ corrections; for a wall at rest: $v_1 \\approx -e u_1$ (rebounds scaled), $v_2 \\approx 0$ (wall barely moves). CASE 4 - light target ($m_1 \\gg m_2$): $v_1 \\approx u_1$ (plows on), $v_2 \\approx (1+e)u_1 - e u_2 \\approx 2u_1$ for resting light target and $e = 1$ - the light flies at nearly TWICE the heavy's speed. Q21-set (source): heavy into light elastic: the light piece's speed is nearly $2u$ and the heavy barely slows (source prints $-2$ / $1$ for its configuration).",
          "CASE 5 - sticking: $v = v_{cm}$ for both. CASE 6 - projectile vs equal target at rest with $e$: $v_1 = \\frac{(1-e)}{2}u$, $v_2 = \\frac{(1+e)}{2}u$ - memorise this pair; many drills specialise it. CASE 7 - target moving toward shooter: use the full formulas; the relative-velocity form $v_{rel} = -e u_{rel}$ plus $v_{cm}$ is fastest.",
          ("WHY", "the cases are the master formulas seen in their natural limits; recognising them converts a 3-minute derive into a 20-second quote - with the derivation still available if the numbers don't match a case.")]),
     CX('h3', CH, "Q11 worked (the detective problem, source)",
       ["Ball A of mass $m$ at speed $u$ strikes ball B (mass $m$) at rest; after, A moves at $u/3$ at some angle... source Q11's configuration: use the master formulas + the 90-degree theorem (CM-12) to pin the outcome: for equal masses elastic 2-D, $\\theta_1 + \\theta_2 = 90$ and $v_1 = u\\cos\\theta_1$, $v_2 = u\\sin\\theta_1$; given one post speed or angle, the rest follows from the momentum triangle.",
          "Method (any Q11-type): (1) check the 90-degree conditions; (2) draw the momentum triangle ($\\mathbf{u} = \\mathbf{v}_1 + \\mathbf{v}_2$); (3) quote the two speeds as components of $u$; (4) audit KE. If the masses differ or $e < 1$, drop the theorem and run the CM-frame machinery (OLY-02).",
          ("CHECK", "sanity: for any angle the two speeds satisfy $v_1^2 + v_2^2 = u^2$ (elastic equal-mass) - the circle of possible outcomes has radius $u$.")]),
     CX('h3', CH, "Contrast drills: same masses, different e",
       ["2 kg at 6 vs 2 kg rest. $e = 1$: $v_1 = 0$, $v_2 = 6$ (exchange). $e = 0.5$: $v_1 = 1.5$, $v_2 = 4.5$; loss $= 27 - (2.25 + 20.25) = 4.5$ J... $K_i = 36$; $K_f = 2.25 + 20.25 = 22.5$; loss 13.5 J $= \\frac{1}{2}(1)(36)(0.75) = 13.5$ ✓. $e = 0$: both at 3 m/s; loss $= 18 = K_{rel}$ ✓.",
          "1 kg at 8 into 3 kg at rest, $e = 1$: $v_1 = (1-3)8/4 = -4$ (rebounds); $v_2 = 2(1)(8)/4 = 4$; loss 0 ✓. Same with $e = 0$: both at 2 m/s; loss $= 24 = \\frac{1}{2}(0.75)(64)$ ✓.",
          ("CHECK", "the trend table: as $e$ falls from 1 to 0, the shooter's rebound fades into forward drift at $v_{cm}$ and the energy loss rises from 0 to $K_{rel}$ monotonically ✓.")]),
     CX('h3', CH, "Recognition drills (60 seconds each)",
       ["(a) equal masses, elastic, one at rest: exchange. (b) heavy hits light elastic at rest: light flies at $\\approx 2u$. (c) light hits heavy at rest, $e = 1$: light rebounds at $\\approx u$. (d) perfectly inelastic any masses: common $v_{cm}$. (e) equal masses elastic 2-D: 90 degrees.",
          "Warning: case 1 is 1-D ONLY (source P5's ambiguity; corrected reading in CM-22); case 3's $2u$ needs $e = 1$; case 5's energy loss is $K_{rel}$, not 'all the energy'.",
          ("CHECK", "self-test: state each case's hypotheses before its conclusion - the hypotheses ARE the exam points.")]),
]), "Equal-mass exchange, heavy/light limits, sticking; Q11 method; contrast drills.")

# ---------------------------------------------------- CM-09 energy loss and the reduced mass
ADD('CM-09', CHUNK([
    CX('h2', HEAD, "K_loss = 1/2 mu (u1-u2)^2 (1-e^2): the complete energy bill",
       ["Decompose the KE: $K = \\frac{1}{2}Mv_{cm}^2 + \\frac{1}{2}\\mu v_{rel}^2$ with $\\mu = \\dfrac{m_1 m_2}{m_1 + m_2}$ (CM-15). Momentum conservation freezes $v_{cm}$; restitution sets $v_{rel}^{after} = -e\\,v_{rel}^{before}$. The collision can only spend the relative part: $K_{loss} = \\frac{1}{2}\\mu u_{rel}^2(1 - e^2)$ with $u_{rel} = u_1 - u_2$ (source 3.8, P32).",
          "Reading the formula: the STAKE is $K_{rel} = \\frac{1}{2}\\mu u_{rel}^2$ (the reduced mass and the approach speed); the FRACTION spent is $1 - e^2$ (not $1 - e$). $e = 1$: nothing lost; $e = 0$: the whole $K_{rel}$ gone; superelastic $e > 1$: negative loss = energy released (a spring). The $K_{cm}$ term is untouchable - sticking still leaves $\\frac{1}{2}Mv_{cm}^2$ moving.",
          "Worked (P32 numbers): $\\mu = 1.2$, $u_{rel} = 7$, $e = 0.5$: $K_{loss} = \\frac{1}{2}(1.2)(49)(0.75) = 22.05$ J ✓ equals $K_i - K_f = 31 - 8.95$ from the master formulas (CM-07). Equal masses sticking: $\\mu = m/2$, $u_{rel} = u$: loss $= \\frac{1}{4}mu^2 = \\frac{1}{2}K_i$ - HALF the energy, the classic true/false (source trap).",
          ("WHY", "the decomposition is exact for two bodies (parallel-axis theorem for KE): $\\sum \\frac{1}{2}m_i v_i^2 = \\frac{1}{2}Mv_{cm}^2 + \\frac{1}{2}\\mu v_{rel}^2$; the cross terms vanish because $\\sum m_i \\mathbf{v}'_i = 0$. So the collision's budget is literally $K_{rel}$."),
          ("CHECK", "E4 (source): 4 kg at 6 into a wall... the perfectly inelastic pair loses $K_{rel}$: 4 kg at 6 sticks to 1 kg: $\\mu = 0.8$, $u_{rel} = 6$: loss $= \\frac{1}{2}(0.8)(36) = 14.4$ J; $K_i = 72$, $v = 4.8$, $K_f = 57.6$; loss 14.4 ✓. Source E4 prints 183.8 J for its own configuration - same formula.")]),
     CX('h3', CH, "Energy ledgers in two-stage problems",
       ["Ballistic pendulum (CM-13): stage-1 loss $= K_{rel}$ with $\\mu \\approx m_{bullet}$; the surviving fraction $m/(m+M)$ of the bullet KE then converts to $mgh$ (E5: 800 J in, 3.98 J swing, 796 J heat = 99.5%). Bullet through block (Q19): $K_i = 1250$, $K_f = 204.5$: 1045.5 J heat. Spring problems (CM-14): the collision's loss and the spring's share must be booked separately.",
          "Superelastic bookkeeping: if $e > 1$ or a spring releases during contact, $K_{loss} < 0$; write $K_{gain} = \\frac{1}{2}\\mu u_{rel}^2(e^2-1)$ and state the source of the energy. Explosions: $\\Delta K = +$ chemical/spring release (source E2): no restitution involved.",
          ("CHECK", "double-entry: compute the loss both from $K_i - K_f$ (master formulas) and from $\\frac{1}{2}\\mu u_{rel}^2(1-e^2)$; they must agree to rounding (P32: 22.05 both ways).")]),
     CX('h3', CH, "The reduced mass itself",
       ["$\\mu = m_1m_2/(m_1+m_2)$: smaller than either mass; for equal masses $m$: $\\mu = m/2$; for $m_2 \\gg m_1$: $\\mu \\approx m_1$ (the light one sets the scale); symmetric in the two bodies. $M = m_1 + m_2$ for the COM term. The pair $(M, \\mu)$ is the natural coordinates of two-body motion - the same $\\mu$ appears in the relative-coordinate equation $\\mu a_{rel} = F_{internal}$ and in spring oscillations of two-body systems.",
          "Limits: $\\mu \\to 0$ when one mass vanishes (no collision stake); $\\mu \\to m/2$ for equal; $1/\\mu = 1/m_1 + 1/m_2$ (the harmonic flavour). Drill: 3 kg and 6 kg: $\\mu = 2$ kg; 1 kg and 1 kg: 0.5; 1 kg and 1000 kg: 0.999.",
          ("CHECK", "dimension: $\\mu$ is a mass; $\\frac{1}{2}\\mu v^2$ an energy ✓; the loss formula is never negative for $|e| \\le 1$ ✓.")]),
     CX('h3', CH, "Loss-formula drills",
       ["(a) 2 kg at 5 vs 3 kg at $-2$, $e = 0.5$ (P32): 22.05 J. (b) Equal 1 kg masses, $u = 4$, $e = 0.8$: $K_{rel} = 4$, loss $= 4(1-0.64) = 1.44$ J. (c) 0.5 kg at 12 vs 1.5 kg rest, $e = 0.8$: $\\mu = 0.375$, $u_{rel} = 12$: stake $= 27$, loss $= 27(0.36) = 9.72$ J (matches CM-07 drill (d)).",
          "Trap: using $1 - e$ instead of $1 - e^2$; using $m_1 + m_2$ instead of $\\mu$; forgetting $u_{rel}$ is SIGNED before squaring (sign dies in the square - but keep it for the $e$-check).",
          ("CHECK", "cross-audit every drill against the master-formula difference; the two routes agreeing is the exam's strongest check.")]),
]), "K_loss formula and derivation; two-stage ledgers; reduced mass; drills.")

# ---------------------------------------------------- CM-10 impulse of deformation and reformation
ADD('CM-10', CHUNK([
    CX('h2', HEAD, "Two impulses inside every collision: deformation and reformation",
       ["A direct impact has two phases. Phase 1 DEFORMATION: the bodies approach at $u_{rel} = u_1 - u_2$, squish, and reach a common velocity $v_{cm}$ at the instant of maximum deformation. The impulse delivered by contact so far is $J_d = \\mu u_{rel}$ (exactly what is needed to kill the relative velocity: after it, both bodies move at $v_{cm}$). Phase 2 REFORMATION: elastic recovery pushes them apart; the reformation impulse is $J_r = e\\,\\mu u_{rel}$. Total contact impulse on each body: $J = J_d + J_r = (1+e)\\mu u_{rel}$, directed along the line of impact.",
          "Why $J_d = \\mu u_{rel}$: at maximum deformation both bodies share one velocity $v$; momentum conservation fixes $v = v_{cm}$ regardless of the contact law. The impulse that took the pair from $(u_1, u_2)$ to $(v_{cm}, v_{cm})$ is $m_1(v_{cm} - u_1) = -\\mu u_{rel}$ on body 1 (and opposite on body 2) - pure algebra from momentum, no material assumption. Then the reformation is the material-dependent part: the contact force history after the peak, with impulse scaled by $e$.",
          "Energy story (this is where the $1-e^2$ comes from): at maximum deformation the ENTIRE relative KE $\\frac{1}{2}\\mu u_{rel}^2$ has been extracted (stored as deformation energy in the contact). Recovery returns a fraction $e^2$ of it ($\\frac{1}{2}\\mu(e u_{rel})^2$ of relative KE after separation). What never comes back: $\\frac{1}{2}\\mu u_{rel}^2(1-e^2)$ = the permanent loss. For sticking ($e = 0$) there is no phase 2 at all; for elastic ($e = 1$) phase 2 returns everything and $J_r = J_d$.",
          ("WHY", "the decomposition isolates the material law in ONE number ($e$) while phase 1 is universal mechanics. It also answers 'maximum compression of the spring between the carts' questions: at max deformation the spring holds ALL of the former relative KE; equate $\\frac{1}{2}k x_{max}^2 = \\frac{1}{2}\\mu u_{rel}^2$ (CM-14)."),
          ("CHECK", "impulse route reproduces the master formulas: $v_1 = u_1 - J/m_1$, $v_2 = u_2 + J/m_2$ with $J = (1+e)\\mu u_{rel}$ gives (3.7a-b) term by term. Elastic equal masses: $J = 2\\mu u = mu$; shooter: $u - mu/m = 0$ stops; target: $0 + mu/m = u$ takes the speed.")]),
     CX('h3', HEAD, "Numbers: J_d, J_r and the peak-force language",
       ["2 kg at 5 m/s hits 3 kg at rest with $e = 0.6$: $u_{rel} = 5$, $\\mu = 1.2$. $J_d = 1.2\\times5 = 6$ N s; $J_r = 0.6\\times6 = 3.6$ N s; $J = 9.6$ N s. Check via velocities: $v_1 = (2-1.8)5/5 = 0.2$ m/s; $v_2 = 1.6\\times2\\times5/5 = 3.2$ m/s. Impulse on 2 kg: $2(0.2-5) = -9.6$ N s equals $-J$; on 3 kg: $3(3.2) = 9.6$.",
          "Peak contact force: at the deformation instant the relative speed is zero and the spring-like contact is maximally compressed - that is where the largest force acts. If a problem quotes an average force over contact time $\\Delta t$: $\\bar F = J/\\Delta t$; if it quotes a spring constant for the contact: $\\frac{1}{2}kx_{max}^2 = \\frac{1}{2}\\mu u_{rel}^2$ and $x_{max}$ occurs at $v_{cm}$ (same instant). The deformation instant is the answer to 'when is the spring fully compressed' questions.",
          ("CHECK", "deformation-phase energy audit on the numbers above: $K_i = 25$ J; at $v_{cm} = 2$ m/s: $K = \\frac{1}{2}(5)(4) = 10$ J; extracted $= 15$ J $= \\frac{1}{2}(1.2)(25) = 15$ J $= K_{rel}$. After reformation: $K_f = \\frac{1}{2}2(0.04) + \\frac{1}{2}3(10.24) = 15.4$ J; returned $= 5.4$ J $= e^2 K_{rel} = 0.36\\times15$. Lost $= 9.6$ J $= 15(1-0.36)$."),
          ("FN", "the Cengage floor names these the impulse of deformation ($J_d$) and impulse of reformation ($J_r$) in section 1.22; the source chapter does not treat them explicitly - added here as core JEE mechanics.")]),
     CX('h3', CH, "Where the phase picture is used",
       ["(1) Spring between carts: max compression at the deformation instant when both move at $v_{cm}$; energy $= K_{rel}$ stored; then release. If the contact is perfectly elastic, the spring returns all of it and the carts separate with $e = 1$ formulas. (2) Squeezing force questions: 'what is the maximum force during contact' - use the contact spring law at $x_{max}$. (3) Two-stage contact: two carts with a bumper of $e$ then a stop - apply the impulse ledger stage by stage.",
          "(4) Sticking clay: $J = J_d$ only; the whole $K_{rel}$ becomes heat. (5) Real materials: $e < 1$ because the contact hysteresis loop is smaller than the loading loop - $J_r < J_d$; the ratio $J_r/J_d = e$ IS the restitution coefficient in impulse language.",
          ("WHY", "the phase picture survives even when the contact is not a linear spring: $J_d = \\mu u_{rel}$ is pure momentum; only $J_r = e J_d$ is empirical. That is why the same formulas describe clay, steel and rubber."),
          ("CHECK", "extremes: $e = 0$: $J = \\mu u_{rel}$, no return; $e = 1$: $J = 2\\mu u_{rel}$, full return. The total impulse is always linear in $(1+e)$ - a useful graph: $J$ vs $e$ is a straight line.")]),
     CX('h3', CH, "Micro-set: impulse-decomposition drills",
       ["(a) 4 kg at 3 m/s vs 4 kg at rest, $e = 0.5$: $\\mu = 2$, $J_d = 6$, $J_r = 3$, $J = 9$; $v_1 = (4-2)3/8 = 0.75$ m/s; $v_2 = 1.5\\times4\\times3/8 = 2.25$ m/s; impulse on 4 kg: $4(0.75-3) = -9$.",
          "(b) Sticking pair 2 kg at 6 into 2 kg at rest: $\\mu = 1$, $J = J_d = 6$ N s; common speed 3 m/s. (c) Elastic equal-mass exchange: $J = 2\\mu u = mu$; the deformation and reformation impulses are equal halves of the contact jolt.",
          ("CHECK", "drill (a) energy: $K_{rel} = \\frac{1}{2}(2)(9) = 9$ J; lost $= 9(1-0.25) = 6.75$ J; direct: $K_i = 18$; $K_f = 1.125 + 10.125 = 11.25$; loss $= 6.75$.")]),
]), "Deformation and reformation impulses J_d = mu u_rel, J_r = e J_d; energy return e^2; peak compression.")

# ---------------------------------------------------- CM-11 2-D oblique collisions
ADD('CM-11', CHUNK([
    CX('h2', HEAD, "Oblique collisions: decompose on the line of impact",
       ["For smooth spheres the collision force is purely normal (no friction), so the recipe is fixed: (1) draw the line of impact (the line joining centres at contact) and the plane of contact (perpendicular to it); (2) project both velocities onto the line of impact - these 1-D components obey momentum + $e$ EXACTLY as in CM-07; (3) the components perpendicular to the line of impact (tangential) are UNCHANGED for each body; (4) recompose. Momentum is conserved in both directions, but restitution speaks only along the normal.",
          "Bookkeeping form: label the line of impact as $n$ and the tangent as $t$. Then $v_{1n} = \\frac{(m_1 - e m_2)u_{1n} + (1+e)m_2 u_{2n}}{m_1+m_2}$, $v_{2n} = \\frac{(1+e)m_1 u_{1n} + (m_2 - e m_1)u_{2n}}{m_1+m_2}$, while $v_{1t} = u_{1t}$, $v_{2t} = u_{2t}$. Four scalars in, four out. If the target is at rest, $u_{2n} = u_{2t} = 0$ and the formulas simplify to the zero-target pair of CM-07 along $n$.",
          "The geometry trap: the line of impact is NOT horizontal unless the geometry says so. For a sphere hitting a fixed inclined plane, the line of impact is the plane normal; for two spheres, it is the line of centres - which depends on the impact parameter (how grazing the hit is). Draw the contact configuration first; every later equation hangs off that line. Angles in the final answer are measured from whatever axis the problem states - recompose then project.",
          ("WHY", "tangential velocities survive because the third-law pair of contact forces acts along the common normal - friction is the only channel into $t$, and smoothness closes it. This independence is what makes 2-D decomposable into a 1-D problem plus free streaming."),
          ("CHECK", "recompose-energy sanity for elastic smooth collisions: KE is conserved iff the normal parts conserve it (they do by $e = 1$) and the tangentials are unchanged (they are). If your 2-D elastic answer fails a KE check, the projection angle is wrong.")]),
     CX('h3', HEAD, "Worked template: at-rest target, impact parameter set by geometry",
       ["A sphere $m_1$ moving horizontally at $u$ strikes an identical sphere $m_2$ at rest; the line of centres at contact makes angle $\\phi$ with the original direction (impact parameter $b = (R_1+R_2)\\sin\\phi$ for centre separation $R_1+R_2$). Decompose: $u_{1n} = u\\cos\\phi$, $u_{1t} = u\\sin\\phi$, target zero. Elastic equal masses along $n$: exchange the normal components: $v_{1n} = 0$, $v_{2n} = u\\cos\\phi$; tangentials unchanged: $v_{1t} = u\\sin\\phi$.",
          "Recompose: shooter leaves with speed $u\\sin\\phi$ perpendicular to the line of centres; target with $u\\cos\\phi$ along the line of centres. The two are PERPENDICULAR - this is the 90-degree theorem of CM-12 in general clothing. For $\\phi \\to 0$ (head-on) the shooter stops; for $\\phi \\to 90$ degrees (grazing) nothing happens; the scattering angle of the shooter is $90 - \\phi$ from its original line.",
          "With restitution $e$ and equal masses: $v_{1n} = \\frac{(1-e)}{2}u\\cos\\phi$ from the master: $v_{1n} = \\frac{(m-em)u\\cos\\phi}{2m} = \\frac{(1-e)}{2}u\\cos\\phi$; $v_{2n} = \\frac{(1+e)}{2}u\\cos\\phi$. Then $v_{1t} = u\\sin\\phi$ untouched. The shooter's speed after: $\\sqrt{u^2\\sin^2\\phi + \\frac{(1-e)^2}{4}u^2\\cos^2\\phi}$ - note only the normal part is taxed by $e$.",
          ("CHECK", "the $e = 1$, $\\phi = 0$ limit gives $v_1 = 0$, $v_2 = u$ (head-on exchange). The $\\phi = 90$ degrees limit gives $v_1 = u$, $v_2 = 0$ (no collision). Both limits of the general formula are physically obvious - a good memorisation anchor.")]),
     CX('h3', CH, "Fixed walls and inclines as 2-D collisions",
       ["Ball hits a fixed smooth wall at angle $\\theta$ from the normal with speed $v$: tangential $= v\\sin\\theta$ unchanged; normal $= v\\cos\\theta$ becomes $-e v\\cos\\theta$ (reversed and scaled). For $e = 1$: reflection with equal angles (specular). For $e < 1$: the rebound is MORE GRAZING: $\\tan\\theta' = \\tan\\theta/e$ measured from the normal - the reflected angle exceeds the incident angle. Energy: $K_f/K_i = \\sin^2\\theta + e^2\\cos^2\\theta$.",
          "Smooth incline (angle $\\alpha$ with horizontal): the line of impact is the incline normal; decompose along the normal and the incline; the normal component flips as $e$; the along-incline component is untouched. For a ball bouncing off a 30-degree incline elastically, the angle of departure is a pure geometry exercise: reflect the velocity across the normal (mirror rule) - the angle to the incline is preserved.",
          ("WHY", "the wall is the $m_2 \\to \\infty$ limit of the two-sphere problem; the wall's velocity is what enters the restitution law ($v_{sep} = e\\,v_{app}$ with the wall's motion included, CM-21). The finite-mass formulas degenerate cleanly: the wall never moves."),
          ("CHECK", "energy check on wall rebound at 45 degrees, $e = 0.8$: $K_f/K_i = 0.5 + 0.64\\times0.5 = 0.82$; direct: $(v\\sin45)^2 + (0.8 v\\cos45)^2 = v^2(0.5+0.32) = 0.82 v^2$.")]),
     CX('h3', CH, "2-D collision drills",
       ["(a) 3 kg at 5 m/s along $x$ hits 2 kg at rest; line of impact along $x$ (head-on): back to 1-D, $e = 1$: $v_1 = (3-2)5/5 = 1$ m/s, $v_2 = 2\\cdot3\\cdot5/5 = 6$ m/s. (b) Same but the line of impact is at 60 degrees to $x$ (glancing): normal components: $u_{1n} = 2.5$, $u_{1t} = 4.33$; keep the general formulas along $n$ and add back $u_{1t}$ to $v_{1t}$.",
          "(c) Ball at 10 m/s at 30 degrees to a smooth floor's normal, $e = 0.75$: rebound normal $= -0.75\\times8.66 = -6.5$; tangential $= 5$ unchanged; departure angle $= \\arctan(5/6.5) = 37.6$ degrees from the normal (more grazing than 30). (d) Two 1 kg spheres, one moving at 4 m/s, impact parameter such that $\\phi = 45$ degrees, elastic: shooter leaves at 2.83 m/s perpendicular to the centre line; target at 2.83 m/s along it.",
          ("CHECK", "drill (c) energy: $K_f/K_i = (25+42.25)/100 = 0.6725$; formula $\\sin^2 30 + e^2\\cos^2 30 = 0.25 + 0.5625(0.75) = 0.672$ - agree to rounding.")]),
]), "Line of impact decomposition; tangential invariance; wall and incline cases; drills.")

# ---------------------------------------------------- CM-12 the equal-mass 90 degree result
ADD('CM-12', CHUNK([
    CX('h2', HEAD, "Equal masses, elastic, target at rest: the velocities separate at 90 degrees",
       ["Theorem: if two equal-mass smooth spheres collide elastically and one is initially at rest, their velocity vectors after the collision are perpendicular: $\\theta_1 + \\theta_2 = 90$ degrees (angles measured from the original direction). Proof in two lines: momentum $m\\mathbf{u} = m\\mathbf{v}_1 + m\\mathbf{v}_2$ gives $\\mathbf{u} = \\mathbf{v}_1 + \\mathbf{v}_2$; elastic KE conservation gives $u^2 = v_1^2 + v_2^2$. Dot the momentum result with itself: $u^2 = v_1^2 + v_2^2 + 2\\mathbf{v}_1\\cdot\\mathbf{v}_2$. Comparing: $\\mathbf{v}_1\\cdot\\mathbf{v}_2 = 0$ - perpendicular. Done. Note the masses cancel in the first equation because they are EQUAL - that is the whole scope condition.",
          "Speeds from the scatter angle: $v_1 = u\\cos\\theta_1$, $v_2 = u\\sin\\theta_1$ where $\\theta_1$ is the shooter's deflection (since $\\theta_2 = 90 - \\theta_1$ and the triangle of momenta is right-angled with hypotenuse $mu$). Worked (source E6): deflection $30$ degrees: $\\theta_2 = 60$ degrees; $v_1 = u\\cos30 = 0.866u$; $v_2 = u\\sin30 = 0.5u$. Momentum-x: $0.866u\\cos30 + 0.5u\\cos60 = 0.75u + 0.25u = u$; momentum-y: $0.866u\\sin30 = 0.433u = 0.5u\\sin60 = 0.433u$.",
          "Scope and failure modes: (i) unequal masses: NOT 90 degrees - $\\theta_1 + \\theta_2 < 90$ degrees when $m_1 > m_2$, and the shooter's angle is capped at $\\arcsin(m_2/m_1)$ (OLY-02); (ii) $e < 1$: KE drops, the dot-product step fails, the angle is NOT 90 degrees; (iii) rough spheres: tangential impulses change the perpendicular components; (iv) head-on ($\\theta_1 = 0$): the shooter stops - the 1-D limit (CM-08).",
          ("WHY", "the dot-product proof works because momentum conservation gives a VECTOR triangle and elasticity gives its SIDE LENGTHS: a right triangle is the only triangle with $a^2 + b^2 = c^2$. Any violation of the theorem's conditions breaks one of those two inputs."),
          ("CHECK", "source P33: deflection 45 degrees: $\\theta_2 = 45$; $v_1 = v_2 = u/\\sqrt{2} = 0.707u$; KE: $2\\times\\frac{1}{2}m(0.5u^2) = \\frac{1}{2}mu^2$ conserved. The equal-angle 45-45 split is the symmetric member of the family.")]),
     CX('h3', HEAD, "Reading exam questions on the 90-degree rule",
       ["'Two identical balls, one at rest, elastic, smooth: find the angle between their paths' - 90 degrees, done in one line, no numbers needed. 'One is deflected by 30 degrees: find the other's angle and both speeds' - $\\theta_2 = 60$, speeds $u\\cos30$ and $u\\sin30$ (source E6, Q6). 'The collision is NOT smooth (friction): what happens to the 90 degrees?' - it fails: friction transfers tangential impulse, and (source P33c) the collision may still be elastic ($e = 1$) but directions change; the angle can open or close.",
          "Variant: BOTH balls moving initially - transform to the CM frame first (CM-15): in CM the elastic collision reverses both velocities; transform back. The 90-degree rule is the $u_2 = 0$ special case of that picture. Variant: unequal masses - use the general oblique recipe (CM-11) and let the numbers decide; the angle between the exits is the sum of the two deflections and no compact closed form is worth memorising: keep the equal-mass theorem and the CM frame instead.",
          ("CHECK", "spot-check the momentum triangle: $\\mathbf{u} = \\mathbf{v}_1 + \\mathbf{v}_2$ means the two exit vectors, placed tip to tail, span the original vector exactly. For the 30-60 case: $v_1$ at 30 degrees $= (0.75, 0.433)u$; $v_2$ at $-60$ degrees $= (0.25, -0.433)u$; sum $= (1, 0)u$.")]),
     CX('h3', CH, "Common mistakes around the theorem",
       ["Mistake 1: applying it when masses are merely SIMILAR - no: exact equality is the hypothesis. Mistake 2: applying it with $e < 1$ - no. Mistake 3: assuming one ball MUST stop - only in 1-D; in 2-D both move with $u\\cos\\theta_1$, $u\\sin\\theta_1$ except at $\\theta_1 = 0$ or 90 degrees. Mistake 4: measuring the angle from the wrong axis - the theorem states the angle BETWEEN the two exit velocities, not each vs the incoming line (though $\\theta_1 + \\theta_2 = 90$ uses those two deflections).",
          "Mistake 5 (from source P5's ambiguity): 'after the collision the incoming ball stops' - TRUE in 1-D elastic equal-mass (exchange), FALSE in 2-D (deflected). The question 'which happens after the collision' must state the dimension; the safe exam sentence: 'in 1-D the velocities exchange; in 2-D they separate at 90 degrees'.",
          ("WHY", "the two statements are the same theorem's two limits: the momentum triangle degenerates to a line in 1-D, and the right angle degenerates to the exchange."),
          ("CHECK", "memorise the one-line proof; regenerating it in 30 seconds beats remembering a formula sheet entry.")]),
     CX('h3', CH, "Drills on the 90-degree family",
       ["(a) Deflection 37 degrees (3-4-5 triangle!): $\\theta_2 = 53$; $v_1 = 0.8u$, $v_2 = 0.6u$. (b) Target twice the mass, elastic: NOT 90 degrees; solve CM-11 style: $v_{1n} = (1-2)/3\\,u_n = -u_n/3$ along the normal, tangential unchanged. (c) Equal masses but $e = 0.5$, head-on: $v_1 = u/4$ from master: $(1-0.5)/2\\,u = 0.25u$; $v_2 = 1.5/2\\,u = 0.75u$; angle between them is 0 or 180 (they are collinear) - no 90-degree rule.",
          ("CHECK", "drill (a): $0.8^2 + 0.6^2 = 1$ - the speed triangle closes on $u$. Drill (c): $e$-check $(0.75-0.25)/1 = 0.5$."),
          ("FN", "in particle physics the same theorem appears in cloud-chamber photographs: equal-mass proton tracks meeting at 90 degrees were used to IDENTIFY the particle as a proton.")]),
]), "Perpendicular-exit theorem via the momentum triangle; scope limits; drills.")

# ---------------------------------------------------- CM-13 ballistic pendulum and two-stage problems
ADD('CM-13', CHUNK([
    CX('h2', HEAD, "The two-stage protocol: momentum first, energy second",
       ["Any collision-then-motion problem splits into stages with DIFFERENT conservation laws. Stage 1 (the collision, duration milliseconds): momentum conserved (no external impulse); energy NOT conserved (deformation heat). Stage 2 (the motion afterwards: swing, slide, spring): energy conserved (smooth; only conservative forces); momentum NOT conserved (gravity/tension/spring force is external). The order is fixed: never use energy across the collision, never use momentum across the swing. Write each stage's equation, then chain them through the shared velocity.",
          "Ballistic pendulum (source E5): bullet mass $m$ at $v_0$ embeds in a hanging block $M$. Collision: $mv_0 = (m+M)V$, so $V = \\dfrac{m v_0}{m+M}$. Swing: $\\frac{1}{2}(m+M)V^2 = (m+M)gh$, so $V = \\sqrt{2gh}$. Chain: $v_0 = \\dfrac{m+M}{m}\\sqrt{2gh}$. Worked numbers (source E5): $m = 10$ g, $M = 2$ kg, $v_0 = 400$ m/s: $V = 4/2.01 = 1.99$ m/s; $h = V^2/2g = 3.96/20 = 0.198$ m (about 20 cm).",
          "Reverse problems: given $h$, find $v_0$: $V = \\sqrt{2gh}$ then $v_0 = \\frac{m+M}{m}V$. Source Q12: 5 g bullet, 1 kg block, $h = 0.1$ m: $V = \\sqrt{2} = 1.414$ m/s; $v_0 = (1.005/0.005)(1.414) = 284$ m/s. Source P29: 10 g, 2 kg, $h = 0.05$ m: $V = 1$ m/s; $v_0 = (2.01/0.01)(1) = 201$ m/s; energy lost in the collision: 202 J down to 1.005 J = 99.5% (stage 1 is violently inelastic).",
          ("WHY", "the collision time is short so gravity's impulse $mg\\Delta t$ is negligible - momentum is the right stage-1 law. The swing time is long and the forces are conservative - energy is the right stage-2 law. Mixing them (energy across the embed, momentum across the swing) is the classic examiner trap."),
          ("CHECK", "always audit the chain at the shared velocity: if a problem gives $v_0$ and $h$, compute $V$ both ways and demand equality. E5: $V = 1.99$ from momentum; $V = \\sqrt{2\\times10\\times0.198} = 1.99$.")]),
     CX('h3', HEAD, "Bullet-through-block: two final velocities, one momentum law",
       ["When the bullet EXITS the block (source Q19): 0.01 kg at 500 m/s passes through a 1 kg block at rest and leaves at 200 m/s. One equation fixes the block: $0.01(500) = 0.01(200) + 1(v)$, $v = 3$ m/s. There is no restitution equation to use here (the contact history is complex: entry deformation, exit fracture); momentum alone answers. The energy audit: $K_i = 1250$ J, $K_f = 200 + 4.5 = 204.5$ J; $1045.5$ J went into heat, sound and deformation.",
          "If the block then slides on a rough floor: third stage - work-energy with friction: $\\frac{1}{2}Mv^2 = f d$ finds the stopping distance. If it compresses a spring: $\\frac{1}{2}Mv^2 = \\frac{1}{2}kx_{max}^2$ (CM-14). The protocol generalises: stage 1 momentum; stage 2 energy with whichever conservative/resistive forces apply; sometimes a stage 3.",
          "Trap: the ballistic-pendulum formula $v_0 = \\frac{m+M}{m}\\sqrt{2gh}$ ASSUMES the bullet stays in. If a problem says 'emerges', 'passes through', 'lodges and sticks with extra mass', rewrite stage 1 for that geometry. Same for a bullet that embeds but the block is on a spring (then stage 1 is momentum, stage 2 is spring energy: $\\frac{1}{2}(m+M)V^2 = \\frac{1}{2}kx^2$).",
          ("CHECK", "Q19 momentum audit with signs: bullet direction positive: $5 = 2 + v$; if the bullet had exited BACKWARD at 200: $5 = -2 + v$, $v = 7$ m/s - the sign convention matters more than the numbers.")]),
     CX('h3', CH, "Energy fraction in the ballistic pendulum (the examiner favourite)",
       ["General fraction lost in stage 1: $1 - K_f/K_i = 1 - \\frac{m}{m+M} = \\frac{M}{m+M}$ (using $V = \\frac{m}{m+M}v_0$: $K_f = \\frac{1}{2}\\frac{m^2 v_0^2}{m+M}$, so $K_f/K_i = \\frac{m}{m+M}$). For $M \\gg m$: nearly ALL the bullet's KE dies in the block - P29's 99.5%. The retained fraction $m/(m+M)$ keeps the pair moving; the rest is heat and deformation.",
          "Stage 2 then loses nothing (smooth swing) but converts KE to PE. The height reached is $h = \\frac{m^2 v_0^2}{2g(m+M)^2}$. For a given $h$, larger $M$ means larger $v_0$ measurement sensitivity - the practical ballistic pendulum: measure $h$, get $v_0$ with the factor $(m+M)/m$ (a 200x amplification for 10 g in 2 kg).",
          ("WHY", "the fraction $M/(m+M)$ is the inelastic energy ledger of CM-09 in disguise: $K_{loss} = K_{rel} = \\frac{1}{2}\\mu u_{rel}^2$ with $\\mu \\approx m$, $u_{rel} \\approx v_0$; $K_i \\approx \\frac{1}{2}m v_0^2$; ratio $\\approx 1$."),
          ("CHECK", "P29 fraction: $M/(m+M) = 2/2.01 = 99.5$% exactly the published number. E5: $\\frac{1}{2}(0.01)(160000) = 800$ J in; lost $= 796$ J; $K_f = \\frac{1}{2}(2.01)(3.96) = 3.98$ J - consistent.")]),
     CX('h3', CH, "Two-stage drills",
       ["(a) 0.02 kg bullet at 300 m/s embeds in 1.98 kg block: $v = 3$ m/s (source P22); if the block hangs on a 0.8 m string, max angle: $h = v^2/2g = 0.45$ m; $\\cos\\theta = 1 - h/L = 0.4375$, $\\theta = 64.1$ degrees. (b) Bullet 5 g at 600 m/s through 1 kg block, exits at 100: $3 = 0.5 + v$, $v = 2.5$ m/s; then the block compresses $k = 500$ N/m spring: $x = v\\sqrt{M/k} = 2.5\\sqrt{1/500} = 0.112$ m.",
          "(c) 2 kg ball at 3 m/s hits 1 kg at rest with $e = 0.6$; then the 1 kg slides against friction $\\mu = 0.2$: $v_2 = 1.6(2)(3)/3 = 3.2$ m/s; friction stop distance: $d = v^2/(2\\mu g) = 10.24/4 = 2.56$ m.",
          ("CHECK", "drill (a) angle: $h = 0.45$, $L = 0.8$: $1 - 0.45/0.8 = 0.4375$; $\\arccos(0.4375) = 64.1$ degrees. Always recompute $h = v^2/2g$ from the stage-1 speed first.")]),
]), "Ballistic pendulum protocol; bullet-through-block; energy fraction M/(m+M); drills.")

# ---------------------------------------------------- CM-14 blocks, springs and post-collision energy
ADD('CM-14', CHUNK([
    CX('h2', HEAD, "Collision then spring: which compression is larger, sticking or elastic?",
       ["Standard problem (source P35): block $m$ at $v_0$ slides into block $M$ attached to a spring ($k$); find the maximum spring compression for (a) perfectly inelastic contact, (b) elastic contact. (a) Sticking: $mv_0 = (m+M)V$, $V = mv_0/(m+M)$; then $\\frac{1}{2}(m+M)V^2 = \\frac{1}{2}kx^2$: $x_{in} = \\dfrac{m v_0}{\\sqrt{k(m+M)}}$. (b) Elastic: target leaves the collision at $v_2 = \\dfrac{2m}{m+M}v_0$; then $\\frac{1}{2}M v_2^2 = \\frac{1}{2}kx^2$: $x_{el} = \\dfrac{2m v_0 \\sqrt{M}}{(m+M)\\sqrt{k}}$.",
          "Compare: $\\dfrac{x_{el}}{x_{in}} = 2\\sqrt{\\dfrac{M}{m+M}}$. So elastic compresses the spring MORE only when $2\\sqrt{M/(m+M)} > 1$, i.e. $4M > m+M$, i.e. $3M > m$. The source's answer 'the elastic collision gives more compression' is CONDITIONAL, not universal: if $m > 3M$ the STICKING case compresses more (sticking transfers $\\frac{m}{m+M}$ of the KE in one lump; elastic gives the light target $\\frac{4mM}{(m+M)^2}$ of the initial KE - compare these fractions directly).",
          "KE fractions check: sticking pair compressing the spring carries $K = \\frac{m}{m+M}K_i$. Elastic target carries $K = \\frac{4mM}{(m+M)^2}K_i$. Ratio of spring energies $= \\frac{4M}{m+M} = (x_{el}/x_{in})^2$ consistent with the amplitude ratio. Equality at $M = m/3$ exactly.",
          ("WHY", "the boundary $M = m/3$ is where the two delivery mechanisms cross: elastic fires the target at up to $2v_0$ but leaves the shooter's KE behind; sticking carries everything together at $v_{cm}$ - for a very light target, riding along beats being fired."),
          ("CHECK", "numbers: $m = 2$, $M = 1$, $k = 500$, $v_0 = 3$: $x_{in} = 6/\\sqrt{1500} = 0.155$ m; $x_{el} = 12/67.08 = 0.179$ m; ratio $= 1.155 = 2\\sqrt{1/3}$. Since $M = 1 > 2/3 = m/3$, elastic wins here.")]),
     CX('h3', HEAD, "Spring released between two blocks (source Q18, corrected)",
       ["2 kg and 3 kg blocks rest on a smooth floor with a compressed spring ($k = 100$ N/m compressed $x = 0.2$ m) between them; released, find the speeds. Momentum: $2v_1 + 3v_2 = 0$, so $v_2 = -2v_1/3$. Energy: $\\frac{1}{2}(100)(0.04) = 2$ J $= \\frac{1}{2}(2)v_1^2 + \\frac{1}{2}(3)v_2^2 = v_1^2 + \\frac{3}{2}v_2^2$. Substitute $v_2 = -2v_1/3$: $\\frac{3}{2}\\cdot\\frac{4}{9}v_1^2 = \\frac{2}{3}v_1^2$; so $2 = v_1^2 + \\frac{2}{3}v_1^2 = \\frac{5}{3}v_1^2$: $v_1 = \\sqrt{6/5} = 1.095$ m/s, $v_2 = 2(1.095)/3 = 0.730$ m/s.",
          "Corrections to the source solution (recorded in SOURCE-AUDIT): the source wrote the second KE term as $3\\times4v_1^2/9 = 4v_1^2/3$ - it dropped the factor $\\frac{1}{2}$ in $\\frac{1}{2}(3)v_2^2$ - and concluded $v_1^2 = 6/7$, $v_1 = 0.926$, $v_2 = 0.617$. Those speeds fail the energy audit: $\\frac{1}{2}(2)(0.857) + \\frac{1}{2}(3)(0.381) = 1.43$ J $\\ne 2$ J. The corrected pair: $\\frac{1}{2}(2)(1.2) + \\frac{1}{2}(3)(0.533) = 2.0$ J exactly the spring energy.",
          ("WHY", "the two-block spring release is just an explosion in disguise: internal forces only, zero total momentum, all spring energy converted to KE of the pair. The split of energy is INVERSELY mass-weighted: lighter block takes more KE ($K_1/K_2 = m_2/m_1$); the momentum split is directly mass-weighted ($v_1/v_2 = -m_2/m_1$)."),
          ("CHECK", "the general check: $U = \\frac{1}{2}\\mu v_{rel}^2$ with $\\mu = 6/5 = 1.2$: $v_{rel} = \\sqrt{2U/\\mu} = \\sqrt{4/1.2} = 1.826$ m/s $= v_2 - v_1 = 0.730 + 1.095 = 1.825$.")]),
     CX('h3', CH, "Spring-compression variants that appear in exams",
       ["(1) Bullet into block attached to spring (P35 with embedding): stage 1 momentum, stage 2 spring energy. (2) Block slides down a ramp into the spring-block: energy through the ramp THEN collision THEN spring - three stages. (3) Two blocks, one spring, one moving (as above). (4) Block hits a SPRING directly and sticks to it - not a collision problem at all: pure SHM with amplitude from energy $\\frac{1}{2}mv_0^2 = \\frac{1}{2}kA^2$.",
          "(5) Collision ONTO a spring-mounted target with $e$: maximum compression is NOT at the end of the contact - during contact the spring compresses further while restitution works; the clean exam route: after separation the target's KE compresses the spring again (detached spring) or, for an ATTACHED spring, the max compression occurs when the two bodies share a velocity (instantaneous rest frame) - solve momentum + energy at that instant.",
          ("FN", "attached-spring + elastic-contact problems converge to SHM of the relative coordinate with reduced mass $\\mu$ and spring $k$; keep the reduced-mass oscillator as the fallback method."),
          ("CHECK", "variant (4): block 0.5 kg at 4 m/s on $k = 200$: KE $= \\frac{1}{2}(0.5)(16) = 4$ J; $A = v\\sqrt{m/k} = 4\\sqrt{0.0025} = 0.2$ m; $\\frac{1}{2}kA^2 = 100(0.04) = 4$ J - consistent.")]),
     CX('h3', CH, "Post-collision energy drills",
       ["(a) 1 kg at 5 m/s sticks to 2 kg against $k = 100$: $V = 5/3$; $x = V\\sqrt{3/100} = 1.667(0.173) = 0.289$ m. (b) Same elastic: $v_2 = 2(5)/3 = 3.33$; $x = 3.33\\sqrt{2/100} = 3.33(0.141) = 0.471$ m; ratio $= 1.633 = 2\\sqrt{2/3}$ ($M = 2 > 1/3$, elastic wins). (c) Q18-corrected pair (1.095, 0.730) rechecked above.",
          "Trap: computing max compression from the SHOOTER's KE after an elastic collision (the shooter may rebound and never touch the spring). Trap: forgetting the spring is attached (sticking) vs detached (target flies off after contact). Trap: using $mv_0 = (m+M)V$ when the bullet exits (use Q19 form).",
          ("CHECK", "drill (a) energy: $K_f = \\frac{1}{2}(3)(2.78) = 4.17$ J; $\\frac{1}{2}kx^2 = 50(0.0835) = 4.17$.")]),
]), "Spring compression after collisions; the 3M > m condition; corrected Q18; drills.")

# ---------------------------------------------------- CM-15 the centre-of-mass frame
ADD('CM-15', CHUNK([
    CX('h2', HEAD, "The CM frame: where collisions become trivial",
       ["The CM (centre-of-mass) frame moves with $\\mathbf{v}_{cm} = \\dfrac{m_1\\mathbf{u}_1 + m_2\\mathbf{u}_2}{m_1+m_2}$. In that frame the total momentum is ZERO by construction: $m_1\\mathbf{u}'_1 + m_2\\mathbf{u}'_2 = 0$, so $\\mathbf{u}'_2 = -\\frac{m_1}{m_2}\\mathbf{u}'_1$ - the two bodies always approach (or recede) along one line, equal and opposite momenta. The frame is inertial before and after the collision (COM velocity changes only under external impulse) - so Newton's laws hold in it.",
          "Elastic collisions in the CM frame are TRIVIAL: the velocities simply reverse direction (speeds unchanged: $|\\mathbf{u}'_i| = |\\mathbf{v}'_i|$; directions flipped along the line of impact). Reason: momentum zero means the momenta reverse (any other outcome would need internal energy change); elasticity keeps the speeds. In 2-D the reversal happens along the line of impact while the common rotation of both vectors by the scattering angle is free - the magnitude statement is $|v'_i| = |u'_i|$ with direction changed.",
          "Energy decomposition: $K = \\frac{1}{2}M v_{cm}^2 + \\frac{1}{2}\\mu v_{rel}^2$ - the CM-frame KE is $K_{rel} = \\frac{1}{2}\\mu v_{rel}^2$ where $\\mu = m_1m_2/(m_1+m_2)$ and $v_{rel} = |\\mathbf{u}_1 - \\mathbf{u}_2|$. First term = the KE of the COM motion (untouchable); second = the KE of relative motion (the collision's play money). For $m_1 = m_2 = m$: $\\mu = m/2$, $M = 2m$: $K = m v_{cm}^2 + \\frac{m}{4}v_{rel}^2$ - check with $u_2 = 0$: $v_{cm} = u/2$, $v_{rel} = u$: $K = m u^2/4 + m u^2/4 = mu^2/2$.",
          ("WHY", "why the decomposition is exact: $\\sum \\frac{1}{2}m_i v_i^2 = \\frac{1}{2}M v_{cm}^2 + \\frac{1}{2}\\mu v_{rel}^2$ for two bodies is the parallel-axis theorem for kinetic energy - expand $\\mathbf{v}_i = \\mathbf{v}_{cm} + \\mathbf{v}'_i$ and the cross terms vanish because $\\sum m_i \\mathbf{v}'_i = 0$."),
          ("CHECK", "source P36(a-b): derive the decomposition (done); CM KE is unchanged by the collision because momentum conservation leaves $v_{cm}$ fixed. The lab-frame velocities are just $\\mathbf{v}_i = \\mathbf{v}_{cm} + \\mathbf{v}'_i$ - transform back and you have solved any collision by inspection.")]),
     CX('h3', HEAD, "The CM-frame recipe for 2-D scattering",
       ["Recipe: (1) compute $\\mathbf{v}_{cm}$ and the CM velocities $\\mathbf{u}'_i = \\mathbf{u}_i - \\mathbf{v}_{cm}$; (2) in CM the collision reverses/rotates the velocities (elastic: reverse the relative velocity along the line of impact; keep magnitudes); (3) transform back $\\mathbf{v}_i = \\mathbf{v}_{cm} + \\mathbf{v}'_i$. For a target at rest, $u'_1 = \\frac{m_2}{m_1+m_2}u$, $u'_2 = -\\frac{m_1}{m_1+m_2}u$ - approach speeds in CM are INVERSELY mass-weighted.",
          "The equal-mass 90-degree rule (CM-12) is one line in this language: $\\mathbf{v}_{cm} = \\mathbf{u}/2$; after reversal $\\mathbf{v}_1 = \\mathbf{u}/2 + \\mathbf{w}$, $\\mathbf{v}_2 = \\mathbf{u}/2 - \\mathbf{w}$ with $|\\mathbf{w}| = u/2$ (speeds in CM preserved); $\\mathbf{v}_1\\cdot\\mathbf{v}_2 = u^2/4 - w^2 = 0$ perpendicular. ANY elastic equal-mass collision with a resting target lands on this circle of radius $u/2$ around $\\mathbf{u}/2$ - the locus of possible exit velocities is a circle (useful for maximum/minimum questions!).",
          "Max-deflection questions: the shooter's exit velocity $\\mathbf{v}_1 = \\mathbf{v}_{cm} + \\mathbf{v}'_1$ is the sum of a fixed vector and a vector of fixed length $\\frac{m_2}{m_1+m_2}u$ at variable angle. The extreme directions are tangent to that circle - this gives the maximum scattering angle (the OLY-02 formula $\\theta_{max} = \\arcsin(m_2/m_1)$ for $m_1 > m_2$ in one geometric picture).",
          ("CHECK", "work E6 in CM: $u = v_0$ along $x$; $v_{cm} = v_0/2$; CM speeds $v_0/2$ each. Shooter deflected 30 in lab at speed $0.866 v_0$: $\\mathbf{v}_1 = (0.75, 0.433)v_0$; $\\mathbf{v}_1 - \\mathbf{v}_{cm} = (0.25, 0.433)v_0$ with length $0.5 v_0$ matches CM speed. Target: $\\mathbf{v}_2 = \\mathbf{v}_{cm} + \\mathbf{v}'_2 = (0.5,0) + (-0.25, -0.433) = (0.25, -0.433)v_0$; length $= 0.5 v_0$ - both CM speeds preserved.")]),
     CX('h3', CH, "CM language for explosions and multi-body problems",
       ["Explosion: all fragments' momenta sum to $M\\mathbf{v}_{cm}$; in the CM frame they scatter with zero total momentum. For three equal masses: momentum triangle closes (CM-03). For n fragments, the CM frame is where you compute the minimum/maximum possible speed of one fragment: e.g. two fragments fly off with momenta $\\mathbf{p}, -\\mathbf{p}$ in CM; lab speeds span $|v_{cm} \\pm p/m|$.",
          "Collisions of more than two bodies: pairwise with $e$ bookkeeping; the CM frame of the PAIR is the natural frame per contact. A ball bouncing between two moving walls: use the wall's frame for each bounce (CM-21), then compose velocities.",
          ("FN", "the relativistic generalisation keeps the same structure: $K = \\gamma_{cm}Mc^2 + K_{rel}$; the CM frame is still where total momentum vanishes. The non-relativistic decomposition suffices for JEE/Olympiad classical problems."),
          ("CHECK", "invariant audit: $v_{cm}$ is the same before and after any internal rearrangement; $K_{cm}$ likewise. If a computation changes $K_{cm}$, the momentum bookkeeping is wrong.")]),
     CX('h3', CH, "CM-frame drills",
       ["(a) 2 kg at 6 m/s hits 1 kg at 2 m/s head-on, elastic: $v_{cm} = (12+2)/3 = 14/3 = 4.667$ m/s; CM speeds: $u'_1 = 6 - 4.667 = 1.333$, $u'_2 = 2 - 4.667 = -2.667$; after reversal: $v'_1 = -1.333$, $v'_2 = 2.667$; lab: $v_1 = 3.333$, $v_2 = 7.333$ m/s. Master-formula check: $v_1 = [(2-1)6 + 2(1)(2)]/3 = 3.333$; $v_2 = [2(2)(6) + (1-2)2]/3 = 7.333$.",
          "(b) Explosion of 4 kg at 10 m/s into 1 kg and 3 kg: $v_{cm} = 10$; CM momenta $\\pm p$; lab speeds $10 \\pm p/m$. If the 1 kg piece gets $v = 13$ in lab: $p = 1(3) = 3$; 3 kg piece: $10 - 1 = 9$ m/s.",
          ("CHECK", "drill (a) energies: $K_i = 36 + 2 = 38$; $K_f = \\frac{1}{2}(2)(11.11) + \\frac{1}{2}(1)(53.78) = 11.11 + 26.89 = 38$ - the CM frame never lies.")]),
]), "CM frame definition; velocity reversal for elastic; energy decomposition; circle locus; drills.")

# ---------------------------------------------------- CM-16 variable mass I: sand, belts, hoppers
ADD('CM-16', CHUNK([
    CX('h2', HEAD, "Picking mass up and throwing it down: F = m_dot v",
       ["A conveyor belt runs at speed $v$; sand falls on it at rate $\\dot m$ (kg/s) with zero horizontal velocity. To carry the sand, the belt must deliver to each kilogram the momentum $v$: force $F = \\dot m v$. Worked (source E7): $\\dot m = 5$ kg/s, $v = 2$ m/s: $F = 10$ N. Power delivered by the motor: $P = Fv = \\dot m v^2 = 20$ W. But the sand's KE grows at only $\\frac{1}{2}\\dot m v^2 = 10$ W. The missing 10 W is heat - friction between sand and belt scatters the KE as the grains slide to rest in the belt frame.",
          "The factor-2 is universal for inelastic pickup from rest: belt power $= \\dot m v^2$, KE rate $= \\frac{1}{2}\\dot m v^2$, heat rate $= \\frac{1}{2}\\dot m v^2$. Examiners love the 'where does the other half go' question (source E7/P34): answer: sliding friction heat at the pickup (and if the sand is thrown OFF the belt at the far end, that KE is carried away with the sand - different audit!).",
          "Cart collecting sand (OLY-10): a cart of mass $M$ rolling at $v$ on a smooth floor collects rain/sand falling vertically at $\\dot m$: horizontal momentum is conserved (vertical rain has none), so $Mv = (M + \\dot m t)v(t)$: $v(t) = \\dfrac{M v_0}{M + \\dot m t}$ - the cart slows. A cart that LEAKS sand vertically: $v$ constant (the dropped sand takes its own momentum); a cart REJECTED from a hopper at speed $u$ rel needs thrust $\\dot m(u - v)$ - sign bookkeeping always via momentum of (cart + ejected mass) per $dt$.",
          ("WHY", "the pickup force is momentum flux: mass $\\dot m$ per second crosses from speed 0 to speed $v$; the momentum source is the belt, paid as $\\dot m v$. Same law as the rocket (CM-17) and the falling chain (OLY-01) with different geometries."),
          ("CHECK", "P34(a): $\\dot m = 3$ kg/s at $v = 4$ m/s: $F = 12$ N, $P = 48$ W, KE rate $= 24$ W, heat $= 24$ W - exactly the factor-2 split.")]),
     CX('h3', HEAD, "Sand thrown off: the full belt audit",
       ["If sand lands at rest and leaves the belt at speed $v$ (belt length $L$, speed $v$): power in $\\dot m v^2$; KE out $\\frac{1}{2}\\dot m v^2$ carried away; heat $\\frac{1}{2}\\dot m v^2$. If instead the belt STOPS the sand (sand lands moving at $v$ and the belt brings it to rest): force $= \\dot m v$ still, but now the KE $\\frac{1}{2}\\dot m v^2$ is destroyed entirely - all heat. The audit table depends on in/out speeds; the momentum flux law $F = \\dot m (v_{out} - v_{in})$ never changes.",
          "Hopper onto a cart: $F = \\dot m u$ if the cart must accelerate the sand from rest to its own speed $u$; the cart's engine force $F$ at speed $u$ delivers $P = \\dot m u^2$ of which half is KE rate - only if the sand starts at rest in the lab. If the sand is thrown forward at $w$ relative to the cart: thrust bookkeeping via the rocket sign discipline (CM-17): the safest exam route is to write momentum of the whole system at $t$ and $t+dt$ and expand.",
          ("CHECK", "cart collecting rain at 0.1 kg/s from 5 m/s at $t = 0$, $M = 20$ kg: at $t = 100$ s: $v = 100/30 = 3.33$ m/s; KE: 250 J to $\\frac{1}{2}(30)(11.1) = 166.7$ J; the 83.3 J lost is the pickup heat, matching the differential identity $\\frac{1}{2}\\dot m v^2 = -\\frac{d}{dt}KE$."),
          ("FN", "the sand-on-belt P = 2 x KE-rate result reappears in fluid jets (OLY-07: F = rho A v^2 on a plate) and the falling chain (OLY-01: flux 2 lambda g x) - one momentum-flux law, many costumes.")]),
     CX('h3', CH, "Variable-mass sign discipline",
       ["The universal recipe: system = (body + the mass being exchanged) over $dt$; write $p(t)$ and $p(t+dt)$; keep every term to FIRST order in $dt$; drop products like $dm\\,dv$. The force on the body: $F_{on\\,body} = \\dot m_{in} u_{in} - \\dot m_{out} u_{out}$ (momentum brought in minus carried out) plus external forces. For the rocket: $m\\,dv = -v_e\\,dm$ with $dm < 0$ (mass lost) - signs set by the exhaust velocity RELATIVE to the body.",
          "Traps: (1) using the sand's speed instead of the RELATIVE speed for rockets (CM-17); (2) forgetting the sand carries momentum away when it leaves a cart (that IS the retarding force on leaky carts); (3) assuming energy conservation anywhere in these problems - variable-mass pickup is dissipative by nature.",
          ("CHECK", "leaky cart: $M$ moving at $v$ leaks at $\\dot m$ vertically down. Horizontal momentum of cart: the leaked grains keep horizontal speed $v$; the leak takes $\\dot m v$ per second but the cart's remaining momentum per mass stays: $\\dot v = 0$ - $v$ CONSTANT (the classic result: leaking does not slow the cart; loading does).")]),
     CX('h3', CH, "Drills: flux and belt",
       ["(a) Belt 1.5 m/s, sand 2 kg/s: $F = 3$ N, $P = 4.5$ W, KE rate 2.25 W. (b) Rain 0.02 kg/s into a 100 kg cart at 2 m/s: $F = 0.04$ N retarding at first; after 100 s the cart holds 2 kg of water and moves $200/102 = 1.96$ m/s. (c) Water jet 3 kg/s at 8 m/s onto a wall (stops): $F = 24$ N (OLY-07).",
          "(d) Belt problem with friction coefficient given: if the question gives $\\mu$ between sand and belt, the static friction force on the sand is $\\dot m v$ total; belt tension difference equals it - solve as a friction-engineering problem, not a collision.",
          ("CHECK", "drill (b): momentum 200 kg m/s conserved; total mass 102; $v = 1.9608$; KE: initial 200 J; final $\\frac{1}{2}(102)(3.845) = 196.1$ J; lost 3.9 J = pickup heat.")]),
]), "F = m_dot v; belt power split; cart pickup and leak; sign discipline; drills.")

# ---------------------------------------------------- CM-17 variable mass II: the rocket equation
ADD('CM-17', CHUNK([
    CX('h2', HEAD, "Delta v = v_e ln(m0/m_f): the rocket equation",
       ["Derivation in the lab frame (source 3.9-3.10): rocket mass $m$, speed $v$; in time $dt$ it ejects mass $-dm > 0$ at exhaust speed $v_e$ RELATIVE to the rocket (backward), so exhaust lab speed $= v - v_e$. Momentum conservation for rocket + exhaust (no external impulse): $mv = (m + dm)(v + dv) + (-dm)(v - v_e)$. Expand: $mv = mv + m\\,dv + v\\,dm + dm\\,dv - v\\,dm + v_e\\,dm$; cancel and drop the second-order $dm\\,dv$: $m\\,dv + v_e\\,dm = 0$, so $dv = -v_e\\,dm/m$. Integrate from $m_0$ to $m_f$: $\\Delta v = v_e \\ln\\dfrac{m_0}{m_f}$.",
          "Reading the formula: $\\Delta v$ depends on the exhaust speed and the MASS RATIO only - not on the burn rate, not on the time profile. Gravity-free, drag-free, constant $v_e$ - those are the assumptions (state them). With gravity acting upward during vertical climb: $dv = -v_e dm/m - g\\,dt$ and the integral gains $-g t_{burn}$. Thrust: $F = \\dot m v_e$ with $\\dot m = |dm/dt|$ (source Q25: $\\dot m = 2$ kg/s at 3000 m/s: $F = 6000$ N).",
          "Numbers (source E10): $v_e = 3$ km/s, $m_0/m_f = 10$: $\\Delta v = 3\\ln 10 = 3(2.303) = 6.91$ km/s - orbit-class. Source Q8: need $\\Delta v = 4$ km/s with $v_e = 2$ km/s: $m_0/m_f = e^{2} = 7.39$. Source P24: $v_e = 2500$, $\\Delta v = 5000$: $m_0/m_f = e^2 = 7.39$. Note the answer to 'how much fuel' is EXPONENTIAL in the mission $\\Delta v$ - the tyranny of the rocket equation.",
          ("WHY", "why no air is needed: the rocket pushes on its own exhaust, not on the atmosphere. Source P16: rockets work in vacuum. The momentum ledger is closed: every bit of forward momentum of the rocket is paid by backward exhaust momentum."),
          ("CHECK", "the limit $m_0/m_f = e$ gives $\\Delta v = v_e$ (about 63% of the launch mass is propellant); $m_f \\to m_0$ (no fuel) gives $\\Delta v = 0$; doubling $m_0/m_f$ adds $v_e \\ln 2 \\approx 0.69 v_e$ - logarithmic, not linear.")]),
     CX('h3', HEAD, "Thrust and power; the burn-rate freedom",
       ["Thrust $F = \\dot m v_e$ is independent of rocket speed (in the rocket's frame the exhaust leaves at $v_e$ regardless). Power delivered to the ROCKET: $P = Fv = \\dot m v_e v$ (speed-dependent!); the exhaust KE rate is $\\frac{1}{2}\\dot m v_e^2$ - both are frame-dependent bookkeeping; the invariant statement is momentum flux. In the instantaneous rest frame of the rocket, the exhaust carries away KE $\\frac{1}{2}\\dot m v_e^2$ in that frame.",
          "Multi-burn problems: apply $\\Delta v = v_e \\ln(m_{start}/m_{end})$ per stage/burn and ADD the $\\Delta v$s (they are speed increments along the path; for collinear burns). Two-stage rockets (OLY-06): the real gain is dropping dead structure; with ZERO structural mass any split gives the same $\\Delta v = v_e \\ln(M/M_p)$.",
          ("FN", "with gravity: $\\Delta v = v_e \\ln(m_0/m_f) - g t_b$ for a vertical burn of duration $t_b$; the gravity loss is why real launches turn downrange quickly."),
          ("CHECK", "Q25 audit: thrust 6000 N on 1000 kg initial gives $a = 6$ m/s$^2$ at burn start - half a g; the mass falls as fuel burns so acceleration grows. Sign check: $dm < 0$; $-v_e dm/m > 0$ speeds up.")]),
     CX('h3', CH, "The variable-mass ledger for exams",
       ["Choose system: rocket + exhaust (closed). Write momentum at $t$ and $t + dt$. Keep first order. Integrate. Assumptions to state: (1) $v_e$ constant relative to the rocket; (2) exhaust collinear; (3) no external impulse (or add $g$ term); (4) all mass ejected is propellant. The same ledger solves sprinklers (water leaving a cart), sand hoppers (CM-16) and jetpacks.",
          "Sprinkler-on-a-cart: cart mass $M$ (with water), ejects at $\\dot m$ at $v_e$ rel: same equation $M dv = v_e (-dM)$ if no external force; the cart accelerates like a rocket until the water runs out. Fire-extinguisher recoil: treat the spray as exhaust with $v_e$ = spray speed relative to the cylinder.",
          ("WHY", "the rocket equation is just $F = dp/dt$ for a system with flowing mass: $p = mv$ differentiates to $m\\,dv + v\\,dm$; the exhaust takes the $v\\,dm$ term away at speed $v - v_e$ so the leftover is $m\\,dv + v_e\\,dm = 0$."),
          ("CHECK", "extinction case: $m_f = m_0/2$: $\\Delta v = v_e \\ln 2 = 0.69 v_e$; half the mass as fuel gives only 0.69 exhaust-speeds - the classic 'rockets are inefficient' table entry.")]),
     CX('h3', CH, "Rocket drills",
       ["(a) $v_e = 2$ km/s, fuel 80% of mass: $m_0/m_f = 5$: $\\Delta v = 2\\ln 5 = 3.22$ km/s. (b) Need 9 km/s with $v_e = 3$: $m_0/m_f = e^3 = 20.1$ - 95% fuel. (c) Thrust 20 kN at $\\dot m = 50$ kg/s: $v_e = 400$ m/s. (d) A 5 kg cart with a 2 kg spring-loaded mass shot at 6 m/s rel: cart + remaining 3 kg at $v$; ejected 2 kg at $v - 6$; momentum: $0 = 3v + 2(v-6) = 5v - 12$; $v = 2.4$ m/s.",
          ("CHECK", "drill (d) energy: cart KE $= \\frac{1}{2}(3)(5.76) = 8.64$ J; ejecta KE $= \\frac{1}{2}(2)(3.6^2) = 12.96$ J; total 21.6 J from the spring. Momentum $= 7.2 - 7.2 = 0$.")]),
]), "Rocket equation derivation; thrust; assumptions; multi-burn and drills.")

# ---------------------------------------------------- CM-18 momentum flux: chains and jets
ADD('CM-18', CHUNK([
    CX('h2', HEAD, "Chains and jets: momentum flux is m_dot v on top of the carried weight",
       ["Chain lifted at constant speed $v$ from a pile on the ground (source P34c, Q13 family): at the moment a length $x$ hangs clear, the force at the top must (1) support the hanging weight $\\lambda x g$ and (2) supply the momentum flux to jerk each stationary link up to speed $v$: $F = \\lambda x g + \\lambda v^2$ with $\\lambda = M/L$. P34(c) with $M = 2$ kg, $v = 3$ m/s, $g = 10$: $F = (2/L)(10x + 9)$ N. The source's Q13 (mass 3 kg at 2 m/s) is under-specified without $L$ or $x$ - the general formula is the answer (recorded in SOURCE-AUDIT).",
          "Energetics of the lift (the exam's 'where does the work go'): power delivered $P = Fv = \\lambda x g v + \\lambda v^3$. Rate of PE growth $= \\frac{d}{dt}(\\frac{1}{2}\\lambda x^2 g) = \\lambda x g v$ matches the weight term. Rate of KE growth $= \\frac{d}{dt}(\\frac{1}{2}\\lambda x v^2) = \\frac{1}{2}\\lambda v^3$. So HALF the flux work $\\lambda v^3$ becomes KE and HALF is dissipated jerking the links from rest to $v$ at the pickup (inelastic). The pile itself does no work: pickup happens at zero displacement - the chain links at rest are accelerated by tension acting over vanishing displacement; the energy audit closes only with the pickup heat included.",
          "Water jet on a fixed plate (OLY-07, source OL9): jet speed $v$, area $A$, density $\\rho$: mass rate $\\dot m = \\rho A v$; the horizontal momentum is destroyed (splatters sideways): $F = \\dot m v = \\rho A v^2$. At angle $\\theta$ to the plate surface: only the normal component $v\\sin\\theta$ dies: $F_n = \\rho A v^2 \\sin\\theta$. Moving plate at $u$ (same direction as jet): relative speed $v - u$: $F = \\rho A (v-u)^2$ - the flux law always uses relative speed (details in OLY-07).",
          ("WHY", "one law: $F = \\frac{dp}{dt} = \\dot m \\Delta v$. When mass arrives at rest and is carried at $v$: $\\Delta v = v$; when a jet dies on a plate: $\\Delta v = v$; when a chain is jerked: $\\Delta v = v$; when a rocket ejects: $\\Delta v = v_e$. Every flux problem is this multiplication with a diagram."),
          ("CHECK", "jet numbers: $A = 5$ cm$^2$, $v = 20$ m/s, $\\rho = 1000$: $\\dot m = 10$ kg/s, $F = 200$ N - about 20 kg-weight, a fire-hose kick.")]),
     CX('h3', HEAD, "Chain landing on a scale (preview of OLY-01)",
       ["A chain segment lands and stops: the flux force stopping it is $\\lambda v^2$ where $v$ is the landing speed. If the segment falls a distance $x$: $v^2 = 2gx$, flux force $= 2\\lambda g x$; plus the landed weight $\\lambda x g$ gives a total $3\\lambda x g$ - the classic result: the scale reads THREE times the landed weight at every instant, ending at $3mg$ when the last link lands. The chain-lift flux $\\lambda v^2$ is the same term seen from above (OLY-01 does the full derivation and the variant geometry).",
          "Exam phrasings to recognise: 'a uniform chain of linear density $\\lambda$ falls onto a scale' vs 'is lifted from a pile at constant speed' vs 'hangs over a smooth peg' (OLY-05) - three geometries, one flux law plus one weight law.",
          ("FN", "the inelastic pickup/landing heat is exactly $\\frac{1}{2}\\dot m v^2$ at every link - the same half-half split as the belt (CM-16)."),
          ("CHECK", "dimension: $\\lambda v^2 = $ kg/m $\\times$ m$^2$/s$^2$ = kg m/s$^2$ = N; $\\lambda x g$ = kg/m $\\times$ m $\\times$ m/s$^2$ = N. Both terms are forces, adding is legitimate.")]),
     CX('h3', CH, "Chain-lift and jet drills",
       ["(a) Chain 4 kg, 2 m long, lifted at constant 3 m/s: when 1.2 m is clear: $F = 2(1.2)(10) + 2(9) = 24 + 18 = 42$ N. (b) Jet $\\rho = 1000$ kg/m$^3$, $A = 3$ cm$^2$, $v = 15$ m/s on a wall: $F = \\rho A v^2 = 1000(3\\times10^{-4})(225) = 67.5$ N. (c) Jet at 60 degrees to a plate surface: $F_n = \\rho A v^2 \\sin 60 = 0.866\\,\\rho A v^2$; at 30 degrees to the surface: $0.5\\,\\rho A v^2$ - the angle is measured to the SURFACE so that the normal component is $v\\sin\\theta$.",
          "(d) Belt at 4 m/s with 6 kg/s sand from rest: $F = 24$ N; $P = 96$ W; KE rate 48 W; heat 48 W (CM-16 again). (e) Chain falling onto a scale: reading $= 3\\lambda x g$ at landed length $x$ (OLY-01).",
          ("CHECK", "drill (a): $\\lambda = 2$; $F = \\lambda x g + \\lambda v^2 = 24 + 18 = 42$ N. Drill (b): $\\dot m = \\rho A v = 1000(3\\times10^{-4})(15) = 4.5$ kg/s; $F = \\dot m v = 4.5\\times15 = 67.5$ N - the $\\rho A v^2$ form and the $\\dot m v$ form agree exactly.")]),
     CX('h3', CH, "Which flux problem is which",
       ["Classification table. Chain lifted: weight + flux; half the flux work heats the pickup. Chain landing: landed weight + flux; reading up to 3x weight. Jet on plate: pure flux $\\rho A v^2$; on a moving plate use relative speed. Belt pickup: flux $\\dot m v$; belt power $\\dot m v^2$. Rocket: flux $\\dot m v_e$ = thrust. Rain into cart: retarding flux. In every case draw the control volume first - what crosses the boundary, at what velocity - then write $\\dot m \\Delta v$.",
          ("WHY", "the control-volume picture is what the fluid-mechanics chapter will formalise as the momentum equation; here it is Newton's second law with a flow diagram."),
          ("CHECK", "re-derive the universal form: mass $dm$ crosses with velocity $u_{in}$ and leaves/absorbs at $u_{out}$; force $= \\frac{dm}{dt}(u_{out} - u_{in})$ - every entry in the table is this with substituted speeds.")]),
]), "Flux law F = m_dot v; chain lift with pickup heat; jets; drills and classification.")

# ---------------------------------------------------- CM-19 systems with internal motion
ADD('CM-19', CHUNK([
    CX('h2', HEAD, "Man on a boat: the COM stays fixed, the parts slide apart",
       ["System: man ($m$) + boat ($M$), initially at rest on frictionless water. No external horizontal force, so the horizontal COM stays FIXED: $m x_m + M x_b = $ const. If the man walks a distance $d$ RELATIVE to the boat, then $x_m - x_b = d + $ const and the ground displacements satisfy $m s_m + M s_b = 0$ with $s_m - s_b = d$. Solve: $s_m = \\dfrac{M d}{m+M}$ (man's ground displacement), $s_b = -\\dfrac{m d}{m+M}$ (boat slides the other way).",
          "Worked (source E8): 60 kg man walks 3 m on a 120 kg boat: $s_m = 120(3)/180 = 2$ m forward; $s_b = -60(3)/180 = -1$ m: the boat moves 1 m opposite. Total check: $60(2) + 120(-1) = 0$ (COM fixed); $s_m + |s_b| = 3 = d$ (the relative walk fully accounted for). Source Q10: 60 kg person JUMPS at 3 m/s relative to the boat: momentum $0 = 60(3 + v_b) + 120 v_b$ (person lab speed $= 3 + v_b$): $180 + 180 v_b = 0$, $v_b = -1$ m/s - the boat recoils at 1 m/s.",
          "Traps: (1) confusing ground displacement with relative displacement - $s_m = Md/(m+M)$ assumes $d$ is measured relative TO THE BOAT; (2) the boat's displacement is opposite; (3) total momentum is zero but the parts' momenta are not; (4) if the water is NOT frictionless, external horizontal friction moves the COM and the fixed-COM shortcut dies.",
          ("WHY", "the COM line stays vertical-fixed because no horizontal external force acts; every internal shuffle trades equal opposite momenta: $m v_m = -M v_b$ at every instant; integrate and the displacements follow."),
          ("CHECK", "source P20: all three statements true: COM fixed; boat opposite; man ground displacement $Md/(m+M)$ with $d$ relative to the boat.")]),
     CX('h3', HEAD, "Block on a movable wedge - the same COM law in 2-D",
       ["Block ($m$) slides down a movable wedge ($M$) on a smooth table: horizontal momentum of block\\wedge is conserved (gravity and the table normal are vertical; the block-wedge normal pair is internal). The horizontal COM stays fixed: as the block descends and moves right relative to the wedge, the wedge slides left so that $m x_b + M x_w = $ const. Vertical momentum is NOT conserved (the floor's normal force and gravity do not cancel).",
          "Constraint version: if the block slides a relative horizontal distance $s_{rel}$ along the wedge: $s_{block} = \\frac{M}{m+M}s_{rel}$, $s_{wedge} = -\\frac{m}{m+M}s_{rel}$ - the same formula as the boat. The geometry is identical whenever horizontal external impulse is zero. For a wedge of incline angle $\\alpha$ and slide length $L$ along the incline: $s_{rel} = L\\cos\\alpha$.",
          "Energy: for the wedge problem energy IS conserved (smooth): $mgh = \\frac{1}{2}mv_b^2 + \\frac{1}{2}Mv_w^2$ with the constraint $v_{bx} = v_{wx} + v_{rel\\,x}$ - a two-equation solve. For the boat walk energy is NOT conserved (muscles); use momentum/COM only. The wedge problem is the standard 'both conservation laws, different stages' exam question.",
          ("CHECK", "mass-ratio sanity: $M \\gg m$: the wedge barely moves and the block does almost all the sliding; $m \\gg M$: the block barely moves and the wedge does almost all the sliding. Both limits pass through the same formula.")]),
     CX('h3', CH, "Internal-motion drills",
       ["(a) 80 kg woman walks 4 m on a 40 kg raft: $s_{raft} = -80(4)/120 = -2.67$ m; $s_{woman} = 1.33$ m. (b) Two skaters 50 and 70 kg push apart to a relative 3 m/s: $50v_1 = 70v_2$ and $v_1 + v_2 = 3$: $50(3-v_2) = 70v_2$, $v_2 = 1.25$ m/s, $v_1 = 1.75$ m/s. (c) Man 60 kg on a 120 kg boat jumps off at 4 m/s relative to the boat: $0 = 60(4+v_b) + 120v_b$: $v_b = -240/180 = -1.33$ m/s.",
          "(d) Block 1 kg on a 3 kg wedge slides 0.5 m along the incline (30 deg): relative horizontal $= 0.433$ m; wedge shift $= 1(0.433)/4 = 0.108$ m opposite.",
          ("CHECK", "drill (c) energy: person KE $= \\frac{1}{2}60(2.67^2) = 213$ J; boat KE $= \\frac{1}{2}(120)(1.78) = 107$ J; total 320 J = the muscle energy of the jump - momentum zero, energy positive, no contradiction.")]),
     CX('h3', CH, "When the COM is NOT fixed: external horizontal forces",
       ["If external horizontal forces act (water drag, floor friction, a rope pull), the COM accelerates: $M\\mathbf{a}_{cm} = \\mathbf{F}_{ext}$. Example: the man-walks-on-boat problem with water drag $f$ opposing the boat: the fixed-COM displacement formula $s_b = -md/(m+M)$ becomes an approximation for short walks; the exact solve is momentum plus the drag impulse. Rule: state the no-external-impulse condition BEFORE using the fixed-COM shortcut.",
          "Drill: woman 80 kg walks 2 m on a 40 kg raft against a constant 12 N drag: during a 1 s walk the COM drifts by $\\frac{1}{2}a_{cm}t^2 = \\frac{1}{2}(0.1)(1) = 0.05$ m - a small correction, but the exam answer should name it. Drift check: $a_{cm} = 12/120 = 0.1$ m/s$^2$.",
          ("CHECK", "if the drag is proportional to speed, the COM decelerates exponentially (OLY-11 Pattern 1) - the displacement formula then needs the drag integral, not a linear correction.")]),
]), "Man on boat and block on wedge; COM-fixed displacements; drills.")

# ---------------------------------------------------- CM-20 bouncing balls: restitution kinematics
ADD('CM-20', CHUNK([
    CX('h2', HEAD, "Bounce heights: e = sqrt(h2/h1) and the geometric ladder",
       ["A ball dropped from $h_1$ rebounds to $h_2$ on a fixed floor: impact speed $v = \\sqrt{2gh_1}$, rebound speed $ev$, so $h_2 = e^2 h_1$ and $e = \\sqrt{h_2/h_1}$. Source Q5: dropped from 5 m, bounces to 3.2 m: $e = \\sqrt{0.64} = 0.8$. Source P10: rebounds to 64%: $e = 0.8$ again. The height ratio is $e^2$, never $e$ - the classic trap (drop height 4 m, $e = 0.5$: rebound 1 m, not 2 m).",
          "Successive bounces (source P25/OL4): $h_n = e^{2n} h_0$ after $n$ bounces. $e = 0.7$ from 10 m: $h_3 = 10(0.7)^6 = 10(0.1176) = 1.176$ m. The heights form a geometric sequence with ratio $e^2$; the velocities with ratio $e$; the bounce times with ratio $e$ (since $t = \\sqrt{2h/g} \\propto e^n$).",
          "Total distance (source P31): $d = h + 2h(e^2 + e^4 + \\cdots) = h\\frac{1+e^2}{1-e^2}$. For $h = 5$, $e = 0.6$: $d = 5(1.36/0.64) = 10.625$ m. Total time: $t = t_0 + 2t_0(e + e^2 + \\cdots) = t_0\\frac{1+e}{1-e}$ with $t_0 = \\sqrt{2h/g}$: $h = 5$, $g = 10$: $t_0 = 1$ s; $t = 1(1.6/0.4) = 4$ s. The two series differ (heights decay by $e^2$, times by $e$) - memorise which is which.",
          ("WHY", "each bounce is a floor collision with $e$ defined on speeds; $h \\propto v^2$ turns the speed ratio $e$ into the height ratio $e^2$. The geometric series follow because the process is self-similar: every bounce reproduces the previous one scaled."),
          ("CHECK", "P31(b): how many bounces until $h_n < 0.1$ m from 5 m with $e = 0.6$: $5(0.36)^n < 0.1$, $0.36^n < 0.02$, $n > \\ln(0.02)/\\ln(0.36) = 3.83$: so after 4 bounces ($h_4 = 5(0.36)^4 = 0.084$ m). The source's printed answer '5' used $|\\ln 0.01|$ by mistake; 4 suffices (recorded in SOURCE-AUDIT).")]),
     CX('h3', HEAD, "Series sums and the energy ladder",
       ["Energy after $n$ bounces: $E_n/E_0 = h_n/h_0 = e^{2n}$. The energy ladder decays by $e^2$ per bounce; total energy dissipated to the floor over infinite bounces $= E_0$ (everything eventually). For $e = 0.8$, after 5 bounces: $0.8^{10} = 0.107$ - about 11% of the original energy remains (source OL4).",
          "Distance sum traps: (i) the FIRST drop counts once ($h$, not $2h$); (ii) each later height counts twice (up and down); (iii) if the ball is thrown DOWN initially, the first impact speed is larger: $v = \\sqrt{v_0^2 + 2gh}$ and the first rebound height is $e^2(v_0^2+2gh)/2g$. Time sums similar: first drop $t_0$ once, later flights $2 t_0 e^k$.",
          "Bounce on a slope: the same $e$ applies to the normal component; the ball hops along the incline with a geometric series in $e^2$ along the normal - distances along the slope form their own series. Out of scope except olympiad geometry (OLY-04 family).",
          ("CHECK", "sum check: $d = h\\frac{1+e^2}{1-e^2}$ at $e = 0$: $d = h$ (just the drop); at $e \\to 1$: $d \\to \\infty$ (perpetual bouncing). $t = t_0\\frac{1+e}{1-e}$ at $e = 0$: $t = t_0$.")]),
     CX('h3', CH, "Bounce drills",
       ["(a) Drop 3.2 m, rebound 1.8 m: $e = \\sqrt{0.5625} = 0.75$. (b) $e = 0.5$ from 8 m: $h_1 = 2$ m, $h_2 = 0.5$ m; $d = 8(1.25/0.75) = 13.33$ m; $t_0 = \\sqrt{16/10} = 1.265$; $t = 1.265(1.5/0.5) = 3.8$ s. (c) $e = 0.9$: after 3 bounces energy $= 0.9^6 = 0.531$ of original - over half remains.",
          "(d) Thrown down at 6 m/s from 5 m: first impact $v = \\sqrt{36+100} = 11.66$ m/s; with $e = 0.8$ rebound speed 9.33 m/s, height 4.35 m. (e) How many bounces to reach 1% height with $e = 0.7$: $0.49^n = 0.01$: $n = \\ln 0.01/\\ln 0.49 = 6.46$: 7 bounces.",
          ("CHECK", "drill (b) distance ladder: $8 + 2(2 + 0.5 + 0.125 + ...) = 8 + 2(2.667) = 13.33$ - matches the closed form.")]),
     CX('h3', CH, "Bouncing-ball question types",
       ["Type A: find $e$ from heights (one ratio). Type B: find $e$ from a TIME ratio (use $t \\propto e^n$). Type C: total distance/time (closed forms). Type D: 'after how many bounces is h below X' (log solve - watch the source's P31 rounding). Type E: energy after n bounces ($e^{2n}$). Type F: ball on a moving lift/platform (use relative speed in the restitution law - CM-21/OLY-04).",
          "Trap: using $e$ instead of $e^2$ for heights. Trap: including the drop twice in distance sums. Trap: forgetting the rebound time on the way up AND down for intermediate bounces. Trap: applying $e = \\sqrt{h_2/h_1}$ when the floor MOVES (then $e$ relates relative speeds, not heights).",
          ("CHECK", "self-consistency: from $h_1, h_2$ alone compute both $e$ and the ratio $h_3 = e^2 h_2$; if a problem gives three heights, they must satisfy $h_2^2 = h_1 h_3$ (geometric middle) - e.g. Q23's 10, 6.4, 4.1: $6.4^2 = 40.96$ vs $10\\times4.1 = 41$ (rounding: $e = 0.8$ exactly gives 4.096).")]),
]), "e = sqrt(h2/h1); geometric bounce ladder; distance and time series; corrected P31(b); drills.")

# ---------------------------------------------------- CM-21 moving walls and moving platforms
ADD('CM-21', CHUNK([
    CX('h2', HEAD, "Bouncing off a MOVING wall: the wall's speed enters the restitution law",
       ["A wall moves at speed $v_w$; a ball with velocity $v_{before}$ (signed, same axis) bounces with restitution $e$ measured in RELATIVE speeds: $v_{after} - v_w = -e(v_{before} - v_w)$. Solve: $v_{after} = v_w - e(v_{before} - v_w)$. In the wall's frame it is an ordinary bounce (relative velocity reverses, scaled by $e$); transform back by adding $v_w$.",
          "Worked (source E9, with the source's own check-block error corrected): ball at 10 m/s toward a wall coming toward it at 5 m/s, $e = 0.8$. Take the ball's direction positive: $v_{before} = +10$, $v_w = -5$. Relative approach: $10 - (-5) = 15$ m/s. $v_{after} = -5 - 0.8(15) = -17$ m/s: the ball rebounds at 17 m/s - FASTER than it came in, because the wall's KE paid the difference. The source's 'Check' block says 7 m/s (a sign slip: it used $v_{after} - v_w = +12$ instead of $-12$); the source's own solution block reaches the correct 17 m/s. Recorded in SOURCE-AUDIT.",
          "Source Q14: 1 kg ball at 3 m/s toward a wall moving toward it at 2 m/s, $e = 0.5$: $v_{after} = -2 - 0.5(5) = -4.5$ m/s: rebounds at 4.5 m/s. General lesson: a wall approaching at $u$ adds roughly $(1+e)u$ to the rebound speed; a receding wall subtracts it. Superball limit ($e = 1$, wall speed $u$ toward a ball at $v$): rebound $= v + 2u$ - the famous 'bounce off a moving train' boost.",
          ("WHY", "restitution measures the relative speed of separation over approach AT THE CONTACT. The wall's motion changes both. Applying $e$ to lab speeds is the classic error - the formula $v_{after} - v_w = -e(v_{before} - v_w)$ encodes the frame change in one line."),
          ("CHECK", "E9 energy sanity (1 kg ball): KE grew from $\\frac{1}{2}(100) = 50$ J to $\\frac{1}{2}(289) = 144.5$ J - no violation; the wall's motor paid. Q14: $\\frac{1}{2}(9) = 4.5$ J to $\\frac{1}{2}(20.25) = 10.125$ J - the approaching wall did work.")]),
     CX('h3', HEAD, "Moving platform (the energy-pump machine)",
       ["A ball bounces on a vertically moving platform (full resonance story in OLY-04). One bounce, up-positive: ball at $v_{before}$ (negative if falling), platform at $v_w$ (positive if rising): $v_{after} = v_w - e(v_{before} - v_w) = (1+e)v_w - e v_{before}$. Platform rising at $u$ meets ball falling at speed $v$: $v_{after} = (1+e)u + e v$ upward - larger than the fixed-floor rebound $ev$: the platform pumped $(1+e)u$ into the ball in one bounce.",
          "Receding platform (falling away at $u$): the rebound weakens the same way. The invariant recipe: relative speeds in the $e$ law, then transform back; never apply $e$ to lab speeds when the surface moves. Elastic platform limit ($e = 1$, rising at $u$): $v_{after} = 2u + v$ - the ball leaves with its own speed plus twice the platform's.",
          ("CHECK", "limit $v_w = 0$: reduces to the fixed-floor law $v_{after} = -e v_{before}$. Elastic head-on ball vs rising platform: relative approach $v + u$; relative separation $v + u$; lab $= (v+u) + u = v + 2u$ - superelastic; platform energy transferred.")]),
     CX('h3', CH, "Wall-collision drills",
       ["(a) Ball at 12 m/s hits a wall receding at 3 m/s (same direction as the ball), $e = 0.9$: $v_{after} = 3 - 0.9(12-3) = 3 - 8.1 = -5.1$ m/s: rebounds at 5.1 m/s - the receding wall 'stole' speed. (b) Ball at 8 m/s meets a wall coming at 6 m/s, $e = 1$: $v_{after} = -6 - 1(8+6) = -20$ m/s: rebounds at 20 m/s. (c) Ball dropped 1.25 m ($v_{before} = -5$ m/s) onto a platform rising at +2 m/s, $e = 0.5$: $v_{after} = 2 - 0.5(-5-2) = 2 + 3.5 = 5.5$ m/s upward - use the formula with signed inputs, not ad-hoc speed arithmetic.",
          ("CHECK", "drill (c) energy audit: ball KE in $= \\frac{1}{2}m(25)$; out $= \\frac{1}{2}m(30.25)$ - the ball gained, the rising platform did work. Drill (b): 32 J to 200 J for 1 kg - the moving wall paid.")]),
     CX('h3', CH, "Bouncing between two walls: compose wall frames",
       ["A ball bouncing between two walls (one or both moving): apply $v' = v_w - e(v - v_w)$ per contact, alternating walls. Between two walls approaching at $u$ each (ball speed $v$ in lab): each bounce adds roughly $(1+e)u$ - the ball heats up like a gas piston; between two receding walls it cools. The wall-frame composition is the olympiad 'bouncing ball in a closing gap' family (OLY-04's fixed-platform cousin).",
          "Drill: ball at 8 m/s between a fixed wall and a wall approaching at 3 m/s, $e = 1$: first bounce off the moving wall: $v' = -3 - 1(8+3) = -14$ m/s toward the fixed wall; off the fixed wall: $+14$; back at the moving wall at 14: $v'' = -3 - 1(14+3) = -20$ m/s - grows by 6 m/s per round trip.",
          ("CHECK", "energy audit per round trip: the approaching wall does work on the ball each bounce; the ball's KE grows - no conservation law is broken (the wall is external and driven).")]),
]), "Moving-wall formula with the source's E9 check-block corrected; platform energy pump; drills.")

# ---------------------------------------------------- CM-22 examiner traps (with two source corrections)
ADD('CM-22', CHUNK([
    CX('h2', HEAD, "The ten examiner traps, sharpened",
       ["(1) Energy conservation across an INELASTIC collision - never; use momentum (and $e$ if given). (2) Applying $e$ to the full velocity - $e$ lives only along the line of impact; tangential components are untouched for smooth bodies. (3) Forgetting the exhaust momentum in rocket problems - the rocket equation IS the exhaust ledger. (4) Using $v_{cm}$ as the velocity of every part after impact - only stuck parts share $v_{cm}$; separated parts do not. (5) Mixing system and particle laws - $M a_{cm} = F_{ext}$ for the system, $F = ma$ for each piece.",
          "(6) Assuming the COM stays fixed when external forces act - fixed only when $\\int F_{ext} dt = 0$ in that direction. (7) Confusing impulse (N s) with force (N) - $J = \\bar F \\Delta t$. (8) Forgetting momentum is a vector - components conserve independently. (9) 'Heavy ball bounces back' - no: the heavy plows on, the light flies at nearly $2u_1 - u_2$. (10) Using the ballistic-pendulum formula when the bullet EXITS - that formula assumes embedding ($e = 0$).",
          ("WHY", "every trap is a broken conservation statement or a broken scope condition. The pre-submission audit (CM-23) checks exactly these.")]),
     CX('h3', HEAD, "Trap 11 (source C9, corrected): equal bounce angles are NOT free",
       ["Source C9 asks: a ball hits a wall at angle $\\theta$ and bounces at angle $\\theta$ - is the collision elastic? The source answers 'not necessarily: the angle of reflection equals the angle of incidence for any smooth-sphere collision regardless of $e$'. That is WRONG for $e < 1$. Correct physics: for a smooth wall the tangential component $v_t$ is unchanged and the normal component becomes $e v_n$. The rebound angle from the normal: $\\tan\\theta' = v_t/(e v_n) = (\\tan\\theta)/e > \\tan\\theta$ for $e < 1$ - the ball leaves MORE GRAZING, not at the mirror angle. Equal angles then imply $e = 1$ exactly (smooth wall, no spin). With friction (rough wall or spinning ball) the tangential impulse also changes $v_t$ and equal angles no longer pin down $e$ - only then is 'not necessarily' fair.",
          "Numbers: impact at 45 degrees from the normal at 10 m/s, $e = 0.5$: $v_t = v_n = 7.07$; the normal part becomes $3.54$: rebound angle $\\arctan(7.07/3.54) = 63.4$ degrees from the normal - far from 45. Energy: $K_f/K_i = \\sin^2 45 + e^2\\cos^2 45 = 0.625$ - visibly not elastic.",
          ("CHECK", "limit $e = 1$: $\\tan\\theta' = \\tan\\theta$ - specular reflection. Limit $e \\to 0$: $\\theta' \\to 90$ degrees - the ball skims the wall (normal motion killed, tangential survives). The formula interpolates physically.")]),
     CX('h3', CH, "Trap 12 (source P5 ambiguity): velocity exchange is 1-D only",
       ["Source P5: 'two equal-mass balls collide elastically, one at rest; after: (a) the incoming ball stops (d) they move at 90 degrees' with answer (a). Correct only in 1-D. In 2-D the general outcome is the 90-degree separation with the shooter deflected at speed $u\\cos\\theta_1$ - it stops only in the head-on limit. Safe exam sentence: 'in 1-D the velocities exchange (shooter stops); in 2-D they separate at 90 degrees and the shooter generally keeps speed $u|\\cos\\theta_1|$'.",
          "Trap 13 (source Q13 under-specification): 'a chain of mass 3 kg is lifted at 2 m/s, find the force' has no unique number without a length scale - the force grows with the hanging length: $F = \\lambda x g + \\lambda v^2$. Answer with the formula (as source P34c does) and define $x$ and $\\lambda = M/L$.",
          ("WHY", "ambiguity traps are scope traps: the statement leaves a free parameter (dimension, length, frame). Name the parameter and answer parametrically - examiners award the method."),
          ("CHECK", "trap 12 numbers: equal masses, shooter at $u$, scatter angle 30: shooter speed $0.866u$ (NOT zero) - one number kills the 'always stops' reading.")]),
     CX('h3', CH, "Sign traps and arithmetic traps",
       ["Sign trap: $e = (v_2-v_1)/(u_1-u_2)$ needs consistent directions; in 2-D project first. Sign trap: the wall formula needs signed velocities; write the axis before numbers. Sign trap: $K_{loss} = K_i - K_f$ comes out negative for superelastic - not an error, a released spring.",
          "Arithmetic trap (documented in SOURCE-AUDIT): in $v_1 = \\frac{(m_1-em_2)u_1 + (1+e)m_2u_2}{m_1+m_2}$ the factor $(1+e)$ multiplies the WHOLE $m_2 u_2$ term. One dropped $\\frac{1}{2}$ in $\\frac{1}{2}(3)v_2^2$ produced the source's Q18 error ($6/7$ instead of $6/5$ for $v_1^2$). Three-invariant audits (momentum, $e$, energy) catch every such slip.",
          ("CHECK", "re-run one old trap against the ledger: 'all KE is lost when things stick'? - NO: $K_{cm} = \\frac{1}{2}Mv_{cm}^2$ survives; equal masses lose exactly half.")]),
]), "Ten standard traps; the wall-angle correction (C9); the 1-D exchange scope (P5); sign and arithmetic discipline.")

# ---------------------------------------------------- CM-23 playbook: triage, validity, audit
ADD('CM-23', CHUNK([
    CX('h2', HEAD, "Triage: route by keyword before touching a number",
       ["'Find the COM' -> definition or negative-mass trick (CM-01/02). 'Explosion / recoil / fragments' -> COM continues, momentum for the pieces (CM-03/05). '1-D collision' -> momentum + $e$, or the master formulas (CM-07/08). '2-D collision / oblique' -> resolve along the line of impact (CM-11/12). 'Ballistic pendulum / bullet-block' -> momentum first, energy second (CM-13). 'Bullet passes through' -> momentum only for the contact (CM-13). 'Spring compression' -> stage bookkeeping then $\\frac{1}{2}kx^2$ (CM-14).",
          "'Rocket / variable mass / jet / belt / chain' -> flux law $\\dot m\\Delta v$ or the rocket equation (CM-16/17/18). 'Man on boat / block on wedge' -> COM fixed in the free direction (CM-19). 'Bounce heights' -> $e = \\sqrt{h_2/h_1}$ ladder (CM-20). 'Moving wall / moving platform' -> relative-speed restitution (CM-21). 'Bouncing between walls' -> wall frames composed (CM-21). 'Maximum / minimum speed after' -> CM-frame circle locus (CM-15/OLY-02).",
          ("WHY", "triage prevents the master sin: applying the wrong conservation law. The keyword names the stage structure; the stage structure names the laws. Every problem in the chapter is one to three stages of (momentum, energy, restitution, flux).")]),
     CX('h3', HEAD, "Validity map: when each formula breaks",
       ["$\\mathbf{R} = \\sum m_i \\mathbf{r}_i/M$: always (definition); continuous bodies need integration. $M\\mathbf{a}_{cm} = \\mathbf{F}_{ext}$: always in Newtonian mechanics (needs third-law pairs). $\\sum \\mathbf{p} = $ const: when net external impulse vanishes in that direction - brief collisions OK by approximation; long pushes not. $e = v_{sep}/v_{app}$: along the line of impact, passive contacts; superelastic allowed with $e > 1$. Master formulas (3.7): 1-D or normal-direction only; fixed masses. $K_{loss} = \\frac{1}{2}\\mu u_{rel}^2(1-e^2)$: same scope; negative means energy gained.",
          "$\\Delta v = v_e \\ln(m_0/m_f)$: constant $v_e$, no external forces (add $-g t_b$ with gravity); collinear exhaust. $v_{after} - v_w = -e(v_{before}-v_w)$: one-dimensional wall contact; smooth. Boat/wedge COM laws: zero external impulse in the tracked direction; frictionless supports. 90-degree rule: equal masses, elastic, smooth, target at rest. Bounce ladder: fixed floor, constant $e$.",
          ("CHECK", "before using any formula, say its validity sentence out loud. If a condition fails, fall back to first principles: momentum ledger + energy ledger + geometry.")]),
     CX('h3', CH, "Pre-submission audit (ten points)",
       ["(1) COM: correct reference point and signed masses. (2) Momentum: asserted why net external impulse is zero (in the relevant direction). (3) Collision classified: elastic / inelastic / sticking, correct $e$. (4) $e$ applied along the line of impact only. (5) Two-stage problems: momentum first, energy second (order locked). (6) Rocket: $\\ln(m_0/m_f)$, not $m_0 - m_f$; $v_e$ relative. (7) 2-D: decomposed along and across the line of impact. (8) Energy loss: $\\mu$ and $u_{rel}$, not raw masses. (9) Units consistent; $g = 9.8$ or 10 as the problem states. (10) Every sub-part answered; signs of final velocities stated as directions.",
          "Time plan for a 3-question collision section: 2 min triage, 3 min per 1-D problem, 5 min for 2-D or two-stage, 2 min audit. COM problems die by definition; collision problems die by momentum + $e$; flux problems die by $\\dot m \\Delta v$.",
          ("CHECK", "the audit's favourite catch: a final velocity reported as a speed when the problem asked for velocity - state direction words ('rebounds at 17 m/s opposite the incoming direction').")]),
     CX('h3', CH, "Mixed-constraint problems: collision plus string, rod or hinge",
       ["When a collision involves a constraint (ball on a string, rod, hinge), the constraint delivers an IMPULSE too: split the impulse into the contact part and the constraint part, or choose coordinates where the constraint impulse does no work (along the string). Example: ball on a string strikes a block: during the impact the string may go slack or jerk - the safe exam route: momentum of the SYSTEM (ball\\block) along the free direction, plus $e$ along the line of impact, plus the string condition (tension $\\ge 0$).",
          "Hinge problems: angular momentum about the hinge is conserved during the collision (the hinge impulse has zero moment arm); linear momentum is not. Ball hitting a hanging rod: $L = I\\omega$ about the pivot, then energy swings the rod - the same two-stage protocol with $I$ in place of $m$.",
          ("CHECK", "the audit: count unknowns (post velocities, constraint impulses) and equations (momentum, $e$, constraint kinematics); if the count mismatches, a physical condition (slack string, hinge direction) is missing.")]),
]), "Triage tree; validity map; pre-submission audit and timing.")

# ---------------------------------------------------- CM-24 results ledger and formula sheet
ADD('CM-24', CHUNK([
    CX('h2', HEAD, "The boxed ledger: six formulas that run the chapter",
       ["$\\mathbf{R} = \\frac{1}{M}\\sum m_i \\mathbf{r}_i$ and $M\\mathbf{a}_{cm} = \\mathbf{F}_{ext}$ (4.1) - the definition and the only equation of motion for a system. $\\mathbf{J} = \\Delta\\mathbf{p} = \\int \\mathbf{F} dt$ (4.2) - impulse equals momentum change. $\\sum\\mathbf{p}_{before} = \\sum\\mathbf{p}_{after}$ when $\\sum\\mathbf{F}_{ext} = 0$ (4.3) - conservation, component-wise.",
          "$e = \\dfrac{v_{sep}}{v_{app}} = \\dfrac{v_2 - v_1}{u_1 - u_2}$ (4.4) - restitution along the line of impact. $K_{loss} = \\frac{1}{2}\\mu(u_1-u_2)^2(1-e^2)$ (4.5) - the energy price of any 1-D collision. $\\Delta v = v_e \\ln\\frac{m_0}{m_f}$ (4.6) - the rocket. Plus the two workhorses: $v_{after} - v_w = -e(v_{before}-v_w)$ (moving wall) and $K = \\frac{1}{2}Mv_{cm}^2 + \\frac{1}{2}\\mu v_{rel}^2$ (CM decomposition).",
          ("WHY", "the ledger is deliberately short: everything else in the chapter is a derived special case or a bookkeeping protocol. If a problem does not reduce to one of these plus geometry, the triage was wrong.")]),
     CX('h3', HEAD, "Limits checklist (each formula, one limit)",
       ["(4.1): $n = 1$ gives $\\mathbf{R} = \\mathbf{r}_1$. (4.2): constant force gives $J = F\\Delta t$. (4.3): switch off external force and $v_{cm}$ freezes. (4.4): $e = 0$ sticks, $e = 1$ elastic. (4.5): $e = 1$ gives zero loss; $e = 0$ gives $\\frac{1}{2}\\mu u_{rel}^2$. (4.6): $m_f = m_0$ gives $\\Delta v = 0$; $m_0/m_f = e$ gives $\\Delta v = v_e$ (63% of the mass is propellant).",
          "Which formula when: mass distribution -> (4.1) or negative mass. Force and time -> (4.2). Collision without external force -> (4.3) + (4.4). Given $e$ and velocities -> energy lost from (4.5). Rocket -> (4.6). Pendulum -> (4.3) then energy. Chain/jet/belt -> $\\dot m \\Delta v$ flux. Boat/wedge -> fixed-COM displacements. Bounce heights -> $e = \\sqrt{h_2/h_1}$.",
          ("CHECK", "final consistency: any collision answer must satisfy three audits - signed momentum, $e$-check, and the energy ledger (surviving $K_{cm}$ + $e^2 K_{rel}$). Any COM answer must shift correctly under a change of origin.")]),
     CX('h3', CH, "One-minute drills on the ledger",
       ["(a) 2 kg at 5 into 2 kg at rest elastic: $v_1 = 0$, $v_2 = 5$ - ledger (4.4) with $m_1 = m_2$. (b) $e = 0.7$ bounce: height ratio 0.49. (c) $\\mu$ for 3 kg and 6 kg: $2$ kg. (d) Rocket 3 km/s exhaust, mass ratio $e$: $\\Delta v = 3$ km/s. (e) Impulse to stop 0.15 kg at 25 m/s: 3.75 N s. (f) Explosion of 8 kg at rest into 5 and 3: 5 kg piece at 3 m/s east -> 3 kg piece at 5 m/s west.",
          "Two-minute version: derive (4.5) from the decomposition; derive (4.6) from momentum in $dt$; prove the 90-degree theorem with a dot product. These three derivations are the olympiad floor and the JEE ceiling - if you can rebuild the ledger, you do not need to memorise it.",
          ("CHECK", "the derivation habit: every boxed formula above appears in the sheets as a derivation with its assumptions. The ledger is the index; the cards are the proof.")]),
     CX('h3', CH, "Rebuild-the-formula drills (60 seconds each)",
       ["(a) Derive $K_{loss} = \\frac{1}{2}\\mu u_{rel}^2(1-e^2)$ from $K = \\frac{1}{2}Mv_{cm}^2 + \\frac{1}{2}\\mu v_{rel}^2$ (CM-09). (b) Derive $\\Delta v = v_e\\ln(m_0/m_f)$ from $m\\,dv = -v_e dm$ (CM-17). (c) Prove the 90-degree rule with $\\mathbf{u} = \\mathbf{v}_1 + \\mathbf{v}_2$ and $u^2 = v_1^2 + v_2^2$ (CM-12). (d) Derive the hole trick $X = \\frac{M_1r_1 - M_2r_2}{M_1 - M_2}$ from negative mass (CM-02).",
          "Each derivation is one algebra chain plus one stated assumption: (a) momentum + $e$; (b) momentum in $dt$, constant $v_e$; (c) momentum + energy + equal masses; (d) superposition of a full body and a negative-mass plug. If you cannot rebuild one in a minute, re-read that sheet's first card.",
          ("CHECK", "the four derivations span the whole ledger: definition (4.1) used in (d), impulse (4.2) in (b), conservation (4.3) in (a) and (c), restitution (4.4) in (a) and (c). Nothing in the chapter outruns them.")]),
]), "Boxed formula ledger; limits; which-formula-when; derivation habit.")

# ---------------------------------------------------- OLY-01 the falling chain on a scale: the 3mg result
ADD('OLY-01', CHUNK([
    CX('h2', HEAD, "The falling chain: the scale reads THREE times the landed weight",
       ["Setup: a uniform chain of mass $m$, length $L$, linear density $\\lambda = m/L$ is released onto a scale (either suspended with its lower end just touching the pan, or lifted as a strand and dropped - the two readings agree, see below). Let $x$ be the length that has LANDED (equal to the distance the chain has fallen). The airborne part moves at $v = \\sqrt{2gx}$; mass arrives at rate $\\dot m = \\lambda v = \\lambda\\sqrt{2gx}$; the impact force stopping it is $\\dot m v = \\lambda v^2 = 2\\lambda g x$. The scale also carries the landed weight $\\lambda x g$. Total: $F = \\lambda x g + 2\\lambda g x = 3\\lambda x g$ - THREE times the weight already on the pan.",
          "At the instant the last link lands ($x = L$): $F = 3\\lambda L g = 3mg$ - the famous three-times-weight reading. Limits: as $x \\to 0$, $F \\to 0$ (nothing on the pan); the reading climbs linearly with $x$; the peak is exactly at the completion of the landing. If instead the chain is dropped from a height $h$ ABOVE the pan in a heap (all links fall together), the reading is a single impulse $J = m\\sqrt{2gh}$ over the collision time, not the smooth $3mg$ ramp - geometry decides the history, but the flux law $\\dot m v$ never changes.",
          "Correction to the source (recorded in SOURCE-AUDIT): source OL1 and its D7.10 brief compute $F = \\lambda(L+x)g$ with $x$ = length still falling and conclude $2mg$ at the end. That bookkeeping pairs the wrong speed with the wrong length (it sets $v = \\sqrt{2g\\ell}$ with $\\ell$ the AIRBORNE length; in fact the airborne speed is $\\sqrt{2g\\times\\text{descent}} = \\sqrt{2g x_{landed}}$). The source README itself advertises the 'three-times-weight result' - the corrected derivation delivers exactly that. Use $F = 3\\lambda x g$ with $x$ = landed length = descent.",
          ("WHY", "the factor 3 = 1 (weight) + 2 (flux): the flux term $\\lambda v^2 = 2\\lambda g x$ is TWICE the landed weight $\\lambda x g$ at every instant because $v^2 = 2gx$ while weight grows as $gx$. Momentum flux is not a small correction here - it dominates."),
          ("CHECK", "units: $3\\lambda x g = 3$(kg/m)(m)(m/s$^2$) = N. Derive the flux term independently: momentum of the falling part changes as links are arrested; force = rate of momentum destruction $= (\\lambda v) v$.")]),
     CX('h3', HEAD, "Variant geometry: the strand lifted from a pile and released",
       ["Variant B (source OL1's words 'piled on a scale, one end lifted and released'): lift a strand (the whole chain) and release. The falling portion descends with $v^2 = 2g y$ where $y$ is the DESCENT (not the airborne length!). Landing rate $\\lambda v$, impact $\\lambda v^2 = 2\\lambda g y$; landed weight $\\lambda y g$ (the landed length equals $y$ when the strand's lower end started at the pan). Then $F = 3\\lambda y g$ again - identical formula with $y$ = descent = landed length. The 3mg endpoint is robust across these geometries.",
          "If instead the whole chain is a heap at rest and simply released from height $H$ above the pan (all links airborne at once): the reading is an IMPULSE spike $J = m\\sqrt{2gH}$ averaged over the short collision, not a smooth ramp - different problem, same momentum bookkeeping. The exam rule: identify what is falling, at what speed, landing at what rate - then $F = $ landed weight $+ \\dot m v$.",
          ("CHECK", "dimensional and limit checks on variant B: $F(y) = 3\\lambda y g$ grows from 0 to 3mg; quasi-static limit: at vanishing fall speed the flux term dies and the pan reads just the landed weight.")]),
     CX('h3', CH, "Why the naive answer is 2mg (and why it fails)",
       ["The tempting wrong bookkeeping: airborne length $\\ell$, speed $\\sqrt{2g\\ell}$ (WRONG pairing: speed follows the FALL DISTANCE, not the remaining airborne length), landed $= L - \\ell$, giving $F = \\lambda(L-\\ell)g + 2\\lambda g \\ell = \\lambda(L+\\ell)g \\to 2mg$. The error: for a strand whose leading end has descended $y$, the airborne portion has length $L - y$ (started as one full strand) and speed $\\sqrt{2gy}$; substituting $\\ell = L - y$ into $\\sqrt{2g\\ell}$ mis-states the speed whenever $y \\ne \\ell$. Only at ONE instant ($y = \\ell = L/2$) do the two agree - which is why the wrong answer survives spot checks at mid-fall.",
          "Sanity probe that exposes it: at $y = L/2$ both give $F = 1.5 mg$ (wrong: $\\lambda(L + L/2)g = 1.5 mg$; right: $3\\lambda(L/2)g = 1.5 mg$); at $y = L$: wrong $2mg$ vs right $3mg$. The ENDPOINT distinguishes them; the 3mg endpoint is the published classic.",
          ("WHY", "the invariant rule: $F = W_{landed} + \\dot m v$ with $\\dot m = \\lambda v$ and $v$ the ACTUAL landing speed measured from the fall distance. One diagram with labelled speeds prevents the pairing error."),
          ("CHECK", "the same 3mg endpoint appears in the equivalent 'chain poured onto a pan at free-fall speed' limit and in the Irodov-style textbook solutions - consistent across treatments.")]),
     CX('h3', CH, "Chain-flux problem set",
       ["(a) Chain 0.5 kg/m falling onto a pan; reading when 0.4 m has landed (g = 10): $F = 3(0.5)(0.4)(10) = 6$ N. (b) At completion ($L = 2$ m, $m = 1$ kg): $F = 3(1)(10) = 30$ N. (c) Same chain held with the end just on the pan and released - same formula. (d) Compare: the same chain RESTING on the pan reads $mg = 10$ N; the falling version peaks at 3x.",
          "(e) Sand falling at constant rate at constant speed (CM-16) reads $W + \\dot m v$; the chain adds the $v^2 = 2gx$ growth. (f) The chain LIFTED at constant speed (CM-18) reads $\\lambda x g + \\lambda v^2$ with $v$ = lift speed (constant) - the weight term grows, the flux term is constant; the falling chain has BOTH growing.",
          ("CHECK", "drill (a): $3\\lambda x g = 3 \\times 0.5 \\times 0.4 \\times 10 = 6$ N; landed weight 2 N; flux 4 N $= 2\\lambda g x$ - the 1:2 split.")]),
]), "Three-times-weight derivation; corrected OL1/D7.10 bookkeeping; variants; problem set.")

# ---------------------------------------------------- OLY-02 CM-frame scattering and deflection limits
ADD('OLY-02', CHUNK([
    CX('h2', HEAD, "Scattering limits: what mass ratios do to the exit angles",
       ["Setup: projectile $m_1$ at speed $u$ hits target $m_2$ at rest; elastic; smooth; deflects at lab angle $\\theta_1$ with target recoil $\\theta_2$. Three regimes. (1) $m_1 < m_2$: the projectile can scatter BACKWARD; $\\theta_1$ ranges over the full $(0, 180)$ degrees - e.g. a neutron off a lead nucleus bounces anywhere. (2) $m_1 = m_2$: $\\theta_1 + \\theta_2 = 90$ degrees exactly (CM-12); $\\theta_1$ itself spans $(0, 90)$. (3) $m_1 > m_2$: the projectile is FORCED FORWARD: $\\theta_1$ is capped at $\\theta_{max} = \\arcsin(m_2/m_1)$ (the circle-locus picture of CM-15: $\\mathbf{v}_1 = \\mathbf{v}_{cm} + \\mathbf{v}'_1$ is the sum of a fixed vector and a vector of fixed length; the extreme direction is tangent to that circle). A bowling ball cannot bounce back off a marble - at best it scatters by $\\arcsin(m_2/m_1)$.",
          "The lab target angle: $\\tan\\theta_2 = \\dfrac{\\sin\\theta_{cm}}{\\cos\\theta_{cm} + m_1/m_2}$ where $\\theta_{cm}$ is the CM-frame scattering angle of the projectile (source OL2's final formula - correct as printed). Consequences: $\\theta_2 = (180 - \\theta_{cm})/2$ when $m_1 = m_2$; $\\theta_2 \\le 90$ degrees always; in the extreme-mass limits $\\theta_2 \\to \\theta_{cm}$ (heavy target) or $\\theta_2 \\to 0$ (light target).",
          "Correction to the source (recorded in SOURCE-AUDIT): source OL2 lists '$\\theta_{max} = \\arcsin(m_2/m_1)$ if $m_1 < m_2$' and 180/90 otherwise. The $\\arcsin$ cap applies when the PROJECTILE IS HEAVIER ($m_1 > m_2$); for $m_1 < m_2$ there is no cap at all ($\\theta_1$ can reach 180). The intermediate values ($\\theta_{max} = 180$ for $m_1 < m_2$; 90 for equality; $\\arcsin(m_2/m_1)$ for $m_1 > m_2$) are the corrected table.",
          ("WHY", "the cap is the tangency of the momentum triangle: $\\mathbf{v}_1 = \\mathbf{v}_{cm} + \\mathbf{v}'_1$ with $v_{cm} = \\frac{m_1}{m_1+m_2}u$ and $v'_1 = \\frac{m_2}{m_1+m_2}u$ (CM speeds). The direction of $\\mathbf{v}_1$ rotates as the impact parameter varies; $\\theta_1$ extremises when $\\mathbf{v}_1$ is tangent to the circle: $\\sin\\theta_{max} = v'_1/v_{cm} = m_2/m_1$ - exactly the condition $m_2 \\le m_1$."),
          ("CHECK", "limit $m_2 \\to m_1$: $\\arcsin(1) = 90$ degrees - the 90-degree theorem's boundary. $m_2 \\ll m_1$: $\\theta_{max} \\to 0$: heavy projectile never deflects. $m_2 > m_1$: the tangent construction fails and every $\\theta_1 \\in (0, 180)$ is reachable.")]),
     CX('h3', HEAD, "Worked: the maximum-deflection geometry",
       ["Head-on elastic against a target of mass $m_2 < m_1$ would send $v_1 = \\frac{m_1 - m_2}{m_1 + m_2}u > 0$ straight through; the MAXIMUM deflection instead occurs at a glancing impact parameter. Method: (1) compute $v_{cm} = \\frac{m_1 u}{m_1+m_2}$, CM speeds $u'_1 = \\frac{m_2 u}{m_1+m_2}$, $u'_2 = -\\frac{m_1 u}{m_1+m_2}$; (2) elastic CM reversal rotates the relative velocity but preserves each CM speed; (3) $\\mathbf{v}_1 = \\mathbf{v}_{cm} + \\mathbf{v}'_1$ traces the circle radius $u'_1$ centred at $v_{cm}$; (4) the deflection angle is extremal at tangency: $\\sin\\theta_{max} = u'_1/v_{cm} = m_2/m_1$; (5) the speed at the tangent point: $v_1 = \\sqrt{v_{cm}^2 - u_1'^2} = u\\frac{\\sqrt{m_1^2 - m_2^2}}{m_1+m_2}$.",
          "Numbers: $m_1 = 2$, $m_2 = 1$, $u = 6$: $v_{cm} = 4$, $u'_1 = 2$; $\\sin\\theta_{max} = 0.5$: $\\theta_{max} = 30$ degrees; $v_1 = \\sqrt{16 - 4} = 3.46$ m/s at that extremum; target flies off at $\\theta_2$ with speed set by the momentum triangle: $\\mathbf{v}_2 = \\mathbf{v}_{cm} + \\mathbf{v}'_2$ with $|v'_2| = 4$; compute $\\theta_{cm}$ from $\\tan\\theta_1 = \\frac{u'_1 \\sin\\theta_{cm}}{v_{cm} + u'_1\\cos\\theta_{cm}}$ (projectile lab angle from the CM decomposition).",
          ("CHECK", "verify the 2:1 numbers via the master formulas at a special impact parameter: head-on $\\theta = 0$: $v_1 = (2-1)6/3 = 2$, $v_2 = 2(2)(6)/3 = 8$ - circle check: $v_1 = |v_{cm} - u'_1| = 2$; opposite extreme $v_1 = v_{cm} + u'_1 = 6$ (zero deflection) - the circle intersects the forward axis at 2 and 6; the deflection extremum is the tangent at 30 degrees - consistent.")]),
     CX('h3', CH, "Olympiad problem patterns (source OL2 family)",
       ["'Find the maximum angle the projectile can be deflected through' -> $\\arcsin(m_2/m_1)$ if heavier, else 180 degrees. 'Find $\\theta_2$ in terms of $\\theta_{cm}$ and masses' -> the $\\tan\\theta_2$ formula. 'Show $\\theta_1 + \\theta_2 = 90$ for equal masses' -> CM-12's dot product. 'Find the impact parameter for maximum deflection' -> the tangent geometry: $b = (R_1+R_2)\\sin\\phi$ with $\\phi$ set by the tangent construction - derive per problem from the circle.",
          "Particle-physics dressing: same math as alpha-particle scattering at fixed energy; the $\\arcsin(m_2/m_1)$ cap is why fast neutrons thermalise efficiently off hydrogen (equal masses, big deflections) and can even backscatter off heavy nuclei ($m_1 < m_2$: full range).",
          ("CHECK", "restated limits table (the corrected version): $m_1 < m_2$: $\\theta_1$ any angle to 180; $m_1 = m_2$: $\\theta_1 + \\theta_2 = 90$; $m_1 > m_2$: $\\theta_1 \\le \\arcsin(m_2/m_1)$. Memorise the table with its regime labels.")]),
     CX('h3', CH, "Drills on the circle locus",
       ["(a) $m_1 = 3$, $m_2 = 1$: $\\theta_{max} = \\arcsin(1/3) = 19.5$ degrees. (b) $m_1 = 1$, $m_2 = 3$: projectile can rebound; the target recoils forward within $\\theta_2 \\le 90$. (c) $m_1 = m_2$, projectile deflected 53 degrees: $\\theta_2 = 37$; $v_1 = u\\cos53 = 0.6u$, $v_2 = u\\sin53 = 0.8u$ (CM-12). (d) Energy check on the tangent point of the 2:1 example: $v_1 = 3.46$; $K_1 = \\frac{1}{2}(2)(12) = 12$ J; target from energy: $m_2 v_2^2 = m_1(u^2 - v_1^2) = 2(36-12) = 48$; $v_2 = \\sqrt{48} = 6.93$; $K_2 = \\frac{1}{2}(1)(48) = 24$ J; total 36 J $= K_i$.",
          ("CHECK", "drill (d) closes the energy circle exactly - the tangent point is a legitimate elastic outcome.")]),
]), "Corrected scattering-limit table; circle-locus geometry; tan(theta2) formula; drills.")

# ---------------------------------------------------- OLY-03 impulse approximation and force pulses
ADD('OLY-03', CHUNK([
    CX('h2', HEAD, "When a finite force acts for a blink: the impulse approximation",
       ["A ball collides with a fixed surface over a short time $\\tau$ with a contact force $F(t)$ that spikes far above every other force in the problem. The impulse approximation: ignore gravity/friction during $\\tau$ and write $J = \\int_0^\\tau F dt = \\Delta p$; then resume the smooth motion with the new velocity. Source OL3: 0.1 kg ball at 10 m/s bouncing elastically off a floor: $J = 2mv = 2$ N s (reversal doubles the momentum swing). If instead the contact force peaks at 1000 N over 2 ms: $J_{contact} = 2$ N s exactly - the pulse alone reverses the ball; gravity's impulse over 2 ms is $mg\\tau = 0.002$ N s, a 0.1% correction. The approximation is honest: state the scale separation.",
          "Source OL3's second half: same ball rolling at 10 m/s stopped by friction $\\mu = 0.5$ in 2 s: impulse $= \\mu mg t = 0.5(1)(2) = 1$ N s - NOT equal to the collision impulse 2 N s because the ball's momentum change is only 1 N s (stops, no reversal). The comparison teaches impulse bookkeeping: $J = |\\Delta p|$ for whatever the actual velocity change is; reversal costs 2mv, stopping costs mv.",
          "Force-pulse problem types: (i) given $F(t)$ shape (rectangular, triangular, half-sine): integrate the shape. (ii) given average force and duration: $\\bar F \\tau = \\Delta p$. (iii) given $F_{max}$ and shape: $J = F_{max} \\tau / k$ with shape factor $k$ (triangle: $J = \\frac{1}{2}F_{max}\\tau$; half-sine: $J = \\frac{2}{\\pi}F_{max}\\tau$). (iv) given a spring stop: use energy instead; the max force is $kx_{max}$ at max compression.",
          ("WHY", "the approximation is a singular perturbation: over $\\tau \\to 0$ the impulse $\\int F dt$ stays finite while the displacement $\\int v dt$ vanishes - positions freeze, velocities jump. This is the mathematical licence for 'collision at a point'."),
          ("CHECK", "self-check on OL3 numbers: $J = 2$ N s vs gravity impulse $0.002$ N s - ratio 1000; state the ratio in an exam answer to justify the approximation. If the pulse lasted 0.2 s instead of 2 ms, gravity's $0.2$ N s would matter - check $mg\\tau \\ll J$ every time.")]),
     CX('h3', HEAD, "Multi-body impulses and constraint impulses",
       ["Two balls colliding with a wall simultaneously: each contact delivers its own $J$; the wall's total impulse is the sum; solve the two pairwise collisions (order irrelevant if contacts are truly simultaneous and independent). A rod on two supports hit at one end: constraint impulses at BOTH supports enter the momentum ledger - solve with momentum + the rigid-body rotation constraint (advanced; olympiad training).",
          "Ball hitting a wedge of finite mass: not a wall - use the two-body master formulas along the line of impact (wedge momentum changes; wedge slides). Ball hitting a SPRING: no impulse approximation - solve the SHM matching. The choice of tool is set by the contact duration and the partner's mobility.",
          ("CHECK", "consistency: for a finite-mass partner, $J$ on the ball and $J$ on the partner are equal/opposite (third law) - if your two $J$s differ, the solution is wrong.")]),
     CX('h3', CH, "Impulse drills",
       ["(a) 0.2 kg ball at 8 m/s hits a wall and rebounds at 6: $J = 0.2(14) = 2.8$ N s. (b) Same ball dropped 1.25 m on concrete ($e = 0.5$): impact $v = 5$; rebound 2.5; $J = 0.2(7.5) = 1.5$ N s. (c) Triangular pulse peaking at 400 N over 6 ms: $J = \\frac{1}{2}(400)(0.006) = 1.2$ N s. (d) Ball 0.15 kg stopped by a 30 N average force: $J = 0.15(25) = 3.75$; $\\tau = 3.75/30 = 0.125$ s.",
          "Trap: using $J = F_{max}\\tau$ for a non-rectangular pulse (overestimates by the shape factor). Trap: forgetting the sign reversal cost $2mv$ vs $mv$. Trap: comparing impulses of contacts with different durations without normalising to $\\Delta p$.",
          ("CHECK", "drill (c) shape factor check: half-sine of same peak and width would give $J = \\frac{2}{\\pi}(400)(0.006) = 1.53$ N s - shape matters by tens of percent.")]),
     CX('h3', CH, "Impulse bounds and force estimates without the pulse shape",
       ["When the force history is unknown, bound it: $J = \\Delta p$ is exact; if the stop distance $d$ is known, the average force satisfies $\\bar F = \\frac{mv^2}{2d}$ (work-energy) - often more useful than the time-average. Example: 0.15 kg ball at 25 m/s stopped in 0.5 m: $\\bar F = \\frac{0.15(625)}{1} = 93.8$ N... precisely $\\frac{mv^2}{2d} = 93.75$ N. Compare with a 30 N average force giving $\\tau = 0.125$ s (the earlier drill) - two different averages of the same impulse.",
          "Shape factors: rectangular pulse $J = F_{max}\\tau$; triangular $J = \\frac{1}{2}F_{max}\\tau$; half-sine $J = \\frac{2}{\\pi}F_{max}\\tau$. If a problem quotes only $F_{max}$, the answer for $J$ must carry the shape assumption explicitly.",
          ("CHECK", "consistency: the time-average and space-average forms must both reproduce $J = \\Delta p$; if your two estimates of $J$ disagree, the assumed shape is inconsistent with the given numbers.")]),
]), "Impulse approximation with scale separation; pulse shapes; multi-body impulses; drills.")

# ---------------------------------------------------- OLY-04 the bouncing machine on a moving platform
ADD('OLY-04', CHUNK([
    CX('h2', HEAD, "Ball on a vertically moving platform: the energy-pump machine",
       ["A platform moves vertically with prescribed speed law $u(t)$; a ball is released above it with restitution $e$ at every contact. One-bounce law (CM-21): up-positive, ball velocity $v$ (negative if falling), platform $u$: $v_{after} = (1+e)u - e v_{before}$. If the platform RISES at $u$ into a ball falling at speed $w$: $v_{after} = (1+e)u + e w$ upward. The platform can therefore pump the ball to arbitrary heights if it keeps rising at the right moments - this is the 'bouncing ball on a piston' machine.",
          "Two regimes. (1) Moving lift at constant speed $U$ (upward): ball dropped in a lift rising at $U$: relative problem in the lift frame: ball speed relative $w$, bounce $ew$; the LAB speed after n bounces grows like a geometric ladder that converges if $e < 1$ to a fixed relative speed where the per-bounce gain $(1+e)U$ balances the per-bounce loss $(1-e)w$: $w_* = \\frac{(1+e)U}{1-e}$ in the platform frame. (2) Oscillating platform: resonance when the platform arrives upward exactly as the ball arrives - phase locking; POGO/springboard questions use this.",
          "The classic exam configuration (source OL6, with the pure bounce ladder in source OL4): platform initially at rest accelerates up at constant $a$ while a ball bounces with $e$; find the speed after n bounces or the conditions for the ball to keep bouncing. Method: time between bounces $t_n = 2v_n/g_{rel}$ (with platform acceleration folded into an effective $g$ in the platform frame: $g_{eff} = g + a$ for a platform accelerating UP); apply the bounce law at each contact; the sequence can be summed if $e$ is constant.",
          ("WHY", "the machine is the olympiad playground for relative-speed restitution: every contact is a one-line map $v \\mapsto (1+e)u - ev$; the composition of maps is where the richness lives. Energy is NOT conserved - the platform's motor does work through the normal force."),
          ("CHECK", "static limit: platform at rest ($u = 0$): $v_{after} = -e v_{before}$; ball on a steadily rising platform in equilibrium: the fixed point of the map $v' = (1+e)U - ev$ is $v = U$ - the ball just rides at the platform speed, bouncing at zero relative speed - physical.")]),
     CX('h3', HEAD, "Worked: ball dropped in a lift rising at constant speed U",
       ["Ball dropped from rest relative to the lift floor; lift rises at $U$ (constant). In the lift frame: ball falls with speed growing as $gt$; hits at relative speed $w = \\sqrt{2gh}$ (h = drop height in the frame); rebounds at $ew$; rises to $e^2 h$; the cycle repeats with $h \\to e^2 h$. In the LAB frame each rebound speed is $U + ew$ (from the map with $v_{before} = U - w$): $v_{after} = (1+e)U - e(U - w) = U + e w$; relative speed up $= ew$ - consistent with the frame picture.",
          "Steady state: the relative speed after bounce is $e^n w_0 \\to 0$ for $e < 1$; the ball settles to riding at $U$ with tiny hops. For $e = 1$: relative speed preserved; the ball keeps bouncing forever at the same relative amplitude, drifting with the lift. Energy in the lab: KE plus PE grows as the lift rises - the motor pays.",
          ("CHECK", "relative-frame audit: every bounce in the lift frame is the textbook fixed-floor bounce with $e$; the lab is a pure velocity shift. If a lab-frame calculation disagrees with the frame-shifted answer, the sign convention broke.")]),
     CX('h3', CH, "Platform-machine drills",
       ["(a) Ball dropped 2 m in a lift rising at 3 m/s, $e = 0.5$, $g = 10$: relative impact speed $w = \\sqrt{40} = 6.32$; lab after $= 3 + 0.5(6.32) = 6.16$ m/s up. (b) Platform rising at 2 m/s meets ball falling at 4 m/s (lab), $e = 0.8$: $v_{after} = (1.8)(2) + 0.8(4) = 6.8$ m/s up. (c) Driven steady relative speed in a lift rising at $U = 1$ with $e = 0.5$: $w_* = \\frac{1.5}{0.5} = 3$ m/s (for periodic kicks; a pure drop decays to 0 instead).",
          "Trap: applying the map with lab speeds and forgetting the $(1+e)u$ platform term. Trap: using $g$ instead of $g + a$ in the platform-accelerating case. Trap: assuming energy conservation anywhere in this machine.",
          ("CHECK", "drill (b) energy sanity: ball KE grew from $\\frac{1}{2}m(16)$ to $\\frac{1}{2}m(46)$ - platform motor did work; momentum is NOT conserved (platform is external).")]),
     CX('h3', CH, "Resonance locking on an oscillating platform",
       ["Platform $u(t) = u_0\\cos\\omega t$; ball released above. Each bounce maps $v \\mapsto (1+e)u(t_n) - e v$ at contact times $t_n$. Phase locking: if the ball always meets the platform rising near its maximum $u_0$, the gain per bounce is maximal $(1+e)u_0 + e w$ - the POGO condition. If the flight time $2v/g$ equals an integer number of platform periods, the phase repeats and the bounce ladder is a clean geometric series.",
          "Numbers: platform $u = 2\\cos(2t)$, ball dropped in phase with the peak: first bounce with $w = 5$, $e = 0.5$: in phase: $(1+e)u + ew = 3 + 2.5 = 5.5$ m/s up. Out of phase (platform at $-u_0$): $v_{after} = -3 + 2.5 = -0.5$ - barely bounces.",
          ("CHECK", "the map's fixed point for constant $u$ is $v = u$ (ride along); for oscillating $u$ there is no fixed point and the amplitude ratchets only when phase-locked - the olympiad question is always about the PHASE.")]),
]), "Bounce map v' = (1+e)u - ev; lift frame solution; energy pump; drills.")

# ---------------------------------------------------- OLY-05 chain sliding over a smooth peg
ADD('OLY-05', CHUNK([
    CX('h2', HEAD, "Chain over a smooth peg: the full solution, including the moment it lets go",
       ["Setup (source OL7): a uniform chain of mass $m$, length $L$ hangs over a frictionless peg with length $x$ on one side and $L - x$ on the other, released from rest at some $x_0 > L/2$. (1) Acceleration: the unbalanced weight is $\\lambda x g - \\lambda(L-x)g = \\lambda g(2x - L)$ on total mass $m = \\lambda L$: $a = \\dfrac{g(2x-L)}{L}$. At $x = L/2$: $a = 0$ (unstable equilibrium); at $x = L$: $a = g$ - the whole chain is in FREE FALL at the end (source OL7's key line). (2) Speed: $v\\,dv = a\\,dx$ gives $v^2 = \\frac{2g}{L}\\left[(x - \\frac{L}{2})^2 - (x_0 - \\frac{L}{2})^2\\right]$; released from rest exactly at $L/2$ plus a nudge, $v^2 = \\frac{2g}{L}(x - \\frac{L}{2})^2$.",
          "(3) Peg force - the part everyone botches. The peg feels the weight $mg$ MINUS the momentum-flux term of the strand going slack: writing the chain's downward momentum $p = \\lambda v(2x - L)$ gives $\\frac{dp}{dt} = 2\\lambda[v^2 + (x-\\frac{L}{2})a] = 4\\lambda v^2$ (consistent substitution), so $F_{peg} = mg - 4\\lambda v^2 = mg\\left[1 - \\dfrac{2(2x-L)^2}{L^2}\\right]$ for the nudge-from-centre release. The peg force DECREASES as the chain accelerates - it does not spike. Contact is lost when $F = 0$: $(2x-L)^2 = L^2/2$, i.e. $x = \\frac{L}{2}\\left(1 + \\frac{1}{\\sqrt{2}}\\right) \\approx 0.854L$; beyond that the chain flies off the peg (formal $F < 0$ is unphysical for a peg that can only push).",
          "Why the folklore '3mg at the end' is wrong for THIS problem: the classic 3mg belongs to the chain LANDED ON A SCALE (OLY-01: weight + landing flux both grow). The sliding peg problem has the opposite structure: the moving chain goes slack against the peg as $a \\to g$; the end-of-motion peg force tends to zero, not to $3mg$. The two chain problems bracket the flux law: onto a pan the flux ADDS to the reading ($\\lambda v^2$ with $v$ of landing); over a peg the flux of the TURNING strand is fed by the chain's own weight and the peg sheds load.",
          ("WHY", "the momentum-ledger method is the only safe route for moving-chain problems: write $p(t)$ for the whole chain, differentiate, equate to $W - F$. Strand-by-strand tension bookkeeping easily double-counts the flux. The source's ODE method ($v\\,dv = a\\,dx$) and the momentum method are the two halves of the complete solution."),
          ("CHECK", "limits: $x = L/2$: $F = mg$, $v = 0$ (static). $x \\to L$: $a \\to g$, $F \\to -mg$ (already detached). Energy: $\\frac{1}{2}m v^2 = $ PE drop: PE $= -\\frac{\\lambda g}{2}[x^2 + (L-x)^2]$; drop from $L/2$ to $x$: $\\Delta PE = -\\lambda g(x - \\frac{L}{2})^2$; KE $= \\lambda g(x-\\frac{L}{2})^2 = \\frac{1}{2}m v^2$ with $v^2 = \\frac{2g}{L}(x-\\frac{L}{2})^2$ - exactly consistent.")]),
     CX('h3', HEAD, "Worked numbers and the released-from-x0 variant",
       ["Chain $m = 1$ kg, $L = 1$ m, $g = 10$, released with $x_0 = 0.75$ m (so $x_0 - L/2 = 0.25$): at $x = 0.9$ m: $v^2 = 20[(0.4)^2 - (0.25)^2] = 20(0.0975) = 1.95$: $v = 1.40$ m/s; $a = 10(2(0.9)-1) = 8$ m/s$^2$; $F = 10[1 - 2(0.8)^2] = -2.8$ N - already detached (contact lost at $x = 0.5(1+0.707) = 0.854$ m, before 0.9). At $x = 0.8$ m: $v^2 = 20[(0.3)^2 - (0.25)^2] = 20(0.0275) = 0.55$: $v = 0.74$ m/s; $F = 10[1 - 2(0.6)^2] = 2.8$ N - still in contact.",
          "Comparison set for exams: (i) chain onto a pan (OLY-01): reading $3\\lambda x g$ to $3mg$ at the end - flux ADDS; (ii) chain over a peg (this sheet): peg force $mg[1 - 2(2x-L)^2/L^2]$, contact loss near the end - flux of the turn is INTERNAL once the chain free-falls; (iii) chain LIFTED at constant speed (CM-18): $\\lambda x g + \\lambda v^2$ - both terms prescribed. The diagram of what flows where decides which of the three structures applies.",
          ("CHECK", "the detachment fraction is geometry-independent of $m$, $g$: $x_{detach}/L = \\frac{1}{2}(1 + 1/\\sqrt{2}) = 0.854$ exactly - a pure number worth quoting in an exam answer as the 'loss of contact' condition.")]),
     CX('h3', CH, "Peg-problem toolkit and drills",
       ["Toolkit: PE of hanging strand length $\\ell$ is $-\\frac{\\lambda g \\ell^2}{2}$ (COM at half depth); energy gives $v^2(x)$; $p = \\lambda v(\\ell_1 - \\ell_2)$ gives the ledger; $F_{peg} = W - dp/dt$; the turn contributes a flux $2\\lambda v^2$ per strand junction when the chain CONTINUES over the peg (e.g. chain poured over a peg into a bucket) - the sign of the flux term depends on whether the strand downstream is pulling or slack.",
          "Drill (a): chain released with $x_0 = 0.6L$: at $x = 0.75L$: $v^2 = \\frac{2g}{L}[(0.25L)^2 - (0.1L)^2] = \\frac{2g}{L}(0.0525L^2) = 0.105 gL$; $F = mg[1 - 2(0.5)^2] = 0.5 mg$. (b) At what $x$ is $v = \\sqrt{gL/2}$? $v^2 = \\frac{2g}{L}(x-\\frac{L}{2})^2 = \\frac{gL}{2}$: $(x - \\frac{L}{2})^2 = \\frac{L^2}{4}$: $x = L$ - only at the very end (for nudge release). (c) Show the chain reaches $a = g$ exactly when it would leave the peg: $F = mg - 4\\lambda v^2$ and $4\\lambda v^2 = mg$ at $x_{detach}$; the free-fall line is approached as contact fades.",
          ("FN", "for a chain FLOWING over a peg into motion on both sides (no slack): $F = W + 2\\lambda v^2$ (flux ADDS) - e.g. the fold-release family of OLY-08. Slack vs pulling downstream is the single most important qualitative judgement in chain problems."),
          ("CHECK", "drill (a): $0.25^2 - 0.1^2 = 0.0525$; $F = 0.5mg$.")]),
     CX('h3', CH, "Tension along the moving chain",
       ["Tension at a point of the moving chain: cut the chain; $T = $ (weight of the part beyond the cut) + (flux of momentum across the cut) + (mass beyond x acceleration). For the peg problem: the strand tension just below the peg is $T = \\lambda g \\ell + \\lambda \\ell a$ for a hanging strand of length $\\ell$ accelerating at $a$ (the strand's own weight plus its acceleration). At the nudge-release with $\\ell = L - x$: $T = \\lambda g(L-x) + \\lambda(L-x)a$.",
          "Drill: $L = 1$, $x = 0.7$ (nudge release): $a = 2g(0.2) = 4$; $\\ell = 0.3$: $T = 0.3(10) + 0.3(4) = 4.2$ N for $\\lambda = 1$ kg/m. The peg force is the sum of the two strand tensions at the peg (which equals $mg - 4\\lambda v^2$ as derived) - the two bookkeepings agree.",
          ("CHECK", "at $x = L/2$ (equilibrium, $v = 0$, $a = 0$): $T = \\lambda g L/2 = mg/2$ each side; the peg holds $mg$ total.")]),
]), "Peg solution: a = g(2x-L)/L, v^2(x), F_peg = mg[1-2(2x-L)^2/L^2], contact loss at 0.854L; corrected folklore.")

# ---------------------------------------------------- OLY-06 two-stage rockets and optimal staging
ADD('OLY-06', CHUNK([
    CX('h2', HEAD, "Why rockets have stages: drop the dead metal",
       ["A rocket stage burns its propellant then throws away its empty tank and engine (structural mass). The next stage starts from a lighter vehicle. Model (source OL8): total mass $M$, payload $M_p$; structural coefficient $\\epsilon = m_{structure}/m_{initial\\,of\\,stage}$; exhaust speed $v_e$. A stage with initial mass $m_i$ burning until $m_f$ gives $\\Delta v = v_e \\ln(m_i/m_f)$; at burnout the empty structure $\\epsilon m_i$ is DISCARDED before the next burn. That discard is what breaks the telescoping of the logs - and it is the entire benefit of staging.",
          "Mass timeline discipline: draw $M_0 \\to$ (burn 1) $\\to m_1 \\to$ (discard structure) $\\to m_2 \\to$ (burn 2) $\\to m_f$. Then $\\Delta v = v_e[\\ln(M_0/m_1) + \\ln(m_2/m_f)]$ with $m_2 = m_1 - m_{structure,1}$. Forget the discard and the two logs telescope to the useless $v_e \\ln(M_0/m_f)$; discard BEFORE burnout and you threw away propellant mass you had not used.",
          "Numbers (source P30 with consistent bookkeeping; the source's printed staging mixes two split conventions - recorded in SOURCE-AUDIT): $M_0 = 1000$ kg, two stages of 400 kg propellant + 50 kg structure each, payload $M_p = 100$ kg: stage 1 burns to 600 kg, discard 50, stage 2 starts at 550, burns to 150: $\\Delta v = v_e[\\ln(1000/600) + \\ln(550/150)] = v_e(0.511 + 1.299) = 1.81 v_e = 5.43$ km/s at $v_e = 3$ km/s. Single-stage with the same total propellant and structure (100 kg kept to the end): $\\Delta v = 3\\ln(1000/200) = 3\\ln 5 = 4.83$ km/s. Staging wins by about 12% with identical hardware.",
          ("WHY", "the rocket equation punishes carried mass logarithmically; dropping empty tanks deepens the mass ratio per burn. With zero structural mass any split gives the same $\\Delta v = v_e \\ln(M/M_p)$ - structure is the ONLY reason to stage."),
          ("CHECK", "limits: $\\epsilon \\to 0$: staged = unstaged; $M_p \\to M$: $\\Delta v \\to 0$; more stages (fixed hardware) always increase $\\Delta v$ until the interstage hardware itself dominates. Timeline closes: $400+400+50+50+100 = 1000$ kg.")]),
     CX('h3', HEAD, "Optimal split and the multistage ladder",
       ["For two identical stages (equal $\\epsilon$, equal $v_e$): the total $\\Delta v = v_e[\\ln(M/m_1) + \\ln(m_2/m_f)]$ under the mass-timeline constraint; the optimisation (Jensen on the logs) equalises the two stage $\\Delta v$s for maximum total at fixed hardware. With $n$ stages and fixed total structure mass, more stages keep helping until interstage hardware eats the gain - real rockets stop at $n = 2$ or 3.",
          "With gravity: $\\Delta v_{net} = \\sum v_e \\ln(m_i/m_f) - g t_{burn}$; staging also keeps acceleration high in thin air, cutting gravity loss - the engineering trade-off beyond the textbook ledger. The same ledger governs 'drop ballast mid-journey' puzzles and two-block spring mass-shedding (CM-14).",
          ("FN", "for identical stages the optimal equal-split principle is a one-line AM-GM argument: $\\ln a + \\ln b = \\ln(ab)$ is maximal at fixed $a + b$ when $a = b$ - equal logs, equal $\\Delta v$."),
          ("CHECK", "single vs staged audit in ratio form: $\\frac{\\Delta v_{staged}}{\\Delta v_{single}} = \\frac{\\ln(1000/600)+\\ln(550/150)}{\\ln 5} = \\frac{1.810}{1.609} = 1.125$ - exactly 12.5% more $\\Delta v$.")]),
     CX('h3', CH, "Staging drills",
       ["(a) Single stage: $M = 1000$, propellant 800, structure 100, payload 100: $\\Delta v = v_e \\ln 5 = 1.61 v_e$. (b) Two stages (the worked case): $1.81 v_e$ - beats (a) by $0.20 v_e$. (c) Three stages of 266.7 propellant + 33.3 structure each, payload 100: the timeline is $1000 \\to 733.3 \\to 700 \\to 433.3 \\to 400 \\to 133.3$ (burn, discard, burn, discard, burn; the last structure rides along). Then $\\Delta v = v_e[\\ln(1000/733.3) + \\ln(700/433.3) + \\ln(400/133.3)]$ $= v_e[0.310 + 0.480 + 1.099] = 1.89 v_e$ - three stages beat two, which beat one: monotone improvement.",
          "Trap: discarding before burnout; telescoping by forgetting the discard; mixing 'structure of stage' with 'payload'. The mass timeline diagram is the answer sheet.",
          ("CHECK", "drill (c) timeline: $266.7\\times3 + 33.3\\times3 + 100 = 800 + 100 + 100 = 1000$; final $133.3 = 100 + 33.3$ (last structure rides along).")]),
     CX('h3', CH, "Inverse staging: sizing the rocket for a mission",
       ["Given $\\Delta v$ target and $v_e$: required mass ratio $m_0/m_f = e^{\\Delta v / v_e}$. Mission $\\Delta v = 9$ km/s at $v_e = 3$ km/s: ratio $= e^3 = 20.1$ - the payload + structure must be under 5% of launch mass. With structural coefficient $\\epsilon$ per stage, $n$ stages give successively deeper ratios; the practical answer: two stages at $\\epsilon = 0.1$ reach ratios around 10-15 - matching real launchers.",
          "Gravity-loss back-of-envelope: at thrust-to-weight 1.3, the gravity loss $\\approx g t_{burn}$ quoted from the burn time, not from $\\Delta v$ alone; a 9 km/s mission at $a = 2g$ loses roughly half a km/s to gravity in the first minutes.",
          ("CHECK", "reverse the worked case: 5.43 km/s at $v_e = 3$ needs ratio $e^{1.81} = 6.1$; the staged design delivers $1000/150 = 6.67$ - consistent with the timeline (final mass includes the last structure).")]),
]), "Staging ledger; mass timeline; corrected P30 numbers (5.43 vs 4.83 km/s); drills.")

# ---------------------------------------------------- OLY-07 momentum flux of a water jet
ADD('OLY-07', CHUNK([
    CX('h2', HEAD, "Jet on a plate: F = rho A v^2, and the moving-plate power game",
       ["A circular jet of area $A$, speed $v$, density $\\rho$ strikes a large fixed flat plate and spreads along it (source OL9). Mass rate $\\dot m = \\rho A v$; the normal momentum is destroyed (the water leaves tangentially): $F = \\dot m v = \\rho A v^2$. For a plate tilted at angle $\\theta$ to the jet axis (normal force only): $F_n = \\rho A v^2 \\cos\\theta$; at angle $\\theta$ to the PLATE surface: $F_n = \\rho A v^2 \\sin\\theta$ - read the angle definition from the diagram before multiplying.",
          "Moving plate at speed $u$ in the jet's direction: the relative speed is $v - u$, so $F = \\rho A (v-u)^2$ and the power delivered to the plate is $P = Fu = \\rho A (v-u)^2 u$. Maximise over $u$: $dP/du = 0$ gives $u = v/3$ (not $v/2$!) with $P_{max} = \\frac{4}{27}\\rho A v^3$. The turbine designer's law: the jet should be slowed to one third. At $u = 0$ (fixed plate) $P = 0$; at $u = v$ (plate flees with the jet) $F = 0$ and $P = 0$; the maximum sits between.",
          "If the water does not spread but rebounds elastically (curved cup): the normal momentum REVERSES: $F = 2\\dot m v = 2\\rho A v^2$ (the cup variant of source OL9) - double the flat-plate force. A Pelton-wheel cup nearly doubles the force of a flat target; the same factor-2 logic as the turn flux in chain problems.",
          ("WHY", "the jet is the cleanest possible flux problem: control volume = the water in contact; momentum in $\\rho A v^2$ per second along the normal; momentum out zero (flat) or reversed (cup). If the jet discharges to atmosphere there are no pressure terms - the whole force is momentum flux."),
          ("CHECK", "numbers: $A = 6$ cm$^2$, $v = 12$ m/s, $\\rho = 1000$: $\\dot m = 7.2$ kg/s; $F = 86.4$ N; on a cup: 172.8 N; at $u = 4$ m/s: $F = 1000(6\\times10^{-4})(64) = 38.4$ N, $P = 153.6$ W.")]),
     CX('h3', HEAD, "Recoil as flux; the jet taxonomy",
       ["A hose or gun ejecting $\\dot m$ at $v_e$ feels recoil $\\dot m v_e$ - the rocket thrust (CM-17) in static form. A fire hose of 5 kg/s at 20 m/s: 100 N on the firefighter. A sprinkler cart: thrust = mass rate x relative jet speed; the cart accelerates like a rocket with water as exhaust. The jet-pump / turbine family: same flux law with the right control volume.",
          "Water falling on a moving horizontal belt: retarding force $= \\dot m(v - u)$ with $u$ the belt speed (CM-16 family). The exam taxonomy: jet on plate $\\rho A v^2$; cup $2\\rho A v^2$; moving plate $\\rho A(v-u)^2$; belt pickup $\\dot m v$; rocket $\\dot m v_e$. One law, five costumes.",
          ("CHECK", "recoil audit: 0.5 kg/s at 15 m/s: 7.5 N; pump power $= \\frac{1}{2}\\dot m v^2 = 56$ W = the jet's KE rate; the plate absorbs $Fu$ on top of that in the belt-split sense - consistent with CM-16's factor-2 bookkeeping.")]),
     CX('h3', CH, "Jet drills",
       ["(a) Jet $A = 4$ cm$^2$, $v = 10$ m/s on a flat plate: $F = 40$ N. (b) Same on a plate at 45 degrees to the jet axis (normal force): $F_n = 28.3$ N. (c) Moving plate at 4 m/s: $F = 1000(4\\times10^{-4})(36) = 14.4$ N; $P = 57.6$ W. (d) Cup reversal: double (a): 80 N. (e) Optimal turbine speed for a 20 m/s jet: $u = 6.67$ m/s; $P_{max} = \\frac{4}{27}(1000)(4\\times10^{-4})(8000) = 474$ W.",
          "Trap: using $v$ instead of $v - u$ for moving plates. Trap: angle measured from the wrong reference. Trap: missing the factor 2 for rebound cups. Trap: equating $P_{max}$ with the jet's KE rate $\\frac{1}{2}\\rho A v^3$ - the best useful power is only $\\frac{8}{27}$ of the jet's KE rate, about 30%.",
          ("CHECK", "drill (e) consistency: $u = v/3 = 6.67$; $F = \\rho A (2v/3)^2 = 1000(4\\times10^{-4})(177.8) = 71.1$ N; $P = 71.1 \\times 6.67 = 474$ W.")]),
     CX('h3', CH, "Efficiency curve of a turbine stage",
       ["Useful power $P = \\rho A (v-u)^2 u$ rises from 0 at $u = 0$, peaks at $u = v/3$ with $P_{max} = \\frac{4}{27}\\rho A v^3$, falls to 0 at $u = v$. Efficiency $\\eta = P/(\\frac{1}{2}\\rho A v^3)$: at the peak $\\eta = 8/27 = 30$%. The Pelton cup shifts the force constant up by the factor 2 in the flux; the $u = v/3$ optimum is unchanged.",
          "Drill: jet $v = 15$ m/s, $\\rho A = 0.5$ kg/m: $P_{max} = \\frac{4}{27}(0.5)(3375) = 250$ W at $u = 5$ m/s. Flat plate at $u = 5$: $F = 0.5(100) = 50$ N, $P = 250$ W.",
          ("CHECK", "curve sanity: $P(v/4) = \\rho A (3v/4)^2 (v/4) = \\frac{9}{64}\\rho A v^3 = 0.141$ vs peak $0.148$ - near-flat top; real impulse turbines cluster $u/v$ near 1/2 with cups.")]),
]), "Jet flux law; moving plate P = rho A (v-u)^2 u with u = v/3 optimum; cup factor 2; drills.")

# ---------------------------------------------------- OLY-08 the folded chain on a table
ADD('OLY-08', CHUNK([
    CX('h2', HEAD, "Folded chain released over a smooth edge: v = y sqrt(2g/L)",
       ["Clean statement (source OL10, whose 'COM \\L/4' phrasing is ambiguous - recorded in SOURCE-AUDIT; this is the standardised version): a uniform chain of mass $m$, length $L$ is folded at its MIDPOINT and laid on a smooth horizontal table with the fold just past the smooth edge, so BOTH halves hang together. Released from rest. Let $y$ = the descent of the fold = the length of EACH hanging strand (total hanging length $2y$). Speed: energy with hanging mass $2\\lambda y$ and COM at depth $y/2$: PE loss $= 2\\lambda y \\cdot g \\cdot \\frac{y}{2} = \\lambda g y^2$; KE $= \\frac{1}{2}\\lambda L v^2$ (the WHOLE chain moves at speed $v$ - the fold is a rigid corner). So $\\frac{1}{2}\\lambda L v^2 = \\lambda g y^2$: $v = y\\sqrt{\\dfrac{2g}{L}}$ - speed linear in descent, NOT $\\sqrt{2gy}$ as for a free particle.",
          "Departure: the chain leaves the table when the fold has descended $y = L/2$ (both strands fully hanging): $v_{dep} = \\frac{L}{2}\\sqrt{\\frac{2g}{L}} = \\sqrt{\\frac{gL}{2}}$. After that the chain falls free with its departure speed. The law $v \\propto y$ means constant acceleration: $a = \\frac{dv}{dt} = \\sqrt{\\frac{2g}{L}} v = \\frac{2g}{L}y$ - the fold accelerates in proportion to its own depth (a linear instability, kin to the chain-over-peg ODE of OLY-05).",
          "Force on the edge (flux bonus): the doubled strand turns over the edge at rate $2\\lambda v$; the edge feels hanging weight plus a turn-flux term of the $2\\lambda v^2$ family with the doubled density. The exam answer quotes the energy line and $v_{dep} = \\sqrt{gL/2}$; the force bookkeeping is a fair exercise on the momentum ledger of OLY-05.",
          ("WHY", "the fold constrains BOTH halves to move together - one velocity, one degree of freedom. That is why the whole chain's KE uses $L$ while the PE uses only the hanging $2y$: the energy equation is unusually clean and $v = y\\sqrt{2g/L}$ is exact."),
          ("CHECK", "limits: $y = 0$: $v = 0$; $y = L/2$: $v = \\sqrt{gL/2}$; $g \\to 0$: $v \\to 0$. Units: $y\\sqrt{g/L} = $ m $\\times$ s$^{-1}$ = m/s. Compare free fall through $y$: $\\sqrt{2gy}$ vs fold $y\\sqrt{2g/L}$ - at $y = L/2$: free $\\sqrt{gL}$ vs fold $\\sqrt{gL/2}$: the fold is SLOWER (half the chain is still on the table).")]),
     CX('h3', HEAD, "Variant geometries and the ambiguity guard",
       ["Variant A: fold NOT at the midpoint (strands of unequal length): the shorter strand runs out first; beyond that it is a single-hanging-strand problem - piecewise solve. Variant B: fold on the table with the fold-point LIFTED then released (the 'COM + L/4' reading of source OL10): the answer depends on the exact initial shape - define the geometry in the diagram before solving.",
          "Variant C: rough table: friction on the table-lying part retards; energy loses the friction-work term. Variant D: the chain is pushed initially: from $\\frac{1}{2}\\lambda L v^2 = \\frac{1}{2}\\lambda L v_0^2 + \\lambda g y^2$: $v^2 = v_0^2 + \\frac{2g y^2}{L}$.",
          ("CHECK", "variant D limit: $y = 0$ gives $v = v_0$; at $y = L/2$, $v_0 = 0$ recovers $v = \\sqrt{gL/2}$.")]),
     CX('h3', CH, "Fold drills",
       ["(a) $L = 2$ m, $g = 10$: $v = y\\sqrt{10} = 3.16y$; at $y = 0.4$ m: $v = 1.26$ m/s; departure at $y = 1$ m: $v = 3.16$ m/s ($= \\sqrt{gL/2} = \\sqrt{10}$). (b) Unequal fold (strands $L/4$ and $3L/4$ hanging, i.e. NOT a doubled fold): different problem - use the peg-style ODE of OLY-05. (c) Compare departure speeds: fold $\\sqrt{gL/2}$; single strand sliding off a peg to $x = L$: $v = \\sqrt{gL/2}$ as well - the two ODEs are first cousins.",
          "Trap: treating the fold as two independent strands (they are kinematically tied - ONE $v$). Trap: using $\\sqrt{2gy}$ (free fall) for the fold. Trap: forgetting the on-table part of the chain in the KE sum.",
          ("CHECK", "drill (a): $\\sqrt{2g/L} = \\sqrt{10} = 3.16$; $v(0.4) = 1.26$ m/s; departure $\\sqrt{10} = 3.16$ m/s.")]),
     CX('h3', CH, "Fold as a variable-mass Atwood",
       ["The fold's equation $a = \\frac{2g}{L}y$ is a variable-mass Atwood: the driving weight $2\\lambda y g$ acts on the accelerating mass $\\lambda L$: $a = \\frac{2\\lambda y g}{\\lambda L} = \\frac{2gy}{L}$ - the same result as the energy route. The Atwood perspective shows WHY the fold accelerates: the hanging weight grows while the inertia stays fixed.",
          "Compare: classic Atwood (two fixed masses): $a = g\\frac{m_1 - m_2}{m_1 + m_2}$ = const; fold: $a \\propto y$ = exponential runaway; peg: $a = g(2x-L)/L$ = linear. Three ODE shapes in one family: constant, linear, linear-in-y - each with its own $v^2(x)$.",
          ("CHECK", "Atwood limit of the fold: freeze $y$ at $y_0$ (clamp): $a = 2gy_0/L$ constant - reduces to a fixed-mass Atwood with effective masses $2\\lambda y_0$; the clamp force appears - consistent bookkeeping.")]),
]), "Folded chain: v = y sqrt(2g/L), departure sqrt(gL/2); ambiguity guard for OL10; drills.")

# ---------------------------------------------------- OLY-09 relativistic momentum preview
ADD('OLY-09', CHUNK([
    CX('h2', HEAD, "Why momentum must be gamma m v (source OL5)",
       ["The demand: conservation of momentum must hold in ALL inertial frames. If $p = m v$ with invariant $m$, a Lorentz transformation of a simple collision gives different momenta in different frames - the law fails. The unique form (up to an overall constant) that transforms correctly is $\\mathbf{p} = \\gamma m \\mathbf{v}$ with $\\gamma = 1/\\sqrt{1 - v^2/c^2}$. Derivation sketch (the standard two-frame elastic collision argument): write $p = m f(v)$; demand that a collision viewed in the lab and in a boosted frame both conserve $p$; the functional equation forces $f = \\gamma$.",
          "Consequences previewed here (full treatment is relativistic dynamics): (1) $\\gamma \\approx 1 + \\frac{v^2}{2c^2}$ at low speed, so $p \\approx mv$ up to tiny corrections - Newtonian mechanics is the $v \\ll c$ shadow. (2) Force is $dp/dt$ not $ma$: $F = \\gamma^3 m a$ along the motion - a constant force cannot accelerate a mass to $c$. (3) Relativistic KE $= (\\gamma - 1)mc^2 \\to \\frac{1}{2}mv^2$ as $v \\to 0$; the full series is $\\frac{1}{2}mv^2 + \\frac{3}{8}\\frac{mv^4}{c^2} + \\ldots$ (4) The 'mass increase' $m \\to \\gamma m$ is a historical way of writing the same formula - the modern view keeps $m$ invariant and changes the momentum law (source OL5's Significance).",
          "For classical olympiad/JEE mechanics: the exam-relevant point is the scope statement - all our conservation laws assume $v \\ll c$; when speeds approach $c$, momentum conservation still holds but with $p = \\gamma mv$ and $e$-type restitution becomes frame-dependent and subtle. Keep this sheet as the fence around the classical playground.",
          ("WHY", "the deep principle: conservation laws are statements about symmetry (translation invariance of space and time). The relativistic momentum is what survives when both symmetries act together - the classical $mv$ is the low-speed limit of the correct object, not a definition."),
          ("CHECK", "low-speed limit $v/c = 0.1$: $\\gamma = 1.005$: a 0.5% correction to $p$ - invisible in every chapter problem. $v = 0.9c$: $\\gamma = 2.29$: more than double $mv$ - classical mechanics gone.")]),
     CX('h3', HEAD, "The two-frame argument in one paragraph",
       ["Take an elastic collision between identical particles, symmetric in the CM. Boost along the collision axis. In Newtonian physics the velocity addition $u' = u - V$ preserves momentum conservation. In relativity, velocity addition is $u' = \\frac{u - V}{1 - uV/c^2}$; requiring conservation in both frames with $p = m f(u)$ gives a functional equation for $f$ whose unique regular solution is $f(u) = \\gamma u$ (up to constant $m$).",
          "Rest mass is invariant: every observer agrees on $m$; they disagree on $p$ and $E$. Energy-momentum forms a four-vector $(E/c, \\mathbf{p})$; $E^2 = (pc)^2 + (mc^2)^2$ unifies the ledger: massless particles have $p = E/c$ (photons); massive at rest have $E = mc^2$.",
          ("FN", "relativistic collisions still use the same triage: choose the frame (CM is best), conserve the four-momentum, transform back. The 90-degree rule of CM-12 becomes 'the angle opens ABOVE 90 for relativistic equal-mass collisions in the lab' - a classic modern-physics exam twist."),
          ("CHECK", "energy-momentum checks: photon $m = 0$: $E = pc$; electron at rest: $p = 0$, $E = mc^2$; Newtonian ledger recovered for $E - mc^2 \\ll mc^2$: $E \\approx mc^2 + \\frac{p^2}{2m}$.")]),
     CX('h3', CH, "What to carry back into classical mechanics",
       ["(1) Momentum conservation is the more fundamental law; $F = ma$ is its low-speed shadow. (2) The classical chapter's formulas (3.7, 4.5, 4.6) are all $v \\ll c$ statements - state the assumption when speeds are given as 'large'. (3) The rocket equation assumes non-relativistic exhaust; relativistic rockets integrate $\\Delta p = v_e dm$ with $\\gamma$ folded in. (4) Restitution ($e$) has no clean relativistic definition for extended bodies - modern physics avoids it.",
          "Exam context: this sheet is the olympiad extension layer (the source lists it as OL5, a PART-28 preview). For JEE the one-line takeaway: $p = \\gamma mv$ reduces to $mv$ at low speed and momentum is conserved in all frames - the syllabus does not require the derivations.",
          ("CHECK", "limit drill: $\\gamma - 1 \\approx v^2/2c^2$ at $v = 0.01c$: $5\\times10^{-5}$ - the classical error is one part in 20,000.")]),
     CX('h3', CH, "Gamma drills",
       ["(a) $v = 0.5c$: $\\gamma = 1.155$; (b) $v = 0.8c$: $\\gamma = 1.667$; (c) $v = 0.99c$: $\\gamma = 7.09$; (d) KE at 0.8c $= (\\gamma-1)mc^2 = 0.667 mc^2$ - twice the Newtonian $\\frac{1}{2}m(0.64c^2) = 0.32 mc^2$. (e) A proton at rest has $E = 938$ MeV; at $\\gamma = 4$: total 3.75 GeV, KE 2.81 GeV.",
          "Momentum at 0.8c for 1 kg: $p = \\gamma m v = 1.667(1)(2.4\\times10^8) = 4\\times10^8$ kg m/s vs Newtonian $2.4\\times10^8$ - a 67% understatement. The classical ledger fails visibly above $0.5c$.",
          ("CHECK", "$\\gamma$ identity: $\\gamma^2(1 - v^2/c^2) = 1$ - verify at 0.8c: $2.78(0.36) = 1.0$.")]),
]), "p = gamma m v from frame-independence; scope fence for classical mechanics; preview of PART 28.")

# ---------------------------------------------------- OLY-10 the hopper cart and the pump
ADD('OLY-10', CHUNK([
    CX('h2', HEAD, "Cart under a hopper: the full variable-mass ledger",
       ["A cart of mass $M_0$ (empty) rolls at $v_0$ on a smooth floor under a hopper that drops sand at rate $\\dot m$ (kg/s). Collecting mode (source family CM-16/Q22): horizontal momentum is conserved (dropped sand has none): $M(t)v(t) = M_0 v_0$ with $M(t) = M_0 + \\dot m t$: $v(t) = \\dfrac{M_0 v_0}{M_0 + \\dot m t}$. The retarding force at any instant: $F = \\dot m v$ (the sand must be dragged from 0 to $v$). Power drained from the cart's KE: exactly $\\frac{1}{2}\\dot m v^2$ - half becomes the sand's KE, half becomes pickup heat (CM-16's factor-2).",
          "Leaking mode: a cart of mass $M$ at $v$ leaks sand vertically at rate $\\dot m$: the dropped sand carries horizontal momentum $\\dot m v$ away per second, so $\\frac{d}{dt}(M v) = \\dot m v$; with $\\frac{dM}{dt} = -\\dot m$ this gives $M \\dot v = 0$: $v$ CONSTANT. The classic surprise: a leaking cart does not slow down; only loading slows it.",
          "Engine mode: a cart with engine force $F$ collecting sand: $\\frac{d}{dt}[(M_0 + \\dot m t)v] = F$; solve the linear ODE. With constant power $P$ instead: $\\frac{d}{dt}[\\frac{1}{2}M v^2] = P - \\frac{1}{2}\\dot m v^2$ (the pickup tax). The hopper family is the rocket equation with the sign of $\\dot m$ flipped and no exhaust speed - same ledger, one diagram.",
          ("WHY", "these three modes (load, leak, thrust) exhaust the first-order variable-mass list for exam mechanics; the momentum ledger in $dt$ is the single method. The surprise results (leaking keeps $v$; loading burns half the delivered power as heat) are examiner favourites because they punish intuition."),
          ("CHECK", "collecting numbers: $M_0 = 20$ kg at 5 m/s, $\\dot m = 0.1$ kg/s, at $t = 100$ s: $v = 100/30 = 3.33$ m/s; KE: 250 J to $\\frac{1}{2}(30)(11.1) = 166.6$ J; the 83.4 J lost is pickup heat, matching the differential identity $\\frac{1}{2}\\dot m v^2 = -\\frac{d}{dt}KE$ (verified in CM-16).")]),
     CX('h3', HEAD, "Sprinkler cart and jet recoil (the same ledger)",
       ["Sprinkler: cart + water tank ejects water at $\\dot m$ with speed $v_e$ relative to the cart (usually backward): thrust $\\dot m v_e$; the cart is a rocket with water propellant: $\\Delta v = v_e \\ln(M_0/M_f)$ if $\\dot m$ runs to dry. Fire-extinguisher recoil: treat the spray as exhaust. A cart under a leaky bucket with a pump: combine loading and thrust terms in one $dt$ equation.",
          "Mixed problem: cart collects rain at $\\dot m_1$ while ejecting at $\\dot m_2$ with relative speed $v_e$: the systematic form is $M\\dot v = F_{ext} + \\dot m_{in}(u_{in} - v) + \\dot m_{out}(u_{out} - v)$ with all velocities lab-frame; the CM-16 sign discipline sets each term.",
          ("CHECK", "sprinkler limit: no water: $\\Delta v = 0$; no external force with ejecta: momentum of cart + ejecta conserved exactly.")]),
     CX('h3', CH, "Hopper drills",
       ["(a) Cart 30 kg at 6 m/s collects 2 kg of dropped sand: $v = 180/32 = 5.625$ m/s. (b) Cart 30 kg at 6 m/s LEAKS 2 kg vertically: $v = 6$ m/s unchanged. (c) Cart 30 kg at rest ejects 5 kg backward at 4 m/s relative to the cart: ejected lab speed $= v - 4$; momentum $0 = 25v + 5(v-4) = 30v - 20$: $v = 0.67$ m/s. (d) Engine force 60 N while loading at 0.2 kg/s (cart 30 kg at 6 m/s initially): $(30 + 0.2t)v = 180 + 60t$; at $t = 10$: $32v = 780$: $v = 24.4$ m/s.",
          "Trap: forgetting the $\\dot m v$ retarding term when loading. Trap: assuming leaking slows the cart. Trap: using $\\Delta v = v_e \\ln(\\cdot)$ for a collecting cart (that formula is for ejecting mass).",
          ("CHECK", "drill (c): $p = 25(0.67) - 5(3.33) = 16.7 - 16.7 = 0$; drill (d): $32 \\times 24.4 = 780 = 180 + 600$.")]),
     CX('h3', CH, "Explicit solutions of the loading-engine ODE",
       ["$\\frac{d}{dt}[(M_0 + \\dot m t)v] = F$ integrates directly: $(M_0 + \\dot m t)v = M_0 v_0 + F t$: $v(t) = \\dfrac{M_0 v_0 + F t}{M_0 + \\dot m t}$. Long-time limit: $v \\to F/\\dot m$ (the engine can only hold that asymptote while dragging new mass). With $F = 0$ it reduces to the pure-loading decay $M_0 v_0/(M_0 + \\dot m t)$; with $\\dot m = 0$ it is uniform acceleration.",
          "Drill: $M_0 = 10$, $v_0 = 2$, $\\dot m = 0.5$, $F = 20$: $v(10) = (20 + 200)/15 = 14.7$ m/s; asymptote $F/\\dot m = 40$ m/s. Power at $t = 10$: $F v = 294$ W; pickup tax $\\frac{1}{2}\\dot m v^2 = 54$ W.",
          ("CHECK", "differentiate the closed form at $t = 0$: $\\dot v = [F M_0 - \\dot m M_0 v_0]/M_0^2 = (200 - 10)/100 = 1.9$ m/s$^2$; the ODE $M\\dot v = F - \\dot m v = 20 - 1 = 19$ gives $\\dot v = 1.9$ - the two agree.")]),
]), "Load/leak/thrust modes; sprinkler and mixed flows; drills with the surprise results.")

# ---------------------------------------------------- OLY-11 momentum integration methods
ADD('OLY-11', CHUNK([
    CX('h2', HEAD, "When momentum needs calculus: the three integration patterns",
       ["Pattern 1 - VARIABLE FORCE with time: $J = \\int F(t) dt = \\Delta p$; if $F$ depends on $v$ (drag), write $m\\frac{dv}{dt} = F(v)$ and separate: $\\frac{m\\,dv}{F(v)} = dt$; integrate. Pattern 2 - VARIABLE FORCE with position: $F = F(x)$; use work-energy $\\int F dx = \\Delta K$ instead (or $v\\,dv = a\\,dx$). Pattern 3 - VARIABLE MASS: the $dt$ ledger of CM-16/OLY-10: $\\frac{d}{dt}(Mv) = F_{ext} + \\dot m_{in}u_{in} - \\dot m_{out}u_{out}$; solve the linear ODE.",
          "Worked (chain ODE, source OL7 method): $a = g(2x-L)/L$ with $v = dx/dt$: $v\\,dv = a\\,dx$ integrates to $v^2(x)$; then $dt = dx/v(x)$ integrates to $t(x)$ - the two-integration pattern of every chain problem. Worked (drag): $m\\dot v = -bv$: $v = v_0 e^{-bt/m}$ - exponential relaxation; distance $= \\frac{mv_0}{b}(1 - e^{-bt/m})$; the body never stops in finite time - a favourite limit question.",
          "Worked (rocket with gravity): $m\\dot v = -v_e \\dot m - mg$ with $m = m_0 - \\dot m t$: $\\Delta v = v_e \\ln(m_0/m_f) - g t_b$ - the $dt$ ledger with a prescribed $m(t)$. The integration pattern is identical to the hopper engine mode (OLY-10) with sign changes.",
          ("WHY", "momentum conservation is a first-order statement about $p$; as soon as the force law or the mass law is nonlinear, the exam problem is really a differential equation. The triage: (i) is $F$ given as $t$, $x$, or $v$? (ii) is mass constant? (iii) choose $J = \\int F dt$ or work-energy accordingly."),
          ("CHECK", "drag limit checks: $b \\to 0$: $v \\to v_0$; $t \\to \\infty$: $v \\to 0$ with finite distance; large $b$: stops almost immediately. Chain ODE check: $v^2 = \\frac{2g}{L}(x - \\frac{L}{2})^2$ differentiated back gives $a = \\frac{2g}{L}(x-\\frac{L}{2})$ - matches Newton.")]),
     CX('h3', HEAD, "The separable-equation toolkit for mechanics",
       ["$m v \\frac{dv}{dx} = F(x)$: energy in disguise. $m \\frac{dv}{dt} = F(v)$: time-separable. $\\frac{d}{dt}(M(t)v) = F(t)$: integrating factor $1/M(t)$. $\\frac{d}{dt}(Mv) = \\dot m u$: variable mass. Recognising WHICH of the four forms a problem takes is the whole exam skill; each has a one-line solution template.",
          "Phase-line view (olympiad flavour): for $a = a(x)$ the fixed points are $a = 0$ (equilibrium; stable if $da/dx < 0$); the chain over the peg has unstable equilibrium at $x = L/2$; the fold has $a \\propto y$ (no fixed point except 0, unstable). Sketching $a$ vs $x$ before integrating prevents sign errors in $v^2(x)$.",
          ("FN", "numerical fallback: if the ODE has no closed form (e.g. $v^2$ drag plus thrust), Euler-step in a table - method marks come from the SETUP $m\\dot v = \\ldots$, and a one-step estimate often answers 'show that the speed exceeds...' questions."),
          ("CHECK", "toolkit sanity: every template above is just $F = dp/dt$ rearranged; if two templates disagree on a shared problem, the bookkeeping of $M(t)$ vs $m$ is wrong.")]),
     CX('h3', CH, "Integration drills",
       ["(a) $m = 2$ kg, $F = 6t$ N: $\\Delta p = \\int_0^2 6t\\,dt = 12$ N s; $\\Delta v = 6$ m/s. (b) $F = -kx$ from $x = 0$ to $A$: work-energy: $\\Delta K = -\\frac{1}{2}kA^2$ (spring stop: $\\frac{1}{2}mv^2 = \\frac{1}{2}kA^2$). (c) Drag $bv$ with $b = 0.4$, $m = 1$, $v_0 = 10$: after 2 s: $v = 10 e^{-0.8} = 4.49$ m/s. (d) Chain $L = 1$, $g = 10$, nudge release: $v = \\sqrt{20}(x - 0.5)$; time from $x = 0.75$ to $x = 1$: $t = \\int_{0.75}^{1} \\frac{dx}{\\sqrt{20}(x-0.5)} = \\frac{\\ln 2}{\\sqrt{20}} = \\frac{0.693}{4.472} = 0.155$ s.",
          "Trap: using $J = F_{avg}t$ when $F$ is not constant - integrate instead. Trap: mixing $F(x)$ problems into $\\int F dt$ (wrong variable). Trap: losing the $\\frac{1}{2}$ in $v\\,dv = a\\,dx$ integration ($v^2/2$, not $v^2$).",
          ("CHECK", "drill (d) via energy: $v(x) = \\sqrt{20}(x-0.5)$ comes from $v^2 = 20(x-0.5)^2$ (OLY-05); $t = \\int dx/v$ = the second integration of Pattern 1.")]),
     CX('h3', CH, "Linearise around the fixed point: the exponential departure",
       ["Near an unstable equilibrium, $a \\approx \\lambda_1 (x - x_*)$ with $\\lambda_1 > 0$ gives $x - x_* \\propto e^{\\sqrt{\\lambda_1} t}$ - the linearised escape law. Peg: $x_* = L/2$, $a = \\frac{2g}{L}(x - \\frac{L}{2})$: departure rate $\\sqrt{2g/L}$; a 1% displacement grows by $e$ in time $\\sqrt{L/2g}$. For $L = 1$ m: 0.15 s per e-fold.",
          "Stable side: if $a = -\\omega^2(x-x_*)$, the linearised solution is SHM at $\\omega$ - the same local analysis classifies every chain/pendulum equilibrium before solving the full ODE.",
          ("CHECK", "the fold's $a = \\frac{2g}{L}y$ is the same linear form with $y_* = 0$: pure exponential from the start; the peg's full solution $v = \\sqrt{2g/L}(x - L/2)$ is the EXACT finite-amplitude version of the linearised escape - they coincide because the ODE is exactly linear in $(x - L/2)$.")]),
]), "Three integration patterns; separable toolkit; phase-line sketch; drills with the drag and chain ODEs.")
# ---------------------------------------------------- convert CX chapters to render pages
import re as _re
import re
from pathlib import Path as _Path
from PIL import Image as _Image, ImageDraw as _ID, ImageFont as _IF
from matplotlib.mathtext import math_to_image as _m2i, MathTextParser as _MTP
from matplotlib.font_manager import FontProperties as _FP
import io as _io

ROOT = _Path(__file__).resolve().parent
_FPATH = str(ROOT / 'fonts/PatrickHand-Regular.ttf')

def normalize(s):
    s=re.sub(r'\\sqrt(\\[A-Za-z]+)',r'\\sqrt{\1}',s)
    s=re.sub(r'\\sqrt\s*([0-9A-Za-z])(?![A-Za-z}])',r'\\sqrt{\1}',s)
    s=re.sub(r'\\(le|ge)(?![A-Za-z])',r'\\\1q',s)
    s=s.replace(r'\sqrt5',r'\sqrt{5}').replace(r'\hbox',r'\mathrm').replace(r'\frac1{',r'\frac{1}{')
    s=re.sub(r'\\(mathcal|mathbf|mathrm)\s+([A-Za-z])',r'\\\1{\2}',s)
    return re.sub(r'\\(?:tfrac|frac)\s*([A-Za-z0-9])\s*([A-Za-z0-9])',r'\\frac{\1}{\2}',s)
import numpy as _np
_M2C = {}
def math_wh(tex):
    if tex not in _M2C:
        b=_io.BytesIO()
        _m2i('$'+normalize(tex)+'$',b,prop=_FP(size=12),dpi=300,format='png',color='#153149')
        a=_Image.open(b).convert('RGBA')
        arr=_np.array(a); arr[:,:,3]=255-arr[:,:,:3].min(axis=2); arr[:,:,:3]=[21,49,73]
        a=_Image.fromarray(arr)
        bbox=a.getbbox(); a=a.crop(bbox) if bbox else a
        _M2C[tex]=(a.width, a.height)
    return _M2C[tex]

_SAFE = {
    '\u2713':'ok', '\u2717':'fails', '\u2192':' $\\to$ ', '\u00b5':'$\\mu$',
    '\u0394':'$\\Delta$', '\u03b1':'$\\alpha$', '\u03b3':'$\\gamma$', '\u03c1':'$\\rho$',
    '\u03c9':'$\\omega$', '\u2202':'$\\partial$', '\u221d':'$\\propto$',
    '\u2080':'$_0$', '\u2081':'$_1$', '\u2082':'$_2$', '\u2083':'$_3$',
    '\u03c8':'$\\psi$', '\u03c6':'$\\phi$', '\u03c3':'$\\sigma$', '\u03bd':'$\\nu$',
    '\u03ba':'$\\kappa$', '\u03b5':'$\\varepsilon$', '\u03b7':'$\\eta$', '\u03c4':'$\\tau$',
    '\u03b8':'$\\theta$', '\u03b2':'$\\beta$', '\u03bc':'$\\mu$', '\u039b':'$\\Lambda$',
    '\u03a3':'$\\Sigma$', '\u03a9':'$\\Omega$', '\u03a6':'$\\Phi$', '\u0393':'$\\Gamma$',
    '\u2032':"'", '\u2033':"''", '\u0302':'', '\u2194':' $\\leftrightarrow$ ',
    '\u21d2':' $\\Rightarrow$ ', '\u2264':'<=',
}
def safe(s):
    out=[]
    for part in _re.split(r'(\$[^$]+\$)', s):
        if len(part)>2 and part[0]=='$' and part[-1]=='$':
            out.append(part)
        else:
            for k,v in _SAFE.items():
                part=part.replace(k,v)
            out.append(part)
    return ''.join(out)

def plain_title(t):
    def mm(m):
        x=m.group(1)
        x=x.replace('\\rm ','').replace('\\mathrm ','').replace('\\mathbf ','')
        x=x.replace('\\','').replace('{','').replace('}','').replace('^','').replace('_',' ')
        x=x.replace('prime',"'").replace('times','x').replace('cdot','.')
        x=re.sub(r'\s+',' ',x).strip()
        return x
    t=_re.sub(r'\$([^$]+)\$', mm, t)
    return t.replace('$','')

_F48=_IF.truetype(_FPATH,48); _F46=_IF.truetype(_FPATH,46)
_D1=_ID.Draw(_Image.new('RGB',(1,1)))
BODYW=1032

def _units(s):
    us=[]
    for part in _re.split(r'(\$[^$]+\$)', s):
        if len(part)>2 and part[0]=='$' and part[-1]=='$':
            us.append(('m',part[1:-1]))
        elif part:
            for w in part.split():
                us.append(('t',w))
    return us

_HC={}
def item_h(kind, s, label=''):
    key=(kind,label,s)
    if key in _HC: return _HC[key]
    text=label+s
    f=_F46 if kind in ('why','trap','check') else _F48
    lead=53 if kind in ('why','trap','check') else 56
    space=_D1.textlength(' ',font=f)
    total=0
    for block in text.split('\n'):
        lw=0.0; mh=0; n=1; cur_units=False
        for kindu,val in _units(block):
            if kindu=='t':
                w=_D1.textlength(val,font=f)+space; h=round(f.size*0.6)
            else:
                mw,mh2=math_wh(val)
                if mw>BODYW:
                    ratio=BODYW/mw
                    assert ratio>=.55, val
                    mw=BODYW; mh2=round(mh2*ratio)
                w=mw+space; h=mh2
            if lw+w>BODYW and (lw>0 or cur_units):
                total+=max(lead,mh+14); n+=1; lw=0.0; mh=0
            cur_units=True
            lw+=w; mh=max(mh,h)
        total+=max(lead,mh+14)
    _HC[key]=total+8
    return _HC[key]*1.05  # 5% safety: absorb residual wrap drift vs the renderer

def split_long_item(kind, s, label='', limit=480):
    if item_h(kind,s,label)<=limit:
        return [(kind,s)]
    parts=_re.split(r'(?<=[.;:!?])\s+', s)
    out=[]; cur=''
    for p in parts:
        cand=(cur+' '+p).strip()
        if cur and item_h(kind,cand,label)>limit:
            out.append((kind,cur)); cur=p
        else:
            cur=cand
    if cur: out.append((kind,cur))
    changed=True
    while changed:
        changed=False
        for i2,(k2,s2) in enumerate(out):
            if item_h(k2,s2,label)>limit:
                words=s2.split(); mid=max(1,len(words)//2)
                out[i2:i2+1]=[(k2,' '.join(words[:mid])),(k2,' '.join(words[mid:]))]
                changed=True
                break
    return out

_LABEL={'why':'WHY / ','trap':'WATCH / ','check':'CHECK / '}

def fit_card(items):
    hs=[item_h(k,s,_LABEL.get(k,'')) for k,s in items]
    total=sum(hs)
    BUDGET=880
    k=max(1, -(-total//BUDGET))  # ceil
    if k>len(items): k=len(items)
    n=len(items)
    if k<=1:
        return [items]
    # DP: partition items[0:n] into k ordered groups minimising the max group height
    INF=float('inf')
    for _try in range(5):
        dp=[[INF]*(k+1) for _ in range(n+1)]
        choice=[[0]*(k+1) for _ in range(n+1)]
        pref=[0]
        for h in hs: pref.append(pref[-1]+h)
        dp[0][0]=0
        for g in range(1,k+1):
            for e in range(g,n+1):
                for b in range(g-1,e):
                    cand=max(dp[b][g-1], pref[e]-pref[b])
                    if cand<dp[e][g]:
                        dp[e][g]=cand; choice[e][g]=b
        if dp[n][k]>=INF:
            return [items]
        groups=[]; e=n
        for g in range(k,0,-1):
            b=choice[e][g]
            groups.append(items[b:e])
            e=b
        groups.reverse()
        if dp[n][k]<=BUDGET+60 or k>=n:
            # local improvement: trade a little max for a better min
            def gH(g): return sum(item_h(kk,ss,_LABEL.get(kk,'')) for kk,ss in g)
            for _ in range(12):
                hs2=[gH(g) for g in groups]
                M0,m0=max(hs2),min(hs2)
                best=None
                for i2 in range(len(groups)-1):
                    A,B=groups[i2],groups[i2+1]
                    if len(A)>1:
                        A2,B2=A[:-1],[A[-1]]+B
                        M1,m1=max(gH(A2),gH(B2)),min(gH(A2),gH(B2))
                        if m1>m0 and M1<=M0+40:
                            sc=(m1,-M1)
                            if best is None or sc>best[0]: best=(sc,i2,'ab')
                    A,B=groups[i2],groups[i2+1]
                    if len(B)>1:
                        A2,B2=A+[B[0]],B[1:]
                        M1,m1=max(gH(A2),gH(B2)),min(gH(A2),gH(B2))
                        if m1>m0 and M1<=M0+40:
                            sc=(m1,-M1)
                            if best is None or sc>best[0]: best=(sc,i2,'ba')
                if best is None: break
                _,i2,mode=best
                A,B=groups[i2],groups[i2+1]
                if mode=='ab': groups[i2],groups[i2+1]=A[:-1],[A[-1]]+B
                else: groups[i2],groups[i2+1]=A+[B[0]],B[1:]
            return groups
        k+=1
    return groups

def cx_to_cards(c):
    conv=[]
    for it in c['items']:
        if isinstance(it,tuple):
            if it[0]=='D':
                continue
            k={'WHY':'why','CHECK':'check'}.get(it[0],'p')
            s=safe(it[1])
            if k=='p' and s.startswith(('Trap','Traps','WATCH','Mistake','Error')):
                k='trap'
            if k=='p' and s.startswith('Note'):
                pass
            items_src=[(k,s)]
        else:
            s=safe(it)
            k='trap' if s.startswith(('Trap','Traps','WATCH','Mistake','Error')) else 'p'
            items_src=[(k,s)]
        for k2,s2 in items_src:
            conv.extend(split_long_item(k2,s2,_LABEL.get(k2,'')))
    return conv

def flow_balance(cards):
    # cards: list of (title, items); move boundary items between neighbours to equalise heights (order kept)
    def H(g):
        return sum(item_h(k2,s2,_LABEL.get(k2,'')) for k2,s2 in g)
    def var():
        hs=[H(g) for _,g in cards]
        m=sum(hs)/max(1,len(hs))
        return sum((h-m)**2 for h in hs), hs
    for _pass in range(40):
        moved=False
        v0,_=var()
        for i in range(len(cards)-1):
            t1,g1=cards[i]; t2,g2=cards[i+1]
            h1,h2=H(g1),H(g2)
            # candidate A: last item of left card -> front of right card
            if len(g1)>1 and h1>h2:
                mv=g1[-1]
                mh=item_h(mv[0],mv[1],_LABEL.get(mv[0],''))
                if h2+mh<=900:
                    cards[i]=(t1,g1[:-1]); cards[i+1]=(t2,[mv]+g2)
                    v1,_=var()
                    if v1<v0:
                        v0=v1; moved=True
                        continue
                    cards[i]=(t1,g1); cards[i+1]=(t2,g2)  # revert
            t1,g1=cards[i]; t2,g2=cards[i+1]
            h1,h2=H(g1),H(g2)
            # candidate B: first item of right card -> end of left card
            if len(g2)>1 and h2>h1:
                mv=g2[0]
                mh=item_h(mv[0],mv[1],_LABEL.get(mv[0],''))
                if h1+mh<=900:
                    cards[i]=(t1,g1+[mv]); cards[i+1]=(t2,g2[1:])
                    v1,_=var()
                    if v1<v0:
                        v0=v1; moved=True
                        continue
                    cards[i]=(t1,g1); cards[i+1]=(t2,g2)  # revert
        if not moved:
            break
    return cards

def partition_k(items, k):
    # ordered partition of items into k groups minimising the max group height
    hs=[item_h(k2,s2,_LABEL.get(k2,'')) for k2,s2 in items]
    n=len(items)
    if k>=n:
        return [[it] for it in items]
    INF=float('inf')
    dp=[[INF]*(k+1) for _ in range(n+1)]
    choice=[[0]*(k+1) for _ in range(n+1)]
    pref=[0]
    for h in hs: pref.append(pref[-1]+h)
    dp[0][0]=0
    for g in range(1,k+1):
        for e in range(g,n+1):
            for b in range(g-1,e):
                cand=max(dp[b][g-1], pref[e]-pref[b])
                if cand<dp[e][g]:
                    dp[e][g]=cand; choice[e][g]=b
    groups=[]; e=n
    for g in range(k,0,-1):
        b=choice[e][g]
        groups.append(items[b:e])
        e=b
    groups.reverse()
    def gH(g): return sum(item_h(kk,ss,_LABEL.get(kk,'')) for kk,ss in g)
    for _ in range(14):
        hs2=[gH(g) for g in groups]
        M0,m0=max(hs2),min(hs2)
        best=None
        for i2 in range(len(groups)-1):
            A,B=groups[i2],groups[i2+1]
            if len(A)>1:
                A2,B2=A[:-1],[A[-1]]+B
                M1,m1=max(gH(A2),gH(B2)),min(gH(A2),gH(B2))
                if m1>m0 and M1<=M0+20:
                    sc=(m1,-M1)
                    if best is None or sc>best[0]: best=(sc,i2,'ab')
            A,B=groups[i2],groups[i2+1]
            if len(B)>1:
                A2,B2=A+[B[0]],B[1:]
                M1,m1=max(gH(A2),gH(B2)),min(gH(A2),gH(B2))
                if m1>m0 and M1<=M0+20:
                    sc=(m1,-M1)
                    if best is None or sc>best[0]: best=(sc,i2,'ba')
        if best is None: break
        _,i2,mode=best
        A,B=groups[i2],groups[i2+1]
        if mode=='ab': groups[i2],groups[i2+1]=A[:-1],[A[-1]]+B
        else: groups[i2],groups[i2+1]=A+[B[0]],B[1:]
    return groups

def greedy_partition(items, k):
    # sequential partition into k groups closest to equal heights
    hs=[item_h(k2,s2,_LABEL.get(k2,'')) for k2,s2 in items]
    total=sum(hs)
    target=total/k
    groups=[]; cur=[]; acc=0.0
    remain_groups=k
    for i,(it,h) in enumerate(zip(items,hs)):
        items_left=len(items)-i
        if cur and ((acc>=target or acc+h>900) and items_left>remain_groups-1):
            groups.append(cur); cur=[it]; acc=h; remain_groups-=1
        else:
            cur.append(it); acc+=h
    if cur: groups.append(cur)
    while len(groups)<k:
        # split the tallest group at its middle item
        gi=max(range(len(groups)), key=lambda j: sum(item_h(k2,s2,_LABEL.get(k2,'')) for k2,s2 in groups[j]))
        g=groups.pop(gi)
        mid=max(1,len(g)//2)
        groups.insert(gi, g[:mid]); groups.insert(gi+1, g[mid:])
    return groups[:k] if len(groups)>k else groups

def build_pages():
    # section-wide flexible packing: cards keep their titles; pages take the sheet data of their first card
    pages=[]
    counters={'JEE':0,'Olympiad':0}
    seen_sheets={'JEE':set(),'Olympiad':set()}
    for part in ('JEE','Olympiad'):
        entries=[e for e in COM if (e['sheet'].startswith('CM')==(part=='JEE'))]
        tagged=[]   # (entry, base_title, kind, s, is_first_of_card)
        for entry in entries:
            for c in entry['cards']:
                base=plain_title(c['title'])
                conv=cx_to_cards(c)
                for j,(k2,s2) in enumerate(conv):
                    tagged.append((entry, base, k2, s2, j==0))
        items=[(k2,s2) for _,_,k2,s2,_ in tagged]
        H=sum(item_h(k2,s2,_LABEL.get(k2,'')) for k2,s2 in items)
        kbest=4*max(1, round(H/(4*820)))
        if kbest>len(items): kbest=4*max(1, len(items)//4)
        groups=greedy_partition(items, kbest)
        # if any group overflows the card body budget, add four more cards and repack
        while max(sum(item_h(k2,s2,_LABEL.get(k2,'')) for k2,s2 in g) for g in groups)>850 and kbest+4<=len(items):
            kbest+=4
            groups=greedy_partition(items, kbest)
        # build subcards with titles
        subcards=[]; idx=0
        for g in groups:
            entry, base, _, _, first = tagged[idx]
            t = base if first else base+' (cont.)'
            subcards.append((t, g, entry))
            idx+=len(g)
        # equalise within quads
        npages=len(subcards)//4
        for pi in range(npages):
            quad_items=subcards[pi*4:(pi+1)*4]
            quad=flow_balance([[t, g] for t, g, _ in quad_items])
            first_entry=quad_items[0][2]
            e=first_entry
            theme=THEME[e['sheet']]
            if e['sheet'] in seen_sheets[part]:
                ptitle=plain_title(e['cards'][0]['title'])+' (cont.)'
            else:
                ptitle=plain_title(e['cards'][0]['title'])
                seen_sheets[part].add(e['sheet'])
            counters[part]+=1
            n=counters[part]
            page_cards=[dict(title=t, items=[list(x) for x in g]) for t, g in quad]
            pages.append(dict(
                section=part, part_page=n,
                slug=f'{part}-{n:02}-{theme}',
                title=ptitle, subtitle=safe(e['summary']),
                source=SOURCE[e['sheet']], diagrams=[theme+'-a', theme+'-b'],
                takeaway=REMEMBER[e['sheet']], cards=page_cards))
    return pages

# ---------------- theme slugs, remember lines, source lines ----------------
THEME={
 'CM-01':'bodies','CM-02':'hole','CM-03':'explosion','CM-04':'impulse','CM-05':'recoil',
 'CM-06':'classify','CM-07':'coll1d','CM-08':'collcases','CM-09':'eloss','CM-10':'defo',
 'CM-11':'oblique','CM-12':'ninety','CM-13':'pendulum','CM-14':'spring','CM-15':'cmframe',
 'CM-16':'belt','CM-17':'rocket','CM-18':'flux','CM-19':'boat','CM-20':'bounces',
 'CM-21':'wall','CM-22':'traps','CM-23':'route','CM-24':'ledger',
 'OLY-01':'chain3','OLY-02':'scatter','OLY-03':'impapprox','OLY-04':'platform',
 'OLY-05':'peg','OLY-06':'staging','OLY-07':'jet','OLY-08':'fold','OLY-09':'relativ',
 'OLY-10':'hopper','OLY-11':'integrate',
}
REMEMBER={
 'CM-01':'R = (1/M) sum m_i r_i: the mass-weighted average position; symmetry pins it, holes shift it.',
 'CM-02':'Treat a hole as negative mass: R = (M1 r1 - M2 r2)/(M1 - M2); the COM always shifts away from the cut.',
 'CM-03':'M a_cm = F_ext: internal forces cancel in pairs; an explosion scatters fragments around an unperturbed COM path.',
 'CM-04':'J = integral F dt = delta p: the area under the F-t spike; same impulse, shorter time, larger average force.',
 'CM-05':'Total momentum is conserved when the net external impulse vanishes, component by component.',
 'CM-06':'Elastic means e = 1; sticking means e = 0; e measures separation speed over approach speed along the line of impact.',
 'CM-07':'One pair of equations prices every 1-D collision: momentum conservation plus v2 - v1 = -e (u1 - u2).',
 'CM-08':'Equal masses exchange velocities only in 1-D elastic; heavy barely slows; light bounces at nearly 2u1 - u2.',
 'CM-09':'K_loss = 1/2 mu (u1 - u2)^2 (1 - e^2): the reduced mass and approach speed set the stake; e sets the loss.',
 'CM-10':'Deformation impulse mu u_app stores the relative KE; a fraction e^2 springs back; (1 + e) mu u_app is the total jolt.',
 'CM-11':'Resolve along the line of impact (momentum + e) and perpendicular to it (unchanged for smooth spheres).',
 'CM-12':'Equal masses, elastic, target at rest: the velocities separate at 90 degrees; head-on is the one-dimensional limit.',
 'CM-13':'Ballistic pendulum: momentum first (the collision), energy second (the swing) - never the other order.',
 'CM-14':'Post-collision spring compression: elastic beats sticking only when 3M > m; compare with the ratio 2 sqrt(M/(m+M)).',
 'CM-15':'K = 1/2 M v_cm^2 + 1/2 mu v_rel^2; in the CM frame elastic collisions just reverse velocities.',
 'CM-16':'Picking mass up or throwing it down needs force m_dot v; belt power splits half KE, half heat.',
 'CM-17':'Rocket: delta v = v_e ln(m0/m_f); thrust = m_dot v_e; the exhaust momentum is the point, not the pushed air.',
 'CM-18':'Momentum flux: F = m_dot v = lambda v^2 on top of the carried weight; jets push rho A v^2.',
 'CM-19':'Man on boat: horizontal COM fixed; ground displacement = M d/(m + M) opposite to the walk.',
 'CM-20':'Bounce heights fall as e^2n; total distance and time are geometric series in e^2 and e.',
 'CM-21':'Moving wall: v_after - v_w = -e (v_before - v_w); a wall coming at you can double the rebound speed.',
 'CM-22':'Traps: e only along the line of impact; equal bounce angles imply e = 1 on a smooth wall; exchange is 1-D only.',
 'CM-23':'Triage first: COM definition, explosion rides the COM, collisions are momentum + e, stages never mix their laws.',
 'CM-24':'The ledger: six boxed formulas, their limits, and the one table that says which formula when.',
 'OLY-01':'Falling chain: scale reads three times the landed weight, ending at 3mg; momentum flux plus weight, no exceptions.',
 'OLY-02':'Lab angle: tan(theta) = sin(Theta)/(cos(Theta) + m1/m2); heavy projectiles cannot exceed arcsin(m2/m1).',
 'OLY-03':'Impulse approximation: F_impulse dt far exceeds other impulses; gravity is a rounding error in a bat-ball collision.',
 'OLY-04':'Bounce map v_new = (1+e)u - e v; a rising platform pumps energy; in the lift frame it is an ordinary bounce.',
 'OLY-05':'Chain over a peg: a = g(2x-L)/L, v^2 = (2g/L)(x - L/2)^2; peg force falls to zero at x = 0.854L - the chain lets go.',
 'OLY-06':'Staging: with zero structure any split gives v_e ln(M/M_p); the real gain is dropping spent tanks.',
 'OLY-07':'Jet on a plate: F = rho A v^2 normal component; on a moving plate the relative speed (v - u) does the work.',
 'OLY-08':'Folded chain off a smooth edge: v = y sqrt(2g/L) with y the fold depth; leaves the table at sqrt(gL/2).',
 'OLY-09':'p = gamma m v is the unique momentum that conservation keeps covariant; mass stays invariant.',
 'OLY-10':'Hopper cart: loading slows (F = m_dot v), leaking does not; the d(Mv)/dt ledger solves all three modes.',
 'OLY-11':'Three integration patterns: J = int F dt for F(t), work-energy for F(x), the M-v ledger for variable mass.',
}
_SRC_SHORT={
 'CM-01':'3.1','CM-02':'3.2 / E1','CM-03':'3.3 / E2','CM-04':'3.4','CM-05':'3.5 / Q2 Q17',
 'CM-06':'3.6','CM-07':'3.7','CM-08':'3.7 / E3 Q3 Q11','CM-09':'3.7-3.8 / E4 P32','CM-10':'3.6-3.7 (Cengage 1.22 added)',
 'CM-11':'3.8','CM-12':'3.8 / E6','CM-13':'3.11 / E5 P29','CM-14':'3.13 / Q18 P35','CM-15':'3.9 / P36',
 'CM-16':'3.10 / E7 P34','CM-17':'3.10 / E10 Q25','CM-18':'3.10 / Q13 P34 OL9','CM-19':'3.12 / E8 Q10',
 'CM-20':'3.6 / Q5 P25 P31','CM-21':'3.13 / E9 Q14','CM-22':'8 traps / C9 C12','CM-23':'9 playbook','CM-24':'4 ledger / 13 sheet',
 'OLY-01':'OL1 / D7.10','OLY-02':'OL2','OLY-03':'OL3','OLY-04':'OL6','OLY-05':'OL7',
 'OLY-06':'OL8 / P30','OLY-07':'OL9','OLY-08':'OL10','OLY-09':'OL5','OLY-10':'3.10 / E7 (synthesis)','OLY-11':'OL7 method / 3.9-3.13 (methods)',
}
SOURCE={k:'Source: centre-of-mass-momentum/Centre-of-mass-momentum.md sec. '+v+'; independently checked' for k,v in _SRC_SHORT.items()}

# ---------------- preflight math, build, measure, dump ----------------
_parser=_MTP('path')
def preflight_text(s):
    for part in _re.split(r'(\$[^$]+\$)', s):
        if len(part)>2 and part[0]=='$' and part[-1]=='$':
            _parser.parse('$'+normalize(part[1:-1])+'$', dpi=72)

PAGES=build_pages()
for p in PAGES:
    preflight_text(p['subtitle']); preflight_text(p['takeaway'])
    for c in p['cards']:
        for kind, s in c['items']:
            preflight_text(s)
        title_w=_D1.textlength(c['title'], font=_IF.truetype(_FPATH, 56))
        while title_w>1380:
            c['title']=c['title'][:-2].rstrip()+'.'
            title_w=_D1.textlength(c['title'], font=_IF.truetype(_FPATH, 56))

fills=[]
for p in PAGES:
    for c in p['cards']:
        used=sum(item_h(k,s,_LABEL.get(k,'')) for k,s in c['items'])+104
        fills.append((used/1028.0, p['slug'], c['title'][:40]))
fills.sort()
print('cards total:', len(fills))
print('fill min/median/max: %.2f / %.2f / %.2f' % (fills[0][0], fills[len(fills)//2][0], fills[-1][0]))
print('lowest 8:', [(round(f,2), t) for f, _, t in fills[:8]])
print('pages:', len(PAGES), 'JEE:', sum(1 for p in PAGES if p['section']=='JEE'), 'Oly:', sum(1 for p in PAGES if p['section']=='Olympiad'))

(ROOT/'sheets.json').write_text(json.dumps(PAGES, indent=1)+'\n')
print('wrote sheets.json')

