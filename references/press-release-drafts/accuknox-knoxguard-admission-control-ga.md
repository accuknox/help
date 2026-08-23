---
title: "AccuKnox Ships KnoxGuard Admission Control for Kubernetes"
slug: "accuknox-knoxguard-admission-control-ga"
url: "https://accuknox.com/press-release/accuknox-knoxguard-admission-control-ga"
release_type: "product-launch"
dateline_city: "Cupertino, California"
dateline_date: "23 AUG 2026"
release_time: "9:00 AM PT"
embargo: "none"
organisations: ["AccuKnox"]
module: "KnoxGuard"
contact_name: "Syed Hadi"
contact_email: "media@accuknox.com"
excerpt: "AccuKnox ships KnoxGuard, an admission controller that turns one custom resource into the Kyverno policy that blocks a privileged pod at the Kubernetes API server."
---

# AccuKnox Ships KnoxGuard Admission Control for Kubernetes

**Cupertino, California**, 23 AUG 2026. *KnoxGuard turns a single custom
resource into the Kyverno policy that rejects a non-compliant workload at the
Kubernetes API server, before the scheduler places it.*

AccuKnox today made KnoxGuard generally available. KnoxGuard is an admission
controller that enforces registry allowlists and privileged-container denials
at the Kubernetes API server, so a workload that violates policy is refused
rather than killed after it starts.

The control closes a gap that runtime enforcement cannot. A runtime sensor sees
a privileged container after the kubelet has already pulled the image and
started the process, which leaves a running workload to kill and a deployment
to roll back. KnoxGuard rejects the same manifest at admission, and the error
returns to the developer's terminal with the failing rule named.

KnoxGuard runs alongside Kyverno rather than replacing it. A platform team
declares an `AdmissionPolicy` custom resource, and KnoxGuard generates and owns
the Kyverno `ClusterPolicy` that performs the enforcement. Both objects stay
visible, so a team can trace any denial back to the policy that caused it.

## What ships today

Three controls, two of them generally available:

| Control | What it enforces | Status |
| --- | --- | --- |
| Registry restrictions | Container registry allowlists and blocklists by pattern, at cluster and namespace scope | Generally available |
| Security posture rules | Denial of privileged-mode containers | Generally available |
| Vulnerability scan thresholds | Blocking an image above a set count of critical or high findings | In the pipeline |

Registry restrictions and the privileged-container denial ship now. Vulnerability
scan thresholds remain in development, and AccuKnox documents them as a pipeline
feature rather than an available control.

KnoxGuard installs through a Helm chart published to Amazon ECR Public and
requires the AccuKnox agents on the cluster. Denials surface in the AccuKnox
console under the Admission Controller alert type and forward to a SIEM through
the standard trigger path. Setup is documented in the
[KnoxGuard guide](https://help.accuknox.com/use-cases/admission-controller-knoxguard/).

## Leadership Perspectives

*"Runtime enforcement and admission control answer different questions.
Admission asks whether a workload should exist at all, and that answer is
cheapest to give before anything is scheduled. KnoxGuard gives platform teams
that answer without asking them to hand-maintain policy engine syntax in every
cluster."*

**— [name], [exact job title], AccuKnox**

*"Kyverno is where most teams already are, so replacing it was never the goal.
KnoxGuard generates and owns the Kyverno policy, which means a team keeps the
engine they know and stops maintaining twenty near-identical cluster policies
by hand."*

**— [name], [exact job title], AccuKnox**

## About AccuKnox

AccuKnox provides a Zero Trust Cloud-Native Application Protection Platform
that delivers security visibility and risk management across applications,
cloud environments, containers, Kubernetes, and AI workloads. Its capabilities
help organisations identify, prioritise, and address security risks across
modern technology environments.

**Website:** [accuknox.com](https://accuknox.com/)

## Media Contacts

**AccuKnox**
Syed Hadi
Product Marketing & Partnerships Lead
media@accuknox.com
