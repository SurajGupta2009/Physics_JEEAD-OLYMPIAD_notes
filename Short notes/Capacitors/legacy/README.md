# legacy - the retired Capacitors edition (v1)

Frozen copy of the **JEE + Olympiad, two-column, 17-sheet** edition that was
replaced on 2026-10-24. Nothing here is rendered by the current build and no page
in the live edition links to it. It is kept so a decision can be reversed.

| file | what it is |
|---|---|
| `sheets-v1-jee-olympiad.json` | the 17-sheet source (11 JEE + 6 Olympiad) |
| `render_sheets_v1.py` | the two-column 2x2 card-grid renderer |
| `build_exports_v1.py` | 3 PDFs + 3 ZIPs, JEE / Olympiad / combined |
| `test_exports_v1.py` | the v1 gate |

## Rebuilding the old edition

```bash
cd "Short notes/Capacitors"
cp legacy/sheets-v1-jee-olympiad.json sheets.json      # overwrites a tracked file
cp legacy/render_sheets_v1.py render_sheets_v1.py
cp legacy/build_exports_v1.py build_exports_v1.py
python3 render_sheets_v1.py && python3 build_exports_v1.py
git checkout -- sheets.json && rm render_sheets_v1.py build_exports_v1.py
```

Paths inside the v1 scripts assume they sit in the chapter folder, which is why
they are copied out rather than run in place. The old PNGs are not kept: the v1
renderer rebuilds them from the v1 JSON.
