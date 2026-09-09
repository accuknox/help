---
title: Data Retention Policy
description: How long AccuKnox retains different types of security data across CSPM, CWPP, ASPM, logs, reports, and raw scanner output.
---

# Data Retention Policy

!!! info "Overview"
    This page lists how long AccuKnox retains each type of data on the platform. Retention periods are measured in days from the time the data is generated. Once a period ends, the data is removed automatically.

## Retention Periods

| Category | Data Type | Retention (days) | Details |
| :-- | :-- | :--: | :-- |
| **CSPM** | Fixed Findings | 180 | Findings that were fixed and are no longer discovered by the scanners. |
| **CSPM** | Deleted Assets | 180 | Cloud assets that are deleted. |
| **CDR** | Logs from CSPs (CloudTrail, Azure/GCP logs) | 90 | Logs sent from AccuKnox integration of cloud logs. |
| **CWPP** | Alerts | 180 | Policy violations from K8s, containers, and virtual machines. |
| **CWPP** | Telemetry | 30 | General process, file, and network telemetry. |
| **ASPM and other scanners** | Fixed Findings | 180 | Findings that were fixed and are no longer discovered by the scanners. |
| **ASPM and other scanners** | Deleted Assets | 180 | Assets that were deleted. |
| **EventTrail** | AccuKnox Control Plane activity logging (who changed a finding's status, when a ticket was created, etc.) | 180 | Contains logs for AccuKnox Control Plane operations. |
| **Reports** | On-demand or scheduled reports shown in the portal | 180 | On-demand or scheduled reports shown in the portal. |
| **SIEM** | Logs from different integrations | 180 | Syslogs, CloudTrail, Azure/GCP logs, and similar. |
| **Raw Scanner Reports** | JSON files from different scanners kept in an S3 bucket | 365 | Contains raw reports in JSON/SARIF format from the native scanning tool. |

!!! note
    Retention periods may be adjusted for specific enterprise or contractual requirements. Contact AccuKnox support if your organization needs a custom retention window.
