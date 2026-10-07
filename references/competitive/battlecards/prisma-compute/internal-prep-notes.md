# Internal prep, AccuKnox vs Prisma Cloud Compute Edition (bank, on-prem)

Not for the customer. Read before the call. The printed comparison leaves these out on purpose, because each one is a place where Prisma Cloud Compute Edition matches or beats AccuKnox, or where an AccuKnox claim needs engineering confirmation.

## Where Compute Edition is as good or better, so expect the question

- **Offline threat feed.** Compute Edition documents `twistcli` download and upload of the Intelligence Stream to an offline Console (https://docs.prismacloud.io/admin-guide/tools/update-intel-stream-offline). AccuKnox docs say an air-gapped site must build its own push pipeline for NVD, EPSS and KEV updates (docs/faqs/deployment.md). Confirm the supported process with engineering.
- **Console footprint.** The Compute Console runs on any container host, x86_64 only. The AccuKnox on-prem control plane needs its own Kubernetes cluster (1 node at 8 vCPU, 32 GB, 256 GB, or 3 VMs for a POC).
- **Upgrade control.** Both let the customer control upgrades. Compute Edition states n-2 support. The Defender upgrade docs conflict: pcee-vs-pcce says upgrade Defenders by hand, the Helm, onebox and OpenShift upgrade pages say Console auto-upgrades them.
- **Mature workload runtime.** Learned models, Prevent and Block, FIM, OPA admission, Trusted Images and CIS checks all exist. The printed rows show parity there. Win on the modules and KubeArmor, not on "Prisma has no runtime".
- **Windows hosts.** Windows Host Defender has no process, network or filesystem runtime protection in Compute Edition. AccuKnox has no documented Windows runtime enforcement either. Do not use this row.

## AccuKnox claims that need confirmation before a bank sees them

- **Air-gapped install.** docs/getting-started/on-prem-installation-guide.md lists internet access as mandatory for the 3 VM install. Air-gapped installs use the private registry path. Have an engineer walk the bank through it.
- **ML model scan on-prem.** docs/how-to/ml-static-scan.md says the scan runs in the AccuKnox sandbox evaluator. docs/how-to/aiml-saas-vs-onprem.md claims parity. Row dropped from the PDF until product confirms.
- **Cloud-dependent features on-prem.** CSPM, CDR, S3 secrets and public-exposure checks need the on-prem control plane to reach cloud APIs and logs. They do nothing in a fully air-gapped site.
- **SAST AI triage** needs an external API key, so it does not run air-gapped. The printed SAST cell omits it.
- **AccuKnox data-usage policy** (docs/resources/data-usage-policy.md) still holds an unfilled `<ANSWER>` placeholder on how updates are fetched. A bank on data residency will ask.
- **ConfigMap secrets and fileless malware** rows were dropped. Their AccuKnox evidence is a demo card and an assertion with no doc.
- **Data Access Verification and Data Policy Controls** are "Coming soon" in AccuKnox. Rows dropped.

## Other findings

- **IaC scanning row dropped.** One Compute page says `twistcli` scans IaC templates. No Compute page documents an IaC command or template list. Ask Palo Alto Networks before claiming a gap.
- **Product status.** Compute Edition is current (docs at /admin-guide/, n-2 support). Palo Alto Networks lists end-of-life only for versions up to 22.12. No end-of-sale for Compute Edition was found. Cortex Cloud is the successor brand, so a Palo Alto Networks rep may steer the bank there.
- **The stronger argument for a bank.** On-prem Compute Edition covers workloads only. The posture module sits in Enterprise Edition, which Palo Alto Networks runs as SaaS (product-architecture page). The Enterprise Edition research dated 2026-09-30 places code security, DSPM and AI security there too. That breaks the bank's data residency need.
