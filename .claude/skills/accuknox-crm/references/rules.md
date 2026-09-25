# CRM Write Rules

Each rule below comes from the trycompai/crm source on the `release` branch
(`apps/api/src`, `packages/db/src`, `docs/api.md`) or from the September 2026
Salesforce import. When a call fails in an unexpected way, read the service file
named in the rule.

## Every Create Queues Agent Work

`companies.service.ts` and `contacts.service.ts` call `agent-trigger.service.ts`
on every create. The API has no switch to turn this off.

| Create | Tasks queued |
|---|---|
| Company | `brand` (budget 2), `company-profile` (budget 4), `agent-event` (budget 1) |
| Contact | `identify` (budget 4), `agent-event` (budget 1) |
| Deal | `agent-event`, plus a second `agent-event` for `deal.closed` when the stage is closed |

The budget is the number of paid vendor calls a task may spend, such as Context
brand and LinkedIn data. The agent model also bills tokens (see
`GET /settings/agent-model`). The September 2026 import of about 30,000
companies and 8,000 contacts queued about 120,000 tasks. Tell the user the count
before a large run. `crm.py queue` shows what is waiting.

## Archive Is Deletion on a Timer

`POST /{entity}/{id}/archive` sets `archivedAt`. A cron job purges archived rows
after `archiveRetentionDays`, which defaults to 180 (`GET
/settings/archive-retention`). Purging a contact also suppresses its email
address, so the mailbox sync never recreates the contact. So never archive a
record to mean "closed" or "inactive". Keep it active and record the status in a
field.

## A Duplicate Domain or Email Returns 409

- A company domain is unique among active companies. The server normalizes the
  domain (lower case, no scheme, no `www.`) and returns 409 on a clash. Leave
  out social or hosting sites such as linkedin.com and linktr.ee. Otherwise every
  company with that site as its website claims the same domain.
- A contact email is unique and case-insensitive, and a clash returns 409.
- The server checks emails with zod `z.email()`, which rejects masked addresses
  such as `kp.@example.com`. A failed check fails the whole create with 400. Check
  emails with the same pattern first (`EMAIL_RE` in
  `examples/salesforce_import.py`), and drop an email that fails the check.
- A contact created with no `companyId` is matched to a company by its email
  domain. The server creates that company when none exists, and that create
  queues more agent tasks. A free-mail address such as gmail.com gets no company.

## A Deal Needs a Real Owner and Cents

- `name`, `companyId` and `ownerId` are required. `ownerId` must be a real user
  id from `GET /users`.
- Stages: `DEMO_BOOKED`, `QUALIFIED_TO_BUY`, `UNQUALIFIED_TO_BUY`,
  `DECISION_MAKER_BOUGHT_IN`, `CONTRACT_SENT`, `CLOSED_WON`, `CLOSED_LOST`.
- `amountCents` is an integer in minor units, so 5,000 USD is `500000`.
  `currency` is an ISO code. Only `baseAmountCents` is safe to sum across
  currencies.
- `POST /deals/{dealId}/contacts` links a contact to a deal only when that
  contact works at the deal's company. It returns 400 otherwise. A `role` has at
  most 80 characters. Linking again keeps the existing role.

## Set agentFilled False on Imported Fields

- `POST /fields` takes `entity` (`COMPANY`, `CONTACT` or `DEAL`), `label` and
  `type` (`TEXT`, `LONG_TEXT`, `NUMBER`, `DATE`, `CHECKBOX`, `SELECT`, `URL`,
  `EMAIL`, `PHONE`, `USER`). The server derives the `key` from the label. Read it
  back with `crm.py fields`.
- `agentFilled` defaults to true, and the agent then fills the field. Set it to
  false for imported history that the agent must not overwrite.
- Set values through PATCH `data.fields`, a map from field key to value. A
  `SELECT` value can be the option id or the option label (case-insensitive). A
  `DATE` value is `YYYY-MM-DD`. A value the field does not accept fails the whole
  PATCH with 400, so retry the PATCH without `fields` to keep the other changes.

## Eight Threads Give 5 to 10 Creates per Second

- One call takes about 0.7 to 1.5 seconds. Eight threads give about 5 to 10
  creates per second.
- Search gets slower as tables grow. With more than 30,000 companies, a search
  takes about 1.3 seconds.
- Retry 429 and 5xx responses with backoff, and never retry a 4xx.
