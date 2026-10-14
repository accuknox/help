"""Load the comparison sheet export, apply the documented overrides, expose rows.

Source: Google Sheet 1hbJFz14lS7VCQk34PP9wZFCKFYpN2drOlPs_lJkTtVM, tab "Detailed Comparison"
(exported to detailed.json). The detailed tab wins over the "ASPM Comparison" summary tab,
because it carries the explanation behind each rating. Six rows disagreed between the tabs.

OVERRIDES hold every place where the sheet was corrected against a vendor's own public
documentation on 2026-10-13. Each carries its source URL. The build prints them.
"""

import json
import re
from pathlib import Path

HERE = Path(__file__).parent
VENDORS = ["AccuKnox", "Snyk", "Veracode", "Checkmarx"]
SYM = {"✓": "Y", "△": "P", "✗": "N"}

# (vendor index, row number) -> (status, text, source url)
OVERRIDES = {
    (0, 6): ("Y", "Java, Python, RPG, .NET, C/C++, JS/TS, Go, Kotlin, Swift, PHP, Ruby, Scala, Apex and Dart, plus IaC, YAML and Bicep in one scanner.", None),
    (0, 12): ("Y", "Dedicated MFA-enabled DAST generates live TOTP codes mid-scan and tracks Logged In, Logged Out and Fallback session states.", None),
    (0, 43): ("Y", "Full xBOM suite: SBOM, HBOM, CBOM (PQC readiness), QBOM and AI-BOM across 12 BOM use cases, including SLSA provenance.", None),
    (1, 8): ("N", "No self-service custom rule authoring for Snyk Code was found in public docs. Custom rules exist for Snyk IaC.",
             "https://docs.snyk.io/scan-fix-and-prevent/scan-with-snyk/snyk-iac/current-iac-custom-rules"),
    (1, 9): ("Y", "Snyk Secrets is a standalone product. It blocks secrets in the IDE, pull requests and CI/CD.",
             "https://snyk.io/product/snyk-secrets/"),
    (1, 11): ("Y", "Native DAST engine (Snyk API & Web) with four built-in scan profiles: Lightning, Safe, Normal and Full.",
              "https://docs.snyk.io/scan-fix-and-prevent/scan-with-snyk/snyk-api-web/start-scanning/overview-scan-settings/built-in-scan-profiles"),
    (1, 12): ("Y", "Supports login forms protected by 2FA through TOTP configuration on a target.",
              "https://developers.probely.com/api/tutorials/target-authentication/how-to-setup-2fa-totp-target-login-form/"),
    (1, 13): ("Y", "Native DAST engine covers web apps and APIs. Snyk lists 115 vulnerability types specific to APIs.",
              "https://snyk.io/product/dast-api-web/"),
    (1, 14): ("P", "Scheduled and CI-driven rescans. Automatic status progression after a clean rescan was not confirmed in public docs.", None),
    (1, 24): ("P", "Snyk API & Web discovery identifies FQDNs and services in your infrastructure. Live-traffic analysis was not confirmed.",
              "https://snyk.io/product/dast-api-web/"),
    (1, 25): ("Y", "API scanning ingests OpenAPI, Swagger and Postman definitions.",
              "https://snyk.io/product/dast-api-web/"),
    (2, 24): ("P", "Attack-surface discovery covers external assets. Live-traffic API discovery was not confirmed.",
              "https://docs.veracode.com/r/Discover_external_assets"),
    (2, 25): ("Y", "Dynamic Analysis scans REST APIs from a specification file in JSON or YAML.",
              "https://docs.veracode.com/r/veracode_dynamic"),
}

# short AccuKnox phrase per row, used on the four-vendor scorecard
SHORT = {
    1: "Native scanners plus SARIF ingestion, one dedup and lifecycle model",
    2: "CVSS, EPSS, CISA KEV and runtime-verified exploitability",
    3: "Customer-built rules for status, tickets and notifications",
    4: "Custom RBAC, SSO and multi-tenancy",
    5: "EventTrail: actor, action, result, raw JSON drill-down",
    6: "Java, Python, .NET, Go, Swift and more, plus IaC in one scanner",
    7: "9 native CI/CD platforms plus VS Code feedback",
    8: "Quality gates and severity tuning today. Custom rule authoring is on the roadmap",
    9: "Passwords, keys, tokens and private keys in source and config",
    10: "Six sticky statuses that persist until changed",
    11: "Baseline, Standard, Extended and Comprehensive profiles",
    12: "Live TOTP codes mid-scan with session-state tracking",
    13: "SQLi, NoSQLi, CMDi, SSTI, XXE, SSRF, CSRF and more",
    14: "Auto-progress to Fixed on a clean rescan, one-click ticket",
    15: "SPDX 2.3 and CycloneDX export",
    16: "Direct and transitive graph with the exact path to each flaw",
    17: "NVD, CISA KEV, MSRC, GitHub PoC, EPSS and CWE, synced continuously",
    18: "Four license risk classes with CI/CD gating",
    19: "Component diff across versions and scans",
    20: "Docker Hub, ECR, GCR, ACR, JFrog, Harbor, Quay, Nexus",
    21: "CRON schedules, scan-on-save, tag-pattern filters",
    22: "Vulnerabilities, Resources, Sensitive Data and Layers tabs",
    23: "Isolated and self-hosted registries in air-gapped networks",
    24: "Live-traffic discovery of Shadow, Zombie and Orphan APIs",
    25: "OpenAPI, Swagger and Postman. REST and gRPC native",
    26: "Maps to OWASP API Top 10, including BOLA",
    27: "PII, PHI and financial data found in live payloads",
    28: "AWS API Gateway, Istio, Kong, F5, NGINX, Azure APIM",
    29: "Rate-limit policies per user, per IP and global",
    30: "KubeArmor (CNCF sandbox) with eBPF and LSM inline enforcement",
    31: "Kubernetes, VMs, containers, serverless and edge",
    32: "Declarative Zero Trust policies that block lateral movement",
    33: "Runtime telemetry tied to build-time findings",
    34: "35+ prebuilt frameworks: PCI DSS, SOC 2, HIPAA, DPDP and more",
    35: "Timestamped evidence packages in PDF, CSV and JSON",
    36: "Application, business-unit and org dashboards with SLA metrics",
    37: "Full feature set in SaaS",
    38: "Self-hosted, AWS on-prem or hybrid, managed OEM or MSSP",
    39: "Full on-prem and air-gapped, customer-run vulnerability DB updates",
    40: "knoxctl CLI with a native Windows binary, plus Python scanner",
    41: "9 CI/CD platforms with soft-fail and hard-fail gating",
    42: "Full browser console, no CLI needed",
    43: "SBOM, HBOM, CBOM, QBOM and AI-BOM across 12 use cases",
    44: "SAST, DAST, SCA, Container, IaC, Secret and API in one layout",
    45: "CVSS, EPSS and KEV enrichment, filter and group by any field",
    46: "Ask AI explains impact and exploit likelihood on the finding",
    47: "One-click Jira or ServiceNow ticket with mapped priority",
    48: "Slack plus a webhook to Teams, email or any SIEM or SOAR",
    49: "GitHub, GitLab, Jenkins, Azure DevOps, Bitbucket, CircleCI, AWS, Google, Harness",
    50: "Jira Cloud and ServiceNow, plus Rule Engine auto-ticketing",
    51: "VS Code, Cursor and IntelliJ with AI remediation and diff preview",
}


def clean(text: str) -> str:
    text = text.strip()
    text = re.sub(r"^Broadest coverage of the three:\s*", "", text)
    # the sheet uses " : " as a dash. Lowercase next word -> comma, uppercase -> colon.
    text = re.sub(r" : ([a-z])", r", \1", text)
    text = re.sub(r" : ([A-Z0-9])", r": \1", text)
    text = text.replace(" : ", ", ")
    text = re.sub(r"(\d)–(\d)", r" to ", text)
    text = text.replace(" – ", ", ").replace("–", " to ")
    text = text.replace("—", ",")
    text = re.sub(r";\s+([a-z])", lambda m: ". " + m.group(1).upper(), text)
    text = text.replace(";", ".")
    return text


def parse_cell(raw: str):
    raw = raw.strip()
    st = SYM.get(raw[:1], "?")
    body = raw[1:].strip()
    body = re.sub(r"^(Yes|No|Partial)\s*", "", body)
    body = re.sub(r"^[–—-]\s*", "", body)
    return st, clean(body)


def load():
    values = json.load(open(HERE / "detailed.json", encoding="utf-8"))["values"]
    sections, current = [], None
    for r in values[1:]:
        if len(r) == 1:
            current = {"name": r[0].strip(), "rows": []}
            sections.append(current)
            continue
        if len(r) < 6:
            continue
        no = int(r[0])
        cells = []
        for i in range(4):
            st, body = parse_cell(r[2 + i])
            src = None
            if (i, no) in OVERRIDES:
                st, body, src = OVERRIDES[(i, no)]
            cells.append({"st": st, "text": body, "src": src})
        current["rows"].append({"no": no, "name": r[1].strip(), "short": SHORT[no], "cells": cells})
    return sections


def rows(sections):
    return [r for s in sections for r in s["rows"]]


VAL = {"Y": 1.0, "P": 0.5, "N": 0.0}
RANK = {"Y": 2, "P": 1, "N": 0}


def score(sections, v):
    rs = rows(sections)
    return sum(VAL[r["cells"][v]["st"]] for r in rs), len(rs)


def tally(sections, a, b):
    lead = par = trail = 0
    for r in rows(sections):
        x, y = RANK[r["cells"][a]["st"]], RANK[r["cells"][b]["st"]]
        lead += x > y
        par += x == y
        trail += x < y
    return lead, par, trail


if __name__ == "__main__":
    s = load()
    for v in range(4):
        print(VENDORS[v], score(s, v))
    for v in (1, 2, 3):
        print("AK vs", VENDORS[v], tally(s, 0, v))
    for k, (st, t, u) in OVERRIDES.items():
        print("OVERRIDE", VENDORS[k[0]], k[1], st, u)
