---
name: accuknox-asset-kit
description: Use when creating any AccuKnox external-facing asset (blog, white paper, datasheet, one-pager, deck, social post, landing copy). Tells you where the images live and how to pick the right one, how to build correct help-docs and blog links, the brand colors/fonts/templates to use, and when to scrape with Firecrawl. Trigger when the task is "write/build/draft a blog / white paper / deck / one-pager / datasheet for AccuKnox".
trigger: /ak-asset
---

# AccuKnox asset kit

Everything you need to attach the right **links** and **images** to an AccuKnox
asset, with the brand details and source locations spelled out. Read this before
writing a blog, white paper, deck, datasheet, or one-pager so you don't guess at
URLs or hunt blindly through image folders.

Repo root for all paths below: `D:\Atharva\AccuKnox\HelpDocs`.

---

## 1. Links

### Help docs: `help.accuknox.com`

Every published help page is one entry in `mkdocs.yml` under `nav:`. Build the
URL from the file path:

- Base: `https://help.accuknox.com/`
- The site uses **directory URLs**: drop the `.md`, add a trailing slash.
- `docs/<path>/page.md` → `https://help.accuknox.com/<path>/page/`
- `docs/<path>/index.md` → `https://help.accuknox.com/<path>/`

Examples:

| `mkdocs.yml` path | Live URL |
|---|---|
| `use-cases/prompt-firewall-overview.md` | https://help.accuknox.com/use-cases/prompt-firewall-overview/ |
| `use-cases/red-teaming.md` | https://help.accuknox.com/use-cases/red-teaming/ |
| `use-cases/aidr.md` | https://help.accuknox.com/use-cases/aidr/ |
| `how-to/aiml-overview.md` | https://help.accuknox.com/how-to/aiml-overview/ |
| `support-matrix/aiml-support-matrix.md` | https://help.accuknox.com/support-matrix/aiml-support-matrix/ |

Some nav entries are already full URLs (e.g. the Compliance matrix points to
`https://accuknox.com/compliance`). Use those verbatim, don't reconstruct them.

To find a page: open `mkdocs.yml`, search the nav for the topic, or read the
folder-index `docs/<section>/README.md` (it lists every page and what it covers).

### Blog and marketing: `accuknox.com`

Discovery entry point: `https://accuknox.com/sitemap_index.xml`. Child sitemaps:

| Sitemap | Content |
|---|---|
| `post-sitemap1.xml`, `post-sitemap2.xml` | **Blog posts** (`/blog/...`) |
| `white-papers-sitemap.xml` | White papers |
| `case-studies-sitemap.xml` | Case studies |
| `data-sheets-sitemap.xml`, `ebooks-sitemap.xml` | Datasheets, eBooks |
| `technical-papers-sitemap.xml`, `analyst-reports-sitemap.xml` | Technical / analyst papers |
| `cve-sitemap.xml`, `videos-sitemap.xml`, `use-cases-sitemap.xml` | CVEs, videos, use cases |

Fetch a child sitemap (WebFetch or the `firecrawl-scrape` skill) and filter the
`<loc>` URLs by slug. **Verify a URL resolves before putting it in an asset**, because
slugs change.

High-value AI-security / compliance blog URLs (verified from the live sitemap,
June 2026):

- https://accuknox.com/blog/rbi-sbom-mandate-banking-compliance-platform
- https://accuknox.com/blog/rbi-and-sebi-compliance
- https://accuknox.com/blog/stateful-prompt-firewall-guardrail-for-ai-security
- https://accuknox.com/blog/llm-prompt-firewall-accuknox
- https://accuknox.com/blog/zero-trust-runtime-security-for-ai-age
- https://accuknox.com/blog/ai-security-monitoring-production-models
- https://accuknox.com/blog/shadow-ai-security-explained
- https://accuknox.com/blog/agentic-ai-security-ai-spm
- https://accuknox.com/blog/ai-spm-tools
- https://accuknox.com/blog/chatbot-leaks-customer-data
- https://accuknox.com/blog/secure-ai-workloads

---

## 2. Images

### Where they live (in priority order)

1. **Curated demo screenshots** in `utils/brian-demo-screenshots/`
   22 clean product screenshots (dashboard, findings, AI red teaming, prompt
   firewall, runtime protection, zero-trust discovery). **Captions and a
   screenshot index are in `utils/brian-demo-screenshots/DEMO-SUMMARY.md`.**
   Use these first for polished AI-security assets. They are consistent and
   already captioned.

2. **Per-feature doc screenshots** in `docs/<section>/images/<topic>/`
   The pictures used on the live help pages. Find the right one without opening
   every PNG: each image folder has a generated `README.md` with a **"Shows"**
   column describing each file (pulled from the alt text on the page that uses
   it). Example: `docs/use-cases/images/aidr/README.md`,
   `docs/use-cases/images/modelarmor/README.md`.

3. **Icons** in `docs/use-cases/icons/*.svg` (e.g. `AIML.svg`, `aidr.svg`,
   `modelarmor.svg`, `model-safety.svg`, `mcp-security.svg`, `zt-security.svg`),
   plus `docs/<section>/icons/`.

4. **Logos** in `docs/assets/images/`: `logo-white.png`, `logo-black.png`,
   `ak-logo.png`, `logo.png`, `web-logo-dark-back.png`.

5. **Diagrams and flowcharts**, not only dashboards. Two good sources:
   - Docs diagrams: e.g. `docs/use-cases/images/aidr/1.png` (AI-DR workflow),
     `docs/use-cases/images/ai-overview/1.png` (managed vs on-prem AI map),
     `docs/use-cases/images/modelarmor/` (adversarial diagrams).
   - The **AI Security macro deck**: `utils/technical-reference/AccuKnox AI
     Security _ Macro Deck _ June_2026.pptx`. Its flowcharts are native slides, so
     render them: convert the pptx to PDF with LibreOffice, rasterise pages with
     PyMuPDF (`fitz`), search slide text for the topic, and crop the slide you
     want. Strong ones include the stateful inspection pipeline and the AI-SPM
     architecture.

### Workflow to pick an image

1. Name the topic (e.g. "AI red teaming results").
2. Find the doc: `mkdocs.yml` nav → or `docs/<section>/README.md`.
3. Open the topic's `docs/<section>/images/<topic>/README.md` and pick by the
   "Shows" caption. For AI-security assets, check `DEMO-SUMMARY.md` first.
4. Copy the chosen image into the asset's own folder. Don't hot-link into the
   docs tree, and don't move originals.

### Caption rule (always)

Every image in a **blog** and every image in a **white paper** gets a caption.
Blogs: caption directly under the image. White papers: images go in the
**appendix**, each with a figure number and caption. No uncaptioned images.

### Make screenshots clean

Product screenshots usually carry junk. Fix it before use:

1. **Crop the browser chrome.** Remove the tab strip, the URL bar, and the
   bookmarks bar. Cut just above the AccuKnox app header (the logo and
   breadcrumb) so the image starts at the product, not the browser.
2. **Trim dead whitespace.** If a screenshot has a large empty area at the
   bottom or right (a short form, a small diagram on a big canvas), crop it so
   the content fills the frame. Keep the top app header and the left nav, only
   cut empty space, and leave a small even margin.
3. **Prefer dense screenshots.** A sparse diagram on a mostly empty canvas reads
   as filler. Pick the view that fills the frame, or crop tightly to the part
   that matters.
4. **Vary the imagery.** Do not make every image a dashboard. Use flow and
   architecture diagrams (source 5 above) for conceptual points such as a
   firewall pipeline, an AI-DR workflow, or the discovery footprint, and reserve
   console screenshots for showing the product itself.

Quick approach (PIL on `py -3.11`): find the bottom-most row and right-most
column that still hold content (ignore the left nav and the right scrollbar),
then crop to that plus a ~20px margin. Work on copies, never the originals in
`utils/brian-demo-screenshots/` or `docs/`.

---

## 3. Blog deliverable spec

When the task is a blog, it ships as a finished, SEO-ready post, not a working
draft. Every blog has:

**Front matter** (YAML) with all of:

```yaml
title: "Punchy display headline"
seo_title: "Keyword-first title, <= 60 characters"
meta_description: "One sentence, 150 to 160 characters, includes the primary keyword"
slug: "lowercase-hyphenated-slug"
url: "https://accuknox.com/blog/<slug>"
primary_keyword: "the one phrase the post targets"
secondary_keywords: ["supporting", "related", "phrases"]
cover_image_prompt_claude: >
  A descriptive, natural-language prompt for an image model: subject, style,
  AccuKnox palette (#11206D / #003BF6), composition, negative space, no text.
cover_image_prompt_midjourney: >
  A keyword-dense Midjourney prompt for the same cover, ending with parameters
  such as --ar 16:9 --style raw --v 6 --no text
```

**Body rules:**

- **Punchy headings.** Each H2 is a sharp statement, not a label. "You can't
  govern a model you can't see" beats "Model inventory".
- **Links live in the text.** Hyperlink help-docs and blog references inline, on
  the words that earn them. Do not dump a "further reading" list at the bottom.
  Inlined links are what make the post SEO-rich.
- **Read like a final blog.** No internal scaffolding: no source-regulation
  paragraph numbers, no "this page", no "(para 60)", no "X asks / AccuKnox
  answers" table voice. State the point in prose.
- **Captioned images**, cleaned per the rules above, spread through the post.
- Keep to the length the brief sets (default under 1500 words) and the
  `CLAUDE.md` style rules (no dashes, plain words).

White papers are different: there, paragraph references to the source regulation
are wanted, because the document's job is a formal clause-by-clause map.

---

## 4. Brand (for designed assets: DOCX, PPTX, HTML)

Templates in `utils/doc-ppt-template/`:
`WORD_TEMPLATE_ACCUKNOX.docx`, `AccuKnox_Proposal_Template_BLANK.pptx`.

**Colors** (hex, from the real templates):

| Use | Hex |
|---|---|
| Primary navy (headers, badges) | `11206D` |
| Deep (dark panels, title bg) | `0000A0` |
| Accent purple-blue (CTAs, bars) | `4D4DD9` |
| Accent light | `5C5CFF` |
| Problem / alert red | `C80019` |
| Body text on white | `0D1B4B` |
| Caption / secondary text | `595959` |

**Fonts:** Space Grotesk (headings/labels), Inter (body). Both embedded in the
templates.

**PPTX builds (Windows):** `python-pptx` is on `py -3.11` only. Render with
PowerPoint COM or LibreOffice. `pdftoppm` is not installed, so extract PDFs with
PyMuPDF (`fitz`). (See the `accuknox-pptx-build` memory for the full recipe.)

---

## 5. When to scrape (Firecrawl)

Use the `firecrawl-*` skills or WebFetch when the repo doesn't have what you need:

- Live blog/white-paper content or fresh URLs → fetch from the sitemaps above.
- A competitor page, an analyst stat, a news item → `firecrawl-search` /
  `firecrawl-scrape`.
- Bulk-pulling a docs section → `firecrawl-crawl` / `firecrawl-map`.

Don't scrape what's already in the repo (docs markdown, screenshots, templates).

---

## 6. Pre-ship checklist

- [ ] Every help-docs link built from `mkdocs.yml` and resolves on `help.accuknox.com`.
- [ ] Every blog link taken from the live sitemap and verified.
- [ ] A blog has the full SEO front matter (seo_title, meta_description, slug, url, primary/secondary keywords, both cover prompts).
- [ ] Blog reference links are inlined in the body, not dumped at the bottom; headings are punchy; no paragraph-number scaffolding.
- [ ] Screenshots have the browser chrome cropped and dead whitespace trimmed.
- [ ] Every image has a caption (appendix figures for white papers).
- [ ] Designed assets use the brand colors and fonts above.
- [ ] Claims are backed by a doc, the demo summary, or a cited source, with no invented features.
- [ ] Writing follows the no-AI-tells style rules in `CLAUDE.md` (no dashes, no "leverage/ensure/robust/seamless", plain sentences).
