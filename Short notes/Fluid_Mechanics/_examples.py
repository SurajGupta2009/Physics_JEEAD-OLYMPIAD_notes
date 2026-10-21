"""A worked-number block for each page.

Every page closes with one short calculation, so the theory is anchored to a
number a student can reproduce. The numbers are recomputed here, not copied.
"""

EX = {
 'JEE-02-manometer': ('A worked reading', [
   ('p', 'Q3: 10 cm of oil (800 kg/m³) floats on water in one limb of an open U-tube. Balance the two columns at the interface: the water level in that limb sits lower.'),
   ('m', r'\rho_o h_o=\rho_w h_w\ \Rightarrow\ h_w=0.8(10)=8\ \mathrm{cm}'),
   ('n', 'Q4: a/A = 1/50 holding 500 kg needs 98 N and a 1 m input stroke for a 2 cm rise'),
 ]),
 'JEE-03-plane-force': ('A worked gate', [
   ('p', 'A 2 m high, 3 m wide gate hangs with its top edge at the water surface. The centroid is 1 m down, and the resultant acts 2H/3 below the surface.'),
   ('m', r'F=5.88\times10^4\ \mathrm{N},\qquad \tau_{top}=F(4/3)=7.84\times10^4\ \mathrm{N\cdot m}'),
   ('n', 'the hinge feels the centre of pressure, not the centroid: the lever arm is 4/3 m, not 1 m'),
 ]),
 'JEE-04-curved-force': ('A worked projection', [
   ('p', 'A hemispherical bump of radius 0.5 m sits in a wall with its centre 2 m below the surface. The horizontal force needs only the projected circle.'),
   ('m', r'F_H=p_cA_{proj}=(1000)(9.8)(2)\pi(0.5)^2=1.54\times10^4\ \mathrm{N}'),
   ('n', 'the vertical part needs the real or imagined column above the curved surface'),
 ]),
 'JEE-05-accelerated': ('A worked lift', [
   ('p', 'Q7: a tank accelerates upward at g. Effective gravity doubles, so the pressure at depth h doubles and so does the reading of a scale under the tank.'),
   ('m', r'p=p_0+2\rho g h'),
   ('n', 'in free fall g_eff = 0: a hole in a falling bottle does not squirt'),
 ]),
 'JEE-06-rotating': ('How the numbers scale', [
   ('p', 'The rim rise is quadratic in the radius. Halve the bucket and the same spin lifts the rim by a quarter as much.'),
   ('m', r'\Delta z(0.15\ \mathrm{m})=\frac{16(0.0225)}{19.6}=1.84\ \mathrm{cm}'),
   ('n', 'the centre drop is still half of that: volume conservation is untouched by the radius'),
 ]),
 'JEE-07-buoyancy': ('A worked two-fluid float', [
   ('p', 'Q8: a cylinder of density 667 floats in water, then oil of density 500 is poured until it is just covered. Two liquids now share the buoyancy.'),
   ('m', r'667=1000f+500(1-f)\ \Rightarrow\ f=\frac{1}{3}'),
   ('n', 'without the oil f = 2/3; the upper liquid carries the rest, so the cylinder rides higher'),
 ]),
 'JEE-08-stability': ('A worked metacentre', [
   ('p', 'A cylinder of radius 0.50 m floats with a 0.50 m draft. Its metacentre sits above the centre of buoyancy by r²/4d.'),
   ('m', r'BM=\frac{(0.50)^2}{4(0.50)}=0.125\ \mathrm{m}'),
   ('n', 'if G is 0.10 m above B then GM = 0.025 m: stable, but tender'),
 ]),
 'JEE-09-ice': ('A worked stone', [
   ('p', 'A 10 cm ice cube carries a 20 g stone in a tank of area 0.02 m². The stone loses the extra displacement it had while riding the ice.'),
   ('m', r'\Delta h=\frac{m_s(1/\rho_w-1/\rho_s)}{A}=\frac{(0.02)(6\times10^{-4})}{0.02}=0.6\ \mathrm{mm}'),
   ('n', 'without the stone the level does not move at all'),
 ]),
 'JEE-10-bernoulli': ('A worked pipe', [
   ('p', 'Q12: water at 1.2 m/s in a 2 cm radius pipe enters a 1 cm radius section 10 m lower. Continuity fixes the speed; Bernoulli fixes the pressure.'),
   ('m', r'v_2=1.2\left(\frac{2}{1}\right)^2=4.8\ \mathrm{m/s}'),
   ('m', r'p_1-p_2=\frac{1}{2}\rho(v_2^2-v_1^2)+\rho g(10)=1.088\times10^5\ \mathrm{Pa}'),
   ('n', 'the 10 m drop contributes 98 kPa; the narrowing only 10.8 kPa'),
 ]),
 'JEE-11-devices': ('A worked siphon', [
   ('p', 'Q14: a siphon lifts water 3 m above the supply surface and discharges 2 m below it. The driving head is the 2 m drop, not the 3 m lift.'),
   ('m', r'v=\sqrt{2(9.8)(2)}=6.26\ \mathrm{m/s}'),
   ('m', r'p_{top}=p_0-\rho g(3)-\frac{1}{2}\rho v^2=5.2\times10^4\ \mathrm{Pa}'),
   ('n', 'positive, so this siphon works; at a 10 m lift it would not'),
 ]),
 'JEE-12-torricelli': ('A worked range', [
   ('p', 'Q13: a tank 1.25 m deep has a hole 0.8 m below the surface. The jet falls the remaining 0.45 m while travelling horizontally.'),
   ('m', r'x=2\sqrt{(0.8)(0.45)}=1.2\ \mathrm{m}'),
   ('n', 'Q15: A/a = 100 gives T = 50.5 s, and the tank is exactly empty at T'),
 ]),
 'JEE-13-momentum': ('A worked hose', [
   ('p', 'Q16: a 5 cm² hose delivers water at 20 m/s onto a wall, and the water leaves along the wall. All the horizontal momentum flux becomes force.'),
   ('m', r'F=\rho a v^2=1000(5\times10^{-4})(400)=200\ \mathrm{N}'),
   ('n', 'Q17: holes at h and 4h give speeds 1:2 and thrusts 1:4'),
 ]),
 'JEE-14-poiseuille': ('A worked radius, and a warning', [
   ('p', 'A sphere of density 2000 falls at 0.1 m/s in glycerine (1260 kg/m³, 1.5 Pa·s). Solve Stokes for the radius, then test the answer.'),
   ('m', r'r=\sqrt{\frac{9\eta v}{2\Delta\rho g}}=9.65\times10^{-3}\ \mathrm{m},\qquad \text{Re}=1.6'),
   ('n', 'Re > 1, so Stokes is not valid here: the printed 3 mm answer in the source fails its own check'),
 ]),
 'JEE-15-networks': ('A worked divider', [
   ('p', 'Q19: two capillaries of radii r and r/2, same length, in series under 3×10⁵ Pa. The resistances are in the ratio 1:16.'),
   ('m', r'\Delta p_{narrow}=\frac{16}{17}(3\times10^5)=2.82\times10^5\ \mathrm{Pa}'),
   ('n', 'the flow is the same in both; only the pressure drops differ'),
 ]),
 'JEE-16-stokes': ('The raindrop, checked', [
   ('p', 'E9: a 0.10 mm water drop in air. Stokes gives a speed, but the same numbers give a Reynolds number far above one.'),
   ('m', r'v_t=1.21\ \mathrm{m/s},\qquad \text{Re}=16'),
   ('n', 'the honest terminal speed is 0.7-1 m/s: Stokes overestimates once inertia matters'),
 ]),
 'JEE-17-surface-energy': ('Two worked surfaces', [
   ('p', 'Q24: lift a 10 cm square frame from water, film on both faces. Q25: split a 1 mm drop into a thousand equal droplets.'),
   ('m', r'F=2\gamma(0.40)=0.058\ \mathrm{N},\qquad W=\gamma(36\pi R^2)=8.2\times10^{-6}\ \mathrm{J}'),
   ('n', 'both use the two-surface count; forgetting it halves or doubles the answer'),
 ]),
 'JEE-18-excess-pressure': ('Bubbles that merge', [
   ('p', 'Q21: two soap bubbles of radii r and 3r coalesce isothermally in vacuum. For a bubble pV ∝ r², so the moles add as radii squared.'),
   ('m', r'r^2+(3r)^2=R^2\ \Rightarrow\ R=\sqrt{10}\,r'),
   ('n', 'the chapter prints R = 2r from an arithmetic slip in the second bubble: see SOURCE-AUDIT'),
 ]),
 'JEE-19-jurin': ('A worked short tube', [
   ('p', 'Q22: water rises 12 cm in a capillary, but the tube is cut to 9 cm. The meniscus flattens until its radius of curvature satisfies the same force balance.'),
   ('m', r"hR=h'R'\ \Rightarrow\ \frac{R'}{R}=\frac{12}{9}=\frac{4}{3}"),
   ('n', 'Q23: mercury in a 1 mm tube is depressed 1.07 cm, because cos140° is negative'),
 ]),
 'Olympiad-01-drain': ('Two numbers for the crossover', [
   ('p', 'The crossover height is enormous for a viscous liquid and modest for water, which is exactly why the teaching pair is fragile.'),
   ('m', r'h^*=1.2\times10^7\ \mathrm{m}\ (\text{glycerine}),\qquad h^*\approx5\ \mathrm{m}\ (\text{water})'),
   ('n', 'water at that speed in a fine tube has Re of order 10³: the real late regime is turbulent'),
 ]),
 'Olympiad-02-paraboloid': ('The same bucket on a cart', [
   ('p', 'Replace the centrifugal field by a constant −a and all three derivations survive: equipotentials become planes, and the free surface tilts.'),
   ('m', r'z=z_0-\frac{a}{g}x'),
   ('n', 'rotation adds nothing essential except a radial coordinate'),
 ]),
 'Olympiad-03-raindrop': ('Two sizes, five decades', [
   ('p', 'A 10 µm mist droplet and a 2 mm raindrop differ in radius by a factor of two hundred; their terminal speeds differ by five orders of magnitude.'),
   ('m', r'v(10\,\mu\mathrm{m})=1.2\ \mathrm{cm/s},\qquad v(2\ \mathrm{mm})=9.9\ \mathrm{m/s}'),
   ('n', 'this is why mist hangs and rain arrives'),
 ]),
 'Olympiad-04-young-laplace': ('A film between rings', [
   ('p', 'Rings of radius 2 cm hold a soap film. At 1 cm separation the catenoid spans; at 3 cm it cannot, and the film snaps into two discs.'),
   ('m', r'd/R=0.5\ \text{spans},\qquad d/R=1.5\ \text{snaps}'),
   ('n', 'the threshold is d/R ≈ 1.325, not a matter of patience'),
 ]),
 'Olympiad-05-drop-strider': ('Calibrate the method', [
   ('p', 'The drop count gives a naive surface tension; the Harkins-Brown factor converts it into the tabulated value.'),
   ('m', r'\gamma=\frac{0.048}{0.66}=0.073\ \mathrm{N/m}'),
   ('n', 'a 4% error in f moves gamma by 4%: the method is only as good as its correction'),
 ]),
 'Olympiad-06-tree': ('The tension needed', [
   ('p', 'A 112 m redwood needs about a megapascal of tension at the top, not a metre of suction.'),
   ('m', r'p=-\rho g h=-(1000)(9.8)(112)=-1.1\ \mathrm{MPa}'),
   ('n', 'the same column would stop at 10.3 m if it relied on suction alone'),
 ]),
 'Olympiad-07-shallow-wave': ('A ten percent bump', [
   ('p', 'A 10 cm bump on 1 m of water is already at the edge of the small-amplitude expansion, and the correction is measurable.'),
   ('m', r'c=\sqrt{9.8}\left(1+\frac{3(0.1)}{4}\right)=3.34\ \mathrm{m/s}\ \text{vs}\ 3.13'),
   ('n', 'the crest outruns the trough by 7%: the wave steepens'),
 ]),
 'Olympiad-08-sprinkler': ('A garden sprinkler', [
   ('p', 'Two nozzles, 0.2 kg/s total, at 0.15 m radius with a 3 m/s tangential jet. The reaction torque follows from the angular momentum flux.'),
   ('m', r'\tau=\dot m\,r v_\theta=(0.2)(0.15)(3)=0.09\ \mathrm{N\cdot m}'),
   ('n', 'at 3 rad/s that is 0.27 W of mechanical power'),
 ]),
 'Olympiad-09-rotating-energy': ('Per kilogram, not per page', [
   ('p', 'Divide the single-mass result by the mass and the geometry is all that is left: every kilogram that moves from r1 to r2 gains the same energy, whatever the flow rate.'),
   ('m', r'\frac{\Delta K}{m}=\frac{1}{2}\omega^2(r_2^2-r_1^2)=4.0\ \mathrm{J/kg}'),
   ('n', 'a steady flow must be fed this much per kilogram; the motor torque is what feeds it'),
 ]),
 'Olympiad-10-viscometer': ('A smaller sphere', [
   ('p', 'Halve the sphere radius and Stokes predicts a quarter of the terminal speed, so the timing run gets four times longer.'),
   ('m', r'v_t=\frac{0.0380}{4}=9.5\times10^{-3}\ \mathrm{m/s},\quad t=\frac{0.20}{0.0095}=21\ \mathrm{s}'),
   ('n', 'Re falls to 0.012: even more comfortably inside Stokes'),
 ]),
}


def add_all(sheets):
    missing = [s.slug for s in sheets if s.slug not in EX and s.slug != 'JEE-01-pressure']
    assert set(missing) <= {'Olympiad-11-regime-map'}, f'no worked block for: {missing}'
    for s in sheets:
        if s.slug in EX:
            s.move(*EX[s.slug])
