---
title: Nuclear Structure, Radioactivity, Fission & Fusion
part: 26
slug: nuclear-physics
source: Cengage Optics and Modern Physics, ch 5 Nuclear Physics (pp. 5.1-5.39)
aliases: [nuclear physics, radioactivity, binding energy, fission fusion]
tags: [jee-advanced, olympiad, modern-physics, nuclear]
---

# Nuclear Structure, Radioactivity, Fission & Fusion — first principles to Olympiad

> [!abstract] How to use this chapter
> Three passes. Pass 1: Parts 0-4 — the nucleus as a drop of nuclear matter, the binding-energy curve as the decision-maker, the three decays, the statistical decay law, chains, dating, fission and fusion with real numbers. Pass 2: Parts 5-9 for exam craft. Pass 3: Parts 10-14 — the Olympiad layer (Geiger-Nuttall from tunnelling, the fissility parameter, solar neutrinos, the Sun's lifetime), the paper, the sheet, the checkpoint. Every number recomputed; every boxed result carries its validity condition. PENDING's P5 (radioactivity and decay kinetics) is folded into this chapter by design.

## Part 0 · Orientation

### 0.1 What you will be able to do

After this chapter you can: balance any decay or reaction and compute its $Q$-value with atomic masses and the electron-mass bookkeeping done right; read the binding-energy-per-nucleon curve as the arbiter of fission versus fusion; split an alpha decay's energy between alpha and daughter; derive the exponential decay law, half-life and mean life; solve two-step chains and name their equilibria; date with carbon and with parent-daughter ratios; compute the energy of a gram of U-235 and the fuel burn of a gigawatt reactor; estimate the Coulomb barrier, the naive temperature and the honest tunnelling answer; and audit the Sun's power budget, mass loss and neutrino flux.

### 0.2 The one idea

Nuclei are bound by a short-range, saturating force, and the binding-energy curve decides which way the energy flows: heavy nuclei pay out by splitting, light ones by fusing, and iron collects nothing.

### 0.3 Prerequisite self-check

1. What did Rutherford's closest-approach argument bound, and where does it fail? (PART 24)
2. Quote $1$ u in MeV and $hc$ in MeV fm.
3. Write the de Broglie wavelength of a thermal neutron and say what it diffracts from. (PARTS 23, 25)
4. What is the statistical meaning of a decay constant?
5. State $E=mc^2$ in practical units.
6. What stops two protons fusing at room temperature, and what lets them fuse in the Sun?
7. Why does a saturated force imply binding energy proportional to $A$?

<details><summary>Solution</summary>

1. It bounded the nuclear size at tens of fm; it fails above $\sim30$ MeV alphas on gold, where the nuclear force takes over — this chapter's doorstep.
2. $931.5$ MeV; $hc=197.3$ MeV fm (or $1240$ eV nm).
3. $\sim1.8$ Å at $25$ meV; crystals — the neutron analogue of Davisson-Germer.
4. Probability per unit time for one nucleus, constant and memoryless.
5. $1$ u $\to931.5$ MeV; $1$ kg $\to9\times10^{16}$ J.
6. The Coulomb barrier, $\sim0.7$ MeV for two protons at touching distance; the Sun uses the Maxwell tail plus tunnelling.
7. Each nucleon binds only to its nearest neighbours, so total binding grows like the number of nucleons.

</details>

### 0.4 Numbers to keep

> [!abstract] Numbers to keep
> $R_0=1.2$ fm; nuclear density $2.3\times10^{17}$ kg/m$^3$ (a teaspoon, $\sim10^{12}$ kg); $1$ u $=931.5$ MeV; deuteron $2.22$ MeV; He-4 $28.3$ MeV ($7.07$ per nucleon); Fe-56 peak $\approx8.8$ MeV per nucleon; U-235 fission $\sim200$ MeV $=8.2\times10^{10}$ J/g, $\sim1$ kg/day per GW thermal ($\sim3$ kg/day per GW electric); $T_{1/2}$(C-14) $=5730$ y; $T_{1/2}$(Ra-226) $=1600$ y, $1$ g $\approx1$ Ci; mean life $=1.44\,T_{1/2}$; n-decay $Q=0.782$ MeV; pp barrier $0.72$ MeV, naive $T\sim10^{10}$ K, real core $1.5\times10^7$ K; Sun loses $4.3\times10^9$ kg/s; solar neutrino flux at Earth $\sim6\times10^{14}$ m$^{-2}$s$^{-1}$; pair and threshold kinematics owned by PART 25 and PART 28.

### 0.5 Three passes

Pass 1 reads the physics; the binding curve is the spine. Pass 2 works every exemplar and practice question by hand. Pass 3 sits the paper, then audits with Part 12.

### 0.6 Cengage coverage map

Sweep read from the committed PDF's chapter 5 contents page (pp. v-vii). The semi-empirical mass formula, Geiger-Nuttall/Gamow tunnelling, counting statistics, the Lawson criterion and the solar-neutrino estimate are not headings of this volume; they are INPhO/IPhO syllabus items added by the sweep.

| Cengage section (ch 5) | What it establishes | Where it lives here | Status |
|---|---|---|---|
| Nuclear structure (5.2); atomic mass number (5.2); definitions (5.3) | protons, neutrons, isotopes, isobars, isotones | §3.1, §2.1 | derived |
| Size of nuclei (5.3) | $R=R_0A^{1/3}$, constant density | §3.2 | derived |
| Nuclear binding energy (5.4); mass defect (5.5); mass-energy equivalence (5.5) | $\Delta m$, $B=\Delta mc^2$ | §3.3 | derived |
| Binding energy per nucleon (5.6); variation with mass number (5.7) | the curve, its peak, fission/fusion arrows | §3.3-3.4 | derived |
| Q values (5.8) | reaction and decay energetics | §3.5, §4 | derived |
| Nuclear stability (5.8); n/p ratio (5.14) | the valley, beta-decay directions | §3.4, §3.6 | derived |
| Radioactivity (5.9); alpha (5.10); beta (5.12); gamma (5.14) | the three decays | §3.6-3.8 | derived |
| Decay and activity (5.15); measurement (5.15); fundamental laws (5.16); decay law (5.16) | $N=N_0e^{-\lambda t}$, $A=\lambda N$ | §3.9 | derived |
| Activity (5.17); half-life (5.17); half-life form (5.18); average life (5.19) | the time scales | §3.9 | derived |
| Radioactive dating (5.20) | carbon and parent-daughter methods | §3.11 | derived |
| Decay series (5.21); equilibrium (5.21) | chains, secular and transient | §3.10 | derived |
| Simultaneous decay modes (5.22); accumulation (5.22) | branching, daughter growth | §3.10, Q18 | derived |
| Nuclear reactions (5.24); kinematics (5.24); energy conservation (5.25) | balance and Q | §3.5 | derived |
| Nuclear fission (5.26) | process, chain, k | §3.12 | derived |
| Reactors (5.28): leakage, regulating energies, capture (5.28-5.29) | moderator, control, geometry | §3.12 | derived |
| Nuclear fusion (5.29); fusion in the Sun (5.29); fusion reactors (5.30) | barrier, p-p chain, Lawson | §3.13 | derived |
| Solved examples (5.34); exercises (5.39 onward) | standard shapes | §6, Part 11 | exercised |
| Semi-empirical mass formula (added by sweep) | five terms, stability valley | §3.4, OL4 | added by sweep |
| Geiger-Nuttall and Gamow tunnelling (added by sweep) | the $10^{20}$ half-life range | OL1 | added by sweep |
| Counting statistics (added by sweep) | $\sqrt N$ and measurement time | §3.14, OL8 | added by sweep |
| Solar neutrino flux and Sun's lifetime (added by sweep) | Fermi estimates | OL6-OL7 | added by sweep |
| Detectors: cloud chamber, Geiger dead time (added by sweep) | tracks and counting | §3.14 | added by sweep |

## Part 1 · Intuition first

### 1.1 A drop of charged nuclear matter

Every nucleus has roughly the density of every other: double the nucleons, double the volume. That is the signature of a saturated, short-range attraction — each nucleon holding hands only with its neighbours, like molecules in a water drop — fighting a long-range repulsion between the protons that never saturates, because every proton repels every other. The whole chapter is the negotiation between those two: the drop term makes binding grow with $A$; the Coulomb term taxes it as $Z^2$; the balance draws the valley of stability and sets the summit at iron.

### 1.2 The curve as a decision-maker

Plot binding energy per nucleon against $A$: it climbs steeply (deuteron $1.1$, helium $7.1$), peaks near iron and nickel at about $8.8$ MeV, then slides gently down to $7.6$ at uranium. Any move *up* the curve releases energy. Heavy nuclei climb by splitting in two (fission); light nuclei climb by merging (fusion). Iron is the summit: nothing to gain either way, which is why stellar burning stops there and why the elements' abundance peaks near it.

### 1.3 A clock that cannot be hurried

A radioactive nucleus has no memory and no middle age: the chance it decays in the next second is the same at birth and after a million years. That single statistical assumption forces the exponential law, the half-life, and the strange fact that no temperature, pressure or chemical bond has ever moved a decay constant measurably. A sample is a crowd of independent coin-flippers; the crowd thins predictably even though no individual is predictable.

### 1.4 Everyday anchors

Smoke detectors hold a speck of americium whose alphas ionise the air; carbon dating reads the $^{14}$C clock in wood and bone; nuclear medicine injects tracers whose half-lives are chosen to die with the measurement; a reactor is a fire of neutrons held at $k=1$; the Sun is a fusion reactor whose neutrino flux crosses your thumbnail at $\sim10^{15}$ per second.

> [!info] Why the nucleus does not explode
> The Coulomb repulsion is real but the strong force wins at femtometre range; only when $Z$ grows so large that the unsaturating Coulomb tax outgrows the saturating strong bonus does the nucleus become fragile — the story of alpha decay, fission, and the end of the periodic table.

## Part 2 · Definitions and bookkeeping

### 2.1 The symbol table

| Symbol | Meaning | Notes |
|---|---|---|
| $Z$, $N$, $A$ | protons, neutrons, nucleons | $A=Z+N$ |
| isotopes / isobars / isotones | same $Z$ / same $A$ / same $N$ | the three bookkeeping families |
| $R_0$ | radius constant | $1.2$ fm |
| $\Delta m$ | mass defect | parts minus whole |
| $B$ | binding energy | $\Delta m c^2$ |
| $Q$ | decay or reaction energy | $>0$ exoergic |
| $\lambda$ | decay constant | probability per unit time |
| $T_{1/2}$, $\tau$ | half-life, mean life | $\tau=\frac{1}{\lambda}=1.443\,T_{1/2}$ |
| $A_{\text{ct}}$ | activity | $\lambda N$, becquerel |
| $k$ | multiplication factor | $1$ critical |
| $Z^2/A$ | fissility | the fission tendency |

### 2.2 Units and the mass triangle

Atomic masses in u; energies in MeV; $1$ u $=931.5$ MeV. Use *atomic* masses (which include the electrons) for almost everything: in $\beta^-$ decay the emitted electron is exactly cancelled by the daughter's extra orbital electron, and in $\alpha$ decay the two electrons balance too. Only $\beta^+$ decay keeps a $2m_e$ correction, because the daughter has one electron fewer while a positron is created. This convention rule ends the oldest sign error in nuclear physics.

> [!warning] Condition of validity
> Atomic-mass bookkeeping assumes the electron binding energies ($\sim$ keV) are negligible against MeV scales; for precision $\beta^+$ work keep the $2m_ec^2=1.022$ MeV term.

### 2.3 Sign conventions and frames

$Q>0$ means energy released (mass of ingredients exceeds mass of products); a decay can proceed only with $Q>0$. In the lab frame the parent is at rest, so $Q$ appears as kinetic energy of the products, shared inversely to their masses. Activities are positive scalars; "decay rate" and "activity" are synonyms here.

### 2.4 Assumptions and what is not here

Assumed: two-body kinematics for decays; constant $\lambda$; ideal narrow counting for statistics; uniform nuclear density. Not here: shell-model magic numbers beyond a mention, detailed reactor engineering, neutrino oscillations (named where the solar flux is computed), full Gamow theory (the estimate is derived, the prefactors are not).

> [!question] Exam note
> JEE Advanced frames this chapter as arithmetic with three tools: the mass triangle ($\Delta m\to Q$), momentum sharing in two-body decay, and the exponential law with its log-linear form. Master those and the paper's core is arithmetic.

## Part 3 · Core derivations

### 3.1 Inside the nucleus

The nucleus holds $Z$ protons and $N$ neutrons in a sphere of a few femtometres. Isotopes share $Z$, isobars share $A$, isotones share $N$. Four interactions exist; two matter here:

| Interaction | Relative strength | Range | Role in the nucleus |
|---|---:|---|---|
| strong | 1 | $\sim1$ fm | binds nucleons |
| electromagnetic | $\sim10^{-2}$ | infinite | repels protons |
| weak | $\sim10^{-7}$ | $<10^{-3}$ fm | beta decay |
| gravity | $\sim10^{-38}$ | infinite | irrelevant here |

The strong force's five properties explain the whole chapter: it is attractive at 1-2 fm; short-range (gone beyond $\sim3$ fm); charge-independent (pp, nn, pn nearly equal); saturating (each nucleon binds only neighbours, hence $B\propto A$); and spin-dependent at short range (the deuteron binds only in the triplet state). Why does the nucleus stick together at all? At 2 fm the strong attraction is tens of MeV deep, dwarfing the $\sim1$ MeV Coulomb hill; the protons' repulsion only wins at large $Z$, where the tax grows as $Z^2$ while the strong bonus grows as $A$.

> [!abstract] DIAGRAM D26.1 · The nucleus as a force balance
> *Show:* a sphere of packed nucleons; short sticky bonds drawn between nearest neighbours only; long red repulsion arrows connecting every proton pair; a caption "saturated attraction versus unsaturating repulsion".
> *Search:* "nuclear force saturation Coulomb repulsion nucleus diagram"
> *Used in:* §3.1, §3.4.

### 3.2 Size and density

Scattering evidence — Rutherford's alphas (PART 24), electron scattering, and muonic atom levels (PART 24's exotic atoms) — agrees on

$$
R=R_0A^{1/3},\qquad R_0=1.2\ \text{fm}. \qquad (3.1)
$$

Derive the constant-density reading: if each nucleon carries a fixed volume $v$, the nucleus has $V=Av=\frac43\pi R^3$, so $R\propto A^{1/3}$ — the law *is* the statement that nuclear matter is incompressible and uniform. The density:

$$
\rho=\frac{Am_N}{\frac43\pi R_0^3A}=\frac{3m_N}{4\pi R_0^3}=2.3\times10^{17}\ \text{kg/m}^3, \qquad (3.2)
$$

independent of $A$. A teaspoon ($5$ cm$^3$) of it weighs $\sim1.2\times10^{12}$ kg — a billion tonnes, a mountain in a spoon. Uranium-238 has $R=1.2\times238^{1/3}=7.4$ fm.

> [!abstract] DIAGRAM D26.2 · R against A to the one-third
> *Show:* radius in fm on the vertical axis, A to the one-third on the horizontal; a straight line through the origin of slope 1.2 fm; data points for carbon, iron, gold, uranium marked; the linearity captioned "constant density".
> *Search:* "nuclear radius A to the one third straight line electron scattering"
> *Used in:* §3.2.

### 3.3 Mass defect and the binding-energy curve

Weigh the parts and the whole: the whole is lighter. The mass defect $\Delta m=Zm_H+Nm_n-M_{\text{atom}}$ times $c^2$ is the binding energy $B$ — the energy you must repay to take the nucleus apart. Deuteron: $\Delta m=(1.007825+1.008665-2.014102)=0.002388$ u, $B=2.22$ MeV. Helium-4: $\Delta m=0.030377$ u, $B=28.3$ MeV, $7.07$ per nucleon — the jump from 1.1 (deuteron per nucleon) to 7.1 is why fusion past hydrogen pays so well.

> [!abstract] DIAGRAM D26.3 · The binding-energy-per-nucleon curve
> *Show:* B over A against A; a steep climb through H-2 (1.1), He-4 (7.1), a bump at C-12 and O-16, the broad summit at Fe-56 and Ni-62 near 8.8, the slow slide to U-238 at 7.6; a fusion arrow climbing the left side and a fission arrow climbing from the right, both pointing toward iron.
> *Search:* "binding energy per nucleon curve fusion fission iron peak"
> *Used in:* §3.3-3.4, §3.12-3.13.

Plot $B/A$ against $A$ and the curve becomes the chapter's decision-maker: any process that moves nucleons *up* the curve releases the difference. Fission of uranium to mid-mass fragments climbs from $7.6$ to $\sim8.5$ MeV per nucleon, $\sim0.9$ MeV per nucleon, $\sim200$ MeV per event. Fusion of hydrogen to helium climbs from $\sim0$ to $7.1$. Both dwarf chemistry's eV-scale rearrangements by a factor of $10^7$ per particle. Iron sits at the summit with nothing to gain: the endpoint of stellar burning.

> [!abstract] DIAGRAM D26.4 · The mass defect on a balance
> *Show:* a balance beam; left pan holding separate protons and neutrons labelled with their summed mass; right pan holding the assembled nucleus, lighter, the gap labelled delta-m times c-squared equals B; an arrow "repay B to dismantle".
> *Search:* "mass defect binding energy balance scale diagram"
> *Used in:* §3.3.

### 3.4 The semi-empirical mass formula and the valley of stability

The liquid-drop energy bookkeeping, five terms with physical origins:

$$
B=a_vA-a_sA^{2/3}-a_c\frac{Z^2}{A^{1/3}}-a_a\frac{(N-Z)^2}{A}+\delta(A,Z). \qquad (3.3)
$$

Volume $a_vA$: saturated binding, every nucleon shares equally. Surface $-a_sA^{2/3}$: surface nucleons miss neighbours, a skin tax proportional to area. Coulomb $-a_cZ^2/A^{1/3}$: every proton pair repels, $\propto Z(Z-1)\approx Z^2$, softened by larger radius. Asymmetry $-a_a(N-Z)^2/A$: Pauli exclusion punishes imbalance between the proton and neutron Fermi seas. Pairing $\delta=\pm a_pA^{-1/2}$: even-even nuclei gain, odd-odd lose. Typical coefficients: $a_v\approx15.8$, $a_s\approx18.3$, $a_c\approx0.71$, $a_a\approx23.2$, $a_p\approx12$ MeV.

> [!abstract] DIAGRAM D26.5 · The five terms as a bar chart
> *Show:* for one nucleus (say A = 238): a tall positive volume bar, then negative bars for surface, Coulomb, asymmetry, a small pairing bar; the net binding arrow summing them; a second panel for A = 56 showing the Coulomb bar shrunk.
> *Search:* "semi empirical mass formula terms bar chart liquid drop"
> *Used in:* §3.4.

For fixed $A$, maximising $B$ over $Z$ gives the valley floor:

$$
Z_0=\frac{A}{2+\frac{a_c}{2a_a}A^{2/3}}=\frac{A}{2+0.0154\,A^{2/3}}. \qquad (3.4)
$$

Light nuclei want $N\approx Z$; at $A=100$ the formula gives $Z_0=42.9$ (molybdenum region); at $A=238$ it gives $Z_0=92.4$ — uranium itself. Nuclei off the floor beta-decay toward it: neutron-rich convert neutrons to protons ($\beta^-$), proton-rich the reverse ($\beta^+$ or capture). The valley is the map, beta decay the traffic.

> [!abstract] DIAGRAM D26.6 · The valley of stability
> *Show:* the N-Z plane with the band of stable nuclides curving above N = Z; arrows from the neutron-rich side pointing down-left (beta-minus) and from the proton-rich side up-left (beta-plus/EC); the actinide end labelled alpha territory.
> *Search:* "valley of stability chart of nuclides beta decay directions"
> *Used in:* §3.4, §3.6.

The same two-term competition sets the table's end: Coulomb grows as $Z^2$, surface as $A^{2/3}$; beyond bismuth no configuration is fully stable, and alpha emission becomes the leak — which is why there is no stable nucleus beyond bismuth (OL12 quantifies the limit).

### 3.5 Q-values and reaction bookkeeping

For any decay or reaction, $Q=(\sum m_{\text{in}}-\sum m_{\text{out}})c^2$ in atomic masses, with the electron rule of §2.2. $Q>0$ proceeds spontaneously (subject to barriers and the weak rate); $Q<0$ needs input. Example, neutron capture on U-238: $Q=(238.050788+1.008665-239.054293)\times931.5=4.8$ MeV — the excitation the compound nucleus must shed.

### 3.6 Alpha decay

Why emit a helium nucleus and not four separate nucleons or a proton? Because the alpha's own $28.3$ MeV of binding makes it the cheapest package: for U-238, $Q_\alpha=(M_{238}-M_{234}-M_4)c^2=4.27$ MeV $>0$, while proton emission from the same nucleus has $Q<0$. The alpha's tight binding is the subsidy.

With the parent at rest, momentum conservation splits $Q$ inversely to mass:

$$
K_\alpha=\frac{A-4}{A}Q,\qquad K_{\text{daughter}}=\frac{4}{A}Q. \qquad (3.5)
$$

For U-238: $K_\alpha=\frac{234}{238}\times4.27=4.20$ MeV. Derivation: $p_\alpha=p_d$, $K=\frac{p^2}{2m}$, so $\frac{K_\alpha}{K_d}=\frac{m_d}{m_\alpha}$ and $K_\alpha+K_d=Q$. Because the levels of parent and daughter are discrete, the alphas emerge at discrete energies — a line spectrum, the nuclear analogue of atomic lines (PART 24), with the daughter's excitation subtracting from $Q$.

> [!abstract] DIAGRAM D26.7 · Alpha decay's level diagram and momentum split
> *Show:* parent level at top, daughter levels below with two alpha branches (ground-state and excited-state alphas of different energies), a gamma arrow de-exciting the daughter; an inset of the two back-to-back momentum arrows sized inversely to the masses.
> *Search:* "alpha decay energy level diagram fine structure gamma"
> *Used in:* §3.6.

> [!abstract] DIAGRAM D26.8 · The three decays in matter and in a field
> *Show:* three beams entering a slab: alpha stopping in paper with a short fat track, beta penetrating foil with a thin crooked track, gamma passing lead partially; the same three in a magnetic field: alpha curving gently one way, beta sharply the other, gamma straight.
> *Search:* "alpha beta gamma penetration magnetic deflection comparison"
> *Used in:* §3.6-3.8.

### 3.7 Beta decay and the neutrino

Beta decay changes a nucleon's flavour: $n\to p+e^-+\bar\nu_e$ inside neutron-rich nuclei, $p\to n+e^++\nu_e$ (or by orbital capture, $p+e^-\to n+\nu_e$) in proton-rich ones. $A$ never changes. The crisis that named the neutrino: the electron's energy is *continuous* from zero to an endpoint $E_0=Q$. If only the electron left, energy, momentum and angular momentum would all be violated event by event. Pauli's fix (1930): a third, neutral, nearly massless particle carries the remainder — the endpoint is where it carries nothing. The missing-energy plot is the neutrino's silhouette.

> [!abstract] DIAGRAM D26.9 · The beta spectrum
> *Show:* number of electrons against energy: a smooth hump from 0 to the endpoint E0; the average energy marked near 0.3 E0; the shaded complement labelled "the neutrino's share"; a vertical line at E0 = Q.
> *Search:* "beta decay continuous spectrum endpoint energy neutrino"
> *Used in:* §3.7.

Free neutron decay has $Q=(m_n-m_H)\times931.5=0.782$ MeV and a mean life of about 880 s. A *bound* neutron may or may not decay: the comparison is between whole nuclear masses, not nucleon masses — in stable nuclei the daughter's mass would be higher, $Q<0$, and the neutron is forbidden to die. Binding decides life and death.

> [!warning] Condition of validity
> Atomic masses cancel the electrons automatically for $\beta^-$; for $\beta^+$ keep the $2m_ec^2$ term: $Q_{\beta^+}=(M_{\text{parent}}-M_{\text{daughter}}-2m_e)c^2$.

### 3.8 Gamma emission

After alpha or beta decay the daughter often stands in an excited state; it relaxes by emitting a photon of the level difference — discrete energies, $\Delta A=\Delta Z=0$, pure nuclear de-excitation. Internal conversion is the rival channel: the nucleus hands its energy directly to an orbital electron, which leaves with $E_\gamma$ minus its binding. Long-lived excited states are isomers. Gamma energies are the nuclear level diagram read aloud, exactly as atomic lines read the atomic ladder (PART 24).

### 3.9 The decay law, half-life and mean life

Assume each nucleus has a constant, memoryless probability $\lambda\,dt$ of decaying in $dt$. Then $dN=-\lambda N\,dt$, and integrating:

$$
N=N_0e^{-\lambda t}. \qquad (3.6)
$$

Activity $A_{\text{ct}}=\lambda N$ decays with the same $\lambda$. The half-life $T_{1/2}=\frac{\ln2}{\lambda}$; the mean life, the average lifetime of a nucleus,

$$
\tau=\frac{1}{N_0}\int_0^\infty t\,(-dN)=\frac{1}{\lambda}=\frac{T_{1/2}}{\ln2}=1.443\,T_{1/2}. \qquad (3.7)
$$

Plot $\ln N$ against $t$: a straight line of slope $-\lambda$ — the experimental standard. Because $\lambda$ is a property of the nuclear state and of the weak or strong or tunnelling matrix element alone, no temperature, pressure or chemical environment has moved it measurably; the test is brutal and done — heated, frozen, ionised samples decay on schedule.

> [!abstract] DIAGRAM D26.10 · Exponential decay and its log-linear twin
> *Show:* left panel N against t with the halving staircase marked at one, two, three half-lives; right panel ln N against t, a straight line, slope labelled minus lambda; the mean life marked where N falls to 1/e.
> *Search:* "radioactive decay curve half life log linear plot"
> *Used in:* §3.9.

### 3.10 Chains, equilibrium and accumulation

A parent (1) feeds a radioactive daughter (2): $\frac{dN_2}{dt}=\lambda_1N_1-\lambda_2N_2$. With $N_2(0)=0$ the solution is a rise-and-fall: the daughter activity climbs, peaks, then follows the parent. Two regimes: **secular equilibrium**, parent vastly longer-lived ($\lambda_1\ll\lambda_2$): the daughter's activity grows to *equal* the parent's, $A_2\to A_1$ — the state of old radium samples and of the natural series. **Transient equilibrium**, parent longer-lived but not immensely: the ratio settles at

$$
\frac{A_2}{A_1}=\frac{\lambda_2}{\lambda_2-\lambda_1}. \qquad (3.8)
$$

If the parent is shorter-lived, no equilibrium: the daughter peaks then decays at its own rate. Simultaneous decay modes add their constants, $\lambda=\lambda_a+\lambda_b$, with branching fractions $\frac{\lambda_a}{\lambda}$; accumulation problems (how much stable lead after time $t$?) are the same integral read backwards. The long-term tempo always belongs to the longest-lived member of the chain present.

> [!abstract] DIAGRAM D26.11 · Two-step chain activities in the two regimes
> *Show:* two panels: secular, parent flat and daughter rising to meet it, activities equal thereafter; transient, parent falling slowly, daughter humping then falling parallel beneath it with the constant ratio annotated; time axes in parent half-lives.
> *Search:* "radioactive equilibrium secular transient daughter activity curve"
> *Used in:* §3.10.

> [!abstract] DIAGRAM D26.12 · A decay chain on the nuclide chart
> *Show:* a zigzag path on the N-Z plane: alpha steps diagonally down-left by two and two, beta steps up-left by one; the uranium series sketched to lead-206; step lengths captioned with delta A and delta Z.
> *Search:* "uranium decay series chart of nuclides zigzag alpha beta"
> *Used in:* §3.10.

### 3.11 Dating and tracing

Carbon dating: cosmic rays keep the atmosphere's $^{14}$C/$^{12}$C ratio roughly constant; living matter exchanges carbon and matches it; death stops the intake and the $^{14}$C clock ($T_{1/2}=5730$ y) runs down. Age from the activity ratio:

$$
t=\frac{T_{1/2}}{\ln2}\ln\frac{A_0}{A}. \qquad (3.9)
$$

A sample at $10$ disintegrations per minute per gram against the living $15$: $t=8267\times\ln1.5=3350$ y. Assumptions to state: constant production, closed sample, known initial ratio — the last is why calibration curves from tree rings and corals correct the raw clock. Range: a few hundred to $\sim50{,}000$ years, bounded by counting statistics at the far end. Potassium-argon ($1.25$ Gyr) and uranium-lead ($4.47$ Gyr) date rocks; the isochron method removes the initial-daughter assumption by plotting ratios against a stable reference isotope. Tracers choose half-lives to match the measurement (technetium-99m, 6 h); the smoke detector's americium-241 ionises its gap; radon is a hazard because a gas with an alpha-emitting chain lives long enough to reach lungs.

> [!abstract] DIAGRAM D26.13 · The carbon-dating curve with its limits
> *Show:* activity ratio against age, the exponential fall; horizontal bands at ratio 1 (modern) and about 0.003 (the 50 ka counting limit); a calibration wiggles inset for the last 10 ka captioned "tree rings correct the clock".
> *Search:* "carbon dating decay curve range limit calibration"
> *Used in:* §3.11.

### 3.12 Fission

A thermal neutron on U-235 makes U-236 at excitation above its fission barrier; the drop deforms, Coulomb outruns surface tension at the neck, and it splits — typically into unequal fragments near $A\sim95$ and $140$, plus two or three fast neutrons and $\sim200$ MeV (fragment kinetic energy $\sim165$, neutrons $\sim5$, betas and gammas from the fragments $\sim25$, neutrinos lost $\sim10$). Per gram: $8.2\times10^{10}$ J — a tonne of coal's energy in a gram of uranium, the factor $10^7$ over chemistry.

The released neutrons make a chain possible. The multiplication factor $k$ counts neutrons of one generation against the last: $k<1$ the fire dies, $k=1$ steady (a reactor), $k>1$ rising (a bomb aims for prompt-critical, a reactor is designed never to reach it). Critical mass depends on shape and enrichment because leakage is a surface effect: a sphere minimises it; a reflector shrinks it further. The moderator slows neutrons by elastic collisions — light nuclei (water, heavy water, graphite) take most energy per bounce — because slow neutrons fission U-235 with vastly larger cross-section; it does *not* absorb them, it cools them. Control rods (cadmium, boron) absorb; coolant carries heat; shielding and containment guard the outside. A reactor cannot explode like a bomb: its fuel is dilute, its chain is slow-neutron and delayed-neutron governed, and any excursion heats and poisons it toward shutdown.

> [!abstract] DIAGRAM D26.14 · Three generations at three values of k
> *Show:* three panels of fission trees: k greater than 1 with branches multiplying, k equal 1 with a steady stream, k less than 1 thinning to extinction; generation numbers on the axes.
> *Search:* "chain reaction multiplication factor k diagrams"
> *Used in:* §3.12.

> [!abstract] DIAGRAM D26.15 · The reactor component stack
> *Show:* core with fuel rods and control rods, moderator filling, coolant loop to a steam generator, turbine, containment shell, shielding layer; each labelled with its one-line job.
> *Search:* "nuclear reactor diagram components moderator control rods coolant"
> *Used in:* §3.12.

### 3.13 Fusion

Two protons at touching distance ($\sim2$ fm) face a Coulomb hill of $\frac{ke^2}{2\ \text{fm}}=0.72$ MeV. The naive temperature $k_BT\sim0.72$ MeV gives $T\sim8\times10^9$ K — the classical answer, and wrong for the Sun by a factor of a few hundred. The honest answer (OL2) is tunnelling through the barrier plus the Maxwell tail: the Gamow peak sits where the two exponentials overlap, at $\sim1.5\times10^7$ K for the solar core.

The proton-proton chain: $p+p\to d+e^++\nu$, then $d+p\to{}^3$He$+\gamma$, then $^3$He$+^3$He$\to{}^4$He$+2p$; net $4p\to{}^4$He$+2e^++2\nu+26.7$ MeV (neutrinos carrying away $\sim2\%$). The CNO cycle closes the same net at higher temperature with carbon as catalyst. Lawson criterion states the confinement bargain for a power plant: $n\tau$ above $\sim10^{20}$ s m$^{-3}$ at fusion temperature — hot, dense, held long enough. Fusion is hard because no material container survives; magnetic and inertial schemes trade one impossibility for another.

The Sun's budget: luminosity $L=3.83\times10^{26}$ W implies mass loss $\frac{L}{c^2}=4.3\times10^9$ kg every second — four million tonnes, yet only $10^{-21}$ of its mass per year, which is why it lasts gigayears (OL7).

> [!abstract] DIAGRAM D26.16 · The Coulomb barrier with the Gamow window
> *Show:* potential energy against separation: the Coulomb hill bending down to a deep nuclear well at 2 fm; a few-MeV alpha or proton energy line far below the summit; the tunnelling region shaded; a right panel with the Maxwell distribution, the tunnelling probability, and their product peak labelled Gamow window.
> *Search:* "Coulomb barrier tunneling Gamow peak fusion diagram"
> *Used in:* §3.13, OL2.

> [!abstract] DIAGRAM D26.17 · The p-p chain ladder
> *Show:* four protons at top; the weak first step to deuterium with positron and neutrino; the radiative step to He-3; the branch merging two He-3 to He-4 plus two protons; the net 26.7 MeV bracketed.
> *Search:* "proton proton chain reactions diagram solar fusion"
> *Used in:* §3.13.

### 3.14 Detectors and counting statistics

A cloud chamber shows the chapter's zoo directly: alphas leave short, fat, straight tracks (dense ionisation, heavy, unflected), betas thin crooked ones (light, scattered), gammas sparse electron sprays. A Geiger counter counts pulses but is blind for a dead time after each — at high rates it undercounts, corrected by $\frac{n}{1-n\tau_d}$. Counting is Poissonian: $N$ counts carry uncertainty $\sqrt N$, so a percentage error $\frac{1}{\sqrt N}$; halving the error needs four times the counts or the time (OL8). This is PART 1's error arithmetic grown up: the statistics of the quantum coin.

## Part 4 · Results, limits and the validity ledger

### 4.1 Boxed results

$$
\boxed{R=1.2\,A^{1/3}\ \text{fm},\quad \rho_{\text{nuc}}=2.3\times10^{17}\ \text{kg/m}^3} \qquad (4.1)
$$

uniform-density liquid drop; surface fuzz at the percent level.

$$
\boxed{B=\Delta m\,c^2,\quad 1\ \text{u}=931.5\ \text{MeV}} \qquad (4.2)
$$

atomic masses with the electron rule of §2.2.

$$
\boxed{K_\alpha=\frac{A-4}{A}Q} \qquad (4.3)
$$

two-body decay from rest.

$$
\boxed{N=N_0e^{-\lambda t},\quad A_{\text{ct}}=\lambda N,\quad \tau=\frac{1}{\lambda}=1.443\,T_{1/2}} \qquad (4.4)
$$

constant, memoryless $\lambda$.

$$
\boxed{t_{\text{age}}=\frac{T_{1/2}}{\ln2}\ln\frac{A_0}{A},\quad \frac{A_2}{A_1}=\frac{\lambda_2}{\lambda_2-\lambda_1}\ (\text{transient})} \qquad (4.5)
$$

closed system; known initial ratio.

$$
\boxed{Z_0=\frac{A}{2+0.0154A^{2/3}}} \qquad (4.6)
$$

liquid-drop valley floor.

### 4.2 Limit checks

- $A\to$ small: $B/A$ collapses (surface dominates), the deuteron's fragility, correct.
- $A\to$ large: Coulomb drags $B/A$ down and $Z_0/N$ up, the valley bends, correct.
- $\lambda_1\ll\lambda_2$ in Eq. (4.5): ratio $\to1$, secular equilibrium, correct.
- $T_{1/2}\to\infty$: activity $\to0$ at fixed $N$, stability, correct.
- $k\to1^-$: the reactor shuts down gently, correct.
- barrier $\to0$: fusion at room temperature, the classical-limit sanity, correct.

### 4.3 Which formula when

| Given | Need | Use |
|---|---|---|
| masses | $Q$ | Eq. (4.2) with electron rule |
| alpha $Q$ | alpha kinetic energy | Eq. (4.3) |
| $T_{1/2}$ | $\lambda$, $\tau$, activity | Eq. (4.4) |
| activity ratio | age | Eq. (4.5) first |
| parent-daughter chain | equilibrium ratio | Eq. (4.5) second |
| $A$ | radius, density | Eq. (4.1) |
| isobar | stable $Z$ | Eq. (4.6) |
| reactor power | fissions per second, fuel mass | $200$ MeV per fission |

### 4.4 Concept checks

**C1 — concept check.** Why is nuclear density the same for all nuclei?

<details><summary>Answer</summary>

Saturated binding gives volume proportional to A, so mass over volume is constant.

</details>

**C2 — concept check.** The binding energy per nucleon of He-4 versus the deuteron, and the consequence?

<details><summary>Answer</summary>

7.1 versus 1.1 MeV: fusing light nuclei climbs the curve steeply, hence large fusion yields.

</details>

**C3 — concept check.** Which side of iron releases energy by fission, which by fusion?

<details><summary>Answer</summary>

Heavier than iron fission; lighter fusion; iron neither.

</details>

**C4 — concept check.** Why does alpha decay beat proton emission for heavy nuclei?

<details><summary>Answer</summary>

The alpha's 28.3 MeV binding subsidises the Q-value; proton separation stays negative.

</details>

**C5 — concept check.** A beta spectrum is continuous. What carries the rest?

<details><summary>Answer</summary>

The (anti)neutrino; the endpoint is where it carries nothing.

</details>

**C6 — concept check.** Why can a bound neutron be stable while a free one decays?

<details><summary>Answer</summary>

Q compares whole nuclear masses; in stable nuclei the would-be daughter is heavier.

</details>

**C7 — concept check.** Does heating a sample change its half-life?

<details><summary>Answer</summary>

No: lambda is a nuclear property; tested and null to high precision.

</details>

**C8 — concept check.** After three half-lives, what fraction of activity remains?

<details><summary>Answer</summary>

12.5 percent.

</details>

**C9 — concept check.** Mean life versus half-life, numerically?

<details><summary>Answer</summary>

tau = 1.443 times T-half.

</details>

**C10 — concept check.** Secular equilibrium in one line?

<details><summary>Answer</summary>

Long-lived parent: daughter activity grows until it equals the parent's.

</details>

**C11 — concept check.** Why does a moderator slow neutrons rather than absorb them?

<details><summary>Answer</summary>

Light nuclei take kinetic energy in elastic collisions; absorption is the control rods' job.

</details>

**C12 — concept check.** Why cannot a reactor explode like a bomb?

<details><summary>Answer</summary>

Dilute fuel, delayed neutrons, negative feedbacks: k cannot prompt-critical by design.

</details>

**C13 — concept check.** The Sun's naive Coulomb temperature versus its real core, and the reason for the gap?

<details><summary>Answer</summary>

About 1e10 K versus 1.5e7 K: tunnelling plus the Maxwell tail (the Gamow window).

</details>

**C14 — concept check.** N counts carry what uncertainty, and what does halving the error cost?

<details><summary>Answer</summary>

sqrt N; four times the counts or counting time.

</details>

## Part 5 · Worked exemplars

### E1 — Helium-4 binding from the mass defect

Compute B and B/A for He-4.

> [!success] Check
> B/A must sit between the deuteron's 1.1 and iron's 8.8, on the steep climb.

<details><summary>Solution</summary>

**Method.** $\Delta m=2(1.007825)+2(1.008665)-4.002603=0.030377$ u; $B=0.030377\times931.5=28.3$ MeV; $B/A=7.07$ MeV.

</details>

### E2 — Radius and the density check for U-238

Find R and confirm the density is A-independent.

> [!success] Check
> Density must reproduce 2.3e17 kg/m3 exactly as for carbon.

<details><summary>Solution</summary>

**Method.** $R=1.2\times238^{1/3}=7.44$ fm. $\rho=\frac{238\times1.66\times10^{-27}}{\frac43\pi(7.44\times10^{-15})^3}=2.3\times10^{17}$ kg/m$^3$, the universal value of Eq. (3.2).

</details>

### E3 — Alpha decay of U-238: Q and the split

With $Q=4.27$ MeV, find the alpha's kinetic energy.

> [!success] Check
> The alpha must carry almost all of Q: fraction (A-4)/A = 0.983.

<details><summary>Solution</summary>

**Method.** $K_\alpha=\frac{234}{238}\times4.27=4.20$ MeV; the daughter recoils with $0.07$ MeV.

</details>

### E4 — Beta-minus Q for carbon-14

Atomic masses: C-14 14.003242 u, N-14 14.003074 u. Find Q.

> [!success] Check
> Atomic masses need no electron correction for beta-minus; Q must be the known 156 keV.

<details><summary>Solution</summary>

**Method.** $Q=(14.003242-14.003074)\times931.5=0.156$ MeV, shared between electron and antineutrino.

</details>

### E5 — A positron emitter with the 2m-e correction

N-13 (13.005739 u) decays to C-13 (13.003355 u). Find the positron endpoint.

> [!success] Check
> Endpoint must be the EC Q minus 1.022 MeV.

<details><summary>Solution</summary>

**Method.** $Q_{\beta^+}=(13.005739-13.003355-2\times0.000549)\times931.5=1.20$ MeV.

</details>

### E6 — The curie, from a gram of radium

Show that 1 g of Ra-226 (T-half 1600 y) has an activity of about 1 Ci.

> [!success] Check
> The historical curie was defined by this very sample; expect 0.99-1.0 Ci.

<details><summary>Solution</summary>

**Method.** $\lambda=\frac{\ln2}{1600\times3.156\times10^7}=1.37\times10^{-11}$ s$^{-1}$; $N=\frac{6.022\times10^{23}}{226}=2.66\times10^{21}$; $A=\lambda N=3.66\times10^{10}$ Bq $=0.99$ Ci.

</details>

### E7 — A carbon age

A sample counts 10 dpm/g against the living 15. Age?

> [!success] Check
> Between one and two half-lives (15 to 7.5 to 3.75), so 3-6 ka.

<details><summary>Solution</summary>

**Method.** $t=\frac{5730}{\ln2}\ln\frac{15}{10}=8267\times0.405=3350$ y.

</details>

### E8 — Technetium through a working day

Tc-99m (T-half 6 h) is prepared at 8:00 with activity 800 MBq. Activity at 20:00?

> [!success] Check
> Two half-lives: one quarter.

<details><summary>Solution</summary>

**Method.** $800\times2^{-2}=200$ MBq.

</details>

### E9 — Mass of a curie of cobalt-60

Co-60, T-half 5.27 y. What mass has A = 3.7e10 Bq?

> [!success] Check
> Sub-milligram: a curie of a years-scale nuclide is a speck.

<details><summary>Solution</summary>

**Method.** $\lambda=\frac{\ln2}{5.27\times3.156\times10^7}=4.17\times10^{-9}$ s$^{-1}$; $N=\frac{3.7\times10^{10}}{4.17\times10^{-9}}=8.9\times10^{18}$; $m=\frac{8.9\times10^{18}}{6.022\times10^{23}}\times60=8.8\times10^{-4}$ g.

</details>

### E10 — Fissions per second in a gigawatt

A reactor runs at 1 GW thermal. Fissions per second?

> [!success] Check
> About 3e19: the standard number.

<details><summary>Solution</summary>

**Method.** $\frac{10^9}{200\times1.602\times10^{-13}}=3.1\times10^{19}$ s$^{-1}$.

</details>

### E11 — A gram of uranium against coal

Energy per gram of U-235, and the coal equivalent (coal about 2.4e10 J per tonne).

> [!success] Check
> The factor of about 10^7 per particle must surface as about 3000 tonnes per kg.

<details><summary>Solution</summary>

**Method.** $8.2\times10^{10}$ J/g; coal equivalent $\frac{8.2\times10^{10}}{2.4\times10^{10}}=3.4$ tonnes per gram, $\sim3400$ tonnes per kg.

</details>

### E12 — The valley floor at A = 100

Most stable Z for A = 100?

> [!success] Check
> Near the real stable isobars Mo/Ru (Z 42-44).

<details><summary>Solution</summary>

**Method.** $Z_0=\frac{100}{2+0.0154\times100^{2/3}}=\frac{100}{2.33}=42.9$.

</details>

## Part 6 · Problem archetypes and practice

### 6.1 Archetypes

| # | Archetype | Template | Where worked | Variations |
|---:|---|---|---|---|
| 1 | Binding energy from masses | $\Delta m c^2$ | E1, Q3 | per nucleon comparisons |
| 2 | Radius and density | Eq. (4.1) | E2, Q1-Q2 | any A |
| 3 | Q-value with electron rule | atomic masses | E4, E5, Q4 | beta-plus keeps 2m-e |
| 4 | Alpha energy split | Eq. (4.3) | E3, Q5 | daughter recoil |
| 5 | Decay bookkeeping | A and Z balance | Q6-Q8 | series counting |
| 6 | Activity and mass | $A=\lambda N$ | E6, E9, Q13 | curie and becquerel |
| 7 | Remaining fraction | $2^{-n}$ | E8, Q9 | non-integer n via ln |
| 8 | Age from ratio | Eq. (4.5) | E7, Q12 | K-Ar, U-Pb scales |
| 9 | Mean life conversions | $\tau=1.443T_{1/2}$ | Q11 | lambda in s-1 |
| 10 | Equilibrium ratios | secular 1; transient Eq. (4.5) | Q14-Q15 | daughter maximum |
| 11 | Fission power arithmetic | 200 MeV per fission | E10, Q16-Q17 | per gram, per day |
| 12 | Coulomb barrier | $\frac{kZ_1Z_2e^2}{r}$ | Q21-Q22 | naive temperature |
| 13 | Solar budget | $L/c^2$, neutrino flux | Q23-Q24 | lifetime |
| 14 | Valley floor Z0 | Eq. (4.6) | E12, Q26 | fissility |
| 15 | Counting statistics | $\sqrt N$ | Q19, Q28 | measurement time |
| 16 | Branching decay | fractions $\lambda_i/\lambda$ | Q18 | accumulation |

### 6.2 In-flow practice

#### Q1. Radius of carbon-12?

<details><summary>Solution</summary>

$1.2\times12^{1/3}=2.75$ fm.

</details>

#### Q2. Density of carbon versus uranium?

<details><summary>Solution</summary>

Identical, $2.3\times10^{17}$ kg/m$^3$: the A cancels.

</details>

#### Q3. Binding per nucleon of the deuteron?

<details><summary>Solution</summary>

$2.22/2=1.11$ MeV.

</details>

#### Q4. Q of D plus T giving He-4 plus neutron?

<details><summary>Solution</summary>

$\Delta m=2.014102+3.016049-4.002603-1.008665=0.018883$ u; $Q=17.6$ MeV.

</details>

#### Q5. Alpha kinetic energy from Po-210 (Q = 5.4 MeV)?

<details><summary>Solution</summary>

$K_\alpha=5.4\times\frac{206}{210}=5.30$ MeV.

</details>

#### Q6. U-238 emits an alpha. The daughter?

<details><summary>Solution</summary>

Th-234.

</details>

#### Q7. Th-234 beta-minus decays. The product?

<details><summary>Solution</summary>

Pa-234.

</details>

#### Q8. Count alphas and betas in U-238 to Pb-206.

<details><summary>Solution</summary>

$\Delta A=32=4n_\alpha\Rightarrow8$ alphas; charge: $92-16+n_\beta=82\Rightarrow6$ betas.

</details>

#### Q9. Activity fraction after three half-lives?

<details><summary>Solution</summary>

$1/8$.

</details>

#### Q10. Decay constant for T-half = 8 days, in per-seconds?

<details><summary>Solution</summary>

$\lambda=\frac{0.693}{6.9\times10^5}=1.0\times10^{-6}$ s$^{-1}$.

</details>

#### Q11. Mean life of C-14?

<details><summary>Solution</summary>

$1.443\times5730=8270$ y.

</details>

#### Q12. Age when the activity ratio is one quarter?

<details><summary>Solution</summary>

Two half-lives: $11460$ y.

</details>

#### Q13. Mass of 1 mCi of Co-60?

<details><summary>Solution</summary>

$0.88$ µg (E9 scaled).

</details>

#### Q14. Secular equilibrium activity ratio?

<details><summary>Solution</summary>

$1$.

</details>

#### Q15. Transient ratio when the daughter's lambda is triple the parent's?

<details><summary>Solution</summary>

$\frac{3\lambda}{3\lambda-\lambda}=\frac32$.

</details>

#### Q16. Fissions per second at 3 GW thermal?

<details><summary>Solution</summary>

$9.4\times10^{19}$.

</details>

#### Q17. U-235 burned per day by a 1 GW electric plant at 33 % efficiency?

<details><summary>Solution</summary>

Thermal power 3 GW: $3\times1.05\approx3.2$ kg/day.

</details>

#### Q18. A nuclide decays by two modes with lambda-a = 2 lambda-b. Branching fraction of mode a?

<details><summary>Solution</summary>

$\frac{2}{3}$.

</details>

#### Q19. 10 000 counts: percentage uncertainty?

<details><summary>Solution</summary>

$\frac{100}{10000}=1\%$.

</details>

#### Q20. Time to fall to one thousandth of activity?

<details><summary>Solution</summary>

$\sim10$ half-lives ($2^{10}=1024$).

</details>

#### Q21. Coulomb barrier for two touching nuclei with Z1 Z2 = 1 at 2 fm?

<details><summary>Solution</summary>

$\frac{1.44\ \text{MeV fm}}{2\ \text{fm}}=0.72$ MeV.

</details>

#### Q22. The naive temperature for that barrier?

<details><summary>Solution</summary>

$T=\frac{0.72\times10^6\times11600\ \text{K/eV}}{1}\approx8\times10^9$ K.

</details>

#### Q23. Solar mass lost per day?

<details><summary>Solution</summary>

$4.26\times10^9\times86400=3.7\times10^{14}$ kg.

</details>

#### Q24. Solar neutrinos through a 1 cm-squared thumbnail per second?

<details><summary>Solution</summary>

$6\times10^{14}\times10^{-4}=6\times10^{10}$.

</details>

#### Q25. Verify the p-p net energy of 26.7 MeV from atomic masses, including the positrons' annihilation.

<details><summary>Solution</summary>

$(4\times1.007825-4.002603-2\times0.000549)\times931.5=25.7$ MeV; add the two annihilation quanta $2\times0.511=1.02$ MeV recovered in the star: $26.7$ MeV.

</details>

#### Q26. Valley floor Z0 for A = 238?

<details><summary>Solution</summary>

$\frac{238}{2+0.0154\times238^{2/3}}=\frac{238}{2.59}=92$: uranium sits on its own floor.

</details>

#### Q27. Fissility Z-squared over A for U-235 and U-238?

<details><summary>Solution</summary>

$36.0$ and $35.6$; the higher fissility is one reason U-235 fissions with slow neutrons.

</details>

#### Q28. To halve a counting uncertainty, the counting time must?

<details><summary>Solution</summary>

Quadruple.

</details>

> [!abstract] DIAGRAM D26.18 · Cloud chamber tracks of the three radiations
> *Show:* a cloud chamber photograph in words: short thick straight alpha tracks from a source dot; long thin kinked beta tracks; sparse delta-ray wisps for gammas; a magnetic field curving betas visibly, alphas barely.
> *Search:* "cloud chamber alpha beta tracks photograph"
> *Used in:* §3.14.

## Part 7 · Alternate methods and the JEE-Advanced advantage toolkit

### 7.1 The mass triangle with the electron rule

Convert every mass difference straight to MeV with $931.5$, using atomic masses and the one rule: beta-minus cancels electrons, beta-plus keeps $2m_e$. Demonstration: C-14's Q in one subtraction (E4). Fails only at keV precision, where electron binding matters.

### 7.2 The halving ladder

For integer half-lives skip exponentials: $n$ half-lives leave $2^{-n}$. For odd ratios use $\log_2$: $\frac{A_0}{A}=10$ is $\log_2 10=3.32$ half-lives. Demonstration: one thousandth is ten half-lives to 3 % accuracy. Fails when the chain feeds; then the equilibrium forms take over.

### 7.3 Momentum-sharing shortcut

In any two-body decay from rest, the lighter product takes $\frac{M_{\text{heavy}}}{M_{\text{total}}}$ of Q. Demonstration: the alpha's $\frac{A-4}{A}$; the recoil nucleus's sliver explains why daughter damage is local. Fails for three-body beta decay — the spectrum is the failure made visible.

### 7.4 The curve as auditor

Before accepting any fission or fusion energy answer, locate both ends on the B/A curve: the per-nucleon gain must be positive and of order the curve's difference (0.1-1 MeV). An answer outside that band is wrong before the arithmetic is checked.

### 7.5 The log-linear fit

Half-life from data: plot ln A against t, slope is $-\lambda$; two points suffice: $T_{1/2}=\frac{(t_2-t_1)\ln2}{\ln(A_1/A_2)}$. Demonstration: activities 800 then 200 MBq over 12 h give T-half 6 h.

### 7.6 The sqrt-N planner

Want 1 % error: 10 000 counts. Want 0.5 %: 40 000. Plan counting time backwards from the required precision; the Poisson coin is the only examiner that never bluffs.

## Part 8 · Examiner traps

> [!danger] Trap 1 — the beta electron bookkeeping
> Adding bare nuclear masses in beta decay, or dropping the 2 m-e in beta-plus. Reply: atomic masses cancel for beta-minus; beta-plus keeps the positron and the missing orbital electron.

> [!danger] Trap 2 — the neutrino's silent share
> Giving the electron all of Q. Reply: the spectrum is continuous; only the endpoint electron takes Q.

> [!danger] Trap 3 — the missing ln 2
> Writing N = N0 e to the minus t over T-half. Reply: the exponent is lambda t with lambda = ln2 over T-half.

> [!danger] Trap 4 — activity versus number
> Equating a big activity with a big mass. Reply: A = lambda N; a short-lived speck outradiates a long-lived kilogram.

> [!danger] Trap 5 — lambda scales with sample
> Halving the sample and halving lambda. Reply: lambda is intensive; A halves, lambda stays.

> [!danger] Trap 6 — delta A in beta
> Changing A by one in beta decay. Reply: beta moves Z, not A.

> [!danger] Trap 7 — half-life as mean life
> Using T-half where tau belongs, or vice versa. Reply: tau = 1.443 T-half; the integral defines tau.

> [!danger] Trap 8 — the absorbing moderator
> Saying the moderator absorbs neutrons. Reply: it slows them; absorption is control rods and poisons.

> [!danger] Trap 9 — the reactor bomb
> Letting a reactor "explode like a bomb". Reply: dilute fuel, delayed neutrons, negative feedbacks; a steam explosion is not a nuclear one.

> [!danger] Trap 10 — the classical fusion temperature
> Quoting 1e10 K for the Sun. Reply: that is the roll-over temperature; tunnelling and the Maxwell tail bring it to 1.5e7 K.

> [!danger] Trap 11 — the one-step Sun
> Treating solar fusion as a single 4p-to-He collision. Reply: it is a chain whose first weak step sets the Sun's clock.

## Part 9 · Playbook

### 9.1 Triage decision tree

- Masses given: Q-value first, electron rule second.
- "Energy of the alpha": momentum share, Eq. (4.3).
- Time and activity: halving ladder or log-linear.
- Age: ratio into Eq. (4.5).
- Chain words: equilibrium regime named before arithmetic.
- Reactor words: 200 MeV per fission, then power bookkeeping.
- Sun words: L over c-squared, barrier, Gamow honesty.

### 9.2 Formula map with validity

| Formula | Valid when | Breaks when |
|---|---|---|
| Eq. (4.1) | liquid drop | halo nuclei, surface fuzz |
| Eq. (4.2) | atomic masses + electron rule | keV precision |
| Eq. (4.3) | two-body from rest | beta decay |
| Eq. (4.4) | constant lambda | never, in this domain |
| Eq. (4.5) | closed chain | open systems, initial daughter |
| Eq. (4.6) | liquid drop valley | shell closures (magic numbers) |

### 9.3 Constants to carry

$931.5$ MeV/u; $R_0=1.2$ fm; $2.3\times10^{17}$ kg/m$^3$; $200$ MeV/fission; $8.2\times10^{10}$ J/g; C-14 5730 y; Ra-226 1600 y about 1 Ci/g; tau = 1.44 T-half; solar loss $4.3\times10^9$ kg/s; neutrino flux $6\times10^{14}$ m$^{-2}$s$^{-1}$.

### 9.4 Timing plan

A and B under two minutes; C three; D twelve. Any Q-value not reduced to one mass subtraction in a minute is mis-bookkeeping; redraw with atomic masses.

### 9.5 Pre-submission audit, ten points

1. Electron rule applied per decay type.
2. Neutrino remembered in beta.
3. ln 2 present in exponents.
4. Activity and N distinguished.
5. Two-body sharing used only for two bodies.
6. Equilibrium regime named.
7. Units: u, MeV, Bq, y consistent.
8. Curve audit on fission/fusion energies.
9. One limit pushed.
10. Every sub-part answered.

## Part 10 · Olympiad extension

### OL1 — Geiger-Nuttall from a tunnelling estimate

The alpha lives in the nuclear well behind a Coulomb hill of height $\sim\frac{2(Z-2)e^2}{4\pi\varepsilon_0 r}$. The Gamow penetration factor for energy $E$ gives $\log_{10}\lambda\approx a-\frac{bZ}{\sqrt{E}}$. Use U-238 ($E=4.27$ MeV, $T_{1/2}=4.5\times10^9$ y) and Po-212 ($E=8.95$ MeV, $T_{1/2}=3\times10^{-7}$ s) to show why a factor two in energy swings the half-life by $\sim10^{24}$.

<details><summary>Solution</summary>

**Method.** The barrier width scales as $\frac{1}{E}$, and the WKB exponent as $\frac{Z}{\sqrt E}$: halving $\sqrt E$ roughly doubles the exponent, and the decay constant is exponential in it. $\log_{10}T$ changes by $\sim24$ between the two nuclides while $\frac{1}{\sqrt E}$ changes from $0.484$ to $0.334$ MeV$^{-1/2}$ — a 30 % change in the argument producing 24 decades: the exponential amplifier is the whole story. Plotting $\log T_{1/2}$ against $\frac{1}{\sqrt E}$ for one element gives the Geiger-Nuttall straight line, the empirical law (1911) that Gamow's 1928 tunnelling explained — the first triumph of quantum mechanics inside the nucleus.

**Checks.** (i) Same-Z families lie on one line. (ii) The slope grows with Z, as $bZ$ says.

</details>

### OL2 — Why the Sun's core is 15 MK, not 10 to the 10 K

The naive $k_BT\sim0.72$ MeV gives $T\sim8\times10^9$ K. The honest rate convolves the Maxwell tail with the tunnelling factor $e^{-\sqrt{E_G/E}}$, producing a Gamow peak at $E_0=\left(\frac{E_G(kT)^2}{4}\right)^{1/3}$; for pp with $E_G\approx490$ keV at $kT=1.3$ keV, $E_0\approx6$ keV — reactions happen at energies far above $kT$ but far below the barrier. State the exponential rate $\propto\exp\left[-3\left(\frac{E_G}{4kT}\right)^{1/3}\right]$ and explain in two sentences why this moves the required temperature down by hundreds.

<details><summary>Solution</summary>

**Method.** The exponent $-3(E_G/4kT)^{1/3}\approx-3(94.2)^{1/3}/1\approx-13.6$ at 15 MK: a survivable suppression, versus the classical $e^{-550}$, which is zero for any practical star. Tunnelling converts an impossible exponential into a moderate one; the Maxwell tail supplies the few fast particles; their overlap is the Gamow window. The Sun is a tunnelling machine, and its slow weak first step (OL11) is why it shines gently for gigayears instead of flashing.

**Checks.** (i) Raising T to 1e10 K makes the exponent tiny: classical regime recovered. (ii) Heavier fuels (CNO, $Z$ larger, $E_G$ bigger) need higher T, as stellar evolution shows.

</details>

### OL3 — The fission barrier and why U-235 but not U-238

Deforming the drop raises surface energy (more skin) and lowers Coulomb energy (protons apart); the barrier is the hump between. Its height shrinks as the fissility $\frac{Z^2}{A}$ grows, vanishing near $\frac{Z^2}{A}\approx50$. U-235 (36.0) and U-238 (35.6) sit far below the limit, yet U-235 fissions with slow neutrons and U-238 needs fast ones. Explain with pairing.

<details><summary>Solution</summary>

**Method.** The barrier is $\sim6$ MeV for both. Adding a thermal neutron to U-235 makes U-236 *even-even*, gaining a pairing bonus $\sim\frac{12}{\sqrt{236}}\approx0.8$ MeV extra excitation: $6.5$ MeV of excitation beats the barrier. U-238 plus a neutron makes odd-even U-239 with no bonus: $4.8$ MeV, below the barrier — only a fast neutron's kinetic energy closes the gap. One pairing term, two different destinies.

**Checks.** (i) Fissilities 36.0/35.6 computed in Q27. (ii) Th-232 behaves like U-238, as reactors show.

</details>

### OL4 — The valley floor, derived

Maximise $B(A,Z)$ of Eq. (3.3) over Z at fixed A and derive Eq. (3.4); evaluate for A = 100 and A = 238, and state what shell effects do to the floor.

<details><summary>Solution</summary>

**Method.** $\frac{\partial B}{\partial Z}=-2a_cZ A^{-1/3}+4a_a\frac{A-2Z}{A}=0$ (pairing's derivative ignored); solving $Z_0=\frac{4a_aA}{8a_a+a_cA^{2/3}}=\frac{A}{2+\frac{a_c}{2a_a}A^{2/3}}$. A = 100: $42.9$; A = 238: $92.0$. Magic numbers dent and bump the smooth floor — the liquid drop is the mean trend, shells the weather.

**Checks.** (i) Small A returns N ≈ Z. (ii) Coefficients give the quoted 0.0154.

</details>

### OL5 — Transient equilibrium in full

Solve $\frac{dN_2}{dt}=\lambda_1N_1-\lambda_2N_2$ with $N_2(0)=0$; find the daughter activity, the equilibrium ratio, and the time of maximum daughter activity.

<details><summary>Solution</summary>

**Method.** $N_2(t)=\frac{\lambda_1N_1(0)}{\lambda_2-\lambda_1}\left(e^{-\lambda_1t}-e^{-\lambda_2t}\right)$. For $\lambda_1<\lambda_2$, late times keep $e^{-\lambda_1t}$: $A_2=\lambda_2N_2\to\frac{\lambda_2}{\lambda_2-\lambda_1}A_1$, Eq. (3.8). Maximum at $\frac{dN_2}{dt}=0$: $t_{\max}=\frac{\ln(\lambda_2/\lambda_1)}{\lambda_2-\lambda_1}$. Secular limit $\lambda_1\to0$: ratio $\to1$.

**Checks.** (i) $t\to0$: $N_2\to0$ with zero slope. (ii) Dimensions of t_max are time.

</details>

### OL6 — Solar neutrinos through your thumb

From $L=3.83\times10^{26}$ W and 26.7 MeV per helium (two neutrinos each), compute the neutrino flux at Earth and the rate through 1 cm squared.

<details><summary>Solution</summary>

**Method.** Helium rate $=\frac{L}{26.7\ \text{MeV}}=8.9\times10^{37}$ s$^{-1}$; neutrino rate $1.8\times10^{38}$ s$^{-1}$; flux $=\frac{1.8\times10^{38}}{4\pi(1.496\times10^{11})^2}=6.4\times10^{14}$ m$^{-2}$s$^{-1}$; through a cm$^2$, $6\times10^{10}$ per second — tens of billions through your thumbnail, nearly all passing through the Earth as if it were not there.

**Checks.** (i) Flux falls as $1/d^2$. (ii) Kamiokande's measured flux (after oscillation physics) is of this order.

</details>

### OL7 — A reactor's daily meal and the ten-half-life rule

(a) Derive the 1.05 kg per day per GW thermal figure. (b) A waste isotope of 30 y half-life is stored 300 y. What fraction remains, and why is "ten half-lives" the engineering shorthand?

<details><summary>Solution</summary>

**Method.** (a) $E_{\text{day}}=10^9\times86400=8.6\times10^{13}$ J; mass $=\frac{8.6\times10^{13}}{8.2\times10^{10}}=1.05$ kg. (b) $2^{-10}\approx10^{-3}$: 0.1 % — each decade of half-lives is a factor 1000 in activity, so ten is the "three orders per decade, three decades" rule of thumb that turns scary into manageable.

**Checks.** (i) The electrical figure triples at 33 % efficiency. (ii) 300 y is indeed ten 30-y half-lives.

</details>

### OL8 — Counting statistics from the Poisson coin

Derive sigma = sqrt N for N independent decay counts and solve: a source gives 100 counts per minute plus negligible background. How long to measure the rate to 1 %?

<details><summary>Solution</summary>

**Method.** Poisson variance equals the mean: $\sigma_N=\sqrt N$, so $\frac{\sigma_N}{N}=\frac{1}{\sqrt N}=0.01\Rightarrow N=10^4$ counts, i.e. 100 minutes. The square-root tax is why weak samples demand long nights.

**Checks.** (i) Four times the time halves the error. (ii) Background, when present, adds in quadrature — the real lab's correction.

</details>

### OL9 — Dating a rock with two isotopes: the isochron

A rock suite has varying Rb-87/Sr-86 but the same initial Sr-87/Sr-86. Show that plotting present Sr-87/Sr-86 against Rb-87/Sr-86 yields a straight line whose slope is $e^{\lambda t}-1$, and read an age from slope 0.05 with lambda = 1.42e-11 per year.

<details><summary>Solution</summary>

**Method.** $\frac{^{87}\text{Sr}}{^{86}\text{Sr}}=\left(\frac{^{87}\text{Sr}}{^{86}\text{Sr}}\right)_0+\frac{^{87}\text{Rb}}{^{86}\text{Sr}}(e^{\lambda t}-1)$: slope 0.05 gives $e^{\lambda t}=1.05$, $t=\frac{\ln1.05}{1.42\times10^{-11}}=3.4\times10^9$ y. The intercept absorbs the unknown initial daughter — the isochron's gift.

**Checks.** (i) Slope grows with t. (ii) All samples of one rock fall on one line only if they are coeval: discordance exposes disturbance.

</details>

### OL10 — Nucleon spacing versus the thermal neutron's wave

From the nuclear density, estimate the mean nucleon spacing and compare with the 25 meV neutron's wavelength. Conclude why slow neutrons diffract from crystals (linking PARTS 23 and 25).

<details><summary>Solution</summary>

**Method.** Spacing $\approx(1/0.17\ \text{fm}^{-3})^{1/3}\approx1.8$ fm inside nuclei — but in *crystals* the relevant spacing is the lattice's Å scale, and the thermal neutron's $1.8$ Å wavelength matches it. Inside the nucleus the neutron's wave is far longer than the spacing, so it sees the nucleus as a point — the same wave logic at two different rulers.

**Checks.** (i) 1.8 Å from Q13 of PART 23. (ii) Cold neutrons (longer λ) probe larger structures, as spectrometrists use.

</details>

### OL11 — The p-p chain audit and the Sun's lifetime

(a) Verify 26.7 MeV from masses including annihilation. (b) With 10 % of the Sun's 70 % hydrogen available to burn, estimate the main-sequence lifetime.

<details><summary>Solution</summary>

**Method.** (a) Q25: 25.7 MeV from masses plus 1.02 MeV recovered annihilation = 26.7 MeV. (b) Available energy $=0.07\times0.7\times1.99\times10^{30}\times0.007c^2\approx8.7\times10^{43}$ J (0.7 % of the fused mass radiates); $t=\frac{8.7\times10^{43}}{3.83\times10^{26}}=2.3\times10^{17}$ s $\approx7\times10^9$ y — the Sun is middle-aged, and the arithmetic says so.

**Checks.** (i) Mass loss per second (4.3e9 kg/s) times lifetime returns the burned mass. (ii) The first weak step's slowness, not the fuel, sets the pace.

</details>

### OL12 — What limits the size of a nucleus?

Balance the Coulomb term's growth against the surface term's to estimate the largest Z for a barrier to survive, and connect to the fissility and the periodic table's end.

<details><summary>Solution</summary>

**Method.** The fission barrier vanishes when the Coulomb energy change under deformation exceeds twice the surface change; in the liquid drop this occurs near $\frac{Z^2}{A}\approx50$. With $A\approx2.5Z$: $Z\approx125$. Shell corrections prop up the superactinides a little beyond the drop's prediction — the "island of stability" is shell physics delaying the Coulomb verdict. Bismuth (83) is merely the last *fully* stable element; the drop says no nucleus survives much past Z ~ 100-120, and the table agrees.

**Checks.** (i) Known superheavies (Z up to 118) live milliseconds to seconds, as a thin barrier demands. (ii) The trend matches the alpha-decay dominance beyond bismuth.

</details>

### 10.2 Limits and failure of the model

The liquid-drop picture dents at magic numbers (shell model takes over); the Geiger-Nuttall estimate carries unknown prefactors; beta-decay rates need the full weak-interaction theory; reactor kinetics needs delayed-neutron fractions and feedback coefficients as engineering inputs; neutrino flavour oscillation modifies the solar flux at Earth (named, not derived). Inside its domain — energetics, systematics, statistical decay — the arithmetic is exact.

## Part 11 · Exam simulation — 36 questions, 200 marks, 180 minutes

Sections: A is 12 multiple-choice at 4 marks, B is 8 short-numerical at 4, C is 6 long-form at 5, D is 10 olympiad-style at 9. Use $931.5$ MeV/u, $R_0=1.2$ fm, C-14 half-life $5730$ y.

#### Section A · Concept MCQ (12 x 4)

### P1 · 4 marks
The binding energy per nucleon of He-4 is nearest:
(a) 1.1 MeV  (b) 3.5 MeV  (c) 7.1 MeV  (d) 8.8 MeV

<details><summary>Answer</summary>

(c). $\Delta m=0.0304$ u, $B=28.3$ MeV, $B/A=7.1$ (E1).

</details>

### P2 · 4 marks
The radius of Au-197 is about:
(a) 3.5 fm  (b) 7.0 fm  (c) 12 fm  (d) 1.2 fm

<details><summary>Answer</summary>

(b). $1.2\times197^{1/3}=7.0$ fm.

</details>

### P3 · 4 marks
The alpha kinetic energy from U-238 (Q = 4.27 MeV) is:
(a) 4.27 MeV  (b) 4.20 MeV  (c) 2.14 MeV  (d) 3.55 MeV

<details><summary>Answer</summary>

(b). $\frac{234}{238}\times4.27=4.20$ MeV (Eq. 3.5).

</details>

### P4 · 4 marks
Th-234 beta-minus decays into:
(a) Pa-234  (b) Ra-234  (c) Th-233  (d) U-238

<details><summary>Answer</summary>

(a). Z rises by one, A unchanged.

</details>

### P5 · 4 marks
After five half-lives, the remaining fraction is:
(a) 1/16  (b) 1/32  (c) 1/64  (d) 1/10

<details><summary>Answer</summary>

(b). $2^{-5}=1/32$.

</details>

### P6 · 4 marks
The Q-value of D plus T giving He-4 plus neutron is:
(a) 3.3 MeV  (b) 17.6 MeV  (c) 26.7 MeV  (d) 200 MeV

<details><summary>Answer</summary>

(b). $\Delta m=0.01888$ u (Q4).

</details>

### P7 · 4 marks
A dated sample shows one quarter of the living C-14 activity. Its age is:
(a) 2865 y  (b) 5730 y  (c) 11460 y  (d) 17190 y

<details><summary>Answer</summary>

(c). Two half-lives.

</details>

### P8 · 4 marks
The mass of 1 curie of Co-60 (T-half 5.27 y) is of order:
(a) 0.9 microgram  (b) 0.9 milligram  (c) 0.9 gram  (d) 9 grams

<details><summary>Answer</summary>

(b). E9 gives $8.8\times10^{-4}$ g.

</details>

### P9 · 4 marks
The moderator in a reactor:
(a) absorbs neutrons  (b) slows neutrons elastically  (c) cools the core  (d) reflects gamma rays

<details><summary>Answer</summary>

(b). Absorption is the control rods' work (Trap 8).

</details>

### P10 · 4 marks
The fissility Z-squared over A of U-235 is:
(a) 18.0  (b) 36.0  (c) 50.0  (d) 92.0

<details><summary>Answer</summary>

(b). $92^2/235=36.0$.

</details>

### P11 · 4 marks
40 000 counts carry a percentage uncertainty of:
(a) 4 %  (b) 2 %  (c) 0.5 %  (d) 0.25 %

<details><summary>Answer</summary>

(c). $100/\sqrt{40000}=0.5\%$.

</details>

### P12 · 4 marks
The Geiger-Nuttall law is steep because:
(a) alpha energies vary  (b) the decay constant depends exponentially on Z over root E  (c) the barrier height varies  (d) daughters recoil

<details><summary>Answer</summary>

(b). The WKB exponent is the amplifier (OL1).

</details>

#### Section B · Short numerical (8 x 4)

### P13 · 4 marks
Find the Q-value of C-14 beta decay from atomic masses 14.003242 u and 14.003074 u.

<details><summary>Answer</summary>

$0.156$ MeV = 156 keV (E4), shared by electron and antineutrino.

</details>

### P14 · 4 marks
I-131 (T-half 8.0 d). Find lambda in per seconds and the activity of one microgram.

<details><summary>Answer</summary>

$\lambda=\frac{0.693}{6.9\times10^5}=1.0\times10^{-6}$ s$^{-1}$; $N=\frac{6.022\times10^{17}}{131}=4.6\times10^{15}$; $A=\lambda N=4.6\times10^9$ Bq $\approx124$ mCi.

</details>

### P15 · 4 marks
Energy released by complete fission of 1 g of U-235, and the coal (2.4e10 J per tonne) equivalent.

<details><summary>Answer</summary>

$8.2\times10^{10}$ J; coal equivalent 3.4 tonnes (E11).

</details>

### P16 · 4 marks
A parent (lambda-1) feeds a daughter with lambda-2 = 3 lambda-1. The late-time activity ratio daughter over parent?

<details><summary>Answer</summary>

Transient equilibrium: $\frac{3}{2}$.

</details>

### P17 · 4 marks
Solar neutrino flux at Earth is 6e14 per m-squared per s. Rate through a 1 cm-squared thumbnail?

<details><summary>Answer</summary>

$6\times10^{10}$ s$^{-1}$ (OL6).

</details>

### P18 · 4 marks
Most stable Z for the isobar A = 64 (use Eq. 4.6)?

<details><summary>Answer</summary>

$Z_0=\frac{64}{2+0.0154\times16.0}=28.5$: nickel-copper region, matching the real stable Ni-64 and Cu-64 neighbours.

</details>

### P19 · 4 marks
A sample counts 800 per minute at t = 0 and 100 per minute at t = 12 h. Half-life?

<details><summary>Answer</summary>

Three halvings in 12 h: $T_{1/2}=4$ h.

</details>

### P20 · 4 marks
Mass the Sun loses per second, and the fraction of an Earth mass per year (Earth mass 6e24 kg)?

<details><summary>Answer</summary>

$4.26\times10^9$ kg/s; per year $1.35\times10^{17}$ kg, i.e. $\sim2\times10^{-8}$ Earth masses.

</details>

#### Section C · Long form (6 x 5)

### P21 · 5 marks
The uranium-238 series ends at Pb-206. (a) Count the alphas and betas. (b) Old radium samples sit in secular equilibrium; a 1 g Ra-226 sample holds Rn-222 (T-half 3.82 d). Estimate the mass of radon present.

<details><summary>Answer</summary>

(a) 8 alphas, 6 betas (Q8). (b) Ra activity $3.66\times10^{10}$ Bq; equilibrium requires $A_{Rn}=A_{Ra}$, so $N_{Rn}=\frac{3.66\times10^{10}}{\ln2/(3.82\times86400)}=1.8\times10^{16}$ atoms; mass $\frac{1.8\times10^{16}}{6.022\times10^{23}}\times222=6.5\times10^{-6}$ g.

</details>

### P22 · 5 marks
For D-T fusion: (a) Q. (b) Barrier at 2 fm. (c) The naive classical temperature. (d) Why the Sun ignites far below it — name the two effects.

<details><summary>Answer</summary>

(a) 17.6 MeV. (b) $\frac{1.44}{2}=0.72$ MeV. (c) $\sim8\times10^9$ K. (d) Quantum tunnelling selects the barrier's thin flank; the Maxwell tail supplies the few fast particles; their overlap (the Gamow window) cuts the required temperature by hundreds.

</details>

### P23 · 5 marks
Carbon dating: (a) derive Eq. (4.5). (b) age for 10 versus 15 dpm/g. (c) why the method ends around 50 000 years.

<details><summary>Answer</summary>

(a) $A=A_0e^{-\lambda t}\Rightarrow t=\frac{1}{\lambda}\ln\frac{A_0}{A}$ with $\lambda=\frac{\ln2}{T_{1/2}}$. (b) 3350 y (E7). (c) after about 9 half-lives the activity is below a percent of living carbon; counting statistics and backgrounds drown the signal.

</details>

### P24 · 5 marks
From Eq. (3.3): (a) derive the valley-floor formula. (b) evaluate Z0 for A = 100. (c) the pairing term's role when U-235 captures a slow neutron.

<details><summary>Answer</summary>

(a) OL4's derivative gives Eq. (3.4). (b) 42.9. (c) the even-even compound U-236 gains about 0.8 MeV of pairing bonus, pushing excitation above the barrier (OL3).

</details>

### P25 · 5 marks
A 3 GW thermal reactor: (a) fissions per second, (b) U-235 consumed per day, (c) cross-check via energy per gram.

<details><summary>Answer</summary>

(a) $\frac{3\times10^9}{200\times1.6\times10^{-13}}=9.4\times10^{19}$ s$^{-1}$. (b) energy per day $2.6\times10^{14}$ J; mass $\frac{2.6\times10^{14}}{8.2\times10^{10}}=3.2$ kg. (c) same route by E11's 8.2e10 J/g — the two bookkeepings agree.

</details>

### P26 · 5 marks
A pure parent sample (lambda-1) breeds a daughter (lambda-2 = 4 lambda-1). (a) Write the daughter's atom-number against time. (b) Time of maximum daughter population. (c) Late-time activity ratio.

<details><summary>Answer</summary>

(a) $N_2=\frac{\lambda_1N_1(0)}{3\lambda_1}(e^{-\lambda_1t}-e^{-4\lambda_1t})$. (b) $t_{\max}=\frac{\ln4}{3\lambda_1}$. (c) $\frac{A_2}{A_1}=\frac{4}{3}$.

</details>

#### Section D · Olympiad style (10 x 9)

### P27 · 9 marks
Geiger-Nuttall from tunnelling. (a) State the empirical form and its WKB origin. (b) From U-238 (4.27 MeV, 4.5e9 y) and Po-212 (8.95 MeV, 3e-7 s), estimate the slope b in log lambda = a minus b over root E. (c) Explain in two lines why a 30 percent argument change moves 24 decades.

<details><summary>Answer</summary>

(a) $\log_{10}\lambda\approx a-\frac{bZ}{\sqrt E}$; the exponent is the integral of momentum across the barrier. (b) $\Delta\log\lambda=\log\frac{0.693/3\times10^{-7}}{0.693/(4.5\times10^9\times3.16\times10^7)}=23.7$; $\Delta(1/\sqrt E)=0.484-0.334=0.150$ MeV$^{-1/2}$; $b\approx158\ \text{MeV}^{1/2}$. (c) $\lambda$ is the exponential of the action; moderate argument motion becomes enormous rate motion — the amplifier is the exponential itself.

</details>

### P28 · 9 marks
Solar core temperature, honestly. (a) Compute the naive roll-over temperature from the 0.72 MeV barrier. (b) Write the Gamow exponent and evaluate it at kT = 1.3 keV with E-G = 490 keV. (c) State the Gamow-window energy and the physical conclusion.

<details><summary>Answer</summary>

(a) $T\sim8\times10^9$ K. (b) $-3(E_G/4kT)^{1/3}=-3(94)^{1/3}\approx-13.6$: survivable, unlike the classical $e^{-550}$. (c) $E_0\approx6$ keV, far above kT, far below the barrier: the Sun burns by tunnelling from the Maxwell tail at $1.5\times10^7$ K (OL2).

</details>

### P29 · 9 marks
Fissility and the odd-even split. (a) Describe the fission barrier as surface-versus-Coulomb under deformation. (b) Compute fissilities of U-235 and U-238. (c) Explain why one fissions with slow neutrons and the other needs fast ones, quantifying the pairing bonus.

<details><summary>Answer</summary>

(a) Deformation adds surface area (cost) and separates protons (gain); the hump is the barrier. (b) 36.0 versus 35.6. (c) U-235 plus a neutron makes even-even U-236, gaining $\approx\frac{12}{\sqrt{236}}\approx0.8$ MeV of pairing: excitation $\sim6.5$ MeV tops the $\sim6$ MeV barrier; U-238's compound U-239 has no bonus, sits below, and needs kinetic help.

</details>

### P30 · 9 marks
The solar neutrino tide. (a) Compute the neutrino flux at Earth from luminosity and the p-p net. (b) The rate through a thumbnail. (c) Why detecting them at all is a miracle of flux times cross-section.

<details><summary>Answer</summary>

(a) $6.4\times10^{14}$ m$^{-2}$s$^{-1}$ (OL6). (b) $\sim6\times10^{10}$ s$^{-1}$. (c) The weak cross-section at MeV energies is $\sim10^{-47}$ m$^2$: per second per atom the capture probability is $\sim10^{-32}$; only a kiloton-scale detector plus the tide's enormity buys a handful of events a day.

</details>

### P31 · 9 marks
The Sun's mass audit. (a) Verify 26.7 MeV from atomic masses including annihilation. (b) With 7 percent of the Sun's hydrogen burnable, estimate the main-sequence lifetime. (c) Cross-check with the mass-loss rate times the lifetime.

<details><summary>Answer</summary>

(a) 25.7 MeV from masses plus 1.02 MeV annihilation: 26.7 (Q25). (b) $\frac{0.07\times0.7\times1.99\times10^{30}\times0.007c^2}{L}\approx2.3\times10^{17}$ s $\approx7\times10^9$ y. (c) $4.26\times10^9\times2.3\times10^{17}=9.8\times10^{26}$ kg $\approx0.007$ of the burned hydrogen mass — energy per mass consistent.

</details>

### P32 · 9 marks
Isochron dating. (a) Derive the straight-line relation for Sr-87 versus Rb-87 normalised to Sr-86. (b) From slope 0.05 and lambda = 1.42e-11 per year find the age. (c) What does a scattered, off-line data set accuse?

<details><summary>Answer</summary>

(a) OL9's relation, slope $e^{\lambda t}-1$. (b) $t=\frac{\ln1.05}{1.42\times10^{-11}}=3.4\times10^9$ y. (c) Metamorphism or leaching after formation: the clock was reset or disturbed.

</details>

### P33 · 9 marks
Counting-statistics design. (a) Derive sigma = sqrt N. (b) At 100 counts per minute, how long for 1 percent precision? (c) With background 25 per minute, does the time grow, shrink, or stay? Estimate.

<details><summary>Answer</summary>

(a) Poisson variance equals the mean. (b) $N=10^4$ counts: 100 min. (c) Grows: signal net rate is unchanged but total variance includes background; roughly a factor 1.3 in counts needed, so about 130 min.

</details>

### P34 · 9 marks
The periodic table's end. (a) Use fissility's vanishing barrier at Z-squared over A about 50 with A about 2.5 Z to estimate the largest Z. (b) Why do superheavy islands live longer than the drop predicts? (c) Reconcile with bismuth being the last stable element.

<details><summary>Answer</summary>

(a) $Z\approx120$. (b) Shell closures add binding pockets against the smooth drop trend. (c) Full stability requires no open decay channel; beyond bismuth alpha and beta channels are all energetically open, however high the barriers.

</details>

### P35 · 9 marks
Transient equilibrium, start to finish. Solve the daughter equation from a pure parent; find the equilibrium ratio; show the secular limit; find the time of maximum daughter activity for lambda-2 = 3 lambda-1.

<details><summary>Answer</summary>

OL5: $N_2(t)=\frac{\lambda_1N_1(0)}{\lambda_2-\lambda_1}(e^{-\lambda_1t}-e^{-\lambda_2t})$; ratio $\frac{\lambda_2}{\lambda_2-\lambda_1}\to\frac32$ here; secular limit 1; $t_{\max}=\frac{\ln3}{2\lambda_1}$.

</details>

### P36 · 9 marks
Reactor economy and waste. (a) Derive the 1.05 kg per day per GW thermal figure. (b) A 30-year isotope is stored 300 years: the surviving fraction, and the engineering meaning. (c) A 1 GW electric plant at 33 percent efficiency: kilograms of U-235 per day.

<details><summary>Answer</summary>

(a) OL7(a): 8.6e13 J per day over 8.2e10 J per gram. (b) $2^{-10}\approx10^{-3}$: three orders of activity removed — the ten-half-life shorthand. (c) 3.2 kg per day (P25).

</details>

## Part 12 · Marking scheme and rubric

Section A (4 each): 4 marks for the correct option with a one-line reason; 2 for a right answer without reasoning.

Section B (4 each): 2 for the setup (formula plus data substituted), 2 for the number with units; a missing unit caps the answer at 2.

Section C (5 each): 1 for the diagram or mass table, 2 for the derivation or method, 2 for the numerical result with stated assumptions; the cross-check line earns the fifth when the method was otherwise compressed.

Section D (9 each): typically three sub-parts at 3 marks. Derivations: 1 for stating the governing expression, 1 for the algebra or integral, 1 for the limit check. Estimates: 1 for the model choice, 1 for the arithmetic, 1 for the honesty line (what the model neglects). Full marks require the stated checks; an answer that contradicts the binding-energy curve loses its numerical marks even with correct algebra.

General: exponential arguments must show the ln 2; beta Q-values must show the electron rule; equilibrium answers must name the regime. These three omissions are the chapter's signature penalties.

## Part 13 · Links across the course

- PART 23 (photoelectric effect): the same electron accounting style recurs here; the Poisson counting logic of photoelectron statistics matures into the sqrt-N discipline of OL8; gamma rays ionise matter the way light ejects electrons, one quantum at a time.
- PART 24 (atomic structure): muonic atom levels are the size-measuring instrument behind Eq. (3.1); nuclear level diagrams are the atom's ladder translated down a factor of a million in scale; Bohr's radius-versus-nucleus-size comparison is where this chapter's femtometre world begins.
- PART 25 (X-rays): K-shell electron capture leaves the very vacancies whose filling makes characteristic X-rays; gamma lines and X-ray lines are the same de-excitation story in two different buildings; Moseley's Z is the ordering principle of the valley of stability's proton axis.
- Forward: the next module inherits the energy bookkeeping (mass-energy, Q-values) and the statistics discipline; the reactor's neutron economy will reappear wherever slow neutrons do the probing.

## Part 14 · Sources and review checklist

Primary: Cengage, Optics and Modern Physics, chapter 5 (pp. 5.1-5.39) — structure and radioactivity as above, solved examples and exercises at the chapter's end. Sweep notes: SEMF, Geiger-Nuttall and Gamow theory, counting statistics, the Lawson criterion, the solar neutrino flux and detector themes were added beyond the printed table of contents, as flagged in the coverage map.

Review checklist before the exam:
1. The six boxed results of Part 4 reproduce from memory with units.
2. The electron rule survives a surprise beta-plus question.
3. The halving ladder and the log-linear fit are both in hand.
4. One equilibrium derivation (OL5) is writable start to finish.
5. The Sun's three numbers (4.3e9 kg/s, 6e14 neutrinos, 1.5e7 K) each carry their one-line story.
6. The fission bookkeeping (200 MeV, 8.2e10 J/g, 3 kg per GWe-day) is instant.
7. Every trap of Part 8 has its one-line reply.
