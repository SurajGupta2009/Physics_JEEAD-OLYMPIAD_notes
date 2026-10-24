"""Authoring source for the JEE-only, single-column Capacitors note sheets.

Run `python3 author_notes.py` to write `sheets.json`.

Design rules (v3, agreed 2026-10-24):
  * JEE Main + Advanced only. Olympiad extension sheets audited out; the six
    ideas that are real JEE methods were merged in (see AUDIT.md).
  * Single column, 8 pages, two figures per page.
  * Every quoted formula is derived in a DERIVE block, in at most four lines.
  * A WHY note gives the physical reason before the algebra.
  * Teacher order: base idea -> derivation -> result -> numbers -> trap -> remember.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def h(n, t, tag=None):
    return {'k': 'h', 'n': n, 't': t, **({'tag': tag} if tag else {})}


def p(s):
    return {'k': 't', 's': s}


def why(s):
    return {'k': 'why', 's': s}


def der(t, lines):
    return {'k': 'der', 't': t, 'lines': lines}


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


def dias(items, height=300):
    return {'k': 'dias', 'items': items, 'h': height}


SHEETS = [

    # ------------------------------------------------------------------ 1
    {
        'slug': 'JEE-01-conductor-toolkit',
        'section': 'JEE', 'page': 1, 'part_page': 1,
        'title': 'A conductor decides the field before you calculate',
        'sub': 'Every conductor fact comes from one sentence: free charges move until they stop moving.',
        'source': 'Capacitors.md ch.1-2',
        'blocks': [
            h('1', 'The four facts, each derived'),
            why('A metal has free electrons. If anything pushes them, they move. Equilibrium means they have stopped, so nothing is pushing them.'),
            der('why the field inside is zero', [
                'If $E$ were non-zero inside, a free electron would feel $eE$ and move. It has stopped, so $E_{\\mathrm{inside}}=0$.',
            ]),
            der('why the field must be perpendicular to the surface', [
                'On the surface the potential is constant. Along the surface $dV=0$, and $dV=-\\vec E\\cdot d\\vec l$ for every such $d\\vec l$: only the normal component survives.',
            ]),
            der('how large the surface field is (pillbox)', [
                'Take a thin pillbox straddling the surface, face area $A$, only the outside face is in a field: $EA=\\sigma A/\\varepsilon_0$.',
                '$\\Rightarrow\\ E_{\\mathrm{surface}}=\\sigma/\\varepsilon_0$',
            ]),
            res('learn these four', [
                '$E_{\\mathrm{inside}}=0$;  the whole conductor, cavity walls included, is one potential',
                'just outside: $E=\\sigma/\\varepsilon_0$, perpendicular to the metal',
                'a cavity holding $+q$ shows $-q$ on its wall and $+q$ on the outer surface',
                'an empty cavity is shielded from fields outside it',
            ]),
            trap('$E=0$ is not $V=0$. A charged shell has no field inside and still sits at $V=kQ/R$: zero slope, non-zero height.'),
            h('2', 'Cavities: where the charge goes', 'RESULT'),
            der('induced charge, from one Gaussian surface', [
                'Draw any closed surface inside the metal. Every point on it has $E=0$, so $\\oint\\vec E\\cdot d\\vec A=0$.',
                'The enclosed charge must then be zero: the wall carries $-q$, and since the conductor is neutral, $+q$ appears outside.',
                'The outer surface knows only the total charge, not where it is hidden - so a cavity is shielded.',
            ]),
            h('3', 'Gauss in three steps'),
            p('Name a surface where $|\\vec E|$ is constant and $\\vec E$ is parallel or perpendicular to $d\\vec A$, then use $\\oint\\vec E\\cdot d\\vec A=Q_{\\mathrm{enc}}/\\varepsilon_0$.'),
            why('The flux integral is only useful after symmetry has turned it into $E$ times an area. Otherwise Gauss is still true, just not calculable.'),
            tab(['source', 'field at distance r', 'note'], [
                ['point charge, outside a sphere', '$kQ/r^2$', 'the starting point'],
                ['inside a uniform solid sphere', '$\\rho r/3\\varepsilon_0$', 'zero at the centre'],
                ['long line, $\\lambda$ per length', '$\\lambda/2\\pi\\varepsilon_0 r$', 'falls as $1/r$'],
                ['large sheet, $\\sigma$ per face', '$\\sigma/2\\varepsilon_0$', 'away on both sides'],
                ['conductor surface', '$\\sigma/\\varepsilon_0$', 'one side only'],
                ['infinite slab, half-width $a$', '$\\rho x/\\varepsilon_0$', 'outside: $\\rho a/\\varepsilon_0$'],
            ], w=[.44, .3, .26]),
            ex('one line of numbers', [
                'Radius $10\\ \\mathrm{cm}$, charge $1\\ \\mu\\mathrm{C}$: $V_s=9.0\\times10^4\\ \\mathrm{V}$, $E_s=9.0\\times10^5\\ \\mathrm{V/m}$; both fall off outside as $1/r$ and $1/r^2$.',
            ]),
            trap('One charged plate gives $\\sigma/2\\varepsilon_0$, but a capacitor gap gives $\\sigma/\\varepsilon_0$ - two plates, two contributions.'),
            dias([{'key': 'cavity', 'cap': 'A neutral shell with $+q$ in the cavity: $-q$ on the wall, $+q$ outside, $E=0$ in the metal.'},
                  {'key': 'sphere_fields', 'cap': 'Field is flat and non-zero inside; the step in $V$ at $r=R$ marks where the charge sits.'}], 330),
            rem('Say where the charge sits, then what the potential is. Neither step needs a capacitor formula.'),
        ],
    },

    # ------------------------------------------------------------------ 2
    {
        'slug': 'JEE-02-plate-and-slab',
        'section': 'JEE', 'page': 2, 'part_page': 2,
        'title': 'Capacitance: the plate formula and the one slab rule',
        'sub': 'Capacitance is charge needed per volt. Derive it once for plates, then a single rule covers dielectric, metal and vacuum.',
        'source': 'Capacitors.md ch.2-3',
        'blocks': [
            h('1', 'Why C depends on geometry alone'),
            der('the ratio is fixed by shape and medium', [
                'Every field and potential is proportional to the charges that produce it. Double every $q$ and every $V$ doubles.',
                'So $Q/V$ cannot depend on $Q$. What is left is geometry and the medium: $C=\\varepsilon_0 A/d$ for plates, $4\\pi\\varepsilon_0R$ for an isolated sphere.',
            ]),
            trap('A capacitor holds $+Q$ and $-Q$, so its net charge is zero. "Charge on the capacitor" always means the positive plate.'),
            h('2', 'The plate formula, derived in three lines', 'RESULT'),
            der('the plate formula', [
                'Gap field of two opposite plates: $E=\\dfrac{Q/2}{\\varepsilon_0A}+\\dfrac{Q/2}{\\varepsilon_0A}=\\dfrac{Q}{\\varepsilon_0A}$ (the two plates add).',
                'Voltage between them: $V=Ed=\\dfrac{Qd}{\\varepsilon_0A}$.',
                'Divide: $C=\\dfrac{Q}{V}=\\dfrac{\\varepsilon_0A}{d}$, and with a dielectric filling the gap $C=\\dfrac{K\\varepsilon_0A}{d}$.',
            ]),
            res('the two you quote', [
                '$C=\\dfrac{\\varepsilon_0A}{d}$,  $\\ C=\\dfrac{K\\varepsilon_0A}{d}$;  $\\varepsilon_0=8.85\\times10^{-12}\\ \\mathrm{F/m}$, $4\\pi\\varepsilon_0=1.11\\times10^{-10}\\ \\mathrm{F/m}$',
            ]),
            ex('two plates, two answers', [
                'Area $100\\ \\mathrm{cm^2}$, gap $1\\ \\mathrm{mm}$: air $88.5\\ \\mathrm{pF}$; with $K=5$, $443\\ \\mathrm{pF}$. Doubling the gap halves $C$; an isolated $1\\ \\mathrm{cm}$ sphere is only $1.1\\ \\mathrm{pF}$.',
            ]),
            h('3', 'One slab rule for every gap', 'RESULT'),
            der('why the thickness becomes t/K', [
                'With a slab of thickness $t$ and constant free charge: $E_{\\mathrm{vac}}=\\dfrac{Q}{\\varepsilon_0A}$, $E_{\\mathrm{slab}}=\\dfrac{Q}{K\\varepsilon_0A}$.',
                'Add the two voltage drops: $V=E_{\\mathrm{vac}}(d-t)+E_{\\mathrm{slab}}\\,t=\\dfrac{Q}{\\varepsilon_0A}\\left(d-t+\\dfrac{t}{K}\\right)$.',
                'Divide by $Q$: $C=\\dfrac{\\varepsilon_0A}{d-t+t/K}$. Metal is the limit $K\\to\\infty$, giving $C=\\dfrac{\\varepsilon_0A}{d-t}$ - the thickness is simply removed.',
            ]),
            res('use it in all three cases', [
                'dielectric slab: $C=\\dfrac{\\varepsilon_0A}{d-t+t/K}$;  metal slab: $C=\\dfrac{\\varepsilon_0A}{d-t}$;  vacuum: $C=\\dfrac{\\varepsilon_0A}{d}$',
                'two layers: $\\dfrac{1}{C}=\\dfrac{t_1}{K_1\\varepsilon_0A}+\\dfrac{t_2}{K_2\\varepsilon_0A}$;  only total thickness of each layer matters',
            ]),
            trap('Use the overlap area, never the sum of both plate areas. And $C=\\varepsilon_0A/d$ needs $d$ small compared with the plate width; edge fringing always adds a little.'),
            h('4', 'Many plates, and plates with unequal charge'),
            der('n plates and two odd charges', [
                'Interleave $n$ plates, alternate ones wired to the two terminals: there are $n-1$ gaps, all at the same voltage, so $C=(n-1)\\varepsilon_0A/d$.',
                'Large plates carrying $Q_1,Q_2$: the facing surfaces hold $\\pm(Q_1-Q_2)/2$, since only that much can be shared across the gap.',
                'Then $V_1-V_2=\\dfrac{(Q_1-Q_2)d}{2\\varepsilon_0A}$. A net plate charge is not the same as the facing charge.',
            ]),
            dias([{'key': 'slab_cases', 'cap': 'Every gap is $C=\\varepsilon_0A/(d-t+t/K)$; metal is $K\\to\\infty$.'},
                  {'key': 'metal_slab', 'cap': 'A floating metal slab removes its own thickness from the voltage drop.'}], 320),
            rem('$C$ is geometry plus medium. Derive the plate formula once, then replace the filled thickness by $t/K$.'),
        ],
    },

    # ------------------------------------------------------------------ 3
    {
        'slug': 'JEE-03-geometries',
        'section': 'JEE', 'page': 3, 'part_page': 3,
        'title': 'Sphere, cylinder and connected conductors',
        'sub': 'One method: assign the charge, find E by Gauss, integrate to get V, divide. The geometry only changes the integral.',
        'source': 'Capacitors.md ch.3',
        'blocks': [
            h('4', 'Potential inside, and why the graph is flat'),
            der('potential of a charged shell', [
                'Outside, $V(r)=-\\int_\\infty^r kQ/r\'^2\\,dr\'=kQ/r$.',
                'Inside, the path in from the surface costs nothing because $E=0$, so $V=kQ/R$ all the way in. The graph steps at $r=R$ because that is where the charge sits, not because $V$ jumps.',
            ]),
            h('2', 'Concentric spheres', 'RESULT'),
            der('the spherical capacitor', [
                'Gauss between the spheres: $E=\\dfrac{Q}{4\\pi\\varepsilon_0r^2}$, independent of the outer shell.',
                'Integrate from $a$ to $b$: $V=\\dfrac{Q}{4\\pi\\varepsilon_0}\\left(\\dfrac{1}{a}-\\dfrac{1}{b}\\right)$.',
                'Divide: $C=4\\pi\\varepsilon_0\\dfrac{ab}{b-a}$.  Let $b\\to\\infty$: the isolated sphere $4\\pi\\varepsilon_0a$.',
                'Let $b-a\\ll a$: the area is $4\\pi a^2$ and the plate formula returns - always check a new geometry against that limit.',
            ]),
            h('3', 'Coaxial cylinders'),
            der('the cylindrical capacitor', [
                'Gauss on a cylinder of radius $r$ and length $L$: $E\\cdot2\\pi rL=\\dfrac{\\lambda L}{\\varepsilon_0}$, so $E=\\dfrac{\\lambda}{2\\pi\\varepsilon_0r}$.',
                'Integrate $1/r$: $V=\\dfrac{\\lambda}{2\\pi\\varepsilon_0}\\ln\\dfrac{b}{a}$, hence $C=\\dfrac{2\\pi\\varepsilon_0L}{\\ln(b/a)}$.',
                'Radial layers in series add their logs: $\\dfrac{1}{C/L}=\\sum_i\\dfrac{\\ln(r_{i+1}/r_i)}{2\\pi\\varepsilon_i}$.',
            ]),
            h('4', 'Two connected spheres: potential is shared, charge is not'),
            der('why the smaller sphere wins the field', [
                'A wire makes one conductor, so $V_a=V_b$: $\\dfrac{Q_a}{a}=\\dfrac{Q_b}{b}\\Rightarrow Q_a=Q\\dfrac{a}{a+b}$.',
                'Surface fields: $E=kQ_a/a^2$ and $E=kQ_b/b^2$, so $\\dfrac{E_a}{E_b}=\\dfrac{b}{a}$ - the smaller sphere has the larger field.',
                'That is why a pointed conductor sparks first.',
            ]),
            trap('These distant-sphere results need separation $\\gg$ radius. For nearby spheres the induced charge makes the surface distribution non-uniform and $V$ is no longer $kQ/r$.'),
            h('5', 'Two more geometries worth having', 'RESULT'),
            res('results worth quoting', [
                'two distant spheres, radii $a,b$, opposite charges: $C\\simeq4\\pi\\varepsilon_0\\dfrac{ab}{a+b}$ (this is the series combination $1/C=1/C_a+1/C_b$)',
                'sphere of radius $a$ coated to radius $b$ with dielectric $K$: $\\dfrac{1}{C}=\\dfrac{(1/a-1/b)/K+1/b}{4\\pi\\varepsilon_0}$ - add the dielectric drop to the vacuum drop',
            ]),
            ex('numbers that catch mistakes', [
                'Coax with $a=2\\ \\mathrm{mm}$, $b=10\\ \\mathrm{mm}$, $L=1\\ \\mathrm{m}$: $C=2\\pi\\varepsilon_0/\\ln5=77\\ \\mathrm{pF}$; the same cable in oil of $K=2.2$ gives $170\\ \\mathrm{pF}$.',
                'Two spheres $1\\ \\mathrm{cm}$ and $4\\ \\mathrm{cm}$ sharing $100\\ \\mu\\mathrm{C}$: the small one takes $20\\ \\mu\\mathrm{C}$ but has $16\\times$ the surface field of the large one.',
            ]),
            dias([{'key': 'shells', 'cap': 'Concentric spheres: $E\\propto1/r^2$, and only the part between $a$ and $b$ sets $V$.'},
                  {'key': 'coax', 'cap': 'Coaxial cylinders: $E\\propto1/r$, so the voltage brings a logarithm.'}], 260),
            rem('Assign $Q$, get $E$ from Gauss, integrate to $V$, divide. Check every new geometry against the plate limit.'),
        ],
    },

    # ------------------------------------------------------------------ 4
    {
        'slug': 'JEE-04-networks',
        'section': 'JEE', 'page': 4, 'part_page': 4,
        'title': 'Networks: islands, bridges, ladders',
        'sub': 'Wires make islands. Charge is conserved on each island, not on each capacitor - derive every combination from that.',
        'source': 'Capacitors.md ch.6-7',
        'blocks': [
            h('1', 'Series and parallel, derived'),
            der('series: one over C adds', [
                'Two capacitors in a line make the middle island. If it started neutral it stays neutral, so both carry the same $Q$.',
                'The voltages add: $V=\\dfrac{Q}{C_1}+\\dfrac{Q}{C_2}$, so $\\dfrac{1}{C_{\\mathrm{eq}}}=\\dfrac{1}{C_1}+\\dfrac{1}{C_2}$.',
                'The smallest capacitor then takes the largest share of the voltage.',
            ]),
            der('parallel: C adds', [
                'Both are across the same two nodes, so $V$ is common and the charges add: $Q=C_1V+C_2V$.',
                '$\\Rightarrow C_{\\mathrm{eq}}=C_1+C_2$. Energy follows: series $\\dfrac{U_i}{U}=\\dfrac{C_{\\mathrm{eq}}}{C_i}$, parallel $\\dfrac{U_i}{U}=\\dfrac{C_i}{C_{\\mathrm{eq}}}$.',
            ]),
            trap('Series or parallel is decided by the wires, not by the drawing - redraw first. A precharged middle island also breaks the equal-charge rule.'),
            h('2', 'The island method that never fails', 'METHOD'),
            der('one conservation law per conductor', [
                'Each floating island has a fixed net charge $Q_i^{\\mathrm{init}}$. Every plate on it holds $C(V_i-V_j)$ against a neighbour.',
                'Add them with signs: $\\sum_j C_{ij}(V_i-V_j)=Q_i^{\\mathrm{init}}$. One equation per floating island.',
                'Solve for the potentials, then read each capacitor as $q=C\\,\\Delta V$.',
            ]),
            p('Island types: grounded $\\Rightarrow V=0$; battery-connected $\\Rightarrow$ difference fixed; floating $\\Rightarrow$ net charge fixed.'),
            h('3', 'Bridge, cube, ladder, star-delta', 'RESULT'),
            der('balanced bridge', [
                'Each arm divides the same applied voltage: $V_X=V\\dfrac{C_1}{C_1+C_2}$ and $V_Y=V\\dfrac{C_3}{C_3+C_4}$.',
                'It carries nothing when $V_X=V_Y$, i.e. $\\dfrac{C_1}{C_2}=\\dfrac{C_3}{C_4}$; otherwise write two island equations.',
            ]),
            der('infinite ladder', [
                'One more repeat unit must change nothing: the remainder $X$ is in series with $C$, then in parallel with $C$.',
                '$X=C+\\dfrac{CX}{C+X}\\Rightarrow X=\\dfrac{\\sqrt5-1}{2}C$ (the negative root is rejected: $C>0$).',
            ]),
            res('results worth memorising', [
                'cube of twelve equal $C$: opposite vertices $\\dfrac{6C}{5}$, edge $\\dfrac{12C}{7}$, face diagonal $\\dfrac{4C}{3}$',
                'star-delta with $S=ab+bc+ca$: arms $x=S/b$, $y=S/c$, $z=S/a$;  back again $C_{12}=xy/(x+y+z)$',
            ]),
            trap('Do not copy the resistor star-delta across: for capacitors the star arm is a sum of products divided by one branch.'),
            ex('reduce, then audit the pieces', [
                '$6\\ \\mu\\mathrm{F}$ and $3\\ \\mu\\mathrm{F}$ in series give $2\\ \\mu\\mathrm{F}$; with $4\\ \\mu\\mathrm{F}$ in parallel, $C_{\\mathrm{eq}}=6\\ \\mu\\mathrm{F}$. At $12\\ \\mathrm{V}$: $Q=72\\ \\mu\\mathrm{C}$, $U=432\\ \\mu\\mathrm{J}$.',
                'Audit: the series pair holds $24\\ \\mu\\mathrm{C}$ at $4\\ \\mathrm{V}$ and $8\\ \\mathrm{V}$, the $4\\ \\mu\\mathrm{F}$ holds $48\\ \\mu\\mathrm{C}$; and $24+48=72$.',
            ]),
            h('4', 'Charge through a wire'),
            p('Cut the circuit with a surface crossed by that wire only. The charge that crossed equals the change in enclosed plate charge, signs included - it is not $C\\Delta V$ in general.'),
            dias([{'key': 'sp_compact', 'cap': 'The middle island is what forces series charges to be equal.'},
                  {'key': 'bridge', 'cap': 'Balanced means $V_X=V_Y$: delete the bridge, or write one island equation at each node.'}], 250),
            rem('Name the terminals, mark the islands, write one charge equation per island. Folding is a shortcut that must be justified.'),
        ],
    },

    # ------------------------------------------------------------------ 5
    {
        'slug': 'JEE-05-energy-battery',
        'section': 'JEE', 'page': 5, 'part_page': 5,
        'title': 'Energy, the battery, and the heat bill',
        'sub': 'Every energy result is an integral or a ledger. The half comes from the triangle, and the battery is part of the accounting.',
        'source': 'Capacitors.md ch.4, ch.10',
        'blocks': [
            h('1', 'Stored energy, integrated', 'RESULT'),
            der('where the half comes from', [
                'Push a small charge $dq$ in while the voltage is $V=q/C$: the work is $dU=V\\,dq=\\dfrac{q}{C}dq$.',
                'Integrate from $0$ to $Q$: $U=\\dfrac{Q^2}{2C}=\\dfrac12QV=\\dfrac12CV^2$.',
                'On a $V$-$q$ graph this is the area of a triangle, not a rectangle - that is the missing half.',
            ]),
            der('field energy density', [
                'For a parallel plate: $U=\\dfrac12CV^2=\\dfrac12\\cdot\\dfrac{\\varepsilon_0A}{d}\\cdot(Ed)^2=\\dfrac12\\varepsilon_0E^2\\,(Ad)$.',
                'Divide by the volume $Ad$: $u=\\dfrac12\\varepsilon_0E^2$ per unit volume, wherever the field is.',
            ]),
            ex('the check that catches sign errors', [
                '$2\\ \\mu\\mathrm{F}$ at $100\\ \\mathrm{V}$: $Q=200\\ \\mu\\mathrm{C}$, $U=0.1\\ \\mathrm{J}$. Pull the plates to twice the gap with the battery off: $C$ halves, $Q$ stays, so $V$ and $U$ double - you supplied that work.',
            ]),
            h('2', 'The one fork: fixed Q or fixed V', 'TABLE'),
            der('why the two columns differ', [
                'At fixed $Q$: $C\\to KC$ and $Q$ cannot change, so $V=Q/C$ falls by $K$ and $U=Q^2/2C$ falls by $K$. Energy leaves into the mechanical work.',
                'At fixed $V$: $V$ is pinned, so $Q=CV$ grows by $K$ and $U=\\frac12CV^2$ grows by $K$. The cell supplies both the extra energy and the mechanical work.',
            ]),
            tab(['after full dielectric insertion', 'fixed $Q$ (battery off)', 'fixed $V$ (battery on)'], [
                ['$C$', 'grows by $K$', 'grows by $K$'],
                ['$V$', 'falls by $K$', 'unchanged'],
                ['$E$ in the gap', 'falls by $K$', 'unchanged, $V/d$'],
                ['$Q$', 'unchanged', 'grows by $K$'],
                ['$U$', 'falls by $K$', 'grows by $K$'],
                ['battery work', 'zero', '$V^2\\Delta C$'],
            ], w=[.4, .3, .3]),
            ex('the fork in numbers', [
                '$1\\ \\mu\\mathrm{F}$ at $100\\ \\mathrm{V}$, then $K=2$ fills the gap. Battery on: $C$ becomes $2\\ \\mu\\mathrm{F}$, the cell supplies $V^2\\Delta C=10\\ \\mathrm{mJ}$, $U$ rises by $5\\ \\mathrm{mJ}$, and the other $5\\ \\mathrm{mJ}$ goes into pulling the slab in.',
                'Battery off: $Q=100\\ \\mu\\mathrm{C}$ is fixed, so $V$ drops to $50\\ \\mathrm{V}$ and $U$ falls from $5\\ \\mathrm{mJ}$ to $2.5\\ \\mathrm{mJ}$ - that released energy is the work the field does on the slab.',
            ]),
            trap('Battery work is not field energy. The cell supplies $V^2\\Delta C$ while $U$ rises by only $\\frac12V^2\\Delta C$; differentiating $U$ alone gives the wrong sign for the force.'),
            h('3', 'The heat bill when two capacitors are joined'),
            der('charge conservation first, energy second', [
                'Islands conserve charge: $C_1V_1+C_2V_2=(C_1+C_2)V_f$, so $V_f=\\dfrac{C_1V_1+C_2V_2}{C_1+C_2}$.',
                'Energy before minus after: $H=\\dfrac{C_1C_2}{2(C_1+C_2)}(V_1-V_2)^2$ - never negative, and independent of the resistance.',
            ]),
            ex('numbers on the heat bill', [
                '$C_1=2\\ \\mu\\mathrm{F}$ at $100\\ \\mathrm{V}$, $C_2=3\\ \\mu\\mathrm{F}$ uncharged: $V_f=40\\ \\mathrm{V}$ and $H=\\frac12\\cdot\\frac65\\ \\mu\\mathrm{F}\\cdot100^2=6\\ \\mathrm{mJ}$.',
                'Check: $10\\ \\mathrm{mJ}$ before, $4\\ \\mathrm{mJ}$ after - the missing $6\\ \\mathrm{mJ}$ is heat. Charging an empty $C$ from a cell loses exactly half of $CE^2$.',
            ]),
            dias([{'key': 'energy_triangle', 'cap': 'Work is the area under the $V$-$q$ line: a triangle, hence $\\frac12$.'},
                  {'key': 'fixed_fork', 'cap': 'Ask what is held fixed before differentiating. It is the whole chapter in one picture.'}], 290),
            rem('Fixed $Q$: differentiate $U$. Fixed $V$: differentiate $U-QV$. Heat: conserve charge, then subtract energies.'),
        ],
    },

    # ------------------------------------------------------------------ 6
    {
        'slug': 'JEE-06-force-on-plates',
        'section': 'JEE', 'page': 6, 'part_page': 6,
        'title': 'Force on plates and dielectrics, from energy',
        'sub': 'Write C(x), state the constraint, differentiate. The factor one-half is the thing examiners test.',
        'source': 'Capacitors.md ch.5, plus the image method',
        'blocks': [
            h('3', 'Force from energy, and the pressure of a charged sphere'),
            der('force from the derivative', [
                'At fixed $Q$: $F=-\\dfrac{d}{dx}\\left(\\dfrac{Q^2}{2C}\\right)=\\dfrac{Q^2}{2C^2}\\dfrac{dC}{dx}$.',
                'At fixed $V$ the battery must be included, $\\Pi=U-QV=-\\frac12CV^2$, so $F=-\\dfrac{d\\Pi}{dx}=\\dfrac12V^2\\dfrac{dC}{dx}$.',
                'Same state $Q=CV$ gives the same force either way - the constraint only decides what happens next.',
            ]),
            der('outward pressure on a charged sphere', [
                'Expand the radius by $dR$ at fixed $Q$: $U=\\dfrac{Q^2}{8\\pi\\varepsilon_0R}$ falls, and $dU=-p\\,4\\pi R^2dR$.',
                '$\\Rightarrow p=\\dfrac{Q^2}{32\\pi^2\\varepsilon_0R^4}$, pushing outward; the net force on the sphere is still zero by symmetry.',
            ]),
            ex('force between real plates', [
                '$100\\ \\mathrm{cm^2}$ at $1\\ \\mathrm{mm}$, $100\\ \\mathrm{V}$: $p=\\frac12\\varepsilon_0E^2=0.044\\ \\mathrm{Pa}$, $F=4.4\\times10^{-4}\\ \\mathrm{N}$.',
                'Halve the gap at fixed $Q$: $E$ is unchanged, so $F$ is unchanged. At fixed $V$: $E$ doubles, $F$ quadruples.',
            ]),
            h('4', 'The force between the plates', 'RESULT'),
            der('why it is half the gap field', [
                'A plate does not pull on itself. The field at one plate due to the other is $\\dfrac{Q}{2\\varepsilon_0A}$ - half the gap field.',
                'So $F=Q\\cdot\\dfrac{Q}{2\\varepsilon_0A}=\\dfrac{Q^2}{2\\varepsilon_0A}$;  as a pressure, $p=\\dfrac{\\sigma^2}{2\\varepsilon_0}$.',
                'The same answer from energy: $F=-\\dfrac{dU}{dx}$ with $U=\\dfrac{Q^2x}{2\\varepsilon_0A}$ gives $F=-\\dfrac{Q^2}{2\\varepsilon_0A}$, inward.',
            ]),
            trap('Do not write $F=QE$ with the full gap field $\\sigma/\\varepsilon_0$; the correct force is $QE/2$. That half is the whole question.'),
            h('5', 'A dielectric is always pulled inward', 'RESULT'),
            der('slab entering by x', [
                'Filled and empty parts are in parallel: $C(x)=\\dfrac{\\varepsilon_0w}{d}\\left[L+(K-1)x\\right]$, so $\\dfrac{dC}{dx}=\\dfrac{\\varepsilon_0(K-1)w}{d}$.',
                'At fixed $V$: $F=\\dfrac12V^2\\dfrac{dC}{dx}=\\dfrac{\\varepsilon_0(K-1)w}{2d}V^2$, constant, pulling the slab in.',
                'At fixed $Q$: use $V=Q/C(x)$, so $F=\\dfrac{Q^2}{2C^2}\\dfrac{dC}{dx}$ - same direction, smaller as the slab goes deeper.',
            ]),
            der('liquid climbing between plates', [
                'Electric force per unit plate width $=\\dfrac{\\varepsilon_0(K-1)V^2}{2d}$; weight of the raised column per width $=\\rho gdh$.',
                'Balance: $h=\\dfrac{\\varepsilon_0(K-1)V^2}{2\\rho gd^2}$ - linear in $K-1$, quadratic in $V$, falling fast as the gap opens.',
            ]),
            res('the three force results', [
                'plate: $F=\\dfrac{Q^2}{2\\varepsilon_0A}=\\dfrac{\\varepsilon_0AV^2}{2d^2}$;  slab: $\\dfrac{\\varepsilon_0(K-1)w}{2d}V^2$;  liquid: $h=\\dfrac{\\varepsilon_0(K-1)V^2}{2\\rho gd^2}$',
                'all three point toward larger $C$ - the one thing that never changes',
            ]),
            dias([{'key': 'insertion', 'cap': 'Filled and empty parts are parallel capacitors, so $dC/dx>0$: the slab is dragged in.'},
                  {'key': 'liquid', 'cap': 'The same force lifts a liquid: electric work pays for the rise in gravitational energy.'}], 300),
            rem('Write $C(x)$, name the constraint, differentiate the right energy. Force always points toward larger $C$.'),
        ],
    },

    # ------------------------------------------------------------------ 7
    {
        'slug': 'JEE-07-images-and-stability',
        'section': 'JEE', 'page': 7, 'part_page': 7,
        'title': 'Image charge, and a plate that snaps down',
        'sub': 'Two questions that look hard and are one construction each: a mirror charge, and an equilibrium that stops existing.',
        'source': 'Capacitors.md ch.5, image method',
        'blocks': [
            h('3', 'Image charge: the one extension worth keeping', 'KEPT'),
            why('A grounded plane is an equipotential, and two opposite charges of equal size make a whole plane equipotential - so the plane can be replaced by the second charge.'),
            der('force, energy and induced charge', [
                'Replace the plane by $-q$ at depth $h$. The real charge is then $2h$ from its image: $F=\\dfrac{q^2}{4\\pi\\varepsilon_0(2h)^2}=\\dfrac{q^2}{16\\pi\\varepsilon_0h^2}$.',
                'Bringing the charge in from infinity: $W=\\dfrac12q\\,(V_{\\mathrm{image}})=\\dfrac{q^2}{16\\pi\\varepsilon_0h}$ - the half is because the induced charge builds up as you approach.',
                'The plane carries induced charge $-q$, spread with $\\sigma(\\rho)=-\\dfrac{qh}{2\\pi(\\rho^2+h^2)^{3/2}}$, largest directly below the charge.',
            ]),
            trap('Using $q^2/8\\pi\\varepsilon_0h$ double counts the work of building the induced charge. The energy is half of $q\\times$ the image potential, not of $q\\times$ the full pair energy.'),
            why('Why a mirror charge is allowed at all: in the region above the plane, solving Laplace with the plane at $V=0$ gives a unique field. The pair of charges already satisfies that boundary condition, so it must be the right field. Above the plane nobody can tell the difference; below it there is no field to speak of, and the metal is not the image.'),
            res('image results for a grounded plane', [
                'force $\\dfrac{q^2}{16\\pi\\varepsilon_0h^2}$,  work to bring from infinity $\\dfrac{q^2}{16\\pi\\varepsilon_0h}$,  induced charge $-q$',
                'surface density $\\sigma(\\rho)=-\\dfrac{qh}{2\\pi(\\rho^2+h^2)^{3/2}}$: sharpest directly under the charge, and it integrates to $-q$',
                'grounded sphere of radius $a$ (optional, one line): image $q\'=-qa/d$ at $a^2/d$; an isolated neutral sphere needs a second image $+qa/d$ at the centre',
            ]),
            h('2', 'Where the method stops'),
            h('4', 'Stretch: a plate held on a spring'),
            der('equilibrium, and where it breaks down', [
                'The gap is $d-x$ and the spring pulls back with $kx$, so $kx=\\dfrac{\\varepsilon_0AV^2}{2(d-x)^2}$. Write $y=\\dfrac{\\varepsilon_0AV^2}{2kd^2}$ and solve $x(1-x/d)^2=yd$.',
                'The two roots merge when the derivative vanishes too: $x=d/3$, at $V^2=\\dfrac{8kd^3}{27\\varepsilon_0A}$. Beyond it no equilibrium exists and the plate snaps down.',
                'At fixed charge the force $Q^2/2\\varepsilon_0A$ does not depend on $x$, so there is no fold and no snap-down.',
            ]),
            h('3', 'Stretch: a plate held on a spring'),
            der('equilibrium, and where it breaks down', [
                'The gap is $d-x$ and the spring pulls back with $kx$, so $kx=\\dfrac{\\varepsilon_0AV^2}{2(d-x)^2}$. Write $y=\\dfrac{\\varepsilon_0AV^2}{2kd^2}$ and solve $x(1-x/d)^2=yd$.',
                'The two roots merge when the derivative vanishes too: $x=d/3$, at $V^2=\\dfrac{8kd^3}{27\\varepsilon_0A}$. Beyond it no equilibrium exists and the plate snaps down.',
                'At fixed charge the force $Q^2/2\\varepsilon_0A$ does not depend on $x$, so there is no fold and no snap-down.',
            ]),
            ex('numbers for the image result', [
                '$q=1\\ \\mu\\mathrm{C}$ at $h=1\\ \\mathrm{cm}$ above a grounded plane: $F=0.225\\ \\mathrm{N}$ and the work to bring it from infinity is $0.45\\ \\mathrm{mJ}$.',
                'At $2\\ \\mathrm{cm}$ the force is four times smaller and the energy half: both scale as $1/h^2$ and $1/h$, so the energy is always the force times $h/2$.',
            ]),
            dias([{'key': 'image_plane', 'cap': 'The image makes the plane equipotential; real-image separation is $2h$, not $h$.'},
                  {'key': 'pull_in', 'cap': 'Two equilibria appear, then merge and disappear: that is the snap-down.'}], 300),
            rem('Mirror the charge to make the boundary equipotential, then treat it as a real Coulomb problem - but count energy once, not twice.'),
        ],
    },

    # ------------------------------------------------------------------ 8
    {
        'slug': 'JEE-08-dielectrics',
        'section': 'JEE', 'page': 8, 'part_page': 8,
        'title': 'Dielectrics: why the field falls, and layers vs patches',
        'sub': 'Polarisation puts bound charge on the faces. Whether the field falls is decided by the constraint, not by the material alone.',
        'source': 'Capacitors.md ch.8, ch.11',
        'blocks': [
            h('1', 'What the material actually does'),
            der('why E falls by K at fixed free charge', [
                'The applied field lines up molecular dipoles; their bound charge appears on the faces, opposing the free charge.',
                'The net field inside is the free field minus the bound contribution: $E=\\dfrac{\\sigma_{\\mathrm{free}}-\\sigma_b}{\\varepsilon_0}=\\dfrac{\\sigma_{\\mathrm{free}}}{K\\varepsilon_0}$, using $\\sigma_b=\\sigma_{\\mathrm{free}}\\left(1-\\dfrac1K\\right)$.',
                'That is the whole of "the dielectric reduces the field": it happens because the bound charge is there, not because the material absorbs field.',
            ]),
            der('why nothing falls with the battery on', [
                'The cell holds the plates at fixed $V$, so $E=V/d$ cannot change. Instead it pushes in more free charge until $Q=KQ_0$.',
                'Capacitance rises by $K$ either way - it is the charge, not the field, that does the extra work.',
            ]),
            res('one-line summary', [
                'fixed $Q$: $E=\\dfrac{E_0}{K}$, $V=\\dfrac{V_0}{K}$, $C=KC_0$, $U=\\dfrac{U_0}{K}$  |  fixed $V$: $E=E_0$, $C=KC_0$, $Q=KQ_0$, $U=KU_0$',
            ]),
            trap('"A dielectric always reduces the field" is false. Fill the gap with the battery still connected and $E$ is untouched - the charge grows instead.'),
            h('2', 'Layers or patches: two derivations', 'RESULT'),
            der('layers along the field (series)', [
                'No free charge at the interface, so the same $D=Q/A$ crosses both layers: $E_i=\\dfrac{Q}{K_i\\varepsilon_0A}$.',
                'Voltages add: $V=\\sum\\dfrac{Q\\,t_i}{K_i\\varepsilon_0A}\\Rightarrow\\dfrac{1}{C}=\\sum\\dfrac{t_i}{K_i\\varepsilon_0A}$, and for one slab $C=\\dfrac{\\varepsilon_0A}{d-t+t/K}$.',
                'Half the thickness filled: $C=\\dfrac{2KC_0}{K+1}$; as $K\\to\\infty$ the metal-slab answer returns.',
            ]),
            der('patches across the area (parallel)', [
                'Every patch sees the same $V$ and the same $E=V/d$, but each carries its own charge: $Q_i=\\dfrac{K_i\\varepsilon_0A_i}{d}\\,\\Delta V$.',
                'Sums add: $C=\\sum\\dfrac{K_i\\varepsilon_0A_i}{d}$; half the area filled gives $C=C_0\\dfrac{K+1}{2}$.',
            ]),
            trap('Which case is which? Cut the plates into pieces and you have patches. Cut across the gap and you have layers. Layers add voltages, patches add charges.'),
            h('3', 'Dielectric strength sets the design', 'RATING'),
            der('ratings and why series is dangerous', [
                'Breakdown needs $E_b$, so the safe voltage is $V_{\\max}=E_bd$; the best stored density is $\\dfrac12\\varepsilon_0KE_b^2$. Air: $3\\times10^6\\ \\mathrm{V/m}$, so $0.1\\ \\mathrm{mm}$ holds about $300\\ \\mathrm{V}$.',
                'In series, equal charge means $V_i\\propto1/C_i$: the smallest capacitor takes the largest voltage and fails first, so a chain is limited by its weakest member.',
            ]),
            ex('numbers worth checking twice', [
                'A $2\\ \\mu\\mathrm{F}$ air capacitor, half the gap filled with $K=4$: layers give $\\dfrac{2\\cdot4}{5}C_0=1.6C_0$, patches give $\\dfrac{4+1}{2}C_0=2.5C_0$. Different answers, same picture - the geometry decides.',
            ]),
            h('4', 'Six checks before you hand in'),
            p('Dimensions: an isolated body has $C\\sim\\varepsilon_0\\times$ length. Limits: $K\\to1$ returns vacuum, $b\\to\\infty$ returns the isolated sphere. Signs: heat cannot be negative, and a dielectric is always pulled toward larger $C$. Endpoints: a transient starts and ends at values the circuit allows. Stability: check curvature when equilibrium is asked. Ratings: compare each local field with $E_b$.'),
            dias([{'key': 'dielectric_layers', 'cap': 'Layers share the normal $D$ and add voltages; patches share the voltage and add charges.'},
                  {'key': 'polarisation', 'cap': 'Bound charge on the faces opposes the free charge: that is the whole mechanism.'}], 300),
            rem('Fixed $Q$ the field falls by $K$; fixed $V$ it does not. Layers add voltages, patches add charges.'),
        ],
    },

    # ------------------------------------------------------------------ 9
    {
        'slug': 'JEE-09-rc-and-ac',
        'section': 'JEE', 'page': 9, 'part_page': 9,
        'title': 'RC transients solved, and the capacitor in AC',
        'sub': 'One differential equation gives every transient. Two switch rules answer the rest, and one derivative gives the AC response.',
        'source': 'Capacitors.md ch.9-10, JEE parts of ch.12',
        'blocks': [
            h('1', 'Solve the circuit once', 'METHOD'),
            der('why every answer is an exponential', [
                'A cell $E$, resistor $R$, capacitor $C$ in series: $E=Ri+V_C$ with $i=C\\dfrac{dV_C}{dt}$, so $RC\\dfrac{dV_C}{dt}=E-V_C$.',
                'Separate and integrate: $V_C(t)=E+(V_0-E)e^{-t/RC}$. The approach to the final value is exponential because the drive is proportional to the remaining gap.',
                'Any linear network reduces to this with $V_\\infty$ and $R_{\\mathrm{th}}$: $V(t)=V_\\infty+(V_0-V_\\infty)e^{-t/\\tau}$, $\\tau=R_{\\mathrm{th}}C$.',
            ]),
            res('the three numbers', [
                '$V_0$: capacitor voltage just before switching - it cannot jump',
                '$V_\\infty$: remove the capacitor (open circuit) and solve the resistors',
                '$R_{\\mathrm{th}}$: resistance seen from the capacitor terminals, sources killed, dependent sources kept',
            ]),
            p('Clock: one time constant 63 %, two 86 %, three 95 %, five 99.3 %. Inverting: $t=\\tau\\ln\\dfrac{V_\\infty-V_0}{V_\\infty-V(t)}$.'),
            h('2', 'The two switch rules, and why they hold'),
            der('the two switch instants', [
                'Capacitor voltage is the integral of a finite current, so it cannot jump: $V_C(0^+)=V_C(0^-)$. Current can jump, because it is set by the resistors.',
                'So at $t=0^+$: uncharged means a wire, charged means a fixed voltage source. At $t=\\infty$ every current has died and the capacitor is an open circuit.',
                'Consequence: a step into a capacitive divider divides by $C$; the final state divides by $R$. That pair of answers is most of what is asked.',
            ]),
            der('discharge, and why energy dies twice as fast', [
                'With $E=0$: $V=V_0e^{-t/RC}$ and $i=\\dfrac{V_0}{R}e^{-t/RC}$.',
                'Energy $U=\\frac12CV^2=\\dfrac12CV_0^2e^{-2t/RC}$: the exponent doubles because $U$ goes as $V^2$.',
                'Settling heat between two voltages: $H=\\dfrac12C(V_0-V_\\infty)^2$, whatever $R$ is - smaller $R$ just means a bigger current for a shorter time.',
            ]),
            trap('At DC steady state the capacitor is open, but its voltage need not be zero. Replacing it by a wire is the $t=0^+$ picture, not the final one.'),
            h('3', 'Reservoir capacitor and the AC response', 'RESULT'),
            der('ripple, then reactance', [
                'Between recharges the capacitor supplies the load: $Q=I\\Delta t$, so $\\Delta V\\approx\\dfrac{I_{\\mathrm{load}}\\Delta t}{C}$. A $1\\ \\mathrm{A}$ load fed every $10\\ \\mathrm{ms}$ with $0.5\\ \\mathrm{V}$ ripple needs $20\\ \\mathrm{mF}$.',
                'For $V=V_0\\sin\\omega t$, $i=C\\dfrac{dV}{dt}=\\omega CV_0\\cos\\omega t$: the current leads by $90^\\circ$ and its size is $V_0/X_C$ with $X_C=\\dfrac{1}{\\omega C}$.',
                'Series $RC$: $Z=\\sqrt{R^2+X_C^2}$, $\\phi=-\\arctan(X_C/R)$; at $X_C=R$ the current leads by $45^\\circ$.',
            ]),
            ex('worked to the last digit', [
                '$2\\ \\mu\\mathrm{F}$ at $10\\ \\mathrm{V}$ discharged through $1\\ \\mathrm{M}\\Omega$: $\\tau=2\\ \\mathrm{s}$, so at $t=2\\ \\mathrm{s}$ the voltage is $10e^{-1}=3.68\\ \\mathrm{V}$.',
                'Energy falls from $100\\ \\mu\\mathrm{J}$ to $13.5\\ \\mu\\mathrm{J}$; the missing $86.5\\ \\mu\\mathrm{J}$ is heat in the resistor.',
            ]),
            h('4', 'The meter changes the reading', 'KEPT'),
            der('why a probe loads the circuit', [
                'The meter has its own input capacitance $C_m$. Connecting it joins two capacitors, so charge is shared.',
                'A capacitor $C_s$ at $V_0$ then reads $V=V_0\\dfrac{C_s}{C_s+C_m}$: with $C_m=C_s$ you lose half the reading. That is why a small capacitor needs a high-impedance probe.',
            ]),
            dias([{'key': 'thevenin', 'cap': 'Everything except the capacitor is one source plus $R_{\\mathrm{th}}$: that is why one exponential is enough.'},
                  {'key': 'charging', 'cap': 'Voltage rises as $1-e^{-t/\\tau}$ while current falls: their areas settle the energy books.'}], 290),
            rem('Solve $RC\\dot V+V=V_\\infty$ once. Then $V_0$, $V_\\infty$, $R_{\\mathrm{th}}C$ answer every transient.'),
        ],
    },
]


def build():
    # headings are numbered by position, so moving a section never leaves a gap
    for sheet in SHEETS:
        n = 0
        for b in sheet['blocks']:
            if b['k'] == 'h':
                n += 1
                b['n'] = str(n)
    data = {
        'edition': 'capacitors-jee-dense-v3',
        'canvas': [2480, 3508],
        'dpi': 300,
        'policy': 'JEE Main + Advanced only; Olympiad sheets retired 2026-10-24 (see AUDIT.md)',
        'sheets': SHEETS,
    }
    (ROOT / 'sheets.json').write_text(json.dumps(data, indent=1) + '\n')
    import re
    prose = sum(len(re.sub(r'\$[^$]*\$', 'X', t).split())
                for s in SHEETS for b in s['blocks']
                for t in ([b['s']] if 's' in b else []) + b.get('lines', [])
                + [c for r in b.get('rows', []) for c in r]
                + [i.get('cap', '') for i in b.get('items', [])])
    ders = sum(1 for s in SHEETS for b in s['blocks'] if b['k'] == 'der')
    figs = sum(len(b['items']) if b['k'] == 'dias' else (1 if b['k'] == 'dia' else 0)
               for s in SHEETS for b in s['blocks'])
    print(f'wrote sheets.json: {len(SHEETS)} pages, {prose} words, {ders} derivations, {figs} figures')


if __name__ == '__main__':
    build()
