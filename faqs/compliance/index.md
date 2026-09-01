---
title: Compliance & GRC FAQs
description: Frequently asked questions about AccuKnox Governance, Risk, and Compliance — framework coverage, continuous compliance, audit readiness, policy-as-code, baselining, remediation, and multi-cloud GRC.
hide:
  - toc
---

# Compliance & GRC

## Core Compliance Platform

??? "**1. What is AccuKnox GRC and what does it cover?**"
    AccuKnox GRC is a continuous governance, risk, and compliance platform built natively into the AccuKnox Zero Trust CNAPP. It automates policy enforcement, compliance monitoring, audit evidence generation, and risk remediation across cloud, Kubernetes, VM, container, and AI workloads.

    Core capabilities include:
    + **Automated Risk Assessments**: Continuously evaluate cloud, Kubernetes, and application environments against your risk posture and alert on anomalies.
    + **Policy-as-Code**: Define security and compliance rules using YAML or JSON and apply them consistently across all infrastructure.
    + **Compliance Benchmarking**: Map your current state to 33+ compliance frameworks with automated, audit-ready reports.
    + **Posture Dashboards**: Track violations, risk severity, compliance trends, and remediation progress in one unified view.
    + **Runtime Enforcement**: Block non-compliant behaviors at the kernel level using eBPF/LSM — not just detect and report them.
    + **Auto-Remediation**: Detect drift in cloud configurations and trigger automated remediation or GitOps workflows before violations escalate.

    **References:**
    - [Compliance Use Case](https://help.accuknox.com/use-cases/compliance/)

??? "**2. Which compliance frameworks does AccuKnox support?**"
    AccuKnox pre-configures 33+ compliance frameworks with automatic control mapping. A single enforcement action simultaneously satisfies overlapping mandates, eliminating redundant policy work across regulatory bodies.

    Frameworks covered include:
    + **Cloud Security**: CIS AWS Benchmarks (v1.4, v1.5, v4.0), CIS Azure, CIS GCP, AWS Foundational Security Best Practices
    + **Industry Standards**: HIPAA, PCI DSS (all 12 requirements and 78 sub-requirements), GDPR, SOC 2, ISO 27001 (2013 and 2022)
    + **Government and Defense**: NIST SP 800-53, NIST CSF, STIG, FedRAMP, CMMC 2.0, DoD
    + **AI and Emerging**: OWASP LLM Top 10, NIST AI RMF, MITRE ATLAS, ISO 42001
    + **Regional Frameworks**: MAS TRM (Singapore), DPDP (India), BAIT and VAIT (Germany), FISC (Japan), ISMS-P (Korea), SEBI CSCRF (India), CCPA (California), COPPA
    + **Operational**: MITRE ATT&CK, CIS Kubernetes Benchmarks, NERC CIP, CMMC

    **References:**
    - [Compliance Support Matrix](https://help.accuknox.com/support-matrix/compliance-matrix/)


??? "**3. How does AccuKnox deliver continuous compliance versus point-in-time audits?**"
    Traditional compliance tools generate a quarterly snapshot that goes stale within days of any deployment change. AccuKnox replaces this with always-on compliance assurance:
    + As soon as a cloud account is onboarded and scanned, the compliance dashboard populates with posture scores across all applicable frameworks.
    + Every new resource deployment is immediately evaluated against all configured compliance programs.
    + Configuration drift is detected in real time and triggers alerts or automated remediation before violations accumulate.
    + Timestamped, immutable audit evidence is generated continuously — not assembled manually before an audit.
    + Exportable reports (PDF, CSV, JSON) show continuous compliance posture, not just the state at the time of report generation.
    AccuKnox reduced audit preparation from 60 hours to under 5 hours per quarter for a financial services client managing 200+ cloud accounts.


??? "**4. How does the AccuKnox compliance dashboard work?**"
    The AccuKnox compliance dashboard gives security and GRC teams a unified, real-time view of their posture across all configured frameworks:
    + After onboarding a cloud account and completing the initial scan, navigate to the Compliance section in the nav bar to see all applicable compliance programs.
    + Each compliance program is broken down into sub-controls, with percentage compliance calculated as: passed checks divided by total checks (passed + failed + warning + not available).
    + Clicking any compliance program or sub-control navigates directly to the list of associated misconfigurations.
    + Findings can be filtered by cloud account, region, severity, check type, and many other dimensions on the detailed view tab.
    + A dedicated compliance report gives a scored breakdown of how you perform against each framework's requirements and rules with full coverage detail.

    - [AccuKnox GRC Platform](https://accuknox.com/platform/compliance)

??? "**5. What types of compliance reports does AccuKnox generate?**"
    AccuKnox generates several report types to support audit and governance workflows:
    + **Compliance Report**: Detailed scoring of your posture against a specific framework's requirements and rules, with sub-control-level breakdown and remediation guidance.
    + **Cloud Asset Summary**: High-level compliance posture overview per framework across all onboarded cloud accounts — useful for board-level and executive reporting.
    + **Posture Trend Report**: Tracks compliance score changes over time to demonstrate continuous improvement or flag regression.
    + **Findings Export**: Export all violations, misconfigurations, and control failures in PDF, CSV, or JSON format for auditor submission or internal ticketing.
    + **GRC Evidence Package**: Timestamped, immutable control evaluation records suitable for regulatory submissions, 3PAO audits, and supervisory reviews.
    Reports reflect only the services and frameworks enabled for the tenant, keeping output clean and relevant.


??? "**6. What is compliance baselining in AccuKnox and how does it work?**"
    Compliance baselining in AccuKnox establishes a verified security baseline for your workloads and cloud configurations, then continuously validates that the environment stays aligned to it:
    + **Advanced Baselining**: AccuKnox aligns with existing cloud postures to establish a consistent, documented security baseline for each environment.
    + **Auto-Generated Policies**: The platform auto-generates security policies from observed workload behavior, creating application-specific baselines without manual policy authoring.
    + **Drift Detection**: Any deviation from the established baseline — a new misconfiguration, a policy change, or an unauthorized resource — triggers an alert or automated remediation action.
    + **GitHub Repository Scans**: Baseline validation extends into code repositories, scanning IaC templates and source code for compliance gaps before deployment.
    + **Framework-Aligned Baselines**: Baselines are mapped directly to compliance controls, so every drift event is immediately associated with the regulatory impact it carries.

    **References:**
    - [Compliance Baseline Data](https://help.accuknox.com/resources/compliance-baseline-data/)
    - [Compliance Use Case](https://help.accuknox.com/use-cases/compliance/)
    - [Robust Compliance in Cloud-Native App Security](https://accuknox.com/blog/continuous-compliance)


??? "**7. How does AccuKnox handle overlapping compliance frameworks to avoid duplicate work?**"
    AccuKnox maps shared technical controls across multiple frameworks, enabling single-control, multi-framework validation:
    + A single security control evaluation simultaneously satisfies overlapping requirements across NIST, CIS, PCI DSS, and HIPAA where controls share technical criteria.
    + A control failure is surfaced once with full regulatory context — it does not appear as separate fragmented findings across each framework independently.
    + This eliminates redundant remediation workflows and reduces audit preparation overhead significantly.
    + Custom compliance mappings can be built for organization-specific requirements or niche industry regulations not covered by built-in frameworks.
    + For financial services, AccuKnox maps shared controls across PCI DSS, SOX IT general controls, and SOC 2 Trust Services Criteria within a single assessment cycle.

    **References:**
    - [Compliance Support Matrix](https://help.accuknox.com/support-matrix/compliance-matrix/)
    - [Compliance Baseline Data](https://help.accuknox.com/resources/compliance-baseline-data/)

??? "**8. How does AccuKnox enforce compliance at runtime — not just report on it?**"
    AccuKnox goes beyond detection by enforcing compliance controls at the kernel level using eBPF/LSM via KubeArmor:
    + When a process attempts non-compliant behavior — unauthorized network egress, privilege escalation, or file tampering — AccuKnox blocks it in real time rather than logging it for later review.
    + This means compliance posture is maintained proactively, not reactively reconstructed after an incident.
    + Runtime enforcement is governed by the same policy-as-code rules that generate compliance reports, so there is no gap between what is measured and what is enforced.
    + Automated remediation workflows handle drift correction for cloud misconfigurations, triggering GitOps PRs, auto-patches, or manual escalation depending on severity.
    + Enforcement mode is configurable per workload — observe, audit, or enforce — allowing teams to roll out controls without disrupting production.

??? "**9. How does policy-as-code work in AccuKnox GRC?**"
    AccuKnox allows security and compliance rules to be defined as code and applied consistently across all infrastructure:
    + Policies are written in YAML or JSON and version-controlled alongside application code — giving compliance teams full GitOps integration.
    + Pre-defined rule sets are available for CIS, HIPAA, PCI DSS, MITRE, NIST, and STIG out of the box, requiring zero custom authoring to get started.
    + Custom rules can be authored for organization-specific requirements, niche industry regulations, or internal governance standards not covered by built-in frameworks.
    + Policies are applied consistently across public cloud, private cloud, Kubernetes, VMs, and AI workloads from a single control plane.
    + Policy changes are tracked with version history and audit trails, providing evidence that controls were updated, reviewed, and approved through a governed process.

    **References:**
    - [Compliance Use Case](https://help.accuknox.com/use-cases/compliance/)
    - [Compliance Baseline Data](https://help.accuknox.com/resources/compliance-baseline-data/)
    - [Robust Compliance in Cloud-Native App Security](https://accuknox.com/blog/continuous-compliance)

??? "**10. How does AccuKnox support regulatory audits and supervisory reviews?**"
    AccuKnox maintains continuous, time-indexed audit evidence that supports any regulatory inquiry without requiring manual evidence collection:
    + Control evaluations are timestamped and immutable — auditors can reconstruct the compliance posture at any point in time, not just the current state.
    + Configuration change histories and remediation records are captured automatically for every finding.
    + Exportable audit packages (PDF, CSV, JSON) deliver the exact evidence format required for PCI DSS QSAs, SOC 2 audits, HIPAA reviews, and supervisory examinations.
    + AccuKnox reduced audit preparation from 60 hours to under 5 hours per quarter for regulated enterprises — a measurable outcome, not a claim.
    + The Federal Government achieved DoD compliance with 20% lower security costs using AccuKnox's continuous compliance model versus legacy quarterly audit approaches.

    **References:**
    - [Compliance Use Case](https://help.accuknox.com/use-cases/compliance/)
    - [Compliance Support Matrix](https://help.accuknox.com/support-matrix/compliance-matrix/)
    - [Top CNAPP Solutions for Compliance and Audit](https://accuknox.com/blog/cnapp-solutions-compliance-audit-support)
    - [GRC for Financial Services](https://accuknox.com/platform/compliance/finance)


??? "**11. How does AccuKnox manage compliance across multi-cloud environments?**"
    AccuKnox provides unified compliance posture management across AWS, Azure, and GCP from a single control plane:
    + Agentless onboarding connects cloud accounts via IAM role, service principal, or service account without installing software on cloud infrastructure.
    + Once connected, AccuKnox continuously scans all cloud resources against applicable compliance frameworks, surfacing misconfigurations and control failures in a unified dashboard.
    + Cross-cloud findings are normalized into a single compliance view, eliminating the need to correlate findings from separate cloud-native security tools.
    + Compliance posture is consistent across cloud providers — the same control evaluated on AWS is evaluated identically on Azure and GCP, giving a true multi-cloud compliance picture.
    + Data residency compliance is supported — CDR policies can alert and remediate if data assets are created outside approved geographic regions.

    **References:**
    - [Compliance Use Case](https://help.accuknox.com/use-cases/compliance/)


??? "**12. How does AccuKnox support compliance for financial services?**"
    AccuKnox provides purpose-built compliance support for financial institutions:
    + **PCI DSS**: Continuous scanning against all 12 requirements and 78 sub-requirements across payment card data environments.
    + **SOC 2**: Trust Services Criteria validation with automated control testing for security, availability, confidentiality, and processing integrity.
    + **SOX IT General Controls**: Monitoring with change management tracking and documentation.
    + **MAS TRM** (Singapore): Pre-configured controls for Monetary Authority of Singapore Technology Risk Management guidelines.
    + **BAIT/VAIT** (Germany): IT risk management and operational resilience frameworks for German financial institutions and insurance companies.
    + **ISMS-P** (Korea): Financial information security and risk management compliance.
    + Overlapping financial frameworks share control mappings — a single assessment satisfies PCI DSS, SOC 2, and SOX requirements simultaneously, avoiding redundant audit work.

    **References:**
    - [GRC for Financial Services](https://accuknox.com/platform/compliance/finance)
    - [Compliance Support Matrix](https://help.accuknox.com/support-matrix/compliance-matrix/)
    - [Compliance Baseline Data](https://help.accuknox.com/resources/compliance-baseline-data/)


??? "**13. How does AccuKnox support HIPAA compliance for healthcare organizations?**"
    AccuKnox provides automated HIPAA compliance coverage for healthcare cloud and AI workloads:
    + Pre-configured HIPAA controls map to cloud infrastructure checks across AWS, Azure, and GCP covering administrative, physical, and technical safeguards.
    + PII/PHI scanning at the dataset level detects regulated health data in AI training pipelines, storage buckets, and inference outputs.
    + Prompt firewall enforcement blocks PII/PHI from being transmitted to or received from LLMs in real time.
    + DeepOrigin achieved 85% reduction in PII leaks and enhanced HIPAA compliance using AccuKnox AI Security.
    + Continuous audit evidence satisfies HIPAA audit requirements without requiring manual quarterly evidence collection.

    **References:**
    - [Compliance Use Case](https://help.accuknox.com/use-cases/compliance/)
    - [Compliance Support Matrix](https://help.accuknox.com/support-matrix/compliance-matrix/)
    - [AccuKnox GRC Platform](https://accuknox.com/platform/compliance)


??? "**14. How does AccuKnox support government and defense compliance — STIG, FedRAMP, CMMC?**"
    AccuKnox delivers purpose-built compliance support for government and defense environments:
    + **STIG**: Security Technical Implementation Guide checks for VMs, containers, and Kubernetes clusters — assessing OS hardening, application configuration, and runtime behavior.
    + **FedRAMP**: Continuous compliance monitoring for federal cloud deployments with automated control evidence generation.
    + **CMMC 2.0**: Cybersecurity Maturity Model Certification controls mapped to cloud and Kubernetes workloads for defense contractor supply chain security.
    + **DoD**: AccuKnox helped the Federal Government achieve DoD compliance with 20% lower security costs compared to legacy approaches.
    + Air-gapped deployment support ensures classified and government-restricted environments can achieve full compliance without external connectivity.

    **References:**
    - [Compliance Support Matrix](https://help.accuknox.com/support-matrix/compliance-matrix/)
    - [Compliance Baseline Data](https://help.accuknox.com/resources/compliance-baseline-data/)
    - [Top CNAPP Solutions for Compliance and Audit](https://accuknox.com/blog/cnapp-solutions-compliance-audit-support)


??? "**15. How does AccuKnox handle compliance violations and remediation?**"
    AccuKnox provides a multi-mode remediation approach covering automated, guided, and manual resolution paths:
    + **Auto-Remediation**: For cloud misconfigurations, AccuKnox can automatically trigger corrective actions — closing public S3 bucket access, reverting IAM policy changes, or restoring compliant configurations.
    + **GitOps PR Generation**: For IaC-managed environments, AccuKnox opens a pull request with the specific code change needed to resolve the violation, routing it through the existing developer review process.
    + **Guided Remediation**: Each finding includes actionable remediation steps, security references, and the specific compliance control that is violated.
    + **Ticketing Integration**: Violations automatically create tickets in Jira, ServiceNow, or similar platforms, with the full compliance context attached for the remediation assignee.
    + **False Positive Management**: Findings can be marked as exceptions with documented justification, so legitimate exceptions are tracked transparently without polluting compliance scores.

    **References:**
    - [Compliance Use Case](https://help.accuknox.com/use-cases/compliance/)
    - [Compliance Baseline Data](https://help.accuknox.com/resources/compliance-baseline-data/)
    - [Robust Compliance in Cloud-Native App Security](https://accuknox.com/blog/continuous-compliance)


??? "**16. How does AccuKnox support compliance for AI and LLM workloads?**"
    AccuKnox extends GRC principles to AI-specific compliance frameworks, covering models, agents, datasets, and AI infrastructure:
    + **NIST AI RMF**: Maps AI asset governance, risk classification, and control evidence to the NIST AI Risk Management Framework.
    + **EU AI Act**: Supports risk-tier classification (minimal, limited, high-risk) with policy controls and audit evidence aligned to EU AI Act requirements. EU AI Act enforcement starts August 2026 — AccuKnox compliance workflows are built for audit-ready evidence collection ahead of that deadline.
    + **ISO 42001**: AI management system standard compliance with structured governance, risk management, and lifecycle monitoring.
    + **OWASP LLM Top 10**: Continuous scanning and runtime enforcement against the OWASP LLM Top 10 vulnerability categories.
    + **MITRE ATLAS**: Adversarial threat landscape for AI systems mapped to detection and enforcement controls in the platform.
    + AI-BOM generation provides bills of materials for the full AI stack — models, frameworks, inference servers, vector databases, and training datasets — required for AI supply chain compliance.


[SCHEDULE DEMO](https://www.accuknox.com/contact-us){ .md-button .md-button--primary }