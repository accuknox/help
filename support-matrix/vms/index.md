---
title: Virtual Machines and Baremetals Support Matrix
description: AccuKnox cloud security tools also supports virtual machine and baremetal workloads with the help of KVMservice.
---

# Virtual Machines / Bare Metal Support Matrix

AccuKnox cloud security tools support seamless discovery, policy enforcement, and process monitoring for virtual machines and baremetal workloads via lightweight agents and VM-specific components.

## Linux VM Vulnerability Scanning

| OS                          | Supported Versions                  | Package Managers       |
| --------------------------- | ----------------------------------- | ---------------------- |
| Alpine Linux                | 2.2–2.7, 3.0–3.22, edge             | apk                    |
| Red Hat Enterprise Linux    | 6, 7, 8, 9                          | dnf / yum / rpm        |
| CentOS                      | 6, 7, 8                             | dnf / yum / rpm        |
| AlmaLinux                   | 8, 9, 10                            | dnf / yum / rpm        |
| Rocky Linux                 | 8, 9                                | dnf / yum / rpm        |
| Oracle Linux                | 5, 6, 7, 8                          | dnf / yum / rpm        |
| Azure Linux (CBL-Mariner)   | 1.0, 2.0, 3.0                       | tdnf / dnf / yum / rpm |
| Amazon Linux                | 1, 2, 2023                          | dnf / yum / rpm        |
| openSUSE Leap               | 42, 15                              | zypper / rpm           |
| SUSE Linux Enterprise       | 11, 12, 15                          | zypper / rpm           |
| SUSE Linux Enterprise Micro | 5, 6                                | zypper / rpm           |
| Photon OS                   | 1.0, 2.0, 3.0, 4.0, 5.0             | tdnf / yum / rpm       |
| Debian GNU/Linux            | 7, 8, 9, 10, 11, 12                 | apt / dpkg             |
| Ubuntu                      | All versions supported by Canonical | apt / dpkg             |
| Bottlerocket                | 1.7.0 and newer                     | bottlerocket           |

<!-- > The above table is based on the [Trivy documentation: Supported OS](https://trivy.dev/docs/latest/guide/coverage/os/#supported-os). -->

!!! info "Note"
    Malware scanning is independent of distribution.

---

[SCHEDULE DEMO](https://www.accuknox.com/contact-us){ .md-button .md-button--primary }
