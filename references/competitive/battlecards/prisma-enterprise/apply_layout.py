"""Group the rows, shorten every cell, and write data/groups.json for the builder.

Source ids, icons and statuses come from data/rows.json (built by merge_research.py).
Keys below are the live-page row numbers 1 to 68.

    python references/competitive/battlecards/prisma-enterprise/apply_layout.py
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
D = HERE / "data"
ROWS = json.loads((D / "rows.json").read_text(encoding="utf-8"))
ROW = {i + 1: r for i, r in enumerate(ROWS)}

# n: (parameter, AccuKnox cell, Prisma cell). None keeps the current text.
SHORT = {
    1: ("SaaS (Regional / Sovereign)", "SaaS in US, EU, India, Middle East", "17 SaaS tenants incl. GovCloud, China"),
    2: ("Customer Cloud (BYOC)", "Control plane in your AWS, Azure or GCP", "SaaS only. PAN runs the console"),
    3: ("On-Prem / Private Cloud", "Full control plane on-prem, all features but AskADA", "Defenders on-prem. Control plane SaaS only"),
    4: ("Air-Gapped Deployment", "ASPM, CSPM, CWPP, KSPM, GRC fully offline", "Not in Enterprise Edition. Compute Edition only"),
    14: ("SAST", "Pipeline and IDE SAST, AI false-positive triage", "No native scanner. Imports Veracode, SonarQube, SARIF"),
    15: ("DAST", "4 scan types, incl. authenticated behind MFA", "No DAST. WAAS is runtime protection"),
    9: ("Code Quality (Best Practices)", "2-engine SAST, 14 languages, SonarQube gates", "No code quality scanning documented"),
    10: ("IaC Scanning", "Terraform, CFN, ARM, Bicep, Helm, Ansible, CDK + 6", "Terraform, OpenTofu, CFN, ARM, Bicep, Helm, Ansible + 7"),
    11: ("Container Scanning", "CI/CD, registry, in-cluster, deploy blocking", "Registry, CI, agentless and twistcli scans"),
    5: ("Secrets (Repo / IaC)", "Repos, pipelines, IaC, correlated in ASPM", "VCS and CI/CD scans, Git history, validation"),
    7: ("Secrets in K8s ConfigMaps", "ConfigMaps and deployment manifests", "Repo files only. No in-cluster ConfigMap scan"),
    12: ("SARIF Ingestion", "Any tool: Checkmarx, JFrog, Gitleaks, Sonatype", "SARIF 2.0 and 2.1 via console or API"),
    13: ("Repo / CI/CD Integration", "GitHub, GitLab, Bitbucket + 9 CI/CD platforms", "5 VCS + Jenkins, Actions, CircleCI, Azure"),
    8: ("SCA", "Dependency SCA with CVE and license checks", "SCA, license compliance, PR package fixes"),
    49: ("Generate & Ingest SBOMs", "CycloneDX out, CycloneDX or SPDX in", "CycloneDX 1.4 export. Ingestion not documented"),
    50: ("Track Vulnerable Components", "CVEs, licenses, outdated versions per component", "Packages with CVEs and top severity"),
    51: ("Continuous CVE Monitoring", "Live NVD feed, daily EPSS and CISA KEV", "Intelligence Stream, several updates daily"),
    16: ("AWS", "CSPM, CDR auto-fix, inventory, GovCloud", "CSPM, runtime security, DSPM"),
    17: ("Azure", "CSPM, org-level onboarding, CDR auto-fix", "CSPM, runtime security, DSPM"),
    18: ("GCP", "CSPM, CDR auto-fix, CIS GCP benchmarks", "CSPM, runtime security, DSPM"),
    19: ("Multi-Cloud Asset Inventory", "One inventory of accounts, assets, workloads", "AWS, Azure, GCP, OCI, Alibaba. 24h refresh SLA"),
    20: ("Private Cloud (OpenShift / Nutanix)", "OpenShift, Nutanix, VMware Tanzu enforcement", "OpenShift v4. Nutanix not listed"),
    6: ("Secrets in S3 / Filesystems", "S3, filesystems, Hugging Face datasets", "Host and image filesystems. S3 undocumented"),
    40: ("Public S3 Detection + Auto-Fix", "CloudTrail detection, reverts bucket to private", "Config policy plus CLI auto-remediation"),
    41: ("Real-Time Cloud Event Automation", "Real-time CloudTrail alerts trigger remediation", "Audit events alert only, can lag hours. No CLI auto-fix"),
    24: ("Host Protection (VM, Bare Metal)", "KubeArmor systemd mode on VMs, bare metal", "Host Defenders, Linux and Windows"),
    25: ("Container & K8s Runtime", "Process, file, network enforcement + microsegmentation", "Learned models, Alert, Prevent, Block rules"),
    26: ("Preemptive / Inline Blocking", "Kernel LSM stops a process before it runs", "Prevent effect stops a disallowed process"),
    43: ("eBPF / Kernel Enforcement", "eBPF plus AppArmor, SELinux, BPF-LSM", "User-space Defender. No eBPF in docs"),
    28: ("Process Allow / Deny", "Per-pod or per-host process policies", "Allow and deny lists, Prevent or Block"),
    29: ("File Integrity Monitoring", "Monitors and blocks critical path changes", "Host FIM. Container write Prevent by directory"),
    30: ("Workload Anomaly Detection", "Learns baseline, blocks deviations", "1h learning, 24h dry run, rule enforcement"),
    31: ("Fileless Malware Protection", "Allow-list blocks unknown processes", "[confirm from Prisma Cloud docs]"),
    27: ("Continuous Image Scanning", "Scheduled scans of running images", "Registry, CI, deployed images, several times daily"),
    35: ("Trusted Registry Enforcement", "KnoxGuard admission per cluster or namespace", "Trusted Images, alert or block"),
    32: ("K8s Misconfiguration", "Findings with fix steps and Jira tickets", "CIS checks plus OPA admission rules"),
    33: ("K8s CIS Benchmarks", "Scheduled Helm-installed CIS scanner", "CIS K8s, EKS, AKS, GKE, OpenShift"),
    34: ("KIEM (K8s Entitlements)", "RBAC search, graph, 15 risk queries", "CIEM is cloud IAM only. No K8s RBAC"),
    36: ("Service Account Inventory", "Service accounts, roles, bindings per cluster", "No K8s identity inventory documented"),
    37: ("Over-Permission Detection", "Flags principals with excess privileges", "Cloud IAM only. K8s RBAC not documented"),
    38: ("Risky Bindings & Cluster-Admin", "Flags roles that modify workloads or read secrets", "Audit-event alerts. No binding analysis"),
    39: ("Stale K8s Entitlements", "Unused roles and orphan service accounts", "Cloud IAM only. K8s not documented"),
    44: ("North-South (NGINX Ingress)", "NGINX Ingress connector feeds API inventory", "WAAS per app. No NGINX ingress integration"),
    45: ("TLS Classification at Ingress", "Inspects TLS, flags misconfigurations", "Decrypts per endpoint. No TLS report"),
    46: ("Sensitive Data in APIs", "Request and response data classification", "Flags card, PII and session data"),
    47: ("Shadow API Detection", "Traffic vs OpenAPI spec", "Detects shadow APIs. OpenAPI import"),
    48: ("Zombie API Detection", "Zombie and orphan APIs vs spec", "Last-seen dates only. No zombie detection"),
    52: ("Data Discovery", "S3, Blob, cloud and self-hosted DBs, Drive, Salesforce", "AWS, Azure, GCP, Snowflake, M365, file shares"),
    53: ("Data Classification", "283 classes, PII, PHI, PCI, secrets, 62 country packs", "Predefined and custom classifiers"),
    54: ("Data Access Verification", "Coming soon", "Read, Write, List, Manage and public access map"),
    55: ("Publicly Exposed Data", "Flags public buckets, CDR makes them private", "Public access flagged by risk rules"),
    56: ("Data Policy Controls", "Coming soon", "Built-in and custom risk rules, DDR alerts"),
    57: ("Compliance Frameworks", "33+ frameworks, 42 versions, ISO, NIST, PCI, SOC 2", "60+ standards for AWS, plus 4 clouds, custom"),
    58: ("Compliance Reports", "Audit-ready PDF, CSV, JSON", "One-time or recurring, emailed"),
    23: ("Findings Reporting", "Deduplicated across CSPM, KSPM, ASPM, runtime", "Alert, compliance and Command Center reports"),
    42: ("Audit Trail", "EventTrail logs who, when, result", "120-day platform audit log"),
    59: ("Findings Collaboration", "Jira, ServiceNow, Zendesk + 2, PDF/CSV/JSON", "Jira, email, Slack, CSV, snooze"),
    60: ("LLM Red Teaming", "Bedrock, Vertex AI, AI Foundry, Triton, vLLM", "Not in Enterprise Edition. Sold as Prisma AIRS"),
    61: ("Prompt Firewall", "Inline: blocks, masks or logs prompts and responses", "Not in Enterprise Edition. Sold as Prisma AIRS"),
    62: ("ML Model Scanning", "Pickle, Keras H5, SavedModel, ONNX", "Finds Hugging Face files. Scanning is AIRS"),
    63: ("OWASP LLM Top 10", "v2025 mapped in AI-SPM and red teaming", "Posture findings mapped. No runtime control"),
    64: ("AI/ML Runtime Sandboxing", "ModelArmor sandboxes models and agents", "Generic runtime defense. No AI sandbox"),
    65: ("AI Model & Dataset Exposure", "Detects public endpoints, makes them private", "Detects exposure. No blocking"),
    66: ("Unknown-Region Model Access", "Alerts outside allowed regions", "Generic UEBA location alerts"),
    67: ("SIEM", "Splunk, Sentinel, QRadar, Sumo Logic, rsyslog", "Splunk HEC, Security Lake, webhooks, SQS"),
    68: ("Bi-Directional Ticketing", "Ticket closes finding, recurrence reopens it", "One-way push to Jira, ServiceNow"),
}

# Rows folded into another row. The kept row inherits both sets of sources.
FOLD = {22: 57, 21: 41}

GROUPS = [
    ("Deployment Models", [1, 2, 3, 4]),
    ("Application Security", [14, 15, 9, 10, 11, 5, 7, 12, 13]),
    ("Software Supply Chain", [8, 49, 50, 51]),
    ("Cloud Security Posture", [16, 17, 18, 19, 20, 6, 40, 41]),
    ("Workload & Kubernetes Runtime", [24, 25, 26, 43, 28, 29, 30, 31, 27, 35, 32, 33]),
    ("Kubernetes Identity (KIEM)", [34, 36, 37, 38, 39]),
    ("API Security", [44, 45, 46, 47, 48]),
    ("Data Security (DSPM)", [52, 53, 54, 55, 56]),
    ("Compliance & Reporting", [57, 58, 23, 42, 59]),
    ("AI Security", [60, 61, 62, 63, 64, 65, 66]),
    ("Integrations", [67, 68]),
]

used = sorted([n for _, ns in GROUPS for n in ns] + list(FOLD))
assert used == list(range(1, 69)), "every live row must be grouped or folded"

out = []
for title, ns in GROUPS:
    rows = []
    for n in ns:
        r = dict(ROW[n])
        for src, dst in FOLD.items():
            if dst == n:
                r["ak_src"] = list(dict.fromkeys(r["ak_src"] + ROW[src]["ak_src"]))
                r["pc_src"] = list(dict.fromkeys(r["pc_src"] + ROW[src]["pc_src"]))
        p, a, c = SHORT[n]
        r.update(param=p, ak=a, pc=c)
        rows.append(r)
    out.append({"title": title, "rows": rows})

(D / "groups.json").write_text(json.dumps(out, indent=1, ensure_ascii=False), encoding="utf-8")
print(sum(len(g["rows"]) for g in out), "rows in", len(out), "groups")
