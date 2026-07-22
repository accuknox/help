---
title: AWS IAM Permissions Reference
description: The 403 read-only IAM permissions the AccuKnox CSPM scanner requests for AWS, with the reason and impact for each.
hide:
  - toc
---

# AWS IAM Permissions Reference

AccuKnox's AWS scanner uses **403 read-only IAM permissions** (`List`, `Describe`, and `Get` only) to inventory your resources and check their configuration. No write, delete, or data-download access, and it never reads object contents.

Review the full list below before onboarding. See the [overview](cspm-permissions-overview.md) to compare clouds, or the [AWS prerequisites](cspm-prereq-aws.md) for setup steps.

!!! tip "How to use this reference"
    Permissions are grouped by service. **Hover** over any permission (or tap it on mobile, or focus it with the keyboard) to see the full rationale: what it does, why AccuKnox needs it, and what you lose if it is not granted. Use the **search box** to find a permission, service, or keyword, and the **service filter** to narrow the list.

<div class="iam-perms" data-src="../../assets/data/iam-perms-aws.json" markdown="0"></div>
