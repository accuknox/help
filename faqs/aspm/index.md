---
title: ASPM & DevSecOps FAQs
description: Frequently asked questions about AccuKnox Application Security Posture Management — SAST, DAST, SCA, IaC scanning, container scanning, secrets detection, CI/CD integration, ASPM reports, playbooks, and DevSecOps workflows.
hide:
  - toc
---

# ASPM & DevSecOps

## Core ASPM Platform

??? "**1. What is AccuKnox ASPM and what does it cover?**"
    AccuKnox ASPM (Application Security Posture Management) is a unified application security module built into the AccuKnox Zero Trust CNAPP. It maintains a comprehensive risk posture across your application architecture — from source code and open-source dependencies through containers, IaC, and into runtime workloads.

    Core capabilities include:
    + **SAST** — Static Application Security Testing to detect vulnerabilities in source code at the earliest stages of development.
    + **DAST** — Dynamic Application Security Testing to identify exploitable vulnerabilities in running web applications.
    + **SCA** — Software Composition Analysis to find CVEs and license risks in open-source dependencies.
    + **IaC Scanning** — Detect misconfigurations in Terraform, Helm, and Kubernetes manifests before they reach production.
    + **Container Scanning** — Scan container images for CVEs, malware, and supply chain risks before deployment.
    + **Secrets Scanning** — Detect hardcoded API keys, credentials, and tokens in code repositories and CI/CD pipelines.
    + **SBOM Generation** — Software Bill of Materials for full dependency lineage and audit readiness.
    + **Runtime Correlation** — Code-to-runtime risk correlation using eBPF-powered insights to prioritize what is actually exploitable in production.
    + **ASPM Reports and Playbooks** — Automated posture reports, compliance evidence, and playbook-driven remediation workflows.

    **References:**
    - [ASPM Overview](https://help.accuknox.com/how-to/aspm-overview/)

??? "**2. How does AccuKnox ASPM differ from using standalone SAST, DAST, and SCA tools?**"
    Standalone tools generate siloed findings that no one can act on efficiently. AccuKnox ASPM connects them:
    + A standalone SAST tool gives you a list of code vulnerabilities with no context about whether they are reachable in your specific runtime environment.
    + A standalone DAST tool tells you what is vulnerable in the running app but cannot trace it back to the code commit that introduced it.
    + AccuKnox ASPM correlates findings across all layers — from the commit that introduced a vulnerability through the container image that packaged it to the runtime behavior in production — giving a single, traceable finding with actionable remediation context.
    + Policy-as-code enforcement means the same controls that generate findings also gate CI/CD pipelines, preventing non-compliant code from reaching production.
    + Compliance evidence is generated continuously from correlated ASPM signals — not assembled manually from separate tool reports before each audit.

    **References:**
    - [Top 8 ASPM Tools for 2026](https://accuknox.com/blog/aspm-tools)

??? "**3. What CI/CD platforms does AccuKnox ASPM support?**"
    AccuKnox integrates with all major CI/CD platforms and version control systems:
    + **Version Control**: GitHub, GitLab, Bitbucket, Azure Repos
    + **CI/CD**: GitHub Actions, GitLab CI/CD, Jenkins, Azure DevOps, AWS CodePipeline, Bitbucket Pipelines, CircleCI, GCP Cloud Build, Harness
    + **Integration Types**: Native plugins, GitHub Actions marketplace, workflow file integration, and REST API for custom pipelines
    Setup requires generating an AccuKnox API token and configuring it as a secret in your CI/CD environment, along with the endpoint and label variables for scan result routing.

    **References:**
    - [CI/CD Integration Overview](https://help.accuknox.com/integrations/cicd-overview/)

## DAST — Dynamic Application Security Testing

??? "**4. What DAST scan types does AccuKnox support?**"
    AccuKnox supports multiple DAST scan types to match different testing scenarios:
    + **Unauthenticated Scans**: Scan publicly accessible web applications and APIs without requiring login credentials. Identifies vulnerabilities visible to unauthenticated attackers — ideal for public-facing endpoints.
    + **Authenticated Scans**: Scan applications behind a login wall using stored session credentials. Covers authenticated attack surfaces including user-role-specific functionality.
    + **MFA-Enabled Scans**: Full DAST coverage for applications protected by Multi-Factor Authentication using TOTP-based credential flows — supporting apps like OWASP Juice Shop with MFA enabled.
    + **XSS-Focused Scans**: Targeted scans for Cross-Site Scripting vulnerabilities including reflected, stored, and DOM-based XSS across web application surfaces.
    + **Baseline Scans**: Quick, lightweight scans suitable for embedding in CI/CD pipelines without causing significant build delays.
    + **Full Active Scans**: Comprehensive scans for pre-production or staging environments where deeper coverage is required.

    **References:**
    - [DAST Scan Types](https://help.accuknox.com/how-to/dast-scan-types/)


??? "**5. How does AccuKnox detect XSS vulnerabilities through DAST?**"
    AccuKnox provides targeted XSS detection through its DAST scanning engine:
    + Active probes inject XSS payloads across input vectors — URL parameters, form fields, headers, and JSON body fields — to identify reflected, stored, and DOM-based XSS vulnerabilities.
    + Findings are categorized by XSS type and include the specific injection point, proof of exploitation, and severity based on OWASP risk scoring.
    + XSS scan results are surfaced in the AccuKnox platform alongside SAST findings for the same application — allowing teams to see whether code-level XSS issues are also exploitable at runtime.
    + DAST XSS scans can be embedded in CI/CD pipelines to catch new XSS vulnerabilities introduced during active development before they reach production.

    **References:**
    - [DAST XSS Use Case](https://help.accuknox.com/use-cases/dast-xss/)
    - [DAST Scan Types](https://help.accuknox.com/how-to/dast-scan-types/)
    - [DAST Unauthenticated Scans](https://help.accuknox.com/how-to/dast-scan-no-auth/)

---

## SAST — Static Application Security Testing

??? "**6. How does AccuKnox SAST work and what does it detect?**"
    AccuKnox SAST analyzes source code without executing the application to identify security vulnerabilities at the earliest stage of development:
    + Scans the full codebase for security flaws including SQL injection, command injection, XSS, insecure cryptographic practices, hardcoded credentials, insecure API usage, and coding standards violations.
    + Analyzes both proprietary application code and the libraries it imports for comprehensive vulnerability coverage.
    + Runs in developer IDEs for real-time feedback during coding, on code commits for pre-merge gates, and in CI/CD pipelines for build-phase security checks.
    + AccuKnox's built-in SAST engine uses AI-acceleration for faster scan cycles without sacrificing detection quality.
    + SAST findings are uploaded to the AccuKnox dashboard and correlated with DAST findings from the same application — so teams can validate which static vulnerabilities are also dynamically exploitable.
    + Supports multiple languages and frameworks for versatile integration across polyglot development environments.

    **References:**
    - [SAST Use Case (SonarQube)](https://help.accuknox.com/use-cases/sast-sq/)

??? "**7. Does AccuKnox SAST require a separate scanning tool like SonarQube?**"
    AccuKnox includes a native, built-in SAST engine — no third-party scanner instance required:
    + AccuKnox's SAST engine is a high-performance static analysis engine built directly into the platform, so teams get SAST out of the box without setting up or maintaining a separate SonarQube or SonarCloud instance.
    + Scans run inside CI/CD pipelines via the AccuKnox GitHub Action, GitLab CI/CD plugin, Jenkins integration, or Azure DevOps task — triggered on every push or pull request.
    + Results are uploaded automatically to the AccuKnox dashboard under Issues → Findings, where they are correlated with DAST, SCA, IaC, and container scan findings from the same application for a unified posture view.
    + AI-accelerated scan mode reduces scan cycle times without sacrificing detection coverage — useful for teams with large codebases that need fast pipeline feedback.
    + For teams already running SonarQube or SonarCloud, AccuKnox also supports ingesting those scan results via its CI/CD plugins — so you can keep your existing scanner and gain centralized AccuKnox visibility on top of it.

---

## IaC Scanning — Infrastructure as Code

??? "**8. How does AccuKnox IaC scanning work?**"
    AccuKnox IaC scanning detects misconfigurations in infrastructure-as-code files before they are provisioned as cloud resources:
    + Scans Terraform, Helm charts, Kubernetes manifests, CloudFormation, AWS CDK output, and other IaC formats for security misconfigurations.
    + Findings are mapped to compliance benchmarks (CIS, NIST, PCI DSS, HIPAA) — so every misconfiguration is surfaced with its regulatory impact alongside its technical detail.
    + Scan results are sent to the AccuKnox dashboard automatically — visible under Issues → Findings → IaC Findings for centralized triage.
    + The `soft_fail` option allows teams to start with observe mode (pipeline continues even with violations) before switching to enforce mode (pipeline breaks on violations).
    + Public asset tagging auto-flags externally reachable cloud resources during every scan — so misconfigured public-facing assets are visible in the inventory, not buried in a weekly report.

    **References:**
    - [GitHub IaC Scan](https://help.accuknox.com/how-to/github-iac-scan/)
    - [AWS CDK IaC Scan](https://help.accuknox.com/how-to/aws-cdk-iac-scan/)

??? "**9. How does AccuKnox IaC scanning integrate with GitHub?**"
    AccuKnox provides a native GitHub Action for IaC scanning that integrates directly into GitHub CI/CD workflows:
    + The `accuknox/iac-scan-action@latest` GitHub Action scans Terraform and Kubernetes configuration files in your repository on every push or pull request.
    + Setup: Create an AccuKnox token under Settings → Tokens, create a label for scan result tagging, and configure `TOKEN`, `ENDPOINT`, and `LABEL` as GitHub repository secrets.
    + Results are uploaded automatically to the AccuKnox Console for centralized visibility — no manual download or parsing of scan output required.
    + Optional parameters include scan directory, output format (JSON), output file path, and `soft_fail` (continue vs. break the pipeline on violations).
    + Regex branch filtering keeps findings focused on production-bound branches — avoiding noise from feature branches or experiment forks.
    + Azure DevOps is now at full parity with GitHub for IaC scanning, including the same branch filtering and result routing capabilities.

    **References:**
    - [GitHub IaC Scan](https://help.accuknox.com/how-to/github-iac-scan/)
    - [IaC Scan Use Case](https://help.accuknox.com/use-cases/iac-scan/)

??? "**10. How does AccuKnox support IaC scanning for AWS CDK?**"
    AccuKnox provides dedicated IaC scanning support for AWS Cloud Development Kit (CDK) projects:
    + AWS CDK generates CloudFormation templates from code — AccuKnox scans the synthesized CloudFormation output for misconfigurations before deployment.
    + The integration works within CI/CD pipelines by running `cdk synth` to generate the CloudFormation template, then passing the output to the AccuKnox IaC scanner.
    + Findings are mapped to AWS security best practices, CIS AWS benchmarks, and relevant compliance frameworks.
    + Results are uploaded to the AccuKnox dashboard for triage alongside IaC findings from Terraform and Kubernetes manifests in the same unified view.
    + Teams using CDK in AWS CodePipeline or GitHub Actions can embed the scan step without restructuring their existing build workflow.

    **References:**
    - [AWS CDK IaC Scan](https://help.accuknox.com/how-to/aws-cdk-iac-scan/)

---

## Container Scanning

??? "**11. How does AccuKnox container scanning work?**"
    AccuKnox scans container images for CVEs, malware, and supply chain risks before they reach production:
    + CVE/NVD-powered scanning identifies known vulnerabilities in OS packages, language runtimes, and application dependencies bundled in the image.
    + SBOM generation provides a complete Software Bill of Materials for every scanned image — capturing all packages, versions, and licenses.
    + Supply chain integrity checks detect malicious payloads in base images, compromised layers, and packages pulled from untrusted registries.
    + Container scanning integrates into CI/CD pipelines — images are scanned at build time and findings are gated before the image is pushed to a registry or deployed to Kubernetes.
    + Findings appear in the AccuKnox dashboard correlated with runtime behavior from KubeArmor — so teams can see whether a vulnerable container package is actually being invoked in production.
    + Registry scanning extends coverage to images already in registries (Amazon ECR, Azure Container Registry, Google Container Registry, Docker Hub, Quay, Harbor, JFrog) — not just images being built.

    **References:**
    - [Container Scan Use Case](https://help.accuknox.com/use-cases/container-scan/)

??? "**12. What types of vulnerabilities does AccuKnox container scanning detect?**"
    AccuKnox container scanning covers a broad range of container and supply chain security issues:
    + **RCE (Remote Code Execution)**: Vulnerable packages that allow arbitrary code execution if exploited.
    + **DoS (Denial of Service)**: Dependencies with known DoS vulnerabilities that could affect service availability.
    + **Authentication Issues**: Misconfigurations in container runtime that expose authentication bypass paths.
    + **Sensitive Data Leaks**: Hardcoded secrets, credentials, or tokens baked into container image layers.
    + **Malicious Images**: Payloads embedded in public images pulled from community registries (e.g., Hugging Face, Docker Hub).
    + **License Violations**: Open-source packages with copyleft licenses that may create compliance obligations.
    + **Outdated Base Images**: Images built on EOL (end-of-life) base OS versions with unpatched CVEs.

    **References:**
    - [Container Scan Use Case](https://help.accuknox.com/use-cases/container-scan/)

---

## Secrets Scanning

??? "**13. How does AccuKnox secrets scanning work in CI/CD pipelines?**"
    AccuKnox detects hardcoded secrets in code repositories, containers, and Kubernetes configurations before they are exposed:
    + Integrates into CI/CD pipelines via GitHub Actions, Jenkins, GitLab, Azure DevOps, and other supported platforms — scanning on every push without requiring manual trigger.
    + Detects API keys, OAuth tokens, database passwords, SSH private keys, cloud credentials (AWS, Azure, GCP), and custom secret patterns.
    + Only scan results (findings metadata) are uploaded to AccuKnox — the sensitive data itself is never transmitted to the platform.
    + Findings appear in the AccuKnox dashboard under Issues → Findings → Secret Scan Findings for centralized triage and remediation workflow.
    + Remediation guidance recommends secret rotation and migration to a secure secrets manager (Vault, AWS Secrets Manager, Azure Key Vault).
    + AWS-specific secret scanning in CI/CD pipelines detects credentials that could be used for unauthorized cloud account access.

    **References:**
    - [Secret Scanning in CI/CD (AWS) Use Case](https://help.accuknox.com/use-cases/secret-scan-cicd-aws/)
---

## ASPM Reports & Playbooks

??? "**14. What ASPM reports does AccuKnox generate?**"
    AccuKnox ASPM generates structured reports for security review, compliance audit, and executive visibility:
    + **ASPM Posture Report**: A comprehensive view of application security posture across all scan types — SAST, DAST, SCA, IaC, container, and secrets — with trend data showing improvement or regression over time.
    + **Vulnerability Summary Report**: Aggregated findings by severity, scan type, application, and team — giving AppSec and development leads a prioritized remediation queue.
    + **Compliance Mapping Report**: Findings mapped to specific compliance control requirements (OWASP Top 10, PCI DSS, HIPAA, NIST, SOC 2) with pass/fail status for each control.
    + **Pipeline Security Report**: Findings from CI/CD-integrated scans showing what was detected at each pipeline stage, what was blocked, and what was remediated.
    Reports are available in PDF, CSV, and JSON formats and can be scheduled for daily, weekly, or monthly delivery.

    **References:**
    - [ASPM Reports Use Case](https://help.accuknox.com/use-cases/aspm-reports/)
    - [ASPM Report PDF](https://help.accuknox.com/resources/assets/ASPM_Report.pdf)

## DevSecOps & Shift-Left Security

??? "**15. How does AccuKnox enable shift-left security in DevSecOps workflows?**"
    AccuKnox embeds security at every stage of the development lifecycle — from the first line of code to production runtime:
    + **IDE Integration**: SAST feedback during active coding so developers see vulnerabilities as they write code — before commit.
    + **Pre-Commit Gates**: Secrets scanning and IaC checks run on code commits to prevent insecure changes from entering the repository.
    + **CI/CD Integration**: SAST, SCA, DAST, IaC, and container scanning embedded directly into pipeline stages — failing builds on policy violations before deployment.
    + **Registry Scanning**: Container images in registries are scanned continuously so vulnerabilities in previously clean images are caught when new CVEs are published.
    + **Runtime Correlation**: eBPF-powered runtime visibility connects code-phase findings to production behavior — so teams know which vulnerabilities are actually being reached by attackers.
    + **Policy-as-Code**: Security rules are version-controlled and applied consistently across all scan stages — enforcing the same standards at commit, build, and deploy.

    **References:**
    - [DevSecOps Getting Started](https://help.accuknox.com/getting-started/devsecops/)
    - [ASPM Overview](https://help.accuknox.com/how-to/aspm-overview/)
    - [CI/CD Integration Overview](https://help.accuknox.com/integrations/cicd-overview/)
    - [CI/CD Support Matrix](https://help.accuknox.com/support-matrix/cicd-support-matrix/#integration-types)


## Risk Prioritization & Remediation

??? "**16. How does AccuKnox ASPM prioritize which vulnerabilities to fix first?**"
    AccuKnox uses multi-dimensional risk prioritization to surface what actually matters:
    + **Exploitability**: EPSS (Exploit Prediction Scoring System) scores identify vulnerabilities with active exploit activity — pushing them above theoretical risks with high CVSS scores but no known exploits.
    + **Runtime Reachability**: eBPF-powered runtime correlation identifies which vulnerable code paths are actually being called in production — reducing the fix list to only what is genuinely exposed.
    + **Business Impact**: Asset criticality (production vs. staging, customer-facing vs. internal) is factored into priority scores — a critical vulnerability in a non-critical internal tool ranks lower than a medium vulnerability in a payment service.
    + **Exposure**: Publicly reachable services and APIs are prioritized over internal-only services even for the same vulnerability severity.
    + **Remediation Age**: Long-unresolved high-severity findings are escalated automatically so they do not stagnate in a backlog indefinitely.

    **References:**
    - [ASPM Overview](https://help.accuknox.com/how-to/aspm-overview/)

??? "**17. How does AccuKnox connect code vulnerabilities to runtime behavior?**"
    AccuKnox's unique differentiation is code-to-runtime correlation — connecting findings from ASPM scans to what is actually happening in production:
    + SAST findings identify vulnerable code paths in source code. eBPF-powered runtime monitoring (KubeArmor) observes which of those code paths are actually executed in production workloads.
    + A vulnerable function that is never called in production is deprioritized. A vulnerable function receiving active traffic — especially if it handles sensitive data — is escalated immediately.
    + Runtime syscall tracing provides real-time profiling of application behavior, tying application actions to risk signals and identifying anomalies without impacting performance.
    + Container scanning findings are correlated with runtime behavior — a vulnerable package in a container that is never loaded by the running application ranks lower than one actively imported.
    + This code-to-runtime traceability reduces the fix list teams actually need to act on — cutting through the noise that overwhelms standalone ASPM tools without runtime context.

    **References:**
    - [ASPM Overview](https://help.accuknox.com/how-to/aspm-overview/)
    - [ASPM Use Case](https://help.accuknox.com/use-cases/aspm/)
    - [DevSecOps Getting Started](https://help.accuknox.com/getting-started/devsecops/)

---

## Compliance & Audit

??? "**18. How does AccuKnox ASPM generate audit-ready evidence from DevSecOps workflows?**"
    AccuKnox converts every CI/CD pipeline security scan into timestamped, compliance-ready audit evidence:
    + Every scan run in the pipeline generates an immutable record — what was scanned, when it ran, what was found, what policy was applied, and what action was taken (passed, flagged, blocked).
    + Compliance control evaluations are timestamped so auditors can verify that controls were validated at the time of each deployment — not assembled retroactively.
    + ASPM posture reports provide a longitudinal view of application security posture — showing trend lines, remediation velocity, and control coverage over time rather than a single point-in-time snapshot.
    + SBOM records for every application release provide the dependency lineage evidence required by PCI DSS v4.0.1 and the EU Cyber Resilience Act.
    + Exportable report formats (PDF, CSV, JSON) match the evidence format required by PCI DSS QSAs, SOC 2 auditors, and HIPAA security rule reviewers — minimizing manual compilation of audit packages.

    **References:**
    - [ASPM Reports Use Case](https://help.accuknox.com/use-cases/aspm-reports/)
    - [ASPM Report PDF](https://help.accuknox.com/resources/assets/ASPM_Report.pdf)
    - [ASPM Overview](https://help.accuknox.com/how-to/aspm-overview/)
    - [DevSecOps Getting Started](https://help.accuknox.com/getting-started/devsecops/)

---

[SCHEDULE DEMO](https://www.accuknox.com/contact-us){ .md-button .md-button--primary }