# Coverage and classification

Source: `work-energy-power/Work-energy-power.md` — 1574 lines, Cengage *Mechanics II*
ch 2 §2.24–2.26 plus *Mechanics I* ch 1 §1.17–1.19, with the Olympiad set OL1–OL10
and the Part 11 paper P1–P36. The Markdown is read-only; nothing in it was edited to make
a sheet true.

## Page map

| Source | Sheets | What the sheets do |
|---|---|---|
| 3.1 work of a constant force | JEE 01 | the dot product, the three signs, and why effort is not work |
| 3.2 variable force, F–x area | JEE 02, 12 | integrate; the spring triangle |
| 3.3 work of the standard forces | JEE 03 | force audit: gravity, normal, friction, net |
| 3.4 work–energy theorem | JEE 04, 17 | the derivation, and when to prefer energy over forces |
| 3.4 (cont.) kinetic energy and frames | JEE 05 | K depends on the frame; the theorem stays valid |
| 3.3, 3.14 friction and heat | JEE 06, 21 | f_k d as an internal loss; a spring plus a rough floor |
| 3.5 power | JEE 07, 08, 09, 19 | P = F·v, constant power, gradient power, efficiency |
| 3.6 conservative tests | JEE 10; OLY 12 | closed loop, path independence, curl |
| 3.7 potential energy | JEE 11, 12, 13 | the arbitrary zero, the spring well, gravity and path |
| 3.8 mechanical-energy conservation | JEE 14, 18 | K + U = const; systems and internal work |
| 3.9 U(x) diagrams | JEE 15, 16 | turning points, wells, F = −dU/dx, stability |
| 3.10 energy or force? | JEE 17, 22 | the decision map that closes Part I |
| 3.11 systems and internal work | JEE 18, 20; OLY 01, 07 | two-body energy, chain lifted, chain unrolled |
| 3.12 power in practice | JEE 19, 20; OLY 10, 13 | pumps, chains, flywheels, drag-limited top speed |
| 3.13 F = −∇U | JEE 16; OLY 12 | the gradient in one and in three dimensions |
| 3.14 non-conservative bookkeeping | JEE 06, 14, 22; OLY 11 | named loss terms; the pseudo potential |
| rotation, §3.12–3.14 of the extra block | JEE 23–26; OLY 15–24 | see below |
| OL1–OL10 | OLY 01–10 | CM split, effective potential, bounce series, rolling, wedge, launch, chain, hoop, restitution, flywheel |
| Part 11 paper P1–P36; Parts 12–14 | — | difficulty calibration and the `KEEP` line only, not reproduced as sheets |

## The circular-motion block

The user's instruction was to include **complete circular motion** in this chapter
*if it is genuinely absent from every other chapter*. It was checked, and it is
absent as a complete treatment:

| Where | What exists | What is missing |
|---|---|---|
| `Kinematics/JEE-23/24/25` | angular displacement, ω, α, the three rotation equations, relative angular velocity | nothing dynamical |
| `motion-in-two-dimensions` §3.7–3.10 | the kinematics of uniform circular motion | no forces, no energy |
| `Newtons_Laws` JEE 15–20, OLY 01/02/16/17 | centripetal force, banked corners, conical pendulum, vertical circle, bead on a hoop | all of it force-based; energy is only a shortcut |

So this edition carries the missing half, and it is folded into the two parts
rather than made a third part — a separate "Part III" would have duplicated the
kinematics that already exists elsewhere and would have separated the force view
from the energy view it belongs with.

* **JEE 23–26** — the rotation language this chapter needs before it can use
  energy in a circle: angle, ω, α, the three equations, ω as a vector, and
  a = v²/R derived twice (the Δv construction and the derivative of the unit
  vector). Cross-references to `Kinematics/JEE-23…25` are in the sheets; the
  kinematics is recapped in one move, not re-taught.
* **OLY 15–24** — the dynamical layer the other chapters never reach: a_t and a_n
  together, α as a function of ω, relative angular speed, why the radial force
  does no work, the vertical circle from energy, string versus rod, conical
  pendulum by energy, the full banked band with friction, the wall of death, and
  the radius of curvature of a path that is not a circle.

Counting the block: 4 + 10 = 14 of the 50 sheets.

## The Part I / Part II rule

Part I is the exam craft: what work is, how to integrate it, the theorem, frames,
the conservative tests, potential energy, the U(x) diagram, systems, power and
efficiency, and the four rotation sheets. Part II is where the standard template
fails or needs a second idea: a moving wedge, a coiled chain, an effective
potential, an infinite bounce series, a frame that is not inertial, a rotating
constraint, or an answer that is only valid inside a stated range.

The boundary is relevance, not difficulty. Several Part II sheets (OLY 03, 09)
are easier than JEE 16, and that is deliberate.

## Deliberately out of scope

* Gravitation beyond the two energy statements the source uses (OLY 02, 06).
* Rigid-body rotation with torque and angular momentum — only the point-mass
  dynamics of the circular block and the *energy* of a rolling body (OLY 04) are
  covered. Torque belongs to `Rigid_Body_Dynamics`.
* Collisions beyond the one elastic-limit statement in OLY 01 and 09; the
  collision chapter is `COM-Collisions`.
* Numerical integration and error analysis: `test_exports.py` recomputes printed
  numbers, it does not fit or integrate anything.

## Density rule

No sheet was shrunk to fit. When a topic needed more room than one page allowed,
the edition grew a sheet rather than reducing body text: eight sheets were trimmed
and one equation was split during authoring, and the type sizes are the same on every
page. The `main_px` column of `sheets.json` records each page's measured body
height against its 2062 px budget (the range across the edition is 1543–1855 px),
and `layout.py` refuses to save a page whose body would enter the figure band.
