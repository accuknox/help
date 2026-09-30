---
title: "A Kubernetes admission controller blocks the bad pod before it runs"
seo_title: "Kubernetes Admission Controller Blocks Pods Early"
meta_description: "A Kubernetes admission controller rejects a privileged pod at the API server. Here is how KnoxGuard writes the Kyverno policy and what it does not cover yet."
slug: "kubernetes-admission-controller-knoxguard"
url: "https://accuknox.com/blog/kubernetes-admission-controller-knoxguard"
primary_keyword: "kubernetes admission controller"
secondary_keywords: ["knoxguard", "kyverno policy", "privileged container", "pod security admission", "registry allowlist"]
excerpt: "Runtime enforcement catches a privileged container after the kubelet starts it. A Kubernetes admission controller rejects the same manifest at the API server, seconds earlier."
category: "KSPM"
author: "Atharva Shah"
reading_time: "7 minutes"
word_count_target: 1500
audience: "platform engineer"
cover_image_prompt_claude: >
  An isometric illustration of a Kubernetes API server drawn as a gate in a wall,
  with one container manifest passing through and one bouncing off, rendered in
  AccuKnox navy #11206D on a white field with #003BF6 accents, flat vector style,
  wide negative space on the right, no text anywhere in the image.
cover_image_prompt_midjourney: >
  isometric kubernetes api server as a gatehouse, one container cube admitted one
  rejected, navy #11206D and electric blue #003BF6 on white, flat vector, clean
  technical illustration, wide right margin --ar 16:9 --style raw --v 6 --no text
---

# A Kubernetes admission controller blocks the bad pod before it runs

> **Cover image prompt:** an isometric Kubernetes API server drawn as a gate in a
> wall, one container manifest passing through and one bouncing off, AccuKnox
> navy `#11206D` on white with `#003BF6` accents, flat vector, wide negative
> space on the right, no text in the image.

## TL;DR

- A Kubernetes admission controller rejects a manifest at the API server, before the scheduler or the kubelet sees it.
- Red Hat found 94% of respondents hit a Kubernetes or container security incident in 12 months. Close to 60% reported a misconfiguration.
- KnoxGuard turns one `AdmissionPolicy` custom resource into the Kyverno policy that blocks. You write the intent, not the engine syntax.
- KnoxGuard enforces registry allowlists and a privileged-container deny today. Vulnerability thresholds are still in the pipeline, and Kyverno is the only supported engine.
- Admission control does not replace runtime enforcement. It removes the class of failure that runtime enforcement should never have had to see.

## Runtime enforcement is the wrong place to catch a privileged pod

By the time a runtime sensor sees a privileged container, the kubelet already pulled the image and started the process. You now have a running workload to kill, an alert to triage and a deployment to roll back. None of that work was necessary, because the manifest declared `privileged: true` in plain text before anything started.

A Kubernetes admission controller sits earlier. It is an API server plugin. It intercepts a request after authentication and authorization, and before the object reaches etcd. A validating admission webhook returns an allow or a deny, and a deny means the object never exists. The [Kubernetes admission controller reference](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/) lists the built-in plugins and the two webhook types.

That timing is the whole value. A rejected `kubectl apply` returns an error to the person who ran it, in their terminal, with the rule name attached. A runtime kill sends a Slack alert to somebody else an hour later, about a workload they did not deploy.

The misconfiguration numbers say this is where the volume is. Red Hat's [State of Kubernetes Security report](https://www.redhat.com/en/blog/state-kubernetes-security) puts 94% of respondents at one or more security incidents over 12 months. Close to 60% reported a misconfiguration incident specifically. A misconfiguration is a manifest problem, and a manifest problem is an admission problem.

## Kubernetes gives you the hook and none of the policy

The API server ships the webhook mechanism and stops there. `ValidatingAdmissionWebhook` is on by default in a modern cluster and calls whatever endpoint you register. Kubernetes has no opinion about what that endpoint should say. Writing the policy is your job.

Most teams reach for [Kyverno](https://kyverno.io/docs/) at this point, because Kyverno policies are Kubernetes resources rather than a separate language. That solves the syntax problem and creates a fleet problem. You end up with a `ClusterPolicy` for privileged containers, another for registry patterns and another for resource limits. Each one is maintained by hand in every cluster, and each drifts from the version in the cluster next door.

Pod Security Admission covers part of this in-tree, with the three built-in profiles applied per namespace. It is a good floor. It is also fixed, so a registry allowlist or a CVE threshold has nowhere to live inside it. The [AccuKnox guide to Pod Security Admission control](https://help.accuknox.com/use-cases/pod-security-admission-controller/) covers where the built-in profiles stop.

## KnoxGuard writes the Kyverno policy from one custom resource

KnoxGuard is the [AccuKnox admission controller](https://accuknox.com/solutions/admission-controller). It runs beside Kyverno rather than replacing it. You declare an `AdmissionPolicy`, and KnoxGuard generates and owns the Kyverno `ClusterPolicy` that enforces it.

Two Helm installs put both pieces in the cluster. Kyverno first:

```bash
helm repo add kyverno https://kyverno.github.io/kyverno/
helm repo update
helm install kyverno kyverno/kyverno -n kyverno --create-namespace
```

Then KnoxGuard, from the public ECR chart:

```bash
helm upgrade --install knoxguard oci://public.ecr.aws/k9v9d5v2/knoxguard-chart --version=v0.2.0 -n knoxguard --create-namespace
```

Put the AccuKnox agents on the cluster first. They carry the alerting and enforcement path back to the SaaS console. Follow the [cluster onboarding guide](https://help.accuknox.com/how-to/cluster-onboarding/) and confirm five pods are running in `accuknox-agents` before you go further.

A policy that blocks privileged pods in the `default` namespace is nine lines:

```yaml
apiVersion: admission.accuknox.com/v1
kind: AdmissionPolicy
metadata:
  name: test-priv-pod-policy
spec:
  denyPrivilegedPod:
    action: Block
    targetNamespaces:
    - default
```

Apply it and KnoxGuard reports which Kyverno policy it now owns:

```bash
$ kubectl get admissionpolicy
NAME                   READY   MESSAGE                                       OWNED_PPLICIES
test-priv-pod-policy   True    clusterpolicy has been updated successfully   ["knoxguard-privilege-pod-test-priv-pod-policy"]
```

The ownership field matters more than it looks. It links the intent you wrote to the engine object doing the work. That is what you need when a deny fires and somebody asks which policy caused it.

> **Image prompt (inline 1):** a left-to-right pipeline, `kubectl apply` feeding
> an API server node, the API server calling a webhook node, the webhook
> returning a red deny badge, AccuKnox navy `#11206D` on white with `#003BF6`
> accents, flat vector, no text in the image.
>
> *Caption: The deny happens between the API server and etcd, so the pod object is never created.*

## A blocked deployment fails in the developer's terminal

Apply a manifest with `privileged: true` against that policy and the API server refuses it:

```bash
$ kubectl apply -f privpod.yaml
Error from server: error when creating "privpod.yaml": admission webhook "validate.kyverno.svc-fail" denied the request:

resource Pod/default/test-privileged was blocked due to the following policies

knoxguard-privilege-pod-test-priv-pod-policy:
  privileged-containers: "validation error: Privileged mode is disallowed. The fields
    spec.containers[].securityContext.privileged,
    spec.initContainers[].securityContext.privileged,
    and spec.ephemeralContainers[*].securityContext.privileged must be unset or set
    to false. rule privileged-containers failed at path /spec/containers/0/securityContext/privileged/"
```

The error names the policy, the rule and the exact JSON path that failed. A developer can fix the manifest from that message alone, with no console access and no ticket.

The same event lands in the AccuKnox console under **Monitors > Alerts**, filtered by the **Admission Controller** alert type. From there it forwards to a SIEM through the standard trigger path, and the [Splunk integration guide](https://help.accuknox.com/integrations/splunk/) covers the setup.

## Three controls today, and one of them is not shipping yet

| Control | What it does | Status |
| --- | --- | --- |
| Registry restrictions | Allowlists or blocks container registries by pattern, at cluster and namespace scope | Available |
| Security posture rules | Denies privileged-mode containers | Available |
| Vulnerability scan thresholds | Blocks an image above a set count of critical or high findings | In the pipeline |

Most teams switch on registry restrictions first. A typo in an image reference pulls a workload from a registry nobody reviewed. Pattern matching runs at cluster and namespace level. A shared cluster can hold a strict default plus a looser exception for one team.

The vulnerability threshold is the one to plan around rather than plan on. AccuKnox documents it as a pipeline feature, so a policy that blocks on CVE count has no place to be written today. Until it ships, keep that gate in the CI pipeline where the image is built.

## What KnoxGuard does not cover

Kyverno is the only supported policy engine. The [KnoxGuard documentation](https://help.accuknox.com/use-cases/admission-controller-knoxguard/) calls the architecture engine-independent and expects more engines. A cluster standardised on Gatekeeper or on OPA still gets no benefit from KnoxGuard today.

The posture rule set is also narrower than the marketing surface suggests. `denyPrivilegedPod` is the rule that exists. Capability constraints, resource limits and pod security context rules are named as directions, not as shipped controls. Read the `AdmissionPolicy` spec in the docs before you promise a control to an auditor.

Admission control only sees what the manifest declares. A pod that is clean at admission and then exploited at runtime is a runtime problem, and no webhook in the world catches it.

## Put admission control in front of runtime enforcement, not instead of it

The two controls answer different questions. Admission asks whether this workload should exist. Runtime asks what this workload is doing now. A cluster with only runtime enforcement spends its day killing workloads that should never have been admitted. A cluster with only admission control goes blind the moment a legitimate container is compromised.

Start with the privileged deny and a registry allowlist. Run both in a non-production namespace for a week and read the alert volume before you widen the scope. Then wire the same clusters to runtime enforcement, which the [AccuKnox writeup on Kyverno policies and KubeArmor](https://accuknox.com/blog/kyverno-admission-controller-policies-kubearmor) covers in detail.

## FAQs

### What is a Kubernetes admission controller?

It is an API server plugin that intercepts a request after authentication and authorization and before the object is written to etcd. A validating webhook can deny the request outright. The pod object is never created and nothing is scheduled.

### How is admission control different from Pod Security Admission?

Pod Security Admission is built into Kubernetes and applies one of three fixed profiles per namespace. A webhook-based Kubernetes admission controller is extensible. It can enforce rules the built-in profiles have no field for, such as a registry allowlist or a CVE threshold.

### Does KnoxGuard replace Kyverno?

KnoxGuard does not replace Kyverno. It generates and owns a Kyverno `ClusterPolicy` from a single `AdmissionPolicy` custom resource. Kyverno still makes the admission decision, and `kubectl get admissionpolicy` shows which Kyverno policy each AccuKnox policy owns.

### Can an admission policy block an image with too many CVEs?

That control is not available yet. AccuKnox documents vulnerability scan thresholds as a pipeline feature, so enforce CVE gates in the build pipeline until the control ships.

### Where do the denials show up outside the terminal?

Under **Monitors > Alerts** in the AccuKnox console, with the alert type set to **Admission Controller**. Those alerts forward to a SIEM or a notification tool through the standard trigger path.
