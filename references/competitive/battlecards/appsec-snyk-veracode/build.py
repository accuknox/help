"""AppSec comparison set: AccuKnox vs Snyk, Veracode and Checkmarx.

    python build.py          # writes the PDFs and *.meta.json into this folder via the shared engine

Data comes from the Google Sheet export in this folder (see data.py and README.md).
"""

import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent.parent / "pdf-engine"))

import data  # noqa: E402
import engine  # noqa: E402

SECTIONS = data.load()

AK_REFS = {
    "A": [("ASPM overview", "/how-to/aspm-overview/"), ("Findings lifecycle", "/how-to/findings-lifecycle/"), ("Rules Engine", "/use-cases/rules-engine-ticket-creation/"), ("RBAC and multi-tenancy", "/resources/multitenancy/"), ("Audit trail", "/getting-started/audit-trail-logs/")],
    "B": [("SAST with Opengrep", "/use-cases/sast-sq/"), ("GitHub SAST", "/integrations/github-sast/"), ("Secret scanning", "/use-cases/github-secret-scan/")],
    "C": [("DAST scan types", "/how-to/dast-scan-types/"), ("MFA-enabled DAST", "/use-cases/mfa-dast/"), ("Authenticated DAST", "/use-cases/dast-authenticated/")],
    "D": [("SBOM getting started", "/getting-started/sbom/"), ("SBOM FAQs", "/faqs/sbom/")],
    "E": [("Registry overview", "/how-to/registry-overview/"), ("Registry support matrix", "/support-matrix/registry/")],
    "F": [("API security use cases", "/use-cases/aspm/")],
    "G": [("Runtime security architecture", "/getting-started/runtime-sec-arch/"), ("KubeArmor support matrix", "/support-matrix/kubearmor-support-matrix/")],
    "H": [("Compliance FAQs", "/faqs/"), ("Sample ASPM report", "/use-cases/aspm-report-sample.pdf")],
    "I": [("Enterprise architecture", "/getting-started/accuknox-arch/")],
    "J": [("AI-BOM static scans", "/how-to/llm-static-scan/"), ("DevSecOps guide", "/getting-started/devsecops/")],
    "K": [("Findings lifecycle", "/how-to/findings-lifecycle/")],
    "L": [("Jira Cloud", "/integrations/jira-cloud/"), ("ServiceDesk Plus", "/integrations/servicedesk-plus/")],
}

COMP_SOURCES = {
    1: ("Snyk", [
        ("Risk and prioritization (AppRisk)", "https://docs.snyk.io/scan-fix-and-prevent/prevent/manage-risk"),
        ("Audit logs API", "https://docs.snyk.io/developer-tools/snyk-api/reference/audit-logs"),
        ("Supported languages", "https://docs.snyk.io/supported-languages/supported-languages-package-managers-and-frameworks"),
        ("IaC custom rules", "https://docs.snyk.io/scan-fix-and-prevent/scan-with-snyk/snyk-iac/current-iac-custom-rules"),
        ("Snyk Secrets", "https://snyk.io/product/snyk-secrets/"),
        ("Snyk API & Web (DAST)", "https://snyk.io/product/dast-api-web/"),
        ("DAST built-in scan profiles", "https://docs.snyk.io/scan-fix-and-prevent/scan-with-snyk/snyk-api-web/start-scanning/overview-scan-settings/built-in-scan-profiles"),
        ("DAST 2FA with TOTP", "https://developers.probely.com/api/tutorials/target-authentication/how-to-setup-2fa-totp-target-login-form/"),
        ("SBOM CLI command", "https://docs.snyk.io/developer-tools/snyk-cli/commands/sbom"),
        ("Container registry integrations", "https://docs.snyk.io/scan-fix-and-prevent/scan-with-snyk/snyk-container/container-registry-integrations"),
        ("IDE plugins and extensions", "https://docs.snyk.io/developer-tools/integrations/snyk-ide-plugins-and-extensions"),
        ("CI/CD integrations", "https://docs.snyk.io/developer-tools/integrations/snyk-ci-cd-integrations"),
    ]),
    2: ("Veracode", [
        ("Veracode Risk Manager", "https://docs.veracode.com/r/Veracode_Risk_Manager"),
        ("Supported languages", "https://docs.veracode.com/r/r_supported_table"),
        ("Security policies", "https://docs.veracode.com/r/c_appsec_policies"),
        ("Reporting REST API", "https://docs.veracode.com/r/Reporting_REST_API"),
        ("SBOM generation", "https://docs.veracode.com/r/veracode_sbom"),
        ("Dynamic Analysis", "https://docs.veracode.com/r/veracode_dynamic"),
        ("Container, IaC and secrets scanning", "https://docs.veracode.com/r/Veracode_Container_Security"),
        ("Discover external assets", "https://docs.veracode.com/r/Discover_external_assets"),
        ("IDE plugins", "https://docs.veracode.com/r/IDEs"),
        ("CI/CD integrations", "https://docs.veracode.com/r/c_integration_buildservs"),
    ]),
}

STRENGTHS = {
    1: [
        ("IDE reach.", "Snyk ships plugins for VS Code, JetBrains, Eclipse and Visual Studio with real-time inline findings and fix suggestions. AccuKnox covers VS Code, Cursor and IntelliJ."),
        ("Developer fix flow.", "Snyk's pull-request fixes and upgrade-path guidance for open source dependencies are a core strength."),
        ("Native DAST.", "Snyk API & Web is a native DAST engine with four built-in scan profiles and TOTP 2FA login support."),
    ],
    2: [
        ("DAST maturity.", "Veracode runs a SaaS Dynamic Analysis engine with about two decades of signature refinement and a claimed sub-1% false-positive rate."),
        ("Suppression governance.", "The Mitigation Approver workflow requires sign-off on every suppression."),
        ("Compliance reporting.", "Long-standing PCI DSS and OWASP reporting, with audit-ready mitigation trails."),
    ],
}

THEMES = [
    ("Inline runtime enforcement", "Kernel-level blocking through KubeArmor, a CNCF sandbox project, with eBPF and LSM. Runtime telemetry ties back to build-time findings.", (30, 31, 32, 33)),
    ("Air-gapped on your terms", "Full on-prem and air-gapped deployment, isolated registry scanning and customer-run vulnerability database updates.", (23, 39)),
    ("API security from live traffic", "Shadow, Zombie and Orphan API discovery, sensitive-data detection in payloads, gateway integrations and rate limiting.", (24, 27, 28, 29)),
    ("xBOM beyond software", "SBOM, HBOM, CBOM for PQC readiness, QBOM and AI-BOM across 12 BOM use cases, including SLSA provenance.", (43,)),
]


SPEC = {
    "vendors": data.VENDORS,
    "sections": SECTIONS,
    "themes": THEMES,
    "strengths": STRENGTHS,
    "sources": COMP_SOURCES,
    "ak_refs": AK_REFS,
    "tag": "Application security",
    "date": "October 2026",
    "category": "appsec",
    "out_dir": HERE,
    "sheet_url": "https://docs.google.com/spreadsheets/d/1hbJFz14lS7VCQk34PP9wZFCKFYpN2drOlPs_lJkTtVM/edit",
    "scope_vs": "AccuKnox and {name} compared across ASPM, SAST, DAST, SCA and SBOM, containers and registries, API security, runtime protection, compliance, deployment models and integrations.",
    "scope_score": "AccuKnox, Snyk, Veracode and Checkmarx across ASPM, SAST, DAST, SCA and SBOM, containers, API security, runtime, compliance, deployment and integrations.",
    "kick_vs": "Head-to-head comparison",
    "kick_score": "Four vendors · one scorecard",
    "score_title": ["AppSec", "Comparison", "Scorecard"],
    "score_note": (
        "<li><b>Custom SAST rule authoring.</b> Quality gates and severity tuning ship today. Self-service custom rules are on the roadmap. "
        "Snyk and Veracode have no self-service equivalent. Checkmarx does, through CxQL.</li>"
        "<li><b>Capabilities only AccuKnox rates Yes.</b> Runtime enforcement, air-gapped and hybrid deployment, live-traffic API controls and the full xBOM suite.</li>"
    ),
    "score_method_extra": "<li>Checkmarx ratings come from the same review of public documentation.</li>",
    "jobs": [
        {"kind": "score", "file": "accuknox-appsec-comparison-scorecard", "title": "AccuKnox AppSec Comparison Scorecard", "vendors": [0, 1, 2, 3]},
        {"kind": "vs", "file": "accuknox-vs-snyk", "title": "AccuKnox vs Snyk", "vendor": 1},
        {"kind": "vs", "file": "accuknox-vs-veracode", "title": "AccuKnox vs Veracode", "vendor": 2},
    ],
}

if __name__ == "__main__":
    engine.build(SPEC, only=sys.argv[1:] or None)
