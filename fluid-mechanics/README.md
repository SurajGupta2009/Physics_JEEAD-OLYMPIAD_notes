# Fluid Mechanics & Surface Tension — first principles to Olympiad

> [!note] Part 11 of [plan.md](../plan.md) · text-only Markdown chapter · written for Obsidian reading mode

**Scope.** Hydrostatics from the isotropy proof and $\frac{dp}{dy}=-\rho g$; barometers, manometers and the step method; Pascal and the hydraulic lift with its energy audit; pressure diagrams and forces on plane, inclined and curved surfaces; fluids in linearly accelerated and rotating vessels (tilted surfaces, the balloon, the paraboloid); Archimedes derived twice with the centre of buoyancy and the metacentre; the melting-ice family as one ledger; continuity and Bernoulli from the work–energy theorem with the four validity gates; Venturi, pitot, siphon, Torricelli, efflux range and momentum-flux thrust; Newton's viscosity law, Poiseuille derived by a shell balance, Stokes and terminal velocity with the Reynolds caveat; surface tension as force and energy, the excess-pressure family, Young–Laplace, Jurin's law twice and the short-tube capillary; the shallow-water speed $v=\sqrt{gh}$ as the bridge to the wave notes.

**Prerequisites.** PART 5 (Newton's laws, pseudo forces) and PART 6 (work–energy theorem); PART 7's momentum language for §3.11.

**The one idea.** Fluids carry pressure; pressure differences are forces; viscosity and surface tension matter only when the length scale is small.

**Contents.** Part 0 orientation and coverage map; 1 intuition; 2 definitions and standing assumptions; 3 core derivations §3.1–3.17; 4 results ledger; 5 exemplars E1–E10; 6 archetypes (18 rows) and Q1–Q25; 7 toolkit T1–T8; 8 traps; 9 playbook; 10 Olympiad block OL1–OL10 with the limits-and-failure section; 11 paper P1–P36; 12 marking and diagnostics; 13 formula sheet; 14 checkpoint.

**Coverage (Cengage floor).** *Cengage Mechanics II*, ch 3 Fluid Mechanics (pp. 3.1–3.69) in full — every contents-page heading carries a row in the block-0 map — plus the fluid half of ch 4 Properties of Solids and Fluids (viscosity pp. 4.20–4.24, surface tension pp. 4.26–4.31, capillarity pp. 4.32–4.37). The elastic half of ch 4 is PART 12's floor.

**Olympiad layer.** The drainage integral with its inertial/viscous two-timescale crossover and the finite-versus-infinite emptying contrast; the paraboloid derived three ways; terminal velocity in two drag regimes with the mist/rain crossover radius; Young–Laplace from virtual work and the catenoid existence limit; the drop-weight (Tate–Harkins–Brown) reconstruction of $\gamma$; the water-strider estimate and the $L$-vs-$L^3$ scaling argument; the tree-height limit (suction vs tension, $\sim10$ m vs $\sim110$ m); shallow-water wave speed from the wave-frame momentum balance; the Feynman sprinkler as a dissipation argument; a rotating-frame energy audit closing at the motor; and a Stokes viscometer reconstructed with the Ladenburg wall correction.

**Media.** All figures are described briefs (`> [!abstract] DIAGRAM D11.k`, D11.1–D11.20) with `*Search:*` lines; no image files by design.

**Gate.** `python3 tools/check.py` → ALL GOOD: 15 blocks · C×12 E×10 Q×25 OL×10 · paper 36 Q / 200 marks · 20 DIAGRAM briefs · 68 callouts · no images.

## Beyond the plan

Mirrored in `topics.json` `beyond_plan`. The PART 11 section of plan.md was the floor; the sweep added:

- the rotating-frame pressure statement $p-\tfrac12\rho\omega^2r^2+\rho gz=\text{const}$ as a single tool unifying the book's "modified manometric equation", equipressure lines and the pendulum comparison (§3.4, OL2);
- the finite-versus-infinite emptying-time contrast and the inertial/turbulent honesty note for water drains (OL1);
- the sinking-ball scale-reading family (P16), absent from the book's exercise shapes;
- the hydraulic-resistance analogy as an explicit toolkit item with its series/parallel rules (T5, Q19);
- two decision-tree DIAGRAM briefs (D11.16, D11.17) that the plan's brief list did not name, in place of two of its micro-briefs (the isotropy wedge and the floating-body force diagram, whose physics the prose carries);
- the hydraulic jump and entropy-selection closing of the paper (P36), naming the model's nonlinear failure;
- the catenoid existence limit $d/R\lesssim1.33$ stated with its physics (OL4).

**Deliberately not covered:** the plan's "rocket-in-a-fluid retarding force / whale shape" estimate (its momentum-flux method is taught in §3.11 and the item was cut for space); turbulent pipe-flow corrections beyond the Reynolds criterion (named as a failure mode in §10.1); deep-water dispersion and water hammer (hand-offs to [[String-waves]] / [[Sound-waves]] / [[Thermodynamics]]).

**Hand-off.** PART 12 inherits the shell-balance technique and the energy-method discipline; PART 13 inherits the flux-and-symmetry habits of the hydrostatic equation; the shallow-water bridge hands wave kinematics to the shipped string-waves note.
