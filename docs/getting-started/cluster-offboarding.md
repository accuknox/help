---
hide:
  - toc
---

# **Cluster Offboarding**

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