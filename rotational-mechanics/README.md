# Rotational Mechanics — first principles to Olympiad

> [!note] Part 8 of [plan.md](../plan.md) · Markdown chapter with editable Excalidraw scenes · written for Obsidian reading mode

**Scope.** Rigid-body kinematics ($\mathbf{v}=\boldsymbol{\omega}\times\mathbf{r}$, instantaneous axis); moment of inertia (derived for standard bodies); parallel-axis and perpendicular-axis theorems (proved); torque and $\tau=I\alpha$ (derived); angular momentum ($\mathbf{L}=I\boldsymbol{\omega}$ for fixed axis, general decomposition); conservation of angular momentum; rolling without slipping ($a=g\sin\theta/(1+I/MR^2)$, the rolling race); rolling with slipping (two-phase); rotational collisions and impulses; rigid-body equilibrium and toppling; gyroscopic precession.

**Prerequisites.** PART 7 (centre of mass, momentum conservation).

**The one idea.** A rigid body is a mass distribution; rotation is the same $F=ma$ story with $I$, $\tau$ and $L$ playing the roles of $m$, $F$ and $p$.

**Contents.** Part 0 orientation; 1 intuition; 2 definitions; 3 core derivations (§3.1–3.14); 4 results ledger; 5 exemplars E1–E10; 6 archetypes and Q1–Q25; 7 toolkit; 8 traps; 9 playbook; 10 Olympiad block OL1–OL10; 11 paper; 12 marking; 13 formula sheet; 14 checkpoint.

**Coverage (Cengage floor).** *Cengage Mechanics II*, ch 2 Rigid Body Dynamics (moment of inertia, axis theorems, torque, angular momentum, conservation of angular momentum, rolling, gyroscopic precession).

**Olympiad layer.** General angular momentum of a rolling body ($\mathbf{L}=I_{\text{cm}}\boldsymbol{\omega}+\mathbf{r}_{\text{cm}}\times M\mathbf{v}_{\text{cm}}$); rolling with slipping (complete two-phase solution); cylinder rolling inside a concave track (SHM link); the yo-yo; spool pulled at an angle; rod sliding down a frictionless wall; the unrolling carpet/inertia problem; the sleeping top condition; the physical pendulum as a rigid body; moment-of-inertia tensor concept.

**Hand-off.** The rotational tools are prerequisites for PART 9 (orbital angular momentum), PART 10 (physical pendulum), and PART 11 (fluid rotation).

## Print-ready short notes

[**Rigid body dynamics — 19 JEE sheets + 4 specialised extension sheets**](../Short%20notes/Rigid_Body_Dynamics/README.md)

- [Offline gallery and individual PNG downloads](../Short%20notes/Rigid_Body_Dynamics/index.html)
- [All PNGs — JEE first](../Short%20notes/Rigid_Body_Dynamics/rigid-body-dynamics-all-pngs.zip)
- [JEE PNGs](../Short%20notes/Rigid_Body_Dynamics/rigid-body-dynamics-jee-pngs.zip) · [Extension PNGs](../Short%20notes/Rigid_Body_Dynamics/rigid-body-dynamics-olympiad-pngs.zip)
- [Combined A4 PDF](../Short%20notes/Rigid_Body_Dynamics/rigid-body-dynamics-short-notes.pdf) · [JEE PDF](../Short%20notes/Rigid_Body_Dynamics/rigid-body-dynamics-jee.pdf) · [Extension PDF](../Short%20notes/Rigid_Body_Dynamics/rigid-body-dynamics-olympiad.pdf)
- [Source corrections and unresolved models](../Short%20notes/Rigid_Body_Dynamics/SOURCE-AUDIT.md) · [Coverage/classification](../Short%20notes/Rigid_Body_Dynamics/SCOPE.md)

These short notes use a relevance-based split, not an easy/hard split. They correct several source results without editing the detailed chapter; consult the audit before relying on the original examples. Print A4 portrait, one sheet per page, **Fit to page—not Fill/Crop**.

**Gate.** `python3 tools/check.py` → ALL GOOD.
