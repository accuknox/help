# Proposal: Rebuild the CWPP Report

**To:** Product, Engineering, PM (CWPP)
**From:** website@accuknox.com
**Subject:** Proposal: rebuild the CWPP report, attached draft + benchmark
**Attachments:** Cloud Workload Protection Management Report (CWPP).pdf

---

Hi team,

The CWPP report is the weakest of our customer-facing PDFs today. It is essentially a config wizard around regex cluster/namespace selection, with no widget-driven narrative like the ASPM, CSPM, AISPM, and Compliance reports already ship. Customers buying CWPP want the same kind of executive view they get for the other modules: workloads in scope, what KubeArmor caught, what it blocked, where the hardening gaps are, what to fix next.

I built a full draft of what that report should look like. PDF is attached. It is modeled on the visual system of the existing ASPM and CSPM reports (cover page, section pages with widget cards, captions, Private & Confidential footer). The data is sample data, but the widgets, structure, and section breakdown are the deliverable.

## Why this matters now

Three things forced the issue:

1. **Customer asks.** Multiple recent CWPP customers have asked why their report does not look like the CSPM or ASPM PDF they also receive. They are comparing reports across modules.
2. **Sales motion.** The CWPP report is a leave-behind during evals. The current PDF does not show what KubeArmor actually did, so it does not sell the inline-mitigation story.
3. **Competitor parity.** Wiz, Prisma Cloud Compute, Sysdig Secure, Aqua, and Lacework all ship runtime-protection PDFs that include MITRE coverage, runtime alert breakdowns, drift events, and hardening posture. We have the data. We are not surfacing it.

## What changes vs. the report today

| Today | Proposed |
|---|---|
| Regex config, then a generic PDF | 15-page PDF with cover, summary, 11 widget sections, and recommendations |
| No KubeArmor runtime data | Alerts by severity, audit vs block vs audit-then-block, trend, top namespaces, top workloads, top policies |
| No app behavior view | Process / file / network observability, top execs, top file paths, top egress/ingress workloads |
| No hardening posture | Coverage by category (FIM, SA token, certs, capabilities, /tmp noexec, etc.), policies by type, gap list, discovered-but-unapplied |
| No KSPM cross-section | Cluster findings, asset type, KIEM, Pod Security Admission, public exposure, risky clusters |
| No image / drift view | Image scan summary, top vulnerable images, top CVEs in images, fixes availability, image-vs-runtime drift events |
| No VM workload view | VM exposure risk, exploitable VMs, exploitable CVEs, over-privileged VMs, exploitable packages, VM scan summary, OWASP |
| No MITRE mapping | Tactic heatmap, top techniques observed, inline blocked vs audit-only by tactic |
| No compliance cross-walk | K8s CIS pass/fail donut, plus PCI, NIST 800-190, FedRAMP, HIPAA, MITRE coverage table |
| No tickets / SLA | Ticket status, by severity, SLA met / approaching / breached, open vs closed trend, MTTR |
| No recommendations | Six prioritized actions, each with module tag, body, and expected risk drop |

## Section list in the attached PDF

1. Cover + Report Summary
2. Workload Inventory & Coverage (KPIs, provider donut, cluster connection, agent coverage, onboarding trend)
3. Workload Inventory continued (OS distribution, EOL VMs, public exposure, asset category)
4. Runtime Threats & KubeArmor Alerts (KPI strip, alerts by severity, volume trend, enforcement breakdown)
5. Runtime Alerts Drill-Down (top namespaces, top workloads, top policies, block-based)
6. Application Behavior & Observability (process, file, network observability, top egress/ingress)
7. Workload Hardening & Policy Enforcement (coverage by category, policy types, gap list, discovered)
8. Cluster Security Posture / KSPM (findings by asset type, KIEM, PSA violations, risky clusters)
9. Compliance Posture (K8s CIS donut, multi-framework table)
10. Container Image & Registry Security (top vulnerable images, fixes, top CVEs, drift)
11. VM Workload Protection (exposure risk, exploitable VMs, top VMs, exploitable packages, scan summary, OWASP)
12. Vulnerability & CVE Management (CVE by SLA, top 5 CVEs, active vs resolved, MTTR)
13. MITRE ATT&CK Coverage (tactic heatmap, top techniques, inline-blocked vs audit-only)
14. Incident & Ticket Management (status, severity, SLA, open vs closed)
15. Recommendations & Action Items (6 numbered actions with expected risk drop)

## Competitor benchmark, briefly

- **Wiz** ships a workload risk PDF with attack-path context and runtime-sensor data. We match this with the runtime alerts, MITRE, and exposure sections.
- **Prisma Cloud Compute** (Twistlock heritage) reports per-host CWPP, image vulnerabilities, WAAS, CIS Docker/K8s, NIST 800-190. We cover all of these except WAAS (out of CWPP scope today).
- **Sysdig Secure** reports Falco alerts, drift events, MITRE heatmap, in-use vuln prioritization, container forensics. We match every section. Our advantage is inline LSM prevention (not just detection), which we call out explicitly in the Enforcement Mode breakdown.
- **Aqua** reports image assurance pass/fail, drift prevention, runtime events. Same coverage in our draft.
- **Lacework** sells behavioral baselining via Polygraph. Our App Behavior section is the equivalent and ties directly to discovered policy recommendations.

The one thing none of them surface is the audit → audit-then-block → block progression. That is unique to KubeArmor and we should make it a signature widget. It is on page 4 of the draft.

## What we already collect (no new data work)

All widgets in the draft map to data we already produce in the SaaS. I cross-checked against:
- The runtime security dashboard (alerts summary, policies generating alerts, top namespaces, top workloads, K8s egress/ingress)
- The KSPM dashboard (cluster findings, asset type, asset category, public exposure, CIS, continuous compliance, KIEM)
- The VM dashboard (exposure risk, exploitable VMs/CVEs, top VMs, OWASP, scan summary, MTTR, by cloud provider, fixes availability)
- App Behavior (process, file, network observability) in the CWPP product
- Hardening (FIM, SA token, certs, capabilities, etc.) — already a documented use-case set

Nothing in the draft requires new telemetry. It is reformatting and presenting what we already have.

## Asks

1. Sign-off on the structure (the 15-page outline above).
2. Eng owner for hooking the existing widget data into the new report template, replacing the regex-config-only flow.
3. Decision on default cadence (on-demand + monthly scheduled, same as the other reports).
4. One review pass on the visual system before we ship it to a pilot customer.

Open to feedback on any section. If we want to drop one or add one, easier to do it now than after engineering hookup.

Atharva
