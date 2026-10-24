"""Authoring source for the JEE-only, single-column Capacitors note sheets.

Run `python3 author_notes.py` to write `sheets.json`. The renderer never edits
content: this file is where the physics, wording and page order are decided.

Design rules (agreed 2026-10-24):
  * JEE Main + Advanced only. The six Olympiad extension sheets were audited
    item by item; the six ideas that are genuinely JEE *methods* were merged
    into the flow, the rest retired. See AUDIT.md.
  * One vertical column, 7 pages, several concepts per page.
  * Teacher order inside a section: statement -> symbols -> result box ->
    worked numbers -> trap -> what to remember.
  * Text runs are ASCII except the glyphs Patrick Hand really has
    (2 3 1/2 sqrt x - deg pi). Everything else goes in a $math$ run.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def h(n, t, tag=None):
    return {'k': 'h', 'n': n, 't': t, **({'tag': tag} if tag else {})}


def p(s):
    return {'k': 't', 's': s}


def m(s):
    return {'k': 'm', 's': s}


def res(label, lines):
    return {'k': 'res', 't': label, 'lines': lines}


def ex(label, lines):
    return {'k': 'ex', 't': label, 'lines': lines}


def trap(s):
    return {'k': 'trap', 's': s}


def rem(s):
    return {'k': 'rem', 's': s}


def tab(head, rows, w=None):
    return {'k': 'tab', 'head': head, 'rows': rows, **({'w': w} if w else {})}


def dia(key, height=440, caption=None):
    return {'k': 'dia', 'key': key, 'h': height, **({'cap': caption} if caption else {})}


SHEETS = [

    # ------------------------------------------------------------------ 1
    {
        'slug': 'JEE-01-conductor-toolkit',
        'section': 'JEE', 'page': 1, 'part_page': 1,
        'title': 'A conductor decides the field before you calculate',
        'sub': 'Four facts about metal answer most electrostatics questions. Fix them first, then reach for a formula.',
        'source': 'Concepts from Capacitors.md ch.1-2',
        'blocks': [
            h('1', 'Equilibrium: the four facts', 'RESULT'),
            p('Inside a conductor at equilibrium the field is zero, so the whole piece of metal - cavity walls included - is one equipotential. Just outside, the field is normal to the surface and equals $E=\\sigma/\\varepsilon_0$, and excess charge sits on the outer surface.'),
            p('The reason is self-correction: a tangential field would keep pushing free electrons until it cancelled itself, so only the normal part survives.'),
            res('learn these four', [
                '$E_{\\mathrm{inside}}=0$;  the conductor is a single potential',
                'just outside: $E=\\sigma/\\varepsilon_0$, perpendicular to the metal',
                'a cavity holding $+q$ shows $-q$ inside and $+q$ on the outer surface',
                'an empty cavity is shielded from outside fields',
            ]),
            trap('$E=0$ is not $V=0$. A charged shell has no field inside and still sits at $V=kQ/R$: zero slope, non-zero height.'),
            h('2', 'Potential is the number that adds'),
            p('Outside a sphere $V=kQ/r$ and $E=kQ/r^2$; inside a shell $V=kQ/R$ is constant while $E=0$. The link is $V_B-V_A=-\\int_A^B\\vec E\\cdot d\\vec l$, that is $\\vec E=-\\nabla V$: a field is a slope, a potential is a height.'),
            ex('one line of numbers', [
                'Radius $10\\ \\mathrm{cm}$, charge $1\\ \\mu\\mathrm{C}$: $V_s=9.0\\times10^4\\ \\mathrm{V}$, $E_s=9.0\\times10^5\\ \\mathrm{V/m}$. Both fall off outside as $1/r$ and $1/r^2$.',
            ]),
            h('3', 'Gauss in three steps', 'RESULT'),
            p('Symmetry first: name the surface where $|\\vec E|$ is constant and $\\vec E$ is parallel or perpendicular to $d\\vec A$. Then write $\\oint\\vec E\\cdot d\\vec A=Q_{\\mathrm{enc}}/\\varepsilon_0$. Only then take $E$ outside the integral.'),
            tab(['source', 'field at distance r', 'note'], [
                ['point charge, outside a sphere', '$kQ/r^2$', 'the starting point'],
                ['inside a uniform solid sphere', '$\\rho r/3\\varepsilon_0$', 'zero at the centre'],
                ['long line, $\\lambda$ per length', '$\\lambda/2\\pi\\varepsilon_0 r$', 'falls as $1/r$'],
                ['large sheet, $\\sigma$ per face', '$\\sigma/2\\varepsilon_0$', 'away on both sides'],
                ['conductor surface', '$\\sigma/\\varepsilon_0$', 'one side only'],
                ['infinite slab, half-width $a$', '$\\rho x/\\varepsilon_0$', 'outside: $\\rho a/\\varepsilon_0$'],
            ], w=[.44, .3, .26]),
            h('4', 'What this buys in capacitor problems'),
            p('A capacitor is two conductors, and only the field between them sets the terminal voltage. Grounding fixes $V=0$ and lets charge flow; isolation fixes net charge and leaves $V$ free. Order of work: name the terminals, say what is fixed, then compute.'),
            trap('One charged plate gives $\\sigma/2\\varepsilon_0$, but a capacitor gap gives $\\sigma/\\varepsilon_0$ - two plates, two contributions. Charging one plate alone does not set the gap field.'),
            dia('sphere_fields', 560, 'Flat potential, zero field inside; the step at $r=R$ is where the charge sits.'),
            rem('Say where the charge sits, then what the potential is. Neither step needs a capacitor formula.'),
        ],
    },

    # ------------------------------------------------------------------ 2
    {
        'slug': 'JEE-02-capacitance-geometries',
        'section': 'JEE', 'page': 2, 'part_page': 2,
        'title': 'Capacitance: one definition, one plate rule, three geometries',
        'sub': 'Charge needed per volt. Geometry and medium set it; the charge already stored does not.',
        'source': 'Concepts from Capacitors.md ch.2-3',
        'blocks': [
            h('1', 'The definition, used correctly'),
            p('$C=Q/V$, with $V$ the potential difference between the conductors and $Q$ the charge on the positive one. Scale every charge and every potential scales with it, so the ratio is geometry and medium only. An isolated conductor has its second plate at infinity: a sphere gives $C=4\\pi\\varepsilon_0R$.'),
            trap('A capacitor holds $+Q$ and $-Q$, so its net charge is zero. "Charge on the capacitor" always means the positive plate; writing $Q$ for the pair is the first mistake in the chapter.'),
            h('2', 'Parallel plates, and the slab that covers everything', 'RESULT'),
            p('Opposite plates give $E=Q/\\varepsilon_0A$ in the gap and cancel outside. Then $V=Ed$ and the ratio is the plate formula. A slab of thickness $t$ replaces part of the gap, and one expression covers dielectric, metal and vacuum.'),
            res('plate, dielectric, metal', [
                '$C=\\dfrac{\\varepsilon_0A}{d}$;  with $K$ filling the gap $C=\\dfrac{K\\varepsilon_0A}{d}$;  with a slab $C=\\dfrac{\\varepsilon_0A}{d-t+t/K}$',
                'metal is the limit $K\\to\\infty$: $C=\\dfrac{\\varepsilon_0A}{d-t}$;  two layers: $\\dfrac{1}{C}=\\dfrac{t_1}{K_1\\varepsilon_0A}+\\dfrac{t_2}{K_2\\varepsilon_0A}$',
                '$\\varepsilon_0=8.85\\times10^{-12}\\ \\mathrm{F/m}$, $\\ 4\\pi\\varepsilon_0=1.11\\times10^{-10}\\ \\mathrm{F/m}$',
            ]),
            ex('two plates, two answers', [
                'Area $100\\ \\mathrm{cm^2}$, gap $1\\ \\mathrm{mm}$: air gives $88.5\\ \\mathrm{pF}$, $K=5$ gives $443\\ \\mathrm{pF}$. Doubling the gap halves $C$; only the total thickness of each layer matters, never where a slab sits.',
            ]),
            h('3', 'Stacks, patches and unequal plates'),
            p('Interleaved plates are gaps in parallel: $n$ plates give $n-1$ gaps and $C=(n-1)\\varepsilon_0A/d$. Two facing plates carrying $Q_1,Q_2$ settle with facing charges $\\pm(Q_1-Q_2)/2$, so $V_1-V_2=(Q_1-Q_2)d/2\\varepsilon_0A$.'),
            trap('Use the overlap area, never the sum of the two plate areas. And $C=\\varepsilon_0A/d$ assumes $d$ is small compared with the plate width; fringing at the edges always adds a little.'),
            h('4', 'Sphere, cylinder, and connected conductors', 'RESULT'),
            res('derive once, then quote', [
                'concentric spheres: $C=4\\pi\\varepsilon_0\\dfrac{ab}{b-a}$;  $b\\to\\infty$ returns the isolated sphere',
                'coaxial cylinders: $C=\\dfrac{2\\pi\\varepsilon_0L}{\\ln(b/a)}$',
                'two distant spheres with opposite charges: $C\\simeq4\\pi\\varepsilon_0\\dfrac{ab}{a+b}$',
                'sphere of radius $a$ coated to $b$ with dielectric $K$: $\\dfrac{1}{C}=\\dfrac{(1/a-1/b)/K+1/b}{4\\pi\\varepsilon_0}$',
            ]),
            p('Two spheres on a long wire share potential, not charge: $Q_a/Q_b=a/b$, so the smaller one carries the larger surface field $kQ/R^2$. That is why a pointed conductor sparks first.'),
            dia('slab_cases', 420, 'Every gap is the plate formula with the filled thickness replaced by $t/K$; metal is the limit $K\\to\\infty$.'),
            rem('$C$ is geometry plus medium. Name the terminals, then either quote a standard result or integrate $E$ once.'),
        ],
    },

    # ------------------------------------------------------------------ 3
    {
        'slug': 'JEE-03-networks',
        'section': 'JEE', 'page': 3, 'part_page': 3,
        'title': 'Networks: islands, bridges, ladders',
        'sub': 'Wires make islands. Charge is conserved on each island, not on each capacitor - that one sentence solves every network.',
        'source': 'Concepts from Capacitors.md ch.6-7',
        'blocks': [
            h('1', 'Series, parallel, and where the energy goes'),
            res('combinations', [
                'series: $\\dfrac{1}{C_{\\mathrm{eq}}}=\\sum\\dfrac{1}{C_i}$, same charge, voltages add as $1/C$',
                'parallel: $C_{\\mathrm{eq}}=\\sum C_i$, same voltage, charges add as $C$',
                'energy: series $\\dfrac{U_i}{U}=\\dfrac{C_{\\mathrm{eq}}}{C_i}$,  parallel $\\dfrac{U_i}{U}=\\dfrac{C_i}{C_{\\mathrm{eq}}}$',
            ]),
            p('In series the smallest capacitor takes the largest voltage, so a chain is limited by its weakest member, not by the sum of the ratings. In parallel each one sees the full voltage.'),
            trap('Series or parallel is decided by the wires, not by how the symbols are drawn - redraw first. A precharged middle island also breaks the "equal charge in series" rule.'),
            h('2', 'The island method that never fails', 'METHOD'),
            p('Use it whenever a network cannot be folded with confidence. It is charge conservation, written once per conductor.'),
            res('four steps', [
                '1. Mark the islands: plates joined by a wire are one electrode.',
                '2. Label each: grounded $\\Rightarrow V=0$; battery-connected $\\Rightarrow$ difference fixed; floating $\\Rightarrow$ net charge fixed.',
                '3. For every floating island write $\\sum_j C_{ij}(V_i-V_j)=Q_i^{\\mathrm{initial}}$, keeping the plate signs.',
                '4. Solve for the potentials, then read each capacitor as $q=C\\,\\Delta V$.',
            ]),
            h('3', 'Bridges, symmetry, standard results', 'RESULT'),
            res('worth memorising', [
                'balanced bridge: $\\dfrac{C_1}{C_2}=\\dfrac{C_3}{C_4}$; the bridge capacitor then carries no charge',
                'cube of twelve equal $C$: opposite vertices $\\dfrac{6C}{5}$, edge $\\dfrac{12C}{7}$, face diagonal $\\dfrac{4C}{3}$',
                'infinite ladder (series $C$, shunt $C$): $X=\\dfrac{\\sqrt5-1}{2}C$',
                'star-delta with $S=ab+bc+ca$: arms $x=S/b$, $y=S/c$, $z=S/a$;  back: $C_{12}=xy/(x+y+z)$',
            ]),
            p('Each result comes from equal potentials, not from the drawing: fold two nodes only after proving the excitation treats them alike, and state the terminals.'),
            trap('Do not copy the resistor star-delta across. The capacitor star arm is a sum of products divided by one branch, the reciprocal arrangement of the resistor rule.'),
            ex('reduce, then audit the pieces', [
                '$6\\ \\mu\\mathrm{F}$ and $3\\ \\mu\\mathrm{F}$ in series give $2\\ \\mu\\mathrm{F}$; with $4\\ \\mu\\mathrm{F}$ in parallel, $C_{\\mathrm{eq}}=6\\ \\mu\\mathrm{F}$. At $12\\ \\mathrm{V}$: $Q=72\\ \\mu\\mathrm{C}$, $U=432\\ \\mu\\mathrm{J}$.',
                'Audit: the series pair holds $24\\ \\mu\\mathrm{C}$ at $4\\ \\mathrm{V}$ and $8\\ \\mathrm{V}$, the $4\\ \\mu\\mathrm{F}$ holds $48\\ \\mu\\mathrm{C}$ - and $24+48=72$.',
            ]),
            h('4', 'Charge through a wire'),
            p('It is not $C\\Delta V$ in general. Cut the circuit with a surface crossed by that wire only; the charge that crossed equals the change in enclosed plate charge, signs included.'),
            dia('bridge', 280, 'Balanced means $V_X=V_Y$: delete the bridge. Otherwise write one island equation at $X$ and one at $Y$.'),
            rem('Name the terminals, mark the islands, conserve charge island by island. Folding is a shortcut that must be justified.'),
        ],
    },

    # ------------------------------------------------------------------ 4
    {
        'slug': 'JEE-04-energy-battery-heat',
        'section': 'JEE', 'page': 4, 'part_page': 4,
        'title': 'Energy, the battery, and the heat bill',
        'sub': 'One question decides every sign: is the charge held fixed, or the voltage?',
        'source': 'Concepts from Capacitors.md ch.4, ch.10',
        'blocks': [
            h('1', 'Stored energy and the missing half', 'RESULT'),
            res('energy', [
                '$U=\\dfrac{Q^2}{2C}=\\dfrac12 QV=\\dfrac12 CV^2$;  per unit volume $u=\\dfrac12\\varepsilon_0E^2$',
            ]),
            p('Charge is pushed in while the voltage climbs from $0$ to $V$, so the work is the area of a triangle, not a rectangle - hence the half. The energy lives in the field in the gap; the metal holds no field and stores nothing.'),
            ex('the check that catches sign errors', [
                '$2\\ \\mu\\mathrm{F}$ at $100\\ \\mathrm{V}$: $Q=200\\ \\mu\\mathrm{C}$ and $U=0.1\\ \\mathrm{J}$. Pull the plates to twice the gap with the battery off: $C$ halves, $Q$ stays, so $V$ and $U$ double - you supplied that work.',
            ]),
            h('2', 'The one fork: fixed Q or fixed V', 'TABLE'),
            tab(['after full dielectric insertion', 'fixed $Q$ (battery off)', 'fixed $V$ (battery on)'], [
                ['$C$', 'grows by $K$', 'grows by $K$'],
                ['$V$', 'falls by $K$', 'unchanged'],
                ['$E$ in the gap', 'falls by $K$', 'unchanged, $V/d$'],
                ['$Q$', 'unchanged', 'grows by $K$'],
                ['$U$', 'falls by $K$', 'grows by $K$'],
                ['battery work', 'zero', '$V^2\\Delta C$'],
            ], w=[.4, .3, .3]),
            p('At the same instant both columns describe the same force, because $Q=CV$ is the same state. The constraint decides how the state moves next, not what the force is now.'),
            trap('Battery work is not field energy. At fixed $V$ the cell keeps feeding charge as $C$ grows, so differentiating $\\frac12CV^2$ alone gives the force with the wrong sign.'),
            h('3', 'Bookkeeping for one move, and the heat bill', 'RESULT'),
            res('two ledgers', [
                'slab drawn in at fixed $V$: battery supplies $V^2\\Delta C$, field energy rises $\\frac12V^2\\Delta C$, the other half leaves as mechanical work or heat',
                'two capacitors joined: $V_f=\\dfrac{C_1V_1+C_2V_2}{C_1+C_2}$,  heat $H=\\dfrac{C_1C_2}{2(C_1+C_2)}(V_1-V_2)^2$',
                'charging an empty $C$ from a cell $E$: cell does $CE^2$, capacitor keeps $\\frac12CE^2$, half is lost whatever $R$ is',
            ]),
            p('The loss does not depend on the resistance: a small $R$ gives a large current for a short time and the same integral. Only an ideal zero-$R$, zero-$L$ connection is singular.'),
            h('4', 'Two results worth carrying'),
            p('Heat is never negative, and it equals $\\frac12C(V_0-V_\\infty)^2$ whenever a single capacitor settles to a new voltage. Energy decays twice as fast as voltage in any RC decay, because $U\\propto V^2$.'),
            ex('numbers on the heat bill', [
                '$C_1=2\\ \\mu\\mathrm{F}$ at $100\\ \\mathrm{V}$, $C_2=3\\ \\mu\\mathrm{F}$ uncharged. Joined: $V_f=40\\ \\mathrm{V}$, and $H=\\frac12\\cdot\\frac{6}{5}\\ \\mu\\mathrm{F}\\cdot(100)^2=6\\ \\mathrm{mJ}$.',
                'Check: before $10\\ \\mathrm{mJ}$, after $4\\ \\mathrm{mJ}$ - the missing $6\\ \\mathrm{mJ}$ is the heat.',
            ]),
            dia('energy_triangle', 510, 'Work is the area under the $V$-$q$ line. A triangle, so the half.'),
            rem('Fixed $Q$: differentiate $U$. Fixed $V$: differentiate $U-QV$, or add the battery term by hand.'),
        ],
    },

    # ------------------------------------------------------------------ 5
    {
        'slug': 'JEE-05-force-insertion',
        'section': 'JEE', 'page': 5, 'part_page': 5,
        'title': 'Force: plates, dielectrics and one image charge',
        'sub': 'Find C(x), state the constraint, differentiate. Never integrate the field unless the question asks for the pressure at a point.',
        'source': 'Concepts from Capacitors.md ch.5, plus the image method',
        'blocks': [
            h('1', 'Force on a plate', 'RESULT'),
            res('the two forms', [
                'attraction: $F=\\dfrac{Q^2}{2\\varepsilon_0A}=\\dfrac{\\varepsilon_0AV^2}{2d^2}$;  pressure $p=\\dfrac{\\sigma^2}{2\\varepsilon_0}$',
            ]),
            p('The factor $\\frac12$ is the physics: a plate does not pull on itself, so only the field of the other plate (half the total gap field) acts on it. Equivalently, $F=-dU/dx$ at fixed $Q$, or $-d(U-QV)/dx$ at fixed $V$.'),
            trap('Do not write $F=QE$ with the full gap field $\\sigma/\\varepsilon_0$. The correct force is $QE/2$; that factor is the whole question.'),
            h('2', 'A dielectric is always pulled inward', 'RESULT'),
            res('slab and liquid', [
                'slab entering by $x$: $C(x)=\\dfrac{\\varepsilon_0w}{d}[L+(K-1)x]$,  $F=\\dfrac{\\varepsilon_0(K-1)w}{2d}V^2$',
                'at fixed $V$ that force is constant; at fixed $Q$ use $V=Q/C(x)$ and it falls as the slab goes in',
                'liquid climbing between plates: $h=\\dfrac{\\varepsilon_0(K-1)V^2}{2\\rho gd^2}$',
            ]),
            p('The force always points toward larger capacitance, at fixed $Q$ as well as at fixed $V$; only the size of the force differs. For the liquid, balance the electric force per unit width against the weight $\\rho gdh$ of the raised column.'),
            h('3', 'Energy of a charged sphere, and the pressure it feels'),
            p('An isolated conducting sphere has $U=Q^2/8\\pi\\varepsilon_0R$ and an outward surface pressure $Q^2/32\\pi^2\\varepsilon_0R^4$. Expanding it increases $C$ and lowers $U$, which is where the outward push comes from. A uniformly charged solid sphere is different: $U=3Q^2/20\\pi\\varepsilon_0R$, because the charge is spread through the volume.'),
            trap('A symmetric charged sphere feels no net translational force, even though every surface element is pushed outward. Net force and pressure are different questions.'),
            h('4', 'Image charge: the one extension worth keeping', 'KEPT'),
            p('For a charge above a grounded conducting plane, replace the plane by a mirror charge $-q$ at depth $h$. It is a bookkeeping device, valid only above the plane, and it answers a whole family of JEE questions in one line.'),
            res('charge q at height h above a grounded plane', [
                '$F=\\dfrac{q^2}{16\\pi\\varepsilon_0h^2}$ with separation $2h$;  $W=\\dfrac{q^2}{16\\pi\\varepsilon_0h}$;  induced charge on the plane $=-q$',
                'the field at the surface gives surface charge density $\\sigma=-qh/2\\pi(\\rho^2+h^2)^{3/2}$',
            ]),
            trap('The energy is half of $q\\times$ the image potential. Writing $q^2/8\\pi\\varepsilon_0h$ double counts the work of building the induced charge.'),
            h('5', 'Stretch: a plate on a spring'),
            p('A plate held at gap $d$ above a fixed plate by a spring of stiffness $k$ is the cleanest test of force plus stability. Equilibrium needs $kx=\\varepsilon_0AV^2/2(d-x)^2$, and the two solutions merge at $x=d/3$, where $V^2=8kd^3/27\\varepsilon_0A$: beyond that voltage the plate snaps down. At fixed charge the force $Q^2/2\\varepsilon_0A$ does not depend on the gap, so no snap-down is possible.'),
            dia('insertion', 405, 'The filled part and the empty part are two capacitors in parallel; increasing the overlap raises C, so the slab is pulled in.'),
            rem('Write C(x), name the constraint, differentiate the right energy. Force always points to larger C.'),
        ],
    },

    # ------------------------------------------------------------------ 6
    {
        'slug': 'JEE-06-dielectrics',
        'section': 'JEE', 'page': 6, 'part_page': 6,
        'title': 'Dielectrics: what changes, what does not',
        'sub': 'A dielectric polarises. Whether the field falls depends on the constraint, and whether it is a layer or a patch decides the formula.',
        'source': 'Concepts from Capacitors.md ch.8, ch.11',
        'blocks': [
            h('1', 'What the material does'),
            p('Molecules stretch and align, putting bound charge on the faces. That bound charge opposes the free charge, so at fixed free charge the field and the voltage fall by $K$ while $C$ rises by $K$. With the battery still on, $V$ is pinned, the field stays $V/d$, and the cell pushes in extra free charge.'),
            res('one-line summary', [
                'fixed $Q$: $E=\\dfrac{E_0}{K}$, $V=\\dfrac{V_0}{K}$, $C=KC_0$, $U=\\dfrac{U_0}{K}$',
                'fixed $V$: $E=E_0=\\dfrac{V}{d}$, $C=KC_0$, $Q=KQ_0$, $U=KU_0$',
            ]),
            trap('"A dielectric always reduces the field" is false. It reduces $E$ only at fixed charge; with the battery on and the gap full, $E$ is untouched and the charge grows instead.'),
            h('2', 'Two golden cases: layers or patches', 'RESULT'),
            p('Cut the capacitor the right way and the geometry names the rule. Stack layers along the field: the same flux crosses each, so voltages add - series. Place patches across the area: they share the voltage, so charges add - parallel.'),
            res('both cases on one page', [
                'layers (series): $C=\\dfrac{\\varepsilon_0A}{d-t+t/K}$;  half the thickness filled: $C=\\dfrac{2KC_0}{K+1}$',
                'patches (parallel): $C=\\dfrac{\\varepsilon_0A}{d}\\left[1+(K-1)\\dfrac{x}{L}\\right]$;  half the area filled: $C=C_0\\dfrac{K+1}{2}$',
                'no free charge at the interface: $D_{1n}=D_{2n}$ and $E_{1t}=E_{2t}$',
            ]),
            p('The interface conditions are the reason the two cases differ: normal $D$ is continuous, so $E$ drops by $K$ across a layer; tangential $E$ is continuous, so the field is unbroken along a patch.'),
            trap('Which case is which? Cut the plates into pieces and you have patches. Cut across the gap and you have layers. A metal slab is the layer recipe with $K\\to\\infty$.'),
            h('3', 'Dielectric strength sets the design', 'RATING'),
            res('ratings', [
                'breakdown: $V_{\\max}=E_bd$ for a nearly uniform field;  best stored density $\\dfrac12\\varepsilon E_b^2$',
                'air: $E_b\\approx3\\times10^6\\ \\mathrm{V/m}=3\\ \\mathrm{kV/mm}$; a $0.1\\ \\mathrm{mm}$ gap holds about $300\\ \\mathrm{V}$',
                'in series the smallest capacitor takes the largest voltage: check each element, not the total',
            ]),
            p('Large $K$ buys capacitance, not safety: useful energy storage needs both a large $K$ and a large $E_b$. Sharp edges and trapped voids concentrate the local field far above $V/d$, so real capacitors fail below the average-field estimate.'),
            h('4', 'Six checks before you hand in'),
            p('Dimensions: an isolated body has $C\\sim\\varepsilon_0\\times$ length. Limits: $K\\to1$ returns vacuum, $b\\to\\infty$ returns the isolated sphere. Signs: heat cannot be negative and a dielectric is always pulled toward larger $C$. Endpoints: a transient starts and ends at values the circuit allows. Stability: check curvature when equilibrium is asked. Ratings: compare each local field with $E_b$.'),
            dia('dielectric_layers', 540, 'Layers in series: same normal $D$, voltages add. Patches in parallel: same $V$, charges add.'),
            rem('Fixed $Q$ the field falls by $K$; fixed $V$ it does not. Layers add voltages; patches add charges.'),
        ],
    },

    # ------------------------------------------------------------------ 7
    {
        'slug': 'JEE-07-rc-and-ac',
        'section': 'JEE', 'page': 7, 'part_page': 7,
        'title': 'RC transients, and the capacitor in AC',
        'sub': 'One capacitor plus resistors is always three numbers. Then two switch rules answer the rest.',
        'source': 'Concepts from Capacitors.md ch.9-10, JEE parts of ch.12',
        'blocks': [
            h('1', 'Three numbers, every time', 'METHOD'),
            res('the three-number method', [
                '$V(t)=V_\\infty+(V_0-V_\\infty)e^{-t/\\tau}$,  $\\tau=R_{\\mathrm{th}}C$',
                '$V_0$: capacitor voltage before switching - it cannot jump',
                '$V_\\infty$: remove the capacitor (open) and solve the resistors',
                '$R_{\\mathrm{th}}$: resistance seen from the capacitor terminals, sources killed, dependent sources kept',
            ]),
            p('Clock: one time constant is 63 %, two 86 %, three 95 %, five 99.3 %. Inverting the exponential is the most used line in the chapter: $t=\\tau\\ln\\dfrac{V_\\infty-V_0}{V_\\infty-V(t)}$.'),
            h('2', 'Charging, discharging, heat'),
            res('one capacitor, one resistor', [
                'charge from a cell $E$: $V_C=E(1-e^{-t/RC})$,  $i=\\dfrac{E}{R}e^{-t/RC}$',
                'discharge: $V=V_0e^{-t/RC}$ and $U=U_0e^{-2t/RC}$ - energy dies twice as fast as voltage',
                'settling heat: $H=\\dfrac12C(V_0-V_\\infty)^2$, independent of $R$',
            ]),
            p('Leakage is why a real capacitor loses its voltage: a resistance $R_p$ across it decays the charge with time constant $R_pC$.'),
            h('3', 'The two switch rules', 'KEPT'),
            res('t = 0+ and t = infinity', [
                'at $t=0^+$: an uncharged capacitor behaves like a wire; a charged one like a fixed voltage source',
                'at $t=\\infty$: every capacitor is an open circuit',
                'so a step into a capacitive divider divides by $C$; the final state divides by $R$',
            ]),
            p('These two rules answer an initial-and-final question with no differential equation - which is most of what is asked.'),
            ex('worked to the last digit', [
                '$2\\ \\mu\\mathrm{F}$ at $10\\ \\mathrm{V}$ discharged through $1\\ \\mathrm{M}\\Omega$: $\\tau=2\\ \\mathrm{s}$, so at $t=2\\ \\mathrm{s}$ the voltage is $10e^{-1}=3.68\\ \\mathrm{V}$.',
                'Energy falls from $100\\ \\mu\\mathrm{J}$ to $13.5\\ \\mu\\mathrm{J}$; the missing $86.5\\ \\mu\\mathrm{J}$ is heat in the resistor.',
            ]),
            h('4', 'Reservoir capacitor and AC'),
            res('ripple and reactance', [
                'ripple: $\\Delta V\\approx I_{\\mathrm{load}}\\Delta t/C$ - a $1\\ \\mathrm{A}$ load fed every $10\\ \\mathrm{ms}$ with $0.5\\ \\mathrm{V}$ ripple needs $20\\ \\mathrm{mF}$',
                '$X_C=\\dfrac{1}{\\omega C}$, $\\omega=2\\pi f$;  current leads the voltage by $90^\\circ$',
                'series $RC$: $Z=\\sqrt{R^2+X_C^2}$,  $\\phi=-\\arctan(X_C/R)$;  at $X_C=R$ the current leads by $45^\\circ$',
            ]),
            p('"Blocks DC, passes AC": at high frequency $X_C\\to0$ it is a short, at DC it is an open.'),
            trap('At DC steady state a capacitor is open, but its voltage need not be zero. Replacing it by a wire is the $t=0^+$ picture, not the final one.'),
            h('5', 'The meter changes the reading', 'KEPT'),
            p('A voltmeter of input capacitance $C_m$ across an isolated capacitor $C_s$ shares the charge and reads $V_0C_s/(C_s+C_m)$. It is the joining-two-capacitors result in disguise, and the reason a small capacitor needs a high-impedance probe.'),
            dia('charging', 370, 'Voltage rises as $1-e^{-t/\\tau}$ while current falls as $e^{-t/\\tau}$; their areas settle the energy books.'),
            rem('Three numbers: $V_0$, $V_\\infty$, $\\tau=R_{\\mathrm{th}}C$. At $t=0^+$ a capacitor is a wire or a source; at $t=\\infty$ it is open.'),
        ],
    },
]


def build():
    data = {
        'edition': 'capacitors-jee-dense-v2',
        'canvas': [2480, 3508],
        'dpi': 300,
        'policy': 'JEE Main + Advanced only; Olympiad sheets retired 2026-10-24 (see AUDIT.md)',
        'sheets': SHEETS,
    }
    (ROOT / 'sheets.json').write_text(json.dumps(data, indent=1) + '\n')
    prose = 0
    for s in SHEETS:
        for b in s['blocks']:
            for t in ([b['s']] if 's' in b else []) + b.get('lines', []) + [c for r in b.get('rows', []) for c in r]:
                prose += len(re.sub(r'\$[^$]*\$', 'X', t).split())
    print(f'wrote sheets.json: {len(SHEETS)} pages, {prose} prose words')


if __name__ == '__main__':
    import re
    build()
