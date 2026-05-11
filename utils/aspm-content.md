# ASPM — Application Security Posture Management

---

## Definition

Application Security Posture Management (ASPM) is a practice that maintains a comprehensive risk posture for application architecture, including services, libraries, APIs, dependencies, attack surfaces, and sensitive data flows. It enables quick identification and prioritization of business-critical risks across the software development lifecycle (SDLC).

ASPM brings together static analysis (SAST), software composition analysis (SCA), infrastructure-as-code scanning (IaC), dynamic testing (DAST), secret scanning, and runtime insights into a unified platform. It empowers AppSec, DevOps, and SecOps teams to collaborate without context switching or alert fatigue.

---

## Pain Points

- Most vulnerability findings are noise — false positives, unexploitable issues, and findings with no runtime context flood security queues with 10,000+ alerts
- AppSec and CloudSec teams operate in silos without shared context, meaning a cloud misconfiguration and an application vulnerability are never correlated
- No single source of truth exists across code, CI/CD pipeline, and runtime
- Manual penetration testing every few months creates long windows of exposure — a basic configuration change by a developer can go undetected until the next scheduled test
- Security signals are scattered across disconnected tools (SonarQube, Trivy, Checkov, ZAP, Gitleaks, etc.) with no normalization or cross-tool correlation
- Third-party dependency vulnerabilities accumulate silently — supply chain risk is invisible until a breach
- Sensitive data such as RSA private keys, API tokens, and credentials are embedded inside container images and pushed to registries
- IaC templates deploy with misconfigurations — S3 buckets without `restrict_public_buckets`, containers with `allowPrivilegeEscalation: true`
- Developers lack feedback in the build pipeline — security findings only surface in separate dashboards after deployment
- No runtime context for static findings — teams cannot distinguish between a vulnerability that is reachable and one that is never executed
- Manual correlation of alerts slows down remediation and increases mean time to resolution (MTTR)
- Supply chain attacks target open-source components that pass standard code review
- No visibility into third-party software components, SBOM, or software bill of materials
- Authentication vulnerabilities in transitive dependencies (e.g., libcurl, curl) remain undetected
- Secrets in CI/CD pipelines, code repositories, S3 buckets, Kubernetes ConfigMaps, and container images are never systematically scanned

---

## Use Cases

### Container Scanning
- Dependency analysis — scanning for supply chain vulnerabilities in Golang, Python, Node.js packages
- Scan for sensitive data exposure — RSA private keys, API tokens, credentials embedded in container images
- Authentication vulnerabilities — detect authentication bypass flaws (e.g., curl/libcurl CVEs) in image layers
- Registry-based scanning with configurable schedules and regex-based image filtering
- Scan images before and after deployment; view findings in context of workloads

### IaC Scanning
- Public cloud exposure — S3 buckets without `restrict_public_buckets`, publicly accessible RDS instances
- Privilege escalation enabled — containers configured with `allowPrivilegeEscalation: true`
- Credential exposure — plaintext credentials or access keys embedded in Terraform / CloudFormation / Helm templates
- Detect open security groups (`0.0.0.0/0` ingress on SSH/RDP/HTTP)
- Detect missing encryption on storage resources
- Flag hardcoded secrets in IaC templates before deployment

### SAST (Static Application Security Testing)
- Identify vulnerabilities in proprietary source code early in the development phase
- Detect injection flaws, insecure deserialization, hardcoded credentials, and broken authentication in code
- Integrate scan results into developer workflow via CI/CD pipeline gates

### DAST (Dynamic Application Security Testing)
- Authenticated scanning — test endpoints that require login, MFA-protected APIs
- Non-authenticated scanning — test publicly exposed surfaces
- XSS detection and mitigation validation
- Detect runtime vulnerabilities that only manifest during application execution

### SCA (Software Composition Analysis)
- Identify vulnerable open-source dependencies and third-party libraries
- Track which versions of a library are in use and flag unpatched versions
- Detect license compliance risks in open-source components
- Protect against supply chain attacks by monitoring OSS component integrity

### Secret Scanning
- Detect secrets in CI/CD pipeline configurations
- Scan code repositories for hardcoded credentials, API keys, tokens
- Scan container images for embedded secrets
- Scan Kubernetes ConfigMaps and manifest files for exposed credentials
- Scan S3 buckets and file systems for sensitive data at rest

### EPSS-Based Prioritization
- Use Exploit Prediction Scoring System (EPSS) scores to rank findings by actual exploitability
- Filter out unexploitable CVEs from the actionable queue
- Combine EPSS with runtime context (is the vulnerable component actually running?) for further noise reduction

### Rules Engine & Automated Ticket Creation
- Define custom rules that trigger automated ticket creation in Jira or other ITSM tools
- Route findings by severity, team, or asset to the right owner automatically
- Track finding lifecycle: open → triaged → remediated

### Vulnerability Management
- Unified findings dashboard across all scan types
- Triage workflow: review, suppress, accept risk, or remediate
- Track remediation status and SLA compliance
- MTTR reduction by unifying context from code to cloud

---

## Features

### Core Scanning Capabilities
| Feature | Description |
|---|---|
| SAST | Static code analysis — detect flaws in proprietary code |
| SCA | Software composition analysis — OSS dependency vulnerability detection |
| DAST | Dynamic testing — authenticated and unauthenticated endpoint scanning |
| IaC Scanning | Terraform, Helm, CloudFormation, and Kubernetes manifest misconfiguration detection |
| Container Scanning | Registry and CI/CD pipeline image vulnerability and secret scanning |
| Secret Scanning | Detect secrets in repos, images, S3, ConfigMaps, CI/CD pipeline configs |
| EPSS Scoring | Exploit Prediction Scoring System for prioritizing exploitable findings |
| Rules Engine | Automated ticket creation on policy violations with routing logic |

### CI/CD Pipeline Integration
| Feature | Description |
|---|---|
| GitHub Actions Integration | AccuKnox Container Scan + AccuKnox IaC available on GitHub Marketplace |
| Jenkins Integration | Plugin-based container scan and IaC integration |
| GitLab CI/CD | Native integration support |
| Azure DevOps | Native integration support |
| Pipeline Gates | Block builds on policy violations; fail pipelines for critical findings |
| Auto Label + Token Setup | Settings → Labels → Create; Settings → Tokens → Create; configure as CI/CD secrets |

### Findings Management
| Feature | Description |
|---|---|
| Findings Dashboard | Centralized view with Container Image Findings, IaC Findings, SAST Findings, Secret Findings |
| Registry Scan Page | View findings by registry and image |
| Finding Detail Drill-down | Click any finding for CVE detail, affected component, fix recommendation |
| Triage Workflow | Review / Suppress / Accept Risk / Remediate with lifecycle tracking |
| MTTR Tracking | Measure time from detection to remediation |

### Reporting
| Feature | Description |
|---|---|
| Scheduled Reports | Automated PDF/email reports on a schedule |
| On-Demand Reports | Trigger report generation at any time |
| Compliance Reports | Map findings to DevSecOps maturity frameworks |

---

## Dashboard & UI Flows

### Onboarding / Setup
1. **Generate Label:** Settings → Labels → Create → copy label string
2. **Generate API Token:** Settings → Tokens → Create → copy token
3. **Configure Secrets in CI/CD:** Add `ACCUKNOX_LABEL`, `ACCUKNOX_TOKEN`, and `ACCUKNOX_ENDPOINT` as secrets in GitHub / Jenkins / GitLab

### GitHub Actions — Container Scan
1. Open repository → navigate to `.github/workflows/your-workflow.yml`
2. After the build step, add the AccuKnox Container Scan GitHub Action
3. Push changes to trigger workflow, or manually run from Actions tab
4. Review findings: AccuKnox dashboard → Issues → Findings → Container Image Findings
5. Click any finding for detailed CVE information and remediation guidance

### GitHub Actions — IaC Scan
1. Open repository → navigate to `.github/workflows/your-workflow.yml`
2. After the build step, add the AccuKnox IaC scan GitHub Action
3. Push changes to trigger workflow
4. Review findings: AccuKnox → Findings → IaC Findings → click finding → arrow icon for detail

### Jenkins — Container Scan
1. Manage Jenkins → Plugins → Advanced Settings → Upload & install AccuKnox plugin
2. Open Jenkins job → Add build step → Select "Scan image with AccuKnox" → fill required details
3. Trigger job; view results in AccuKnox → Issues → Registry Scan page

### Findings Navigation
- **Registry Scan page:** Issues → Registry Scan — shows findings grouped by registry and image
- **Findings page:** Issues → Findings → select "Container Image Findings" from dropdown
- **IaC Findings page:** Issues → Findings → select "IaC Findings" from dropdown
- **SAST/DAST/Secret Findings:** Same Findings page with scan type filter applied

---

## AccuKnox Differentiators

| Differentiator | Detail |
|---|---|
| Multi-tool parser flexibility | Integrates open-source and commercial scanning tools via built-in parsers — not locked to a single vendor |
| Composite security posture | Normalizes and correlates findings from multiple tools into one risk score |
| Runtime context for static findings | Understands which vulnerable components are actually running — deprioritizes unexploitable CVEs |
| Code-to-cloud continuity | Single platform from SAST/SCA → IaC → Container Scan → Runtime (KubeArmor) |
| GitHub Actions in Marketplace | AccuKnox Container Scan and IaC actions are published and usable directly from GitHub Marketplace |
| Zero Trust integration | ASPM signals feed runtime policy enforcement via KubeArmor for closed-loop security |
| Pipeline-first approach | No IDE lock-in — enforces security centrally at the CI/CD level |
| No single-tool dependency | Removes scope limitations of individual tools; brings contextual understanding across the full stack |
| EPSS-based prioritization | Focuses teams on the 5 findings that can actually cause damage out of 10,000 alerts |

---

## Integrations

### CI/CD Platforms
- GitHub Actions (AccuKnox Container Scan, AccuKnox IaC — GitHub Marketplace)
- Jenkins (plugin-based)
- GitLab CI/CD
- Azure DevOps
- Others — see CI/CD Support Matrix

### Scanning Tools (supported via parsers)
- Trivy (container and OS vulnerability scanning)
- Checkov (IaC scanning — Terraform, CloudFormation, Helm, Kubernetes)
- tfsec (Terraform security scanning)
- Semgrep (SAST)
- OWASP ZAP (DAST)
- TruffleHog (secret scanning)
- Gitleaks (secret scanning)
- Grype (container vulnerability)
- Snyk (optional commercial integration)

### Ticketing / ITSM
- Jira (auto-ticket on finding with asset ID + severity)
- Freshservice
- ConnectWise
- ServiceNow

### Alerting / Notification
- Slack
- Email (SMTP)
- Webhooks (generic)
- PagerDuty

### SIEM
- Splunk (log forwarding)
- ELK / Elasticsearch (log forwarding)

### Cloud Storage / Registry
- Amazon ECR
- Azure Container Registry (ACR)
- Google Artifact Registry / GCR
- Harbor
- Generic container registries

---

## Onboarding

### Prerequisites
- AccuKnox account with access to Settings
- CI/CD pipeline (GitHub Actions, Jenkins, GitLab, or Azure DevOps)
- Container registry (optional — for registry-based scanning)
- API Label and Token from AccuKnox console

### Steps
1. Log into AccuKnox → Settings → Labels → Create → copy label
2. Settings → Tokens → Create → copy token
3. Add `ACCUKNOX_LABEL`, `ACCUKNOX_TOKEN`, `ACCUKNOX_ENDPOINT` as secrets in your CI/CD tool
4. Add AccuKnox scanning action/plugin to your pipeline workflow file
5. Push or trigger the pipeline run
6. Open AccuKnox dashboard → Issues → Findings → select scan type → review results
7. Triage findings: suppress, accept risk, or create remediation ticket
8. Configure rules engine for automated ticket routing (optional)
9. Set up scheduled reports for stakeholder distribution (optional)

### Deployment Options
- SaaS (AccuKnox-hosted) — fastest onboarding, no infrastructure required
- On-Premises — self-managed, air-gapped environments supported

---

## Compliance Frameworks Supported

- PCI-DSS
- HIPAA
- SOC 2 Type II
- NIST 800-53
- CIS Benchmarks
- GDPR
- ISO 27001
- FedRAMP
- OWASP Top 10 (for SAST/DAST findings mapping)
- DevSecOps maturity frameworks

---

## Diagrams

### 1. SDLC Pipeline Security Map
- Stages: Code → Build → Test → Deploy → Runtime
- At Code: SAST, SCA, Secret Scanning
- At Build: Container Scanning, IaC Scanning, Pipeline Gates
- At Test: DAST (authenticated + unauthenticated)
- At Deploy: Policy-as-Code checks, IaC validation
- At Runtime: KubeArmor enforcement, drift detection, runtime context feedback

### 2. Findings Funnel (Noise Reduction)
- Input: 10,000 raw findings across tools
- Filter 1: EPSS scoring — remove low-exploitability CVEs
- Filter 2: Runtime context — remove findings where component is not running
- Filter 3: Deduplication across tools
- Output: 5 actionable critical findings requiring immediate attention

### 3. Tool Integration Architecture
- AccuKnox as central aggregator
- Inbound: Trivy, Semgrep, Checkov, ZAP, TruffleHog, Gitleaks via parsers
- Outbound: Jira tickets, Slack alerts, SIEM events, compliance reports

### 4. GitHub Actions Workflow
- Developer pushes PR → GitHub Actions triggers → AccuKnox Container Scan runs → findings appear in AccuKnox dashboard → notification sent to team → developer sees result in PR

### 5. ASPM Component Map
- Grid: Scan Type (Container / IaC / SAST / DAST / Secrets) × Use Case (Supply chain / Misconfig / Auth vuln / Sensitive data / Runtime drift)

---

## Important Links & Resources

| Resource | URL |
|---|---|
| ASPM Overview (Help) | https://help.accuknox.com/how-to/aspm-overview/ |
| CI/CD Support Matrix | https://help.accuknox.com/support-matrix/cicd-support-matrix/ |
| CI/CD Integrations | https://help.accuknox.com/integrations/cicd-overview/ |
| DevSecOps Page | https://help.accuknox.com/getting-started/devsecops/ |
| IaC Scan Use Case | https://help.accuknox.com/use-cases/iac-scan/ |
| Container Scan Use Case | https://help.accuknox.com/use-cases/container-scan/ |
| SAST Use Case | https://help.accuknox.com/use-cases/sast-sq/ |
| Vulnerability Management | https://help.accuknox.com/use-cases/vulnerability/ |
| DAST (MFA-Enabled) | https://help.accuknox.com/use-cases/mfa-dast/ |
| DAST XSS Mitigation | https://help.accuknox.com/use-cases/dast-xss/ |
| Secret Scan in CI/CD | https://help.accuknox.com/use-cases/secret-scan-cicd-aws/ |
| Secrets in Code Repos | https://help.accuknox.com/use-cases/aspm/ |
| Secrets in S3 / File Systems | https://help.accuknox.com/use-cases/cloud/aws-storage/ |
| EPSS Scoring Use Case | https://help.accuknox.com/use-cases/epss-scoring/ |
| Rules Engine & Ticket Creation | https://help.accuknox.com/use-cases/rules-engine-ticket-creation/ |
| SCA Solution | https://www.accuknox.com/solutions/software-composition-analysis |
| Secrets in Container Images (Demo) | https://app.storylane.io/share/hmt8tl3ovppy |
| Secrets in K8s ConfigMaps (Demo) | https://app.storylane.io/share/2iw7zsxwougy |
| Azure IaC Integration | https://help.accuknox.com/integrations/azure-iac/ |
| GitHub Action: Container Scan | https://github.com/marketplace/actions/accuknox-container-scan |
| GitHub Action: IaC | https://github.com/marketplace/actions/accuknox-iac |
| ASPM Definitive Guide (eBook) | https://accuknox.com/ebooks/application-security-posture-management-definitive-guide |
| Top 5 Critical CVEs Video | https://www.youtube.com/watch?v=fK7tUKpmC90 |
| Top 8 ASPM Tools (Blog) | https://accuknox.com/blog/aspm-tools |
| Application Security Tools (Blog) | https://accuknox.com/blog/application-security-tools |
