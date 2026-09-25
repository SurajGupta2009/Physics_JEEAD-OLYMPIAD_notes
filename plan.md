# MASTER MULTI-AGENT PLAN — the remaining JEE Advanced / Olympiad chapters

> **Repository**: `Physics_JEEAD-OLYMPIAD_notes`
> **Audience**: JEE Advanced · NSEP · INPhO · IPhO aspirants
> **Standard**: ≥ Cengage floor + a dedicated Olympiad section + proof-first, teacher-ordered exposition
> **Media**: **Obsidian-native and deterministic** (see §1.2 and `docs/obsidian-plugin-workflow.md`).
> Figures are RENDERED, not AI-drawn: ` ```mermaid ` diagrams — mindmaps, flowcharts,
> `quadrantChart` sign-plots and `xychart-beta` data graphs — each wrapped in a `[!tip] FIGURE`
> callout with `*Why:*` / `*Data:*` / `*Read:*`. Runtime figures carry their seed as a
> searchable `> [!abstract] DIAGRAM` brief. **Banned:** AI raster art (PNG/JPG), AI hand-drawn SVG,
> external image URLs, ASCII art. Existing HTML-heritage topics keep their committed SVG sets.
> **Format**: Markdown written for **Obsidian reading mode** (§1.3.1): YAML frontmatter, Obsidian
> callouts, `$...$` / `$$...$$` math, `<details>` solutions, pipe tables, Mermaid figures.
> Markdown-first topics: no parallel HTML edition is required.
> **Completeness**: each chapter's section list below is a **floor, not a ceiling** — the agent must also
> sweep the Cengage chapter's own contents page (the PDFs live in this repo, §1.13) and add anything the
> plan misses (§1.12).
> **Cross-check**: the five Cengage volumes are committed in the repository root, so the Cengage floor can
> be verified, not assumed — including which volume really holds a chapter (§1.13).

---

## 0 · How to use this plan (the agent protocol)

### 0.1 What this file is, and what it replaces

* **This is plan v2.** It covers **everything still missing** from the repo, chapter by chapter.
  It replaces plan v1 (`docs/plan-v1-waves-optics.md`), whose four work packages
  (string waves → sound waves → electromagnetic waves → wave optics audit) are **complete on `main`**.
  Those nine finished note-sets are listed in **Appendix A**; they are *not* numbered here, so a
  reference like "PART 14" in this file is unambiguous.
* **One PART = one chapter = one folder = one agent = one pull request.** A chapter is a whole topic
  in this repo's sense (`work-energy-power/`, `gravitational/`, …): one master Markdown file, one
  README, one local gate, one commit series.
* **The numbering is the protocol.** A human (or a coordinating agent) says *"execute PART 17"* and
  the agent does exactly PART 17 and nothing else. Parts are additively mergeable: two agents never
  need to negotiate anything except the four shared-file lines listed in §1.9.

### 0.2 The three prompts you will actually paste

**Kick-off prompt (one chapter, one agent).**

```text
You are an elite physics teacher-author working in the repository Physics_JEEAD-OLYMPIAD_notes.
Read plan.md. Execute exactly PART <N> — "<TITLE>" — and nothing else.
Read §0, §1 and §2 of plan.md first (the contracts and the teaching doctrine), then your PART's
section, then Appendix C (the copy-paste kit).
Deliverables: the folder <slug>/ with <Title>.md, README.md, notes.json, tools/check.py, exactly as
plan.md §1.1 and §1.10 specify.
Rules that matter most:
- The notes are read in **Obsidian reading mode** — obey plan.md §1.3.1 exactly (frontmatter, callouts,
  math spacing, blank lines around <details>, wikilinks, no #hashtags).
- No images at all: use the Mermaid FIGURE callouts of §1.2 for rendered figures, and DIAGRAM
  callout briefs as the runtime seed wherever a hand-drawn picture is wanted (every seed line
  still carries search words).
- Every formula derived, with its validity condition and a limit check.
- The 15-block spine of §1.4 in order, ending in a separate Olympiad section and a 36-question /
  200-mark Olympiad paper with its marking scheme and formula sheet.
- **Completeness (§1.12): the PART's section list is a floor.** Sweep the Cengage chapter's own contents
  page from the PDF committed in this repo (§1.13 — read the page images; four of the five volumes have no
  text layer), sweep the shipped notes for hand-offs, and add in the right block anything the plan missed.
  Record additions under "Beyond the plan" in the chapter README + topics.json `beyond_plan`.
- Every number recomputed; maths in KaTeX-safe $...$ / $$...$$.
Finish by running  python3 tools/check.py  in the chapter folder and  python3 tools/check_all.py --update
from the repo root; report the gate output, the word count, the DIAGRAM-brief count and what the book
sweep added.
```

**Resume prompt (an agent continuing half-written work).**

```text
Read plan.md §0–§2, PART <N>, §1.12 (completeness) and §1.13 (PDF cross-check). Before writing
anything: git log --oneline -- <slug>; grep -n 'TODO\|FIXME\|{{' <slug>/*.md; run python3 tools/check.py.
Continue the existing file and do not rewrite reasoning that is already there — the missing blocks are the
job. Then complete the book sweep of §1.12 against the Cengage PDF named in your PART's source line, and
finish the definition of done in §1.11.
```

**Coordinator / audit prompt (after every few parts).**

```text
You are the lead architect for Physics_JEEAD-OLYMPIAD_notes. Read plan.md §5–§7.
Audit the parts marked complete against their per-part exit criteria, their "Beyond the plan" lists and
their coverage maps (spot-check two rows of each against the Cengage PDF §1.13). Run
python3 tools/check_all.py. Fold every `beyond_plan` finding back into plan.md as a plan amendment.
Repair only cross-part inconsistencies (naming, hand-offs, registry, CURRICULUM.md, docs/site, Obsidian
conventions per §1.3.1). Do not rewrite a chapter's physics.
```

### 0.3 Master index of the 28 parts

"Needs" is the strict prerequisite set. A part may be written in parallel with anything it does not
need. Source = the Cengage volume/chapter whose floor it must cover (verify the printed chapter
number on the volume's contents page before writing; the notes' coverage map is keyed to **section
names**, never to numbers).

| PART | slug | chapter | block | source (Cengage floor — verified against the PDF, §1.13) | needs |
|---:|---|---|---|---|---|
| 1 | `units-measurements` | Units, Dimensions & Measurement Errors | A · Mechanics | *Mechanics I* ch 3 Units and Dimensions (+ ch 1 Basic Mathematics as an appendix) | — |
| 2 | `vectors` | Vectors & Vector Algebra | A · Mechanics | *Mechanics I* ch 2 Vectors | — |
| 3 | `kinematics-1d` | Motion in One Dimension | A · Mechanics | *Mechanics I* ch 4 Motion in One Dimension | 1, 2 |
| 4 | `motion-in-two-dimensions` | 2-D Motion: Projectiles, Relative Velocity, Circular Kinematics | A · Mechanics | *Mechanics I* ch 5 Motion in Two Dimensions (+ ch 6 archives) | 2, 3 |
| 5 | `newtons-laws` | Newton's Laws, Friction, Constraints & Circular Dynamics | A · Mechanics | *Mechanics I* ch 7 Newton's Laws of Motion | 4 |
| 6 | `work-energy-power` | Work, Energy & Power | A · Mechanics | *Mechanics II* ch 2 Rigid Body Dynamics §2.24–2.26 (rotational work and power, work–energy theorem, conservation of mechanical energy) + ch 1 §1.17–1.19 on impulse | 5 |
| 7 | `centre-of-mass-momentum` | Centre of Mass, Momentum & Collisions | A · Mechanics | *Mechanics II* ch 1 Centre of Mass, Conservation of Linear Momentum and Collision | 6 |
| 8 | `rotational-mechanics` | Rotational Mechanics | A · Mechanics | *Mechanics II* ch 2 Rigid Body Dynamics | 7 |
| 9 | `gravitation` | Gravitation & Orbital Motion | A · Mechanics | *Mechanics II* ch 5 Gravitation | 8 |
| 10 | `simple-harmonic-motion` | Simple Harmonic Motion & Oscillations | A · Mechanics | *Waves and Thermodynamics* ch 4 Linear and Angular Simple Harmonic Motion (+ ch 7 §7.3–7.7 on springs and their combinations) | 8 |
| 11 | `fluid-mechanics` | Fluid Mechanics & Surface Tension | A · Mechanics | *Mechanics II* ch 3 Fluid Mechanics (+ ch 4 Properties of Solids and Fluids for surface tension) | 5 |
| 12 | `elasticity` | Elasticity & Properties of Matter | A · Mechanics | *Mechanics II* ch 4 Properties of Solids and Fluids (elasticity) | 5 |
| 13 | `electric-field` | Charge, Coulomb's Law & Electric Field | B · E&M | *Electrostatics & Current Electricity* ch 1 Coulomb's Laws and Electric Field | 2 |
| 14 | `gauss-law` | Electric Flux & Gauss's Law | B · E&M | same volume ch 2 Electric Flux and Gauss's Law | 13 |
| 15 | `electric-potential` | Potential, Potential Energy & Conductors | B · E&M | same volume ch 3 Electric Potential | 14 |
| 16 | `magnetic-field` | Magnetic Field, Biot–Savart & Lorentz Force | B · E&M | **no PDF in this repo** — standard JEE Advanced magnetism chapters (§1.13) | 15 |
| 17 | `amperes-law` | Ampère's Law, Currents & Magnetic Dipoles | B · E&M | standard magnetism chapter (no PDF in this repo) | 16 |
| 18 | `moving-charges-magnetism` | Cyclotron, Velocity Selector, Hall Effect | B · E&M | standard magnetism chapter (no PDF in this repo) | 17 |
| 19 | `magnetism-and-matter` | Magnetism & Matter, Earth's Magnetism | B · E&M | standard magnetism chapter (no PDF in this repo) | 17 |
| 20 | `electromagnetic-induction` | Faraday, Lenz, Motional EMF & Eddy Currents | B · E&M | standard EMI chapter (no PDF in this repo) | 17 |
| 21 | `inductance` | Self & Mutual Inductance, RL, Magnetic Energy | B · E&M | standard EMI/inductance chapter (no PDF in this repo) | 20 |
| 22 | `alternating-current` | AC Circuits, Resonance & Transformers | B · E&M | standard AC chapter (no PDF in this repo) | 21 |
| 23 | `photoelectric-effect` | Photons, Photoelectric Effect & Matter Waves | C · Modern | *Optics & Modern Physics* ch 3 Photoelectric Effect | EM waves (shipped), 15 |
| 24 | `atomic-structure` | Rutherford, Bohr Model & Atomic Spectra | C · Modern | same volume ch 4 Atomic Physics (Bohr model and spectra half) | 23 |
| 25 | `x-rays` | X-rays, Moseley's Law, Bragg & Compton | C · Modern | same volume **ch 4 Atomic Physics, pp. 4.25–4.32** (X-rays, X-ray spectra, Moseley's law) | 24 |
| 26 | `nuclear-physics` | Nuclear Structure, Radioactivity, Fission & Fusion | C · Modern | same volume ch 5 Nuclear Physics | 24 |
| 27 | `semiconductors` | Semiconductors & Electronic Devices | C · Modern | **not in this volume** — standard JEE Advanced semiconductor syllabus (grep the other PDFs before writing, §1.13) | current electricity (shipped), 18 |
| 28 | `special-relativity` | Special Relativity & Relativistic Mechanics | C · Modern (olympiad) | olympiad extension (IPhO-level; nothing in these volumes) | 6, EM waves (shipped), 23 |

> **Book-sweep reminder.** The source column is where the §1.12 sweep starts, not where it ends: read the
> Cengage chapter's own contents page (page numbers in §1.13) and pull in every heading it lists.

### 0.4 Execution batches (what can be written simultaneously)

Agents working in different batches never share a file. Within a batch, the only shared lines are the
four in §1.9 and they merge by "keep both".

| batch | parts | why they can go together |
|---:|---|---|
| 0 | 1, 2, 3, 13, 23, 27 | no in-repo prerequisites; 13 needs only vectors; 27 needs the shipped current-electricity notes |
| 1 | 4, 5, 14, 24 | each is the successor of one batch-0 part |
| 2 | 6, 7, 15, 25 | |
| 3 | 8, 9, 16, 26 | |
| 4 | 10, 11, 17, 28 | |
| 5 | 12, 18, 19 | |
| 6 | 20, 21, 22 | EMI → inductance → AC is one continuous argument; do not split it across agents |

A single agent can also take a full block (1–12 mechanics, 13–22 electricity & magnetism,
23–28 modern physics) serially; that costs nothing structurally — only the per-chapter gates still
have to pass one at a time.

### 0.5 What this plan deliberately does not cover

* The nine shipped note-sets (Appendix A) and the four v1 wave/optics work packages.
* Thermal topics folded into the shipped `heat/` and `thermodynamics/` notes (Appendix B).
* Communication systems, astrophysics-as-a-chapter, numerical simulation, formal statistical
  mechanics, and university-level quantum mechanics (Appendix B lists where each one hands off).

---

## 1 · The non-negotiable contracts

Read this section once, completely, before writing a line. It is what makes 28 independently written
chapters feel like one book.

### 1.1 Deliverables and folder layout (Markdown-first, Obsidian-first)

```
<slug>/
├── <Title>.md            the chapter: the notes. THE deliverable.
├── README.md             scope, coverage map, status, hand-off note, `## Beyond the plan` (§1.10, §1.12)
├── notes.json            machine-readable config for the local gate (§1.10)
└── tools/
    └── check.py          the local gate, copied from Appendix C and configured by notes.json
```

* **No `assets/`.** No `figures/`. No `.html`. No binary of any kind. A chapter that ships an image
  fails review.
* `<Title>.md` is the single source of truth: orientation → theory → worked questions → Olympiad
  section → paper → formula sheet, in one file, in that order (§1.4). It opens with YAML frontmatter and
  is written for Obsidian reading mode (§1.3.1).
* The folder name is the slug in the index table; the file name is the title with hyphens
  (`Work-energy-power.md`, `Amperes-law.md`, `X-rays.md`, `Magnetism-and-matter.md`,
  `Centre-of-mass-momentum.md`). Register the topic in `topics.json` with `"format": "markdown"`,
  `"entry": "<slug>/<Title>.md"`, `"plan_part": <N>`, `"owner": "<agent or human handle>"`.
* **Claim before you write.** In `topics.json`, set `status: "in-progress"` and your `owner`. In
  `README.md` (repo root) add your one row; in `PENDING.md` change the chapter's box from `[ ]`-style
  pending text to "PART N — in progress (agent)". These three one-line edits land in the same commit
  as the first draft, never as a separate "claim" commit that can collide.

### 1.2 The media policy — rendered figures, never AI art

**The media policy (v2).** The vault is Obsidian-first, and figures are *rendered from source the agent
writes* — deterministic, never AI-art. Two constructs coexist (full contract:
`docs/obsidian-plugin-workflow.md` §2, with the worked pilot `kinematics-1d`):

**(a) RUNTIME FIGURE — a `[!tip] FIGURE` callout wrapping a ` ```mermaid ` block.** This is the new
default for anything a diagram adds value to: a mindmap, a flowchart, a `quadrantChart`, or an
`xychart-beta` data graph. Every FIGURE is both the rendered diagram *and* the described slot:

````markdown
> [!tip] FIGURE F5.3 · Static friction vs applied force
> *Why:* the drop from peak to plateau is the single most-misread feature of the curve.
> *Data:* f = F while F ≤ 60 N, then f = 40 N constant (μ_s N = 60, μ_k N = 40).

```mermaid
xychart-beta
  title "friction force vs applied force"
  x-axis [0, 100]
  y-axis [0, 70]
  line [0, 20, 40, 60, 60, 40, 40, 40, 40, 40, 40]
```

> *Read:* the kink sits at the peak f_max; after it, f is constant at f_k regardless of F.
````

Hard rules for FIGURE callouts:

* `> [!tip] FIGURE F<part>.<n> · <title>`, then exactly one `*Why:*`, one `*Data:*`, one ` ```mermaid `
  block, then one `*Read:*` line. Blank line after the callout and around the fence. **LaTeX does not
  render inside Mermaid** — node/label/title text is plain text or Unicode (`v₀`, `→`, `μ`) only; put
  `$…$` in the `*Data:*`/`*Read:*` lines or surrounding prose.
* Numbering contiguous per chapter, matching the PART number (`F8.4` = fourth figure of PART 8).
  Minimum **6** per chapter, 12–20 for the big ones. **≥ one** `xychart-beta` data graph **per
  chapter that could support one** (any "graph" content: x–t/v–t, V–I, U–r, stress–strain, spectra),
  2–4 for the big ones.
* `xychart-beta` line series must plot the function stated in `*Data:*`; compute the values on a
  uniform grid. Add `line [0,0]` as a zero axis. Curve shape (concavity, asymptote, symmetry) must
  match the physics.

**(b) LEGACY SEED — a `> [!abstract] DIAGRAM D<part>.<n>` brief**, kept wherever a diagram is *wanted
but deferred* (the reader searches for it):

* **Every** place a picture carries part of the argument gets a DIAGRAM placeholder in this exact
  syntax (three lines, blank line after; nothing else on those lines):

```markdown
> [!abstract] DIAGRAM D5.3 · Static friction vs applied force
> *Show:* a plot with the applied force $F$ on the $x$-axis and the friction force $f$ on the $y$-axis; the $45^\circ$ straight line $f=F$ up to the peak $f_{\max}=\mu_s N$, then a sudden drop to the constant kinetic plateau $f_k=\mu_k N$; both plateaux labelled numerically.
> *Search:* "static friction graph applied force versus friction force threshold kinetic plateau"
```

The `[!abstract]` callout is what makes the brief read as a *figure slot* in Obsidian's reading mode
(tinted, indented, visually distinct from theory). The gate counts these callouts, so the syntax is
load-bearing: `> [!abstract] DIAGRAM D<part>.<n> · <title>`, then the two `*Show:*` / `*Search:*` lines,
then a blank line.

* The three required pieces: a **numbered label** `D<part>.<n>`, a **`*Show:*`** line that is a
  complete drawing brief (axes, vectors, labels, angles, what is dashed, what is highlighted), and a
  **`*Search:*`** line with 5–12 English words that will find a textbook version of exactly that
  figure. Optional fourth line `*Used in:* §3.4, Q7.`
* Numbering is per chapter, contiguous from `D<n>.1`, and the number matches the PART number
  (`D8.7` is the seventh diagram of PART 8).
* **The prose must survive without the picture.** A DIAGRAM placeholder is a *convenience*, never a
  load-bearing crutch: never write "as the figure shows, the force is zero here". Write the physics
  in words and symbols, then add the brief.
* Minimums: **≥ 6** `F`-figures per chapter (12–20 for the big ones), **≥ 6** `D`-seeds per chapter
  (the seed count is per the D-list in each PART section below). The chapter gate counts them (§1.10).

  A `D`-seed is *not* a rendered figure yet — it is the ground truth a rendering is checked against.
  Nothing is lost if a seed is later upgraded to an `F`-figure; the current numbering is covered by
  the gate, so upgrade careful both places (`D`-count and `F`-count) in one commit.
* **The prose must survive without the picture.** A figure or brief is a *convenience*, never a
  load-bearing crutch: never write "as the figure shows, the force is zero here". Write the physics
  in words and symbols, then add the figure/brief.
* Banned everywhere: `![alt](path)`, `<img …>`, raster art (`png/jpg/gif/webp`), AI-generated SVG,
  a URL to an image, an ASCII-art figure. Allowed: Mermaid blocks *inside the `[!tip] FIGURE`
  wrapper only*, and the committed `assets/figures/*.svg` sets of the HTML-heritage topics.

### 1.3 Markdown formatting contract

| element | rule |
|---|---|
| Frontmatter | the file **opens** with YAML properties (no heading above them): `title:`, `part: <N>`, `slug:`, `aliases:`, `tags:`; then a blank line, then the `#` title |
| Title | one `#` heading: `# <Chapter> — first principles to Olympiad` |
| Chapter blocks | `## Part 0 · …` through `## Part 14 · …` — exactly the 15 blocks of §1.4, in order, headings matching the names in Appendix C |
| Subsections | `### <block>.<k> Title` (e.g. `### 3.4 The validity ledger`), numbered contiguously inside their block |
| Sub-subsections | `#### ` sparingly (derivation steps, sub-cases) |
| Maths | inline `$…$`, display `$$…$$` on its own lines; KaTeX-safe: no `\tag`, no `\label`, no `\begin{tikzpicture}`, no `\middle`, no raw `$$` inside a word; one command per brace group as usual; `\text{}` for words |
| Equation labels | prose "Eq. (3.4)" or a trailing `\qquad (3.4)` **inside** the display block; never `\tag` |
| Callouts | **Obsidian callouts only** (see the mapping in §1.3.1): `> [!note] Definition`, `> [!info] Why`, `> [!warning] Condition of validity`, `> [!success] Check`, `> [!danger] Trap`, `> [!tip] Insight`, `> [!quote] Hand-off`, `> [!question] Exam note`, `> [!abstract] Numbers to keep`, `> [!example] Worked example`. Never write `> **Definition.**` — the gate rejects it |
| Worked examples | `### E7 — Title`, then the problem, then `<details><summary>Solution</summary>` (blank line, body, blank line, `</details>`), closing with a `> [!success] Check` limit/unit/dimensional line |
| Concept checks | `**C4 — concept check.** …` followed by a one-line answer in a `<details>` |
| Cengage-floor practice | `#### Q12. …` then options or a free answer, then a `<details>` solution |
| Olympiad problems | `### OL3 — Title`, full multi-part long problem, then a `<details>` solution that names the method and the checks |
| Paper questions | `### P14 · 5 marks` (36 of them, sections A–D), each with a `<details>` solution |
| Tables | GitHub pipe tables; a *validity* column wherever the table lists formulas |
| Traps | one per trap, in the block-8 section, written as the tempting wrong answer then the one-line reply |
| Empathy markers | `> [!question] Exam note` for "this is how it appears in a paper"; `> [!quote] Hand-off` for "this result is owned by PART k / the shipped note-set X — read it there" |
| Forbidden | HTML beyond `<details>`/`<summary>`/`<br>`; images; external links; `#hashtags` in prose (Obsidian turns them into tags); `\( \)` / `\[ \]` math delimiters; `\tag` / `\label`; blank lines inside a `$$` block; emoji-only headings; `TODO`, `FIXME`, `…`, `??`, `{{PLACEHOLDER}}`; "it can be shown that"; "obviously" |

### 1.3.1 Obsidian reading-mode contract (the notes are read in Obsidian)

The target reader opens the vault in Obsidian and reads in **reading mode**. Everything in this table is a
hard requirement; §1.10's gate checks all of it.

| # | rule | why (what breaks otherwise) |
|---:|---|---|
| 1 | YAML **frontmatter first**, then a blank line, then `# <Chapter> — …` | Obsidian shows the frontmatter as properties; the `part:` property is what lets the reader filter the vault by plan part. A `#` heading before `---` disables properties |
| 2 | callouts in the form `> [!type] Title`, with **every** continuation line starting `> ` and a blank line after the block | an unmarked or unspaced line breaks out of the callout and the box renders as loose quoted text |
| 3 | allowed callout types only: `note` (definition), `info` (why), `warning` (validity), `success` (check), `danger` (trap), `tip` (insight), `quote` (hand-off, history), `question` (exam note), `abstract` (numbers to keep, DIAGRAM briefs), `example` (worked example) | unknown types fall back to plain blockquotes, so the visual language of the notes disappears |
| 4 | inline math `$...$` with **no space** just inside the dollars; display math `$$` alone on its line, formula on the next line | `$ x $` is not recognised as math by Obsidian and prints as raw dollars — a silent, ugly failure |
| 5 | **no blank lines inside** a `$$ ... $$` block; one display per block | Obsidian closes the math block at a blank line and the rest prints as text |
| 6 | no `\( \)` or `\[ \]`; no `\tag`, no `\label`, no custom macros/preamble, no `\ce{}` | Obsidian's KaTeX has no preamble and no macro definitions; `\tag` fights the `\qquad (n)` convention the notes use |
| 7 | solutions stay `<details><summary>Solution</summary>` with a **blank line after `</summary>`** and **before `</details>`** | without the blank lines Obsidian does not parse Markdown inside the block: equations and lists come out raw |
| 8 | pipe tables: keep to ≤ 6 columns and short cells; put long formulas in display math *above* the table; inside table math use `\lvert x \rvert` (never a bare `|`) | an unescaped pipe silently splits the table; wide cells scroll horizontally in reading mode |
| 9 | cross-references are **wikilinks**: `[[Work-energy-power#Part 3 · Core derivations|WEP §3]]` — file name first, then the heading after `#` | relative Markdown links to other notes are clumsy in Obsidian; wikilinks also feed the graph view and backlinks panel |
| 10 | heading numbers stay unique and stable (`### 3.4 …`); never two headings with identical text | the outline pane and `[[#heading]]` links are ambiguous with duplicates |
| 11 | no `#hashtags` in prose (say *chapter 6*, *Q12*, *§3.4*); tags live only in the frontmatter | Obsidian converts `#word` into a tag, polluting the tag pane |
| 12 | no HTML beyond `<details>`, `<summary>` and `<br>` (inside tables); `<br>` is allowed nowhere else | anything else prints literally in reading mode |
| 13 | figures are the `F`-numbered `[!tip] FIGURE` callouts wrapping ` ```mermaid ` blocks (§1.2); deferred figures are `[!abstract] DIAGRAM …` briefs. Raster art, AI-generated SVG, external image URLs and ASCII art are banned | AI art was inaccurate and wasteful; rendered diagrams are deterministic and always render; hand-drawn pictures remain searchable via the seed brief |
| 14 | bold `**…**` for emphasis, `*…*` for figure-brief field names, backticks for commands and symbols only | keeps reading mode calm; backticks around physics symbols render as code and break math |
| 15 | footnote-style asides are discouraged; if used, keep `[^n]` and its definition in the same block | Obsidian's footnotes jump to the end of the note, which loses the reader's place |

A ready-to-copy skeleton (frontmatter + callout + `<details>` + DIAGRAM brief) is in **Appendix C.3**.

### 1.4 The 15-block spine (identical in every chapter, in this order)

The spine is the *pedagogy*. It is ordered the way a strong teacher teaches: picture → quantities →
derivations → standard results → practice → methods → traps → playbook → Olympiad → paper → sheet.

| block | heading | what it contains |
|---:|---|---|
| 0 | `## Part 0 · Orientation` | What you will be able to do; **the one idea** of the chapter in ≤ 3 sentences; prerequisite self-check (6–8 recall questions with answers); "numbers to keep" table; how to use the chapter in 3 passes; the coverage map of §1.5 |
| 1 | `## Part 1 · Intuition first` | The physical picture with **no formulas yet** (or with at most one); what the phenomenon looks like, what is being conserved, what changes with what, the everyday anchors (a lift, a bicycle, a balloon, a lamp) |
| 2 | `## Part 2 · Definitions and bookkeeping` | Every symbol defined, units, sign conventions fixed once, state variables, frames, the model's assumptions, and the "what is NOT in this model" list |
| 3 | `## Part 3 · Core derivations` | The proof-first spine of the chapter, in teaching order (each PART's section below gives that order explicitly): every step justified, every "therefore" paid for |
| 4 | `## Part 4 · Results, limits and the validity ledger` | Boxed standard results, each with its condition of validity; the limit checks ($x\to0$, $x\to\infty$, massless/rigid/ideal); the "which formula when" table; the correspondence to the next simplest case |
| 5 | `## Part 5 · Worked exemplars` | `E1 … E10+`, interleaved at the exact point of theory they use, each with a collapsible full solution and a check |
| 6 | `## Part 6 · Problem archetypes and practice` | The archetype table of §1.5 (template → why it works → worked instance → variations), then `Q1 … Q25+` in-flow practice with collapsible solutions |
| 7 | `## Part 7 · Alternate methods and the JEE-Advanced advantage toolkit` | Symmetry, frames, energy, phasors, complex numbers, matrices, superposition, scaling, dimensional analysis — the methods that cut a 6-minute problem to 90 seconds, each with a worked demonstration and a statement of when it fails |
| 8 | `## Part 8 · Examiner traps` | 8–12 traps: the wrong answer students give, why it is tempting, the one-line reply, and the paper archetype that exploits it |
| 9 | `## Part 9 · Playbook` | Triage decision tree ("if the question asks…, do…"), formula map with validity, constants/numbers to memorise, timing plan for the paper, a 10-point pre-submission audit |
| 10 | `## Part 10 · Olympiad extension` | The **Olympiad-level section**: non-standard methods, deeper derivations, order-of-magnitude estimates, `OL1 … OL10+` solved long problems (each: method named → derivation → numeric answer → two checks) |
| 11 | `## Part 11 · Olympiad-grade paper` | 36 questions / 200 marks / 180 minutes, sections A–D of §1.7, instructions and a coverage map; each question carries its own collapsible solution |
| 12 | `## Part 12 · Marking scheme and post-paper audit` | Mark distribution table (must sum to 200), the "which block each question tested" map, the diagnostic table ("if you lost marks here, reread §…") |
| 13 | `## Part 13 · Formula sheet` | Dense reference: every formula with its validity condition, unit conventions, the 15–25 constants worth carrying in your head, laid out for 2–3 printed A4 pages |
| 14 | `## Part 14 · Checkpoint and hand-off` | 20–30 "can I do this?" statements with self-scoring; what the next chapter assumes from this one; open questions the reader is now equipped to attack |

**Olympiad-at-the-end rule.** The chapter's *theory* ends by block 9; blocks 10–11 are the Olympiad
layer, and blocks 12–14 are its apparatus (marking, formula sheet, checkpoint). That is the required
"I understand the Cengage level, and now I can be examined at Olympiad level" finish.

### 1.5 Cengage floor and archetype coverage (the "at least Cengage" rule)

* Block 0 of every note contains a **coverage map table**: one row per Cengage section of that
  chapter — `Cengage section (name) | what it establishes | where it lives here | status` — with
  status ∈ {derived, stated + used, extended beyond book}. No row may be blank. Any deliberate
  omission is named and justified in the same table (and repeated in `topics.json`'s
  `deliberately_not_covered`).
* Block 6 contains an **archetype table** with ≥ 15 rows — the recurring problem shapes of that
  chapter (each PART's section lists the mandatory ones). Every archetype appears at least once as a
  worked `#### Q` with a full solution and once as a *variation* with the numbers changed, because
  recognition + variation is what transfers to an exam.
* Nothing is quoted from the book. Same ground, original derivations, original numbers.
* The floor is a **floor**: where the Cengage treatment stops (JEE-level), the note must keep going
  through blocks 10–11.

### 1.6 The Olympiad layer (block 10) — what "olympiad level" means here

Block 10 is not "harder JEE questions". It must contain, as a minimum:

1. **≥ 3 first-principles derivations** that a school book states without proof (each PART's section
   names candidates: variational principles, differential equations, adiabatic invariants, symmetry
   arguments, scaling laws, energy methods, complex/phasor methods, eigenvalues).
2. **≥ 3 order-of-magnitude estimates** ("how many?", "how big?", "how long?") with the algebra shown
   and the answer verified against a known value.
3. **≥ 10 solved long problems** `OL1 … OL10`, each 15–40 minutes of honest work, mixing theory with
   a number, and each solved twice where a second method exists (that second method is the point).
4. **≥ 2 "physics behind the number" items** — a real measurement (muon lifetime, Cavendish, Millikan,
   nuclear density, the Sun's luminosity) reconstructed from the chapter's results.
5. **An explicit limits-and-failure section**: where the chapter's model breaks (non-linear, chaotic,
   relativistic, quantum, dissipative) and which later PART or reference takes over.

### 1.7 Question, paper and marks contract

* In-flow: `C`-checks (short), `E`-exemplars (full), `Q`-practice (full). Numbering contiguous from 1
  inside each family. Every one has a `<details>` solution. Minimums: `C ≥ 12`, `E ≥ 10`, `Q ≥ 25`.
* Paper: 36 questions, **200 marks**, 180 minutes, exactly this shape —

| section | count | marks each | subtotal | style |
|---|---:|---:|---:|---|
| A | 12 | 4 | 48 | single correct |
| B | 8 | 4 | 32 | one or more correct |
| C | 6 | 5 | 30 | numerical / integer |
| D | 10 | 9 | 90 | comprehensive long-form (multi-part, Olympiad standard) |
| | 36 | | **200** | |

* Every paper question is marked with its `· N marks` tag on the heading line — the local gate sums
  these and compares with `notes.json`; a mismatch is a hard failure. Never print a total you did not
  recompute.
* The paper's coverage map (block 11 intro and block 12 table) names, for each question, the block it
  tests. Every one of blocks 2–4 and 10 must be tested by at least one question.
* Difficulty spread: sections A–C mostly JEE-Advanced standard with 3–4 INPhO-grade items; section D
  is INPhO/IPhO standard, at least two questions with a two-method solution.

### 1.8 Numbers, limits and honesty rules

1. **Recompute every number you print** (python one-liners are fine) — including intermediate values
   in solutions and every mark total.
2. **Check a limit in the text** for every boxed result: `as m→∞ this returns the fixed pulley, ✓`.
3. **Units in every substitution**, and state the assumptions (STP, ideal gas, frictionless, small
   angle, $\mu_s = \mu_k$, air at 20 °C).
4. **Mark the validity** of every idealisation you use: point mass, rigid body, incompressible,
   steady, laminar, linear, paraxial, small amplitude, non-relativistic.
5. **No invented data.** If you cite a measured value, it must be a standard one (CODATA/PDG/NIST
   style) and used consistently across the chapter.
6. **Say when a formula is an approximation and how big the error is** (e.g. pendulum: ≤ 0.2 % for
   $\theta_0 < 7^\circ$; $\sin\theta\approx\theta$ error $<1\%$ below 14°).
7. **No thinking-out-loud fragments** in the file: `grep -n 'TODO\|FIXME\|\.\.\.\|? no:' <file>` must
   be empty before commit.

### 1.9 Parallel-work rules (what you may touch)

| file | rule for a chapter agent |
|---|---|
| your `<slug>/**` | yours alone; edit freely |
| `topics.json` | add **one** object for your slug (and nothing else); `pages/counts` are regenerated by `--update` |
| `README.md` (root) | append **one** row to the note-sets table |
| `PENDING.md` | mark **your** chapter's line as done/in-progress; never rewrite another block |
| `CURRICULUM.md` | the coordinator rewrites this after every 4–6 parts; do not touch it per chapter |
| `docs/site/**`, `tools/md_site.py` | coordinator only (one regeneration pass at the end of each batch) |
| `STRUCTURE.md`, `CONTRIBUTING.md`, `tools/*.py` (root) | do not touch. If you believe a rule is wrong, put it in the PR description as `rules-proposal:` |
| other `<slug>/**` | never edit — not even a typo. Report it as `drive-by:` in your PR description |

Branch and commit: `git switch -c notes/part-<N>-<slug>` (or stay on the session branch you were
given) and commit in readable steps: `part-07: structure + coverage map`, `part-07: derivations
blocks 2–4`, `part-07: exemplars and practice`, `part-07: olympiad + paper`, `part-07: gate green`.
PR title: `part-<N>: <slug> — <chapter title>`. Never commit to `main` directly.

### 1.10 The local gate, the registry, the site

Every chapter ships `notes.json` (config) plus `tools/check.py` (the validator, copied verbatim from
Appendix C). The validator enforces: the YAML frontmatter (`title`, `part`, `slug`); the 15 block
headings; the minimum counts of C/E/Q/OL, DIAGRAM briefs and **Obsidian callouts**; contiguous numbering
in every family; the paper's section shape and the mark total; **absence** of image syntax, `<img`,
external links, `#hashtags` in prose, `\( \)`/`\[ \]` delimiters, `\tag`/`\label`,
`TODO`/`FIXME`/`{{…}}`; the retired `> **Label.**` box style; unbalanced dollar delimiters and unbalanced
TeX braces; a missing blank line after `</summary>`; a blank line *inside* a `$$` block; a stray pipe
inside table math; and a space just inside the dollars of an inline span — the reading-mode failures of
§1.3.1 that Obsidian hides silently. It prints one line per failure and exits non-zero.

```bash
cd <slug> && python3 tools/check.py          # local gate
cd .. && python3 tools/check_all.py --update # repo gate + registry recount
```

`check_all.py` requires, for a Markdown-first topic, the `.md` entry, `tools/check.py` and an `owner`.
It recounts `figures` (will be **0** — expected and correct here), `questions`, `solutions`,
`math_spans`, `words`, `display_formulas`, `bytes_markdown`. Commit the recounted registry.

### 1.11 Definition of done (a chapter is finished only when all of this is true)

* [ ] `<slug>/<Title>.md`, `README.md`, `notes.json`, `tools/check.py` exist; `python3 tools/check.py`
      prints ALL GOOD.
* [ ] The 15 blocks are present, in order, with the required minimums (C ≥ 12, E ≥ 10, Q ≥ 25,
      OL ≥ 10, DIAGRAM ≥ 12, callouts ≥ 24, paper = 36 Q / 200 marks / 180 min).
* [ ] The chapter reads correctly in **Obsidian reading mode**: frontmatter, callouts (no `> **Why.**`
      boxes), math with no space inside the dollars and no blank line inside a `$$` block, blank lines
      around `<details>` bodies, table math using `\lvert … \rvert`, wikilinks for cross-references, no
      `#hashtags` in prose (§1.3.1). Open the file in Obsidian (or in a vault preview) before saying yes.
* [ ] The **book sweep** of §1.12 is done: the Cengage chapter's contents page was read from the PDF in
      the repo (§1.13), and every book heading appears in the coverage map with one of the four statuses.
* [ ] Anything the plan did not ask for but the sweep justified is listed under `## Beyond the plan` in the
      chapter README and mirrored in `topics.json` as `beyond_plan`; any chapter-sized gap was escalated to
      `PENDING.md` instead of absorbed.
* [ ] The coverage map has a row for every Cengage section of the chapter, with a status.
* [ ] ≥ 15 archetype rows in block 6, each exercised.
* [ ] Every boxed result has a validity condition; every derivation has an `> [!info] Why` callout where
      a competent reader would otherwise ask "why?".
* [ ] Every numerical answer recomputed; every mark total summed; at least one limit check per block.
* [ ] Media policy met: ≥ 6 `F`-figures with `*Why:*`/`*Data:*`/`*Read:*` and valid mermaid kinds;
      ≥ 6 well-written DIAGRAM briefs with usable search terms; ≥ 1 `xychart-beta` data graph where
      the chapter has graph content; no raster art, no AI SVG, no external images, no bare mermaid.
* [ ] `python3 tools/check_all.py --update` green from the repo root; registry, README row and
      PENDING line updated; `README.md`'s table row matches the registry's counts.
* [ ] The chapter README records the hand-off: what it assumes, what the next PART inherits, what was
      deliberately skipped and why.

---

### 1.12 Completeness duty — the plan is a floor, not a ceiling

**The PART section you are given is a checklist of the *minimum*.** It was written from the volume's
contents page and the standard JEE-Advanced/NSEP/INPhO syllabus, and it can miss a subtopic, a standard
result, a question archetype or a whole section of the book. It is your job to close that gap, not to
inherit it. Do all four sweeps, in this order, before you call the chapter finished:

1. **The plan sweep.** Write the PART's section table as your teaching order. Every row of it must exist in
   the chapter. Nothing else yet.
2. **The book sweep.** Open the Cengage chapter in the PDF that is committed in this repository (§1.13) and
   read its **contents list and every heading**. Every heading — including the sub-headings and the
   `Solved Examples` / `Exercises` structure — must be accounted for in the chapter's coverage map
   (block 0), one of four ways: *derived*, *stated and used*, *extended beyond the book*, or *excluded with
   a written reason*. A heading you never looked at is the failure mode this section exists to prevent.
3. **The vault sweep.** Search the shipped notes (Appendix A) and the other PARTS (Appendix D) for the same
   subject matter. Anything they own becomes a `> [!quote] Hand-off` pointer. Anything they *do not* cover
   that belongs to your chapter becomes a new section in the right block.
4. **The syllabus sweep.** Walk the standard JEE Advanced + NSEP/INPhO topic list for your chapter's
   subject and ask of each item: *is this in my chapter?* The olympiad layer (block 10) is where the items
   the book omits belong.

Then:

* **Record what you added.** The chapter's README ends with a `## Beyond the plan` list — one line per
  section, archetype, exemplar or olympiad problem that the PART section did not ask for — and the same
  list is mirrored in `topics.json` as `"beyond_plan": [...]`. The coordinator folds it back into this file
  (see the plan-amendment rule at the end of this document).
* **Escalate, do not absorb, chapter-sized findings.** If the sweep shows a missing *chapter* (not a
  section), do **not** write it inside your chapter: add it to `PENDING.md` as a new part with a one-line
  scope, and add a row to Appendix D's ledger if it takes ownership of a result. One chapter per agent is
  what keeps 28 agents from colliding.
* **You may add; you may not subtract.** If a plan section looks wrong, derive the correct result, put it
  in the chapter with a `> [!warning] Plan amendment` note explaining the correction, and say so in the PR
  description. Never silently drop a required section.
* **The gate cannot check completeness** — it counts markers, headings and marks. The coverage map in
  block 0 is the only artifact that proves the sweep happened, which is exactly why §1.5 requires every
  row to carry a status and a location.

### 1.13 Cross-checking against the Cengage volumes (they are in this repo)

The five volumes are committed at the repository root (yes, in git — `git ls-files | grep pdf` lists them),
so *"the Cengage floor"* is verifiable rather than remembered. **Note on the scans:** four of the five are
image-only (there is no text layer — `pdftotext` returns just the watermark), so search inside them does
not work; you read the page images. `Cengage  MECHANICS  1-compressed.pdf` **does** have a text layer. The
verified map (contents pages read directly, 2026-09):

| file in the repo | pages | what it actually holds | use it for |
|---|---:|---|---|
| `Cengage  MECHANICS  1-compressed.pdf` | 454 | Basic Mathematics, Vectors, Units and Dimensions, Motion in One Dimension, Motion in Two Dimensions, Ch 6 (Misc. assignments + archives on ch 1–5), Newton's Laws of Motion (friction, constraint relation, springs, Lami, circular dynamics) | PARTS 1, 2, 3, 4, 5; the work-energy, impulse and circular-motion sections of ch 5 and ch 7 |
| `Cengage MECHANICS 2-compressed.pdf` | 629 | Ch 1 Centre of Mass, Conservation of Linear Momentum and Collision · Ch 2 Rigid Body Dynamics (moment of inertia, torque, angular momentum, **rotational work and power §2.24, work–energy theorem §2.25** — the book's only work-energy treatment) · Ch 3 Fluid Mechanics · Ch 4 Properties of Solids and Fluids (elasticity) · Ch 5 Gravitation | PARTS 6, 7, 8, 9, 11, 12 |
| `CENGAGE  Electro statics and current electricity-compressed.pdf` | 492 | Ch 1 Coulomb's Laws and Electric Field · Ch 2 Electric Flux and Gauss's Law · Ch 3 Electric Potential · Ch 4 Capacitor and Capacitance · Ch 5 Electric Current and Circuit · Ch 6 Electrical Measuring Instruments · Ch 7 Heating Effects of Current · Appendices A1–A3 | PARTS 13, 14, 15 (chs 1–3); chs 4–7 are already shipped notes |
| `Cengage Waves and Thermodynamics-compressed.pdf` | 607 | Unit I Thermal Physics (ch 1 Thermal Properties of Matter, ch 2 Kinetic Theory of Gases and First Law of Thermodynamics, ch 3 archives) · Unit II Oscillation and Waves (ch 4 Linear and Angular SHM, ch 5 Travelling Waves, ch 6 Sound Waves and Doppler, ch 7 Superposition and Standing Waves, ch 8 archives) | **PART 10** (ch 4 + ch 7), and the shipped wave/thermal notes |
| `Cengage. Optics and  Modern Physics. Modern Physics-compressed.pdf` | 588 | Unit I Optics (ch 1 Geometrical Optics, ch 2 Wave Optics) · Unit II Modern Physics: **ch 3 Photoelectric Effect** (photons, photon flux, radiation pressure, de Broglie matter waves, electron emission, photoelectric cell, Einstein's equation, laws, failure of the wave theory) · **ch 4 Atomic Physics** (Thomson model, Bohr model, radii/velocity/frequency/energy, hydrogen-like atoms, ionisation and excitation potentials, limitations, hydrogen spectrum, nuclear-mass effects, atomic collision, **X-rays and Moseley's law, pp. 4.25–4.32**) · **ch 5 Nuclear Physics** (nuclear structure, size, binding energy, Q values, stability, α/β/γ radioactivity, decay law, activity, half-life, average life, dating, decay series and equilibrium, nuclear reactions, fission, reactors, fusion, fusion in the Sun) | PARTS 23, 24, 25, 26 |

Consequences of that map, which override any older note in the repo:

* **X-rays is not a separate chapter in this volume.** It is the second half of **ch 4 Atomic Physics**
  (pp. 4.25–4.32). PART 25 still owns it as a chapter of its own, but its coverage map must be keyed to
  the *section names* inside ch 4.
* **Semiconductors is not in this volume at all** (Unit II holds only chs 3–5). PART 27's floor therefore
  comes from the standard JEE Main/Advanced semiconductor syllabus, and it must say so in its coverage map
  instead of citing a chapter that does not exist. Before writing it, the agent should also grep the other
  four PDFs — if a semiconductors chapter turns up in another volume, cite it.
* **Magnetism, EMI, inductance, AC circuits and matter-and-magnetism are not in these five volumes.** They
  are not "the book's chapter 6 and 7"; they are a standalone volume the repo does not have. The source line
  of PARTS 16–22 therefore names the *standard syllabus headings* (in the PART sections below) as the floor,
  and the agent must build the coverage map from that list plus the shipped `current-electricity/` and
  `electromagnetic-waves/` notes.
* **Everything else is a real chapter in a real PDF**, so the book sweep of §1.12 is compulsory and cheap:
  read the contents page at the page number in this table, then walk the chapter's own headings and tick
  them off in the coverage map.

**How to read a scanned contents page (recipe for agents).** Paginate to the page listed above (the contents
pages sit at PDF indices 4–6, i.e. printed pages v–vii), render it, and read it like a human would. A
five-line python recipe that works with no setup beyond `pip install pymupdf`:

```python
import pymupdf                                   # pip install pymupdf
doc = pymupdf.open("Cengage MECHANICS 2-compressed.pdf")
doc[4].get_pixmap(dpi=150).save("/tmp/contents.png")   # index 4 = the printed 'Contents' page
# then open /tmp/contents.png and read the chapter's heading list
```

Then, for the chapter itself, read its first two or three pages (the contents gives the page number, e.g.
`Chapter 2 Rigid Body Dynamics 2.1`) to see the section order and the exercise structure. **Never quote the
book**: the notes are original prose; the PDFs are there to make the coverage claim true.

## 2 · Teaching doctrine — how an expert teacher orders a chapter

An expert teacher is not someone who knows more physics; it is someone who knows **what to say first**
so that nothing later has to be unlearned. This section is the standard against which every PART is
written.

### 2.1 The ten ordering laws

1. **Phenomenon before formalism.** Block 1 shows what happens (drop a stone, spin a wheel, rub a
   balloon) and only then names the variables. A student who has the picture never confuses the
   symbols; a student who starts with symbols has nothing to attach them to.
2. **One new idea per subsection.** If a subsection needs two new ideas, it is two subsections. The
   test: can a reader state, in one sentence, what was new here?
3. **Define the bookkeeping before using it.** Sign conventions, axes, positive directions, the state
   variables, the frame — settled in block 2, used unchanged for the rest of the chapter. Most JEE
   errors are bookkeeping errors, not physics errors.
4. **Derive before you use.** No formula appears in a problem until it has been derived (or, for a
   genuinely empirical law, stated with the evidence and the limit of its validity). The block-3 order
   is the dependency order of the results, not the book's order.
5. **Every result carries its validity condition, immediately.** Not in a footnote, not at the end of
   the chapter: next to the box, or the reader will apply an ideal-gas result to a real gas and blame
   the physics.
6. **Interleave retrieval.** A worked example lands within 300 words of the theory it uses; a concept
   check lands immediately after a definition; practice follows the archetype it practises. Never park
   a question set at the end of a chapter.
7. **Special → general → special.** Derive the concrete case (one block on a plane, the simple
   pendulum, the single resistor) before the general one, then show the general result collapsing back.
   The collapse is the proof the student understands it.
8. **Say what the limit predicts before computing it.** "At large distances this should look like a
   point charge" — then check. Predicted limits convert algebra into physics.
9. **Name the method when you use it.** "This is the element-and-symmetry method." Named methods are
   transferable; unnamed algebra is not. Every PART ends block 3 with its named-method list.
10. **Teach the trap at the moment it can bite.** A trap box placed at the point of the derivation that
    creates the temptation outperforms a list at the end — but keep the consolidated list in block 8
    too, because that is what the reader revises from.

### 2.2 Bad order versus good order (the standard, demonstrated)

**Bad** (how a formula sheet is ordered): *Biot–Savart law → field of a wire → Ampère's law → torque
on a loop*, with Ampère's law arriving as a *deus ex machina* and the loop's torque derived by
integration only.

**Good** (how the chapter is ordered): Oersted's observation → the force on a moving charge in a field
→ the field *produced* by a moving charge (Biot–Savart) → integrate it once for a straight wire and
once for a loop → notice that a wire's field has circular symmetry, which suggests a loop integral →
**derive** the general form of that integral (Ampère's law) → use the loop form where it is cheaper →
only then define the magnetic moment and the loop torque, now as a two-line consequence of the forces
already known. Nothing is asserted, nothing is used before it is earned, and the last step is a reward
rather than a new burden.

Apply that shape to every PART.

### 2.3 The micro-template of one subsection (copy this rhythm)

```markdown
### 3.6 Why the centre of mass moves as if it held the whole mass

**The claim.** (one sentence, in words, before any symbol)

[ derivation, 3-8 lines, every step justified inline or in a callout ]

> [!info] Why
> The step a book hides: the internal forces cancel in pairs — that is Newton's third law applied to a
> system, and it is the entire content of this result.

> [!warning] Condition of validity
> The model, and the way it fails.

> [!success] Check
> A limit, a dimension or a special case — computed, not asserted.

> [!question] Exam note
> How this appears in a paper; the 20-second version.
```

Every callout needs its own blank line before and after, and every line inside it starts with `> `
(§1.3.1) — that is what makes it render as a box in Obsidian rather than loose quoted text.

Rules for the rhythm: short sentences; the reader is addressed as "you" and is assumed to be holding a
pen in a timed room; no "it is easy to see", no "as everyone knows", no hedging; every symbol
introduced before use; every subsection ends with something the reader can *do*.

### 2.4 Voice and reader contract

* Write for a strong 16–18-year-old who has been taught the topic badly once already. Assume
  intelligence, not prior fluency.
* Correct the reader's likely wrong model out loud, once per block: "you probably think the scale
  reads the weight of the chain; it reads three times that, and here is why."
* Use the reader's own experience as the anchor (the lift, the bicycle, the balloon, the torch bulb,
  the MRI magnet, the phone charger).
* Keep awe available but rationed: one `> [!tip] Insight` callout per block, no more, and it must earn
  its place by changing how a familiar result looks.
* Never end a chapter without telling the reader what they can read next and what they still cannot
  (block 14).

---

## 3 · The parts — how each section is written, and the one idea of each

Every PART section below gives, in this order: the identity line (slug, source chapter, prerequisites);
**the one idea** (the sentence that belongs on page 1 of the notes); the **teaching-order table** (what
to teach in which sequence, and what closes each section); the **must-derive list**; the **DIAGRAM
briefs** that must appear; the **mandatory archetypes**; the **Olympiad-block content**; the **traps**;
the **exit criteria**. If your judgement ever conflicts with the table, the table wins on ordering and
coverage; your judgement governs the prose.

Quick view of the one idea of each chapter (use it as the first sentence of block 0):

| PART | the one idea |
|---:|---|
| 1 | Every measurement is a comparison plus an honest statement of how wrong it could be. |
| 2 | Vectors are the language in which direction stops being an accident of the coordinate system. |
| 3 | Motion is one function $x(t)$; everything else in kinematics is its slope or its area. |
| 4 | Two-dimensional motion is two one-dimensional motions that share a clock. |
| 5 | Force changes momentum, constraints are geometry rather than forces, and friction is a range rather than a number. |
| 6 | Work is energy in transit; energy bookkeeping replaces force bookkeeping whenever path, not time, is the question. |
| 7 | In an isolated system the centre of mass keeps moving in a straight line — every collision is a discussion about the motion around it. |
| 8 | A rigid body is a mass distribution; rotation is the same $F=ma$ story with $I$, $\tau$ and $L$ in the roles of $m$, $F$ and $p$. |
| 9 | Gravity is a central inverse-square field, and every orbit is energy and angular momentum trading places. |
| 10 | If the restoring effect is proportional to the displacement, the motion is sinusoidal — almost everything linear oscillates. |
| 11 | Fluids carry pressure; pressure differences are forces; viscosity and surface tension matter only when the length scale is small. |
| 12 | Elasticity is the macroscopic face of the interatomic spring: moduli are material properties, stiffness is geometry. |
| 13 | The electric field is the bookkeeping device for forces at a distance, and superposition makes every distribution a sum of point charges. |
| 14 | Flux counts field lines through a surface; symmetry turns that count into the fastest way to find a field. |
| 15 | Potential turns a vector problem into a scalar one, at the price of a direction you recover by differentiating. |
| 16 | A magnetic field is what a moving charge calls the relativistic correction to the electric force; its effects are always perpendicular to motion. |
| 17 | Ampère's law is Gauss's law for currents: symmetry plus a loop integral gives the field in one line. |
| 18 | In a magnetic field a charge circles to a clock whose rate depends only on $q/m$ and $B$ — that single fact is an industry. |
| 19 | Matter responds to magnetic fields through induced (dia), aligned (para) or permanently ordered (ferro) dipoles. |
| 20 | A changing magnetic flux drives an electric field, and Lenz's law is energy conservation wearing a disguise. |
| 21 | A coil resists changes in its own current because the energy lives in the field, not in the wire. |
| 22 | In AC everything is a phase relationship; impedance is resistance that knows about time. |
| 23 | Light delivers its energy in indivisible quanta, and matter waves are the same fact seen from the other side. |
| 24 | Atoms have discrete levels because an electron is a standing wave, not a planet. |
| 25 | X-rays are photon physics with enough energy to see atoms and to knock electrons free — and they prove the photon carries momentum. |
| 26 | Nuclei are bound by a short-range saturated force, and the binding-energy curve decides which way the energy flows. |
| 27 | Bands and doping turn a poor conductor into a controllable one — the whole of electronics in two ideas. |
| 28 | Space and time are part of the physics rather than a stage; $c$ is the same for everyone and everything else bends to keep it so. |

---

## 4 · The 28 parts

> Each part is self-contained: hand an agent only its section (plus §0–§2 and Appendix C) and it can
> write the chapter without asking a question. "Blocks" are the 15 note blocks of §1.4; "PART" is this
> plan's chapter number.

### PART 1 · Units, Dimensions & Measurement Errors

`units-measurements` · folder `units-measurements/` · source: Cengage *Mechanics I* **ch 3 Units and
Dimensions** (contents p. 3), with **ch 1 Basic Mathematics** folded in as a 2-page appendix of the
calculus you will actually use (derivatives, integrals, binomial approximation, maxima–minima) · needs
nothing ·
JEE Advanced · NSEP · INPhO · IPhO (the IPhO data-analysis floor).
*The one idea:* every measurement is a comparison plus an honest statement of how wrong it could be.

| # | Section | Teach this, in this order | Closes with |
|---:|---|---|---|
| 1 | Why units exist | The three base decisions (standard, name, symbol); why SI chose its seven bases; derived units as *products and quotients of bases* | A concept check: is the litre a base unit? Is the radian? |
| 2 | SI in practice | Base + derived + supplementary units, prefixes, the kilogram's definitional history (artefact → Planck constant), unit hygiene in writing answers | A table of the 20 units you must never mis-write |
| 3 | Dimensions | Dimensional formulae derived from *definitions* (force, energy, power, pressure, modulus, viscosity, surface tension, $G$, $h$, $R$, $\varepsilon_0$, $B$) — one row per constant | Dimensional-formula table + a check that each came from a definition |
| 4 | Homogeneity and its limits | The principle of homogeneity; using it to *test* an equation; the three things it cannot do (find dimensionless constants, distinguish added like-dimension terms, catch a factor of 2) | A "spot the impossible equation" drill |
| 5 | Dimensional derivation | Deriving relations: the pendulum's period, the terminal speed of a falling drop, the stress in a wire, Kepler's third law — each with the missing-constant caveat stated | One derivation the reader does alone |
| 6 | Dimensionless groups | Why ratios of like quantities control behaviour; the idea of a similarity parameter (Reynolds, Mach, Froude previewed, derived in the later PARTs) | A "which group decides this?" table |
| 7 | Significant figures and rounding | Rules, why they exist, when to keep one extra, the catastrophic-cancellation warning, the "never round intermediate values in a multi-step problem" rule | A rounding drill with answer keys |
| 8 | Errors I: classification | Systematic vs random vs gross; accuracy vs precision; calibration, zero error, parallax, least count, backlash | The error budget table of a real experiment |
| 9 | Errors II: propagation | Derive the propagation rules by differentiation for sums, differences, products, quotients and powers; then the honest statement that independent random errors combine in quadrature while systematic ones add linearly | Derive $\Delta Z/Z$ for $Z = a^2b/c^3$ and for $Z=(a-b)$ |
| 10 | Instruments | Vernier caliper (least count, zero error, why 0.1 mm works), screw gauge (pitch, circular scale, zero error, ratchet), travelling microscope, the metre scale — each with the "what can go wrong on the bench" list | A worked read-the-instrument set (three diagrams-briefs, three answers) |
| 11 | Graphs and data | Slope/intercept with units, linearisation (log–log, $T^2$ vs $L$), best-fit vs max–min slope, error bars, why a straight line is the goal | A log-log plot extraction of an exponent from a small data table |
| 12 | Estimation | Fermi method: bracket the answer, choose the right model, carry the units; three fully worked estimates (how many breaths in a life; the mass of the atmosphere; the number of photons in this room's light) | Two estimates the reader does alone |

**Must be derived, not stated:** the propagation rules (by differentiation, including the power rule
for $Z=x^n$); the quadrature rule's origin (independent random errors add as variances — state the
result and justify with a two-error example); the linearisation of $T=2\pi\sqrt{L/g}$ and of $y=ax^n$;
the least-count argument for a vernier.

**DIAGRAM briefs (D1.1–D1.14):** vernier scale with main scale and vernier coincidence; screw gauge
with the circular scale reading and a zero error; a source's systematic offset on a repeated-measurement
histogram; the error-bar + max–min-slope construction on a straight-line fit; log–log plot of $T$ vs $L$
for a pendulum; the "how big is the error of $\sin\theta\approx\theta$" percentage-error curve; a
micrometer's pitch geometry; chain of a real error budget. (12 minimum; more is better.)

**Mandatory archetypes (block 6):** unit conversion with squared/cubed units; check-the-equation
dimensional drills; derive-a-formula-by-dimensions; find the exponent from data; propagation through a
multi-step formula; vernier/screw-gauge reading with zero error; the "which measurement limits this
result" question; significant-figure rounding of a computed answer; the order-of-magnitude estimate;
the "is this graph linearisable?" judgement.

**Olympiad block content:** standard error of the mean and why repeating $N$ times divides
the random part of the error by $\sqrt N$; least-squares fitting — derive the normal equations for a
straight line and compare with the graphical max–min method; $\chi^2$ as a goodness-of-fit number and
when a straight line is not good enough; the Buckingham $\pi$ theorem (statement, then applied to the
pendulum and to the blast-radius problem $R \propto (Et^2/\rho)^{1/5}$); the "how precisely can you
measure $g$ with this pendulum?" design problem (choose the length, the amplitude, the number of
oscillations from the error analysis); reconstructing Avogadro from an oil film/Rutherford-style
estimate; the SI redefinition (why the kilogram died in 2019) as a reading exercise; the
non-inverses: why dimensional analysis fails for the pendulum's amplitude correction
$\theta_0^2/16$.

**Traps to plant:** adding percentage errors instead of propagating them; treating $\Delta(a/b)$ as
$\Delta a/\Delta b$; using the "one extra significant figure" rule to keep four digits in an answer
written to two; forgetting that a vernier's zero error is *subtracted*; using dimensional analysis to
"prove" a formula that has a dimensionless constant; confusing accuracy with precision; quoting an
answer to six figures from two-figure data.

**Exit criteria:** the dimensional-formula table covers ≥ 25 quantities; the four derivation-by-
dimension worked examples are complete; both instruments have full reading procedures + zero-error
handling; the error-propagation block derives (not quotes) every rule; ≥ 3 Fermi estimates fully
worked; the Olympiad block has the least-squares derivation and the $\pi$-theorem application; the
coverage map accounts for the Basic-Mathematics appendix.

---

### PART 2 · Vectors & Vector Algebra

`vectors` · folder `vectors/` · source: Cengage *Mechanics I* **ch 2 Vectors** · needs nothing ·
JEE Advanced · NSEP.
*The one idea:* vectors are the language in which direction stops being an accident of the coordinate
system.

| # | Section | Teach this, in this order | Closes with |
|---:|---|---|---|
| 1 | Why vectors | Scalars vs vectors; displacement vs distance; the failure of "3 km north plus 4 km east = 7 km"; equality, negative, free translation of a vector | A concept check on which quantities are vectors (work? current? area? torque?) |
| 2 | Two laws of addition | Triangle law from walking, parallelogram law from two pulls; the resultant's magnitude range $\lvert a-b\rvert \le R \le a+b$; subtraction as adding the negative | A three-vector equilibrium check |
| 3 | Components | Basis vectors, resolution along axes, the "any two perpendicular directions" freedom, why the choice of axes is a tool and not a law; resultant from components | Resolve a 3-force system and prove equilibrium |
| 4 | Unit vectors | Unit vector of a vector, direction cosines, $\hat r$ in 2-D and 3-D; vector from two points | Direction-cosine problem |
| 5 | Dot product | Definition from work done; projection interpretation; distributivity; $\lvert a\pm b\rvert^2$ identities; the perpendicularity test; the angle between vectors in 3-D | Angle between two lines in a cube |
| 6 | Cross product | Definition, right-hand rule, magnitude as area of the parallelogram, direction as normal, anti-commutativity, distributivity; component determinant form | Area of a triangle from two vectors; torque preview |
| 7 | Triple products | Scalar triple product = volume of the parallelepiped and the coplanarity test; vector triple product $\mathbf a\times(\mathbf b\times\mathbf c)=\mathbf b(\mathbf a\cdot\mathbf c)-\mathbf c(\mathbf a\cdot\mathbf b)$ with a proof sketch and a worked use | Coplanarity drill |
| 8 | Vector equations | Solving $\mathbf r$ from $(\mathbf r-\mathbf a)\cdot\mathbf b=0$, $\mathbf r\times\mathbf a=\mathbf b$ and friends; uniqueness and non-uniqueness; the locus interpretation of a vector equation | Two vector-equation problems with a sketch brief |
| 9 | Vector calculus you will need | Derivative of a vector; the product rules for $\frac{d}{dt}(\mathbf a\cdot\mathbf b)$ and $\frac{d}{dt}(\mathbf a\times\mathbf b)$; the rotating unit vector $\dot{\hat r}=\omega\hat\theta$ (used in PART 4 and PART 8) | Differentiate $\mathbf r=r\hat r$ to get velocity in polar form |
| 10 | Choosing coordinates | Cartesian vs polar vs "along the incline": a decision table with three worked examples showing the time saved | The reader redoes one problem in two coordinate systems |

**Must be derived, not stated:** the parallelogram law's component proof; the projection formula
$\mathbf a\cdot\hat b$; the area formula $\tfrac12\lvert\mathbf a\times\mathbf b\rvert$; the vector
triple product identity (by components); the polar-velocity identity $\mathbf v=\dot r\hat r+r\omega\hat\theta$.

**DIAGRAM briefs (D2.1–D2.12):** triangle law with the head-to-tail construction; parallelogram law with
the diagonal and the angle $\theta$; resolution into components with $\theta$ measured from each axis
(the classic confusion); dot product as projection (shadow diagram); cross product as area with the
right-hand rule; the right-hand-rule corner check; scalar triple product as a parallelepiped; a vector
equation's locus (a line/plane); the polar basis $\hat r,\hat\theta$ on a curved path; direction
cosines in a 3-D box; the cube angle problem; a 3-force equilibrium triangle.

**Mandatory archetypes:** resultant of $n$ vectors by components; minimum resultant of two vectors;
angle between two vectors from components; work as a dot product; torque/area as a cross product;
coplanarity; a vector equation with a parameter; relative-vector setup (used again in PART 4);
3-D line/shortest-distance flavour; velocity in polar coordinates via differentiation.

**Olympiad block content:** the Lagrange identity $\lvert \mathbf a\times\mathbf b\rvert^2 =
\lvert a\rvert^2\lvert b\rvert^2-(\mathbf a\cdot\mathbf b)^2$ with its trigonometric interpretation;
the general proof of the vector triple product and the Jacobi identity $\mathbf a\times(\mathbf
b\times\mathbf c)+\dots=0$ (as a "why the cross product is not associative" insight); vector equations
solved by dotting with a clever vector (the "kill the cross product" technique); the spherical basis
$\hat r,\hat\theta,\hat\phi$ and the fact that their time derivatives are non-zero — with the
derivation $\dot{\hat r}=\boldsymbol\omega\times\hat r$ used for rotating frames in PART 8; areas and
volumes by vector methods (a triangle's area from three points, the volume of a tetrahedron); the
rotating-frame velocity and acceleration preview $\mathbf a = (\ddot r - r\omega^2)\hat r +
(r\alpha+2\dot r\omega)\hat\theta$ derived as a *pure vector-algebra exercise* (this becomes circular
motion in PART 4 and Coriolis in the olympiad extensions).

**Traps to plant:** taking components with the angle measured from the wrong axis; writing
$\mathbf a\cdot\mathbf b = ab$ (dropping $\cos\theta$); assuming $\mathbf a\times\mathbf b
=\mathbf b\times\mathbf a$; cancelling a vector from both sides of a dot or cross equation; treating
$\lvert\mathbf a+\mathbf b\rvert = a+b$; resolving along non-perpendicular directions without the
projection formula; mixing up $\hat r$ (variable) with $\hat i$ (constant).

**Exit criteria:** the dot/cross/triple-product blocks each derive their formula and each have ≥ 2
worked problems; the polar-velocity derivation is present (PART 4 depends on it); ≥ 3 problems requiring
the reader to *choose* coordinates; the "vector calculus you will need" block covers both product rules.

---

### PART 3 · Motion in One Dimension

`kinematics-1d` · folder `kinematics-1d/` · source: Cengage *Mechanics I* **ch 4 Motion in One
Dimension** · needs PART 1, PART 2 · JEE Advanced · NSEP · INPhO.
*The one idea:* motion is one function $x(t)$; everything else in kinematics is its slope or its area.

| # | Section | Teach this, in this order | Closes with |
|---:|---|---|---|
| 1 | Frames and the description of motion | Frame of reference, position, the arbitrary origin (and why the physics does not care), the particle model and its validity | "Is the passenger moving?" concept check |
| 2 | Distance and displacement | Path length vs displacement, the round-trip trap, displacement as a signed quantity | A "find distance and displacement" pair of drills |
| 3 | Average and instantaneous | Average velocity vs average speed; instantaneous as the limit; the harmonic-mean trap for two equal distances | Two-equal-halves problem, done both ways |
| 4 | $x$–$t$ graphs | Slope = velocity; the sign of the slope; reading a real journey off a graph; drawing the graph from a story | Sketch the graph of a bouncing ball's $x(t)$ |
| 5 | Acceleration | Second derivative, the curvature of $x$–$t$, the sign of acceleration vs the sign of velocity (the "slowing down or speeding up?" rule) | A sign-analysis drill table |
| 6 | The graph trio | $x$–$t$, $v$–$t$, $a$–$t$: differentiation down, area up (with sign); "which graph is impossible?" logic; the turning point where $v=0$ but $a\neq0$ | Reconstruct one graph from another, three times |
| 7 | Constant acceleration | Derive $v=u+at$, $s=ut+\tfrac12at^2$, $v^2=u^2+2as$, $s=\tfrac{u+v}{2}t$ by integration; the $n$-th-second formula and the ratio tricks ($1:3:5$, $\sqrt1:\sqrt2:\dots$) | A 6-part problem set on the ratio tricks |
| 8 | Free fall | $g$, the sign convention, dropped vs thrown, two bodies meeting, the lift problem; the "up and down are symmetric" theorem | Three-body free-fall problem |
| 9 | Variable acceleration I | $a=f(t)$: integrate twice with the constants from initial conditions; $a=f(v)$: separate $\frac{dv}{dt}=f(v)$; the exponential case | A retarding-force problem done two ways |
| 10 | Variable acceleration II | $a=f(x)$ via $v\frac{dv}{dx}=a$; the velocity-from-force curve; energy preview (the same integral) | A spring-force problem solved by the $v\,dv/dx$ route |
| 11 | Relative motion in 1-D | Relative position/velocity, the "closing speed" of two bodies, the meeting condition, the classic "two trains and a bird" | Bird-and-trains problem, two ways |
| 12 | Motion with changing direction | Piecewise kinematics: the ball thrown up from a cliff, the particle that reverses, the distance travelled vs displacement | A cliff problem with the full $v$–$t$ sketch brief |

**Must be derived, not stated:** the three constant-acceleration equations (by integration); the
$n$-th-second result; $v\,dv/dx=a$ (chain rule); the meeting time of two uniformly accelerated bodies;
the symmetry of the up-and-down phase; the harmonic-mean average speed for two equal distances.

**DIAGRAM briefs (D3.1–D3.13):** the $x$–$t$/$v$–$t$/$a$–$t$ triad for one motion (three aligned
panels); the three "possible/impossible" graph cases with their reasons; a bouncing ball's piecewise
$x(t)$ with the energy loss visible; the free-fall parabola with $h$–$t$ and the velocity at impact;
the up-and-down symmetry with the same speed at the same height; the $v$–$dv/dx$ integration picture as
area under the force curve; two trains' relative position graph; the "sign of $v$ and $a$" quadrant
chart; a retarding car's velocity decay with the terminal value; the reaction-time rectangle in the
stopping-distance diagram; a multi-stage journey graph.

**Mandatory archetypes:** read a graph and answer three questions; pick the graph matching a story;
constant-acceleration two-body meet; free fall with a delay; distance vs displacement on a reversal;
$a=f(v)$ exponential approach to terminal speed; $v\,dv/dx$ integration; relative velocity of two
bodies in 1-D; ratio tricks for equal time intervals; average speed over two equal distances and over
two equal times (compare!); the "braking distance scales as $v^2$" question.

**Olympiad block content:** linear drag $\dot v = -kv$ (derive $v(t)$, $x(t)$, the terminal speed, the
stopping distance, and the "half-life" of the velocity) and quadratic drag $\dot v = -kv^2$ (derive the
time to stop and the distance, then compare the two laws' stopping distances at two speeds); the
exponential–hyperbolic contrast $\tanh$/$\tan$-type solutions and their limits; motion in a
distance-dependent force with the $v\,dv/dx$ method to get the speed profile; the pursuit problem with a
constant-speed chaser and a linearly moving target; two-body relative motion with acceleration (the
closing-time equation); the "does a heavier body fall faster with drag?" analysis (terminal speed vs
$m$, and the mass dependence of the terminal speed of a raindrop); estimating drag coefficients
from $F=\tfrac12\rho C_dAv^2$ for a car and for a cyclist; the "braking with reaction time" design
problem (the safe-distance formula and the 2-second rule); relativistic 1-D kinematics as a limit-preview
(this result belongs to PART 28 — link forward, do not derive here).

**Traps to plant:** treating deceleration as a negative $a$ without checking the sign of $v$; using
$s=\frac{u+v}{2}t$ when $a$ is not constant; taking the average of two speeds for equal distances (the
harmonic mean, not the arithmetic one); forgetting the second integration constant; using $v^2=u^2+2as$
with a negative $s$ mishandled; assuming the fastest point of a journey is the halfway point; forgetting
that $v=0$ does not imply $a=0$.

**Exit criteria:** graph reading is taught as a skill (block 1–6) before any equation; every one of the
four constant-acceleration equations is derived; the $a=f(v)$ and $a=f(x)$ routes both appear; the drag
analysis is in block 10 with two drag laws; ≥ 2 problems require naming the method before doing algebra.

---

### PART 4 · 2-D Motion: Projectiles, Relative Velocity & Circular Kinematics

`motion-in-two-dimensions` · folder `motion-in-two-dimensions/` · source: Cengage *Mechanics I* **ch 5
Motion in Two Dimensions** (+ the ch 6 archives/exercise patterns) · needs PART 2, PART 3 · JEE Advanced · NSEP · INPhO.
*The one idea:* two-dimensional motion is two one-dimensional motions that share a clock.

| # | Section | Teach this, in this order | Closes with |
|---:|---|---|---|
| 1 | The independence principle | Why $x$- and $y$-motions do not talk to each other; the shared clock; the vector form $\mathbf r=\mathbf r_0+\mathbf u t+\tfrac12\mathbf a t^2$ | A concept check: which quantity is common to both axes? |
| 2 | Relative velocity in 2-D | $\mathbf v_{AB}=\mathbf v_A-\mathbf v_B$, the vector triangle; rain-and-man; aircraft-and-wind; the general "meet/catch" condition | Rain problem done by vector triangle *and* by components |
| 3 | River crossing | Minimum-time crossing (aim straight across, drift $=v_rT$) and minimum-drift crossing (aim upstream, $\sin\theta=v_r/v_b$, drift zero if $v_b>v_r$) — derive both, then plot the trade-off | A two-part river problem with both optima |
| 4 | Oblique projectile: time and height | Derive $T=\frac{2u\sin\theta}{g}$, $H=\frac{u^2\sin^2\theta}{2g}$ from the two 1-D problems; the "same clock" check | Prove $T$ is twice the rise time |
| 5 | Oblique projectile: range | Derive $R=\frac{u^2\sin2\theta}{g}$; maximum range at 45°; complementary angles give equal ranges; the ratio table $R:H:T$ | The "which angle gives $R=H$?" problem |
| 6 | The trajectory equation | Eliminate $t$ to get $y=x\tan\theta-\frac{gx^2}{2u^2\cos^2\theta}$; use it to hit a target, to find the launch angle for a given point, and to check the direction of motion | A "hit the point $(x,y)$" problem with two solutions |
| 7 | Projection from a height | Horizontal projection; projection from a tower at an angle; the "throw up first" case; time vs horizontal distance | Cliff problem with the $v$–$t$ components sketched |
| 8 | On an incline | Projectile up/down an incline: derive $R$, $T$, $H$ in the rotated frame (the "choose the axes along the plane" method) and the maximum range on an incline | Two-part incline problem |
| 9 | The safety parabola and envelopes | For a fixed $u$: the region of reachability. Derive $y=\frac{u^2}{2g}-\frac{gx^2}{2u^2}$ and its uses (minimum speed to hit a point, the "can it clear the wall?" test) | "Minimum launch speed to hit $(x,y)$" |
| 10 | Circular motion kinematics | Angular position/velocity; $v=\omega r$; the derivation of $a_c=v^2/r=\omega^2r$ **twice** (the limiting-difference construction and the rotating-unit-vector derivative); the $v$–$\omega$ vector relation | A concept check: what is the acceleration at constant speed? |
| 11 | Non-uniform circular motion | Tangential and radial components; $a_t=\alpha r$; the total acceleration's direction; the radius of curvature $\rho=v^2/a_\perp$ and its use in projectiles | Compute $\rho$ at the apex and at launch for a projectile |
| 12 | Relative angular velocity | Two bodies on circles; the angular velocity of the line joining them; the "minimum distance" and "closest approach" problems | Closest-approach problem of two moving points |

**Must be derived, not stated:** $T$, $H$, $R$ (from the two 1-D problems, never quoted); the trajectory
equation; the $R,H,T$ ratio relations; the two derivations of $a_c$; $\rho=v^2/a_\perp$; the incline
results by rotating the axes; the safety-parabola envelope; the minimum-drift river condition.

**DIAGRAM briefs (D4.1–D4.16):** projectile trajectory with the velocity components drawn at three points
(launch, apex, landing) and the angles marked; the $R$–$H$–$T$ annotation on one trajectory; complementary
angles 30°/60° sharing a range; the horizontal-projection-from-a-tower geometry with the two
displacements; projection from a cliff at an angle above/below the horizontal; the incline problem with
the rotated axes drawn; the safety parabola with three sample trajectories tangent to it; the
rain-and-man vector triangle; the river-crossing drift diagram for both optima; the aircraft-wind
vector triangle; the centripetal-acceleration limit construction ($\Delta\mathbf v$ from two nearby
velocity vectors); the polar basis on a circle with $\hat r,\hat\theta$; tangential and radial
acceleration components on a non-uniform circle; radius of curvature at two points of a trajectory;
closest-approach geometry for two moving points; the "wall clearance" diagram.

**Mandatory archetypes:** projectile hitting a target on a wall; projectile over a fence (does it clear?);
find $\theta$ from $R$ and $H$; two projectiles at complementary angles; range on an incline; time of
flight with a vertical wind/acceleration (e.g. a constant horizontal force); projectile inside a lift
or on a moving trolley; river-crossing minimum time; river-crossing minimum drift; rain relative
velocity with an umbrella angle; aircraft ground-speed with a crosswind; two-body closest approach;
centripetal acceleration in a conical/vertical circle setup (setup only — dynamics is PART 5);
projectile in a uniform electric field (identical mathematics — hand-off to PART 13); a
relative-velocity chase with the "minimum distance" answer.

**Olympiad block content:** projectiles with drag — set up the equations ($\ddot x=-kv_x$,
$\ddot y=-g-kv_y$) and solve the horizontal part exactly and the vertical part exactly, then find the
asymptotic behaviour and the range shortfall; the optimum drag-limited range (statement + numeric
comparison with the vacuum range); the envelope with an added headwind; the "hit a moving target"
optimisation (the relative-motion method: solve in the target's frame); the launch-angle problem for a
target above an incline and the two-solution condition; the radius of curvature and the "where does the
trajectory have the largest curvature" result; the conical-spiral problem (a particle with constant
radial speed on a turntable — an elegant $(\ddot r-r\omega^2)$ problem); Coriolis deflection of a
projectile over a long range (order-of-magnitude: the $10^{-5}$ fractional effect); the "how fast can a
stone be thrown?" biomechanical estimate (order of magnitude with a real number: ~25 m/s); the
cycloid/brachistochrone mentioned but not solved (as an "ask a harder question next year" pointer); the
minimum-speed interception problem (two moving objects, a rendezvous condition).

**Traps to plant:** using $R=u^2\sin2\theta/g$ for a projectile landing at a different height; assuming
the apex is the midpoint in time when a wall intervenes; forgetting that $v_x$ is constant *only* in
vacuum (see "wind"); treating $a_c$ as a force rather than an acceleration (it becomes the force's
*result* in PART 5); using $v=\omega r$ with $\omega$ in degrees per second; forgetting that "minimum
time" and "minimum drift" river problems have different aims; thinking the velocity at the top of a
projectile is zero.

**Exit criteria:** all three projectile results derived twice (once by components, once from the
trajectory equation); the two derivations of $a_c$ present; the incline and envelope sections complete
with their own problems; the relative-velocity block has all four classic problems (rain, river ×2,
aircraft); the Olympiad block contains a drag derivation and ≥ 3 estimates.

---

### PART 5 · Newton's Laws, Friction, Constraints & Circular Dynamics

`newtons-laws` · folder `newtons-laws/` · source: Cengage *Mechanics I* **ch 7 Newton's Laws of
Motion** — force classification, impulse, free-body diagrams, tension, friction, spring forces,
non-inertial frames, Lami's theorem, constraint relations (pulley/wedge/spring combinations) and
dynamics of circular motion · needs PART 4 · JEE Advanced · NSEP · INPhO · IPhO (friction and constraint
methods are olympiad core).
*The one idea:* force changes momentum, constraints are geometry rather than forces, and friction is a
range rather than a number.

| # | Section | Teach this, in this order | Closes with |
|---:|---|---|---|
| 1 | Inertia and the first law | What a force-free body does; frames in which the first law holds; the honest statement that "inertial frame" is defined by the law | Which of these frames is inertial? concept check |
| 2 | The second law | $\mathbf F_{\text{net}}=m\mathbf a$ as a *vector* statement; $\mathbf F=\frac{d\mathbf p}{dt}$ and when the two differ; the impulse preview | A two-axis $F=ma$ drill |
| 3 | The third law | Action–reaction pairs, the "same type of force, different bodies" rule; why internal forces cancel only in a *system* calculation; pushing-a-block-against-a-wall examples | Identify the reaction partner for six common forces |
| 4 | FBD discipline | The five-step method (isolate → external forces only → axes along the acceleration → components → solve); the "never draw the force the body exerts" trap | Three FBDs drawn and solved |
| 5 | Standard forces | Weight, contact normal (and why it is *not* always $mg$), tension in a massless string, spring force preview, hinge/rope reactions; the "ideal string, ideal pulley" assumptions and what changes when they fail | A lift problem with the apparent-weight table |
| 6 | Equilibrium | Concurrent forces, Lami's theorem (derived by sine rule), three-force bodies, the balance of a hanging sign, the rod-on-a-wall problem (with friction, done properly) | Lami's-theorem problem plus a two-surface contact problem |
| 7 | Friction I: static | How static friction adjusts itself; $f\le\mu_sN$ as a *range*; determining the direction by asking "which way would it slip?"; the friction cone and the angle of repose | Block on a rough incline in three regimes |
| 8 | Friction II: kinetic and the modelling | $\mu_k<\mu_s$; the independence of area and speed (with the honest limits); rolling friction; the "we assume $\mu_s=\mu_k$" convention and when it ruins an answer | The friction-graph concept check ($f$ vs applied $F$) |
| 9 | Friction III: systems | Two stacked blocks with a horizontal push (find the maximum force before slipping, both blocks accelerated); the block over a plank; the minimum force to move a block ($\tan\theta=\mu$ optimum — derived); the wedge with friction | Stacked-block limit problem, both cases |
| 10 | Constraints | The method: write the geometric relation (string length, rod length, contact distance), differentiate once for velocity and twice for acceleration; strings (fixed and movable pulleys), wedges, blocks on a rod, the two-block-with-a-vertical-string case | Movable-pulley and wedge problems solved by the constraint method |
| 11 | Pseudo forces | Non-inertial frames, $ma_{\text{frame}}$ in the opposite direction, when this *saves* time (the accelerating lift, the braking bus, the accelerating wedge); the honest warning to master inertial frames first | Accelerating-lift problem both ways |
| 12 | Circular dynamics | The radial equation $\Sigma F_{\text{radial}}=mv^2/r$ and the fact that the centripetal force is a *resultant*, not a new force; conical pendulum; horizontal circle with friction; banking (derive both friction limits) | Banked-road maximum-speed derivation |
| 13 | Vertical circle | String (tension $\ge0$), rod (speed $\ge0$), the minimum speed at the top $v=\sqrt{gR}$, the tension as a function of angle, the "where does the string slack?" problem | Full vertical-circle analysis with a graph of $T(\theta)$ |
| 14 | Multi-body systems with an eye on PART 7 | The "system + parts" duality: solve by system $F=ma$ and by isolating; the reason the block-with-wedge needs both methods; the rocket/variable-mass pointer | A four-block pulley system solved twice |

**Must be derived, not stated:** Lami's theorem; the friction-cone result $\tan\theta=\mu_s$; the
minimum-force-to-move result; the constraint relations for pulley systems and wedges (by
differentiation, always); the banked-road limits with and without friction; the vertical circle's
minimum speeds and the tension profile; the apparent weight in an accelerating lift.

**DIAGRAM briefs (D5.1–D5.18):** four different free-body diagrams on one page (inclined plane, lift,
pulley pair, stacked blocks); the friction force vs applied force graph with the $\mu_s$ peak and $\mu_k$
plateau; the friction cone and angle of repose geometry; the stacked-block-with-push geometry with the
"which block slips first" arrow; the minimum-force-to-drag-a-block diagram with the optimum angle; the
pulley-and-strings constraint-length labelling; the movable pulley's displacement relation
($h$ vs $2h$); the wedge-block constraint triangle; the lift with a weighing scale and the three cases;
the banked road with the friction force drawn along the incline in both extreme cases; the conical
pendulum with the two-force triangle; the horizontal-circle-on-a-table-with-a-hole setup; the vertical
circle at four angles with $T$, $mg$ and the direction to the centre marked; the $T(\theta)$ and
$v(\theta)$ graphs for a vertical circle; the string-slack criterion picture; the wedge pushed so the
block does not slide ($\mu$ threshold); a two-pulley single-string system; the "block on an accelerating
trolley" FBD in the non-inertial frame.

**Mandatory archetypes:** block on a rough incline, all three regimes; two blocks in contact pushed
horizontally; blocks over a pulley (Atwood, and Atwood with an incline); the "what happens first"
stacked-block limit; the minimum-force angle-dependence problem; the lift with a spring balance; the
block that never slips (any incline angle, because the acceleration is bounded — a beautiful concept
question); conical pendulum period; banked road with a design speed; the car on a curve with ice; the
vertical circle's minimum speed; a bead on a rotating hoop (setup, then the position-dependent normal);
the two-block constraint problem; the "unbalanced pulley with a hanging mass and a mass on a table"
energy-versus-force duality.

**Olympiad block content:** the general constraint method formalised (virtual work in one worked
example: the block-on-wedge problem solved by the "work of the constraint forces is zero" argument —
a preview of the Lagrange viewpoint, entirely elementary); the falling-chain-on-a-scale problem
(the reading is three times the weight of the landed part — derived by momentum flux, with the "where
does the energy go?" audit); the rocket equation derived from the variable-mass form
$m\,dv/dt=F_{\text{ext}}+v_{\text{rel}}\,dm/dt$ and applied to a two-stage estimate; sand falling onto
a conveyor belt (the force is not $mg$ — the momentum-flux derivation, then the power and the
"why the belt's power is twice the kinetic energy rate" resolution); the "block on a wedge that is
pushed" problem with friction, solved by the non-inertial frame; the friction-direction paradox (a
block on a rotating turntable with an inward force); the brachistochrone-adjacent "quickest descent on
two planes" comparison with free fall; bead-on-a-rotating-hoop stability (the $\omega$ threshold, and the
"why the symmetric position becomes unstable" argument); a rope sliding off a table with friction
(integrating $F=ma$ on a variable-mass configuration); Coulomb's friction at an angle of attack (the
belt drive, the capstan equation $T_2=T_1e^{\mu\theta}$ — stated and applied, with a derivation by
integrating over an element); the "how does a climber use a friction hitch?" (application of the
capstan result); the minimum coefficient of friction for a car to go around a banked curve at a
*given* speed (design problem).

**Traps to plant:** drawing the "reaction to the weight" as a normal force on the same body; adding
$mv^2/r$ as if it were a real force on the FBD; using $\mu_s$ and $\mu_k$ interchangeably; assuming
$N=mg$ on an incline or in a lift; forgetting that the constraint relates *displacements*, not forces;
using the pseudo force in the wrong direction; assuming a rope stays taut through a whole motion
(the "when does the string slack?" question); the "block never slides on any incline if the whole
system falls freely" insight; the friction force on a wheel (rolling friction vs static friction).

**Exit criteria:** the friction section is split into three (static, kinetic, systems) and each has a
trap box; constraint motion is taught as a *method* with ≥ 3 configurations; circular dynamics derives
the banked-road limit; the vertical-circle section covers string, rod and the general $T(\theta)$; the
Olympiad block includes the chain-on-scale, the rocket and the capstan problems.

---

### PART 6 · Work, Energy & Power

`work-energy-power` · folder `work-energy-power/` · source: Cengage *Mechanics II* **ch 2 Rigid Body
Dynamics §2.24–2.26** — rotational work and power, the work–energy theorem, conservation of mechanical
energy (the volume has no separate work-energy chapter; this is its only work-energy treatment) — plus
ch 1 §1.17–1.19 on impulse · needs PART 5 · JEE Advanced · NSEP · INPhO · IPhO.
*The one idea:* work is energy in transit; energy bookkeeping replaces force bookkeeping whenever path,
not time, is the question.

| # | Section | Teach this, in this order | Closes with |
|---:|---|---|---|
| 1 | Work by a constant force | $W=\mathbf F\cdot\mathbf d$; positive, negative, zero; the "who does work on whom" bookkeeping; the convention that the *agent* is named | A six-case work-sign drill |
| 2 | Work by a variable force | $W=\int\mathbf F\cdot d\mathbf r$; the area under the $F$–$x$ curve; work in 2-D along a path; the "same endpoints, different path" example | Work along two paths in a field |
| 3 | The work of the standard forces | Gravity (path independent), friction (path length dependent), normal force (zero when the surface does not move — and non-zero when it does), tension (zero for a fixed pulley, non-zero for a moving one), spring ($\tfrac12kx^2$ derived by integration) | The accelerating-wedge normal-force check |
| 4 | The work–energy theorem | Derive $W_{\text{net}}=\Delta K$ from $F=ma$ and the chain rule; the theorem for a system vs a particle (the honest statement about internal work) | A particle problem solved by WET and by $F=ma$ |
| 5 | Power | Average and instantaneous power, $P=\mathbf F\cdot\mathbf v$; the "constant-power climb" problem; efficiency | A car's power-limited top speed derivation |
| 6 | Conservative forces | The two tests (closed-loop work zero; work depends on endpoints only); path-independence and the existence of a potential; the field from the potential | Test four force fields for conservativeness |
| 7 | Potential energy | $U=-\int F\,dx$ and the additive-constant freedom (with the "only differences matter" rule); $U_{\text{grav}}=mgh$ (near the surface), $U_{\text{spring}}=\tfrac12kx^2$; the spring's zero point | Derive $U$ for a force $F=-kx^3$ |
| 8 | Mechanical energy conservation | Derive $K+U$ constancy from WET + conservative forces; the *precise condition* (only conservative forces do work); what to do when friction acts (the dissipated-energy ledger) | A friction-on-incline energy ledger problem |
| 9 | Energy diagrams | $U(x)$ graphs: turning points, the kinetic-energy as a vertical gap, bound vs unbound, equilibrium points and their stability via $U''$; reading a physical story off a curve | A "desert" or "volcano" $U(x)$ problem |
| 10 | The energy method in practice | The decision rule: use energy when the question is "how fast / how far / does it reach?", force when the question is "how long / when / what is the contact force?" — with four worked comparisons | Which method for this problem? drill |
| 11 | Systems and internal work | Two blocks and a spring; the block-and-wedge (the wedge moves, so the block's normal force does work — the "where does the work go?" analysis); kinetic-energy partitions between bodies | Block-and-wedge problem by two methods |
| 12 | Power in practice | Pumps, elevators, hydroelectric plants, vehicles with drag; the "power to climb" and "power to accelerate" split; the fuel-economy vs speed estimate | A pump's power and efficiency problem |
| 13 | Force from potential energy | $F_x=-dU/dx$ in 1-D; the gradient in 2-D and 3-D (statement + use); the "which way does the force point?" rule; equilibrium and stability in 2-D | A $U(x,y)$ problem |
| 14 | Non-conservative bookkeeping | Friction, drag, inelastic deformation: total energy accounting including the thermal term; the "energy lost" language corrected to "energy transferred" | A full ledger problem with an energy-balance table |

**Must be derived, not stated:** $W_{\text{net}}=\Delta K$ (from $F=ma$); the spring potential's
$\tfrac12kx^2$; the closed-loop test for a conservative force; $F_x=-dU/dx$; the condition for
mechanical-energy conservation; the power-limited top speed; the stability criterion $U''(x)>0$.

**DIAGRAM briefs (D6.1–D6.14):** the $F$–$x$ curve with the work shown as area (and the sign regions
shaded); a closed-loop path in a conservative field vs one that fails the test; the spring's $U(x)$
parabola with three energy levels and the turning-point arrows; the $U(x)$ landscape with a stable well,
an unstable hill and the two turning points at a given $E$; the vertical circle's energy split at four
angles; the accelerating-wedge geometry with the block's displacement and the wedge's displacement
drawn; the constant-power climb (velocity–time and power–time); a car's power-limited top-speed force
balance; the chain-being-lifted variable-weight problem; the two-blocks-and-a-spring before/after
diagram; the gravitational escape energy curve $U=-GMm/r$ with the escape energy line; the
block-and-wedge with the normal force doing non-zero work; the energy ledger bar chart (initial,
final, dissipated); the $F$–$x$ curve of a real spring with the linear region marked.

**Mandatory archetypes:** block on an incline with friction (WET route); spring-launched block; loop-the-
loop with and without friction; pendulum with a nail (the string wraps — energy + circular dynamics);
energy with a variable force given graphically; the "does it make it over the hill?" problem; constant-
power vehicle; pump/elevator power; the two-mass system with a spring; the "find the speed at the
bottom" family; the chain over the edge; the block-wedge with the correct work audit; the
conservative-or-not test; the $U(x)$-graph reading.

**Olympiad block content:** the block-on-wedge problem solved by the energy method and the *false* result
that ignores the wedge's kinetic energy, with the "what does the missing energy do?" resolution; a
variable-mass energy audit (a chain unrolling from a table, a leaking sand cart) showing that
$\tfrac12mv^2$-type balances must include the kinetic energy of the leaving mass; energy in the centre-
of-mass frame and the general decomposition $K=\tfrac12Mv_{\text{cm}}^2+\tfrac12\mu v_{\text{rel}}^2$
(derived here, used in PART 7); the effective potential for a bead on a rotating hoop and for a particle
in a central field with angular momentum (the $L^2/2mr^2$ barrier — the "why orbits have a minimum
radius" insight, link PART 9); the "how much energy does it take to launch a satellite and to escape?"
two-part calculation with the ratio $\sqrt2$; restitution-free bouncing (a ball bouncing with a fixed
coefficient of restitution $e$: derive the total distance, the total time and the $e$-dependence);
energy of a rolling body derived by the no-slip constraint (preview of PART 8, one worked example); the
"Hagen–Poiseuille work budget" (the power to push fluid through a pipe, link PART 11); a
power-law force's energies and the corresponding "turning point" formula; the "who pays for the kinetic
energy of a flywheel?" energy-transfer problem.

**Traps to plant:** omitting the work done by the normal force when the surface accelerates; calling
friction a "non-conservative force" and therefore not accounting for it at all; using
$\tfrac12kx^2$ for a spring stretched past its elastic limit; mixing the two forms of gravitational
potential (near-surface vs $-GMm/r$); forgetting the spring's potential when a spring is in the system;
using power $=$ force $\times$ speed without checking the direction; assuming a rolling body's
$\tfrac12mv^2$ alone is its kinetic energy.

**Exit criteria:** WET is derived, not quoted, and applied to a system with the internal-work caveat
stated; $U(x)$ diagrams are a full section with stability; the energy/force decision rule is taught
explicitly; the Olympiad block includes the CM-frame decomposition and the effective-potential idea;
every numerical answer in the worked problems has a unit check.

---

---

### PART 7 · Centre of Mass, Momentum & Collisions

`centre-of-mass-momentum` · folder `centre-of-mass-momentum/` · source: Cengage *Mechanics II* **ch 1
Centre of Mass, Conservation of Linear Momentum and Collision** (contents p. 4: COM, motion of the COM,
impulse, collision classification, coefficient of restitution, oblique collisions, variable mass, rocket
propulsion) · needs PART 6 · JEE Advanced · NSEP · INPhO · IPhO.
*The one idea:* in an isolated system the centre of mass keeps moving in a straight line — every
collision is a discussion about the motion around it.

| # | Section | Teach this, in this order | Closes with |
|---:|---|---|---|
| 1 | Why the centre of mass | Two particles with equal pulls; the definition $\mathbf R=\frac{\sum m_i\mathbf r_i}{\sum m_i}$; the "where is the mass?" picture; the fact that it can lie outside the body | COM of a ring and of a crescent (concept check) |
| 2 | COM of real bodies | Rod, triangle (the $\tfrac13$ rule), semicircular ring and disc, hollow/solid hemisphere, cone, composite plates by the positive-mass/negative-mass trick; symmetry shortcuts | COM of a cut-out disc |
| 3 | Motion of the COM | Derive $M\mathbf a_{\text{cm}}=\mathbf F_{\text{ext}}$ from Newton's third law; internal forces cannot move the COM; the "explosion keeps the COM trajectory" theorem | Explosion problem with a mid-air break-up |
| 4 | Momentum | $\mathbf p=m\mathbf v$, impulse $\mathbf J=\int\mathbf F\,dt$ (area under the $F$–$t$ curve), the impulse–momentum theorem; the average force in a bounce | A bounce problem computing the mean force |
| 5 | Conservation of momentum | The real condition (net *external* impulse zero in the chosen direction); the component-wise rule; recoil, explosions, the gun-and-bullet; momentum bookkeeping tables | The bomb-splitting-into-three-pieces problem |
| 6 | Collisions I: classification | Elastic, inelastic, perfectly inelastic; the line of impact and the plane of contact; the coefficient of restitution $e=\frac{v_{\text{sep}}}{v_{\text{app}}}$ along the line of impact only | Identify the line of impact in four geometries |
| 7 | Collisions II: 1-D results | Derive the general $e$-dependent final velocities; the elastic case; equal masses exchange; heavy–light limits (each computed as a limit, not asserted); the energy-loss formula $\Delta K=\tfrac12\mu v_{\text{rel}}^2(1-e^2)$ with the reduced mass | Three-limit audit of the elastic formula |
| 8 | Collisions III: 2-D | Momentum conservation along and perpendicular to the line of impact; smooth balls (no tangential impulse → tangential velocity unchanged); the equal-mass elastic 90° result; ball-off-a-wall at an angle with $e$ | An oblique sphere collision, both components |
| 9 | The centre-of-mass frame | The transformation, the fact that total momentum vanishes there, the energy decomposition $K=\tfrac12Mv_{\text{cm}}^2+K_{\text{rel}}$; why elastic collisions are trivial in the CM frame; the "minimum energy to react" idea | Redo one collision entirely in the CM frame |
| 10 | Variable mass | Derive $m\dot v=F_{\text{ext}}+v_{\text{rel}}\dot m$ honestly (the momentum of the *system* including the ejecta); the rocket equation $\Delta v=v_e\ln\frac{m_0}{m_f}$; thrust; the falling-chain and sand-on-belt cases with their surprising factors | Rocket $\Delta v$ calculation and the chain-on-a-scale reading |
| 11 | Two-stage impulse problems | Ballistic pendulum (momentum then energy, and *why* in that order); bullet through a block; the jumping-on-a-moving-cart family; the "which conservation law when" decision table | Ballistic-pendulum full solution with the energy audit |
| 12 | Systems with internal motion | Man walking on a boat, a block on a movable wedge (COM stays put), a bomb on a cart, the recoil of a spring-loaded toy; the displacement-in-the-lab-frame calculation | Man-on-a-boat displacement from the COM's fixed position |
| 13 | Collisions with a third body | Collisions on a spring link, collisions with friction afterwards, the "block hits a spring-buffer" family; restitution with a wall moving at a speed | Block-into-block-into-spring chain problem |

**Must be derived, not stated:** $M\mathbf a_{\text{cm}}=\mathbf F_{\text{ext}}$; the COM of the standard
bodies; the impulse–momentum theorem; the general 1-D collision formula; the energy-loss formula with
reduced mass; the variable-mass equation and the rocket equation; the equal-mass 90° result in 2-D;
the CM-frame energy decomposition.

**DIAGRAM briefs (D7.1–D7.16):** COM of a rod/triangle/semicircle/cone on one plate; a composite body
with the subtraction trick marked; an explosion's COM parabola with the fragment paths drawn around it;
the $F$–$t$ impulse curve with the area shaded and the mean force marked; the collision classification
chart (three cases with the before/after velocity arrows); the oblique collision geometry with the line
of impact, the plane of contact and the resolved components; the $e$-dependence graph of the final
velocities for $m_1=m_2$; the energy-loss fraction vs $e$ curve; the lab frame vs CM frame side by side
for the same collision; the rocket's momentum ledger (before/after with the exhaust parcel drawn);
the falling chain on a scale with the force components separated; the ballistic pendulum's two stages;
a man walking on a boat with the COM's fixed vertical line; a block on a movable wedge with the two
displacements; the sand-on-belt momentum flux; a moving-wall bounce.

**Mandatory archetypes:** two-block perfectly inelastic collision; elastic collision with unequal masses
(compute both velocities and check the limits); the "find $e$ from the rebound height" experiment; the
2-D equal-mass elastic collision at 90°; oblique ball-off-floor; the recoiling gun; the exploding shell
into fragments; a bullet embedding in a hanging block; a ball hitting a moving wall; the sand-on-a-belt
force; the chain folding onto a table; the rocket's mass ratio; the man-on-a-boat displacement; the
wedge-block energy split; the two-block-with-a-spring compression maximum; a collision followed by a
rough section.

**Olympiad block content:** the falling-chain-on-a-scale result (three times the weight of the landed
part) with its energy-accounting resolution; the variable-mass equation applied to a chain that is
lifted off a pile (the "why the force is $mg$ plus a momentum-flux term" analysis) and the surprising
zero-work case; the sand-hopper/cart problem as a *system* problem, including the "what happens when the
hopper runs out of sand" limit; the general two-body scattering problem in the CM frame with the
angle–energy relation and the "maximum scattering angle when $m_1>m_2$" result (elastic billiard
physics); the relativistic momentum's conservation requirement and the reason $\mathbf p=\gamma m\mathbf
v$ is forced (a one-page preview that PART 28 completes); impulse-approximation problems (a collision so
fast that finite forces are negligible — the honest criterion $F_{\text{impulse}}\gg F_{\text{other}}T$);
successive collisions with a restitution coefficient (energy decay per bounce and the limiting
behaviour); the "bouncing ball on a moving platform" resonance-flavoured problem; centre-of-mass
problems with a variable mass distribution (a sliding chain over a peg — the classic
$\ddot x$ equation, solved without Lagrange by the "system = COM + relative" decomposition); two-stage
rocket staging and the optimal stage-mass ratio estimate; the momentum-flux force of a water jet on a
plate (link PART 11) and on a moving plate (the $v_{\text{rel}}^2$ factor).

**Traps to plant:** using energy conservation in an inelastic collision; applying the coefficient of
restitution across the whole velocity instead of along the line of impact; forgetting that the normal
force does no *impulsive* work but momentum still changes; treating the recoil speed of a gun as if the
bullet's momentum were the gun's; using $v_{\text{cm}}$ as the velocity of every part after a collision;
forgetting the ejecta's momentum in the variable-mass equation; mixing "system" and "particle" when
external forces act; assuming the COM stays fixed when an external force acts.

**Exit criteria:** the COM's motion theorem is derived from the third law; both frame pictures (lab and
CM) are used on the same problem; the collision results are derived and then limit-checked (heavy–light,
$e=1$, $e=0$); the variable-mass equation is derived honestly; the Olympiad block has ≥ 3 problems where
a naive momentum argument fails.

---

### PART 8 · Rotational Mechanics

`rotational-mechanics` · folder `rotational-mechanics/` · source: Cengage *Mechanics II* **ch 2 Rigid
Body Dynamics** (moment of inertia, axis theorems, radius of gyration, torque, couple, equilibrium,
rotational kinetic energy, angular momentum and impulse, conservation of angular momentum) · needs
PART 7 · JEE Advanced · NSEP · INPhO · IPhO (the biggest single chapter in the
mechanics block: plan 18,000–25,000 words).
*The one idea:* a rigid body is a mass distribution; rotation is the same $F=ma$ story with $I$,
$\tau$ and $L$ playing the roles of $m$, $F$ and $p$.

| # | Section | Teach this, in this order | Closes with |
|---:|---|---|---|
| 1 | Rigid-body kinematics | Angular position, velocity and acceleration as vectors; $\mathbf v=\boldsymbol\omega\times\mathbf r$; the velocity field of a spinning body; the instantaneous axis of rotation (and why the contact point of a rolling wheel is instantaneously at rest) | Velocity of two points of a spinning disc |
| 2 | Fixed-axis rotation | The analogy table with translation, and the honest warning that an analogy is not a proof; constant-$\alpha$ equations; $\omega$ vs $v$ graphs | A spinning-up flywheel problem |
| 3 | Moment of inertia I | Definition $I=\sum m_ir_i^2$ and the integral form; *why* the mass distribution matters (derive $I$ for two point masses and then a rod); the standard results derived one by one (rod about centre and end, ring, disc, solid and hollow sphere, cylinder, plate, cone); radius of gyration | Derive $I$ for a solid sphere in a worked example |
| 4 | Axis theorems | Parallel-axis theorem with proof; perpendicular-axis theorem with proof (planar bodies) and its failure in 3-D; the "about a diameter" family; the composite-body method with subtraction | $I$ of a disc about a rim tangent, two ways |
| 5 | Torque | $\boldsymbol\tau=\mathbf r\times\mathbf F$; the moment arm; torque about a point vs about an axis; the derivation that $\tau_{\text{net}}=I\alpha$ about a fixed axis (and the cancellation of internal torques) | A pulley-with-mass problem |
| 6 | Angular momentum | $\mathbf L=\mathbf r\times\mathbf p$ for a particle; $L=I\omega$ for a rigid body about a fixed axis; the general statement $\mathbf L_{\text{about a point}}=\mathbf L_{\text{spin}}+\mathbf r_{\text{cm}}\times M\mathbf v_{\text{cm}}$ (derived, and used later); the "$L$ about a moving point" subtlety | Angular momentum of a rolling body about the ground contact point |
| 7 | Conservation of angular momentum | The condition ($\tau_{\text{ext}}=0$ about the chosen point/axis); the turntable and the person-with-weights problem (including *where the energy comes from*); a bullet hitting a hinged rod; a disc dropped on a spinning disc (with the energy-loss explanation); the spinning skater; the man on a rotating platform walking inwards | Bullet-into-hinged-rod, full solution |
| 8 | Rolling without slipping | The no-slip constraint $v_{\text{cm}}=\omega R$, drawn as a velocity field; the kinetic energy $\tfrac12Mv^2+\tfrac12I\omega^2$ (and its split into $\tfrac12Mv^2(1+\frac{I}{MR^2})$); rolling on an incline: derive $a=\frac{g\sin\theta}{1+I/MR^2}$, the minimum $\mu$, and the rolling race with an $I$-ordering | The rolling race for five bodies, with the derived order |
| 9 | Rolling with a force at various heights | A disc pulled by a string wound at the top/centre/bottom: the friction direction changes — a full three-case analysis with the $\mu$ conditions | The three-case friction-direction table |
| 10 | Rolling with slipping | Two-phase motion: kinetic friction, the slip-decay, the moment rolling starts, the distance, and the energy audit; a ball thrown with backspin | The "when does it start rolling?" problem |
| 11 | Rotational collisions and impulses | Angular impulse $\int\tau\,dt=\Delta L$; a rod struck by a bullet (find the axis and the angular velocity); the centre of percussion (why a bat stings your hands); the falling-rod-onto-a-peg problem | Rod-into-peg angular impulse problem |
| 12 | Rigid-body equilibrium | Centre of gravity (and why it can be treated as the COM); toppling: the tipping condition, the ladder problem, the maximum overhang of stacked blocks ($\sum 1/2n$ — derived), the stability of a body on a step | Overhang derivation with the first four blocks drawn |
| 13 | Gyroscopic precession | $\Delta\mathbf L=\boldsymbol\tau\,dt$ as a vector statement; the precession rate $\Omega=\frac{\tau}{I\omega}$; the spinning-top/flywheel/bicycle-wheel demonstrations; the torque-free precession of the Earth; the "why a spinning top does not fall" explanation | Precession-rate calculation for a real flywheel |
| 14 | Synthesis: which equation when | The decision tree (pure rotation / pure translation / rolling / impulse / conservation of $L$) with four worked 90-second examples | Mixed problem set with the method named first |

**Must be derived, not stated:** every $I$ used (at least rod, ring, disc, sphere, cylinder); the
parallel- and perpendicular-axis theorems; $\tau=I\alpha$ about a fixed axis; the general angular-momentum
decomposition; $a=\frac{g\sin\theta}{1+I/MR^2}$ and the minimum-friction condition; the two-phase
slipping solution; $\Omega=\tau/L$ for precession; the maximum-overhang sum.

**DIAGRAM briefs (D8.1–D8.22):** the velocity field of a spinning disc (with the instantaneous axis
marked); the pure-rotation $v=r\omega$ profile; $I$ of six standard bodies on one plate; the parallel-axis
theorem's geometry; the perpendicular-axis theorem for a lamina; a composite body with the cut-out
(dashed) marked; torque about a point with the moment arm drawn; the internal-torque cancellation in a
rigid body (a pair of internal forces on two elements); the rolling wheel's velocity field with the
contact point at rest and the top point at $2v$; the rolling-incline force diagram with the friction
direction derived; the rolling race with five bodies at the same $t$; the three "pull the string"
cases with the friction direction marked; the slipping-to-rolling phase diagram ($v$ and
$\omega R$ vs $t$ converging); the ball-with-backspin velocity/angular-velocity graphs; a rod struck
off-centre with the angular impulse; the centre of percussion on a bat; the falling rod hitting a peg;
the ladder problem's force diagram with the incipient-tip normal force; the stacked-blocks overhang
construction; a gyroscope with $\mathbf L$, $\tau$ and the precession cone; the Earth's wobble; the
rolling-body energy split (translational vs rotational bars); the "which point do you compute $L$ about?"
diagram for a rolling wheel.

**Mandatory archetypes:** pulley with mass (two ways: torque and energy); $I$ of a composite body;
rolling down an incline (find $a$, $\mu_{\min}$, speed at the bottom three ways); the race ranking;
a disc/hoop with a hanging mass; a rod hinged at one end released from horizontal (find $\omega$ at the
bottom and the hinge force); a bullet hitting a hinged rod; a rotating disc with a dropped mass
(conservation of $L$, energy loss computed); the turntable-and-weights problem; the man-on-a-ladder;
toppling of a tilted block; a spool with a string (three cases); a rolling wheel on a moving plank;
a ball hitting a wall with a spin; the flywheel's stored energy; the bicycle-wheel gyroscope.

**Olympiad block content:** the general angular momentum of a rolling body about a point
($\mathbf L=I_{\text{cm}}\boldsymbol\omega+\mathbf r_{\text{cm}}\times M\mathbf v_{\text{cm}}$) and *why*
the "ground-frame $L=I_{\text{contact}}\omega$" shortcut works — with the proof; rolling with slipping
solved completely (the algebraic $v(t)$, $\omega(t)$, the transition time, the energy lost to friction,
and the verification that friction's work is exactly the lost energy); a cylinder rolling inside a
concave track (the SHM link to PART 10, with the correct $\frac{I}{MR^2}$ factor); the yo-yo (derive the
acceleration by torque-and-force and by energy, then the string's tension); a spool on a rough surface
pulled at an angle (find the condition for it to roll *towards* you — a famous counter-intuitive
problem); a coin/ring rolling on a table and turning (gyroscopic turning); a rod sliding down a
frictionless wall (the classic "when does it leave the wall?" problem — with the $L$ constant argument);
rolling friction's paradox (why a rolling body eventually stops if rolling friction is tiny but non-zero);
the "unrolling carpet" and "unwinding paper roll" variable-inertia problems; the top's steady precession
$\Omega$ with the torque's angle dependence, and the "sleeping top" condition; the physical pendulum as a
rigid body (hand-off to PART 10); the angular momentum of a system with an accelerating COM (the
moving-point subtlety, with the "which point is safe to use?" rule); the "how much energy does a
flywheel store per kilogram?" design estimate (with a real material's strength limit — link PART 12);
the moment-of-inertia tensor as a *concept* (why $\mathbf L\not\parallel\boldsymbol\omega$ for a
dumbbell, stated with the two-axis picture and no tensor algebra).

**Traps to plant:** using $I$ about the wrong axis; forgetting the parallel-axis theorem's
$Md^2$ term's distance definition; taking $\tau=I\alpha$ about a non-fixed, non-CM point; using
$L=I\omega$ blindly when the axis is not principal; applying energy conservation to a body that slips;
forgetting that static friction at the contact point of a rolling body does no work; saying the
friction acts "backwards" on a rolling object without deriving the sign; using $v=\omega R$ for a
slipping body; confusing the angular momentum about different points (the classic exam trap).

**Exit criteria:** every $I$ is derived; both axis theorems are proved; rotational kinematics precedes
rotational dynamics; rolling is split into "without slipping" and "with slipping"; conservation of $L$
has ≥ 5 worked applications including one energy-loss audit; gyroscopic precession is present with the
vector-triangle explanation; the overhang and sliding-rod problems appear in block 10.

---

### PART 9 · Gravitation & Orbital Motion

`gravitation` · folder `gravitation/` · source: Cengage *Mechanics II* **ch 5 Gravitation** · needs
PART 8 ·
JEE Advanced · NSEP · INPhO · IPhO.
*The one idea:* gravity is a central inverse-square field, and every orbit is energy and angular momentum
trading places.

| # | Section | Teach this, in this order | Closes with |
|---:|---|---|---|
| 1 | The law and its evidence | The inverse-square law, the gravitational constant (its smallness and what it implies), the Cavendish experiment's logic; why gravity is always attractive and always central | A "why does the Moon not fall?" concept check |
| 2 | Field and potential of simple sources | $\mathbf g$ and $V$ for a point mass; the equipotentials and field lines; $V=-\frac{GM}{r}$ with the reference at infinity; the shell theorem — prove it with the elementary cone/solid-angle argument (so this PART does not depend on PART 14) | The shell-theorem proof written out |
| 3 | Sphere, shell and cavity | Field and potential inside, outside and on the shell; the solid sphere's $\mathbf g\propto r$ inside; $V$ at the centre (the "three-halves" result); the spherical-cavity superposition trick | A cavity problem solved by superposition |
| 4 | $g$ and its variations | $g$ with altitude, depth, latitude and rotation (each derived); the "effective $g$" in a rotating frame; the reduction at the equator; the free-fall-vs-apparent-weight distinction | The $\Delta g$ table with numbers |
| 5 | Gravitational potential energy | $U=-GMm/r$ for the pair; the system's total energy; the "three-body" caution; the energy needed to assemble a sphere from shells (the self-energy — and its link to PART 15's charged sphere) | Self-energy of a uniform sphere |
| 6 | Kepler's laws | The three laws stated and *derived* (the second from angular momentum, the third from the circular orbit and then generalised to ellipses); areal velocity $=\frac{L}{2m}$; the extension to any central force (the $r^4$ test) | Derive $T^2\propto a^3$ from $F=ma$ |
| 7 | Circular orbits and energies | $v=\sqrt{GM/r}$; the total energy $E=-\frac{GMm}{2r}$ (derive and explain the factor $\tfrac12$); the vis-viva equation; the "the more energetic orbit is the slower one" paradox resolved | The orbiter energy ledger |
| 8 | Escape and capture | Escape speed derived from the energy condition; $v_e=\sqrt2v_{\text{orb}}$; the atmosphere's retention criterion (compare to the mean molecular speed); the launch-energy calculation | "Which gases can Earth hold?" table |
| 9 | Elliptical orbits | The ellipse's geometry ($a$, $b$, $e$, perigee, apogee); energy and angular momentum from the vis-viva at two points; the speed at any point; the flight-path angle; the "which orbit is more energetic" comparisons | Two-point vis-viva problem |
| 10 | Satellites in practice | Geostationary orbit (derived), polar and sun-synchronous orbits, the "why a geostationary satellite must be equatorial", weightlessness in orbit vs free fall, the ISS's period from its altitude | Compute the geostationary radius |
| 11 | Transfers and manoeuvres | Hohmann transfer (the two-impulse $\Delta v$ budget), plane changes, the "Oberth effect" qualitatively, docking and rendezvous phasing | A two-impulse transfer's $\Delta v$ |
| 12 | Systems of bodies | Binary stars about the COM (with the reduced-mass link to PART 7); the two-body correction to Kepler's third law; the mass of the Sun from Earth's orbit; gravity assist as an elastic bounce off a moving planet (with the velocity-triangle analysis) | Binary-star period problem |
| 13 | Gravity's reach | Tides (the difference of pull across the Earth, with the two-bulge explanation); the Roche limit's logic; the deep-tunnel oscillation and the free-fall collapse time as estimates | Tide-raising estimate and tunnel period |

**Must be derived, not stated:** the shell theorem; $\mathbf g$ and $V$ inside a solid sphere and a
cavity by superposition; the four $g$ variations; $U$ and $E$ of a circular orbit; the escape speed; the
second and third Kepler laws; the vis-viva equation; the two-body generalisation; the geostationary
radius; the deep-tunnel period.

**DIAGRAM briefs (D9.1–D9.16):** field lines and equipotentials of a point mass; the shell-theorem
cone construction; the "inside a uniform sphere" linear $\mathbf g$ profile and the $V(r)$ curve;
the cavity-by-superposition construction; the four $g$-variation curves on one plate; the "effective
gravity with rotation" vector diagram; a Kepler ellipse with the focus, the two radii and the equal-area
sectors; the vis-viva graph of $E$ vs $r$ for several $L$ (the effective-potential picture); the escape
energy diagram; the launch-from-a-tower energy ladder; the geostationary orbit drawn to scale; the
Hohmann transfer's two ellipses; the binary-star COM motion; the gravity-assist velocity triangle;
the tide-raising differential-pull diagram; the deep-tunnel problem with the enclosed mass marked.

**Mandatory archetypes:** find the speed/period at a given orbital radius; energy to move a satellite
from one orbit to another; escape-speed comparisons for two planets; the weight at the equator vs the
pole; a body dropped into a tunnel; the satellite's mass from its period; a planet's year from its
orbital radius; a projectile on a small asteroid (does it escape?); the cavity-in-a-sphere field;
potential at the centre of a shell-with-a-particle system; two-satellite rendezvous timing.

**Olympiad block content:** deriving the shell theorem with both methods (solid angle and Gauss's law for
gravity) and stating the "only $1/r^2$ gives a shell theorem" insight; the free-fall collapse time of a
uniform cloud, $t\sim\frac{1}{\sqrt{G\rho}}$, with the Kepler analogy and the real number for a
molecular cloud; tidal force derived by the difference of the inverse square and the Roche-limit
distance for a satellite of density $\rho$ orbiting a planet of density $\rho_p$; the Hohmann transfer's
$\Delta v$ with numbers for an Earth–Mars trip and the launch-window consequence; the "gravity assist"
as an elastic bounce off a moving planet — energy gained from the planet's orbital motion, with the
maximum-gain angle and a numeric example; the Oberth effect explained via the energy change as a function
of the burn altitude; the virial-like result $\langle U\rangle=-2\langle K\rangle$ for an inverse-square
orbit (derived by averaging the vis-viva) and its use in the "energy of a galaxy" estimate; the
"why does the ISS not fall?" question answered with the numbers; the geostationary transfer with the
required plane change; the Schwarzschild radius derived by dimensional analysis and by the escape-speed
argument (with the caveat that this is a Newtonian coincidence); the binary's observed radial-velocity
curve as a mass-measurement method (real exoplanet data style); the "how much energy would it take to
spread out the Earth?" estimate (comparison with its binding energy); the satellite-drag spiral-in
estimate (the $\Delta r$ per orbit from the work of drag).

**Traps to plant:** using $g=GM/R^2$ at a height without adjusting $R$; treating potential energy as
$mgh$ at orbital distances; forgetting the negative sign of the gravitational potential energy; using
$v=\sqrt{GM/r}$ with $r$ measured from the surface; assuming the geostationary orbit is over any city;
mixing up the two "escape" conditions (energy zero vs $v=\sqrt2v_{\text{orb}}$); applying Kepler's
second law with the wrong reference point; forgetting the planet's own radius when computing surface
gravity; saying "there is no gravity in orbit".

**Exit criteria:** the shell theorem is proved in-chapter (no dependence on PART 14); all four $g$
variations derived; the orbit-energy ledger gives $E=-\frac{GMm}{2r}$ with the reason for the
$\tfrac12$; Kepler's laws are derived rather than quoted; the Olympiad block contains ≥ 3 real-data
estimates (collapse time, Roche limit, gravity assist).

---

---

### PART 10 · Simple Harmonic Motion & Oscillations

`simple-harmonic-motion` · folder `simple-harmonic-motion/` · source: Cengage ***Waves and
Thermodynamics* ch 4 Linear and Angular Simple Harmonic Motion**, with the spring material of ch 7
(§7.3–7.7, springs and their combinations) pulled in — here is where the volume's SHM live · needs
PART 8 (and PART 6 for energy) · JEE Advanced · NSEP · INPhO · IPhO.
*The one idea:* if the restoring effect is proportional to the displacement, the motion is sinusoidal —
and almost everything linear oscillates.

| # | Section | Teach this, in this order | Closes with |
|---:|---|---|---|
| 1 | The defining test | Restoring force $\propto$ displacement (with the minus sign); the differential equation $\ddot x=-\omega^2x$; the general solution and the meaning of $A$, $\phi$; the distinction between SHM and "any oscillation" | Which of five motions is SHM? concept check |
| 2 | The kinematic triple | $x$, $v$, $a$ as functions of time and of position; $v=\omega\sqrt{A^2-x^2}$; the phase relations and the quarter-period offsets; $v_{\max}=\omega A$, $a_{\max}=\omega^2A$ | A "find the speed at $x=A/2$" drill |
| 3 | The circular-motion picture | SHM as the projection of uniform circular motion (the phasor); why this is more than an analogy (the same differential equation); the phase convention | Read a phasor diagram to get initial conditions |
| 4 | Energy in SHM | $K$, $U$, $E=\tfrac12kA^2$; the position dependence of the split; the time averages $\langle K\rangle=\langle U\rangle=\tfrac14kA^2$; the $K$–$U$ ellipse/rectangle picture | Energies at $x=A/\sqrt2$ |
| 5 | Springs | Horizontal and vertical spring-mass systems; the **equilibrium-shift theorem** (gravity moves the equilibrium but does not change $\omega$); springs in series and parallel (derive $k_{\text{eff}}$); cutting a spring; the two-block-spring and the block-between-two-springs | Vertical spring's period, proved gravity-independent |
| 6 | The simple pendulum | Derive the small-angle equation from the tangential force and from the torque; the $\sin\theta\approx\theta$ justification with the error percentage; the amplitude dependence's origin; the pendulum in a lift, a car, a freely falling frame, a liquid, and with a charge in an electric field (the "effective $g$" method) | Pendulum period in an accelerating car |
| 7 | The physical pendulum | $\tau=I\alpha$ derivation, $T=2\pi\sqrt{I/(mgd)}$, the equivalent simple pendulum length, the oscillating rod/disc/ring; the minimum-period problem and its $d$ optimisation | Minimum period of a rod pivoted at a distance $d$ |
| 8 | Other real oscillators | The torsion pendulum; the liquid in a U-tube; the floating cylinder (buoyancy as a spring); the ball in a bowl (with rolling, using the $I$ factor); the block on a frictionless track with two springs; the tube-through-the-Earth (link PART 9) | Floating-cylinder period derivation |
| 9 | The "show it is SHM" toolkit | Three methods, each demonstrated: (a) force/torque linearisation, (b) energy method with $k_{\text{eff}}=U''(x_0)$ and $m_{\text{eff}}$, (c) small-angle/small-displacement expansion; when each is fastest | Slope a three-method comparison table |
| 10 | Damped oscillations | The equation $m\ddot x+b\dot x+kx=0$; the three regimes (under/critical/over) with their solutions' shapes; the decay envelope $e^{-bt/2m}$; the logarithmic decrement; the "how many oscillations before it stops?" estimate | Damped pendulum's amplitude after $n$ cycles |
| 11 | Forced and resonant | The driven equation and the steady-state amplitude; the resonance curve; the *displacement* resonance at $\omega=\sqrt{\omega_0^2-2\beta^2}$ versus the *velocity* resonance at $\omega_0$ (the subtlety most books skip); the phase lag; realistic examples (bridge, building, tuning fork) | Resonance-curve sketch brief + read-off |
| 12 | Coupled oscillators and beats | Two masses and a spring: the symmetric and antisymmetric normal modes, then the general solution as a superposition (the beating energy exchange); the $N$-mass limit as a standing wave (the hand-off to the shipped string-waves note) | Two-mode coupled-pendulum solution |
| 13 | Non-idealities | Why real pendulums slow down (amplitude and damping); the anharmonic correction's size; the "small oscillation" validity statement per system | The $\theta_0^2/16$ correction computed |

**Must be derived, not stated:** the SHM solution and its initial-condition constants; $v=\omega\sqrt{A^2-x^2}$;
the energy expressions and their averages; the spring combinations; the pendulum equation from the
torque; $T=2\pi\sqrt{I/mgd}$ and the minimum-period condition; the effective-$g$ method for accelerations;
the damped regimes; the resonance condition; the two normal modes of a coupled pair.

**DIAGRAM briefs (D10.1–D10.18):** the SHM $x$, $v$, $a$ triple graph with the quarter-period offsets
marked; the reference circle with the phasor and the projection; the energy-split bar chart at five
positions; the $K(x)$ and $U(x)$ parabolas with the horizontal total-energy line; the spring–mass
horizontal vs vertical setup with the equilibrium shift marked; series and parallel spring combinations;
the pendulum's force diagram at angle $\theta$ with the tangential component; the pendulum in a lift/car
with the effective-$g$ vector; the physical pendulum with the pivot, the COM and $d$; a rod and a disc
about a pivot at distance $d$ with the $T(d)$ curve (minimum marked); the U-tube liquid column with the
restoring pressure difference; the floating cylinder with the displaced-volume geometry; a ball in a
bowl rolling (with the $I$ factor); the damped oscillation's envelope and the three regimes' curves; the
resonance amplitude vs $\omega$ for three damping values; the phase-lag curve; the coupled-oscillator's
two modes drawn side by side; the beat pattern of two nearly equal frequencies.

**Mandatory archetypes:** find $A$, $\omega$, $\phi$ from initial conditions; energy at a given position;
spring in series/parallel; a block on two springs; the vertical spring with a slowly lowered mass; the
pendulum in an accelerating frame; the pendulum with a charged bob near a charged plate (link PART 13);
the physical pendulum's period; the ring-on-a-nail problem; the floating-body period; the U-tube period;
the ball-in-a-bowl period (with and without rolling); the damped oscillation's amplitude after $t$; the
resonance read-off; a two-spring "effective $k$" chain; the coupled-pendulum beat period; the SHM
amplitude from a graph.

**Olympiad block content:** the general small-oscillation method stated properly (expand $U$ to second
order: $\omega^2=U''(x_0)/m_{\text{eff}}$), applied to four systems including one where the mass
redistributes (a rolling cylinder in a track, a partially-filled U-tube); the large-amplitude pendulum's
period $T\approx T_0(1+\theta_0^2/16)$ derived by expanding $\sin\theta$ (a two-term expansion, no
elliptic integrals) and compared with the exact numerical value at 30°, 60°, 90°; the damped,
driven oscillator's full solution with a "what happens at resonance" energy-balance derivation
(average power in = average dissipation) and the $Q=\omega_0/2\beta$ definition, then the "ring-down
time" measurement; the resonance peak's width and the trade-off in designing a suspension (a real
engineering estimate); parametric resonance (a child on a swing pumping: state the mechanism and
derive the growth condition qualitatively); the coupled-oscillator energy exchange time and the
"N coupled pendulums → wave" limit (link the shipped string-waves note); the two-degree-of-freedom
system with different masses solved by the "subtract and add the equations" trick (the standard
normal-mode algebra) and then by the eigenvalue-free shortcut; the anharmonic oscillator's
$U(x)=\tfrac12kx^2+\tfrac13bx^3$ correction's effect on the period (order of magnitude, via
$\Delta T/T\sim bA/k$); the torsion pendulum used to measure $G$ and the moment of inertia of an
irregular body (a laboratory reconstruction); the "how to measure $g$ with a pendulum to 4 significant
figures" experimental design (with the error analysis handed back to PART 1); oscillations in a
non-inertial frame (the effective-$g$ method at an angle, with the "why the equilibrium position
rotates" insight); the SHM of a spring with a mass that changes (a dripping-bag problem — the adiabatic
invariant's first appearance, with the amplitude scaling $A\propto m^{-1/4}$ stated).

**Traps to plant:** writing $T=2\pi\sqrt{m/k}$ with the wrong $k$ after adding springs in series
(inverse sum); assuming $\omega$ changes when the orientation changes (the equilibrium-shift trap);
using $A$ as the total travel (it is half); taking the average energy as $\tfrac12kA^2$ (it is the
total, and the average of each part is half); using the undamped amplitude in a damped problem;
confusing the driving frequency with the natural frequency; forgetting the $I$ factor for a rolling
oscillator; treating the physical pendulum's $d$ as the length of the rod rather than the pivot-to-COM
distance; applying small-angle results to $90^\circ$ amplitudes without saying so.

**Exit criteria:** the three "show it is SHM" methods are taught with named examples; the
equilibrium-shift theorem is derived; the resonance subtlety (displacement vs velocity peak) is
explained; damped and driven appear with their energy interpretation; the Olympiad block includes
large-amplitude correction, $Q$-factor and the general linearisation method.

---

### PART 11 · Fluid Mechanics & Surface Tension

`fluid-mechanics` · folder `fluid-mechanics/` · source: Cengage *Mechanics II* **ch 3 Fluid Mechanics**
with surface tension from **ch 4 Properties of Solids and Fluids** · needs PART 5 (and PART 6 for energy
methods) · JEE Advanced · NSEP · INPhO · IPhO.
*The one idea:* fluids carry pressure; pressure differences are forces; viscosity and surface tension
matter only when the length scale is small.

| # | Section | Teach this, in this order | Closes with |
|---:|---|---|---|
| 1 | Pressure in a fluid at rest | Why pressure is a scalar; the isotropic-pressure proof by a small wedge; the hydrostatic equation $\frac{dp}{dy}=-\rho g$ derived; $p=p_0+\rho gh$ and the "shape does not matter" paradox | Pressure at the bottom of three differently-shaped vessels |
| 2 | Measuring pressure | Manometer, barometer, gauge vs absolute pressure, the "how high can a water barometer be?" estimate, blood pressure units | A manometer problem with two liquids |
| 3 | Pascal and hydraulic machines | Pascal's law and its derivation from incompressibility; the hydraulic lift's force-distance trade (and the energy audit); the hydrostatic paradox explained | Hydraulic jack problem with an energy check |
| 4 | Buoyancy | Archimedes derived twice (by the pressure-difference argument and by the "displaced fluid" argument); floating bodies' fraction submerged; apparent weight; the "ice melting in water" family (with the correct answer for each case: fresh water, salt water, with a stone) | Fraction-submerged problem with three fluids |
| 5 | Stability of floating bodies | The centre of buoyancy, the metacentre and the metacentric height $BM=I/V$; why a wide barge is stable; the "why a submerged body is unstable above neutral" argument | Metacentric-height comparison for two hull shapes |
| 6 | Buoyancy in non-inertial frames | Apparent $g$ in a lift; the balloon in an accelerating car (the counter-intuitive direction — derived); a balloon in a rotating fluid; the "why the helium balloon leans forward" insight | Balloon-in-a-braking-car problem |
| 7 | Fluid flow and continuity | The Lagrangian vs Eulerian descriptions; steady flow, streamlines, streaklines; derive the equation of continuity from mass conservation; variable-area ducts; the "flow rate is constant but the speed is not" concept | Continuity with a branching pipe |
| 8 | Bernoulli's equation | Derive from the work–energy theorem on a streamtube; state the four conditions (steady, incompressible, non-viscous, along a streamline) as a 4-point validity box; pressure–speed trade explained physically | A pitot-tube problem with the relevance of each assumption |
| 9 | Bernoulli's applications | Torricelli's efflux (with the derivation and the range result), Venturi meter, pitot tube, the siphon (and its maximum height limit), the atomiser/spray, the "two holes give equal ranges" result | Venturi flow-rate calculation |
| 10 | Bernoulli's limits | Why the naive airfoil explanation is wrong (a `> [!tip] Insight` callout), the curved-flow pressure gradient ($\frac{\partial p}{\partial r}=\frac{\rho v^2}{r}$) derived, the rotating fluid's paraboloid surface (derived from the equipotential argument) | Paraboloid surface shape with the derivation |
| 11 | Momentum-flux forces | The force of a jet on a plate (normal and inclined, moving plate); the rocket/thrust momentum argument (link PART 7); the pipe bend's reaction force; the "water hammer" estimate | Jet-on-a-moving-vane force |
| 12 | Viscosity | Newton's law of viscosity; the velocity gradient's meaning; dimensional analysis of $\eta$; laminar flow between plates; temperature dependence qualitatively | The viscous force on a sliding plate |
| 13 | Poiseuille and Stokes | Derive Poiseuille's law by the force balance on a cylindrical shell (teach the *technique*); the $r^4$ consequence and the "why narrow pipes dominate" scaling; Stokes' law (statement + why it is $\propto\eta rv$ by dimensional analysis); terminal velocity derived and used to measure $\eta$ | Terminal velocity of a falling sphere with numbers |
| 14 | Reynolds and real flows | Reynolds number as the ratio of inertial to viscous effects; the laminar–turbulent transition; the drag crisis mentioned; turbulence's scaling; why the flow rate in a pipe is limited | Estimate the Reynolds number of a swimmer and of a capillary |
| 15 | Surface tension I | Molecular origin; the two equivalent definitions (force per length, surface energy per area) with the equivalence proof; surface energy of a film; the "why a liquid minimizes area" argument | Energy to blow a soap bubble |
| 16 | Surface tension II | Excess pressure in a drop and in a soap bubble (derive both, noting the two surfaces); the general Young–Laplace result stated; the merging of bubbles; the "smaller bubble is at a higher pressure" consequence | Two-bubble valve problem |
| 17 | Surface tension III | Contact angle, capillary rise (derive by force balance *and* by energy), Jurin's law, the too-short-tube problem, the floating needle and the water-strider, the force between two plates with a droplet | Capillary rise in a tube of insufficient length |

**Must be derived, not stated:** the hydrostatic equation; Archimedes' principle both ways; continuity;
Bernoulli from the work–energy theorem; Torricelli; the curved-flow pressure-gradient equation and the
paraboloid surface; Poiseuille's law; Stokes' terminal velocity; the two definitions of surface tension's
equivalence; the excess-pressure results; capillary rise (both derivations).

**DIAGRAM briefs (D11.1–D11.20):** the pressure-vs-depth graph for a fluid with two layers; the
wedge/isotropy pressure proof; the hydrostatic-paradox vessels; the hydraulic press with the
piston-displacement trade; the floating-body force diagram with the displaced volume shaded; the
metacentre construction with the righting moment; the helium balloon in an accelerating car with the
pressure-gradient arrows; streamlines in a duct of varying area; the streamtube used for the Bernoulli
derivation (before/after states marked); the Venturi meter with the manometer; the pitot tube's two
openings; the siphon with the pressure at the highest point; the draining tank (with the variable
height); the rotating-fluid paraboloid with the free-surface equation; a jet striking a plate (flat,
inclined and moving cases); the Poiseuille flow's parabolic velocity profile with the shell element
marked; the terminal-velocity force diagram for a sphere; the Reynolds-number regimes for a sphere
(drag-coefficient curve); the soap-bubble cross-section with the two surfaces and the pressure arrows;
the capillary rise with the contact angle and the force balance; a floating needle's depressed surface.

**Mandatory archetypes:** pressure at a depth in a two-fluid system; the manometer's height difference;
the hydraulic lift's force and stroke; floating fraction in three fluids; the iceberg's submerged
fraction; a body held at the bottom (the "no water underneath" case); apparent weight in a fluid;
the ice-melting question's four variants; continuity in a tapering pipe; Torricelli's range; the
Venturi flow rate; the pitot tube's airspeed; the siphon's height limit; a jet on a plate; the
terminal velocity of a raindrop/sphere; the capillary rise in a glass tube; the bubble's excess
pressure; the drop's splitting (why a bigger drop has less pressure).

**Olympiad block content:** the draining-tank time derived by integrating Torricelli
($T=\frac{A}{a}\sqrt{\frac{2H}{g}}$ with the constant-area case and the "why the last bit takes
forever" limit); the viscous (Hagen–Poiseuille) drainage regime and the exponential decay of the height
with the crossover to the inertial regime (the two-timescale analysis); the rotating-fluid paraboloid
derived three ways (equipotential, force balance, Bernoulli) with the "why the free surface is an
equipotential" insight; the terminal velocity in two drag regimes (Stokes vs quadratic) with the
crossover radius for a raindrop, and the *practical* consequence that raindrops are much slower than the
vacuum estimate; the Young–Laplace equation's general form $\Delta p=\gamma(\frac1{r_1}+\frac1{r_2})$
derived by the energy method, and its use for the "soap film between two rings" surface; a liquid column
held by surface tension (Jurin's law with a finite tube and the "drop hanging from a tap" problem,
including the drop-weight method for measuring $\gamma$); the "how much does a water strider weigh?"
estimate and the "why large animals cannot walk on water" scaling argument; Bernoulli in a rotating
frame (the "where does the energy come from?" audit for a fluid rising in a spinning tube); the
Feynman sprinkler ("which way does the water go?") as a physics-argument exercise, not a formula hunt;
the rocket-in-a-fluid retarding-force estimate (drag's $\rho v^2 A$ form and the "why a whale is shaped
like that" insight); the stability of a submerged vs floating cylinder with the metacentric height
computed for a real hull; the "how high can a tree suck water?" limit (the capillary and pressure
bounds, with the real number ~100 m and the transpiration-pull explanation); the viscosity measurement
of glycerine by the Stokes method, with the wall-correction caveat stated; the shallow-water wave speed
$v=\sqrt{gh}$ derived from the continuity + Bernoulli pair (the bridge to the shipped sound-waves note).

**Traps to plant:** assuming the pressure depends on the container's shape or on the volume of water;
using absolute pressure where gauge pressure is meant; forgetting the displaced-fluid *volume* equals the
submerged volume (not the body's total volume); ignoring the extra surface in a soap bubble (a factor of
2); using Bernoulli across a viscous, unsteady or turbulent region; using Torricelli with a small but not
negligible tank area; assuming a siphon works up to any height; forgetting that the buoyant force acts at
the centre of buoyancy, not the centre of mass; ignoring the air's buoyancy when weighed in air (fine
for JEE, fatal for precise work — say so).

**Exit criteria:** hydrostatics is derived from the pressure-gradient equation; buoyancy is derived twice;
Bernoulli has an explicit four-condition validity box and a "where it fails" section; the momentum-flux
section connects to PART 7; viscosity includes the Poiseuille derivation *technique*; surface tension
covers the two definitions and all three standard results; the Olympiad block contains the drainage
integration, the paraboloid's three derivations and the shallow-water wave speed.

---

### PART 12 · Elasticity & Properties of Matter

`elasticity` · folder `elasticity/` · source: Cengage *Mechanics II* **ch 4 Properties of Solids and
Fluids** (elasticity and moduli; the fluid half is PART 11's) · needs PART 5 ·
JEE Advanced · NSEP · INPhO · IPhO.
*The one idea:* elasticity is the macroscopic face of the interatomic spring: moduli are material
properties, stiffness is geometry.

| # | Section | Teach this, in this order | Closes with |
|---:|---|---|---|
| 1 | Stress and strain | Normal vs shear stress; tensile, compressive, volumetric and shear strain; the dimensionless strain; the "why engineers use stress, not force" argument | A strain-definition drill |
| 2 | Hooke's law and the three moduli | $Y$, $B$, $G$ defined by their experiments; the stress–strain curve with all its landmarks (proportional limit, elastic limit, yield, ultimate, fracture); ductile vs brittle; what "modulus is a material property" means and what it does not | Read a stress–strain curve and rank materials |
| 3 | Poisson's ratio and the interrelations | $\sigma$, why it is positive for most materials, the bounds $-1<\sigma<0.5$ with the physical reason; derive $Y=2G(1+\sigma)$ and $Y=3B(1-2\sigma)$; the "rubber's $\sigma\approx0.5$ means it is nearly incompressible" insight | The interrelation problems |
| 4 | Extension problems I | A wire under a load (with the force–extension linearity); the spring-constant interpretation $k=YA/L$; the springs-in-series/parallel link to PART 10; a wire of varying cross-section; the composite-rod problem (equal force vs equal extension branches) | Composite rod's extension with the stress distribution |
| 5 | Extension problems II | A wire under its own weight: derive the elongation $\frac{\rho gL^2}{2Y}$ by integrating over the element; the "why half the weight" explanation; a hanging cone/rod with a varying area | Wire-under-own-weight numeric problem |
| 6 | Thermal stress | The two-constraint method (expand freely, then compress back); the rod between two rigid walls; the rail-track and bridge-expansion problems; the "how much does a steel rail expand in a year of temperature cycles?" estimate; the bolt-and-nut tightening problem | A rail problem with and without expansion gaps |
| 7 | Bulk modulus and compressibility | $B$ for gases vs liquids vs solids (why gases are excluded from "elasticity" tables); the compressibility of water and the "why depth does not compress water much" estimate; the pressure–density correction; the sound-speed link $v=\sqrt{B/\rho}$ (hand-off to the shipped sound-waves note) | The density change at the ocean floor |
| 8 | Shear and torsion | $G$'s definition and measurement; the twist in a rod (state $\theta=\frac{TL}{GJ}$ with $J$ explained) and the torsion-pendulum's return (link PART 10); why a hollow shaft is more efficient per kilogram (compare $J/A$); a rivet's shear | Hollow-vs-solid shaft comparison with numbers |
| 9 | Elastic potential energy | $U=\tfrac12\times\text{stress}\times\text{strain}\times\text{volume}$ for each mode; the energy density; a suddenly applied load's double stress; a weight falling on a wire (energy method vs force method, and the "why the answer is not simply $mgh=FL/2$" trap); elastic hysteresis and damping | Falling-weight problem with the stress-factor discussion |
| 10 | Bending and beams | The neutral-axis argument; strain $\propto$ distance from the neutral axis; bending moment $\propto$ curvature $EI$; cantilever deflection $\delta=\frac{FL^3}{3EI}$ (statement + the qualitative derivation via the curvature equation); why an I-beam; a beam on two supports with a central load | Cantilever deflection with the I-beam comparison |
| 11 | Beyond the linear law | Elastic limit breakdown: plasticity, creep, fatigue; why a paperclip hardens after bending; the atomic picture of the modulus (the interatomic potential's curvature — with the "why $Y$ depends on the bond, not the sample" derivation); the "why steel is stiffer than rubber by 10⁵" explanation | The interatomic-potential curvature derivation |
| 12 | Choosing materials | Strength vs stiffness vs toughness vs density; the "specific modulus" $\frac{Y}{\rho}$ and the "specific strength"; the failure modes (buckling, yielding, fracture); one design problem (a light stiff bicycle frame or a crane cable) | A material-selection table for two applications |

**Must be derived, not stated:** the elongation $L\Delta L$ relations; $k=YA/L$; the wire-under-its-own-
weight integral; the thermal-stress method; the interrelations between $Y$, $B$, $G$, $\sigma$; the
elastic energy density; the suddenly-applied-load factor; the falling-weight maximum stress; the
cantilever's curvature relation; the atomic-spring derivation of $Y$.

**DIAGRAM briefs (D12.1–D12.14):** the stress–strain curve with all six landmarks labelled and a
brittle material's curve beside it; the three modulus geometries (a wire pulled, a volume compressed, a
block sheared); a wire's cross-section with the lateral contraction (Poisson) drawn; a composite rod in
series and in parallel with the stress/extension conditions; the wire-under-own-weight element diagram;
the thermal-stress setup with the "free expansion vs forced length" comparison; the ocean-depth density
curves; a twisted rod with the shear strain and the angle of twist; the hollow-vs-solid shaft's $J$ and
area; a falling weight onto a wire with the $F$–$x$ graph (linear spring plus the weight's line) and the
maximum-extension intersection; the neutral-axis bending diagram with the fibre strains drawn; a
cantilever with the deflection curve and the load; the interatomic potential well with the linear region
and the asymmetry that causes thermal expansion (link the shipped `heat/` note); a material-property
comparison chart (Ashby-style, strength vs density).

**Mandatory archetypes:** find the extension of a wire under a load (with units); the maximum load
before breaking; the elongation under own weight; a wire with a mid-point load (a two-wire hanger — the
classic "why the tension acts like $\frac{mg}{2\sin\theta}$" problem); thermal stress in a clamped bar;
the composite rod's extension; the bulk modulus from a pressure change; the shear modulus from a
rivet; the energy stored in a stretched wire; a weight dropped on a wire (maximum stress); the torsion
pendulum's period; finding $Y$ from the stress–strain graph; the cantilever's deflection comparison.

**Olympiad block content:** the microscopic derivation of $Y$ (an interatomic potential $U(r)$, the
equilibrium separation, $Y\propto U''(r_0)/r_0$, with the estimate for a typical solid using
$U''\sim D/r_0^2$ and $D$ from an eV-scale bond energy — the "why Young's modulus is around
$10^{11}$ Pa" derivation, a stunning order-of-magnitude result); thermal expansion as the *asymmetry* of
the potential well (derive the scaling $\alpha\propto \frac{k_BU'''(r_0)}{a\,U''(r_0)^2}$ qualitatively and compute the
sign/magnitude); the falling-weight problem with the rod's own mass included (an integral equation);
the constant-stress rod's exponential area profile $A(x)=A_0e^{x/\lambda}$ derived from the "every
cross-section carries the same stress" condition (a beautiful olympiad result with the
"biological limit" insight); the cantilever's deflection derived from the curvature equation
$\frac{d^2y}{dx^2}=\frac{M(x)}{EI}$ (a full integration — the exam-level version of a university
derivation); the buckling load's dimensional derivation $P\propto\frac{YI}{L^2}$ and the Euler result
$P=\pi^2YI/L^2$ (stated, then applied to a real column comparison); the I-beam's efficiency derived by
$I$ per unit area; a stretched wire's *nonlinear* correction (why Hooke's law fails first at large
strain, with the $x^3$ term); the "how much can a spider's silk lift?" estimate; the pressure vessel's
hoop stress derived by a free-body cut ($\sigma=\frac{pr}{t}$) and the "why a thin-walled tube fails
lengthwise first" insight; the speed of sound in a solid rod from $Y$ and $\rho$ compared with the
measured value; the earthquake wave speeds (P and S) as a two-modulus application with real numbers.

**Traps to plant:** confusing stress with force; using the cross-sectional area in the wrong place;
forgetting that the extension under self-weight uses $\frac12$ of the weight *at each cross-section* —
and integrating rather than averaging wrongly; the thermal-stress sign convention; using $\Delta L = L
\alpha \Delta T$ with $\Delta T$ in the wrong sign; treating Poisson's ratio as a correction to the
length; forgetting the factor 2 in a suddenly applied load; using the linear spring formula for the
falling weight with the maximum force rather than the maximum extension; assuming the beam's neutral
axis is at the geometric centre for a composite section.

**Exit criteria:** all three moduli have experiments and units; the stress–strain curve is read as a
source of design information; the elongation family (load, self-weight, composite, thermal) is complete;
the energy method and the force method both solve the falling-weight problem; bending has the
neutral-axis argument and one integrated deflection; the atomic-spring derivation of $Y$ is in block 10.

---

---

## Block B · Electricity & Magnetism

> The shipped notes `capacitors/` and `current-electricity/` own capacitance and circuits. This block
> supplies what comes *before* them (charge, field, flux, potential — Cengage *Electrostatics and Current
> Electricity* chs 1–3, which **are** in the repo as a PDF) and the whole magnetism → EMI → AC chain that
> comes after. **That chain has no PDF in this repository** (a standalone magnetism/EMI volume was never
> supplied), so PARTS 16–22 build their coverage maps from the standard JEE Advanced headings listed in
> their sections, plus the shipped `current-electricity/` and `electromagnetic-waves/` notes. If you find
> the volume somewhere in the tree, say so in the PR and cite it. Do not duplicate a shipped result: cite it as
> `> [!quote] Hand-off` — capacitance is the shipped `capacitors/` note's property; here we only meet the
> field that makes it.`

### PART 13 · Charge, Coulomb's Law & Electric Field

`electric-field` · folder `electric-field/` · source: Cengage ***Electrostatics and Current
Electricity* ch 1 Coulomb's Laws and Electric Field** · needs PART 2 (vectors) · JEE Advanced · NSEP · INPhO · IPhO.
*The one idea:* the electric field is the bookkeeping device for forces at a distance, and superposition
makes every distribution a sum of point charges.

| # | Section | Teach this, in this order | Closes with |
|---:|---|---|---|
| 1 | Charge | The two kinds, quantisation, conservation, the electron's charge and the "why we never see a fractional charge" statement; conductors vs insulators; charging by friction, contact and induction (with the electron-transfer bookkeeping); the electroscope | Charge-transfer bookkeeping problem |
| 2 | Coulomb's law | The force law, its vector form (and the correct way to write the direction: $\mathbf F_{12}=\frac{kq_1q_2}{r^2}\hat r_{12}$), superposition, action–reaction consistency; the torsion-balance logic and the modern bound on the exponent | Three-charge force problem |
| 3 | The electric field | $\mathbf E=\mathbf F/q_0$ and why the test charge must be small; the field of a point charge; field lines and their five rules; what field lines cannot tell you (magnitude from density is qualitative only) | Field-line reading drill |
| 4 | Element-and-symmetry method | The named method: choose the element, write $dq$, write $d\mathbf E$, kill components by symmetry, integrate; demonstrated on a charged ring's axis — the template for the whole chapter | Ring's axial field derived |
| 5 | Line, disc and sheet | Charged rod (finite by angle parametrisation; infinite as a limit); the ring's axial maximum at $x=R/\sqrt2$; a disc's axial field via rings; the infinite sheet's $E=\sigma/2\varepsilon_0$ (derived by integration so that PART 14 can be a *short cut*, not the only route) | Disc and sheet fields, with the limits |
| 6 | Arc, ring and sphere by integration | The semicircular arc's field at the centre; the "field at the centre of a charged circular arc" family; a spherical shell by integration (to be re-derived by Gauss in PART 14 — state the duplication honestly and use it as the Gauss motivation) | Arc and ring field problems |
| 7 | Conductors in the field picture | Why $\mathbf E=0$ inside (the "if it were not, charges would move" argument); the field perpendicular to the surface; the charge on the surface; the surface field $\sigma/\varepsilon_0$ and the factor-of-2 resolution (local patch vs total field — a `> [!danger] Trap` callout) | The "which is the field just outside?" problem |
| 8 | The dipole | Definition $\mathbf p=q\mathbf d$; the axial and equatorial fields at $r\gg d$ (derived); the dipole's field lines and internal field direction; the two-charge approximation's error | Axial/equatorial comparison |
| 9 | Dipole in a field | Torque $\boldsymbol\tau=\mathbf p\times\mathbf E$; the potential energy $U=-\mathbf p\cdot\mathbf E$ (derived, with the "why $\cos\theta$" reasoning and the zero at $90^\circ$ convention); the non-uniform-field net force; the "why a charged comb attracts paper" explanation | Dipole-in-a-gradient problem |
| 10 | Equilibrium of charges | Two-charge, three-charge (collinear and triangle) equilibrium; the sign/position counting rules; the stability question and Earnshaw's theorem's statement; the "charge at the centre of a square" problem | Three-charge equilibrium solved |
| 11 | Charge distributions | Linear/surface/volume density; the general $\mathbf E$ of a continuous distribution as an integral; the "which distribution do I approximate with?" decision table | Density-to-charge conversion drill |
| 12 | Motion of charges in fields | Charged particle in a uniform field = projectile motion with $a=qE/m$ (link PART 4); the charged pendulum; a ball bouncing between plates; the electron's deflection through a set of plates; the Millikan-style balance of gravity, buoyancy (link PART 11) and drag | The electron-deflection calculation |

**Must be derived, not stated:** Coulomb's vector form; the ring, rod, disc, arc and sheet fields; the
maximum of the ring's axial field; the dipole fields; the torque and the potential energy of a dipole;
the surface-field result with its factor-of-2 subtlety; the equilibrium position of a third charge.

**DIAGRAM briefs (D13.1–D13.16):** the three charging methods with the electron transfer drawn;
Coulomb's law on a pair with the unit vector labelled; the torsion balance; the field lines of a point
charge, a dipole and two like charges side by side; the field-line rules chart (five panels); the ring
element method with $dq$, $d\mathbf E$ and the symmetry cancellation; the axial field plot of a ring with
the maximum at $x=R/\sqrt2$; the rod field with the two angles $\alpha,\beta$; the disc-by-rings
construction; the infinite sheet's field lines with the pillbox preview; the arc's field at the centre
with the cancellation pattern; the conductor's surface field with the "local patch" and the total field
drawn separately; the dipole in a uniform field with the torque and the two stable/unstable orientations;
the dipole-in-a-gradient attraction; the three-charge equilibrium geometry; the charged pendulum.

**Mandatory archetypes:** the resultant force on one charge of a triangle/square; the field at a
distance on the axis of a ring/disc/rod; the field at the centre of a ring/arc; the field just outside a
charged conductor; the dipole's field and torque; the work to rotate a dipole; the equilibrium position
of a third charge; the maximum-field position problems; a charged ball hanging on a string; the electron
in a uniform field; the field due to two parallel sheets with opposite densities; a charged ring with a
charge at its centre (force and stability).

**Olympiad block content:** the off-axis stability of a charge at the centre of a charged ring (stable
along the axis, unstable perpendicular — derived with the potential's second derivatives, and reconciled
with Earnshaw's theorem); Earnshaw's theorem proved by the potential's Laplacian (the "no stable
equilibrium in a static field" result, with the honest caveat about alternating fields and magnets);
the field of a uniformly charged disc's edge and the near-surface divergence (stated as a caveat about
idealised models); the field inside a uniformly charged sphere (state and use; Gauss derives it cleanly
in PART 14); the cube's field at its centre and the "eight cubes" superposition trick; determining the
exponent of Coulomb's law experimentally (what a $1/r^{2+\epsilon}$ would do to a cavity experiment);
the self-force and the "why a charged shell does not push itself" argument; the millimetre-scale
electrostatic precipitator/inkjet design estimate; the "how much charge does it take to lift a
paper scrap?" estimate with the field-gradient force (a beautiful Fermi problem); the charge
distribution on a conducting shell with a point charge inside (the induced-charge picture, which the
shipped capacitors note will use); the "field of a rotating charged ring = magnetic moment" preview
(link PART 16); the interatomic field in a solid ($\sim10^{11}$ V/m) estimate from the ionisation
energy and the spacing — the "why lightning is only a small fraction of the internal field" insight.

**Traps to plant:** using $F=kq_1q_2/r^2$ with $r$ as a distance between charges but writing the
direction by hand for a repulsive pair and forgetting to reverse it for attraction; treating field lines
as trajectories; assuming the field is zero where the potential is zero (defer explicitly to PART 15);
confusing the field due to a patch with the total field near a conductor; using $\sigma/\varepsilon_0$
for a non-conducting sheet (the factor 2); adding field magnitudes when the vectors are not parallel;
forgetting that the test charge must be small; taking the dipole formulas outside their $r\gg d$ range.

**Exit criteria:** the element-and-symmetry method is named and reused ≥ 5 times; the sheet's
$\sigma/2\varepsilon_0$ is derived (so PART 14's Gauss result is a shortcut, not a new fact); the
factor-of-2 conductor trap is in the text at the point of the derivation; the dipole family (field,
torque, energy, gradient force) is complete; the Olympiad block contains Earnshaw's theorem and the
off-axis instability.

---

### PART 14 · Electric Flux & Gauss's Law

`gauss-law` · folder `gauss-law/` · source: Cengage ***Electrostatics and Current Electricity* ch 2
Electric Flux and Gauss's Law** · needs PART 13 · JEE Advanced · NSEP · INPhO · IPhO.
*The one idea:* flux counts field lines through a surface, and symmetry turns that count into the fastest
way to find a field.

| # | Section | Teach this, in this order | Closes with |
|---:|---|---|---|
| 1 | Flux | Field × projected area; $\Phi=\mathbf E\cdot\mathbf A$; the closed-surface sign convention (outward normal) and the "nothing actually flows" honesty box; flux of a uniform field through a tilted plane and through a hemisphere | Flux through a tilted disc and a hemisphere |
| 2 | Why the flux rule is what it is | The solid-angle proof for a point charge: (a) a closed surface not enclosing the charge has zero net flux; (b) an enclosing surface has flux $q/\varepsilon_0$ (the cone argument) — this proof *is* the law's justification | The two-case solid-angle argument written out |
| 3 | Gauss's law | The statement, its equivalence to Coulomb + superposition, and the distinction from a "new physics law"; the differential form preview $\nabla\cdot\mathbf E=\rho/\varepsilon_0$ | A concept check: what does Gauss's law forbid? |
| 4 | The Gaussian-surface protocol | The four-step method (identify the symmetry → choose the surface → argue $\mathbf E$ is normal and constant → solve); the honest statement that Gauss is always *true* but often *useless*; the "if you cannot state the symmetry, do the integral" rule | Choose the surface for four situations |
| 5 | Spherical symmetry | Point charge; thin shell (inside/outside); solid sphere with uniform density; a sphere with $\rho\propto1/r^2$ (the "does a hydrogen-like density change the outside field?" question); the potential's continuity check deferred to PART 15 | $E(r)$ for a solid sphere, both regions |
| 6 | Line and cylinder | Infinite line $\frac{\lambda}{2\pi\varepsilon_0 r}$; the thick wire; concentric cylinders; the "field inside a hollow charged cylinder" result; coaxial surfaces (the link to the shipped capacitors note's coaxial capacitor) | Coaxial field problem |
| 7 | Plane and slab | Infinite sheet $\frac{\sigma}{2\varepsilon_0}$; two sheets and the capacitor's interior field; a thick slab's interior field (derive the linear profile); the "field of a conductor's surface" reconciliation | Slab profile with a graph |
| 8 | Conductors and cavities | The "no field in a cavity without enclosed charge" result; the Faraday cage; a charge inside a cavity with the induced-charge bookkeeping; the shielded-cavity inversion; lightning rods and the sharp-edge field enhancement (with the "why $\sigma\propto1/r$ on two connected spheres" derivation) | Cavity-with-a-charge problem |
| 9 | Flux without the field | The cube-with-a-charge-at-a-corner/edge/centre family; the octant and half-space results; flux through a disc computed by the solid-angle trick; a charge outside a closed surface; the "which fraction of the flux?" table | The cube-corner flux problem |
| 10 | Gauss in matter (pointer) | Free vs bound charge, the vector $\mathbf D$, and the promise that the shipped capacitors note and the dielectric section of PART 15 resolve it; here: only the statement | The "why $\varepsilon_0$ is not the only constant" note |
| 11 | Gauss and gravity | The same structure for a $1/r^2$ force: $\oint\mathbf g\cdot d\mathbf A=-4\pi GM_{\text{enc}}$; the shell theorem as a corollary; the "why a $1/r^3$ pair would have no Gauss law" insight | Shell theorem re-derived by flux |

**Must be derived, not stated:** the solid-angle flux proof; all seven field results (point, shell,
sphere, line, cylinder, sheet, slab); the cavity result; the two-connected-spheres density ratio; the
flux-through-a-disc solid-angle result; the "flux through a cube's face" family.

**DIAGRAM briefs (D14.1–D14.16):** flux through a tilted area (with the projected area marked); the
solid-angle cone from a charge to a patch, with the two patched surfaces at different distances; the
Gaussian-surface selection chart for the four symmetries; the spherical shell's $E(r)$ and $V(r)$ with
the continuity at $r=R$; the solid sphere's field profile with the $r$ and $1/r^2$ regions labelled; the
infinitely long line's cylindrical Gaussian surface; the coaxial cylinders; the parallel-sheet
superposition (two rows of arrows adding); the thick slab's linear field with the mid-plane zero; the
conductor's surface with the local patch argument; the cavity-in-a-conductor with a charge and the
induced charges drawn; the Faraday cage with a spark and without; the two connected spheres with the
charge-density ratio and the field-line crowding; the cube-corner flux figure with the eight-cube
symmetry; the flux-through-a-disc solid-angle geometry; the gravity analogue's Gaussian surface inside
the Earth.

**Mandatory archetypes:** field of a uniformly charged shell at three radii; field inside a solid sphere;
field of a long charged cylinder inside/outside; field between two parallel sheets; a charge at the
centre of a cube and at a corner (flux fractions); a charge inside a conducting shell with the surface
charge densities; the slab's field profile; a coaxial cable's field at the inner conductor's surface;
the "where is the field zero between two charges?" problem; the sphere-with-a-cavity problem (also
solved by superposition); the "which surfaces have zero flux?" question; a charged conductor's field just
outside.

**Olympiad block content:** the cavity-in-a-uniformly-charged-sphere problem solved by superposition
(the "add a negative sphere" trick) with a full field map; the electrostatic pressure on a conductor's
surface, $P=\frac{\sigma^2}{2\varepsilon_0}$, derived by the "pull the surface layer apart" force
argument and by the energy argument, then applied to the capacitor plate attraction (hand-off to the
shipped capacitors note) and to the **charged soap bubble** (pressure balance versus surface tension —
the most beautiful cross-topic problem in this block, using PART 11); the self-energy of a uniformly
charged sphere by assembling shells, $U=\frac{3}{5}\frac{kQ^2}{R}$, with the "why the factor is not 1/2
of $QV$" explanation and the classical electron radius estimate; the two-overlapping-cylinders problem
(a uniform field inside the lens — the superb olympiad calculation that also previews the magnetic
equivalent in PART 17); the "how much charge can a sphere hold before the air breaks down?" estimate
(the field at the surface vs the breakdown field of air, giving the maximum charge and the maximum
potential — with real numbers); a "non-inverse-square universe" analysis (if $\mathbf E\propto1/r^3$,
what happens to the shell theorem and to Gauss's law? — a thought experiment that tests whether the
student understands *why* $1/r^2$ is special); the Gauss-law derivation of the gravitational shell theorem
and the free-fall estimate inside a planet (link PART 9); the flux-through-a-disc problem generalised to
a patch of any shape via solid angle; the Faraday-cage shielding effectiveness with a "how big a hole is
still safe?" argument; the field inside a uniformly charged *cube* by superposition of eight smaller
cubes (a genuinely hard but elementary olympiad problem).

**Traps to plant:** using Gauss's law to find $\mathbf E$ where the symmetry is absent; forgetting the
enclosed-charge bookkeeping when a surface passes through a distribution; using $\sigma/\varepsilon_0$
for a charged *sheet* (it is $\sigma/2\varepsilon_0$) versus a conductor's surface (it is
$\sigma/\varepsilon_0$); assuming a charge inside a cavity has no effect on the outside of a conductor;
treating flux as "flow" and expecting a non-zero flux for a charge outside a surface; forgetting that the
Gaussian surface must be closed for the law's statement; mis-drawing the normal direction.

**Exit criteria:** the solid-angle proof precedes the law; the four-step protocol is named and used for
every application; the conductor/cavity section covers the induced-charge bookkeeping; the flux-without-
the-field family has ≥ 5 members; the Olympiad block includes the charged-bubble pressure balance, the
two-cylinder uniform field and the non-inverse-square test.

---

### PART 15 · Electric Potential, Potential Energy & Conductors

`electric-potential` · folder `electric-potential/` · source: Cengage ***Electrostatics and Current
Electricity* ch 3 Electric Potential** · needs PART 14 · JEE Advanced · NSEP · INPhO · IPhO.
*The one idea:* potential turns a vector problem into a scalar one, at the price of a direction you
recover by differentiating.

| # | Section | Teach this, in this order | Closes with |
|---:|---|---|---|
| 1 | Why a potential exists | The conservative nature of the Coulomb field: prove the loop integral vanishes (point charge in detail, distributions by superposition); the path-independence consequence | A "which field is conservative?" drill |
| 2 | Definition and reference | $W=q\Delta V$; $V=\frac{U}{q}$; the choice of reference (infinity for isolated charges, ground for circuits) and the "only differences are physical" rule; potential as a scalar map | Compute $V$ for three point charges at a point |
| 3 | Potential of distributions | Superposition of scalars (and the explicit contrast with the vector sum for fields); the point-charge potential; the potential of a shell and of a solid sphere; the "potential at the centre" results; the "why the potential does not fall abruptly at a shell's surface" insight | Sphere/shell $V(r)$ with the graph |
| 4 | From potential to field | $V_b-V_a=-\int\mathbf E\cdot d\mathbf r$; $\mathbf E=-\nabla V$; the equipotential–field-line orthogonality; reading field lines from equipotentials and vice versa; the "field is steeper where the equipotentials crowd" rule | Sketch the field from two given equipotential maps |
| 5 | Differentiate instead of integrate | The method: get $V$ first (a scalar integral), then differentiate to obtain $\mathbf E$ — demonstrated on the ring's axis (recovering PART 13's result with a one-line derivative) and on the disc; the "when is this route cheaper" decision | Disc's axial field from $V$'s derivative |
| 6 | Zeros and zeros | Points where $V=0$ but $\mathbf E\ne0$ (the dipole's equatorial line); points where $\mathbf E=0$ but $V\ne0$ (the centre of a charged ring's axis; the mid-point of a dipole's axis for unequal charges); the "zero is not special" insight and the potential's arbitrary offset | The dipole's zero-potential line problem |
| 7 | Energy of a system of charges | Assemble the system charge by charge and *derive* the factor $\tfrac12$ in $U=\frac12\sum q_iV_i$ (with the honest explanation of where the half comes from); the energy of a charge in an *external* field (no half!); the two-charge, triangle, square and shell-assembly results | Assembly energy of four charges at a square's corners |
| 8 | Conductors in equilibrium | The complete property list (field zero inside, surface equipotential, charge on the surface, field normal, $\sigma/\varepsilon_0$, cavity shielding); the potential of a charged conductor; the "why the whole conductor is at one potential even with non-uniform charge" argument | Which conductor property fails first when a charge approaches? |
| 9 | Induced charges and sharing | Charged concentric shells (compute the potential of each, then the inner sphere's); earthing a shell containing a charge; connecting two charged spheres with a wire (equal potentials, unequal charges — derive the ratio) and the *energy lost* in the connection (with the "where did it go" resolution and the link to PART 7's inelastic collisions); induced charge on a conductor near a point charge | Two-spheres-connected problem with the energy audit |
| 10 | Potentials in the real world | The eV as an energy unit; accelerating a charge through a potential difference (energy conservation); the potential of the Earth and "ground"; the electrostatic hazards and the "why a car is a safe place in lightning" tie-back | A particle accelerated through $V$: find the speed |
| 11 | Energy stored in an assembly | The energy of a charged shell/sphere (assembled by shells) as a two-way calculation ($\frac12QV$ vs the field energy integral); the pointer that the capacitors note owns the systematic treatment; the "energy is in the field" statement with the $u=\frac12\varepsilon_0E^2$ result announced | Reconcile $\frac12QV$ with the field integral |
| 12 | Nuclear and atomic applications | The Coulomb barrier of a nucleus (link PART 26), the ionisation energy of hydrogen by a dimensional + potential estimate (link PART 24), and the "why the nucleus does not explode" energy argument | Coulomb-barrier energy for two protons |

**Must be derived, not stated:** the conservative-field proof; the shell/sphere potentials; $\mathbf
E=-\nabla V$; the ring's field from $V$'s derivative; the half-factor in the assembly energy; the
equal-potential two-sphere charge ratio; the energy lost when two charged spheres are connected; the
field-energy integral's agreement with $\frac12QV$.

**DIAGRAM briefs (D15.1–D15.16):** the closed loop in a point charge's field with the two arcs cancelling;
the equipotential contours and field lines for (a) a point charge, (b) a dipole, (c) two like charges;
the $V(r)$ and $E(r)$ graphs for a shell (with the discontinuity in $E$ but not in $V$); the ring's
axial $V$ curve with the field's derivative sketched beneath it; the dipole's zero-potential plane with
a non-zero field marked on it; the assembly of four charges with the successive-work bookkeeping; the
concentric-shells problem with the potential at four radii; the earthed-shell-with-a-charge
configuration with the induced charges; two connected spheres with the density ratio and the field-line
crowding; the energy-loss-on-connection apparatus with the "heat and radiation" outcome; the eV scale
chart; the field-energy integral over all space (annulus shells drawn); the Coulomb barrier's
energy–distance curve; the drop-model competition between surface energy and Coulomb energy (link
PART 26); the "ground" symbol with the Earth's own potential caveat; an equipotential map of a real
conductor's neighbourhood.

**Mandatory archetypes:** the potential at a point due to a charge configuration; $V$ from $\mathbf E$
along a path; $\mathbf E$ from a given $V(x,y)$; the potential of a ring/disc/rod on the axis; the
potential energy of a three-charge system; the work to move a charge between two points; the potential
inside a charged shell with a point charge inside (the induced-charge family); the two-spheres-connected
problem; the "find the field from the equipotential spacing" question; a particle accelerated through a
potential difference; the energy to assemble a sphere from shells; the potential of a dipole at a general
angle.

**Olympiad block content:** the potential of a uniformly charged rod and the logarithmic/near-field
behaviour; the potential of a charged ring at a general point (statement and one evaluation by the
complete elliptic integral named but not required) and the "why the centre's field is zero and the
centre's potential is maximum" pairing; the general theorem "$\mathbf E=-\nabla V$ implies no closed
field lines in electrostatics" (with the proof sketch from the loop integral); the self-energy of a
charged sphere computed both ways and the **classical electron radius** $r_e=\frac{e^2}{4\pi\varepsilon_0
m_ec^2}$ with the honest statement that this is a warning, not a prediction; the energy of a charged
capacitor's field (hand-off to the shipped capacitors note but one worked problem here); the
"how much energy is released when two charged droplets merge?" estimate with the surface-energy
comparison (a beautiful link to PART 11 and PART 26); the **image-charge method** introduced for a
charge near a grounded plane (state the construction, prove it satisfies the boundary conditions, and
compute the force and the induced charge) — the reader is told the shipped capacitors note and the
olympiad literature take this further; the potential map of a grounded conductor near a point charge
with the "why the field lines meet the surface perpendicular" check; the "shielding a voltmeter" problem
(the field inside a conductor is zero, so measure there — with the caveat about the leads); the
Coulomb-blocking/ionisation limit of a charged nanodrop (the Rayleigh-limit-style estimate
$Q_{\max}\sim8\pi\sqrt{\varepsilon_0\gamma R^3}$ stated and evaluated for a water drop, linking PART 11's
surface tension to this chapter's Coulomb energy: the single best synthesis problem in the block).

**Traps to plant:** treating the potential as a vector; forgetting the sign in $V=-\int\mathbf
E\cdot d\mathbf r$; assuming $V=0$ means $\mathbf E=0$; using the half-factor for a charge in an external
field; forgetting that a conductor's interior can have a non-zero potential; assuming the charge
distribution on a conductor is uniform; forgetting the induced charges when computing the field outside
a conducting shell that contains a charge; adding potentials without regard to sign; mixing the
"ground = 0" convention with "infinity = 0" in the same problem.

**Exit criteria:** the conservativeness is proved before the potential is defined; the differentiate-
instead-of-integrate method is demonstrated; the half-factor in $U$ is derived and contrasted with the
external-field case; the conductor properties are derived, not listed; the two-sphere energy-loss problem
is present with the resolution; the Olympiad block contains the image method, the self-energy and the
charged-drop Rayleigh estimate.

---

---

### PART 16 · Magnetic Field, Biot–Savart & the Lorentz Force

`magnetic-field` · folder `magnetic-field/` · source: **no PDF in this repo** (the magnetism volume was
never supplied) — build the coverage map from the standard JEE Advanced headings: magnetic field and
Biot–Savart, field of straight wire/arc/loop/solenoid/toroid, Lorentz force, motion of a charge, force
and torque on a current loop, magnetic dipole and parallel currents · needs PART 15 · JEE Advanced · NSEP · INPhO · IPhO.
*The one idea:* a magnetic field is what a moving charge calls the relativistic correction to the
electric force, and its effects are always perpendicular to motion.

| # | Section | Teach this, in this order | Closes with |
|---:|---|---|---|
| 1 | The observation | Oersted's compass; magnetism as a *moving-charge* phenomenon; the honest statement that there are no magnetic monopoles (and what that forbids); the "which forces are magnetic?" question | A concept check: does a stationary charge feel $\mathbf B$? |
| 2 | The Lorentz force | $\mathbf F=q(\mathbf v\times\mathbf B)$; the three properties (perpendicular to $\mathbf v$ → no work; zero when parallel; direction by the right-hand rule); the right-hand-rule errors and how to avoid them; SI units and the tesla's size | Force-direction drill with signs |
| 3 | Circular and helical motion | $\mathbf F$ perpendicular to $\mathbf v$ → circular motion; derive $r=\frac{mv}{qB}$; the cyclotron frequency $\omega=\frac{qB}{m}$ **independent of the speed** (the crucial insight); pitch of a helix; the "which plane does it circle in?" method | Radius and period for an electron at a given speed |
| 4 | Combined fields | Velocity selector ($v=E/B$), the crossed-field motion with a full solution (the cycloid coming in PART 18), the magnetic bottle preview; the "what if $\mathbf E$ and $\mathbf B$ are parallel?" case | Velocity-selector calculation |
| 5 | Biot–Savart | The law $\mathbf B=\frac{\mu_0}{4\pi}\int\frac{I\,d\mathbf l\times\hat r}{r^2}$; its "experimental input" status; the direction rule; the superposition of $d\mathbf B$; the dimensional check | Field at a point from a given $I\,d\mathbf l$ |
| 6 | The straight wire | Finite wire by angle parametrisation (derive the "both ends" form), semi-infinite cases, the infinite-wire limit $\frac{\mu_0I}{2\pi r}$; the field's direction by the right-hand grip rule | Field at the centre of a square/hexagon of wires |
| 7 | The loop and the arc | The circular loop's centre field $\frac{\mu_0I}{2R}$; the axial field (derive); the arc and the semicircle; the "field at the centre of a compound loop" (straight + arc) method | Compound-loop field problem |
| 8 | Solenoid and toroid | Stack the loops to get the infinite solenoid's $\mu_0nI$; the finite solenoid's edge field (half, stated with the argument); the toroid; the "why the outside field is nearly zero" reasoning | Solenoid field with the finite-length caveat |
| 9 | The magnetic moment | Define $\boldsymbol\mu=IA$ (direction by the current's right-hand rule); the axial/equatorial dipole fields; the direct analogy table with the electric dipole (with the honest factor-of-difference listed) | The dipole analogy table completed by the reader |
| 10 | Force on a current | Derive $\mathbf F=I\mathbf L\times\mathbf B$ from the charge version (drift velocity → the $IL$ form); the force on a curved wire = the force on the chord (proved); the net force on a closed loop in a uniform field = 0 (with the "then why does it rotate?" answer coming next) | Force on a semicircular wire |
| 11 | Torque on a loop | The two-side-force derivation of $\boldsymbol\tau=\boldsymbol\mu\times\mathbf B$; the potential energy $U=-\boldsymbol\mu\cdot\mathbf B$; the stable/unstable orientations; the moving-coil galvanometer's principle (link the shipped current-electricity note's instruments) | Torque and energy of a tilted loop |
| 12 | Forces between currents | Parallel wires: the force per unit length $\frac{\mu_0I_1I_2}{2\pi d}$, same-direction attraction, and the historical *definition* of the ampere; the "which wire feels what" third-law check; the force between a wire and a moving charge (with the honest "third law is saved by momentum in the field" box) | Two-wire force with a numeric answer |
| 13 | Where the energy comes from | The "the field does no work, yet the motor runs" resolution: the source does the work, the motor's torque does the work on the load, and the EMF that appears in the coil is the bridge to PART 20 (one page, clearly flagged as a forward link) | A concept check on work and magnetic forces |

**Must be derived, not stated:** $r=\frac{mv}{qB}$ and the cyclotron period; the fields of the finite
wire, the loop, the arc, the solenoid and the toroid; the dipole's field forms; $\mathbf F=I\mathbf
L\times\mathbf B$ from the microscopic force; the curved-wire chord theorem; $\boldsymbol\tau=\boldsymbol
\mu\times\mathbf B$; the parallel-wire force per unit length.

**DIAGRAM briefs (D16.1–D16.18):** Oersted's experiment with the compass deflections; the right-hand
rule shown three ways (the flat hand, the grip rule, the cross-product geometry) with a "which finger
points where" caption; the circular orbit with $\mathbf v$, $\mathbf B$, $\mathbf F$ marked at four
points; the helix with the pitch labelled; the velocity selector with the crossed fields and the
undeflected path; the $d\mathbf l\times\hat r$ geometry for Biot–Savart; the finite wire's
angle-parametrisation diagram; the loop's axial field with the element method; the solenoid's stacked
loops and the resulting field lines (with the outside's weak return field drawn small); the toroid's
field lines; the magnetic-dipole field lines beside the electric-dipole ones; the curved wire and its
equivalent chord; the loop in a field with the two side forces and the torque axis drawn; the
galvanometer's coil in a radial field; two parallel wires with the force arrows and the same/opposite
direction comparison; the field-momentum resolution cartoon for the two-charge third-law puzzle; a
solenoid's edge-field plot; the "field lines of a bar magnet vs a solenoid" equivalence (a bridge to
PART 19).

**Mandatory archetypes:** force on a charge with a given velocity direction; radius and period in a field;
a charge entering at an angle (helix); a velocity selector; field at the centre of a square loop; field on
the axis of a coil; field inside a solenoid; field of a toroid; force on a current-carrying wire at an
angle; force on a curved wire; net force on a closed loop; torque on a rectangular coil with $N$ turns;
a galvanometer's deflection; the force between two parallel wires; the magnetic moment of a rotating
charged ring; the field inside a current-carrying cylindrical shell.

**Olympiad block content:** the "magnetism is a relativistic consequence of electrostatics" derivation at
the estimate level (take a current-carrying wire with and without a moving test charge in its rest frame
and show that the electric force from the length-contracted charge density reproduces $F=qvB$ with the
right constant — the single most illuminating derivation in the block, and the correct answer to "what
*is* magnetism?"); the magnetic field of a moving point charge (the $\frac{\mu_0}{4\pi}\frac{q\mathbf
v\times\hat r}{r^2}$ form) and its relation to Biot–Savart; the field of a finite solenoid along its
axis by direct integration (the $\cos$ form) with the edge-field result as a limit; the field of a
rotating uniformly charged disc (integrate the ring contributions) and the "why a rotating charged body
has a magnetic moment proportional to its angular momentum" result (the gyromagnetic ratio, with the
Bohr magneton computed for an electron on a Bohr orbit — a bridge to PART 24); the magnetic-dipole
interaction energy and the "how strong a field does an MRI magnet need to align protons?" order-of-
magnitude; the magnetic-mirror trapping condition's qualitative form and the Van Allen belt picture
(full derivation deferred to PART 18); the "why can't you make a magnetic monopole with a solenoid?" 
argument via the field lines' closure; the magnetic force between a charged particle and a current-
carrying wire; the "magnetic field of the Earth as a dipole" with the dipole moment estimated from the
surface field (real data: 25–65 μT, and the dipole moment $8\times10^{22}$ A·m²) — a genuine
measurement-reconstruction problem; the field of a current sheet and the field's symmetry argument; the
"field of a helix (solenoid) seen from far away" dipole consistency check.

**Traps to plant:** applying the right-hand rule with the *left* hand for a negative charge (solve by
direction of $\mathbf v\times\mathbf B$ then reverse for the sign); thinking $\mathbf F=qvB\sin\theta$
changes the speed; forgetting that $\mathbf B$ does no work but the source does; using $B=\mu_0I/2R$ for a
point off the centre; mixing up $\mu_0/2\pi$ and $\mu_0/4\pi$; adding fields as scalars for a compound
loop; forgetting the $N$ in a coil's moment; assuming the field outside a solenoid is exactly zero;
confusing the direction of $\boldsymbol\mu$ (current's right-hand rule) with the field direction.

**Exit criteria:** the force and the field are introduced in that order (effect before cause); the
cyclotron-frequency independence is derived and highlighted; every field result is integrated from
Biot–Savart; the loop's torque is derived from forces rather than asserted; the "where does the motor's
energy come from" resolution is present with the forward link to PART 20; the Olympiad block contains the
relativistic origin of magnetism and the Bohr magneton.

---

### PART 17 · Ampère's Law, Currents & Magnetic Dipoles

`amperes-law` · folder `amperes-law/` · source: standard JEE Advanced headings (no PDF in this repo):
Ampère's circuital law and its applications (wire, thick wire, plane sheet, solenoid, toroid), forces
between currents, magnetic dipole interaction, magnetic pressure, the no-monopoles statement ·
needs PART 16 ·
JEE Advanced · NSEP · INPhO · IPhO.
*The one idea:* Ampère's law is Gauss's law for currents — symmetry plus a loop integral gives the field
in one line.

| # | Section | Teach this, in this order | Closes with |
|---:|---|---|---|
| 1 | Why a loop law should exist | Revisit the infinite wire's field (which circles the wire) and ask what is special about a closed loop around a current; the "every current inside contributes, every current outside cancels" intuition | A concept check: which loop encloses the current? |
| 2 | Ampère's circuital law | The statement $\oint\mathbf B\cdot d\mathbf l=\mu_0I_{\text{encl}}$; the sign convention fixed once (right-hand rule for the current and the loop together, with a worked positive/negative example); the honest statement of the symmetry requirement | The sign-convention drill with three loops |
| 3 | The applications | Infinite wire (rederived in one line); the thick wire (derive the $B\propto r$ interior and the $B\propto1/r$ exterior with the graph); the coaxial cable (both regions); the infinite sheet $B=\frac{\mu_0K}{2}$; two sheets and the cancellation outside; the solenoid (the rectangular loop derivation and the argument that the outside field is zero); the finite solenoid's edge; the toroid; the cylindrical current sheet | The $\mathbf B$-vs-$r$ graph for a thick wire and a coaxial cable |
| 4 | The overlap trick | Two overlapping cylindrical distributions (a uniform field inside the lens-shaped region — derive it fully; the same method as PART 14's electric case, which is why it is here as well) | The uniform-field-inside-the-lens proof |
| 5 | Ampère vs Biot–Savart | The decision table: use Ampère when the symmetry closes the loop, Biot–Savart when it does not; two problems solved both ways to show the cost difference; the caution that Ampère's law alone cannot give the field of a finite wire | A "which tool first?" drill |
| 6 | Forces on currents revisited | Parallel wires (from Ampère's law to the force per unit length); the rail geometry; the force on a wire in a non-uniform field; the solenoid's end force and the "magnetic pressure" $B^2/2\mu_0$ derivation; the relay/launcher principle | The solenoid-end force with the magnetic-pressure argument |
| 7 | The magnetic dipole as the fundamental object | The equivalence of a bar magnet and a solenoid (with the "why the pole picture is a convenience" box); the dipole moment of a magnet; the field's form inside and outside; the "how do you measure a magnet's moment in a lab?" procedure (oscillation method — link PART 10's torsion pendulum) | Measure-the-dipole-moment procedure |
| 8 | Boundary conditions and field energy (announced) | The normal/tangential field rules at a surface current (stated, used to explain the solenoid's interior/exterior field jump); the energy density $B^2/2\mu_0$ announced with the promise that PART 21 derives it | Why the solenoid's field jumps at the winding |
| 9 | No monopoles | The consequences of $\nabla\cdot\mathbf B=0$: field lines close, a cut magnet gives two magnets, the flux through any closed surface is zero; the "how would you detect a monopole?" idea | The "cut the magnet in half" concept check |

**Must be derived, not stated:** the sign convention with a worked instance; the thick-wire and coaxial
profiles; the sheet's field; the solenoid's interior field; the toroid's field; the overlap trick's
uniform field; the magnetic pressure at a solenoid's end; the dipole's oscillation period.

**DIAGRAM briefs (D17.1–D17.14):** the loop-around-the-wire with the current's right-hand rule drawn
consistently; the positive and negative loop orientations on the same wire; the Amperian loops for five
geometries on one plate; the thick wire's $\mathbf B(r)$ graph with the two regions; the coaxial cable's
Amperian circle at three radii; the two parallel sheets' field superposition with the outside
cancellation; the solenoid's rectangular Amperian loop with the four sides' contributions marked; the
toroid with the circular Amperian path inside the winding; the overlapping-cylinders construction with
the lens region marked; the rail geometry with the force on the moving bar; the solenoid's end with the
magnetic-pressure arrows; the bar magnet and solenoid equivalence with identical field lines; the
oscillating bar magnet in a field with the moment and period labels; the "cut magnet" thought experiment.

**Mandatory archetypes:** field inside and outside a cylindrical conductor carrying a uniform current
density; field of a coaxial cable in both regions; field of a current sheet and of two sheets; the field
inside a solenoid with $N$ turns and length $L$; the field inside a toroid of given dimensions; the force
per unit length between two wires; the force between two currents at an angle; the torque on a coil in a
field from the moment; the oscillation period of a magnet in a known field; the field of a rotating
charged cylinder; the overlapping-cylinder uniform-field question; the magnetic pressure on a solenoid's
end.

**Olympiad block content:** the "magnetic pressure" $B^2/2\mu_0$ derived as the force per unit area on a
field-confining boundary and applied to (a) the solenoid's end, (b) the wire's self-constriction (the
$I^2$ inward force and the "why a thick wire can explode" pinch estimate — the z-pinch), (c) the
levitation of a superconducting slab; the two-cylinders uniform-field result's *use*: the field gradient
inside the overlap region and the "how would you build a uniform-field region?" design question;
the interaction of two magnetic dipoles — derive the force law ($\propto1/r^4$) and the alignment
torques, then apply to a compass near a magnet and to a "magnetic dimer"; the magnetic field of a
rotating charged sphere (integrate the surface current) and the check that it reduces to the earlier
ring result; the field inside a uniformly magnetised sphere via its bound surface current (state and
evaluate: $B=\frac{2}{3}\mu_0M$); the "why does a ferromagnetic rod concentrate the field?" (link
PART 19) with a factor-of-$\mu_r$ estimate; the field of an infinitely long solenoid with a *finite*
thickness winding layer; the "how uniform is the field in a real Helmholtz pair?" problem (compute the
field along the axis and the vanishing second derivative — the Helmholtz condition $d=2R$ derived, a
beautiful olympiad calculation); a magnetic shielding estimate for a ferromagnetic shell; the "magnetic
field at the centre of a current-carrying wire is zero — reconcile with Ampère's law" conceptual trap.

**Traps to plant:** using Ampère's law with a loop that does not enclose the current; getting the sign
wrong by reversing the loop's direction; assuming the field is constant along a loop that does not have
the symmetry; forgetting the $N$ turns in a solenoid's enclosed current; confusing $K$ (current per unit
width) with $I$; using the parallel-wire force with the *sum* of the two fields (the classic
gauge-field vs test-field error — the correct field at wire 2 is the one produced by wire 1 only);
assuming the field inside a current-carrying *shell* is zero when it is (careful: for a cylindrical
shell the interior field is zero only if you are inside a long shell — state the assumption).

**Exit criteria:** the loop law is *motivated* from the wire's field before it is stated; the sign
convention is fixed with a worked example; ≥ 7 applications each derived with the four-step method; the
Ampère-vs-Biot–Savart decision table is present with two dual solutions; the Olympiad block contains the
magnetic pressure, the Helmholtz condition and the magnetised-sphere field.

---

### PART 18 · Cyclotron, Velocity Selector & the Hall Effect

`moving-charges-magnetism` · folder `moving-charges-magnetism/` · source: standard JEE Advanced headings
(no PDF in this repo): circular and helical motion, velocity selector, mass spectrometer, cyclotron,
$\mathbf E	imes\mathbf B$ drift, magnetic mirror, Hall effect, $e/m$ measurement (plus the olympiad
extensions listed below) · needs PART 17 · JEE Advanced · NSEP · INPhO · IPhO.
*The one idea:* in a magnetic field a charge circles to a clock whose rate depends only on $q/m$ and $B$ —
that single fact is an industry.

| # | Section | Teach this, in this order | Closes with |
|---:|---|---|---|
| 1 | The three-region method | Particle motion problems solved by the protocol: identify the field regions → write $r=mv/qB$ in each → match the geometry (tangency, exit angle, time in each region); the "time spent in a field region" calculation | A two-region deflection problem |
| 2 | The velocity selector and the mass spectrometer | The selector's $v=E/B$ (derived, with the "what if $v$ is not exactly $E/B$?" analysis); the mass spectrometer's $r=\frac{mv}{qB'}$ and the mass-to-charge separation of isotopes; the resolution question (can it separate $^{235}$U from $^{238}$U?) | The isotope-separation radius difference |
| 3 | The cyclotron | The two-dee geometry; the resonance condition $f=\frac{qB}{2\pi m}$ (and its independence of speed, from PART 16); the maximum energy from the outer radius $E_{\max}=\frac{q^2B^2R^2}{2m}$; the number of revolutions and the total time; the practical limits (relativity, focusing) | Cyclotron energy for a real proton machine |
| 4 | Helical motion and magnetic mirrors | The pitch and the drift along $\mathbf B$; the converging field's mirror effect; the adiabatic invariant $\mu=\frac{mv_\perp^2}{2B}$ and the trapping condition; the loss cone; the Van Allen belts; the fusion-mirror concept (a one-page bridge to PART 26's fusion) | Mirror-trap condition with numbers |
| 5 | The Hall effect | Derive $V_H=\frac{IB}{nqt}$ from the force balance; determine the carrier sign; measure $n$ and the mobility; the "why the Hall voltage is small in copper and usable in semiconductors" comparison | Hall-voltage calculation for a real sample |
| 6 | Crossed fields and drifts | The $\mathbf E\times\mathbf B$ drift velocity derived two ways (force balance and the Lorentz-transformed frame); the cycloid/curtate trajectory with the rolling-circle interpretation; the gradient and curvature drifts (stated with the physical picture, derived for the gradient case) | The cycloid's amplitude and drift speed |
| 7 | Measured $q/m$: the electron | J. J. Thomson's tube: the deflection equations, the $\frac{e}{m}$ combination from the deflection and the magnetic bend, and the "what actually gets measured" logic; the Millikan-style charge measurement's role in getting $m_e$; the honest scale of both numbers | The $e/m$ calculation from a described tube |
| 8 | Where it matters | The synchrotron (and why the cyclotron's limit forces it), magnetic confinement, MHD thrusters, plasma heating (link EM waves), mass spectrometry in chemistry, and the aurora | An order-of-magnitude for the aurora's field and energy |
| 9 | The particle zoo preview | Pair production and the positron's discovery in a cloud chamber (curvature + energy loss → direction and momentum), the bubble chamber's spiral; the "how do you read a photograph?" skill | Read a described cloud-chamber spiral |

**Must be derived, not stated:** the selector condition; the cyclotron resonance and maximum energy; the
mirror invariant and the trapping cone; the Hall voltage and the carrier-sign rule; the $\mathbf E\times
\mathbf B$ drift; the cycloid trajectory; the gradient drift; the Thomson deflection formulas.

**DIAGRAM briefs (D18.1–D18.16):** the three-region particle path with the tangency points marked; the
velocity selector with the undeflected path and the two deviated paths; the mass spectrometer with two
isotope arcs of different radii; the cyclotron with the two dees, the gap crossings and the spiral; the
resonance condition's "field-locked" timing diagram; the helical path with the pitch and the drift field
lines; the converging mirror field with the reflection at the throat; the loss cone in velocity space;
the Hall plate with the carriers' deflection, the transverse field and the polarity convention (with the
"what if the carriers are positive?" panel); the $\mathbf E\times\mathbf B$ drift with the crossed fields
and the straight path; the cycloid trajectory with the rolling circle drawn beneath it; the gradient
drift in a non-uniform field; the Thomson tube's plates, coil and screen; the cloud-chamber spiral with
the radius decreasing (energy loss) and the "which way does it curve?" annotation; the synchrotron ring
with the bending and accelerating cavities; the aurora's field-line geometry with the precipitating
particles.

**Mandatory archetypes:** radius of a particle given $v$ and $B$; the time spent in a field region; a
particle entering at an angle (helix); the velocity-selector problem; the mass-spectrometer radius ratio
for two isotopes; the cyclotron's maximum energy and frequency; the Hall voltage and the carrier sign;
the conductivity from the Hall data; the $\mathbf E\times\mathbf B$ drift speed; the cycloid's
dimensions; the gradient-drift direction; the Thomson tube's deflection; the mirror-trap condition.

**Olympiad block content:** the full cycloid solved by integrating the crossed-field equations and then
re-solved by jumping into the drifting frame (where the field is a pure $\mathbf B$ and the path is a
circle) — the second method is the lesson; the gradient and curvature drift derivations with the
$R$-dependence, and their application to the Earth's radiation belts' particle lifetimes (order of
magnitude); the Fermi acceleration mechanism of cosmic rays (a charged particle bouncing between
converging magnetic mirrors — with the fractional energy gain per bounce and the "how many bounces to
double the energy?" estimate; this is the magnetic analogue of the elastic bounce off a moving wall from
PART 7); the relativistic cyclotron frequency and the "why the synchrotron is not a cyclotron" analysis
with numbers for a 1 GeV electron; the betatron condition (a changing flux that both accelerates and
guides: derive the 2:1 relation between the field at the orbit and the average field inside — this is
revisited in PART 20 where it properly belongs; here the reader sees why the geometry matters); the Hall
effect in a *semiconductor* with both carrier types present (the "why the sign can flip with
temperature" analysis); the "how do you weigh a single molecule?" mass-spectrometry estimate; the
magnetic-mirror fusion reactor's design constraint (the mirror ratio and the plugging energy estimate);
the "what is the momentum of the particle in that photograph?" cloud-chamber exercise with a stated
field and radius; the aurora's total particle energy estimate (the solar-wind power hitting the
magnetosphere, order of magnitude).

**Traps to plant:** using $r=\frac{mv}{qB}$ with $v$ the component *along* the field (it must be the
perpendicular component); forgetting that a charge entering parallel to $\mathbf B$ feels nothing; mixing
the time in the field region with the period; assuming the cyclotron frequency changes with energy
(it does — but only relativistically, which the classical theory denies; say so); getting the Hall
polarity backwards because the sign of the carriers was forgotten; treating the $\mathbf E\times\mathbf B$
drift as a force; confusing the curate/cycloid/prolate families.

**Exit criteria:** the three-region protocol is named and used; the cyclotron's resonance and energy
limits are derived with a worked numeric machine; the Hall effect is derived and used to determine a
carrier sign; the drift family is presented with the physical picture; the Olympiad block contains the
two-method cycloid and the Fermi acceleration; the cloud-chamber reading skill is practised.

---

---

### PART 19 · Magnetism & Matter, Earth's Magnetism

`magnetism-and-matter` · folder `magnetism-and-matter/` · source: standard JEE Advanced headings (no PDF
in this repo): magnetisation and bound currents, $\mathbf B$–$\mathbf H$–$\mathbf M$, dia/para/ferro
magnetism, hysteresis, Earth's magnetism (declination, dip, components) · needs PART 17 · JEE Advanced · NSEP · INPhO.
*The one idea:* matter responds to magnetic fields through induced (dia), aligned (para) or permanently
ordered (ferro) dipoles.

| # | Section | Teach this, in this order | Closes with |
|---:|---|---|---|
| 1 | The magnet as a dipole | The moment of a bar magnet; the pole picture as a convenience and its failure inside the material; the solenoid equivalence; the field inside and outside a magnet; the "cut it in half" concept | Field comparison of a magnet and a solenoid |
| 2 | Magnetisation | $\mathbf M$ = moment per unit volume; the bound surface current $K_b=M$ and the bound volume current $\nabla\times\mathbf M$ (stated, with the flat-slab derivation of $K_b$); the "why a magnetised cylinder behaves like a solenoid" insight | Derive the equivalent surface current for a uniformly magnetised rod |
| 3 | The field inside matter | $\mathbf B=\mu_0(\mathbf H+\mathbf M)$; the three conventions ($\chi$, $\mu_r$) and what each is measured for; the "which field is the applied one?" clarification with the demagnetising-field caveat named | The three-convention conversion drill |
| 4 | Diamagnetism | The induced-moment mechanism (Lenz at the atomic level: an applied field changes the orbital motion so as to oppose it); the weak negative $\chi$; the "why water, copper and bismuth are diamagnetic" table; the "everything has a diamagnetic part" insight | Compare $\chi$ magnitudes across the three classes |
| 5 | Paramagnetism | Competing alignment and thermal disorder; the Langevin/Curie picture; the $1/T$ dependence (Curie's law, stated and applied); the saturation at high field/low temperature; the "why the effect is weak at room temperature" estimate | Curie-law numeric comparison |
| 6 | Ferromagnetism | Domains and the exchange interaction (words, with the honest "this is quantum" flag); saturation, retentivity, coercivity; the hysteresis loop and its enclosed area as energy dissipated per unit volume per cycle (derived via the $\int H\,dB$ work); soft vs hard magnets and their uses; why heating/hammering demagnetises | Hysteresis-loop energy loss calculation |
| 7 | Materials in circuits | The solenoid with a core (the $\mu_r$ amplification derived from the bound currents); the transformer core's requirements (soft iron, laminated — the eddy-current link to PART 20); magnetic shielding; the electromagnet's design; the read/write head idea | Core-amplification calculation |
| 8 | Forces on materials | A magnet near a nail (induced dipole attraction); the "why only iron is strongly attracted"; the magnet's force on a diamagnetic object (repulsion — and the levitation of a frog/superconductor teaser); the "how much can a magnet lift?" estimate | Estimate the lift of a small electromagnet |
| 9 | Earth's magnetism | The field as a tilted dipole (with the pole/north confusion resolved); declination, dip (inclination) and the horizontal component; the three-component decomposition of $\mathbf B$ (a 3-D vector exercise, linking PART 2); the "why a compass points north" and the "where does a compass fail?" (the poles) | The three-component problem at a given latitude |
| 10 | Magnetism in nature | Paleomagnetic reversals, the magnetic field's role in animal navigation (qualitative), the solar wind's interaction, the Curie temperature and the loss of magnetism on heating, the "where does the Earth's field come from?" (the dynamo, one paragraph) | Reading a magnetic-anomaly map |

**Must be derived, not stated:** the bound surface current for a uniformly magnetised cylinder; the
$\mu_r$ amplification of a solenoid with a core; the hysteresis-area energy loss; the Curie-law
temperature dependence (with a two-level Boltzmann estimate); the three-component Earth-field
decomposition.

**DIAGRAM briefs (D19.1–D19.14):** a bar magnet's field lines vs a solenoid's (side by side);
magnetisation with the bound surface currents drawn on a cylinder; the $\mathbf B$, $\mathbf H$,
$\mathbf M$ relation as a three-bar chart; the diamagnetic induced-moment mechanism (the applied field
and the opposing induced current loop); the paramagnetic alignment-vs-thermal picture; the domain
structure and its growth with an applied field (four stages); the hysteresis loop with saturation,
remanence and coercivity labelled and the area shaded; soft vs hard loops compared; a solenoid with a
core with the bound currents marked; the magnetic shield (a shell in a field); the magnet lifting a nail's
induced dipole; the Earth's dipole with the geographic poles marked and the declination/dip angles; the
three components of the field at a mid-latitude point; the Curie-temperature magnetisation collapse
curve.

**Mandatory archetypes:** the moment of a magnet from its oscillation period in a known field; comparing
$\chi$ magnitudes; the relative permeability from a coil's inductance change (link PART 21); the
hysteresis-loss estimation; the core's effect on a solenoid's field; the Earth's field components at a
stated latitude; the dip angle at the magnetic equator and poles; a magnet's oscillation in the Earth's
field (measurement problem); the "which material for a permanent magnet / for a transformer core?"
choice; the induced-magnet attraction problem.

**Olympiad block content:** the magnetic energy density $u=\frac{B^2}{2\mu_0}$ used as a *force* tool:
derive $F=-\frac{dU}{dx}$ for a magnet being pulled off an iron plate (the classic "how strong is a fridge
magnet, really?" calculation) and for the force between two magnets; the demagnetising factor (why the
field inside a bar magnet is much less than the material's magnetisation; state $H_d=-N_dM$ and use it
for the "why does a long thin magnet keep its magnetism?" question); the magnetic field inside a
uniformly magnetised sphere via its bound surface current, $B=\frac{2}{3}\mu_0M$ (a clean olympiad
derivation); superconductors as perfect diamagnets — the Meissner effect, the levitation force
$F=\frac{B^2A}{2\mu_0}$, and the "how much can a 1 T field levitate?" estimate; the Curie–Weiss law
$\chi=\frac{C}{T-T_c}$ (statement + the "why the divergence at $T_c$ means a phase transition" reading);
the "magnetic refrigeration" idea (the magnetocaloric effect) as an order-of-magnitude energy estimate;
the dipole-dipole interaction in a ferromagnetic lattice's *scaling* argument (the exchange energy must
beat $kT$ — derive the Curie temperature's order of magnitude from the exchange energy! — a stunning
estimate); a compass's accuracy limit (the field of a nearby current-carrying wire vs the Earth's field
— a real measurement problem); the "magnetic field of the human heart" order-of-magnitude (the
SQUID magnetometer's need); the "why do the magnetic poles wander?" short discussion with the real drift
rate.

**Traps to plant:** confusing $\mathbf B$ with $\mathbf H$ and quoting the wrong symbol in a
$\mu_r$ problem; assuming $\mu_r$ is constant (it is not, for ferromagnets); saying "diamagnetic materials
have $\mu_r=0$"; forgetting the retentivity/coercivity distinction (hard vs soft); using the Curie law
for a ferromagnet; assuming the Earth's *geographic* north pole is the magnetic north pole (it is the
magnetic *south* pole of the dipole); mixing the dip angle with declination; forgetting the bound
currents when computing a magnet's equivalent coil.

**Exit criteria:** the dia/para/ferro mechanisms are explained mechanically (not just tabulated); the
hysteresis loop is read as an energy-loss diagram; the core-amplification result is derived from bound
currents; the Earth's field is a 3-D vector exercise; the Olympiad block contains the Meissner levitation
and the Curie-temperature scaling estimate.

---

### PART 20 · Electromagnetic Induction: Faraday, Lenz, Motional EMF & Eddy Currents

`electromagnetic-induction` · folder `electromagnetic-induction/` · source: standard JEE Advanced
headings (no PDF in this repo): magnetic flux, Faraday's law and Lenz's law, motional EMF, rod-and-rails
family, induced electric fields, eddy currents, generators and motors, mutual induction preview ·
needs PART 17 · JEE Advanced · NSEP · INPhO · IPhO.
*The one idea:* a changing magnetic flux drives an electric field, and Lenz's law is energy conservation
wearing a disguise.

| # | Section | Teach this, in this order | Closes with |
|---:|---|---|---|
| 1 | Flux | The definition $\Phi=\int\mathbf B\cdot d\mathbf A$; the surface and its normal convention; flux through a tilted loop; flux of a non-uniform field; the "flux is a scalar but has a sign" bookkeeping | Flux through a loop in three orientations |
| 2 | The discovery and the law | The experiments (magnet and coil, moving loop, changing area, rotating loop); Faraday's law $\mathcal E=-\frac{d\Phi}{dt}$; the minus sign's meaning; the "how do you decide the sign of the EMF?" protocol | Sign-of-EMF drill |
| 3 | Motional EMF from the Lorentz force | Derive $\mathcal E=Bvl$ from $q\mathbf v\times\mathbf B$ — *without* flux — and note that this and Faraday are independent statements that agree; the "which is the physical law?" honest discussion; the flux rule's celebrated failure case (a loop with a moving boundary where the flux argument hides the physics) | The two derivations side by side |
| 4 | Lenz's law as energy conservation | The statement, the algorithm (find $\Delta\Phi$ → the induced current opposes it → the mechanical consequence); the "why the loop resists your pull" energy audit; the "Lenz's law gives the direction, Faraday gives the value" discipline | The falling-magnet-in-a-copper-tube estimate |
| 5 | The standard configurations | A rod sliding on rails (derive the EMF, the current, the force, the acceleration's decay and the terminal speed, with the power balance); a rod rotating about one end (derive $\mathcal E=\frac12B\omega L^2$ by integrating $v\times B$); a rotating loop (derive the sinusoidal EMF and its peak); the disc dynamo; a loop pulled out of a field region (the two-part EMF analysis); a loop entirely inside a changing field | Rod-on-rails complete solution with the energy check |
| 6 | Coupled mechanics and circuits | The rod on rails with a mass hanging over a pulley (the two-equation system and the terminal state); the rod with a capacitor instead of a resistor (no steady current, the uniformly accelerated rod — the famous trap); the rod with friction; the rod with a spring | The capacitor-rod's constant acceleration derived |
| 7 | Induced electric fields | Faraday's law read as "a changing $\mathbf B$ creates $\mathbf E$"; the induced circular field inside a changing flux region (derive $E=\frac{r}{2}\frac{dB}{dt}$ inside and $E=\frac{R^2}{2r}\frac{dB}{dt}$ outside); the non-conservative nature and the "why no potential here" box; a charged particle accelerated by the induced field | The induced-field magnitude at two radii |
| 8 | The betatron condition | An electron on a circular orbit in a growing field: the acceleration from the induced EMF plus the guiding field → derive $B_{\text{orbit}}=\frac12\langle B\rangle$ (the 2:1 condition); the "why a uniform field cannot work" check | The 2:1 condition derived with numbers |
| 9 | Eddy currents | The origin; the retarding force on a plate entering a field; magnetic braking (derive the exponential velocity decay $v=v_0e^{-t/\tau}$ and the $\tau$ from the plate's thickness and conductivity); induction heating/cooking; the transformer's lamination (the $\propto d^2$ loss scaling derived); the "which metal falls slower?" comparison | The copper-tube terminal-velocity estimate |
| 10 | Generators and motors | The AC generator's EMF curve; the DC generator's commutation; the motor's back-EMF and the "what limits a motor's current at start-up?" question; the motor–generator equivalence (the same machine, read backwards) — the forward link to PART 22 | Motor back-EMF problem |
| 11 | The voltmeter paradoxes | Two voltmeters across the same two points around a changing-flux loop give different readings (the classic); the "how do you even define a potential difference here?" resolution; the honest conclusion that the EMF is not a potential difference | The two-voltmeter problem solved in both paths |
| 12 | Induction in everyday life | Metal detectors, the induction hob, the electric guitar pickup, regenerative braking, the loudspeaker's coil, wireless charging, the maglev idea | One design estimate (a metal detector's sensitivity) |

**Must be derived, not stated:** $\mathcal E=-d\Phi/dt$ with the sign protocol; the motional-EMF law from
the Lorentz force; $\frac12B\omega L^2$; the rotating coil's sinusoidal EMF; the rod-on-rails equations
with the terminal speed; the induced-field profiles; the betatron 2:1 condition; the eddy-current
braking's exponential; the transformer's lamination scaling.

**DIAGRAM briefs (D20.1–D20.18):** the flux through a tilted loop with the normal drawn; the four
experiments that produce an EMF; the sign-convention protocol drawn as a flowchart; the rod on rails with
the Lorentz forces on the charges and the resulting current; the rotating rod with the $v$ profile along
it; the rotating coil's EMF vs angle curve; the loop leaving a field region with the two EMFs marked;
the rod-on-rails-with-hanging-mass system with both free-body diagrams; the capacitor-rod's "no steady
state" current; the induced circular field inside and outside the flux region (two panels); the
betatron's orbit with the field profile $B(r)$ and the average field marked; a plate entering a field with
the eddy-current loops drawn and the retarding force; the magnet falling in a copper tube with the
terminal-velocity force balance; the laminated core with the eddy loops drawn small vs a solid core; the
AC generator's slip rings; the motor's back-EMF; the two-voltmeter paradox with the two paths drawn in
different colours (described in words); the metal detector's coil and the conducting target.

**Mandatory archetypes:** the flux change given $B(t)$; the rod on rails with a resistor (current,
force, terminal speed, power); the rod on rails with a capacitor; the rod on rails with an inductance
(hand-off to PART 21); the rotating rod's EMF; the rotating loop's peak EMF and RMS preview; the
loop-leaving-a-field-region question with the "which side is the positive terminal?" trap; the induced
field inside a solenoid's core region; the charge accelerated by an induced field (find the final
speed); the eddy-current damping time; the betatron's condition; the mutual-inductance-free
"two-rod" problems; a sliding rod with friction and the energy audit; the magnetic braking of a
pendulum.

**Olympiad block content:** the "flux rule vs Lorentz force" paradox family (a loop with a moving
contact, a rotating disc with a sliding contact, the unipolar inductor) with the resolution that the
physics is the field's action on charges and the flux rule is a shortcut valid when the boundary's motion
is simple — this is the single most important conceptual exercise in the chapter; the betatron 2:1
condition derived twice (from the EMF and from the canonical-angular-momentum argument — the second
method is the deeper one); the falling-magnet-in-a-tube problem with the full terminal-velocity
estimate (using the eddy-current drag's $v/(1+...)$ structure) and a comparison with real measurements;
the magnetic braking problem as a damped oscillator (derive the equation and the "critical damping"
condition — linking PART 10's damped SHM to this chapter); the flux-conservation theorem for a
superconducting loop (used fully in PART 21) introduced here via "what happens if the resistance is
zero?"; the energy audit of a generator with a load (mechanical power in vs electrical power out plus
losses) and the "why a generator gets harder to turn when the light bulb is brighter" insight; the
electrodynamic tether (a satellite dragging a wire through the ionosphere: derive the EMF, the current,
the force and the power — a beautiful orbital-engineering problem linking PART 9); the "how much energy
does a metal detector need to see a ₹10 coin?" order-of-magnitude; the induction-cooktop's skin depth and
frequency choice (link the conducting-medium analysis of the shipped EM-waves note); the non-conservative
field's role in the "how does a transformer's core transfer energy?" analysis (Poynting-flux flavour, one
paragraph with the honest pointer to the shipped EM-waves note).

**Traps to plant:** using $\mathcal E=-d\Phi/dt$ for a loop whose *area* is ambiguous (say what surface
you chose); forgetting the sign of the flux when the loop flips; using $Bvl$ for a rod that is not
perpendicular to $\mathbf B$ and $\mathbf v$ both; forgetting the inductor or capacitor in the circuit and
therefore assuming an instantaneous current; ignoring the induced field's direction relative to the
decreasing flux; using a "potential difference" language where only an EMF exists; assuming the
eddy-current force is constant instead of velocity-dependent; getting the lamination benefit as
$\propto d$ instead of $d^2$.

**Exit criteria:** the two independent derivations of induction are both present with their relationship
discussed; Lenz's law is presented as an energy statement with an audit; the coupled mechanics–circuit
family covers the resistor, the capacitor and (as a hand-off) the inductor; the induced-field and
betatron sections are complete; the voltmeter paradox is solved; the Olympiad block contains the
paradox family and the electrodynamic tether.

---

### PART 21 · Self & Mutual Inductance, RL Circuits & Magnetic Energy

`inductance` · folder `inductance/` · source: standard JEE Advanced headings (no PDF in this repo):
self and mutual inductance, $L$ of solenoid/toroid/coaxial cable, RL transients, magnetic energy density,
inductor combinations, LC oscillations, the coil force $F=\frac12I^2\frac{dM}{dx}$ · needs PART 20 ·
JEE Advanced · NSEP · INPhO · IPhO.
*The one idea:* a coil resists changes in its own current because the energy lives in the field, not in
the wire.

| # | Section | Teach this, in this order | Closes with |
|---:|---|---|---|
| 1 | The inertia of current | The observation that a current cannot jump; the flux linkage $N\Phi$; the definition $L=\frac{N\Phi}{I}$; the "why $L$ is geometry only" statement (and the exception: ferromagnetic cores) | A concept check: does $L$ depend on the current? |
| 2 | Computing self-inductance | The solenoid $L=\mu_0n^2Al$ (derived, with the "why $N^2$ matters" insight); the toroid; the coaxial cable via flux integration; the two-wire line; the "inductance per unit length" way of thinking; the $L$ of a single loop (order of magnitude) | Coaxial cable's $L$ derived |
| 3 | Mutual inductance | $M=\frac{\Phi_{21}}{I_1}$; reciprocity $M_{12}=M_{21}$ (stated with the flux argument); the concentric-coil and coaxial-solenoid results; the coupling coefficient $k$ and its meaning; the "when is $M$ zero?" (perpendicular axes) | Mutual inductance of two coaxial solenoids |
| 4 | The RL circuit | The differential equation; the exponential rise and decay; the time constant $\tau=L/R$ (derived); the initial and final states; the "why the current cannot jump but the voltage across $L$ can" statement | $i(t)$ and $V_L(t)$ for a switched RL circuit |
| 5 | The inductive kick | Opening a switch: the huge $L\,di/dt$, the spark, the ignition coil, the protection diode; the "where does the energy go?" analysis; the rise-time limit of a real magnet | The maximum voltage estimate for a real coil |
| 6 | Energy in the magnetic field | Derive $U=\frac12LI^2$ by integrating the power; then derive $u=\frac{B^2}{2\mu_0}$ from the solenoid; the "energy is in the field" statement; the magnetic pressure; the comparison table with the electric case $\frac12\varepsilon_0E^2$ | Field energy in a real magnet, with numbers |
| 7 | The mechanical–electrical analogy | The table (mass ↔ $L$, spring ↔ $1/C$, damping ↔ $R$, force ↔ voltage); using it to *read off* the solution of an unfamiliar circuit; the caution about where the analogy breaks | Translate a mechanical problem into a circuit |
| 8 | Inductors in combinations | Series and parallel (derived), the "they add like resistors in series but the *reason* is different" note; the mutual-inductance correction ($L=L_1+L_2\pm2M$) with the sign discussion; the "why you cannot ignore $M$ for two coils on the same core" | The two-coil-on-one-core equivalent inductance |
| 9 | Energy of coupled coils | $U=\frac12L_1I_1^2+\frac12L_2I_2^2+MI_1I_2$ with the sign convention; the maximum-work-extractable question; the force between two coils $F=\frac12I^2\frac{dM}{dx}$ derived from the energy — the basis of the electromagnetic launcher and the relay | Force between two coils with a real geometry |
| 10 | LC oscillations | Derive $\ddot q=-\frac{q}{LC}$ and identify SHM; the energy exchange table ($\frac12LI^2\leftrightarrow\frac12CV^2$); the frequency; the phase relations; the damped LCR's qualitative behaviour; the "why a real LC circuit rings down" | The LC oscillator's energy cycle |
| 11 | Transients with flux conservation | The "flux linkage cannot jump" rule for a superconducting/zero-resistance loop; energy-loss audits; the "where does the flux go when the geometry changes?" problem | Flux-conservation problem |
| 12 | Inductance in practice | The transformer's ideal equations preview (full treatment in PART 22); the inductor's parasitic resistance and capacitance; the "why high-frequency inductors are hard" note | The ideal-transformer equations stated |

**Must be derived, not stated:** $L$ for the solenoid, toroid and coaxial cable; the RL transient
solution; $\tau=L/R$; the inductive kick; $U=\frac12LI^2$ and $u=B^2/2\mu_0$; the series/parallel
combinations; the coupled-coil energy; the coil-force expression; the LC frequency.

**DIAGRAM briefs (D21.1–D21.16):** the flux linkage in an $N$-turn coil with only one turn's flux drawn;
the solenoid's $L$ derivation with the flux through one turn; the coaxial cable's flux element (an
annular strip) for the integral; two coaxial solenoids with the coupling flux marked; the RL circuit's
$i(t)$ and $V_L(t)$ curves with $\tau$ marked; the inductive kick at a switch with the arc drawn; the
energy density in a solenoid with a slab of field volume; the mechanical–electrical analogy table drawn
as two columns; the two-coils-on-one-core circuit with the dot convention; the force between two coils
with the $dM/dx$ geometry (one coil being pulled); the LC circuit's charge/current/energy curves; the
mechanical analogue's spring-mass with the same curves; the damped LCR's ring-down; the coupled-coil
energy surface (a simple 3-D sketch described in words); the flux-conservation problem's before/after
geometry; a real inductor's equivalent circuit (R and C parasitics).

**Mandatory archetypes:** the solenoid's inductance from geometry; the RL rise/decay with numbers; the
time to reach half the final current; the spark voltage on opening; the field energy in a solenoid; the
inductor's combination with $M$; the LC oscillation period; the coaxial cable's $L$ and $C$ (link the
shipped capacitors note) and the cable's impedance preview; the flux-conservation problem; the force
between a coil and a magnet (the launcher); the mutual inductance of two loops at a distance.

**Olympiad block content:** the "how does a coil launcher throw a ring?" problem — a pulsed current in
one coil and a conducting ring: derive the mutual inductance's role, the impulsive force, the ring's
launch speed and the energy split (a superb multi-part olympiad problem); the coil-force result
$F=\frac12I^2\frac{dM}{dx}$ applied to a magnetic relay and to the "how much force does an MRI gradient
coil produce?" estimate; the flux-conservation theorem in a superconducting loop: when the loop's
geometry changes, the current changes as $I\propto1/L$ and the magnetic energy changes — derive where
the energy comes from (the mechanical work) with a worked example (a superconducting ring squashed);
the "two inductors connected by a switch" problem: the flux-linkage-conservation method to find the final
currents and the energy dissipated; the eddy-current/inductance drag law (the velocity-dependent force
derived from the coupled equations $L\dot I+Ri=\mathcal E$), and its use for magnetic braking from
PART 20 as a *self-consistency* exercise; the "why a big magnet needs a lot of steel" structural
estimate (the $B^2/2\mu_0$ pressure and the stress limit from PART 12 — a genuine engineering physics
problem); the "how long does an LC circuit ring?" answer from the $Q$ factor with a real coil's $R$;
the derivation of the transmission line's characteristic impedance $\sqrt{L/C}$ from the shipped
capacitors note's $C$ per length and this chapter's $L$ per length (a beautiful synthesis that also
explains why an oscilloscope cable is 50 Ω); the "energy in a mechanical relay's coil vs its spring"
comparison; the "magnetic energy storage for a car" estimate ($\frac12LI^2$ with real numbers and the
comparison to a battery's energy density — an order-of-magnitude reality check).

**Traps to plant:** forgetting the $N$ in $L=N\Phi/I$; using $L$ as a "circuit property" independent of
geometry; ignoring the mutual inductance between two coils on a shared core; using $\tau=L/R$ with the
wrong $R$ in a multi-resistor network; assuming the current through an inductor can jump at a switch;
assuming the voltage across an inductor is $L\,di/dt$ with the wrong sign convention; treating the
$\frac12LI^2$ energy as stored "in the wire"; forgetting that $M$ can be negative depending on the
winding sense (the dot convention).

**Exit criteria:** $L$ is derived for three geometries; the RL solution is derived, not quoted, with the
initial/final-state protocol; the inductive kick has a numeric example; the field-energy derivation links
$\frac12LI^2$ to $B^2/2\mu_0$; coupled coils and the coil force are present; the LC oscillator is
identified with SHM and the mechanical analogy table is complete; the Olympiad block contains the
launcher, the superconducting-flux conservation and the $50\,\Omega$ cable synthesis.

---

### PART 22 · Alternating Current, Resonance & Transformers

`alternating-current` · folder `alternating-current/` · source: standard JEE Advanced headings (no PDF
in this repo): AC through R, L, C, phasors, series and parallel LCR resonance, $Q$ factor, power factor,
transformers, LC oscillations, rectification · needs PART 21 ·
JEE Advanced · NSEP · INPhO · IPhO.
*The one idea:* in AC everything is a phase relationship; impedance is resistance that knows about time.

| # | Section | Teach this, in this order | Closes with |
|---:|---|---|---|
| 1 | Why AC and where it comes from | The generator's sinusoidal EMF (link PART 20); the transmission advantage (the transformer needs a changing flux — derived in this chapter); the waveform vocabulary (peak, peak-to-peak, period, frequency, phase) | Read a waveform and write its equation |
| 2 | RMS values | The heating-equivalence definition; derive $I_{\text{rms}}=\frac{I_0}{\sqrt2}$ by integrating; the half-cycle average $2I_0/\pi$ vs the RMS (the classic confusion, with the "which one does a DC meter read?" note); RMS of non-sinusoidal waves (square, triangular, half-rectified) by the definition | RMS of a square and of a half-wave |
| 3 | AC through R, L, C | Each alone: derive the current's amplitude and phase relation (in phase; $I_0=V_0/\omega L$ with the current lagging; $I_0=V_0\omega C$ with the current leading); the reactances and their frequency dependences; the "why L blocks high frequency and C blocks low" physical explanation (inertia and spring pictures) | The 'CIVIL' current-leads-voltage mnemonic *derived*, not memorised |
| 4 | Phasors | The rotating-vector representation; why phasor addition is legitimate (same frequency, only amplitudes and phases differ); the phasor diagrams for R, L, C, RL, RC, LC | Draw the phasor diagram for an RC circuit |
| 5 | Series LCR | Build the phasor diagram, derive $Z=\sqrt{R^2+(X_L-X_C)^2}$ and $\tan\phi=\frac{X_L-X_C}{R}$; the impedance triangle; the "where does the source voltage appear?" checks ($V_R$, $V_L$, $V_C$ do not add algebraically); the amplitude and phase of the current | Series LCR's $Z$, $\phi$, $I_0$ for given values |
| 6 | Resonance | The $I(\omega)$ curve; the resonance condition $\omega_0=\frac{1}{\sqrt{LC}}$ (from the phasor diagram, not by assertion); the voltage magnification across $L$ and $C$ at resonance; the $Q$ factor defined two ways (bandwidth and energy ratio) and shown to agree; the bandwidth $\Delta\omega=R/L$; the practical uses and the danger | The resonance frequency and $Q$ for a real radio circuit |
| 7 | Power in AC | Derive $P_{\text{avg}}=V_{\text{rms}}I_{\text{rms}}\cos\phi$ by integrating the product; the power factor; the wattless current; the power triangle (real, reactive, apparent); the "why L and C consume no average power" energy-exchange picture; the "why the electricity board charges industry for a poor power factor" analysis | Power factor and the electricity-bill problem |
| 8 | Parallel AC circuits | The admittance approach; the parallel LC tank's anti-resonance (impedance maximum); the "currents in parallel branches do not add algebraically" trap; the general method (complex impedances) introduced as the *third* method after phasors and the triangle | Parallel LCR's impedance at resonance |
| 9 | The complex-impedance method | $Z=R+jX_L-jX_C$; the arithmetic of complex numbers as a time-saver; the magnitude/phase read-off; the caution that the physics is in the real part | A four-element network solved by both methods |
| 10 | Transformers | The ideal transformer's flux-linkage argument; the turns ratio for voltage and current; the power balance; the impedance reflection $Z_p=(N_p/N_s)^2Z_s$; the "why the primary current is set by the load"; the real transformer's losses (copper, eddy, hysteresis, flux leakage) with their physical origins (links PART 19 and PART 20); the high-voltage transmission argument with the $I^2R$ loss arithmetic | The transmission-loss problem: 11 kV vs 220 kV |
| 11 | Rectification and filters | The diode's role (link PART 27); half- and full-wave rectifiers with load and smoothing capacitor; derive the ripple voltage's $\approx\frac{I}{2fC}$ estimate; the "why a capacitor smooths" impedance picture; the transformer-rectifier-capacitor supply chain as a system | Ripple voltage and the required capacitor |
| 12 | LC oscillations and the road ahead | The LC circuit as a source of AC (link PART 21); the damped LCR's transient; the bridge to the shipped EM-waves note (a radiating oscillator) | The LC frequency and an estimate of the radiation's wavelength |

**Must be derived, not stated:** the RMS value; the three reactances with their phase relations; the
series LCR impedance and phase; the resonance frequency and the $Q$-factor equivalence; the average power
expression; the transformer's relations and impedance reflection; the ripple estimate; the LC frequency.

**DIAGRAM briefs (D22.1–D22.18):** the sinusoidal waveform with peak, RMS and the half-cycle average
marked on the same axes; the "same heating effect" comparison (a resistor heated by DC vs AC); the phasor
diagrams for R, L and C separately (three panels); the series LCR phasor diagram with the impedance
triangle; the $I(\omega)$ resonance curves for three values of $R$ with the bandwidth marked; the
voltage-magnification curve ($V_L/V$ vs $\omega$); the power triangle; the instantaneous power waveform
for a lagging load with the average line; the parallel LC tank's admittance picture; the transformer's
core with the flux, the turns and the load; the impedance-reflection diagram; the transmission-line
loss comparison for two voltages; the rectifier circuits (half-wave and full-wave) with the smoothing
capacitor and the ripple waveform; the diode's I–V curve with the knee (link PART 27); the LC
oscillator's charge/current/energy curves; the LCR transient; the "current leads/lags" summary chart;
the complex-impedance plane with a point marked.

**Mandatory archetypes:** RMS and peak conversions; the reactances at a given frequency; series LCR
impedance/phase/current; resonance frequency and $Q$; the voltage across L and C at resonance; the
power dissipated in a series LCR; the power factor correction; the parallel LC tank's resonance; a
transformer's secondary current given the load and the turns ratio; reflection of a load impedance;
the transmission-line loss; the rectifier's DC output and ripple; the average and RMS of a rectified
wave; the LC circuit's frequency and the maximum charge/current.

**Olympiad block content:** the full transient-plus-steady-state analysis of an AC circuit (solve the
differential equation, split the solution into the dying transient and the steady oscillation, and find
the time to reach steady state — the honest treatment that textbooks avoid); the derivation of the
average power $P=\frac12V_0I_0\cos\phi$ from the product of two sinusoids, with the identification of the
"reactive" part; the impedance-matching theorem for AC (maximum power transfer requires
$Z_{\text{load}}=Z_{\text{source}}^*$ — derived in complex form and interpreted physically); the
"why a square wave of the same RMS heats a resistor identically while the *peak* differs" verification by
direct integration (a beautiful exercise in the RMS definition); the harmonic decomposition's first
term (a square wave as the sum of odd harmonics, the "why a transformer's output is not a square wave"
observation); the three-phase supply's phasor sum (why the neutral carries no current when the load is
balanced — a phasor exercise with a real-world hook); the Wien bridge's balance condition derived
(the phase-shift oscillator, a favourite olympiad circuit); the power-factor-correction design problem
(a factory's load and the capacitor bank's size); the skin effect's order-of-magnitude (why a thick
conductor is useless at high frequency — link the shipped EM-waves note's conducting medium); the
"how long can a household supply a short-circuit current before the breaker trips?" estimate (the
inductive energy and the fault current's rise); the transmitter–receiver resonance problem
(an LC tank coupled by mutual inductance — the radio's tuning, using PART 21's $M$ and this chapter's
resonance together: the best synthesis problem in the block).

**Traps to plant:** mixing RMS and peak values in one formula; using $V_{\text{rms}}I_{\text{rms}}$ as
the power without the power factor; adding $V_R+V_L+V_C$ algebraically; assuming the current is the same
in parallel branches; treating the impedance as a resistance (ignoring the phase); forgetting that the
resonance frequency in a *parallel* circuit maximises the impedance, not the current; assuming a
transformer works on DC; forgetting the diode drop in a rectifier's DC output; believing a capacitor
"uses up" power.

**Exit criteria:** RMS is derived from the heating definition and contrasted with the half-cycle average;
the reactances and their phase relations are derived physically; the phasor method precedes the complex
method; resonance includes the voltage magnification and the $Q$-factor equivalence; the power section
derives the power factor; the transformer includes impedance reflection and the loss table; the
rectifier-with-ripple estimate is present; the Olympiad block contains the transient analysis, the
matching theorem and the Wien bridge.

---

---

## Block C · Modern Physics

> The shipped `geometrical-optics/` and `wave-optics/` notes already own the optics half of the Cengage
> volume, and `electromagnetic-waves/` owns light as a wave. This block closes the volume with the quantum
> half — **verified from the volume's own contents page**: Unit II is exactly ch 3 Photoelectric Effect,
> ch 4 Atomic Physics (which contains the X-ray sections that PART 25 claims) and ch 5 Nuclear Physics.
> There is **no semiconductors chapter** in these five volumes, and no relativity chapter anywhere, so
> PARTS 27 and 28 build their floors from the standard JEE/olympiad syllabus and say so in their coverage
> maps (§1.13).

### PART 23 · Photons, Photoelectric Effect & Matter Waves

`photoelectric-effect` · folder `photoelectric-effect/` · source: Cengage ***Optics and Modern
Physics* ch 3 Photoelectric Effect** (quantum theory of light, photon counts/flux/density, force and
radiation pressure of a light beam, matter waves, electron emission, photoelectric cell, Einstein's
equation, laws, failure of the wave theory) · needs PART 15 and the shipped `electromagnetic-waves/`
note · JEE Advanced ·
NSEP · INPhO · IPhO.
*The one idea:* light delivers its energy in indivisible quanta, and matter waves are the same fact seen
from the other side.

| # | Section | Teach this, in this order | Closes with |
|---:|---|---|---|
| 1 | The crisis before the quantum | Blackbody radiation and the ultraviolet catastrophe stated honestly (the classical prediction diverging, the measured curve peaking); Wien's displacement and Stefan's law as *scaling* results (link the shipped `heat/` note); Planck's quantum hypothesis as the fix; the "what was actually quantised in 1900?" question | The Wien-shift and $T^4$ estimates |
| 2 | The experimental facts of the photoelectric effect | The apparatus; the five facts (threshold below which nothing happens, instantaneous emission, current $\propto$ intensity, $K_{\max}$ depends on frequency not intensity, the stopping potential); each fact with the classical prediction it destroys — and the *quantitative* "how long would you have to wait classically?" estimate | The classical waiting-time estimate |
| 3 | The photon | $E=hf$; the photon's momentum $p=\frac{h}{\lambda}$ (stated as the relativistic massless relation, verified by experiment — the derivation belongs to PART 28, the *use* is here); intensity as photon flux; the photon's energy in eV as a function of wavelength (the "numbers to keep" table: 400 nm ≈ 3.1 eV, 1240 eV·nm rule) | Photon-number-per-second calculations |
| 4 | Einstein's equation | $K_{\max}=hf-\phi$; the work function; the threshold wavelength; the stopping potential; the $V_s$ vs $f$ graph's slope $\frac{h}{e}$ (the measurement of Planck's constant!) and the intercept's meaning; the "why the current saturates" and "why $K$ is a maximum" explanation (the depth of origin) | Read a $V_s$–$f$ graph to get $h$ and $\phi$ |
| 5 | Current, intensity and frequency as independent knobs | The three-parameter behaviour table; the "increase the intensity, get more current at the same stopping potential" experiment; the "why the classical wave model gets the current right and everything else wrong" summary | The two-intensity curve comparison |
| 6 | de Broglie's hypothesis | $\lambda=\frac{h}{p}$ from the photon's symmetry argument; the electron's wavelength in terms of accelerating voltage (derive $\lambda=\frac{1.226\,\text{nm}}{\sqrt{V}}$); the thermal/de Broglie comparison for gases; the "why we do not see a cricket ball's waves" order-of-magnitude | Compute $\lambda$ for three accelerating voltages |
| 7 | The Bohr orbit as a standing wave | Impose $2\pi r=n\lambda$ with de Broglie's $\lambda$ and *derive* the angular-momentum quantisation $L=n\hbar$ (the "where the magic postulate comes from" bridge to PART 24) | The standing-wave condition derived |
| 8 | Davisson–Germer and electron diffraction | The experiment's geometry and the diffraction condition; why it was decisive; the double-slit with electrons; the neutron and atom interferometry previews; the "what happens if you measure which slit?" honest flag (the interpretation is beyond this chapter — say where it is studied) | The nickel crystal spacing from the diffraction angles |
| 9 | The uncertainty principle | The statement $\Delta x\Delta p\gtrsim\hbar/2$; its derivation via the wave packet ("a wave of extent $\Delta x$ needs a spread $\Delta k\sim1/\Delta x$" — the honest argument); the applications: the minimum energy of a confined particle, why the electron does not fall into the nucleus, why the hydrogen atom has the size it has (the order-of-magnitude derivation of $a_0$ and $-13.6$ eV), the natural linewidth of a spectral line | Derive the hydrogen radius and energy from uncertainty |
| 10 | Which model, when? | The decision table (energy exchange → photon; propagation and interference → wave; localisation → uncertainty-limited packet); the Einstein–de Broglie symmetry statement; the classical limit's appearance ($\lambda\ll$ the geometry) | Three scenarios to classify |
| 11 | Matter waves in instruments | The electron microscope's resolution argument (and why it beats light); LEED's surface sensitivity (slow electrons have *longer* wavelengths — the counter-intuitive fact stated carefully); the diffraction of atoms in a real experiment | The microscope resolution comparison |
| 12 | Where the photon picture pays | Photoelectric spectroscopy, the photovoltaic effect's threshold (link PART 27), the photographic process (one photon per grain), the photomultiplier, the laser's stimulated emission (a one-page mention with the population-inversion idea) | A photovoltaic threshold calculation |

**Must be derived, not stated:** the classical waiting-time estimate; the $V_s$-vs-$f$ slope's meaning;
$\lambda=\frac{h}{p}$'s consequences for an accelerated electron; the standing-wave route to $L=n\hbar$;
the uncertainty-principle derivation of the hydrogen radius and energy; the electron microscope's
resolution advantage.

**DIAGRAM briefs (D23.1–D23.16):** the blackbody spectrum family with the Wien shift and the classical
curve's divergence marked; the photoelectric apparatus with the variable stopping voltage; the
photocurrent vs voltage curves for two intensities at one frequency (and one frequency below threshold);
the $K_{\max}$ vs $f$ lines for two different metals with the slope $\frac{h}{e}$ marked; the photon
energy–wavelength conversion chart with the visible band highlighted; the "one photon ejects one electron"
bookkeeping picture; the de Broglie standing wave around a circular Bohr orbit with $n=3$ drawn; the
Davisson–Germer apparatus with the crystal planes and the diffraction angle; the electron double-slit
build-up (dots accumulating into fringes); the wave packet with the $\Delta x$ and the wavelength spread;
the confined-particle-in-a-box energy sketch; the hydrogen atom's size from the uncertainty estimate
(the electron's momentum spread vs its Coulomb well); the electron microscope's lens geometry with the
wavelength comparison; the LEED pattern; the photomultiplier's dynode chain; the laser's three-level
pumping scheme.

**Mandatory archetypes:** photon energy from wavelength and vice versa; the number of photons per second
from a power; the stopping potential for a given metal and wavelength; the threshold wavelength; the
maximum kinetic energy and speed of the photoelectron; the work function from a graph; the electron's
de Broglie wavelength at a given voltage; the momentum of a photon and the force of a light beam
(link the shipped EM-waves note); the standing-wave condition in an orbit; the minimum energy from
uncertainty in a box; the diffraction angle for electrons from a grating-like crystal.

**Olympiad block content:** the classical wave model's quantitative failure (compute the time to
accumulate one electron's worth of energy at a realistic intensity — the answer of the order of
minutes to hours destroys the wave picture, and the experiment shows nanoseconds: the most convincing
single calculation in the chapter); the Duane–Hunt-limit preview (the inverse photoelectric effect,
where a photon's maximum frequency comes from a decelerating electron — link PART 25); the derivation of
the de Broglie relation from the photon's momentum and the relativistic Doppler shift (with the honest
"why the phase velocity of a matter wave exceeds $c$ while the group velocity does not" box — a stunning
olympiad insight, derived from $v_{\text{phase}}=\frac{\omega}{k}=\frac{c^2}{v_{\text{particle}}}$);
the group velocity $v_g=\frac{d\omega}{dk}=v_{\text{particle}}$ derived explicitly and identified with the
classical particle velocity; the uncertainty principle's role in the natural linewidth
($\Delta E\Delta t\sim\hbar$ → $\Delta\lambda$) with a real spectral line's width; the minimum-energy
estimate for a particle in a Coulomb well derived by balancing the kinetic and potential terms
(the "how does the uncertainty principle generate the Bohr radius?" derivation, which then yields the
Rydberg energy without postulates — the intellectual high point of the chapter); the photoelectric
effect's two-photon variant and the "why a low-intensity pulsed laser can still emit" statement; the
"how bright must a light be to see single photons?" estimate (the eye's sensitivity, the real number
of ~100 photons); the laser's Einstein-coefficient argument (why stimulated emission wins above a
threshold — the population inversion and the Boltzmann factor's role) with an order-of-magnitude;
the electron's diffraction through a thin film and the "which potential should I use for
$\lambda$?" question (accelerating voltage vs total energy, with the relativistic correction's size).

**Traps to plant:** using $\lambda=\frac{h}{p}$ with the non-relativistic momentum at high energies
without checking (say when the correction exceeds 1 %); mixing the work function's units (eV vs J);
thinking the stopping potential depends on intensity; using $hf$ for the *maximum* kinetic energy without
subtracting $\phi$; confusing the threshold frequency with the stopping potential's zero; using
$\Delta x\Delta p\ge\hbar/2$ with $\hbar$ vs $h$ (and the $2\pi$'s origin); assuming the electron's
wavelength decreases with *lower* energy (the LEED trap); treating the photocurrent's saturation as a
quantum effect (it is geometrical).

**Exit criteria:** the five experimental facts are each paired with the classical failure; the $h/e$
measurement is presented as a graph-reading skill; the Bohr-orbit standing-wave bridge is derived; the
uncertainty principle is derived from the wave packet, not asserted, and used to derive $a_0$; the
"which model when" table is present; the Olympiad block contains the classical waiting-time calculation
and the phase/group velocity discussion.

---

### PART 24 · Rutherford, the Bohr Model & Atomic Spectra

`atomic-structure` · folder `atomic-structure/` · source: Cengage ***Optics and Modern Physics* ch 4
Atomic Physics** — Thomson model, Bohr model (radius, velocity, frequency, energy of the $n$th orbit),
hydrogen-like atoms, ionisation and excitation potentials, limitations of the Bohr model, hydrogen
spectrum and origin of spectra, effect of nuclear mass, atomic collision — the X-ray half of the same
chapter is PART 25's · needs PART 23 · JEE Advanced · NSEP · INPhO · IPhO.
*The one idea:* atoms have discrete levels because an electron is a standing wave, not a planet.

| # | Section | Teach this, in this order | Closes with |
|---:|---|---|---|
| 1 | The atom before 1911 | Thomson's plum-pudding model and what it predicted; the alpha-scattering experiment's setup and the "what would you expect if the positive charge were spread out?" prediction; the observation's shock (large-angle back-scattering) | Predict the Thomson result before seeing the data |
| 2 | Rutherford scattering | The trajectory in a $1/r^2$ force field: the impact parameter, the scattering angle's relation, the distance of closest approach $r_{\min}=\frac{2kZe^2}{m v^2}$ (derived by energy conservation), the nuclear-size estimate from the fastest alphas; the "how big is the nucleus compared with the atom?" ratio | The $r_{\min}$ calculation for a real alpha |
| 3 | The classical collapse | Why a radiating electron spirals in: the energy-loss rate (Larmor form stated) and the "how long does an atom last?" estimate ($\sim10^{-11}$ s); the two killer facts: collapse and the discrete line spectrum | The classical-lifetime estimate |
| 4 | Bohr's postulates | (i) stationary orbits, (ii) no radiation in them, (iii) $hf=E_i-E_f$ on transition; the honest "these are postulates, but they came from a standing-wave condition and the spectrum" framing; the connection to PART 23's standing-wave derivation | State the postulates in the student's own words |
| 5 | Consequences for hydrogen | Derive $r_n=n^2a_0$; $v_n=\frac{v_1}{n}$; $E_n=-\frac{13.6}{n^2}$ eV; the ionisation energy; the "why is the kinetic energy half the magnitude of the potential energy?" (the consistency check); the speed's comparison with $c$ and the model's limit | The first four radii and energies |
| 6 | The spectrum | The Rydberg formula for hydrogenic atoms; derive $R$ from Bohr's model and compare with the spectroscopic value; the series (Lyman, Balmer, Paschen, Brackett, Pfund) with their wavelength regions; the number of lines from a level ($\frac{n(n-1)}{2}$); maximum/minimum wavelengths | Compute three Balmer lines |
| 7 | Transitions and excitation | Photon vs electron excitation (the "11 eV electron can excite what a 10.2 eV photon cannot" logic); ionisation vs excitation; the Franck–Hertz experiment's discrete dips; the Boltzmann-factor reason the ground state dominates at room temperature | The excitation-energy problem set |
| 8 | Hydrogen-like ions and exotic atoms | $Z^2$ scaling (He⁺, Li²⁺); the reduced-mass correction and the H/D isotope shift (the discovery of deuterium!); muonic hydrogen and positronium as scaling exercises; the "why the finite nuclear mass matters" argument | The isotope-shift calculation |
| 9 | X-ray lines from the same picture | The inner-shell vacancy and the characteristic lines (the full treatment is PART 25); Moseley's law as a Bohr-model corollary with a shielding constant; the "why the Kα line's frequency is much higher than an optical line's" | Moseley's law applied |
| 10 | Fine structure and the quantum numbers | The honest limits of Bohr: the Zeeman splitting derived (the magnetic moment of the orbiting electron, $\mu_B$), the fine structure's existence and size, the Stern–Gerlach idea, and the introduction of $n$, $l$, $m_l$, $m_s$ with the selection rule $\Delta l=\pm1$; the correspondence principle as the bridge to classical behaviour at large $n$ | The Zeeman splitting in a 1 T field |
| 11 | Where the model is used today | Spectroscopic identification (astrophysics), the 21 cm line's origin (one paragraph), the isotope-shift method, the ionisation-potential measurement, the "why emission spectra identify elements" argument | Identify an element from three lines |
| 12 | Reading the numbers | The "numbers to keep" table: $a_0$, the Rydberg constant, 13.6 eV, $\mu_B$, $\hbar$; the habit of quoting energies in eV and wavelengths in nm | Quick-fire conversions |

**Must be derived, not stated:** the scattering angle's impact-parameter relation; $r_{\min}$; the
classical collapse time; all four hydrogen results ($r_n$, $v_n$, $E_n$, $R$); the ionisation energy; the
line-count formula; the $Z^2$ scaling; the reduced-mass correction; Moseley's law from the Bohr picture;
the Zeeman splitting; the correspondence-principle limit.

**DIAGRAM briefs (D24.1–D24.16):** Thomson vs Rutherford predictions with the alpha paths drawn;
the scattering geometry with the impact parameter, the hyperbola and the angle; the "one in 8000 bounces
back" data table visualized; the $r_{\min}$ vs alpha-energy curve; the classical spiral-in with the
emitted spectrum's continuum; the Bohr orbits with $n=1,2,3$ and the radii drawn to scale; the hydrogen
energy-level ladder with the Lyman/Balmer/Paschen series drawn as arrows on different colours (described
in words); the spectrum's line positions for hydrogen with the visible lines marked; the Franck–Hertz
curve with the periodic dips; the $R$ prediction vs the measured value table; the He⁺ / Li²⁺ scaled
level diagram; the isotope-shift of the Hα line; Moseley's √f vs Z straight line; the Zeeman splitting
of a level in a field; the correspondence-principle illustration (the $n\to\infty$ orbit's classical
limit); the emission-vs-absorption spectrum comparison.

**Mandatory archetypes:** the closest-approach distance for an alpha of given energy; the alpha's kinetic
energy at the closest approach; the energies and radii of the first three levels; the photon wavelength
for a given transition; the ionisation energy of a hydrogen-like ion; the number of spectral lines from an
excited level; the excitation-energy problem with an electron beam; the maximum and minimum wavelengths
of a series; the Rydberg constant from the model; the Zeeman splitting; the reduced-mass correction for
deuterium.

**Olympiad block content:** the Rutherford differential cross-section's $1/\sin^4(\theta/2)$ law (derive
the impact-parameter relation in full, compute $b(\theta)$, then show which angles are common — the
classic olympiad long problem, with the "why almost all alphas go nearly straight through" arithmetic);
the "why the experiment proves the nucleus is tiny and the force is Coulomb up to a scale" argument
(compute the deviation expected if the exponent were not 2, and the energy at which the nuclear force
takes over, from the deviation angle); the Bohr model derived *without postulates* (from de Broglie's
standing wave plus the centripetal Coulomb force: a two-equation derivation that yields everything —
the pedagogical peak of the chapter); the correspondence-principle derivation that the frequency of the
radiation at large $n$ equals the orbital frequency (a gorgeous olympiad calculation: expand $\Delta E$
in powers of $1/n$); the "why the classical atom's collapse time is about $10^{-11}$ s and how
$10^{-11}$ s × $c$ compares with the atom's size" reality check; the muonic-hydrogen / positronium
scaling problems with the mass ratio's physical origin; the spectral line's natural width from the
finite lifetime (link PART 23's uncertainty and PART 25's linewidth); the "how hot must a star be to show
Balmer lines?" estimate (the Boltzmann factor for the $n=2$ population, with a real stellar-temperature
answer); the Rydberg constant's extraction from a real measured line list (a data-analysis exercise that
uses PART 1's fitting discipline); the "why helium's spectrum has two line systems" (the singlet/triplet
idea, stated as the doorway to spin — beyond the syllabus but named); the 21 cm line's order-of-magnitude
(the hyperfine splitting, why it is so important in radio astronomy); the "how small a wavelength shift
can a spectrometer see?" practical question, and the Doppler method it enables (link PART 28).

**Traps to plant:** using $r_{\min}$ as the nucleus's actual radius (it is an upper bound only for the
head-on case); forgetting the $Z$ in hydrogenic formulas; using the electron's mass in a muonic-atom
problem; treating the Bohr model as a valid theory for multi-electron atoms; using
$E_n=-13.6/n^2$ eV for anything but hydrogen (and its hydrogen-like ions); getting the series names
backwards; assuming the photon's energy equals the level spacing for *ionisation* problems (the free
electron's kinetic energy takes the remainder); confusing excitation energy with ionisation energy;
forgetting the reduced-mass correction when asked about an isotope shift.

**Exit criteria:** the experiment is framed as a hypothesis test (Thomson vs Rutherford); $r_{\min}$ and
the classical collapse are derived with numbers; all four hydrogen results are derived; the standing-wave
derivation of the postulates appears (either here or as a clearly cross-linked block); the spectrum
section includes the line-count formula and the region table; the limits of the model are listed with the
quantum numbers introduced; the Olympiad block contains the scattering cross-section and the
correspondence-principle derivations.

---

---

### PART 25 · X-rays, Moseley's Law, Bragg Diffraction & the Compton Effect

`x-rays` · folder `x-rays/` · source: Cengage ***Optics and Modern Physics* ch 4 Atomic Physics,
pp. 4.25–4.32** (X-rays: discovery, Coolidge tube, properties, applications, absorption, spectra and
their origin, Moseley's law) — the chapter is shared with PART 24, so key the coverage map to these
section names · needs PART 24 · JEE Advanced · NSEP · INPhO · IPhO.
*The one idea:* X-rays are photon physics with enough energy to see atoms and to knock electrons free —
and they prove that the photon carries momentum.

| # | Section | Teach this, in this order | Closes with |
|---:|---|---|---|
| 1 | Making X-rays | The Coolidge tube: thermionic emission, the accelerating voltage, the target, the vacuum and the window; why heavy targets and why rotating anodes; the production efficiency's estimate ($\sim1\%$ — the rest is heat); the "how many X-ray photons per second?" calculation | Tube-efficiency estimate |
| 2 | The continuous spectrum | Bremsstrahlung's origin (deceleration in the nuclear field); the Duane–Hunt cutoff $\lambda_{\min}=\frac{hc}{eV}$ (derived from the photon picture, and used as a *measurement of $h/e$*); the shape's dependence on voltage and target; why there is a sharp short-wavelength end but no sharp long-wavelength end | $\lambda_{\min}$ for three tube voltages |
| 3 | The characteristic spectrum | Inner-shell vacancy and the cascade; the Kα/Kβ, Lα notation; the sharp lines and their element-specificity; the threshold voltage for producing a given line (the "why the characteristic lines vanish below some voltage" logic — an excellent exam trap) | The minimum voltage for a given Kα line |
| 4 | Moseley's law | $\sqrt{f}=a(Z-b)$ derived from the Bohr picture with the shielding constant; the $b\approx1$ for Kα argument; the periodic-table ordering consequence; identifying an unknown element from its lines | Identify an element from two lines |
| 5 | Absorption and imaging | The exponential absorption law $I=I_0e^{-\mu x}$; the half-value thickness; the mass-attenuation coefficient; why bone/contrast media absorb more; the "why soft X-rays image better but dose more" trade-off; computed tomography in one paragraph | Half-value thickness calculation |
| 6 | X-ray diffraction: why crystals | The need for a grating whose spacing is comparable to $\lambda$ (the link back to PART 23's electron wavelength and forward to the shipped wave-optics note's grating); the crystal as a 3-D grating; the Laue condition preview | Why visible light cannot use a crystal grating |
| 7 | Bragg's law | The two-ray derivation $2d\sin\theta=n\lambda$ (geometry drawn carefully, including that $\theta$ is measured from the *plane*, not the normal); the orders; the missing orders and the "which planes are involved?" idea; the powder photograph's rings | A spacing calculation from two orders |
| 8 | X-ray diffraction in practice | Determining the lattice constant; determining Avogadro's number from the density and the unit cell (a classic olympiad calculation!); the rotation-crystal method; the structure-factor idea's first appearance (why some reflections are absent — stated with the "atoms at different sites interfere" picture) | Avogadro from a crystal |
| 9 | The Compton effect: the experiment | The observations (a shifted line and an unshifted line; the shift depends only on $\theta$); the classical prediction's failure; the "which line is which" (the unshifted one comes from tightly bound electrons) | Reading a Compton spectrum |
| 10 | Compton's derivation | Energy and momentum conservation with $E=hf$ and $p=\frac{h}{\lambda}$: derive $\Delta\lambda=\frac{h}{m_ec}(1-\cos\theta)$; the Compton wavelength 2.43 pm; the electron's recoil kinetic energy and angle from the momentum triangle; the extremes at $\theta=0,90^\circ,180^\circ$ | The shift and the electron's energy at 90° |
| 11 | Why it matters | The shift's size for visible light (order of magnitude: $10^{-5}$) and hence why X-rays are needed; the photon's momentum as the decisive evidence; the inverse Compton effect and astrophysical applications (a one-paragraph mention); the pair-production threshold preview ($2m_ec^2=1.02$ MeV, link PART 28) | The visible-light shift estimate |
| 12 | Cross-topic synthesis | Photoelectric (photon energy) + Compton (photon momentum) + diffraction (photon interference) = the complete photon; the "which experiment proves what" table; the electromagnetic spectrum's high-energy end (link the shipped EM-waves note) | The three-experiment summary table |

**Must be derived, not stated:** the Duane–Hunt limit; Moseley's law from the Bohr model; the
Bragg condition; the Avogadro-from-crystal result; the Compton shift; the electron's recoil angle and
energy; the visible-light shift estimate; the pair-production threshold.

**DIAGRAM briefs (D25.1–D25.16):** the X-ray tube in section with the filament, target, window and
cooling; the continuous spectrum at three voltages with the cutoff marked and the envelope noted; the
characteristic lines on top of the continuous spectrum with Kα/Kβ labelled; the $K$-shell vacancy and
cascade drawn on an energy-level diagram; the Moseley line ($\sqrt f$ vs $Z$) with two elements'
positions; the absorption curve with the half-value thickness drawn; a radiograph's differential
absorption described; the crystal planes with the two parallel rays and the extra path $2d\sin\theta$
drawn (with the angle's definition highlighted); the powder-photograph rings and their relation to the
planes; the unit cell with the atoms and the spacing $d$; the Compton scattering geometry with the
incoming and outgoing photon and the recoiling electron; the momentum triangle with $\theta$ and the
electron's angle $\phi$; the $\Delta\lambda$ vs $\theta$ curve with the values at 90° and 180° marked; the
measured Compton spectrum with the shifted and unshifted peaks; the "photon energy scale" from radio to
gamma with the three experiments' regions highlighted; the pair-production threshold's Feynman-style
diagram (described in words, no symbols to reproduce).

**Mandatory archetypes:** the minimum wavelength for a given tube voltage; the maximum photon energy;
the minimum voltage to produce a Kα line; the Kα frequency from Moseley's law; identifying the element
from a spectrum; the absorption through a thickness and the half-value layer; the Bragg angle for a given
spacing and order; the number of orders visible; the lattice spacing from the density and the unit cell;
Avogadro's number from the crystal data; the Compton shift at a given angle; the electron's recoil energy
and angle; the maximum shift; the "why there are two peaks" question; the pair-production threshold.

**Olympiad block content:** the full Compton derivation *twice*: once with scalar conservation
(algebraic, using $\cos\theta$ and the electron's recoil angle) and once with the momentum triangle/four-
vector invariant (the elegant route that also gives the electron's energy directly) — comparing the two is
the point; the maximum electron kinetic energy at $\theta=180^\circ$ and the "why the energy cannot all
go to the electron" reasoning; the inverse Compton effect derived by the "elastic bounce off a light
mirror" analogy (a photon reflecting off a moving electron gains energy — the same velocity-triangle
logic as PART 7's gravity assist: an explicit cross-topic link); the Moseley shielding constant estimated
from a shell-model argument, with the real measured offset for $K\alpha$; the "Duane–Hunt limit as the
most accurate early measurement of $h/e$" data exercise; the microscopic justification of the
$1\sin^4$ Compton-corrected X-ray absorption (a one-paragraph discussion, no derivation) with the
"why increasing the wavelength of the emitted line requires increasing the excitation" check; the
determination of Avogadro's number from a real NaCl/debye density and the modern value's agreement (a
genuine measurement-reconstruction problem); the "how much power does an X-ray tube deposit in the
anode?" engineering estimate with the required rotating-anode heat capacity and the cooling design; the
"safety" calculation (the dose in a dental X-ray versus a cosmic-ray flight — an order-of-magnitude with
the absorbed-dose unit defined); the X-ray laser/free-electron-laser idea mentioned with the
"why it is hard" argument; the "why the sky is blue" (Rayleigh's $\lambda^{-4}$) as the *low-energy*
contrast to this chapter's high-energy scattering, computed for two wavelengths and used to explain both
the blue sky and the red sunset.

**Traps to plant:** using $\lambda_{\min}=\frac{hc}{eV}$ for the *characteristic* line (it is only the
continuous limit); forgetting the factor $e$ in eV conversions; confusing $\theta$ in Bragg's law with the
grazing angle (it is the *grazing* angle actually — the "angle with the plane" IS the grazing angle, so
emphasise that it is not the angle with the normal); using the wrong $n$ for a "second-order" reflection;
applying $\Delta\lambda$ as a fractional change; forgetting that the unshifted peak is from bound
electrons; using the classical wave picture to "explain" Compton (it cannot produce a shift at a single
angle with a definite value); mixing the photon's energy and momentum units.

**Exit criteria:** the tube, the continuous and characteristic spectra are all explained with the
underlying mechanism; Moseley's law is derived, not quoted; Bragg's law is derived with the angle
convention made foolproof; Compton is derived twice and limit-checked ($\theta\to0$); the absorption and
imaging application is present; the Olympiad block contains the Avogadro determination, the
inverse-Compton analogy and the depth-of-scattering discussion.

---

### PART 26 · Nuclear Structure, Radioactivity, Fission & Fusion

`nuclear-physics` · folder `nuclear-physics/` · source: Cengage ***Optics and Modern Physics* ch 5
Nuclear Physics** (nuclear structure, size, binding energy, mass defect, $Q$ values, stability,
α/β/γ radioactivity, decay law, activity, half-life, average life, dating, decay series and equilibrium,
nuclear reactions and their kinematics, fission, reactors, fusion including fusion in the Sun) · needs
PART 24 · JEE Advanced · NSEP · INPhO · IPhO.
*The one idea:* nuclei are bound by a short-range saturated force, and the binding-energy curve decides
which way the energy flows.

| # | Section | Teach this, in this order | Closes with |
|---:|---|---|---|
| 1 | Inside the nucleus | Protons, neutrons, the isotopes/isobars/isotones bookkeeping; the four fundamental interactions named with their ranges and relative strengths; the "why does the nucleus stick together at all?" question; the strong force's five properties (attractive, short-range, charge-independent, saturating, spin-dependent at short range) | The forces table filled in by the reader |
| 2 | Size and density | $R=R_0A^{1/3}$ and its interpretation (constant density); the density calculation and the "a teaspoon weighs a billion tonnes" estimate; the "why every nucleus has the same density" insight; the evidence (alpha scattering, electron scattering, muonic atoms) | Nuclear density and the teaspoon estimate |
| 3 | Mass defect and binding energy | The atomic mass unit and the conversion triangle ($1\,\text{u}=931.5$ MeV); the mass defect's meaning; the binding energy of the deuteron and of helium; the binding-energy-per-nucleon curve with its peak at the Fe/Ni region; the two consequences (fission releases energy for heavy nuclei, fusion for light ones); why iron is the end of stellar burning | The binding-energy calculation for He-4 |
| 4 | The semi-empirical mass formula | The five terms (volume, surface, Coulomb, asymmetry, pairing) named with their physical origins and their $A,Z$ dependence; the "why each term has that power" explanation; using the formula to find the most stable $Z$ for a given $A$ (the beta-stability valley) and to predict which isobar decays | The stability-valley calculation |
| 5 | Radioactivity's zoo | Alpha (a helium nucleus), beta (electron/positron/EC), gamma (a photon): the nature, charge, mass, penetration; the $\Delta A$, $\Delta Z$ bookkeeping table; the decay chains; the "why is there no stable nucleus beyond bismuth?" argument (Coulomb vs surface energy) | Balance three decay equations |
| 6 | Alpha decay | Why an alpha and not a proton/neutron (the binding-energy argument!); the $Q$-value; the energy split between the alpha and the daughter by momentum conservation: $K_\alpha=\frac{A-4}{A}Q$ (derived); the discrete alpha energies and the "why the spectrum is a line" point | The alpha/daughter energy split |
| 7 | Beta decay and the neutrino | The continuous beta spectrum and the "where does the missing energy go?" crisis; the neutrino's prediction from conservation laws alone; the endpoint energy; the positron/EC variants; the "why a free neutron decays but a bound one may not" question (the mass comparison) | The endpoint-energy argument |
| 8 | Gamma emission | De-excitation, the discrete energies, the internal conversion mention; the isomer idea; the "why gamma has no $\Delta A$" bookkeeping | Gamma-energy calculation from a level scheme |
| 9 | The decay law | Derive $N=N_0e^{-\lambda t}$ from the statistical assumption (no memory, constant probability per unit time); the activity $A=\lambda N$; the half-life and mean life with the mean-life integral (mean life $=\frac{1}{\lambda}=\frac{T_{1/2}}{\ln2}$); the log-plot linearisation; the "why the decay constant is unaffected by temperature, pressure and chemistry" and how you would test it | Half-life and mean-life problems |
| 10 | Decay chains and equilibrium | The two-step chain's solution; transient vs secular equilibrium (with the ratio of activities derived); the "which parent's half-life dominates the long-term behaviour" rule; the activity's maximum in the daughter | The chain's activity vs time; the equilibrium activity ratio |
| 11 | Dating and tracing | Carbon dating (derive the age formula, state the assumptions, give the range's limits and the calibration-curve reason); potassium-argon and uranium-lead dating; the isochron idea; medical tracers' activity and dose; the smoke detector; the "why radon is a hazard" (the gas + the alpha + the half-life chain) | A carbon-dating calculation with its uncertainty |
| 12 | Fission | The process; the energy per fission (~200 MeV) and its comparison with a chemical reaction (a factor of $10^7$); the chain reaction and the multiplication factor $k$; the critical mass's dependence on shape and enrichment; the moderator's role (slowing neutrons — why fast neutrons are less effective); the reactor's components (moderator, control rods, coolant, shielding, containment); the "why a reactor cannot explode like a bomb" design distinction | The energy from a gram of U-235 |
| 13 | Fusion | The Coulomb barrier and the required temperature (derive the order of magnitude); the proton–proton chain and the CNO cycle (the reactions and the net 26.7 MeV per helium); the Lawson criterion stated; why fusion is hard (temperature, confinement, neutron damage); the Sun's power budget (the mass-loss rate per second from the luminosity) | The Sun's mass loss per second |
| 14 | Detectors and statistics | The cloud chamber's tracks (why alphas leave short fat tracks and betas thin coiled ones); the Geiger counter's deadtime idea; the statistics of counting ($\sqrt N$) and its consequences for measurement time (link PART 1) | The counting-time problem |

**Must be derived, not stated:** the constant-density argument from $R\propto A^{1/3}$; the binding-energy
curve's consequences (both directions); the energy share $K_\alpha=\frac{A-4}{A}Q$; the exponential decay
law and the mean-life integral; the transient equilibrium's activity ratio; the carbon-dating formula;
the fission energy per nucleon's gain; the Coulomb-barrier temperature; the Sun's mass-loss rate; the
$\sqrt N$ counting statistics.

**DIAGRAM briefs (D26.1–D26.18):** the nucleus's force-balance picture (Coulomb repulsion vs the strong
attraction's range); the $R$ vs $A^{1/3}$ straight line with real data points; the binding-energy-per-
nucleon curve with fusion and fission arrows and the Fe/Ni peak; the mass-defect arithmetic on a
balance-beam cartoon; the semi-empirical formula's five terms as a bar chart for one nucleus; the valley
of stability with the beta-decay directions drawn; the three decay types with their penetration and
deflection behaviour; the alpha decay's energy-level diagram and the momentum split; the beta spectrum
with the average and endpoint energies and the neutrino's share shaded; a decay chain's nuclide chart
path; the exponential decay curve with the half-life marked and the log-linear plot beside it; the
two-step chain's activities vs time in the two equilibrium regimes; the carbon-dating curve with the
range limits and the calibration caveat; the fission chain reaction's generations drawn with $k>1$,
$k=1$, $k<1$ panels; the reactor's component stack; the Coulomb barrier with a tunnelling sketch and
the Gamow peak; the p–p chain's reaction ladder; the cloud chamber's three track types.

**Mandatory archetypes:** the binding energy from the mass defect; the most stable isobar for a given
$A$; the $Q$-value of a decay; the alpha/daughter energy split; the activity after three half-lives;
the age from an activity ratio; the mass of a radioactive sample from its activity; the half-life from a
log-plot; the equilibrium activity ratio; the energy released per fission and per gram; the number of
fissions per second in a reactor; the Sun's mass-loss rate; the Coulomb-barrier energy for two nuclei;
the count-rate standard deviation and the measurement time.

**Olympiad block content:** the Coulomb barrier and the Gamow factor's qualitative argument, then the
**Geiger–Nuttall law**'s form ($\log\lambda \propto -b/\sqrt{E}$) and the "why a small change in the
alpha's energy changes the half-life by a factor of $10^{20}$" analysis — the most spectacular
order-of-magnitude result in the chapter, derived by a one-dimensional tunnelling estimate; the
fission barrier's origin (the competition between the surface energy that resists deformation and the
Coulomb energy that drives it), the fissility parameter $\frac{Z^2}{A}$ and the "why $^{235}$U fissions
with slow neutrons while $^{238}$U prefers to capture" analysis; the spontaneous-fission estimate from
the barrier's height; the derived solar core temperature from the Gamow peak and the "why the Sun's
centre is 15 MK rather than the 10⁷ K a naive Coulomb calculation gives" correction (the tunnelling
exponential in the reaction rate — an honest, deep olympiad-level argument); the neutrino's flux at the
Earth and the "how many solar neutrinos pass through your thumb per second?" estimate (the classic
Kamiokande-style Fermi problem, with the real number $\sim10^{15}\,\text{m}^{-2}\text{s}^{-1}$); the
"how much uranium must a reactor burn per day per gigawatt?" calculation with the real number
(~3 kg/day of U-235); the "how long does a radioactive waste isotope need to be stored?" problem
(10 half-lives rule); the decay chain's transient-equilibrium derivation in full; the "how do you date
a rock with two isotopes?" isochron method; the nuclear-density consistency check "what is the mean
nucleon spacing, and how does it compare with the de Broglie wavelength of a thermal neutron?"
(the answer explains why slow neutrons diffract from crystals — a beautiful cross-topic link to PART 23
and PART 25); the mass–energy audit of the p–p chain (four protons in, one helium plus two
positrons and two neutrinos out — verify 26.7 MeV from the masses); the "how long can the Sun last?"
estimate from the hydrogen mass fraction; the "what limits the size of a nucleus?" argument (the
competition between the surface and Coulomb terms, giving the maximum $Z\approx100$).

**Traps to plant:** adding the *atomic* masses without accounting for the electron masses in a beta
decay's $Q$-value; forgetting the neutrino's energy share; using $N=N_0e^{-t/T_{1/2}}$ (needs $\ln2$);
confusing activity with the number of nuclei; assuming the decay constant changes with the amount of
sample (intensive vs extensive confusion); using the mass number's change in beta decay ($\Delta A=0$);
mixing the half-life and mean-life; thinking the moderator "absorbs" the neutrons (it slows them);
assuming a reactor can be made to explode like a nuclear bomb; treating the Sun's fusion as a single
reaction rather than a chain; using the classical "roll over the barrier" temperature instead of the
tunnelling one.

**Exit criteria:** the strong force's properties are explained before the binding curve is used; the
binding-energy curve is read as a *decision-maker* for fission/fusion; alpha, beta (with the neutrino
argument) and gamma decays are each derived; the decay law is derived from a statistical assumption; the
chain and equilibrium analysis is present; dating has its assumptions stated; fission and fusion both
have real numbers; the Olympiad block contains the tunnelling/Geiger–Nuttall analysis and the solar
neutrino estimate.

---

### PART 27 · Semiconductors & Electronic Devices

`semiconductors` · folder `semiconductors/` · source: **no semiconductor chapter exists in the supplied
Cengage volumes** (verified: the *Optics and Modern Physics* volume's Unit II holds only chs 3–5). The
floor is the standard JEE Main/Advanced semiconductor syllabus, and the coverage map must be built from
that syllabus — after grepping the other four PDFs in case a chapter turns up there (§1.13) · needs the
shipped `current-electricity/` note and PART 18 · JEE Advanced · NSEP (JEE Main
weight is high; keep the olympiad layer about real device physics).
*The one idea:* bands and doping turn a poor conductor into a controllable one — the whole of
electronics in two ideas.

| # | Section | Teach this, in this order | Closes with |
|---:|---|---|---|
| 1 | The three classes of conduction | The resistivity range ($10^{30}$!) of insulators, semiconductors and conductors *on one logarithmic axis*; why metals' resistance rises with temperature while a semiconductor's falls (two different mechanisms — the "which scattering mechanism wins" table); the "why is silicon not a metal?" question | The resistivity-comparison reading |
| 2 | Bands in words and in one picture | The band picture (allowed bands, forbidden gaps) with the "why a filled band cannot conduct" argument; the gap sizes for diamond, Si, Ge, GaAs; the electron's effective-mass idea; the "why an insulator is just a semiconductor with a bigger gap" statement | Rank four materials by gap |
| 3 | Intrinsic semiconductors | Thermal generation of electron–hole pairs; the hole as a *real* mobile positive carrier (and why it is not a "missing electron" only in words); recombination; the strong temperature dependence $n_i\propto T^{3/2}e^{-E_g/2kT}$ (stated and used qualitatively); the pure-silicon conductivity number | The "why pure silicon conducts poorly at 300 K" analysis |
| 4 | Doping | Pentavalent donors and trivalent acceptors (with the "a donor's fifth electron is nearly free" picture); the donor ionisation energy's estimate from a Bohr-model scaling with the dielectric constant and the effective mass (a stunning cross-topic derivation using PART 24); n-type and p-type; the mass-action law $n_en_h=n_i^2$; the "why doped silicon is still electrically neutral" resolution | The donor binding-energy estimate |
| 5 | Carrier transport | Drift and mobility ($\sigma=e(n_e\mu_e+n_h\mu_h)$); why a tiny doping beats the intrinsic conductivity by orders of magnitude; diffusion and the diffusion current; the temperature dependence of mobility vs carrier number | A conductivity calculation for doped silicon |
| 6 | The p–n junction | Diffusion of majority carriers → the depletion region → the built-in field; why the field stops further diffusion (equilibrium); the contact potential ($\sim0.7$ V for Si) and its temperature coefficient; the junction capacitance (link the shipped capacitors note) and its $1/\sqrt V$ dependence announced | Sketch the junction's charge and field profiles |
| 7 | The diode | Forward and reverse bias pictures; the knee voltage; the reverse saturation current; the exponential law $I=I_0(e^{eV/kT}-1)$ (stated, with the thermal voltage $kT/e=26$ mV and the 60 mV-per-decade rule derived); the ideal-diode models for circuits (the decision tree); breakdown: Zener vs avalanche (and which needs a thin junction) | The 60 mV/decade rule applied |
| 8 | Diode circuits | Half-wave and full-wave rectifiers; the smoothing capacitor and the ripple estimate $\Delta V\approx\frac{I}{2fC}$ (link PART 22); clippers and clampers; the peak detector; the voltage doubler's cascade; the average and RMS of the rectified output | Rectifier + capacitor design calculation |
| 9 | Voltage regulation and light | The Zener shunt regulator: choosing the series resistor for the worst-case load and line variation (a genuine engineering calculation); the LED's colour–bandgap relation ($E_g=\frac{hc}{\lambda}$, link PART 23) and the material choice problem (why blue needs GaN); the photodiode and the solar cell (the same junction read in opposite directions) | The LED's bandgap from its colour |
| 10 | The bipolar transistor | The structure and the "why the base must be thin and lightly doped" argument; the current relations $\alpha$, $\beta=\frac{\alpha}{1-\alpha}$, $I_E=I_B+I_C$; the two active-mode rules (0.7 V across the base–emitter, $I_C=\beta I_B$); saturation and cutoff; the "where does the amplified power come from?" resolution (the supply — the classic conceptual trap) | The transistor's currents for a given circuit |
| 11 | Transistor circuits | The common-emitter amplifier's load line and gain; the transistor as a switch (the lamp-driver design calculation); the emitter follower as a buffer; the transistor as a current source; the "why a transistor is not a resistor" summary | The switch design with a real lamp |
| 12 | Logic gates | The diode–transistor NOT gate (analysed, not just asserted); the truth tables of AND, OR, NOT, NAND, NOR, XOR; De Morgan's laws proved by truth table; NAND as a universal gate; the half adder built from XOR + AND; the "why binary?" noise-margin argument | Build and verify a half adder |
| 13 | Devices in the real world | The integrated circuit's scale; Moore's law and its physical limits (tunnelling — link PART 23's uncertainty principle); the photolithography idea; the "how many transistors in a phone?" order of magnitude | The scaling-limit discussion |

**Must be derived, not stated:** the filled-band non-conduction argument; the intrinsic carrier density's
temperature form and its consequence; the donor-ionisation estimate; the conductivity sum; the junction's
equilibrium condition and contact potential; the 60 mV-per-decade rule; the rectifier ripple; the Zener
resistor sizing formulas; the LED's bandgap–wavelength relation; the transistor's $\beta$–$\alpha$
relation; De Morgan's laws; the half adder.

**DIAGRAM briefs (D27.1–D27.18):** the logarithmic resistivity axis with the three classes and real
materials marked; the resistance-vs-temperature curves for a metal, a semiconductor and a thermistor;
the band diagram for a metal, an insulator and a semiconductor with the gaps labelled; the intrinsic
generation/recombination cycle; the hole's motion in a field drawn as successive bond-swaps; the doped
lattice with a pentavalent and a trivalent substitutional atom; the donor's loosely bound electron with
its Bohr-like radius; the p–n junction's depletion region with the fixed ions, the field and the
potential hill; the junction's charge/field/potential profiles as three aligned graphs; the diode's I–V
curve with the knee, the reverse saturation and the breakdown marked; the 60 mV-per-decade exponential
annotated on the forward curve; the half-wave rectifier with the input and output waveforms and the
ripple; the full-wave bridge rectifier; the Zener regulator circuit with the series resistor and the load;
the LED's wavelength vs bandgap chart with material labels; the photodiode/solar-cell operation diagram;
the transistor's structure with the emitter/base/collector currents; the common-emitter load line and the
saturation clipper; the transistor switch with the lamp; the logic gate symbols with truth tables; the
half adder's gate-level circuit.

**Mandatory archetypes:** classify a material by its resistivity/temperature behaviour; the number of
carriers from the mass-action law; the conductivity from the doping; the junction's contact potential;
the diode's current at a given forward voltage; the diode-circuit "is it on or off?" analysis; the
rectifier's DC output and ripple; the Zener regulator's resistor value; the transistor's $I_C$ from
$I_B$; determining whether a transistor is in saturation; the amplifier's voltage gain; the switch
design; a truth-table completion; a gate-combination's output; the LED's colour from the gap.

**Olympiad block content:** the donor/acceptor ionisation energy derived by scaling the hydrogen atom's
Bohr energy with the dielectric constant and the effective mass (the "why a doped electron is bound by
only tens of meV" derivation, linking PART 24 explicitly — and the comparison with the measured value
for Si:P ≈ 45 meV, so the model's factor-of-2 error is discussed honestly); the diode equation's
derivation from the Boltzmann factor and the diffusion/drift balance (the exponential's origin — with
the "why the reverse current is so small" argument); the junction capacitance's $C\propto V^{-1/2}$
derivation from the depletion width (link the shipped capacitors note — a synthesis problem); the
"why a solar cell's efficiency is bounded" argument at the order-of-magnitude level (the spectrum's
photon energies versus the gap, the thermalisation loss, the ~33 % single-junction limit stated);
the transistor as a temperature sensor (the $\Delta V_{BE}$ method) and the bandgap reference idea;
the Hall-effect measurement of a semiconductor's carrier type and density (the link back to PART 18,
now applied to a real sample — the classic lab experiment); the "how small can a transistor be?"
analysis with the tunnelling limit computed from the de Broglie wavelength and the uncertainty
principle (the fundamental end of Moore's law, linking PART 23); the noise floor of a photodiode
receiver (the shot noise $i\sim\sqrt{2eI\Delta f}$ stated and used for a "how weak a signal can I
detect?" calculation); the "why an LED is not a resistor" circuit problem (the series-resistor design
with the diode's steep curve); the "what happens to a solar panel's output when one cell is shaded?"
analysis (the bypass diode's role — real engineering, elementary physics); the "how much power does a
chip dissipate and why does it need a fan?" estimate (the switching energy $\frac12CV^2$ per gate —
linking the shipped capacitors note!).

**Traps to plant:** saying the holes "move" as if they were free particles without the bond-swap picture;
forgetting the fixed ions in the depletion region (and claiming a net charge on the junction);
assuming a doped crystal is charged; using the ideal diode (zero drop) where the 0.7 V matters;
treating a Zener diode as a normal forward diode; assuming $I_C=\beta I_B$ holds in saturation;
forgetting the base current in the power budget; thinking a transistor amplifies *power* from nothing;
confusing the LED's colour with its brightness; assuming the resistance of a thermistor is
temperature-independent.

**Exit criteria:** the band picture is introduced with the filled-band argument (not as a table to
memorise); doping is motivated by the donor-ionisation estimate; the junction is derived
(diffusion → depletion → equilibrium); the diode equation is unpacked with the 60 mV rule; diode circuits
include the ripple calculation; the transistor covers active/saturation/switching with the power-source
resolution; logic gates include De Morgan and a half adder; the Olympiad block contains the donor
binding-energy derivation and the Moore's-law tunnelling limit.

---

### PART 28 · Special Relativity & Relativistic Mechanics

`special-relativity` · folder `special-relativity/` · source: **olympiad extension** — no Cengage
chapter in these volumes; the floor is the IPhO relativity syllabus · needs PART 6, PART 23 and the
shipped `electromagnetic-waves/` note · NSEP (light), INPhO, IPhO.
*The one idea:* space and time are part of the physics rather than a stage; $c$ is the same for everyone
and everything else bends to keep it so.

| # | Section | Teach this, in this order | Closes with |
|---:|---|---|---|
| 1 | The crisis | The Michelson–Morley logic and its null result; the ether's failure; the "what would you have to give up?" framing; the two postulates stated as postulates with the promise that their consequences are testable | The why-the-ether-died summary |
| 2 | Simultaneity goes first | The train-and-lightning thought experiment analysed fully: the conclusion that simultaneity is frame-dependent *before* any formula; the "why this is the deepest result in the chapter" framing | The simultaneity argument written out |
| 3 | The Lorentz transformation | Derive $x'=\gamma(x-vt)$, $t'=\gamma(t-vx/c^2)$ from the postulates (linearity + the light-signal condition); the inverse transformation; the low-speed limit's recovery of Galileo; the invariant interval $s^2=c^2t^2-x^2$ | The transformation derived and limit-checked |
| 4 | Time dilation | The light-clock derivation; the proper-time rule (the clock at both events); the muon experiment as evidence with real numbers; the "which observer ages" question deferred to the twin paradox | Muon survival calculation |
| 5 | Length contraction | The derivation from the transformation (not from time dilation alone); the proper-length rule; the "why the contraction is only along the motion" and "why you cannot see it in a snapshot" notes | The rod-and-barn numbers |
| 6 | Velocity addition | Derive $u'=\frac{u-v}{1-uv/c^2}$; the "nothing exceeds $c$" check; the Fizeau water experiment as evidence; the aberration of light (the "why a moving observer sees a distorted sky" result) | The velocity-addition problems |
| 7 | Momentum and energy | The derivation of $p=\gamma mv$ from momentum conservation in a collision between two frames; $E=\gamma mc^2$; the rest energy; the kinetic energy $(\gamma-1)mc^2$ with the low-speed check; the relation $E^2=(pc)^2+(mc^2)^2$; the photon's $p=E/c$ (the massless limit) | The relativistic kinetic energy at $0.5c$, $0.9c$, $0.99c$ |
| 8 | The invariant and useful combinations | The invariant mass of a system; the "why a system's mass is more than its parts' " (binding energy, heat); the useful approximations and the $\gamma$ values to memorise; the "when does relativity matter? (1 % at $v\approx0.14c$)" table | The 1 %-effect table |
| 9 | Applications with a frame discipline | The twin paradox resolved (the turnaround and the frame change, with a spacetime diagram); the pole-and-barn paradox in both frames; the muon's lifetime; the relativistic Doppler effect (longitudinal and transverse, with the "why the transverse shift is pure time dilation" insight); the aberration and the relativistic beaming of a moving source (a one-paragraph astrophysics link) | The relativistic Doppler's red/blue shifts |
| 10 | Mass–energy in action | The Sun's mass-loss rate; annihilation and pair production (the threshold energy and the "why you need a heavy nucleus nearby" momentum argument); the nuclear binding energy as a mass defect (link PART 26); the "one gram of matter = 20 kilotonnes of TNT" estimate | The pair-production threshold |
| 11 | Relativistic collisions | The elastic collision in the lab and CM frames; the inelastic collision's invariant mass; the threshold energy for a reaction $A+B\to C+D$ derived with invariants (a superb olympiad technique); the Compton effect re-derived as a relativistic collision (link PART 25) | A reaction's threshold kinetic energy |
| 12 | Where relativity shows up in engineering | GPS's two corrections (special and general) with their signs and sizes; particle accelerators' design; the synchrotron radiation loss; nuclear reactors' mass defect; the muon's relativistic lifetime in cosmic-ray showers | The GPS correction arithmetic |
| 13 | The limits and the road beyond | What special relativity does not cover (gravity, accelerating frames) and the one-paragraph statement of general relativity's equivalence principle; the "why $c$ is a speed limit for information" argument; where quantum field theory takes over | The "what I still cannot do" list |

**Must be derived, not stated:** the Lorentz transformation; time dilation and length contraction; the
velocity-addition law; $p=\gamma mv$ from the momentum-conservation argument; $E=\gamma mc^2$'s
consequences; the kinetic-energy expansion's leading term; the invariant relation; the relativistic
Doppler; the pair-production threshold; the reaction threshold with invariants.

**DIAGRAM briefs (D28.1–D28.16):** the Michelson–Morley interferometer with the two arms and the
expected fringe shift; the train-and-lightning simultaneity figure in both frames; the light-clock
triangle with the two paths and $\gamma$'s geometry; the muon's path from the mountain with the two
frames' explanations; a rod and a barn in the two frames; the velocity-addition curve showing the
approach to $c$; the $\gamma$ vs $v/c$ graph with the 1 % and 10 % markers; the energy–momentum triangle
$E^2=(pc)^2+(mc^2)^2$; the Minkowski diagram with the light cone, the world lines and the two frames'
axes; the twin-paradox world lines with the turnaround and the age difference; the relativistic Doppler
geometry with the source's motion; the aberration cone (the "sky distorts" picture); the particle
accelerator's bending and the relativistic mass-increase consequence; the pair-production threshold's
energy bookkeeping; the mass–energy conversion chart (chemical, nuclear, annihilation) on one
log scale; the GPS correction components.

**Mandatory archetypes:** the $\gamma$ factor for a given speed; the proper time between two events;
the length of a moving rod; the velocity-addition problem with two velocities; the relativistic momentum
and kinetic energy at a given speed; the total energy and the rest energy; the mass converted in a
reaction; the muon's survival fraction; the twin paradox's age difference; the relativistic Doppler
wavelength; the invariant interval's classification (timelike/lightlike/spacelike); the threshold energy
for pair production; the Compton shift from the relativistic collision (a cross-topic problem).

**Olympiad block content:** the Lorentz transformation derived twice (the algebraic route from the
postulates and the elegant $k$-factor/Doppler route) — with the proof that they agree; the invariant
interval and the causality analysis (which event pairs can be causally connected, and why the time order
can flip only for spacelike separations); the derivation of $E=mc^2$ from the "photon emitted inside a
moving box" thought experiment (Einstein's original argument, a superb multi-step olympiad problem);
the "what is the mass of a hot body?" calculation (heat as a mass increase, with the fractional size for
a 1 kg block raised by 100 K — the definitive answer to "does energy weigh?"); the relativistic
Doppler derived from the time-dilation plus the source's motion (with the transverse case as the pure
time-dilation check); the resolution of the pole-and-barn paradox in both frames with the simultaneity
analysis (a full worked problem); the "why a rigid body cannot exist in relativity" argument (the front
and back cannot start simultaneously — with the sound-speed limit as the non-relativistic echo); the
derivation of the magnetic force from the electric force via length contraction (the definitive answer to
PART 16's question, now done properly with $\gamma$ factors — the single best synthesis problem in the
whole plan); the relativistic cyclotron frequency's correction and the "how much does the mass increase
in a 1 GeV proton?" arithmetic (link PART 18); the reaction-threshold derivation for
$p+p\to p+p+\pi^0$ with the invariant-mass method and the interpretation of the excess (why a
fixed-target machine needs much more energy than a collider — real physics with real numbers); the
"how long does a journey to Proxima Centauri take from the traveller's point of view?" problem (with
the two frames' answers and the ratio's meaning); the twin-paradox calculation done with the Doppler
shifts of the signals the twins exchange (the "what does each twin see?" table — the honest resolution);
the "why can't you exceed $c$ by adding velocities?" argument in terms of the rapidity addition
(the elegant variable where velocities simply add — a beautiful olympiad-level insight).

**Traps to plant:** applying the time-dilation formula with the wrong clock (identify the two events
first); using $\Delta t=\gamma\Delta t_0$ and $\Delta x=\Delta x_0/\gamma$ in the wrong direction (the
"who is moving?" discipline); adding relativistic velocities with $u+v$; using $E=\frac12mv^2$ at
$0.5c$; forgetting the rest energy in an energy balance; assuming the transverse Doppler effect is
zero; treating simultaneity as absolute in a paradox; using the Newtonian momentum in a
collision where $\gamma$ changes; assuming a photon has mass because it has momentum; forgetting the
electron's rest energy (0.511 MeV) in pair-production arithmetic.

**Exit criteria:** simultaneity precedes the transformation (the pedagogical order that makes the rest
intelligible); the transformation is derived, and both contraction and dilation come from it; the
$p=\gamma mv$ argument is a derivation, not an assertion; the invariant relation and the threshold
technique are taught; the twin and pole-barn paradoxes are resolved with diagrams described in words;
the Olympiad block contains the $E=mc^2$ thought experiment and the magnetic-force-from-Coulomb
derivation.

---

---

## 5 · Execution: batches, parallel agents and conflict rules

### 5.1 The loop for one agent

```bash
git switch -c notes/part-13-electric-field        # never commit to main
mkdir -p electric-field/tools
#  write <Title>.md in the 15-block spine, then README.md, notes.json, tools/check.py (Appendix C)
cd electric-field && python3 tools/check.py        # fix until ALL GOOD
cd .. && python3 tools/check_all.py --update       # registry recount + repo gate
git add -A && git commit -m "part-13: electric-field chapter (gate green)"
```

Commit in the five steps from §1.9 so a reviewer can see the structure land before the prose.

### 5.2 Batch discipline

* **Within a batch:** parts share only the four lines of §1.9. Merging is "keep both". Never let two
  agents reformat the same table: append, do not rewrite.
* **Between batches:** the coordinator (one agent, 20–40 minutes) updates `CURRICULUM.md` and
  `docs/site` from the finished parts, runs the full gate, and posts one summary.
* **Hand-offs are one-directional and written down.** If PART 17 needs a result that PART 21 owns
  (the field energy), it writes `> [!quote] Hand-off` with the pointer and *does not* derive it. Appendix D
  is the ledger; add a row there if you create a new hand-off.
* **An agent that runs out of context mid-part** must commit what passes the gate with a message that
  says what is missing (`part-13: blocks 0–4 (blocks 5–14 pending)`), then the resume prompt of §0.2
  finishes it. A half-written file that fails the gate is not committed.

### 5.3 Sizing and time budget (so no agent over-runs)

| chapter size | parts | target words in `<Title>.md` | expected agent effort |
|---|---|---|---|
| standard | most | 12 000 – 16 000 | 1 long session |
| large | 8 (rotational), 11 (fluids), 13 (electric field), 16 (Biot–Savart), 22 (AC), 24 (Bohr) | 16 000 – 22 000 | 1–2 sessions; split the *commits*, never the chapter |
| compact | 1 (units), 2 (vectors), 12 (elasticity), 19 (matter) | 9 000 – 13 000 | 1 session |

If a chapter is heading past the large bracket, cut *variations* in block 6 and *duplicated* derivations —
never cut block 10 (Olympiad) or block 11 (the paper), which are the chapter's contract.

### 5.4 Review checklist for whoever merges (10 minutes, human or agent)

1. Does the 15-block spine exist in order, with the required minimum counts (the gate checks the
   numbers; you check the *content*)?
2. Open the chapter in **Obsidian reading mode** (or paste it into a vault): do the callouts colour, do
   the `$$` blocks typeset, do the `<details>` panels open with their math intact, do the tables fit?
3. **Book sweep audit:** open the Cengage chapter's contents page (§1.13) and pick two of its headings at
   random; find their row in the coverage map and read the section that serves them.
4. Pick two derivations at random: is every "therefore" justified, and is the validity condition stated
   where the result lands?
5. Recompute one numeric answer and try one limit yourself.
6. Are the DIAGRAM briefs specific enough that a stranger could find the right picture — and are the
   FIGURE `*Why:*`/`*Data:*`/`*Read:*` lines load-bearing (the prose readable *without* them)?
7. Is anything duplicated from another PART or a shipped note (should be a `> [!quote] Hand-off` instead)?
8. Do the paper's marks sum to 200, and does every block 2–4 and 10 appear in the coverage map?
9. Does the chapter README's `## Beyond the plan` list match what the diff actually added beyond the
   PART's section table?
10. `grep -n 'TODO\|FIXME\|{{' <slug>/*.md` is empty; no raster/image syntax anywhere; every mermaid
    block sits inside an `F`-numbered `[!tip] FIGURE` callout.

---

## 6 · Repository integration

### 6.1 What each chapter agent changes (nothing more)

1. `<slug>/**` — the four files of §1.1.
2. `topics.json` — append one object (Appendix C has the template): `slug`, `title`, `status`,
   `owner`, `entry` (`<slug>/<Title>.md`), `format: "markdown"`, `plan_part`, `exam`, `media`
   (`"Obsidian-first; Mermaid FIGURE callouts + DIAGRAM briefs"`), `source` (the exact Cengage
   file + chapter/pp. that the coverage map was built from), `beyond_plan` (what the sweep added),
   `deliberately_not_covered`, `next_candidates`. Leave every mechanical count to `--update`.
3. `README.md` (root) — append one row to the note-sets table with the Markdown link, the figure
   count (Mermaid diagrams) and the question count.
4. `PENDING.md` — mark the chapter's row: `→ PART n · <slug> · <status>`.
5. The chapter's own `README.md`: scope, prerequisites, what it hands on, what it deliberately skips.

### 6.2 What the coordinator does after each batch

```bash
python3 tools/check_all.py --update     # recount everything, fix any drift
python3 tools/md_site.py                # regenerate docs/site (needs pip install markdown)
```

* `tools/md_site.py` — append one tuple to `TOPICS` and one line to `name_map` per new topic (the
  `figures` field in the card is the placeholder-documentation count; keep it 0 and say so in the
  blurb). Take **both** sides of any conflict here and re-run the generator.
* `CURRICULUM.md` — add the new chapters to the reading-order table (one row each: first pass,
  JEE/Cengage floor, olympiad extension) and extend the "why this order" argument. This is the one file
  a chapter agent must not touch.
* `README.md` — make the counts in the table match `topics.json` after the recount.
* `docs/site/**` — commit the regenerated pages (they are tracked on purpose, so the site works from
  `file://`).

### 6.3 Registering honestly

The registry's `figures` count (SVG `assets/figures/` embeds) will be **0** for every chapter in this
plan — the figures are Mermaid `F`-callouts, not image files. That is not a failure; it is the media
policy of §1.2 (figures render from ` ```mermaid ` source inside the `.md`). Say so in the chapter
README (`media: Obsidian-first; Mermaid FIGURE callouts + DIAGRAM briefs`, with the F-count named) and
in the `topics.json` `media` field, so a future reader does not "fix" it by generating SVGs.
`tools/md_site.py` ignores Mermaid blocks gracefully (they remain as fenced source in the HTML export),
so no change is required.

---

## 7 · Final audit of the whole plan

Run once, when the last part is merged, and again after any later edit:

1. **The gate.** `python3 tools/check_all.py` green from the repo root. Then
   `python3 tools/check_all.py --quick` to confirm it is not being slowed by a stale artifact.
2. **The census.** `grep -c '^## PART ' plan.md` is 28, and the topics marked complete in
   `topics.json` equal the shipped topics (Appendix A) plus the completed parts.
3. **Cross-part consistency.** No chapter re-derives another chapter's owned result (Appendix D);
   every `> [!quote] Hand-off` points at a section that exists; the notation is uniform across chapters
   ($\mathbf E$ for fields, $\mu_0$ not $k_m$, eV/nm/km-s conventions fixed once).
4. **Obsidian pass over the whole vault.** Open `docs/site`-independent: the repo root as an Obsidian
   vault; check that every chapter renders in reading mode (callouts, math, details, tables, wikilinks
   resolving rather than showing as broken links) and that the frontmatter `part:` properties are
   complete enough to filter the vault by block A/B/C.
5. **The numbers.** Spot-check five numeric answers across five different chapters by recomputation,
   and confirm each has a unit and a limit check beside it.
6. **The paper quality.** Read one section-D question per batch as a hostile examiner: is it
   answerable in the stated time, is the marking scheme's sum right, and does the solution name the
   method before the algebra?
7. **The book sweeps.** For every finished chapter, open its Cengage chapter's contents page and confirm
   three random headings are covered; then confirm every `beyond_plan` entry has been folded back into
   plan.md (and delete the `beyond_plan` entry once it is part of the plan proper).
8. **The reader's path.** Read `CURRICULUM.md` top to bottom and confirm a beginner can follow the
   reading order from units → mechanics → electrostatics → magnetism → EMI/AC → modern physics with no
   forward reference that has not been flagged.
9. **The honesty pass.** Every chapter keeps its "deliberately not covered" list in `topics.json` and
   its README, and no chapter claims more scope than it delivers — including the two places where the
   plan overrides an older note: X-rays living inside the atomic-physics chapter, and semiconductors
   having no Cengage chapter at all.

---

## Appendix A · Already shipped (do not rewrite, do not renumber)

These nine note-sets are complete on `main` and pass `python3 tools/check_all.py`. They keep their own
diagrams (SVGs / HTML editions) and stay in HTML-style markup (bold-label boxes); the *new* chapters of
this plan are Obsidian-first Markdown (§1.3.1) with Mermaid `F`-figures and DIAGRAM briefs. Treat these
nine as the vault's reference shelf: they define the notation the new chapters must match, and their
results are hand-offs, not material to re-derive.

**The five Cengage PDFs are in the repository root** (`git ls-files | grep pdf`), which is what makes the
"≥ Cengage floor" claim checkable: §1.13 maps each file to the chapters it really contains, the pages its
contents page sits on, and the two places where the older book-notes in the repo were wrong about which
volume owns which chapter.

| # | note-set | location | origin |
|---:|---|---|---|
| 1 | String waves | [string-waves/String-waves.md](string-waves/String-waves.md) | plan v1 PART 1 |
| 2 | Sound waves | [sound-waves/Sound-waves.md](sound-waves/Sound-waves.md) + HTML | plan v1 PART 2 |
| 3 | Electromagnetic waves | [electromagnetic-waves/Electromagnetic-waves.md](electromagnetic-waves/Electromagnetic-waves.md) (+ paper + solutions) | plan v1 PART 3 |
| 4 | Wave optics | [wave-optics/Wave-optics.md](wave-optics/Wave-optics.md) | plan v1 PART 4 |
| 5 | Thermodynamics | [thermodynamics/Thermodynamics.md](thermodynamics/Thermodynamics.md) + HTML | earlier work |
| 6 | Heat | [heat/Heat.md](heat/Heat.md) + HTML | earlier work |
| 7 | Capacitors | [capacitors/Capacitors.md](capacitors/Capacitors.md) + HTML | earlier work |
| 8 | Current electricity | [current-electricity/Current-electricity.md](current-electricity/Current-electricity.md) + HTML | earlier work |
| 9 | Geometrical optics | [geometrical-optics/Geometrical-optics.md](geometrical-optics/Geometrical-optics.md) + HTML | earlier work |

Plan v1 itself is archived verbatim at [docs/plan-v1-waves-optics.md](docs/plan-v1-waves-optics.md) so
the provenance of parts 1–4 stays readable. The cross-topic reading order and the Cengage→Olympiad audit
live in [CURRICULUM.md](CURRICULUM.md); the registry is [topics.json](topics.json).

**Existing-topic hand-offs the new chapters must respect** (these results are already derived in-repo;
cite them, do not re-derive them): the wave equation and standing waves (string waves), acoustic
intensity and Doppler (sound waves), Maxwell's equations and the Poynting vector (electromagnetic
waves), thermodynamic processes and entropy (thermodynamics), calorimetry and conduction (heat),
capacitance and dielectrics (capacitors), drift, Kirchhoff and instruments (current electricity),
mirrors/lenses/prisms (geometrical optics), Huygens, interference and diffraction (wave optics).

---

## Appendix B · Deliberately out of scope (and where each one hands off)

| topic | why it is not a PART | where the reader goes |
|---|---|---|
| Thermal expansion, calorimetry, kinetic theory, laws of thermodynamics, entropy, heat transfer | already covered to Olympiad depth | the shipped `heat/` and `thermodynamics/` notes |
| Waves on strings, sound, EM waves, ray optics, wave optics | already covered | the shipped notes of Appendix A |
| Capacitance and circuits (lumped) | already covered | shipped `capacitors/`, `current-electricity/` |
| Communication systems (AM/FM, modulation) | JEE **Main**-only material, no Olympiad content; a short appendix can be added to PART 22 if the reader wants it | PART 22 §11 (rectifiers/filters) is the closest bridge |
| A Cengage *magnetism/EMI/AC* volume | never supplied to this repository; PARTS 16–22 therefore have no PDF to sweep and use the standard JEE syllabus as the floor (§1.13) | the PART sections themselves list the headings; the shipped `current-electricity/` and `electromagnetic-waves/` notes carry the neighbouring results |
| A *semiconductors* chapter | not present in the supplied volumes (the optics/modern volume's Unit II is chs 3–5 only) | PART 27's coverage map is built from the standard JEE syllabus; grep the other PDFs first |
| A *special-relativity* chapter | not in the JEE syllabus; it is the IPhO extension | PART 28 |
| Astrophysics, cosmology, stellar structure | a full course of its own; fragments appear inside PART 9 (orbits, tides), PART 24 (spectra), PART 26 (nucleosynthesis), PART 28 (Doppler/beaming) | those blocks, then a dedicated course |
| General relativity, formal quantum mechanics, statistical mechanics, quantum field theory | university level; the plan stops at the boundary and names it | PART 9 (Newtonian gravity's limit), PART 23–26 (the quantum facts without the formalism), PART 28 §13 |
| Numerical simulation, SPICE, finite elements, computational physics | not examinable and not needed for understanding | the analytic results everywhere, plus `python` for the numeric checks the plan requires |
| Engineering design courses (control systems, signal processing, semiconductor fabrication) | beyond the exam scope | PART 22 (filters), PART 27 (device physics), PART 12 (materials) |

Anything the reader still misses after all 28 parts is a *new* part: add it as PART 29+ at the end of
this file with the same §1 contracts, and register it the same way.

---

## Appendix C · The copy-paste kit

Everything below is meant to be copied rather than invented. Replace `<slug>`, `<Title>`, `<PART>`
and the chapter title; keep the syntax byte-for-byte, because the gate in §C.2 reads it.

### C.1 `notes.json`

```json
{
  "slug": "work-energy-power",
  "title": "Work, Energy & Power",
  "master": "Work-energy-power.md",
  "part": 6,
  "source": "Cengage MECHANICS 2-compressed.pdf ch 2 Rigid Body Dynamics (pp. 2.1-2.32)",
  "obsidian": "reading mode: frontmatter, callouts, $...$ / $$...$$, details panels, Mermaid FIGURE callouts + DIAGRAM briefs",
  "paper": {
    "questions": 36,
    "marks": 200,
    "minutes": 180,
    "sections": { "4": 20, "5": 6, "9": 10 }
  },
  "minimums": {
    "checks": 12,
    "exemplars": 10,
    "practice": 25,
    "olympiad": 10,
    "diagrams": 6,
    "figures": 6,
    "words": 9000,
    "callouts": 24
  },
  "callout_types": ["note", "info", "warning", "success", "danger", "tip", "quote",
                    "question", "abstract", "example"]
}
```

`sections` is "marks per question → how many questions carry that mark". The default shape of §1.7
(12×4, 8×4, 6×5, 10×9) is therefore `{ "4": 20, "5": 6, "9": 10 }` and sums to 200. Raise `words`
for the large chapters (16 000–22 000), never lower the others.

### C.2 `tools/check.py` (copy verbatim; it is tested)

```python
#!/usr/bin/env python3
"""Local gate for an Obsidian-first Markdown chapter written under plan.md.

Run it from the topic folder:   python3 tools/check.py
Everything it enforces comes from plan.md §1 and this topic's notes.json.
"""
from __future__ import annotations
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CFG = json.loads((ROOT / "notes.json").read_text(encoding="utf-8"))
SRC = (ROOT / CFG["master"]).read_text(encoding="utf-8")

errors: list[str] = []


def need(cond: bool, msg: str) -> None:
    if not cond:
        errors.append(msg)


def contiguous(tag: str, pattern: str, minimum: int) -> int:
    got = [int(n) for n in re.findall(pattern, SRC, re.M)]
    shown = got[:12] + (["..."] if len(got) > 12 else [])
    need(got == list(range(1, len(got) + 1)),
         f"{tag}: numbering must run 1..n with no gaps or repeats (got {shown})")
    need(len(got) >= minimum, f"{tag}: {len(got)} found, plan.md requires at least {minimum}")
    return len(got)


# ---- 0. Obsidian frontmatter ---------------------------------------------------
need(SRC.startswith("---\n"), "the file must open with a YAML frontmatter block ('---')")
if SRC.startswith("---\n"):
    fm = SRC[4:SRC.find("\n---", 4)]
    for key in ("title:", "part:", "slug:"):
        need(key in fm, f"frontmatter is missing '{key}'")
    need(str(CFG["part"]) in fm, f"frontmatter 'part:' must be {CFG['part']}")

# ---- 1. the 15 blocks, in order ------------------------------------------------
blocks = re.findall(r"^## Part (\d+) · ", SRC, re.M)
need(blocks == [str(i) for i in range(15)],
     f"the 15 blocks must appear in order as '## Part 0 · ...' through '## Part 14 · ...' (got {blocks})")

# ---- 2. the question families --------------------------------------------------
n_c = contiguous("concept checks", r"^\*\*C(\d+) — ", CFG["minimums"]["checks"])
n_e = contiguous("worked exemplars", r"^### E(\d+) — ", CFG["minimums"]["exemplars"])
n_q = contiguous("practice questions", r"^#### Q(\d+)\. ", CFG["minimums"]["practice"])
n_ol = contiguous("olympiad problems", r"^### OL(\d+) — ", CFG["minimums"]["olympiad"])

# ---- 3. the paper --------------------------------------------------------------
paper = [(int(n), int(m)) for n, m in re.findall(r"^### P(\d+) · (\d+) marks", SRC, re.M)]
need([n for n, _ in paper] == list(range(1, 37)),
     f"paper must have P1..P36 with no gaps (got {len(paper)})")
marks = sum(m for _, m in paper)
need(marks == CFG["paper"]["marks"],
     f"paper marks sum to {marks}, notes.json says {CFG['paper']['marks']}")
for m, count in CFG["paper"]["sections"].items():
    got = sum(1 for _, mm in paper if mm == int(m))
    need(got == count, f"paper: expected {count} questions worth {m} marks, found {got}")
sections = re.findall(r"^#### Section ([A-D]) · ", SRC, re.M)
need(sections == ["A", "B", "C", "D"], f"paper sections A-D must be present in order (got {sections})")
need(SRC.count("<details>") >= len(paper), "every paper question needs its own collapsible solution")

# ---- 4. figure briefs (Obsidian callouts) --------------------------------------
diags = re.findall(r"^> \[!abstract\] DIAGRAM D(\d+)\.(\d+) · ", SRC, re.M)
need(len(diags) >= CFG["minimums"]["diagrams"],
     f"DIAGRAM briefs: {len(diags)} found, plan.md requires at least {CFG['minimums']['diagrams']}")
need(not [p for p, _ in diags if int(p) != CFG["part"]],
     f"DIAGRAM numbers must start with this part's number ({CFG['part']})")
need(SRC.count("*Show:*") >= len(diags), "every DIAGRAM brief needs a '*Show:*' line")
need(SRC.count("*Search:*") >= len(diags), "every DIAGRAM brief needs a '*Search:*' line")

# ---- 5. media policy -----------------------------------------------------------
fence = chr(96) * 3                          # never write a literal fence in this file
for pattern, why in ((r"!\[", "Markdown image"), (r"<img", "HTML image"),
                     (r"\]\(https?://", "external link")):
    need(not re.search(pattern, SRC), f"media policy: no {why} allowed")
need(not re.search(r"\.(png|jpe?g|gif|webp)\b", SRC, re.I), "media policy: no raster images")
# ── FIGURE system (plan.md §1.2 media policy v2 / docs/obsidian-plugin-workflow.md §2) ──
figs = re.findall(r"^> \[!tip\] FIGURE F(\d+)\.(\d+) · ", SRC, re.M)
need(len(figs) >= CFG["minimums"]["figures"],
     f"FIGURES: {len(figs)} found, requires at least {CFG['minimums']['figures']}")
need(not [p for p, _ in figs if int(p) != CFG["part"]],
     f"FIGURE numbers must start with this part's number ({CFG['part']})")
need(SRC.count("*Why:*") >= len(figs), "every FIGURE needs a '*Why:*' line")
need(SRC.count("*Data:*") >= len(figs), "every FIGURE needs a '*Data:*' line")
need(SRC.count("*Read:*") >= len(figs), "every FIGURE needs a '*Read:*' line")
mm = re.findall(fence + r"mermaid[ \t]*\n([A-Za-z0-9_-]+)", SRC)
kinds = {"flowchart", "graph", "mindmap", "xychart-beta", "quadrantChart",
         "sequenceDiagram", "stateDiagram-v2", "stateDiagram", "classDiagram",
         "pie", "erDiagram", "gitGraph", "gantt", "journey"}
need(all(k in kinds for k in mm), f"unknown mermaid kind: {sorted(set(mm) - kinds)}")
need(len(mm) >= len(figs), "every FIGURE needs a ```mermaid block")

# ---- 6. Obsidian reading-mode contract -----------------------------------------
callouts = re.findall(r"^> \[!([a-z]+)\]", SRC, re.M)
need(len(callouts) >= CFG["minimums"]["callouts"],
     f"Obsidian callouts: {len(callouts)} found, notes.json requires at least {CFG['minimums']['callouts']}")
need(not [c for c in callouts if c not in CFG["callout_types"]],
     f"unknown callout type: {sorted(set(callouts) - set(CFG['callout_types']))}")
bold_box = re.findall(r"^> \*\*(Definition|Why|Condition|Check|Trap|Insight|Hand-off|"
                      r"Exam note|Numbers|History|Example)\.\*\*", SRC, re.M)
need(not bold_box, "use the Obsidian callout form (> [!type] Title) instead of "
                   f"'> **Label.**' boxes: {bold_box[:3]}")
need(not re.search(r"<summary>.*?</summary>\n(?!\n)", SRC, re.S),
     "leave a blank line after </summary> so Obsidian renders the solution body")
need(not re.search(r"[^\n]\n</details>", SRC), "leave a blank line before </details>")
for m in re.finditer(r"\$\$(.*?)\$\$", SRC, re.S):
    need(not re.search(r"\n\s*\n", m.group(1)), "no blank line inside a $$...$$ block")
for m in re.finditer(r"(?<![\\$])\$(?!\$)([^\n$]*)(?<!\\)\$(?!\$)", SRC):
    tex = m.group(1)
    need(tex == tex.strip(), f"Obsidian needs no space just inside the dollars: {tex[:40]!r}")
need(not re.search(r"\\\(|\\\[", SRC), r"use $...$ / $$...$$; Obsidian does not render \( \) or \[ \]")
need("\\tag" not in SRC and "\\label" not in SRC,
     "no \\tag or \\label; number equations as a trailing \\qquad (n)")
table_pipes = []
for line in SRC.split("\n"):
    if line.startswith("|"):
        for tex in re.findall(r"(?<![\\$])\$(?!\$)([^\n$]*)(?<!\\)\$(?!\$)", line):
            if "|" in tex.replace("\\|", ""):
                table_pipes.append(tex[:40])
need(not table_pipes, f"escape the pipe or use \\lvert/\\rvert inside table maths: {table_pipes[:3]}")
tags, inside = [], False
for line in SRC.split("\n"):
    if line.startswith(fence):
        inside = not inside
        continue
    if inside or line.lstrip().startswith("#"):
        continue
    if re.search(r"(?<!\S)#[A-Za-z][A-Za-z0-9_/-]*", line):
        tags.append(line[:60])
need(not tags, f"no #hashtags in prose - they become Obsidian tags: {tags[:3]}")

# ---- 7. authoring hygiene ------------------------------------------------------
need(not re.search(r"TODO|FIXME|\{\{[A-Z_]+\}\}", SRC), "unfinished authoring placeholder")
need(not re.search(r"\?\s*no:", SRC), "thinking-out-loud fragment ('? no:')")
need(SRC.count("<details>") == SRC.count("</details>"), "<details> / </details> mismatch")
need(SRC.count("<summary>") == SRC.count("</summary>"), "<summary> / </summary> mismatch")
need(len(SRC.split()) >= CFG["minimums"]["words"],
     f"only {len(SRC.split())} words, notes.json requires at least {CFG['minimums']['words']}")

# ---- 8. maths hygiene ----------------------------------------------------------
body = re.sub(fence + r".*?" + fence, "", SRC, flags=re.S)   # code fences are not maths
displays = re.findall(r"\$\$(.*?)\$\$", body, re.S)
rest = re.sub(r"\$\$.*?\$\$", "", body, flags=re.S)
inline = re.findall(r"(?<![\\$])\$(?!\$)([^\n$]*)(?<!\\)\$(?!\$)", rest)
need(rest.count("$") % 2 == 0, "unbalanced single-dollar delimiters")
need(body.count("$$") % 2 == 0, "unbalanced display-math delimiters")
for tex in displays + inline:
    depth = 0
    for tok in re.findall(r"(?<!\\)[{}]", tex):
        depth += 1 if tok == "{" else -1
        if depth < 0:
            break
    need(depth == 0, f"unbalanced TeX braces in: {tex[:60]!r}")

# ---- report --------------------------------------------------------------------
if errors:
    print("\n".join(f"FAIL: {e}" for e in errors))
    sys.exit(1)
print(f"ALL GOOD: 15 blocks · C×{n_c} E×{n_e} Q×{n_q} OL×{n_ol} · "
      f"paper {len(paper)} Q / {marks} marks · {len(diags)} DIAGRAM briefs · "
      f"{len(figs)} FIGURES (mermaid) · {len(callouts)} callouts · no raster images")
```

Run it from inside the topic folder. It fails with a list of `FAIL:` lines; a clean chapter prints
`ALL GOOD: …`. It is deliberately independent of any other tool in the repository, so a chapter folder
copied anywhere still validates itself.

### C.3 The chapter skeleton (frontmatter + the 15 blocks + the four recurring patterns)

```markdown
---
title: Work, Energy & Power
part: 6
slug: work-energy-power
source: Cengage Mechanics 2, ch 2 (pp. 2.1-2.32)
aliases: [WEP, work energy power]
tags: [jee-advanced, olympiad, mechanics]
---

# Work, Energy & Power — first principles to Olympiad

> [!abstract] How to use this chapter
> Three passes: read Parts 0-4 for the physics, 5-9 for the exam craft, 10-14 for the Olympiad layer.

## Part 0 · Orientation
## Part 1 · Intuition first
## Part 2 · Definitions and bookkeeping
## Part 3 · Core derivations
## Part 4 · Results, limits and the validity ledger
## Part 5 · Worked exemplars
## Part 6 · Problem archetypes and practice
## Part 7 · Alternate methods and the JEE-Advanced advantage toolkit
## Part 8 · Examiner traps
## Part 9 · Playbook
## Part 10 · Olympiad extension
## Part 11 · Olympiad-grade paper
## Part 12 · Marking scheme and post-paper audit
## Part 13 · Formula sheet
## Part 14 · Checkpoint and hand-off
```

**The four patterns you will write hundreds of times.** Copy them exactly; the spacing is part of the
contract (§1.3.1).

```markdown
> [!note] Definition
> Work is energy in transit: $W=\mathbf F\cdot\mathbf d$ for a constant force.

> [!warning] Condition of validity
> Valid for a constant force along a straight displacement; for a variable force integrate, Eq. (3.4).

### E7 — The block on the accelerating wedge

A block of mass $m$ rests on a wedge of mass $M$ that is pushed with force $F$ ...

> [!success] Check
> As $F\to 0$ the block slides down the incline with $a=g(\sin\theta-\mu\cos\theta)$, the standard result, so the sign is right.

<details><summary>Solution</summary>

**Method.** System first for the acceleration, then the block alone for the contact force.

$$\mathbf F_{\text{net}} = (M+m)a \qquad (7.2)$$

... algebra, numbers with units, then the check above ...

</details>

> [!abstract] DIAGRAM D6.3 · Work as the area under a force-displacement curve
> *Show:* force $F$ on the vertical axis against displacement $x$ on the horizontal; the curve rising then falling; the area shaded in two colours for the positive and the negative parts; the turning point where $F$ changes sign circled.
> *Search:* "work done area under force displacement graph positive negative"
> *Used in:* §3.4 and Q9.
```

For the paper, the exemplar pattern is

```markdown
#### Section D · Comprehensive long-form

### P27 · 9 marks

A chain of mass $M$ and length $L$ hangs over a frictionless peg ...

<details><summary>Solution</summary>

**Method.** Centre-of-mass argument first; energy only after the constraint is written down.

... full solution, marking split in the text (3+3+3) ...

</details>
```

### C.4 The markers the gate counts

| marker | use | example |
|---|---|---|
| `**C4 — concept check.** …` | a 20-second check with a one-line answer | `**C4 — concept check.** If the block is pushed at the top edge, does it slide?` |
| `### E7 — …` | a worked exemplar with a full solution | `### E7 — The falling chain on a scale` |
| `#### Q12. …` | an interleaved practice question | `#### Q12. A spring is compressed by 5 cm …` |
| `### OL3 — …` | an Olympiad long problem | `### OL3 — The rolling cylinder in a track` |
| `### P14 · 5 marks` | a paper question (the marks are summed by the gate) | `### P14 · 5 marks` |
| `> [!abstract] DIAGRAM D6.3 · …` | a figure brief (§1.2) | see C.5 |
| `> [!note]` / `[!info]` / `[!warning]` / `[!success]` / `[!danger]` / `[!tip]` / `[!quote]` / `[!question]` / `[!example]` | definition · why · validity · check · trap · insight · hand-off/history · exam note · worked example | see C.3 |

Every problem of every family ends with

```markdown
<details><summary>Solution</summary>

*Method named first, then the algebra, then the checks.*

</details>
```

and the blank lines after `</summary>` and before `</details>` are compulsory (§1.3.1 item 7).

### C.5 The DIAGRAM brief (the runtime seed — a FIGURE F-callout renders the pictures that are ready)

```markdown
> [!abstract] DIAGRAM D6.3 · Work as area under a force-displacement curve
> *Show:* the force $F$ on the vertical axis against displacement $x$ on the horizontal; the curve rising then falling; the area between the curve and the axis shaded in two colours for the positive and the negative parts; the turning point where $F$ changes sign marked with a small circle.
> *Search:* "work done area under force displacement graph positive negative"
> *Used in:* §3.4 and Q9.
```

Rules: numbering `D<PART>.<n>` contiguous from 1; one blank line after the callout; `*Show:*` must be a
complete drawing brief (axes, labels, what is dashed, shaded or circled); `*Search:*` must be 5–12 plain
English words a search engine will match; the surrounding prose must be readable without the picture.

### C.6 The coverage map (block 0) and the archetype table (block 6)

The coverage map is where the §1.12 book sweep becomes visible. One row per Cengage heading — including the
chapter's `Solved Examples` band and its exercise **types** — plus one row per section you added beyond the
plan, marked `added by the sweep`.

```markdown
### 0.4 Cengage coverage map

| Cengage section | What it establishes | Where it lives here | Status |
|---|---|---|---|
| The work–energy theorem | $W_{\text{net}}=\Delta K$ for a particle | §3.1–3.2, E1–E3, Q1–Q4 | derived |
| Energy diagrams | turning points, stability | §3.9, E8, Q17 | extended beyond book |

### 6.1 Archetypes

| # | Archetype | Template (one line) | Where worked | Variations |
|---:|---|---|---|---|
| 1 | Block on a rough incline | $W_f=-f\cdot s$, then WET | Q2 | change the angle, then the mass |
```

### C.7 `topics.json` — append exactly one object

```json
{
  "slug": "work-energy-power",
  "title": "Work, Energy & Power — first principles to Olympiad",
  "status": "in-progress",
  "owner": "<your handle or agent id>",
  "entry": "work-energy-power/Work-energy-power.md",
  "format": "markdown",
  "plan_part": 6,
  "source": "Cengage MECHANICS 2-compressed.pdf, ch 2 Rigid Body Dynamics, pp. 2.1-2.32",
  "exam": ["JEE Advanced", "NSEP", "INPhO", "IPhO"],
  "media": "Obsidian-first; Mermaid FIGURE callouts + DIAGRAM briefs (no image files by design)",
  "beyond_plan": [
    "the variable-mass energy audit (plan asked for the rocket only)",
    "the effective potential and the reduced-mass energy split"
  ],
  "deliberately_not_covered": [
    "rotational kinetic energy beyond the rolling preview (owned by PART 8)",
    "two-body Lagrange formalism (not in JEE or IPhO syllabus)"
  ],
  "next_candidates": ["a timed 25-question JEE-Advanced-only set keyed to blocks 2-4"]
}
```

Then run `python3 tools/check_all.py --update` from the repo root: it fills `pages`, `questions`,
`solutions`, `math_spans`, `words`, `display_formulas`, `bytes_markdown` and `bytes_html` mechanically.
Never hand-edit those fields.

### C.8 The chapter `README.md`

```markdown
# Work, Energy & Power — first principles to Olympiad

> [!note] Part 6 of [plan.md](../plan.md) · Obsidian-first Markdown chapter · written for Obsidian reading mode

**Scope.** One paragraph on what this chapter teaches and to what depth.
**Prerequisites.** PART 5 (Newton's laws), … plus the shipped notes it cites.
**The one idea.** One sentence (from plan.md §3).
**Contents.** A bullet per block with the section range.
**Coverage (Cengage floor).** The chapter and pages of the PDF the sweep read (e.g. *Cengage Mechanics 2*,
ch 2 §2.24-2.26), and where the full row-by-row map lives (block 0 of the chapter).
**Olympiad layer.** What block 10 adds beyond the book: the three derivations, the estimates.
**Beyond the plan.** The sections, archetypes and problems this chapter added that plan.md PART 6 did not
ask for — mirrored in `topics.json` as `beyond_plan`, so the coordinator can fold them back into the plan.
**Hand-off.** What the next PART inherits; what a reader can now attempt.
**Media.** Figures are Obsidian-native and deterministic ([docs/obsidian-plugin-workflow.md](../docs/obsidian-plugin-workflow.md) §2): `F`-numbered Mermaid diagrams (mindmap, quadrant, data graphs, flowchart) in `[!tip] FIGURE` callouts. Deferred hand-drawn figures stay searchable `> [!abstract] DIAGRAM D6.k` briefs with a `*Search:*` line. No raster art, no AI SVG, no external images.
**Gate.** `python3 tools/check.py` → ALL GOOD (…).
```

### C.9 The paper's header (copy, then edit the numbers)

```markdown
## Part 11 · Olympiad-grade paper

**Time: 180 minutes · Maximum marks: 200 · 36 questions.**
Sections: A — 12 single-correct (4 marks each, −1 for a wrong answer); B — 8 one-or-more-correct
(4 marks each, no negative marking); C — 6 numerical answers (5 marks each); D — 10 long-form
(9 marks each). Solutions follow each question in a collapsible block; the marking scheme is in Part 12.

| Section | Questions | Marks each | Subtotal | Topic coverage |
|---|---|---:|---:|---|
| A | 1–12 | 4 | 48 | blocks 2–4 |
| B | 13–20 | 4 | 32 | blocks 3–4 |
| C | 21–26 | 5 | 30 | blocks 4, 10 |
| D | 27–36 | 9 | 90 | blocks 10 |
| | 36 | | 200 | |
```

### C.10 Branch, commit and PR

```bash
git switch -c notes/part-<N>-<slug>
# … write the chapter …
cd <slug> && python3 tools/check.py
cd .. && python3 tools/check_all.py --update
git add <slug> topics.json README.md PENDING.md
git commit -m "part-<N>: <slug> — <what landed>"
git push -u origin notes/part-<N>-<slug>
gh pr create --title "part-<N>: <slug> — <Title>" --body "Blocks 0–14 complete; gate green; \
new questions: E1–E10, Q1–Q25, OL1–OL10, P1–P36 (200 marks). drive-by: none."
```


---

## Appendix D · Cross-part ownership ledger (read this before deriving anything)

If a result appears in the left column, **it is owned by the right column**: write a
`> [!quote] Hand-off` callout and move on. This is what keeps 28 independently written chapters from
becoming a pile of near-duplicates.

| result / machinery | owner | consumes it |
|---|---|---|
| the wave equation, standing waves, impedance of a string | shipped `string-waves/` | PART 10 (the $N$-mass limit), PART 11 (shallow-water waves) |
| acoustic intensity, decibels, organ pipes, acoustic Doppler | shipped `sound-waves/` | PART 12 ($v=\sqrt{B/\rho}$), PART 28 (the relativistic Doppler) |
| Maxwell's equations, Poynting vector, radiation pressure, EM spectrum | shipped `electromagnetic-waves/` | PART 20 (conducting media, skin depth), PART 22, PART 23, PART 25 |
| Huygens, interference, YDSE, thin films, diffraction, polarisation | shipped `wave-optics/` | PART 23 (electron diffraction), PART 25 (crystal diffraction) |
| the laws of thermodynamics, entropy, engines, kinetic theory | shipped `thermodynamics/` | PART 26 (energy scales, the Sun), PART 28 (heat and mass) |
| calorimetry, expansion, conduction, radiation | shipped `heat/` | PART 12 (thermal stress uses expansion) |
| capacitance, dielectrics, RC networks | shipped `capacitors/` | PART 15 (announces the field energy), PART 27 (junction capacitance, gate switching energy) |
| drift, Ohm, Kirchhoff, bridges, instruments, heating | shipped `current-electricity/` | PART 20, PART 21, PART 22, PART 27 |
| mirrors, refraction, prisms, lenses, instruments | shipped `geometrical-optics/` | PART 25 (Bragg as a 3-D grating) |
| dimensional analysis, error propagation, instruments, statistics | **PART 1** | all parts; PART 26 (counting statistics), PART 18 (measurement), PART 10 (measuring $g$) |
| vector algebra, dot/cross products, the rotating basis | **PART 2** | PARTS 4, 5, 8, 13, 16, 19 |
| graphs, integration of kinematics, drag laws, the $v\,dv/dx$ method | **PART 3** | PARTS 4–12 |
| projectile results, relative velocity, radius of curvature, circular kinematics | **PART 4** | PARTS 5, 9, 13, 18 |
| free-body discipline, friction ranges, constraint method, pseudo forces, circular dynamics | **PART 5** | PARTS 6–15, 18 |
| work–energy theorem, potential energy, $U(x)$ stability | **PART 6** | PARTS 7–15, 23, 28 |
| COM/momentum bookkeeping, collisions, variable mass, the rocket, reduced mass, CM frame | **PART 7** | PARTS 8, 10, 11, 26, 28 |
| moment of inertia, torque, angular momentum, rolling, gyroscopes, equilibrium/toppling | **PART 8** | PARTS 9, 10, 11, 12, 26 |
| the shell theorem, $g$ variations, orbit energies, Kepler, tides | **PART 9** | PARTS 10 (tunnel SHM), 14 (the Gauss analogy), 26, 28 |
| SHM kinematics, the small-oscillation linearisation, damping, resonance, $Q$, normal modes | **PART 10** | PARTS 11, 12, 17, 19, 21, 22 |
| hydrostatics, Archimedes, Bernoulli, Poiseuille, Stokes, surface tension | **PART 11** | PARTS 12, 13, 14, 15, 26 |
| stress/strain, the three moduli, elastic energy, bending, thermal stress | **PART 12** | PARTS 10, 21, 26 |
| the element-and-symmetry field method, the dipole (field, torque, energy), the conductor-surface field | **PART 13** | PARTS 14–16, 23 |
| flux, the Gaussian-surface protocol, $E=\sigma/\varepsilon_0$ for a conductor, electrostatic pressure, Earnshaw | **PART 14** | PARTS 15, 27, and PART 9's gravity analogy |
| potential, assembly energy, conductor properties, the image method, the Rayleigh drop limit | **PART 15** | PARTS 16, 21, 23, 24, 26, 27 |
| the Lorentz force, Biot–Savart fields, the magnetic moment, motor torque, the relativistic origin of $\mathbf B$ | **PART 16** | PARTS 17–20, 28 |
| Ampère's law, magnetic pressure, dipole–dipole forces, the Helmholtz condition | **PART 17** | PARTS 18, 19, 21 |
| cyclotron/mass spectrometer, the Hall effect, drifts, $e/m$ | **PART 18** | PARTS 21, 27, 28 |
| magnetisation, hysteresis energy, Curie behaviour, Earth's field, the Meissner effect | **PART 19** | PARTS 20, 21 |
| Faraday/Lenz, motional EMF, the induced field, the betatron condition, eddy-current braking | **PART 20** | PARTS 21, 22, 27 |
| inductance, RL transients, magnetic field energy, the coil force $F=\frac12I^2\frac{dM}{dx}$, LC oscillation | **PART 21** | PARTS 22, 26 |
| RMS/phasors, series and parallel resonance, power factor, transformers, rectifier ripple | **PART 22** | PART 27 (supplies, ripple, matching) |
| photons, the photoelectric equation, de Broglie, the uncertainty principle | **PART 23** | PARTS 24, 25, 26, 27, 28 |
| the Bohr model, hydrogen spectra, $Z^2$ scaling, the Zeeman splitting, Moseley's law *mention* | **PART 24** | PARTS 25, 26, 27 |
| X-ray production and spectra, Moseley's law *derivation*, Bragg, Compton, pair-production threshold | **PART 25** | PART 26, PART 28 |
| nuclear size/density, the binding-energy curve, decay laws, chain equilibrium, dating, fission/fusion, counting statistics | **PART 26** | PART 28 (mass defect), the shipped thermal notes (energy scales) |
| bands, doping, the p–n junction, the diode law, transistor active/saturation/switching, logic gates | **PART 27** | — |
| the Lorentz transformation, dilation/contraction, velocity addition, relativistic energy–momentum, thresholds, the relativistic Doppler | **PART 28** | — (it is the terminal chapter; it answers PART 16's opening question) |

**Duplication watch list** (the pairs most likely to be written twice — decide the owner, link the other):

| tempting duplicate | keep it in | the other one writes |
|---|---|---|
| capacitor energy $\frac12CV^2$ | shipped `capacitors/` | PART 15: a one-paragraph announcement + the field-energy integral as a check |
| the simple pendulum's energy method | PART 10 | PART 6: a *preview* of the same idea on a block-on-a-spring only |
| the $E=\sigma/\varepsilon_0$ conductor-surface field | PART 14 (as a Gauss result) | PART 13: only the $\sigma/2\varepsilon_0$ sheet, with a pointer forward |
| cycloid motion in crossed fields | PART 18 (full solution) | PART 16: the qualitative picture, then the pointer |
| the betatron 2:1 condition | PART 20 | PART 18: "why the geometry matters", with the pointer |
| the LC oscillator | PART 21 | PART 22: reuse with a cross-reference, no re-derivation |
| the magnetic force as a relativistic effect | PART 28 (full $\gamma$ derivation) | PART 16: the estimate-level argument, flagged as a preview |
| the Bohr orbit from a de Broglie standing wave | PART 23 (the condition) and PART 24 (the consequences) | either may state it; PART 24 owns the consequences and the spectra |
| the Hall effect | PART 18 (physics and derivation) | PART 27: the *semiconductor* application only |
| the rectifier ripple estimate | PART 22 | PART 27: reuse with a pointer |
| thermal expansion and thermal stress | shipped `heat/` (expansion) · **PART 12** (stress) | the other cites, never re-derives |
| the relativistic Doppler vs acoustic Doppler | shipped `sound-waves/` (acoustic) · **PART 28** (relativistic) | PART 25's inverse Compton may use the "moving mirror" analogy as a link |

---

## Closing note on this plan

* **Version.** v2.1 (2026-09). v1 — the four wave/optics work packages — is archived at
  [docs/plan-v1-waves-optics.md](docs/plan-v1-waves-optics.md) and complete. v2.1 adds the three
  requirements learned from the first review of this plan: the notes are **Obsidian-first** (§1.3.1), the
  Cengage chapters are **cross-checked from the PDFs that sit in this repo** (§1.13), and a chapter is
  required to **close any gap the plan leaves** rather than inherit it (§1.12).
* **Change rule.** If a chapter's section list below has to change (a discovery that a chapter is two
  chapters, or that a prerequisite is missing), edit *this file in the same commit* as the chapter and
  note it at the end of the part's entry and inside the chapter as `> [!warning] Plan amendment …`.
  A plan that is not updated when
  reality moves is how the next agent wastes a session.
* **Adding later chapters.** Append them as PART 29, 30, … in the same shape, add the row to the §0.3
  index and to the §0.4 batch table, and keep Appendix D's ledger accurate.
* **What "done" means for the whole plan.** All 28 chapters merged, each with its own gate green, the
  repo gate green, `CURRICULUM.md` covering the full reading order from units to relativity, every
  chapter's Cengage sweep recorded in its coverage map, the whole vault rendering cleanly in Obsidian
  reading mode, and a reader who has never seen the Cengage volumes able to sit an INPhO-level paper from
  these notes alone.
* **The three questions a finished chapter must answer.** (1) *Does the plan's section table exist in it?*
  (2) *Did the book sweep happen — which Cengage headings does it cover, and which did it exclude, with a
  reason?* (3) *Does it read correctly in Obsidian?* The gate answers part of (3); the coverage map and
  the README's `Beyond the plan` list are the evidence for (1) and (2).
