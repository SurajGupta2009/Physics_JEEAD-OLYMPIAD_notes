# Newton's laws of motion — handwritten-style short notes

50 A4 sheets (2480 x 3508 px, 300 DPI): **26 JEE Main + Advanced** sheets numbered
`01/26 ... 26/26`, and **24 Olympiad / extension** sheets numbered `01/24 ... 24/24`.
The two parts are numbered independently. Each sheet is one page: a titled question,
numbered moves with equations and prose, a right-hand rail of key-result / gate /
trap / numbers cards, one wide analytical figure, and a `KEEP` line.

Built from `newtons-laws/Newtons-laws.md` (Part 5 of the notes set, 1573 lines,
source: Cengage *Mechanics I*, chapter 7). The Markdown is unchanged: every
disagreement is recorded in `SOURCE-AUDIT.md`, not edited into the source.

## The arc of the edition

Part I is the exam craft: the three laws and the free-body method (01-04), standard
forces and apparent weight (05-06), friction as a range rather than a formula
(07-09), systems and constraints (10-13), pseudo forces (14), circular dynamics
(15-20), then five "why is this shortcut legal" sheets that close the part
(21-26). Part II is the Olympiad layer: rotating frames and turntables (01-02),
wedge constraints and virtual work (03-06), variable mass and the rocket
(07, 09, 14, 20), friction-driven mechanisms (12-13), impulse limits (15), the
bead on a hoop (16), the slack angle (17), the bounce series (18), momentum on a
wedge (19), rolling contact (22), the four shortcuts (23), the monkey and its
counterweight (24), and an honest statement of where the model stops (21).

## What is in the box

| File | What it is |
|---|---|
| `JEE-*.png`, `Olympiad-*.png` | the 50 sheets |
| `newtons-laws-all-pngs.zip` | all 50 PNGs, reading order |
| `newtons-laws-jee-pngs.zip`, `...-olympiad-pngs.zip` | the two parts |
| `newtons-laws-short-notes.pdf` | all 50, A4, one sheet per page, bookmarked |
| `newtons-laws-jee.pdf`, `...-olympiad.pdf` | the two parts, bookmarked |
| `index.html` | offline gallery with per-sheet download links |
| `SCOPE.md` | page map, the Part I / Part II rule, and what is out of scope |
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
```

Everything is deterministic: `author_content.py` draws with PIL and matplotlib only,
no sampled "handwriting" noise, so a rebuild reproduces the same pixel grid.

## Part I — JEE Main + Advanced

| # | Sheet | File |
|---|---|---|
| 01 | What is a force, really? | `JEE-01-inertial-frames.png` |
| 02 | Is F = ma the law, or a special case? | `JEE-02-second-law.png` |
| 03 | Why is the normal force not the reaction to weight? | `JEE-03-third-law.png` |
| 04 | How do you draw a diagram that never lies? | `JEE-04-free-body.png` |
| 05 | What does a weighing scale actually measure? | `JEE-05-apparent-weight.png` |
| 06 | Three forces, no acceleration: why does the triangle close? | `JEE-06-lami.png` |
| 07 | Is friction equal to mu N? | `JEE-07-static-friction.png` |
| 08 | Which way does friction point? | `JEE-08-friction-direction.png` |
| 09 | Why is the easiest pull not horizontal? | `JEE-09-min-pull.png` |
| 10 | When do two stacked blocks stop moving together? | `JEE-10-stacked-blocks.png` |
| 11 | System or single body: which do you solve? | `JEE-11-system-vs-parts.png` |
| 12 | Atwood on a ramp: where does the motion change hands? | `JEE-12-atwood-ramp.png` |
| 13 | Why does the free end move twice as far? | `JEE-13-movable-pulley.png` |
| 14 | Should you ever add a force that is not there? | `JEE-14-pseudo-force.png` |
| 15 | Is centripetal force a new force? | `JEE-15-centripetal-source.png` |
| 16 | Why are racetrack corners banked? | `JEE-16-banked-design.png` |
| 17 | How much slower or faster can you take the bank? | `JEE-17-banked-band.png` |
| 18 | Why does a conical pendulum ignore the mass? | `JEE-18-conical-pendulum.png` |
| 19 | What is the slowest a ball can go round a vertical loop? | `JEE-19-vertical-circle-string.png` |
| 20 | Why can a bead on a rod stop at the top? | `JEE-20-vertical-circle-rod.png` |
| 21 | Why is energy faster than forces in a vertical circle? | `JEE-21-energy-shortcut.png` |
| 22 | What changes when the table is rough? | `JEE-22-rough-table-pulley.png` |
| 23 | Can an accelerating ramp hold a block still? | `JEE-23-accelerating-incline.png` |
| 24 | How do you measure friction without a force meter? | `JEE-24-measuring-mu.png` |
| 25 | Why does a chain accelerate faster as it falls? | `JEE-25-chain-over-edge.png` |
| 26 | How hard must you push a wedge to carry its block? | `JEE-26-wedge-carry.png` |

## Part II — Olympiad / specialised extensions

| # | Sheet | File |
|---|---|---|
| 01 | Is there friction on a block tied to the axis? | `Olympiad-01-turntable-string.png` |
| 02 | Why does a coin and a brick slip at the same speed? | `Olympiad-02-turntable-limit.png` |
| 03 | Why is the block's acceleration not along the face? | `Olympiad-03-wedge-constraint.png` |
| 04 | What is g inside a lift, a car, a centrifuge? | `Olympiad-04-effective-gravity.png` |
| 05 | When does a block leave a wedge that is pulled away? | `Olympiad-05-wedge-liftoff.png` |
| 06 | Why can you ignore the normal force in a work calculation? | `Olympiad-06-virtual-work.png` |
| 07 | At what length does a rope over an edge start to slide? | `Olympiad-07-rope-over-edge.png` |
| 08 | Does a falling chain weigh three times as much? | `Olympiad-08-falling-chain.png` |
| 09 | Why is the cost of speed logarithmic? | `Olympiad-09-rocket-equation.png` |
| 10 | Why does a conveyor belt need twice the power? | `Olympiad-10-sand-conveyor.png` |
| 11 | Why does lifting a chain cost more than its weight? | `Olympiad-11-chain-lift.png` |
| 12 | Why can one hand hold a ship? | `Olympiad-12-capstan.png` |
| 13 | How does a friction hitch hold a falling climber? | `Olympiad-13-friction-hitch.png` |
| 14 | Why does staging beat one big tank? | `Olympiad-14-staging.png` |
| 15 | When is it safe to ignore gravity during a hit? | `Olympiad-15-impulse-window.png` |
| 16 | Why does a spinning hoop push its bead up the wire? | `Olympiad-16-bead-on-hoop.png` |
| 17 | At what angle does a slackening string let go? | `Olympiad-17-slack-angle.png` |
| 18 | How far does a bouncing ball travel before it stops? | `Olympiad-18-bounce-series.png` |
| 19 | Is horizontal momentum really conserved on a wedge? | `Olympiad-19-wedge-momentum.png` |
| 20 | Where should the fuel go between two stages? | `Olympiad-20-stage-split.png` |
| 21 | Where exactly do Newton’s laws stop being true? | `Olympiad-21-model-limits.png` |
| 22 | If a rolling wheel is not sliding, what is friction doing? | `Olympiad-22-rolling-contact.png` |
| 23 | What are the four moves that solve almost every problem here? | `Olympiad-23-four-shortcuts.png` |
| 24 | Can a monkey climb away from its own counterweight? | `Olympiad-24-monkey-rope.png` |

## What has been checked

* `python3 tools/check.py` in `newtons-laws/` — source gate, ALL GOOD, before any
  content was written. The Markdown was never edited.
* `test_exports.py` — 50 pages, 26 + 24 split, independent numbering, one figure
  per sheet and 50 distinct figures, PNG canvas and DPI, top margin, PDF page
  counts and bookmarks, ZIP order and CRCs, every gallery link, plus ~100
  independent recomputations of numbers printed on the sheets.
* `_audit_figs.py` — every text object of every figure inside the canvas.
* `layout.py` asserts per page: title and question fit, no body overflow, no
  equation crushed below 82 % of its natural width, rail cards fit their height,
  figure band inside its window.

Not checked: no claim that the physics of all 50 sheets has been verified line by
line. `SOURCE-AUDIT.md` states exactly which numbers were recomputed independently
and which follow the source.
