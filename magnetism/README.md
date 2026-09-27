# Magnetism — from the Lorentz force to the Earth's field

**Module folder for plan.md PARTs 16, 17, 18 and 19**, merged into one chapter at the owner's direction (2026-09-27), following the [electrostatics](../electrostatics/) precedent: the force on a moving charge and everything built on it → currents as sources (Biot–Savart, Ampère) → forces, torques and the magnetic dipole → magnetism in matter → the Earth's field. There is **no Cengage magnetism volume in this repository** (plan.md Block B): the coverage map of block 0 is built from the standard JEE Advanced headings itemised in plan.md PART 16–19 plus what the shipped [current-electricity](../current-electricity/) and [electromagnetic-waves](../electromagnetic-waves/) notes assume. Induction, inductance and AC (PART 20–22) are the next module — this chapter never lets the flux change.

| file | what it is |
|---|---|
| `Magnetism.md` | the chapter — the single deliverable, written for Obsidian reading mode |
| `notes.json` | gate configuration: the **stage** the chapter is at and the minimums that apply at each stage |
| `tools/check.py` | the local gate (the stage-aware electrostatics gate, unchanged apart from the docstring); `python3 tools/check.py` from this folder |

## Status: stage 1 of 3 — the theory is complete, the exam craft and the Olympiad layer are not

| stage | blocks | what it delivers | state |
|---|---|---|---|
| 1 | Parts 0–3 | orientation with the four-part coverage map, intuition, definitions and right-hand rules fixed once, and **the complete theory in teaching order** (§3.1–§3.38): every result of the four plan parts derived, the electric twins cited at each correspondence | **done** — 22 500 words, 7 rendered FIGUREs, 29 DIAGRAM briefs, 75 callouts |
| 2 | Parts 4–9 | validity ledger, C1–C14, E1–E20, the archetype table (≥ 40 rows) with Q1–Q60, toolkit, traps, playbook | next turn |
| 3 | Parts 10–14 | Olympiad extension with OL1–OL12 (magnetism from relativity, the cycloid twice, the pinch, Helmholtz, the magnetised sphere, Fermi acceleration, the Curie estimate), the 36-question / 200-mark paper, marking scheme, formula sheet, checkpoint | the turn after |

Blocks not yet written carry a `> [!warning] Stage n deliverable` notice stating their contents. The gate enforces every reading-mode, media and maths rule from stage 1; the question families and the paper become hard requirements when their stage arrives (`notes.json` → `stages`). `topics.json` lists the chapter as `in-progress` until stage 3 is green.

## Teaching order (block 3), and why

| § | topic | the reason it sits here |
|---|---|---|
| 3.1–3.2 | the observation; the Lorentz force and its three properties | effect before cause: what the field *does* is a one-line law; where it comes from is an integral |
| 3.3–3.4 | circles and helices; combined fields and the selector | the speed-independent period is the chapter's one big fact; the selector is its first use |
| 3.5–3.12 | the three-region method, the mass spectrometer, the cyclotron, mirrors and the adiabatic invariant, the Hall effect, drifts and the cycloid, Thomson's $e/m$, reading a track | everything a charge does in a known field, before any field is computed — plan PART 18 needs only the force law |
| 3.13–3.17 | Biot–Savart; the wire by angles; loop and arc; solenoid and toroid by stacking; the magnetic moment and the dipole analogy | the source law and its integrals, each with the electrostatic twin named |
| 3.18–3.22 | why a loop law exists; Ampère's law with its sign convention; eight applications; the overlap trick; the decision table; no monopoles | the symmetric shortcut, motivated from the wire's field before it is stated |
| 3.23–3.28 | $I\mathbf L\times\mathbf B$ from carriers; the chord theorem; torque, energy, galvanometer, the oscillating magnet; parallel wires and the third law; magnetic pressure and boundary conditions; the motor puzzle; the gyromagnetic ratio | forces need both the field and the source law; the motor puzzle is the bridge to induction |
| 3.29–3.36 | the magnet as a solenoid of bound currents; $\mathbf B$, $\mathbf H$, $\mathbf M$; dia-, para-, ferromagnetism derived mechanically; hysteresis as energy; cores, shields, electromagnets; forces on materials | matter last, because it needs the dipole, Ampère and the energy density |
| 3.37–3.38 | the Earth's elements and their measurement; the dipole moment, the dynamo, reversals, nature | the planet as the last worked example |

## Media

Text-only Markdown, Obsidian-first. Seven `[!tip] FIGURE` callouts render from Mermaid (module map, the loop's axial field, the finite solenoid's profile, the thick wire's $B(r)$, the source-law decision tree, the two-level paramagnet's alignment curve, a hysteresis loop drawn as two branches); 29 `[!abstract] DIAGRAM` briefs give the pictures that carry an argument and the search terms that find a textbook version. No raster art, no AI images, no external links.

## Hand-off

* **Assumes** cross products (PART 2), circular kinematics (PART 4), torque and moments of inertia (PART 8), small oscillations (PART 10), the Boltzmann factor (thermodynamics), and the electrostatics module (Coulomb's law, the ring and rod integrals, the dipole family, the energy density, Gauss's-law reasoning).
* **Gives the next module** the flux through a loop and why it is well defined (§3.22), the motional EMF hiding in the motor puzzle (§3.27), the force on a current (§3.23), the solenoid's field and its energy density (§3.19, §3.26), eddy currents and laminations as a named problem (§3.35); and gives atomic and nuclear physics the cyclotron frequency and the Bohr magneton.
* **Deliberately not covered:** anything with a changing flux (Faraday, Lenz, inductance, AC — PART 20–22); the energy density $B^2/2\mu_0$ is announced and checked, not derived (PART 21); displacement current and radiation (electromagnetic waves); the quantum origin of spin and exchange (named, not derived).

## Beyond the plan

Added at the theory level (mirrored in `topics.json` as `beyond_plan`):

* the adiabatic invariant $\mu=mv_\perp^2/2B$ derived from $\nabla\cdot\mathbf B=0$ and energy conservation, with the loss cone (§3.8);
* the gradient drift derived from the averaged force, with the ring current as its consequence (§3.10);
* the $n$-gon field with its circular limit as a check on the wire and loop formulas (§3.14);
* the moving charge's field written as $\mathbf v\times\mathbf E/c^2$ with $\mu_0\varepsilon_0=1/c^2$, previewing the relativistic origin (§3.13, §2.5);
* the wire-with-a-hole uniform field as an application of the overlap trick, with numbers (§3.20);
* the current-sheet force $(B_1^2-B_2^2)/2\mu_0$ derived with the factor-of-two logic of the electrostatic conductor (§3.26);
* the motor puzzle resolved with the back-EMF accounting, one page (§3.27);
* the rotating disc's field and moment checked against the gyromagnetic ratio (§3.28);
* the Larmor-frequency derivation of the diamagnetic susceptibility with its magnitude checked against real materials (§3.32);
* the hysteresis loss derived as $\oint H\,dB$ from the source's work, with transformer numbers (§3.34);
* the gapped magnetic circuit $B\approx\mu_0NI/(g+\ell/\mu_r)$ (§3.35) and the lift cap set by iron's saturation (§3.36);
* the Earth's dipole moment reconstructed from the equatorial field, and the thermal-energy argument for biological compasses (§3.38).

## Local gate

```bash
cd magnetism && python3 tools/check.py           # stage-aware local gate
cd .. && python3 tools/check_all.py --update     # repo gate + registry recount
```
