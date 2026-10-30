# Make the Deck Look Human Made

Read this before you storyboard. A reader judges a deck in the first three slides, and several small AI tells together make the whole deck look generated. No single tell proves it. The fix is the same every time: state the point, cut decoration that carries no information, and vary the layout where the argument lives.

Sources: the Perceptis consultant guide (Oct 2026, a vendor blog that tested six AI slide tools) and the Uniphore OEM trial build (29 Oct 2026, five rounds of render and review).

## Nine Tells Give an AI Deck Away

These marks give an AI deck away. `ak.js` already avoids the ones marked (lib).

1. A kicker or eyebrow label above every title ("01 ABOUT ACCUKNOX"). Put the section name in the footer. (lib)
2. A colored stripe on the top edge of every card. Cards carry no accent unless one card is the point. (lib)
3. Descriptive titles such as "Market Overview", "AI Governance" or "Summary".
4. Filler icons: a lightbulb for ideas, a gear for process, a shield on every security card.
5. The same card grid on slide after slide, every block centered and evenly spaced.
6. Badges, ratings, stat chips and footer text on the cover. (lib)
7. Rings, floating shapes, glows and glassy gradients behind text. (lib)
8. Bullets that restate the title, and sentences that trace back to no source.
9. Claims the source does not hold. Check every sentence a tool adds.

## Ten Rules Make a Slide Read as Designed

1. **Write action titles.** The title is a full sentence that states the conclusion, such as "Eight AI security modules ship today." It runs two lines at most at 28pt. Force a clean break with `\n` when the natural wrap leaves one word alone on line two.
2. **Build top down.** Slide 2 states the governing answer. Each section then proves one part of it, one point per slide.
3. **Vary the form.** Use a timeline, a layered table, a diagram, one big number, or a logo map. Never run three card grids in a row.
4. **Break the symmetry on argument slides.** Give the main column more width, and let a row with two items keep its empty third column rather than stretching.
5. **Use rules and whitespace before boxes.** A thin rule between rows reads as designed. A border around every item reads as a template.
6. **Contrast with size and weight.** Inter is the only brand face, so the hierarchy comes from 28pt bold titles, 16 to 18pt bold item names, 14pt regular body and 72pt numerals.
7. **Name things the same way on every slide.** If slide 3 says "AI GRC", the control plane box on slide 5 says "AI GRC" too. Count what a title counts: a slide titled "Eight modules" shows exactly eight names.
8. **Keep real logos in real colors.** Use the icon form (`openai-icon`, `claude-icon`, `google-gemini-icon`) when a wordmark would shrink below 0.3in tall.
9. **Source third-party numbers on the slide.** Put a market figure, a survey stat or a quote in the `source:` line. Internal product facts go in speaker notes, because a line that cites "our own deck" looks odd to a customer.
10. **Label a proof strip by what it is.** A PoC is not "running in production". Write "Customers and recognition" or name the PoC.

## A Ten Minute Human Pass Catches the Rest

Run this after the last render, before you deliver.

1. Tighten two or three titles.
2. Delete any sentence you cannot trace to the source material.
3. Remove decoration that carries no information.
4. Break the uniform layout on the slides that carry the argument.
5. Cut one redundant slide.
6. Check every number, count and label against the source, and against the other slides.

## A Calibri Render Hides Inter Overflow

A render that falls back to Calibri hides overflow, because Calibri is narrower than Inter. On Windows, LibreOffice may be missing or broken, so render through PowerPoint with `scripts/render.ps1`. The script registers the per-user Inter files with `AddFontResource` before it opens PowerPoint. Zoom into one title after the first render and confirm the glyphs are Inter: Inter has a flat-topped "t" and a wide "a", Calibri has a narrow rounded build.

## The Deep Tech Theme Wins a Technical Room

Use the schematic system when the audience is a CTO, an architect or an engineering team. Build with `createDeck({ theme: "tech" })`, which is white. On 2026-10-29 Atharva asked for the deep tech schematics, tried them on ink (`theme: "deep"`), and then chose the white background with the same schematics for the Uniphore OEM deck.

1. Use `D.*` colors, never `C.*`, so a slide works in both themes. Data and the one accent are `D.sky`.
2. Draw schematics, not text tables. Put modules on a lifecycle flow, and wire a control plane to its targets with edges. Use a dashed edge for agentless and a solid edge for agent or inline, and add a one-line legend.
3. Put `ak.dotGrid()` under a schematic only, never under a whole slide.
4. Tag maturity with `ak.pill()`: a filled pill for GA, an outlined pill for "In build" or "R&D". Use a time axis with "Now", "T + 90 days" and "T + 180 days" ticks for a roadmap.
5. Close the answer slide with a row of 3 or 4 proof numbers in 36pt, each with a one-line label that names the source event.
6. Put logos on small chips with `logoChips()` from the build kit, because most brand logos disappear on ink. Give a wide wordmark such as NVIDIA a wide chip.
7. Size a block from the space left above the next element, and guard every connector against a negative length. PowerPoint refuses to open a file with a negative line extent.

## The Template Covers, a Contents Slide and Purple Dividers Frame Every Long Deck

Atharva set these on 2026-10-29 for the Uniphore OEM deck. They apply to every deck of more than about 12 slides.

1. Build the front and back cover from `D:\AccuKnox\doc-ppt-template\PPT Template.pptx` only: layout 0 for the front, layout 1 for the back. Use the template navy (`ak.TEMPLATE_NAVY`, 11206D), its image layers at their own positions, and its text sizes from `_akdeck.cover_slide` and `closing_slide`, scaled from 10 in to 13.333 in. The worked version is `tplCover` and `tplBack` in `references/drafts/oem-u1-deck/build/kit.js`.
2. Put a contents slide right after the cover. Group the chapters by the question they answer, and fill in each chapter's start page from a dry-run build, so no page number goes stale.
3. Mark every chapter divider in brand ink (#000025) with white text, as `ak.sectionSlide` does in the "tech" theme. Atharva first chose purple 4D4DD9, then switched to ink the same day.
4. Deliver the PPTX only, unless he asks for a PDF.

## A Short Head on an Ink Strip Makes Each Slide Scannable

Atharva asked for this on 2026-10-29, after the full Uniphore deck: shorter headings that stand out, more icons, and dividers in brand ink.

1. In the "tech" theme, pass `head` (2 to 6 words, one line at 26pt) and `icon` (a Tabler outline icon) to `contentSlide`. The head prints in white on an ink (#000025) strip with the brand gradient on its lower edge. The long action title prints under the strip as the takeaway line.
2. Put icons on concrete things: list rows, schematic nodes, flow steps and stats. Use `ak.iconLater()` from sync code. A specific icon such as a key, a database or a robot earns its place. A lightbulb or a gear does not.
3. Chapter dividers sit on ink (#000025), not purple. The template covers stay on template navy.
4. Leave about 20% spare width in every text box, and room under it for one extra line. A viewer without Inter swaps in a wider font, and a tight box then collides with the line below.
