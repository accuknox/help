Cluster Onboarding: 
Un Managed cluster installation:
![](/images/k3s.png)
Step 1: As a first time user, the management console will show up the CNAPP dashboard without any data mentioned in widgets, since the cloud account and cluster onboarding is not done. 
![](/images/cnapp-dashboard.png)
Step 2: Navigate to Manage Cluster from Settings Tab: 
From this page we can onboard the clusters running in various cloud platforms like GCP,AWS and Azure. We can onboard locally setup cluster using an unmanaged cloud option. 
![](/images/cluster-onboarding-1.png)

Step 3: In our example we are going to onboard a locally setup cluster using an unmanaged cloud option. 
For unmanaged cloud option Regional/zonal values are optional.
![](/images/cluster-onboarding-2.png)
step 4: Onboarded Cluster without AccuKnox agents: 

The onboarded cluster’s workload details will not be visible as we have not installed AccuKnox agents. So next we will be installing AccuKnox agents.
![](/images/cluster-onboarding-3.png)
Step 5: Installing KubeArmor and AccuKnox agents: 

We are going to install KubeArmor and AccuKnox-agents to connect to the AccuKnox SaaS application.

Step 5.1: KubeArmor Installation: 

KubeArmor: 
KubeArmor is a cloud-native runtime security enforcement system that restricts the behavior (such as process execution, file access, and networking operation) of containers and nodes at the system level. With KubeArmor, a user can:

Restrict file system access for certain processes

Restrict what processes can be spawned within the pod

Restrict the capabilities that can be used by the processes within the pod
![](/images/kubeArmor.png)

KubeArmor differs from seccomp-based profiles, wherein KubeArmor allows to dynamically set the restrictions on the pod. With seccomp, the restrictions must be placed during the pod startup and cannot be changed later. KubeArmor leverages Linux Security Modules (LSMs) to enforce policies at runtime.
![](/images/cluster-onboarding-4.png)
KubeArmor is installed using the following commands:

```bash
>> curl -sfL http://get.kubearmor.io/ | sudo sh -s -- -b /usr/local/bin
>> karmor install
```
![](/images/cluster-onboarding-5.png)
Step 5.2 AccuKnox-Agents installation:

After installing KubeArmor we are going to install AccuKnox Agents in the cluster. 

AccuKnox Agents: 
KubeArmor:  KubeArmor is a cloud-native runtime security enforcement system that restricts the behavior (such as process execution, file access, and networking operation) of containers and nodes at the system level. KubeArmor dynamically set the restrictions on the pod. KubeArmor leverages Linux Security Modules (LSMs) to enforce policies at runtime.

Feeder Service: It collects the feeds from kubeArmor and relays to the app. 

Shared Informer Agent: It collects information about the cluster like pods, nodes, namespaces etc., 

Policy Discovery Engine: It discovers the policies using the workload and cluster information that is relayed by a shared informer Agent. 
![](/images/cluster-onboarding-6.png)
Accuknox Agents can be installed using the following command: 

```bash
 helm repo add accuknox-agents-dev https://accuknox-agents-dev:h47Sh4taEs@agents.accuknox.com/repository/accuknox-agents-dev
      helm repo update
      helm upgrade --install agents-operator accuknox-agents-dev/agents-operator \
        --set props.tenant_id="1354" \
        --set props.workspace_id="1354" \
        --set props.cluster_name="demotestk3" \
        --set props.CLUSTER_NAME="demotestk3" \
        --set props.cluster_id="1762" \
        --set props.helm_repo="accuknox-agents-dev" \
        --set props.helm_repo_url="https://accuknox-agents-dev:h47Sh4taEs@agents.accuknox.com/repository/accuknox-agents-dev" \
        --set props.docker_repo_host="agents.accuknox.com" \
        --set props.docker_repo_username="accuknox-agents-image" \
        --set props.docker_repo_password="SjnnJxs3fk" \
        --create-namespace -n accuknox-agents
```
![](/images/cluster-onboarding-7.png)

Note: In the above command workspace_id,cluster_name,tenant_id  are specific to this example and it will vary based on the cluster

Step 6: Onboarded Cluster: 

After installing all the AccuKnox agents the cluster is onboarded successfully into the SaaS application. We can see the workload details of the onboarded cluster by Navigating to Inventory->cloud Workloads option 
![](/images/cluster-onboarding-8.png)

Cloud Account onboarding:
Onboarding AWS Account using Access Keys method:
Step 1: To onboard Cloud Account Navigate to Settings->cloud Accounts
![](/images/cloud-onboarding-1.png)
Step 2: In the Cloud Account Page select Add Account option

We can onboard AWS, Microsoft Azure and Google Cloud Platform Accounts in AccuKnox Saas.
![](/images/cloud-onboarding-2.png)
Step 3: We can onboard AWS account using Manual and Access Keys Methods.
![](/images/cloud-onboarding-3.png)
Step 4: Now select Access Keys Connection method from the dropdown menu.
![](/images/cloud-onboarding-4.png)
Step 5: In the next Screen select the labels and Tags field from the dropdown Menu.
![](/images/cloud-onboarding-5.png)
Step 6: After giving labels and Tag in the Next Screen Provide the AWS account’s Access Key and Secret Access Key ID and Select the Region of the AWS account.
![](/images/cloud-onboarding-6.png)
Step 7: AWS account is added to the AccuKnox using Access Key Method. We can see the onboarded cloud account by navigating to Settings->cloud Accounts option. 
![](/images/cloud-onboarding-7.png)