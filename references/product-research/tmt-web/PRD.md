# PRD, AccuKnox Threat Modeler (tmt.accuknox.com) v1

Owner: Atharva Shah. Stakeholder: Rahul. API guidance: Ayush. Target: demo build for Tuesday 29 September 2026, fallback the week after.

The v1 build is a browser-only copy of the Microsoft Threat Modeling Tool (MSTMT) core loop. The user draws a data flow diagram, clicks Analyze, triages STRIDE threats, and exports CSV or SARIF. AccuKnox push and sync sit behind a mock client until the API details arrive, so the demo works without them.

The build prompt lives in [lovable-prompt.md](lovable-prompt.md). This file holds the scope, the decisions behind the prompt, the questions for Ayush, and the acceptance tests.

## Sources Behind the Rule Engine

- Microsoft Learn, [Threat Modeling Tool feature overview](https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-feature-overview). Design view, Analysis view, stencils, element properties, messages, notes, read indicator, interaction focus.
- Microsoft Learn, [Getting started](https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-getting-started). The four threat states: Not Started, Needs Investigation, Not Applicable, Mitigated.
- Microsoft Learn, [Threat Modeling Tool threats](https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-threats). STRIDE category definitions.
- GitHub, [microsoft/threat-modeling-templates `default.tb7`](https://github.com/microsoft/threat-modeling-templates/blob/master/default.tb7). The SDL template holds 47 threat types with Include and Exclude expressions. Six of them are empty "(v3)" migration placeholders. The prompt carries the other 41 as 40 rules, because the two SQL injection rules merge into one.
- OASIS, [SARIF 2.1.0](https://docs.oasis-open.org/sarif/sarif/v2.1.0/errata01/os/sarif-v2.1.0-errata01-os-complete.html). The export format.

## What MSTMT Does and What v1 Copies

| MSTMT feature | v1 | Note |
|---|---|---|
| Stencil palette, drag to canvas, DFD shapes | Yes | Four kinds plus subtypes. Cloud-native subtypes added: Container Workload, Kubernetes Namespace, Cloud VPC. |
| Trust border boundary (box) | Yes | Crossing uses geometry: the center point of each element inside the box. |
| Trust line boundary (a drawn line) | No | Box boundaries cover the same cases with simpler math. |
| Element properties that drive threats | Yes | Only the properties that a rule reads. |
| Out of scope plus reason | Yes | Out-of-scope elements and flows generate no threats. |
| Messages and Notes panels | Yes | Six validation checks. |
| Analyze, threat list, threat properties | Yes | Read indicator, interaction focus, priority, status, justification. |
| Multiple diagrams per model (tabs) | No | Phase 1.1. One diagram per model keeps the store simple. |
| Custom template editor | No | Rules live in code. Phase 2 adds MAESTRO as a second rule file. |
| HTML full report | No | CSV and SARIF replace it for v1. |
| OneDrive save and share | No | Local `.tm.json` file plus localStorage. |
| CSV and SARIF export | Added | MSTMT has neither. |
| Push to AccuKnox and manual Sync | Added | Mock client now, live client once Ayush confirms the API. |

## Decisions Written Into the Prompt

- **D1, no backend.** Lovable adds Supabase when a prompt is vague, so the prompt forbids it by name. Everything persists in localStorage and in the downloadable `.tm.json` file.
- **D2, stable threat IDs.** A threat ID is `ruleId:flowId`. The same ID drives the re-analysis merge, the CSV, the SARIF `partialFingerprints`, and the AccuKnox mapping. Sync breaks without a stable ID, so this decision matters most.
- **D3, the re-analysis merge.** Re-analysis keeps a user's priority, status, and justification. A threat that no longer fires is dropped, unless the user edited it, in which case it stays with a Stale badge.
- **D4, AccuKnox wins on sync.** This follows the tentative direction from the meeting. The sync dialog shows each change before it applies, so a local edit never disappears without the user seeing it.
- **D5, the protocol sets the defaults.** HTTPS and IPsec switch on confidentiality and integrity. That matches the MSTMT behavior where an HTTPS flow removes the sniffing threat.
- **D6, rule priorities are ours.** MSTMT gives every threat the same starting priority. The prompt assigns High, Medium, or Low per rule so the demo list sorts usefully. Rahul can change any value in `rules.ts`.

## Questions for Ayush

The help docs already show the upload call that CI integrations use, in `docs/use-cases/mfa-dast.md:93` and `docs/integrations/harness-container-scan.md:70`. The call is `POST /api/v1/artifact/?tenant_id=&data_type=&label_id=&save_to_s3=` with a `Tenant-Id` header, a Bearer token, and the report as a multipart `file` field. `docs/use-cases/access-keys.md:244` shows `GET /api/v1/findings?data_type=` for reading findings. The prompt builds the live client on these two calls, so the questions only cover the gaps.

Ask Q1 to Q4 first, because the live client cannot ship without them.

- **Q1, the data type.** The docs show `data_type` values `ZAP`, `TR`, `SQ`, and `cloudsploit`, and none for SARIF. Which `data_type` value makes the parser read a generic SARIF file? The prompt uses the placeholder `SARIF`.
- **Q2, the label.** Is `label_id` required? Should the tool create one label per threat model, or use one fixed label such as `threat-model`?
- **Q3, the access key.** Is the Bearer token the same "access key" from the tenant settings page? Does the upload still need the `tenant_id` param and the `Tenant-Id` header when the key already carries the tenant?
- **Q4, CORS.** Will `/api/v1/artifact/` and `/api/v1/findings` accept a browser request from `https://tmt.accuknox.com`? If not, the push needs a small proxy, and that decision changes D1.
- **Q5, the SARIF parser.** Which SARIF fields does the AccuKnox parser read? Is `physicalLocation` required? Does it read `security-severity`, `partialFingerprints`, `suppressions`, and `properties`? A sample SARIF file that parses cleanly today would answer all of this.
- **Q6, the finding identity.** Which field does AccuKnox use to decide that two uploads hold the same finding? If it is not `partialFingerprints`, which field is it? The answer decides whether a second push updates findings or duplicates them.
- **Q7, reading state back.** Does `GET /api/v1/findings` return status, exceptions, and notes for SARIF findings? Which query param filters the list to one threat model, by label, by upload, or by fingerprint?
- **Q8, the status values.** What status and exception values can a finding hold on the platform? The prompt maps Open, In Progress, Risk Accepted, and Resolved to the four MSTMT states. The real values replace that table.
- **Q9, the asset.** Which asset or label should the findings attach to, and does the tool need to create the asset first?
- **Q10, a test tenant.** Can Atharva get a sandbox tenant and a test access key for the build?

## Acceptance Tests

The engine fixtures F1 to F8 sit in section 12 of the prompt, and Lovable writes them as vitest tests. Run `npm test` in the exported repo to check them. The tests below cover the UI, and each one takes under two minutes.

| ID | Steps | Expected result |
|---|---|---|
| A1 | Open Home, click "Open sample model". | The canvas shows 2 dashed red boundaries, 6 elements, and 6 labeled flows. The Messages tab shows no errors. |
| A2 | Drag a "Web Application" stencil onto the canvas. | A circle named "Web Application 1" appears, and the Properties panel shows the sanitizer switches. |
| A3 | Drag a flow from "Customer" to itself, then to a boundary. | The canvas rejects both connections. |
| A4 | Add a Data Store and leave it unconnected. | Messages shows the warning that the store is not connected to any data flow. Clicking the message selects the store. |
| A5 | Click Analyze on the sample model. | A toast reports the threat count. Every row has an ID in the form `TMT-xxx:<flowId>`. |
| A6 | Select any threat. | The row stops being bold, and the canvas highlights the flow and both nodes. |
| A7 | Set one threat to Mitigated with a justification. Move "Customer" inside "Corporate Network". | The yellow "diagram changed" banner appears. |
| A8 | Click Re-analyze after A7. | The Mitigated threat keeps its status and justification if its rule still fires, or it shows a Stale badge. Boundary threats on the "Browse and checkout" flow disappear. |
| A9 | Change a flow from HTTP to HTTPS. | Both the confidentiality and integrity switches turn on. |
| A10 | Mark "Orders DB" out of scope with an empty reason, then Analyze. | Messages warns about the empty reason. No threat names "Orders DB". |
| A11 | Export CSV and open it in a spreadsheet. | There is one row per threat, and the 13 columns follow the order in the prompt. A justification with a comma stays in one cell. |
| A12 | Export SARIF and validate it at [sarifweb.azurewebsites.net/Validation](https://sarifweb.azurewebsites.net/Validation). | The file passes schema validation. The result count equals the threat count, and every Not Applicable threat carries a suppression. |
| A13 | Save the `.tm.json` file, delete the model, and import the file. | The model returns with the same diagram, threats, and statuses under a new ID. |
| A14 | Import a JSON file with `"schemaVersion": 2`. | The import stops with a clear error, and no model is created. |
| A15 | Open AccuKnox Settings in mock mode, save, then click Push findings. | A toast reports the count pushed, and each threat shows an `AK-` finding ID. |
| A16 | Click Sync twice. | Each click opens a dialog with 2 changes. After Apply, the local status matches the mapped AccuKnox status. |
| A17 | Reload the browser tab. | The model, the threats, the triage state, and the AccuKnox settings all come back. |
| A18 | Press Ctrl+Z after deleting a node. | The node and its flows come back. |

## Out of Scope for v1

MAESTRO and other frameworks, login and SSO, multiple diagrams per model, a template editor, an HTML report, real-time collaboration, webhooks and polling, and embedding in the CNAPP console.
