---
title: Understanding Zero Trust with AccuKnox for Secure Access
description: AccuKnox provides a comprehensive Zero Trust solution that helps you secure your Kubernetes workloads by enforcing security policies and best practices.
---

[comment]: <> (This is an auto-generated file. Do not edit manually.)

# Zero Trust Runtime Security

Zero Trust at runtime means deny by default and allow only known, approved behavior. AccuKnox gets you there by learning what each container does, hardening it against industry frameworks, then enforcing a least-permissive baseline in **BLOCK** mode.

## The AccuKnox Runtime Security Journey

True Zero Trust runtime protection is **Step 8** of the journey: the destination, not the starting point. The seven steps that come before it (onboard, discover, harden, audit, learn, stabilize, enforce) are what make Step 8 safe to turn on.

![AccuKnox Runtime Security Journey, steps 1 to 4](../assets/images/runtime-security-journey-1.png)

![AccuKnox Runtime Security Journey, steps 5 to 8](../assets/images/runtime-security-journey-2.png)

!!! info "Zero Trust is reached through a continuous loop"
    Step 5 loops back to Step 2. AccuKnox never stops learning, so the golden baseline keeps tracking real application behavior. Once policies are **STABLE** they switch to **BLOCK** mode: known activity is allowed, everything else is denied. Unknown malware and unknown signatures are automatically rejected. That is AccuKnox's patented runtime Zero Trust.

## Zero Trust Policy Building Blocks

::cards:: cols=3

- title: Process based network control
  content: Allow only specific processes to access network primitives, deny/audit everything else.
  image: images/uc/net-console.png
  url: cards/Process-based-network-control.md

- title: Process based asset access
  content: Allow only specific processes to access sensitive assets, deny/audit everything else.
  image: images/uc/box-lock.png
  url: cards/Process-based-asset-access.md

- title: Process Whitelisting
  content: Allow only specific processes to execute, deny/audit everything else.
  image: images/uc/process-white.png
  url: cards/Process-Whitelisting.md

- title: Network Segmentation
  content: Limit network access strictly between whitelisted service endpoints, deny everything else.
  image: images/uc/net-shield.png
  url: cards/Network-Segmentation.md

- title: Ensure TLS
  content: Ensure that all service endpoints are using the right TLS and certificate configuration.
  image: images/uc/shield-lock.png
  url: cards/Ensure-TLS.md

::/cards::

