---
title: ASPM & DevSecOps FAQs
description: Frequently asked questions about AccuKnox Application Security Posture Management: SAST, DAST, SCA, IaC scanning, container scanning, secrets detection, CI/CD integration, ASPM reports, playbooks, and DevSecOps workflows.
hide:
  - toc
---

# ASPM & DevSecOps

## Core ASPM Platform

??? "**1. What is AccuKnox ASPM and what does it cover?**"
    **AccuKnox ASPM** (Application Security Posture Management) is the unified application security module inside the AccuKnox Zero Trust CNAPP. It tracks risk posture across your whole application architecture. Coverage runs from source code and open-source dependencies, through containers and IaC, to runtime workloads.

    Core capabilities:

    - **SAST:** Static Application Security Testing finds vulnerabilities in source code at the earliest stages of development.
    - **DAST:** Dynamic Application Security Testing finds exploitable vulnerabilities in running web applications.
    - **SCA:** Software Composition Analysis finds CVEs and license risks in open-source dependencies.
    - **IaC Scanning:** Detects misconfigurations in Terraform, Helm and Kubernetes manifests before they reach production.
    - **Container Scanning:** Scans container images for CVEs, malware and supply chain risks before deployment.
    - **Secrets Scanning:** Detects hardcoded API keys, credentials and tokens in code repositories and CI/CD pipelines.
    - **SBOM Generation:** Builds a Software Bill of Materials for full dependency lineage and audit readiness.
    - **Runtime Correlation:** Uses eBPF-powered code-to-runtime correlation to rank what is actually exploitable in production.
    - **ASPM Reports and Playbooks:** Delivers automated posture reports, compliance evidence and playbook-driven remediation workflows.

    **References:**

    - [ASPM Overview](https://help.accuknox.com/how-to/aspm-overview/)

??? "**2. How does AccuKnox ASPM differ from using standalone SAST, DAST, and SCA tools?**"
    **AccuKnox ASPM connects the findings** that standalone tools leave in silos. Siloed findings are hard for anyone to act on.

    - **Standalone SAST:** It lists code vulnerabilities with no context on whether they are reachable in your runtime environment.
    - **Standalone DAST:** It shows what is vulnerable in the running app. It cannot trace the issue back to the code commit that introduced it.
    - **Cross-layer correlation:** AccuKnox ASPM traces a vulnerability from its commit, through the container image, to runtime behavior in production. You get one traceable finding with actionable remediation context.
    - **Policy-as-code:** The same controls that generate findings also gate CI/CD pipelines. They block non-compliant code from reaching production.
    - **Continuous compliance evidence:** AccuKnox generates evidence continuously from correlated ASPM signals. You do not assemble it by hand from separate tool reports before each audit.

    **References:**

    - [Top 8 ASPM Tools for 2026](https://accuknox.com/blog/aspm-tools)

??? "**3. What CI/CD platforms does AccuKnox ASPM support?**"
    AccuKnox integrates with all major CI/CD platforms and version control systems:

    - **Version Control**: GitHub, GitLab, Bitbucket, Azure Repos
    - **CI/CD**: GitHub Actions, GitLab CI/CD, Jenkins, Azure DevOps, AWS CodePipeline, Bitbucket Pipelines, CircleCI, GCP Cloud Build, Harness
    - **Integration Types**: Native plugins, GitHub Actions marketplace, workflow file integration, and REST API for custom pipelines

    To set up, generate an **AccuKnox API token** and store it as a secret in your CI/CD environment. Then set the endpoint and label variables, which route scan results.

    **References:**

    - [CI/CD Integration Overview](https://help.accuknox.com/integrations/cicd-overview/)

## DAST (Dynamic Application Security Testing)

??? "**4. What DAST scan types does AccuKnox support?**"
    AccuKnox supports six DAST scan types for different testing scenarios:

    - **Unauthenticated Scans:** Scan public web applications and APIs without login credentials. They find what unauthenticated attackers can see, which suits public-facing endpoints.
    - **Authenticated Scans:** Scan applications behind a login wall with stored session credentials. They cover authenticated attack surfaces, including functionality specific to a user role.
    - **MFA-Enabled Scans:** Give full DAST coverage for apps behind Multi-Factor Authentication, through TOTP-based credential flows. Supported apps include OWASP Juice Shop with MFA enabled.
    - **XSS-Focused Scans:** Target reflected, stored and DOM-based Cross-Site Scripting vulnerabilities across web application surfaces.
    - **Baseline Scans:** Run quick, lightweight checks inside CI/CD pipelines without significant build delays.
    - **Full Active Scans:** Run deeper scans in pre-production or staging environments that need more coverage.

    **References:**

    - [DAST Scan Types](https://help.accuknox.com/how-to/dast-scan-types/)


??? "**5. How does AccuKnox detect XSS vulnerabilities through DAST?**"
    AccuKnox detects XSS with **targeted active probes** in its DAST scanning engine:

    - **Active probes:** The engine injects XSS payloads into URL parameters, form fields, headers and JSON body fields. It finds reflected, stored and DOM-based XSS.
    - **Categorized findings:** Each finding shows its XSS type, injection point, proof of exploitation, and severity from OWASP risk scoring.
    - **SAST correlation:** XSS results appear in the AccuKnox platform next to SAST findings for the same application. Teams see whether a code-level XSS issue is also exploitable at runtime.
    - **CI/CD scans:** You can embed DAST XSS scans in CI/CD pipelines. They catch new XSS vulnerabilities from active development before production.

    **References:**

    - [DAST XSS Use Case](https://help.accuknox.com/use-cases/dast-xss/)
    - [DAST Scan Types](https://help.accuknox.com/how-to/dast-scan-types/)
    - [DAST Unauthenticated Scans](https://help.accuknox.com/how-to/dast-scan-no-auth/)

---

## SAST (Static Application Security Testing)

??? "**6. How does AccuKnox SAST work and what does it detect?**"
    AccuKnox SAST analyzes source code **without running the application**, so it finds vulnerabilities at the earliest stage of development:

    - **Detection scope:** Scans the full codebase for SQL injection, command injection, XSS, insecure cryptographic practices, hardcoded credentials, insecure API usage and coding standards violations.
    - **Code and libraries:** Analyzes both proprietary application code and the libraries it imports.
    - **Where it runs:** Runs in developer IDEs for real-time feedback, on code commits for pre-merge gates, and in CI/CD pipelines for build-phase checks.
    - **AI acceleration:** The built-in SAST engine uses AI acceleration for faster scan cycles without losing detection quality.
    - **DAST correlation:** SAST findings upload to the AccuKnox dashboard and correlate with DAST findings from the same application. Teams see which static vulnerabilities are also dynamically exploitable.
    - **Language support:** Supports multiple languages and frameworks for polyglot development environments.

    **References:**

    - [SAST Use Case (SonarQube)](https://help.accuknox.com/use-cases/sast-sq/)

??? "**7. Does AccuKnox SAST require a separate scanning tool like SonarQube?**"
    **No.** AccuKnox includes a native, built-in SAST engine, so you need no third-party scanner instance.

    - **Built in:** The high-performance static analysis engine is part of the platform. You do not set up or maintain a separate SonarQube or SonarCloud instance.
    - **Pipeline triggers:** Scans run in CI/CD through the AccuKnox GitHub Action, GitLab CI/CD plugin, Jenkins integration or Azure DevOps task. They trigger on every push or pull request.
    - **Unified view:** Results upload automatically to the AccuKnox dashboard under Issues → Findings. There they correlate with DAST, SCA, IaC and container scan findings from the same application.
    - **AI-accelerated mode:** Cuts scan cycle times without losing detection coverage. This helps teams with large codebases that need fast pipeline feedback.
    - **SonarQube ingestion:** If you already run SonarQube or SonarCloud, AccuKnox can ingest those results through its CI/CD plugins. You keep your scanner and gain central AccuKnox visibility.

---

## IaC Scanning (Infrastructure as Code)

??? "**8. How does AccuKnox IaC scanning work?**"
    AccuKnox IaC scanning finds misconfigurations in infrastructure-as-code files **before they become cloud resources**:

    - **Formats:** Scans Terraform, Helm charts, Kubernetes manifests, CloudFormation, AWS CDK output and other IaC formats.
    - **Compliance mapping:** Maps each finding to compliance benchmarks (CIS, NIST, PCI DSS, HIPAA). Every misconfiguration shows its regulatory impact next to its technical detail.
    - **Central triage:** Sends results to the AccuKnox dashboard automatically, under Issues → Findings → IaC Findings.
    - **Observe or enforce:** The `soft_fail` option lets teams start in observe mode, where the pipeline continues despite violations. Later they switch to enforce mode, where violations break the pipeline.
    - **Public asset tagging:** Every scan auto-flags externally reachable cloud resources. Misconfigured public-facing assets show in the inventory instead of a weekly report.

    **References:**

    - [GitHub IaC Scan](https://help.accuknox.com/how-to/github-iac-scan/)
    - [AWS CDK IaC Scan](https://help.accuknox.com/how-to/aws-cdk-iac-scan/)

??? "**9. How does AccuKnox IaC scanning integrate with GitHub?**"
    AccuKnox integrates with GitHub through a **native GitHub Action** for IaC scanning:

    - **The action:** `accuknox/iac-scan-action@latest` scans Terraform and Kubernetes configuration files on every push or pull request.
    - **Setup:** Create an AccuKnox token under Settings → Tokens and a label for scan result tagging. Then add `TOKEN`, `ENDPOINT` and `LABEL` as GitHub repository secrets.
    - **Automatic upload:** Results go to the AccuKnox Console automatically. You do not download or parse scan output by hand.
    - **Optional parameters:** Set the scan directory, output format (JSON), output file path and `soft_fail` (continue vs. break the pipeline on violations).
    - **Branch filtering:** Regex branch filtering keeps findings on production-bound branches. It cuts noise from feature branches and experiment forks.
    - **Azure DevOps parity:** Azure DevOps now matches GitHub for IaC scanning, including branch filtering and result routing.

    **References:**

    - [GitHub IaC Scan](https://help.accuknox.com/how-to/github-iac-scan/)
    - [IaC Scan Use Case](https://help.accuknox.com/use-cases/iac-scan/)

??? "**10. How does AccuKnox support IaC scanning for AWS CDK?**"
    AccuKnox scans the **synthesized CloudFormation output** of AWS Cloud Development Kit (CDK) projects:

    - **Synthesized output:** AWS CDK generates CloudFormation templates from code. AccuKnox scans that output for misconfigurations before deployment.
    - **Pipeline flow:** The CI/CD pipeline runs `cdk synth` to generate the template, then passes the output to the AccuKnox IaC scanner.
    - **Benchmark mapping:** Findings map to AWS security best practices, CIS AWS benchmarks and relevant compliance frameworks.
    - **One view:** Results upload to the AccuKnox dashboard next to IaC findings from Terraform and Kubernetes manifests.
    - **No rework:** Teams on AWS CodePipeline or GitHub Actions can add the scan step without restructuring their build workflow.

    **References:**

    - [AWS CDK IaC Scan](https://help.accuknox.com/how-to/aws-cdk-iac-scan/)

---

## Container Scanning

??? "**11. How does AccuKnox container scanning work?**"
    AccuKnox scans container images for **CVEs, malware and supply chain risks** before they reach production:

    - **CVE scanning:** CVE/NVD-powered scanning finds known vulnerabilities in OS packages, language runtimes and application dependencies in the image.
    - **SBOM generation:** Every scanned image gets a complete Software Bill of Materials with all packages, versions and licenses.
    - **Supply chain integrity:** Checks detect malicious payloads in base images, compromised layers, and packages from untrusted registries.
    - **CI/CD gating:** AccuKnox scans images at build time. Findings gate the image before it goes to a registry or to Kubernetes.
    - **Runtime correlation:** Dashboard findings correlate with runtime behavior from KubeArmor. Teams see whether a vulnerable package is actually invoked in production.
    - **Registry scanning:** Covers images already in registries (Amazon ECR, Azure Container Registry, Google Container Registry, Docker Hub, Quay, Harbor, JFrog), plus images being built.

    **References:**

    - [Container Scan Use Case](https://help.accuknox.com/use-cases/container-scan/)

??? "**12. What types of vulnerabilities does AccuKnox container scanning detect?**"
    AccuKnox container scanning detects these container and supply chain issues:

    - **RCE (Remote Code Execution)**: Vulnerable packages that allow arbitrary code execution if exploited.
    - **DoS (Denial of Service)**: Dependencies with known DoS vulnerabilities that could affect service availability.
    - **Authentication Issues**: Container runtime misconfigurations that expose authentication bypass paths.
    - **Sensitive Data Leaks**: Hardcoded secrets, credentials or tokens baked into container image layers.
    - **Malicious Images**: Payloads embedded in public images from community registries (for example, Hugging Face and Docker Hub).
    - **License Violations**: Open-source packages with copyleft licenses that may create compliance obligations.
    - **Outdated Base Images**: Images built on EOL (end-of-life) base OS versions with unpatched CVEs.

    **References:**

    - [Container Scan Use Case](https://help.accuknox.com/use-cases/container-scan/)

---

## Secrets Scanning

??? "**13. How does AccuKnox secrets scanning work in CI/CD pipelines?**"
    AccuKnox detects hardcoded secrets in code repositories, containers and Kubernetes configurations **before they are exposed**:

    - **Pipeline integration:** Runs in GitHub Actions, Jenkins, GitLab, Azure DevOps and other supported platforms. It scans on every push with no manual trigger.
    - **What it detects:** Finds API keys, OAuth tokens, database passwords, SSH private keys, cloud credentials (AWS, Azure, GCP) and custom secret patterns.
    - **Metadata only:** AccuKnox receives only scan results (findings metadata). The sensitive data itself never reaches the platform.
    - **Central triage:** Findings appear in the AccuKnox dashboard under Issues → Findings → Secret Scan Findings for triage and remediation workflow.
    - **Remediation guidance:** Recommends secret rotation and a move to a secure secrets manager (Vault, AWS Secrets Manager, Azure Key Vault).
    - **AWS credentials:** AWS-specific secret scanning in CI/CD pipelines detects credentials that could allow unauthorized cloud account access.

    **References:**

    - [Secret Scanning in CI/CD (AWS) Use Case](https://help.accuknox.com/use-cases/secret-scan-cicd-aws/)

---

## ASPM Reports & Playbooks

??? "**14. What ASPM reports does AccuKnox generate?**"
    AccuKnox ASPM generates four structured reports for security review, compliance audit and executive visibility:

    - **ASPM Posture Report:** Shows application security posture across all scan types (SAST, DAST, SCA, IaC, container and secrets). Trend data shows improvement or regression over time.
    - **Vulnerability Summary Report:** Aggregates findings by severity, scan type, application and team. AppSec and development leads get a prioritized remediation queue.
    - **Compliance Mapping Report:** Maps findings to specific compliance control requirements (OWASP Top 10, PCI DSS, HIPAA, NIST, SOC 2), with pass/fail status for each control.
    - **Pipeline Security Report:** Shows what CI/CD-integrated scans detected at each pipeline stage, what was blocked and what was remediated.

    Reports come in **PDF, CSV and JSON** formats. You can schedule daily, weekly or monthly delivery.

    **References:**

    - [ASPM Reports Use Case](https://help.accuknox.com/use-cases/aspm-reports/)
    - [ASPM Report PDF](https://help.accuknox.com/resources/assets/ASPM_Report.pdf)

## DevSecOps & Shift-Left Security

??? "**15. How does AccuKnox enable shift-left security in DevSecOps workflows?**"
    AccuKnox embeds security at **every stage of the development lifecycle**, from the first line of code to production runtime:

    - **IDE Integration:** SAST feedback appears during coding, so developers see vulnerabilities before they commit.
    - **Pre-Commit Gates:** Secrets scanning and IaC checks run on code commits and keep insecure changes out of the repository.
    - **CI/CD Integration:** SAST, SCA, DAST, IaC and container scans run inside pipeline stages. They fail builds on policy violations before deployment.
    - **Registry Scanning:** AccuKnox scans registry images continuously. A previously clean image is flagged when a new CVE affecting it is published.
    - **Runtime Correlation:** eBPF-powered runtime visibility links code-phase findings to production behavior. Teams know which vulnerabilities attackers actually reach.
    - **Policy-as-Code:** Security rules are version-controlled and apply the same way across all scan stages. The same standards apply at commit, build and deploy.

    **References:**

    - [DevSecOps Getting Started](https://help.accuknox.com/getting-started/devsecops/)
    - [ASPM Overview](https://help.accuknox.com/how-to/aspm-overview/)
    - [CI/CD Integration Overview](https://help.accuknox.com/integrations/cicd-overview/)
    - [CI/CD Support Matrix](https://help.accuknox.com/support-matrix/cicd-support-matrix/#integration-types)


## Risk Prioritization & Remediation

??? "**16. How does AccuKnox ASPM prioritize which vulnerabilities to fix first?**"
    AccuKnox ranks vulnerabilities across **multiple risk dimensions**, so the real risks rise to the top:

    - **Exploitability:** EPSS (Exploit Prediction Scoring System) scores flag vulnerabilities with active exploit activity. These rank above theoretical risks with high CVSS scores but no known exploits.
    - **Runtime Reachability:** eBPF-powered runtime correlation finds which vulnerable code paths production actually calls. The fix list shrinks to what is exposed.
    - **Business Impact:** Priority scores factor in asset criticality (production vs. staging, customer-facing vs. internal). A critical vulnerability in a non-critical internal tool ranks below a medium one in a payment service.
    - **Exposure:** Publicly reachable services and APIs rank above internal-only services at the same vulnerability severity.
    - **Remediation Age:** Long-unresolved high-severity findings escalate automatically, so they do not sit in a backlog indefinitely.

    **References:**

    - [ASPM Overview](https://help.accuknox.com/how-to/aspm-overview/)

??? "**17. How does AccuKnox connect code vulnerabilities to runtime behavior?**"
    AccuKnox links ASPM scan findings to what actually happens in production. This **code-to-runtime correlation** is its unique differentiator.

    - **Code paths:** SAST finds vulnerable code paths in source code. eBPF-powered runtime monitoring (KubeArmor) observes which of those paths production workloads execute.
    - **Traffic-based priority:** A vulnerable function that production never calls is deprioritized. One with active traffic is escalated immediately, especially if it handles sensitive data.
    - **Syscall tracing:** Runtime syscall tracing profiles application behavior in real time. It ties application actions to risk signals and finds anomalies without impacting performance.
    - **Container correlation:** Container scanning findings correlate with runtime behavior. A vulnerable package the running application never loads ranks below one it actively imports.
    - **Shorter fix list:** Code-to-runtime traceability cuts the fix list teams must act on. It removes the noise that overwhelms standalone ASPM tools without runtime context.

    **References:**

    - [ASPM Overview](https://help.accuknox.com/how-to/aspm-overview/)
    - [ASPM Use Case](https://help.accuknox.com/use-cases/aspm/)
    - [DevSecOps Getting Started](https://help.accuknox.com/getting-started/devsecops/)

---

## Compliance & Audit

??? "**18. How does AccuKnox ASPM generate audit-ready evidence from DevSecOps workflows?**"
    AccuKnox turns every CI/CD pipeline security scan into **timestamped, compliance-ready audit evidence**:

    - **Immutable records:** Every pipeline scan creates an immutable record. It logs what was scanned, when, what was found, which policy applied and the action taken (passed, flagged, blocked).
    - **Timestamped controls:** Compliance control evaluations carry timestamps. Auditors can verify each control was validated at deployment time, not assembled retroactively.
    - **Posture over time:** ASPM posture reports show trend lines, remediation velocity and control coverage over time, instead of a single point-in-time snapshot.
    - **SBOM records:** An SBOM for every application release gives the dependency lineage evidence that PCI DSS v4.0.1 and the EU Cyber Resilience Act require.
    - **Audit-ready exports:** PDF, CSV and JSON exports match the evidence format that PCI DSS QSAs, SOC 2 auditors and HIPAA security rule reviewers require. This cuts manual compilation of audit packages.

    **References:**

    - [ASPM Reports Use Case](https://help.accuknox.com/use-cases/aspm-reports/)
    - [ASPM Report PDF](https://help.accuknox.com/resources/assets/ASPM_Report.pdf)
    - [ASPM Overview](https://help.accuknox.com/how-to/aspm-overview/)
    - [DevSecOps Getting Started](https://help.accuknox.com/getting-started/devsecops/)

---

[SCHEDULE DEMO](https://www.accuknox.com/contact-us){ .md-button .md-button--primary }
