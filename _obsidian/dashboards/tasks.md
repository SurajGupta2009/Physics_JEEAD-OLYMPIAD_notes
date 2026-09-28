# Task queue — plan mirror

> Live mirror of [`plan.md`](../../plan.md) and [`PENDING.md`](../../PENDING.md). The rows below
> are the **unwritten** chapters still on the plan (details, order and dependencies in
> [pending.md](pending.md)); tick them off here only as bookkeeping — the registry
> (`topics.json` `status`) is the source of truth.

## Chapters (PART 13–22, Electricity & Magnetism)

- [x] `electrostatics` — plan.md PART 13 + 14 + 15 as one module (all three stages shipped 2026-09-27)
- [x] `magnetism` — plan.md PART 16 + 17 + 18 + 19 as one module (all three stages shipped 2026-09-27)
- [/] `emi-ac` — plan.md PART 20 + 21 + 22 as one module: stage 1 (theory) done; stage 2 (exemplars, practice, toolkit, traps, playbook) and stage 3 (Olympiad block, paper, formula sheet, checkpoint) open

## Repository chores

- [ ] run `python3 tools/obsidian_plugins.py` once on a machine with internet, then commit `.obsidian/plugins/*/{main.js,manifest.json,styles.css}` so the vault works out of the box (`.obsidian/README` section of [`_obsidian/README.md`](../README.md))
- [ ] when `emi-ac` reaches stage 3: mark plan.md complete in [PENDING.md](../../PENDING.md), regenerate `docs/site/` (`python3 tools/md_site.py`)

**Shipped** (do not re-queue): 30 of the 31 topics registered in `topics.json` have status `complete` —
PART 1–12, PART 13–15 (as `electrostatics`), PART 16–19 (as `magnetism`), PART 23–28, the nine original note-sets and `communication-systems`.

## Every open checkbox in the vault (Tasks plugin)

```tasks
not done
path does not include _templates
path does not include docs/
group by folder
```
