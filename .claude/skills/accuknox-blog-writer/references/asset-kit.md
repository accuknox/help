# Asset kit

Where the pictures live, which one to pick, and the brand values a designed
asset needs. Merged here from the retired `accuknox-asset-kit` skill on
2026-08-23. The link rules that used to sit alongside it now live in
`references/source-of-truth.md`, so this file covers images and brand only.

All four AccuKnox writing skills read this file. Repo root for every path:
`D:\Atharva\AccuKnox\HelpDocs`.

## Four image sources, in the order you should try them

| # | Source | What it holds | Reach it with |
| --- | --- | --- | --- |
| 1 | `media/INDEX.md` in this skill | 298 product-UI screenshots, diagrams, booth art, event photos, 279 of them images | `scripts/drive_sync.py search` |
| 2 | `references/brian-demo-screenshots/` | 22 curated, pre-captioned demo screenshots | `DEMO-SUMMARY.md` in that folder |
| 3 | `docs/<section>/images/<topic>/` | The pictures on the live help pages | the generated `README.md` in each image folder |
| 4 | The AI Security macro deck | Native flowcharts, rendered from the pptx | `references/technical-reference/` |

Source 1 is the eye candy and is new. Sources 2 and 3 are the product truth and
match what a customer sees in the console today. Prefer a real screenshot over a
generated illustration for anything a reader might try to reproduce.

## Source 1, the PRODUCT UI Drive folder

[PRODUCT UI on Drive](https://drive.google.com/drive/folders/1wrvtlSCSB7hZfWKd_7V7BUtf3R7FbZk2)
is the marketing screenshot library. It is not in the help docs and it is not on
the website. Forty folders, organised by product area: `1_dashboard`,
`4_AI ML security/PROMPT FIREWALLING`, `CIEM/Graph View`, `DSPM (Data Security)`,
`sbom`, `security graph`, `Agent Z`, `Booth Banner`, `AccuKnox Event Images`.

The index is text and lives in the repo. The binaries do not, because 246 MB of
PNG has no business in git history. They mirror to
`D:\Atharva\AccuKnox\product-ui-assets`, and `ACCUKNOX_MEDIA_MIRROR` overrides
that path.

```bash
cd .claude/skills/accuknox-blog-writer
python scripts/drive_sync.py search "prompt firewall"     # find by name
python scripts/drive_sync.py pull --folder "CIEM/Graph View"
python scripts/drive_sync.py check                        # staleness
python scripts/drive_sync.py check --deep                 # diff against Drive
python scripts/drive_sync.py index                        # rebuild the manifest
```

**Run `check` at the start of any asset-heavy job.** It exits 1 once the manifest
passes 90 days, which is the quarterly cadence agreed for this folder. Say so in
your reply rather than working from a stale index in silence.

The filenames are honest but terse. `vlcsnap-00003.png` is a video frame, and
`AISPM Report-Prompt Firewall.png` is a report page. Read the pixel dimensions in
`media/INDEX.md` before you commit to one: a 5760x3240 report render crops well,
and a 1902x908 video frame does not survive a 2x upscale.

## Source 2, the curated demo screenshots

`references/brian-demo-screenshots/` holds 22 clean shots covering the dashboard,
findings, AI red teaming, prompt firewall, runtime protection and zero-trust
discovery. `DEMO-SUMMARY.md` in that folder carries the caption for each one.
Use these first for a polished AI-security asset, because they are consistent and
already described.

## Source 3, the help-doc screenshots

Every image folder under `docs/` carries a generated `README.md` with a **Shows**
column, pulled from the alt text on the page that uses the file. That column is
how you pick without opening 40 PNGs.

```bash
cat docs/use-cases/images/aidr/README.md
cat docs/use-cases/images/modelarmor/README.md
```

Icons sit in `docs/use-cases/icons/*.svg` (`AIML.svg`, `aidr.svg`,
`modelarmor.svg`, `model-safety.svg`, `mcp-security.svg`, `zt-security.svg`).
Logos sit in `docs/assets/images/`: `logo-white.png`, `logo-black.png`,
`ak-logo.png`, `web-logo-dark-back.png`.

## Source 4, diagrams out of the deck

`references/technical-reference/AccuKnox AI Security _ Macro Deck _ June_2026.pptx`
holds the stateful inspection pipeline and the AI-SPM architecture as native
slides. Convert the pptx to PDF with LibreOffice, rasterise with PyMuPDF
(`fitz`), search the slide text for your topic, and crop the slide. `pdftoppm` is
not installed on this machine.

## Clean a screenshot before you use it

1. **Crop the browser chrome.** Cut the tab strip, the URL bar and the bookmarks
   bar. Start the image just above the AccuKnox app header so it opens on the
   product, not on Chrome.
2. **Trim dead whitespace.** Find the bottom-most row and right-most column that
   still hold content, ignoring the left nav and the scrollbar, then crop to that
   plus a 20px margin.
3. **Prefer a dense frame.** A sparse diagram on an empty canvas reads as filler.
4. **Vary the imagery.** Not every picture is a dashboard. Use a flow or
   architecture diagram for a conceptual point and reserve console shots for
   showing the product.
5. **Redact before you crop.** No tenant name, customer domain, real IP, token or
   account id survives into a published asset. This is the safety rule in
   `.claude/core/runtime-contract.md` and nothing overrides it.

PIL on `py -3.11` does steps 1 and 2 in a few lines. Work on copies. Never touch
an original under `docs/` or `references/brian-demo-screenshots/`.

To enlarge, use the machine-wide upscaler rather than an image model:

```bash
python "D:\Atharva\NOTES\SCRIPTS\upscale\upscale.py" <file-or-dir>
```

The default `-m screen` model preserves glyphs. `-m photo` invents plausible
letters instead of the real ones, which makes any screenshot with text
untrustworthy.

## Captions and alt text

Every image in a published asset carries a caption. The caption says what the
picture proves, not what it is.

- Weak: `AccuKnox dashboard`
- Strong: `Model-layer findings by check type, and the five deployed models ranked by issue count`

In a blog the caption sits directly under the image, in italics. In a white paper
the images go to an appendix with a figure number. Alt text follows the same
rule and never opens with `a screenshot of`.

## Brand

Templates: `references/doc-ppt-template/WORD_TEMPLATE_ACCUKNOX.docx` and
`AccuKnox_Proposal_Template_BLANK.pptx`.

| Use | Hex |
| --- | --- |
| Primary navy, headers and badges | `11206D` |
| Deep, dark panels and title backgrounds | `0000A0` |
| Accent purple-blue, CTAs and bars | `4D4DD9` |
| Accent light | `5C5CFF` |
| Problem or alert red | `C80019` |
| Body text on white | `0D1B4B` |
| Caption and secondary text | `595959` |
| Bright accent used in image prompts | `003BF6` |

Fonts: Space Grotesk for headings and labels, Inter for body. Both are embedded
in the templates.

`python-pptx` lives on `py -3.11` only. Render a deck with PowerPoint COM or
LibreOffice, and extract PDF pages with PyMuPDF.

## Image prompts, when no real picture fits

Write the prompt into the draft as a blockquote placeholder. Never generate or
commit a cover file.

```markdown
> **Image prompt (inline 1):** a four-layer stack diagram, infrastructure at the
> base rising to agents at the top, AccuKnox navy `#11206D` on white with
> `#003BF6` accents, flat vector, no text labels, generous negative space.
>
> *Caption: The four layers of AI risk and the controls applied at each.*
```

Front matter carries two cover prompts, one natural-language for Claude and one
keyword-dense for Midjourney ending in `--ar 16:9 --style raw --v 6 --no text`.

## Related

- `references/source-of-truth.md`, links and where facts come from
- `media/INDEX.md`, the PRODUCT UI file list
- `scripts/drive_sync.py`, the sync and search tool
