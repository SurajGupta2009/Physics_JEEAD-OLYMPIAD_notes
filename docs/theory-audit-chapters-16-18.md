# Theory-only audit: chapters 16–18

**Date:** 2026-09-29  
**Scope:** theory/derivation spine only; excludes question banks, worked-solution keys, diagrams, and experimental-practical coverage.

## Bottom line and order

The next three chapters are **Heat (16), Electrostatics (17), and Capacitors (18)**. The order is sensible: thermal state/energy and transport; then charge, fields, potential and electrostatic energy; finally capacitance as a geometry-specific application of fields, followed by energy and circuit behaviour. Across the material sampled, explanations are unusually explicit about models, limits, and checks.

No theory correction was made in these three chapters during this review. The initially suspected bimetal-strip discrepancy is not an inconsistency: the figure uses the thickness $t$ of **one** layer, while the equation and worked example use the total thickness $h=2t$. Thus $R=2t/(3\Delta\alpha\Delta T)=2h/(3\Delta\alpha\Delta T)$ would be incorrect; the actual equation is $1/R=3\Delta\alpha\Delta T/(2h)$, which agrees with the figure after substituting $h=2t$.

## Findings by chapter

### Chapter 16 — Heat

The progression from thermal quantities and expansion to calorimetry/phase change, conduction, convection, radiation, and transient/advanced heat transfer is coherent. The notes repeatedly distinguish temperature, internal energy, and heat transfer, and place useful assumptions near the governing models. Sampled derivations and checks—including temperature-dependent conductivity, Stefan ice growth, thermal penetration depth, and the equal-layer bimetal result—were consistent.

- **Bimetal convention verified:** for equal layer thickness $t$ and equal moduli in the stated textbook model, total thickness is $h=2t$ and the curvature expression is consistent. The worked numbers follow the total-thickness convention. Keeping the one-layer/total-thickness distinction prominent is important; no change was needed.
- **Scope/validity:** the chapter contains broad advanced material (including transient diffusion, boiling/phase boundaries, and radiation). This review sampled the theory spine and selected calculations rather than reconstructing every advanced derivation. Apply the stated constant-property, geometry, boundary-condition, and linearisation assumptions when using those results.

### Chapter 17 — Electrostatics

The sequence from Coulomb force and field superposition through continuous distributions, conductors/dipoles, flux and Gauss’s law, potential, energy, and induced charge is pedagogically sound. A separate results/limits ledger supports transfer between geometries. In sampled sections, the distinctions among a test charge’s $qV$, system self-energy’s half factor, conductor boundary fields, and exact versus far-field dipole results are appropriately emphasized. No specific theory error was confirmed in the sampled material.

- The Gaussian-surface material correctly treats symmetry as the condition that makes Gauss’s law directly useful for finding a field; the law itself is not restricted to symmetric charge distributions.
- **Scope/validity:** no full line-by-line proof of every distribution integral, advanced application, or image-method construction was performed. The broad syllabus map is not by itself evidence that every exam-syllabus item has been independently verified.

### Chapter 18 — Capacitors

The chapter builds from charge/conductors and electrostatic tools to capacitance for standard geometries and dielectrics, then to field energy, force, fixed-$Q$ versus fixed-$V$ constraints, and RC/transient behaviour. This is an effective order: it grounds capacitance in potential difference and geometry before introducing energy methods and circuit applications. The sampled formulas and the distinctions between series/parallel geometry, dielectric layering, and electrical constraints appeared internally consistent.

- The fixed-charge/fixed-voltage distinction is essential and is called out in the notes; force and energy statements must be read with the specified constraint and, for voltage-driven systems, the source’s work included.
- Ideal parallel-plate formulas require edge/fringing effects to be negligible; ideal lumped-capacitor/RC descriptions also require the circuit assumptions stated in their sections. These qualifications should remain adjacent to applications.
- **Scope/validity:** the lengthy later derivations and advanced dielectric/transient cases were sampled, not independently re-derived in full. No confirmed theory correction arose from the sample.

## Remaining limits

1. This is a targeted theory review, not a complete proofread or certification that every equation in these long chapters is error-free.
2. Exam-syllabus completeness and experimental/practical-skills coverage were not assessed here; the existing syllabus review separately flags the need for an item-by-item, source-linked audit.
3. Chapter checker scripts validate document structure/renderability, not physics correctness. The three chapter-specific checks passed; that should not be read as a substitute for expert review.
