# Curriculum map: Cengage floor → JEE → Olympiad

This repository now has two readers for the same six consolidated note-sets (three more are registered in
`topics.json` as the wave sequence below and are not on disk yet):

- the `*.md` files are the portable editions, with standard Markdown, `$...$` / `$$...$$` math, collapsible solutions and local SVG diagrams;
- the `*.html` files are the optional interactive editions, retained for the generated table of contents, progress ticks, theme switch and printing.

The order below is intentional. Read the theory in the first column before attempting the paper/gauntlet in the last column. Within every file the same rule applies: **concepts → derivation → worked question → checkpoint → playbook → paper → solutions → formula sheet**.

## Recommended reading order

| order | note | first pass | JEE/Cengage floor | Olympiad extension |
|---:|---|---|---|---|
| 1 | String waves · *planned* (plan.md PART 1) | disturbance vs matter transport → the 1-D wave equation from Newton's second law → energy and power → boundary reflection and impedance → standing waves and normal modes | the mechanical-wave floor named in plan.md §2 PART 1, plus the sonometer and Melde | hanging-rope waves, WKB amplitude scaling, phasor sums |
| 2 | Sound waves · *planned* (plan.md PART 2) | displacement vs pressure waves → Laplace's speed → intensity and decibels → columns, end-correction and resonance → beats → Doppler | the acoustic floor named in plan.md §2 PART 2, incl. Quincke's tube and Kundt's tube | oblique and accelerated Doppler, moving-wall echoes, Mach cones |
| 3 | Electromagnetic waves · *planned* (plan.md PART 3) | displacement current → Maxwell's equations → the wave equation for E and B → Poynting → radiation pressure → spectrum | the EM floor named in plan.md §2 PART 3 | momentum of light, curved-surface radiation force, spectrum as a working table |
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
states the debt explicitly and why the first three links, while still on the drawing board, are registered ahead of
it in `topics.json`. A reader who has none of them can still use the wave-optics note as written — it re-derives what
it uses — but the three notes are what turn "light happens to obey this equation" into "any linear restoring
mechanism obeys this equation, and light is one of them".

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
