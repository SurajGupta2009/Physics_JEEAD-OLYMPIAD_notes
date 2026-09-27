# Electrostatics — first principles to Olympiad

**Module folder for plan.md PARTs 13, 14 and 15**, merged into one chapter at the owner's direction (2026-09-27): charge and Coulomb's law → the electric field and the element-and-symmetry method → conductors and dipoles → charges in fields → flux and Gauss's law → the potential, energy and conductors again from the scalar side. Cengage floor: *Electrostatics and Current Electricity* chapters 1–3 (the PDF is in the repository root; the contents pages were read from it and every section heading appears in the coverage map of block 0). The shipped [capacitors](../capacitors/) and [current-electricity](../current-electricity/) notes are the two chapters that follow it in the course order (slots 18 and 19).

| file | what it is |
|---|---|
| `Electrostatics.md` | the chapter — the single deliverable, written for Obsidian reading mode |
| `notes.json` | gate configuration: the **stage** the chapter is at and the minimums that apply at each stage |
| `tools/check.py` | the local gate (plan.md Appendix C, made stage-aware); `python3 tools/check.py` from this folder |

## Status: stage 1 of 3 — the theory is complete, the exam craft and the Olympiad layer are not

The module is written in three turns so that each turn ships something whole:

| stage | blocks | what it delivers | state |
|---|---|---|---|
| 1 | Parts 0–3 | orientation, intuition, definitions, and **the complete theory in teaching order** (§3.1–§3.37): every result of the three Cengage chapters derived, most of them twice by different tools | **done** — 21 500 words, 7 rendered FIGUREs, 23 DIAGRAM briefs, 81 callouts |
| 2 | Parts 4–9 | validity ledger, exemplars E1–E20, the archetype table (≥ 30 rows) with practice Q1–Q50, toolkit, traps, playbook | next turn |
| 3 | Parts 10–14 | Olympiad extension with OL1–OL12, the 36-question / 200-mark paper, marking scheme, formula sheet, checkpoint and hand-off | the turn after |

Blocks that are not yet written carry a `> [!warning] Stage n deliverable` notice stating their contents, so the reader is never surprised by an empty heading. The gate enforces every reading-mode, media and maths rule from stage 1; the question families and the paper become hard requirements when their stage arrives (`notes.json` → `stages`). `topics.json` lists the chapter as `in-progress` until stage 3 is green.

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

## Media

Text-only Markdown, Obsidian-first. Seven `[!tip] FIGURE` callouts render deterministically from Mermaid (module map, the element-and-symmetry flow, the ring's axial field, the Gaussian-surface protocol, the solid sphere's $E(r)$, the slab's $E(x)$, the shell's $V(r)$ and $E(r)$); 23 `[!abstract] DIAGRAM` briefs mark the pictures that carry part of an argument and give the search terms that find a textbook version. No raster art, no AI images, no external links. Stage 2 upgrades several briefs to figures (field-line patterns as a quadrant chart is the first candidate).

## Hand-off

* **Assumes** vector algebra and unit vectors (PART 2), projectile kinematics (PART 4), the work–energy theorem and the notion of a conservative force (PART 6), torque and small oscillations (PARTs 8, 10), the shell theorem (PART 9) and Stokes drag (PART 11).
* **Gives the next chapters** the field between charged conductors and $u=\tfrac12\varepsilon_0E^2$ (capacitors), the conservative-field argument and the meaning of potential difference (current electricity), the charge-in-a-field kinematics and the dipole family (the magnetism module), and the field-energy picture (electromagnetic waves).
* **Deliberately not covered:** capacitance and dielectrics beyond the pointer in §3.23 (owned by `capacitors/`); steady currents (`current-electricity/`); the general boundary-value problem (only the image charge for a plane, in stage 3); the field of moving charges and radiation (later modules); quantum effects beyond the warning attached to the classical electron radius.

## Beyond the plan

Added at the theory level because the book sweep or the merge justified it (mirrored in `topics.json` as `beyond_plan`):

* the four-face rule for two parallel conducting plates, derived from "zero field inside the metal" (§3.8), because it is the cleanest demonstration of the factor of two and a standard paper item;
* the $\rho\propto r^n\Rightarrow E\propto r^{n+1}$ table and the constant-field $\rho\propto1/r$ case (§3.18);
* the off-centre cavity's uniform field derived at the point where the interior field is first written in vector form (§3.18), instead of waiting for the Olympiad block;
* the arc-equals-its-chord mnemonic for the field at the centre of an arc (§3.7);
* the face-centre flux of a cube by the rectangle solid-angle formula, closing the "flux without the field" family where symmetry stops (§3.22);
* the "which fields are conservative" drill with a circulating counter-example that previews induction (§3.25);
* the energy audit of two connected spheres as the electrostatic inelastic collision, with the resistance-independence argument (§3.34);
* the field-energy integral checked on the solid sphere, interior and exterior, against the layer-assembly result (§3.36);
* the uranium Coulomb self-energy against the total binding energy, tying (3.47) to the semi-empirical mass formula (§3.37);
* the "same 1.44, three scales" numbers box (§3.37).

## Local gate

```bash
cd electrostatics && python3 tools/check.py      # stage-aware local gate
cd .. && python3 tools/check_all.py --update     # repo gate + registry recount
```
