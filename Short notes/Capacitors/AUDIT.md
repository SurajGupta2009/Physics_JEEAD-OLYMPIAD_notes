# Capacitors: what was kept, what was cut (2026-10-24)

**Decision.** This chapter is now **JEE Main + Advanced only**. The six Olympiad
extension sheets were audited item by item against one question:

> *Is this a **method** that solves JEE-level questions, or is it extra physics that
> JEE Main/Advanced does not examine?*

Methods were kept - and more importantly, **moved into the JEE flow at the point
where they are used**. Extra physics was dropped and, where it belongs to another
chapter's syllabus, logged as a hand-off (see §4) instead of being deleted silently.

Editions:

| | before | after |
|---|---|---|
| pages | 17 (11 JEE + 6 Olympiad) | **7, JEE only** |
| cards/moves | 68 | - |
| prose | ~4,500 words | ~2,300 words |
| separate JEE/Olympiad PDFs and ZIPs | 3 + 3 | **1 + 1** |
| old edition | - | `legacy/` (frozen, not rendered) |

Every sheet is a **single column**: numbered teaching sections, a result box, a
worked number, a trap, a figure, and a one-line remember strip. Pages 1-7 run in
the order a teacher actually builds the chapter:

1. conductors → 2. definition and geometry → 3. networks → 4. energy, battery and
heat → 5. force and image charge → 6. dielectrics → 7. transients and AC.

---

## 1. The six Olympiad sheets, item by item

Legend: **KEPT** = merged into the JEE pages · **HAND-OFF** = valid JEE topic, but
it belongs to another chapter (logged in §4) · **DROP** = not in the JEE syllabus
and not needed as a method.

### Olympiad-01 "Microscopic & dispersive dielectrics"

| card | verdict | why |
|---|---|---|
| From dipoles to permittivity (Clausius-Mossotti, $\alpha_e$, $\alpha_{orient}$) | **DROP** | solid-state / statistical mechanics. No JEE Main or Advanced question starts from a molecular polarisability. |
| Debye relaxation, $K^*$, $\tan\delta$ | **DROP** | frequency-dependent permittivity is not examined; JEE treats $K$ as a constant. |
| Heat, leakage and memory (ESR, dielectric absorption, piezoelectrics) | **DROP** | engineering material behaviour. (Leakage *as a resistor* survives on page 7: $R_pC$ decay.) |
| Gas breakdown and the Paschen law | **DROP** | JEE asks for $V_{\max}=E_bd$ and "air breaks down near 3 kV/mm"; the pressure-gap curve is not asked. The *number* survives in the rating box on page 6. |

### Olympiad-02 "AC, dividers & timing circuits"

| card | verdict | why |
|---|---|---|
| Impedance $Z_C=1/i\omega C$, low-pass $H(\omega)$, cutoff, phase | **HAND-OFF** | AC through a capacitor is a **JEE EMI/AC** topic. One line of it is kept on page 7 ($X_C$, series $RC$, phase, $X_C=R$) so the capacitor chapter is not left incomplete. |
| High-pass and compensated divider | **DROP** | oscilloscope probe compensation; no JEE question. |
| Relaxation timing ($t=RC\ln$, $T=2RC\ln2$) | **KEPT (as method)** | it is the three-number exponential read backwards. Page 7 keeps the inverted-exponential formula; the 555-style oscillator is dropped. |
| Ripple, gentle charging, noise $\sqrt{k_BT/C}$ | **part KEPT** | the reservoir/ripple formula $\Delta V\approx I\Delta t/C$ is a standard JEE circuit question → **kept on page 7**. Ramp heat and thermal noise → **DROP** (noise is not JEE). |

### Olympiad-03 "Coupled RC & specialised models"

| card | verdict | why |
|---|---|---|
| Several independent storage modes ($C\dot V+GV=b$, eigenvalues) | **HAND-OFF** | two-node RC transient is a JEE Advanced *circuits* question, not a capacitor one; it needs matrix formalism JEE does not require. |
| Equal-$R$ equal-$C$ example, $\lambda_\pm=(3\pm\sqrt5)/2RC$ | **DROP** | same reason; the $\sqrt5$ eigenvalue has never been a JEE answer. |
| Measuring can change the voltage $V_{read}=V_0C_s/(C_s+C_m)$ | **KEPT** | pure charge sharing - already a JEE favourite - and it teaches *why* the third condition of "joining two capacitors" matters. Page 7, §5. |
| Wire-to-wire and wire-to-plane capacitance (arcosh) | **DROP** | inverse hyperbolic geometry. The *two-wire* idea stays where JEE needs it: two distant spheres, page 2. |

### Olympiad-04 "Matrices, reciprocity & images"

| card | verdict | why |
|---|---|---|
| Capacitance matrix $Q_i=\sum C_{ij}V_j$, reciprocity, $\sum Q_iV_i'=\sum Q_i'V_i$ | **HAND-OFF** | multi-conductor systems are a natural extension of the island method (page 3, 4 steps); the matrix form is not JEE. |
| Weighting potential / induced signal | **DROP** | detector physics. |
| Charge above a grounded plane (image $-q$, $F$, $W$, $\sigma(\rho)$) | **KEPT** | a genuine **method**: one construction answers a whole family of induced-charge and attraction questions that otherwise need an integral. Page 5, §4, with the half-energy trap. |
| Grounded versus neutral sphere (image $q'=-qa/d$, $r'=a^2/d$) | **DROP (flagged)** | correct and still one line, but the two-image bookkeeping is beyond what JEE asks. **Judgement call** - say the word and it goes back in as a 3-line note on page 5. |

### Olympiad-05 "Shape, conformal maps & pores"

| card | verdict | why |
|---|---|---|
| Spheroids: needle to disc | **DROP** | prolate/oblate formulae are not JEE. The *idea* - sharp curvature → large local field → spark - survives in one sentence on page 2 and in the rating box on page 6. |
| Ellipsoidal inclusions, depolarising factors | **DROP** | no JEE question; $L_1+L_2+L_3=1$ is a physics-competition result. |
| Wedges, corner fields, conformal maps | **DROP** | conformal mapping is not on the syllabus. |
| Porous electrodes, transmission-line pore, $Z_\infty=(1-i)\sqrt{r/2\omega c}$ | **DROP** | electrochemistry / impedance spectroscopy. |

### Olympiad-06 "Pull-in, oscillations & charged drops"

| card | verdict | why |
|---|---|---|
| Voltage-driven movable plate: $\Pi=kx^2/2-\varepsilon AV^2/2(d-x)$, stability $\Pi''>0$ | **KEPT (as method)** | movable plate + spring is the standard JEE "equilibrium of a plate" question, and it teaches the fixed-$Q$ vs fixed-$V$ fork better than any static example. Page 5, §5 - equilibrium and the $d/3$ snap-down.** |
| Pull-in voltage $V_{pi}^2=8kd^3/27\varepsilon A$, softening $\omega^2$ | **KEPT (one paragraph)** | the voltage is the answer to "beyond what voltage is there no equilibrium"; the small-oscillation frequency is **DROP** (needs SHM of a plate, not asked). |
| What changes at fixed charge: $F=Q^2/2\varepsilon A$, $\omega=\sqrt{k/m}$ | **KEPT (as the trap)** | it is the cleanest statement of the fixed-$Q$ / fixed-$V$ fork, and it is already page 4's table in mechanical form. |
| Rayleigh limit of a liquid drop | **HAND-OFF** | charged-drop instability is **fluid mechanics + surface tension**, not capacitors; it is logged for `fluid-mechanics` (§4). |

\**The snap-down voltage is not on the printed JEE syllabus. It is kept as one
paragraph because it follows from the equilibrium equation in two lines. Marked
as "stretch" on the sheet so a student knows it is optional.*

---

## 2. What happened to the eleven JEE sheets

No JEE topic was deleted. The eleven sheets were **repacked into seven** by
removing duplication and reordering into teaching sequence:

| old sheet | topic carried | new home |
|---|---|---|
| JEE-01 conductors, Gauss, potential | conductor facts, Gauss table, equipotential | p1 |
| JEE-02 capacitance, plates, slab, plates-count | definition, plate formula, slab rule, patches, $n$ plates | p2 |
| JEE-03 sphere, cylinder, connected spheres | three geometries + two distant spheres | p2 |
| JEE-04 energy, fixed $Q$ vs fixed $V$ | energy, the fork table, bookkeeping | p4 |
| JEE-05 pressure, insertion, liquid rise | plate force, slab/liquid force, sphere pressure | p5 |
| JEE-06 networks, islands, sources, switches | series/parallel, island method, switching | p3, p7 |
| JEE-07 bridges, cube, delta-star, ladder | four standard results, terminal warning | p3 |
| JEE-08 dielectrics, $D$, layers, patches | polarisation, layers vs patches, ratings | p6 |
| JEE-09 RC, Thevenin, charge/discharge | three-number method, switch rules | p7 |
| JEE-10 charge sharing, heat, branch charge | heat bill, energy ledger | p4 |
| JEE-11 revision checklist | the six sanity checks, numbers | p6 §4, p4 §4 |

Explicitly **dropped from the old JEE sheets** (all non-syllabus): differential
capacitance of a nonlinear dielectric, the $\Phi=q\Omega/4\pi\varepsilon_0$
solid-angle trick, delta-star for capacitors (kept - it is a legitimate Advanced
shortcut), and the "complements the practice paper" filler.

---

## 3. Coverage proof (no JEE topic lost)

Each row is a topic a JEE question can be set on, and the page that now carries it.

| topic | page |
|---|---|
| conductor equilibrium, shielding, grounding | 1 |
| potential/field of sphere, shell, line, sheet, slab | 1 |
| Gauss protocol and the six standard fields | 1 |
| $C=Q/V$, isolated sphere | 2 |
| parallel plate, dielectric fill, metal slab, layers | 2 |
| overlap area and fringing | 2 |
| $n$ plates, unequal plate charges | 2 |
| concentric spheres, coax, coated sphere, two spheres | 2 |
| series, parallel, energy division | 3 |
| island method (4 steps) | 3 |
| balanced bridge, cube, ladder, star-delta | 3 |
| charge through a branch | 3 |
| $U=Q^2/2C$, energy density | 4 |
| fixed $Q$ vs fixed $V$ table | 4 |
| battery work, heat on joining, $H=\frac12C(\Delta V)^2$ | 4 |
| plate force, pressure $p=\sigma^2/2\varepsilon_0$ | 5 |
| slab force, liquid rise | 5 |
| charged-sphere energy and pressure | 5 |
| image charge above a plane (method) | 5 |
| movable plate + spring, snap-down | 5 |
| polarisation, $E$/$V$/$Q$/$U$ scaling | 6 |
| layers vs patches, interface conditions | 6 |
| dielectric strength, ratings, series rating trap | 6 |
| six sanity checks | 6 |
| $RC$ charge/discharge, $\tau$, three-number method | 7 |
| $t=0^+$ / $t=\infty$ switch rules | 7 |
| leakage, ripple, $X_C$, series $RC$ | 7 |
| meter loading / charge sharing | 7 |

Gaps this audit found in the **old** edition, now fixed: no worked numeric example
on any of the 17 old sheets; no page stated the "two plates, two contributions"
factor of $\frac12$ as a trap; fringing never appeared as a limit; and the
"charge through a branch" rule was buried with no example.

---

## 4. Hand-offs to other chapters (not lost, just not here)

| item | belongs to | status |
|---|---|---|
| Debye relaxation, $\tan\delta$, dielectric loss | `electromagnetic-waves` (dispersive media) | logged, optional |
| Two-node coupled RC, eigenvalues $\lambda_\pm$ | `emi-ac` (transient in LCR/RC networks) | logged |
| Coax cable impedance, reflections | `emi-ac` | already present there |
| Capacitance matrix, reciprocity | `electrostatics` (multi-conductor) | logged |
| Rayleigh limit, charged drops | `fluid-mechanics` (surface tension) | logged |
| Movable-plate small oscillations | `simple-harmonic-motion` | logged |

Nothing above is referenced by this chapter's pages, so their removal breaks no
link and no page number.

---

## 5. How to reverse a decision

* `legacy/sheets-v1-jee-olympiad.json` + `legacy/render_sheets_v1.py` rebuild the
  old 17-sheet edition exactly; it is kept for reference only and is not part of
  the gate.
* Any **DROP** row above can be restored by moving it into the matching `KEPT`
  section of `author_notes.py` and re-running:
  `python3 author_notes.py && python3 render_sheets.py && python3 build_exports.py`.
* The "judgement call" items (grounded-sphere image, snap-down voltage) are the
  first candidates if the chapter feels thin.
