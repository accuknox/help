# In-Cluster Image Scanning with Helm

AccuKnox offers an in-cluster container image scanning solution designed to periodically inspect container images deployed within your Kubernetes (K8s) environment. This automated scanning process detects known vulnerabilities, promoting compliance and enhancing your cluster’s overall security. All scan results, including detailed vulnerability insights, are automatically sent to the AccuKnox Control Plane, where they can be viewed and managed through an intuitive user interface.

## 🛠 Installation Guide

Follow these steps to deploy the in-cluster image scanner using Helm:

### 1. Create a Label

In the AccuKnox Control Plane, create a unique [**Label**](https://app.accuknox.com/settings/labels). This will be associated with the container image scan reports.

### 2. Generate a Token

From the AccuKnox Control Plane:

- Generate an [**Artifact Token**](https://app.accuknox.com/settings/tokens)
- Note down both the **Token** and your **Tenant ID**

### 3. Schedule and Deploy the Scanner via Helm

Use the following Helm command to install the scanner in your Kubernetes cluster:

```bash
helm install kubeshield oci://public.ecr.aws/k9v9d5v2/kubeshield-chart -n agents --create-namespace \
  --set scan.tenantId="{{tenantId}}" \
  --set scan.authToken="{{authToken}}" \
  --set scan.url="{{url}}" \
  --set scan.label="{{label}}" \
  --set scan.cronTab="30 9 * * *" \
  --version "v0.1.2"
```

Replace the parameters (`{{tenantId}}`, `{{authToken}}`, `{{url}}`, `{{label}}` and `{{cronTab}}`) with the appropriate values.

#### Sample Output

```bash
Pulled: public.ecr.aws/k9v9d5v2/kubeshield-chart:v0.1.1
Digest: sha256:a4c1a8948db7a24d8990b71b53184f564960b2b39dbd6cba1cd6104c12addd75
NAME: kubeshield
LAST DEPLOYED: Mon May  5 10:08:24 2025
NAMESPACE: agents
STATUS: deployed
REVISION: 1
TEST SUITE: None
```

### ⚙️ Parameters:

| Variable  | Sample Value      | Description                |
| --------- | ----------------- | -------------------------- |
| tenantId  | 11                | AccuKnox Tenant ID         |
| authToken | eyJhbGc...        | AccuKnox Token {JWT}       |
| url       | cspm.accuknox.com | AccuKnox CSPM API Endpoint |
| label     | kubeshield        | AccuKnox Label             |
| cronTab   | 30 9 \* \* \*     | Schedule in Cron           |

> **Note:** Deploy the Scanner via Helm (One Time)
> If you don't want to schedule and just want to trigger scan for one time, remove this flag `--set scan.cronTab`

### ✅ Post-Installation

Once the scanner is deployed and completes a scan cycle, results will be visible in the [**Findings**](https://app.accuknox.com/issues/findings/findings-summary) or [**Registry Scan**](https://app.accuknox.com/issues/registry-scan) sections within the AccuKnox Control Plane.

- Navigate to [**Issues -> Findings**](https://app.accuknox.com/issues/findings/findings-summary)
- Switch to **Findings** tab
- Select **Container Image Findings** & do **Group by** based on **Label Name**
- You should be able to see the data for the **Label** used in above command

---

### 🧪 Scan Status from Cluster

🔧 Check if `kubeshield-controller-manager` is running fine or not

```bash
kubectl get po -n kubeshield
NAME                                             READY   STATUS    RESTARTS   AGE
kubeshield-controller-manager-5dd5cbc6d4-8xg8k   1/1     Running   0          22s
```

> STATUS should be **Running**

🔧 Check how many images are scanned or yet to scan

```bash
kubectl get ClusterScan -n kubeshield

kubectl get -n kubeshield clusterscan.kubeshield.accuknox.com/triggered-schedule-clusterscan-jdb2k -o yaml
```

> Replace value of `triggered-schedule-clusterscan-jdb2k` from 1st command
