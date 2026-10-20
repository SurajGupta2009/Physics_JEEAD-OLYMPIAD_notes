# Thermodynamics source audit

## Primary source and preservation

The repository's `thermodynamics/Thermodynamics.md`, authoritative HTML-first `Thermodynamics.html`, figure metadata and 35 local SVGs are primary. The source-reading record from the preceding work covered theory, derivations, examples, diagrams, toolkit/traps, the 36-question paper, detailed solutions and final formula sheet. An early compact extractor incorrectly removed inequalities and intervening passages; those passages were recovered before the earlier authoring. This regeneration carries that review forward and checks current formulas, illustrations and exports; it does not claim every original exercise has independently been certified.

The detailed sources are unchanged; no HTML-to-Markdown exporter was run:
- Markdown SHA-256: `35d4b65fcfce071b81d7dcf2efdebb79bb78d30b5dc8c5dc84a57ea756ba4541`
- HTML SHA-256: `28673e895d32aaddbc07ab9bb2106a56fc1f3dcd32e885053b03f780c5c8cab0`

Earlier generated thermodynamics folders were absent from later workspaces for an unestablished reason. This edition is regenerated, not claimed to be a byte-identical recovery. The editable source/build tools were pushed early in this task; final exports are committed and published through the authorised PR workflow. Verification reports describe current files, not missing historical outputs.

## Source corrections applied or errors deliberately not propagated

| Source issue | Treatment in this edition |
|---|---|
| Zeroth-law wall implies molecular traffic | Thermal contact need not transmit matter. Equilibrium means zero net heat transfer. |
| Thermal-stress numerical scale | Y=200 GPa, alpha=12 micro/K, blocked 10 K rise gives 24 MPa, not 2.4 MPa. Full restraint and linear elasticity are stated. |
| Tyre fitting | Initial ID 0.998 m must reach 0.999 m: rise about 83.5 K, not final red-hot/200 C temperature. |
| Bimetal geometry/prose | Higher-alpha layer is the longer OUTER arc on heating. Cooling reverses curvature. Drawn arcs have a common centre. |
| Relative-speed explanation | sqrt(2) is an averaged Maxwellian relative-speed factor, not a literal right angle for every collision pair. |
| Mean-free-path interpretation | At 10 Pa, 273 K, d=3.7 angstrom: lambda about 0.62 mm, not 1.6 m. |
| Flux angular factor | Isotropic hemisphere projection gives 1/4. The printed arrival-weighted cos²/cos ratio is 2/3, not 1/2, and is not the needed derivation. |
| Molecular classification | CO2 is LINEAR, rigid f=5. CH4 is nonlinear and pentatomic. Triatomic does not imply nonlinear. |
| Heat-capacity regimes | CP-CV=R is ideal-gas-specific; constant gamma assumes fixed active modes. CV=7R/2 is vibration-active diatomic, not rigid room-temperature air CV=5R/2. |
| Adiabatic work comparison | One mol monatomic at 300 K doubling V: W and internal-energy loss about 1384 J. Difference from isothermal work about 345 J is not its delta U. |
| Isotherm versus reversible isotherm | Ideal delta U=0 gives Q=W on any isotherm. Logarithmic work additionally needs the quasistatic frictionless boundary-work path. |
| Adiabatic versus isentropic | Q=0 alone does not imply PV^gamma constant or zero entropy generation. Slow/quasistatic alone is insufficient for reversibility. |
| Overloaded exponent n | n=moles, N=particles, nu=number density, s=polytropic exponent. |
| Polytropic summary limits | s=0 isobar; s=1 isotherm; s=gamma reversible adiabat; limiting vertical absolute s to infinity isochore, not isobar. |
| Isothermal path capacity | Nonzero heat divided by zero dT is undefined, not a finite capacity or a phase transition. |
| Gas spring | Isothermal stiffness is 1/gamma of adiabatic: about 29% lower for air, not 8%. |
| Malformed adiabatic identity | Correct constant forms: PV^gamma, TV^(gamma-1), T^gamma P^(1-gamma), with ideal/reversible/constant-capacity conditions. |
| Second-law equivalence proof | Hypothetical work-free fridge returns rejected Qc from cold to hot. Composite converts Qh-Qc from one bath fully into work. |
| Real-engine efficiency gap | Dissipation and finite-temperature heat flow generate entropy. The gap is a second-law limitation, not energy destruction. |
| Carnot derivation header | Explicit PV construction uses an IDEAL gas; reversible efficiency theorem is substance independent. |
| COP temperature equalities | They are reversible ceilings between specified reservoirs, not universal real-device equalities. |
| Cycle entropy statement | Every true cycle has system delta S=0, even if irreversible. A nonzero sum is a ledger/state error. |
| Q15 / T-S area claims | Actual heat equals integral T dS for reversible exchange. Quasistatic but dissipative is insufficient; no general irreversible actual-heat area assertion retained. |
| Small-gap entropy coefficient | Each equal capacity C, FULL gap delta: Sgen approximately C delta²/(4 Tmean²). Define symbols to avoid factor-two ambiguity. |
| Water mixing scale | One kg each at 80 and 20 C generates about 36 J/K for the entire pair, not an undefined per-kg quantity. |
| Atmosphere adiabatic sign | Invariant T P^((1-gamma)/gamma) has a NEGATIVE pressure exponent in that form. |
| Moist lapse comparison | Latent heat usually makes saturated moist ascent cool more gently, staying warmer aloft than a dry prediction from the same base T. |
| Dry-profile zero-T altitude | Formal extrapolated zero marks model breakdown, not a literal atmospheric edge or accessible absolute zero. |
| Moon / retention claims | The Moon has an exosphere; retention depends on exobase T, species, loss mechanism, replenishment and time. Six-rms is only a heuristic. |
| Q34 escape exponent | Lambda=m vesc²/(2kBT)=3 vesc²/(2 vrms²), not merely (vesc/vrms)². Notes give a qualified Jeans flux. |
| Nonideal free expansion called isothermal | The vdW energy-conserving cooling result is insulated free expansion, not simultaneously isothermal without another energy transfer. |
| Joule-Thomson sign and variable | Positive muJT cools on a pressure DROP. Steady adiabatic no-shaft-work throttle conserves h; closed insulated free expansion conserves U. |
| Inversion-temperature scope | 2a/(Rb) is a dilute upper inversion limit, not the full pressure-dependent inversion curve. |
| Radiation spectral labels | 966 nm is infrared, not visible. Peaks per wavelength and per frequency are different locations. |
| Albedo wording | 0.30 to 0.33 is increased reflection/brightening, producing about 2.8 K cooling, not darkening. |
| Photon exponent and notation | Radiation PV^(4/3) is not a naive fixed-mole CP/CV result: photon number is not conserved. a_rad is distinct from vdW a. |
| Cooling Q5 rate comparison | Instantaneous rates at 60 and 80 C differ from first-minute average rate. Only a stated short-interval approximation can identify them. |
| Open-fridge room | 60 cubic metres, not 0.06. Cord input is electrical work; the room's external Q remains zero. |
| Three-leg cycle §8.2 | Specify A=(P0,V0), B=(2P0,V0), C=(P0,2V0), use consistent rigid CV=5R/2. Recomputed eta about 9.94%, not inconsistent printed 7.0% ledger. |
| Baseline state | 1 atm and 24.9 L/mol correspond to about 303.5 K, not exactly 300 K. Define states consistently before numerical substitution. |
| Cycle-extremes figure comparison | Otto example has about 1378/300 K extremes, not the same 2:1 extremes as the three-leg example. Compare actual heat-transfer models. |
| Q14 helium arrival claim | Higher helium flux needs an appropriate density comparison. Thermal equilibrium fixes T, not partial pressures/concentrations. |
| Q17 identical-gas wording | Zero identical-gas mixing entropy assumes matching relevant equilibrium states. Replacement wording must not hide other changes. |
| Q27 sudden-compression algebra | Per mol at half-volume: CV(T2-300)=RT2. Rigid diatomic T2=500 K; TWO-mol work input=8.314 kJ, not 4.16 kJ. |
| Q28 particle counting | Initial rate 3 times 10^21/s is roughly 200 s per mole, not a mole per week. A finite-vessel leak rate changes over time. |
| Q29 T-S hint | Otto has two vertical adiabats and two curved isochores: no horizontal isothermal heat-transfer leg. |
| Q30 exergy comparison | T0 Sgen needs a fixed environment and appropriate endpoint comparison. Direct contact and reversible two-body engine end in different states. |
| Q32 density prose | Air near 1 atm is roughly a kg per cubic metre, not a tonne per two cubic metres. Density equation controls lift. |
| Q33 reservoir count | THREE physical baths (600, 350, 300 K), not four. Outside 300 K has two contributions in one account. |
| Q36 tank maximum work | Closed-gas logarithmic isothermal work is TOTAL, not useful shaft output. Subtract atmospheric displacement: useful availability about 4.361 MJ for 200 atm, 50 L at ambient T. |
| Q36 blowdown cooling | Rigid well-mixed tank needs OPEN-system enthalpy-outflow balance; T(P) exponent (gamma-1)/gamma gives about 66 K, not 36 K. |
| Q36 phase onset | Ideal T=77 K near 1.72 atm is a marker, not a valid air dew point: 77 K is nitrogen's ONE-atm boiling point. No precise phase onset/constant-pressure slush claim retained. |
| Q36 safety verdict | Ideal sealed heating gives 213.3 atm at 320 K from 200 atm, 300 K. Fire safety also needs wall temperature/strength, ratings and relief-system data. |
| Solution Q2 check | 60% of 750 is 450, not 150; erroneous check is not reproduced. |

## Added supporting derivations and model boundaries

Fourier/resistance networks, local heat-sign reversal on P(V), spring loading, regeneration qualifications and mechanical stops are consolidated from standard force/energy balances to complete the thermal revision spine. These are not represented as chapter quotations. Sudden-compression final equilibrium assumes all transient mechanical energy thermalises in the gas; an undamped piston does not simply settle.

No precise real-air phase envelope, universal atmospheric lifetime, engineering safety verdict or official-current-syllabus/frequency audit is claimed. Specialised concepts can be derivable in an exam with supplied information; extension placement does not mean impossibility of appearance.

## Rendering refinements

All prose glyphs are checked against the handwriting font. Scientific powers use explicit supported notation such as `10^(-6)` and species `CO2`, `CH4`; equations have properly typeset subscripts/superscripts. Analytic plot axes do not inherit schematic limits. Tick labels and legends are checked; force directions are distinct. Bimetal arcs are concentric, the heated plate and hole scale together, and the vdW tie line solves coexistence/equal-area conditions numerically. Source pixels are retained losslessly in the PDF exports; body prose is not shrunk to solve overflow.
