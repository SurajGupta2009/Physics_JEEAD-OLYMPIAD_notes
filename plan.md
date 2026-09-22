# MASTER MULTI-AGENT EXECUTION PLAN: WAVES, EM WAVES & OPTICS CURRICULUM
> **Repository**: `Physics_JEEAD-OLYMPIAD_notes`  
> **Target Audience**: JEE Advanced, NSEP, INPhO, IPhO aspirants  
> **Standard**: 100% Cengage-complete floor + Olympiad depth + Proof-first rigor  
> **Format**: Self-contained Markdown (`.md`) with clean standard MathJax/KaTeX syntax (`$...$`, `$$...$$`), collapsible `<details>` solutions, and standalone local SVGs under `assets/figures/`.
---
## 0. Architecture & Non-Negotiable Contracts
Every agent working on this repository **MUST** adhere to the repository architecture defined in `STRUCTURE.md` and `CONTRIBUTING.md`:
1. **Folder Autonomy**:
   - Every topic lives in its own kebab-case directory (e.g. `string-waves/`, `sound-waves/`, `electromagnetic-waves/`).
   - Every topic directory must be self-contained:
     ```
     <topic-slug>/
     ├── <Topic-Slug>.md           # Master portable Markdown edition
     ├── README.md                 # Topic roadmap, status, prerequisite graph
     ├── assets/
     │   └── figures/              # Standalone local SVGs (fig-001.svg, ...)
     └── ...
     ```
2. **Quality & Completeness Rules**:
   - **No external links** for images or fonts. All diagrams must be local SVGs referenced as `assets/figures/fig-XXX.svg`.
   - **No hand-waving**: Every formula must be derived from foundational laws (Newton's laws, Maxwell's equations, wave continuity).
   - **Explicit condition of validity**: Every boxed formula must state its boundary domain (e.g. valid for small amplitudes $A \ll \lambda$, paraxial limit, linear lossless medium).
   - **No verbatim copying**: Cover 100% of the Cengage concepts, derivations, and question archetypes, but write original explanations, diagrams, and problem variations.
3. **The 8-Part Didactic Progression** (Required for every `<Topic-Slug>.md`):
   - **Section 1: Foundations & Physical Motivation**: Intuition, definitions, state variables, frame definitions.
   - **Section 2: Core Derivations & Asymptotic Limits**: Rigorous proofs with boundary and dimensional checks ($x \to 0$, $x \to \infty$, symmetry checks).
   - **Section 3: Interleaved Exemplars & Concept Checks**: Conceptual problems with collapsible `<details><summary>Solution</summary>...</details>` blocks.
   - **Section 4: [JEE Advanced Advantage / Alternate Method]**: Center-of-mass frames, phasor calculus, impedance methods, symmetry/superposition shortcuts.
   - **Section 5: Examiner Traps (`.trap`)**: Common sign errors, phase inversion traps, boundary condition slips, Doppler sign errors.
   - **Section 6: Topic Playbook**: Triage decision-tree, formula maps, numbers/constants to memorise for high-speed estimation.
   - **Section 7: Olympiad-Grade Paper**: Full 30+ question examination paper (Single-Correct, Multi-Correct, Numerical, Comprehensive Olympiad Long-Form) with full solutions and grading rubrics.
   - **Section 8: Printable Formula Sheet**: High-density reference summary with conditions of validity.
---
## 1. Topic Breakdown & Agent Assignments
The curriculum for Waves, EM Waves, and Wave Optics is divided into 4 modular work packages:
| Work Package | Topic Directory | Primary Markdown Deliverable | Scope / Cengage Floor |
|---|---|---|---|
| **PART 1** | `string-waves/` | `String-waves.md` | Mechanical waves, 1D wave equation, tension & wave speed, energy/power transmission, boundary reflections, standing waves & harmonics. |
| **PART 2** | `sound-waves/` | `Sound-waves.md` | Longitudinal pressure waves, speed of sound (Laplace), decibels/intensity, organ pipes & end-correction, beats, resonance, complete Doppler effect. |
| **PART 3** | `electromagnetic-waves/` | `Electromagnetic-waves.md` | Displacement current, Maxwell's equations, EM wave equations in vacuum/matter, Poynting vector, radiation pressure, EM spectrum. |
| **PART 4** | `wave-optics/` | `Wave-optics.md` | Wavefronts, Huygens' principle, interference, YDSE in all cases, thin films, biprism, Lloyd's mirror, diffraction, polarisation, coherence. |
---
## 2. Detailed Work Package Directives
### PART 1: String Waves (Transverse Mechanical Waves)
**Target Directory**: `string-waves/`  
**Master Deliverable**: `string-waves/String-waves.md`  
**Agent Role**: Agent 1 (or prompt: *"Execute PART 1 of plan.md: String Waves"*)
#### Required Coverage (The Cengage Floor + Olympiad Bridge):
1. **Kinematics & Wave Dynamics**:
   - Definition of wave: disturbance propagation vs matter transport.
   - 1D differential wave equation: derivation from Newton's second law on a curved string element of mass $dm = \mu \, dx$:
     $$\frac{\partial^2 y}{\partial t^2} = \frac{T}{\mu} \frac{\partial^2 y}{\partial x^2} \implies v = \sqrt{\frac{T}{\mu}}$$
   - Verification of general solutions: $y(x,t) = f(x \mp vt)$ and d'Alembert's formulation.
   - Harmonic traveling waves: $y(x,t) = A \sin(kx - \omega t + \phi)$. Wave vector $k = 2\pi/\lambda$, angular frequency $\omega = 2\pi f$, velocity $v = \omega/k$.
2. **Particle Velocity vs. Wave Velocity**:
   - Derivation of transverse particle velocity: $v_p = \frac{\partial y}{\partial t} = -v \frac{\partial y}{\partial x} = -v \times (\text{slope})$.
   - Transverse acceleration: $a_p = \frac{\partial^2 y}{\partial t^2} = -\omega^2 y$.
   - Direction rules and wave profiles: mapping $v_p$ direction from the spatial curve $y(x)$.
3. **Energy, Power & Intensity**:
   - Kinetic energy density $u_k = \frac{1}{2}\mu \left(\frac{\partial y}{\partial t}\right)^2$ and Potential energy density $u_p = \frac{1}{2}T \left(\frac{\partial y}{\partial x}\right)^2$.
   - Proof that $u_k = u_p$ at every point in a traveling wave, total energy density $u = \mu \omega^2 A^2 \cos^2(kx - \omega t)$.
   - Instantaneous power transmission: $P(x,t) = -T \left(\frac{\partial y}{\partial x}\right)\left(\frac{\partial y}{\partial t}\right)$.
   - Average power: $\langle P \rangle = \frac{1}{2}\mu \omega^2 A^2 v$.
4. **Boundary Reflections & Impedance Matching**:
   - Rigid boundary (fixed end): zero displacement condition $\to$ reflected pulse inverted ($\Delta \phi = \pi$).
   - Free boundary (massless frictionless ring): zero transverse force condition $\frac{\partial y}{\partial x} = 0 \to$ reflected pulse in phase ($\Delta \phi = 0$).
   - Junction of two strings with different linear mass densities $\mu_1, \mu_2$:
     $$A_r = \frac{v_2 - v_1}{v_2 + v_1} A_i = \frac{\sqrt{\mu_1} - \sqrt{\mu_2}}{\sqrt{\mu_1} + \sqrt{\mu_2}} A_i, \quad A_t = \frac{2v_2}{v_1 + v_2} A_i = \frac{2\sqrt{\mu_1}}{\sqrt{\mu_1} + \sqrt{\mu_2}} A_i$$
   - Verification of energy conservation at junctions: $\langle P_i \rangle = \langle P_r \rangle + \langle P_t \rangle$.
5. **Superposition & Standing Waves**:
   - Mathematical derivation of standing wave equation: $y = 2A \sin(kx) \cos(\omega t)$.
   - Nodes and antinodes: spacing, zero energy transmission across nodes.
   - Energy distribution in standing waves: periodic interchange between purely kinetic and purely potential energy.
   - Normal modes of a string fixed at both ends: $\lambda_n = \frac{2L}{n}$, $f_n = n \frac{v}{2L} = \frac{n}{2L}\sqrt{\frac{T}{\mu}}$ ($n = 1, 2, 3, \dots$).
   - String fixed at one end and free at the other: $\lambda_n = \frac{4L}{2n-1}$, $f_n = (2n-1)\frac{v}{4L}$.
   - Laws of transverse vibrations of a string (Sonometer): Law of length, Law of tension, Law of mass.
   - Melde's experiment: transverse and longitudinal arrangements and resonance condition.
6. **Olympiad Extensions**:
   - Wave propagation in a hanging heavy rope ($v(y) = \sqrt{gy}$), time for pulse to travel from bottom to top: $t = 2\sqrt{L/g}$.
   - Non-uniform mass density: WKB approximation for wave amplitude scaling $A(x) \propto \mu(x)^{-1/4}$.
   - Phasor method for superposition of multiple harmonic waves with arbitrary phase differences.
---
### PART 2: Sound Waves & Doppler Effect
**Target Directory**: `sound-waves/`  
**Master Deliverable**: `sound-waves/Sound-waves.md`  
**Agent Role**: Agent 2 (or prompt: *"Execute PART 2 of plan.md: Sound Waves"*)
#### Required Coverage (The Cengage Floor + Olympiad Bridge):
1. **Nature of Longitudinal Acoustic Waves**:
   - Longitudinal displacement wave $s(x,t) = s_0 \sin(kx - \omega t)$.
   - Relation between displacement and volumetric strain: $\frac{\Delta V}{V} = \frac{\partial s}{\partial x}$.
   - Excess pressure wave (acoustic pressure):
     $$\Delta P(x,t) = -B \frac{\partial s}{\partial x} = \Delta P_0 \cos(kx - \omega t), \quad \text{where } \Delta P_0 = B k s_0 = \rho v \omega s_0$$
   - Phase relationship: Pressure wave leads/lags displacement wave by $90^\circ$ ($\pi/2$ phase shift). Where displacement is zero, pressure variation is maximum (compression/rarefaction).
   - Density variations: $\Delta \rho = -\rho_0 \frac{\partial s}{\partial x} = \frac{\rho_0}{B}\Delta P$.
2. **Speed of Sound in Gases, Liquids, and Solids**:
   - General wave speed in elastic media: $v = \sqrt{B/\rho}$ (fluids) and $v = \sqrt{Y/\rho}$ (thin solid rods).
   - Newton's isothermal assumption: $P V = \text{const} \implies B_T = P \implies v = \sqrt{P/\rho}$ (leads to error in air: $\approx 280\text{ m/s}$).
   - Laplace's adiabatic correction: Sound oscillations are rapid with no thermal exchange ($P V^\gamma = \text{const} \implies B_S = \gamma P$):
     $$v = \sqrt{\frac{\gamma P}{\rho}} = \sqrt{\frac{\gamma R T}{M}}$$
   - Factors affecting speed of sound: temperature ($v \propto \sqrt{T}$), molar mass $M$, humidity (moist air has lower effective $M \implies$ higher speed), pressure independence at constant temperature.
3. **Sound Intensity & Human Auditory Response**:
   - Acoustic intensity: $I = \frac{\Delta P_0^2}{2\rho v} = \frac{1}{2}\rho v \omega^2 s_0^2$.
   - Loudness and sound level: Decibel scale $\beta = 10 \log_{10}\left(\frac{I}{I_0}\right)$ with reference threshold $I_0 = 10^{-12}\text{ W/m}^2$.
   - Geometric attenuation: Point source (inverse square law $I \propto 1/r^2 \implies \Delta P_0 \propto 1/r$), line source ($I \propto 1/r \implies \Delta P_0 \propto 1/\sqrt{r}$).
4. **Standing Sound Waves & Resonance in Columns**:
   - Boundary conditions for sound:
     - Closed end: Rigid wall $\implies$ Displacement node ($s = 0$), Pressure antinode ($\Delta P = \pm \Delta P_0$).
     - Open end: Contact with ambient atmosphere $\implies$ Pressure node ($\Delta P = 0$), Displacement antinode.
   - Closed organ pipe (one end closed): $L = (2n-1)\frac{\lambda}{4} \implies f_n = (2n-1)\frac{v}{4L}$ ($n = 1, 2, 3, \dots$). Only odd harmonics present.
   - Open organ pipe (both ends open): $L = n \frac{\lambda}{2} \implies f_n = n \frac{v}{2L}$ ($n = 1, 2, 3, \dots$). All harmonics present.
   - End-Correction (Rayleigh's correction): $e \approx 0.6 r$ (for open end), effective length $L_{\text{eff}} = L + e$ (closed pipe) and $L_{\text{eff}} = L + 2e$ (open pipe).
   - Resonance tube experiment: Determination of $v$ and end correction $e$ via consecutive resonance lengths $l_1, l_2$:
     $$v = 2f(l_2 - l_1), \quad e = \frac{l_2 - 3l_1}{2}$$
   - Kundt's tube experiment: Acoustic standing waves in gas/rods, measurement of wavelength and sound speed ratio.
5. **Interference & Beats**:
   - Superposition of acoustic waves: path difference $\Delta x$, phase difference $\Delta \phi = \frac{2\pi}{\lambda}\Delta x$.
   - Quincke's tube: Acoustic interferometer, destructive condition $(2n+1)\lambda/2$.
   - Beats phenomenon: Superposition of two frequencies $f_1, f_2$:
     $$s(t) = 2s_0 \cos\left(2\pi \frac{f_1 - f_2}{2} t\right) \sin\left(2\pi \frac{f_1 + f_2}{2} t\right) \implies f_{\text{beat}} = |f_1 - f_2|$$
   - Tuning fork adjustments: Loading with wax (decreases frequency), filing prongs (increases frequency).
6. **Comprehensive Doppler Effect**:
   - Master reference-frame derivation for sound in a medium with wind velocity $w$:
     $$f' = f \left(\frac{(v \pm w) \pm v_o}{(v \pm w) \mp v_s}\right)$$
   - Physical distinction: Moving source compresses wavefronts in the medium ($\lambda' = \frac{v \mp v_s}{f}$); moving observer intercepts wavefronts at a different relative speed ($v_{\text{rel}} = v \pm v_o$).
   - Oblique / 2D Doppler effect: Line-of-sight velocity projections:
     $$f' = f \left(\frac{v - v_o \cos\theta_o}{v - v_s \cos\theta_s}\right)$$
   - Accelerated sources and observers: Frequency variation vs. time during closest approach.
   - Acoustic echo/reflection from a moving wall or vehicle (double Doppler shift).
   - Supersonic speeds, Shock waves, Mach number $M = v_s/v$, and Mach cone angle $\sin\alpha = v/v_s = 1/M$.
---
### PART 3: Electromagnetic Waves
**Target Directory**: `electromagnetic-waves/`  
**Master Deliverable**: `electromagnetic-waves/Electromagnetic-waves.md`  
**Agent Role**: Agent 3 (or prompt: *"Execute PART 3 of plan.md: Electromagnetic Waves"*)
#### Required Coverage (The Cengage Floor + Olympiad Bridge):
1. **Maxwell's Equations & Displacement Current**:
   - Inconsistency of Ampère's circuital law $\oint \vec B \cdot d\vec l = \mu_0 I_{\text{encl}}$ for a charging capacitor: surface bounded by loop passing between capacitor plates.
   - Displacement current definition: $I_d = \varepsilon_0 \frac{d\Phi_E}{dt}$.
   - Maxwell–Ampère law: $\oint \vec B \cdot d\vec l = \mu_0 \left(I_c + \varepsilon_0 \frac{d\Phi_E}{dt}\right)$.
   - Continuity of current: $I_c = I_d$ during charging/discharging.
   - Summary of Maxwell's 4 equations in vacuum and in linear matter (integral and differential forms):
     - Gauss's Law for Electricity: $\nabla \cdot \vec E = \frac{\rho}{\varepsilon_0}$
     - Gauss's Law for Magnetism: $\nabla \cdot \vec B = 0$
     - Faraday's Law of Induction: $\nabla \times \vec E = -\frac{\partial \vec B}{\partial t}$
     - Maxwell–Ampère Law: $\nabla \times \vec B = \mu_0 \vec J + \mu_0 \varepsilon_0 \frac{\partial \vec E}{\partial t}$
2. **Derivation of the Electromagnetic Wave Equation**:
   - Using vector identity $\nabla \times (\nabla \times \vec E) = \nabla(\nabla \cdot \vec E) - \nabla^2 \vec E$ in charge-free and current-free space ($\rho = 0, \vec J = 0$):
     $$\nabla^2 \vec E = \mu_0 \varepsilon_0 \frac{\partial^2 \vec E}{\partial t^2}, \quad \nabla^2 \vec B = \mu_0 \varepsilon_0 \frac{\partial^2 \vec B}{\partial t^2}$$
   - Speed of light: $c = \frac{1}{\sqrt{\mu_0 \varepsilon_0}} \approx 2.998 \times 10^8\text{ m/s}$.
   - Speed in a dielectric medium: $v = \frac{1}{\sqrt{\mu \varepsilon}} = \frac{c}{\sqrt{\mu_r \varepsilon_r}} = \frac{c}{n}$.
3. **Properties of Plane Harmonic EM Waves**:
   - Transverse nature proof: $\vec E \perp \hat k$, $\vec B \perp \hat k$, and $\vec E \perp \vec B$.
   - Phase alignment: $\vec E$ and $\vec B$ oscillate in phase in free space.
   - Mathematical expressions for waves traveling along $+z$:
     $$\vec E(z,t) = E_0 \sin(kz - \omega t) \hat i, \quad \vec B(z,t) = B_0 \sin(kz - \omega t) \hat j$$
   - Fundamental amplitude relation: $E_0 = c B_0$ (derived from Faraday's law).
4. **Energy, Poynting Vector & Momentum**:
   - Electric energy density $u_E = \frac{1}{2}\varepsilon_0 E^2$ and Magnetic energy density $u_B = \frac{B^2}{2\mu_0}$.
   - Equipartition proof: $u_E = u_B \implies$ Total energy density $u = \varepsilon_0 E^2 = \frac{B^2}{\mu_0}$.
   - Poynting vector: Direction and rate of energy flow per unit area:
     $$\vec S = \frac{1}{\mu_0} (\vec E \times \vec B)$$
   - Average intensity: $\langle S \rangle = I = \frac{1}{2}\varepsilon_0 c E_0^2 = \frac{E_0 B_0}{2\mu_0} = \frac{c B_0^2}{2\mu_0}$.
   - Momentum of an EM wave: $p = \frac{U}{c}$.
5. **Radiation Pressure**:
   - Normal incidence:
     - Complete absorption (black surface): Radiation pressure $P = \frac{I}{c}$.
     - Complete reflection (perfect mirror): Momentum change is doubled $\implies P = \frac{2I}{c}$.
     - Reflection coefficient $R$: $P = (1 + R)\frac{I}{c}$.
   - Oblique incidence at angle $\theta$ to the normal:
     - Absorption: $P = \frac{I}{c}\cos^2\theta$.
     - Reflection: $P = \frac{2I}{c}\cos^2\theta$.
   - Radiation force on spherical and curved particles (absorbing and reflecting spheres).
6. **Electromagnetic Spectrum & Applications**:
   - Complete classification table: Radio waves, Microwaves, Infrared, Visible light, Ultraviolet, X-rays, Gamma rays.
   - Exact bounds for frequency and wavelength.
   - Production mechanisms (oscillating LC circuits, magnetrons, thermal vibration, atomic transitions, deceleration of fast electrons, nuclear decay).
   - Practical & modern applications (RADAR, cellular communication, greenhouse effect, LASIK, crystallography, radiation therapy).
---
### PART 4: Wave Optics (Audit, Harmonization & Review)
**Target Directory**: `wave-optics/`  
**Master Deliverable**: `wave-optics/Wave-optics.md`  
**Agent Role**: Agent 4 (or prompt: *"Execute PART 4 of plan.md: Wave Optics Alignment"*)
#### Required Coverage (Audit & Deep Alignment with Parts 1–3):
1. **Cross-Topic Harmonization**:
   - Ensure clear pedagogical linkage: String waves $\to$ Sound waves $\to$ EM waves $\to$ Light as transverse EM wave $\to$ Wave optics.
   - Explicitly link the scalar wave equation from `string-waves/` and the vector field properties from `electromagnetic-waves/` to the optical wave model.
2. **Cengage Floor Verification (Pages 2.1–2.95)**:
   - Huygens' principle, secondary wavelets, reflection and refraction derivations.
   - Superposition of coherent light waves, intensity formula $I = I_1 + I_2 + 2\sqrt{I_1 I_2}\cos\Delta\phi$.
   - Young's Double Slit Experiment (YDSE): Complete geometry, fringe width $\beta = \frac{\lambda D}{d}$, angular fringe width $\theta = \frac{\lambda}{d}$.
   - Special YDSE configurations:
     - Slit covered with thin transparent sheet (path increase $\Delta x = (\mu - 1)t$, fringe shift $\Delta y = \frac{D}{d}(\mu - 1)t$).
     - YDSE immersed in a liquid of refractive index $\mu$ ($\lambda' = \lambda/\mu$).
     - Tilted incidence and source placed off-axis.
     - Shape of fringes on flat screen (hyperbolic sections vs straight central lines).
     - White light YDSE (central white fringe, colored fringes, dark bands for missing wavelengths).
   - Division of Amplitude & Interferometers:
     - Thin film interference (reflected and transmitted systems, Stokes' phase shift of $\pi$ upon reflection from denser medium).
     - Wedge-shaped thin films and Newton's rings.
     - Fresnel biprism and Lloyd's mirror (including central dark fringe).
3. **Olympiad & Advanced Extensions**:
   - Fraunhofer single-slit diffraction: Phasor derivation of intensity $I(\theta) = I_0 \left(\frac{\sin\beta}{\beta}\right)^2$ with $\beta = \frac{\pi a \sin\theta}{\lambda}$.
   - Circular aperture diffraction, Airy disc, and Rayleigh criterion for angular resolution $\theta_R = 1.22 \frac{\lambda}{D}$.
   - Diffraction grating: Grating equation $d\sin\theta = m\lambda$, dispersion and resolving power.
   - Polarisation: Unpolarised light, plane polarised light, Malus's law ($I = I_0 \cos^2\theta$).
   - Brewster's law ($\tan\theta_p = \mu$) and microscopic dipole explanation.
   - Double refraction in calcite/quartz, optic axis, ordinary and extraordinary rays, Quarter-wave ($\lambda/4$) and Half-wave ($\lambda/2$) retarder plates.
---
## 3. Parallel Execution Instructions for Multiple Agents
When distributing work among multiple agents, use these copy-paste prompt templates:
### Prompt for Agent 1 (Part 1):
```text
You are an elite Physics educator working on the repository Physics_JEEAD-OLYMPIAD_notes.
Execute PART 1 of plan.md: "String Waves".
Create the complete directory string-waves/ containing String-waves.md and README.md.
Follow the 8-part progression strictly: Foundations, Rigorous Derivations, In-flow Exemplars with collapsible <details> solutions, [JEE Advanced Advantage / Alternate Method] blocks, Examiner Traps, Playbook, 3-hour Olympiad Paper (30+ questions with full solutions), and Formula Sheet.
Ensure all formulas have conditions of validity and math is clean MathJax/KaTeX ($...$ / $$...$$).
Generate standalone SVG diagrams under string-waves/assets/figures/ for all key geometries.
Refer to plan.md for the complete topic syllabus and quality rules.
```
### Prompt for Agent 2 (Part 2):
```text
You are an elite Physics educator working on the repository Physics_JEEAD-OLYMPIAD_notes.
Execute PART 2 of plan.md: "Sound Waves & Doppler Effect".
Create the complete directory sound-waves/ containing Sound-waves.md and README.md.
Follow the 8-part progression strictly: Foundations, Rigorous Derivations, In-flow Exemplars with collapsible <details> solutions, [JEE Advanced Advantage / Alternate Method] blocks, Examiner Traps, Playbook, 3-hour Olympiad Paper (30+ questions with full solutions), and Formula Sheet.
Cover Laplace correction, organ pipes with end-correction, acoustic impedance, beats, and the complete 2D/moving medium Doppler effect.
Generate standalone SVG diagrams under sound-waves/assets/figures/.
Refer to plan.md for the complete topic syllabus and quality rules.
```
### Prompt for Agent 3 (Part 3):
```text
You are an elite Physics educator working on the repository Physics_JEEAD-OLYMPIAD_notes.
Execute PART 3 of plan.md: "Electromagnetic Waves".
Create the complete directory electromagnetic-waves/ containing Electromagnetic-waves.md and README.md.
Follow the 8-part progression strictly: Foundations, Rigorous Derivations, In-flow Exemplars with collapsible <details> solutions, [JEE Advanced Advantage / Alternate Method] blocks, Examiner Traps, Playbook, 3-hour Olympiad Paper (30+ questions with full solutions), and Formula Sheet.
Cover displacement current, full Maxwell curl derivations, Poynting vector, radiation pressure at normal and oblique angles, and the comprehensive EM spectrum.
Generate standalone SVG diagrams under electromagnetic-waves/assets/figures/.
Refer to plan.md for the complete topic syllabus and quality rules.
```
### Prompt for Agent 4 (Part 4 & Coordinator):
```text
You are the Lead Physics Architect for Physics_JEEAD-OLYMPIAD_notes.
Execute PART 4 of plan.md: "Wave Optics Audit & Repository Integration".
Audit wave-optics/Wave-optics.md against plan.md to ensure zero gaps in Cengage coverage (Huygens, YDSE, thin films, biprism, Lloyd's mirror, diffraction, polarisation).
Update topics.json and CURRICULUM.md to register string-waves, sound-waves, and electromagnetic-waves alongside existing note-sets.
Run the quality gate: python3 tools/check_all.py.
```
---
## 4. Final Quality Gate Protocol
Once all parts are synthesized:
1. Verify math syntax with `python3 tools/mathfix.py` in each topic directory.
2. Update the master registry `topics.json` with the exact word, question, and formula counts.
3. Verify that `CURRICULUM.md` reflects the unified progression:
   $$\text{String Waves} \longrightarrow \text{Sound Waves} \longrightarrow \text{Electromagnetic Waves} \longrightarrow \text{Geometrical Optics} \longrightarrow \text{Wave Optics}$$
4. Run the quality test: `python3 tools/check_all.py`.