---
title: Scan Paths in a Monorepo
description: Split one repository into several scan targets, each with its own branches and scan types, and read the results per path.
---

# Scan Paths in a Monorepo

!!! warning "Draft"
    This page describes a feature that is not released. It is not in the navigation. Confirm the screens and the release with the feature owner before you publish it.

A monorepo holds several services in one repository. Path configuration makes each path its own scan target, with its own findings and owner.

## Connect the Repository

1. Go to **Settings** → **Integrations** and select **GitHub**.
2. Choose **GitHub Cloud (Using Application)** or **GitHub Self-Hosted (Using PAT)**.
3. Install the AccuKnox Security Scanner GitHub App on your organization.
4. Enter an **Integration Name**. Leave **Auto connect new repos** checked to add new repositories as they appear.
5. Select **Save & Continue**, then pick repositories and branches.

## Configure Paths

1. In the repository list, open **Path configuration** for the repository.
2. Enter a **Name** and a detection path, such as `services/api` or `apps/web`, then select **Add Path**.
3. For each path, choose the branches to scan and the scan types: SCA, Secrets, SAST, SBOM or IaC.
4. For IaC, pick the configuration to scan, such as Dockerfile.
5. Select **Done**. Each path needs at least one scan type. The form shows **Select at least one scan** until you add one.

Select **Reset** to clear the paths.

## Read Results by Path

The repository tree shows the repository, each branch, each path and each scan type. Each row lists critical, high, medium and low counts and the time of the last scan.
