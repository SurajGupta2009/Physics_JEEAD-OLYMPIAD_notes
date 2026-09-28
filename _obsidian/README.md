# _obsidian — the vault home

> **What this folder is.** The human-facing half of the Obsidian harness, per
> [`docs/obsidian-plugin-workflow.md`](../docs/obsidian-plugin-workflow.md) §7.5: the live
> dashboards, the chapter template and the LaTeX Suite snippet set. The machine half — Obsidian's
> own settings, the enabled-plugin list, every plugin's configuration and the CSS snippet — is the
> hidden **`.obsidian/`** directory at the repository root, and it is committed on purpose so the
> vault opens configured.
>
> **Open this vault** by pointing Obsidian at the repository root (*Open folder as vault* →
> `Physics_JEEAD-OLYMPIAD_notes`). When it asks, choose **Trust author and enable plugins**. The
> chapter notes are the `<topic>/<Title>.md` files; the five Cengage PDFs open in Obsidian's own PDF
> viewer, so "sweep the book" (plan.md §1.12) happens without leaving the vault.

## Reading order

The course spine — mechanics → waves → thermal → electricity & magnetism → EM waves → optics →
modern — is **[dashboards/spine.md](dashboards/spine.md)**. Every chapter's frontmatter carries its
slot as `order:` (1–31) and its syllabus `block:`; the Dataview tables sort on those, and
`tools/check_all.py` keeps them equal to `topics.json`.

## Dashboards

| view | file | what it shows |
|---|---|---|
| Reading spine | [dashboards/spine.md](dashboards/spine.md) | the 31-slot course order with the one-line reason for each position |
| Library | [dashboards/README.md](dashboards/README.md) | every chapter by order and by block, self-clearing "missing properties" list |
| Pending chapters | [dashboards/pending.md](dashboards/pending.md) | the delivery record of the E&M block (nothing unwritten), batches, definition of done |
| Task queue | [dashboards/tasks.md](dashboards/tasks.md) | checkbox mirror of plan/PENDING + every open task in the vault |

## Authoring harness

| file | consumed by | purpose |
|---|---|---|
| [templates/chapter.md](templates/chapter.md) | Templater (folder is pre-configured) | the full 15-block skeleton for a new chapter — *Templater: Insert template* |
| [latex-suite/snippets.js](latex-suite/snippets.js) · [latex-suite/README.md](latex-suite/README.md) | LaTeX Suite (path is pre-configured) | default snippet set + the vault's physics shorthands and callout skeletons |
| `excalidraw/` (created on first drawing) | Excalidraw | scratch drawings; export the finished figure as SVG into `<topic>/assets/figures/` |

## The `.obsidian/` configuration (committed)

| file | what it sets |
|---|---|
| `app.json` | reading mode by default, readable line length, Markdown links (relative), attachments to `./assets/figures`, unsupported files hidden, `docs/site/`, `_templates/`, `tools/` excluded from search and graph |
| `appearance.json` | system light/dark, base font 16, CSS snippet `physics-notes` enabled |
| `core-plugins.json` | outline, backlinks, tags, properties, canvas, bookmarks, word count, file recovery on; daily notes, slides, sync, publish off |
| `community-plugins.json` | the eight plugins below, enabled |
| `plugins/<id>/data.json` | each plugin's settings, already pointed at this vault's files |
| `plugins.lock.json` | the pinned plugin versions read by `tools/obsidian_plugins.py` |
| `snippets/physics-notes.css` | wider maths column, framed Mermaid figures, dashed `DIAGRAM` slots, styled `<details>` solutions, scrollable tables and display maths, print rules |

Per-device state (`workspace.json`, `workspace-mobile.json`, `cache`) is git-ignored.

### Plugins

| plugin | id · pinned | tier | role in this vault |
|---|---|:-:|---|
| **Dataview** | `dataview` · 0.5.70 | 1 | the dashboards above; frontmatter is the vault's metadata. DataviewJS is off (nothing needs it) |
| **Templater** | `templater-obsidian` · 2.25.1 | 1 | template folder = `_obsidian/templates` |
| **LaTeX Suite** | `obsidian-latex-suite` · 1.13.3 | 1 | snippets from `_obsidian/latex-suite/snippets.js`; auto-fraction, matrix shortcuts, tab-out, conceal, bracket colouring |
| **Git** | `obsidian-git` · 2.40.0 | 1 | source-control pane, history, blame; **auto-commit 15 min after the last edit, no auto-push** — push is an explicit command (*Git: Push*); pulls on start |
| **Advanced Tables** | `table-editor-obsidian` · 0.23.2 | 4 | aligned pipe tables, `Tab`/`Enter` cell navigation, sort, CSV export |
| **Spaced Repetition** | `obsidian-spaced-repetition` · 1.15.4 | 1 | `==cloze==` and `::` cards — **opt-in per note**: add `#flashcards` to a note's tags and its boxed results become a deck (nothing is scanned otherwise) |
| **Tasks** | `obsidian-tasks-plugin` · 8.4.0 | 4 | the pending queue and Part 14 checkpoints as live task lists; no global filter |
| **Excalidraw** | `obsidian-excalidraw-plugin` · 2.27.3 | 2 | hand-drawn diagrams (ray diagrams, free-body diagrams, circuits); drawings live in `_obsidian/excalidraw/`, the committed figure is the exported **SVG** |

Mermaid (the figure system of plan.md §1.2), Canvas, checklists, properties and the PDF viewer are
**core Obsidian** — nothing to install.

### Finishing the install (one command, once)

Obsidian does not download plugins from a config list; the plugin files are GitHub release
artefacts. From the repository root, on a machine with internet:

```bash
python3 tools/obsidian_plugins.py            # fetches main.js / manifest.json / styles.css at the pinned versions
python3 tools/obsidian_plugins.py --check    # shows what is installed
git add .obsidian/plugins && git commit -m "vault: vendor the pinned Obsidian plugins"
```

The vault configuration and content are committed, and the five Cengage PDFs are tracked in the repository; those source books are an intentional part of the project, not optional external dependencies. Community-plugin binaries are separate release artefacts: until they are vendored, each clone must complete the one-time install above (or install the eight listed plugins through Obsidian's *Settings → Community plugins → Browse*). The committed `data.json` settings are picked up either way. Do not remove the tracked Cengage PDFs or treat the Obsidian vault as optional. `--latest` re-pins to the
newest releases and updates `plugins.lock.json`.

### Vault conventions the plugins rely on

- Chapters are written for **reading mode**: YAML frontmatter, the eight callout roles, `$…$` /
  `$$…$$`, `<details>` solutions with blank lines inside, `> [!tip] FIGURE` + ` ```mermaid `,
  `> [!abstract] DIAGRAM` briefs. HTML beyond `<details>/<summary>/<br>` is banned
  (docs/obsidian-plugin-workflow.md §3).
- Links are standard Markdown links (relative paths), so the same files render on GitHub.
- New attachments land in `./assets/figures` next to the note (app setting) — only SVG is committed.
- Dataview lives in this folder's dashboards, never inside a chapter.
