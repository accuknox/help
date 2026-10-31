"""Simplified content for the AccuKnox vs Wiz, Palo Alto Networks and SentinelOne CNAPP comparison.

One short line per cell. Every line carries evidence as (source id, exact phrase).
validate_evidence.py checks each phrase against the saved page under research/raw/.
A cell with no text is "Not compared": it makes no claim about the vendor.

Win keys per competitor cell: ak AccuKnox leads, par matches, comp shown neutral, nc not compared.
"""
from cnapp_sources import READ_DATE, SOURCES  # noqa: F401

GROUPS = [
    ("A", "Cloud posture"),
    ("B", "Data and AI security"),
    ("C", "Code scanning and CI/CD"),
    ("D", "Runtime protection"),
]


def b(text, *ev):
    return {"t": text, "ev": list(ev)}


def c(win, text="", *ev):
    return {"win": win, "t": text, "ev": list(ev)}


ROWS = [
    {"g": "A", "cap": "Agentless cloud posture", "icon": "cloud",
     "ak": c("", "Agentless, read-only, AWS and Azure", ("ak_cspm", "CSPM is agentless and uses cloud APIs"), ("ak_cspm", "supports AWS, Azure, and GCP")),
     "wz": c("par", "Agentless, 2,800+ configuration rules", ("wz_cspm", "Wiz connects in minutes using CSP's APIs"), ("wz_cspm", "2,800+ cloud configuration rules, including KSPM rules")),
     "pa": c("par", "Agentless posture in Cortex Cloud", ("pa_lic", "Agentless comprehensive visibility across your cloud environment")),
     "s1": c("par", "Agentless, 2,000+ built-in policies", ("s1_cspm", "2,000+ built-in policy assessments"))},
    {"g": "A", "cap": "Compliance frameworks", "icon": "list",
     "ak": c("", "33+ frameworks", ("ak_comp", "33+ compliance frameworks")),
     "wz": c("comp", "100+ frameworks", ("wz_comp", "100+ Built-In Frameworks")),
     "pa": c("par", "Built-in and custom standards", ("pa_comp", "built-in and custom standards")),
     "s1": c("par", "CIS, SOC 2, NIST, EU AI Act", ("s1_cspm", "CIS, SOC 2, the EU AI Act, and NIST"))},
    {"g": "A", "cap": "Attack-path context", "icon": "graph",
     "ak": c("", "Security Graph on AWS and Azure findings", ("ak_36", "asset to asset, and asset to finding"), ("ak_36", "It covers cloud findings on AWS, Azure, and GCP")),
     "wz": c("par", "Security Graph, attack paths", ("wz_plat", "Attack path analysis")),
     "pa": c("par", "Graph rules find attack paths", ("pa_graph", "identify risky relationships and attack paths")),
     "s1": c("comp", "Tests which exposures are exploitable", ("s1_cns", "validating which exposures are truly exploitable with the Offensive Security Engine"))},
    {"g": "B", "cap": "Data security (DSPM)", "icon": "db",
     "ak_star": True, "ak": c("", "Scanner runs in your cloud account", ("ak_dspm", "The scanner runs on a machine you own"), ("ak_dspm", "sends only a findings file to the AccuKnox console")),
     "wz": c("par", "Agentless discovery, access governance", ("wz_dspm", "Continuous agentless discovery of your sensitive data"), ("wz_dspm", "Data access management and governance")),
     "pa": c("par", "Included in Cortex Runtime Security", ("pa_data", "Cortex Data Security is included with your Cloud Runtime Security license")),
     "s1": c("par", "DSPM with attack-path context", ("s1_cns", "integrates DSPM with Attack Path Analysis"))},
    {"g": "B", "cap": "AI posture on AWS and Azure", "icon": "brain",
     "ak": c("", "Finds SageMaker, Bedrock, Azure OpenAI", ("ak_ai", "automatically discovers SageMaker endpoints, Bedrock model deployments"), ("ak_ai", "Discovers Azure AI Foundry, Azure OpenAI Service, Copilot Studio agents")),
     "wz": c("par", "AI-BOM finds SageMaker, OpenAI", ("wz_ai", "including managed services such as AWS SageMaker, OpenAI")),
     "pa": c("par", "Cortex AI-SPM inventories models", ("pa_aispm", "See all AI models in your cloud environment")),
     "s1": c("par", "AI models, services, data flows", ("s1_cns", "provides visibility into AI models, services, and data flows"))},
    {"g": "B", "cap": "AI runtime guardrails", "icon": "shield",
     "ak": c("", "Prompt Firewall, ModelArmor, red teaming", ("ak_ai", "Prompt Firewall"), ("ak_ai", "ModelArmor"), ("ak_ai", "Automated Red Teaming")),
     "wz": c("par", "Detects prompt injection at runtime", ("wz_ai", "Detect prompt injection, rogue agents, and malicious behavior targeting AI systems")),
     "pa": c("par", "Prisma AIRS blocks prompt injections", ("pa_airs", "blocks prompt injections and data leaks")),
     "s1": c("par", "Prompt Security AI firewall", ("s1_prompt", "real-time AI firewall"))},
    {"g": "C", "cap": "SAST", "icon": "code",
     "ak_star": True, "ak": c("", "14 languages on two engines", ("ak_sast", "across two scanning engines"), ("ak_sast", "Kotlin")),
     "wz": c("par", "Rule-based and agentic SAST", ("wz_sast", "Wiz combines rule-based and agentic SAST")),
     "pa": c("ak", "No native SAST in Cortex Cloud", ("pa_sast", "Currently, Cortex Cloud does not support native SAST scanners")),
     "s1": c("nc")},
    {"g": "C", "cap": "DAST", "icon": "globe",
     "ak": c("", "Four scan types, AI Pentesting (Beta)", ("ak_dast", "Four scan types are available"), ("ak_dast", "Try AI Pentesting (Beta)")),
     "wz": c("par", "Red Agent includes API DAST, GA", ("wz_red", "API DAST Attacker"), ("wz_red", "is now generally available (GA)")),
     "pa": c("nc"),
     "s1": c("nc")},
    {"g": "C", "cap": "IaC, secrets, SCA, SBOM", "icon": "pipe",
     "ak": c("", "IaC incl. Bicep and ARM, reads CycloneDX and SPDX", ("ak_iac", "Bicep"), ("ak_iac", "Terraform"), ("ak_sbom", "CycloneDX and SPDX")),
     "wz": c("par", "IaC, secrets, SCA and SBOM", ("wz_code", "Secrets Scanning"), ("wz_code", "SCA & SBOM")),
     "pa": c("par", "IaC, SCA, secrets, CycloneDX export", ("pa_tech", "Bicep"), ("pa_sbom", "CycloneDX v1.4 standard")),
     "s1": c("par", "Secrets, IaC and image scans", ("s1_cns", "continuous scanning of repositories, IaC templates, and container images"))},
    {"g": "D", "cap": "Runtime prevention", "icon": "lock",
     "ak_star": True, "ak": c("", "KubeArmor, open source, inline blocking", ("ak_rt", "Inline Mitigation"), ("ak_gen", "CNCF Sandbox project with 2 million+ downloads")),
     "wz": c("par", "eBPF Sensor blocks threats", ("wz_sensor", "The sensor blocks sophisticated cloud and AI threats in real time")),
     "pa": c("par", "Defender blocks or alerts", ("pa_def", "actively blocking or alerting according to the rules defined in Console")),
     "s1": c("par", "eBPF agent, automated response", ("s1_cws", "eBPF-based approach"), ("s1_cws", "automated containment and rollback"))},
    {"g": "D", "cap": "Cloud detection and response", "icon": "pulse",
     "ak": c("", "Reads CloudTrail, auto-remediates", ("ak_cdr", "ingests cloud logs (CloudTrail, Audit Logs)"), ("ak_cdr", "via CI/CD or Webhooks")),
     "wz": c("par", "Wiz Defend reads cloud logs", ("wz_defend", "deep analysis of cloud & SaaS logs")),
     "pa": c("par", "Cortex Runtime Security lists CDR", ("pa_cxrt", "Cloud Detection & Response (CDR)")),
     "s1": c("par", "Hyperautomation for cloud events", ("s1_cns", "Respond to misconfigurations, alerts, and cloud events with pre-built or custom Hyperautomation workflows"))},
    {"g": "D", "cap": "Where the platform runs", "icon": "server",
     "ak_star": True, "ak": c("", "SaaS, on-prem or air-gapped", ("ak_dep", "Full On-premises or Air-gapped")),
     "wz": c("nc", "SaaS, sold on AWS Marketplace", ("wz_mp", "Software as a Service (SaaS)")),
     "pa": c("ak", "Enterprise Edition is SaaS", ("pa_welcome", "SaaS (Prisma Cloud Enterprise Edition)"), ("pa_pclic", "workload protection for hosts, containers, and serverless deployments")),
     "s1": c("nc")},
]

# (module, priority, why, AccuKnox unit, evidence). Priority is a suggestion for the stated scope.
FIT = [
    ("CSPM and KSPM", "Must", "Posture on AWS and Azure is the base ask", "Cloud assets as units", [("ak_price", "Number of cloud assets normalized to units")]),
    ("Runtime protection", "Must", "Continuous runtime protection is in scope", "Worker nodes", [("ak_price", "Number of worker nodes")]),
    ("Code scanning and CI/CD", "Must", "SAST, IaC, secrets and SCA before deploy", "Scanner tools", [("ak_price", "Number of Tools in SCA, SAST, DAST, IaC")]),
    ("DSPM", "Must", "Data security is in scope. Confirm the data stores in the POC", "By quote", []),
    ("DAST and CDR", "Good", "Add once the first three are live", "Scanner tools", [("ak_price", "Number of Tools in SCA, SAST, DAST, IaC")]),
    ("AI security", "Good", "Size it by your GenAI footprint", "AI and LLM models", [("ak_price", "Number of AI/LLM Model")]),
    ("SBOM generation", "Defer", "You already use JFrog. AccuKnox can read CycloneDX and SPDX", "Scanner tools", [("ak_sbom", "CycloneDX and SPDX")]),
]

LICENSE_NOTES = [
    b("AccuKnox: custom quote, pay per module, no hard stop if the quota is exceeded",
      ("ak_price", "custom quote"), ("ak_price", "will not stop you from exceeding the quota")),
    b("Wiz: base plans on AWS Marketplace, with Sensor, Code and Defend as add-ons",
      ("wz_mp", "Wiz Essential"), ("wz_mp", "Add-on for Wiz Advanced"), ("wz_mp", "Add-on for Wiz Cloud")),
    b("Palo Alto, Cortex Cloud: priced per protected workload, code security is an add-on",
      ("pa_lic", "The fundamental metric for consumption is the protected workload"), ("pa_appsec", "Application Security Add-on")),
    b("Palo Alto, Prisma Cloud: priced in credits",
      ("pa_pclic", "Licensing is sold in increments of 100 credits")),
]

WHERE_ACCUKNOX_LEADS = [
    b("SAST: 14 languages natively. Cortex Cloud has no native SAST scanner",
      ("ak_sast", "across two scanning engines"), ("pa_sast", "Currently, Cortex Cloud does not support native SAST scanners")),
    b("Runtime: open-source KubeArmor with inline blocking",
      ("ak_gen", "CNCF Sandbox project with 2 million+ downloads"), ("ak_rt", "Inline Mitigation")),
    b("Data: the DSPM scanner runs in your account and only a findings file leaves",
      ("ak_dspm", "The scanner runs on a machine you own"), ("ak_dspm", "sends only a findings file to the AccuKnox console")),
    b("Deployment: SaaS, on-prem or air-gapped. Prisma Cloud Enterprise Edition is SaaS",
      ("ak_dep", "Full On-premises or Air-gapped"), ("pa_welcome", "SaaS (Prisma Cloud Enterprise Edition)")),
]

POC = [
    ("Posture", "One AWS account and one Azure subscription, read-only.",
     b("", ("ak_cspm", "read-only"), ("ak_36", "CloudFormation"))),
    ("Data and AI", "One S3 bucket and one Blob container. Add AI posture if Bedrock or Azure OpenAI is live.",
     b("", ("ak_dspm_on", "Blob Storage and ADLS Gen2"), ("ak_ai", "Azure OpenAI Service"))),
    ("Code and CI/CD", "One or two repositories: SAST, IaC, secrets, SCA. One JFrog registry.",
     b("", ("ak_aspm", "Secrets Scanning"), ("ak_jfrog", "JFrog"))),
    ("Runtime", "KubeArmor on one non-production cluster or VM, with one block policy.",
     b("", ("ak_rt", "Inline Mitigation"), ("ak_gen", "CNCF Sandbox project with 2 million+ downloads"))),
]
POC_TIMELINE = b("A SaaS proof of concept runs about one to two weeks when the infrastructure is in place",
                 ("ak_dep", "SaaS PoC:"), ("ak_dep", "1–2 weeks"))

PICK = [
    ("code", "Native SAST, DAST, IaC, secrets and SCA",
     [("ak_sast", "across two scanning engines"), ("ak_dast", "Four scan types are available"), ("pa_sast", "Currently, Cortex Cloud does not support native SAST scanners")]),
    ("lock", "Open-source runtime enforcement with KubeArmor",
     [("ak_gen", "CNCF Sandbox project with 2 million+ downloads"), ("ak_rt", "Inline Mitigation")]),
    ("sliders", "Pay per module, run SaaS or on-prem",
     [("ak_price", "Customers only pay for the modules they choose"), ("ak_dep", "Full On-premises or Air-gapped")]),
]

NOTES = {
    "palo": ("Palo Alto Networks sells Prisma Cloud and Cortex Cloud. Its Prisma Cloud page now promotes Cortex Cloud.",
             [("pa_page", "MEET CORTEX CLOUD")]),
    "wiz": ("Google completed its acquisition of Wiz on 11 March 2026. Wiz says it stays multi-cloud.",
            [("wz_google", "Google has completed its acquisition of Wiz"), ("wz_google", "March 11, 2026"), ("wz_close", "Wiz remains a multi-cloud platform")]),
}
