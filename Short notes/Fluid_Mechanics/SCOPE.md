# Fluid mechanics — coverage and classification

Primary source: `../../fluid-mechanics/Fluid-mechanics.md` (unedited). The Cengage
chapter it cites is the book floor behind that file; it is not in this repository,
so no claim is made about material that exists only in the printed book.

## The rule used to split the chapter

Part I is everything a JEE Main + Advanced candidate is expected to own: the
hydrostatic equations and their standard geometries, buoyancy and stability,
Bernoulli with its four gates, the device set, Torricelli and draining, momentum
flux, Poiseuille flow and hydraulic resistance, Stokes drag with a Reynolds check,
surface energy and the excess-pressure family, and Jurin's law.

Part II is the same physics pushed into places the school syllabus does not go:
the two draining regimes and their crossover, three derivations of the rotating
surface, the Stokes-to-quadratic drag crossover for a raindrop, the energy proof
of Young–Laplace and the catenoid limit, pendant-drop weighing, the water strider,
xylem tension in tall trees, shallow-water waves, the reverse sprinkler, the
rotating-frame energy audit, and a viscometer with both corrections.

The boundary is **relevance and prerequisite**, not difficulty. Nothing in Part II
is claimed to be impossible in an Olympiad or a JEE Advanced paper; several items
(Poiseuille, surface energy, the rotating surface) are already JEE Advanced scope.
Conversely, no Part I sheet claims to be sufficient for every JEE question: it is
a short-note set, not a question bank.

## Page map

### Part I — JEE Main + Advanced (19 sheets)

| # | Question on the sheet | Core result |
|---|---|---|
| 01 | Why does depth, not shape, set the pressure? | `p_x=p_y=p_θ`, `dp/dy=−ρg`, `p=p₀+ρgh`, gauge vs absolute, barometer |
| 02 | How do you walk a U-tube without writing force balances? | manometer walk, Pascal lift, `F₂/F₁=A/a`, work equality |
| 03 | Where does the push on a gate act? | `F=p_cA`, centre of pressure `2H/3` for a rectangle from the surface, hydrostatic paradox |
| 04 | How much force does a curved face feel? | projection theorem, `F_H` on the projected rectangle, `F_V` on the column above, resultant through the centre |
| 05 | What changes when the tank moves? | `tanθ=a/g`, effective gravity, balloon and plumb line |
| 06 | Why does the coffee climb the wall? | `z=z₀+ω²r²/2g`, volume conservation, centre drop = rim rise |
| 07 | What is a floating body really displacing? | Archimedes twice, `V_sub/V=ρ_b/ρ_f`, apparent weight |
| 08 | When does a floating body stay upright? | `BM=I/V`, metacentre, righting moment |
| 09 | Does the level rise when the ice melts? | the four-case ledger (ice, ice+stone, ice+bubble, ice in salt water) |
| 10 | When may you use Bernoulli? | derivation, the four gates, head form |
| 11 | How do Venturi, pitot and siphon read a pressure difference? | `Q=A₁A₂√(2Δp/ρ(A₁²−A₂²))`, `v=√(2Δp/ρ)`, siphon limit |
| 12 | How fast does water leave a hole, and where does it land? | `v=√(2gh)`, `x=2√(h(H−h))`, `T=(A/a)√(2H/g)` |
| 13 | Why is a hose a force? | `F=ρav²`, `F=ρa(v−u)²`, `1−cosφ` |
| 14 | Why does a narrow pipe change the flow? | `τ=rΔp/2L`, parabola, `Q=πR⁴Δp/8ηL` |
| 15 | How do pipes combine like resistors? | `R=8ηL/πR⁴`, series add, parallel split as `r⁴` |
| 16 | How fast does a small sphere sink? | `v_t=2r²(ρ−σ)g/9η`, `Re=ρvD/η`, quadratic crossover |
| 17 | Why is a soap film a stretched sheet? | `γ=F/2L`, `W=γΔA`, film has two faces |
| 18 | Why is the pressure inside a bubble higher? | `2γ/r` drop, `4γ/r` bubble, `γ/r` jet |
| 19 | How high does water climb a narrow tube? | `h=2γcosθ/ρgr`, `hR=h′R′`, tilt, energy check |

### Part II — Olympiad / specialised extensions (11 sheets)

| # | Question on the sheet | Core result |
|---|---|---|
| 01 | Why does a tank empty in finite time but a viscous one never does? | `T=(A/a)√(2H/g)`, `τ=8ηLA/(πr⁴ρg)`, crossover `h*` |
| 02 | Three ways to derive the rotating surface | force balance, equipotential, centrifugal head |
| 03 | Where does Stokes drag hand over to quadratic drag? | `r*≈4×10⁻⁵ m`, 2 mm drop ≈ 9.9 m/s |
| 04 | Why is a soap film a minimal surface? | energy proof of `Δp=γ(1/R₁+1/R₂)`, catenoid limit `d/R≲1.33` |
| 05 | Measuring gamma with a drip, and why no strider sinks | Tate's law `mg≈2πrγf`, two-leg contact `≈0.035 N` |
| 06 | How high can a tree suck? | `5.9 m` capillary, `10.3 m` pressure, tension and cavitation |
| 07 | Why does a shallow wave follow `√(gh)`? | continuity plus momentum, first-order steepening |
| 08 | Which way does a reverse sprinkler turn? | ejection reaction vs suction, ideal torque zero |
| 09 | Where does the energy come from in a rotating U-tube? | `ΔK/m=½ω²(r₂²−r₁²)`, motor torque |
| 10 | Rethink a real measurement: glycerine viscosity | Stokes, Ladenburg wall correction, timed fall |
| 11 | Where does this chapter stop being true? | six-box triage, five failure modes |

## Deliberate omissions

* Turbulence modelling, boundary-layer theory, drag crises, vortex shedding.
* Compressible flow beyond the bulk-modulus/`√(B/ρ)` limit.
* Non-Newtonian constitutive models (the sheets state only where the linear law dies).
* Capillary waves, Marangoni flow, contact-angle hysteresis beyond the stated
  advancing/receding remark.
* Numerically solved flows: every curve on every sheet is a closed form.

## Honesty statement

The sheets are a *short-note* rendering of the source, checked for the items listed
in `SOURCE-AUDIT.md`. They are not a substitute for the source, for a textbook, or
for solving problems. See `README.md` for exactly what the automated checks do and
do not cover.
