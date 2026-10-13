---
name: accuknox-blog-writer
description: Write, grade and ship an AccuKnox blog post. Use this skill whenever the user asks for a blog, a blog output, a post, an article or a writeup for AccuKnox, and whenever they want an existing post graded, audited, scored, optimized or reviewed for SEO. Triggers include "write a blog on X", "blog output", "draft a post about X", "grade this blog", "SEO audit this", "check this URL", "optimize my post", "review this article", or pasting an accuknox.com blog URL with any request attached. Carries the accuknox.com URL inventory, the layout of the current live posts, the SEO grader, the image finder and the Google Docs publisher, so it needs nothing outside its own folder except the repo's writing rules.
---

# AccuKnox blog writer

Two jobs share one harness. **Write** a new post, or **grade** an existing one.
Both run on the same sources, the same layout spec and the same gates.

Repo root for every path below: `D:\AccuKnox\help`.
Skill root: `.claude/skills/accuknox-blog-writer/`.

This skill also carries the shared harness the three sibling skills read:
`references/source-of-truth.md`, `references/house-style.md`,
`references/asset-kit.md`, `sources/`, `media/` and `scripts/`. Change one of
those and you change all four. The siblings are
`accuknox-press-release-writer`, `accuknox-case-study-writer` and
`accuknox-comparison-writer`.

## Load the Writing Chain First

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

A PRD, a roadmap deck or an internal memo is an opened source for direction, and
it is never proof of a shipped feature. Publish only what a public doc, a release
note or accuknox.com also states. Write the rest as a visible bracket, such as
`[confirm with product: scope and timing before this line ships]`.

## Ask Only What the User Has Not Answered

Three facts shape a post. Take each one from the request when it is there, and
ask for the missing ones in a single message.

1. **Length.** A word limit or a reading time. A limit from the user wins over
   every default. With none, the default is 1,500 words, which is 8 minutes at
   the 200 wpm the site uses. Recent posts run 1,200 to 2,000.
2. **External references.** Sources the post cites and links. A pasted paper,
   deck or URL counts as the answer. With none, cite every standard and CVE the
   post names, and nothing beyond that.
3. **Audience.** Platform or DevOps engineer, security engineer or analyst,
   security lead, or CISO.

When the user supplied sources and a length and left the audience open, do not
stop. Pick the audience the sources imply, say which one you picked in the reply,
and write. Ask once, never mid-draft, and never when the user said "go with your
recommendation".

## Writing a Post, Step by Step

**1. Resolve the topic against what already exists.**

```bash
grep -i "<topic keyword>" .claude/skills/accuknox-blog-writer/sources/blog.md
```

A near-duplicate slug means the job is an update, not a new post. Say so before
you write 1,500 words nobody needed.

**2. Read the sources the user gave you.** A PDF, deck or docx opens with one
command that always writes UTF-8 and needs no poppler:

```bash
python .claude/skills/accuknox-blog-writer/scripts/extract_text.py "D:/Downloads/paper.pdf"
```

Open the file it prints with the Read tool. Check every figure you plan to quote
against the source text, because a summary memo can round or merge numbers.

**3. Pull the AccuKnox pages.** Product positioning comes from accuknox.com,
product behavior comes from this repo's `docs/`.

```bash
cd .claude/skills/accuknox-blog-writer
python scripts/fetch_md.py platform/cspm solutions/ai-red-teaming --out /tmp/research
python scripts/fetch_md.py blog/<closest-existing-post> --headings
```

Read a hub page before you drill. `comparisons.md`, `platform.md` and `blog.md`
each list their whole section in one fetch. `references/source-of-truth.md` has
the full method, the Firecrawl fallback and the help.accuknox.com URL rules.

accuknox.com sits behind Cloudflare. A `.md` twin can return 404 or 530, and curl
returns 403, even for a page that is live. Fall back in this order: the matching
page under `docs/`, the Browser pane, then Firecrawl. Do not treat the failure as
proof that the page is gone.

**4. Read the layout spec.** `references/blog-layout.md`. It carries the section
order, the front matter, the TL;DR shape, the heading rule, the table rule, the
image rules and the link budget, all derived from the six most recent live posts.

**5. Pick the images.** At least one is a real product screenshot.
`references/asset-kit.md` names the sources and `references/blog-layout.md` names
the order to try them.

```bash
cd .claude/skills/accuknox-blog-writer
python scripts/images.py find agentz trace
python scripts/images.py prep SRC.webp ../../../references/drafts/blog/images/<slug>/name.png --crop x0,y0,x1,y1
python scripts/drive_sync.py check
```

`images.py find` searches the help-doc images with their alt text, the demo set
and the PRODUCT UI index in one pass. `prep` converts webp, crops, and downscales.
Open every crop and look at it before you use it. A concept with no screenshot
gets a diagram you render from HTML with Playwright, in AccuKnox navy. Never put
an image prompt in the draft or the front matter.

`drive_sync.py check` exits 1 once the manifest passes 90 days. Say so in your
reply rather than quietly working from a stale index.

**6. Start the draft.**

```bash
python scripts/new_draft.py <slug> --keyword "<primary keyword>"
```

It copies `assets/blog-template.md` to `references/drafts/blog/<slug>.md`, fills
the slug, the date and the author, and makes `images/<slug>/`. Never write a
draft in `docs/`.

**7. Write pass 1.** Do not evaluate while writing.

**8. Read it cold and answer three questions for yourself, in writing, unprinted.**
Which exact sentence would a reader call generated. Does the post state a
version, flag, score or control that no opened source supports. Which sentence
is the weakest, and does the post rest on it.

**9. Fix what pass 2 found, then run the gates.**

## The Front Matter Holds Eight Fields

The SEO table at the top of the Doc carries these and nothing else:

| Field | Rule |
| --- | --- |
| `slug` | Lowercase words joined by hyphens, under 65 characters |
| `title` | 45 to 60 characters, carries the primary keyword |
| `description` | 150 to 160 characters, carries the primary keyword |
| `author` | `Atharva Shah` unless told otherwise |
| `date` | `YYYY-MM-DD`, today for a new draft |
| `category` | A live accuknox.com category, such as `AI-SPM` or `CNAPP` |
| `primary_keyword` | The one phrase the post targets |
| `secondary_keywords` | A list of three to five supporting phrases |

No image prompt, no excerpt, no url, no reading time and no audience. WordPress
owns the cover image, the excerpt and the reading time. `grade.py` flags any
extra field, and flags a field with `prompt` in its name as HIGH.

## Heading and Image Rules

Every H2 is AP Title Case. The writer's global hook blocks a draft that breaks it,
and `grade.py` checks it too. `TL;DR` and `FAQs` stay as they are.

An italic line under an image says what the picture proves. Never open it with
the word `Caption` and never label it. Alt text says what the picture proves and
never opens with `a screenshot of`.

## Grading a Post

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

## The Gates

One command runs all three gates and prints one line each:

```bash
cd .claude/skills/accuknox-blog-writer
python scripts/gates.py <draft.md> --min-words 800 --max-words 1199
```

Pass the length the user set. `--max-words` counts every word in the body, tables
and headings included, so "under 1200 words" means `--max-words 1199`. Add
`--full` to print each gate's complete output. The three gates, run separately:

```bash
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

## Google Doc Is the Default Output

When the user says **blog output**, or asks for a blog without naming a format,
ship a Google Doc. Always write the markdown file to disk first, because that is
the artifact the repo keeps. Publishing runs through `gws`, which the user is
signed in to:

```bash
cd .claude/skills/accuknox-blog-writer
python scripts/push_gdoc.py <draft.md>
```

The script does five things:

1. Converts the draft to HTML with `to_gdoc_html.py`.
2. Embeds every local image as a base64 data URI sized to the page width, with
   its alt text, so the Doc carries the picture and nothing needs a public URL.
3. Creates the Google Doc, or replaces the body of the Doc it made last time. The
   Doc id lives in `<draft>.gdoc.json` beside the draft, so a revision keeps the
   same URL. Pass `--new` for a fresh Doc.
4. Sets line spacing to 100 on every paragraph, table cells included. 100 is
   single spacing and the tightest Docs offers. The converter also sets
   `line-height: 1` in the HTML.
5. Reads the Doc back and reports how many paragraphs sit at 100 and how many
   inline images arrived.

Use `--dry-run` to convert and stop, `--update <url>` to target a specific Doc and
`--folder <id>` to place a new one.

The front matter renders as an `SEO metadata` table at the top of the Doc,
because that is the block marketing copies into WordPress. Google Docs imports
`<pre>` as plain text, so the converter rewrites every fenced block as a one-cell
table, which keeps the line breaks and leading spaces. It also omits the `nl2br`
markdown extension, because a hard-wrapped paragraph would otherwise arrive with a
line break after every source line.

Reply with the Doc URL, the local markdown path, the gate results and the word
count. If `gws auth status` shows an invalid token, say so. A person at a browser
has to run `gws auth login`. Then hand over the `<draft>.gdoc.html` path, because
`File > Open` in Google Docs turns it into the same document.

`gws` refuses an upload path outside its working directory. `push_gdoc.py` handles
that, and any hand-rolled `gws drive files create --upload` call must run from the
file's own folder.

## What This Skill Does Not Write

WordPress injects the table of contents, the social share row, the byline, the
reading-time line, the `Ready For A Personalized Security Assessment` CTA, the
three customer testimonials and the `Continue Reading` block. Write none of it.
A draft that hand-rolls a CTA duplicates the template.

No cover image file and no image prompt. The cover belongs to WordPress.

Do write one thing the template does not inject: a YouTube embed from the
AccuKnox channel, [@AccuKnox](https://www.youtube.com/@AccuKnox). Pick the most
relevant video for the topic, place it in an H2 before the FAQ, and write it as
an iframe in a fenced `html` block so the Google Doc converter renders it as a
copy-paste code cell. `references/blog-layout.md` carries the exact shape. Verify
the video is on the channel, because a `youtu.be` link from an email is not
always AccuKnox content. The product page for the topic often links the right
video, so read its links first.

## Keep the Sources Fresh

```bash
python scripts/refresh_sources.py --check    # exits 1 when a bucket is 30 days old
python scripts/refresh_sources.py            # rebuild all ten buckets
```

The inventory is a fast index, never proof. `platform/aispm` is live and missing
from the sitemap. `platform/prompt-firewall` is linked from a published post and
returns 404. Only `verify_links.py` settles it.

## Files in This Skill

| Path | What it holds |
| --- | --- |
| `references/blog-layout.md` | The section order, front matter, image rules and every layout rule |
| `references/source-of-truth.md` | Shared. The `.md` twin trick, the sitemap map, help-docs URL rules, Firecrawl |
| `references/house-style.md` | Shared. The AI watermarks a word list misses, plus tables, bullets and callouts |
| `references/asset-kit.md` | Shared. Image sources, screenshot cleanup, brand colors and fonts |
| `references/seo-audit.md` | The judgement half of the audit that no script can run |
| `assets/blog-template.md` | The file `new_draft.py` copies to start a draft |
| `sources/*.md` | Shared. Cached accuknox.com URL inventory, ten buckets |
| `media/INDEX.md`, `media/MANIFEST.json` | Shared. The PRODUCT UI Drive library, 298 files indexed |
| `scripts/new_draft.py` | Start a draft from the template with the fixed fields filled |
| `scripts/extract_text.py` | Text out of a PDF, docx or pptx, always UTF-8, no poppler |
| `scripts/images.py` | Find a real image by keyword, then crop and convert it |
| `scripts/gates.py` | Run grade, links and slop in order and print one summary |
| `scripts/grade.py` | Deterministic SEO and structure score |
| `scripts/verify_links.py` | Every link resolves, anchors are descriptive |
| `scripts/slop.py` | The shared slop scorer, with the `TL;DR` collision accounted for |
| `scripts/to_gdoc_html.py` | Markdown to the HTML Google Drive imports as a Doc |
| `scripts/push_gdoc.py` | Publish or update the Doc through `gws`, line spacing 100 |
| `scripts/refresh_sources.py` | Rebuild the inventory from the sitemap index |
| `scripts/drive_sync.py` | Index, search and mirror the PRODUCT UI Drive folder |
| `scripts/fetch_md.py` | Read any accuknox.com page as markdown, boilerplate stripped |
| `scripts/selftest.py` | Proves the scripts still work, offline where it can |

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
