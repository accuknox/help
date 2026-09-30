# Does Prisma Cloud Enterprise Edition detect hardcoded secrets in Kubernetes ConfigMaps, either in repository YAML or in running clusters?

I can’t find any docs that say **Prisma Cloud Enterprise Edition** detects **hardcoded secrets inside Kubernetes ConfigMaps**—either:

* **in repository Kubernetes YAML** (for example, manifests checked into Git), or
* **in running clusters** (for example, existing ConfigMaps in Kubernetes at runtime).

What the docs *do* describe is secrets detection for:

* **Inside container images and containers** (Defender-based “Secrets Detection”), including sensitive data found in **environment variables** of images/containers. See \[Detect secrets]\(mention: [Detect secrets](/admin-guide/33/compliance/detect-secrets.md)).
* **Inside hosts and container image filesystems** (agentless scanning). See the same \[Detect secrets]\(mention: [Detect secrets](/admin-guide/33/compliance/detect-secrets.md)) page.

Separately, Prisma Cloud documents that **IaC scanning is available only with Prisma Cloud Enterprise Edition** via `twistcli`, but the accessible docs don’t specifically mention scanning **Kubernetes ConfigMaps** for hardcoded secrets. See \[twistcli]\(mention: [twistcli](/admin-guide/33/tools/twistcli.md)).

# Suggested Follow-up Questions:

If you need more information, consider asking one of these follow-up questions by performing an HTTP GET request on the URL:

- [Do we scan ConfigMaps for secrets?](https://docs.prismacloud.io?ask=Do%20we%20scan%20ConfigMaps%20for%20secrets%3F)
- [Is IaC scanning enabled for K8s YAML?](https://docs.prismacloud.io?ask=Is%20IaC%20scanning%20enabled%20for%20K8s%20YAML%3F)
- [What exactly counts as a secret in ConfigMaps?](https://docs.prismacloud.io?ask=What%20exactly%20counts%20as%20a%20secret%20in%20ConfigMaps%3F)

# Sources:

- [Secrets](https://docs.prismacloud.io/content-collections/runtime-security/secrets.md)
- [Prisma Cloud Enterprise Edition vs Compute Edition](https://docs.prismacloud.io/content-collections/runtime-security/pcee-vs-pcce.md)
- [Secrets](https://docs.prismacloud.io/admin-guide/secrets/secrets.md)
- [Prisma Cloud Enterprise Edition vs Compute Edition](https://docs.prismacloud.io/admin-guide/33/welcome/pcee-vs-pcce.md)
- [Secrets](https://docs.prismacloud.io/admin-guide/32/secrets/secrets.md)
- [Prisma Cloud Enterprise Edition vs Compute Edition](https://docs.prismacloud.io/admin-guide/32/welcome/pcee-vs-pcce.md)
- [Secrets](https://docs.prismacloud.io/admin-guide/33/secrets/secrets.md)
- [Prisma Cloud Enterprise Edition vs Compute Edition](https://docs.prismacloud.io/admin-guide/welcome/pcee-vs-pcce.md)
- [Scan IaC Files with twistcli](https://docs.prismacloud.io/content-collections/runtime-security/tools/twistcli-scan-iac.md)
- [Deploy the Prisma Cloud Console on Kubernetes](https://docs.prismacloud.io/admin-guide/33/install/deploy-console/console-on-kubernetes.md)
- [Detect secrets](https://docs.prismacloud.io/admin-guide/33/compliance/detect-secrets.md)
- [Detect Secrets](https://docs.prismacloud.io/content-collections/runtime-security/compliance/operations/detect-secrets.md)
- [Detect secrets](https://docs.prismacloud.io/admin-guide/32/compliance/detect-secrets.md)
- [Detect secrets](https://docs.prismacloud.io/admin-guide/compliance/detect-secrets.md)
- [Prisma Cloud Threat Detection](https://docs.prismacloud.io/content-collections/governance/prisma-cloud-threat-detection.md)
- [Prisma Cloud Platform](https://docs.prismacloud.io/content-collections/get-started/prisma-cloud-platform.md)
- [Secrets Stores](https://docs.prismacloud.io/content-collections/runtime-security/secrets/secrets-stores.md)
- [Scan images with twistcli](https://docs.prismacloud.io/admin-guide/32/tools/twistcli-scan-images.md)
- [Scan images with twistcli](https://docs.prismacloud.io/admin-guide/tools/twistcli-scan-images.md)
- [Scan Images with twistcli](https://docs.prismacloud.io/content-collections/runtime-security/tools/twistcli-scan-images.md)
- [Scan images with twistcli](https://docs.prismacloud.io/admin-guide/33/tools/twistcli-scan-images.md)
- [twistcli](https://docs.prismacloud.io/admin-guide/33/tools/twistcli.md)
- [twistcli](https://docs.prismacloud.io/content-collections/runtime-security/tools/twistcli.md)
- [Tools](https://docs.prismacloud.io/admin-guide/33/tools/tools.md)
- [Tools](https://docs.prismacloud.io/admin-guide/tools/tools.md)
- [Tools](https://docs.prismacloud.io/content-collections/runtime-security/tools.md)
- [Tools](https://docs.prismacloud.io/admin-guide/32/tools/tools.md)

