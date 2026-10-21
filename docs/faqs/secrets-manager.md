---
title: Secrets Management FAQs
description: Frequently asked questions about AccuKnox Secrets Management and secure secret storage.
hide:
  - toc
---

# Secrets Management

??? "**1. What is AccuKnox Secrets Manager and how is it different from Vault?**"
    AccuKnox Secrets Manager is a centralized secret store that is **compatible with Vault APIs**. This makes migration from HashiCorp Vault easier. It provides:

    - **Storage**: Secure secret storage.
    - **Credentials**: Dynamic credentials.
    - **Encryption**: Transit encryption.
    - **Certificates**: PKI.
    - **Access**: Identity-based access control.

??? "**2. What secret engines and authentication methods are supported?**"
    AccuKnox supports these **secret engines and authentication methods**:

    - **Secret engines**: Key/value secret storage, dynamic secret issuance, transit encryption and PKI workflows.
    - **Authentication methods**: Tokens, AppRole, OIDC, LDAP, Okta, Kubernetes auth and JWT-based identity providers.

??? "**3. Can existing Vault applications work with AccuKnox Secrets Manager without code changes?**"
    In most cases, yes. AccuKnox keeps **Vault-compatible APIs**. Applications that already use Vault can often point to the new endpoint with minimal changes. They keep their existing secret workflows.

??? "**4. How are dynamic secrets and secret rotation handled?**"
    AccuKnox issues **short-lived dynamic credentials** for cloud resources, databases and other services. Leases and renewal policies rotate the credentials automatically. This reduces the risk of credential exposure.

??? "**5. What deployment models and access controls are available?**"
    AccuKnox Secrets Manager runs in **cloud, on-premises and air-gapped** deployments. It provides tenant namespaces, fine-grained policies, audit logging and encrypted storage. You can safely manage secrets across teams and environments.

??? "**6. Which Kubernetes clusters does Secrets Manager run on?**"
    Secrets Manager runs on **any Kubernetes cluster at version 1.30 or later**, with Helm 3 and a default StorageClass. OpenShift has its own values file in the chart. Applications on other clusters and on virtual machines connect over TLS. See the [Deployment Guide](../secrets-manager/deployment.md).

??? "**7. Should I use the SDK or the External Secrets Operator?**"
    It depends on where the secret must live and whether you can change the code.

    - **Use the SDK**: When the secret must stay out of the namespace, or when the application runs on a virtual machine.
    - **Use the External Secrets Operator**: When you cannot change the application code.

    See [Connect Applications](../secrets-manager/connect-applications.md).

??? "**8. Does an application pick up a changed secret on its own?**"
    It depends on how the application reads the secret. The External Secrets Operator updates the Kubernetes secret **within its refresh interval**.

    - **Reads at startup**: A running application sees the new value only after it restarts.
    - **Uses the SDK**: The application sees the new value on its next read.

    See the [WordPress and MySQL walkthrough](../secrets-manager/use-case-wordpress-mysql.md).

??? "**9. Can Secrets Manager run with no internet access?**"
    Yes. Set up an **air-gapped install** in three steps.

    1. Mirror the images into an internal registry.
    2. Install from the chart tar file.
    3. Unseal with your own key holders.

    See [Air-Gapped Deployment](../secrets-manager/air-gapped.md).
