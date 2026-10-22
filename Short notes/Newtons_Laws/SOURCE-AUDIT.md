# Source audit — what was recomputed, what was corrected, what was not checked

Source of record: `newtons-laws/Newtons-laws.md` (1573 lines, Part 5; Cengage
*Mechanics I*, chapter 7). The Markdown was **not edited**. Where a sheet and the
source disagree, the sheet carries the corrected result and the disagreement is
listed here.

## 1. Corrections to the source

### 1.1 Bottom tension in a vertical circle — factor of two (source line 651)

The source's E6 writes, for the limiting speed, `T = 3mg = 15 N` at the bottom of
the loop with `m = 0.5 kg`, `R = 1 m` (so `sqrt(5gR) = 7.07 m/s`).

Energy from bottom to top: `v_top^2 = 5gR - 4gR = gR`. Then
`T_bot = m v_bot^2 / R + mg = 5mg + mg = 6mg = 29.4 N`, not `3mg`.
The `3mg` value is what the tension would be at the *side* of the loop, not at the
bottom. **JEE 19 prints `T_bot = 6mg`** and works `6(0.4)(9.8) = 23.5 N` for its own
data; the factor is stated in the `KEEP` line so the two results cannot be confused.

### 1.2 Falling chain on a scale — 2mg vs 3mg (source OL1, line 1048)

The source computes the reading as
`F = (m/L)(L - x)g + 2(m/L)xg = (m/L)(L + x)g`, giving `2mg` at `x = L`.

The weight term is wrong: the mass *already on the scale* is `(m/L)x`, not
`(m/L)(L - x)`. With the correct term,
`F = (m/L)xg + 2(m/L)xg = 3(m/L)xg`, so at `x = L` the scale reads `3mg = 58.8 N`
for the source's own 2 kg, 1 m chain. The mass arrival rate
`dm/dt = (m/L)sqrt(2gx)` and the momentum flux `(dm/dt)v = 2(m/L)gx` are both
correct in the source; only the weight term is mis-assigned.

**OLY 08 prints 3mg and states the source's 2mg explicitly**, so a student comparing
the two is not left guessing which was dropped.

### 1.3 A "minimum force" that does not exist (source Q11, line 810)

The question asks for the minimum horizontal force that keeps a 1 kg block from
sliding down a 30 deg incline with `mu_s = 0.6`. The source's own arithmetic gives
`F = 9.8(0.5 - 0.52)/... < 0`, and its check notes `mu_s > tan 30 = 0.577`.

That check is the answer: with `mu_s > tan(theta)` friction alone holds the block,
so the minimum force is `F = 0`, and the negative root is a signal that the
assumed direction of impending motion is wrong, not a force to apply backwards.
**JEE 07 and JEE 09 use the case `mu_s < tan(theta)`**, where a finite force is
genuinely required, and JEE 09 derives the optimum angle `tan(alpha) = mu`.

### 1.4 The pulley constraint sign (source lines 336, 449, 559, 1553)

The source's `a_1 = -2a_2` is correct *for its coordinates* (both downward, `x_1`
for the free end, `x_2` for the movable pulley). It is easy to read as "the block
on the movable pulley is twice as fast", which is the opposite of what the algebra
says: the **free end** moves twice as fast. The relation is also quoted at line 559
with the labels reversed ("if `a_1` is the movable pulley mass").

The sheets keep the constraint and fix the labels: **JEE 13** writes `a_1 = -2a_2`
with `a_1` on the free end, and prints `a_1 = 5.16`, `a_2 = -2.58 m/s^2`. No
disagreement with the source's numbers, only with one of its two verbal readings.

### 1.5 Staging: the source is right, the folklore is not (OL8, line 1130)

The source's OL8 says "the optimal fuel/structure split depends on the imposed
stage dry-mass model; equal ratios are not a universal optimum". This edition
makes that concrete. With the source's own data (1000 kg, 100 kg payload, two
50 kg dry stages, 800 kg of fuel, `v_e = 2 km/s`):

```
f = 0.2   ->  3.67 km/s
f = 0.5   ->  3.62 km/s      (the source's equal split)
f = 0.8   ->  3.50 km/s
f -> 1    ->  3.22 km/s      (all fuel in stage 1, stage 2 empty)
```

The curve is **monotone**, not humped: in this ideal model there is no interior
optimum, and the best split is "as little fuel as possible in stage one". The
interior optimum that textbooks quote needs a dry mass that scales with the
propellant, or gravity and thrust-to-weight losses. **OLY 20 says exactly this**
and separates the two effects: staging at all is worth about 0.40 km/s, the split
inside the sensible range about 0.17 km/s.

### 1.6 Figure briefs (D5.1-D5.12)

The twelve briefs in `newtons-laws/figures.json` were used for composition, not as
physics. Where a brief and the algebra pull in opposite directions — the wedge
brief D5.10 draws the recoil on the side that the constraint puts it — the sheets
follow the constraint. All 50 figures in this edition are newly drawn; none is a
copy of a brief.

### 1.7 Corrections inside this edition (caught by recomputation, before release)

| Sheet | Was | Is | Why |
|---|---|---|---|
| JEE 02 | weight is 0.06 % of the impact force | 0.017 % | `1.42 N / 8.46 kN` |
| JEE 17 | slowest safe speed 10.4 m/s | 10.3 m/s | `sqrt(784(0.454-0.312)/(0.891+0.159)) = 10.30` |
| JEE 18 | conical period 1.27 s | 1.24 s | `2 pi sqrt(0.5 cos40 / 9.8) = 1.242` |
| OLY 19 | momentum check `2(6.30 + 2.52) = 17.6` | `2(6.30 - 2.52) = 7.56 = -M a_w` | the wedge recoil must be subtracted, not added |

## 2. What was checked, and how

**Source gate.** `python3 tools/check.py` inside `newtons-laws/` — ALL GOOD, run
before any sheet was written. The Markdown's hash is unchanged in the merge.

**Arithmetic.** `test_exports.py` recomputes ~100 printed numbers from their own
formulas, independently of the drawing code: Newton's-law arithmetic (JEE 02-14),
friction and belts (07-09, 22, 24), constraints and wedges (13, 25, 26, OLY 03,
05, 06, 19), circular dynamics (15-21, OLY 01, 02, 16, 17), and the Olympiad layer
(chain, rocket, conveyor, capstan, staging, bounce, slack angle, monkey). Each
check is `near(name, value, target, rel)`, and the list is written to
`verification-results.json`.

**Figures.** `_audit_figs.py` walks every text object of all 50 figures and asserts
it lies inside the canvas: 0 of 50 with issues. Label-on-label collisions are not
caught by that script; the 12 figures most at risk were additionally rendered as
standalone probes and inspected.

**Layout.** `layout.py` asserts, per page: title and question fit their boxes, the
main column does not overflow its window, no equation is squeezed below 82 % of
its natural width, every rail card fits the height its contents need, and the
figure band stays inside its window. A failing assert stops the build.

**Exports.** `test_exports.py` checks 50 pages, the 26 + 24 split, independent
numbering, 50 distinct figures, PNG canvas 2480 x 3508 at 300 DPI, top margin,
PDF page counts and one bookmark per sheet, ZIP order and CRCs, and every gallery
link.

## 3. What was not checked

* **Not every line of every sheet.** The ~100 recomputations are representative,
  weighted toward the worked-number blocks, not a proof of all 50 pages of prose.
* **Not the source's Part 11 paper (P1-P36) question by question.** It was read to
  calibrate difficulty; its answers were not reproduced as a test suite.
* **Not the twelve figure briefs' physics claims.** They are treated as layout
  guidance only (section 1.6).
* **No claim about the printed values of physical constants.** `g = 9.8 m/s^2`
  throughout, as in the source; no sheet mixes 9.81 with 9.8.
* **No dimensional analysis pass.** Units are printed per equation where the
  layout has room, not audited everywhere.
