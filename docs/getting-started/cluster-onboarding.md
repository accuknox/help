---
hide:
  - toc
---

# **Cluster Onboarding:** 

In the below section you can find the detailed steps to be followed for onboarding cluster to AccuKnox SaaS. AccuKnox Saas Platform supports onboarding of AKS, EKS, GKE and umanaged Clusters.  

??? "**Unmanaged cluster installation**"
    Below shown image is the unmanaged k3s cluster running in local machine with Ubuntu 22.04 Operating System. We can onboard this umanaged cluster by following the steps shown below 
    ![](/getting-started/images/k3s.png)

    **Step 1:** As a first time user, the management console will show up the CNAPP dashboard without any data mentioned in widgets, since the cloud account and cluster onboarding is not done. 

    ![](/getting-started/images/cnapp-dashboard.png)

    **Step 2:** Navigate to Manage Cluster from Settings Tab: 
    From this page we can onboard the clusters running in various cloud platforms like GCP,AWS and Azure. We can onboard locally setup cluster using an unmanaged cloud option. To onboard cluster select *onboard now* option

    ![](/getting-started/images/cluster-onboarding-1.png)

    **Step 3:** In this screen, give any name to the cluster that you are going to onboard now.

    ![](/getting-started/images/cluster-onboarding-2.png)

    **Step 4:** Onboarded Cluster without AccuKnox agents: 

    The onboarded cluster’s workload details will not be visible as we have not installed AccuKnox agents. So next we will be installing AccuKnox agents.

    ![](/getting-started/images/cluster-onboarding-3.png)

    **Step 5:** Installing KubeArmor and AccuKnox agents: 

    We are going to install KubeArmor and AccuKnox-agents to connect to the AccuKnox SaaS application.

    **Step 5.1:** KubeArmor Installation: 

    **KubeArmor:** 

    KubeArmor is a cloud-native runtime security enforcement system that restricts the behavior (such as process execution, file access, and networking operation) of containers and nodes at the system level. With KubeArmor, a user can:

    + Restrict file system access for certain processes

    + Restrict what processes can be spawned within the pod

    + Restrict the capabilities that can be used by the processes within the pod

    KubeArmor differs from seccomp-based profiles, wherein KubeArmor allows to dynamically set the restrictions on the pod. With seccomp, the restrictions must be placed during the pod startup and cannot be changed later. KubeArmor leverages Linux Security Modules (LSMs) to enforce policies at runtime.

    ![](/getting-started/images/cluster-onboarding-4.png)

    KubeArmor is installed using the following commands:

    ```bash
    >> curl -sfL http://get.kubearmor.io/ | sudo sh -s -- -b /usr/local/bin
    >> karmor install
    ```
    ![](/getting-started/images/cluster-onboarding-5.png)

    **Step 5.2:** AccuKnox-Agents installation:

    After installing KubeArmor we are going to install AccuKnox Agents in the cluster. 

    **AccuKnox Agents:** 

    1. **KubeArmor:**  KubeArmor is a cloud-native runtime security enforcement system that restricts the behavior (such as process execution, file access, and networking operation) of containers and nodes at the system level. KubeArmor dynamically set the restrictions on the pod. KubeArmor leverages Linux Security Modules (LSMs) to enforce policies at runtime.

    2. **Feeder Service:** It collects the feeds from kubeArmor and relays to the app. 

    3. **Shared Informer Agent:** It collects information about the cluster like pods, nodes, namespaces etc., 

    4. **Policy Discovery Engine:** It discovers the policies using the workload and cluster information that is relayed by a shared informer Agent. 

    ![](/getting-started/images/cluster-onboarding-6.png)

    AccuKnox Agents can be installed using the following command: 

    ```bash
    helm repo add accuknox-agents-dev https://accuknox-agents-dev:h47Sh4taEs@agents.accuknox.com/repository/accuknox-agents-dev
          helm repo update
          helm upgrade --install agents-operator accuknox-agents-dev/agents-operator \
            --set props.tenant_id="1354" \
            --set props.workspace_id="1354" \
            --set props.cluster_name="demotestk3" \
            --set props.CLUSTER_NAME="demotestk3" \
            --set props.cluster_id="********" \
            --set props.helm_repo="accuknox-agents-dev" \
            --set props.helm_repo_url="https://accuknox-agents-dev:**********@agents.accuknox.com/repository/accuknox-agents-dev" \
            --set props.docker_repo_host="agents.accuknox.com" \
            --set props.docker_repo_username="***********" \
            --set props.docker_repo_password="***********" \
            --create-namespace -n accuknox-agents
    ```

    ![](/getting-started/images/cluster-onboarding-7.png)

    **Note:** In the above command **workspace_id,cluster_name,tenant_id**  are specific to this example and it will vary based on the cluster

    **Step 6:** Onboarded Cluster: 

    After installing all the AccuKnox agents the cluster is onboarded successfully into the SaaS application. We can see the workload details of the onboarded cluster by Navigating to Inventory->cloud Workloads option 

    ![](/getting-started/images/cluster-onboarding-8.png)

??? "**Managed Cluster Onboarding**"

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

??? "**Cluster Offboarding**"

      In the below section you can find the detailed steps to be followed for Agent uninstallation from your cluster CLI and Deleting cluster from Accuknox SaaS.
      The given steps are common for all  AKS, EKS, GKE and unmanaged Clusters.

      **Agents Uninstallation** 

      **Step 1:** Login to your Cluster.

      ![](/getting-started/images/cluster-off-0.png)

      **Step 2:** Uninstall Accuknox agent and Spire token using the following commands:

      ```sh
            helm uninstall -n accuknox-agents  accuknox-agents
            kubectl -n accuknox-agents delete secrets spire-agent-secret
            kubectl delete ns accuknox-agents
      ```
      ![](/getting-started/images/cluster-off-1.png)

      **Cluster Deletion**

      **Step 1:** Login to Accuknox SaaS and Go to Manage Cluster under Settings

      ![](/getting-started/images/cluster-off-2.png)

      **Step 2:** Select the cluster and click Delete to delete the cluster from SaaS.

      ![](/getting-started/images/cluster-off-3.png)

 



  - - - 
[SCHEDULE DEMO](https://www.accuknox.com/contact-us){ .md-button .md-button--primary }