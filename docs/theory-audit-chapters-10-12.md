# Theory-only audit: chapters 10–12

**Date:** 2026-09-28  
**Scope:** the theory and derivation sections of the next three mechanics chapters; not their exercise banks, solutions, figures, diagrams, or a complete syllabus audit.

## Verdict

The sequence is pedagogically coherent: **oscillations (SHM) → fluids → elasticity**. SHM develops the restoring-force model and its period/energy before adding pendulums, damping, driving, and coupled modes. Fluid mechanics proceeds from hydrostatics to flow and Bernoulli, then viscosity and surface effects. Elasticity starts with stress/strain and moduli, then builds to deformation of rods, thermal effects, torsion, energy, and bending. The flow-first then viscosity treatment is reasonable because Bernoulli's ideal-flow conditions are stated before viscous corrections are introduced.

These notes are substantial and explain many concepts rather than listing formulae, but the three chapters are **not certified as fully complete or universally error-free**. Chapters 10 and 12 contain significant enrichment beyond the JEE core; label that distinction carefully. This was a targeted theory audit, not a line-by-line check of every derivation or result.

## Findings and edits made

### Chapter 10 — Simple harmonic motion

- The core sequence is sound: differential equation → general solution and phase → velocity/acceleration → energy → springs and pendulums → superposition → damping/forcing → coupled modes.
- Corrected the equal-pendulum coupling result: for equal bobs with a connecting spring whose small-angle extension is $L(\theta_1-\theta_2)$, the out-of-phase frequency is $\sqrt{g/L+2k/m}$, not $\sqrt{g/L+k/m}$. The geometry assumption is now explicit.
- Distinguished the response at the driving frequency $\omega_0$ from the actual finite-damping amplitude peak, which lies below $\omega_0$ when a nonzero-frequency peak exists. Clarified the zero-damping ideal resonance statement.
- Remaining boundary: full damped/forced oscillator and coupled-mode theory are useful extensions; the note should not imply that every real oscillator has a single amplitude-independent period or that every damping level has a resonance peak at nonzero frequency.

### Chapter 11 — Fluid mechanics

- The sequence is broadly sound: pressure/hydrostatics → buoyancy → continuity/Bernoulli → jet momentum → viscosity → surface tension/capillarity.
- Replaced an internally contradictory scratch derivation of pressure isotropy with the standard infinitesimal-wedge scaling argument.
- Corrected the opening intuition: a fluid at rest cannot sustain shear, but a moving viscous fluid can sustain shear stress when velocity varies across layers.
- Corrected the Stokes-regime example. A 0.1 mm-radius drop gives $\mathrm{Re}\approx16$ when the Stokes terminal speed is substituted, so that Stokes result is self-inconsistent. The example now uses a 10 μm-radius water droplet, for which the estimated Reynolds number is about 0.016, and explicitly warns against using Stokes' law for the larger drop.
- Remaining boundary: Bernoulli, Poiseuille, Stokes drag, capillarity, and the surface-tension relations each have model/geometry conditions; the theory mostly gives these, but every later application should preserve them. Reynolds transition values are approximate and depend on flow geometry and disturbances.

### Chapter 12 — Elasticity and properties of matter

- The sequence from stress/strain and linear moduli through Poisson effects, rod deformation, thermal stress, torsion, strain energy, and bending is coherent and appropriately builds mathematical tools before applications.
- In the inspected theory spine, the modulus relations, linear-range conditions, self-weight extension, constrained thermal stress, torsion constant for a circular shaft, and standard bending relations are consistent with their stated assumptions.
- Chapter includes advanced topics (yield/fatigue, atomic-scale modulus estimate, material selection, buckling previews) beyond core JEE elasticity. Keep these marked as extensions and ensure simplified model assumptions remain visible; the atomic-bond estimate is an order-of-magnitude argument, not a universal material law.

## Validation

The three chapter structural checks passed. A repository-wide registry/check run is included in the task validation; those checks validate note structure and metadata, not the truth of every physics statement. See the main theory audit at `docs/theory-audit-chapters-1-9.md` for the preceding chapters and their limitations.
