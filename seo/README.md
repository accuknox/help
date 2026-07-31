# AccuKnox SEO workspace

Working folder for the accuknox.com marketing-site SEO effort. Notes, exports, keyword lists, competitor research, and reports live here over time so future sessions don't start cold.

## Scope

- **Site**: accuknox.com marketing site only. Not this docs site, not a blog subdomain — those are out of scope for this effort.
- **OpenSEO project**: `Default` (`projectId: 9de7506c-6c9c-4264-92c7-e48848e10195`), org `E3cYuJTfl9bUNJpBN9QYCdFEHgd7uze9`.
- **GSC**: connected (`sc-domain:accuknox.com`), live via `get_search_console_performance`.
- **Rank tracker**: one active config (`5e962bc8-c678-4c94-9f12-23068dc53d4d`), US/en, desktop, weekly, SERP depth 40. No keywords attached yet.
- **Saved keywords**: none yet.

## Goals

- More inbound (trial/demo signups, qualified traffic)
- More ranking, specifically for non-branded/buying-intent terms — current GSC top queries are branded (`accuknox`, `accuknox careers`, misspellings) or off-topic (`dvwa`), so there's not much non-branded footing yet
- No fixed deadline given; treat as an ongoing program

## Target markets

- **US** — primary, majority of effort
- Europe, UAE, India — secondary markets to account for in keyword/location targeting

Note: the existing rank tracker config is US-only (location 2840). Extending tracking to the other markets is a `keyword-research`/tracking follow-up, not done yet.

## Positioning source of truth

Do **not** use `utils/content-planning/` — outdated. Do not lean on this docs repo generally, since it's the docs site (not accuknox.com) and has stale content.

**Primary signal source: OpenSEO MCP data** (GSC performance, SERP results, domain/keyword data, rank tracker) — treat this as ground truth over any file in this repo.

## Folder structure

- `gsc/` — GSC CSV exports, if ever needed as a fallback (GSC is connected live, so this should stay mostly empty)
- `keywords/` — keyword research exports, saved keyword lists, clustering output
- `competitors/` — competitor domain/keyword/backlink research
- `content/` — briefs, drafts, content mapped to keyword clusters
- `outreach/` — link prospecting lists and outreach notes
- `reports/` — audit reports, periodic summaries

## Next steps

Recommended first workflow: `keyword-research` to build a non-branded, buying-intent keyword base (US-weighted, with EU/UAE/India variants where relevant), since there's no saved keyword list yet and current organic visibility is mostly branded.
