# PPT Output

Build workspace for AccuKnox slide decks generated via python-pptx.

## To start a new deck

1. Copy `AccuKnox_Proposal_Template_BLANK.pptx` and rename it for your project.
2. Copy `build.py` and update the three path variables at the top:
   - `SRC` — master brand template (leave as-is)
   - `OUT` — where the generated `.pptx` lands (inside this folder)
   - `BLANK` — your renamed copy of the blank template
3. Run `py -3.11 build.py` to generate the deck.

## Utility scripts

| Script | Purpose |
|---|---|
| `build.py` | Main deck builder — edit slide content here |
| `render.ps1` | Exports every slide as a PNG via PowerPoint COM — pass `-Pptx` and `-Out` args |
| `final_check.py` | Prints slide titles and counts em/en dash hits |
| `verify.py` | Same dash check with per-slide detail |

For `final_check.py`, `verify.py`, and `render.ps1`: update the output path variable at the top to point to the `.pptx` you just built.

## Template inspection tools

`.tmp_tpl/` holds one-off scripts for probing the master template's shape layout and placeholder indices. Run these against `SRC` if you need to map slide layouts before writing a new `build.py`.

## What goes here

- Generated `.pptx` files (output per project)
- `render/` subfolder when you run `render.ps1` (PNG previews, gitignored)

The master brand template lives one level up at `utils/` root — see [`utils/README.md`](../README.md) for the full index.
