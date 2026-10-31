"""AccuKnox vs HashiCorp Vault comparison set.

    python build.py          # writes the PDF and its .meta.json into this folder via the shared engine
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
    "A": [("Overview", "/secrets-manager/overview/"), ("Architecture", "/secrets-manager/architecture/"), ("Air-Gapped Deployment", "/secrets-manager/air-gapped/")],
    "B": [("Storing secrets in the KV engine", "/secrets-manager/kv-secrets/"), ("Encryption as a Service", "/secrets-manager/transit/"), ("TOTP Authenticator", "/secrets-manager/totp/")],
    "C": [("Architecture", "/secrets-manager/architecture/"), ("Sharing Secrets in an Organisation", "/secrets-manager/sharing-secrets/")],
    "D": [("Architecture", "/secrets-manager/architecture/"), ("Overview", "/secrets-manager/overview/")],
    "E": [("External Secrets Operator", "/secrets-manager/external-secrets/"), ("Direct SDK and REST API", "/secrets-manager/sdk-integration/"), ("High Availability and Backup", "/secrets-manager/high-availability/"), ("Deployment Guide", "/secrets-manager/deployment/")],
}

D = data.DOCS
COMP_SOURCES = {
    1: ("HashiCorp Vault", [
        ("Vault API documentation", "https://developer.hashicorp.com/vault/api-docs"),
        ("Namespaces and secure multi-tenancy", f"{D}/enterprise/namespaces"),
        ("Audit logging", f"{D}/audit"),
        ("Production hardening", f"{D}/concepts/production-hardening"),
        ("High availability", f"{D}/internals/high-availability"),
        ("Vault Enterprise", data.ENT),
        ("KV secrets engine", f"{D}/secrets/kv"),
        ("Transit secrets engine", f"{D}/secrets/transit"),
        ("PKI secrets engine", f"{D}/secrets/pki"),
        ("Database secrets engine", f"{D}/secrets/databases"),
        ("AWS secrets engine", f"{D}/secrets/aws"),
        ("TOTP secrets engine", f"{D}/secrets/totp"),
        ("JWT/OIDC auth method", f"{D}/auth/jwt"),
        ("AppRole auth method", f"{D}/auth/approle"),
    ]),
}

THEMES = [
    ("Keep the Vault API", "API-compatible with HashiCorp Vault, so existing apps, scripts and tooling keep working with no major code changes.", (1, 17)),
    ("Namespaces in the product", "Every tenant gets a separate namespace with its own permissions, resources and configuration.", (2,)),
    ("Audit logs that reach your SIEM", "Every request is logged, and dedicated instances integrate directly with AccuKnox SIEM and CDR.", (13, 14)),
    ("Hardened at runtime", "AccuKnox CWPP, built on KubeArmor, limits what processes in each Secrets Manager pod can read and run.", (15,)),
    ("Air-gapped on your terms", "Install from an internal registry with no internet access, or run a dedicated instance on-prem or air-gapped.", (3,)),
]

SPEC = {
    "vendors": data.VENDORS,
    "sections": SECTIONS,
    "themes": THEMES,
    "strengths": {},
    "sources": COMP_SOURCES,
    "ak_refs": AK_REFS,
    "tag": "Secrets management",
    "date": "October 2026",
    "category": "secrets-management",
    "out_dir": HERE,
    "sheet_url": "https://docs.google.com/spreadsheets/d/1Kf5QWIPbu9GZ_oJTNe3TGCPgcvg4gcGnUAweumBnRPA/edit",
    "scope_vs": "AccuKnox Secrets Manager and {name} compared across Vault API compatibility, multi-tenancy, secret engines, authentication, audit and SIEM, runtime hardening, compliance, Kubernetes delivery, high availability and deployment options.",
    "kick_vs": "Head-to-head comparison",
    "jobs": [
        {"kind": "vs", "file": "accuknox-vs-hashicorp-vault", "title": "AccuKnox vs HashiCorp Vault", "vendor": 1},
    ],
}

if __name__ == "__main__":
    engine.build(SPEC, only=sys.argv[1:] or None)
