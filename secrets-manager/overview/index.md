---
title: AccuKnox Secrets Manager Overview
description: AccuKnox Secrets Manager stores, rotates, and audits secrets from one place. Start here to deploy it, connect applications, and follow a use case.
---

# AccuKnox Secrets Manager

AccuKnox Secrets Manager gives you one secure place to store, manage, and read passwords, API keys, tokens, certificates, and other credentials. It replaces hardcoded secrets with central storage, scoped access, encryption, and a full audit log. It is API-compatible with HashiCorp Vault and runs on any Kubernetes cluster at version 1.30 or later.

<div class="grid cards" markdown>

-   :material-lock-outline:{ .lg .middle } **One place for every secret**

    ---

    Versioned secrets, encryption keys, certificates and one-time codes, each behind a policy.

-   :material-account-key-outline:{ .lg .middle } **Each app reads only its own paths**

    ---

    Pods, VMs and pipelines prove who they are, then read what their policy allows.

-   :material-file-document-check-outline:{ .lg .middle } **Every request is logged**

    ---

    Allowed and denied calls land in the audit log, ready for your SIEM.

-   :material-shield-check-outline:{ .lg .middle } **Hardened at runtime**

    ---

    AccuKnox CWPP protects every Secrets Manager pod with KubeArmor.

</div>

!!! info "A separate product from the AccuKnox CNAPP platform"
    Secrets Manager ships and installs on its own. You do not need an AccuKnox CNAPP subscription to run it. Contact your AccuKnox point of contact for the Helm chart.

## Deploy and Run Secrets Manager

<div class="grid cards" markdown>

-   :material-sitemap:{ .lg .middle } **[Architecture](architecture.md)**

    ---

    See what runs where and how a request reaches a secret.

-   :material-rocket-launch:{ .lg .middle } **[Deployment Guide](deployment.md)**

    ---

    Install with Helm, then initialize and unseal the server.

-   :material-wifi-off:{ .lg .middle } **[Air-Gapped Deployment](air-gapped.md)**

    ---

    Install from an internal registry with no internet access.

-   :material-server-network:{ .lg .middle } **[High Availability and Backup](high-availability.md)**

    ---

    Run three nodes, take snapshots, restore, and handle Day 2 jobs.

</div>

## Connect Your Applications in One of Two Ways

<div class="grid cards" markdown>

-   :material-code-braces:{ .lg .middle } **[Direct SDK and REST API](sdk-integration.md)**

    ---

    The app reads the secret itself and keeps it in memory. A few lines of code.

    :fontawesome-brands-java: Java · :simple-dotnet: .NET · :fontawesome-brands-python: Python · :fontawesome-brands-node-js: Node.js

-   :simple-kubernetes:{ .lg .middle } **[External Secrets Operator](external-secrets.md)**

    ---

    Sync secrets into a Kubernetes secret. The app code does not change.

</div>

Not sure which one fits? See [Choose a Method](connect-applications.md).

## Follow a Use Case

<div class="grid cards" markdown>

-   :material-database-sync:{ .lg .middle } **[Sync a Database Password Into a Kubernetes App](use-case-wordpress-mysql.md)**

    ---

    WordPress reads its MySQL password from Secrets Manager. Includes a video.

-   :material-key-variant:{ .lg .middle } **[Store Secrets in the KV Engine](kv-secrets.md)**

    ---

    Create, read, version, and delete a secret in the UI.

-   :material-shield-lock:{ .lg .middle } **[Encryption as a Service](transit.md)**

    ---

    Encrypt and decrypt values with the Transit engine.

-   :material-cellphone-key:{ .lg .middle } **[TOTP Authenticator](totp.md)**

    ---

    Generate and validate 6-digit MFA codes under policy control.

-   :material-account-multiple:{ .lg .middle } **[Share Secrets in an Organisation](sharing-secrets.md)**

    ---

    Give each teammate a scoped account that reads only what they need.

-   :material-help-circle:{ .lg .middle } **[Secrets Manager FAQs](../faqs/secrets-manager.md)**

    ---

    Answers to the questions customers ask most often.

</div>

- - -
[SCHEDULE DEMO](https://www.accuknox.com/contact-us){ .md-button .md-button--primary }
