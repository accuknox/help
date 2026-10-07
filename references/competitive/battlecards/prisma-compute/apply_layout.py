"""Build data/rows.json-free layout: groups.json, sources.json and page.json for the Compute Edition PDF.

Prisma cells come from research/rows-A..D.json (Compute Edition docs, read 2026-10-06).
AccuKnox cells come from research/accuknox-rows-ee-run.json, plus the new rows in rows-A.json.
Row numbers 1 to 68 are the live-page numbers. Rows 100 to 105 are new on-prem rows.

    python references/competitive/battlecards/prisma-compute/apply_layout.py
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
R = HERE / "research"
D = HERE / "data"
D.mkdir(exist_ok=True)

ICON = {"Supported": "tick", "Limited": "dash", "Not supported": "cross", "No equivalent": "cross"}
ARCH = "https://docs.prismacloud.io/admin-guide/welcome/product-architecture"
DEPLOY = "https://help.accuknox.com/resources/deployment/"

pc, newrows = {}, {}
for k in "ABCD":
    for r in json.loads((R / f"rows-{k}.json").read_text(encoding="utf-8")):
        pc[r["n"]] = r
ak = {r["n"]: r for r in json.loads((R / "accuknox-rows-ee-run.json").read_text(encoding="utf-8"))}

# Rows that exist only for the Compute Edition page.
EXTRA = {
    100: dict(
        param="Modules Available On-Prem",
        ak="All features run on-prem except AI CoPilot (AskADA)", ak_urls=[DEPLOY],
        pc_status="Limited", pc="CWPP module only. CSPM is in Enterprise Edition (SaaS)", pc_url=ARCH,
    ),
}

# n: (parameter, AccuKnox cell or None, Prisma cell or None). None keeps the researched text.
# Order inside each group is the print order.
GROUPS = [
    ("Deployment and Data Residency", [
        (100, None, None, None),
        (101, "On-Prem Control Plane", "Native install on your servers, VMs or bare metal", None),
        (102, "Air-Gapped Operation", "Isolated network with no call-home, images staged in own registry", "Listed for air-gapped sites, with manual threat feed loading"),
        (104, "Data Residency and Telemetry", "No data egress on-prem. Control plane pulls image and chart updates", "Data stays on your Console. Anonymous telemetry on by default, can be off"),
        (105, "Multi-Tenancy", "Each tenant runs in its own K8s namespace", "Projects: one Console per tenant behind a central Console"),
    ]),
    ("Application Security", [
        (5, "Secrets (Repo / IaC)", "Repos, pipelines, IaC, correlated in ASPM", "Secrets in images, containers, hosts. Not in repos or IaC files"),
        (9, "Code Quality (Best Practices)", "2-engine SAST, 14 languages, SonarQube gates", "Repo scans check package dependencies only. No source code analysis"),
        (14, "SAST", "Pipeline and IDE SAST", "No SAST scanner. CWPP module only"),
        (15, "DAST", "4 scan types, incl. authenticated behind MFA", "No DAST scanner. WAAS protects running web apps and APIs"),
        (12, "SARIF Ingestion", "Any tool: Checkmarx, JFrog, Gitleaks, Sonatype", "No SARIF import. CWPP module only"),
        (13, "Repo / CI/CD Integration", "GitHub, GitLab, Bitbucket + 9 CI/CD platforms", "Jenkins plugin plus twistcli for other CI. No repo-host apps"),
        (11, "Container Scanning", "CI/CD, registry, in-cluster, deploy blocking", "Image CVE scans in CI, 13 registry types, deployed images"),
        (49, "Generate & Ingest SBOMs", "CycloneDX out, CycloneDX or SPDX in", "Exports CycloneDX 1.4. No SBOM import"),
    ]),
    ("Cloud Security Posture", [
        (16, "CSPM (AWS, Azure, GCP)", "CSPM on all 3 clouds with CDR auto-remediation", "No CSPM. CWPP module only"),
        (19, "Multi-Cloud Asset Inventory", "One inventory of accounts, assets, workloads", "Discovers VMs, K8s, registries, serverless on 3 clouds"),
        (20, "Private Cloud (OpenShift / Nutanix)", "OpenShift, Nutanix, VMware Tanzu enforcement", "OpenShift 4.12 to 4.22 and Tanzu. Nutanix not listed"),
        (21, "Real-Time Cloud Event Automation", "CDR alerts on CloudTrail events, triggers remediation", "No cloud audit-event alerting. CWPP module only"),
        (57, "Compliance Frameworks", "42 benchmarks incl. ISO 27001, NIST, CIS, PCI, SOC 2, HIPAA", "8 CIS benchmarks plus PCI DSS, HIPAA, NIST 800-190, GDPR, DISA STIG"),
    ]),
    ("Workload and Kubernetes Runtime", [
        (25, "Container & K8s Runtime", "Process, file, network enforcement + microsegmentation", "Learned models and rules with Alert, Prevent, Block"),
        (26, "Preemptive / Inline Blocking", "Kernel LSM stops a process before it runs", "Prevent stops the violating process. Block stops the container"),
        (43, "eBPF / Kernel Enforcement", "eBPF plus AppArmor, SELinux, BPF-LSM", "Linux Defender runs in user space, not as a kernel module. eBPF not named"),
        (28, "Process Allow / Deny", "Per-pod or per-host process policies", "Allowed and denied process lists per rule"),
        (29, "File Integrity Monitoring", "Monitors and blocks critical path changes", "Host FIM. Container writes block by directory"),
        (30, "Workload Anomaly Detection", "Learns baseline, blocks deviations", "Learned models, 1h learning, 24h dry run"),
        (32, "K8s Misconfiguration", "Findings with fix steps and Jira tickets", "CIS node checks plus OPA admission rules"),
        (35, "Trusted Registry Enforcement", "KnoxGuard admission per cluster or namespace", "Trusted Images rules. Alert or block"),
    ]),
    ("Kubernetes Identity (KIEM)", [
        (34, "KIEM (K8s Entitlements)", "RBAC search, graph, 15 risk queries", "Alerts on K8s audit events only. No RBAC entitlement analysis"),
        (36, "Service Account Inventory", "Service accounts, roles, bindings per cluster", "No K8s RBAC or service account inventory. CWPP only"),
        (37, "Over-Permission Detection", "Flags principals with excess privileges", "No RBAC privilege analysis. CWPP only"),
        (38, "Risky Bindings & Cluster-Admin", "Flags roles that modify workloads or read secrets", "Custom audit rules alert on events. No binding risk analysis"),
        (39, "Stale K8s Entitlements", "Unused roles and orphan service accounts", "No stale entitlement analysis. CWPP only"),
    ]),
    ("API Security", [
        (44, "North-South (NGINX Ingress)", "NGINX Ingress connector feeds API inventory", "WAAS inspects at the app container. No ingress connector documented"),
        (45, "TLS Classification at Ingress", "Inspects TLS, flags misconfigurations", "Per-endpoint TLS with a supplied certificate. No TLS report"),
        (47, "Shadow API Detection", "Traffic vs OpenAPI spec", "WAAS alerts or blocks paths missing from the imported spec"),
        (48, "Zombie API Detection", "Zombie and orphan APIs vs spec", "Last-seen date per endpoint. No zombie API flag"),
    ]),
    ("Data Security (DSPM)", [
        (52, "Data Discovery", "S3, Blob, cloud and self-hosted DBs, Drive, Salesforce", "No DSPM. CWPP module only"),
        (53, "Data Classification", "283 classes, PII, PHI, PCI, secrets, 62 country packs", "No data classification. CWPP module only"),
    ]),
    ("AI Security", [
        (60, "LLM Red Teaming", "Bedrock, Vertex AI, AI Foundry, Triton, vLLM", "No AI security module. CWPP module only"),
        (61, "Prompt Firewall", "Inline: blocks, masks or logs prompts and responses", "No prompt firewall. CWPP module only"),
        (63, "OWASP LLM Top 10", "v2025 mapped in AI-SPM and red teaming", "No OWASP LLM Top 10 mapping. CWPP module only"),
        (64, "AI/ML Runtime Sandboxing", "ModelArmor sandboxes models and agents", "Generic runtime defense. No AI-specific sandbox"),
    ]),
    ("Integrations", [
        (68, "Bi-Directional Ticketing", "Ticket closes finding, recurrence reopens it", "Alerts create Jira issues and ServiceNow incidents. Push only"),
    ]),
]

# AccuKnox sources for the combined CSPM row (3 clouds).
AK_SRC_OVERRIDE = {
    16: ["https://help.accuknox.com/use-cases/cloud/aws/", "https://help.accuknox.com/how-to/azure-org-onboard/", "https://help.accuknox.com/use-cases/cloud/gcp/"],
    14: ["https://help.accuknox.com/getting-started/3.4-release/"],
}

sources, seen = [], {}


def title_for(url):
    tail = url.rstrip("/").split("/")[-1].replace("-", " ")
    if "help.accuknox.com" in url:
        return "AccuKnox Help, " + tail.capitalize()
    if "docs.prismacloud.io" in url:
        return "Prisma Cloud Compute Edition docs, " + tail
    if "paloaltonetworks.com" in url:
        return "Palo Alto Networks, " + tail
    return "AccuKnox, " + tail


def sid(url):
    if url not in seen:
        seen[url] = f"s{len(seen) + 1}"
        sources.append({"id": seen[url], "title": title_for(url), "url": url})
    return seen[url]


groups, missing = [], []
for title, items in GROUPS:
    rows = []
    for n, param, ak_text, pc_text in items:
        if n in EXTRA:
            e = EXTRA[n]
            rows.append({
                "param": e["param"], "ak_icon": "tick", "ak": e["ak"], "ak_src": [sid(u) for u in e["ak_urls"]],
                "pc_icon": ICON[e["pc_status"]], "pc": e["pc"], "pc_src": [sid(e["pc_url"])],
            })
            continue
        p = pc[n]
        if n in ak:
            a = ak[n]
            ak_status, ak_url, ak_cell = a["status"], a["url"], a["ak_new"]
        else:
            ak_status, ak_url, ak_cell = p["ak_status"], p["ak_url"], p["ak_new"]
        ak_urls = AK_SRC_OVERRIDE.get(n, [ak_url])
        if ak_status != "Supported":
            missing.append((n, "AccuKnox status " + ak_status))
        rows.append({
            "param": param or p["param"],
            "ak_icon": ICON[ak_status], "ak": ak_text or ak_cell, "ak_src": [sid(u) for u in ak_urls],
            "pc_icon": ICON[p["status"]], "pc": pc_text or p["pc_new"], "pc_src": [sid(p["url"])],
        })
    groups.append({"title": title, "rows": rows})

PAGE = {
    "title": "AccuKnox vs Prisma Cloud Compute Edition",
    "accessed": "2026-10-06",
    "h2": "Workloads On-Prem With Prisma. Everything On-Prem With AccuKnox.",
    "intro": (
        "Prisma Cloud Compute Edition is the self-hosted edition of Prisma Cloud. It includes the Cloud Workload "
        "Protection Platform (CWPP) module only. Cloud posture sits in Prisma Cloud Enterprise Edition, which Palo Alto "
        "Networks runs as SaaS. AccuKnox installs its control plane on your servers or in an air-gapped network. "
        "It runs every feature there except AI CoPilot (AskADA)."
    ),
    "intro_src_urls": [ARCH, "https://docs.prismacloud.io/admin-guide/welcome/pcee-vs-pcce", DEPLOY],
    "edition_tag": "Compared with Prisma Cloud Compute Edition (self-hosted), per its administrator guide read on 2026-10-06.",
    "edition_src_urls": ["https://docs.prismacloud.io/admin-guide/welcome/getting-started"],
    "why_h2": "Why Customers Choose AccuKnox Over Prisma Cloud Compute Edition",
    "why_cards": [
        {
            "title": "Better",
            "body": (
                "AccuKnox covers code, cloud, Kubernetes, data and AI from one on-prem control plane. "
                "Compute Edition covers workloads, and its docs list no SAST, DAST, DSPM or AI security module."
            ),
            "src_urls": [DEPLOY, ARCH],
        },
        {
            "title": "Faster",
            "body": (
                "KubeArmor enforces policy inline at the kernel, so a disallowed process stops before it runs. "
                "The Compute Edition Linux Defender runs in user space. At one of India's top 3 public sector banks, "
                "AccuKnox cut remediation time by 91% and false positives by 89%."
            ),
            "src_urls": [
                "https://help.accuknox.com/faqs/runtime-security/",
                "https://docs.prismacloud.io/admin-guide/technology-overviews/host-defender-architecture",
                "https://accuknox.com/wp-content/uploads/SBOM-Case-Study.pdf",
            ],
        },
        {
            "title": "Affordable",
            "body": (
                "One AccuKnox platform includes SAST, DAST, DSPM and AI security on-prem. Compute Edition licenses "
                "each protected host, container host and function with credits, and covers workload protection only."
            ),
            "src_urls": [DEPLOY, "https://docs.prismacloud.io/admin-guide/welcome/licensing"],
        },
    ],
    "sources_note": (
        "Prisma Cloud facts come from the Prisma Cloud Compute Edition administrator guide at docs.prismacloud.io, "
        "read on 2026-10-06. AccuKnox facts come from help.accuknox.com and one published AccuKnox case study. "
        "Palo Alto Networks also sells Prisma Cloud Enterprise Edition (SaaS) and Cortex Cloud, and their "
        "capabilities differ from this table."
    ),
}

for u in PAGE["intro_src_urls"] + PAGE["edition_src_urls"] + [u for c in PAGE["why_cards"] for u in c["src_urls"]]:
    sid(u)
for s in sources:
    if s["url"].endswith("SBOM-Case-Study.pdf"):
        s["title"] = "AccuKnox case study, Top 3 Indian public sector bank operationalises SBOM air-gapped"

(D / "groups.json").write_text(json.dumps(groups, indent=1, ensure_ascii=False), encoding="utf-8")
(D / "sources.json").write_text(json.dumps(sources, indent=1, ensure_ascii=False), encoding="utf-8")
(D / "page.json").write_text(json.dumps(PAGE, indent=1, ensure_ascii=False), encoding="utf-8")
print(sum(len(g["rows"]) for g in groups), "rows,", len(sources), "sources; AccuKnox flags:", missing)
