# AccuKnox Help Docs

Source repository for the [AccuKnox Help Center](https://help.accuknox.com/) — the public documentation site for the AccuKnox Cloud Native Application Protection Platform (CNAPP).

Built with [MkDocs](https://www.mkdocs.org/) and the [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) theme.

---

## Prerequisites

- Python 3.9+
- pip

## Quick Start

```sh
# Install dependencies
pip install mkdocs-material mkdocs-material-extensions pymdown-extensions mkdocs-macros-plugin mkdocs-embed-external-markdown mkdocs-redirects neoteroi-mkdocs mkdocs-breadcrumbs-plugin

# Start the local dev server (http://127.0.0.1:8000)
mkdocs serve

# Production build (outputs to site/)
mkdocs build --strict
```

## Directory Structure

```
.
+-- mkdocs.yml              # Site configuration, navigation, theme, extensions
+-- Makefile                 # Card generation targets (use-cases templates)
+-- docs/                   # All documentation content
|   +-- index.md            # Homepage (custom HTML/JS landing page)
|   +-- faqs.md             # FAQs page
|   +-- robots.txt          # Search engine crawl rules
|   +-- assets/
|   |   +-- images/         # Logos, favicons, shared images
|   |   +-- icons/          # SVG icons for cards and UI
|   |   +-- stylesheets/    # Custom CSS (theme overrides, neoteroi cards, banner)
|   +-- javascripts/
|   |   +-- extra.js        # Analytics, beta badges, trailing-slash redirect
|   +-- getting-started/    # Platform setup, release notes, architecture, on-prem
|   +-- how-to/             # Step-by-step onboarding and configuration guides
|   |   +-- vm-security/    # VM agent-based and agentless guides
|   +-- integrations/       # CI/CD, SIEM, ticketing, SSO, API, AI integrations
|   +-- use-cases/          # Feature use-case walkthroughs (CSPM, CWPP, KSPM, etc.)
|   |   +-- cloud/          # Cloud-provider-specific CSPM use cases
|   |   +-- cards/          # Auto-generated card content (see Makefile)
|   |   +-- res/            # Abbreviated resource snippets for card templates
|   +-- support-matrix/     # Compatibility matrices (CI/CD, cloud, VM, registry, IaC)
|   +-- resources/          # Architecture, troubleshooting, pricing, glossary
|   +-- knoxctl/            # knoxctl CLI documentation
|   +-- introduction/       # Open-source vs enterprise comparison
+-- overrides/              # Material theme template overrides
|   +-- main.html           # Base template: adds announcement banner via announce block
|   +-- partials/
|       +-- banner.html     # Dismissible banner for latest release
|       +-- logo.html       # Light/dark mode logo switcher
|       +-- tabs.html       # Navigation tabs with support ticket link
+-- site/                   # Build output (git-ignored)
```

## Navigation Structure

The site has **six top-level tabs** defined in the `nav:` section of `mkdocs.yml`:

| Tab | Path Prefix | Content |
|-----|-------------|---------|
| Home | `index.md` | Custom landing page with interactive module explorer |
| Getting Started | `how-to/`, `getting-started/` | Onboarding playbooks, cloud/K8s/VM setup, on-prem, CLI |
| Integrations | `integrations/` | CI/CD pipelines, SIEM, ticketing, SSO, notifications |
| Use-Cases | `use-cases/` | Feature walkthroughs per product area (CSPM, CWPP, KSPM, ASPM, AI/ML, VM) |
| Support Matrix | `support-matrix/` | Compatibility tables for platforms, regions, registries |
| Resources | `resources/` | Architecture, troubleshooting, pricing calculators, release notes |
| FAQs | `faqs.md` | Frequently asked questions |

## Content Conventions

### Front Matter

Every markdown file should start with YAML front matter:

```yaml
---
title: Human-Readable Page Title
description: A concise 1-2 sentence description for SEO and social sharing.
---
```

For landing pages that use card grids, hide the table of contents:

```yaml
---
title: Page Title
description: Short description.
hide:
  - toc
---
```

### Headings

- Every content page must have exactly **one H1** (`# Heading`) matching the nav label.
- Use H2 (`##`) and H3 (`###`) for subsections. The theme renders up to 3 levels in the TOC (`toc_depth: 3`).

### Neoteroi Cards

Landing and overview pages use the [neoteroi-mkdocs](https://www.neoteroi.dev/mkdocs-plugins/) cards plugin for grid navigation:

```markdown
::cards:: cols=3

- title: Card Title
  image: ./icons/icon-name.svg
  url: /section/page-slug/

::/cards::
```

Common column counts: `cols=2` for narrow layouts, `cols=3` for section overviews, `cols=4` for dense grids.

## Adding a New Page

1. Create the `.md` file in the appropriate `docs/` subdirectory.
2. Add YAML front matter with `title` and `description`.
3. Write an H1 heading matching the title.
4. Add the page to the `nav:` section in `mkdocs.yml` at the correct hierarchy level.
5. Run `mkdocs serve` and verify the page renders correctly.

## Custom Overrides

| Override | Purpose |
|----------|---------|
| `overrides/main.html` | Extends Material base template; injects the announcement banner via the `announce` block |
| `overrides/partials/banner.html` | Dismissible banner for the latest release (update version and link when releasing) |
| `overrides/partials/logo.html` | Dual logo system for light and dark color schemes |
| `overrides/partials/tabs.html` | Navigation tabs with a 24/7 support ticket link and usage tracking pixel |

## Auto-Generated Content

The `Makefile` has a `hardening` target that generates card-based pages from `.template` files in `docs/use-cases/`:

```sh
make hardening
```

This runs `docs/use-cases/generate-cards.sh` against `hardening.template`, `zero-trust.template`, and `forensics.template` to produce card content in `docs/use-cases/cards/`.

## Useful Commands

| Command | Description |
|---------|-------------|
| `mkdocs serve` | Start local dev server with hot-reload at `http://127.0.0.1:8000` |
| `mkdocs build` | Build the static site into `site/` |
| `mkdocs build --strict` | Build with strict mode — fails on warnings (recommended for CI) |
| `make hardening` | Regenerate use-case card pages from templates |

## Architecture Overview

![AccuKnox High Level Design](./docs/introduction/images/accuknox-architecture.png)
