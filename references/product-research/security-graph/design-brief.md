# Security Graph UI Design Brief: AccuKnox CNAPP
**Prepared for: Balaji (UI/UX), Engineering, Product Strategy | May 2026**

---

## Context and Mandate

Security Graph visualization has moved from a Wiz-pioneered differentiator to table-stakes for every serious CNAPP. Google's $32B acquisition of Wiz (March 2026) cemented the graph data model as the asset the industry is building around. Every top vendor now ships a graph UI; absence of one is a fast disqualifier in enterprise RFPs.

AccuKnox has a structural advantage most competitors cannot replicate: KubeArmor with BPF-LSM enforcement at the kernel level, eBPF observability across process/file/network/syscall dimensions, and a Discovery Engine that auto-generates least-privilege policies from observed behavior. The data exists. The engine, transmission, wheels, and brakes are there. What's missing is the exterior: a graph UI layer that makes this data visually explorable, queryable, and presentable to CISOs.

**Critical architectural enabler:** AccuKnox already runs Neo4j (GraphDB) for KIEM metadata, with planned expansion to assets/findings in v3.0. This means the graph database infrastructure is partially in place.

**Customer feedback that triggered this project:**
1. Pod ingress/egress interconnections are not visualized.
2. Pod-to-pod logical connections within a cluster are missing.
3. Behavioral alerts (file/process/network) are not shown on pod state changes.
4. No clarity on overall cluster pod internetworking layout.

---

## Design Principles (Apply to Every Graph View)

1. **Typed, visually distinct nodes.** Each node type gets a unique shape + color + icon. Always show a legend.
2. **Directional, encoded edges.** Edges encode direction (arrow), relationship type (label), and risk severity (thickness + color). Dashed = audit mode, solid = enforced, red = blocked.
3. **Two zoom levels minimum.** Every graph has a "zoom out" (cluster/namespace view) and "zoom in" (pod/process/file view).
4. **Clickable nodes open a side drawer** with full asset context, findings, and remediation actions.
5. **Standard filter bar on every graph:** severity, namespace, label selector, time window, cluster.
6. **KubeArmor heat overlay.** Behavioral alerts (file/process/network anomalies) render as a red glow on affected nodes. Toggle on/off.
7. **Policy state as edge attribute.** Color-code edges by KubeArmor enforcement status: green = Allow, orange = Audit, red = Block.
8. **Attack paths are chains, not isolated findings.** Only show a path if it connects an internet-facing entry point to a sensitive target (secret, PII, privileged role, host mount).

---

## Module-by-Module Analysis

---

### 1. CNAPP Dashboard

**What data exists:**
- 32 CWPP widgets: cluster findings (top 5), findings by asset category with severity, K8s security metrics (misconfigs + vulns), workload alerts by container/VM, workloads without policies, K8s resource summary, cluster connection status, workloads without network policies, top 5 CIS findings, block-based policies with alerts
- 5 CSPM widgets: top 3 cloud accounts with failed controls, top 10 risks (IAM, S3, SGs, LBs), findings trends over time, cloud account status (active/inactive), total findings with top 3 asset categories
- 3 KIEM widgets: risk assessment by criticality, findings by asset type, top 5 critical findings
- Image widgets: severity distribution, risk assessment
- Tickets widget: status breakdown
- Cloud Misconfiguration widget: check results pie chart

**Proposed graph views:**

1. **Executive Security Posture Graph (landing page)**
   - **Nodes:** Cloud accounts (AWS/Azure/GCP icons), K8s clusters (hexagon), VM groups (rectangle), AI/ML services (diamond). Size = asset count. Color = worst severity finding (red/orange/yellow/green).
   - **Edges:** Data flow and trust relationships between accounts and clusters. Thickness = traffic volume or finding count.
   - **Visual encoding:** Each node shows a mini donut chart of finding severity distribution. Red glow = active incidents. Gray = disconnected.
   - **Interaction:** Click any node to drill into that module's dedicated graph. Hover shows summary stats (findings count, compliance %, policy coverage). Filter bar: cloud provider, severity, time range.
   - **Competitive analog:** Wiz's top-level Security Graph overview; Prisma Cloud's three-tab Incidents | Attack Paths | Risks home.
   - **Effort:** Medium (aggregation queries across existing widget data, new graph rendering)
   - **Sales impact:** HIGH (this is the "show the board" artifact CISOs need; directly addresses Nat's feedback)

2. **Cross-Module Attack Path Summary**
   - **Nodes:** Internet (entry point, cloud icon), cloud resources, K8s workloads, secrets/sensitive data (crown jewels). All typed by shape.
   - **Edges:** Chains connecting exposed entry points through misconfigurations, overprivileged roles, vulnerable images, to crown jewels. Each edge labeled with the finding that enables traversal.
   - **Visual encoding:** Path severity = color of the chain (red = critical, orange = high). Choke points highlighted with a shield icon where a single fix breaks the chain.
   - **Interaction:** Click any path to see the full finding chain. Click a choke point to see what policy or fix would break it. Filter by: cloud account, cluster, severity, whether runtime-validated.
   - **Competitive analog:** Wiz toxic combination paths; Microsoft Defender choke point dashboard; Tenable blast radius view.
   - **Effort:** High (requires cross-module correlation engine to compute chains)
   - **Sales impact:** HIGH (single highest-value RFP feature; every competitor has this)

**AccuKnox-unique graph opportunities:**
- Policy coverage overlay on the posture graph: nodes glow differently based on whether KubeArmor hardening policies are active, in audit mode, or missing entirely. No competitor can show "% of attack surface with kernel-level enforcement active."
- Runtime-validated attack paths: mark paths as "observed in production" when KubeArmor telemetry confirms the syscall pattern that would enable traversal. Competitors (except Sysdig and Wiz Defend) show only theoretical paths.

**Priority recommendation:** Ship the Executive Security Posture Graph first. It is the default landing page every CISO demo starts on, it uses only existing widget data, and it immediately answers "show me my risk."

---

### 2. CWPP / Runtime Security (KubeArmor + App Behavior)

**What data exists:**
- **File Observability:** Last Updated Time, File Path Accessed, Process, Cluster, Namespace, Workload, Action (Allow/Block), Occurrence count
- **Process Observability:** Process execution events with PID, PPID, ProcessName, ParentProcessName, Source, Resource, Operation, Action, Syscall data (SYS_EXECVE), Enforcer (eBPF Monitor/AppArmor), Result (Passed/Denied), Severity, MITRE/CIS/NIST tags
- **Network Observability:** IP, Port, Protocol, Namespace, Workload, Command, direction (ingress/egress), connection type
- **API Observability:** (tab visible in UI)
- **Forensics/Alerts:** Full alert records with ClusterName, HostName, NamespaceName, PodName, ContainerName, ContainerID, ContainerImage, Labels, Owner, PolicyName, Tags, timestamp
- **Existing Graph View:** Cluster topology with port-labeled service nodes and directional ingress/egress edges. Clicking an edge opens a detail panel showing IP, namespace, workload, command. Shows 22 clusters, 4 connected, 18 disconnected. Displays total blocked files and processes.
- **Policy enforcement data:** Action taken (Allow/Audit/Block), enforcer type, matched policy name

**Proposed graph views:**

1. **Cluster Topology Graph (upgrade existing)**
   - **Nodes:** Clusters (large circle), Namespaces (nested circles), Pods/Workloads (small circles inside namespaces). Icon on each pod = workload type (Deployment, StatefulSet, DaemonSet, CronJob). Badge count = active alerts.
   - **Edges:** Pod-to-pod network connections observed by eBPF sensor. Arrow = direction. Color = policy state (green = allowed, orange = audit, red = blocked). Thickness = traffic volume (occurrence count). Dashed = no network policy covers this connection.
   - **Visual encoding:** Pod nodes colored by health: green = clean, yellow = warnings, red = critical findings or active blocks. Red glow = behavioral alert active. Cluster-level ring shows connection status (connected/disconnected).
   - **Interaction:** Zoom out = cluster-of-clusters view (the 22-cluster overview). Zoom in = namespace view = pod-level view. Click any pod to open side drawer with: running processes, file accesses, network connections, active policies, alerts. Click any edge to see connection details (IP, port, protocol, process, command). Right-click edge = "Create network policy for this connection."
   - **Competitive analog:** Upwind Topology Graph + Illumio Illumination dependency map applied to K8s. Multi-zoom matches Upwind's "Orbital View."
   - **Effort:** Medium (existing graph view needs restructuring + namespace nesting + policy color overlay)
   - **Sales impact:** HIGH (directly addresses all 4 customer feedback items from Gaurav's CNA call)

2. **Pod Process Tree Graph**
   - **Nodes:** Pod (root), Containers (children), Processes (leaves). Process nodes show: binary name, PID, syscall count. Sensitive files accessed shown as file-icon leaf nodes off each process.
   - **Edges:** Parent-child process relationships (PPID→PID). Process→file edges (labeled with syscall: SYS_OPEN, SYS_OPENAT). Process→network edges (labeled with SYS_CONNECT, SYS_SOCKET + destination IP:port).
   - **Visual encoding:** Process nodes red if blocked by policy, orange if in audit, green if allowed. File nodes flagged if path is sensitive (/etc/shadow, /run/secrets/, service account tokens). Network edges red if connecting to unknown external IPs.
   - **Interaction:** Click any process node to see full forensics: syscall history, matched policies, MITRE ATT&CK technique tags. Time slider to replay process tree evolution. Filter by: severity, operation type (file/process/network), action (allow/block/audit).
   - **Competitive analog:** SentinelOne Process Graph + Storyline (best-in-class for container process-tree visibility). SentinelOne shows containerd as root with bash child processes flagged red. AccuKnox can replicate this with deeper syscall context.
   - **Effort:** Medium (data exists in forensics/alerts; needs tree layout + time slider)
   - **Sales impact:** HIGH (incident response buyers need this; currently only SentinelOne does it well in K8s)

3. **Runtime Behavior Heatmap Graph**
   - **Nodes:** Same topology as Cluster Topology Graph (clusters → namespaces → pods).
   - **Edges:** Same as Cluster Topology Graph.
   - **Visual encoding overlay:** Heat intensity on each node proportional to anomaly score: number of new file accesses + new process executions + new network connections observed in the selected time window vs. baseline. Nodes with zero anomalies = cool blue. High anomaly = hot red. Pulsing animation on nodes with active block events.
   - **Interaction:** Toggle heat overlay on/off. Click a hot node to see what changed (new processes, new file paths, new outbound IPs). Time window selector: last 1h, 6h, 24h, 7d, 30d. Drill-down opens the Pod Process Tree Graph for that pod.
   - **Competitive analog:** Lacework Polygraph behavioral baseline + anomaly overlay. Sysdig's in-use risk highlighting. No competitor combines behavioral anomaly with enforcement status.
   - **Effort:** Medium (behavioral baseline computation needed; visualization is an overlay on existing topology)
   - **Sales impact:** HIGH (addresses "behavioral alerts on pod state changes" feedback; differentiates from all agentless CNAPPs)

4. **File Integrity Monitoring (FIM) Graph**
   - **Nodes:** Pods/containers (circles) connected to file paths (document icons). Sensitive directories (/etc/, /bin/, /sbin/, /boot/, service account token paths) shown as folder nodes.
   - **Edges:** Access relationships from processes to files. Labeled with access type (read/write/execute) and syscall. Color: green = read-only allowed, orange = write in audit mode, red = write blocked.
   - **Visual encoding:** File nodes flagged with shield icon if covered by FIM policy. Warning triangle if accessed by unexpected process. Badge count = access occurrences.
   - **Interaction:** Click any file node to see which processes accessed it, when, and what policy applied. Filter by: directory, access type, action.
   - **Competitive analog:** No direct competitor analog at this granularity. Closest is Aqua Tracee's eBPF file monitoring, but Aqua presents it as timelines, not graphs.
   - **Effort:** Low (data already in File Observability; just needs graph rendering)
   - **Sales impact:** Medium (important for compliance buyers, not a primary demo feature)

**AccuKnox-unique graph opportunities:**
- **Policy overlay on every edge** is the single most differentiated capability. No other CNAPP can show "this network connection is actively being enforced at the kernel level by BPF-LSM" with Allow/Audit/Block color coding. Wiz, Orca, Prisma Cloud, and Tenable can only show theoretical permissions, not runtime enforcement state.
- **"What breaks if I enforce?"** simulation: before activating a hardening policy, show on the graph which currently-allowed edges would become blocked. This mirrors Illumio's draft-mode simulation but at the syscall level, not just network flow level.
- **Discovery Engine policy suggestions rendered as dashed green edges:** show the auto-discovered least-privilege policy as a "proposed" overlay on the graph, letting the operator visually diff current state vs. proposed hardened state.

**Priority recommendation:** Upgrade the existing Cluster Topology Graph to add namespace nesting, pod-level nodes, and policy-state edge coloring. This is the highest-value, lowest-effort change and directly addresses the 4 customer pain points.

---

### 3. KSPM (Kubernetes Security Posture Management)

**What data exists:**
- **KIEM (Kubernetes Identity and Entitlement Management):** Already has an interactive graph visualization (Neo4j-backed). Tracks: Roles, ClusterRoles, RoleBindings, ClusterRoleBindings, Service Accounts, Users, Groups, Workloads. Columns: Role, Resource, ApiGroup, Verbs, Rolebinding, Service Accounts, Workload. 15 predefined security queries (dormant permissions, excessive privileges, roles with secret read access, unused roles, etc.)
- **Admission Controller (KnoxGuard):** Policy name, Action (Block/Allow), target namespaces, READY status, owned Kyverno policies. Enforcement on: registry restrictions, privileged container denial, securityContext validation.
- **Pod Security Admission (PSA):** Per-namespace PSA level (Privileged/Baseline/Restricted), Mode (Enforce/Audit), dry-run preview.
- **CIS K8s Benchmarking:** Finding name/ID, Risk Factor (Critical/High), Tool Output (Passed/Failed), Description, Solution. Covers: etcd, API server, kubelet, cluster components.
- **Cluster Misconfiguration Scanning:** Finding title, source manifest, affected resource type (Deployment/Pod), severity, source code view showing hardcoded values, solution tab, Jira integration.
- **Supply Chain (KnoxGuard):** Registry whitelist patterns, namespace targeting, deployment blocking for untrusted images.

**Proposed graph views:**

1. **KIEM Identity-to-Resource Attack Path Graph (upgrade existing)**
   - **Nodes:** Service Accounts (key icon), Users/Groups (person icon), Roles/ClusterRoles (shield icon), Workloads (pod icon), Secrets (lock icon), Sensitive Resources (crown icon).
   - **Edges:** ServiceAccount→RoleBinding→Role (labeled with verbs: get, list, create, delete). Workload→ServiceAccount (labeled "uses"). Role→Resource (labeled with API group + resource type + verbs). Overprivileged edges shown thicker and red.
   - **Visual encoding:** Nodes sized by blast radius (how many resources an identity can reach). Red border on identities flagged by predefined queries (dormant, excessive, secret-reading). Gray = unused/dormant roles. Yellow = roles with write access to workload resources.
   - **Interaction:** Click any identity node to see full permission chain. Click any resource to see all identities that can access it (reverse path). Toggle "show dormant" to highlight unused service accounts and roles. Filter by namespace, predefined query.
   - **Competitive analog:** Wiz IAM-to-resource permission graph; Prisma Cloud CIEM graph; Orca IAM graph. AccuKnox's version is K8s-native (RBAC-specific), which is more relevant than cloud IAM for KSPM buyers.
   - **Effort:** Low (KIEM already has Neo4j graph; needs visual upgrade + attack path chaining + blast radius sizing)
   - **Sales impact:** HIGH (CIEM/identity graphs are a top-3 RFP requirement)

2. **Cluster Security Posture Graph**
   - **Nodes:** Cluster (center), Namespaces (ring 1), critical K8s components: etcd, API server, kubelet, scheduler (ring 2, hexagons). CIS findings attached as leaf nodes.
   - **Edges:** Component-to-component trust relationships (API server↔kubelet TLS, etcd peer auth). Each edge labeled with CIS benchmark status (pass/fail). Failed edges = red dashed.
   - **Visual encoding:** Components colored by CIS compliance: green = all checks passed, yellow = warnings, red = critical failures. Badge count = number of failed checks. PSA level shown as a label on each namespace node (Privileged/Baseline/Restricted).
   - **Interaction:** Click any component to see its CIS findings in the side drawer. Click a namespace to see its PSA level, misconfigurations, and workloads. Filter by: CIS section, risk factor, compliance status.
   - **Competitive analog:** Microsoft Defender for Cloud's cluster attack path with K8s templates; Tenable's MITRE ATT&CK heatmap applied to K8s.
   - **Effort:** Medium (CIS data + PSA data + cluster component relationships need to be combined)
   - **Sales impact:** Medium (useful for compliance demos; less visual impact than KIEM or topology graphs)

3. **Admission Control Flow Graph**
   - **Nodes:** Deployment request (entry), Admission Controller (gate), KnoxGuard policies (filter nodes), Registry whitelist (list node), PSA validator (gate), final state: Admitted or Rejected.
   - **Edges:** Request flow through each validation gate. Green arrow = passed. Red arrow = blocked (with policy name label).
   - **Visual encoding:** Gate nodes show pass/fail ratio as a mini bar chart. Rejected deployments shown in a side panel with error messages and the specific policy that blocked them.
   - **Interaction:** Filter by namespace, time range. Click any gate to see its configuration. Click any rejected deployment to see why it was blocked and which policy triggered.
   - **Competitive analog:** No direct competitor analog. This is an AccuKnox-unique view because KnoxGuard + PSA + registry whitelisting form a multi-layer admission pipeline that no other vendor visualizes as a flow.
   - **Effort:** Low (admission data already logged; visualization is a simple flow diagram)
   - **Sales impact:** Medium (strong for regulated industries that need audit trails for why deployments were blocked)

**AccuKnox-unique graph opportunities:**
- **KIEM graph + KubeArmor runtime overlay:** Connect KIEM's identity graph to KubeArmor's observed process behavior. Show not just what a service account *can* do (RBAC permissions) but what it *actually does* (observed syscalls). This collapses the gap between theoretical and actual permissions, which is the exact problem CIEM tools try to solve. No competitor does this at the K8s RBAC + kernel syscall level.
- **Supply chain trust graph:** Show container image → registry → admission policy → deployed workload as a chain, with each link validated (trusted registry, scanned image, policy-compliant securityContext). Rejected images shown as broken chains.

**Priority recommendation:** Upgrade the existing KIEM graph with blast-radius node sizing and overprivileged-edge highlighting. This is the lowest-effort, highest-impact change because the Neo4j graph already exists.

---

### 4. CSPM (Cloud Security Posture Management)

**What data exists:**
- **Asset Inventory:** Asset name, asset type, location, cloud account, cloud type, vulnerability findings. Views: List perspective (by asset category), Hierarchy perspective (tree view), Graphical view. Asset categories: Hosts, Applications, Web APIs, Containers, Clusters.
- **Compliance:** 30+ frameworks (CIS Benchmarks, NIST, PCI, HIPAA, SOC2, GDPR, etc.). Data: compliance program name, sub-controls, compliance percentage, passed/failed/warning/not-available check counts. Filters: cloud account, region, severity, checks, compliance program.
- **Cloud Misconfiguration & Drift:** Asset name/type, findings, severity, status, description, scan timestamp, vulnerability trends. Features: periodic scans, custom baselines, monitors for critical assets, drift detection.
- **Cloud accounts:** Active/Inactive status, AWS/Azure/GCP/Oracle.

**Proposed graph views:**

1. **Cloud Asset Relationship Graph**
   - **Nodes:** Cloud accounts (large circle with provider icon), Regions (medium circle), Services (small circles: IAM, S3, EC2, VPC, RDS, Lambda, etc. with AWS/Azure/GCP-specific icons). Assets within each service as leaf nodes. Size = finding count.
   - **Edges:** Account→Region→Service→Asset hierarchy. Cross-cutting edges for: IAM role trust relationships, security group rules (which SG allows traffic to which resource), VPC peering, S3 bucket policies granting cross-account access.
   - **Visual encoding:** Nodes colored by worst finding severity. Red border = critical misconfiguration. Orange = high. Shield icon = compliant. Warning triangle = drift detected. Internet-facing assets get a globe icon.
   - **Interaction:** Drill-down: account → region → service → individual asset. Click any asset to see findings, compliance status, and drift history. Click any IAM edge to see the trust policy. Filter by: cloud provider, region, severity, compliance framework, asset type.
   - **Competitive analog:** Wiz Security Graph (the reference implementation); Orca SideScanning asset graph; CrowdStrike Asset Graph.
   - **Effort:** High (requires building cross-service relationship mapping; CSPM data is currently flat/tabular)
   - **Sales impact:** HIGH (this is the graph every CSPM RFP evaluates)

2. **Compliance Posture Heatmap Graph**
   - **Nodes:** Compliance frameworks (outer ring), sub-controls (inner ring), cloud accounts (center). Each account node connects to frameworks it's evaluated against.
   - **Edges:** Account→Framework→Sub-control chains. Edge color = pass/fail. Thickness = number of checks.
   - **Visual encoding:** Framework nodes show a percentage ring (% compliant). Sub-control nodes colored red/green/yellow by pass rate. Accounts colored by overall compliance score.
   - **Interaction:** Click any framework to expand its sub-controls. Click any sub-control to see the specific failed checks and affected resources. Filter by cloud account, framework, severity.
   - **Competitive analog:** Tenable's ATT&CK heatmap concept applied to compliance; Prisma Cloud's compliance dashboard but as a graph.
   - **Effort:** Low (data already exists in compliance module; just needs graph layout)
   - **Sales impact:** Medium (compliance buyers care, but this is less differentiating than the asset graph)

3. **Cloud Drift Detection Timeline Graph**
   - **Nodes:** Assets that have drifted from baseline. Node = asset. Icon = asset type. Badge = number of drift events.
   - **Edges:** Timeline axis (horizontal). Each drift event = a node on the timeline connected to the asset. Edge labeled with what changed.
   - **Visual encoding:** Drift events colored by severity. Current state vs. baseline state shown in side-by-side comparison when clicked.
   - **Interaction:** Time scrubbing (slide to see state at any point). Click any drift event to see before/after config. Filter by: asset type, severity, cloud account, time range.
   - **Competitive analog:** SentinelOne Storyline time-scrubbing applied to cloud config drift.
   - **Effort:** Medium (drift data exists; timeline rendering with before/after comparison is new)
   - **Sales impact:** Medium (strong for audit/compliance use cases)

**AccuKnox-unique graph opportunities:**
- **Cloud-to-K8s bridge graph:** Connect CSPM cloud assets (e.g., an EKS cluster resource in AWS, an IAM role, an S3 bucket) to CWPP K8s entities (the pods running in that cluster, the service accounts using that IAM role). No other CNAPP stitches cloud posture + K8s runtime + kernel enforcement into one graph. This is AccuKnox's cross-module differentiator.

**Priority recommendation:** Start with the Compliance Posture Heatmap Graph (low effort, data exists) while building toward the Cloud Asset Relationship Graph (high effort, high impact).

---

### 5. CDR (Cloud Detection and Response)

**What data exists:**
- Cloud log event ingestion: AWS CloudTrail, Azure Activity Logs, GCP Audit Logs
- Policy types: Public S3 Bucket Detected, VM-pubip (public IP), unk-access (unauthorized region access)
- Alert data: policy name, type, status, resource affected, region, timestamp
- Remediation: automated workflows via webhooks, notification chains (email/Slack)
- Event flow: Cloud Events → Policy evaluation → Alert → Remediation action

**Proposed graph views:**

1. **CDR Incident Chain Graph**
   - **Nodes:** Cloud event (trigger, lightning bolt icon), affected resource (asset icon), policy violated (shield icon), alert generated (bell icon), remediation action taken (wrench icon).
   - **Edges:** Event→Resource→Policy→Alert→Remediation flow. Temporal ordering preserved (left to right).
   - **Visual encoding:** Event severity colors the entire chain. Remediation node shows status: green = auto-remediated, yellow = pending, red = failed. Resource node shows before/after state.
   - **Interaction:** Click any node to see full event detail. Click remediation to see webhook/action log. Filter by: event type, severity, cloud account, region, remediation status. Time range selector for historical view.
   - **Competitive analog:** Sysdig Cloud Attack Graph real-time detection; CrowdStrike Falcon Fusion SOAR chains.
   - **Effort:** Low (event chain data already exists; visualization is a simple flow graph)
   - **Sales impact:** Medium (CDR is a growing requirement but secondary to posture in current RFPs)

2. **Threat Activity Map (Geographic)**
   - **Nodes:** Cloud regions (positioned on a world map), event hotspots overlaid.
   - **Edges:** Lines connecting source region of suspicious activity to target resource region.
   - **Visual encoding:** Heatmap intensity = event count. Red regions = unauthorized access attempts. Pulsing dots for real-time events.
   - **Interaction:** Click any region to see events originating from or targeting it. Filter by event type, time range.
   - **Competitive analog:** Standard SIEM geo-visualization; unique in CNAPP context.
   - **Effort:** Medium (geographic mapping layer needed)
   - **Sales impact:** Low (visual appeal for demos but low analytical depth)

**AccuKnox-unique graph opportunities:**
- **Cloud-to-Runtime correlation:** When a CDR alert fires (e.g., public S3 bucket detected), show the K8s workloads that access that bucket and whether KubeArmor policies restrict their access. This connects cloud-plane events to runtime enforcement. No agentless CNAPP can do this.

**Priority recommendation:** Ship the CDR Incident Chain Graph first. It's low effort and makes CDR incidents immediately comprehensible as visual flows instead of alert tables.

---

### 6. ASPM (Application Security Posture Management)

**What data exists:**
- **SAST:** Finding type, severity, file path, code snippet, remediation
- **DAST:** Vulnerability type (XSS, SQLi, etc.), endpoint, request/response, severity
- **IaC Scan:** Terraform/CloudFormation misconfigs, resource type, check pass/fail, repository reference
- **Container Scan:** Image name/tag, base image, CVE ID, severity, affected packages, package versions, sensitive data found, full component inventory
- **Secrets Scan:** Secret type (AWS key, DB password, token), file path, commit SHA, developer responsible
- **SCA:** Dependency analysis, component licensing

**Proposed graph views:**

1. **Code-to-Cloud Supply Chain Graph**
   - **Nodes:** Code repositories (folder icon), CI/CD pipelines (gear icon), container images (box icon), registries (database icon), K8s workloads (pod icon), cloud resources (cloud icon).
   - **Edges:** Repo→Pipeline→Image→Registry→Workload→Cloud Resource. Each edge labeled with scan results at that stage (SAST findings, container vulns, IaC misconfigs). Edge color = worst finding severity at that stage.
   - **Visual encoding:** Nodes sized by finding count. Red border = critical/high findings unresolved. Green check = all scans passed. Lock icon on secrets found. Each stage shows a mini severity bar (CVSS distribution).
   - **Interaction:** Click any node to see scan results for that artifact. Click a repo to see SAST + IaC + secret scan findings. Click an image to see CVEs + sensitive data. Click a workload to see runtime behavior (links to CWPP graph). Trace back from a runtime workload to the exact commit that introduced a vulnerability.
   - **Competitive analog:** Wiz Code + Wiz Security Graph back-trace (click a node, see the offending Terraform line); Prisma Cloud Application Graph (CI/CD graph).
   - **Effort:** High (requires stitching scan results from multiple pipeline stages into a unified graph data model)
   - **Sales impact:** HIGH (code-to-cloud traceability is a top-5 enterprise requirement; Wiz Code is driving this)

2. **Container Image Dependency Graph**
   - **Nodes:** Container image (center), base image (parent), packages/libraries (children, sized by CVE count), CVEs (leaf nodes, colored by CVSS severity).
   - **Edges:** Image→Base Image (inheritance). Image→Package (contains). Package→CVE (affected by).
   - **Visual encoding:** Packages with critical CVEs = red. Packages with EPSS > 50% = pulsing red (actively exploited). Clean packages = green. Gray = no vulnerability data.
   - **Interaction:** Click any CVE to see CVSS score, EPSS score, CWE classification, exploit availability (ExploitDB, Metasploit), and remediation (upgrade path). Click base image to see all child images affected. Filter by: severity, EPSS threshold, exploitability, package type.
   - **Competitive analog:** Aqua Hub image→runtime graph; Sysdig in-use vulnerability filtering.
   - **Effort:** Medium (container scan data + EPSS data exist; dependency tree rendering is new)
   - **Sales impact:** Medium (useful but not a primary graph demo feature)

**AccuKnox-unique graph opportunities:**
- **Runtime-validated ASPM findings:** A container image CVE is theoretical until KubeArmor observes the vulnerable package actually being loaded/executed at runtime. AccuKnox can mark "in-use" vs. "not in-use" vulnerabilities on the image dependency graph using runtime process telemetry. This is Sysdig's "Risk Spotlight" concept, but AccuKnox has the enforcement layer to auto-block the vulnerable process.
- **Code-to-enforcement trace:** From a SAST finding → through the container image → to the deployed pod → to the KubeArmor policy that blocks exploitation. Full chain from code defect to kernel-level mitigation. No competitor can show this.

**Priority recommendation:** Build the Code-to-Cloud Supply Chain Graph as a Phase 2 item. In Phase 1, ship the Container Image Dependency Graph since the data is more readily available.

---

### 7. Vulnerability Management

**What data exists:**
- Finding type, Risk Factor (Medium/High/Critical), Last Seen date, Asset name, Finding status
- CVSS score (0-10), EPSS score (0%-100%), CWE classification
- Exploit availability: ExploitDB, Metasploit module status
- Grouping: by Asset or by Finding type
- Rules Engine: automated status changes, ticket creation, notifications (email/Slack/SIEM)
- Findings lifecycle: Active → In Progress → Waiting → Fixed (with intermediate states)

**Proposed graph views:**

1. **Vulnerability Prioritization Matrix Graph**
   - **Nodes:** Vulnerabilities (CVE nodes), sized by affected asset count. Assets (squares), grouped by type.
   - **Edges:** CVE→Asset (affected by). Multiple CVEs connecting to the same asset cluster together visually.
   - **Visual encoding:** CVE nodes positioned on a 2D scatter: X-axis = CVSS severity, Y-axis = EPSS exploitation probability. Top-right quadrant (high CVSS + high EPSS) = red, pulsing. Nodes with known exploits (ExploitDB/Metasploit) get an exploit icon. CWE category shown as a colored ring around CVE nodes.
   - **Interaction:** Click any CVE to see affected assets, EPSS timeline, exploit links, and CWE details. Click any asset to see all CVEs. Quadrant click filters the list. Filter by: severity, EPSS threshold, CWE, asset type, status.
   - **Competitive analog:** Tenable's CVSS + EPSS prioritization; CrowdStrike ExPRT.AI predictive scoring. AccuKnox adding runtime "in-use" context on top goes beyond both.
   - **Effort:** Low (CVSS + EPSS + CWE data already collected; scatter plot layout)
   - **Sales impact:** HIGH (vulnerability prioritization with EPSS is a hot buyer criterion right now)

2. **Vulnerability Blast Radius Graph**
   - **Nodes:** Selected CVE (center), affected images (ring 1), workloads running those images (ring 2), namespaces containing those workloads (ring 3), clusters (ring 4).
   - **Edges:** CVE→Image→Workload→Namespace→Cluster chain. Each edge shows count (e.g., "12 pods affected").
   - **Visual encoding:** Rings expand outward = increasing blast radius. Color intensity = finding severity. Workloads with active KubeArmor policies shown with shield icon (mitigated).
   - **Interaction:** Click any ring level to see details. Select multiple CVEs to see combined blast radius. Filter by: cluster, namespace, policy status.
   - **Competitive analog:** Tenable's Blast Radius view; Wiz toxic combination scope.
   - **Effort:** Medium (requires joining container scan data with cluster inventory)
   - **Sales impact:** Medium (strong for remediation prioritization conversations)

**AccuKnox-unique graph opportunities:**
- **EPSS + Runtime = true priority:** Overlay KubeArmor's observed process execution data on the EPSS chart. A high-EPSS vulnerability in a package that KubeArmor observes being actively loaded at runtime is a confirmed risk. A high-EPSS vulnerability in a package never loaded = deprioritize. This is the "in-use" concept that Sysdig pioneered, but with AccuKnox's enforcement capability to immediately block the process.

**Priority recommendation:** Ship the Vulnerability Prioritization Matrix Graph in Phase 1. The scatter plot layout is simple, data already exists, and EPSS-driven prioritization is a strong sales differentiator.

---

### 8. API Security

**What data exists:**
- Endpoints: Method (GET/POST/PUT/DELETE/PATCH), Path, Host/Domain
- Request/response bodies, sensitive data classification labels
- External/Internal designation
- API classification: Active, Shadow (runtime but undocumented), Zombie (documented but inactive), Orphan (documented but unused)
- OpenAPI specification comparison
- Collections (grouped by host/pattern)
- Rate limit policies (per user/IP per endpoint, per user/IP global, global service limit)
- Attribution policy (JWT claims/headers mapping requests to user identities)

**Proposed graph views:**

1. **API Topology and Risk Graph**
   - **Nodes:** Hosts/domains (large circles), API endpoints (small circles inside hosts, colored by method: GET=blue, POST=green, PUT=orange, DELETE=red). Shadow APIs = dashed border. Zombie APIs = gray. Orphan APIs = dotted. Active APIs = solid.
   - **Edges:** Client→Endpoint (traffic flow). Endpoint→Sensitive Data (if classified as handling PII/credentials). Endpoint→Backend Service (if known).
   - **Visual encoding:** Endpoint nodes sized by request volume. Red glow on endpoints with security findings (injection, auth bypass). Shadow APIs pulsing yellow (undocumented risk). Zombie APIs grayed out.
   - **Interaction:** Click any endpoint to see request/response patterns, sensitive data labels, findings, rate limit config. Click host to see all endpoints and their classification. Toggle: show only Shadow APIs, show only with findings. Filter by: method, classification, sensitive data, host.
   - **Competitive analog:** Orca API security graph (apps→domains→endpoints→IPs). Salt Security API topology.
   - **Effort:** Medium (API inventory data exists; topology rendering and classification overlay are new)
   - **Sales impact:** Medium (API security is a growing CNAPP requirement but not the primary graph demo)

**AccuKnox-unique graph opportunities:**
- **API endpoint → K8s workload → KubeArmor policy chain:** Trace an API endpoint to the pod serving it, then to the KubeArmor policies governing that pod's network and process behavior. Show whether the pod behind a Shadow API has any enforcement policies at all. No other CNAPP connects API inventory to kernel-level enforcement.

**Priority recommendation:** Ship the API Topology Graph in Phase 2 after the core K8s and cloud graphs are in place.

---

### 9. AI/ML Security (AI-SPM)

**What data exists:**
- **AI-DR (Detection and Response):** Cloud AI service events (SageMaker notebook creation, Bedrock model customization, Azure ML workspace changes, Azure OpenAI resource deletion). Configuration parameters, risk classification (public access, encryption, IAM).
- **Prompt Firewall:** LLM request/response monitoring, prompt injection detection, jailbreak detection, PII leakage detection, toxicity detection.
- **ModelArmor:** Model file scanning (pickle code injection, adversarial attack detection), deployment security.
- **Red Teaming:** Probe categories and results.
- **MCP Security:** (documented as integration)

**Proposed graph views:**

1. **AI Asset and Risk Graph**
   - **Nodes:** AI/ML services (SageMaker, Bedrock, Azure ML, Azure OpenAI as large icons), individual assets (notebooks, models, workspaces, endpoints as smaller nodes), data sources (training data, S3 buckets, databases as cylinder icons), IAM roles accessing AI services (key icons).
   - **Edges:** Service→Asset (hosts). Asset→Data Source (reads from). IAM Role→Service (accesses). Prompt Firewall→Endpoint (protects, shown as a shield on the edge).
   - **Visual encoding:** Assets colored by risk: red = public access + no encryption + overprivileged IAM. Green = properly configured. Nodes with AI-DR alerts get a pulsing red glow. Prompt Firewall coverage shown as a green shield badge on protected endpoints.
   - **Interaction:** Click any AI asset to see its configuration, AI-DR events, and risk factors. Click an IAM role to see what AI resources it can access (and whether that's excessive). Click a Prompt Firewall-protected endpoint to see detection stats (injections blocked, PII caught). Filter by: cloud provider, risk level, asset type.
   - **Competitive analog:** No established competitor analog. AI-SPM graphs are nascent. Wiz has early AI asset inventory; Prisma Cloud is adding AI posture. AccuKnox can lead here.
   - **Effort:** Medium (AI-DR event data exists; IAM cross-referencing and graph layout are new)
   - **Sales impact:** HIGH (AI security is the fastest-growing CNAPP sub-category; a visual graph here is a first-mover advantage)

**AccuKnox-unique graph opportunities:**
- **Prompt Firewall as a graph edge attribute:** Show LLM request flows with the Prompt Firewall as an inline gate (like the Admission Controller flow graph). Requests pass through: toxicity check → PII check → injection check → model endpoint. Each check node shows pass/block rates. No competitor visualizes prompt firewall enforcement as a flow graph.
- **ModelArmor scan results on the graph:** Model file nodes show scan results (pickle injection detected, adversarial vulnerability found) directly as badges.

**Priority recommendation:** Ship the AI Asset and Risk Graph in Phase 2. AI security demos are increasingly requested, and a visual graph here positions AccuKnox ahead of competitors who only have asset lists.

---

### 10. Network Micro-segmentation

**What data exists:**
- Auto-discovered network policies (east-west traffic patterns)
- Pod labels and selectors, port specifications, protocol specifications
- Network policy rules: ingress/egress, source/destination pods, ports, protocols
- Policy status: pending, active, approved
- TLS scan data: service name, IP, port, TLS status (TLS/PLAIN_TEXT/CONNFAIL), TLS version, cipher suite, certificate hash, signature algorithm, verification status
- Zero Trust network control: process-based network access, binary-specific TCP/UDP

**Proposed graph views:**

1. **East-West Traffic Flow Graph (Illumio-style for K8s)**
   - **Nodes:** Namespaces (large bubbles), pods/workloads within each namespace (small circles). App tier grouping (frontend, backend, database) if labels exist.
   - **Edges:** Network connections between pods. Arrow = direction. Color = policy state: green = covered by network policy (allowed), orange = no network policy (uncontrolled), red = explicitly blocked. Dashed = connection observed but no policy exists yet (discovered by Discovery Engine). Line thickness = traffic volume.
   - **Visual encoding:** Namespace bubbles show overall policy coverage percentage. Pods without any network policy = yellow warning icon. TLS status shown on edges: lock icon = TLS, open lock = PLAIN_TEXT, broken lock = CONNFAIL.
   - **Interaction:** Click any edge to see: source/destination details, port, protocol, TLS status, cipher suite, policy covering this connection. Click "Create Policy" on any uncontrolled edge to auto-generate a network policy from the discovered traffic pattern. Click any namespace to see all its network policies. Filter by: namespace, protocol, TLS status, policy state, port.
   - **Competitive analog:** Illumio Illumination bubble-and-flow map (the gold standard for microsegmentation visualization); Cilium Hubble flow map but with security context added.
   - **Effort:** Medium (network observability data exists; Illumio-style bubble layout and TLS overlay are new)
   - **Sales impact:** HIGH (microsegmentation visualization is exactly what Gaurav's customer requested; this is the "pod internetworking layout" feedback item)

2. **TLS Compliance Graph**
   - **Nodes:** Services (circles), organized by namespace. Each service annotated with its TLS status.
   - **Edges:** Service-to-service connections. Green = TLS 1.3. Yellow = TLS 1.2. Red = PLAIN_TEXT. Gray = CONNFAIL.
   - **Visual encoding:** Services using deprecated TLS versions flagged with warning. Services with failed certificate verification flagged with red X.
   - **Interaction:** Click any service to see TLS details (version, cipher, cert hash, verification). Filter by TLS status, version.
   - **Competitive analog:** No direct competitor analog. Unique AccuKnox capability from the zero-trust TLS scanning feature.
   - **Effort:** Low (TLS scan data already collected; simple graph layout)
   - **Sales impact:** Medium (strong for zero-trust / compliance-focused buyers)

**AccuKnox-unique graph opportunities:**
- **Process-level network segmentation:** Show not just pod-to-pod connections but process-to-process connections. KubeArmor knows which binary (wget, curl, nginx) initiated each connection. No other network policy tool operates at process granularity. Edges labeled with the binary name, not just the pod label.
- **"What breaks if I enforce?"** simulation for network policies: before activating a discovered network policy, overlay its effect on the traffic graph. Connections that would be blocked turn red. Connections that are already covered stay green. New connections that would be explicitly allowed turn green. This is Illumio's draft-mode concept brought to K8s.

**Priority recommendation:** Ship the East-West Traffic Flow Graph in Phase 1. This directly solves all 4 customer feedback items and the data already flows through the existing graph view.

---

### 11. Policy Management

**What data exists:**
- 668 total policies: Discovered (239), Hardening (417), Custom (12)
- Policy fields: Policy Name, Category (Discovered/Hardening/Custom), Status (Active/Inactive), Cluster, Namespace, Selector Labels
- KubeArmor policy types: process execution, file access, network operations, capabilities, syscalls
- Policy enforcement: Allow/Audit/Block actions
- Compliance mapping: MITRE ATT&CK, CIS, NIST 800-53, STIGs
- 15 hardening policy categories: service account token protection, FIM, package manager blocking, trusted certs, database access, config data protection, file copy prevention, network access control, /tmp/ no-exec, admin tools restriction, discovery tools, log delete prevention, ICMP control, capability restriction
- Discovery Engine auto-generates policies from observed behavior
- Version control (Git-based)

**Proposed graph views:**

1. **Policy Coverage Map**
   - **Nodes:** Workloads/pods (circles), policies (shield icons). Workloads sized by number of applied policies. Policies sized by number of workloads they protect.
   - **Edges:** Policy→Workload (protects). Color: green = active and enforcing (Block mode), orange = audit only, blue = discovered but inactive. Thickness = policy specificity (more specific selector = thicker).
   - **Visual encoding:** Workloads with zero policies = red border (unprotected). Workloads with only audit-mode policies = orange. Workloads with block-mode hardening = green with shield. Compliance tags shown as small badges on policy nodes (MITRE, CIS, NIST).
   - **Interaction:** Click any workload to see all policies applied to it and their enforcement state. Click any policy to see all workloads it covers. Toggle: show only unprotected workloads, show only audit-mode, show by compliance framework. Filter by: cluster, namespace, policy category, status, compliance tag.
   - **Competitive analog:** Upwind Explorer query→policy round-trip; Illumio policy coverage view.
   - **Effort:** Low (all policy and workload data exists; bipartite graph layout)
   - **Sales impact:** HIGH (immediately answers "how much of my cluster is actually protected?" which is the #1 CISO question)

2. **Policy Enforcement State Machine**
   - **Nodes:** Policy lifecycle states: Discovered → Inactive → Audit → Active (Block). Each state as a column.
   - **Edges:** Policies flow from left (discovered) to right (enforced). Each policy is a small dot moving through the pipeline.
   - **Visual encoding:** Column heights represent count of policies in each state. Color = policy category (hardening = blue, custom = purple, discovered = gray). Bottleneck detection: if "Inactive" column is much taller than "Active," it's visually obvious that policies aren't being activated.
   - **Interaction:** Click any column to see the policies in that state. Drag a policy dot from Inactive to Audit to preview its effect. Click "Activate All Discovered" to batch-activate. Filter by: cluster, namespace, category.
   - **Competitive analog:** No direct competitor analog. This pipeline visualization is unique because no other CNAPP has a multi-stage policy activation workflow.
   - **Effort:** Low (policy status data exists; Kanban/pipeline layout)
   - **Sales impact:** Medium (strong for operational teams managing large policy sets; helps explain the 239 Discovered → Active journey)

**AccuKnox-unique graph opportunities:**
- **Every graph view in every module should have a "Show Policies" toggle** that overlays KubeArmor policy state on nodes and edges. This is AccuKnox's cross-cutting differentiator. When toggled on: every node shows whether it's protected, every edge shows whether the connection is enforced. No competitor can do this because they don't have an LSM-level enforcement engine.
- **"Hardening gap analysis" graph:** Overlay the 15 hardening policy categories on each workload. Show a radar/spider chart per workload: which of the 15 categories are covered (FIM, package managers, capability restriction, etc.) and which are missing. This quantifies "how hardened is this workload?" visually.

**Priority recommendation:** Ship the Policy Coverage Map in Phase 1. It answers the #1 CISO question, uses only existing data, and is a simple bipartite graph layout.

---

### 12. VM Security

**What data exists:**
- Agent-based: Linux and Windows host monitoring, process execution events, file access events, KubeArmor systemd-mode enforcement
- Agentless: Cloud VM scan (AWS, Azure, GCP), misconfiguration detection, compliance benchmarking (STIGs, CIS)
- Host vulnerability/malware scan: CVE findings, malware detection
- Compliance benchmarking: GDPR, HIPAA, PCI DSS conformance
- FIM and workload hardening for VMs (blocking package managers, log deletion prevention, cryptominer prevention)
- Audit log management

**Proposed graph views:**

1. **VM Fleet Posture Graph**
   - **Nodes:** Cloud accounts (outer ring), regions (middle ring), VMs (inner nodes). VMs typed by OS icon (Linux penguin, Windows logo). Agent-based VMs show a sensor icon. Agentless = no sensor icon.
   - **Edges:** Account→Region→VM hierarchy. VM→VM lateral movement potential (if they share security groups/VPCs). VM→Cloud Service dependencies.
   - **Visual encoding:** VMs colored by posture: green = compliant + no critical vulns + malware-free. Yellow = warnings. Red = critical vulns or malware detected. Shield icon = KubeArmor agent installed and enforcing. Gray border = agentless only (scan data but no enforcement).
   - **Interaction:** Click any VM to see: vulns, malware scan results, compliance status, installed packages, KubeArmor policies (if agent-based). Filter by: OS, agent status, severity, compliance framework.
   - **Competitive analog:** CrowdStrike Falcon endpoint fleet view; SentinelOne Singularity fleet graph.
   - **Effort:** Medium (VM scan data exists; fleet graph layout and lateral movement edges are new)
   - **Sales impact:** Medium (VM security graph matters for hybrid cloud buyers)

**AccuKnox-unique graph opportunities:**
- **Unified K8s + VM graph:** Show K8s clusters and VMs on the same topology graph, connected by network edges where they communicate. Useful for customers running mixed workloads. KubeArmor's systemd mode means VM enforcement telemetry has the same format as K8s telemetry, so the graph can treat both uniformly.

**Priority recommendation:** VM Fleet Posture Graph is a Phase 2 item. Most AccuKnox customers lead with K8s; VM graph is important for hybrid deals.

---

### 13. xBOM (Extended Bill of Materials)

**What data exists:**
- SBOM: Software dependencies, package names, versions, licenses
- CBOM: Cryptographic assets (algorithms, key lengths, certificates)
- AIBOM: AI/ML model components
- Per-project organization with labels
- Post-generation scanning: CVEs, license issues, outdated components
- Generation methods: knoxctl CLI, container image scan, GitHub Actions

**Proposed graph views:**

1. **Dependency and Risk Graph**
   - **Nodes:** Projects (large), components/packages (medium, colored by type: library=blue, framework=purple, OS package=gray), CVEs (small red circles), licenses (small colored tags).
   - **Edges:** Project→Component (depends on). Component→CVE (affected by). Component→License (governed by).
   - **Visual encoding:** Components with critical CVEs = red border. Components with copyleft licenses = yellow flag. Outdated components = gray with clock icon. Shared components (used by multiple projects) = larger node with count badge.
   - **Interaction:** Click any component to see CVEs, license, version, and which projects use it. Click any CVE to see CVSS/EPSS/CWE details. Click any license to see compliance implications. "Shared dependency" view highlights components used across multiple projects. Filter by: project, CVE severity, license type, outdated.
   - **Competitive analog:** Aqua Hub code→image→runtime graph; Wiz Code dependency tracking.
   - **Effort:** Medium (SBOM data exists; graph rendering of dependency trees is new)
   - **Sales impact:** Medium (SBOM is increasingly mandated by regulation, but the graph is supplementary to the primary data)

**AccuKnox-unique graph opportunities:**
- **SBOM→Runtime validation:** Cross-reference SBOM components with KubeArmor's observed process execution. A package listed in the SBOM but never loaded at runtime = deprioritize its CVEs. A package actively being executed = prioritize. This "in-use" filtering applied to SBOM is very rare.

**Priority recommendation:** Phase 2/3 item. SBOM graph is regulation-driven but not a primary sales driver for graph UI.

---

### 14. Secrets Management

**What data exists:**
- Vault-compatible Secrets Manager with KV, Transit, PKI engines
- Dynamic secrets (short-lived credentials for AWS, K8s, databases)
- Identity-based access control (OIDC, LDAP, Okta, K8s Auth, tokens, AppRole)
- Audit logs for every request
- Multi-tenant namespaces
- Secrets scan (from ASPM): secret type, file path, commit SHA, developer responsible

**Proposed graph views:**

1. **Secrets Access and Exposure Graph**
   - **Nodes:** Secrets (lock icons), identities/service accounts that access them (key icons), workloads that use them (pod icons), code repos where secrets were found in scans (warning triangle).
   - **Edges:** Identity→Secret (accesses, labeled with engine type: KV/Transit/PKI). Workload→Secret (mounts/reads). Repo→Secret (leaked in, with commit SHA). Dynamic secret edges = dashed (ephemeral).
   - **Visual encoding:** Leaked secrets = red pulsing. Rotated/revoked = green. Static long-lived secrets = yellow warning. Dynamic secrets = blue (healthy). Secrets accessible by too many identities = large node.
   - **Interaction:** Click any secret to see access audit log, which identities and workloads use it, and whether it was leaked in code. Click any identity to see all secrets it can access. "Over-exposed secrets" filter highlights secrets with too many consumers. Filter by: secret type, engine, namespace, exposure status.
   - **Competitive analog:** Wiz secrets-in-graph; Prisma Cloud DSPM context on attack paths.
   - **Effort:** Medium (secrets management data + scan data exist; joining them into a graph is new)
   - **Sales impact:** Medium (secrets exposure is a common attack path component; important for path completeness)

**AccuKnox-unique graph opportunities:**
- **Service account token access graph:** KubeArmor specifically monitors /run/secrets/kubernetes.io/serviceaccount/ access. Show which processes in which pods are reading service account tokens, and whether KubeArmor policies restrict this access. This is a Hildegard-attack-specific defense that AccuKnox already implements but doesn't visualize.

**Priority recommendation:** Phase 2 item. Secrets access graph becomes critical when building full attack paths (a chain often terminates at a secret).

---

## Master Graph Roadmap

| # | Module | Graph View | Effort | Sales Impact | Unique to AccuKnox? | Ship Phase |
|---|--------|-----------|--------|-------------|---------------------|------------|
| 1 | CNAPP Dashboard | Executive Security Posture Graph | Medium | HIGH | Partial (policy coverage overlay) | 1 |
| 2 | CNAPP Dashboard | Cross-Module Attack Path Summary | High | HIGH | Yes (runtime-validated paths) | 3 |
| 3 | CWPP/Runtime | Cluster Topology Graph (upgrade existing) | Medium | HIGH | Yes (policy-state edges, process-level) | 1 |
| 4 | CWPP/Runtime | Pod Process Tree Graph | Medium | HIGH | Yes (syscall-level tree with enforcement) | 1 |
| 5 | CWPP/Runtime | Runtime Behavior Heatmap Graph | Medium | HIGH | Yes (behavioral baseline + enforcement) | 2 |
| 6 | CWPP/Runtime | File Integrity Monitoring Graph | Low | Medium | Yes (FIM at graph level with policy state) | 2 |
| 7 | KSPM | KIEM Identity-to-Resource Attack Path (upgrade) | Low | HIGH | Partial (+ runtime overlay is unique) | 1 |
| 8 | KSPM | Cluster Security Posture Graph | Medium | Medium | No | 2 |
| 9 | KSPM | Admission Control Flow Graph | Low | Medium | Yes (multi-layer admission pipeline) | 2 |
| 10 | CSPM | Cloud Asset Relationship Graph | High | HIGH | Partial (cloud-to-K8s bridge is unique) | 2 |
| 11 | CSPM | Compliance Posture Heatmap Graph | Low | Medium | No | 1 |
| 12 | CSPM | Cloud Drift Detection Timeline Graph | Medium | Medium | No | 2 |
| 13 | CDR | CDR Incident Chain Graph | Low | Medium | Partial (cloud-to-runtime correlation) | 1 |
| 14 | CDR | Threat Activity Map (Geographic) | Medium | Low | No | 3 |
| 15 | ASPM | Code-to-Cloud Supply Chain Graph | High | HIGH | Yes (code-to-enforcement trace) | 2 |
| 16 | ASPM | Container Image Dependency Graph | Medium | Medium | Partial (in-use filtering is unique) | 2 |
| 17 | Vuln Mgmt | Vulnerability Prioritization Matrix | Low | HIGH | Partial (runtime "in-use" overlay) | 1 |
| 18 | Vuln Mgmt | Vulnerability Blast Radius Graph | Medium | Medium | Partial (enforcement shield overlay) | 2 |
| 19 | API Security | API Topology and Risk Graph | Medium | Medium | Partial (API→pod→policy chain) | 2 |
| 20 | AI-SPM | AI Asset and Risk Graph | Medium | HIGH | Yes (Prompt Firewall flow graph) | 2 |
| 21 | Network | East-West Traffic Flow Graph | Medium | HIGH | Yes (process-level segmentation) | 1 |
| 22 | Network | TLS Compliance Graph | Low | Medium | Yes (zero-trust TLS scan visualization) | 1 |
| 23 | Policy Mgmt | Policy Coverage Map | Low | HIGH | Yes (enforcement state on every workload) | 1 |
| 24 | Policy Mgmt | Policy Enforcement State Machine | Low | Medium | Yes (multi-stage activation pipeline) | 1 |
| 25 | VM Security | VM Fleet Posture Graph | Medium | Medium | Partial (unified K8s+VM graph) | 2 |
| 26 | xBOM | Dependency and Risk Graph | Medium | Medium | Partial (SBOM→runtime validation) | 2 |
| 27 | Secrets | Secrets Access and Exposure Graph | Medium | Medium | Yes (SA token access monitoring) | 2 |

---

## Phase 1 Summary (0-6 months): Ship These First

**9 graph views, all using existing data, no new telemetry required:**

| Priority | Graph View | Module | Why First |
|----------|-----------|--------|-----------|
| P0 | Cluster Topology Graph (upgrade) | CWPP/Runtime | Directly fixes all 4 customer feedback items. Existing graph view just needs namespace nesting + policy-state edges. |
| P0 | East-West Traffic Flow Graph | Network | The "pod internetworking layout" request. Illumio-style bubble map for K8s. |
| P0 | Policy Coverage Map | Policy Mgmt | Answers "how protected am I?" in one visual. Simple bipartite layout. |
| P1 | Executive Security Posture Graph | Dashboard | The CISO demo landing page. Aggregates existing widget data into a graph. |
| P1 | KIEM Graph upgrade | KSPM | Neo4j graph already exists. Add blast-radius sizing and overprivileged highlighting. |
| P1 | Vulnerability Prioritization Matrix | Vuln Mgmt | EPSS scatter plot. Data exists. Strong sales differentiator. |
| P2 | Pod Process Tree Graph | CWPP/Runtime | SentinelOne-style process tree for K8s. Uses existing forensics data. |
| P2 | CDR Incident Chain Graph | CDR | Simple flow visualization of existing CDR event chains. |
| P2 | TLS Compliance Graph | Network | Quick win from existing TLS scan data. Low effort. |
| P2 | Policy Enforcement State Machine | Policy Mgmt | Kanban pipeline for policy activation. Low effort, clarifies the Discovered→Active journey. |
| P2 | Compliance Posture Heatmap | CSPM | Framework compliance as a graph. Low effort. |

**Phase 1 success metric:** After shipping these 11 views, AccuKnox should be able to run a 30-minute CISO demo that never leaves graph views: Dashboard posture graph → drill into a cluster topology → show policy coverage → show a process tree for an incident → show east-west traffic → show vulnerability prioritization → show compliance.

---

## Phase 2 Summary (6-12 months): KubeArmor-Unique Value

| Graph View | Why Phase 2 |
|-----------|-------------|
| Runtime Behavior Heatmap | Needs behavioral baseline computation engine |
| FIM Graph | Extends CWPP graph with file-level detail |
| Cloud Asset Relationship Graph | Requires CSPM cross-service relationship mapping |
| Cloud Drift Timeline | Needs before/after config diffing |
| Code-to-Cloud Supply Chain Graph | Requires stitching CI/CD scan stages |
| Container Image Dependency Graph | Needs SBOM data joined with scan results |
| API Topology Graph | Needs API inventory → K8s workload mapping |
| AI Asset and Risk Graph | Needs AI-DR data structured as graph nodes |
| VM Fleet Posture Graph | Needs VM scan data → graph conversion |
| xBOM Dependency Graph | Needs SBOM component tree rendering |
| Secrets Access Graph | Needs secrets audit logs joined with workload data |
| Vulnerability Blast Radius | Needs CVE→image→workload chain computation |
| Cluster Security Posture Graph | Needs CIS data + PSA + component relationships |
| Admission Control Flow Graph | Needs admission event pipeline rendering |

**Phase 2 unique capability:** Every graph view gets the "Show Policies" toggle that overlays KubeArmor enforcement state. And the key demo moment: "What breaks if I enforce this policy?" simulation, where proposed policies are overlaid on the graph showing which edges would change from green (allowed) to red (blocked).

---

## Phase 3 Summary (12-18 months): Runtime-Validated Attack Paths + AI

| Graph View | Why Phase 3 |
|-----------|-------------|
| Cross-Module Attack Path Summary | Requires cross-module correlation engine computing chains across CSPM + KSPM + CWPP + ASPM + Secrets data |
| Threat Activity Map (Geographic) | Nice-to-have geographic overlay |
| Runtime-validated attack paths | Mark each theoretical attack path as "confirmed by runtime" when KubeArmor eBPF telemetry observes the syscall pattern |
| Behavioral anomaly nodes | When KubeArmor sees a new outbound IP, new process, or new file access for the first time, the graph lights up |
| Natural-language graph queries | AI layer for querying the graph: "show me all pods with internet exposure that have critical CVEs and no network policy" |
| Auto-generated KubeArmor policy from graph selection | Select 5 pods on the graph → "Harden to least-privilege based on last 14 days of observed behavior" |

---

## Cross-Cutting Capabilities (Build Once, Use Everywhere)

These capabilities apply across all graph views and should be built as shared components:

1. **Graph rendering engine:** Use a library like D3.js, Cytoscape.js, or react-flow. Must support: zoom/pan, node grouping/nesting, edge bundling, animations, 1000+ node performance.

2. **Side drawer component:** Standardized panel that opens on node/edge click. Shows asset details, findings, policies, remediation actions. Consistent across all graph views.

3. **Filter bar component:** Standard filter bar: severity, namespace, cluster, label selector, time window. Same component on every graph.

4. **KubeArmor policy overlay toggle:** A single toggle button that, when enabled, color-codes all edges by enforcement state (Allow/Audit/Block) and shows shield badges on protected nodes. Shared across every graph view.

5. **Heat overlay toggle:** Behavioral anomaly heatmap that can be toggled on any topology-style graph. Shared computation engine, shared visual layer.

6. **Export and share:** Every graph view can be exported as PNG/SVG for reports, or shared as a deep link with preserved filters and zoom state. This is the "show the board" capability CISOs need.

7. **Graph query language (Phase 3):** A unified query language that works across all graph views. Natural language layer on top. "Show me all pods in namespace X that have critical CVEs and no hardening policy." Returns a filtered graph view.

---

## Competitive Positioning After Full Rollout

After Phase 3, AccuKnox's graph capabilities vs. the competition:

| Capability | Wiz | Prisma | Sysdig | SentinelOne | AccuKnox (target) |
|-----------|-----|--------|--------|-------------|-------------------|
| Cloud asset graph | Best | Good | Limited | Limited | Good (Phase 2) |
| K8s topology graph | Good | Partial | Good | Good | **Best** (Phase 1) |
| Pod process tree | No | No | Limited | Best | **Best** (Phase 1, with enforcement) |
| Runtime behavioral heatmap | Limited | No | Good | Limited | **Best** (Phase 2) |
| Enforcement policy overlay | No | No | No | No | **Only AccuKnox** (Phase 1) |
| East-west traffic (K8s-native) | No | No | Partial | No | **Best** (Phase 1) |
| "What breaks if I enforce?" sim | No | No | No | No | **Only AccuKnox** (Phase 2) |
| Runtime-validated attack paths | Wiz Defend (new) | No | Yes | Verified Paths | **Yes** (Phase 3) |
| AI/ML security graph | Early | Early | No | No | **First** (Phase 2) |
| Code-to-enforcement trace | No | No | No | No | **Only AccuKnox** (Phase 2) |
| Natural-language graph query | Wiz AI | Copilot | Sage | Purple AI | Phase 3 |

**The AccuKnox differentiation story in three sentences:** "We show you the same cloud and K8s security graph that every CNAPP shows. But we're the only one that can color every edge by whether it's actively enforced at the kernel level right now. And we can simulate what breaks before you flip the switch from audit to enforce."
