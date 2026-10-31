# Lovable Prompt: AccuKnox POC and Customer Portal

Paste everything below the line into Lovable as the first message. Use fictional seed data only. Add real customers after the security review.

---

Build a web app called **AccuKnox Customer Hub**. It is an internal portal for a cloud security company's Solutions Engineering (SE) and customer success teams. It replaces Jira for tracking customer POCs and production onboarding. Staff manage one workspace per customer. Customer contacts get a limited view of their own workspace.

## Use React and Lovable Cloud With an Apple-Style Light Design

- React, TypeScript, Tailwind, shadcn/ui.
- Use Lovable Cloud (Supabase) for auth, Postgres, Row Level Security (RLS), private file storage and edge functions.
- Use the Lovable AI gateway for the "Ask AI" feature.
- Light mode. Apple-style design: white background, generous spacing, one blue accent (#2563EB), Inter font, thin borders, no gradients, no heavy shadows. Dead simple. Fewest clicks.
- Desktop first. Works on tablet.

## Staff Sign In With Google and Customers Use Magic Links

Two user types.

1. **Staff**: sign in with Google, restricted to the accuknox.com domain. Roles: `admin`, `se`, `csm`, `viewer`. Staff see all workspaces.
2. **Customer contact**: sign in by email magic link. Each contact belongs to one workspace. RLS must restrict them to that workspace and only to records where `customer_visible = true`. Internal notes and internal comments must never reach them.

Seed 5 staff, 2 customer contacts and the roles above.

## Sixteen Tables Hold Workspaces, Issues, Files and Alerts

Create these tables with sensible foreign keys, timestamps and RLS.

- `workspaces`: id, name, type (`poc` | `production`), segment, region, deployment_model (`saas` | `onprem`), products (text array), stage, csat (0 to 4), advocate_id, se_owner_id, start_date, target_close_date, decision (`won` | `lost` | `extended` | null), created_at.
- `contacts`: id, workspace_id, name, email, title, is_primary.
- `team_members`: id, name, email, role, manager_id, slack_handle.
- `poc_templates`: id, name, description. `poc_template_items`: id, template_id, position, title, default_owner_role, due_offset_days, is_prerequisite_to_send, customer_visible.
- `checklist_items`: id, workspace_id, title, owner_id, due_date, percent_complete (0 to 100), status (`not_started` | `in_progress` | `blocked` | `done`), customer_visible, is_prerequisite_to_send, prerequisite_sent_at, updated_at.
- `issues`: id, workspace_id, title, description, severity (`p1` | `p2` | `p3`), owner_id, status (`open` | `in_progress` | `waiting_on_customer` | `resolved`), percent_complete, next_update_due, first_response_due, source (`form` | `email` | `staff`), customer_visible, created_at, resolved_at.
- `roadmap_items`: id, workspace_id, title, eta, status, committed_to_customer, customer_visible.
- `comments`: id, parent_type, parent_id, author_id, body, is_internal, created_at.
- `files`: id, workspace_id, name, storage_path, file_type (`deck` | `report` | `guide` | `log` | `contract` | `other`), size_bytes, uploaded_by, customer_visible, created_at.
- `file_events`: id, file_id, user_id, action (`upload` | `download`), created_at.
- `activity_log`: id, workspace_id, actor_id, entity_type, entity_id, summary, created_at. Write a row on every status, owner, percent or file change.
- `sla_rules`: id, severity, first_response_hours, update_every_hours, escalate_after_hours.
- `alert_events`: id, issue_id or checklist_item_id, kind (`sla_breach` | `overdue` | `stale` | `escalated`), notified_user_id, channel, created_at, acknowledged_at.
- `email_drafts`: id, workspace_id, to_email, subject, body, status (`draft` | `sent`), created_by.
- `inbound_emails`: id, from_email, subject, body, matched_workspace_id (nullable), issue_id (nullable), received_at.

Seed `sla_rules`: P1 respond in 1 hour, update every 24 hours, escalate after 4 hours. P2 respond in 8 hours, update every 48 hours, escalate after 24 hours. P3 respond in 24 hours, update every 120 hours, escalate after 72 hours.

## Three Seeded POC Templates Create the Checklist

Each item has an owner role, a due offset in days from the POC start and a prerequisite flag.

**1. CSPM on AWS**
1. Kickoff call and success criteria agreed (day 0)
2. Send prerequisites: AWS account or OU scope, read-only IAM role, optional write role for auto-remediation (day 1, prerequisite)
3. Customer creates IAM role and shares role ARN (day 3)
4. Tag resources by team and type (day 4)
5. Connect Jira and Slack integrations (day 5, optional)
6. First automated scan complete (day 6)
7. Triage findings with customer (day 10)
8. Compliance framework report (CIS, NIST, SOC 2, HIPAA, as chosen) (day 12)
9. Executive summary readout (day 14)
10. Decision recorded (day 16)

**2. On-Prem Airgapped Container Security**
1. Kickoff and success criteria agreed (day 0)
2. Send prerequisites: one node with 16 vCPU, 32 GB RAM, 512 GB disk for the control plane, cluster access, image registry access (day 1, prerequisite)
3. Control plane installed (day 4)
4. Agents installed on target workloads (day 6)
5. Runtime use cases tested: file integrity, process and network enforcement (day 9)
6. Vulnerability scan of container images (day 10)
7. Scheduled reports configured (day 11)
8. Executive summary readout (day 14)
9. Decision recorded (day 16)

**3. Generic CNAPP POC**
1. Qualification and scope agreed (day 0)
2. Send prerequisites (day 1, prerequisite)
3. Onboarding session #1 (day 3)
4. Success criteria signed off by customer (day 3)
5. Mid-point review (day 8)
6. Findings triage session (day 10)
7. Executive summary readout (day 14)
8. Decision recorded (day 16)

When staff create a workspace of type `poc`, they pick a template. The app copies the items into `checklist_items` with real due dates.

## Six POC Stages Move From Qualified to Decision

`qualified` → `prerequisites_sent` → `onboarding` → `running` → `readout` → `decision`. Show the stage as a horizontal stepper at the top of each POC workspace. Staff can change it. Moving to `decision` requires choosing won, lost or extended.

## Staff and Customers See Different Screens

### Staff

1. **Portfolio** (home). A table of all workspaces: name, type, stage, CSAT badge (0 red "Renewal Risk", 1 grey "Not Started", 2 blue "In Progress", 3 amber "Done, open issues", 4 green "Happy"), SE owner, open issues, overdue items, next milestone date. Filters for type, stage, owner, CSAT. A "Needs attention" panel above the table lists overdue items, items with no update in 7 days, and SLA breaches. Each row links to the workspace.

2. **Workspace**. Header with name, type, stage stepper, CSAT, owners and a "Invite customer" button. Tabs:
   - **Overview**: summary cards (percent of checklist done, open issues, next milestone) and a timeline from `activity_log`.
   - **Checklist** (POC) or **Onboarding** (production): the items with owner, due date, percent slider, status, a customer-visible toggle. A "Send prerequisites" button emails the prerequisite items (opens a draft first).
   - **Issues**: table with severity, owner, percent, status, next update due, SLA countdown chip (green, amber under 25% time left, red when breached). New issue button.
   - **Roadmap**: items with ETA and a "Committed to customer" toggle.
   - **Files**: drag-and-drop upload to a private bucket, file-type tag, customer-visible toggle, a download history popover.
   - **Activity**: the full log.
   - **Ask AI**: described below.

3. **Item drawer**. Clicking any checklist item, issue or roadmap item opens a side drawer with fields, comments (with an "Internal only" checkbox) and an **Update customer** button. That button opens an email draft to the primary contact, prefilled with the item title, new status, percent and ETA. Staff edit it and click Send. Nothing sends without a click.

4. **Triage queue**. Lists `inbound_emails` with no matched workspace. Staff pick a workspace and click "Create issue".

5. **SLA and alerts**. Shows `sla_rules` (editable by admins), a list of `alert_events`, and a per-person "misses in the last 30 days" count. Anyone with 3 or more misses shows a red flag on the Portfolio.

6. **Templates**. Read-only list of POC templates in the MVP.

### Customer view

A clean, reduced page reached after magic-link sign-in:
- Workspace name and stage stepper.
- "Open actions" (customer-visible checklist items with owner, due date, percent).
- "Issues" (customer-visible) with status and next update date. A **Report an issue** button opens a form (title, description, severity suggestion).
- "Roadmap" (customer-visible items with ETA).
- "Files" (customer-visible, download only).
- A comment box on each item. A **Confirm done** button on actions assigned to the customer.

## Four Edge Functions Chase the Team and Ingest Email

1. **SLA checker**. Runs every 15 minutes with a scheduled function. For each open issue, if `first_response_due` or `next_update_due` has passed, create an `alert_events` row, send a Slack message to the owner and an email to the owner. If the issue stays unhandled past `escalate_after_hours`, notify the owner's manager and mark the alert `escalated`. Also alert for checklist items past due and items with no update in 7 days.
2. **Inbound email webhook**. An edge function at `/inbound-email` accepts a JSON POST (from, subject, body). Match the sender's domain to a contact's domain. If matched, create an issue with `source = email` and the owner set to the workspace's SE owner. If not matched, store it in the triage queue. Also build a "Paste an email" form in the Triage page that calls the same function, so the flow works before real email forwarding is wired up.
3. **Slack**. Read a `SLACK_WEBHOOK_URL` secret and post alerts. Ask me for the secret when needed. Do not hard-code it.
4. **Email**. Use Lovable's built-in email sending or a Resend key stored as a secret. Ask me when needed.

## Ask AI Answers Questions and Cites Its Records

On each workspace and on the Portfolio page, add an "Ask AI" box. Send the question and the relevant records (checklist items, issues, roadmap, last 20 activity rows, file names) to the Lovable AI gateway. The answer must cite which records it used, shown as small links. Example questions to show as chips:
- "What is blocking this customer?"
- "Which POCs have prerequisites unsent for more than 3 days?"
- "Summarize this week for the CFL sync."
- "Which accounts have overdue items and low CSAT?"

Never send file contents. Send only metadata and text fields.

## Eight Fictional Workspaces Fill the Demo

Create 8 workspaces with realistic status:
- 4 POCs: "Northwind Bank" (CSPM on AWS, stage `onboarding`), "Contoso Airlines" (On-Prem Container, stage `running`, one overdue item), "Fabrikam Health" (Generic CNAPP, stage `prerequisites_sent`, prerequisites unsent for 4 days), "Tailspin Retail" (CSPM on AWS, stage `readout`).
- 4 production customers: "Litware Insurance" (CSAT 3), "Adventure Works Telecom" (CSAT 2), "Wingtip Mobile" (CSAT 0, Renewal Risk), "Proseware Education" (CSAT 4).

Add 12 issues across them (mix of severities, 3 with breached SLAs), 15 roadmap items with ETAs, 20 files with fake names, and activity log history so the timelines look real.

## Six Behaviors Must Hold in Every Screen

- Every status, owner, percent or file change writes an `activity_log` row.
- Percent complete of 100 sets status to `done`. Status `done` sets percent to 100.
- A customer contact can never read a record with `customer_visible = false`. Write RLS policies and test them.
- Files use private storage with signed URLs that expire in 10 minutes. Log every download in `file_events`.
- Empty states are helpful: each one says what to do next in one sentence.
- Show loading skeletons. Show clear error toasts.

## Build in Seven Steps and Show Me After Two

1. Auth, roles, data model, RLS and seed data.
2. Portfolio and Workspace screens with the checklist and issues tabs.
3. Templates and "start a POC".
4. Files tab with private storage.
5. Customer view and invites.
6. SLA checker, Slack and email alerts, inbound email webhook and triage.
7. Ask AI.

Build steps 1 and 2 first and show me. Then continue in order.
