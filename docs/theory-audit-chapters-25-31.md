# Theory-only audit: chapters 25–31

**Date:** 2026-09-29  
**Scope:** theory/derivation spine only; excludes problem solutions, question banks, and diagrams. This is a targeted review, not a line-by-line certification of all seven long chapters.

## Bottom line and order

The remaining course slots are **Photoelectric effect & matter waves (25), Atomic structure (26), X-rays (27), Nuclear physics (28), Semiconductors (29), Communication systems (30), and Special relativity (31)**. The order mostly follows the modern-physics dependency chain: photons and matter waves → atomic energy levels → X-ray transitions/diffraction and Compton scattering → nuclear structure/reactions → semiconductor devices. Communication systems is a self-contained JEE-Main-depth appendix, while special relativity supplies the relativistic framework used by photon momentum, Compton scattering, and reaction thresholds.

Four theory passages were corrected during this audit: (1) pair-production threshold now includes nuclear recoil (and identifies the common heavy-nucleus approximation); (2) nuclear decay-rate invariance is qualified for electron capture and extreme ionisation; (3) reactor safety no longer implies all excursions are self-limiting; and (4) communication-system noise and radio-horizon formulas now state their practical assumptions more carefully.

## Findings by chapter

### Chapter 25 — Photoelectric effect & matter waves

The progression from the classical crisis and experimental signatures to photon bookkeeping, Einstein’s equation/stopping potential, de Broglie waves, and diffraction is coherent. The distinction between intensity (photon rate) and frequency (energy per photon) is especially useful. Sampled equations are consistent under their stated single-photon and nonrelativistic assumptions.

- The classical waiting-time calculation is a deliberately simplified scale estimate: its atomic interception area and energy-collection model are not a detailed microscopic theory. The text frames it as an illustrative challenge to the classical picture.
- De Broglie wavelength from an accelerating voltage uses nonrelativistic kinetic energy; at sufficiently high voltage, use relativistic momentum.

### Chapter 26 — Atomic structure

The historical and conceptual sequence—Rutherford scattering, the failure of classical atomic stability, Bohr quantisation, hydrogenic levels and spectra, then model limits/extensions—is sensible. Sampled Rutherford and Bohr derivations were internally consistent.

- The Bohr hydrogenic formulas assume a Coulomb centre and the elementary model’s approximations (including effectively fixed nuclear mass unless reduced mass is specified). They are not a general many-electron atomic theory.
- The interpretation of discrete photon absorption applies to bound–bound transitions; ionisation permits a continuum of excess kinetic energies, as the notes distinguish.

### Chapter 27 — X-rays

The chapter connects tube production and the Duane–Hunt cutoff to characteristic lines/Moseley scaling, attenuation, Bragg diffraction, and Compton scattering in a clear order. Sampled Bragg geometry, attenuation law, NaCl unit-cell count, and Compton shift were consistent with their stated models.

- The screened-Bohr derivation of Moseley’s law is an approximation; actual characteristic spectra require more detailed electronic structure and screening constants.
- The exponential attenuation coefficient depends on photon energy and material; the rough power-law scaling quoted away from absorption edges is not universal.

### Chapter 28 — Nuclear physics

The sequence from nuclear size and binding energy through reaction bookkeeping, decay, chains/dating, fission, fusion, and detection is appropriate. The constant-hazard assumption is clearly connected to exponential decay.

- **Corrected decay-rate qualification:** ordinary environmental changes have negligible effect on most decay modes, but electron-capture rates depend on electron density at the nucleus and can change with ionisation/chemical environment; extreme ionisation can alter other channels. The notes now state the usual constant-$\lambda$ JEE model as an approximation under ordinary conditions.
- **Corrected reactor-safety wording:** a power reactor cannot undergo a nuclear-weapon-style detonation, but accidents and destructive power excursions are possible; steam/hydrogen explosions and decay-heat hazards are distinct from nuclear detonation. The notes now avoid asserting that every excursion automatically shuts itself down.
- The detailed fission-energy partition, reactor feedback, and fusion-rate estimates are model-dependent and were not independently reconstructed here.

### Chapter 29 — Semiconductors

The conceptual order from bands and carrier populations to doping, transport, junctions, diode behaviour, rectification, optoelectronics, transistors, and logic is sound. The sampled intrinsic-carrier, mass-action, conductivity, and ideal-diode relationships were internally consistent.

- The intrinsic-carrier temperature law is an approximation with temperature-dependent band gap/effective density of states simplified; the ideal diode equation omits nonideal recombination, series resistance, and high-injection effects.
- The built-in potential is not itself a terminal voltage available from an isolated equilibrium junction; the notes’ later circuit treatment should preserve that distinction.

### Chapter 30 — Communication systems

The progression from signal/channel bandwidth and propagation to modulation, demodulation, and noise/capacity is appropriate for an introductory communication-systems appendix. AM sideband and single-tone power relations and Carson’s FM bandwidth estimate were consistent in the sampled sections.

- **Corrected horizon qualification:** $\sqrt{2Rh}$ is the geometric horizon for one antenna at height $h\ll R$. The text now gives the two-antenna range as approximately $\sqrt{2Rh_t}+\sqrt{2Rh_r}$ and distinguishes geometric horizon from atmospheric refraction and terrain.
- **Corrected noise interpretation:** $kTB$ is available thermal-noise power for the ideal matched case; it is a practical noise scale, not an absolute signal-detection floor. Receiver noise figure, required SNR, processing, and interference matter.
- Carson’s rule is an effective occupied-bandwidth estimate, not a strict finite spectral cutoff; FM has infinitely many sidebands in the ideal single-tone model.

### Chapter 31 — Special relativity

The order from postulates and simultaneity to Lorentz transformations, time/length effects, velocity addition, momentum/energy, Doppler shift, and applications is strong. Sampled transformations, energy–momentum relation, and relativistic Doppler formulas were consistent.

- **Corrected pair-production threshold:** $2m_ec^2=1.022$ MeV is the heavy-nucleus approximation, not the exact laboratory threshold for a stationary recoil partner. For a stationary nucleus of mass $M$, exact energy–momentum conservation gives $E_{\gamma,\mathrm{th}}=2m_ec^2(1+m_e/M)$. The chapter’s text, exemplar, question, and formula map now distinguish these cases.
- The GPS clock correction combines special and general relativity; the GR contribution is an application-level result, not derived by special relativity alone.
- **Scope/validity:** advanced relativistic collision derivations and all worked solutions were not re-solved line by line.

## Validation and remaining limits

The seven chapter-specific structural checks passed after the edits. These checks validate document structure, not physics correctness.

1. The review covers theory exposition and selected representative derivations; it does not certify every equation or numerical example in these chapters.
2. Problem solutions and diagrams were not reviewed, in keeping with the standing scope.
3. Full JEE syllabus and experimental-skills coverage remain separate audit tasks; the existing syllabus review calls for an item-by-item, source-linked check.
