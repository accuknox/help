> For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.prismacloud.io/content-collections/runtime-security/compliance/visibility/prisma-cloud-compliance-checks.md).

# Prisma Cloud Compliance Checks

Twistlock Labs compliance checks are designed by our research team and fill gaps not offered by other benchmarks. Like all compliance checks, Prisma Cloud’s supplementary checks monitor and enforce a baseline configuration across your environment.

Twistlock Labs compliance checks can be enabled or disabled in custom rules. New rules can be created under **Defend > Compliance > Policy**.

## Container Checks

**596 — Potentially dangerous NET\_RAW capability enabled**\
Checks if a running container has the NET\_RAW capability enabled. This capability grants an application the ability to craft raw packets. In the hands of an attacker, NET\_RAW can enable a wide variety of networking exploits, such as ARP-spoofing and hijacking a cluster’s DNS traffic.

**597 — Secrets in clear text environment variables (container and serverless function check)**\
Checks if a running container (instantiated from an image) or serverless function contains sensitive information in its environment variables. These env vars can be easily exposed with docker inspect, and thus compromise privacy.

**598 — Container app is running with weak settings**\
Weak settings incidents indicate that a well-known service is running with a non-optimal configuration. This covers settings for common applications, specifically: Mongo, Postgres, Wordpress, Redis, Kibana, Elastic Search, RabbitMQ, Tomcat, Haproxy, KubeProxy, Httpd, Nginx, MySql, and registries. These check for things such as the use of default passwords, requiring SSL, etc. The output for a failed compliance check will contain a "Cause" field that gives specifics on the exact settings detected that caused a failure.

**599 — Container is running as root (container check)**\
Checks if the user value in the container configuration is root. If the user value is 0, root, or "" (empty string), the container is running as a root user, and the policy’s configured effect (ignore, alert, or block) is actuated.

## Container Image Checks

**422 — Image contains malware (image check)**\
Checks if any binary file in the image matches the MD5 checksum for known malicious software in the database. For this check, we use the database composed of our Intelligence Stream (IS) and WildFire. We check the CI images for malware by WildFire detection and check deployed images by MD5 detection. You can populate MD5 by adding them to the [**Manage > System > Custom feeds > Malware signatures**](/content-collections/runtime-security/configure/custom-feeds.md#_create_a_list_of_malware_signatures_and_trusted_executables), these signatures added by you will also be checked for any malicious software. Whether the user updates the MD5 on the custom-feed page or not, we will always check the images with the Intelligence Stream and Wildfire.

**423 — Image is not trusted (image check)**\
Checks if unauthorized (untrusted) images are pulled or loaded into your environment.

Prisma Cloud provides a mechanism to specify specific registries, repositories, and images that are considered trusted. Enable this check to prevent unauthorized containers from running in your critical environment. For more information, see [Trusted images](/content-collections/runtime-security/compliance/operations/trusted-images.md).

**424 — Sensitive information provided in environment variables (image and serverless function check)**\
Checks if images or serverless functions contain sensitive information in their environment variables. Container images define environment variables with the Dockerfile ENV instruction. These environment variables can be easily exposed with *docker inspect*. These checks use pattern-matching with various terms related to secrets, and no extra analysis is done on these environment variables. These checks can detect private keys, Amazon access keys (for example `AKIAIOSFODNN7EXAMPLE`), and key-values secrets with known keys (for example "token=fdfsfgsdfkjbsdkf").

**425 — Private keys stored in image (image and serverless function check)**\
Opens the file with an image or serverless function, and uses a regex pattern to search only for private keys. A policy effect (ignore, alert, block) is applied on deployment if any private key is found.

**426 — Image contains binaries used for crypto mining (image check)**\
Detects when there are crypto miners in an image. Attackers have been quietly poisoning registries and injecting crypto mining tools into otherwise legitimate images. When you run these images, they perform their intended function, but also mine Bitcoin for the attacker. This check is based on research from Prisma Cloud Labs. For more information, see [Real World Security: Software Supply Chain](https://dockercon.docker.com/watch/T2xVKBNbq255j56Hecd1XZ). The improved search logic detects binaries with known crypto miners. The following examples from Docker Hub include crypto miners that we identify:

[Ethereum CUDA Miner](https://hub.docker.com/r/anthonytatowicz/eth-cuda-miner/)

[BFGMiner](https://hub.docker.com/r/wernight/bfgminer)

The output message does not include remediation details, only that the binary is identified as a crypto miner.

**448 — Package binaries should not be altered**\
Checks the integrity of package binaries in an image. During an image scan, every binary’s checksum is compared with its package info. If there’s a mismatch, a compliance issue is raised.

Besides scan-time, this compliance issue can also be raised at run-time if a modified binary is spawned.

## Prisma Cloud Labs Istio Compliance Checks

Istio compliance checks help enforce a secure Istio configuration. They address risks such as misconfigured TLS settings and universally scoped service roles.

The goals of the compliance rules are to:

* Ensure mutual TLS is configured correctly (enabled over HTTPS).
* Ensure RBAC policy is configured with service level access control (service x can only talk with service y).
* Ensure RBAC policy is not too permissive.

### Istio Checks

**427 — Configure TLS per service using Destination Rule traffic policy**

**450 — Enable mesh-wide mutual TLS authentication using Peer Authentication Policy**

**451 — Avoid using permissive authorization policies without rules as it can compromise the target services**

**452 — Enable Istio access control on all workloads in the mesh using Authorization Policies**

In Istio versions 1.6 and later, Mesh Policy is deprecated and replaced with Peer Authentication Policy.

## Linux Host Checks

**449 — Ensure no pending OS security updates**

On each host scan, Prisma Cloud checks for available package updates marked as security updates. If such updates are found, they’re listed under the security updates tab in **Monitor > Runtime > Host observations > \<HOST>** Supported for Ubuntu and Debian hosts only.

## Malware Checks

Agentless scanning scans your workloads for malware by using an integration with [Palo Alto Networks Advanced WildFire](https://www.paloaltonetworks.com/network-security/advanced-wildfire), the industry’s leading malware scanning feed.

Malware scanning covers malicious files known as Malware and also Grayware, which are unwanted applications or files that are not classified as malware, but can worsen the performance of workloads and cause security risks.

### Agentless Malware Detection

When agentless scanning checks your hosts and container images for security risks, it calculates the MD5 signatures of the [relevant files](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/enterprise-edition/content-collections/runtime-security/compliance/visibility/.md/README.md#support) for malware analysis. Agentless malware detection uses the following process.

1. The agentless scan concludes for vulnerabilities and compliance issues.
2. Prisma Cloud sends the list of signatures to WildFire to determine their verdicts.
3. While a workload is pending verdicts from WildFire, a relevant status shows up in the workload scan results.

   The possible verdicts are:

   * Malware
   * Grayware
   * Benign

     By default, Prisma Cloud only reports files flagged as malware and you can [enable flagging of grayware](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/enterprise-edition/content-collections/runtime-security/compliance/visibility/.md/README.md#grayware).
4. All verdicts are received and the appropriate status is set on the [workload malware status](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/enterprise-edition/content-collections/runtime-security/compliance/visibility/.md/README.md#status).

### Configuration

Malware scanning is a default capability for all hosts and container images scanned by agentless.

Malware scanning is incorporated into Prisma Cloud Compute as compliance checks: **ID 454** - Host file is flagged as malware by WildFire **ID 455** - Image file is flagged as malware by WildFire

#### Enable Flagging Of Grayware

1. Select **Runtime Security > Manage > System > WildFire**.
2. Under the Advanced configuration section, enable **Treat grayware as malware**.

### Results

Once an agentless scan is complete, go to **Runtime Security > Monitor > Compliance > Images** or to **Runtime Security > Monitor > Compliance > Host** to see the results for a deployed image or a host.

Go to **Runtime Security > Monitor > Compliance** to find the malware scanning results in the [Prisma Cloud Compliance Explorer](/content-collections/runtime-security/compliance/visibility/compliance-explorer.md) after an agentless scan was completed successfully.

It can take some time for the **Malware status** to appear in the **Host** and **Image details** and the status shows as **Pending** until Advanced WildFire reports the verdicts. Malware analysis results are reported asynchronously only after a host scan is completed for vulnerabilities and other compliance issues. You can see the results of an agentless scan for vulnerabilities and other compliance issues in your deployment before the **Malware status** is resolved. Given the large number of binaries found in Windows systems, malware scanning results will take longer to conclude.

### Workload Malware Status

The following malware scan statuses are possible.

* Pending Verdicts
* No issues found
* The number of issues found

You can’t allowlist specific malware results, but you can allowlist all malware results from specific workloads by scoping compliance rules.

### Supported Environments and Files

Malware scanning is supported only for hosts scanned by agentless and images of containers running on those hosts since it is done in an offline manner on a snapshot and not on a running host. Calculating signatures of all relevant files on a filesystem with a Defender would have performance implications on a running workload.

#### Supported Cloud Service Providers

Supported for the following cloud service providers.:

* GCP
* AWS
* Azure
* OCI

#### Linux Hosts and Container Images

Supports scanning binaries - ELF files.

#### Windows Hosts

Supports all executable types and shared libraries.

### Defenders Malware Detection

Defenders also check your [container images for malware](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/enterprise-edition/content-collections/runtime-security/compliance/visibility/.md/README.md#container-image).


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.prismacloud.io/content-collections/runtime-security/compliance/visibility/prisma-cloud-compliance-checks.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
