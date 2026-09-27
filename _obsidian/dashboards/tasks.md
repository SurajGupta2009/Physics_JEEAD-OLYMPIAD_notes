# Task queue — plan mirror

> Live mirror of [`plan.md`](../../plan.md) and [`PENDING.md`](../../PENDING.md). The rows below
> are the **unwritten** chapters still on the plan (details, order and dependencies in
> [pending.md](pending.md)); tick them off here only as bookkeeping — the registry
> (`topics.json` `status`) is the source of truth.

## Chapters (PART 13–22, Electricity & Magnetism)

- [ ] `electric-field` — plan.md PART 13
- [ ] `gauss-law` — plan.md PART 14
- [ ] `electric-potential` — plan.md PART 15
- [ ] `magnetic-field` — plan.md PART 16
- [ ] `amperes-law` — plan.md PART 17
- [ ] `moving-charges-magnetism` — plan.md PART 18
- [ ] `magnetism-and-matter` — plan.md PART 19
- [ ] `electromagnetic-induction` — plan.md PART 20
- [ ] `inductance` — plan.md PART 21
- [ ] `alternating-current` — plan.md PART 22

## Repository chores

- [ ] run `python3 tools/obsidian_plugins.py` once on a machine with internet, then commit `.obsidian/plugins/*/{main.js,manifest.json,styles.css}` so the vault works out of the box (`.obsidian/README` section of [`_obsidian/README.md`](../README.md))
- [ ] when PART 22 lands: mark plan.md complete in [PENDING.md](../../PENDING.md), regenerate `docs/site/` (`python3 tools/md_site.py`)

**Shipped** (do not re-queue): all 28 topics registered in `topics.json`, status `complete` —
PART 1–12, PART 23–28, the nine original note-sets and `communication-systems`.

## Every open checkbox in the vault (Tasks plugin)

```tasks
not done
path does not include _templates
path does not include docs/
group by folder
```
