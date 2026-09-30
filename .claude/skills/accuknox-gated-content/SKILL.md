---
name: accuknox-gated-content
description: >
  Design an AccuKnox gated lead-gen PDF: a report, an ebook, a whitepaper, a
  playbook or a benchmark study. Use this skill whenever the user asks for a
  gated PDF, gated content, a lead magnet, an ebook, a whitepaper, a report PDF,
  a playbook PDF or a benchmark study for AccuKnox, or wants an existing one
  redesigned or versioned. Pulls real images from the help docs, from
  references/PRODUCT UI and from accuknox.com through Firecrawl, cites
  accuknox.com and help.accuknox.com URLs, and renders an A4 PDF with Playwright
  Chromium. Carries its own template, logo and Inter font, so it runs from
  Claude Code with no Claude project behind it.
trigger: /ak-gated
---

# AccuKnox gated content PDFs

This skill builds gated lead-gen PDFs that read like a premium editorial report.
The output is one A4 PDF file and nothing else.

Repo root for every path below: `D:\AccuKnox\help`.
Skill root: `.claude/skills/accuknox-gated-content/`.

## The Output Rule Overrides Everything Else in This Skill

1. Deliver only the final PDF file.
2. Do not send the HTML source, the page map, contact sheets, preview images, logs or design notes.
3. Write one line in chat at most, and that line is the file name.
4. Share anything else only when the user asks for it.

The repo's writing chain still loads, silently. Read
`.claude/core/runtime-contract.md`, `.claude/core/writing-rules.md` and
`.claude/core/restraint-rules.md` before you write copy. Do not print the
`Loaded` block, because the output rule outranks it for this channel.

## Ask Four Questions Before You Build

Check that you have each item below. If one is missing, ask for it. Ask one
question at a time, wait for the answer, then ask the next. Never guess.

1. The final copy, or a source document to adapt.
2. Every statistic, each with its source.
3. The CTA text and the destination URL.
4. The author or signatory for the foreword, if the piece has a foreword.

Plan the pages yourself. Do not send the plan.

For an AI security topic, also load
`references/source-of-truth/ai-security-data-points.md`. Tier D data ships in a
gated PDF. Tier I and tier A data ship only when the user confirms it.

## Eight Steps Take a Brief to a PDF

1. Run `python scripts/scaffold.py <slug>`. It creates
   `references/drafts/gated-content/<slug>/build/` with `report.html`,
   `logo.png`, `fonts/` and an empty `img/`.
2. Plan the page map from the archetypes below. A report runs 12 to 30 pages and
   a short guide runs 8 to 12. One idea per page.
3. Collect images and URLs with the three sources in the next section. Copy every
   image into `build/img/`. The PDF never loads a remote image.
4. Build the pages in `report.html` from `references/page-snippets.md`. Each
   `<section class="page">` is exactly one A4 page.
5. Run `python scripts/check.py <build>/report.html`. Fix every failure.
6. Run `python scripts/render.py <build>/report.html references/drafts/gated-content/<slug>/<file>.pdf`.
7. Read every contact sheet in `<build>/qa/`, and open a single page image in
   `<build>/qa/` when a sheet is too small to judge. Fix, then render the next
   version. Do not show this step to the user.
8. Send the PDF file and nothing else.

## Pull Images From Three Sources, by Relevance

Pick an image because it shows the exact thing the page claims. File dates never
count. `find_images.py` ranks by relevance only.

### 1. The Help Docs

Every image under `docs/` carries alt text and a page. `find_images.py` reads the
alt text, the page title and the `mkdocs.yml` nav, and prints the live
help.accuknox.com URL of the page that embeds each image.

```bash
python .claude/skills/accuknox-gated-content/scripts/find_images.py "prompt firewall" --source docs --top 10
```

```bash
python .claude/skills/accuknox-gated-content/scripts/find_images.py "prompt firewall" --source docs --top 3 --copy references/drafts/gated-content/<slug>/build/img
```

Prefer a page tagged `nav`, because that page is live on the site. Cite the
printed help.accuknox.com URL in the screenshot caption.

### 2. The Product UI Folder

`references/PRODUCT UI/` holds the product screenshots from the design team,
sorted by module: `1_dashboard`, `2_inventory`, `3_issues`, `4_AI ML security`,
`5_compliance`, `6_runtime`, `7_alerts`, `10_reports`, `CIEM`, `DSPM (Data Security)`,
`API security`, `Agent Z`, `sbom` and more. Use it when the help docs have no
clean screen for the claim.

```bash
python .claude/skills/accuknox-gated-content/scripts/find_images.py "cspm dashboard" --source ui --top 10
```

Open every candidate before you use it. Skip a screen that shows a real customer
name, a tenant ID, an email address or an unredacted hostname. The folders under
`10_reports/customer reports` need that check most.

### 3. accuknox.com, Through Firecrawl

Cloudflare blocks a plain request for an accuknox.com page, so page reads go
through the Firecrawl API. The key comes from `FIRECRAWL_API_KEY`, else from
`D:\Atharva\NOTES\.env` through `keys.py`. Image files download directly and
cost no credit.

```bash
python .claude/skills/accuknox-gated-content/scripts/site_assets.py images platform/ai-security --grep prompt
```

```bash
python .claude/skills/accuknox-gated-content/scripts/site_assets.py download https://accuknox.com/wp-content/uploads/Ai-sec-Prompt-Firewall.webp --out references/drafts/gated-content/<slug>/build/img
```

```bash
python .claude/skills/accuknox-gated-content/scripts/site_assets.py links platform/ai-security --grep blog
```

```bash
python .claude/skills/accuknox-gated-content/scripts/site_assets.py cite platform/ai-security contact-us
```

Run `cite` on every accuknox.com URL before it goes into the PDF. It prints the
status code, the final URL after redirects and the page title. Cite the final
URL, never the one you typed. The `images` command drops nav icons, logos and
badges by default. Add `--all` to keep them.

The Firecrawl MCP tool `firecrawl_scrape` works too, with `formats: ["images"]`
or `["links"]`. When a scrape fails with `Insufficient credits`, run
`python "D:\Atharva\NOTES\SCRIPTS\keys\keys.py" activate` and retry.

## The Logo Is a File, Never a Drawing

`assets/logo.png` is the official wordmark, copied from
`D:\AccuKnox\doc-ppt-template\assets\logos\accuknox-logo-light-bg.png`. It is a
2763 x 653 transparent PNG with the blue wordmark and the red to blue mark.
`scaffold.py` copies it into every build.

If that file is ever missing, take the same logo from `doc-ppt-template`, else
download `https://accuknox.com/wp-content/uploads/accuknox-logo-2.png`. Never
redraw the logo. On a navy page, add `class="logo-white"`, which turns the same
file white with a CSS filter.

## Every Page Follows One A4 Grid and One Brand Palette

### Page

Every page is A4 portrait. Margins are 24 mm top, 17 mm sides and 26 mm bottom. Each page
carries one idea, and at least one third of each page stays empty. When a page
feels full, split it.

### Type

Inter only, bundled in `assets/fonts/` at weights 200 to 700. The template loads
it with `@font-face`, so the render never falls back to a system font.

| Role | Size | Weight | Tracking | Line height |
|---|---|---|---|---|
| Cover or divider title `.h-display` | 62 to 68 pt | 600 | -0.035em | 1.02 |
| Page title `.h1` | 48 to 52 pt | 600 | -0.03em | 1.05 |
| Subtitle `.h2` | 30 pt | 600 | -0.025em | 1.1 |
| Deck under a title | 17 to 20 pt | 400, `--ink-3` | -0.01em | 1.3 |
| Hero stat `.stat` | 110 to 130 pt | 200 | -0.05em | 0.95 |
| Medium stat `.stat-m` | 64 pt | 200 | -0.045em | 1 |
| Table numerals | 36 to 44 pt | 200 | -0.04em | 1 |
| Ghost list numbers | 64 pt | 200, `--ak-sky` | -0.04em | 1 |
| Lede | 12.5 pt | 400 | 0 | 1.5 |
| Body | 11.5 pt | 400 | 0 | 1.6 |
| Chip, table header, caption | 8.5 pt | 500 to 600 | 0 | 1.3 |
| Eyebrow caps | 8 pt | 600 uppercase | 0.12em | 1.3 |

A text block is never wider than 150 mm. Long copy flows into `.cols-3`. A
heading takes 2 to 4 lines, and you break it by meaning with `<br>` so no word
sits alone on a line.

### Color

| Token | Hex | Use |
|---|---|---|
| `--ak-blue` | #1040C5 | Primary. CTAs, links, accent words, chart primary |
| `--ak-navy` | #000025 | Cover, section dividers, closing CTA |
| `--ak-red` | #D63637 | Risk, alerts, spotlight headings |
| `--ak-yellow` | #FFD900 | Section chips and highlighter only |
| `--ink` | #263238 | Headings |
| `--ink-2` | #37474F | Body |
| `--ink-3` | #607D8B | Decks, captions, meta |
| `--grad` | #FF4646 to #1040C5 | Panel top edges, underlines, flow lines, short rules |
| `--ak-sky` | #4F9CF9 | Ghost numerals and icon strokes |
| `--rule` | #CFD8DC | Hairlines and panel borders |

Page tints are #FFFFFF, #F8FAFF, #E9F8FE, #E2EEFF and #FEF7F7. Each section gets
its own tint. #FFE3E3 appears only as the light beam on a spotlight page.

### Page Furniture

1. Navy pages are the cover, the section dividers and the closing CTA.
2. Every inner page carries the logo bottom left and the page number bottom right.
3. A yellow `Section 0X` chip opens each section.
4. The yellow highlighter `.hl` marks 1 to 3 key words per heading.

### Infographics

Use very large thin numbers in white cards with a gradient top edge. Add thin
line icons, ring patterns, gradient flow lines and simple bar charts. A chart
carries two data colors at most, plus red for risk. Use no 3D, no stock photos
and no drop shadows. A product screenshot sits in a `.shot` frame with a caption
that names the screen and links its source page.

### Page Archetypes

Rotate the tints by section. Pick each page from this list.

| # | Archetype | Background | Key elements |
|---|---|---|---|
| 1 | Cover | navy | White logo, eyebrow caps, display title with one gradient-underlined phrase, deck, orbit ring art top right |
| 2 | Foreword | ice | `.h1` "Foreword", body max 150 mm, signature block. Only a real named author the user supplied |
| 3 | Methodology | white | `.h1`, lede, stacked `.panel`s pushed right, each with one thin number and a one-line label, source bottom right |
| 4 | Table of contents | ice | `.h1` about 40 mm down, yellow chips, 21 pt titles, right-aligned page numbers |
| 5 | Section divider | navy | White logo top left, yellow chip, display title, deck, gradient flow lines at the bottom |
| 6 | Numbered findings | aqua or blue | Lede, `.h1` with `.hl`, `.nlist` rows with ghost number, line icon and 2-line body |
| 7 | Big-number table | white | `.h1` with `.hl`, lede, `.ntable` with 36 pt thin values, takeaway paragraph |
| 8 | Hero stat | blue or rose | Letter chip, `.h1`, deck, one centered `.panel` with a 120 pt blue number and a bold caption |
| 9 | Chart and columns | white | Chip, `.h2`, a `.panel` with horizontal bars, `.cols-3` body |
| 10 | Product spotlight | rose | Light-beam triangle, eyebrow "AccuKnox capability spotlight", red `.h1`, `.cols-3` body, "See how it works" link |
| 11 | Product screenshot | ice or white | Chip, `.h1`, deck, one `.shot` frame, caption with the source URL |
| 12 | Recommendation | aqua | Bold recommendation line, 2 to 3 option rows with a line icon and an h3 |
| 13 | Quote or pull stat | navy | One large quote or stat with attribution. Only real, approved quotes |
| 14 | Closing CTA | navy | White logo, gradient short rule, `.h1` CTA headline, deck, primary and ghost buttons, URL and copyright |

The structural reference is the Factors.ai report "From Benchmarks to
Blueprints": huge headings, one idea per page, thin numerals as the main
infographic, tinted pages by section. Do not copy its illustrations, its serif
font or its colors.

## Every Number Carries Its Source on the Same Page

1. Write in the AccuKnox voice: authoritative, prevention first, technical and accessible. Use CNAPP, CSPM, CWPP, ASPM, AI-SPM, eBPF, LSM and K8s without expansion.
2. Use no em dash, en dash, semicolon, hyphenated compound, hashtag or emoji in the copy.
3. Drop filler such as "cutting-edge", "streamline", "game-changer" and "powerful".
4. Write headings in sentence case, with no colon.
5. Every number carries its source on the same page. Never ship unverified data.
6. Never fabricate a quote, a customer, an author or a metric. Name no unannounced product, price or partner.
7. Every CTA link carries `utm_source=gated-pdf`, `utm_medium=pdf` and `utm_campaign=<campaign-slug>`.
8. Remove all placeholder text, such as TBD, [INSERT] and `{{ }}`.

`check.py` catches rules 2, 3, 4, 7 and 8, a stat with no source line on its
page, a missing image file and any font other than Inter. It cannot judge rules
1, 5 and 6, so read the copy for those yourself.

## Four Render Checks Run Silently Before Delivery

`render.py` renders with Playwright Chromium and then checks four things.

1. The page count equals the section count, and every page is A4.
2. Inter is the only embedded font.
3. No element spills off its page or runs into the footer.
4. Every page rasterizes into `<build>/qa/`.

After the script, read every contact sheet by eye. Look for an orphan word in a
heading, a body block wider than 150 mm, a highlighter over more than 3 words,
two hero numbers on one page and a page less than one third empty. Fix each one
before delivery.

## A New Version Never Overwrites an Old One

1. Name the file in lowercase with hyphens, dated and versioned, for example `2026-10-01-runtime-security-report-v1.pdf`.
2. Save it in `references/drafts/gated-content/<slug>/`.
3. Never overwrite an earlier version. `render.py` refuses an existing name, so raise the `-vN` suffix.
4. Do not publish, send or upload the PDF anywhere before the user reviews it.

## Nine Files Make the Skill Self-Contained

| File | Job |
|---|---|
| `assets/template.html` | The HTML shell with every class and brand token |
| `assets/logo.png` | The official AccuKnox logo |
| `assets/fonts/` | Inter at weights 200 to 700, with its OFL license |
| `references/page-snippets.md` | One HTML snippet per archetype |
| `scripts/scaffold.py` | Creates a build folder |
| `scripts/find_images.py` | Ranks help docs and Product UI images by relevance |
| `scripts/site_assets.py` | Reads accuknox.com through Firecrawl for images and URLs |
| `scripts/check.py` | Checks the HTML against the content rules |
| `scripts/render.py` | Renders the PDF and runs the QA checks |
