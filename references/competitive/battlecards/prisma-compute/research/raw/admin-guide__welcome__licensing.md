For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/welcome/licensing.md).

Licensing on Prisma Cloud uses a metering system based on credits. You must procure a license for each resource that Prisma Cloud protects and renew the license before the expiry term. Refer to [license types](https://docs.paloaltonetworks.com/prisma/prisma-cloud/prisma-cloud-admin/get-started-with-prisma-cloud/prisma-cloud-licenses).

This section is specifically for Prisma Cloud Compute capabilities that protects your hosts, containers, and serverless functions using a security agent called Defender, and using an agentless method. The number of credits you consume directly correlates with the type and mix of Defenders you deploy and the agentless security option. If you exceed the license count, Palo Alto Networks will notify you with a prominent banner that displays at the top of the Prisma Cloud web console. Exceeding the license count does not disable any security functions nor prevent the deployment of additional Defenders.

Prisma Cloud also offers twistcli, a command-line configuration tool for which there is no additional credit usage. The credit usage is for the resources that are being protected using an agent or an agentless method.

## Defender types[Direct link to heading](https://docs.prismacloud.io/admin-guide/welcome/licensing\#defender-types)

The type of Defender you deploy depends on the resource you’re securing.

- **Host Defender** — Secures legacy hosts (Linux or Windows) that don’t run containers.

- **Container Defender** — Secures hosts (Linux or Windows) that run containers. These types of hosts have a container runtime installed, such as Docker Engine or CRI-O. Container Defender protects both the underlying host and any containers it runs, and the license (7 credits) includes coverage for both. A container host consumes 7 credits whether it runs one container or a hundred containers.

- **Container Defender - App Embedded** — Secures containers which are run by a managed service, where the service provider maintains all infrastructure required to run the container, including the underlying host and container runtime. For this type of deployment, a Container App Embedded Defender is embedded into each container to be secured.

- **Serverless Defender** — Secures serverless functions. For this type of deployment, a Serverless Defender is embedded into each function to be secured.


[PreviousSecurity Assurance Policy on Prisma Cloud Compute Edition](https://docs.prismacloud.io/admin-guide/welcome/security-assurance-policy) [NextPrisma Cloud Enterprise Edition vs Compute Edition](https://docs.prismacloud.io/admin-guide/welcome/pcee-vs-pcce)

Last updated 3 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
