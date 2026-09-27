# Pending chapters — JEE Advanced & Olympiad Physics notes

Regenerated 2026-09-27 from the repository state (`topics.json` + the topic folders), so it agrees
with `python3 tools/check_all.py` (29 registered topics, gate green). The Obsidian mirror of this
list is [`_obsidian/dashboards/pending.md`](_obsidian/dashboards/pending.md).

**Score: 18 of the 28 [plan.md](plan.md) parts are written, 3 are in progress as one module, 7
remain.** Mechanics (PART 1–12) and Modern Physics (PART 23–28) are closed. PART 13–15 are being
written as the single **`electrostatics/`** module (stage 1 of 3 done — see §1a). Everything left
after it is **magnetism → induction → AC, PART 16–22** — the only chapter-sized gaps in the syllabus
this repository set out to cover.

## 0 · Score board

| block | parts | written | remaining |
|---|---|---:|---:|
| A · Mechanics | 1–12 | 12 | — |
| B · Electricity & magnetism | 13–22 | 0 (+ 13–15 in progress as `electrostatics/`) | **7** |
| C · Modern physics | 23–28 | 6 | — |
| Original note-sets (plan.md Appendix A: waves, thermal, capacitors, current, optics) | — | 9 | — |
| Appendix chapter (`communication-systems`, JEE-Main depth) | — | 1 | — |

## 1a · In progress — the electrostatics module (PART 13 + 14 + 15)

At the owner's direction (2026-09-27) the three electrostatics parts are one chapter,
[`electrostatics/Electrostatics.md`](electrostatics/Electrostatics.md), slot **17** of the course
spine, written in three stages so that every turn ships something whole:

| stage | blocks | delivers | state |
|:-:|---|---|---|
| 1 | Parts 0–3 | orientation, intuition, definitions, and the **complete theory** of Cengage chs 1–3 in teaching order (§3.1–§3.37, every result derived, most twice) | **done** — 21 500 words, 7 FIGUREs, 23 DIAGRAM briefs |
| 2 | Parts 4–9 | validity ledger, E1–E20, archetype table (≥ 30 rows) + Q1–Q50, toolkit, traps, playbook | next |
| 3 | Parts 10–14 | Olympiad extension OL1–OL12, the 36-question / 200-mark paper, marking scheme, formula sheet, checkpoint | after that |

Its gate (`electrostatics/tools/check.py`) is stage-aware: reading-mode, media and maths rules from
stage 1, question families and the paper when their stage arrives (`electrostatics/notes.json`).
The plan.md sections for PART 13, 14 and 15 remain the content checklist; the chapter's block-0
coverage map accounts for every heading of the three Cengage chapters.

## 1 · The seven pending chapters, in teaching order

The order below is the dependency order and the course order: each chapter uses only what the
ones above it have derived. `order` is the slot the chapter takes in the course spine
([`_obsidian/dashboards/spine.md`](_obsidian/dashboards/spine.md)); write it into the chapter's
frontmatter together with `block: electricity-magnetism`. Size bands are plan.md §5.3 (compact
9–13k words · standard 12–16k · large 16–22k). The section-by-section teaching order, the
must-derive list, the figure briefs and the Olympiad block for every part are in plan.md §4.

| PART | slug | title | order | size | needs | Cengage floor | the one idea |
|---:|---|---|:-:|---|---|---|---|
| 16 | `magnetic-field` | Magnetic Field, Biot–Savart & the Lorentz Force | 20 | large | electrostatics (13–15) | no PDF — standard JEE Advanced headings | a magnetic field is what a moving charge calls the relativistic correction to the electric force; its effects are always perpendicular to motion |
| 17 | `amperes-law` | Ampère's Law, Currents & Magnetic Dipoles | 21 | standard | 16 | no PDF | Ampère's law is Gauss's law for currents — symmetry plus a loop integral gives the field |
| 18 | `moving-charges-magnetism` | Cyclotron, Velocity Selector & the Hall Effect | 22 | standard | 17 | no PDF | in a magnetic field a charge circles to a clock whose rate depends only on $q/m$ and $B$ — that single fact is an industry |
| 19 | `magnetism-and-matter` | Magnetism & Matter, Earth's Magnetism | 23 | compact | 17 | no PDF | matter responds through induced (dia), aligned (para) or permanently ordered (ferro) dipoles |
| 20 | `electromagnetic-induction` | Faraday, Lenz, Motional EMF & Eddy Currents | 24 | standard | 17 | no PDF | a changing flux drives an electric field, and Lenz's law is energy conservation in disguise |
| 21 | `inductance` | Self & Mutual Inductance, RL Circuits & Magnetic Energy | 25 | standard | 20 | no PDF | a coil resists changes in its own current because the energy lives in the field, not in the wire |
| 22 | `alternating-current` | Alternating Current, Resonance & Transformers | 26 | large | 21 | no PDF | in AC everything is a phase relationship; impedance is resistance that knows about time |

### Scope, chapter by chapter (the JEE floor each must cover; the Olympiad layer is plan.md §4)

- **13–15 · electrostatics** (in progress, §1a) — the scope of the three plan.md parts, now the block-3 teaching order of one chapter: charge → Coulomb → field and the element-and-symmetry method → conductors and dipoles → charges in fields → flux and Gauss → potential, energy, conductors and sharing.
- **16 · magnetic-field** — Biot–Savart; the field of a straight wire (finite and infinite), arc, loop (on axis), solenoid, toroid; the Lorentz force and its perpendicularity; force on a current element and on a wire; torque on a loop and the magnetic moment; the ampere; parallel currents.
- **17 · amperes-law** — Ampère's circuital law and the symmetry protocol; wire, thick wire, sheet, solenoid, toroid; forces between currents; the dipole interaction; magnetic pressure; no monopoles ($\nabla\cdot\mathbf B=0$); the displacement-current preview that `electromagnetic-waves/` completes.
- **18 · moving-charges-magnetism** — circular and helical motion, the cyclotron frequency; velocity selector; mass spectrometer; the cyclotron and its relativistic limit; $\mathbf E\times\mathbf B$ drift; magnetic mirror; Hall effect; the $e/m$ measurement.
- **19 · magnetism-and-matter** — magnetisation and bound currents; $\mathbf B$, $\mathbf H$, $\mathbf M$ and susceptibility; dia-, para- (Curie's law) and ferromagnetism; hysteresis and its energy loss; Earth's field: declination, dip, horizontal/vertical components; magnetic materials in devices.
- **20 · electromagnetic-induction** — flux, Faraday's law, Lenz's law as energy conservation; motional EMF and the rod-and-rails family (with the energy audit); induced electric fields and why they are non-conservative; the betatron condition; eddy currents and magnetic braking; generators and motors, back-EMF; the two-voltmeter paradox.
- **21 · inductance** — flux linkage and $L$; $L$ of solenoid, toroid, coaxial cable; mutual inductance and reciprocity; RL transients and $\tau=L/R$; the inductive kick; $U=\tfrac12LI^2$ and $u=B^2/2\mu_0$; the mechanical analogy; inductors in combination with the $\pm2M$ correction; coupled-coil energy and $F=\tfrac12I^2\,dM/dx$; LC oscillations; flux conservation in zero-resistance loops.
- **22 · alternating-current** — the generator's EMF and the waveform vocabulary; RMS by integration (and the half-cycle average trap); R, L, C alone with derived phase relations; phasors; series LCR, $Z$ and $\tan\phi$; resonance, $Q$ two ways, bandwidth; power and power factor; parallel circuits and admittance; the complex-impedance method; transformers and transmission losses; rectification and filters (link `semiconductors/`); LC oscillations as the bridge to `electromagnetic-waves/`.

### Batches (plan.md §0.4)

| batch | parts | rule |
|---|---|---|
| 1 | 13 + 14 + 15 | **merged** into `electrostatics/`, written in three stages (§1a); the only batch with a PDF to sweep |
| 2 | 16 → 17 | serial |
| 3 | 18 ∥ 19 | parallel — both need only 17 |
| 4 | 20 → 21 → 22 | **one continuous argument; never split across writers** |

## 2 · Syllabus audit — is anything else missing?

No. After PART 22 lands, every JEE Advanced topic and every Olympiad extension the plan names has a
chapter. The items below are *deliberately* not chapters (plan.md Appendix B), so nobody re-queues
them:

| topic | why it is not pending | where it lives |
|---|---|---|
| thermal expansion, calorimetry, kinetic theory, the two laws, entropy, heat transfer | already at Olympiad depth | `thermodynamics/`, `heat/` |
| waves on strings, sound, EM waves, ray and wave optics | already covered | the nine original note-sets |
| capacitance and lumped circuits | already covered | `capacitors/`, `current-electricity/` |
| communication systems | JEE-Main-only; written as an appendix chapter, not a PART | `communication-systems/` |
| a Cengage magnetism / EMI / AC volume | never supplied; PART 16–22 use the standard JEE syllabus as the floor | plan.md §1.13 |
| astrophysics, general relativity, formal QM, statistical mechanics, QFT | university courses; the plan stops at the boundary and names it | pointers inside PART 9, 23–26, 28 |
| numerical simulation, SPICE, engineering design | not examinable | — |

Anything a reader still misses after all 28 parts is a *new* part: add it as PART 29+ at the end
of plan.md with the same §1 contracts, and register it the same way.

## 3 · Done — the eighteen written parts

| PART | slug | order | location |
|---:|---|:-:|---|
| 1 | `units-measurements` | 1 | [Units-measurements.md](units-measurements/Units-measurements.md) |
| 2 | `vectors` | 2 | [Vectors.md](vectors/Vectors.md) |
| 3 | `kinematics-1d` | 3 | [Kinematics-1d.md](kinematics-1d/Kinematics-1d.md) |
| 4 | `motion-in-two-dimensions` | 4 | [Motion-in-two-dimensions.md](motion-in-two-dimensions/Motion-in-two-dimensions.md) |
| 5 | `newtons-laws` | 5 | [Newtons-laws.md](newtons-laws/Newtons-laws.md) |
| 6 | `work-energy-power` | 6 | [Work-energy-power.md](work-energy-power/Work-energy-power.md) |
| 7 | `centre-of-mass-momentum` | 7 | [Centre-of-mass-momentum.md](centre-of-mass-momentum/Centre-of-mass-momentum.md) |
| 8 | `rotational-mechanics` | 8 | [Rotational-mechanics.md](rotational-mechanics/Rotational-mechanics.md) |
| 9 | `gravitation` | 9 | [Gravitation.md](gravitation/Gravitation.md) |
| 10 | `simple-harmonic-motion` | 10 | [Simple-harmonic-motion.md](simple-harmonic-motion/Simple-harmonic-motion.md) |
| 11 | `fluid-mechanics` | 11 | [Fluid-mechanics.md](fluid-mechanics/Fluid-mechanics.md) — landed in band (large) |
| 12 | `elasticity` | 12 | [Elasticity.md](elasticity/Elasticity.md) — ~15 600 words, above the compact band; the overshoot is recorded, not hidden |
| 23 | `photoelectric-effect` | 30 | [Photoelectric-effect.md](photoelectric-effect/Photoelectric-effect.md) |
| 24 | `atomic-structure` | 31 | [Atomic-structure.md](atomic-structure/Atomic-structure.md) |
| 25 | `x-rays` | 32 | [X-rays.md](x-rays/X-rays.md) |
| 26 | `nuclear-physics` | 33 | [Nuclear-physics.md](nuclear-physics/Nuclear-physics.md) — absorbs the old P5 radioactivity row |
| 27 | `semiconductors` | 34 | [Semiconductors.md](semiconductors/Semiconductors.md) |
| 28 | `special-relativity` | 36 | [Special-relativity.md](special-relativity/Special-relativity.md) |

Plus `communication-systems` (order 35): JEE-Main depth, deliberately not a plan.md part.

## 4 · The nine original note-sets (plan.md Appendix A — do not rewrite, do not renumber)

| order | topic | location |
|:-:|---|---|
| 13 | String waves | [string-waves/String-waves.md](string-waves/String-waves.md) |
| 14 | Sound waves | [sound-waves/Sound-waves.md](sound-waves/Sound-waves.md) |
| 15 | Thermodynamics | [thermodynamics/Thermodynamics.md](thermodynamics/Thermodynamics.md) |
| 16 | Heat | [heat/Heat.md](heat/Heat.md) |
| 18 | Capacitors | [capacitors/Capacitors.md](capacitors/Capacitors.md) |
| 19 | Current electricity | [current-electricity/Current-electricity.md](current-electricity/Current-electricity.md) |
| 27 | Electromagnetic waves | [electromagnetic-waves/Electromagnetic-waves.md](electromagnetic-waves/Electromagnetic-waves.md) |
| 28 | Geometrical optics | [geometrical-optics/Geometrical-optics.md](geometrical-optics/Geometrical-optics.md) |
| 29 | Wave optics | [wave-optics/Wave-optics.md](wave-optics/Wave-optics.md) |

## 5 · Claiming and writing a pending chapter

1. **Claim.** In [`topics.json`](topics.json) append one object for the slug (template: plan.md
   Appendix C.7) with `"status": "in-progress"`, your `"owner"`, `"entry": "<slug>/<Title>.md"`,
   `"format": "markdown"`, `"plan_part": <N>`, `"order"` and `"block"` from the table in §1,
   `"source"`, `"exam"`, `"media"`, `"beyond_plan"`. Leave every mechanical count to `--update`.
   Add the README.md row and tick nothing here until the chapter is complete — the three edits land
   in the same commit as the first draft (plan.md §1.9).
2. **Scaffold** the four files of plan.md §1.1 — `<Title>.md`, `README.md`, `notes.json`,
   `tools/check.py` (copy `kinematics-1d/tools/check.py`, the pilot gate). In Obsidian:
   *Templater → Insert template → chapter* gives the 15-block skeleton with frontmatter.
3. **Teach it in order** (plan.md §2–§4 and CONTRIBUTING.md §3): intuition before definitions,
   every derivation with its "why", the validity condition beside every boxed result, worked
   exemplars and practice interleaved with the theory, traps named, then the Olympiad extension,
   the 36-question / 200-mark paper with marking scheme, the formula sheet, the checkpoint.
4. **Media** are Obsidian-native (docs/obsidian-plugin-workflow.md §2): ≥ 6 `> [!tip] FIGURE`
   callouts with Mermaid, `> [!abstract] DIAGRAM` briefs for drawn figures, no image files. The
   LaTeX Suite shorthands `;fig`, `;dia`, `;q`, `;sol`, `;trap` … emit the exact idioms.
5. **Sweep the book** (plan.md §1.12). PART 16–22 have no Cengage volume: build the coverage map
   from the headings listed in their plan.md sections plus the shipped `current-electricity/` and
   `electromagnetic-waves/` notes (the electrostatics module did its sweep from the PDF; its block-0
   map is the model).
6. **Gate.** `cd <slug> && python3 tools/check.py` → `ALL GOOD`; then
   `python3 tools/check_all.py --update` at the root. Flip `status` to `complete`, tick the row in
   §1 of this file and in `_obsidian/dashboards/pending.md`, append the topic to `TOPICS` /
   `SLUG_BY_NOTE` in `tools/md_site.py`, and regenerate `docs/site/`.

## 6 · Repository integration — current state

| integration point | state |
|---|---|
| `topics.json` registry | 29 topics (28 `complete`, `electrostatics` `in-progress`), each with `format` / `entry` / `owner` / `order` / `block` and mechanically recounted counts; gate green |
| `tools/check_all.py` | green; also checks that every master's frontmatter `order`/`block` equals the registry |
| Obsidian vault | `.obsidian/` committed (settings, CSS snippet, eight plugins configured and pinned in `plugins.lock.json`); plugin binaries are fetched by `python3 tools/obsidian_plugins.py` — see [`_obsidian/README.md`](_obsidian/README.md) |
| `tools/md_site.py` / `docs/site/` | all 29 topics render; regenerated 2026-09-27 |
| [README.md](README.md) | one row per note-set; keep the counts matching the registry after each recount |
| [CURRICULUM.md](CURRICULUM.md) | carries the full course order (all 36 slots) at the end |
