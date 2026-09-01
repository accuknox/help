---
title: Onboard Cluster for Misconfiguration Scanning
description: AccuKnox helps detect and fix security misconfigurations in Kubernetes clusters, securing applications and infrastructure.
---

# Onboard Cluster for Misconfiguration Scanning
This guide outlines the steps for onboarding a cluster to AccuKnox SaaS for scanning cluster misconfigurations.

**Step 1:** To onboard a cluster and scan for misconfigurations, you first need to create a token. Follow these steps:

Go to `Settings > Tokens` and click on the create button.
Give your token a name and click on generate button.

![image-20240930-120702.png](images/cluster-misconfig-onboarding/1.png)

**Step 2:** Once the token is generated, copy it and take a note of it.

![image-20241009-075101.png](images/cluster-misconfig-onboarding/2.png)

**Step 3:** Now go to `Settings > Manage Clusters`, click on onboard now button or select an existing cluster.

![Navigate to Manage Clusters in AccuKnox Settings](./images/cluster-onboarding/image-1.png)

**Step 4:** Give your cluster a name. Under the Jobs section **select Cluster Misconfiguration**. Select a label and paste your token. You can also change the schedule as per your requirement. Then next scan will happen based on the schedule. Scroll down and copy the helm command and run it inside a terminal. Then click on Finish button.

![AccuKnox agent installation toggles and generated onboarding command](./images/cluster-onboarding/image-2.png)

**Step 5:** Here's an example of how the command might look after selecting the Cluster Misconfiguration job. **Note that this is just an example; your actual command may vary based on your selections and join tokens so please copy it directly from the UI**:

```sh
helm upgrade --install agents oci://public.ecr.aws/k9v9d5v2/kspm-runtime \
-n agents --create-namespace \
--set global.agents.enabled=true \
--set global.agents.joinToken="" \
--set global.agents.url="demo.accuknox.com" \
--set kubearmor-operator.enabled=true \
--set kubearmor-operator.autoDeploy=true \
--set global.tenantId="19" \
--set global.authToken="" \
--set global.clusterName="TEST-B" \
--set global.cronTab="08 19 * * *" \
--set global.label="" \                         // Needed for any job to select specific workloads
--set global.riskassessment.enabled=true \      // Enable Risk Assessment job
--version v0.1.16
```

**Step 6:** Once the scan is completed you can see the results on the findings page.

**Step 7:**
1. Go to the `Issues > Findings` page.

2. Select the Cluster Finding from the drop down.

![image-20241009-080027.png](images/cluster-misconfig-onboarding/6.png)

**Step 8:** Click on any of the findings to see more details.

![image-20241009-080245.png](images/cluster-misconfig-onboarding/7.png)

![image-20241009-080311.png](images/cluster-misconfig-onboarding/8.png)
