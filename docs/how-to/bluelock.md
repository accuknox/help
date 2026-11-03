---
title: BlueLock Runtime Security for Serverless Containers
description: BlueLock enforces runtime security policy from inside the container on AWS Fargate and Azure Container Apps, where you cannot reach the host kernel. Pick the deployment guide for EKS Fargate, ECS Fargate or Azure Container Apps.
---

# BlueLock Runtime Security for Serverless Containers

BlueLock is the AccuKnox open-source engine for runtime security in environments where you cannot reach the host. On AWS Fargate and Azure Container Apps you cannot load kernel modules, deploy eBPF probes or run a privileged DaemonSet, so KubeArmor cannot run on the node. BlueLock enforces policy from inside the container instead.

The source code lives in the [accuknox/bluelock](https://github.com/accuknox/bluelock) repository.

## Pick the Guide That Matches Your Environment

Each guide takes you from an empty cloud account to a blocked command and an alert in AccuKnox.

<div class="grid cards" markdown>

-   :material-kubernetes:{ .lg .middle .sai-ic } __EKS Fargate__

    ---

    Kubernetes cluster. Create or reuse an EKS Fargate cluster, then deploy the BlueLock sample with `kubectl` and onboard the cluster.

    [:octicons-arrow-right-24: Deploy on EKS Fargate](bluelock-eks-fargate.md)

-   :material-aws:{ .lg .middle .sai-ic } __ECS Fargate__

    ---

    VM cluster. Terraform builds the AWS resources and a control plane node. Two Fargate tasks join as workers.

    [:octicons-arrow-right-24: Deploy on ECS Fargate](bluelock-ecs-fargate.md)

-   :material-microsoft-azure:{ .lg .middle .sai-ic } __Azure Container Apps__

    ---

    VM cluster. Terraform builds the Azure network, a control plane VM and a container app with two replicas.

    [:octicons-arrow-right-24: Deploy on Azure Container Apps](bluelock-azure-container-apps.md)

</div>

## The Three Guides at a Glance

| | EKS Fargate | ECS Fargate | Azure Container Apps |
|---|---|---|---|
| Cluster type in AccuKnox | Kubernetes | VM | VM |
| Control plane | AccuKnox agents in the `agents` namespace of your EKS cluster | EC2 instance that runs `knoxctl` | Azure VM that runs `knoxctl` |
| Workers | Fargate pods | Fargate tasks | Container app replicas |
| How you deploy | `eksctl`, `kubectl` and Helm | Terraform | Terraform |
| Cloud tools you need | AWS CLI, `eksctl` | AWS CLI, Terraform | Azure access, AWS CLI, Terraform |

The EKS guide has no script. It needs only a cluster, and you can use your own. The ECS and Azure guides use the public Terraform scripts in the [BlueLock repository](https://github.com/accuknox/bluelock/tree/master/terraform).

## How BlueLock Enforces Policy Inside the Container

BlueLock cannot hook the host kernel, so it moves enforcement into the container. It wraps your application and uses `ptrace` and `seccomp` to inspect system calls.

<div class="ak-dia" role="img" aria-label="How BlueLock enforces policy in four steps. An init container copies the bluelock binary into a shared volume. The app container starts the bluelock binary first, with your own command as its arguments. BlueLock applies a seccomp filter and launches your app as a child process. When the app makes a sensitive system call, BlueLock inspects it through ptrace and either allows it or blocks it with a Permission denied error and an AccuKnox alert.">
<svg viewBox="0 0 920 292" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="mhow" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="7" markerHeight="7" orient="auto">
      <path class="head" d="M0 0 L8 4 L0 8 z"/>
    </marker>
    <marker id="mhowa" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="7" markerHeight="7" orient="auto">
      <path class="head-acc" d="M0 0 L8 4 L0 8 z"/>
    </marker>
  </defs>
  <rect class="p" x="8" y="14" width="210" height="150" rx="8"/>
  <circle class="step" cx="34" cy="42" r="12"/>
  <text class="t-step" x="34" y="46" text-anchor="middle">1</text>
  <text class="t-h" x="56" y="47">Init container</text>
  <text class="t-s" x="26" y="84">Copies the bluelock binary</text>
  <text class="t-s" x="26" y="102">into a shared volume</text>
  <text class="t-s" x="26" y="120">mounted at /kubearmor.</text>
  <path class="ln" d="M219 89 H243" marker-end="url(#mhow)"/>
  <rect class="p" x="244" y="14" width="210" height="150" rx="8"/>
  <circle class="step" cx="270" cy="42" r="12"/>
  <text class="t-step" x="270" y="46" text-anchor="middle">2</text>
  <text class="t-h" x="292" y="47">Entrypoint override</text>
  <text class="t-s" x="262" y="84">Your app container starts</text>
  <text class="t-s" x="262" y="102">/kubearmor/bluelock first,</text>
  <text class="t-s" x="262" y="120">with your own command</text>
  <text class="t-s" x="262" y="138">passed as its arguments.</text>
  <path class="ln" d="M455 89 H479" marker-end="url(#mhow)"/>
  <rect class="acc" x="480" y="14" width="210" height="150" rx="8"/>
  <circle class="step" cx="506" cy="42" r="12"/>
  <text class="t-step" x="506" y="46" text-anchor="middle">3</text>
  <text class="t-h" x="528" y="47">Sandbox and launch</text>
  <text class="t-s" x="498" y="84">BlueLock receives policies,</text>
  <text class="t-s" x="498" y="102">applies a seccomp filter,</text>
  <text class="t-s" x="498" y="120">then launches your app</text>
  <text class="t-s" x="498" y="138">as its child process.</text>
  <path class="ln" d="M691 89 H715" marker-end="url(#mhow)"/>
  <rect class="acc" x="716" y="14" width="210" height="150" rx="8"/>
  <circle class="step" cx="742" cy="42" r="12"/>
  <text class="t-step" x="742" y="46" text-anchor="middle">4</text>
  <text class="t-h" x="764" y="47">Syscall inspection</text>
  <text class="t-s" x="734" y="84">A sensitive system call</text>
  <text class="t-s" x="734" y="102">pauses the app and hands</text>
  <text class="t-s" x="734" y="120">control to BlueLock,</text>
  <text class="t-s" x="734" y="138">which checks it (ptrace).</text>
  <path class="ln" d="M821 164 V184 H585 V204" marker-end="url(#mhow)"/>
  <path class="ln-bad" d="M821 164 V204" marker-end="url(#mhow)"/>
  <text class="t-s" x="8" y="198">BlueLock compares the call with your policy</text>
  <rect class="good" x="470" y="204" width="230" height="66" rx="8"/>
  <text class="t-h" x="486" y="230">Allowed</text>
  <text class="t-s" x="486" y="250">The call proceeds as normal.</text>
  <rect class="bad" x="716" y="204" width="196" height="66" rx="8"/>
  <text class="t-h" x="732" y="230">Blocked</text>
  <text class="t-s" x="732" y="248">The app gets Permission</text>
  <text class="t-s" x="732" y="262">denied and AccuKnox alerts.</text>
</svg>
</div>

BlueLock returns the error `-EACCES` when a call violates policy, and the application sees Permission denied. You create and activate the policy in the AccuKnox console, the same way you do for any KubeArmor policy.

!!! note "What BlueLock covers"
    BlueLock enforces policy on the application it launches and on that application's child processes. Every protected workload needs the `bluelock` binary from an init container and an entrypoint that starts with `/kubearmor/bluelock`.

## What You Need Before You Start

- An AccuKnox account with access to the console.
- Cloud credentials for the guide you pick. The EKS Fargate and ECS Fargate guides need AWS. The Azure Container Apps guide needs Azure and the AWS CLI.
- A terminal with `socat`. Every guide uses it to reach the sample application on port 1337.

If a teammate tests a guide, give that person the cloud credentials before they start.

## Where to Find Agent and Node Requirements

- [Runtime Security Onboarding](cluster-onboarding.md) covers the standard Kubernetes agent install that the EKS Fargate guide builds on.
- [Onboarding and Deboarding VMs with Docker](vm-onboard-deboard-docker.md) lists the resource and port requirements for a control plane node.
