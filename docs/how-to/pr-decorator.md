---
title: Pull Request Decorator
description: Add an AccuKnox security review to every pull request, with a summary, ranked fixes, a findings map and inline suggestions.
---

# Pull Request Decorator

!!! warning "Draft"
    This page describes a feature that is not released. It is not in the navigation. Confirm the action name, the supported platforms and the release with the feature owner before you publish it.

The pull request decorator posts an **AccuKnox Security Review** on each pull request. It runs the AccuKnox ASPM scanner CLI in your pipeline, so it does not depend on one CI/CD tool.

## Add the Action to a GitHub Workflow

Add a step that runs the action after `actions/checkout`. Set `fetch-depth: 0` on the checkout.

Set these inputs on the step.

| Input | Value |
|---|---|
| `scan_type` | The scans to run, such as `sast,sca,iac,secret,quality` |
| `accuknox_endpoint` | Your AccuKnox endpoint, stored as a repository secret |
| `accuknox_token` | Your AccuKnox token, stored as a repository secret |
| `accuknox_label` | The label that groups the results, stored as a repository secret |
| `soft_fail` | `true` keeps the build passing when the scan finds issues |
| `pr_decorator` | `true` posts the review on the pull request |

Give the workflow `pull-requests: write` permission so it can comment.

## Read the Review on the Pull Request

The comment holds these parts.

- **Pull Request Summary**: what the change does, a table of key changes per file, and an impact analysis.
- **Top fixes**: the findings to fix first, ordered by risk.
- **Findings by File**: a map of files and the findings in each.
- **Security Findings**: counts by severity, and the quality conditions that failed, such as `CRITICAL: found 3, threshold 0`.

The decorator also adds an inline comment on the changed line for each finding. A comment shows the severity, the reason and the CWE. When a fix exists, it offers a suggested change that you apply with one click. When none exists, the comment says the fix needs a manual review.

## Platform Support

The team tested GitHub and GitLab. Azure DevOps and Bitbucket are not tested. The decoration step is specific to each platform, so confirm support before you promise it.
