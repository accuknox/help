---
title: Least-Privilege Permissions Reference
description: The read-only permissions AccuKnox CSPM requests for AWS, Azure, and GCP, and why each is needed.
---

# Least-Privilege Permissions Reference

Before you onboard a cloud account, your team can review exactly what AccuKnox will read. This reference lists every permission the CSPM scanner requests for AWS, Azure, and GCP, with a plain-English reason for each.

**Every permission is read-only.** AccuKnox scans posture, it never changes your environment, and it never reads object contents, database rows, or secret payloads. It reads how resources are configured to flag misconfigurations and build your asset inventory.

| Cloud | Permissions | Scope | Full list |
|---|---|---|---|
| **AWS** | 403 read-only actions | IAM policy on a read-only user/role | [AWS Permissions Reference](cspm-permissions-aws.md) |
| **Azure** | 209 permissions | AK Reader Aligned custom role | [Azure Permissions Reference](cspm-permissions-azure.md) |
| **GCP** | 901 permissions across 41 services | Project-level custom role | [GCP Permissions Reference](cspm-permissions-gcp.md) |

On each page, permissions are grouped by service. Hover a permission (or tap it on mobile) to see what it does, why AccuKnox needs it, and what you lose if it is not granted. Use the search box and service filter to jump straight to one.

Denying a permission does not break the scan. It only creates a blind spot for that service: missing assets, or skipped findings for that area.

## Legacy Azure services

The Azure role intentionally keeps permissions for services Microsoft has retired for new customers (classic Redis, Spring Cloud, MySQL/PostgreSQL Single Server, classic Front Door). Many customers still run legacy instances, and dropping these would leave those workloads unaudited. See the [retired-services table](cspm-permissions-azure.md#support-for-retired-azure-services) on the Azure page.

## Next steps

- Review the full list for your cloud: [AWS](cspm-permissions-aws.md), [Azure](cspm-permissions-azure.md), or [GCP](cspm-permissions-gcp.md).
- Set up the read-only role in the [onboarding prerequisites](cspm-prereq-aws.md).
- Connect the account from the [CSPM onboarding guide](aws-onboarding.md).
