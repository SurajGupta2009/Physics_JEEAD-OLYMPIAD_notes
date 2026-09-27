# Curriculum map: Cengage floor → JEE → Olympiad

This repository has two generations of notes. The nine note-sets in the table below were the original courses: seven have Markdown and interactive HTML editions; String Waves and Electromagnetic Waves are Markdown-first. Parts 1–12 and 23–28 of [plan.md](plan.md) are a second generation, text-only and Obsidian-first, with Mermaid `FIGURE` callouts and `DIAGRAM` briefs instead of image files. The table immediately below is the original **wave-first spine** — the order in which the first nine notes were written, and still the right order *within* the wave/optics material. **The order to study the whole vault is the course spine in [§ The course order](#the-course-order-all-38-slots) at the end of this file** — mechanics first, then waves and thermal physics, then electricity and magnetism, then EM waves and optics, then modern physics. Every chapter carries that slot in its frontmatter as `order:`.

- the `*.md` files are the portable editions, with standard Markdown, `$...$` / `$$...$$` math, collapsible solutions and local SVG diagrams;
- the `*.html` files are the optional interactive editions, retained for the generated table of contents, progress ticks, theme switch and printing.

The order below is intentional. Read the theory in the first column before attempting the paper/gauntlet in the last column. Within every file the same rule applies: **concepts → derivation → worked question → checkpoint → playbook → paper → solutions → formula sheet**.

## Recommended reading order

| order | note | first pass | JEE/Cengage floor | Olympiad extension |
|---:|---|---|---|---|
| 1 | [String Waves](string-waves/String-waves.md) | disturbance vs matter transport → the 1-D wave equation from Newton's second law → energy and power → boundary reflection and impedance → standing waves and normal modes | the mechanical-wave floor named in plan.md §2 PART 1, plus the sonometer and Melde | hanging-rope waves, WKB amplitude scaling, Bessel standing modes, mechanical impedance |
| 2 | [Sound Waves](sound-waves/Sound-waves.md) | longitudinal $s$ & pressure $\Delta P$, $v=\sqrt{B/\rho}$, Laplace $\sqrt{\gamma RT/M}$, intensity & dB, organ pipes & end-correction, beats, Doppler with wind/2D/echo, Mach cone | Cengage *Waves and Thermodynamics* – sound: longitudinal waves, speed (Newton vs Laplace), intensity, organ pipes, beats, Doppler, supersonic | Impedance matching, accelerated Doppler & closest approach glide, WKB for horns, acoustic ranging, shock |
| 3 | [Electromagnetic Waves](electromagnetic-waves/Electromagnetic-waves.md) | Displacement current → Maxwell → vector waves → energy/momentum → pressure → spectrum | Part 3 plan scope: vacuum/material Maxwell equations, both wave-equation derivations, fields/intensity, normal and oblique pressure, EM spectrum and sources | Poynting/stress derivations, spherical force integration, impedance matching, standing waves, isotropic pressure, conducting-medium limit |
| 4 | [Thermodynamics](thermodynamics/Thermodynamics.md) | Temperature and equilibrium → kinetic theory → first law → heat capacities/processes → second law → entropy | Temperature scales, expansion, kinetic theory, calorimetry, work, ideal-gas processes, engines and refrigerators | Equipartition limits, distributions/effusion, hydrostatic atmospheres, van der Waals criticality, radiation as a working fluid, entropy counting |
| 5 | [Heat](heat/Heat.md) | Heat/temperature/internal energy → expansion → calorimetry and phase change → conduction → convection/cooling → radiation | Specific heat, latent heat, thermal expansion, calorimetry, Fourier/Newton/Stefan–Boltzmann laws and thermal resistance | Heat equation and diffusion time, thermal waves, effusivity, fins, critical insulation radius and radiation-balance estimates |
| 6 | [Current Electricity](current-electricity/Current-electricity.md) | Current/drift → resistance/materials → cells → Kirchhoff/bridges → network theorems → instruments | Cengage *Electric Current and Circuits* (ch. 5), *Electrical Measuring Instruments* (ch. 6) and *Heating Effects of Current* (ch. 7) | Reciprocity/compensation, loaded four-terminal measurements, thermoelectricity, thermistor stability, transmission scaling and superconducting ledgers |
| 7 | [Capacitors](capacitors/Capacitors.md) | Charge/conductors/Gauss → capacitance geometries → energy/force → combinations → dielectrics → RC networks | Cengage *Capacitor and Capacitance* (ch. 4): capacitance, units, geometries, energy, force, combinations, Kirchhoff, dielectrics, breakdown and exercises | Method of images, coefficients of capacitance, Green reciprocity, conformal/wedge methods, spheroids, MEMS pull-in, dielectric loss and Rayleigh fission |
| 8 | [Geometrical Optics](geometrical-optics/Geometrical-optics.md) | Rays/plane mirrors → spherical mirrors → plane refraction → TIR → prisms/dispersion → lenses → instruments | Cengage *Optics and Modern Physics*, geometrical-optics chapter 1: mirrors, refraction, slabs, TIR, prisms, dispersion, spherical surfaces, lenses, combinations and instruments | Fermat as a variational principle, ray-transfer matrices, thick lenses, exact non-paraxial results, aberrations, rainbow/atmospheric refraction and étendue |
| 9 | [Wave Optics](wave-optics/Wave-optics.md) | Waves/Huygens → YDSE → thin films/Newton rings → interferometers → diffraction → polarisation | Cengage *Optics and Modern Physics*, wave-optics chapter 2: wavefronts, superposition/coherence, YDSE, optical path, films, biprism, Lloyd mirror, interferometer and exercises | Diffraction/gratings/resolution, coherence length and visibility, Fresnel coefficients, evanescent waves, Fabry–Perot, Abbe limit and olympiad measurements |

### Why the wave notes precede wave optics

The intended spine of this repository's wave material is

$$
\text{String Waves} \longrightarrow \text{Sound Waves} \longrightarrow \text{Electromagnetic Waves} \longrightarrow \text{Geometrical Optics} \longrightarrow \text{Wave Optics}
$$

and it is a chain of *methods*, not of topics. The string note owns the wave equation itself (Newton's second law on
an element of a stretched string, $v = \sqrt{T/\mu}$, and the rule that a harder boundary reflects with a phase
change of $\pi$); the sound note owns intensity as energy flux and the discipline of writing one wave in terms of
another (displacement versus pressure); the electromagnetic note owns the fact that light's wave is transverse, that
it needs no medium, and that $c = 1/\sqrt{\mu_0\epsilon_0}$. Wave optics then needs all three and nothing else,
which is why [wave-optics/Wave-optics.md §1.1.1](wave-optics/Wave-optics.md#111-one-equation-three-mechanisms-what-light-inherits)
states the debt explicitly. All three wave courses are now present and registered in `topics.json`. A reader who has none of them can still use the wave-optics note as written — it re-derives what
it uses — but the three notes are what turn "light happens to obey this equation" into "any linear restoring
mechanism obeys this equation, and light is one of them".

The [EM course coverage map](electromagnetic-waves/Electromagnetic-waves.md#13-coverage-and-study-route) maps every Part 3 requirement to theory and retrieval. Its 36-question paper is 180 minutes / 180 marks, with separate printable solutions. The Part 1, Part 2 and Part 4 work already on `main` is preserved.

### Why thermodynamics precedes heat

The heat note uses `U`, `Q`, `W` and the first-law ledger as established tools. It repeats every result needed for marks, but the thermodynamics note is the cleanest place to learn the state/process distinction and the sign convention. If those words are already secure, Heat can be read independently from its prerequisite paragraph.

### Why geometrical optics precedes wave optics

The wave note reuses refractive index, optical path and the slab geometry from geometrical optics. It then deliberately reverses the direction of explanation: rays become normals to wavefronts, and the familiar refraction rules become consequences of Huygens' construction. The wave note therefore starts with a prerequisite self-check rather than repeating the full ray course.

## Cengage coverage audit

The four notes that correspond directly to the supplied Cengage volumes carry their detailed row-by-row maps inside the Markdown file. The short audit below makes the scope visible from the root.

### Electrostatics and current electricity volume

| Cengage floor | Markdown location | status |
|---|---|---|
| Capacitor and Capacitance, chapter 4: definition, units, parallel plate, sphere, spherical/cylindrical capacitors, energy and energy density | [Capacitors.md — Cengage coverage map](capacitors/Capacitors.md#cengage-coverage) and parts 1–3 | derived, with limit checks |
| Combinations, capacitor Kirchhoff/sign convention, bridges, cube, ladders and redistribution | [Capacitors.md — part 4](capacitors/Capacitors.md#section-04-combinations) | derived before problems |
| Dielectric constant, polarisation, bound charge, `D`, breakdown, force and parameter changes | [Capacitors.md — part 5](capacitors/Capacitors.md#section-05-dielectrics) | battery-connected and isolated cases both explicit |
| RC charging/discharging and time constant | [Capacitors.md — part 6](capacitors/Capacitors.md#section-06-networks-and-transients) | derived from the loop equation and extended to networks |
| Current, drift, continuity, microscopic Ohm law and resistivity | [Current Electricity.md — Cengage coverage map](current-electricity/Current-electricity.md#cengage-coverage), parts 1–2 | derived, not only quoted |
| EMF, internal resistance, cell grouping and power/heating audit | [Current Electricity.md — parts 3 and 7](current-electricity/Current-electricity.md#section-03-emf-and-cells) | source model and energy check included |
| Kirchhoff, Wheatstone/meter bridges, dividers, Δ–Y, ladders and network theorems | [Current Electricity.md — parts 4–5](current-electricity/Current-electricity.md#section-04-kirchhoff-and-bridges) | symmetry and nodal routes both taught |
| Galvanometer, ammeter, voltmeter, potentiometer and meter bridge | [Current Electricity.md — part 6](current-electricity/Current-electricity.md#section-06-instruments-and-measurement) | loading error and null measurement included |
| Heating effects, fuse, maximum power and applications | [Current Electricity.md — part 7](current-electricity/Current-electricity.md#section-07-advanced-topics) | extended to olympiad estimates |

### Waves and thermodynamics volume

| Cengage floor | Markdown location | status |
|---|---|---|
| String waves: disturbance, $v=\sqrt{T/\mu}$, $f(x\mp vt)$, energy/power, reflection, standing waves | [String Waves.md — §1–2](string-waves/String-waves.md#section-01-foundations) | wave equation from $F=ma$, $v$ derived |
| Longitudinal waves, $s(x,t)$, $\Delta P=-B\partial s/\partial x$, phase $\pi/2$, density variations | [Sound Waves.md — §1](sound-waves/Sound-waves.md#section-01-foundations) | derived, Fig.1.1 |
| Speed $v=\sqrt{B/\rho}$, $\sqrt{Y/\rho}$, Newton $v=\sqrt{P/\rho}$ vs Laplace $v=\sqrt{\gamma P/\rho}=\sqrt{\gamma RT/M}$, factors $T,M$, humidity, $P$ independence | [Sound Waves.md — §2.1–2.4](sound-waves/Sound-waves.md#section-02-derivations) | full derivation + limit checks |
| Intensity $I=\Delta P_0^2/2\rho v$, loudness dB $\beta=10\log(I/I_0)$, point $I\propto1/r^2$, line $I\propto1/r$ | [Sound Waves.md — §2.5](sound-waves/Sound-waves.md#section-02-derivations) | energy method, impedance |
| Organ pipes, closed $L=(2n-1)\lambda/4$ odd only, open $L=n\lambda/2$ all, end-correction $e=0.6r$, resonance tube $v=2f(l_2-l_1)$, Kundt's tube | [Sound Waves.md — §2.6–2.7](sound-waves/Sound-waves.md#section-02-derivations) | boundary conditions derived, Fig.2.4–2.6 |
| Interference Quincke's tube, beats $f_{\text{beat}}=|f_1-f_2|$, tuning fork wax/filing | [Sound Waves.md — §2.8](sound-waves/Sound-waves.md#section-02-derivations) | superposition + phasor |
| Doppler: moving source $\lambda'=(v\mp v_s)/f$, moving observer $v_{\text{rel}}=v\pm v_o$, wind $v\pm w$, 2D $v_s\cos\theta_s$, echo double shift, Mach $\sin\alpha=1/M$ | [Sound Waves.md — §2.9–2.12](sound-waves/Sound-waves.md#section-02-derivations) | master formula with projections, Fig.2.9–2.14 |

### Optics and modern physics volume

| Cengage floor | Markdown location | status |
|---|---|---|
| Plane and spherical mirrors, sign convention, image/velocity problems | [Geometrical Optics.md — parts 1–2](geometrical-optics/Geometrical-optics.md#section-01-rays-and-plane-mirrors) | derivation + ray diagrams + questions |
| Refraction, apparent depth, slabs, variable-index rays and refractive-index measurement | [Geometrical Optics.md — parts 3–4](geometrical-optics/Geometrical-optics.md#section-03-refraction-at-plane-surfaces) | standard and limiting cases |
| TIR, fibres, prisms and dispersion | [Geometrical Optics.md — parts 4–5](geometrical-optics/Geometrical-optics.md#section-04-total-internal-reflection) | JEE core before extensions |
| Spherical surfaces, lenses, combinations, silvered lenses and instruments | [Geometrical Optics.md — parts 6–7](geometrical-optics/Geometrical-optics.md#section-06-lenses-and-refracting-surfaces) | sign-safe derivations and applications |
| Wavefronts/Huygens, superposition and coherent sources | [Wave Optics.md — part 1](wave-optics/Wave-optics.md#section-01-waves-and-huygens) | wave picture established before interference; §1.1.1 links the scalar wave equation to the string, sound and EM notes |
| YDSE, fringe width/order/shape, white light, slabs and optical path | [Wave Optics.md — part 2](wave-optics/Wave-optics.md#section-02-interference-ydse) | all standard cases: angular fringe width §2.3, missing wavelengths §2.6, slab/liquid/unequal slits/displaced source/oblique incidence §2.7 |
| Thin films, wedges, Newton rings and coatings | [Wave Optics.md — part 3](wave-optics/Wave-optics.md#section-03-thin-films) | reflection phase changes stated explicitly |
| Biprism, Lloyd mirror, Michelson and fringe displacement | [Wave Optics.md — part 4](wave-optics/Wave-optics.md#section-04-interferometers) | instrument problems plus checks |
| Diffraction, grating, resolution and polarisation | [Wave Optics.md — parts 5–6](wave-optics/Wave-optics.md#section-05-diffraction) | JEE floor plus olympiad machinery: phasor arc, Airy disc and Rayleigh criterion, Malus, Brewster with the dipole argument, calcite $\lambda/4$ and $\lambda/2$ plates |

## Where the Olympiad layer begins

The level tags are not a second disconnected syllabus. They mark the point at which the same Cengage idea is pushed by a new method or a stricter check:

- **JEE Advanced core:** use the first theory chapters and their in-flow questions. The boxed result is always paired with a condition of validity.
- **NSEP/INPhO bridge:** use the advanced/olympiad toolkit chapters, where symmetry, scaling, limits, energy methods, differential equations or matrix methods are made explicit.
- **IPhO-style practice:** sit the final paper without notes, write the model before the algebra, and finish with a dimensional or limiting check. The full solutions are deliberately after the paper.

Every topic records its exclusions in `topics.json` and its own `README.md`; “covered through Olympiad” therefore means the complete stated scope, not an unbounded claim that every university topic is present. The main omissions are quantum optics, numerical simulation, advanced convection correlations and formal statistical-mechanics ensembles, named so the reader knows what to study next. One item that used to sit on that list is now a hand-off rather than a gap: the Maxwell-equation derivation of the Fresnel coefficients, which wave optics states without deriving, is the electromagnetic-waves note's own deliverable (see the wave-sequence section above).

## Markdown conversion contract

Each converted note has:

1. headings in reading order with stable anchors retained from the HTML;
2. inline math as `$...$` and display math as `$$...$$`, including equation tags as comments;
3. `<details>` solutions preserved so questions remain interleaved and self-contained;
4. one local SVG per source diagram, with embedded styles, marker definitions, alt text and the original asserting caption;
5. no CDN, JavaScript, external image or remote font dependency.

Regenerate all six with:

```bash
python3 tools/html_to_markdown.py
```

## The course order (all 33 slots)

The way the syllabus is taught, and the order the Obsidian dashboards use
([`_obsidian/dashboards/spine.md`](_obsidian/dashboards/spine.md)): every chapter relies only on the
ones above it. The `order` is registered in `topics.json` and written into each chapter's
frontmatter; `tools/check_all.py` keeps the two equal. Slot 17 is the electrostatics module
(plan.md PARTs 13–15 merged into one chapter, complete) and slot 20 the magnetism module (PARTs 16–19,
complete); the three **pending** slots are the induction → inductance → AC chapters listed in
[PENDING.md](PENDING.md).

| order | chapter | block | plan.md PART | status | it supplies the next chapters with |
|:-:|---|---|:-:|:-:|---|
| 1 | [Units, dimensions & errors](units-measurements/Units-measurements.md) | mechanics | 1 | ✅ | SI, dimensional analysis, error propagation |
| 2 | [Vectors](vectors/Vectors.md) | mechanics | 2 | ✅ | components, dot and cross products |
| 3 | [Kinematics in 1-D](kinematics-1d/Kinematics-1d.md) | mechanics | 3 | ✅ | $x(t)$, slopes and areas, $v\,dv/dx$ |
| 4 | [Motion in 2-D](motion-in-two-dimensions/Motion-in-two-dimensions.md) | mechanics | 4 | ✅ | projectiles, relative velocity, circular kinematics |
| 5 | [Newton's laws & friction](newtons-laws/Newtons-laws.md) | mechanics | 5 | ✅ | free-body diagrams, constraints, pseudo-forces |
| 6 | [Work, energy & power](work-energy-power/Work-energy-power.md) | mechanics | 6 | ✅ | conservative forces, potential-energy curves |
| 7 | [Centre of mass, momentum & collisions](centre-of-mass-momentum/Centre-of-mass-momentum.md) | mechanics | 7 | ✅ | systems of particles, impulse |
| 8 | [Rotational mechanics](rotational-mechanics/Rotational-mechanics.md) | mechanics | 8 | ✅ | torque, $I$, angular momentum, rolling |
| 9 | [Gravitation](gravitation/Gravitation.md) | mechanics | 9 | ✅ | the first field, shell theorem, orbits |
| 10 | [Simple harmonic motion](simple-harmonic-motion/Simple-harmonic-motion.md) | mechanics | 10 | ✅ | the oscillator every wave is built from; phasors; resonance |
| 11 | [Fluid mechanics & surface tension](fluid-mechanics/Fluid-mechanics.md) | mechanics | 11 | ✅ | pressure, buoyancy, Bernoulli, viscosity |
| 12 | [Elasticity & properties of matter](elasticity/Elasticity.md) | mechanics | 12 | ✅ | $Y$, $B$, $G$ — the restoring constants of waves |
| 13 | [String waves](string-waves/String-waves.md) | waves | — | ✅ | the wave equation, $v=\sqrt{T/\mu}$, reflection phase, standing waves |
| 14 | [Sound waves](sound-waves/Sound-waves.md) | waves | — | ✅ | intensity as energy flux, pipes, beats, Doppler |
| 15 | [Thermodynamics](thermodynamics/Thermodynamics.md) | thermal | — | ✅ | kinetic theory, the two laws, $\gamma$, entropy |
| 16 | [Heat](heat/Heat.md) | thermal | — | ✅ | expansion, calorimetry, conduction / convection / radiation |
| 17 | [Electrostatics](electrostatics/Electrostatics.md) | electricity-magnetism | 13–15 | ✅ | charge and Coulomb, the field of any distribution, Gauss, potential, energy of charges, conductors |
| 18 | [Capacitors](capacitors/Capacitors.md) | electricity-magnetism | — | ✅ | capacitance, dielectrics, RC transients |
| 19 | [Current electricity](current-electricity/Current-electricity.md) | electricity-magnetism | — | ✅ | drift, Kirchhoff, bridges, network theorems, instruments |
| 20 | [Magnetism](magnetism/Magnetism.md) | electricity-magnetism | 16–19 | ✅ | the Lorentz force and everything a charge does in a field, Biot–Savart and Ampère, forces and dipoles, matter, the Earth |
| 21 | Electromagnetic induction — `electromagnetic-induction` | electricity-magnetism | 20 | ⏳ pending | Faraday, Lenz, motional EMF, induced fields, eddy currents |
| 22 | Self & mutual inductance, RL circuits & magnetic energy — `inductance` | electricity-magnetism | 21 | ⏳ pending | $L$, $M$, $\tfrac12LI^2$, $B^2/2\mu_0$, LC oscillations |
| 23 | Alternating current, resonance & transformers — `alternating-current` | electricity-magnetism | 22 | ⏳ pending | phasors, impedance, resonance, power factor, transformers |
| 24 | [Electromagnetic waves](electromagnetic-waves/Electromagnetic-waves.md) | waves | — | ✅ | Maxwell's equations, $c=1/\sqrt{\mu_0\varepsilon_0}$, energy and pressure of light |
| 25 | [Geometrical optics](geometrical-optics/Geometrical-optics.md) | optics | — | ✅ | mirrors, refraction, prisms, lenses, instruments |
| 26 | [Wave optics](wave-optics/Wave-optics.md) | optics | — | ✅ | interference, diffraction, polarisation |
| 27 | [Photoelectric effect & matter waves](photoelectric-effect/Photoelectric-effect.md) | modern | 23 | ✅ | photons, de Broglie |
| 28 | [Atomic structure](atomic-structure/Atomic-structure.md) | modern | 24 | ✅ | Rutherford, Bohr, spectra |
| 29 | [X-rays](x-rays/X-rays.md) | modern | 25 | ✅ | Moseley, Bragg, Compton |
| 30 | [Nuclear physics](nuclear-physics/Nuclear-physics.md) | modern | 26 | ✅ | binding energy, radioactivity, fission and fusion |
| 31 | [Semiconductors](semiconductors/Semiconductors.md) | modern | 27 | ✅ | bands, diodes, transistors, logic |
| 32 | [Communication systems](communication-systems/Communication-systems.md) | modern | appendix | ✅ | modulation, bandwidth, propagation (JEE-Main depth) |
| 33 | [Special relativity](special-relativity/Special-relativity.md) | modern | 28 | ✅ | Lorentz transformations, $E=mc^2$, relativistic dynamics |

### Why this order

- **Mechanics first, in plan.md order.** Each part is the tool the next one uses: kinematics gives
  Newton's laws something to describe; energy and momentum are the two integrals of $F=ma$;
  rotation is the same laws for extended bodies; gravitation is the first field; SHM is the
  small-oscillation limit of everything before it; fluids and elasticity apply Newton to a
  continuum and supply the moduli that waves need.
- **Waves right after SHM and elasticity**, because a wave is SHM propagated through a medium and
  its speed is $\sqrt{\text{restoring modulus}/\text{inertia}}$ — $T/\mu$ for a string, $B/\rho$ for
  sound.
- **Thermodynamics before heat** (see the section above): heat uses $U$, $Q$, $W$ and the first-law
  ledger as established tools; thermodynamics also supplies the $\gamma$ in Laplace's speed of sound.
- **Electrostatics as one module in the order field → flux → potential**, then the two shipped circuit chapters
  (capacitors need potential and Gauss; current needs potential difference), then magnetism as one module in the
  order force → motion → sources → Ampère → forces and dipoles → matter → Earth, then induction →
  inductance → AC as one continuous argument (plan.md §0.4).
- **EM waves after AC**: Maxwell's displacement current completes Ampère's law, and the LC
  oscillator of the AC chapter is the radiating source. Geometrical optics is the short-wavelength
  limit; wave optics puts the wavelength back and needs the string, sound and EM-wave notes.
- **Modern physics last**, in plan.md order, with special relativity as the Olympiad capstone.
