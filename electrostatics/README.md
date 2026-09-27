# Electrostatics — first principles to Olympiad

**Module folder for plan.md PARTs 13, 14 and 15**, merged into one chapter at the owner's direction (2026-09-27): charge and Coulomb's law → the electric field and the element-and-symmetry method → conductors and dipoles → charges in fields → flux and Gauss's law → the potential, energy and conductors again from the scalar side → the Olympiad layer and a 200-mark paper. Cengage floor: *Electrostatics and Current Electricity* chapters 1–3 (the PDF is in the repository root; the contents pages were read from it and every section heading appears in the coverage map of block 0). The shipped [capacitors](../capacitors/) and [current-electricity](../current-electricity/) notes are the two chapters that follow it in the course order (slots 18 and 19).

| file | what it is |
|---|---|
| `Electrostatics.md` | the chapter — the single deliverable, written for Obsidian reading mode |
| `notes.json` | gate configuration: the stage the chapter is at (now 3 of 3) and the minimums that apply |
| `tools/check.py` | the local gate (plan.md Appendix C, made stage-aware); `python3 tools/check.py` from this folder |

## Status: complete (stage 3 of 3)

Written in three stages so that each turn shipped something whole; all three are on the page and the gate enforces the full plan.md §1 contract:

| stage | blocks | what it delivers | size |
|---|---|---|---|
| 1 | Parts 0–3 | orientation, intuition, definitions, and **the complete theory in teaching order** (§3.1–§3.37): every result of the three Cengage chapters derived, most of them twice by different tools | 21 500 words |
| 2 | Parts 4–9 | the validity ledger (36 rows), C1–C14 concept checks, exemplars E1–E20 with checks, the archetype table (34 rows) and practice Q1–Q56 (each archetype worked once and varied once), toolkit T1–T10, 18 traps, playbook with triage tree | + 9 000 words |
| 3 | Parts 10–14 | Olympiad extension (Earnshaw by the Laplacian, the image charge with uniqueness, electrostatic pressure two ways and the charged bubble, the Coulomb-exponent test, the ring off-axis and the charged cube, estimates, two measurements reconstructed, limits) with OL1–OL12 solved twice where a second method exists; the 36-question / 200-mark paper with a solution under every question; marking scheme and diagnostic table; two-page formula sheet; 25-point checkpoint and hand-off | + 11 000 words |

Totals: 41 000 words · 10 rendered FIGUREs (Mermaid) · 26 DIAGRAM briefs · 107 callouts · C×14 E×20 Q×56 OL×12 · paper 36 Q / 200 marks (A 12×4, B 8×4, C 6×5, D 10×9).

## Teaching order (block 3), and why

| § | topic | the reason it sits here |
|---|---|---|
| 3.1–3.2 | charge; Coulomb's law in vector form; superposition | the force law is the only physics; everything after is bookkeeping |
| 3.3 | the field and its lines | the test charge must drop out before distributions can be summed |
| 3.4 | the element-and-symmetry method, on the ring | one named procedure, then reused seven times |
| 3.5–3.7 | rod, disc and sheet, arc, shell by integration | the sheet and the shell are done the hard way so that Gauss is later a *shortcut* |
| 3.8 | conductors in the field picture, the factor of two | needs only $\mathbf E=0$ inside and the sheet result |
| 3.9–3.10 | the dipole; the dipole in a field | the far field of every neutral body; torque, energy, gradient force |
| 3.11–3.13 | equilibrium and stability; density bookkeeping; charges moving in fields | closes the "field" half with the exam family |
| 3.14–3.17 | flux; the solid-angle proof; Gauss's law; the protocol | the proof precedes the law, as the plan requires |
| 3.18–3.20 | spherical, cylindrical, planar symmetry | every shipped result re-derived in a line; slab and cavity added |
| 3.21–3.24 | cavities and shielding; flux without the field; matter (pointer); gravity | the law's consequences beyond field-finding |
| 3.25–3.26 | the conservative-field proof; the potential and its reference | the potential is *earned*, not postulated |
| 3.27–3.31 | potentials of distributions; $\mathbf E=-\nabla V$; differentiate instead of integrate; zeros; the dipole's potential | the scalar route, closing the loop on §3.4, §3.6 and §3.9 |
| 3.32–3.37 | energy of a system (the half); conductors; induced charges and sharing; the real world; field energy; nuclear and atomic | energy last, because it needs everything before it |

Blocks 4–9 follow the same order (ledger → exemplars → archetypes → methods → traps → playbook), and block 10 is written last, as the plan's Olympiad-at-the-end rule requires.

## Media

Text-only Markdown, Obsidian-first. Ten `[!tip] FIGURE` callouts render deterministically from Mermaid (module map, the element-and-symmetry flow, the ring's axial field, the Gaussian-surface protocol, the solid sphere's $E(r)$, the slab's $E(x)$, the shell's $V(r)$ and $E(r)$, the correspondence chain of the standard fields, the triage tree, the ring's potential along its axis and across its plane — the last computed from the complete elliptic integral by the arithmetic–geometric mean); 26 `[!abstract] DIAGRAM` briefs mark the pictures that carry part of an argument and give the search terms that find a textbook version. No raster art, no AI images, no external links.

## Hand-off

* **Assumes** vector algebra and unit vectors (PART 2), projectile kinematics (PART 4), the work–energy theorem and the notion of a conservative force (PART 6), torque and small oscillations (PARTs 8, 10), the shell theorem (PART 9), Stokes drag and surface tension (PART 11).
* **Gives the next chapters** the field between charged conductors and $u=\tfrac12\varepsilon_0E^2$ (capacitors), the conservative-field argument and the meaning of potential difference (current electricity), the charge-in-a-field kinematics and the dipole family (the magnetism module), the superposition tricks for uniform fields (Ampère's law), and the field-energy picture (electromagnetic waves).
* **Deliberately not covered:** capacitance and dielectrics beyond the pointer in §3.23 (owned by `capacitors/`); steady currents (`current-electricity/`); the general boundary-value problem (only the image charge for a plane, with its uniqueness argument, in Part 10); the field of moving charges and radiation (later modules; named in §10.8); quantum effects beyond the warning attached to the classical electron radius.

## Beyond the plan

Added because the book sweep or the merge justified it (mirrored in `topics.json` as `beyond_plan`):

* the four-face rule for two parallel conducting plates, derived from "zero field inside the metal" (§3.8, T5);
* the $\rho\propto r^n\Rightarrow E\propto r^{n+1}$ table and the constant-field $\rho\propto1/r$ case (§3.18);
* the off-centre cavity's uniform field derived where the interior field is first written in vector form (§3.18), with the full field map and the two-cylinder twin in OL6;
* the arc-equals-its-chord mnemonic (§3.7);
* the face-centre flux of a cube by the rectangle solid-angle formula, closing the flux-without-the-field family (§3.22, T6);
* the "which fields are conservative" drill with a circulating counter-example that previews induction (§3.25);
* the energy audit of two connected spheres as the electrostatic inelastic collision, including the superconducting-wire case (§3.34, P31);
* the field-energy integral checked on the solid sphere against layer assembly (§3.36, OL5);
* the uranium and gold Coulomb self-energies against total binding energies, tying $\tfrac35kQ^2/R$ to the semi-empirical mass formula (§3.37, OL12);
* the first-order interior field of a shell for a $1/r^{2+\epsilon}$ law, $E=-(\epsilon/3)kQr/R^3$, and the design of a null test (§10.4, OL8);
* the charged-drop coalescence threshold at $\approx0.42$ of the Rayleigh charge (OL9);
* the sealed charged bubble as a lesson in stiffness (OL4);
* the mean-value argument for the potential of a neutral sphere near a point charge (P10).

## Local gate

```bash
cd electrostatics && python3 tools/check.py      # stage-aware local gate (stage 3 = full contract)
cd .. && python3 tools/check_all.py --update     # repo gate + registry recount
```
