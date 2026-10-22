---
title: CIS Benchmarking Compliance Scan Onboarding
description: Guide on onboarding Kubernetes clusters for CIS Benchmarking compliance, enabling monitoring and improving security based on CIS standards.
---

# CIS Benchmarking Compliance Scan Onboarding

This guide details the steps to onboard a Kubernetes cluster to AccuKnox SaaS for CIS Benchmarking compliance scanning, enabling you to monitor and improve cluster security in line with CIS standards.

## Step 1: Generate an Access Token

To begin, create a token that will authenticate your cluster for scanning. Follow these steps:

1. Navigate to **Settings** > **Tokens** in the AccuKnox platform and click the **Create** button, give your token a descriptive name (e.g., "CIS-Compliance-Token"), and click **Generate**.
![image-20241114-115409.png](./images/cis-benchmarking/1.png)

1. Once the token is generated, copy it and securely save it for later use.
![image-20241114-115456.png](./images/cis-benchmarking/2.png)

## Step 2: Onboard Your Cluster

1. Go to **Settings** > **Manage Clusters** and click **Onboard Now** or select an existing cluster if you're updating a previously onboarded cluster.
![Navigate to Manage Clusters in AccuKnox Settings](./images/cluster-onboarding/image-1.png)

1. Enter a name for your cluster to identify it in Accuknox. From the jobs, choose **Kubernetes CIS Benchmarking.**

2. Select a label for easy identification and paste the token you generated in Step 1. Set a scan schedule based on your requirements. AccuKnox will automatically run scans according to the selected schedule.

![AccuKnox agent installation toggles and generated onboarding command](./images/cluster-onboarding/image-2.png)

Here's an example of how the command might look after selecting the CIS Benchmarking job. **Note that this is just an example; your actual command may vary based on your selections and join tokens so please copy it directly from the UI**:

```sh
helm upgrade --install agents oci://public.ecr.aws/k9v9d5v2/kspm-runtime \
-n agents --create-namespace \
--set global.agents.enabled=true \
--set global.agents.joinToken="" \
--set global.agents.url="demo.accuknox.com" \
--set kubearmor-operator.enabled=true \
--set kubearmor-operator.autoDeploy=true \
--set global.tenantId="" \
--set global.authToken="" \
--set global.clusterName="" \
--set global.cronTab="08 19 * * *" \
--set global.label="" \                         // Needed for any job to select specific workloads
--set global.cis.enabled=true \                 // Enable CIS Benchmark job
--set global.cis.toolConfig.platform="GKE" \    // Specify platform for CIS
--version v0.1.16
```

!!! info "Note"
    - If you are only enabling the CIS Benchmarking job, token is needed along with the label to identify the cluster. Also note that the platform selection is important for accurate benchmarking.
    - Currently we support GKE based CIS Benchmarking for managed GKE clusters.


1. Run this command in your terminal on a machine that has access to your Kubernetes cluster. The command will schedule the scan for CIS Benchmarking compliance.

2. Once the Helm installation is complete, return to the AccuKnox platform and click **Finish**.

## Step 3: View Compliance Findings

After the initial scan is completed, you can view the compliance results:

1. Go to **Issues** > **Findings** in AccuKnox.

2. Use the **Findings** dropdown to filter and select CIS k8s Benchmarking finding results.
![image-20241114-124849.png](./images/cis-benchmarking/6.png)

1. Each result will provide details on specific CIS controls and any non-compliant configurations detected.
![image-20241114-125156.png](./images/cis-benchmarking/7.png)

![image-20241114-125012.png](./images/cis-benchmarking/8.png)

This completes the onboarding process for CIS Benchmarking compliance scanning. You can review findings regularly to maintain and improve your cluster's CIS compliance.
