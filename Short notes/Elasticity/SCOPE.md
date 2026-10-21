# Scope and concept-by-concept classification

Membership is **relevance and prerequisite**, not difficulty and not the
source's own headings. Part I keeps every JEE-relevant result, including the
algebraically demanding composite, drop and torsion problems. Part II isolates
theory that needs a model the chapter does not otherwise use.

**No claim is made that an extension can never appear in JEE.** Several Part II
sheets are ordinary mechanics once the extra idea is supplied; Mohr's circle in
particular is a standard transformation that a strong JEE student can use. The
split says "additional theory or a longer derivation", not "off-syllabus".

## Part I — JEE Main + Advanced (8 sheets, 32 cards)

The organising spine is the triage order used on sheet 08: **mode → section →
load history → formula → limit check**.

- **01 Material response** — stress and strain on a named cut plane; the four
  modes (tension, compression, volume, shear); the pairs (σ, ε), (p, ΔV/V),
  (τ, γ); reading a stress–strain curve through proportional limit, yield,
  ultimate and fracture; why the elastic region is a fraction of a percent of
  strain. *Prerequisite for everything else.*
- **02 Moduli and Poisson** — definitions of Y, B, G and ν; the two exact
  interrelations Y = 3B(1 − 2ν) and Y = 2G(1 + ν), each derived from
  superposition; the admissible range −1 < ν < 0.5 and the physical meaning of
  each bound. *Needed before composite and wave problems.*
- **03 Extension family** — k = YA/L; series (common force) and parallel (common
  extension) as the two constraint statements; self-weight by integration,
  giving mgL/2AY; the hanger and sag geometries. *The highest-frequency JEE
  calculation block.*
- **04 Composite and thermal** — thermal strain αΔT, blocked stress YαΔT, the
  free/partial/fully constrained decision, the two-material composite with a
  compatibility equation, shrink fits and the quarter-turn bolt. *Combines 02
  and 03; kept in Part I because it is a standard Advanced multi-step question.*
- **05 Energy and impact** — ½σε per volume, ½kδ², the factor 2 for a suddenly
  applied load, the drop formula
  Δ = Δ_st(1 + √(1 + 2h/Δ_st)), and double shear. *Energy methods are JEE core;
  the wave-transit caveat is deferred to Part II sheet 03.*
- **06 Torsion and bending** — θ = TL/GJ with J = πR⁴/2; the I-section
  comparison at fixed mass; M = YI/R and the neutral axis; the cantilever
  FL³/3YI. *Standard Advanced material; the double integration is Part II.*
- **07 Yield, fatigue, materials** — plastic deformation, hysteresis, specific
  strength σ/ρ and specific modulus Y/ρ, Ashby-style selection, buckling versus
  crushing as competing failure modes, toughness and safety factors. *Kept in
  Part I as the "which material" reasoning JEE asks for.*
- **08 Toolkit** — the five-step triage, the four unrelated factors of two, a
  short table of numbers to carry, and the scaling laws. *Deliberately a
  synthesis page, not new theory.*

## Part II — Olympiad / specialised extensions (9 sheets, 36 cards)

- **01 The interatomic spring** — U(r) curvature sets Y ≈ D/r₀³, the bond spring
  constant k_a ≈ Yr₀ and the Debye-scale vibration frequency; why B comes from
  the same well. *Needs a pair-potential model.*
- **02 Thermal expansion as well asymmetry** — the cubic term, the Boltzmann
  average ⟨s⟩ = −γk_BT/(2k²), α ≈ k_B/2D, and where the model fails (Invar,
  anisotropy). *Needs statistical averaging.*
- **03 Falling weight with rod mass** — energy with a distributed mass, the
  quadratic for δ, the wave-transit validity condition L/c, and the m/3 dynamic
  effective mass. *Needs a modal assumption and a wave-speed argument.*
- **04 Constant-stress rod** — σ₀A(x) = W + ∫ρgA dx′ gives exponential flare;
  λ = σ₀/ρg; steel 3.3 km, wood 7 km, bone 10 km; the real limits are buckling
  and tree hydraulics. *Needs a differential balance.*
- **05 Bending integrated** — d²y/dx² = M/YI, boundary conditions, uniform load
  wL⁴/8YI, pinned FL³/48YI, fixed–fixed FL³/192YI, and the (h/L)² shear
  criterion. *Needs two integrations; the cantilever result alone stays in JEE 06.*
- **06 Euler buckling** — dimension argument, sine mode, P_cr = π²YI/(κL)²,
  κ = 1, 2, 0.5, 0.7, hollow sections at equal mass, and inelastic limits.
  *Needs an eigenvalue argument; JEE 07 only compares buckling with crushing.*
- **07 I-beam and vessel** — the fair "same depth, same area" comparison (factor
  1.9), hoop and longitudinal stress by free-body cuts, sphere pr/2t, and the
  scale dependence of a silk strand. *Extends JEE 06/07 with careful comparisons.*
- **08 Seismic waves** — v_rod = √(Y/ρ), v_S = √(G/ρ), v_P = √((B + 4G/3)/ρ),
  inverting two arrivals to B and G, and the S-wave shadow as evidence for a
  liquid core. *Needs wave speeds and a spherical-Earth picture.*
- **09 Plane stress, principal axes, Mohr** — the stress element, principal
  stresses, Mohr's circle to scale, and the mean/deviatoric split in 3D.
  *Explicitly an added extension; the algebra is short but the tensor idea is
  beyond the chapter.*

## Deliberately not covered

- Finite-element or numerical beam solutions; tapered or curved beams beyond
  the constant-stress case.
- Anisotropic elasticity (wood, fibre composites beyond the transformed-section
  idea), viscoelasticity and creep laws.
- Thick-walled cylinders (Lamé), contact stress, fracture-mechanics K-fields.
- Full seismic ray theory, attenuation and anisotropy; sheet 08 stops at
  isotropic homogeneous speeds.
- Plastic collapse mechanisms and shakedown; sheet 07 names the concepts and
  gives the safety-factor bookkeeping only.

These are gaps, not omissions by accident. The source chapter also stops at
these boundaries, and inventing the missing theory would have violated the
"do not invent content" rule.
