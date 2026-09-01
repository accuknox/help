---
title: App Hardening
description: Steps to achieve zero-trust environment by App Hardening using AccuKnox security solution for Kubernetes and cloud native platforms.
---

# App Hardening

Application Hardening is one path to a Zero Trust environment. KubeArmor ships a curated set of block-based hardening policies derived from CIS, MITRE ATT&CK, NIST 800-53, PCI DSS, and STIG, so you can pick the controls that match your compliance posture and apply them at runtime.

## Where Hardening Fits in the Runtime Security Journey

Hardening policies cover steps 3, 4, and 7 of the AccuKnox Runtime Security Journey: you pull recommended policies from industry frameworks, activate them in AUDIT mode for continuous diagnostics, and promote them to BLOCK mode once stable.

![AccuKnox Runtime Security Journey, steps 1 to 4](../assets/images/runtime-security-journey-1.png)

![AccuKnox Runtime Security Journey, steps 5 to 8](../assets/images/runtime-security-journey-2.png)

!!! info "Hardening sits on top of a learning loop"
    Step 5 loops back to Step 2. Discovered policies keep refining the baseline while hardening policies sit alongside in AUDIT for 2-3 weeks, then move to BLOCK once behavior is **STABLE**, locking in true Zero Trust runtime protection.

Use case example: **Disallowing arbitrary binary execution to prevent RCE**

1.Select your cluster and namespace from this Policies screen. We will be getting list of hardening policies for the selected Namespace.

![app-harden-accuknox](images/app-harden-1.png)

2.Applying the hardening policies

3.Selecting the below hardening policy to apply

![app-harden-accuknox](images/app-harden-2.png)

4.Select this policy and click on the apply option

![app-harden-accuknox](images/app-harden-3.png)

5.After applying the above hardening policy, it goes into pending state

![app-harden-accuknox](images/app-harden-4.png)

6.To make it active the user needs to approve

![app-harden-accuknox](images/app-harden-5.png)

7.After approval policy goes into active state.

![app-harden-accuknox](images/app-harden-6.png)

- - -
[SCHEDULE DEMO](https://www.accuknox.com/contact-us){ .md-button .md-button--primary }
