For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-kubernetes.md).

This topic helps you install Prisma Cloud in your Kubernetes cluster quickly. There are many ways to install Prisma Cloud, but use this workflow to quickly deploy Defenders and verify how information is accessible from the Prisma Cloud Console. After completing this procedure, you can modify the installation to match your needs.

To install Prisma Cloud, you use the command-line utility called `twistcli`, which is bundled with the Prisma Cloud software. The process has the following steps to give you full control over the created objects.

1. The `twistcli` command-line utility generates YAML configuration files or Helm charts for the Prisma Cloud Console and Defender.

2. You create the required objects in your cluster with the `kubectl create` command.


To better understand clusters, read our [cluster context](https://docs.prismacloud.io/admin-guide/install/cluster-context) topic.

You can inspect, customize, and manage the YAML configuration files or Helm charts before deploying the Prisma Cloud Console and Defender. You can place the files or charts under source control to track changes, to integrate them with Continuous Integration and Continuous Development (CI/CD) pipelines, and to enable effective collaboration.

To ensure a single copy of the Prisma Cloud Console is always available, the Prisma Cloud Console is created as a Kubernetes `Deployment`. Kubernetes deployments are also known as Kubernetes services. To ensure that a Prisma Cloud Defender instance runs on each worker node of your cluster, each Prisma Cloud Defender is deployed as a Kubernetes `DaemonSet`.

When a node goes down, the orchestrator can reschedule the Prisma Cloud Console on a different healthy node. To improve the availability of the Prisma Cloud Console, you must ensure that the orchestrator can run the Prisma Cloud Console on any healthy node. The default configuration files or charts ensure this capability. These default configuration files or charts enable the following features to ensure availability.

- **Deploy a persistent volume (PV), to enable Prisma Cloud Console to save the state.** This configuration ensures that no matter where Prisma Cloud Console runs, it has access to the state of the deployment. For persistent volumes to work, every node in the cluster must have access to the shared storage. Setting up a [persistent volume](https://kubernetes.io/docs/concepts/storage/persistent-volumes/) can be easy or hard depending on the following factors.









  - What is your cloud provider?











    For example, Google Cloud Kubernetes Engine (GKE) offers persistent volumes out-of-the box with zero additional configuration required.

  - Is Kubernetes managed or unmanaged?











    If you deploy your clusters manually, you might need to configure a Network File System (NFS).


- **Expose the Prisma Cloud Console to the network through a load balancer.** A load balancer ensures that the Prisma Cloud Console is reachable regardless of where it runs in the cluster. The Prisma Cloud Console must be accessible in your deployment because it serves as a web interface and communicates policy to all the deployed Defenders.


## Requirements[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-kubernetes\#requirements)

To deploy your Defenders smoothly, you must meet the following requirements.

- You have a valid Prisma Cloud license key and access token.

- You provisioned a Kubernetes cluster that meets the minimum [system requirements](https://docs.prismacloud.io/admin-guide/install/system-requirements) and runs a [supported Kubernetes version](https://docs.prismacloud.io/admin-guide/install/system-requirements#orchestrators).

- You set up a Linux or macOS system to control your cluster, and you can access the cluster using the `kubectl` command-line utility.

- The nodes in your cluster can reach Prisma Cloud’s cloud registry at `registry-auth.twistlock.com`.

- Your cluster can create [PersistentVolumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/) and [LoadBalancers](https://kubernetes.io/docs/tasks/access-application-cluster/create-external-load-balancer/) from YAML configuration files or Helm charts.

- Your cluster uses any of the following runtimes. For more information about the runtimes that Prisma Cloud supports, see the [system requirements](https://docs.prismacloud.io/admin-guide/install/system-requirements#container-runtimes).









  - Docker Engine

  - CRI-O

  - CRI-containerd


### Required Permissions[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-kubernetes\#required-permissions)

- You can create and delete namespaces in your cluster.

- You can run the `kubectl create` command.


### Required Firewall and Port Configuration[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-kubernetes\#required-firewall-and-port-configuration)

Open the following ports in your firewall.

Ports for the **Prisma Cloud Console**:

- Incoming: 8083, 8084

- Outgoing: 443, 53


## Download the Prisma Cloud Console[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-kubernetes\#download-the-prisma-cloud-console)

Download the Prisma Cloud software to any system where you run `kubectl` to manage your cluster.

1. [Download](https://docs.prismacloud.io/admin-guide/welcome/releases#download) the current release.

2. Create the `prisma_cloud` folder and unpack the release tarball.

















AskCopy



```
$ mkdir prisma_cloud
$ tar xvzf prisma_cloud_compute_edition_<VERSION>.tar.gz -C prisma_cloud/
```


## Deploy the Prisma Cloud on Kubernetes[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-kubernetes\#deploy-the-prisma-cloud-on-kubernetes)

To use Prisma Cloud as part of your Kubernetes deployment, you need the `twistcli` command-line utility and the Prisma Cloud Defenders.

Use the [`twistcli`](https://docs.prismacloud.io/admin-guide/tools/twistcli) command-line utility to install the Prisma Cloud Console and deploy the Defenders. The `twistcli` utility is included with every release, or you can [download the utility separately](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-kubernetes#download-twistlock). After completing this procedure, the Prisma Cloud Console and Prisma Cloud Defenders run in your Kubernetes cluster.

When you install Prisma Cloud on [Amazon Elastic Kubernetes Service](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-eks) (EKS), [Azure Kubernetes Service](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-aks) (AKS), or [Alibaba Container Service](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-acs) with Kubernetes, additional configuration steps are required.

Install the Prisma Cloud Console and expose the service using a load balancer.

1. On your cluster controller, navigate to the directory where you downloaded and extracted the Prisma Cloud release tarball.

2. Generate a YAML configuration file for Console, where <PLATFORM> can be linux or osx.











The following command saves `twistlock_console.yaml` to the current working directory. If needed, you can edit the generated YAML file to modify the default settings.

















AskCopy



```
$ <PLATFORM>/twistcli console export kubernetes --service-type LoadBalancer
```









If you’re using Network File System version 4 (NFSv4) as the persistent storage in your cluster, use the `nolock`, `noatime` and `bg` mount options in your `PersistentVolume` custom resource definition (CRD). After generating the YAML file in the Prisma Cloud Console, add the mount options to your `PersistentVolume` CRD as follows.

















AskCopy



```
apiVersion: v1
kind: PersistentVolume
metadata:
name: twistlock-console
labels:
app-volume: twistlock-console
annotations:
volume.beta.kubernetes.io/mount-options: "nolock,noatime,bg"
```

3. Deploy the Prisma Cloud Console with the following command.

















AskCopy



```
$ kubectl create -f twistlock_console.yaml
```

4. Wait for the service to come up completely.

















AskCopy



```
$ kubectl get service -w -n twistlock
```


## Configure the Prisma Cloud Console[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-kubernetes\#configure-the-prisma-cloud-console)

Create your first administrator and enter your license key.

1. Get the public endpoint address for the Prisma Cloud Console.

















AskCopy



```
$ kubectl get service -o wide -n twistlock
```

2. Register a DNS entry for the external IP address of the Prisma Cloud Console. This procedure assumes the registered DNS name is `yourconsole.example.com`.

3. If you need to secure the Prisma Cloud Console communication with TLS, set up a [custom certificate](https://docs.prismacloud.io/admin-guide/configure/certificates). (Optional)

4. Open a browser window, and navigate to the Prisma Cloud Console. By default, the Prisma Cloud Console is served with the HTTPS protocol on port 8083. You can go to [https://yourconsole.example.com:8083](https://yourconsole.example.com:8083/) to access the Prisma Cloud Console.

5. Create your first administrator.

6. Enter your Prisma Cloud license key.

7. The Defender communicates with the Prisma Cloud Console using TLS. Update the [list of identifiers in the Prisma Cloud Console certificate](https://docs.prismacloud.io/admin-guide/configure/subject-alternative-names) that Defenders use to validate the identity of the Prisma Cloud Console.









1. Go to **Manage > Defenders > Names**.

2. In the **Subject Alternative Name** table, click **Add SAN**, then enter the Prisma Cloud Console IP address or domain name. Enter the `yourconsole.example.com` domain name. Any Defenders deployed outside the cluster can use this domain name to connect to the Prisma Cloud Console.

3. In the **Subject Alternative Name** table, click **Add SAN** again, then enter `twistlock-console`. Any Defenders deployed in the same cluster as the Prisma Cloud Console can use the `yourconsole.example.com` domain name to access the Prisma Cloud console.











      The service name of the Prisma Cloud Console is `twistlock-console`, but that name is not the same as the pod’s name, which is `twistlock-console-XXXX`.


## Install Prisma Cloud with Helm charts[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-kubernetes\#install-prisma-cloud-with-helm-charts)

You can use `twistcli` to create Helm charts for the Prisma Cloud Console and the Defenders. Helm is a package manager for Kubernetes, and a `chart` is a Helm package.

Apply the following changes.

- Pass the `--helm_ option to _twistcli` to generate a Helm chart. Don’t change the other options passed to `twistcli` since they configure the chart.

- Deploy your Defender with the `helm install` command instead of `kubectl create`.


The following procedure shows the modified commands.

1. [Download](https://docs.prismacloud.io/admin-guide/welcome/releases#download) the current recommended release.

2. Create a Console Helm chart.

















AskCopy



```
$ <PLATFORM>/twistcli console export kubernetes \
     --service-type LoadBalancer \
     --helm
```

3. Install the Console.

















AskCopy



```
$ helm install twistlock-console \
     --namespace twistlock \
     --create-namespace \
     ./twistlock-console-helm.tar.gz
```

4. [Configure Console](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-kubernetes#configure-console).

5. Create a Defender `DaemonSet` Helm chart.

















AskCopy



```
$ <PLATFORM>/twistcli defender export kubernetes \
     --address https://yourconsole.example.com:8083 \
     --helm \
     --user <ADMIN_USER> \
     --cluster-address twistlock-console
```

6. Install the Defender.

















AskCopy



```
$ helm install twistlock-defender-ds \
     --namespace twistlock \
     --create-namespace \
     ./twistlock-defender-helm.tar.gz
```


## Troubleshooting[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-kubernetes\#troubleshooting)

### Pod Security Policy[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-kubernetes\#pod-security-policy)

If Pod Security Policy is enabled in your cluster, you might get the following error when trying to create a Defender DaemonSet.

AskCopy

```
Error creating: pods "twistlock-defender-ds-" is forbidden: unable to validate against any pod security policy ..Privileged containers are not allowed
```

If you get this error, then you must create a PodSecurityPolicy for the Defender and the necessary ClusterRole and ClusterRoleBinding for the twistlock namespace. You can use the following Pod Security Policy, ClusterRole and ClusterRoleBinding:

PodSecurityPolicy

AskCopy

```
apiVersion: extensions/v1beta1
kind: PodSecurityPolicy
metadata:
 name: prismacloudcompute-service
spec:
 privileged: false
 seLinux:
  rule: RunAsAny
 allowedCapabilities:
  - AUDIT_CONTROL
  - NET_ADMIN
  - SYS_ADMIN
  - SYS_PTRACE
  - MKNOD
  - SETFCAP
 volumes:
  - "hostPath"
  - "secret"
 allowedHostPaths:
  - pathPrefix: "/etc"
  - pathPrefix: "/var"
  - pathPrefix: "/run"
  - pathPrefix: "/dev/log"
  - pathPrefix: "/"
 hostNetwork: true
 hostPID: true
 supplementalGroups:
  rule: RunAsAny
 runAsUser:
  rule: RunAsAny
 fsGroup:
  rule: RunAsAny
```

ClusterRole

AskCopy

```
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
 name: prismacloudcompute-defender-role
rules:
- apiGroups: ['policy']
  resources: ['podsecuritypolicies']
  verbs: ['use']
  resourceNames:
  - prismacloudcompute-service
```

ClusterRoleBinding

AskCopy

```
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
 name: prismacloudcompute-defender-rolebinding
roleRef:
 apiGroup: rbac.authorization.k8s.io
 kind: ClusterRole
 name: prismacloudcompute-defender-role
subjects:
- kind: ServiceAccount
  name: twistlock-service
  namespace: twistlock
```

[PreviousPrisma Cloud container images](https://docs.prismacloud.io/admin-guide/install/deploy-console/container-images) [NextDeploy the Prisma Cloud Console on Amazon ECS](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-amazon-ecs)

Last updated 3 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
