<a id="section-index"></a>

<a id="top"></a>

_11-page chapter set · JEE Advanced · NSEP · INPhO · IOPT · self-contained — opens with no internet, prints cleanly_

# Current Electricity — first principles to Olympiad

A complete, proof-first treatment of current, resistance, cells, networks, instruments and the physics of real wires. Every formula here is **derived from something you already accept** — charge conservation, Newton's law plus collisions, energy accounting — and every place where a JEE or Olympiad examiner can catch you is marked explicitly. Two ideas do all the work: charge is a ledger, and every real device is a divider wearing a badge.

![A cell driving a lamp through two resistors, with the ledger and the divider annotated](assets/figures/fig-001.svg)

**The whole course in one picture.** A source that pumps and taxes, resistances that divide, and a load that takes what the divider allows. Chapter 3 owns the pump, chapter 4 the network, chapter 5 the replacement of everything left of the lamp by two numbers — and the audit line at the bottom is the habit that turns solves into marks.

### How these notes are organised

Each chapter builds only on the ones before it. Chapters **1–3** are the conceptual base: what current is, what resistance is, and what a battery actually sells. Chapters **4–6** are the JEE-Advanced engine: Kirchhoff and symmetry, the network theorems, and the instruments built from them. Chapter **7** is the Olympiad extension (scaling laws, transmission, thermoelectricity, superconductors). Chapter **8** consolidates a solving strategy; chapters **9–10** are the full paper with detailed solutions; chapter **11** is a printable formula sheet.

- Chapter 1 **[Current, drift & continuity](#section-01-current-and-drift)** Compute drift speeds, derive $\sigma=ne^{2}\tau/m$, and explain why the lamp lights while the electrons crawl.

- Chapter 2 **[Resistance & materials](#section-02-resistivity-and-materials)** Integrate $R=\int\rho\,dl/A$ over any geometry and predict metal vs semiconductor temperature behaviour from mechanism.

- Chapter 3 **[EMF, cells & the power audit](#section-03-emf-and-cells)** Model any real source, choose cell groupings, and close every circuit with a balanced joule ledger.

- Chapter 4 **[Kirchhoff & bridges](#section-04-kirchhoff-and-bridges)** Solve any two-loop circuit with sign discipline, crack cubes, bridges and ladders by symmetry, and run an RC circuit through its single time constant.

- Chapter 5 **[Network theorems](#section-05-network-theorems)** Replace any linear network by two numbers (Thevenin/Norton) and know exactly when each theorem is illegal.

- Chapter 6 **[Instruments & measurement](#section-06-instruments-and-measurement)** Convert one galvanometer into any meter, quantify loading error, and measure EMF without stealing current.

- Chapter 7 **[Advanced topics](#section-07-advanced-topics)** Derive fuse and transmission scaling laws, handle thermocouples and thermistor stability, and tame superconducting ledgers.

- Chapter 8 **[The playbook](#section-08-playbook)** Triage any problem in twenty seconds, execute the twelve moves, dodge the named traps, survive the timed drill.

- Chapter 9 **[The Olympiad paper](#section-09-olympiad-paper)** Sit 36 questions in three hours — 245 marks, INPhO standard, JEE format, every chapter examined.

- Chapter 10 **[Solutions to the paper](#section-10-olympiad-solutions)** Mark yourself with principle-first solutions, marks distributed as printed, and a check in every answer.

- Chapter 11 **[The formula sheet](#section-11-formula-sheet)** Print the whole course on three A4 pages the night before — including the traps and the numbers to own.

> **Exam note**
>
> JEE Advanced and Main draw this topic from three syllabus lines: Ohm's law with drift velocity and relaxation time, Kirchhoff's laws with Wheatstone bridge and potentiometer, cells, internal resistance and combinations, and the RC time constant (kept in this chapter, as Cengage does, in §4.6). The Olympiad track (NSEP → INPhO) adds the estimation culture — fuses, transmission, thermoelectric EMFs, superconducting persistence — which is chapter 7's whole content, and expects the audit-and-check discipline of chapter 8 in every long answer. The paper of chapter 9 is set to that joint standard: sections A–C in JEE format, section D at INPhO length.

<a id="cengage-coverage"></a>

### Cengage coverage map — the floor this chapter is built on

The specification for this note-set was **at least everything in the Cengage chapter**, plus the Olympiad material that chapter does not reach. The Cengage volume's *Electric Current and Circuits* is chapter 5, *Electrical Measuring Instruments* is chapter 6 and *Heating Effects of Current* is chapter 7; every numbered contents entry of those three chapters is mapped below. Nothing is missing and nothing is merely named: where a row says "derived", the derivation is in the text, and where it says "extended", the extension goes past the book.

| Cengage section | Where it is here | How it is treated |
| --- | --- | --- |
| 5.2 Electric current; statement of Ohm's law | §1.1, §1.4 | current as a flux; Ohm's law *derived* from $\sigma=ne^{2}\tau/m$, not quoted |
| 5.3 Current density | §1.2 | $\vec J = ne\vec v_d$, continuity equation $\nabla\cdot\vec J+\partial\rho/\partial t=0$ derived for the 1-D wire case |
| 5.5 Drift velocity; relation between drift velocity and current | §1.3 | random-plus-drift picture, $I=neAv_d$, numerical crawl speeds (mm/s), the AC-cycle displacement |
| 5.6 Structural model for an electrical conductor | §1.4 | relaxation time $\tau$ from collisions; the model's three assumptions stated and tested |
| 5.7 Mobility | §1.4 (box *Mobility*) | $\mu=v_d/E=e\tau/m$, units, $\sigma=ne\mu$, two-carrier (electron + hole) form |
| 5.8 Temperature coefficient of resistivity; temperature coefficients of resistance; finding the coefficient | §2.3 | $R_T=R_0[1+\alpha\Delta T]$ with $\alpha$ derived from mechanism for metals and semiconductors; measurement method and the sign of $\alpha$ |
| 5.9 Validity and failure of Ohm's law | §2.4 | the non-ohmic three (diode, filament, electrolyte/gas) with the $I$–$V$ shapes |
| 5.10 Electromotive force and potential difference; $E$ versus $V$ | §3.1 | emf as work per unit charge of the *pump*, terminal voltage under load, the zero-current measurement problem |
| 5.11 Internal resistance of a cell | §3.2 | $V=\mathcal E-Ir$, the $V$–$I$ line, short-circuit current, efficiency |
| 5.11 Combination of resistances: series, parallel | §4.2 | derived from charge and loop conservation, with the conditions each rule needs |
| 5.12 Voltage divider; current divider for two and for three resistances | §4.2 | two-resistor forms *and* the general conductance form $I_k=I\,G_k/\sum G$ (box *The general divider*), with the loading caveat |
| 5.13 Calculation of effective resistance | §4.2–§4.5 | cube, balanced bridge, unbalanced bridge by node equations, Δ–Y, infinite ladders |
| 5.13 Kirchhoff's laws for electrical networks | §4.1 | both laws with the sign discipline, plus the nodal form that scales to any number of loops |
| 5.17 Wheatstone bridge; balanced bridge | §4.3, §6.3 | balance derived by symmetry and by loop equations; the meter bridge as its laboratory form |
| 5.20 Combination of cells: series, parallel, mixed | §3.3 | all three groupings with the mismatched-cell warning and the maximised current condition |
| 5.21 Superposition principle; concepts | §5.1 | stated with its linearity condition, used, and the theorem-based alternative given |
| 5.25 Charging and discharging of a capacitor through a resistance | §4.6 | *new section*: $q=Q_0(1-e^{-t/RC})$ and $q=Q_0e^{-t/RC}$ derived from Kirchhoff, with the half-life and the 63%/5σ milestones |
| 5.26 Charging of the capacitor — other approach | §4.6 | the final/initial-value (Thévenin) route: $q(t)=q_\infty-(q_\infty-q_0)e^{-t/\tau}$ |
| 5.30 Equivalent time constant | §4.6, and capacitors note-set §6 | $\tau=R_{\text{Th}}C$ for a network; two-capacitor networks with n states and n time constants are worked in the sister note-set |
| 5.32 Solved examples; exercises (subjective, objective, multiple-correct, assertion–reasoning, comprehension, matching, integer) | §1.6, §2.5, §3.5, §6.5, §7.6, §8.5 and the paper (ch 9) | in-chapter questions after every chapter with folded full solutions; the paper's seven sections mirror the Cengage exercise types |
| 6.2–6.3 Galvanometer, ammeter, voltmeter | §6.1, §6.2 | one galvanometer turned into any meter; loading error quantified; the ideal-meter limits |
| 6.4–6.6 Potentiometer: construction and uses | §6.4 | null measurement, internal-resistance and emf comparison, sensitivity, the wire's uniform-potential-drop assumption |
| 6.7–6.8 Meter bridge (slide wire bridge): construction, checking of connections | §6.3 | balance, end-error correction, and the two-way check (interchange the gaps and confirm the balance point moves the other way) that catches wrong connections |
| 7.2 Heat produced by an electric current; cause of heating | §3.4, §7.1 | $P=I^{2}R$ from the joule ledger; the fuse's steady-state balance as the worked scaling law |
| 7.2 Electric power produced in the circuit; units of electric energy and electric power | §3.4 (box *Units ledger*) | watt, joule, the commercial unit kWh and its cost arithmetic, the eV, and the $I^{2}R$/$V^{2}/R$ trap |
| 7.5 Maximum power transfer theorem | §5.4 | derived from Thévenin, with the efficiency at that point (50%) and the reason a power utility does not want it |
| 7.5 Some applications | §7.1–§7.5 | bulbs in series and parallel and the rated-voltage trap, heaters, fuses, filament inrush, thermistors, thermocouples, superconductors |

> **Beyond the Cengage floor — the Olympiad layer**
>
> Chapters 5 and 7 exist to take the same physics past the book: Thévenin, Norton, reciprocity and compensation theorems with their legality conditions; symmetry folding for cubes and ladders; the four-terminal Kelvin measurement; thermoelectric Seebeck/Peltier coefficients with the Thomson relation; the semiconductor thermistor's self-consistent operating point; superconducting persistence and critical fields; and the estimation culture (transmission-line loss scaling, fuse-current scaling $I\propto r^{3/2}$) that NSEP and INPhO reward. The paper of chapter 9 is set to that joint standard.

> **How to study this set**
>
> Read chapters 1–3 with a pen and recompute every number (they are all checkable by hand). Do the in-chapter questions *before* opening their solutions. Chapters 4–5 are the engine room: do every question twice, once by nodal slog and once by theorem, and make the two agree. Then chapter 8, then the paper under the clock. The formula sheet is for the week after the paper — it consolidates what you now understand; it cannot substitute for it.

Start with [**Chapter 1 →**](#section-01-current-and-drift).

<a id="section-01-current-and-drift"></a>

_Chapter 1 of 11 · JEE Advanced · base · ≈ 45 min read · 8 questions_

## Current, drift and the ledger of charge

Every circuit you will ever solve is a bookkeeping problem: charge is never created or destroyed, it only moves, and it moves because a field pushed it. After this chapter you can say precisely what current *is*, compute how fast the electrons in a wire actually crawl, and derive — not quote — why a metal that obeys Newton plus collisions obeys Ohm's law. The mistake this chapter exists to kill is the picture of electrons sprinting through wires at the speed of light.

### 1.1 Current: a flux, not a vector

> **Definition · electric current**
>
> Current through a surface is the **rate at which charge crosses that surface**:
>
>  $$
> I=\frac{dq}{dt},\qquad 1\ \text{A}=1\ \text{C s}^{-1} \tag{1.1}
> $$
>
>  The defining surface is part of the definition — "the current in the wire" always means "through a cross-section cutting the wire". Current is a **scalar**. It has a direction of flow, but it does not add like a vector: two currents of 2 A and 3 A crossing the same surface in the same sense give 5 A, regardless of the angle between the wires they flow in.

> **Why current cannot be a vector**
>
> A vector quantity adds by the parallelogram law. Test it: bend a wire so two segments meet at a right angle, carrying 2 A and 3 A into the same junction. The current leaving is 5 A — the *sum* — not $\sqrt{2^{2}+3^{2}}=3.6$ A. What is vectorial is the **current per unit area** at a point, the current density $\vec j$ of §1.2, and the total current is its flux through the surface, $I=\int\vec j\cdot d\vec a$. A flux is a scalar; the arrow lives in the surface's orientation. This is the same move as in magnetostatics, where $\oint\vec B\cdot d\vec a$ counts field lines, not vectors.

The sign convention: current is drawn in the direction **positive** charge would move, even in a metal where the movers are electrons going the other way. The convention costs nothing — the field, the current density and the energy flow all come out consistent — but every arrow you draw in a circuit commits you to it. Electrons in a wire move opposite to $\vec j$; a positive ion, a hole, or an ion in electrolyte may move along it. The ledger does not care who carries the charge:

$$
I=\sum_s n_s q_s A v_s \quad\text{(one line per carrier species)} \tag{1.2}
$$

### 1.2 Current density and the continuity equation

> **Definition · current density**
>
> $\vec j$ at a point: carriers of charge $q$, number density $n$, mean (drift) velocity $\vec v$ give
>
>  $$
> \vec j=nq\vec v\qquad\big[\text{A m}^{-2}\big] \tag{1.3}
> $$
>
>  valid pointwise, for each carrier species, with the **mean** velocity — not the instantaneous velocity of any one electron. Current is the flux: $I=\int_S\vec j\cdot d\vec a$, and for a uniform $\vec j$ across a plane surface of area $A$, $I=jA$.

Now the bookkeeping law. Charge inside a fixed volume can change in exactly one way: charge crosses the boundary. This is nothing but conservation of charge, written locally:

$$
\vec\nabla\cdot\vec j=-\frac{\partial\rho}{\partial t}\qquad\text{(continuity equation)} \tag{1.4}
$$

> **Why the node rule follows from it**
>
> A circuit node is a small volume with no capacity to store charge — the metal and the junction are perfect conductors, so any attempt to accumulate charge there would build a field that instantly sweeps it away ($\tau$ of §1.4 is $10^{-14}$ s). So $\partial\rho/\partial t=0$ inside the node, the continuity equation gives $\vec\nabla\cdot\vec j=0$, and integrating over the node's surface leaves $\sum I_{\text{in}}=\sum I_{\text{out}}$: **Kirchhoff's junction law is charge conservation, not a new law of nature** (chapter 4 uses it as step one of every network solve).

![Current as charge flux through two cross-sections of a wire, with the segment between them storing none in steady state](assets/figures/fig-002.svg)

**Fig. 1.1 — Steady state means every cross-section passes the same current.** If $I_2>I_1$ the segment would pile up charge until its field corrected the flow; that correction time is $10^{-14}$ s, which is why series elements carry equal currents without exception.

![Same current density crossing a flat surface and a tilted surface: flux scales with cos theta](assets/figures/fig-003.svg)

**Fig. 1.2 — Current is the flux of $\vec j$, so tilt costs a factor of $\cos\theta$.** The wires meeting at an angle in a junction do not add like vectors, yet each *surface* they cross feels $\vec j\cdot\hat n$ — the scalar flux view keeps both facts straight.

### 1.3 Drift: what the electrons are actually doing

Put a field $\vec E$ along a copper wire. Each conduction electron feels $-e\vec E$, accelerates for a short time, collides with a lattice vibration or defect, loses its directed memory, and starts again. The net result is a slow systematic crawl — the **drift velocity** $\vec v_d$ — superimposed on a huge random thermal motion that transports no charge at all on average.

> **Definition · drift velocity**
>
> $\vec v_d$ is the **average** velocity of the carriers, averaged over the enormous number inside any small volume. It is the only part of their motion that survives the average; the thermal part, $\sim10^{5}$–$10^{6}$ m s⁻¹, cancels because it points randomly in all directions.

![Zig-zag electron path: random thermal motion with a slow drift to the left along the field of the wire](assets/figures/fig-004.svg)

**Fig. 1.3 — One collision-rich trajectory and its mean.** The instantaneous speed is set by temperature; the *displacement per second* is set by the field. Signal speed and carrier speed are different quantities — confusing them is the classic error this chapter exists to prevent.

> **The number that recalibrates your intuition**
>
> 1 A in copper of cross-section 1 mm²: worked out in §1.5, the drift speed is $7\times10^{-5}$ m s⁻¹ — about **26 cm per hour** — while the random speed of the same electrons is $\sim10^{6}$ m s⁻¹. The ratio is $10^{-10}$. A wire carries a large current while its electrons barely relocate; the energy travels in the field at nearly light speed (§1.5), not in the electron cargo.

### 1.4 From collisions to Ohm's law

Here is the derivation that turns Newton's second law plus one statistical assumption into the microscopic form of Ohm's law. Assume each electron, after every collision, starts with zero *mean* velocity, and the average time between collisions is the relaxation time $\tau$.

> **The one-step derivation**
>
> Between collisions an electron accelerates: $a=eE/m$. Just before a collision its directed velocity is $eE\tau/m$, just after it is 0; averaged over the cycle the directed velocity is the **mean of 0 and the final value**:
>
>  $$
> v_d=\frac{eE\tau}{2m}\quad\text{(cycle average)},\qquad \vec j=ne\vec v_d\ \Rightarrow\ \vec j=\frac{ne^{2}\tau}{2m}\vec E \tag{1.5}
> $$
>
>  With the more careful exponential average (velocity decays as $e^{-t/\tau}$ after each collision) the factor $1/2$ disappears: $v_d=eE\tau/m$ and
>
>  $$
> \boxed{\vec j=\sigma\vec E},\qquad \sigma=\frac{ne^{2}\tau}{m},\qquad \mu=\frac{v_d}{E}=\frac{e\tau}{m} \tag{1.6}
> $$
>
>  The exponential argument is the honest one — after a collision the electron's directed velocity decays continuously, it does not stay at zero for half the interval — but both routes give the same **structure**: conductivity is set by how many carriers there are ($n$) and how long they remember the field ($\tau$). Chapter 2 lives off that structure: cool the metal and $\tau$ grows, so $\sigma$ grows; heat a semiconductor and $n$ explodes, so $\sigma$ grows for a different reason.

> **The trap in this section**
>
> Writing "the electrons accelerate steadily, so $v$ grows without bound" in a wire carrying a steady current. The reply: collisions reset the directed velocity every $\sim10^{-14}$ s; $v_d=eE\tau/m$ is a **terminal** velocity, the electrical twin of a raindrop's fall through air. The acceleration picture is only valid between collisions, never across them.

### Worked example 1.1 · Drift numbers for a laboratory wire

Copper: $n=8.5\times10^{28}\ \text{m}^{-3}$, $\rho=1.7\times10^{-8}\ \Omega$m. A wire of cross-section 1 mm² carries 1 A. **Plan:** convert the macroscopic current into a carrier bookkeeping statement, then use $\sigma=ne^{2}\tau/m$ backwards to find $\tau$.

 **Do:** $v_d=I/(neA)=1/\big(8.5\times10^{28}\times10^{-6}\times1.6\times10^{-19}\big) =7.4\times10^{-5}$ m/s — 26 cm per hour. From $\tau=m/(ne^{2}\rho)= 9.11\times10^{-31}/\big(8.5\times10^{28}\times(1.6\times10^{-19})^{2}\times1.7\times10^{-8}\big) =2.5\times10^{-14}$ s. The electrons' Fermi speed is $\sqrt{2E_F/m}\approx1.6\times10^{6}$ m/s (for $E_F\approx7$ eV), so the mean free path is $v_F\tau\approx4\times10^{-8}$ m ≈ 40 nm — about 150 atomic spacings, which is why metals conduct so well: an electron sails past many atoms before scattering. **Check:** the drift-to-thermal ratio $7.4\times10^{-5}/1.2\times10^{5}\approx6\times10^{-10}$ — the drift is a whisper on top of a storm, exactly as Fig. 1.3 shows.

> **Mobility — the carrier's obedience rating**
>
> Define the **mobility** as the drift speed a carrier acquires per unit driving field:
>
>  $$
> \mu\equiv\frac{v_d}{E}= \frac{e\tau}{m}\qquad[\,\mu\,]= \frac{\text{m s}^{-1}}{\text{V m}^{-1}}=\text{m}^{2}\text{V}^{-1}\text{s}^{-1} \tag{1.7}
> $$
>
>  It is the third way of writing the same physics — $n$ says how many carriers there are, $\tau$ how long each remembers the field, and $\mu$ packages the two into "how fast does one carrier end up moving". Multiplying back gives the form used for real materials, including those with two carrier species:
>
>  $$
> \sigma=ne\mu\qquad\text{and for two species}\qquad \sigma=e\left(n\mu_e+p\mu_h\right) \tag{1.8}
> $$
>
>  Numbers worth knowing: in copper $\mu\approx4.4\times10^{-3}$ m²V⁻¹s⁻¹ (from $\tau\approx2.5\times10^{-14}$ s); in silicon at 300 K, $\mu_e\approx0.14$ and $\mu_h\approx0.05$ m²V⁻¹s⁻¹ — ten to thirty times larger than in a metal, because carriers scatter far less often. What silicon lacks is carriers: $n\sim10^{16}$ m⁻³ against copper's $8.5\times10^{28}$. **High mobility with almost no carriers still means a poor conductor** — which is exactly why doping works: it leaves the mobility roughly alone and multiplies $n$ by a million. Raising the temperature *lowers* $\mu$ in both materials (more lattice vibration, smaller $\tau$); whether the resistance rises or falls is then decided by whether $n$ is fixed (metal: resistance rises) or thermally liberated (semiconductor: resistance falls).

### 1.5 The field travels, not the electrons

> **Why the lamp lights at once if the electrons crawl**
>
> Close a switch 3 m from a lamp. The electrons *at the lamp filament* are already there, and so is the field apparatus: charges on the switch, the wires and the battery establish an electric field throughout the circuit at the speed of light. The electrons *everywhere along the wire* begin drifting within $L/c\approx10^{-8}$ s of the switch closing — long before any electron from the switch could arrive (that journey would take $3/7\times10^{-5}\approx12$ hours). What propagates is the **field and the instruction to move**; the carriers are a standing crowd. This is also why circuit theory works as an instantaneous theory: a circuit of size $L$ settles in $L/c$, vastly shorter than any timescale a battery-and-resistor problem cares about. (The proper statement — circuit size $\ll$ wavelength — returns in chapter 7.)

> **Alternating current, seen from the electron's seat**
>
> Mains at 50 Hz: the drift velocity itself oscillates with period 20 ms. With $I_0=5$ A in our 1 mm² wire, the drift amplitude is $v_{d,0}/\omega=3.7\times10^{-4}/314\approx1.2\ \mu$m. The electron cloud of your house wiring merely trembles by a micrometre, 50 times a second — while delivering kilowatt-hours through the field. Any exam question of the form "how far does an electron move in one AC cycle" is this two-line calculation.

![When the switch closes the field is established everywhere within L over c, so every electron starts drifting at once](assets/figures/fig-005.svg)

**Fig. 1.4 — What crosses the circuit at light speed is the instruction, not the carriers.** All electrons between switch and lamp begin drifting together the moment the field reaches them; no electron needs to travel the route for the lamp to light.

### 1.6 Questions

### **Q1** A current of 4.8 A flows in a silver wire. How many electrons cross a given cross-section each second, and does the answer change if the wire is thicker? _(JEE main)_

<details>
<summary>Solution</summary>

$N=I/e=4.8/(1.6\times10^{-19})=3.0\times10^{19}$ electrons per second.

The count depends **only on the current**, not on the wire's thickness or material: it is the definition $I=dq/dt$, divided by $e$. What changes with thickness is the *speed* of the drift ($v_d=I/neA$ — more carriers on the starting line, so each need move slower) and the current density $j=I/A$. **Check:** one ampere is famously $\sim6\times10^{18}$ electrons/s; 4.8 A gives 4.8× that ✓.

</details>

### **Q2** Two wires of the same material, cross-sections 2 mm² and 0.5 mm², are joined end to end and carry the same current. Find the ratio of drift velocities and of current densities in the two sections, and say which quantity is the same in both. _(JEE main)_

<details>
<summary>Solution</summary>

Series elements carry **equal current** (Fig. 1.1 — the junction cannot store charge). So $I=n e A_1v_1=n e A_2v_2$ and

$$
\frac{v_2}{v_1}=\frac{A_1}{A_2}=\frac{2}{0.5}=4,\qquad \frac{j_2}{j_1}=\frac{I/A_2}{I/A_1}=\frac{A_1}{A_2}=4
$$

The same in both wires: the **current** $I$ (and, being the same material, the field-to-current relation through $\sigma$). Different: $v_d$ and $j$, each 4× larger in the thin wire. **Check:** narrowing a pipe raises speed and pressure-drop per metre together — the hydraulic analogy gives the same 4× ✓.

</details>

### **Q3** A conductor contains two carrier species: electrons of density $n$, mobility $\mu_e$, and holes of density $p$, mobility $\mu_h$. Show the conductivity is $\sigma=e(n\mu_e+p\mu_h)$ and evaluate it for $n=p=10^{16}\ \text{m}^{-3}$, $\mu_e=0.14$, $\mu_h=0.05$ m²V⁻¹s⁻¹. _(JEE advanced)_

<details>
<summary>Solution</summary>

Mobility is drift velocity per unit field: $v_e=\mu_eE$ (against $\vec E$) and $v_h=\mu_hE$ (along it). Both species carry **positive** current along $\vec E$ — the electron's negative charge cancels its backward motion — so the densities add:

$$
\vec j=e n\mu_e\vec E+e p\mu_h\vec E=e(n\mu_e+p\mu_h)\vec E
$$

Numbers: $\sigma=1.6\times10^{-19}\times(0.14+0.05)\times10^{16}=1.6\times10^{-19}\times1.9\times10^{15} =3.0\times10^{-4}$ S/m. **Check:** a million times less than copper's $5.9\times10^{7}$ S/m — consistent with a doped semiconductor, whose carriers are $10^{12}$ times fewer but mobility only ~100× worse ✓. The sign subtlety is the whole point: **mobility is a magnitude**; the current of a negative carrier is along $\vec E$ regardless.

</details>

### **Q4** Estimate the relaxation time $\tau$ for conduction electrons in aluminium, given $\rho=2.7\times10^{-8}\ \Omega$m and $n=1.8\times10^{29}\ \text{m}^{-3}$, and the distance an electron travels between collisions. _(JEE advanced · estimation)_

<details>
<summary>Solution</summary>

$$
\tau=\frac{m}{ne^{2}\rho}=\frac{9.11\times10^{-31}}{1.8\times10^{29}\times(1.6\times10^{-19})^{2}\times2.7\times10^{-8}} =\frac{9.11\times10^{-31}}{1.246\times10^{-16}}\approx7.3\times10^{-15}\ \text{s}
$$

With Fermi speed $\sqrt{2E_F/m}\approx\sqrt{2\times11\times1.6\times10^{-19}/9.11\times10^{-31}} \approx2.0\times10^{6}$ m/s (Al: $E_F\approx11$ eV), the step per collision is $v_F\tau\approx1.5\times10^{-8}$ m ≈ 15 nm. **Check:** copper gave $2.5\times10^{-14}$ s and 40 nm (§1.4); aluminium's slightly higher $n\rho$ product must shorten both — and it does, by a factor of ~3 ✓. **Order of magnitude to own:** $\tau\sim10^{-14}$ s, free path $\sim10$–$40$ nm in any ordinary metal.

</details>

### **Q5** In a lightning stroke a current of $2\times10^{4}$ A flows through a channel of radius 2 cm. Find the current density and the electron drift speed, treating the channel as air at breakdown with $n\approx10^{16}$ free electrons per m³. Comment on what the answer is telling you. _(Olympiad · estimation)_

<details>
<summary>Solution</summary>

$$
A=\pi(0.02)^{2}=1.26\times10^{-3}\ \text{m}^{2},\quad j=\frac{2\times10^{4}}{1.26\times10^{-3}}=1.6\times10^{7}\ \text{A m}^{-2}
$$

$$
v_d=\frac{j}{ne}=\frac{1.6\times10^{7}}{10^{16}\times1.6\times10^{-19}}=1.0\times10^{10}\ \text{m s}^{-1}
$$

That is **33 times the speed of light** — impossible, so the assumption that fails is the carrier density. A lightning channel is a fully ionised, avalanche-multiplied plasma with effective carrier densities nearer $10^{22}$–$10^{23}$ m⁻³ (and it grows as the stroke develops), which brings $v_d$ back to $\sim10^{3}$–$10^{4}$ m/s. **The lesson:** drift-speed bookkeeping is also a consistency test — when $v_d=c$ pops out, your $n$ was wrong, not relativity. Examiners set this exactly to see who notices.

</details>

### **Q6** A student says: "In an AC circuit the electrons shuttle back and forth, so over one full cycle no charge is transported — hence no energy is delivered by the current." Locate the error. _(concept)_

<details>
<summary>Solution</summary>

The premise is right (net transported charge per cycle is zero — Q's insight box: the amplitude is micrometres); the conclusion confuses **charge transport** with **energy transport**. Energy flow is set by $P=I^{2}R$ at every instant, and $I^{2}$ is positive on both halves of the cycle: the source does work on the electron gas twice per cycle, the lattice takes it as heat, and the direction of drift is irrelevant. Equivalently, the field does work at the rate $\vec j\cdot\vec E$ per unit volume, and this too is positive whenever current and field are aligned — which they are, in both polarities. Zero *net* charge and nonzero *delivered* energy coexist without contradiction.

</details>

### **Q7** A copper wire and an aluminium wire of the same length and the same cross-section carry the same current. Find the ratio of drift velocities, given $n_{\text{Cu}}=8.5\times10^{28}$, $n_{\text{Al}}=1.8\times10^{29}\ \text{m}^{-3}$. _(JEE main)_

<details>
<summary>Solution</summary>

$$
\frac{v_{\text{Cu}}}{v_{\text{Al}}}=\frac{n_{\text{Al}}}{n_{\text{Cu}}} =\frac{1.8\times10^{29}}{8.5\times10^{28}}=2.1
$$

Aluminium packs **more** conduction electrons per m³ than copper (it contributes ~3 per atom at molar volume smaller per electron), so its electrons drift *slower* for the same current. **Check:** aluminium's higher resistivity despite the larger $n$ (§1.4: $\sigma=ne^{2}\tau/m$) pins the difference on a shorter $\tau$, not on carrier supply — a distinction JEE likes to probe ✓.

</details>

### **Q8** A steady current flows in a toroidal (doughnut-shaped) superconducting ring. Using the continuity equation, explain (i) why the current can persist without a battery, and (ii) what the continuity equation alone does *not* tell you about the current. _(Olympiad · concept)_

<details>
<summary>Solution</summary>

(i) The continuity equation in steady state demands $\vec\nabla\cdot\vec j=0$: the field lines of $\vec j$ neither start nor end anywhere — they close on themselves around the ring. Nothing in charge conservation requires a source to keep such a closed loop going; it only requires that nothing *destroys* the directed motion. In an ordinary metal, collisions destroy it in $\tau\sim10^{-14}$ s unless a field feeds it; in a superconductor the carriers scatter elastically with zero resistance, so once launched, the loop current runs for times of order $L/R$ that exceed the age of the universe (chapter 7 puts numbers on this).

(ii) The continuity equation is **one scalar equation per point**: it constrains the divergence of $\vec j$, not its value. Whether the ring carries 1 A or 1000 A, and what sets that number (flux quantisation, inductance, the initial condition), are questions the ledger cannot answer. Conservation tells you what cannot change in transit; it never tells you how much is in transit.

</details>

### 1.7 Chapter summary — the results to own

> **The ledger and the crawl**
>
> $$
> I=\int\vec j\cdot d\vec a,\qquad \vec j=\sum n_sq_s\vec v_s,\qquad \vec\nabla\cdot\vec j=-\frac{\partial\rho}{\partial t}
> $$
>
>  $$
> \vec j=\sigma\vec E,\qquad \sigma=\frac{ne^{2}\tau}{m},\qquad v_d=\frac{I}{neA},\qquad \mu=\frac{e\tau}{m}
> $$
>
>  Current is a flux through a named surface — a scalar. The junction law is the steady-state continuity equation. Drift speed is a terminal velocity set by collisions: $\sim0.1$ mm/s in house wiring, against thermal speeds $10^{10}$ times larger. Signals travel at field speed ($\sim c$), not carrier speed.

### 1.8 Checkpoint

- I can say why current is a scalar while current density is a vector, and demonstrate it with a bent wire.
- I can derive $\sigma=ne^{2}\tau/m$ from Newton's law plus one collision assumption, and name the assumption.
- Given any three of $I, n, A, v_d$ I can produce the fourth, with units, in under a minute.
- I can explain to a sceptic why a lamp 3 m from a switch lights in nanoseconds while its electrons move centimetres per hour.
- I can estimate $\tau$ and the mean free path for a metal from its resistivity, and sanity-check both.

Next: [**Chapter 2 · Resistance, resistivity and real materials →**](#section-02-resistivity-and-materials) — the same physics turned into a property of stuff, and what happens when the stuff refuses to obey.

<a id="section-02-resistivity-and-materials"></a>

_Chapter 2 of 11 · JEE Advanced · core · ≈ 45 min read · 8 questions_

## Resistance, resistivity and real materials

Chapter 1 gave you the microscopic law $\vec j=\sigma\vec E$. This chapter converts it into the number a circuit actually feels — **resistance** — and then asks the question examiners actually test: *when does that number stay fixed?* After it you can compute the resistance of any geometry by field integration, predict how metals and semiconductors respond to temperature *for different microscopic reasons*, and recognise the four non-ohmic devices on sight. The mistake this chapter prevents: quoting $R=\rho l/A$ for a conductor whose cross-section changes along its length.

### 2.1 Resistance: the lump, defined

> **Definition · resistance**
>
> For a two-terminal conductor, $R=V/I$ where $V$ is the potential difference between the terminals and $I$ the current through them. Unit: ohm, $\Omega$. The reciprocal is conductance $G=1/R$ in siemens (S). This definition is **always** valid — for a diode too — but it is a *ratio measured at an operating point*; calling it "the resistance" as if it were a constant is an extra assumption called Ohm's law (§2.5).

> **Why $R=V/I$ is a property of the conductor alone — sometimes**
>
> In a linear material, $\vec j=\sigma\vec E$. The potential satisfies $\vec E=-\vec\nabla V$, so the whole boundary-value problem is linear in $V$: double the terminal voltage and you double $\vec E$ everywhere, hence $\vec j$ everywhere, hence $I$. The ratio $V/I$ therefore cannot depend on $V$ — it is a pure geometry-times-material number. This linearity argument is the *same one* that makes capacitance a geometry constant (capacitors, ch 2), which is no accident: both are consequences of Laplace's equation. The argument breaks exactly where $\sigma$ itself depends on $E$ or on temperature — §2.5.

### 2.2 Resistivity: the material's own number

$$
\vec E=\rho\vec j,\qquad \rho=\frac{1}{\sigma},\qquad [\rho]=\Omega\ \text{m} \tag{2.1}
$$

For a **uniform** conductor of length $l$ and constant cross-section $A$ carrying current along its axis, $j=I/A$ is uniform, so $E=\rho I/A$ is uniform, and $V=El=\rho lI/A$:

$$
\boxed{R=\frac{\rho l}{A}}\qquad\text{(uniform section only)} \tag{2.2}
$$

For everything else — a cone, a wedge, current spreading through the earth — $j$ varies from point to point and the safe route is to integrate. Slice the conductor into thin slabs *perpendicular to the local current flow*, each of thickness $dl$ and area $A(dl)$; each slab contributes $dR=\rho\,dl/A(dl)$ (equipotential end faces, so slabs are in series):

$$
R=\int\frac{\rho\,dl}{A}\qquad\text{(works whenever you can name the flow lines)} \tag{2.3}
$$

> **The trap in this section**
>
> Writing $R=\rho l/A_{\text{average}}$ for a frustum or a tapered bar. The reply: resistance integrals add **reciprocals of areas**, not areas — the thin part dominates. For a frustum of radii $a$ and $b$ the exact answer is $\rho l/\big(\pi ab\big)$, not $\rho l/\pi\big(\tfrac{a+b}{2}\big)^{2}$; with $b=2a$ these differ by 12%. Always ask: *where are the equipotentials?* Then integrate between them.

### Worked example 2.1 · The spherical shell — the template for every "spread into a medium" problem

Two concentric conducting spheres of radii $a$ and $b$ ($a<b$) with the space between filled by material of resistivity $\rho$. Find the resistance between them. **Plan:** current flows radially and symmetrically, so equipotentials are spheres; slice at radius $r$. **Do:** $dR=\rho\,dr/(4\pi r^{2})$, so

 $$
R=\frac{\rho}{4\pi}\int_a^b\frac{dr}{r^{2}}=\frac{\rho}{4\pi}\left(\frac{1}{a}-\frac{1}{b}\right)=\frac{\rho(b-a)}{4\pi ab} \tag{2.4}
$$

 **Check:** as $b\to\infty$, $R\to\rho/4\pi a$ — the resistance of one small sphere dumping current into an infinite medium: finite, because the current spreads through ever-larger areas faster than $1/r^{2}$ resistance accumulates. This limit is the earthing-electrode result, and it reappears in Q4.

![Radial current between concentric spheres, with the slice used in the integral highlighted](assets/figures/fig-006.svg)

**Fig. 2.1 — Slicing along the flow lines makes a hard geometry into a one-line integral.** The area multiplying $dr$ is the area of the equipotential surface; naming that surface is the whole method.

![A tapered conductor sliced perpendicular to the axis: each slice has its own area, and reciprocals add](assets/figures/fig-007.svg)

**Fig. 2.2 — Tapered bar: the answer is the geometric-mean area.** Adding $dR=\rho\,dx/\pi r(x)^{2}$ weights the thin slices most; the closed form $\rho l/\pi ab$ is the exact result of that weighting, and the arithmetic-mean guess is simply wrong.

### 2.3 Temperature: two materials, two reasons

Chapter 1 delivered $\sigma=ne^{2}\tau/m$. Every temperature effect on conductivity is a story about the two factors on the right — and metals and semiconductors tell **opposite stories**:

> **Definition · temperature coefficient**
>
> Near a reference temperature $T_0$, a material's resistance is parametrised as
>
>  $$
> R_T=R_0\big[1+\alpha(T-T_0)\big],\qquad \alpha=\frac{1}{R}\frac{dR}{dT}\bigg|_{T_0} \tag{2.5}
> $$
>
>  $\alpha$ is itself temperature-dependent, so the linear law is a local approximation — good over tens of kelvin, bad over hundreds. For platinum $\alpha=3.85\times10^{-3}\ \text{K}^{-1}$; it is the working substance of the platinum-resistance thermometer (a Pt-100 sensor reads 138.5 $\Omega$ at 120 °C).

> **Why metals and semiconductors pull in opposite directions**
>
> **Metal:** $n$ is fixed (every atom has already donated its conduction electrons). Heat the lattice and its vibrations grow, cutting the collision time $\tau$ roughly in inverse proportion to $T$; so $\rho\propto T$ and $\alpha>0$. Over the range 0–100 °C copper obeys $\alpha=3.9\times10^{-3}\ \text{K}^{-1}$ well: from 20 °C to 120 °C its resistance grows by $\alpha\,\Delta T=39\%$ — the drift a long extension cord can measurably add.
>
>  **Intrinsic semiconductor:** $\tau$ also worsens on heating, but the carrier density wins outright: thermal pair creation goes as $n\propto e^{-E_g/2kT}$, an exponential that flattens everything linear in its path. For silicon ($E_g=1.1$ eV) the carrier density **doubles roughly every 8–10 K** near room temperature (from 300 K to 310 K alone it grows $e^{(E_g/2k)(1/300-1/310)}\approx2.0\times$) — so $\rho$ falls, and $\alpha<0$.
>
>  The exam question hiding inside: **same sign of response, opposite signs of cause**. A metal's resistance rises because carriers collide *more*; a semiconductor's falls because carriers exist *more*. Quote the mechanism, not the sign, and you cannot be tricked by a "both increase over some range" option — alloys like manganin are engineered to sit near $\alpha\approx0$ ($\sim2\times10^{-5}\ \text{K}^{-1}$: 0.2% per 100 K), which is why standard resistors are wound from them.

![Resistivity versus temperature for a metal and an intrinsic semiconductor, with the mechanisms labelled](assets/figures/fig-008.svg)

**Fig. 2.3 — The two conductivities part company with increasing temperature.** The metal's line is the failure of memory ($\tau$); the semiconductor's dive is the birth of carriers ($n$). A thermometer uses the left curve, a thermistor the right.

### 2.4 When Ohm's law fails: the non-ohmic three

Ohm's law is the **claim** that $V/I$ stays constant as $V$ varies. Three devices on every syllabus refute it, each for a distinct reason:

> **Device 1 · the filament lamp**
>
> Tungsten runs at 2800 K in use and 300 K cold. With $\alpha=4.5\times10^{-3}\ \text{K}^{-1}$ the hot resistance is $1+4.5\times10^{-3}\times2500\approx12$ times the cold value. The $I$–$V$ curve therefore **bends downward** (current grows more slowly than voltage). Consequence you will be asked to exploit twice: at switch-on the filament draws ~12× its running current — most bulbs die in the first tenth of a second — and in circuit comparisons a "60 W bulb" only has its rated resistance *at rated voltage*.

> **Device 2 · the thermistor**
>
> A sintered semiconductor, usually NTC (negative temperature coefficient): $R$ falls steeply as it warms, doubling its conductivity every $\sim$10 K. In a voltage divider it is a thermometer and a surge-limiter. The feedback sign is the exam content: warm it → $R$ drops → if it is in series it grabs *more* current and warms further — self-heating is a runaway unless something stabilises it (chapter 7 turns this into a numerical estimate).

> **Device 3 · the junction diode**
>
> Conducts only when forward-biased beyond $\sim0.7$ V (Si); below that, essentially no current; reversed, nanoamps. The $I$–$V$ curve is the steepest nonlinearity in your syllabus, and the reason circuit problems with diodes are solved **piecewise**: decide first which way the diode faces, guess on/off, solve, and *check the guess against the resulting current sign* (worked example 7.1 does this in full).

![Current-voltage characteristics of an ohmic resistor, a filament lamp, an NTC thermistor and a diode](assets/figures/fig-009.svg)

**Fig. 2.4 — One graph, four signatures.** Straight through the origin: linear. Bending below the chord: self-heating resistor. Bending above: thermistor. Flat then vertical: diode. Name the mechanism and the device is identified from the curve shape alone — a recurring JEE question format.

### 2.5 Questions

### **Q1** A wire of resistance $R$ is uniformly stretched to twice its length (volume conserved). Find the new resistance. _(JEE main)_

<details>
<summary>Solution</summary>

Volume fixed ⇒ $A' =A/2$ when $l'=2l$. Resistivity is a material property, unchanged by stretching:

$$
R'=\frac{\rho l'}{A'}=\frac{\rho(2l)}{A/2}=4R
$$

**Check:** the general rule $R\propto l^{2}$ at fixed volume (since $A=V_{\text{vol}}/l$) — doubling length quadruples $R$; stretch to $k\,l$ and $R\to k^{2}R$ ✓. The trap is halving: students divide by the area change once and forget the length change.

</details>

### **Q2** A truncated cone of length $l$ has end radii $a$ and $b$. Show its resistance along the axis is $R=\rho l/\pi ab$, and evaluate it for $a=1$ mm, $b=3$ mm, $l=10$ mm of copper. _(JEE advanced)_

<details>
<summary>Solution</summary>

Radius grows linearly: $r(x)=a+(b-a)x/l$. Slices perpendicular to the axis are equipotentials to good approximation (valid because the taper is gentle — the standard assumption; state it):

$$
R=\int_0^{l}\frac{\rho\,dx}{\pi r(x)^{2}}=\frac{\rho l}{\pi(b-a)}\left[\frac{1}{a}-\frac{1}{b}\right] =\frac{\rho l}{\pi ab}
$$

Numbers: $R=1.7\times10^{-8}\times10^{-2}/\big(\pi\times10^{-3}\times3\times10^{-3}\big) =1.7\times10^{-10}/9.42\times10^{-6}=1.8\times10^{-5}\ \Omega$ = 18 µΩ. **Check:** the uniform-tube value with $A=\pi ab$ (radius $\sqrt{ab}=1.73$ mm, the geometric mean — not the arithmetic mean 1.999 mm) sits between the naive guesses ✓. Compare worked example 2.1: same integral, different geometry, identical structure.

</details>

### **Q3** Two cylindrical rods of the same material, same length, radii $r$ and $2r$ are connected (i) in series, (ii) in parallel across a supply. Find the ratio of heat produced in the thin rod to the thick rod in each case. _(JEE main)_

<details>
<summary>Solution</summary>

$R_{\text{thin}}=2R_{\text{thick}}$ (area half). **(i) Series:** same $I$, so $H=I^{2}Rt$ gives $H_{\text{thin}}/H_{\text{thick}}=2$. **(ii) Parallel:** same $V$, so $H=V^{2}t/R$ gives $H_{\text{thin}}/H_{\text{thick}}=R_{\text{thick}}/R_{\text{thin}}=1/2$.

**Check with j:** in series the thin rod has double the current density (Q2, ch 1) and hence double $j^{2}\rho$ heating per volume, and half the volume — consistent with 2× total ✓. This pair of answers is the entire "which bulb is brighter" family in miniature: **series favours the higher-$R$ element, parallel favours the lower-$R$ one.**

</details>

### **Q4** A hemispherical electrode of radius $a=0.5$ m is buried with its flat face flush in earth of resistivity $\rho=100\ \Omega$m; a second identical electrode is 100 m away. Estimate the resistance between the electrodes, and the step voltage a cow standing with its feet 1 m apart on a radial line feels if 100 A leaks into the earth. _(Olympiad · estimation)_

<details>
<summary>Solution</summary>

Current from one hemisphere spreads radially through hemispherical surfaces $A=2\pi r^{2}$, so by the slice method $R_{\text{one}}=\rho/2\pi a=100/(\pi)=31.8\ \Omega$ into "infinity". Two electrodes far apart in series give $R\approx2\times31.8=64\ \Omega$; at 100 m the finite separation raises it slightly (mutual term $\rho/2\pi D=0.16\ \Omega$ — negligible, which *is* the check).

**Step voltage:** field at radius $r$ from one electrode: $E=\rho I/2\pi r^{2}$. At $r=100$ m, $E=100\times100/(2\pi\times10^{4})=0.16$ V/m; over a 1 m stride the cow's two feet sit at a potential difference of $\approx0.16$ V. **Check:** dangerous step potentials near earthing systems occur within a few metres of the electrode where $E\sim\rho I/2\pi a^{2}\approx6400$ V/m — the 1/r² collapse is why earth pits are fenced off, and why the answer far away is safe ✓.

</details>

### **Q5** A platinum wire has $R=10.00\ \Omega$ at 0 °C and $\alpha=3.85\times10^{-3}\ \text{K}^{-1}$. It is used as a thermometer and reads 13.85 $\Omega$. Find the temperature, and state what assumption about $\alpha$ the reading inherits. _(JEE main)_

<details>
<summary>Solution</summary>

$$
R=R_0(1+\alpha T)\ \Rightarrow\ T=\frac{R/R_0-1}{\alpha}=\frac{1.385-1}{3.85\times10^{-3}}=100\ ^\circ\text{C}
$$

The reading assumes $\alpha$ is constant from 0 to 100 °C. In reality $\alpha$ drifts by ~1% over this range; the platinum scale is therefore **calibrated** against fixed points (ice, steam, sulphur) rather than trusting one linear coefficient. **Check:** $1+3.85\times10^{-3}\times100=1.385$ ✓. If asked at 800 °C the same linear formula would be wrong by tens of degrees — the linear law is local (§2.3).

</details>

### **Q6** The resistance of a semiconductor diode, defined as $V/I$ at its operating point, is 25 $\Omega$ when it carries 20 mA at 0.5 V. A student reports "the diode is a 25 $\Omega$ resistor". Give two distinct reasons this is wrong. _(concept)_

<details>
<summary>Solution</summary>

**First:** $V/I$ at a point on a curved $I$–$V$ characteristic is the **static** resistance, a property of that operating point only. Change the current to 40 mA and the ratio changes (the curve is far from straight — Fig. 2.3). What matters for small signals is the **dynamic** resistance $r=\big(dI/dV\big)^{-1}$, which for a diode is $\eta kT/qI\approx1.3\ \Omega$ at 20 mA — twenty times smaller, because the curve's local slope is twenty times the chord's slope. **Second:** a resistor's value cannot depend on the sign of $V$; a diode's does, catastrophically (25 $\Omega$ forward, gigaohms reverse). "Resistance of a diode" is a meaningless sentence unless the operating point and the direction are both quoted — which is exactly the sentence the examiner wants from you.

</details>

### **Q7** A copper coil immersed in liquid nitrogen (77 K) has its resistance measured at 4.5 $\Omega$; at room temperature (293 K) it is 12 $\Omega$. Estimate $\alpha$ and comment on why a linear-in-$T$ law survives this far from room temperature. _(JEE advanced)_

<details>
<summary>Solution</summary>

$$
R_1=R_0(1+\alpha T_1),\quad R_2=R_0(1+\alpha T_2)\ \Rightarrow\ \alpha=\frac{R_2-R_1}{R_1T_2-R_2T_1}=\frac{7.5}{12\times77-4.5\times293}=\frac{7.5}{924-1318.5}=-\frac{7.5}{394.5}
$$

Careful with signs: solving for $\alpha$ from $R_1/R_2=(1+\alpha T_1)/(1+\alpha T_2)$ with $R_1=4.5$ at $T_1=77$, $R_2=12$ at $T_2=293$: $4.5(1+293\alpha)=12(1+77\alpha)\Rightarrow4.5+1318.5\alpha=12+924\alpha\Rightarrow 394.5\alpha=7.5\Rightarrow\alpha=1.9\times10^{-2}\ \text{K}^{-1}$ — about 5× copper's room-temperature coefficient. **Why so big:** near 77 K lattice scattering is nearly frozen and $\rho$ approaches its impurity floor, so the remaining resistance change per kelvin, referred to the now-small $R$, is large. The linear law in *absolute* temperature (Bloch–Grüneisen at low T) is better behaved than the linear law in $T-T_0$ — a genuine Olympiad-level observation to quote. **Check:** extrapolating $R\to0$ gives $1/\alpha\approx53$ K, comfortably above 77 K — no superconductivity is being claimed ✓.

</details>

### **Q8** An aluminium transmission wire is replaced by a copper wire of the same length and resistance. Find the ratio of the masses of the two wires, given $\rho_{\text{Cu}}=1.7\times10^{-8}$, $\rho_{\text{Al}}=2.7\times10^{-8}\ \Omega$m and densities 8.9 and 2.7 g cm⁻³. Which metal is the honest choice for overhead lines? _(JEE advanced · synthesis)_

<details>
<summary>Solution</summary>

Equal resistance at equal length ⇒ equal $\rho/A$ ⇒ $A_{\text{Cu}}/A_{\text{Al}}=\rho_{\text{Cu}}/\rho_{\text{Al}}=1.7/2.7=0.63$.

$$
\frac{m_{\text{Cu}}}{m_{\text{Al}}}=\frac{d_{\text{Cu}}A_{\text{Cu}}}{d_{\text{Al}}A_{\text{Al}}} =\frac{8.9}{2.7}\times0.63=2.1
$$

For the **same resistance**, copper weighs more than twice as much — and weight per span is the real cost of an overhead line (steel-cored aluminium, ACSR, is the industry answer). **Check:** flip the logic: at equal *mass*, aluminium's resistance is $(2.7/8.9)\times(2.7/1.7)=0.48$ of copper's — aluminium wins on resistance-per-kilogram, which is why transmission grids are aluminium and house wiring (where stiffness and termination reliability matter more) is copper ✓.

</details>

### 2.6 Chapter summary — the results to own

> **Shape × stuff**
>
> $$
> R=\frac{\rho l}{A}\ (\text{uniform}),\qquad R=\int\frac{\rho\,dl}{A},\qquad R_{\text{shell}}=\frac{\rho(b-a)}{4\pi ab},\qquad R_T=R_0\big[1+\alpha(T-T_0)\big]
> $$
>
>  Uniform-section formula is a special case of the integral; the integral needs only that you can name the equipotentials. Metals: $\rho\uparrow$ with $T$ via $\tau\downarrow$; intrinsic semiconductors: $\rho\downarrow$ via $n\uparrow\uparrow$. Every real device owes its non-ohmic curve to one of: carrier density changing (thermistor, diode), lattice temperature changing (filament), or band asymmetry (diode).

### 2.7 Checkpoint

- I can write down $R=\int\rho\,dl/A$ and say when it is illegal (equipotentials unknown).
- I can derive the spherical-shell resistance in one line and take both limits $b\to a$ and $b\to\infty$.
- I can explain metal vs semiconductor temperature behaviour by naming which factor of $\sigma=ne^{2}\tau/m$ moves.
- I can identify a device from its $I$–$V$ curve shape and state its failure mode.
- I know why a stretched wire's resistance scales as $l^{2}$, and why alloy resistors are used for standards.

Next: [**Chapter 3 · EMF, internal resistance and real sources →**](#section-03-emf-and-cells) — what a battery actually sells, and the tax it charges.

<a id="section-03-emf-and-cells"></a>

_Chapter 3 of 11 · JEE Advanced · core · ≈ 45 min read · 8 questions_

## EMF, internal resistance and real sources

A battery does not manufacture charge and does not store field; it **pumps** charge, spending chemical energy to do it. After this chapter you can model every real source as an ideal pump in series with its own resistance, read a $V$–$I$ graph of a cell the way you read a person's ECG, choose a cell grouping for maximum current, and account for every joule the circuit spends. The mistake this chapter prevents: treating the battery's stated voltage as its terminal voltage at every current.

### 3.1 EMF: work done per unit charge, and by whom

> **Definition · electromotive force**
>
> The EMF $\mathcal E$ of a source is the **work done per unit charge by the non-electrostatic forces** inside the source (chemical in a cell, mechanical in a generator, thermal in a thermocouple) driving charge from the negative to the positive terminal *through the source*:
>
>  $$
> \mathcal E=\frac{W_{\text{non-el}}}{q},\qquad [\mathcal E]=\text{volt} \tag{3.1}
> $$
>
>  It is a potential-*difference-like* quantity but not a potential difference: there is no electrostatic field doing this work — inside the cell the chemical forces push charges **up** the potential hill, against $\vec E$. "EMF" is a name, not a force; the unit is the volt and the thing is an energy ledger.

> **Why the circuit needs a pump at all**
>
> Electrostatic fields are conservative: $\oint\vec E\cdot d\vec l=0$ around any closed loop. A charge carried round a circuit that only felt electrostatic forces would gain nothing net per lap — current would stop the instant the wire's surfaces charged up and cancelled the pump's field inside the wire. The source is precisely the place where the loop integral is *violated* by non-electrostatic forces: it maintains the terminal potential difference, and with it the field along the wire, forever. In steady state the net energy given to a coulomb per lap — pump's work $\mathcal E$, minus tax $Ir$ lost inside — is exactly what the external resistance dissipates: $\mathcal E=IR+Ir$. That one line *is* the loop law for a one-cell circuit.

### 3.2 The practical cell: pump + internal resistance

Every real source is modelled as an ideal EMF $\mathcal E$ in series with an internal resistance $r$. The model is not decoration: the electrolyte and plates genuinely resist. Write the loop equation for a cell driving an external $R$ and you get the current, the terminal voltage, and everything else:

$$
I=\frac{\mathcal E}{R+r},\qquad V_{\text{term}}=\mathcal E-Ir\quad\text{(discharging)},\qquad V_{\text{term}}=\mathcal E+Ir\quad\text{(charging)} \tag{3.2}
$$

![A cell modelled as an ideal EMF in series with internal resistance r, driving external resistance R](assets/figures/fig-010.svg)

**Fig. 3.1 — The cell is a pump in series with a resistor you cannot remove.** The dashed box is the physical cell: chemistry (the ladder $\mathcal E$) plus electrolyte resistance ($r$). Only the terminals are sold to you.

> **The trap in this section**
>
> Reading "a 12 V battery" as "the voltmeter will say 12 V". The reply: the voltmeter reads the **terminal voltage** $\mathcal E-Ir$ whenever the battery delivers current. A starter motor drawing 200 A from a 12 V battery with $r=0.01\ \Omega$ sees only $12-200\times0.01=10$ V — the sag you hear in a car's cranking whine. And the sign flips on charge: a battery being charged sits at **more** than its EMF ($\mathcal E+Ir$). Terminal voltage above EMF ⇒ the cell is being charged; below ⇒ discharging; equal ⇒ open circuit.

![Terminal voltage versus current for a real cell: a straight line from E at zero current to zero at short-circuit current E/r](assets/figures/fig-011.svg)

**Fig. 3.2 — The load line of a cell carries its entire specification.** Intercept at $I=0$: EMF. Intercept at $V=0$: short-circuit current $\mathcal E/r$. Slope: $-r$. Given any two, the third follows — and reading intercepts off a drawn line is a complete JEE question.

### 3.3 Grouping cells: series, parallel, mixed

**Series (n cells):** EMFs add, resistances add: $\mathcal E_{\text{eq}}=n\mathcal E$, $r_{\text{eq}}=nr$. Current through a load $R$: $I=n\mathcal E/(R+nr)$.

**Parallel (m identical cells):** $\mathcal E_{\text{eq}}=\mathcal E$, $r_{\text{eq}}=r/m$: $I=m\mathcal E/(mR+r)$.

> **Parallel cells of *different* EMF — the honest case**
>
> Identical cells in parallel are safe; unequal cells fight each other. Combine them by treating each as pump plus $r$ and solving one node: two cells $(\mathcal E_1,r_1)$, $(\mathcal E_2,r_2)$ in parallel are equivalent to one cell of
>
>  $$
> \mathcal E_{\text{eq}}=\frac{\mathcal E_1r_2+\mathcal E_2r_1}{r_1+r_2},\qquad r_{\text{eq}}=\frac{r_1r_2}{r_1+r_2}\quad\text{(parallel sum)} \tag{3.3}
> $$
>
>  the weighted mean of the EMFs, weights $r$ of the *other* cell. If $\mathcal E_1\ne\mathcal E_2$, the weaker cell carries **negative** current — it is being charged by the stronger one even with no external load. Q6 makes you verify this; the equivalent-cell formula hides it, the node solution shows it.

**Mixed grouping (n in series per row, m rows in parallel):** $\mathcal E_{\text{eq}}=n\mathcal E$, $r_{\text{eq}}=nr/m$, and the current

$$
I=\frac{mn\mathcal E}{mR+nr} \tag{3.4}
$$

is largest when the denominator's two terms balance, $mR=nr$ — i.e. when the battery's internal resistance $nr/m$ equals the load $R$. That is not a coincidence; it is §3.4's maximum-power result wearing grouping clothes.

### Worked example 3.1 · Choosing the grouping

You have 12 cells, each $\mathcal E=2$ V, $r=0.5\ \Omega$, and must drive $R=1.5\ \Omega$. **Plan:** try the three groupings; the mixed rule $R=nr/m$ predicts the winner, so arrange $n/m=R/r=3$ — six in series, two rows in parallel. **Do:** mixed $(n=6,m=2)$: $I=12\times2/(2\times1.5+6\times0.5)=24/6=4.0$ A. All series $(n=12)$: $I=24/(18+6)=1.0$ A. All parallel $(m=12)$: $I=24/(18+0.5)=1.30$ A. **Check:** the predicted optimum (4.0 A) beats both extremes by large factors — with cells of $0.5\ \Omega$ against a $1.5\ \Omega$ load, all-parallel leaves $r_{\text{eq}}=0.042\ \Omega$ (fine) but only 2 V of pump, while all-series has 24 V of pump strangled by $6\ \Omega$ of internal resistance ✓.

### 3.4 The power audit

Multiply the loop equation $\mathcal E=I(R+r)$ by $I$ and every term becomes a power:

$$
\mathcal EI=I^{2}R+I^{2}r\qquad \Rightarrow\qquad \eta=\frac{P_{\text{load}}}{P_{\text{chemical}}}=\frac{R}{R+r} \tag{3.5}
$$

The chemical power $\mathcal EI$ splits into the useful $I^{2}R$ and the internal heat $I^{2}r$. Two results to own, and one warning:

> **Maximum power from a cell — and its price**
>
> With $P=\mathcal E^{2}R/(R+r)^{2}$, maximise in $R$: $dP/dR=\mathcal E^{2}(r-R)/(R+r)^{3}=0$ at
>
>  $$
> R=r\quad\Rightarrow\quad P_{\max}=\frac{\mathcal E^{2}}{4r},\qquad \eta=\frac{r}{r+r}=50\% \tag{3.6}
> $$
>
>  **Validity:** $\mathcal E, r$ fixed, varying $R$. The price is the half: at matched load the cell burns as much inside itself as it delivers. The warning: **never** quote $R=r$ for a problem where $R$ is fixed and you choose the *cell* — then $I^{2}R$ grows without bound with $\mathcal E$, and efficiency, not matching, is the design constraint. Power stations transmit at $\eta\gg90\%$; matching is a low-power electronics idea (chapter 5 generalises it to Thevenin sources).

> **Units ledger — energy, power and the commercial unit**
>
> Power is a rate, energy is an amount, and every billing question is a conversion between them.
>
>  | unit | equals | where it is used |
> | --- | --- | --- |
> | watt (W) | 1 J s⁻¹ | rating of any appliance: $P=VI=I^{2}R=V^{2}/R$ |
> | joule (J) | 1 W s | physics answers; $Q=I^{2}Rt$ heat |
> | kilowatt-hour (kWh), the "unit" | $10^{3}\times3600=3.6\times10^{6}$ J | electricity bills: cost $=$ power in kW $\times$ hours $\times$ tariff |
> | electron-volt (eV) | $1.60\times10^{-19}$ J | single-particle energies; $1\ \text{eV}=1$ V $\times$ $e$ |
> | ampere-hour (Ah) | $3600$ C | battery capacity: 12 V, 100 Ah stores $12\times100\times3600=4.3$ MJ $=1.2$ kWh |
>
>  **The two conversions examiners use.** (i) A 100 W lamp for 10 h uses $0.1\times10=1$ kWh — at ₹8 a unit that is ₹8, while the same energy as joules is 3.6 MJ. (ii) $P=I^{2}R$ is *always* the power in a resistor, but $P=V^{2}/R$ is only correct when $V$ is the voltage **across that same resistor**; writing $P=V_{\text{supply}}^{2}/R$ for two resistors in series is the standard error. The companion trap is the **rated-power trap**: a "60 W, 220 V" bulb has $R=V^{2}/P=807\ \Omega$ *at its rated temperature*. Put it in series with another bulb and it no longer receives 220 V, so it no longer dissipates 60 W — compute the new current first, then $I^{2}R$. (Its cold resistance is several times smaller still, which is why bulbs fail at switch-on.)

![Power delivered to the load versus load resistance: peak at R = r with half efficiency, falling to zero at both ends](assets/figures/fig-012.svg)

**Fig. 3.3 — The power hill has one summit and two cliffs.** Both $R=0$ (everything burns inside) and $R\to\infty$ (nothing flows) deliver zero useful power; the symmetric peak sits at $R=r$, where the split is exactly even. The curve's symmetry about $R=r$ is exact — check it at $R=2r$ and $R=r/2$.

![Energy ledger bars for R equal to r, three r and r over three: chemical power split between load and internal heat](assets/figures/fig-013.svg)

**Fig. 3.4 — The audit is the same width; only the split moves.** At $R=r$ the load takes the largest slice it can ever take, but half the chemistry is burned in the cell. Efficiency and delivered power are different maximisations — quote both, always.

### 3.5 Questions

### **Q1** A battery of EMF 12 V and internal resistance 0.01 $\Omega$ is short-circuited by a thick copper bar of negligible resistance. What is the current, and why does the cable, not the battery, usually melt first in real jump-start accidents? _(JEE main · estimation)_

<details>
<summary>Solution</summary>

$I_{\text{sc}}=\mathcal E/r=12/0.01=1200$ A.

At 1200 A the bar dissipates $I^{2}R_{\text{bar}}$ while the battery dissipates $I^{2}r=1200^{2}\times0.01=14.4$ kW spread through its whole mass of lead plates in acid; the bar's few millimetres of copper concentrate comparable power in far less metal with worse cooling. The model's answer (1200 A) is the idealisation; the real limit is the bar's resistance and the cell's chemistry catching up (polarisation raises $r$ within seconds). **Check:** order of magnitude — car batteries are indeed rated to deliver $\sim10^{3}$ A cold-cranking ✓.

</details>

### **Q2** The terminal voltage of a cell is 2.2 V when it delivers 0.5 A and 2.6 V when the same cell is being charged at 0.5 A. Find the EMF and internal resistance. _(JEE main)_

<details>
<summary>Solution</summary>

Discharging: $V=\mathcal E-Ir=2.2$. Charging: $V=\mathcal E+Ir=2.6$. Add and subtract:

$$
2\mathcal E=4.8\ \Rightarrow\ \mathcal E=2.4\ \text{V},\qquad 2Ir=0.4\ \Rightarrow\ r=\frac{0.4}{2\times0.5}=0.4\ \Omega
$$

**Check:** EMF sits exactly midway between the two readings — it must, because the $\pm Ir$ term flips sign while $\mathcal E$ does not ✓. This symmetric reading is also the cheapest honest measurement of EMF: measure $V$ at $\pm I$ and average.

</details>

### **Q3** A cell of EMF 2 V, internal resistance 1 $\Omega$ is connected to $R=3\ \Omega$. Compute the chemical power, the useful power and the efficiency. Then a second identical cell is added in parallel. Which quantities change, which do not, and why? _(JEE advanced)_

<details>
<summary>Solution</summary>

**Single cell:** $I=2/4=0.5$ A. Chemical: $\mathcal EI=1.0$ W. Useful: $I^{2}R=0.25\times3=0.75$ W. Internal heat 0.25 W. $\eta=75\%=R/(R+r)=3/4$ ✓.

**Two in parallel:** $\mathcal E_{\text{eq}}=2$ V (EMF does not add in parallel — one pump per potential difference), $r_{\text{eq}}=0.5\ \Omega$. Now $I=2/3.5=0.571$ A, useful power $V^2/R=I^{2}R=0.571^{2}\times3=0.98$ W, chemical power $\mathcal E I=1.143$ W, efficiency $R/(R+r/2)=85.7\%$.

**What changed and why:** the terminal voltage rose (less sag: $V=2-0.571\times0.5=1.714$ V vs 1.5 V) because only the *resistance* halves in parallel grouping; each cell now carries half the current and dissipates a quarter of its former internal heat. The EMF was never going to change — it is chemistry's constant. **Check:** $0.98+0.163=1.143$ ✓ ledger balanced.

</details>

### **Q4** For what external resistance is the power in $R$ half of $P_{\max}=\mathcal E^{2}/4r$? Solve exactly and comment on the two solutions. _(Olympiad)_

<details>
<summary>Solution</summary>

$$
\frac{\mathcal E^{2}R}{(R+r)^{2}}=\frac{1}{2}\cdot\frac{\mathcal E^{2}}{4r} \ \Rightarrow\ 8rR=(R+r)^{2}\ \Rightarrow\ R^{2}-6rR+r^{2}=0
$$

$$
R=r\big(3\pm2\sqrt{2}\big)\qquad\text{i.e.}\quad R\approx5.83r\ \text{or}\ 0.172r
$$

Two solutions, mirror images on a log axis about $R=r$ (their product is $r^{2}$ — the power hill of Fig. 3.3 is symmetric in this scaled sense). **Check:** at $R=5.83r$, $\eta=5.83/6.83=85\%$; at $R=0.17r$, $\eta=15\%$ — the two efficiencies sum to 100%, as they must when $R_1R_2=r^{2}$. Same delivered power, wildly different waste. When someone offers you "half power" without telling you the efficiency, there are always two designs, and the hot one is usually wrong.

</details>

### **Q5** A voltmeter of resistance 300 $\Omega$ reads 1.49 V across a cell; with a 150 $\Omega$ resistor in parallel with the voltmeter it reads 1.40 V. Find the cell's EMF and internal resistance. _(JEE advanced)_

<details>
<summary>Solution</summary>

**Reading 1:** the meter itself is the load: $1.49=\mathcal E\dfrac{300}{300+r}$. **Reading 2:** meter ∥ 150 gives $R_L=100\ \Omega$: $1.40=\mathcal E\dfrac{100}{100+r}$.

Divide: $1.49/1.40=\dfrac{300(100+r)}{100(300+r)}\Rightarrow1.0643(300+r)=3(100+r) \Rightarrow319.3+1.0643r=300+3r\Rightarrow19.3=1.936r\Rightarrow r=9.97\approx10\ \Omega$. Then $\mathcal E=1.49\times310/300=1.54$ V.

**Check:** open-circuit EMF (1.54 V) must exceed both readings ✓; with $r=10\ \Omega$, a plain 300-$\Omega$ meter drags the reading down by 3% — which is precisely why potentiometer methods (chapter 6), which draw *zero* current at balance, exist.

</details>

### **Q6** Two cells with $\mathcal E_1=2$ V, $r_1=1\ \Omega$ and $\mathcal E_2=1$ V, $r_2=2\ \Omega$ are connected in parallel (like terminals together) and this pair drives $R=3\ \Omega$. Find the current through each cell and through $R$, and say what cell 2 is doing. _(JEE advanced)_

<details>
<summary>Solution</summary>

Let $V$ be the terminal voltage of the pair. KCL at the top node:

$$
\frac{\mathcal E_1-V}{r_1}+\frac{\mathcal E_2-V}{r_2}=\frac{V}{R}\ \Rightarrow\ \frac{2-V}{1}+\frac{1-V}{2}=\frac{V}{3}
$$

Multiply by 6: $12-6V+3-3V=2V\Rightarrow15=11V\Rightarrow V=15/11=1.364$ V. Then $I_R=V/3=0.455$ A; $I_1=(2-1.364)/1=0.636$ A (discharging); $I_2=(1-1.364)/2=-0.182$ A — **negative: cell 2 is being charged** by cell 1 even while both feed the load. **Check:** $0.636-0.182=0.455$ ✓; equivalent-cell formula (3.3): $\mathcal E_{\text{eq}}=(2\times2+1\times1)/3=1.67$ V, $r_{\text{eq}}=2/3\ \Omega$, $I=1.67/3.67=0.455$ A ✓. The formula compresses the physics but hides who is charging whom — always solve the node when the EMFs differ.

</details>

### **Q7** A storage battery of EMF 24 V, internal resistance 0.05 $\Omega$ is charged from a 30 V supply through a resistor R. If the charging current is to be 20 A, find R, the power wasted in it, and the fraction of the supply's energy that ends up stored in the battery. _(JEE advanced)_

<details>
<summary>Solution</summary>

The battery being charged sits at $\mathcal E+Ir=24+20\times0.05=25$ V. Loop: $30-25=I(R+r)$ with $r$ already accounted — cleaner to write $30=25+IR\Rightarrow R=5/20=0.25\ \Omega$.

Ballast resistor: $I^{2}R=400\times0.25=100$ W. Supply delivers $30\times20=600$ W; battery takes in $25\times20=500$ W, of which $\mathcal EI=480$ W is stored chemically and $I^{2}r=20$ W heats the battery. Stored fraction: $480/600=80\%$.

**Check:** 480+20+100=600 ✓. The lesson inside the numbers: charging is intrinsically lossy ($\mathcal E/V_{\text{supply}}\le1$), and the ballast resistor's 100 W is why real chargers regulate current electronically instead — but the energy ledger is identical.

</details>

### **Q8** Two identical cells drive $R=4\ \Omega$. Connected in series they push 0.5 A; connected in parallel they push 0.4 A. Find $\mathcal E$ and $r$, and then correct the student who explains the difference as "parallel cells give half the EMF". _(JEE main)_

<details>
<summary>Solution</summary>

Series: $2\mathcal E=0.5(4+2r)\Rightarrow\mathcal E=1+0.5r$. Parallel (EMF unchanged, internal resistance halved): $\mathcal E=0.4(4+r/2)=1.6+0.2r$.

$$
1+0.5r=1.6+0.2r\ \Rightarrow\ 0.3r=0.6\ \Rightarrow\ r=2\ \Omega,\qquad \mathcal E=2\ \text{V}
$$

**Check:** series $2\times2/(4+4)=0.5$ A ✓; parallel $2/(4+1)=0.4$ A ✓.

**The correction:** cells in parallel have *exactly the same EMF* as one cell — they hold the same terminals at the same potential difference. What changed is the denominator: $r_{\text{eq}}=r/2$ and the internal drop shrank. In this data the parallel current is *lower* than series only because the load (4 $\Omega$) dwarfs the internal resistances; with a load comparable to $r$, parallel grouping wins. Naming which quantity moved — never "the EMF halved" — is the entire mark.

</details>

### 3.6 Chapter summary — the results to own

> **The pump, the tax and the ledger**
>
> $$
> I=\frac{\mathcal E}{R+r},\quad V=\mathcal E\mp Ir,\quad \mathcal EI=I^{2}R+I^{2}r,\quad \eta=\frac{R}{R+r},\quad P_{\max}=\frac{\mathcal E^{2}}{4r}\ \text{at}\ R=r
> $$
>
>  EMF is work per coulomb done by non-electrostatic forces — the only place the loop integral is not zero. Terminal voltage is a signed quantity: below EMF in discharge, above in charge. Mixed grouping gives maximum current at $R=nr/m$, the same matching idea as $R=r$. Every joule is accounted: chemistry = load + internal heat.

### 3.7 Checkpoint

- I can state EMF in words (work per unit charge by non-electrostatic forces) and say why the unit is volts.
- Given any two of $\mathcal E, r, V, I$ at an operating point, I produce the other two — in both charge and discharge.
- I can derive $P_{\max}=\mathcal E^{2}/4r$ at $R=r$, state $\eta=50\%$, and say when matching is the wrong goal.
- I can handle unequal cells in parallel by a single node equation and identify which cell is being charged.
- I can choose $n, m$ for 12 cells to maximise current in a given load and verify by computing all three groupings.

Next: [**Chapter 4 · Kirchhoff, bridges and equivalent resistance →**](#section-04-kirchhoff-and-bridges) — two laws that crack any network, and the symmetry tricks that crack it faster.

<a id="section-04-kirchhoff-and-bridges"></a>

_Chapter 4 of 11 · JEE Advanced · engine · ≈ 55 min read · 10 questions_

## Kirchhoff, bridges and equivalent resistance

Chapters 1–3 gave you the physics; this chapter gives you the **algorithm**. Two laws — charge conservation at nodes, energy conservation round loops — crack any network whatsoever, and symmetry cracks the ones the algorithm would crack slowly. After this chapter you can solve a two-loop circuit in three minutes, prove the Wheatstone balance condition, find the current in a bridge's galvanometer when it is *not* balanced, and quote the cube's three resistances from a symmetry argument you can reproduce. The mistake this chapter prevents: sign errors that survive because nobody drew the currents before writing the equations.

### 4.1 The two laws, and the discipline that makes them work

> **Definition · Kirchhoff's laws**
>
> **Junction law (KCL):** at every node, $\sum I_{\text{in}}=\sum I_{\text{out}}$. It is the steady-state continuity equation (ch 1, §1.2) — charge conservation, unbreakable.
>
>  **Loop law (KVL):** round any closed loop, $\sum \mathcal E=\sum IR$, with each $IR$ signed by the direction you traverse the resistor. It is $\oint\vec E\cdot d\vec l=0$ plus the pump's work (ch 3, §3.1) — energy conservation, unbreakable.

> **Why the sign convention is the whole method**
>
> The laws cannot fail; your bookkeeping can. The convention that never fails: **(1)** assign a direction to every unknown current — any direction, a guess you are allowed to get wrong; **(2)** traverse each loop in one fixed sense; **(3)** write $+IR$ if you cross the resistor along the current's arrow, $-IR$ against it; $+\mathcal E$ if you cross the cell from − to + (the pump lifts you), $-\mathcal E$ otherwise; **(4)** a negative answer means the current flows opposite to your guess — **it is a result, not an error**. Consistency, not clairvoyance, is what KCL/KVL demand. Redraw Fig. 4.1 in your head until assigning signs feels mechanical; every wrong answer in this chapter's problems traces to skipping step 1.

![A two-loop circuit with three branch currents assigned and two loop directions chosen](assets/figures/fig-014.svg)

**Fig. 4.1 — The setup that cannot go wrong.** Three branch currents guessed (one already fixed by KCL), two loop senses chosen: two unknowns, two independent loops, done. The guessed directions are disposable — the solved signs are not.

### Worked example 4.1 · A full two-loop solve, audited

Circuit: a 12 V battery with $R_1=2\ \Omega$ in series with a parallel pair $R_2=6\ \Omega$, $R_3=3\ \Omega$ (both batteries ideal). **Plan:** reduce the parallel pair, but keep the branch currents for the audit. **Do:** $R_{23}=6\times3/9=2\ \Omega$; $I=12/(2+2)=3$ A; $V_{23}=3\times2=6$ V; $I_2=6/6=1$ A, $I_3=6/3=2$ A (KCL: $1+2=3$ ✓). **Check (the power audit):** source $12\times3=36$ W; spent: $3^{2}\times2=18$, $1^{2}\times6=6$, $2^{2}\times3=12$; $18+6+12=36$ ✓. **Never hand in a network answer without the audit line** — it costs ten seconds and catches every sign slip.

### 4.2 Series, parallel, and the two dividers

$$
R_{\text{ser}}=\sum R_i,\qquad \frac{1}{R_{\text{par}}}=\sum\frac{1}{R_i}\quad\Big(R_{\text{par}}=\frac{R_1R_2}{R_1+R_2}\Big) \tag{4.1}
$$

> **The two dividers — with their conditions of validity**
>
> $$
> \text{voltage divider: }V_1=V\frac{R_1}{R_1+R_2}\quad(\text{series, same }I); \qquad \text{current divider: }I_1=I\frac{R_2}{R_1+R_2}\quad(\text{parallel, same }V) \tag{4.2}
> $$
>
>  Note the crossing: the current divider's numerator is the **other** resistor. Validity: dividers are exact only while no third element loads the tapped node — the moment a voltmeter or a load attaches, the effective $R$ changes and you must re-reduce (chapter 6 quantifies exactly this error).

> **The general divider — three resistors, or any number**
>
> The two-resistor forms are special cases of one rule. In a parallel group the currents share in proportion to the **conductances**, $G_k=1/R_k$:
>
>  $$
> I_k=I\,\frac{G_k}{\sum_j G_j}=I\,\frac{1/R_k}{\sum_j 1/R_j} \tag{4.3}
> $$
>
>  For three resistors in parallel ($R_1,R_2,R_3$) this reads
>
>  $$
> I_1=I\,\frac{R_2R_3}{R_1R_2+R_2R_3+R_3R_1},\qquad I_2=I\,\frac{R_3R_1}{\Sigma},\qquad I_3=I\,\frac{R_1R_2}{\Sigma},\qquad \Sigma\equiv R_1R_2+R_2R_3+R_3R_1 \tag{4.4}
> $$
>
>  The pattern to remember: **each numerator is the product of the other resistors**. The two-resistor shortcut "numerator = the other resistor" is that same statement with one factor left over after cancelling — which is why it does *not* survive at three elements. Sanity check the general form: if $R_3\to\infty$ it collapses to $I_1=I R_2/(R_1+R_2)$, the two-resistor rule ✓, and if all three are equal each carries $I/3$ ✓. In conductance language the voltage divider becomes the dual statement $V$ divides in proportion to $R_k$, currents in proportion to $G_k$: voltage prefers the big resistor, current prefers the small one.
>
>  Worked use: $R_1=2\ \Omega$, $R_2=3\ \Omega$, $R_3=6\ \Omega$ in parallel carry a total of 6 A. Then $\Sigma=6+18+12=36$, so $I_1=6(18)/36=3$ A, $I_2=6(12)/36=2$ A and $I_3=6(6)/36=1$ A. Check: these are $V=6$ V across each of 2, 3 and 6 $\Omega$ ✓, and the total is 6 A ✓.

> **The trap in this section**
>
> Applying the parallel formula to elements that are not actually in parallel. "Parallel" means **the same two nodes**, not "drawn side by side". In a bridge, the arms $R_1$ and $R_3$ are neither series nor parallel (the galvanometer branch joins their middles); that is precisely why bridges need their own machinery in §4.3. Before reducing anything, point at the two nodes each element hangs between.

### **Q1** At a node, 3 A flows in from the west wire and 1 A flows out through the east wire. Find the third branch's current and its direction. _(JEE main)_

<details>
<summary>Solution</summary>

KCL: $3=1+I_3\Rightarrow I_3=2$ A **flowing out**. **Check:** total in 3 A, total out $1+2=3$ A ✓. If you had guessed the third current inward, the algebra would have returned $-2$ A — the same physical answer with the arrow flipped, exactly as promised in §4.1.

</details>

### **Q2** In the circuit of worked example 4.1, an extra $2\ \Omega$ resistor is connected in parallel with the 12 V battery. Find the new battery current and the new total power drawn. _(JEE main)_

<details>
<summary>Solution</summary>

The 2 $\Omega$ hangs directly across the ideal battery, so it sees 12 V whatever else happens — elements in parallel with an ideal source do not disturb the rest:

$$
I_{2\Omega}=\frac{12}{2}=6\ \text{A},\qquad I_{\text{batt}}=3+6=9\ \text{A},\qquad P=12\times9=108\ \text{W}
$$

**Check:** 36 W in the original network plus $12^{2}/2=72$ W in the new branch: $36+72=108$ ✓. The invariant behaviour of the untouched branch is the whole point: **ideal sources are walls** — voltage fixed on their terminals, current through them free.

</details>

### 4.3 Symmetry: the cube and the balanced bridge

The fastest solving tool is not a formula but a question: **which nodes are at the same potential?** Connect them, delete them, or erase the branch between them — the network collapses without any algebra. Two canonical harvests:

> **The cube of resistors — all three answers from one argument**
>
> Twelve equal resistors $R$ form a cube. Drive current in at corner A, out at the opposite corner G. The three edges from A are equivalent by symmetry, so each carries $I/3$; the three edges into G likewise carry $I/3$. The six middle edges split as $I/6$. Then
>
>  $$
> V_{AG}=\frac{I}{3}R+\frac{I}{6}R+\frac{I}{3}R=\frac{5IR}{6} \ \Rightarrow\ R_{AG}=\frac{5R}{6}\ \text{(body diagonal)} \tag{4.5}
> $$
>
>  The same symmetry-planes argument with **edge** endpoints gives $7R/12$, and with **face-diagonal** endpoints gives $3R/4$ (Q3 walks you through the face-diagonal case). Q7 shows the power of the converse: when the endpoints are chosen so two nodes are provably equal in potential, the resistor between them may be **removed with no effect at all**.

![Cube of resistors between opposite corners, with the three symmetry classes of edges and the equipotential planes marked](assets/figures/fig-015.svg)

**Fig. 4.2 — Symmetry sorts the twelve edges into three current classes.** Everything flows from naming the equipotential planes perpendicular to the body diagonal; no simultaneous equations are ever written.

> **Why the balanced bridge carries no galvanometer current**
>
> Bridge $ABCD$: battery across $AC$, detector across $BD$, arms $R_1(AB),R_2(BC),R_3(AD),R_4(DC)$. Suppose $I_{BD}=0$. Then $R_1,R_2$ carry a common current $I_a$ and $R_3,R_4$ a common $I_b$, and equal potentials at B and D force $I_aR_1=I_bR_3$ and $I_aR_2=I_bR_4$. Dividing:
>
>  $$
> \boxed{\frac{R_1}{R_2}=\frac{R_3}{R_4}}\qquad\text{(balance: detector current exactly zero)} \tag{4.6}
> $$
>
>  The logic runs both ways: if the ratios match, $B$ and $D$ are at equal potential *however* you feed the bridge, so the detector branch may be deleted (or any resistance inserted there — Q7). This is why the null method is king of precision measurement (chapter 6): at balance the detector's own imperfections are irrelevant, because no current through it exists to be wrong about.

![Wheatstone bridge: battery across one diagonal, galvanometer across the other, arms labelled R1 to R4](assets/figures/fig-016.svg)

**Fig. 4.3 — The bridge and its licence.** At balance the detector diagonal is electrically dead: delete it or replace it with a wire, and every other current in the network is unchanged.

### 4.4 The unbalanced bridge: the honest calculation

Off balance, the bridge is just a two-loop network; solve it by nodes (or, faster, by Thevenin — chapter 5 re-derives the same numbers in three lines). The important skill is knowing **which side wins** before computing:

### Worked example 4.2 · Galvanometer current in an unbalanced bridge

Arms $AB=10\ \Omega$, $BC=20\ \Omega$, $AD=30\ \Omega$, $DC=40\ \Omega$; 10 V battery across $AC$; galvanometer of 50 $\Omega$ across $BD$. **Plan:** name node potentials $V_B,V_D$ (C earthed, A at 10 V) and write KCL at B and D. **Do:**

 $$
\frac{V_B-10}{10}+\frac{V_B}{20}+\frac{V_B-V_D}{50}=0;\qquad \frac{V_D-10}{30}+\frac{V_D}{40}+\frac{V_D-V_B}{50}=0
$$

 Solving the 2×2: $V_B=6.581$ V, $V_D=5.935$ V. Current through the galvanometer: $(V_B-V_D)/50=0.645/50=12.9$ mA, from B toward D. **Check:** B sits at 10×20/30 = 6.67 V and D at 10×40/70 = 5.71 V on the open-circuit bridge — B is genuinely the higher node, so the direction is right, and the loaded potentials have moved toward each other exactly as connecting any load would predict ✓. Ratio $R_1/R_2=1/2<R_3/R_4=3/4$: the pair with the *smaller* top-arm ratio wins, B rides higher — a one-line direction check worth doing before any algebra.

### 4.5 Delta–star and ladders

> **Delta–star (Δ–Y) conversion**
>
> Three resistors $R_{12},R_{23},R_{31}$ in a delta are equivalent, seen from their terminals, to a star of
>
>  $$
> R_1=\frac{R_{12}R_{31}}{R_{12}+R_{23}+R_{31}},\qquad R_2=\frac{R_{12}R_{23}}{S},\qquad R_3=\frac{R_{23}R_{31}}{S},\qquad S=R_{12}+R_{23}+R_{31} \tag{4.7}
> $$
>
>  each star arm = **product of the two delta sides touching that terminal ÷ sum of all three**. For a symmetric delta $(R,R,R)$ the star is $(R/3,R/3,R/3)$. Validity: the equivalence is exact for terminal behaviour only — internal currents and power splits differ; never mix the two pictures in one audit. Use it to break unbalanced bridges: replace one delta of the bridge by its star and the network becomes series–parallel (Q6 does this numerically).

> **The infinite ladder — self-similarity as an equation**
>
> Remove one section from an infinite ladder of series $R_s$ and shunt $R_p$; what remains is the same ladder. If its input resistance is $R_\infty$:
>
>  $$
> R_\infty=R_s+\frac{R_pR_\infty}{R_p+R_\infty} \ \Rightarrow\ R_\infty=\frac{R_s+\sqrt{R_s^{2}+4R_sR_p}}{2} \tag{4.8}
> $$
>
>  the positive root, because resistance is positive. For $R_s=2,R_p=1$: $R_\infty=1+\sqrt3=2.732\ \Omega$; for $R_s=R_p=1$: $R_\infty=(1+\sqrt5)/2$ — the golden ratio appears in a resistor network. **Check:** substitute back: $2+2.732/3.732=2.732$ ✓, and adding sections from the right can no longer move the answer — that is what "infinite" means here.

### **Q3** Twelve equal resistors $R$ form a cube. Show the resistance across a face diagonal is $3R/4$. _(JEE advanced)_

<details>
<summary>Solution</summary>

Name the corners: A, its two face-neighbours B and D, the vertical neighbour Z, the mirror partners $B',D'$, the far top corner Y, and the target C (opposite A on the bottom face). The reflection in the face diagonal swaps $B\leftrightarrow D$ and $B'\leftrightarrow D'$ while fixing A, C, Z, Y — so $V_B=V_D\equiv V_1$ and $V_{B'}=V_{D'}\equiv V_2$. Put A at 1 V, earth C. Four node equations:

$$
3V_1-V_2=1;\qquad 3V_Z-2V_2=1;\qquad 3V_2=V_1+V_Z+V_Y;\qquad 3V_Y=2V_2
$$

Solving: $V_2=V_1=\tfrac12,\ V_Z=\tfrac23,\ V_Y=\tfrac13$. Current drawn from A: $(1-V_1)+(1-V_1)+(1-V_Z)=\tfrac12+\tfrac12+\tfrac13=\tfrac43$ A, so $R=3R/4$ for unit $R$. **Check:** current delivered into C: $V_1+V_1+V_Y=\tfrac12+\tfrac12+\tfrac13=\tfrac43$ ✓ — ledger balanced. The three cube answers order as $7R/12<3R/4<5R/6$ (edge, face, body diagonal): closer endpoints mean more symmetric parallel paths, hence lower resistance. In an exam, **draw the symmetry plane first**; the arithmetic is then 30 seconds.

</details>

### **Q4** In worked example 4.2, the 50 $\Omega$ galvanometer is replaced by (i) an ideal ammeter (0 $\Omega$), (ii) an ideal voltmeter (∞ $\Omega$). Find both readings. _(JEE advanced)_

<details>
<summary>Solution</summary>

**(ii)** Ideal voltmeter: no current drawn, so it reads the open-circuit difference $V_B-V_D=6.67-5.71=0.952$ V ≈ 0.95 V.

**(i)** Ideal ammeter: shorts B to D. With $V_B=V_D$, KCL at the merged node (call it B′) with the two 10 V feeds:

$$
\frac{V_{B'}-10}{10}+\frac{V_{B'}-10}{30}+\frac{V_{B'}}{20}+\frac{V_{B'}}{40}=I_{BD}
$$

and the ammeter reading is the current in the shorting link. Fastest honest route: superposition/Norton — the short-circuit current is $V_{th}/R_{th}$ with $V_{th}=0.952$ V and $R_{th}=1/(1/10+1/20)+1/(1/30+1/40)=6.667+17.143=23.81\ \Omega$ (battery killed = replaced by wire, ideal cell): $I_{BD}=0.952/23.81=40.0$ mA. **Check:** 40 mA × nothing opposes it — short-circuit current must exceed the 12.9 mA the 50 $\Omega$ detector drew ✓; chapter 5 verifies $R_{th}$ by nodal solve.

</details>

### **Q5** A Wheatstone bridge balances with $R_1=20\ \Omega$, $R_2=30\ \Omega$, $R_3=40\ \Omega$ in the arms. Find $R_4$, and then find it again after the battery and galvanometer diagonals are interchanged. _(JEE main)_

<details>
<summary>Solution</summary>

Balance: $R_1/R_2=R_3/R_4\Rightarrow R_4=30\times40/20=60\ \Omega$.

After swapping diagonals, the arm ratios re-group but the balance condition is the **same products**: $R_1R_4=R_2R_3$ is symmetric under the swap (it becomes $R_1R_4=R_2R_3$ again, with the arms re-labelled). The balance survives: $R_4=60\ \Omega$ either way. **Check:** this invariance is the reciprocity theorem (chapter 5) in its most useful disguise: source and detector may trade places without changing any balance ✓. It also explains why meter-bridge measurements survive sloppy end corrections when you swap $R$ and $S$ (chapter 6, Q4).

</details>

### **Q6** Convert the delta $(6\ \Omega, 6\ \Omega, 6\ \Omega)$ into its star, and use the result to find the resistance between A and B of the network: A–X 6 $\Omega$, B–X 6 $\Omega$, C–X 6 $\Omega$ (a star), with a 6 $\Omega$ resistor also joined directly between A and B, and 6 $\Omega$ between B and C, and 6 $\Omega$ between C and A. _(JEE advanced)_

<details>
<summary>Solution</summary>

The network is a delta $(6,6,6)$ on terminals A,B,C *superposed* on a star $(6,6,6)$ from centre X. Convert the delta to a star $(2,2,2)$; now two stars share terminals A,B,C — stars in parallel arm-by-arm: each terminal arm is $6\parallel2=1.5\ \Omega$. Between A and B with C open, the two arms in series: $3.0\ \Omega$. **Check:** brute-force nodal on the original 6-resistor network: inject 1 A at A, draw at B, C floating: by symmetry V_A−V_B = 3 V ⇒ $R_{AB}=3\ \Omega$ ✓. Delta–star earns its keep when the superposition is *not* symmetric — then the conversion is the only clean route.

</details>

### **Q7** A Wheatstone bridge has all four arms equal to 10 $\Omega$ and is driven by an ideal 10 V battery across one diagonal. Find the battery current when the detector diagonal is (i) open, (ii) bridged by 10 $\Omega$, (iii) shorted. _(JEE main)_

<details>
<summary>Solution</summary>

The bridge is balanced, so the detector diagonal is dead in all three cases (§4.3: cut it, or insert anything, or short it — no other current changes).

$$
R_{AC}= (10+10)\parallel(10+10)=10\ \Omega,\qquad I_{\text{batt}}=\frac{10}{10}=1\ \text{A in all three cases}
$$

**Check:** case (iii): shorting B–D merges the four arms into two parallel pairs $10\parallel10=5$ in series with $10\parallel10=5$: $R_{AC}=10\ \Omega$ ✓. The invariance is the entire content of "balanced": **a null cannot be disturbed by the instrument that detects it.**

</details>

### **Q8** An infinite ladder has $R_s=3\ \Omega$ in the series arms and $R_p=1\ \Omega$ shunts. Find its input resistance, and the input resistance of the network after one more section is appended — verify nothing changed. _(Olympiad)_

<details>
<summary>Solution</summary>

$$
R_\infty=\frac{3+\sqrt{9+12}}{2}=\frac{3+\sqrt{21}}{2}=\frac{3+4.583}{2}=3.79\ \Omega
$$

Append one section to the front of the $R_\infty$ network:

$$
3+\frac{1\times3.79}{1+3.79}=3+0.791=3.79\ \Omega\quad\checkmark
$$

The fixed-point property *is* the derivation: the quadratic $R^{2}-R_sR-R_sR_p=0$ is just "$R_\infty$ with one more section equals $R_\infty$". **Check:** truncating after 1 section gives $3+1=4\ \Omega$, after 2: $3+3.79/4.79=3.791\ \Omega$ — the sequence drops from 4 and is already within 0.03% of the limit at two sections; infinite-ladder answers converge absurdly fast, so a "three-section" exam question is a disguised fixed-point question.

</details>

### 4.6 The capacitor in a DC circuit: charging, discharging and the time constant

Cengage puts the capacitor's transient behaviour in the current chapter, and rightly: nothing new is needed — Kirchhoff's loop law plus the capacitor's own $q=CV$. What is new is that the answer depends on *time*, so the circuit has a **state** (the charge on the capacitor) and an equation of motion for it. This section is the one-time-constant theory; networks with two or more capacitors, sinusoids and the full energy bookkeeping are worked in the companion note-set *Capacitors*, chapter 6.

> **The two limits that read a circuit in one second**
>
> An **uncharged** capacitor has $V_C=0$: at the instant a switch closes it behaves like a **short circuit** (any current may flow through it, with no voltage across it). A capacitor that has been in a DC circuit for a long time has $i=C\,dV/dt=0$: it behaves like an **open circuit**. Between those limits the circuit is genuinely time-dependent, and the crossover time is
>
>  $$
> \tau=RC\qquad[\,\Omega\cdot\text{F}=\text{s}\,] \tag{4.9}
> $$
>
>  The unit check is worth doing once: $\Omega\cdot\text{F}=(\text{V}/\text{A})(\text{C}/\text{V}) =\text{C}/\text{A}=\text{s}$ ✓. Every insulating "why is there no current?" answer in the chapter is the open-circuit limit; every "which bulb lights first?" question is the short-circuit limit.

> **Charging: the loop equation and its solution**
>
> Cell $\mathcal E$, resistor $R$, uncharged capacitor $C$ in series; switch closed at $t=0$. The loop law around the single mesh is
>
>  $$
> \mathcal E=iR+\frac{q}{C}=R\frac{dq}{dt}+\frac{q}{C},\qquad q(0)=0 \tag{4.10}
> $$
>
>  whose solution (separate the variables, or differentiate to get $i$ first) is
>
>  $$
> q(t)=C\mathcal E\left(1-e^{-t/\tau}\right),\qquad i(t)=\frac{\mathcal E}{R}e^{-t/\tau},\qquad V_C(t)=\mathcal E\left(1-e^{-t/\tau}\right) \tag{4.11}
> $$
>
>  Read the three factors: the **final charge** is $C\mathcal E$ and is set by the capacitor alone; the **initial current** is $\mathcal E/R$ and is set by the resistor alone (the capacitor is a short at $t=0$); and the **rate** at which one gives way to the other is $1/\tau$. At $t=\tau$ every quantity has covered $1-e^{-1}=63.2\%$ of its journey, at $3\tau$ it is 95.0%, and by $5\tau$ it is 99.3% — the practical end of the transient. The current, being the complementary exponential, has *fallen* to 37% at $t=\tau$: charge and current are not on the same schedule.

> **The general formula that covers every case — including "the other approach"**
>
> Charging, discharging, a capacitor that starts part-charged, a capacitor connected to a new cell: all of them are the same statement, that the approach to the final value is exponential:
>
>  $$
> q(t)=q_\infty-\left(q_\infty-q_0\right)e^{-t/\tau} \tag{4.12}
> $$
>
>  with $q_0$ the charge at $t=0$ and $q_\infty$ the charge the circuit would settle at if you waited forever. Check it against the two cases above: charging has $q_0=0,\ q_\infty=C\mathcal E$; discharging through $R$ with the cell removed has $q_\infty=0$, giving $q=Q_0e^{-t/\tau}$. In a network, $q_\infty$ is found by treating the capacitor as an open circuit and solving the resistive circuit, and $\tau$ is found by killing every source and reading the resistance seen from the capacitor's terminals: $\tau=R_{\text{Th}}C$, the bridge to chapter 5.
>
>  **Discharging, explicitly:** $q(t)=Q_0e^{-t/\tau}$, $i(t)=\frac{Q_0}{\tau}e^{-t/\tau} =\frac{V_0}{R}e^{-t/\tau}$, so the initial current is the same as if the charged capacitor were a battery of voltage $V_0=Q_0/C$ shorted through $R$. Half-life: $t_{1/2}=\tau\ln 2=0.693\tau$.

> **Where the energy goes — and why the resistance does not matter**
>
> Charge the capacitor from a cell: the cell delivers $\int\mathcal E\,i\,dt=C\mathcal E^{2}$, the capacitor stores $\tfrac12C\mathcal E^{2}$, and the resistor dissipates
>
>  $$
> \int I^{2}R\,dt=\tfrac12C\mathcal E^{2}\qquad\text{independent of }R \tag{4.13}
> $$
>
>  **Exactly half of the energy is lost, whatever the resistance.** Make $R$ smaller and the process is faster but not cheaper: the current is larger for a shorter time, and the integral is identical. (The same result appears in the capacitors note-set as the two-capacitor paradox — charging one capacitor from another instead of from a cell loses half the energy too, and the resolution is the same: the integral of $i^{2}R$ does not care how the current is spread in time.) A capacitor charged this way can be called a "half-efficiency" store, which is why charging circuits for pulsed-power systems use switched inductors or resonant transfer rather than a plain resistor.

![Charging curves: capacitor voltage rising and current falling, both with time constant tau marked](assets/figures/fig-017.svg)

**Fig. 4.4 — The two curves of a single time constant.** The capacitor voltage climbs toward the cell's emf and the current decays toward zero; both are drawn for the same $\tau=RC$. The tangent at $t=0$ on the current curve reaches zero at $t=\tau$, which is the geometric definition of a time constant: *the time the initial rate of change would need if it never slowed*. Marks at 63% and 99.3% are the ones to quote in an answer.

### Worked example 4.3 · A complete charging cycle

A $2\ \text{V}$ cell charges a $1\ \mu\text{F}$ capacitor through a $1\ \text{M}\Omega$ resistor. Find $\tau$, the charge at $t=\tau$ and at $t=5\tau$, the total energy the cell delivers, and how much of it the resistor burns.

 **Do:** $\tau=RC=10^{6}\times10^{-6}=1$ s. Final charge $C\mathcal E=10^{-6}\times2=2\ \mu$C; at $t=\tau$ it is $0.632\times2=1.26\ \mu$C; at $5\tau$, $0.993\times2=1.99\ \mu$C. Cell energy $C\mathcal E^{2}=4\ \mu$J, stored $\tfrac12C\mathcal E^{2}=2\ \mu$J, so the resistor dissipates $2\ \mu$J.

 **Check:** the initial current must be $\mathcal E/R=2\ \mu$A; integrating $i=\tfrac{\mathcal E}{R}e^{-t/\tau}$ gives total charge $\mathcal E C=2\ \mu$C ✓, and $\int i^{2}R\,dt=(\mathcal E^{2}/R)\cdot(\tau/2)=4/2=2\ \mu$J ✓ — the half-and-half split of the box above. Note both energies are independent of $R$; only the clock ($\tau$) moves.

> **The three traps in this section**
>
> - **"The capacitor blocks DC, so no current ever flows."** It blocks *steady* current. During the
>   transient $i$ is whatever the loop law demands; the block is the $t\to\infty$ limit, not a property of the
>   component.
> - **Using $RC$ when the capacitor is not at the end of a simple branch.** If other resistors sit around it,
>   the relevant resistance is $R_{\text{Th}}$ seen *from the capacitor's own terminals* with all sources
>   killed, not any single resistor in the picture. Two capacitors in one network do not even share a single time
>   constant — that circuit has as many $\tau$'s as it has independent charge variables.
> - **Adding a "current through the capacitor" to the final steady state.** Steady state means $i_C=0$; any
>   answer with a steady current through a capacitor is wrong before it is arithmetic.

### **Q9** A charged capacitor of $2\ \mu\text{F}$ at 50 V is connected across a $5\ \text{k}\Omega$ resistor. How long until the voltage falls below 5 V, and what total energy is dissipated? _([3])_

<details>
<summary>Solution</summary>

$\tau=RC=5000\times2\times10^{-6}=10$ ms. Discharge: $V=V_0e^{-t/\tau}$, so $5=50e^{-t/10\text{ms}}\Rightarrow e^{t/\tau}=10\Rightarrow t=\tau\ln10=23$ ms.

Energy: all the stored energy ends in the resistor — $\tfrac12CV_0^{2}=\tfrac12(2\times10^{-6})(2500) =2.5$ mJ. **Check:** $t=2.3\tau$ on the decaying curve, and $e^{-2.3}=0.10$ ✓.

</details>

### **Q10** In the circuit of worked example 4.3 the cell is removed at $t=5\tau$ and the capacitor is discharged through the same resistor. Sketch $q(t)$ across the whole history and state the current just after the switch. _([4])_

<details>
<summary>Solution</summary>

Charging for $0<t<5\tau$: rising as $2(1-e^{-t/\tau})\ \mu$C. After the change, with $t'=t-5\tau$: $q=1.99e^{-t'/\tau}\ \mu$C — the same time constant, mirrored. Just after the switch the capacitor still holds 1.99 $\mu$C, so the voltage across it is 1.99 V and the current is $1.99\ \text{V}/1\ \text{M}\Omega=1.99\ \mu$A, flowing the other way through the resistor.

**Check:** the charge is continuous at the switch (charge cannot jump), the current jumps from $-0.0067\ \mu$A to $-1.99\ \mu$A — a discontinuity in current is allowed, a discontinuity in charge is not ✓. This is the "initial value" reading of $q(t)=q_\infty-(q_\infty-q_0)e^{-t/\tau}$ with $q_0=1.99$ and $q_\infty=0$.

</details>

### 4.7 Chapter summary — the results to own

> **The algorithm and the shortcuts**
>
> $$
> \text{KCL: }\sum I_{\text{in}}=\sum I_{\text{out}};\qquad \text{KVL: }\sum\mathcal E=\sum IR;\qquad \frac{R_1}{R_2}=\frac{R_3}{R_4}\ \text{(balance)}
> $$
>
>  $$
> R_{\text{cube}}=\tfrac{7}{12}R,\tfrac34R,\tfrac56R;\qquad R_\infty=\frac{R_s+\sqrt{R_s^{2}+4R_sR_p}}{2};\qquad R_Y=\frac{\text{product of touching sides}}{\text{sum of sides}}
> $$
>
>  $$
> \tau=RC;\qquad q(t)=q_\infty-\left(q_\infty-q_0\right)e^{-t/\tau};\qquad q_{\text{charge}}=C\mathcal E\left(1-e^{-t/\tau}\right),\qquad q_{\text{discharge}}=Q_0e^{-t/\tau}
> $$
>
>  Guess arrows, write consistent signs, audit powers. Symmetry before algebra: name equipotential nodes and delete dead branches. Balance makes a bridge's detector diagonal dispensable; off balance, nodal (or Thevenin) gives the detector current — direction first, number second.

### 4.8 Checkpoint

- I can set up any two-loop circuit with guessed currents and sign discipline, and audit the power ledger at the end.
- I can prove the Wheatstone balance condition in four lines and state what it licenses (cut/short the detector).
- I can find an unbalanced bridge's galvanometer current by nodal analysis and predict its direction by ratios alone.
- I can produce $7R/12, 3R/4, 5R/6$ for the cube from symmetry, and say which endpoints give which.
- I can convert delta to star and sum an infinite ladder via a fixed-point equation.
- I can write the loop equation of an RC circuit, solve it, and quote the 63%/5τ milestones; I know that exactly half the cell's energy is burnt in the resistor whatever its value.

Next: [**Chapter 5 · Superposition, Thevenin, Norton and friends →**](#section-05-network-theorems) — theorems that replace hard networks with two numbers.

<a id="section-05-network-theorems"></a>

_Chapter 5 of 11 · JEE Advanced · engine · ≈ 45 min read · 8 questions_

## Superposition, Thevenin, Norton and friends

Chapter 4 cracks networks by force. This chapter replaces them by **two numbers**: kill the sources and read one resistance; wake one source and read one voltage. After it you can produce the Thevenin and Norton equivalents of any linear network, transform sources on sight, prove and use reciprocity, and know — this is where marks die — exactly when each theorem is *illegal*. Every theorem here is applied twice to the same unbalanced bridge, so you can watch three different roads arrive at $12.9$ mA.

### 5.1 Superposition: one source at a time

> **Theorem · superposition**
>
> In any network of **linear** resistances and independent sources, every branch current (or node voltage) is the algebraic sum of the contributions of each source acting alone — with all other ideal voltage sources **replaced by wires** (their internal resistances, if any, left in place) and all other ideal current sources **opened**.
>
>  **Validity:** linearity is the whole licence. The moment a non-ohmic element (diode, thermistor at its operating point, a bulb) sits in the network, superposition is dead — solve piecewise instead (worked example 7.1). Power does **not** superpose: $(i_1+i_2)^{2}R\ne i_1^{2}R+i_2^{2}R$ — sum currents first, square last.

### Worked example 5.1 · Two sources, one branch, three checks

A 10 V battery in series with 2 $\Omega$ is connected in parallel with a 6 V battery in series with 1 $\Omega$; the pair drives a 4 $\Omega$ load. Find the load current. **Plan:** superpose, because the two sources make a single loop reduction ambiguous.

 **Do:** 6 V killed (replaced by wire, its 1 $\Omega$ stays): $I_a=\dfrac{10}{2+(1\times4)/5}\times\dfrac{1}{5}=\dfrac{10}{2.8}\times0.2=0.714$ A. 10 V killed: $I_b=\dfrac{6}{1+(2\times4)/6}\times\dfrac{2}{6}=\dfrac{6}{2.333}\times\tfrac13=0.857$ A. Total: $I=0.714+0.857=1.571$ A. **Check:** direct nodal solve, $(10-V)/2+(6-V)/1=V/4\Rightarrow V=44/7=6.286$ V, $I=V/4=1.571$ A ✓. Bonus finding: the 6 V branch carries $(6-6.286)/1=-0.286$ A — **it is being charged** by the stronger source, exactly the ch 3, Q6 phenomenon in theorem's clothing.

### 5.2 Thevenin: any linear network is a battery

> **Theorem · Thevenin (and Norton)**
>
> Seen from two terminals, any network of resistances and sources behaves exactly like an ideal source $V_{th}$ in series with $R_{th}$ (Thevenin), or equivalently a current source $I_N$ in parallel with $R_{th}$ (Norton), where
>
>  $$
> V_{th}=V_{\text{open-circuit}},\qquad R_{th}=\frac{V_{th}}{I_{\text{short-circuit}}}=R\ \text{seen with all ideal sources killed},\qquad I_N=\frac{V_{th}}{R_{th}} \tag{5.1}
> $$
>
>  **Validity:** linear networks only; the equivalence is exact at the terminals for *every* load, including nonlinear ones — that is what makes it useful. Inside the black box the two models disagree (internal dissipation differs); never audit power inside a Thevenin equivalent.

> **Why killing a source means a wire (or a gap)**
>
> An ideal voltage source holds its terminal difference at $\mathcal E$ *whatever* the current. Setting $\mathcal E=0$ leaves "whatever the current, no difference" — a conductor. An ideal current source holds its current whatever the voltage; setting it to zero leaves "no current whatever the voltage" — a break. Real sources keep their $r$: that is the whole content of the cell model of ch 3, and it is why the Thevenin resistance of a battery network is computed with $r$ left in place. This one sentence is the most-fumbled instruction in JEE problem solving.

![A complicated two-terminal network replaced by its Thevenin equivalent: one source and one resistance](assets/figures/fig-018.svg)

**Fig. 5.1 — The Thevenin contract.** Two measurements (open-circuit voltage, killed-source resistance) buy a one-source model of any linear network. The arrow is the only place loads may be attached.

### Worked example 5.2 · The bridge, redone in three lines

The bridge of worked example 4.2 (arms 10, 20, 30, 40 $\Omega$, 10 V battery, detector across the midpoints). **Do:** remove the 50 $\Omega$ detector. Open-circuit voltage: $V_B=10\times20/30=6.667$, $V_D=10\times40/70=5.714$, so $V_{th}=0.952$ V. Kill the battery (replace by wire): from the detector's seat, $R_{th}=10\parallel20+30\parallel40=6.667+17.143=23.81\ \Omega$. Then $I=0.952/(23.81+50)=12.9$ mA ✓ — the same 12.9 mA as the two-equation nodal slog, in three lines. **Check:** short the detector: $I_{sc}=V_{th}/R_{th}=0.952/23.81=40.0$ mA — larger than 12.9 mA, as any load current must be smaller than its own short-circuit value ✓.

### 5.3 Norton and source transformation

![Thevenin and Norton equivalents side by side, with the conversion formulas between them](assets/figures/fig-019.svg)

**Fig. 5.2 — Two black boxes, one behaviour.** Source transformation is just these two equations read backwards: a Thevenin pair becomes a Norton pair with $R$ unchanged. The load cannot tell which it is wired to.

> **The trap in this section**
>
> Transforming a source that is not "in series/parallel with $R$ relative to the terminals you care about". A voltage source transforms only with the resistor **in series with it between the same two terminals**; a current source only with one **in parallel**. Transforming an ideal source alone (no partner resistor) is meaningless — an ideal 10 V source is not a 10 V source "with $R=0$" for transformation purposes; it is a wall, and walls cannot become current sources. Before every transformation, point at the two terminals and check the partnership.

### 5.4 Maximum power transfer

> **Result · the matched load**
>
> A Thevenin source $(V_{th},R_{th})$ delivers maximum power to a load $R_L=R_{th}$:
>
>  $$
> P_{\max}=\frac{V_{th}^{2}}{4R_{th}},\qquad \eta_{\text{at match}}=50\% \tag{5.2}
> $$
>
>  **Validity:** $V_{th},R_{th}$ fixed, $R_L$ varied. This is ch 3's $R=r$ result — the cell was already a Thevenin source. Two warnings worth marks: (i) at the matched point the source burns as much inside as it delivers — power stations and audio amplifiers driving speakers do **not** match, they maximise $\eta$; matching is for signals, where the watts are microwatts and the information is the cargo. (ii) If the problem fixes $R_L$ and lets the *source* change, there is no interior maximum at all.

![Load power versus load resistance: peak at R_L = R_th delivering V squared over four R, at half efficiency](assets/figures/fig-020.svg)

**Fig. 5.3 — The power hill again, now for any network.** To the left of the summit the load is current-limited; to the right it is voltage-starved. Every "find $R_L$ for maximum power" question is a Thevenin question in disguise: reduce, then match.

### Worked example 5.3 · Maximum power from the bridge

Replace the bridge's detector by a variable $R_L$. Thevenin at the detector terminals: $V_{th}=0.952$ V, $R_{th}=23.81\ \Omega$. Maximum power at $R_L=23.81\ \Omega$: $P_{\max}=0.952^{2}/(4\times23.81)=0.907/95.24=9.52$ mW. **Check:** at $R_L=2R_{th}=47.62\ \Omega$, $P=V_{th}^{2}R_L/(R_L+R_{th})^{2}=0.907\times47.62/71.43^{2}=43.2/5102=8.47$ mW — 8/9 of the maximum, the exact ratio the quadratic predicts ✓.

### 5.5 Reciprocity and compensation

> **Theorem · reciprocity**
>
> In a network of resistances (any linear passive network), interchange an ideal voltage source and an ideal ammeter and the ammeter reads the same. Equivalently: the short-circuit current at port 2 per unit voltage at port 1 equals the short-circuit current at port 1 per unit voltage at port 2 — the **ratio is invariant**, each number separately is not.
>
>  **Verified on our bridge:** excite A–C, short the detector diagonal: 40.0 mA. Swap — excite B–D, short A–C: **again 40.0 mA**. But the open-circuit voltages differ (0.952 V vs 0.833 V): reciprocity equates $I_{sc}/V_{\text{drive}}$, never the two open voltages. Q6 makes you do the second measurement honestly.
>
>  **Validity:** no dependent sources, no nonlinearity, and the swap must not disturb the network's resistances. It is why a Wheatstone balance survives exchanging the battery and galvanometer diagonals (ch 4, Q5), and why four-terminal resistance standards work from either end.

> **Definition · the compensation theorem**
>
> If a resistor $R$ carrying current $I$ is changed by $\Delta R$, the change in every current elsewhere equals what a single voltage source $-I\,\Delta R$ (opposing the original flow), inserted in place of the change, would produce — with all other sources killed. It is the perturbation version of Thevenin, and it is how you answer "a galvanometer of resistance $R_g$ is replaced by one of $2R_g$: how much do the *other* currents move?" without re-solving the whole network.

### **Q1** In worked example 5.1's circuit, verify the superposition components by computing the current in the 2 $\Omega$ resistor both ways, and find the total power delivered by the 10 V source. _(JEE advanced)_

<details>
<summary>Solution</summary>

Node voltage (both sources live): $V=6.286$ V, so the 2 $\Omega$ carries $(10-6.286)/2=1.857$ A. **By superposition:** 6 V killed: $10/[2+(1\times4)/5]=3.571$ A through the 2 $\Omega$. 10 V killed: the 2 $\Omega$ sits in the middle of the divider; current through it = current of the 6 V loop $6/2.333=2.571$ A flowing the *opposite* way through the 2 $\Omega$ (it returns via the shorted source): net $3.571-2.571=1.857$ A ✓. Source power: $P_{10}=10\times1.857=18.57$ W. **Check:** audit: 4 $\Omega$ takes $1.571^{2}\times4=9.88$ W; 6 V source absorbs $6\times0.286=1.71$ W (charging); resistors $1.857^{2}\times2+0.286^{2}\times1=6.90+0.08=6.98$ W; total consumed $9.88+1.71+6.98=18.57$ W ✓ — ledger balances, including the charged cell.

</details>

### **Q2** A 10 V battery of negligible internal resistance feeds a divider of 10 k$\Omega$ and 10 k$\Omega$. A load $R_L$ is attached across the lower resistor. Find $V_L$ for $R_L=$ 100 k$\Omega$, 10 k$\Omega$, 1 k$\Omega$, and explain the pattern with a Thevenin sentence. _(JEE main)_

<details>
<summary>Solution</summary>

The divider, from the load's terminals, is a Thevenin source: $V_{th}=5$ V, $R_{th}=10k\parallel10k=5$ k$\Omega$. Then $V_L=5R_L/(R_L+5k)$:

$$
R_L=100k:\ 4.76\ \text{V};\qquad 10k:\ 3.33\ \text{V};\qquad 1k:\ 0.833\ \text{V}
$$

**Pattern:** loading is negligible only while $R_L\gg R_{th}$. The unloaded "half of 10 V" promise of the divider formula holds only in the open-circuit limit — chapter 6 turns this exact arithmetic into the voltmeter-loading error. **Check:** full nodal solve for $R_L=10k$: $V=10\times(10k\parallel10k)/(10k+5k)=10\times5/15=3.33$ V ✓.

</details>

### **Q3** Using Norton equivalents only, find the current through the 50 $\Omega$ detector of worked example 5.2. _(JEE main)_

<details>
<summary>Solution</summary>

$I_N=V_{th}/R_{th}=0.952/23.81=40.0$ mA, in parallel with $R_{th}=23.81\ \Omega$. Current divider with the detector:

$$
I_{50}=40.0\times\frac{23.81}{23.81+50}=40.0\times0.3226=12.9\ \text{mA}\quad\checkmark
$$

Third method, third arrival at 12.9 mA. **Check:** the Norton and Thevenin forms are algebraically identical — $V_{th}/(R_{th}+R_L)\equiv I_N R_{th}/(R_{th}+R_L)$ — so agreement is guaranteed; the value of the exercise is catching arithmetic slips in $R_{th}$, which is where everyone errs.

</details>

### **Q4** A real source delivers 9 W to a 9 $\Omega$ load and 16 W to a 4 $\Omega$ load. Find its Thevenin parameters and the maximum power it can deliver. _(JEE advanced)_

<details>
<summary>Solution</summary>

A Thevenin source obeys $P=V_{th}^{2}R_L/(R_L+R_{th})^{2}$. Both data give the same current per volt readily: 9 W into 9 $\Omega$ ⇒ $I=1$ A; 16 W into 4 $\Omega$ ⇒ $I=2$ A. Loop equations $V_{th}=I(R_L+R_{th})$:

$$
V_{th}=1(9+R_{th});\qquad V_{th}=2(4+R_{th})\ \Rightarrow\ 9+R_{th}=8+2R_{th} \ \Rightarrow\ R_{th}=1\ \Omega,\ V_{th}=10\ \text{V}
$$

Maximum power at $R_L=R_{th}=1\ \Omega$: $P_{\max}=V_{th}^{2}/4R_{th}=100/4=25$ W. **Check:** 9 $\Omega$: $100\times9/100=9$ W ✓; 4 $\Omega$: $100\times4/25=16$ W ✓. **Sanity note:** had the second datum been 4 W instead of 16 W, the two equations would read $V=9+R$ and $V=4+R$ — no source exists, and the correct answer would be "the data are inconsistent", not a forced fit. Always solve the system before believing it.

</details>

### **Q5** State two distinct reasons superposition cannot be used to find the current in a circuit containing a bulb filament and a junction diode, and name the method that replaces it. _(concept)_

<details>
<summary>Solution</summary>

**Reason 1:** the filament's resistance depends on the *total* current (through its temperature); killing one source changes the heating, hence $R$, hence the response to the other source — the "response proportional to cause" premise dies. **Reason 2:** the diode's conductance depends on the *sign* of the applied voltage; with two sources superposing to opposite signs, the diode may conduct for the sum but not for each part separately (and vice versa) — no sum of parts can reproduce that. **Replacement:** piecewise solution — guess each nonlinear element's state, solve the remaining linear network, then **check every guess** against the solution (diode current must be positive in the conducting direction; filament resistance must match its own heating). Worked example 7.1 is the template.

</details>

### **Q6** For the bridge network (arms 10, 20, 30, 40 $\Omega$), the source is moved to the detector diagonal and an ideal ammeter is placed where the battery was. Predict the ammeter reading, and state why the open-circuit voltage across the old battery diagonal is *not* the same as the old detector open-voltage. _(Olympiad)_

<details>
<summary>Solution</summary>

By reciprocity, the short-circuit current is invariant under the swap: $I=V_{th}/R_{th}=40.0$ mA — the ammeter reads 40.0 mA, the same as the original detector short-circuit current. **Why the open voltages differ:** reciprocity equates the *ratios* $I_{sc}/V_{\text{drive}}$ between the ports, not the open-circuit voltages; computing the second configuration honestly: with 10 V across B–D and A–C open, $V_A=10\times10/40=2.5$ V (divider A–D–? arms from B: A via 10 $\Omega$: $V_A=10-10\times10/(10+30)=7.5$ V), $V_C=10\times40/(20+40)=6.67$ V, open difference $0.833$ V — different from 0.952 V, same 40 mA. **Check:** nodal solve confirms both numbers exactly ✓. The invariant is one number; quote it and resist the urge to "symmetrise" the rest.

</details>

### **Q7** For worked example 5.1's two-source network, find the load resistance that draws maximum power and the value of that maximum. _(JEE advanced)_

<details>
<summary>Solution</summary>

Kill both sources: 10 V becomes a wire (2 $\Omega$ stays), 6 V becomes a wire (1 $\Omega$ stays). From the load terminals: $R_{th}=2\parallel1=0.667\ \Omega$. Open-circuit voltage: no load current, so $(10-V)/2+(6-V)/1=0\Rightarrow 10-V+12-2V=0\Rightarrow V=22/3=7.333$ V. Then

$$
R_L=R_{th}=\tfrac23\ \Omega,\qquad P_{\max}=\frac{V_{th}^{2}}{4R_{th}} =\frac{53.78}{2.667}=20.2\ \text{W}
$$

**Check:** at $R_L=2/3$: total loop $R=1.333\ \Omega$, $I=7.333/1.333=5.5$ A, $P=5.5^{2}\times\tfrac23=20.17$ W ✓, and the internal dissipation is also 20.2 W (50% efficiency, as promised). Note what the answer is telling you: maximum-power matching wants a *tiny* load here — the sources are stiff, and 20 W of matching wastes 20 W inside them.

</details>

### **Q8** An ammeter of resistance 0.5 $\Omega$ is inserted in series with a resistor of about 0.1 $\Omega$ to "measure" it from a 1 V source in series with 10 $\Omega$. Use the compensation idea to estimate the fractional error, and name the measurement method that removes it. _(Olympiad)_

<details>
<summary>Solution</summary>

True current (ammeter ideal): $I=1/(10+0.1)=0.0990$ A. With the ammeter: $I'=1/(10+0.1+0.5)=0.0943$ A. The ammeter reads $I'$ and you infer $R=V_R/I'\approx(1-10\times0.0943)/0.0943=0.057/0.0943=0.60\ \Omega$ — a **500% overestimate**: the 0.5 $\Omega$ instrument dwarfs the 0.1 $\Omega$ specimen. The compensation view: inserting the ammeter is a $\Delta R=+0.5\ \Omega$ perturbation in a loop whose other resistance is 10.1 $\Omega$; the current change is second-order small but the *inference* error is first-order because the perturbation sits in series with the quantity being measured. **Removal:** the four-terminal (Kelvin) method — force the current through the specimen with one pair of leads, read the voltage with a second pair that carries no current, so the lead and instrument resistances drop out (chapter 6, Q8).

</details>

### 5.6 Chapter summary — the results to own

> **Two numbers replace a network**
>
> $$
> V_{th}=V_{oc},\qquad R_{th}=\frac{V_{oc}}{I_{sc}},\qquad I_N=\frac{V_{th}}{R_{th}},\qquad P_{\max}=\frac{V_{th}^{2}}{4R_{th}}\ \text{at}\ R_L=R_{th},\ \eta=50\%
> $$
>
>  Kill sources: voltage source → wire (keep $r$), current source → break. Superposition sums currents, never powers, and dies on any nonlinearity. Reciprocity preserves short-circuit ratios under port swap; compensation computes perturbations by a single opposing source. Every one of these was verified against the same 12.9 mA — that cross-checking habit is the real content of the chapter.

### 5.7 Checkpoint

- I can state the killing rule for both source types and say why it is true.
- I can find $V_{th}$ and $R_{th}$ of a bridge circuit and predict detector current and direction for any detector resistance.
- I can transform Thevenin ↔ Norton without pausing, and refuse to transform a bare ideal source.
- I can derive $R_L=R_{th}$ for maximum power, state $\eta=50\%$, and argue when matching is the wrong objective.
- I can state reciprocity with its precise invariant and verify it numerically on a bridge.

Next: [**Chapter 6 · Meters, bridges and the potentiometer →**](#section-06-instruments-and-measurement) — the same theorems, built into hardware.

<a id="section-06-instruments-and-measurement"></a>

_Chapter 6 of 11 · JEE Advanced · applied · ≈ 45 min read · 8 questions_

## Meters, bridges and the potentiometer

Every instrument is a theorem from chapter 5 wearing a case. After this chapter you can convert one galvanometer into any ammeter or voltmeter range you like, compute the error a real meter commits the moment you connect it, run a meter bridge with its end-error correction, and explain why the potentiometer — a stretched wire and a jockey — outperforms every dial instrument ever made. The mistake this chapter prevents: believing a meter changes nothing in the circuit it measures.

### 6.1 The galvanometer and its two careers

> **Definition · the moving-coil galvanometer**
>
> A coil of $N$ turns in a radial field $B$: current $I_g$ gives deflection $\phi=\big(NB A/k\big)I_g$ (spring constant $k$, area $A$), linear to full-scale $I_g$ of order microamp–milliamp, with coil resistance $G$ of order 20–500 $\Omega$. The radial field (curved pole pieces, soft-iron core) keeps $\phi\propto I$ — linearity is engineered, not automatic. Everything in this chapter hangs off two numbers: full-scale current $I_g$ and resistance $G$.

> **Ammeter: small shunt, because an ammeter must not disturb the current it measures**
>
> To read large currents, most of the current must **bypass** the coil. Shunt $S$ in parallel with $G$, total current $I$: same voltage across both, so $I_gG=(I-I_g)S$:
>
>  $$
> S=\frac{I_gG}{I-I_g}=\frac{G}{n-1},\qquad n=\frac{I}{I_g} \tag{6.1}
> $$
>
>  The shunted meter's resistance is $GS/(G+S)\approx S\ll G$. Validity: $n\gg1$ for any honest ammeter — a 1 mA, 100 $\Omega$ movement becomes a 1 A meter with $S=0.1001\ \Omega$ and total resistance $0.1\ \Omega$, which passes 99.9% of the current. The shunt must be low-$\alpha$ (manganin): the calibration would otherwise drift as the shunt warms under load.

> **Voltmeter: large multiplier, because a voltmeter must not disturb the voltage it measures**
>
> To read voltage, the meter must draw as little current as possible while its deflection needs $I_g$: a multiplier $R_m$ in series:
>
>  $$
> R_m=\frac{V}{I_g}-G,\qquad\text{sensitivity in }\Omega/\text{V}=\frac{1}{I_g} \tag{6.2}
> $$
>
>  The same 1 mA, 100 $\Omega$ movement becomes a 10 V meter with $R_m=9900\ \Omega$ — and its 1000 $\Omega$/V rating is the **only** number a practicing engineer needs: on any range, resistance = rating × full-scale volts.

![Galvanometer converted to an ammeter by a small shunt and to a voltmeter by a large series multiplier](assets/figures/fig-021.svg)

**Fig. 6.1 — One movement, two instruments, opposite strategies.** The ammeter hides inside a tiny resistance; the voltmeter hides behind a huge one. Both conversions are exact applications of "same voltage" / "same current" — chapter 4's two dividers with purpose.

### 6.2 The loading error: every meter lies a little

> **Result · what a real voltmeter reads**
>
> A voltmeter of resistance $R_V$ across the lower resistor $R_2$ of a divider fed by $V$ through $R_1$ reads
>
>  $$
> V_{\text{read}}=V\,\frac{R_2\parallel R_V}{R_1+(R_2\parallel R_V)} \qquad\text{vs the true }V\frac{R_2}{R_1+R_2} \tag{6.3}
> $$
>
>  **Worked numbers:** 100 V across 10 k$\Omega$ + 10 k$\Omega$, true answer 50 V; a 10 k$\Omega$ meter drags the reading to $100\times5/15=33.3$ V — a **33% lie**. The meter does not malfunction; the *circuit plus meter* is a different circuit. A 1000 $\Omega$/V meter on its 100 V range (100 k$\Omega$) reads $100\times9.09/19.09=47.6$ V; a potentiometer (§6.4) reads 50.0 V exactly.

> **The trap in this section**
>
> "The ammeter reads the current, so connect it and read." The reply: an ammeter adds its own small resistance $R_A$ to a loop — for a 0.1 $\Omega$ meter in a 1 $\Omega$ circuit that is a 10% error, and for a 0.1 $\Omega$ *specimen* (Q8) it is a 500% error. Instrument choice is error analysis: the rule is $R_A\ll R_{\text{circuit}}$ and $R_V\gg R_{\text{element}}$, and when either fails, you need a null method or four terminals — not a better meter.

### 6.3 The Wheatstone and meter bridges

The Wheatstone bridge (ch 4, §4.3) balances when $R_1/R_2=R_3/R_4$ and draws **no current through the detector at balance** — instrument imperfections are then irrelevant. The **meter bridge** implements the two ratio arms as 100 cm of uniform resistance wire with a jockey: balance at length $l$ gives

$$
\frac{R}{S}=\frac{l}{100-l} \tag{6.4}
$$

> **End errors, and why swapping kills them**
>
> The zero of the scale rarely coincides with the end of the wire: soldering lumps add a millimetre or two at each end. If the true balance point is $l$ but the contact sits at scale reading $l+e_1$ with an end error $e_1$ at one end and $e_2$ at the other, the ratio is really $R/S=(l+e_1)/(100-l+e_2)$ — two unknown corruptions. Now swap $R$ and $S$ and re-balance at $l'$: $S/R=(l'+e_1)/(100-l'+e_2)$. Multiplying and adding the equations eliminates the errors only approximately; the standard practical recipe is *interchange and average* — the errors enter with opposite signs, and for $e\ll l$ the corrected value is $\sqrt{RS}$ exactly from $R/l$ and $S/l'$ products. Example: $R=4\ \Omega$, balance at 44.0 cm gives $S=4\times56/44=5.091\ \Omega$; a 2 mm end error shifts that by about 0.4% — visible, and the reason the swap is taught.

> **Checking the connections before you trust a balance**
>
> A bridge answers only if the current actually flows the way you are assuming, so run these four checks in order before reading a number. (i) **Continuity both ways:** touch the jockey at the two ends of the wire and confirm the galvanometer deflects in *opposite* senses — if it deflects the same way at both ends, one end connection (or the galvanometer's own terminal) is open or crossed. (ii) **A balance point exists inside 0–100 cm:** if the null is only found off the wire, the ratio $R/S$ is outside what the bridge can span — swap the resistors rather than hunting. (iii) **Deflection reverses about the null:** moving the jockey 1 cm either side of balance must send the galvanometer the two ways; if it does not, the galvanometer branch is missing its key or is shorted. (iv) **Check the copper strips:** the thick end strips, not the wire, carry the gap currents — a loose screw in a gap is the commonest cause of a "dead" bridge, and the reason the null moves when you press the plug.

![Meter bridge: one-metre wire with jockey, known and unknown resistors, galvanometer with key](assets/figures/fig-022.svg)

**Fig. 6.2 — The meter bridge is a Wheatstone bridge whose two arms are one piece of wire.** Length is the cheapest precision ratio ever manufactured: a good wire gives parts-in-10⁴, which no dial instrument of the era could touch.

### 6.4 The potentiometer: measurement without theft

> **Why the potentiometer is the gold standard**
>
> Drive a uniform wire with a stable source so that every centimetre drops the same voltage $\sigma=V/L$ (the **gradient**). Slide a jockey until the galvanometer between the unknown cell and the wire shows **null**: at that instant the wire segment's drop equals the cell's EMF exactly — and because the detector reads zero, **no current is drawn from the cell**. The internal resistance is invisible, the loading error is zero, and the calibration is a length. The comparison of two EMFs is a pure ratio of balance lengths:
>
>  $$
> \frac{\mathcal E_1}{\mathcal E_2}=\frac{l_1}{l_2};\qquad r=R\,\frac{l_0-l}{l}\quad\text{(internal resistance from one extra reading)} \tag{6.5}
> $$
>
>  the second formula: with resistance $R$ shunting the cell, its terminal voltage (now carrying current) balances at $l<l_0$, and $\mathcal E/(\mathcal E-Ir)=l_0/l$ rearranges to the printed result.

![Potentiometer: driver cell across a long wire, unknown cell opposed to the wire drop through a galvanometer](assets/figures/fig-023.svg)

**Fig. 6.3 — Two EMFs opposed, one galvanometer, zero stolen current.** The instrument chain — chapter 4's balance, chapter 5's null philosophy — made physical. It measures EMF, not terminal voltage, because it never lets the cell deliver a thing.

### 6.5 Questions

### **Q1** A galvanometer of resistance 100 $\Omega$ gives full-scale deflection at 1 mA. Convert it to (i) a 0–1 A ammeter and (ii) a 0–10 V voltmeter. In each case compute the added resistance and the power it must safely dissipate at full scale. _(JEE main)_

<details>
<summary>Solution</summary>

**(i)** $n=1000$: $S=G/(n-1)=100/999=0.1001\ \Omega$. Shunt power at full scale: the shunt carries 0.999 A, so $P_S=0.999^{2}\times0.1001=0.0999\approx0.1$ W (the coil itself takes only $10^{-6}\times100=0.1$ mW — the shunt is the thermal part).

**(ii)** $R_m=V/I_g-G=10/0.001-100=9900\ \Omega$. Multiplier power: $I_g^{2}R_m=9.9$ mW plus coil 0.1 mW.

**Check:** shunted meter total resistance $=GS/(G+S)=100\times0.1001/100.1001=0.1\ \Omega$ ✓ ≪ load resistances in any circuit where 1 A flows honestly; voltmeter resistance 10 k$\Omega$ ✓ = 1000 $\Omega$/V. The asymmetry — 0.1 W in the shunt vs 10 mW in the multiplier — is the thermal fingerprint of the two jobs.

</details>

### **Q2** The galvanometer of Q1 is made into a multi-range ammeter using a universal (Ayrton) shunt tapped at points that give ×10 and ×100 ranges. Explain why the shunt must be tapped rather than switched, and what happens at the instant of a bad contact. _(Olympiad · concept)_

<details>
<summary>Solution</summary>

A make-before-break tapped shunt never leaves the coil's circuit open: at every instant of switching, the coil sees *some* shunt path. If the shunt circuit were broken while 1 A flows, the full current would try to pass through the 1 mA coil — a thousand-fold overload, and the movement burns in the milliseconds before you notice. With a tapped (universal) shunt the coil is permanently in parallel with a definite resistance; the tap only changes how much of the shunt is in the coil's branch. **Check of the principle:** at ×100, the shunt section in the coil branch is $G/(n-1)=100/99\approx1.01\ \Omega$, and the remaining sections act as series safety resistors ✓. The same logic is why ammeters carry fused links and why you never short an ammeter's shunt terminals while current flows.

</details>

### **Q3** In the divider of §6.2 (100 V, 10 k$\Omega$ + 10 k$\Omega$), a student wants the reading within 1% of 50 V. What minimum voltmeter resistance is needed? Express it as a sensitivity for a 100 V range. _(JEE advanced)_

<details>
<summary>Solution</summary>

Reading: $V_{read}=100\,R_p/(10k+R_p)$ with $R_p=R_2\parallel R_V$. Require $V_{read}\ge49.5$ V: $R_p\ge10k\times49.5/50.5=9.80k\ \Omega$. With $1/R_p=1/10k+1/R_V$: $1/R_V=1/9.80k-1/10k=2.04\times10^{-6}\Rightarrow R_V\ge490\ k\Omega$ — i.e. $\ge4900\ \Omega$/V on the 100 V range. **Check:** the 100 k$\Omega$ meter of §6.2 (1000 $\Omega$/V) read 47.6 V — 4.8% low, four times the budget ✓. The lesson in one line: **sensitivity must scale with the impedance of the circuit being measured**; 1000 $\Omega$/V is splendid on a 12 V car battery and useless in a valve amplifier.

</details>

### **Q4** In a meter bridge, $R=4\ \Omega$ balances at scale reading $l=44.5$ cm, but the wire's left end has a +0.5 cm zero error (the scale reads 0.5 cm when the contact is at the true end). Find $S$ from the naive formula, then eliminate the error by the interchange method, and compare both answers with the true value. _(JEE advanced)_

<details>
<summary>Solution</summary>

The naive reading: $S_1=4\times(100-44.5)/44.5=4\times55.5/44.5=4.989\ \Omega$.

The truth: the real balance sits at wire-position 44.0 cm (reading = position + 0.5), so the true $S=4\times56/44=5.091\ \Omega$ — the naive answer is 2% low from half a centimetre of solder.

**Interchange:** put $S$ in the left gap, $R$ in the right. The true balance moves to wire-position 56.0 cm (since $S/R=56/44$), read as 56.5. Now $R/S_2=(100-56.5)/56.5=43.5/56.5=0.7699$, giving $S_2=4/0.7699=5.196\ \Omega$ — 2.1% high. **Mean:** $(4.989+5.196)/2=5.092\ \Omega$ — within 0.03% of the truth. **Check:** the error enters the first reading as $+e$ in the denominator-arm and the second as $+e$ in the other arm, so the two naive values bracket the truth almost symmetrically; averaging cancels the error to first order (2% → 0.03%), which is the whole practical content of the swap.

</details>

### **Q5** A cell gives a null at 150 cm; with a 4 $\Omega$ resistor across it, the null moves to 120 cm. Find the EMF (driver gradient 0.01 V/cm) and internal resistance. _(JEE main)_

<details>
<summary>Solution</summary>

$$
\mathcal E=0.01\times150=1.50\ \text{V};\qquad r=R\frac{l_0-l}{l}=4\times\frac{30}{120}=1.0\ \Omega
$$

**Check:** with the resistor the cell delivers $I=1.5/(4+1)=0.3$ A, terminal voltage $1.5-0.3=1.2$ V, which balances at $1.2/0.01=120$ cm ✓ — the two chapters' pictures agree. If the same cell were read by a 1500 $\Omega$ voltmeter: current $1.5/1501$ mA, reading $1.499$ V — the meter is nearly honest here only because 1500 $\Omega$ ≫ 1 $\Omega$; with $r=100\ \Omega$ it would read 1.41 V and the potentiometer would still read 1.500.

</details>

### **Q6** Two cells balance at 250 cm and 200 cm on the same wire. State both EMFs' ratio, and predict the balance length of the two cells connected in series aiding and in opposition (internal resistances immaterial at balance). _(JEE main)_

<details>
<summary>Solution</summary>

$$
\frac{\mathcal E_1}{\mathcal E_2}=\frac{250}{200}=1.25
$$

Series aiding: EMFs add (potentiometer draws no current, so internal resistance is irrelevant): $l=250+200=450$ cm. Opposition: $l=50$ cm. **Check:** the opposition measurement is the classical way to find a small difference of two nearly equal EMFs — 1 cm of wire resolves $\sigma=\mathcal E_2/200$, so the difference is measured with the *full* precision of the original lengths, not their difference's precision ✓.

</details>

### **Q7** Rank these four methods for measuring an EMF to 0.1%: (i) moving-coil voltmeter 1000 $\Omega$/V; (ii) digital multimeter, 10 M$\Omega$ input; (iii) meter bridge with galvanometer; (iv) potentiometer with a steady driver. Justify each ranking with the error mechanism, not the label. _(Olympiad · synthesis)_

<details>
<summary>Solution</summary>

**(iv) > (ii) > (iii) > (i).** The potentiometer's error is the driver's *stability and wire uniformity* — a calibration question, answerable to parts in 10⁴ or better, and fundamentally zero loading. The DMM's 10 M$\Omega$ input makes loading negligible for any source below megaohm impedance; its 0.1% is the instrument's own calibration, factory-locked. The meter bridge's limit is mechanical (contact resistance at the jockey, end errors, wire non-uniformity — parts in 10³ at best) and it measures *resistance ratios*, not EMFs, without extra recipe. The moving-coil voltmeter loads every source it touches (§6.2: 33% on our divider) and its 1% scale reading is the least of its sins. **Check:** the ranking reorders if the source impedance is multi-megaohm — then the DMM's 10 M$\Omega$ loads too, and only the potentiometer (or an electrometer) stays honest. Error mechanism first, instrument label second: that sentence is the answer.

</details>

### **Q8** A 0.1 $\Omega$ shunt must be measured to 1%. Two-wire measurement includes two leads of 10 m$\Omega$ each and an ammeter of 0.5 $\Omega$ in the force circuit. Show the two-wire scheme cannot succeed, and design the four-terminal measurement that can. _(Olympiad)_

<details>
<summary>Solution</summary>

**Two wires:** the voltmeter across the specimen's *terminals* includes both leads: $V=I(R+0.02)$ — the lead contribution alone is $0.02/0.1=20\%$, ten times the budget before any contact resistance. Passing the voltage leads through the ammeter's 0.5 $\Omega$ is even worse (600%, ch 5 Q8). No instrument quality fixes a topology error.

**Four terminals:** solder *current* leads at the outer pair, *voltage* leads at inner points on the shunt body. The voltage circuit carries (with a DMM or potentiometer) essentially zero current, so its leads drop nothing: $V=IR$ for the metal *between the voltage taps* only. Measure $I$ with any decent series ammeter (its resistance now sits outside the measured region and affects only the source setting) and $V$ with the null instrument. Errors left: tap-position uncertainty (~mm on a cm-scale shunt, <1%) and the current measurement — both inside budget. **Check:** this is why precision shunts, standard resistors and bus bars are *born* with four terminals; the geometry of the measurement is the correction.

</details>

### 6.6 Chapter summary — the results to own

> **Conversions, loading, nulls**
>
> $$
> S=\frac{G}{n-1};\qquad R_m=\frac{V}{I_g}-G;\qquad V_{read}=V\frac{R_2\parallel R_V}{R_1+R_2\parallel R_V};\qquad \frac{R}{S}=\frac{l}{100-l};\qquad r=R\frac{l_0-l}{l}
> $$
>
>  Ammeters shunt small, voltmeters multiply large — and both still lie by exactly the Thevenin arithmetic of chapter 5. Null methods (bridge, potentiometer) move the precision from the meter to a length ratio and draw no current at balance. Four terminals kill lead resistance by topology, not calibration.

### 6.7 Checkpoint

- I can convert a galvanometer to any current or voltage range, including the power rating of the added element.
- I can compute a voltmeter's loading error in one line from its ohms-per-volt rating.
- I can run a meter bridge including the end-error swap, and say why averaging a ratio pair works.
- I can explain — to a sceptic — why the potentiometer reads EMF and the voltmeter reads terminal voltage.
- I can look at a low-resistance measurement and say "four terminals" before anyone asks.

Next: [**Chapter 7 · Advanced topics →**](#section-07-advanced-topics) — fuses, transmission, thermoelectricity, thermistors, superconductors, and the discipline of the estimate.

<a id="section-07-advanced-topics"></a>

_Chapter 7 of 11 · Olympiad · advanced · ≈ 50 min read · 8 questions_

## Advanced topics: where the syllabus ends and physics continues

Five topics that Olympiad papers love and textbooks compress: why a fuse blows (a scaling law with an exponent you must derive), why transmission lines run at kilovolts, how a thermocouple turns temperature into voltage (with two characteristic temperatures examiners quote interchangeably to catch you), how a thermistor's self-heating finds its own operating point, and what a superconductor changes about chapter 1's ledger. The mistake this chapter prevents: quoting a scaling law without deriving its exponent — in an oral that is a lost mark, in a written paper a lost question.

### 7.1 The fuse: a $I\propto r^{3/2}$ world

> **Deriving the fuse law — steady state, then scale**
>
> A straight wire of radius $r$, length $L$, resistivity $\rho$, carrying current $I$ in still air. Steady state: electrical heating = convective loss. Heating $P=I^{2}\rho L/\pi r^{2}$; loss $=h\,(2\pi rL)\,\Delta T$ (Newtons law of cooling, coefficient $h$, allowed temperature rise $\Delta T$). Equate and solve for $I$:
>
>  $$
> I=\sqrt{\frac{2\pi^{2}h\,\Delta T}{\rho}}\ r^{3/2} \qquad\Rightarrow\qquad \boxed{I\propto r^{3/2}} \tag{7.1}
> $$
>
>  The length cancels — a longer fuse is not a better fuse, a fact every apprentice electrician rediscovers — and the radius enters as the 3/2 power: **double the radius and the safe current grows by $2^{3/2}=2.83$**, not by 2 or 4. The same law reverse-engineered a fuse: a 32 mm cartridge and a 6 mm one of equal rating have similar wire radii, because $L$ never mattered.

> **The cancellation is a design command**
>
> That $r$ drops out of $j=I/\pi r^{2}\propto r^{-1/2}$ says current density alone never fixes thermal safety: a thin wire runs at higher current *density* at the same temperature. For house wiring the relevant scaling is the same equation solved for $\Delta T$: $\Delta T\propto j^{2}r^{?}$ — recompute it: $\Delta T=\rho I^{2}/(2\pi^{2}h r^{3})=\rho j^{2}\pi r^{4}/(2\pi^{2}hr^{3})\propto j^{2}r$: thick cables tolerate a higher current density at the same temperature rise. Codes permit 2–5 A/mm² in copper; the bare-wire air estimate of Q1 lands in that county with nothing but $h\sim10$ W m⁻²K⁻¹.

### 7.2 Transmission: the case for kilovolts

> **Result · line loss scales as $1/V^{2}$**
>
> Deliver power $P$ through a line of total resistance $R_{line}$ at transmission voltage $V$: the line current is $I=P/V$ and the loss is
>
>  $$
> P_{loss}=I^{2}R_{line}=\frac{P^{2}R_{line}}{V^{2}} \tag{7.2}
> $$
>
>  Numbers to own: $P=100$ kW over $R_{line}=10\ \Omega$. At 200 V: $I=500$ A and the line burns $2.5$ **MW** — 25 times the delivered power: the scheme is impossible, not merely inefficient. At 20 kV: $I=5$ A, loss 250 W — **0.25%**. Ten thousand-fold reduction for a hundred-fold voltage step; that arithmetic, not corporate conspiracy, is why pylons exist.

![The same 100 kW delivered at 200 volts and at 20 kilovolts, with the line losses drawn to scale](assets/figures/fig-024.svg)

**Fig. 7.1 — Two transmission plans, drawn honestly.** The 200 V plan cannot even be drawn: its loss bar is 25 times its delivery bar. The 20 kV plan's loss is invisible at this scale — 0.25%.

### 7.3 Thermoelectricity: Seebeck, with two temperatures

> **Definition · the thermocouple**
>
> Two junctions of dissimilar metals at temperatures $T_1$ (cold) and $T_2$ (hot) drive a current — the **Seebeck effect**; the EMF is an energy-per-charge statement exactly like ch 3's $\mathcal E$, with thermal transport playing the pump's role. Over a useful range the EMF against a 0 °C reference follows
>
>  $$
> \mathcal E=aT-bT^{2}\qquad(\text{Cu--Fe: }a\approx41\ \mu\text{V/K}, \ b\approx0.16\ \mu\text{V/K}^{2}) \tag{7.3}
> $$
>
>  Define the **neutral temperature** $T_n$: where $\mathcal E$ peaks ($d\mathcal E/dT=0$), and the **inversion temperature** $T_i$: where $\mathcal E$ crosses zero and changes sign. Differentiate:
>
>  $$
> T_n=\frac{a}{2b},\qquad T_i=\frac{a}{b}=2T_n \qquad\text{(for Cu--Fe: }\approx128\ ^\circ\text{C and }\approx256\ ^\circ\text{C)} \tag{7.4}
> $$

> **The trap in this section**
>
> Confusing $T_n$ and $T_i$. The reply, in one breath: **neutral = maximum EMF = a/2b; inversion = zero EMF = a/b = twice the neutral**. Half the thermocouple questions ever set are this pairing worn in a different coat. Second trap: quoting $\mathcal E=aT-bT^{2}$ outside its range — the parabola is a fit over a few hundred kelvin, not a law of nature; at 1000 °C real couples are calibrated tables, not algebra.

> **Why the EMF must peak**
>
> The Seebeck EMF is the net of two contact contributions (one per junction), each roughly proportional to the temperature difference that drives carrier diffusion. As the hot-junction temperature rises, the EMF first grows — more diffusion pressure — but the second-order term (Thomson heat along the wires' temperature gradients) grows faster and eventually cancels then reverses the net. The reversal is physical, not a fit artefact: beyond $T_i$ the current direction flips. Peltier (current at a junction pumps heat) and Thomson (heat absorbed along a current-carrying gradient) are the two sibling effects; a thermoelectric cooler is Peltier run backward, and its COP analysis is a favourite long question.

### 7.4 The thermistor finds its own operating point

> **Self-heating as a load line**
>
> A thermistor obeys roughly $R(T)=R_0e^{\beta(1/T-1/T_0)}$ with $\beta\approx3000$–4000 K — ch 2's carrier explosion in one constant. Feed it and it heats *itself*: electrical power in must equal $\delta(T-T_{amb})$ out (dissipation constant $\delta\sim$ mW/K in still air). The operating point is the intersection of the device's $I(V)$ curve with the thermal load line $P=\delta\Delta T$. Below the intersection the curve is ohmic; above it, warming lowers $R$, raises $I$, warms further — **negative resistance territory**, and the crossing can be unstable (a run-away Q5 examines numerically). This is the same fixed-point thinking as ch 4's infinite ladder, wearing thermal clothes.

![Thermistor I-V curve with a thermal load line: stable operating point at the first intersection, unstable runaway beyond the peak](assets/figures/fig-025.svg)

**Fig. 7.2 — An NTC thermistor's $I$–$V$ curve and the thermal load line.** Left of the peak the device behaves; the descending branch is negative differential resistance sustained by self-heating. Circuit designs live on the rising branch on purpose.

### 7.5 Superconductors: the ledger with no tax

> **Definition · the DC superconductor**
>
> Below a critical temperature $T_c$ (e.g. 4.2 K mercury, 9.3 K niobium, 92 K YBCO) a superconductor carries DC current with **exactly zero resistance** — not small, zero. Chapter 1's ledger survives intact: the continuity equation still demands closed current loops, but with $\rho=0$ nothing damps them. A ring opened, cooled, closed and induced carries its current for $\tau=L/R$; with measured lower bounds on $R$ below $10^{-18}\ \Omega$ for a 10 $\mu$H loop, $\tau>3\times10^{11}$ s ≈ ten thousand years — the experiment that retired all "it's just a very good conductor" theories. Also true and examinable: **flux freezing** (the trapped flux $\Phi=LI$ is fixed — the ring adjusts $I$ to keep it), the **critical field** $B_c(T)$ that kills superconductivity, and the **Meissner effect** (expulsion of $B$, which a perfect conductor alone would *not* produce — that distinction is a real viva question).

> **What breaks and what survives**
>
> Ohm's law dies (no field is needed to sustain current — $\vec j$ with $\vec E=0$ violates $\vec j=\sigma\vec E$ unless $\sigma\to\infty$, which is the point). KCL/KVL survive untouched (charge and energy conservation are not negotiable). The drift picture of ch 1 survives with $\tau\to\infty$ — coherent pairs instead of collision-rich electrons. What this course deliberately does not do: the microscopic mechanism (BCS pairs, energy gap) and Josephson junctions — recorded in the topic README's "deliberately not covered".

### Worked example 7.1 · The piecewise discipline — a diode circuit done honestly

A 3 V battery, a 100 $\Omega$ resistor and a silicon diode (forward drop 0.7 V, dynamic resistance negligible) in series. **Plan:** nonlinear element ⇒ guess its state, solve linearly, check the guess. **Do:** guess "on": loop gives $I=(3-0.7)/100=23$ mA. Check: 23 mA forward is comfortably on for a signal diode, and the diode voltage is $+0.7$ V — consistent. **Reverse the battery** and the guess must be "off": current ≈ 0, and the *check* is that the resistor then has zero drop, leaving the full −3 V across the diode, which a reverse-biased junction happily blocks. **What is forbidden:** treating the diode as a resistor and superposing — ch 5, Q5 said why. Swap the diode for an LED of 2.0 V forward drop and the same arithmetic gives 10 mA — the whole of "LED resistor sizing" is this line.

### 7.6 Questions

### **Q1** A bare horizontal copper wire must stay within $\Delta T=40$ K of ambient in still air ($h=10$ W m⁻²K⁻¹, $\rho=1.7\times10^{-8}\ \Omega$m). Show that the safe current is independent of wire length but scales as $r^{3/2}$, and evaluate the current and current density for a wire of radius 0.5 mm. _(Olympiad · estimation)_

<details>
<summary>Solution</summary>

Per unit length, electrical heating $=I^{2}\rho/\pi r^{2}$ and convective cooling $=h\,2\pi r\,\Delta T$. Equate:

$$
I^{2}=\frac{2\pi^{2}h\,\Delta T}{\rho}\,r^{3} \ \Rightarrow\ I=\sqrt{\frac{2\pi^{2}h\,\Delta T}{\rho}}\;r^{3/2}=6.8\times10^{5}\,r^{3/2}
$$

with $I$ in amperes and $r$ in metres; $L$ has cancelled — a longer wire is not a safer wire. For $r=5\times10^{-4}$ m: $I=6.8\times10^{5}\times1.12\times10^{-5}=7.6$ A, and $j=I/\pi r^{2}=7.6/7.85\times10^{-7}=9.7\ \text{A mm}^{-2}$.

**Check:** $j\propto r^{-1/2}$ — thinner wire runs at *higher* current density for the same temperature, so no j-based safety rule can be wire-independent. Wiring codes allow 5–10 A/mm² for bundled, insulated cable: our bare-wire single-figure lands in the same county once the real $h$ (moving air, conduction into terminals) and the larger allowed $\Delta T$ enter. The estimate's virtue is the county, not the digit.

</details>

### **Q2** A 500 kW load is fed over a line of total resistance 8 $\Omega$. Compare line losses at 25 kV and at 250 V, and state the highest power the 250 V scheme could possibly deliver. _(JEE advanced)_

<details>
<summary>Solution</summary>

At 25 kV: $I=P/V=20$ A; loss $=400\times8=3.2$ kW = **0.64%** of 500 kW. At 250 V: $I=2000$ A; loss $=4\times10^{6}\times8=32$ **MW** — 64 times the load power. The 250 V scheme delivers nothing: the maximum power the line could pass, even into a matched load, is $P_{\max}=V^{2}/4R_{line}=250^{2}/32=1.95$ kW with all of it burned half-and-half (ch 5). **Check:** loss ratio $=\big(250/25000\big)^{2}=10^{-4}$ ✓ consistent with 3.2 kW/3200 MW… careful: 32 MW/3.2 kW $=10^{4}$ ✓. Low-voltage transmission is not an engineering compromise; it is arithmetically void.

</details>

### **Q3** A Cu–Fe thermocouple obeys $\mathcal E=40T-0.08T^{2}$ (µV, T in °C, cold junction at 0 °C). Find the neutral and inversion temperatures and the maximum EMF. A student claims the EMF at the inversion point is "the largest negative value possible". Correct them. _(JEE advanced)_

<details>
<summary>Solution</summary>

$$
T_n=\frac{40}{2\times0.08}=250\ ^\circ\text{C},\qquad T_i=\frac{40}{0.08}=500\ ^\circ\text{C}=2T_n,\qquad \mathcal E_{\max}=40(250)-0.08(250)^{2}=10^{4}-5\times10^{3}=5.0\ \text{mV}
$$

**Correction:** at the inversion point $\mathcal E=0$ — the EMF crosses zero and changes sign; the largest negative value on this parabola lies beyond $T_i$ at the edge of the fit's validity (at 400 °C it is already $40\times400-0.08\times1.6\times10^{5}=16-12.8=3.2$ mV, still positive). The trap is reading "inversion" as "most negative" — the word describes the *direction of the current* inverting, at zero EMF. **Check:** vertex of a downward parabola at $a/2b$ ✓; root at $a/b$ ✓; $T_i=2T_n$ always, for this form ✓.

</details>

### **Q4** A divider has a 1.0 k$\Omega$ upper resistor and an NTC thermistor (4.0 k$\Omega$ at 25 °C, $\beta=3500$ K) to a 12 V source. Find the output at 25 °C and at 55 °C, and estimate the thermistor's self-heating power at the cold end if the dissipation constant is 5 mW/K. _(JEE advanced)_

<details>
<summary>Solution</summary>

25 °C: $V_{out}=12\times4/5=9.6$ V. 55 °C: $R=R_0e^{\beta(1/T-1/T_0)}$ with $1/328-1/298=-30/97\,744=-3.07\times10^{-4}\ \text{K}^{-1}$, so the exponent is $3500\times(-3.07\times10^{-4})=-1.074$ and $R=4\times e^{-1.074}=4\times0.342=1.37$ k$\Omega$. Then $V_{out}=12\times1.37/2.37=6.9$ V — a 2.7 V swing over 30 K, i.e. ≈90 mV/K: a thermometer with no moving parts. **Self-heating:** at the cold point the thermistor dissipates $9.6^{2}/4000=23.0$ mW ⇒ $\Delta T=23.0/5=4.6$ K — the "25 °C" reading is really of a thermistor self-warmed to ≈30 °C, and honest calibration subtracts this offset. **Check:** at the hot end the dissipation rises to $6.9^{2}/1370=34.8$ mW ($\Delta T=7.0$ K): the divider feeds the thermistor more voltage share as its resistance falls toward the 1 k$\Omega$ partner — which is precisely why stability needs an argument, and Q5 supplies it.

</details>

### **Q5** Show that a thermistor in series with a fixed resistor across a supply is thermally stable, while the same thermistor fed from a stiff voltage source alone can run away. Use the load-line language of §7.4. _(Olympiad)_

<details>
<summary>Solution</summary>

**With a series resistor:** suppose the thermistor warms by $dT$; its resistance falls by $dR<0$, so its voltage share $V_{th}=V_{supply}R_{th}/(R_s+R_{th})$ falls and its power $P=V_{th}^{2}/R_{th}$ changes by

$$
\frac{dP}{dR_{th}}=V_s^{2}\,\frac{R_s-R_{th}}{(R_s+R_{th})^{2}}
$$

If $R_{th}< R_s$ (our divider: 4 k vs 1 k fails this — but the *thermistor branch* sees the 1 k as its series partner, 4 k > 1 k, so $dP/dR<0$): falling $R$ **raises** power when $R_{th}< R_s$ and lowers it when $R_{th}> R_s$. Stability requires $dP/dT<\delta$ (power gain per kelvin below the cooling rate): the series resistor caps the current, so past the peak of Fig. 7.2 the operating point slides **back** to a unique stable crossing. **Stiff source alone:** $P=V^{2}/R_{th}$ grows without bound as $R$ falls — the load line is horizontal, no second crossing exists, and the device destructures. **Check:** the crossover is at $R_{th}=R_s$ — maximum power transfer (ch 5) is exactly the stability boundary in thermal clothes ✓. This is why NTC inrush limiters always ship with (or act as) their own series element.

</details>

### **Q6** A superconducting ring of inductance 10 $\mu$H is cooled below $T_c$ while carrying zero current, threaded by 0.5 mWb of flux; the flux source is removed. Find the persistent current and the smallest decay time consistent with measured resistance bounds. _(Olympiad)_

<details>
<summary>Solution</summary>

Flux freezing: the ring keeps $\Phi=LI$ fixed at its trapped value:

$$
I=\frac{\Phi}{L}=\frac{0.5\times10^{-3}}{10\times10^{-6}}=50\ \text{A}
$$

Decay time $\tau=L/R$; laboratory bounds put $R<10^{-18}\ \Omega$ for such a loop, so $\tau>10^{-5}/10^{-18}=10^{13}$ s ≈ $3\times10^{5}$ years. **Check:** the current does real work on nothing (zero resistance), so 50 A costs nothing to maintain — the flux, not the current, is the conserved object; the current is whatever $\Phi/L$ demands. If the ring were warmed through $T_c$, the flux would escape and the current would collapse — superconductivity, not inertia, is doing the holding.

</details>

### **Q7** Why are there no superconducting long-distance power lines in commercial use, even though $\rho=0$ makes line loss zero? Give three physical reasons and one economic one. _(Olympiad · synthesis)_

<details>
<summary>Solution</summary>

**1. Cooling is a loss:** keeping hundreds of kilometres at 77 K (or 4 K) consumes compressor power continuously — the "zero" loss is replaced by a fixed cryogenic tax that scales with length exactly as $I^{2}R$ did. **2. Critical limits:** superconductivity dies above a critical current density, field and temperature; a fault surge (lightning, short) can quench kilometres of cable in milliseconds, dumping $\tfrac12LI^{2}$ as heat inside a cold, brittle system. **3. AC is not free:** superconductors are perfect for DC; AC suffers hysteresis and coupling losses in the very currents grids mostly carry (and our syllabus's DC-only claim — see "deliberately not covered"). **4. Economics:** copper at 0.25% loss (§7.2) costs almost nothing to beat; the capital and maintenance of cryogenics cannot amortise against 0.25%. **Check:** where cryogenics already exists for other reasons — MRI magnets, particle accelerators — superconducting transport *is* used, tens of kiloampères at zero loss ✓. The lesson generalises: no technology wins in the abstract, only against a measured alternative.

</details>

### **Q8** A "30 A, 32 mm" cartridge fuse has a wire of radius 0.15 mm. Using $I\propto r^{3/2}$ with this as reference, estimate the rating of the same alloy drawn to 0.30 mm, and the radius needed for a 100 A fuse. State one assumption that could break the scaling. _(JEE advanced)_

<details>
<summary>Solution</summary>

Doubling the radius: $I=30\times(0.30/0.15)^{3/2}=30\times2.83=84.8\approx85$ A. For 100 A: $r=0.15\times(100/30)^{2/3}=0.15\times(3.333)^{0.667}=0.15\times2.23=0.335$ mm. **Assumptions that can break it:** uniform $\rho$ (fuse alloys have $\alpha\sim4\times10^{-4}$, small but the blow point is a runaway where heating outruns cooling — the blow threshold sits where $dP/dT$ overtakes $\delta$, the thermistor logic of Q5 in metal clothes); end-cooling (short fuses conduct heat into their caps, length sneaking back in); and convection vs radiation at high temperature (melting-point wires radiate as $T^{4}$, bending the exponent). **Check:** catalogue cross-check — real 0.3 mm fuse wire ratings run 60–100 A depending on alloy and enclosure: our 85 A is in the county ✓.

</details>

### 7.7 Chapter summary — the results to own

> **Scaling, stability, and the estimate**
>
> $$
> I_{fuse}\propto r^{3/2};\qquad P_{loss}=\frac{P^{2}R_{line}}{V^{2}};\qquad T_n=\frac{a}{2b},\ T_i=2T_n;\qquad \text{stability} \iff dP/dT<\delta;\qquad I=\Phi/L\ \text{(flux freezing)}
> $$
>
>  Every scaling law here came from equating two rates — heating with cooling, electrical with thermal, electrical with convective. That habit — name the two flows, equate, scale — generates more Olympiad answers than any formula sheet. The diode discipline (guess state, solve linear, check guess) is the only legal method once superposition's licence is revoked.

### 7.8 Checkpoint

- I can derive $I\propto r^{3/2}$ for a fuse in three lines and say which assumptions give the 3/2.
- I can compute transmission loss at any voltage and explain the $1/V^{2}$ scaling in one sentence.
- I can find $T_n$, $T_i$ and $\mathcal E_{\max}$ for any $aT-bT^{2}$ couple without hesitating over which is which.
- I can find a thermistor's operating point and say whether it is stable, using $dP/dT$ vs $\delta$.
- I can state what superconductivity changes in ch 1's ledger (nothing — and everything about $\tau$).

Next: [**Chapter 8 · The playbook →**](#section-08-playbook) — triage, the twelve moves, every trap in one list, and a timed drill.

<a id="section-08-playbook"></a>

_timed drill inside · triage + traps · ≈ 35 min read · 15-question drill_

## 8 · The playbook: triage, moves, traps, numbers

Everything from chapters 1–7, compressed into the form you can carry into a timed room: how to *classify* a problem in twenty seconds, the twelve moves that solve ninety percent of them, the traps with their one-line replies, the numbers worth memorising, and a 15-question drill to run against the clock. This chapter is a tool, not a read — mark it up.

### 8.1 Triage: what kind of problem is this?

| the problem says… | you are in… | the move |
| --- | --- | --- |
| "drift velocity", "number of electrons per second" | ch 1 ledger | $I=neAv_d$; count = $I/e$; sanity: $v_d\sim$ sub-mm/s |
| "stretched", "reshaped", cone, shell, "material between spheres" | ch 2 geometry | $R=\int\rho\,dl/A$; name the equipotentials first; stretch ⇒ $R\propto l^{2}$ |
| "temperature rises/falls", "thermistor", "filament" | ch 2 materials | which factor of $\sigma=ne^{2}\tau/m$ moved? $R_T=R_0(1+\alpha\Delta T)$ locally |
| "terminal voltage", "charging", "internal resistance", "maximum current from n cells" | ch 3 cell model | $V=\mathcal E\mp Ir$; sign by charge/discharge; grouping optimum $mR=nr$ |
| "find all currents", two loops, three loops | ch 4 algorithm | guess arrows, KCL+KVL, solve, **audit powers** |
| "cube", "symmetric network", "ladder", "bridge is balanced" | ch 4 symmetry | find equal potentials; delete dead branches; $R_\infty$ fixed point |
| "galvanometer current", "unbalanced bridge", "what the meter reads" | ch 5 Thevenin | $V_{th},R_{th}$ at the terminals, then one divider; short-circuit current $=V_{th}/R_{th}$ |
| "maximum power", "matched load", "efficiency" | ch 3/5 | reduce to Thevenin; $R_L=R_{th}$, $\eta=50\%$ — then ask if matching is even wanted |
| "ammeter", "voltmeter", "shunt", "multiplier", "loading" | ch 6 | one divider with the meter's resistance inside it; $\Omega$/V = sensitivity |
| "potentiometer", "null", "balance length" | ch 6 | no current flows at balance: EMF from length ratios; $r=R(l_0-l)/l$ |
| "fuse", "transmission line", "thermocouple", "persistence of current" | ch 7 scaling | name the two flows (heating/cooling, electrical/thermal), equate, scale |

![Triage flow: nonlinear element, sources varied, geometry, meters, leading to the matching method](assets/figures/fig-026.svg)

**Fig. 8.1 — The triage flow.** Classification is the solution's first third; the audit line is its last third. The middle is arithmetic.

### 8.2 The twelve moves

1. **Label every current with a guessed direction** before writing a single equation (ch 4).
2. **Reduce series/parallel only between named nodes** — "drawn side by side" is not parallel.
3. **Audit powers** as the closing bracket of every network solve: $\sum\mathcal EI=\sum I^{2}R$.
4. **Name equal potentials by symmetry**; delete or merge them before algebra (cube, balanced bridge).
5. **Thevenin at the terminals of the thing asked about** — meters, galvanometers, "what if the load is…".
6. **Kill sources correctly**: voltage → wire (keep $r$), current → break.
7. **Check limits**: $R\to0$, $R\to\infty$, $\kappa$-style parameters → their trivial cases.
8. **Convert the meter question into a divider question** — every instrument is a resistance wearing a badge.
9. **Null beats deflection**: if the problem offers a balance condition, the detector's resistance is irrelevant.
10. **Scale before computing**: write $I\propto r^{3/2}$-type laws first; exponents are the marks.
11. **For cell groupings**, compute all three groupings if unsure — the arithmetic is 30 seconds total.
12. **Estimate the answer's size** before the exact calculation; trust nothing that violates the estimate.

### 8.3 Traps — the wrong answer, and the one-line reply

> **Current and drift (ch 1)**
>
> - "Electrons travel near light speed." Reply: $v_d=I/neA\sim0.1$ mm/s; the *field* travels at $\sim c$.
> - "Current is a vector; wires at an angle add like vectors." Reply: current is a flux (scalar); only $\vec j$ is a vector.
> - "Electrons accelerate continuously along a wire." Reply: $\tau\sim10^{-14}$ s; drift is a terminal velocity.
> - "Thicker wire, more electrons per second." Reply: count = $I/e$; only the speed changes.

> **Resistance and materials (ch 2)**
>
> - "Stretch to $k\,l$ ⇒ $R\to kR$." Reply: volume fixed ⇒ $R\to k^{2}R$.
> - "Average the cross-section for a taper." Reply: reciprocals add; frustum gives $\rho l/\pi ab$ (geometric mean).
> - "All conductors heat up in the same direction." Reply: metals via $\tau\downarrow$, semiconductors via $n\uparrow$ — opposite signs.
> - "A diode is a resistor of $V/I$." Reply: that ratio is an operating point, not a property; dynamic vs static.

> **Cells and networks (ch 3–5)**
>
> - "A 12 V battery supplies 12 V always." Reply: terminal voltage is $\mathcal E-Ir$, and $\mathcal E+Ir$ on charge.
> - "Parallel cells halve the EMF." Reply: EMF never halves; $r$ does.
> - "Maximum power ⇒ maximum efficiency." Reply: at $R=r$, $\eta=50\%$ exactly.
> - "Superpose the powers." Reply: superpose currents; square afterwards.
> - "Killed voltage source = removed." Reply: killed = wire, $r$ stays; killed current source = break.
> - "Reciprocity preserves open-circuit voltages." Reply: it preserves $V/I$ ratios (short-circuit currents), not open voltages.

> **Instruments and advanced (ch 6–7)**
>
> - "The voltmeter reads the true voltage." Reply: the meter is a load; check $R_V$ vs the divider impedance.
> - "An ideal ammeter changes nothing." Reply: 0 $\Omega$ is fine in parallel-rich circuits but a 0.5 $\Omega$ real one wrecks low-resistance work — four terminals.
> - "Neutral and inversion temperatures are the same." Reply: $T_n=a/2b$ (max EMF), $T_i=2T_n$ (zero EMF).
> - "A fuse twice as thick carries twice the current." Reply: $2^{3/2}=2.83$ times.
> - "A perfect conductor is a superconductor." Reply: Meissner effect distinguishes them; a perfect conductor traps flux, a superconductor expels it.

### 8.4 Numbers to own (memorise, with units)

| $e=1.6\times10^{-19}$ C; 1 A = $6.25\times10^{18}$ electrons/s | Cu: $\rho=1.7\times10^{-8}\ \Omega$m, $n=8.5\times10^{28}\ \text{m}^{-3}$, $\alpha=3.9\times10^{-3}\ \text{K}^{-1}$ |
| --- | --- |
| drift speed in house wiring $\sim0.1$ mm/s; $\tau\sim10^{-14}$ s; thermal speed $\sim10^{6}$ m/s | Al: $\rho=2.7\times10^{-8}$, $n=1.8\times10^{29}$; manganin $\alpha\approx2\times10^{-5}\ \text{K}^{-1}$ |
| cube of $R$: $7R/12, 3R/4, 5R/6$; ladder $R_s=R_p=R\Rightarrow\varphi R=1.618R$ | air breakdown $\approx3$ kV/mm; Si $E_g=1.1$ eV, $n$ doubles per $\sim$10 K |
| matched load: $P_{\max}=V_{th}^{2}/4R_{th}$, $\eta=50\%$ | thermocouple Cu–Fe: $T_n\approx128\ ^\circ$C, $T_i\approx256\ ^\circ$C, $\mathcal E_{\max}$ few mV |

### 8.5 The timed drill — 15 questions, 30 minutes

Answers below each question are collapsible; do ten first, then mark. Every answer includes the **reason** worth carrying, not just the number.

### **Q1** Drift speed of electrons in a copper wire of cross-section 0.5 mm² carrying 2 A ($n=8.5\times10^{28}$). _(90 s)_

<details>
<summary>Solution</summary>

$v_d=I/neA=2/(8.5\times10^{28}\times0.5\times10^{-6}\times1.6\times10^{-19})=0.29$ mm/s. **Reason to keep:** sub-mm/s always; if your answer exceeds 1 mm/s in copper you slipped a factor of 10.

</details>

### **Q2** A wire is stretched to 3× its length. New resistance? _(30 s)_

<details>
<summary>Solution</summary>

$9R$ — $R\propto l^{2}$ at fixed volume. **Reason:** both length and area move, in opposite directions in the formula, quadratically overall.

</details>

### **Q3** A 6 V battery of $r=0.5\ \Omega$ drives $R=5.5\ \Omega$. Terminal voltage? _(45 s)_

<details>
<summary>Solution</summary>

$I=1$ A, $V=6-0.5=5.5$ V. **Reason:** with $R=r\times11$, the sag is $r/(R+r)=8.3\%$ of EMF — always sanity-check the sag against the $r:R$ ratio.

</details>

### **Q4** A Wheatstone bridge balances with arms 20, 30, 40, and $x$. Find $x$. _(30 s)_

<details>
<summary>Solution</summary>

$x=60\ \Omega$ — products equal: $20x=30\times40$. **Reason:** balance is a products condition, immune to which diagonal holds the battery (reciprocity).

</details>

### **Q5** Twelve 10 $\Omega$ resistors form a cube. Resistance across a body diagonal? _(60 s)_

<details>
<summary>Solution</summary>

$5R/6=8.33\ \Omega$ — currents $I/3, I/6, I/3$ through the three classes. **Reason:** symmetry plane first, arithmetic second; never solve the cube by loop equations.

</details>

### **Q6** A 500 $\Omega$, 200 µA galvanometer becomes a 1 mA ammeter. Shunt? _(60 s)_

<details>
<summary>Solution</summary>

$S=GI_g/(I-I_g)=500\times0.2/0.8=125\ \Omega$. **Reason:** same voltage: coil and shunt currents in inverse ratio to resistances; $n=5\Rightarrow S=G/4$.

</details>

### **Q7** A 10 V battery of $r=1\ \Omega$: maximum power deliverable? _(45 s)_

<details>
<summary>Solution</summary>

$V^{2}/4r=25$ W at $R=1\ \Omega$. **Reason:** matched load, half the voltage across each; efficiency there is 50% — never quote one without the other.

</details>

### **Q8** A thermocouple follows $\mathcal E=30T-0.05T^{2}$ (µV, °C). Neutral temperature and peak EMF? _(60 s)_

<details>
<summary>Solution</summary>

$T_n=a/2b=300\ ^\circ$C; $\mathcal E_{max}=30\times300-0.05\times9\times10^{4}=4.5$ mV. **Reason:** vertex of the parabola; inversion sits at $600\ ^\circ$C, where $\mathcal E=0$.

</details>

### **Q9** Infinite ladder: $R_s=3\ \Omega$ series arms, $R_p=1\ \Omega$ shunts. Input resistance? _(90 s)_

<details>
<summary>Solution</summary>

$R=\big(3+\sqrt{9+12}\big)/2=3.79\ \Omega$. **Reason:** fixed point $R=R_s+R_pR/(R_p+R)$; take the positive root; verify by one iteration ($3+3.79/4.79=3.79$ ✓).

</details>

### **Q10** A 1000 $\Omega$/V voltmeter on its 50 V range reads a 100 V source divided by two 100 k$\Omega$ resistors. Reading? _(90 s)_

<details>
<summary>Solution</summary>

Meter resistance 50 k$\Omega$; lower arm becomes 100k∥50k=33.3 k$\Omega$; reading $=100\times33.3/133.3=25$ V (true 50). **Reason:** divider impedance (100 k) vs meter (50 k) — the meter is not a passenger, it is a load.

</details>

### **Q11** Potentiometer: null at 150 cm; with $R=2\ \Omega$ across the cell, null at 100 cm. Internal resistance? _(60 s)_

<details>
<summary>Solution</summary>

$r=R(l_0-l)/l=2\times50/100=1.0\ \Omega$. **Reason:** at the second null the cell is delivering current $\mathcal E/(R+r)$; the wire reads its terminal voltage — the ratio does the rest.

</details>

### **Q12** 40 W and 100 W lamps (rated 220 V) in series across 220 V. Which is brighter, and total power? _(90 s)_

<details>
<summary>Solution</summary>

$R_{40}=1210\ \Omega$, $R_{100}=484\ \Omega$; $I=220/1694=0.13$ A; powers 20.4 W and 8.2 W — the **40 W lamp is brighter**, total 28.6 W. **Reason:** series favours the larger resistance; "bigger lamp" is a parallel intuition.

</details>

### **Q13** In mains (50 Hz) the drift oscillates. Amplitude of the electron's excursion in the ch 1 wire (1 A, 1 mm²)? _(90 s)_

<details>
<summary>Solution</summary>

$v_{d,0}=I/neA=7.35\times10^{-5}$ m/s; excursion $=v_{d,0}/\omega=7.35\times10^{-5}/314=0.23\ \mu$m. **Reason:** at 5 A it was 1.2 µm; the excursion scales with current — sub-micrometre at household currents, always.

</details>

### **Q14** A fuse wire's radius is halved. Its rating becomes…? _(45 s)_

<details>
<summary>Solution</summary>

$(1/2)^{3/2}=0.354$ of the original — about a third. **Reason:** heating per length grows as $1/r^{2}$, cooling surface as $r$; the exponent is the quotient's square root.

</details>

### **Q15** The bridge of ch 5 (arms 10, 20, 30, 40; 10 V): a student swaps battery and galvanometer diagonals and re-measures the short-circuit current. What does she get? _(60 s)_

<details>
<summary>Solution</summary>

$V_{th}/R_{th}=40.0$ mA — identical (reciprocity), though the open-circuit voltage changes to 0.833 V. **Reason:** the invariant is the ratio; the open voltage was never promised to survive the swap.

</details>

Next: [**Chapter 9 · The paper →**](#section-09-olympiad-paper) — 36 questions, 245 marks, three hours. It is time.

<a id="section-09-olympiad-paper"></a>

_INPhO / IPhO standard · JEE Advanced format · 3 hours · 36 questions_

## 9 · The paper: current electricity, from drift to reciprocity

Thirty-six questions, four sections, three hours. Every section of chapters 1–7 is examined by at least two questions; the coverage map below says which. Attempt it in one sitting, with a non-programmable calculator, and mark yourself with [part 10](#section-10-olympiad-solutions) only afterwards — the paper's value is the two hours you spend deciding what to write, not the marking.

> **Instructions**
>
> - **Time:** 180 minutes. Suggested split — Section A 40 min, B 25 min, C 35 min, D 80 min.
> - **Section A** (Q1–Q12): *exactly one* option is correct; +3 for it, 0 for unanswered, −1 for anything
>   else. Do not second-guess a question you have already checked with a limit — a limit is stronger than a doubt.
> - **Section B** (Q13–Q18): one or more options correct; +4 if all correct and none wrong, +1 for each correct
>   option left unmarked with no wrong mark, 0 for none marked, −2 otherwise.
> - **Section C** (Q19–Q26): numerical, +4/0; give the value to the precision asked. Units are stated in the
>   table; a correct number with a wrong prefix scores zero, so state the prefix.
> - **Section D** (Q27–Q36): long questions, marks as printed — nine at [15] and Q36 at [18], total 153; the
>   paper is 245 marks in all. Start every answer with the principle you are using and end with a check — both carry
>   marks even when the algebra slips.
> - **Data, unless stated:**$e=1.6\times10^{-19}$ C, $m_e=9.11\times10^{-31}$ kg,
>   Cu: $\rho=1.7\times10^{-8}\ \Omega$m, $n=8.5\times10^{28}\ \text{m}^{-3}$,
>   $g=9.8$ m/s², air breakdown $3$ kV/mm at 1 atm.

| topic | A | B | C | D |
| --- | --- | --- | --- | --- |
| 1 · current, drift, continuity, microscopic Ohm | 1, 4 | 15 | 19 | 27, 36 |
| 2 · resistance, resistivity, temperature, non-ohmic | 2, 3, 12 | 13, 14 | 20, 24 | 29, 34 |
| 3 · EMF, internal resistance, grouping, power audit | 4, 5 | 16 | 25 | 27, 30 |
| 4 · Kirchhoff, symmetry, bridges, ladders | 6, 10, 11 | 15, 17 | 21 | 28, 33 |
| 5 · superposition, Thevenin, Norton, reciprocity | 6, 7 | 18 | 23 | 28, 35 |
| 6 · meters, bridges, potentiometer, loading | 5, 9 | 17 | 22, 23, 25, 26 | 31, 32 |
| 7 · fuses, transmission, thermoelectricity, superconductors | 8, 12 | 14, 18 | 20, 24 | 34, 36 |
| 8 · traps and estimation | all | all | all | all |

### Section A · Single correct (Q1–Q12)

### **Q1** [3] A copper wire carries a steady current. If the wire is replaced by one of the same material with double the cross-section and the same current is maintained, which quantity is unchanged?

- **A** the drift speed of the electrons
- **B** the number of electrons crossing a cross-section per second
- **C** the current density
- **D** the electric field inside the wire

### **Q2** [3] A wire is drawn through a die so that its length increases by 10% (volume conserved). Its resistance increases by approximately

- **A** 10%
- **B** 21%
- **C** 11%
- **D** 33%

### **Q3** [3] Two tungsten lamps rated 60 W and 100 W at 220 V are joined in series to a 220 V supply. Immediately after switch-on, before the filaments heat up, the 100 W lamp briefly

- **A** glows brighter than the 60 W lamp, because it is rated higher
- **B** glows dimmer, because its cold resistance is lower
- **C** stays dark, because a cold filament does not conduct
- **D** explodes, because cold tungsten cannot carry current

### **Q4** [3] A car battery of EMF 12 V and internal resistance 0.01 $\Omega$ drives the starter, which draws 200 A. The terminal voltage during cranking is

- **A** 12 V
- **B** 11 V
- **C** 10 V
- **D** 13 V

### **Q5** [3] A cell is being charged at 2 A. Compared with its EMF, its terminal voltage during charging is

- **A** lower by $Ir$
- **B** higher by $Ir$
- **C** equal, because EMF is a constant of the cell
- **D** zero, since no net charge is delivered to the load

### **Q6** [3] A Wheatstone bridge balances. The battery and the galvanometer are now interchanged. The new balance condition is

- **A** the reciprocal of the old one
- **B** the same as the old one
- **C** the old one with arms re-grouped in series
- **D** no balance exists after the swap

### **Q7** [3] The current drawn from a real source is halved by increasing the load resistance. The internal power loss $I^{2}r$

- **A** halves
- **B** quarters
- **C** stays the same, since $r$ is fixed
- **D** doubles

### **Q8** [3] A fuse wire of a given alloy and length is replaced by another of the same alloy, twice the radius, same length. The safe current becomes

- **A** 2 times
- **B** 4 times
- **C**$2\sqrt2$ times
- **D**$\sqrt2$ times

### **Q9** [3] To convert a galvanometer into a voltmeter of higher range you add

- **A** a low shunt in parallel
- **B** a high multiplier in series
- **C** a high shunt in parallel
- **D** a low multiplier in series

### **Q10** [3] Twelve equal resistors $R$ form a cube. The equivalent resistance between adjacent corners is

- **A**$7R/12$
- **B**$3R/4$
- **C**$5R/6$
- **D**$11R/12$

### **Q11** [3] An infinite ladder of series $R$ and shunt $R$ has input resistance

- **A**$2R$
- **B**$1.618R$
- **C**$2.732R$
- **D**$1.5R$

### **Q12** [3] A 100 W, 220 V lamp is run from a 110 V supply (resistance taken as constant at its hot value). It delivers

- **A** 50 W
- **B** 100 W
- **C** 25 W
- **D** 200 W

### Section B · Multiple correct (Q13–Q18)

### **Q13** [4] Which of the following increase in resistance when their temperature rises moderately (tens of kelvin)?

- **A** a copper coil
- **B** an NTC thermistor
- **C** a carbon-composition resistor
- **D** a platinum resistance element

### **Q14** [4] A metal's resistivity rises roughly linearly with $T$ near room temperature. This is because

- **A** the conduction-electron density grows with $T$
- **B** the relaxation time falls as lattice vibrations grow
- **C** the electron charge changes with temperature
- **D** the conduction-electron density is fixed while $\tau$ shortens

### **Q15** [4] Kirchhoff's junction law follows from

- **A** conservation of charge in steady state
- **B** conservation of energy round a loop
- **C** the continuity equation with $\partial\rho/\partial t=0$ at the node
- **D** Ohm's law applied to the junction

### **Q16** [4] For a cell of EMF $\mathcal E$, internal resistance $r$, delivering current $I$ to $R$:

- **A** chemical power is $\mathcal EI$
- **B** the efficiency of delivery is $R/(R+r)$
- **C** the efficiency at maximum power transfer is 100%
- **D** the internal loss is $I^{2}r$ regardless of $R$

### **Q17** [4] A meter bridge measurement of an unknown $S\approx R$ gains accuracy when

- **A** the balance point is near 50 cm
- **B** the balance point is near 5 cm
- **C**$R$ and $S$ are interchanged and the two results averaged
- **D** the galvanometer is replaced by one of higher resistance

### **Q18** [4] Superposition of currents is valid when the network contains

- **A** resistors and ideal batteries only
- **B** a filament lamp working hot
- **C** an ideal diode conducting steadily in one loop
- **D** a thermistor held at a regulated, constant temperature

### Section C · Numerical (Q19–Q26)

| Q | answer as | Q | answer as |
| --- | --- | --- | --- |
| Q19 | mm/s, 2 significant figures | Q23 | mA, nearest 0.1 |
| Q20 | $\Omega$, 3 significant figures | Q24 | kW, 3 significant figures |
| Q21 | mA, nearest 0.1 | Q25 | V, 2 significant figures |
| Q22 | $\Omega$, 3 significant figures | Q26 | V, nearest 1 |

### **Q19** [4] Copper, $n=8.5\times10^{28}\ \text{m}^{-3}$, cross-section 2.0 mm², current 6.8 A. Drift speed?

### **Q20** [4] Two concentric spheres of radii 1.0 cm and 10 cm, the gap filled with material of resistivity 100 $\Omega$m. Resistance between them?

### **Q21** [4] Bridge arms $AB=10\ \Omega$, $BC=20\ \Omega$, $AD=30\ \Omega$, $DC=40\ \Omega$; 10 V battery across $AC$; a 50 $\Omega$ galvanometer across $BD$. Current through the galvanometer?

### **Q22** [4] A galvanometer of resistance 100 $\Omega$, full scale 1 mA, is shunted into a 0–1 A ammeter. Its shunt resistance?

### **Q23** [4] The bridge of Q21, but with the galvanometer replaced by an ideal ammeter. Its reading?

### **Q24** [4] 500 kW is transmitted 20 km over a line of total resistance 8.0 $\Omega$ at 25 kV. Line loss?

### **Q25** [4] A cell gives a potentiometer null at 150 cm; with 4.0 $\Omega$ connected across it, the null moves to 120 cm. The cell's terminal voltage while delivering current is?

### **Q26** [4] A 100 V source feeds two series 20 k$\Omega$ resistors; a voltmeter of resistance 20 k$\Omega$ is placed across one of them. What does it read?

### Section D · Long questions (Q27–Q36)

### **Q27** [15] Two batteries are joined in parallel between nodes A and B: battery 1 is $\mathcal E_1=12$ V with $r_1=1\ \Omega$; battery 2 is $\mathcal E_2=6$ V with $r_2=0.5\ \Omega$. A resistor $R=5\ \Omega$ is also connected between A and B.

(a) [4] Find the potential difference $V_{AB}$ and the current through each battery and through $R$. (b) [4] Identify what battery 2 is doing and compute the power flowing into or out of each battery, splitting it into stored (chemical) and heated parts. (c) [4] Produce a complete power ledger for the circuit and verify it sums. (d) [3] What would $V_{AB}$ become if $R\to\infty$ (battery 2 disconnected first, then still present but open)? Comment on the difference, if any.

### **Q28** [15] A Wheatstone bridge has arms $AB=10\ \Omega$, $BC=20\ \Omega$, $AD=30\ \Omega$, $DC=40\ \Omega$ and a 10 V battery of negligible internal resistance across $AC$.

(a) [3] State the balance condition and show it fails here. (b) [4] Find the Thevenin equivalent seen from the detector diagonal $BD$: open-circuit voltage and killed-source resistance. (c) [4] Find the current through detector resistances of 50 $\Omega$ and 0 $\Omega$, and the load resistance that extracts maximum power from the bridge, with its value. (d) [4] The battery and detector are now interchanged. State the new short-circuit current at the old battery diagonal, justify with the theorem involved, and give the new open-circuit voltage there, computed honestly.

### **Q29** [15] A hemispherical electrode of radius $a=0.5$ m is embedded with its flat face flush in soil of resistivity $\rho=100\ \Omega$m; a second, identical electrode is 100 m away.

(a) [4] Show the resistance from one hemisphere to "infinity" is $\rho/2\pi a$ and evaluate it. (b) [4] Estimate the two-electrode resistance, including a comment on whether the 100 m separation's mutual term matters. (c) [4] A current of 100 A enters the earth at electrode 1. Compute the potential difference between a cow's front and rear feet, 1 m apart, on a radial line at 10 m from the electrode, and again at 100 m. (d) [3] Using the same slice method, find the resistance between two concentric spheres $a$ and $b$ and take the limit $b\to\infty$; relate it to your answer in (a).

### **Q30** [15] A battery of EMF 12 V and internal resistance 2.0 $\Omega$ drives a variable load $R$.

(a) [4] Derive the load power $P(R)$ and the condition for its maximum, including the second-derivative check. (b) [3] Compute $P_{\max}$, the terminal voltage and the efficiency at the maximum. (c) [4] Find the two load resistances at which the battery delivers half of $P_{\max}$, and their efficiencies. (d) [4] A designer argues "transmission lines should therefore be matched". Write the two-sentence rebuttal using the numbers of this question and the $P^{2}R/V^{2}$ law.

### **Q31** [15] A potentiometer has a driver of EMF 6.0 V and a 10 m uniform wire of resistance 20 $\Omega$; a resistance box in the driver loop is set so the gradient is exactly 0.005 V/cm.

(a) [3] What current flows in the wire, what is the wire's total drop, and what resistance sits in the driver loop besides the wire?

(b) [4] Cell X balances at 150 cm, cell Y at 120 cm. Give both EMFs and their ratio.

(c) [4] With a 4.0 $\Omega$ resistor across X, the balance moves to 135 cm. Find X's internal resistance and the current it then delivers.

(d) [4] Explain — with the balance condition, not slogans — why this instrument reads the EMF while a 10 k$\Omega$ voltmeter across the same cell reads lower; quantify the voltmeter's error for $r=1\ \Omega$.

### **Q32** [15] A galvanometer has $G=100\ \Omega$, full scale 1 mA.

(a) [3] Design the 0–1 A ammeter: shunt value, total meter resistance, and the power the shunt must survive. (b) [3] Design the 0–10 V voltmeter: multiplier value, meter resistance, and its $\Omega$/V rating. (c) [4] This voltmeter is placed across the lower 10 k$\Omega$ of a 100 V, 10 k$\Omega$ + 10 k$\Omega$ divider. Compute the reading and the percentage error. (d) [5] A "ring circuit" trick connects the same voltmeter *twice*: once across each resistor, and the sum is taken. Compute both readings and their sum, and state whether summing two loaded readings can beat one loaded reading here — with arithmetic, not hope.

### **Q33** [15] Twelve equal resistors $R$ form a cube.

(a) [5] For current entering corner A and leaving the body-diagonal opposite G, use symmetry to find the current in every edge and prove $R_{AG}=5R/6$. (b) [5] Repeat the argument for a face diagonal and prove $R_{AC}=3R/4$ (you may use the potential-class method). (c) [5] Two opposite edges (no shared corners) of the cube are now short-circuited by wires of negligible resistance. Recompute $R_{AG}$ and justify each step of the collapse of the network.

### **Q34** [15] $P=100$ kW must be delivered over a line of resistance 10 $\Omega$.

(a) [3] Compute the line loss at 200 V and at 20 kV, and the loss fraction in each. (b) [4] Show generally that $P_{loss}\propto1/V^{2}$, and find the voltage at which the loss equals 1% of the delivered power for this line. (c) [4] A fuse wire in the substation is drawn to radius $r$. Derive $I\propto r^{3/2}$ from the steady-state balance of $I^{2}\rho/\pi r^{2}$ heating against $h\,2\pi rL\,\Delta T$ cooling, and find the ratio of the safe currents of 0.2 mm and 0.5 mm radius wires of the same alloy. (d) [4] If the delivered power must grow to 400 kW at the same voltage and line, find the new loss fraction, and comment on why growth in demand, not efficiency, drives voltage upgrades.

### **Q35** [15] A network: a 10 V battery in series with 2 $\Omega$, in parallel with a 6 V battery in series with 1 $\Omega$, the pair feeding a load $R_L$.

(a) [4] Find the load current for $R_L=4\ \Omega$ by superposition, showing both components, and verify by a single nodal solve. (b) [4] Find the Thevenin equivalent at the load terminals and recompute the load current. (c) [3] Determine the current in each battery branch at $R_L=4\ \Omega$ and identify which battery is being charged. (d) [4] Find $R_L$ for maximum power and that power; state the efficiency there and the fraction of the 10 V battery's chemical power that ends up in the load at that operating point.

### **Q36** [18] A laboratory gives you: a 9 V battery of unknown internal resistance (order 1 $\Omega$), a resistor advertised as $R=0.10\ \Omega\pm10\%$, an ammeter of resistance 0.50 $\Omega$ and full scale 5 A, a voltmeter of resistance 10 k$\Omega$, connecting leads of 10 m$\Omega$ each, and a potentiometer wire system of gradient 0.01 V/mm.

(a) [4] Design the best measurement of $R$ with the DC meters alone. Compute the exact error of the naive series connection (ammeter inside the voltmeter's reach) and of the alternative connection, and pick the winner. (b) [4] Show why no two-terminal scheme with these instruments can reach 1% on $R$, and describe the four-terminal rewiring that can — down to which resistance drops out and why. (c) [4] The battery's EMF is measured on the potentiometer (null at 0.90 m). With the battery then driving $R=0.10\ \Omega$ through the ammeter (reading 4.0 A — compute whether this is consistent), predict the new null position and deduce the internal resistance. (d) [3] Estimate the drift speed of the electrons in a 1 mm² copper wire carrying the 4.0 A of part (c), and the time for one electron to traverse the 10 m of lead wire. Comment on what actually delivers the energy to $R$. (e) [3] The whole experiment is repeated inside a superconducting magnet room where a superconducting loop (inductance 10 $\mu$H) has trapped 2.0 A. State the loop's stored energy and flux, and what, if anything, in this paper's toolkit is needed to describe its persistence.

Continue: [10 · Solutions to all 36 questions, with marks distributed](#section-10-olympiad-solutions)

<a id="section-10-olympiad-solutions"></a>

_full solutions · marks as printed · 36 questions_

## 10 · Solutions

Every solution is written the way chapter 8 recommends: the principle first, then the algebra, then a check. The **why this is the answer** line at the end of each is the part worth reading twice. A compact answer key sits at the bottom for fast marking.

### Section A

### **Q1** Answer: B _([3] · §1.2)_

**Principle.** Electrons per second = $I/e$: the definition of current, independent of the wire. Double the area at the same current: $v_d=I/neA$ halves, $j=I/A$ halves, and $E=\rho j$ halves — only the count survives. **Why not A:** more carriers on the starting line means each moves slower, not the same.

### **Q2** Answer: B — 21% _([3] · §2.2)_

$$
R\propto\frac{l}{A}=\frac{l^{2}}{V_{\text{vol}}}\ \Rightarrow\ R' /R=(1.1)^{2}=1.21
$$

**Why not C:** 11% is the naive single-factor answer; the area shrinks too and it multiplies. **Check:** exact $l^{2}$ law for any stretch at constant volume ✓.

### **Q3** Answer: B _([3] · §2.4)_

**Principle.** In series, power divides as $I^{2}R$ — the *smaller* resistance glows dimmer. The 100 W lamp has the lower hot resistance ($484\ \Omega$ vs 807 $\Omega$), and both cold resistances scale the same way, so the 100 W lamp stays the weaker element at every temperature. **Why not A:** "rated higher" is a parallel-circuit intuition; series favours the bigger resistor.

### **Q4** Answer: C — 10 V _([3] · §3.2)_

$$
V=\mathcal E-Ir=12-200\times0.01=10\ \text{V}
$$

**Check:** the sag equals $Ir=2$ V on a 12 V battery — exactly the cranking whine you hear in a cold car. **Why not D:** 13 V would mean charging, not discharging.

### **Q5** Answer: B _([3] · §3.2)_

**Principle.** On charge the external supply must defeat both the EMF and the internal drop: $V=\mathcal E+Ir$. Terminal voltage above EMF is the signature of charging — the sign of $Ir$ is the whole question. **Why not C:** EMF is constant, but the *terminal voltage* is not the EMF.

### **Q6** Answer: B _([3] · §5.5)_

**Principle.** Reciprocity: source and detector may trade diagonals; the balance condition $R_1R_4=R_2R_3$ is symmetric under the swap. **Check:** ch 4, Q5 verified it arm by arm; the invariant underlying it is the port-swap invariance of $V/I$.

### **Q7** Answer: B — quarters _([3] · §3.4)_

$I^{2}r$ with $I\to I/2$ is $I^{2}r/4$. **Why not C:** $r$ fixed does not fix $I^{2}$; the whole point of raising $R$ is that the internal share of the current falls as $\mathcal E/(R+r)$.

### **Q8** Answer: C — $2\sqrt2$ times _([3] · §7.1)_

$$
I^{2}\frac{\rho}{\pi r^{2}}L=h\,2\pi rL\,\Delta T\ \Rightarrow\ I\propto r^{3/2}
$$

Doubling $r$: $2^{3/2}=2.83$. **Why not B:** 4× would be right if heating alone scaled — it is the cooling surface $r$ in the denominator that bends the exponent to 3/2.

### **Q9** Answer: B _([3] · §6.1)_

A voltmeter must steal as little current as possible while the coil needs $I_g$: a large series multiplier, $R_m=V/I_g-G$. Shunts are the ammeter's trick, where most of the current must *bypass* the coil.

### **Q10** Answer: A — 7R/12 _([3] · §4.3)_

Adjacent corners: symmetry gives currents $I/2, I/4, I/4$ through the three classes of edges, total drop $\big(\tfrac12+\tfrac14+\tfrac14\big)IR$ split as $\tfrac12IR+\tfrac14IR$ along any path ⇒ $7R/12$. **Check:** $7/12<3/4<5/6$ as endpoints separate ✓ (ch 4, Q3 did the face case in full).

### **Q11** Answer: B — 1.618R _([3] · §4.5)_

$$
R_\infty=\frac{R+\sqrt{R^{2}+4R^{2}}}{2}=\frac{1+\sqrt5}{2}R=\varphi R
$$

**Check:** $R+R\varphi/(1+\varphi)=R(1+1/\varphi)=R\varphi$ since $\varphi^{2}=\varphi+1$ ✓. The golden ratio is a resistor network before it is anything else.

### **Q12** Answer: C — 25 W _([3] · §2.4)_

Half the voltage on a fixed resistance: $P=V^{2}/R$ falls by 4, to 25 W. **Why not A:** 50 W is the linear fallacy — power is quadratic in voltage. (A real lamp also runs cooler and dims further; "constant hot resistance" is the stated assumption.)

### Section B

### **Q13** Answer: A, D _([4] · §2.3)_

Copper and platinum: $\tau$ shortens, $n$ fixed, $R$ rises. NTC thermistor: carrier flood, $R$ falls. Carbon composition: also negative coefficient. **Why D matters:** platinum's predictability is precisely why it is the thermometer standard.

### **Q14** Answer: B, D _([4] · §1.4, §2.3)_

$\sigma=ne^{2}\tau/m$: in a metal $n$ is frozen, so everything is the story of $\tau$. **Why not A:** the carrier density in a metal does not grow with $T$ — that is the semiconductor mechanism; a question that offers both mechanisms is testing whether you know which material owns which.

### **Q15** Answer: A, C _([4] · §1.2)_

Junction law = charge conservation in steady state = continuity equation at a node with $\partial\rho/\partial t=0$. **Why not B:** energy conservation is the *loop* law. **Why not D:** Ohm's law is constitutive, not conserved-anything.

### **Q16** Answer: A, B, D _([4] · §3.4)_

$\mathcal EI$ in, $I^{2}R$ out, $I^{2}r$ heat, efficiency $R/(R+r)$. **Why not C:** at $R=r$ — the maximum-power point — efficiency is exactly $50\%$, the price of matching.

### **Q17** Answer: A, C _([4] · §6.3)_

Near 50 cm the length error in $l$ and $100-l$ is fractional-smallest; the swap-and-average cancels end errors to first order. **Why not B:** at 5 cm a 1 mm jockey wobble is 2% of $l$. **Why not D:** at balance the detector carries no current — its resistance is already irrelevant.

### **Q18** Answer: A, D _([4] · §5.1)_

Superposition needs linearity: resistors with fixed values and ideal sources qualify; a thermistor clamped at constant temperature is just a resistor. The hot filament ($R$ depends on total current) and the diode ($R$ depends on current sign) both revoke the licence. **Why not C:** "conducting steadily" fixes its drop at 0.7 V — still a nonlinearity; superposition must apply to *every* element.

### Section C

### **Q19** Answer: 0.25 mm/s _([4] · §1.3)_

$$
v_d=\frac{I}{neA}=\frac{6.8}{8.5\times10^{28}\times2.0\times10^{-6}\times1.6\times10^{-19}} =2.5\times10^{-4}\ \text{m/s}
$$

**Check:** double the ch-1 wire's area at ~7× the current: $7.35\times10^{-5}\times3.4=2.5\times10^{-4}$ ✓. The trap was the prefix: 0.25 mm/s, not 0.25 m/s.

### **Q20** Answer: 716 $\Omega$ _([4] · §2.2)_

$$
R=\frac{\rho(b-a)}{4\pi ab}=\frac{100\times0.09}{4\pi\times10^{-3}}=716\ \Omega
$$

**Check:** the thin-sphere limit $\rho(b-a)/(4\pi a^{2})$ with $b=10a$ would give 7160 $\Omega$; the growing area must cut it tenfold ✓.

### **Q21** Answer: 12.9 mA (B → D) _([4] · §4.4)_

Nodal: $V_B=6.581$ V, $V_D=5.935$ V ⇒ $I=(0.645)/50=12.9$ mA. **Direction check first:** open-circuit $V_B=6.67>V_D=5.71$, and $R_1/R_2<R_3/R_4$ — B is the high node; the algebra only confirms it.

### **Q22** Answer: 0.100 $\Omega$ _([4] · §6.1)_

$$
S=\frac{G}{n-1}=\frac{100}{1000-1}=0.1001\ \Omega
$$

**Check:** total meter resistance $=GS/(G+S)=0.1\ \Omega$ ✓ — 99.9% of the current bypasses the coil.

### **Q23** Answer: 40.0 mA _([4] · §5.2)_

Ideal ammeter = short circuit: $I_{sc}=V_{th}/R_{th}=0.952/23.81=40.0$ mA. **Check:** 40 mA > 12.9 mA — no load current may exceed its own short-circuit value ✓. (Full derivation in Q28.)

### **Q24** Answer: 3.20 kW _([4] · §7.2)_

$$
I=\frac{5\times10^{5}}{2.5\times10^{4}}=20\ \text{A};\qquad P_{loss}=20^{2}\times8=3.2\times10^{3}\ \text{W}=0.64\%\ \text{of delivery}
$$

**Check:** at 250 V the same line would demand 2000 A and burn 32 MW — the 10⁴ ratio $=100^{2}$ ✓.

### **Q25** Answer: 1.2 V _([4] · §6.4)_

Gradient $=1.5/150=0.01$ V/cm; the loaded null is a *terminal-voltage* balance: $V=0.01\times120=1.2$ V. **Check:** $r=4\times30/120=1\ \Omega$, $I=1.5/5=0.3$ A, $V=1.5-0.3=1.2$ ✓.

### **Q26** Answer: 33 V _([4] · §6.2)_

Meter ∥ 20 k = 10 k; reading $=100\times10/30=33.3\approx33$ V against a true 50 V — a 34% lie. **Why:** the meter's resistance equals the arm it loads; that is not an instrument fault, it is circuit modification.

### Section D

### **Q27** Two batteries in parallel driving R — answers _([15] · §3.2, §3.4)_

**(a) [4] Principle: one node equation.** With $V=V_{AB}$: $\frac{12-V}{1}+\frac{6-V}{0.5}=\frac{V}{5}$. Multiply by 5: $60-5V+60-10V=V\Rightarrow V=120/16=7.5$ V. Then $I_1=(12-7.5)/1=4.5$ A (out of battery 1), $I_2=(6-7.5)/0.5=-3.0$ A — **negative: into battery 2** — and $I_R=7.5/5=1.5$ A. Check: $4.5-3.0=1.5$ ✓.

**(b) [4] What battery 2 is doing.** Its current is opposite to its EMF: it is **being charged** by the 12 V battery while both feed the load. Power: battery 1 chemical out $12\times4.5=54$ W, of which $4.5^{2}\times1=20.25$ W heats $r_1$; battery 2 absorbs $7.5\times3=22.5$ W, splitting into stored $6\times3=18$ W and heated $3^{2}\times0.5=4.5$ W; load takes $7.5\times1.5=11.25$ W.

**(c) [4] The ledger.** Chemical out 54 W. Consumed: $20.25+22.5+11.25=54.00$ W ✓ — and within battery 2's absorption, 18 W stored + 4.5 W heat is itself a balanced sub-ledger. A circuit with a charging cell has *negative dissipation* in that branch; the audit is what makes that visible.

**(d) [3] R removed.** Only the loop $\mathcal E_1\to r_1\to r_2\to\mathcal E_2$ remains: circulating current $I=(12-6)/(1+0.5)=4.0$ A, and $V_{AB}=12-4=8.0$ V (= $6+4\times0.5$ ✓). Battery 1 delivers $48$ W: 16 W heats $r_1$, 8 W heats $r_2$, 24 W is pumped into battery 2 as stored charge. **Why this matters:** "open-circuit voltage of a battery pair" is well defined but thermally honest — nothing is open about the circulation. Two unequal batteries must never be paralleled bare.

### **Q28** The bridge by Thevenin, then by reciprocity — answers _([15] · §4.4, §5.2, §5.5)_

**(a) [3]** Balance needs $R_{AB}/R_{BC}=R_{AD}/R_{DC}$: $10/20=1/2$ against $30/40=3/4$. Not equal — B sits higher than D; the bridge is off by a wide margin.

**(b) [4]** Detector removed: $V_B=10\times20/30=6.667$ V, $V_D=10\times40/70=5.714$ V ⇒ $V_{th}=0.952$ V. Battery killed (wire): $R_{th}=10\parallel20+30\parallel40=6.667+17.143=23.81\ \Omega$.

**(c) [4]** $I(50)=0.952/(23.81+50)=12.9$ mA; $I(0)=0.952/23.81=40.0$ mA. Maximum power at $R_L=R_{th}=23.8\ \Omega$: $P_{max}=0.952^{2}/(4\times23.81)=9.5$ mW. **Check:** at $2R_{th}$ the power is $8/9$ of maximum, as the quadratic demands ✓.

**(d) [4]** Swap battery and detector. By **reciprocity** the short-circuit current is invariant: 40.0 mA again. The *open-circuit* voltage is not invariant: honest computation with 10 V across B–D gives $V_A=10-10\times10/(10+30)=7.5$ V, $V_C=10\times40/(20+40)=6.667$ V, so $V_{AC}=0.833$ V — different from 0.952 V. **Why:** reciprocity equates the ratio $I_{sc}/V_{drive}$, never the open voltages separately.

### **Q29** Earthing and the slice method — answers _([15] · §2.2)_

**(a) [4]** Hemispherical equipotentials of area $2\pi r^{2}$: $R=\int_a^{\infty}\rho\,dr/2\pi r^{2}=\rho/2\pi a=100/\pi=31.8\ \Omega$. The integral converges because the area grows as $r^{2}$.

**(b) [4]** Two far electrodes in series: $2\times31.8=63.7\ \Omega$. Mutual correction $\rho/2\pi D=100/628=0.16\ \Omega$ — 0.25%, negligible; the check *is* the negligibility.

**(c) [4]** $E(r)=\rho I/2\pi r^{2}$: at 10 m, $=100\times100/(2\pi\times100)=15.9$ V/m ⇒ step voltage $\approx15.9$ V across a 1 m stride — a real hazard (animals are killed by step potentials near faulted earths). At 100 m: $0.159$ V/m ⇒ 0.16 V, safe. The $1/r^{2}$ collapse is why earth pits are fenced.

**(d) [3]** Concentric spheres: $R=\rho(b-a)/4\pi ab\to\rho/4\pi a$ as $b\to\infty$ — exactly half the hemisphere's $\rho/2\pi a$, because the hemisphere radiates through half the area at every radius. **Check:** same integral, half the solid angle ✓.

### **Q30** Maximum power, dissected — answers _([15] · §3.4, §7.2)_

**(a) [4]** $P(R)=\mathcal E^{2}R/(R+r)^{2}=144R/(R+2)^{2}$. $dP/dR=144(2-R)/(R+2)^{3}=0\Rightarrow R=2\ \Omega$. Second-derivative check: $d^{2}P/dR^{2}=144(2R-8)/(R+2)^{4}=-2.25<0$ at $R=2$ ✓ maximum.

**(b) [3]** $P_{max}=144\times2/16=18$ W; terminal voltage $=12-3\times2=6$ V; efficiency $6/12=50\%$ — always, at the match.

**(c) [4]** Half power = 9 W: $144R/(R+2)^{2}=9\Rightarrow R^{2}-12R+4=0\Rightarrow R=2(3\pm2\sqrt2)$ = $0.343$ or $11.66$ $\Omega$. Efficiencies $R/(R+2)=14.7\%$ and $85.3\%$. **Check:** product of the two roots $=4=r^{2}$ ✓ (the log-symmetry of the power hill).

**(d) [4]** Matching buys maximum watts at a ruinous price: here it would burn 18 W inside the battery for every 18 W delivered — $\eta=50\%$. A transmission line delivering 100 kW with 0.25% loss runs at $\eta=99.75\%$ precisely because it is *not* matched; and since $P_{loss}=P^{2}R/V^{2}$, the design variable is $V$, not the load ratio. Matching is for signals; efficiency is for power.

### **Q31** The potentiometer, end to end — answers _([15] · §6.4)_

**(a) [3]** Gradient $=0.005$ V/cm $\times100=0.5$ V/m over 10 m ⇒ wire drop $=5.0$ V; wire current $=5/20=0.25$ A; driver loop resistance $=6/0.25=24\ \Omega$, i.e. $4\ \Omega$ besides the wire. **Check:** $5+0.25\times4=6$ ✓.

**(b) [4]** $\mathcal E_X=0.005\times150=0.75$ V; $\mathcal E_Y=0.60$ V; ratio $=1.25$. No current flows at either null, so internal resistance never enters — that is the point of the instrument.

**(c) [4]** Loaded null 135 cm ⇒ terminal voltage $0.675$ V. $r=R(l_0-l)/l=4\times15/135=0.444\ \Omega$. Current delivered: $I=0.675/4=0.169$ A. **Check:** $(0.75-0.675)/0.444=0.169$ ✓ both routes agree.

**(d) [4]** At null the cell delivers *zero* current, so no $Ir$ drop exists and the wire segment equals the EMF exactly. The 10 k$\Omega$ voltmeter draws $0.75/10001=75\ \mu$A, giving terminal voltage $0.75-75\times10^{-6}\times1=0.749925$ V — an error of 0.01% for $r=1\ \Omega$. Honest reading of the numbers: with a small $r$ the modern meter is nearly honest; the potentiometer's superiority is *categorical* (zero loading regardless of $r$, and calibration by length ratio) — and it becomes decisive the moment $r$ is comparable to $R_V$.

### **Q32** One galvanometer, four instruments — answers _([15] · §6.1, §6.2)_

**(a) [3]** $S=G/(n-1)=100/999=0.1001\ \Omega$; total resistance 0.1 $\Omega$; shunt power at full scale $(0.999)^{2}\times0.1001=0.10$ W — the shunt is the thermal element, not the coil.

**(b) [3]** $R_m=10/0.001-100=9900\ \Omega$; meter resistance 10 k$\Omega$; sensitivity $=1/I_g=1000\ \Omega/\text{V}$.

**(c) [4]** Lower arm becomes $10k\parallel10k=5k$: reading $=100\times5/15=33.3$ V — an error of **−33%** on a true 50 V. The meter is honest; the *circuit it joined* is different.

**(d) [5]** Put an identical meter across each resistor: upper arm $10k\parallel10k=5k$, lower the same — the divider is symmetric again and each meter reads 50.0 V, summing to 100.0 V. **The verdict, with a counterexample:** the sum is exact by KVL for *any* arms (the meters merely close the same series chain), but the individual readings are not corrected in general: on 10 k + 20 k the same two meters read 71.4 V and 28.6 V (true: 33.3 and 66.7). The recovery here is a symmetry miracle of equal arms — not a method. One good high-impedance meter beats two clever ones.

### **Q33** The cube, extended — answers _([15] · §4.3)_

**(a) [5]** From A the three edges are equivalent: $I/3$ each; into G likewise. The reflection planes through the body diagonal force the six middle edges to carry $I/6$. Any path drops $\tfrac{I}{3}R+\tfrac{I}{6}R+\tfrac{I}{3}R=\tfrac{5IR}{6}$, so $R_{AG}=5R/6$. **Check:** currents sum to $I$ at every node class ✓.

**(b) [5]** Face diagonal A–C: the reflection in that diagonal makes $V_B=V_D\equiv V_1$ and $V_{B'}=V_{D'}\equiv V_2$; earth C, put 1 V on A. The four node equations $3V_1-V_2=1$, $3V_Z-2V_2=1$, $3V_2=V_1+V_Z+V_Y$, $3V_Y=2V_2$ give $V_1=V_2=\tfrac12, V_Z=\tfrac23, V_Y=\tfrac13$; input current $=(1-V_1)+(1-V_1)+(1-V_Z)=\tfrac43$ ⇒ $R_{AC}=3R/4$. **Check:** the current into C, $V_1+V_1+V_Y=\tfrac43$ ✓.

**(c) [5]** Short edge A–B and the antipodal edge G–H. Merge A,B into node P and G,H into node Q: each of C, D, Z, F now hangs from *both* P and Q through unit edges, with two bridges C–D and Z–F between them. The swap C↔D maps the network on itself with P, Q fixed, so $V_C=V_D$ — the C–D bridge carries no current and may be deleted; likewise Z–F. Four independent 2R paths in parallel: $R_{AG}=2R/4=R/2$. **Check:** shorting edges can only lower resistance; $5R/6\to R/2$ ✓, and the two deleted bridges carried nothing by the balance-type argument of ch 4 ✓.

### **Q34** Transmission and fuses — answers _([15] · §7.1, §7.2)_

**(a) [3]** 200 V: $I=500$ A, loss $=2.5$ MW — **25× the delivered power**, impossible to run. 20 kV: $I=5$ A, loss 250 W = 0.25%.

**(b) [4]** $P_{loss}=P^{2}R/V^{2}$: quadratic in the step-down ratio. Loss = 1% of 100 kW = 1 kW: $V^{2}=P^{2}R/1000=10^{11}/10^{3}=10^{8}\Rightarrow V=10$ kV. **Check:** 20 kV gave 0.25%; halving the voltage quadruples the fraction ✓.

**(c) [4]** Balance $I^{2}\rho L/\pi r^{2}=h\,2\pi rL\,\Delta T$ ⇒ $I=r^{3/2}\sqrt{2\pi^{2}h\Delta T/\rho}$; $L$ cancels, radius enters as 3/2. Ratio for 0.5/0.2 mm: $(2.5)^{3/2}=3.95$.

**(d) [4]** 400 kW at 20 kV: $I=20$ A, loss 4 kW = **1%** (was 0.25%). At fixed $V$ and line, the loss *fraction* grows linearly with demand: $P_{loss}/P=PR/V^{2}\propto P$. Growth, not gadgetry, is what forces utilities to step up voltage.

### **Q35** Two sources, four theorems — answers _([15] · §5.1–§5.4)_

**(a) [4]** 6 V killed (wire, 1 $\Omega$ kept): $I_a=\dfrac{10}{2+4/5}\times\tfrac15=0.714$ A. 10 V killed: $I_b=\dfrac{6}{1+8/6}\times\tfrac26=0.857$ A. Sum $1.571$ A. Nodal check: $(10-V)/2+(6-V)/1=V/4\Rightarrow V=44/7=6.286$ V, $I=1.571$ A ✓.

**(b) [4]** Open circuit: $(10-V)/2+(6-V)/1=0\Rightarrow V_{th}=22/3=7.333$ V; killed sources: $R_{th}=2\parallel1=0.667\ \Omega$; $I=7.333/(4.667)=1.571$ A ✓ — third route, same number.

**(c) [3]** $I_{10V}=(10-6.286)/2=1.857$ A out; $I_{6V}=(6-6.286)/1=-0.286$ A — the 6 V battery **is being charged** by the 10 V one even while both serve the load.

**(d) [4]** $R_L=2/3\ \Omega$: $P_{max}=V_{th}^{2}/4R_{th}=53.78/2.667=20.2$ W, efficiency 50%. Branch currents at this load: $V_L=3.667$ V, $I_L=5.5$ A, $I_{10V}=(10-3.667)/2=3.167$ A ⇒ chemical power 31.67 W, of which $20.2/31.67=63.7\%$ reaches the load. **Check:** full ledger $31.67+14.0=20.06+5.44+20.17=45.67$ W ✓ (the 6 V battery now discharges: $(6-3.667)/1=2.33$ A out).

### **Q36** The measurement design — answers _([18] · §6.1–§6.4, §1.3, §7.5)_

**(a) [4]** Naive (voltmeter across $R$ + ammeter, i.e. ammeter inside): the meter reads $I(R+R_A)$; at 4.0 A that is 2.4 V on 0.1 $\Omega$ — inferred $R=0.60\ \Omega$, a **+500%** error. Ammeter outside (voltmeter on $R$ alone): voltmeter steals $0.4/10^{4}=40\ \mu$A against 4 A — 0.001%; inferred $R=0.4/4=0.100\ \Omega$. Winner: ammeter outside, always, for small resistances.

**(b) [4]** One percent of 0.1 $\Omega$ is 1 m$\Omega$; the leads alone are 2×10 m$\Omega$ and the ammeter 500 m$\Omega$. No rearrangement of *two* terminals can separate specimen from leads because the same pair of wires must both carry current and define the voltage — the topology itself is the error. Four terminals: current leads at the outer pair (their drops now merely load the battery), voltage leads on the specimen body feeding the 10 k$\Omega$ meter (40 µA ⇒ $0.4\ \mu$V in the sense leads — 0.0004%). The resistance that drops out is everything outside the voltage taps; what remains is the metal you meant.

**(c) [4]** EMF $=0.01\ \text{V/mm}\times900\ \text{mm}=9.0$ V. Consistency: the loop is $9/(0.1+0.5+r)$; the meter reads 4.0 A ⇒ $r=2.25-0.6=1.65\ \Omega$ (order-1, as advertised ✓). Loaded terminal voltage $=9-4\times1.65=2.4$ V ⇒ new null at $240$ mm. **Check:** $r=R(l_0-l)/l$ with $R=0.6$: $0.6\times660/240=1.65\ \Omega$ ✓.

**(d) [3]** $v_d=I/neA=4/(8.5\times10^{28}\times10^{-6}\times1.6\times10^{-19})=2.9\times10^{-4}$ m/s; one lead traversal takes $10/2.9\times10^{-4}=3.4\times10^{4}$ s ≈ 9.5 h. What delivered the energy was the field, established throughout the circuit within $L/c\sim10^{-8}$ s of contact — the electrons at $R$ never waited for colleagues from the battery.

**(e) [3]** Stored energy $\tfrac12LI^{2}=\tfrac12\times10^{-5}\times4=20\ \mu$J; trapped flux $\Phi=LI=20\ \mu$Wb. Persistence needs nothing from this paper's toolkit but the two conservation laws: KCL (the current has nowhere to go) and $\rho=0$ (nothing damps it); the decay time $L/R$ is unbounded for $R=0$. Flux freezing says the *current* is whatever $\Phi/L$ demands — the ledger, not a battery, keeps the books.

### Answer key

Marks: $12\times3+6\times4+8\times4+153=245$ in total. Section D is marked as printed — nine questions at [15] and Q36 at [18] — and part-answers earn partial credit, so never leave one blank.

| A | B | C |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 B | 2 B | 3 B | 4 C | 5 B | 6 B | 7 B | 8 C | 9 B | 10 A | 11 B | 12 C |  |  |
| 13 AD | 14 BD | 15 AC | 16 ABD | 17 AC | 18 AD | 19 0.25 mm/s | 20 716 Ω | 21 12.9 mA | 22 0.100 Ω | 23 40.0 mA | 24 3.20 kW | 25 1.2 V | 26 33 V |

| D | headline result | D | headline result |
| --- | --- | --- | --- |
| 27 | $V_{AB}=7.5$ V; 1.5 A in the load, battery 2 *charging* at 3 A | 32 | shunt 0.1001 $\Omega$; multiplier 9.90 k$\Omega$; loading error quantified |
| 28 | off balance: $R_{\text{th}}=23.8\ \Omega$, $I_g=12.9$ mA; reciprocity swaps drive and response only | 33 | body diagonal $5R/6$, face $3R/4$, edge $7R/12$; bridged case $R/2$ |
| 29 | hemisphere $\rho/2\pi a=31.8\ \Omega$; two far electrodes $63.7\ \Omega$; spheres $\rho/4\pi a$ | 34 | 200 V: 2.5 MW (25×); 20 kV: 0.25%; fuse current $\propto r^{3/2}$ |
| 30 | $R=r=2\ \Omega$, $P_{\max}=18$ W, $\eta=50\%$ — matching is not efficiency | 35 | $I=1.571$ A by superposition, Thévenin and Norton; $\eta=63.7\%$ |
| 31 | gradient 0.5 V m⁻¹; wire drop 5.0 V; 4 $\Omega$ of driver resistance besides the wire | 36 | naive ammeter-inside scheme reads 0.60 $\Omega$ for 0.10 $\Omega$ (+500%); four-terminal wins |

> **After marking: the four things to fix first**
>
> 1. A wrong direction or missing charging battery (Q5, Q16, Q27) ⇒ re-read §3.2 and redo Q27(a) without notes.
> 2. A Thevenin resistance slip (Q21, Q23, Q28, Q35) ⇒ recompute $R_{th}$ by two different routes; they must
>   agree before you trust any downstream number.
> 3. A missing limit or check in any long answer (Q29–Q36) ⇒ rewrite with the check sentence first; it is the
>   cheapest mark in the paper.
> 4. Any part of Q33 or Q36 blank ⇒ chapters 4 and 6 need one more pass; those two parts are the difference
>   between a rank and a compliment.

Last: [11 · The formula sheet](#section-11-formula-sheet) · back to [the paper](#section-09-olympiad-paper)

<a id="section-11-formula-sheet"></a>

_3 pages A4 · JEE · INPhO_

## Current Electricity — the whole course on three pages

### 1 · Carriers, materials, sources

$$
I=\frac{dq}{dt},\quad \vec j=nq\vec v_d,\quad \vec\nabla\cdot\vec j=-\frac{\partial\rho}{\partial t},\quad \vec j=\sigma\vec E,\quad \sigma=\frac{ne^{2}\tau}{m} \tag{S1}
$$

- **Current is a flux** (scalar) through a named surface; $\vec j$ is the vector. Node law = continuity
  in steady state; loop law = energy per coulomb.
- **Drift**: $v_d=I/neA\sim0.1$ mm/s in house wiring; $\tau\sim10^{-14}$ s; thermal speed
  $\sim10^{6}$ m/s. Signals travel at $\sim c$ (the field), electrons at centimetres per hour.
- **Electrons per second** through any cross-section: $I/e$ — independent of wire thickness.

$$
R=\frac{\rho l}{A}\ (\text{uniform}),\qquad R=\int\frac{\rho\,dl}{A},\qquad R_{\text{shell}}=\frac{\rho(b-a)}{4\pi ab},\qquad R_{\text{hemi}\to\infty}=\frac{\rho}{2\pi a} \tag{S2}
$$

- **Stretch at constant volume**: $R\propto l^{2}$. **Taper**: frustum = $\rho l/\pi ab$
  (geometric mean area) — reciprocals add, never averages.
- **Temperature**: $R_T=R_0[1+\alpha(T-T_0)]$ (a local law). Metal: $\tau$ shortens,
  $\rho\uparrow\propto T$ ($\alpha_{Cu}=3.9\times10^{-3}$ K⁻¹). Intrinsic semiconductor:
  $n\propto e^{-E_g/2kT}$ doubles per ~10 K, so $\rho$ falls. Manganin: $\alpha\approx2\times10^{-5}$.
- **Non-ohmic three**: filament (hot $R\approx12\times$ cold, I–V bends down), NTC thermistor (bends
  up, self-heating), diode (0.7 V threshold — solve piecewise: guess state, solve, **check guess**).

$$
I=\frac{\mathcal E}{R+r},\quad V=\mathcal E\mp Ir,\quad \mathcal EI=I^{2}R+I^{2}r,\quad \eta=\frac{R}{R+r} \tag{S3}
$$

- **EMF** = work per coulomb by non-electrostatic forces; the only place $\oint\vec E\cdot d\vec l\ne0$.
- Discharge: $V<\mathcal E$. Charge: $V>\mathcal E$. Open: $V=\mathcal E$.
  The $V$–$I$ line has intercepts $\mathcal E$ and $\mathcal E/r$, slope $-r$.
- **Grouping** (n series × m rows, identical cells): $\mathcal E_{eq}=n\mathcal E$,
  $r_{eq}=nr/m$; current $=mn\mathcal E/(mR+nr)$, maximal at $R=nr/m$.
- **Unequal cells in parallel**: $\mathcal E_{eq}=\dfrac{\mathcal E_1r_2+\mathcal E_2r_1}{r_1+r_2}$;
  the weaker cell is being charged — solve the node to see who drives whom.
- **Max power**: $R=r\Rightarrow P_{max}=\mathcal E^{2}/4r,\ \eta=50\%$. Half-power loads:
  $R=r(3\pm2\sqrt2)$. Matching is for signals; efficiency is for power.

| charge conservation | node law, always |
| --- | --- |
| energy conservation | loop law + the audit $\sum\mathcal EI=\sum I^{2}R$ |
| the audit habit | close every solve with the ledger |

### 2 · Networks, theorems, instruments

$$
R_{ser}=\sum R_i,\qquad R_{par}=\Big(\sum R_i^{-1}\Big)^{-1},\qquad \text{balance: }\frac{R_1}{R_2}=\frac{R_3}{R_4}\ (R_1R_4=R_2R_3) \tag{S4}
$$

- **Dividers**: $V_1=VR_1/(R_1+R_2)$; $I_1=IR_2/(R_1+R_2)$ (the *other* resistor!). Valid
  only unloaded.
- **Cube of R**: edge $7R/12$, face $3R/4$, body $5R/6$ — symmetry planes first, algebra second.
- **Infinite ladder**: $R_\infty=\big(R_s+\sqrt{R_s^{2}+4R_sR_p}\big)/2$; $R_s=R_p=R$ gives
  $\varphi R=1.618R$.
- **Delta→star**: $R_1=R_{12}R_{31}/(R_{12}+R_{23}+R_{31})$; symmetric delta $R$ → star $R/3$.

$$
V_{th}=V_{oc},\qquad R_{th}=\frac{V_{oc}}{I_{sc}},\qquad I_N=\frac{V_{th}}{R_{th}},\qquad P_{max}=\frac{V_{th}^{2}}{4R_{th}}\ \text{at}\ R_L=R_{th} \tag{S5}
$$

- **Kill sources**: ideal voltage → wire ($r$ stays), ideal current → break. Superposition sums currents,
  never powers; dies on any nonlinearity.
- **Reciprocity**: swap source and detector ports, same $I_{sc}/V$ ratio; open voltages are
  *not* preserved.
- **Compensation**: changing $R$ by $\Delta R$ ≡ inserting source $-I\Delta R$, others killed.

$$
S=\frac{G}{n-1},\qquad R_m=\frac{V}{I_g}-G,\qquad \text{sensitivity}=\frac{1}{I_g}\ \Omega/\text{V} \tag{S6}
$$

- **Loading**: meter across $R_2$ reads $V(R_2\parallel R_V)/(R_1+R_2\parallel R_V)$. A 10 kΩ meter
  on a 10k+10k divider from 100 V reads 33.3 V, not 50 V.
- **Meter bridge**: $R/S=l/(100-l)$; end errors killed by interchanging $R,S$ and averaging.
- **Potentiometer**: $\mathcal E_1/\mathcal E_2=l_1/l_2$; $r=R(l_0-l)/l$. At balance the cell
  delivers zero current — reads EMF, not terminal voltage.
- **Low resistance ⇒ four terminals**: current leads outside, voltage leads inside; all lead drops vanish by
  topology.

$$
I_{fuse}\propto r^{3/2},\qquad P_{loss}=\frac{P^{2}R_{line}}{V^{2}},\qquad T_n=\frac{a}{2b},\quad T_i=\frac{a}{b}=2T_n,\qquad \tau=\frac{L}{R}\to\infty \tag{S7}
$$

- **Fuse**: length cancels; $2\times r\Rightarrow2.83\times I$. Cable $\Delta T\propto j^{2}r$.
- **Transmission**: 100 kW over 10 Ω: 200 V loses 2.5 MW; 20 kV loses 250 W. Loss fraction $\propto P$
  at fixed $V$.
- **Thermocouple**$\mathcal E=aT-bT^{2}$: peak at neutral $a/2b$; zero (current reverses) at
  inversion $a/b$.
- **Thermistor stability**: needs $dP/dT<\delta$; a series resistor caps the current (boundary at
  $R=R_s$ — max-power transfer in thermal clothes).
- **Superconductor ring**: $I=\Phi/L$ (flux freezing); $E=\tfrac12LI^{2}$; nothing decays.

### 3 · The traps, and the numbers to own

- Electrons do **not** move at light speed; the field does.
- "12 V battery" delivers $\mathcal E-Ir$ under load, $\mathcal E+Ir$ on charge.
- A voltmeter is a load; an ammeter is a resistance in the loop. Check both against the circuit impedance.
- A killed voltage source is a **wire** (keep $r$); a killed current source is a **break**.
- Reciprocity preserves the $V/I$ ratio, not the open-circuit voltage.
- Neutral $=a/2b$ (max EMF); inversion $=a/b$ (zero EMF, current reverses). Never swap them.
- Perfect conductor ≠ superconductor: Meissner expels flux; a mere perfect conductor would trap it.
- Audit the ledger after every solve: $\sum\mathcal EI=\sum I^{2}R$ — including negative (charging)
  branches.
- Stretched wire: $R\to k^{2}R$. Series favours the bigger R; parallel the smaller.
- Superposition of currents only, never powers; and never with a diode or a hot filament in the loop.

| number | value |
| --- | --- |
| electron charge | $1.6\times10^{-19}$ C; 1 A = $6.25\times10^{18}$ e/s |
| Cu | $\rho=1.7\times10^{-8}\ \Omega$m, $n=8.5\times10^{28}$, $\alpha=3.9\times10^{-3}$ |
| Al | $\rho=2.7\times10^{-8}$, $n=1.8\times10^{29}$ (more carriers than Cu) |
| relaxation time / free path | $\sim10^{-14}$ s, 10–40 nm |
| drift speed (household) | $\sim0.1$ mm/s; AC excursion $\sim\mu$m at 50 Hz |
| cube / ladder | $7R/12,\ 3R/4,\ 5R/6$; $\varphi R$ |
| matched load | $P=V_{th}^{2}/4R_{th}$, $\eta=50\%$ |
| air breakdown | 3 kV/mm |
| Cu–Fe couple | $T_n\approx128\ ^\circ$C, $T_i\approx256\ ^\circ$C |
| Pt sensor | $\alpha=3.85\times10^{-3}$ K⁻¹ (Pt-100: 138.5 Ω at 120 °C) |

Back to: [**the course map**](#section-index) · the [**paper**](#section-09-olympiad-paper)
