# Onboard Cluster for Misconfiguration Scanning

This guide outlines the steps for onboarding a cluster to AccuKnox SaaS for scanning cluster misconfigurations.

For onboarding a cluster and for scanning for misconfigurations you need to create a token first. For creating follow these steps

1. Go to `Settings > Tokens`.
2. Click on the create button.
3. Give your token a name.
4. Click on generate button.

![image-20240930-120702.png](images/cluster-misconfig-onboarding/1.png)

Once the token is generated, copy it and take a note of it.

![image-20241009-075101.png](images/cluster-misconfig-onboarding/2.png)

Now go to `Settings > Manage Clusters`, click on onboard now button or select an existing cluster.

![image-20240930-121156.png](images/cluster-misconfig-onboarding/3.png)

Give your cluster a name. Under the Agents Installation section select Cluster Misconfiguration. Select a label and paste your token.

![image-20241009-075422.png](images/cluster-misconfig-onboarding/4.png)

You can also change the schedule as per your requirement. Then next scan will happen based on the schedule. Scroll down and copy the helm command and run it inside a terminal. Then click on Finish button.

![image-20241009-075905.png](images/cluster-misconfig-onboarding/5.png)

Once the scan is completed you can see the results on the findings page.

1. Go to the `Issues > Findings` page.

2. Select the Cluster Finding from the drop down.

![image-20241009-080027.png](images/cluster-misconfig-onboarding/6.png)

Click on any of the findings to see more details.

![image-20241009-080245.png](images/cluster-misconfig-onboarding/7.png)

![image-20241009-080311.png](images/cluster-misconfig-onboarding/8.png)
