---
title: GCP IAM Permissions Reference
description: The 901 read-only permissions in the AccuKnox CSPM GCP custom role, with the reason for each.
hide:
  - toc
---

# GCP Permissions Reference

AccuKnox's GCP scanner uses a **project-level custom role with 901 read-only permissions** across 41 services. Every permission is a `.list`, `.get`, `.getIamPolicy`, or export/analyze verb, so AccuKnox never reads object contents, table rows, or secret payloads.

Review the full list below before onboarding. See the [overview](cspm-permissions-overview.md) to compare clouds, or the [GCP prerequisites](cspm-prereq-gcp.md) for setup steps.

!!! note "About the `iam.googleapis.com/*` permissions"
    17 permissions use the fully-qualified `iam.googleapis.com/*` form (Workload Identity Federation and OAuth clients). These are not part of the built-in `roles/viewer` and are included deliberately for full IAM posture visibility.

!!! tip "How to use this reference"
    Permissions are grouped by service. **Hover** over any permission (or tap it on mobile, or focus it with the keyboard) to see the full rationale. Use the **search box** to find a permission, service, or keyword, and the **service filter** to narrow the list.

<div class="iam-perms" data-src="../../assets/data/iam-perms-gcp.json" markdown="0"></div>
