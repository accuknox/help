---
title: Tenant Settings
description: Set tenant-wide defaults for branding, finding SLAs, default scans, downloads, data retention and cloud checks.
---

# Tenant Settings

!!! warning "Draft"
    This page describes a feature that is not released. It is not in the navigation. Confirm the screens and the release with the feature owners before you publish it.

Go to **Settings** → **Tenant**. Three tabs hold the tenant-wide settings.

## General Sets Branding, SLAs and Default Scans

- **Branding**: how the tenant appears across the platform.
- **Findings SLA**: the remediation window in days for each severity. A finding breaches its SLA once the window ends.
- **Application Security**: the default scans for the tenant: SCA, Secrets, SAST, SBOM and IaC.
- **Download Settings**: send exports by **Email Delivery** or place them in **File Manager**.
- **S3 Profile**: one S3 bucket per tenant for exported archives and scan artifacts.

Select the pencil icon on a section to edit it.

## Data Retention Sets How Long Each Data Type Stays

The **Data Retention** tab sets the retention period per data type before automatic purge. The tab states a default of 365 days and a maximum of 1095 days. The data types are all findings, compliance, closed tickets, workload alerts, event trail, CDR, reports, File Manager and raw scanner reports.

See also the [Data Retention Policy](../resources/data-retention-policy.md) page.

## Checks Management Turns Cloud Checks off and Back On

The **Checks Management** tab lists every check with its severity, cloud provider, asset category and status. Filter by severity, status, cloud provider or asset category. Select checks to change their severity or status together. See [Checks Management](../getting-started/3.6-release.md#checks-management) for how a change reaches findings and reports.
