---
title: YouTube Publish Sheet for the Kubernetes Security Walkthrough
video: references/video-edits/cnapp-walkthrough/output/AccuKnox_Kubernetes_Security_Walkthrough.mp4
sources:
  - docs/how-to/k8s-security-onboarding.md
  - docs/use-cases/hardening.md
  - docs/use-cases/kiem.md
  - docs/use-cases/image-scan.md
  - references/video-edits/cnapp-walkthrough/edit.py
  - references/video-edits/cnapp-walkthrough/output/timeline.json
posted: false
---

# YouTube Publish Sheet for the Kubernetes Security Walkthrough

Chapter times come from the render's `timeline.json`. The 5 s hook folds into the first
chapter, and the 10 s Policies section folds into the hardening demo, so every chapter runs
22 seconds or more. Upload settings match the other sheets: channel `accuknox`, Science &
Technology, not made for kids, English, captions from `output/narration.srt`, Unlisted first.

The recording comes from a live AccuKnox tenant. Every environment-specific name is blurred
by the `REDACT` list in `edit.py`. Watch the whole file once more before you set it to Public.

**File:** `references/video-edits/cnapp-walkthrough/output/AccuKnox_Kubernetes_Security_Walkthrough.mp4`, 4:56

**Title**

```text
Kubernetes Security With AccuKnox, From Inventory to a Blocked Attack
```

Alternates for the YouTube Studio title test:

- `Block a Package Manager Inside a Running Pod With AccuKnox`
- `AccuKnox Kubernetes Security Walkthrough in 5 Minutes`

**Thumbnail text:** "Command blocked" over the terminal line `Permission denied`.

**Description**

```text
A shell inside a running Kubernetes workload runs a package manager. AccuKnox activates one hardening policy, and the same command is blocked with permission denied. This 5-minute walkthrough shows that block, and the cluster view around it.

Kubernetes onboarding: https://help.accuknox.com/how-to/k8s-security-onboarding/
Workload hardening: https://help.accuknox.com/use-cases/hardening/
KIEM, identity and entitlements: https://help.accuknox.com/use-cases/kiem/
Container image scanning: https://help.accuknox.com/use-cases/image-scan/
AccuKnox CNAPP: https://accuknox.com/platform/cnapp

Recorded on a live AccuKnox tenant. Environment-specific names are blurred.

What you will see:
- The dashboard: alerts, the policies that raised them, workload traffic and cluster risk posture
- The cluster inventory, with tabs for misconfigurations, vulnerabilities, alerts, compliance, policies and app behavior
- About 1,200 identity findings, and the Kubernetes CIS benchmark findings
- App behavior: file, process and network activity observed in each workload
- 20 ready-made hardening policies, and one that blocks package managers
- The block as a new alert, with the policy, the blocked program, the action and the raw log
- KIEM: subjects, role bindings, roles and the permissions they grant, as a table and a graph
- Container image findings, with the fixed version to upgrade to

The hardening policy lists the package manager programs to block, and its action is Block. Before the policy is active, the command runs. After activation, the same command in the same shell returns permission denied, and the alert appears at the top of the alerts list.

Chapters:
0:00 The Kubernetes security dashboard
0:28 Cluster inventory and detail tabs
1:13 Identity and CIS benchmark findings
1:53 App behavior: file, process and network activity
2:23 A hardening policy blocks a package manager
3:36 KIEM identity graph and excessive permissions
4:21 Container image findings and fix versions
```

**Tags**

```text
Kubernetes security, Kubernetes runtime security, CNAPP, CWPP, workload hardening, runtime protection, KubeArmor, KIEM, Kubernetes RBAC, excessive permissions, CIS Kubernetes benchmark, container image scanning, container security, cloud native security, AccuKnox, AccuKnox CNAPP
```
