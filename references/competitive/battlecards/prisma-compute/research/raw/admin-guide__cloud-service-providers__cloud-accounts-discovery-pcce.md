For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/cloud-service-providers/cloud-accounts-discovery-pcce.md).

It’s difficult to ensure that all your apps running on all the different types of cloud services are being properly secured. If you’re using multiple cloud platforms, you might have many separate accounts per platform. You could easily have hundreds of combinations of providers, accounts, and regions where cloud native services are being deployed.

Cloud discovery helps you find all cloud-native services being used on AWS, Azure, and Google Cloud, across all regions, and across all accounts. It enables you to continuously monitor these accounts, detect when new services are added, and report on the services that are unprotected, so that you can mitigate your exposure to rogue deployments, abandoned environments, and sprawl.

Cloud discovery offers coverage for the following services.

**Registries:**

- AWS

- Azure

- Google Artifact Registry

- Google Container Registry1,2


**Serverless functions:**

- AWS

- Azure

- Google Cloud


3 **Managed platforms:**

- AWS ECS

- AWS EKS

- Azure Kubernetes Service (AKS)

- Azure Container Instances (ACI)

- Google Kubernetes Engine (GKE)


**Virtual machines:**

- AWS EC2 instances

- Azure VMs3

- Google Cloud Platform (GCP) Compute Engine VM instances3


1Although Artifact Registry supports a number of content types (for example, Java, Node.js, and Python language packs), Prisma Cloud only supports discovering and scanning Docker images.

2Prisma Cloud doesn’t support scanning Helm charts saved as OCI images and stored in Artifact Registry. The OCI image that represents a Helm chart has a single layer that contains the Helm package. It is only a way to store a Helm chart, but it has no meaning in terms of a container. Prisma Cloud has no way to run the image to scan it. Note that Helm charts stored as OCI images will be shown in the list of resources discovered in the registry because we can’t indicate their type until we actually pull and scan them.

3Auto-defend is currently not yet available for these services. Auto-defend utilizes rule-based policies to automatically deploy Prisma Cloud to protect resources in your environment.

## Troubleshooting[Direct link to heading](https://docs.prismacloud.io/admin-guide/cloud-service-providers/cloud-accounts-discovery-pcce\#troubleshooting)

Ensure you have the right [permissions](https://docs.prismacloud.io/admin-guide/configure/permissions) for the account before you start with cloud discovery.

### Empty results from Cloud Discovery[Direct link to heading](https://docs.prismacloud.io/admin-guide/cloud-service-providers/cloud-accounts-discovery-pcce\#empty-results-from-cloud-discovery)

Cloud discovery results are visible per account. If you have multiple credentials associated with the same account, the results are only displayed for one credential to avoid duplication. The other credentials for the same account will show empty results. To view comprehensive results for all credentials, navigate to Cloud Radar **Radars > Cloud**.

[PreviousCloud Service Providers](https://docs.prismacloud.io/admin-guide/cloud-service-providers/cloud-service-providers) [NextConfigure Cloud Discovery](https://docs.prismacloud.io/admin-guide/cloud-service-providers/configure-cloud-discovery)

Last updated 3 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
