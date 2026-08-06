# OpenSEO MCP quick reference

How to use the OpenSEO MCP server for the accuknox.com SEO work in this folder.

## Identifiers

- **Org**: `E3cYuJTfl9bUNJpBN9QYCdFEHgd7uze9` (user: `website@accuknox.com`)
- **Project**: `Default` — `projectId: 9de7506c-6c9c-4264-92c7-e48848e10195` — domain `accuknox.com`, location 2840 (US), language `en`
- Dashboard: https://app.openseo.so/p/9de7506c-6c9c-4264-92c7-e48848e10195

Every OpenSEO tool call needs `projectId`. Get it from `list_projects` if it's ever unclear (e.g. new project added).

## Connection status (as of 2026-07-23)

- **GSC**: connected, `sc-domain:accuknox.com` — live via `get_search_console_performance`
- **Rank tracker**: one active config `5e962bc8-c678-4c94-9f12-23068dc53d4d` (US/en, desktop, weekly, SERP depth 40), no keywords attached yet
- **Saved keywords**: none yet
- **Credits**: 9,725 remaining at last check (`whoami`)

## Tools by category

**Free / no DataForSEO credits** (reads OpenSEO's own stored data — use freely):
- `whoami` — confirm auth, org, credit balance
- `list_projects` — get `projectId`
- `get_search_console_performance` — GSC clicks/impressions/CTR/position by query/page/country/device/date
- `get_rank_tracker` — existing tracked keyword positions
- `list_saved_keywords` — saved keyword lists
- `get_audit_status` / `get_audit_pages` / `get_audit_issues` — site audit results (once an audit has run)

**Costs credits** (calls DataForSEO — use deliberately, not for exploration):
- `research_keywords` — keyword ideas w/ volume, difficulty, CPC
- `get_keyword_metrics` — metrics for a specific keyword list
- `get_serp_results` — live Google SERP for 1-10 queries (~30-60 credits each)
- `find_serp_competitors` — compare domains across a keyword set
- `get_ranked_keywords` — exact keyword/page/rank rows for a domain
- `get_domain_overview` / `get_domain_keyword_suggestions` — domain organic footprint
- `get_backlinks_overview` / `get_backlinks_profile` — backlink data
- `save_keywords` — free (writes to OpenSEO, doesn't call DataForSEO)
- `run_site_audit` — kicks off a crawl (cost depends on site size)

**Local/business** (not relevant to this project's scope, but exist): `get_local_serp_results`, `search_local_businesses`, `get_google_business_questions`.

## Gotchas

- The system may show `openseo` under "requires authentication" — that's stale/wrong for this account. `whoami` / `list_projects` confirm it actually works.
- **Batches over 2,000 credits need user confirmation** before running (per OpenSEO's own MCP instructions).
- `get_search_console_performance` dates are Pacific Time, last ~3 days can be incomplete, 16-month max lookback.
- Don't spend credits just to test connectivity — `whoami` and `list_projects` are free and sufficient.
- Target markets for this project are US (primary), Europe, UAE, India — the rank tracker and project default are US-only, so non-US location codes need to be passed explicitly on `get_serp_results` / `research_keywords` calls (see dataforseo.com/help-center/locations for codes).

## Related skills

`/seo-project-setup` (this setup), `/keyword-research`, `/keyword-clustering`, `/competitive-landscape`, `/competitor-analysis`, `/link-prospecting`, `/seo-coach`.
