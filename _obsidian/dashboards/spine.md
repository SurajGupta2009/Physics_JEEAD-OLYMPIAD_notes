# The course spine — read the vault in this order

This is the teaching order for the whole syllabus, mechanics first, the way a course is actually
taught: every chapter uses only what the chapters above it have already derived. It is carried by
the `order:` and `block:` properties in each chapter's frontmatter (registered in `topics.json`
and checked by `tools/check_all.py`), so the live table at the bottom cannot drift from this one.

Slots 17, 20 and 21 are the three merged Electricity & Magnetism modules: electrostatics (plan.md
PARTs 13–15, complete), magnetism (PARTs 16–19, complete) and induction–inductance–AC (PARTs 20–22,
complete). Nothing is pending — every plan.md part is written ([PENDING.md](../../PENDING.md) ·
[pending dashboard](pending.md)).

## Block A · Mechanics (plan.md PART 1–12)

| # | chapter | plan PART | why here |
|--:|---|:-:|---|
| 1 | [Units, dimensions & errors](../../units-measurements/Units-measurements.md) | 1 | the language: SI, dimensional analysis, significant figures, error propagation, vernier/screw gauge |
| 2 | [Vectors](../../vectors/Vectors.md) | 2 | every quantity from here on has a direction; components, dot and cross products |
| 3 | [Kinematics in 1-D](../../kinematics-1d/Kinematics-1d.md) | 3 | motion as one function $x(t)$; slopes and areas; calculus enters through physics |
| 4 | [Motion in 2-D](../../motion-in-two-dimensions/Motion-in-two-dimensions.md) | 4 | projectiles, relative velocity, circular kinematics — vectors applied to kinematics |
| 5 | [Newton's laws & friction](../../newtons-laws/Newtons-laws.md) | 5 | *why* things move: free-body diagrams, constraints, pseudo-forces, circular dynamics |
| 6 | [Work, energy & power](../../work-energy-power/Work-energy-power.md) | 6 | the first integral of $F=ma$; conservative forces and potential-energy curves |
| 7 | [Centre of mass, momentum & collisions](../../centre-of-mass-momentum/Centre-of-mass-momentum.md) | 7 | the second integral; systems of particles; impulse; the collision algebra |
| 8 | [Rotational mechanics](../../rotational-mechanics/Rotational-mechanics.md) | 8 | the same laws for extended bodies: torque, $I$, rolling, angular momentum |
| 9 | [Gravitation](../../gravitation/Gravitation.md) | 9 | the first field theory: shell theorem, $U=-GMm/r$, Kepler, orbits |
| 10 | [Simple harmonic motion](../../simple-harmonic-motion/Simple-harmonic-motion.md) | 10 | the universal small-oscillation limit; the phasor, energy, damping and resonance |
| 11 | [Fluid mechanics & surface tension](../../fluid-mechanics/Fluid-mechanics.md) | 11 | Newton applied to a continuum: pressure, buoyancy, Bernoulli, viscosity |
| 12 | [Elasticity & properties of matter](../../elasticity/Elasticity.md) | 12 | stress–strain, moduli, thermal stress — supplies the $Y$ and $B$ that waves need |

## Block B · Waves and thermal physics

| # | chapter | why here |
|--:|---|---|
| 13 | [String waves](../../string-waves/String-waves.md) | SHM propagated through a medium; the wave equation from $F=ma$ on a string element; standing waves |
| 14 | [Sound waves](../../sound-waves/Sound-waves.md) | the same equation with the bulk modulus; intensity, pipes, beats, Doppler |
| 15 | [Thermodynamics](../../thermodynamics/Thermodynamics.md) | kinetic theory, the first and second laws, entropy — the $\gamma$ behind Laplace's speed of sound |
| 16 | [Heat](../../heat/Heat.md) | expansion, calorimetry, phase change and the three transfer laws, using the first-law ledger |

## Block C · Electricity & magnetism

| # | chapter | plan PART | status | why here |
|--:|---|:-:|:-:|---|
| 17 | [Electrostatics](../../electrostatics/Electrostatics.md) | 13–15 | complete | Coulomb's law summed three ways — vectors (field), surfaces (flux), scalars (potential); the element-and-symmetry method; conductors; dipoles; energy |
| 18 | [Capacitors](../../capacitors/Capacitors.md) | — | complete | potential and Gauss applied to two conductors; dielectrics; RC transients |
| 19 | [Current electricity](../../current-electricity/Current-electricity.md) | — | complete | charge in motion: drift, Kirchhoff, bridges, network theorems, instruments |
| 20 | [Magnetism](../../magnetism/Magnetism.md) | 16–19 | complete | effect before cause: the Lorentz force and the speed-independent period, then currents as sources, then forces, dipoles, matter and the Earth |
| 21 | [Induction, inductance & AC](../../emi-ac/Emi-ac.md) | 20–22 | complete | one continuous argument: a changing flux drives an electric field; a coil resists changes in its own current; a sinusoidal drive makes every element a phase relationship |

## Block D · Electromagnetic waves and optics

| # | chapter | why here |
|--:|---|---|
| 22 | [Electromagnetic waves](../../electromagnetic-waves/Electromagnetic-waves.md) | Maxwell's equations close the E&M story: displacement current, $c=1/\sqrt{\mu_0\varepsilon_0}$, energy and pressure |
| 23 | [Geometrical optics](../../geometrical-optics/Geometrical-optics.md) | the short-wavelength limit: mirrors, refraction, prisms, lenses, instruments |
| 24 | [Wave optics](../../wave-optics/Wave-optics.md) | the wavelength back in: Huygens, YDSE, thin films, diffraction, polarisation — needs 13, 14 and 29 |

## Block E · Modern physics (plan.md PART 23–28)

| # | chapter | plan PART | why here |
|--:|---|:-:|---|
| 25 | [Photoelectric effect & matter waves](../../photoelectric-effect/Photoelectric-effect.md) | 23 | light as quanta; de Broglie |
| 26 | [Atomic structure](../../atomic-structure/Atomic-structure.md) | 24 | Rutherford, Bohr, spectra — quantisation applied to the atom |
| 27 | [X-rays](../../x-rays/X-rays.md) | 25 | Moseley, Bragg, Compton — the photon picture tested at high energy |
| 28 | [Nuclear physics](../../nuclear-physics/Nuclear-physics.md) | 26 | binding energy, radioactivity, fission and fusion |
| 29 | [Semiconductors](../../semiconductors/Semiconductors.md) | 27 | band picture, diodes, transistors, logic gates |
| 30 | [Communication systems](../../communication-systems/Communication-systems.md) | appendix | JEE-Main depth only; modulation, bandwidth, propagation |
| 31 | [Special relativity](../../special-relativity/Special-relativity.md) | 28 | the Olympiad capstone: Lorentz transformations, $E=mc^2$, relativistic dynamics |

## Live view (Dataview)

Sorted by the frontmatter `order:`; a chapter appears here the moment its file carries the property.

```dataview
TABLE WITHOUT ID
  order AS "#",
  link(file.path, title) AS "Chapter",
  block AS "Block",
  part AS "plan PART",
  status AS "Status"
FROM -"_obsidian" AND -"_templates" AND -"docs"
WHERE order
SORT order ASC
```

> [!note] Why this order and not the "wave spine"
> The nine oldest note-sets were written waves-first (string → sound → EM → thermo → heat →
> capacitors → current → geometrical → wave optics), which is why their `part:` numbers run 1–9.
> That was the order of *writing*, not of teaching. Their `order:` now places them where a course
> puts them; the `part:` numbers are left untouched because the figure labels (`F5.1` …) and the
> local gates depend on them.
