# Pending chapters — JEE Advanced & Olympiad Physics notes

Generated: 2026-09-22. The nine note-sets listed in [README.md](README.md)
(capacitors, current electricity, heat, thermodynamics, geometrical optics,
wave optics, string waves, sound waves, electromagnetic waves) are complete
and pass `python3 tools/check_all.py`. Everything below is the rest of a
standard JEE Advanced / NSEP / INPhO / IPhO syllabus, organised so a
contributor can claim one topic, scaffold it with `python3 tools/new_topic.py`,
and write it to the same standard (proof-first, Cengage floor + Olympiad
extension, 8-part didactic structure, SVG figures, interleaved solutions,
final paper, formula sheet — see [CONTRIBUTING.md](CONTRIBUTING.md)).

To claim a topic, open a PR (or an issue) that sets its `"owner"` in
[`topics.json`](topics.json) and flips `"status"` to `"in-progress"`. **[plan.md](plan.md) numbers every remaining chapter as PART 1 … PART 28** (mechanics 1–12, electricity and magnetism 13–22, modern physics 23–28), so a chapter is claimed by part number — *"execute PART 17"*. Nothing
below is locked; `rotational-mechanics` is already in the registry as a
suggestion but not yet scaffolded.

Reading order is the suggested dependency order; earlier topics are
prerequisites for later ones.

---

## 0. How these rows map to plan.md's PART numbers

[plan.md](plan.md) is now the authoritative document and numbers every one of these chapters
**PART 1 … PART 28**; the tables below use the older M/E/P ordering, so use this bridge:

| PENDING rows | plan.md parts |
|---|---|
| M1 units-measurements · M3 vectors · M2 kinematics-1d · M4 projectile-motion · M5 newtons-laws · M6 work-energy-power · M7 center-of-mass · M8 rotational-mechanics · M9 gravitation · M10 simple-harmonic-motion · M11 fluid-mechanics · M12 elasticity | **PART 1–12** (in that order: vectors now precedes 1-D kinematics) |
| E1 coulomb-electric-field · E2 gauss-law · E3 electric-potential · E4 magnetic-field · E5 amperes-law · E6 moving-charges-magnetism · E7 magnetism-matter · E8 electromagnetic-induction · E9 inductance · E10 ac-circuits | **PART 13–22** |
| P1 photoelectric-effect · P2 atomic-structure · P3 x-rays · P4 nuclear-physics · P5 radioactivity | **PART 23–26** (P5 is merged into PART 26, as its own row suggests) |
| P6 semiconductors · P7 communication-systems · P8 special-relativity | **PART 27** · *dropped* (JEE-Main-only; see plan.md Appendix B) · **PART 28** |
| M0 capacitors and the current-electricity rows | already shipped: [capacitors/](capacitors/), [current-electricity/](current-electricity/) — do not rewrite |

Each of those parts carries its own source line, teaching order, must-derive list, figure briefs,
archetypes, Olympiad block and traps. Claim a chapter by part number and follow plan.md §1.

---

## 1. Mechanics (Cengage *Mechanics 1* and *Mechanics 2*)

Both mechanics volumes are supplied as reference PDFs, **committed in this
repository** (`Cengage  MECHANICS  1-compressed.pdf`, `Cengage MECHANICS 2-compressed.pdf`
— `git ls-files | grep pdf`), but **no note-set yet exists** for any of the
mechanics chapters. These are the foundation for everything else. plan.md §1.13 maps each
PDF to the chapters it really contains — note that *Mechanics II* has no separate
work-energy chapter (it lives inside ch 2 *Rigid Body Dynamics*) and that SHM is in the
*Waves and Thermodynamics* volume, not *Mechanics II*.

| order | slug (suggested) | title | scope / Cengage floor | depends on |
|---:|---|---|---|---|
| M1 | `units-measurements` | Units, Dimensions & Measurement Errors | SI, dimensional analysis, significant figures, error propagation, vernier / screw-gauge | — |
| M2 | `kinematics-1d` | Kinematics in One Dimension | position/velocity/acceleration, graphs, constant-`a` equations, free fall | M1 |
| M3 | `vectors` | Vectors & Vector Algebra | components, dot/cross product, unit vectors, resolution | M1 |
| M4 | `projectile-motion` | Projectile & 2-D Motion | oblique projection, range/max-height, projection from height/tower, relative velocity | M2, M3 |
| M5 | `newtons-laws` | Newton's Laws of Motion | N1/N2/N3, pseudo forces, constraint motion (pulleys, wedges), friction (static/kinetic) | M4 |
| M6 | `work-energy-power` | Work, Energy & Power | work by constant/variable force, work-energy theorem, conservative forces, potential energy, power | M5 |
| M7 | `center-of-mass` | Center of Mass, Momentum & Collisions | COM, conservation of momentum, variable mass (rocket), elastic/inelastic collisions, impulse | M6 |
| M8 | `rotational-mechanics` | Rotational Mechanics *(already in topics.json as planned)* | moment of inertia, parallel/perpendicular axes, torque, $\vec{\tau}=I\vec{\alpha}$, angular momentum, rolling motion, gyroscopic precession | M7 |
| M9 | `gravitation` | Gravitation | universal law, g variation (altitude/depth/rotation), orbital motion, Kepler, escape velocity, satellites, gravitational PE | M8 |
| M10 | `simple-harmonic-motion` | Simple Harmonic Motion | differential equation, $x=A\sin(\omega t+\phi)$, spring-mass, simple & compound pendulum, energy, damped/forced (intro), SHM as circular-motion projection | M6, M8 |
| M11 | `fluid-mechanics` | Fluid Mechanics (Hydrostatics & Hydrodynamics) | pressure, Pascal/Archimedes, surface tension, Bernoulli, Torricelli, Venturi, viscosity, Stokes, Reynolds | M5, M7 |
| M12 | `elasticity` | Elasticity & Properties of Matter | stress/strain, Hooke, Young/Bulk/Shear moduli, Poisson ratio, beam bending (intro) | M5 |

---

## 2. Electrostatics & Magnetism (Cengage *Electrostatics and Current Electricity* ch. 1–3; standalone magnetism/EMI volumes)

Capacitors (ch. 4) and Current Electricity (chs. 5–7) are **already complete**.
What is missing is the run-up to capacitors and the entire magnetism / EMI /
AC block.

| order | slug (suggested) | title | scope / Cengage floor | depends on |
|---:|---|---|---|---|
| E1 | `coulomb-electric-field` | Coulomb's Law & Electric Field | Coulomb, superposition, E due to rod/ring/disc/arc, dipole in E field, electric lines of force | M4 |
| E2 | `gauss-law` | Gauss's Law & Electric Flux | flux, Gauss, applications (shell, sheet, wire, solid sphere, conductor) | E1 |
| E3 | `electric-potential` | Electric Potential & Potential Energy | $V = kq/r$, potential due to distributions, equipotentials, $\mathbf{E}=-\nabla V$, conductors in equilibrium, $W=q\Delta V$ | E2 |
| M0 (placed here because Capacitors depends on it — note: already covered in capacitors §1 from field theory, but a standalone note is a candidate) | — | Capacitors & Capacitance | — | **already in repo: [capacitors/](capacitors/)** |
| E4 | `magnetic-field` | Magnetic Field & Biot–Savart | $\mathbf{B}$ due to straight wire, loop, arc, solenoid, ampere definition; Lorentz force | E3, M3 |
| E5 | `amperes-law` | Ampère's Law & Magnetic Forces on Currents | Ampère applications (wire, solenoid, toroid); force on current wire; force between parallel wires; torque on current loop / magnetic dipole | E4 |
| E6 | `moving-charges-magnetism` | Motion of Charged Particles in B Fields | cyclotron radius/helix, velocity selector, cyclotron, J.J. Thomson, Hall effect | E4 |
| E7 | `magnetism-matter` | Magnetism & Matter | para/dia/ferro, magnetisation $\mathbf{M}$, $\mathbf{H}$, hysteresis, Earth's magnetism, magnetic materials | E5 |
| E8 | `electromagnetic-induction` | Electromagnetic Induction (Faraday / Lenz) | magnetic flux, Faraday, Lenz, motional emf, induced E field, eddy currents | E5, M10 |
| E9 | `inductance` | Self & Mutual Inductance | $L$, $M$, solenoid/toroid inductance, RL circuits, L/R time constant, energy in B field | E8 |
| E10 | `ac-circuits` | Alternating Current & RLC Circuits | phasors, LCR series/parallel, resonance, Q-factor, power factor, transformer, LC oscillations | E9, M10 |

---

## 3. Optics & Modern Physics (Cengage *Optics and Modern Physics*)

Geometrical Optics (ch. 1) and Wave Optics (ch. 2) are **already complete**.
The modern-physics half of that volume is the largest single remaining block.

| order | slug (suggested) | title | scope / Cengage floor | depends on |
|---:|---|---|---|---|
| P1 | `photoelectric-effect` | **PART 23 — complete (arena-agent)** · Photoelectric Effect & Dual Nature | photon hypothesis, Einstein equation, stopping potential, cutoff, de Broglie, Davisson–Germer | E3 |
| P2 | `atomic-structure` | **PART 24 — complete (arena-agent)** · Atomic Structure (Bohr Model & Beyond) | Rutherford scattering, Bohr postulates, H-atom spectra, X-rays (Mosley), Bohr shortcomings, Sommerfeld, quantum numbers (intro) | P1 |
| P3 | `x-rays` | **PART 25 — complete (arena-agent)** · X-rays — production, spectra & Bragg | continuous/characteristic, $f_{\min}$, Moseley, Bragg diffraction, Compton scattering | P2 |
| P4 | `nuclear-physics` | Nuclear Physics | nuclear size/density, binding energy / mass defect, radioactivity (α β γ, decay law), half-life/mean-life, chain reaction, fission/fusion | P2 |
| P5 | `radioactivity` | Radioactivity & Decay Kinetics *(can be merged into P4)* | decay series, secular/transient equilibrium, carbon dating, statistical nature | P4 |
| P6 | `semiconductors` | Semiconductors & Electronic Devices | bands, intrinsic/extrinsic, p-n junction diode, LED, Zener, transistor (BJT) basics, logic gates (intro) | E10 |
| P7 | `communication-systems` | Communication Systems | amplitude/frequency modulation, bandwidth, EM-propagation modes, signal processing (intro, JEE-main level only) | EM-waves |
| P8 | `special-relativity` | Special Relativity *(olympiad/extension)* | postulates, time dilation, length contraction, relativistic momentum/energy, $E=mc^2$, Doppler (optical) | M6, EM-waves |

---

## 4. Thermodynamics / Matter already covered

The two matter-and-heat volumes share several chapter lists with what is
already in the repo. No duplicate note-sets are wanted here:

- ✅ thermodynamics (kinetic theory, first & second law, entropy, engines) — [thermodynamics/](thermodynamics/)
- ✅ heat transfer & calorimetry — [heat/](heat/)
- ❓ **Thermal expansion / calorimetry / kinetic theory** — already folded into
  `heat/` and `thermodynamics/` (see their Cengage coverage maps); no separate
  note-set planned unless a hole is found during review.

---

## 5. Already complete (quick index, so the list above is the complement)

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

If you are picking up work from scratch, the highest-leverage order is:

1. **M5 Newton's laws → M6 Work/energy → M7 COM → M8 Rotational mechanics** —
   these are the spine of every mechanics problem, and mechanics is roughly
   30–35 % of any JEE Advanced paper. `rotational-mechanics/` is already
   registered as `planned`.
2. **E1–E3 Coulomb/Gauss/Potential → E4–E7 Magnetism → E8–E9 EMI/Inductance
   → E10 AC circuits** — the second-largest weight on JEE Advanced, and all
   four blocks sit directly on top of the existing capacitors/current notes.
3. **P1–P4 Photoelectric → Atom → X-rays → Nucleus** — the modern-physics
   octave that closes the Cengage *Optics and Modern Physics* volume.
4. **M10 SHM, M11 Fluids, M9 Gravitation, M12 Elasticity** — important
   standalone topics that can be written in parallel after M5–M8.
5. **M1–M4 Units, vectors, 1-D kinematics, projectiles** — shorter, mostly
   school-level, but needed for completeness.

---

## Claiming a topic

1. In [`topics.json`](topics.json), add an entry (or copy the existing
   `rotational-mechanics` stub):
   ```json
   { "slug": "<kebab-name>", "title": "...", "status": "in-progress",
     "owner": "<your-handle>", "entry": "<kebab-name>/index.html",
     "exam": ["JEE Advanced", "NSEP", "INPhO", "IPhO"] }
   ```
2. Scaffold: `python3 tools/new_topic.py <slug> --title "<Title>" --chapters "01-..."`.
3. Write it to the structure in [plan.md](plan.md) §1.4 — the **15-block spine** (for the chapters numbered PART 1–28 below) — or the eight-part structure of the archived v1 blueprint for the wave/optics topics.
4. Into the note-set: **Obsidian-first, text-only Markdown** (plan.md §1.3.1 — frontmatter, callouts, `$...$`/`$$...$$`, `<details>` solutions) with inline `> [!abstract] DIAGRAM D<n>.<k>` figure briefs (plan.md §1.2) for every new chapter — no image files, no SVG, no bitmaps, no CDN. The shipped wave/optics topics keep their existing local SVG figures.
5. **Sweep the book.** Read your Cengage chapter's own contents page from the PDF in this repo (plan.md §1.13) and close every gap the plan left, recording what you added under `## Beyond the plan` in the chapter README and in `topics.json` `beyond_plan` (plan.md §1.12).
6. Run `python3 tools/check_all.py --update` to refresh the registry counts
   and validate. Flip `status` to `complete` when the gate is green.
7. Add the topic to `tools/md_site.py` `TOPICS` and `name_map` lists, regenerate
   with `python3 tools/md_site.py`, and update this file and the README table.
