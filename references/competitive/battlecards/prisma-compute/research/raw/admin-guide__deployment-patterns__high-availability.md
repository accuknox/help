For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/deployment-patterns/high-availability.md).

The following article describes the key guidelines for keeping your Prisma Cloud Compute deployment highly available, and creating a disaster recovery process.

Prisma Cloud Compute deployment consists of two components - Console and Defenders.

- Console is the management interface. It lets you define policy and monitor your environment.

- Defenders are spread across your environment and protect its workloads according to the policies set in the Console.


When the Console fails or stops working, your environment still has active runtime protection done by the Defenders. Each Defender holds the updated policies, and keeps protecting your workloads according to them.

This article mainly focuses on Prisma Cloud Compute Edition deployment (self-hosted Console). When leveraging Prisma Cloud Enterprise Edition (SaaS Console), high availability for the console is automatically provided by Palo Alto Networks.

## Guidelines[Direct link to heading](https://docs.prismacloud.io/admin-guide/deployment-patterns/high-availability\#guidelines)

Use the guidelines in this section to create high availability and disaster recovery processes for your deployment.

The following flowchart depicts the guidelines:

![ha dr flow chart](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-84381c00d682422eaebb481af11743ff2b649ba7%252Fha_dr_flow_chart.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=e13347ac8dd05e8e225d08c9551215c7&sv=3)

### Inside each cluster[Direct link to heading](https://docs.prismacloud.io/admin-guide/deployment-patterns/high-availability\#inside-each-cluster)

Whether your deployment is in the cloud or on-premises, orchestrators, such as Kubernetes, OpenShift, and AWS ECS, automatically support HA of the cluster and the containers running on it.

- **Console** — Set your storage to be external to the Console container/node. In case the Console container/node fails, the orchestrator brings Console back up, where it connects to the external storage to get its latest state.

- **Defenders** — Defenders are deployed as a DaemonSet. In case of a node failure, the orchestrator automatically brings up another node and deploys a Defender container on it, as a part of the DaemonSet definition.


### Between clusters[Direct link to heading](https://docs.prismacloud.io/admin-guide/deployment-patterns/high-availability\#between-clusters)

While not explicitly tested or supported by Palo Alto Networks, in general, solutions that replicate storage between clusters to provide disaster recovery work transparently to Prisma Cloud Compute Edition. Note that ingress into the Console (DNS mapping and IP routing) may require additional steps during the activation of the secondary sites to ensure the Console is reachable over the network.

**Public cloud**

- **Inside each region** — CSPs provide high availability using availability zones inside each region. In case of an AZ failure, most cloud providers bring the cluster back up in another AZ.











Use cross availability zones storage solutions, so when the cluster is up in another AZ, it connects to the shared storage and keeps functioning as before. For example, in AWS, EFS can be used as a shared storage between availability zones.

- **Between regions** — CSPs provide solutions such as snapshots and backups that can be moved between regions, shared storage between regions, etc. You can also use [Compute’s backup and restore](https://docs.prismacloud.io/admin-guide/configure/disaster-recovery) capabilities for moving the data between regions.


**Private cloud (on-premises)**

- **Inside each site/data center** (between clusters on the same site)









  - Use shared storage between the clusters.

  - Create a disaster recovery process using [Compute’s backup and restore](https://docs.prismacloud.io/admin-guide/configure/disaster-recovery) capabilities:









    - Create a spare cluster (warm or cold) with a Prisma Cloud Compute (PCC) deployment.

    - Backup PCC’s data periodically to a location outside of the active cluster.

    - If the active cluster fails, bring the spare cluster up, and restore PCC’s data to it.


- **Between sites/data centers**









  - Create a disaster recovery process for cases where one site goes down, using [Compute’s backup and restore](https://docs.prismacloud.io/admin-guide/configure/disaster-recovery) capabilities:









    - Create a spare site (warm or cold) with a PCC deployment.

    - Backup PCC’s data periodically to a location outside of the active site.

    - If the entire active site fails, bring the spare site up, and restore PCC’s data from the external location to it.


## Projects[Direct link to heading](https://docs.prismacloud.io/admin-guide/deployment-patterns/high-availability\#projects)

[Projects](https://docs.prismacloud.io/admin-guide/deployment-patterns/projects) solve the problem of multi-tenancy. Each project consists of a Console and its Defenders. Each project is a separate, compartmentalized environment which operates independently with its own rules and configurations.

High availability and disaster recovery processes should be created for each tenant project, similar to the way you would handle a single Console deployment. If using Compute’s backup and restore capabilities, backups should be created and restored separately for each project.

[PreviousAutomated deployment](https://docs.prismacloud.io/admin-guide/deployment-patterns/automated-deployment) [NextAPI](https://docs.prismacloud.io/admin-guide/api/api)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
