---
title: Compliance FAQs
description: Frequently asked questions about AccuKnox Compliance: framework coverage, continuous compliance, audit readiness, policy-as-code, baselining, remediation, and multi-cloud GRC.
hide:
  - toc
---

# Compliance

## Core Compliance Platform

??? "**1. What is AccuKnox Compliance and what does it cover?**"
    AccuKnox Compliance is a continuous compliance platform built into the **AccuKnox Zero Trust CNAPP**. It automates policy enforcement, compliance monitoring, audit evidence, and risk remediation. It covers cloud, Kubernetes, VM, container, and AI workloads.

    Core capabilities:

    - **Automated Risk Assessments**: Continuously evaluate cloud, Kubernetes, and application environments against your risk posture, and alert on anomalies.
    - **Policy-as-Code**: Define security and compliance rules in YAML or JSON, and apply them the same way across all infrastructure.
    - **Compliance Benchmarking**: Map your current state to 33+ compliance frameworks with automated, audit-ready reports.
    - **Posture Dashboards**: Track violations, risk severity, compliance trends, and remediation progress in one view.
    - **Runtime Enforcement**: Block non-compliant behavior at the kernel level with eBPF/LSM, instead of only detecting and reporting it.
    - **Auto-Remediation**: Detect drift in cloud configurations, and trigger automated remediation or GitOps workflows before violations escalate.

    **References:**

    - [Compliance Use Case](https://help.accuknox.com/use-cases/compliance/)

??? "**2. Which compliance frameworks does AccuKnox support?**"
    AccuKnox supports **33+ compliance frameworks**, pre-configured with automatic control mapping. One enforcement action satisfies overlapping mandates at the same time. You avoid repeat policy work across regulatory bodies.

    Frameworks covered:

    - **Cloud Security**: CIS AWS Benchmarks (v1.4, v1.5, v4.0), CIS Azure, CIS GCP, AWS Foundational Security Best Practices
    - **Industry Standards**: HIPAA, PCI DSS (all 12 requirements and 78 sub-requirements), GDPR, SOC 2, ISO 27001 (2013 and 2022)
    - **Government and Defense**: NIST SP 800-53, NIST CSF, STIG, FedRAMP, CMMC 2.0, DoD
    - **AI and Emerging**: OWASP LLM Top 10, NIST AI RMF, MITRE ATLAS, ISO 42001
    - **Regional Frameworks**: MAS TRM (Singapore), DPDP (India), BAIT and VAIT (Germany), FISC (Japan), ISMS-P (Korea), SEBI CSCRF (India), CCPA (California), COPPA
    - **Operational**: MITRE ATT&CK, CIS Kubernetes Benchmarks, NERC CIP, CMMC

    **References:**

    - [Compliance Support Matrix](https://help.accuknox.com/support-matrix/compliance-matrix/)


??? "**3. How does AccuKnox deliver continuous compliance versus point-in-time audits?**"
    AccuKnox checks compliance **all the time**, instead of once a quarter. A quarterly snapshot from a traditional tool goes stale within days of any deployment change.

    - **Instant posture**: The dashboard shows posture scores for all applicable frameworks as soon as a cloud account is onboarded and scanned.
    - **New resources**: AccuKnox evaluates every new resource deployment against all configured compliance programs at once.
    - **Real-time drift**: AccuKnox detects configuration drift in real time, then triggers alerts or automated remediation before violations pile up.
    - **Continuous evidence**: AccuKnox generates timestamped, immutable audit evidence all the time, so you never assemble it by hand before an audit.
    - **Exportable reports**: PDF, CSV, and JSON reports show continuous compliance posture, beyond the state at report time.

    **Result:** AccuKnox cut audit preparation from **60 hours to under 5 hours per quarter**. The client was a financial services firm managing 200+ cloud accounts.


??? "**4. How does the AccuKnox compliance dashboard work?**"
    The AccuKnox compliance dashboard gives security and compliance teams **one real-time view** of posture across all configured frameworks.

    - **Find it**: Onboard a cloud account and finish the first scan. Then open the Compliance section in the nav bar to see all applicable compliance programs.
    - **Score per control**: Each compliance program breaks down into sub-controls. Percentage compliance equals passed checks divided by total checks (passed + failed + warning + not available).
    - **Drill down**: Click any compliance program or sub-control to open its list of misconfigurations.
    - **Filter**: On the detailed view tab, filter findings by cloud account, region, severity, check type, and many other dimensions.
    - **Report**: A dedicated compliance report scores you against each framework's requirements and rules, with full coverage detail.

    **References:**

    - [AccuKnox Compliance Platform](https://accuknox.com/platform/compliance)

??? "**5. What types of compliance reports does AccuKnox generate?**"
    AccuKnox generates **five report types** for audit and governance work.

    - **Compliance Report**: Scores your posture against one framework's requirements and rules, with a sub-control breakdown and remediation guidance.
    - **Cloud Asset Summary**: Gives a high-level posture overview per framework across all onboarded cloud accounts, for board and executive reporting.
    - **Posture Trend Report**: Tracks compliance score changes over time to show continuous improvement or flag regression.
    - **Findings Export**: Exports all violations, misconfigurations, and control failures in PDF, CSV, or JSON for auditors or internal ticketing.
    - **Compliance Evidence Package**: Holds timestamped, immutable control evaluation records for regulatory submissions, 3PAO audits, and supervisory reviews.

    Reports show only the services and frameworks enabled for the tenant, so output stays clean and relevant.


??? "**6. What is compliance baselining in AccuKnox and how does it work?**"
    Compliance baselining sets a **verified security baseline** for your workloads and cloud configurations. AccuKnox then checks all the time that the environment stays aligned to it.

    - **Advanced Baselining**: AccuKnox aligns with existing cloud postures to set a consistent, documented security baseline for each environment.
    - **Auto-Generated Policies**: AccuKnox generates security policies from observed workload behavior. You get app-specific baselines without writing policies by hand.
    - **Drift Detection**: Any deviation from the baseline triggers an alert or automated remediation. Examples are a new misconfiguration, a policy change, or an unauthorized resource.
    - **GitHub Repository Scans**: Baseline checks extend into code repositories. They scan IaC templates and source code for compliance gaps before deployment.
    - **Framework-Aligned Baselines**: Baselines map directly to compliance controls, so each drift event shows its regulatory impact at once.

    **References:**

    - [Compliance Baseline Data](https://help.accuknox.com/resources/compliance-baseline-data/)
    - [Compliance Use Case](https://help.accuknox.com/use-cases/compliance/)
    - [Robust Compliance in Cloud-Native App Security](https://accuknox.com/blog/continuous-compliance)


??? "**7. How does AccuKnox handle overlapping compliance frameworks to avoid duplicate work?**"
    AccuKnox maps shared technical controls across frameworks, so **one control check validates many frameworks**.

    - **One check, many frameworks**: One control evaluation satisfies overlapping NIST, CIS, PCI DSS, and HIPAA requirements where the controls share technical criteria.
    - **One finding**: A control failure shows once, with full regulatory context. It never splits into separate findings per framework.
    - **Less rework**: This removes repeat remediation workflows and reduces audit preparation overhead significantly.
    - **Custom mappings**: You can build custom mappings for your own requirements or for niche industry regulations outside the built-in frameworks.
    - **Financial services**: One assessment cycle maps shared controls across PCI DSS, SOX IT general controls, and SOC 2 Trust Services Criteria.

    **References:**

    - [Compliance Support Matrix](https://help.accuknox.com/support-matrix/compliance-matrix/)
    - [Compliance Baseline Data](https://help.accuknox.com/resources/compliance-baseline-data/)

??? "**8. How does AccuKnox enforce compliance at runtime instead of only reporting on it?**"
    AccuKnox **blocks non-compliant behavior at the kernel level** with eBPF/LSM through KubeArmor.

    - **Real-time blocking**: AccuKnox blocks a non-compliant process in real time instead of logging it for later review. Examples are unauthorized network egress, privilege escalation, and file tampering.
    - **Proactive posture**: Compliance posture holds before an incident, instead of being rebuilt after one.
    - **One rule set**: The same policy-as-code rules drive runtime enforcement and compliance reports. What AccuKnox measures is what it enforces.
    - **Drift correction**: Automated remediation workflows fix cloud misconfiguration drift. Depending on severity, they trigger GitOps PRs, auto-patches, or manual escalation.
    - **Per-workload modes**: You set enforcement mode per workload (observe, audit, or enforce). Teams can roll out controls without disrupting production.

??? "**9. How does policy-as-code work in AccuKnox Compliance?**"
    You define security and compliance rules **as code**, and AccuKnox applies them the same way across all infrastructure.

    - **Format**: You write policies in YAML or JSON and version-control them with application code, for full GitOps integration.
    - **Built-in rule sets**: Pre-defined rule sets for CIS, HIPAA, PCI DSS, MITRE, NIST, and STIG work out of the box. You need zero custom authoring to start.
    - **Custom rules**: You can write rules for your own requirements, niche industry regulations, or internal governance standards outside the built-in frameworks.
    - **Coverage**: One control plane applies policies across public cloud, private cloud, Kubernetes, VMs, and AI workloads.
    - **Change history**: AccuKnox tracks policy changes with version history and audit trails. They prove controls were updated, reviewed, and approved through a governed process.

    **References:**

    - [Compliance Use Case](https://help.accuknox.com/use-cases/compliance/)
    - [Compliance Baseline Data](https://help.accuknox.com/resources/compliance-baseline-data/)
    - [Robust Compliance in Cloud-Native App Security](https://accuknox.com/blog/continuous-compliance)

??? "**10. How does AccuKnox support regulatory audits and supervisory reviews?**"
    AccuKnox keeps **continuous, time-indexed audit evidence**. You can answer any regulatory inquiry without collecting evidence by hand.

    - **Point-in-time recall**: Control evaluations are timestamped and immutable. Auditors can rebuild the compliance posture at any point in time, beyond the current state.
    - **Automatic records**: AccuKnox captures configuration change histories and remediation records for every finding.
    - **Audit packages**: Exportable packages (PDF, CSV, JSON) give the exact evidence format each review needs. This covers PCI DSS QSAs, SOC 2 audits, HIPAA reviews, and supervisory examinations.
    - **Measured result**: AccuKnox cut audit preparation from 60 hours to under 5 hours per quarter for regulated enterprises.
    - **DoD compliance**: The Federal Government reached DoD compliance with 20% lower security costs, using AccuKnox's continuous model instead of legacy quarterly audits.

    **References:**

    - [Compliance Use Case](https://help.accuknox.com/use-cases/compliance/)
    - [Compliance Support Matrix](https://help.accuknox.com/support-matrix/compliance-matrix/)
    - [Top CNAPP Solutions for Compliance and Audit](https://accuknox.com/blog/cnapp-solutions-compliance-audit-support)
    - [Compliance for Financial Services](https://accuknox.com/platform/compliance/finance)


??? "**11. How does AccuKnox manage compliance across multi-cloud environments?**"
    AccuKnox manages compliance posture for **AWS, Azure, and GCP from one control plane**.

    - **Agentless onboarding**: Connect cloud accounts through an IAM role, service principal, or service account. You install no software on cloud infrastructure.
    - **Continuous scans**: AccuKnox scans all cloud resources against applicable frameworks. It shows misconfigurations and control failures in one dashboard.
    - **One view**: AccuKnox normalizes cross-cloud findings into one compliance view. You skip correlating findings from separate cloud-native security tools.
    - **Same checks everywhere**: A control evaluated on AWS is evaluated the same way on Azure and GCP, for a true multi-cloud compliance picture.
    - **Data residency**: CDR policies can alert and remediate if data assets are created outside approved geographic regions.

    **References:**

    - [Compliance Use Case](https://help.accuknox.com/use-cases/compliance/)


??? "**12. How does AccuKnox support compliance for financial services?**"
    AccuKnox has **purpose-built compliance support** for financial institutions.

    - **PCI DSS**: Continuous scanning against all 12 requirements and 78 sub-requirements across payment card data environments.
    - **SOC 2**: Trust Services Criteria validation, with automated control testing for security, availability, confidentiality, and processing integrity.
    - **SOX IT General Controls**: Monitoring, with change management tracking and documentation.
    - **MAS TRM** (Singapore): Pre-configured controls for Monetary Authority of Singapore Technology Risk Management guidelines.
    - **BAIT/VAIT** (Germany): IT risk management and operational resilience frameworks for German financial institutions and insurance companies.
    - **ISMS-P** (Korea): Financial information security and risk management compliance.
    - **Shared mappings**: Overlapping financial frameworks share control mappings. One assessment satisfies PCI DSS, SOC 2, and SOX requirements at once.

    **References:**

    - [Compliance for Financial Services](https://accuknox.com/platform/compliance/finance)
    - [Compliance Support Matrix](https://help.accuknox.com/support-matrix/compliance-matrix/)
    - [Compliance Baseline Data](https://help.accuknox.com/resources/compliance-baseline-data/)


??? "**13. How does AccuKnox support HIPAA compliance for healthcare organizations?**"
    AccuKnox gives **automated HIPAA compliance coverage** for healthcare cloud and AI workloads.

    - **Pre-configured controls**: HIPAA controls map to cloud infrastructure checks across AWS, Azure, and GCP. They cover administrative, physical, and technical safeguards.
    - **PII/PHI scanning**: Dataset-level scans detect regulated health data in AI training pipelines, storage buckets, and inference outputs.
    - **Prompt firewall**: The prompt firewall blocks PII/PHI from going to or coming from LLMs in real time.
    - **Customer result**: DeepOrigin achieved 85% reduction in PII leaks and enhanced HIPAA compliance with AccuKnox AI Security.
    - **Continuous evidence**: Continuous audit evidence meets HIPAA audit requirements without manual quarterly evidence collection.

    **References:**

    - [Compliance Use Case](https://help.accuknox.com/use-cases/compliance/)
    - [Compliance Support Matrix](https://help.accuknox.com/support-matrix/compliance-matrix/)
    - [AccuKnox Compliance Platform](https://accuknox.com/platform/compliance)


??? "**14. How does AccuKnox support government and defense compliance (STIG, FedRAMP, CMMC)?**"
    AccuKnox has **purpose-built compliance support** for government and defense environments.

    - **STIG**: Security Technical Implementation Guide checks for VMs, containers, and Kubernetes clusters. They assess OS hardening, application configuration, and runtime behavior.
    - **FedRAMP**: Continuous compliance monitoring for federal cloud deployments, with automated control evidence.
    - **CMMC 2.0**: Cybersecurity Maturity Model Certification controls mapped to cloud and Kubernetes workloads, for defense contractor supply chain security.
    - **DoD**: AccuKnox helped the Federal Government achieve DoD compliance with 20% lower security costs than legacy approaches.
    - **Air-gapped**: Air-gapped deployment support lets classified and government-restricted environments reach full compliance without external connectivity.

    **References:**

    - [Compliance Support Matrix](https://help.accuknox.com/support-matrix/compliance-matrix/)
    - [Compliance Baseline Data](https://help.accuknox.com/resources/compliance-baseline-data/)
    - [Top CNAPP Solutions for Compliance and Audit](https://accuknox.com/blog/cnapp-solutions-compliance-audit-support)


??? "**15. How does AccuKnox handle compliance violations and remediation?**"
    AccuKnox resolves violations in **three modes**: automated, guided, and manual.

    - **Auto-Remediation**: AccuKnox can fix cloud misconfigurations automatically. Examples are closing public S3 bucket access, reverting IAM policy changes, or restoring compliant configurations.
    - **GitOps PR Generation**: For IaC-managed environments, AccuKnox opens a pull request with the exact code fix. The PR goes through your existing developer review.
    - **Guided Remediation**: Each finding includes remediation steps, security references, and the compliance control it violates.
    - **Ticketing Integration**: Violations automatically create tickets in Jira, ServiceNow, or similar platforms, with full compliance context for the assignee.
    - **False Positive Management**: You can mark findings as exceptions with a documented reason. AccuKnox tracks them openly, and they stay out of compliance scores.

    **References:**

    - [Compliance Use Case](https://help.accuknox.com/use-cases/compliance/)
    - [Compliance Baseline Data](https://help.accuknox.com/resources/compliance-baseline-data/)
    - [Robust Compliance in Cloud-Native App Security](https://accuknox.com/blog/continuous-compliance)


??? "**16. How does AccuKnox support compliance for AI and LLM workloads?**"
    AccuKnox extends compliance to **AI-specific frameworks**. It covers models, agents, datasets, and AI infrastructure.

    - **NIST AI RMF**: Maps AI asset governance, risk classification, and control evidence to the NIST AI Risk Management Framework.
    - **EU AI Act**: Supports risk-tier classification (minimal, limited, high-risk) with policy controls and audit evidence aligned to EU AI Act requirements. Enforcement starts August 2026, and AccuKnox workflows collect audit-ready evidence ahead of that deadline.
    - **ISO 42001**: AI management system standard compliance, with structured governance, risk management, and lifecycle monitoring.
    - **OWASP LLM Top 10**: Continuous scanning and runtime enforcement against the OWASP LLM Top 10 vulnerability categories.
    - **MITRE ATLAS**: Maps the adversarial threat landscape for AI systems to detection and enforcement controls in the platform.
    - **AI-BOM**: AI-BOM generation gives bills of materials for the full AI stack, as AI supply chain compliance requires. The stack covers models, frameworks, inference servers, vector databases, and training datasets.


[SCHEDULE DEMO](https://www.accuknox.com/contact-us){ .md-button .md-button--primary }
