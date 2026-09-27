# Magnetism — from the Lorentz force to the Earth's field

**Module folder for plan.md PARTs 16, 17, 18 and 19**, merged into one chapter at the owner's direction (2026-09-27), following the [electrostatics](../electrostatics/) precedent: the force on a moving charge and everything built on it → currents as sources (Biot–Savart, Ampère) → forces, torques and the magnetic dipole → magnetism in matter → the Earth's field. There is **no Cengage magnetism volume in this repository** (plan.md Block B): the coverage map of block 0 is built from the standard JEE Advanced headings itemised in plan.md PART 16–19 plus what the shipped [current-electricity](../current-electricity/) and [electromagnetic-waves](../electromagnetic-waves/) notes assume. Induction, inductance and AC (PART 20–22) are the next module — this chapter never lets the flux change.

| file | what it is |
|---|---|
| `Magnetism.md` | the chapter — the single deliverable, written for Obsidian reading mode |
| `notes.json` | gate configuration: the stage the chapter is at (now 3 of 3) and the minimums that apply |
| `tools/check.py` | the local gate (the stage-aware electrostatics gate, unchanged apart from the docstring); `python3 tools/check.py` from this folder |

## Status: complete (stage 3 of 3)

Written in three stages so that each turn shipped something whole; all three are on the page and the gate enforces the full plan.md §1 contract:

| stage | blocks | what it delivers | size |
|---|---|---|---|
| 1 | Parts 0–3 | orientation with the four-part coverage map, intuition, definitions and right-hand rules fixed once, and **the complete theory in teaching order** (§3.1–§3.38): every result of the four plan parts derived, the electric twins cited at each correspondence | 22 500 words |
| 2 | Parts 4–9 | the validity ledger (44 rows), C1–C14 concept checks, exemplars E1–E20 with checks, the archetype table (41 rows) and practice Q1–Q60 (each archetype worked once and varied once), toolkit T1–T10, 19 traps, playbook with triage tree | + 8 000 words |
| 3 | Parts 10–14 | Olympiad extension (magnetism from electrostatics and relativity with the constant coming out right, the Helmholtz condition and its fourth-order flatness, the magnetised sphere two ways, the pinch and the levitated slab and the cosine-theta coil, five estimates, the Curie temperature and Gauss's absolute measurement reconstructed, limits) with OL1–OL12 solved twice where a second method exists; the 36-question / 200-mark paper with a solution under every question; marking scheme and diagnostic table; two-page formula sheet; 25-point checkpoint and hand-off | + 10 000 words |

Totals: 40 000 words · 10 rendered FIGUREs (Mermaid) · 30 DIAGRAM briefs · 99 callouts · C×14 E×20 Q×60 OL×12 · paper 36 Q / 200 marks (A 12×4, B 8×4, C 6×5, D 10×9).

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

Text-only Markdown, Obsidian-first. Ten `[!tip] FIGURE` callouts render from Mermaid (module map, the loop's axial field, the finite solenoid's profile, the thick wire's $B(r)$, the source-law decision tree, the two-level paramagnet's alignment curve, a hysteresis loop drawn as two branches, the correspondence chain, the triage tree, the Helmholtz pair at three spacings); 30 `[!abstract] DIAGRAM` briefs give the pictures that carry an argument and the search terms that find a textbook version. No raster art, no AI images, no external links.

## Hand-off

* **Assumes** cross products (PART 2), circular kinematics (PART 4), torque and moments of inertia (PART 8), small oscillations (PART 10), the Boltzmann factor (thermodynamics), and the electrostatics module (Coulomb's law, the ring and rod integrals, the dipole family, the energy density, Gauss's-law reasoning).
* **Gives the next module** the flux through a loop and why it is well defined (§3.22), the motional EMF hiding in the motor puzzle (§3.27), the force on a current (§3.23), the solenoid's field and its energy density (§3.19, §3.26), eddy currents and laminations as a named problem (§3.35); and gives atomic and nuclear physics the cyclotron frequency and the Bohr magneton.
* **Deliberately not covered:** anything with a changing flux (Faraday, Lenz, inductance, AC — PART 20–22); the energy density $B^2/2\mu_0$ is announced and checked, not derived (PART 21); displacement current and radiation (electromagnetic waves); the quantum origin of spin and exchange (named, not derived).

## Beyond the plan

Added because the merge or the derivations justified it (mirrored in `topics.json` as `beyond_plan`):

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
* the Earth's dipole moment reconstructed from the equatorial field, and the thermal-energy argument for biological compasses (§3.38);
* the cycloid family classified by the drifting-frame gyration speed (OL5) and the three radiation-belt clocks with numbers (OL6);
* the Hall coefficient with two carrier types and its temperature sign-flip (OL9, P33);
* the Meissner levitation height by the image method and by pressure (OL10);
* the dip–latitude relation $\tan\theta_{\text{dip}}=2\tan\lambda$ used as a consistency check on a station's field (OL12, P36);
* the free-decay time of the Earth's field as the argument for the dynamo (§10.5).

## Local gate

```bash
cd magnetism && python3 tools/check.py           # stage-aware local gate (stage 3 = full contract)
cd .. && python3 tools/check_all.py --update     # repo gate + registry recount
```
