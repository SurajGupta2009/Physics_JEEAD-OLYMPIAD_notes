# Verification — regenerated thermodynamics edition

## Automated results

Final run: **PASS, 1,016 assertions including 49 representative physics/model checks**. Machine-readable numerical values are in [verification-results.json](verification-results.json). These are concrete checks, not certification that every line or source exercise is perfect.

- 28 sheets: independently numbered JEE 01–21 and Olympiad/extensions 01–07; JEE-first combined order; no stale PNGs.
- 112 concept cards, 248 displayed mathematical blocks, 56 native figure panels.
- Every PNG: 2480 × 3508 pixels, 300 DPI within metadata rounding, indexed colour; content bounds checked against the ~10.6 mm safe inset.
- Every card's measured height fits without body shrinking: body 11.52 pt, explanations 11.04 pt. Measurements: [layout-checks.json](layout-checks.json).
- All display math pre-parsed with the same mathtext normalisation used to render it. Font coverage checked for handwritten prose, titles, subtitles, card headings, source footers and takeaways; renderer also guards annotation, tick-label and legend bounds.
- Three PNG-only ZIPs: CRCs, exact ordered filenames and byte-for-byte original PNG contents.
- Three PDFs: exact A4 portrait media boxes, 28/21/7 pages, ordered title bookmarks with correct destinations, exactly one full-resolution image per page. Each PDF image's decoded indices and palette equal its source PNG: no hidden lossy JPEG conversion or resampling.
- Offline gallery: all 28 sheets and local hyperlinks resolve. Documentation/download navigation is also checked locally before publication.
- [asset-manifest.json](asset-manifest.json): SHA-256 and byte length of all 28 PNGs and six ZIP/PDF bundles. [build-environment.json](build-environment.json) records the rendering libraries.
- Detailed Markdown and HTML SHA-256 equal their preserved originals. `python thermodynamics/tools/check.py` reports **ALL GOOD: 943 inline maths, 71 display maths**. That source gate is separate from the 1,016 export assertions; it validates source markup/structure, not every physics claim.

The 49 numerical/model checks cover expansion stress/fitting, Maxwell speeds and mean free path, capacity mixtures, room electrical work, basic path heat, adiabatic versus isothermal work, polytropic and sudden compression, cyclic efficiencies, refrigeration/cascades, entropy and finite bodies, gas stiffness/sound, atmospheric scales/escape, vdW parameters and coexistence, radiation/albedo, and useful tank availability/blowdown. The Maxwell tie line satisfies equal-pressure and equal-area conditions numerically; it was not positioned by eye.

## Visual review and refinements

All 28 page compositions were inspected in seven review montages. All 56 diagram panels were inspected separately in four larger figure montages. Full-resolution samples included the isotherm/adiabat derivation sheet, real-gas criticality/coexistence sheet and final first-law sheet. This is not a claim of a line-by-line, full-resolution inspection of every pixel on every page.

Final ink-bound checks caught small handwriting negative side bearings and low source footers. Titles/subtitles were inset slightly and footers raised, rather than reducing the body font or relaxing the safe-margin check. All 28 final pages then passed. The one overflowing calorimetry paragraph was edited concisely without removing its vessel/insulation/equilibrium assumptions. A test initially used 100 C where the mixing example says 80 C; the independent test inputs were corrected, while the already-correct notes remained unchanged. PDF palette comparison uses raw original bytes, not a text-decoded interpretation of its binary palette.

Native diagrams use analytical data for curves; sketches label model assumptions. Bimetal layers have concentric arcs with the higher-alpha material outside; heating scales the hole and plate consistently; piston force arrows are distinct. No final export is a screenshot of the HTML gallery or a generated image of mathematical text.

## Limits and publication

See [SOURCE-AUDIT.md](SOURCE-AUDIT.md) for source corrections and model qualifications and [SCOPE.md](SCOPE.md) for concept-level membership decisions. No official-current-syllabus audit, exact air phase boundary, fire-safety verdict, universal atmospheric lifetime or exhaustive correctness guarantee is made. The detailed chapter retains its unedited physics text; corrections are explicit in this edition.

The user's authorisation covers committing, pushing, creating a PR and merging into main. Source/build tools were pushed before export completion to provide an early remote checkpoint. Final publication is verified against the merged remote main tree, including PNGs, ZIPs and the three explicitly tracked PDFs (the repository's general PDF ignore rule is not allowed to omit these requested deliverables). Print **A4 portrait, one sheet per page, Fit—not Fill/Crop**.

## Concurrent main reorganisation

Main was reorganised by PR #25 during authoring. The first merge attempt correctly stopped on a documentation conflict. This branch merged the updated main, preserved its Capacitors and Rigid_Body_Dynamics folders, and adopted `Short notes/Thermodynamics/` with direct `JEE-`/`Olympiad-` PNG filenames. PNG pixels were not changed by these renames; archives, bookmarks, gallery, hashes and tests were rebuilt/rechecked. The shared folder-structure gate also passes.
