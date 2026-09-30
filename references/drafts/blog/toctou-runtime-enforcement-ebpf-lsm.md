---
title: "TOCTOU Attacks Beat the Scanner by Design. Only Enforcement at Time-of-Use Closes the Gap"
seo_title: "TOCTOU Attacks: Why Runtime Enforcement Stops Them"
meta_description: "A TOCTOU attack passes every scan, then swaps the resource before it is used. Here is how the race works and why kernel enforcement at time-of-use is the only fix."
slug: "toctou-runtime-enforcement-ebpf-lsm"
url: "https://accuknox.com/blog/toctou-runtime-enforcement-ebpf-lsm"
primary_keyword: "TOCTOU attack"
secondary_keywords: ["time of check time of use", "race condition security", "eBPF LSM enforcement", "container escape TOCTOU"]
excerpt: "A TOCTOU attack passes the check, then swaps the resource before it is used. Scanners validate once and trust forever. Enforcement at the syscall is the only control that holds."
category: "CNAPP"
author: "Atharva Shah"
reading_time: "5 minutes"
word_count_target: 1100
audience: "platform engineer | security engineer"
cover_image_prompt_claude: >
  An isometric illustration of two moments on a timeline: a green checkmark at the check
  point, a red swapped file icon at the use point, with a kernel-level gate sitting on the
  use point. AccuKnox navy #11206D on white with #003BF6 accents, flat vector, generous
  negative space, no text anywhere in the image.
cover_image_prompt_midjourney: >
  isometric timeline two moments green check then red swapped file, kernel gate on the use
  point, race condition concept, navy #11206D white #003BF6, flat vector, negative space
  --ar 16:9 --style raw --v 6 --no text
---

# A TOCTOU attack passes every scan, then swaps the resource before you use it

> **Cover image prompt:** Two moments on a timeline, a green check at the check point and a red swapped file at the use point, with a kernel gate on the use point. AccuKnox navy `#11206D` on white with `#003BF6` accents, flat vector, no text.

## TL;DR

- A TOCTOU (Time-of-Check to Time-of-Use) attack exploits the gap between the moment a program checks a resource and the moment it uses it. In that window, an attacker swaps the resource for a malicious one.
- Anything that validates once and trusts afterward is bypassable by design. A scanner, an admission check, and a `setuid` program that calls `access()` then `open()` all share this flaw.
- The classic case is a symlink swap: a privileged program checks a file it is allowed to write, an attacker points that name at `/etc/passwd`, and the program overwrites the system password file.
- The fix is not a better check. It is enforcement at time-of-use, where the policy decision fires at the syscall the operation actually runs on.
- [AccuKnox](https://accuknox.com/platform/runtime-security), built on the open-source [KubeArmor](https://accuknox.com/open-source) engine, enforces through eBPF and Linux Security Modules whose hooks fire after the kernel resolves the real object, so the check and the use become the same event.

## The race, in one concrete example

TOCTOU is a race condition. A program checks a property of a resource, then acts on the result of that check. The bug exists because the two steps are not atomic: another process can run in between and change the property, so the second step operates on stale information. The [Wikipedia entry on TOCTOU](https://en.wikipedia.org/wiki/Time-of-check_to_time-of-use) documents the pattern and its history.

The textbook example is a `setuid` program that wants to write a file on behalf of a real user:

```c
if (access("file", W_OK) != 0) exit(1);   // time of check
fd = open("file", O_WRONLY);              // time of use
write(fd, data, len);
```

`access()` checks the real user's permission, which is correct. Between that call and `open()`, an unprivileged attacker runs `symlink("/etc/passwd", "file")`. The check passed against a file the user could write. The `open()` now follows the symlink, and the privileged program overwrites `/etc/passwd`. The security check was real, and it was bypassed anyway, because the resource it validated is not the resource that got used.

This is not a userspace curiosity. The public record includes a 2019 root-access-to-host race in `docker cp` driven by a symlink swap, and a gateway compromise at Pwn2Own 2023, both listed in the same reference. Container filesystems, shared volumes, and CI workspaces are full of the mutable paths this attack needs.

## Why the scanner and the admission gate miss it

A vulnerability scanner reads an image, a manifest, or a filesystem and reports what it found at that instant. An admission controller checks a workload's spec before it is scheduled. Both run at time-of-check. Neither watches what happens at time-of-use.

That is the structural problem. The scan of a container image is honest about the image it scanned, but the running container can mount a writable volume, resolve a symlink, or race a file open that the scan never saw. A 2004 result cited in the reference above showed there is no portable, deterministic userspace fix for the `access`/`open` race. You cannot check your way out of a check-versus-use gap. The defense has to move to the moment of use.

> **Image prompt (inline 1):** A side-by-side comparison, left panel "check-time control" showing a scanner reading a static image with a green pass, right panel "use-time control" showing a kernel LSM hook on a live syscall with a red block. AccuKnox navy `#11206D` on white with `#003BF6` accents, flat vector, no text in the image.
>
> *Caption: A check-time control validates a snapshot. A use-time control decides on the operation itself.*

## Enforcement at time-of-use, through eBPF and BPF-LSM

Linux Security Module (LSM) hooks are decision points inside the kernel that fire before a sensitive operation commits: opening a file, executing a program, loading a library. A [security engineering write-up on hunting TOCTOU with eBPF LSM](https://medium.com/@satyam012005/hunting-toctou-and-ld-preload-attacks-with-ebpf-lsm-ea7f4e6c3884) makes the key point: these hooks fire after the kernel has resolved the path, checked permissions, and validated the inode, so the hook sees the real kernel object, not the user-supplied argument an attacker can still swap.

That timing is the whole game. When the policy runs at the `file_open` hook rather than at the userspace `access()` call, there is no window left to swap the resource, because the decision and the operation are the same event. The same write-up names the hooks that matter for this class: `bprm_check_security` for program execution, `file_open` for file and library access, and `path_symlink` and `path_rename` to catch rapid filesystem changes during an execution window.

AccuKnox uses exactly this layer. [KubeArmor](https://accuknox.com/open-source) enforces policy through eBPF and BPF-LSM at the kernel, at the same privilege level as the operating system, with no userspace agent racing the attacker. Read the mechanics in [how AccuKnox uses eBPF and BPF-LSM](https://accuknox.com/blog/runtime-security-ebpf-bpf-lsm).

> **Existing screenshot (inline 2):** Use the runtime security dashboard from the PRODUCT UI library, `1_dashboard/Runtime sec dash.png`. Crop the browser chrome and redact any tenant name before publishing.
>
> *Caption: Kernel-enforced policy decisions in the AccuKnox console, applied at the operation itself rather than at an earlier check.*

| Control | When it decides | Can an attacker swap the resource after? |
| --- | --- | --- |
| Image or filesystem scanner | Time of check, on a snapshot | Yes, at runtime |
| Admission controller | Time of check, on the spec | Yes, after scheduling |
| Userspace `access()` guard | Time of check, on a path string | Yes, before `open()` |
| KubeArmor LSM enforcement | Time of use, on the resolved object | No, the decision is the operation |

## What enforcement at time-of-use does not do

Runtime enforcement closes the check-versus-use gap on a workload under policy. It does not remove the underlying bug from your code, and a `setuid` binary with a TOCTOU flaw should still be fixed. Enforcement also depends on the LSM being active and the policy covering the sensitive paths, so a path you never restricted is a path the hook will allow.

The point stands regardless. A check that runs once and trusts forever is not a control against an attacker who owns the window after the check. Move the decision to the syscall, and the window disappears. That is the difference between knowing a resource was safe a moment ago and enforcing that it is safe right now.

## Watch KubeArmor enforce policy at the kernel

KubeArmor is the open-source engine behind this enforcement model. This walkthrough covers getting started and three enforcement use cases.

```html
<iframe width="560" height="315" src="https://www.youtube.com/embed/Q4QIkUwj5vI" title="KubeArmor - Getting Started and 3 Use Cases" frameborder="0" allowfullscreen></iframe>
```

[Watch it on the AccuKnox YouTube channel](https://www.youtube.com/watch?v=Q4QIkUwj5vI).

## FAQs

### What does TOCTOU stand for?

Time-of-Check to Time-of-Use. It is a race where an attacker swaps a resource in the gap between a program checking it and using it.

### Why can't a scanner catch a TOCTOU attack?

A scanner reports the state it saw at check time. The swap happens later, at use time, so any control that validates once and trusts afterward is bypassable.

### How does eBPF with BPF-LSM stop TOCTOU?

Its hooks fire in the kernel after the path and inode are resolved, at the moment the operation runs. The decision and the operation are the same event, so no swap window remains.

### Does AccuKnox need a kernel module?

No. It enforces through eBPF and in-tree LSMs such as BPF-LSM and AppArmor. The same model works on Kubernetes, VMs, and bare metal.
