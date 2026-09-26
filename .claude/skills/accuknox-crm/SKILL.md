---
name: accuknox-crm
description: Read, query, reshape and bulk-edit data in the AccuKnox CRM at crm.accuknox.com (the open-source trycompai/crm app) through its REST API and live OpenAPI spec. Use this skill whenever the user mentions the CRM, crm.accuknox.com, a crm_ API key, or wants to look up, export, count, import, update, merge, restage, reassign or clean companies, contacts, people, orgs, accounts, deals or opportunities, custom fields, owners, the agent or enrichment queue, even when they do not say "API". Also use it for a CSV or Salesforce/HubSpot export that should land in the CRM, and for questions like "how many deals closed this quarter" or "which accounts have no owner".
---

# AccuKnox CRM

The CRM is the self-hosted trycompai/crm app at `https://crm.accuknox.com`. The
API key authenticates as the person who made it, with that person's role, so an
owner's key can do anything the owner can do in the UI, including delete.

## Check the Key Before the First Call

1. Get the key from the user. Read it from `CRM_API_KEY` in the environment, and
   never write it to a file, a commit or a log. `scripts/crm.py` also reads a
   `CRM_API_KEY=` line from `./.env`, or from the file named by `CRM_ENV_FILE`.
2. Check the key before any other call.

```bash
python scripts/crm.py whoami
```

3. Find the endpoint. The spec is live, so it is always current.

```bash
python scripts/crm.py spec                # every endpoint, grouped by tag
python scripts/crm.py spec --path /deals  # request schema for matching paths
```

`references/endpoints.txt` is a snapshot of that list from 2026-09-25. Read it
when the network is down, and trust the live spec when the two disagree.

## Nine Commands Cover Most CRM Jobs

| Job | Command |
|---|---|
| Check the key and the workspace | `crm.py whoami` |
| Count records | `crm.py counts` |
| List users, the valid `ownerId` values | `crm.py users` |
| List custom fields with keys, types and options | `crm.py fields COMPANY` (or `CONTACT`, `DEAL`) |
| Search and export | `crm.py search deals --filter '{"stage":["CLOSED_WON"]}' --all --out won.csv` |
| Read one record | `crm.py get companies <id>` |
| Call any endpoint | `crm.py call POST /deals/bulk-set-stage --data @body.json` |
| Create or update from a CSV | `crm.py bulk update contacts edits.csv --dry-run` |
| See the agent queue | `crm.py queue` |

For work that needs logic, import the client instead of chaining CLI calls:

```python
import sys; sys.path.insert(0, ".claude/skills/accuknox-crm/scripts")  # from the repo root
from crm import Crm
crm = Crm()
for deal in crm.search_all("deals", {"stage": ["CONTRACT_SENT"]}):
    crm.patch(f"/deals/{deal['id']}", {"fields": {"potential": "Highest"}})
```

`Crm.call` retries 429 and 5xx responses, and raises `CrmError` for any other
failure. `search_all` pages through results 100 rows at a time.

## Lists Are POST Searches and Creates Take Few Fields

- **Two route families.** tRPC procedures sit under `/rest` (companies, contacts,
  deals, fields, users and most others). Nest controllers sit at the site root
  (`/auth/*`, `/health`, `/internal/*`, `/api/*`). In the spec, a root route has an
  `operationId` like `AuthController_getMe`. The client picks the right prefix
  for you.
- **Lists are POST searches.** `POST /{companies|contacts|deals}/search` takes
  `q`, `page`, `pageSize` (at most 100), `archived` and array filters such as
  `stage`, `owner`, `industry` and `fields`. The response is
  `{rows, total, facetCounts}`.
- **Creates take a few fields.** Put everything else in a PATCH after the create.
  PATCH bodies are wrapped as `{"data": {...}}`, and `crm.patch` does the
  wrapping.
- **There is no bulk create.** Make one call per record. For bulk changes to
  existing records, use `bulk-assign-owner`, `bulk-set-stage` and
  `bulk-set-company`.

Read `references/rules.md` before you write to the CRM. It holds the rules that
cause silent damage, such as archive meaning deletion after 180 days, and every
create queueing paid agent work.

## Pilot Five Records Before a Bulk Write

1. Search first, so the write does not make duplicates. A company domain and a
   contact email are unique, and a duplicate create returns 409.
2. Run the write on 1 to 5 records, then read them back with `crm.py get`.
3. For more than about 50 creates, tell the user how many agent tasks the run
   will queue (see `references/rules.md`), and get a yes first.
4. Keep a state file that maps each source row to the CRM id it produced, so a
   rerun resumes. `crm.py bulk` and `examples/salesforce_import.py` both do this.

`crm.py call` refuses DELETE, purge, revoke, API-key creation and changes to
workspace, SSO, settings, currency, tracking and Slack unless you pass `--yes`.
Get the user's explicit go-ahead before you pass it.

## The Salesforce Import Moved 109,000 Records

`examples/salesforce_import.py` imported a Salesforce export of 33,291 accounts,
72,705 contacts and 3,496 opportunities. It shows the full pattern: dedupe
against the CRM, map stages and owners, create custom fields with
`agentFilled: false`, link contacts to deals, run 8 threads, resume from a state
file and log failures to `errors.csv`. Copy it when a new import comes in.
