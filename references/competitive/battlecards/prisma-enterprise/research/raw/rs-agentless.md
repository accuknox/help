> For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.prismacloud.io/content-collections/runtime-security/agentless-scanning.md).

# Agentless Scanning

Agentless scanning lets you inspect the risks and vulnerabilities of a cloud workload without having to install an agent or affecting the execution of your workload. Prisma Cloud gives you the flexibility to choose between agentless and agent-based security using Defenders. Prisma Cloud supports agentless scanning of cloud workloads on AWS, Azure, GCP, and OCI for vulnerabilities and compliance.

In AWS, Azure, and GCP you can also use agentless scanning for container images as well as [Serverless functions](/content-collections/runtime-security/vulnerability-management/scan-serverless-functions.md).

Azure Virtual Machines with Trusted Launch enabled are not supported for scanning by Prisma Cloud in Agentless mode.

Follow the [step-by-step instructions to configure agentless scanning](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/enterprise-edition/content-collections/runtime-security/agentless-scanning/configure-accounts/configure-accounts.md) and start scanning your AWS, Azure, GCP, and OCI accounts for vulnerabilities and configuration risks with agentless scanning.

Once you onboard your cloud account with agentless scanning enabled, that account is continuously scanned regardless of how many workloads are under that account. Whether you add or remove hosts and containers, agentless scanning keeps your workload’s security issues visible.

When onboarding an organization into Prisma Cloud and enabling agentless scanning across the organization, agentless scanning automatically scans accounts added to the organization.

To achieve that goal, you grant the needed permissions during onboarding and Prisma Cloud scans the account regularly. By default, agentless scans are performed periodically every 24 hours and this interval is [configurable](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/enterprise-edition/content-collections/runtime-security/agentless-scanning/configure-accounts/configure-accounts.md#start-agentless-scan).

## Agentless Scanning Process

To understand the process of agentless scanning, it is important to understand how cloud service providers group workloads. At a fundamental level, workloads are grouped by region. Agentless scans are performed regionally. Once you add your cloud account to Prisma Cloud and enable agentless scanning, the scanning infrastructure is deployed within each region of your project, account, organization, or subscription with workloads.

At a high level, Agentless scanning performs the following steps.

1. Validates that the Prisma Cloud role for the onboarded cloud account has the appropriate permissions and that those permissions are not blocked by an organizational policy.
2. Lists the hosts within the onboarded cloud accounts and the containers running on those hosts.
3. Creates a snapshot for each host in the onboarded cloud accounts. The snapshots are copies of the hosts' volume regardless of whether they are encrypted or not.
4. Creates scanner instances in each region with deployed workloads.
5. Creates the needed [networking infrastructure](#networking-infrastructure) in each region. The networking infrastructure is required to allow the scanner instances to report the scan results back to Prisma Cloud.
6. Attaches each snapshot to the corresponding scanner instance in each region.
7. Scans each snapshot for vulnerabilities and compliance issues on the host or on containers running on that host.
8. Reports the scan results back to Prisma Cloud.
9. Cleans up all snapshots, network infrastructure, and scanner instances provisioned to perform the scan from your onboarded cloud accounts. This cleanup removes the resources that were set up from your cloud account until the next scan.

In the cloud accounts page you can see the general scan progress you can see the status of the agentless scan of a specific account, for example, **scanning** and **completed**, and you can sort accounts by status.

## Networking Infrastructure

Agentless scanning automatically deploys the network infrastructure that the scanner requires to report the scan results back to Prisma Cloud. By default, scanners are attached to a public IP address and the networking infrastructure deployed only allows egress traffic and blocks all ingress traffic.

<figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-553c7a86f27942343c641c17efba19791a018bf4%2Fnetworking-infrastructure.png?alt=media" alt="networking infrastructure"><figcaption></figcaption></figure>

If you require the scanners to use a private IP address or prefer to disallow Prisma Cloud from creating the network infrastructure automatically, it is required that you deploy and maintain the network infrastructure to enable the communication between the scanners and Prisma Cloud.

Ensure that you follow these guidelines.

* Create your own network infrastructure using the network resources available in each cloud service provider.
* Ensure that any hosts using your network infrastructure can connect to the Prisma Cloud console.
* Configure the relevant network resources under **Runtime Security > Manage > Cloud accounts > Edit Cloud Account > Agentless scanning > Advanced settings**.
  * In [AWS](/content-collections/runtime-security/agentless-scanning/configure-accounts/configure-aws.md#aws-agentless-network): Specify the deployed Security group.
  * In [Azure](/content-collections/runtime-security/agentless-scanning/configure-accounts/configure-azure.md#azure-agentless-network): Specify the deployed Security group ID and Subnet ID.
  * In [GCP](/content-collections/runtime-security/agentless-scanning/configure-accounts/configure-gcp.md#gcp-agentless-network): Specify the deployed subnet name or a shared VPC.
  * In [OCI](/content-collections/runtime-security/agentless-scanning/configure-accounts/configure-oci.md): Specify the VCN, Subnet, or Security group.

These settings are mandatory to allow scanners to use a private IP address. After you configure them, the next time an agentless scan is performed the default networking infrastructure is not provisioned. Instead, the scanners use these settings for the egress traffic to communicate to the Prisma Cloud console.

To minimize the permissions used by agentless scanning, you can optionally remove the permissions used to create and delete network resources. Check the networking information in the [Permissions by feature page](/content-collections/runtime-security/configure/permissions.md). Once you remove the permissions, no network resources are created or deleted but you can expect to see the following error:

```
Failed cleaning up network resources: UnauthorizedOperation: You are not authorized to perform this operation.
```

This error is expected because the Prisma Cloud role doesn’t have the permissions and the validation process generates this message. You can ignore the message if you deploy and maintain the networking infrastructure for the agentless scanning process.

## Scan Progress and Statuses

During a scan, the accounts display the following statuses:

* **New** - Indicates that the account was added either during an ongoing scan or between scan cycles.
* **Scanning** - Indicates that the scan process is in progress, which includes pre-flight checks for permissions.
  * Hosts that have completed scanning appear immediately in the scan results; there is no delay until the end of a scan cycle.
  * In this state, all scanners, snapshots, and disks are cleaned up immediately.
* **Cleanup** - Indicates that if networking resources were created, they are cleaned up across all accounts and regions. Note: Accounts move to this state of networking resources cleanup only after all accounts have finished scanning.
* **On** - Indicates the completion of both scanning and cleanup, with the account waiting for either networking resources cleanup state or the next scheduled scan.

If any errors occur during the scan process, they appear in the "Agentless issues" column.

## Scan Cycle Length

It is nearly impossible to estimate what is the end-to-end duration of a scan cycle since it depends on a variety of factors, for example.

* Number of hosts
* Hosts disks sizes
* Used space on hosts disks
* Number of files in the hosts disks
* How the hosts are dispersed between accounts and regions, for example: a single account with a single region that contains 100 hosts, is scanned faster than 10 accounts with 10 regions each, that contains a single host in every region.
* CSP-related factors:
  * API calls latency
  * API calls errors

## Snapshots Creation

During the agentless scanning process, Prisma Cloud iterates through all regions within your environment and creates a snapshot of each host in every region. To mitigate the security risk that non-running hosts pose,you can enable agentless scanning and scan non-running hosts by configuring the agentless scanning for every account you onboard. Each scanner instance is attached with a maximum of 26\* snapshots, which it then scans for security risks.

For OCI accounts, the maximum snapshots scanned per agentless scanner is set to 16 snapshots.

By default, agentless scanning is configured to spin up a single agentless scanner within every region, meaning that at any given time, only a single agentless scanner is deployed in every region. The agentless scanner scans hosts snapshots iteratively within every region in batches of 26 snapshots at a time.

## Scaling and Parallel Scanning

To expedite the scanning process, you can enable auto scaling under the agentless configuration, this enables the scanning process to spin up to 50 agentless scanners in parallel to scan the snapshots within every region. If enabled, auto-scaling allows scanning of up to 50\*26=1300 hosts in parallel within every region.

You can also configure a limit other than 50 in the **Max number of scanners** configuration field.

<figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-217a90c5c870fd332a007c6b6fe379e62b719154%2Fagentless-scanning-max-number-of-scanners.png?alt=media" alt="agentless scanning max number of scanners"><figcaption></figcaption></figure>

If using a [hub account](/content-collections/runtime-security/agentless-scanning/agentless-scanning-modes.md#hub-account-mode), the same limit applies to the hub itself. Meaning, that a hub account with auto-scaling enabled, spins up to 50 agentless scanners within a region to scan all target accounts.

If the quota is exceeded within a region, for example, if an insufficient quota is set for either VM instances, IP addresses or other resources, the scan process fails for that region showing an appropriate quota error message for that specific region in the Compute Cloud Accounts page.

### Parallel Agentless Scanning

Agentless scanning takes place in parallel across 20 regions at a time that spans across all accounts. For example, 10 regions from account A, 5 regions from account B, and 5 regions from account C could be scanned in parallel.

## Cloud Service Provider Cost of Agentless Scanning

The main cost associated with agentless scanning is attributed to the running time of the scanners. By default, Prisma Cloud tries to create the scanner instance as a spot instance that is at a significantly discounted price compared to regular on-demand instances, and falls back to on-demand, only when spot instances are unavailable.

Other factors that determine the cost associated with agentless scanning is the snapshots and disks creation, and a minimal cost of egress networking from the scanners to the Prisma Cloud Compute backend. Agentless scanning does not incur cross-region networking costs because the scanners create the snapshots within the same region for both [scanning modes](/content-collections/runtime-security/agentless-scanning/agentless-scanning-modes.md).

If an instance type is not available the agentless scan process falls back to the next instance types as listed for each CSP. For example, an instance type might not be available in all regions.

### AWS

1. m5.2xlarge
2. m4.2xlarge
3. m3.2xlarge
4. t2.2xlarge

### Azure

* Standard\_DS4\_v2

### GCP

* e2-standard-8

### OCI

1. VM.Standard.E4.Flex
2. VM.Standard.E3.Flex
3. VM.Standard3.Flex

To get an estimate of the CSP costs associated with agentless scanning, reach out to your Prisma Cloud sales representative.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.prismacloud.io/content-collections/runtime-security/agentless-scanning.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
