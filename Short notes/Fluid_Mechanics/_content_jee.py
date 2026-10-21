"""Part I content: JEE Main + Advanced core of fluid mechanics.

Every page is a Sheet: a question as the title, numbered moves down the main
column, evidence and warnings in the right-hand rail, one wide figure.
"""
from layout import Sheet

K = 'FLUID MECHANICS  /  PART I: JEE MAIN + ADVANCED'


def build(total):
    S = []

    # ---------------------------------------------------------------- 1
    s = Sheet('JEE-01-pressure', 'Why does depth, not shape, set the pressure?',
              'Pressure is called a scalar, yet it pushes on every surface. Where does the direction come from?',
              K, 1, total, 'source: Fluid-mechanics.md  §3.1-3.2, E1-E2', 
              'pressure is one number per point; direction belongs to the area you choose')
    s.move('A point has no orientation', [
        ('p', 'Cut a small wedge of fluid with a slanted face dA at angle θ. The three faces have areas dA, dA sinθ and dA cosθ. Resolving along the slant and across it gives the same pressure on all three.'),
        ('m', r'p_x=p_y=p_\theta', '(3.1)'),
        ('n', 'shrink the wedge: the weight falls as dV, the forces only as dA, so the weight drops out'),
    ])
    s.move('The vertical gradient is a slab weight', [
        ('p', 'For a slab of area A and thickness dy, the net pressure force must carry its weight. With y measured upward:'),
        ('m', r'\frac{dp}{dy}=-\rho g'),
        ('p', 'Density may vary with height; for a liquid it does not, and the equation integrates at once.'),
    ])
    s.move('Integrate once and you own hydrostatics', [
        ('p', 'Take h downward from the free surface, where the pressure is p₀. Constant density gives the everyday formula, and a layered fluid is integrated layer by layer.'),
        ('m', r'p=p_0+\rho g h', '(3.2)'),
        ('n', 'a two-layer tank has a kink in p(h) at the interface, never a jump'),
    ])
    s.move('Absolute, gauge, and the barometer', [
        ('p', 'Gauge pressure is p − p₀, the part a manometer can see. A barometer is the same equation solved for the height that balances the atmosphere: 0.76 m of mercury, or 10.3 m of water.'),
        ('m', r'p_0=\rho_{Hg}\,g(0.76)=1.013\times10^5\ \mathrm{Pa}'),
    ])
    s.move('Shape cannot matter, but weight must go somewhere', [
        ('p', 'Every vessel with the same depth has the same pressure at the base, hence the same force pA on the base, flared or narrow. The walls supply the difference, which is why a flared vessel can weigh much more than the force on its base.'),
        ('n', 'hydrostatic paradox: pressure is local, weight is global'),
    ])
    s.chip('key', 'the three you use', [('m', r'p=p_0+\rho g h'), ('m', r'dp/dy=-\rho g'), ('p', 'F = pA on any face, along its normal')])
    s.chip('trap', 'two silent errors', [('p', 'Mixing gauge and absolute inside a Δp balance.'), ('p', 'Reading "more water" as "more pressure on the base".')])
    s.chip('num', 'carry these', [('p', 'p₀ = 1.013×10⁵ Pa'), ('p', '0.76 m Hg = 10.3 m water'), ('p', 'ρHg/ρw = 13.6')])
    s.figure('pressure_wedge')
    S.append(s)

    # ---------------------------------------------------------------- 2
    s = Sheet('JEE-02-manometer', 'How do you walk a U-tube without writing force balances?',
              'Multi-fluid columns look like bookkeeping. There is one rule, and it survives acceleration.',
              K, 2, total, 'source: §3.2-3.3, E2-E3, Q1-Q4',
              'walk from an open end: down adds, up subtracts, horizontal is free')
    s.move('The step rule', [
        ('p', 'Start at a point of known pressure, usually an open end at p₀. Move through the connected fluid: each descent Δh adds ρgΔh, each rise subtracts it, and a horizontal run costs nothing.'),
        ('m', r'p_{end}=p_0+\sum_{down}\rho g\,\Delta h-\sum_{up}\rho g\,\Delta h'),
    ])
    s.move('A trapped gas, walked', [
        ('p', 'Left limb open, 10 cm of water above the mercury; the right mercury stands 18 cm higher over trapped gas. Down the water, up the mercury:'),
        ('m', r'p_{gas}=p_0+\rho_w g(0.10)-\rho_{Hg}g(0.18)=7.83\times10^4\ \mathrm{Pa}'),
        ('n', 'below atmospheric, which is why the right column stands higher'),
    ])
    s.move('The barometer is the same walk', [
        ('p', 'Close one end, fill with mercury, invert into a dish. The column stops when ρHg g h balances p₀. Water needs 10.3 m, so a water barometer is a building, not an instrument.'),
        ('m', r'h=\frac{p_0}{\rho g}'),
    ])
    s.move('Pascal, and what a lift costs', [
        ('p', 'At the same height in a connected fluid at rest the pressure is equal. A small piston therefore holds a big load with a small force, but the strokes are in the same ratio and the works agree:'),
        ('m', r'F_1/a=F_2/A,\qquad F_1d_1=F_2d_2'),
        ('n', 'a 392 N push over 5 m lifts 19600 N by 0.10 m'),
    ])
    s.chip('gate', 'when the walk works', [('p', 'One connected fluid at rest, or rigidly accelerated (use g_eff).'), ('p', 'Same height, same pressure only inside the same continuous fluid.')])
    s.chip('trap', 'three traps', [('p', 'Adding p₀ twice when the two ends are both open.'), ('p', 'Forgetting the water above the mercury, or its density.'), ('p', 'Reading a manometer difference as an absolute pressure.')])
    s.chip('key', 'lift audit', [('m', r'F_2=F_1A/a'), ('m', r'd_1/d_2=A/a'), ('p', 'work in = work out, minus friction')])
    s.figure('manometer_walk')
    S.append(s)

    # ---------------------------------------------------------------- 3
    s = Sheet('JEE-03-plane-force', 'Where does the push on a gate act?',
              'A dam knows the total force and the point where a single resultant would act. Both come from the same integral.',
              K, 3, total, 'source: §3.3, E4, Q5-Q6',
              'force at the centroid of area, line of action below it')
    s.move('Integrate the linear pressure', [
        ('p', 'For a plane face, p = ρg × (vertical depth), which is linear across the face. The integral of a linear function is its value at the centroid:'),
        ('m', r'F=\int p\,dA=\rho g\,h_c A=p_cA', '(3.3)'),
        ('n', 'h_c is the vertical depth of the area centroid, not the depth of the plate centre in general'),
    ])
    s.move('The resultant sits lower', [
        ('p', 'Taking moments about the centroid gives the centre of pressure. For a rectangle whose top edge is at the free surface, h_c = H/2 and I_c = bH³/12, so h_cp = 2H/3. The extra H/6 is the whole story of a gate hinge.'),
        ('m', r'h_{cp}=h_c+\frac{I_c}{A\,h_c}\quad\Rightarrow\quad h_{cp}=\frac{2H}{3}'),
    ])
    s.move('Inclined faces', [
        ('p', 'Depth is still vertical: h = y sinα from the surface, and F = ρg h_c A. The centre of pressure moves closer to the centroid as the plate approaches horizontal, because the depth variation across it shrinks.'),
        ('n', 'torque about a top hinge = F × (h_cp − h_hinge)'),
    ])
    s.move('Shape independence, and where the weight went', [
        ('p', 'Three vessels with the same base and depth have equal base forces, though their weights differ. The difference is carried by the walls: a flared vessel pushes down on its base less than it weighs.'),
    ])
    s.chip('key', 'plane faces', [('m', r'F=p_cA'), ('m', r'h_{cp}=h_c+\frac{I_c}{Ah_c}'), ('p', 'rectangle from the surface: 2H/3')])
    s.chip('trap', 'hinge mistakes', [('p', 'Putting the resultant at the centroid.'), ('p', 'Using the slant length instead of vertical depth.'), ('p', 'Forgetting that a free surface at the top means zero pressure there.')])
    s.chip('check', 'sanity', [('p', 'If the plate is horizontal, every point is at one depth: cp = centroid.'), ('p', 'If it is deep, cp tends to the centroid because Δp across it is small.')])
    s.figure('plane_force')
    S.append(s)

    # ---------------------------------------------------------------- 4
    s = Sheet('JEE-04-curved-force', 'How much force does a curved face feel?',
              'A quadrant gate looks like a calculus problem. Projection turns it into two statics lookups.',
              K, 4, total, 'source: §3.3, E4, Q6',
              'split the force: projection for horizontal, column weight for vertical')
    s.move('Horizontal: project onto a vertical plane', [
        ('p', 'Every horizontal strip of the curved face has the same depth as the corresponding strip of its vertical projection. So the horizontal resultant equals the force on the projection, applied at the projection\'s centre of pressure.'),
        ('m', r'F_H=p_cA_{proj}', '(3.5)'),
    ])
    s.move('Vertical: weigh the column above', [
        ('p', 'The vertical component is the weight of the liquid that would fill the space between the face and the free surface: real column where liquid sits above the face, imagined column where it does not. The sign follows the wetted side.'),
        ('m', r'F_V=\rho g V_{column}'),
        ('n', 'draw the wetted side first; the sign of F_V is decided by that drawing'),
    ])
    s.move('Resultant and line of action', [
        ('p', 'Combine the two components. On a circular arc every elemental pressure force is radial, so the resultant must pass through the centre of curvature; use that instead of re-deriving moments.'),
        ('m', r'F=\sqrt{F_H^2+F_V^2},\qquad \tan\beta=\frac{F_V}{F_H}'),
    ])
    s.move('The quarter-cylinder gate, numerically', [
        ('p', 'Radius 2 m, width 3 m, water surface at the top of the gate. The projection is 2 × 3 m with its centroid 1 m deep; the column area is the square minus the quarter disc.'),
        ('m', r'F_H=5.88\times10^4\ \mathrm{N},\ F_V=2.52\times10^4\ \mathrm{N},\ F=6.4\times10^4\ \mathrm{N}'),
        ('n', 'direction 23° below horizontal, line of action through the arc centre'),
    ])
    s.chip('key', 'curved faces', [('p', 'F_H = p_c A_proj'), ('p', 'F_V = ρgV of the column above'), ('p', 'resultant through the centre of a circular arc')])
    s.chip('trap', 'wetting', [('p', 'Using the body volume instead of the liquid column.'), ('p', 'Assuming F_V always points down: a face wetted from below feels upthrust.')])
    s.chip('check', 'limits', [('p', 'Flat vertical face: F_V = 0, F_H = p_cA.'), ('p', 'Horizontal face: F_H = 0, F_V = weight above.')])
    s.figure('curved_gate')
    S.append(s)

    # ---------------------------------------------------------------- 5
    s = Sheet('JEE-05-accelerated', 'What changes when the tank moves?',
              'Accelerate a cup and the surface tilts. The physics is still hydrostatics, with a different gravity.',
              K, 5, total, 'source: §3.4, E5-E6, Q7',
              'replace g by g_eff = g − a and reuse every static tool')
    s.move('One substitution', [
        ('p', 'In the tank frame every element feels gravity plus the pseudo-force −ma. Define g_eff = g − a; the fluid is static under g_eff, so level surfaces are perpendicular to it and pressure grows along −g_eff.'),
        ('m', r'\mathbf{g}_{eff}=\mathbf{g}-\mathbf{a},\qquad \nabla p=\rho\,\mathbf{g}_{eff}'),
    ])
    s.move('The free surface tells you the answer', [
        ('p', 'A free surface is a level surface of p, so it is perpendicular to g_eff and therefore tilts by'),
        ('m', r'\tan\theta=\frac{a}{g}', '(3.4)'),
        ('n', 'vertical acceleration adds: g_eff = g + a; free fall gives g_eff = 0 and no pressure gradient'),
    ])
    s.move('Volume, not the surface, fixes the level', [
        ('p', 'Before spilling, the water volume is unchanged. A plane cut through a rectangular tank keeps the volume only if it passes through the mid-length point, so the surface pivots there: rise at the back equals fall at the front.'),
        ('m', r'\text{rise at back}=\frac{L}{2}\tan\theta'),
        ('n', 'E5: brim at a = 1.63 m/s²; bottom exposed at 4.08 m/s², after spilling has begun'),
    ])
    s.move('Light and heavy bodies disagree', [
        ('p', 'Buoyancy points along −g_eff. A helium balloon, lighter than air, leans along a; a plumb line, denser than air, hangs along g_eff, against a. Both are the same vector statement applied to bodies of opposite density.'),
        ('n', 'rule: balloon leans with a, plumb line against a'),
    ])
    s.chip('key', 'moving vessels', [('m', r'\tan\theta=a/g'), ('m', r'p=p_0+\rho\,g_{eff}h'), ('p', 'level surfaces perpendicular to g_eff')])
    s.chip('gate', 'rigid body only', [('p', 'The whole vessel accelerates together; no sloshing, no rotation of parts.'), ('p', 'For rotation add the centrifugal field ω²r radially.')])
    s.chip('trap', 'volume bookkeeping', [('p', 'Using the pivot rule after water starts spilling.'), ('p', 'Forgetting that a closed tank has no free surface, only tilted isobars.')])
    s.figure('accel_tank')
    S.append(s)

    # ---------------------------------------------------------------- 6
    s = Sheet('JEE-06-rotating', 'Why does the coffee climb the wall?',
              'Spin a bucket and the surface becomes a paraboloid. The shape follows from one force balance and one volume count.',
              K, 6, total, 'source: §3.4, OL2, Q7',
              'paraboloid: rim rise = centre drop when the volume is conserved')
    s.move('Balance a surface element', [
        ('p', 'A element on the surface feels N, mg and the pseudo-force mω²r. Dividing the horizontal balance by the vertical one gives the slope:'),
        ('m', r'\tan\alpha=\frac{dz}{dr}=\frac{\omega^2r}{g}\quad\Rightarrow\quad z=z_0+\frac{\omega^2r^2}{2g}', '(3.4)'),
    ])
    s.move('The pressure field behind it', [
        ('p', 'In the rotating frame, dp/dr = ρω²r and dp/dz = −ρg. Integrating gives a "rotating Bernoulli" whose constant-pressure surfaces are the same paraboloids.'),
        ('m', r'p-\frac{1}{2}\rho\omega^2r^2+\rho gz=\text{const}'),
    ])
    s.move('Volume conservation splits the difference', [
        ('p', 'The paraboloid holds exactly half the volume of the cylinder that circumscribes it. So the liquid lost near the axis equals the liquid gained at the rim: the rest level sits halfway, and each side moves Δz/2.'),
        ('m', r'\Delta z=\frac{\omega^2R^2}{2g},\qquad \text{centre drop}=\text{rim rise}=\frac{\Delta z}{2}'),
        ('n', 'ω = 4 s⁻¹, R = 0.30 m: Δz = 7.35 cm total, 3.7 cm each way'),
    ])
    s.move('When the bottom shows', [
        ('p', 'The surface reaches the bottom centre when the centre drop equals the original depth. Beyond that the paraboloid is cut by the floor and the simple volume argument must be replaced by the actual paraboloid volume.'),
        ('n', 'spilling begins when the rim rise exceeds the freeboard'),
    ])
    s.chip('key', 'rotating vessel', [('m', r'z=z_0+\frac{\omega^2r^2}{2g}'), ('m', r'p-\frac{1}{2}\rho\omega^2r^2+\rho gz=\text{const}'), ('p', 'rim-to-centre height = ω²R²/2g')])
    s.chip('trap', 'two errors', [('p', 'Saying the whole surface rises by Δz: it pivots about the rest level.'), ('p', 'Forgetting to conserve volume in a closed or partly filled vessel.')])
    s.chip('num', 'numbers', [('p', 'Δz = ω²R²/2g'), ('p', 'ω = 4, R = 0.30: 7.35 cm'), ('p', 'each side 3.7 cm')])
    s.figure('rotating_paraboloid')
    S.append(s)

    # ---------------------------------------------------------------- 7
    s = Sheet('JEE-07-buoyancy', 'What does a floating body actually displace?',
              'Archimedes is a pressure integral in disguise, and the volume that matters is the one the fluid lost.',
              K, 7, total, 'source: §3.5, E1, Q8-Q10',
              'buoyancy = weight of displaced fluid, acting at the centre of buoyancy')
    s.move('Archimedes from the pressure integral', [
        ('p', 'The horizontal pressure forces on a submerged body cancel in pairs. The vertical ones leave the difference between the push on the bottom and on the top, which is exactly the weight of the displaced fluid.'),
        ('m', r'F_b=(p_2-p_1)A=\rho_f gV_{disp}', '(3.6)'),
    ])
    s.move('Floating is an equilibrium statement', [
        ('p', 'A floating body displaces just enough fluid to carry its weight, so the submerged fraction is the density ratio. In layered fluids each layer contributes its own ρgV.'),
        ('m', r'\frac{V_s}{V}=\frac{\rho_b}{\rho_f}'),
        ('n', 'wood at 667 kg/m³ floats with two thirds under water'),
    ])
    s.move('Apparent weight and the two-fluid case', [
        ('p', 'A body weighed while submerged seems lighter by the weight of the fluid it displaces. With two liquids the displaced volumes are set by the layer boundaries, not by the body shape alone.'),
        ('m', r'W_{app}=W-\rho_fVg'),
        ('n', 'a cylinder half in water, half in oil: ρb = ½(1000) + ½(800) = 900 kg/m³'),
    ])
    s.move('Where the buoyant force acts', [
        ('p', 'It acts at the centroid of the displaced volume, the centre of buoyancy B, not at the centre of mass. That distinction is the whole of the next page on stability.'),
        ('n', 'a body whose density equals the fluid has no preferred depth: neutral equilibrium'),
    ])
    s.chip('key', 'buoyancy', [('m', r'F_b=\rho_fV_{disp}g'), ('m', r'V_s/V=\rho_b/\rho_f'), ('p', 'B = centroid of the displaced volume')])
    s.chip('trap', 'volume confusion', [('p', 'Using the whole body volume for a floating body.'), ('p', 'Putting F_b at the centre of mass, then wondering why the moments are wrong.'), ('p', 'Ignoring air buoyancy in a precision weighing.')])
    s.chip('check', 'limits', [('p', 'ρb -> ρf: the body is neutrally buoyant.'), ('p', 'ρb > ρf: it sinks and F_b is fixed at ρfVg.'), ('p', 'In an accelerating lift use g_eff.')])
    s.figure('buoyancy')
    S.append(s)

    # ---------------------------------------------------------------- 8
    s = Sheet('JEE-08-stability', 'When does a floating body tip over?',
              'A ship is stable although its centre of mass is above the waterline. The metacentre explains why.',
              K, 8, total, 'source: §3.5, Q8, D11.2',
              'stable when the metacentre M is above G; BM = I/V')
    s.move('Two different points', [
        ('p', 'Gravity acts at G, the centre of mass. Buoyancy acts at B, the centroid of the displaced volume. When the body heels, the submerged shape changes and B slides toward the low side; the body may right itself or capsize.'),
    ])
    s.move('The metacentre', [
        ('p', 'For a small heel the vertical through the new B meets the original centreline at M. The distance from B to M depends on the waterplane area and the displaced volume:'),
        ('m', r'BM=\frac{I}{V}'),
        ('n', 'I is the second moment of the waterplane area about the heel axis; V is the displaced volume'),
    ])
    s.move('The stability criterion', [
        ('p', 'If M is above G, a heel produces a righting moment; if M is below G, the moment tips the body further. For small angles the righting moment is linear in the heel.'),
        ('m', r'GM=BM-BG>0,\qquad \tau\approx W\,GM\,\theta'),
    ])
    s.move('A cylinder, to see the scaling', [
        ('p', 'A cylinder of radius r floating with draft d has I = πr⁴/4 and V = πr²d, so BM = r²/4d. A wide, shallow body is stable; a tall, narrow one is tender.'),
        ('m', r'BM=\frac{r^2}{4d}'),
        ('n', 'a fully submerged body has no waterplane: stability needs G below B'),
    ])
    s.chip('key', 'flotation stability', [('m', r'BM=I/V'), ('m', r'GM=BM-BG'), ('p', 'stable iff GM > 0')])
    s.chip('trap', 'two mistakes', [('p', 'Assuming a low G is enough: a submerged body needs G below B.'), ('p', 'Using the volume of the whole body instead of the displaced volume in BM.')])
    s.chip('num', 'feel for sizes', [('p', 'cylinder: BM = r²/4d'), ('p', 'wide beam buys stability cheaply'), ('p', 'ballast lowers G, not B')])
    s.figure('stability')
    S.append(s)

    # ---------------------------------------------------------------- 9
    s = Sheet('JEE-09-ice', 'Does the level rise when the ice melts?',
              'Four versions of one question. One ledger answers all four without a single integral.',
              K, 9, total, 'source: §3.6, E7, Q10-Q11',
              'compare the floating displacement with the volume added after melting')
    s.move('The ledger', [
        ('p', 'A floating body displaces its own mass of liquid. After melting, the water it becomes occupies its own mass divided by the density of the liquid it joins. Compare those two volumes; the sign of the difference is the sign of the level change.'),
        ('m', r'\Delta V=\frac{m}{\rho_f}-\frac{m}{\rho_{melt}}'),
    ])
    s.move('Pure ice: exactly zero', [
        ('p', 'Floating ice displaces m/ρw, and the melt water is m/ρw. The level does not move, however much of the cube is above water.'),
        ('m', r'\Delta h=0'),
    ])
    s.move('Ice carrying a stone', [
        ('p', 'While floating, the stone\'s weight is carried by the ice, so it displaces m_s/ρw. After melting the stone lies on the bottom and displaces only its own volume m_s/ρs. The difference is a fall.'),
        ('m', r'\Delta V=m_s\left(\frac{1}{\rho_w}-\frac{1}{\rho_s}\right)>0'),
        ('n', 'E7: 0.1 kg stone in 0.02 m² cylinder -> 3 mm fall'),
    ])
    s.move('Salt water and trapped air', [
        ('p', 'In salt water the melt is fresh and lighter than the brine it displaced, so the level rises. An air bubble has no mass, so it changes nothing: the ice still displaces its own mass.'),
        ('n', 'rules: stone falls, bubble unchanged, salt water rises, pure ice unchanged'),
    ])
    s.chip('key', 'ice family', [('p', 'pure ice: unchanged'), ('p', 'ice + stone: falls'), ('p', 'ice + air: unchanged'), ('p', 'ice in salt water: rises')])
    s.chip('trap', 'the usual slip', [('p', 'Tracking volumes of ice rather than masses of water.'), ('p', 'Forgetting that a sunken stone still displaces its own volume.')])
    s.chip('check', 'one-line audit', [('p', 'Floating: displaced volume ∝ mass.'), ('p', 'Sunk: displaced volume ∝ volume.'), ('p', 'Melt: added volume = mass / ρ of the receiving liquid.')])
    s.figure('ice_cases')
    S.append(s)

    # ---------------------------------------------------------------- 10
    s = Sheet('JEE-10-bernoulli', 'When may you use Bernoulli?',
              'The equation is short and the conditions are strict. Most lost marks are gate violations, not algebra.',
              K, 10, total, 'source: §3.8, E8, T8',
              'name the four gates before you write the equation')
    s.move('Derive it once, on a streamtube', [
        ('p', 'Take a steady streamtube between sections 1 and 2. In a time dt the pressure at section 1 does work p₁A₁v₁dt and section 2 removes p₂A₂v₂dt. The difference changes the kinetic and potential energy of the fluid between the sections.'),
        ('m', r'p_1+\frac{1}{2}\rho v_1^2+\rho gy_1=p_2+\frac{1}{2}\rho v_2^2+\rho gy_2', '(3.8)'),
    ])
    s.move('Divide by ρg and it becomes heads', [
        ('p', 'Each term is now a length: pressure head, velocity head, elevation head. A pitot tube reads the first two; a Venturi turns one into the other.'),
        ('m', r'\frac{p}{\rho g}+\frac{v^2}{2g}+y=\text{const}'),
    ])
    s.move('The four gates', [
        ('p', 'Steady flow, incompressible fluid, no viscous work, and both points on the same streamline. Drop any one and the constant changes along the flow, or between streamlines.'),
        ('n', 'a long pipe fails gate 3; a pump changes the constant; a boundary layer fails gate 4'),
    ])
    s.move('Where it must not be used', [
        ('p', 'Across a long narrow pipe the pressure falls linearly with length, not with v². Across a pump or turbine there is shaft work. In a viscous wake the total head drops from point to point.'),
        ('n', 'if the question names viscosity, length or flow rate, suspect Poiseuille'),
    ])
    s.chip('gate', 'the four gates', [('p', '1 steady'), ('p', '2 incompressible'), ('p', '3 inviscid'), ('p', '4 along one streamline')])
    s.chip('key', 'heads', [('m', r'\frac{p}{\rho g}+\frac{v^2}{2g}+y=\text{const}'), ('p', 'a pump adds head; a turbine removes it')])
    s.chip('trap', 'the classic', [('p', 'Applying Bernoulli between the ends of a long pipe and calling the loss a pressure drop.'), ('p', 'Using it across streamlines in a vortex.')])
    s.figure('bernoulli_streamtube')
    S.append(s)

    # ---------------------------------------------------------------- 11
    s = Sheet('JEE-11-devices', 'How do Venturi, pitot and siphon read a pressure difference?',
              'Three instruments, one balance. Each converts a speed into a height you can see.',
              K, 11, total, 'source: §3.9-3.10, E8, Q12-Q14',
              'continuity supplies the speed ratio; Bernoulli supplies the pressure drop')
    s.move('Venturi: continuity plus Bernoulli', [
        ('p', 'The throat is faster by the area ratio. Bernoulli between the wide section and the throat gives the pressure drop; a manometer reads it as a height difference.'),
        ('m', r'Q=A_1\sqrt{\frac{2\Delta p}{\rho\left(A_1^2/A_2^2-1\right)}}', '(3.9)'),
        ('n', 'A1/A2 = 2 gives v2 = 4v1 and a dynamic-pressure rise of 15/2 ρv1²'),
    ])
    s.move('Pitot: bring the fluid to rest', [
        ('p', 'At the mouth of a pitot tube the fluid stagnates, so the pressure there is the static pressure plus ½ρv². The difference is measured directly.'),
        ('m', r'v=\sqrt{\frac{2\Delta p}{\rho}}'),
        ('n', 'E8: Δp = 1470 Pa, A1/A2 = 2 -> Q = 1.77×10⁻³ m³/s'),
    ])
    s.move('Siphon: gravity across two free surfaces', [
        ('p', 'Both ends are at atmospheric pressure, so the speed depends only on the height difference between the surfaces. The top of the tube is the constraint: its pressure must stay above the liquid\'s vapour pressure.'),
        ('m', r'v=\sqrt{2g\,\Delta h},\qquad p_{top}=p_0-\rho g h_{top}-\frac{1}{2}\rho v^2\ge0'),
        ('n', 'this caps the lift at about 10.3 m of water'),
    ])
    s.move('Atomiser and aspirator', [
        ('p', 'A fast stream has low pressure, so it draws liquid up a side tube and shatters it into droplets. Same balance, run backwards: high speed, low pressure, entrainment.'),
    ])
    s.chip('key', 'three readings', [('p', 'Venturi: Q from Δp and the area ratio'), ('p', 'Pitot: v from the stagnation pressure'), ('p', 'Siphon: v from the free-surface height difference')])
    s.chip('trap', 'manometer fluid', [('p', 'Using Δp = ρgΔh with the wrong density: a mercury manometer reads (ρHg − ρ)gΔh.'), ('p', 'Ignoring the vapour-pressure cap on a siphon.')])
    s.chip('check', 'limits', [('p', 'A2 -> A1: Q -> ∞ is the signal that the model has lost the pressure drop.'), ('p', 'Pitot in a viscous boundary layer reads too little.')])
    s.figure('venturi_pitot')
    S.append(s)

    # ---------------------------------------------------------------- 12
    s = Sheet('JEE-12-torricelli', 'How fast does water leave a hole, and where does it land?',
              'Depth sets the speed, the fall sets the time, and their product sets the range.',
              K, 12, total, 'source: §3.10, E5, Q13-Q15, OL1',
              'v = sqrt(2gh); range peaks at half depth; the tank empties in finite time')
    s.move('Speed from the surface', [
        ('p', 'Apply Bernoulli between the free surface (p₀, v ≈ 0) and the hole (p₀). The depth h is the only head left. The exact result keeps the surface speed through continuity.'),
        ('m', r'v=\sqrt{2gh}\quad\left(\text{exact: } v=\sqrt{\frac{2gh}{1-(a/A)^2}}\right)', '(3.10)'),
        ('n', 'the correction is 0.5% for a/A = 0.1, but 25% for a/A = 0.6'),
    ])
    s.move('Range: two motions at once', [
        ('p', 'The jet leaves horizontally and falls a distance H − h. Eliminating time gives the range, whose maximum is at half depth.'),
        ('m', r'x=2\sqrt{h(H-h)},\qquad x_{max}=H \text{ at } h=H/2', '(3.11)'),
    ])
    s.move('Draining: a clock made of area', [
        ('p', 'With a ≪ A the flow is quasi-steady: −A dh/dt = a√(2gh). Separating and integrating gives a finite emptying time, and a height that is a perfect square in time.'),
        ('m', r'T=\frac{A}{a}\sqrt{\frac{2H}{g}},\qquad h(t)=H\left(1-\frac{t}{T}\right)^2'),
        ('n', 'A/a = 100, H = 1.25 m -> T = 50.5 s'),
    ])
    s.move('Two holes, moving tanks and siphons', [
        ('p', 'Two holes at depths h₁ and h₂ give speeds in the ratio √h₁:√h₂ and thrusts in that ratio squared. A moving tank adds a pseudo-force term; a sealed tank slows as the air above expands.'),
        ('n', 'a jet from a hole in a tank on a cart pushes the cart the other way'),
    ])
    s.chip('key', 'Torricelli family', [('m', r'v=\sqrt{2gh}'), ('m', r'x=2\sqrt{h(H-h)}'), ('m', r'T=\frac{A}{a}\sqrt{\frac{2H}{g}}')])
    s.chip('gate', 'quasi-steady', [('p', 'a ≪ A, so the surface speed is negligible.'), ('p', 'The hole is sharp and short; a long tube makes it a Poiseuille problem.')])
    s.chip('trap', 'surface speed', [('p', 'Forgetting the 1 − (a/A)² correction for a large hole.'), ('p', 'Using H instead of H − h in the range formula.')])
    s.figure('torricelli')
    S.append(s)

    # ---------------------------------------------------------------- 13
    s = Sheet('JEE-13-momentum', 'Why does a hose push back?',
              'Pressure is not the force on a plate. Momentum flux is.',
              K, 13, total, 'source: §3.11, Q16-Q17',
              'force = momentum flux: ρav² stopped, ρa(v−u)² on a retreating plate')
    s.move('Mass flow carries momentum', [
        ('p', 'A jet of area a and speed v delivers mass ρav every second, each kilogram carrying v. If the plate stops the jet, the whole momentum flux becomes a force.'),
        ('m', r'F=\dot m v=\rho a v^2', '(3.12)'),
        ('n', 'a 5 cm² hose at 20 m/s pushes with 200 N'),
    ])
    s.move('A plate that runs away', [
        ('p', 'If the plate moves at u in the jet direction, the impact speed is v − u and the mass striking it per second is ρa(v − u). The force falls as the square of the relative speed, and the power delivered peaks at u = v/3.'),
        ('m', r'F=\rho a (v-u)^2,\qquad P=Fu'),
    ])
    s.move('Curved vanes and reversals', [
        ('p', 'A vane that turns the jet through 180° reverses its momentum, so the force doubles. Turning it through an angle φ gives a factor (1 − cosφ) per unit mass flow.'),
        ('m', r'F=\rho a v^2(1-\cos\varphi)'),
    ])
    s.move('Ejection is the same statement', [
        ('p', 'A rocket or a sprinkler feels the reaction of the momentum it throws away. The thrust is the momentum flux plus any pressure difference across the nozzle exit.'),
        ('m', r'F=\rho a v_e^2+(p_e-p_0)A_e'),
        ('n', 'for a hose the pressure term is already counted inside ρav² if the jet is at atmospheric pressure'),
    ])
    s.chip('key', 'momentum flux', [('m', r'F=\rho a v^2'), ('m', r'F=\rho a(v-u)^2'), ('p', 'reversal doubles the force')])
    s.chip('trap', 'not pressure', [('p', 'Using pA at the nozzle instead of the momentum flux.'), ('p', 'Forgetting the relative speed for a moving plate.'), ('p', 'Adding speeds instead of subtracting them.')])
    s.chip('check', 'limits', [('p', 'u = 0 recovers the fixed plate.'), ('p', 'u = v gives zero force and zero power.'), ('p', 'φ = 180° doubles the force.')])
    s.figure('jet_thrust')
    S.append(s)

    # ---------------------------------------------------------------- 14
    s = Sheet('JEE-14-poiseuille', 'Why does a narrow pipe strangle the flow?',
              'Viscosity turns a pressure difference into a flow rate, and the fourth power of the radius decides who wins.',
              K, 14, total, 'source: §3.12-3.13, Q19-Q20',
              'Q ∝ R⁴Δp/ηL: the radius is the whole design')
    s.move('Newton\'s law of viscosity', [
        ('p', 'Fluid layers slide past each other; the shear stress is proportional to the velocity gradient. The constant η is the dynamic viscosity, in Pa·s. At a solid wall the fluid does not slip.'),
        ('m', r'\tau=\eta\frac{dv}{dy}'),
    ])
    s.move('Shell balance, then integrate', [
        ('p', 'On a cylindrical shell of radius r and length L, the pressure force πr²Δp balances the shear on the curved surface 2πrLτ. Substituting Newton\'s law and integrating with v(R) = 0 gives the parabolic profile.'),
        ('m', r'\tau=\frac{r\Delta p}{2L},\qquad v(r)=\frac{\Delta p}{4\eta L}(R^2-r^2)'),
        ('m', r'Q=\frac{\pi R^4\Delta p}{8\eta L}', '(3.13)'),
    ])
    s.move('What the quartic does', [
        ('p', 'Halve the radius and the same pressure drives 1/16 of the flow. The mean speed is half the centreline speed, and the wall shear is 4ηv_avg/R. Doubling the length doubles the drop.'),
        ('m', r'v_{max}=2v_{avg},\qquad \tau_w=\frac{4\eta v_{avg}}{R}'),
    ])
    s.move('Where the law stops', [
        ('p', 'The derivation assumes laminar, steady, fully developed flow of a Newtonian fluid with no slip. Above Re ≈ 2000 the flow becomes turbulent, the profile flattens and Δp grows roughly as Q².'),
        ('n', 'entrance length ≈ 0.06 Re D: near the inlet the profile is still developing'),
    ])
    s.chip('key', 'pipe flow', [('m', r'Q=\frac{\pi R^4\Delta p}{8\eta L}'), ('m', r'v_{max}=2v_{avg}'), ('p', 'wall shear 4ηv/R')])
    s.chip('gate', 'laminar only', [('p', 'Re = ρvD/η ≲ 2000'), ('p', 'Newtonian, no slip, fully developed'), ('p', 'straight pipe, no fittings')])
    s.chip('trap', 'two habits', [('p', 'Using Bernoulli along a long pipe.'), ('p', 'Forgetting that a narrower section has a much larger resistance, not just a larger speed.')])
    s.figure('poiseuille_profile')
    S.append(s)

    # ---------------------------------------------------------------- 15
    s = Sheet('JEE-15-networks', 'How do pipes combine like resistors?',
              'Once the flow is linear in Δp, a pipe network is a circuit with pressure for voltage.',
              K, 15, total, 'source: §3.12, Q19, T5',
              'series adds R; parallel splits Q as 1/R')
    s.move('The hydraulic Ohm\'s law', [
        ('p', 'Poiseuille is linear in the pressure drop, so each pipe is a resistor. The analogy is exact while the flow stays laminar and the fluid incompressible.'),
        ('m', r'\Delta p=R_{hyd}Q,\qquad R_{hyd}=\frac{8\eta L}{\pi R^4}'),
    ])
    s.move('Series and parallel', [
        ('p', 'In series the same Q passes through every pipe and the drops add. In parallel every branch sees the same drop and the flows add, so conductances add.'),
        ('m', r'R_{series}=\sum R_i,\qquad \frac{1}{R_{parallel}}=\sum\frac{1}{R_i}'),
    ])
    s.move('A factor of sixteen, then seventeen', [
        ('p', 'Two capillaries of radii r and r/2 in series carry the same flow. The narrow one has 16 times the resistance, so it takes 16/17 of the total drop: 2.82×10⁵ Pa out of 3×10⁵ Pa.'),
        ('m', r'\frac{\Delta p_{narrow}}{\Delta p_{total}}=\frac{16}{17}'),
    ])
    s.move('Design consequences', [
        ('p', 'A small narrowing dominates a network; a parallel bypass steals flow in proportion to R⁻¹. The same algebra sizes blood vessels, irrigation lines and oil pipelines, until turbulence or elasticity breaks the linearity.'),
        ('n', 'two equal pipes in parallel carry half each; a 2:1 radius pair carries 16:1'),
    ])
    s.chip('key', 'network rules', [('m', r'R=8\eta L/\pi R^4'), ('p', 'series: R adds, Q same'), ('p', 'parallel: 1/R adds, Δp same')])
    s.chip('trap', 'analogy limits', [('p', 'Turbulent pipes: Δp ∝ Q², so R is not constant.'), ('p', 'Fittings, bends and valves add local losses.'), ('p', 'Compliant vessels store volume, like capacitors.')])
    s.chip('num', 'the 17', [('p', 'r and r/2: resistance ratio 16'), ('p', 'narrow drop = 16/17 of total'), ('p', 'its flow if parallel = 1/17')])
    s.figure('hydraulic_network')
    S.append(s)

    # ---------------------------------------------------------------- 16
    s = Sheet('JEE-16-stokes', 'How fast does a small sphere sink?',
              'Stokes drag is a low-Reynolds result. The number that validates it is the one most answers omit.',
              K, 16, total, 'source: §3.13, E9, Q20',
              'terminal velocity v_t = 2r²Δρg/9η, valid while Re ≲ 1')
    s.move('Three forces at terminal speed', [
        ('p', 'Weight down, buoyancy up, drag up. At terminal speed the acceleration is zero. Stokes solved the slow-flow drag around a sphere:'),
        ('m', r'F_d=6\pi\eta rv', '(3.14)'),
        ('n', 'the derivation assumes Re ≪ 1, so inertia is negligible and the flow is reversible'),
    ])
    s.move('Solve for the terminal speed', [
        ('p', 'Setting 6πηrv equal to the net weight 4/3πr³(ρ − σ)g gives a speed proportional to r². That squared signature is the experimental fingerprint of Stokes flow.'),
        ('m', r'v_t=\frac{2r^2(\rho-\sigma)g}{9\eta}', '(3.15)'),
        ('n', 'a 0.10 mm raindrop: v_t = 1.21 m/s on paper'),
    ])
    s.move('Then check the Reynolds number', [
        ('p', 'The same raindrop has Re ≈ 16, far outside Stokes. The honest terminal speed is lower once quadratic drag enters, of order 0.7 to 1 m/s. An answer without Re is an unfinished answer.'),
        ('m', r'\text{Re}=\frac{\rho vD}{\eta},\qquad \text{Stokes needs Re}\lesssim1'),
    ])
    s.move('What replaces it at larger sizes', [
        ('p', 'At large Re the drag is quadratic, F ≈ ½C_dρπr²v², and the terminal speed scales as √r instead of r². Between the two regimes there is a crossover radius; the Olympiad page finds it.'),
        ('m', r'F_d\approx\frac{1}{2}C_d\rho\pi r^2v^2'),
    ])
    s.chip('key', 'Stokes', [('m', r'F_d=6\pi\eta rv'), ('m', r'v_t=\frac{2r^2\Delta\rho\,g}{9\eta}'), ('p', 'always print Re with v_t')])
    s.chip('gate', 'Re ≲ 1', [('p', 'small sphere, slow flow, no wall nearby'), ('p', 'wall correction: divide by 1 + 2.4r/R'), ('p', 'above Re ≈ 1 use quadratic drag')])
    s.chip('trap', 'the missing check', [('p', 'Quoting 1.21 m/s for a raindrop and stopping there.'), ('p', 'Using the sphere radius where the diameter belongs in Re.')])
    s.figure('stokes_regime')
    S.append(s)

    # ---------------------------------------------------------------- 17
    s = Sheet('JEE-17-surface-energy', 'Why is a soap film a stretched sheet?',
              'Surface tension can be read as a force per length or an energy per area. The film makes the factor of two visible.',
              K, 17, total, 'source: §3.14, Q24-Q25',
              'two definitions, one number; a film has two faces')
    s.move('Two definitions', [
        ('p', 'Pull a slider along a soap film: the force per unit length of the slider is γ. Alternatively, count the energy needed to create new surface: γ is also the energy per unit area. For a simple liquid the two numbers are identical.'),
        ('m', r'\gamma=\frac{F}{L}=\frac{W}{\Delta A}'),
        ('n', 'units: N/m = J/m²'),
    ])
    s.move('The film doubles everything', [
        ('p', 'A soap film has two free surfaces, so the force on the slider is 2γL and stretching it by dx costs 2γLdx. This factor of two is the most reliably forgotten factor in the chapter.'),
        ('m', r'F_{film}=2\gamma L,\qquad W=2\gamma\Delta A'),
    ])
    s.move('Where the energy goes', [
        ('p', 'A molecule in the bulk is pulled equally in all directions; one at the surface has fewer neighbours and therefore higher energy. Creating area raises the energy, which is why free surfaces shrink to the smallest area they can.'),
        ('m', r'U_{surface}=\gamma A'),
        ('n', 'splitting a 1 mm drop into 1000 droplets costs 8.2×10⁻⁶ J'),
    ])
    s.move('Values and temperature', [
        ('p', 'Water\'s γ falls from 0.0728 N/m at 20 °C toward zero at the critical point; mercury\'s is about 0.465 N/m, which is why it beads and does not wet glass. Surfactants lower γ by sitting at the interface.'),
    ])
    s.chip('key', 'surface tension', [('m', r'\gamma=F/L=W/\Delta A'), ('m', r'F_{film}=2\gamma L'), ('p', 'U = γA for one surface')])
    s.chip('trap', 'factor two', [('p', 'Using γL for a soap film.'), ('p', 'Counting the area of one face when two are created.'), ('p', 'Mixing up N/m and N/m².')])
    s.chip('num', 'values at 20 °C', [('p', 'water 0.0728 N/m'), ('p', 'mercury 0.465 N/m'), ('p', 'soap solution ≈ 0.025-0.03 N/m')])
    s.figure('surface_energy')
    S.append(s)

    # ---------------------------------------------------------------- 18
    s = Sheet('JEE-18-excess-pressure', 'Why is the pressure inside a bubble higher?',
              'Curvature costs surface energy, so a curved interface must carry a pressure step.',
              K, 18, total, 'source: §3.15, Q21, D11.14',
              'drop 2γ/r, soap bubble 4γ/r, cylinder γ/r')
    s.move('Balance half a drop', [
        ('p', 'Cut a droplet through its centre. The pressure difference pushes the hemisphere out with Δp·πr²; the rim pulls it back with 2πrγ. Dividing gives the excess pressure.'),
        ('m', r'\Delta p=\frac{2\gamma}{r}'),
    ])
    s.move('Count surfaces before you divide', [
        ('p', 'A soap bubble has an inner and an outer surface, so the same balance carries a factor two. A cylindrical jet has one curved radius, and the missing second curvature halves the result again.'),
        ('m', r'\Delta p_{bubble}=\frac{4\gamma}{r},\qquad \Delta p_{jet}=\frac{\gamma}{r}', '(3.17)'),
    ])
    s.move('The general law', [
        ('p', 'For any smooth patch with principal radii r₁ and r₂, the pressure step is γ times the sum of the curvatures. A saddle has curvatures of opposite sign and can have zero mean curvature.'),
        ('m', r'\Delta p=\gamma\left(\frac{1}{r_1}+\frac{1}{r_2}\right)', '(3.18)'),
    ])
    s.move('Consequences', [
        ('p', 'Small bubbles have the higher pressure, so they empty into large ones through a connecting tube. Blowing a bubble is hardest at the start, when r is smallest. Two equal bubbles coalesce slowly; a small one disappears.'),
        ('n', 'Q21: bubbles r and 3r coalesce isothermally to R = 2r, conserving moles, not volume'),
    ])
    s.chip('key', 'excess pressure', [('m', r'\Delta p=2\gamma/r'), ('m', r'\Delta p=4\gamma/r'), ('m', r'\Delta p=\gamma(1/r_1+1/r_2)')])
    s.chip('trap', 'surface counting', [('p', 'Using 2γ/r for a soap bubble.'), ('p', 'Using 4γ/r for a liquid drop in air.'), ('p', 'Forgetting that a bubble in water has one surface; in air it has two.')])
    s.chip('check', 'limits', [('m', r'r\to\infty:\ \Delta p\to0'), ('p', 'sphere: both radii equal'), ('p', 'cylinder: one radius infinite')])
    s.figure('excess_pressure')
    S.append(s)

    # ---------------------------------------------------------------- 19
    s = Sheet('JEE-19-jurin', 'How high does water climb a narrow tube?',
              'Capillary rise is a force balance and an energy minimum, and the two disagree by a factor of two unless you audit the dissipation.',
              K, 19, total, 'source: §3.16, E10, Q22-Q23',
              'h = 2γcosθ/ρgr; a short tube only changes the curvature')
    s.move('Force balance on the column', [
        ('p', 'The rim pulls up with 2πrγcosθ; the column weighs ρgπr²h. Setting them equal gives Jurin\'s law. The contact angle is measured through the liquid.'),
        ('m', r'h=\frac{2\gamma\cos\theta}{\rho g r}', '(3.19)'),
        ('n', 'r = 0.5 mm, clean water: h = 2.97 cm'),
    ])
    s.move('Mercury walks the other way', [
        ('p', 'For θ > 90° the cosine is negative and the surface is depressed: a convex meniscus. Mercury in a 1 mm tube sits 1.07 cm below the outside level.'),
        ('m', r'h=\frac{2(0.465)\cos140^\circ}{(13600)(9.8)(5\times10^{-4})}=-1.07\ \mathrm{cm}'),
    ])
    s.move('Energy: the same answer, twice the budget', [
        ('p', 'The potential energy is ½ρgπr²h² minus the surface energy released 2πrγhcosθ. Minimising reproduces Jurin exactly. But the total adhesion release is twice the gravitational gain; the other half is dissipated as the column oscillates and settles.'),
        ('m', r'U(h)=\frac{1}{2}\rho g\pi r^2h^2-2\pi r\gamma h\cos\theta'),
        ('n', 'E10: U_g = 3.4×10⁻⁶ J, adhesion release 6.8×10⁻⁶ J'),
    ])
    s.move('Short and tilted tubes', [
        ('p', 'If the tube is shorter than h, the meniscus flattens until its radius R′ satisfies hR = h′R′; the liquid does not overflow. Tilting the tube lengthens the wetted run but leaves the vertical rise unchanged.'),
        ('m', r"hR=h'R'"),
    ])
    s.chip('key', 'capillarity', [('m', r'h=\frac{2\gamma\cos\theta}{\rho g r}'), ('m', r"hR=h'R'"), ('p', 'θ measured through the liquid')])
    s.chip('trap', 'signs and factors', [('p', 'Measuring θ through the gas, which flips the sign for mercury.'), ('p', 'Using the diameter where the radius belongs.'), ('p', 'Assuming a short tube overflows.')])
    s.chip('num', 'bench numbers', [('p', 'water: 2.97 cm at r = 0.5 mm'), ('p', 'mercury: −1.07 cm at r = 0.5 mm'), ('p', 'h ∝ 1/r, so 10 µm gives 2.97 m')])
    s.figure('jurin')
    S.append(s)

    return S
