# Magnetism + EMI + AC — short notes (77 sheets: 58 JEE + 19 extensions)

Dense teacher-style handwritten revision sheets built from the repository's complete [`magnetism/Magnetism.md`](../../magnetism/Magnetism.md) and [`emi-ac/Emi-ac.md`](../../emi-ac/Emi-ac.md) modules (the original chapters are unchanged). Physical meaning, governing equations, short derivations, assumptions, traps and checks — not a formula-only dump. Every card is packed near capacity. Same format as the other chapters' short notes: navy body, teal headings, yellow result bands, red warnings, faintly ruled white pages.

**Layout:** [index.html](index.html) (offline gallery) · [SCOPE.md](SCOPE.md) coverage and classification · [SOURCE-AUDIT.md](SOURCE-AUDIT.md) corrections · [VERIFICATION.md](VERIFICATION.md) checks · [PRINTING.txt](PRINTING.txt) print settings.

## Downloads

| Deliverable | File |
|---|---|
| **Everything (77 PNGs)** | **[magnetism-all-pngs.zip](magnetism-all-pngs.zip)** |
| All sheets, one A4 page each | [magnetism-short-notes.pdf](magnetism-short-notes.pdf) |
| JEE Main + Advanced (58 sheets) | [magnetism-jee-pngs.zip](magnetism-jee-pngs.zip) · [magnetism-jee.pdf](magnetism-jee.pdf) |
| Olympiad / extensions (19 sheets) | [magnetism-olympiad-pngs.zip](magnetism-olympiad-pngs.zip) · [magnetism-olympiad.pdf](magnetism-olympiad.pdf) |
| Individual sheets | `JEE-01-lorentz.png` … `JEE-58-rectifiers.png`, `Olympiad-01-relativity.png` … `Olympiad-19-emi-estimates.png` in this folder |

A4 portrait · one sheet per page · print with **Fit**, not Fill/Crop · PNGs are 2480 × 3508 at 300 DPI.

## Reading order

Part I (JEE) first, then Part II. The boundary is syllabus relevance and usefulness, not difficulty: hard core applications stay in JEE; the extensions add specialised derivations and engineering. JEE sheets 01–29 cover the magnetism module (Lorentz force → sources of B → forces and dipoles → matter → Earth); sheets 30–58 cover induction and AC from the EMI+AC module (flux and Faraday → motional EMF and Lenz → rails and machines → induced fields, betatron, eddy effects, motors → inductance and transients → LC and energy → AC, reactance, phasors, LCR and resonance → power, parallel circuits, complex methods → transformers and rectifiers). Part II adds the specialised extensions of both modules, including the Faraday disc, betatron orbit theory, magnetic braking, persistent flux, launchers, transmission-line surges, driven transients, impedance matching, radio oscillators and EMI estimates.

## Rebuild (fully reproducible)

```bash
pip install -r requirements.txt
python author_content.py     # teacher content -> sheets.json (77 sheets, deterministic)
python render_sheets.py      # -> 77 A4 PNGs + layout-checks.json
python build_exports.py      # -> 3 PDFs + 3 ZIPs + index.html + manifests
python revalidate.py         # -> verification-recheck.json (independent physics checks)
python test_exports.py       # -> verification-results.json (exports, links, models)
```

Licensed font: Patrick Hand (SIL OFL, [fonts/OFL.txt](fonts/OFL.txt)).
