# Theory-only audit: chapters 1–9

**Date:** 2026-09-28  
**Scope:** conceptual theory, sequence, assumptions, equations, and explanations in the core teaching sections (especially Parts 1–4). This is not a line-by-line audit of worked examples, exercise answers, Olympiad solutions, diagrams, or experimental procedures.

## Bottom line

The nine chapters form a sensible progression and cover the central mechanics foundations expected for JEE: measurement and dimensions → vectors → 1-D kinematics → 2-D/projectile and circular motion → Newtonian dynamics → work/energy/power → centre of mass and momentum → rotation → gravitation and orbits. Definitions, intuitions, derivations, validity conditions, and recaps are generally present, so the notes are pedagogically structured rather than just formula collections.

**They should not yet be described as fully complete or error-free.** The core sequence is substantially covered, but some boundaries/assumptions need to be clearer, and this pass found and corrected several specific conceptual issues. Coverage of the complete JEE experimental-skills syllabus is outside this theory-only review and should not be inferred from this result. The course also intentionally includes material beyond JEE, so enrichment should be identified as such.

## Ordering and teaching structure

The order is sound: tools first (dimensions and vectors), then motion, then causes of motion, then energy and system-level mechanics, then rigid-body rotation and gravitational applications. Chapter sections usually move from intuition/definitions to derivation, validity conditions, examples, and recap. One minor pedagogical improvement for a later edit would be to introduce the most-used vector components/coordinate conventions immediately before their first mechanics applications, with consistent axis sketches and signed examples.

## Chapter-by-chapter theory verdict

| Ch. | Topic | Verdict on coverage, correctness, and explanation |
|---|---|---|
| 1 | Units, dimensions, measurement errors | Strong core: SI, dimensions/homogeneity and limitations, significant figures, uncertainty propagation, instruments, and graph linearisation. The key limitation—that dimensional analysis cannot determine dimensionless factors or functional dependence on dimensionless variables—is explained. Treat statistical error formulae as applying under their stated random/independent-measurement assumptions. This review did not validate every instrument convention or every practical-syllabus detail. |
| 2 | Vectors | Broad and well ordered: components, dot/cross products, triple products, vector equations, polar basis, and introductory vector calculus. Most identities are correctly stated and their geometric meanings help. The vector-equation example depends on nonzero **a** and requires **a·b=0**; the note states the existence condition, but it would be clearer to collect this with the final solution. |
| 3 | 1-D kinematics | Clear and substantially complete for the core: position/displacement/distance, signed velocity, graphs, constant and variable acceleration, free fall, relative motion, and piecewise motion. The constant-acceleration validity warning and signed nth-interval displacement clarification are good. No major theory error was found in the inspected core. |
| 4 | 2-D motion | Good coverage of projectiles, relative velocity, circular motion, and curvature, with derivations and assumptions. **Corrected:** the river-crossing vector components mixed “across” and “along-bank” axes and used an ambiguous angle; the passage now fixes axes, defines the upstream angle from straight across, and gives consistent ground velocity and feasibility condition. Wind-heading notation should continue to be treated with a declared signed crosswind convention in worked applications. |
| 5 | Newton’s laws | Strong foundation: inertial frames, momentum form of the second law, third-law pairs, FBDs, standard forces, friction, constraints, pseudo-forces, and circular dynamics. The conceptual FBD guidance is particularly clear. Remember that ideal-string equal tension and Coulomb friction are model assumptions, not universal laws; the note generally flags idealisation. |
| 6 | Work, energy, and power | Strong conceptual path from work integral and work–energy theorem to conservative forces, potential, energy balance, power, and force from potential. It correctly distinguishes a moving contact surface (which can do work) from a fixed smooth surface. The energy balance is stated with non-conservative work. No major issue in the inspected core theory. |
| 7 | Centre of mass, momentum, collisions | Substantive and well ordered: COM motion, impulse/momentum, collision mechanics, CM frame, variable mass, and system applications. **Corrected:** clarified that the ideal rocket equation assumes negligible external impulse, constant exhaust speed relative to the rocket, and collinear motion; clarified kinetic-energy loss notation as initial minus final; corrected the sliding-chain integration factor in the extension. The restitution summary mainly describes passive impacts; a note now flags superelastic $e>1$ collisions. |
| 8 | Rotational mechanics | Broad coverage: rigid-body kinematics, inertia/axis theorems, torque, angular momentum, rolling, impulses, equilibrium, and precession. **Corrected:** general spin angular momentum is expressed with the inertia tensor; fixed-axis torque and angular momentum conservation are restricted to their proper axes/origins; the rolling-race ordering and steady-top assumptions are corrected/qualified. The scalar $\tau=I\alpha$ shortcut must not be generalized to arbitrary 3-D motion about the COM; the note now distinguishes it from $\boldsymbol\tau=d\mathbf L/dt$. |
| 9 | Gravitation | Broad coverage of fields/potential, shells/spheres, $g$ variation, Kepler/orbits, transfers, tides, and extensions. **Corrected:** the shell theorem proof now uses a valid ring integral rather than an invalid cancellation sketch; the spherical-cavity result states the uniform field; the collapse and Hohmann treatments were corrected; simple tidal balance is distinguished from the fluid Roche model; L1 coordinate and geostationary sidereal period were clarified. The latitude formula is now explicitly an approximation on a spherical, non-deforming Earth, and Kepler’s central-mass approximation is stated. |

## Changes made in this pass

- Fixed the chapter 4 river-crossing coordinate and angle convention.
- Added assumptions to chapter 7’s ideal rocket-equation derivation and noted superelastic impacts.
- Tightened chapter 8’s general angular-momentum, torque/conservation, and steady-precession validity statements; retained the corrected rolling order.
- Clarified chapter 9’s cavity field, latitude approximation, and two-body/central-mass assumption, alongside the corrections already made to its shell theorem, collapse, Hohmann transfer, Roche-limit distinction, L1 coordinate, and sidereal period.
- Earlier chapter 7–9 audit corrections and earlier unrelated chapter edits remain in place; unrelated worktree modifications were preserved.

## Remaining limits / next theory-only pass

1. This was a targeted audit of the theory spine, not proof that every sentence and every displayed equation in nine long chapters is flawless. Any claim of total correctness requires a full line-by-line review and independent checks of derivations.
2. Verify that JEE-specific core material is clearly separated from Olympiad/advanced extensions; especially scrutinize advanced claims that are presented as universal rather than model-dependent.
3. Review diagrams only insofar as they teach the theory; this pass did not check whether requested visual briefs have become rendered, accurate figures.
4. Experimental Skills coverage is not certified here. If the question is “complete for the entire JEE Physics syllabus,” the practical/experimental syllabus needs a separate audit.
