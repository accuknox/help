---
title: Azure IAM Permissions Reference
description: The 209 permissions in the AccuKnox CSPM Azure reader role, with the reason and impact for each.
hide:
  - toc
---

# Azure Permissions Reference

AccuKnox's Azure scanner uses the **AK Reader Aligned Role, 209 read-only permissions** on Azure Resource Manager (ARM) resources. It reads configuration to detect misconfigurations, with no write or delete access.

Review the full list below before onboarding. See the [overview](cspm-permissions-overview.md) to compare clouds, or the [Azure prerequisites](cspm-prereq-azure.md) for setup steps.

!!! tip "How to use this reference"
    Permissions are grouped by service. **Hover** over any permission (or tap it on mobile, or focus it with the keyboard) to see the full rationale: what it does, why AccuKnox needs it, and what you lose if it is not granted. Use the **search box** to find a permission, service, or keyword, and the **service filter** to narrow the list.

<div class="iam-perms" data-src="../../assets/data/iam-perms-azure.json" markdown="0"></div>

## Support for retired Azure services

The role deliberately keeps permissions for several Azure services Microsoft has retired for new customers. Many customers still run legacy instances, so retaining these permissions means AccuKnox continues to report the full security posture during migration instead of showing a misleadingly clean scan.

| Retired service | Retirement status | Permission retained | Support this provides |
|---|---|---|---|
| Redis Cache (classic) | Microsoft is migrating customers to Azure Managed Redis. Existing classic Redis instances continue to work. | `Microsoft.Cache/redis/*` | Full scan of TLS enforcement, firewall rules, private endpoint, non-SSL port, diagnostic settings on legacy Redis instances. |
| Azure Spring Cloud | Retired for new customers. Existing Spring Cloud services still operational. | `Microsoft.AppPlatform/*` | Continued audit of Spring app deployments, TLS settings, network access, encryption for existing customers. |
| PostgreSQL Single Server | Retired by Microsoft in March 2025. Customers must migrate to Flexible Server but many have not yet. | `Microsoft.DBforPostgreSQL/servers/read` | Continued audit of SSL enforcement, log_checkpoints, firewall rules, threat detection on legacy PG single-server instances during migration period. |
| MySQL Single Server | Retired by Microsoft. Customers must migrate to MySQL Flexible Server. | `Microsoft.DBforMySQL/servers/read` | Continued audit of SSL enforcement, weak TLS, threat detection, firewall rules on legacy MySQL single-server instances. |
| Azure Front Door (classic) | Microsoft strongly encourages migration to Front Door Standard/Premium. Classic Front Door still operational. | `Microsoft.Network/frontdoors/*` | Continued audit of classic Front Door WAF policies, SSL configuration, custom rules until customers migrate. |

!!! info "Customer value"
    By retaining these permissions, we provide continuous security posture visibility during the customer's migration window from legacy to current-generation Azure services. A competitor scanner that only supports current-generation services will show a clean scan while legacy services remain unaudited. Our scanner reports the full picture, including the legacy services where security incidents are more likely due to reduced Microsoft support.
