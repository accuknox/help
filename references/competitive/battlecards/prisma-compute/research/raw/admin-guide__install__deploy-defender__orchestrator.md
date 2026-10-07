For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/install/deploy-defender/orchestrator.md).

This topic helps you install Prisma Cloud in your Kubernetes cluster quickly. There are many ways to install Prisma Cloud, but use this workflow to quickly deploy Defenders and verify how information is accessible from the Prisma Cloud Console. After completing this procedure, you can modify the installation to match your needs.

To better understand clusters, read our [cluster context](https://docs.prismacloud.io/admin-guide/install/cluster-context) topic.

To deploy Prisma Cloud Defenders, you use the [command-line utility called `twistcli`](https://docs.prismacloud.io/admin-guide/tools/twistcli), which is bundled with the Prisma Cloud software. The process has the following steps to give you full control over the created objects.

1. The `twistcli` utility generates YAML configuration files or Helm charts for the Defender.

2. You create the required objects in your cluster with the `kubectl create` command.


You can inspect, customize, and manage the YAML configuration files or Helm charts before deploying the Prisma Cloud Console and Defender. You can place the files or charts under source control to track changes, to integrate them with Continuos Integration and Continuos Development (CI/CD) pipelines, and to enable effective collaboration.

Each Prisma Cloud Defender is deployed as a `DaemonSet` to ensure that a Prisma Cloud Defender instance runs on each worker node of your cluster.

## Prerequisites[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/orchestrator\#prerequisites)

To deploy your Defenders smoothly, you must meet the following requirements.

- You have a valid Prisma Cloud license key and access token.

- You have a valid access key and secret key created for the admin user inside Prisma Cloud

- You provisioned a Kubernetes cluster that meets the minimum [system requirements](https://docs.prismacloud.io/admin-guide/install/system-requirements) and runs a [supported Kubernetes version](https://docs.prismacloud.io/admin-guide/install/system-requirements#orchestrators).

- You set up a Linux or macOS system to control your cluster, and you can access the cluster using the `kubectl` command-line utility.

- The nodes in your cluster can reach Prisma Cloud’s cloud registry at `registry-auth.twistlock.com`.

- Your cluster uses any of the following runtimes. For more information about the runtimes that Prisma Cloud supports, see the [system requirements](https://docs.prismacloud.io/admin-guide/install/system-requirements#container-runtimes).









  - Docker Engine

  - CRI-O

  - CRI-containerd


- Install the [Prisma Cloud command-line utility](https://docs.prismacloud.io/admin-guide/tools/twistcli) called `twistcli`, which is bundled with the Prisma Cloud software. You use `twistcli` to deploy the Defenders.


### Required Permissions[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/orchestrator\#required-permissions)

- You can create and delete namespaces in your cluster.

- You can run the `kubectl create` command.


### Required Firewall and Port Configuration[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/orchestrator\#required-firewall-and-port-configuration)

Open the following ports in your firewall.

Ports for the **Prisma Cloud Defenders**:

## Install the Prisma Cloud Defender[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/orchestrator\#install-the-prisma-cloud-defender)

To install the Prisma Cloud Defender, deploy the Defenders as `DaemonSet` custom resources. This approach ensures that a Defender instance runs on every node in the cluster. To deploy the Prisma Cloud Defender, use a macOS or Linux cluster controller with `kubectl` enabled and follow these steps:

1. Use the `twistcli` command-line utility to generate the `DaemonSet` YAML configuration file for the Defender.

2. Deploy the generated custom resource with `kubectl`.


This approach is called declarative object management. It allows you to work directly with the YAML configuration files. The benefit is that you get the full source code for the custom resources you create in your cluster, and you can use a version control tool to manage and track modifications. With YAML configuration files under version control, you can delete and reliably recreate `DaemonSets` in your environment.

If you don’t have `kubectl` access to your cluster, you can deploy Defender `DaemonSets` directly from the [Console UI](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/compute-edition/34/admin-guide/install/deploy-defender/container/container.md).

This procedure shows you how to deploy Defender `DaemonSets` using the `twistcli` command-line utility and declarative object management. You can also generate the installation commands using the Prisma Cloud Console UI under **Manage > Defenders > Deploy > Defenders**. Installation scripts are provided for Linux and MacOS workstations. Use the `twistcli` command-line utility to generate the Defender `DaemonSet` YAML configuration files from Windows workstations. Deploy the custom resources with `kubectl` following this procedure.

1. Generate the DaemonSet custom resource for the Defender.









1. Go to **Compute > Manage > Defenders > Defenders: Deployed > Manual deploy**.

2. Select **Orchestrator**.

3. Select **Kubernetes** from **Step 2: Choose the orchestrator type**.

4. Copy the hostname from **Step 3: The name that Defender will use to connect to this Console**.


2. Generate the `defender.yaml` file using the following `twistcli` command with the described parameters.

















AskCopy



```
$ <PLATFORM>./twistcli defender export kubernetes \
     --user <ADMIN_USER_ACCESS_KEY> \
     --address <PRISMA_CLOUD_COMPUTE_CONSOLE_URL> \
     --cluster-address <PRISMA_CLOUD_COMPUTE_HOSTNAME> \
     --container-runtime containerd
```







   - <PLATFORM> can be `linux`, `osx`, or `windows`.

   - <ADMIN\_USER\_ACCESS\_KEY> is the access key of the Prisma Cloud user with the System Admin role.

   - <PRISMA\_CLOUD\_COMPUTE\_CONSOLE\_URL> specifies the address of the Prisma Cloud Compute Console.

   - <PRISMA\_CLOUD\_COMPUTE\_HOSTNAME> specifies the address Defender uses to connect to Prisma Cloud Console. You can use the external IP address exposed by your load balancer or the DNS name that you manually set up.

   - Once you run the given command, after altering the fields for your environment, you will get a prompt requesting a password. The password is the secret key of the Prisma Cloud user with the System Admin role that you should have created as part of the prerequisite.


Note:

- For provider managed clusters, Prisma Cloud automatically gets the cluster name from your cloud provider.

- To override the cluster name used that your cloud provider has, use the `--cluster` option.

- For self-managed clusters, such as those built with kops, manually specify a cluster name with the `--cluster` option.

- When using the CRI-O or `containerd` runtimes, pass the `--container-runtime crio` or `--container-runtime containerd` flag to `twistcli` when you generate the YAML configuration file or the Helm chart.

- When using an AWS Bottlerocket-based EKS cluster, pass the `--container-runtime crio` flag when creating the `YAML` file.

- To use Defenders in **GKE on ARM**, you must [prepare your workloads](https://cloud.google.com/kubernetes-engine/docs/how-to/prepare-arm-workloads-for-deployment#node-affinity-multi-arch-arm).

- For Kubernetes defenders on RKE2, create the YAML file with the “SELinux Policy” option.









1. Deploy the Defender `DaemonSet` custom resource.

















     AskCopy



     ```
     $ kubectl create -f ./defender.yaml
     ```

2. In Prisma Cloud Compute, go to **Manage > Defenders > Defenders: Deployed > Manual deploy** to see a list of deployed Defenders.


## Install Prisma Cloud with Helm charts[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/orchestrator\#install-prisma-cloud-with-helm-charts)

## Install Prisma Cloud on a CRI (non-Docker) cluster[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/orchestrator\#install-prisma-cloud-on-a-cri-non-docker-cluster)

## Deploy Defenders as DaemonSets[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/orchestrator\#deploy-defenders-as-daemonsets)

Kubernetes lets you set up a cluster with the container runtime of your choice. Prisma Cloud supports Docker Engine, CRI-O, and cri-containerd.

When generating the YAML file or Helm chat to deploy the Defender DaemonSet, you can select the **Container Runtime type** on Prisma Cloud console from **Manage > Defenders > Defenders: Deployed > Manual deploy**.

Since Defenders need to have a view of other containers, this option is necessary to guide the communication.

If you use _containerd_ on GKE, and you install Defender without selecting the `CRI-O` **Container Runtime type**, everything will appear to work properly, but you’ll have no images or container scan reports in **Monitor > Vulnerability** and **Monitor > Compliance pages** and you’ll have no runtime models in **Monitor > Runtime**. This happens because the Google Container Optimized Operating system (GCOOS) nodes have Docker Engine installed, but Kubernetes doesn’t use it. Defender thinks everything is OK because all of the integrations succeed, but the underlying runtime is actually different.

![container runtime type ui](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-0cd393b9eb679ad1e547c83eb2af865d8b10f5fe%252Fcontainer-runtime-type-ui.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=713d761a5493e431df99a0a43b380c8a&sv=3)

If you’re deploying Defender DaemonSets with twistcli, use the following flag with one of the container runtime types:

- `--container-runtime docker`

- `--container-runtime crio`

- `--container-runtime containerd`


When generating YAML from Console or twistcli, there is a simple change to the _yaml_ file as seen below.

In this abbreviated version DEFENDER\_TYPE:daemonset will use the Docker interface.

To change the default containerd data directory from `/var/lib/containerd` to a custom directory (for example: `/var/lib/kubelet/containerd`), modify the `volumeMounts` and `volumes` sections. Here is an example:

To change the default containerd data directory from `/var/lib/containerd` to a custom directory (for example: `/var/lib/kubelet/containerd`), modify the `volumeMounts` and `volumes` sections. Here is an example:

In this abbreviated version DEFENDER\_TYPE:cri will use the CRI.

Similar to the Defenders, to customize the containerd data directory, modify the paths in the `volumeMounts` and `volumes` sections accordingly.

## Troubleshooting[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/orchestrator\#troubleshooting)

### 1\. Kubernetes CrashLoopBackOff Error[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/orchestrator\#id-1.-kubernetes-crashloopbackoff-error)

**Error**

AskCopy

```
Back-off restarting failed container
```

To get the error logs, run the command: `kubectl describe pod[name]`.

**Reason**

This is caused due to a temporary memory resource overload. When running WAAS Out-of-Band (OOB), the Defender automatically increases the `cgroup` memory limit to 4 GB (as OOB needs more memory). But since the Defenders' `cgroup` in K8s is hierarchically under the `cgroup` of the K8s pod with a limit of 512 MB, this results in an Out-Of-Memory error.

### 2\. Out-of-Memory (OOM) Error in Kubernetes Defender Nodes[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/orchestrator\#id-2.-out-of-memory-oom-error-in-kubernetes-defender-nodes)

**Issue**

Users encounter out-of-memory (OOM) issues when running an inline container firewall on Defender nodes operating within Kubernetes (k8s), particularly when there are more than 10 protected workloads on the same node.

**Reason**

The hierarchical nature of cgroups in Kubernetes means that the memory limit set for the pod takes precedence over the memory limit set specifically for the Defender cgroup. Consequently, this hierarchy can lead to OOM errors, especially when multiple protected workloads are present on the same node.

**Solution**

When deploying inline firewall instances on a Defender node with more than 10 protected workloads, increase the memory allocation for the Defender pod to 4GB.

### 3\. Increase the Defender Pod Limit[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/orchestrator\#id-3.-increase-the-defender-pod-limit)

Increase the Pod limit to 4 GB when activating WAAS OOB on K8s cluster.

1. **For running Defenders**









1. Run `kubectl edit ds twistlock-defender-ds -n twistlock` and change the value under **resources > limits > memory** to **4096Mi** in the Daemonset spec `*.yaml` file.

2. **Save** the file to restart the Defenders with the increased memory limit.


2. **When deploying Defenders**









1. **With YAML**:









      1. Change the value of **resources > limits > memory** to **4096Mi**.

      2. Deploy the `*.yaml` file.


2. **With HELM**:









      1. Change the value of **limit\_memory** to **4096Mi** in "values.yaml" file.


3. **With script**:









      1. Deploy the Defender using the install script.

      2. Run `kubectl edit ds twistlock-defender-ds -n twistlock` and change the value under **resources > limits > memory** to **4096Mi**.

      3. **Save** the file to restart the Defenders with the increased memory limit.


### 4\. Pod Security Policy[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/orchestrator\#id-4.-pod-security-policy)

If Pod Security Policy is enabled in your cluster, you might get the following error when trying to create a Defender DaemonSet.

AskCopy

```
Error creating: pods "twistlock-defender-ds-" is forbidden: unable to validate against any pod security policy ..Privileged containers are not allowed
```

Kubernetes has [deprecated Pod Security Policy](https://kubernetes.io/blog/2021/04/06/podsecuritypolicy-deprecation-past-present-and-future/). The following troubleshooting steps only apply to the deprecated `PodSecurityPolicy` custom resource.

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

### 5\. Warning while applying the defender YAML[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/orchestrator\#id-5.-warning-while-applying-the-defender-yaml)

When using newer Kubernetes versions (1.30 and above), you may see the following warning while applying the defender YAML:

AskCopy

```
Warning: spec.template.metadata.annotations[container.apparmor.security.beta.kubernetes.io/twistlock-defender]: deprecated since v1.30; use the "appArmorProfile" field instead
```

This warning doesn’t affect the defender deployment and the defender will be fully operational. The warning pertains to the deprecation of the `appArmorProfile` attribute used in the generated YAML configuration, which will be addressed in future releases.

If you wish to resolve this warning, open the YAML file, search for the securityContext section:

securitycontextbeforeappArmorProfile

AskCopy

```
securityContext:
  readOnlyRootFilesystem: true
  privileged: false
  capabilities:
    add:
    - NET_ADMIN  # Required for process monitoring
    - NET_RAW    # Required for iptables (CNNF, runtime DNS, WAAS). See: https://bugzilla.redhat.com/show_bug.cgi?id=1895032
    - SYS_ADMIN  # Required for filesystem monitoring
    - SYS_PTRACE # Required for local audit monitoring
    - SYS_CHROOT # Required for changing mount namespace using setns
    - MKNOD      # A capability to create special files using mknod(2), used by docker-less registry scanning
    - SETFCAP    # A capability to set file capabilities, used by docker-less registry scanning
    - IPC_LOCK   # Required for perf events monitoring, allowing to ignore memory lock limits
```

And add the new `appArmorProfile` field in order to get the following result:

securitycontextafterappArmorProfile

AskCopy

```
securityContext:
  readOnlyRootFilesystem: true
  privileged: false
  appArmorProfile:
    type: Unconfined
  capabilities:
    add:
    - NET_ADMIN  # Required for process monitoring
    - NET_RAW    # Required for iptables (CNNF, runtime DNS, WAAS). See: https://bugzilla.redhat.com/show_bug.cgi?id=1895032
    - SYS_ADMIN  # Required for filesystem monitoring
    - SYS_PTRACE # Required for local audit monitoring
    - SYS_CHROOT # Required for changing mount namespace using setns
    - MKNOD      # A capability to create special files using mknod(2), used by docker-less registry scanning
    - SETFCAP    # A capability to set file capabilities, used by docker-less registry scanning
    - IPC_LOCK   # Required for perf events monitoring, allowing to ignore memory lock limits
```

You can now apply the YAML without any warning message.

[PreviousWindows Defender](https://docs.prismacloud.io/admin-guide/install/deploy-defender/host/windows-host) [NextDeploy Defenders on Amazon ECS](https://docs.prismacloud.io/admin-guide/install/deploy-defender/orchestrator/install-amazon-ecs)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
