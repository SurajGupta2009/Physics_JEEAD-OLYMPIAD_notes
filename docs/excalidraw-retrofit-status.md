# Excalidraw diagram retrofit — status and hand-off

**Updated:** 2026-10-01
**Working branch:** `arena/01a0ee1c-physics-jeead-olympiad-notes`
**State:** all 31 course chapters have native diagram companions — 544 scenes total (366 pre-existing, 81 converted from retained SVGs in slots 22–24, 97 drawn from DIAGRAM briefs in slots 25–31). Structural gates pass; native Obsidian rendering/edit-save-reopen remains unverified.

## Repository-wide verification (final)

`python3 tools/verify_all_diagrams.py` checks every chapter registered in `topics.json` and currently reports **31 chapters · 544 scenes · 0 problems**:

- every DIAGRAM brief in every master has exactly one native embed, and the embeds resolve to parseable, primitives-only scenes under `_obsidian/excalidraw/` with finite, on-canvas geometry;
- every `figures.json` records those ids, in topic order, with the pinned renderer and provenance, and no scene file is orphaned;
- every master is a **strict superset of its committed original** — an insert-only line diff shows that no original line was removed or rewritten — and each chapter's Mermaid `figures` records are unchanged;
- no raster images or `image` elements anywhere.

Regeneration is verified end to end: all eight builders (`tools/build_excalidraw_batch*.py`, `build_excalidraw_waves_thermal.py`, `build_excalidraw_heat_capacitors.py`, `build_excalidraw_current_magnetism_emi.py`, `build_excalidraw_em_optics.py`, `build_excalidraw_remaining.py`) rerun with **zero changed files** over 606 masters/manifests/scenes. `python3 -m unittest discover -s tools -p 'test_*.py'` reports **30 passing tests**, `python3 tools/check_all.py` passes every topic gate, and the offline site rebuilds with plugin embeds stripped.

## Latest batch — Electromagnetic Waves → Geometrical Optics → Wave Optics

| Master | Course slot | New scene IDs | Count |
|---|---:|---|---:|
| `electromagnetic-waves/Electromagnetic-waves.md` | 22 | D21.1–7 | 7 |
| `geometrical-optics/Geometrical-optics.md` | 23 | D22.1–46 | 46 |
| `wave-optics/Wave-optics.md` | 24 | D23.1–28 | 28 |

**447 native scene files** (366 previous + 81 new), embedded beside retained local SVGs. D21–D23 continue the drawing series, not frontmatter part or course numbers. The existing inline SVG beside Geometrical Optics §3.3 is preserved verbatim. All six Mermaid records in each manifest remain unchanged.

Build: `python3 tools/build_excalidraw_em_optics.py`. Rebuilding overwrites manual edits to these scene files. The shared converter gained support for non-rendered SVG title/description metadata and editable polyline paths; prior builders’ deterministic-output tests continue to pass. SVG gradients/hatches and marker shapes are approximated, inline tspan styling is flattened, and long annotations are moved below the geometry. This is not a pixel-exact export.

### Targeted corrections

- Geometrical Optics D22.43: analytically traced spherical-mirror rays, R = 20 cm, with exact intercepts for heights 2/4/6 cm. D22.45: solar diameter 0.533° versus radius 0.267°, consistent thin-lens limb-ray geometry, separate paraxial concentration and étendue limits. D22.46: legible method-selection cards instead of cramped SVG columns.
- Wave Optics D23.9/11: analytic interference curves with explicit normalisation; unequal 2:1 amplitudes give minimum/maximum ratio 1/9. D23.15: quarter-wave film has π phase difference, not one wavelength; exact lossless Fresnel reflectance has a zero at the design wavelength for the matching film index. D23.26: explicitly rectangular spectrum and sinc visibility, without claiming a universal revival at twice the coherence length. D23.28: legible method-selection cards.
- Companion labels clarify biprism small-angle assumptions, Lloyd’s mirror screen distance, diffraction angular half-width, and minor source typos. The originals remain unchanged; these are companion corrections, not silent edits to the authoritative text or SVGs.

### Validation and remaining acceptance

- **24 unit tests pass**: scene coverage, expected native primitives, deterministic output, no embedded raster, analytic sample values, exact master preservation after removing additive blocks, unchanged original assets and Mermaid provenance.
- All-topic consistency gates pass; three chapter gates now include native companion checks. EM Waves’ generated paper/solutions/formula sheet remain current without re-exporting them. Offline site rebuilt; SVGs and briefs retained, plugin embeds stripped.
- Approximate primitive contact sheets were generated; sampled EM/optics sheets were reviewed and several crowded/incorrect panels redrawn. These projections do not reproduce native text metrics, opacity, rotations or dash styles faithfully. Comprehensive physics/visual acceptance is still pending for inherited diagrams.
- **Native Obsidian rendering and edit/save/reopen remain unverified.** This batch is generated and structurally validated, not plugin-certified or a complete independent physics audit.

## Source-asset note (Sound Waves)

Ten `sound-waves/assets/figures/*.svg` files contained malformed XML attributes (`stroke-width:1.5"` instead of `stroke-width="1.5"`). Those attribute quotes were repaired so the files parse; geometry, labels and physics are unchanged. No other chapter's SVG assets were modified, and every converted scene keeps its source SVG beside it.

## Latest batch — Photoelectric Effect → Special Relativity (course slots 25–31)

| Master | Course slot | Scene IDs | Count |
|---|---:|---|---:|
| `photoelectric-effect/Photoelectric-effect.md` | 25 | D23.1, 3, 4, 7–16 | 13 |
| `atomic-structure/Atomic-structure.md` | 26 | D24.2, 3, 4, 6, 8–16 | 13 |
| `x-rays/X-rays.md` | 27 | D25.1, 3–10, 13–16 | 13 |
| `nuclear-physics/Nuclear-physics.md` | 28 | D26.1, 2, 4–9, 11–18 | 16 |
| `semiconductors/Semiconductors.md` | 29 | D27.1–18 | 18 |
| `communication-systems/Communication-systems.md` | 30 | D100.1–12 (source numbering) | 12 |
| `special-relativity/Special-relativity.md` | 31 | D28.1–12 | 12 |

**544 native scene files** (447 previous + 97 new) covering all remaining course chapters. These seven masters previously had no figure assets or native scenes: every scene was **drawn from its existing DIAGRAM brief**, and the brief ids in the masters are preserved exactly, gaps included, so the inherited `D100.x` numbering in Communication Systems is unchanged. Native scenes sit beside each non-SVG brief; every original `*Show:*`, `*Search:*` and `*Used in:*` line and all six Mermaid FIGURE records per chapter are untouched.

Build: `python3 tools/build_excalidraw_remaining.py [topic-slug ...]`. Regeneration replaces manual scene edits. The shared deterministic converter needed no new SVG features for this batch.

### Diagrams worth a note

- Several briefs describe curves and tables rather than pictures: plotted against real equations where practical (Planck peak shift, Wien displacement, Shannon capacity, Compton shifts, allowed beta spectrum, secular/transient activities, Shockley law) and labelled as schematic wherever sampled data would be misleading.
- Two briefs are drawn with departures the brief could not supply: the Michelson–Morley interferometer now has an explicit arm layout and beam path, and the half-adder/gate block is a functional symbol set with a four-row truth table.
- Kirkendall-style false claims were not copied into scenes: the source's H/He⁺/Li²⁺ ladders use independent vertical scales, the p-p chain sketch names the two ³He branch, and Bi209-free "four-decimal" Balmer agreement is replaced by an explicit measured-versus-vacuum table with its 0.2–0.4 nm differences. The original prose keeps its own wording; nothing in the masters was rewritten.

### Validation and remaining acceptance

- **28 unit tests pass**, including seven new tests: expected scene counts and ids per chapter, primitives-only scenes with finite bounded geometry, deterministic regeneration over 111 files, byte-level brief preservation versus `HEAD`, unchanged manifest figure records, and sampled analytic curve values.
- All seven chapter gates now also validate their native companions; `tools/check_all.py --update` passes every topic. Offline site rebuilt with plugin embeds stripped and every original asset retained.
- Approximate contact sheets were reviewed for all 97 scenes; crowded or inaccurate panels were redrawn (beam-balance scale, ³He branch, cloud chamber, resistivity and mixing panels, sun/earth geometry, and label placement).
- **Native Obsidian rendering and edit/save/reopen remain unverified** for this batch, and the scenes are illustrative companions, not a certified physics audit of the inherited prose.

## Previous batch — Current Electricity → Magnetism → Induction, Inductance & AC

| Master | Course slot | IDs | New scenes |
|---|---:|---|---:|
| `current-electricity/Current-electricity.md` | 19 | D19.1–26 | 26 |
| `magnetism/Magnetism.md` | 20 | existing D16.1–30 | 30 |
| `emi-ac/Emi-ac.md` | 21 | existing D20.1–22 | 22 |

**366 native scenes total** (288 previous + 78 new). IDs are chapter-local: Magnetism D16 and Thermodynamics D16 have different slug-qualified filenames. Original Markdown prose, questions, solutions, briefs, SVG assets and Mermaid remain intact. Current Electricity retains its SVG fallback; Magnetism and EMI keep their original searchable briefs on the offline site.

Regenerate with `python3 tools/build_excalidraw_current_magnetism_emi.py` (overwrites manual scene edits). New manifests record native provenance and existing Mermaid identifiers. Chapter gates validate native embeds and scene structure; Current Electricity validates its Markdown companions without running its HTML exporter.

### Corrections and remaining acceptance

- Current Electricity: analytic matching-power curves (12/20), absolute power ledger (13), normalised RC voltage/current axes (17), and explicit local exponential thermistor thermal model (25). Other scenes are editable conversions of legacy SVGs, not a claim that all legacy physics has been independently audited.
- Magnetism: clockwise positive-charge orbit with B out; compound-loop tangent leads follow arc current; moving-frame wire uses transformed net line density rather than the original brief’s unsupported electron-spacing claim.
- EMI: energy triangle uses flux linkage versus current, not back EMF versus current. Betatron profile demonstrates the area-flux condition only, not stable focusing. Several complex briefs are represented by simplified schematic panels and equations; detailed apparatus/measurement annotations may need refinement.
- Automated checks: 20 unit tests pass, covering this batch’s counts, native primitives, idempotence and exact master preservation after removing additive blocks. All-topic gates pass; offline site rebuilt.
- Approximate primitive projections were generated for review; these are not native plugin renders. No live Obsidian edit/save/reopen test has been performed. Complete visual/brief-detail acceptance is still pending, so this is a generated and structurally validated retrofit, not final visual certification.

## Previous batch — Heat → Electrostatics → Capacitors

The owner explicitly chose the next three course slots **including already-completed Electrostatics**, rather than skipping it to reach Current Electricity. That batch did not touch Current Electricity.

| Master | Course slot | Scene IDs | Result |
|---|---:|---|---|
| `heat/Heat.md` | 16 | D17.1–D17.25 | 25 new native companions |
| `electrostatics/Electrostatics.md` | 17 | D13.1–D13.26 | Existing 26 scenes validated, untouched |
| `capacitors/Capacitors.md` | 18 | D18.1–D18.32 | 32 new native companions |

**288 scenes total** across all batches (231 previous + 57 new). D17/D18 continue the drawing series, not course slots or frontmatter part numbers. Heat has 25 SVG assets, not the 24 stated by its old README.

Each new source has one brief and Obsidian embed beside its first SVG occurrence. Both manifests preserve their six Mermaid records and add drawing provenance. The chapter validators now check native Markdown scene wiring as well as the legacy HTML. The originals remain the portable fallback, and the offline site retains SVGs and searchable briefs without leaking plugin-specific links.

## Generation

Run `python3 tools/build_excalidraw_heat_capacitors.py` from the repository root (standard library only). It first validates Electrostatics and then rebuilds Heat/Capacitors companions deterministically. Like the previous builders, regeneration **overwrites manual scene edits**: preserve or port manual changes before rerunning it.

The converter reuses the previous batch's primitive/path helpers, adding native polygons, ellipses, rotated labels/rectangles, CSS colour mixes, fallback colours and flattened inline text spans. Source styles inherited only from the HTML page are replaced by explicit light-theme defaults; Heat fig-002's invalid `Nonepx` font size falls back to 13px. All scene labels and shapes are editable—no SVG/raster image elements, remote assets or embedded files. Long annotations move below the diagram. This is not a pixel-identical SVG importer: font styling, hatch textures, marker shapes and HTML map links are simplified.

## Physics and layout review

Temporary local projections of native primitives were inspected, not screenshots from Obsidian. Source review identified errors that should not be copied verbatim. Analytic replacements are explicitly marked in their briefs and manifests:

- **Heat D17.5/6:** inward clamp forces/compressive stress; higher-expansion brass on the outer bimetal arc.
- **Heat D17.11/12:** steeper temperature gradient in lower-k material; straight temperature line versus ln r for cylindrical conduction.
- **Heat D17.16:** exponential cooling with exact half-life, τ and ln(10)τ markers.
- **Heat D17.18:** Planck spectra with correct Wien peak ordering on a log-wavelength axis. Each curve is explicitly normalised to its own peak, not misleadingly drawn as absolute equal-height emission.
- **Heat D17.22:** depth profile with the actual exponential attenuation and phase lag.
- **Capacitors D18.1/9/11:** a single connected battery/plate circuit, correct coaxial field jumps and 1/r region, and force-curve tangency at the remaining gap 2g₀/3.
- **Capacitors D18.14:** an explicitly connected infinite ladder with real capacitor symbols and its 0.618C input capacitance.
- **Capacitors D18.21/22:** consistent positive-loss Debye semicircle and hysteresis labels distinguishing remanence from saturation.
- **Capacitors D18.23/24/25:** connected divider circuits and correct DC/RC/compensation relations; RC current has no spurious factor of C.
- **Capacitors D18.28:** clear plate-distance convention and induced pulse area qΔx/d for a partial traversal, not always q.
- **Capacitors D18.31:** distinguishes MEMS minimum/maximum merging from the volume-preserving Rayleigh shape instability; corrects the claim that the ideal Taylor apex field stays finite.

Smaller companion-only wording fixes include the steam/ice mass balance, Q-axis plateau units, critical-radius resistance competition, the slab half-thickness convention, the 3/6/3 capacitor-cube edge groups, and critical-point/thermal-film caveats. The originals are **unchanged**, including their pre-existing errors. Other scenes are schematic reconstructions, not a comprehensive re-audit of every legacy physics assertion.

## Checks completed

- Heat, Electrostatics and Capacitors local gates: pass.
- `python3 tools/check_all.py`: every registered topic passes; no registry recount needed for these HTML-first chapters.
- `python3 -m unittest discover -s tools -p 'test_*.py'`: **17 tests pass**, including six new tests for colour/rotation/polygons, coverage, native editability, analytic coordinates and deterministic regeneration.
- Regeneration test hashes all scene files plus the target masters/manifests and Electrostatics files; a second run makes no changes.
- Stripping only the newly inserted brief/embed blocks reproduces the original Heat/Capacitors Markdown exactly. Source SVGs and Electrostatics have zero diff against HEAD.
- Pinned Obsidian Excalidraw plugin 2.27.3: passes check.
- Offline site rebuilt; `git diff --check`: passes.

## Remaining manual acceptance / next hand-off

Open Heat, Electrostatics and Capacitors in Obsidian with the pinned plugin. Check reading-mode embeds, rotated labels (especially D18.15), dense layouts, and edit/save/reopen a label and curve. **Actual Obsidian font metrics, rendering and round-trip editing have not been verified here.** Geometry projections are only a partial layout check and are not committed.

Do **not** run the Heat/Capacitors HTML-to-Markdown exporters; they would discard the native diagram additions and existing Mermaid/frontmatter work. Course slots after this batch are **Current Electricity → Magnetism → Induction/Inductance/AC**; no work on those chapters was done in this batch.

---

# Previous batch: String Waves / Sound Waves / Thermodynamics

**Updated:** 2026-09-29
**Working branch:** `arena/01a0ee1c-physics-jeead-olympiad-notes`
**State:** 54 editable companion scenes implemented for the three requested chapters; automated gates pass. Live Obsidian rendering/editing remains unverified.

## Current batch — course slots 13–15

The owner explicitly chose the course-spine order after Elasticity: **String Waves → Sound Waves → Thermodynamics**. These are not plan Parts 13–15. Existing Electrostatics D13 is untouched. The drawing-ID series continues with D14–D16; these IDs are **not course slots or frontmatter part numbers**.

| Chapter master | Course slot | New scene IDs | Count |
|---|---:|---|---:|
| `string-waves/String-waves.md` | 13 | D14.1–D14.4 | 4 |
| `sound-waves/Sound-waves.md` | 14 | D15.1–D15.15 | 15 |
| `thermodynamics/Thermodynamics.md` | 15 | D16.1–D16.35 | 35 |

- All 54 source SVG figures now have native `.excalidraw.md` companions in `_obsidian/excalidraw/`. Total across batches: **231** scenes.
- Each companion is embedded after its source figure's first occurrence, with an explicit source/reading brief. The repeated String Waves fig-001 remains in both original locations; its scene is embedded once. Sound fig-014 occurs earlier in reading order than fig-007; IDs follow source filenames, not heading order.
- Original prose, questions, solutions, six Mermaid figures per chapter, and source SVG references are retained. HTML-to-Markdown exporters were **not** run.
- Repaired 28 malformed `stroke-width` attributes in ten existing sound SVG files (colon changed to equals); no other legacy SVG geometry changed.
- `figures.json` retains Mermaid provenance and adds native scene paths and source references. Both HTML-first chapter gates now also validate their Markdown scene wiring.

## Generation and review

Run `python3 tools/build_excalidraw_waves_thermal.py` (standard library only). It uses the existing deterministic Scene builder. Native text, rectangles, circles, arrows and multipoint lines remain independently editable; no scene contains an image element or embedded image file.

The converter handles these sources' CSS variables/compound classes, nested translate/scale transforms, quadratic/cubic Béziers, smooth continuations and elliptical arcs. Curves are sampled into editable polylines. Long annotations are moved below their plots rather than clipped. Missing HTML theme colours use light-theme fallbacks. Hatch patterns become grey fills; SVG marker shapes become native arrowheads; HTML branch links are not reproduced. This is an editable companion, not a pixel-identical SVG importer.

Source review found errors that should not be blindly copied. Analytic overrides in the builder provide:

- **D14.1:** string endpoint forces along the actual local tangents.
- **D15.1:** consistent sinusoidal displacement and `ΔP = −B ∂s/∂x` quadrature.
- **D15.5:** closed/open pipe displacement harmonics obeying the boundary conditions.
- **D15.8:** a resultant beat signal bounded by its actual envelope.
- **D16.14:** a self-consistent monatomic cycle ledger with `ΣQ = ΣW = ½P₀V₀`; the original SVG's numerical table is inconsistent.
- **D16.16:** decreasing isotherm and steeper adiabat through a common state (the original left panel had positive slopes).
- **D16.34:** efficiency bars scaled to their numerical values and the correct Otto temperature-extremes bound.

These overrides are marked in their chapter briefs/manifests. Other scenes are schematic reconstructions, not a new comprehensive physics audit of the legacy material. The originals are retained for provenance, including their pre-existing errors; consult the corrected native companion where noted. A few terminology edits remove the misleading clickable-map promise and distinguish throttling from Joule free expansion.

## Validation

- All three chapter gates pass, including fixed scene coverage, IDs, provenance, source SVG XML, native JSON and no embedded images.
- `python3 tools/check_all.py --update` passes for every registered topic and refreshes String Waves' Markdown counts.
- `python3 -m unittest discover -s tools -p 'test_*.py'`: **11 tests pass**, including six new path/CSS/transform/wiring/reproducibility tests.
- Pinned Obsidian Excalidraw plugin **2.27.3** check passes.
- Offline site rebuilt with `tools/md_site.py`: original SVGs and new briefs are visible; plugin embeds are omitted by the existing renderer. Actual embeds follow the established extensionless target convention (`…excalidraw` resolving to `…excalidraw.md`), so no renderer change was necessary.
- Geometry review used temporary SVG/PNG projections of the scene primitives. These are not Excalidraw/Obsidian screenshots and are not committed. A browser-based Excalidraw render attempt was blocked by unavailable Chromium system libraries/network package access.
- `git diff --check` passes. Generation is deterministic and scene contents are compared against the committed JSON by the test suite.

## Remaining manual acceptance

Open the three masters in Obsidian with the pinned plugin enabled. Check embed rendering and label layout at normal zoom (particularly dense thermal maps), open a scene, edit a label/curve and save/reopen it. **Live Obsidian rendering, round-trip editing and font metrics have not been tested here.** Do not run the HTML-to-Markdown exporters on Sound Waves or Thermodynamics; they would erase the added Markdown content.

---

# Previous batch: Elasticity / Electrostatics

**Updated:** 2026-09-29
**Working branch:** `arena/01a0ea90-physics-jeead-olympiad-notes`
**State:** scoped Parts 12–15 retrofit is implemented; code and scene validation pass; live Obsidian rendering remains unverified.

## Scope and interpretation

The request for “the next four chapters” did not specify a numbering scheme. This work followed the repository's plan-part organization: Part 12 is Elasticity, while plan Parts 13, 14, and 15 are consolidated into the single `electrostatics/Electrostatics.md` master. That master records `plan_parts: [13, 14, 15]` and retains its existing D13 numbering. Accordingly, this batch adds D12.1–D12.14 and D13.1–D13.26; it does **not** invent separate D14 or D15 IDs. Confirm this interpretation with the owner if “four chapters” meant four course slots instead.

## Completed

- Created **40 native, editable Excalidraw Markdown scenes** and embedded each immediately below its corresponding brief:
  - Elasticity: 14 scenes, D12.1–D12.14.
  - Electrostatics: 26 scenes, D13.1–D13.26.
- Added per-chapter `figures.json` provenance; Electrostatics also preserves provenance for its ten existing Mermaid figures.
- Connected both target chapter gates to the shared Excalidraw validator. Updated chapter metadata, READMEs, the Obsidian workflow documentation, repository structure/readme counts, and the registry.
- Refreshed the offline site from current Markdown. The site generator intentionally omits plugin-specific Excalidraw embeds while retaining the searchable briefs; the native scenes are for Obsidian.
- Audited for stale D1–D11 retrofit references; none were found.
- The repository now contains **177** scoped D1–D13 scenes in `_obsidian/excalidraw/`: 137 from the earlier batches plus these 40.

### Physics and diagram review notes

The scene-source review caught and corrected several geometry/sign issues before generation, including equal-area section comparisons and bending-stress signs in D12, and field-component directions, charge-equilibrium geometry, flux projection/solid-angle intersections, and radial-path arrows in D13. D12.9's potential curve and local quadratic fit were also corrected to stay on-canvas and show the intended well shape.

## Validation completed

- Ran `python3 tools/build_excalidraw_batch_12_15.py`; all 40 builders completed.
- `python3 elasticity/tools/check.py` — passed (14 briefs/scenes; no raster images).
- `python3 electrostatics/tools/check.py` — passed (26 briefs/scenes; ten Mermaid figures; no raster images).
- `python3 tools/check_all.py` — all registered topics passed.
- `python3 -m unittest discover -s tools -p 'test_*.py'` — 5 tests passed.
- `python3 tools/obsidian_plugins.py --check obsidian-excalidraw-plugin` — pinned v2.27.3 check passed.
- Parsed all 177 scene documents; the 40 new scenes had no JSON or canvas-bounds issues.
- Rebuilt the offline site with `tools/md_site.py`; `git diff --check` passed.

## Remaining work

1. **Verify in Obsidian.** Open the repository as a vault with the pinned Excalidraw plugin enabled; check that D12/D13 embeds render in reading mode, fit their embeds, and open as editable drawings. The plugin-version check is not a substitute for a live app/render test. Fix any runtime or layout issues found, then rerun the chapter and repository gates.
2. **Finish the literal full-repository read.** Relevant chapters, generators, checkers, manifests, documentation, and repository-wide gates were reviewed, but every file and source PDF has not been read line by line.
3. **Continue the retrofit (superseded).** This early note ended at D13; the retrofit has since covered all 31 course chapters — see the repository-wide verification section at the top.
4. **Confirm the chapter interpretation** if the intended four chapters were course slots 12–15 rather than plan Parts 12–15 as described above.

## Key files

- Generator: `tools/build_excalidraw_batch_12_15.py`
- Chapter masters: `elasticity/Elasticity.md`, `electrostatics/Electrostatics.md`
- Scene sources: `_obsidian/excalidraw/elasticity-D12-*.excalidraw.md`, `_obsidian/excalidraw/electrostatics-D13-*.excalidraw.md`
- Provenance: `elasticity/figures.json`, `electrostatics/figures.json`
- Shared validation: `tools/excalidraw_checks.py`
