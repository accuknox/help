# PRD: AccuKnox POC and Customer Portal (MVP)

Owner: Atharva Shah. Requesters: Rahul Jadhav (CTO), Syed Hadi.
Status: Draft for the discussion with Syed. Date: 2026-10-23.

## Jira Leaves Teams Without One View of the Customer

Jira does not give the Solutions Engineering (SE) and Customer For Life (CFL) teams one view of a customer.

Evidence from the "POC / Customer portal" thread (22 Oct 2026):

- Status tickets go stale. Syed digs through threads and scrum notes to learn if a task is done.
- No consolidated list of pending items and owners per customer or POC.
- Syed follows up by hand on items a dashboard should show.
- Rahul: "we are not able to handle the customer support effectively with existing tools."

Evidence from the CFL minutes (22 Oct 2026):

- About 25 accounts are tracked as CM-### Jira tickets, each with a free-text update and a CSAT score from 0 to 4.
- The weekly sync copies status into Jira by hand.
- Support requests arrive as SUPPORT-### tickets through support@accuknox.com, separate from the CM board.
- Customer files (deployment guides, reports, POC decks) live in email, Drive and Slack. No team member sees the full exchange with one customer.

## One Workspace per Customer Replaces Scattered Status

One workspace per customer. It holds the POC or production onboarding status, open issues, roadmap commitments and every shared file. The system chases the team when a deadline slips.

### Success metrics (first 60 days)

| Metric | Target |
|---|---|
| Accounts moved from Jira CM board to the portal | 100% of active POCs, 10 pilot production accounts |
| Hours per week spent on manual status follow-up (Syed, self-reported) | Down 50% |
| SLA breaches alerted before the customer asks | 90% |
| Customer issues with a named owner and next-update date | 100% |
| Time to find any file shared with a customer | Under 1 minute |

## Five Roles Use the Portal

| Persona | Needs |
|---|---|
| SE (Solutions Engineer) | Run the POC checklist, update percent complete, upload artifacts, get nudged on misses |
| CSM and CFL lead (Syed) | See all accounts, all pending items and owners, one health score |
| Leadership (Rahul, Nat) | Portfolio view, SLA breaches, at-risk accounts, ask questions in plain English |
| Customer contact | See open actions, ETAs and shared files for their own workspace only. Reply or confirm a task |
| Sales and partner managers | Read-only view of POC state |

## Nine Features Fit the MVP

### In the MVP (build with Lovable)

**F1. Customer workspaces**
One workspace per customer. Type is POC prospect or Production customer. Fields: name, segment, region, deployment model (SaaS or on-prem), products in scope, customer advocate, SE owner, CSAT (0 to 4), start date, target close date.

**F2. POC templates and checklists**
Starting a POC creates an action list from a template. Three templates ship in the MVP, taken from the existing POC guides:

- CSPM on AWS (account scope, IAM role, asset tagging, Jira/Slack integration, scan, report)
- On-prem airgapped container security (control plane sizing, agent install, runtime use cases, report)
- Generic CNAPP POC (kickoff, prerequisites sent, onboarding session, success criteria agreed, mid-point review, executive summary, decision)

Each item has: title, owner, due date, percent complete, status, "customer-visible" flag, prerequisite-to-send flag.

POC stages: Qualified, Prerequisites Sent, Onboarding, Running, Readout, Decision (Won, Lost, Extended).

**F3. Issue tracking**
- Issues belong to a workspace. Fields: title, severity, owner, percent complete, status, next-update date, SLA clock.
- Customer submits an issue through a form on their portal page.
- An email to support@ creates an issue through an inbound-email webhook. The sender's domain maps to the workspace. Unmatched mail lands in a triage queue.
- Roadmap items: title, ETA, status, linked workspace, "committed to customer" flag.

**F4. Customer-facing view**
Invite a customer contact by email (magic link). They see only customer-visible items: open actions, issues, roadmap ETAs, files. They can submit an issue, comment, and confirm an action.

**F5. Status-change email**
When a team member updates a customer-visible item, the screen offers "Notify customer". It drafts an email to the customer contact. The team member edits and sends. Nothing sends without a click.

**F6. SLA and escalation alerts**
Rules per severity, for example: P1 first response 1 hour, update every 24 hours. When a clock expires, the portal:

1. alerts the owner on Slack and email,
2. after a second grace period alerts the owner's manager,
3. records a "miss" against the owner. Three misses in 30 days flags the owner on the leadership view.

**F7. Artifact storage**
Upload and download files per workspace. Tag by type (deck, report, guide, log, contract). Every upload and download is logged with who and when. Customer-visible flag per file. The whole team sees the full exchange.

**F8. Dashboards**
- Portfolio: all accounts with stage, CSAT, open issues, overdue items, next milestone.
- "Needs attention": overdue items, stale items (no update in 7 days), SLA breaches.
- Per-workspace timeline of status changes and files.

**F9. Ask AI**
A plain-English question box scoped to one workspace or the whole portfolio. Examples: "What is blocking Acme Bank?" and "Which POCs have prerequisites unsent for more than 3 days?" Answers cite the records used.

### Out of scope for the MVP

- Two-way sync with Jira. Plan a one-time CSV import of the CM board instead.
- Salesforce sync (phase 2).
- Billing, contracts, renewals workflow.
- Mobile app.
- Auto-ingest of Gmail threads beyond the support@ webhook.
- Custom template builder UI (templates ship as seed data).

## Four Flows Cover Daily Work

**Start a POC.** SE clicks New POC, picks a template, enters the customer and dates. The portal builds the checklist, marks which prerequisites to send, and offers a draft email with the prerequisites. SE invites the customer contact.

**Customer reports an issue.** Customer emails support@ or uses the form. The portal creates an issue, assigns the account owner, starts the SLA clock, and posts to Slack. The owner replies and sets a next-update date. A missed date triggers escalation.

**Weekly CFL sync.** Syed opens the portfolio view. Stale and overdue items show first. The meeting updates records in place, so the post-meeting Jira copy step goes away.

**Close a POC.** SE sets the decision, attaches the executive summary deck, and the portal archives the checklist and keeps the files.

## Thirteen Records Hold the Data

Workspace, Contact, TeamMember, POCTemplate, ChecklistItem, Issue, RoadmapItem, Comment, File, ActivityLog, SLARule, AlertEvent, EmailDraft.

Row-level security: team members see all workspaces. Customer contacts see only their own workspace and only items flagged customer-visible. Internal notes never reach the customer view.

## Security and Cost Limits Bound the Build

- Sign-in for staff through Google Workspace SSO (accuknox.com domain only).
- Customer sign-in through email magic link.
- Files stored in private buckets with signed URLs. No public links.
- Audit log on every status change, upload and download.
- Cost target under 20 USD a month at pilot scale (file storage, AI queries, alert email).
- Page load under 2 seconds for the portfolio view with 50 workspaces.

## Four Risks and Four Open Questions Need Owners

| # | Item | Plan |
|---|---|---|
| R1 | Lovable cannot poll Gmail. Support-email ingest needs an inbound email service | Use an inbound-parse webhook (for example Resend or Postmark) pointed at an edge function. Ship a "paste an email" form first |
| R2 | Customer data and security posture. AccuKnox is a security vendor and customers will judge the portal | Run a security review before inviting any customer. Use RLS tests, signed URLs, SSO. Keep real customer data out of the first build |
| R3 | Team keeps using Jira in parallel | Pilot with the 5 active POCs. Retire the CM board for pilot accounts after 30 days |
| R4 | A big build for a small team (Rahul's own note) | Hold the MVP to F1 to F9 above. Defer the rest |
| Q1 | SLA targets per severity: who signs them off? | Syed and Rahul to confirm |
| Q2 | Does the customer see roadmap ETAs by default? | Rahul to confirm |
| Q3 | Which Slack channels receive alerts? | Syed to name them |
| Q4 | Which CSAT definition do we keep (0 to 4 scale from the CFL minutes)? | Keep it for the MVP |

## A Four-Week Rollout Ends With a Jira Retirement Decision

1. Week 1: build the MVP in Lovable with fictional seed data. Demo to Syed.
2. Week 2: import the active POCs and 10 production accounts. Wire Slack and email alerts.
3. Week 3: security review. Invite two friendly customers.
4. Week 4: review metrics. Decide to retire the Jira CM board for pilot accounts.

## Sources Come From Email and Repo Files

- Email thread "POC / Customer portal", 22 Oct 2026 (Rahul, Atharva, Syed).
- CFL meeting minutes, 22 Oct 2026.
- POC guides in this repo: `references/technical-reference/playbooks-and-poc/` (CSPM prerequisites, on-prem container POC), `references/poc-decks/cwpp-poc-exec-summary/`, `references/onboarding/openshift-private-cloud/`.
