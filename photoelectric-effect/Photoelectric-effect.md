---
title: Photons, Photoelectric Effect & Matter Waves
part: 23
slug: photoelectric-effect
source: Cengage Optics and Modern Physics, ch 3 Photoelectric Effect (pp. 3.1-3.41)
aliases: [photoelectric effect, photons, matter waves, de Broglie]
tags: [jee-advanced, olympiad, modern-physics, quantum]
---

# Photons, Photoelectric Effect & Matter Waves — first principles to Olympiad

> [!abstract] How to use this chapter
> Three passes. Pass 1: Parts 0-4 for the physics (crisis, photon, Einstein equation, matter waves, uncertainty). Pass 2: Parts 5-9 for exam craft (exemplars, archetypes, traps, playbook). Pass 3: Parts 10-14 for the Olympiad layer, the paper, the sheet and the checkpoint. Every numerical answer in this file was recomputed; every boxed result carries its validity condition.

## Part 0 · Orientation

### 0.1 What you will be able to do

After this chapter you can: read off Planck's constant and a work function from a stopping-potential graph; count photons per second from a lamp's power; predict the stopping potential for any metal and wavelength; compute the de Broglie wavelength of an electron, a neutron or a cricket ball; derive the angular-momentum quantisation $L=n\hbar$ from a standing-wave condition; estimate the size and energy of the hydrogen atom from the uncertainty principle; and decide, for any situation, whether the wave picture or the photon picture is the one that pays.

### 0.2 The one idea

Light delivers its energy in indivisible packets of size $hf$, and matter waves are the same fact seen from the other side: anything with momentum $p$ has a wavelength $\lambda=\frac{h}{p}$. Every surprise in this chapter — the threshold frequency, the instantaneous emission, the electron microscope, the stability of atoms — is a consequence of those two lines.

### 0.3 Prerequisite self-check

Answer these before reading; the answers are in the fold.

1. What is the energy of a photon of wavelength $620$ nm, in eV?
2. A particle of charge $e$ falls through a potential difference of $V$ volts. What kinetic energy does it gain?
3. State the classical (wave) expression for the intensity of light in terms of the field amplitude $E_0$.
4. What does the Poynting vector tell you about a light beam, and where does its momentum story live in this vault?
5. A body at temperature $T$ radiates. How does the total radiated power scale with $T$, and where in the vault is that derived?
6. Write the kinetic energy of a non-relativistic particle in terms of its momentum.
7. What is the condition for a standing wave on a circle of radius $r$?

<details><summary>Solution</summary>

1. $E=\frac{1240}{620}=2.0$ eV, using $hc\approx1240$ eV nm.
2. $K=eV$, i.e. numerically $V$ electron-volts.
3. $I=\frac{1}{2}\varepsilon_0 c E_0^2$; intensity is set by amplitude, not frequency.
4. It carries the energy flux; the momentum flux and radiation pressure are owned by [[Electromagnetic-waves]], quoted here as $p=\frac{E}{c}$ per photon.
5. $P\propto T^4$ (Stefan's law), derived in [[Heat]] and [[Thermodynamics]].
6. $K=\frac{p^2}{2m}$.
7. An integer number of wavelengths fits the circumference: $2\pi r=n\lambda$.

</details>

### 0.4 Numbers to keep

> [!abstract] Numbers to keep
> $hc=1240$ eV nm (exactly $1239.84$). $h=6.626\times10^{-34}$ J s $=4.136\times10^{-15}$ eV s. $\hbar=1.055\times10^{-34}$ J s. $e=1.602\times10^{-19}$ C. $m_e=9.109\times10^{-31}$ kg. Electron wavelength $\lambda=\frac{1.226}{\sqrt{V}}$ nm for accelerating voltage $V$ in volts. Compton wavelength of the electron $\lambda_C=\frac{h}{m_ec}=2.426$ pm. $a_0=0.529$ Å. Visible band $400$-$700$ nm $=3.1$-$1.8$ eV. Work functions: Cs $2.14$ eV, Na $2.28$ eV, Zn $4.3$ eV, Cu $4.7$ eV, Pt $6.35$ eV.

### 0.5 Three passes

Pass 1 reads Parts 0-4 straight through; do not skip the validity ledger. Pass 2 works every exemplar and practice question by hand before opening the fold. Pass 3 sits the paper under timed conditions, then uses Part 12 as a diagnostic.

### 0.6 Cengage coverage map

The sweep read the chapter 3 contents page of the committed PDF (*Optics and Modern Physics*, pp. v-vii). Every heading appears below with a status; nothing is quoted from the book, all derivations and numbers are original.

| Cengage section (ch 3) | What it establishes | Where it lives here | Status |
|---|---|---|---|
| Quantum theory of light (3.2) | energy quanta, photon bookkeeping | §3.4, §4.1 | derived |
| Properties of photons (3.2) | $E=hf$, $p=\frac{h}{\lambda}$, zero rest mass | §2.1, §3.4, §4.1 | derived |
| Photon counts per second (3.2) | $n=\frac{P}{hf}$ | §3.4, E2, Q3 | derived |
| Intensity of light due to a source (3.2) | $I=\frac{P}{4\pi r^2}$ as photon flux | §3.4, §3.6 | derived |
| Photon flux (3.3) | photons per area per second | §2.1, §3.4 | derived |
| Photon density in a beam (3.4) | $n_{\text{vol}}=\frac{I}{hfc}$ | §3.4, Q5 | derived |
| Force exerted by a light beam (3.4) | $F=\frac{P}{c}$ absorbed, $\frac{2P}{c}$ reflected | §3.4, E6, OL10 | derived |
| Radiation pressure/force (3.5) | momentum flux picture | §3.4, §4.1, hand-off to [[Electromagnetic-waves]] | stated + used |
| Matter waves (3.10) | $\lambda=\frac{h}{p}$ | §3.7, §4.1 | derived |
| Properties of matter waves (3.11) | not a mechanical wave; $\lambda\to0$ classically | §2.5, §3.11 | derived |
| Applications of de Broglie hypothesis (3.11) | electron optics, Davisson-Germer | §3.8, §3.10, §3.12 | extended beyond book |
| Electron emission (3.14) | thermionic, photoelectric, field emission | §2.4, §3.5 | stated + used |
| Photoelectric cell and applications (3.15) | the device and its uses | §1.2, §3.12 | stated + used |
| Study of photoelectric effect (3.16) | apparatus and the five facts | §3.2, §3.3 | derived |
| Einstein's photoelectric equation (3.16) | $K_{\max}=hf-\phi$ | §3.5, §4.1 | derived |
| Laws of photoelectric effect (3.17) | the three empirical laws | §3.2, §3.6 | derived |
| Failure of classical wave theory (3.17) | the waiting-time argument | §3.3, OL1 | extended beyond book |
| Solved examples band (3.21) | standard problem shapes | archetypes in §6.1, Q1-Q28 | exercised |
| Exercise types (subjective, objective, multiple-correct, assertion-reasoning, comprehension, matching, integer, archives) | exam formats | mirrored in Part 11 sections A-D | exercised |
| Blackbody crisis and Planck (added by sweep) | where the quantum began | §3.1 | added by sweep |
| Uncertainty principle and hydrogen estimate (added by sweep) | $\Delta x\Delta p\gtrsim\frac{\hbar}{2}$; $a_0$ from it | §3.9, OL3 | added by sweep |
| Wave packet, phase and group velocity (added by sweep) | $v_g=v_{\text{particle}}$ | §3.9, OL2 | added by sweep |

## Part 1 · Intuition first

### 1.1 Light as a rain of packets

Stand in rain and in drizzle made from the same water. The drizzle wets you slowly because fewer drops arrive per second, not because each drop is smaller. Classical light is like a mist that can be made arbitrarily fine: the wave theory says the energy arrives continuously, spread over the wavefront, so a dim light should take a long time to deliver a fixed amount of energy to a small target. The photoelectric effect says otherwise: even light so dim that the wave picture predicts hours of waiting ejects electrons within nanoseconds. The resolution is that light is not a mist. It is a rain of indivisible drops, each carrying $hf$. A dim beam is fewer drops per second, never smaller drops.

### 1.2 The turnstile

A photon counter is a turnstile that only opens for a coin of exactly the right size. A metal surface holds its electrons behind an energy toll $\phi$, the work function. An arriving photon pays the toll with its whole energy $hf$ or not at all — it cannot be split between two electrons, and two photons cannot pool their coins in the ordinary (single-photon) effect. If $hf<\phi$ the turnstile never opens, however many photons arrive: that is the threshold frequency, and it is the single most anti-classical fact in the chapter. If $hf>\phi$, the change comes back as kinetic energy of the electron, at most $K_{\max}=hf-\phi$, reduced further for electrons that start below the surface.

### 1.3 Everyday anchors

Three machines on your street already use this chapter. A solar-powered garden light and a photodiode door sensor use the photoelectric effect: one photon lifts one electron over a gap. Night-vision equipment runs a photomultiplier, a chain of surfaces where one photon becomes a measurable avalanche of electrons. An electron microscope uses the other half of the chapter, matter waves: accelerated electrons have wavelengths a hundred thousand times shorter than visible light, so they resolve what light cannot.

> [!info] Why the particle picture did not kill the wave picture
> Interference and diffraction of light are real and are owned by [[Wave-optics]] and [[Electromagnetic-waves]]. The photon does not replace the wave; the two pictures answer different questions. Energy exchange is granular; propagation is wavelike. §3.11 makes this a decision table.

## Part 2 · Definitions and bookkeeping

### 2.1 The symbol table

| Symbol | Meaning | SI unit | Notes |
|---|---|---|---|
| $f$ | frequency of the light | Hz | $f=\frac{c}{\lambda}$ in vacuum |
| $\lambda$ | wavelength | m | use nm for light, pm for X-rays |
| $E_{\text{ph}}=hf$ | energy of one photon | J or eV | $=\frac{1240}{\lambda\,[\text{nm}]}$ eV |
| $p_{\text{ph}}=\frac{h}{\lambda}$ | momentum of one photon | kg m/s | $=\frac{E}{c}$ |
| $\phi$ | work function of the metal | eV | surface-dependent, tabulated |
| $K_{\max}$ | maximum kinetic energy of photoelectrons | eV | electrons from the very surface |
| $V_s$ | stopping potential | V | $eV_s=K_{\max}$ |
| $f_0=\frac{\phi}{h}$ | threshold frequency | Hz | below it, no emission at any intensity |
| $n$ | photon flux, photons per m$^2$ per s | m$^{-2}$ s$^{-1}$ | $n=\frac{I}{hf}$ |
| $I$ | intensity | W/m$^2$ | classical: $\frac{1}{2}\varepsilon_0 cE_0^2$ |
| $\lambda_{\text{dB}}=\frac{h}{p}$ | de Broglie wavelength of matter | m | any object with momentum |

### 2.2 Units and the eV habit

The electron-volt is the energy an electron gains falling through one volt: $1\ \text{eV}=1.602\times10^{-19}$ J. In atomic-scale problems always convert to eV first; the number $hc=1240$ eV nm then makes every conversion one division. Wavelengths in nm, energies in eV, voltages in V: with this convention the stopping potential in volts equals the kinetic energy in eV numerically.

> [!warning] Condition of validity
> $K=eV$ numerically in eV only because the charge is exactly $e$. For an alpha particle falling through $V$ the energy is $2eV$, i.e. $2V$ electron-volts. Carry the charge factor explicitly.

### 2.3 Sign conventions and frames

All energies in the photoelectric bookkeeping are positive magnitudes: $\phi>0$, $K_{\max}\ge0$, $V_s\ge0$. The stopping potential is the retarding potential of the collector that just reduces the current to zero; we quote its magnitude. Work functions are quoted for clean polycrystalline surfaces; a real surface's $\phi$ shifts with coatings, which is why exam tables state their own values.

### 2.4 Assumptions of the model

The Einstein bookkeeping assumes: (i) one photon transfers all of $hf$ to one electron; (ii) the transfer is a single event, hence instantaneous; (iii) $\phi$ is a fixed surface property; (iv) electrons deeper than the surface lose energy on the way out, which is why $K_{\max}$ refers to surface electrons; (v) the quantum efficiency (electrons out per photon in) is small but irrelevant to the energy bookkeeping. Electron emission by other means — thermionic (heat), field emission (strong field) — exists and is mentioned in Cengage ch 3; this chapter uses photoelectric emission only.

### 2.5 What is NOT in this model

No multi-photon absorption (it exists, with intense pulsed lasers; §10 flags it). No band structure: metals are treated with a single $\phi$, semiconductors with a gap in [[semiconductors]]-style language later (PART 27). No relativistic electrons: photoelectron speeds here are far below $c$; the check is $K\ll m_ec^2=511$ keV. No question of which slit or interpretation: §3.10 states where that is studied, not here.

> [!question] Exam note
> JEE Advanced loves the graph form: $V_s$ against $f$ for two metals, or photocurrent against collector voltage for two intensities. If you can redraw both from memory with slopes and intercepts labelled, half the paper is already done.

## Part 3 · Core derivations

### 3.1 The crisis before the quantum

A hot body emits a smooth curve of radiation: little at long wavelength, a peak, then a fall at short wavelength. Classical physics, counting standing waves in a cavity and giving each the average energy $kT$, predicts instead an intensity growing like $\frac{1}{\lambda^4}$ without bound as $\lambda\to0$ — the ultraviolet catastrophe, infinite power radiated in the ultraviolet. The measured curve does not diverge; it peaks and dies.

Two scaling facts were known before the fix. Stefan's law, $P=\sigma T^4$, says the total power grows like the fourth power of temperature (derived thermodynamically in [[Thermodynamics]]). Wien's displacement law says the peak wavelength slides inversely with temperature:

$$
\lambda_{\max}T=b,\qquad b=2.898\times10^{-3}\ \text{m K}. \qquad (3.1)
$$

Wien's law follows from a scaling argument: if the spectrum has the form $u(\lambda,T)=\lambda^{-5}F(\lambda T)$, then the peak condition $\frac{du}{d\lambda}=0$ forces $\lambda_{\max}T$ to be a constant, whatever the unknown function $F$ is. Planck's 1900 fix was to assume the cavity walls exchange energy with the field only in lumps $E_n=nhf$. The honest historical caveat: in 1900 what was quantised was the *exchange* at the walls, not the light in flight. Einstein's 1905 photoelectric paper is what made the lump a real object — the photon.

> [!abstract] DIAGRAM D23.1 · The blackbody family of curves
> *Show:* intensity against wavelength for three temperatures $T_1<T_2<T_3$; each curve rising from zero, peaking, and falling; the peaks joined by a dashed hyperbola $\lambda_{\max}T=b$; a dotted curve labelled "classical $\lambda^{-4}$" diverging at short wavelength; the visible band shaded.
> *Search:* "blackbody radiation curves Wien displacement ultraviolet catastrophe classical divergence"
> *Used in:* §3.1 and Q1.

### 3.2 The experimental facts and the classical predictions they destroy

The apparatus is an evacuated tube with two electrodes: an emitter plate (the metal under test) and a collector. Light of chosen frequency falls on the emitter; a variable battery pushes the collector positive (accelerating photoelectrons) or negative (retarding them); a sensitive ammeter reads the photocurrent.

> [!abstract] DIAGRAM D23.2 · The photoelectric apparatus
> *Show:* evacuated glass tube; emitter plate E lit by a monochromatic beam entering a quartz window; collector C opposite; a variable supply with a reversing switch; a microammeter in series and a voltmeter across the tube; arrows showing electrons crossing when the collector is positive.
> *Search:* "photoelectric effect experiment apparatus stopping potential circuit diagram"
> *Used in:* §3.2, §3.5, §3.6.

The five facts, each against the wave prediction:

| Fact | Observation | Classical wave prediction |
|---|---|---|
| Threshold | no emission below $f_0$, at any intensity | energy accumulates continuously, so bright light of any $f$ should eject |
| Instantaneity | emission within $\lesssim10^{-9}$ s even for dim light | dim light should need minutes to hours (§3.3) |
| Current vs intensity | photocurrent $\propto$ intensity, at fixed $f$ | correct, the one thing waves get right |
| $K_{\max}$ vs frequency | $K_{\max}$ grows linearly with $f$, independent of intensity | $K$ should grow with amplitude, i.e. intensity |
| Stopping potential | $V_s$ independent of intensity, linear in $f$ | $V_s$ should grow with intensity |

> [!info] Why the current being proportional to intensity is not a victory for waves
> In the photon picture, doubling intensity at fixed $f$ doubles the photon flux $n=\frac{I}{hf}$, hence doubles the electron rate. The wave picture predicts the same proportionality, so this single fact cannot discriminate. The discriminators are the threshold, the instantaneity, and the intensity-independence of $V_s$.

### 3.3 The classical waiting time, derived

Give the wave picture its best numbers. Take a very dim beam, $I=10^{-3}$ W/m$^2$ (moonlit-night order). An absorbing atom presents an area of order $A\approx(10^{-10}\ \text{m})^2=10^{-20}$ m$^2$. Power intercepted: $P=IA=10^{-23}$ W. To collect the $2$ eV $=3.2\times10^{-19}$ J needed to escape:

$$
t=\frac{\phi}{IA}=\frac{3.2\times10^{-19}}{10^{-23}}\approx3.2\times10^{4}\ \text{s}\approx9\ \text{hours}. \qquad (3.2)
$$

At an even dimmer $I=10^{-8}$ W/m$^2$ the wait is $\sim3\times10^{9}$ s, of order a century. The experiment shows electrons arriving within nanoseconds of switching the light on, with no warm-up at any intensity. This single calculation — energy spread over a wavefront cannot be hoarded fast enough by one atom — is the most convincing destroyer of the classical picture in the chapter.

> [!abstract] DIAGRAM D23.3 · Photocurrent versus collector voltage
> *Show:* current on the vertical axis, collector voltage on the horizontal from negative to positive; two curves at the same frequency, intensities $I$ and $2I$: both start at zero current at the same negative voltage $-V_s$, rise, and flatten at different saturation plateaux; a third dashed curve at a frequency below threshold lying flat on the zero axis.
> *Search:* "photoelectric effect current voltage graph stopping potential saturation two intensities"
> *Used in:* §3.5, §3.6, Q8.

### 3.4 The photon and its bookkeeping

One photon of frequency $f$ carries

$$
E=hf=\frac{hc}{\lambda}=\frac{1240\ \text{eV nm}}{\lambda\ [\text{nm}]}, \qquad (3.3)
$$

and, because a massless relativistic particle has $E=pc$, a momentum

$$
p=\frac{E}{c}=\frac{h}{\lambda}. \qquad (3.4)
$$

> [!quote] Hand-off
> Eq. (3.4) as a *derivation* from $E^2=(pc)^2+(mc^2)^2$ with $m=0$ belongs to PART 28 (special relativity). Here it is an experimental input: Compton scattering (§25 of this vault, PART 25) verifies it. The radiation-pressure and Poynting-flux machinery is owned by [[Electromagnetic-waves]].

A beam of power $P$ and frequency $f$ is a stream of $\frac{P}{hf}$ photons per second. Spread over a sphere of radius $r$ from a source, the intensity is $I=\frac{P}{4\pi r^2}$ and the photon flux is

$$
n=\frac{I}{hf}\quad[\text{photons per m}^2\text{ per s}]. \qquad (3.5)
$$

Inside the beam, photons travel at $c$, so the number per unit volume is the flux divided by $c$:

$$
n_{\text{vol}}=\frac{I}{hfc}. \qquad (3.6)
$$

When the beam stops on a surface, each photon hands over momentum $\frac{h}{\lambda}$; a beam of power $P$ therefore pushes with force $F=\frac{P}{c}$ if absorbed and $F=\frac{2P}{c}$ if reflected straight back. That is radiation pressure, $p_{\text{rad}}=\frac{I}{c}$ for absorption — the same result [[Electromagnetic-waves]] obtains from Maxwell's stress, here obtained by counting coins.

> [!abstract] DIAGRAM D23.4 · One photon, one electron
> *Show:* a metal surface drawn as a row of atoms with electrons; one wavy arrow labelled $hf$ arriving at one electron; the electron leaving with an arrow labelled $K_{\max}=hf-\phi$; a second panel showing two photons of $hf<\phi$ arriving and nothing leaving, with a cross over a pooled-arrow.
> *Search:* "photoelectric effect one photon one electron work function diagram"
> *Used in:* §3.4, §3.5.

### 3.5 Einstein's equation and the stopping potential

An electron at the very surface, paying the minimum toll $\phi$, keeps the most change:

$$
K_{\max}=hf-\phi. \qquad (3.7)
$$

Electrons from deeper lose extra energy in collisions on the way out, so $K_{\max}$ is a *maximum*; the spectrum of emitted electrons runs from $0$ to $K_{\max}$. Retarding the collector until even the fastest electron turns back defines the stopping potential:

$$
eV_s=K_{\max}=hf-\phi\quad\Longrightarrow\quad V_s=\frac{h}{e}f-\frac{\phi}{e}. \qquad (3.8)
$$

> [!abstract] DIAGRAM D23.5 · $K_{\max}$ versus frequency for two metals
> *Show:* $K_{\max}$ on the vertical axis, $f$ on the horizontal; two straight lines for cesium and zinc, both with the same slope $\frac{h}{e}$, crossing the $f$-axis at their threshold frequencies $f_0^{\text{Cs}}<f_0^{\text{Zn}}$; the common slope annotated $\frac{h}{e}$; the vertical intercepts $-\phi$ marked on the dashed backward extension.
> *Search:* "photoelectric effect kinetic energy frequency graph slope h/e two metals work function"
> *Used in:* §3.5, E4, Q10.

Eq. (3.8) is the measurement of Planck's constant: the slope of $V_s$ against $f$ is $\frac{h}{e}$ for *every* metal, and the horizontal intercept is $f_0=\frac{\phi}{h}$. Millikan's decade of such graphs confirmed Einstein's line and measured $h$ to agree with the blackbody value — the decisive cross-check that one quantum governs both phenomena.

> [!warning] Condition of validity
> Eq. (3.7) needs $hf\ge\phi$; below threshold the right side is negative and simply means no emission. It also assumes single-photon absorption and a clean surface with a single $\phi$.

> [!info] Why saturation is not a quantum effect
> At large positive collector voltage every emitted electron is swept across, so the current equals the emission rate — a geometric collection limit. Saturation therefore tells you the electron rate (hence the photon rate), not anything about energy quanta.

### 3.6 Three independent knobs

| Knob turned up | Photocurrent | $K_{\max}$ and $V_s$ | Photon story |
|---|---|---|---|
| Intensity at fixed $f$ | up, proportional | unchanged | more photons, same energy each |
| Frequency at fixed $I$ | slightly down (fewer photons per watt) | up, linearly | fewer but richer photons |
| Collector voltage | rises then saturates | $V_s$ marks the cutoff | collection efficiency, not emission |

The second row is the subtle one: at fixed intensity, raising $f$ means *fewer* photons per second, so the current actually falls a little while $V_s$ climbs. Any exam statement that current must rise with frequency is testing whether you track photon number and photon energy separately.

### 3.7 de Broglie's hypothesis

Einstein attached a momentum $\frac{h}{\lambda}$ to a quantum of light. de Broglie proposed the mirror image: any particle with momentum $p$ carries a wavelength

$$
\lambda=\frac{h}{p}. \qquad (3.9)
$$

For an electron accelerated from rest through $V$ volts, $K=eV=\frac{p^2}{2m_e}$, so $p=\sqrt{2m_e eV}$ and

$$
\lambda=\frac{h}{\sqrt{2m_e eV}}=\frac{1.226\ \text{nm}}{\sqrt{V\ [\text{V}]}}. \qquad (3.10)
$$

Numbers: $54$ V gives $0.167$ nm; $100$ V gives $0.123$ nm; $10$ kV gives $0.0123$ nm. A thermal particle at temperature $T$ has a typical momentum $p\sim\sqrt{3mk_BT}$, so a neutron at room temperature ($k_BT\approx25$ meV) has $\lambda\approx1.8$ Å — atomic scale, which is why thermal neutrons diffract from crystals (PART 26 will use this). A $0.15$ kg cricket ball at $30$ m/s has $\lambda\sim10^{-34}$ m: no interface in the universe has slits that fine, so the ball shows no wave behaviour. The classical world is the $\lambda\ll$ geometry limit.

> [!abstract] DIAGRAM D23.6 · de Broglie wavelength across the world
> *Show:* a log axis of wavelength from $10^{-34}$ m to $1$ m with five labelled markers: cricket ball, running person, thermal neutron (1.8 Å), 100 V electron (0.12 nm), X-ray band; a shaded band "atomic spacings 0.1-1 nm" overlapping only the neutron and electron markers.
> *Search:* "de Broglie wavelength scale macroscopic electron neutron atomic spacing"
> *Used in:* §3.7, Q12.

### 3.8 The Bohr orbit as a standing wave

Demand that the matter wave on a circular orbit close on itself in phase: circumference $=$ integer wavelengths,

$$
2\pi r=n\lambda=n\frac{h}{p}\quad\Longrightarrow\quad pr=n\frac{h}{2\pi}=n\hbar. \qquad (3.11)
$$

But $pr$ *is* the angular momentum $L$ of a circular orbit. Therefore $L=n\hbar$: Bohr's quantisation postulate is not magic, it is the condition for the electron's wave not to interfere with itself destructively. This is the bridge to PART 24, which takes Eq. (3.11) plus the Coulomb force and derives the whole hydrogen atom.

> [!abstract] DIAGRAM D23.7 · The standing wave on the n = 3 orbit
> *Show:* a circle with a sinusoidal wave drawn along it, exactly three wavelengths fitting the circumference; a second circle where a non-integer number of wavelengths fails to meet in phase, marked with a cross; radii labelled.
> *Search:* "Bohr orbit standing wave de Broglie three wavelengths constructive interference"
> *Used in:* §3.8, Q15.

### 3.9 Wave packets and the uncertainty principle

A pure sine wave has a perfect wavelength and hence a perfect momentum — but it is spread over all space, so its position is completely unknown. A localised particle is a packet, a superposition of sines; Fourier analysis says a packet of spatial extent $\Delta x$ requires a spread of wave numbers $\Delta k\gtrsim\frac{1}{\Delta x}$. With $p=\hbar k$,

$$
\Delta x\,\Delta p\gtrsim\frac{\hbar}{2}. \qquad (3.12)
$$

> [!abstract] DIAGRAM D23.8 · A wave packet and its two spreads
> *Show:* top panel: a localised envelope of oscillation with width $\Delta x$ marked; bottom panel: the amplitude in $k$-space, a bump of width $\Delta k\sim\frac{1}{\Delta x}$; a double arrow between the panels labelled "narrow in one, wide in the other".
> *Search:* "wave packet position momentum uncertainty Fourier spread"
> *Used in:* §3.9, OL3.

The principle is not a statement about clumsy measurement; it is a statement about waves. Three payoffs, each used later in the vault:

1. **The atom does not collapse.** Confine the electron to radius $r$ and $p\gtrsim\frac{\hbar}{r}$, so its energy is

$$
E(r)\approx\frac{\hbar^2}{2m_er^2}-\frac{ke^2}{r}. \qquad (3.13)
$$

The kinetic term climbs as $r$ shrinks; minimising, $\frac{dE}{dr}=0$ gives $r=\frac{\hbar^2}{m_ek e^2}=a_0=0.529$ Å and $E_{\min}=-\frac{m_ek^2e^4}{2\hbar^2}=-13.6$ eV. The uncertainty principle alone predicts the size and binding energy of hydrogen to within the precision of this estimate. Squeezing the electron toward the nucleus costs more kinetic energy than the Coulomb well repays — there is a floor, and it is the ground state.

2. **A confined particle has a minimum energy.** In a box of size $L$, $K_{\min}\approx\frac{\hbar^2}{2mL^2}$; this zero-point energy is why helium never freezes at ordinary pressure and why nuclei, being tiny boxes, make their nucleons so energetic (PART 26).

3. **Spectral lines have a natural width.** An excited state lives a finite time $\tau$, so its energy is uncertain by $\Delta E\sim\frac{\hbar}{\tau}$, and every line it emits is broadened by that amount (§10, OL4).

> [!abstract] DIAGRAM D23.9 · The hydrogen atom as a balance of two curves
> *Show:* energy against radius $r$; a positive curve $\frac{\hbar^2}{2m_er^2}$ falling steeply, a negative curve $-\frac{ke^2}{r}$ rising toward zero, and their sum with a clear minimum at $a_0$ marked by a dot at $-13.6$ eV.
> *Search:* "hydrogen atom ground state uncertainty principle energy minimum Bohr radius"
> *Used in:* §3.9, OL3.

### 3.10 Davisson-Germer and electron diffraction

If electrons are waves of $\lambda=\frac{h}{p}$, a crystal — a three-dimensional grating with spacings of order $1$ Å — should diffract them. Davisson and Germer fired electrons at nickel and measured the scattered intensity against angle. At $54$ V the detector at $65^\circ$ from the incident beam saw a strong peak. Treating the nickel planes as a grating of spacing $d=0.91$ Å and using the glancing-angle condition $2d\sin\theta=n\lambda$ (derived fully in PART 25), the $n=1$ prediction is $\lambda=2(0.91)\sin65^\circ=1.65$ Å $=0.165$ nm, against de Broglie's $\frac{1.226}{\sqrt{54}}=0.167$ nm. Agreement within the experimental scatter: matter waves are real. The same logic now runs as LEED (low-energy electron diffraction) in every surface-science lab, and double-slit experiments with electrons build up interference fringes one dot at a time — each dot a single electron arriving whole, the ensemble a wave pattern.

> [!abstract] DIAGRAM D23.10 · Davisson-Germer geometry
> *Show:* an electron gun aimed at a nickel crystal; parallel atomic planes drawn inside the crystal with spacing $d$; the incident beam and the detector arm at $65^\circ$; the extra path $2d\sin\theta$ highlighted between two reflected rays; a polar plot of intensity against angle with the $65^\circ$ lobe.
> *Search:* "Davisson Germer experiment nickel crystal diffraction 65 degrees diagram"
> *Used in:* §3.10, Q18.

> [!abstract] DIAGRAM D23.11 · Double slit with electrons, one dot at a time
> *Show:* three panels of the same screen after 100, 3000 and 100000 electrons: scattered dots, emerging bands, sharp fringes; the slit plane drawn to the left; a note that each dot is one whole electron.
> *Search:* "electron double slit experiment single electron buildup interference fringes"
> *Used in:* §3.10.

> [!question] Exam note
> What happens if you measure which slit each electron used? The fringes disappear. The *physics of why* is interpretation-level quantum mechanics and is outside this syllabus; the examinable fact is complementarity: path information and interference are mutually exclusive.

### 3.11 Which model, when?

| Question asked | Use | Because |
|---|---|---|
| Energy exchanged with matter (emission, absorption, thresholds) | photon | exchange is granular, $hf$ at a time |
| Propagation, interference, diffraction, polarisation | wave | superposition of amplitudes |
| Where is the particle and how localised? | wave packet + Eq. (3.12) | localisation costs momentum spread |
| Macroscopic limit, $\lambda\ll$ every dimension | either, wave reduces to ray | fringes too fine to see |

The symmetry statement to memorise: $E=hf$ and $p=\frac{h}{\lambda}$ connect the particle words (energy, momentum) to the wave words (frequency, wavelength) in *both* directions — for light and for matter alike.

### 3.12 Where the pictures pay: instruments

**Electron microscope.** Resolution is limited by wavelength to roughly $\lambda$. Light at $550$ nm resolves about $300$ nm; electrons at $10$ kV have $\lambda=0.0123$ nm, a factor $4.5\times10^4$ finer in principle (lens aberrations keep the practical gain smaller, but still enormous).

**LEED.** Slow electrons (tens of eV) have wavelengths of a few Å and penetrate only a few atomic layers, so their diffraction reads *surfaces*. The counterintuitive fact: slower electrons, longer wavelengths, and the long wavelength is exactly what makes them surface-sensitive and strongly diffracted.

**Photomultiplier.** One photon ejects one photoelectron; that electron is accelerated into a dynode and knocks out several; ten stages give $\sim10^6$ gain — single photons become visible pulses.

**Photovoltaic threshold.** A solar cell with gap $E_g$ uses only photons with $hf>E_g$; the surplus above the gap is lost as heat, which is why one junction cannot use the whole solar spectrum (PART 27 owns the device physics).

**Laser, one page.** Stimulated emission makes an incoming photon clone itself off an excited atom; a population inversion (more excited than ground, impossible in thermal equilibrium) makes cloning beat absorption; two mirrors make a pass count many times. Einstein's 1917 coefficients are the quantitative core (§10, OL6).

> [!abstract] DIAGRAM D23.12 · The photomultiplier dynode chain
> *Show:* a photon striking the first photocathode, one electron arcing to dynode 1, three electrons to dynode 2, nine to dynode 3, the cascade widening to an anode pulse; each stage labelled with its gain.
> *Search:* "photomultiplier tube dynode cascade single photon detection diagram"
> *Used in:* §3.12.

> [!abstract] DIAGRAM D23.13 · Photon energy-wavelength conversion chart
> *Show:* a horizontal band of the electromagnetic spectrum from radio to gamma with a dual scale: wavelength in m on top, photon energy in eV below; the visible band shaded with 1.8-3.1 eV labelled; markers at 1240 nm = 1 eV and 0.124 nm = 10 keV.
> *Search:* "photon energy wavelength chart electromagnetic spectrum electron volt"
> *Used in:* §3.4 and Part 13.

> [!abstract] DIAGRAM D23.14 · The electron microscope's wavelength advantage
> *Show:* two panels: a light microscope column with a 550 nm wave drawn coarse, and an electron column at 100 kV with a 3.7 pm wave drawn fine; the same specimen feature of 0.1 nm shown unresolved in the first panel and sharp in the second; magnetic lens coils sketched.
> *Search:* "electron microscope resolution wavelength comparison light microscope diagram"
> *Used in:* §3.12 and OL12.

> [!abstract] DIAGRAM D23.15 · A LEED pattern
> *Show:* a fluorescent screen with a symmetric array of bright spots on a dark background; the spot spacing annotated as inversely proportional to the surface lattice spacing; a low-energy electron gun at the centre.
> *Search:* "LEED low energy electron diffraction pattern spots surface"
> *Used in:* §3.12.

> [!abstract] DIAGRAM D23.16 · Three-level laser pumping scheme
> *Show:* three horizontal levels E1, E2, E3; an upward pump arrow E1 to E3, a fast non-radiative drop E3 to E2, the long-lived E2 holding population, and a stimulated arrow E2 to E1 drawn as two identical photons leaving; the inversion between E2 and E1 bracketed.
> *Search:* "three level laser pumping scheme population inversion diagram"
> *Used in:* §3.12 and OL6.

## Part 4 · Results, limits and the validity ledger

### 4.1 Boxed results

$$
\boxed{E=hf=\frac{1240}{\lambda[\text{nm}]}\ \text{eV}} \qquad (4.1)
$$

valid for any photon, always.

$$
\boxed{p=\frac{h}{\lambda}=\frac{E}{c}} \qquad (4.2)
$$

valid for massless quanta; verified by Compton scattering (PART 25).

$$
\boxed{K_{\max}=hf-\phi,\qquad eV_s=K_{\max}} \qquad (4.3)
$$

valid for $hf\ge\phi$, single-photon absorption, non-relativistic electrons.

$$
\boxed{\lambda=\frac{h}{p},\qquad \lambda_e=\frac{1.226}{\sqrt{V}}\ \text{nm}} \qquad (4.4)
$$

the second form valid for electrons with $eV\ll511$ keV; beyond that use the relativistic momentum (error exceeds 1 % near $V\approx3$ kV, §10).

$$
\boxed{\Delta x\,\Delta p\gtrsim\frac{\hbar}{2}} \qquad (4.5)
$$

valid always; a property of waves, not of instruments.

### 4.2 Limit checks

- $f\to f_0$: $K_{\max}\to0$ and $V_s\to0$, the threshold, correct.
- $I\to0$ at fixed $f$: current vanishes but $V_s$ unchanged — dim light, same coin size, correct.
- $V\to\infty$ in Eq. (4.4): $\lambda\to0$, rays, classical mechanics returns, correct.
- $m\to\infty$ at fixed $v$: $\lambda\to0$, cricket balls are classical, correct.
- $h\to0$ (the formal classical limit): threshold frequency vanishes, waiting time vanishes, the wave paradoxes dissolve into the classical world, correct.

### 4.3 Which formula when

| You are given | You need | Use |
|---|---|---|
| $\lambda$ of light | photon energy | Eq. (4.1) |
| power and $\lambda$ | photons per second | $n=\frac{P}{hc/\lambda}$ |
| metal and $\lambda$ | $V_s$ | Eq. (4.3) |
| $V_s$-$f$ graph | $h$ and $\phi$ | slope $\frac{h}{e}$, intercept $f_0$ |
| accelerating voltage | electron $\lambda$ | Eq. (4.4) |
| beam power on mirror | force | $F=\frac{2P}{c}$ |
| confinement size | minimum energy | $E\approx\frac{\hbar^2}{2mL^2}$ |

### 4.4 Correspondence to the next simplest case

When the photon number in a beam is astronomical — a $1$ W beam at $550$ nm carries $2.8\times10^{18}$ photons per second — the grain is invisible and the wave description of [[Electromagnetic-waves]] is exact for propagation. The photon never contradicts the wave; it refines the bookkeeping of exchange.

### 4.5 Twenty-second checks

**C1 — concept check.** A $2$ eV photon and a $4$ eV photon: which has the longer wavelength, and by what factor?

<details><summary>Answer</summary>

The $2$ eV one, twice as long: $\lambda=\frac{1240}{E}$.

</details>

**C2 — concept check.** Below the threshold frequency, what does increasing the intensity do to the emission?

<details><summary>Answer</summary>

Nothing: no single photon can pay the toll, and photons do not pool.

</details>

**C3 — concept check.** Which is larger: the stopping potential for bright red light above threshold, or for dim blue light above threshold?

<details><summary>Answer</summary>

Dim blue: $V_s$ follows frequency, not intensity.

</details>

**C4 — concept check.** An electron and a proton fall through the same voltage. Which has the longer de Broglie wavelength?

<details><summary>Answer</summary>

The electron: same $p$? No — same energy, smaller mass, smaller $p=\sqrt{2mK}$, longer $\lambda$.

</details>

**C5 — concept check.** What happens to the photon flux at fixed intensity when the frequency doubles?

<details><summary>Answer</summary>

It halves: same power carried in twice-as-rich coins.

</details>

**C6 — concept check.** True or false: the saturation current proves light is quantised.

<details><summary>Answer</summary>

False: saturation is geometric collection of every emitted electron.

</details>

**C7 — concept check.** If the uncertainty principle were false, what would hydrogen do?

<details><summary>Answer</summary>

Collapse: $E(r)$ has no floor without the $\frac{\hbar^2}{2mr^2}$ term.

</details>

**C8 — concept check.** A wave packet is squeezed narrower in space. What happens to its momentum spread?

<details><summary>Answer</summary>

It widens: $\Delta p\gtrsim\frac{\hbar}{2\Delta x}$.

</details>

**C9 — concept check.** Slower electrons diffract more strongly or less strongly from a crystal, and why in one clause?

<details><summary>Answer</summary>

More strongly: smaller $p$ means longer $\lambda$, closer to the lattice spacing.

</details>

**C10 — concept check.** What single number tells you whether the non-relativistic electron-wavelength formula is safe?

<details><summary>Answer</summary>

$\frac{eV}{511\ \text{keV}}$; below about $10^{-2}$ the error is under a percent.

</details>

**C11 — concept check.** A mirror reflects a beam. Compared with absorption, the force is?

<details><summary>Answer</summary>

Doubled: each photon's momentum change is $2\frac{h}{\lambda}$.

</details>

**C12 — concept check.** The phase velocity of a matter wave exceeds $c$. Does any measurable thing exceed $c$?

<details><summary>Answer</summary>

No: energy, momentum and information travel at the group velocity $=v$.

</details>

**C13 — concept check.** An excited state lives $10^{-8}$ s. Order of its energy width in eV?

<details><summary>Answer</summary>

$\sim10^{-7}$ eV: $\Delta E\approx\frac{\hbar}{\tau}$.

</details>

**C14 — concept check.** In the standing-wave picture, what is special about $n=1$?

<details><summary>Answer</summary>

One wavelength fits the orbit: the smallest angular momentum $\hbar$, the ground state.

</details>

## Part 5 · Worked exemplars

### E1 — How many photons leave a sodium lamp per second?

A $100$ W sodium lamp radiates (idealising) all of its power at $589$ nm. Find the photon energy in eV and the emission rate.

> [!success] Check
> The rate must scale linearly with power and inversely with wavelength; doubling the power doubles the count.

<details><summary>Solution</summary>

**Method.** Convert with $hc=1240$ eV nm, then divide power by energy-per-photon in joules.

$E=\frac{1240}{589}=2.11$ eV $=2.11\times1.602\times10^{-19}=3.37\times10^{-19}$ J.

$N=\frac{P}{E}=\frac{100}{3.37\times10^{-19}}=2.97\times10^{20}$ photons per second.

</details>

### E2 — Stopping potential for sodium at 400 nm

Sodium has $\phi=2.28$ eV. Light of $400$ nm falls on it. Find $K_{\max}$ and $V_s$.

> [!success] Check
> At the threshold $\lambda_0=\frac{1240}{2.28}=544$ nm; $400$ nm is shorter, so emission must occur, and $K_{\max}$ must be positive.

<details><summary>Solution</summary>

**Method.** Einstein equation in eV, then $V_s=K_{\max}$ numerically.

$K_{\max}=\frac{1240}{400}-2.28=3.10-2.28=0.82$ eV, so $V_s=0.82$ V.

</details>

### E3 — Threshold wavelength for zinc

Zinc has $\phi=4.3$ eV. What is the longest wavelength that can eject electrons?

> [!success] Check
> A larger work function must give a shorter threshold wavelength than sodium's $544$ nm.

<details><summary>Solution</summary>

**Method.** Set $K_{\max}=0$: $\lambda_0=\frac{1240}{\phi}=\frac{1240}{4.3}=288$ nm, deep in the ultraviolet — zinc needs UV, which is why visible light never discharges a zinc plate.

</details>

### E4 — Reading h and the work function off a graph

A $V_s$ against $f$ line for some metal passes through $(5.0\times10^{14}\ \text{Hz},\,0\ \text{V})$ and $(11.0\times10^{14}\ \text{Hz},\,2.48\ \text{V})$. Extract $h$ and $\phi$.

> [!success] Check
> The slope must equal $\frac{h}{e}\approx4.14\times10^{-15}$ V s for every metal; a different value means a misread graph.

<details><summary>Solution</summary>

**Method.** Slope is $\frac{h}{e}$, intercept on the $f$-axis is $f_0$.

Slope $=\frac{2.48-0}{(11.0-5.0)\times10^{14}}=4.13\times10^{-15}$ V s, so $h=e\times4.13\times10^{-15}=6.62\times10^{-34}$ J s. Threshold $f_0=5.0\times10^{14}$ Hz, so $\phi=hf_0=4.13\times10^{-15}\times5.0\times10^{14}=2.07$ eV.

</details>

### E5 — de Broglie wavelengths at 100 V and 10 kV

Compute the electron wavelength for accelerating voltages $100$ V and $10^4$ V.

> [!success] Check
> Ten times the voltage must shrink $\lambda$ by $\sqrt{100}=10$, since $10^4=100\times100$.

<details><summary>Solution</summary>

**Method.** Eq. (4.4): $\lambda=\frac{1.226}{\sqrt{V}}$ nm.

$V=100$: $\lambda=0.123$ nm. $V=10^4$: $\lambda=0.0123$ nm. The ratio is exactly $10$, as the square-root scaling demands.

</details>

### E6 — The push of a one-watt mirror

A $1$ W laser beam reflects straight back from a perfect mirror. Find the force, and the mass whose weight it equals.

> [!success] Check
> Reflection must give twice the absorbed force; the equivalent mass must be of order a microgram, which is why light pressure is invisible at kitchen scale.

<details><summary>Solution</summary>

**Method.** Momentum change per second $=\frac{2P}{c}$.

$F=\frac{2\times1}{3.0\times10^{8}}=6.7\times10^{-9}$ N. Equivalent mass $m=\frac{F}{g}=6.8\times10^{-10}$ kg $=0.68$ µg.

</details>

### E7 — Photon flux two metres from a lamp

A $100$ W isotropic source (all at $550$ nm) is $2$ m away. Find the intensity and the photon flux on a small detector facing it.

> [!success] Check
> Doubling the distance must quarter the flux; the inverse-square law is geometry, not optics.

<details><summary>Solution</summary>

**Method.** Spread the power over a sphere, then count photons.

$I=\frac{100}{4\pi(2)^2}=1.99$ W/m$^2$. Photon energy $2.25$ eV $=3.61\times10^{-19}$ J. Flux $n=\frac{1.99}{3.61\times10^{-19}}=5.5\times10^{18}$ photons per m$^2$ per second.

</details>

### E8 — The classical waiting time in numbers

A dim beam of $I=10^{-3}$ W/m$^2$ shines on a surface whose atoms present $10^{-20}$ m$^2$. How long would the wave picture need to accumulate $2$ eV? Compare with the observed nanosecond response.

> [!success] Check
> The answer must grow as $\frac{1}{I}$; at sunlight intensity ($10^3$ W/m$^2$) the same estimate gives milliseconds, still far above the observed instantaneity at dim light.

<details><summary>Solution</summary>

**Method.** Power into one atom times time equals the work function.

$P=IA=10^{-23}$ W; $t=\frac{3.2\times10^{-19}\ \text{J}}{10^{-23}\ \text{W}}=3.2\times10^{4}$ s $\approx9$ hours, against an observed delay below $10^{-9}$ s: thirteen orders of magnitude of disagreement.

</details>

### E9 — Minimum energy of an electron confined to an atom-sized box

Confine an electron to $L=0.1$ nm. Estimate the minimum kinetic energy the uncertainty principle forces on it.

> [!success] Check
> A smaller box must give a larger energy, as $\frac{1}{L^2}$; a nuclear-sized box ($10^{-15}$ m) gives MeV energies, anticipating PART 26.

<details><summary>Solution</summary>

**Method.** Take $p\approx\frac{\hbar}{L}$ and $K=\frac{p^2}{2m}$.

$K\approx\frac{(1.055\times10^{-34})^2}{2\times9.109\times10^{-31}\times(10^{-10})^2}=6.1\times10^{-19}$ J $=3.8$ eV. Atomic electrons are unavoidably energetic; confinement is why they do not sit still.

</details>

### E10 — Two intensities, one stopping potential

Light of frequency $f$ ejects electrons with $V_s=1.5$ V at intensity $I$. The intensity is tripled at the same $f$. What are the new $V_s$ and the new saturation current?

> [!success] Check
> Any answer that changes $V_s$ with intensity contradicts §3.6 and is an automatic exam trap.

<details><summary>Solution</summary>

**Method.** Intensity changes photon number, not photon energy.

$V_s$ stays $1.5$ V. The emission rate triples, so the saturation current triples.

</details>

### E11 — The Davisson-Germer angle

Electrons accelerated through $54$ V diffract from nickel planes of spacing $d=0.91$ Å. Find the glancing angle of the first-order peak.

> [!success] Check
> Raising the voltage shortens $\lambda$ and must shrink the angle; the $1.65$ Å wavelength and $65^\circ$ are the historic pair.

<details><summary>Solution</summary>

**Method.** $\lambda=\frac{1.226}{\sqrt{54}}=0.167$ nm $=1.67$ Å; Bragg $2d\sin\theta=\lambda$.

$\sin\theta=\frac{1.67}{2\times0.91}=0.918$, $\theta=66^\circ$, within a degree of the observed $65^\circ$ lobe (the small gap is the textbook rounding of $d$).

</details>

### E12 — Hydrogen from the uncertainty principle, numerically

Evaluate $E(r)=\frac{\hbar^2}{2m_er^2}-\frac{ke^2}{r}$ at $r=0.5$ Å and confirm the atom-scale balance.

> [!success] Check
> The sum must sit near $-13.6$ eV; the kinetic term alone at this radius must be of order $+15$ eV, showing the squeeze cost.

<details><summary>Solution</summary>

**Method.** Two substitutions.

Kinetic: $\frac{(1.055\times10^{-34})^2}{2\times9.109\times10^{-31}\times(0.5\times10^{-10})^2}=2.44\times10^{-18}$ J $=15.3$ eV. Potential: $-\frac{(8.99\times10^9)(1.602\times10^{-19})^2}{0.5\times10^{-10}}=-4.61\times10^{-18}$ J $=-28.8$ eV. Sum $=-13.5$ eV, the ground state to the precision of the estimate.

</details>

## Part 6 · Problem archetypes and practice

### 6.1 Archetypes

| # | Archetype | Template (one line) | Where worked | Variations |
|---:|---|---|---|---|
| 1 | Photon energy from wavelength | $E=\frac{1240}{\lambda}$ eV | Q2, E1 | give $f$ instead; give eV, ask $\lambda$ |
| 2 | Photons per second from power | $N=\frac{P}{hf}$ | E1, Q3 | laser in mW; lamp with efficiency |
| 3 | Stopping potential | $eV_s=hf-\phi$ | E2, Q6 | change metal; change $\lambda$ |
| 4 | Threshold wavelength | $\lambda_0=\frac{1240}{\phi}$ | E3, Q4 | ask threshold frequency |
| 5 | Max speed of photoelectron | $v=\sqrt{\frac{2K}{m_e}}$ | Q7 | ask momentum instead |
| 6 | Work function from a graph | intercept $\times\frac{h}{e}$ | E4, Q10 | slope given, read $\phi$; two-metal comparison |
| 7 | Electron wavelength at voltage | $\lambda=\frac{1.226}{\sqrt{V}}$ nm | E5, Q11 | proton, alpha, neutron versions |
| 8 | Photon momentum and beam force | $F=\frac{P}{c}$ or $\frac{2P}{c}$ | E6, Q19 | partial reflection coefficient |
| 9 | Standing wave in an orbit | $2\pi r=n\lambda$ | Q15, §3.8 | give $n$, ask $r$ with Bohr input |
| 10 | Box minimum energy | $K\approx\frac{\hbar^2}{2mL^2}$ | E9, Q16 | proton in a nucleus-sized box |
| 11 | Crystal diffraction angle | $2d\sin\theta=n\lambda$ | E11, Q18 | higher orders; solve for $d$ |
| 12 | Flux and distance | $n=\frac{P}{4\pi r^2 hf}$ | E7, Q23 | pupil area; detector area |
| 13 | Current from quantum efficiency | $I=\eta e\frac{P}{hf}$ | Q9 | give current, ask $\eta$ |
| 14 | Two metals, same light | $K_1-K_2=\phi_2-\phi_1$ | Q20, Q26 | two wavelengths, same metal |
| 15 | Classical waiting time | $t=\frac{\phi}{IA}$ | E8, OL1 | vary intensity by decades |
| 16 | Scaling without algebra | $\lambda\propto\frac{1}{\sqrt{V}}$, $N\propto\frac{P}{f}$ | Q12, Q21 | factor-of changes only |

### 6.2 In-flow practice

#### Q1. A body at $300$ K radiates like a blackbody. Where is its peak?

<details><summary>Solution</summary>

**Method.** Wien's law, Eq. (3.1). $\lambda_{\max}=\frac{2.898\times10^{-3}}{300}=9.7\times10^{-6}$ m $=9.7$ µm, in the infrared — the band thermal cameras see.

</details>

#### Q2. What is the energy, in eV, of a $620$ nm photon?

<details><summary>Solution</summary>

**Method.** $E=\frac{1240}{620}=2.0$ eV.

</details>

#### Q3. A $1$ mW helium-neon laser emits at $633$ nm. How many photons per second?

<details><summary>Solution</summary>

**Method.** $E=\frac{1240}{633}=1.96$ eV $=3.14\times10^{-19}$ J; $N=\frac{10^{-3}}{3.14\times10^{-19}}=3.2\times10^{15}$ s$^{-1}$.

</details>

#### Q4. A surface has $\phi=2.3$ eV. Find the threshold frequency.

<details><summary>Solution</summary>

**Method.** $f_0=\frac{\phi}{h}=\frac{2.3}{4.136\times10^{-15}}=5.6\times10^{14}$ Hz.

</details>

#### Q5. A $550$ nm beam has intensity $1$ W/m$^2$. What is the photon number density in the beam?

<details><summary>Solution</summary>

**Method.** $n_{\text{vol}}=\frac{I}{hfc}$ with $hf=3.61\times10^{-19}$ J: $n_{\text{vol}}=\frac{1}{3.61\times10^{-19}\times3\times10^8}=9.2\times10^{9}$ m$^{-3}$. Sparse — photons are light packets, not a dense fluid.

</details>

#### Q6. Copper has $\phi=4.7$ eV. Find $V_s$ for $200$ nm light.

<details><summary>Solution</summary>

**Method.** $K_{\max}=\frac{1240}{200}-4.7=6.2-4.7=1.5$ eV; $V_s=1.5$ V.

</details>

#### Q7. A photoelectron has $K=2.0$ eV. What is its speed?

<details><summary>Solution</summary>

**Method.** $v=\sqrt{\frac{2K}{m_e}}=\sqrt{\frac{2\times3.204\times10^{-19}}{9.109\times10^{-31}}}=8.4\times10^{5}$ m/s, about $0.3\%$ of $c$: safely non-relativistic.

</details>

#### Q8. In the photocurrent-voltage graph, two curves at intensities $I$ and $2I$ (same $f$) meet the voltage axis at the same point. Name that point and explain the meeting.

<details><summary>Solution</summary>

**Method.** It is $-V_s$. The stopping potential measures energy per electron, set by $f$ alone; intensity only multiplies the number of electrons, so both curves die at the same retarding voltage.

</details>

#### Q9. Light of $400$ nm at power $1$ µW strikes a cell with quantum efficiency $0.1\%$. What current flows?

<details><summary>Solution</summary>

**Method.** Photon rate $\frac{10^{-6}}{4.97\times10^{-19}}=2.0\times10^{12}$ s$^{-1}$; electrons out $2.0\times10^{9}$ s$^{-1}$; $I=2.0\times10^{9}\times1.602\times10^{-19}=3.2\times10^{-10}$ A $=0.32$ nA.

</details>

#### Q10. A $V_s$-$f$ line cuts the frequency axis at $1.0\times10^{15}$ Hz. Find $\phi$.

<details><summary>Solution</summary>

**Method.** $\phi=hf_0=4.136\times10^{-15}\times1.0\times10^{15}=4.14$ eV.

</details>

#### Q11. What is the de Broglie wavelength of an electron accelerated through $1$ V?

<details><summary>Solution</summary>

**Method.** $\lambda=\frac{1.226}{\sqrt{1}}=1.23$ nm — longer than an atom, which is why volt-range electrons diffract strongly from surfaces.

</details>

#### Q12. A proton and an alpha particle are accelerated through the same voltage. Ratio of wavelengths?

<details><summary>Solution</summary>

**Method.** $\lambda\propto\frac{1}{\sqrt{mq}}$. Proton: $\sqrt{1\times1}=1$; alpha: $\sqrt{4\times2}=2.83$. Ratio $\lambda_p:\lambda_\alpha=2.83:1$.

</details>

#### Q13. A thermal neutron has energy $25$ meV. Find its wavelength.

<details><summary>Solution</summary>

**Method.** $K=25$ meV $=4.005\times10^{-21}$ J; $p=\sqrt{2m_nK}=\sqrt{2\times1.675\times10^{-27}\times4.005\times10^{-21}}=3.66\times10^{-24}$ kg m/s; $\lambda=\frac{6.626\times10^{-34}}{3.66\times10^{-24}}=1.8\times10^{-10}$ m $=1.8$ Å. Atomic scale: thermal neutrons diffract from crystals, the neutron analogue of Davisson-Germer.

</details>

#### Q14. A $0.15$ kg ball moves at $30$ m/s. Its de Broglie wavelength?

<details><summary>Solution</summary>

**Method.** $\lambda=\frac{6.626\times10^{-34}}{0.15\times30}=1.5\times10^{-34}$ m; no physical structure has features within thirty orders of magnitude, so the wave nature is unobservable.

</details>

#### Q15. An electron wave on a circular orbit fits exactly three wavelengths around the circumference. What is its angular momentum?

<details><summary>Solution</summary>

**Method.** $2\pi r=3\lambda=3\frac{h}{p}$ gives $pr=\frac{3h}{2\pi}=3\hbar$, i.e. $L=3\hbar$.

</details>

#### Q16. Estimate the minimum kinetic energy of an electron confined to $L=0.05$ nm.

<details><summary>Solution</summary>

**Method.** $K\approx\frac{\hbar^2}{2mL^2}$; halving $L$ from E9 quadruples $K$: $4\times3.8=15$ eV.

</details>

#### Q17. An electron is localised within $\Delta x=0.1$ nm. What is the minimum spread in its speed?

<details><summary>Solution</summary>

**Method.** $\Delta p\ge\frac{\hbar}{2\Delta x}=5.3\times10^{-25}$ kg m/s; $\Delta v=\frac{\Delta p}{m_e}=5.8\times10^{5}$ m/s — confinement to atomic scale makes the electron unavoidably fast.

</details>

#### Q18. Electrons at $100$ V diffract from planes with $d=0.91$ Å. Find the first-order glancing angle.

<details><summary>Solution</summary>

**Method.** $\lambda=0.123$ nm $=1.23$ Å; $\sin\theta=\frac{1.23}{1.82}=0.676$; $\theta=42.5^\circ$.

</details>

#### Q19. A $100$ W beam is fully absorbed by a black sail. Force on the sail?

<details><summary>Solution</summary>

**Method.** $F=\frac{P}{c}=\frac{100}{3\times10^8}=3.3\times10^{-7}$ N.

</details>

#### Q20. The same light strikes metal A ($\phi=2.0$ eV) and metal B ($\phi=3.5$ eV). Compare the maximum kinetic energies.

<details><summary>Solution</summary>

**Method.** $K_A-K_B=\phi_B-\phi_A=1.5$ eV, whatever the photon energy (as long as both emit).

</details>

#### Q21. Intensity of a fixed-frequency beam is doubled. By what factor do the photon flux and the stopping potential change?

<details><summary>Solution</summary>

**Method.** Flux $\times2$; $V_s$ $\times1$ (unchanged).

</details>

#### Q22. An electron microscope must resolve $0.1$ nm features. Minimum accelerating voltage?

<details><summary>Solution</summary>

**Method.** Need $\lambda\le0.1$ nm: $\frac{1.226}{\sqrt{V}}\le0.1\Rightarrow V\ge(12.26)^2=150$ V. Real instruments use kV for margin and lens quality.

</details>

#### Q23. The dark-adapted eye can respond to about $100$ photons at $500$ nm arriving within $0.1$ s. What power is that at the retina?

<details><summary>Solution</summary>

**Method.** $E_{\text{ph}}=2.48$ eV $=3.97\times10^{-19}$ J; $P=\frac{100\times3.97\times10^{-19}}{0.1}=4\times10^{-16}$ W. The eye is a near-single-photon instrument.

</details>

#### Q24. Doubling the frequency of incident light triples $K_{\max}$. Express the original photon energy in terms of $\phi$.

<details><summary>Solution</summary>

**Method.** $hf-\phi=K$ and $2hf-\phi=3K$; subtract: $hf=2K$, so $K=\frac{hf}{2}$ and $\phi=\frac{hf}{2}$: the original photon had exactly $2\phi$.

</details>

#### Q25. Momentum of a $550$ nm photon?

<details><summary>Solution</summary>

**Method.** $p=\frac{h}{\lambda}=\frac{6.626\times10^{-34}}{550\times10^{-9}}=1.2\times10^{-27}$ kg m/s.

</details>

#### Q26. Sodium ($\phi=2.28$ eV) is lit first with $300$ nm, then $400$ nm. Change in stopping potential?

<details><summary>Solution</summary>

**Method.** $\Delta V_s=\left(\frac{1240}{300}-\frac{1240}{400}\right)=4.13-3.10=1.03$ V; the work function cancels.

</details>

#### Q27. The saturation current of a cell is $0.6$ µA at intensity $I$. Predict it at $3I$, same $f$.

<details><summary>Solution</summary>

**Method.** Saturation current is proportional to photon rate: $1.8$ µA.

</details>

#### Q28. For one metal, $V_s=1.0$ V at frequency $f_1$ and $2.0$ V at $1.5f_1$. Find $\phi$ in eV.

<details><summary>Solution</summary>

**Method.** $\frac{h}{e}f_1-\frac{\phi}{e}=1$ and $1.5\frac{h}{e}f_1-\frac{\phi}{e}=2$; subtracting gives $0.5\frac{h}{e}f_1=1$, so $\frac{h}{e}f_1=2$ and $\frac{\phi}{e}=1$: $\phi=1.0$ eV.

</details>

## Part 7 · Alternate methods and the JEE-Advanced advantage toolkit

### 7.1 The eV-nm bookkeeping

Never carry $10^{-34}$ through a photoelectric calculation. Convert every photon to eV with $E=\frac{1240}{\lambda[\text{nm}]}$, keep work functions in eV, and read stopping potentials off directly in volts. Demonstration: $310$ nm on $\phi=2.2$ eV gives $V_s=4.0-2.2=1.8$ V in one line. Fails only when a joule-level quantity (force, pressure, power) is asked — then convert at the end.

### 7.2 Scaling instead of solving

When a question changes one quantity by a factor, answer by proportionality and skip the constants: $\lambda_e\propto V^{-1/2}$, photon rate $\propto P\lambda$, $K_{\max}$ affine in $f$. Demonstration: quadrupling the accelerating voltage halves the electron wavelength — no constants touched. Fails when the change crosses a regime (relativistic voltage, below threshold), where the proportionality itself changes.

### 7.3 Dimensional synthesis

Build the atom from $\hbar$, $m_e$, $ke^2$: the unique length is $\frac{\hbar^2}{m_ek e^2}=0.53$ Å and the unique energy $\frac{m_ek^2e^4}{\hbar^2}=27.2$ eV. Any atomic-scale answer must be these times an order-unity number; a result of $10^{-4}$ Å or $10^3$ eV is wrong before the algebra is checked. Fails where a second length enters (nuclear size, lattice spacing), which is exactly how you spot muonic atoms and X-ray scales.

### 7.4 Momentum bookkeeping for light on surfaces

For a beam of power $P$ with reflection coefficient $R$, the force is $F=\frac{P}{c}(1+R)$: absorbed photons hand over $\frac{h}{\lambda}$, reflected ones twice that, and the mix is linear. Demonstration: $R=0.4$, $P=3$ W gives $F=\frac{3}{c}\times1.4=1.4\times10^{-8}$ N. Fails for mirrors moving at relativistic speed, where the reflected photon's frequency shifts — PART 28 territory.

### 7.5 Linearise the graph

Any photoelectric graph question is $y=mx+c$ in disguise: $V_s$ vs $f$ has $m=\frac{h}{e}$, $c=-\frac{\phi}{e}$; $K_{\max}$ vs $f$ has $m=h$. Read two points, take the slope, take the intercept; never trust a drawn slope's eye-value. Fails when the axes are $\lambda$ instead of $f$: the graph is a hyperbola, and the trick is to replot mentally against $\frac{1}{\lambda}$.

### 7.6 The limit as a solver

Before finishing any answer, push one parameter to an extreme: $I\to0$ must not move $V_s$; $V\to\infty$ must send $\lambda_e\to0$; $\phi\to hf$ must send the current to zero. A wrong option in a multiple-correct question usually dies under exactly one of these pushes, at the cost of five seconds.

## Part 8 · Examiner traps

### 8.1 The trap ledger

> [!danger] Trap 1 — non-relativistic momentum at high voltage
> Using $\lambda=\frac{1.226}{\sqrt{V}}$ nm at $100$ kV. The relativistic momentum is larger, the true wavelength $3.70$ pm against the formula's $3.88$ pm: a $4.6\%$ error, above the 1 % tolerance by $V\approx3$ kV. Reply: check $eV$ against $511$ keV first.

> [!danger] Trap 2 — eV versus joule
> Substituting a work function in eV into $\frac{1}{2}mv^2$ with $m$ in kg. Reply: one conversion line, $1$ eV $=1.602\times10^{-19}$ J, written every time.

> [!danger] Trap 3 — stopping potential versus intensity
> Answering that brighter light raises $V_s$. Reply: $V_s$ counts energy per photon, set by $f$ alone; intensity multiplies electrons, not their energy.

> [!danger] Trap 4 — forgetting the toll
> Writing $K_{\max}=hf$. Reply: the work function is always paid; $K_{\max}=hf-\phi$, and if $hf<\phi$ the answer is "no emission", not a negative kinetic energy.

> [!danger] Trap 5 — threshold bookkeeping
> Using the threshold wavelength as if it gave electrons with energy: at $\lambda_0$ the electrons emerge with $K=0$. Reply: threshold means barely, $V_s=0$.

> [!danger] Trap 6 — the two-pi slip
> Writing $\Delta x\Delta p\ge\hbar$ or $L=nh$. Reply: $\hbar=\frac{h}{2\pi}$; the uncertainty bound is $\frac{\hbar}{2}$, and $L=n\hbar=\frac{nh}{2\pi}$.

> [!danger] Trap 7 — the LEED reversal
> Assuming slower electrons diffract less because they have less energy. Reply: slower means smaller $p$ means longer $\lambda$ means stronger diffraction; low energy is the point.

> [!danger] Trap 8 — saturation as quantum
> Citing saturation current as evidence for photons. Reply: saturation is geometry — every emitted electron collected; the quantum evidence is the threshold and the $V_s$ behaviour.

> [!danger] Trap 9 — current versus frequency
> Claiming the photocurrent must rise with frequency. Reply: at fixed intensity, higher $f$ means fewer photons per second, so the current falls slightly.

> [!danger] Trap 10 — massive photon momentum
> Using $p=\frac{E}{c}$ for the photoelectron. Reply: that is the massless relation; for electrons $p=\sqrt{2mK}$.

## Part 9 · Playbook

### 9.1 Triage decision tree

- If the question mentions emission, threshold, stopping potential: photon bookkeeping, §3.5.
- If it mentions wavelength of a particle, diffraction of electrons or neutrons: §3.7-3.10.
- If it mentions force or pressure of light: §3.4 momentum bookkeeping, reflection factor.
- If it gives a graph: §7.5 linearise.
- If it asks "explain why not classically": §3.3 waiting time plus threshold.
- If it asks for a size or minimum energy with no orbit given: uncertainty, §3.9.

### 9.2 Formula map with validity

| Formula | Valid when | Breaks when |
|---|---|---|
| $E=\frac{1240}{\lambda}$ eV | always, photons | never |
| $K_{\max}=hf-\phi$ | $hf\ge\phi$, one photon | intense pulsed lasers (two-photon) |
| $\lambda_e=\frac{1.226}{\sqrt{V}}$ nm | $eV\ll511$ keV | above a few kV, use relativistic $p$ |
| $F=\frac{P}{c}(1+R)$ | slow surface | relativistic mirror |
| $\Delta x\Delta p\gtrsim\frac{\hbar}{2}$ | always | never (it defines the quantum regime) |
| $2\pi r=n\lambda$ | circular orbit | non-circular states need full quantum mechanics |

### 9.3 Constants to carry

$hc=1240$ eV nm; $h=4.14\times10^{-15}$ eV s; $m_ec^2=511$ keV; $\lambda_C=2.43$ pm; $a_0=0.53$ Å; $13.6$ eV; $\frac{h}{e}=4.14\times10^{-15}$ V s.

### 9.4 Timing plan

Section A: 90 s each. Section B: 2 min each. Section C: 3 min. Section D: 12 min. Reserve 15 min for audit. A photoelectric question that has not reduced to eV bookkeeping within a minute is mis-triaged; re-read it.

### 9.5 Pre-submission audit, ten points

1. Units: eV or J declared on every line.
2. Threshold checked: is $hf\ge\phi$?
3. $V_s$ intensity-independent?
4. Relativistic check if $eV>3$ keV.
5. $\hbar$ versus $h$ checked.
6. Charge factor for non-electron particles.
7. Limit pushed once.
8. Graph axes: $f$ or $\lambda$?
9. Answer magnitude sane (wavelengths in the right band, speeds $<c$).
10. Marks allocation: did you answer every sub-part?

## Part 10 · Olympiad extension

### 10.1 First-principles derivations the school book skips

Three derivations anchor this block: the group-and-phase-velocity structure of matter waves (OL2), the hydrogen atom from the uncertainty principle by two independent routes (OL3), and the natural linewidth from finite lifetime (OL4). Two measurement reconstructions give the physics behind the numbers: the eye's single-photon sensitivity (OL5) and the laser's inversion requirement (OL6).

### OL1 — The classical wave model on trial

A photoelectric surface (work function $2$ eV, atomic cross-section $10^{-20}$ m$^2$) is lit at three intensities: bright lab light $10^3$ W/m$^2$, moonlight $10^{-3}$ W/m$^2$, and a starlit $10^{-8}$ W/m$^2$. Compute the wave-theory waiting time in each case, and state what the experiment shows instead.

<details><summary>Solution</summary>

**Method.** Energy balance on one atom: $t=\frac{\phi}{IA}$ with $\phi=3.2\times10^{-19}$ J.

$10^3$ W/m$^2$: $t=\frac{3.2\times10^{-19}}{10^{-17}}=3.2\times10^{-2}$ s. $10^{-3}$: $t=3.2\times10^{4}$ s $\approx9$ h. $10^{-8}$: $t=3.2\times10^{9}$ s $\approx100$ years.

Experiment: electrons appear within $10^{-9}$ s at all intensities, with no warm-up. The wave model fails by up to eighteen orders of magnitude; the photon model predicts no intensity dependence at all, since each photon arrives whole.

**Checks.** (i) $t\propto\frac{1}{I}$: each decade of dimming multiplies the wait by ten, as tabulated. (ii) Unit check: J divided by W is s.

</details>

### OL2 — Phase velocity above c, group velocity below: the structure of a matter wave

Assign to a free particle the Einstein-de Broglie pair $E=\hbar\omega$, $p=\hbar k$, with the relativistic relation $E^2=p^2c^2+m^2c^4$. Derive the phase velocity $v_p=\frac{\omega}{k}$ and the group velocity $v_g=\frac{d\omega}{dk}$, identify each physically, and explain why $v_p>c$ offends nothing.

<details><summary>Solution</summary>

**Method.** Divide and differentiate.

$v_p=\frac{\omega}{k}=\frac{E}{p}=\frac{\gamma mc^2}{\gamma mv}=\frac{c^2}{v}>c$. Differentiating $E^2=p^2c^2+m^2c^4$: $E\,dE=pc^2\,dp$, so $v_g=\frac{d\omega}{dk}=\frac{dE}{dp}=\frac{pc^2}{E}=v$, the particle's own speed.

The phase velocity carries no energy and no signal — a single infinite sine wave carries nothing — so its exceeding $c$ violates no principle; every measurable thing (energy, momentum, information) travels at $v_g=v\le c$. The product $v_pv_g=c^2$ is the invariant fingerprint of a relativistic matter wave.

**Checks.** (i) $m\to0$: both velocities $\to c$, the photon case. (ii) Non-relativistic limit $p\ll mc$: $v_g=\frac{p}{m}$, the classical speed.

</details>

### OL3 — Hydrogen without postulates, twice

Derive the ground-state radius and energy of hydrogen from the uncertainty principle by (a) minimising $E(r)=\frac{\hbar^2}{2m_er^2}-\frac{ke^2}{r}$ and (b) the virial-style balance in which one sets $p\sim\frac{\hbar}{r}$ and demands the two terms' $r$-dependence cancel at the minimum. Compare with the exact Bohr values.

<details><summary>Solution</summary>

**Method (a).** $\frac{dE}{dr}=-\frac{\hbar^2}{m_er^3}+\frac{ke^2}{r^2}=0\Rightarrow r=\frac{\hbar^2}{m_ek e^2}=0.529$ Å; substituting back, $E_{\min}=-\frac{m_ek^2e^4}{2\hbar^2}=-13.6$ eV.

**Method (b).** At the minimum the kinetic and potential magnitudes satisfy $\frac{\hbar^2}{2m_er^2}=\frac{ke^2}{2r}$ (kinetic is half the potential's magnitude), giving the same $r$ and $E=-\frac{ke^2}{2r}=-13.6$ eV.

Both routes reproduce $a_0$ and the Rydberg energy exactly, because the true ground state of hydrogen saturates the uncertainty bound to within a factor of order one — the estimate is accidentally exact for $s$-states.

**Checks.** (i) Dimensional: $\frac{\hbar^2}{mke^2}$ has units of length. (ii) Scaling: replacing $m_e$ by $207m_e$ (muonic hydrogen) shrinks $r$ by 207, as PART 24 will need.

</details>

### OL4 — The natural width of a spectral line

An excited atomic state lives $\tau=10^{-8}$ s before emitting. Use $\Delta E\,\Delta t\gtrsim\frac{\hbar}{2}$ to find the energy width of the state and the wavelength width of the $656$ nm line it emits.

<details><summary>Solution</summary>

**Method.** $\Delta E\approx\frac{\hbar}{\tau}=\frac{1.055\times10^{-34}}{10^{-8}}=1.05\times10^{-26}$ J $=6.6\times10^{-8}$ eV. Convert with $\Delta\lambda=\frac{\lambda^2}{hc}\Delta E$: $\Delta\lambda=\frac{(656\times10^{-9})^2}{1.986\times10^{-25}}\times1.05\times10^{-26}=2.3\times10^{-14}$ m $=2.3\times10^{-5}$ nm.

Spectral lines are never perfectly sharp; this irreducible width is why precision spectroscopy eventually meets a quantum floor (and why PART 24's isotope shifts of $0.18$ nm are comfortably resolvable above it).

**Checks.** (i) Longer $\tau$ narrows the line, $\Delta\lambda\propto\frac{1}{\tau}$. (ii) $\frac{\Delta\lambda}{\lambda}=\frac{\Delta E}{E}=\frac{6.6\times10^{-8}}{1.89}=3.5\times10^{-8}$, consistent.

</details>

### OL5 — How dim can a human see? Reconstruct the measurement

The fully dark-adapted eye responds to a flash of about $100$ photons at $500$ nm at the cornea. Compute the flash energy and average power over the $0.1$ s integration time, and compare with a $1$ mW laser pointer.

<details><summary>Solution</summary>

**Method.** $E_{\text{ph}}=\frac{1240}{500}=2.48$ eV $=3.97\times10^{-19}$ J. Flash energy $=100\times3.97\times10^{-19}=4\times10^{-17}$ J; power $=4\times10^{-16}$ W.

The eye resolves $4\times10^{-16}$ W; the pointer emits $10^{-3}$ W, thirteen orders of magnitude above threshold. The retina is, functionally, a photomultiplier array.

**Checks.** (i) Photon count times photon energy reproduces the flash energy. (ii) The number is between a candle kilometres away and total darkness, sanity-checking the order.

</details>

### OL6 — Why lasers must be pumped: the Boltzmann obstruction

In thermal equilibrium at temperature $T$, the ratio of atoms in an excited level $2$ eV above the ground level is $e^{-hf/k_BT}$. Evaluate this at $300$ K and at $3000$ K, and conclude what population inversion demands.

<details><summary>Solution</summary>

**Method.** $\frac{hf}{k_BT}=\frac{2\times1.602\times10^{-19}}{1.381\times10^{-23}\times300}=77.3$, so the ratio is $e^{-77.3}\approx10^{-34}$; at $3000$ K, $e^{-7.7}\approx4.5\times10^{-4}$.

Thermal light never inverts an optical transition: even at $3000$ K one atom in a few thousand is up, far from the majority required for stimulated emission to out-absorb. Inversion is a deliberately engineered non-equilibrium — optical or electrical pumping into a level that drains slowly — which is exactly why lasers appeared only in 1960, not 1917.

**Checks.** (i) Ratio rises with $T$, as the formula demands. (ii) Microwave transitions ($hf\sim10^{-4}$ eV) have ratio near $1$ at room temperature, explaining why masers came first.

</details>

### OL7 — Two-photon photoemission

A metal with $\phi=2.3$ eV shows no emission under continuous $1.5$ eV light of any intensity, yet a pulsed laser of the same photon energy ejects electrons with $K_{\max}=0.7$ eV. Explain both facts and predict the intensity dependence of the current in the pulsed regime.

<details><summary>Solution</summary>

**Method.** Single-photon: $1.5<2.3$, no emission at any intensity — the threshold is a per-photon statement. Pulsed: two photons absorbed simultaneously give $3.0$ eV $>2.3$ eV, $K_{\max}=3.0-2.3=0.7$ eV. The rate of two-photon absorption scales as the *square* of intensity (two independent photons must coincide), so the current $\propto I^2$, a measurable fingerprint.

**Checks.** (i) $K_{\max}=2hf-\phi$ numerically. (ii) Halving the pulsed intensity quarters the current.

</details>

### OL8 — Which voltage for the wavelength? The relativistic correction

An electron diffraction instrument runs at $100$ kV. Compute the wavelength with the non-relativistic formula and with the correct relativistic momentum, and quote the fractional error.

<details><summary>Solution</summary>

**Method.** Non-relativistic: $\lambda=\frac{1.226}{\sqrt{10^5}}=3.88$ pm. Relativistic: $E_{\text{tot}}=511+100=611$ keV; $pc=\sqrt{611^2-511^2}=332$ keV; $\lambda=\frac{hc}{pc}=\frac{1240\ \text{eV nm}}{3.32\times10^5\ \text{eV}}=3.70$ pm. Fractional error of the shortcut: $\frac{3.88-3.70}{3.70}=4.6\%$.

Diffraction angles scale with $\lambda$, so a $4.6\%$ wavelength error is a $4.6\%$ structural error — fatal for lattice metrology, which is why electron-diffraction software is relativistic.

**Checks.** (i) At $1$ kV the same computation gives an error of $0.1\%$, showing the threshold of neglect. (ii) $pc<E_{\text{tot}}$, as required.

</details>

### OL9 — The inverse photoelectric effect (Duane-Hunt preview)

Electrons stopped in a metal target emit light. Argue from energy conservation that the emitted spectrum has a sharp *minimum* wavelength $\lambda_{\min}=\frac{hc}{eV}$ for tube voltage $V$, and evaluate it at $50$ kV.

<details><summary>Solution</summary>

**Method.** One electron can give at most its whole kinetic energy $eV$ to one photon; the richest photon has $hf_{\max}=eV$, hence $\lambda_{\min}=\frac{hc}{eV}=\frac{1240}{5\times10^4}=0.0248$ nm $=24.8$ pm. This is the photoelectric equation read backwards — emission instead of absorption — and historically the sharpest early measurement of $\frac{h}{e}$. PART 25 derives the full continuous spectrum around this edge.

**Checks.** (i) $\lambda_{\min}\propto\frac{1}{V}$. (ii) At $V\to0$ the edge slides to infinite wavelength, i.e. no X-rays at all.

</details>

### OL10 — Levitating a mirror with light

What beam power, perfectly reflected, would levitate a $1$ g mirror against gravity? Comment on feasibility.

<details><summary>Solution</summary>

**Method.** $\frac{2P}{c}=mg\Rightarrow P=\frac{mgc}{2}=\frac{10^{-3}\times9.8\times3\times10^8}{2}=1.5\times10^6$ W.

A megawatt to hold up a gram: light's momentum is real but feeble at human scale, which is precisely why radiation pressure matters for comet tails, solar sails and laser cooling, not for kitchen objects.

**Checks.** (i) Units: kg m/s$^2$ times m/s is W. (ii) Doubling the mass doubles the power.

</details>

### OL11 — When a gas becomes quantum: the thermal de Broglie wavelength

Compute the thermal wavelength $\lambda_{\text{th}}=\frac{h}{\sqrt{3mk_BT}}$ of (a) a nitrogen molecule and (b) an electron at $300$ K, and compare each with the typical interparticle spacing ($3$ nm in air, $0.25$ nm in a metal). Conclude which gas is classical and which is quantum.

<details><summary>Solution</summary>

**Method.** (a) $m=4.65\times10^{-26}$ kg: $\lambda_{\text{th}}=\frac{6.626\times10^{-34}}{\sqrt{3\times4.65\times10^{-26}\times4.14\times10^{-21}}}=2.2\times10^{-11}$ m, sixty times smaller than the $3$ nm spacing: air is a classical gas. (b) $m_e$: $\lambda_{\text{th}}=6.2$ nm, twenty-five times *larger* than the $0.25$ nm spacing in a metal: the electron waves overlap completely, and conduction electrons are a quantum (Fermi) gas at room temperature — the deep reason metals' heat capacities and conductivities defy classical physics.

**Checks.** (i) $\lambda_{\text{th}}\propto T^{-1/2}$ and $\propto m^{-1/2}$. (ii) Cooling air toward $1$ K would grow its wavelength toward the spacing, anticipating Bose-Einstein condensation.

</details>

### OL12 — The microscope resolution audit

A visible-light microscope uses $550$ nm; an electron microscope runs at $100$ kV with relativistic wavelength $3.7$ pm. Estimate the best resolvable feature for each (about $\lambda$), the improvement factor, and the voltage an electron instrument would need to match the X-ray band at $0.1$ nm.

<details><summary>Solution</summary>

**Method.** Light: $\sim300$ nm features. Electrons: in principle $\sim4$ pm, a factor $\frac{550}{0.0037}\approx1.5\times10^5$ finer. To reach $\lambda=0.1$ nm: $V=\left(\frac{1.226}{0.1}\right)^2=150$ V non-relativistically — any electron microscope is already beyond X-ray wavelengths, and its practical resolution is set by lens aberrations, not by $\lambda$.

**Checks.** (i) Improvement factor equals the wavelength ratio. (ii) The $150$ V figure agrees with Q22.

</details>

### 10.2 Limits and failure of the model

The photon bookkeeping of this chapter breaks, and hands over, at four frontiers: (i) *intensity*: above $\sim10^{12}$ W/m$^2$ multi-photon absorption turns the threshold into a ladder (OL7); (ii) *material*: real surfaces have band structure, and semiconductors replace $\phi$ by a gap plus band edges (PART 27); (iii) *energy*: above a few keV the electron needs relativity (OL8), and above $1.02$ MeV the photon itself dies into pairs (PART 25, PART 28); (iv) *interpretation*: which-slit questions are answered by full quantum mechanics, not by this chapter's bookkeeping. Every one of these is a later PART's opening door, not a defect of the photon picture inside its domain.

## Part 11 · Olympiad-grade paper

**Time: 180 minutes · Maximum marks: 200 · 36 questions.**
Sections: A — 12 single-correct (4 marks each, −1 for a wrong answer); B — 8 one-or-more-correct (4 marks each, no negative marking); C — 6 numerical answers (5 marks each); D — 10 long-form (9 marks each). Solutions follow each question in a collapsible block; the marking scheme is in Part 12.

| Section | Questions | Marks each | Subtotal | Topic coverage |
|---|---|---:|---:|---|
| A | 1–12 | 4 | 48 | blocks 2–4 |
| B | 13–20 | 4 | 32 | blocks 3–4 |
| C | 21–26 | 5 | 30 | blocks 4, 10 |
| D | 27–36 | 9 | 90 | blocks 3, 10 |
| | 36 | | 200 | |

#### Section A · Single correct

### P1 · 4 marks

Photon A has wavelength $400$ nm, photon B has $800$ nm. The ratio $E_A:E_B$ is:
(a) $1:2$ (b) $2:1$ (c) $4:1$ (d) $1:4$

<details><summary>Solution</summary>

$E\propto\frac{1}{\lambda}$, so the ratio is $800:400=2:1$. Answer (b).

</details>

### P2 · 4 marks

Which single observation most directly rules out the classical wave model, even at high intensity?
(a) current proportional to intensity (b) saturation of the current (c) a threshold frequency below which nothing is emitted (d) existence of radiation pressure

<details><summary>Solution</summary>

(c). Waves deliver energy continuously, so a bright wave of any frequency should eventually eject; a hard threshold per frequency is a per-quantum statement. (a) and (b) waves also predict; (d) is classical Maxwell physics.

</details>

### P3 · 4 marks

A metal with $\phi=2.3$ eV is lit with $496$ nm light. The stopping potential is:
(a) $0.2$ V (b) $2.5$ V (c) $0.46$ V (d) zero, no emission

<details><summary>Solution</summary>

$E=\frac{1240}{496}=2.5$ eV; $K_{\max}=2.5-2.3=0.2$ eV; $V_s=0.2$ V. Answer (a).

</details>

### P4 · 4 marks

A $60$ W source emits only at $600$ nm. Photons per second:
(a) $1.8\times10^{20}$ (b) $1.8\times10^{17}$ (c) $3.6\times10^{20}$ (d) $9\times10^{19}$

<details><summary>Solution</summary>

$E=\frac{1240}{600}=2.07$ eV $=3.31\times10^{-19}$ J; $N=\frac{60}{3.31\times10^{-19}}=1.8\times10^{20}$. Answer (a).

</details>

### P5 · 4 marks

The de Broglie wavelength of an electron accelerated through $400$ V is:
(a) $0.061$ nm (b) $0.12$ nm (c) $0.031$ nm (d) $0.24$ nm

<details><summary>Solution</summary>

$\lambda=\frac{1.226}{\sqrt{400}}=\frac{1.226}{20}=0.061$ nm. Answer (a).

</details>

### P6 · 4 marks

A $2$ W beam reflects normally from a mirror. The force is:
(a) $6.7\times10^{-9}$ N (b) $1.3\times10^{-8}$ N (c) $3.3\times10^{-9}$ N (d) $2.7\times10^{-8}$ N

<details><summary>Solution</summary>

$F=\frac{2P}{c}=\frac{4}{3\times10^8}=1.3\times10^{-8}$ N. Answer (b).

</details>

### P7 · 4 marks

The order of the de Broglie wavelength of a $0.15$ kg ball at $20$ m/s is:
(a) $10^{-10}$ m (b) $10^{-24}$ m (c) $10^{-34}$ m (d) $10^{-44}$ m

<details><summary>Solution</summary>

$\lambda=\frac{6.6\times10^{-34}}{3}=2.2\times10^{-34}$ m. Answer (c).

</details>

### P8 · 4 marks

The slope of a stopping-potential versus frequency graph, in SI units, is:
(a) $h$ (b) $\frac{h}{e}$ (c) $\frac{e}{h}$ (d) $he$

<details><summary>Solution</summary>

$V_s=\frac{h}{e}f-\frac{\phi}{e}$: slope $\frac{h}{e}=4.14\times10^{-15}$ V s. Answer (b).

</details>

### P9 · 4 marks

A metal has $\phi=4.14$ eV. Its threshold frequency is:
(a) $10^{15}$ Hz (b) $10^{14}$ Hz (c) $6\times10^{14}$ Hz (d) $4\times10^{15}$ Hz

<details><summary>Solution</summary>

$f_0=\frac{4.14}{4.14\times10^{-15}}=10^{15}$ Hz. Answer (a).

</details>

### P10 · 4 marks

The minimum kinetic energy of an electron confined to a $1$ nm box is closest to:
(a) $3.8$ eV (b) $0.04$ eV (c) $38$ eV (d) $0.4$ eV

<details><summary>Solution</summary>

$K\approx\frac{\hbar^2}{2mL^2}=\frac{(1.055\times10^{-34})^2}{2\times9.109\times10^{-31}\times10^{-18}}=6.1\times10^{-21}$ J $=0.038$ eV. Answer (b).

</details>

### P11 · 4 marks

Light of fixed wavelength ejects electrons from A ($\phi_A=2$ eV) with $K_{\max}=1$ eV. From B ($\phi_B=3$ eV), $K_{\max}$ is:
(a) $2$ eV (b) $1$ eV (c) $0$ (d) no emission is guaranteed without checking

<details><summary>Solution</summary>

Photon energy $=3$ eV; for B, $K_{\max}=3-3=0$ eV. Answer (c): emission just at threshold.

</details>

### P12 · 4 marks

An electron's standing wave fits two wavelengths around its orbit. Its angular momentum is:
(a) $\frac{h}{\pi}$ (b) $\frac{h}{2\pi}$ (c) $\frac{2h}{\pi}$ (d) $2h$

<details><summary>Solution</summary>

$L=n\hbar=2\hbar=\frac{2h}{2\pi}=\frac{h}{\pi}$. Answer (a).

</details>

#### Section B · One or more correct

### P13 · 4 marks

Light of frequency $f>f_0$ at intensity $I$ produces current. The intensity is doubled at the same $f$. Which statements are correct?
(a) saturation current doubles (b) stopping potential is unchanged (c) $K_{\max}$ doubles (d) photon flux doubles

<details><summary>Solution</summary>

(a), (b), (d). Photon energy is unchanged, so (c) is false.

</details>

### P14 · 4 marks

At fixed intensity, the frequency is increased above threshold. Which increase?
(a) $K_{\max}$ (b) $V_s$ (c) photon flux (d) saturation current

<details><summary>Solution</summary>

(a) and (b). Fixed intensity means fixed power; richer photons mean fewer of them, so (c) and (d) decrease.

</details>

### P15 · 4 marks

About matter waves:
(a) $\lambda=\frac{h}{p}$ for any particle (b) at the same voltage, an alpha particle has a shorter wavelength than a proton (c) thermal neutrons diffract from crystals (d) a moving molecule has no wavelength until observed

<details><summary>Solution</summary>

(a), (b), (c). (b): $\lambda\propto\frac{1}{\sqrt{mq}}$, alpha wins on both factors. (d) is false: the wavelength is a property of the state, not of observation.

</details>

### P16 · 4 marks

The uncertainty principle:
(a) is a property of waves, not of clumsy instruments (b) explains why atoms have a finite size (c) forces a confined particle to have nonzero minimum energy (d) can be defeated by a perfect instrument

<details><summary>Solution</summary>

(a), (b), (c). (d) contradicts the wave-packet mathematics of §3.9.

</details>

### P17 · 4 marks

Two metals' $V_s$-$f$ lines are drawn. Correct statements:
(a) equal slopes (b) equal $f$-intercepts (c) the metal with larger $f_0$ has larger $\phi$ (d) slopes differ by the mass ratio

<details><summary>Solution</summary>

(a) and (c). Slopes are $\frac{h}{e}$ universally; $\phi=hf_0$ makes (c) true and (b) false.

</details>

### P18 · 4 marks

For a photon of wavelength $\lambda$:
(a) $p=\frac{h}{\lambda}$ (b) $E=pc$ (c) absorbed by a surface, it transfers $\frac{h}{\lambda}$ (d) it can be split between two electrons in the ordinary effect

<details><summary>Solution</summary>

(a), (b), (c). (d) violates the one-photon-one-electron bookkeeping of §3.4.

</details>

### P19 · 4 marks

The Davisson-Germer experiment:
(a) confirmed $\lambda=\frac{h}{p}$ for electrons (b) used the crystal as a three-dimensional grating (c) shows a diffraction angle that shrinks as the voltage rises (d) proved electrons are waves and never particles

<details><summary>Solution</summary>

(a), (b), (c). (c): higher $V$, shorter $\lambda$, smaller angle. (d) is false — complementarity, §3.11.

</details>

### P20 · 4 marks

In two-photon photoemission with pulsed lasers:
(a) emission can occur with each photon below threshold (b) the current scales as $I^2$ (c) the effect works with ordinary lamp light (d) $K_{\max}=2hf-\phi$

<details><summary>Solution</summary>

(a), (b), (d). (c) fails: coincidence rate at lamp intensities is vanishing.

</details>

#### Section C · Numerical

### P21 · 5 marks

Sodium ($\phi=2.28$ eV) is lit with $300$ nm light. Give $V_s$ in volts.

<details><summary>Solution</summary>

$K_{\max}=\frac{1240}{300}-2.28=4.13-2.28=1.85$ eV; $V_s=1.85$ V.

</details>

### P22 · 5 marks

A $50$ W isotropic source at $620$ nm is $5$ m from a detector. The photon flux at the detector, in photons per m$^2$ per second, is $a\times10^{17}$; give $a$ to one decimal.

<details><summary>Solution</summary>

$I=\frac{50}{4\pi\times25}=0.159$ W/m$^2$; $E=2.0$ eV $=3.2\times10^{-19}$ J; $n=\frac{0.159}{3.2\times10^{-19}}=5.0\times10^{17}$. $a=5.0$.

</details>

### P23 · 5 marks

Give the de Broglie wavelength, in nm, of an electron accelerated through $25$ V.

<details><summary>Solution</summary>

$\lambda=\frac{1.226}{5}=0.245$ nm.

</details>

### P24 · 5 marks

A surface with $\phi=1.8$ eV is lit with $400$ nm light. $K_{\max}$ in eV?

<details><summary>Solution</summary>

$3.10-1.8=1.3$ eV.

</details>

### P25 · 5 marks

An electron and a proton have the same kinetic energy. The ratio $\lambda_e:\lambda_p$ is $1:n$; give $n$ to the nearest integer.

<details><summary>Solution</summary>

$\lambda\propto\frac{1}{\sqrt{m}}$; $n=\sqrt{\frac{m_p}{m_e}}=\sqrt{1836}=42.8\approx43$.

</details>

### P26 · 5 marks

Estimate the minimum kinetic energy, in eV, of an electron confined to $0.2$ nm.

<details><summary>Solution</summary>

$K\approx\frac{\hbar^2}{2mL^2}$; scaling from the $0.1$ nm value $3.8$ eV by $\left(\frac{0.1}{0.2}\right)^2$: $0.95$ eV.

</details>

#### Section D · Comprehensive long-form

### P27 · 9 marks

For a metal, $V_s=1.10$ V at $400$ nm and $V_s=2.13$ V at $300$ nm. (i) Find $\phi$ in eV. (ii) Find $h$ in eV s from this data alone. (iii) Predict the threshold wavelength. (3+3+3)

<details><summary>Solution</summary>

**Method.** Two instances of $eV_s=hf-\phi$; subtract to get the slope.

(i) $\phi=E_1-eV_1=\frac{1240}{400}-1.10=3.10-1.10=2.0$ eV. Cross-check with line 2: $\frac{1240}{300}-2.13=4.13-2.13=2.0$ eV, consistent.

(ii) $f_1=\frac{3\times10^8}{400\times10^{-9}}=7.50\times10^{14}$ Hz, $f_2=1.00\times10^{15}$ Hz. $h=e\cdot\frac{V_2-V_1}{f_2-f_1}=\frac{2.13-1.10}{2.50\times10^{14}}=4.12\times10^{-15}$ eV s $=6.6\times10^{-34}$ J s.

(iii) $\lambda_0=\frac{1240}{2.0}=620$ nm.

**Checks.** Both lines give the same $\phi$; the slope equals the universal $\frac{h}{e}$ of §3.5.

</details>

### P28 · 9 marks

(a) Derive the classical waiting-time formula $t=\frac{\phi}{IA}$. (b) Evaluate it for $I=10^{-3}$ W/m$^2$, $A=10^{-20}$ m$^2$, $\phi=2$ eV. (c) State the two experimental facts that make the result fatal for the wave model. (3+3+3)

<details><summary>Solution</summary>

(a) Wave energy arrives continuously at rate $IA$ per atom; time to accumulate $\phi$ is $\frac{\phi}{IA}$.
(b) $t=\frac{3.2\times10^{-19}}{10^{-23}}=3.2\times10^{4}$ s, about nine hours.
(c) Emission is observed within nanoseconds, and the threshold frequency exists at any intensity; neither is compatible with hoarded wave energy.

</details>

### P29 · 9 marks

Electrons at $100$ V strike planes of spacing $0.20$ nm. (a) First-order glancing angle. (b) The highest observable order. (c) At $100$ kV, would the non-relativistic formula misplace the angle by more than 1 %? (3+3+3)

<details><summary>Solution</summary>

(a) $\lambda=0.123$ nm; $\sin\theta=\frac{0.123}{0.40}=0.307$; $\theta=17.9^\circ$.
(b) $\sin\theta\le1\Rightarrow n\le\frac{2d}{\lambda}=\frac{0.40}{0.123}=3.25$: orders 1-3.
(c) Yes: the wavelength error is $4.6\%$ (OL8), and angles inherit several percent.

</details>

### P30 · 9 marks

(a) Write $E(r)$ for an electron localised to radius $r$ around a proton, using $p\sim\frac{\hbar}{r}$. (b) Minimise it to obtain $a_0$ and $E_{\min}$ numerically. (c) Show the kinetic term at the minimum is half the potential's magnitude, and state what replaces the electron for muonic hydrogen. (3+3+3)

<details><summary>Solution</summary>

(a) $E(r)=\frac{\hbar^2}{2m_er^2}-\frac{ke^2}{r}$.
(b) $r_{\min}=\frac{\hbar^2}{m_ek e^2}=0.529$ Å; $E_{\min}=-13.6$ eV.
(c) At $r_{\min}$: kinetic $=13.6$ eV, potential $=-27.2$ eV, ratio one-half (the virial theorem for $1/r$ forces). Muonic hydrogen: $m\to207m_e$, so $a\to\frac{0.529}{207}$ Å and $E\to-2.8$ keV.

</details>

### P31 · 9 marks

A $10$ W beam hits a surface with reflection coefficient $0.5$. (a) Force on the surface. (b) Power needed to levitate a $1$ g perfect mirror. (c) Why such pressures shaped comet tails but not kitchen life. (3+3+3)

<details><summary>Solution</summary>

(a) $F=\frac{P}{c}(1+R)=\frac{10}{3\times10^8}\times1.5=5\times10^{-8}$ N.
(b) $P=\frac{mgc}{2}=1.5\times10^6$ W.
(c) The force-to-power ratio is $\frac{1}{c}$: enormous areas and astronomical powers make it matter in space; gram-scale weights need megawatts on Earth.

</details>

### P32 · 9 marks

(a) For a relativistic particle with $E=\hbar\omega$, $p=\hbar k$, derive $v_p=\frac{c^2}{v}$. (b) Derive $v_g=v$. (c) Explain in two sentences why $v_p>c$ is harmless. (3+3+3)

<details><summary>Solution</summary>

(a) $v_p=\frac{\omega}{k}=\frac{E}{p}=\frac{\gamma mc^2}{\gamma mv}=\frac{c^2}{v}$.
(b) $E\,dE=pc^2dp\Rightarrow v_g=\frac{dE}{dp}=\frac{pc^2}{E}=v$.
(c) A pure phase carries no energy, momentum or information; all measurable transport occurs at $v_g\le c$.

</details>

### P33 · 9 marks

(a) Compute $\lambda_{\text{th}}$ for conduction electrons at $300$ K and compare with the $0.25$ nm spacing in copper. (b) Conclude which statistics govern them. (c) An electron microscope uses $100$ kV electrons of $3.7$ pm; estimate its wavelength-limited resolution and the factor over $550$ nm light. (3+3+3)

<details><summary>Solution</summary>

(a) $\lambda_{\text{th}}=\frac{h}{\sqrt{3m_ek_BT}}=6.2$ nm, twenty-five times the spacing.
(b) Overlapping waves: Fermi-Dirac, a quantum gas; classical equipartition fails for metal electrons.
(c) $\sim4$ pm in principle; factor $\frac{550}{0.0037}\approx1.5\times10^5$.

</details>

### P34 · 9 marks

(a) Show that thermal equilibrium can never invert a $2$ eV transition at $3000$ K. (b) A pulsed laser of $1.5$ eV photons ejects electrons with $K_{\max}=0.7$ eV from a metal; find $\phi$ and the process order. (c) Predict the current's intensity exponent. (3+3+3)

<details><summary>Solution</summary>

(a) Ratio $=e^{-2\times1.602\times10^{-19}/(1.381\times10^{-23}\times3000)}=e^{-7.7}=4.5\times10^{-4}\ll1$.
(b) Two-photon: $2\times1.5-\phi=0.7\Rightarrow\phi=2.3$ eV; second order.
(c) Current $\propto I^2$.

</details>

### P35 · 9 marks

(a) An excited state lives $10^{-8}$ s. Find $\Delta E$ in eV. (b) Find the resulting width in nm of a $656$ nm line. (c) The H-D isotope shift of H$\alpha$ is $0.18$ nm; is it resolvable above the natural width? (3+3+3)

<details><summary>Solution</summary>

(a) $\Delta E=\frac{\hbar}{\tau}=6.6\times10^{-8}$ eV.
(b) $\Delta\lambda=\frac{\lambda^2}{hc}\Delta E=2.3\times10^{-5}$ nm.
(c) Yes, by four orders of magnitude — isotope shifts are comfortably above the quantum floor.

</details>

### P36 · 9 marks

A photocell with $\phi=2.0$ eV is lit at $400$ nm. (a) Find $V_s$ and the saturation-current ratio when intensity triples. (b) Sketch in words the two current-voltage curves. (c) The same light is now described as a wave of intensity $10^{-3}$ W/m$^2$; compute the classical accumulation time for one atom ($A=10^{-20}$ m$^2$) and contrast with the photon picture's prediction for the first electron's arrival. (3+3+3)

<details><summary>Solution</summary>

(a) $K_{\max}=3.10-2.0=1.10$ eV, $V_s=1.10$ V; saturation current $\times3$, $V_s$ unchanged.
(b) Both curves leave the voltage axis at $-1.10$ V, rise through zero at small positive voltage, and flatten at plateaux in ratio 1:3.
(c) $t=\frac{3.2\times10^{-19}}{10^{-23}}=3.2\times10^{4}$ s; the photon picture says the first electron can arrive with the first photon, nanoseconds after switch-on — the contrast is the chapter in one number.

</details>

## Part 12 · Marking scheme and post-paper audit

| Section | Questions | Marks each | Subtotal |
|---|---|---:|---:|
| A | P1-P12 | 4 | 48 |
| B | P13-P20 | 4 | 32 |
| C | P21-P26 | 5 | 30 |
| D | P27-P36 | 9 | 90 |
| Total | 36 | | 200 |

| Question | Block tested | Question | Block tested |
|---|---|---|---|
| P1 | 2, 4 | P19 | 3, 4 |
| P2 | 3 | P20 | 10 |
| P3 | 3, 4 | P21 | 4 |
| P4 | 2, 4 | P22 | 2, 4 |
| P5 | 4 | P23 | 4 |
| P6 | 3, 4 | P24 | 4 |
| P7 | 2 | P25 | 4 |
| P8 | 3, 4 | P26 | 4, 10 |
| P9 | 4 | P27 | 3, 4 |
| P10 | 3, 10 | P28 | 3, 10 |
| P11 | 4 | P29 | 3, 4, 10 |
| P12 | 3 | P30 | 3, 10 |
| P13 | 3, 4 | P31 | 3, 10 |
| P14 | 3, 4 | P32 | 10 |
| P15 | 3 | P33 | 10 |
| P16 | 3, 10 | P34 | 10 |
| P17 | 3, 4 | P35 | 10, 3 |
| P18 | 2, 3 | P36 | 3, 4, 10 |

Blocks 2, 3, 4 and 10 are each tested by many questions, as §1.7 requires.

| If you lost marks on | Reread | Because |
|---|---|---|
| threshold or intensity questions | §3.2, §3.6 | the per-photon bookkeeping is the chapter's spine |
| graph questions | §3.5, §7.5 | slope-intercept discipline |
| wavelength-of-matter questions | §3.7-3.10 | $\lambda=\frac{h}{p}$ and its regimes |
| uncertainty estimates | §3.9, OL3 | minimisation and the virial balance |
| unit slips | §2.2, §9.5 | the eV conversion line, every time |

## Part 13 · Formula sheet

> [!abstract] Numbers to keep
> $h=6.626\times10^{-34}$ J s $=4.136\times10^{-15}$ eV s; $\hbar=1.055\times10^{-34}$ J s; $hc=1240$ eV nm; $e=1.602\times10^{-19}$ C; $m_e=9.109\times10^{-31}$ kg ($m_ec^2=511$ keV); $\lambda_C=2.43$ pm; $a_0=0.529$ Å; $13.6$ eV; $\frac{h}{e}=4.14\times10^{-15}$ V s; $\sigma$-free: visible $400$-$700$ nm $=3.1$-$1.8$ eV.

| Formula | Validity |
|---|---|
| $E=hf=\frac{1240}{\lambda[\text{nm}]}$ eV | any photon |
| $p=\frac{h}{\lambda}=\frac{E}{c}$ | massless quantum |
| $n=\frac{I}{hf}$; $n_{\text{vol}}=\frac{I}{hfc}$ | monochromatic beam |
| $F=\frac{P}{c}(1+R)$ | slow surface |
| $K_{\max}=hf-\phi$; $eV_s=K_{\max}$ | $hf\ge\phi$, one photon |
| $f_0=\frac{\phi}{h}$; $\lambda_0=\frac{1240}{\phi}$ | threshold |
| $V_s=\frac{h}{e}f-\frac{\phi}{e}$ | linear regime, clean surface |
| $\lambda=\frac{h}{p}$ | any matter |
| $\lambda_e=\frac{1.226}{\sqrt{V}}$ nm | $eV\ll511$ keV |
| $\lambda_{\text{th}}=\frac{h}{\sqrt{3mk_BT}}$ | thermal gas |
| $2\pi r=n\lambda\Leftrightarrow L=n\hbar$ | circular orbit |
| $\Delta x\Delta p\gtrsim\frac{\hbar}{2}$; $\Delta E\Delta t\gtrsim\frac{\hbar}{2}$ | always |
| $E_{\text{box}}\approx\frac{\hbar^2}{2mL^2}$ | confinement floor |
| $a_0=\frac{\hbar^2}{m_ek e^2}$; $E_1=-\frac{m_ek^2e^4}{2\hbar^2}$ | hydrogen estimate, exact for $s$-states |
| $v_p=\frac{c^2}{v}$; $v_g=v$ | relativistic matter wave |
| $\lambda_{\max}T=2.898\times10^{-3}$ m K | blackbody peak |

Work functions (eV): Cs $2.14$, Na $2.28$, Zn $4.3$, Cu $4.7$, Pt $6.35$.

## Part 14 · Checkpoint and hand-off

### 14.1 Can I do this?

Score yourself one point per honest yes; 24 plus is exam-ready.

1. Convert any wavelength in the visible band to eV in five seconds.
2. Count photons per second from power and wavelength.
3. State the five photoelectric facts and the classical failure each kills.
4. Derive the classical waiting time and quote its nine-hour value.
5. Write Einstein's equation and define every symbol.
6. Read $h$ and $\phi$ off a $V_s$-$f$ graph.
7. Predict the effect on current and $V_s$ of each of the three knobs.
8. Explain why $K_{\max}$ is a maximum.
9. Compute an electron's wavelength from its voltage.
10. Compute a neutron's or proton's wavelength from its energy.
11. Say why a cricket ball shows no fringes, with a number.
12. Derive $L=n\hbar$ from the standing-wave condition.
13. State and derive the uncertainty principle from a wave packet.
14. Derive $a_0$ and $-13.6$ eV by minimisation.
15. Explain in one sentence why the atom does not collapse.
16. Compute a natural linewidth from a lifetime.
17. Describe Davisson-Germer and verify its numbers.
18. Classify five scenarios into photon, wave or packet reasoning.
19. Compute the force of a light beam with partial reflection.
20. Quote the relativistic correction threshold for electron wavelengths.
21. Explain why thermal electrons in metals form a quantum gas.
22. Explain why lasers need pumping, with the Boltzmann number.
23. Recognise and defuse each trap of Part 8.
24. Run the ten-point audit of §9.5 without looking.

### 14.2 What the next chapter assumes

PART 24 (atomic structure) takes the standing-wave condition §3.8 and the uncertainty estimate §3.9 as inputs and adds the Coulomb force to derive $r_n$, $v_n$, $E_n$ and the Rydberg constant; it also inherits the photon bookkeeping for transitions. PART 25 inherits $E=hf$ and $p=\frac{h}{\lambda}$ for X-rays and Compton scattering, and the diffraction logic of §3.10 for Bragg's law. The shipped [[Electromagnetic-waves]] note remains the owner of radiation pressure as field theory; this chapter's photon counting is its particle-side twin.

### 14.3 Open questions you can now attack

Why does the Sun's spectrum peak where it does, and what does that say about its surface temperature? How small a structure could a $1$ MeV electron microscope see? Why do metals glow at temperatures where classical physics says they should already be blinding? Each is answered by the tools above plus one later PART.
