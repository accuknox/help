# CWPP — Cloud Workload Protection Platform

---

## Definition

A Cloud Workload Protection Platform (CWPP) safeguards workloads running in cloud environments regardless of the underlying technology — containers, virtual machines, bare metal, and serverless functions. CWPP focuses on runtime threat detection, vulnerability management, and enforcing security policies at the workload level. AccuKnox CWPP is built on KubeArmor, a CNCF sandbox project that uses eBPF and Linux Security Modules (LSMs) to provide kernel-level inline mitigation — stopping attacks before execution rather than responding after.

---

## Pain Points

- Traditional security tools cannot protect ephemeral, short-lived workloads — containers spin up and disappear faster than agent-based tools can onboard
- Runtime attacks (process injection, privilege escalation, container breakout) are not detected until after damage is done
- Post-attack mitigation tools create a false sense of security — the attacker has already executed code, possibly disabled security controls, accessed logs, or exfiltrated data before the process is killed
- Vulnerability exploitation in container images or serverless code goes undetected without continuous runtime monitoring
- Difficulty tracking workload activity across multi-cloud and hybrid environments — no unified visibility
- Remote code execution via compromised application pods — attacker gains foothold in pod and moves laterally
- Unauthorized process execution from `/tmp` folders bypasses traditional monitoring
- Access to environment variables (API keys, secrets) from within containers is uncontrolled
- Filesystem tampering operations (mount, nsenter, fsck, lsblk) executed from within containers
- Crypto-mining processes execute silently inside workloads, consuming cluster resources
- Package management tools (apt, dnf, yum) abused at runtime to install malicious binaries
- Container management tools (docker, crictl, kubectl) executed from inside containers — enables container escape
- Network scanning tools (nmap, masscan) running from inside containers — reconnaissance phase of attack
- Penetration testing tools executed from within production containers
- Trusted root certificates tampered or replaced — enables man-in-the-middle attacks
- HashiCorp Vault and on-prem secrets managers accessed without authorization
- Lateral movement between workloads enabled by flat network topology
- Alert fatigue from post-detection engines that generate high volumes of low-signal alerts
- No behavioral baseline — impossible to distinguish normal from anomalous workload activity
- Multi-tenant deployment risks — workload isolation failures in shared environments

---

## Use Cases

### Runtime Threat Detection & Protection

**File Integrity Monitoring (FIM)**
- Block updates to system `/bin` or `/boot` folders — violation logged as "Permission Denied"
- Protect trusted root certificate stores and certificate bundle directories (`*cert*`, `*ca*`, `*bundle*`) from tampering or deletion
- Monitor critical file paths for unauthorized read, write, or delete operations

**Process Execution Control**
- Flag and block process executions from `/tmp` folder
- Detect anomalous process executions outside the discovered behavioral baseline
- Block execution of known crypto-mining binaries and processes at runtime
- Prevent unauthorized access to environment variables
- Audit use of package management tools at runtime (apt, dnf, yum) — log all invocations
- Prevent container management tools (docker, crictl, kubectl) from being used within containers
- Prevent network scanning tools (masscan, nmap) from executing within containers
- Prevent reconnaissance and penetration testing tools from running inside containers
- Classify process executions: interactive terminal vs background/system processes

**Filesystem Operations**
- Prevent or audit filesystem-related operations (mount, nsenter, fsck, lsblk) based on policy
- Block container escape attempts via filesystem operations

**Secrets Protection**
- Protect HashiCorp Vault on-prem secrets manager — block unauthorized access and interactions at runtime
- Block access to environment variables containing sensitive credentials

**Zero Trust Process Execution**
- Process Whitelisting: only explicitly allow-listed processes permitted to execute under Zero Trust model
- All other processes blocked and reported in AccuKnox Control Plane

**Network — Nano Segmentation**
- Only trusted processes allowed to initiate or handle network communication
- Dynamically identify trusted processes from observed application behavior
- Block unauthorized process-to-network connections at runtime

### Application Behavior Monitoring
- Discover behavior of workloads in public cloud, private cloud, on-prem VMs/BareMetal, and Kubernetes
- Auto-detect and recommend behavioral policies based on app observability
- Monitor: file systems, processes, and networks that are granted access
- Network Graph view: visualize pod-to-pod communication and process-level network activity
- List view: filter by cluster, namespace, or workload; tabs for network, file, and process activity

### Application Microsegmentation
- Microsegmentation via pod-level isolation, fine-grained control, and application-aware policies
- Detect which specific process requires network access — careful whitelisting
- Derive network understanding from CNI (agnostic to CNI type) to construct L3, L4, and L7 layers
- Isolate workloads and protect against lateral movement or unauthorized access

### Zero Trust Policy Management

**Auto-Discovered Zero Trust Policy**
- Policies automatically generated based on compliance frameworks: MITRE, NIST, PCI-DSS, CIS
- System suggests hardening policies — reduce attack surface based on behavioral observation
- Whitelist detected behavior; block everything else

**Custom Zero Trust Policy**
- Policy Editor Tool — personalize policy creation per workload
- Fine-grained control: observe/audit mode or enforce mode
- Allow/block specific process executions, file access, and network connections

**Inline Remediation**
- Declarative policy enforced at runtime against attacks like APT vulnerabilities and Log4j
- Maintain application uptime while enforcing Zero Trust posture
- Contrast: inline mitigation blocks attack before execution; post-exploit kills process after damage

### App Hardening
- Readymade hardening policies based on CIS, MITRE, NIST-800-53, and STIGs
- Block-based recommendations — reduce attack surface via deny-by-default
- Auto-recommendations to the cluster — customizable
- All violations blocked with inline mitigation approach
- Tweak and create custom policies using the policy editor
- Activate framework-specific hardening policies: Runtime Protection → Policies → Hardening → Activate

### Container Registry Scanning & Vulnerability Management
- Onboard container image registries (ECR, ACR, GCR, Harbor, generic)
- Configure scan schedule, image filter (regex, update date, pull date)
- Scan images for CVEs across all layers
- View findings grouped by registry and image
- View vulnerability findings in the context of Kubernetes clusters, namespaces, and workloads
- Alert on new critical vulnerability detection — send to email, notification, webhook
- Triage findings lifecycle: review, suppress, accept risk, remediate
- Inventory of container images: Inventory → Cloud Assets → filter by Container

### Pod Security Admission (PSA)
- Enforce security standards at pod admission time
- PSA Levels: Privileged (unrestricted) / Baseline (minimally restrictive) / Restricted (heavily hardened)
- PSA Modes: enforce (reject non-compliant pods) / audit (allow but alert)
- Dry Run mode: preview enforcement effects before applying
- Integrate with Kubernetes native Pod Security Standards

### GitOps & Policy Lifecycle
- Apply policies via CLI, AccuKnox Control Plane, or GitOps workflows
- Policy changes versioned and reflected consistently across environment
- Maintain policy-as-code alongside application code in version control

### Forensics & Compliance
- All audit and block events centrally visible in AccuKnox Control Plane
- Events clearly indicate policy action taken (audit or block)
- Audit or block events trigger configurable actions and forward to notification channels
- Map violations to MITRE ATT&CK framework
- NIST 800-53 control mapping for audit readiness
- CIS benchmark scan and compliance reporting
- Scheduled and on-demand PDF reports

---

## Features

### Core Runtime Engine
| Feature | Technology | Description |
|---|---|---|
| eBPF-based enforcement | eBPF + BPF-LSM | Kernel-level visibility and enforcement without kernel source changes |
| LSM enforcement | AppArmor, BPF-LSM, SELinux | Best-of-breed Linux Security Modules for inline mitigation |
| KubeArmor | CNCF sandbox project | Open-source runtime security enforcement system |
| Inline mitigation | Syscall-level blocking | Stops attacks before execution — not post-exploit |
| Non-privileged daemonset | KubeArmor | Monitors all pods/containers without being privileged itself |

### Policy Engine
| Feature | Description |
|---|---|
| Auto-policy discovery | Behavioral policies auto-generated from workload observation |
| Custom policy editor | Personalized rule creation per workload |
| Hardening policies | CIS, MITRE, NIST-800-53, STIGs — select and activate |
| Policy modes | Observe/Audit (alert only) / Enforce (block) |
| GitOps integration | Policy-as-code versioned in Git |
| Policy scopes | Pod-level, namespace-level, node/host-level |

### Workload Protection
| Feature | Description |
|---|---|
| Process execution control | Allowlist-based process execution; block everything else |
| File access control | Read/write/delete controls on specific paths |
| Network access control | Process-level network connection allowlisting |
| FIM | File Integrity Monitoring for critical system paths |
| Crypto-mining prevention | Block known mining binary execution |
| Container escape prevention | Block fsops, privilege escalation syscalls |
| Secrets protection | Block env variable access and secrets manager unauthorized access |

### Vulnerability Management
| Feature | Description |
|---|---|
| Registry scanning | Onboard multiple registries; scan on schedule or on-demand |
| Image filtering | Regex, update date, pull date filters |
| CVE detection | All layers of container image scanned |
| Workload context | Vulnerabilities shown in context of cluster/namespace/workload |
| Alerts | Critical CVE alerts via email, webhook, notification |
| Triage lifecycle | Review / Suppress / Accept Risk / Remediate |

### Visibility & Reporting
| Feature | Description |
|---|---|
| App Behavior Graph | Network graph of pod-to-pod communication + process-level traffic |
| App Behavior List | Filter by cluster/namespace/workload; network/file/process tabs |
| CWPP Dashboard | Per-cluster comprehensive posture view |
| Alerts Dashboard | All policy violations — audit and block — with custom filter |
| Scheduled Reports | Automated PDF CWPP reports |
| On-Demand Reports | Generate reports at any time |
| Audit Logs | Detailed event logs for forensic investigation |

---

## Dashboard & UI Flows

### Cluster Onboarding (Agent-Based)
1. Settings → Manage Cluster → "Onboard Now"
2. Provide a name for the cluster
3. Install agents via commands displayed on screen (KubeArmor DaemonSet via kubectl)
4. Inventory → Clusters — confirm cluster appears in list
5. Click cluster → "View Workloads" — see all containers and pods

### Application Behavior — Graph View
1. Runtime Protection → App Behavior
2. Network Graph: visual representation of pod-to-pod network communication
3. Process-level network activity overlaid on graph
4. Click on a workload to see detailed activity

### Application Behavior — List View
1. Runtime Protection → App Behavior
2. Switch to List view
3. Filter by specific cluster, namespace, or workload
4. Tabs: Network activity / File access / Process execution
5. Data shows observed real-time and historical behavior

### Policies — Discovered (Zero Trust Journey)
1. Runtime Protection → Policies → Discovered tab
2. Policies auto-generated from observed application behavior
3. Each policy whitelists detected behavior (file paths, process names, network connections)
4. Applied in audit/learning mode by default — alerts for violations, no blocking
5. "Changes Available" — update policy as application changes
6. When no deviation detected → policy marked "Stable"
7. When stable → enforce in Block mode:
   - Inventory → Clusters → View Workloads → cog icon → set KubeArmor posture to Block
8. When application updates → change back to Audit to learn new behavior

### Policies — Hardening
1. Runtime Protection → Policies → Hardening tab
2. Framework-based hardening policies displayed (MITRE, CIS, NIST)
3. Select policy → click "Activate"
4. Policy enforced — violations blocked with inline mitigation

### Pod Security Admission (PSA)
1. Inventory → Clusters → click cluster → View Workloads
2. Click cog icon next to namespace
3. Select Level: Privileged / Baseline / Restricted
4. Select Mode: enforce / audit
5. Click "Dry Run" — preview effects before enforcing
6. Save — enforcement applies at pod admission time

### Alerts & Violation Logs
1. Monitors/Alerts → Alerts
2. All policy violation alerts visible — audit events and block events
3. Each event shows: policy action taken (audit/block), workload, violation detail
4. Custom filtering available — save filter views for recurring use

### CWPP Dashboard (Post-Policy View)
1. Runtime Protection → CWPP Dashboard
2. Select cluster
3. View: applied policies, violation counts, threat timeline, compliance status
4. Comprehensive posture view after policies have been applied

### Container Registry Scanning Onboarding
1. Settings → Integrations → Registry tab
2. Click "Add Registry"
3. Input Name, Description, Registry Type
4. Provide Auth Credentials per registry type
5. Optional configuration:
   - Images to scan: by Regex, Update Date, or Pull Date filter
   - Scan schedule
6. Click "Test Connection" → Save
7. Issues → Registry Scan — view scanned registries
8. Click any image → view detailed scan results

### Container Image Findings Navigation
1. Issues → Registry Scan — grouped view by registry and image
2. Issues → Findings → filter "Container Image Findings" from dropdown
3. Inventory → Cloud Assets → filter Asset Type as "Container" — all scanned images and associated findings

---

## AccuKnox Differentiators

| Differentiator | Detail |
|---|---|
| Inline mitigation — pre-execution blocking | BPF-LSM stops attack at syscall level before execution completes — no damage |
| Zero false positives | Allowlist-based policy — anything not explicitly permitted is blocked |
| eBPF without kernel modifications | Modern workload protection without requiring changes to kernel source code |
| Open-source KubeArmor (CNCF sandbox) | Community-validated, transparent security engine |
| Reduced alert fatigue | Inline blocking stops attacks silently — no noisy post-exploit alert storms |
| CNI-agnostic microsegmentation | Works with any Container Network Interface — Calico, Cilium, Flannel, etc. |
| Auto-policy discovery | No manual policy writing — behavioral learning generates precise allowlists |
| Multi-environment single agent | Kubernetes + VM (systemd) + BareMetal + IoT/Edge (ARM/x86) |
| NIST/Gartner-aligned Zero Trust | Documented alignment with NIST ZT guidelines and Gartner recommendations |
| Non-privileged daemonset | KubeArmor monitors workloads without requiring privileged container access |
| LSM abstraction across node types | Single policy abstraction works across nodes using AppArmor, BPF-LSM, or SELinux |
| Proactive + inline + adaptive | Anticipates attacks, enforces inline, adapts policies as applications evolve |

---

## Inline Mitigation vs Post-Attack Mitigation

| Aspect | Post-Attack Mitigation | AccuKnox Inline Mitigation |
|---|---|---|
| When does blocking happen? | After malicious process executes | Before malicious process executes |
| Attacker can execute binary? | Yes | No |
| Risk of disabling security controls | Yes — attacker can disable monitoring | No — blocked before any action |
| Risk of data exfiltration | Yes — attacker may transmit before kill | No — process never runs |
| Risk of log tampering | Yes — attacker may clear logs | No — process never runs |
| Performance impact | Kill signal after execution | Kernel-level LSM — minimal overhead |
| Enforcement mechanism | Process kill signal | BPF-LSM / AppArmor / SELinux syscall block |

---

## Supported Environments

| Environment Type | Specifics |
|---|---|
| Kubernetes (cloud-managed) | EKS (AWS), AKS (Azure), GKE (GCP) |
| Kubernetes (on-prem) | Robin Clusters, Kubeadm, OpenShift, Rancher |
| Kubernetes (edge) | K3s, MicroK8s, lightweight edge distributions |
| Containers (non-orchestrated) | Docker, Containerd, CRIO, Podman, ECS |
| Virtual Machines | KVM, VMware, Hyper-V — any hypervisor |
| Bare Metal | Direct physical node deployment |
| IoT / Edge | ARM 32/64-bit, x86 — lightweight footprint |

---

## Integrations

### Container Runtimes
- Docker
- Containerd
- CRIO
- Podman
- ECS (containers on VM)

### Container Registries
- Amazon ECR (AWS)
- Azure Container Registry (ACR)
- Google Artifact Registry / GCR
- Harbor
- Generic container registries (any registry with auth credentials)
- Filter by: Regex, Update Date, Pull Date

### Policy / GitOps
- `knoxctl` CLI
- AccuKnox Control Plane UI
- GitOps workflows (version-controlled policy-as-code)
- Kubernetes CRDs: `KubeArmorPolicy`, `KubeArmorHostPolicy`

### Ticketing / ITSM
- Jira
- ServiceNow (SNOW table API)
- Freshservice
- ConnectWise

### Alerting / Notification
- Slack
- Email (SMTP)
- Webhooks (generic endpoint)
- PagerDuty

### SIEM
- Splunk (log forwarding)
- ELK / Elasticsearch (log forwarding)

---

## Onboarding

### Prerequisites — Agent-Based
- Kubernetes cluster (any supported distribution)
- `kubectl` access with cluster-admin permissions for DaemonSet deployment
- AccuKnox account with cluster management access
- Network connectivity between cluster nodes and AccuKnox Control Plane (SaaS or on-prem)

### Prerequisites — On-Prem / Air-Gapped
- 1 VM: ≥16 vCPUs, ≥64 GB RAM, ≥512 GB disk (256 GB allocated to `/var`)
- AccuKnox provides licensed installation tgz (~20 GB)
- No external network connectivity required during installation

### Steps — Agent-Based
1. Settings → Manage Cluster → "Onboard Now"
2. Name the cluster
3. Run agent installation commands (KubeArmor DaemonSet)
4. Inventory → Clusters → verify cluster is listed
5. View Workloads → confirm pods and containers appear
6. Runtime Protection → App Behavior → review network graph and list view
7. Runtime Protection → Policies → Discovered → review auto-generated behavioral policies
8. Begin Zero Trust Journey: audit mode → stable → block mode

### Steps — Container Registry Scanning
1. Settings → Integrations → Registry tab → "Add Registry"
2. Input Name, Description, Registry Type, Auth Credentials
3. Configure scan filters (regex, update date, pull date) and schedule (optional)
4. Test Connection → Save
5. Issues → Registry Scan → view results
6. Issues → Findings → Container Image Findings for unified findings view

---

## Pricing

Pricing is based on:
- Number of nodes (CWPP nodes)
- Deployment environment (cloud vs. on-prem)
- Modules selected: CWPP-only, or full CNAPP bundle (CWPP + KSPM + CSPM + ASPM)
- Flexible licensing — purchase CWPP independently or as part of CNAPP

Custom quote: https://accuknox.com/pricing

---

## Diagrams

### 1. eBPF / BPF-LSM Architecture
- Workload process issues syscall → eBPF probe at kernel boundary intercepts → BPF-LSM policy evaluated → Allow (continue execution) or Block (syscall rejected, violation logged)
- AppArmor and SELinux shown as alternative LSM backends on different node types
- KubeArmor abstracts LSM complexity — single policy format across all node types

### 2. CWPP Platform Architecture
- KubeArmor DaemonSet on each node → collects telemetry and enforces policies
- Feeder Service → collects feeds from KubeArmor, relays to Control Plane
- Shared Informer Agent → collects cluster metadata (pods, nodes, namespaces)
- Policy Discovery Engine → uses workload + cluster info to generate behavioral policies
- AccuKnox Control Plane → unified dashboard, policy management, alerts, reports

### 3. Inline vs Post-Attack Comparison
- Left side (Post-attack): Attack → Process executes → Alert fires → Process killed → Damage already done
- Right side (AccuKnox inline): Attack attempt → BPF-LSM blocks syscall → Violation logged → Zero execution, zero damage

### 4. Zero Trust Journey (4 Phases)
- Phase 1 Learn: KubeArmor observes workload behavior, no blocking
- Phase 2 Audit: Policies applied in audit mode — violations alerted, not blocked
- Phase 3 Stable: Policies show no deviation for defined period → marked Stable
- Phase 4 Enforce: KubeArmor posture set to Block — only allowlisted actions permitted

### 5. App Behavior Network Graph
- Nodes: pods/workloads in the cluster
- Edges: observed network connections between pods
- Edge color/weight: traffic volume and policy status (allowed/blocked)
- Drill-down: click node → see process-level network and file activity

### 6. Microsegmentation Visual
- Pod A (web app) → allowed → Pod B (API service) on port 8080
- Pod A → blocked → Pod C (database) on port 5432 (not in policy)
- External IP → blocked → Pod B (no external ingress in policy)
- L3/L4/L7 policy layers labeled

### 7. Multi-Environment Workload Protection
- Single AccuKnox agent works across:
  - Kubernetes pod (DaemonSet mode)
  - VM (systemd mode)
  - Bare Metal (systemd mode)
  - IoT/Edge device (lightweight ARM binary)
- All workloads report to unified AccuKnox Control Plane

### 8. CNAPP Consolidation
- Before AccuKnox: separate tools for runtime security, container scanning, network segmentation, compliance, alerting — all siloed
- After AccuKnox: single CNAPP platform consolidating CWPP + KSPM + CSPM + ASPM

---

## Important Links & Resources

| Resource | URL |
|---|---|
| CWPP Overview | https://help.accuknox.com/overview/what-is-cwpp/ |
| App Behavior | https://help.accuknox.com/saas/app-behavior/ |
| Network Segmentation | https://help.accuknox.com/use-cases/cards/Network-Segmentation/ |
| Zero Trust Use Case | https://help.accuknox.com/use-cases/zero-trust/ |
| CNAPP Security Overview | https://help.accuknox.com/use-cases/cnapp-security-overview/ |
| Cluster Onboarding | https://help.accuknox.com/how-to/cluster-onboarding/ |
| Runtime Security Architecture | https://help.accuknox.com/getting-started/runtime-sec-arch/ |
| AccuKnox Agents Overview | https://help.accuknox.com/getting-started/accuknox-agents/ |
| On-Prem Single Node Installation | https://help.accuknox.com/getting-started/on-prem-single-node-installation/ |
| KubeArmor Differentiation | https://docs.kubearmor.io/kubearmor/quick-links/differentiation |
| KubeArmor GitHub | https://github.com/kubearmor/KubeArmor |
| CWPP eBook | https://accuknox.com/ebooks/accuknox-cloud-workload-protection-platform-cwpp-an-inside-look |
| CrushFTP CVE Exploitation Demo | https://www.youtube.com/watch?v=3uhBXc71-U0 |
| Enterprise ZT Automation Demo | https://www.youtube.com/watch?v=lxq5sLNFj9w |
| Role of CWPP (Blog) | https://accuknox.com/blog/role-of-cwpp-in-modern-cloud-security |
| Micro-segmentation (Blog) | https://accuknox.com/blog/micro-segmentation |
| DVWA Demo | https://help.accuknox.com/getting-started/dvwa/ |
| PHP/MySQL Demo | https://help.accuknox.com/getting-started/php-mysql/ |
| WordPress/MySQL Demo | https://help.accuknox.com/getting-started/wordpress-mysql/ |
| Pricing | https://accuknox.com/pricing |
