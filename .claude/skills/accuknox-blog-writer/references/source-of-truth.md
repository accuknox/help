# Where every fact and every link comes from

Four sources, in priority order. Go down the list only when the one above it
does not hold the answer.

1. **This repo.** `docs/`, `mkdocs.yml`, `references/`. Product behaviour,
   console paths, supported platforms, screenshots.
2. **accuknox.com through its `.md` twins.** Positioning, feature names,
   customer stories, competitor comparisons, press.
3. **Firecrawl.** Anything off both domains. A standard, an advisory, a
   competitor page, a news item, an analyst figure.
4. **A bracket.** When nobody has the fact, write `[confirm the minimum agent
   version]` and leave it. The accuracy rule in
   `.claude/core/runtime-contract.md` outranks any instruction to fill it in.

## accuknox.com serves markdown

Append `.md` to any page path and the site returns YAML front matter plus the
body as clean markdown:

```bash
curl -sL https://accuknox.com/comparisons.md
curl -sL https://accuknox.com/blog/ai-spm-tools.md
curl -sL https://accuknox.com/platform/cspm.md
```

Front matter carries `title`, `id`, `type`, `slug`, `published_at`,
`modified_at`, `url`, `markdown_url`, `excerpt` and `taxonomy_category`.

Use the wrapper rather than raw curl. It strips the WordPress boilerplate and
reports the body word count:

```bash
python scripts/fetch_md.py platform/cspm
python scripts/fetch_md.py blog/ai-spm-tools --headings
python scripts/fetch_md.py comparisons blog/ai-spm-tools --out research/
```

Read a hub page first, then drill. `comparisons.md` lists every comparison with
its one-line pitch in 15 KB, which is far cheaper than fetching 55 pages.
The same holds for `platform.md`, `solutions.md` and `blog.md`.

Not every page has a twin. `platform/aispm` returns 200 as HTML and 404 as
`.md`. Fall back to Firecrawl on a 404.

## The cached URL inventory

`sources/` holds one markdown table per bucket, rebuilt from the sitemap index:

| File | What it lists |
| --- | --- |
| `sources/platform.md` | `/platform/*` capability pages |
| `sources/solutions.md` | `/solutions/*` outcome pages |
| `sources/comparisons.md` | `/comparisons/*` versus and alternatives pages |
| `sources/blog.md` | every `/blog/*` post, newest first |
| `sources/press-release.md` | `/press/*` announcements |
| `sources/case-study.md` | `/case-studies/*` customer stories |
| `sources/resources.md` | white papers, ebooks, datasheets, videos, CVEs, use cases |
| `sources/company.md`, `sources/product.md`, `sources/other.md` | everything else |

Rebuild them when the newest row is more than a month old:

```bash
python scripts/refresh_sources.py --check    # report staleness only
python scripts/refresh_sources.py            # rebuild every bucket
```

**The sitemap is not exhaustive.** `platform/aispm` is live and absent from it.
Treat `sources/` as a fast index, never as proof a URL does or does not exist.

## Links that are live today

`platform/prompt-firewall` and `platform/ai-dr` both return 404 while a
published post links to them. A slug that worked last quarter is not a slug that
works now, so verify every link in the draft:

```bash
python scripts/verify_links.py draft.md --fix-suggestions
```

It checks each URL, flags weak anchor text, flags bare URLs in prose, and for a
broken accuknox.com link names the closest slugs in `sources/`.

## help.accuknox.com, built from mkdocs.yml

This repo is the site. Build the URL from the file path:

- Base `https://help.accuknox.com/`, directory URLs, trailing slash, no `.md`.
- `docs/<path>/page.md` becomes `https://help.accuknox.com/<path>/page/`
- `docs/<path>/index.md` becomes `https://help.accuknox.com/<path>/`

Find the page by searching the `nav:` block in `mkdocs.yml`, or by reading the
generated `docs/<section>/README.md`, which lists every page and what it covers.

Some nav entries are already absolute URLs, such as the compliance matrix
pointing at `https://accuknox.com/compliance`. Use those verbatim.

```bash
grep -n "runtime-sec-arch\|prompt-firewall" mkdocs.yml
```

## Firecrawl, for everything off both domains

The CLI is installed and reads its key from `D:\Atharva\NOTES\.env` through the
rotation script. Reach for it when the topic needs an external reference:

```bash
firecrawl scrape "https://www.cisa.gov/known-exploited-vulnerabilities-catalog"
firecrawl search "OWASP Top 10 for LLM Applications 2025" --limit 5
```

On `Insufficient credits`, rotate and retry:

```bash
python "D:\Atharva\NOTES\SCRIPTS\keys\keys.py" activate
```

Always ask for the external references you want before you draft. A post with a
standard cited and linked outranks the same post with the standard named and
unlinked, and the ask costs one line.

Do not scrape what the repo or a `.md` twin already holds.

## What a competitor claim needs

Never attack a competitor. Compare on a named capability with a source, or drop
the comparison. `writing-rules.md` section 10 is hard on this, and a comparison
sourced from a competitor's own documentation is the only version that survives
their legal team reading it.

`references/comparisons-builder/` in this repo holds the existing comparison
work. Read it before you write a versus paragraph.

## Related

- `references/asset-kit.md`, images, brand colors, templates, the PRODUCT UI library
- `references/blog-layout.md`, the shape the facts go into
- `.claude/core/runtime-contract.md`, the accuracy rule that outranks all of this
