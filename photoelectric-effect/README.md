# Photons, Photoelectric Effect & Matter Waves — first principles to Olympiad

> [!note] Part 23 of [plan.md](../plan.md) · text-only Markdown chapter · written for Obsidian reading mode

**Scope.** The quantum of light and the wave of matter: the blackbody crisis, the five photoelectric
facts each paired with its classical failure, the photon bookkeeping ($E=hf$, $p=\frac{h}{\lambda}$,
intensity as flux, beam force), Einstein's equation and the $V_s$-$f$ measurement of $h$, de Broglie's
hypothesis with the accelerated-electron wavelength, the standing-wave bridge to Bohr, the
uncertainty principle derived from wave packets and used to predict $a_0$ and $-13.6$ eV,
Davisson-Germer, and the instruments (electron microscope, LEED, photomultiplier, photovoltaic
threshold, laser in one page).

**Prerequisites.** PART 15's potential language is useful but not assumed; the shipped
`electromagnetic-waves/` note owns radiation pressure as field theory (cited, not re-derived);
`heat/` and `thermodynamics/` own Stefan's law.

**The one idea.** Light delivers its energy in indivisible quanta, and matter waves are the same
fact seen from the other side.

**Contents.** Part 0 orientation and coverage map; 1 intuition; 2 definitions; 3 core derivations
(§3.1-3.12); 4 results and validity ledger with concept checks; 5 exemplars E1-E12; 6 sixteen
archetypes and Q1-Q28; 7 toolkit; 8 ten traps; 9 playbook; 10 Olympiad block OL1-OL12 with the
classical waiting time, phase/group velocity, hydrogen-from-uncertainty, linewidth, eye threshold,
laser Boltzmann obstruction, two-photon emission, relativistic wavelength correction; 11 the
36-question 200-mark paper; 12 marking and audit; 13 formula sheet; 14 checkpoint and hand-off.

**Coverage (Cengage floor).** *Cengage Optics and Modern Physics* ch 3 Photoelectric Effect,
pp. 3.1-3.41; every heading of the chapter's contents page (quantum theory of light, photon
counts, intensity, flux, density, beam force, radiation pressure, matter waves, electron emission,
photoelectric cell, photoelectric effect, Einstein equation, laws, classical failure, solved
examples, exercise bands) has a row in the block-0 coverage map.

**Olympiad layer.** Three first-principles derivations (group/phase velocity, hydrogen from
uncertainty by two routes, natural linewidth), four order-of-magnitude estimates (waiting time,
eye threshold, levitation power, quantum-gas criterion), two measurement reconstructions (the
eye's sensitivity, the laser inversion requirement), and an explicit limits-and-failure section.

**Beyond the plan.** Mirrored in `topics.json` `beyond_plan`: blackbody opening in core theory;
uncertainty-derived hydrogen in core theory; phase/group velocity structure; two-photon and laser
Boltzmann problems; thermal de Broglie quantum-gas criterion; eye-sensitivity reconstruction.

**Hand-off.** PART 24 inherits the standing-wave condition (§3.8) and the uncertainty estimate
(§3.9) and adds the Coulomb force; PART 25 inherits $E=hf$ and $p=\frac{h}{\lambda}$ for X-rays and
Compton, and the diffraction logic for Bragg. Deliberately skipped: interpretation-level quantum
mechanics, band structure (PART 27), relativistic mirrors and pair production (PARTS 25, 28).

**Media.** All figures are described briefs (`> [!abstract] DIAGRAM D23.k`, sixteen of them) with
a `*Search:*` line; no image files by design.

**Gate.** `python3 tools/check.py` → ALL GOOD: 15 blocks · C×14 E×12 Q×28 OL×12 · paper 36 Q /
200 marks · 16 DIAGRAM briefs · 49 callouts · no images.
