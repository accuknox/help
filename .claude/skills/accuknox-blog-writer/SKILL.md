---
name: accuknox-blog-writer
description: >
  Write, grade and ship an AccuKnox blog post. Use this skill whenever the user
  asks for a blog, a blog output, a post, an article or a writeup for AccuKnox,
  and whenever they want an existing post graded, audited, scored, optimized or
  reviewed for SEO. Triggers include "write a blog on X", "blog output",
  "draft a post about X", "grade this blog", "SEO audit this", "check this URL",
  "optimize my post", "review this article", or pasting an accuknox.com blog URL
  with any request attached. Carries the accuknox.com URL inventory, the layout
  of the current live posts, the SEO grader and the Google Docs publisher, so it
  needs nothing outside its own folder except the repo's writing rules.
trigger: /ak-blog
---

# AccuKnox blog writer

Two jobs share one harness. **Write** a new post, or **grade** an existing one.
Both run on the same sources, the same layout spec and the same gates.

Repo root for every path below: `D:\Atharva\AccuKnox\HelpDocs`.
Skill root: `.claude/skills/accuknox-blog-writer/`.

This skill also carries the shared harness the three sibling skills read:
`references/source-of-truth.md`, `references/house-style.md`,
`references/asset-kit.md`, `sources/`, `media/` and `scripts/`. Change one of
those and you change all four. The siblings are
`accuknox-press-release-writer`, `accuknox-case-study-writer` and
`accuknox-comparison-writer`.

## Load the writing chain first

This repo carries a load-order contract and it applies here. Read, in order:

1. `.claude/core/runtime-contract.md`
2. `.claude/core/writing-rules.md`, and section 11 owns the blog channel
3. `.claude/core/restraint-rules.md`
4. `references/house-style.md`, the AI watermarks and the layout Atharva reads by

Print the `Loaded` block above every draft. The `Sourced` line names the pages
and files you actually opened, and `sources/*.md` does not count as a source
for a fact. It is an index of URLs.

Two rules outrank everything in this skill. No version, CVE, CVSS score,
compliance control, CLI flag, API field, default or supported platform without
an opened source behind it, and a visible bracket where the fact is missing. No
working exploit, live payload or unredacted customer data, in text or in a
screenshot.

## Ask three questions, every time

Whenever the user gives you a topic and has not already answered these, ask all
three in one message and wait:

1. **Length.** Word count or reading time. Default 1,500 words, which is 8
   minutes at the 200 wpm the site uses. Recent posts run 1,200 to 2,000.
2. **External references.** Which outside sources should the post cite and link.
   A standard, an advisory, an analyst figure, a competitor's own documentation,
   a news item. Firecrawl is installed and reaches any of them. Default: cite
   every standard and CVE the post names, and nothing beyond that.
3. **Audience.** Platform or DevOps engineer, security engineer or analyst,
   security lead, or CISO. The answer decides how much the post explains and how
   deep the commands go.

Ask once. Do not ask again mid-draft, and do not ask when the user has already
said "go with your recommendation".

## Writing a post, step by step

**1. Resolve the topic against what already exists.**

```bash
grep -i "<topic keyword>" .claude/skills/accuknox-blog-writer/sources/blog.md
```

A near-duplicate slug means the job is an update, not a new post. Say so before
you write 1,500 words nobody needed.

**2. Pull the source pages.** Product positioning comes from accuknox.com, product
behaviour comes from this repo.

```bash
cd .claude/skills/accuknox-blog-writer
python scripts/fetch_md.py platform/cspm solutions/ai-red-teaming --out /tmp/research
python scripts/fetch_md.py blog/<closest-existing-post> --headings
```

Read a hub page before you drill. `comparisons.md`, `platform.md` and
`blog.md` each list their whole section in one fetch.
`references/source-of-truth.md` has the full method, the Firecrawl fallback and
the help.accuknox.com URL rules.

**3. Read the layout spec.** `references/blog-layout.md`. It carries the section
order, the TL;DR shape, the heading rule, the table rule, the image placeholder
format and the link budget, all derived from the six most recent live posts.

**3b. Pick the images.** `references/asset-kit.md` names the four sources and the
order to try them. Check the PRODUCT UI mirror is fresh before you rely on it:

```bash
python scripts/drive_sync.py check
python scripts/drive_sync.py search "<topic>"
python scripts/drive_sync.py pull --folder "<folder from the search hit>"
```

`check` exits 1 once the manifest passes 90 days. Say so in your reply rather
than quietly working from a stale index.

**4. Copy the template and fill it.**

```bash
cp .claude/skills/accuknox-blog-writer/assets/blog-template.md \
   references/<series>/<slug>.md
```

Drafts land in `references/<series>/`, per the runtime contract. Never in `docs/`.

**5. Write pass 1.** Do not evaluate while writing.

**6. Read it cold and answer three questions for yourself, in writing, unprinted.**
Which exact sentence would a reader call generated. Does the post state a
version, flag, score or control that no opened source supports. Which sentence
is weakest, and does the post rest on it.

**7. Fix what pass 2 found, then run the gates.**

## Grading a post

Input is a URL, a local file or pasted text.

```bash
cd .claude/skills/accuknox-blog-writer
python scripts/fetch_md.py https://accuknox.com/blog/<slug> --out /tmp/audit
python scripts/grade.py /tmp/audit/<slug>.md
python scripts/verify_links.py /tmp/audit/<slug>.md --fix-suggestions
```

For pasted text with no front matter, the grader reports every SEO field as
missing. Say "not provided" in the report rather than treating it as a failure.

Then work `references/seo-audit.md` against the draft. It holds the judgement
the script cannot make: search intent match, E-E-A-T for a security audience,
schema, and AI citation readiness. Report the script's score table, then the
findings, ranked CRITICAL, HIGH, MEDIUM, LOW, each with the fix and the line.

## The gates

Run all three, in this order, and report each result.

```bash
cd .claude/skills/accuknox-blog-writer
python scripts/grade.py <draft.md>                          # CRITICAL must reach 0
python scripts/verify_links.py <draft.md> --fix-suggestions # 0 broken
python scripts/slop.py <draft.md>                           # adjusted CRIT must reach 0
```

Then run section 5 of `.claude/core/restraint-rules.md` by reading. It is the
only check that looks for damage the other gates cause, and the failure it
catches is a post polished until nobody is home.

`slop.py` wraps the shared scorer at `D:\Atharva\NOTES\SCRIPTS\slop\score.py`.
That scorer bans the semicolon and the layout requires a `TL;DR` heading, so a
correct draft always scores one CRIT. The wrapper prints the raw output, names
the suppressed finding, and reports an adjusted count. It suppresses nothing
else. When the scorer path is unavailable it exits 2, and you then apply the
rules by reading and say in your reply that the scorer did not run.

`mkdocs build --strict` does not apply. A blog draft is not in the nav.

## Google Doc is the default output

When the user says **blog output**, or asks for a blog without naming a format,
ship a Google Doc. Always write the markdown file to disk first, because that is
the artifact the repo keeps.

```bash
cd .claude/skills/accuknox-blog-writer
python scripts/to_gdoc_html.py <draft.md>            # writes <draft>.gdoc.html
python scripts/to_gdoc_html.py <draft.md> --print-title
```

Then upload through the Google Drive connector, passing the HTML as text:

```
create_file(
  title       = <the --print-title output>,
  textContent = <the full contents of the .gdoc.html file>,
  contentMimeType = "text/html")
```

Drive converts `text/html` into a native Google Doc and keeps headings, tables,
bold, italics and hyperlinks. Uploading raw markdown loses all of it, so never
skip the conversion. The front matter is rendered as an `SEO metadata` table at
the top of the document, because that is the block marketing copies into
WordPress.

Two conversion details are load-bearing. Google Docs imports `<pre>` as ordinary
body text and drops the monospace font, the shading and the indentation, so
`to_gdoc_html.py` rewrites every fenced block as a one-cell table, which
survives the import with its line breaks and leading spaces intact. And the
converter omits the `nl2br` markdown extension, because a hard-wrapped paragraph
would otherwise arrive with a line break after every source line.

**Republishing creates a new Doc.** The Drive connector can create a file and
change its metadata. It cannot replace the body of an existing Google Doc. To
ship a revision, call `create_file` again and then `trash_file` on the old id,
and give the user the new URL.

Reply with the Doc URL, the local markdown path, and the gate results. If the
Drive connector is not authorized in the session, say so, hand over the
`.gdoc.html` path, and note that opening it in Google Docs through
`File > Open` produces the same document.

## What this skill does not write

WordPress injects the table of contents, the social share row, the byline, the
reading-time line, the `Ready For A Personalized Security Assessment` CTA, the
three customer testimonials and the `Continue Reading` block. Write none of it.
A draft that hand-rolls a CTA duplicates the template.

No cover image file either. The cover is a prompt in the front matter and a
blockquote under the H1.

## Keep the sources fresh

```bash
python scripts/refresh_sources.py --check    # exits 1 when a bucket is 30 days old
python scripts/refresh_sources.py            # rebuild all ten buckets
```

The inventory is a fast index, never proof. `platform/aispm` is live and missing
from the sitemap. `platform/prompt-firewall` is linked from a published post and
returns 404. Only `verify_links.py` settles it.

## Files in this skill

| Path | What it holds |
| --- | --- |
| `references/blog-layout.md` | The section order and every layout rule, from the six newest live posts |
| `references/source-of-truth.md` | Shared. The `.md` twin trick, the sitemap map, help-docs URL rules, Firecrawl |
| `references/house-style.md` | Shared. The AI watermarks a word list misses, plus tables, bullets and callouts |
| `references/asset-kit.md` | Shared. Four image sources, screenshot cleanup, brand colors and fonts |
| `references/seo-audit.md` | The judgement half of the audit that no script can run |
| `assets/blog-template.md` | The file you copy to start a draft |
| `sources/*.md` | Shared. Cached accuknox.com URL inventory, ten buckets |
| `media/INDEX.md`, `media/MANIFEST.json` | Shared. The PRODUCT UI Drive library, 298 files indexed |
| `scripts/refresh_sources.py` | Rebuild the inventory from the sitemap index |
| `scripts/drive_sync.py` | Index, search and mirror the PRODUCT UI Drive folder |
| `scripts/fetch_md.py` | Read any accuknox.com page as markdown, boilerplate stripped |
| `scripts/grade.py` | Deterministic SEO and structure score |
| `scripts/verify_links.py` | Every link resolves, anchors are descriptive |
| `scripts/slop.py` | The shared slop scorer, with the `TL;DR` collision accounted for |
| `scripts/to_gdoc_html.py` | Markdown to the HTML Google Drive imports as a Doc |
| `scripts/selftest.py` | Proves the five scripts still work, offline where it can |

Check the harness itself after any change to it:

```bash
python .claude/skills/accuknox-blog-writer/scripts/selftest.py
```

## Related

- `references/asset-kit.md`, images and brand. This replaced the retired
  `accuknox-asset-kit` skill on 2026-08-23.
- `.claude/skills/accuknox-press-release-writer/`, an announcement
- `.claude/skills/accuknox-case-study-writer/`, a customer outcome
- `.claude/skills/accuknox-comparison-writer/`, a versus or alternatives page
- `.claude/core/runtime-contract.md`, the load order and the accuracy rule
