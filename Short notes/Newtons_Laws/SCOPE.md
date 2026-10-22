# Coverage and classification

Source: `newtons-laws/Newtons-laws.md` — 1573 lines, Part 5 of the notes set,
built from Cengage *Mechanics I*, chapter 7 (Newton's laws of motion).
The Markdown is read-only; nothing in it was edited to make a sheet true.

## Page map

| Source | Sheets | What the sheets do |
|---|---|---|
| 3.1 first law, inertial frames | JEE 01 | force as the bookkeeping of interactions; the van that has to invent a force |
| 3.2 second law | JEE 02 | F = ma as the definition of force plus the impulse budget |
| 3.3 third law | JEE 03 | pairing audit; why N is not the reaction to mg |
| 3.4 free-body method | JEE 04, 10, 11 | the diagram, stacking, system vs parts |
| 3.5 standard forces, apparent weight | JEE 05, 06 | lift readings, Lami |
| 3.6 equilibrium | JEE 06 | triangle closure |
| 3.7 static friction | JEE 07, 09 | the range, the optimum pull angle |
| 3.8 kinetic friction | JEE 08, 22, 24 | direction on a belt, a rough pulley, measuring mu |
| 3.9 systems | JEE 11, 12, 13 | contact forces, Atwood on a ramp, the movable pulley |
| 3.10 constraints | JEE 13, 25, 26; OLY 03, 06 | differentiate the length; wedges and chains |
| 3.11 pseudo forces | JEE 14, 23 | the accelerated frame, a ramp that holds a block |
| 3.12 circular dynamics | JEE 15-20, 21; OLY 01, 02, 16, 17 | crest, bank, conical, vertical circle, hoop, slack angle |
| 3.13 vertical circle | JEE 19, 20, 21; OLY 17 | string vs rod, energy shortcut, the release angle |
| 3.14 multi-body | OLY 03, 05, 19, 24 | wedge recoil, liftoff, momentum, the monkey |
| Part 10 OL1-OL10 | OLY 07-16 | falling chain, rocket, capstan, conveyor, hoop, staging, impulse window, hitch |
| Parts 12-13 (paper P1-P36) | - | used as a difficulty calibration, not reproduced as sheets |
| Part 14 (checkpoint) | - | used to choose the `KEEP` line of each sheet |

## The Part I / Part II rule

Part I (JEE) is everything a JEE Main + Advanced candidate is expected to produce
under time pressure: the standard force inventory, friction as a range, constraint
algebra, pseudo forces, and the four circular-dynamics templates.

Part II is everything where the standard template fails or needs a second idea:
a moving wedge, a variable mass, a rope that grips a bollard, an infinite series
of bounces, a frame that is not inertial, or a result whose validity has to be
stated. The boundary is relevance, not difficulty: several Part II sheets are
easier than JEE 17, and that is deliberate.

## Deliberately out of scope

* Rigid-body rotation, torque, angular momentum of extended bodies, and rolling
  with slipping — only the point-mass circular dynamics of 3.12 and the contact
  kinematics of one rolling wheel (OLY 22) are covered. The source chapter does
  not develop them either.
* Gravitation, work-energy theorems beyond the vertical-circle shortcut, and
  collisions — used only where the source uses them (OLY 15, 18).
* Numerical simulation and error analysis: `test_exports.py` recomputes printed
  numbers, it does not fit or integrate anything.

## Density rule

No sheet is shrunk to fit. When a topic needed more room than one page allowed,
the edition grew a sheet (JEE 21-26 and OLY 17-24 exist for that reason) rather
than reducing body text below 45 px on a 2480 px canvas.
