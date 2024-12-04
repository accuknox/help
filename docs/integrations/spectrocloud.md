# Deploy AK agents via Spectrocloud / Palette

This document provides instructions on using Spectrocloud/Palette to onboard the clusters to AccuKnox via the use of Cluster Add On Profiles. Essentially simplifying the onboarding of clusters already connected to the Spectrocloud platform.

## Prerequisites

### Add Helm Charts

To add the helm charts to be deployed, navigate to Tenant Settings → Infrastructure → Registries and click on **Add New Helm Registry**

![image-20240807-122924.png](./images/spectrocloud/1.png)

Enter the following:

- Name: KubeArmor

- Endpoint: `https://kubearmor.github.io/charts`

Click on **Confirm**

![image-20240807-123434.png](./images/spectrocloud/2.png)

Follow the same steps as above and add another helm chart registry for the AccuKnox Enterprise Agents. The following details will be used to add the registry:

- Name: AccuKnox-Agents

- Endpoint: `http://agents.accuknox.com`

### Generate Access Key

On the AccuKnox platform, navigate to Settings → User Management. Click on the three dots to the right of your username and select **Get Access Key**

![image-20241029-095248.png](./images/spectrocloud/3.png)

In the pop up,

- Enter a Name for the access key

- Set the Expiration time for the key's usage

- Select a sufficient role, for the purpose of onboarding cluster

- Enter the maximum number of clusters that can be onoarded using this access key

![image-20241029-095403.png](./images/spectrocloud/4.png)

Click on **Generate** and copy the access key.

## Configuration

![image-20241029-142425.png](./images/spectrocloud/5.png)

### Create a Cluster Profile

Navigate to Profiles and click on **Add Cluster Profile**

![image-20240807-131647.png](./images/spectrocloud/6.png)

In the following screen, enter a Name for the profile, a version number and select Type as Add-On. Click on **Next**

![image-20240807-131828.png](./images/spectrocloud/7.png)

Click on **Add Helm chart** and select **Public packs**

![image-20240807-132128.png](./images/spectrocloud/8.png)

Select the KubeArmor Registry and click on KubeArmor Operator

![image-20240807-132229.png](./images/spectrocloud/9.png)

In the values for the helm chart, enter the namespace to deploy the agent and set `autoDeploy` to `true`. Click on **Confirm & Create**

![image-20240807-132347.png](./images/spectrocloud/10.png)

Select Add Helm Charts → Public packs again. This time, select the AccuKnox-Agents Registry and click on accuknox-agents

![image-20240807-132556.png](./images/spectrocloud/11.png)

In the values file, enter the namespace and set the following variables with regards to the AccuKnox platform in use:

- `ppsHost`: `pps.<env-name>.accuknox.com`

- `knoxGateway`: `knox-gw.<env-name>.accuknox.com:3000`

- `spireHost`: `spire.<env-name>.accuknox.com`

**Note**: The values for the above variables can be fetched from the cluster onboarding screen in the AccuKnox platform. The accessKey should be replaced by the user token generated on AccuKnox to reuse this profile

- `clusterName`: A name to uniquely identify the cluster on AccuKnox

- `tokenURL:`Value will be `cwpp.<env-name>.accuknox.com` where <env name> could be demo or other depending on the AccuKnox platform URL.

- `accessKey`: The Access Key that was generated from AccuKnox

Click on **Confirm & Create**

![image-20241030-052955.png](./images/spectrocloud/12.png)

Click on **Next** after creating the two layers

![image-20240807-133301.png](./images/spectrocloud/13.png)

Click on **Finish Configuration** to finalize setting up the Cluster Profile

![image-20240807-133353.png](./images/spectrocloud/14.png)

## Deploying Agents

Navigate to Profiles and select the Cluster Profile created for AccuKnox

![image-20240807-133653.png](./images/spectrocloud/15.png)

Click on **Deploy**

![image-20240807-133729.png](./images/spectrocloud/16.png)

Select the cluster and click on **Confirm**

![image-20241030-053833.png](./images/spectrocloud/17.png)

Edit the `clusterName` and provide a unique name for identification in the AccuKnox platform. It can contain alphanumeric characters with an hyphen in between the characters.

Click on **Save** after confirming the details.

![image-20241030-074633.png](./images/spectrocloud/18.png)

To onboard any clusters, the same profile can be reused by changing only the `clusterName` parameter.
