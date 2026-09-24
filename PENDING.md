# Pending chapters — JEE Advanced & Olympiad Physics notes

Regenerated: 2026-09-24, from the repository state rather than from prose.
The counts below were produced by walking `topics.json` and the topic folders,
so they agree with `python3 tools/check_all.py` (26 registered topics, gate
green).

**Score: 16 of the 28 [plan.md](plan.md) parts are written. 12 remain** —
`fluid-mechanics` and `elasticity` close out mechanics, and the whole of
electricity & magnetism (PART 13–22) is untouched. Those twelve are the only
chapter-sized gaps left in the syllabus this repository set out to cover.

Everything below is organised so a contributor can claim one topic, scaffold it,
and write it to the same standard: proof-first, Cengage floor plus an Olympiad
extension, the 15-block spine of [plan.md](plan.md) §1.4, `DIAGRAM` figure
briefs instead of images, interleaved solutions, a 36-question 200-mark paper,
and a formula sheet. The content bar is [CONTRIBUTING.md](CONTRIBUTING.md); the
layout contract is [STRUCTURE.md](STRUCTURE.md).

**Claim by part number.** [plan.md](plan.md) numbers every chapter PART 1 …
PART 28, so a chapter is claimed as *"execute PART 17"*. To claim one: set
`"owner"` and `"status": "in-progress"` for its slug in
[`topics.json`](topics.json), add its row to the table in
[README.md](README.md), and mark its line here — those three edits land in the
same commit as the first draft (plan.md §1.9).

---

## 0 · Score board

| block | parts | written | remaining |
|---|---|---:|---:|
| A · Mechanics | 1–12 | 1–10 | **11, 12** |
| B · Electricity & magnetism | 13–22 | — | **13–22** |
| C · Modern physics | 23–28 | 23–28 | — |
| Shipped note-sets (plan.md Appendix A) | — | 9 | — |

Reading order is the dependency order; earlier parts are prerequisites for later
ones. plan.md §0.4 lists which parts can be written in parallel.

### How the older row labels map to plan.md's PART numbers

The tables in §1–§3 below used to be ordered M/E/P. That ordering is retired;
plan.md is authoritative. The bridge, for anyone holding an old note:

| old label | plan.md part |
|---|---|
| M1 units · M3 vectors · M2 kinematics-1d · M4 projectiles · M5 Newton's laws · M6 work-energy · M7 centre of mass · M8 rotation · M9 gravitation · M10 SHM · M11 fluids · M12 elasticity | **PART 1–12** in that order (vectors precedes 1-D kinematics) |
| E1 Coulomb/field · E2 Gauss · E3 potential · E4 magnetic field · E5 Ampère · E6 moving charges · E7 magnetism & matter · E8 EMI · E9 inductance · E10 AC | **PART 13–22** |
| P1 photoelectric · P2 atom · P3 X-rays · P4 nucleus · P5 radioactivity | **PART 23–26** (P5 is folded into PART 26) |
| P6 semiconductors · P7 communication systems · P8 relativity | **PART 27** · dropped (JEE-Main only; plan.md Appendix B) · **PART 28** |
| M0 capacitors and the current-electricity rows | already shipped: [capacitors/](capacitors/), [current-electricity/](current-electricity/) — do not rewrite |

Note the slug corrections plan.md makes against the old table: PART 13 is
`electric-field` (not `coulomb-electric-field`), PART 19 is
`magnetism-and-matter`, PART 22 is `alternating-current`.

---

## 1. Remaining: mechanics (Cengage *Mechanics II*)

Both mechanics volumes are committed in this repository
(`Cengage  MECHANICS  1-compressed.pdf`, `Cengage MECHANICS 2-compressed.pdf` —
`git ls-files | grep pdf`), so the book sweep of plan.md §1.12 is verifiable for
both of these chapters. plan.md §1.13 maps each PDF to the chapters it really
contains.

| PART | slug | title | scope / Cengage floor | needs | status |
|---:|---|---|---|---|---|
| 11 | `fluid-mechanics` | Fluid Mechanics & Surface Tension | hydrostatics from $\frac{dp}{dy}=-\rho g$; Pascal; Archimedes derived twice; metacentre; buoyancy in non-inertial frames; continuity; Bernoulli and its four validity conditions; Torricelli, Venturi, pitot, siphon; momentum flux; viscosity; Poiseuille derived; Stokes and terminal velocity; Reynolds; surface tension (both definitions, excess pressure, capillarity) | 5, 6 | **pending** |
| 12 | `elasticity` | Elasticity & Properties of Matter | stress/strain; $Y$, $B$, $G$ from their experiments; the stress–strain curve's landmarks; Poisson's ratio and the two interrelations; extension under load, self-weight, composite rods; thermal stress; torsion; elastic energy density and the suddenly-applied load; bending and the neutral axis; the atomic-spring derivation of $Y$ | 5 | **pending** |

* Cengage floor for 11: *Mechanics II* ch 3 Fluid Mechanics, plus ch 4
  Properties of Solids and Fluids for surface tension.
* Cengage floor for 12: *Mechanics II* ch 4 Properties of Solids and Fluids (the
  elasticity half; the fluid half is PART 11's).
* plan.md §5.3 sizes 11 as **large** (16 000–22 000 words) and 12 as **compact**
  (9 000–13 000).

---

## 2. Remaining: electricity & magnetism (PART 13–22)

This is the largest single block left, and the second-heaviest on a JEE Advanced
paper. Capacitors and current electricity are already shipped, so the block sits
directly on top of existing notes — but note that only PART 13–15 have a PDF in
this repository to sweep. **There is no magnetism, EMI, inductance or AC volume
here** (plan.md §1.13): PART 16–22 build their coverage map from the standard
syllabus headings listed in their plan.md sections, plus the shipped
`current-electricity/` and `electromagnetic-waves/` notes.

| PART | slug | title | scope / floor | needs | status |
|---:|---|---|---|---|---|
| 13 | `electric-field` | Charge, Coulomb's Law & Electric Field | Coulomb and superposition; $E$ for rod, ring, disc, arc, shell; dipole in a field; lines of force | 2 | **pending** — PDF available (ch 1) |
| 14 | `gauss-law` | Electric Flux & Gauss's Law | flux; Gauss; shell, sheet, wire, solid sphere, conductor | 13 | **pending** — PDF available (ch 2) |
| 15 | `electric-potential` | Potential, Potential Energy & Conductors | $V=kq/r$; distributions; equipotentials; $\mathbf{E}=-\nabla V$; conductors in equilibrium; $W=q\Delta V$ | 14 | **pending** — PDF available (ch 3) |
| 16 | `magnetic-field` | Magnetic Field, Biot–Savart & the Lorentz Force | $B$ for wire, loop, arc, solenoid; the ampere; Lorentz force | 15 | **pending** — no PDF in repo |
| 17 | `amperes-law` | Ampère's Law, Currents & Magnetic Dipoles | Ampère for wire, solenoid, toroid; force on a current; force between parallel wires; torque on a loop | 16 | **pending** — no PDF in repo |
| 18 | `moving-charges-magnetism` | Cyclotron, Velocity Selector & the Hall Effect | cyclotron radius and helix; velocity selector; cyclotron; J.J. Thomson; Hall effect | 17 | **pending** — no PDF in repo |
| 19 | `magnetism-and-matter` | Magnetism & Matter, Earth's Magnetism | para/dia/ferro; $\mathbf{M}$ and $\mathbf{H}$; hysteresis; Earth's field; magnetic materials | 17 | **pending** — no PDF in repo |
| 20 | `electromagnetic-induction` | Faraday, Lenz, Motional EMF & Eddy Currents | flux; Faraday; Lenz; motional emf; induced $E$ field; eddy currents | 17 | **pending** — no PDF in repo |
| 21 | `inductance` | Self & Mutual Inductance, RL Circuits & Magnetic Energy | $L$, $M$; solenoid and toroid inductance; RL transients; $L/R$; energy in a $B$ field | 20 | **pending** — no PDF in repo |
| 22 | `alternating-current` | AC Circuits, Resonance & Transformers | phasors; series and parallel LCR; resonance; $Q$; power factor; transformer; LC oscillations | 21 | **pending** — no PDF in repo |

plan.md §0.4 puts 20, 21 and 22 in one batch on purpose: EMI → inductance → AC
is a single continuous argument and should not be split across agents.

---

## 3. Done: the sixteen written parts

| PART | slug | location |
|---:|---|---|
| 1 | `units-measurements` | [Units-measurements.md](units-measurements/Units-measurements.md) |
| 2 | `vectors` | [Vectors.md](vectors/Vectors.md) |
| 3 | `kinematics-1d` | [Kinematics-1d.md](kinematics-1d/Kinematics-1d.md) |
| 4 | `motion-in-two-dimensions` | [Motion-in-two-dimensions.md](motion-in-two-dimensions/Motion-in-two-dimensions.md) |
| 5 | `newtons-laws` | [Newtons-laws.md](newtons-laws/Newtons-laws.md) |
| 6 | `work-energy-power` | [Work-energy-power.md](work-energy-power/Work-energy-power.md) |
| 7 | `centre-of-mass-momentum` | [Centre-of-mass-momentum.md](centre-of-mass-momentum/Centre-of-mass-momentum.md) |
| 8 | `rotational-mechanics` | [Rotational-mechanics.md](rotational-mechanics/Rotational-mechanics.md) |
| 9 | `gravitation` | [Gravitation.md](gravitation/Gravitation.md) |
| 10 | `simple-harmonic-motion` | [Simple-harmonic-motion.md](simple-harmonic-motion/Simple-harmonic-motion.md) |
| 23 | `photoelectric-effect` | [Photoelectric-effect.md](photoelectric-effect/Photoelectric-effect.md) |
| 24 | `atomic-structure` | [Atomic-structure.md](atomic-structure/Atomic-structure.md) |
| 25 | `x-rays` | [X-rays.md](x-rays/X-rays.md) |
| 26 | `nuclear-physics` | [Nuclear-physics.md](nuclear-physics/Nuclear-physics.md) — absorbs the old P5 radioactivity row |
| 27 | `semiconductors` | [Semiconductors.md](semiconductors/Semiconductors.md) |
| 28 | `special-relativity` | [Special-relativity.md](special-relativity/Special-relativity.md) |

Plus `communication-systems` (the old P7 row): written at JEE-Main depth, and
**deliberately not a plan.md part** — plan.md Appendix B drops it as a chapter of
its own, and the note says so.

---

## 4. Thermodynamics and matter: no separate note-sets planned

The two matter-and-heat volumes share their chapter lists with notes that
already exist. Nothing is missing here:

- ✅ thermodynamics — kinetic theory, first and second law, entropy, engines: [thermodynamics/](thermodynamics/)
- ✅ heat transfer and calorimetry: [heat/](heat/)
- ✅ thermal expansion, calorimetry and kinetic theory are folded into the two
  above (see their Cengage coverage maps). No separate note-set is planned
  unless a hole turns up during review.

---

## 5. Shipped note-sets (the complement of everything above)

| # | topic | location |
|---:|---|---|
| 1 | String waves | [string-waves/String-waves.md](string-waves/String-waves.md) |
| 2 | Sound waves | [sound-waves/Sound-waves.md](sound-waves/Sound-waves.md) |
| 3 | Electromagnetic waves | [electromagnetic-waves/Electromagnetic-waves.md](electromagnetic-waves/Electromagnetic-waves.md) |
| 4 | Thermodynamics | [thermodynamics/Thermodynamics.md](thermodynamics/Thermodynamics.md) |
| 5 | Heat | [heat/Heat.md](heat/Heat.md) |
| 6 | Capacitors | [capacitors/Capacitors.md](capacitors/Capacitors.md) |
| 7 | Current electricity | [current-electricity/Current-electricity.md](current-electricity/Current-electricity.md) |
| 8 | Geometrical optics | [geometrical-optics/Geometrical-optics.md](geometrical-optics/Geometrical-optics.md) |
| 9 | Wave optics | [wave-optics/Wave-optics.md](wave-optics/Wave-optics.md) |

---

## 6. Priority recommendation

1. **PART 11 fluids, then PART 12 elasticity.** They close mechanics, both have a
   PDF in this repository to sweep, and both are prerequisites for later work
   (PART 11 hands the shallow-water wave speed to the shipped sound-waves note
   and the momentum-flux argument back to PART 7).
2. **PART 13 → 14 → 15 Coulomb/Gauss/potential.** The only E&M parts with a
   verifiable Cengage floor here, and each is the successor of the one before.
3. **PART 16 → 17, then 18 and 19 in parallel.** Magnetism proper; 18 and 19 both
   need only 17.
4. **PART 20 → 21 → 22 as one batch.** EMI, inductance and AC are one argument.
5. Nothing else is outstanding. When PART 22 lands, plan.md's 28 parts are
   complete and this file should say so.

---

## 7. Repository integration — current state

These are the cross-cutting chores, so a chapter agent knows what is already
wired up and what it still has to do.

| integration point | state |
|---|---|
| `topics.json` registry | 26 topics, all `complete`, all with `format`/`entry`/`owner` and mechanically recounted counts. Gate green. |
| `tools/check_all.py` | green (`python3 tools/check_all.py --quick`). Every Markdown-first topic now has an `entry`, so its counts are actually checked rather than assumed. |
| `tools/md_site.py` / `docs/site/` | **all 26 topics render**, grouped by block, with Obsidian callouts, frontmatter properties, wikilinks and `DIAGRAM` briefs styled. Regenerate with `python3 tools/md_site.py` (needs `pip install markdown`). |
| [README.md](README.md) | one row per note-set in the table; keep the counts matching the registry after each recount. |
| [CURRICULUM.md](CURRICULUM.md) | **stale** — it still describes nine note-sets and does not mention the sixteen plan.md chapters. Coordinator job (plan.md §6.2), not a chapter-agent job. |

---

## Claiming a topic

1. In [`topics.json`](topics.json), append one object for your slug (template:
   plan.md Appendix C.7) with `"status": "in-progress"`, your `"owner"`,
   `"entry": "<slug>/<Title>.md"`, `"format": "markdown"`, `"plan_part": <N>`,
   `"source"`, `"exam"`, `"media"` and `"beyond_plan"`. Leave every mechanical
   count to `--update`.
2. Scaffold the four files of plan.md §1.1: `<Title>.md`, `README.md`,
   `notes.json`, `tools/check.py` (copied verbatim from Appendix C.2).
   `tools/new_topic.py` scaffolds the *HTML-first* layout; the plan.md chapters
   are Markdown-first and text-only, so most agents write the four files
   directly from the Appendix C templates.
3. Write it to the **15-block spine** of plan.md §1.4.
4. **Obsidian-first, text-only Markdown** (plan.md §1.3.1): frontmatter,
   callouts, `$...$` / `$$...$$`, `<details>` solutions, and inline
   `> [!abstract] DIAGRAM D<N>.<k>` figure briefs (§1.2) — no image files, no
   SVG, no bitmaps, no CDN. The nine shipped note-sets keep their local SVGs.
5. **Sweep the book** (plan.md §1.12). Read your Cengage chapter's own contents
   page from the PDF in this repo (§1.13) and account for every heading in the
   block-0 coverage map. Record what you added under `## Beyond the plan` in the
   chapter README and in `topics.json` `beyond_plan`.
6. Run `cd <slug> && python3 tools/check.py` until it prints `ALL GOOD`, then
   `python3 tools/check_all.py --update` from the root. Flip `status` to
   `complete` when both are green.
7. Add your row to [README.md](README.md), mark your line in this file, and —
   coordinator step — append one tuple to `TOPICS` and one line to
   `SLUG_BY_NOTE` in `tools/md_site.py`, then regenerate `docs/site/`.
