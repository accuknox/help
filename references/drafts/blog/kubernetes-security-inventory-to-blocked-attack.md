---
title: "AccuKnox Kubernetes security takes you from inventory to a blocked attack"
seo_title: "Kubernetes Security With AccuKnox, Inventory to Block"
meta_description: "Follow AccuKnox Kubernetes security step by step, from cluster inventory and findings to a hardening policy that blocks apt in a running pod, with alerts."
slug: "kubernetes-security-inventory-to-blocked-attack"
url: "https://accuknox.com/blog/kubernetes-security-inventory-to-blocked-attack"
date: "2026-10-11"
primary_keyword: "kubernetes security"
secondary_keywords: ["kubernetes hardening policy", "KIEM", "CIS Kubernetes Benchmark", "kubernetes runtime security", "container image scanning"]
excerpt: "A step-by-step walkthrough of AccuKnox Kubernetes security, from cluster inventory and findings to a hardening policy that blocks a package manager in a running pod."
category: "KSPM"
author: "Atharva Shah"
reading_time: "5 minutes"
word_count_target: 1100
audience: "platform engineer | security engineer"
cover_image: "https://img.youtube.com/vi/M_6RKJFTvOI/maxresdefault.jpg"
cover_image_prompt_claude: >
  Not used. The cover is the YouTube thumbnail for video M_6RKJFTvOI.
cover_image_prompt_midjourney: >
  Not used. The cover is the YouTube thumbnail for video M_6RKJFTvOI.
---

# AccuKnox Kubernetes security takes you from inventory to a blocked attack

> ![The thumbnail of the AccuKnox Kubernetes security walkthrough video](https://img.youtube.com/vi/M_6RKJFTvOI/maxresdefault.jpg)

*Caption: The thumbnail of the five-minute AccuKnox Kubernetes security walkthrough.*

## TL;DR

- AccuKnox shows a cluster's inventory, identity findings, benchmark failures, runtime behavior and image vulnerabilities in one console.
- The demo cluster lists about 1,200 identity findings. Each one opens to a detail view with its severity and first and last detected dates.
- The Hardening tab holds 20 ready-made policies, and one of them blocks package managers.
- Before activation, `apt` runs in a shell inside a workload. After activation, the same command returns `Permission denied` and a new alert appears.
- A hardening policy blocks only the programs it lists, and runtime security needs Linux kernel 4.15 or later.

## The Dashboard and Inventory Show What You Protect

The AccuKnox dashboard for a connected Kubernetes environment opens on a 30-day window. Its widgets summarize alerts, the policies that raised them, workload traffic and the risk posture of the connected clusters. Lower down, you find the top identity findings and the compliance status of the benchmark checks.

![The AccuKnox dashboard with the Top identity findings and Benchmark compliance widgets highlighted](https://media.zernio.com/temp/1791272895178_lg7megst_k01-dashboard.jpg)

*Caption: The lower dashboard widgets show the top identity findings and the benchmark compliance status.*

Open Inventory next, then open the cluster. The overview lists nodes, workloads, namespaces and active policies. Six tabs sit beside it.

![The Inventory Clusters list with one connected cluster highlighted](https://media.zernio.com/temp/1791272897424_s010ghuc_k02-clusters.jpg)

*Caption: The Clusters list shows each connected cluster with its alerts and findings.*

![The cluster overview panel with the Cluster Information card showing nodes, workloads, namespaces and active policies](https://media.zernio.com/temp/1791272899521_zktg7026_k03-cluster-info.jpg)

*Caption: The cluster overview lists nodes, workloads, namespaces and active policies, with a tab for each finding type.*

| Tab | What it shows |
| --- | --- |
| Misconfiguration | Open findings grouped by severity |
| Vulnerabilities | Container image findings, and the images with the most findings |
| Alerts | The policies that raised alerts, and the workload for each |
| Compliance | The benchmark checks for this cluster |
| Policies | The policies applied to this cluster |
| App behavior | The network connections seen in this cluster |

Each feature installs on its own, so you can start with one. Runtime security runs as a DaemonSet, and misconfiguration scanning, KIEM, CIS benchmarking and image scanning run as cron jobs. The [Kubernetes Security Onboarding](https://help.accuknox.com/how-to/k8s-security-onboarding/) page lists the Helm command for each.

## Identity and Benchmark Findings Share One Findings List

Go to Issues, then Findings. The Findings Summary splits cluster findings into two groups, identity findings and Kubernetes benchmark findings. In the demo, the identity list holds about 1,200 entries.

![The Findings Summary with KIEM identity findings and K8s CIS benchmark findings as two groups](https://media.zernio.com/temp/1791272901268_0njs7pxm_k04-findings-summary.jpg)

*Caption: The Findings Summary splits cluster findings into KIEM identity findings and K8s CIS benchmark findings.*

Open one entry for the full detail. The example is a service account with no workloads. The detail shows its severity and the dates it was first and last detected.

![The KIEM findings list with the total of 1,201 findings highlighted](https://media.zernio.com/temp/1791272903603_m6034r2g_k05-kiem-findings.jpg)

*Caption: The KIEM findings list in the demo shows 1,201 findings.*

Switch the data type to CIS K8s Benchmark Findings to see one row per failed check. The checks come from the [CIS Kubernetes Benchmark](https://www.cisecurity.org/benchmark/kubernetes). To keep only failures, set the Tool Output filter to Failed, as the [CIS benchmark findings guide](https://help.accuknox.com/use-cases/cis-benchmarking/) describes. This view is part of AccuKnox [KSPM](https://accuknox.com/platform/kspm).

![The CIS Kubernetes benchmark findings list with the Failed tool output rows highlighted](https://media.zernio.com/temp/1791272905454_e024t682_k06-cis-failed.jpg)

*Caption: The benchmark findings list has one row per check, and the Tool Output column marks the failed ones.*

> **Limitation.** The CIS benchmark job covers generic Kubernetes, EKS, AKS and GKE. OKE is not currently supported.

## App Behavior Shows What Each Workload Does at Runtime

Under Runtime Protection, App behavior opens on a runtime summary and a graph of the connections AccuKnox observed. AccuKnox uses KubeArmor to watch and control this activity. The list view splits the data into three areas.

- **File activity.** The demo shows one attempt to change a file, and the action is Block.
- **Process activity.** This view lists the processes that ran in each workload.
- **Network activity.** This view lists the connections of each workload.

The [Application Behavior](https://help.accuknox.com/use-cases/app-behavior/) guide walks through the same views on a MySQL workload.

![The App behavior page with the runtime summary counts above the connection graph of one workload](https://media.zernio.com/temp/1791272907063_gvvinnqm_k07-app-behavior.jpg)

*Caption: The runtime summary and connection graph for one workload.*

## One Hardening Policy Turns a Working Command Into Permission Denied

Hardening policies are KubeArmor policies, and the Hardening tab ships 20 of them. The demo uses the one that prohibits package manager execution. It is part of AccuKnox [runtime security](https://accuknox.com/platform/runtime-security).

1. Open Runtime Protection, then Policies, then the Hardening tab. All 20 policies show as Inactive.
2. Open a shell inside a workload with `kubectl exec`, and run `apt`. The command runs, because no policy blocks it yet.
3. Open the package manager policy. It lists the programs to block, and its action is Block.
4. Select the policy and click Activate.
5. Wait for the confirmation message. The policy status changes to Active.
6. Run `apt` again in the same shell. The shell prints the line below.

```text
bash: /usr/bin/apt: Permission denied
```

![The Policies page with the Hardening tab open and 20 hardening policies listed as Inactive](https://media.zernio.com/temp/1791272909939_ze7r5yan_k08-hardening-list.jpg)

*Caption: The Hardening tab lists the 20 policies, all Inactive until you activate one.*

![A shell inside the workload where the apt command runs and prints its usage text](https://media.zernio.com/temp/1791272911790_9bldc3ee_k09-before.jpg)

*Caption: Before activation, apt runs in the shell inside the workload.*

![The package manager hardening policy YAML with Action Block and the list of package manager programs highlighted](https://media.zernio.com/temp/1791272913504_ipgyhw65_k10-policy-yaml.jpg)

*Caption: The package manager policy lists the programs it blocks, and its action is Block.*

![The Hardening policies list with the package manager policy selected and the Activate button highlighted](https://media.zernio.com/temp/1791272915263_qgfuo68h_k11-activate.jpg)

*Caption: Select the policy and click Activate.*

![The Hardening policies list with the package manager policy marked Active and the label Policy enabled](https://media.zernio.com/temp/1791272917024_eegxqel7_k12-policy-enabled.jpg)

*Caption: The policy status changes to Active, and the confirmation reads Policy enabled.*

![The same shell after activation, where apt returns bash: /usr/bin/apt: Permission denied](https://media.zernio.com/temp/1791272918899_7xgyyw28_k13-blocked.jpg)

*Caption: The same apt command in the same shell now returns Permission denied.*

Open the alerts list next. The block appears as a new alert at the top. The alert names the policy, the blocked program, the Block action and the result. The raw log keeps the full context, including the process name of the blocked command.

![The alerts list with the alert for the blocked command at the top](https://media.zernio.com/temp/1791272920851_0sd23qnw_k14-alert.jpg)

*Caption: The alert for the blocked command sits at the top of the alerts list.*

![The alert detail with the policy name, the blocked program, the Block action and the Permission denied result](https://media.zernio.com/temp/1791272922504_0h1izh04_k15-alert-detail.jpg)

*Caption: The alert names the policy, the blocked program, the Block action and the Permission denied result.*

> **Limitation.** The policy blocks only the programs it lists. The [Packaging tools card](https://help.accuknox.com/use-cases/cards/Packaging-tools/) shows a sample policy and the alert it raises.

## KIEM Graphs Subjects, Roles and Permissions in One View

Back in the identity view, the table maps each subject to its role binding, its role and its permissions. The graph view shows the same links, grouped by namespace. Open a service account to see its bindings and the pod that uses it. The manifest view shows the role binding definition.

A key query filters the graph. The Excessive Permission query matched three system controllers in the demo. The result shows as a list or as a graph. [KIEM](https://help.accuknox.com/use-cases/kiem/) ships 15 built-in queries. One finds service accounts that connect to no workload.

![The KIEM table with subject, role binding, role and permissions columns](https://media.zernio.com/temp/1791272924234_29q55l0c_k16-kiem-table.jpg)

*Caption: The KIEM table maps each subject to its role binding, its role and its permissions.*

![The KIEM graph view of subjects, role bindings and roles grouped by namespace](https://media.zernio.com/temp/1791272926471_hsh9z65s_k17-kiem-graph.jpg)

*Caption: The graph view shows the same links, grouped by namespace.*

![The KIEM Excessive Permission key query result as a table of subjects, role bindings and roles](https://media.zernio.com/temp/1791272928052_5qbhwkiv_k18-excessive.jpg)

*Caption: The Excessive Permission query lists the subjects, role bindings and roles that matched.*

## Image Findings Name the Fixed Version to Upgrade To

In-cluster image scanning feeds the Container Image Findings view. Each finding shows the affected package, its severity and when it was first and last detected. The Solution tab gives the fixed version to upgrade to. The Other info tab links to the public vulnerability record.

![The Container Image Findings list with each CVE, its package and its severity](https://media.zernio.com/temp/1791272929826_lllh2gtg_k19-image-findings.jpg)

*Caption: The Container Image Findings list shows each vulnerability with its package and its severity.*

![The Solution tab of an image finding showing the fixed version to upgrade to](https://media.zernio.com/temp/1791272931487_qm1mgmit_k20-fix-version.jpg)

*Caption: The Solution tab gives the fixed version to upgrade to.*

The in-cluster scanner reads cached images on the nodes, so it needs no registry access. Findings go to the AccuKnox console for triage.

## Watch a Package Manager Get Blocked on a Live Tenant

The video follows these steps in order. It was recorded on a live AccuKnox tenant, and environment-specific names are blurred.

```html
<iframe width="560" height="315" src="https://www.youtube.com/embed/M_6RKJFTvOI" title="Kubernetes Security With AccuKnox, From Inventory to a Blocked Attack" frameborder="0" allowfullscreen></iframe>
```

[Watch the walkthrough on YouTube](https://www.youtube.com/watch?v=M_6RKJFTvOI). To try it on your own clusters, start at the [AccuKnox CNAPP platform page](https://accuknox.com/platform/cnapp).

## FAQs

### Does the package manager policy block every program?

No, it blocks only the programs it lists, and its action is Block. The policy in the video lists 12 programs: apk, apt-get, apt, dnf, dpkg, gdebi, makepkg, pacman, rpm, yaourt, yum and zypper.

### What does my cluster need before I start?

Kubernetes 1.18 or later, and Linux kernel 4.15 or later for runtime security. The cluster needs only egress connectivity to the control plane. AccuKnox supports managed clusters on EKS, AKS and OCI, and on-prem clusters.

### Which clusters does the CIS benchmark check cover?

Generic Kubernetes, EKS, AKS and GKE. OKE is not currently supported.
