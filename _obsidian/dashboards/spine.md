# Reading spine

The canonical cross-topic order (mirrors `README.md` / `CURRICULUM.md`): the wave spine first,
then the thermal/material spine, then geometrical optics — part 1 → part 9 in `topics.json`.

```dataview
TABLE part AS "Part", status AS "Status"
FROM #jee-advanced OR #olympiad
WHERE part >= 1 AND part <= 9
SORT part ASC
```

Then the mechanics and modern-physics chapters by their own part numbers:

```dataview
TABLE part AS "Part", status AS "Status"
WHERE part >= 10
SORT part ASC
```

> The parts 1–30 numbering is the `plan.md` protocol number. The wave spine reads
> **string waves → sound waves → electromagnetic waves → wave optics**, then
> **thermodynamics → heat → capacitors → current electricity → geometrical optics**.
