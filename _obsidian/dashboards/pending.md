# Pending chapters — live queue

> Mirror of [PENDING.md](../../PENDING.md) (the canonical list, kept in sync with `topics.json`).
> No chapter is unclaimed. PART 13–15 shipped as the single `electrostatics/` module, PART 16–19 as the
> single `magnetism/` module, and PART 20–22 (induction → inductance → AC) are in progress as the
> single `emi-ac/` module (stage 1 of 3 — theory — done). Mechanics (PART 1–12) and Modern Physics
> (PART 23–28) are complete. Tick a box here as bookkeeping only —
> the registry (`topics.json` → `status`) is the source of truth.

## Write in this order

Each row depends on the one above it (the dependency *is* the teaching order). `order` is the
course-spine slot the chapter takes in [spine.md](spine.md); `size` is plan.md §5.3's word band.

- [x] **PART 13 + 14 + 15** · [`electrostatics`](../../electrostatics/Electrostatics.md) · Electrostatics — first principles to Olympiad · order 17 · one merged chapter, three stages, all shipped 2026-09-27 · Cengage *Electrostatics* ch 1–3 ✅ PDF in repo
- [x] **PART 16 + 17 + 18 + 19** · [`magnetism`](../../magnetism/Magnetism.md) · Magnetism — from the Lorentz force to the Earth's field · order 20 · one merged chapter, three stages, all shipped 2026-09-27 · no PDF — standard JEE Advanced headings
- [/] **PART 20 + 21 + 22** · [`emi-ac`](../../emi-ac/Emi-ac.md) · Induction, inductance and alternating current — one continuous argument · order 21 · one merged chapter in three stages · no PDF — standard JEE Advanced headings
    - [x] stage 1 · Parts 0–3 · the complete theory in teaching order (§3.1–§3.36) ✅ 2026-09-27
    - [ ] stage 2 · Parts 4–9 · validity ledger, C1–C14, E1–E20, archetypes + Q1–Q60, toolkit, traps, playbook
    - [ ] stage 3 · Parts 10–14 · Olympiad extension OL1–OL12, the 36-question / 200-mark paper, formula sheet, checkpoint

Batches that may run in parallel (plan.md §0.4): **13 + 14 + 15** shipped as one module; **16 + 17 + 18 + 19** shipped as one module;
**20 + 21 + 22** as one module too (stages 2 and 3 left) — the plan's one-continuous-argument rule, honoured by merging.

## What "done" means for each

Every pending chapter is written to the same contract as the 18 finished plan.md chapters:

1. the **15-block spine** (plan.md §1.4): orientation → intuition → definitions → core derivations →
   validity ledger → worked exemplars → practice archetypes → JEE toolkit → traps → playbook →
   Olympiad extension → 36-question, 200-mark, 3-hour paper → marking scheme → formula sheet →
   checkpoint;
2. **basics → JEE Advanced → Olympiad, with the worked problems interleaved**, and every "therefore"
   justified (CONTRIBUTING.md §3–§4);
3. Obsidian-native media: ≥ 6 Mermaid `FIGURE` callouts + `DIAGRAM` briefs, no image files
   (docs/obsidian-plugin-workflow.md §2);
4. frontmatter with `title / part / slug / order / block / status / source / aliases / tags`;
5. `python3 tools/check.py` green in the folder, `python3 tools/check_all.py --update` green at
   the root, a row in README.md, and the box above ticked.

## Registry view

Chapters are registered only once their folder exists, so this table fills in as they land:

```dataview
TABLE WITHOUT ID order AS "#", link(file.path, title) AS "Chapter", part AS "PART", status AS "Status"
FROM -"_obsidian" AND -"_templates" AND -"docs"
WHERE block = "electricity-magnetism"
SORT order ASC
```
