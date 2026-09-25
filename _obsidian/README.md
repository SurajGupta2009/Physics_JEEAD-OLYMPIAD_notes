# _obsidian — the vault home

> **What this folder is.** The Obsidian-native harness for the whole vault, per
> [`docs/obsidian-plugin-workflow.md`](../docs/obsidian-plugin-workflow.md) §7.5:
> the shared snippets, the chapter template, and the live dashboards. Chapters share the same
> frontmatter schema, so the dashboards resolve without special-casing any topic.
>
> **Open this vault** by pointing Obsidian at the repository root (`Physics_JEEAD-OLYMPIAD_notes`).
> The chapter notes are the `*/X.md` files at the top level; this folder only holds the
> authoring harness and the live views. Folders are backed by Dataview (Tier 1).

## Reading order (canonical spine)

| # | chapter | part | file | status |
|---:|---|---|---|---|
| 1 | String Waves | 1 | [`string-waves/String-waves.md`](../string-waves/String-waves.md) | complete |
| 2 | Sound Waves & Doppler | 2 | [`sound-waves/Sound-waves.md`](../sound-waves/Sound-waves.md) | complete |
| 3 | Electromagnetic Waves | 3 | [`electromagnetic-waves/Electromagnetic-waves.md`](../electromagnetic-waves/Electromagnetic-waves.md) | complete |
| 4 | Wave Optics | 4 | [`wave-optics/Wave-optics.md`](../wave-optics/Wave-optics.md) | complete |
| 5 | Thermodynamics | 5 | [`thermodynamics/Thermodynamics.md`](../thermodynamics/Thermodynamics.md) | complete |
| 6 | Heat | 6 | [`heat/Heat.md`](../heat/Heat.md) | complete |
| 7 | Capacitors | 7 | [`capacitors/Capacitors.md`](../capacitors/Capacitors.md) | complete |
| 8 | Current Electricity | 8 | [`current-electricity/Current-electricity.md`](../current-electricity/Current-electricity.md) | complete |
| 9 | Geometrical Optics | 9 | [`geometrical-optics/Geometrical-optics.md`](../geometrical-optics/Geometrical-optics.md) | complete |

*The wave spine (parts 1–4) precedes the thermal/material spine (parts 5–8); both feed
geometrical optics (part 9), per `CURRICULUM.md`. The mechanics (parts 1–10 per `plan.md`) and
modern-physics (parts 23–28) chapters are listed by part in the dashboards below.*

## Dashboards

| view | file | what it shows |
|---|---|---|
| Master index | [dashboards/README.md](dashboards/README.md) | every chapter by part, status, links, paper endpoint |
| Reading spine | [dashboards/spine.md](dashboards/spine.md) | the canonical cross-topic order |
| Task queue | [dashboards/tasks.md](dashboards/tasks.md) | live mirror of plan/PENDING work |

## Authoring harness

| file | consumed by | purpose |
|---|---|---|
| [templates/chapter.md](templates/chapter.md) | Templater | the full 15-block skeleton for a new chapter |
| [latex-suite/snippets.md](latex-suite/snippets.md) | LaTeX Suite | curated `$…$`/`$$…$$` shorthand |

Load the snippet file once in **LaTeX Suite → Settings → "Load snippets from file or folder"** and
set **Templater → template folder** to `_obsidian/templates`. Plugin list and setup order are in
[`docs/obsidian-plugin-workflow.md`](../docs/obsidian-plugin-workflow.md) §4 and §9.3.
