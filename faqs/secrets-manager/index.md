---
title: Secrets Management FAQs
description: Frequently asked questions about AccuKnox Secrets Management and secure secret storage.
hide:
  - toc
---

# Secrets Management

??? "**1. What is AccuKnox Secrets Manager and how is it different from Vault?**"
    AccuKnox Secrets Manager is a centralized secret store that is compatible with Vault APIs. It provides secure secret storage, dynamic credentials, transit encryption, PKI, and identity-based access control while enabling easier migration from HashiCorp Vault.

??? "**2. What secret engines and authentication methods are supported?**"
    AccuKnox supports key/value secret storage, dynamic secret issuance, transit encryption, and PKI workflows. Authentication methods include tokens, AppRole, OIDC, LDAP, Okta, Kubernetes auth, and JWT-based identity providers.

??? "**3. Can existing Vault applications work with AccuKnox Secrets Manager without code changes?**"
    In most cases, yes. AccuKnox maintains Vault-compatible APIs, so applications that already use Vault can often point to the new endpoint with minimal changes, preserving existing secret workflows.

??? "**4. How are dynamic secrets and secret rotation handled?**"
    AccuKnox can issue short-lived dynamic credentials for cloud resources, databases, and other services. Leases and renewal policies allow automatic rotation, reducing the risk of credential exposure.

??? "**5. What deployment models and access controls are available?**"
    AccuKnox Secrets Manager supports cloud, on-premises, and air-gapped deployments. It provides tenant namespaces, fine-grained policies, audit logging, and encrypted storage so you can safely manage secrets across teams and environments.
