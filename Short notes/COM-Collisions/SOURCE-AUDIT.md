# Source audit — centre of mass, momentum & collisions

Primary source: `centre-of-mass-momentum/Centre-of-mass-momentum.md`, SHA-256 prefix `8ce5e1832a18`. Verified byte-unchanged. The source is never edited; corrections below are applied only in these short notes.

Every boxed result was independently re-derived or checked from the momentum ledger, energy ledger and geometry. Representative numerical anchors are independently tested in `test_exports.py`. Source slips, ambiguity and added scope are distinguished below.

## Source corrections (a)–(l)

**(a) C9 — equal bounce angles are not independent of e.** For a smooth wall, tangential speed is unchanged and normal speed scales by e. Thus `tan(theta_r) = tan(theta_i)/e`; for e < 1 the rebound is more grazing. Equal angles imply e = 1 (smooth contact, no spin). At 45° with e = 0.5, the rebound angle is 63.4° from the normal and Kf/Ki = 0.625. CM-22.

**(b) E9 — the Check block contradicts the Solution.** Ball at 10 m/s, wall approaching at 5 m/s, e = 0.8: `v_after = v_w - e(v_before-v_w) = -17 m/s`. The ball rebounds at 17 m/s because the wall does work. The source's Check value 7 m/s is a sign slip; the Solution reaches 17. CM-21.

**(c) Q13 — under-specified.** A 3 kg chain lifted at 2 m/s has no unique force without length/hanging length. Give the parametric result `F = lambda*x*g + lambda*v^2`, with `lambda=M/L`. CM-18, CM-22.

**(d) Q18 — dropped factor 1/2.** For 2 kg and 3 kg blocks released by a 2 J spring, momentum gives `v2=-2v1/3`; energy gives `2=(5/3)v1^2`. Correct speeds: `v1=sqrt(6/5)=1.095 m/s`, `v2=0.730 m/s`. Source values 0.926 and 0.617 fail the energy audit. CM-14.

**(e) OL1 + D7.10 — falling chain on a scale: 2mg bookkeeping is wrong.** Let x be landed length/descent: `v^2=2gx`, `m_dot=lambda*v`, so impact flux is `lambda*v^2=2lambda*x*g`; landed weight is `lambda*x*g`; total `F=3lambda*x*g`, ending at 3mg. The source pairs speed with airborne length and obtains 2mg. OLY-01.

**(f) OL2 — arcsin cap on the wrong mass regime.** The cap `theta_max=arcsin(m2/m1)` applies when the projectile is heavier (`m1>m2`). For `m1<m2`, backward scattering through 180° is possible; equal masses give the 90° result. The source's lab-angle tangent formula is retained. OLY-02.

**(g) OL8/P30 — inconsistent staging timeline.** Consistent worked case: 1000 kg initial; two stages each with 400 kg propellant and 50 kg structure; 100 kg payload. `delta-v=3[ln(1000/600)+ln(550/150)]=5.43 km/s`; single-stage with same total propellant/structure kept to burnout gives `3 ln 5=4.83 km/s`. The source walkthrough mixes splits. OLY-06.

**(h) P31(b) — bounce count.** `5(0.36)^n < 0.1` requires `n > ln(0.02)/ln(0.36)=3.83`, so 4 bounces suffice (`h4=0.084 m`), not 5. CM-20.

**(i) P35(c) — spring comparison is conditional.** `x_el/x_in=2 sqrt(M/(m+M))`; elastic compression is greater iff `3M>m`. CM-14.

**(j) OL10 — folded-chain wording ambiguous (“COM + L/4”).** The sheet pins down a standard geometry: midpoint fold just past a smooth table edge, both halves hanging; energy gives `v=y sqrt(2g/L)` and departure speed `sqrt(gL/2)`. OLY-08.

**(k) P36(a) cross-reference.** The kinetic-energy decomposition derivation belongs to §3.9; the source cross-reference is loose, not a physics error. CM-15.

**(l) e notation collision.** The rocket section also uses e for Euler's number while e denotes restitution elsewhere. Sheets use `exp()`/the numeric value where useful; context is stated. CM-17/24.

## Beyond-source addition and closure

- **Deformation/reformation impulses (Cengage Mechanics II §1.22):** `J_d=mu*u_app`, `J_r=e*J_d`, `J=(1+e)*mu*u_app`; energy return fraction is e². Not explicit in the source chapter; included as JEE-core material on CM-10.
- **Chain over a peg (source OL7):** source gives `a=g(2x-L)/L`; integrating from a nudge at L/2 gives `v²=(2g/L)(x-L/2)²`. The unilateral peg force reaches zero at `x/L=(1+1/sqrt(2))/2≈0.854`; contact is lost before the endpoint. The 3mg result belongs to chain landing on a scale, not this peg geometry. OLY-05.
- **Number mapping:** source OL5 is the relativistic-momentum preview (sheet OLY-09); source OL6 is the moving platform (OLY-04); source OL7 peg (OLY-05); source OL8 staging (OLY-06); OL9 jet (OLY-07); OL10 fold (OLY-08). OLY-10/11 are synthesis sheets.

## Assumptions

Smooth contacts unless friction is stated; restitution only along line of impact; g = 10 m/s² in drills unless specified. Verification is representative, not exhaustive; see `VERIFICATION.md`.
