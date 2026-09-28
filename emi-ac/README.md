# Electromagnetic induction, inductance and alternating current — one continuous argument

**Module folder for plan.md PARTs 20, 21 and 22**, merged into one chapter at the owner's direction (2026-09-27), following the [electrostatics](../electrostatics/) and [magnetism](../magnetism/) precedents — and this time also the plan's own instruction that PART 20 → 21 → 22 are "one continuous argument; never split across writers". Induction (a changing flux drives an electric field) → inductance (a coil's own changing flux) → alternating current (a sinusoidally changing flux). There is **no Cengage volume in this repository** for this material (plan.md Block B): the coverage map of block 0 is built from the standard JEE Advanced headings itemised in plan.md PART 20–22 plus what the shipped [current-electricity](../current-electricity/), [capacitors](../capacitors/) and [electromagnetic-waves](../electromagnetic-waves/) notes assume.

| file | what it is |
|---|---|
| `Emi-ac.md` | the chapter — the single deliverable, written for Obsidian reading mode |
| `notes.json` | gate configuration: the **stage** the chapter is at and the minimums that apply at each stage |
| `tools/check.py` | the local gate (the stage-aware electrostatics gate, unchanged apart from the docstring); `python3 tools/check.py` from this folder |

## Status: stage 1 of 3 — the theory is complete, the exam craft and the Olympiad layer are not

| stage | blocks | what it delivers | state |
|---|---|---|---|
| 1 | Parts 0–3 | orientation with the three-part coverage map, intuition, definitions with the sign conventions fixed once, and **the complete theory in teaching order** (§3.1–§3.36): every result of the three plan parts derived, the previous chapters cited at each borrowing | **done** — 19 000 words, 8 rendered FIGUREs, 22 DIAGRAM briefs, 62 callouts |
| 2 | Parts 4–9 | validity ledger, C1–C14, E1–E20, the archetype table (≥ 40 rows) with Q1–Q60, toolkit, traps, playbook | next turn |
| 3 | Parts 10–14 | Olympiad extension with OL1–OL12 (the flux-rule paradoxes, the betatron twice, the falling magnet, the tether, the coil launcher, superconducting flux conservation, the 50 Ω cable, the full transient-plus-steady-state solution, impedance matching, the Wien bridge, three-phase), the 36-question / 200-mark paper, marking scheme, formula sheet, checkpoint | the turn after |

Blocks not yet written carry a `> [!warning] Stage n deliverable` notice stating their contents. The gate enforces every reading-mode, media and maths rule from stage 1; the question families and the paper become hard requirements when their stage arrives (`notes.json` → `stages`). `topics.json` lists the chapter as `in-progress` until stage 3 is green.

## Teaching order (block 3), and why

| § | topic | the reason it sits here |
|---|---|---|
| 3.1–3.2 | flux with its sign; Faraday's law and the sign protocol | the law is one line; every error is a sign, so the protocol comes first |
| 3.3–3.4 | motional EMF from the Lorentz force, reconciled with the flux rule; Lenz's law as energy conservation | two independent derivations, and the physical reason for the minus sign |
| 3.5–3.6 | the rod family: rails, rotating rod, rotating coil, disc, loop leaving a field; then every attachment — mass, capacitor, friction, spring, inductor | one geometry, all the mechanics–circuit couplings; the inductor is the hand-off to the next third |
| 3.7–3.8 | induced electric fields; the betatron's 2:1 condition | Faraday's law without a wire, and its first machine |
| 3.9–3.12 | eddy currents (braking, falling magnet, heating, laminations); generators and motors; the voltmeter paradox; everyday induction | the consequences, each with its scaling law |
| 3.13–3.15 | flux linkage and $L$; four geometries; mutual inductance and coupling | Faraday's law applied to a coil's own flux |
| 3.16–3.18 | the RL transient; the inductive kick; $\tfrac12LI^2$ and $B^2/2\mu_0$ | the first-order circuit and where its energy lives |
| 3.19–3.24 | the mechanical analogy; combinations with $M$; coupled-coil energy and force; LC oscillations; flux conservation; practice | the second-order circuit and the tools that read it |
| 3.25–3.28 | AC and its source; RMS from heating; R, L, C with phases derived; phasors | a sinusoidal drive, one element at a time |
| 3.29–3.31 | series LCR; resonance, magnification, $Q$ two ways, bandwidth; power and the power factor | the elements together |
| 3.32–3.33 | parallel circuits and admittance; the complex method | the general tools, after the phasors that justify them |
| 3.34–3.36 | transformers, impedance reflection, transmission; rectifiers and ripple; the LC source and the road to radiation | the machines, and the hand-off to electromagnetic waves |

## Media

Text-only Markdown, Obsidian-first. Eight `[!tip] FIGURE` callouts render from Mermaid (module map, the sign protocol, the rod on rails coasting and driven, the induced field profile, the RL transient, the LC energy exchange, a sinusoid and its square, resonance curves for three $Q$); 22 `[!abstract] DIAGRAM` briefs give the pictures that carry an argument and the search terms that find a textbook version. No raster art, no AI images, no external links.

## Hand-off

* **Assumes** the magnetism module (Lorentz force, force on a current, the solenoid's field, torque on a coil, magnetic pressure announced), the electrostatics module (conservative fields, the conductor as an equipotential — the statement induction breaks), current electricity (Kirchhoff), capacitors ($\tfrac12CV^2$, $RC$), SHM (the oscillator and its damping) and vectors (phasors are vectors).
* **Gives the next chapters** the displacement-current question and the radiating LC circuit (electromagnetic waves), RL/LC/rectifier behaviour (semiconductor circuits), and induction as the working principle of the instruments in the modern-physics chapters.
* **Deliberately not covered:** displacement current and radiation (the shipped EM-waves note); the skin effect beyond an estimate; three-phase and power electronics beyond a paragraph (stage 3 adds three-phase); the quantum origin of superconductivity (flux conservation is used, not explained).

## Beyond the plan

Added at the theory level (mirrored in `topics.json` as `beyond_plan`):

* the falling-magnet terminal speed with the derived drag coefficient $\tfrac{45}{1024}\mu_0^2\mu^2\sigma t/a^4$ and real numbers for copper and aluminium (§3.4);
* the rod with a spring as a damped oscillator with a magnetic dashpot, and with an inductor as an LC circuit (§3.6);
* the impulse-per-unit-charge result for a bead on a ring around a changing flux (§3.7);
* the betatron worked with numbers (75 MeV, $4.8\times10^5$ turns, 157 V per turn) (§3.8);
* the braking time as $\rho_m/k\sigma B^2$ — material-dependent, size-independent (§3.9);
* the lamination loss derived as $\sigma\omega^2B_0^2d^2/24$ with silicon-steel numbers (§3.9);
* the coaxial cable's $L'C'=1/c^2$ and $\sqrt{L'/C'}=60\ln(b/a)\ \Omega$ (§3.14);
* reciprocity proved from the coupled-coil energy (§3.21);
* $Q$ shown three ways — magnification, bandwidth, energy ratio — and the ring-down as $Q$ cycles (§3.22, §3.30);
* a radio's tuned circuit with numbers (§3.30) and a four-element network solved by complex numbers and by phasors (§3.33);
* the power-factor correction sized for an industrial and a workshop load (§3.31);
* the transmission-loss arithmetic and the note on HVDC (§3.34).

## Local gate

```bash
cd emi-ac && python3 tools/check.py              # stage-aware local gate
cd .. && python3 tools/check_all.py --update     # repo gate + registry recount
```
