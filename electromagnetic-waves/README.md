# Electromagnetic Waves — Part 3

**Status:** complete against the six Part 3 coverage groups in `plan.md`; original Markdown-first course by `arena-agent`. The map in §1.3 states the scope precisely: this is not a page-by-page audit of every exercise in the supplied scanned textbook.

Start with **[Electromagnetic-waves.md](Electromagnetic-waves.md)**. It is the authoritative source, not an export from an HTML edition. It uses standard `$...$` / `$$...$$` math, collapsible solutions, YAML frontmatter, and seven standalone local SVGs. Six rendered Mermaid figures (chapter map, Ampère paradox, E–B–k triad, inverse-square graph, radiation-pressure cosines, triage) follow the template in [docs/obsidian-plugin-workflow.md](../docs/obsidian-plugin-workflow.md) §2. No external images, fonts or network resources are needed; a Markdown viewer with MathJax/KaTeX support typesets equations.

## Roadmap and prerequisites

Vectors/cross products + differential/integral calculus → flux/circulation → Gauss/Faraday/Ampère → displacement current → Maxwell waves → energy and momentum → radiation pressure → spectrum → optical wave models.

Mechanical waves are useful preparation but not required: the scalar wave equation is reintroduced. Charge storage and linear material response are reviewed. The text is self-contained; no missing String Waves or Sound Waves files are linked as prerequisites.

| Section | What you learn |
|---|---|
| 1 | Motivation, symbols, frames, models and syllabus coverage map |
| 2 | Capacitor paradox; Maxwell integral/differential laws in vacuum/matter; both curl derivations; phase/transversality; Poynting and stress; normal/oblique/spherical forces; spectrum |
| 3 | Ten worked exemplars, supplementing six concept checks embedded in §2 |
| 4 | Impedance matching, standing waves, isotropic radiation pressure, conducting-medium limit |
| 5 | Fifteen examiner traps and their corrective replies |
| 6 | Triage, formula routes, constants and submission checklist |
| 7 | 36-question, 180-minute, 180-mark paper; complete collapsible solutions and rubrics |
| 8 | Compact printable formula sheet with validity conditions |

## Files

| File | Purpose |
|---|---|
| [Electromagnetic-waves.md](Electromagnetic-waves.md) | Master: eight sections, 52 solved prompts (6 checks + 10 exemplars + 36 paper questions) |
| [Paper.md](Paper.md) | Generated paper without solutions or answer key, for printing |
| [Solutions.md](Solutions.md) | Generated separate solutions and marking scheme |
| [Formula-sheet.md](Formula-sheet.md) | Generated standalone revision sheet |
| `assets/figures/fig-001.svg`–`fig-007.svg` | Original labelled capacitor, field, pressure, sphere, spectrum and standing-wave diagrams |
| `tools/export.py` | Regenerate the three print extracts deterministically |
| `tools/check.py` | Structural, math-delimiter, link/SVG, export and rubric validation |
| `tools/test_content.py` | Negative tests for missing solutions, figures, validity conditions, delimiters and rubric marks |
| `tools/test-tex.js` | Optional strict rendering check using the repository’s vendored KaTeX (or `KATEX_PATH`) |
| `tools/test_physics.py` | Recompute worked numbers and independent physical limiting checks |

## Checks and editing

From the repository root:

```bash
python3 electromagnetic-waves/tools/export.py
python3 electromagnetic-waves/tools/check.py
python3 electromagnetic-waves/tools/test_physics.py
node electromagnetic-waves/tools/test-tex.js
python3 tools/test_check_all.py
python3 tools/check_all.py --update electromagnetic-waves
python3 tools/check_all.py
```

From a copied topic folder, `python3 tools/check.py` and `python3 tools/test_physics.py` work without other topics. `tools/export.py --check` detects stale print extracts. The legacy HTML `mathfix.py` normaliser is not used: it operates on HTML markup, not this Markdown-first source. The checks enforce balanced dollar delimiters/braces/environments; a separate KaTeX rendering pass can use the repository's vendored renderer. No structural validator proves the physics, so review derivations as well as running checks.

Registry counts refer **only to the master**, not its generated extracts. `words` means whitespace-separated source tokens (including math); `math_spans` counts inline plus display math occurrences; `display_formulas` counts display blocks, not distinct physical laws. Question/solution counts include checks and exemplars once each. The paper is 8×3 + 8×4 + 12×3 + 8×11 = 180 marks.

## Deliberate boundaries

- No full relativistic moving-mirror/Doppler treatment.
- No material-momentum (Abraham–Minkowski) resolution; pressure problems use vacuum momentum.
- No general anisotropic/dispersive/nonlinear propagation or oblique Fresnel derivation.
- No antenna radiation-pattern/power derivation or multipole expansion; qualitative source mechanisms only.
- No quantum derivation of photon energy; `hf` is identified as quantum input.
- No Mie/Rayleigh scattering theory, diffuse-sphere recoil or asymmetric thermal-emission model.

The adopted spectrum boundaries are explicit conventions, not universal exact physical cutoffs. Absorption, specular reflection and transmission are distinguished throughout. Repository-wide Parts 1/2 creation and Part 4's optics audit are outside this work package.
