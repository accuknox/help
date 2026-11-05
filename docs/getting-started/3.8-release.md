---
title: AccuKnox v3.8 Release Notes
description: AccuKnox v3.8 revamps the Prompt Firewall view, adds step-by-step DAST scan evidence and AI Pentesting, pull request decoration, monorepo scan paths, tenant settings, and AgentZ investigation skills that re-score findings.
---

# AccuKnox v3.8 Release Notes

!!! warning "Draft"
    This note is a draft built from the 23 October 2026 sprint demo. Release targets are not confirmed. The page is not in the navigation. Each entry links to the page that holds the details.

## Prompt Firewall

The Prompt Firewall view now shows integrations, applications, policies and violations in one place. Group applications by integration, bulk edit policies, and trace a query to the text that triggered a policy. See [Prompt Firewall](../how-to/prompt-firewall.md).

## DAST

- **Scan evidence.** A legacy DAST scan that fails to log in now shows each step and a screenshot of the failure. See [DAST Authenticated Scan](../how-to/dast-authenticated-scans.md#read-the-scan-evidence-for-a-failed-login).
- **AI Pentesting.** The AI Dast Scan collector validates targets and TOTP secrets, and writes a report to File Manager. See [AI Pentesting](../how-to/ai-pentesting.md).

## Source Code Security

- **Pull request decoration.** Each pull request gets an AccuKnox security review with ranked fixes and inline suggestions. See [Pull Request Decorator](../how-to/pr-decorator.md).
- **Monorepo scan paths.** Each path in a repository becomes its own scan target. See [Scan Paths in a Monorepo](../how-to/aspm-monorepo-paths.md).

## Platform

Tenant settings now hold branding, finding SLAs, default scans, download settings, data retention and checks management. See [Tenant Settings](../how-to/tenant-settings.md).

## AgentZ

Investigation skills check a finding against live evidence, adjust its severity and write a labeled report. The AgentZ documentation covers the workflow.
