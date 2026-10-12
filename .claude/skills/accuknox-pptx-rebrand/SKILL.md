---
name: accuknox-pptx-rebrand
description: "AccuKnox master presentation skill. Creates new AccuKnox slide decks or redesigns existing ones from pasted or uploaded content (notes, docs, PDFs, old .pptx) into an editable .pptx in the October 2026 AccuKnox style, with Inter type, red to blue gradient accents, larger readable body text, icons and logos. Use it for /accuknox-pptx-rebrand, /ak-presentation and every AccuKnox deck, slides, pitch deck, partner deck, webinar deck, sales or product presentation, or any request to build, redesign, restyle, refresh or fix a PowerPoint, even when the user does not name this skill. It takes priority over the generic pptx skill."
---

# AccuKnox presentation builder

You turn source material into an AccuKnox deck that looks like it came from the same design team as the October 2026 Partnership Program deck. The output is always an editable `.pptx` built with native shapes and text, so the team can tweak it in PowerPoint or Google Slides.

Two modes:

- **Create**: the user pastes or uploads content (notes, a doc, a PDF, a brief) and you design the deck.
- **Redesign**: the user uploads an existing deck and you rebuild it in this style, keeping every fact.

The reference deck set body text at 9 to 11pt, which was hard to read on shared screens. This skill raises the floor to 14pt. At the same time, decks should stay short: aim for 20 slides or fewer. The way to satisfy both is editing, not shrinking. Cut fluff, merge slides that repeat a point, move narration into speaker notes, and keep every number, name, link and image.

---

## Files in this skill

| Path | What it is |
|---|---|
| `scripts/ak.js` | Helper library on top of pptxgenjs. Brand tokens, slide frames (cover, content, section, closing), cards, stats, tables, steps, icons, and `finalize()` which writes native red to blue gradients. Use it for every deck. |
| `references/layouts.md` | Layout catalog with code for each slide pattern and when to pick it. Read it before storyboarding. |
| `assets/logo-white.png`, `assets/logo-blue.png` | AccuKnox logo for dark and light slides |
| `assets/brand-logos-iconify.json` | About 2,000 full colour company and product logos (AWS, Azure, Google Cloud, OpenAI, Kubernetes, Red Hat, NVIDIA and more), used through `ak.brandLogo()`. CC0, see `brand-logos-LICENSE.txt`. |
| `scripts/cover_art.js` | Topic based outline artwork for covers (ai, cloud, code, network, compliance, runtime). Used through `ak.coverArt(topic)`. |
| `assets/cover-globe.png` | Photo globe, only for global or partner network topics |
| `assets/g2-rating-badge-1.png`, `assets/g2-rating-badge-2.png`, `assets/cloud-marketplaces.png` | Cover proof badges |
| `assets/certifications-strip.png` | CNCF, SOC 2, AWS, Nutanix strip for the closing slide |
| `assets/secured-by-accuknox-badge.png` | Partner badge |

`ak.js` resolves `assets/` relative to itself, so require it by absolute path from wherever this skill is installed. Find it with `find / -path "*accuknox-pptx-rebrand/scripts/ak.js" 2>/dev/null | head -1`.

If the assets folder is missing (for example the skill was saved without its bundled files), extract logos from any AccuKnox `.pptx` the user supplies: unzip it, look in `ppt/media/`, view the candidates, and copy the white and blue wordmarks into an `assets/` folder next to a copy of `ak.js`. If no AccuKnox deck is available, ask the user to upload one. Never redraw the AccuKnox logo by hand.

---

## Workflow

### 1. Read the source

- Pasted text: use as is.
- `.pptx`: `markitdown file.pptx` for text, and render thumbnails (`soffice --headless --convert-to pdf`, then `pdftoppm -r 50 -png`) so you see diagrams, charts and logos the text dump misses. Pull reusable images (customer logos, product screenshots, architecture diagrams) from `ppt/media/`.
- `.pdf` or `.docx`: extract text, and view pages that hold diagrams.

Capture every number, name, claim and source link. These are the facts you must carry through. Never invent metrics, quotes, customers or pricing. If the source has a gap a slide needs, leave the slide out or mark the specific missing item for the user rather than filling it.

Facts from your own knowledge (a regulation's penalty, a market size, a CVE date) can strengthen a slide, but only with a source line on the slide, and you must list each one in your reply under a heading "UNVERIFIED, please confirm" so a human checks it before the deck goes out.

### 2. Confirm only what you cannot infer

Build straight away when the audience, purpose and content are clear. Ask one short question when something material is unclear, such as who the audience is (partner, prospect, analyst, internal) when it changes the story, or whether a redesign should also cut or reorder content. Default for redesigns: keep slide order and every fact, restyle and tighten wording.

### 3. Storyboard

Read `references/layouts.md`. Then write a one line plan per slide: layout, eyebrow, title, and what goes on it. A typical deck runs cover, agenda, content sections with section dividers for decks over about 12 slides, and a closing CTA slide.

Rules that keep slides readable at the new type sizes:

- One idea per slide. The title states the takeaway in plain words.
- **Slide budget: 20 or fewer.** Count the storyboard before building. If it runs over, reduce in this order:
  1. Cut fluff: restated titles, generic claims with no number or name behind them, filler intros, duplicate "why us" slides, a second agenda.
  2. Merge slides that share a point, such as two stat slides, overlapping module lists, or logos and awards on one proof slide.
  3. Move narration into speaker notes. Explanatory sentences can live in notes while the slide keeps the numbers, names, labels and links.
  4. Use denser layouts that still respect 14pt: a table instead of a card grid, 4 columns of short cards, a logo wall instead of logo cards.
  5. Only then split.
- **Nothing important is lost.** Every number, name, claim, link (hyperlink, video, source) and image from the source must survive on a slide or, for prose only, in the notes. Count them before and after. Data, links and images never move to notes only.
- 20 is a target, not a hard cap. If the content still needs more after the steps above, go over and say why in your reply. Fewer is always better.
- Card grids hold at most 6 cards (3 by 2) with body copy, or 8 short cards (4 by 2) with a title and one line each.
- Card body copy stays under about 25 words, or 4 bullets of under 8 words.
- Never shrink the font, crowd the margins or drop the footer to make content fit.
- Vary layouts. Do not run three card grids in a row when a table, stat row, steps or split layout would carry the content better.
- Every content slide gets a visual: icons in cards, a stat, a chart, a diagram, logos, or an image from the source.

### 4. Build

Work in a fresh folder of your own (`WORK=$(mktemp -d /tmp/ak-deck-XXXX)`) for the build script, extracted media and renders. Shared scratch paths get overwritten when several decks build at once.

Write a Node script that requires `ak.js`, builds each slide with the helpers, and ends with `await ak.finalize(pres, outPath)`. `finalize` is required, because it converts gradient placeholders into native PowerPoint gradients. Skipping it leaves odd red bars.

```javascript
const ak = require("/ABS/PATH/accuknox-pptx-rebrand/scripts/ak.js");
(async () => {
  const pres = ak.createDeck({ title: "Partnership Program" });
  ak.coverSlide(pres, { eyebrow: "Partner program · October 2026", title: "Partnership Program",
    subtitle: "Co-sell with AccuKnox", tagline: "Zero Trust CNAPP for cloud, AI and runtime security.",
    image: await ak.coverArt("network") });
  const s = ak.contentSlide(pres, { eyebrow: "01  About AccuKnox", title: "AccuKnox at a glance",
    subtitle: "Founded in 2020 in partnership with SRI International" });
  ak.statRow(s, [{ value: "10+", label: "Patents" }, { value: "2M+", label: "KubeArmor downloads" }]);
  ak.closingSlide(pres, { subtitle: "Partner with AccuKnox to co-sell Zero Trust security.",
    cta: "Become a partner", ctaUrl: "https://accuknox.com/partners", email: "support@accuknox.com" });
  await ak.finalize(pres, "/mnt/user-data/outputs/2026-10-07-partner-program-v1.pptx");
})().catch((e) => { console.error(e); process.exit(1); });
```

`contentSlide` sets `slide.top`, the first free y for content. Helpers like `cardGrid`, `statRow`, `table` and `steps` default to it.

The library prints `[ak] possible overflow` warnings when copy will not fit its box at the set size. Treat each warning as a defect. Shorten the copy or split the slide, then rebuild.

**Icons** use one house style: outline icons with no background, in a darker bluish grey (`ak.C.iconGrey`, 4A5873). `ak.iconCircle` and `ak.icon` draw them that way by default, and `cardGrid` items with `icon` get it automatically. Use the Tabler set (`tb:`) first and Lucide (`lu:`) second. Look up names with `node ak.js --find shield lock`. Avoid solid glyph sets (`fa6:`) and filled discs behind icons. Never use an icon to stand in for a company.

**Company and product logos** always appear in their real brand form and colours, never recoloured blue or grey. Pick the source in this order:
1. The logo image from the source deck or one the user supplied.
2. `await ak.brandLogo(slide, "microsoft-azure", { x, y, w, h })`, a full colour logo from the bundled set. Find names with `node ak.js --logo azure`.
3. The company name set as text, if neither exists.

Never draw an imitation of a company logo, and never use a mono glyph (`si:`, `fa6:FaAws`, `tb:TbBrand*`) as a logo.

### 5. QA

Render and look at every slide. You will see what you expect after writing the code, so look at the images fresh:

```bash
cd OUTDIR && soffice --headless --convert-to pdf deck.pptx && pdftoppm -r 80 -png deck.pdf qa
```

Check for:

- Text overflow, clipping, or text sitting on top of other text. Check this first.
- Body copy under 14pt anywhere except footers, chart axes and table footnotes.
- Content crossing into the footer zone (below y 6.75in).
- Uneven gaps, cards of mismatched height in a row, orphaned single words on titles.
- Low contrast: blue text on dark navy, gray text on the tint strip, or any CTA label that is not white on its blue button.
- Leftover placeholder text, and copy that breaks the writing rules below.

Fix, re-render only the changed slides, and stop once clean. One or two passes is normal.

### 6. Deliver

- File name: lowercase with hyphens, date prefix, version suffix, for example `2026-10-07-partner-program-v1.pptx`. On a redesign, keep the original topic and bump the version.
- Never put prospect names, emails or deal sizes in the file name. Use an account code.
- Save to `/mnt/user-data/outputs/`. If the user has a connected folder, also write it there, in a `drafts/` subfolder unless they say it is final.
- Reply with one or two lines: what you built, slide count, and any facts you flagged as missing.

---

## Design system

### Colors (`ak.C`)

| Token | Hex | Use |
|---|---|---|
| `blue` | 1040C5 | Eyebrows, numerals, links, footer bar, page numbers, highlighted table values |
| `red` | FF4646 | Gradient start, cost or risk stats |
| `redDeep` | D63637 | Small red labels on white |
| `ink` | 000025 | Titles on white, dark slide background, table header |
| `iconGrey` | 4A5873 | Outline icons, no background |
| `navyCard` | 16205A | Panels and concentric rings on dark slides |
| `body` | 37474F | Body text on white |
| `muted` | 607D8B | Subtitles, card descriptions |
| `border` | DCE3F0 | Card borders, table rules |
| `tint` | E2EEFF | Callout strip, highlighted panels |
| `tintSoft` | F8FAFF | Alternating table rows |
| `periwinkle` | 8FA8FF | Secondary text on dark slides |

Signature motif: the red to blue gradient (FF4646 to 1040C5). It appears as the short tick above every eyebrow and as the top edge of every card. Keep it to those two uses so it stays a signature rather than decoration.

### Type (`ak.T`), Inter throughout

| Role | Size | Style |
|---|---|---|
| Cover title | 54pt | Inter Bold, white |
| Section title | 48pt | Inter Bold, white |
| Slide title | 32pt | Inter Bold, ink |
| Subtitle | 16pt | Inter Regular, muted |
| Eyebrow and labels | 11pt | Inter Bold, uppercase, letterspaced, blue |
| Card title | 18pt | Inter Bold, ink |
| Body | 14pt minimum | Inter Regular, body or muted |
| Numerals and stats | 36 to 54pt | Inter Light, blue (or red for costs and risk) |
| Footer | 9pt | Inter Regular, muted |

Inter ships with the sandbox, so QA renders are true to width. Users without Inter installed see a fallback font in PowerPoint. If the user reports that, tell them to install Inter from Google Fonts.

### Buttons and CTAs

- Text on any blue button or CTA (blue `1040C5` fill) is always white, bold, with no underline. The same applies to text on ink or other dark fills.
- Build every button with `ak.ctaButton(slide, { text, url, x, y, w, h })`. It keeps the label white and puts the link on an invisible layer over the button. Putting a hyperlink on the text itself makes PowerPoint repaint it in the theme link colour, which shows blue on blue.
- Plain text links on white slides (such as "Source →" or "Watch video →") stay brand blue.

### Slide frame

- 16:9 (13.33 by 7.5in), 0.6in side margins.
- Content slides: gradient tick, eyebrow `NN  SECTION NAME`, title, optional subtitle. Footer: blue logo left, "Confidential. Limited distribution under NDA." centered, two digit page number right, solid blue bar along the bottom edge. Pass `confidential: null` to drop the line for public decks.
- Dark slides (cover, section dividers, closing): ink background with thin concentric rings on the right.
- Cover artwork matches the deck topic. Use `await ak.coverArt(topic)`, which draws a thin outline illustration in the brand style: a dashed blue to red outer contour, a solid inner contour, a fine purple node network, one filled blue control node, and a red attack dot stopped by a blue tick at the boundary. Motifs: `ai` (shield and neural net) for AI security, `cloud` (cloud and workload mesh) for CNAPP, CSPM, CWPP and Kubernetes, `code` for ASPM, AppSec and supply chain, `compliance` for GRC, DPDP and audits, `runtime` for KubeArmor, eBPF and runtime, `network` for company, partner and global topics. Do not reuse the same cover art across decks on different topics, and keep the photo globe (`assets/cover-globe.png`) for global or partner network decks only. If a topic needs a new motif, add it to `cover_art.js` in the same line style rather than using stock imagery.
- Section numbers in eyebrows match the agenda numbering.

---

## Writing rules

Slides carry the AccuKnox voice: authoritative, prevention first, technical, accessible. Readers are security practitioners, so use CNAPP, CSPM, CWPP, ASPM, AI-SPM, eBPF, K8s and Zero Trust without expanding them.

- Titles are short statements of the point, in sentence case.
- Active voice, concrete nouns, numbers over adjectives.
- No em dashes, en dashes, semicolons or hashtags. Avoid hyphenated compounds where a rewrite works ("open source" not "open-source", "AI powered" not "AI-powered"). Product and framework names keep their official spelling.
- Avoid filler and hype: "cutting edge", "streamline", "game changer", "powerful", "unparalleled", "it's important to note".
- No emojis.
- Pricing never goes on a slide as a hardcoded figure unless the user supplied it for this deck. Otherwise write `[PRICING — CONFIRM WITH SALES OPS]` and mention it in your reply.
- Cite incident costs, market sizes and analyst claims in a small source line or the speaker notes, using what the source material gave you.
- Put talking points in speaker notes (`notes` option on `contentSlide`) when the source has more detail than fits the slide. That keeps slides clean without losing content.

---

## Redesign mode details

1. Inventory the old deck: one line per slide with its facts, images and purpose. Older AccuKnox decks use a 10 by 5.625in canvas with a solid blue header bar. The output is always the 13.33 by 7.5in frame in this skill, so nothing is copied over position for position.
2. Map each old slide to a layout in `references/layouts.md`. Merge thin slides and split crowded ones. Crowded old slides are common because the old body size was 9 to 11pt.
3. Decide per visual how to carry it over:
   - **Photos, logos, product screenshots, illustrations**: reuse the original file from `ppt/media/`. Match each image to its slide through `ppt/slides/_rels/slideN.xml.rels`.
   - **Diagrams built from shapes and text** (flows, matrices, layer stacks, wheels): rebuild them natively with `ak.js` primitives, at the new type sizes, so the text is readable and editable. Simplify when the original has more labels than fit at 14pt, and move the detail to speaker notes.
   - **Complex artwork you cannot rebuild well** (a dense roadmap illustration, an iceberg graphic): reuse the image file, and put any tiny embedded text it carries as readable text beside it.
   - Never paste a screenshot of an old slide region into the new deck. It brings the tiny old fonts back.
4. Keep every number, name and claim. Tighten wording to the writing rules, without changing meaning. Carry speaker notes across.
5. For decks over about 20 slides, organise the build script as one function per slide and build and render in batches of 8 to 10, fixing each batch before moving on. This keeps QA honest on long decks.
6. Aim for 20 slides or fewer, using the reduction order in the storyboard rules. Old decks often hold repeated proof slides, two agendas, and slides that only restate a heading. Those are the first to merge or cut.
7. Before delivering, check the redesign against the original: every number, name, hyperlink and image is still on a slide.
8. In your reply, give the slide count before and after, list any slide you merged, split or dropped, and list anything moved into speaker notes.
