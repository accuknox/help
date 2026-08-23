# The AccuKnox blog layout

Derived on 2026-08-23 from the six most recently modified posts on accuknox.com,
read through their `.md` twins:

| Post | Body words | Reading time |
| --- | --- | --- |
| `blog/global-airline-ai-security` | 1,270 | 6 min |
| `blog/continuous-compliance-monitoring-cert-in-iso-27001` | 1,486 | 6 min |
| `blog/best-cnapp-tools-for-enterprise-security` | 1,997 | 8 min |
| `blog/best-kubernetes-tools-for-rbac-visibility` | 1,209 | 6 min |
| `blog/ai-agent-security-zero-trust` | 1,585 | 8 min |
| `blog/salesloft-data-theft-campaign` | 1,289 | 3 min |

Refresh those numbers with `python scripts/fetch_md.py blog/<slug> --headings`.

## What you write and what WordPress adds

Every published post ends with the same three blocks: **Ready For A Personalized
Security Assessment**, three customer testimonials, and **Continue Reading** with
three fixed related posts. The table of contents, the social share row, the
author byline and the reading-time line are injected the same way.

None of that is authored. Write none of it. `scripts/fetch_md.py` strips the
whole tail so you study only the parts a human wrote. A draft that hand-rolls a
CTA block duplicates the template and gets cut in review.

## The section order

1. **YAML front matter.** The SEO fields. Full list in `assets/blog-template.md`.
2. **H1.** One only. Carries the primary keyword and reads as a claim, not a label.
3. **Cover image prompt.** A blockquote placeholder, never a real cover file.
4. **TL;DR.** H2, three to six bullets, at least one number.
5. **Body.** Four to nine H2 sections, each heading stating a conclusion.
6. **A closing H2 that lands a position.** `Treat identity as the first control
   plane in Kubernetes` and `Final thoughts` both appear in the sample. Prefer
   the first shape.
7. **FAQ.** H2 labelled `FAQs` or `Frequently Asked Questions`, three to five
   H3 questions, each answered in two or three sentences.

Nothing after the FAQ. The template owns that space.

## TL;DR, the block an answer engine lifts

Three to six bullets. Each one is a complete sentence carrying a fact, and at
least one carries a figure. The airline post opens with `2,968 findings across
five deployed LLMs, and 2,428 of those were critical`, which is quotable on its
own and needs no surrounding paragraph.

A bullet that says `AccuKnox helps organizations secure their AI workloads` is
the failure mode. It survives every mechanical check and gets cited by nobody.

## Headings that carry the conclusion

Every H2 in the sample states something. `Why RBAC visibility breaks at scale`,
`Red teaming ran first, the prompt firewall went inline second`, `The gap between
88% on ISO 27001 and 47% on the OWASP Top 10 for LLM`. A reader who reads only
the headings has read the argument.

Sentence case. No colon. No skipped level. `grade.py` flags a heading that opens
with `Understanding`, `Introduction`, `Overview` or `Key takeaways`.

## Tables

Every post in the sample carries at least one table, usually a control map, a
criteria matrix or a persona shortlist. The CERT-IN post maps seven operational
areas across four columns. A table is the block an answer engine extracts most
reliably, so a post with none is leaving citations on the table.

Header row always. No empty cells.

## Images

Two to four per post, each as an italic caption line under the image. The caption
says what the picture proves, not what it is. `Model-layer findings by check
type, and the five deployed models ranked by issue count` beats `AI-SPM
dashboard`.

In a draft, write each image as a placeholder block rather than a file path:

```markdown
> **Image prompt (inline 1):** A four-layer stack diagram, infrastructure at the
> base rising to agents at the top, AccuKnox navy `#11206D` on white with
> `#003BF6` accents, flat vector, no text labels, generous negative space.
>
> *Caption: The four layers of AI risk and the controls applied at each.*
```

Where a real product screenshot fits better than a generated image, say so and
name the source folder. `references/asset-kit.md` names the four image sources and how to crop a
screenshot.

## Links

Inline, on the words that earn them, never a list at the bottom. The sample runs
five to twelve links per post, split roughly:

- Three or more `accuknox.com` product pages, on the first mention of the
  capability. `AccuKnox's [AI Prompt Firewall](https://accuknox.com/...)`.
- At least one `help.accuknox.com` page where a claim needs the doc that proves it.
- One or more external citations for every standard, CVE, benchmark or
  third-party behaviour. The CERT-IN post links the CERT-In directive PDF and
  the ISO 27001 catalogue entry directly.

Run `scripts/verify_links.py` before you ship. The sitemap is incomplete and
slugs move.

## Length

1,200 to 2,000 prose words. Reading time is the word count divided by 200,
rounded to the nearest minute, and it goes in the front matter.

Below 1,200 the post reads as a stub. Above 2,600 it is two posts.

## The FAQ

Three to five questions a practitioner would actually type. Each answer is two
or three sentences and resolves the question on its own, because an answer
engine lifts the pair without the surrounding page.

The airline post asks `Does adding a firewall break the AI application?` and
answers with audit mode plus failover handling in two sentences. That is the
shape.

Never recommend FAQPage schema for this. Google restricts FAQ rich results to
government and health sites.

## Related

- `assets/blog-template.md`, the file you copy to start a draft
- `references/source-of-truth.md`, where every fact and link comes from
- `references/seo-audit.md`, the judgement the grader cannot make
- `.claude/core/writing-rules.md` section 11, the channel rule this layout serves
