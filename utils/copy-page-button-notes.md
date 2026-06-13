# Copy page / Open in LLM button — implementation notes

A native MkDocs implementation of the Firecrawl-style "Copy page" split-button
with options to:

- Copy the page as Markdown to the clipboard
- View the raw Markdown source in a new tab
- Open the current page in ChatGPT with a prefilled prompt
- Open the current page in Claude with a prefilled prompt

No paid plugin. No third-party dependency. Pure MkDocs hook + a small JS/CSS pair.

## Why this is hard at first glance

MkDocs ships HTML to the browser. To do "copy as Markdown" you need the original
`.md` source available client-side. Firecrawl-style sites usually solve this
with a custom backend or a paid plugin like `mkdocs-llmstxt`. Neither is
acceptable here.

The trick: ask MkDocs to copy each `.md` source into the built site next to its
rendered HTML, so a page at `/foo/bar/` has a sibling raw markdown file at
`/foo/bar/index.md`. The JS then `fetch()`es that file on demand.

## What was added

1. **`hooks/copy_md_source.py`** — a MkDocs build hook.
   Hooks are a stock MkDocs feature (`hooks:` key in `mkdocs.yml`). No plugin
   needed. The hook runs `on_post_build` and walks `docs_dir`, copying every
   `.md` to its `site_dir` counterpart at `<page-url>index.md`. With
   `use_directory_urls: true` (the default in this project), `docs/foo/bar.md`
   serves as `/foo/bar/`, so we write the raw markdown to `site/foo/bar/index.md`.

2. **`docs/javascripts/copy-page.js`** — injects the button into every article.
   - Locates `article.md-content__inner` and inserts a split-button right above
     the `<h1>`.
   - The main button copies the markdown. The caret opens a dropdown with the
     four actions.
   - Hooks into Material's `window.document$` observable so the button survives
     SPA-style instant navigation (`navigation.instant` is enabled in this repo).
   - "Copy page" uses `navigator.clipboard.writeText()` with the markdown text
     fetched from `<page-url>index.md`.
   - "View as Markdown" opens that same URL in a new tab — browsers render `.md`
     as plain text by default, which matches the Firecrawl behavior.
   - "Open in ChatGPT" → `https://chatgpt.com/?hints=search&q=<prefilled prompt>`.
   - "Open in Claude" → `https://claude.ai/new?q=<prefilled prompt>`.
   - The prefilled prompt includes the page title and full URL so the LLM can
     fetch the page itself.

3. **`docs/assets/stylesheets/copy-page.css`** — styles the button and dropdown
   using Material's CSS variables (`--md-default-bg-color`,
   `--md-default-fg-color--lightest`, etc.) so it auto-themes with light/dark
   mode. The button floats right of the H1 on desktop and stacks above the H1 on
   mobile.

4. **`mkdocs.yml`** — added three lines:
   - `hooks:` block pointing at `hooks/copy_md_source.py`.
   - `copy-page.css` added to `extra_css`.
   - `javascripts/copy-page.js` added to `extra_javascript`.

## How it works at runtime

```
User visits /how-to/aws-onboarding/
   │
   ├─ HTML loads, copy-page.js runs
   │   └─ injects <div class="ak-copy-page"> above <h1>
   │
   ├─ User clicks "Copy page"
   │   └─ fetch('/how-to/aws-onboarding/index.md')
   │       └─ served by the static file written by the hook at build time
   │           └─ navigator.clipboard.writeText(text)
   │
   ├─ User clicks "Open in ChatGPT"
   │   └─ window.open('https://chatgpt.com/?q=Read https://help.accuknox.com/how-to/aws-onboarding/ ...')
   │       └─ ChatGPT fetches the page itself
```

## Things to know if you touch this later

- **SPA navigation matters.** Material's `navigation.instant` swaps page bodies
  without a full reload. That's why injection runs through `window.document$`
  rather than `DOMContentLoaded`. If you ever remove `navigation.instant` from
  `mkdocs.yml`, the code still works via the `DOMContentLoaded` fallback.
- **Why `index.md` and not `page.md`?** With `use_directory_urls: true`, the
  page lives at a directory URL ending in `/`. Putting the raw md at the same
  directory as `index.md` keeps the URL-to-source mapping trivial: just append
  `index.md` to whatever `window.location.pathname` is.
- **The hook publishes ALL markdown.** Including pages excluded from the nav
  but still in `docs_dir`. If you have private drafts in `docs/` that should
  not be public, the hook will expose their raw sources too. Currently this
  matches MkDocs's own behavior (it would render them too unless explicitly
  excluded), so no new risk. Flag this if that changes.
- **No build-time markdown cleaning.** The raw `.md` is shipped as-is,
  including snippet includes (`--8<--`) that haven't been resolved and any
  `pymdownx`-specific syntax. That's fine for "copy for an LLM" (LLMs handle
  this) but is not pretty-printed reading material. If you want resolved
  markdown, the hook would need to hold the `on_page_markdown` output instead.
- **ChatGPT / Claude URL params.** Both currently accept a `?q=` query
  parameter that prefills the composer. If either changes their URL format,
  update `openChatGPT` / `openClaude` in `copy-page.js`.

## Files touched

- `mkdocs.yml` — added `hooks:`, one `extra_css` entry, one `extra_javascript` entry
- `hooks/copy_md_source.py` — new
- `docs/javascripts/copy-page.js` — new
- `docs/assets/stylesheets/copy-page.css` — new
