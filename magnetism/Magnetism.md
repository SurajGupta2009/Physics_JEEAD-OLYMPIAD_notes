---
title: Magnetism
part: 16
plan_parts: [16, 17, 18, 19]
slug: magnetism
order: 20
block: electricity-magnetism
status: in-progress
stage: 1
source: no Cengage volume in this repository for magnetism; the coverage map is built from the standard JEE Advanced headings listed in plan.md PART 16–19 and the shipped current-electricity and electromagnetic-waves notes
aliases: [magnetism, magnetic field, lorentz force, biot-savart law, ampere's law, cyclotron, hall effect, magnetic dipole, magnetism and matter, earth's magnetism]
tags: [jee-advanced, olympiad, electricity-magnetism, magnetism]
---

# Magnetism — from the Lorentz force to the Earth's field

> [!abstract] How to use this chapter
> One module for the whole of magnetostatics and magnetic matter, in three passes. **Pass 1: Parts 0–3** — the theory in teaching order: the force on a moving charge first (the *effect*), then everything a charge does in a field (circles, helices, selectors, cyclotrons, mirrors, the Hall effect, drifts), then the *cause* — currents as sources through Biot–Savart and Ampère — then forces and torques on currents, the magnetic dipole, matter's three responses, and the Earth as a magnet. **Pass 2: Parts 4–9** — the validity ledger, worked exemplars, the archetype table with practice, the toolkit, the traps, the playbook. **Pass 3: Parts 10–14** — the Olympiad layer (magnetism as relativity, the cycloid two ways, magnetic pressure and the pinch, Helmholtz coils, the magnetised sphere, Fermi acceleration, the Curie-temperature estimate), the 200-mark paper, the marking scheme, the formula sheet and the checkpoint. Every number is recomputed; every boxed result carries its condition of validity.

> [!warning] Stage 1 of 3 — what is on the page today
> The module merges plan.md PARTs 16, 17, 18 and 19 into one chapter, written in three turns. **This stage ships Parts 0–3 in full** — the complete theory from the Lorentz force to the Earth's dipole. Parts 4–14 carry a one-paragraph statement of what they will contain and are written in stages 2 and 3; the local gate (`tools/check.py`) enforces the reading-mode, media and maths rules now and the question families and the paper when their stage arrives. Nothing in Parts 0–3 will be rewritten later: later stages *add* blocks.

## Part 0 · Orientation

### 0.1 What you will be able to do

After this chapter you can: write the Lorentz force and get its direction from $\mathbf v\times\mathbf B$ with the sign of the charge applied afterwards, and say why a magnetic field never changes a particle's speed; derive the radius and the period of a charge's circle and explain why the period does not depend on the speed — then build the cyclotron, the mass spectrometer and the velocity selector on that one fact; run the three-region method for a particle crossing field boundaries; derive the pitch of a helix, the magnetic-mirror invariant and the loss cone; derive the Hall voltage and read a carrier's sign from it; derive the $\mathbf E\times\mathbf B$ drift and the cycloid; reconstruct Thomson's $e/m$; write Biot–Savart and integrate it for a finite wire, a loop on its axis, an arc, a solenoid and a toroid, with every limit checked; motivate and state Ampère's law with its sign convention, and use it for the wire, the thick wire, the coaxial cable, the sheet, the solenoid, the toroid and the overlapping cylinders; decide between Ampère and Biot–Savart in ten seconds; derive $\mathbf F=I\mathbf L\times\mathbf B$ from the force on carriers, the chord theorem, the torque $\boldsymbol\mu\times\mathbf B$ and the energy $-\boldsymbol\mu\cdot\mathbf B$, the force between parallel currents and the magnetic pressure $B^2/2\mu_0$; explain how a motor does work when the magnetic force does none; derive the gyromagnetic ratio of a rotating charge; describe a magnet as a solenoid of bound currents, relate $\mathbf B$, $\mathbf H$ and $\mathbf M$, explain dia-, para- and ferromagnetism mechanically, read a hysteresis loop as an energy diagram, and derive the core's amplification; and resolve the Earth's field into its three components at any place. The Olympiad layer (Part 10, stage 3) adds the derivation of magnetism from electrostatics and relativity, the pinch, Helmholtz coils, the magnetised sphere and Fermi acceleration.

### 0.2 The one idea

A magnetic field acts only on *moving* charge, always at right angles to the motion, so it steers without ever speeding up or slowing down; the field itself is made by moving charge, and Ampère's loop law does for currents what Gauss's law did for charges. Every formula in the chapter is one of those two sentences with geometry attached.

### 0.3 Prerequisite self-check

1. *$\mathbf a\times\mathbf b$ for $\mathbf a=\hat{\mathbf x}$, $\mathbf b=\hat{\mathbf y}$; and $\hat{\mathbf y}\times\hat{\mathbf x}$?* — $\hat{\mathbf z}$ and $-\hat{\mathbf z}$: anticommutative, right-handed ([[Vectors|PART 2]]).
2. *A particle moves in a circle of radius $r$ at speed $v$; what force acts and where does it point?* — $mv^2/r$, towards the centre ([[Motion-in-two-dimensions|PART 4]]).
3. *Field of an infinite line charge $\lambda$ at distance $r$; field on the axis of a charged ring?* — $\lambda/2\pi\varepsilon_0r$; $kQx/(x^2+R^2)^{3/2}$ ([[Electrostatics|electrostatics]] §3.5, §3.4 — the magnetic twins are §3.14 and §3.15 here).
4. *Torque and energy of an electric dipole in a uniform field?* — $\mathbf p\times\mathbf E$, $-\mathbf p\cdot\mathbf E$ (electrostatics §3.10; the magnetic versions are §3.24).
5. *Small oscillations: $I\ddot\theta=-\kappa\theta$ gives what period?* — $2\pi\sqrt{I/\kappa}$ ([[Simple-harmonic-motion|PART 10]]).
6. *Current $I$ in terms of carrier density $n$, charge $q$, drift speed $v_d$ and area $A$?* — $I=nqv_dA$ ([[Current-electricity|current electricity]]).
7. *Relative population of two levels separated by $\Delta E$ at temperature $T$?* — $e^{-\Delta E/k_BT}$ ([[Thermodynamics|thermodynamics]]).
8. *Angular momentum of a ring of mass $m$, radius $R$, angular speed $\omega$?* — $mR^2\omega$ ([[Rotational-mechanics|PART 8]]).

### 0.4 Numbers to keep

| quantity | value | why it matters |
|---|---|---|
| $\mu_0$ | $4\pi\times10^{-7}$ T m A$^{-1}$ (exactly, to $10^{-9}$) | $\mu_0/4\pi=10^{-7}$ is the Biot–Savart constant; $\mu_0/2\pi=2\times10^{-7}$ the wire's |
| $\mu_0\varepsilon_0$ | $1/c^2$ | magnetism and electricity are one theory (§2.5) |
| Earth's field | $25$–$65\ \mu$T; $\approx45\ \mu$T at mid-latitudes | the scale every laboratory field is compared with |
| field of $10$ A at $1$ cm | $0.2$ mT $=4\times$ Earth | why a compass near a wire swings (Oersted) |
| fridge magnet / MRI / strongest steady | $5$ mT / $1.5$–$3$ T / $45$ T | the tesla is a large unit |
| iron's saturation | $B_s\approx2.1$ T | the ceiling on every iron-core design |
| $e/m_e$ | $1.76\times10^{11}$ C kg$^{-1}$ | electron cyclotron frequency $28$ GHz per tesla |
| $e/m_p$ | $9.58\times10^{7}$ C kg$^{-1}$ | proton cyclotron frequency $15.2$ MHz per tesla |
| Bohr magneton $\mu_B=e\hbar/2m_e$ | $9.27\times10^{-24}$ A m$^2$ | the atomic moment; $\mu_BB/k_BT=2.2\times10^{-3}$ at $1$ T, $300$ K |
| magnetic pressure $B^2/2\mu_0$ at $1$ T | $4.0\times10^5$ Pa $\approx4$ atm | why big magnets need steel and why a 1 T pole lifts $40$ kg per $10$ cm$^2$ |
| $p\,[\text{MeV}/c]=300\,B\,[\text{T}]\,r\,[\text{m}]$ | the track-reading rule | momentum from a curved track in a chamber |
| Earth's dipole moment | $8\times10^{22}$ A m$^2$ | from $B\approx30\ \mu$T at the equator and $R_\oplus$ |
| $\chi$: water, copper, aluminium, iron | $-9\times10^{-6}$, $-1\times10^{-5}$, $+2\times10^{-5}$, $\sim10^3$–$10^5$ | the three classes of matter, five orders apart |
| Curie temperature of iron | $1043$ K | above it, iron is a paramagnet |

### 0.5 How to use the chapter

Read Part 3 straight through once, doing the worked examples with pencil (there are ten of them inside the theory; the exemplars E1–E20 of stage 2 add the exam craft). Every derivation ends with a check; do not skip it, because the checks are where the traps of Part 8 are first defused. Then come back to §3.3 and §3.13 and make sure you can say why the cyclotron period is independent of speed and why Biot–Savart has a cross product in it — the chapter hangs on those two.

### 0.6 Coverage map

There is no Cengage magnetism volume in this repository (plan.md Block B). The floor is therefore the standard JEE Advanced syllabus as itemised in plan.md PART 16–19 (headings as printed there), plus what the shipped [[Current-electricity|current-electricity]] and [[Electromagnetic-waves|electromagnetic-waves]] notes assume of this chapter. Status vocabulary: **derived**, **stated + used**, **extended beyond floor**, and — for exam craft — **archetypes (Parts 5–6, stage 2)**.

**PART 16 · Magnetic field, Biot–Savart and the Lorentz force**

| syllabus heading | what it establishes | where it lives here | status |
|---|---|---|---|
| The observation (Oersted; moving charge; no monopoles) | magnetism is a moving-charge phenomenon | §3.1 | derived (argument), stated (no monopoles, proved in §3.22) |
| The Lorentz force | $\mathbf F=q\mathbf v\times\mathbf B$, three properties, the tesla | §3.2 | derived (properties) |
| Circular and helical motion | $r=mv/qB$, $\omega=qB/m$ independent of $v$, pitch | §3.3 | derived |
| Combined fields | parallel and crossed fields; $v=E/B$ | §3.4, §3.10 | derived |
| Biot–Savart | the law, its status, direction, dimensions | §3.13 | stated + used; checked against the moving charge |
| The straight wire | finite by angles; semi-infinite; infinite | §3.14 | derived |
| The loop and the arc | centre, axis, arc, compound loops | §3.15 | derived |
| Solenoid and toroid | stacked loops; $\mu_0nI$; edge half; toroid | §3.16, §3.19 | derived twice |
| The magnetic moment | $\boldsymbol\mu=I\mathbf A$; dipole fields; the analogy table | §3.17 | derived |
| Force on a current | $I\mathbf L\times\mathbf B$ from carriers; chord theorem; closed loop | §3.23 | derived |
| Torque on a loop | $\boldsymbol\mu\times\mathbf B$ from side forces; $-\boldsymbol\mu\cdot\mathbf B$; galvanometer | §3.24 | derived |
| Forces between currents | $\mu_0I_1I_2/2\pi d$; the ampere; third law and field momentum | §3.25 | derived |
| Where the energy comes from | the motor puzzle resolved | §3.27 | derived (argument) |

**PART 17 · Ampère's law, currents and magnetic dipoles**

| syllabus heading | what it establishes | where it lives here | status |
|---|---|---|---|
| Why a loop law should exist | circulation around a wire | §3.18 | derived |
| Ampère's circuital law | statement, sign convention with a worked instance, symmetry requirement | §3.18 | stated + used |
| The applications | wire, thick wire, coax, sheet, two sheets, solenoid, toroid, cylindrical shell | §3.19 | derived (eight) |
| The overlap trick | uniform field in the lens | §3.20 | derived |
| Ampère vs Biot–Savart | decision table; two dual solutions | §3.21 | derived |
| Forces on currents revisited | parallel wires from Ampère; rails; magnetic pressure at a solenoid's end | §3.25, §3.26 | derived |
| The magnetic dipole as the fundamental object | magnet–solenoid equivalence; measuring $\mu$ by oscillation | §3.24, §3.29 | derived |
| Boundary conditions and field energy | tangential jump $\mu_0K$; $B^2/2\mu_0$ announced | §3.26 | stated + used (energy derived in PART 21) |
| No monopoles | $\nabla\cdot\mathbf B=0$; closed lines; the cut magnet | §3.22 | derived (consequences) |

**PART 18 · Cyclotron, velocity selector and the Hall effect**

| syllabus heading | what it establishes | where it lives here | status |
|---|---|---|---|
| The three-region method | the protocol for field boundaries | §3.5 | derived |
| Velocity selector and mass spectrometer | $v=E/B$; isotope separation; resolution | §3.4, §3.6 | derived |
| The cyclotron | resonance, $E_{\max}$, turns, limits | §3.7 | derived |
| Helical motion and magnetic mirrors | pitch; $\mu=mv_\perp^2/2B$; loss cone; Van Allen | §3.8 | derived |
| The Hall effect | $V_H=IB/nqt$; carrier sign; $n$, mobility; Cu vs semiconductor | §3.9 | derived |
| Crossed fields and drifts | $\mathbf E\times\mathbf B$ two ways; cycloid; gradient and curvature drifts | §3.10 | derived (gradient); stated (curvature) |
| Measured $q/m$: the electron | Thomson's tube | §3.11 | derived |
| Where it matters | synchrotron, confinement, aurora, mass spectrometry | §3.12 | stated + used |
| The particle zoo preview | reading a cloud-chamber track | §3.12 | derived (the $300Br$ rule) |

**PART 19 · Magnetism and matter, Earth's magnetism**

| syllabus heading | what it establishes | where it lives here | status |
|---|---|---|---|
| The magnet as a dipole | moment; pole picture and its failure; solenoid equivalence | §3.29 | derived |
| Magnetisation | $\mathbf M$; bound currents $K_b=M$ (slab derivation) | §3.30 | derived |
| The field inside matter | $\mathbf B=\mu_0(\mathbf H+\mathbf M)$; $\chi$, $\mu_r$; demagnetising caveat | §3.31 | derived |
| Diamagnetism | induced-moment mechanism; weak negative $\chi$ | §3.32 | derived (Larmor estimate) |
| Paramagnetism | alignment vs disorder; Curie law; saturation | §3.33 | derived (two-level Boltzmann) |
| Ferromagnetism | domains; hysteresis as energy; soft vs hard; Curie temperature | §3.34 | derived (loop area) |
| Materials in circuits | core amplification; transformer cores; shielding | §3.35 | derived |
| Forces on materials | induced-dipole attraction; diamagnetic repulsion; lift estimate | §3.36 | derived |
| Earth's magnetism | tilted dipole; declination, dip, components | §3.37 | derived |
| Magnetism in nature | reversals, dynamo, Curie temperature, navigation | §3.38 | stated + used |

### 0.7 Plan-part map

| plan.md part | this chapter |
|---|---|
| PART 16 · Magnetic field, Biot–Savart, Lorentz force | §3.1–§3.4, §3.13–§3.17, §3.23–§3.25, §3.27–§3.28 |
| PART 17 · Ampère's law, currents, dipoles | §3.18–§3.22, §3.25–§3.26 |
| PART 18 · Cyclotron, selector, Hall effect | §3.5–§3.12 |
| PART 19 · Magnetism and matter, Earth | §3.29–§3.38 |

Induction, inductance and alternating current (PART 20–22) are the next module: everything there begins with the sentence "now let the flux change", which this chapter never says.

## Part 1 · Intuition first

A compass needle beside a wire swings the moment the current is switched on, and swings back when it stops (Oersted, 1820). Nothing electrostatic does that: a static charge near a compass does nothing at all. Whatever moves the needle is made by *moving* charge and, as it turns out, acts only *on* moving charge. That is the whole subject in a sentence, and it explains the strangeness that follows.

The force is sideways. Fire an electron across a magnetic field and it is pushed neither along the field nor along its own motion but at right angles to both — so it curves. Since the push is always perpendicular to the velocity, it does no work: the speed never changes, only the direction. A charge in a uniform field therefore runs in a circle, and the time round the circle turns out not to depend on how fast it goes: a faster particle runs a bigger circle in the same time. That single fact is a clock that ticks at a rate set only by the field and by the charge-to-mass ratio, and on it are built the cyclotron, the mass spectrometer, the magnetic-resonance scanner and the radio emission of electrons spiralling in space.

The sources are currents. Every magnetic field in the laboratory comes from moving charge — a current in a wire, electrons circling in atoms, the spin of the electron itself. A straight wire's field circles the wire; a loop's field threads the loop; a long coil's field is straight and uniform inside and almost nothing outside; and from far away every loop, coil and magnet looks the same — a *dipole*, the magnetic twin of the electric dipole of the previous chapter, with the same $1/r^3$ field and the same torque and energy in an external field. There is no magnetic "charge" for the lines to start or end on: they always close.

Matter answers in three ways. Everything is slightly *diamagnetic*: an applied field disturbs the electrons' orbits so as to oppose it (a weak repulsion — a frog can be levitated). Atoms with a permanent moment are *paramagnetic*: the field aligns them a little against thermal jostling (a weak attraction that fades as $1/T$). And in iron, cobalt and nickel a quantum effect locks neighbouring moments parallel in whole domains, so that a modest field organises an enormous internal one — *ferromagnetism*, the reason magnets exist, and the reason a coil with an iron core is a thousand times stronger than the same coil without. The Earth itself is a magnet, a tilted dipole driven by currents in its liquid core, whose field a compass reads and whose direction is written into rocks as they cool.

> [!tip] FIGURE F16.1 · The module in one picture
> *Why:* a first map of the four plan parts merged here, so that every later section is a known place on it.
> *Data:* the four branches of Part 3 — force and motion, currents as sources, forces and dipoles, matter and Earth — with the leaf topics of the coverage map.

```mermaid
mindmap
  root((Magnetism))
    Force on moving charge
      q v cross B, no work
      circles: r = mv/qB, omega = qB/m
      helix, mirrors, adiabatic invariant
      selector, spectrometer, cyclotron
      Hall effect, drifts, cycloid, e/m
    Currents make fields
      Biot-Savart: wire, loop, arc
      solenoid and toroid
      Ampere's loop law and its symmetries
      overlap trick, decision table
      no monopoles
    Forces and dipoles
      I L cross B, chord theorem
      torque mu cross B, energy
      parallel wires, the ampere
      magnetic pressure B^2 / 2 mu0
      gyromagnetic ratio
    Matter and Earth
      bound currents, B H M
      dia, para, ferro
      hysteresis, cores, lifting
      Earth's tilted dipole, dip and declination
    Olympiad layer
      magnetism from relativity
      pinch, Helmholtz, magnetised sphere
      Fermi acceleration, Curie estimate
```

> *Read:* effect before cause. The first branch never asks where the field comes from; the second answers it; the third and fourth put the two together in wires, magnets, matter and the planet.

## Part 2 · Definitions and bookkeeping

### 2.1 Symbols and units

| symbol | meaning | unit | convention fixed here |
|---|---|---|---|
| $\mathbf B$ | magnetic field (flux density) | tesla, T $=$ N A$^{-1}$ m$^{-1}$ $=$ N s C$^{-1}$ m$^{-1}$ | defined by the force on a moving charge, (3.1); $1$ T $=10^4$ gauss |
| $\mathbf v$, $q$, $m$ | velocity, charge (signed), mass of a particle | m s$^{-1}$, C, kg | $q$ carries its sign into every formula; the electron is $q=-e$ |
| $r$, $\omega_c$, $T$ | orbit radius, cyclotron angular frequency, period | m, rad s$^{-1}$, s | $\omega_c=\lvert q\rvert B/m$, $T=2\pi m/\lvert q\rvert B$ |
| $I$, $d\mathbf l$ | current, an element of the wire *in the direction of the current* | A, m | $I\,d\mathbf l$ is the source element; for a negative carrier the current still points along $I\,d\mathbf l$ |
| $\mathbf J$, $\mathbf K$ | volume current density, surface current density (current per unit *width*) | A m$^{-2}$, A m$^{-1}$ | $I=\int\mathbf J\cdot d\mathbf A=\int K\,dw$; a solenoid is $K=nI$ |
| $n$ | turns per unit length (solenoid) *or* carrier density (Hall effect) | m$^{-1}$ *or* m$^{-3}$ | the context names which; never both in one formula |
| $N$ | number of turns | — | a coil's moment and enclosed current both carry $N$ |
| $\boldsymbol\mu$ | magnetic dipole moment | A m$^2$ $=$ J T$^{-1}$ | $\boldsymbol\mu=NI\mathbf A$, $\mathbf A$ by the current's right-hand rule |
| $\mathbf M$, $\mathbf H$ | magnetisation (moment per volume), auxiliary field | A m$^{-1}$, A m$^{-1}$ | $\mathbf B=\mu_0(\mathbf H+\mathbf M)$; $\mathbf H$ is what a free current makes, $\mathbf M$ what matter adds |
| $\chi$, $\mu_r$, $\mu$ | susceptibility, relative permeability, permeability | —, —, T m A$^{-1}$ | $\mathbf M=\chi\mathbf H$, $\mu_r=1+\chi$, $\mu=\mu_r\mu_0$; linear media only |
| $\Phi_B$ | magnetic flux | weber, Wb $=$ T m$^2$ | $\int\mathbf B\cdot d\mathbf A$; through any *closed* surface, zero |
| $\mu_0$ | permeability of free space | $4\pi\times10^{-7}$ T m A$^{-1}$ | $\mu_0/4\pi=10^{-7}$ exactly enough for every problem |
| $\delta$, $\theta_{\text{dip}}$, $B_H$, $B_V$ | declination, dip (inclination), horizontal and vertical components of the Earth's field | °, °, T, T | $B_H=B\cos\theta_{\text{dip}}$, $B_V=B\sin\theta_{\text{dip}}$; dip positive when the north-seeking end points down |

### 2.2 Right-hand rules, fixed once

Three rules, one hand, and they are all the same cross product.

1. **Force on a charge:** $\mathbf F=q\,\mathbf v\times\mathbf B$. Point the fingers of the right hand along $\mathbf v$, curl them towards $\mathbf B$; the thumb gives $\mathbf v\times\mathbf B$. *Then* apply the sign of $q$: for an electron the force is opposite to the thumb. Never use the left hand for negative charges — compute the cross product, then flip.
2. **Field of a current (grip rule):** thumb along the current, fingers curl in the direction of $\mathbf B$ around it. For a loop: fingers along the current, thumb gives the field through the loop's centre — which is also the direction of the loop's moment $\boldsymbol\mu$.
3. **Ampère's loop:** choose a direction round the loop; curl the fingers that way; the thumb gives the positive direction for currents threading it. Currents along the thumb count $+$, against it $-$.

Cross-product bookkeeping in components, when the hand fails: $\hat{\mathbf x}\times\hat{\mathbf y}=\hat{\mathbf z}$, $\hat{\mathbf y}\times\hat{\mathbf z}=\hat{\mathbf x}$, $\hat{\mathbf z}\times\hat{\mathbf x}=\hat{\mathbf y}$, and reversing any pair reverses the sign. In diagrams, $\odot$ is a field (or current) *out of* the page, $\otimes$ *into* it — the tip and the tail of an arrow.

> [!danger] Trap — the left hand
> "For a negative charge use the left hand." It works and it is how mistakes are made, because the next problem has a positive ion and the hand has not changed back. One rule, one hand: $\mathbf v\times\mathbf B$ first, the sign of $q$ second.

### 2.3 Sign and direction conventions

* $\mathbf B$ points the way a compass's *north-seeking* end points. Field lines leave a magnet's north pole and enter its south pole *outside* the magnet, and run south-to-north *inside* it — so they close.
* A current loop's moment $\boldsymbol\mu$ is along the thumb when the fingers follow the current; the loop's own field at its centre is along $\boldsymbol\mu$. Seen from the side $\boldsymbol\mu$ points to, the current runs anticlockwise.
* Ampère's law: the sign of $I_{\text{enc}}$ follows rule 3 of §2.2; a wrong choice of loop direction flips the signs of *both* sides, so the physics survives but a copied sign does not.
* The Hall voltage's polarity is defined by which face the *carriers* pile up on; the sign of the carriers is what the measurement determines (§3.9).
* Dip is positive when the north-seeking pole dips *below* the horizontal — the northern hemisphere. Declination is measured east or west of geographic north and is stated with its direction.

### 2.4 The model and its assumptions

*Magnetostatics:* all currents are steady, so all fields are constant in time and no electric field is induced (PART 20 removes this). *Point particles* with non-relativistic speeds ($v\ll c$) unless stated; the cyclotron's limit (§3.7) and the synchrotron are where relativity enters, and Part 10 shows that magnetism *is* a relativistic effect. *Vacuum* between sources, except in §3.29–§3.36, where matter is linear ($\mathbf M\propto\mathbf H$) unless it is a ferromagnet, in which case nothing is linear and the hysteresis loop is the model. *Thin wires* are lines of current; *solenoids* are long compared with their radius unless the finite formula is used; *the Earth's field* is a dipole plus stated local corrections. What is *not* in the model: induced EMF (PART 20), the energy stored in a magnetic field except as an announced result (PART 21), radiation (electromagnetic waves), the quantum origin of spin and exchange (named where they enter, derived nowhere in this course).

### 2.5 The constants are not independent

$\mu_0=4\pi\times10^{-7}$ T m A$^{-1}$ and $\varepsilon_0=8.854\times10^{-12}$ F m$^{-1}$ satisfy $\mu_0\varepsilon_0=1/c^2$ ($c=2.998\times10^8$ m s$^{-1}$): the magnetic constant is the electric constant divided by the square of the speed of light. Stated here, it is a coincidence; in Part 10 it is derived — a moving charge's magnetic force on another is its electric force times $v_1v_2/c^2$, which is why laboratory magnetic forces are tiny compared with electric ones between the *same* charges, and why they dominate in practice only because wires are neutral and their electric forces cancel while their currents' magnetic forces do not.

> [!info] Why the tesla is so large
> $1$ T exerts $1$ N on $1$ C moving at $1$ m s$^{-1}$; since a coulomb is enormous, so is a tesla. The Earth manages $5\times10^{-5}$ T, a strong permanent magnet $1$ T at its face, an MRI $1.5$–$3$ T, the largest steady laboratory fields $45$ T, and a neutron star $10^8$ T. The old unit, the gauss ($10^{-4}$ T), is the one at which everyday numbers come out human-sized: the Earth is half a gauss.

### 2.6 Bookkeeping for sources

A source is described by whichever density matches its dimensionality, and every integral in Part 3 is $\int(\ldots)\,I\,d\mathbf l$ with the substitution the geometry dictates:

$$
I\,d\mathbf l\ \longleftrightarrow\ \mathbf K\,dA\ \longleftrightarrow\ \mathbf J\,dV\ \longleftrightarrow\ q\mathbf v\ \ (\text{a single moving charge}). \qquad (2.1)
$$

A solenoid of $n$ turns per metre carrying $I$ is a cylindrical sheet with $K=nI$; a rotating charged ring of charge $Q$ and angular speed $\omega$ is a loop with $I=Q\omega/2\pi$; a rotating charged disc is a stack of such rings. The current threading a loop, for Ampère's law, is $\int\mathbf J\cdot d\mathbf A$ over any surface bounded by the loop — $NI$ for a coil that passes through it $N$ times.

## Part 3 · Core derivations

The order is the teaching order, effect before cause: what a magnetic field *does* to a moving charge (§3.1–§3.4) and everything built on that (§3.5–§3.12), then where the field *comes from* — Biot–Savart (§3.13–§3.17) and Ampère (§3.18–§3.22) — then the two put together in forces on currents and dipoles (§3.23–§3.28), and finally matter and the Earth (§3.29–§3.38). Every result is derived once here; the electric twins of the previous chapter are cited at the point of correspondence, because half of this chapter is that chapter with a cross product added.

### 3.1 The observation: magnetism is moving charge acting on moving charge

A compass needle is deflected by a nearby current and returns when the current stops; two parallel wires carrying currents attract or repel; a magnet swings a beam of electrons in a television tube. A charged pith ball at rest beside the same wire does nothing and feels nothing. Everything magnetic in these experiments involves charge *in motion* on both sides: the source is a current (or the orbital and spin motion of electrons inside a magnet), and the thing acted on is a moving charge (or a current, or those same electrons). The field that mediates this is called $\mathbf B$; §3.2 defines it by its effect, and §3.13 by its cause.

What decides whether a force is magnetic: **does it depend on the velocity of the thing it acts on?** A stationary charge in a purely magnetic field feels nothing, however strong the field; the same charge moving feels a force that grows with its speed and reverses when the velocity reverses. Electric forces do neither. A charged particle at rest in the Earth's field or between the poles of a magnet stays at rest — the first concept check of this chapter, and the one most often failed.

There are no magnetic charges. Every attempt to isolate a single magnetic pole — cutting a magnet, looking in cosmic rays, searching rocks from the Moon — has produced two-poled magnets or nothing. The statement "no monopoles" is a law of nature on the same footing as Gauss's law, and it forbids something specific: magnetic field lines can neither begin nor end, so they always close on themselves (or run to infinity); the magnetic flux through any *closed* surface is zero. §3.22 draws out the consequences.

> [!abstract] DIAGRAM D16.1 · Oersted's experiment
> *Show:* a straight wire above a compass, needle aligned north–south with no current; the same with current flowing, the needle swung across the wire; a third panel with the current reversed and the needle swung the other way; concentric circles of $\mathbf B$ drawn around the wire with the grip rule's hand.
> *Search:* "oersted experiment compass needle deflection current carrying wire diagram"

> [!abstract] Numbers to keep — how strong is a wire's field
> A wire carrying $10$ A produces, $1$ cm away, $B=\mu_0I/2\pi r=2\times10^{-7}\times10/0.01=2\times10^{-4}$ T — four times the Earth's field, which is why Oersted's needle swung hard. At $1$ m the same wire gives $2\ \mu$T, a twentieth of the Earth's: household wiring does not disturb a compass unless you hold it against the cable.

### 3.2 The Lorentz force

The magnetic field $\mathbf B$ at a point is defined by the force it exerts on a charge $q$ moving through the point with velocity $\mathbf v$:

$$
\mathbf F=q\,\mathbf v\times\mathbf B,\qquad \lvert\mathbf F\rvert=\lvert q\rvert vB\sin\theta, \qquad (3.1)
$$

with $\theta$ the angle between $\mathbf v$ and $\mathbf B$; with an electric field present, $\mathbf F=q(\mathbf E+\mathbf v\times\mathbf B)$ — the Lorentz force, the complete statement of what electromagnetic fields do to a charge. Three properties follow from the cross product, and every later result is one of them in disguise:

1. **The force is perpendicular to $\mathbf v$, so it does no work.** $dW=\mathbf F\cdot\mathbf v\,dt=q(\mathbf v\times\mathbf B)\cdot\mathbf v\,dt=0$ identically. A magnetic field can change a particle's direction but never its speed or kinetic energy. (When a motor lifts a load, something else does the work — §3.27.)
2. **The force is perpendicular to $\mathbf B$**, so the component of velocity *along* the field is never changed; motion along $\mathbf B$ is free.
3. **The force vanishes when $\mathbf v\parallel\mathbf B$** and is largest when $\mathbf v\perp\mathbf B$; a charge fired along a field line goes straight.

Units: $[B]=$ N/(C m s$^{-1}$) $=$ N A$^{-1}$ m$^{-1}$ $=$ tesla. The size of the force: an electron at $10^{6}$ m s$^{-1}$ (a $3$ eV electron) crossing $1$ mT feels $evB=1.6\times10^{-19}\times10^{6}\times10^{-3}=1.6\times10^{-16}$ N, an acceleration of $1.8\times10^{14}$ m s$^{-2}$ — thirteen orders of magnitude above $g$, which is why gravity never appears in these problems.

> [!example] Worked example — directions with signs
> $\mathbf B=0.20\,\hat{\mathbf z}$ T. (a) A proton moves with $\mathbf v=3\times10^5\,\hat{\mathbf x}$ m s$^{-1}$: $\mathbf v\times\mathbf B=3\times10^5\times0.2\,(\hat{\mathbf x}\times\hat{\mathbf z})=-6\times10^4\,\hat{\mathbf y}$, so $\mathbf F=e(\ldots)=-9.6\times10^{-15}\,\hat{\mathbf y}$ N. (b) An electron with the same velocity: same cross product, $q=-e$: $\mathbf F=+9.6\times10^{-15}\,\hat{\mathbf y}$ N. (c) The proton with $\mathbf v=3\times10^5(\hat{\mathbf x}+\hat{\mathbf z})/\sqrt2$: only the $\hat{\mathbf x}$ part contributes, $F=e(3\times10^5/\sqrt2)(0.2)=6.8\times10^{-15}$ N along $-\hat{\mathbf y}$; the $\hat{\mathbf z}$ component of velocity rides along the field untouched.

> [!abstract] DIAGRAM D16.2 · The right-hand rule three ways
> *Show:* (a) the flat hand: fingers along $\mathbf v$, curling towards $\mathbf B$, thumb along $\mathbf v\times\mathbf B$, with the caption "then apply the sign of $q$"; (b) the grip rule for a wire: thumb along $I$, fingers along $\mathbf B$; (c) the cross-product parallelogram with $\mathbf v$, $\mathbf B$ and $\mathbf v\times\mathbf B$ as three mutually perpendicular arrows; each panel with $\odot$/$\otimes$ notation shown beside it.
> *Search:* "right hand rule lorentz force grip rule cross product three panels"

> [!danger] Trap — "the force changes the speed"
> $F=qvB\sin\theta$ has a $v$ in it, so students let it accelerate the particle along its motion. It cannot: it is always sideways. What the $v$ in the formula does is set the *radius of curvature*; the speed is a constant of the motion. If a question asks for the change in kinetic energy of a charge in a pure magnetic field, the answer is zero before any calculation.

### 3.3 Circular and helical motion: the clock that ignores the speed

**Perpendicular entry.** A charge $q$ enters a uniform field $\mathbf B$ with $\mathbf v\perp\mathbf B$. The force $qvB$ is perpendicular to $\mathbf v$ and constant in magnitude, so it is a centripetal force and the path is a circle in the plane perpendicular to $\mathbf B$:

$$
qvB=\frac{mv^2}{r}\quad\Rightarrow\quad r=\frac{mv}{\lvert q\rvert B}=\frac{p}{\lvert q\rvert B},\qquad \omega_c=\frac{v}{r}=\frac{\lvert q\rvert B}{m},\qquad T=\frac{2\pi m}{\lvert q\rvert B}. \qquad (3.2)
$$

The radius grows with momentum — the form $r=p/qB$ survives into relativity with $p=\gamma mv$, which is why chambers measure momentum, §3.12 — but **the period does not depend on the speed or the radius at all.** A faster particle runs a proportionally larger circle in exactly the same time; the angular frequency $\omega_c$, the *cyclotron frequency*, is fixed by $q/m$ and $B$ alone. This is the single most consequential fact in the chapter: it lets an alternating voltage of fixed frequency stay in step with a particle whose speed doubles and doubles again (§3.7), it makes the radio frequency of gyrating electrons a measurement of the field they are in, and it is the "clock" of magnetic resonance.

**Sense of rotation.** With $\mathbf B$ out of the page and a positive charge moving to the right, $\mathbf v\times\mathbf B$ points down: the centre is below the particle and it circles *clockwise*; a negative charge circles anticlockwise. Either way the charge's own circular current makes, inside its orbit, a field *opposite* to $\mathbf B$ — the orbital motion of a free charge is diamagnetic (§3.32 uses this).

**Oblique entry: the helix.** Resolve $\mathbf v$ into $v_\parallel=v\cos\theta$ along $\mathbf B$ and $v_\perp=v\sin\theta$ across it. The parallel part is untouched (property 2 of §3.2); the perpendicular part circles with radius and period (3.2) computed from $v_\perp$. The path is a helix about a field line, of radius $r=mv_\perp/\lvert q\rvert B$ and **pitch**

$$
p_{\text{helix}}=v_\parallel T=\frac{2\pi m\,v\cos\theta}{\lvert q\rvert B}. \qquad (3.3)
$$

Which plane does it circle in: always the plane perpendicular to $\mathbf B$, whatever the entry direction. Which way is the axis: along $\mathbf B$. What sets the radius: only the perpendicular component — the commonest error in helix problems is to put the full speed into $r$.

> [!success] Check
> Dimensions of $mv/qB$: kg m s$^{-1}$/(C · N s C$^{-1}$ m$^{-1}$) $=$ kg m$^2$ s$^{-1}$/(N s) $=$ m ✓. $\theta=90^\circ$ in (3.3): pitch zero, a circle ✓; $\theta=0$: infinite pitch, a straight line along $\mathbf B$ ✓. Numbers: an electron at $10^6$ m s$^{-1}$ in $1$ mT has $r=mv/eB=9.11\times10^{-31}\times10^6/(1.6\times10^{-19}\times10^{-3})=5.7$ mm and $T=2\pi m/eB=36$ ns ($f=28$ MHz — $28$ GHz per tesla for electrons). A $10$ MeV proton in $1$ T: $v=4.4\times10^7$ m s$^{-1}$, $r=0.46$ m, $f=15.2$ MHz — $15.2$ MHz per tesla for protons, the number every cyclotron and every MRI scanner is built around (the proton's *spin* precession frequency, $42.6$ MHz per tesla, is a different constant from a related physics).

> [!abstract] DIAGRAM D16.3 · The circle and the helix
> *Show:* left, a circular orbit seen along $\mathbf B$ ($\odot$ out of the page) with $\mathbf v$ tangent and $\mathbf F$ towards the centre at four points, a positive charge going clockwise and, dashed, a negative one going anticlockwise; right, a helix about a field line with the pitch $p=v_\parallel T$ marked, $v_\parallel$ and $v_\perp$ resolved at the entry point, and the entry angle $\theta$ to $\mathbf B$.
> *Search:* "charged particle circular motion magnetic field helix pitch entry angle diagram"

### 3.4 Combined fields: parallel, crossed, and the velocity selector

**$\mathbf E\parallel\mathbf B$.** The electric force accelerates the charge along the common direction; the magnetic force acts only on the perpendicular velocity, which it turns in a circle of unchanging radius. The path is a helix whose pitch grows (or shrinks) as $v_\parallel$ changes under $qE$: a screw with a stretching thread. No trickery of directions is needed — the two fields simply do not talk to each other in this configuration.

**$\mathbf E\perp\mathbf B$: the velocity selector.** Let $\mathbf E=E\hat{\mathbf y}$, $\mathbf B=B\hat{\mathbf z}$, and a charge enter along $\hat{\mathbf x}$ with speed $v$. Electric force $qE\hat{\mathbf y}$; magnetic force $q\mathbf v\times\mathbf B=qvB(\hat{\mathbf x}\times\hat{\mathbf z})=-qvB\hat{\mathbf y}$: the two are antiparallel *whatever the sign of $q$* (both flip together), and they cancel when

$$
v=\frac{E}{B}. \qquad (3.4)
$$

A particle with exactly this speed passes undeflected, of either sign and any mass; a slower one is pushed towards the electric force's side (the electric force wins), a faster one towards the other side (the magnetic force, $\propto v$, wins). Crossed plates and a magnet therefore *select a speed*: with $E=10^5$ V m$^{-1}$ and $B=0.10$ T, only $v=10^{6}$ m s$^{-1}$ gets through. What happens to those that do not pass exactly is the cycloid family of §3.10.

> [!abstract] DIAGRAM D16.4 · The velocity selector
> *Show:* two plates with $\mathbf E$ between them (down), a magnetic field into the page ($\otimes$) filling the same region, a positive charge moving right with $q\mathbf E$ drawn down and $q\mathbf v\times\mathbf B$ drawn up; three paths: the undeflected one at $v=E/B$, a slower one curving towards the electric side, a faster one curving the other way; a slit at the exit.
> *Search:* "velocity selector crossed electric magnetic fields undeflected path faster slower particles"

> [!info] Why the selector does not care about the sign or the mass
> Both forces are proportional to $q$, so the balance condition has no $q$ in it; neither force involves $m$, so neither does the condition. That is exactly what makes the selector useful in front of a mass spectrometer (§3.6): it hands over particles of one speed, and the spectrometer's radius then measures $m/q$ cleanly.

### 3.5 The three-region method

Most "particle in a field" problems have the field in a bounded region and the particle entering from outside. The protocol: **(1) mark the regions** and the field in each; **(2) in each field region the path is a circular arc of radius $r=mv_\perp/qB$ about a centre that lies on the perpendicular to $\mathbf v$ at the entry point**, a distance $r$ away, on the side $\mathbf F$ points; **(3) match the geometry** — where the arc meets the boundary fixes the exit point, the tangent there fixes the exit direction, and the angle turned, $\varphi$, fixes the time inside, $t=\varphi/\omega_c=\varphi m/qB$, *never* the full period unless the particle completes a circle.

**A strip of field.** A field $\mathbf B$ fills the strip $0<x<d$; a particle enters at $x=0$ moving along $+x$. Its centre is at $(0,\pm r)$. If $r>d$ the arc reaches $x=d$ after turning through $\varphi$ with $\sin\varphi=d/r$: the particle exits deflected by $\varphi$, displaced sideways by $r(1-\cos\varphi)$, having spent $t=(m/qB)\arcsin(d/r)$ inside. If $r<d$ it never reaches the far edge: it turns through $180^\circ$ and comes back out through $x=0$, displaced by $2r$, after exactly half a period, $t=\pi m/qB$. The borderline $r=d$ — the particle grazes the far boundary — is the "minimum speed to cross" question: $v_{\min}=qBd/m$.

**A circular region** of radius $R$ entered radially: by symmetry the particle exits radially too, having turned through $\varphi$ with $\tan(\varphi/2)=R/r$ (the centre of the arc, the entry point and the region's centre form a right-angled figure). For $r=R$ the deflection is $90^\circ$.

> [!example] Worked example — through a strip
> Protons at $2.0\times10^{6}$ m s$^{-1}$ enter a $5.0$ cm strip of $0.30$ T perpendicularly. $r=mv/eB=1.67\times10^{-27}\times2\times10^6/(1.6\times10^{-19}\times0.3)=6.96$ cm $>d$: they cross. $\sin\varphi=5/6.96=0.719$, $\varphi=46^\circ$; time inside $t=\varphi m/eB=(0.802)(1.67\times10^{-27})/(4.8\times10^{-20})=28$ ns (against a full period of $219$ ns); sideways displacement $r(1-\cos\varphi)=2.1$ cm. Halve the speed: $r=3.48$ cm $<d$, the protons turn back, exit $7.0$ cm from where they entered, after $109$ ns.

> [!abstract] DIAGRAM D16.5 · The three-region protocol
> *Show:* a field strip with $\otimes$ marks; entry point, the perpendicular to $\mathbf v$ with the centre at distance $r$; the arc to the exit point on the far boundary with the turned angle $\varphi$ and the tangent (exit direction) drawn; below, the $r<d$ case with the semicircle back out; a third panel with a circular field region entered radially and the exit radial too.
> *Search:* "charged particle enters magnetic field region arc exit angle time inside geometry"

### 3.6 The mass spectrometer

Ions of charge $q$ and mass $m$, accelerated from rest through $V$, enter a field $B$ perpendicularly and are bent into a semicircle onto a detector. From $\tfrac12mv^2=qV$ and (3.2),

$$
r=\frac{mv}{qB}=\frac1B\sqrt{\frac{2mV}{q}},\qquad \frac{r_1}{r_2}=\sqrt{\frac{m_1}{m_2}}\ \ (\text{same }q,V,B). \qquad (3.5)
$$

Heavier ions land farther out; the separation at the detector is $2\Delta r$. Two isotopes of masses $m$ and $m+\Delta m$: $\Delta r/r=\tfrac12\Delta m/m$, so the resolution $\Delta m/m$ is set by how narrowly the ion beam can be defined compared with $r$. With a velocity selector in front (Bainbridge), $v=E/B_1$ is fixed independently of $V$ and $r=mE/qB_1B_2$ is linear in $m$.

> [!example] Worked example — separating uranium
> Singly charged $^{235}$U and $^{238}$U ions ($m=235u$ and $238u$, $u=1.66\times10^{-27}$ kg) accelerated through $10$ kV in $0.50$ T: $r_{238}=\dfrac{1}{0.5}\sqrt{\dfrac{2\times3.95\times10^{-25}\times10^4}{1.6\times10^{-19}}}=0.444$ m; $r_{235}=0.444\sqrt{235/238}=0.441$ m. $\Delta r=2.8$ mm, so the two beams arrive $5.6$ mm apart after their semicircles — resolvable, and this is the calutron that separated uranium in 1944, at enormous cost per gram because each ion carries one atom.

### 3.7 The cyclotron

Two hollow D-shaped electrodes in a uniform $\mathbf B$, with an alternating voltage $V_0$ across the gap. Inside a dee the field is zero (a conductor) and the ion coasts on a semicircle; each time it crosses the gap the voltage kicks it by $qV_0$ — *if* the voltage has reversed since the last crossing. Because $T=2\pi m/qB$ is independent of speed, a gap voltage alternating at the **resonance frequency**

$$
f=\frac{qB}{2\pi m} \qquad (3.6)
$$

is always in the right phase, though the ion's speed and radius grow with every turn: the spiral is a sequence of ever-larger semicircles, each taking the same time. The ion gains $2qV_0$ per revolution and leaves at the dee radius $R$ with $v=qBR/m$:

$$
K_{\max}=\frac{q^2B^2R^2}{2m},\qquad N_{\text{turns}}=\frac{K_{\max}}{2qV_0},\qquad t=\frac{N_{\text{turns}}}{f}. \qquad (3.7)
$$

The energy depends on $B$ and $R$, *not* on $V_0$: a smaller voltage only means more turns.

> [!example] Worked example — a real machine
> Protons, $B=1.5$ T, $R=0.50$ m, $V_0=50$ kV. $f=eB/2\pi m_p=22.9$ MHz. $K_{\max}=(1.6\times10^{-19}\times1.5\times0.5)^2/(2\times1.67\times10^{-27})=4.3\times10^{-12}$ J $=27$ MeV. Energy per turn $2eV_0=100$ keV, so $N=270$ turns in $t=270/22.9\times10^{6}=12\ \mu$s — the proton travels about $270\times\pi\times0.3$ m $\approx250$ m in that time, at an average speed of $2\times10^7$ m s$^{-1}$.

**The limits.** (i) *Relativity:* at $27$ MeV, $\gamma-1=K/m_pc^2=2.9\%$, so the effective mass and the period have grown by $3\%$ and the fixed-frequency voltage falls out of step; the classical cyclotron stops being useful for protons at a few tens of MeV and never worked for electrons (a $0.5$ MeV electron already has $\gamma=2$). The remedies are to sweep the frequency (synchrocyclotron) or to raise $B$ with the energy and keep $r$ fixed (synchrotron, §3.12). (ii) *Focusing:* a perfectly uniform field lets the ions drift out of the mid-plane; a field that falls slightly with radius curves the field lines and pushes strays back (the same physics as the mirror of §3.8). (iii) *Size:* $K_{\max}\propto B^2R^2$ — doubling the energy needs a magnet with four times the pole area.

> [!abstract] DIAGRAM D16.6 · The cyclotron
> *Show:* two dees seen from above with the gap between them, the field $\odot$ throughout, the ion's spiral of semicircles growing outward and the deflector at the rim; beneath it a timing strip showing the gap voltage alternating and the ion's gap crossings landing on the same phase every half-period.
> *Search:* "cyclotron dees spiral path gap voltage resonance timing diagram"

### 3.8 Helices in a converging field: the magnetic mirror

A charge spiralling along a field line that *converges* (the field grows along the line) is slowed along the line and eventually reflected. The mechanism is in $\nabla\cdot\mathbf B=0$: where $B_z$ increases with $z$ near an axis, the field lines bend inward and there is a small radial component $B_r=-\tfrac r2\,\partial B_z/\partial z$ (integrate $\nabla\cdot\mathbf B=0$ over a thin disc of radius $r$: $2\pi rB_r\,dz+\pi r^2\,dB_z=0$). The azimuthal velocity $v_\perp$ crossed with this $B_r$ gives a force *along* the axis,

$$
F_z=-\frac{\lvert q\rvert v_\perp r}{2}\frac{\partial B}{\partial z}=-\frac{mv_\perp^2}{2B}\frac{\partial B}{\partial z}=-\mu\,\frac{\partial B}{\partial z},\qquad \mu\equiv\frac{mv_\perp^2}{2B}, \qquad (3.8)
$$

using $r=mv_\perp/\lvert q\rvert B$; the direction — towards weaker field — is the same for either sign of charge, because the sense of gyration and the sign of $q$ flip together. The particle is pushed towards *weaker* field: $\mu$ is its magnetic moment (a circulating charge, §3.28) and $-\mu\,\partial B/\partial z$ is the force on a dipole in a gradient — the magnetic version of the electric dipole's gradient force. Now the invariant: the parallel kinetic energy changes as $d(\tfrac12mv_\parallel^2)=F_z\,dz=-\mu\,dB$; the total kinetic energy is constant (no work by $\mathbf B$), so $d(\tfrac12mv_\perp^2)=+\mu\,dB$; but $\tfrac12mv_\perp^2=\mu B$, so $d(\mu B)=\mu\,dB+B\,d\mu=\mu\,dB$, whence

$$
d\mu=0:\qquad \frac{mv_\perp^2}{2B}=\text{const}\quad(\text{field varying slowly over one orbit}). \qquad (3.9)
$$

As the particle moves into stronger field, $v_\perp^2\propto B$ grows and $v_\parallel$ shrinks; it is **reflected** where $\tfrac12mv_\perp^2$ has swallowed all the kinetic energy, i.e. where $B$ reaches $B_0/\sin^2\theta_0$, $\theta_0$ being the pitch angle (between $\mathbf v$ and $\mathbf B$) at the point where the field is $B_0$. A particle between two such regions (a *magnetic bottle*) is trapped if the field at the throats, $B_{\max}$, exceeds that value:

$$
\sin^2\theta_0>\frac{B_0}{B_{\max}}\quad\text{trapped};\qquad \sin^2\theta_0<\frac{B_0}{B_{\max}}\quad\text{lost through the throat.} \qquad (3.10)
$$

The velocities that escape fill a cone about the field direction — the **loss cone** — of half-angle $\theta_{\text{lc}}=\arcsin\sqrt{B_0/B_{\max}}$: for a mirror ratio $B_{\max}/B_0=10$, $\theta_{\text{lc}}=18^\circ$. The Earth's dipole field is such a bottle: charged particles from the solar wind and from cosmic-ray collisions in the atmosphere bounce between the polar regions, where the field lines converge, in the Van Allen belts; the ones in the loss cone precipitate into the upper atmosphere and make the aurora. Fusion "mirror machines" used the same idea; the loss cone was their weakness, because collisions keep scattering particles into it.

> [!abstract] DIAGRAM D16.7 · The magnetic mirror
> *Show:* field lines converging into a throat on the right; a helical path whose radius shrinks and whose pitch closes up as it approaches, reflecting before the throat; the radial component $B_r$ drawn at one point with the force $F_z=-\mu\,\partial B/\partial z$; inset, velocity space with the loss cone of half-angle $\theta_{\text{lc}}$ about the field axis.
> *Search:* "magnetic mirror converging field lines reflection loss cone velocity space diagram"

> [!warning] Condition of validity
> (3.9) is an *adiabatic* invariant: it holds when $B$ changes little over one gyration ($r\,\lvert\nabla B\rvert\ll B$) and over one period. In a sharply varying field — a particle crossing the edge of a magnet's pole — it fails, and the three-region method of §3.5 applies instead.

### 3.9 The Hall effect

A flat conductor of thickness $t$ (along $\mathbf B$) and width $w$ carries current $I$ along $x$ in a field $B\hat{\mathbf z}$. The carriers — density $n$, charge $q$, drift velocity $v_d$ along $\pm x$ — are pushed sideways by $q\mathbf v_d\times\mathbf B$ and pile up on one edge until the transverse electric field they create balances the magnetic force: $qE_H=qv_dB$, so $E_H=v_dB$ and the **Hall voltage** across the width is $V_H=E_Hw=v_dBw$. With $I=nqv_d(wt)$,

$$
V_H=\frac{IB}{nqt},\qquad R_H\equiv\frac{E_H}{JB}=\frac{1}{nq}. \qquad (3.11)
$$

Three things fall out. **The carrier sign:** for a given current direction, positive carriers move with the current and negative ones against it; $q\mathbf v_d$ is the same vector for both, so the *force* is towards the same edge — but positive carriers make that edge positive while electrons make it negative. The polarity of $V_H$ therefore reveals the sign of the carriers; that is how it was learned that some metals (zinc, cadmium) and $p$-type semiconductors conduct by positive holes. **The carrier density**, from $n=IB/qtV_H$ — the Hall coefficient $R_H=1/nq$ is the standard way of counting carriers. **The mobility** $\mu_m=v_d/E=\sigma R_H$, from combining with the conductivity.

> [!example] Worked example — copper against a semiconductor
> A copper strip $1.0$ mm thick, $I=10$ A, $B=1.0$ T, $n=8.5\times10^{28}$ m$^{-3}$: $V_H=IB/net=10/(8.5\times10^{28}\times1.6\times10^{-19}\times10^{-3})=0.73\ \mu$V — measurable with care, useless as a sensor. An $n$-type semiconductor wafer, $t=0.10$ mm, $n=10^{21}$ m$^{-3}$, $I=10$ mA, $B=0.50$ T: $V_H=0.01\times0.5/(10^{21}\times1.6\times10^{-19}\times10^{-4})=0.31$ V. The ratio is the ratio of carrier densities, $10^{8}$: Hall probes, the everyday magnetic-field sensors, are semiconductors for exactly this reason.

> [!abstract] DIAGRAM D16.8 · The Hall plate, two panels
> *Show:* a slab with current along $x$, $\mathbf B$ along $z$, and (a) electrons drifting along $-x$ pushed to the front edge by $q\mathbf v\times\mathbf B$, the front edge marked $-$ and $E_H$ drawn; (b) positive holes drifting along $+x$ pushed to the *same* front edge, now marked $+$, with $E_H$ reversed; a voltmeter across the width in each panel showing opposite polarities.
> *Search:* "hall effect electrons versus holes same edge opposite polarity diagram"

### 3.10 Drifts: crossed fields in general, the cycloid, and the gradient drift

**$\mathbf E\times\mathbf B$ drift, first way — force balance.** In crossed fields, look for a velocity at which the net force vanishes: $q(\mathbf E+\mathbf v_d\times\mathbf B)=0$. The solution perpendicular to both fields is

$$
\mathbf v_d=\frac{\mathbf E\times\mathbf B}{B^2},\qquad v_d=\frac EB, \qquad (3.12)
$$

the selector speed of (3.4) — with no $q$ and no $m$ in it: electrons and ions drift *together*, at the same velocity, in the same direction. (That is why the drift carries no net current in a neutral plasma, and why it is not a "force" but a motion of the whole guiding centre.)

**Second way — change frame.** In a frame moving at $\mathbf v_d$ the electric field is $\mathbf E'=\mathbf E+\mathbf v_d\times\mathbf B=0$ (for $v_d\ll c$), and only $\mathbf B$ remains: the particle simply circles. Back in the laboratory frame, the motion is a circle *carried along* at $\mathbf v_d$ — a **cycloid** if the particle started from rest. Take $\mathbf E=E\hat{\mathbf y}$, $\mathbf B=B\hat{\mathbf z}$, a positive charge released at the origin from rest: the drift is $\mathbf E\times\mathbf B/B^2=(E/B)\hat{\mathbf x}$, and the gyration about the drifting centre has speed $E/B$ (in the drifting frame the particle starts with velocity $-v_d\hat{\mathbf x}$) and radius $r_c=mv_d/qB=mE/qB^2$:

$$
x(t)=\frac EB\left(t-\frac{\sin\omega_ct}{\omega_c}\right),\qquad y(t)=\frac{E}{B\omega_c}\left(1-\cos\omega_ct\right),\qquad \omega_c=\frac{qB}{m}. \qquad (3.13)
$$

This is the path of a point on the rim of a wheel of radius $r_c$ rolling along the $x$-axis at speed $E/B$: the particle stops momentarily at the cusps every period, rises to a maximum height $2r_c=2mE/qB^2$, and reaches its maximum speed $2E/B$ at the top of each arch — all consistent with energy conservation, $\tfrac12mv_{\max}^2=qE\cdot2r_c$ ✓. A particle launched with some initial velocity traces a *curtate* or *prolate* cycloid (loops), the same rolling wheel with the point inside or outside the rim. Numbers: $E=10^4$ V m$^{-1}$, $B=0.10$ T: $v_d=10^{5}$ m s$^{-1}$; an electron from rest has $r_c=mE/eB^2=5.7\ \mu$m, rises $11\ \mu$m and peaks at $2\times10^{5}$ m s$^{-1}$; a proton on the same path has $r_c$ $1836$ times larger, $1.0$ cm, and the same drift speed.

> [!abstract] DIAGRAM D16.9 · The cycloid and the rolling wheel
> *Show:* crossed fields ($\mathbf E$ up, $\mathbf B$ out of page); a cycloid with cusps on the $x$-axis and arches of height $2r_c$; beneath it the rolling wheel of radius $r_c$ whose rim point traces the curve, with the drift velocity $E/B$ marked; dashed, a curtate and a prolate variant.
> *Search:* "charged particle crossed E and B fields cycloid trajectory rolling circle drift"

**Gradient drift.** In a field that is stronger on one side of the orbit, the radius of curvature $r=mv_\perp/qB$ is smaller where $B$ is larger: the orbit does not close, and the guiding centre creeps sideways, perpendicular to both $\mathbf B$ and $\nabla B$. Averaging the force $q\mathbf v\times\mathbf B$ over one gyration with $B=B_0+(\nabla B)\cdot\mathbf r$ gives a mean force $-\mu\nabla B$ (the same $\mu=mv_\perp^2/2B$ as (3.8), now with the gradient across the orbit), and a steady force $\mathbf F$ perpendicular to $\mathbf B$ produces a drift $\mathbf v=\mathbf F\times\mathbf B/qB^2$ by the argument of (3.12) with $\mathbf F/q$ in place of $\mathbf E$:

$$
\mathbf v_{\nabla B}=\frac{\mu}{q}\,\frac{\mathbf B\times\nabla B}{B^2}=\pm\frac{v_\perp r}{2}\,\frac{\mathbf B\times\nabla B}{B^2}. \qquad (3.14)
$$

Unlike the $\mathbf E\times\mathbf B$ drift this one *depends on the sign of $q$*: ions and electrons drift oppositely and a current flows. Around the Earth, whose dipole field weakens outward, trapped protons drift westward and electrons eastward — the *ring current*, a few million amperes circling the planet at a few Earth radii, whose field is what a magnetometer on the ground measures during a magnetic storm. A curved field line adds a **curvature drift** of the same form with $mv_\parallel^2/R_c$ (the centrifugal force in the frame following the line) as the force; it is stated here and used in Part 10.

### 3.11 Measured $q/m$: Thomson's electron

Thomson (1897) sent cathode rays between two plates (field $E$, length $L$) inside a magnetic field $B$ perpendicular to both the beam and $\mathbf E$, and watched a spot on a screen. With $\mathbf E$ alone the beam deflects, as in the electrostatics chapter, by $y=\dfrac{qEL^2}{2mv^2}$ inside the plates (and by a proportionate amount on the screen). With $\mathbf B$ added and adjusted until the spot returns to the centre, $v=E/B$ (3.4). Eliminating the unknown $v$:

$$
\frac qm=\frac{2yE}{B^2L^2}\quad\text{or, with the magnetic bend alone, }\ \frac qm=\frac{v}{Br}=\frac{E}{B^2r}. \qquad (3.15)
$$

Neither $q$ nor $m$ is measured — only their ratio, and it came out $1.76\times10^{11}$ C kg$^{-1}$, nearly two thousand times the largest known value (hydrogen's ion). Millikan's oil drops (electrostatics §3.13) later supplied $e$ separately, and the electron's mass followed. Numbers that reproduce the experiment: $E=10^4$ V m$^{-1}$, $B=5.0\times10^{-4}$ T, so $v=2.0\times10^{7}$ m s$^{-1}$; with $L=5.0$ cm the electric deflection inside the plates is $y=\dfrac{(1.76\times10^{11})(10^4)(0.05)^2}{2(2\times10^7)^2}=5.5$ mm, and the magnetic bend alone would have radius $r=mv/eB=0.23$ m.

> [!abstract] DIAGRAM D16.10 · Thomson's tube
> *Show:* a cathode-ray tube with the deflecting plates, the coils producing $\mathbf B$ into the page over the same length, the screen with the undeflected spot and the electric-only deflected spot; the three vectors $\mathbf v$, $\mathbf E$, $\mathbf B$ mutually perpendicular; the formula $v=E/B$ beside the null condition.
> *Search:* "J J Thomson e/m experiment cathode ray tube crossed fields deflection diagram"

### 3.12 Where it matters, and how to read a track

**The synchrotron.** Since $r=p/qB$, a particle can be kept on a *fixed* circle while it gains energy if $B$ is raised in proportion to $p$ and the accelerating frequency is raised as the speed approaches $c$ — a ring of bending magnets and a few accelerating cavities, unlimited in energy by the cyclotron's resonance problem, limited instead by radiation (electrons) and magnet strength (protons: $p\,[\text{GeV}/c]=0.3\,B\,[\text{T}]\,r\,[\text{m}]$, so $7$ TeV needs $8.3$ T over a bending radius of $2.8$ km — the LHC's ring is $4.3$ km in radius because dipoles fill only two-thirds of it).

**Reading a cloud- or bubble-chamber photograph.** The track is a circle of radius $r$ in a known $B$, so $p=qBr$; in the units experimenters use,

$$
p\,[\text{MeV}/c]=300\,B\,[\text{T}]\,r\,[\text{m}], \qquad (3.16)
$$

because $eBr\cdot c$ in joules divided by $e$ per MeV is $3\times10^8Br$ eV. A particle losing energy to the gas spirals *inward*: the direction in which the radius shrinks is the direction of motion, and with the direction known the sense of curvature gives the sign of the charge. Anderson's 1932 photograph — a track curving the "electron way" but *entering* a lead plate from below and emerging with a smaller radius above — was a positive particle of electron mass: the positron. A $10$ cm radius in $1.5$ T is $45$ MeV/$c$, already relativistic for an electron ($m_ec^2=0.5$ MeV) and gentle for a proton ($938$ MeV): the same rule (3.16) applies to both because it never assumed $v\ll c$.

**The aurora.** Solar-wind electrons of a few keV, trapped and then scattered into the loss cone, spiral down converging field lines into the atmosphere at $100$–$300$ km and excite oxygen (green, $558$ nm) and nitrogen (red and blue); the total power deposited in an active oval is of order $10^{10}$–$10^{11}$ W. Mass spectrometry in chemistry, magnetic confinement of fusion plasmas, magnetohydrodynamic pumps and the deflection coils of every old television are the same equation, $r=mv/qB$, at different scales.

> [!abstract] DIAGRAM D16.11 · Reading a chamber track
> *Show:* a spiral track in a uniform field ($\otimes$) with the radius visibly decreasing along the motion, an arrow marking the direction of travel deduced from the shrinking radius, and the centre of curvature on the side that reveals the sign; a lead plate across the chamber with the track's curvature tighter after it; the $p=300Br$ rule written beside a measured radius.
> *Search:* "cloud chamber positron track lead plate curvature energy loss direction anderson"

### 3.13 Biot–Savart: the source law

A short element $d\mathbf l$ of a thin wire carrying steady current $I$ contributes, at a point displaced from it by $\mathbf r$ (unit vector $\hat{\mathbf r}$ *from the element to the point*),

$$
d\mathbf B=\frac{\mu_0}{4\pi}\,\frac{I\,d\mathbf l\times\hat{\mathbf r}}{r^2},\qquad \mathbf B=\frac{\mu_0}{4\pi}\int\frac{I\,d\mathbf l\times\hat{\mathbf r}}{r^2}, \qquad (3.17)
$$

with $\mu_0/4\pi=10^{-7}$ T m A$^{-1}$. This is the magnetic Coulomb's law, and like Coulomb's law it is experimental input, not a theorem: Biot and Savart (1820) measured the force on a magnet near wires of various shapes, and Ampère's force law between circuits is the same statement. Read it as Coulomb's law with three changes. The source is $I\,d\mathbf l$ instead of $dq$; the strength still falls as $1/r^2$ and still superposes; but the *direction* is a cross product — $d\mathbf B$ is perpendicular both to the element and to the line joining it to the point. So a current element makes no field on its own line ($d\mathbf l\parallel\hat{\mathbf r}$), the largest field broadside on ($\sin90^\circ$), and its field lines are circles around the element's axis, oriented by the grip rule. The dimensional check: T m A$^{-1}$ · A · m/m$^2$ $=$ T ✓.

By (2.1), a single charge $q$ moving at $\mathbf v$ is the element $I\,d\mathbf l\to q\mathbf v$:

$$
\mathbf B=\frac{\mu_0}{4\pi}\,\frac{q\,\mathbf v\times\hat{\mathbf r}}{r^2}=\frac{1}{c^2}\,\mathbf v\times\mathbf E\qquad(v\ll c), \qquad (3.18)
$$

the second form using $\mu_0=1/\varepsilon_0c^2$ and the charge's own Coulomb field $\mathbf E=q\hat{\mathbf r}/4\pi\varepsilon_0r^2$. A moving charge carries its electric field with it and, in addition, a magnetic field that is that electric field crossed with $\mathbf v/c^2$ — small by the factor $v/c$, which is the first hint that magnetism is electricity seen in motion (Part 10). Two charges moving side by side at $v$ attract magnetically with a force $v^2/c^2$ times their electric repulsion: at $v=10^6$ m s$^{-1}$, one part in $10^5$.

> [!abstract] DIAGRAM D16.12 · The Biot–Savart element
> *Show:* a wire with an element $I\,d\mathbf l$, the vector $\mathbf r$ to a field point $P$ off to the side, the angle between them, and $d\mathbf B$ at $P$ pointing into the page (perpendicular to both); a second point on the wire's own line with $d\mathbf B=0$ marked; the circles of $\mathbf B$ around the element's axis with the grip-rule hand.
> *Search:* "biot savart law current element cross product geometry dB direction"

> [!info] Why a cross product
> Because a current has a direction and the field must be built from the only vectors available — the element's direction and the displacement to the point — in a way that reverses when the current reverses. The two candidates are along $d\mathbf l$ (fails: a compass beside a wire points *around* it, not along it) and along $d\mathbf l\times\hat{\mathbf r}$. Experiment picks the second, and Part 10 shows that relativity would have forced it.

### 3.14 The straight wire: finite by angles, infinite as a limit

A straight segment carries $I$; the field point $P$ is at perpendicular distance $d$ from its line. Take the foot of the perpendicular as origin along the wire; an element at position $l$ subtends angle $\theta$ at $P$ measured from the perpendicular, so $l=d\tan\theta$, $dl=d\sec^2\theta\,d\theta$, $r=d\sec\theta$, and the angle between $d\mathbf l$ and $\hat{\mathbf r}$ is $90^\circ-\theta$, so $\lvert d\mathbf l\times\hat{\mathbf r}\rvert=dl\cos\theta$. Every element's $d\mathbf B$ points the same way (perpendicular to the plane of the wire and $P$, by the grip rule), so the magnitudes add:

$$
B=\frac{\mu_0I}{4\pi}\int\frac{\cos\theta\,dl}{r^2}=\frac{\mu_0I}{4\pi d}\int_{-\beta}^{\alpha}\cos\theta\,d\theta=\frac{\mu_0I}{4\pi d}\,(\sin\alpha+\sin\beta), \qquad (3.19)
$$

where $\alpha$ and $\beta$ are the angles subtended at $P$ by the two ends, on either side of the perpendicular (the electrostatic rod, §3.5 of the previous chapter, had the same integral with a $\lambda$ and no cross product). The limits: **infinite wire**, $\alpha=\beta\to90^\circ$:

$$
B=\frac{\mu_0I}{2\pi d}, \qquad (3.20)
$$

circling the wire, falling as $1/d$ — the $1/r$ law of a line source, exactly as for the line charge. **Semi-infinite wire**, point level with the end ($\alpha=90^\circ$, $\beta=0$): $\mu_0I/4\pi d$, half the infinite value. **A point on the line of the wire** (beyond an end): zero, since $d\mathbf l\parallel\hat{\mathbf r}$ for every element. **Far away** ($d\gg L$): $\sin\alpha+\sin\beta\approx L/d$, $B\approx\mu_0IL/4\pi d^2$ — a single element's field, (3.17) with $dl=L$ ✓.

> [!example] Worked example — the centre of a square, and of a hexagon
> A square of side $a$: each side is at $d=a/2$ and subtends $\alpha=\beta=45^\circ$, contributing $\dfrac{\mu_0I}{4\pi(a/2)}\cdot2\sin45^\circ=\dfrac{\sqrt2\mu_0I}{2\pi a}$, all four in the same direction (grip rule on each side, the current circulating): $B=\dfrac{2\sqrt2\mu_0I}{\pi a}$. A regular hexagon of side $a$: $d=a\sqrt3/2$, $\alpha=\beta=30^\circ$, six sides: $B=6\cdot\dfrac{\mu_0I}{4\pi(a\sqrt3/2)}=\dfrac{\sqrt3\mu_0I}{\pi a}$. For $a=10$ cm and $I=1$ A: $11.3\ \mu$T and $6.9\ \mu$T. The general $n$-gon inscribed in a circle of radius $R$ gives $B=\dfrac{\mu_0In}{2\pi R}\tan\dfrac\pi n$, which tends to $\mu_0I/2R$ as $n\to\infty$ — the circular loop of §3.15, recovered as a limit ✓.

> [!abstract] DIAGRAM D16.13 · The finite wire's angles
> *Show:* a straight segment, the point $P$ at perpendicular distance $d$, the foot of the perpendicular, an element at angle $\theta$ with $r=d\sec\theta$ marked, the two end-angles $\alpha$ and $\beta$; $\mathbf B$ at $P$ drawn into the page with the grip-rule hand; a small inset of the square with the four contributions all pointing the same way.
> *Search:* "magnetic field finite straight wire angles alpha beta biot savart derivation"

> [!danger] Trap — $\mu_0/2\pi$ or $\mu_0/4\pi$
> $\mu_0I/2\pi d$ is the *infinite* wire; $\mu_0I/4\pi d$ is the semi-infinite wire *at a point level with its end*, and $\mu_0/4\pi$ is the Biot–Savart constant itself. A finite wire at a general point is neither: use (3.19). The paper's favourite: "a long wire is bent at right angles; find the field at a point on the bisector at distance $d$ from the corner" — two semi-infinite wires, each seen at perpendicular distance $d/\sqrt2$ with angles $45^\circ$ and $90^\circ$.

### 3.15 The loop and the arc

**Centre of a circular loop.** Every element $dl$ of a loop of radius $R$ is perpendicular to $\hat{\mathbf r}$ (which points to the centre) and at the same distance $R$; every $d\mathbf B$ points along the axis (grip rule):

$$
B_{\text{centre}}=\frac{\mu_0I}{4\pi R^2}\oint dl=\frac{\mu_0I}{2R}\quad(N\text{ turns: }N\mu_0I/2R). \qquad (3.21)
$$

Numbers: $R=5$ cm, $I=1$ A: $12.6\ \mu$T, a quarter of the Earth's; $100$ turns: $1.26$ mT.

**On the axis**, at distance $x$ from the centre. An element at the top of the loop is at distance $s=\sqrt{R^2+x^2}$ from $P$; $d\mathbf l\perp\hat{\mathbf r}$ still, so $dB=\mu_0I\,dl/4\pi s^2$, directed perpendicular to $\hat{\mathbf r}$ in the plane containing the axis — tilted from the axis by the angle $\alpha$ with $\sin\alpha=R/s$. The diametrically opposite element's $d\mathbf B$ has the same axial component and the opposite transverse one (the ring symmetry of the electrostatics chapter, §3.4, once more); only the axial component survives:

$$
B_x=\int dB\sin\alpha=\frac{\mu_0I}{4\pi s^2}\cdot\frac Rs\cdot2\pi R=\frac{\mu_0IR^2}{2(R^2+x^2)^{3/2}}. \qquad (3.22)
$$

> [!success] Check
> $x=0$: $\mu_0I/2R$ ✓ (3.21). $x\gg R$: $B\approx\mu_0IR^2/2x^3=\dfrac{\mu_0}{4\pi}\dfrac{2\mu}{x^3}$ with $\mu=I\pi R^2$ — the axial field of a *dipole* (§3.17), the exact counterpart of $2kp/x^3$ ✓. Unlike the charged ring's field, the loop's axial field is largest *at the centre* and falls monotonically: there is no $\sin$-of-a-tilt penalty because $d\mathbf B$ is perpendicular to $\hat{\mathbf r}$ rather than along it. At $x=R$ it is $2^{-3/2}=0.354$ of the centre value.

> [!tip] FIGURE F16.2 · Axial field of a current loop
> *Why:* the profile the paper asks you to sketch, and the one to contrast with the charged ring's (which vanishes at the centre).
> *Data:* $B/B_{\text{centre}}=(1+(x/R)^2)^{-3/2}$ on $x/R=0,0.25,\dots,3$; the line [0, 0] is the axis.

```mermaid
xychart-beta
  title "current loop: axial field against distance from the centre (units mu0 I / 2R, x/R)"
  x-axis 0 --> 3
  y-axis 0 --> 1.1
  line [1.0, 0.913, 0.716, 0.512, 0.354, 0.244, 0.171, 0.122, 0.089, 0.067, 0.051, 0.04, 0.032]
  line [0, 0]
```

> *Read:* maximum at the centre, $0.35$ at one radius, then the $1/x^3$ dipole tail — at $x=3R$ the field is $3\%$ of the centre value, and $(R/x)^3/1=3.7\%$ would be the pure-dipole estimate.

**Arc.** An arc of radius $R$ subtending angle $\theta_0$ at its centre: the same argument as (3.21) with $\oint dl\to R\theta_0$,

$$
B_{\text{arc, centre}}=\frac{\mu_0I\theta_0}{4\pi R}, \qquad (3.23)
$$

$\mu_0I/4R$ for a semicircle, $\mu_0I/8R$ for a quadrant — proportional to the angle, with no trigonometry (contrast the charged arc's $\sin(\theta_0/2)$: there the element fields were radial and had to be resolved; here they are all axial).

**Compound loops.** A wire made of straight segments and arcs: add the pieces, each by its own formula, with directions by the grip rule on each piece; **any straight segment whose line passes through the field point contributes nothing** there. So a semicircle with two long straight leads along its diameter's line gives $\mu_0I/4R$ at the centre — the leads contribute zero; a semicircle whose leads run off perpendicular to the diameter at its ends gives $\mu_0I/4R$ plus two semi-infinite-wire terms $\mu_0I/4\pi R$ each; a circular loop with a straight chord across it needs (3.19) for the chord. Two concentric semicircles of radii $a<b$ joined by radial segments (the "horseshoe"): $\dfrac{\mu_0I}{4}\left(\dfrac1a-\dfrac1b\right)$ if the currents run oppositely as seen from the centre, which they do in a single closed loop.

> [!abstract] DIAGRAM D16.14 · Compound loops at their centres
> *Show:* four shapes with the field point at the centre and each piece labelled with its contribution: (a) semicircle plus diameter-line leads ($\mu_0I/4R+0$); (b) semicircle with perpendicular leads ($\mu_0I/4R+2\times\mu_0I/4\pi R$); (c) concentric semicircles joined by radial legs; (d) a full loop with one straight chord; directions $\odot$/$\otimes$ marked on each piece.
> *Search:* "magnetic field at centre of combination of arc and straight wire compound loop problems"

### 3.16 Solenoid and toroid by stacking loops

A solenoid — $n$ turns per unit length, current $I$, radius $R$ — is a stack of loops. The slice between $z$ and $z+dz$ (measured along the axis from the field point) carries current $nI\,dz$ and contributes, by (3.22), $dB=\dfrac{\mu_0nI\,dz\,R^2}{2(R^2+z^2)^{3/2}}$ along the axis. Substitute $z=R\cot\theta$ (so $\theta$ is the angle between the axis and the line from the field point to the rim of that slice): $dz=-R\csc^2\theta\,d\theta$, $(R^2+z^2)^{3/2}=R^3\csc^3\theta$, and $dB=\tfrac12\mu_0nI\sin\theta\,d\theta$. Integrating from one end (angle $\theta_1$) to the other ($\theta_2$):

$$
B_{\text{axis}}=\frac{\mu_0nI}{2}\left(\cos\theta_1+\cos\theta_2\right), \qquad (3.24)
$$

with $\theta_1,\theta_2$ the angles subtended at the point by the radii of the two end rims, measured from the axis on either side.

> [!success] Check — the three limits
> **Infinite solenoid**, $\theta_1=\theta_2\to0$: $B=\mu_0nI$ — uniform along the axis, independent of $R$ ✓ (and, Ampère will show, uniform across the whole interior). **End of a long solenoid**, $\theta_1=0$, $\theta_2=90^\circ$: $B=\tfrac12\mu_0nI$, exactly half — the other half would come from the missing continuation ✓. **Far from a short coil** ($L\ll$ distance): expand and recover the dipole field of a loop with $N=nL$ turns ✓.

> [!tip] FIGURE F16.3 · Axial field of a finite solenoid
> *Why:* the plateau, the half-value at the ends and the rapid fall outside are the whole story of "how long is long".
> *Data:* (3.24) for a solenoid of length $L=10R$, $B/\mu_0nI$ against $z/L$ from $-0.75$ to $0.75$ in steps of $0.125$; the ends are at $z/L=\pm0.5$.

```mermaid
xychart-beta
  title "solenoid L = 10R: axial field B / (mu0 n I) against z / L"
  x-axis -0.75 --> 0.75
  y-axis 0 --> 1.05
  line [0.034, 0.108, 0.498, 0.887, 0.96, 0.977, 0.981, 0.977, 0.96, 0.887, 0.498, 0.108, 0.034]
  line [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
```

> *Read:* $0.98$ at the centre, $0.50$ at the ends, $0.14$ one radius beyond an end. A solenoid ten times longer than its radius is "infinite" to $2\%$ over its middle half; a coil as long as its diameter is not a solenoid at all.

**Outside a long solenoid** the field is weak but not zero: all the flux $\pi R^2\mu_0nI$ that goes up the inside must come back down the outside, spread over an area that grows without limit as the solenoid lengthens — so the outside field tends to zero *for an infinite solenoid*, and is of order $R/L$ times the inside field for a finite one. Ampère's law (§3.19) makes the infinite case exact.

**Toroid.** Bend a solenoid of $N$ turns into a ring of mean radius $r$: the turns per unit length are $n=N/2\pi r$, the field is confined to the winding and circles the ring, and

$$
B_{\text{toroid}}=\mu_0nI=\frac{\mu_0NI}{2\pi r} \qquad (3.25)
$$

inside the winding, varying as $1/r$ across the cross-section (stronger near the hole), and zero both in the hole and outside — §3.19 proves this in one line; here it follows from stacking loops whose return flux is all inside the ring. Numbers: $N=500$, $I=2$ A, $r=10$ cm: $2.0$ mT.

> [!abstract] DIAGRAM D16.15 · Stacked loops and the field lines of a solenoid and a toroid
> *Show:* a solenoid in section with its turns as $\odot$ above the axis and $\otimes$ below, the field lines dense and straight inside, spreading at the ends and returning outside as widely spaced curves (drawn small, labelled "$\sim R/L$ of inside"); the angles $\theta_1$, $\theta_2$ from an axial point to the two end rims; beside it a toroid with the circular field lines confined to the winding and none in the hole.
> *Search:* "solenoid field lines inside outside return flux; toroid magnetic field confined to winding"

### 3.17 The magnetic moment

A plane loop of area $A$ carrying $I$ has magnetic dipole moment

$$
\boldsymbol\mu=I\mathbf A\quad(N\text{ turns: }NI\mathbf A), \qquad (3.26)
$$

with $\mathbf A$ normal to the loop in the sense given by the right-hand rule on the current. Its far field, from (3.22) and the general dipole form, is

$$
B_{\text{axis}}=\frac{\mu_0}{4\pi}\frac{2\mu}{r^3},\qquad B_{\text{equator}}=\frac{\mu_0}{4\pi}\frac{\mu}{r^3},\qquad \mathbf B=\frac{\mu_0}{4\pi}\,\frac{3(\boldsymbol\mu\cdot\hat{\mathbf r})\hat{\mathbf r}-\boldsymbol\mu}{r^3}\quad(r\gg\sqrt A), \qquad (3.27)
$$

the electric dipole's (3.12) of the previous chapter with $k\mathbf p\to(\mu_0/4\pi)\boldsymbol\mu$. The loop is the elementary magnet: every coil, solenoid and bar magnet is a dipole from far enough away, with $\mu$ equal to $NIA$ for a coil and to the sum of its atoms' moments for a magnet.

| | electric dipole $\mathbf p$ | magnetic dipole $\boldsymbol\mu$ |
|---|---|---|
| made of | $+q$ and $-q$ separated by $\mathbf d$ | a current loop, $I\mathbf A$ |
| far field, axis / equator | $2kp/r^3$ / $kp/r^3$ | $(\mu_0/4\pi)2\mu/r^3$ / $(\mu_0/4\pi)\mu/r^3$ |
| torque in a uniform field | $\mathbf p\times\mathbf E$ | $\boldsymbol\mu\times\mathbf B$ (§3.24) |
| energy | $-\mathbf p\cdot\mathbf E$ | $-\boldsymbol\mu\cdot\mathbf B$ (§3.24) |
| force in a gradient | $(\mathbf p\cdot\nabla)\mathbf E$ | $\nabla(\boldsymbol\mu\cdot\mathbf B)$, e.g. $\mu\,dB/dz$ (§3.8, §3.36) |
| field *inside* the source | from $+$ to $-$: **opposite** to $\mathbf p$ | through the loop: **along** $\boldsymbol\mu$ |
| field lines | begin and end on the charges | close through the loop |

The last two rows are the honest difference. Far away the two dipoles are indistinguishable; inside, the electric dipole's field runs against its moment (from the positive charge to the negative) while the current loop's field runs *with* it — because there are no poles for the lines to end on. That difference is what makes a bar magnet's interior field point from its south pole to its north (§3.29), and it is the reason the "two poles" picture of a magnet, convenient outside, is wrong inside.

> [!abstract] DIAGRAM D16.16 · Two dipoles, side by side
> *Show:* left, an electric dipole with its field lines leaving $+q$ and entering $-q$, the internal line from $+$ to $-$ antiparallel to $\mathbf p$; right, a current loop with identical external lines but the internal lines passing through the loop *along* $\boldsymbol\mu$, closing round the outside; the far-field region shaded on both with "identical here".
> *Search:* "electric dipole versus magnetic dipole field lines comparison inside the source"

### 3.18 Why a loop law should exist, and Ampère's law

The infinite wire's field (3.20) circles the wire and falls as $1/r$. Walk once round the wire on a circle of radius $r$, adding up $\mathbf B\cdot d\mathbf l$: the field is everywhere along the path, so the sum is $(\mu_0I/2\pi r)(2\pi r)=\mu_0I$ — **independent of $r$**. Now walk round on any closed path whatever: along an element $d\mathbf l$ the component of $d\mathbf l$ along the circling field is $r\,d\varphi$ ($\varphi$ the azimuth about the wire), so $\mathbf B\cdot d\mathbf l=(\mu_0I/2\pi r)\,r\,d\varphi=(\mu_0I/2\pi)\,d\varphi$, and a closed path that goes round the wire once has $\oint d\varphi=2\pi$, one that does not enclose it has $\oint d\varphi=0$. The $1/r$ of the field and the $r$ of the arc cancel exactly — the same cancellation that made Gauss's law out of $1/r^2$ and $r^2$ in the previous chapter. By superposition the circulation of the total field around a closed loop counts the currents that thread it:

$$
\oint_C\mathbf B\cdot d\mathbf l=\mu_0I_{\text{enc}}, \qquad (3.28)
$$

where $I_{\text{enc}}$ is the net current through *any* surface bounded by $C$ — Ampère's circuital law, the magnetic Gauss's law, true for every closed loop and every steady current distribution (for changing fields Maxwell adds a term; the electromagnetic-waves note owns it).

**The sign convention, fixed with an instance.** Choose a direction round $C$; curl the right hand's fingers that way; the thumb is the positive direction for threading currents. Three long parallel wires carry $I_1=5$ A out of the page, $I_2=3$ A into the page and $I_3=2$ A out of the page. A loop taken *anticlockwise* (thumb out of the page) around wires 1 and 2 only: $I_{\text{enc}}=+5-3=+2$ A, $\oint\mathbf B\cdot d\mathbf l=\mu_0\times2=2.5\times10^{-6}$ T m. The same loop clockwise: $-2.5\times10^{-6}$ T m — both sides change sign, nothing physical changes. A loop around all three anticlockwise: $+4$ A. A loop enclosing none: zero, although $\mathbf B$ is nowhere zero on it.

**The honest symmetry requirement.** (3.28) is always *true* and only sometimes *useful*: it gives $B$ only when the symmetry guarantees that $\mathbf B$ is parallel to the loop and constant in magnitude along it (or perpendicular to some sides, or zero on them), so that the integral collapses to $B\times$ (length). That is exactly the Gaussian-surface logic of electrostatics §3.17, with the loop in place of the surface and "along" in place of "normal".

> [!abstract] DIAGRAM D16.17 · Loops around a wire, and the sign convention
> *Show:* a wire ($\odot$) with its circular field lines; a circular loop of radius $r$ and an irregular loop both enclosing it, with $\mathbf B\cdot d\mathbf l=(\mu_0I/2\pi)d\varphi$ marked on an element of the irregular one; a loop that does not enclose the wire with the azimuth going forward and back; a second panel with the three wires, the anticlockwise loop, the thumb out of the page, and "$+5-3=+2$ A".
> *Search:* "ampere's circuital law loop around wire azimuth argument sign convention right hand rule"

### 3.19 The applications: eight fields in eight lines

The protocol is the electrostatic one: **name the symmetry** (a straight line, a plane, an axis of a long cylinder or solenoid), **choose the loop** so that $\mathbf B$ is along it and constant on the parts that count and perpendicular or zero on the rest, **say why**, and **count $I_{\text{enc}}$** — through the loop, with signs, with $N$ turns counted $N$ times.

1. **Infinite straight wire.** Circle of radius $r$: $B\cdot2\pi r=\mu_0I$, $B=\mu_0I/2\pi r$ — (3.20) in one line.
2. **Thick wire**, radius $a$, uniform current density $J=I/\pi a^2$. Inside ($r<a$): $I_{\text{enc}}=I\,r^2/a^2$, so $B=\mu_0Ir/2\pi a^2$, rising linearly; outside: $\mu_0I/2\pi r$. Continuous at the surface, maximum there — the solid sphere's profile with $r$ and $1/r$ in place of $r$ and $1/r^2$. Numbers: $100$ A in a $5$ mm wire: $4.0$ mT at the surface, $2.0$ mT halfway in, $0$ on the axis.
3. **Coaxial cable**: inner conductor radius $a$ carrying $I$, outer shell $b<r<c$ carrying $-I$. Between them ($a<r<b$): $\mu_0I/2\pi r$; inside the shell: $I_{\text{enc}}=I-I\dfrac{r^2-b^2}{c^2-b^2}=I\dfrac{c^2-r^2}{c^2-b^2}$, so $B=\dfrac{\mu_0I}{2\pi r}\dfrac{c^2-r^2}{c^2-b^2}$, falling to zero at $r=c$; outside: zero — the cable radiates no static field, which is why it is a cable.
4. **Infinite plane sheet** with surface current $K$ (amperes per metre of width). By symmetry $\mathbf B$ is parallel to the sheet, perpendicular to $\mathbf K$, and reverses across the sheet. A rectangular loop of length $\ell$ straddling the sheet with two sides parallel to $\mathbf B$: $2B\ell=\mu_0K\ell$,
$$
B=\frac{\mu_0K}{2}\quad\text{on each side, independent of distance}, \qquad (3.29)
$$
the twin of the charged sheet's $\sigma/2\varepsilon_0$. $K=1000$ A m$^{-1}$: $0.63$ mT.
5. **Two parallel sheets** with opposite $\mathbf K$: $\mu_0K$ between them, zero outside — a solenoid flattened out, and the field of a pair of bus bars.
6. **Infinite solenoid**, $n$ turns per metre. Take a rectangular loop with one side of length $\ell$ inside, parallel to the axis, and the opposite side far outside; the two connecting sides are perpendicular to $\mathbf B$ and contribute nothing; the far side is in zero field (a loop with both long sides outside encloses no current, so the outside field is the same at every distance, hence equal to its value at infinity, zero). Then $B\ell=\mu_0n\ell I$:
$$
B=\mu_0nI\quad\text{everywhere inside, zero outside}, \qquad (3.30)
$$
and moving the inside side off the axis changes nothing: the interior field is *uniform*, not just uniform along the axis. Numbers: $1000$ turns per metre at $5$ A: $6.3$ mT.
7. **Toroid**, $N$ turns, at radius $r$ inside the winding: a circle of radius $r$ threads all $N$ turns once, $B\cdot2\pi r=\mu_0NI$, giving (3.25); a circle in the hole threads no current; a circle outside the whole toroid threads $N$ turns going one way and $N$ coming back, net zero. Both give $B=0$ ✓.
8. **Thin cylindrical current shell** (a hollow pipe of radius $a$ carrying $I$ along its length): inside, $I_{\text{enc}}=0$, $B=0$ — *provided the shell is long*, so that the field has the cylindrical symmetry the loop needs; outside, $\mu_0I/2\pi r$, exactly as if the current were on the axis. A thick pipe with inner radius $a$ and outer $b$: $B=\dfrac{\mu_0I}{2\pi r}\dfrac{r^2-a^2}{b^2-a^2}$ inside the wall.

> [!tip] FIGURE F16.4 · Field of a thick wire
> *Why:* the linear interior and the $1/r$ exterior meeting at the surface is the profile students draw with a jump; the coaxial cable is the same curve with a second conductor switched on.
> *Data:* $B/B(a)$ against $r/a$ on $0,0.25,\dots,3$: $r/a$ inside, $a/r$ outside; the line [0, 0] is the axis.

```mermaid
xychart-beta
  title "thick wire: B(r) in units of B at the surface, against r/a"
  x-axis 0 --> 3
  y-axis 0 --> 1.1
  line [0, 0.25, 0.5, 0.75, 1.0, 0.8, 0.667, 0.571, 0.5, 0.444, 0.4, 0.364, 0.333]
  line [0, 0]
```

> *Read:* zero on the axis, maximum at the surface, no jump (the current is distributed, not on a sheet), and $1/r$ outside — half the surface value at $r=2a$, where the solid *sphere's* electric field would be a quarter.

> [!danger] Trap — the loop that does not enclose, and the $N$ that is forgotten
> Ampère's law with a loop *beside* a wire gives zero circulation and tells you nothing about $B$ there — it does not say the field is zero. And a solenoid loop of length $\ell$ encloses $n\ell$ turns, a toroid's circle encloses all $N$: the enclosed *current* is $n\ell I$ or $NI$, never $I$.

### 3.20 The overlap trick: a uniform field from two cylinders

Inside a long cylinder of radius $a$ carrying uniform current density $\mathbf J$ (along $z$), the field at perpendicular position $\mathbf r_\perp$ from the axis is, by application 2 in vector form,

$$
\mathbf B=\frac{\mu_0}{2}\,\mathbf J\times\mathbf r_\perp, \qquad (3.31)
$$

azimuthal, of magnitude $\mu_0Jr/2$. Now overlap two such cylinders with densities $+\mathbf J$ and $-\mathbf J$, axes displaced by $\mathbf d$. In the lens-shaped overlap both formulas apply and add:

$$
\mathbf B=\frac{\mu_0}{2}\,\mathbf J\times\mathbf r_\perp-\frac{\mu_0}{2}\,\mathbf J\times(\mathbf r_\perp-\mathbf d)=\frac{\mu_0}{2}\,\mathbf J\times\mathbf d, \qquad (3.32)
$$

**uniform**, of magnitude $\mu_0Jd/2$, perpendicular to both the current and the line of centres. The electrostatic twin (previous chapter, OL6) produced a uniform *electric* field in the same lens from $\pm\rho$; the magnetic version is more useful, because it is also the answer to a standard question — **the field inside a cylindrical hole drilled off-centre in a current-carrying wire**: the wire with the hole is the full wire ($+\mathbf J$) plus a cylinder of $-\mathbf J$ filling the hole, so the field in the hole is uniform, $\mu_0Jd/2$, with $J=I/\pi(a^2-b^2)$ for a wire of radius $a$, hole radius $b$ and total current $I$. Numbers: $I=100$ A, $a=1.0$ cm, $b=3.0$ mm, $d=5.0$ mm: $J=3.5\times10^{5}$ A m$^{-2}$, $B=1.1$ mT throughout the hole, independent of the hole's size. Two overlapping cylinders are also how a uniform transverse field is made over a large volume in accelerator magnets ("cosine-theta" coils are this construction, thinned to a shell).

> [!success] Check
> $\mathbf d\to0$: the cylinders cancel, $\mathbf B=0$ ✓. A hole on the axis ($d=0$): zero field inside, as the hollow pipe of application 8 requires ✓. Dimensions: (T m A$^{-1}$)(A m$^{-2}$)(m) $=$ T ✓.

> [!abstract] DIAGRAM D16.18 · Overlapping cylinders and the off-centre hole
> *Show:* two circles of equal radius overlapping, one $\odot$ ($+J$) and one $\otimes$ ($-J$), axes $d$ apart, with parallel field arrows filling the lens perpendicular to the line of centres; beside it a wire in cross-section with an off-centre circular hole, the same uniform arrows in the hole, and the two component cylinders drawn dashed.
> *Search:* "magnetic field inside off-centre cylindrical hole in current carrying wire superposition uniform field"

### 3.21 Ampère or Biot–Savart? The decision, and two problems both ways

| the source | use | because |
|---|---|---|
| infinite wire, thick wire, coax, pipe | Ampère | cylindrical symmetry closes a circular loop |
| infinite sheet, two sheets | Ampère | planar symmetry closes a rectangle |
| infinite solenoid, toroid | Ampère | translation / rotation symmetry closes the loop |
| finite wire, polygon, arc, loop, finite solenoid | Biot–Savart | no loop has $B$ constant along it |
| a point *off* the axis of a loop or coil | neither, in closed form | elliptic integrals; Part 10 names them |
| two overlapping cylinders, a wire with a hole | Ampère twice, then superpose | each piece is symmetric alone |

**Problem 1, both ways — the infinite wire.** *Biot–Savart:* (3.19) with $\alpha=\beta=90^\circ$, an integral and a substitution. *Ampère:* one line. **Problem 2 — the infinite solenoid.** *Biot–Savart:* stack the loops, (3.24), then take both angles to zero — and even then only the *axial* field is obtained; the uniformity across the interior needs a further argument. *Ampère:* the rectangle of application 6 gives the field everywhere inside in three lines and proves the uniformity at the same time. The cost difference is the point of the law; but Ampère's law *cannot* give the finite wire, the finite solenoid or the loop, because their fields are not constant along any closed path, and a finite isolated segment is not even a steady current (charge would pile up at its ends — real circuits close, and it is the *whole* circuit's field that Biot–Savart computes piece by piece).

> [!tip] FIGURE F16.5 · Which source law
> *Why:* the choice is made in the first ten seconds of a problem and cannot be undone cheaply.
> *Data:* the decision table above as a flow, with the three admissible symmetries and the superposition exit.

```mermaid
flowchart TD
  A["What is the source?"] --> B{"infinitely long with cylindrical symmetry?"}
  A --> C{"infinite plane sheet or pair of sheets?"}
  A --> D{"infinite solenoid or toroid?"}
  B -- "yes" --> B1["Ampere: circle, B times 2 pi r = mu0 I enclosed"]
  C -- "yes" --> C1["Ampere: rectangle straddling, 2 B l = mu0 K l"]
  D -- "yes" --> D1["Ampere: rectangle with one side inside, B = mu0 n I"]
  B -- "no" --> E{"is it a symmetric piece minus another symmetric piece?"}
  C -- "no" --> E
  D -- "no" --> E
  E -- "yes" --> E1["Ampere on each piece, superpose (hole in a wire)"]
  E -- "no" --> F["Biot-Savart: angles for straight pieces, arcs by angle, loops on axis"]
  B1 --> Z["check: limits, direction by grip rule, N turns counted"]
  C1 --> Z
  D1 --> Z
  E1 --> Z
  F --> Z
```

> *Read:* three symmetries, one superposition trick, and everything else is an integral. If the field point is off every axis of symmetry, expect no closed form.

### 3.22 No monopoles

The magnetic analogue of Gauss's law has a zero on the right:

$$
\oint_S\mathbf B\cdot d\mathbf A=0\quad\text{for every closed surface},\qquad \nabla\cdot\mathbf B=0. \qquad (3.33)
$$

It is not a theorem but the experimental absence of magnetic charge, and Biot–Savart is consistent with it (the field of every current element circles the element and threads no closed surface net). Consequences:

* **Field lines never begin or end.** They close on themselves (through a loop, through a solenoid, through a magnet) or run to infinity; there is no magnetic "source" for them to leave from. The lines *inside* a bar magnet run from its south pole to its north — the only way to close the loops that leave north and enter south outside.
* **Cutting a magnet gives two magnets**, never a separated north and south. In the bound-current picture (§3.30) a magnet is a solenoid of atomic currents, and cutting a solenoid in two gives two solenoids, each with a field entering one end and leaving the other.
* **The flux through any closed surface is zero**: whatever enters the end of a solenoid leaves through its sides and the far end; a Gaussian surface around one pole of a magnet has as much flux in as out. For an *open* surface, "the flux through a loop" (PART 20's central quantity) is well defined only because (3.33) makes it the same for every surface spanning the loop.
* **A solenoid cannot be made into a monopole** by any winding: its lines that come out of one end must go back in the other.

How would a monopole announce itself? A magnetic charge $g$ passing through a superconducting ring would change the flux through the ring by $\mu_0g$ and leave a permanent step in its current — the signature Cabrera's detector looked for in 1982 (one candidate event, never repeated). Dirac showed that a single monopole anywhere would explain why electric charge is quantised, with $g$ quantised in units of $h/e$; none has been found, and (3.33) stands.

> [!abstract] DIAGRAM D16.19 · The cut magnet and the closed lines
> *Show:* a bar magnet with its external lines from N to S and its internal lines from S to N, every line closed; the same magnet sawn in two, each half with its own N and S and its own closed lines; a closed Gaussian surface drawn around one pole with equal flux in and out; a dashed "impossible" panel of an isolated N pole with lines only leaving.
> *Search:* "cut a bar magnet two magnets no monopoles closed magnetic field lines gauss law magnetism"

### 3.23 Force on a current: from the carriers to $I\mathbf L\times\mathbf B$

A wire of cross-section $A$ carries $n$ carriers per unit volume, each of charge $q$ drifting at $\mathbf v_d$. In a field $\mathbf B$ each feels $q\mathbf v_d\times\mathbf B$; a length $\mathbf L$ of wire (vector along the current) holds $nAL$ of them, so the total force is $nALq\,\mathbf v_d\times\mathbf B$. Since $I=nqv_dA$ and $q\mathbf v_d$ points along the current for either sign of carrier,

$$
\mathbf F=I\,\mathbf L\times\mathbf B\quad(\text{straight wire, uniform }\mathbf B),\qquad d\mathbf F=I\,d\mathbf l\times\mathbf B\quad(\text{in general}). \qquad (3.34)
$$

The force is transmitted to the wire because the deflected carriers press against the lattice (the Hall field of §3.9 is the mechanism); magnitude $ILB\sin\theta$, direction by $\mathbf L\times\mathbf B$ with no sign to apply — the current's direction already contains the carriers' sign. Numbers: $10$ A over $0.50$ m across $0.20$ T: $1.0$ N, the weight of $100$ g; motors are many such lengths in strong fields.

**The chord theorem.** For a curved wire in a *uniform* field, $\mathbf F=I\left(\int d\mathbf l\right)\times\mathbf B$, and $\int d\mathbf l$ along any path is the straight vector from its start to its end: **a curved wire feels the force of the straight chord joining its ends.** A semicircle of radius $R$ with $\mathbf B$ perpendicular to its plane feels $2IRB$, perpendicular to the chord in the plane; the same current in the diameter would feel the same force. **A closed loop** has $\oint d\mathbf l=0$, so in a uniform field it feels **no net force** — the semicircle and its diameter, run as one loop, push against each other and cancel. Then why does a loop turn? Because the forces on its sides are equal and opposite but not collinear: a *couple* (§3.24). In a non-uniform field the loop does feel a net force, $\nabla(\boldsymbol\mu\cdot\mathbf B)$, towards stronger field when aligned — the pull on a nail (§3.36).

> [!abstract] DIAGRAM D16.20 · The chord theorem
> *Show:* a semicircular wire in a uniform field ($\otimes$) with $d\mathbf F$ arrows on several elements all radial, their vector sum equal to the force on the dashed diameter drawn beneath; a closed loop of arbitrary shape with the forces on opposite elements cancelling; a small inset of a rectangular loop whose side forces form a couple.
> *Search:* "force on curved current carrying wire equals chord uniform magnetic field semicircle closed loop zero net force"

### 3.24 Torque on a loop, its energy, the galvanometer and the oscillating magnet

A rectangular loop, sides $a$ and $b$, carries $I$ in a uniform $\mathbf B$; its normal $\hat{\mathbf n}$ (by the current's right-hand rule) makes angle $\theta$ with $\mathbf B$. Orient the sides of length $b$ perpendicular to $\mathbf B$: each feels $F=IbB$, in opposite directions, and the two lines of action are separated by $a\sin\theta$ — a couple of moment $IbB\cdot a\sin\theta=IAB\sin\theta$. The other two sides feel forces along the rotation axis, equal and opposite and collinear (they stretch the loop, they do not turn it). With $\mu=IA$ (or $NIA$):

$$
\tau=\mu B\sin\theta,\qquad \boldsymbol\tau=\boldsymbol\mu\times\mathbf B, \qquad (3.35)
$$

turning $\boldsymbol\mu$ towards $\mathbf B$. Any planar loop is a sum of thin rectangles whose internal sides cancel, so (3.35) holds for every shape; for a non-planar coil, $\boldsymbol\mu$ is the vector sum of its faces' moments. **Energy:** the work to rotate from $\theta_1$ to $\theta_2$ against the couple is $\int\mu B\sin\theta\,d\theta=\mu B(\cos\theta_1-\cos\theta_2)$, so with the zero at $90^\circ$,

$$
U=-\boldsymbol\mu\cdot\mathbf B, \qquad (3.36)
$$

lowest when aligned (stable), highest when anti-aligned (unstable) — the electric dipole's (3.14) of the previous chapter with the symbols changed, and the same caveat: in a *non-uniform* field the loop also feels the force $-\nabla U=\nabla(\boldsymbol\mu\cdot\mathbf B)$.

**Small oscillations and the measurement of $\boldsymbol\mu$.** A magnet (or coil) of moment $\mu$ and moment of inertia $I_m$ about its suspension, displaced by $\theta$ from alignment: $I_m\ddot\theta=-\mu B\sin\theta\approx-\mu B\theta$,

$$
T=2\pi\sqrt{\frac{I_m}{\mu B}}, \qquad (3.37)
$$

the torsion pendulum of PART 10 with $\mu B$ as the torsion constant. This is how a magnet's moment is measured: time its oscillations in a known field (the Earth's horizontal component, §3.37), weigh and measure it for $I_m$, solve for $\mu$. A bar magnet of $50$ g and $10$ cm ($I_m=mL^2/12=4.2\times10^{-5}$ kg m$^2$) with $\mu=1.0$ A m$^2$ in $B_H=30\ \mu$T swings with $T=2\pi\sqrt{4.2\times10^{-5}/3\times10^{-5}}=7.4$ s; a moment twice as large halves the *square* of the period. Two magnets compared in the same field: $\mu_1/\mu_2=(T_2/T_1)^2(I_1/I_2)$ — no absolute field needed.

**The moving-coil galvanometer.** A coil of $N$ turns and area $A$ hangs on a torsion fibre (constant $\kappa$) between the poles of a magnet shaped so that the field is *radial* at the coil's sides: the plane of the coil is then always parallel to the local $\mathbf B$, $\sin\theta=1$ for every deflection, and the couple is $NIAB$ whatever the angle. Equilibrium with the fibre: $NIAB=\kappa\varphi$,

$$
\varphi=\frac{NAB}{\kappa}\,I, \qquad (3.38)
$$

a deflection *proportional* to the current — the linear scale that makes the instrument. The current sensitivity $NAB/\kappa$ is raised by more turns, a larger area, a stronger magnet or a weaker fibre (and a soft-iron core, §3.35, to make the field radial and strong). The [[Current-electricity|current-electricity]] note turns this into ammeters and voltmeters with shunts and multipliers; here the point is that (3.35) plus a radial field is the whole principle.

> [!abstract] DIAGRAM D16.21 · Torque on a loop, and the galvanometer's radial field
> *Show:* a rectangular loop seen edge-on with $\hat{\mathbf n}$ at angle $\theta$ to horizontal $\mathbf B$, the two side forces $IbB$ up and down separated by $a\sin\theta$, the rotation axis marked; beside it the galvanometer: curved pole pieces and a cylindrical iron core making radial field lines, the coil's sides always crossing the field at right angles, the fibre and pointer above.
> *Search:* "torque on rectangular current loop couple derivation; moving coil galvanometer radial magnetic field diagram"

### 3.25 Forces between currents, the ampere, and the third law

Wire 1 carries $I_1$; at distance $d$ its field is $\mu_0I_1/2\pi d$, circling it. A parallel wire 2 carrying $I_2$ lies in that field, and by (3.34) a length $L$ of it feels $I_2LB_1$:

$$
\frac FL=\frac{\mu_0I_1I_2}{2\pi d}, \qquad (3.39)
$$

**attractive for currents in the same direction, repulsive for opposite** — check with $\mathbf L\times\mathbf B$: for parallel currents, wire 1's field at wire 2 (grip rule) crossed with wire 2's direction points *towards* wire 1. Two $100$ A wires $1$ cm apart: $0.20$ N per metre. Until 2019 this equation *defined* the ampere: the current that, in two infinite parallel wires $1$ m apart, produces $2\times10^{-7}$ N per metre — which is why $\mu_0$ was exactly $4\pi\times10^{-7}$; since 2019 the ampere is fixed by the value of $e$ and $\mu_0$ is measured ($4\pi\times1.00000000055\times10^{-7}$ — the difference matters to no problem in this course).

**Which wire feels what.** The force on wire 2 is computed from *wire 1's* field alone, never from the total field (a wire feels no force from its own field, by symmetry). The force on wire 1 from wire 2's field is equal and opposite: Newton's third law holds for two long parallel currents.

**A wire and a moving charge.** A charge $q$ moving parallel to a wire at speed $v$ and distance $d$ feels $F=qv\mu_0I/2\pi d$, towards the wire if $q$ moves with the current's sense of positive charge. The wire feels the charge's field (3.18) acting on its current. For two *point* charges moving at right angles the magnetic forces are not even antiparallel — the third law fails for magnetic forces between point charges, and momentum is conserved only when the *field's* momentum (density $\varepsilon_0\mathbf E\times\mathbf B$) is counted. Steady closed circuits always obey the third law in total; isolated moving charges do not.

> [!info] Why the third law can fail without breaking mechanics
> Newton's third law is momentum conservation for two bodies *with nothing in between*. Between two moving charges there is the field, which carries momentum and can hold some of it for a while; the total — particles plus field — is conserved exactly. PART 28 and the electromagnetic-waves note (radiation pressure) make this quantitative; here it is enough to know that the exception is real and that it never appears for closed steady circuits.

**Rails.** A bar of length $L$ slides on two rails in a field $\mathbf B$ perpendicular to the plane; a current $I$ driven through bar and rails feels $ILB$ along the rails — the rail gun and, run backwards, the generator of PART 20. Two currents at an angle, or a wire near a loop, are the same computation with the field of one at the other, element by element.

> [!abstract] DIAGRAM D16.22 · Parallel wires
> *Show:* two long parallel wires with currents in the same direction; wire 1's circular field lines, its field at wire 2 drawn, and the force on wire 2 towards wire 1 with $\mathbf L\times\mathbf B$ indicated; a second panel with opposite currents and repulsion; the formula $\mu_0I_1I_2/2\pi d$ and a note "field of the *other* wire only".
> *Search:* "force between two parallel current carrying wires attract repel direction definition of ampere"

### 3.26 Magnetic pressure, boundary conditions, and the field's energy

**The force on a current sheet.** A sheet with surface current $K$ separates a region of field $B_1$ from one of field $B_2$ (both parallel to the sheet, perpendicular to $\mathbf K$). The sheet's *own* field is $\pm\mu_0K/2$ on its two sides (3.29), and it cannot push on itself; the field of everything else is the same on both sides, namely the average $(B_1+B_2)/2$. So the force per unit area is $K\times(B_1+B_2)/2$, and since $B_1-B_2=\mu_0K$ (the sheet's own jump), it equals

$$
\frac FA=\frac{B_1^2-B_2^2}{2\mu_0}, \qquad (3.40)
$$

directed from the strong-field side to the weak: **a magnetic field pushes on the currents that confine it with a pressure $B^2/2\mu_0$.** For a solenoid, $B$ inside and $0$ outside: the windings are pushed *outward* with $B^2/2\mu_0$ — $4.0\times10^{5}$ Pa, four atmospheres, at $1$ T; $400$ atmospheres at $10$ T, which is why high-field magnets are built like pressure vessels and why the winding of a pulsed magnet can burst. The factor $\tfrac12$ is the electrostatic conductor's factor once more (electrostatics §3.8): the sheet feels only the field of the *rest*.

**The solenoid's end.** Cut a long solenoid across; the two halves carry parallel currents and attract, with a force equal to $B^2/2\mu_0$ times the cross-section (the field lines behave as if under a tension $B^2/2\mu_0$ along their length and a pressure $B^2/2\mu_0$ across it — the Maxwell stress, which Part 10 uses for the pinch). A $1$ T solenoid of $10$ cm$^2$ bore pulls its halves together with $400$ N.

**Boundary conditions.** Across any surface current $K$, the *tangential* component of $\mathbf B$ jumps by $\mu_0K$ (a small Amperian rectangle straddling the sheet) and the *normal* component is continuous (a small pillbox and (3.33)). That is why the solenoid's field steps from $\mu_0nI$ to zero exactly at the winding: the winding is a sheet with $K=nI$.

**Energy density, announced.** A magnetic field stores energy $u=B^2/2\mu_0$ per unit volume — the same expression as the pressure, as for the electric field ($\tfrac12\varepsilon_0E^2$ was both the energy density and the electrostatic pressure). PART 21 derives it from the work done to establish the current in an inductor; the check to carry meanwhile: a solenoid of volume $V$ stores $\tfrac12LI^2$ with $L=\mu_0n^2V$, which is $\tfrac12\mu_0n^2I^2V=(B^2/2\mu_0)V$ ✓. At $1$ T that is $0.4$ MJ per cubic metre; an MRI magnet's bore holds a few megajoules, which is why a quench is an event.

> [!abstract] DIAGRAM D16.23 · Magnetic pressure on a solenoid
> *Show:* a solenoid in section with $B$ inside and zero outside; on the winding, outward arrows labelled $B^2/2\mu_0$; the sheet's own field $\pm\mu_0K/2$ drawn on both sides and the "field of the rest" $B/2$ crossing it; a second panel with the solenoid cut in two and the halves pulled together with $B^2A/2\mu_0$.
> *Search:* "magnetic pressure B squared over 2 mu0 solenoid winding outward force hoop stress"

### 3.27 Where the energy comes from: the motor puzzle

A motor lifts a load, yet §3.2 proved that magnetic forces do no work. Both are true; the resolution is worth one page because it is the bridge to induction. Take the simplest motor: a straight wire of length $L$ carrying $I$ across a field $B$, moving sideways at speed $u$ under the force $ILB$. The carriers have two velocity components — the drift $v_d$ along the wire and the wire's own $u$ sideways. The magnetic force on each carrier is perpendicular to its *total* velocity, and has two components: one sideways, $qv_dB$, which pushes the wire and does work on it at the rate $qv_dB\cdot u$ per carrier (total $ILB\,u$); and one *along the wire*, $quB$, directed *against* the drift, which does negative work on the carriers at the rate $quB\cdot v_d$ per carrier — the same amount. The magnetic force's net work is zero, as it must be. But the backward force along the wire is an electric-field's worth of push against the current — an **EMF of $BLu$ opposing the current** (the motional EMF of PART 20) — and to keep $I$ flowing the battery must supply an extra power $\mathcal E I=BLuI=F_{\text{mag}}u$: exactly the mechanical power delivered. The battery does the work; the magnetic force merely *redirects* it, from the carriers' motion along the wire into the wire's motion across the field. Every motor, loudspeaker and rail gun runs on this accounting, and every generator runs it backwards.

> [!abstract] Numbers to keep — the small forces and the large ones
> A carrier drifting at $v_d=10^{-4}$ m s$^{-1}$ in $1$ T feels $qv_dB=1.6\times10^{-23}$ N; a metre of $1$ mm$^2$ copper wire holds $10^{23}$ of them, and at $10$ A their forces sum to $ILB=10$ N. The largest laboratory magnetic pressures, $B^2/2\mu_0$ at $40$ T, are $6\times10^{8}$ Pa — the strength of steel, which is the practical ceiling on steady fields.

### 3.28 Rotating charges: the gyromagnetic ratio

A ring of radius $R$ carrying charge $Q$ and spinning at angular speed $\omega$ is a current $I=Q\omega/2\pi$ (charge past a point per unit time), hence a moment $\mu=I\pi R^2=\tfrac12Q\omega R^2$. If the ring also has mass $m$, its angular momentum is $L=mR^2\omega$, so

$$
\frac{\mu}{L}=\frac{Q}{2m}, \qquad (3.41)
$$

independent of $R$ and $\omega$. A disc, a sphere, any rigid body in which the charge is distributed like the mass, is a stack of such rings each obeying (3.41): the same ratio holds for the whole body. The **gyromagnetic ratio** $Q/2m$ is therefore a property of the charge-to-mass ratio alone — and for an electron on a Bohr orbit with $L=\hbar$,

$$
\mu_B=\frac{e\hbar}{2m_e}=9.27\times10^{-24}\ \text{A m}^2, \qquad (3.42)
$$

the Bohr magneton, the natural unit of atomic moments ([[Atomic-structure|atomic structure]] uses it; §3.33 needs it). The electron's *spin* moment is almost exactly $\mu_B$ although its spin angular momentum is $\hbar/2$: its gyromagnetic ratio is *twice* (3.41), the "$g=2$" that has no classical explanation and was the first sign that spin is not a spinning ball. Numbers for a laboratory object: a ring of $1\ \mu$C and radius $10$ cm spun at $100$ revolutions per second is a current of $10^{-4}$ A and a moment of $3.1\times10^{-6}$ A m$^2$ — the field at its centre, $\mu_0I/2R=0.6$ nT, is a hundred-thousandth of the Earth's. Rotating charge is a feeble magnet at human scales and the only magnet at atomic ones.

**The field of a rotating charged disc** (a first use of the ring stack): surface density $\sigma$, radius $R$, angular speed $\omega$. The ring between $r$ and $r+dr$ carries $dq=\sigma2\pi r\,dr$, hence current $dI=\sigma\omega r\,dr$, and contributes $\mu_0\,dI/2r=\tfrac12\mu_0\sigma\omega\,dr$ at the centre — the same for every ring:

$$
B_{\text{centre}}=\frac{\mu_0\sigma\omega R}{2}, \qquad (3.43)
$$

and the disc's moment is $\int\pi r^2\,dI=\tfrac14\pi\sigma\omega R^4=\tfrac14Q\omega R^2$ with $Q=\sigma\pi R^2$ — consistent with (3.41) for a disc, whose $L=\tfrac12mR^2\omega$. A rotating uniformly charged *spherical shell* gives a uniform interior field $\tfrac23\mu_0\sigma\omega R$ (Part 10 derives it from the surface current $K=\sigma\omega R\sin\theta$; it is the same calculation as the uniformly magnetised sphere of §3.30).

> [!success] Check
> Dimensions of $Q\omega R^2$: C s$^{-1}$ m$^2$ $=$ A m$^2$ ✓. (3.43) $\to0$ as $R\to0$ ✓ and grows linearly with $R$ — a larger disc at the same $\sigma$ and $\omega$ has more current at every radius, each ring contributing equally.

### 3.29 The magnet as a dipole

Outside a bar magnet the field is that of a solenoid of the same shape: lines leave one end (the *north* pole, the end that seeks geographic north), curve round, and enter the other. From far away it is the dipole field (3.27) with a moment $\mu$ equal to the magnetisation (§3.30) times the volume; a neodymium magnet with $M\approx10^6$ A m$^{-1}$ has $\mu\approx1$ A m$^2$ per cubic centimetre, and a field of order $\mu_0M/2\approx0.6$ T at its face.

**The pole picture** treats the ends as concentrations of "pole strength" $\pm q_m$ with an inverse-square law between poles, $\boldsymbol\mu=q_m\mathbf d$. It is a convenience that works *outside* the magnet, exactly as a two-charge picture works outside an electric dipole, and it is useful: a long thin magnet's end acts like an isolated pole for nearby points, and the torque and energy in an external field come out right. **Inside** it fails: the field $\mathbf B$ inside a magnet runs from the south pole to the north (the lines must close, §3.22), *along* $\boldsymbol\mu$, whereas the pole picture would put a field from north to south. What the pole picture computes inside is $\mathbf H$, not $\mathbf B$ (§3.31) — and the distinction is the reason both symbols exist. **Cut the magnet in half** and each half is a complete magnet with its own two poles: the "poles" were never objects, only the places where the bound currents' field emerges.

> [!abstract] DIAGRAM D16.24 · Bar magnet and solenoid, side by side
> *Show:* a bar magnet and a solenoid of the same shape with identical external field lines; inside the solenoid the lines run along the axis from the "S" end to the "N" end, and the same is drawn inside the magnet; the pole picture's wrong internal arrow shown dashed and crossed out with the label "that is $\mathbf H$, not $\mathbf B$".
> *Search:* "bar magnet versus solenoid field lines equivalence inside field direction south to north"

### 3.30 Magnetisation and bound currents

Matter magnetises when its atomic moments (orbital and spin) acquire a net alignment. The **magnetisation** $\mathbf M$ is the dipole moment per unit volume (A m$^{-1}$). Its field is the field of the atomic current loops, and for uniform $\mathbf M$ those loops add up to a **surface current** only.

**The slab derivation.** A slab of thickness $t$ and area $A$, uniformly magnetised along its normal, is a stack of layers of tiny loops. Inside the slab every loop's current is cancelled by its neighbour's running the other way; only at the rim is there no neighbour, so a net current circulates around the edge. Its size follows from the moment: the slab's total moment is $MAt$ and must equal $I_bA$ for an equivalent single loop around the rim, so $I_b=Mt$ — a current $M$ per unit height of rim:

$$
\mathbf K_b=\mathbf M\times\hat{\mathbf n}, \qquad (3.44)
$$

flowing around the surface, perpendicular to $\mathbf M$ and to the outward normal. A uniformly magnetised cylinder is therefore a solenoid with $nI=M$: inside a long one, $B=\mu_0M$ (3.30); its external field is the solenoid's; its moment is $M\times$ volume — which is why a bar magnet *is* a solenoid, and why cutting it makes two. Where $\mathbf M$ is not uniform the internal cancellation is incomplete and a **volume bound current** $\mathbf J_b=\nabla\times\mathbf M$ remains (stated; not needed for uniform samples). A uniformly magnetised **sphere** has $K_b=M\sin\theta$, the same surface current as a rotating charged shell (§3.28), and its interior field is uniform,

$$
B_{\text{inside}}=\tfrac23\mu_0M \qquad (3.45)
$$

(Part 10 derives it), with a pure dipole field outside — the reason a sphere is the textbook shape for magnetised bodies.

> [!abstract] DIAGRAM D16.25 · Bound currents on a magnetised slab
> *Show:* a slab in section with rows of small atomic current loops all circulating the same way; adjacent loops' shared sides with currents cancelling (drawn as opposing arrows that strike out); the uncancelled current around the rim, labelled $K_b=M$; the same slab redrawn as a single loop of current $I_b=Mt$; beside it a magnetised cylinder drawn as a solenoid.
> *Search:* "magnetisation bound surface current atomic current loops cancel interior slab derivation"

### 3.31 The field inside matter: $\mathbf B$, $\mathbf H$, $\mathbf M$

Ampère's law counts *all* currents, free and bound: $\oint\mathbf B\cdot d\mathbf l=\mu_0(I_{\text{free}}+I_{\text{bound}})$. The bound currents are inconvenient — they depend on the response of the material — so define the **auxiliary field**

$$
\mathbf H\equiv\frac{\mathbf B}{\mu_0}-\mathbf M,\qquad \oint\mathbf H\cdot d\mathbf l=I_{\text{free}},\qquad \mathbf B=\mu_0(\mathbf H+\mathbf M), \qquad (3.46)
$$

whose circulation counts the free currents only (the bound ones are $\oint\mathbf M\cdot d\mathbf l$ and have been subtracted). $\mathbf H$ is what the *free* currents make; $\mathbf M$ is what the material adds; $\mathbf B$ is the total, and it is $\mathbf B$ that exerts forces and $\mathbf B$ whose lines close. In a **linear** material $\mathbf M=\chi\mathbf H$, so

$$
\mathbf B=\mu_0(1+\chi)\mathbf H=\mu_r\mu_0\mathbf H=\mu\mathbf H, \qquad (3.47)
$$

and the three conventions are one number in three dresses: $\chi$ (dimensionless, negative for diamagnets, small positive for paramagnets), $\mu_r=1+\chi$ (what an inductance measurement gives, PART 21), $\mu=\mu_r\mu_0$ (the constant that replaces $\mu_0$ in every formula for a medium-filled geometry). Ferromagnets are not linear; for them $\mu_r$ is a working number that depends on $H$ and on history (§3.34).

**Which field is the applied one?** In a *long* solenoid wound on a core, the circulation of $\mathbf H$ around the usual rectangle is fixed by the winding: $H=nI$ inside, *whatever the core*; then $B=\mu_r\mu_0nI$, and the core multiplies the field by $\mu_r$ — §3.35 shows this is literally extra current on the core's surface. For a *short* sample the ends of the magnetised body carry the bound currents' "return", which produces an $\mathbf H$ inside the sample *opposing* $\mathbf M$: the **demagnetising field**, $\mathbf H_d=-N_d\mathbf M$ with a shape factor $N_d$ ($\tfrac13$ for a sphere, $\to0$ for a long needle along its axis, $\to1$ for a thin plate across it). It is why a short fat magnet holds less magnetisation than a long thin one and why measured $\chi$'s are quoted for long samples; Part 10 uses it.

> [!danger] Trap — quoting the wrong symbol
> "The field inside the core is $\mu_rnI$." Wrong by $\mu_0$: $H=nI$ (A m$^{-1}$) and $B=\mu_r\mu_0nI$ (T). And "a diamagnet has $\mu_r=0$": no — $\mu_r=1+\chi$ with $\chi\sim-10^{-5}$, so $\mu_r=0.99999$; only a superconductor, with $\chi=-1$, has $\mu_r=0$.

### 3.32 Diamagnetism: Lenz's law inside the atom

Every atom has electrons in orbit, and an applied field changes their motion so as to oppose it. Take an electron circling at radius $r$ and angular speed $\omega_0$ under the atom's central force $F_0=m\omega_0^2r$, in a plane perpendicular to an applied $\mathbf B$. The magnetic force $e\omega rB$ is radial and adds to or subtracts from $F_0$ according to the sense of the orbit: $m\omega^2r=F_0\pm e\omega rB$. For $eB/m\ll\omega_0$ the solution is

$$
\omega=\omega_0\pm\frac{eB}{2m}\equiv\omega_0\pm\omega_L, \qquad (3.48)
$$

the **Larmor frequency** $\omega_L=eB/2m$ ($14$ GHz per tesla): orbits of both senses shift their frequency in the direction that makes their *moment* change *against* $\mathbf B$ — the one circulating so as to reinforce the field slows down, the other speeds up. Each electron's moment changes by $\Delta\mu=-\dfrac{e^2r^2}{4m}B$ for an orbit perpendicular to $\mathbf B$, or $-\dfrac{e^2\langle r^2\rangle}{6m}B$ averaged over orientations; with $n$ atoms per unit volume of $Z$ electrons each,

$$
\chi_{\text{dia}}=\mu_0\frac{M}{B}=-\frac{\mu_0nZe^2\langle r^2\rangle}{6m_e}\ \sim\ -10^{-5}, \qquad (3.49)
$$

negative, small, and independent of temperature (the orbits, not their thermal population, respond). For $nZ\sim10^{30}$ m$^{-3}$ and $\langle r^2\rangle\sim(0.1\ \text{nm})^2$, (3.49) gives $-6\times10^{-5}$ — the right size: water $-9\times10^{-6}$, copper $-1\times10^{-5}$, bismuth $-1.7\times10^{-4}$, pyrolytic graphite up to $-4\times10^{-4}$ across its planes. Every material has this contribution; it is *visible* only where there are no permanent moments to swamp it (filled shells: the noble gases, water, most organic matter, copper, gold, bismuth). A superconductor carries the same logic to its limit — surface currents that cancel the applied field completely, $\chi=-1$ — and floats over a magnet (Part 10).

> [!abstract] DIAGRAM D16.26 · The induced moment
> *Show:* two electron orbits of opposite sense in the same applied $\mathbf B$ (into the page), one speeding up and one slowing down, with the change in each orbit's moment drawn as a small arrow *opposite* to $\mathbf B$ in both cases; the net induced $\mathbf M$ antiparallel to $\mathbf B$; a caption "Lenz's law for one atom".
> *Search:* "diamagnetism larmor precession induced magnetic moment opposes applied field orbit diagram"

### 3.33 Paramagnetism: alignment against disorder

Atoms or ions with unpaired electrons carry a permanent moment of order $\mu_B$. In a field each moment has energy $-\boldsymbol\mu\cdot\mathbf B$, lowest when aligned; thermal agitation scrambles the alignment. The simplest honest model is a **two-level** moment that can only point along or against $\mathbf B$ (energies $\mp\mu B$), with populations in the Boltzmann ratio $e^{+\mu B/k_BT}:e^{-\mu B/k_BT}$. The net magnetisation of $n$ such moments per unit volume is

$$
M=n\mu\,\frac{e^{x}-e^{-x}}{e^{x}+e^{-x}}=n\mu\tanh x,\qquad x=\frac{\mu B}{k_BT}. \qquad (3.50)
$$

For $x\ll1$ (every ordinary case: $x=\mu_BB/k_BT=2.2\times10^{-3}$ at $1$ T and $300$ K), $\tanh x\approx x$ and

$$
M=\frac{n\mu^2B}{k_BT},\qquad \chi_{\text{para}}=\frac{\mu_0n\mu^2}{k_BT}=\frac CT, \qquad (3.51)
$$

**Curie's law**: a susceptibility inversely proportional to the temperature (the classical Langevin average over all orientations gives the same form with $\tfrac13$ in place of $1$ — a factor of order one, not a different law). For $n=10^{28}$ m$^{-3}$ and $\mu=\mu_B$ at $300$ K, $\chi\approx3\times10^{-4}$ — ten times a typical diamagnetism, so paramagnets are net attracted, weakly. At $1$ K the same salt has $x=0.67$ at $1$ T, $\tanh x=0.58$: more than half saturated, and Curie's law is failing — which is exactly how adiabatic demagnetisation refrigerators reach millikelvins (Part 10). Metals like aluminium ($\chi=+2\times10^{-5}$) are paramagnetic for a different reason — the conduction electrons' spins, whose susceptibility is temperature-independent (Pauli) because only the electrons near the Fermi level can respond.

> [!tip] FIGURE F16.6 · Alignment of a two-level moment
> *Why:* the curve is Curie's law at the origin and saturation at the end; every "why is the effect weak at room temperature" question is a point near $x=0.002$ on it.
> *Data:* $M/n\mu=\tanh x$ for $x=\mu B/k_BT$ from $0$ to $3$ in steps of $0.25$; the dashed line would be the linear (Curie) law $M/n\mu=x$.

```mermaid
xychart-beta
  title "two-level paramagnet: M / (n mu) against x = mu B / kT"
  x-axis 0 --> 3
  y-axis 0 --> 1.05
  line [0.0, 0.245, 0.462, 0.635, 0.762, 0.848, 0.905, 0.941, 0.964, 0.978, 0.987, 0.992, 0.995]
  line [0.0, 0.25, 0.5, 0.75, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
```

> *Read:* linear with slope $1$ (Curie) until $x\sim0.5$, $90\%$ saturated by $x=1.5$. Room temperature at $1$ T is $x=0.002$ — invisible at this scale; $x=1$ needs $1$ T at $0.7$ K, or $450$ T at room temperature.

> [!warning] Condition of validity
> (3.50)–(3.51) assume independent moments (no interaction between neighbours) and a two-level moment. Interacting moments are ferromagnets (§3.34), and Curie's law applied to iron below its Curie temperature is simply wrong — the paper's standard trap.

### 3.34 Ferromagnetism: exchange, domains and hysteresis

In iron, cobalt, nickel and their alloys, neighbouring atomic moments are locked parallel by the **exchange interaction** — a quantum consequence of the Pauli principle and the Coulomb repulsion between electrons, with an energy of order $0.1$ eV per pair. That is a thousand times the room-temperature $k_BT$ and thirty thousand times the magnetic dipole–dipole energy of two Bohr magnetons at atomic spacing ($\mu_0\mu_B^2/4\pi a^3\approx4\ \mu$eV at $a=0.25$ nm): magnetic forces between the moments are irrelevant, and the alignment is electrostatic in origin (Part 10 turns this into an estimate of the Curie temperature, $T_c\sim J/k_B\sim10^3$ K; iron's is $1043$ K, above which iron is an ordinary paramagnet obeying a Curie–Weiss law $\chi=C/(T-T_c)$). The result is a **spontaneous magnetisation** $M_s$ — $1.7\times10^6$ A m$^{-1}$ for iron, i.e. $B_s=\mu_0M_s=2.1$ T — but organised in **domains**, regions of a few micrometres each fully magnetised in a different direction, arranged so that the sample's external field (and its energy $\int B^2/2\mu_0$) is small. An unmagnetised iron bar is saturated everywhere and magnetised nowhere.

**Magnetising it.** An applied $\mathbf H$ first moves the domain walls (domains aligned with $\mathbf H$ grow at their neighbours' expense — reversible at first, then in jumps as walls snap past defects), then rotates the remaining moments into line, until the whole sample is one domain: **saturation**. Remove the field and the walls do not all return: a **remanent** $B_r$ stays (a permanent magnet). Reverse the field and $B$ falls to zero only at the **coercive** field $-H_c$; carry on to negative saturation and back, and the $B$–$H$ curve is a closed **hysteresis loop**. The material's $\mu_r=B/\mu_0H$ is therefore not a constant but a slope that depends on where you are on the loop — hundreds to tens of thousands for soft iron on the initial curve, meaningless near saturation.

**The loop's area is energy.** Magnetising a unit volume by $dB$ in the presence of $H$ costs the source work $dW=H\,dB$: for a toroidal core of length $\ell$ and area $A$ wound with $N$ turns, the induced EMF is $NA\,dB/dt$ (PART 20's Faraday law, used here in its one-line form), the source's work is $\mathcal EI\,dt=NAI\,dB$, and with $H=NI/\ell$ this is $(H\,dB)(A\ell)$ ✓. Around a complete cycle the work per unit volume is

$$
w_{\text{cycle}}=\oint H\,dB=\text{area of the loop in the }(H,B)\text{ plane}, \qquad (3.52)
$$

dissipated as heat in the domain walls' jumps. A transformer core cycled at $50$ Hz with a loop of $300$ J m$^{-3}$ loses $15$ kW m$^{-3}$ — about $2$ W per kilogram of steel, the "iron loss" that warms every transformer. **Soft** magnetic materials (silicon steel, permalloy, ferrites) have narrow loops: small $H_c$, small area, easily reversed — cores, shields, relay armatures. **Hard** materials (Alnico, ferrite ceramics, NdFeB with $H_c\sim10^6$ A m$^{-1}$ and loop areas of $10^5$–$10^6$ J m$^{-3}$) have wide loops: permanent magnets, which must not be easy to reverse. Heating past $T_c$ or hammering (mechanical shock lets walls move) demagnetises either.

> [!tip] FIGURE F16.7 · A hysteresis loop
> *Why:* the loop is the whole ferromagnetic story — saturation at the ends, remanence where it crosses $H=0$, coercivity where it crosses $B=0$, and its area the loss per cycle.
> *Data:* a model loop, $B/B_s=\tanh(H/H_0\pm H_c/H_0)$ with $H_c/H_0=0.5$, on $H/H_0$ from $-3$ to $3$ in steps of $0.5$; the upper branch is traversed with $H$ decreasing, the lower with $H$ increasing.

```mermaid
xychart-beta
  title "hysteresis: B / Bs against H / H0 (upper branch H falling, lower branch H rising)"
  x-axis -3 --> 3
  y-axis -1.1 --> 1.1
  line [-0.987, -0.964, -0.905, -0.762, -0.462, 0.0, 0.462, 0.762, 0.905, 0.964, 0.987, 0.995, 0.998]
  line [-0.998, -0.995, -0.987, -0.964, -0.905, -0.762, -0.462, 0.0, 0.462, 0.762, 0.905, 0.964, 0.987]
  line [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
```

> *Read:* remanence $B_r=0.46B_s$ (the upper branch at $H=0$), coercivity $H_c=0.5H_0$ (where the upper branch crosses zero), and the enclosed area — here $2\,B_sH_0$ exactly, for this model loop — is the energy lost per unit volume per cycle. A soft material would be a thin sliver hugging the axis; a hard one nearly a rectangle.

> [!abstract] DIAGRAM D16.27 · Domains and the magnetising curve
> *Show:* four stages of a rectangular sample: unmagnetised (four domains closing their flux), wall motion (the favourable domain grown), rotation (moments turning towards $\mathbf H$), saturation (one domain); beneath, the initial magnetisation curve with the three stages marked and the hysteresis loop drawn around it, $B_r$ and $H_c$ labelled, the area shaded; an inset comparing a soft and a hard loop.
> *Search:* "ferromagnetic domains growth rotation saturation hysteresis loop remanence coercivity soft hard"

### 3.35 Materials in circuits: cores, transformers, shields, electromagnets

**A solenoid with a core.** The winding makes $H=nI$ (§3.31); the core magnetises to $M=\chi H$ and, by (3.44), carries a bound surface current $K_b=M$ running the *same way* as the winding's current sheet $K=nI$. Ampère's law with all currents:

$$
B=\mu_0(nI+M)=\mu_0(1+\chi)nI=\mu_r\mu_0nI. \qquad (3.53)
$$

The amplification by $\mu_r$ is not a mystery of the medium: it is extra current, the core's own, added to the coil's. A $1000$-turns-per-metre solenoid at $5$ A gives $6.3$ mT in air; on a soft-iron core with an initial $\mu_r\sim1000$ it would give $6.3$ T — except that iron saturates at $2.1$ T, so the true answer is "about $2$ T and the core is saturated": $\mu_r$ is not a constant, and the saturation field is the ceiling of every iron-core design.

**Transformer cores** must carry a large alternating flux with little loss: soft material (narrow loop, §3.34), high $\mu_r$ (so that a small magnetising current suffices), and *laminations* — thin sheets insulated from one another, because a changing flux drives circulating **eddy currents** in a solid core whose Joule heating would be intolerable (PART 20 derives them; the lamination cuts the loops). **Magnetic shielding** encloses the instrument in a high-$\mu_r$ shell (mu-metal, $\mu_r\sim10^{4}$–$10^{5}$): the field lines prefer the low-reluctance path through the shell's wall and bypass the interior, reducing the inside field by a factor of order $\mu_rt/R$ for a shell of thickness $t$ and radius $R$ — a millimetre of mu-metal on a $10$ cm shell shields by a factor of a few hundred. **An electromagnet** is an iron core with a gap: the circulation of $\mathbf H$ round the magnetic circuit, $H_{\text{iron}}\ell+H_{\text{gap}}g=NI$, with the same $B$ in iron and gap (normal $B$ continuous, §3.26) and $H_{\text{iron}}=B/\mu_r\mu_0$, gives

$$
B\approx\frac{\mu_0NI}{g+\ell/\mu_r}, \qquad (3.54)
$$

so a $5$ mm gap in a $0.5$ m core of $\mu_r=2000$ (effective iron length $0.25$ mm) is what limits the field: the iron merely *guides* the flux to the gap, and $NI=5000$ A-turns gives $1.2$ T there. The read head of a hard disc is a microscopic version; the write head is the same gap run in reverse.

### 3.36 Forces on materials

A magnet brought near an iron nail magnetises it ($\mathbf M$ along the local $\mathbf B$, hugely, because $\mu_r$ is large), and the induced moment is then pulled *towards stronger field* by the gradient force $\nabla(\boldsymbol\mu\cdot\mathbf B)$ of §3.24 — the magnetic version of the comb and the paper scrap. Every para- and ferromagnet is attracted; only iron, cobalt, nickel and their alloys visibly so, because their $M$ is $10^{4}$–$10^{6}$ times a paramagnet's. A diamagnet's induced moment is *anti*parallel to $\mathbf B$ and is pushed towards weaker field: the repulsion is feeble ($\chi\sim-10^{-5}$) but real — a $16$ T magnet with a field gradient of $100$ T m$^{-1}$ levitated a live frog in 1997, because water needs $B\,dB/dz=\mu_0\rho g/\lvert\chi\rvert\approx1400$ T$^2$ m$^{-1}$ to float, and pyrolytic graphite floats over ordinary neodymium magnets.

**How much can a magnet lift?** At the pole face of an electromagnet holding an iron plate, the field $B$ crosses the thin gap; the plate is a boundary that confines the field, and the magnetic pressure of §3.26 acts on it:

$$
F=\frac{B^2}{2\mu_0}A, \qquad (3.55)
$$

with $A$ the total pole area. At $B=1$ T over two poles of $5$ cm$^2$ each: $F=4\times10^5\times10^{-3}=400$ N, a $40$ kg lift from a magnet the size of a fist — and since $B$ cannot exceed iron's $2.1$ T, the lift per unit pole area is capped near $1.8$ MPa ($180$ N cm$^{-2}$), which is why scrap-yard magnets are large in area rather than strong in field. The same (3.55) with the sign reversed is the levitation force on a superconductor (Part 10, the Meissner effect).

> [!abstract] DIAGRAM D16.28 · A magnet and a nail; the lifting electromagnet
> *Show:* a bar magnet's converging field near its pole, an iron nail with its induced moment drawn along the local $\mathbf B$ and the net force arrow towards the pole; a small diamagnetic sample with its induced moment reversed and the force away; beside it a U-shaped electromagnet with an iron bar across its poles, the field crossing the two gaps and the pressure $B^2/2\mu_0$ on each pole face.
> *Search:* "magnet attracts iron nail induced dipole gradient force; electromagnet lifting force B squared A over 2 mu0"

### 3.37 The Earth's field: a tilted dipole, and how to read it

To a first approximation the Earth's field is that of a dipole at its centre, tilted about $11^\circ$ from the rotation axis, of moment $8\times10^{22}$ A m$^2$ (§3.38). Its lines *enter* the Earth in the northern hemisphere: the magnetic pole near the geographic north is a **south** pole of the dipole — which is why it attracts the north-seeking end of a compass. Three angles and two components describe the field at any place:

* **Declination** $\delta$: the angle between the compass direction (magnetic north) and true north, stated east or west. Near-zero along the "agonic" line, $10$–$20^\circ$ in much of North America and Europe's far north, small ($\sim0$–$2^\circ$) across India.
* **Dip (inclination)** $\theta_{\text{dip}}$: the angle by which a freely pivoted needle tilts below the horizontal, positive (north end down) in the northern hemisphere. Zero at the magnetic equator — where a dip needle lies flat — and $90^\circ$ at the magnetic poles, where a compass is useless because the horizontal component vanishes. Across India it runs from roughly $5^\circ$ at the southern tip to about $50^\circ$ in Kashmir.
* **The components:** $B_H=B\cos\theta_{\text{dip}}$ horizontal (what a compass and a tangent galvanometer respond to), $B_V=B\sin\theta_{\text{dip}}$ vertical, $\tan\theta_{\text{dip}}=B_V/B_H$; and $B_H$ splits into $B_H\cos\delta$ towards true north and $B_H\sin\delta$ towards east or west.

> [!example] Worked example — the three components
> At a station the total field is $48\ \mu$T, the dip $60^\circ$ and the declination $5^\circ$ W. Then $B_H=48\cos60^\circ=24.0\ \mu$T, $B_V=48\sin60^\circ=41.6\ \mu$T; north component $24.0\cos5^\circ=23.9\ \mu$T, west component $24.0\sin5^\circ=2.1\ \mu$T, down $41.6\ \mu$T. Check: $\sqrt{23.9^2+2.1^2+41.6^2}=48.0$ ✓. A compass here points $5^\circ$ west of true north; a dip needle rests $60^\circ$ below horizontal; a horizontal needle (compass) feels only $24\ \mu$T of the $48$.

**Measuring it.** A *tangent galvanometer* — a vertical coil in the magnetic meridian with a compass at its centre — deflects the needle by $\theta$ where $B_{\text{coil}}=B_H\tan\theta$; with $B_{\text{coil}}=\mu_0NI/2R$ known, $B_H$ follows (or, with $B_H$ known, $I$). A *dip circle* is a needle pivoted to swing in the vertical meridian plane. And the oscillation method of §3.24 gives $\mu B_H$; combined with the tangent-galvanometer's $B_H$ it gives $\mu$, or combined with a deflection measurement that gives $\mu/B_H$ (a magnet placed to deflect a compass), it gives both — Gauss's 1832 procedure, the first absolute measurement of the Earth's field.

> [!abstract] DIAGRAM D16.29 · The Earth's dipole and the field elements
> *Show:* the Earth with its rotation axis and the dipole axis tilted $11^\circ$, field lines entering in the north (the dipole's "S" near geographic north labelled); a tangent plane at a mid-latitude point with true north, magnetic north (declination $\delta$ between them), the total $\mathbf B$ dipping by $\theta_{\text{dip}}$ below the horizontal, and the components $B_H$, $B_V$, $B_H\cos\delta$, $B_H\sin\delta$.
> *Search:* "earth's magnetic field tilted dipole declination inclination dip horizontal vertical components diagram"

> [!danger] Trap — north is south
> The Earth's magnetic pole in the Arctic is the *south* pole of the Earth's dipole; "the north magnetic pole" names the place, not the polarity. And dip is not declination: one is a tilt below the horizontal, the other a swing from true north.

### 3.38 Magnetism in nature

**The dipole moment from the surface field.** At the magnetic equator the surface field is the dipole's equatorial value, $B=\mu_0\mu/4\pi R_\oplus^3$; with $B\approx30\ \mu$T and $R_\oplus=6.37\times10^6$ m, $\mu=BR_\oplus^3/10^{-7}=7.8\times10^{22}$ A m$^2$ — the "$8\times10^{22}$" of §0.4, a genuine reconstruction of a planetary quantity from a compass reading and a radius (Part 10 asks what current loop in the core would make it). The polar surface field is twice the equatorial, $\sim60\ \mu$T ✓ against the measured range.

**Where it comes from.** Not from a permanent magnet: the core is at $\sim4000$–$6000$ K, far above any Curie temperature. It is a *dynamo* — convection of the liquid iron outer core, organised by the Earth's rotation, carrying electric currents whose field sustains the currents (PART 20's induction is the mechanism). The field **wanders** (the north magnetic pole has moved from Canada towards Siberia at up to $50$ km per year in recent decades) and **reverses** irregularly, on average every few hundred thousand years — the last full reversal was $780{,}000$ years ago — and the reversals are recorded as stripes of alternately magnetised basalt on either side of mid-ocean ridges, where cooling rock froze in the field of its day: the evidence that made sea-floor spreading, and plate tectonics, undeniable. Rocks cooled through their Curie temperature carry a **remanent** magnetisation (§3.34) that points where the field pointed and dips as it dipped, so a rock's *dip* records the latitude at which it formed — palaeomagnetism.

**Outside the planet** the solar wind, a plasma of protons and electrons at $400$ km s$^{-1}$, compresses the dipole field on the day side (the magnetopause at $\sim10$ Earth radii) and draws it into a long tail on the night side; the trapped populations of §3.8 live in the belts between, and the aurorae (§3.12) mark where the loss cone empties into the atmosphere. **Animals** — pigeons, sea turtles, salmon, robins — navigate by the field, some with magnetite crystals, some (it appears) with a light-driven chemical compass in the eye; both are active research, and the physics they must contend with is that the Earth's field is $50\ \mu$T and the thermal energy is $k_BT$: a single Bohr magneton in $50\ \mu$T has $\mu_BB=4.6\times10^{-28}$ J, $10^{7}$ times below $k_BT$, so any biological compass must integrate many moments or exploit a quantum trick. **Reading a magnetic-anomaly map:** local rocks rich in magnetite add their own remanent and induced fields to the dipole's — a few hundred nanotesla typically, several microtesla over ore bodies (the Kursk anomaly deflects compasses by tens of degrees) — and a magnetometer survey of those anomalies is how buried structures, from ore to shipwrecks to archaeological walls, are found.

## Part 4 · Results, limits and the validity ledger

> [!warning] Stage 2 deliverable
> Written in the module's second stage: the boxed results of Part 3 with their conditions of validity and limit checks in one table, the "which formula when" table for sources and forces, and the correspondence chain (finite wire → infinite wire → sheet; loop → dipole; solenoid → sheet pair → toroid; two-level paramagnet → Curie law).

## Part 5 · Worked exemplars

> [!warning] Stage 2 deliverable
> Written in stage 2: concept checks C1–C14 and exemplars E1–E20 at the point of theory they use — force directions with signs, radius and period, a helix, the three-region strip, a mass-spectrometer separation, a cyclotron, a mirror ratio, a Hall probe, a cycloid, Thomson's tube, the square and the hexagon, a compound loop, a finite solenoid, a coaxial cable, the hole in a wire, a torque and a galvanometer, parallel wires, the magnetic pressure, an oscillating magnet, a core and a gap, the Earth's components — each with a collapsible solution and a check.

## Part 6 · Archetypes and practice

> [!warning] Stage 2 deliverable
> Written in stage 2: the archetype table (the union of the mandatory lists of plan.md PARTs 16–19, at least 40 rows) and the practice questions Q1–Q60 with collapsible solutions, each archetype worked once and varied once.

## Part 7 · Toolkit

> [!warning] Stage 2 deliverable
> Written in stage 2: the grip rule and cross products as bookkeeping, the three-region protocol, Ampère versus Biot–Savart, superposition with negative current, the $p=300Br$ rule, energy methods for forces at fixed current, the magnetic-circuit analogy, dimensional and limit checks, and the scaling laws — each with a demonstration and its failure case.

## Part 8 · Traps

> [!warning] Stage 2 deliverable
> Written in stage 2: the trap list of plan.md PARTs 16–19 in the "tempting answer, one-line reply, paper archetype" format — the left hand, the speed that "changes", the loop that does not enclose, $\mu_0/2\pi$ against $\mu_0/4\pi$, the forgotten $N$, the sum of the fields in the parallel-wire force, $v_\parallel$ in the radius, the period against the time in the region, the Hall polarity, $\mathbf B$ against $\mathbf H$, Curie's law for iron, north that is south, dip against declination.

## Part 9 · Playbook

> [!warning] Stage 2 deliverable
> Written in stage 2: the triage tree, the formula map with validity, the constants card, the paper timing plan and the ten-point pre-submission audit.

## Part 10 · Olympiad extension

> [!warning] Stage 3 deliverable
> Written in stage 3: magnetism derived from electrostatics and relativity (the length-contracted wire, with the constant coming out right); the field of a moving charge and Biot–Savart; the finite solenoid by direct integration and the Helmholtz condition $d=R$ with the vanishing second derivative; the rotating charged disc and sphere and the gyromagnetic ratio, with the Bohr magneton; the magnetised sphere's $\tfrac23\mu_0M$; magnetic pressure applied to the solenoid's end, the wire's self-pinch and a levitating superconductor; the two-cylinder uniform field as a design; dipole–dipole forces; the cycloid solved twice; gradient and curvature drifts and the radiation belts' timescales; Fermi acceleration; the relativistic cyclotron and the synchrotron; the betatron's 2:1 condition; the Hall effect with two carrier types; the demagnetising factor; the Meissner levitation estimate; the Curie–Weiss law and the Curie-temperature estimate from the exchange energy; adiabatic demagnetisation; the compass's accuracy near a wire; the heart's field and the SQUID; the Earth's core current; the limits-and-failure section; and OL1–OL12 solved long problems, each with a named method, a numeric answer and two checks.

## Part 11 · Olympiad-grade paper

> [!warning] Stage 3 deliverable
> Written in stage 3: 36 questions, 200 marks, 180 minutes — Section A (12 single-correct, 4 marks), Section B (8 one-or-more-correct, 4 marks), Section C (6 numerical, 5 marks), Section D (10 long-form, 9 marks) — with a coverage map naming the block each question tests and a collapsible solution under every question. It is not on the page yet so that no reader sits a half-built paper.

## Part 12 · Marking scheme and post-paper audit

> [!warning] Stage 3 deliverable
> Written in stage 3 with the paper: the mark distribution summing to 200, the question-to-block map, and the diagnostic table.

## Part 13 · Formula sheet

> [!warning] Stage 3 deliverable
> Written in stage 3: every formula of Parts 3–4 with its validity condition, the right-hand rules of §2.2, the source-law decision table, the material constants and the Earth's elements, laid out for two printed A4 pages.

## Part 14 · Checkpoint and hand-off

> [!warning] Stage 3 deliverable
> Written in stage 3: the 25 "can I do this?" statements with self-scoring, what the next module assumes from this one (the flux through a loop, the motional EMF of §3.27, the force on a current, the field of a solenoid and its energy density for induction, inductance and alternating current; the cyclotron frequency and the Bohr magneton for atomic and nuclear physics; the field momentum for electromagnetic waves), and the open questions the reader is now equipped to attack.
