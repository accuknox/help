For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/install/deploy-defender.md).

To take advantage of the agent-based security features of Prisma Cloud, you must deploy the Defender agent.

You can deploy single Defenders for containers, hosts, and serverless functions or deploy Defenders on entire clusters using an orchestrator. There are several [Defender types](https://docs.prismacloud.io/admin-guide/install/deploy-defender/defender-types) based on the assets they protect and how you wish to deploy them.

## Defender capabilities[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender\#defender-capabilities)

The following table summarizes the key functional differences between Defender types.

Capabilities

Defender type

Container1

Host

Serverless

App-Embedded

**Deployment methods**

**Console UI**

Y

Y

Y

Y

**API**

Y

Y

Y

Y

**twistcli**

Y

Y

**Vulnerability management**

Y

Y

Y2

Y3

**Compliance**

Y

Y

Y2

Y4

**Runtime defense**

**Behavioral modeling**

Y

**Process**

Y

Y

Y

Y

**Networking**

Y

Y

Y

Y

**File system**

Y

Y

Y

Y

**Forensics**

Y

Y

Y

**Access control**

**Kubernetes auditing**

Y5

Y5

**Admission control**

Y

**Firewalls**

**WAAS**

Y

Y

Y

Y

**Radar (visualization)**

**Radar**

Y

Y

Y

1 Container Defender supports all Host Defender capabilities. You can deploy single container and host Defenders or deploy container and host Defenders using an [orchestrator](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/compute-edition/34/admin-guide/install/deploy-defender/orchestrator/orchestrator.md).

2 Normally Defender scans workloads for vulnerabilities and compliance issues. For serverless functions, Console does the scanning. In the Console, create a configuration that points to your repository of functions in your cloud provider.

3 Vulnerability management for deployed images only. Registry scanning by app-embedded Defenders is not supported.

4 Image compliance and custom compliance checks only. The trusted images feature isn’t supported.

5 Kubernetes auditing is done by the Console, and not by the Defenders. In the Console, enable Kubernetes auditing and create a configuration that points to your cluster.

## Connectivity Requirements[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender\#connectivity-requirements)

Defender must be able to communicate with Prisma Cloud over the network because it pulls policies down and sends data (alerts, events, etc) back to the Prisma Cloud console.

If you are using a certificate authority through a proxy, add the `--proxy-cacert` flag to the curl command [as described in the curl documentation](https://curl.se/docs/manpage.html#--proxy-cacert).

### URL Whitelisting[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender\#url-whitelisting)

When Defenders are behind a proxy or firewall, ensure the following URLs are whitelisted to allow proper communication:

- **Console URL**: Ensure Defenders can access the Prisma Cloud Console URL.

- **API Endpoint**: For SaaS consoles (not applicable to self-hosted versions), allow Defenders to connect to the API endpoint URL.











API endpoint URL format: `api.<region>.prismacloud.io`. Replace `<region>` with the Prisma Cloud instance location. For example, `sg` for Singapore or `us` for the United States.

- **WildFire Service**: If the WildFire service is enabled, allow Defenders to connect to \*.wildfire.paloaltonetworks.com or the relevant [regional WildFire URLs](https://docs.prismacloud.io/admin-guide/configure/wildfire).


[PreviousDeploy the Prisma Cloud Console on Openshift](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-openshift) [NextAvailable Defender Types](https://docs.prismacloud.io/admin-guide/install/deploy-defender/defender-types)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
