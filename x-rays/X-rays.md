---
title: X-rays, Moseley's Law, Bragg Diffraction & the Compton Effect
part: 25
slug: x-rays
source: Cengage Optics and Modern Physics, ch 4 Atomic Physics pp. 4.25-4.32 (X-rays, X-ray spectra, Moseley's law)
aliases: [X-rays, Moseley, Bragg, Compton]
tags: [jee-advanced, olympiad, modern-physics, quantum]
---

# X-rays, Moseley's Law, Bragg Diffraction & the Compton Effect — first principles to Olympiad

> [!abstract] How to use this chapter
> Three passes. Pass 1: Parts 0-4 — the tube, the two spectra, Moseley, absorption, Bragg, Compton. Pass 2: Parts 5-9 — exemplars, archetypes, traps, playbook. Pass 3: Parts 10-14 — the Olympiad layer (Compton twice, Avogadro from a crystal, inverse Compton, doses), the paper, the sheet, the checkpoint. Every number recomputed; every boxed result carries its validity condition.

## Part 0 · Orientation

### 0.1 What you will be able to do

After this chapter you can: compute the Duane-Hunt cutoff for any tube voltage and explain why the short-wavelength end is sharp; read a characteristic spectrum and find the minimum voltage that produces a given line; derive Moseley's law from the screened Bohr picture and identify an element from its lines; work the exponential absorption law and half-value thicknesses; derive Bragg's law with a foolproof angle convention and extract lattice spacings and Avogadro's number from a crystal; derive the Compton shift twice, with the electron's recoil energy and angle; and place all three effects (photoelectric, Compton, diffraction) in the single table of what each proves about the photon.

### 0.2 The one idea

X-rays are photon physics with enough energy to see atoms and to knock electrons free — and Compton scattering is the experiment that proves the photon carries momentum.

### 0.3 Prerequisite self-check

1. What is the photon energy of a $0.1$ nm X-ray, in keV?
2. An electron falls through $50$ kV. What is the richest photon one such electron can make?
3. State the standing-wave diffraction condition for a grating of spacing $d$ at glancing angle $\theta$.
4. Write energy and momentum conservation for a photon scattering off a free electron at rest.
5. What is $m_ec^2$, and why does it set the Compton scale?
6. Quote the de Broglie relation and say which experiment of PART 23 verified it.
7. What does $I=I_0e^{-\mu x}$ describe, and what is a half-value thickness?

<details><summary>Solution</summary>

1. $E=\frac{1240}{0.1}=12.4$ keV.
2. $50$ keV: the whole kinetic energy in one photon, the Duane-Hunt limit.
3. $2d\sin\theta=n\lambda$, with $\theta$ measured from the plane.
4. $hf+m_ec^2=hf'+E_e$ and $\frac{h}{\lambda}=\frac{h}{\lambda'}\cos\theta+p_e\cos\phi$, $\frac{h}{\lambda'}\sin\theta=p_e\sin\phi$.
5. $511$ keV; the Compton shift is $\frac{h}{m_ec}(1-\cos\theta)$.
6. $\lambda=\frac{h}{p}$, verified by Davisson-Germer ([[Photoelectric-effect]] §3.10).
7. Exponential attenuation; the thickness cutting intensity to one half, $x_{1/2}=\frac{\ln2}{\mu}$.

</details>

### 0.4 Numbers to keep

> [!abstract] Numbers to keep
> $hc=1240$ eV nm $=1.24$ keV pm; $\lambda_C=\frac{h}{m_ec}=2.426$ pm; $m_ec^2=511$ keV; Duane-Hunt $\lambda_{\min}=\frac{1240}{V[\text{V}]}$ nm $=\frac{1.24\times10^6}{V}$ pm; Moseley $f_{K\alpha}=\frac34cR(Z-1)^2$ (Cu K$\alpha$: $154$ pm, needs $\sim9$ kV); NaCl $d=0.282$ nm, $\rho=2165$ kg/m$^3$, $N_A=6.02\times10^{23}$; Pb half-value layer at 100 keV $\approx0.12$ mm; Compton shifts: $90^\circ$ $2.43$ pm, $180^\circ$ $4.86$ pm; pair threshold $1.022$ MeV; X-ray tube efficiency $\sim10^{-9}ZV$ (about 1 % at 100 kV on tungsten).

### 0.5 Three passes

Pass 1 for the six mechanisms (bremsstrahlung, characteristic cascade, Moseley screening, absorption, Bragg reflection, Compton recoil). Pass 2 for craft. Pass 3 timed paper, then audit.

### 0.6 Cengage coverage map

The sweep read the chapter 4 contents page; the X-ray sections sit at pp. 4.25-4.32 inside ch 4 Atomic Physics, so the map is keyed to those section names. Bragg diffraction, Compton scattering, Avogadro-from-crystal and pair production are not headings of this volume — they are INPhO/IPhO syllabus items added by the sweep and marked so.

| Cengage section (ch 4, X-ray half) | What it establishes | Where it lives here | Status |
|---|---|---|---|
| Discovery of X-rays (4.25) | history and phenomenology | §1.1 | stated + used |
| Production of X-rays, Coolidge's tube (4.25) | thermionic source, acceleration, target, vacuum, window | §3.1 | derived |
| Properties of X-rays (4.25) | penetration, fluorescence, photographic action, neutrality | §2.4, §3.5 | stated + used |
| Application of X-rays (4.26) | imaging, crystallography, therapy | §3.5, §3.8 | stated + used |
| X-ray absorption (4.27) | $I=I_0e^{-\mu x}$, half-value thickness | §3.5, E5 | derived |
| X-ray spectra and origin of X-rays (4.27) | continuous plus characteristic; vacancy cascade | §3.2-3.3 | derived |
| Moseley's law (4.30) | $\sqrt f=a(Z-b)$; ordering the table | §3.4, E4 | derived |
| Solved examples band (4.32) | standard shapes | §6.1, Q1-Q28 | exercised |
| Exercise bands (4.42-4.94) | exam formats | Part 11 | exercised |
| Duane-Hunt cutoff as measurement of h/e (added by sweep) | the sharp edge | §3.2, OL5 | added by sweep |
| Bragg diffraction and powder rings (added by sweep) | $2d\sin\theta=n\lambda$ | §3.6-3.8 | added by sweep |
| Avogadro from a crystal (added by sweep) | the classic olympiad determination | §3.8, OL6 | added by sweep |
| Compton effect, twice derived (added by sweep) | photon momentum proven | §3.9-3.10, OL1-OL2 | added by sweep |
| Pair production threshold (added by sweep) | $2m_ec^2$ | §3.11 | added by sweep |
| Production efficiency and anode heat (added by sweep) | engineering estimate | §3.1, OL7 | added by sweep |

## Part 1 · Intuition first

### 1.1 The inverse photoelectric effect

Run the photoelectric effect backwards. There, a photon hands an electron enough energy to leave a metal; here, a fast electron slams into a metal and hands its energy to photons. Two things happen at the target. Most electrons brake in the nuclear field and shed their energy as a smooth smear of photons — bremsstrahlung, "braking radiation" — and the smear has a sharp rich end: no photon can exceed the electron's kinetic energy. That is the Duane-Hunt limit, Einstein's equation read right-to-left. A few electrons knock inner-shell electrons out; the atom refills the hole and emits a photon whose energy is the atom's own ladder — sharp, element-specific lines riding on the smear.

### 1.2 A ruler made of crystals

An X-ray's wavelength is a few tenths of a nm — the same scale as the spacing of atoms in a crystal. No manufactured grating is that fine, but every crystal is a three-dimensional grating waiting for exactly this light. When the reflections from successive atomic planes add in phase, a flash appears at a definite angle: Bragg's law. Turn the argument around and the crystal becomes a ruler — for wavelengths, for lattice spacings, and, with a density measurement, for Avogadro's number.

### 1.3 The photon catches its momentum

Shine X-rays on electrons and the scattered beam contains two wavelengths: the original, and one shifted longer by an amount that depends only on the scattering angle. Classical waves cannot do that — a wave scatters at the frequency it arrives. A particle can: the shift is exactly the kinematics of a relativistic billiard ball of momentum $\frac{h}{\lambda}$ striking an electron. Compton's 1923 measurement is the single most direct proof that the photon carries momentum, closing the triangle that the photoelectric effect (energy) and diffraction (wave) began.

> [!info] Why X-rays and not visible light for Compton
> The shift is at most $4.9$ pm; against a $550$ nm photon that is one part in $10^5$, invisible, while against a $100$ pm photon it is several percent, obvious. High energy is not a luxury here; it is the resolution.

## Part 2 · Definitions and bookkeeping

### 2.1 The symbol table

| Symbol | Meaning | Unit | Notes |
|---|---|---|---|
| $V$ | tube voltage | V | sets $\lambda_{\min}$ |
| $\lambda_{\min}$ | Duane-Hunt cutoff | pm | $\frac{1.24\times10^6}{V}$ pm |
| $Z$ | target atomic number | — | lines scale as $(Z-1)^2$ |
| $\mu$ | linear attenuation coefficient | m$^{-1}$ | energy- and material-dependent |
| $x_{1/2}$ | half-value thickness | m | $\frac{\ln2}{\mu}$ |
| $d$ | plane spacing | pm or nm | NaCl $0.282$ nm |
| $\theta$ | glancing angle from the plane | deg | not the angle from the normal |
| $n$ | Bragg order | — | integer |
| $\lambda_C$ | Compton wavelength | pm | $2.426$ |
| $\theta$, $\phi$ | photon and electron scattering angles | deg | §3.10 |
| $\eta$ | tube efficiency | — | $\sim10^{-9}ZV$ |

### 2.2 Units and bands

X-ray energies in keV, wavelengths in pm ($1$ nm $=1000$ pm), voltages in kV. The conversion $E[\text{keV}]=\frac{1.24}{\lambda[\text{nm}]}=\frac{1240}{\lambda[\text{pm}]}$ keeps everything one division. Diagnostic X-rays: $10$-$100$ keV; characteristic K lines of heavy targets: tens of keV; gamma rays overlap the band from the nuclear side (PART 26).

### 2.3 Sign and angle conventions

Bragg's $\theta$ is measured **from the plane**, the glancing angle; the path difference is $2d\sin\theta$. This is the opposite convention from a transmission grating's angle-from-normal, and it is the single most common sign of a muddled solution. Compton's $\theta$ is the photon's deflection from its original direction; $\phi$ the electron's.

> [!warning] Condition of validity
> Bragg's law treats planes as mirrors and ignores which atoms sit where; absent reflections (structure factors) are the correction, named in §3.8. Compton's free-electron formula applies when the photon energy dwarfs the electron's binding; the unshifted line is the bound-electron remainder.

### 2.4 Assumptions and what is not here

Assumed: single scattering events; electrons at rest for Compton; monochromatic lines where stated; exponential attenuation (narrow-beam geometry). Not here: full quantum electrodynamics of scattering (Klein-Nishina named in §10), detailed crystal structure factors, X-ray optics and lenses, medical dosimetry beyond one order-of-magnitude.

> [!question] Exam note
> The exam loves the double spectrum drawn together: smear plus lines. If you can sketch it, label $\lambda_{\min}$, the K$\alpha$/K$\beta$ lines, and explain each feature's origin and its voltage dependence, the chapter's core is examinable.

## Part 3 · Core derivations

### 3.1 Making X-rays: the Coolidge tube

A hot filament boils off electrons (thermionic emission, the same physics as the photoelectric cell's cousin in PART 23); a voltage $V$ of tens of kV accelerates them; they strike a heavy metal target (tungsten, $Z=74$: bremsstrahlung power grows steeply with $Z$, and a high melting point survives the heat) inside a vacuum, and the X-rays leave through a thin window. Rotating anodes spread the heat, because only about one percent of the electron power becomes X-rays.

Efficiency estimate: the fraction of electron energy radiated is of order

$$
\eta\approx10^{-9}\,Z\,V, \qquad (3.1)
$$

with $V$ in volts: tungsten at $100$ kV gives $\eta\approx7\times10^{-3}$, the quoted one percent. A dental tube at $70$ kV and $10$ mA takes $700$ W of electron power and radiates a few watts of X-rays; the other $695$ W is an engineering problem — the rotating anode's heat capacity and cooling set the duty cycle.

> [!abstract] DIAGRAM D25.1 · The Coolidge tube in section
> *Show:* a glass envelope under vacuum; a heated filament cathode with its focusing cup; the angled tungsten anode with a rotating stem and cooling fins; the electron beam converging on the focal spot; the X-ray fan leaving through a window; the high-voltage supply labelled.
> *Search:* "Coolidge tube X-ray production diagram filament anode rotating"
> *Used in:* §3.1.

How many X-ray photons per second? A $700$ W tube at one percent efficiency radiates $7$ W; taking a mean photon energy of $30$ keV $=4.8\times10^{-15}$ J, that is $\sim1.5\times10^{15}$ photons per second.

### 3.2 The continuous spectrum and the Duane-Hunt limit

An electron braking in the nuclear field can shed any fraction of its energy as one photon, so the spectrum is continuous — but never beyond the whole amount. One electron of charge $e$ falling through $V$ carries $eV$; the richest possible photon has $hf_{\max}=eV$, hence

$$
\lambda_{\min}=\frac{hc}{eV}=\frac{1.24\times10^6}{V\ [\text{V}]}\ \text{pm}. \qquad (3.2)
$$

Numbers: $30$ kV gives $41.3$ pm, $50$ kV gives $24.8$ pm, $100$ kV gives $12.4$ pm. Raising $V$ pushes the cutoff to shorter wavelengths and drags the whole smear up and with it; changing the target changes the intensity (roughly $\propto Z$) but not the cutoff, which depends only on $V$. The short end is sharp because it is a one-electron-one-photon extreme; the long end fades gently because soft photons are reabsorbed in the target and window.

> [!abstract] DIAGRAM D25.2 · The continuous spectrum at three voltages
> *Show:* intensity against wavelength for 30, 50 and 100 kV on the same target; each curve rising from a sharp cutoff, peaking, and falling; the cutoffs at 41.3, 24.8, 12.4 pm marked and joined by the hyperbola lambda-min proportional to 1/V; no characteristic lines in this panel.
> *Search:* "bremsstrahlung continuous X-ray spectrum cutoff voltage dependence"
> *Used in:* §3.2.

Historically the cutoff was a precision instrument: plotting $\lambda_{\min}$ against $\frac1V$ measures $\frac{h}{e}$ — the Duane-Hunt limit as the inverse photoelectric effect, matching Millikan's $V_s$-$f$ slope from the other direction (OL5).

### 3.3 The characteristic spectrum

A fast electron can also eject a K-shell electron. The vacancy is refilled from above: an L electron dropping to K emits K$\alpha$, an M electron K$\beta$; the new L vacancy then produces L lines. Because the levels are the atom's own, the lines are sharp and element-specific — a fingerprint that survives chemistry, which is how Moseley counted the elements.

The threshold logic examiners love: a line appears only when the tube voltage can create the vacancy it comes from. For copper the K shell binds about $9$ keV, so below $\sim9$ kV the Cu K lines are absent whatever the current, while the continuous spectrum is present from the first volt. A spectrum without its characteristic lines is a spectrum below its threshold voltage.

> [!abstract] DIAGRAM D25.3 · Characteristic lines on the continuous spectrum
> *Show:* one curve of intensity against wavelength: the bremsstrahlung hump with its cutoff, and two sharp spikes labelled K-alpha and K-beta (K-beta at shorter wavelength, smaller); a second dashed curve at lower voltage showing the hump without the spikes, captioned "below the K threshold".
> *Search:* "X-ray spectrum continuous characteristic K alpha K beta lines"
> *Used in:* §3.3.

> [!abstract] DIAGRAM D25.4 · The K-shell vacancy cascade
> *Show:* three levels K, L, M; an outgoing arrow from K labelled "ejected electron"; a downward arrow M to K labelled K-beta, L to K labelled K-alpha, M to L labelled L-alpha; energies in keV for copper beside the arrows.
> *Search:* "characteristic X-ray emission K alpha L shell vacancy cascade diagram"
> *Used in:* §3.3.

### 3.4 Moseley's law, derived from the screened Bohr picture

The K$\alpha$ transition is hydrogen-like arithmetic in a nucleus screened by the one remaining K electron: the falling L electron sees charge $(Z-1)e$, so

$$
E_{K\alpha}=\frac34\times13.6\,(Z-1)^2\ \text{eV},\qquad \sqrt{f}=\sqrt{\tfrac34cR}\,(Z-1). \qquad (3.3)
$$

Moseley's 1913 plot of $\sqrt f$ against $Z$ is a straight line with intercept $1$ — and gaps where no element exists, which is how the missing elements (43, 61, 72, 75) were identified before they were found. For copper: $f=\frac34\times3\times10^8\times1.097\times10^7\times28^2=1.93\times10^{18}$ Hz, $\lambda=155$ pm, against the measured $154$ pm. The shielding constant $b\approx1$ for K$\alpha$; L lines use larger $b$ (more inner electrons screening), which the exam phrases as "Moseley's constants $a$ and $b$".

> [!info] Why the K-alpha photon is keV while optical photons are eV
> The inner orbit's energy scales as $(Z-1)^2$ and its radius as $\frac{1}{Z-1}$: for copper the factor is $\sim800$, squared into the energy. Optical lines are outer-electron business; X-ray lines are the deep atom.

> [!abstract] DIAGRAM D25.5 · Moseley's line
> *Show:* sqrt(f) vertical against Z horizontal; a straight line through measured points; the intercept at Z = 1 marked; gaps at Z = 43 and 61 shown as empty slots on the axis; copper highlighted.
> *Search:* "Moseley law plot sqrt frequency Z straight line missing elements"
> *Used in:* §3.4.

### 3.5 Absorption and imaging

A narrow beam through thickness $x$ of material loses a fixed *fraction* per unit length, because every layer presents the same number of absorbers:

$$
I=I_0e^{-\mu x},\qquad x_{1/2}=\frac{\ln2}{\mu}. \qquad (3.4)
$$

$\mu$ falls with photon energy (roughly $\lambda^3$ away from edges) and rises steeply with atomic number (roughly $Z^3$-$Z^4$): bone's calcium absorbs far more than tissue's carbon and oxygen, which is the entire physics of a radiograph; barium and iodine contrast media exploit the same $Z$ hunger. Lead at 100 keV has $x_{1/2}\approx0.12$ mm, so $\mu=\frac{\ln2}{0.012\ \text{cm}}=58$ cm$^{-1}$. Soft X-rays image with better contrast but deposit more dose — the trade-off is set by the same $\mu(E)$ curve. Computed tomography is this law inverted numerically: many projections, one absorption map per slice, stated here in one paragraph as an application of Eq. (3.4), not derived.

> [!abstract] DIAGRAM D25.6 · The attenuation curve with half-value thickness
> *Show:* I over I0 against thickness, an exponential fall; the half and quarter levels marked with dashed lines at x-half and 2 x-half; a second steeper curve for bone against a shallower one for tissue, the contrast region shaded.
> *Search:* "X-ray attenuation exponential half value thickness bone tissue contrast"
> *Used in:* §3.5.

### 3.6 X-ray diffraction: why crystals

A grating resolves structure of order its spacing. Visible light ($500$ nm) sees a crystal's planes ($0.3$ nm) as perfectly smooth — the ratio is $10^3$ too small, and no Bragg angle exists. X-rays at $100$ pm match the spacing: the crystal is the only grating fine enough, exactly as the electron's wavelength made crystals the grating for matter waves in PART 23. Laue's 1912 spot pattern was the first proof both that X-rays are waves and that crystals are lattices — one experiment, two discoveries.

### 3.7 Bragg's law, with the angle made foolproof

Two parallel rays strike successive planes at glancing angle $\theta$ (from the plane, never from the normal). The lower ray travels an extra $d\sin\theta$ down and $d\sin\theta$ up:

$$
2d\sin\theta=n\lambda. \qquad (3.5)
$$

Orders $n=1,2,3$ are the same geometry with $n$ wavelengths of path; the highest visible order satisfies $n\le\frac{2d}{\lambda}$. Because $\theta$ is from the plane, the diffracted beam leaves at $2\theta$ from the incident direction — the angle the detector actually reads is twice the Bragg angle. A powder of randomly oriented crystallites turns each order into a cone, and the film records rings.

> [!abstract] DIAGRAM D25.7 · The Bragg geometry
> *Show:* two parallel atomic planes separated by d; two incoming rays at glancing angle theta measured from the plane, highlighted with an arc; the extra path 2 d sin theta drawn as two dashed perpendiculars; the reflected rays in phase; a note "theta is from the plane, not the normal".
> *Search:* "Bragg diffraction geometry glancing angle path difference 2d sin theta"
> *Used in:* §3.7, E7.

> [!abstract] DIAGRAM D25.8 · Powder rings
> *Show:* a Debye-Scherrer camera: incident beam, powder sample at centre, concentric arcs on the film; two cones drawn from the sample to the arcs; caption "each ring is one order and one family of planes".
> *Search:* "powder X-ray diffraction Debye Scherrer rings pattern"
> *Used in:* §3.7.

### 3.8 Diffraction in practice: lattice constants and Avogadro

Measure $\theta$ for a known $\lambda$: $d=\frac{n\lambda}{2\sin\theta}$. For NaCl with Cu K$\alpha$ ($154$ pm), first order at $\sin\theta=\frac{154}{2\times282}=0.273$, $\theta=15.8^\circ$; the highest order is $n\le\frac{564}{154}=3.65$, so three orders.

The classic determination: NaCl's cubic cell of side $a$ holds alternating ions; the volume per ion pair is $2d^3$ with $d$ the adjacent-ion spacing. Density gives the same volume as $\frac{M}{\rho N_A}$:

$$
N_A=\frac{M}{2\rho d^3}. \qquad (3.6)
$$

With $M=58.44$ g/mol, $\rho=2165$ kg/m$^3$, $d=0.282$ nm: $N_A=\frac{0.05844}{2\times2165\times(2.82\times10^{-10})^3}=6.02\times10^{23}$. A wavelength, an angle and a balance — Avogadro's number from a crystal. Some reflections are absent because atoms at different sites in the cell scatter out of phase (the structure factor's first appearance): the pattern's missing lines are themselves structural information.

> [!abstract] DIAGRAM D25.9 · The NaCl cell and the spacing d
> *Show:* a cube with alternating Na and Cl spheres; the edge a and the half-edge d labelled; one plane family shaded; the volume-per-pair argument annotated.
> *Search:* "sodium chloride crystal structure unit cell spacing Avogadro"
> *Used in:* §3.8, OL6.

### 3.9 The Compton effect: the experiment

Compton sent monochromatic X-rays ($\sim100$ pm, molybdenum K) onto graphite and measured the scattered beam at angles $\theta$. Two peaks: one at the original wavelength, one shifted by $\Delta\lambda$ that grows with $\theta$ and depends on nothing else — not the target, not the intensity. The shifted peak is the free-electron scatter; the unshifted one comes from electrons so tightly bound that the whole atom recoils, making $m$ in $\frac{h}{mc}(1-\cos\theta)$ the atomic mass and the shift unobservably small. Classical electrodynamics predicts a single unshifted line at every angle; the extra moving line killed it.

> [!abstract] DIAGRAM D25.10 · The measured Compton spectrum
> *Show:* intensity against wavelength at three angles (0, 90, 135 degrees): at 0 one peak; at 90 two peaks separated by 2.43 pm; at 135 the shifted peak taller and 4 pm away; the unshifted peak fixed in position.
> *Search:* "Compton effect scattered X-ray spectrum two peaks wavelength shift angle"
> *Used in:* §3.9.

### 3.10 Compton's derivation

A photon of momentum $\frac{h}{\lambda}$ strikes an electron at rest. Energy: $\frac{hc}{\lambda}+m_ec^2=\frac{hc}{\lambda'}+E_e$. Momentum along and across the beam: $\frac{h}{\lambda}=\frac{h}{\lambda'}\cos\theta+p_e\cos\phi$ and $\frac{h}{\lambda'}\sin\theta=p_e\sin\phi$. Eliminate $\phi$ and use $E_e^2=(p_ec)^2+(m_ec^2)^2$; the algebra (OL1) or the momentum triangle with the four-vector invariant (OL2) yields

$$
\Delta\lambda=\lambda'-\lambda=\frac{h}{m_ec}(1-\cos\theta)=2.426\,(1-\cos\theta)\ \text{pm}. \qquad (3.7)
$$

Extremes: $\theta=0$: no shift; $90^\circ$: $2.43$ pm; $180^\circ$: $4.86$ pm, the maximum. The electron's recoil kinetic energy follows from energy conservation; writing $x=\frac{hf}{m_ec^2}$,

$$
K_e=hf\,\frac{x(1-\cos\theta)}{1+x(1-\cos\theta)}, \qquad (3.8)
$$

so at $90^\circ$ for a $12.4$ keV photon ($x=0.0243$): $K_e=0.29$ keV; at $180^\circ$: $0.57$ keV. The electron's angle satisfies $\tan\phi=\frac{1}{(1+x)\tan\frac{\theta}{2}}$: never backwards, at most $90^\circ$.

> [!abstract] DIAGRAM D25.11 · Compton scattering geometry and momentum triangle
> *Show:* left panel: incoming photon arrow, outgoing photon at theta, recoil electron at phi; right panel: the triangle of momenta h/lambda = h/lambda-prime + p-e with the angles marked.
> *Search:* "Compton scattering diagram photon electron recoil momentum triangle"
> *Used in:* §3.10, OL1.

> [!abstract] DIAGRAM D25.12 · The shift against angle
> *Show:* delta-lambda against theta from 0 to 180 degrees, the curve 2.43(1-cos theta); points marked at 90 (2.43 pm) and 180 (4.86 pm); a flat dashed line at 0.005 pm labelled "visible light, magnified ten thousand times" to show invisibility.
> *Search:* "Compton wavelength shift versus scattering angle curve"
> *Used in:* §3.10-3.11.

### 3.11 Why it matters

Scale check: for $550$ nm light the maximum shift is $\frac{4.86\ \text{pm}}{550\ \text{nm}}=9\times10^{-6}$ of the wavelength — unresolvable, which is why Thomson's classical no-shift picture works for visible light and why Compton needed X-rays. The effect is the decisive evidence that the photon carries momentum $p=\frac{h}{\lambda}$: energy quantisation (photoelectric) plus momentum quantisation (Compton) plus interference (diffraction) is the complete photon. Inverse Compton — a fast electron boosting a soft photon — is the same kinematics reversed, important in astrophysics (one paragraph; the moving-mirror analogue is OL3). At photon energies above $2m_ec^2=1.022$ MeV the photon can disappear into an electron-positron pair near a nucleus — the threshold where the photon picture hands over to PART 28's relativistic bookkeeping.

> [!abstract] DIAGRAM D25.13 · The photon evidence table as a spectrum map
> *Show:* a horizontal energy axis from 1 eV to 10 MeV; three bands highlighted: photoelectric dominant at a few eV, diffraction at keV with crystals, Compton at tens to hundreds of keV, pair production beyond 1.02 MeV marked with a vertical line; each band labelled with what it proves (energy quantum, wave, momentum quantum).
> *Search:* "photon experiments energy scale photoelectric Compton pair production"
> *Used in:* §3.11-3.12.

> [!abstract] DIAGRAM D25.14 · Pair production at the threshold
> *Show:* a photon line ending at a nucleus with an electron and positron curving away in opposite senses in a magnetic field; the caption "needs 1.022 MeV and a nucleus to take momentum".
> *Search:* "pair production electron positron photon nucleus diagram"
> *Used in:* §3.11.

### 3.12 Cross-topic synthesis

| Experiment | Proves | Owns | Needs |
|---|---|---|---|
| Photoelectric (PART 23) | energy comes in quanta $hf$ | thresholds, $V_s$ | — |
| Electron and X-ray diffraction | wave character, $\lambda$ | gratings, lattices | wave logic of [[Wave-optics]] |
| Compton | momentum $p=\frac{h}{\lambda}$ | recoil kinematics | relativity of PART 28 for the full frame |
| Blackbody (PART 23 §3.1) | quantised exchange | $T$ scaling | thermodynamics |

The high-energy end of the spectrum chart links to [[Electromagnetic-waves]]; the atomic ladder the lines ride on is PART 24's; the nucleus that absorbs recoil momentum is PART 26's.

## Part 4 · Results, limits and the validity ledger

### 4.1 Boxed results

$$
\boxed{\lambda_{\min}=\frac{hc}{eV}=\frac{1.24\times10^6}{V[\text{V}]}\ \text{pm}} \qquad (4.1)
$$

the continuous spectrum's edge only; characteristic lines ignore it.

$$
\boxed{E_{K\alpha}=\frac34\times13.6\,(Z-1)^2\ \text{eV}} \qquad (4.2)
$$

screened hydrogenic; L lines need larger screening constants.

$$
\boxed{I=I_0e^{-\mu x},\quad x_{1/2}=\frac{\ln2}{\mu}} \qquad (4.3)
$$

narrow-beam geometry; broad beams add scatter and need build-up factors (named, not treated).

$$
\boxed{2d\sin\theta=n\lambda} \qquad (4.4)
$$

$\theta$ from the plane; elastic, coherent scattering.

$$
\boxed{\Delta\lambda=\frac{h}{m_ec}(1-\cos\theta),\quad K_e=hf\frac{x(1-\cos\theta)}{1+x(1-\cos\theta)}} \qquad (4.5)
$$

free electron at rest; bound electrons give the unshifted line.

### 4.2 Limit checks

- $V\to0$: $\lambda_{\min}\to\infty$, no X-rays, correct.
- $Z\to1$ in Eq. (4.2): hydrogen's $10.2$ eV line returns — K$\alpha$ is Lyman $\alpha$ in disguise, correct.
- $\theta\to0$ in Eq. (4.5): shift vanishes, forward scattering undisturbed, correct.
- $m_e\to\infty$ (bound to a heavy atom): shift vanishes, the unshifted line, correct.
- $\lambda\gg d$: no Bragg angle exists, visible light on crystals, correct.
- $hf\ll m_ec^2$: $K_e\to0$, the classical Thomson limit, correct.

### 4.3 Which formula when

| Given | Need | Use |
|---|---|---|
| tube voltage | cutoff | Eq. (4.1) |
| element | K$\alpha$ | Eq. (4.2) |
| line energy | minimum voltage | $eV\ge E_{\text{K edge}}$ |
| thickness | transmission | Eq. (4.3) |
| $\theta$, known $\lambda$ | $d$ | Eq. (4.4) |
| $d$, $\rho$, $M$ | $N_A$ | Eq. (3.6) |
| $\theta$ | Compton shift, recoil | Eq. (4.5) |
| shift | identify process | compare $2.43$ pm scale |

### 4.4 Concept checks

**C1 — concept check.** Why is the Duane-Hunt edge sharp but the long-wavelength end soft?

<details><summary>Answer</summary>

The edge is a one-electron extreme; the soft end is smeared by partial braking and self-absorption.

</details>

**C2 — concept check.** Raising the tube voltage changes the characteristic lines' wavelengths?

<details><summary>Answer</summary>

No: the lines are the atom's ladder; voltage only switches them on above threshold and changes their intensity.

</details>

**C3 — concept check.** Why does bone show white on a radiograph?

<details><summary>Answer</summary>

Calcium's higher Z absorbs more, fewer photons reach the film behind bone.

</details>

**C4 — concept check.** In Bragg's law, theta is measured from what?

<details><summary>Answer</summary>

From the plane — the glancing angle; the detector reads 2 theta from the beam.

</details>

**C5 — concept check.** The highest Bragg order for lambda = d?

<details><summary>Answer</summary>

$n\le2$: orders 1 and 2.

</details>

**C6 — concept check.** Why is there an unshifted Compton line?

<details><summary>Answer</summary>

Tightly bound electrons make the whole atom recoil; the mass in the shift formula is atomic, the shift negligible.

</details>

**C7 — concept check.** Why did Compton use X-rays rather than light?

<details><summary>Answer</summary>

The shift is absolute (a few pm); only a comparably small wavelength makes it visible.

</details>

**C8 — concept check.** What sets the pair-production threshold?

<details><summary>Answer</summary>

$2m_ec^2=1.022$ MeV, plus a nucleus to absorb momentum.

</details>

**C9 — concept check.** The Compton shift depends on the target material?

<details><summary>Answer</summary>

No: only on theta, because the electron is treated free and at rest.

</details>

**C10 — concept check.** A 100 keV photon scatters at 90 degrees. Order of the electron's kinetic energy?

<details><summary>Answer</summary>

$x=0.196$; $K\approx100\times\frac{0.196}{1.196}\approx16$ keV.

</details>

**C11 — concept check.** Why does Moseley's line use Z minus one for K-alpha?

<details><summary>Answer</summary>

The remaining 1s electron screens one unit of nuclear charge from the falling L electron.

</details>

**C12 — concept check.** X-ray tube efficiency at 100 kV on tungsten, order?

<details><summary>Answer</summary>

One percent; the rest is heat.

</details>

**C13 — concept check.** Three orders visible means what inequality?

<details><summary>Answer</summary>

$3\le\frac{2d}{\lambda}<4$.

</details>

**C14 — concept check.** Which two numbers does the Duane-Hunt plot measure?

<details><summary>Answer</summary>

The slope of lambda-min against 1/V is hc/e: with e known, h.

</details>

## Part 5 · Worked exemplars

### E1 — The cutoff at 50 kV

Find the minimum wavelength from a 50 kV tube.

> [!success] Check
> Doubling V must halve lambda-min.

<details><summary>Solution</summary>

**Method.** Eq. (4.1): $\lambda_{\min}=\frac{1.24\times10^6}{5\times10^4}=24.8$ pm. At 100 kV it is 12.4 pm, exactly half.

</details>

### E2 — Maximum photon energy and the photon count

A 100 kV tube runs at 10 mA with efficiency 1 %. Richest photon energy, X-ray power, and photons per second at a mean 30 keV?

> [!success] Check
> The richest photon equals eV; the count is power over mean energy.

<details><summary>Solution</summary>

**Method.** $E_{\max}=100$ keV. Electron power $P=VI=1000$ W; X-ray power $10$ W; $N=\frac{10}{30\times10^3\times1.602\times10^{-19}}=2.1\times10^{15}$ s$^{-1}$.

</details>

### E3 — The threshold voltage for copper's K lines

Copper's K shell binds about 9 keV. What is the minimum tube voltage for its K-alpha line, and what changes if the voltage is halved?

> [!success] Check
> Below threshold the lines vanish while the smear survives.

<details><summary>Solution</summary>

**Method.** $V_{\min}\approx9$ kV. At 4.5 kV the characteristic lines are absent; the continuous spectrum, with cutoff 276 pm, remains.

</details>

### E4 — Identify the element from a K-alpha line

An unknown target's K-alpha is at 72 pm. Identify it.

> [!success] Check
> The answer must sit between copper (154 pm) and molybdenum's neighbours in Z.

<details><summary>Solution</summary>

**Method.** $f=\frac{c}{\lambda}=4.16\times10^{18}$ Hz; $(Z-1)^2=\frac{f}{\frac34cR}=\frac{4.16\times10^{18}}{2.47\times10^{15}}=1686$; $Z-1=41$; $Z=42$, molybdenum.

</details>

### E5 — Through half a millimetre of lead

Lead's half-value thickness at 100 keV is 0.12 mm. What fraction of a narrow beam survives 0.5 mm?

> [!success] Check
> 0.5 mm is about 4.2 half-layers: 2 to the minus 4.2 is about 5 %.

<details><summary>Solution</summary>

**Method.** $\mu=\frac{\ln2}{0.012\ \text{cm}}=57.8$ cm$^{-1}$; $I/I_0=e^{-57.8\times0.05}=e^{-2.89}=0.055$.

</details>

### E6 — First-order Bragg angle for NaCl

Cu K-alpha (154 pm) on NaCl planes with d = 282 pm. First-order glancing angle?

> [!success] Check
> sin theta must be below 1 and the angle small-ish: the plane convention.

<details><summary>Solution</summary>

**Method.** $\sin\theta=\frac{154}{2\times282}=0.273$; $\theta=15.8^\circ$; the detector sits at $2\theta=31.7^\circ$ from the beam.

</details>

### E7 — How many orders fit?

With the same geometry, the highest observable order?

> [!success] Check
> n must satisfy n at most 2d over lambda.

<details><summary>Solution</summary>

**Method.** $\frac{2d}{\lambda}=\frac{564}{154}=3.66$: orders 1, 2, 3.

</details>

### E8 — Avogadro from a crystal

Using d = 0.282 nm, rho = 2165 kg per cubic metre, M = 58.44 g per mole, compute N-A.

> [!success] Check
> The result must land within a percent of 6.022e23.

<details><summary>Solution</summary>

**Method.** Eq. (3.6): $N_A=\frac{0.05844}{2\times2165\times(2.82\times10^{-10})^3}=\frac{0.05844}{9.71\times10^{-26}}=6.02\times10^{23}$ mol$^{-1}$.

</details>

### E9 — Compton at 90 degrees for a 100 keV photon

Shift and electron kinetic energy.

> [!success] Check
> Shift 2.43 pm; K must be below the photon energy and above zero.

<details><summary>Solution</summary>

**Method.** $\Delta\lambda=2.43$ pm. $x=\frac{100}{511}=0.196$; $K=100\times\frac{0.196}{1.196}=16.4$ keV; the scattered photon keeps $83.6$ keV at $102.4$ pm.

</details>

### E10 — The electron's recoil angle

For the same event, the electron's angle phi?

> [!success] Check
> phi must be below 90 degrees; at theta = 180 it must be 0.

<details><summary>Solution</summary>

**Method.** $\tan\phi=\frac{1}{(1+x)\tan45^\circ}=\frac{1}{1.196}=0.836$; $\phi=39.9^\circ$, forward of the perpendicular, as momentum demands.

</details>

### E11 — The shift for visible light

Maximum Compton shift as a fraction of a 550 nm wavelength?

> [!success] Check
> Of order 1e-5: the reason light shows no Compton effect.

<details><summary>Solution</summary>

**Method.** $\frac{4.86\ \text{pm}}{550\ \text{nm}}=8.8\times10^{-6}$; at 90 degrees half that, $4.4\times10^{-6}$.

</details>

### E12 — Pair production budget

A 2 MeV photon converts near a nucleus. Total kinetic energy of the pair?

> [!success] Check
> Threshold 1.022 MeV must be subtracted first.

<details><summary>Solution</summary>

**Method.** $K=2-1.022=0.98$ MeV, shared between electron and positron.

</details>

## Part 6 · Problem archetypes and practice

### 6.1 Archetypes

| # | Archetype | Template | Where worked | Variations |
|---:|---|---|---|---|
| 1 | Cutoff wavelength | Eq. (4.1) | E1, Q1 | in frequency form |
| 2 | Richest photon from V | $eV$ | E2, Q2 | power and count |
| 3 | Tube efficiency and heat | $\eta\approx10^{-9}ZV$ | Q3, OL7 | duty cycle |
| 4 | K-line threshold voltage | $eV\ge E_K$ | E3, Q6 | other elements |
| 5 | Moseley identification | $(Z-1)^2=\frac{f}{\frac34cR}$ | E4, Q7 | two-line identification |
| 6 | K-alpha energy and wavelength | Eq. (4.2) | Q5 | Z ratios |
| 7 | Exponential attenuation | Eq. (4.3) | E5, Q9-Q11 | HVL counting |
| 8 | Bragg angle | Eq. (4.4) | E6, Q12, Q14 | orders |
| 9 | Order counting | $n\le\frac{2d}{\lambda}$ | E7, Q13 | change lambda |
| 10 | Lattice spacing to Avogadro | Eq. (3.6) | E8, Q15 | other crystals |
| 11 | Compton shift | Eq. (4.5) | E9, Q16-Q17 | angles |
| 12 | Recoil energy and angle | Eqs. (4.5), tan phi | E10, Q18, Q21 | extremes |
| 13 | Visible-light shift estimate | ratio | E11, Q19 | why X-rays |
| 14 | Pair threshold | $2m_ec^2$ | E12, Q22-Q23 | kinetic budget |
| 15 | Duane-Hunt as h measurement | slope of lambda-min vs 1/V | OL5 | Millikan comparison |
| 16 | Rayleigh contrast at low energy | $\lambda^{-4}$ | Q24, OL9 | sky and sunset |

### 6.2 In-flow practice

#### Q1. Minimum wavelength at 30 kV?

<details><summary>Solution</summary>

$41.3$ pm.

</details>

#### Q2. Maximum photon frequency at 50 kV?

<details><summary>Solution</summary>

$f=\frac{eV}{h}=\frac{5\times10^4}{4.136\times10^{-15}}=1.2\times10^{19}$ Hz.

</details>

#### Q3. Tungsten target at 100 kV: efficiency order?

<details><summary>Solution</summary>

$10^{-9}\times74\times10^5=7.4\times10^{-3}$, about one percent.

</details>

#### Q4. A tube emits 7 W of X-rays at mean 30 keV. Photons per second?

<details><summary>Solution</summary>

$\frac{7}{4.8\times10^{-15}}=1.5\times10^{15}$.

</details>

#### Q5. Copper K-alpha energy from Moseley's law?

<details><summary>Solution</summary>

$\frac34\times13.6\times28^2=8.0$ keV, $\lambda=155$ pm.

</details>

#### Q6. Minimum voltage for copper's K lines?

<details><summary>Solution</summary>

$\sim9$ kV (K-edge 8.98 keV).

</details>

#### Q7. K-alpha at 72 pm identifies which element?

<details><summary>Solution</summary>

$Z=42$, molybdenum (E4).

</details>

#### Q8. Ratio of K-alpha frequencies, copper to potassium (Z = 19)?

<details><summary>Solution</summary>

$\left(\frac{28}{18}\right)^2=2.4$.

</details>

#### Q9. Transmission through two half-value layers?

<details><summary>Solution</summary>

$25\%$.

</details>

#### Q10. Mu in per-metres for lead with HVL 0.12 mm?

<details><summary>Solution</summary>

$\mu=\frac{0.693}{1.2\times10^{-4}}=5.8\times10^3$ m$^{-1}$.

</details>

#### Q11. Thickness of lead for 1 % transmission at 100 keV?

<details><summary>Solution</summary>

$x=\frac{\ln100}{57.8\ \text{cm}^{-1}}=0.08$ cm $=0.8$ mm.

</details>

#### Q12. Second-order Bragg angle for NaCl with Cu K-alpha?

<details><summary>Solution</summary>

$\sin\theta=\frac{2\times154}{564}=0.546$; $\theta=33.1^\circ$.

</details>

#### Q13. Highest order in that geometry?

<details><summary>Solution</summary>

$3$.

</details>

#### Q14. A first-order peak at 15.8 degrees with 154 pm implies d?

<details><summary>Solution</summary>

$d=\frac{154}{2\sin15.8^\circ}=282$ pm.

</details>

#### Q15. With that d and rho = 2165, N-A?

<details><summary>Solution</summary>

$6.0\times10^{23}$ (E8).

</details>

#### Q16. Compton shift at 60 degrees?

<details><summary>Solution</summary>

$2.426\times0.5=1.21$ pm.

</details>

#### Q17. Maximum possible Compton shift?

<details><summary>Solution</summary>

$4.86$ pm at 180 degrees.

</details>

#### Q18. Maximum electron kinetic energy from a 100 keV photon?

<details><summary>Solution</summary>

$K=100\times\frac{2x}{1+2x}$, $x=0.196$: $28.1$ keV.

</details>

#### Q19. 90-degree shift as a fraction of 550 nm?

<details><summary>Solution</summary>

$4.4\times10^{-6}$.

</details>

#### Q20. A 100 pm photon scatters at 90 degrees. New wavelength and energy?

<details><summary>Solution</summary>

$102.4$ pm; $E'=\frac{1240}{0.1024}=12.1$ keV.

</details>

#### Q21. The electron's angle when the photon back-scatters?

<details><summary>Solution</summary>

$\phi=0$: the electron goes straight ahead.

</details>

#### Q22. Pair-production threshold?

<details><summary>Solution</summary>

$1.022$ MeV.

</details>

#### Q23. A 5 MeV photon converts. Pair kinetic energy?

<details><summary>Solution</summary>

$3.98$ MeV.

</details>

#### Q24. Rayleigh scattering ratio of 400 to 700 nm?

<details><summary>Solution</summary>

$\left(\frac{700}{400}\right)^4=9.4$: blue scatters nine times stronger.

</details>

#### Q25. Compare a 10 keV electron's wavelength with the 10 kV tube's cutoff.

<details><summary>Solution</summary>

Electron: $12.3$ pm; photon cutoff: $124$ pm. Same voltage, the electron's wave is ten times finer — the microscope argument of PART 23.

</details>

#### Q26. Which is shorter: lambda-min at 20 kV or Cu K-alpha?

<details><summary>Solution</summary>

$\lambda_{\min}=62$ pm, shorter than 154 pm: at 20 kV the smear extends beyond the lines.

</details>

#### Q27. Order of magnitude: dental X-ray dose versus a transatlantic flight?

<details><summary>Solution</summary>

A dental film is a few microsievert; a long flight a few tens of microsievert of cosmic rays. The flight is the larger dose — context, not complacency.

</details>

#### Q28. Resolving power needed to separate the 90-degree Compton line from a 100 pm incident line?

<details><summary>Solution</summary>

$\frac{\lambda}{\Delta\lambda}=\frac{100}{2.43}\approx41$: a modest crystal spectrometer suffices, which is why Compton could do it in 1923.

</details>

## Part 7 · Alternate methods and the JEE-Advanced advantage toolkit

### 7.1 The pm-keV bookkeeping

Work X-rays in pm and keV with $E[\text{keV}]=\frac{1.24}{\lambda[\text{nm}]}=\frac{1240}{\lambda[\text{pm}]}$. Demonstration: 154 pm is $\frac{1240}{154}=8.05$ keV in one division. Fails when joule-level powers enter (tube heat): convert once at the end.

### 7.2 Half-value counting instead of exponentials

When thicknesses come in half-layers, skip the exponential: $n$ half-layers transmit $2^{-n}$. Demonstration: 0.5 mm of lead at 100 keV is 4.17 half-layers, $2^{-4.17}\approx5.5\%$, no logarithms touched. Fails when the answer must be a thickness for a given transmission and $n$ is not round — then take the log.

### 7.3 Scaling as solver

$\lambda_{\min}\propto\frac1V$; $f_{K\alpha}\propto(Z-1)^2$; Compton shift independent of $\lambda$ and material. Demonstration: doubling the voltage halves the cutoff; going from copper ($Z=29$) to silver ($Z=47$) multiplies K$\alpha$ frequency by $\left(\frac{46}{28}\right)^2=2.7$. Fails for L lines, where the screening constant differs.

### 7.4 The extremes auditor

Before submitting any Compton answer: $\theta=0$ must give zero shift and zero recoil; $\theta=180$ the maxima; $m\to\infty$ the unshifted line; $hf\ll m_ec^2$ the Thomson limit. Before any Bragg answer: $\sin\theta\le1$ bounds the orders; $\theta$ from the plane.

### 7.5 The two-peak diagnostic

A shifted-plus-unshifted pair means Compton on something partly bound; a single shifted line at the free-electron value means free electrons; a single unshifted line means classical (visible) scattering or whole-atom recoil. Reading which peaks exist is reading which masses recoiled.

### 7.6 Dimensional synthesis for Avogadro

$N_A$ must come from $\frac{M}{\rho d^3}$ times an order-unity lattice factor (2 for the rock-salt ion-pair cell). A result off by the factor 2 means the cell was miscounted — the dimensional skeleton catches it before the arithmetic does.

## Part 8 · Examiner traps

> [!danger] Trap 1 — the cutoff applied to lines
> Using lambda-min for a characteristic line. Reply: the cutoff bounds only the continuous spectrum; lines sit where the atom says.

> [!danger] Trap 2 — the missing e
> Equating keV numbers with kV without the charge. Reply: numerically they match for electrons precisely because the charge is e; for alphas they do not.

> [!danger] Trap 3 — Bragg's angle from the normal
> Writing 2 d cos theta. Reply: theta is the glancing angle, from the plane; the path difference is 2 d sin theta.

> [!danger] Trap 4 — the wrong order
> Calling the second peak n = 1. Reply: orders count wavelengths of path difference; check n against 2 d over lambda.

> [!danger] Trap 5 — fractional Compton shift
> Applying delta-lambda as a percentage of lambda. Reply: the shift is absolute, 2.43 pm per right angle; the fraction is what varies with lambda.

> [!danger] Trap 6 — the unshifted line misread
> Attributing the unshifted peak to experimental error or classical success. Reply: it is whole-atom recoil off tightly bound electrons.

> [!danger] Trap 7 — classical Compton
> Explaining the shift with wave physics. Reply: a classical wave scatters at its own frequency at every angle; a definite shifted line at a definite angle is particle kinematics.

> [!danger] Trap 8 — energy-momentum units
> Mixing eV and J, or using p = E/c for the recoil electron. Reply: photons take E/c; electrons take sqrt of 2 m K or the relativistic form.

> [!danger] Trap 9 — pair production without a nucleus
> Allowing conversion in empty space. Reply: momentum conservation needs a third body; the nucleus takes the recoil.

> [!danger] Trap 10 — attenuation without geometry
> Using the narrow-beam mu for a broad beam. Reply: scatter returns photons to a broad detector; build-up factors then matter (named, beyond syllabus).

## Part 9 · Playbook

### 9.1 Triage decision tree

- Voltage and cutoff words: Eq. (4.1).
- Element, line, fingerprint: Moseley, Eq. (4.2).
- Thickness, shielding, contrast: Eq. (4.3) with HVL counting.
- Angle and crystal: Bragg, Eq. (4.4), angle from the plane.
- Scattered photon, shift, recoil: Compton, Eq. (4.5).
- Above 1 MeV: pair threshold.

### 9.2 Formula map with validity

| Formula | Valid when | Breaks when |
|---|---|---|
| Eq. (4.1) | one electron, one photon extreme | never for the edge |
| Eq. (4.2) | K lines, screened hydrogenic | L lines need other b |
| Eq. (4.3) | narrow beam | broad beams, build-up |
| Eq. (4.4) | coherent elastic scattering | amorphous materials |
| Eq. (4.5) | free electron at rest | bound electrons (unshifted line) |
| $2m_ec^2$ threshold | near a nucleus | never in vacuum |

### 9.3 Constants to carry

$hc=1240$ eV nm; $\lambda_C=2.43$ pm; $m_ec^2=511$ keV; NaCl $d=0.282$ nm; Pb HVL(100 keV) $0.12$ mm; $\frac34cR=2.47\times10^{15}$ Hz; pair threshold $1.022$ MeV; tube efficiency $10^{-9}ZV$.

### 9.4 Timing plan

A and B: 90 s-2 min. C: 3 min. D: 12 min. A Compton question not reduced to the triangle within two minutes is mis-triaged; a Bragg question without a drawn plane-angle sketch invites trap 3.

### 9.5 Pre-submission audit, ten points

1. pm versus nm versus m consistent.
2. Cutoff used only for the continuous spectrum.
3. Characteristic threshold checked in voltage.
4. Bragg angle from the plane; orders bounded.
5. Compton shift absolute, not fractional.
6. Unshifted line explained if present.
7. Recoil electron momentum relativistic where needed.
8. Pair production has its nucleus.
9. One limit pushed.
10. All sub-parts answered.

## Part 10 · Olympiad extension

### OL1 — Compton, the scalar route

Derive Eq. (3.7) by algebra alone: write energy and the two momentum components, eliminate the electron's angle $\phi$, and close with $E_e^2=(p_ec)^2+(m_ec^2)^2$.

<details><summary>Solution</summary>

**Method.** From the momentum components: $p_e\cos\phi=\frac{h}{\lambda}-\frac{h}{\lambda'}\cos\theta$, $p_e\sin\phi=\frac{h}{\lambda'}\sin\theta$. Square and add: $p_e^2=\left(\frac{h}{\lambda}\right)^2+\left(\frac{h}{\lambda'}\right)^2-2\frac{h^2}{\lambda\lambda'}\cos\theta$. Energy: $E_e=\frac{hc}{\lambda}-\frac{hc}{\lambda'}+m_ec^2$. Insert into $E_e^2=(p_ec)^2+(m_ec^2)^2$; the squared terms cancel, leaving $2m_ec^2\left(\frac{hc}{\lambda}-\frac{hc}{\lambda'}\right)=-2\frac{h^2c^2}{\lambda\lambda'}\cos\theta+2\frac{h^2c^2}{\lambda\lambda'}$, i.e. $\frac{1}{\lambda'}-\frac{1}{\lambda}$ times $m_ec^2$ equals $\frac{h c}{\lambda\lambda'}(1-\cos\theta)$; multiply by $\frac{\lambda\lambda'}{m_ec^2}$... rearranged: $\lambda'-\lambda=\frac{h}{m_ec}(1-\cos\theta)$.

**Checks.** (i) $\theta=0$: zero shift. (ii) Dimensions: $\frac{h}{mc}$ is length.

</details>

### OL2 — Compton, the invariant route

Re-derive the shift in four lines with the four-momentum invariant: $(P_\gamma+P_e-P_{\gamma'})^2=P_{e'}^2$, using $P_\gamma^2=0$, $P_e^2=(m_ec)^2$.

<details><summary>Solution</summary>

**Method.** Expand: $-2P_\gamma\cdot P_{\gamma'}+2P_e\cdot(P_\gamma-P_{\gamma'})=0$. In the electron's rest frame $P_e=(m_ec,\mathbf0)$, $P_\gamma=(\frac{h}{\lambda},\frac{h}{\lambda}\hat n)m_ec$-units aside: $P_\gamma\cdot P_{\gamma'}=\frac{h^2}{\lambda\lambda'}(1-\cos\theta)$ and $P_e\cdot P_\gamma=\frac{m_ech}{\lambda}$ (times $c$ bookkeeping). Hence $\frac{m_echc}{\lambda}-\frac{m_echc}{\lambda'}=\frac{h^2c^2}{\lambda\lambda'}(\cos\theta-1)$, giving $\Delta\lambda=\frac{h}{m_ec}(1-\cos\theta)$ — and the electron's energy falls out of $E_e=E_\gamma-E_{\gamma'}+m_ec^2$ directly, which is why this route is the elegant one.

**Checks.** (i) Matches OL1 term for term. (ii) Lorentz-invariant derivation: valid in any frame, the scalar route's assumption of a resting electron made explicit.

</details>

### OL3 — Why the photon cannot give everything

Show that at $\theta=180^\circ$ the electron receives $K_{\max}=hf\frac{2x}{1+2x}$ with $x=\frac{hf}{m_ec^2}$, and argue in one sentence why $K<hf$ always.

<details><summary>Solution</summary>

**Method.** From Eq. (3.8) at $\cos\theta=-1$: $K=hf\frac{2x}{1+2x}$. Since the scattered photon's momentum must vanish or reverse, a photon with zero final energy would carry zero momentum while the electron carried some — momentum conservation forbids the photon from disappearing. For a 100 keV photon: $K_{\max}=28.1$ keV; for 1 MeV: $0.85$ MeV, approaching but never reaching $hf$.

**Checks.** (i) $x\to0$: $K\to2x\,hf\to0$ relative fraction vanishes, the classical limit. (ii) $x\to\infty$: $K\to hf$ asymptotically.

</details>

### OL4 — Inverse Compton as a moving mirror

A 1 GeV electron ($\gamma\approx2000$) collides head-on with a microwave photon of $10^{-3}$ eV. Estimate the boosted photon's energy by the mirror analogy, and name the cross-topic cousin.

<details><summary>Solution</summary>

**Method.** In the electron's frame the photon arrives blue-shifted by $\sim\gamma$; it "reflects" and is boosted by $\sim\gamma$ again on the way back: $E'\sim\gamma^2E=4\times10^6\times10^{-3}=4$ keV — soft microwave in, X-ray out. The velocity-triangle logic is identical to a gravity assist (PART 7's slingshot) and to PART 28's moving-mirror Doppler: fast object, slow projectile, energy transfer by reflection.

**Checks.** (i) Exact head-on kinematics gives $E'\approx\frac{4\gamma^2E}{1+4\gamma E/m_ec^2}$, here $\approx4$ keV. (ii) This is how the universe makes some of its X-ray sky.

</details>

### OL5 — Duane-Hunt as the sharpest early h/e

A lab records cutoffs: 30 kV at 41.3 pm, 40 kV at 31.0 pm, 50 kV at 24.8 pm. Extract h from the slope of lambda-min against 1/V, with e known.

<details><summary>Solution</summary>

**Method.** Slope $=\lambda_{\min}V$: $41.3\times10^{-12}\times3\times10^4=1.24\times10^{-6}$ V m; $31.0\times10^{-12}\times4\times10^4=1.24\times10^{-6}$; consistent. $h=\frac{e\times\text{slope}}{c}=\frac{1.602\times10^{-19}\times1.24\times10^{-6}}{3\times10^8}=6.62\times10^{-34}$ J s. The three points collinear through the origin is the quantum statement; Millikan's photoelectric slope measures the same ratio from the other side of the mirror.

**Checks.** (i) All three products equal within rounding. (ii) The value matches blackbody h.

</details>

### OL6 — The shielding constant from the shell picture

Argue from the shell model why K-alpha uses b of 1, and why K-beta's effective b is slightly larger; quote the measured K-alpha offset for copper.

<details><summary>Solution</summary>

**Method.** The L electron falling into the K vacancy spends the transition outside the remaining 1s electron, which screens one full unit: $b=1$. For K$\beta$ the falling M electron is screened by the 1s electron plus, partly, the two L electrons between it and the nucleus on average, so the effective $b$ exceeds 1 (fits give $\sim1.5$-$2$ for heavier atoms' K$\beta$ and larger for L lines). Copper's measured K$\alpha$ (154 pm) against the $b=1$ prediction (155 pm): agreement within the model's one percent, which is why Moseley's line is straight to the eye.

**Checks.** (i) L lines need still larger b, as tables show. (ii) Hydrogen has no screening: b = 0, recovering Lyman alpha.

</details>

### OL7 — The anode as an engineering problem

A dental tube runs 70 kV at 10 mA in 0.5 s exposures. Estimate the energy dumped per exposure, the adiabatic temperature rise of a 100 g tungsten anode (specific heat 0.13 J per g per K), and say what the rotating anode buys.

<details><summary>Solution</summary>

**Method.** $E=VIt=70\times10^3\times10^{-2}\times0.5=350$ J per exposure. $\Delta T=\frac{350}{100\times0.13}=27$ K per shot if the heat stayed in 100 g; in reality the focal spot is a few mm$^2$, so the local rise is hundreds of K — the rotating anode spreads each shot over a ring, multiplying the effective mass by the ring-to-spot ratio, $\sim50$: the difference between a working tube and a melted one.

**Checks.** (i) Tungsten melts at 3700 K; the spot margin is real but thin. (ii) Efficiency 0.7 % means 348 of the 350 J are heat.

</details>

### OL8 — Dose in perspective

Define absorbed dose (gray: J per kg) and equivalent dose (sievert: weighted), then place a dental X-ray, a chest X-ray and a transatlantic flight on one line.

<details><summary>Solution</summary>

**Method.** A dental film is about 5 µSv, a chest film about 100 µSv, a long flight about 40-80 µSv of cosmic rays. The flight exceeds the dental shot; background life delivers about 10 µSv per day. The numbers teach scale, not licence: the linear-no-threshold model is a convention for regulation, stated here as convention.

**Checks.** (i) Orders match published radiation-protection tables. (ii) A CT scan (mSv) sits two decades above the dental film.

</details>

### OL9 — The sky as the low-energy contrast

Compute Rayleigh's $\lambda^{-4}$ ratio for 400 versus 700 nm, and contrast the physics with this chapter's scattering.

<details><summary>Solution</summary>

**Method.** $\left(\frac{700}{400}\right)^4=9.4$: blue scatters about nine times harder — the blue sky, and the red sunset (long path, blue removed). Rayleigh scattering is the low-energy limit where the photon's wavelength dwarfs the scatterer and the cross-section scales as $\lambda^{-4}$; Compton-Thomson scattering is the high-energy limit where the wavelength is comparable to or smaller than the electron's quantum scale and the cross-section is essentially flat (then falling, Klein-Nishina). One chapter of photon physics, two opposite limits.

**Checks.** (i) The ratio is dimensionless and steep. (ii) Sunset redness and Compton flatness share the same parent theory.

</details>

### OL10 — Why X-ray lasers are hard

State in one paragraph the three obstacles to lasing at angstrom wavelengths, and name the machine that finally did it.

<details><summary>Solution</summary>

**Method.** (i) Inversion at keV gaps is thermally absurd (Boltzmann $e^{-40}$ at any temperature, PART 23 OL6) and needs violent pumping — nuclear tests and huge lasers. (ii) No mirrors: at X-ray frequencies every material's refractive index is just below 1, so only grazing-incidence or Bragg reflection works. (iii) The upper states live femtoseconds. Free-electron lasers sidestep all three by lasing in the electron beam itself: kilometre linacs producing angstrom pulses, the XFELs of the 2010s.

**Checks.** (i) Each obstacle traces to a result derived earlier in this vault. (ii) The workarounds are engineering, not new physics.

</details>

### OL11 — Which potential for the wavelength?

Electron diffraction through a thin film at 100 kV: should lambda use the accelerating voltage or the total energy, and how large is the difference?

<details><summary>Solution</summary>

**Method.** The wavelength wants the momentum, and at 100 kV the electron is mildly relativistic: the non-relativistic formula gives 3.88 pm, the correct momentum gives 3.70 pm, a 4.6 % difference that shifts every inferred lattice constant by the same fraction. Rule: use $p=\sqrt{2m_eK(1+\frac{K}{2m_ec^2})}$ — the first relativistic correction — whenever $K$ exceeds a few keV (PART 23 OL8).

**Checks.** (i) At 10 kV the correction is 1 %, matching the 1 % tolerance line. (ii) The sign: relativity shortens the wavelength.

</details>

### OL12 — Avogadro with an error budget

Re-run E8, but propagate a 0.1 % error in d. Why did this determination historically fix N-A to crystal-quality precision?

<details><summary>Solution</summary>

**Method.** $N_A\propto d^{-3}$: a 0.1 % error in d triples to 0.3 % in N-A. Bragg angles can be read to better than 0.1 % (angles, not lengths, are measured), and density to 0.05 %: the chain delivers N-A at the 0.3 % level — which, reversed, is how the modern metre-scale lattice standards propagate. The result $6.02\times10^{23}$ agrees with the modern value because both ends of the chain are now defined quantities.

**Checks.** (i) Cubic propagation correct. (ii) X-ray density and chemical density agree at this level for good crystals.

</details>

### 10.2 Limits and failure of the model

The chapter's models hand over at: high precision in Compton scattering (Klein-Nishina, the full quantum-electrodynamic cross-section, named not derived); absent reflections and intensities (structure factors, full crystallography); broad-beam dosimetry (build-up factors); pair production's full kinematics (PART 28); and the characteristic lines of multi-electron atoms beyond Moseley's one-parameter screening (quantum mechanics). Within its domain — keV photons, narrow beams, free electrons, coherent planes — the arithmetic is exact.

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

The cutoff wavelength of a 40 kV tube is nearest:
(a) 31 pm (b) 62 pm (c) 12 pm (d) 41 pm

<details><summary>Solution</summary>

$\frac{1.24\times10^6}{4\times10^4}=31$ pm. (a).

</details>

### P2 · 4 marks

The sharp short-wavelength cutoff of the continuous spectrum is direct evidence that:
(a) electrons are waves (b) one electron can give its whole energy to one photon (c) the target is crystalline (d) X-rays are longitudinal

<details><summary>Solution</summary>

(b), the Duane-Hunt limit.

</details>

### P3 · 4 marks

A copper target runs at 5 kV. The spectrum shows:
(a) continuous plus K lines (b) continuous only (c) K lines only (d) nothing

<details><summary>Solution</summary>

(b): below the 9 kV K threshold the lines are absent.

</details>

### P4 · 4 marks

The ratio of K-alpha frequencies of copper (29) to potassium (19) is:
(a) 1.6 (b) 2.4 (c) 2.7 (d) 0.42

<details><summary>Solution</summary>

$(28/18)^2=2.4$. (b).

</details>

### P5 · 4 marks

Three half-value layers transmit:
(a) 33 % (b) 12.5 % (c) 25 % (d) 3 %

<details><summary>Solution</summary>

$2^{-3}=12.5\%$. (b).

</details>

### P6 · 4 marks

First-order Bragg reflection of 154 pm X-rays from planes 282 pm apart occurs at glancing angle nearest:
(a) 16 degrees (b) 33 degrees (c) 45 degrees (d) 74 degrees

<details><summary>Solution</summary>

$\sin\theta=0.273$, 15.8 degrees. (a).

</details>

### P7 · 4 marks

The highest Bragg order in that geometry is:
(a) 2 (b) 3 (c) 4 (d) 3.66

<details><summary>Solution</summary>

(b): 3.66 truncates to 3.

</details>

### P8 · 4 marks

The Compton shift at 90 degrees is:
(a) 1.21 pm (b) 2.43 pm (c) 4.86 pm (d) 24.3 pm

<details><summary>Solution</summary>

(b).

</details>

### P9 · 4 marks

The Compton shift depends on:
(a) the target material (b) the intensity (c) the scattering angle only (d) the wavelength

<details><summary>Solution</summary>

(c).

</details>

### P10 · 4 marks

The unshifted line in a Compton spectrum comes from:
(a) experimental error (b) electrons bound so tightly the whole atom recoils (c) free electrons (d) pair production

<details><summary>Solution</summary>

(b).

</details>

### P11 · 4 marks

Pair production becomes possible at photon energies above:
(a) 511 keV (b) 1.022 MeV (c) 13.6 eV (d) 9 MeV

<details><summary>Solution</summary>

(b).

</details>

### P12 · 4 marks

The X-ray production efficiency of tungsten at 100 kV is of order:
(a) 50 % (b) 10 % (c) 1 % (d) 0.001 %

<details><summary>Solution</summary>

(c).

</details>

#### Section B · One or more correct

### P13 · 4 marks

Raising the voltage of an X-ray tube:
(a) shortens lambda-min (b) raises the continuous intensity (c) shifts the characteristic lines to shorter wavelengths (d) can switch characteristic lines on

<details><summary>Solution</summary>

(a), (b), (d). Line wavelengths are atomic, (c) false.

</details>

### P14 · 4 marks

Moseley's law:
(a) makes sqrt f linear in Z (b) uses b of 1 for K-alpha (c) ordered the periodic table (d) revealed missing elements as gaps

<details><summary>Solution</summary>

All four.

</details>

### P15 · 4 marks

Bragg diffraction:
(a) measures theta from the plane (b) bounds orders by 2d over lambda (c) gives rings from powders (d) works for visible light on crystals

<details><summary>Solution</summary>

(a), (b), (c). (d) false: the wavelength ratio is 1e3 too large.

</details>

### P16 · 4 marks

Compton scattering:
(a) the shift is absolute, not fractional (b) two peaks can appear (c) the electron never recoils backwards (d) the electron can take all the photon energy

<details><summary>Solution</summary>

(a), (b), (c). (d) violates momentum (OL3).

</details>

### P17 · 4 marks

X-ray attenuation:
(a) mu generally falls with energy away from edges (b) high-Z materials absorb much more (c) x-half equals ln 2 over mu (d) broad and narrow beams attenuate identically

<details><summary>Solution</summary>

(a), (b), (c). (d) false: scatter build-up.

</details>

### P18 · 4 marks

Pair production:
(a) needs 1.022 MeV (b) needs a nucleus or electron nearby (c) shares surplus energy as kinetic energy (d) occurs in perfect vacuum

<details><summary>Solution</summary>

(a), (b), (c).

</details>

### P19 · 4 marks

The Coolidge tube:
(a) converts about one percent of power to X-rays at 100 kV on tungsten (b) must rotate or cool the anode (c) emits characteristic lines from any voltage (d) uses thermionic emission

<details><summary>Solution</summary>

(a), (b), (d). (c) false.

</details>

### P20 · 4 marks

The photon evidence table:
(a) photoelectric proves energy quanta (b) Compton proves photon momentum (c) crystal diffraction proves the wave character (d) Compton proves light is only a particle

<details><summary>Solution</summary>

(a), (b), (c). (d) false: complementarity stands.

</details>

#### Section C · Numerical

### P21 · 5 marks

Cutoff wavelength at 60 kV, in pm.

<details><summary>Solution</summary>

$\frac{1.24\times10^6}{6\times10^4}=20.7$ pm.

</details>

### P22 · 5 marks

A target's K-alpha is at 72 pm. Its atomic number?

<details><summary>Solution</summary>

$Z=42$ (molybdenum).

</details>

### P23 · 5 marks

Fraction transmitted through 0.24 mm of lead at 100 keV, in percent.

<details><summary>Solution</summary>

Two half-layers: 25 %.

</details>

### P24 · 5 marks

Sin of the third-order Bragg angle for 154 pm on 282 pm planes, to two decimals.

<details><summary>Solution</summary>

$\frac{3\times154}{564}=0.82$.

</details>

### P25 · 5 marks

Maximum electron kinetic energy from a 50 keV photon, in keV to one decimal.

<details><summary>Solution</summary>

$x=0.0978$; $K=50\times\frac{0.1957}{1.1957}=8.2$ keV.

</details>

### P26 · 5 marks

A 50 keV photon back-scatters. The scattered wavelength, in pm.

<details><summary>Solution</summary>

$\lambda=24.8$ pm; $\lambda'=24.8+4.86=29.7$ pm.

</details>

#### Section D · Comprehensive long-form

### P27 · 9 marks

(a) Derive lambda-min = hc over eV from energy conservation. (b) Evaluate at 30, 50, 100 kV. (c) Explain how the plot of lambda-min against 1 over V measures h, and why it is the inverse photoelectric effect. (3+3+3)

<details><summary>Solution</summary>

(a) Richest photon: $hf_{\max}=eV$.
(b) 41.3, 24.8, 12.4 pm.
(c) Slope is $\frac{hc}{e}$; with e known, h; PART 23's $V_s$-$f$ slope measures $\frac{h}{e}$ from absorption, this from emission.

</details>

### P28 · 9 marks

(a) Derive Moseley's law from the screened Bohr picture. (b) A line at 72 pm: identify the element. (c) The minimum voltage to excite its K lines (K edge about 20 keV). (3+3+3)

<details><summary>Solution</summary>

(a) $E_{K\alpha}=\frac34\times13.6(Z-1)^2$ eV; square root linear.
(b) $Z=42$.
(c) $\sim20$ kV.

</details>

### P29 · 9 marks

(a) Derive I = I0 e to the minus mu x from the constant-fraction-per-layer argument. (b) Lead: HVL 0.12 mm; transmission through 0.5 mm. (c) Why bone images white, and the soft-X-ray trade-off in one line each. (3+3+3)

<details><summary>Solution</summary>

(a) $\frac{dI}{dx}=-\mu I$.
(b) 5.5 %.
(c) Calcium's Z absorbs more; soft X-rays give contrast but deposit more dose.

</details>

### P30 · 9 marks

(a) Derive Bragg's law with the glancing-angle convention. (b) First order at 15.8 degrees with 154 pm: find d. (c) With rho = 2165 and M = 58.44, find Avogadro's number. (3+3+3)

<details><summary>Solution</summary>

(a) Path $2d\sin\theta=n\lambda$.
(b) $d=\frac{154}{2\sin15.8^\circ}=282$ pm.
(c) $6.02\times10^{23}$.

</details>

### P31 · 9 marks

(a) By scalar conservation laws, derive the Compton shift. (b) For a 100 keV photon at 90 degrees: shift, electron kinetic energy, electron angle. (c) State the two limits theta to 0 and theta to 180. (3+3+3)

<details><summary>Solution</summary>

(a) OL1's algebra.
(b) 2.43 pm; 16.4 keV; 39.9 degrees.
(c) 0 and 4.86 pm.

</details>

### P32 · 9 marks

(a) Re-derive the shift with the four-momentum invariant. (b) Which route gives the electron energy more directly, and why? (c) Why can the photon never vanish into the electron alone? (3+3+3)

<details><summary>Solution</summary>

(a) OL2.
(b) The invariant route: $E_e$ falls out of energy conservation with both photon energies already known.
(c) Momentum: a gone photon leaves the electron with momentum but no partner.

</details>

### P33 · 9 marks

(a) Maximum Compton shift as a fraction of 550 nm. (b) The same for a 100 pm photon at 90 degrees. (c) Conclude why Compton needed X-rays, and the resolving power his spectrometer required. (3+3+3)

<details><summary>Solution</summary>

(a) $8.8\times10^{-6}$ (at 180), $4.4\times10^{-6}$ at 90.
(b) 2.4 %.
(c) Percent-level shifts are resolvable, parts-per-million were not in 1923; R about 41 suffices.

</details>

### P34 · 9 marks

(a) Why does pair production need 1.022 MeV? (b) Why a nucleus? (c) A 5 MeV photon converts: total pair kinetic energy, and name the chapter that owns the full relativistic bookkeeping. (3+3+3)

<details><summary>Solution</summary>

(a) Two rest masses.
(b) Momentum conservation needs a recoil partner.
(c) 3.98 MeV; PART 28.

</details>

### P35 · 9 marks

A 70 kV, 10 mA dental tube fires 0.5 s. (a) Electron power and energy per shot. (b) X-ray power at 0.7 % efficiency and photons per second at mean 30 keV. (c) The adiabatic rise of a 100 g tungsten anode and what rotation buys. (3+3+3)

<details><summary>Solution</summary>

(a) 700 W; 350 J.
(b) 4.9 W; $1.0\times10^{15}$ s$^{-1}$.
(c) 27 K per shot spread over the whole anode; rotation spreads the spot heat over a ring, the survival factor.

</details>

### P36 · 9 marks

(a) Fill the three-experiment table: photoelectric, Compton, diffraction — what each proves. (b) A 1 GeV electron head-on with a 1 meV photon: estimate the outgoing photon energy and name the process. (c) State one sentence on why the sky is blue as this chapter's low-energy contrast. (3+3+3)

<details><summary>Solution</summary>

(a) Energy quantum; momentum quantum; wave character.
(b) $\sim\gamma^2E=4$ keV, inverse Compton.
(c) Rayleigh's lambda to the minus four scatters blue nine times harder than red.

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
| P1 | 3, 4 | P19 | 3 |
| P2 | 3 | P20 | 3, 4 |
| P3 | 3 | P21 | 4 |
| P4 | 3, 4 | P22 | 3, 4 |
| P5 | 4 | P23 | 4 |
| P6 | 3, 4 | P24 | 4 |
| P7 | 4 | P25 | 4, 10 |
| P8 | 4 | P26 | 4 |
| P9 | 3, 4 | P27 | 3, 10 |
| P10 | 3 | P28 | 3, 4 |
| P11 | 3, 4 | P29 | 3 |
| P12 | 3 | P30 | 3, 10 |
| P13 | 3 | P31 | 3, 10 |
| P14 | 3 | P32 | 10 |
| P15 | 3 | P33 | 3, 10 |
| P16 | 3, 10 | P34 | 3 |
| P17 | 3, 4 | P35 | 3, 10 |
| P18 | 3 | P36 | 10, 3 |

Blocks 2 (definitions and conventions used throughout), 3, 4 and 10 are each tested.

| If you lost marks on | Reread | Because |
|---|---|---|
| cutoff questions | §3.2 | the edge is the continuous spectrum's only |
| line questions | §3.3-3.4 | threshold voltage and Moseley screening |
| Bragg questions | §3.7 | the angle convention |
| Compton questions | §3.10, OL1-OL3 | absolute shift, recoil bookkeeping |
| attenuation questions | §3.5 | HVL counting and Z dependence |

## Part 13 · Formula sheet

> [!abstract] Numbers to keep
> $hc=1240$ eV nm $=1.24$ keV pm; $\lambda_C=2.426$ pm; $m_ec^2=511$ keV; $\frac34cR=2.47\times10^{15}$ Hz; NaCl $d=0.282$ nm, $\rho=2165$ kg/m$^3$; Pb HVL(100 keV) $0.12$ mm; pair threshold $1.022$ MeV; efficiency $\sim10^{-9}ZV$; Cu K$\alpha$ $154$ pm at $\sim9$ kV threshold; Mo K$\alpha$ $72$ pm.

| Formula | Validity |
|---|---|
| $\lambda_{\min}=\frac{1.24\times10^6}{V}$ pm | continuous edge only |
| $E_{K\alpha}=\frac34\times13.6(Z-1)^2$ eV | K lines; other b for L, K-beta |
| $I=I_0e^{-\mu x}$; $x_{1/2}=\frac{\ln2}{\mu}$ | narrow beam |
| $2d\sin\theta=n\lambda$; $n\le\frac{2d}{\lambda}$ | theta from the plane |
| $N_A=\frac{M}{2\rho d^3}$ | rock-salt type cells |
| $\Delta\lambda=2.426(1-\cos\theta)$ pm | free electron |
| $K_e=hf\frac{x(1-\cos\theta)}{1+x(1-\cos\theta)}$, $x=\frac{hf}{m_ec^2}$ | same |
| $\tan\phi=\frac{1}{(1+x)\tan(\theta/2)}$ | same |
| $\eta\approx10^{-9}ZV$ | bremsstrahlung fraction |
| pair threshold $2m_ec^2$ | with a recoil partner |
| Rayleigh $\propto\lambda^{-4}$ | low-energy limit |
| $\lambda_e=\frac{1.226}{\sqrt V}$ nm, corrected $p=\sqrt{2mK(1+\frac{K}{2m_ec^2})}$ | electron diffraction (PART 23) |

## Part 14 · Checkpoint and hand-off

### 14.1 Can I do this?

One point per honest yes; 24 plus is exam-ready.

1. Sketch the double spectrum and explain every feature.
2. Derive the Duane-Hunt limit and quote three cutoffs.
3. Say why the edge is sharp and the long end soft.
4. State the characteristic-line threshold logic and use it.
5. Derive Moseley's law and identify an element.
6. Explain the shielding constant's value for K-alpha.
7. Work the exponential law by HVL counting.
8. Explain bone-white and the soft-X-ray trade-off.
9. Derive Bragg's law with the plane convention.
10. Bound the orders and count them.
11. Extract d from an angle, and N-A from d, rho, M.
12. Describe powder rings.
13. State what the two Compton peaks are.
14. Derive the shift by the scalar route.
15. Derive it by the invariant route.
16. Compute recoil energy and angle at any theta.
17. Explain why the photon cannot give everything.
18. Estimate the visible-light shift and its consequence.
19. Quote the pair threshold and its nucleus requirement.
20. Estimate tube efficiency and anode heating.
21. Place photoelectric, Compton, diffraction in the evidence table.
22. Run the inverse-Compton mirror estimate.
23. Defuse each trap of Part 8.
24. Run the ten-point audit of 9.5.

### 14.2 What the next chapter assumes

PART 26 inherits the pair-production threshold, the eV-keV bookkeeping and the nuclear recoil habit; the binding-energy curve lives where this chapter's K edges hinted at nuclear scales. PART 28 owns the full relativistic kinematics that this chapter used at threshold level (inverse Compton, pair production). The crystallography here closes the diffraction trilogy begun in PART 23 and [[Wave-optics]].

> [!abstract] DIAGRAM D25.15 · The X-ray tube spectrum with every label
> *Show:* one spectrum combining the hump, the cutoff labelled lambda-min equals hc over eV, K-alpha and K-beta spikes, the threshold voltage annotation, and a second lower-voltage curve without spikes; all six labels of the chapter's core in one figure.
> *Search:* "X-ray tube spectrum labelled cutoff K alpha K beta threshold voltage"
> *Used in:* Part 13 review.

> [!abstract] DIAGRAM D25.16 · The photon's three proofs and the two limits
> *Show:* a vertical energy axis; at eV scale the photoelectric block, at keV the Bragg and Compton blocks, at MeV the pair block; arrows to "energy quantum", "wave", "momentum quantum"; at the bottom the Rayleigh low-energy limit and the Klein-Nishina high-energy limit bracketing the Compton block.
> *Search:* "photon interactions energy regimes photoelectric Compton pair production chart"
> *Used in:* 3.12 and Part 13.

### 14.3 Open questions you can now attack

What does the photon do at energies where the electron's rest mass is small change — PART 28. Why do nuclei bind at MeV scales while atoms bind at eV — PART 26. How does a crystal's absent reflection reveal its hidden atoms — the structure-factor door this chapter opened.
