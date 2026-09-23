# Semiconductors & Electronic Devices — first principles to Olympiad

> [!note] Part 27 of [plan.md](../plan.md) · text-only Markdown chapter · written for Obsidian reading mode

**Scope.** Bands and doping as the two ideas behind all of electronics: the thirty-order
resistivity axis and the temperature-coefficient mechanism table; the filled-band argument;
intrinsic carriers and the $T^{3/2}e^{-E_g/2kT}$ law; donors and acceptors with the scaled-Bohr
binding estimate; the mass-action law and neutrality; conductivity, drift and diffusion; the
junction derived from diffusion to depletion to equilibrium; the diode equation with the 60
mV-per-decade rule; rectifiers and ripple; Zener regulation; LEDs, photodiodes and solar cells;
the bipolar transistor with active/saturation modes, the load line and switch design; logic
gates, De Morgan's laws, universality and the half adder; integration and the tunnelling wall
of Moore's law.

**Prerequisites.** `current-electricity/` (resistivity, drift), `capacitors/` (junction
capacitance, ripple, switching energy), PART 23 (photon energy, de Broglie and uncertainty for
the Moore's-law wall), PART 24 (the hydrogen atom the donor estimate rescales). PART 18 (Hall
Effect, to be shipped) is previewed in OL6.

**The one idea.** Bands and doping turn a poor conductor into a controllable one — the whole of
electronics in two ideas.

**Contents.** Part 0 orientation and syllabus coverage map; 1 intuition; 2 definitions and
bookkeeping; 3 core derivations (§3.1-3.13); 4 results ledger and concept checks C1-C14; 5
exemplars E1-E12; 6 sixteen archetypes and Q1-Q28; 7 toolkit; 8 ten traps; 9 playbook; 10
Olympiad block OL1-OL12 (donor binding from the scaled Bohr atom with the honest factor-1.7,
the diode equation from the Boltzmann factor, the junction capacitance's inverse-square-root
law, the Shockley-Queisser bound, the bandgap reference, the Hall measurement, the tunnelling
wall of Moore's law, shot noise, the LED series-resistor argument, the shaded panel with bypass
diodes, chip switching power, and the temperature at which doping is forgotten); 11 the
36-question 200-mark paper; 12 marking; 13 cross-links; 14 sources and review checklist.

**Coverage (syllabus floor).** No semiconductor chapter exists in the supplied Cengage volumes
(verified: *Optics and Modern Physics* Unit II holds only chs 3-5; the other volumes checked
per plan.md §1.13), so the block-0 coverage map is keyed to the JEE Main/Advanced syllabus
headings: classification, energy bands, intrinsic and extrinsic conduction, p-n junction,
junction diode, rectifiers, Zener/LED/photodiode/solar cell, transistor and circuits, logic
gates, integrated circuits — every heading has a row, with the olympiad extras flagged as added
by sweep.

**Olympiad layer.** One cross-topic derivation (scaled Bohr donor), one statistical derivation
(diode law from Boltzmann), one synthesis (junction capacitance from Poisson), four estimates
(Solar bound, Moore's wall, chip power, doping-forgetting temperature), two measurement
reconstructions (Hall density and type, bandgap thermometry), and an explicit limits-and-failure
section naming valley anisotropy, ideality factors and the Shockley-Queisser assumptions.

**Beyond the plan.** Mirrored in `topics.json` `beyond_plan`: donor binding-energy derivation
with honest error discussion; diode equation from the Boltzmann factor; junction capacitance
$V^{-1/2}$ law; Shockley-Queisser bound; bandgap reference construction; Hall measurement on a
real sample; Moore's-law tunnelling limit from de Broglie/uncertainty; shot-noise receiver
design; bypass-diode panel analysis; switching-power estimate; the doping-forgetting
temperature.

**Hand-off.** P7 (communication systems) inherits the diode as detector/mixer and the
transistor as amplifier. Deliberately skipped: op-amps, FET internals, biasing networks beyond
the load line, AC small-signal models beyond gain, crystal-structure and phonon physics beyond
device needs.

**Media.** All figures are described briefs (`> [!abstract] DIAGRAM D27.k`, eighteen of them)
with a `*Search:*` line; no image files by design.

**Gate.** `python3 tools/check.py` → ALL GOOD: 15 blocks · C×14 E×12 Q×28 OL×12 · paper 36 Q /
200 marks · 18 DIAGRAM briefs · 42 callouts · no images.
