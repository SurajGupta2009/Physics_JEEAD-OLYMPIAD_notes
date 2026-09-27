# Pending chapters — JEE Advanced & Olympiad Physics notes

Regenerated 2026-09-27 from the repository state (`topics.json` + the topic folders), so it agrees
with `python3 tools/check_all.py` (28 registered topics, gate green). The Obsidian mirror of this
list is [`_obsidian/dashboards/pending.md`](_obsidian/dashboards/pending.md).

**Score: 18 of the 28 [plan.md](plan.md) parts are written; 10 remain.** Mechanics (PART 1–12)
and Modern Physics (PART 23–28) are closed. Everything left is **Electricity & Magnetism,
PART 13–22** — the only chapter-sized gaps in the syllabus this repository set out to cover.

## 0 · Score board

| block | parts | written | remaining |
|---|---|---:|---:|
| A · Mechanics | 1–12 | 12 | — |
| B · Electricity & magnetism | 13–22 | 0 | **10** |
| C · Modern physics | 23–28 | 6 | — |
| Original note-sets (plan.md Appendix A: waves, thermal, capacitors, current, optics) | — | 9 | — |
| Appendix chapter (`communication-systems`, JEE-Main depth) | — | 1 | — |

## 1 · The ten pending chapters, in teaching order

The order below is the dependency order and the course order: each chapter uses only what the
ones above it have derived. `order` is the slot the chapter takes in the course spine
([`_obsidian/dashboards/spine.md`](_obsidian/dashboards/spine.md)); write it into the chapter's
frontmatter together with `block: electricity-magnetism`. Size bands are plan.md §5.3 (compact
9–13k words · standard 12–16k · large 16–22k). The section-by-section teaching order, the
must-derive list, the figure briefs and the Olympiad block for every part are in plan.md §4.

| PART | slug | title | order | size | needs | Cengage floor | the one idea |
|---:|---|---|:-:|---|---|---|---|
| 13 | `electric-field` | Charge, Coulomb's Law & Electric Field | 17 | large | PART 2 | *Electrostatics & Current Electricity* ch 1 — **PDF in repo** | the field is the bookkeeping device for forces at a distance; superposition makes every distribution a sum of point charges |
| 14 | `gauss-law` | Electric Flux & Gauss's Law | 18 | standard | 13 | ch 2 — **PDF in repo** | flux counts field lines through a surface, and symmetry turns that count into the fastest way to find a field |
| 15 | `electric-potential` | Electric Potential, Potential Energy & Conductors | 19 | standard | 14 | ch 3 — **PDF in repo** | potential turns a vector problem into a scalar one, at the price of a direction you recover by differentiating |
| 16 | `magnetic-field` | Magnetic Field, Biot–Savart & the Lorentz Force | 22 | large | 15 | no PDF — standard JEE Advanced headings | a magnetic field is what a moving charge calls the relativistic correction to the electric force; its effects are always perpendicular to motion |
| 17 | `amperes-law` | Ampère's Law, Currents & Magnetic Dipoles | 23 | standard | 16 | no PDF | Ampère's law is Gauss's law for currents — symmetry plus a loop integral gives the field |
| 18 | `moving-charges-magnetism` | Cyclotron, Velocity Selector & the Hall Effect | 24 | standard | 17 | no PDF | in a magnetic field a charge circles to a clock whose rate depends only on $q/m$ and $B$ — that single fact is an industry |
| 19 | `magnetism-and-matter` | Magnetism & Matter, Earth's Magnetism | 25 | compact | 17 | no PDF | matter responds through induced (dia), aligned (para) or permanently ordered (ferro) dipoles |
| 20 | `electromagnetic-induction` | Faraday, Lenz, Motional EMF & Eddy Currents | 26 | standard | 17 | no PDF | a changing flux drives an electric field, and Lenz's law is energy conservation in disguise |
| 21 | `inductance` | Self & Mutual Inductance, RL Circuits & Magnetic Energy | 27 | standard | 20 | no PDF | a coil resists changes in its own current because the energy lives in the field, not in the wire |
| 22 | `alternating-current` | Alternating Current, Resonance & Transformers | 28 | large | 21 | no PDF | in AC everything is a phase relationship; impedance is resistance that knows about time |

### Scope, chapter by chapter (the JEE floor each must cover; the Olympiad layer is plan.md §4)

- **13 · electric-field** — charge and its quantisation/conservation; induction; Coulomb's law in vector form and superposition; $\mathbf E$ and field lines; the *element-and-symmetry method* (ring axis as the template); rod, disc, sheet, arc, shell by integration; conductors in the field picture and the $\sigma/\varepsilon_0$ vs $\sigma/2\varepsilon_0$ resolution; dipole fields, torque and $U=-\mathbf p\cdot\mathbf E$; equilibrium of charges and Earnshaw; motion of charges in uniform fields (projectile analogy, Millikan).
- **14 · gauss-law** — flux and the outward-normal convention; the solid-angle proof; Gauss's law and its equivalence to Coulomb + superposition; the four-step Gaussian-surface protocol; spherical, cylindrical and planar symmetry (shell, solid sphere, $\rho\propto1/r^2$, line, thick wire, coaxial, sheet, slab); conductors and cavities, Faraday cage, sharp edges; flux without the field (cube-corner family); $\mathbf D$ pointer; Gauss for gravity and the shell theorem.
- **15 · electric-potential** — why a potential exists (conservative field); $W=q\,\Delta V$, reference choices; potential of distributions (scalar superposition, shell, sphere, ring, disc); $\mathbf E=-\nabla V$ and equipotentials; the differentiate-instead-of-integrate method; $V=0$ vs $\mathbf E=0$; energy of a system of charges and self-energy; conductors: equipotential bodies, connected spheres, charge sharing, the dielectric section that hands off to `capacitors/`.
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
| 1 | 13 → 14 → 15 | serial — each is the successor of the one before, and these three have a PDF to sweep |
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
| 23 | `photoelectric-effect` | 32 | [Photoelectric-effect.md](photoelectric-effect/Photoelectric-effect.md) |
| 24 | `atomic-structure` | 33 | [Atomic-structure.md](atomic-structure/Atomic-structure.md) |
| 25 | `x-rays` | 34 | [X-rays.md](x-rays/X-rays.md) |
| 26 | `nuclear-physics` | 35 | [Nuclear-physics.md](nuclear-physics/Nuclear-physics.md) — absorbs the old P5 radioactivity row |
| 27 | `semiconductors` | 36 | [Semiconductors.md](semiconductors/Semiconductors.md) |
| 28 | `special-relativity` | 38 | [Special-relativity.md](special-relativity/Special-relativity.md) |

Plus `communication-systems` (order 37): JEE-Main depth, deliberately not a plan.md part.

## 4 · The nine original note-sets (plan.md Appendix A — do not rewrite, do not renumber)

| order | topic | location |
|:-:|---|---|
| 13 | String waves | [string-waves/String-waves.md](string-waves/String-waves.md) |
| 14 | Sound waves | [sound-waves/Sound-waves.md](sound-waves/Sound-waves.md) |
| 15 | Thermodynamics | [thermodynamics/Thermodynamics.md](thermodynamics/Thermodynamics.md) |
| 16 | Heat | [heat/Heat.md](heat/Heat.md) |
| 20 | Capacitors | [capacitors/Capacitors.md](capacitors/Capacitors.md) |
| 21 | Current electricity | [current-electricity/Current-electricity.md](current-electricity/Current-electricity.md) |
| 29 | Electromagnetic waves | [electromagnetic-waves/Electromagnetic-waves.md](electromagnetic-waves/Electromagnetic-waves.md) |
| 30 | Geometrical optics | [geometrical-optics/Geometrical-optics.md](geometrical-optics/Geometrical-optics.md) |
| 31 | Wave optics | [wave-optics/Wave-optics.md](wave-optics/Wave-optics.md) |

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
5. **Sweep the book** (plan.md §1.12) for PART 13–15: open the Cengage *Electrostatics* PDF in the
   vault, read the chapter's contents page, and account for every heading in the block-0 coverage
   map. PART 16–22 build the map from the headings listed in their plan.md sections.
6. **Gate.** `cd <slug> && python3 tools/check.py` → `ALL GOOD`; then
   `python3 tools/check_all.py --update` at the root. Flip `status` to `complete`, tick the row in
   §1 of this file and in `_obsidian/dashboards/pending.md`, append the topic to `TOPICS` /
   `SLUG_BY_NOTE` in `tools/md_site.py`, and regenerate `docs/site/`.

## 6 · Repository integration — current state

| integration point | state |
|---|---|
| `topics.json` registry | 28 topics, all `complete`, each with `format` / `entry` / `owner` / `order` / `block` and mechanically recounted counts; gate green |
| `tools/check_all.py` | green; also checks that every master's frontmatter `order`/`block` equals the registry |
| Obsidian vault | `.obsidian/` committed (settings, CSS snippet, eight plugins configured and pinned in `plugins.lock.json`); plugin binaries are fetched by `python3 tools/obsidian_plugins.py` — see [`_obsidian/README.md`](_obsidian/README.md) |
| `tools/md_site.py` / `docs/site/` | all 28 topics render; regenerated 2026-09-27 |
| [README.md](README.md) | one row per note-set; keep the counts matching the registry after each recount |
| [CURRICULUM.md](CURRICULUM.md) | carries the full course order (all 38 slots) at the end |
