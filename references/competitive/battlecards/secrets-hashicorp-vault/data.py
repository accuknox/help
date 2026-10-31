"""Rows for the AccuKnox vs HashiCorp Vault comparison.

Source: Google Sheet 1Kf5QWIPbu9GZ_oJTNe3TGCPgcvg4gcGnUAweumBnRPA (AccuKnox-vs-HashiCorp-Vault).
Every row was re-read against AccuKnox help docs and HashiCorp's own pages on 2026-10-26.
The README in this folder lists what the sheet claimed that no source supported, and what was cut.
"""

VENDORS = ["AccuKnox", "HashiCorp Vault"]

DOCS = "https://developer.hashicorp.com/vault/docs"
ENT = "https://www.hashicorp.com/en/products/vault/vault-enterprise"


def row(no, name, short, ak, vault, vsrc=None):
    return {
        "no": no,
        "name": name,
        "short": short,
        "cells": [
            {"st": ak[0], "text": ak[1], "src": None},
            {"st": vault[0], "text": vault[1], "src": vsrc},
        ],
    }


def load():
    return [
        {"name": "A. Platform and Compatibility", "rows": [
            row(1, "Vault API Compatibility", "API-compatible with Vault, no major code changes",
                ("Y", "API-compatible with HashiCorp Vault. Existing apps, scripts and tooling keep working with no major code changes."),
                ("Y", "Defines the Vault HTTP API that AccuKnox Secrets Manager matches."),
                "https://developer.hashicorp.com/vault/api-docs"),
            row(2, "Multi-Tenancy and Namespaces", "A namespace per tenant, with its own permissions",
                ("Y", "Each tenant gets a separate namespace with its own permissions, resources and configuration. Dedicated instances support several namespaces."),
                ("P", "Namespaces need a Vault Enterprise license or an HCP Vault Dedicated cluster."),
                f"{DOCS}/enterprise/namespaces"),
            row(3, "Air-Gapped and On-Prem Deployment", "Air-gapped install from an internal registry",
                ("Y", "Install from an internal registry with no internet access, or run a dedicated instance on-prem or air-gapped. LDAP sign-in works offline."),
                ("P", "Vault Enterprise is self-managed for hybrid and on-premises estates. The page does not describe an air-gapped install."),
                ENT),
        ]},
        {"name": "B. Secrets and Encryption Engines", "rows": [
            row(4, "Versioned KV Secrets", "KV version 1 and 2 with versions and rollback",
                ("Y", "KV version 1 and 2 engines hold static secrets, with versions and rollback in version 2."),
                ("Y", "The KV secrets engine stores static secrets, and version 2 keeps versions of each key."),
                f"{DOCS}/secrets/kv"),
            row(5, "Encryption as a Service (Transit)", "Transit engine for encrypt and decrypt",
                ("Y", "The Transit engine encrypts and decrypts values through the API, so apps never hold the key."),
                ("Y", "The Transit secrets engine handles cryptographic functions on data in transit."),
                f"{DOCS}/secrets/transit"),
            row(6, "Certificate Issuance (PKI)", "PKI engine for certificates",
                ("Y", "The PKI engine issues certificates through the same API and policies."),
                ("Y", "The PKI secrets engine generates dynamic X.509 certificates."),
                f"{DOCS}/secrets/pki"),
            row(7, "Dynamic Database Credentials", "Short-lived database credentials",
                ("Y", "The Database engine issues short-lived database credentials."),
                ("Y", "The database secrets engine generates database credentials dynamically."),
                f"{DOCS}/secrets/databases"),
            row(8, "Dynamic Cloud and Kubernetes Credentials", "Short-lived AWS and Kubernetes credentials",
                ("Y", "Dynamic secrets cover AWS and Kubernetes with short-lived credentials."),
                ("Y", "Separate AWS and Kubernetes secrets engines generate credentials on demand."),
                f"{DOCS}/secrets/aws"),
            row(9, "TOTP and SSH Engines", "TOTP codes and one-time SSH passwords",
                ("Y", "The TOTP engine generates and validates 6-digit codes under policy control. An SSH engine issues one-time passwords."),
                ("Y", "The TOTP engine generates and validates time-based codes. The SSH engine covers one-time SSH passwords."),
                f"{DOCS}/secrets/totp"),
        ]},
        {"name": "C. Authentication and Access", "rows": [
            row(10, "Identity Provider Sign-In", "OIDC, LDAP, Okta and username and password",
                ("Y", "People sign in with OIDC (for example Microsoft Entra ID), LDAP, Okta, or a username and password."),
                ("Y", "JWT/OIDC, LDAP and Okta auth methods connect people to an identity provider."),
                f"{DOCS}/auth/jwt"),
            row(11, "Workload and Machine Identity", "Kubernetes, AppRole, TLS certificate and JWT",
                ("Y", "Pods use a Kubernetes service account. VMs, jobs and scripts use AppRole, a TLS certificate or JWT."),
                ("Y", "AppRole and Kubernetes auth methods cover machines and pods."),
                f"{DOCS}/auth/approle"),
            row(12, "Per-Path Access Policies", "Each app reads only its own paths",
                ("Y", "A policy limits each application or teammate to its own paths. A token keeps its old policies until the holder logs in again."),
                ("Y", "ACL policies limit access within Vault and inside each namespace."),
                f"{DOCS}/enterprise/namespaces"),
        ]},
        {"name": "D. Audit, Compliance and Hardening", "rows": [
            row(13, "Audit Logging", "Every request logged, allowed or denied",
                ("Y", "Every request is logged, allowed or denied, and the logs are ready for your SIEM."),
                ("Y", "Audit devices record API requests and responses. Auditing stays off until you enable a device."),
                f"{DOCS}/audit"),
            row(14, "Audit Logs Into SIEM and CDR", "Direct feed to AccuKnox SIEM and CDR",
                ("Y", "Dedicated instances integrate directly with AccuKnox SIEM and CDR."),
                ("P", "Audit devices write to a file, a syslog server or a socket."),
                f"{DOCS}/audit"),
            row(15, "Runtime Hardening of the Server", "CWPP hardens every pod at runtime",
                ("Y", "AccuKnox CWPP, built on KubeArmor, hardens every Secrets Manager pod at runtime. It limits what processes in the pods can read and run."),
                ("P", "Vault publishes baseline and extended production hardening recommendations. Your team applies them."),
                f"{DOCS}/concepts/production-hardening"),
            row(16, "Compliance Reporting", "Compliance reports and a secrets health dashboard",
                ("Y", "Real-time audit logs, compliance reporting and a dashboard for secrets health and status."),
                ("Y", "Vault Enterprise lists multi-level access controls, customizable audit logs, and FIPS 140-2 and SOC 2 support."),
                ENT),
        ]},
        {"name": "E. Delivery and Operations", "rows": [
            row(17, "Kubernetes Delivery", "Agent Injector and External Secrets Operator",
                ("Y", "The Agent Injector and External Secrets Operator deliver secrets to pods, and the Operator needs no app code change."),
                ("Y", "Vault Enterprise lists OpenShift OLM, sidecar injection, a CSI provider and Vault Operator."),
                ENT),
            row(18, "High Availability and Backup", "Three nodes and snapshots every 15 minutes",
                ("Y", "Three nodes run in high availability mode on all instances. A snapshot agent saves to S3-compatible storage every 15 minutes by default."),
                ("Y", "Vault runs multiple servers in high availability mode to protect against outages."),
                f"{DOCS}/internals/high-availability"),
            row(19, "Managed Instances", "Shared or dedicated, in four regions",
                ("Y", "Shared or dedicated managed instances in North America, Europe, the Middle East and India."),
                ("Y", "HCP Vault Dedicated is the hosted option."),
                f"{DOCS}/enterprise/namespaces"),
        ]},
    ]
