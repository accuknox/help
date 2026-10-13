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

1. **YAML front matter.** Eight fields and no others: `slug`, `title`,
   `description`, `author`, `date`, `category`, `primary_keyword`,
   `secondary_keywords`. No image prompt, no excerpt, no url, no reading time.
   WordPress owns the cover image, the excerpt and the reading time.
2. **H1.** One only. Carries the primary keyword and reads as a claim, not a label.
3. **TL;DR.** H2, three to six bullets, at least one number.
4. **Body.** Four to nine H2 sections, each heading stating a conclusion.
   Fewer when the user sets a short word limit.
5. **A closing H2 that lands a position.** `Treat Identity as the First Control
   Plane in Kubernetes` and `Final Thoughts` both appear in the sample. Prefer
   the first shape.
6. **A video embed H2.** One YouTube embed from [@AccuKnox](https://www.youtube.com/@AccuKnox),
   the most relevant to the topic. See the Video embed section below.
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

Every H2 in the sample states something. `Why RBAC Visibility Breaks at Scale`,
`Red Teaming Ran First, the Prompt Firewall Went Inline Second`, `The Gap Between
88% on ISO 27001 and 47% on the OWASP Top 10 for LLM`. A reader who reads only
the headings has read the argument.

AP Title Case on every H2, and `grade.py` checks it. Lowercase only a, an, the,
and, but, or, nor, for, so, yet, as, at, by, in, of, off, on, per, to, up, via and
vs in the middle of a heading, and capitalize each part of a hyphenated word.
The writer's global rule sets this, and it overrides the sentence-case line in
`.claude/core/writing-rules.md` section 6 for a blog post. H3 FAQ questions stay
as ordinary questions. No colon. No skipped level. `grade.py` flags a heading that opens
with `Understanding`, `Introduction`, `Overview` or `Key takeaways`.

## Tables

Every post in the sample carries at least one table, usually a control map, a
criteria matrix or a persona shortlist. The CERT-IN post maps seven operational
areas across four columns. A table is the block an answer engine extracts most
reliably, so a post with none is leaving citations on the table.

Header row always. No empty cells.

## Images

Two to four per post, and at least one is a real product screenshot. A post of
nothing but diagrams reads as filler, and a post of nothing but dashboards shows
no mechanism, so mix them.

Pull images in this order. `scripts/images.py find <keyword>` searches all of it.

1. A console shot from the help docs or the demo set, cropped with
   `scripts/images.py prep`. Real, current and already described.
2. The PRODUCT UI Drive library, through `scripts/drive_sync.py`.
3. A diagram you render from HTML with Playwright in AccuKnox navy `#11206D`,
   accent `#4D4DD9`, Inter. Use it for a concept that has no screenshot, such as
   a framework or a stack. Source and facts on the diagram come from the post.

Write each image as a standard markdown image with a local path, then one italic
line under it. The path is relative to the draft, and the files live in
`references/drafts/blog/images/<slug>/`.

```markdown
![The AgentZ span list for one run, with each model call, its duration and token count](images/auditable-ai-agents/agentz-span-trace.png)

*Every model call and tool call in a run is a span with its own duration and token count.*
```

The italic line says what the picture proves, not what it is. `Model-layer
findings by check type, and the five deployed models ranked by issue count` beats
`AI-SPM dashboard`. Never open the line with the word `Caption`, and never label
it at all. Alt text follows the same rule and never opens with `a screenshot of`.

`push_gdoc.py` embeds each local image into the Google Doc, sized to the page
width, so nothing needs a public URL. A remote image keeps its URL.

Do not write an image prompt anywhere in the draft or its front matter. When no
real picture exists yet, leave an open `> **Image needed:** ...` block. The
grader flags it until you replace it.

## Video embed

Every post carries one YouTube embed from the AccuKnox channel, [@AccuKnox](https://www.youtube.com/@AccuKnox). Pick the single most relevant video for the topic, a webinar, a product demo, or a KubeArmor walkthrough, and place it in a short H2 near the end, before the FAQ. The heading states what the video shows, such as `See runtime enforcement stop an attack in real time`, never `Watch this`.

Write the embed as an HTML iframe inside a fenced ```html block, so `to_gdoc_html.py` renders it as a copy-paste code cell that marketing pastes into WordPress. Keep the `allow` attribute out, because the shared slop scorer flags the semicolons a full `allow` list carries. Follow the iframe with a plain inline link to the watch URL.

```html
<iframe width="560" height="315" src="https://www.youtube.com/embed/VIDEO_ID" title="The exact video title" frameborder="0" allowfullscreen></iframe>
```

Confirm the video exists on the channel before you embed it. The `youtu.be` short link an email hands you is not always an AccuKnox video, so verify the channel, not just that the URL resolves.

## Links

Inline, on the words that earn them, never a list at the bottom. The sample runs
five to twelve links per post, split roughly:

- Three or more `accuknox.com` product pages, on the first mention of the
  capability. `AccuKnox's [AI Prompt Firewall](https://accuknox.com/...)`.
- At least one `help.accuknox.com` page where a claim needs the doc that proves it.
- One or more external citations for every standard, CVE, benchmark or
  third-party behaviour. The CERT-IN post links the CERT-In directive PDF and
  the ISO 27001 catalogue entry directly.

Run `scripts/gates.py` before you ship. It runs `verify_links.py` with the other two gates. The sitemap is incomplete and
slugs move.

## Length

The user's number wins. When they say `under 1200 words`, write to that and
run `scripts/gates.py <draft> --min-words 800 --max-words 1199`. The ceiling
counts every word in the body, tables and headings included.

With no number from the user, the default is 1,200 to 2,000 prose words. Below
1,200 the post reads as a stub, and above 2,600 it is two posts. Reading time is
the word count divided by 200, and WordPress shows it, so it stays out of the
front matter.

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
