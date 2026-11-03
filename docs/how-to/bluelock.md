---
title: BlueLock Runtime Security for Serverless Containers
description: BlueLock enforces runtime security policy from inside the container on AWS Fargate and Azure Container Apps, where you cannot reach the host kernel. Pick the guide for EKS Fargate, ECS Fargate or Azure Container Apps.
hide:
  - toc
---

# BlueLock Runtime Security for Serverless Containers

BlueLock is the AccuKnox open-source engine for runtime security where you cannot reach the host, such as AWS Fargate and Azure Container Apps. It runs inside the workload and enforces KubeArmor policy. See the [BlueLock repository](https://github.com/accuknox/bluelock).

## Choose Your Environment

::cards:: cols=3

- title: EKS Fargate
  image: ./icons/bluelock-eks.svg
  url: /how-to/bluelock-eks-fargate/

- title: ECS Fargate
  image: ./icons/bluelock-ecs.svg
  url: /how-to/bluelock-ecs-fargate/

- title: Azure Container Apps
  image: ./icons/bluelock-azure.svg
  url: /how-to/bluelock-azure-container-apps/

::/cards::

## How BlueLock Enforces Policy

<div class="bl-dia" role="img" aria-label="BlueLock enforcement in four steps. An init container copies the bluelock binary. The bluelock binary starts first and wraps your command. Your app runs as its child with a seccomp filter. A sensitive system call pauses the app and BlueLock checks it, then allows it or blocks it with Permission denied and an alert." data-bl="how">
<svg viewBox="0 0 760 246" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="bl-how" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="7" markerHeight="7" orient="auto">
      <path class="head" d="M0 0 L8 4 L0 8 z"/>
    </marker>
  </defs>
  <rect class="card" x="0" y="0" width="160" height="108" rx="10"/>
  <g class="ic" transform="translate(16 16) scale(1.0)"><path d="M12 3 3.5 7.5v9L12 21l8.5-4.5v-9L12 3z"/><path d="M3.5 7.5 12 12l8.5-4.5M12 12v9"/></g>
  <circle class="navy" cx="138" cy="28" r="10"/>
  <text class="num" x="138" y="32" text-anchor="middle">1</text>
  <text class="h" x="16" y="72">Init container</text>
  <text class="s" x="16" y="92">Copies the binary</text>
  <path class="ln" d="M164 54 H196" marker-end="url(#bl-how)"/>
  <rect class="card" x="200" y="0" width="160" height="108" rx="10"/>
  <g class="ic" transform="translate(216 16) scale(1.0)"><rect x="3" y="4" width="18" height="16" rx="2"/><path d="m7 9 3 3-3 3M13 15h4"/></g>
  <circle class="navy" cx="338" cy="28" r="10"/>
  <text class="num" x="338" y="32" text-anchor="middle">2</text>
  <text class="h" x="216" y="72">bluelock first</text>
  <text class="s" x="216" y="92">Wraps your command</text>
  <path class="ln" d="M364 54 H396" marker-end="url(#bl-how)"/>
  <rect class="card" x="400" y="0" width="160" height="108" rx="10"/>
  <g class="ic" transform="translate(416 16) scale(1.0)"><path d="M12 3l8 3v6c0 4.5-3.2 8-8 9-4.8-1-8-4.5-8-9V6l8-3z"/></g>
  <circle class="navy" cx="538" cy="28" r="10"/>
  <text class="num" x="538" y="32" text-anchor="middle">3</text>
  <text class="h" x="416" y="72">App as a child</text>
  <text class="s" x="416" y="92">Seccomp filter set</text>
  <path class="ln" d="M564 54 H596" marker-end="url(#bl-how)"/>
  <rect class="card" x="600" y="0" width="160" height="108" rx="10"/>
  <g class="ic" transform="translate(616 16) scale(1.0)"><rect x="3" y="4" width="18" height="7" rx="2"/><rect x="3" y="13" width="18" height="7" rx="2"/><circle class="dot" cx="7" cy="7.5" r=".9"/><circle class="dot" cx="7" cy="16.5" r=".9"/></g>
  <circle class="navy" cx="738" cy="28" r="10"/>
  <text class="num" x="738" y="32" text-anchor="middle">4</text>
  <text class="h" x="616" y="72">Syscall check</text>
  <text class="s" x="616" y="92">Paused and inspected</text>
  <path class="ln" d="M680 108 V138 H515 V166" marker-end="url(#bl-how)"/>
  <path class="ln" d="M680 108 V166" marker-end="url(#bl-how)"/>
  <rect class="card" x="440" y="170" width="150" height="72" rx="10"/>
  <text class="h" x="456" y="198">Allowed</text>
  <text class="s" x="456" y="218">Call proceeds</text>
  <rect class="navy" x="610" y="170" width="150" height="72" rx="10"/>
  <text class="wh" x="626" y="198">Blocked</text>
  <text class="ws" x="626" y="218">Permission denied</text>
  <text class="ws" x="626" y="234">and an alert</text>
</svg>
</div>

BlueLock applies a `seccomp` filter, traces system calls with `ptrace` and returns `-EACCES` when a call violates policy. It enforces on the application it launches and on that application's child processes.
