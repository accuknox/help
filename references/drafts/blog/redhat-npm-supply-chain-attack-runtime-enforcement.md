---
title: "32 Red Hat NPM Packages Were Poisoned in 72 Seconds. Runtime Enforcement Is the Only Control That Would Have Held"
seo_title: "Red Hat NPM Supply Chain Attack: Runtime Defense"
meta_description: "A worm poisoned 32 @redhat-cloud-services npm packages and swept credentials from every install. Here is the anatomy, the root cause, and the runtime control that stops it."
slug: "redhat-npm-supply-chain-attack-runtime-enforcement"
url: "https://accuknox.com/blog/redhat-npm-supply-chain-attack-runtime-enforcement"
primary_keyword: "Red Hat npm supply chain attack"
secondary_keywords: ["npm credential stealing worm", "Shai-Hulud npm worm", "runtime enforcement supply chain", "postinstall script attack"]
excerpt: "A credential-stealing worm poisoned 32 @redhat-cloud-services npm packages in a 72-second burst. Detection would have watched it happen. Here is what stops it."
category: "CNAPP"
author: "Atharva Shah"
reading_time: "5 minutes"
word_count_target: 1150
audience: "platform engineer | security engineer"
cover_image_prompt_claude: >
  An isometric illustration of an npm package box on a CI/CD conveyor belt splitting
  into many copies, faint credential keys leaking from each, one kernel-level barrier
  stopping the flow. AccuKnox navy #11206D on white with #003BF6 accents, flat vector,
  generous negative space, no text anywhere in the image.
cover_image_prompt_midjourney: >
  isometric npm package on CI/CD conveyor belt self-replicating, credential keys leaking,
  single kernel barrier blocking exfiltration, navy #11206D white #003BF6, flat vector,
  negative space --ar 16:9 --style raw --v 6 --no text
---

# 32 Red Hat npm packages were poisoned in 72 seconds, and detection would have watched it happen

> **Cover image prompt:** An isometric npm package on a CI/CD conveyor belt splitting into copies, credential keys leaking from each, one kernel-level barrier stopping the flow. AccuKnox navy `#11206D` on white with `#003BF6` accents, flat vector, no text.

## TL;DR

- The Red Hat npm supply chain attack poisoned 32 packages under the `@redhat-cloud-services` scope, which carry close to 10 million collective downloads, with a credential-stealing worm published across a 72-second window that only automation can hit.
- The malware ran during `npm install` through a `preinstall` hook, swept SSH keys, npm and GitHub tokens, and AWS, Azure, GCP and Kubernetes secrets, then committed them to public GitHub repos created under the victim's own account.
- [OX Security](https://www.ox.security/blog/new-shai-hulud-hits-npm-redhat-cloud-services-compromised/) found stolen credentials in over 210 GitHub repositories, and the payload carried a kill-switch that wipes the host if a stolen token is revoked.
- Every stage runs and finishes in seconds, so a detect-and-respond tool logs the theft after the token is already gone.
- Inline enforcement at the kernel, through eBPF and Linux Security Modules, denies the credential read and the unauthorized process before either completes. That is the one control that would have held.

## The attack rode a routine `npm install`, no click required

If your build ran `npm install` on an affected `@redhat-cloud-services` package during the compromise window, the worm ran on your CI runner before a line of application code executed. It rode the package's `preinstall` hook, a script npm runs automatically before the package is even imported, per [SecurityWeek's account](https://www.securityweek.com/supply-chain-attack-hits-32-red-hat-npm-packages/) citing ReversingLabs and Socket.

Once running, the payload swept the machine. Environment variables, SSH keys, npm authentication tokens, GitHub tokens, cloud credentials for AWS, Azure and GCP, and Kubernetes secrets, all read from the well-known paths where build tooling keeps them. OX Security traced the exfiltration: the worm uses the stolen GitHub token to create a public repo on the victim's account, described in the attacker's own words as "Miasma: The Spreading Blight", then commits the encrypted secrets there. It pings `api.anthropic.com` as a decoy command channel to send researchers down the wrong path, while the real theft lands in that GitHub repo.

Two details raise this above a routine token grab. The worm self-replicates: it uses stolen npm tokens to republish backdoored versions of other packages the compromised account controls, so each victim becomes the next carrier. And the payload ships a destructive kill-switch that deletes the host if a stolen token is invalidated, which turns incident response itself into a trigger.

> **Image prompt (inline 1):** A five-step horizontal kill-chain, left to right: npm install, preinstall hook fires, credential sweep, exfil to attacker-owned GitHub repo, self-replicate to next package. AccuKnox navy `#11206D` on white with `#003BF6` accents, flat vector, no text in the image.
>
> *Caption: The Red Hat npm worm kill chain, from install hook to self-propagation, every stage completing in seconds.*

## The root cause is install-time code execution on a trusted package

The npm ecosystem lets a package run arbitrary code at install through lifecycle hooks like `preinstall` and `postinstall`. That is the enabler. A developer who trusts the `@redhat-cloud-services` name gets attacker code the moment the package unpacks, with the full permissions of the build user.

The delivery was not a guessed password. SecurityWeek reports, citing Aikido and ReversingLabs, that the attackers likely compromised the CI/CD pipeline and abused GitHub Actions OIDC to publish the poisoned versions, and probably held valid credentials for the `@redhat-cloud-services` npm scope. The 72-second publish burst across all 32 packages is the signature of an automated pipeline, not a person.

This is the same playbook that hit four SAP packages weeks earlier, which we broke down in [the SAP npm attack analysis](https://accuknox.com/blog/sap-npm-supply-chain-attack-runtime-security-mitigation). Both trace to the Shai-Hulud worm family. The threat actor TeamPCP open-sourced the Mini Shai-Hulud code, so copycats now assemble these campaigns from a published kit. Expect more, not fewer.

## Why detect-and-respond loses this race

Endpoint and workload detection tools work on a fixed loop: observe the behavior, raise an alert, run a response. Kill the process, quarantine the file, page the SOC. That loop has a built-in delay, and this attack finishes inside it.

The worm reads a credential file, encrypts the contents, and pushes them to a remote repo in seconds. By the time a detector scores the anomaly and starts a response, the npm token is already in the attacker's repo and the worm is publishing under the victim's name. Detection after exfiltration is a postmortem. It tells you which credentials to rotate, not that they are safe.

## How inline runtime enforcement stops it at the kernel

The only control that beats a seconds-long attack is one that decides before the operation returns. [AccuKnox runtime security](https://accuknox.com/platform/runtime-security), built on the open-source [KubeArmor](https://accuknox.com/open-source) engine and enforced through eBPF and Linux Security Modules, evaluates policy inline at the syscall, at the same privilege level as the operating system. There is no userspace agent racing the attacker.

| Attack stage | What the worm does | The inline control that blocks it |
| --- | --- | --- |
| Process spawn | Runs an unknown script or downloaded runtime through the install hook | [Process whitelisting](https://help.accuknox.com/use-cases/cards/Process-Whitelisting/) denies any binary outside the allowed set at `SYS_EXECVE` |
| Credential read | Reads SSH keys, cloud configs, tokens, and `/proc/self/environ` | [File-access policy](https://help.accuknox.com/use-cases/cards/Sensitive-Asset-audit/) denies unauthorized reads of sensitive paths at `SYS_OPEN` |
| Exfiltration | Pushes encrypted secrets to an attacker-owned GitHub repo | Network policy denies egress to endpoints outside the allowed list |

Each row is a hard denial, not a log line. The install hook can fire, but the credential read never returns the file contents, and the egress never reaches the repo. Because the decision happens at kernel speed, there is no window between detection and response for the worm to exploit. The [CWPP enforcement layer](https://accuknox.com/platform/cwpp) applies the same model on Kubernetes runners, VMs, and bare-metal build servers.

> **Existing screenshot (inline 2):** Use the runtime protection view from the PRODUCT UI library, `6_runtime/Runtime 1.png`. Crop the browser chrome and redact any tenant name before publishing.
>
> *Caption: Runtime enforcement in the AccuKnox console, where an unlisted process is denied at the syscall rather than logged after it runs.*

## What this does not cover, and where to look next

Runtime enforcement stops the theft on a workload you control and have put under policy. It does not remove the poisoned package from your dependency tree, and it does not help on an unmanaged laptop with no enforcement agent. Pair it with a software bill of materials so you can answer which builds pulled an affected version. AccuKnox generates that through [xBOM](https://accuknox.com/blog/xbom-security-explained) and [SBOM tooling](https://accuknox.com/solutions/sbom), and an admission controller can block a workload whose BOM carries a flagged component before it ever deploys.

Treat install-time code execution as hostile by default. The package registries will not fix this soon, the attack kit is public, and the next poisoned scope is a matter of when. Default-deny execution and least-privilege file access on your build environment is the control that holds when the next trusted name turns.

## See runtime enforcement stop an attack in real time

The same inline model that would have blocked this worm is shown here stopping a live exploit at the kernel.

```html
<iframe width="560" height="315" src="https://www.youtube.com/embed/nSzlMm7QiBM" title="Block Log4j Attack with AccuKnox" frameborder="0" allowfullscreen></iframe>
```

[Watch it on the AccuKnox YouTube channel](https://www.youtube.com/watch?v=nSzlMm7QiBM).

## FAQs

### What was the Red Hat npm supply chain attack?

A credential-stealing worm poisoned 32 packages in the `@redhat-cloud-services` scope, published in a 72-second burst. It ran during `npm install`, swept developer and cloud credentials, and self-replicated to other packages.

### How is this different from the earlier SAP npm attack?

Both belong to the Shai-Hulud family. This one hit far more packages, rebranded as "Miasma", used `api.anthropic.com` as a decoy channel, and added a kill-switch that wipes the host if a stolen token is revoked.

### Why can't detection tools stop it?

The sweep and exfiltration finish in seconds during a routine install. A detect-and-respond tool alerts after the tokens are already gone.

### How does AccuKnox prevent it?

It enforces inline at the kernel through eBPF and LSM: unauthorized execution is denied at `SYS_EXECVE`, credential reads at `SYS_OPEN`, and egress to unapproved endpoints is blocked. The theft never completes.
