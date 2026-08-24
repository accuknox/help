# AccuKnox Cloud Security Demo Summary

**Presenter:** Brian Lang
**Duration:** ~17 minutes
**Tenant shown:** SERAN

## Demo Structure

The demo covers four areas: generic findings (dashboard + tabular), compliance, AI security, and runtime protection.

## 1. Dashboards & Findings (0:00 - 6:13)

The platform opens on a configurable dashboard showing 8 accounts, 3 clusters, 2 registries, and 11 repos. Key points:

- **Multi-tenant architecture** with full RBAC across tenants. Users pick which tenant to view.
- **Configurable widgets** pulled from different data areas. An AI widget builder can generate custom widgets on demand.
- **Cloud connectors** for AWS, Google, Azure, Nutanix, and other hypervisors/asset management platforms.
- **Date range filtering** demonstrated at 2-day, 12-hour, and 90-day views. Filters can scope to specific applications (e.g., "AI app only").
- **Dashboard drill-down**: clicking a metric (e.g., 1,600 failing checks) navigates directly into the findings screen with that filter applied.

The **Findings screen** shows all detected vulnerabilities, misconfigurations, and triggered events. Findings can be grouped by name, expanded for detail (e.g., ACM certificates without tags), and acted on:

- Add notes, create tickets (bidirectional with ServiceNow)
- **Ask AI co-pilot** for remediation steps specific to the selected assets, not generic advice. It generates scripts referencing the actual certificate ARNs.
- Search for new vulnerabilities across all assets
- **Saved filter sets** for recurring views (e.g., "last 12 hours, exploit available only")
- **Rules engine** for custom rules. Example: flag any asset type missing AccuKnox runtime protection.

## 2. Compliance (6:13 - 8:44)

About 50 compliance frameworks are available, including AWS CIS Benchmark, HIPAA, PCI, SOC 2, and FedRAMP. Each shows last scan time and pass rate.

Drilling into HIPAA shows section-level checks (e.g., access controls requiring CloudTrail bucket delete policy). Clicking a failure navigates to the filtered finding with full detail and ticket creation. New frameworks can be added on request since the platform already monitors the underlying controls.

**Integrations:** Single-directional (push or pull) and bidirectional (e.g., ServiceNow ticket sync where status updates flow both ways).

## 3. AI Security (8:44 - 13:00)

The AI/ML Security section shows a per-application view with tabs for Overview, Models, Datasets, Computes, Pipelines, and Risks.

- **Pipeline topology** visualizes user region, model, and infrastructure (e.g., Bedrock).
- **Automated red teaming** tests models for: code generation, hallucination, prompt injection, and negative sentiment. The demo app failed in all four areas.

**Prompt Firewall** (stateful, considers ongoing conversation context):

- Policies apply to prompts, responses, or both
- **Banned topics**: block specific subjects (e.g., malware) from being asked
- **Code-Response policy**: strip code from model responses when the app shouldn't generate code
- **Sensitive information filtering**: block PII/secrets in both directions
- **Token limiting**: prevent token exhaustion attacks via API
- **Language restriction**: one customer limits input to Portuguese to constrain the attack surface
- Mix of **deterministic** (regex, code detection) and **probabilistic** (AI-evaluated toxicity with adjustable thresholds) checks
- **Gibberish detection**: catches encoded bypass attempts like Morse code

Scope can be global (all apps) or local (specific applications).

## 4. Runtime Protection (13:00 - 17:00)

Demonstrated by showing how Claude on an EC2 instance bypasses its own guardrails. The model refuses to print credentials when asked directly, but complies when asked to print "a file starting with the letter C" in the .aws directory.

AccuKnox's fix: activate a **runtime protection policy** that blocks any process from accessing `~/.aws/`. This is OS-level enforcement, not prompt-level. The AI's attempt to read the file gets blocked, and it returns an error instead of secrets.

**Zero trust policy discovery**: AccuKnox inspects containers, source code, and running processes to determine what access each workload actually needs, then generates a zero trust policy. It flags when container changes require policy updates.

**Application behavior monitoring** (File Observability, Process Observability, Network Observability, API Observability) shows every file access, process execution, and network call. The blocked `.aws` access appears here with a "Block" action. All observed behaviors can feed into policy creation.

## Key Differentiators Highlighted

- Stateful prompt firewall (not single-prompt evaluation)
- Runtime protection as a backstop for guardrails that can be bypassed
- Automated red teaming with asset-specific AI remediation
- Zero trust policy discovery from workload behavior
- Bidirectional integrations (ServiceNow, ticketing)
- Multi-tenant RBAC with configurable dashboards

## Screenshot Index

| # | File | What it shows |
|---|------|--------------|
| 01 | main-dashboard-overview.png | Main dashboard with accounts, clusters, registries, checks passed/failed |
| 02 | multi-tenant-selection.png | Tenant dropdown showing available dashboards (dast, DAST, default, KSPM, etc.) |
| 03 | widget-builder-ai-widget.png | Widget selection panel with AI widget builder option |
| 04 | cloud-connector-selection.png | Cloud provider and hypervisor connector options |
| 05 | dashboard-nis-framework-2day-view.png | Dashboard filtered to 2-day view with NIS framework compliance |
| 06 | dashboard-ai-app-12hr-filter.png | Dashboard filtered to AI app, last 12 hours |
| 07 | compliance-frameworks-90day-view.png | 90-day compliance overview across multiple frameworks |
| 08 | findings-screen-grouped-by-name.png | Findings list grouped by finding name, cloud findings |
| 09 | finding-detail-acm-certificates.png | Expanded finding detail for ACM certificates without tags |
| 10 | ask-ai-copilot-remediation.png | AI co-pilot generating asset-specific remediation steps |
| 11 | saved-filter-sets.png | Filter configuration with exploit availability, risk factors |
| 12 | rules-engine-custom-rules.png | Custom rules engine for creating security rules |
| 13 | compliance-frameworks-list.png | Full list of compliance frameworks (CIS, HIPAA, PCI, SOC2, FedRAMP) |
| 14 | hipaa-compliance-detail-view.png | HIPAA framework drill-down with section-level pass/fail |
| 15 | ai-application-models-view.png | AI application overview showing model details |
| 16 | ai-pipeline-topology.png | AI pipeline topology diagram (user, region, model, Bedrock) |
| 17 | ai-red-teaming-risks.png | Automated red teaming results showing risks across categories |
| 18 | prompt-firewall-policy-config.png | Prompt firewall policy configuration (prompt vs response side) |
| 19 | response-code-block-policy.png | Code-Response policy creation with global/local scope |
| 20 | runtime-protection-policy-activation.png | Runtime protection policies list with KubeArmor policy YAML |
| 21 | zero-trust-policy-discovery.png | Zero trust policy discovery from container/workload analysis |
| 22 | application-behavior-monitoring.png | App behavior: file observability showing blocked .aws access |
