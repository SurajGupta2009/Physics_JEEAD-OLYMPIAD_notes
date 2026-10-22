# Work, energy and power — handwritten-style short notes

50 A4 sheets (2480 × 3508 px, 300 DPI): **26 JEE Main + Advanced** sheets numbered
`01/26 … 26/26`, and **24 Olympiad / extension** sheets numbered `01/24 … 24/24`.
The two parts are numbered independently. Each sheet is one page: a titled question,
numbered moves with equations and prose, a right-hand rail of key-result / gate /
trap / numbers cards, one wide analytical figure, and a `KEEP` line.

Built from `work-energy-power/Work-energy-power.md` (1574 lines; Cengage *Mechanics II*
ch 2 §2.24–2.26 and *Mechanics I* ch 1 §1.17–1.19). The Markdown is unchanged: every
correction is recorded in `SOURCE-AUDIT.md`, not edited into the source.

## The arc of the edition

Part I is the exam craft: what work is (01), how to integrate it (02), which force
does it (03), the theorem and its proof (04), whose kinetic energy it is (05),
where friction's share goes (06), power (07–09), the conservative tests and
potential energy (10–13), conservation and the U(x) diagram (14–16), the decision
rule that closes the block (17), systems, pumps, chains and spring launches
(18–22), then the four rotation sheets the rest of the edition leans on (23–26).

Part II is where the template needs a second idea: the CM split (01), the effective
potential (02), the bounce series (03), rolling energy (04), the false `sqrt(2gh)`
(05), the launch budget (06), the coiled chain (07), the rotating hoop (08),
restitution (09), the flywheel (10), energy in a frame that is not inertial (11),
the curl test (12), the `v³` drag ceiling (13), and where the classical ledger stops
(14). Then the dynamical circular block: `a_t` with `a_n` (15), variable `α` (16),
relative angular speed (17), why the radial force does no work (18), the vertical
circle from energy (19), string versus rod (20), the conical pendulum (21), the full
banked band (22), the wall of death (23), and curvature for a path that is not a
circle (24).

## Complete circular motion — checked before it was added

The brief was to include complete circular motion **only if it is genuinely absent**
from every other chapter. It is absent as a complete treatment, and the check is
recorded in `SCOPE.md`: `Kinematics/JEE-23…25` has the kinematics, `Newtons_Laws`
has the force templates, and neither has the energy view, the `a_t`/`a_n` split,
the effective potential, the friction band with both limits, the rotor, or
curvature. So the block is here, folded into the two parts as 4 + 10 = 14 sheets
rather than made a third part that would duplicate the kinematics.

## What is in the box

| File | What it is |
|---|---|
| `JEE-*.png`, `Olympiad-*.png` | the 50 sheets |
| `work-energy-power-all-pngs.zip` | all 50 PNGs, reading order |
| `work-energy-power-jee-pngs.zip`, `…-olympiad-pngs.zip` | the two parts |
| `work-energy-power-short-notes.pdf` | all 50, A4, one sheet per page, bookmarked |
| `work-energy-power-jee.pdf`, `…-olympiad.pdf` | the two parts, bookmarked |
| `index.html` | offline gallery with per-sheet download links |
| `SCOPE.md` | page map, the circular-motion check, and what is out of scope |
| `SOURCE-AUDIT.md` | what was recomputed, the corrections, the gaps |
| `PRINTING.txt` | one-page print settings |
| `sheets.json` | per-sheet manifest, including the pixel report |
| `verification-results.json` | the numbers `test_exports.py` recomputed |
| `asset-manifest.json` | size and SHA-256 of every generated file |
| `build-environment.json` | interpreter, platform, package versions |

## Rebuild

```
python3 -m pip install --break-system-packages -r requirements.txt
python3 author_content.py      # 50 PNGs + sheets.json   (~1 min)
python3 build_exports.py       # 3 PDFs + 3 ZIPs + gallery + manifests
python3 test_exports.py        # structure, typography, exports, physics checks
python3 _audit_figs.py         # figure text containment, 50 figures
python3 _audit_text.py         # text-on-text collisions, 50 figures
```

Everything is deterministic: `author_content.py` draws with PIL and matplotlib
only, no sampled "handwriting" noise, so a rebuild reproduces the same pixel grid.

## Part I — JEE Main + Advanced

| # | Sheet | File |
|---|---|---|
| 01 | What does it mean to do work? | `JEE-01-work-sign.png` |
| 02 | When the force changes, what replaces F d? | `JEE-02-fx-area.png` |
| 03 | Which forces actually change the energy? | `JEE-03-force-audit.png` |
| 04 | Why is Newton enough to get the work–energy theorem? | `JEE-04-we-theorem.png` |
| 05 | Whose kinetic energy is it? | `JEE-05-ke-frames.png` |
| 06 | Where does the energy go when friction stops a block? | `JEE-06-friction-heat.png` |
| 07 | What is power, and why is it a dot product? | `JEE-07-power-definition.png` |
| 08 | What happens when the power is held constant? | `JEE-08-constant-power.png` |
| 09 | Why does a hill cost so much more than a straight road? | `JEE-09-slope-power.png` |
| 10 | What makes a force conservative? | `JEE-10-conservative.png` |
| 11 | Why can the zero of potential energy be anywhere? | `JEE-11-potential-energy.png` |
| 12 | Why is the spring energy half k x squared? | `JEE-12-spring-energy.png` |
| 13 | Does the route up a hill change the energy? | `JEE-13-gravity-paths.png` |
| 14 | When may you write K + U = constant? | `JEE-14-energy-conservation.png` |
| 15 | What can a potential-energy graph tell you at a glance? | `JEE-15-u-graph.png` |
| 16 | How do you get the force back from the energy? | `JEE-16-force-gradient.png` |
| 17 | Energy or Newton: which method does the question want? | `JEE-17-energy-or-force.png` |
| 18 | What changes when the system has two bodies? | `JEE-18-system-energy.png` |
| 19 | Why does a pump need more power than the water gains? | `JEE-19-efficiency.png` |
| 20 | Why does lifting a hanging chain cost more than its weight? | `JEE-20-chain-work.png` |
| 21 | A spring launches a block onto a rough floor. How far does it go? | `JEE-21-spring-and-friction.png` |
| 22 | What is the whole chapter in one picture? | `JEE-22-wpe-map.png` |
| 23 | Why describe rotation with an angle at all? | `JEE-23-omega-alpha.png` |
| 24 | What are the rotation equations for constant angular acceleration? | `JEE-24-alpha-kinematics.png` |
| 25 | Why is angular velocity a vector? | `JEE-25-omega-vector.png` |
| 26 | Why is circular motion at constant speed still accelerated? | `JEE-26-centripetal.png` |

## Part II — Olympiad / specialised extensions

| # | Sheet | File |
|---|---|---|
| 01 | How much of the energy is actually available? | `Olympiad-01-cm-split.png` |
| 02 | Why does angular momentum keep a planet out of the Sun? | `Olympiad-02-effective-potential.png` |
| 03 | How far does a bouncing ball travel before it stops? | `Olympiad-03-bouncing-ball.png` |
| 04 | Why does a rolling ball beat a sliding block downhill? | `Olympiad-04-rolling-energy.png` |
| 05 | Why is the block on a moving wedge slower than sqrt(2gh)? | `Olympiad-05-block-on-wedge.png` |
| 06 | How much energy does it take to reach orbit? | `Olympiad-06-satellite-launch.png` |
| 07 | Where does the missing half of the work go? | `Olympiad-07-chain-unroll.png` |
| 08 | Why does a spinning hoop make the bead climb? | `Olympiad-08-bead-on-hoop.png` |
| 09 | What does the coefficient of restitution actually measure? | `Olympiad-09-restitution.png` |
| 10 | Who pays for the kinetic energy of a flywheel? | `Olympiad-10-flywheel.png` |
| 11 | Can a force that is not there do work? | `Olympiad-11-pseudo-work.png` |
| 12 | Is one closed loop enough to prove a force is conservative? | `Olympiad-12-path-integral.png` |
| 13 | Why does doubling speed need eight times the power? | `Olympiad-13-drag-power.png` |
| 14 | Where does the energy bookkeeping stop working? | `Olympiad-14-energy-limits.png` |
| 15 | What if the speed changes as well as the direction? | `Olympiad-15-tangential-normal.png` |
| 16 | What if the angular acceleration is not constant? | `Olympiad-16-variable-alpha.png` |
| 17 | How fast do two points on a wheel separate? | `Olympiad-17-relative-angular.png` |
| 18 | If the centripetal force is always inward, how does anything speed up? | `Olympiad-18-work-radial.png` |
| 19 | What speed does a bead have at the top of a loop? | `Olympiad-19-vertical-circle-energy.png` |
| 20 | Why must a string be launched faster than a rod? | `Olympiad-20-string-vs-rod.png` |
| 21 | Why does a conical pendulum ignore the mass? | `Olympiad-21-conical-pendulum.png` |
| 22 | What is the slowest safe speed on a banked corner? | `Olympiad-22-banked-limits.png` |
| 23 | How does a wall of death hold a rider up? | `Olympiad-23-rotor-wall.png` |
| 24 | How tight is a curve that is not a circle? | `Olympiad-24-curvature.png` |

## What has been checked

* `python3 tools/check.py` in `work-energy-power/` — source gate, ALL GOOD, before
  any content was written. The Markdown was never edited.
* `test_exports.py` — 50 pages, 26 + 24 split, independent numbering, one figure per
  sheet and 50 distinct figures, PNG canvas and DPI, top margin, PDF page counts and
  bookmarks, ZIP order and CRCs, every gallery link, plus independent recomputation
  of the printed numbers (see `verification-results.json`).
* `_audit_figs.py` — every text object of every figure inside the canvas: 0 of 50.
* `_audit_text.py` — no two text objects overlap in the same slot: 0 of 50.
* `layout.py` asserts per page: title and question fit, no body overflow, no equation
  crushed below 82 % of its natural width, rail cards fit their height, figure band
  inside its window.

Not checked: no claim that the physics of all 50 sheets has been verified line by
line. `SOURCE-AUDIT.md` states exactly which numbers were recomputed independently,
which were corrected, and which follow the source.
