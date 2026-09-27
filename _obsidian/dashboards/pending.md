# Pending chapters — live queue

> Mirror of [PENDING.md](../../PENDING.md) (the canonical list, kept in sync with `topics.json`).
> Seven chapters remain, all in **Electricity & Magnetism** (plan.md PART 16–22); PART 13–15 are
> in progress as the single `electrostatics/` module (stage 1 of 3 — theory — done). Mechanics
> (PART 1–12) and Modern Physics (PART 23–28) are complete. Tick a box here as bookkeeping only —
> the registry (`topics.json` → `status`) is the source of truth.

## Write in this order

Each row depends on the one above it (the dependency *is* the teaching order). `order` is the
course-spine slot the chapter takes in [spine.md](spine.md); `size` is plan.md §5.3's word band.

- [/] **PART 13 + 14 + 15** · [`electrostatics`](../../electrostatics/Electrostatics.md) · Electrostatics — first principles to Olympiad · order 17 · one merged chapter in three stages · Cengage *Electrostatics* ch 1–3 ✅ PDF in repo
    - [x] stage 1 · Parts 0–3 · the complete theory in teaching order (§3.1–§3.37) ✅ 2026-09-27
    - [ ] stage 2 · Parts 4–9 · validity ledger, E1–E20, archetypes + Q1–Q50, toolkit, traps, playbook
    - [ ] stage 3 · Parts 10–14 · Olympiad extension OL1–OL12, the 36-question / 200-mark paper, formula sheet, checkpoint
- [ ] **PART 16** · `magnetic-field` · Magnetic Field, Biot–Savart & the Lorentz Force · order 20 · large · needs electrostatics (13–15) · no PDF — standard JEE Advanced headings
- [ ] **PART 17** · `amperes-law` · Ampère's Law, Currents & Magnetic Dipoles · order 21 · standard · needs 16 · no PDF
- [ ] **PART 18** · `moving-charges-magnetism` · Cyclotron, Velocity Selector & the Hall Effect · order 22 · standard · needs 17 · no PDF
- [ ] **PART 19** · `magnetism-and-matter` · Magnetism & Matter, Earth's Magnetism · order 23 · compact (9–13k) · needs 17 · no PDF
- [ ] **PART 20** · `electromagnetic-induction` · Faraday, Lenz, Motional EMF & Eddy Currents · order 24 · standard · needs 17 · no PDF
- [ ] **PART 21** · `inductance` · Self & Mutual Inductance, RL Circuits & Magnetic Energy · order 25 · standard · needs 20 · no PDF
- [ ] **PART 22** · `alternating-current` · Alternating Current, Resonance & Transformers · order 26 · large · needs 21 · no PDF

Batches that may run in parallel (plan.md §0.4): **13 + 14 + 15** as one module (stages 2 and 3 left); **16 → 17**, then **18 ∥ 19**;
**20 → 21 → 22 is one continuous argument — never split it across writers.**

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
