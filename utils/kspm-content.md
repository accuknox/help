# KSPM — Kubernetes Security Posture Management

---

## Definition

Kubernetes Security Posture Management (KSPM) is designed to help teams manage and secure Kubernetes environments by continuously scanning cluster configurations, workloads, and RBAC policies. It ensures Kubernetes clusters are compliant, hardened, and protected — whether deployed in the cloud, on-prem, or at the edge. AccuKnox KSPM combines static posture insights with runtime enforcement to provide protection from cluster configuration all the way down to the pod and process level.

---

## Key Statistics

- Over 78% of organizations use Kubernetes
- Over 62% of Kubernetes deployments are severely misconfigured or unsecured
- Top security risks: misconfigurations, vulnerable containers, and insider threats
- Kubernetes has a large attack surface — vulnerabilities can lead to data breaches, outages, and compliance violations

---

## Pain Points

- Flat network topology and dynamic IP allocation make network segmentation extremely complex — any compromised pod can laterally access other pods and nodes
- Cryptojacking malware spreads between pods to mine cryptocurrency using cluster resources
- Misconfigured cluster roles and namespaces allow unauthorized access
- Excessive RBAC permissions — over-permissioned service accounts — expand blast radius significantly
- Unsecured workloads and open network paths between namespaces
- Limited visibility into dynamic, short-lived pods that spin up and disappear within seconds
- Unauthorized process execution from `/tmp` folders within containers
- Containers configured with `allowPrivilegeEscalation: true` — privilege escalation risk
- Container management tools (docker, crictl, kubectl) abused from inside containers
- Penetration testing and reconnaissance tools (nmap, masscan) executing from within containers
- Workloads missing CPU and memory limits — resource exhaustion attacks possible
- Secrets and credentials embedded in Kubernetes manifests and ConfigMap files
- Service accounts configured with anonymous access
- Privileged containers running in production clusters
- Writable hostPath volumes allow container escape to host filesystem
- Users, services, and namespaces with ClusterAdmin privileges beyond what is necessary
- TLS certificates misconfigured or expiring without detection
- No baseline for normal application behavior — impossible to detect anomalies without it
- No admission control — any image from any registry can be deployed
- RBAC drift — permission changes introduced manually through the console, not tracked

---

## Use Cases

### K8s Security Posture Management (KSPM)

**Misconfiguration Detection**
- Identify and flag security misconfigurations in Kubernetes cluster setup
- Detect: privileged containers, writable hostPath volumes, containers with `allowPrivilegeEscalation`
- Detect workloads/accounts with Host PID and IPC namespace privileges
- Identify external-facing workloads exposed without intended business justification
- Ensure CPU and memory limits are set across all workloads
- Identify secrets and credentials embedded in manifests and config files
- Identify service accounts configured with anonymous access

**CIS / STIGs Benchmarks**
- Automated scan of Kubernetes clusters against CIS Benchmarks
- Scan against NSA/CISA Kubernetes Hardening Guidance
- STIG benchmark scanning and reporting
- Compliance status per control — pass/fail with remediation guidance

**Admission Controller (KnoxGuard)**
- Pod Security Admission (PSA) support — enforce security standards at admission time
- Control container image deployment — allow only images from trusted registries
- PSA levels: Privileged / Baseline / Restricted
- PSA modes: enforce (reject non-compliant pods) / audit (allow but alert)
- Dry Run mode: preview effects of PSA enforcement before applying

**K8s Security Risk Assessment**
- Evaluate and prioritize security risks across all Kubernetes resources
- Risk scoring per cluster, namespace, workload
- Track which workloads are highest risk and why

**KIEM — Kubernetes Identity & Entitlements Management**
- Manage and audit unused service accounts
- Revoke excessive permissions automatically
- Identify users, services, and namespaces with ClusterAdmin or equivalent privileges
- Identify Kubernetes service accounts with elevated or excessive permissions
- Identify unused roles not mapped to any active workloads
- Identify subjects with permission to create roles and role bindings
- Track permission drifts in real time

**K8TLS — TLS Posture**
- Enforce TLS and certificate best practices across the cluster
- Detect expiring or misconfigured TLS certificates
- Open-source tool developed in-house by AccuKnox

### Runtime Security

**Container Runtime Protection**
- File Integrity Monitoring and Protection — block updates to system bin or boot folders; `Permission Denied` on violation
- Protect trusted root certificate stores and certificate bundle directories (`*cert*`, `*ca*`, `*bundle*`) from tampering
- Flag and block process executions from `/tmp` folder
- Detect anomalous process executions outside the discovered behavioral baseline
- Prevent crypto-mining binary or process execution at runtime
- Prevent unauthorized access to environment variables
- Audit use of package management tools at runtime (apt, dnf)
- Prevent container management tools (docker, crictl, kubectl) from being used within containers
- Prevent use of network scanning tools (masscan, nmap) from within containers
- Prevent or audit filesystem-related operations (mount, nsenter, fsck, lsblk)
- Prevent use of reconnaissance or penetration testing tools from inside containers
- Classify process executions: interactive terminal vs background/system

**Zero Trust Policy Enforcement**
- Process Whitelisting: Zero Trust execution model — only explicitly allow-listed processes permitted to execute
- Nano Segmentation: only trusted processes handle network communication; dynamically identified from observed application behavior
- Auto-discovered policies based on application runtime behavior — no manual policy writing required
- Custom Zero Trust policies via the Policy Editor Tool
- Policies applicable via CLI, AccuKnox Control Plane, or GitOps workflows
- Policy changes versioned and reflected consistently

**Workload Hardening**
- File Integrity Monitoring (FIM)
- Malware protection
- Secure sensitive assets such as root certificates
- Hardening policies based on MITRE ATT&CK, NIST 800-53, CIS, PCI-DSS
- Readymade hardening policies from AccuKnox — select and activate
- All violations blocked with inline mitigation approach

**K8s Network Microsegmentation**
- Automatically discover and suggest network policies for ingress and egress
- Derive network understanding from CNI (agnostic to CNI type) to construct L3, L4, and L7 layers of understanding
- Detect which specific process requires network access — careful allowlisting
- Ensure workload security by isolating workloads and protecting against lateral movement
- Nano segmentation: restrict traffic at process level, not just pod level

**Application Behavior Monitoring**
- Monitor file, process, and network activity per workload
- Workload network graph — visualize pod-to-pod communication
- List view: filter by cluster, namespace, or workload; tabs for network, file, and process activity
- Baseline normal behavior; flag deviations

**Auto Remediation & Preemptive Mitigation**
- Kill malicious processes automatically on detection
- Quarantine compromised pods
- Detailed audit logs for forensic investigations
- Map logs to MITRE ATT&CK framework

### Compliance

**Framework Mapping**
- CIS Kubernetes Benchmark
- MITRE ATT&CK framework mapping for policies and policy violations
- NIST 800-53 mapping — controls available for audit readiness
- NSA/CISA Kubernetes Hardening Guidance
- PCI-DSS
- HIPAA

**Vulnerability Scanning**
- Scan container images in the Kubernetes environment for CVEs
- Alert on new critical vulnerability detection (email, notifications, webhooks)
- Show vulnerabilities in the context of clusters, namespaces, and workloads
- Triage and handle findings lifecycle: review, suppress, accept risk, remediate
- Alert on new critical vulnerabilities with configurable notification channels

---

## Features

### KSPM (Posture Management)
| Feature | Mode | Description |
|---|---|---|
| K8s Misconfiguration Detection | Agentless / CronJob | Scan and flag K8s misconfigurations |
| CIS/STIGs Benchmarks | Agentless / CronJob | Benchmark compliance scanning |
| Admission Controller (KnoxGuard) | Agent-based | PSA enforcement at pod admission |
| K8s Security Risk Assessment | Agentless / CronJob | Risk prioritization across K8s resources |
| KIEM | Agentless | Identity and entitlement management |
| K8TLS | Agent-based | TLS posture and certificate enforcement |

### Runtime Security
| Feature | Mode | Description |
|---|---|---|
| KubeArmor Runtime Enforcement | Agent-based (eBPF) | Process, file, network policy enforcement at kernel level |
| Workload Hardening | Agent-based | FIM, malware protection, root cert security |
| Network Microsegmentation | Agent-based | L3/L4/L7 isolation, CNI-agnostic |
| App Behavior Monitoring | Agent-based | Graph + list view of workload activity |
| Zero Trust Policy | Agent-based | ZTNA + process whitelisting |
| Auto Remediation | Agent-based | Kill, quarantine, alert on threat |
| Pod Security Admission | Agent-based | Privileged/Baseline/Restricted × enforce/audit |
| Policy Discovery Engine | Agent-based | Auto-generate behavioral policies per workload |
| GitOps Policy Management | Any | CLI + UI + GitOps workflows |

### Threat Detection
| Threat | Detection Method |
|---|---|
| Privilege escalation attempts | Syscall-level monitoring |
| Container breakout | Process and filesystem policy enforcement |
| Cryptojacking | Block known crypto-mining binary execution |
| Hidden processes | Behavioral baseline deviation detection |
| Lateral movement | Network microsegmentation + policy enforcement |
| Command injection | File and process policy enforcement |

---

## Dashboard & UI Flows

### Agent-Based Cluster Onboarding
1. Settings → Manage Cluster → click "Onboard Now"
2. Provide a name for the cluster
3. Install agents via commands displayed on screen (KubeArmor DaemonSet)
4. Inventory → Clusters — verify cluster appears in the list
5. Click on the onboarded cluster → "View Workloads" — see containers and pods

### Application Behavior View
1. Runtime Protection → App Behavior
2. Network Graph view: visualize pod-to-pod communication + process-level network activity
3. List view: filter by cluster/namespace/workload → tabs for network, file access, process execution

### Policies — Discovered (Behavioral Whitelist)
1. Runtime Protection → Policies → Discovered tab
2. Auto-generated policies based on observed application behavior
3. Click any policy to view whitelisted behaviors (file paths, process names, network destinations)

### Zero Trust Journey (Audit → Stable → Block)
1. Discovered policies applied in learning/audit mode by default — alert only, no blocking
2. Review and update policy as needed by selecting "Changes Available"
3. When no deviation detected from the policy for a defined period → policy marked as "Stable"
4. When policy is stable → enforce in Block mode:
   - Inventory → Clusters → click cluster → View Workloads
   - Click cog icon next to namespace → set KubeArmor posture to "Block"
5. When application is updated → change posture back to Audit to learn new behavior

### Policies — Hardening
1. Runtime Protection → Policies → Hardening tab
2. Framework-based hardening policies (MITRE, CIS, NIST)
3. Select policy → click "Activate" to apply
4. Violations blocked with inline mitigation

### Pod Security Admission (PSA)
1. Inventory → Clusters → click cluster → View Workloads
2. Click cog icon next to namespace
3. Select Level: Privileged / Baseline / Restricted
4. Select Mode: enforce / audit
5. Click "Dry Run" to preview effects before enforcing
6. Apply — non-compliant pods rejected (enforce) or alerted (audit)

### Alerts & Violation Logs
1. Monitors/Alerts → Alerts
2. View all policy violation alerts: audit events and block events
3. Filter by cluster, namespace, workload, policy, severity
4. Save custom filter views for recurring use

### CWPP / Runtime Dashboard
1. Runtime Protection → CWPP Dashboard
2. Select cluster → comprehensive posture view with applied policies and alert history

### KIEM Navigation
1. Inventory → KIEM
2. View service accounts, role bindings, ClusterAdmin assignments
3. Filter unused roles, excessive permissions, anonymous access accounts
4. Take action: revoke, restrict, or flag for review

---

## AccuKnox Differentiators

| Differentiator | Detail |
|---|---|
| Inline mitigation — pre-execution | KubeArmor stops attacks at syscall level before execution completes — not post-exploit |
| eBPF + LSM (AppArmor/BPF-LSM/SELinux) | Kernel-level enforcement using Linux Security Modules — not application-layer hooks |
| Open-source KubeArmor (CNCF sandbox) | Community-validated, transparent, extensible |
| Patented micro-segmentation | Pod-level isolation using Linux primitives |
| Zero false positives | Policy-based allowlist — anything not in policy is blocked, no guessing |
| Multi-LSM abstraction | Works across nodes using different LSMs seamlessly — AppArmor + BPF-LSM + SELinux |
| Auto-policy discovery | Behavioral learning auto-generates policies — no manual policy writing required |
| 50 microservices protected under 1 hour | Fast time-to-value — enterprise-scale deployment speed |
| Multi-environment support | Single agent for K8s + VM + BareMetal + IoT/Edge |
| Inline vs post-attack differentiation | Post-exploit: attacker executes, then gets killed — too late. AccuKnox blocks before execution |
| K8TLS in-house TLS posture tool | Open-source TLS posture enforcement built and maintained by AccuKnox |
| KIEM | Kubernetes-native identity and entitlement management — not just RBAC visualization |
| Nano segmentation | Process-level network trust, not just pod-level microsegmentation |
| Agentless KSPM option | CronJob-based posture scanning — no persistent agent for static posture checks |

---

## Inline Mitigation vs Post-Attack Mitigation

| Method | What Happens |
|---|---|
| Post-attack mitigation | Attacker executes binary → security tool detects suspicious process → kills process → attacker may have already disabled security controls, accessed logs, deleted/encrypted/transmitted sensitive data |
| Inline mitigation (AccuKnox/KubeArmor) | Attack attempt → BPF-LSM / AppArmor policy blocks syscall → process never executes → violation logged and alerted → zero damage |

---

## Supported Environments

| Environment | Details |
|---|---|
| Kubernetes (cloud-managed) | EKS (AWS), AKS (Azure), GKE (GCP) |
| Kubernetes (on-prem/self-managed) | Robin Clusters, Kubeadm, OpenShift, Rancher |
| Kubernetes (edge) | K3s, MicroK8s, edge distributions |
| Containers (non-orchestrated) | Docker, Containerd, CRIO, Podman, ECS |
| Virtual Machines | Any hypervisor — KVM, VMware, Hyper-V |
| Bare Metal | Direct physical node deployment |
| IoT / Edge | ARM (32/64-bit), x86 — lightweight agent |

---

## Integrations

### Deployment & Agent Integration
- KubeArmor DaemonSet (Kubernetes)
- KubeArmor systemd mode (VMs and Bare Metal)
- Agentless CronJob mode (KSPM posture scanning)

### Policy / GitOps
- `knoxctl` CLI
- AccuKnox Control Plane UI
- GitOps workflows (policy-as-code, version-controlled)
- Kubernetes-native: `KubeArmorPolicy`, `KubeArmorHostPolicy` CRDs

### Container Registries
- Amazon ECR
- Azure Container Registry (ACR)
- Google Artifact Registry / GCR
- Harbor
- Generic registries

### Ticketing / ITSM
- Jira
- ServiceNow
- Freshservice

### Alerting / Notification
- Slack
- Email
- Webhooks
- PagerDuty

### SIEM
- Splunk
- ELK / Elasticsearch

### Compliance Tools
- OpenSCAP (integrated for compliance scanning)
- MITRE ATT&CK framework (mapping built in)

---

## Onboarding

### Agent-Based (Cloud or On-Prem K8s)
1. Settings → Manage Cluster → "Onboard Now"
2. Name the cluster
3. Run the agent installation commands shown on screen (DaemonSet deployment via kubectl)
4. Inventory → Clusters → confirm cluster appears
5. View Workloads → see pods and containers
6. Runtime Protection → App Behavior → review network graph
7. Runtime Protection → Policies → Discovered — review auto-generated behavioral policies
8. Begin Zero Trust Journey: audit → stable → block

### On-Prem / Air-Gapped Deployment
- Hardware: 1 VM, ≥16 vCPUs, ≥64 GB RAM, ≥512 GB disk (256 GB allocated to `/var`)
- AccuKnox provides a licensed installation tgz (~20 GB)
- No external network connectivity required during installation
- Reference: https://help.accuknox.com/getting-started/on-prem-single-node-installation/

### Agentless KSPM
- CronJob-based scanning deployed to cluster
- No persistent agent; scans run on schedule
- Supports EKS, AKS, GKE, and on-prem managed clusters

---

## Diagrams

### 1. eBPF / LSM Architecture
- Syscall issued by process → eBPF probe intercepts → BPF-LSM / AppArmor / SELinux policy evaluated → Allow or Block decision before execution
- Contrast with: Post-exploit (process executes → suspicious activity detected → process killed)

### 2. Kubernetes Attack Surface Map
- Cluster level: API server exposure, etcd access, control plane misconfiguration
- Namespace level: RBAC overprovisioning, missing network policies
- Pod level: privileged containers, writable hostPath, env variable exposure
- Container level: /tmp execution, crypto mining, container breakout
- Network level: lateral movement between pods, flat topology risk

### 3. Zero Trust Journey Timeline
- Phase 1 — Learning/Audit: observe workload behavior, generate policies, audit mode (alert only)
- Phase 2 — Stable: no deviations detected, policy marked stable
- Phase 3 — Enforce/Block: KubeArmor posture set to Block, violations rejected at syscall level

### 4. KIEM Visual
- Service Account → Role Binding → ClusterRole → Namespace / Cluster scope
- KIEM flags: unused accounts, excess permissions, ClusterAdmin assignments
- Actions: revoke, restrict, annotate for review

### 5. Multi-Environment Deployment
- Single KubeArmor agent runs across: Kubernetes pods → VMs (systemd mode) → Bare Metal → IoT/Edge (ARM/x86)
- All report to AccuKnox Control Plane

### 6. Network Microsegmentation Visual
- Pod A → tries to connect to Pod B on port 8080 → policy allows → green
- Pod A → tries to connect to Pod C on port 5432 (DB) → policy blocks → red
- L3 (IP), L4 (port/protocol), L7 (process name) controls shown per path

### 7. CNAPP Kubernetes Security Architecture
- KSPM layer (agentless): misconfiguration detection, CIS benchmarks, KIEM, K8TLS
- Runtime layer (agent-based eBPF): workload hardening, microsegmentation, behavior monitoring, Zero Trust policy
- Both layers report to unified AccuKnox Control Plane dashboard

---

## Runtime Guardrails — Capability Table

### System Call Policies
| Policy Type | Examples |
|---|---|
| Block dangerous syscalls | execute, chroot, pivot_root, ptrace |
| Allow/block I/O | read, write, mmap on files, directories, sockets, pipes |
| Network controls | connect, listen, accept on IP, port, protocol |

### Threat Detection Scope
- Privilege escalation attempts
- Container breakout attempts
- Crypto mining (known mining binaries)
- Hidden processes (running without standard parent process)
- Lateral movement (cross-pod unauthorized connection)
- Reconnaissance tools (nmap, masscan) running from within containers
- Package manager abuse at runtime (apt, dnf, yum)

### Compliance & Forensics
- Detailed audit logs for every block and audit event
- Map violations to MITRE ATT&CK techniques
- NIST 800-53 control mapping for audit readiness
- CIS benchmark pass/fail reports
- Export logs to Splunk, ELK, or SIEM

---

## Important Links & Resources

| Resource | URL |
|---|---|
| Cluster Onboarding | https://help.accuknox.com/how-to/cluster-onboarding/ |
| CNAPP Security Overview | https://help.accuknox.com/use-cases/cnapp-security-overview/ |
| K8s Security Metrics Widgets | https://help.accuknox.com/use-cases/cnapp-security-overview/#3-k8s-security-metrics-widgets |
| K8s CIS Findings Widget | https://help.accuknox.com/use-cases/cnapp-security-overview/#9-top-5-k8s-cis-findings-widget |
| K8s Resource Summary Widget | https://help.accuknox.com/use-cases/cnapp-security-overview/#6-k8s-resource-summarywidget |
| Admission Controller (KnoxGuard) | https://help.accuknox.com/use-cases/admission-controller-knoxguard/ |
| KIEM Use Case | https://help.accuknox.com/use-cases/kiem/ |
| Network Segmentation | https://help.accuknox.com/use-cases/cards/Network-Segmentation/ |
| Zero Trust Use Case | https://help.accuknox.com/use-cases/zero-trust/ |
| App Behavior | https://help.accuknox.com/saas/app-behavior/ |
| On-Prem Single Node Installation | https://help.accuknox.com/getting-started/on-prem-single-node-installation/ |
| On-Prem Overview | https://help.accuknox.com/getting-started/on-prem-overview/ |
| KSPM Playbook | https://help.accuknox.com/how-to/playbook-kspm/ |
| Security on OpenShift | https://help.accuknox.com/getting-started/security-on-openshift/ |
| EKS / AKS / GKE On-Prem | https://help.accuknox.com/getting-started/onprem-eks-aks-gke/ |
| KubeArmor Differentiation | https://docs.kubearmor.io/kubearmor/quick-links/differentiation |
| K8TLS GitHub | https://github.com/kubearmor/k8tls |
| KubeArmor GitHub | https://github.com/kubearmor/KubeArmor |
| KubeArmor Slack | https://kubearmor.slack.com |
| Zero Trust K8s Guide (eBook) | https://accuknox.com/ebooks/zero-trust-kubernetes-security-definitive-guide |
| CWPP Playbook | https://help.accuknox.com |
| Runtime Security Architecture | https://help.accuknox.com/getting-started/runtime-sec-arch/ |
| Accuknox Agents Overview | https://help.accuknox.com/getting-started/accuknox-agents/ |
