# Battlecard PDF, the sales output mode

Use this mode when the request is a PDF, a battlecard, a one-pager or an edit to an existing
AccuKnox comparison PDF. A web comparison page and a PDF battlecard read differently. A buyer reads
a web page top to bottom. A PDF gets scanned in 30 seconds, often on a phone, so density decides
whether anyone reads it.

The reference build is `references/competitive/battlecards/netskope/battlecard/`. It renders the cover
and the tables from HTML with Playwright, then appends the stock AccuKnox back page.

```bash
python references/competitive/battlecards/netskope/battlecard/build_battlecard.py
```

For a new competitor, copy the folder, swap the competitor logo in `assets/`, and edit the row lists
and the `PICK` strip in `build_battlecard.py`.

## Page Order Stays Fixed at Four Pages

1. **Cover.** The AccuKnox logo, the title `AccuKnox vs <Competitor>`, the category in brackets such
   as `(AI Security)`, and one card per row group with an icon per capability. The cover carries no
   sentences.
2. **Verdict and group 1.** The headline frame, the "Pick AccuKnox to" strip, the one-line tally, then
   the first row group. For AI security, the Shadow AI panel follows here.
3. **Group 2.** One table that fits one page. Cut words until it fits, never split a table across
   pages for one leftover row.
4. **Back page.** `assets/back-page.pdf`, unchanged.

## Density Rules the Reviewer Enforced

Every rule below came from review feedback on the Netskope battlecard.

1. **Power phrases, not sentences.** A cell bullet runs three to seven words. "AI flags false
   positives" passes. "The AI reviews each finding and marks the false positives" fails.
2. **Keep every fact while you cut words.** Cut articles, verbs of being and repeated nouns. Never
   cut a number, a product name or a platform.
3. **Bullet caps per cell.** AccuKnox gets three bullets, four at most. The competitor gets two. The
   takeaway gets one phrase of eight words or fewer.
4. **Column widths.** Capability 22%, AccuKnox 38%, competitor 24%, takeaway 16%. The AccuKnox column
   is always the widest and carries a tinted background.
5. **Capability names stand out.** Set them at 11.5 pt bold with a line icon beside each. Body text
   sits at 9 pt and the takeaway at 8.2 pt bold blue.
6. **Logos replace column headers.** Use the AccuKnox and competitor logos in the table header.
   Use brand marks from simple-icons (OpenAI, Claude, Gemini, GitHub Copilot, NVIDIA, Kubernetes) where a
   cell names those products.
7. **Status chips carry the color.** Use the five labels from `positioning-playbook.md`, each with a
   check, cross, half-circle or equals icon. A colored left border on the competitor cell repeats
   the status.
8. **No legend.** The one-line tally under the verdict strip explains the colors.

## What to Leave Out

The reviewer removed each of these, so leave them out from the start.

- A paragraph under the headline explaining what the page covers. The cover already does that job.
- A four-box scorecard. Use the one-line tally.
- A stats row of anonymized customer numbers, such as 4,026 assets and 130 critical findings. Those
  numbers belong in a case study or a blog post, where the context fits.
- Footnotes, source dates and "example results" disclaimers.
- Doc links in the AI for Security rows, and links to release-note pages anywhere. Keep sources in
  the builder data and the evidence log, not on the page.
- Cryptic reference labels such as "AK · NS".

## The Shadow AI Panel

Against any vendor that leads on discovery, the Shadow AI panel is the centrepiece of page 2. It is a
two-column card titled `Shadow AI: identify ≠ protect`.

- **The AccuKnox side (62%)** shows the four surfaces in a 2 by 2 grid. Each surface has an icon, a bold
  name, one line of controls and the brand marks of the apps it covers. The four surfaces are the
  browser, hosts, the desktop (Beta) and CLI agents.
- **The competitor side (38%)** shows four bullets at most. Lead with the bolded coverage ratio, such as
  identifies 3,300+ against guards 20.
- **One takeaway line** sits under both columns. "AccuKnox enforces on every surface it discovers."

## Checks Before You Send

1. Render every page to PNG and look at it. `pypdfium2` renders without poppler.
2. Confirm that page 3 holds the whole group 2 table.
3. Run `python "D:\Atharva\NOTES\SCRIPTS\slop\score.py"` on the extracted text. CRIT must reach 0.
   MED hits on table fragments are expected.
4. List every AccuKnox claim that has no help-docs source in the reply, as `R1`, `R2` and on.

## Related

- `positioning-playbook.md`, row selection, status labels and takeaways
- `parameter-sets.md`, the two-group `ai-security` row set
- `references/source-of-truth/ai-security-data-points.md` at the repo root, the data points and their sources
