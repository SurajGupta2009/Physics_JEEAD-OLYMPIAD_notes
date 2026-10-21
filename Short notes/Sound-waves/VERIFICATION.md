# Verification — sound waves short notes

All checks below are **representative, not exhaustive**. Machine-readable details:
`layout-checks.json` (per-card pixel fill), `asset-manifest.json` (byte sizes +
SHA-256 of every deliverable), `build-environment.json` (tool versions).

## Geometry and print format (checked in `revalidate.py` + renderer asserts)

- Every sheet: exactly 2480×3508 px, 300 DPI (≈10.5 mm safe margin on all sides) —
  exact A4 portrait at print, one sheet per page.
- Renderer hard asserts (all passed): no card overflow; no equation wider than the
  card after ≥0.82 scaling; no clipped diagram text/legends/ticks; no unsupported
  prose glyph (Patrick Hand charmap); all display mathtext pre-parses cleanly.
- Card fill (render-measured): 336 cards, min 0.27 / median 0.80 / max 0.97 of the
  card body; 271/336 cards ≥ 0.70. Body text is 11.5 pt equivalent and is never
  shrunk.

## Deliverables (checked in `revalidate.py`)

- `sound-all-pngs.zip`: 84 PNGs in reading order (JEE 60 first, then Olympiad 24);
  `sound-jee-pngs.zip` / `sound-olympiad-pngs.zip`: correct subsets in order.
- `sound-short-notes.pdf`: 84 A4 pages with bookmarks (JEE first); `sound-jee.pdf`
  60 pages; `sound-olympiad.pdf` 24 pages; all pages exact A4 (595.28×841.89 pt).
- `index.html` links every PNG and all four docs; `asset-manifest.json` matches the
  current bytes of every asset.
- Source chapter `sound-waves/Sound-waves.md` unchanged (SHA-256 prefix `d2edcf5e`).
- Numbering: JEE 01–60 and Olympiad 01–24, continuous and independently labelled
  on every sheet header and in the PDF outlines.

## Physics (checked in `test_exports.py`, ~40 representative assertions)

All passed. Highlights:

- Speed of sound: 331.3 m/s at 0 C, 343.2 m/s at 20 C, dv/dT = 0.585 m/s per K;
  Newton isothermal vs Laplace factor √γ = 1.1832; He 1007.7 m/s (γ = 5/3),
  H₂ 1260.5 m/s; paper Q2 (M = 32 g/mol, γ = 1.4, T = 300 K) 330.3 m/s.
- Intensity chain (worked Q3: 0.1 W isotropic at 10 m): I = 7.958e-5 W/m²,
  ΔP₀ = 0.2559 Pa (Z = 411.6), β = 79.0 dB; 0 dB reference 2.87e-5 Pa;
  doubling laws 3.01 / 6.021 dB.
- Pipes and end correction (Q4): e = 0.6r = 1.2 cm; closed f 100.9 → 98.61 Hz;
  open ratio L/(L+2e) = 0.9725.
- Resonance tube (Q5): λ = 2(l₂−l₁) = 0.672 m, v = 344.06 m/s, e = 3 mm by both
  formulas ((l₂−3l₁)/2 and λ/4 − l₁); paper Q9 337.9 m/s.
- Doppler pair (f = 1 kHz, u = 30 m/s): 1096.77 Hz (source) vs 1088.24 Hz
  (observer), second-order gap 8.54 Hz; echo 1193.55 Hz vs 1176.47 linear;
  combined case (paper Q36) 1161.29 Hz.
- Mach (M = 2, h = 10 km): α = 30°, ground distance 17.32 km, boom delay 25.47 s
  (envelope), slant sound time 58.82 s, emission 8.49 s before the pass.
- Corrected glide slope 11.76 Hz/s (and the wrong 3.9 Hz/s value is absent from the
  sheets); Kundt v_gas = 400 m/s; paper Q16 750 Hz (first overtone labelled
  correctly), Q17 8 (×10⁻⁴ W/m²), Q20 330 m/s.
- Content assertions: the corrected resonance-tube relations (2f(l₂−l₁),
  (l₂−3l₁)/2, l = λ/4 − e) are present in the delivered sheets.

## Known limitations

- Inline-mathtext wrapping uses a 5% height safety factor in packing; a small number
  of cards finish below 50% fill where item boundaries make balancing impossible
  without reordering content (order is preserved).
- Diagram geometry was checked by the renderer's clipping asserts and visual
  inspection of representative panels; not every panel was manually proofed.
- PDF bookmark titles use the sheet titles; very long titles wrap in some viewers.
