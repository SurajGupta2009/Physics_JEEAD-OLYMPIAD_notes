---
title: Fluid Mechanics & Surface Tension
part: 11
slug: fluid-mechanics
source: Cengage MECHANICS 2-compressed.pdf, ch 3 Fluid Mechanics (pp. 3.1-3.69) + ch 4 Properties of Solids and Fluids (viscosity, surface tension, capillarity, pp. 4.20-4.37)
aliases: [fluids, hydrostatics, hydrodynamics, buoyancy, bernoulli, surface tension, viscosity]
tags: [jee-advanced, olympiad, mechanics, fluids]
---

# Fluid Mechanics & Surface Tension — first principles to Olympiad

> [!abstract] How to use this chapter
> Three passes. Pass 1: Parts 0–4 — the pressure field, buoyancy, accelerated fluids, the continuity–Bernoulli pair, viscosity and surface tension, each derived before it is used. Pass 2: Parts 5–9 for exam craft. Pass 3: Parts 10–14 — the Olympiad layer (drainage integrals, the paraboloid three ways, two-drag terminal velocity, Young–Laplace from energy, the tree-height limit), the paper, the sheet, the checkpoint. Every number recomputed; every boxed result carries its validity condition.

## Part 0 · Orientation

### 0.1 What you will be able to do

After this chapter you can: derive the hydrostatic equation from a force balance on a fluid element and use it in layered liquids and manometers; state Pascal's law as a consequence of incompressibility and audit the energy of a hydraulic lift; compute hydrostatic forces on plane, inclined and curved surfaces with pressure diagrams; handle fluids in linearly accelerating and rotating vessels, including the counter-intuitive balloon; derive Archimedes' principle twice, locate the centre of buoyancy and decide floating-body stability with the metacentre; derive the continuity equation and Bernoulli's equation from mass conservation and the work–energy theorem, and police their four validity conditions; run Torricelli, Venturi, pitot, siphon and efflux-range problems; compute momentum-flux forces of jets and draining vessels; use Newton's viscosity law, derive Poiseuille's law by a shell balance, and get terminal velocity from Stokes; estimate Reynolds numbers and name the laminar–turbulent transition; treat surface tension as both force per length and energy per area, derive the excess-pressure results and Jurin's law two ways, and solve the insufficient-tube capillary problem.

### 0.2 The one idea

Fluids carry pressure; pressure differences are forces; viscosity and surface tension matter only when the length scale is small.

### 0.3 Prerequisite self-check

Answers are at the end of each item's block in later parts; if two or more of these fail, revisit the named part first.

1. Can you write Newton's second law for a small element and take its limit to a differential equation? ([[Newtons-laws#Part 3 · Core derivations|Newton's laws §3]])
2. Can you compute work done by a force whose magnitude varies with position? ([[Work-energy-power#Part 3 · Core derivations|WEP §3]])
3. Do you trust that pressure is a scalar, and can you say why a *scalar* can push in a definite direction? (§3.1)
4. Can you find the centre of mass of a composite body, and the torque of a distributed force about a point? ([[Centre-of-mass-momentum#Part 2 · Definitions and bookkeeping|COM §2]])
5. Can you integrate $v\,dv/dx$ type equations and separable first-order ODEs? ([[Kinematics-1d#Part 3 · Core derivations|Kinematics §3]])
6. Do you know what a conservative force is, and the statement of the work–energy theorem including non-conservative work? ([[Work-energy-power#Part 4 · Results, limits and the validity ledger|WEP §4]])
7. Can you estimate orders of magnitude (the Fermi method)? ([[Units-measurements#Part 10 · Olympiad extension|Units §10]])

### 0.4 Numbers to keep

| quantity | value | where it bites |
|---|---|---|
| $g$ | $9.8$ m/s$^2$ | every hydrostatic number |
| $p_0$ (1 atm) | $1.013\times10^5$ Pa | barometers, bubbles, siphons |
| $\rho_{\text{water}}$ | $1000$ kg/m$^3$ | buoyancy, Bernoulli |
| $\rho_{\text{Hg}}$ | $13.6\times10^3$ kg/m$^3$ | manometers |
| water barometer | $\approx 10.3$ m | the siphon height limit |
| $\gamma_{\text{water}}(20^\circ\text{C})$ | $0.0728$ N/m | capillarity, drops |
| $\eta_{\text{water}}(20^\circ\text{C})$ | $1.0\times10^{-3}$ Pa·s | Stokes, Poiseuille, Reynolds |
| $\eta_{\text{air}}(20^\circ\text{C})$ | $1.8\times10^{-5}$ Pa·s | drag estimates |
| contact angle, water–glass | $\approx 0^\circ$ (clean) | meniscus shape, Jurin |
| $B_{\text{water}}$ | $2.2\times10^9$ Pa | compressibility, sound speed |

### 0.5 What this chapter is not

Not a course in the Navier–Stokes equations: viscosity enters through Newton's law, Poiseuille and Stokes, not through the full tensor. Not gas dynamics: the working fluid is incompressible except where the compressibility of water is explicitly estimated (§3.13, §4.7). Surface waves appear only as the shallow-water speed $v=\sqrt{gh}$, which is the bridge to [[String-waves#Part 2 · Definitions and bookkeeping|the shipped string-waves note]]; deep-water dispersion and full wave theory live there.

### 0.6 Cengage coverage map

The floor is *Cengage Mechanics II*, ch 3 Fluid Mechanics (pp. 3.1–3.69) for hydrostatics and hydrodynamics, and the fluid half of ch 4 Properties of Solids and Fluids (pp. 4.20–4.37) for viscosity, surface tension and capillarity. Status: *derived* (proved here from first principles), *stated + used*, *extended beyond book*, or *excluded with reason*.

| Cengage section (ch 3) | What it establishes | Where it lives here | Status |
|---|---|---|---|
| Pressure; some properties of pressure | pressure is isotropic; the hydrostatic equation | §3.1 | derived |
| Measuring pressure | barometer, manometer, gauge vs absolute | §3.2 | derived |
| Pascal's law | pressure transmits undiminished in an enclosed incompressible fluid | §3.2 | derived |
| Measurement of pressure (manometric equations) | step method for multi-liquid columns | §3.2, Q3 | stated + used |
| Pressure diagrams; force on boundaries | triangular load, centre of pressure | §3.3 | derived |
| Force on immersed surface and centre of force | $F=p_c A$, $y_{cp}$ below centroid | §3.3 | derived |
| Hydrostatic forces on inclined surfaces | $\sin\theta$ projection | §3.3, Q5 | derived |
| Force on curved surface | horizontal/vertical components as projections and weights | §3.3, E4 | derived |
| Fluid in uniformly accelerating motion | tilted free surface, $\tan\theta=a/g$ | §3.4 | derived |
| Equipressure lines; modified manometric equation | $\nabla p=\rho(\mathbf{g}-\mathbf{a})$ | §3.4 | extended beyond book |
| Comparison with an accelerated pendulum | plumb-line analogy | §3.4 | stated + used |
| Liquid rotating with constant angular velocity | paraboloid $z=\omega^2 r^2/2g$ | §3.4, OL3 | derived |
| Archimedes' principle; calculation of buoyant force | $F_b=\rho_f V g$ | §3.5 | derived twice |
| Floating body; centre of buoyancy | fraction submerged; line of action | §3.5 | derived |
| Buoyant force in accelerating fluid | $g\to g_{\text{eff}}$; the balloon | §3.4, §3.5 | derived |
| Visualization of flow; streamline; turbulent flow | flow regimes | §3.7 | stated + used |
| Principle of continuity and applications | $Av=$ const from mass conservation | §3.7 | derived |
| Energy associated with a moving liquid | kinetic, pressure, potential heads | §3.8 | derived |
| Bernoulli's equation; other forms; proof | work–energy on a streamtube | §3.8 | derived |
| Venturi meter | flow rate from a constriction | §3.9 | derived |
| Static and dynamic pressure; pitot tube | $p+\tfrac12\rho v^2$ | §3.9 | derived |
| Velocity of efflux: Torricelli | $v=\sqrt{2gh}$ | §3.10 | derived |
| Horizontal range of escaping liquid | $x=2\sqrt{h(H-h)}$ | §3.10, Q13 | derived |
| Force of reaction due to ejection | $F=\rho a v^2$ thrust | §3.11 | derived |
| Solved examples; exercise families | problem shapes | Part 5, Part 6, Part 11 | extended beyond book |

| Cengage section (ch 4, fluid half) | What it establishes | Where it lives here | Status |
|---|---|---|---|
| Viscosity; Newton's formula | $\eta$; velocity gradient | §3.12 | derived |
| Flow in a tube: critical velocity | transition to turbulence | §3.13 | stated + used |
| Viscosity in fluids; similarities to friction | molecular origin; contrast with dry friction | §3.12 | stated + used |
| Units; effect of temperature on viscosity | Poise; liquids vs gases | §3.12 | stated + used |
| Stokes' law; terminal velocity | $6\pi\eta r v$; $v_t$ | §3.13 | derived by dimensions + stated |
| Surface tension; causes; cohesion; adhesion | molecular picture | §3.14 | stated + used |
| Measuring surface tension | force and energy methods | §3.14, OL6 | extended beyond book |
| Surface energy; relation to surface tension | $\gamma$ as energy/area | §3.14 | derived |
| Angle of contact; shape of meniscus | wetting; concave vs convex | §3.14 | derived |
| Excess pressure: plane/concave/convex; drop; bubble; soap bubble | $2\gamma/r$, $4\gamma/r$ | §3.15 | derived |
| Excess pressure in general; Young–Laplace | $\Delta p=\gamma(1/r_1+1/r_2)$ | §3.15, OL5 | stated + OL derived |
| Capillarity; wetting and non-wetting; Jurin | $h=2\gamma\cos\theta/\rho g r$ | §3.16 | derived twice |
| Rise in a capillary of insufficient length | $h$ fixed, $R$ adjusts | §3.16, Q22 | derived |
| Applications and practical applications of capillarity | wicks, plants, blotting | §3.16 | stated + used |
| Solved examples; exercises | problem shapes | Part 5, Part 6 | extended beyond book |

> [!quote] Hand-off
> The elastic half of ch 4 (stress, strain, moduli, bending) is **PART 12's** floor, not this chapter's. The sound-speed formula $v=\sqrt{B/\rho}$ appears here only to *use* the bulk modulus; its life as a wave speed belongs to [[Sound-waves#Part 2 · Derivations|the shipped sound-waves note]].

## Part 1 · Intuition first

**A fluid is matter that cannot keep a shape.** Push a solid sideways and it pushes back with a *shear* force that grows with how far you deform it. Push a fluid sideways and it does not push back at all once it is moving steadily: a fluid at rest cannot sustain shear. That single negative statement is the whole of hydrostatics. Every force a static fluid exerts on a surface is perpendicular to that surface, which is exactly what "pressure" means.

**Pressure is depth, not volume.** Stand behind a dam and what stresses the concrete is the depth of water, never the size of the reservoir: a thin vertical tube of water ten metres high presses the bottom exactly as hard as the ocean at ten metres. This is the hydrostatic paradox, and it is why the dam in a drawing always gets thicker toward its base — the pressure triangle grows linearly with depth.

**Buoyancy is the fluid's memory of itself.** Remove a parcel of water from a swimming pool and the hole stays where it was: the surrounding water was holding that parcel up with a force equal to its weight. Put anything else into the same hole and the surrounding water, unaware of the substitution, pushes with the *same* force. That is Archimedes, in one image, before any algebra.

**Flow trades pressure for speed.** Where a stream narrows it speeds up (the same water must get through), and where it speeds up the sideways push on the walls drops. Blowing between two hanging sheets of paper pulls them together; a pitot tube reads the speed of an aircraft by letting the air stagnate and measuring the pressure it recovers. The trade is exact as long as the flow is steady, smooth, incompressible and followed along one streamline — and it fails, spectacularly and instructively, the moment any of those four is broken.

**Viscosity is internal friction with a different temperament.** Honey resists being *stirred*, not being *pushed*: viscous forces oppose relative motion between layers and vanish at rest. That is why a raindrop does not keep accelerating — the air's viscous drag grows until it balances gravity and the drop cruises at terminal velocity, which is also why drizzle falls gently while hailstones are dangerous.

**Surface tension is the skin that isn't a skin.** Molecules inside a liquid are pulled equally in all directions by their neighbours; molecules at the surface are pulled only inward and sideways, so the surface behaves like a stretched membrane that tries to shrink. A dewdrop rounds itself; a water strider stands on a dented but unbroken surface; water climbs a thin glass tube because glass attracts water more strongly than water attracts itself. Halve the tube radius and the climb doubles — which is the whole of capillarity in one sentence.

> [!tip] Insight
> The single length scale that decides whether the "skin" and the "internal friction" matter is tiny: a millimetre. Above it, pressure and inertia run the show and you may set $\gamma=0$ and $\eta=0$. Below it, drops, bubbles, menisci and creeping flows appear. Most exam traps in this chapter are exactly the mistake of applying the wrong scale's physics.

## Part 2 · Definitions and bookkeeping

| symbol | meaning | SI unit |
|---|---|---|
| $p$ | pressure (isotropic normal force per area) | Pa = N/m$^2$ |
| $p_0$ | atmospheric pressure | $1.013\times10^5$ Pa |
| $\rho$ | mass density | kg/m$^3$ |
| $h$, $y$ | depth below free surface; height coordinate | m |
| $\gamma$ | surface tension (force/length = energy/area) | N/m = J/m$^2$ |
| $\eta$ | coefficient of viscosity | Pa·s (= 10 poise) |
| $Q$ | volume flow rate | m$^3$/s |
| $A$ | cross-sectional area of a stream or pipe | m$^2$ |
| $v$ | flow speed | m/s |
| $F_b$ | buoyant force | N |
| $V$ | displaced volume | m$^3$ |
| $g_{\text{eff}}$ | $\lvert\mathbf{g}-\mathbf{a}\rvert$ in an accelerated vessel | m/s$^2$ |
| $\theta$ | contact angle, measured *through the liquid* | rad or deg |
| $r$ | radius of tube, drop or bubble | m |
| $\text{Re}$ | Reynolds number $\rho v D/\eta$ | dimensionless |

> [!note] Definition
> **Pressure at a point** is the limit $p=\lim_{\Delta A\to 0}\Delta F/\Delta A$ of the normal force per area on a small surface, and hydrostatics' first theorem (§3.1) is that this limit is the same for every orientation of the surface — pressure is a scalar.

**Sign conventions, fixed once.** Depth $h$ is measured downward from the free surface; $p=p_0+\rho g h$ then needs no sign gymnastics. Gauge pressure means $p-p_0$; absolute pressure means $p$. In manometers, going *down* a column *adds* $\rho g h$ and going *up* subtracts it, whatever the column's shape. Contact angle $\theta$ is measured through the liquid: $\theta<90^\circ$ is wetting (concave meniscus, capillary rise), $\theta>90^\circ$ non-wetting (convex meniscus, capillary depression, mercury).

**The standing assumptions, each flagged where it is used.**

1. *Incompressible:* $\rho$ constant. Excellent for liquids to hundreds of atmospheres (§3.13 computes the actual correction); wrong for gases above modest pressure differences.
2. *Non-viscous:* $\eta=0$ in Bernoulli applications. Viscous losses are restored in §3.12–3.13 (Poiseuille) and in the traps.
3. *Steady:* the velocity field does not change with time. A draining tank is *not* steady; Torricelli still applies quasi-statically when the hole is small (§3.10 makes the condition quantitative).
4. *Along a streamline:* Bernoulli compares points on one streamline unless the flow is irrotational (§3.8 states the upgrade).
5. *Hydrostatic equilibrium:* the fluid is at rest, or rigidly accelerated/rotated (§3.4), so every element has a single known acceleration.

> [!warning] Condition of validity
> The hydrostatic equation $p=p_0+\rho g h$ requires (a) a connected body of one fluid at rest in one frame and (b) constant $\rho$ over the interval. Across an interface, or across a trapped gas pocket, apply it *piece by piece*: pressure is continuous through the interface, but $\rho$ jumps.

**What is not in this model.** Elastic solids (PART 12), compressible flow and shocks ([[Sound-waves|sound waves]]), full turbulence theory (only the Reynolds criterion here), deep-water waves ([[String-waves|string waves]]), and thermodynamics of fluids ([[Thermodynamics|thermodynamics]] owns the equation of state).

> [!abstract] DIAGRAM D11.1 · The pressure–depth graph for a two-layer liquid
> *Show:* depth $h$ on the vertical axis (downward), pressure $p$ on the horizontal; a straight line of slope $\rho_1 g$ from $p_0$ at the surface to the interface at $h_1$, then a steeper straight line of slope $\rho_2 g$ below it; the kink at the interface circled with the label "slope changes because $\rho$ changes; $p$ itself is continuous".
> *Search:* "pressure depth graph two liquids interface kink hydrostatic"
> *Used in:* §3.1 and Q2.

## Part 3 · Core derivations

### 3.1 Why pressure is a scalar, and the hydrostatic equation

Take a tiny wedge of fluid at rest: two faces of area $A$ perpendicular to $x$ and to $y$, and a slanted face of area $A/\cos\phi$ at angle $\phi$. Let the pressures on the three faces be $p_x$, $p_y$, $p_\phi$. Force balance on the wedge (mass $m\to0$) in $x$ and $y$:

$$
p_x A - p_\phi \frac{A}{\cos\phi}\sin\phi\cdot\frac{\cos\phi}{\sin\phi}\sin\phi = p_x A - p_\phi A \tan\phi \sin\phi/\tan\phi
$$

That clumsy route hides the point; do it cleanly. The slanted face's normal makes angle $\phi$ with the $x$-axis, so its force components are $p_\phi (A/\cos\phi)\cos\phi=p_\phi A$ in $x$ and $p_\phi (A/\cos\phi)\sin\phi=p_\phi A\tan\phi$ in $y$. Balance:

$$
x:\quad p_x A = p_\phi A \quad\Rightarrow\quad p_x = p_\phi,
$$

$$
y:\quad p_y A\tan\phi = p_\phi A\tan\phi + m g \quad\Rightarrow\quad p_y = p_\phi + m g/(A\tan\phi).
$$

Shrink the wedge ($m\propto$ volume $\to 0$ faster than areas): the gravity term dies and $p_x=p_y=p_\phi$ for *every* $\phi$.

> [!info] Why
> The weight term is volume-proportional ($\sim \ell^3$) while the pressure forces are area-proportional ($\sim\ell^2$); in the limit $\ell\to0$ weight is negligible of higher order. That is the entire reason pressure at a point has no direction.

**The hydrostatic equation.** Now a thin horizontal slab of fluid, thickness $dy$, area $A$, height coordinate $y$ (up). Forces: $p(y)A$ up, $p(y+dy)A$ down, weight $\rho g A\,dy$ down:

$$
p(y)A - p(y+dy)A - \rho g A\,dy = 0 \quad\Rightarrow\quad \frac{dp}{dy}=-\rho g. \qquad (3.1)
$$

With $\rho$ constant and $h$ measured down from the free surface:

$$
p = p_0 + \rho g h. \qquad (3.2)
$$

> [!warning] Condition of validity
> Eq. (3.2) needs $\rho$ constant over $h$ and one connected static fluid. For air over kilometres, integrate (3.1) with $\rho(p)$ from the ideal gas law instead ([[Thermodynamics#Part 3 · Core derivations|thermodynamics §3]]).

> [!success] Check
> Units: $[\rho g h]=$ (kg/m$^3$)(m/s$^2$)(m) $=$ kg/(m·s$^2$) $=$ N/m$^2$ ✓. Limit $\rho\to0$ (a gas pocket) gives $p=p_0$: pressure does not change across a negligible-density layer ✓.

**The paradox, dissolved.** Eq. (3.2) contains depth only. Three vessels of different shapes connected at the bottom hold the same level (communicating vessels): if any one had higher $p$ at the shared bottom, the fluid would flow until it did not. The total *weight* of water differs, but the bottom also receives forces from the slanted walls, and those vertical components supply exactly the missing or surplus weight.

> [!abstract] DIAGRAM D11.2 · The hydrostatic paradox vessels
> *Show:* three vessels on a common base pipe with a valve: a cylinder, a funnel widening upward, a funnel narrowing upward; equal water levels dashed across all three; arrows on the slanted walls of the widening vessel pointing perpendicular to the wall with their upward vertical components highlighted; caption "same level, same bottom pressure; the walls carry the weight difference".
> *Search:* "hydrostatic paradox three vessels same height different shapes"
> *Used in:* §3.1 and C3.

### 3.2 Measuring pressure: barometer, manometer, Pascal

**Barometer.** Invert a mercury-filled tube in a mercury dish. Above the column is (near) vacuum, $p\approx0$; at the dish, $p_0$. Eq. (3.2) across the column: $p_0=\rho_{\text{Hg}} g h$, so $h=1.013\times10^5/(13.6\times10^3\times9.8)=0.760$ m. The same argument with water gives $h=1.013\times10^5/(1000\times9.8)=10.3$ m — the number to remember whenever a siphon or a well pump is proposed.

**Manometers and the step method.** To find a trapped gas pressure, walk from one open end to the other, adding $\rho g h$ going down and subtracting going up, switching $\rho$ at each interface. The result depends only on the *vertical* heights, never on tube shapes or horizontal runs, because $p$ varies only with depth (Eq. 3.1).

**Pascal's law.** Enclose an incompressible fluid and change the pressure at one piston by $\Delta p$. Any other point must change by the same $\Delta p$, else Eq. (3.1) with unchanged $\rho$ and $g$ would be violated at the second point after the change settled. Consequence: the hydraulic lift. Small piston area $a$, large $A$: force ratio $F_2/F_1=A/a$, but stroke ratio $d_2/d_1=a/A$, so $F_1 d_1=F_2 d_2$ — the lift is a lever in pressure clothing and conserves energy exactly.

> [!success] Check
> Hydraulic lift energy audit: $W_1=F_1 d_1$, $W_2=F_2 d_2$, $F_2=F_1 A/a$, $d_2=d_1 a/a\cdot(a/A)=d_1 a/A$; product $F_2 d_2=F_1 d_1$ ✓. No free lunch.

> [!abstract] DIAGRAM D11.3 · The hydraulic press with the piston-displacement trade
> *Show:* two connected cylinders, small piston $a$ pushed down $d_1$ with $F_1$, large piston $A$ rising $d_2\ll d_1$ under load $F_2$; shaded equal volumes $a d_1 = A d_2$; labels $F_2=F_1 A/a$ and $W_1=W_2$.
> *Search:* "hydraulic press pistons force multiplication displacement trade diagram"

### 3.3 Pressure diagrams and forces on surfaces

**Plane vertical surface.** Pressure grows linearly with depth, so the load on a dam face of width $w$ and depth $H$ is a triangle: total force $F=\int_0^H \rho g h\, w\, dh=\tfrac12 \rho g H^2 w=\rho g (H/2)(wH)=p_c A$ — the centroid-pressure rule $F=p_c A$. The resultant acts not at mid-depth but at the triangle's centroid, $2H/3$ down: the *centre of pressure*.

**Inclined plane at angle $\theta$.** Depth is $h=s\sin\theta$ where $s$ runs along the plate; every force element scales by the same depth, so $F=p_c A$ still holds with $p_c$ at the centroid depth, and the centre of pressure lies below the centroid by $I_c/(A h_c)$ measured along the plate's slope projection; for a rectangle from the surface, again $2/3$ of the slant length.

**Curved surface.** Decompose. The horizontal force on a curved gate equals the force on its *vertical projection* (every horizontal pressure element acts on the same projected area). The vertical force equals the weight of fluid *directly above* the surface, taken positive downward if fluid rests above, or the weight of the *imagined* fluid that would fill above it (upthrust) if the surface holds fluid from below. Combine as vectors; the line of action passes through the appropriate centres.

> [!info] Why
> Both rules are just Eq. (3.1) integrated componentwise: horizontal elements at a given depth are identical to those on the flat projection at that depth, and the vertical balance on the fluid column above the surface involves only its weight and the end pressures.

> [!abstract] DIAGRAM D11.4 · Force on a curved gate by projection
> *Show:* a quarter-circle gate holding water on its convex side; left panel: horizontal arrows integrated to $F_H$ acting on the vertical projected rectangle; right panel: the shaded water column above the gate whose weight is $F_V$; the vector sum $F$ drawn through the hinge with its angle.
> *Search:* "hydrostatic force curved surface horizontal vertical components quarter circle gate"
> *Used in:* §3.3 and E4.

### 3.4 Accelerated and rotating fluids: one equation for all of it

Give the vessel acceleration $\mathbf{a}$. In the vessel's frame each fluid element of mass $m$ feels gravity $m\mathbf{g}$ and pseudo force $-m\mathbf{a}$, so the effective gravity is $\mathbf{g}_{\text{eff}}=\mathbf{g}-\mathbf{a}$, and *hydrostatics in that frame* is unchanged: surfaces of constant pressure are perpendicular to $\mathbf{g}_{\text{eff}}$, and $p$ grows along $-\mathbf{g}_{\text{eff}}$ at rate $\rho\lvert\mathbf{g}_{\text{eff}}\rvert$.

**Linear acceleration $a$ horizontal.** The free surface tilts so that its normal is along $\mathbf{g}_{\text{eff}}$:

$$
\tan\theta = \frac{a}{g}. \qquad (3.3)
$$

Equipressure lines are parallel to the tilted surface. A plumb bob hangs along $\mathbf{g}_{\text{eff}}$ too — the accelerated-fluid/accelerated-pendulum comparison the book makes: both define "down" as $-\mathbf{g}_{\text{eff}}$. The *modified manometric equation* is the step method with $\mathbf{g}\to\mathbf{g}_{\text{eff}}$, adding $\rho g_{\text{eff}} h$ along $-\mathbf{g}_{\text{eff}}$.

> [!tip] Insight
> The helium balloon in a braking car leans *forward*, toward the windscreen, and in an accelerating car leans forward into the acceleration — the opposite of a hanging strap. Reason: buoyancy points along $-\mathbf{g}_{\text{eff}}$ (away from the effective "down"), and the lighter-than-air balloon is pushed the way the air is pushed out of. The air piles up at the back; the balloon goes to the front.

**Rotating vessel, angular speed $\omega$.** In the rotating frame, element at radius $r$ needs centripetal acceleration, i.e. feels pseudo force $\rho\,\omega^2 r$ per volume outward. Balance on a surface element: $\partial p/\partial r=\rho\omega^2 r$ and $\partial p/\partial z=-\rho g$. Along the free surface $dp=0$:

$$
\frac{dz}{dr}=\frac{\omega^2 r}{g}\quad\Rightarrow\quad z(r)=z_0+\frac{\omega^2 r^2}{2g}. \qquad (3.4)
$$

The free surface is a paraboloid. (OL3 derives it three independent ways.)

> [!abstract] DIAGRAM D11.5 · The rotating fluid's paraboloid
> *Show:* a cylinder of liquid spinning at $\omega$; the parabolic free surface $z=z_0+\omega^2 r^2/2g$; a fluid element at radius $r$ with the outward pseudo-force arrow $\rho\omega^2 r$ and downward gravity arrow; the tangent to the surface drawn with slope $\omega^2 r/g$; dashed level lines below.
> *Search:* "rotating liquid paraboloid free surface derivation"
> *Used in:* §3.4 and OL3.

### 3.5 Buoyancy, twice

**First derivation (pressure difference).** A vertical cylinder of area $A$, height $L$, fully submerged at top depth $h_1$. Top face pushed down with $p_1 A$, bottom pushed up with $p_2 A$: $F_b=(p_2-p_1)A=\rho_f g L A=\rho_f V g$.

**Second derivation (the hole argument).** The fluid that *used to occupy* the volume was in equilibrium, so the surrounding fluid's resultant on that volume was exactly its weight $\rho_f V g$ upward, through its centre of mass. The surroundings do not know the parcel was replaced: same surface, same pressures, same resultant. Hence any body in that hole feels $F_b=\rho_f V g$ acting at the *centre of buoyancy* — the centroid of the displaced volume.

$$
F_b = \rho_f V_{\text{disp}}\, g. \qquad (3.5)
$$

**Floating.** Equilibrium $F_b=mg$ gives $\rho_f V_{\text{disp}}=\rho_b V$, so the submerged fraction is $V_{\text{disp}}/V=\rho_b/\rho_f$ — an iceberg shows about $0.92/1.03\approx 0.89$ of itself below sea water.

**Stability.** For a floating body the weight acts at $G$, the buoyancy at $B$ (centroid of the *submerged* part, which moves when the body heels). Tilt slightly: if the new buoyancy line crosses the symmetry axis above $G$ at the *metacentre* $M$, the couple restores. The metacentric height:

$$
GM = \frac{I}{V} - \text{(distance } BG\text{)},\qquad BM=\frac{I}{V}, \qquad (3.6)
$$

with $I$ the second moment of the waterline area about the tilt axis and $V$ the displaced volume. Wide waterline, shallow draft: stable barge. A fully submerged body has fixed $B$: stable only if $B$ is below $G$.

> [!info] Why
> Heeling changes the submerged wedge: extra volume on one side, missing on the other, a couple of moment $\rho_f g\, x^2\, dA \cdot\theta$ integrated over the waterline, i.e. $\rho_f g I\theta$. That restoring moment equals $F_b\cdot BM\cdot\theta$, giving $BM=I/V$.

> [!success] Check
> Limit: a barge with huge beam has $I\to\infty$, $GM>0$ strongly stable ✓. A pencil floating point-down has tiny $I$ and $G$ above $B$: unstable, as experience confirms ✓.

**Buoyancy in an accelerating fluid.** Replace $g$ by $g_{\text{eff}}=\lvert\mathbf{g}-\mathbf{a}\rvert$ everywhere in (3.5): both the weight and the buoyancy scale, so the *fraction submerged is unchanged* in a lift accelerating vertically, but a pendulum-like tilt appears for horizontal $\mathbf{a}$ (the balloon case of §3.4).

> [!abstract] DIAGRAM D11.6 · Floating body: $G$, $B$, $M$ and the righting moment
> *Show:* a hull cross-section heeled by small $\theta$; weight arrow down at $G$, buoyancy arrow up at shifted $B'$; the buoyancy line extended to meet the axis at $M$ above $G$; the restoring couple arc; a second small sketch of the submerged body case with $B$ fixed and $G$ below required.
> *Search:* "metacentre metacentric height ship stability diagram G B M"
> *Used in:* §3.5 and Q8.

### 3.6 The melting-ice family (with the correct answer for each case)

An ice cube floats in water; it melts. Does the level change? The displaced mass equals the ice mass; the meltwater has exactly that mass and exactly the water's density, so it occupies exactly the displaced volume: **level unchanged**, in fresh water. In *salt* water the ice displaced volume $m/\rho_{sw}$; the melt (fresh) occupies $m/\rho_{fw}>m/\rho_{sw}$: **level rises**. If the ice holds a *stone* (denser than water): while embedded, the stone's share of displacement is $m_s/\rho_w$; after melting the stone sits on the bottom displacing only $m_s/\rho_{stone}<m_s/\rho_w$: **level falls**. If the ice holds an *air bubble*: the bubble's mass is negligible both before and after: **unchanged**.

> [!danger] Trap
> The family is decided by one comparison only: compare the volume the extra object displaces *while floating* (mass-based, $m/\rho_{\text{fluid}}$) with the volume it displaces *after melting* (geometry-based if it sinks). Every variant is that one sentence with different densities.

**C1 — concept check.** A beaker of water on a balance reads $W$. You dip a hanging metal block (not touching the bottom) halfway in. What does the balance read now, and why, without computing any force on the block?

<details><summary>Solution</summary>

$W+\rho_w V_{\text{sub}} g$: by Newton's third law the water feels the reaction of the buoyant force; equivalently the water level rises as if $V_{\text{sub}}$ of water were added. No free-body of the block needed.

</details>

**C2 — concept check.** Two identical vessels hold water to the same height; one also has a floating wooden block. Which vessel is heavier?

<details><summary>Solution</summary>

Identical. The floating block displaces its own weight of water, so vessel+water+block equals vessel+water-filled-to-same-level.

</details>

**C3 — concept check.** The hydrostatic paradox: which force is *not* equal among the three vessels — on the base, or on the table?

<details><summary>Solution</summary>

On the base, equal (same $p$, same area). On the table, different: the table carries each vessel's actual total weight; the slanted walls' vertical force components reconcile the two.

</details>

**C4 — concept check.** In the rotating vessel, where is the pressure greatest at the bottom?

<details><summary>Solution</summary>

At the rim: $p=p_{\text{centre}}+\tfrac12\rho\omega^2 r^2$ from $\partial p/\partial r=\rho\omega^2 r$, and the deeper liquid column there confirms it.

</details>

### 3.7 Flow language and the continuity equation

A *streamline* is a curve everywhere tangent to the velocity; in steady flow streamlines are the actual paths and never cross. *Steady* means the pattern is fixed in time; *uniform* would mean fixed in space too. Mass conservation on a streamtube between cross-sections $A_1$, $A_2$: in time $\Delta t$ the inflow mass is $\rho A_1 v_1\Delta t$ and outflow $\rho A_2 v_2\Delta t$; steady flow stores nothing between, so with constant $\rho$:

$$
A_1 v_1 = A_2 v_2 = Q. \qquad (3.7)
$$

> [!info] Why
> The derivation is bookkeeping, not dynamics: mass cannot accumulate in a fixed streamtube segment under steady conditions. That is why continuity holds even where viscosity matters; it is Bernoulli that is the fragile one.

Consequences: a tapering tap-stream thins as it falls ($v$ grows under gravity, $A$ shrinks); a branching pipe splits $Q$ among branches; a river runs fast where shallow.

### 3.8 Bernoulli from the work–energy theorem

Follow a streamtube from section 1 to section 2. Pressures $p_1,p_2$, speeds $v_1,v_2$, heights $y_1,y_2$, cross-sections $A_1,A_2$. In time $\Delta t$ a mass $m=\rho A_1 v_1\Delta t$ enters and the same mass leaves. Work by pressure at the inlet: $W_1=p_1 A_1 v_1\Delta t$; at the outlet the fluid does work against $p_2$: $W_2=-p_2A_2v_2\Delta t$; gravity does $-mg(y_2-y_1)$. Work–energy theorem on the segment (the interior is unchanged in steady flow, so only the end slugs change their state):

$$
p_1 A_1 v_1\Delta t - p_2 A_2 v_2 \Delta t - m g (y_2-y_1) = \tfrac12 m v_2^2 - \tfrac12 m v_1^2.
$$

Divide by the volume $A_1 v_1 \Delta t=A_2 v_2\Delta t$:

$$
p_1 + \tfrac12\rho v_1^2 + \rho g y_1 = p_2 + \tfrac12\rho v_2^2 + \rho g y_2. \qquad (3.8)
$$

> [!warning] Condition of validity — the four gates
> (1) **Steady** flow; (2) **incompressible** $\rho$; (3) **non-viscous** (no internal friction losses — Poiseuille is the viscous correction, §3.12); (4) **along one streamline**. If the flow is additionally irrotational, the constant becomes the same on every streamline and (3.8) may be used across streamlines.

> [!tip] Insight
> Bernoulli is energy conservation per volume: $p$ is the flow-work term, $\tfrac12\rho v^2$ the kinetic density, $\rho g y$ the potential density. Reading it as "fast means low pressure" is correct only when the height term is equal and nothing else absorbs the difference.

**Heads.** Divide (3.8) by $\rho g$: pressure head $p/\rho g$, velocity head $v^2/2g$, elevation head $y$ — the book's "energy associated with a moving liquid" is this ledger, and every friction loss appears as a drop in total head.

> [!abstract] DIAGRAM D11.7 · The streamtube used for the Bernoulli derivation
> *Show:* a curved streamtube narrowing from $A_1$ (left, low, slow, wide arrows) to $A_2$ (right, high, fast, thin arrows); the two end slugs of length $v_1\Delta t$, $v_2\Delta t$ shaded; pressure arrows $p_1$ pushing in, $p_2$ pushing back; heights $y_1,y_2$ from a datum line.
> *Search:* "Bernoulli derivation streamtube work energy diagram"

### 3.9 Bernoulli's applications, each with its gate checked

**Venturi meter.** A constriction in a horizontal pipe. Continuity $v_2=v_1 A_1/A_2$ into (3.8):

$$
p_1-p_2=\tfrac12\rho v_1^2\left(\frac{A_1^2}{A_2^2}-1\right),\qquad
Q=A_1\sqrt{\frac{2(p_1-p_2)}{\rho\left(A_1^2/A_2^2-1\right)}}. \qquad (3.9)
$$

The manometer reads $p_1-p_2$; the gates: steady, incompressible, short device so viscous loss is a small calibration correction.

**Pitot tube and static/dynamic pressure.** A tube facing the flow stagnates it ($v=0$ at the mouth): it reads the *total* pressure $p+\tfrac12\rho v^2$; a wall tap reads the *static* pressure $p$; the difference is the *dynamic* pressure, so

$$
v=\sqrt{\frac{2\,\Delta p}{\rho}}. \qquad (3.10)
$$

**The siphon and its height limit.** A tube over a rim drains a vessel because the outlet leg's water column outweighs the inlet leg's. Speed at the outlet is Torricelli-like, $v=\sqrt{2g\Delta h}$ with $\Delta h$ the level difference. But at the top the pressure is $p_{\text{top}}=p_0-\rho g h_{\text{top}}-\tfrac12\rho v^2$; the column breaks (water cavitates near its vapour pressure) when $p_{\text{top}}\to0$, i.e. $h_{\text{top}}\lesssim 10.3$ m minus the velocity-head term. *Assuming a siphon works at any height is the classic trap.*

> [!danger] Trap
> "Suction lifts water" is wrong language: nothing pulls. The atmosphere pushes the supply up the rising leg, and it can push at most $\sim p_0/\rho g\approx10.3$ m of water column.

> [!abstract] DIAGRAM D11.8 · The siphon with the pressure at its highest point
> *Show:* a vessel, a bent tube over the rim, outlet below the level; the top point labelled with $p_{\text{top}}=p_0-\rho g h-\tfrac12\rho v^2$; a gauge sketch showing $p_{\text{top}}$ approaching zero as $h\to10.3$ m; flow arrows.
> *Search:* "siphon maximum height limit pressure at top diagram"

### 3.10 Torricelli, range of the escaping liquid, and quasi-steadiness

A hole at depth $h$ in a tank of level $H$ above the floor of the tank. Bernoulli between surface (speed $\approx0$ if $a\ll A$) and hole: $v=\sqrt{2gh}$ — **Torricelli**. The jet then falls as a projectile from height $H-h$:

$$
x = v t = \sqrt{2gh}\sqrt{2(H-h)/g} = 2\sqrt{h(H-h)}. \qquad (3.11)
$$

Symmetric in $h\leftrightarrow H-h$: holes equally above and below mid-depth land at the same spot; maximum range $x_{\max}=H$ at $h=H/2$.

> [!warning] Condition of validity
> Quasi-steady: the level falls at $V_{\text{level}}=v\,a/A$, negligible against $v$ when $a/A\ll1$. If the hole is not small, the surface speed enters (continuity) and (3.11) must use both speeds from (3.8) — OL1 does exactly this for the drainage *time*.

> [!abstract] DIAGRAM D11.9 · The draining tank with two equal-range holes
> *Show:* a tank, level $H$; holes at $h$ and $H-h$ with both jets drawn as parabolas landing at the same point $x=2\sqrt{h(H-h)}$; the mid-depth jet drawn reaching $x=H$; axis labels.
> *Search:* "Torricelli theorem two holes same range tank diagram"

### 3.11 Momentum flux: jets, thrust and the reaction of ejection

Fluid of density $\rho$ leaving an orifice of area $a$ at speed $v$ carries momentum per time $\dot p=\rho a v\cdot v=\rho a v^2$. The vessel feels the reaction $F=\rho a v^2$ opposite to the jet — the force that spins a sprinkler arm and pushes a punctured can backwards. The same flux idea gives the force of a jet on a plate: mass rate $\rho a v$ meets the plate; a stationary flat plate normal to the jet destroys the normal momentum, $F=\rho a v^2$; a plate moving away at $u$ sees relative speed $v-u$, so $F=\rho a (v-u)^2$; an inclined or curved vane redirects the momentum and the force is the vector change of $\rho a v\,\mathbf{v}$ per time.

> [!info] Why
> Thrust is not pressure at the hole times area: near the hole the streamlines converge (vena contracta) and the pressure there is not $p_0+\rho g h$. The momentum-flux route never needs the messy near-field — it counts what leaves.

> [!abstract] DIAGRAM D11.10 · A jet striking a plate: flat, inclined, moving
> *Show:* three panels: (a) jet normal to a fixed plate, splash arrows radial, $F=\rho a v^2$; (b) jet on a plate tilted $\theta$, the tangential split arrows, normal force $\rho a v^2\cos\theta$ component labelled; (c) jet chasing a plate moving at $u$, relative speed $v-u$ marked, $F=\rho a (v-u)^2$.
> *Search:* "force of water jet on flat inclined moving plate momentum"
> *Used in:* §3.11 and Q16.

### 3.12 Viscosity: Newton's law and Poiseuille by shell balance

Between two parallel plates, the lower fixed, the upper dragged at $v$ across gap $d$, the fluid forms a linear velocity profile; the force per area needed is

$$
\frac{F}{A}=\eta\frac{dv}{dy}, \qquad (3.12)
$$

defining $\eta$ (Pa·s; 1 poise $=0.1$ Pa·s). Liquids: $\eta$ falls as temperature rises (cohesion weakens). Gases: $\eta$ *rises* with temperature (momentum carried by faster molecules) — the contrast with dry friction the book flags: viscous force needs *relative motion*, vanishes at rest, and depends on speed gradient, not on normal force.

**Poiseuille by the force balance on a cylindrical shell.** Steady laminar flow in a horizontal pipe of radius $R$, length $L$, pressure difference $\Delta p$. A coaxial fluid cylinder of radius $r$ moves at constant speed: pressure force $\Delta p\,\pi r^2$ forward balances viscous drag on its side, $-\eta\,(dv/dr)\,2\pi r L$ (the gradient is negative, so written with the sign that gives a positive drag):

$$
\Delta p\,\pi r^2 = -\eta \frac{dv}{dr} 2\pi r L \quad\Rightarrow\quad \frac{dv}{dr}=-\frac{\Delta p}{2\eta L}r.
$$

Integrate with $v(R)=0$ (no slip): $v(r)=\frac{\Delta p}{4\eta L}(R^2-r^2)$ — a paraboloid of velocities. Then

$$
Q=\int_0^R v\,2\pi r\,dr=\frac{\pi R^4 \Delta p}{8\eta L}. \qquad (3.13)
$$

The $R^4$ is the whole story of plumbing: halve a pipe's radius and you need sixteen times the pressure difference for the same flow — "why narrow pipes dominate" any series network, exactly like resistors with $R_{\text{hyd}}=8\eta L/\pi R^4$ adding in series.

> [!abstract] DIAGRAM D11.11 · Poiseuille's parabolic profile with the shell element
> *Show:* a pipe cross-section with the parabolic velocity profile arrows; the coaxial shell of radius $r$ and thickness $dr$ highlighted with the pressure arrows at its ends and the shear arrows on its curved surface; the no-slip wall labelled $v=0$.
> *Search:* "Poiseuille flow parabolic velocity profile pipe derivation"
> *Used in:* §3.12 and Q19.

**Series and parallel pipes.** Series: same $Q$, $\Delta p$ adds; parallel: same $\Delta p$, $Q$ adds. A wide pipe short-circuits a narrow one: with $R$ vs $R/2$ in parallel the narrow carries $1/17$ of the flow.

### 3.13 Stokes, terminal velocity, Reynolds

For a sphere at low speed in a viscous fluid, dimensional analysis forces the drag form: $[F]=[\eta]^a[r]^b[v]^c$ gives $a=b=c=1$, so $F=k\eta r v$; Stokes' computation fixes $k=6\pi$:

$$
F_d = 6\pi\eta r v. \qquad (3.14)
$$

Balance with gravity minus buoyancy, $\tfrac43\pi r^3(\rho-\sigma)g$, for terminal velocity:

$$
v_t=\frac{2 r^2(\rho-\sigma)g}{9\eta}. \qquad (3.15)
$$

**Reynolds number.** The ratio of inertial to viscous forces in a flow scales as

$$
\text{Re}=\frac{\rho v D}{\eta}. \qquad (3.16)
$$

Pipe flow turns turbulent around $\text{Re}\sim2000$–$4000$; Stokes' law itself is reliable only for $\text{Re}\lesssim1$, beyond which the quadratic drag $F\approx\tfrac12 C_d\rho A v^2$ takes over (OL4 treats the crossover).

> [!success] Check
> Raindrop sanity: $r=2$ mm, quadratic regime, $v_t\approx\sqrt{8 r\rho_w g/(3 C_d\rho_a)}\approx 8$–$9$ m/s; the Stokes formula would absurdly give $\sim10^2$ m/s — a signal that $\text{Re}\gg1$ there. Small drizzle $r=0.1$ mm sits near the Stokes side: $v_t\approx1.2$ m/s with (3.15) at $\eta_{air}=1.8\times10^{-5}$: $v_t=2(10^{-4})^2(1000)(9.8)/(9\times1.8\times10^{-5})\approx1.2$ m/s ✓ gentle.

> [!abstract] DIAGRAM D11.12 · Terminal velocity force diagram and the drag regimes
> *Show:* left: a falling sphere with $mg$ down, $F_b$ and $F_d$ up, $a\to0$ labelled; right: drag coefficient vs Reynolds log-log sketch with the Stokes line $C_d=24/\text{Re}$, the plateau $C_d\approx0.44$, and the drag-crisis dip circled.
> *Search:* "drag coefficient versus Reynolds number sphere Stokes regime"

**Compressibility of water, honestly.** $B_{\text{water}}=2.2\times10^9$ Pa; at the ocean floor ($\sim11$ km, $p\approx1.1\times10^8$ Pa) the fractional density rise is $\Delta\rho/\rho=\Delta p/B\approx5\%$ — real, and the reason precise oceanography cares, but small enough that every JEE hydrostatic number may ignore it. The sound-speed link: $v_s=\sqrt{B/\rho}=\sqrt{2.2\times10^9/1000}\approx1480$ m/s, matching measurement; that life of $B$ belongs to [[Sound-waves#Part 2 · Derivations|sound waves]].

### 3.14 Surface tension: two definitions, one quantity

**Definition 1 (force):** $\gamma=F/L$, the force per unit length with which a surface pulls along any line drawn in it, perpendicular to the line, in the surface plane. **Definition 2 (energy):** $\gamma=W/\Delta A$, the work to create unit area. Their equivalence, by a sliding wire frame: pulling the wire by $dx$ against the force $F=\gamma L$ (two surfaces of a film: $2\gamma L$) does $W=2\gamma L\,dx=\gamma\,\Delta A$.

> [!info] Why
> Molecularly, a surface molecule has fewer neighbours and higher potential energy; enlarging the surface promotes molecules up that deficit, costing energy, and the surface's tendency to shrink is the force reading of the same deficit.

**Cohesion and adhesion; contact angle.** At a wall, the liquid surface meets the solid where the resultant of cohesive (liquid pulls liquid) and adhesive (solid pulls liquid) forces on a surface molecule is perpendicular to the surface. Adhesion stronger (water–clean glass): the surface climbs the wall, $\theta<90^\circ$, concave meniscus. Cohesion stronger (mercury–glass): $\theta\approx140^\circ$, convex meniscus, capillary *depression*. Wetting is this single comparison.

> [!abstract] DIAGRAM D11.13 · Meniscus shapes and the contact angle
> *Show:* two tubes side by side: water with concave meniscus, $\theta$ drawn through the liquid below $90^\circ$, adhesion arrows toward the wall; mercury with convex meniscus, $\theta\approx140^\circ$, cohesion arrows; the tangent lines at the contact point emphasised.
> *Search:* "contact angle concave convex meniscus water mercury glass"

### 3.15 Excess pressure across curved surfaces

A spherical drop of radius $r$: cut it by a plane through the centre. The surface-tension ring pulls the hemisphere inward with $\gamma\cdot2\pi r$; the excess pressure $\Delta p$ pushes it outward with $\Delta p\,\pi r^2$:

$$
\Delta p = \frac{2\gamma}{r}\quad(\text{drop, one surface}). \qquad (3.17)
$$

A soap bubble has *two* surfaces: $\Delta p=4\gamma/r$. The factor 2 is the single most-missed point in the book's exercise family. For a general curved surface with principal radii $r_1,r_2$ (stated here; OL5 derives it from energy):

$$
\Delta p=\gamma\left(\frac{1}{r_1}+\frac{1}{r_2}\right). \qquad (3.18)
$$

Plane surface: $r_{1,2}\to\infty$, no excess. Cylindrical film or a saddle: signs of curvature subtract. Consequences used constantly: two connected bubbles — the smaller one empties into the larger (higher pressure); a drop splitting into many droplets needs work input because total area grows; capillary pressure supports liquid columns.

> [!abstract] DIAGRAM D11.14 · Soap-bubble cross-section with the two surfaces
> *Show:* a bubble wall greatly magnified: outer and inner surfaces each carrying $\gamma$, the ring force $2\gamma\cdot2\pi r$ on a hemisphere, excess-pressure arrows $\Delta p=4\gamma/r$ inside; beside it a single-surface drop with $2\gamma/r$; the factor-2 contrast boxed.
> *Search:* "soap bubble excess pressure two surfaces factor two derivation"

### 3.16 Capillarity: Jurin's law, twice, and the short tube

**Force balance.** In a tube of radius $r$ with contact angle $\theta$, the surface pulls the column up along the wall with vertical component $\gamma\cos\theta$ per length, around circumference $2\pi r$; the column's weight is $\rho g h\,\pi r^2$ (meniscus volume neglected at $r\ll h$):

$$
2\pi r\,\gamma\cos\theta=\rho g h\,\pi r^2\quad\Rightarrow\quad h=\frac{2\gamma\cos\theta}{\rho g r}. \qquad (3.19)
$$

**Energy method.** Raising the column by $dh$ trades adhesion for gravity: the surface-energy change per height is $-2\pi r(\gamma_{sg}-\gamma_{sl})=-2\pi r\gamma\cos\theta$ (Young's relation); minimising total energy $U(h)=-2\pi r\gamma\cos\theta\, h+\tfrac12\rho g h^2\pi r^2$ gives the same $h$. (The $\tfrac12$ appears because the column grows from zero: $U_g=\rho g \pi r^2 h\cdot h/2$.)

> [!success] Check
> Numbers: water, $\gamma=0.0728$, $\theta\approx0$, $r=0.1$ mm: $h=2(0.0728)/(1000\cdot9.8\cdot10^{-4})\approx0.149$ m — a hand-span in a tenth-of-a-millimetre tube, which is why blotting paper works and why the same physics caps at about $10$ m even for microscopic pores (pressure side), setting the tree-height problem for OL9.

**Insufficient length.** A tube shorter than $h$ does not overflow: the meniscus radius of curvature $R$ increases until $2\gamma/R\cdot\cos(\text{effective})$ supports the actual column, i.e. $R\,=\,r/\cos\theta$ becomes $R'=2\gamma/(\rho g h')$ with $h'$ the tube length; the liquid adjusts its *curvature*, never spills. $h R = h' R'$ is the working relation at $\theta=0$.

> [!abstract] DIAGRAM D11.15 · Capillary rise in a tube of insufficient length
> *Show:* left: a long tube with full Jurin height $h$ and tight meniscus radius $R=r$; right: a short tube with the meniscus flattened to $R'>r$, same liquid, no overflow; labels $hR=h'R'$.
> *Search:* "capillary tube insufficient length meniscus radius adjustment"
> *Used in:* §3.16 and Q22.

### 3.17 Shallow-water wave speed: the bridge to the wave notes

A gravity wave in depth $h$ with wavelength $\lambda\gg h$: the water moves nearly horizontally, and a crest is a moving bump whose excess height $\eta$ is pushed along by the hydrostatic pressure difference $\rho g\eta$. Continuity and momentum on the moving bump (worked fully in OL10) give

$$
v=\sqrt{gh}. \qquad (3.20)
$$

Validity: shallow water, small amplitude, inviscid. This is the chapter's single deliberate hand-off into [[String-waves|the shipped wave notes]]: the same continuity-plus-momentum machinery that produced (3.7) and (3.8) produces a wave speed, showing that the "fluid block" and the "wave block" of the syllabus are one method.

> [!quote] Hand-off
> Deep-water dispersion ($v=\sqrt{g\lambda/2\pi}$), dispersion relations generally, and impedance of wave media live in [[String-waves#Part 3 · Core derivations|string waves §3]]; the sound-speed route $\sqrt{B/\rho}$ in [[Sound-waves#Part 2 · Derivations|sound waves §2]].

**C5 — concept check.** Why does a narrowing falling water stream from a tap eventually break into droplets?

<details><summary>Solution</summary>

Continuity thins it as $v$ grows; below a millimetre-scale radius surface tension's inward pull $2\gamma/r$ beats the stream's inertia and the cylinder is unstable to necking (Plateau–Rayleigh). Scale argument: the skin wins at small $r$.

</details>

**C6 — concept check.** In Poiseuille flow, what carries the "missing" pressure at the wall?

<details><summary>Solution</summary>

The wall shear stress $\eta\lvert dv/dr\rvert_{r=R}=\Delta p R/2L$: the pressure force on each fluid shell is exactly balanced by shear, all the way to the wall.

</details>

**C7 — concept check.** A U-tube holds two immiscible liquids; the interface is level only in the heavier-liquid arm. How do the free levels compare?

<details><summary>Solution</summary>

Pressures at the interface must match: $\rho_1 g h_1=\rho_2 g h_2$ measured from the interface; the lighter liquid's column stands taller. The interface itself is not a level surface across two fluids.

</details>

**C8 — concept check.** Does the buoyant force on a fully submerged ball change as it sinks deeper in an incompressible liquid?

<details><summary>Solution</summary>

No, to the extent that both $\rho_f$ and the ball's volume are constant; the pressure *difference* top–bottom is $\rho g L$ at any depth because the gradient (3.1) is depth-independent.

</details>

## Part 4 · Results, limits and the validity ledger

| result | formula | validity | limit check |
|---|---|---|---|
| hydrostatic pressure | $p=p_0+\rho g h$ | one static fluid, constant $\rho$ | $\rho\to0\Rightarrow p=p_0$ |
| Pascal lift | $F_2=F_1 A/a$ | incompressible, sealed | $A=a\Rightarrow F_2=F_1$ |
| plane force | $F=p_c A$ | plane surface | centroid depth $0$ gives $0$ |
| centre of pressure, rectangle from surface | $2H/3$ | vertical rectangle | matches triangle centroid |
| tilt of accelerated surface | $\tan\theta=a/g$ | rigid acceleration, settled | $a\to0\Rightarrow\theta\to0$ |
| rotating surface | $z=z_0+\omega^2r^2/2g$ | rigid rotation, settled | $\omega\to0$ flat |
| Archimedes | $F_b=\rho_f V g$ | fluid in hydrostatic equilibrium | $\rho_f\to0$ (air) negligible |
| float fraction | $V_s/V=\rho_b/\rho_f$ | floating at rest | $\rho_b=\rho_f\Rightarrow$ fully submerged, neutral |
| metacentric height | $BM=I/V$ | small heel | $I\to\infty$ stable |
| continuity | $Av=\text{const}$ | steady, incompressible | $A\to\infty\Rightarrow v\to0$ |
| Bernoulli | $p+\tfrac12\rho v^2+\rho g y=\text{const}$ | the four gates of §3.8 | $v=0$ reduces to (3.2) |
| Torricelli | $v=\sqrt{2gh}$ | small hole, quasi-steady | $h\to0\Rightarrow v\to0$ |
| efflux range | $x=2\sqrt{h(H-h)}$ | as Torricelli + projectile fall | $h\to0$ or $H$ gives $x\to0$ |
| jet thrust | $F=\rho a v^2$ | momentum flux | $v\to0\Rightarrow0$ |
| Poiseuille | $Q=\pi R^4\Delta p/8\eta L$ | laminar, steady, no slip | $\eta\to0\Rightarrow Q\to\infty$ (inviscid runs free) |
| Stokes drag | $6\pi\eta r v$ | $\text{Re}\lesssim1$ | $\eta\to0\Rightarrow0$ |
| terminal velocity | $v_t=2r^2(\rho-\sigma)g/9\eta$ | Stokes regime | $r\to0\Rightarrow0$ |
| Reynolds | $\rho v D/\eta$ | definition | $\eta\to0\Rightarrow\infty$ |
| drop excess pressure | $2\gamma/r$ | spherical, one surface | $r\to\infty\Rightarrow0$ |
| bubble excess pressure | $4\gamma/r$ | two surfaces | half of two drops' worth |
| Jurin | $h=2\gamma\cos\theta/\rho g r$ | $r\ll h$, wetting equilibrium | $\theta=90^\circ\Rightarrow h=0$ |
| shallow-water speed | $v=\sqrt{gh}$ | $\lambda\gg h$, small amplitude | deep water invalidates |

**Which formula when.** Depth and rest → (3.2). Rigidly accelerated vessel → replace $\mathbf g$ by $\mathbf g-\mathbf a$. Floating/stability → §3.5–3.6. Flow speeds and pressures with the four gates → Bernoulli; if a *long narrow* pipe with a flow rate is named → Poiseuille, not Bernoulli. Sinking sphere at low Re → Stokes. Millimetre-scale surfaces → $\gamma$ family.

> [!danger] Trap
> Bernoulli across a long pipe "because it flows" is the exam favourite: a long pipe's pressure drop is viscous (Poiseuille), not inertial. Bernoulli explains the *constriction*, Poiseuille explains the *length*.

> [!abstract] DIAGRAM D11.16 · The decision tree: which pressure tool?
> *Show:* a small flowchart: "fluid at rest?" yes → hydrostatics/manometer; no → "long narrow pipe, flow rate given?" yes → Poiseuille; no → "four gates ok?" yes → Bernoulli; no → momentum flux or full dynamics; each leaf with one worked-problem number (Q2, Q19, Q12, Q16).
> *Search:* "fluid mechanics choosing bernoulli poiseuille hydrostatic decision"

## Part 5 · Worked exemplars

### E1 — Two-layer tank: pressure at the bottom and the kink

A tank holds $0.8$ m of oil ($\rho=800$) above $1.2$ m of water. Find the gauge pressure at the interface and at the bottom.

<details><summary>Solution</summary>

Interface: $p_i=\rho_o g h_o=800\times9.8\times0.8=6272$ Pa. Bottom adds the water column: $p_b=6272+1000\times9.8\times1.2=6272+11760=18032$ Pa gauge. The graph kinks at the interface (D11.1) but never jumps.

> [!success] Check
> Single-fluid limit $\rho_o\to\rho_w$: $p_b=\rho g(2.0)=19600$ Pa; our $18032<19600$ because oil is lighter ✓.

</details>

### E2 — The manometer with a trapped gas

A U-tube: left limb open, right limb closed over trapped gas. Mercury stands $18$ cm higher in the right limb; water fills $10$ cm above the mercury in the *open* limb. Find the trapped gas pressure (absolute).

<details><summary>Solution</summary>

Start at the open end: $p_0+\rho_w g(0.10)$ at the water–mercury interface. Descend and climb to the right mercury surface: net mercury height difference $0.18$ m *up* on the right, so subtract $\rho_{Hg} g(0.18)$: $p_{gas}=1.013\times10^5+1000\times9.8\times0.10-13600\times9.8\times0.18=1.013\times10^5+980-23990=7.83\times10^4$ Pa.

> [!success] Check
> Below atmospheric, consistent with the right column standing higher ✓. Units Pa throughout ✓.

</details>

### E3 — Hydraulic lift energy audit

A lift with $a=0.01$ m$^2$, $A=0.5$ m$^2$ raises $2000$ kg by $0.10$ m. Input force, input stroke, and both works.

<details><summary>Solution</summary>

$F_2=2000\times9.8=19600$ N; $F_1=F_2 a/A=392$ N. Output stroke $0.10$ m needs volume $A\times0.10=0.05$ m$^3$, so input stroke $0.05/0.01=5$ m. $W_1=392\times5=1960$ J $=W_2=19600\times0.10$ ✓.

</details>

### E4 — Quarter-circle gate

A quarter-cylinder gate of radius $R=2$ m, width $w=3$ m, holds water with the surface at the gate's top. Find the force components on the gate.

<details><summary>Solution</summary>

Horizontal component: the vertical projection is a $2\times3$ m rectangle whose centroid lies $1$ m deep, so $F_H=\rho g h_c A=1000\times9.8\times1\times6=5.88\times10^4$ N. Vertical component: the liquid column directly above the curved face has cross-section (square minus quarter circle) $=R^2-\pi R^2/4=4-\pi=0.858$ m$^2$, hence $F_V=\rho g\times0.858\times3=2.52\times10^4$ N downward. Resultant $\sqrt{F_H^2+F_V^2}=6.4\times10^4$ N at $\tan^{-1}(2.52/5.88)=23.3^\circ$ below horizontal.

> [!success] Check
> Every pressure force on a circular arc is radial and passes through the centre, so the resultant must too — use that as the line of action instead of re-deriving moments ✓.

</details>

### E5 — The accelerating tank and the uncovered strip

An open tank $6$ m long, $2.5$ m high holds water to $2$ m. It accelerates horizontally. (a) At what $a$ does water reach the brim at the back? (b) At what $a$ does the bottom begin to show at the front?

<details><summary>Solution</summary>

(a) The surface pivots about the mid-length point while no water spills (volume fixed): rise at back $=0.5$ m over $3$ m, $\tan\theta=0.5/3=a/g$, $a=9.8/6=1.63$ m/s$^2$. (b) Bottom shows when the surface passes through the front bottom corner and the back top corner: $\tan\theta=2.5/6$, $a=9.8\times2.5/6=4.08$ m/s$^2$ — but only after spilling has begun; at the onset of spilling the depth at the back is $2.5$ m and volume conservation no longer holds, so use geometry directly: $a=4.08$ m/s$^2$ is the answer at the instant the front bottom corner is exposed *with* spilling already accounted (surface through both corners).

> [!warning] Condition of validity
> Between (a) and (b) the pivot-about-centre rule holds only until spilling starts at $a$ where the back level hits the brim; afterwards recompute with the surface pinned at the back rim.

</details>

### E6 — The balloon in the braking car

A helium balloon is tied to the floor of a car whose acceleration is $\mathbf a$ (forward when speeding up, rearward when braking). Which way does it lean, and why does a hanging strap lean the other way?

<details><summary>Solution</summary>

In the car's frame, effective gravity is $\mathbf g_{\text{eff}}=\mathbf g-\mathbf a$; pressure increases along $-\mathbf g_{\text{eff}}$, so the air piles toward the rear when $\mathbf a$ is forward. Buoyancy on the balloon points along $-\mathbf g_{\text{eff}}$, i.e. up *plus* $\mathbf a$: the balloon leans **along** $\mathbf a$ — forward under acceleration, rearward under braking. The strap, denser than air, hangs along $\mathbf g_{\text{eff}}$, i.e. against $\mathbf a$. Both are the same vector statement applied to bodies lighter and denser than the surrounding fluid.

> [!tip] Insight
> Rule to carry: the balloon leans *along* $\mathbf a$, the strap *against* $\mathbf a$.

</details>

### E7 — Ice with a stone, numerically

A $0.5$ kg ice cube embeds a $0.1$ kg stone ($\rho_s=2500$). It floats in fresh water in a cylinder of area $0.02$ m$^2$. After melting, by how much does the level change?

<details><summary>Solution</summary>

While floating, displaced volume $V_1=(0.6)/1000=6.0\times10^{-4}$ m$^3$. After: meltwater $0.5/1000=5.0\times10^{-4}$ m$^3$ joins the tank; stone displaces $0.1/2500=4.0\times10^{-5}$ m$^3$. Total added to the water body: $5.4\times10^{-4}$ m$^3$ vs removed displacement $6.0\times10^{-4}$ m$^3$: deficit $6\times10^{-5}$ m$^3$, level falls by $6\times10^{-5}/0.02=3$ mm.

> [!success] Check
> Sign matches §3.6's qualitative rule (stone denser ⇒ fall) ✓.

</details>

### E8 — Venturi flow rate

A horizontal pipe $A_1=4\times10^{-3}$ m$^2$ narrows to $A_2=10^{-3}$ m$^2$. A water manometer across the pair reads $0.15$ m of water. Find $Q$.

<details><summary>Solution</summary>

$\Delta p=\rho g \Delta h=1000\times9.8\times0.15=1470$ Pa. $A_1^2/A_2^2=16$. $v_1=\sqrt{2\times1470/(1000\times15)}=\sqrt{0.196}=0.443$ m/s. $Q=A_1v_1=1.77\times10^{-3}$ m$^3$/s.

> [!success] Check
> $v_2=1.77$ m/s; dynamic-pressure rise $\tfrac12\rho(v_2^2-v_1^2)=\tfrac12\times1000\times(3.13-0.196)=1467$ Pa ✓ matches $\Delta p$.

</details>

### E9 — Raindrop terminal velocity in the Stokes regime

Find $v_t$ for $r=0.10$ mm in air ($\eta=1.8\times10^{-5}$, $\rho_w=1000$), then check the regime.

<details><summary>Solution</summary>

Numerator: $2r^2(\rho-\sigma)g=2\times(10^{-4})^2\times1000\times9.8=1.96\times10^{-4}$. Denominator: $9\eta=9\times1.8\times10^{-5}=1.62\times10^{-4}$. So $v_t=1.21$ m/s. Now the regime: $\text{Re}=\rho_a v_t D/\eta=1.2\times1.21\times2\times10^{-4}/1.8\times10^{-5}\approx16$, well beyond $\text{Re}\lesssim1$ — Stokes overestimates; the honest terminal speed is of order $0.7$–$1$ m/s once quadratic drag enters (OL4 does the crossover). The exercise's real lesson is that a Stokes answer without its Reynolds number is an unfinished answer.

> [!warning] Condition of validity
> Always print Re with a Stokes answer; graders award the check, not the number.

</details>

### E10 — Capillary rise and the energy book

Water rises in a clean tube of $r=0.5$ mm. (a) The height. (b) The surface-energy and gravitational-energy changes, and where the "missing" half went.

<details><summary>Solution</summary>

(a) $h=2\times0.0728/(1000\times9.8\times5\times10^{-4})=0.0297$ m. (b) $U_g=\tfrac12\rho g h^2\pi r^2=\tfrac12\times1000\times9.8\times(0.0297)^2\times\pi(5\times10^{-4})^2=3.37\times10^{-7}$ J. The adhesion release is $2\pi r h\,\gamma\cos\theta=2\pi(5\times10^{-4})(0.0297)(0.0728)=6.8\times10^{-7}$ J — twice $U_g$; the other half dissipates as heat and sloshing while the column oscillates and damps to rest. Energy methods give the equilibrium height from $dU/dh=0$; the full release explains the factor.

> [!success] Check
> $dU/dh=0$ reproduces Jurin exactly; the factor-2 dissipation is the classic capillary paradox, stated, not hidden.

</details>

## Part 6 · Problem archetypes and practice

### 6.1 Archetypes

| # | Archetype | Template | Where worked | Variations |
|---:|---|---|---|---|
| 1 | Two-fluid column pressure | add $\rho g h$ per layer | E1, Q2 | three layers; tilted tube |
| 2 | Manometer step method | walk, add down, subtract up | E2, Q3 | trapped gas both limbs; accelerated manometer |
| 3 | Hydraulic lift audit | force ratio $A/a$, equal works | E3, Q4 | two-stage lift; spring-loaded piston |
| 4 | Force on plane/inclined surface | $F=p_cA$, centre of pressure $2H/3$ | §3.3, Q5 | hinged gate torque; trapezoidal dam |
| 5 | Curved surface by projection | $F_H$ on projection, $F_V$ weight above | E4, Q6 | gate holding from below (upthrust) |
| 6 | Accelerated tank geometry | $\tan\theta=a/g$, volume bookkeeping | E5, Q7 | vertical acceleration; rotation |
| 7 | Floating fraction | $\rho_b/\rho_f$ | §3.5, Q8, Q9 | layered liquids; overflow |
| 8 | Ice-melting levels | displaced vs added volume | E7, Q10, Q11 | salt water; bubble; stone; oil layer |
| 9 | Metacentre/stability | $BM=I/V$ | §3.5, Q8 | cylinder float; submerged case |
| 10 | Continuity in tapers | $Av$ const | §3.7, Q12 | branching; falling stream radius |
| 11 | Bernoulli device | four gates, then (3.8) | E8, Q12–Q14 | pitot; siphon; atomiser |
| 12 | Torricelli family | $v=\sqrt{2gh}$, range, drain time | §3.10, Q13, OL1 | moving tank; two holes |
| 13 | Jet thrust | $F=\rho a v^2$ | §3.11, Q16 | moving plate; curved vane |
| 14 | Poiseuille networks | $R_{hyd}=8\eta L/\pi R^4$ series/parallel | §3.12, Q19 | series pair; ratio flows |
| 15 | Terminal velocity + regime | (3.15) then print Re | E9, Q20 | oil column; density match |
| 16 | Excess pressure book | $2\gamma/r$, $4\gamma/r$, merging | §3.15, Q21 | bubble coalescence; splitting work |
| 17 | Jurin and short tube | (3.19); $hR=h'R'$ | E10, Q22, Q23 | contact angle; mercury depression |
| 18 | Surface-energy work | $\gamma\Delta A$ with surface counting | §3.14, Q24, Q25 | film on frame; drop splitting |

### 6.2 Practice

#### Q1. A vertical tube holds $40$ cm of water above $30$ cm of mercury. Gauge pressure at the bottom?

<details><summary>Solution</summary>

$1000\times9.8\times0.40+13600\times9.8\times0.30=3920+39984=43904$ Pa $\approx4.39\times10^4$ Pa.

</details>

#### Q2. In a two-layer lake ($3$ m oil of $900$ over $7$ m water) a ball rests exactly at the interface. The pressures just above and just below it are equal; the *buoyant* forces per volume are not. Explain in one line.

<details><summary>Solution</summary>

Pressure is continuous, but the local gradient $\rho g$ — which sets the buoyant force per displaced volume — jumps from $900g$ to $1000g$.

</details>

#### Q3. A U-tube with both limbs open holds water; $10$ cm of oil ($800$) is poured into one limb. The difference of the water levels in the two limbs?

<details><summary>Solution</summary>

Interface balance: $\rho_o g h_o=\rho_w g h_w\Rightarrow h_w=0.8\times10=8$ cm.

</details>

#### Q4. A hydraulic press has $a/A=1/50$. To hold $500$ kg, the input force? If the load rises $2$ cm, the input stroke?

<details><summary>Solution</summary>

$F_1=500\times9.8/50=98$ N; stroke $=50\times0.02=1$ m.

</details>

#### Q5. A $2$ m $\times$ $3$ m vertical gate has its top edge at the water surface. Force on it and the torque about the top hinge.

<details><summary>Solution</summary>

$F=\rho g h_c A=1000\times9.8\times1\times6=5.88\times10^4$ N acting at $2H/3=4/3$ m; torque about top $=5.88\times10^4\times4/3=7.84\times10^4$ N·m.

</details>

#### Q6. A hemispherical bump of radius $0.5$ m protrudes from a tank wall, water outside at depth $2$ m to the bump centre. Horizontal force on the bump?

<details><summary>Solution</summary>

$F_H=p_c A_{proj}=(\rho g\times2)\times\pi(0.5)^2=19600\times0.785=1.54\times10^4$ N. (Vertical component needs the weight-above argument; the projection trick kills it for $F_H$.)

</details>

#### Q7. A tank accelerates upward at $g$. The pressure at depth $h$?

<details><summary>Solution</summary>

$g_{eff}=2g$: $p=p_0+2\rho g h$. The scale under the tank agrees: apparent weight doubles.

</details>

#### Q8. A wooden cylinder of density $667$ kg/m$^3$ floats vertically in water. Oil of density $500$ kg/m$^3$ is poured until the cylinder is just covered. What fraction of the cylinder now sits in the water?

<details><summary>Solution</summary>

Buoyancy now has two contributors: $\rho_b V=\rho_w V_w+\rho_o(V-V_w)$. Substituting: $667V=1000V_w+500V-500V_w$, so $167V=500V_w$ and $V_w/V=1/3$. The cylinder rides up because the upper liquid *helps* buoyancy; the water need hold only a third.

Limit checks: with $\rho_o\to0$ the fraction returns to $667/1000=2/3$, the original float fraction ✓; with $\rho_o\to667$ the cylinder is neutral in the oil and $V_w\to0$ ✓.

</details>

#### Q9. A cubical block floats half-in water half-in oil ($800$). Its density?

<details><summary>Solution</summary>

$\rho_b=0.5(1000)+0.5(800)=900$ kg/m$^3$.

</details>

#### Q10. Ice floats in water with an iron pin stuck *underneath* it (fully submerged pin). On melting, the level?

<details><summary>Solution</summary>

Same as stone-in-ice: falls, by the pin's $(m/\rho_w-m/\rho_{Fe})>0$ deficit.

</details>

#### Q11. Ice containing an air pocket floats; it melts. Level?

<details><summary>Solution</summary>

Unchanged: the pocket's mass is negligible in both states.

</details>

#### Q12. Water flows in a pipe at $1.2$ m/s where the radius is $2$ cm. Speed where the radius is $1$ cm? If the wide part is $10$ m lower, the pressure difference (ignore viscosity)?

<details><summary>Solution</summary>

$v_2=1.2\times4=4.8$ m/s. Bernoulli: $p_1-p_2=\tfrac12\rho(v_2^2-v_1^2)+\rho g(y_2-y_1)=\tfrac12\times1000(23.04-1.44)+1000\times9.8\times10=10800+98000=1.088\times10^5$ Pa.

</details>

#### Q13. A tank of water height $H=1.25$ m has a hole at $h=0.8$ m depth. Horizontal range on the floor?

<details><summary>Solution</summary>

$x=2\sqrt{0.8\times0.45}=2\times0.6=1.2$ m.

</details>

#### Q14. A siphon's top is $3$ m above the supply level; the outlet is $2$ m below it. Speed in the tube (uniform bore)?

<details><summary>Solution</summary>

$v=\sqrt{2g\times2}=6.26$ m/s; top pressure $p_0-\rho g(3)-\tfrac12\rho v^2=1.013\times10^5-29400-19600=5.23\times10^4$ Pa — safely positive.

</details>

#### Q15. A cylindrical vessel of area $A$ has a hole of area $a=A/100$. Time to drain from $H=1.25$ m to empty?

<details><summary>Solution</summary>

$T=(A/a)\sqrt{2H/g}=100\times\sqrt{0.255}=100\times0.505=50.5$ s (OL1 derives the formula).

</details>

#### Q16. A fire hose ($a=5\times10^{-4}$ m$^2$) jets water at $20$ m/s horizontally at a wall. Force on the wall if the water drops straight down after impact?

<details><summary>Solution</summary>

$F=\rho a v^2=1000\times5\times10^{-4}\times400=200$ N.

</details>

#### Q17. Two holes at depths $h$ and $4h$ in a tall tank. Ratio of efflux speeds? Ratio of thrusts (equal areas)?

<details><summary>Solution</summary>

Speeds $1:2$; thrusts $\rho a v^2\Rightarrow1:4$.

</details>

#### Q18. A balloon of volume $V$ rises in air; why does its ascent slow and stop? (Name two mechanisms.)

<details><summary>Solution</summary>

Air density falls with height, shrinking $F_b=\rho_a V g$ toward the weight; and drag (quadratic at balloon Re) eats the acceleration. Equilibrium where $\rho_a V=\!m$.

</details>

#### Q19. Two capillaries in series, radii $r$ and $r/2$, same length, carry oil under total $\Delta p=3\times10^5$ Pa. The drop across the narrow one?

<details><summary>Solution</summary>

Resistance ratio $1:16$ (from $R^4$); narrow carries $16/17$ of $\Delta p=2.82\times10^5$ Pa.

</details>

#### Q20. A sphere of density $2000$ kg/m$^3$ falls in glycerine ($\rho=1260$, $\eta=1.5$ Pa·s) reaching $v_t=0.1$ m/s. Its radius (Stokes)?

<details><summary>Solution</summary>

$r=\sqrt{9\eta v_t/(2(\rho-\sigma)g)}=\sqrt{9\times1.5\times0.1/(2\times740\times9.8)}=\sqrt{0.135/14504}=\sqrt{9.31\times10^{-6}}=3.05\times10^{-3}$ m. Regime Re $=1260\times0.1\times6.1\times10^{-3}/1.5\approx0.51<1$ ✓ Stokes honest.

</details>

#### Q21. Two soap bubbles of radii $r$ and $3r$ coalesce in vacuum (isothermal, surface tension fixed). The new radius?

<details><summary>Solution</summary>

Isothermal coalescence conserves moles of air: for a bubble $n\propto pV=(4\gamma/r)\tfrac43\pi r^3=\tfrac{16}{3}\pi\gamma r^2$. Bubble 1 gives $\tfrac{16}{3}\pi\gamma r^2$; bubble 2 ($3r$) gives $(4\gamma/3r)\tfrac43\pi(3r)^3=16\pi\gamma r^2$. The new bubble carries $\tfrac{16}{3}\pi\gamma R^2$. Sum: $\tfrac{16}{3}\pi\gamma R^2=\tfrac{16}{3}\pi\gamma r^2+16\pi\gamma r^2=\tfrac{64}{3}\pi\gamma r^2$, so $R^2=4r^2$ and $R=2r$.

> [!success] Check
> Volume check: $V_{new}=\tfrac43\pi 8r^3$ vs $V_1+V_2=\tfrac43\pi(28)r^3$ — the new bubble has *less* volume because its internal pressure is lower; moles, not volume, are conserved ✓.

</details>

#### Q22. Water rises $12$ cm in a capillary; the tube is only $9$ cm long. The meniscus radius ratio $R'/R$?

<details><summary>Solution</summary>

$hR=h'R'\Rightarrow R'/R=12/9=4/3$. The meniscus flattens; no overflow.

</details>

#### Q23. Mercury ($\gamma=0.465$, $\theta=140^\circ$, $\rho=13600$) in a $1$ mm tube: rise or depression, and by how much?

<details><summary>Solution</summary>

$\cos140^\circ=-0.766$, so $h=2\times0.465\times(-0.766)/(13600\times9.8\times5\times10^{-4})=-0.712/66.6=-0.0107$ m: a $1.07$ cm **depression**, as the convex meniscus promised.

> [!success] Check
> Sign check via §3.14: $\theta>90^\circ$ means the liquid is pulled away from the wall, so the column stands lower than the reservoir ✓.

</details>

#### Q24. A square wire frame $10$ cm side is lifted from a water surface; the extra force just before the film breaks?

<details><summary>Solution</summary>

Film on both faces: $F=2\gamma\times(4\times0.10)=2\times0.0728\times0.4=0.058$ N.

</details>

#### Q25. A drop of radius $R$ splits into $1000$ equal drops. The work done?

<details><summary>Solution</summary>

$r=R/10$. $\Delta A=1000\times4\pi r^2-4\pi R^2=4\pi R^2(10-1)=36\pi R^2$; $W=\gamma\times36\pi R^2$. For $R=1$ mm: $W=0.0728\times36\pi\times10^{-6}=8.2\times10^{-6}$ J.

</details>

## Part 7 · Alternate methods and the JEE-Advanced advantage toolkit

**T1 · The frame trick.** Any rigidly accelerated or rotated vessel is a hydrostatics problem in disguise: replace $\mathbf g$ by $\mathbf g-\mathbf a$ (add $\omega^2 r$ radially for rotation) and reuse every static tool — manometer steps, Archimedes, "level surfaces perpendicular to $g_{eff}$". Cuts E5, E6, Q7-class questions to one line. *Fails* the moment different parts of the fluid have different accelerations (sloshing, transients): then it is dynamics, not hydrostatics.

**T2 · The displacement-volume ledger.** For any "what happens to the level" question, never integrate pressures: compare *volume displaced while floating* (mass-based, $m/\rho_f$) with *volume occupied or displaced afterwards* (geometry-based if sunk, mass-based if floating). The four ice-family answers are one table, not four derivations (§3.6).

**T3 · Pressure-walk (manometric) method with $g_{eff}$.** Walk from any open end to the target point, adding $\rho g_{eff}\Delta h$ per descent; horizontal segments cost nothing. Beats writing force balances for every multi-fluid column (E2, Q3).

**T4 · Projection theorem for curved surfaces.** $F_H$ equals the plane-projection force; $F_V$ equals the real-or-imagined column weight above. Converts a calculus problem into two statics lookups (E4, Q6). *Fails* only when the surface is not wetted on the assumed side — draw the wetting first.

**T5 · Hydraulic resistance analogy.** Poiseuille gives $R_{hyd}=8\eta L/\pi R^4$; series and parallel combine like electrical resistors with $\Delta p\leftrightarrow V$, $Q\leftrightarrow I$. Q19 becomes a voltage divider. *Fails* for short fittings and turbulent flow, where the $\Delta p\propto Q$ linearity dies.

**T6 · Energy-vs-force double solve.** Capillary rise, bubble expansion, film stretching: solve once with forces (Jurin balance) and once with $dU/dh=0$ or $dU/dr=0$. Disagreement signals a missed surface (the factor-2 family) — E10 shows the audit including dissipation.

**T7 · Dimensional bootstrap.** Stokes' drag form and the Reynolds number are dimensional statements (§3.13); shallow-water speed $v\propto\sqrt{gh}$ is one too. When an exam says "depends only on...", dimensional analysis *is* the solution, with the constant left for experiment ([[Units-measurements#Part 10 · Olympiad extension|units §10]] owns the method).

**T8 · Scaling/limit audit.** After solving any fluid number, hit it with $r\to0$ (skin physics appears), $\eta\to0$ (Bernoulli world), $a\to0$ (statics), $A/a\to\infty$ (Torricelli exact). Every worked exemplar here closes with one of these; make it reflexive.

> [!question] Exam note
> JEE Advanced loves *composite* fluid items: a Bernoulli jet feeding a buoyancy balance, a capillary in an accelerating lift. The trap is solving with the wrong $g$ or forgetting that the jet's thrust is momentum flux, not $pA$. Triage by the §9 tree first.

## Part 8 · Examiner traps

1. **Shape dependence.** "More water, more pressure on the base." Reply: pressure is depth, Eq. (3.2); the hydrostatic paradox (D11.2) carries the rest. Paper archetype: three-vessel MCQ.
2. **Absolute vs gauge.** Plugging $p_0$ into a $\Delta p$ manometer walk, or reporting gauge where absolute is asked (bubbles!). Reply: label every pressure you write as *abs* or *gauge* on first use.
3. **Displaced volume ≠ body volume.** Using the whole body volume for $F_b$ on a floating or partially submerged body. Reply: $V_{disp}$ is what the fluid actually lost.
4. **The soap-bubble factor 2.** Using $2\gamma/r$ for a bubble. Reply: two surfaces, $4\gamma/r$; a drop has one (D11.14).
5. **Bernoulli where Poiseuille rules.** Applying (3.8) between the ends of a long pipe with flow. Reply: the four gates; long pipe ⇒ viscous drop (3.13).
6. **Torricelli with a big hole.** Ignoring the surface speed. Reply: the condition is $a/A\ll1$; otherwise include $v_{surface}$ from continuity.
7. **Siphon at any height.** Reply: $p_{top}\ge0$ caps the lift at $\sim p_0/\rho g\approx10.3$ m of water (3.10's warning).
8. **Buoyancy at the wrong point.** Taking moments about the centre of mass with $F_b$ applied there. Reply: $F_b$ acts at the centre of *buoyancy*, the centroid of displaced volume (3.5).
9. **Air buoyancy ignored in precision work.** Weighing "in air" as in vacuum. Reply: fine for JEE numbers, fatal for metrology — say so in one line, as §3.5's honesty note does.
10. **Stokes beyond its regime.** Printing (3.15) without Re. Reply: print Re; if $>1$, say quadratic drag enters (E9).
11. **Neutral axis at the geometric centre for composite sections.** (Preview for PART 12, but the fluid analogue bites here:) assuming the centre of pressure is the centroid. Reply: it is below, by $I_c/Ah_c$; the pressure triangle decides.
12. **Contact angle on the wrong side.** Measuring $\theta$ through the gas. Reply: through the liquid; mercury's $140^\circ$ then gives depression with the right sign (Q23).

## Part 9 · Playbook

**Triage tree.**

1. Fluid at rest (or rigidly accelerated/rotated)? → hydrostatics with $\mathbf g$ or $\mathbf g_{eff}$ (T1, T3).
2. Floating/sinking/level-change? → Archimedes plus the displacement ledger (T2).
3. Flow with speeds/pressures, short devices, four gates OK? → continuity + Bernoulli (T8's limits after).
4. Long narrow pipe, flow rate or viscosity named? → Poiseuille network (T5).
5. Jet, thrust, draining-force question? → momentum flux $\rho a v^2$ (and OL1 for times).
6. Millimetre scale: drops, bubbles, menisci, tubes? → $\gamma$ family (T6's double solve).

**Formula map with validity.** (3.2) statics; (3.3)–(3.4) rigid acceleration/rotation; (3.5)–(3.6) buoyancy/stability; (3.7) continuity; (3.8) the four gates; (3.9)–(3.11) devices; (3.13) laminar pipe; (3.14)–(3.15) Stokes; (3.17)–(3.19) surface family. Each carries its warning box in Part 3; the Part 4 ledger is the cram version.

**Constants to memorise.** $p_0\approx10^5$ Pa; water barometer $10.3$ m; $\gamma_{water}\approx0.073$ N/m; $\eta_{water}\approx10^{-3}$ Pa·s; $\rho_{Hg}/\rho_w=13.6$; $B_{water}\approx2.2\times10^9$ Pa.

**Timing plan.** Section A items: 90 s each, mostly T2/T3 lookups. Section D fluid longs: 12 min — 2 min to draw and choose the tool, 8 to derive, 2 to limit-check.

**Pre-submission audit (10 points).** (1) Every pressure labelled abs/gauge. (2) $V_{disp}$ drawn, not assumed. (3) Bernoulli gates named if used. (4) Re printed with any Stokes number. (5) Factor 2 audited on every film/bubble surface count. (6) $g_{eff}$ consistent across the item. (7) Units in every substitution. (8) One limit checked per item. (9) Centre of pressure vs centroid not conflated. (10) Answer magnitude sane (metres, not kilometres, of water).

> [!abstract] DIAGRAM D11.17 · The toolkit map as a one-page cheat figure
> *Show:* the triage tree of §9 as a compact flowchart with the six toolboxes and their equation numbers at the leaves, and the four Bernoulli gates drawn as a small gate icon on the Bernoulli branch.
> *Search:* "fluid mechanics summary flowchart hydrostatics bernoulli surface tension"

## Part 10 · Olympiad extension

### OL1 — The draining tank, two regimes and two timescales

A cylindrical tank of area $A$ holds water to $H$. (a) With a sharp orifice of area $a\ll A$, derive the emptying time. (b) Replace the orifice by a horizontal capillary tube of radius $r$, length $L$, and derive the late-time behaviour. (c) Find the height $h^*$ where the description crosses over.

<details><summary>Solution</summary>

(a) Quasi-steady Torricelli: $-A\,dh/dt=a\sqrt{2gh}$. Separate: $\int_0^T dt=\frac{A}{a\sqrt{2g}}\int_0^H h^{-1/2}dh$, giving

$$
T=\frac{A}{a}\sqrt{\frac{2H}{g}}. \qquad (10.1)
$$

Numerics of Q15: $T=100\sqrt{2\times1.25/9.8}=50.5$ s. Note $h(t)$ is a *perfect square* in $t$ and the tank is exactly empty at $T$ — inertia-limited drainage has a finite lifetime.

(b) With a long thin drain the flow is Poiseuille: $Q=\pi r^4\rho g h/(8\eta L)$, so $-A\,dh/dt=Q$ gives exponential decay $h(t)=H e^{-t/\tau}$ with $\tau=8\eta L A/(\pi r^4\rho g)$. Viscous drainage never finishes; the last centimetre takes as long as the first $63\%$ did. That is the honest content of "the last bit takes forever".

(c) Crossover where the two outflows are equal. Write the viscous outflow as $kh$ with $k=r^2\rho g/(8\eta L)$ and the inertial one as $\sqrt{2gh}$ (taking $a=\pi r^2$); equating and squaring gives $2gh=k^2h^2$, so

$$
h^*=\frac{2g}{k^2}=\frac{128\,\eta^2L^2}{\rho^2 g r^4}.
$$

Numbers, using glycerine ($\eta=1.5$ Pa·s) so the laminar assumption is honest: $k=r^2\rho g/(8\eta L)=2.5\times10^{-7}\times1260\times9.8/(8\times1.5\times0.2)=1.29\times10^{-3}$ s$^{-1}$, hence $h^*=2g/k^2=19.6/1.66\times10^{-6}\approx1.2\times10^7$ m — no bench-scale column ever reaches it, and the glycerine drain is viscous (exponential) from the first millimetre. With water the same $k$ is $1500\times$ larger and $h^*\approx5$ m; but water at those speeds in a half-millimetre tube has $\text{Re}\sim10^3$–$10^4$, so the real late regime is *turbulent*, not laminar Poiseuille — the clean inertial/laminar pair is a teaching model, and the honest water story is inertial-then-turbulent. Say which pair you are using.

> [!success] Check
> $\eta\to0$ gives $h^*\to0$: the viscous regime shrinks to nothing and (10.1) rules the whole drain ✓. Dimensions of $h^*$: $[\eta^2L^2/(\rho^2 g r^4)]=$ (Pa$^2$s$^2$m$^2$)/(kg$^2$m$^{-6}$·m s$^{-2}$·m$^4$)$=$ m ✓.

</details>

> [!abstract] DIAGRAM D11.18 · The draining tank with the variable height
> *Show:* tank of area $A$, instantaneous level $h(t)$, orifice $a$ with jet speed $\sqrt{2gh}$; beside it the $h(t)$ curve: a parabola-squared reaching zero at $T$ for the orifice, and the exponential tail for the capillary drain drawn dashed, crossing at $h^*$; the two timescales labelled.
> *Search:* "draining tank Torricelli height versus time exponential viscous"
> *Used in:* OL1.

### OL2 — The paraboloid, three ways

Derive $z=z_0+\omega^2r^2/2g$ for the free surface of a rotating liquid (a) by force balance on a surface element, (b) by the equipotential argument, (c) by "Bernoulli with a centrifugal head". Then: a bucket of radius $0.30$ m spins at $\omega=4$ rad/s; find the rim-to-centre height difference and the centre's drop relative to the rest level.

<details><summary>Solution</summary>

(a) Surface element of mass $m$: horizontal $m\omega^2 r=N\sin\alpha$, vertical $mg=N\cos\alpha$; divide: $\tan\alpha=dz/dr=\omega^2r/g$; integrate: (3.4).

(b) In the rotating frame the fluid is static under $\mathbf g$ and the centrifugal field $\omega^2 r\,\hat r$; both are conservative with potential per mass $\Phi=gz-\tfrac12\omega^2r^2$. A static fluid cannot sustain tangential stress, so $\nabla p\parallel\nabla\Phi$; on the free surface $p$ is constant, so $\Phi$ is constant: $gz-\tfrac12\omega^2r^2=\text{const}$ — the same paraboloid, and the deep reason the force balance integrated at all.

(c) For a fluid static in the rotating frame, integrate $dp=\rho\omega^2r\,dr-\rho g\,dz$ between any two points: $p-\tfrac12\rho\omega^2r^2+\rho gz=\text{const}$ everywhere — the rotating-frame Bernoulli with centrifugal head $-\omega^2r^2/2g$. Setting $p=p_0$ on the surface recovers (3.4).

Numbers: rim rise over centre $=\omega^2R^2/2g=16\times0.09/19.6=0.0735$ m. Volume conservation in a cylinder: the rest level sits halfway, so the centre drops $3.7$ cm and the rim rises $3.7$ cm.

> [!success] Check
> $\omega\to0$: flat ✓. The three derivations agree because they are the same theorem in three languages (Newton, energy, Bernoulli).

</details>

> [!abstract] DIAGRAM D11.19 · The rotating bucket's three derivations in one figure
> *Show:* the paraboloid surface; inset (a) the surface element with $N$, $mg$, $m\omega^2r$; inset (b) equipotential lines of $\Phi=gz-\tfrac12\omega^2r^2$ drawn as nested parabolas with the surface as the $p_0$ member; inset (c) the centrifugal-head column sketch; the numbers $\omega=4$, $R=0.3$ m, $\Delta z=7.35$ cm labelled.
> *Search:* "rotating bucket paraboloid equipotential surfaces derivation"

### OL3 — Terminal velocity in two drag regimes, and the raindrop crossover

(a) Show that a water sphere of radius $r$ falling in air has $v_t=\frac{2r^2\rho_w g}{9\eta}$ for $\text{Re}\lesssim1$ and $v_t=\sqrt{\frac{8r\rho_w g}{3C_d\rho_a}}$ (with $C_d\approx0.44$) for large Re. (b) Find the crossover radius $r^*$ where the Stokes answer self-destructs (Re$=1$), and the speeds on either side. (c) State the practical consequence for mist versus rain.

<details><summary>Solution</summary>

(a) Balance $\tfrac43\pi r^3\rho_w g$ against $6\pi\eta r v$ (Stokes) and against $\tfrac12C_d\rho_a\pi r^2v^2$ (quadratic): the two formulas.

(b) Set $\text{Re}=\rho_a v_t 2r/\eta=1$ with the Stokes $v_t$: $\rho_a\frac{2r^2\rho_w g}{9\eta}\frac{2r}{\eta}=1\Rightarrow r^{*3}=\frac{9\eta^2}{4\rho_a\rho_w g}$, $r^*=\left(\frac{9(1.8\times10^{-5})^2}{4\times1.2\times1000\times9.8}\right)^{1/3}=\left(6.2\times10^{-14}\right)^{1/3}\approx4\times10^{-5}$ m. At $r^*$: $v_t=\eta/(2\rho_a r^*)=1.8\times10^{-5}/(2\times1.2\times4\times10^{-5})=0.19$ m/s. A $2$ mm drop in the quadratic formula: $v_t=\sqrt{8\times2\times10^{-3}\times1000\times9.8/(3\times0.44\times1.2)}=\sqrt{156.8/1.584}=\sqrt{99}=9.9$ m/s (measured raindrops of that size fall $\sim6.5$–$9$ m/s; deformation raises the drag — say so).

(c) Mist ($r<r^*$) drifts at centimetres per second and stays airborne; rain ($r\sim$ mm) cruises at $\sim10$ m/s. The vacuum estimate $\sqrt{2gh}$ from a cloud at $2000$ m would give $200$ m/s — the atmosphere's viscosity is the only reason rain is weather rather than shrapnel.

> [!success] Check
> Both formulas give $v_t\propto r^2$ and $r^{1/2}$ respectively; the crossover is where the curves meet, independent of which is trusted ✓.

</details>

### OL4 — Young–Laplace from energy, and the soap film between two rings

(a) Derive $\Delta p=\gamma(1/r_1+1/r_2)$ by virtual work. (b) A soap film spans two coaxial rings of radius $R$ separated by $d$. What shape, what pressure difference, and when does the film refuse to exist?

<details><summary>Solution</summary>

(a) Push a small rectangular patch $A$ of curved surface (principal radii $r_1,r_2$) outward by $\delta n$. The radii grow to $r_i+\delta n$, so $A\to A(1+\delta n/r_1)(1+\delta n/r_2)$ and $\delta A=A\,\delta n(1/r_1+1/r_2)$; the swept volume is $\delta V=A\,\delta n$. At equilibrium the pressure work $\Delta p\,\delta V$ equals the surface work $\gamma\,\delta A$: (3.18).

(b) Both sides see the same air, $\Delta p=0$, so the mean curvature vanishes: the minimal surface of revolution, a **catenoid**, $r(z)=r_{min}\cosh(z/r_{min})$ with $r(\pm d/2)=R$. The catenoid exists only while $d/R\lesssim1.33$; beyond it the film snaps into two discs — a classic demonstration that minimal surfaces have existence limits, and a beautiful exam "state and explain" item.

> [!success] Check
> Sphere: $r_1=r_2=r$ recovers $2\gamma/r$ ✓; cylinder: $r_2\to\infty$ gives $\gamma/r$ ✓; plane: $0$ ✓.

</details>

### OL5 — Capillarity beyond Jurin: the drop-weight method and the water strider

(a) Drops fall from a tube of radius $1.0$ mm; a hundred drops weigh $3.1$ g. Estimate $\gamma$ naively (Tate's law) and then with the Harkins–Brown correction $f\approx0.66$, explaining physically why $f<1$. (b) Estimate the maximum mass a water strider can support on six legs of total contact length $0.24$ m, and use scaling to say why no elephant walks on water.

<details><summary>Solution</summary>

(a) Tate's law: at detachment the neck's surface-tension ring $2\pi r\gamma$ supports the drop's weight. One drop: $m=3.1\times10^{-5}$ kg, $mg=3.04\times10^{-4}$ N, so $\gamma_{naive}=mg/(2\pi r)=3.04\times10^{-4}/(6.28\times10^{-3})=0.048$ N/m. The naive value undershoots because part of the neck's liquid never falls — it shrinks back onto the tip — so the fallen drop carries only a fraction $f\approx0.66$ of the ideal ring weight (Harkins–Brown). Correcting: $\gamma=\gamma_{naive}/f=0.048/0.66=0.073$ N/m — water's surface tension, recovered from a kitchen balance and a drop count.

(b) The dented surface pulls up with about $\gamma$ per unit length on each side of each leg: $F_{max}\approx\gamma\times2\times0.24=0.035$ N, supporting $\approx3.6$ g. Real striders weigh $\sim0.01$–$0.1$ g: two orders of margin. Scaling: support $\propto L$ (contact length) but weight $\propto L^3$; at $L\sim100\times$ a strider the margin is gone — which is why the trick is exclusively a small-animal one.

> [!success] Check
> (a) reproduces the tabulated $0.0728$ N/m within the correction's accuracy ✓. (b) $F$ linear in $\gamma$ and length, dimensionally a force ✓.

</details>

> [!abstract] DIAGRAM D11.20 · The water strider's dented surface and the drop-weight neck
> *Show:* left: a water strider leg in cross-section denting the surface, the tension vectors $\gamma$ tangent at both edges of the dent with their vertical components summed; right: the pendant drop at a tube tip with the neck radius smaller than the tube, the fraction left behind shaded, Tate's ring force arrow.
> *Search:* "water strider surface tension dent leg force diagram drop weight method"
> *Used in:* OL5.

### OL6 — How high can a tree suck water?

(a) Compute the capillary height in a xylem vessel of radius $2.5\ \mu$m. (b) Compute the pressure (suction) limit. (c) Redwoods move water past $100$ m; name the mechanism that beats both limits and the physical quantity that makes it possible.

<details><summary>Solution</summary>

(a) $h=2\gamma/(\rho g r)=2\times0.0728/(1000\times9.8\times2.5\times10^{-6})=5.9$ m. (b) A pump at the top can reduce $p$ to near zero: $h_{max}=p_0/\rho g\approx10.3$ m. (c) Neither: transpiration pull puts the xylem water under **tension** (negative pressure, several MPa), sustained by cohesion of the hydrogen-bonded column; the column hangs from the leaves like a rope rather than being pushed from below. Measured giants exceed $110$ m; the true ceiling is cavitation of the stretched water, not the $10$ m barometer.

> [!tip] Insight
> The "10 m limit" is a limit on *suction*, i.e. on pressure differences with $p\ge0$ on one side. Tension is a different state of the liquid; the barometer argument never applied to it.

</details>

### OL7 — Shallow-water wave speed from continuity and momentum

A small-amplitude bump of height $\eta$ travels over depth $h$ ($\eta\ll h\ll\lambda$). Work in the bump's frame and derive $v=\sqrt{gh}$, keeping the first correction in $\eta/h$.

<details><summary>Solution</summary>

In the wave frame the flow is steady: upstream depth $h$, speed $c$; over the bump depth $h+\eta$, speed $c'$. Continuity: $ch=c'(h+\eta)$. Momentum per unit width: pressure thrusts $\tfrac12\rho g h^2$ and $\tfrac12\rho g(h+\eta)^2$ plus momentum fluxes $\rho c^2h$, $\rho c'^2(h+\eta)$:

$$
\tfrac12\rho g h^2+\rho c^2h=\tfrac12\rho g(h+\eta)^2+\rho c'^2(h+\eta).
$$

Eliminate $c'$ and solve: $c^2=g(h+\eta)\left(1+\frac{\eta}{2h}\right)=g\,h\left(1+\frac{\eta}{h}\right)\left(1+\frac{\eta}{2h}\right)$; to first order $c\approx\sqrt{gh}\left(1+\frac{3\eta}{4h}\right)$. The leading term is (3.20); the correction explains why big bumps overtake small ones and steepen — the seed of the hydraulic jump and of surf.

> [!success] Check
> Dimensions $\sqrt{gh}$ ✓; $\eta\to0$ exact ✓; deeper bumps travel faster, matching the steepening observation ✓.

</details>

### OL8 — The Feynman sprinkler, as an argument

A sprinkler that rotates while ejecting water is everyday physics. Its inverse — a head that *sucks* water in — does what in steady state? Argue without formulas first, then locate the idealisation that decides the answer.

<details><summary>Solution</summary>

Transient: as suction starts, water is accelerated toward the nozzles and the head receives a brief torque *toward* the suction direction. Steady ideal flow: the momentum flux entering the control volume is balanced by pressure forces at the inlet; the inflow pattern is time-independent, so the assembly's angular momentum is constant and the net torque vanishes — the ideal sprinkler does not turn. Real fluids: viscous dissipation in the inner vortices breaks the symmetry of the pressure recovery, leaving a small steady torque toward the suction direction; experiments with low-friction bearings observe exactly that slow creep. The deciding idealisation is reversibility: ejection is ordered-to-ordered, suction is ordered-to-disordered, and the arrow of the effect is the arrow of dissipation.

> [!quote] Hand-off
> The entropy bookkeeping of the dissipative correction belongs to [[Thermodynamics#Part 5 · Worked exemplars|thermodynamics]]; here the point is the momentum-flux discipline of §3.11.

</details>

### OL9 — Bernoulli in a rotating frame: the energy audit

A U-tube rotates about one limb at $\omega$; liquid is driven from the axis limb ($r_1=0.10$ m) out to $r_2=0.30$ m. (a) In the rotating frame, write the pressure difference that drives it. (b) Compute the kinetic energy gained by $0.10$ kg of liquid and name, with a number, the real source of that energy.

<details><summary>Solution</summary>

(a) $p-\tfrac12\rho\omega^2r^2+\rho gz=\text{const}$ (OL2(c)): at equal heights, $p_2-p_1=\tfrac12\rho\omega^2(r_2^2-r_1^2)$ — the centrifugal head is a pump.

(b) $\Delta K=\tfrac12 m\omega^2(r_2^2-r_1^2)=0.5\times0.10\times100\times0.08=0.40$ J at $\omega=10$ rad/s. In the lab frame the liquid's tangential speed grows from $\omega r_1$ to $\omega r_2$; something must supply the torque: the **motor** holding $\omega$ constant against the reaction of the outward-moving liquid (the system's moment of inertia grows, and without motor work $\omega$ would sag). The rotating-frame "centrifugal work" is the motor's work in disguise.

> [!success] Check
> Energy and torque accounts agree: $W_{motor}=\Delta K$ for constant $\omega$ with the tube rigid ✓ — the audit closes, answering "where does the energy come from".

</details>

### OL10 — Reconstructing a measurement: glycerine's viscosity by Stokes

Design the classic falling-sphere viscometer and reconstruct a real number. Steel spheres of $r=2.0$ mm ($\rho=7800$) fall through glycerine ($\sigma=1260$, $\eta\approx1.5$ Pa·s) in a $4$ cm-diameter cylinder; a marked $20$ cm takes $t$ seconds. Predict $t$, including the Ladenburg wall correction $v_{true}=v_{meas}(1+2.4\,r/R)$, and state the two checks that validate the regime.

<details><summary>Solution</summary>

Unbounded-fluid $v_t=2r^2(\rho-\sigma)g/9\eta=2(4\times10^{-6})(6540)(9.8)/(13.5)=0.0380$ m/s. Wall correction: measured speed is lower, $v_{meas}=v_t/(1+2.4\times2/20)=0.0380/1.24=0.0307$ m/s. Time over $0.20$ m: $t=6.5$ s. Regime checks: $\text{Re}=\sigma v 2r/\eta=1260\times0.031\times4\times10^{-3}/1.5=0.10<1$ ✓ Stokes honest; end effects avoided by timing the middle third only (state it on the sheet). This is the experiment as a *prediction*: the numbers are standard, the checks are the physics.

> [!success] Check
> $\eta\to\infty$ gives $t\to\infty$ ✓; doubling $r$ quadruples $v_t$ (radius-squared signature) — the experimental fingerprint of Stokes flow ✓.

</details>

### 10.1 Limits and failure modes of the chapter's model

The machinery of Parts 3–4 breaks, in order of encounter: (i) **turbulence** — Re beyond a few thousand; the velocity field becomes a many-scale dissipative cascade and (3.8), (3.13) lose quantitative force (the drag crisis of D11.12); (ii) **unsteady free surfaces** — sloshing and hydraulic jumps are genuinely nonlinear and, past the jump, dissipative; (iii) **compressibility** — water hammer and sound are the $B$-finite world (§3.13 hands the sound speed to [[Sound-waves|sound waves]]); (iv) **non-Newtonian rheology** — shear-thinning and yield-stress fluids violate (3.12)'s linearity; (v) **microscale** — below microns, no-slip itself fails. The hand-offs: elasticity of containers and solids to PART 12; equations of state to [[Thermodynamics|thermodynamics]]; wave kinematics to [[String-waves|string waves]] and [[Sound-waves|sound waves]].

**C9 — concept check.** Which of OL2's three derivations survives if the vessel is accelerated linearly instead of rotated?

<details><summary>Solution</summary>

All three, with $\omega^2r\,\hat r\to-\mathbf a$: the field stays conservative, equipotentials stay planar, and the "Bernoulli with pseudo head" integrates identically. Rotation adds nothing essential except a radial coordinate.

</details>

**C10 — concept check.** In OL1, why is the Torricelli emptying time finite while the viscous one is infinite?

<details><summary>Solution</summary>

Outflow $\propto\sqrt h$ gives $dh/\sqrt h$ integrable at $h=0$; outflow $\propto h$ gives $dh/h$, which is not. The exponent of $h$ in the rate law decides finiteness.

</details>

**C11 — concept check.** A film spans two rings just inside the catenoid limit. Is the pressure inside the film higher, lower, or equal to outside?

<details><summary>Solution</summary>

Equal: $\Delta p=0$ is precisely the zero-mean-curvature condition; the principal curvatures are equal and opposite (saddle), so (3.18) gives zero.

</details>

**C12 — concept check.** Why does the water-strider estimate scale as $L$ while weight scales as $L^3$?

<details><summary>Solution</summary>

Support is a line integral of $\gamma$ (a length); weight is a volume. Surface physics is a boundary phenomenon; gravity is a bulk one. The ratio $L^{-2}$ is why smallness is a superpower.

</details>

## Part 11 · Olympiad-grade paper

**Time: 180 minutes · Maximum marks: 200 · 36 questions.**
Sections: A — 12 single-correct (4 marks each, −1 for a wrong answer); B — 8 one-or-more-correct (4 marks each, no negative marking); C — 6 numerical answers (5 marks each); D — 10 long-form (9 marks each). Solutions follow each question in a collapsible block; the marking scheme is in Part 12.

| Section | Questions | Marks each | Subtotal | Topic coverage |
|---|---|---:|---:|---|
| A | 1–12 | 4 | 48 | blocks 2–4 |
| B | 13–20 | 4 | 32 | blocks 3–4 |
| C | 21–26 | 5 | 30 | blocks 4, 10 |
| D | 27–36 | 9 | 90 | block 10 and syntheses |
| | 36 | | 200 | |

#### Section A · Single correct

### P1 · 4 marks

An open tank 2 m wide accelerates horizontally at $a=g/2$. The difference of water levels between the two ends is: (a) 0.5 m (b) 1 m (c) 2 m (d) 0.

<details><summary>Solution</summary>

$\tan\theta=a/g=0.5$; $\Delta h=2\times0.5=1$ m while no water spills. **(b)**. Check: $a\to0$ gives 0 ✓ (block 3, §3.4).

</details>

### P2 · 4 marks

A beaker of water reads $W$ on a balance. A $50$ g metal piece of density $5000$ kg/m$^3$ is lowered in on a string until fully submerged without touching the bottom. The reading is: (a) $W$ (b) $W+0.49$ N (c) $W+0.10$ N (d) $W+0.39$ N.

<details><summary>Solution</summary>

Added force = buoyancy $=\rho_w (m/\rho_m) g=1000\times10^{-5}\times9.8=0.098$ N. **(c)**. (Block 3, §3.5; C1.)

</details>

### P3 · 4 marks

A barometer liquid of density $2\rho_{Hg}$ would stand at: (a) 152 cm (b) 76 cm (c) 38 cm (d) 19 cm.

<details><summary>Solution</summary>

$h=p_0/(\rho g)\propto1/\rho$: half of 76 = 38 cm. **(c)** (§3.2).

</details>

### P4 · 4 marks

Two holes at depths $h_1,h_2$ on a tank give equal horizontal ranges on the ground below the tank base only if: (a) $h_1=h_2$ (b) $h_1+h_2=H$ (where $H$ is the water height above the base) (c) $h_1h_2=H^2/4$ for all cases (d) ranges can never be equal.

<details><summary>Solution</summary>

$x=2\sqrt{h(H-h)}$ is symmetric under $h\to H-h$: **(b)** (§3.10). Option (c) is the *maximum*-range condition misread.

</details>

### P5 · 4 marks

A soap bubble of radius $r$ has internal excess pressure $\Delta p$. A second bubble with excess pressure $2\Delta p$ has radius: (a) $2r$ (b) $r/2$ (c) $r/\sqrt2$ (d) $r/4$.

<details><summary>Solution</summary>

$\Delta p=4\gamma/r\propto1/r$: **(b)** (§3.15).

</details>

### P6 · 4 marks

A capillary shows rise $h$ in a stationary lab. The lift accelerates upward at $g$. The rise becomes: (a) $h$ (b) $h/2$ (c) $2h$ (d) $0$.

<details><summary>Solution</summary>

$g_{eff}=2g$, $h'\propto1/g_{eff}$: $h/2$. **(b)** (§3.16 with T1).

</details>

### P7 · 4 marks

Water exits a tap at $0.2$ m/s through a $1$ cm radius. The stream radius after falling $0.75$ m is nearest: (a) 0.5 cm (b) 0.7 cm (c) 1 cm (d) 0.25 cm.

<details><summary>Solution</summary>

$v=\sqrt{v_0^2+2gh}=\sqrt{0.04+14.7}\approx3.84$ m/s; $r=r_0\sqrt{v_0/v}=1\times\sqrt{0.2/3.84}=0.228$ cm ≈ 0.25 cm. **(d)** (§3.7).

</details>

### P8 · 4 marks

In the Stokes regime, doubling a falling sphere's radius changes $v_t$ by: (a) $\times2$ (b) $\times4$ (c) $\times\sqrt2$ (d) $\times8$.

<details><summary>Solution</summary>

$v_t\propto r^2$: **(b)** (§3.13).

</details>

### P9 · 4 marks

Many small drops coalesce into one big drop in isolation. The temperature of the result is: (a) unchanged (b) higher (c) lower (d) unpredictable.

<details><summary>Solution</summary>

Surface area shrinks; released $\gamma\Delta A$ thermalises: **(b)** (Q25's energy, block 4).

</details>

### P10 · 4 marks

A floating body is stable for small heel when: (a) $G$ above $M$ (b) $M$ above $G$ (c) $B$ above $G$ always (d) $I$ small.

<details><summary>Solution</summary>

**(b)**; metacentre above centre of mass gives a righting couple (§3.5).

</details>

### P11 · 4 marks

In a siphon the speed is $2$ m/s and the top is $2$ m above the supply level. With $p_0=10^5$ Pa, $p_{top}$ is nearest: (a) $7.9\times10^4$ Pa (b) $10^5$ Pa (c) $5.9\times10^4$ Pa (d) $2\times10^4$ Pa.

<details><summary>Solution</summary>

$p_{top}=p_0-\rho g h-\tfrac12\rho v^2=10^5-19600-2000=7.84\times10^4$ Pa. **(a)** (§3.9).

</details>

### P12 · 4 marks

A horizontal tube of length $L$ filled with liquid rotates about one end at $\omega$. The pressure difference between the ends is: (a) $\tfrac12\rho\omega^2L^2$ (b) $\rho\omega^2L^2$ (c) $\rho g L$ (d) $0$.

<details><summary>Solution</summary>

$\int_0^L\rho\omega^2r\,dr=\tfrac12\rho\omega^2L^2$. **(a)** (§3.4, OL9).

</details>

#### Section B · One or more correct

### P13 · 4 marks

Ice floats in water in a vessel. Mark the correct statements: (a) melting ice with an embedded stone *denser* than water lowers the level; (b) melting ice with an air bubble changes the level; (c) melting pure ice in salt water raises the level; (d) melting pure ice in the same fresh water leaves the level unchanged.

<details><summary>Solution</summary>

**(a), (c), (d)**. (b) is false: negligible bubble mass (§3.6, E7).

</details>

### P14 · 4 marks

About Bernoulli's equation as used in this chapter: (a) it is the work–energy theorem per volume; (b) it holds across streamlines in any steady flow; (c) viscosity enters as a head-loss term in its extended engineering form; (d) it requires compressibility.

<details><summary>Solution</summary>

**(a), (c)**. (b) needs irrotational flow; (d) is the opposite (§3.8).

</details>

### P15 · 4 marks

A soap bubble is inflated slowly at constant $T$: (a) internal excess pressure falls as it grows; (b) the work you do exceeds $\gamma\Delta A$ of the two surfaces if you count pushing air in against $p_0$; (c) the film tension $\gamma$ of the solution is constant; (d) the bubble's internal pressure is below $p_0$.

<details><summary>Solution</summary>

**(a), (b), (c)**. (d) false: $p_0+4\gamma/r$ (§3.15).

</details>

### P16 · 4 marks

A ball denser than water is released just below the surface in a tall tank on a scale. During the sinking at terminal-like acceleration (ignore viscous detail): (a) the scale reads more than the water's weight from the instant of release; (b) the reading equals water+ball weight only after the ball rests at the bottom; (c) while the ball accelerates downward, the reading is less than water+ball weight; (d) the reading never changes.

<details><summary>Solution</summary>

**(b), (c)**: while the ball accelerates down, the system's centre of mass accelerates down, so the normal force is below the total weight; after rest, the full weight returns. (Block 3 synthesis.)

</details>

### P17 · 4 marks

A vessel accelerates horizontally at $a$: (a) the free surface tilts by $\tan\theta=a/g$; (b) a fully submerged balloon on a string tied to the floor leans along $\mathbf a$; (c) a hanging strap leans along $\mathbf a$; (d) equipressure surfaces stay horizontal.

<details><summary>Solution</summary>

**(a), (b)**. (c) leans against $\mathbf a$; (d) tilt with the surface (§3.4, E6).

</details>

### P18 · 4 marks

Capillary rise $h=2\gamma\cos\theta/\rho g r$. Correct: (a) on the Moon ($g/6$) the rise is $6h$; (b) doubling $r$ halves $h$; (c) at $\theta=90^\circ$ there is neither rise nor depression; (d) heating the liquid (lowering $\gamma$) raises $h$.

<details><summary>Solution</summary>

**(a), (b), (c)**. (d) is backwards (§3.16).

</details>

### P19 · 4 marks

Two tubes of radii $r$ and $2r$, equal lengths, carry a viscous flow under a total drop $\Delta p$. Mark the correct statements: (a) in series, the narrow tube takes $16/17$ of $\Delta p$; (b) in parallel under the same $\Delta p$, the wide tube carries $16\times$ the flow of the narrow one; (c) in series the flow *speed* is equal in both; (d) doubling both lengths doubles $\Delta p$ at fixed $Q$.

<details><summary>Solution</summary>

**(a), (b), (d)**. (c) false: $v\propto1/A$ by continuity (§3.12, Q19).

</details>

### P20 · 4 marks

About Stokes' law and terminal velocity: (a) $v_t\propto r^2$ in the Stokes regime; (b) the law is reliable for $\text{Re}\lesssim1$; (c) terminal velocity makes the drag equal to weight minus buoyancy; (d) in a vacuum chamber the same sphere reaches the same $v_t$.

<details><summary>Solution</summary>

**(a), (b), (c)**. (d) nonsense: $\eta\to0$ removes the drag (§3.13).

</details>

#### Section C · Numerical

### P21 · 5 marks

A vessel holds $0.5$ m of oil ($800$) over $1.0$ m of water. Gauge pressure at the bottom, in kPa to two significant figures?

<details><summary>Solution</summary>

$800\times9.8\times0.5+1000\times9.8\times1.0=3920+9800=13720$ Pa ≈ **14 kPa**. (§3.1.)

</details>

### P22 · 5 marks

A tank of water height $1.8$ m has a hole at depth $0.8$ m. Horizontal range on the ground at the tank base, in metres?

<details><summary>Solution</summary>

$x=2\sqrt{0.8\times1.0}=1.79$ m ≈ **1.8 m**. (§3.10.)

</details>

### P23 · 5 marks

Water in a clean $0.2$ mm radius tube rises $h$ cm. Give $h$ to two significant figures ($\gamma=0.0728$, $\theta=0$).

<details><summary>Solution</summary>

$h=2\times0.0728/(1000\times9.8\times2\times10^{-4})=0.0743$ m = **7.4 cm**. (§3.16.)

</details>

### P24 · 5 marks

$A/a=200$, $H=0.8$ m. Emptying time in seconds (nearest integer)?

<details><summary>Solution</summary>

$T=200\sqrt{1.6/9.8}=200\times0.404=80.8$ ≈ **81 s**. (OL1.)

</details>

### P25 · 5 marks

A $1$ mm radius sphere ($\rho=1100$) sinks in water at Stokes terminal speed; give $v_t$ in mm/s (nearest integer; ignore the regime caveat but state it).

<details><summary>Solution</summary>

$v_t=2(10^{-3})^2(100)(9.8)/(9\times10^{-3})=2\times10^{-6}\times980/9\times10^{-3}=1.96\times10^{-3}/9\times10^{-3}=0.218$ m/s $=218$ mm/s. Regime: Re$\approx440$ — Stokes invalid; the honest answer would use quadratic drag ($\sim0.06$ m/s). Grading wants the formula value **218** with the caveat named. (§3.13, E9.)

</details>

### P26 · 5 marks

A cuboid barge $10$ m × $6$ m floats at draft $1$ m. $BM=I/V$ in metres (nearest integer)?

<details><summary>Solution</summary>

$I=Lb^3/12=10\times216/12=180$ m$^4$; $V=60$ m$^3$; $BM=3$ m. **3**. (§3.5.)

</details>

#### Section D · Comprehensive long-form

### P27 · 9 marks

A cylindrical tank ($A=0.2$ m$^2$) holds water to $H=0.45$ m. A sharp orifice $a=1$ cm$^2$ opens at the base. (a) Derive $T=(A/a)\sqrt{2H/g}$ from first principles (3). (b) Evaluate $T$ (2). (c) State quantitatively when the quasi-steady assumption is safe here, and what changes in the last 1 cm of depth (4).

<details><summary>Solution</summary>

(a) Continuity $Av_{s}=av$ with $v=\sqrt{2gh}$ (Bernoulli, $a\ll A$): $-A\,dh/dt=a\sqrt{2gh}$; separate and integrate as OL1(a): $T=(A/a)\sqrt{2H/g}$. Marking: continuity 1, Torricelli 1, integration 1. (b) $T=200\times\sqrt{0.9/9.8}=200\times0.303=60.6$ s (2). (c) $a/A=5\times10^{-3}$, surface speed $\le v\,a/A\approx2.9\times0.005=0.015$ m/s against $v\approx2.9$ m/s: 0.5% error, safe (2). In the last centimetre $v$ is small, the orifice's own discharge coefficient and surface tension/viscous effects (ignored throughout) become comparable, and the jet ceases to be a clean Torricelli jet — the model's remainder, stated honestly (2).

</details>

### P28 · 9 marks

A bucket of radius $0.25$ m holds water to $0.20$ m and is spun at $\omega$. (a) Show the free surface is a paraboloid (3). (b) Find $\omega$ at which the base centre is first exposed (3). (c) Find the volume spilled by the time the rim is first reached, or show none has spilled yet (3).

<details><summary>Solution</summary>

(a) OL2(a): $\tan\alpha=\omega^2r/g$, integrate, paraboloid. (b) While nothing spills, volume conservation pins the surface pivot at the rest level $0.20$ m, so the centre has dropped by half the rim-to-centre difference; the base centre is first exposed when that drop equals $0.20$ m, i.e. when the rim-to-centre difference $\omega^2R^2/2g=0.40$ m. Then $\omega^2=0.40\times2\times9.8/0.0625=125.4$, $\omega=11.2$ rad/s. (c) At that speed the rim level stands at $0.20+0.20=0.40$ m; a bucket taller than $0.40$ m has therefore spilled nothing, which the symmetry of the paraboloid confirms (volume above the rest level equals volume below it). State the bucket-height condition as part of the answer.

</details>

### P29 · 9 marks

A vertical rectangular gate $1.5$ m wide holds water to depth $2.4$ m on one side, hinged at the bottom. (a) Total force (3). (b) Torque about the hinge (3). (c) The horizontal force at the top latch needed to hold the gate (3).

<details><summary>Solution</summary>

(a) $F=\rho g h_c A=1000\times9.8\times1.2\times(1.5\times2.4)=4.23\times10^4$ N. (b) Centre of pressure at $2H/3=1.6$ m from top $=0.8$ m above hinge: $\tau=4.23\times10^4\times0.8=3.39\times10^4$ N·m. (c) Latch at $2.4$ m: $F_L=\tau/2.4=1.41\times10^4$ N. Checks: $F$ scales as $H^2$ ✓.

</details>

### P30 · 9 marks

A U-tube manometer connects a gas bulb (left limb) to the atmosphere (right limb). The left limb holds $20$ cm of water above a water–mercury interface; the right limb's mercury surface stands $12$ cm *above* that interface. Find the gas gauge pressure, and then the reading when the whole apparatus rides a lift accelerating upward at $g$ (4+5).

<details><summary>Solution</summary>

Pressure walk from the bulb: $p_{gas}+\rho_w g(0.20)$ at the interface; climb the mercury column $0.12$ m to the open surface where $p=0$ gauge: $p_{gas}=\rho_{Hg}g(0.12)-\rho_w g(0.20)=13600\times9.8\times0.12-1000\times9.8\times0.20=15994-1960=1.40\times10^4$ Pa gauge. In the lift $g_{eff}=2g$ and every column term doubles: $2.81\times10^4$ Pa gauge — a manometer reads pressure *in metres of its own liquid under local gravity*, so the height pattern is unchanged while the pascal value doubles. Marking: walk 2, arithmetic 2, $g_{eff}$ identification 2, doubling argument 2, units and gauge/absolute statement 1.

</details>

### P31 · 9 marks

Ice of mass $0.9$ kg embeds a stone of $0.1$ kg ($\rho=2500$), floating in fresh water in a cylinder of area $0.05$ m$^2$. (a) Displaced volume while floating (2). (b) Level change after melting, in mm with direction (4). (c) The same ice–stone floating on a $1$ cm oil layer ($800$) over water: does the stone-on-bottom conclusion change qualitatively? (3)

<details><summary>Solution</summary>

(a) $V_1=1.0/1000=10^{-3}$ m$^3$. (b) After: melt $0.9/1000=9\times10^{-4}$ plus stone $0.1/2500=4\times10^{-5}$: $9.4\times10^{-4}$; deficit $6\times10^{-5}$ m$^3$; $\Delta h=6\times10^{-5}/0.05=1.2$ mm **fall**. (c) No: the ledger compares displaced weight with after-volumes; the oil merely changes which fluid supplies the displacement while floating, and both after-states (melt in water/ oil, stone at bottom) shift by the same bookkeeping; level still falls. Marks: ledger 2, numbers 2, sign 1, oil argument 3, check 1.

</details>

### P32 · 9 marks

Air flows in a duct; a pitot-static pair reads $\Delta p=60$ Pa ($\rho_{air}=1.2$). (a) The speed (3). Downstream a venturi of area ratio 2 carries water at $Q=2\times10^{-3}$ m$^3$/s in a $4$ cm$^2$ throat... (b) find the water manometer difference in cm (4). (c) State why the two instruments read differently in kind (2).

<details><summary>Solution</summary>

(a) $v=\sqrt{2\Delta p/\rho}=\sqrt{120/1.2}=10$ m/s. (b) $v_2=Q/A_2=5$ m/s; $v_1=2.5$ m/s; $\Delta p=\tfrac12\times1000(25-6.25)=9375$ Pa; water column $=9375/(1000\times9.8)=0.957$ m = 95.7 cm. (c) Pitot compares stagnation with static on *one* streamline (speed sensor); Venturi compares two statics on *different* sections (flow-rate sensor via continuity); both are (3.8) with different gate uses.

</details>

### P33 · 9 marks

Water rises $10$ cm in a capillary. (a) The tube is tilted $60^\circ$ from vertical: the length of water column along the tube (3). (b) A second identical tube only $6$ cm long stands vertical: meniscus radius ratio $R'/R$ (3). (c) The short tube is now in the $60^\circ$ tilt: does it overflow? Justify quantitatively (3).

<details><summary>Solution</summary>

(a) The supported quantity is the *vertical* height, so the slant length is $\ell=h/\cos60^\circ=0.20$ m. (b) $hR=h'R'$: $R'/R=10/6=5/3$. (c) No overflow, ever: tilted, the tube offers a vertical height of $6\cos60^\circ=3$ cm against the required $10$ cm, so the meniscus simply flattens to $R''=R\times10/3$ and sits at the lip with a nearly flat face. The invariant is "a capillary adjusts curvature, never overflows"; the $hR$ arithmetic above is its quantitative form.

</details>

### P34 · 9 marks

A steel sphere ($r=2$ mm, $\rho=7800$) falls through $1$ m of oil ($\rho=900$, $\eta=0.5$) then $1$ m of water ($\eta=10^{-3}$). (a) Terminal speed in oil and the time across the oil assuming terminal from entry (4). (b) In water, which drag regime governs? Estimate the water transit time crudely with quadratic drag, $C_d=0.44$ (5).

<details><summary>Solution</summary>

(a) $v_t=2r^2(\rho-\sigma)g/9\eta=2(4\times10^{-6})(6900)(9.8)/(4.5)=0.12$ m/s; Re$=900\times0.12\times4\times10^{-3}/0.5=0.86<1$ ✓ honest; $t=1/0.12=8.3$ s. (b) In water, Stokes would give $v_t=2(4\times10^{-6})(6800)(9.8)/(9\times10^{-3})=59$ m/s at Re$\sim10^5$ — the regime test rejects it, so quadratic drag governs, and even that terminal speed is $v_t=\sqrt{8r(\rho_s-\rho_w)g/(3C_d\rho_w)}=\sqrt{8\times2\times10^{-3}\times6800\times9.8/(3\times0.44\times1000)}=\sqrt{808}=28$ m/s. Neither is attainable over one metre: the approach distance scales as $v_t^2/g'\approx80$ m. The sphere therefore accelerates from its $0.12$ m/s entry at the buoyancy-reduced gravity $g'=g(1-\rho_w/\rho_s)=9.8\times0.872=8.5$ m/s$^2$, and $1=\tfrac12 g't^2$ gives $t=0.49$ s. The exam point is the recognition itself: name the regime, then prove terminal is never reached (the two-timescale thinking of OL1/OL3).

</details>

### P35 · 9 marks

A jet of area $a=2$ cm$^2$ at $v=15$ m/s strikes a curved vane moving away at $u=5$ m/s that turns the relative flow by $120^\circ$. (a) Force on the vane along the jet (4). (b) Power delivered (2). (c) The efficiency $\eta=Pu/( \tfrac12\dot m v^2)$ and its maximum over $u$ (3).

<details><summary>Solution</summary>

(a) Relative speed $w=v-u=10$ m/s; mass rate arriving at the vane $\dot m=\rho a w=1000\times2\times10^{-4}\times10=2$ kg/s. The exit relative velocity makes $120^\circ$ with the entry direction, so the along-jet momentum change per unit mass is $w-w\cos120^\circ=w(1+\tfrac12)=15$ m/s, and $F=\dot m\times15=30$ N. (b) $P=Fu=30\times5=150$ W. (c) Jet power available $=\tfrac12\rho a v^3=0.5\times1000\times2\times10^{-4}\times3375=337.5$ W, so $\eta=150/337.5=0.44$. In general $P(u)=\rho a(v-u)(1+\cos\phi)\,u$; maximising over $u$ gives $u=v/2$ and $\eta_{max}=(1+\cos\phi)/2=0.75$ for $\phi=120^\circ$.

> [!success] Check
> $u\to0$ and $u\to v$ both give $P\to0$, so an interior maximum must exist ✓; $\phi=180^\circ$ (perfect reversal) gives the Pelton-wheel limit $\eta_{max}=1$ ✓.

</details>

### P36 · 9 marks

(a) Derive $v=\sqrt{gh}$ for a shallow-water bump from continuity and momentum in the wave frame (4). (b) A $3$ cm high bump moves over $0.5$ m depth; its speed (2). (c) Explain in two sentences why the same machinery predicts a hydraulic jump when a fast shallow stream decelerates, and name the quantity that increases across the jump (3).

<details><summary>Solution</summary>

(a) As OL7: continuity $ch=c'(h+\eta)$; momentum $\tfrac12\rho gh^2+\rho c^2h=\tfrac12\rho g(h+\eta)^2+\rho c'^2(h+\eta)$; eliminate $c'$: $c^2=g(h+\eta)(1+\eta/2h)\to gh$. (b) $v=\sqrt{9.8\times0.5}=2.2$ m/s (correction $+3\eta/4h\approx4.5\%$: 2.3 m/s; accept 2.2–2.3). (c) The equations admit a discontinuous (shock-like) solution when the incoming Froude number $v/\sqrt{gh}>1$; the jump is where kinetic energy is irreversibly converted to heat and surface elevation — entropy increases across it, selecting the jump direction. Hand-off: the entropy language is [[Thermodynamics|thermodynamics]]'; the wave kinematics [[String-waves|string waves]]'.

</details>

## Part 12 · Marking scheme and post-paper audit

| Section | Marks each | Questions | Subtotal |
|---|---:|---:|---:|
| A | 4 | 12 | 48 |
| B | 4 | 8 | 32 |
| C | 5 | 6 | 30 |
| D | 9 | 10 | 90 |
| **Total** | | 36 | **200** |

**Which block each question tested.** A: P1 §3.4, P2 §3.5, P3 §3.2, P4 §3.10, P5 §3.15, P6 §3.16, P7 §3.7, P8 §3.13, P9 §3.14, P10 §3.5, P11 §3.9, P12 §3.4. B: P13 §3.6, P14 §3.8, P15 §3.15, P16 §3.5, P17 §3.4, P18 §3.16, P19 §3.12, P20 §3.13. C: P21 §3.1, P22 §3.10, P23 §3.16, P24 OL1, P25 §3.13, P26 §3.5. D: P27 OL1, P28 OL2, P29 §3.3, P30 §3.2+§3.4, P31 §3.6, P32 §3.9, P33 §3.16, P34 §3.13+OL3, P35 §3.11, P36 OL7+§10.1. Blocks 2–4 and 10 all appear, as §1.7 requires.

**Diagnostic table.**

| If you lost marks on… | the likely gap | reread |
|---|---|---|
| P1, P6, P17, P30-lift | $\mathbf g_{eff}$ not automatic | §3.4, T1 |
| P2, P13, P16, P31 | displaced-volume ledger | §3.5–3.6, T2 |
| P4, P22, P27 | Torricelli family and quasi-steadiness | §3.10, OL1 |
| P5, P9, P15 | surface counting and the factor 2 | §3.14–3.15, T6 |
| P7, P12, P19, P25 | continuity/Poiseuille/regime discipline | §3.7, §3.12–3.13 |
| P11, P21, P30 | manometer walking and gauge/absolute | §3.2, T3 |
| P26, P10 | stability and the metacentre | §3.5 |
| P28, P36 | rotating-frame energy and wave-frame methods | OL2, OL7 |

## Part 13 · Formula sheet

| formula | validity |
|---|---|
| $dp/dy=-\rho g$; $p=p_0+\rho g h$ | static, constant $\rho$, one fluid |
| $F=p_cA$; centre of pressure $2H/3$ (vertical rectangle from surface) | plane surface |
| $\tan\theta=a/g$; $z=z_0+\omega^2r^2/2g$ | rigid acceleration / rotation, settled |
| $p-\tfrac12\rho\omega^2r^2+\rho gz=\text{const}$ | rotating-frame statics |
| $F_b=\rho_fVg$ at centre of buoyancy | hydrostatic surroundings |
| $V_s/V=\rho_b/\rho_f$; $BM=I/V$ | float; small heel |
| $Av=Q$ | steady, incompressible |
| $p+\tfrac12\rho v^2+\rho gy=\text{const}$ | the four gates |
| $Q=A_1\sqrt{2\Delta p/(\rho(A_1^2/A_2^2-1))}$ | Venturi |
| $v=\sqrt{2\Delta p/\rho}$ | pitot |
| $v=\sqrt{2gh}$; $x=2\sqrt{h(H-h)}$; $T=(A/a)\sqrt{2H/g}$ | small hole, quasi-steady |
| $F=\rho a v^2$ (jet thrust); $\rho a(v-u)^2$ (moving plate) | momentum flux |
| $F/A=\eta\,dv/dy$; $Q=\pi R^4\Delta p/8\eta L$; $R_{hyd}=8\eta L/\pi R^4$ | Newtonian; laminar; no slip |
| $F_d=6\pi\eta rv$; $v_t=2r^2(\rho-\sigma)g/9\eta$; $\text{Re}=\rho vD/\eta$ | $\text{Re}\lesssim1$ |
| $\gamma=F/L=W/\Delta A$ | definition pair |
| $\Delta p=2\gamma/r$ (drop), $4\gamma/r$ (bubble), $\gamma(1/r_1+1/r_2)$ (general) | spherical / smooth patch |
| $h=2\gamma\cos\theta/\rho gr$; $hR=h'R'$ (short tube) | Jurin; curvature adjusts |
| $v=\sqrt{gh}$ | shallow-water, small amplitude |
| Numbers: $p_0=1.013\times10^5$ Pa; water barometer $10.3$ m; $\gamma_w=0.0728$ N/m; $\eta_w=10^{-3}$ Pa·s; $\eta_{air}=1.8\times10^{-5}$; $B_w=2.2\times10^9$ Pa; $\rho_{Hg}=13.6\rho_w$ | — |

## Part 14 · Checkpoint and hand-off

- [ ] I can prove pressure is isotropic from a shrinking wedge, and derive $dp/dy=-\rho g$.
- [ ] I can walk any manometer, including accelerated ones, without re-deriving.
- [ ] I can state Pascal's law as a consequence of incompressibility and audit a lift's energy.
- [ ] I can compute forces and centres of pressure on plane, inclined and curved surfaces.
- [ ] I can handle linearly accelerated and rotating vessels, including the balloon and the paraboloid.
- [ ] I can derive Archimedes twice and use the displaced-volume ledger on any level-change question.
- [ ] I can state and police the four Bernoulli gates, and know when Poiseuille replaces Bernoulli.
- [ ] I can run Torricelli, range, drainage-time, Venturi, pitot and siphon problems with their conditions.
- [ ] I can compute jet and ejection thrusts by momentum flux.
- [ ] I can derive Poiseuille by a shell balance and combine hydraulic resistances.
- [ ] I can use Stokes with its Reynolds-number caveat and the quadratic regime beyond.
- [ ] I can treat surface tension as force and energy, count surfaces, and derive the excess-pressure family.
- [ ] I can derive Jurin twice and solve the short-tube and tilted-tube variants.
- [ ] I can derive $v=\sqrt{gh}$ in the wave frame and say where the model breaks.

**What the next chapters inherit.** PART 12 (elasticity) inherits the shell-balance technique of Poiseuille and the energy-method discipline; the pressure-gradient argument reappears in stress analysis. PART 13 (electrostatics) inherits the flux-and-symmetry habits of the hydrostatic equation (the $\nabla p\parallel\mathbf g_{eff}$ argument has a direct Coulomb analogue). The momentum-flux method returns in PART 11's sibling topics and in [[Electromagnetic-waves#Part 3 · Core derivations|EM waves]] as radiation pressure. The shallow-water bridge hands wave kinematics to [[String-waves|string waves]].

**Open questions now attackable.** Why does a boiled egg spin differently (rigid-body hand-off to PART 8)? Why do tea leaves gather at the centre of a stirred cup (secondary flows beyond this model)? How tall can a mountain be (elasticity, PART 12)? Each is a one-line extension of a tool in this chapter plus one from a later one.
