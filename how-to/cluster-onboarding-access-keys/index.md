---
title: Cluster Onboarding with Access Keys
description: Guide to onboarding multiple clusters using access keys, with options to set expiration times and limit the number of onboarded clusters.
---

# Cluster Onboarding with Access Keys

Streamlining cluster onboarding is made easy with access keys, allowing users to onboard multiple clusters using the same key. Additionally, users can set expiration times for these keys and specify the number of clusters each key can onboard. This process can be performed directly from the CLI if the access key is already created, offering enhanced flexibility and convenience.

**Pre-requisite:**

1. Kubernetes (managed/unmanaged) cluster

2. AccuKnox CNAPP login access

3. One or more clusters to onboard

4. Access Key (See how to [create](https://help.accuknox.com/how-to/create-access-keys/ "https://help.accuknox.com/how-to/create-access-keys/"))


## AccuKnox Agents

The AccuKnox Agent is a Kubernetes operator that deploys and manages the agents required to onboard a cluster to AccuKnox CNAPP:

- Feeder service — collects KubeArmor feeds.
- Shared-informer-agent — gathers cluster metadata (nodes, pods, namespaces).
- Policy-enforcement-agent — applies labels and enforces policies.
- Discovery Engine — analyzes workloads and auto-discovers least‑permissive policy sets using KubeArmor visibility.

The operator also manages resource limits and automatically scales agents when cluster size changes.

## Onboarding

In the case of the Access Key onboarding method, you can directly onboard clusters from the CLI. To onboard a new cluster, run the following command:

```cmd
helm upgrade --install agents oci://public.ecr.aws/k9v9d5v2/kspm-runtime \
-n agents --create-namespace \
--set global.agents.enabled=true \
--set global.agents.url="demo.accuknox.com" \
--set kubearmor-operator.enabled=true \
--set kubearmor-operator.autoDeploy=true \
--set global.enableJobsUrl=true \
--set global.kiem.enabled=true \
--set global.riskassessment.enabled=true \
--set global.inClusterScan.enabled=true \
--set global.cis.enabled=true \
--set global.clusterName="<existing-cluster-names>" \
--set global.cronTab="20 09 * * *" \
--set global.label="<label>" \
--set global.tenantId="<tenant-id>" \
--set global.agents.accessKey="<access-key>" \
--version v0.1.49
```

!!! info "Note"
    - Ensure the following when using the command:
        - `--version v0.1.16` (minimum) for access key onboarding.
        - `--set global.label` is required.
        - Provide the generated access key via `--set global.agents.accessKey="<your_access_key>"`.
        - Specify `--set global.cronTab` to set the cron schedule.
    - In the commands above, substitute `--set clusterName` with the desired cluster name, and replace the ```<your_access_key>``` with the **Access Keys** generated from UI. Adjust the URLs if required


#### Output

```cmd
Release "agents" does not exist. Installing it now.
Pulled: registry-1.docker.io/accuknox/accuknox-agents:v0.5.11
Digest: sha256:6b7870020c0470741b7a89f47fd6f4e85882521721ce50407351d231508c6aaf
NAME: agents
LAST DEPLOYED: Thu Jan  2 19:05:38 2025
NAMESPACE: accuknox-agents
STATUS: deployed
REVISION: 1
TEST SUITE: None
```

To verify please use

```cmd
kubectl get po -n accuknox-agents
```

After installing all the AccuKnox agents, the cluster is onboarded successfully into the SaaS application. We can see the workload details of the onboarded cluster by Navigating to Inventory-> Clusters

![image-20250102-134403.png](./images/cluster-onboarding-access-keys/1.png)

#### View the workloads

![image-20250102-134439.png](./images/cluster-onboarding-access-keys/2.png)

!!! info "Note"
    You can repeat the same command with different **"clusterName"** to onboard multiple cluster using access keys
