For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/authentication/credentials-store/kubernetes-credentials.md).

Kubernetes stores cluster authentication information in a YAML file known as kubeconfig. The kubeconfig file grants access to clients, such as kubectl, to run commands against the cluster. By default, kubeconfig is stored in _$HOME/.kube/config_.

Prisma Cloud uses the kubeconfig credential to deploy and upgrade Defender DaemonSets directly from the [Console UI](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/compute-edition/34/admin-guide/install/deploy-defender/container/container.md). If you plan to manage DaemonSets from the command line with kubectl, you don’t need to create this type of credential.

The user or service account in your kubeconfig must have permissions to create and delete the following resources:

- ClusterRole

- ClusterRoleBinding

- DaemonSet

- Secret

- ServiceAccount


Prisma Cloud doesn’t currently support kubeconfig credentials for Google Kubernetes Engine (GKE) or AWS Elastic Kubernetes Service(EKS). The kubeconfig for these clusters require an external binary for authentication (specifically the Google Cloud SDK and aws-iam-authenticator, respectively), and Prisma Cloud Console doesn’t ship with these binaries.

1. Open Console, and go to **Manage > Authentication > Credentials Store**.

2. Click **Add credential**, and enter the following values:









1. In **Name**, enter a label to identify the credential.

2. In **Type** , select **Kubeconfig**.

3. In **Kubeconfig**, paste the contents of your _kubeconfig_ file.


[PreviousIBM Credentials](https://docs.prismacloud.io/admin-guide/authentication/credentials-store/ibm-credentials) [NextGitLab Credentials](https://docs.prismacloud.io/admin-guide/authentication/credentials-store/gitlab-credentials)

Last updated 3 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
