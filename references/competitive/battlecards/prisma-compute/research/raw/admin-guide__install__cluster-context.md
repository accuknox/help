For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/install/cluster-context.md).

Prisma Cloud can segment your environment by cluster. For example, you might have three clusters: test, staging, and production. The cluster pivot in Prisma Cloud lets you inspect resources and administer security policy on a per-cluster basis.

![radar clusters pivot](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-c1ee4c6317bbef850423b292e8a444a06cce4f41%252Fradar_clusters_pivot.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=d015bf3fa124801caab241b0433fe77f&sv=3)

## Cluster awareness across the product[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/cluster-context\#cluster-awareness-across-the-product)

Radar lets you explore your environment cluster-by-cluster. Various scan reports and audits include the relevant cluster name to provide environment context. You can also create stored filters (also known as [collections](https://docs.prismacloud.io/admin-guide/configure/collections)) based on cluster names. Finally, you can scope policy by cluster. Vulnerability and compliance rules for container images and hosts, runtime rules for container images, and trusted images rules can all be scoped by cluster name.

## Generating cluster names in Prisma Cloud[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/cluster-context\#generating-cluster-names-in-prisma-cloud)

When two or more clusters share the same name, Prisma Cloud treats them as a single cluster. This can cause vulnerability information to be inaccurately reported for each cluster. The resulting data inconsistency might also lead to clean clusters being misrepresented as vulnerable ones.

To avoid cluster name conflicts when deploying a Defender DaemonSet, Prisma Cloud provides a **Cluster name resolving method** option that enables greater flexibility and accuracy in generating cluster names within Prisma Cloud.

**Cluster name resolving method** is added to the **Manage > Defenders > “Manual Deploy” > Orchestrator > “Orchestrator type = Kubernetes" > Advanced Settings** page.

**Cluster name resolving method** has the following options:

- **Default**: This option allows Prisma Cloud to automatically generate the name based on available information from the kubeconfig file (specifically from the server field), resource group information, and cloud provider metadata endpoints.

- **Manual**: This option allows for manually specifying a cluster name. This is particularly useful for self-managed clusters, such as those built with kops, or for Bottlerocket clusters which do not provide a cluster name by default. When you select this option, the **Specify a cluster name** box appears, allowing you to enter the desired name.

- **API Server**: This option enables Prisma Cloud to use the API server address from the kubeconfig file to generate a unique cluster name.


### Important Considerations[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/cluster-context\#important-considerations)

- **Google Cloud Platform (GCP) clusters**: For Google Cloud Platform, clusters with the same name in different projects are treated as a single cluster. Consider manually specifying different names for each cluster using **Cluster name resolving method**.

- **Manual naming limitations**: Manually specifying names isn’t supported in **Manage > Defenders > Defenders:Auto-Defend > DaemonSets**. For this deployment flow, cluster names are automatically retrieved from the cloud provider or the kubeconfig file.


### Changing cluster names for an existing deployment[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/cluster-context\#changing-cluster-names-for-an-existing-deployment)

To change the cluster name determined by Prisma Cloud Compute or the manually set name, you must redeploy the Defender DaemonSet and specify the new name. Historical records for audits and incidents will retain the original cluster name. The new cluster name will only apply to future reporting. Collections created with the old cluster name need to be manually updated with the new name.

[PreviousSystem requirements](https://docs.prismacloud.io/admin-guide/install/system-requirements) [NextDeploy the Prisma Cloud Console On-Prem](https://docs.prismacloud.io/admin-guide/install/deploy-console)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
