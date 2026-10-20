# Source audit — Rigid body dynamics

Audit date: 2026-10-20 (dense JEE revision). Primary source: [Rotational-mechanics.md](../../rotational-mechanics/Rotational-mechanics.md), all 1,529 source lines, including Parts 0–14, derivations, C1–C12, E1–E10, Q1–Q25, OL1–OL10, P1–P36, traps and formula sheet. Also read the chapter README, figures.json (F8.1–F8.6, D8.1–D8.12), diagram briefs and text elements extracted from all 12 native Excalidraw scenes. The new native diagrams implement the physics independently; the existing Excalidraw artwork is not reproduced or visually certified by this audit.

The detailed chapter is **not edited**. Its SHA-256 at creation was `0c92e817bb00ed19607edce22f5891ebdf8c218600bacac68aa1895070d362fb`. These are corrected short notes, not a claim that the source chapter is now error-free. The source's examination-frequency claims are not repeated or independently verified. No current official syllabus or external textbook-wide audit was performed.

## Corrections and qualifications used in the sheets

| Source location | Issue | Independent check / corrected treatment | Destination |
|---|---|---|---|
| §3.2 | theta used as if initial position is zero | Use delta theta, not absolute theta, in constant-alpha equations. Radians required. | JEE 01 |
| E1, Q1, D8.3 | “tangent axis” ambiguous | Disc axis through rim normal to plane: 3MR²/2. Tangent in plane: 5MR²/4. Ring normal-through-rim: 2MR²; ring in-plane tangent: 3MR²/2. State orientation. | JEE 06 |
| §§3.6, 7.3; Part 13 | Scalar and vector L=I omega can be confused | Axis component L(axis)=I(axis) omega for fixed-axis rotation. Planar spin Lz=I(C) omega. General vector spin requires the inertia tensor. | JEE 08; extension 01 |
| Part 13; C7; traps | tau=I alpha “about the COM” is overbroad as a vector assertion | Planar scalar COM equation is valid; arbitrary 3-D motion needs dL/dt. Fixed-axis component equation is valid even for a non-principal axis. | JEE 07, 09; extension 01 |
| §7.1, E9 | Contact shortcut justified merely by zero contact velocity | Derive tau(P)=I(C) alpha+r(C/P) cross M a(C), then use straight-plane circular rolling. Do not generalise to arbitrary moving centres. | JEE 09 |
| C5, P3, repeated static-friction trap | “Static friction does no work” stated without frame/support conditions | Zero power holds for no slip on a stationary rigid support. Moving belts or moving strings can transfer energy without slipping. | JEE 09–10, 13 |
| E4 | alpha=7.5 rad/s², t=2.67 s incorrect | fR/I = mu g/(beta R) = 75 rad/s² for R=.1, beta=.4, mu=.3, g=10. t*=10/(3+7.5)=20/21 s. OL1 and P29 agree with this correction. | JEE 11 |
| D8.8 | Initial v>v0 typo | At t=0, v=v0 and omega=0 in the no-spin example. Both speeds meet continuously at 5v0/7; slopes change at t*. | JEE 11 |
| Q8, Q19 | Incomplete arithmetic and mixed units in intermediate expressions | Q8 alpha=100 rad/s², t*=8/7 s. In Q19 write R omega=-5+5t (m/s), not omega=-5+alpha t. t*=15/7 s. | JEE 11 |
| C11, P12 | Backspin said to always produce forward rolling | General final speed [v0+beta R omega0]/(1+beta) may be positive, zero or negative. Sufficient backspin reverses motion; the equality case comes to rest. | JEE 11 |
| E9 | Friction claimed backward for top-pulled disc | F+f=Ma; FR-fR=I a/R. With beta=.5, a=4F/(3M), f=+F/3 forward. Acceleration in source was correct. | JEE 12 |
| OL4, P35 | Reversal criterion depends on mu(k), winding not specified | Explicit lower-hub tangent, pull angle phi: a=F(cos(phi)-r/R)/[M(1+beta)]. Reversal at cos(phi)=r/R, not mu R/r. mu(s) tests feasibility, not reversal. Upper tangent has opposite hub torque. | JEE 12 |
| P35 numeric statement | F and I absent | For the specified lower winding, horizontal pull gives acceleration toward puller if rolling is possible. Cannot establish rolling feasibility from mu, M, R, r alone; need F and I. | JEE 12 |
| P31 | Tension too small by factor 2 | T=Mg-aM=MgR²/(2r²+R²) for I=MR²/2. At r=R gives T=Mg/3 and a=2g/3. | JEE 13 |
| Q22 | Last denominator mixes lower-case l and upper-case L | Uniform notation l: omega=mv/[l(M/3+m)]. | JEE 14 general d=l case |
| §9.6 | Hinge reaction called finite during impact | Hinge impulse may be large. Its angular impulse about the hinge is zero, not its force. Neglect gravitational angular impulse only for a sufficiently brief collision. | JEE 14 |
| P28(c) | Loss said maximal at far-end hit | Q=(mv²/2) I0/(I0+md²) decreases with d>=0. Maximum loss at smallest allowed d; at zero offset all bullet KE is lost in the ideal fixed-hinge model. Angular speed itself peaks at d=sqrt(I0/m), if in allowed range; neither claim in source is generally right. | JEE 14 |
| E3 | Rounding | I(f)=1/3+.0025=.335833333; omega=5.95533499 rad/s (5.96 to 3 significant figures). | JEE 14 |
| C12 | Million-block overhang 7.48l incorrect | H(10^6)/2 = 7.19636336. H(10)/2=1.46448413. Overhang is a marginal COM equilibrium; rigidity and tolerances are important, but lateral friction is not needed for ideal horizontal gravity-only stacks. | JEE 16 |
| D8.10 | Ladder slip mixed with block tipping / base-edge normal | Separate the point-contact ladder from a finite-base block and its pressure resultant. | JEE 16 |
| E7; §7.4; Part 13 | Pendulum result missing small-amplitude condition in some places | I theta-double-dot=-Mgd sin(theta); linearise only near stable downward equilibrium. E7's 1.64 s is consistent with g≈9.8, while P24 uses g=10 and gives 1.62 s. | JEE 18 |
| OL6, P32 | “Oscillations are SHM” without amplitude limit | Exact equation has sin(theta); only small oscillations are SHM. q=R-r is exact in circular geometry; R much greater than r is unnecessary. Contact/friction remain conditions. | JEE 18 |
| OL3, P33 | Detachment uses cosine while energy uses floor-angle sine; COM speed also wrong | Floor angle theta: theta-dot²=(3g/l)(sin(theta0)-sin(theta)); Nw=(3Mg/4)cos(theta)[3sin(theta)-2sin(theta0)]. Hence sin(theta*)=2sin(theta0)/3, v(C,*)=sqrt(gl sin(theta0))/2. | JEE 19 |
| P33(c) | Contradictory vertical-release claims | Perfectly vertical and motionless is degenerate; ideal equations alone do not select a perturbed falling trajectory. State 0<theta0<pi/2 for the derivation and discuss a limiting perturbation separately. | JEE 19 |
| §4.2 | beta→infinity called “mass at rim” | A body with all mass within radius R has beta<=1; rim mass gives beta=1, not infinity. The formal effective-inertia limit is not a usual wheel-shape limit. | JEE 10 excludes false identification |
| Part 8 trap 11 | Smooth and insufficiently rough conflated; all bodies said to rotate while sliding | On a perfectly smooth incline a symmetric body's gravity has no torque about C; initially zero spin stays zero. Insufficient roughness instead requires kinetic-friction dynamics. | JEE 10–11 |
| P13 | Parallel-axis theorem said valid for any two parallel axes by adding Md² | The reference term must be about the COM parallel axis. Use separate COM shifts otherwise. | JEE 06 |
| P15 | Zero torque at a moving axis asserted sufficient | With absolute velocities about A: dL(A)/dt=tau(A)-v(A) cross M v(C). Fixed origins and CM are safe cases. | JEE 08; extension 01 |
| P9 | Single-correct question gives two correct choices | Do not reproduce the flawed MCQ. Dependence is explained directly. | JEE 18 |
| Traps 9, 10 repeated | Duplicate numbering and repeated topics | Consolidate warnings into concept cards, not a second duplicate trap list. | throughout |
| §4.5, §9.2, §10.2, P36 | Slow precession labelled a small-tilt approximation; large tilt equated with nutation | At nonzero tilt both torque and rate of L contain sin(theta). Slow precession needs dominant spin and appropriate motion/initial conditions, not small tilt alone. | extension 02 |
| §4.2 | omega→0 gives “instantaneous fall” | This exits the fast-spin approximation. Do not extrapolate its singular expression. | extension 02 |
| OL7, P36 | Sleeping-top condition uses unspecified I and an invented R/r factor | Ideal fixed-point upright heavy symmetric top: (I3 omega3)²>4Mgd I(perp), where I(perp) is about the pivot. Derived by linearised tilt dynamics. Real tip dissipation is model-dependent. | extension 02 |
| OL8 | Dumbbell L decomposition uses an incorrect direction | For unit rod direction n and masses ±a n: L=2ma²[omega-(omega dot n)n]. It has zero component along n. | extension 01 |
| OL10, P34 | Elastic-stress result not accompanied by all material conditions | Retain as supplied-model extension: thin uniform isotropic free-edge disc, no bore, plane stress. K/M=2 sigma/[rho(3+nu)]=38.85 kJ/kg with source parameters. No universal battery-performance comparison retained. | extension 03 |

## Unresolved source models — deliberately not “solved” by inventing assumptions

**OL5 carpet.** No unique R-to-speed law is specified. A finite-radius roll needs thickness/packing and core information. Mass leaving the roll may be brought to rest dissipatively. The instantaneous m(R) and I(R) relations alone do not determine the energy flux or deposition loss. Extension 04 displays the supplied continuum approximation and explicitly lists missing laws. A separate definite model would be needed for a closed-form answer.

**OL9 rod onto peg.** Smooth floor does not fix the bottom, and initial perfect vertical balance requires a perturbation. Peg geometry, simultaneous support impulses, restitution/capture and whether contact becomes a hinge are unspecified. Extension 04 gives conditional phase logic, not a numerical swing-over condition. Once those conditions are supplied, this can become a core-principle JEE-style problem; the under-specified original is not made “Olympiad” merely by being difficult.

## Verification method and limits

Equations were re-derived from Newton–Euler balances, the velocity constraint, energy and angular impulse. Representative numerical and limiting checks are automated in `test_exports.py`; examples include E2, corrected E4, E9, P28 monotonicity, P31 tension, sliding-rod normal force, bowl frequency, dumbbell vector direction and stress-limited energy. All displayed math is pre-parsed by matplotlib, but parsing is not a physics proof. Every new page received visual review; programmatic checks cover bounds and print/export metadata. This is not a complete solution-by-solution certification of the source paper, nor a formal proof of every extension model.

## Dense JEE revision — added coverage and independent checks

The original source is still primary, but its short standard-body table is not enough for a useful JEE MOI revision resource. The revised notes explicitly add standard axis variants and derivations, rather than implying every new expression was already printed in the source.

- **JEE 02–05:** rod offset/oblique axes; rectangle and square axes; ring/disc normal, diameter and tangent axes; annulus; half-disc/half-wire COM shifts; solid/hollow cylinders with transverse axes; solid/thin/thick spherical shells; off-centre disc hole; nonuniform rod; radial-density disc; cone axial integration. These follow from the source's inertia integral, axis theorems and COM bookkeeping. Numerical quadrature independently checks representative coefficients and limits.
- **JEE 06–14, 16, 18–19:** added brief algebra, standard specialisations, support/friction inequalities and limiting checks beside the existing explanations. No body text was reduced in size.
- **JEE 15:** single-direction eccentric impulse and normal restitution for an initially resting free target; the effective denominator D=1/m+1/M+b²/I is derived from contact-point speed. This assumes a central incident particle velocity along the impulse direction and no other relevant impulsive forces. Normal restitution e=0 alone does not guarantee capture. For the hinged-body centre of percussion, the impulse is transverse to the O–COM line; the body starts at rest.
- **JEE 17:** fixed-hinge rod fall and endpoint reactions; inside-loop rolling energy/contact lower bound h>=(5+beta)(R-r)/2. This bound assumes ideal no slip. Finite static friction must also satisfy |f|<=mu(s)N everywhere; at the marginal top-energy limit, that may fail near the top. It is NOT advertised as sufficient for a finite-friction roller.
- Source corrections in the earlier table remain in force. Only local JEE page references were renumbered. The original detailed Markdown hash is still checked.

Additional numerical tests include direct rod, cylinder, sphere, shell, cone and variable-density mass integrals; restitution and energy loss at e=0, 0.4 and 1; centre of percussion; and the corrected slip-stage displacement. These supplement, not replace, the derivation and visual reviews.
