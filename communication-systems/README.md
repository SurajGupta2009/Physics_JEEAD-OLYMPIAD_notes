# Communication Systems — first principles to Olympiad

> [!note] P7 of PENDING.md · text-only Markdown chapter · written for Obsidian reading mode
> **Note:** This topic was marked as "dropped (JEE-Main-only)" in PENDING.md and plan.md Appendix B.
> It is being written as a standalone supplement at the user's request. It has no plan.md PART number.

**Scope.** Amplitude modulation (AM) and frequency modulation (FM): the need for modulation, the modulation index, bandwidth of AM signals, sidebands, AM and FM transmitter block diagrams, demodulation (detection), signal-to-noise and bandwidth trade-offs, the electromagnetic propagation modes (ground wave, sky wave, space wave, line of sight), the antenna basics, the communication channel model, and an introduction to digital communication (sampling, quantisation, PCM). JEE Main level throughout; the Olympiad layer extends to Shannon's channel capacity, the Friis transmission formula, and the link budget.

**Prerequisites.** `electromagnetic-waves/` (Maxwell's equations, the EM spectrum, wave speed $c=f\lambda$), `current-electricity/` (basic circuit ideas), `capacitors/` (RC filter behaviour for demodulation), PART 22 (AC circuits, resonance, rectifiers — the bridge from which this chapter inherits its filter language).

**The one idea.** A message cannot ride a carrier unless the carrier's amplitude, frequency or phase is steered by the message — modulation is the steering, and every system in communication is a chain of modulation, transmission and demodulation fighting noise at every step.

**Contents.** Part 0 orientation; 1 intuition; 2 definitions; 3 core derivations (§3.1–3.12); 4 results ledger; 5 exemplars E1–E10; 6 archetypes and Q1–Q25; 7 toolkit; 8 traps; 9 playbook; 10 Olympiad block OL1–OL10; 11 paper; 12 marking; 13 formula sheet; 14 checkpoint.

**Coverage (JEE Main floor).** No Cengage communication chapter exists in the supplied volumes (verified). The coverage map is built from the standard JEE Main syllabus headings for Communication Systems: need for modulation, bandwidth of signals, bandwidth of transmission medium, propagation of EM waves (ground/sky/space), modulation index, AM and FM waveforms, detection/demodulation, and basic block diagrams.

**Olympiad layer.** Shannon's channel capacity theorem, the Friis transmission formula, link-budget arithmetic, the noise figure, the FM capture effect, the signal-to-noise improvement of FM over AM, information content and entropy (introduction), and the deep-space communication estimate.

**Beyond the plan.** Mirrored in `topics.json` `beyond_plan`: Shannon's theorem and link-budget arithmetic; the Friis formula; the FM capture effect; the entropy/information-content introduction.

**Hand-off.** Deliberately skipped: advanced digital modulation (QAM, spread-spectrum, OFDM), error-correcting codes, information theory beyond Shannon's theorem, radar and lidar, fibre-optic communication, and networking protocols.

**Media.** All figures are described briefs (`> [!abstract] DIAGRAM D100.k`) with a `*Search:*` line; no image files by design. The `part: 100` is a placeholder since this topic is outside the 28-part plan.

**Gate.** `python3 tools/check.py` → ALL GOOD.
