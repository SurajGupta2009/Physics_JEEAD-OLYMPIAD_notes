---
title: Semiconductors & Electronic Devices
part: 27
slug: semiconductors
source: JEE Main/Advanced semiconductor syllabus (no chapter exists in the supplied Cengage volumes, verified)
aliases: [semiconductors, diodes, transistors, logic gates, p-n junction]
tags: [jee-main, jee-advanced, olympiad, modern-physics, electronics]
---

# Semiconductors & Electronic Devices — first principles to Olympiad

> [!abstract] How to use this chapter
> Three passes. Pass 1: Parts 0-4 — bands instead of a resistivity table, doping as a numbers game, the junction derived from diffusion, the diode equation unpacked, rectifiers, regulation, light devices, the transistor, and logic gates. Pass 2: Parts 5-9 for exam craft. Pass 3: Parts 10-14 — the Olympiad layer (donor binding from a scaled Bohr atom, the diode equation from the Boltzmann factor, junction capacitance, the solar-cell bound, shot noise, Moore's law's tunnelling wall), the paper, the sheet, the checkpoint. Every number recomputed; every boxed result carries its validity condition.

## Part 0 · Orientation

### 0.1 What you will be able to do

After this chapter you can: rank materials by resistivity and predict the sign of their temperature coefficient; explain conduction with the filled-band argument; compute intrinsic carrier density and conductivity; find electron and hole densities in any doped sample from the mass-action law; derive the junction's depletion region, built-in field and contact potential; apply the exponential diode law with the 60 mV-per-decade rule; design and analyse rectifiers with ripple; size a Zener regulator for worst case; get an LED's colour from its gap; solve transistor currents in active and saturation modes, and design a switch; build truth tables, prove De Morgan's laws, and wire a half adder; and estimate the tunnelling limit of Moore's law and the switching power of a chip.

### 0.2 The one idea

Bands and doping turn a poor conductor into a controllable one: a tiny, charged impurity population sets the carriers, the junction's diffusion makes the one-way valve, and every device in electronics is a refinement of that valve.

### 0.3 Prerequisite self-check

1. Define resistivity and drift velocity, and state how current density relates to them. (`current-electricity/`)
2. What energy is stored on a capacitor, and how does $C$ scale with plate separation? (`capacitors/`)
3. Quote $E=\frac{hc}{\lambda}$ in eV-nm form and the de Broglie relation. (PART 23)
4. Scale the hydrogen ground-state energy and radius; name what sets them. (PART 24)
5. State the Hall voltage's dependence on current, field and thickness. (PART 18, when shipped — we preview it in OL6)

### 0.4 Exam orientation

JEE Main treats this chapter as high-yield and formula-friendly: classification, doping arithmetic, junction physics, diode circuits, transistor currents and gates. JEE Advanced pushes device reasoning (which mode is the transistor in, regulator design, ripple). NSEP and olympiad rounds reward first principles: the donor binding-energy estimate, the diode equation's origin, shot noise, scaling limits. The trap density here is conceptual, not algebraic.

### 0.5 What this chapter is not

Not a circuits course: op-amps, FET internals, biasing networks and AC analysis beyond the load line are out. Not a solid-state course: crystal structure, phonons and effective-mass theory appear only as far as devices need them.

### 0.6 Syllabus coverage map

The supplied Cengage volumes contain no semiconductor chapter (verified: *Optics and Modern Physics* Unit II holds only chs 3-5), so this map is keyed to the JEE Main/Advanced syllabus headings, per plan.md PART 27.

| # | Syllabus topic | Covered in | Status |
|---:|---|---|---|
| 1 | Classification: conductors, semiconductors, insulators; resistivity; temperature behaviour | §3.1 | full |
| 2 | Energy bands; forbidden gap; effective mass (intro) | §3.2 | full |
| 3 | Intrinsic semiconductors; electron-hole pairs; $n_i$ and its temperature dependence | §3.3 | full |
| 4 | Extrinsic: donors, acceptors, n and p type; mass-action law; neutrality | §3.4 | full |
| 5 | Conductivity, mobility, drift and diffusion currents | §3.5 | full |
| 6 | p-n junction formation; depletion region; barrier potential | §3.6 | full |
| 7 | Junction diode: forward/reverse, knee, exponential law, breakdown | §3.7 | full |
| 8 | Rectifiers (half/full-wave), ripple; clippers and clampers | §3.8 | full |
| 9 | Zener regulator; LED; photodiode; solar cell | §3.9 | full |
| 10 | Transistor: structure, $\alpha$, $\beta$, modes; amplification | §3.10 | full |
| 11 | Transistor circuits: amplifier load line, switch, follower | §3.11 | full |
| 12 | Logic gates; De Morgan; universal gates; half adder | §3.12 | full |
| 13 | Integrated circuits; Moore's law and its limits | §3.13 | full |
| 14 | Donor binding from scaled Bohr atom; diode equation from Boltzmann; junction capacitance; solar-cell bound; Hall measurement; shot noise; tunnelling limit; chip power | §3.4, §3.6, §3.13, Part 10 | added by sweep (olympiad layer) |

## Part 1 · Intuition first

**Silicon is not a metal because of a gap, not because of weak atoms.** Four electrons per silicon atom make four covalent bonds; at low temperature every electron is committed to a bond, and a filled band cannot carry current — there is nowhere to go. Warm the crystal and a few electrons jump the 1.1 eV gap, leaving behind vacancies that behave as positive carriers. The gap is the whole story: diamond with a 5.5 eV gap is an insulator, silicon with 1.1 eV a semiconductor, a metal has no gap at all.

**Doping is a numbers game, and the numbers are absurd.** Pure silicon at room temperature has about $1.5\times10^{16}$ carriers per m$^3$ — one in $10^{12}$ atoms. Replace one atom in a million with phosphorus and the carrier count jumps by a factor of $10^5$. The crystal's conductivity is no longer silicon's; it is the dopant's. Electronics is the art of placing those impurities.

**The junction is a one-way valve made by diffusion.** Put n-type against p-type and the majority carriers diffuse across, leaving fixed ions behind; the field those ions build stops the diffusion. Forward bias lowers the hill and current pours through exponentially; reverse bias raises it and only a trickle remains. Everything diode-like follows from that hill.

**A transistor is a valve controlled by a small current — but it amplifies nothing for free.** The collector current is a large stream throttled by a small base current; the energy in the output comes from the power supply, not from the base. Say that sentence whenever an exam asks where the power comes from.

## Part 2 · Definitions and bookkeeping

| Symbol | Meaning | Typical Si value (300 K) |
|---|---|---|
| $\rho$, $\sigma$ | resistivity, conductivity | $\rho_i\approx2300\ \Omega$ m; $\sigma_i\approx4.4\times10^{-4}$ S/m |
| $n$, $p$, $n_i$ | electron, hole, intrinsic density | $n_i=1.5\times10^{16}$ m$^{-3}$ |
| $\mu_e$, $\mu_h$ | electron, hole mobility | $0.135$, $0.048$ m$^2$/Vs |
| $E_g$ | band gap | Si 1.12 eV; Ge 0.66 eV; GaAs 1.42 eV; diamond 5.5 eV |
| $V_T$ | thermal voltage $kT/e$ | $25.9$ mV at 300 K |
| $\alpha$, $\beta$ | transistor current gains | $\beta=\frac{\alpha}{1-\alpha}$, typically 50-300 |
| $V_\gamma$ | diode knee voltage | $\sim0.7$ V (Si), $\sim0.3$ V (Ge) |

> [!info] Bookkeeping rules
> Carrier densities are per m$^3$ unless flagged; $1\ \text{cm}^{-3}=10^6\ \text{m}^{-3}$. The mass-action law $np=n_i^2$ holds in thermal equilibrium for non-degenerate doping. The exponential diode law holds below breakdown and at modest currents; real diodes carry an ideality factor we set to 1 here. A doped crystal is neutral: mobile carriers plus fixed ion charges sum to zero.

Three numbers to carry everywhere: $V_T=26$ mV; $60$ mV per decade of current; $1240$ eV-nm for $hc$.

## Part 3 · Core derivations

### 3.1 The three classes of conduction

Resistivities span thirty orders: metals $\sim10^{-8}\ \Omega$ m, semiconductors $10^{-5}$ to $10^{3}\ \Omega$ m, insulators up to $\sim10^{22}\ \Omega$ m. Only a logarithmic axis can hold the table on one page. Temperature separates the classes by *mechanism*, not sign of the answer:

| Class | Carriers | What limits current | Effect of heating |
|---|---|---|---|
| metal | plenty | lattice scattering | more scattering, $R$ rises |
| semiconductor | scarce | carrier supply | more pairs, $R$ falls |
| thermistor (NTC) | scarce, engineered | carrier supply | $R$ falls steeply |

In a metal the carrier count is fixed, so rising temperature only raises the collision rate and $\rho$. In a semiconductor, $n_i$ rises exponentially with $T$ (Eq. 3.2 below), overwhelming the mild mobility loss: $\rho$ falls. Same thermometer, opposite verdict, different mechanism — examiners love to swap the two stories.

> [!abstract] DIAGRAM D27.1 · The thirty-order resistivity axis
> *Show:* a horizontal log axis from 10 to the minus 8 to 10 to the 22 ohm-metre; three labelled bands (conductors, semiconductors, insulators); real materials pinned at their values (copper, silicon intrinsic, germanium, glass, quartz).
> *Search:* "resistivity ranges conductors semiconductors insulators log scale"
> *Used in:* §3.1.

> [!abstract] DIAGRAM D27.2 · Resistance against temperature, three curves
> *Show:* R against T for a metal (rising line), an intrinsic semiconductor (falling exponential), and an NTC thermistor (steeper fall); each annotated with its mechanism.
> *Search:* "resistance temperature metal semiconductor thermistor curves"
> *Used in:* §3.1.

### 3.2 Bands, and why a filled band cannot conduct

Electrons in a crystal form allowed energy bands separated by forbidden gaps. Conduction needs electrons that can change state under a field — move to a slightly different momentum. A completely filled band offers no empty state to move into, so an applied field produces no net motion: the band is inert, like a full parking lot with nowhere to shift. Conduction therefore happens in partially filled bands (metals) or in bands that acquire a few carriers (semiconductors).

Gap sizes decide everything: diamond 5.5 eV (nothing jumps at 300 K — $kT=0.026$ eV), Si 1.12 eV (a few jump), Ge 0.66 eV (more), GaAs 1.42 eV (the optoelectronics workhorse). An insulator is a semiconductor with a gap too big to feed; the distinction is practical, not categorical. The electron responds inside the band as if it had an effective mass $m^*$ set by the band's curvature — we use it as a number, not a theory, in the donor estimate (§3.4).

> [!abstract] DIAGRAM D27.3 · Three band diagrams
> *Show:* metal: overlapping or half-filled band; insulator: full valence band, 5 eV gap, empty conduction band; semiconductor: same but a 1 eV gap with a few electrons promoted and holes marked below; gaps labelled in eV.
> *Search:* "band diagram metal insulator semiconductor comparison"
> *Used in:* §3.2.

### 3.3 Intrinsic carriers and their temperature law

At temperature $T$, collisions promote valence electrons across the gap, creating an electron-hole pair; recombination annihilates one. Equilibrium fixes the intrinsic density, whose form comes from the density of states ($\propto T^{3/2}$) times the Boltzmann jump probability $e^{-E_g/kT}$ split across two carriers:

$$
n_i\propto T^{3/2}e^{-E_g/2kT}. \qquad (3.1)
$$

The half-gap in the exponent is the reason semiconductors are so temperature-sensitive: for Si, $E_g/2kT=21.6$ at 300 K, so doubling $T$ changes the exponential by $e^{10.8}\approx5\times10^4$. With $n_i(\text{Si})=1.5\times10^{16}$ m$^{-3}$ at 300 K and mobilities $0.135/0.048$ m$^2$/Vs:

$$
\sigma_i=en_i(\mu_e+\mu_h)=4.4\times10^{-4}\ \text{S/m}\quad\Rightarrow\quad\rho_i\approx2300\ \Omega\,\text{m}. \qquad (3.2)
$$

Pure silicon is a poor conductor by everyday standards — about $10^{22}$ worse than copper, barely better than a damp brick. The chapter exists to fix that.

> [!abstract] DIAGRAM D27.4 · Generation and recombination
> *Show:* a band gap with an electron promoted up (arrow up, photon or phonon label) leaving a hole, and an electron falling back (arrow down) with recombination; equilibrium captioned as equal rates.
> *Search:* "electron hole pair generation recombination band diagram"
> *Used in:* §3.3.

> [!abstract] DIAGRAM D27.5 · A hole moves by bond-swapping
> *Show:* a silicon lattice row; a hole (empty bond) at one site; a neighbouring valence electron stepping into it; the hole apparently stepping the other way; three frames of the swap making the vacancy travel right while electrons travel left.
> *Search:* "hole conduction bond model semiconductor animation frames"
> *Used in:* §3.3.

### 3.4 Doping, neutrality and the mass-action law

Replace one Si atom in $10^6$ with phosphorus (five valence electrons): four electrons bond, the fifth sits so loosely that room temperature frees it — a donor, making n-type material. Replace with boron (three valence electrons): one bond lacks an electron, a vacancy that accepts one — an acceptor, making p-type.

Why so loosely bound? Scale the hydrogen atom (PART 24): the donor electron orbits the P$^+$ core screened by the lattice dielectric constant $\kappa=11.7$ and moving with effective mass $m^*=0.26m_e$:

$$
E_d=13.6\,\text{eV}\times\frac{m^*/m}{\kappa^2}=13.6\times\frac{0.26}{136.9}=26\ \text{meV}, \qquad (3.3)
$$

against $kT=26$ meV at 300 K — thermal energy alone ionises nearly all donors. The orbit radius $a^*=\kappa a_0(m/m^*)=2.4$ nm spans a dozen lattice spacings: the electron is barely bound to the atom at all, which is what "nearly free" means here. Measured Si:P ionisation is 45 meV — the model is a factor of 1.7 off (the simple hydrogen picture ignores valley degeneracy and anisotropy), an honesty line worth writing in olympiad answers (OL1).

Charge neutrality of an n-type crystal with donors $N_d$ fully ionised: mobile electrons $n$ plus fixed donor ions $+eN_d$ — the crystal is neutral because $n\approx N_d$ counts the electrons *released from the donors themselves*. Combine with the mass-action law,

$$
np=n_i^2, \qquad (3.4)
$$

which survives doping because generation-recombination equilibrium still holds: for $N_d=10^{21}$ m$^{-3}$, $n\approx10^{21}$, $p=\frac{(1.5\times10^{16})^2}{10^{21}}=2.3\times10^{11}$ m$^{-3}$. Majority and minority differ by ten orders.

> [!abstract] DIAGRAM D27.6 · The doped lattice
> *Show:* two panels of the silicon lattice: one site swapped to a pentavalent phosphorus with its fifth electron marked loosely bound and a free-electron arrow; another swapped to trivalent boron with an empty bond marked as a hole.
> *Search:* "n-type p-type doping silicon lattice diagram phosphorus boron"
> *Used in:* §3.4.

> [!abstract] DIAGRAM D27.7 · The giant donor orbit
> *Show:* the donor ion at the centre with the electron's Bohr-like orbit of radius 2.4 nm drawn over the 0.54 nm lattice cell, spanning many cells; an energy inset comparing E-d = 26 meV below the conduction band against the 1.1 eV gap.
> *Search:* "donor electron hydrogenic orbit effective mass semiconductor"
> *Used in:* §3.4, OL1.

### 3.5 Transport: drift, mobility and conductivity

Drift under field $E$: each carrier reaches $v_d=\mu E$, giving the conductivity sum

$$
\sigma=e(n_e\mu_e+n_h\mu_h). \qquad (3.5)
$$

The doped crystal of §3.4: $\sigma=e(10^{21})(0.135)=21.6$ S/m, $\rho=0.046\ \Omega$ m — a factor of $5\times10^4$ over intrinsic silicon from one impurity per million atoms. Diffusion is the second transport mode: carriers flow down concentration gradients, $J_{\text{diff}}\propto-\frac{dn}{dx}$, and it is diffusion, not the field, that builds the junction (§3.6). Temperature pulls two levers: mobility falls gently with $T$ (more scattering) while $n_i$ rises exponentially; at high enough temperature every semiconductor reverts to intrinsic behaviour and devices forget their doping.

### 3.6 The p-n junction

Join n-type to p-type. Majority carriers near the interface diffuse across — electrons into p-side, holes into n-side — leaving behind fixed donor and acceptor ions the lattice cannot move. A depletion region forms, charged and field-bearing. The field drives drift currents opposing the diffusion; equilibrium is reached when drift exactly cancels diffusion for each carrier species, which fixes the built-in potential (contact potential, $\sim0.7$ V for Si): the Boltzmann balance $n(x)\propto e^{-eV(x)/kT}$ across the junction gives $eV_0=kT\ln\frac{n_nn_p}{n_i^2}$, of order the gap voltage. The potential hill $V_0$ is why no perpetual current flows: any drift current is exactly offset by the diffusion current it would feed.

> [!abstract] DIAGRAM D27.8 · The depletion region
> *Show:* the junction vertical; left side n-type with fixed positive donor ions, right p-type with fixed negative acceptor ions; field arrows pointing right-to-left across the depleted strip; the potential hill rising from p to n labelled about 0.7 V; mobile carriers absent inside.
> *Search:* "p-n junction depletion region fixed ions field potential diagram"
> *Used in:* §3.6.

> [!abstract] DIAGRAM D27.9 · Charge, field and potential aligned
> *Show:* three graphs stacked with a common x-axis across the junction: fixed charge density as two rectangles of opposite sign; electric field as a triangle peaking at the junction; potential as a smooth S-shaped hill; widths and peaks aligned between the three.
> *Search:* "pn junction charge field potential profiles aligned graphs"
> *Used in:* §3.6, OL3.

Bias the junction: forward (p positive) lowers the hill to $V_0-V$ and diffusion floods through — current grows exponentially. Reverse raises the hill to $V_0+V$; only thermally generated minority carriers can be swept across, giving the tiny saturation current $I_0$. The depletion width grows with reverse voltage as $W\propto\sqrt{V_0+V}$ (OL3), and the junction acts as a capacitor whose value falls as $V^{-1/2}$.

### 3.7 The diode equation and the 60 mV rule

The balance of drift and diffusion across the biased hill gives the Shockley law:

$$
I=I_0\left(e^{eV/kT}-1\right)=I_0\left(e^{V/V_T}-1\right),\qquad V_T=\frac{kT}{e}=25.9\ \text{mV}. \qquad (3.6)
$$

Two consequences define diode practice. First, the knee: at $V\approx0.6$ V the exponential factor is $e^{23}\sim10^{10}$, so current explodes from nanoamps to milliamps in a tenth of a volt — the "0.7 V drop" is just where this explosion meets circuit resistance. Second, the decade rule: increasing $V$ by $\ln10\times V_T=59.5$ mV multiplies current by 10 — the 60 mV per decade of the logarithmic I-V. Reverse bias kills the exponential, leaving $I\approx-I_0$ until breakdown: Zener tunnelling across a thin heavily-doped junction (low voltages), or avalanche impact ionisation in wider junctions (higher voltages). The Zener diode is engineered to live in that reverse region; an ordinary diode is not.

> [!abstract] DIAGRAM D27.10 · The diode I-V in full
> *Show:* I against V: forward exponential rising at 0.6-0.7 V with a decade-per-60 mV annotation; reverse saturation current near zero; breakdown knee at negative V labelled Zener/avalanche; knee and V-T marked.
> *Search:* "diode IV curve knee breakdown zener annotated"
> *Used in:* §3.7.

### 3.8 Rectifiers and ripple

Half-wave: one diode passes alternate half-cycles; the average output over a full period is $V_{\text{dc}}=\frac{V_p}{\pi}=0.318V_p$. Full-wave (bridge of four diodes, or centre-tap) flips the negative halves: $V_{\text{dc}}=\frac{2V_p}{\pi}=0.637V_p$, RMS $=\frac{V_p}{\sqrt2}$, and the ripple frequency doubles. A smoothing capacitor charges to the peak and discharges into the load between peaks; with discharge time $\approx\frac{1}{2f}$ (full-wave) and constant load current $I$:

$$
\Delta V\approx\frac{I}{2fC}. \qquad (3.7)
$$

At $I=100$ mA, $f=50$ Hz, $C=1000\ \mu$F: $\Delta V=1.0$ V — the arithmetic of every power-supply question. Clippers cut waveform regions (biased diode thresholds); clampers shift the whole waveform by a capacitor-diode charge pump; the peak detector is the capacitor charged to $V_p$ minus one drop.

> [!abstract] DIAGRAM D27.11 · Half-wave rectification with ripple
> *Show:* sine input; the half-wave output with gaps; a capacitor-smoothed trace with sawtooth ripple labelled delta-V; the discharge slope annotated I over C.
> *Search:* "half wave rectifier capacitor ripple waveform"
> *Used in:* §3.8.

> [!abstract] DIAGRAM D27.12 · The full-wave bridge
> *Show:* four diodes in the bridge diamond with the AC source and load; below, input sine and full-wave output (all humps positive); the current path drawn for each half-cycle in two small panels.
> *Search:* "bridge rectifier full wave diagram current paths"
> *Used in:* §3.8.

### 3.9 Regulation, light and detection

The Zener shunt regulator: a series resistor $R$ feeds the load in parallel with a reverse-biased Zener at $V_Z$. The resistor must supply the worst-case load current plus enough Zener current to stay in breakdown, while never exceeding the Zener's power at minimum load:

$$
R=\frac{V_{\text{in}}-V_Z}{I_{L,\max}+I_{Z,\min}},\qquad P_{Z,\max}=V_Z\,I_{Z,\max}\ \text{at}\ I_L=0. \qquad (3.8)
$$

For $V_{\text{in}}=12$ V, $V_Z=5$ V, $I_{L,\max}=50$ mA, $I_{Z,\min}=5$ mA: $R=\frac{7}{0.055}=127\ \Omega$, and at no load the Zener carries all 55 mA, $P=0.28$ W — the resistor choice is a two-sided squeeze, which is what makes it an engineering problem.

The LED is a forward-biased junction whose recombinations emit photons: $\lambda=\frac{hc}{E_g}=\frac{1240\ \text{eV nm}}{E_g}$. Red 620 nm needs 2.0 eV; blue 470 nm needs 2.64 eV — silicon's 1.1 eV gap emits infrared, and worse, indirectly, so LEDs use compound semiconductors (GaAsP, GaP, InGaN), and blue had to wait for GaN materials science. A photodiode is the same junction run in reverse: light-generated pairs are swept by the depletion field, giving current proportional to flux. A solar cell is the same device with no external bias, delivering power: light shifts the I-V curve into the fourth quadrant.

> [!abstract] DIAGRAM D27.13 · The Zener shunt regulator
> *Show:* input source, series resistor, node splitting to the load resistor and the reverse Zener to ground; currents labelled I-R, I-L, I-Z; the output clamped at V-Z; a note showing the worst-case choices.
> *Search:* "zener voltage regulator circuit series resistor load"
> *Used in:* §3.9.

> [!abstract] DIAGRAM D27.14 · Colour versus gap
> *Show:* a horizontal wavelength strip from red to violet with LED materials pinned at their gaps: GaAsP at 1.9 eV red, GaP at 2.26 eV green, InGaN at 2.6 eV blue, GaN at 3.4 eV ultraviolet; the 1240 over E-g relation captioned.
> *Search:* "LED color bandgap wavelength materials chart"
> *Used in:* §3.9.

> [!abstract] DIAGRAM D27.15 · The junction as photodiode and solar cell
> *Show:* two panels of the same reverse-looking junction: photodiode, photons creating pairs swept by the field into a meter current; solar cell, the same pairs driving a load with no battery, the I-V curve shifted into the power quadrant.
> *Search:* "photodiode solar cell pn junction operation comparison"
> *Used in:* §3.9.

### 3.10 The bipolar transistor

An npn transistor sandwiches a thin, lightly doped p base between n emitter and n collector. Forward-bias the base-emitter junction; the emitter floods the base with electrons. Because the base is thin and lightly doped, most electrons cross it before recombining — collected by the reverse-biased base-collector junction. The small recombination current is the base current. Current bookkeeping:

$$
I_E=I_B+I_C,\qquad \alpha=\frac{I_C}{I_E},\qquad \beta=\frac{I_C}{I_B}=\frac{\alpha}{1-\alpha}. \qquad (3.9)
$$

With $\alpha=0.98$, $\beta=49$: losing 2 % to recombination buys a current gain of 49. Active-mode rules: $V_{BE}\approx0.7$ V (Si) and $I_C=\beta I_B$, with $I_C$ nearly independent of $V_{CE}$. Saturation: both junctions forward-biased, $V_{CE}\sim0.2$ V, and $I_C<\beta I_B$ — the collector current is then set by the external circuit, not by $\beta$; applying Eq. (3.9) in saturation is the chapter's classic trap. Cutoff: no base drive, no current. Where does the amplified power come from? The supply: the base current only turns the tap.

### 3.11 Transistor circuits

Common-emitter amplifier: a load resistor in the collector and the load line $V_{CE}=V_{CC}-I_CR_C$ drawn on the output characteristics; the operating point sits on the line, small base swings ride it, and the voltage gain is $A_v\approx-g_mR_C$ — sign inverted, hence the inversion. The switch: drive the base hard so the transistor saturates ($V_{CE}\approx0.2$ V) and the load sees nearly the full supply; choose $I_B>\frac{I_{C,\text{sat}}}{\beta}$ with margin. A 5 V supply driving a 100 mA lamp with $\beta=100$ needs $I_B\geq1$ mA, so $R_B\leq\frac{5-0.7}{1\ \text{mA}}=4.3\ \text{k}\Omega$. The emitter follower buffers (gain 1, current gain $\beta$); the current source exploits $I_C$'s indifference to $V_{CE}$. A transistor is not a resistor: its output current is set by the base, not by the voltage across it.

> [!abstract] DIAGRAM D27.16 · The npn transistor and its currents
> *Show:* the three regions with doping labels and widths (base drawn thin); I-E arrow in, I-C arrow out through the reverse-biased collector junction, the thin I-B recombination arrow; biasing batteries shown with polarities.
> *Search:* "npn transistor structure emitter base collector currents diagram"
> *Used in:* §3.10.

> [!abstract] DIAGRAM D27.17 · Load line and switch
> *Show:* left panel: output characteristics with the load line from V-CC to V-CC over R-C, Q-point marked, an input swing producing an inverted output swing; right panel: the switch circuit with a lamp load, base resistor, saturation point labelled V-CE about 0.2 V.
> *Search:* "common emitter load line transistor switch diagram"
> *Used in:* §3.11.

### 3.12 Logic gates

Build NOT from a transistor: input high saturates the transistor, pulling the output to ground; input low leaves the output pulled up — inversion, analysed not asserted. AND and OR follow from diode networks (or from NAND/NOR plus NOT); the truth tables of all six standard gates are the chapter's table work. De Morgan's laws, proved by exhaustive truth tables:

$$
\overline{A\cdot B}=\overline{A}+\overline{B},\qquad \overline{A+B}=\overline{A}\cdot\overline{B}. \qquad (3.10)
$$

NAND (and NOR) are universal: any logic follows from NANDs alone. The half adder adds two bits: $S=A\oplus B$ (XOR), $C=A\cdot B$ (AND) — two gates, and binary arithmetic begins. Why binary? Two well-separated voltage levels tolerate noise; ten levels would need precision no noisy wire can hold.

> [!abstract] DIAGRAM D27.18 · Gates and the half adder
> *Show:* the six gate symbols with two-line truth tables each; then the half adder: XOR and AND gates sharing inputs A and B, outputs S and C, with the four-row table verifying the sums.
> *Search:* "logic gates symbols truth tables half adder circuit"
> *Used in:* §3.12.

### 3.13 Integration and its wall

Modern chips pack billions of gates; Moore's doubling ran for fifty years because lithography kept shrinking features. The wall is quantum: when a gate's barrier thins to a few nanometres, carriers tunnel through it whether the gate is "off" or not (PART 23's de Broglie and uncertainty in the engineer's clothing — OL7 computes it). Leakage, not speed, ends the scaling era; the industry answers with new geometries and materials, not just smaller lines. Switching itself costs energy: charging a gate capacitance $C$ through a voltage swing $V$ dissipates $\sim\frac12CV^2$ per transition (the capacitor's stored energy, half lost in the resistance — `capacitors/`), so a billion gates at a gigahertz dissipate hundreds of watts and need the fan (OL11).

## Part 4 · Results, limits and the validity ledger

### 4.1 Boxed results

$$
\boxed{\sigma=e(n\mu_e+p\mu_h),\qquad np=n_i^2,\qquad n_i\propto T^{3/2}e^{-E_g/2kT}} \qquad (4.1)
$$

thermal equilibrium, non-degenerate doping.

$$
\boxed{E_d=13.6\,\text{eV}\times\frac{m^*/m}{\kappa^2}\approx26\ \text{meV (Si)}} \qquad (4.2)
$$

hydrogenic donor; measured 45 meV, factor 1.7 low.

$$
\boxed{V_0\sim0.7\ \text{V (Si)},\qquad I=I_0(e^{V/V_T}-1),\qquad V_T=25.9\ \text{mV}} \qquad (4.3)
$$

ideality 1, below breakdown; 60 mV per decade.

$$
\boxed{\Delta V\approx\frac{I}{2fC}\ (\text{full-wave}),\qquad V_{\text{dc}}=\frac{2V_p}{\pi}} \qquad (4.4)
$$

ripple small compared with $V_p$.

$$
\boxed{R=\frac{V_{\text{in}}-V_Z}{I_{L,\max}+I_{Z,\min}},\qquad \beta=\frac{\alpha}{1-\alpha},\qquad I_E=I_B+I_C} \qquad (4.5)
$$

Zener sizing; active mode only for the gain laws.

$$
\boxed{\lambda=\frac{1240\ \text{eV nm}}{E_g}} \qquad (4.6)
$$

LED emission; direct-gap materials assumed.

### 4.2 Limit checks

- $E_g\to\infty$: $n_i\to0$, the insulator, correct.
- $E_g\to0$: intrinsic density diverges, the metal, correct.
- $T\to\infty$: extrinsic devices lose their doping to intrinsic carriers, correct.
- $V\ll V_T$ in Eq. (4.3): $I\approx I_0V/V_T$, ohmic, correct.
- $\alpha\to1$: $\beta\to\infty$, the ideal transistor, correct.
- $C\to\infty$ in Eq. (4.4): ripple vanishes, correct.

### 4.3 Which formula when

| Given | Need | Use |
|---|---|---|
| doping and mobilities | conductivity | Eq. (4.1) |
| one carrier density | the other | $np=n_i^2$ |
| dopant, lattice constant | binding energy, orbit | Eq. (4.2) |
| forward voltage | current ratio | decade rule of Eq. (4.3) |
| load, frequency | capacitor | Eq. (4.4) |
| supply, Zener, load range | series resistor | Eq. (4.5) |
| base current, mode | collector current | Eq. (4.5), check saturation |
| colour or wavelength | gap | Eq. (4.6) |

### 4.4 Concept checks

**C1 — concept check.** Why does a metal's resistance rise with temperature while silicon's falls?

<details><summary>Answer</summary>

Metals have fixed carrier counts, so extra scattering raises rho; silicon gains carriers exponentially, which beats its mild mobility loss.

</details>

**C2 — concept check.** Why can a filled band not conduct?

<details><summary>Answer</summary>

No empty states: the field cannot shift electrons to new momenta, so no net motion.

</details>

**C3 — concept check.** An insulator versus a semiconductor, in one line?

<details><summary>Answer</summary>

Same mechanism, bigger gap: too big for thermal promotion at working temperatures.

</details>

**C4 — concept check.** Is a doped crystal charged?

<details><summary>Answer</summary>

No: mobile carriers plus fixed ion charges sum to zero; donors release their own electrons.

</details>

**C5 — concept check.** In n-type silicon with n = 1e21 per m-cubed, the hole density?

<details><summary>Answer</summary>

p = ni-squared over n = 2.3e11 per m-cubed.

</details>

**C6 — concept check.** Why are donors ionised at room temperature?

<details><summary>Answer</summary>

Their 26 meV binding equals the 26 meV thermal energy: kT alone frees them.

</details>

**C7 — concept check.** What stops the junction's diffusion from running forever?

<details><summary>Answer</summary>

The fixed-ion field it creates: drift exactly cancels diffusion at equilibrium.

</details>

**C8 — concept check.** Forward versus reverse bias in terms of the hill?

<details><summary>Answer</summary>

Forward lowers the built-in hill to V0 minus V; reverse raises it to V0 plus V.

</details>

**C9 — concept check.** Current rises from 1 mA to 10 mA. The voltage change?

<details><summary>Answer</summary>

About 60 mV (one decade at room temperature).

</details>

**C10 — concept check.** Zener breakdown versus avalanche: which needs the thin junction?

<details><summary>Answer</summary>

Zener tunnelling needs the thin, heavily doped junction; avalanche needs room to accelerate.

</details>

**C11 — concept check.** In saturation, is I-C equal to beta I-B?

<details><summary>Answer</summary>

No: the external circuit limits I-C below beta I-B; both junctions are forward-biased.

</details>

**C12 — concept check.** Where does a transistor amplifier's output power come from?

<details><summary>Answer</summary>

The DC supply; the base current only controls the flow.

</details>

**C13 — concept check.** Why must the base be thin and lightly doped?

<details><summary>Answer</summary>

So injected electrons cross it before recombining, keeping alpha near one and beta large.

</details>

**C14 — concept check.** Why binary and not decimal logic?

<details><summary>Answer</summary>

Two separated levels survive noise margins; ten levels would need noiseless wires.

</details>

## Part 5 · Worked exemplars

### E1 — Classifying a mystery sample

A sample has $\rho\approx10^{-2}\ \Omega$ m and its resistance falls as it warms. Classify it.

> [!success] Check
> Between metal and insulator on the log axis, with semiconductor temperature behaviour.

<details><summary>Solution</summary>

**Method.** $\rho$ sits in the semiconductor band ($10^{-5}$ to $10^3\ \Omega$ m); falling $R$ with $T$ confirms it — heating frees carriers. A metal at this resistivity would rise with temperature.

</details>

### E2 — Intrinsic silicon's conductivity

Compute $\sigma_i$ and $\rho_i$ for Si at 300 K ($n_i=1.5\times10^{16}$ m$^{-3}$, $\mu_e=0.135$, $\mu_h=0.048$ m$^2$/Vs).

> [!success] Check
> Kilohm-metres: pure silicon conducts like a damp brick, not like a wire.

<details><summary>Solution</summary>

**Method.** $\sigma_i=en_i(\mu_e+\mu_h)=1.6\times10^{-19}\times1.5\times10^{16}\times0.183=4.4\times10^{-4}$ S/m; $\rho_i=\frac{1}{\sigma_i}=2270\ \Omega$ m.

</details>

### E3 — One impurity in a million

Si doped n-type at $N_d=10^{21}$ m$^{-3}$ (one P atom per $5\times10^7$ Si atoms). Find $n$, $p$, $\sigma$, $\rho$ and the gain over intrinsic.

> [!success] Check
> Majority-minority gap of ten orders; conductivity gain about 10 to the five.

<details><summary>Solution</summary>

**Method.** $n\approx N_d=10^{21}$ m$^{-3}$; $p=\frac{n_i^2}{n}=\frac{2.25\times10^{32}}{10^{21}}=2.25\times10^{11}$ m$^{-3}$; $\sigma=en\mu_e=21.6$ S/m; $\rho=0.046\ \Omega$ m; gain $\frac{21.6}{4.4\times10^{-4}}\approx4.9\times10^4$.

</details>

### E4 — The donor's binding energy

Estimate the ionisation energy and orbit radius of phosphorus in silicon ($\kappa=11.7$, $m^*=0.26m_e$); compare with the measured 45 meV.

> [!success] Check
> Tens of meV, comparable to kT; orbit spanning many cells; model short by about a factor of two.

<details><summary>Solution</summary>

**Method.** $E_d=13.6\times\frac{0.26}{11.7^2}=26$ meV, against measured 45 meV: the hydrogenic picture misses valley structure by a factor 1.7 but nails the scale and the physics. $a^*=\kappa a_0\frac{m}{m^*}=11.7\times0.053\times\frac{1}{0.26}=2.4$ nm, about 4.4 lattice spacings across.

</details>

### E5 — The decade rule on a real curve

A diode carries 1 mA at 0.60 V. Current at 0.66 V? At 0.72 V?

> [!success] Check
> Exactly one decade per 60 mV at room temperature.

<details><summary>Solution</summary>

**Method.** $\Delta V=60$ mV $\Rightarrow\times10$: so 10 mA at 0.66 V, 100 mA at 0.72 V. The knee is where this ladder meets the circuit's resistance.

</details>

### E6 — Rectifier averages

For a 10 V peak sinusoid, the DC outputs of half-wave and full-wave rectification?

> [!success] Check
> 0.318 and 0.637 of the peak.

<details><summary>Solution</summary>

**Method.** Half-wave: $\frac{10}{\pi}=3.18$ V; full-wave: $\frac{20}{\pi}=6.37$ V (before diode drops).

</details>

### E7 — Designing the ripple away

A full-wave supply must deliver 100 mA with ripple below 1 V at 50 Hz. Capacitor? What if the ripple spec halves?

> [!success] Check
> C inversely proportional to ripple; halving ripple doubles C.

<details><summary>Solution</summary>

**Method.** $\Delta V=\frac{I}{2fC}\Rightarrow C=\frac{0.1}{100\times1}=1000\ \mu$F. Halving $\Delta V$: $C=2000\ \mu$F.

</details>

### E8 — Sizing the Zener resistor

$V_{\text{in}}=12$ V, $V_Z=5$ V, load up to 50 mA, keep at least 5 mA in the Zener. Find R and the worst-case Zener power.

> [!success] Check
> The two-sided squeeze: enough current at full load, safe power at no load.

<details><summary>Solution</summary>

**Method.** $R=\frac{12-5}{0.050+0.005}=127\ \Omega$ (use 120 $\Omega$ standard). At no load the Zener carries $\frac{7}{120}=58$ mA: $P=5\times0.058=0.29$ W — specify a 0.5 W part.

</details>

### E9 — Choosing an LED material

Which gap gives red 620 nm light, and why not silicon?

> [!success] Check
> 1240 over wavelength; silicon's gap lands in the infrared and is indirect anyway.

<details><summary>Solution</summary>

**Method.** $E_g=\frac{1240}{620}=2.0$ eV — GaAsP territory. Si's 1.12 eV gives $\lambda=\frac{1240}{1.12}=1107$ nm (infrared) and indirect recombination: a silicon LED is doubly impossible.

</details>

### E10 — Transistor current bookkeeping

$\alpha=0.98$, $I_B=20\ \mu$A. Find $\beta$, $I_C$, $I_E$.

> [!success] Check
> Beta near 50; emitter current equals base plus collector to three figures.

<details><summary>Solution</summary>

**Method.** $\beta=\frac{0.98}{0.02}=49$; $I_C=\beta I_B=0.98$ mA; $I_E=I_C+I_B=1.00$ mA.

</details>

### E11 — The lamp-driver switch

A 5 V supply, a 100 mA lamp, $\beta=100$. Maximum base resistor for guaranteed saturation, and the lamp voltage in saturation?

> [!success] Check
> Drive at least the critical base current; V-CE collapses to about 0.2 V.

<details><summary>Solution</summary>

**Method.** Need $I_B\geq\frac{100\ \text{mA}}{100}=1$ mA (design with margin, say 2 mA); $R_B\leq\frac{5-0.7}{1\ \text{mA}}=4.3\ \text{k}\Omega$. In saturation $V_{CE}\approx0.2$ V, so the lamp sees $\sim4.8$ V.

</details>

### E12 — Verifying the half adder

Tabulate S and C for all input pairs and identify the gates.

> [!success] Check
> S is XOR, C is AND; the 1-plus-1 row must read 10 in binary.

<details><summary>Solution</summary>

**Method.** Rows: 00 $\to$ S 0, C 0; 01 $\to$ 1, 0; 10 $\to$ 1, 0; 11 $\to$ 0, 1. So $S=A\oplus B$, $C=A\cdot B$: two gates build binary addition.

</details>

## Part 6 · Problem archetypes and practice

### 6.1 Archetypes

| # | Archetype | Template | Where worked | Variations |
|---:|---|---|---|---|
| 1 | Classify by resistivity and temperature sign | log axis plus mechanism table | E1, Q1-Q2 | thermistor wording |
| 2 | Compare gaps and thermal access | exponential of $E_g/2kT$ | Q3-Q4 | Ge vs Si |
| 3 | Intrinsic conductivity | Eq. (4.1) | E2 | per material |
| 4 | Carrier densities from doping | $np=n_i^2$ | E3, Q5 | either type |
| 5 | Conductivity from doping | $\sigma=en\mu$ | E3, Q7 | p-type uses $\mu_h$ |
| 6 | Donor binding and radius | scaled Bohr | E4 | acceptor analogue |
| 7 | Junction response to bias | hill up or down; $W\propto\sqrt V$ | Q9 | capacitance link |
| 8 | Diode current from voltage | decade rule | E5, Q10 | temperature of V-T |
| 9 | Diode on or off in a circuit | assume, check consistency | Q15 | two-diode logic |
| 10 | Rectifier DC and ripple | Eqs. (4.4) | E6, E7, Q12-Q14 | half vs full |
| 11 | Zener resistor sizing | Eq. (4.5) | E8, Q16 | worst case both sides |
| 12 | LED colour from gap | Eq. (4.6) | E9, Q17-Q18 | reverse direction |
| 13 | Photodiode and solar cell modes | reverse bias; power quadrant | Q19-Q20 | bias choice |
| 14 | Transistor currents | Eqs. (4.5) | E10, Q21-Q22 | alpha-beta conversions |
| 15 | Saturation test | compare $\beta I_B$ with circuit maximum | Q23, E11 | switch design |
| 16 | Truth tables and adders | exhaustive rows | Q25-Q28, E12 | De Morgan rows |

### 6.2 In-flow practice

#### Q1. A wire's resistance rises with temperature. The mechanism?

<details><summary>Solution</summary>

Fixed carrier count, rising collision rate: lattice scattering dominates.

</details>

#### Q2. An NTC thermistor warms. Its resistance?

<details><summary>Solution</summary>

Falls steeply: carrier generation wins over mobility loss.

</details>

#### Q3. Diamond's gap is 5.5 eV against silicon's 1.12 eV. Ratio of intrinsic densities at 300 K, order of magnitude?

<details><summary>Solution</summary>

$n_i$ ratio $\sim e^{-(5.5-1.12)/(2\times0.026)}=e^{-84}\approx10^{-37}$: diamond has essentially none.

</details>

#### Q4. Germanium (0.66 eV) versus silicon (1.12 eV): which has more intrinsic carriers at 300 K?

<details><summary>Solution</summary>

Germanium, by $e^{(1.12-0.66)/(2\times0.026)}\approx e^{8.8}\approx7\times10^3$.

</details>

#### Q5. p-type Si with $N_a=10^{22}$ m-cubed: the electron density?

<details><summary>Solution</summary>

$n=\frac{n_i^2}{N_a}=\frac{2.25\times10^{32}}{10^{22}}=2.25\times10^{10}$ m$^{-3}$.

</details>

#### Q6. State the neutrality condition for n-type silicon with ionised donors.

<details><summary>Solution</summary>

$n=p+N_d^+$: mobile electrons balance holes plus fixed positive donor ions; net charge zero.

</details>

#### Q7. Conductivity of the sample in Q5, with $\mu_h=0.048$ m-squared per volt-second?

<details><summary>Solution</summary>

$\sigma\approx ep\mu_h=1.6\times10^{-19}\times10^{22}\times0.048=76.8$ S/m.

</details>

#### Q8. Same field on electrons and holes in silicon: drift-speed ratio?

<details><summary>Solution</summary>

$\frac{\mu_e}{\mu_h}=\frac{0.135}{0.048}\approx2.8$.

</details>

#### Q9. Reverse bias on a junction is quadrupled. The depletion width?

<details><summary>Solution</summary>

Doubles: $W\propto\sqrt{V_0+V}$.

</details>

#### Q10. A diode at 1 mA, 0.60 V: voltage for 1 A?

<details><summary>Solution</summary>

Three decades: $0.60+3\times0.060=0.78$ V (ideal law).

</details>

#### Q11. Why is the reverse saturation current so small, and what grows it?

<details><summary>Solution</summary>

Only thermally generated minority carriers feed it; heating (doubling roughly every 10 K) grows it.

</details>

#### Q12. Half-wave rectifier, 10 V peak: average output?

<details><summary>Solution</summary>

$10/\pi=3.18$ V.

</details>

#### Q13. Full-wave rectifier fed from 50 Hz mains: ripple frequency?

<details><summary>Solution</summary>

100 Hz.

</details>

#### Q14. The smoothing capacitor in E7 is halved. Ripple?

<details><summary>Solution</summary>

Doubles to 2 V.

</details>

#### Q15. Two ideal diodes anode-connected to inputs A, B, cathodes joined to the output through a pull-down. The logic function?

<details><summary>Solution</summary>

OR: either high input pulls the output high.

</details>

#### Q16. The regulator of E8 with the load disconnected: Zener current and power (R = 120 ohms)?

<details><summary>Solution</summary>

$I_Z=\frac{12-5}{120}=58$ mA; $P=5\times0.058=0.29$ W.

</details>

#### Q17. An LED's gap is 1.8 eV. Colour?

<details><summary>Solution</summary>

$\lambda=\frac{1240}{1.8}=689$ nm: deep red.

</details>

#### Q18. Wavelength of a hypothetical silicon LED, and the real reason silicon LEDs do not exist?

<details><summary>Solution</summary>

$\frac{1240}{1.12}=1107$ nm (infrared); and silicon's gap is indirect, so recombination emits phonons, not photons, efficiently.

</details>

#### Q19. Bias direction for a photodiode, and why?

<details><summary>Solution</summary>

Reverse: the widened depletion field sweeps photogenerated pairs out fast, and dark current stays small.

</details>

#### Q20. On the I-V plane, where does a solar cell deliver power?

<details><summary>Solution</summary>

The fourth quadrant: positive voltage, negative current (current out of the positive terminal).

</details>

#### Q21. $\alpha=0.95$: $\beta$?

<details><summary>Solution</summary>

$\frac{0.95}{0.05}=19$.

</details>

#### Q22. $I_B=50$ microamps, $\beta=100$, active mode: $I_C$ and $I_E$?

<details><summary>Solution</summary>

$I_C=5.0$ mA; $I_E=5.05$ mA.

</details>

#### Q23. $V_{CC}=5$ V, $R_C=1\ \text{k}\Omega$, $\beta=100$, $I_B=100\ \mu$A. Active or saturated?

<details><summary>Solution</summary>

$\beta I_B=10$ mA would need $V_{CE}=5-10=-5$ V: impossible, so saturated, $I_C\approx\frac{5-0.2}{1000}=4.8$ mA.

</details>

#### Q24. Phase of the common-emitter output relative to its input?

<details><summary>Solution</summary>

Inverted, 180 degrees.

</details>

#### Q25. NAND output for inputs 1 and 1?

<details><summary>Solution</summary>

0.

</details>

#### Q26. Verify De Morgan for A = 1, B = 0 on the first law.

<details><summary>Solution</summary>

$A\cdot B=0$, complement 1; $\overline A+\overline B=0+1=1$: equal.

</details>

#### Q27. Name a universal gate and the claim it must justify.

<details><summary>Solution</summary>

NAND (also NOR): every Boolean function can be built from NANDs alone.

</details>

#### Q28. Half adder with inputs 1 and 1: sum and carry?

<details><summary>Solution</summary>

S = 0, C = 1: binary 10.

</details>

## Part 7 · Alternate methods and the JEE-Advanced advantage toolkit

### 7.1 The decade ladder

Replace exponentials with the 60 mV ladder: one step per decade. Any "current at a new voltage" problem becomes addition. Demonstration: E5's three-decade climb. Fails far from 300 K (the step is $2.3kT/e$, so it grows with temperature) and near the knee where series resistance bends the ladder.

### 7.2 The mass-action seesaw

Doping fixes one carrier; the other follows $n_i^2$ divided by it. Demonstration: E3 and Q5 as one line each. Fails for degenerate doping ($N_d$ approaching $10^{25}$ m$^{-3}$) where the simple law bends.

### 7.3 The on-off assumption

For ideal-diode circuits: assume a state, solve, check consistency (forward needs positive current, reverse needs $V<0.6$ V). Demonstration: Q15's OR gate. Fails when two diodes fight; then compare their open-circuit drives.

### 7.4 The worst-case squeeze

Regulator and switch designs are two-inequality problems: minimum condition sets the lower bound, maximum condition sets the upper; a component exists only if the bounds overlap. Demonstration: E8's resistor between "enough at full load" and "safe at no load". This is the engineering habit JEE Advanced rewards.

### 7.5 The load-line picture

Any transistor question with a collector resistor: draw $V_{CE}=V_{CC}-I_CR_C$; the solution is where device physics meets the straight line. Saturation is simply the line's left wall. Demonstration: Q23 resolved in one line, no algebra needed.

### 7.6 The gap-to-colour conversion

$\lambda=1240/E_g$ both ways. Demonstration: E9. Memorise the anchors: 2 eV red, 2.3 eV green, 2.7 eV blue, 3.1 eV violet.

## Part 8 · Examiner traps

> [!danger] Trap 1 — holes as words only
> Saying holes "move" without the mechanism. Reply: the bond-swap picture — valence electrons shift one way, the vacancy travels the other, and the vacancy carries current as a real positive carrier.

> [!danger] Trap 2 — charged junction
> Claiming the depletion region carries net charge or the diode is charged. Reply: fixed ions on both sides balance; the region is depleted of mobile carriers, not of charge overall.

> [!danger] Trap 3 — charged crystal
> Saying n-type silicon is negative. Reply: every donated electron came from a donor ion; the crystal stays neutral.

> [!danger] Trap 4 — the zero-drop diode
> Using an ideal short where 0.7 V matters (low-voltage circuits, LED series resistors). Reply: keep the knee unless the supply dwarfs it.

> [!danger] Trap 5 — Zener as forward diode
> Wiring or analysing the Zener forward. Reply: it regulates in reverse breakdown, by design.

> [!danger] Trap 6 — beta in saturation
> Writing I-C = beta I-B when both junctions conduct. Reply: in saturation the external circuit sets I-C below beta I-B; test the mode first (Q23).

> [!danger] Trap 7 — invisible base current
> Ignoring I-B in power or node budgets. Reply: the base current is small, never zero, and it is what the driving stage must supply.

> [!danger] Trap 8 — power from nothing
> Saying the transistor creates energy. Reply: the supply provides it; the transistor is a valve.

> [!danger] Trap 9 — colour equals brightness
> Reading an LED's colour as its intensity. Reply: colour is the gap; brightness is the current and the efficiency.

> [!danger] Trap 10 — flat thermistor
> Assuming the thermistor's resistance is temperature-independent. Reply: its resistance-versus-temperature curve is the device's whole reason to exist.

## Part 9 · Playbook

### 9.1 Triage decision tree

- "Which class / temperature behaviour": mechanism table, §3.1.
- Carrier densities: mass-action seesaw, one line.
- Junction words (depletion, barrier, bias): hill picture, $W\propto\sqrt V$.
- Diode current at a voltage: decade ladder.
- Supply questions: rectifier averages, ripple formula, worst-case squeeze.
- Transistor: mode first (active or saturation test), then currents.
- Gates: truth table exhaustively; De Morgan for complements.

### 9.2 Formula map with validity

| Formula | Valid when | Breaks when |
|---|---|---|
| Eqs. (4.1) | equilibrium, non-degenerate | heavy doping, high field |
| Eq. (4.2) | hydrogenic dopant | deep levels, anisotropy (factor 1.7 in Si) |
| Eqs. (4.3) | ideality 1, below breakdown | high current, high T |
| Eqs. (4.4) | ripple small, constant I | discontinuous conduction |
| Eqs. (4.5) gain laws | active mode | saturation, cutoff |
| Eq. (4.6) | direct-gap emission | indirect gaps (Si, Ge) |

### 9.3 Constants to carry

$kT/e=25.9$ mV at 300 K; 60 mV/decade; $n_i$(Si) = $1.5\times10^{16}$ m$^{-3}$; $\mu_e/\mu_h=0.135/0.048$; gaps Si 1.12, Ge 0.66, GaAs 1.42, diamond 5.5 eV; knee 0.7 V (Si); $V_{CE,\text{sat}}\approx0.2$ V; $hc=1240$ eV nm; $\rho_i$(Si) $\approx2300\ \Omega$ m.

### 9.4 Timing plan

A and B under two minutes; C three; D twelve. Transistor questions die by algebra but live by mode-checking: decide the mode in twenty seconds before touching currents.

### 9.5 Pre-submission audit, ten points

1. Temperature behaviour attributed to the right mechanism.
2. Mass-action used in equilibrium only.
3. Neutrality honoured (no charged crystals).
4. Diode mode assumed and checked.
5. Ripple formula matched to half- or full-wave.
6. Zener analysed in reverse; both worst cases squeezed.
7. Transistor mode tested before applying beta.
8. LED gap and colour mutually consistent.
9. Truth tables exhaustive (all rows).
10. Every sub-part answered, units on numerics.

## Part 10 · Olympiad extension

### OL1 — Why a doped electron is bound by only tens of meV

Derive the donor ionisation energy by scaling the hydrogen ground state with the lattice dielectric constant $\kappa$ and the effective mass $m^*$; derive the orbit radius; compare with the measured Si:P value of 45 meV and account for the discrepancy honestly. Repeat the scaling argument for an acceptor in words.

<details><summary>Solution</summary>

**Method.** Hydrogen's energy scales as $m/\kappa^2$ (Coulomb weakened by $\kappa$, inertia set by $m^*$): $E_d=13.6\times\frac{0.26}{11.7^2}=26$ meV; radius scales as $\kappa/m^*$: $a^*=11.7\times0.053\ \text{nm}\times\frac{1}{0.26}=2.4$ nm — four lattice spacings, so the hydrogenic picture is geometrically legitimate. Measured 45 meV: the model is low by a factor 1.7 because silicon's conduction band has six valleys with anisotropic masses, which a single-mass hydrogen atom cannot see; the scale and the physics are right. An acceptor (hole bound to a negative core) scales the same way with the hole mass, giving slightly deeper levels, as measured. The punchline survives: 26 meV $\approx kT$ at 300 K, which is why doping works at room temperature at all.

**Checks.** (i) $E_d\ll E_g$, consistent with a shallow level just below the conduction band. (ii) $a^*$ many cells wide, consistent with treating the lattice as a continuum.

</details>

### OL2 — The diode equation from the Boltzmann factor

Derive $I=I_0(e^{V/V_T}-1)$ from the equilibrium of drift and diffusion across the junction, and explain in two lines why the reverse current is so small.

<details><summary>Solution</summary>

**Method.** In equilibrium the electron density obeys Boltzmann across the built-in hill: $n_p=n_ne^{-eV_0/kT}$. Under bias the hill becomes $V_0-V$, so the injection from n into p scales as $e^{-e(V_0-V)/kT}=e^{-eV_0/kT}e^{V/V_T}$: the diffusion current grows as $e^{V/V_T}$ against its equilibrium value. Subtracting equilibrium (net current zero at $V=0$) gives $I=I_0(e^{V/V_T}-1)$, with $I_0$ set by minority supply. Reverse bias can only remove the equilibrium injection; what remains is the drift of thermally generated minority carriers — few per diffusion length, hence nanoamps. The exponential's origin is the hill, and the hill is the Boltzmann factor: no separate postulate anywhere.

**Checks.** (i) $V=0$ gives $I=0$. (ii) Small forward $V$ recovers Ohm's law with slope $I_0/V_T$.

</details>

### OL3 — The junction capacitor and its inverse-square-root law

Show that the depletion width grows as the square root of total reverse voltage and that the junction capacitance falls as $V^{-1/2}$.

<details><summary>Solution</summary>

**Method.** Poisson across the depletion strip of width $W$ and ion density $N$: the field peaks at $E_{\max}=\frac{eNW}{\varepsilon}$ and the potential is the triangle area, $V_0+V=\frac12E_{\max}W$, giving $W=\sqrt{\frac{2\varepsilon(V_0+V)}{eN}}\propto\sqrt V$. The junction is a parallel-plate capacitor with that spacing: $C=\frac{\varepsilon A}{W}\propto(V_0+V)^{-1/2}$ — a capacitance you tune with voltage, the varactor (`capacitors/` supplies the definition; the junction supplies the voltage control).

**Checks.** (i) More reverse bias, wider strip, smaller C: varactor tuning works exactly this way. (ii) Units of the $W$ expression are metres.

</details>

### OL4 — Why a solar cell's efficiency is bounded

At order of magnitude, bound a single-junction cell's efficiency from the spectrum alone, and name the named limit.

<details><summary>Solution</summary>

**Method.** Photons below $E_g$ pass through unabsorbed: a gap too big wastes the red. Photons above $E_g$ give the cell only $E_g$ each, thermalising the excess: a gap too small wastes the blue. The two losses cross near $E_g\approx1.3$ eV; adding diode recombination losses gives the Shockley-Queisser bound of about 33 % for one junction under unconcentrated sunlight. Silicon at 1.12 eV sits near the optimum, which is why it rules the market; tandem stacks beat the bound by splitting the spectrum.

**Checks.** (i) The optimum gap 1.3 eV is of order the visible photon energy — consistent. (ii) Measured record cells approach but do not pass the bound.

</details>

### OL5 — The transistor as a thermometer

The base-emitter voltage at fixed collector current falls about 2 mV per kelvin. Use this to design a temperature readout, and state how the industry turns the same physics into a stable voltage reference.

<details><summary>Solution</summary>

**Method.** From the diode law at fixed $I$: $V_{BE}=V_T\ln\frac{I}{I_0}$; $V_T$ rises with $T$ while $I_0$ rises far faster, so $V_{BE}$ falls $\approx2$ mV/K — a junction thermometer read with a voltmeter. The bandgap reference exploits the split: one signal proportional to $V_T$ (rising, from a $\Delta V_{BE}$ of two matched transistors at different currents) added to one proportional to $V_{BE}$ (falling) in the right ratio gives a temperature-independent $\approx1.2$ V — the silicon bandgap voltage, hence the name. Every regulator's "1.25 V" is this trick.

**Checks.** (i) Signs: CTAT plus PTAT cancels. (ii) The reference magnitude is of order $E_g/e$: consistent.

</details>

### OL6 — The Hall measurement on a real sample

A slab of thickness 0.5 mm carries 10 mA in a 0.5 T field. The Hall voltage is 62 mV with the n-type polarity. Find the carrier density and type.

<details><summary>Solution</summary>

**Method.** Lorentz force deflects carriers until the Hall field balances it: $V_H=\frac{IB}{net}$, so $n=\frac{IB}{eV_Ht}=\frac{0.01\times0.5}{1.6\times10^{-19}\times0.062\times5\times10^{-4}}=1.0\times10^{21}$ m$^{-3}$. The voltage sign names the carriers: this polarity is electrons, n-type. This is PART 18's Hall effect applied to its canonical job — measuring a semiconductor.

**Checks.** (i) The density matches a one-per-million doping level: consistent with device-grade silicon. (ii) $R_H=\frac{1}{ne}=6.2\times10^{-3}$ m$^3$/C.

</details>

### OL7 — How small can a transistor be?

Estimate the quantum wall of Moore's law from the de Broglie wavelength and the uncertainty principle.

<details><summary>Solution</summary>

**Method.** A gate controls carriers through a barrier; when the barrier (gate oxide or channel length) thins to a few nanometres, the confined electron's momentum uncertainty $\Delta p\sim\frac{\hbar}{\Delta x}$ gives a kinetic spread $\frac{(\Delta p)^2}{2m}\approx1.5$ meV at 5 nm — comparable to the thermal smearing — and the tunnelling probability through a 1-2 nm oxide becomes order one, so "off" leaks. Carriers with de Broglie wavelengths of nanometres simply ignore a thinner wall. Practical scaling stalled in the few-nanometre regime exactly here; the industry's answer is geometry (fin gates, which squeeze the channel electrostatically), not thinner walls. PART 23's wave mechanics is the verdict; lithography merely executes it.

**Checks.** (i) 1.5 meV versus 26 meV thermal: confinement energy becomes a design number well before it dominates, so the estimate is an order statement, not a cliff. (ii) Reported tunnelling currents through 2 nm oxides are large, as the argument requires.

</details>

### OL8 — The noise floor of a photodiode receiver

The shot noise of a current $I$ in bandwidth $\Delta f$ is $i_{\text{rms}}=\sqrt{2eI\Delta f}$. For a dark-plus-signal current of 1 microamp and a 1 MHz bandwidth, how weak a signal current can you resolve?

<details><summary>Solution</summary>

**Method.** $i_{\text{rms}}=\sqrt{2\times1.6\times10^{-19}\times10^{-6}\times10^6}=5.7\times10^{-10}$ A: sub-nanoamp signals sit at the floor, and detection means keeping the photocurrent above this rms by a safety factor. Shot noise is Poisson statistics of charge quanta — PART 26's $\sqrt N$ counting in circuit clothing.

**Checks.** (i) Halving the bandwidth reduces noise by $\sqrt2$. (ii) Cooling reduces dark current, not the shot term of the signal itself.

</details>

### OL9 — Why an LED is not a resistor

Design the series resistor for a 2.0 V red LED at 20 mA from a 5 V supply, and explain from the steep I-V why the resistor is essential.

<details><summary>Solution</summary>

**Method.** $R=\frac{5-2.0}{0.020}=150\ \Omega$. Steepness: 60 mV changes current tenfold, so a 0.1 V supply sag or diode spread changes current by a factor $\sim40$; the resistor converts a voltage-driven device into an approximately current-driven one because most of the supply voltage falls across R, whose law is linear. Connecting the LED straight across 5 V is how LEDs die.

**Checks.** (i) Power in R: $0.06$ W, trivial. (ii) A 12 V supply wants $500\ \Omega$ — the same rule.

</details>

### OL10 — The shaded cell

One cell of a series-connected panel is shaded. Analyse the string's current and the shaded cell's fate, and explain the bypass diode's role.

<details><summary>Solution</summary>

**Method.** Series current is set by the weakest cell: the shaded one generates almost nothing, so the string current collapses toward that cell's dark limit, and the healthy cells drive their current backward through it — the shaded cell becomes a reverse-biased diode dissipating $I\times V$ as heat, a hotspot that can crack the panel. A bypass diode antiparallel to each cell block conducts when the block is shaded, letting the string current skip the dark block: the panel loses one block's voltage instead of all its power. Real engineering, elementary diode physics.

**Checks.** (i) Without bypass, power scales with the worst cell. (ii) With bypass, the I-V curve shows steps — one per block.

</details>

### OL11 — Why the chip needs a fan

Estimate a modern chip's dynamic power from $\frac12CV^2$ per gate per transition.

<details><summary>Solution</summary>

**Method.** $P=Nf\frac12CV^2$: with $N=10^9$ gates, $f=1$ GHz, $C=1$ fF, $V=1$ V: $P=\frac12\times10^{-15}\times1\times10^9\times10^9=500$ W — and real chips trade speed against this by lowering V, since power scales as $V^2$ while speed degrades gently. Half a kilowatt in a fingernail area is why packages carry heat spreaders and fans; it is also why the industry's voltage scaling mattered more than its speed scaling. The energy per transition equals the capacitor's stored energy (`capacitors/`), half delivered to the gate, half burned in the channel resistance.

**Checks.** (i) Halving V quarters the power — the industry's actual lever. (ii) Leakage (OL7's tunnelling) adds a static term at small nodes.

</details>

### OL12 — When does a device forget its doping?

An n-type silicon device is doped at $10^{21}$ m$^{-3}$. Estimate the temperature at which intrinsic carriers rival the doping, using the $T^{3/2}e^{-E_g/2kT}$ form anchored at 300 K.

<details><summary>Solution</summary>

**Method.** Need $n_i(T)=10^{21}$, a factor $6.7\times10^4$ above the 300 K value. Solving $(T/300)^{3/2}\exp\left[\frac{E_g}{2k}\left(\frac{1}{300}-\frac{1}{T}\right)\right]=6.7\times10^4$ gives $T\approx560$ K ($\sim290$ °C). Above it the sample reverts to intrinsic behaviour: the junction flattens, gain dies, and electronics built on doping stops working — the temperature ceiling of silicon technology, set by the same exponential that makes doping powerful.

**Checks.** (i) Automotive and aerospace silicon is derated well below this. (ii) Wide-gap materials (SiC, GaN) push the ceiling up by raising $E_g$, exactly as the formula predicts.

</details>

### 10.2 Limits and failure of the model

The hydrogenic donor model carries a factor-two uncertainty (valley structure); the ideality-1 diode law bends at high current (series resistance) and high temperature (generation current); the Shockley-Queisser bound assumes one junction and unconcentrated sunlight; the tunnelling-limit estimate is an order statement, not a threshold; mobility values depend on doping and temperature and are quoted here for lightly doped material at 300 K. Inside these fences the arithmetic is exact and the devices behave.

## Part 11 · Exam simulation — 36 questions, 200 marks, 180 minutes

Sections: A is 12 multiple-choice at 4 marks, B is 8 short-numerical at 4, C is 6 long-form at 5, D is 10 olympiad-style at 9. Carry: $V_T=26$ mV at 300 K, $n_i(\text{Si})=1.5\times10^{16}$ m$^{-3}$, $\mu_e=0.135$, $\mu_h=0.048$ m$^2$/Vs, $hc=1240$ eV nm unless overridden.

#### Section A · Concept MCQ (12 x 4)

### P1 · 4 marks
Heating a metal and heating intrinsic silicon:
(a) both resistances rise  (b) both fall  (c) metal rises, silicon falls  (d) metal falls, silicon rises

<details><summary>Answer</summary>

(c). Scattering dominates in the metal; carrier generation dominates in silicon (§3.1).

</details>

### P2 · 4 marks
A filled band cannot conduct because:
(a) it has no electrons  (b) electrons have no empty states to move into  (c) the gap is too small  (d) phonons block motion

<details><summary>Answer</summary>

(b). The full-lot argument of §3.2.

</details>

### P3 · 4 marks
Largest band gap among diamond, silicon, GaAs, germanium:
(a) silicon  (b) germanium  (c) GaAs  (d) diamond

<details><summary>Answer</summary>

(d), 5.5 eV.

</details>

### P4 · 4 marks
n-type Si with $N_d=10^{21}$ m$^{-3}$: hole density at 300 K is of order:
(a) $10^{21}$  (b) $10^{16}$  (c) $10^{11}$  (d) $10^6$ per m-cubed

<details><summary>Answer</summary>

(c). $n_i^2/N_d=2.25\times10^{11}$ (E3).

</details>

### P5 · 4 marks
The binding energy of a phosphorus donor electron in silicon is of order:
(a) 13.6 eV  (b) 1.1 eV  (c) 26 meV  (d) 26 micro-eV

<details><summary>Answer</summary>

(c). Scaled Bohr, Eq. (4.2).

</details>

### P6 · 4 marks
Forward biasing a p-n junction:
(a) raises the built-in hill  (b) lowers it  (c) widens the depletion region  (d) removes the fixed ions

<details><summary>Answer</summary>

(b), to $V_0-V$ (§3.6).

</details>

### P7 · 4 marks
A diode at 1 mA, 0.60 V carries at 0.72 V:
(a) 2 mA  (b) 20 mA  (c) 100 mA  (d) 1 A

<details><summary>Answer</summary>

(c). Two decades, 120 mV (E5).

</details>

### P8 · 4 marks
A full-wave rectifier on 60 Hz mains produces ripple at:
(a) 30 Hz  (b) 60 Hz  (c) 120 Hz  (d) zero

<details><summary>Answer</summary>

(c).

</details>

### P9 · 4 marks
A Zener diode regulates when biased:
(a) forward above the knee  (b) in reverse breakdown  (c) at zero bias  (d) in avalanche only, never Zener

<details><summary>Answer</summary>

(b).

</details>

### P10 · 4 marks
$\alpha=0.99$ gives $\beta$:
(a) 0.99  (b) 9.9  (c) 99  (d) 990

<details><summary>Answer</summary>

(c). $\frac{0.99}{0.01}=99$.

</details>

### P11 · 4 marks
A universal gate:
(a) AND  (b) OR  (c) XOR  (d) NAND

<details><summary>Answer</summary>

(d).

</details>

### P12 · 4 marks
An LED with gap 2.6 eV emits:
(a) red  (b) green  (c) blue  (d) infrared

<details><summary>Answer</summary>

(c). $\lambda=\frac{1240}{2.6}\approx477$ nm.

</details>

#### Section B · Short numerical (8 x 4)

### P13 · 4 marks
Compute the intrinsic conductivity and resistivity of silicon at 300 K from the standard data.

<details><summary>Answer</summary>

$\sigma=en_i(\mu_e+\mu_h)=4.4\times10^{-4}$ S/m; $\rho=2270\ \Omega$ m (E2).

</details>

### P14 · 4 marks
p-type Si, $N_a=5\times10^{21}$ m$^{-3}$: conductivity, using the hole mobility.

<details><summary>Answer</summary>

$\sigma=ep\mu_h=1.6\times10^{-19}\times5\times10^{21}\times0.048=38.4$ S/m.

</details>

### P15 · 4 marks
A diode carries 1 mA at 0.60 V. Current at 0.72 V?

<details><summary>Answer</summary>

100 mA (two 60 mV decades).

</details>

### P16 · 4 marks
Full-wave supply: 50 mA load, 50 Hz, $C=470\ \mu$F. Ripple?

<details><summary>Answer</summary>

$\Delta V=\frac{0.05}{2\times50\times470\times10^{-6}}=1.06$ V.

</details>

### P17 · 4 marks
Zener: 9 V supply, $V_Z=5.1$ V, load to 30 mA, keep 5 mA minimum in the diode. Series resistor?

<details><summary>Answer</summary>

$R=\frac{9-5.1}{0.035}=111\ \Omega$.

</details>

### P18 · 4 marks
A green LED emits at 550 nm. Its gap?

<details><summary>Answer</summary>

$E_g=\frac{1240}{550}=2.25$ eV.

</details>

### P19 · 4 marks
$\beta=150$, $I_B=40\ \mu$A, active mode: $I_C$, $I_E$?

<details><summary>Answer</summary>

$I_C=6.0$ mA; $I_E=6.04$ mA.

</details>

### P20 · 4 marks
Hall measurement: 10 mA through a 0.5 mm slab in 0.5 T gives 31 mV. Carrier density?

<details><summary>Answer</summary>

$n=\frac{IB}{eV_Ht}=\frac{0.005}{1.6\times10^{-19}\times0.031\times5\times10^{-4}}=2.0\times10^{21}$ m$^{-3}$.

</details>

#### Section C · Long form (6 x 5)

### P21 · 5 marks
Silicon doped with $N_d=2\times10^{21}$ m$^{-3}$. Find n, p, $\sigma$, $\rho$, and the conductivity gain over intrinsic.

<details><summary>Answer</summary>

$n\approx2\times10^{21}$; $p=\frac{2.25\times10^{32}}{2\times10^{21}}=1.1\times10^{11}$ m$^{-3}$; $\sigma=en\mu_e=43.2$ S/m; $\rho=0.023\ \Omega$ m; gain $\approx\frac{43.2}{4.4\times10^{-4}}\approx10^5$.

</details>

### P22 · 5 marks
The donor estimate. (a) Derive the scaled-Bohr energy. (b) Evaluate for Si:P and its orbit radius. (c) Compare with 45 meV and explain the mismatch honestly; why does room temperature ionise donors anyway?

<details><summary>Answer</summary>

(a) $E_d=13.6(m^*/m)/\kappa^2$ (OL1). (b) 26 meV; $a^*=2.4$ nm. (c) Factor 1.7 from valley anisotropy; 26 meV equals $kT$, so thermal agitation ionises nearly all donors regardless of the exact value.

</details>

### P23 · 5 marks
(a) Explain how diffusion creates the depletion region and the equilibrium condition. (b) Show $W\propto\sqrt{V_0+V}$. (c) With $V_0=0.7$ V, the capacitance factor when reverse bias rises from 1 V to 8 V?

<details><summary>Answer</summary>

(a) Majority diffusion leaves fixed ions; their field drives opposing drift; equilibrium when drift cancels diffusion (§3.6). (b) OL3's triangle-area argument. (c) $\frac{C_2}{C_1}=\sqrt{\frac{0.7+1}{0.7+8}}=\sqrt{\frac{1.7}{8.7}}=0.44$.

</details>

### P24 · 5 marks
Design a full-wave supply: 12 V peak transformer, load 120 mA, ripple at most 0.5 V, 50 Hz. (a) DC output without diode drops. (b) Smoothing capacitor. (c) Ripple frequency.

<details><summary>Answer</summary>

(a) $\frac{2\times12}{\pi}=7.64$ V. (b) $C=\frac{0.12}{100\times0.5}=2400\ \mu$F. (c) 100 Hz.

</details>

### P25 · 5 marks
$V_{CC}=10$ V, $R_C=2\ \text{k}\Omega$, $\beta=100$, $I_B=50\ \mu$A. (a) Active or saturated? Give $I_C$. (b) Redesign the base resistor from a 5 V logic output for a 2 mA drive.

<details><summary>Answer</summary>

(a) $\beta I_B=5$ mA would force $V_{CE}=10-10=0$: the load line's wall — saturated, $I_C\approx\frac{10-0.2}{2000}=4.9$ mA. (b) $R_B=\frac{5-0.7}{0.002}=2.15\ \text{k}\Omega$.

</details>

### P26 · 5 marks
(a) Verify the half adder's table. (b) Prove the first De Morgan law by exhaustive rows. (c) Build NOT from a single NAND.

<details><summary>Answer</summary>

(a) E12. (b) Rows of $A\cdot B$ complemented match $\overline A+\overline B$ for 00, 01, 10, 11. (c) Tie both NAND inputs together: $\overline{A\cdot A}=\overline A$.

</details>

#### Section D · Olympiad style (10 x 9)

### P27 · 9 marks
The diode equation's origin. (a) Derive $I=I_0(e^{V/V_T}-1)$ from the Boltzmann factor across the hill. (b) Why is the reverse current tiny? (c) At fixed 0.60 V, the exponential factor when $V_T$ doubles?

<details><summary>Answer</summary>

(a) OL2: injection scales as $e^{V/V_T}$ against equilibrium; subtract equilibrium. (b) Reverse bias leaves only thermally generated minority carriers. (c) $e^{0.60/0.026}\approx1.2\times10^{10}$ falls to $e^{0.60/0.052}\approx1.1\times10^5$: at fixed voltage the exponential factor shrinks — though the rising $I_0$ (OL12 physics) dominates in practice, which is the subtlety worth naming.

</details>

### P28 · 9 marks
Donors across materials. Derive the binding energy and radius for GaAs ($\kappa=12.9$, $m^*=0.067m$) and compare with silicon's 26 meV and 2.4 nm.

<details><summary>Answer</summary>

$E_d=13.6\times\frac{0.067}{12.9^2}=5.5$ meV — five times shallower; $a^*=12.9\times0.053/0.067=10.2$ nm, four times wider. Small mass plus large dielectric constant: GaAs donors barely exist, which is why modulation doping works there — the honesty line about the model's material dependence.

</details>

### P29 · 9 marks
Junction capacitance from first principles. (a) Derive W and $C\propto V^{-1/2}$. (b) With $\varepsilon=11.7\varepsilon_0$, $N=10^{21}$ m$^{-3}$, $V_0=0.7$ V, reverse bias 4.3 V, area 1 mm-squared: W and C.

<details><summary>Answer</summary>

(a) OL3. (b) $W=\sqrt{\frac{2\times1.04\times10^{-10}\times5.0}{1.6\times10^{-19}\times10^{21}}}=2.5\ \mu$m; $C=\frac{\varepsilon A}{W}=\frac{1.04\times10^{-10}\times10^{-6}}{2.5\times10^{-6}}=41$ pF — a voltage-tunable capacitor.

</details>

### P30 · 9 marks
The solar bound. (a) State the two spectral losses. (b) Why the optimum single gap is near 1.3 eV and the bound about 33 %. (c) Why silicon dominates anyway, and what beats the bound.

<details><summary>Answer</summary>

(a) Sub-gap transmission; above-gap thermalisation (OL4). (b) The losses cross near 1.3 eV; recombination completes the 33 % Shockley-Queisser ceiling. (c) Si at 1.12 eV sits near the optimum with unmatched cost and maturity; tandem junctions beat the bound by dividing the spectrum.

</details>

### P31 · 9 marks
Moore's wall. (a) The uncertainty-principle energy at 3 nm confinement. (b) The tunnelling argument for thin oxides. (c) The industry's workaround.

<details><summary>Answer</summary>

(a) $\frac{\hbar^2}{2m(\Delta x)^2}\approx4.2$ meV, approaching thermal scales. (b) Barriers of 1-2 nm transmit carriers with order-one probability, so "off" leaks (OL7). (c) Geometry: fin gates and new channel materials squeeze electrostatics instead of thinning walls.

</details>

### P32 · 9 marks
Shot-noise design. (a) State $i_{\text{rms}}=\sqrt{2eI\Delta f}$ and its Poisson origin. (b) Evaluate for 4 microamp, 2 MHz. (c) The minimum detectable photocurrent at signal-to-noise one.

<details><summary>Answer</summary>

(a) Charge arrives in quanta; Poisson variance gives the rms. (b) $\sqrt{2\times1.6\times10^{-19}\times4\times10^{-6}\times2\times10^6}=1.6$ nA. (c) $\approx1.6$ nA at SNR 1; real receivers demand a factor of several — the noise floor is the budget, not the bill.

</details>

### P33 · 9 marks
The Hall experiment complete. (a) Derive $V_H=\frac{IB}{net}$. (b) For 10 mA, 0.5 T, 0.5 mm, measured 62 mV: density and type. (c) How would the reading change for a p-type sample at the same density?

<details><summary>Answer</summary>

(a) Lorentz deflection balanced by the Hall field (OL6). (b) $n=1.0\times10^{21}$ m$^{-3}$, n-type by polarity. (c) Same magnitude, opposite sign: the voltmeter names the carriers.

</details>

### P34 · 9 marks
The junction thermometer. (a) Why $V_{BE}$ falls about 2 mV per kelvin at fixed current. (b) The bandgap-reference construction from CTAT and PTAT parts. (c) The expected reference magnitude.

<details><summary>Answer</summary>

(a) $V_{BE}=V_T\ln(I/I_0)$ with $I_0$ rising faster than $V_T$ (OL5). (b) Add a $\Delta V_{BE}$-derived rising term to the falling $V_{BE}$ in the cancelling ratio. (c) About 1.2 V — the silicon gap voltage, by design and by name.

</details>

### P35 · 9 marks
The shaded panel. (a) Series-string current under one shaded cell. (b) The shaded cell's electrical fate without protection. (c) The bypass diode's action and the visible signature on the I-V curve.

<details><summary>Answer</summary>

(a) String current collapses toward the shaded cell's dark limit (OL10). (b) It becomes a reverse-biased dissipator: hotspot. (c) Antiparallel diodes let current skip shaded blocks; the curve shows one voltage step per bypassed block.

</details>

### P36 · 9 marks
The chip's heat. (a) Derive the per-gate switching energy. (b) Estimate for $C=0.5$ fF, $V=0.9$ V, $f=2$ GHz, $2\times10^9$ gates. (c) Why voltage scaling mattered more than frequency scaling.

<details><summary>Answer</summary>

(a) $\frac12CV^2$ per transition, half stored, half burned (`capacitors/`). (b) $2.0\times10^{-16}$ J per switch; total $\approx810$ W. (c) Power scales as $V^2$: halving the supply quarters the bill, while frequency only scales it linearly — the industry's actual history, and the fan's origin.

</details>

## Part 12 · Marking scheme and rubric

Section A (4 each): 4 marks for the correct option with a one-line reason; 2 for a right answer without reasoning.

Section B (4 each): 2 for the setup (formula plus substituted data), 2 for the number with units; missing units cap at 2.

Section C (5 each): 1 for the picture (junction, load line, circuit), 2 for the method, 2 for the result with stated assumptions; the worst-case line earns the fifth when the method was compressed.

Section D (9 each): typically three sub-parts at 3 marks. Derivations: 1 for the governing expression, 1 for the algebra, 1 for the limit or honesty check. Estimates: 1 for the model, 1 for the arithmetic, 1 for what the model neglects. The donor problem must carry the factor-1.7 honesty line; the diode-equation problem must name the Boltzmann origin; the solar problem must name both spectral losses. Answers that apply beta in saturation lose their numerical marks even with correct arithmetic.

General: mode before algebra (transistor, diode); equilibrium stated before using the mass-action law; ripple formula matched to the rectifier type. These three omissions are the chapter's signature penalties.

## Part 13 · Links across the course

- PART 23 (photoelectric effect and dual nature): $E_g=\frac{hc}{\lambda}$ runs the LED and photodiode colour logic; the de Broglie wavelength and uncertainty principle set Moore's wall (OL7); shot noise (OL8) is the photon-arrival story translated to charge quanta.
- PART 24 (atomic structure): the donor estimate is the hydrogen atom rescaled by the lattice — the chapter's deepest cross-topic derivation; effective mass is the band's answer to the Bohr radius.
- PART 26 (nuclear physics): the Poisson discipline of $\sqrt N$ counting reappears as shot noise; exponential thinking (decades per step) is the same muscle as decay halving.
- `current-electricity/`: resistivity, drift velocity and the $J$-$E$ language the conductivity formula speaks; the metal-versus-semiconductor temperature contrast is its sequel.
- `capacitors/`: the junction capacitance, the varactor, the ripple capacitor and the $\frac12CV^2$ switching energy are all capacitor physics wearing device costumes.
- PART 18 (Cyclotron and Hall Effect, to be shipped): OL6 and P20/P33 are its canonical laboratory application — measuring carrier type and density in a real sample.
- Forward: P7 (communication systems) inherits the diode as detector and mixer, and the transistor as amplifier; modulation without these valves is just arithmetic.

## Part 14 · Sources and review checklist

Primary floor: the JEE Main/Advanced semiconductor syllabus, since no chapter exists in the supplied Cengage volumes (verified: *Optics and Modern Physics* Unit II holds only chs 3-5; the other volumes were checked for a stray chapter per plan.md §1.13 and contain none). The treatment follows the NCERT Class-12 sequence (classification, doping, junction, devices, logic) at JEE-Advanced depth, with the olympiad layer added by sweep.

Review checklist before the exam:
1. The mechanism table (§3.1) survives a swapped-statement trap.
2. Mass-action and neutrality each take one line, cold.
3. The donor scaling reproduces 26 meV and 2.4 nm with the honesty line.
4. The decade ladder and the knee story are fluent.
5. Ripple and Zener formulas carry their worst-case conditions.
6. Alpha-beta bookkeeping plus the saturation test resolve any transistor circuit.
7. De Morgan and the half adder are writable without a reference table.
8. The five olympiad stories (donor, diode origin, capacitance, solar bound, Moore's wall) each open with one sentence.
