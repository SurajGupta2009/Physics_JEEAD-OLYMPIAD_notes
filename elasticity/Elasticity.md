---
title: Elasticity & Properties of Matter
part: 12
slug: elasticity
source: Cengage MECHANICS 2-compressed.pdf, ch 4 Properties of Solids and Fluids — elasticity half (pp. 4.1-4.19)
aliases: [elasticity, stress strain, youngs modulus, hooke, bending, torsion]
tags: [jee-advanced, olympiad, mechanics, elasticity]
---

# Elasticity & Properties of Matter — first principles to Olympiad

> [!abstract] How to use this chapter
> Three passes. Pass 1: Parts 0–4 — stress and strain as bookkeeping, Hooke's law as the small-strain theorem, the three moduli and their interrelations, the elongation family, thermal stress, torsion, energy and bending. Pass 2: Parts 5–9 for exam craft. Pass 3: Parts 10–14 — the Olympiad layer (the atomic-spring derivation of $Y$, the constant-stress rod, the integrated cantilever, buckling, hoop stress, seismic wave speeds), the paper, the sheet, the checkpoint. Every number recomputed; every boxed result carries its validity condition.

## Part 0 · Orientation

### 0.1 What you will be able to do

After this chapter you can: write stress and strain for tension, compression, volume change and shear, and say why engineers use stress rather than force; read a stress–strain curve as design information (proportional limit, elastic limit, yield, ultimate, fracture; ductile vs brittle); define $Y$, $B$, $G$ by their experiments and derive the two interrelations $Y=2G(1+\sigma)$ and $Y=3B(1-2\sigma)$ with the bounds $-1<\sigma<0.5$; solve the elongation family (load, self-weight, composite rods, tapered rods, the spring-constant link to [[Simple-harmonic-motion|PART 10]]); run thermal-stress problems by the expand-then-compress method; use torsion ($\theta=TL/GJ$) and the torsion pendulum; compute elastic energy densities and the suddenly-applied-load factor 2; analyse a falling weight on a wire by energy and by force; argue the neutral axis and the $M=EI/R$ curvature law, state cantilever and beam deflections and explain the I-beam; and derive $Y$ itself from the interatomic potential, recovering the order $10^{11}$ Pa.

### 0.2 The one idea

Elasticity is the macroscopic face of the interatomic spring: moduli are material properties, stiffness is geometry.

### 0.3 Prerequisite self-check

1. Can you take a force balance on an element and pass to a differential equation? ([[Fluid-mechanics#Part 3 · Core derivations|fluids §3]] does the same move for pressure.)
2. Can you integrate a linearly varying load to a resultant and its line of action? ([[Centre-of-mass-momentum#Part 2 · Definitions and bookkeeping|COM §2]])
3. Do you know the work–energy theorem with a spring force, $W_{spring}=-\tfrac12kx^2$? ([[Work-energy-power#Part 3 · Core derivations|WEP §3]])
4. Can you use $T=2\pi\sqrt{I/C}$ for a torsional oscillator? ([[Simple-harmonic-motion#Part 3 · Core derivations|SHM §3]])
5. Can you estimate with powers of ten and check a limit without being asked? ([[Units-measurements#Part 10 · Olympiad extension|units §10]])

### 0.4 Numbers to keep

| quantity | value | where it bites |
|---|---|---|
| $Y_{\text{steel}}$ | $2.0\times10^{11}$ Pa | wires, rails, cables |
| $Y_{\text{Al}}$ | $7.0\times10^{10}$ Pa | light structures |
| $Y_{\text{Cu}}$ | $1.1\times10^{11}$ Pa | mixed-metal problems |
| $G_{\text{steel}}$ | $8.0\times10^{10}$ Pa | torsion |
| $\sigma_{\text{steel}}$ | $\approx0.29$ | interrelations |
| $\sigma_{\text{rubber}}$ | $\approx0.5$ | incompressible |
| $\alpha_{\text{steel}}$ | $1.2\times10^{-5}$ K$^{-1}$ | thermal stress |
| elastic limit, mild steel | $\sim2.5\times10^8$ Pa | design stress |
| $U''$ estimate | $Y\sim D/r_0^3$, $D\sim$ a few eV, $r_0\sim2$ Å | OL1 |
| sound in steel rod | $\sqrt{Y/\rho}\approx5.1$ km/s | OL10 |

### 0.5 What this chapter is not

Not continuum mechanics with tensors: stress enters as force per area on a named plane, in the four classical modes. Not materials science: dislocations, creep mechanisms and fracture mechanics are named at the frontier (§3.11, §10.1) but not developed. The *fluid* half of the same Cengage chapter (viscosity, surface tension, capillarity) is [[Fluid-mechanics|PART 11]]'s; this chapter owns pp. 4.1–4.19 of *Mechanics II* ch 4.

### 0.6 Cengage coverage map

Floor: *Cengage Mechanics II*, ch 4 Properties of Solids and Fluids, elasticity half (contents page read from the PDF in this repository; section numbers as printed).

| Cengage section | What it establishes | Where it lives here | Status |
|---|---|---|---|
| Elasticity; elastic behaviour of solids | the phenomenon; recoverable deformation | §1, §3.1 | stated + used |
| Elasticity and plasticity; some definitions; cause of elasticity | elastic vs plastic; the interatomic origin preview | §3.2, §3.11 | stated + used |
| Stress; types of stress | normal and shear stress | §3.1 | derived |
| Strain; types of strain | tensile, volumetric, shear strain | §3.1 | derived |
| Elastic limit | the small-strain theorem's boundary | §3.2 | stated + used |
| Hooke's law and elastic moduli | $Y$, $B$, $G$ by experiment | §3.2 | derived |
| Types of modulus of elasticity | which mode each modulus owns | §3.2, §4 ledger | stated + used |
| Analogy of rod as a spring | $k=YA/L$ | §3.4 | derived |
| Bars of composite section | series/parallel rods | §3.4 | derived |
| Stress–strain diagram | landmarks; ductile vs brittle | §3.2 | stated + used |
| Elastic aftereffect; elastic fatigue | time-dependent recovery; cyclic failure | §3.11 | stated + used |
| Energy stored in a deformed body; wire or rod | $U=\tfrac12$ stress × strain × volume | §3.9 | derived |
| Interatomic force constant | $k_a=U''(r_0)$; the microscopic spring | §3.11, OL1 | derived |
| *(syllabus sweep, no own heading in this volume)* Poisson's ratio and the interrelations | $\sigma$; $Y=2G(1+\sigma)$; $Y=3B(1-2\sigma)$ | §3.3 | extended beyond book |
| *(syllabus sweep)* thermal stress | constrained expansion | §3.6 | extended beyond book |
| *(syllabus sweep)* torsion and bending | $\theta=TL/GJ$; $M=EI/R$; cantilever | §3.8, §3.10 | extended beyond book |
| *(syllabus sweep)* buckling, hoop stress, seismic speeds | design limits | §3.12, OL6, OL10 | extended beyond book |
| Solved examples; exercise families | problem shapes | Parts 5–6, 11 | extended beyond book |

> [!quote] Hand-off
> The bulk modulus and the sound-speed link $\sqrt{B/\rho}$ were used in [[Fluid-mechanics#Part 3 · Core derivations|fluids §3.13]] from the liquid side; here they belong to the solid's volume mode (§3.7) and to the seismic pair (OL10). Thermal *expansion coefficients* as phenomena live in [[Heat|the shipped heat note]]; this chapter only uses $\alpha$ to build thermal stress.

## Part 1 · Intuition first

**A solid is a lattice of springs you cannot see.** Pull a steel wire and every interatomic bond along it stretches by a fraction of an angstrom; the wire's stiffness is the sum of billions of bond-stiffnesses in series and parallel. That is why doubling the length halves the stiffness (twice as many springs in series) and doubling the area doubles it (twice as many in parallel) — the whole of $k=YA/L$ is already in that picture, before any algebra.

**Stress is force democratised.** A cable holding a lift cares not that the force is $10^4$ N but that each bond carries its share: the same force through a thinner cable is more stress, and materials fail at a *stress*, never at a force. Strain is the honest counterpart: a dimensionless report of how much every bond stretched. Hooke's law says that for small reports, stress and strain are proportional — the straight line at the left of every curve, the small-angle approximation of the interatomic potential.

**Three ways to deform, three moduli.** Stretch a rod (shape change at fixed volume, mostly): $Y$. Squeeze a block from all sides (volume change at fixed shape): $B$. Slide a deck of cards (shape change at fixed volume): $G$. A rubber eraser under your thumb does all three at once; the interrelations of §3.3 are precisely the bookkeeping that splits one deformation into its volume part and its shear part.

**Geometry fights or helps the material.** An I-beam puts its metal far from the neutral axis because bending strains grow linearly with that distance — the same material, rearranged, carries five times the load. A hollow shaft does the same trick for torsion. And a column fails not by crushing but by *buckling*, a geometric instability: elasticity's most dangerous surprise is that strength can be irrelevant.

> [!tip] Insight
> One length scale decides again, as in fluids but inverted: here the *sample's* dimensions ($L$, $A$, $I$) convert material constants into stiffnesses. Material says $Y$; geometry says $L/A$; the product is the spring. Every trap in this chapter confuses the two.

## Part 2 · Definitions and bookkeeping

| symbol | meaning | SI unit |
|---|---|---|
| $\sigma_{n}$ (or $s$) | normal stress $F/A$ | Pa |
| $\tau$ | shear stress | Pa |
| $\varepsilon$ | tensile strain $\Delta L/L$ | dimensionless |
| $\theta_v$ | volumetric strain $\Delta V/V$ | dimensionless |
| $\gamma$ | shear strain (angle) | rad |
| $Y$ | Young's modulus | Pa |
| $B$ | bulk modulus; compressibility $=1/B$ | Pa |
| $G$ | shear (rigidity) modulus | Pa |
| $\sigma$ | Poisson's ratio $-\varepsilon_{lat}/\varepsilon_{long}$ | dimensionless |
| $I$ | second moment of area (bending) | m$^4$ |
| $J$ | polar second moment (torsion) | m$^4$ |
| $M$ | bending moment | N·m |
| $T$ | torque in torsion | N·m |

> [!note] Definition
> **Stress** is internal force per area on a plane inside the material; **strain** is the resulting dimensionless deformation. Hooke's regime is the range where each strain component is linear in each stress component; the moduli are the slopes.

**Sign conventions, fixed once.** Tensile stress and strain positive; compressive negative; a temperature rise $\Delta T>0$ produces compressive thermal stress when expansion is prevented. Poisson's ratio is written $-\varepsilon_{lat}/\varepsilon_{long}$ so that $\sigma>0$ for ordinary materials. In bending, $y$ is measured from the neutral axis, tension on the convex side.

**Standing assumptions.** (1) *Homogeneous, isotropic* material unless flagged; (2) *small strain* ($\varepsilon\lesssim10^{-3}$ for metals in the linear range) so geometry does not change under load; (3) *static or quasi-static* loading except the impact problems of §3.9, which are energy methods in disguise; (4) *Saint-Venant's principle* silently used: stress distributions become uniform a few widths away from the load point — stated once here, used everywhere.

> [!warning] Condition of validity
> Hooke's law is a *small-strain* theorem. "Linear up to the proportional limit" is the validity statement; past yield the same symbols mean different physics (§3.2, §3.11).

**What is not in this model.** Anisotropy (wood, composites), large-strain rubber elasticity (entropy springs — a different mechanism, named in §3.11), viscoelastic time effects beyond naming, and fracture mechanics beyond the curve's landmarks.

> [!abstract] DIAGRAM D12.1 · The stress–strain curve with all six landmarks
> *Show:* stress vertical, strain horizontal; the straight Hooke line to the proportional limit P; elastic limit E just beyond; yield Y with the small plateau; ultimate U at the top; fracture F after the necking drop; a brittle material's steep curve ending at fracture drawn dashed beside it; the elastic area shaded as recoverable energy.
> *Search:* "stress strain curve proportional limit yield ultimate fracture ductile brittle"
> *Used in:* §3.2 and Q4.

## Part 3 · Core derivations

### 3.1 Stress and strain: the four modes

Cut an imaginary plane through a loaded body; the internal force per area transmitted across it, resolved normal and tangential, is **normal stress** $\sigma_n=F_\perp/A$ and **shear stress** $\tau=F_\parallel/A$. The corresponding bookkeepings: tensile strain $\varepsilon=\Delta L/L$; volumetric strain $\Delta V/V$; shear strain $\gamma$ = the angle (in radians) by which a right angle distorts.

> [!info] Why stress, not force
> Failure and deformation are local: a bond stretches by the force *per bond chain*, i.e. per area. Two cables of different thickness carrying the same force are in different physical states; same stress, same state. That is the entire argument — and the reason allowable loads scale with area.

Strain is dimensionless, which is why all moduli carry pascal units and why a strain gauge is a ruler, not a scale.

### 3.2 Hooke's law, the three moduli, and the curve's landmarks

In the linear range, each mode obeys its own proportionality, defined by its experiment:

$$
Y=\frac{\sigma_n}{\varepsilon}=\frac{F/A}{\Delta L/L},\qquad B=-\frac{\Delta p}{\Delta V/V},\qquad G=\frac{\tau}{\gamma}. \qquad (3.1)
$$

The minus in $B$ keeps it positive (pressure up, volume down). The **stress–strain curve** of mild steel (D12.1) records, in order: proportional limit (Hooke dies), elastic limit (recovery dies), yield (strain runs at constant stress), ultimate strength (necking begins), fracture. Ductile materials draw this full story; brittle ones snap shortly after the elastic limit — the curve is read as *design information*: working stress is the yield divided by a safety factor, never the ultimate.

> [!warning] Condition of validity
> "Modulus is a material property" means: independent of $L$, $A$, and load — *within the linear range and for one temperature*. It does not mean the material is linear, nor that stiffness is a material property (stiffness carries geometry, §3.4).

### 3.3 Poisson's ratio and the two interrelations

Stretch a rod: it thins. $\sigma=-\varepsilon_{lat}/\varepsilon_{long}$. The bounds are the demand that both $B$ and $G$ stay positive in the relations below, which forces $-1<\sigma<\tfrac12$. At $\sigma=\tfrac12$ the volume does not change (rubber, nearly); $\sigma<0$ (auxetics) means the material thickens when stretched — geometrically possible and energetically allowed, just uncommon.

**Derive $Y=3B(1-2\sigma)$.** Apply hydrostatic pressure $p$: each of three equal principal stresses $-p$ produces strain $\varepsilon_1=-p/Y$ directly plus $+\sigma p/Y$ from each of the other two axes: $\varepsilon_1=-(p/Y)(1-2\sigma)$. Volume strain is thrice that: $\Delta V/V=-3p(1-2\sigma)/Y$. But $\Delta V/V=-p/B$ by definition; equate: $Y=3B(1-2\sigma)$.

**Derive $Y=2G(1+\sigma)$.** Pure shear $\tau$ on a square is, rotated $45^\circ$, tension $\tau$ on one diagonal and compression $\tau$ on the other. The diagonal's strain from those normal stresses is $(\tau/Y)(1+\sigma)$; geometrically the diagonal strain equals $\gamma/2$ with $\gamma=\tau/G$. So $\tau/(2G)=(\tau/Y)(1+\sigma)$, giving $Y=2G(1+\sigma)$.

> [!info] Why
> Both derivations are the same theorem — superposition of principal strains — applied to the two invariant ways of loading. Knowing any two of $Y,B,G,\sigma$ fixes all four: two constants describe an isotropic linear solid.

> [!success] Check
> $\sigma\to1/2$ forces $B\to\infty$ at finite $Y$: the solid may still be stretched, but it cannot change volume. Rubber sits here. Steel at $\sigma=0.29$: $B=Y/[3(1-2\times0.29)]=1.59\times10^{11}$ Pa, the tabulated order ✓.

> [!abstract] DIAGRAM D12.2 · The three modulus geometries
> *Show:* three panels: a wire under $F$ with $\Delta L$ and the lateral necking arrows; a cube under all-face pressure $p$ with the shrunken dashed cube; a block under opposing tangential forces with the skewed dashed outline and angle $\gamma$; each labelled with its modulus and its strain.
> *Search:* "young bulk shear modulus deformation diagrams tension compression shear"

### 3.4 Extension problems I: the spring constant of a rod

A rod of length $L$, area $A$, modulus $Y$ under force $F$: $\Delta L=FL/(AY)$. Rewrite as $F=(YA/L)\Delta L$:

$$
k=\frac{YA}{L}. \qquad (3.2)
$$

Series rods (same $F$, extensions add): $1/k=\sum1/k_i$; parallel rods (same $\Delta L$, forces add): $k=\sum k_i$ — the exact [[Simple-harmonic-motion#Part 3 · Core derivations|SHM spring machinery]] now applies to wires, including cutting a wire into $n$ pieces ($k\to nk$).

**Composite rod, equal force branch.** Steel ($L_1,A_1,Y_1$) welded to copper ($L_2,A_2,Y_2$) in line under $F$: same $F$ through both, $\Delta L=F(L_1/A_1Y_1+L_2/A_2Y_2)$; the stress is larger where $A$ is smaller — draw the stress distribution (D12.3), it is the picture that prevents the classic error.

**Two wires sharing a load (parallel branch).** A rigid bar hung from two wires of different $Y,A$: the load splits so that *extensions match the bar's constraint* (equal for a level bar): $F_1/F_2=k_1/k_2$ — the stiffer wire carries more.

> [!abstract] DIAGRAM D12.3 · Composite rod in series, with the stress distribution
> *Show:* two segments of different thickness joined end to end under $F$; arrows of equal $F$ through both; a side bar chart of stress $\sigma=F/A$ tall in the thin segment, short in the thick one; extensions labelled $\Delta L_i=FL_i/A_iY_i$.
> *Search:* "composite rod series stress distribution different cross sections"

### 3.5 Extension problems II: self weight and taper

A hanging rod carries, at height $x$ from the free bottom, the weight of the material below, $F(x)=\rho A g x$. The element $dx$ stretches by $F(x)dx/(AY)$:

$$
\Delta L=\int_0^L\frac{\rho g x}{Y}dx=\frac{\rho g L^2}{2Y}=\frac{(mg/2)L}{AY}. \qquad (3.3)
$$

The rod stretches as if half its weight hung at the end — because the load ramps linearly from zero to $mg$. For a cone or any $A(x)$: $\Delta L=\int F(x)dx/(A(x)Y)$; the integrand's $A$-dependence is the only new ingredient.

> [!danger] Trap
> "Self-weight extension uses the full weight" is wrong by exactly 2: the integral of $x$ is $L^2/2$, not $L^2$. If your answer equals the end-load formula with $mg$, you averaged where you should have integrated.

### 3.6 Thermal stress: expand free, then compress back

A rod between rigid walls, heated by $\Delta T$. Left free it would grow $\alpha L\Delta T$; the walls push it back by force $F$ producing $\Delta L=-FL/AY$. Net change zero: $FL/AY=\alpha L\Delta T$, so

$$
\sigma_{th}=Y\alpha\Delta T,\qquad F=Y\alpha\Delta T\,A. \qquad (3.4)
$$

Notice $L$ cancels: a short rail and a long rail develop the *same stress* for the same $\Delta T$ — geometry enters only through $A$. Steel, $\Delta T=30$ K: $\sigma=2\times10^{11}\times1.2\times10^{-5}\times30=7.2\times10^7$ Pa — a third of yield: expansion gaps and sleepers are not optional. Two-material composite bars use the same two-step method with a compatibility condition (equal final lengths) replacing "net zero".

> [!abstract] DIAGRAM D12.4 · Thermal stress: free expansion versus forced length
> *Show:* top: rod with gap $\alpha L\Delta T$ shown by dashed outline; bottom: the same rod between hatched walls with the reaction arrows $F$ and the label "compress back by $\alpha L\Delta T$"; a rail track with expansion gaps as inset.
> *Search:* "thermal stress rod between rigid walls expansion gap diagram"
> *Used in:* §3.6 and Q9.

### 3.7 Bulk modulus, compressibility, and the density at depth

$B=-\Delta p/(\Delta V/V)$. Gases have tiny $B$ (which is why they are excluded from elasticity tables: their "modulus" depends on the process — isothermal $B=p$, adiabatic $B=\gamma p$, a thermodynamics hand-off to [[Thermodynamics#Part 3 · Core derivations|thermodynamics]]). Water: $B=2.2\times10^9$ Pa; at depth $d$, $\Delta p=\rho g d$ and the fractional volume shrink is $\rho g d/B$; density rises by the same fraction:

$$
\rho(d)\approx\rho_0\left(1+\frac{\rho_0 g d}{B}\right). \qquad (3.5)
$$

At $d=4$ km: $\rho g d/B=1000\times9.8\times4000/2.2\times10^9=0.018$: water is 1.8% denser — small, nonzero, and the reason "incompressible" is always a flagged idealisation. The sound-speed link $v=\sqrt{B/\rho}$ hands the liquid side to [[Sound-waves|sound waves]]; the solid side returns in OL10.

### 3.8 Shear and torsion

A shaft of radius $R$, length $L$, twisted by torque $T$: a cylindrical shell at $r$ shears by angle $\gamma=r\theta/L$ (twist $\theta$ over $L$), stress $\tau=G r\theta/L$, and its torque contribution $\tau\cdot2\pi r\,dr\cdot r$ integrates to

$$
T=\frac{G\theta}{L}\int_0^R2\pi r^3dr=\frac{G\theta}{L}\frac{\pi R^4}{2}\quad\Rightarrow\quad \theta=\frac{TL}{GJ},\ J=\frac{\pi R^4}{2}. \qquad (3.6)
$$

The torsion pendulum is this spring: $C=T/\theta=GJ/L$, period $2\pi\sqrt{I/C}$ — the SHM hand-off. **Hollow vs solid at equal mass:** removing the core removes little $J$ (integrand $\propto r^3$) but much area; per kilogram the hollow shaft is stiffer — the same "put material far from the axis" principle as bending.

> [!abstract] DIAGRAM D12.5 · Twisted rod: shear strain, angle of twist, hollow vs solid
> *Show:* a shaft with a longitudinal line helixed by $\theta$; the surface element square skewed by $\gamma=R\theta/L$; the $r^3$ weighting drawn as a shaded ring; side-by-side hollow and solid sections of equal area with $J/A$ compared.
> *Search:* "torsion of shaft angle of twist shear strain derivation hollow solid"

### 3.9 Elastic energy, the factor 2, and the falling weight

Stretch a wire quasi-statically: $dU=F\,d(\Delta)=k x\,dx$, so $U=\tfrac12k\Delta^2=\tfrac12F\Delta$. In densities, $u=\tfrac12\sigma\varepsilon$ (tension), $\tfrac12\tau\gamma$ (shear), $\tfrac12B(\Delta V/V)^2$ (volume):

$$
u=\tfrac12\times\text{stress}\times\text{strain}. \qquad (3.7)
$$

**Suddenly applied load.** Hang $mg$ with no gradual release: the wire overshoots to the extension where stored energy equals lost potential, $mg\Delta=\tfrac12k\Delta^2$, i.e. $\Delta=2mg/k$ — *twice* the static extension and *twice* the static stress. Dynamic loading is a factor-2 event; cranes lower loads, they do not drop them.

**Weight dropped from height $h$.** Energy: $mg(h+\Delta)=\tfrac12k\Delta^2$; solve the quadratic: $\Delta=\frac{mg}{k}\left(1+\sqrt{1+2hk/mg}\right)$; for $h\gg\Delta_{st}$: $\Delta\approx\sqrt{2hmg/k}$, and the peak force $F_{max}=k\Delta=\sqrt{2hmgk}$ grows as $\sqrt{k}$ — a *stiffer* wire shocks harder, the counter-intuitive design lesson of the family.

> [!info] Why
> The force method (balance at maximum extension with an effective static equation) and the energy method agree because at maximum extension the kinetic energy is zero; energy is the cleaner route because the intermediate dynamics are irrelevant.

> [!abstract] DIAGRAM D12.6 · Falling weight on a wire: the F–x intersection
> *Show:* the wire's line $F=kx$ and the weight's constant line $mg$ with the energy areas shaded: rectangle $mg(h+\Delta)$ equals triangle $\tfrac12k\Delta^2$; the static point $mg/k$ and the dynamic point $\Delta$ marked; the factor-2 case $h=0$ inset.
> *Search:* "weight falling on wire maximum extension energy method diagram"
> *Used in:* §3.9 and E7.

### 3.10 Bending: neutral axis, curvature, and the cantilever

A beam bent into an arc of radius $R$: fibres at distance $y$ from the **neutral axis** (the unstretched layer) change length by $y/R$, so strain $=y/R$ and stress $=Yy/R$ — linear across the section, tension one side, compression the other. The neutral axis passes through the centroid for a homogeneous section (the axial force must vanish: $\int y\,dA=0$). The internal moment is

$$
M=\int\frac{Yy^2}{R}dA=\frac{YI}{R}\quad\Rightarrow\quad \frac{M}{I}=\frac{Y}{R}. \qquad (3.8)
$$

Curvature proportional to moment: the beam equation. **Cantilever, end load $F$.** $M(x)=F(L-x)$; with small slopes $d^2y/dx^2=M/(YI)$; integrate twice with $y(0)=y'(0)=0$:

$$
\delta_{end}=\frac{FL^3}{3YI}. \qquad (3.9)
$$

Simply supported, central load: $\delta=FL^3/(48YI)$. **Why the I-beam:** $I=\int y^2dA$ rewards material far from the axis; moving the same area from a square to an I-profile multiplies $I$ (and the load capacity) several times at unchanged mass — the worked comparison is OL7.

> [!abstract] DIAGRAM D12.7 · Neutral axis and fibre strains in bending
> *Show:* a bent beam segment with the neutral axis dashed; top fibres compressed (arrows inward), bottom stretched; the linear stress diagram across the depth drawn beside it, crossing zero at the neutral axis; the arc radius $R$ indicated.
> *Search:* "bending beam neutral axis stress distribution linear diagram"

> [!abstract] DIAGRAM D12.8 · Cantilever deflection curve and the I-beam comparison
> *Show:* left: cantilever with end load $F$, the deflected curve, $\delta=FL^3/3YI$ labelled, moment diagram triangle beneath; right: square versus I section of equal area with $I$ values compared and the arrow "same metal, five times stiffer".
> *Search:* "cantilever beam end load deflection I-beam cross section comparison"

### 3.11 Beyond the linear law: plasticity, fatigue, and the atomic spring

Past yield, dislocations move and the deformation becomes permanent; **elastic aftereffect** is the slow partial recovery; **elastic fatigue** is the progressive weakening under repeated loading — a paperclip snaps after a dozen bends at stresses far below yield, because each cycle grows a microcrack (named, not developed: fracture mechanics is the frontier).

**The atomic derivation of $Y$.** Model neighbours by a pair potential $U(r)$ with minimum at $r_0$. A chain of atoms under force $F$: each bond stretches by $s$, and $F=U''(r_0)s$ to first order. The rod's stress is $F$ per bond-chain area $\sim r_0^2$, strain is $s/r_0$:

$$
Y=\frac{F/r_0^2}{s/r_0}=\frac{U''(r_0)}{r_0}. \qquad (3.10)
$$

Estimate with bond energy $D\sim3$ eV and $U''\sim D/r_0^2$: $Y\sim D/r_0^3=3\times1.6\times10^{-19}/(8\times10^{-30})=6\times10^{10}$ Pa — the right *order* for solids, $10^{10}$–$10^{11}$ Pa, from two atomic numbers. This is the chapter's central order-of-magnitude fact: every solid's stiffness is its bond energy per atomic volume.

**Why steel is stiffer than rubber by $10^5$.** Rubber's elasticity is entropic (coiled chains straightening — a thermodynamic spring, $Y\propto T$), not energetic. The interatomic spring just derived is not its mechanism. Named here as the model's boundary.

**Thermal expansion from the well's asymmetry.** A symmetric well would give $\langle r\rangle=r_0$ at every temperature. The real well is softer outward, so the mean separation drifts as the amplitude grows. OL2 derives $\alpha=-\gamma k_B/(2r_0 k^2)$ and the estimate $\alpha\sim k_B/(2D)\sim10^{-5}$ K$^{-1}$, and notes that $\alpha B$ is roughly $k_B$ per atomic volume. The asymmetry that expands a rail is the same asymmetry §3.6 has to fight — the hand-off to [[Heat|heat]] made explicit.

### 3.12 Choosing materials: specific modulus, buckling preview, one design

Strength (yield stress), stiffness ($Y$), toughness (area under the curve), density ($\rho$) are independent axes. For a light stiff tie, maximise $Y/\rho$ (specific modulus): steel and aluminium roughly tie, and a carbon-fibre composite beats both. For a light stiff beam, maximise $Y^{1/2}/\rho$ (from $\delta\propto FL^3/YI$ at fixed mass), where aluminium does pull ahead of steel. For a column, the failure is often buckling, $P_{cr}=\pi^2YI/L^2$ (OL6), which punishes long thin members regardless of strength. The design exemplar E10 closes the section: a crane cable chooses strength over density; a bicycle frame chooses $Y^{1/2}/\rho$ and joint behaviour.

> [!abstract] DIAGRAM D12.9 · The interatomic potential well and its linear region
> *Show:* $U(r)$ with minimum at $r_0$, depth $D$; the parabolic fit over the small-strain region shaded; the asymmetry beyond it highlighted with the arrow "thermal expansion lives here"; the slope $U''(r_0)$ labelled as the bond spring.
> *Search:* "interatomic potential curve asymmetric thermal expansion young modulus bond"

> [!abstract] DIAGRAM D12.10 · Material property chart, Ashby style
> *Show:* log-log plot of $Y$ versus $\rho$ with metals, ceramics, polymers, foams as labelled blobs; guide lines of slope 1 for $Y/\rho$ (ties) and slope 2 for $Y^{1/2}/\rho$ (beams); steel, aluminium, CFRP, rubber marked with dots.
> *Search:* "Ashby chart young modulus density materials selection guide lines"

## Part 4 · Results, limits and the validity ledger

| result | formula | validity | limit check |
|---|---|---|---|
| Hooke, tension | $\sigma=Y\varepsilon$ | below proportional limit | $\varepsilon\to0$ trivial |
| rod spring | $k=YA/L$ | linear, uniform | $L\to2L\Rightarrow k/2$ |
| self-weight | $\Delta L=\rho gL^2/2Y$ | uniform rod | equals half the end-load value |
| thermal stress | $\sigma=Y\alpha\Delta T$ | fully constrained, linear | $A$ cancels ✓ |
| Poisson bounds | $-1<\sigma<0.5$ | $B,G>0$ | rubber $0.5$ |
| interrelations | $Y=2G(1+\sigma)=3B(1-2\sigma)$ | isotropic linear | $\sigma=0.5\Rightarrow B\to\infty$ |
| torsion | $\theta=TL/GJ$ | circular section, linear | $R\to2R$: $\theta/16$ |
| energy density | $u=\tfrac12\sigma\varepsilon$ | linear | area of triangle |
| sudden load | stress $\times2$ | no damping | $h=0$ case |
| drop load | $\Delta=\Delta_{st}(1+\sqrt{1+2h/\Delta_{st}})$ | energy method | $h\to0\Rightarrow2\Delta_{st}$ |
| bending | $M=YI/R$; $\delta=FL^3/3YI$ (cantilever) | small slope, linear | $I\to\infty\Rightarrow0$ |
| buckling | $P_{cr}=\pi^2YI/L^2$ | pinned ends, elastic | $L\to2L$: $P/4$ |
| hoop stress | $\sigma=pr/t$ | thin wall | $t\to2t$: $\sigma/2$ |
| atomic | $Y\sim D/r_0^3$ | pair potential | eV/Å$^3\sim10^{11}$ Pa |

**Which modulus when.** Pull/bend a slender member: $Y$. Squeeze a volume: $B$. Twist or shear: $G$. Mixed states: decompose with §3.3.

> [!danger] Trap
> Strength and stiffness are different axes: a nylon rope is stiff enough to tow but never to hold a precision frame; glass is stiffer than nylon but shatters at its strength. The ledger rows carry the distinction.

## Part 5 · Worked exemplars

**C1 — concept check.** Two steel wires carry the same load. One has twice the cross-section of the other. Which is closer to breaking, and why does the answer not mention the lengths?

<details><summary>Solution</summary>

The thinner one: failure is a stress, $\sigma=F/A$, and $A$ is the only difference. Length changes the extension, not the stress, in a uniform wire under an end load.

</details>

**C2 — concept check.** A stress–strain curve for mild steel and one for glass are laid over each other. Glass has the steeper initial slope and no yield plateau. Which is stiffer, which is tougher, and which would you choose for a cable that must not snap without warning?

<details><summary>Solution</summary>

Glass is stiffer (larger $Y$). Mild steel is tougher: the area under its curve, out to fracture, is far larger. The cable wants the steel — a brittle snap gives no warning, a yielding cable stretches first.

</details>

**C3 — concept check.** Why can Poisson's ratio of a stable isotropic solid not be $0.6$?

<details><summary>Solution</summary>

$Y=3B(1-2\sigma)$ would then make $B$ negative: the solid would expand when squeezed, and the energy would be unbounded below. The bound $\sigma<\tfrac12$ is an energy demand, not a convention.

</details>

**C4 — concept check.** A steel rod and a copper rod are welded end to end and pulled. A second pair, of the same rods, hang side by side from a rigid bar and share a load. In which arrangement are the stresses equal, and in which are the extensions equal?

<details><summary>Solution</summary>

End to end (series): the force is common, so the stresses are equal only if the areas are equal; the extensions add and are generally unequal. Side by side under a rigid bar (parallel): the extension is common, and the stiffer rod carries the larger share of the force.

</details>

**C5 — concept check.** A uniform hanging rod stretches by $1$ mm under its own weight. An equal load is now hung at its end and the self-weight is imagined removed. What is the new extension?

<details><summary>Solution</summary>

$2$ mm. Self-weight is equivalent to half the weight hung at the end, because the axial force ramps from zero at the free end to $mg$ at the support. Full end-load uses the whole weight at every section.

</details>

**C6 — concept check.** A short steel bolt and a long steel rail are both fully constrained and both heated by $30$ K. Compare their stresses and their would-be free expansions.

<details><summary>Solution</summary>

The stresses are equal: $\sigma=Y\alpha\Delta T$ does not contain $L$. The free expansions are not: $\Delta L=\alpha L\Delta T$ scales with length. Stress is local; expansion is extensive.

</details>

**C7 — concept check.** A load is lowered gently onto a wire, then the experiment is repeated by releasing the same load from zero height (a sudden application). Compare the peak extensions.

<details><summary>Solution</summary>

The sudden case peaks at twice the static extension. Energy: $mg\Delta=\tfrac12 k\Delta^2$ has the root $\Delta=2mg/k$, whereas static balance is $mg=k\Delta$.

</details>

**C8 — concept check.** For a drop from a height large compared with the static extension, a stiffer wire develops a larger peak force. Why is that not a reason to choose the stiffest wire available?

<details><summary>Solution</summary>

$F_{max}\approx\sqrt{2hmgk}$ grows as $\sqrt{k}$. The stiff wire shocks harder; what you want is a wire whose peak *stress* stays under yield, which is a competition between $k=YA/L$ and the area that stress is reckoned on. Stiffness is not strength.

</details>

**C9 — concept check.** A beam is half steel and half aluminium, bonded along its length, and bent. Is the neutral axis at the geometric mid-depth?

<details><summary>Solution</summary>

No. The neutral axis is where the axial force vanishes, $\int \sigma\,dA=0$. Steel carries more stress at the same strain, so the axis shifts toward the steel. Only a homogeneous section puts it at the centroid.

</details>

**C10 — concept check.** A hollow shaft and a solid shaft have the same mass, length and material, and carry the same torque. Which twists more?

<details><summary>Solution</summary>

The solid one. $J=\int r^2\,dA$ weights area by $r^2$; moving material outward raises $J$ at fixed area, so the hollow shaft has the larger torsional stiffness $GJ/L$.

</details>

**C11 — concept check.** Rubber has $\sigma\approx0.5$ and a Young's modulus five orders below steel's. Which of those two facts tells you rubber is nearly incompressible, and which tells you it is not an interatomic spring?

<details><summary>Solution</summary>

$\sigma\approx\tfrac12$ is the incompressible limit ($B\to\infty$ at finite $Y$). The factor $10^5$ in $Y$ is the mechanism: rubber's restoring force is the entropy of coiled chains, not the curvature of a bond well, so the atomic estimate of §3.11 does not apply to it.

</details>

**C12 — concept check.** A long thin column and a short fat one are cut from the same bar. One fails by crushing, one by buckling. Which is which, and which failure load depends on $Y$?

<details><summary>Solution</summary>

The short fat one crushes, at a load $\sigma_y A$ set by strength, independent of $Y$. The long thin one buckles, at $P_{cr}=\pi^2 YI/L^2$, which depends on stiffness and on $L^2$ and not on strength at all.

</details>

> [!abstract] DIAGRAM D12.11 · Poisson contraction of a pulled wire
> *Show:* a wire before and after loading; longitudinal arrows $\Delta L$; a cross-section inset with the original radius dashed and the contracted radius solid, labelled $\Delta r=-\sigma r\,\Delta L/L$; a note that the fractional volume change is $(1-2\sigma)\Delta L/L$.
> *Search:* "poisson ratio lateral contraction wire diagram"

> [!abstract] DIAGRAM D12.12 · Element of a rod under its own weight
> *Show:* a hanging rod, origin at the free lower end; an element $dx$ at height $x$ carrying the weight $\rho A g x$ of everything below it; the local extension $d(\Delta)=\rho g x\,dx/Y$ written beside the element; the triangular load diagram from $0$ to $mg$.
> *Search:* "elongation of rod under own weight element diagram"

> [!abstract] DIAGRAM D12.13 · Density of seawater against depth
> *Show:* $\rho(d)/\rho_0$ from the surface to $10$ km; the straight line $1+\rho_0 g d/B$ with $B=2.2\times10^9$ Pa; the $4$ km point marked at $+1.8\%$; a dashed curve showing where the linear compressibility would itself need a correction.
> *Search:* "seawater density increase with depth compressibility graph"

### E1 — Extension, stress, and the breaking load

A steel wire, $L=2.0$ m, diameter $1.0$ mm, $Y=2.0\times10^{11}$ Pa, carries $100$ N. Find the extension and the stress, and the greatest load if the breaking stress is $4.0\times10^8$ Pa.

<details><summary>Solution</summary>

$A=\pi(0.5\times10^{-3})^2=7.85\times10^{-7}$ m$^2$. Extension $\Delta L=FL/(AY)=100\times2.0/(7.85\times10^{-7}\times2.0\times10^{11})=1.27\times10^{-3}$ m $=1.27$ mm. Stress $\sigma=F/A=1.27\times10^8$ Pa. Breaking load $F_{max}=\sigma_b A=4.0\times10^8\times7.85\times10^{-7}=314$ N.

> [!success] Check
> Doubling the diameter at fixed load quarters the stress and the extension; the breaking load quadruples. Both follow from $A$ alone.

</details>

### E2 — Composite rod, both branches

Steel ($L=1.0$ m, $A=1.0$ cm$^2$, $Y=2.0\times10^{11}$) is fastened to copper ($L=1.0$ m, $A=2.0$ cm$^2$, $Y=1.1\times10^{11}$). (a) In series under $2000$ N, find each extension and each stress. (b) The same two rods hang in parallel from a rigid bar and share $2000$ N. Find the load in each.

<details><summary>Solution</summary>

(a) Series, common force. $\Delta L_s=2000\times1.0/(1.0\times10^{-4}\times2.0\times10^{11})=1.00\times10^{-4}$ m. $\Delta L_c=2000/(2.0\times10^{-4}\times1.1\times10^{11})=9.1\times10^{-5}$ m. Total $0.191$ mm. Stresses: steel $2.0\times10^7$ Pa, copper $1.0\times10^7$ Pa — equal forces, unequal areas (D12.3). (b) Parallel, common extension, so loads split as the stiffnesses. $k_s=YA/L=2.0\times10^7$ N/m, $k_c=2.2\times10^7$ N/m. $F_s=2000\times k_s/(k_s+k_c)=952$ N, $F_c=1048$ N. The copper, despite the lower modulus, carries slightly more, because its area more than compensates.

> [!success] Check
> Series limit of identical rods: equal stresses and equal extensions. Parallel limit $k_c\to0$: steel carries everything. Both recovered.

</details>

### E3 — A mine cable under its own weight

A uniform steel cable, $L=100$ m, $\rho=7800$ kg/m$^3$, $Y=2.0\times10^{11}$ Pa, hangs down a shaft. Find its elongation under self-weight, and the extra elongation when a $1.0$ tonne cage hangs at the end (cable area $5.0$ cm$^2$).

<details><summary>Solution</summary>

Self-weight: $\Delta L_1=\rho g L^2/(2Y)=7800\times9.8\times10^4/(4.0\times10^{11})=1.91\times10^{-3}$ m $=1.9$ mm. The cage adds an end load at every section: $\Delta L_2=MgL/(AY)=1000\times9.8\times100/(5.0\times10^{-4}\times2.0\times10^{11})=9.8\times10^{-3}$ m $=9.8$ mm. Total $11.7$ mm. The self-weight piece is the integral of a triangular load; forgetting the $\tfrac12$ would have doubled it, a $1.9$ mm error against a $9.8$ mm signal — small here, dominant for a cable with no cage.

> [!success] Check
> The end-load term is linear in $L$, the self-weight term quadratic, so self-weight wins only for very long cables. Here $L$ would need to exceed $2M/(\rho A)=2\times1000/(7800\times5.0\times10^{-4})=513$ m before self-weight outgrows the cage.

</details>

### E4 — Rail gaps, welded rail, and a quarter-turn of a nut

(a) A free $1.00$ km steel rail ($\alpha=1.2\times10^{-5}$ K$^{-1}$) sees an annual temperature swing of $40$ K. How much does its length change from winter to summer? (b) The same rail is welded continuous and constrained. What compressive stress develops over that swing? (c) A steel bolt of gripped length $20$ cm and pitch $1.0$ mm is tightened by a quarter turn. Estimate the stress.

<details><summary>Solution</summary>

(a) $\Delta L=\alpha L\Delta T=1.2\times10^{-5}\times1000\times40=0.48$ m. A year of daily cycles does not accumulate: the rail breathes by $0.48$ m peak to peak and returns. (b) Constrained, $\sigma=Y\alpha\Delta T=2.0\times10^{11}\times1.2\times10^{-5}\times40=9.6\times10^7$ Pa, about $40\%$ of mild-steel yield — which is why continuous rail is tensioned at a set temperature rather than clamped cold. (c) A quarter turn advances the nut by $0.25$ mm, all of it extension of the gripped length. Strain $=0.25\times10^{-3}/0.20=1.25\times10^{-3}$, stress $=Y\times\text{strain}=2.5\times10^8$ Pa, at yield. One quarter-turn past snug yields a short bolt; torque wrenches exist because pitch converts a small angle into a large strain.

> [!success] Check
> (a) scales with $L$, (b) does not, (c) scales with pitch over gripped length. Heating the bolt after tightening adds a further stress $Y\alpha\Delta T$ if the clamped plates expand less than the bolt.

</details>

### E5 — The two-wire hanger, and the straight wire that sags

(a) A $10$ kg mass hangs from two steel wires, each of length $2.0$ m and area $1.0$ mm$^2$, each at $30^\circ$ to the horizontal, supports fixed. Find the tension and the descent of the mass. (b) The same mass is hung at the midpoint of a single initially straight wire of length $2l=4.0$ m and the same area, fixed at both ends. Find the sag.

<details><summary>Solution</summary>

(a) Vertical balance: $2T\sin30^\circ=mg$, so $T=mg=98$ N — the factor $\tfrac12$ and the sine cancel at $30^\circ$. $\Delta L=TL/(AY)=98\times2.0/(1.0\times10^{-6}\times2.0\times10^{11})=9.8\times10^{-4}$ m. With the supports fixed the angle steepens as the wires stretch, and the descent is $\Delta L/\sin\theta=1.96$ mm. (Holding $\theta$ fixed by sliding the supports would give only $\Delta L\sin\theta$.) (b) Now $\theta$ is not given; the wire makes it. Each half, unstretched length $l=2.0$ m, stretches by $\approx y^2/(2l)$ for a sag $y$. Then $T=YA\,y^2/(2l^2)$, and $2T(y/l)=mg$, which collapses to

$$
y=l\left(\frac{mg}{YA}\right)^{1/3}=2.0\left(\frac{98}{2.0\times10^{5}}\right)^{1/3}=2.0\times0.0788=0.158\text{ m}.
$$

The tension is $T=mgl/(2y)=98\times2.0/(2\times0.158)=620$ N, six times the weight: a nearly flat wire buys its vertical component by a large tension. Using $mg/2$ here would be wrong by that factor.

> [!success] Check
> (a) $\theta\to90^\circ$: $T\to mg/2$, two vertical wires. (b) $y\propto F^{1/3}$, not $F$: doubling the load increases the sag by only $26\%$.

</details>

### E6 — How much the ocean compresses

Estimate the density of seawater at $4.0$ km depth. $B=2.2\times10^9$ Pa, surface density $1025$ kg/m$^3$.

<details><summary>Solution</summary>

Fractional compression $|\Delta V/V|=\rho g d/B$. With $\rho g d=1025\times9.8\times4000=4.02\times10^7$ Pa, $|\Delta V/V|=4.02\times10^7/2.2\times10^9=0.0183$. Density rises by the same fraction: $\rho(d)=1025\times1.0183=1044$ kg/m$^3$. A $1.8\%$ correction — the reason hydrostatics treats water as incompressible for a few atmospheres, and the reason it must not at trench depths (D12.13).

> [!success] Check
> $d\to0$ returns the surface density; doubling $B$ halves the correction. Gases are absent from elasticity tables because their $B$ is the pressure itself and depends on whether the compression is isothermal ($B=p$) or adiabatic ($B=\gamma p$) — a hand-off to [[Thermodynamics|thermodynamics]], not a bigger number in the same column.

</details>

### E7 — A falling weight, energy against force

A steel wire, $L=2.0$ m, $A=1.0$ mm$^2$, $Y=2.0\times10^{11}$ Pa, is fixed at the top. A $2.0$ kg mass falls onto a stop at its lower end from $0.20$ m above the slack position. Find the maximum extension, the peak force, and say whether the wire survives a yield stress of $2.5\times10^8$ Pa.

<details><summary>Solution</summary>

$k=YA/L=2.0\times10^{11}\times1.0\times10^{-6}/2.0=1.0\times10^5$ N/m. Static extension $\Delta_{st}=mg/k=1.96\times10^{-4}$ m. Energy, with the mass descending $h+\Delta$ and the wire storing $\tfrac12 k\Delta^2$:

$$
\Delta=\Delta_{st}\left(1+\sqrt{1+\frac{2h}{\Delta_{st}}}\right)=1.96\times10^{-4}\left(1+\sqrt{2042}\right)=9.06\times10^{-3}\text{ m}.
$$

Peak force $k\Delta=906$ N, against a static $19.6$ N. Peak stress $906/10^{-6}=9.1\times10^8$ Pa, nearly four times yield: the wire does not survive. The energy ledger is the whole story, because at maximum extension the kinetic energy is zero; a free-body diagram at that instant does *not* balance, since the mass is accelerating back up. The trap $mgh=\tfrac12 F\Delta$ with $F$ guessed as $mg$ undercounts the energy by about $h/\Delta_{st}$.

> [!success] Check
> $h\to0$ returns $\Delta=2\Delta_{st}$, the sudden-load result. For $h\gg\Delta_{st}$, $F_{max}\approx\sqrt{2hmgk}=\sqrt{7.84\times10^5}=885$ N, within $3\%$ of $906$ N. A thicker wire lowers the stress faster than it raises the force.

</details>

### E8 — Torsion pendulum, and a rivet in double shear

(a) A disc of moment of inertia $0.020$ kg·m$^2$ hangs from a steel wire, $L=0.50$ m, radius $0.50$ mm, $G=8.0\times10^{10}$ Pa. Find the period. (b) A rivet of diameter $8.0$ mm in double shear must carry $10$ kN. Find the shear stress.

<details><summary>Solution</summary>

(a) $J=\pi R^4/2=\pi(0.50\times10^{-3})^4/2=9.82\times10^{-14}$ m$^4$. Torsional stiffness $C=GJ/L=8.0\times10^{10}\times9.82\times10^{-14}/0.50=1.57\times10^{-2}$ N·m/rad. Period $T=2\pi\sqrt{I/C}=2\pi\sqrt{0.020/0.0157}=7.1$ s. This is the [[Simple-harmonic-motion|SHM]] torsion pendulum with the stiffness now computed from the material. (b) Two shear planes: $\tau=F/(2A)=10000/(2\times\pi\times(4.0\times10^{-3})^2)=9.95\times10^7$ Pa $\approx100$ MPa. Single shear would have doubled it — the plane count is the whole problem.

> [!success] Check
> (a) $R\to2R$ multiplies $J$ by $16$ and divides the period by $4$. (b) $\tau$ scales as $1/d^2$; specifying the diameter specifies the answer up to the plane count.

</details>

### E9 — Cantilever deflection

A cantilever of length $1.0$ m carries $100$ N at the free end. Find the end deflection of a rectangular steel section $20$ mm wide by $40$ mm deep. $Y=2.0\times10^{11}$ Pa. What does rotating the rectangle through a right angle do?

<details><summary>Solution</summary>

$I=bh^3/12=0.020\times(0.040)^3/12=1.07\times10^{-7}$ m$^4$. $YI=2.13\times10^4$ N·m$^2$. $\delta=FL^3/(3YI)=100/(3\times2.13\times10^4)=1.56\times10^{-3}$ m $=1.6$ mm. Rotating the section to $40$ mm wide by $20$ mm deep divides $I$ by $4$ (depth enters as the cube, width as the first power) and multiplies the deflection by $4$. Same steel, wrong axis. Putting that area into an I-profile, which is OL7's comparison, beats either orientation.

> [!success] Check
> $\delta\propto L^3$ and, for a rectangle, $\delta\propto 1/h^3$. Doubling the depth at fixed width cuts the deflection by $8$.

</details>

### E10 — Crane cable or bicycle frame

Choose, with a number, between mild steel ($\sigma_y=2.5\times10^8$ Pa, $Y=2.0\times10^{11}$, $\rho=7800$), aluminium alloy ($\sigma_y=2.0\times10^8$, $Y=7.0\times10^{10}$, $\rho=2700$) and a carbon-fibre composite ($\sigma_f=1.5\times10^9$, $Y=1.5\times10^{11}$, $\rho=1600$) for (a) a crane cable of fixed breaking load and (b) a light stiff beam of fixed mass.

<details><summary>Solution</summary>

(a) A cable fails by yield. Mass per unit length at fixed breaking load is $\rho F/\sigma_y$, so the figure of merit is the specific strength $\sigma_y/\rho$: steel $3.2\times10^4$, aluminium $7.4\times10^4$, CFRP $9.4\times10^5$ (SI). The composite cable is about thirty times lighter than steel for the same break load. (b) At fixed mass and fixed proportions, $I\propto 1/\rho^2$ while $\delta\propto 1/(YI)$, so the beam index is $Y^{1/2}/\rho$: steel $57$, aluminium $98$, CFRP $242$. Ratio CFRP : aluminium : steel $\approx 4.2 : 1.7 : 1$. The bicycle frame wants the composite; the cable wants it too, but for a different index. Strength, stiffness and density are three axes, and the application picks the combination (D12.10).

> [!success] Check
> At equal density the cable ranking would follow $\sigma_y$ alone and the beam ranking $\sqrt{Y}$ alone. Density is what demotes steel in both.

</details>

## Part 6 · Archetypes and practice

| archetype | the move | the trap |
|---|---|---|
| extension under a load | $\Delta L=FL/(AY)$, units first | using diameter where area belongs |
| breaking load | $F_{max}=\sigma_b A$ | reading ultimate off a strain axis |
| self-weight | integrate; equivalent to $mg/2$ at the end | using the full weight |
| two-wire hanger | $T=mg/(2\sin\theta)$ | using it when $\theta$ is not given |
| sag of a straight wire | $y\propto (mg/YA)^{1/3}$ | linearising in the load |
| thermal, free | $\Delta L=\alpha L\Delta T$ | summing a year of cycles |
| thermal, constrained | $\sigma=Y\alpha\Delta T$, $L$ cancels | the sign: heating compresses |
| composite, series | common force, extensions add | assuming equal stress |
| composite, parallel | common extension, $F\propto k$ | assuming equal force |
| bulk modulus | $\Delta V/V=-\Delta p/B$ | quoting $B$ for a gas without the process |
| rivet | count the shear planes | single shear written as double |
| stored energy | $\tfrac12 F\Delta L$ | the $\tfrac12$ omitted |
| sudden load | peak extension $2\times$ static | equating it to a drop from height |
| falling weight | quadratic from energy | forgetting $\Delta$ in the descent $h+\Delta$ |
| torsion pendulum | $C=GJ/L$, $T=2\pi\sqrt{I/C}$ | $J=\pi R^4/2$, not $\pi R^4/4$ |
| $Y$ from a graph | slope of stress against strain | slope of force against extension, unconverted |
| cantilever | $\delta=FL^3/(3YI)$ | $I$ about the wrong axis |
| buckling | $P_{cr}=\pi^2 YI/L^2$ | keeping the larger of buckling and yield |

#### Q1. A steel wire of length $2.0$ m and area $1.0$ mm$^2$ ($Y=2.0\times10^{11}$ Pa) stretches $1.0$ mm under a load. What is the load?

<details><summary>Solution</summary>

$F=\Delta L\cdot AY/L=1.0\times10^{-3}\times1.0\times10^{-6}\times2.0\times10^{11}/2.0=100$ N.

</details>

#### Q2. The same wire breaks at a stress of $5.0\times10^8$ Pa. What is the breaking load?

<details><summary>Solution</summary>

$F=\sigma A=5.0\times10^8\times1.0\times10^{-6}=500$ N. Length and modulus do not enter.

</details>

#### Q3. A uniform rod of length $L$, density $\rho$ and modulus $Y$ hangs vertically. Show that its elongation is $\rho gL^2/(2Y)$, and state the end-load to which this is equivalent.

<details><summary>Solution</summary>

At height $x$ above the free end the section carries $\rho A gx$; an element $dx$ stretches $\rho g x\,dx/Y$. Integrate from $0$ to $L$: $\rho gL^2/(2Y)$. Equivalent end-load: $mg/2$.

</details>

#### Q4. A mass hangs from two wires at angle $\theta$ to the horizontal. Why is the tension $mg/(2\sin\theta)$ and not $mg/2$?

<details><summary>Solution</summary>

Each wire's vertical component is $T\sin\theta$, and two of them balance the weight. $mg/2$ is the answer only at $\theta=90^\circ$. At small $\theta$ the tension is much larger than the weight.

</details>

#### Q5. A steel rod ($\alpha=1.2\times10^{-5}$ K$^{-1}$, $Y=2.0\times10^{11}$ Pa) is clamped between two walls at $20^\circ$C and then cooled to $0^\circ$C. Find the stress and its sign.

<details><summary>Solution</summary>

The rod wants to shorten and is held, so the stress is tensile. $|\sigma|=Y\alpha\Delta T=2.0\times10^{11}\times1.2\times10^{-5}\times20=4.8\times10^7$ Pa, tension.

</details>

#### Q6. Two rods in series have stiffnesses $k$ and $2k$. What is the combined stiffness, and what fraction of the total extension sits in the softer rod?

<details><summary>Solution</summary>

$1/k_{tot}=1/k+1/(2k)=3/(2k)$, so $k_{tot}=2k/3$. Extensions at common force scale as $1/k$: the softer rod takes $2/3$ of the extension.

</details>

#### Q7. Water at $2.0\times10^7$ Pa above atmospheric is compressed. $B=2.2\times10^9$ Pa. Find the fractional volume change.

<details><summary>Solution</summary>

$|\Delta V/V|=\Delta p/B=2.0\times10^7/2.2\times10^9=9.1\times10^{-3}$, just under one percent.

</details>

#### Q8. A rivet of diameter $10$ mm in single shear carries $8.0$ kN. Find the shear stress.

<details><summary>Solution</summary>

$A=\pi(5.0\times10^{-3})^2=7.85\times10^{-5}$ m$^2$. $\tau=F/A=8000/(7.85\times10^{-5})=1.02\times10^8$ Pa. Double shear would have halved it.

</details>

#### Q9. A wire extends $2.0$ mm under $200$ N. How much elastic energy does it store?

<details><summary>Solution</summary>

$U=\tfrac12 F\Delta L=\tfrac12\times200\times2.0\times10^{-3}=0.20$ J. Equivalently $\tfrac12\times\text{stress}\times\text{strain}\times\text{volume}$.

</details>

#### Q10. A $1.0$ kg mass falls $0.10$ m onto a wire of stiffness $2.0\times10^4$ N/m. Estimate the peak force, stating the approximation.

<details><summary>Solution</summary>

$\Delta_{st}=mg/k=4.9\times10^{-4}$ m, and $h\gg\Delta_{st}$, so $F_{max}\approx\sqrt{2hmgk}=\sqrt{2\times0.10\times1.0\times9.8\times2.0\times10^4}=198$ N. The neglected $\Delta$ in the descent corrects this by under one percent.

</details>

#### Q11. A torsion pendulum has $C=0.010$ N·m/rad and a disc of $I=0.040$ kg·m$^2$. Find the period.

<details><summary>Solution</summary>

$T=2\pi\sqrt{I/C}=2\pi\sqrt{4.0}=12.6$ s.

</details>

#### Q12. A force–extension graph for a wire of length $2.0$ m and area $1.0$ mm$^2$ is a straight line through the origin with slope $1.0\times10^5$ N/m. Find $Y$.

<details><summary>Solution</summary>

The slope is $k=YA/L$, so $Y=kL/A=1.0\times10^5\times2.0/1.0\times10^{-6}=2.0\times10^{11}$ Pa. Reading the slope as $Y$ itself is the trap.

</details>

#### Q13. Two cantilevers, identical except that one is twice as long, carry the same end load. Compare their deflections and their maximum bending stresses.

<details><summary>Solution</summary>

$\delta\propto L^3$, so the long one deflects $8$ times as much. Maximum moment is $FL$, so the maximum stress, $\sigma=My_{max}/I$, doubles. Deflection and stress scale differently; a stiffness check is not a strength check.

</details>

#### Q14. A steel bar ($\sigma=0.29$) is stretched by $0.10\%$ longitudinally. Find the lateral strain and the fractional volume change.

<details><summary>Solution</summary>

Lateral strain $=-\sigma\varepsilon=-2.9\times10^{-4}$. Volume strain $=(1-2\sigma)\varepsilon=0.42\times1.0\times10^{-3}=4.2\times10^{-4}$. The bar gets longer more than it gets thinner.

</details>

#### Q15. A wire is cut into four equal lengths and the pieces are used side by side. By what factor does the stiffness change?

<details><summary>Solution</summary>

Each piece has $4$ times the original stiffness (quarter length). Four in parallel: factor $16=4^2$. In general, $n$ pieces cut from one wire and used in parallel give $n^2$.

</details>

#### Q16. The same load is applied gradually, suddenly, and by a drop from a height of ten static extensions. Rank the peak extensions.

<details><summary>Solution</summary>

Gradual: $\Delta_{st}$. Sudden: $2\Delta_{st}$. Drop from $h=10\Delta_{st}$: $\Delta=\Delta_{st}(1+\sqrt{1+20})=5.6\Delta_{st}$. Order: gradual, sudden, drop.

</details>

#### Q17. A hollow shaft and a solid shaft have the same outer radius. Which has the larger torsional stiffness, and why is that the wrong comparison for a designer counting kilograms?

<details><summary>Solution</summary>

The solid shaft has the larger $J$, since the hollow one is missing the core. Per kilogram the hollow shaft wins, because the core contributes little $J$ and much mass. Equal-radius and equal-mass are different questions.

</details>

#### Q18. A brass ring is heated and slipped over a steel plug, then cooled. Is the ring left in tension or compression?

<details><summary>Solution</summary>

Tension. Cooling wants to shrink the ring onto the plug; the plug prevents the shrinkage, so the ring is stretched. The plug is left in compression. This is E4's sign convention on a closed shape.

</details>

#### Q19. A material has $Y=1.0\times10^9$ Pa and $\sigma=0.49$. Estimate $B$ and $G$, and say what the material is like.

<details><summary>Solution</summary>

$B=Y/[3(1-2\sigma)]=1.0\times10^9/(3\times0.02)=1.7\times10^{10}$ Pa. $G=Y/[2(1+\sigma)]=1.0\times10^9/2.98=3.4\times10^8$ Pa. $B\gg G$: nearly incompressible, easy to shear. Rubber.

</details>

#### Q20. A thin closed cylindrical pressure vessel has hoop stress $\sigma$. What is the longitudinal stress, and which crack appears first?

<details><summary>Solution</summary>

Longitudinal stress is $\sigma/2$: the pressure on the end cap, $p\pi r^2$, is carried by a ring of wall $2\pi rt$, while the hoop stress from a diametral cut is twice that. The hoop stress is the larger, so the vessel splits along a generator — a lengthwise crack — first.

</details>

#### Q21. A pinned column's length is doubled and its diameter doubled. What happens to the Euler load?

<details><summary>Solution</summary>

$I\propto d^4$ rises by $16$; $L^2$ rises by $4$; $P_{cr}\propto I/L^2$ rises by $4$. The yield load also rises by $4$, but from $\sigma_y A$ and not from the same formula. The two do not keep pace in general.

</details>

#### Q22. Why does the neutral axis of a composite beam not sit at the geometric centre?

<details><summary>Solution</summary>

Zero net axial force requires $\int Y\varepsilon\,dA=0$, and $\varepsilon\propto y$. If $Y$ varies across the section the stiffness-weighted centroid, not the geometric one, is the axis. Assuming the geometric centre mis-assigns the stress to both materials.

</details>

#### Q23. Rank steel, aluminium and wood by specific modulus $Y/\rho$, using $Y_{wood}\sim10^{10}$ Pa and $\rho_{wood}\sim600$ kg/m$^3$.

<details><summary>Solution</summary>

Steel $2.0\times10^{11}/7800=2.6\times10^7$. Aluminium $7.0\times10^{10}/2700=2.6\times10^7$. Wood $1\times10^{10}/600=1.7\times10^7$, all in m$^2$/s$^2$. Steel and aluminium tie; wood is close behind. Specific modulus, not modulus, is the ranking for a light tie-rod.

</details>

#### Q24. A load $mg$ is applied suddenly to a wire. Show that the peak stress is twice the static stress, and name the assumption that fails if the wire yields.

<details><summary>Solution</summary>

Energy $mg\Delta=\tfrac12 k\Delta^2$ gives $\Delta=2mg/k$. Stress scales with extension in the linear range, so it doubles. If the wire yields, $k$ is not constant and the stored-energy triangle is the wrong shape; the stress sticks near yield while the extension runs away.

</details>

#### Q25. The speed of a longitudinal wave in a thin steel rod is $\sqrt{Y/\rho}$. Estimate it, and say why a thick block of the same steel is faster.

<details><summary>Solution</summary>

$\sqrt{2.0\times10^{11}/7800}=\sqrt{2.56\times10^7}=5.1\times10^3$ m/s. A thick block cannot contract laterally as the wave passes, so the effective modulus is $B+4G/3$, larger than $Y$ by $(1-\sigma)/[(1+\sigma)(1-2\sigma)]\approx1.3$ for steel, and the speed is about $5.9$ km/s. The thin-rod formula needs free sides.

</details>

## Part 7 · Toolkit

**T1 — Stress, not force.** Before any formula, name the plane and divide by its area. If the answer has dimensions of force and the question asked how close to breaking, you have not started.

**T2 — Series and parallel, as springs.** Compute $k=YA/L$ for each member first. Series: compliances add. Parallel under a rigid bar: stiffnesses add, and the load splits in proportion to $k$. Everything else in the extension family is one of these two with a constraint written on top.

**T3 — Expand free, then put it back.** Thermal problems in two steps: the free change $\alpha L\Delta T$, then the mechanical change that restores the constraint. The stress is whatever mechanics needs for that restoration. The sign is the sign of the restoration, not of $\Delta T$.

**T4 — Energy at the turning point, not balance.** For a falling weight, write $Mg(h+\Delta)=\tfrac12 k\Delta^2$. At maximum extension the kinetic energy is zero, so energy closes the problem; the free-body diagram does not balance, because the mass is accelerating. Demanding $F=mg$ at the extreme is the wrong tool.

**T5 — Which modulus.** Pull or bend a slender member: $Y$. Squeeze a volume from all sides: $B$. Twist or shear: $G$. If the loading is mixed, split it into principal stresses and superpose — that is all the interrelations are. If you cannot name the mode, you cannot pick the modulus.

**T6 — Section before material.** $I$ and $J$ are geometry. Compute them, or their ratio, before inserting $Y$ or $G$; most "which is stiffer" questions cancel the material. A solid circle has $I=\pi R^4/4$ in bending and $J=\pi R^4/2$ in torsion. A rectangle has $I=bh^3/12$ about the centroidal axis parallel to the side $b$.

**T7 — The atomic estimate.** $Y\sim D/r_0^3$ with $D$ a few eV and $r_0\sim2$ Å lands on $10^{10}$–$10^{11}$ Pa. Use it to smell-test any modulus. A result of $10^6$ Pa is a polymer or an error; $10^{14}$ Pa is neither a metal nor a calculation to trust.

**T8 — Static, sudden, dropped.** Three loadings, three factors. Static: $\Delta_{st}=mg/k$. Sudden: $2\Delta_{st}$. Dropped from $h$: $\Delta_{st}(1+\sqrt{1+2h/\Delta_{st}})$. "Released" with no height stated is sudden; "falls from" is the quadratic.

> [!tip] Insight
> T2, T3 and T8 are the whole of the extension paper. T5 and T6 are the whole of the modulus paper. T7 is the olympiad smell test. A question that mixes two of them is a synthesis, not a new formula.

## Part 8 · Traps

1. **Stress written as force.** $F$ where $F/A$ belongs, usually visible because the units come out in newtons. Cure: T1.
2. **Diameter in the area slot.** $A=\pi d^2/4$, not $\pi d^2$ and not $\pi r^2$ with the diameter read as a radius. The square makes this a factor-of-four error, the commonest arithmetic fault in the chapter.
3. **Self-weight with the full weight.** The integral of a triangular load is half the rectangle. If your elongation equals $MgL/(AY)$, you have skipped the integration.
4. **Thermal sign.** Heating a constrained rod compresses it; cooling tensions it. The stress opposes the prevented strain.
5. **Summing a year of cycles.** Expansion is not a ratchet. The annual question asks for the swing, $\alpha L\Delta T$ over the peak range, once.
6. **Poisson applied to the length.** $\sigma$ corrects the lateral strain. The length change of a uniaxial test is $\Delta L=FL/(AY)$ with no Poisson factor; Poisson appears in the volume change and in the interrelations.
7. **The missing factor $2$ on a sudden load.** Peak extension $2mg/k$, peak stress twice static. Setting $h=0$ in the drop formula is the check, not a coincidence.
8. **$mgh=\tfrac12 k\Delta^2$ for a falling weight.** The mass descends $h+\Delta$, not $h$. Dropping $\Delta$ is safe only when $h\gg\Delta$, and the approximation must be named.
9. **Neutral axis at the geometric centre of a composite section.** True for one material, false for two. The axis is the stiffness-weighted centroid.
10. **$J$ and $I$ swapped.** Bending of a circular section uses $I=\pi R^4/4$; torsion uses $J=\pi R^4/2$. A factor-of-two error with the right dimensions is this one.
11. **Buckling load compared with yield, and the larger kept.** The column fails at the smaller. For slender columns buckling wins by a wide margin, and it depends on $Y$, not on strength.
12. **Thin-rod sound speed used inside a bulk solid.** $\sqrt{Y/\rho}$ needs free sides. A seismic P-wave travels at $\sqrt{(B+4G/3)/\rho}$.

> [!danger] Trap
> The factor-of-two family — self-weight, sudden load, hoop against longitudinal stress, $J$ against $I$ — is four different twos. They are not interchangeable, and inserting a two is not a method. Each has a one-line origin: a triangular integral, an energy root, a free-body cut, a definition.

## Part 9 · Playbook

**Triage, in order.**

1. Is the body being stretched, squeezed, sheared, twisted, bent, or heated? Name the mode before the modulus (T5).
2. Is the geometry a wire, a composite, a shaft, a beam, or a vessel? Section properties $A$, $I$, $J$ come next (T6).
3. Is the load static, sudden, or dropped (T8)? Thermal loads take the expand-then-restore route (T3) instead.
4. Only then the formula from the ledger. If two formulae seem to apply, one of them is a limit of the other; say which.
5. Smell test: stress against yield, strain against $10^{-3}$, modulus against $D/r_0^3$ (T7), and the limit checks in the ledger.

**Timing.** A four-mark extension or thermal-stress item is two minutes. A nine-mark falling-weight or buckling comparison is eight, mostly bookkeeping. If the algebra exceeds a short quadratic, the setup is wrong.

**What a full-mark answer looks like.** The mode named, the formula written with its validity ("linear, fully constrained"), the number with units, the sign where a sign exists, and one limit check. A bare number scores the arithmetic and nothing else.

> [!tip] Insight
> Most lost marks in this chapter are category errors: a stiffness question answered with a strength, a thermal question answered with a free expansion, a dynamic question answered with a balance. The triage exists to make the category choice visible before the arithmetic starts.

## Part 10 · Olympiad extension

The linear law is a small piece of a well. Two things sit just outside it and are examined as if they were inside. **Hysteresis:** a real loading–unloading curve is a loop, and the area of the loop is energy turned to heat per cycle. Rubber's loop is fat, which is why a rubber mount damps; spring steel's is thin, which is why a tuning fork rings. The $\tfrac12\sigma\varepsilon$ formula is the area of the triangle, not of the loop, and it overcounts the recovered energy by exactly the loop area. **Fatigue:** a paperclip hardens because each bend multiplies dislocations and tangles them, raising the stress needed for the next slip — and then snaps, because the same tangle nucleates a crack. The yield stress went up; the life went down. Neither effect is in Hooke's law. Both are why a design that lives on the straight line is quoted with a safety factor.

### OL1 — Why Young's modulus is $10^{11}$ Pa

Model neighbouring atoms by a pair potential $U(r)$ with a minimum at $r_0$ and a well depth $D$ of a few electronvolts. A chain under tension $F$ stretches each bond by $s$, and $F=U''(r_0)\,s$ to first order. One chain occupies an area $\sim r_0^2$, and the strain is $s/r_0$, so

$$
Y=\frac{F/r_0^2}{s/r_0}=\frac{U''(r_0)}{r_0}.
$$

The curvature of a well of depth $D$ and width $r_0$ is $U''\sim D/r_0^2$, hence $Y\sim D/r_0^3$. With $D=3$ eV $=4.8\times10^{-19}$ J and $r_0=2$ Å, $r_0^3=8\times10^{-30}$ m$^3$ and $Y\sim6\times10^{10}$ Pa. Every ordinary solid lands between $10^{10}$ and $10^{11}$ Pa because every ordinary bond is a few eV across a few angstroms: the modulus is a bond energy per atomic volume, and there are no other scales in the problem. The same estimate gives the interatomic spring, $k_a=U''(r_0)=Yr_0\approx40$ N/m for steel — a laboratory-scale spring constant, hiding in a bond. Rubber's $10^6$ Pa is not a failure of the arithmetic; it is a different mechanism, entropy of coiled chains, and the estimate does not apply to it.

<details><summary>Solution</summary>

The derivation is the solution. Checks: diamond, with a deeper well, is several times stiffer than steel and has a smaller thermal expansion, as OL2 will demand; ice, with a hydrogen-bond well of tenths of an eV, has $Y\sim10^{10}$ Pa. Both sit where $D/r_0^3$ puts them.

</details>

### OL2 — Thermal expansion as the asymmetry of the well

A symmetric well would give $\langle r\rangle=r_0$ at every temperature. Write the real well, with $s=r-r_0$, as $U=\tfrac12 k s^2+\tfrac16\gamma s^3$, where $k=U''(r_0)$ and $\gamma=U'''(r_0)$. A well that is softer outward — the usual case, steep wall at small $r$, flat tail at large $r$ — has $\gamma<0$.

The classical average to first order in $\gamma$: the Boltzmann weight is the Gaussian of the parabola times $1-\gamma s^3/(6k_B T)$. The correction to $\langle s\rangle$ comes from the even integrand $s^4$, and with $a=k/(2k_B T)$ the Gaussian moments $\langle s^2\rangle=1/(2a)$ and $\langle s^4\rangle=3/(4a^2)$ give

$$
\langle s\rangle=-\frac{\gamma\,k_B T}{2k^2},\qquad \alpha=\frac{1}{r_0}\frac{d\langle s\rangle}{dT}=-\frac{\gamma\,k_B}{2r_0 k^2}.
$$

Since $\gamma<0$, $\alpha>0$: the solid expands. Estimating $|\gamma|\sim k/r_0$ and $k\sim D/r_0^2$ collapses this to $\alpha\sim k_B/(2D)$. For $D=3$ eV, $k_B/D=2.9\times10^{-5}$ K$^{-1}$ and $\alpha\sim1.4\times10^{-5}$ K$^{-1}$ — the steel number, from the bond energy alone, with $r_0$ cancelled. The same estimate ranks materials: diamond (large $D$) expands little, a weakly bound molecular solid (small $D$) expands a lot. And $\alpha B$ is roughly $k_B$ per atomic volume, a few MPa/K, which is why a table of $\alpha$ and a table of $B$ are nearly reciprocals of each other. The phenomenon of expansion is [[Heat|heat]]'s; the reason it has the sign and the size it has is this asymmetry.

<details><summary>Solution</summary>

As derived. A symmetric well ($\gamma=0$) gives $\alpha=0$ exactly, to this order; the first surviving term is then the quartic, and it does not shift $\langle s\rangle$ at all in the classical average. Expansion is evidence of asymmetry, not merely of vibration.

</details>

### OL3 — A falling weight, with the rod's own mass

A rod of mass $m$, stiffness $k=YA/L$, hangs vertically. A mass $M$ falls onto its end from height $h$. Assuming the displacement stays in the static shape $u(x)=\delta\,x/L$ (origin at the support), write the energy balance as an integral and solve for $\delta$.

<details><summary>Solution</summary>

Elastic energy $\int_0^L\tfrac12 YA(du/dx)^2 dx=\tfrac12 k\delta^2$ for this shape, which is the shape that minimises it at given end displacement. The falling mass descends $h+\delta$. The rod's own centre of mass descends $\delta/2$, so its gravitational energy falls by $mg\delta/2$. At maximum extension every velocity in this self-similar mode is zero, and

$$
\tfrac12 k\delta^2=Mg(h+\delta)+\tfrac12 mg\delta.
$$

The quadratic $k\delta^2-2(M+m/2)g\delta-2Mgh=0$ has the positive root

$$
\delta=\frac{(M+m/2)g+\sqrt{[(M+m/2)g]^2+2kMgh}}{k}.
$$

Numbers: $M=10$ kg, $m=40$ kg, $k=1.0\times10^5$ N/m, $h=1.0$ mm. Then $(M+m/2)g=294$ N, $2kMgh=1.96\times10^4$ N$^2$, and $\delta=(294+325)/k=6.2\times10^{-3}$ m. Dropping the rod's mass gives $2.7\times10^{-3}$ m: the rod's weight, sampled at half the end displacement, more than doubles the extension. The assumption fails when the loading time is not long compared with the transit time $L/c$, $c=\sqrt{Y/\rho}$: a stress wave of amplitude $\rho c v$ then arrives at the support before the rod has agreed on a shape, and the integral over the static mode is the wrong ledger. For a $2$ m steel rod, $L/c\sim0.4$ ms; a drop that loads over many milliseconds is safe, an impact is not.

</details>

### OL4 — The constant-stress rod

A rod must carry a load $W$ at its lower end plus its own weight, and every cross-section is to work at the same stress $\sigma_0$. Find $A(x)$.

<details><summary>Solution</summary>

At height $x$ above the load, $\sigma_0 A(x)=W+\int_0^x\rho g A(x')dx'$. Differentiate both sides: $\sigma_0 A'=\rho g A$, so

$$
A(x)=A_0 e^{x/\lambda},\qquad \lambda=\frac{\sigma_0}{\rho g},\qquad A_0=\frac{W}{\sigma_0}.
$$

The length $\lambda$ is the height at which a *uniform* column's base stress equals $\sigma_0$; past $\lambda$ a prismatic column crushes under its own weight no matter how wide you make it (widening adds weight in proportion to strength). The exponential flare removes that limit: stress stays $\sigma_0$ at any height, paid for by a base that grows as $e^{h/\lambda}$. For structural steel $\lambda=\sigma_y/(\rho g)\approx2.5\times10^8/(7800\times9.8)\approx3.3$ km; for wood in compression along the grain, $\sim40$ MPa and $600$ kg/m$^3$, $\lambda\sim7$ km; for bone, of order $10$ km. No tree, bone or building is anywhere near its crushing length. The limits that actually bind are buckling (OL6) and, for a tree, the hydraulic limit of [[Fluid-mechanics#Part 10 · Olympiad extension|the fluid chapter]] — suction and embolism, near $100$ m, fifty times nearer than $\lambda$. Constant stress explains the flare of a trunk. It does not explain the height of a forest.

</details>

### OL5 — The cantilever, integrated

A cantilever of length $L$ and flexural rigidity $YI$ carries an end load $F$. Derive the tip deflection from $d^2y/dx^2=M(x)/(YI)$, and state the result for a uniform load $w$ per unit length.

<details><summary>Solution</summary>

Take $x$ from the built-in end. Then $M(x)=F(L-x)$ (the sign convention: sagging positive downward, with $y$ positive down). 

$$
\frac{d^2y}{dx^2}=\frac{F(L-x)}{YI}.
$$

Integrate, with $y'(0)=0$: $y'=F(Lx-x^2/2)/(YI)$. Integrate again, with $y(0)=0$: $y=F(Lx^2/2-x^3/6)/(YI)$. At the tip,

$$
\delta=y(L)=\frac{FL^3}{3YI}.
$$

For a uniform load the moment is $w(L-x)^2/2$, and the same two integrations with the same boundary conditions give $\delta=wL^4/(8YI)=WL^3/(8YI)$ where $W=wL$ is the total load. Comparing $FL^3/(3YI)$ with $WL^3/(8YI)$: the same total load concentrated at the tip deflects $8/3$ times as much as when it is spread along the beam. The small-slope step $y''\approx 1/R$ is the validity condition; a deflection comparable to $L$ needs the exact curvature.

</details>

### OL6 — Buckling: the Euler load, then a real column

(a) Show dimensionally that an elastic buckling load can only be $P\propto YI/L^2$. (b) For a pinned column the buckled shape is $y=\delta\sin(\pi x/L)$. Derive $P_{cr}$. (c) Compare buckling with yield for a steel rod of radius $1.0$ cm and length $2.0$ m, and for a hollow tube of the same mass and length with outer radius $1.5$ cm.

<details><summary>Solution</summary>

(a) $Y$ brings force per area, $I$ brings length$^4$, $L$ brings length. The only combination with the dimensions of force that uses the bending stiffness rather than the area is $YI/L^2$. (Yield, $P=\sigma_y A$, is the combination that uses strength and area instead. A column has both available; the smaller one governs.) (b) Curvature of the sine shape: $y''=-\delta(\pi/L)^2\sin(\pi x/L)$, so the peak curvature is $\delta\pi^2/L^2$. The moment at midspan is $P\delta$, and $M=YI/R$, hence $P\delta=YI\cdot\delta\pi^2/L^2$ and

$$
P_{cr}=\frac{\pi^2 YI}{L^2}.
$$

The amplitude $\delta$ cancels: buckling is an eigenvalue, not a deflection. (c) Solid: $I=\pi R^4/4=7.85\times10^{-9}$ m$^4$, $P_{cr}=\pi^2\times2.0\times10^{11}\times7.85\times10^{-9}/4=3.9\times10^3$ N. Yield load $\sigma_y A=2.5\times10^8\times\pi\times10^{-4}=7.9\times10^4$ N. Buckling wins by a factor of twenty: the rod is a column, not a strut, and thickening it helps as $R^4$ while shortening it helps as $1/L^2$. Hollow, same area: $R^2-r^2=10^{-4}$, $r=1.12$ cm, $I=\pi(R^4-r^4)/4=2.75\times10^{-8}$ m$^4$, $P_{cr}=1.4\times10^4$ N, three and a half times the solid rod's, at the same mass. Material moved away from the axis is the whole of the improvement, exactly as in torsion.

</details>

### OL7 — What an I-beam actually buys

Compare $I$ per unit area for a $20\times40$ mm rectangle and for an I-section $80$ mm deep, flanges $40\times5$ mm, web $4$ mm thick. Then compare the I-section with a rectangle of the *same* depth and the *same* area, so that the depth is not doing the work unsupervised.

<details><summary>Solution</summary>

Rectangle: $A=800$ mm$^2$, $I=bh^3/12=1.07\times10^5$ mm$^4$, $I/A=133$ mm$^2$. I-section: $A=2\times40\times5+70\times4=680$ mm$^2$. Web $I=4\times70^3/12=1.14\times10^5$ mm$^4$. Each flange: its own $bh^3/12$ is negligible ($4\times10^2$ mm$^4$), and $Ad^2=200\times(37.5)^2=2.81\times10^5$ mm$^4$, so two flanges contribute $5.63\times10^5$. Total $I=6.8\times10^5$ mm$^4$, $I/A=1000$ mm$^2$ — seven times the shallow rectangle, but the I-section is also twice as deep, and depth alone, as $h^2$, would give a factor of four. Fair comparison: a rectangle $80$ mm deep with area $680$ mm$^2$ has width $8.5$ mm and $I=3.6\times10^5$ mm$^4$, $I/A=530$ mm$^2$. The I-profile beats it by a factor $1.9$, which is the genuine gain from moving area to the flanges. "Five times stiffer" is what you get by changing the depth and the profile at once and then crediting the profile. Quote the comparison you actually made.

</details>

### OL8 — Where Hooke's law would have failed, if yield had not got there first

Keep the cubic well of OL2 and find the force, the fractional correction to Hooke's law, and the strain at which the correction reaches one percent.

<details><summary>Solution</summary>

$F=dU/ds=ks+\tfrac12\gamma s^2$. The fractional correction to the linear law is $|\gamma|s/(2k)$. With $|\gamma|\sim k/r_0$ this is $s/(2r_0)=|\varepsilon|/2$. A one-percent correction needs $|\varepsilon|\sim0.02$. Mild steel yields at a strain of order $10^{-3}$, where the cubic correction is $0.05\%$ — invisible on any stress–strain plot. So for metals the straight line ends because dislocations move, not because the well is curved. The cubic term's fingerprint, in a crystal that somehow did not yield, would be tension/compression asymmetry: the correction changes sign with $s$, so the apparent modulus in compression differs from the one in tension. Rubber leaves the straight line for a third reason, finite chain length, at strains of order $1$, where no cubic expansion was ever going to cope.

</details>

> [!abstract] DIAGRAM D12.14 · Hoop stress by a diametral cut
> *Show:* a closed thin cylinder, cut along a diameter and one end removed in a second small sketch; on the diametral cut, pressure $p$ acting on the rectangle $2r\times L$ balanced by two walls of thickness $t$ carrying $\sigma$; on the end cap, $p\pi r^2$ balanced by the ring $2\pi rt$ carrying $\sigma_L$; the two stresses labelled $\sigma=pr/t$ and $\sigma_L=pr/(2t)$, with the lengthwise crack drawn on the generator.
> *Search:* "thin cylinder hoop stress longitudinal stress free body diagram"

### OL9 — A thin wall and a thin strand

(a) Derive the hoop stress in a thin closed cylinder and the longitudinal stress, and say which crack forms first. (b) A spider's dragline, representative values $\sigma_f=1.0\times10^9$ Pa, $Y=1.0\times10^{10}$ Pa, $\rho=1300$ kg/m$^3$, diameter $3.0$ μm. How much mass can one strand lift, and how does its specific strength compare with mild steel?

<details><summary>Solution</summary>

(a) Cut the cylinder along a diameter (D12.14). Pressure on the cut face $2rL$ is balanced by two walls: $p\cdot2rL=2\sigma t L$, so $\sigma=pr/t$. Cut across the end cap: $p\pi r^2=\sigma_L\cdot2\pi rt$, so $\sigma_L=pr/(2t)$. Hoop stress is twice longitudinal stress, so the wall fails along a generator — the crack runs lengthwise — while the ends are still comfortable. The thin-wall step ($t\ll r$, stress uniform through the thickness) is the validity condition; a gun barrel is not this problem. (b) $A=\pi(1.5\times10^{-6})^2=7.1\times10^{-12}$ m$^2$, $F=\sigma_f A=7.1\times10^{-3}$ N, liftable mass $0.72$ g. A human-hair thickness, $70$ μm, multiplies the area by $(70/3)^2\approx540$ and lifts about $0.4$ kg. Specific strength $\sigma_f/\rho$: silk $7.7\times10^5$, mild steel $3.2\times10^4$ m$^2$/s$^2$, so silk wins by a factor of about $24$. Specific modulus $Y/\rho$ goes the other way: silk $7.7\times10^6$, steel $2.6\times10^7$. A strand of silk is an excellent rope and a poor ruler. Strength and stiffness are different axes even at the scale of a protein.

</details>

### OL10 — Two wave speeds, and what an earthquake is made of

(a) Estimate the longitudinal wave speed in a thin steel rod and in the bulk of the same steel. (b) Crustal rock carries P-waves at $6.0$ km/s and S-waves at $3.5$ km/s, with $\rho=2700$ kg/m$^3$. Find $G$, $B$ and Poisson's ratio, and say what the absence of S-waves beyond a certain depth told seismology.

<details><summary>Solution</summary>

(a) Thin rod, sides free to contract: $v=\sqrt{Y/\rho}=\sqrt{2.0\times10^{11}/7800}=5.1$ km/s, and the measured bar velocity sits there. In the bulk the sides are constrained by the material beside them, the modulus becomes $B+4G/3=Y(1-\sigma)/[(1+\sigma)(1-2\sigma)]$, and for $\sigma=0.29$ the factor is $1.31$. Speed $\sqrt{1.31}\times5.1=5.8$ km/s. Using the rod formula on a seismic arrival is a category error of the sort Part 9 exists to prevent. (b) S-waves are shear: $v_S=\sqrt{G/\rho}$, so $G=\rho v_S^2=2700\times(3500)^2=3.3\times10^{10}$ Pa. P-waves are the constrained compression: $v_P=\sqrt{(B+4G/3)/\rho}$, so $B+4G/3=2700\times(6000)^2=9.7\times10^{10}$ Pa, $4G/3=4.4\times10^{10}$, and $B=5.3\times10^{10}$ Pa. Then $\sigma=(3B-2G)/[2(3B+G)]=(1.59\times10^{11}-6.6\times10^{10})/[2(1.59\times10^{11}+3.3\times10^{10})]=0.24$. A liquid has $G=0$ and carries no S-wave. The Earth's outer core, which transmits P and refuses S, is fluid — an inference from two moduli and one absence, which is as much as this chapter's wave theory can say. The wave equation itself belongs to [[Sound-waves|sound waves]] and [[String-waves|string waves]].

</details>

### 10.1 Where the model stops

Hooke's law ends at yield for every metal you will meet, and at a strain of a few percent for a perfect crystal that somehow did not yield (OL8). Euler's load is an elastic eigenvalue; a column that has already yielded buckles by a different, lower, formula that this chapter does not own. The hoop-stress cut assumes $t\ll r$. The falling-weight integral assumes the rod agrees on a shape, which it does only if $L/c$ is short compared with the loading (OL3). Isotropy fails for wood and for the composite of E10, whose $Y$ depends on direction; the scalar modulus is then the wrong object. Rubber is an entropy spring, and nothing in §3.11 prices it.

> [!quote] Hand-off
> [[Heat|Heat]] owns thermal expansion as a phenomenon and the tables of $\alpha$; this chapter only borrows $\alpha$ to build a stress, and returns the explanation of its size in OL2. [[Sound-waves|Sound waves]] owns $v=\sqrt{B/\rho}$ as a wave result; OL10 only identifies which modulus goes in the square root. [[Simple-harmonic-motion|SHM]] owns the oscillator once $k$ or $C$ has been computed. [[Fluid-mechanics|Fluids]] owns the tree's hydraulic ceiling, which is the limit OL4's crushing length does not turn out to be.

## Part 11 · Olympiad-grade paper

**Time: 180 minutes · Maximum marks: 200 · 36 questions.**
Sections: A — 12 single-correct (4 marks each, −1 for a wrong answer); B — 8 one-or-more-correct (4 marks each, no negative marking); C — 6 numerical answers (5 marks each); D — 10 long-form (9 marks each). Solutions follow each question. The marking scheme is in Part 12.

| Section | Questions | Marks each | Subtotal | What it tests |
|---|---|---:|---:|---|
| A | 1–12 | 4 | 48 | blocks 2–4 |
| B | 13–20 | 4 | 32 | blocks 3–4 |
| C | 21–26 | 5 | 30 | blocks 4, 6 |
| D | 27–36 | 9 | 90 | block 10 |
| | 36 | | 200 | |

#### Section A · Single correct

### P1 · 4 marks

A wire's length is doubled and its diameter halved, the material and the load unchanged. The extension becomes: (a) $2$ times (b) $8$ times (c) $16$ times (d) $4$ times.

<details><summary>Solution</summary>

$\Delta L=FL/(AY)$ and $A\propto d^2$, so $A$ falls by $4$ while $L$ rises by $2$. Extension multiplies by $8$. **(b)**.

</details>

### P2 · 4 marks

The elongation of a uniform rod under its own weight equals the elongation under an end load of: (a) $mg$ (b) $mg/2$ (c) $2mg$ (d) $mg/4$.

<details><summary>Solution</summary>

The axial force ramps from $0$ to $mg$; the integral is half the rectangle. **(b)**.

</details>

### P3 · 4 marks

A rod fixed between two rigid walls is heated. The stress in it is: (a) tensile (b) compressive (c) zero (d) pure shear.

<details><summary>Solution</summary>

The rod wants to lengthen and is pushed back. **(b)**.

</details>

### P4 · 4 marks

A material that does not change volume when stretched has Poisson's ratio: (a) $0$ (b) $0.25$ (c) $0.5$ (d) $1$.

<details><summary>Solution</summary>

Volume strain $(1-2\sigma)\varepsilon=0$ gives $\sigma=\tfrac12$. **(c)**.

</details>

### P5 · 4 marks

A load applied suddenly produces a peak extension which, compared with the static extension, is: (a) equal (b) twice (c) four times (d) half.

<details><summary>Solution</summary>

$mg\Delta=\tfrac12 k\Delta^2$ gives $\Delta=2mg/k$. **(b)**.

</details>

### P6 · 4 marks

A hollow shaft and a solid shaft have the same mass, length, material and applied torque. The hollow shaft twists: (a) more (b) less (c) the same (d) only if it is thin.

<details><summary>Solution</summary>

$J=\int r^2 dA$ rewards material far from the axis. **(b)**.

</details>

### P7 · 4 marks

The tip deflection of a cantilever under an end load scales with length as: (a) $L$ (b) $L^2$ (c) $L^3$ (d) $L^4$.

<details><summary>Solution</summary>

$\delta=FL^3/(3YI)$. **(c)**. A uniform load would have been $L^4$ in $w$, which is the distractor.

</details>

### P8 · 4 marks

The thermal stress in a fully constrained rod does not depend on: (a) $Y$ (b) $\alpha$ (c) $\Delta T$ (d) $L$.

<details><summary>Solution</summary>

$\sigma=Y\alpha\Delta T$. Length cancels when the prevented strain is written. **(d)**.

</details>

### P9 · 4 marks

A load hung at the midpoint of a straight wire is doubled. The sag becomes about: (a) $1.26$ times (b) $2$ times (c) $4$ times (d) $8$ times.

<details><summary>Solution</summary>

$y\propto F^{1/3}$, and $2^{1/3}=1.26$. **(a)**. Linear scaling is the trap E5(b) exists to kill.

</details>

### P10 · 4 marks

The isothermal bulk modulus of an ideal gas is: (a) $\gamma p$ (b) $p$ (c) $0$ (d) infinite.

<details><summary>Solution</summary>

$pV=$ constant gives $dp=-p\,dV/V$, so $B=p$. The adiabatic value is $\gamma p$. **(b)**.

</details>

### P11 · 4 marks

The rod of P3 is cooled instead. The stress is: (a) compressive (b) tensile (c) zero (d) pure shear.

<details><summary>Solution</summary>

Cooling wants to shorten the rod; the walls hold it, so it is in tension. **(b)**.

</details>

### P12 · 4 marks

The Euler buckling load of a pinned column depends on its length as: (a) $1/L$ (b) $1/L^2$ (c) $1/L^3$ (d) not at all.

<details><summary>Solution</summary>

$P_{cr}=\pi^2 YI/L^2$. **(b)**.

</details>

#### Section B · One or more correct

### P13 · 4 marks

For an isotropic linear solid: (a) $Y=2G(1+\sigma)$; (b) $Y=3B(1-2\sigma)$; (c) $\sigma=0.6$ is possible; (d) $\sigma\approx0.5$, as in rubber, means $B$ is very large compared with $Y$.

<details><summary>Solution</summary>

**(a), (b), (d)**. (c) would make $B$ negative, which a stable solid cannot have.

</details>

### P14 · 4 marks

A mass falls onto a wire from rest: (a) the maximum extension exceeds the static extension; (b) when $h\gg\Delta_{st}$, a stiffer wire develops a larger peak force; (c) force balance and energy agree at the lowest point; (d) the limit $h=0$ returns twice the static extension.

<details><summary>Solution</summary>

**(a), (b), (d)**. At the lowest point the mass is accelerating upward, so the free-body diagram does not balance; energy is the tool that closes.

</details>

### P15 · 4 marks

Rods treated as springs: (a) in series the force is common and extensions add; (b) in parallel under a rigid bar the forces are proportional to the stiffnesses; (c) in a series pair the stresses are equal even when the areas differ; (d) cutting one wire into $n$ equal pieces and using them in parallel multiplies $k$ by $n^2$.

<details><summary>Solution</summary>

**(a), (b), (d)**. (c) is false: a common force through a smaller area is a larger stress.

</details>

### P16 · 4 marks

Torsion: (a) $\theta=TL/(GJ)$; (b) a solid circular shaft has $J=\pi R^4/2$; (c) at equal outer radius, a hollow shaft has a smaller $J$ per unit area than a solid one; (d) a torsion pendulum has period $2\pi\sqrt{I/C}$ with $C=GJ/L$.

<details><summary>Solution</summary>

**(a), (b), (d)**. Removing the core removes little $J$ and much area, so $J/A$ rises. (c) has the comparison backwards.

</details>

### P17 · 4 marks

Bending: (a) strain is proportional to distance from the neutral axis; (b) an I-beam raises $I$ by placing area far from that axis; (c) a cantilever's tip deflection under an end load is $FL^3/(3YI)$; (d) the neutral axis of a two-material section is always the geometric centroid.

<details><summary>Solution</summary>

**(a), (b), (c)**. (d) holds only for one material. Two materials shift the axis toward the stiffer one.

</details>

### P18 · 4 marks

Thermal strain: (a) a free rod expands by $\alpha L\Delta T$; (b) a fully constrained rod develops stress $Y\alpha\Delta T$, independent of $L$; (c) a rail with expansion gaps develops no stress until a gap closes; (d) heating a clamped rod puts it in tension.

<details><summary>Solution</summary>

**(a), (b), (c)**. (d) has the sign wrong: heating compresses a clamped rod.

</details>

### P19 · 4 marks

Elastic energy: (a) the energy density is $\tfrac12\times$ stress $\times$ strain in the linear range; (b) the area of a hysteresis loop is energy lost per cycle; (c) a wire stores $\tfrac12 F\Delta L$; (d) past the elastic limit, unloading recovers all the work done.

<details><summary>Solution</summary>

**(a), (b), (c)**. Past yield, unloading recovers only the elastic triangle; the rest has become heat and permanent set. (d) is false.

</details>

### P20 · 4 marks

The atomic picture: (a) $Y=U''(r_0)/r_0$; (b) a few eV per cubic angstrom is a stress of order $10^{11}$ Pa, which is why solids sit there; (c) rubber is the same interatomic spring with weaker bonds; (d) thermal expansion needs an asymmetric well.

<details><summary>Solution</summary>

**(a), (b), (d)**. Rubber is an entropy spring. The pair-potential estimate does not price it, which is why (c) is false.

</details>

#### Section C · Numerical

### P21 · 5 marks

A steel wire, length $2.0$ m, diameter $1.0$ mm, $Y=2.0\times10^{11}$ Pa, carries $157$ N. Extension in mm, to two significant figures?

<details><summary>Solution</summary>

$A=\pi(0.50\times10^{-3})^2=7.85\times10^{-7}$ m$^2$. $\Delta L=157\times2.0/(7.85\times10^{-7}\times2.0\times10^{11})=2.0\times10^{-3}$ m. **$2.0$ mm**.

</details>

### P22 · 5 marks

A fully constrained steel rod, $\alpha=1.2\times10^{-5}$ K$^{-1}$, $Y=2.0\times10^{11}$ Pa, is heated by $50$ K. The stress, in MPa?

<details><summary>Solution</summary>

$\sigma=Y\alpha\Delta T=2.0\times10^{11}\times1.2\times10^{-5}\times50=1.2\times10^8$ Pa. **$120$ MPa**, compressive.

</details>

### P23 · 5 marks

A uniform steel rod, $L=50$ m, $\rho=7800$ kg/m$^3$, $Y=2.0\times10^{11}$ Pa, hangs under its own weight. Elongation in mm, to two significant figures?

<details><summary>Solution</summary>

$\Delta L=\rho gL^2/(2Y)=7800\times9.8\times2500/(4.0\times10^{11})=4.8\times10^{-4}$ m. **$0.48$ mm**.

</details>

### P24 · 5 marks

Seawater, $B=2.2\times10^9$ Pa, $\rho=1.0\times10^3$ kg/m$^3$, at a depth of $4.0$ km. Percentage increase in density, to two significant figures?

<details><summary>Solution</summary>

$\rho g d/B=1.0\times10^3\times9.8\times4.0\times10^3/(2.2\times10^9)=0.018$. **$1.8\%$**.

</details>

### P25 · 5 marks

A steel shaft, $L=0.50$ m, radius $1.0$ mm, $G=8.0\times10^{10}$ Pa, carries a torque of $0.10$ N·m. Angle of twist in degrees, to the nearest integer?

<details><summary>Solution</summary>

$J=\pi R^4/2=1.57\times10^{-12}$ m$^4$. $\theta=TL/(GJ)=0.050/(8.0\times10^{10}\times1.57\times10^{-12})=0.40$ rad $=23^\circ$. **$23$**.

</details>

### P26 · 5 marks

A cantilever, $L=1.0$ m, rectangular section $20$ mm by $40$ mm deep, $Y=2.0\times10^{11}$ Pa, end load $200$ N. Tip deflection in mm, to two significant figures?

<details><summary>Solution</summary>

$I=0.020\times(0.040)^3/12=1.07\times10^{-7}$ m$^4$. $\delta=FL^3/(3YI)=200/(3\times2.13\times10^4)=3.1\times10^{-3}$ m. **$3.1$ mm**.

</details>

#### Section D · Comprehensive long-form

### P27 · 9 marks

(a) From a pair potential of depth $D$ and equilibrium spacing $r_0$, derive $Y\sim D/r_0^3$ (5). (b) Estimate $Y$ for $D=4$ eV, $r_0=2.0$ Å, and compare with steel's $2\times10^{11}$ Pa (4).

<details><summary>Solution</summary>

(a) $F=U''s$ per bond, area per chain $\sim r_0^2$, strain $s/r_0$, so $Y=U''/r_0$. A well of depth $D$ and width $r_0$ has $U''\sim D/r_0^2$, hence $Y\sim D/r_0^3$. (b) $D=6.4\times10^{-19}$ J, $r_0^3=8\times10^{-30}$ m$^3$, $Y\sim8\times10^{10}$ Pa. Steel is two to three times stiffer: same order, a somewhat deeper or narrower well. Marks: force and area 2, strain 1, curvature estimate 2, arithmetic 2, comparison with the order stated 2.

</details>

### P28 · 9 marks

(a) Explain why a symmetric interatomic well gives no thermal expansion (3). (b) Show that an asymmetric well gives $\alpha\sim k_B/(2D)$, and evaluate it for a $3$ eV bond (6).

<details><summary>Solution</summary>

(a) A symmetric well has $\langle r\rangle=r_0$ at every amplitude; vibration widens the motion equally both ways and the mean does not drift. (b) With $U=\tfrac12 ks^2+\tfrac16\gamma s^3$ and $\gamma<0$ (softer outward), the classical average is $\langle s\rangle=-\gamma k_B T/(2k^2)$, so $\alpha=-\gamma k_B/(2r_0 k^2)$. Estimating $|\gamma|\sim k/r_0$ and $k\sim D/r_0^2$ leaves $\alpha\sim k_B/(2D)$. For $D=3$ eV, $k_B/D=2.9\times10^{-5}$ K$^{-1}$ and $\alpha\sim1.4\times10^{-5}$ K$^{-1}$, the steel value. Marks: symmetry argument 3, average and the sign 3, collapse to $k_B/D$ and the number 3.

</details>

### P29 · 9 marks

A rod of mass $m=40$ kg and stiffness $k=1.0\times10^5$ N/m hangs vertically. A mass $M=10$ kg falls on its end from $h=1.0$ mm. (a) Write the energy balance including the rod's own weight, stating the shape you assumed (5). (b) Find $\delta$, and the value you would have got with $m=0$ (4).

<details><summary>Solution</summary>

(a) Static shape $u(x)=\delta x/L$: elastic energy $\tfrac12 k\delta^2$, falling mass descends $h+\delta$, rod's centre of mass descends $\delta/2$. So $\tfrac12 k\delta^2=Mg(h+\delta)+\tfrac12 mg\delta$. Valid only if the loading is slow against $L/c$. (b) $\delta=[(M+m/2)g+\sqrt{((M+m/2)g)^2+2kMgh}]/k=(294+326)/10^5=6.2\times10^{-3}$ m. With $m=0$: $2.7\times10^{-3}$ m. The rod's weight, sampled at half the end drop, more than doubles the extension.

</details>

### P30 · 9 marks

(a) Derive the area profile of a rod that carries an end load $W$ plus its own weight at constant stress $\sigma_0$ (5). (b) Compute $\lambda=\sigma_0/(\rho g)$ for steel at $2.5\times10^8$ Pa, and say why no building is this tall (4).

<details><summary>Solution</summary>

(a) $\sigma_0 A(x)=W+\int_0^x\rho g A\,dx'$; differentiate to get $A'=A/\lambda$ with $\lambda=\sigma_0/(\rho g)$, so $A=A_0 e^{x/\lambda}$ and $A_0=W/\sigma_0$. (b) $\lambda=2.5\times10^8/(7800\times9.8)=3.3$ km. A prismatic column cannot stand taller than $\lambda$; the flare removes that particular limit. Real structures stop far earlier by buckling, and a tree by the hydraulic limit, neither of which is a crushing stress.

</details>

### P31 · 9 marks

(a) Integrate $d^2y/dx^2=M/(YI)$ for a cantilever with an end load $F$, from the built-in end, and obtain $\delta=FL^3/(3YI)$ (6). (b) Evaluate $\delta$ for $F=100$ N, $L=1.0$ m, $YI=2.0\times10^4$ N·m$^2$ (3).

<details><summary>Solution</summary>

(a) $M=F(L-x)$. $y'=F(Lx-x^2/2)/(YI)$ after $y'(0)=0$; $y=F(Lx^2/2-x^3/6)/(YI)$ after $y(0)=0$; $y(L)=FL^3/(3YI)$. Marks: moment 1, each integration with its boundary condition 2, tip value 1. (b) $\delta=100/(6.0\times10^4)=1.7\times10^{-3}$ m.

</details>

### P32 · 9 marks

A pinned steel column, radius $1.0$ cm, length $2.0$ m, $Y=2.0\times10^{11}$ Pa, yield stress $2.5\times10^8$ Pa. (a) Compare the Euler load with the yield load (5). (b) The length is halved. Which failure governs now? (4)

<details><summary>Solution</summary>

(a) $I=\pi R^4/4=7.85\times10^{-9}$ m$^4$. $P_{cr}=\pi^2 YI/L^2=3.9\times10^3$ N. Yield load $\sigma_y A=7.9\times10^4$ N. Buckling governs, by a factor of about twenty. (b) $P_{cr}\propto 1/L^2$ rises by $4$, to $1.6\times10^4$ N, still well below yield. Halving the length once does not turn this rod into a strut; it would take another factor of two in length, or a serious thickening, before yield got there first.

</details>

### P33 · 9 marks

A thin closed steel cylinder, inner radius $0.50$ m, wall $5.0$ mm, holds a gauge pressure of $2.0$ MPa. (a) Derive and evaluate the hoop and longitudinal stresses (6). (b) Which crack forms first, and why does the derivation fail for a gun barrel? (3)

<details><summary>Solution</summary>

(a) Diametral cut: $p\cdot2rL=2\sigma t L$, so $\sigma=pr/t=2.0\times10^6\times0.50/5.0\times10^{-3}=2.0\times10^8$ Pa. End-cap cut: $\sigma_L=pr/(2t)=1.0\times10^8$ Pa. (b) Hoop is the larger, so the crack runs along a generator. A gun barrel has $t$ comparable to $r$, the stress is not uniform through the wall, and the thin-wall cut is the wrong free body.

</details>

### P34 · 9 marks

(a) For a rectangular section, show $I/A=h^2/12$ (2). (b) An I-section of equal area and equal overall depth beats this by a factor of about $2$, not $7$. Explain what the factor of $7$ was quietly including (4). (c) Why does the same "put material far from the axis" argument apply to a hollow shaft in torsion? (3)

<details><summary>Solution</summary>

(a) $I=bh^3/12$, $A=bh$, so $I/A=h^2/12$. (b) Comparing an I-profile with a much shallower rectangle credits the depth change, which enters as $h^2$, to the profile. At equal depth the flanges still win, by a factor near $2$, because area at the extremities contributes $Ad^2$ while area at the axis contributes nothing. The larger number is a depth effect wearing the profile's name. (c) $J=\int r^2 dA$ is the same weighting. A hollow shaft of equal mass has the larger $J$, and twists less, for the same reason the flanges deflect less.

</details>

### P35 · 9 marks

A dragline strand has $\sigma_f=1.0\times10^9$ Pa, $Y=1.0\times10^{10}$ Pa, $\rho=1300$ kg/m$^3$ and diameter $3.0$ μm. (a) What mass can it lift (3)? (b) Compare its specific strength and its specific modulus with mild steel, $\sigma_y=2.5\times10^8$ Pa, $Y=2.0\times10^{11}$ Pa, $\rho=7800$ kg/m$^3$ (6).

<details><summary>Solution</summary>

(a) $A=7.1\times10^{-12}$ m$^2$, $F=\sigma_f A=7.1\times10^{-3}$ N, mass $0.72$ g. (b) Specific strength: silk $7.7\times10^5$, steel $3.2\times10^4$, silk ahead by about $24$. Specific modulus: silk $7.7\times10^6$, steel $2.6\times10^7$, steel ahead by about $3$. The strand is the better rope and the worse ruler. Strength and stiffness are different axes; a single "better material" does not exist.

</details>

### P36 · 9 marks

(a) Estimate the longitudinal wave speed in a thin steel rod, and say why the bulk of the same steel is faster (4). (b) Rock with $\rho=2700$ kg/m$^3$ carries P-waves at $6.0$ km/s and S-waves at $3.5$ km/s. Find $G$, and explain what the disappearance of S-waves implies about the material they failed to cross (5).

<details><summary>Solution</summary>

(a) $v=\sqrt{Y/\rho}=\sqrt{2.0\times10^{11}/7800}=5.1$ km/s, sides free. In the bulk the sides cannot contract, the modulus is $B+4G/3$ rather than $Y$, about $1.3$ times larger for steel, and the speed is near $5.8$ km/s. (b) $G=\rho v_S^2=2700\times(3500)^2=3.3\times10^{10}$ Pa. An S-wave is a shear wave and needs $G>0$. A liquid has $G=0$ and cannot carry it, which is why the absence of S-waves from the outer core is read as evidence that the core is fluid.

</details>

## Part 12 · Marking scheme and post-paper audit

| Section | Marks each | Questions | Subtotal |
|---|---:|---:|---:|
| A | 4 | 12 | 48 |
| B | 4 | 8 | 32 |
| C | 5 | 6 | 30 |
| D | 9 | 10 | 90 |
| **Total** | | 36 | **200** |

**Which block each question tested.** A: P1 §3.4, P2 §3.5, P3 §3.6, P4 §3.3, P5 §3.9, P6 §3.8, P7 §3.10, P8 §3.6, P9 E5, P10 §3.7, P11 §3.6, P12 OL6. B: P13 §3.3, P14 §3.9, P15 §3.4, P16 §3.8, P17 §3.10, P18 §3.6, P19 §3.9, P20 OL1–OL2. C: P21 §3.4, P22 §3.6, P23 §3.5, P24 §3.7, P25 §3.8, P26 §3.10. D: P27 OL1, P28 OL2, P29 OL3, P30 OL4, P31 OL5, P32 OL6, P33 OL9, P34 OL7, P35 OL9, P36 OL10. Blocks 2–4, 6 and 10 all appear.

**Diagnostic table.**

| If you lost marks on… | the likely gap | reread |
|---|---|---|
| P1, P15, P21 | $k=YA/L$ and what $A$ actually is | §3.4, T2 |
| P2, P23 | the triangular load | §3.5, D12.12 |
| P3, P8, P11, P18, P22 | expand, then restore; the sign | §3.6, T3 |
| P4, P13, P20 | the interrelations and the bounds on $\sigma$ | §3.3 |
| P5, P14, P29 | energy at the turning point | §3.9, OL3 |
| P6, P16, P25 | $J$, and $J$ per kilogram | §3.8 |
| P7, P17, P26, P31 | the curvature equation, actually integrated | §3.10, OL5 |
| P9 | sag goes as $F^{1/3}$ | E5 |
| P12, P32 | buckling against yield, keep the smaller | OL6 |
| P20, P27, P28 | the well: curvature and asymmetry | OL1, OL2 |
| P33, P35 | a free-body cut on a thin member | OL9 |
| P34 | $I/A$, and holding the depth fixed | OL7 |
| P36 | which modulus goes under the square root | OL10 |

## Part 13 · Formula sheet

| formula | validity |
|---|---|
| $\sigma=F/A$, $\varepsilon=\Delta L/L$, $\gamma$ the shear angle | definitions; stress is not force |
| $Y=\sigma/\varepsilon$, $B=-\Delta p/(\Delta V/V)$, $G=\tau/\gamma$ | linear range, one mode each |
| $\sigma=-\varepsilon_{lat}/\varepsilon_{long}$, and $-1<\sigma<\tfrac12$ | isotropic; bounds from $B>0$, $G>0$ |
| $Y=2G(1+\sigma)=3B(1-2\sigma)$ | isotropic linear solid |
| $k=YA/L$; series $1/k$ adds; parallel $k$ adds | uniform members, rigid joints |
| $\Delta L=\rho gL^2/(2Y)$ | uniform hanging rod, self-weight |
| $\sigma_{th}=Y\alpha\Delta T$ | fully constrained, linear |
| $\Delta L_{free}=\alpha L\Delta T$ | free; not a stress |
| $U=\tfrac12 F\Delta L$, $u=\tfrac12\times$ stress $\times$ strain | linear; loop area is extra loss |
| sudden load: $\Delta=2mg/k$ | released from the slack point |
| drop: $\Delta=\Delta_{st}(1+\sqrt{1+2h/\Delta_{st}})$ | massless rod; add $m$ as in OL3 |
| $\theta=TL/(GJ)$, $J=\pi R^4/2$ solid | circular shaft, linear |
| $M=YI/R$, $\delta=FL^3/(3YI)$ cantilever tip | small slope, end load |
| $P_{cr}=\pi^2 YI/L^2$ | pinned ends, still elastic |
| hoop $\sigma=pr/t$, long $\sigma_L=pr/(2t)$ | thin closed cylinder |
| $A=A_0 e^{x/\lambda}$, $\lambda=\sigma_0/(\rho g)$ | constant-stress rod |
| $Y\sim D/r_0^3$, $\alpha\sim k_B/(2D)$ | pair potential; not rubber |
| $v_{rod}=\sqrt{Y/\rho}$, $v_S=\sqrt{G/\rho}$, $v_P=\sqrt{(B+4G/3)/\rho}$ | thin rod; bulk shear; bulk compression |
| Numbers: $Y_{steel}=2.0\times10^{11}$ Pa, $G_{steel}=8.0\times10^{10}$, $\alpha_{steel}=1.2\times10^{-5}$ K$^{-1}$, $\sigma_{steel}\approx0.29$, $B_{water}=2.2\times10^9$ Pa, yield of mild steel $\sim2.5\times10^8$ Pa | — |

## Part 14 · Checkpoint and hand-off

- [ ] I can say why engineers use stress, and write the four strains.
- [ ] I can read a stress–strain curve as design information, ductile against brittle.
- [ ] I can derive both interrelations and the bounds on $\sigma$.
- [ ] I can do the extension family: end load, self-weight, series, parallel, the straight wire's sag.
- [ ] I can run a thermal-stress problem by expanding free and compressing back, sign included.
- [ ] I can compute a torsion, a rivet, and a cantilever deflection from the curvature equation.
- [ ] I can solve the falling-weight problem by energy, including the factor $2$ and the rod's own mass.
- [ ] I can compare buckling with yield and keep the smaller.
- [ ] I can derive $Y\sim D/r_0^3$ and $\alpha\sim k_B/(2D)$ from one well.
- [ ] I can cut a pressure vessel and a silk strand and get a stress out of each.
- [ ] I can put the right modulus under a wave speed, rod against bulk, P against S.

**What the next chapters inherit.** The shell balance of the hoop-stress cut is the same move as the pressure integration in [[Fluid-mechanics|fluids]]. The energy method is [[Work-energy-power|work and energy]] with a material spring attached. Once $k$ or $C$ is known, the oscillator is [[Simple-harmonic-motion|SHM]]'s. Thermal expansion as a measured fact is [[Heat|heat]]'s; the wave equation is [[Sound-waves|sound]]'s. Nothing here is re-derived in those chapters, and nothing of theirs is re-derived here.

**Open questions now attackable.** How tall can a mountain be? — yield or creep under self-weight, the constant-stress length of OL4 with rock's $\sigma_y$ and $\rho$, cut down further by gravity's variation, which is [[Gravitation|gravitation]]'s. Why a flywheel's rim is the part that bursts — hoop stress from [[Centre-of-mass-momentum|the rotor's]] own centripetal requirement, $\sigma=\rho v^2$, the same cut as OL9 with $p$ replaced by an inertia load. Both are one formula from this chapter plus one from a neighbour.
