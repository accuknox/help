---
title: Least-Privilege Permissions Reference
description: The read-only permissions AccuKnox CSPM requests for AWS, Azure, and GCP, and why each is needed.
---

# Least-Privilege Permissions Reference

Every permission the AccuKnox CSPM scanner requests is **read-only**. It reads how your resources are configured to flag misconfigurations and build your asset inventory. It never changes anything, and never reads object contents, database rows, or secret payloads.

Pick your cloud to see every permission, grouped by service, with the reason for each on hover:

| Cloud | Permissions | Full list |
|---|---|---|
| **AWS** | 403 | [AWS Permissions Reference](cspm-permissions-aws.md) |
| **Azure** | 209 | [Azure Permissions Reference](cspm-permissions-azure.md) |
| **GCP** | 901 | [GCP Permissions Reference](cspm-permissions-gcp.md) |

Denying a permission does not break the scan. It only creates a blind spot for that service: missing assets, or skipped findings.
