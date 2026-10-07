For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/install/deploy-defender/orchestrator/install-cluster-container-defender.md).

Container orchestrators provide native capabilities for deploying agents, such as Defender, to every node in the cluster. Prisma Cloud leverages these capabilities to install Defender.

The process for deploying Container Defender to a cluster can be found in the dedicated orchestrator-specific [install guides](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/compute-edition/34/admin-guide/install/install.md).

If you wish to automate the defenders deployment process to a cluster, or you don’t have kubectl access to your cluster (or oc access for OpenShift), you can deploy Defender DaemonSets directly from the Console UI.

This Defender install flow doesn’t let you manually configure a cluster name. Cluster names let you [segment your views](https://docs.prismacloud.io/admin-guide/technology-overviews/radar#cluster-pivot) of the environment. For most cases, this shouldn’t be a problem because if you’re deploying to a managed cluster, then Prisma Cloud retrieves the cluster name directly from the cloud provider. If you must manually specify a name, deploy your Defenders from **Manage > Defenders > Deploy > DaemonSet** or use twistcli.

If your clusters use **ARM architecture or multiple architectures** on Google Kubernetes Engine (GKE) you can’t use the following procedure to automatically deploy the defenders. Instead, use the [manual installation procedure for Kubernetes](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/compute-edition/34/admin-guide/install/deploy-defender/orchestrator/orchestrator.md#install-defender) and edit the `daemonset.yaml` configuration file to [prepare your workloads](https://cloud.google.com/kubernetes-engine/docs/how-to/prepare-arm-workloads-for-deployment#node-affinity-multi-arch-arm).

## Deploy Defender DaemonSet using kubeconfig[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/orchestrator/install-cluster-container-defender\#deploy-defender-daemonset-using-kubeconfig)

**Prerequisites:**

- You’ve created a [kubeconfig credential](https://docs.prismacloud.io/admin-guide/authentication/credentials-store/kubernetes-credentials) for your cluster so that Prisma Cloud can access it to deploy the Defender DaemonSet.


**Deployment process:**

1. Log into Prisma Cloud Console.

2. Go to **Manage > Defenders > Manage**.

3. Click **DaemonSets**.

4. For each cluster in the table, click **Actions > Deploy**.











The table shows a count of deployed Defenders and their version number.


## Deploy Defender DaemonSet for GKE[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/orchestrator/install-cluster-container-defender\#deploy-defender-daemonset-for-gke)

**Prerequisites:**

- You deployed a GKE cluster

- You created a corresponding Service Account key in JSON format. The Service Account should have the following permissions:









  - Editor

  - Compute Storage Admin

  - Kubernetes Engine Admin

  - Service Account Token Creator


- You created a xref:~/authentication/credentials-store/gcp-credentials.adoc.adoc\[GCP credential\] for your cluster so that Prisma Cloud can access it to deploy the Defender DaemonSet:









1. Log into Prisma Cloud Console.

2. Go to **Manage > Authentication > Credentials Store**

3. Click **Add credential** button

4. Select type **GCP** and credential level, then copy the content of the JSON Service Account key into the Service Account line (take it all including brackets).


To deploy the Defender DaemonSet, use the following procedure.

1. Log into Prisma Cloud Console.

2. Go to **Manage > Defenders > Manage > DaemonSets**.











When the page is loaded, multiple rows of K8S clusters visible with SA credentials are displayed.











For GCP organizations with hundreds of projects, using organization level credentials might affect the performance of the page and the time to load the clusters. Therefore, the best approach to reduce the time and to avoid potential timeouts, is to divide the projects within your organization into multiple GCP folders. Then, create a service account and credential for each one of them.

3. Verify that the status is **Success** and the Defender count is 0/0 for all relevant clusters.

4. For each cluster, click **Actions > Deploy**.

5. Refresh the view and verify that for each cluster the version is the correct, the status is **Success**, and the Defender count is equal to the number of cluster nodes.


[PreviousDeploy Defenders on Amazon ECS](https://docs.prismacloud.io/admin-guide/install/deploy-defender/orchestrator/install-amazon-ecs) [NextDeploy Prisma Cloud Defender from the GCP Marketplace](https://docs.prismacloud.io/admin-guide/install/deploy-defender/orchestrator/install-defender-gcp-marketplace)

Last updated 3 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
