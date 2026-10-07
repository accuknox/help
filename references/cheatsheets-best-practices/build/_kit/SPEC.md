# AccuKnox best practices cheat sheet kit

One kit, ten modules. Every cheat sheet follows this spec so the set reads as one series.

Repo root: `D:\AccuKnox\help`. Kit root: `references/cheatsheets-best-practices/`.

## Folders

| Path | Holds |
|---|---|
| `build/_kit/` | This spec, `template.html`, the scraped sample live pages |
| `build/<module>/` | `report.html`, `img/`, `fonts/`, `logo.png`, `qa/`, `research.md`, `package.md`, `email.html`, `social/` |
| `output/` | Final deliverables only: the PDF, the HTML email, the LinkedIn image, the web form image |

Never write a final deliverable into `build/`. Never write scratch files into `output/`.

## Skill and rules

1. Read `.claude/skills/accuknox-gated-content/SKILL.md` and follow it. Its design rules, palette, type scale and copy rules apply.
2. Read `.claude/core/runtime-contract.md`, `.claude/core/writing-rules.md` and `.claude/core/restraint-rules.md` before you write copy.
3. Scripts live in `.claude/skills/accuknox-gated-content/scripts/`. `scaffold.py` writes to the old drafts path, so do not run it. The build folder is already scaffolded.
4. Copy rules that `check.py` enforces: no em dash, en dash, semicolon, hyphenated compound, hashtag or emoji. Headings in sentence case with no colon. Every stat has its source on the same page. Every CTA link carries `utm_source=gated-pdf&utm_medium=pdf&utm_campaign=<module>-cheat-sheet`.
5. Never fabricate a stat, a quote, a customer or a metric. Every number comes from an opened source.

## The 12 page map

Use the CSS in `build/_kit/template.html` (copy the whole `<style>` block into your `report.html`). The reference implementation is `build/ai-security/report.html`. Match its look: page 3 to 8 use its module page pattern (`.chip`, `.h2` with `.hl`, `.deck`, `.shot`, `.dd` do and don't columns, `.fix` box).

| # | Page | Background | Content |
|---|---|---|---|
| 1 | Cover | navy | White logo, caps eyebrow `<Domain> best practices cheat sheet`, display title of 3 short lines with one `.ul` phrase, deck of one sentence, orbit ring art |
| 2 | The problem | rose | Chip `The problem`, `.h1` that states the risk, lede of 2 sentences, then `.prob` with 3 sourced stat cards in red thin numerals. Each card names its source with a link |
| 3 | Why it keeps happening | white | Chip `Root causes`, `.h2`, `.nlist` of 3 or 4 root causes with an inline SVG `.icon` each, one short body each. Cite any number on the page |
| 4 | The map | ice | Chip `Start here`, `.h1`, lede, one platform or architecture image in `.shot`, then `.mods` list of the 5 or 6 practice pages with page numbers |
| 5 to 10 | Practices | rotate white, aqua, blue, white, aqua, rose | One practice per page. Chip `Practice 0N`, `.h2` claim, `.deck`, one product screenshot in `.shot`, `.dd` Do (4 items) and Don't (3 items), `.fix` box "How AccuKnox closes the gap" with a help.accuknox.com link |
| 11 | Gap check | white | Chip `Gap check`, `.h1`, lede, `.gap` table of 6 rows: If this is true, AccuKnox capability, First step |
| 12 | Book a demo | navy | White logo, gradient rule, `.h1` CTA headline, deck, primary button `Book a demo` to `https://accuknox.com/demo/?utm_source=gated-pdf&utm_medium=pdf&utm_campaign=<module>-cheat-sheet`, ghost button to the module docs on help.accuknox.com, then a short proof row (2 to 4 facts from accuknox.com, each cited, for example analyst recognition at `https://accuknox.com/analyst-recognition/`) and `accuknox.com · © 2026 AccuKnox, Inc.` |

12 pages is the target. 11 to 14 is allowed when the domain needs it. One idea per page, one third of each page empty.

## Screenshots must be sharp

The user rejected the first AI guide because some images were blurry. Blur has two causes, and both are banned.

1. A source image too small for its frame. A full width `.shot` is 176 mm. Use an image at least 1600 px wide for full width, at least 900 px for a half width frame. Check with `python -c "from PIL import Image;print(Image.open('x').size)"`.
2. A crop that zooms in. `object-fit:cover` on a short frame scales a small region up. Prefer `.shot.full` (natural height) or crop the source file with PIL to the region you want, then show it at natural aspect ratio. After a PIL crop, the cropped width must still clear the limits above.

When the best screen is too small, look for a larger copy first: `references/PRODUCT UI/` holds design team exports, often 2880 px wide. Only if no larger copy exists, run the `upscale` skill on it (it keeps the picture, it does not redraw it). Then open the result and check it.

Skip any screen that shows a real customer name, tenant ID, email address or unredacted hostname.

Find images:

```bash
python .claude/skills/accuknox-gated-content/scripts/find_images.py "<query>" --source docs --top 10
python .claude/skills/accuknox-gated-content/scripts/find_images.py "<query>" --source ui --top 10
```

## Research

Write `build/<module>/research.md` first. Use Firecrawl (`firecrawl search`, `firecrawl scrape`, or the `site_assets.py` script) and WebSearch to find 4 to 8 current, public, citable data points about the problem in this domain. Good sources: Verizon DBIR, IBM Cost of a Data Breach, Gartner public press releases, CSA, Datadog State of reports, Wiz or Orca public cloud risk reports, GitGuardian State of Secrets Sprawl, Salt Security State of API Security, OWASP, CISA, Red Hat State of Kubernetes Security, Sysdig usage report, Microsoft Digital Defense or State of Cloud Permissions Risks. For each data point record: the exact number, the exact wording, the publisher, the year and the URL you opened. Use only a number you read on the page. If a number cannot be confirmed, drop it.

When `site_assets.py` or `firecrawl` fails with `Insufficient credits`, run `python "D:\Atharva\NOTES\SCRIPTS\keys\keys.py" activate` and retry.

Also read the module's help docs pages under `docs/` so every do and don't is true to the product. Never claim a feature the docs do not show.

## Render

```bash
python .claude/skills/accuknox-gated-content/scripts/check.py references/cheatsheets-best-practices/build/<module>/report.html
python .claude/skills/accuknox-gated-content/scripts/render.py references/cheatsheets-best-practices/build/<module>/report.html references/cheatsheets-best-practices/output/2026-10-07-<slug>-v1.pdf
```

`render.py` refuses an existing name, so raise `-vN` for each new render. Read every contact sheet in `build/<module>/qa/`, and open single page images at full size to judge sharpness. Fix and re-render until clean. Delete superseded PDFs of your own module from `output/` so only the final version stays. Never touch another module's files.

## Package

Write `build/<module>/package.md` with exactly these sections. The live sample is `https://accuknox.com/cheatsheets/ai-security-best-practices-guide/` and `build/_kit/sample-live-page.md`.

### 1. Web page metadata

| Field | Rule |
|---|---|
| Eyebrow | `CHEAT SHEET` |
| Title (H1) | `<Domain> Best Practices: Do's and Don'ts Guide` style, AP title case, under 65 characters |
| Meta title | Under 60 characters, ends with `| AccuKnox` |
| Meta description | 140 to 155 characters, states what the reader gets |
| Slug | lowercase hyphenated, for example `cspm-best-practices-guide` |
| URL | `https://accuknox.com/cheatsheets/<slug>/` |
| Tagline (H2) | One sentence of 4 to 8 words, like "Secure every AI model, agent and prompt." |
| Subtitle blurb | One sentence for the cyan box, like "This free guide provides clear do's and don'ts for six AI security controls, plus a gap checklist." |
| What's inside | Exactly 5 bullets, each under 70 characters |
| What's new | One line on what this guide adds |
| Form image | `output/<slug>-form-image.png` |
| OG image alt text | One sentence |
| Primary keyword and 3 secondary keywords | Plain search phrases |

### 2. Email

A short promo email. Subject under 50 characters, preview text under 90 characters, body of 3 to 5 short lines and one button. Write the copy into `package.md`, and write the HTML version to `build/<module>/email.html`: table based, inline CSS, 600 px wide, AccuKnox logo from `https://accuknox.com/wp-content/uploads/accuknox-logo-2.png`, the PDF cover thumbnail optional as a hosted placeholder comment, one blue `#1040C5` button to the landing URL with `utm_source=email&utm_medium=email&utm_campaign=<module>-cheat-sheet`, and a hidden preheader span. Copy the final email to `output/<slug>-email.html`.

### 3. LinkedIn post

Load the `accuknox-linkedin-post` skill and follow its AccuKnox voice and its link in comments rule. 60 to 120 words. A hook line that names the problem with one sourced number, 3 short lines of value, a CTA to comment or grab the guide. Put the link in a separate "First comment" block. No emoji or hashtag in the body unless the skill says otherwise, then follow the skill.

### 4. Images

1. Form image. Render page 1 of the PDF as a PNG at 2x with a soft angled stack look, or simply the cover at 1200 px wide, into `output/<slug>-form-image.png`.
2. LinkedIn image. 1200 x 1200 PNG built with HTML and Playwright from the brand palette: navy ground, logo, eyebrow `CHEAT SHEET`, the title, the cover thumbnail. Save to `output/<slug>-linkedin.png`. The `social-cards` skill shows the method, but use AccuKnox branding, never Atharva's personal branding.

## Final report back

Reply in under 120 words: final PDF path and page count, the screenshots used with their pixel widths, the data points used with sources, anything you could not verify.
