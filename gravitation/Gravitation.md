---
title: "Gravitation & Orbital Motion"
part: 9
slug: gravitation
source: Cengage Mechanics II-compressed.pdf, ch 5 Gravitation
aliases: [gravitation, orbital-motion, kepler, satellite, escape-velocity]
tags: [jee-advanced, olympiad, mechanics, gravitation, orbits]
---

# Gravitation & Orbital Motion — first principles to Olympiad

> [!abstract] How to use this chapter
> Three passes. Pass 1: Parts 0–4 — the inverse-square law, the shell theorem, $g$ variations, gravitational PE, and Kepler's laws. Pass 2: Parts 5–9 for exam craft. Pass 3: Parts 10–14 — the Olympiad layer (tidal forces, the Roche limit, Hohmann transfers, gravity assist, the virial theorem, the Schwarzschild radius, binary-star masses), the paper, the sheet, the checkpoint. Every number recomputed; every boxed result carries its validity condition.

## Part 0 · Orientation

### 0.1 What you will be able to do

After this chapter you can: state and apply the inverse-square law; prove the shell theorem; compute the gravitational field and potential inside and outside spheres, shells and cavities; derive all four $g$ variations; use $U=-GMm/r$ for orbital problems; derive Kepler's three laws; solve circular and elliptical orbit problems; compute geostationary-orbit parameters; analyse Hohmann transfers and gravity-assist manoeuvres.

### 0.2 The one idea

Gravity is a central inverse-square field, and every orbit is energy and angular momentum trading places.

### 0.3 Prerequisite self-check

You need PART 8 (rotational mechanics, angular momentum) and PART 6 (energy, potential energy). If you can integrate a polynomial and apply energy conservation, you are ready.

### 0.4 Exam orientation

JEE Advanced treats gravitation as a "standard" topic — 2–3 questions per year, usually on orbital mechanics, escape velocity, or $g$ variations. INPhO and IPhO reward the ability to derive the shell theorem, handle elliptical orbits, and analyse gravity-assist and tidal problems. The trap density is moderate: using $g=GM/R^2$ at a height without adjusting $R$, treating PE as $mgh$ at orbital distances, and forgetting the negative sign of $U$.

### 0.5 What this chapter is not

Not an electrostatics chapter: the $1/r^2$ force in electrostatics (PART 13) has the same mathematical form but different physics (can be repulsive). Not a general-relativity chapter: the Newtonian theory is exact for weak fields and low speeds.

### 0.6 Syllabus coverage map

| # | Cengage section | What it establishes | Where it lives here | Status |
|---:|---|---|---|---|
| 1 | The inverse-square law | $F=GMm/r^2$ | §3.1 | full |
| 2 | Field and potential | $\mathbf{g}$, $V=-GM/r$ | §3.2 | full |
| 3 | Shell theorem | Field inside/outside shells | §3.3 | full |
| 4 | Sphere, shell, cavity | Field and potential by superposition | §3.4 | full |
| 5 | $g$ variations | Altitude, depth, latitude, rotation | §3.5 | full |
| 6 | Gravitational PE | $U=-GMm/r$ | §3.6 | full |
| 7 | Kepler's laws | Derived from angular momentum and energy | §3.7 | full |
| 8 | Circular orbits | $v=\sqrt{GM/r}$, $E=-GMm/(2r)$ | §3.8 | full |
| 9 | Elliptical orbits | Vis-viva, perigee/apogee | §3.9 | full |
| 10 | Satellites | Geostationary, polar | §3.10 | full |
| 11 | Transfers | Hohmann, plane changes | §3.11 | full |
| 12 | Binary stars | Reduced mass, two-body Kepler | §3.12 | full |
| 13 | Tides and Roche limit | Differential pull | §3.13 | full |

## Part 1 · Intuition first

**Gravity is always attractive and always central.** The gravitational force between two masses acts along the line joining them and is proportional to each mass and inversely proportional to the square of the distance: $F=GMm/r^2$. The universal constant $G=6.674\times10^{-11}$ N m$^2$/kg$^2$ is tiny — gravity is the weakest of the four fundamental forces.

**A uniform shell exerts no net force on a particle inside it.** This is the shell theorem — the most powerful result in gravitational theory. It means that inside a uniform sphere, only the mass closer to the centre than the particle contributes to the gravitational force. The field inside a uniform sphere is proportional to $r$: $g(r)=GM r/R^3$.

**Orbits are conic sections.** A particle in a $1/r^2$ force follows a circle, ellipse, parabola, or hyperbola, depending on its energy. Bound orbits (circles and ellipses) have $E<0$; unbound orbits (parabolas and hyperbolas) have $E\ge0$.

**The orbital speed decreases with altitude.** $v=\sqrt{GM/r}$ — the higher the orbit, the slower the satellite. This is counter-intuitive: "higher = slower." The reason: a higher orbit has more PE and less KE, and the total energy is more negative.

## Part 2 · Definitions and bookkeeping

| Symbol | Meaning | SI unit |
|---|---|---|
| $G$ | universal gravitational constant $=6.674\times10^{-11}$ | N m$^2$/kg$^2$ |
| $M$ | mass of the central body | kg |
| $m$ | mass of the orbiting body | kg |
| $r$ | distance from the centre | m |
| $\mathbf{g}$ | gravitational field (acceleration) | m/s$^2$ |
| $V$ | gravitational potential | J/kg |
| $U$ | gravitational potential energy | J |
| $E$ | total orbital energy | J |
| $L$ | orbital angular momentum | kg m$^2$/s |
| $T$ | orbital period | s |
| $a$ | semi-major axis of an ellipse | m |
| $e$ | eccentricity of an orbit | dimensionless |

> [!info] Bookkeeping rules
> $U=-GMm/r$ with the reference at infinity (where $U=0$). The total energy $E=K+U$ for a bound orbit is always negative. The escape speed is $v_{\text{esc}}=\sqrt{2GM/R}$ — the speed needed to reach infinity with zero KE.

## Part 3 · Core derivations

### 3.1 The inverse-square law

$$
\mathbf{F}=-\frac{GMm}{r^2}\hat{r}. \qquad (3.1)
$$

The force is attractive (toward the central mass), central (along $\hat{r}$), and proportional to $1/r^2$.

### 3.2 Field and potential

$$
\mathbf{g}=-\frac{GM}{r^2}\hat{r},\qquad V=-\frac{GM}{r}. \qquad (3.2)
$$

$\mathbf{g}$ is the force per unit mass. $V$ is the potential energy per unit mass. The equipotentials are spheres; the field lines are radial.

### 3.3 The shell theorem

**Statement:** (1) A uniform spherical shell attracts a particle outside as if all the shell's mass were concentrated at the centre. (2) A uniform spherical shell exerts no net gravitational force on a particle inside it.

**Proof sketch:** Consider a shell of radius $R$ and a particle at distance $r>R$. Divide the shell into thin rings. Each ring's contribution is $dF=GM\,dm\cos\phi/r'^2$ where $r'$ is the distance from the ring to the particle. By geometry, the $\cos\phi$ factor and the $1/r'^2$ combine to give $dF=G(M\,dm/M)/r^2$ — the same as if all mass were at the centre. For $r<R$: the contributions from opposite sides of the shell cancel exactly.

> [!abstract] DIAGRAM D9.1 · The shell theorem cone construction
> *Show:* a spherical shell with a particle $P$ outside. Two small cones from $P$ intersect the shell in two areas $dA_1$ and $dA_2$. The nearer area is smaller but closer (stronger pull); the farther area is larger but farther (weaker pull). The two effects exactly cancel for a $1/r^2$ force.
> *Search:* "shell theorem cone construction inverse square proof diagram"

### 3.4 Sphere, shell and cavity

**Outside a uniform sphere** ($r\ge R$): $g=GM/r^2$, $V=-GM/r$ (same as a point mass).

**Inside a uniform sphere** ($r<R$): only the mass within $r$ contributes. $M(r)=M(r/R)^3$.

$$
g(r)=\frac{GM(r)}{r^2}=\frac{GMr}{R^3},\qquad V(r)=-\frac{GM}{2R^3}(3R^2-r^2). \qquad (3.3)
$$

**Spherical cavity** (by superposition): field at a point in a cavity = field of the full sphere minus the field of the removed sphere.

> [!abstract] DIAGRAM D9.2 · Field inside a uniform sphere and the cavity
> *Show:* left: $g(r)$ vs $r$ for a uniform sphere — linear rise from zero at the centre to $GM/R^2$ at the surface, then $1/r^2$ falloff. Right: a sphere with a cavity, with the superposition method shown (full sphere minus small sphere).
> *Search:* "gravitational field inside uniform sphere cavity superposition diagram"

### 3.5 $g$ and its variations

**Altitude:** $g'=g(1-2h/R)$ for $h\ll R$.

**Depth:** $g'=g(1-d/R)$ (inside a uniform sphere, $g$ decreases linearly).

**Latitude:** $g_{\text{eff}}=g-\omega^2 R\cos^2\lambda$ (centrifugal reduction, $\lambda$ = latitude).

**Rotation:** $g_{\text{eff}}$ at the equator is $g-\omega^2 R\approx9.78$ m/s$^2$ (0.3% less than at the pole).

> [!abstract] DIAGRAM D9.3 · The four $g$-variation curves on one plate
> *Show:* four panels: (1) $g$ vs altitude (decreasing); (2) $g$ vs depth (linear decrease to zero at centre); (3) $g$ vs latitude (slight increase from equator to pole); (4) $g$ vs rotation rate (decreasing as $\omega$ increases).
> *Search:* "gravitational acceleration variation altitude depth latitude rotation graph"

### 3.6 Gravitational potential energy

$$
U=-\frac{GMm}{r}. \qquad (3.4)
$$

The reference is at infinity ($U=0$). The PE is always negative for a bound system. The "energy to escape": $E_{\text{escape}}=0-E_{\text{orbit}}=GMm/(2r)$ for a circular orbit.

### 3.7 Kepler's laws

**First law:** orbits are ellipses with the central mass at one focus.

**Second law:** equal areas in equal times (angular momentum conservation: $dA/dt=L/(2m)$).

**Third law:**

$$
T^2=\frac{4\pi^2}{GM}a^3. \qquad (3.5)
$$

> [!abstract] DIAGRAM D9.4 · A Kepler ellipse with the focus, the two radii and the equal-area sectors
> *Show:* an ellipse with the central mass at one focus. Two radii drawn from the focus to the ellipse at two nearby times. The area swept (a thin sector) shaded. The equal-area property shown: the sector at perigee (narrow, long) has the same area as the sector at apogee (wide, short).
> *Search:* "Kepler ellipse focus equal area sectors perigee apogee diagram"

### 3.8 Circular orbits

$$
v=\sqrt{\frac{GM}{r}},\qquad E=-\frac{GMm}{2r},\qquad L=m\sqrt{GMr}. \qquad (3.6)
$$

The total energy is negative (bound). The KE is half the magnitude of the PE: $K=-E$, $U=2E$.

### 3.9 Elliptical orbits and the vis-viva equation

$$
v^2=GM\left(\frac{2}{r}-\frac{1}{a}\right). \qquad (3.7)
$$

At perigee ($r=a(1-e)$): $v_p=\sqrt{\frac{GM}{a}\frac{1+e}{1-e}}$.

At apogee ($r=a(1+e)$): $v_a=\sqrt{\frac{GM}{a}\frac{1-e}{1+e}}$.

> [!abstract] DIAGRAM D9.5 · The vis-viva graph of $E$ vs $r$ for several $L$
> *Show:* a graph of the effective potential $U_{\text{eff}}=-GMm/r+L^2/(2mr^2)$ vs $r$ for three values of $L$. For each: the total energy $E$ shown as a horizontal line. The turning points (where $E=U_{\text{eff}}$) are the perigee and apogee.
> *Search:* "effective potential energy versus r circular elliptical orbit turning points"

### 3.10 Geostationary orbit

A satellite in a geostationary orbit orbits above the equator with a period of 24 hours, so it appears stationary in the sky.

$$
r_{\text{geo}}=\left(\frac{GMT^2}{4\pi^2}\right)^{1/3}\approx42{,}164\text{ km}. \qquad (3.8)
$$

Altitude above Earth's surface: $\approx35{,}786$ km.

### 3.11 Hohmann transfer

The most energy-efficient transfer between two circular orbits uses an ellipse tangent to both. Two burns: one at perigee to enter the transfer ellipse, one at apogee to circularise.

### 3.12 Binary stars

Two stars orbit their common COM. The reduced mass $\mu=m_1m_2/(m_1+m_2)$. Kepler's third law becomes:

$$
T^2=\frac{4\pi^2}{G(m_1+m_2)}a^3. \qquad (3.9)
$$

### 3.13 Tides and the Roche limit

The tidal force is the differential pull across the Earth: $F_{\text{tidal}}\approx2GMmr/R^3$ (where $r$ is the Earth's radius and $R$ is the Moon's distance). The Roche limit: the distance within which tidal forces tear a satellite apart: $d_{\text{Roche}}\approx2.44R_p(\rho_p/\rho_s)^{1/3}$.

> [!abstract] DIAGRAM D9.6 · The tide-raising differential-pull diagram
> *Show:* the Earth with the Moon on the right. The Moon's pull on the near side (stronger) and the far side (weaker) shown as arrows. The differential (tidal) force creates two bulges: one toward the Moon, one away.
> *Search:* "tidal force differential pull Moon Earth two bulges diagram"

## Part 4 · Results, limits and the validity ledger

### 4.1 Boxed results

$$
\boxed{g(r)=\frac{GMr}{R^3}\text{ (inside uniform sphere)},\quad g(r)=\frac{GM}{r^2}\text{ (outside)}} \qquad (4.1)
$$

$$
\boxed{U=-\frac{GMm}{r},\quad E=-\frac{GMm}{2r}\text{ (circular orbit)}} \qquad (4.2)
$$

$$
\boxed{v_{\text{esc}}=\sqrt{\frac{2GM}{R}}=\sqrt{2}\,v_{\text{orb}}} \qquad (4.3)
$$

$$
\boxed{v^2=GM\left(\frac{2}{r}-\frac{1}{a}\right)\text{ (vis-viva)}} \qquad (4.4)
$$

$$
\boxed{T^2=\frac{4\pi^2}{GM}a^3\text{ (Kepler's third law)}} \qquad (4.5)
$$

### 4.2 Limit checks

- $r\to\infty$: $U\to0$, $g\to0$ — no gravity at infinity. ✓
- $r=R$ (surface): $g=GM/R^2$ — the familiar surface gravity. ✓
- $r=0$ (centre): $g=0$ — symmetric cancellation. ✓
- $a\to\infty$: $T\to\infty$ — infinite orbit has infinite period. ✓
- $e=0$: ellipse becomes a circle. ✓

### 4.3 Which formula when

| Given | Need | Use |
|---|---|---|
| $r$ outside a sphere | $g$ or $V$ | $g=GM/r^2$, $V=-GM/r$ |
| $r$ inside a uniform sphere | $g$ | $g=GMr/R^3$ |
| Circular orbit | $v$, $E$, $T$ | Eqs. (4.2), (4.5) |
| Elliptical orbit | speed at any $r$ | Eq. (4.4) |
| Surface gravity | $g$ with altitude/depth/latitude | §3.5 |
| Escape from a planet | $v_{\text{esc}}$ | Eq. (4.3) |
| Binary stars | period | Eq. (3.9) |

### 4.4 Concept checks

**C1 — concept check.** Why does the Moon not fall to Earth?

<details><summary>Answer</summary>

It is falling — constantly. But its tangential velocity is large enough that the "fall" curves it into an orbit. The Moon is in free fall around the Earth.

</details>

**C2 — concept check.** Is there gravity in orbit?

<details><summary>Answer</summary>

Yes — at the ISS altitude (400 km), $g\approx8.7$ m/s$^2$ (90% of surface gravity). The astronauts feel weightless because they are in free fall, not because there is no gravity.

</details>

**C3 — concept check.** Why is $U$ negative for a bound orbit?

<details><summary>Answer</summary>

$U=0$ at infinity (the reference). A bound orbit has $E<0$, meaning the particle cannot escape to infinity without adding energy. The negative $U$ represents the "binding energy."

</details>

**C4 — concept check.** Does a satellite in a higher orbit have more or less energy?

<details><summary>Answer</summary>

More negative energy (less total energy). $E=-GMm/(2r)$: as $r$ increases, $|E|$ decreases (less negative), meaning the satellite is less tightly bound. This is counter-intuitive: a "higher" orbit is actually "less bound." The reason is that the total energy is negative, and it approaches zero as $r\to\infty$. To move a satellite to a higher orbit, you must add energy (fire rockets), which makes $E$ less negative. The confusion arises because "more energy" can mean "more positive" or "more negative" depending on context. In orbital mechanics, always specify whether you mean "more positive total energy" (= less bound) or "more negative total energy" (= more bound).

</details>

**C5 — concept check.** Why does a geostationary orbit have to be above the equator?

<details><summary>Answer</summary>

A satellite orbits in a plane through the centre of the Earth. For the satellite to appear stationary, this plane must be the equatorial plane. An inclined orbit would appear to wander north and south.

</details>

**C6 — concept check.** What is the vis-viva equation used for?

<details><summary>Answer</summary>

Finding the speed at any point in an elliptical orbit, given $r$ and $a$. It combines energy and the orbit geometry.

</details>

**C7 — concept check.** Does the shell theorem apply to non-uniform shells?

<details><summary>Answer</summary>

No — the proof relies on the shell being uniform. A non-uniform shell does exert a net force on an interior particle.

</details>

**C8 — concept check.** Why do we have two tidal bulges (one toward the Moon, one away)?

<details><summary>Answer</summary>

The Moon's pull on the near side is stronger than on the far side. The differential force stretches the Earth along the Earth–Moon line, creating bulges on both sides.

</details>

**C9 — concept check.** Can a satellite orbit at any altitude?

<details><summary>Answer</summary>

In principle yes, but below about 160 km, air drag is significant and the satellite decays quickly. The ISS orbits at about 400 km to minimise drag.

</details>

**C10 — concept check.** What happens to a satellite that loses energy (e.g., due to drag)?

<details><summary>Answer</summary>

It spirals inward, moving *faster* (lower orbit, higher speed). This is counter-intuitive: losing energy makes the satellite speed up! The reason: the PE decrease is larger than the KE increase.

</details>

**C11 — concept check.** The Schwarzschild radius $r_s=2GM/c^2$. What does it represent?

<details><summary>Answer</summary>

The radius at which the escape speed equals the speed of light. For a black hole, $r_s$ is the event horizon. For the Sun: $r_s\approx3$ km.

</details>

**C12 — concept check.** Why does the $\sqrt{2}$ ratio appear in $v_{\text{esc}}=\sqrt{2}\,v_{\text{orb}}$?

<details><summary>Answer</summary>

The orbital KE is $GMm/(2r)$. The escape KE is $GMm/r$ (twice as much). So $v_{\text{esc}}^2=2v_{\text{orb}}^2$.

</details>

## Part 5 · Worked exemplars

### E1 — Orbital speed and period

Find the orbital speed and period of a satellite at altitude 400 km. ($M_E=5.97\times10^{24}$ kg, $R_E=6370$ km.)

> [!success] Check
> $r=6770$ km. $v=\sqrt{GM/r}=\sqrt{6.674\times10^{-11}\times5.97\times10^{24}/6.77\times10^6}=7.67$ km/s. $T=2\pi r/v=5540$ s $\approx92$ min.

<details><summary>Solution</summary>

**Method.** $v=\sqrt{GM/r}=7670$ m/s. $T=2\pi r/v=2\pi\times6.77\times10^6/7670=5540$ s.

</details>

### E2 — Geostationary orbit

Find the radius and altitude of a geostationary orbit. ($G=6.674\times10^{-11}$, $M_E=5.97\times10^{24}$ kg.)

> [!success] Check
> $r=(GMT^2/(4\pi^2))^{1/3}=(6.674\times10^{-11}\times5.97\times10^{24}\times86400^2/(4\pi^2))^{1/3}=42,164$ km. Altitude $=35,786$ km.

<details><summary>Solution</summary>

**Method.** $T=86400$ s. $r^3=GMT^2/(4\pi^2)=3.986\times10^{14}\times7.465\times10^9/39.48=7.54\times10^{22}$. $r=4.216\times10^7$ m $=42,164$ km.

</details>

### E3 — Escape velocity

Find the escape velocity from Earth's surface. ($g=9.8$ m/s$^2$, $R_E=6370$ km.)

> [!success] Check
> $v=\sqrt{2gR}=\sqrt{2\times9.8\times6.37\times10^6}=11.2$ km/s.

<details><summary>Solution</summary>

**Method.** $v=\sqrt{2GM/R}=\sqrt{2gR}=\sqrt{2\times9.8\times6.37\times10^6}=11186$ m/s $=11.2$ km/s.

</details>

### E4 — Energy to move a satellite

Find the energy to move a 1000 kg satellite from a 200 km orbit to a 400 km orbit.

> [!success] Check
> $\Delta E=GMm/(2r_1)-GMm/(2r_2)=GMm(r_2-r_1)/(2r_1r_2)$. $=3.986\times10^{14}\times1000\times200\times10^3/(2\times6.57\times10^6\times6.77\times10^6)=9.5\times10^8$ J.

<details><summary>Solution</summary>

**Method.** $E_1=-GMm/(2r_1)$, $E_2=-GMm/(2r_2)$. $\Delta E=E_2-E_1=GMm/(2r_1)-GMm/(2r_2)=GMm(r_2-r_1)/(2r_1r_2)=9.5\times10^8$ J $\approx0.95$ GJ.

</details>

### E5 — $g$ at the centre of a planet

What is $g$ at the centre of a uniform sphere of radius $R$ and surface gravity $g_0$?

> [!success] Check
> $g=GMr/R^3$ at $r=0$: $g=0$. ✓

<details><summary>Solution</summary>

**Method.** $g(r)=GMr/R^3$. At $r=0$: $g=0$. At $r=R$: $g=GM/R^2=g_0$. The field is linear from 0 to $g_0$.

</details>

### E6 — Kepler's third law: Mars orbit

Mars orbits the Sun at $a=1.524$ AU. Find its orbital period in Earth years.

> [!success] Check
> $T=a^{3/2}=1.524^{3/2}=1.881$ years. ✓

<details><summary>Solution</summary>

**Method.** $T^2\propto a^3$. $T=T_E\times(a/a_E)^{3/2}=1\times1.524^{3/2}=1.881$ years.

</details>

### E7 — Speed at apogee

A satellite in an elliptical orbit has perigee $r_p=7000$ km and apogee $r_a=42000$ km. Find the speed at apogee. ($GM=3.986\times10^{14}$ m$^3$/s$^2$.)

> [!success] Check
> $a=(r_p+r_a)/2=24500$ km. $v_a=\sqrt{GM(2/r_a-1/a)}=\sqrt{3.986\times10^{14}(2/4.2\times10^7-1/2.45\times10^7)}=\sqrt{3.986\times10^{14}\times6.8\times10^{-9}}=1646$ m/s.

<details><summary>Solution</summary>

**Method.** $v_a^2=GM(2/r_a-1/a)=3.986\times10^{14}\times(4.76\times10^{-8}-4.08\times10^{-8})=3.986\times10^{14}\times6.8\times10^{-9}$. $v_a=1646$ m/s $=1.65$ km/s.

</details>

### E8 — Binary star masses

A binary star has $a=10$ AU and $T=25$ years. Find the total mass.

> [!success] Check
> $M=a^3/T^2=1000/625=1.6$ solar masses.

<details><summary>Solution</summary>

**Method.** From Kepler's third law (with solar units): $M/M_\odot=a^3/T^2=10^3/25^2=1.6$.

</details>

### E9 — Tidal force estimate

Estimate the ratio of the Moon's tidal force to the Sun's tidal force on Earth.

> [!success] Check
> $F_{\text{tidal}}\propto M/d^3$. Moon: $M/d^3=7.35\times10^{22}/(3.84\times10^8)^3=1.3\times10^{-6}$. Sun: $M/d^3=2\times10^{30}/(1.5\times10^{11})^3=5.9\times10^{-4}$. Ratio: Moon/Sun $=1.3\times10^{-6}/5.9\times10^{-4}=0.0022$. Wait — the Moon's tidal effect is about 2.2 times the Sun's. Let me recompute. Moon: $M/d^3=7.35\times10^{22}/5.66\times10^{25}=1.3\times10^{-3}$. Sun: $2\times10^{30}/3.375\times10^{33}=5.9\times10^{-4}$. Ratio $=1.3\times10^{-3}/5.9\times10^{-4}=2.2$. The Moon's tidal force is about 2.2 times the Sun's.

<details><summary>Solution</summary>

**Method.** $F_{\text{tidal}}\propto M/d^3$. Moon: $7.35\times10^{22}/(3.84\times10^8)^3=1.3\times10^{-3}$. Sun: $2\times10^{30}/(1.5\times10^{11})^3=5.9\times10^{-4}$. Ratio $=2.2$. The Moon's tidal force is about twice the Sun's — this is why solar and lunar tides are comparable (spring tides when they align).

</details>

### E10 — The Roche limit

Estimate the Roche limit for a satellite of density $\rho_s=2000$ kg/m$^3$ orbiting a planet of density $\rho_p=5000$ kg/m$^3$ and radius $R_p=6\times10^7$ m.

> [!success] Check
> $d=2.44\times6\times10^7\times(5000/2000)^{1/3}=1.464\times10^8\times1.357=1.99\times10^8$ m $\approx199,000$ km.

<details><summary>Solution</summary>

**Method.** $d=2.44R_p(\rho_p/\rho_s)^{1/3}=2.44\times6\times10^7\times(2.5)^{1/3}=1.464\times10^8\times1.357=1.99\times10^8$ m.

</details>

## Part 6 · Problem archetypes and practice

| # | Archetype | Template | Where worked | Variations |
|---:|---|---|---|---|
| 1 | Orbital speed/period | $v=\sqrt{GM/r}$, $T=2\pi r/v$ | E1 | different planets |
| 2 | Geostationary orbit | $r_{\text{geo}}$ | E2 | other planets |
| 3 | Escape velocity | $v=\sqrt{2GM/R}$ | E3 | from orbit |
| 4 | Orbit transfer energy | $\Delta E$ | E4 | Hohmann |
| 5 | $g$ inside a sphere | $g=GMr/R^3$ | E5 | cavity |
| 6 | Kepler's third law | $T^2\propto a^3$ | E6 | binary stars |
| 7 | Vis-viva | $v^2=GM(2/r-1/a)$ | E7 | any point in orbit |
| 8 | Binary star mass | $M=a^3/T^2$ | E8 | radial velocity |
| 9 | Tidal force | $\propto M/d^3$ | E9 | Roche limit |
| 10 | Roche limit | $d=2.44R_p(\rho_p/\rho_s)^{1/3}$ | E10 | different bodies |

### 6.2 In-flow practice

#### Q1. Find $g$ at the surface of Mars ($M=6.4\times10^{23}$ kg, $R=3.4\times10^6$ m).

<details><summary>Solution</summary>

$g=GM/R^2=6.674\times10^{-11}\times6.4\times10^{23}/(3.4\times10^6)^2=42.7\times10^{12}/1.156\times10^{13}=3.7$ m/s$^2$.

</details>

#### Q2. Find the orbital speed at the ISS altitude (400 km). ($g_0=9.8$, $R_E=6370$ km.)

<details><summary>Solution</summary>

$r=6770$ km. $v=\sqrt{g_0R_E^2/r}=\sqrt{9.8\times6370^2/6770}=\sqrt{9.8\times6000}=7.67$ km/s.

</details>

#### Q3. Find the escape velocity from the Moon ($M=7.35\times10^{22}$ kg, $R=1.74\times10^6$ m).

<details><summary>Solution</summary>

$v=\sqrt{2GM/R}=\sqrt{2\times6.674\times10^{-11}\times7.35\times10^{22}/1.74\times10^6}=\sqrt{5.64\times10^6}=2375$ m/s $=2.38$ km/s.

</details>

#### Q4. How much energy to escape from a circular orbit of radius $r$?

<details><summary>Solution</summary>

$\Delta E=0-(-GMm/(2r))=GMm/(2r)$. This equals the orbital KE.

</details>

#### Q5. Find the period of a satellite at the geostationary altitude.

<details><summary>Solution</summary>

$T=24$ hours (by definition of geostationary).

</details>

#### Q6. A planet has $g=20$ m/s$^2$ and $R=8000$ km. Find its mass.

<details><summary>Solution</summary>

$M=gR^2/G=20\times6.4\times10^{13}/6.674\times10^{-11}=1.28\times10^{15}/6.674\times10^{-11}=1.92\times10^{25}$ kg.

</details>

#### Q7. Find $g$ at depth $d=R/2$ inside a uniform Earth. ($g_0=9.8$ m/s$^2$.)

<details><summary>Solution</summary>

$g=g_0(1-d/R)=9.8\times0.5=4.9$ m/s$^2$.

</details>

#### Q8. A satellite's perigee is $r_p=7000$ km, apogee $r_a=21000$ km. Find the semi-major axis.

<details><summary>Solution</summary>

$a=(r_p+r_a)/2=14000$ km.

</details>

#### Q9. The ISS orbits at 400 km. Find its period.

<details><summary>Solution</summary>

$T=2\pi r^{3/2}/\sqrt{GM}=2\pi\times(6.77\times10^6)^{3/2}/\sqrt{3.986\times10^{14}}=2\pi\times5.57\times10^9/1.996\times10^7=1755$ s $\approx29.3$ min... wait. $T=2\pi\sqrt{r^3/(GM)}=2\pi\times(6.77\times10^6)^{3/2}/(3.986\times10^{14})^{1/2}$. $(6.77\times10^6)^{3/2}=5.57\times10^9$. $\sqrt{3.986\times10^{14}}=1.996\times10^7$. $T=2\pi\times5.57\times10^9/1.996\times10^7=1755$ s $\approx87.7$ min. ✓

</details>

#### Q10. Earth orbits the Sun at 1 AU. Mars at 1.524 AU. Find Mars's period.

<details><summary>Solution</summary>

$T=1.524^{3/2}=1.881$ years.

</details>

#### Q11. A satellite is in a circular orbit. It fires its engines to increase its speed by 10%. What happens to the orbit?

<details><summary>Solution</summary>

The orbit becomes elliptical (the satellite is now above circular-orbit speed at that radius). The perigee is at the current position; the apogee is higher.

</details>

#### Q12. Find the speed of a comet at perihelion ($r_p=0.5$ AU) if its aphelion is $r_a=5$ AU.

<details><summary>Solution</summary>

$a=(0.5+5)/2=2.75$ AU. $v_p=\sqrt{GM(2/r_p-1/a)}=\sqrt{GM(4-0.364)/AU}=\sqrt{3.636GM/AU}$. In Earth units: $v_p=v_E\sqrt{3.636}=29.8\times1.907=56.8$ km/s.

</details>

#### Q13. What is the Schwarzschild radius of the Sun? ($M=2\times10^{30}$ kg.)

<details><summary>Solution</summary>

$r_s=2GM/c^2=2\times6.674\times10^{-11}\times2\times10^{30}/(3\times10^8)^2=2.67\times10^{20}/9\times10^{16}=2967$ m $\approx3$ km.

</details>

#### Q14. The Moon orbits at 384,000 km. Find its orbital speed.

<details><summary>Solution</summary>

$v=\sqrt{GM_E/r}=\sqrt{3.986\times10^{14}/3.84\times10^8}=\sqrt{1.038\times10^6}=1019$ m/s $\approx1.02$ km/s.

</details>

#### Q15. Find the minimum speed to put a satellite into a low Earth orbit (ignoring air resistance).

<details><summary>Solution</summary>

$v=\sqrt{gR}=\sqrt{9.8\times6.37\times10^6}=7.9$ km/s.

</details>

#### Q16. A planet has twice Earth's radius and the same density. Find its surface gravity.

<details><summary>Solution</summary>

$g\propto\rho R$. If $R$ doubles and $\rho$ is the same: $g$ doubles. $g=2\times9.8=19.6$ m/s$^2$.

</details>

#### Q17. Find the orbital angular momentum of Earth. ($M=5.97\times10^{24}$ kg, $r=1.5\times10^{11}$ m, $v=29.8$ km/s.)

<details><summary>Solution</summary>

$L=Mvr=5.97\times10^{24}\times2.98\times10^4\times1.5\times10^{11}=2.67\times10^{40}$ kg m$^2$/s.

</details>

#### Q18. A satellite spirals inward due to drag. Does it speed up or slow down?

<details><summary>Solution</summary>

Speed up — it moves to a lower orbit, which has a higher orbital speed. The PE decreases more than the KE increases.

</details>

#### Q19. Find the ratio $v_{\text{esc}}/v_{\text{orb}}$ for any planet.

<details><summary>Solution</summary>

$\sqrt{2}$ — this is universal.

</details>

#### Q20. A Hohmann transfer from Earth orbit (1 AU) to Mars orbit (1.524 AU). Find the semi-major axis of the transfer ellipse.

<details><summary>Solution</summary>

$a=(1+1.524)/2=1.262$ AU.

</details>

#### Q21. Find the gravitational PE of a 100 kg person on Earth's surface.

<details><summary>Solution</summary>

$U=-GMm/R=-6.674\times10^{-11}\times5.97\times10^{24}\times100/6.37\times10^6=-6.25\times10^9$ J $=-6.25$ GJ.

</details>

#### Q22. A binary star has $m_1=2M_\odot$, $m_2=1M_\odot$, $a=5$ AU. Find the period.

<details><summary>Solution</summary>

$T^2=a^3/(m_1+m_2)=125/3=41.67$. $T=6.46$ years.

</details>

#### Q23. What is the density of a planet with $g=10$ m/s$^2$ and $R=6.4\times10^6$ m?

<details><summary>Solution</summary>

$\rho=3g/(4\pi GR)=30/(4\pi\times6.674\times10^{-11}\times6.4\times10^6)=30/5.37\times10^{-3}=5587$ kg/m$^3$ — close to Earth's density. ✓

</details>

#### Q24. Find the minimum speed to escape from the Moon's surface. ($g_{\text{Moon}}=1.6$ m/s$^2$, $R=1740$ km.)

<details><summary>Solution</summary>

$v=\sqrt{2gR}=\sqrt{2\times1.6\times1.74\times10^6}=\sqrt{5.57\times10^6}=2360$ m/s $=2.36$ km/s.

</details>

#### Q25. A satellite at $r=2R_E$ has speed $v$. What is its total energy per unit mass?

<details><summary>Solution</summary>

$E/m=v^2/2-GM/r$. At $r=2R_E$: $v=\sqrt{GM/(2R_E)}$. $E/m=GM/(4R_E)-GM/(2R_E)=-GM/(4R_E)=-gR_E/4=-1.57\times10^7$ J/kg.

</details>

## Part 7 · Alternate methods and the JEE-Advanced advantage toolkit

### 7.1 Energy methods for orbital problems

Instead of solving Newton's law ($F=ma$) component by component, use energy conservation. For a satellite in a circular orbit: $\frac{1}{2}mv^2-\frac{GMm}{r}=E$. This is simpler and less error-prone than resolving forces.

### 7.2 The Gauss's law analogy for gravity

Gauss's law for gravity: $\oint \mathbf{g}\cdot d\mathbf{A}=-4\pi GM_{\text{enc}}$. Use this to find $g$ for symmetric mass distributions (spheres, cylinders, slabs). It is the most elegant way to prove the shell theorem and derive $g(r)$ inside and outside a sphere.

> [!abstract] DIAGRAM D9.7 · The Gauss's law Gaussian surface for a uniform sphere
> *Show:* a uniform sphere with a concentric spherical Gaussian surface of radius $r$ inside the sphere. The enclosed mass $M_{\text{enc}}=M(r/R)^3$ shaded. The field $\mathbf{g}$ is radial and uniform on the Gaussian surface. The integral $\oint g\,dA=g\times4\pi r^2$.
> *Search:* "Gauss's law gravitational field uniform sphere Gaussian surface diagram"

### 7.3 The virial theorem

For a gravitationally bound system in equilibrium: $\langle K\rangle=-\frac{1}{2}\langle U\rangle$, so $\langle E\rangle=\langle K\rangle+\langle U\rangle=-\langle K\rangle=\frac{1}{2}\langle U\rangle$. This is exact for time-averaged quantities and is the foundation of stellar-structure calculations.

### 7.4 Dimensional analysis for orbital quantities

The only combination of $G$, $M$, and $r$ that gives a speed is $\sqrt{GM/r}$. The only combination that gives a time is $\sqrt{r^3/(GM)}$. Use this to check formulas or to derive them from scratch.

## Part 8 · Examiner traps

> [!danger] Trap 1 — Using $g=GM/R^2$ at a height
> $g=GM/R^2$ is valid only at the surface. At height $h$: $g'=GM/(R+h)^2$. The linear approximation $g'=g(1-2h/R)$ is valid only for $h\ll R$.

> [!danger] Trap 2 — Forgetting the minus sign in $U=-GMm/r$
> The potential energy is always negative for a bound system. The energy to escape is $+GMm/r$, not $-GMm/r$.

> [!danger] Trap 3 — Using $mgh$ at orbital distances
> $mgh$ is the small-height approximation of $\Delta U$. At orbital distances, $h$ is not small, and you must use $U=-GMm/r$.

> [!danger] Trap 4 — Confusing $v_{\text{esc}}$ and $v_{\text{orb}}$
> $v_{\text{orb}}=\sqrt{GM/r}$ for a circular orbit. $v_{\text{esc}}=\sqrt{2GM/r}=\sqrt{2}\,v_{\text{orb}}$. The factor of $\sqrt{2}$ is easy to forget.

> [!danger] Trap 5 — Using $T^2=4\pi^2 a^3/(GM)$ for binary stars
> For binary stars, $M$ is replaced by $m_1+m_2$: $T^2=4\pi^2 a^3/(G(m_1+m_2))$.

> [!danger] Trap 6 — Applying the shell theorem to non-uniform shells
> The shell theorem applies only to uniform spherical shells. A non-uniform shell exerts a net force on interior particles.

> [!danger] Trap 7 — Treating $g$ as constant for orbital calculations
> $g$ varies with altitude. For satellites in low orbit, the variation is small but not negligible for precision calculations.

> [!danger] Trap 8 — Confusing the semi-major axis with the average radius
> $a=(r_p+r_a)/2$ is the semi-major axis of the ellipse, not the average radius. The time-averaged distance is different from $a$ for an elliptical orbit.

> [!danger] Trap 9 — Using $E=-GMm/(2r)$ for non-circular orbits
> For elliptical orbits, $E=-GMm/(2a)$, not $-GMm/(2r)$. Only for circular orbits does $a=r$.

> [!danger] Trap 10 — Forgetting that the orbit period depends on the central mass, not the satellite mass
> $T^2=4\pi^2 a^3/(GM)$. The satellite mass $m$ cancels — a feather and a cannonball orbit at the same period.

> [!abstract] DIAGRAM D9.8 · The energy ladder diagram for orbital transfers
> *Show:* three energy levels: surface ($E=-GMm/R$), low orbit ($E=-GMm/(2R)$), escape ($E=0$). The energy increments $\Delta E$ between each level marked. The total energy to launch to orbit is $GMm/(2R)$, half the escape energy.
> *Search:* "energy diagram orbital transfer surface orbit escape ladder"

## Part 9 · Playbook

### 9.1 Triage decision tree

- "Find $g$ at height/depth/latitude": use the four variation formulas.
- "Orbital speed/period": $v=\sqrt{GM/r}$, $T=2\pi r/v$.
- "Escape velocity": $v=\sqrt{2GM/R}$.
- "Geostationary orbit": $r=(GMT^2/(4\pi^2))^{1/3}$.
- "Orbit transfer": vis-viva equation at perigee and apogee.
- "Binary star mass": $M=a^3/T^2$ (in solar units).
- "Tidal force": $\Delta F\propto M/d^3$.
- "Energy inside/outside a sphere": superposition or integration.

### 9.2 Formula map with validity

| Formula | Valid when | Breaks when |
|---|---|---|
| $g=GM/r^2$ | outside a sphere | inside ($r<R$) |
| $g=GMr/R^3$ | inside a uniform sphere | non-uniform sphere |
| $U=-GMm/r$ | reference at infinity | finite-reference problems |
| $v=\sqrt{GM/r}$ | circular orbit | elliptical orbit |
| $T^2=4\pi^2 a^3/(GM)$ | single central mass | binary stars ($M\to m_1+m_2$) |
| $v_{\text{esc}}=\sqrt{2GM/R}$ | from the surface | from orbit |

### 9.3 Timing plan

Sections A and B under two minutes each. Section C three minutes. Section D twelve minutes. Most gravity problems reduce to finding the right $r$ and applying the formula. The vis-viva equation is the single most useful tool.

### 9.4 Pre-submission audit, ten points

1. $r$: measured from the centre, not the surface.
2. $U$: the negative sign is correct.
3. $v_{\text{esc}}$: the factor of $\sqrt{2}$ is correct.
4. Kepler's third law: $M$ is the central mass (or $m_1+m_2$ for binary stars).
5. Geostationary orbit: period is exactly 24 hours.
6. $g$ inside a sphere: $g$ is proportional to $r$.
7. $g$ at a depth: $g'=g(1-d/R)$, not $g(1-d/R)^2$.
8. Energy: $E=-GMm/(2a)$ for elliptical orbits.
9. Units consistent throughout.
10. Every sub-part answered.

> [!abstract] DIAGRAM D9.9 · Hohmann transfer: the tangential ellipse
> *Show:* two concentric circular orbits (inner and outer). An ellipse connecting them, tangent to both at the transfer points. The two velocity vectors at perigee and apogee shown, along with the $\Delta v$ burns.
> *Search:* "Hohmann transfer orbit ellipse perigee apogee delta v diagram"

### 9.5 Strategy notes for the paper

For Section A and B, the most common mistakes are: forgetting the negative sign in $U$, using $g=GM/R^2$ at altitude (instead of $g'=GM/(R+h)^2$), and confusing $v_{\text{orb}}$ with $v_{\text{esc}}$. For Section D, write the solution in logical order: identify the orbit geometry, write the energy equation, solve for the unknown, and check limits.

### 9.6 The Hohmann transfer in detail

The Hohmann transfer is the most energy-efficient transfer between two coplanar circular orbits. It uses an ellipse tangent to both: the perigee is at the inner orbit, the apogee is at the outer orbit. Two engine burns are needed: one at perigee to enter the transfer ellipse, one at apogee to circularise at the outer orbit.

The transfer time is half the period of the transfer ellipse: $T_{\text{transfer}}=\pi\sqrt{a^3/(GM)}$ where $a=(r_1+r_2)/2$. For Earth-to-Mars: $a=1.262$ AU, $T_{\text{transfer}}=258$ days.

The total $\Delta v$ depends on the orbit ratio. For $r_2/r_1=2$: $\Delta v_{\text{total}}=0.536v_1$ (about 53.6% of the inner circular speed). For $r_2/r_1=10$: $\Delta v_{\text{total}}=1.22v_1$ (more than the inner circular speed — this is why transfers to very distant orbits are expensive).

### 9.7 Common numerical pitfalls

When computing orbital quantities, the most common numerical errors are: (1) confusing km with m — $GM$ for Earth is $3.986\times10^{14}$ m$^3$/s$^2$, not km$^3$/s$^2$; (2) forgetting that the period in Kepler's third law is in seconds, not years (unless using solar units); (3) using $g=9.8$ m/s$^2$ at the ISS altitude — the actual $g$ is about $8.7$ m/s$^2$; (4) confusing the semi-major axis with the radius — $a=(r_p+r_a)/2$, not $r_p$ or $r_a$.

### 9.8 The virial theorem applied to circular orbits

For a circular orbit: $K=GMm/(2r)$, $U=-GMm/r$. The virial theorem states $2K=-U$, so $E=K+U=-K=U/2$. This is a powerful shortcut: if you know $K$, you immediately know $U$ and $E$. It applies to any $1/r^2$ force, including electrostatics (where $2K=-U$ for bound states like hydrogen).

### 9.9 Strategy notes for the paper

For Section A and B, the most common mistakes are: forgetting the negative sign in $U$, using $g=GM/R^2$ at altitude instead of $g'=GM/(R+h)^2$, and confusing $v_{\text{orb}}$ with $v_{\text{esc}}$. For Section C numerical problems, always check units and significant figures — the answer must be a single number, and rounding errors can cost marks. For Section D long-form problems, write the solution in logical order: identify the orbit geometry, write the energy equation, solve for the unknown, and check limits. The most common long-form problem is the binary-star mass measurement or the Hohmann transfer $\Delta v$ calculation.

### 9.10 The free-fall time and its applications

The free-fall time for a self-gravitating sphere of density $\rho$ is $t_{\text{ff}}=\sqrt{3\pi/(32G\rho)}$. This is the time it takes for a uniform cloud to collapse from rest under its own gravity. For the Sun's mean density ($1400$ kg/m$^3$): $t_{\text{ff}}\approx1700$ s $\approx28$ minutes. For a galaxy cluster ($\rho\sim10^{-26}$ kg/m$^3$): $t_{\text{ff}}\sim10^{10}$ years — comparable to the age of the universe. The free-fall time is important in star formation, supernova collapse, and the dynamics of galaxy clusters.

### 9.11 Escape from a binary system

A spacecraft in orbit around one star of a binary system can escape to infinity if its total energy (relative to the two-star system) is positive. The escape speed from a circular orbit of radius $r$ around one star is $v_{\text{esc}}=\sqrt{2GM/r}$ — the same as for a single star. However, if the spacecraft is at a Lagrange point, the escape speed is lower because the gravitational pulls of both stars partially cancel. The L1 point between two equal-mass stars is a saddle point of the effective potential — a small perturbation can send the spacecraft toward either star.

> [!info] History note — Cavendish and the measurement of $G$
> Henry Cavendish (1798) measured $G$ using a torsion balance with two lead spheres. His result was accurate to about 1%. The modern value is $G=6.674\times10^{-11}$ N m$^2$/kg$^2$, known to about 0.01%. $G$ is the least precisely known of the fundamental constants — because gravity is so weak, the experiment is extremely sensitive to environmental noise. Cavendish's experiment was originally designed to measure Earth's density, not $G$ — the constant was not identified as fundamental until later. The torsion balance uses two small lead spheres on a wire; the gravitational attraction between them and two larger spheres twists the wire, and the twist angle gives the force.


### 9.12 Connecting to other chapters

The gravitational potential $V=-GM/r$ has exactly the same form as the electric potential $V=kq/r$ for a point charge (PART 24). Every result in this chapter has an exact electrostatic analogue. The key difference: gravity is always attractive, while electrostatics can be repulsive. For like charges, there are no bound orbits; for opposite charges, the orbital physics is identical to gravity. The virial theorem $2K=-U$ applies to both gravitational and electrostatic bound systems.

### 9.13 The gravitational lensing analogy

In general relativity, light bends around massive objects, an effect called gravitational lensing. The deflection angle for a light ray passing at distance $b$ from a mass $M$ is $4GM/(bc^2)$. This is twice the Newtonian prediction because of spatial curvature in general relativity. For the Sun the deflection is about 1.75 arcseconds, first measured by Eddington in 1919 during a solar eclipse. Gravitational lensing is used today to detect dark matter and to measure the masses of galaxy clusters. The phenomenon also produces Einstein rings and arcs when a distant galaxy is aligned behind a massive foreground cluster.

### 9.14 Connecting to electrodynamics

The gravitational potential $V=-GM/r$ has exactly the same form as the electric potential $V=kq/r$ for a point charge, which is covered in PART 24. Every result in this chapter has an exact electrostatic analogue. The key difference is that gravity is always attractive while electrostatics can be repulsive. For like charges there are no bound orbits, but for opposite charges the orbital physics is identical to gravity. The virial theorem $2K=-U$ applies to both gravitational and electrostatic bound systems. This mathematical parallel means that mastering gravitation now will give a head start on electrostatics later in the course.

## Part 10 · Olympiad extension

### OL1 — Shell theorem by Gauss's law for gravity

Use Gauss's law for gravity ($\oint \mathbf{g}\cdot d\mathbf{A}=-4\pi GM_{\text{enc}}$) to prove the shell theorem: a uniform spherical shell exerts no net force on a particle inside it.

<details><summary>Solution</summary>

**Method.** For a Gaussian surface inside the shell (radius $r<R$): $M_{\text{enc}}=0$ (no mass enclosed). By Gauss's law: $\oint \mathbf{g}\cdot d\mathbf{A}=0$. By symmetry, $\mathbf{g}$ is radial and constant on the sphere: $g\times4\pi r^2=0$, so $g=0$.

**Significance.** This is the gravitational analogue of the result for electric fields inside a conducting shell. The proof is exact and does not require integration over rings.

</details>

### OL2 — Free-fall collapse time of a uniform cloud

A uniform spherical cloud of mass $M$ and initial radius $R$ starts at rest and collapses under its own gravity. Find the collapse time.

<details><summary>Solution</summary>

**Method.** By energy conservation: $\frac{1}{2}M\dot{r}^2-GM^2/r=-GM^2/R$ (using $U=-GM^2/r$ for self-gravitating sphere, with some care about factors). The time to collapse from $R$ to $0$: $t=\pi\sqrt{R^3/(8GM)}$. This is a special case of the free-fall time for a self-gravitating sphere, important in astrophysics for star formation.

**Check.** Dimensionally: $t\propto\sqrt{R^3/(GM)}$ — same as Kepler's third law. ✓

</details>

### OL3 — Hohmann transfer $\Delta v$ computation

Find the two $\Delta v$ values for a Hohmann transfer from Earth orbit ($r_1=1$ AU) to Mars orbit ($r_2=1.524$ AU).

<details><summary>Solution</summary>

**Method.** Transfer ellipse: $a=(r_1+r_2)/2=1.262$ AU. At perigee: $v_p=\sqrt{GM(2/r_1-1/a)}$. At apogee: $v_a=\sqrt{GM(2/r_2-1/a)}$. Circular orbit speeds: $v_1=\sqrt{GM/r_1}$, $v_2=\sqrt{GM/r_2}$. $\Delta v_1=v_p-v_1$, $\Delta v_2=v_2-v_a$. In Earth-orbit units: $\Delta v_1=29.8\times(\sqrt{2-1/1.262}-1)=29.8\times0.257=7.66$ km/s. $\Delta v_2=24.1\times(1-\sqrt{2/1.524-1/1.262})=24.1\times0.148=3.57$ km/s. Total: $11.2$ km/s.

</details>

### OL4 — Gravity assist (slingshot) mechanism

A spacecraft approaches Jupiter in a head-on collision geometry (from Jupiter's perspective). Show how the spacecraft gains speed by stealing Jupiter's orbital momentum.

<details><summary>Solution</summary>

**Method.** In Jupiter's rest frame, the spacecraft's speed is unchanged (elastic scattering in Jupiter's gravity). But Jupiter is moving in the Sun's frame at $v_J=13.1$ km/s. If the spacecraft approaches head-on: in Jupiter's frame, the spacecraft speed is $v_s+v_J$. After the encounter, it leaves at speed $v_s+v_J$ in the opposite direction. In the Sun's frame: $v_{\text{after}}=2v_J+v_s$. The spacecraft gains $2v_J$ — a huge boost. This is how Voyager missions reached the outer solar system.

**Significance.** Gravity assist transfers momentum from the planet to the spacecraft. The planet's orbit changes negligibly because $M_{\text{planet}}\gg m_{\text{spacecraft}}$.

</details>

### OL5 — The Roche limit and tidal disruption

Derive the Roche limit: the distance at which a satellite is torn apart by tidal forces.

<details><summary>Solution</summary>

**Method.** The tidal force on a small body of radius $r_s$ at distance $d$ from a planet of mass $M_p$ and radius $R_p$: $F_{\text{tidal}}=2GM_p m r_s/d^3$ (differential force across the body). The self-gravity holding the satellite together: $F_{\text{self}}=Gm^2/r_s^2=G\rho_s(4\pi r_s^3/3)^2/r_s^2$. Setting $F_{\text{tidal}}=F_{\text{self}}$ and simplifying: $d_{\text{Roche}}=R_p(2\rho_p/\rho_s)^{1/3}\approx2.44R_p(\rho_p/\rho_s)^{1/3}$ (the numerical factor accounts for the detailed geometry).

</details>

### OL6 — Binary-star radial-velocity curves

A binary star system has $m_1=1.5M_\odot$, $m_2=0.5M_\odot$, and $a=2$ AU. Find the radial velocity amplitude of each star.

<details><summary>Solution</summary>

**Method.** $a_1=a\times m_2/(m_1+m_2)=2\times0.5/2=0.5$ AU. $a_2=1.5$ AU. $v_1=2\pi a_1/T$, $v_2=2\pi a_2/T$. $T=\sqrt{a^3/(m_1+m_2)}=\sqrt{8/2}=2$ years $=6.31\times10^7$ s. $v_1=2\pi\times0.5\times1.5\times10^{11}/6.31\times10^7=7.47$ km/s. $v_2=22.4$ km/s.

</details>

### OL7 — The Schwarzschild radius

Derive the Schwarzschild radius $r_s=2GM/c^2$ by setting the escape velocity equal to the speed of light.

<details><summary>Solution</summary>

**Method.** $v_{\text{esc}}=\sqrt{2GM/r_s}=c$. $r_s=2GM/c^2$. For the Sun: $r_s=2\times6.674\times10^{-11}\times2\times10^{30}/(3\times10^8)^2=2967$ m $\approx3$ km. For a $10M_\odot$ black hole: $r_s\approx30$ km. For a $10^9M_\odot$ supermassive black hole: $r_s\approx3\times10^{12}$ m $=20$ AU.

**Significance.** This is the event horizon of a black hole — the radius from within which nothing, not even light, can escape. The Newtonian derivation gives the correct result, which is a remarkable coincidence.

</details>

### OL8 — Effective potential and orbit shapes

For a particle in a gravitational field with angular momentum $L$, find the effective potential and determine the conditions for circular, elliptical, parabolic and hyperbolic orbits.

<details><summary>Solution</summary>

**Method.** $U_{\text{eff}}(r)=-GMm/r+L^2/(2mr^2)$. The minimum occurs at $r_0=L^2/(GMm^2)$. At the minimum: $U_{\text{eff,min}}=-G^2M^2m^3/(2L^2)$. For $E=U_{\text{eff,min}}$: circular orbit (radius $r_0$). For $U_{\text{eff,min}}<E<0$: elliptical orbit (two turning points). For $E=0$: parabolic orbit (one turning point at $r_{\min}$, escape at infinity). For $E>0$: hyperbolic orbit (one turning point, excess speed at infinity).

</details>

### OL9 — Lagrange points

A small body sits at the L1 Lagrange point between the Earth and the Sun. Show that the L1 point is closer to the Earth than the Earth–Sun distance.

<details><summary>Solution</summary>

**Method.** At L1, the gravitational pulls of the Sun and Earth, plus the centrifugal force in the rotating frame, balance. The Sun's pull: $GM_\odot/r^2$. The Earth's pull: $GM_E/d^2$ (where $d$ is the distance from Earth). The centrifugal acceleration: $\omega^2 r$ (where $\omega$ is the orbital angular velocity). The balance condition is approximately: $r_1\approx R(1-(M_E/(3M_\odot))^{1/3})$. For Earth–Sun: $r_1\approx1.5\times10^6$ km from Earth — about 1% of the Earth–Sun distance.

</details>

### OL10 — The virial theorem applied to galaxy clusters

A galaxy cluster has velocity dispersion $\sigma=1000$ km/s and radius $R=1$ Mpc. Estimate the cluster mass.

<details><summary>Solution</summary>

**Method.** By the virial theorem: $2\langle K\rangle=-\langle U\rangle$. $\langle K\rangle=\frac{1}{2}M\sigma^2$, $\langle U\rangle=-GM^2/R$. So $M\sigma^2=GM^2/R$, $M=R\sigma^2/G$. $M=3.086\times10^{22}\times(10^6)^2/6.674\times10^{-11}=4.6\times10^{44}$ kg $\approx2\times10^{14}M_\odot$. This is typical for galaxy clusters — and it is much larger than the visible mass, providing evidence for dark matter.

</details>

> [!abstract] DIAGRAM D9.10 · The effective potential curve for gravitational orbits
> *Show:* $U_{\text{eff}}(r)=-GMm/r+L^2/(2mr^2)$ plotted vs $r$. The minimum at $r_0$ marked. Four horizontal lines: $E=E_{\min}$ (circular), $E_{\min}<E<0$ (elliptical, two turning points), $E=0$ (parabolic), $E>0$ (hyperbolic).
> *Search:* "effective potential gravitational orbit circular elliptical parabolic hyperbolic diagram"

> [!abstract] DIAGRAM D9.11 · The Lagrange points of the Sun–Earth system
> *Show:* the Sun and Earth with the five Lagrange points (L1–L5) marked. L1 between them, L2 beyond Earth, L3 opposite Earth, L4 and L5 at the equilateral-triangle points ($60°$ ahead and behind).
> *Search:* "Lagrange points Sun Earth system L1 L2 L3 L4 L5 diagram"

> [!abstract] DIAGRAM D9.12 · The gravity-assist slingshot in the Sun's frame
> *Show:* Jupiter moving in its orbit. A spacecraft approaches from behind, swings around Jupiter, and leaves with higher speed in the Sun's frame. The spacecraft's trajectory curved by Jupiter's gravity. The velocity vectors before and after shown in both Jupiter's frame and the Sun's frame.
> *Search:* "gravity assist slingshot spacecraft Jupiter velocity change diagram"

### 10.2 Limits and failure of the model

Newtonian gravity is exact for weak fields and low speeds ($v\ll c$). In strong fields (near black holes), general relativity is needed. In quantum mechanics, gravity is thought to be mediated by gravitons — but a complete quantum theory of gravity does not yet exist. For JEE and INPhO, Newtonian gravity is sufficient for all problems. IPhO may occasionally probe relativistic corrections (e.g., GPS satellite timing), but these are rare.

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
The gravitational field inside a uniform hollow sphere is:
(a) $GM/R^2$ (b) $GM/(R^2-r^2)$ (c) zero (d) $GMr/R^3$

<details><summary>Answer</summary>

(c). By the shell theorem, the field inside a uniform hollow sphere is zero.

</details>

### P2 · 4 marks
The escape velocity from a planet of mass $M$ and radius $R$ is:
(a) $\sqrt{GM/R}$ (b) $\sqrt{2GM/R}$ (c) $GM/R$ (d) $2GM/R$

<details><summary>Answer</summary>

(b). $v_{\text{esc}}=\sqrt{2GM/R}$.

</details>

### P3 · 4 marks
The gravitational potential energy of a mass $m$ at distance $r$ from a mass $M$ (reference at infinity) is:
(a) $GMm/r$ (b) $-GMm/r$ (c) $-GMm/r^2$ (d) $GMm/r^2$

<details><summary>Answer</summary>

(b). $U=-GMm/r$ with reference at infinity.

</details>

### P4 · 4 marks
At the centre of a uniform Earth, $g$ is:
(a) $GM/R^2$ (b) $GM/(2R^2)$ (c) zero (d) infinite

<details><summary>Answer</summary>

(c). $g=GMr/R^3$, and at $r=0$, $g=0$.

</details>

### P5 · 4 marks
A satellite in a circular orbit loses energy (e.g., due to drag). It:
(a) moves to a higher orbit (b) moves to a lower orbit and speeds up (c) slows down (d) remains in the same orbit

<details><summary>Answer</summary>

(b). Losing energy makes the orbit lower (more negative $E$) and the speed higher.

</details>

### P6 · 4 marks
Kepler's second law is a consequence of:
(a) energy conservation (b) angular momentum conservation (c) the inverse-square law (d) Newton's third law

<details><summary>Answer</summary>

(b). Equal areas in equal times is equivalent to $dA/dt=L/(2m)=$ const, which is angular momentum conservation.

</details>

### P7 · 4 marks
The period of a geostationary satellite is:
(a) 12 hours (b) 24 hours (c) 365 days (d) 1 year

<details><summary>Answer</summary>

(b). 24 hours — the satellite must appear stationary in the sky.

</details>

### P8 · 4 marks
The energy of a satellite in a circular orbit of radius $r$ is:
(a) $-GMm/r$ (b) $-GMm/(2r)$ (c) $GMm/(2r)$ (d) zero

<details><summary>Answer</summary>

(b). $E=-GMm/(2r)$ — half the PE (virial theorem for circular orbits).

</details>

### P9 · 4 marks
The gravitational field at depth $d$ inside a uniform sphere is:
(a) $g(1+d/R)$ (b) $g(1-d/R)$ (c) $g(1-d/R)^2$ (d) $g$

<details><summary>Answer</summary>

(b). $g'=g(1-d/R)$ — linear decrease with depth.

</details>

### P10 · 4 marks
The Moon's tidal force on Earth is approximately how many times the Sun's?
(a) 0.01 (b) 0.5 (c) 2.2 (d) 100

<details><summary>Answer</summary>

(c). The Moon's tidal force is about 2.2 times the Sun's (despite the Sun's much larger mass, the Moon is much closer).

</details>

### P11 · 4 marks
For a binary star system, Kepler's third law becomes $T^2=4\pi^2 a^3/(G(m_1+m_2))$. What is $a$?
(a) The distance from the star to the COM (b) The semi-major axis of the relative orbit (c) The average separation (d) The radius of the larger star

<details><summary>Answer</summary>

(b). $a$ is the semi-major axis of the relative orbit (the orbit of one star relative to the other).

</details>

### P12 · 4 marks
The vis-viva equation $v^2=GM(2/r-1/a)$ gives the speed:
(a) only at perigee (b) only at apogee (c) at any point in an elliptical orbit (d) only for circular orbits

<details><summary>Answer</summary>

(c). The vis-viva equation is valid at any point $r$ in the orbit with semi-major axis $a$.

</details>

#### Section B · One-or-more-correct (8 × 4)

### P13 · 4 marks
Which of the following quantities are the same for all satellites in circular orbits around the same planet at the same altitude?
(a) Speed (b) Period (c) Kinetic energy (d) Angular momentum

<details><summary>Answer</summary>

(a), (b). Speed and period depend only on $r$ (and $M$), not on $m$. KE and $L$ depend on $m$.

</details>

### P14 · 4 marks
Which of the following are consequences of the inverse-square law?
(a) Kepler's first law (elliptical orbits) (b) Kepler's second law (equal areas) (c) Kepler's third law ($T^2\propto a^3$) (d) The shell theorem

<details><summary>Answer</summary>

(a), (c), (d). Kepler's second law follows from angular momentum conservation (any central force), not specifically from $1/r^2$. The other three require the inverse-square form.

</details>

### P15 · 4 marks
For which of the following orbits is $E<0$?
(a) Circular (b) Elliptical (c) Parabolic (d) Hyperbolic

<details><summary>Answer</summary>

(a), (b). Bound orbits have $E<0$. Parabolic orbits have $E=0$. Hyperbolic orbits have $E>0$.

</details>

### P16 · 4 marks
Which of the following are required for a satellite to be geostationary?
(a) Orbit in the equatorial plane (b) Period of 24 hours (c) Circular orbit (d) Altitude of 35,786 km

<details><summary>Answer</summary>

(a), (b), (c), (d). All four are necessary.

</details>

### P17 · 4 marks
The Schwarzschild radius $r_s=2GM/c^2$. For which of the following is $r_s$ well-defined?
(a) The Sun (b) The Earth (c) A neutron star (d) All massive objects

<details><summary>Answer</summary>

(d). The Schwarzschild radius is defined for any mass. Whether the object is actually a black hole depends on whether its physical radius is less than $r_s$.

</details>

### P18 · 4 marks
A Hohmann transfer between two circular orbits requires:
(a) Two engine burns (b) An elliptical transfer orbit (c) Less energy than a direct transfer (d) A parabolic transfer orbit

<details><summary>Answer</summary>

(a), (b), (c).

</details>

### P19 · 4 marks
For an elliptical orbit, which quantities are constant?
(a) Speed (b) Angular momentum (c) Total energy (d) Distance from the focus

<details><summary>Answer</summary>

(b), (c).

</details>

### P20 · 4 marks
The Roche limit depends on:
(a) The planet's density (b) The satellite's density (c) The planet's radius (d) The satellite's radius

<details><summary>Answer</summary>

(a), (b), (c). $d_{\text{Roche}}=2.44R_p(\rho_p/\rho_s)^{1/3}$.

</details>

#### Section C · Numerical answers (6 × 5)

### P21 · 5 marks
Find the orbital speed of a satellite at altitude 300 km above Earth's surface. ($R_E=6370$ km, $g_0=9.8$ m/s$^2$.) Give your answer in km/s.

<details><summary>Answer</summary>

$r=6670$ km. $v=\sqrt{g_0R_E^2/r}=\sqrt{9.8\times6370^2/6670}=7.73$ km/s.

</details>

### P22 · 5 marks
Find the escape velocity from Jupiter's surface. ($M_J=1.9\times10^{27}$ kg, $R_J=7.14\times10^7$ m.) Give your answer in km/s.

<details><summary>Answer</summary>

$v=\sqrt{2GM/R}=\sqrt{2\times6.674\times10^{-11}\times1.9\times10^{27}/7.14\times10^7}=59.6$ km/s.

</details>

### P23 · 5 marks
A satellite orbits at $r=3R_E$. Find the ratio of its total energy to that of a satellite at $r=R_E$ (both in circular orbits).

<details><summary>Answer</summary>

$E\propto-1/r$. $E_3/E_1=R_E/(3R_E)=1/3$.

</details>

### P24 · 5 marks
Find the geostationary orbit altitude above Earth. ($M_E=5.97\times10^{24}$ kg, $R_E=6370$ km.) Give your answer in km.

<details><summary>Answer</summary>

$r=(GMT^2/(4\pi^2))^{1/3}=42164$ km. Altitude $=42164-6370=35794$ km.

</details>

### P25 · 5 marks
Find the period of a binary star with $a=3$ AU and $M_{\text{total}}=2M_\odot$. Give your answer in years.

<details><summary>Answer</summary>

$T=a^{3/2}/M^{1/2}=3^{3/2}/2^{1/2}=5.196/1.414=3.67$ years.

</details>

### P26 · 5 marks
Find $g$ at the surface of the Moon. ($M=7.35\times10^{22}$ kg, $R=1.74\times10^6$ m.) Give your answer in m/s$^2$.

<details><summary>Answer</summary>

$g=GM/R^2=6.674\times10^{-11}\times7.35\times10^{22}/(1.74\times10^6)^2=1.62$ m/s$^2$.

</details>

#### Section D · Long-form (10 × 9)

### P27 · 9 marks
Derive the expression for $g(r)$ inside a uniform sphere of radius $R$ and total mass $M$. Show that $g=0$ at the centre and $g=GM/R^2$ at the surface.

<details><summary>Solution</summary>

**Method.** At distance $r$ from the centre, the enclosed mass is $M(r)=M(r/R)^3$ (by the shell theorem, only the mass inside $r$ contributes). $g(r)=GM(r)/r^2=GMr/R^3$. At $r=0$: $g=0$. At $r=R$: $g=GM/R^2$. The field increases linearly from 0 to the surface value.

</details>

### P28 · 9 marks
A satellite is in an elliptical orbit with perigee $r_p=7000$ km and apogee $r_a=42000$ km. Find the speed at perigee and apogee, and the orbital period.

<details><summary>Solution</summary>

**Method.** $a=(r_p+r_a)/2=24500$ km. $v_p=\sqrt{GM(2/r_p-1/a)}=\sqrt{3.986\times10^{14}(2/7\times10^6-1/2.45\times10^7)}=\sqrt{3.986\times10^{14}\times2.45\times10^{-7}}=9.89$ km/s. $v_a=\sqrt{GM(2/r_a-1/a)}=\sqrt{3.986\times10^{14}\times6.8\times10^{-9}}=1.65$ km/s. $T=2\pi\sqrt{a^3/GM}=2\pi\times(2.45\times10^7)^{3/2}/\sqrt{3.986\times10^{14}}=38550$ s $=10.7$ h.

</details>

### P29 · 9 marks
Derive the escape velocity from energy conservation. Show that $v_{\text{esc}}=\sqrt{2}\,v_{\text{orb}}$.

<details><summary>Solution</summary>

**Method.** At the surface: $E=\frac{1}{2}mv_{\text{esc}}^2-GMm/R$. At infinity: $E=0$ (just barely escapes). Setting $\frac{1}{2}mv_{\text{esc}}^2=GMm/R$: $v_{\text{esc}}=\sqrt{2GM/R}$. For a circular orbit at the surface: $v_{\text{orb}}=\sqrt{GM/R}$. So $v_{\text{esc}}=\sqrt{2}\,v_{\text{orb}}$.

</details>

### P30 · 9 marks
A binary star system has masses $m_1=3M_\odot$ and $m_2=1M_\odot$, separated by $a=4$ AU. Find the orbital period and the distance of each star from the COM.

<details><summary>Solution</summary>

**Method.** $T=\sqrt{a^3/(m_1+m_2)}=\sqrt{64/4}=4$ years. $a_1=a\times m_2/(m_1+m_2)=4\times1/4=1$ AU. $a_2=3$ AU. The heavier star is closer to the COM.

</details>

### P31 · 9 marks
Explain the mechanism of a gravity-assist manoeuvre. A spacecraft approaches Jupiter from behind (in Jupiter's orbital direction). Does it gain or lose speed in the Sun's frame?

<details><summary>Solution</summary>

**Method.** In Jupiter's rest frame, the spacecraft's speed is unchanged (elastic gravitational scattering). In the Sun's frame: if the spacecraft approaches from behind, its Sun-frame speed is $v_s+v_J$. After the encounter, the spacecraft is deflected and leaves Jupiter's vicinity at speed $v_s$ in Jupiter's frame — but in a direction that adds to Jupiter's velocity. In the Sun's frame: $v_{\text{after}}=2v_J+v_s$. The spacecraft gains $2v_J$.

</details>

### P32 · 9 marks
A planet has density $\rho$ and radius $R$. Show that the surface gravity $g=\frac{4}{3}\pi G\rho R$ and the escape velocity $v_{\text{esc}}=\sqrt{8\pi G\rho R^2/3}$.

<details><summary>Solution</summary>

**Method.** $M=\frac{4}{3}\pi R^3\rho$. $g=GM/R^2=\frac{4}{3}\pi G\rho R$. $v_{\text{esc}}=\sqrt{2GM/R}=\sqrt{2G\frac{4}{3}\pi R^3\rho/R}=\sqrt{8\pi G\rho R^2/3}$.

</details>

### P33 · 9 marks
Derive the effective potential for a particle in a gravitational field with angular momentum $L$. Find the radius of the circular orbit and the minimum energy.

<details><summary>Solution</summary>

**Method.** $U_{\text{eff}}(r)=-GMm/r+L^2/(2mr^2)$. $dU_{\text{eff}}/dr=GMm/r^2-L^2/(mr^3)=0$. $r_0=L^2/(GMm^2)$. $U_{\text{eff,min}}=-GMm/r_0+L^2/(2mr_0^2)=-G^2M^2m^3/(2L^2)$. The minimum energy for a bound orbit is $E_{\min}=-G^2M^2m^3/(2L^2)$.

</details>

### P34 · 9 marks
A spacecraft is in a circular orbit of radius $r_1$ around a planet. It performs a Hohmann transfer to a circular orbit of radius $r_2>r_1$. Derive the two $\Delta v$ values.

<details><summary>Solution</summary>

**Method.** Transfer ellipse: $a=(r_1+r_2)/2$. At perigee: $v_p=\sqrt{GM(2/r_1-1/a)}=\sqrt{2GMr_2/(r_1(r_1+r_2))}$. Circular speed at $r_1$: $v_1=\sqrt{GM/r_1}$. $\Delta v_1=v_p-v_1=\sqrt{GM/r_1}(\sqrt{2r_2/(r_1+r_2)}-1)$. At apogee: $v_a=\sqrt{2GMr_1/(r_2(r_1+r_2))}$. Circular speed at $r_2$: $v_2=\sqrt{GM/r_2}$. $\Delta v_2=v_2-v_a=\sqrt{GM/r_2}(1-\sqrt{2r_1/(r_1+r_2)})$.

</details>

### P35 · 9 marks
Estimate the tidal force of the Moon on Earth. If the Moon were twice as close, how would the tidal force change?

<details><summary>Solution</summary>

**Method.** $F_{\text{tidal}}=2GM_{\text{Moon}}m r_E/d^3$. With $d=3.84\times10^8$ m, $r_E=6.37\times10^6$ m: $F_{\text{tidal}}/m=2\times6.674\times10^{-11}\times7.35\times10^{22}\times6.37\times10^6/(3.84\times10^8)^3=1.1\times10^{-6}$ m/s$^2$. If $d$ is halved: $F_{\text{tidal}}\propto1/d^3$, so the tidal force increases by $2^3=8$ times. This would cause catastrophic tides.

</details>

### P36 · 9 marks
A satellite of mass $m$ is in a circular orbit of radius $r$. It fires its engines radially inward, reducing its speed by a small amount $\Delta v$. Describe the resulting orbit and find the new perigee.

<details><summary>Solution</summary>

**Method.** After the impulse: $v'=v-\Delta v$ where $v=\sqrt{GM/r}$. The new orbit is an ellipse with the current position as the apogee (the speed is now less than circular). Using angular momentum: $L'=m(v-\Delta v)r$. The new semi-major axis: $1/a'=2/r-v'^2/(GM)$. The new perigee: $r_p=2a'-r$. For small $\Delta v$: $r_p\approx r(1-4\Delta v/v)$ — the perigee is significantly lower.

</details>

## Part 12 · Marking scheme and post-paper audit

| Section | Questions | Marks each | Subtotal |
|---|---|---:|---:|
| A | P1–P12 | 4 | 48 |
| B | P13–P20 | 4 | 32 |
| C | P21–P26 | 5 | 30 |
| D | P27–P36 | 9 | 90 |
| Total | 36 | | 200 |

**Post-paper audit:** After completing the paper, check: (1) Did I answer every question? (2) For Section A, did I guess or skip? ($-1$ for wrong, so skip if unsure.) (3) For Section C, are my numerical answers in the correct units? (4) For Section D, did I show all steps? (partial credit is available.)

## Part 13 · Formula sheet

| Formula | Validity |
|---|---|
| $F=GMm/r^2$ | inverse-square law |
| $g=GMr/R^3$ (inside), $g=GM/r^2$ (outside) | uniform sphere |
| $V=-GM/r$ | gravitational potential |
| $U=-GMm/r$ | reference at infinity |
| $v_{\text{esc}}=\sqrt{2GM/R}$ | from surface |
| $v=\sqrt{GM/r}$ | circular orbit |
| $E=-GMm/(2r)$ | circular orbit |
| $v^2=GM(2/r-1/a)$ | vis-viva |
| $T^2=4\pi^2 a^3/(GM)$ | Kepler's third law |
| $r_{\text{geo}}=(GMT^2/(4\pi^2))^{1/3}$ | geostationary |
| $d_{\text{Roche}}=2.44R_p(\rho_p/\rho_s)^{1/3}$ | Roche limit |

## Part 14 · Checkpoint and hand-off

### 14.1 Mastery checklist

- [ ] I can prove the shell theorem (by integration and by Gauss's law).
- [ ] I can compute $g$ inside/outside spheres, shells and cavities.
- [ ] I can derive all four $g$ variations (altitude, depth, latitude, rotation).
- [ ] I can use $U=-GMm/r$ and the vis-viva equation.
- [ ] I can derive Kepler's three laws.
- [ ] I can solve geostationary-orbit and Hohmann-transfer problems.
- [ ] I can analyse binary stars and gravity-assist manoeuvres.
- [ ] I understand tidal forces and the Roche limit.
- [ ] I can apply the virial theorem to bound systems.
- [ ] I can derive the Schwarzschild radius and the Lagrange points.

### 14.2 What comes next

PART 10 (Simple Harmonic Motion) uses the energy methods from this chapter (specifically, $U(x)$ and $F=-dU/dx$) to study oscillations about equilibrium. The concept of stable equilibrium ($U''>0$) is the foundation of SHM. The orbital mechanics from this chapter also connects to PART 24 (Electrostatics), where the $1/r^2$ force gives the same orbital physics but with opposite sign for like charges.
