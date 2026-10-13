# Shared Engine for Detailed Comparison PDFs

One engine builds the long, capability-by-capability comparison PDFs for prospects, so each one
carries the same A4 cover, type, colors and table layout. Cover and body render as separate PDFs
and merge, so the cover has no header or footer.

This is not the 4-page sales battlecard. For that format use `.claude/skills/accuknox-comparison-writer/references/battlecard-pdf.md`.

## Where Each Part Lives

| What | Where |
| --- | --- |
| The engine | `references/competitive/pdf-engine/engine.py` |
| One folder per comparison set, holding its data, builder and final PDFs | `references/competitive/battlecards/<set>/` |
| The index of everything competitive | `references/competitive/INDEX.md`, generated |

## A New Set Takes Four Files

Copy `references/competitive/battlecards/appsec-snyk-veracode/` to `battlecards/<new-set>/`, then change:

1. `data.py` returns `sections` in the shape documented at the top of `engine.py`.
2. `build.py` holds the SPEC: vendors, themes, strengths, competitor sources, docs links and jobs.
3. The raw data export (a sheet or workbook) sits in the same folder.
4. `README.md` records the data source, every correction made to it and the open items.

Use lowercase kebab-case for the PDF file names, as `references/README.md` requires. Then run:

```bash
cd references/competitive/battlecards/<new-set>
python build.py
python ../../build_index.py
```

## Rules the Engine Does Not Enforce

- Index 0 in `vendors` is AccuKnox. Every row needs one cell per vendor.
- Every competitor cell with a claim needs a source in `sources`. The engine cannot judge fairness.
- Check each competitor claim against the vendor's current docs. A source sheet goes stale.
- Run the slop scorer on the text before sharing. The cover and the tables carry prose too.
- Never add a footer note. The footer shows the page number only.

## Three Packages and a Network Connection Are Required

`playwright` with Chromium, `pypdf` and `Pillow`, plus network access for Google Fonts.
