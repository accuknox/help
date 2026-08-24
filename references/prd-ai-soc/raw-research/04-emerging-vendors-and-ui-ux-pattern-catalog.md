# Raw Research — Emerging AI-SOC Vendors and Cross-Vendor UI/UX Pattern Catalog

Compiled June 2026 from homepage and product-page crawls. This is the design and capability reference for AccuKnox's own AI-SOC UI/UX journey. The pattern catalog at the end is the screen vocabulary the whole category has converged on. AccuKnox's UI must hit this vocabulary and then extend it with the one screen type nobody else has: live runtime enforcement.

---

## Part A — Emerging vendor scan (the field beyond Mate and Exaforce)

### Prophet Security
- Positioning: "A Smarter, Scalable SOC Powered by Agentic AI," a "force multiplier." $41M raised.
- Agents: Prophet AI SOC Analyst, AI Threat Hunter, Detection Advisor, Copilot, Guidance (ingests playbooks + analyst feedback).
- Reasoning agents "plan and execute investigations like a senior analyst," "dynamically build an investigation plan."
- Explainability: shows the investigation plan, the queries used, and all evidence gathered. Strong.
- Autonomy: hybrid. Autonomous remediation for high-confidence threats, human-in-the-loop for complex cases.
- Metrics: 10x SOC throughput, 75% faster triage, "100% alert coverage across all severities."

### Dropzone AI
- Positioning: investigate "every alert in under 10 minutes," augment analysts with "unlimited intelligence."
- Agent: fully autonomous AI SOC Analyst, "100% Software Execution," "No analysts on the keyboard behind the scenes," "No playbooks. No code."
- Features: autonomous investigation across 90+ tools, decision-ready conclusions + auto-containment, can "interview affected users," federated threat hunting (10 to 20 hours into ~1 hour), context memory.
- Explainability: "Glass Box, Not Black Box," full audit trail of every question, tool, and finding.
- Pricing: capacity-based, ~$36K/yr per AI analyst = ~4,000 investigations.
- Metrics: 85% reduction in manual investigation, 5x faster MTTR, ~30-min deploy.

### Radiant Security
- Positioning: "The quality of your best analyst, at the speed and scale of AI." Triages "100% of alert types."
- Agents: AI Research Agents + agentic triage that "dynamically builds and executes triage logic for every alert," no rule updates.
- Features: eliminate "up to 98% of false positives," 1-click and automated response, unlimited log management at a fraction of SIEM cost, broad coverage (email, endpoint, identity, network, cloud, insider, SIEM, WAF, DLP, OT/IoT, dark web, supply chain).
- UI: Cases dashboard, alert triage queue ("1 to 3 high-fidelity alerts per day"), investigation context view, response plans.
- Explainability: "Total transparency into AI reasoning, full context at every step."
- Pricing: flat, priced on use cases + end users, "100% predictable, no per-alert add-ons." ~$1,188/yr starting.
- Metrics: triage 45 to 10 min, 90%+ noise reduction within weeks, 10x MTTR, 60 to 85% logging cost reduction.

### Intezer (Forensic AI SOC)
- Positioning: "Every alert investigated. Detection coverage perfected." Differentiator is forensic depth.
- Agent: agentic reasoning fused with deterministic forensics (endpoint forensics, reverse engineering, sandboxing, static analysis).
- Features: sub-minute triage across 100% of alerts, endpoint/identity/phishing/SIEM triage, auto-response via API/webhook.
- UI: dashboard with investigation time / escalation rate / alerts by source, triage queue with verdicts + recommended actions, forensic-artifact displays.
- Explainability: transparent triage logic, review/override.
- Autonomy: human-in-the-loop.
- Metrics (strongest hard numbers): 98% verdict accuracy, fewer than 2% escalated, resolves over 98% of false positives in under a minute.
- Pricing: predictable, endpoint-based.

### Torq (HyperSOC / Socrates)
- Positioning: "More than an AI SOC Analyst. Investigate, orchestrate, and build." Fuses agentic AI with Hyperautomation. $1.2B valuation.
- Agent: Socrates the "agentic quarterback" orchestrating HyperAgents (Runbook, Investigation, Remediation, Case Management). Multi-agent.
- Features: Agentic Builder (NL into production-ready agents, tested on sample data), machine-speed investigation, autonomous response coordination, proactive hunting, Context Graph grounding.
- UI: case interface with inline NL collaboration, chat, "fully auditable record of the reasoning behind every agentic decision," timeline, sample-data agent testing.
- Metrics: HyperSOC-2o resolves "95% of Tier-1 alerts and many Tier-2 tasks without human involvement." Customer: "autonomously closes over 50% of Tier 1 and Tier 2 alerts."

### 7AI
- Positioning: "AI Agents That Actually Do The Work," "hours to minutes." $166M total, ex-Cybereason founders.
- Agent: swarm of "60+ purpose-built agents" across Endpoint (14), Identity (12), Cloud (8), Email (5), Network (6). "Dynamic Reasoning, bounded by design to eliminate hallucinations."
- Features: Cases (auto-populated summaries + cross-alert correlation), Investigations (autonomous enrichment + conclusions with full evidence), Detection (95 to 99% FP elimination), Response (conclusion-driven, HITL options, audit trail), Enterprise Insights (org context).
- UI: Kanban-style Cases dashboard, Alert Intelligence triage view, Workflow Builder (drag-and-drop, conditional branching, no code), threat-hunting interface.
- Metrics: 95 to 99% FP elimination, 80% reduction in tier-1 time, 5M+ alerts, 732,910+ analyst hours saved, $42.1M reclaimed.

### AiStrike
- Positioning: "The SOC Intelligence Fabric." AI-native, "preemptive."
- Agent: "Composite AI," four-cycle loop: Unify Signals, Investigate in Context, Respond with Confidence, Continuously Improve.
- Features: detection engineering with coverage-gap discovery, threat-intel correlation + exposure prioritization, AI alert correlation that reconstructs attacks, analyst-gated response, cloud investigation.
- Explainability: "explainable investigations and actions" not "generic text recommendations."
- Autonomy: human-in-the-loop, analyst-gated.
- Metrics: impact within days, "Cut Costs by 50%," 100+ integrations.

### Conifers AI (CognitiveSOC)
- Positioning: "SOC excellence at machine speed," "the first end-to-end agentic SOC."
- Agent: "One fabric. Five stages. Agents inside. Analysts on top." Five autonomous stages: Threat Intelligence, Threat Hunting, Detection Engineering, Investigation, Remediation. "Intel sharpens hunts. Hunts upgrade detections. Detections feed investigations." (Same closed-loop idea as Mate's CD/CR.)
- Explainability: governance-forward, "evidence to prove it," staged control transfer.
- Metrics: 2.5-min average investigation, >99% investigation accuracy, 3x faster, 87% reduction in investigation duration, 3x ROI.

### Simbian
- Positioning: "The First Self-Improving AI SOC Agent." "Reasoning, not rules." "No playbooks required." Distributed via Wipro and CrowdStrike Marketplace.
- Features: automated investigation, Verdict & Reasoning (TP/FP + severity + confidence), Response across 70+ tools, self-improvement via analyst feedback, MSSP multi-tenant.
- UI: investigation reports, verdict screens with "instant confidence rating," "Context Lake" visualization.
- Metrics: 92% automated resolution, 5x cost savings, deploy in days, ROI within one week.

---

## Part B — The cross-vendor UI/UX pattern catalog (the screen vocabulary)

Every vendor converges on roughly the same screens. This is the canonical list. AccuKnox's UI must cover all of these, then add the enforcement screens at the end that no competitor has.

1. **Alert triage queue / inbox.** Incoming alerts auto-classified, deduped, sorted. Most auto-closed, a thin slice escalated. The promise is always "your queue is now 1 to 3 items." (Radiant, Mate, everyone.)
2. **Cases / incident dashboard (often Kanban).** Correlated alerts consolidated into a case with an auto-populated summary. (7AI Kanban, Radiant Cases, Torq case interface.)
3. **Investigation timeline / attack reconstruction.** Chronological narrative stitching multi-source signals into one attack story. The screen that sells "the AI thinks like an analyst." (Dropzone multi-stage, AiStrike reconstruction, Exaforce Attack Chain.)
4. **Reasoning / show-your-work panel (the explainability screen).** The single most emphasized differentiator. Which sources queried, what questions asked, what evidence gathered, why the verdict. (Dropzone "Glass Box," Prophet "investigative plan + queries + evidence," Radiant "transparency at every step," Torq "auditable record.")
5. **Verdict / conclusion card.** Compact decision object: TP/FP, severity, confidence score, recommended actions. The atomic unit the analyst approves or overrides. (Simbian, Intezer, Exaforce detail card.)
6. **Chat copilot.** NL box for ad-hoc questions mid-investigation. (Prophet Copilot, Dropzone chatbot, Torq NL collaboration, Exaforce Search.)
7. **Coverage / performance dashboard.** Exec-facing trends: alerts investigated over time, MTTR reduction, escalation rate, FP elimination. (Mate homepage charts, Intezer, Conifers KPIs, Exaforce SOC Insights.)
8. **Response / remediation plan + one-click action.** Auto-generated remediation with manual / one-click / fully automated execution and auto-containment. (Radiant 1-click, Dropzone/7AI auto-containment, AiStrike analyst-gated, Exaforce workflow.)
9. **Detection-as-code / detection engineering editor.** The loop writes back into detections: tuning recommendations, coverage-gap discovery, auto-authoring (MITRE-aligned). (Prophet Detection Advisor, AiStrike + Conifers agentic detection engineering, Mate Sigma export.)
10. **Knowledge / context graph (the back end made visible).** The context store surfaced as concept or visualization. (Mate Security Context Graph, Torq Context Graph, Simbian Context Lake, Conifers fabric, Exaforce Entity/Knowledge Graph.)
11. **Workflow / agent builder.** Drag-and-drop or NL agent construction with pre-production testing. (7AI Workflow Builder, Torq Agentic Builder, Exaforce Visual Workflow Editor.)
12. **Analyst-in-their-own-tools surface.** Meeting analysts where they work rather than a new console. (Mate browser extension + standalone console, Dropzone/Radiant inside existing SIEM/case systems, Conifers inside existing incident management.)
13. **HITL approval prompt (out-of-band).** Slack/Teams/email card with action buttons, timeouts, auto-escalation, full context. (Exaforce Slack confirmations.)
14. **Entity / identity inventory and risk profile.** All human/machine/AI identities with threat scores, unused privileges, effective permissions. (Exaforce Identity Inventory + Permissions Matrix.)
15. **Behavioral heatmap / anomaly view.** Day-by-hour activity grid, color = anomaly severity. (Exaforce Activity Heatmap.)
16. **Evidence table.** Evidence by type with links back to source systems. (Exaforce Evidence Tab.)
17. **NL + dropdown query builder.** Dual-mode query construction, no SQL required. (Exaforce Query Builder.)

## Part C — Two strategic observations for AccuKnox

1. **Autonomy is the real positioning axis.** Vendors spread along a spectrum: fully autonomous (Dropzone "no analysts on the keyboard," Simbian 92%, Torq 95% Tier-1, 7AI), explicitly human-in-the-loop (Intezer, AiStrike), and a tunable "controllable autonomy" middle (Prophet, Radiant, Conifers, Mate). AccuKnox should sit in the controllable-autonomy middle for analysis and decisively at the autonomous end for one thing nobody else can do: kernel enforcement that blocks regardless of whether a human approved, because the policy was approved once, in advance, as code.
2. **The headline metric is always the same three numbers.** False-positive elimination (~90 to 99%), investigation/triage time (hours to minutes, sub-minute for Intezer), MTTR reduction (Mate 93%, Radiant 10x). Verdict accuracy (Intezer 98%, Conifers >99%) and autonomous-resolution rate (Simbian 92%, Torq 95%) are the secondary proof points. AccuKnox already has matching or better numbers it can cite (85% alert noise reduction, 89% fewer false positives, 91% faster remediation). The differentiator is not the numbers, which everyone has. It is that AccuKnox can add a fourth number nobody else can: threats blocked at the kernel before execution.

## Part D — The screen AccuKnox adds that no competitor has

Every catalog above ends at "response," meaning an orchestrated API action through an integration. AccuKnox adds three screen types beyond the category:

- **Enforcement policy view.** The eBPF/KubeArmor policy generated from an investigation, shown as versioned YAML, with the syscalls it blocks, the workloads it applies to, and a dry-run/enforce toggle.
- **Runtime block timeline.** A live feed of syscalls blocked at the kernel in real time, tied back to the investigation that authorized the policy. Proof that the SOC did not just recommend, it prevented.
- **Agent trust and sandbox monitor.** The KnoxClaw/ModelArmor view showing the AI-SOC's own agents running sandboxed, what each agent is allowed to touch (filesystem, network, process), and any policy violation by an agent. The "we secured the analysts that are software" screen.

These three are the visual proof of AccuKnox's category claim. Design them as the climax of the journey, not a footnote.
