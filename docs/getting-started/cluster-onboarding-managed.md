---
hide:
  - toc
---

# **Managed Cluster Onboarding**

Below shown image is the GKE cluster running with Google Container optimized Operating System. 

![](/getting-started/images/gke-1.png)



![](/getting-started/images/gke-2.png)


We can onboard this managed cluster by following the steps shown below:

**Step 1:** After signing up, user will be taken to CNAPP dashboard. Since there is no cluster or cloud account onboarded widgets will not have any data. 

![](/getting-started/images/gke-3.png)


**Step 2:** Navigate to *Manage Cluster from Settings Tab*. From this page we can onboard the clusters running in various cloud platforms like GCP,AWS and Azure. We can also onboard unmanaged cluster set up locally in the on-premise environment or virtual machines. To onboard cluster select onboard now option


![](/getting-started/images/gke-4.png)

**Step 3:** In this screen, give any name to the cluster that you are going to onboard now.


![](/getting-started/images/gke-5.png)

**step 4:** Onboarded Cluster without AccuKnox agents:

The onboarded cluster’s workload details will not be visible as we have not installed AccuKnox agents. So next we will be installing AccuKnox agents.


![](/getting-started/images/gke-6.png)

**Step 5:** Installing KubeArmor and AccuKnox agents:

We are going to install KubeArmor and AccuKnox-agents to connect to the AccuKnox SaaS application.

**Step 5.1:** KubeArmor Installation:

**KubeArmor:**

KubeArmor is a cloud-native runtime security enforcement system that restricts the behavior (such as process execution, file access, and networking operation) of containers and nodes at the system level. With KubeArmor, a user can:

+ Restrict file system access for certain processes

+ Restrict what processes can be spawned within the pod

+ Restrict the capabilities that can be used by the processes within the pod

KubeArmor differs from seccomp-based profiles, wherein KubeArmor allows to dynamically set the restrictions on the pod. With seccomp, the restrictions must be placed during the pod startup and cannot be changed later. KubeArmor leverages Linux Security Modules (LSMs) to enforce policies at runtime.


![](/getting-started/images/gke-7.png)

KubeArmor is installed using the following commands:




```sh
>> curl -sfL http://get.kubearmor.io/ | sudo sh -s -- -b /usr/local/bin
>> karmor install
```

![](/getting-started/images/gke-8.png)

**Step 5.2:** AccuKnox-Agents installation:

After installing KubeArmor we are going to install AccuKnox Agents in the cluster.

**AccuKnox Agents:**

**1.KubeArmor:** KubeArmor is a cloud-native runtime security enforcement system that restricts the behavior (such as process execution, file access, and networking operation) of containers and nodes at the system level. KubeArmor dynamically set the restrictions on the pod. KubeArmor leverages Linux Security Modules (LSMs) to enforce policies at runtime.

**2.Feeder Service:** It collects the feeds from kubeArmor and relays to the app.

**3.Shared Informer Agent:** It collects information about the cluster like pods, nodes, namespaces etc.,

**4.Policy Discovery Engine:** It discovers the policies using the workload and cluster information that is relayed by a shared informer Agent.

![](/getting-started/images/gke-11.png)

AccuKnox Agents can be installed using the following command:


```sh
      helm repo add accuknox-agents https://accuknox-agents-dev:h47Sh4taEs@artifactory.accuknox.com/repository/accuknox-agents
      helm repo update
      helm upgrade --install agents-operator accuknox-agents/agents-operator \
            --set props.tenant_id="399" \
            --set props.workspace_id="399" \
            --set props.cluster_name="gke-cluster" \
            --set props.CLUSTER_NAME="gke-cluster" \
            --set props.cluster_id="1814" \
            --set props.helm_repo="accuknox-agents" \
            --set props.helm_repo_url="https://accuknox-agents-dev:h47Sh4taEs@artifactory.accuknox.com/repository/accuknox-agents" \
            --set props.docker_repo_host="artifactory.accuknox.com" \
            --set props.docker_repo_username="accuknox-agents-image" \
            --set props.docker_repo_password="SjnnJxs3fk" \
            --create-namespace -n accuknox-agents 
```


![](/getting-started/images/gke-9.png)

**Note:** In the above command workspace_id,cluster_name,tenant_id are specific to this example and it will vary based on the cluster

**Step 6:** After installing all the AccuKnox agents the cluster is onboarded successfully into the SaaS application. We can see the workload details of the onboarded cluster by Navigating to Inventory->cloud Workloads option

![](/getting-started/images/gke-10.png)


  - - - 
[SCHEDULE DEMO](https://www.accuknox.com/contact-us){ .md-button .md-button--primary }