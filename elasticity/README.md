# Elasticity & Properties of Matter — first principles to Olympiad

> [!note] Part 12 of [plan.md](../plan.md) · text-only Markdown chapter · written for Obsidian reading mode

**Scope.** Stress and strain in the four classical modes; Hooke's law as the small-strain theorem and the stress–strain curve read as design information; Young's, bulk and shear moduli from their experiments; Poisson's ratio with the bounds $-1<\sigma<\tfrac12$ and both interrelations derived; the extension family (end load, the spring constant $k=YA/L$, series and parallel composites, self-weight by integration, a tapered rod); thermal stress by expanding free and restoring the constraint; torsion ($\theta=TL/GJ$) and the torsion pendulum; elastic energy, the sudden-load factor 2, and the falling weight by energy; bending from the neutral axis through $M=YI/R$ to an integrated cantilever; plasticity, fatigue and the atomic spring; material selection by specific strength and specific modulus.

**Prerequisites.** PART 5 (force balances) and PART 6 (work–energy). The spring and torsion-pendulum machinery is PART 10's once $k$ or $C$ is known. The fluid half of the same Cengage chapter is [PART 11](../fluid-mechanics/Fluid-mechanics.md).

**The one idea.** Elasticity is the macroscopic face of the interatomic spring: moduli are material properties, stiffness is geometry.

**Contents.** Part 0 orientation and coverage map; 1 intuition; 2 definitions; 3 core derivations §3.1–3.12; 4 results ledger; 5 exemplars E1–E10 with concept checks C1–C12; 6 archetypes (18 rows) and Q1–Q25; 7 toolkit T1–T8; 8 twelve traps; 9 playbook; 10 Olympiad block OL1–OL10 with the limits section; 11 paper P1–P36; 12 marking and diagnostics; 13 formula sheet; 14 checkpoint.

**Coverage (Cengage floor).** *Cengage Mechanics II*, ch 4 Properties of Solids and Fluids, elasticity half (pp. 4.1–4.19): elasticity and plasticity, stress and strain and their types, elastic limit, Hooke's law, the three moduli, the rod-as-spring analogy, composite bars, the stress–strain diagram, elastic aftereffect and fatigue, energy stored in a wire, and the interatomic force constant. Every contents-page heading of that half has a row in the block-0 map. Poisson's ratio, thermal stress, torsion and bending are syllabus requirements the volume does not give their own headings; they are derived here and marked as extended beyond the book.

**Olympiad layer.** $Y\sim D/r_0^3$ and the reason solids sit near $10^{11}$ Pa; thermal expansion as the asymmetry of the well, collapsing to $\alpha\sim k_B/(2D)$; the falling weight with the rod's own mass kept in the energy integral; the constant-stress rod $A=A_0 e^{x/\lambda}$ and why $\lambda$ is not the height of a tree; the cantilever integrated from the curvature equation; Euler buckling derived from the sine shape and compared with yield; the I-beam's real gain once depth is held fixed; the cubic correction to Hooke's law, and why yield arrives first; hoop stress by a free-body cut, and a spider-silk specific-strength estimate; thin-rod, P-wave and S-wave speeds as a two-modulus reading of an earthquake.

**Media.** All figures are described briefs (`> [!abstract] DIAGRAM D12.k`, D12.1–D12.14) with `*Search:*` lines; no image files by design.

**Gate.** `python3 tools/check.py` → ALL GOOD. The chapter is about 15 600 words. plan.md §5.3 calls this part compact (9 000–13 000); the required derivations and the 200-mark paper do not fit under that ceiling without cutting a proof the plan says must be derived, so the overshoot is recorded here and in `PENDING.md` rather than hidden. The gate minimum of 9 000 is met.

## Beyond the plan

Mirrored in `topics.json` `beyond_plan`. The PART 12 section of plan.md was the floor; the sweep added:

- the straight-wire sag $y=l(mg/YA)^{1/3}$, beside the angled hanger the plan names, because the plan's own trap ("why not $mg/2$") is sharpest there (E5);
- the bolt-and-nut quarter-turn as a numerical thermal-stress cousin (E4), which the plan lists and the book's elasticity half does not work;
- the fair I-beam comparison at equal depth and equal area, against the inflated factor you get by also changing the depth (OL7);
- the wave-transit caveat on the falling-weight integral, $L/c$ against the loading time (OL3);
- a material-selection table with three real candidates and two different indices, rather than a qualitative ranking (E10).

**Deliberately not covered.** Plastic buckling after yield (named as the failure of Euler's formula, not derived). Anisotropic laminate theory for the composite of E10. Fracture mechanics beyond the statement that fatigue grows a crack. Large-strain rubber elasticity as an entropy spring is named, in §3.11 and OL8, and then left alone: it is not Hooke's law with a small $Y$.

**Hand-off.** [Fluids](../fluid-mechanics/Fluid-mechanics.md) shares the shell-balance habit and owns the tree's hydraulic ceiling, which OL4's crushing length does not turn out to be. [Heat](../heat/Heat.md) owns $\alpha$ as a measured fact. [Sound waves](../sound-waves/Sound-waves.md) owns the wave equation; this chapter only chooses the modulus under the square root. [SHM](../simple-harmonic-motion/Simple-harmonic-motion.md) owns the oscillator once $k$ or $C$ is known.
