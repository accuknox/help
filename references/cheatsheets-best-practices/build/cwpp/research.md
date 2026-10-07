# CWPP cheat sheet research

Module: `cwpp`. Slug: `cwpp-best-practices-guide`. Campaign: `cwpp-cheat-sheet`. Opened on 2026-10-07.

## Problem data points, each opened

| # | Number | Exact wording on the page | Publisher, year | URL opened | Used on |
|---|---|---|---|---|---|
| 1 | 10 minutes | "the average time from recon to attack completion is now only 10 minutes." | Sysdig, 2023 Global Cloud Threat Report press release, 2023-08-02 | https://www.sysdig.com/press-releases/2023-cloud-threat-report | p2 |
| 2 | 45% | "45% of respondents reported that their organizations experienced runtime incidents in the last 12 months." | Red Hat, State of Kubernetes Security report, 2024 | https://www.redhat.com/en/resources/kubernetes-adoption-security-market-trends-overview | p2 |
| 3 | $53 per $1 | "Attackers make $1 for every $53 a victim is billed." Also: $8,100 mined, more than $430,000 in victim cloud cost | Sysdig, 2022 Cloud Native Threat Report press release, 2022-09-28 | https://sysdig.com/press-releases/sysdig-threat-report-reveals-victims-lose-53-for-every-1-cryptojackers-gain | p2 |
| 4 | 11 days | "Global median dwell time rose to 11 days from 10 days in 2023." | Mandiant (Google Cloud), M-Trends 2025, 2025-04-24 | https://cloud.google.com/blog/topics/threat-intelligence/m-trends-2025/ | p3 |
| 5 | 60% | "60% of containers now live for 60 seconds or less." | Sysdig, 2025 Cloud-Native Security and Usage Report press release, 2025-03-12 | https://www.sysdig.com/press-releases/2025-usage-report | p3, p10 |
| 6 | 86% | "Of 50 recently compromised GCP instances, 86% of the compromised Cloud instances were used to perform cryptocurrency mining" | Google Cybersecurity Action Team, Threat Horizons, November 2021 | https://services.google.com/fh/files/misc/gcat_threathorizons_brief_nov2021.pdf | p9 |
| 7 | 67% | "67% of respondents have delayed or slowed down deployment of container-based applications due to security concerns." | Red Hat, State of Kubernetes Security report, 2024 | https://www.redhat.com/en/resources/kubernetes-adoption-security-market-trends-overview | not used |

Dropped: the Google "22 seconds" claim (press coverage only, the text was not in the PDF text layer), the Sysdig 2024 "70% of containers live 5 minutes or less" (superseded by the 2025 figure), and the Red Hat 2024 blog URL (404).

## Product truth, help docs opened

| Claim used | Doc |
|---|---|
| eBPF sensor in kernel space, LSM enforcer (LSM BPF and AppArmor), default mode is Audit, no inline proxy, no sidecar, enforcement continues without control plane connectivity, degrades to visibility only without eBPF and LSM | `docs/getting-started/runtime-sec-arch.md` |
| Eight step Runtime Security Journey, step 5 loops to step 2, AUDIT for 2 to 3 weeks, STABLE then BLOCK | `docs/use-cases/cwpp.md`, `app-behavior.md`, `zero-trust.md` |
| Discovery Engine, App Behavior file, process and network observability | `docs/use-cases/app-behavior.md` |
| Hardening policies from CIS, MITRE ATT&CK, NIST 800-53, PCI DSS and STIG, apply then approve then active | `docs/use-cases/app-hardening.md` |
| Hardening cards: package tools, /tmp/ noexec, service account token, restrict capabilities (NET_RAW), admin and discovery tools, ICMP control, logs delete | `docs/use-cases/hardening.md`, `docs/use-cases/cards/*.md` |
| Post attack mitigation versus inline mitigation, AppArmor, BPF LSM, SELinux for host only | `docs/faqs/runtime-security.md` |
| Unknown malware and unknown signatures rejected in BLOCK mode | `docs/use-cases/zero-trust.md` |
| Process whitelisting, process based network control, process based asset access | `docs/use-cases/zero-trust.md`, cards |
| Pods talk to all pods by default, discovered network policies, Pending then approve then Active | `docs/use-cases/network-segmentation.md`, `cards/Network-Segmentation.md` |
| Same node pods share Layer 2 across namespaces | `cards/Restrict-Capabilities.md` |
| Miner policy blocks /tmp/ execution, xmrig, dero, masscan, zgrab2, nmap, apt, apk, ntpdate, read only system binary folders, exit status 126 | `docs/use-cases/crypto-mining.md` |
| FIM read only folders, PCI DSS, NIST and CIS expect FIM | `cards/FIM.md`, `docs/use-cases/vm-file-integrity.md` |
| Process, file, network, syscall forensics, sensitive asset audit of /etc/shadow, /etc/sudoers, /etc/pam.d/ | `docs/use-cases/forensics.md`, cards |
| Forward alerts to Splunk, ELK, Rsyslog | `docs/integrations/telemetry-alerts.md` |

CDR (`docs/use-cases/cdr.md`) covers cloud control plane events, not workloads, so the guide leaves it out. `iot-edge-security.md` holds one link only, so the guide makes no IoT claim.

## accuknox.com proof points

| Fact | URL |
|---|---|
| KuppingerCole 2026 CNAPP Leadership Compass highlights AccuKnox eBPF based runtime enforcement | https://accuknox.com/analyst-recognition/ |
| Andrew Green named AccuKnox in the Runtime Environment group for kernel level enforcement | https://accuknox.com/analyst-recognition/ |
| KubeArmor, created by AccuKnox, performs inline mitigation against zero day attacks | https://accuknox.com/platform/cwpp (cite returned 200) |

## Screenshots

| File | Source | Pixels |
|---|---|---|
| `img/arch.png` | `docs/getting-started/images/deep-arch/1.png`, cropped to the diagram | 1920 wide |
| `img/app-behavior.png` | `docs/use-cases/images/app-behavior-4.png` | 1600 x 748 |
| `img/hardening.png` | `docs/getting-started/images/release-notes/v3.5/runtime-policies-bulk-accept-reject.png` | 1920 x 972 |
| `img/block-alert.png` | `references/PRODUCT UI/7_alerts/Alerts 2.png`, alert panel only, raw log with hostname cropped out | 1470 x 1030 |
| `img/network.png` | `docs/use-cases/images/network-1.png` | 1570 x 736 |
| `img/fim-block.png` | `docs/use-cases/images/vm-file-integrity/4.png` | 1920 x 917 |
| `img/alert-log.png` | `references/PRODUCT UI/7_alerts/Alerts 1.png`, filter pills with the tenant ID cropped out | 3250 x 1392 |

`references/PRODUCT UI/6_runtime` shows CSPM and ASPM policy builders, not workload runtime, so no screen from it is used.
