

??? "**AccuKnox KubeArmor**"

    ## **Introducing the D2iQ Kubernetes Platform (DKP)**

    As the leading independent Kubernetes Management Platform in production, the D2iQ Kubernetes Platform (DKP) provides a holistic approach and a complete set of enterprise-grade technologies, services, training, and support to build and run applications in production at scale. Built around the open-source Cluster API, the new version of DKP becomes the single, centralized point of control for an organization’s application infrastructure, empowering organizations to more easily deploy, manage, and scale Kubernetes workloads in Day 2 production environments

    ![](images/d2iq/d2iq-intro.png)

    ## **Deploying D2iQ Kubernetes Platform on AWS Cloud**

    ### **Pre-requisites**

    1. Latest DKP Binary
    2. DKP Enterprise License key
    3. Hands-on experience with AWS services like CloudFormation, EC2, IAM, etc.
    4. Follow the <a href="https://docs.d2iq.com/dkp/2.7/day-0-basic-installs-by-infrastructure" target="_blank">official documentation for DKP deployment</a>

    Once, DKP deployment is done, Activate the enterprise license from the UI

    ## **DKP Application catalog**

    Catalog applications are any third-party or open-source applications that appear in the Catalog. These applications are deployed to be used for customer workloads.

    D2iQ provides <a hred="https://docs.d2iq.com/dkp/2.7/workspace-dkp-applications" target="_blank">DKP Catalog Applications</a> for use in your environment.

    ![](images/d2iq/dkp-cat.png)

    We will be adding KubeArmor to the DKP application catalog.

    ## **Introducing KubeArmor** - An Open-Source policy enforcement engine

    KubeArmor is a cloud-native runtime security enforcement system that restricts the behavior (such as process execution, file access, and networking operations) of pods, containers, and nodes (VMs) at the system level.

    KubeArmor leverages Linux security modules (LSMs) such as AppArmor, SELinux, or BPF-LSM to enforce the user-specified policies. KubeArmor generates rich alerts/telemetry events with container/pod/namespace identities by leveraging eBPF.

    [KubeArmor Github](https://github.com/kubearmor/KubeArmor)

    ![](images/d2iq/ka-arch.png)

    ### **Steps to add KubeArmor to DKP Catalog**

    1. Create a <a href="https://docs.d2iq.com/dkp/2.7/create-a-git-repository" target="_blank">git-repository</a>
    2. Set the Git Repository <a href="https://docs.d2iq.com/dkp/2.7/git-repository-structure" target="_blank">Directory Structure</a>

    Use the following basic directory structure for your git repository:

    ```sh
    ├── helm-repositories
    │   ├── <helm repository 1>
    │   │   ├── kustomization.yaml
    │   │   └── <helm repository name>.yaml
    │   └── <helm repository 2>
    │       ├── kustomization.yaml
    │       └── <helm repository name>.yaml
    └── services
        ├── <app name>
        │   ├── <app version1> # semantic version of the app helm chart. e.g., 1.2.3
        │   │   ├── defaults
        │   │   │   ├── cm.yaml
        │   │   │   └── kustomization.yaml
        │   │   ├── <app name>.yaml
        │   │   └── kustomization.yaml
        │   ├── <app version2> # another semantic version of the app helm chart. e.g., 2.3.4
        │   │   ├── defaults
        │   │   │   ├── cm.yaml
        │   │   │   └── kustomization.yaml
        │   │   ├── <app name>.yaml
        │   │   └── kustomization.yaml
        │   └── metadata.yaml
        └── <another app name>
        ...
    ```

    Refer to the KubeArmor Git repository for the DKP Catalog <a href="https://github.com/th3-v3ng34nc3/kubearmor/" target="_blank">**Link**</a>

    **Note**: Please remember to fill out the <a href="https://docs.d2iq.com/dkp/2.7/workspace-application-metadata" target="_blank">metadata.yaml</a> with the application details that will be visible on the UI.

    ### **Enable KubeArmor from the Workspace Catalog**

    #### **Prerequisites**

    - Determine the name of the workspace where you wish to perform the deployments. You can use the ```dkp get workspaces``` command to see the list of workspace names and their corresponding namespaces.

    - Set the ```WORKSPACE_NAMESPACE``` environment variable to the name of the workspace’s namespace where the cluster is attached:

    ```sh
    export WORKSPACE_NAMESPACE=<workspace_namespace>
    ```

    #### **Steps to enable**

    **Step 1**: Get the list of available applications to enable using the following command:

    ```sh
    kubectl get apps -n kommander
    ```

    Sample:
    ```sh
    kubectl get apps -n kommander --kubeconfig cluster.conf
    NAME                  APP ID          APP VERSION   AGE
    elasticsearch-2.0.0   elasticsearch   2.0.0         3d22h
    gitlab-5.7.0          gitlab          5.7.0         3d22h
    keycloak-15.1.0       keycloak        15.1.0        3d22h
    kubearmor-1.3.2       kubearmor       1.3.2         3d22h
    linkerd-2.13.4        linkerd         2.13.4        3d22h
    linkerd-2.13.5        linkerd         2.13.5        3d22h
    weave-gitops-0.11.0   weave-gitops    0.11.0        3d22h
    weave-gitops-0.12.0   weave-gitops    0.12.0        3d22h
    weave-gitops-0.18.0   weave-gitops    0.18.0        3d22h
    weave-gitops-0.32.0   weave-gitops    0.32.0        3d22h
    ```

    **Step 2**: Deploy KubeArmor from the list with an ```AppDeployment``` resource.

    **Step 3**: Within the ```AppDeployment```, define the ```appRef``` to specify which ```App``` will be enabled:

    ```sh
    cat <<EOF | kubectl apply -f -
    apiVersion: apps.kommander.d2iq.io/v1alpha3
    kind: AppDeployment
    metadata:
    name: my-custom-app
    namespace: ${WORKSPACE_NAMESPACE}    //kommander
    spec:
    appRef:
        name: kubearmor-1.3.2
        kind: App
    EOF
    ```

    ### **Verify Applications**

    After completing the previous steps, your applications are enabled. Connect to the attached cluster and check the ```HelmReleases``` to verify the deployments:

    ```sh
    kubectl get helmreleases -n kommander
    ```

    **Output**:

    ```sh
    kubectl get helmreleases -n kommander --kubeconfig cluster.conf
    NAME                            AGE     READY   STATUS
    ai-navigator-cluster-info-api   8d      True    Release reconciliation succeeded
    centralized-grafana             8d      True    Release reconciliation succeeded
    centralized-kubecost            8d      True    Release reconciliation succeeded
    cluster-observer-2360587938     8d      True    Release reconciliation succeeded
    dex                             8d      True    Release reconciliation succeeded
    dex-k8s-authenticator           8d      True    Release reconciliation succeeded
    dkp-insights-management         8d      True    Release reconciliation succeeded
    gatekeeper                      8d      True    Release reconciliation succeeded
    gatekeeper-proxy-mutations      8d      True    Release reconciliation succeeded
    gitea                           8d      True    Release reconciliation succeeded
    grafana-logging                 8d      True    Release reconciliation succeeded
    grafana-loki                    8d      True    Release reconciliation succeeded
    karma                           8d      True    Release reconciliation succeeded
    karma-traefik                   8d      True    Release reconciliation succeeded
    karma-traefik-certs             8d      True    Release reconciliation succeeded
    kommander                       8d      True    Release reconciliation succeeded
    kommander-appmanagement         8d      True    Release reconciliation succeeded
    kommander-operator              8d      True    Release reconciliation succeeded
    kommander-ui                    8d      True    Release reconciliation succeeded
    kube-oidc-proxy                 8d      True    Release reconciliation succeeded
    kube-prometheus-stack           8d      True    Release reconciliation succeeded
    kubearmor-operator              3d23h   True    Release reconciliation succeeded
    kubecost                        8d      True    Release reconciliation succeeded
    kubecost-thanos-traefik         8d      True    Release reconciliation succeeded
    kubecost-traefik-certs          8d      True    Release reconciliation succeeded
    kubefed                         8d      True    Release reconciliation succeeded
    kubernetes-dashboard            8d      True    Release reconciliation succeeded
    kubetunnel                      8d      True    Release reconciliation succeeded
    logging-operator                8d      True    Release reconciliation succeeded
    logging-operator-logging        8d      True    Release reconciliation succeeded
    object-bucket-claims            8d      True    Release reconciliation succeeded
    prometheus-adapter              8d      True    Release reconciliation succeeded
    prometheus-thanos-traefik       8d      True    Release reconciliation succeeded
    prometheus-traefik-certs        8d      True    Release reconciliation succeeded
    reloader                        8d      True    Release reconciliation succeeded
    rook-ceph                       8d      True    Release reconciliation succeeded
    rook-ceph-cluster               8d      True    Release reconciliation succeeded
    thanos                          8d      True    Release reconciliation succeeded
    traefik                         8d      True    Release reconciliation succeeded
    traefik-forward-auth-mgmt       8d      True    Release reconciliation succeeded
    velero                          8d      True    Release reconciliation succeeded
    ```

    #### **Verify from the UI**

    ![](images/d2iq/dkp-apps.png)

    ![](images/d2iq/dkp-custom-app.png)

    Check the status of Kubearmor pods using

    ```sh
    kubectl get po -A -n kommander
    ```

    Sample:
    ```sh
    kubectl get po -A -n kommander --kubeconfig cluster.conf
    ```

    ![](images/d2iq/cli-pods.png)

    All the pods are running now we can enforce KubeArmor to a sample application

    ## **Applying KubeArmor Policy**

    **Step 1**: User needs to access the Cluster to apply the following KubeArmor policy.

    ```sh
    apiVersion: security.kubearmor.com/v1
    kind: KubeArmorPolicy
    metadata:
    name: harden-mysql-pkg-mngr-exec
    namespace: wordpress-mysql
    spec:
    action: Block
    message: Alert! Execution of package management process inside container is denied
    process:
        matchPaths:
        - path: /usr/bin/apt
        - path: /usr/bin/apt-get
        - path: /bin/apt-get
        - path: /sbin/apk
        - path: /bin/apt
        - path: /usr/bin/dpkg
        - path: /bin/dpkg
        - path: /usr/bin/gdebi
        - path: /bin/gdebi
        - path: /usr/bin/make
        - path: /bin/make
        - path: /usr/bin/yum
        - path: /bin/yum
        - path: /usr/bin/rpm
        - path: /bin/rpm
        - path: /usr/bin/dnf
        - path: /bin/dnf
        - path: /usr/bin/pacman
        - path: /usr/sbin/pacman
        - path: /bin/pacman
        - path: /sbin/pacman
        - path: /usr/bin/makepkg
        - path: /usr/sbin/makepkg
        - path: /bin/makepkg
        - path: /sbin/makepkg
        - path: /usr/bin/yaourt
        - path: /usr/sbin/yaourt
        - path: /bin/yaourt
        - path: /sbin/yaourt
        - path: /usr/bin/zypper
        - path: /bin/zypper
    selector:
        matchLabels:
        app: mysql
    severity: 5
    tags:
    - NIST
    - NIST_800-53_CM-7(4)
    - SI-4
    - process
    - NIST_800-53_SI-4
    ```

    Save the policy as a  “**.yaml**” file.

    **Step 2**: Apply the policy from the cluster:

    ```sh
    kubectl apply -f mysql.yaml -n wordpress-mysql --kubeconfig cluster.conf
    kubearmorpolicy.security.kubearmor.com/harden-mysql-pkg-mngr-exec created
    ```

    **Step 3**: Violating the Policy

    To violate the Above policy users need to exec into the MySQL pod under the WordPress-MySQL namespace

    ```sh
    kubectl exec -it mysql-74775b4bf4-mfdcr -n wordpress-mysql --kubeconfig cluster.conf -- bash
    ```
    Try to make use of the package manager
    ```sh
    root@mysql-74775b4bf4-mfdcr:/# apt-get update
    bash: /usr/bin/apt-get: Permission denied
    root@mysql-74775b4bf4-mfdcr:/# apt upgrade
    bash: /usr/bin/apt: Permission denied
    ```

    **Step 4**: Policy logs

    To see the Policy Logs the users must navigate to the Cluster CLI and execute the following command to watch the logs. Violate the policy after executing from MySQL pod

    ```sh
    karmor logs
    ```

    Sample Output:

    ```sh
    karmor logs --kubeconfig cluster.conf
    local port to be used for port forwarding kubearmor-relay-599df6f667-pzjqk: 32890
    Created a gRPC client (localhost:32890)
    Checked the liveness of the gRPC server
    Started to watch alerts
    == Alert / 2024-04-01 11:12:56.921907 ==
    ClusterName: default
    HostName: ip-10-0-122-67
    NamespaceName: wordpress-mysql
    PodName: mysql-74775b4bf4-mfdcr
    Labels: app=mysql
    ContainerName: mysql
    ContainerID: befbef6b9371eac5d3966f40f87593829e6f1a820f2454bbd13e656f0b5bbdab
    ContainerImage: docker.io/library/mysql:5.6@sha256:20575ecebe6216036d25dab5903808211f1e9ba63dc7825ac20cb975e34cfcae
    Type: MatchedPolicy
    PolicyName: harden-mysql-pkg-mngr-exec
    Severity: 5
    Message: Alert! Execution of package management process inside container is denied
    Source: /bin/bash
    Resource: /usr/bin/apt-get update
    Operation: Process
    Action: Block
    Data: syscall=SYS_EXECVE
    Enforcer: AppArmor
    Result: Permission denied
    ATags: [NIST NIST_800-53_CM-7(4) SI-4 process NIST_800-53_SI-4]
    Cwd: /
    HostPID: 770816
    HostPPID: 270053
    Owner: map[Name:mysql Namespace:wordpress-mysql Ref:Deployment]
    PID: 196
    PPID: 188
    ParentProcessName: /bin/bash
    ProcessName: /usr/bin/apt-get
    TTY: pts0
    Tags: NIST,NIST_800-53_CM-7(4),SI-4,process,NIST_800-53_SI-4
    UID: 0
    ```

    ## **Testing the Integration on User attached EKS cluster**

    This procedure requires the following items and configurations:

    - A fully configured and running Amazon <a href="https://aws.amazon.com/eks/" target="_blank"a>EKS cluster</a> with administrative privileges.

    - The current version of DKP Enterprise is <a href="https://docs.d2iq.com/dkp/2.7/kommander-installations-by-environment" target="_blank">installed</a> on your cluster.

    - Ensure you have installed kubectl in your Management cluster.

    - Follow the <a href="https://docs.d2iq.com/dkp/2.7/eks-attach-a-cluster" target="_blank">official guide</a> to attach a EKS cluster.

    ### **Installing KubeArmor**

    Follow the same steps that we followed while deploying KubeArmor in the management cluster

    1. Create Git repository
    2. Deploy KubeArmor from the apps list with an ```AppDeployment``` resource.
    3. Verify the deployment from the UI

    ![](images/d2iq/ka-in-ui.png)

    KubeArmor is enabled under Default Workspace in the attached EKS cluster and all the pods are running

    ![](images/d2iq/pods-run.png)

    ### **Applying KubeArmor Policy**

    **Step 1**: The user needs to go to the cluster to apply the following KubeArmor Policy

    ```sh
    apiVersion: security.kubearmor.com/v1
    kind: KubeArmorPolicy
    metadata:
    name: harden-mysql-pkg-mngr-exec
    namespace: wordpress-mysql
    spec:
    action: Block
    message: Alert! Execution of package management process inside container is denied
    process:
        matchPaths:
        - path: /usr/bin/apt
        - path: /usr/bin/apt-get
        - path: /bin/apt-get
        - path: /sbin/apk
        - path: /bin/apt
        - path: /usr/bin/dpkg
        - path: /bin/dpkg
    selector:
        matchLabels:
        app: mysql
    severity: 5
    tags:
    - NIST
    - NIST_800-53_CM-7(4)
    - SI-4
    - process
    - NIST_800-53_SI-4
    ```
    Save the policy as a  “**.yaml**” file.

    **Step 2**: Apply the policy from the cluster:

    ```sh
    kubectl apply -f mysql.yaml --kubeconfig dkp-eks-kubeconfig.conf
    kubearmorpolicy.security.kubearmor.com/harden-mysql-pkg-mngr-exec created
    ```

    **Step 3**: Violating the Policy

    To violate the Above policy users need to exec into the MySQL pod under the WordPress-MySQL namespace

    ```sh
    kubectl exec -it mysql-768cb6b7bd-txbvh -n wordpress-mysql --kubeconfig dkp-eks-kubeconfig.conf -- bash
    ```
    Try to execute the blocked binary
    ```sh
    root@mysql-768cb6b7bd-txbvh:/# apt-get
    bash: /usr/bin/apt-get: Permission denied
    ```

    **Step 4**: Policy logs

    To see the Policy Logs the users must navigate to the Cluster CLI and give the following command and then violate the policy from MySQL pod

    ```sh
    karmor logs --kubeconfig dkp-eks-kubeconfig.conf
    ```

    Sample Output:

    ```sh
    karmor logs --kubeconfig dkp-eks-kubeconfig.conf
    local port to be used for port forwarding kubearmor-relay-6b59fbf77f-f8g2m: 32859
    Created a gRPC client (localhost:32859)
    Checked the liveness of the gRPC server
    Started to watch alerts
    == Alert / 2024-04-05 17:11:16.812423 ==
    ClusterName: default
    HostName: ip-10-0-120-36.ec2.internal
    NamespaceName: wordpress-mysql
    PodName: mysql-768cb6b7bd-txbvh
    Labels: app=mysql
    ContainerName: mysql
    ContainerID: 42b044cdd51b2e01f106a14fc6e06cf2d5d786fe1b24e3212e2425821f50111f
    ContainerImage: docker.io/library/mysql:5.6@sha256:20575ecebe6216036d25dab5903808211f1e9ba63dc7825ac20cb975e34cfcae
    Type: MatchedPolicy
    PolicyName: harden-mysql-pkg-mngr-exec
    Severity: 5
    Message: Alert! Execution of package management process inside container is denied
    Source: /bin/bash
    Resource: /usr/bin/apt-get
    Operation: Process
    Action: Block
    Data: lsm=SECURITY_BPRM_CHECK
    Enforcer: BPFLSM
    Result: Permission denied
    ATags: [NIST NIST_800-53_CM-7(4) SI-4 process NIST_800-53_SI-4]
    Cwd: /
    HostPID: 21015
    HostPPID: 20531
    Owner: map[Name:mysql Namespace:wordpress-mysql Ref:Deployment]
    PID: 167
    PPID: 160
    ParentProcessName: /bin/bash
    ProcessName: /usr/bin/apt-get
    Tags: NIST,NIST_800-53_CM-7(4),SI-4,process,NIST_800-53_SI-4
    UID: 0
    ```

    **Note**: Once the KubeArmor is added to the DKP default application catalog a user can directly enable it from the UI

??? "**AccuKnox Enterprise**"

    AccuKnox runtime security for Kubernetes aids in discovering the application behavior of your workload and offers the capability to enforce security policies. AccuKnox automatically detects and suggests Behavioral Policies based on application observability, such as file system access for processes and processes that are accessing the network.

    AccuKnox leverages KubeArmor to implement runtime security policies, utilizing eBPF and LSMs (SELinux, BPF LSM, AppArmor). LSMs serve as a checkpoint based on the applied policies, scrutinizing all events and system calls against these policies before they interact with kernel objects. KubeArmor ensures that any event not compliant with the policies is prevented from executing in the userspace, thus maintaining a secure environment for your applications to operate.

    AccuKnox offers the subsequent enterprise functionalities to enhance runtime security:

    - Auto-Discovered Behavioural Policies
    - Recommendation of Hardening Policies based on compliance framework - MITRE, NIST, PCI-DSS, CIS
    - Inventory View of Application
    - Network Graph View of the Application
    - Network micro-segmentation in the application
    - Hardening of the Secrets Managers like Hashicorp Vault, CyberArk Conjur
    - GitOps-based Version Control for Policy Lifecycle Management
    - Rollback of recently changed Policy governing App Behavior
    - On-the-fly detection of change in App Behavior through Policies
    - Multi-tenant, Multi-Cluster, RBAC for user management
    - Comprehensive Dashboard across workloads running in Managed/Unmanaged Cluster, Containerized environment, VM or Baremetal
    - Integration with Registries for Container Image Vuln Scan
    - Telemetry aggregation (Process executed, File accessed, Network connections made) and Alerts events (Audit, Block)
    - Integration to SIEM for security events and Notification tool

    The utilization of the following AccuKnox agents assists in delivering the enterprise features:

    **Agents operator**: It will detect the environment of the k8s that is installed and based on that, it will pull all the AccuKnox Agents for Installation.

    **Discovery Engine**: AccuKnox Discovery Engine leverages the pod visibility provided by KubeArmor to automatically generate System and Network Policies.

    **Feeder Service**: The feeder service sends information from the Client Cluster to the AccuKnox SaaS Control Plane. Feeder Service is an agent that runs on every node, collects telemetry/alert events from source systems and messages, and emits them to the Messaging Cluster for Storage and Analysis.

    **Policy Enforcement Agent**: AccuKnox’s Policy Enforcement Agent enforces the policies by leveraging KubeArmor. The policy not only keeps track of the policies but is capable of doing tasks such as applying policies, denying policies, updating policies, and deleting the policies.

    **Shared Informer Agent**: Shared Informer Agent watches all the changes occurring in Kubernetes entities such as Pods, Nodes, Namespaces, Endpoints, and Services.

    ## **Before you Begin**

    This procedure requires the following items and configurations:

    - A fully configured and running Amazon EKS cluster with administrative privileges.

    - The current version of DKP Enterprise is <a href="https://docs.d2iq.com/dkp/2.7/kommander-installations-by-environment" target="_blank">installed</a> on your cluster.

    - Ensure you have installed ```kubectl``` in your Management cluster.

    In this case, we will be using D2iQ managed cluster created from the D2iQ console, You can use user attached cluster as well

    ![](images/d2iq/d2iq-con.png)

    ## **Steps to onboard cluster**

    **Step 1**: When the cluster is provisioned successfully > click on **Actions** from the upper right corner download the KubeConfig and export it to kubeconfig environment variable

    ![](images/d2iq/d2iq-actions.png)

    ```sh
    export KUBECONFIG=dkp-aditya-kubeconfig.yaml
    ```

    **Step 2**: From the application catalog enable **KubeArmor**

    ![](images/d2iq/enable-ka.png)

    **Step 3**: Login to AccuKnox Saas > Navigate to settings and click on manage clusters

    ![](images/d2iq/mng-cluster.png)

    **Step 4**: Click on **Onboard Now** to onboard a new cluster and In the next screen give a name to your cluster then click on **Save & Next**

    ![](images/d2iq/clust-name.png)

    **Step 5**: In the onboarding steps skip the first step as we have already added “KubeArmor” from the DKP catalog, Follow the “Install AccuKnox Agents” to onboard your cluster

    ![](images/d2iq/onboard-clust.png)

    **Step 6**: Copy the command and execute it in CLI

    ```sh
    helm upgrade --install accuknox-agents oci://public.ecr.aws/k9v9d5v2/accuknox-agents --version "v0.2.12" --set joinToken="38d851ba-2660-4aa3-b488-0cfb666bdb5e" --set spireHost="spire.demo.accuknox.com" --set ppsHost="pps.demo.accuknox.com" --set knoxGateway="knoxgw.demo.accuknox.com:3000" -n accuknox-agents --create-namespace
    Release "accuknox-agents" does not exist. Installing it now.
    Pulled: public.ecr.aws/k9v9d5v2/accuknox-agents:v0.2.12
    Digest: sha256:0bccba7c90fd5b844c84010613941da1938020336fa50c6ed9b1d045c37bb8ea
    NAME: accuknox-agents
    LAST DEPLOYED: Tue Apr 23 11:11:21 2024
    NAMESPACE: accuknox-agents
    STATUS: deployed
    REVISION: 1
    TEST SUITE: None
    ```

    **Step 7**: Verify if all the agents are up and running

    ```sh
    kubectl get po -n accuknox-agents
    NAME                                        READY   STATUS    RESTARTS   AGE
    agents-operator-6cf7ccb7c4-zl58p            1/1     Running   0          3m18s
    discovery-engine-86c7fcc48c-bgvg8           5/5     Running   0          3m18s
    feeder-service-78bfcc75bb-xxfqt             1/1     Running   0          2m45s
    policy-enforcement-agent-7c9cddddf6-6rwv7   1/1     Running   0          2m44s
    shared-informer-agent-787465dc55-wlzm8      1/1     Running   0          2m43s
    ```

    The agents are up and running.

    ## **Expected Outcome**

    After the Onboarding Process is complete user can utilize the following features of AccuKnox SaaS to protect their cloud workload at runtime:

    ### **Cloud Workloads**

    Users can view all the workloads within the cluster through the cloud workload graph view.

    ![](images/d2iq/graph-view.png)

    ### **Application Behavior**

    AccuKnox SaaS monitors cluster workload behavior using KubeArmor and AccuKnox Agents, installed as DaemonSets. Information is collected at the pod-level granularity, allowing users to access details for each pod across various namespaces. Workload behavior is presented through both list and graphical views

    ![](images/d2iq/app-behav.png)

    ### **List view**

    In the list view, users can access the selected pod's application behavior through three types of lists:

    **File Observability**: This list provides information about file access occurring inside the pod. It includes details such as which process is accessing which file within the pod. Additionally, it indicates the status of the access, whether it's allowed, audited, or denied.

    **Process Observability**: This list displays the processes executing within the pod, along with information about which pods or containers are executing those processes. It also provides details about processes that are blocked from execution within the pod.

    **Network Observability**: Network Observability presents the ingress and egress connections entering and leaving the pod. It offers information regarding port numbers, the source of ingress connections, and the destination to which egress connections are intended.

    ![](images/d2iq/list-view.png)

    ### **CWPP Dashboard**

    The AccuKnox CWPP Dashboard offers a comprehensive overview of runtime protection for clusters through various informative widgets. These widgets include:

    - **Alerts Summary**: Provides a summarized count of alerts generated in the cluster or a specific namespace. Details include total alerts, blocked alerts (from system block policies), and audited alerts (from audit policies).

    - **Compliance Summary**: Displays the compliance benchmarks applied to the cluster/namespace through KubeArmor's hardening policies. Presents information about MITRE, NIST, CIS, PCI-DSS benchmarks.

    - **Compliance Alerts**: Graphically represents compliance alerts generated in the cluster/namespace, using distinct color coding for various compliance benchmarks like MITRE, NIST, PCI-DSS, etc.

    - **Namespace Severity**: Offers a summary of attack severity attempted in the different namespaces within the cluster.

    - **Top 10 Policies by Alerts Count**: Presents a graphical representation of the top 10 policies for which alerts are generated in the cluster/namespace. Useful for identifying high-alert generating policies.

    - **Namespace Alerts**: Displays alerts specific to the selected namespace within the cluster, providing detailed information about the alerts.

    - **Pod Alerts**: Offers insights into alerts originating from the pods running within the cluster/namespace.

    - **Alert-based Operations**: Graphically represents alert-triggering operations such as file access, process blocks, and audits, giving users an overview of the types of alerts generated.

    - **Alerts based on Severity**: Provides information on attack severity levels that were mitigated by the runtime protection policies within the chosen cluster/namespace.

    ![](images/d2iq/cwpp-dash.png)

    ### **Policy Enforcement**

    The Policies section provides users with information about the runtime protection policies applied in the cluster. These policies are categorized as Discovered, Active, Inactive, Pending, Hardening, and more. Users can view policies based on the cluster, namespace, and policy type selected using the filters displayed on the page.

    AccuKnox offers the option to view policies related to a specific namespace and workload. In addition to discovered and hardening policies, users can also create custom policies using the policy editor tool.

    ![](images/d2iq/pol-screen.png)

    ### **Monitoring Logs**

    AccuKnox CNAPP Solution provides comprehensive visibility of the cloud assets with the help of Dashboards and logs/alerts. AccuKnox’s open-source KubeArmor can forward policy-related logs/alerts to the SaaS. Also, it can forward the container logs that are present in the workloads. Logs are generated in real time based on certain conditions/rules you configure on the security policies. You will get logs from four different components.

    ![](images/d2iq/logs-screen.png)

    The Log Detail contents vary depending on the selected component type of the log event.

    ![](images/d2iq/log-details.png)

    ### **SIEM/Notification Integration**

    Users can use the Feeder service agent to pass the logs to other SIEM tools like Splunk, ELK, Rsyslog, etc.., Users can also forward the logs from AccuKnox SaaS using the channel integration option to these SIEM tools. Users can integrate with various SIEM and ticketing tools like Splunk, Rsyslog, AWS CloudWatch, Elastic Search, Slack, and Jira.

    ![](images/d2iq/integ-screen.png)

- - -
[SCHEDULE DEMO](https://www.accuknox.com/contact-us){ .md-button .md-button--primary }