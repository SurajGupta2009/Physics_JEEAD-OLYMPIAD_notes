# Electrostatics — source audit and model boundaries

## Primary-source review

Primary source: [`electrostatics/Electrostatics.md`](../../electrostatics/Electrostatics.md), the repository's consolidated Parts 13–15 chapter. Its theory/validity spine, worked-example and practice families, diagram briefs, toolkit, examiner traps, extension problems, paper/formula sections and chapter coverage map guided this edition. The local source gate confirms the 37 core derivation sections' surrounding complete apparatus: 15 blocks, C×14, E×20, Q×56, OL×12, 36-question/200-mark paper, 26 diagram briefs, 10 Mermaid figures, 26 editable scenes and 107 callouts. This gate validates structure/media, not every physics assertion. No claim is made that all 41,014 source words, every exercise solution and every original figure have independently been certified.

The detailed chapter was NOT rewritten. Preserved original SHA-256:

`6033c09818b9df2bd81ee993cc4cb417c445349d74d9a5a007fa9c48561aef29`

The short notes are an explanatory consolidation, not a replacement for every worked exercise. Supporting derivations and boundary-value tools are identified below; original theory remains available as text.

## Corrections and qualifications applied

| Source location / issue | Treatment in these notes |
|---|---|
| §3.1 says only electrons move in all charging | Electron deficit/excess is the ordinary metal model. Ions and charged fragments can transfer; the electron-only assertion is not universal. |
| Work-function rule stated as a universal triboelectric mechanism | Not reproduced. Contact charging depends on materials, surface chemistry and environment; a simple work-function ranking is not a complete general theory. |
| §3.2 mixed-sign triangle gives a below-base resultant and calls magnitude halved | With left positive charge at (0,0), right positive at (a,0), negative apex at (a/2,sqrt(3)a/2), resultant is (-F0/2,+sqrt(3)F0/2), angle 120 degrees from +x. Magnitude changes from sqrt(3)F0 to F0, not exactly half. |
| E1 square check says flipping one sign halves magnitude | Pairwise components, not the informal half claim, are the reliable method. Notes retain exact pair-count/vector rules. |
| §3.5 / E3 finite-rod error language | State half-length L explicitly. Infinite estimate exceeds finite result by sqrt(1+(d/L)^2)-1 relative to the finite value; a different denominator gives a different percentage. |
| §3.7 split ring direction | Positive upper and negative lower semicircles produce a downward field at the centre: perpendicular to their separating diameter, from positive half to negative half. |
| §3.9 equatorial theta-hat check | E_theta=+kp sin(theta)/r^3. At theta=pi/2, theta-hat itself points antiparallel to p. A prose minus theta-hat would reverse that correct direction. |
| OL1 direct in-plane ring-field derivation | For positive ring charge, E_s=-kQs/(2R^3) near the centre, INWARD. A negative test charge therefore has outward force and transverse instability. The source's outward-E sentence contradicts its own correct potential expansion. |
| Earnshaw proof via all-positive second derivatives / every equilibrium a saddle | Use the harmonic maximum principle for the precise no-strict-extremum result. The Hessian test is sufficient only when nondegenerate; constant/degenerate stationary regions need not be ordinary quadratic saddles. |
| Q19 electron wording | An E field opposed to an electron's velocity produces a force along its velocity, so does not stop it. Notes consistently use signed qE; retardation requires the FORCE to oppose the motion. |
| Beam deflection sign after voltage acceleration | Va is a positive accelerating voltage magnitude. Matching Va removes q/m from the magnitude, but opposite charge signs deflect oppositely in the same transverse E. |
| Formula-sheet nonrelativistic voltage threshold | No fixed universal 50 kV threshold retained. State v much less than c and an error tolerance; electron corrections already matter at tens of keV. |
| Q32 and formula-sheet edge flux | For source at (0,0,a/2) in [0,a]^3, opposite side faces each get atan(1/3)/(2pi)=0.05120819117 times q/epsilon0; end faces each get atan(4/3)/(4pi)=0.07379180883 times q/epsilon0. They are NOT four equal 1/16 shares. Their sum is 1/4. Independent direct face quadrature checks both numbers. |
| Point charge on Gaussian boundary | The standard smooth divergence theorem does not assign an unambiguous ordinary enclosed point charge at a singular boundary. Corner/edge fractions here explicitly use the solid-angle/excluding-point boundary convention; faces through that point are assigned zero limiting flux. |
| General conductor cavity / exterior wording | Induced inner TOTAL is -q; outer total is Qc+q for isolated net conductor charge Qc. Exterior is point-like only for a spherical outer boundary with no external symmetry-breaking sources. Grounding fixes V, not total charge. |
| Uniform conductor surface density and curvature mnemonic | A lone isolated sphere is uniform; arbitrary conductor density depends on its entire environment. Sigma proportional to inverse local radius is not a universal theorem. |
| Connected sphere formula and dissipative settling | Q proportional to R assumes spheres far apart and negligible wire capacitance. The decrease in field energy is transferred to heating/radiation/transients, not destroyed. An ideal lossless system needs a relaxation model before assuming it settles. |
| Point self-energy versus pair energy | Finite signed mutual energy excludes divergent self-terms. The positive integral epsilon0 E^2/2 includes self-energy and cannot be equated to a finite point-pair sum without subtraction/regularisation. |
| Image force versus image energy | Real charge feels full image field, but the physical induced energy is half q V_induced. Plane U=-kq^2/(4h), grounded sphere U=-kq^2 R/[2(d^2-R^2)]. Both derivatives are checked. |
| Charged bubble surviving a hole at zero overpressure | Omitted as a dynamical claim. The spherical pressure equality only determines zero overpressure; it establishes neither puncture survival nor shape stability. |
| Rayleigh threshold by pressure equality alone | Threshold formula retained with its ideal incompressible conducting-drop quadrupole-mode assumptions. A radial pressure-scale equality is not a proof of shape-mode stability. |
| Drop merging claimed to predict bouncing at contact | The derived endpoint comparison is for initially far-separated spherical drops. Touching-drop mutual energy, deformation, barriers and dissipation prevent a universal contact/bounce verdict. |
| Induced dipole called always attracted | Positive scalar polarisability in the stated surrounding medium gives attraction up the gradient of E^2. Material/medium response and geometry can change the model. |
| Perturbed inverse-square potential normalisation | Reference scale r0 makes powers/logarithms dimensional. With force coefficient fixed as r^-2(r0/r)^delta, potential includes 1/(1+delta). The uniform-shell first-order near-centre radial signal is retained with its assumptions. |
| Historical exponent limits / nuclear and air limits | No unsupported current precision bound or apparatus-independent safety assertion is repeated. A uniform fixed shell estimate alone is not a full test of a real conductor under a changed force law. |

## Supporting derivations and scope

Core retains demanding equilibrium, finite rods, angular density, cube flux, insulating cavities, particle mechanics, conductor charge ledgers, sharing, concentric grounding and energy checks. The extension section adds/collects the harmonic maximum principle, grounded/isolated sphere images, pressure integrations, bubble/drop qualifications, induced-dipole assembly energy, far-field quadrupoles, cube scaling and converged numerical integrals. The grounded-sphere formulas expand the source's sphere pointer rather than pretending the full derivation was printed there. Ordinary capacitance and circuit details remain in the separate Capacitors chapter; only their minimal electrostatic sharing bridge is retained here.

No official-current-syllabus or frequency audit is claimed. An extension may be derived in an exam from supplied information. Nuclear, microscopic image, thin-wire singularity, infinite-source and breakdown calculations carry their explicit model limits. See [SCOPE.md](SCOPE.md).

## Rendering decisions

All mathematics and geometry are native typeset/analytical assets, not AI-painted equation images. Prose is checked against the bundled handwriting font; body size is not reduced for overflow. Long plot labels use typeset fractions rather than small clipped prose. Diagram captions, ticks, legends and annotation bounds are guarded; visual review additionally caught crowded geometry labels and they were repositioned. All final PNGs retain 300 DPI metadata and the A4 safe inset. PDF images preserve the complete PNG pixel indices and palettes losslessly.

## Publication recheck

The fresh verification adds 94 independent direct-integral, derivative and boundary-condition checks in `revalidate.py`. No change to the explanatory sheet content was required. All 37 PNGs reproduce byte-for-byte from the editable sources; the original detailed chapter hash still matches. The user explicitly authorised publication after this recheck.
