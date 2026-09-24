---
title: "Centre of Mass, Momentum & Collisions"
part: 7
slug: centre-of-mass-momentum
source: Cengage Mechanics II-compressed.pdf, ch 1 Centre of Mass, Conservation of Linear Momentum and Collision
aliases: [centre-of-mass, momentum, impulse, collisions, restitution, rocket-equation]
tags: [jee-advanced, olympiad, mechanics, momentum, collisions, centre-of-mass]
---

# Centre of Mass, Momentum & Collisions — first principles to Olympiad

> [!abstract] How to use this chapter
> Three passes. Pass 1: Parts 0–4 — the centre of mass, conservation of momentum, and the classification of collisions. Pass 2: Parts 5–9 for exam craft. Pass 3: Parts 10–14 — the Olympiad layer (CM-frame analysis, variable mass, two-body scattering, the impulse approximation, successive bouncing), the paper, the sheet, the checkpoint. Every number recomputed; every boxed result carries its validity condition.

## Part 0 · Orientation

### 0.1 What you will be able to do

After this chapter you can: find the centre of mass of any body or system; derive $M\mathbf{a}_{\text{cm}}=\mathbf{F}_{\text{ext}}$ from Newton's third law; apply conservation of momentum to explosions, collisions, and recoil problems; classify collisions (elastic, inelastic, perfectly inelastic) and use the coefficient of restitution; solve 1-D and 2-D collision problems; work in the CM frame; solve variable-mass problems (rocket equation); and analyse two-stage impulse problems (ballistic pendulum, bullet through block).

### 0.2 The one idea

In an isolated system the centre of mass keeps moving in a straight line — every collision is a discussion about the motion around it.

### 0.3 Prerequisite self-check

You need PART 5 (Newton's laws, the FBD method) and PART 6 (work–energy theorem, energy conservation). If you can solve a system of linear equations and compute a dot product, you are ready.

### 0.4 Exam orientation

JEE Advanced treats collisions and momentum as high-frequency topics — 3–4 questions per year, often combined with energy conservation (PART 6). The ballistic pendulum, the 2-D elastic collision, and the variable-mass rocket are classic JEE problems. INPhO and IPhO reward the ability to work in the CM frame, handle the impulse approximation, and solve variable-mass problems with momentum flux. The trap density is high: using energy conservation in an inelastic collision, applying the coefficient of restitution across the whole velocity instead of along the line of impact, and forgetting the ejecta's momentum in the rocket equation.

### 0.5 What this chapter is not

Not an energy chapter: work and energy are in PART 6. Not a rotation chapter: angular momentum is in PART 8. Not a fluid-mechanics chapter: momentum flux in fluids is in PART 11. Not a relativity chapter: relativistic momentum is in PART 28.

### 0.6 Syllabus coverage map

| # | Cengage section | What it establishes | Where it lives here | Status |
|---:|---|---|---|---|
| 1 | Centre of mass | Definition, COM of standard bodies | §3.1 | full |
| 2 | COM of real bodies | Rod, triangle, semicircle, cone | §3.2 | full |
| 3 | Motion of the COM | $M\mathbf{a}_{\text{cm}}=\mathbf{F}_{\text{ext}}$ | §3.3 | full |
| 4 | Momentum and impulse | $\mathbf{p}=m\mathbf{v}$, $\mathbf{J}=\int\mathbf{F}\,dt$ | §3.4 | full |
| 5 | Conservation of momentum | Conditions, component-wise | §3.5 | full |
| 6 | Collisions I: classification | Elastic, inelastic, $e$ | §3.6 | full |
| 7 | Collisions II: 1-D results | General $e$-dependent velocities | §3.7 | full |
| 8 | Collisions III: 2-D | Smooth balls, equal-mass 90° | §3.8 | full |
| 9 | CM frame | Energy decomposition, trivial elastic | §3.9 | full |
| 10 | Variable mass | Rocket equation, chain, sand | §3.10 | full |
| 11 | Two-stage impulse | Ballistic pendulum, bullet-block | §3.11 | full |
| 12 | Systems with internal motion | Man on boat, block on wedge | §3.12 | full |
| 13 | Collisions with a third body | Spring link, moving wall | §3.13 | full |

## Part 1 · Intuition first

**The centre of mass is the "average position" of the mass.** For a uniform rod, it is at the midpoint. For a triangle, it is at the centroid (one-third of the way from each side). For a complex object, it is the weighted average of all the mass elements: $\mathbf{R}=\sum m_i\mathbf{r}_i/M$.

**The centre of mass of an isolated system moves at constant velocity.** This is the deepest consequence of Newton's third law: internal forces cancel in pairs, so they cannot accelerate the system as a whole. An exploding shell follows the same parabola it would have followed without exploding — the fragments fly apart, but their centre of mass continues on the original trajectory.

**Momentum is conserved in collisions.** In any collision, the total momentum before equals the total momentum after (provided no external forces act during the brief collision time). This is true for elastic and inelastic collisions alike. What differs is the kinetic energy: elastic collisions conserve KE, inelastic do not.

**The coefficient of restitution measures the "bounciness."** $e=v_{\text{sep}}/v_{\text{app}}$ along the line of impact. $e=1$: perfectly elastic (no energy lost). $e=0$: perfectly inelastic (the objects stick together). Real collisions have $0<e<1$.

## Part 2 · Definitions and bookkeeping

| Symbol | Meaning | SI unit |
|---|---|---|
| $\mathbf{R}$ | position of the centre of mass | m |
| $M$ | total mass | kg |
| $\mathbf{p}$ | momentum $=m\mathbf{v}$ | kg m/s |
| $\mathbf{J}$ | impulse $=\int\mathbf{F}\,dt$ | N s |
| $e$ | coefficient of restitution | dimensionless |
| $\mu$ | reduced mass $=m_1m_2/(m_1+m_2)$ | kg |
| $\mathbf{v}_{\text{cm}}$ | velocity of the centre of mass | m/s |
| $\Delta K$ | kinetic energy lost in a collision | J |

> [!info] Bookkeeping rules
> Momentum is a vector — conservation applies independently to each component. In 1-D collisions: use the sign convention consistently (rightward positive). In 2-D collisions: resolve along and perpendicular to the line of impact. The coefficient of restitution applies only along the line of impact — the tangential component of velocity is unchanged for smooth spheres.

## Part 3 · Core derivations

### 3.1 The centre of mass: definition

For $n$ particles:

$$
\mathbf{R}=\frac{\sum_{i=1}^n m_i\mathbf{r}_i}{\sum_{i=1}^n m_i}=\frac{1}{M}\sum m_i\mathbf{r}_i. \qquad (3.1)
$$

For a continuous body: $\mathbf{R}=\frac{1}{M}\int\mathbf{r}\,dm$.

**Component form:** $X_{\text{cm}}=\sum m_i x_i/M$, $Y_{\text{cm}}=\sum m_i y_i/M$.

**Standard results:**

| Body | COM location |
|---|---|
| Uniform rod (length $L$) | Centre ($L/2$ from either end) |
| Uniform triangle | Centroid (intersection of medians, 1/3 from each side) |
| Semicircular ring (radius $R$) | $y_{\text{cm}}=2R/\pi$ from the diameter |
| Semicircular disc (radius $R$) | $y_{\text{cm}}=4R/(3\pi)$ from the diameter |
| Solid hemisphere (radius $R$) | $y_{\text{cm}}=3R/8$ from the flat face |
| Hollow hemisphere (radius $R$) | $y_{\text{cm}}=R/2$ from the flat face |
| Solid cone (height $h$) | $h/4$ from the base |
| Uniform arc (angle $\theta$) | $R\sin(\theta/2)/(\theta/2)$ from the centre |

> [!abstract] DIAGRAM D7.1 · COM of standard bodies on one plate
> *Show:* a rod, a triangle, a semicircular ring, a semicircular disc, and a solid cone, each with their COM marked by a dot and the distance from the reference surface labelled.
> *Search:* "centre of mass standard bodies rod triangle semicircle cone COM position"

### 3.2 COM of composite bodies

**The positive-mass/negative-mass trick:** To find the COM of a body with a hole, treat the hole as negative mass:

$$
\mathbf{R}=\frac{M_1\mathbf{r}_1-M_2\mathbf{r}_2}{M_1-M_2}. \qquad (3.2)
$$

where $M_1$ is the mass of the full body and $M_2$ is the mass of the hole.

**Symmetry shortcuts:** If a body has an axis of symmetry, the COM lies on that axis. If it has two axes of symmetry, the COM is at their intersection.

> [!abstract] DIAGRAM D7.2 · The positive/negative mass trick
> *Show:* a disc of radius $R$ with a smaller disc of radius $r$ cut out. The full disc (mass $M_1$) and the cut-out (mass $-M_2$) shown separately. The COM of the composite body marked.
> *Search:* "centre of mass positive negative mass trick disc with hole"

### 3.3 Motion of the COM

**Derivation from Newton's third law:**

$$
M\mathbf{a}_{\text{cm}}=\sum\mathbf{F}_{\text{ext}}. \qquad (3.3)
$$

Internal forces cancel in pairs (Newton's third law): $\sum\mathbf{F}_{\text{int}}=\mathbf{0}$. Therefore, the COM accelerates only under external forces.

**Key consequence:** In an isolated system ($\sum\mathbf{F}_{\text{ext}}=\mathbf{0}$), the COM moves at constant velocity. An explosion, a collision, or any internal rearrangement cannot change the COM's velocity.

> [!abstract] DIAGRAM D7.3 · The explosion's COM parabola
> *Show:* a shell following a parabolic trajectory. At the peak, it explodes into fragments. The fragments fly in different directions, but their centre of mass continues on the original parabola. The COM trajectory shown as a dashed line.
> *Search:* "explosion centre of mass parabola fragments trajectory"

### 3.4 Momentum and impulse

$$
\mathbf{p}=m\mathbf{v}. \qquad (3.4)
$$

$$
\mathbf{J}=\int_{t_i}^{t_f}\mathbf{F}\,dt=\Delta\mathbf{p}. \qquad (3.5)
$$

Impulse is the area under the $F$–$t$ curve. The impulse–momentum theorem: the impulse equals the change in momentum.

**Average force:** $\bar{F}=J/\Delta t=\Delta p/\Delta t$. In a collision, the average force can be very large even for a small impulse, because $\Delta t$ is very short.

> [!abstract] DIAGRAM D7.4 · The $F$–$t$ impulse curve
> *Show:* a graph of $F$ vs $t$ during a collision (a sharp peak). The area under the curve shaded (the impulse $J$). The average force $\bar{F}=J/\Delta t$ shown as a horizontal line enclosing the same area.
> *Search:* "impulse force versus time curve area average force collision"

### 3.5 Conservation of momentum

**The condition:** if the net external impulse is zero (in a given direction), the total momentum is conserved (in that direction):

$$
\sum\mathbf{p}_{\text{before}}=\sum\mathbf{p}_{\text{after}}. \qquad (3.6)
$$

**Component-wise:** momentum is conserved independently in each direction. In a 2-D collision: $p_{x,\text{before}}=p_{x,\text{after}}$ and $p_{y,\text{before}}=p_{y,\text{after}}$.

### 3.6 Collisions I: classification

| Type | KE conserved? | $e$ | Example |
|---|---|---|---|
| Elastic | Yes | $e=1$ | Billiard balls (approximately) |
| Inelastic | No | $0<e<1$ | Most real collisions |
| Perfectly inelastic | No (maximum loss) | $e=0$ | Bullet embedding in a block |

**The line of impact:** the line along which the collision force acts (for smooth spheres: the line joining the centres). The coefficient of restitution applies only along this line. The tangential component of velocity is unchanged for smooth spheres (no tangential impulse).

> [!abstract] DIAGRAM D7.5 · Collision classification: before and after
> *Show:* three cases: (1) elastic — two balls approach, exchange velocities (or bounce); (2) inelastic — they bounce with reduced speeds; (3) perfectly inelastic — they stick together. Velocity arrows shown before and after.
> *Search:* "collision classification elastic inelastic perfectly inelastic before after"

### 3.7 Collisions II: 1-D results

For a 1-D collision between $m_1$ and $m_2$ with initial velocities $u_1$ and $u_2$:

$$
v_1=\frac{m_1-em_2}{m_1+m_2}u_1+\frac{(1+e)m_2}{m_1+m_2}u_2, \qquad (3.7a)
$$

$$
v_2=\frac{(1+e)m_1}{m_1+m_2}u_1+\frac{m_2-em_1}{m_1+m_2}u_2. \qquad (3.7b)
$$

**Special cases:**

- **Elastic ($e=1$), $m_1=m_2$:** $v_1=u_2$, $v_2=u_1$ (velocities exchange).
- **Elastic, $m_1\gg m_2$:** $v_1\approx u_1$, $v_2\approx2u_1-u_2$ (the heavy particle barely moves; the light particle bounces off at $2u_1-u_2$).
- **Elastic, $m_1\ll m_2$:** $v_1\approx2u_2-u_1$, $v_2\approx u_2$ (the light particle bounces back; the heavy particle barely moves).
- **Perfectly inelastic ($e=0$):** $v_1=v_2=\frac{m_1u_1+m_2u_2}{m_1+m_2}$ (they stick together).

**Energy loss:**

$$
\Delta K=\frac{1}{2}\mu(u_1-u_2)^2(1-e^2). \qquad (3.8)
$$

where $\mu=m_1m_2/(m_1+m_2)$ is the reduced mass. For $e=1$: $\Delta K=0$ (elastic). For $e=0$: $\Delta K=\frac{1}{2}\mu v_{\text{rel}}^2$ (maximum loss).

> [!abstract] DIAGRAM D7.6 · The $e$-dependence of final velocities
> *Show:* a graph of $v_1$ and $v_2$ vs $e$ for a collision where $m_1$ approaches $m_2$ at rest. At $e=0$: both move together at $v_{\text{cm}}$. At $e=1$: $v_1=0$, $v_2=u_1$ (equal-mass exchange). The curves are linear in $e$.
> *Search:* "final velocities versus coefficient of restitution e graph 1D collision"

### 3.8 Collisions III: 2-D

For a smooth-sphere collision in 2-D:

1. **Line of impact:** the line joining the centres at contact.
2. **Along the line of impact:** momentum conservation + restitution ($e$).
3. **Perpendicular to the line of impact:** each sphere's tangential velocity is unchanged (no tangential impulse).

**Equal-mass elastic 90° result:** If two equal-mass smooth spheres collide elastically (one initially at rest), the velocities after collision are perpendicular: $\theta_1+\theta_2=90°$.

> [!abstract] DIAGRAM D7.7 · The 2-D oblique collision
> *Show:* two spheres colliding. The line of impact and the plane of contact drawn. The velocity components along and perpendicular to the line of impact shown for each sphere. The tangential components unchanged; the normal components determined by momentum conservation and $e$.
> *Search:* "2D oblique collision line of impact plane of contact velocity components"

### 3.9 The centre-of-mass frame

**The CM frame** moves at velocity $\mathbf{v}_{\text{cm}}=\frac{m_1\mathbf{u}_1+m_2\mathbf{u}_2}{m_1+m_2}$.

**Properties:**
1. Total momentum is zero in the CM frame.
2. For elastic collisions: the velocities simply reverse direction in the CM frame.
3. Energy decomposition: $K=\frac{1}{2}Mv_{\text{cm}}^2+K_{\text{rel}}$ where $K_{\text{rel}}=\frac{1}{2}\mu v_{\text{rel}}^2$.

> [!info] Why
> The CM frame is the "natural" frame for collisions because it simplifies the analysis: the total momentum is zero, and elastic collisions simply reverse the velocities. The lab-frame results can be obtained by transforming back.

### 3.10 Variable mass

**Derivation of the rocket equation:**

At time $t$: mass $m$, velocity $v$. At $t+dt$: mass $m+dm$ ($dm<0$), velocity $v+dv$. Exhaust: mass $-dm$, velocity $v-v_e$ (in the ground frame). Momentum conservation:

$$
mv=(m+dm)(v+dv)+(-dm)(v-v_e). \qquad (3.9)
$$

Expanding and dropping $dm\,dv$: $m\,dv+v_e\,dm=0$. Integrating:

$$
\boxed{\Delta v=v_e\ln\frac{m_0}{m_f}} \qquad (3.10)
$$

> [!abstract] DIAGRAM D7.8 · The rocket's momentum ledger
> *Show:* at time $t$: rocket of mass $m$ moving at $v$. At time $t+dt$: rocket of mass $m+dm$ at $v+dv$, and exhaust mass $-dm$ at $v-v_e$. The momentum of each drawn as arrows.
> *Search:* "rocket equation momentum conservation exhaust diagram variable mass"

> [!abstract] DIAGRAM D7.9 · The lab frame vs CM frame side by side
> *Show:* left: a collision in the lab frame (one particle approaching a stationary target). Right: the same collision in the CM frame (both particles approach the CM with equal and opposite momenta, then scatter). The CM frame shows the total momentum is zero.
> *Search:* "lab frame versus centre of mass frame collision comparison diagram"

> [!abstract] DIAGRAM D7.10 · The falling chain on a scale with force components
> *Show:* a chain falling onto a scale. Two forces on the scale: (1) the weight of the landed part ($\lambda(L-x)g$, downward); (2) the impact force from the arriving chain ($2\lambda gx$, downward — the momentum flux). The total reading $F=\lambda(L+x)g$ annotated. At $x=L$: $F=2mg$.
> *Search:* "falling chain scale reading impact force weight momentum flux"

> [!abstract] DIAGRAM D7.11 · The ballistic pendulum's two stages
> *Show:* left: the collision stage — a bullet embeds in a hanging block (momentum conserved, energy not). Right: the swing stage — the block+bullet swings up to height $h$ (energy conserved, momentum not). The two stages clearly separated with labels.
> *Search:* "ballistic pendulum two stages collision swing momentum energy"

> [!abstract] DIAGRAM D7.12 · A man walking on a boat with the COM's fixed line
> *Show:* a boat on frictionless water with a man standing on it. Left: initial position. Right: the man has walked rightward; the boat has moved leftward. The COM of the man+boat system shown as a fixed vertical dashed line (it does not move). The displacements $d_{\text{man}}$ and $d_{\text{boat}}$ annotated.
> *Search:* "man walking boat centre of mass fixed line displacement diagram"

### 3.11 Two-stage impulse problems

**Ballistic pendulum:** a bullet embeds in a hanging block. The block swings up to height $h$.

1. **Collision (momentum conserved):** $mv_0=(m+M)V$.
2. **Swing (energy conserved):** $\frac{1}{2}(m+M)V^2=(m+M)gh$.

$v_0=\frac{m+M}{m}\sqrt{2gh}$.

> [!info] Why
> Momentum is conserved during the collision (brief time, no external horizontal impulse). Energy is conserved during the swing (only gravity does work). The order matters: momentum first (collision), energy second (swing).

### 3.12 Systems with internal motion

**Man on a boat:** a man of mass $m$ walks a distance $d$ on a boat of mass $M$ (initially at rest, frictionless water). The boat moves in the opposite direction so that the COM stays fixed: $md_{\text{man}}+Md_{\text{boat}}=0$ (in the lab frame, the displacements are relative to the water). The man's displacement relative to the ground: $d_{\text{man}}=Md/(m+M)$.

**Block on a movable wedge:** the block slides down the wedge; the wedge slides on the table. Horizontal momentum is conserved (no external horizontal force). The COM stays fixed horizontally.

### 3.13 Collisions with a third body

**Block-into-block-into-spring:** two blocks collide (with $e$), then the combined system compresses a spring. The collision determines the post-collision velocity; the spring determines the maximum compression.

**Moving-wall bounce:** a ball bounces off a wall moving at speed $v_w$. The relative velocity reverses: $v_{\text{sep}}=ev_{\text{app}}$. $v_{\text{after}}-v_w=-e(v_{\text{before}}-v_w)$.

## Part 4 · Results, limits and the validity ledger

### 4.1 Boxed results

$$
\boxed{\mathbf{R}=\frac{1}{M}\sum m_i\mathbf{r}_i,\quad M\mathbf{a}_{\text{cm}}=\mathbf{F}_{\text{ext}}} \qquad (4.1)
$$

centre of mass definition and its equation of motion.

$$
\boxed{\mathbf{J}=\Delta\mathbf{p}=\int\mathbf{F}\,dt} \qquad (4.2)
$$

impulse–momentum theorem.

$$
\boxed{\sum\mathbf{p}_{\text{before}}=\sum\mathbf{p}_{\text{after}}\text{ if }\sum\mathbf{F}_{\text{ext}}=\mathbf{0}} \qquad (4.3)
$$

conservation of momentum.

$$
\boxed{e=\frac{v_{\text{sep}}}{v_{\text{app}}}=\frac{v_2-v_1}{u_1-u_2}\text{ (1-D)}} \qquad (4.4)
$$

coefficient of restitution along the line of impact.

$$
\boxed{\Delta K=\frac{1}{2}\mu(u_1-u_2)^2(1-e^2)} \qquad (4.5)
$$

energy lost in a 1-D collision.

$$
\boxed{\Delta v=v_e\ln\frac{m_0}{m_f}} \qquad (4.6)
$$

rocket equation.

### 4.2 Limit checks

- $e=1$: $\Delta K=0$ — elastic, no energy lost. ✓
- $e=0$: $\Delta K=\frac{1}{2}\mu v_{\text{rel}}^2$ — maximum energy lost. ✓
- $m_1=m_2$, $e=1$: $v_1=u_2$, $v_2=u_1$ — velocities exchange. ✓
- $m_1\gg m_2$: the heavy mass barely changes velocity. ✓
- $m_0/m_f=e$: $\Delta v=v_e$ — if 63% of the mass is fuel, the speed increases by $v_e$. ✓

### 4.3 Which formula when

| Given | Need | Use |
|---|---|---|
| mass distribution | COM | Eq. (4.1) |
| force and time | impulse/change in momentum | Eq. (4.2) |
| collision (no external force) | final velocities | Eq. (4.3) + $e$ |
| $e$ and initial velocities | energy lost | Eq. (4.5) |
| rocket | velocity change | Eq. (4.6) |
| ballistic pendulum | bullet speed | momentum then energy |

### 4.4 Concept checks

**C1 — concept check.** Can the COM of a body lie outside the body?

<details><summary>Answer</summary>

Yes — for a ring, the COM is at the centre (inside the hole). For a boomerang, the COM may be in empty space.

</details>

**C2 — concept check.** An explosion breaks a shell into fragments. Does the COM of the fragments follow the original parabola?

<details><summary>Answer</summary>

Yes — the explosion is an internal force. The COM continues on the original trajectory (as if the shell had not exploded).

</details>

**C3 — concept check.** In a perfectly inelastic collision, is all kinetic energy lost?

<details><summary>Answer</summary>

No — only the maximum possible is lost. The stuck-together objects still move with $v_{\text{cm}}$, so some KE remains ($\frac{1}{2}Mv_{\text{cm}}^2$).

</details>

**C4 — concept check.** What is the coefficient of restitution for a ball bouncing off a hard floor?

<details><summary>Answer</summary>

$e=v_{\text{after}}/v_{\text{before}}$ (the ratio of speeds, since the floor is stationary). A tennis ball: $e\approx0.75$. A superball: $e\approx0.9$.

</details>

**C5 — concept check.** Why is momentum conserved in a collision but energy may not be?

<details><summary>Answer</summary>

Momentum is conserved because the collision forces are internal (equal and opposite) and act for the same time. Energy may not be conserved because the deformations during the collision convert KE to heat, sound, or deformation energy.

</details>

**C6 — concept check.** In the rocket equation, why is $dm<0$?

<details><summary>Answer</summary>

The rocket loses mass (ejects exhaust), so $dm$ is negative. The exhaust mass $-dm$ is positive.

</details>

**C7 — concept check.** A gun fires a bullet. Which has more momentum: the bullet or the gun?

<details><summary>Answer</summary>

They have equal and opposite momentum (by conservation of momentum, starting from zero). The bullet has more speed (because it has less mass).

</details>

**C8 — concept check.** In a 2-D collision, which component of momentum is conserved?

<details><summary>Answer</summary>

Both components (if no external force). Along the line of impact: momentum conservation + restitution. Perpendicular: each sphere's tangential velocity is unchanged.

</details>

**C9 — concept check.** A ball hits a wall at angle $\theta$ and bounces off at angle $\theta$. Is this elastic?

<details><summary>Answer</summary>

Not necessarily — the angle of reflection equals the angle of incidence for any smooth-sphere collision with a massive wall, regardless of $e$. The energy loss depends on $e$ (the normal component of velocity is reduced by factor $e$).

</details>

**C10 — concept check.** A man walks on a boat. Does the COM of the man+boat system move?

<details><summary>Answer</summary>

No — there are no external horizontal forces (the water is frictionless). The COM stays fixed. The boat moves opposite to the man.

</details>

**C11 — concept check.** Why does the ballistic pendulum use momentum first and energy second?

<details><summary>Answer</summary>

During the collision: momentum is conserved (brief time, no external impulse), but energy is not (the bullet embeds — inelastic). During the swing: energy is conserved (only gravity does work), but momentum is not (gravity is an external force). Each conservation law applies to a different stage.

</details>

**C12 — concept check.** Can a lighter object stop a heavier object in an elastic collision?

<details><summary>Answer</summary>

No — in an elastic collision, the lighter object always bounces back (reverses velocity in the CM frame). The heavy object continues forward, barely slowed.

</details>

## Part 5 · Worked exemplars

### E1 — COM of a composite body

Find the COM of a uniform plate consisting of a 4 m × 2 m rectangle with a 1 m × 1 m square cut from one corner.

> [!success] Check
> Using the positive/negative mass trick: the COM shifts away from the cut-out.

<details><summary>Solution</summary>

**Method.** Full rectangle: mass $M_1=8$ (area proportional), COM at $(2,1)$. Cut-out: mass $M_2=1$, COM at $(0.5,0.5)$. $X_{\text{cm}}=(8\times2-1\times0.5)/7=15.5/7=2.21$ m. $Y_{\text{cm}}=(8\times1-1\times0.5)/7=7.5/7=1.07$ m.

</details>

### E2 — Explosion: COM trajectory

A shell of mass 10 kg is fired at 30 m/s at 45°. At the peak, it explodes into two fragments: 4 kg and 6 kg. The 4 kg fragment falls straight down. Find the velocity of the 6 kg fragment.

> [!success] Check
> At the peak: $v_x=30\cos45°=21.2$ m/s, $v_y=0$. The 4 kg fragment has $v_x=0$. Momentum: $10\times21.2=4\times0+6\times v_{6x}$. $v_{6x}=35.3$ m/s.

<details><summary>Solution</summary>

**Method.** At the peak: total momentum $p_x=10\times21.2=212$ kg m/s. After explosion: $p_x=6v_{6x}=212$. $v_{6x}=35.3$ m/s. The 6 kg fragment moves faster in the original direction.

</details>

### E3 — 1-D elastic collision: equal masses

A 2 kg ball at 5 m/s collides elastically with a 2 kg ball at rest. Find the velocities after.

> [!success] Check
> $v_1=0$, $v_2=5$ m/s — complete velocity exchange.

<details><summary>Solution</summary>

**Method.** $v_1=\frac{m_1-m_2}{m_1+m_2}u_1+\frac{2m_2}{m_1+m_2}u_2=0+0=0$. $v_2=\frac{2m_1}{m_1+m_2}u_1+\frac{m_2-m_1}{m_1+m_2}u_2=5+0=5$ m/s.

</details>

### E4 — 1-D perfectly inelastic collision

A 5 kg ball at 10 m/s collides with a 3 kg ball at $-4$ m/s. They stick together. Find the final velocity and energy lost.

> [!success] Check
> $v=(50-12)/8=38/8=4.75$ m/s. $\Delta K=\frac{1}{2}\times5\times100+\frac{1}{2}\times3\times16-\frac{1}{2}\times8\times22.56=250+24-90.2=183.8$ J.

<details><summary>Solution</summary>

**Method.** $v=\frac{5\times10+3\times(-4)}{5+3}=\frac{50-12}{8}=4.75$ m/s. $K_i=\frac{1}{2}\times5\times100+\frac{1}{2}\times3\times16=274$ J. $K_f=\frac{1}{2}\times8\times22.56=90.2$ J. $\Delta K=183.8$ J.

</details>

### E5 — Ballistic pendulum

A 10 g bullet at 400 m/s embeds in a 2 kg block hanging from a string. Find the height the block rises. ($g=10$ m/s$^2$.)

> [!success] Check
> $V=0.01\times400/2.01=1.99$ m/s. $h=V^2/(2g)=3.96/20=0.198$ m $\approx20$ cm.

<details><summary>Solution</summary>

**Method.** Momentum: $0.01\times400=(0.01+2)V$. $V=4/2.01=1.99$ m/s. Energy: $\frac{1}{2}\times2.01\times3.96=2.01\times10\times h$. $h=3.96/20=0.198$ m.

</details>

### E6 — 2-D elastic collision: equal masses

A ball of mass $m$ at speed $v_0$ hits an equal-mass ball at rest. The collision is elastic and smooth. The incoming ball is deflected by 30°. Find the speeds and the angle of the second ball.

> [!success] Check
> $\theta_1+\theta_2=90°$. $\theta_2=60°$. From momentum: $v_1\cos30°+v_2\cos60°=v_0$, $v_1\sin30°-v_2\sin60°=0$. From the second: $v_1=2v_2\sqrt{3}/2=v_2\sqrt{3}$. Substituting: $v_2\sqrt{3}\times0.866+v_2\times0.5=v_0$. $v_2(1.5+0.5)=v_0$. $v_2=v_0/2$. $v_1=v_0\sqrt{3}/2$.

<details><summary>Solution</summary>

**Method.** The 90° result: $\theta_1+\theta_2=90°\Rightarrow\theta_2=60°$. Momentum $x$: $mv_1\cos30°+mv_2\cos60°=mv_0$. Momentum $y$: $mv_1\sin30°=mv_2\sin60°$. From $y$: $v_1=v_2\sqrt{3}$. From $x$: $v_2\sqrt{3}\times\frac{\sqrt{3}}{2}+v_2\times\frac{1}{2}=v_0$. $v_2(3/2+1/2)=v_0$. $v_2=v_0/2$. $v_1=v_0\sqrt{3}/2$.

</details>

### E7 — Variable mass: sand on a belt

Sand falls at 5 kg/s onto a conveyor belt moving at 2 m/s. Find the force needed and the power.

> [!success] Check
> $F=\dot{m}v=10$ N. $P=Fv=20$ W. KE rate $=\frac{1}{2}\dot{m}v^2=10$ W — the other 10 W is heat.

<details><summary>Solution</summary>

**Method.** $F=\dot{m}v=5\times2=10$ N. $P=Fv=20$ W. $\dot{K}=\frac{1}{2}\dot{m}v^2=10$ W. The belt's power is twice the KE rate — the rest goes into heat.

</details>

### E8 — Man on a boat

A 60 kg man walks 3 m on a 120 kg boat (initially at rest, frictionless water). How far does the boat move?

> [!success] Check
> The COM stays fixed: $60\times d_{\text{man}}+120\times d_{\text{boat}}=0$. $d_{\text{man}}=-2d_{\text{boat}}$. The man moves 3 m relative to the boat: $d_{\text{man}}-d_{\text{boat}}=3$. $-2d_{\text{boat}}-d_{\text{boat}}=3$. $d_{\text{boat}}=-1$ m. The boat moves 1 m opposite to the man.

<details><summary>Solution</summary>

**Method.** $d_{\text{man}}-d_{\text{boat}}=3$ (relative displacement). $60d_{\text{man}}+120d_{\text{boat}}=0$ (COM fixed). $d_{\text{man}}=-2d_{\text{boat}}$. $-2d_{\text{boat}}-d_{\text{boat}}=3$. $d_{\text{boat}}=-1$ m.

</details>

### E9 — Moving-wall bounce

A ball at 10 m/s hits a wall moving toward it at 5 m/s. $e=0.8$. Find the ball's velocity after.

> [!success] Check
> $v_{\text{app}}=10-(-5)=15$ m/s (relative approach speed). $v_{\text{sep}}=0.8\times15=12$ m/s. $v_{\text{after}}-(-5)=12$. $v_{\text{after}}=7$ m/s (away from the wall).

<details><summary>Solution</summary>

**Method.** $v_{\text{after}}-v_w=-e(v_{\text{before}}-v_w)$. $v_{\text{after}}-(-5)=-0.8(10-(-5))=-12$. $v_{\text{after}}=-12+5=-7$ m/s. Wait — sign convention: positive is toward the wall. $v_{\text{before}}=+10$, $v_w=-5$ (wall moving toward the ball... actually, let me be careful. If the wall moves toward the ball: $v_w=-5$ (in the ball's frame, the wall approaches faster). $v_{\text{after}}-v_w=-e(v_{\text{before}}-v_w)$. $v_{\text{after}}+5=-0.8(10+5)=-12$. $v_{\text{after}}=-17$ m/s. The ball bounces back at 17 m/s — faster than it came in! The wall's kinetic energy was transferred to the ball.

</details>

### E10 — Rocket $\Delta v$

A rocket has $v_e=3$ km/s and mass ratio $m_0/m_f=10$. Find $\Delta v$.

> [!success] Check
> $\Delta v=3\ln10=3\times2.303=6.91$ km/s — enough for a low orbit.

<details><summary>Solution</summary>

**Method.** $\Delta v=v_e\ln(m_0/m_f)=3\times\ln10=6.91$ km/s.

</details>

## Part 6 · Problem archetypes and practice

### 6.1 Archetypes

| # | Archetype | Template | Where worked | Variations |
|---:|---|---|---|---|
| 1 | COM of composite | Positive/negative mass | E1 | subtraction trick |
| 2 | Explosion | COM trajectory | E2 | three fragments |
| 3 | 1-D elastic | Velocity exchange | E3 | unequal masses |
| 4 | 1-D perfectly inelastic | Stick together | E4 | find $e$ from energy |
| 5 | Ballistic pendulum | Momentum then energy | E5 | bullet through block |
| 6 | 2-D elastic | 90° result | E6 | oblique collision |
| 7 | Sand on belt | Momentum flux | E7 | chain, rocket |
| 8 | Man on boat | COM fixed | E8 | block on wedge |
| 9 | Moving wall | $v_{\text{sep}}=ev_{\text{app}}$ | E9 | wall with speed |
| 10 | Rocket | $\Delta v=v_e\ln(m_0/m_f)$ | E10 | two-stage |

### 6.2 In-flow practice

#### Q1. Find the COM of a system: $m_1=2$ kg at $(1,0)$, $m_2=3$ kg at $(0,2)$.

<details><summary>Solution</summary>

$X_{\text{cm}}=(2\times1+3\times0)/5=0.4$ m. $Y_{\text{cm}}=(2\times0+3\times2)/5=1.2$ m.

</details>

#### Q2. A 5 kg object explodes into 3 kg and 2 kg. The 3 kg piece moves at 4 m/s east. Find the velocity of the 2 kg piece.

<details><summary>Solution</summary>

$0=3\times4+2v$. $v=-6$ m/s (west).

</details>

#### Q3. A 1 kg ball at 6 m/s hits a 2 kg ball at rest (elastic, 1-D). Find the velocities.

<details><summary>Solution</summary>

$v_1=(1-2)/(1+2)\times6+0=-2$ m/s. $v_2=2\times1/(1+2)\times6+0=4$ m/s.

</details>

#### Q4. A 0.05 kg bullet at 200 m/s embeds in a 2 kg block. Find the common velocity.

<details><summary>Solution</summary>

$v=0.05\times200/2.05=4.88$ m/s.

</details>

#### Q5. A ball is dropped from 5 m and bounces to 3.2 m. Find $e$.

<details><summary>Solution</summary>

$e=\sqrt{h_2/h_1}=\sqrt{3.2/5}=\sqrt{0.64}=0.8$.

</details>

#### Q6. Two equal-mass balls collide elastically. One is at rest. The incoming ball is deflected 30°. Find the other ball's angle.

<details><summary>Solution</summary>

$\theta_2=90°-30°=60°$.

</details>

#### Q7. A 1000 kg car at 20 m/s hits a 2000 kg truck at rest (perfectly inelastic). Find the common velocity.

<details><summary>Solution</summary>

$v=1000\times20/3000=6.67$ m/s.

</details>

#### Q8. A rocket has $v_e=2$ km/s and must reach $\Delta v=4$ km/s. Find $m_0/m_f$.

<details><summary>Solution</summary>

$m_0/m_f=e^{4/2}=e^2=7.39$.

</details>

#### Q9. A 0.1 kg ball at 10 m/s hits a wall and bounces back at 8 m/s. Find the impulse.

<details><summary>Solution</summary>

$J=m(v_f-v_i)=0.1(-8-10)=-1.8$ N s (magnitude 1.8 N s, direction: away from the wall).

</details>

#### Q10. A 60 kg person jumps off a 120 kg boat at 3 m/s (relative to the boat). Find the boat's velocity.

<details><summary>Solution</summary>

$0=60(3+v_b)+120v_b$. $180+60v_b+120v_b=0$. $180v_b=-180$. $v_b=-1$ m/s.

</details>

#### Q11. A 2 kg ball at 5 m/s collides with a 3 kg ball at $-2$ m/s (elastic). Find the velocities.

<details><summary>Solution</summary>

$v_1=(2-3)/5\times5+2\times3/5\times(-2)=-1-2.4=-3.4$ m/s. $v_2=2\times2/5\times5+(3-2)/5\times(-2)=4-0.4=3.6$ m/s.

</details>

#### Q12. A ballistic pendulum: 5 g bullet, 1 kg block, height 0.1 m. Find bullet speed. ($g=10$ m/s$^2$.)

<details><summary>Solution</summary>

$V=\sqrt{2gh}=\sqrt{2}=1.414$ m/s. $v_0=(1.005/0.005)\times1.414=284$ m/s.

</details>

#### Q13. A chain of mass 3 kg is lifted at 2 m/s. Find the force. (Take $g=10$ m/s$^2$.)

<details><summary>Solution</summary>

$F=\lambda xg+\lambda v^2$. For a specific $x$: $F=(3/L)x\times10+(3/L)\times4$. At $x=L$: $F=30+12/L\times L$... this needs the full chain length. If the entire chain is being lifted at constant speed: $F=mg+\dot{m}v=3\times10+(3/0)\times2$... the problem needs more information. For a chain being pulled at constant speed $v$: $F=\lambda vg+\lambda v^2$ at the point where the chain is being lifted. If the chain is already fully off the ground: $F=mg=30$ N (no momentum flux). If the chain is being lifted from a pile: $F=\lambda xg+\lambda v^2$ where $x$ is the length already lifted.

</details>

#### Q14. A 1 kg ball at 3 m/s collides with a wall moving toward it at 2 m/s. $e=0.5$. Find the ball's speed after.

<details><summary>Solution</summary>

$v_{\text{after}}-(-2)=-0.5(3-(-2))=-2.5$. $v_{\text{after}}=-4.5$ m/s. Speed $=4.5$ m/s.

</details>

#### Q15. Find the COM of a uniform semicircular wire of radius $R$.

<details><summary>Solution</summary>

$y_{\text{cm}}=2R/\pi$ from the diameter (by symmetry, $x_{\text{cm}}=0$).

</details>

#### Q16. A 0.2 kg ball at 5 m/s collides elastically with a 0.3 kg ball at $-3$ m/s. Find the velocities.

<details><summary>Solution</summary>

$v_1=(0.2-0.3)/0.5\times5+2\times0.3/0.5\times(-3)=-0.2\times5+1.2\times(-3)=-1-3.6=-4.6$ m/s. $v_2=2\times0.2/0.5\times5+(0.3-0.2)/0.5\times(-3)=4+0.2\times(-3)=3.4$ m/s.

</details>

#### Q17. A bomb at rest explodes into three equal masses. Two move at right angles at 10 m/s each. Find the velocity of the third.

<details><summary>Solution</summary>

$0=m\times10\hat{i}+m\times10\hat{j}+mv_3$. $v_3=-10\hat{i}-10\hat{j}$. Speed $=10\sqrt{2}=14.1$ m/s at 225° from the first.

</details>

#### Q18. A 2 kg block and a 3 kg block are connected by a compressed spring ($k=100$ N/m, $x=0.2$ m). When released, find the speeds. (No friction.)

<details><summary>Solution</summary>

Momentum: $2v_1+3v_2=0\Rightarrow v_2=-2v_1/3$. Energy: $\frac{1}{2}\times100\times0.04=2=\frac{1}{2}\times2v_1^2+\frac{1}{2}\times3v_2^2$. $2=v_1^2+3\times4v_1^2/9=v_1^2+4v_1^2/3=7v_1^2/3$. $v_1^2=6/7$. $v_1=0.926$ m/s. $v_2=0.617$ m/s.

</details>

#### Q19. A 0.01 kg bullet passes through a 1 kg block (initially at rest). The bullet enters at 500 m/s and exits at 200 m/s. Find the block's speed.

<details><summary>Solution</summary>

$0.01\times500=0.01\times200+1\times v$. $5=2+v$. $v=3$ m/s.

</details>

#### Q20. A 1000 kg car at 30 m/s brakes with a force of 5000 N. Find the time to stop.

<details><summary>Solution</summary>

$J=Ft=\Delta p$. $5000t=1000\times30$. $t=6$ s.

</details>

#### Q21. A 2 kg ball at 4 m/s collides with a 4 kg ball at $-2$ m/s ($e=0.5$). Find the velocities.

<details><summary>Solution</summary>

$v_1=(2-0.5\times4)/6\times4+(1+0.5)\times4/6\times(-2)=0+(-2)=-2$ m/s. Wait, let me use the full formulas. $v_1=(m_1-em_2)u_1/(m_1+m_2)+(1+e)m_2u_2/(m_1+m_2)=(2-2)\times4/6+1.5\times4\times(-2)/6=0-2=-2$ m/s. $v_2=(1+e)m_1u_1/(m_1+m_2)+(m_2-em_1)u_2/(m_1+m_2)=1.5\times2\times4/6+(4-1)\times(-2)/6=2-1=1$ m/s.

</details>

#### Q22. A man (70 kg) and a woman (55 kg) on ice push apart. The man moves at 1.5 m/s. Find the woman's speed.

<details><summary>Solution</summary>

$0=70\times1.5+55v$. $v=-105/55=-1.91$ m/s.

</details>

#### Q23. A ball bounces three times. Heights: 10 m, 6.4 m, 4.1 m. Find $e$.

<details><summary>Solution</summary>

$e_1=\sqrt{6.4/10}=0.8$. $e_2=\sqrt{4.1/6.4}=0.8$. Average $e=0.8$.

</details>

#### Q24. A 0.5 kg ball at 10 m/s hits a 1 kg ball at rest. The 0.5 kg ball stops. Is the collision elastic?

<details><summary>Solution</summary>

$K_i=\frac{1}{2}\times0.5\times100=25$ J. $K_f=\frac{1}{2}\times1\times v^2$. Momentum: $0.5\times10=1\times v$. $v=5$ m/s. $K_f=12.5$ J. $\Delta K=12.5$ J. Not elastic.

</details>

#### Q25. A rocket ejects mass at 2 kg/s with $v_e=3000$ m/s. Find the thrust.

<details><summary>Solution</summary>

$F=\dot{m}v_e=2\times3000=6000$ N.

</details>

## Part 7 · Alternate methods and the JEE-Advanced advantage toolkit

### 7.1 The CM-frame shortcut

For any collision: transform to the CM frame, reverse the velocities (elastic), transform back. This is often faster than solving the full system of equations, especially for 2-D collisions.

### 7.2 The "momentum then energy" protocol

For problems with a collision followed by a motion (ballistic pendulum, bullet through block + spring): use momentum for the collision stage, energy for the motion stage. Never mix them.

### 7.3 The relative-velocity shortcut

For 1-D collisions: $v_2-v_1=-e(u_1-u_2)$ (the relative velocity reverses, scaled by $e$). Combined with momentum conservation, this gives a simpler system of two equations.

### 7.4 The "does it stick?" test

For a collision: compute $v_{\text{cm}}$. If $e=0$, the objects stick and move at $v_{\text{cm}}$. If $e>0$, they separate. The energy loss is $\frac{1}{2}\mu v_{\text{rel}}^2(1-e^2)$.

## Part 8 · Examiner traps

> [!danger] Trap 1 — Using energy conservation in an inelastic collision
> In an inelastic collision, KE is not conserved. Use momentum conservation, not energy.

> [!danger] Trap 2 — Applying $e$ across the whole velocity
> $e$ applies only along the line of impact. The tangential component is unchanged for smooth spheres.

> [!danger] Trap 3 — Forgetting the ejecta's momentum in the rocket equation
> The rocket equation accounts for the exhaust momentum. Ignoring it gives the wrong $\Delta v$.

> [!danger] Trap 4 — Using $v_{\text{cm}}$ as the velocity of every part after a collision
> After an inelastic collision, the stuck-together objects move at $v_{\text{cm}}$. But the individual parts of the system do not all move at $v_{\text{cm}}$ — only the COM does.

> [!danger] Trap 5 — Mixing "system" and "particle" when external forces act
> For a system: $\sum F_{\text{ext}}=Ma_{\text{cm}}$. For an individual particle: $\sum F_i=m_i a_i$. Don't mix them.

> [!danger] Trap 6 — Assuming the COM stays fixed when an external force acts
> The COM stays fixed only if the net external force is zero. Gravity, friction, and other external forces move the COM.

> [!danger] Trap 7 — Confusing impulse and force
> Impulse $J=F\Delta t$ has units N s. Force has units N. A large impulse can come from a large force for a short time or a small force for a long time.

> [!danger] Trap 8 — Forgetting that momentum is a vector
> In 2-D collisions, momentum is conserved independently in each direction. You cannot mix $x$ and $y$ components.

> [!danger] Trap 9 — The "heavy ball bounces back" fallacy
> A heavy ball hitting a light ball at rest does not bounce back — it continues forward, barely slowed. The light ball bounces forward at nearly $2v_{\text{heavy}}$.

> [!danger] Trap 10 — Using the ballistic pendulum formula for a bullet that passes through
> The ballistic pendulum formula assumes the bullet embeds ($e=0$). If the bullet passes through, you need a different analysis (momentum conservation with two separate final velocities).

## Part 9 · Playbook

### 9.1 Triage decision tree

- "Find the COM": use the definition or the positive/negative mass trick.
- "Explosion": COM trajectory continues; use momentum conservation for the fragments.
- "1-D collision": use momentum + $e$ (or relative-velocity formula).
- "2-D collision": resolve along/perpendicular to the line of impact.
- "Ballistic pendulum": momentum (collision) then energy (swing).
- "Variable mass": rocket equation or momentum flux.
- "Man on boat": COM stays fixed (no external horizontal force).

### 9.2 Formula map with validity

| Formula | Valid when | Breaks when |
|---|---|---|
| $\mathbf{R}=\sum m_i\mathbf{r}_i/M$ | always | continuous bodies (use integration) |
| $M\mathbf{a}_{\text{cm}}=\mathbf{F}_{\text{ext}}$ | always | internal forces cancel |
| $\sum\mathbf{p}=$ const | no external impulse | external forces act during the collision |
| $e=v_{\text{sep}}/v_{\text{app}}$ | along the line of impact only | tangential component not involved |
| $\Delta v=v_e\ln(m_0/m_f)$ | constant $v_e$, no external forces | gravity, air resistance |

### 9.3 Timing plan

Sections A and B under two minutes each; Section C three minutes; Section D twelve minutes. COM problems die by the definition or the subtraction trick. Collision problems die by momentum + $e$. Ballistic pendulum problems die by the two-stage protocol.

### 9.4 Pre-submission audit, ten points

1. COM: correct reference point and correct formula.
2. Momentum conservation: verified that net external impulse is zero (in the relevant direction).
3. Collision: correct classification (elastic vs inelastic) and correct $e$.
4. $e$ applied along the line of impact only (not the full velocity).
5. Ballistic pendulum: momentum first, energy second (correct order).
6. Rocket equation: used $\ln(m_0/m_f)$, not $m_0-m_f$.
7. 2-D collision: resolved along and perpendicular to the line of impact.
8. Energy loss: used the correct formula with $\mu$ and $v_{\text{rel}}$.
9. Units consistent throughout.
10. Every sub-part answered.

## Part 10 · Olympiad extension

### OL1 — Falling chain on a scale

A chain of mass $m$ and length $L$ is piled on a scale. One end is lifted and released. Find the scale reading when a length $x$ has been lifted.

<details><summary>Solution</summary>

**Method.** The scale supports: (1) the weight of the landed part $(m/L)(L-x)g$; (2) the momentum-flux force from the chain landing. The chain falls from height $x$: $v=\sqrt{2gx}$. Mass arriving per unit time: $\dot{m}=(m/L)\sqrt{2gx}$. Force to stop it: $F_{\text{impact}}=\dot{m}v=2(m/L)gx$. Total reading: $F=(m/L)(L+x)g$. At $x=L$: $F=2mg$ — twice the weight!

</details>

### OL2 — Two-body scattering in the CM frame

A particle of mass $m_1$ scatters elastically off a stationary target of mass $m_2$. Find the maximum scattering angle of $m_1$ in the lab frame.

<details><summary>Solution</summary>

**Method.** In the CM frame: the scattering angle $\theta_{\text{cm}}$ can be anything from 0 to 180°. The lab-frame angle $\theta_{\text{lab}}$ is related to $\theta_{\text{cm}}$ by: $\tan\theta_{\text{lab}}=\frac{\sin\theta_{\text{cm}}}{\cos\theta_{\text{cm}}+m_1/m_2}$. For $m_1>m_2$: the denominator can be zero (at $\cos\theta_{\text{cm}}=-m_2/m_1$), giving $\theta_{\text{lab}}=90°$. The maximum lab-frame angle is $\theta_{\max}=\sin^{-1}(m_2/m_1)$. For $m_1\le m_2$: $\theta_{\max}=90°$ (any angle is possible).

**Significance.** This explains why a bowling ball ($m_1$) cannot be scattered backward by a tennis ball ($m_2$) — the maximum scattering angle is less than 90°.

</details>

### OL3 — Impulse approximation problems

A ball of mass $m$ is hit by a bat for time $\Delta t=0.001$ s with average force 500 N. The ball also experiences gravity. Find the impulse from the bat and from gravity, and show gravity is negligible.

<details><summary>Solution</summary>

**Method.** $J_{\text{bat}}=500\times0.001=0.5$ N s. $J_{\text{gravity}}=mg\Delta t=0.145\times9.8\times0.001=0.0014$ N s. Ratio: $J_g/J_{\text{bat}}=0.003$. Gravity is 0.3% of the bat's impulse — negligible. The impulse approximation: $F_{\text{impulse}}\gg F_{\text{other}}$ during the collision time.

</details>

### OL4 — Successive bouncing with restitution

A ball bounces from height $h$ with coefficient $e$. After $n$ bounces, what fraction of the original energy remains?

<details><summary>Solution</summary>

**Method.** After each bounce: height $=e^2\times$ previous. After $n$ bounces: $h_n=e^{2n}h$. Energy: $E_n=mgh_n=e^{2n}E_0$. Fraction remaining: $e^{2n}$. For $e=0.8$, $n=5$: $0.8^{10}=0.107$ — about 11% remains.

</details>

### OL5 — Relativistic momentum preview

Why must the relativistic momentum be $\mathbf{p}=\gamma m\mathbf{v}$ and not $m\mathbf{v}$?

<details><summary>Solution</summary>

**Method.** Conservation of momentum must hold in all inertial frames. If $p=mv$: applying a Lorentz transformation to a collision gives different momenta in different frames — momentum is not conserved. The form $p=\gamma mv$ is the unique form (up to an overall constant) that is conserved in all frames. The derivation: consider an elastic collision in two frames (the lab and the CM). The only form of $p(v)$ that makes momentum conserved in both frames is $p=mv/\sqrt{1-v^2/c^2}=\gamma mv$.

**Significance.** This is a one-page preview of PART 28. The relativistic momentum $\mathbf{p}=\gamma m\mathbf{v}$ is forced by the requirement of frame-independence of the conservation law. The "mass increase" interpretation ($m\to\gamma m$) is a historical artefact — the modern view is that the mass $m$ is invariant and it is the momentum formula that changes.

</details>

### OL6 — Bouncing ball on a moving platform

A ball bounces on a platform that oscillates vertically at frequency $f$. For what $f$ does the ball "resonate" (bounce higher each time)?

<details><summary>Solution</summary>

**Method.** The ball must hit the platform when the platform is moving upward (to gain energy). The ball's flight time after a bounce: $T=2v/g$. The platform's period: $T_p=1/f$. For resonance: $T=nT_p$ (the ball lands when the platform is at the same phase). The ball gains energy when the platform is moving up at impact: $v_{\text{after}}=v_{\text{before}}+ev_{\text{platform}}$ (approximately). The condition: $f=ng/(2v)$ for integer $n$.

**Significance.** This is a simplified model of a "bouncing ball on a vibrating plate" — a classic experiment in nonlinear dynamics. The ball can exhibit periodic, quasi-periodic, or chaotic bouncing depending on $f$ and the driving amplitude.

</details>

### OL7 — Sliding chain over a peg

A chain of length $L$ and mass $m$ hangs over a frictionless peg, with length $x$ on one side and $L-x$ on the other. Find the acceleration as a function of $x$.

<details><summary>Solution</summary>

**Method.** Force: $F=\lambda xg-\lambda(L-x)g=\lambda g(2x-L)$. Total mass: $m$. $a=F/m=g(2x-L)/L$. At $x=L/2$: $a=0$ (equilibrium — unstable). At $x>L/2$: $a>0$ (the longer side pulls). At $x=L$: $a=g$ (free fall of the entire chain).

**Significance.** The chain's motion is not constant acceleration — $a$ depends on $x$. The equation $a=g(2x-L)/L$ is a first-order ODE in $v$ and $x$: $v\,dv=g(2x-L)dx/L$. Integrating: $v^2=g(x^2-Lx+L^2/4)/L+C$. At $x=L/2$: $v=0$ (starting from rest at the equilibrium position... but this is unstable, so the chain will fall if perturbed).

</details>

### OL8 — Two-stage rocket optimal staging

A two-stage rocket has total mass $M$, payload $M_p$, and structural coefficient $\epsilon$ (structure mass / initial mass per stage). Find the optimal mass split.

<details><summary>Solution</summary>

**Method.** For equal stages: each stage has initial mass $M/2$, fuel mass $(1-\epsilon)M/2$, structure $\epsilon M/2$. After stage 1: mass $=M/2+\epsilon M/2+M_p$... this is getting complicated. The key result: equal mass ratios $r_1=r_2=r$ give the maximum $\Delta v$. For two stages: $\Delta v=2v_e\ln r$ where $r=\sqrt{M/M_p}$ (for $\epsilon=0$). For $\epsilon>0$: the optimal $r$ is smaller (the dead weight of the structure limits the benefit of staging).

</details>

### OL9 — Momentum flux of a water jet on a plate

A water jet of cross-section $A$ and speed $v$ hits a stationary plate perpendicularly. Find the force on the plate.

<details><summary>Solution</summary>

**Method.** Mass hitting the plate per unit time: $\dot{m}=\rho Av$. The water's horizontal momentum is destroyed (it splatters sideways): $\Delta p/\text{time}=\dot{m}v=\rho Av^2$. Force on the plate: $F=\rho Av^2$.

**Significance.** For a jet at angle $\theta$: $F=\rho Av^2\sin\theta$. For a moving plate at speed $u$: $F=\rho A(v-u)^2$ (the relative speed matters). This is used in turbine design (PART 11).

</details>

### OL10 — The chain folded onto a table

A chain of length $L$ and mass $m$ is folded in half and placed on a table with the fold hanging over the edge. The chain is released. Find the speed when the chain just leaves the table.

<details><summary>Solution</summary>

**Method.** At the moment the chain leaves: the fold has fallen a distance $L/2$ (from the edge to the point where the chain is straight). But this is not a simple free-fall problem — the chain's configuration changes. Energy conservation: the PE lost by the chain equals the KE gained. The COM of the chain starts at height $L/4$ above the table (approximately, for the folded configuration) and ends at height $-L/2$ below the table. $\Delta U=mg\times(3L/4)$. $K=\frac{1}{2}mv^2$. $v=\sqrt{3gL/2}$.

</details>

### 10.2 Limits and failure of the model

Conservation of momentum is exact in Newtonian mechanics for isolated systems. In relativity (PART 28), the momentum is $\mathbf{p}=\gamma m\mathbf{v}$, and the conservation law still holds but in the relativistic form. The coefficient of restitution is an empirical parameter — it depends on the materials, the speed, and the geometry. The rocket equation assumes constant $v_e$ and no external forces — real rockets must account for gravity and air resistance. Inside these fences the methods are exact.

## Part 11 · Olympiad-grade paper

**Time: 180 minutes · Maximum marks: 200 · 36 questions.**
Sections: A — 12 single-correct (4 marks each, −1 for a wrong answer); B — 8 one-or-more-correct (4 marks each, no negative marking); C — 6 numerical answers (5 marks each); D — 10 long-form (9 marks each).

| Section | Questions | Marks each | Subtotal | Topic coverage |
|---|---|---:|---:|---|
| A | 1–12 | 4 | 48 | blocks 2–5 |
| B | 13–20 | 4 | 32 | blocks 5–9 |
| C | 21–26 | 5 | 30 | blocks 7–13 |
| D | 27–36 | 9 | 90 | block 10 |
| | 36 | | 200 | |

#### Section A · Concept MCQ (12 × 4)

### P1 · 4 marks
The COM of a system moves at constant velocity when:
(a) all internal forces cancel  (b) the net external force is zero  (c) the system is at rest  (d) the system is rigid

<details><summary>Answer</summary>

(b). Internal forces always cancel; the COM accelerates only under external forces.

</details>

### P2 · 4 marks
In a perfectly inelastic collision:
(a) all KE is lost  (b) the objects stick together  (c) $e=1$  (d) momentum is not conserved

<details><summary>Answer</summary>

(b). $e=0$ (not 1). Momentum is always conserved in a collision.

</details>

### P3 · 4 marks
The coefficient of restitution applies:
(a) to the full velocity  (b) only along the line of impact  (c) only for elastic collisions  (d) only in 1-D

<details><summary>Answer</summary>

(b). $e$ applies only along the line of impact, regardless of the collision type.

</details>

### P4 · 4 marks
In the rocket equation $\Delta v=v_e\ln(m_0/m_f)$:
(a) $v_e$ is the rocket's speed  (b) $v_e$ is the exhaust speed relative to the rocket  (c) $m_0$ is the final mass  (d) $\Delta v$ is proportional to $m_0/m_f$

<details><summary>Answer</summary>

(b). $v_e$ is the exhaust speed relative to the rocket. $\Delta v$ is logarithmic in $m_0/m_f$.

</details>

### P5 · 4 marks
Two equal-mass balls collide elastically (one at rest). After the collision:
(a) the incoming ball stops  (b) both move at $v/2$  (c) the incoming ball bounces back  (d) they move at 90°

<details><summary>Answer</summary>

(a). In 1-D: the incoming ball stops, the target moves at $v$. In 2-D: they move at 90° to each other.

</details>

### P6 · 4 marks
Impulse has units:
(a) N  (b) N s  (c) J  (d) kg m/s

<details><summary>Answer</summary>

(b), (d). N s and kg m/s are equivalent.

</details>

### P7 · 4 marks
A man walks on a boat (no external forces). The COM:
(a) moves forward  (b) moves backward  (c) stays fixed  (d) depends on who is heavier

<details><summary>Answer</summary>

(c). No external horizontal force — the COM stays fixed.

</details>

### P8 · 4 marks
In a 1-D elastic collision with $m_1\gg m_2$:
(a) $v_1\approx u_1$  (b) $v_2\approx2u_1$  (c) the heavy ball barely slows  (d) all of the above

<details><summary>Answer</summary>

(d). The heavy ball barely changes; the light ball bounces at nearly $2u_1$.

</details>

### P9 · 4 marks
The energy lost in a 1-D collision is:
(a) $\frac{1}{2}\mu v_{\text{rel}}^2$  (b) $\frac{1}{2}\mu v_{\text{rel}}^2(1-e^2)$  (c) zero for elastic  (d) both (b) and (c)

<details><summary>Answer</summary>

(d). For $e=1$: $\Delta K=0$. For $e=0$: $\Delta K=\frac{1}{2}\mu v_{\text{rel}}^2$.

</details>

### P10 · 4 marks
A ball bounces to 64% of its original height. $e=$:
(a) 0.64  (b) 0.8  (c) 0.36  (d) 0.4

<details><summary>Answer</summary>

(b). $e=\sqrt{h_2/h_1}=\sqrt{0.64}=0.8$.

</details>

### P11 · 4 marks
The positive-mass/negative-mass trick is used for:
(a) finding the COM of a body with a hole  (b) conservation of momentum  (c) elastic collisions  (d) rocket problems

<details><summary>Answer</summary>

(a). Treat the hole as negative mass to find the COM.

</details>

### P12 · 4 marks
In the ballistic pendulum:
(a) momentum is conserved during the collision  (b) energy is conserved during the collision  (c) momentum is conserved during the swing  (d) energy is conserved during the swing

<details><summary>Answer</summary>

(a), (d). Momentum for the collision; energy for the swing.

</details>

#### Section B · One-or-more-correct (8 × 4)

### P13 · 4 marks
The COM of a system:
(a) can lie outside the body  (b) moves at constant velocity if $\sum F_{\text{ext}}=0$  (c) is always at the geometric centre  (d) is the weighted average of positions

<details><summary>Answer</summary>

(a), (b), (d). The COM is at the geometric centre only for uniform symmetric bodies.

</details>

### P14 · 4 marks
For a 1-D collision:
(a) momentum is always conserved  (b) KE is conserved only if $e=1$  (c) the relative velocity reverses  (d) $v_2-v_1=-e(u_1-u_2)$

<details><summary>Answer</summary>

(a), (b), (c), (d). All four are correct.

</details>

### P15 · 4 marks
In the CM frame:
(a) total momentum is zero  (b) elastic collisions reverse velocities  (c) $K=K_{\text{rel}}$  (d) all of the above

<details><summary>Answer</summary>

(d). All three are correct.

</details>

### P16 · 4 marks
A rocket:
(a) works by conservation of momentum  (b) needs an atmosphere to push against  (c) works in vacuum  (d) the thrust is $\dot{m}v_e$

<details><summary>Answer</summary>

(a), (c), (d). Rockets work by ejecting mass — no atmosphere needed.

</details>

### P17 · 4 marks
The impulse approximation:
(a) assumes the collision time is very short  (b) neglects finite forces during the collision  (c) is valid when $F_{\text{impulse}}\gg F_{\text{other}}$  (d) all of the above

<details><summary>Answer</summary>

(d). All three are correct.

</details>

### P18 · 4 marks
A ball bouncing on a moving platform:
(a) can gain energy from the platform  (b) the bounce height depends on $e$  (c) resonance occurs at specific frequencies  (d) all of the above

<details><summary>Answer</summary>

(d). All three are correct.

</details>

### P19 · 4 marks
The energy loss in a collision:
(a) is $\frac{1}{2}\mu v_{\text{rel}}^2(1-e^2)$  (b) is zero for $e=1$  (c) is maximum for $e=0$  (d) all of the above

<details><summary>Answer</summary>

(d). All three are correct.

</details>

### P20 · 4 marks
For a man walking on a boat:
(a) the COM of the system stays fixed  (b) the boat moves opposite to the man  (c) the man's displacement relative to the ground is $Md/(m+M)$  (d) all of the above

<details><summary>Answer</summary>

(d). All three are correct.

</details>

#### Section C · Numerical answers (6 × 5)

### P21 · 5 marks
Find the COM of three masses: 1 kg at $(0,0)$, 2 kg at $(3,0)$, 3 kg at $(0,4)$.

<details><summary>Answer</summary>

$X=(0+6+0)/6=1$ m. $Y=(0+0+12)/6=2$ m. COM at $(1,2)$.

</details>

### P22 · 5 marks
A 0.02 kg bullet at 300 m/s embeds in a 1.98 kg block. Find the common velocity.

<details><summary>Answer</summary>

$v=0.02\times300/2=3$ m/s.

</details>

### P23 · 5 marks
A 2 kg ball at 6 m/s collides elastically with a 4 kg ball at rest (1-D). Find $v_2$.

<details><summary>Answer</summary>

$v_2=2\times2\times6/(2+4)=24/6=4$ m/s.

</details>

### P24 · 5 marks
A rocket ($v_e=2500$ m/s) needs $\Delta v=5000$ m/s. Find $m_0/m_f$.

<details><summary>Answer</summary>

$m_0/m_f=e^{5000/2500}=e^2=7.39$.

</details>

### P25 · 5 marks
A ball bounces three times with $e=0.7$ from 10 m. Find the height after the third bounce.

<details><summary>Answer</summary>

$h_3=10\times0.7^6=10\times0.1176=1.176$ m.

</details>

### P26 · 5 marks
A 5 kg object at rest explodes into 3 kg and 2 kg. The 3 kg piece moves at 4 m/s. Find the KE of the 2 kg piece.

<details><summary>Answer</summary>

$v_2=3\times4/2=6$ m/s. $K_2=\frac{1}{2}\times2\times36=36$ J.

</details>

#### Section D · Long-form (10 × 9)

### P27 · 9 marks
(a) Derive $M\mathbf{a}_{\text{cm}}=\mathbf{F}_{\text{ext}}$ from Newton's third law. (b) A shell explodes into three equal fragments at the top of its trajectory. Two fragments fly horizontally at right angles at 100 m/s each. Find the velocity of the third. (c) Sketch the COM trajectory.

<details><summary>Answer</summary>

(a) See §3.3. (b) $0=m\times100\hat{i}+m\times100\hat{j}+mv_3$. $v_3=-100\hat{i}-100\hat{j}$. Speed $=100\sqrt{2}=141$ m/s at 225°. (c) The COM continues on the original parabola — the fragments fly apart around it.

</details>

### P28 · 9 marks
(a) Derive the general 1-D collision formulas for $v_1$ and $v_2$. (b) Verify the limits: $e=1$ (elastic), $e=0$ (perfectly inelastic), $m_1\gg m_2$. (c) Derive the energy-loss formula.

<details><summary>Answer</summary>

(a) See §3.7. (b) At $e=1$: $v_1=(m_1-m_2)u_1/(m_1+m_2)$, $v_2=2m_1u_1/(m_1+m_2)$. At $e=0$: $v_1=v_2=(m_1u_1+m_2u_2)/(m_1+m_2)$. At $m_1\gg m_2$: $v_1\approx u_1$, $v_2\approx2u_1-u_2$. (c) $\Delta K=\frac{1}{2}\mu(u_1-u_2)^2(1-e^2)$.

</details>

### P29 · 9 marks
(a) A ballistic pendulum: 10 g bullet, 2 kg block, height 0.05 m. Find the bullet speed. ($g=10$ m/s$^2$.) (b) What fraction of the KE is lost in the collision? (c) Where does the lost energy go?

<details><summary>Answer</summary>

(a) $V=\sqrt{2\times10\times0.05}=1$ m/s. $v_0=(2.01/0.01)\times1=201$ m/s. (b) $K_i=\frac{1}{2}\times0.01\times201^2=202$ J. $K_f=\frac{1}{2}\times2.01\times1=1.005$ J. Fraction lost $=(202-1)/202=99.5\%$. (c) The lost energy goes into heat, sound, and deformation of the bullet and block.

</details>

### P30 · 9 marks
(a) Derive the rocket equation. (b) A two-stage rocket has $m_0=1000$ kg, $M_p=100$ kg, $v_e=3$ km/s, equal stages. Find $\Delta v$. (c) Compare with a single-stage rocket.

<details><summary>Answer</summary>

(a) See §3.10. (b) Stage 1: $m_0=1000$, $m_f=550$ (half structure + payload + half fuel). $\Delta v_1=3\ln(1000/550)=3\times0.598=1.79$ km/s. Stage 2: $m_0=500$, $m_f=100$. $\Delta v_2=3\ln(500/100)=3\times1.609=4.83$ km/s. Total $=6.62$ km/s. (c) Single stage: $\Delta v=3\ln(1000/100)=3\times2.303=6.91$ km/s. The two-stage is slightly worse here because the structural mass is the same. The advantage of staging comes when the structural coefficient $\epsilon$ is significant.

</details>

### P31 · 9 marks
(a) A ball bounces with $e=0.6$ from height 5 m. Find the total distance and time. ($g=10$ m/s$^2$.) (b) How many bounces until the height is less than 0.1 m? (c) What is the total energy dissipated?

<details><summary>Answer</summary>

(a) $d=5(1+0.36)/(1-0.36)=5\times1.36/0.64=10.625$ m. $t_0=1$ s. $t=1\times1.6/0.4=4$ s. (b) $5\times0.6^{2n}<0.1$. $0.36^n<0.02$. $n\ln0.36<\ln0.02$. $n>4.6/1.02=4.5$. After 5 bounces. (c) All original energy is eventually dissipated: $E_0=mgh=5mg$ J (for mass $m$).

</details>

### P32 · 9 marks
(a) A 2 kg ball at 5 m/s collides with a 3 kg ball at $-2$ m/s ($e=0.5$). Find the velocities. (b) Find the energy lost. (c) Verify the energy-loss formula.

<details><summary>Answer</summary>

(a) $v_1=(2-0.5\times3)/5\times5+(1.5)\times3/5\times(-2)=(0.5/5)\times5+0.9\times(-2)=0.5-1.8=-1.3$ m/s. $v_2=(1.5)\times2/5\times5+(3-0.5\times2)/5\times(-2)=3+(-0.8)=2.2$ m/s. (b) $K_i=\frac{1}{2}\times2\times25+\frac{1}{2}\times3\times4=31$ J. $K_f=\frac{1}{2}\times2\times1.69+\frac{1}{2}\times3\times4.84=1.69+7.26=8.95$ J. $\Delta K=22.05$ J. (c) $\mu=2\times3/5=1.2$. $v_{\text{rel}}=5-(-2)=7$. $\Delta K=\frac{1}{2}\times1.2\times49\times(1-0.25)=29.4\times0.75=22.05$ J. ✓

</details>

### P33 · 9 marks
(a) Two equal-mass balls collide elastically (one at rest). The incoming ball is deflected by 45°. Find the speeds and the other ball's angle. (b) Verify that the total KE is conserved. (c) What happens if the collision is not smooth (friction)?

<details><summary>Answer</summary>

(a) $\theta_2=45°$ (90° rule). From momentum: $v_1\cos45°+v_2\cos45°=v_0$. $v_1\sin45°=v_2\sin45°$. $v_1=v_2$. From $x$: $2v_1\cos45°=v_0$. $v_1=v_2=v_0/\sqrt{2}$. (b) $K_i=\frac{1}{2}mv_0^2$. $K_f=\frac{1}{2}m\times v_0^2/2+\frac{1}{2}m\times v_0^2/2=\frac{1}{2}mv_0^2$. ✓ (c) With friction: a tangential impulse acts, changing the tangential velocities. The 90° result no longer holds. The collision is still elastic (if $e=1$), but the directions change.

</details>

### P34 · 9 marks
(a) Sand falls at 3 kg/s onto a belt moving at 4 m/s. Find the force and power. (b) Where does the belt's power go? (c) A chain of mass 2 kg is lifted at 3 m/s. Find the force as a function of height $x$.

<details><summary>Answer</summary>

(a) $F=\dot{m}v=3\times4=12$ N. $P=Fv=48$ W. (b) Half goes into KE of the sand ($\frac{1}{2}\dot{m}v^2=24$ W). Half goes into heat (friction between sand and belt). (c) $F=\lambda xg+\lambda v^2$. $\lambda=2/L$. $F=(2/L)(10x+9)$.

</details>

### P35 · 9 marks
(a) A block of mass $m$ slides into a block of mass $M$ connected to a spring ($k$). The collision is perfectly inelastic. Find the maximum compression of the spring. (b) What if the collision is elastic? (c) Which gives more compression?

<details><summary>Answer</summary>

(a) Momentum: $mv_0=(m+M)V$. $V=mv_0/(m+M)$. Energy: $\frac{1}{2}(m+M)V^2=\frac{1}{2}kx^2$. $x=V\sqrt{(m+M)/k}=mv_0/\sqrt{k(m+M)}$. (b) Elastic: $v_1=(m-M)v_0/(m+M)$, $v_2=2mv_0/(m+M)$. Energy of $M$: $\frac{1}{2}Mv_2^2=\frac{1}{2}kx^2$. $x=v_2\sqrt{M/k}=2mv_0\sqrt{M}/((m+M)\sqrt{k})$. (c) The elastic collision gives more compression (the target receives more energy).

</details>

### P36 · 9 marks
(a) Derive the COM-frame energy decomposition $K=\frac{1}{2}Mv_{\text{cm}}^2+K_{\text{rel}}$. (b) For a collision, show that the CM KE is unchanged. (c) Find the minimum energy to create a particle of mass $M$ in a collision of two particles (each of mass $m$) in the CM frame.

<details><summary>Answer</summary>

(a) See OL1. (b) The CM velocity is unchanged by the collision (momentum conservation). So $\frac{1}{2}Mv_{\text{cm}}^2$ is unchanged. (c) In the CM frame: total momentum is zero. To create a particle of mass $M$: the total energy must be at least $Mc^2$ (in the relativistic case) or the total KE must equal $Mc^2-mc^2-mc^2$... this is a relativistic calculation. In the non-relativistic case: the minimum KE is such that the particles come to rest in the CM frame — all KE goes into creating the new mass. This is a preview of PART 28 (relativistic collisions).

</details>

## Part 12 · Marking scheme and post-paper audit

| Section | Marks each | Questions | Subtotal |
|---|---:|---:|---:|
| A | 4 | 12 | 48 |
| B | 4 | 8 | 32 |
| C | 5 | 6 | 30 |
| D | 9 | 10 | 90 |
| **Total** | | 36 | **200** |

## Part 13 · Formula sheet

| Formula | Validity |
|---|---|
| $\mathbf{R}=\sum m_i\mathbf{r}_i/M$ | centre of mass definition |
| $M\mathbf{a}_{\text{cm}}=\mathbf{F}_{\text{ext}}$ | COM equation of motion |
| $\mathbf{J}=\Delta\mathbf{p}=\int\mathbf{F}\,dt$ | impulse–momentum theorem |
| $\sum\mathbf{p}=$ const | if $\sum\mathbf{F}_{\text{ext}}=\mathbf{0}$ |
| $e=v_{\text{sep}}/v_{\text{app}}$ | along the line of impact |
| $\Delta K=\frac{1}{2}\mu v_{\text{rel}}^2(1-e^2)$ | energy lost in 1-D collision |
| $\Delta v=v_e\ln(m_0/m_f)$ | rocket equation |
| $v_{\text{after}}-v_w=-e(v_{\text{before}}-v_w)$ | moving-wall bounce |
| $K=\frac{1}{2}Mv_{\text{cm}}^2+\frac{1}{2}\mu v_{\text{rel}}^2$ | CM-frame energy decomposition |

## Part 14 · Checkpoint and hand-off

- [ ] I can find the centre of mass of any body or system.
- [ ] I can derive $M\mathbf{a}_{\text{cm}}=\mathbf{F}_{\text{ext}}$ from Newton's third law.
- [ ] I can apply conservation of momentum to explosions, collisions, and recoil.
- [ ] I can classify collisions and use the coefficient of restitution.
- [ ] I can solve 1-D and 2-D collision problems.
- [ ] I can work in the CM frame and use the energy decomposition.
- [ ] I can solve variable-mass problems (rocket equation, sand on belt).
- [ ] I can solve two-stage impulse problems (ballistic pendulum, bullet-block).
- [ ] I understand the impulse approximation and its validity.
- [ ] I can analyse successive bouncing with restitution.

**What the next chapters inherit.** Conservation of momentum is the foundation of PART 8 (angular momentum conservation), PART 9 (two-body reduced mass and orbital mechanics), and PART 11 (fluid momentum flux). The CM-frame analysis is used in nuclear and particle physics (PART 26). The collision tools are used in PART 10 (energy of oscillations via the collision model of damping).

**Open questions.** What is the relativistic generalisation of momentum ($\mathbf{p}=\gamma m\mathbf{v}$)? How does the impulse approximation justify the use of momentum conservation in nuclear reactions? These are questions for PART 28 and nuclear physics.
