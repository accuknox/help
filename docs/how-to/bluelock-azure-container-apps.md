---
title: Deploy BlueLock on Azure Container Apps
description: Deploy BlueLock on Azure Container Apps with Terraform, onboard the replicas to AccuKnox as a VM cluster and block a command to confirm runtime enforcement.
---

# Deploy BlueLock on Azure Container Apps

!!! info "Overview"
    This guide builds an Azure Container Apps test environment with Terraform, onboards it to AccuKnox as a VM cluster and blocks a command in a running replica. Terraform creates the Azure network, a control plane VM and a container app with two replicas that run BlueLock. Read [BlueLock Runtime Security for Serverless Containers](bluelock.md) first if you want the background.

## Workflow at a Glance

<div class="ak-dia" role="img" aria-label="Six-step workflow for Azure Container Apps. Step 1, get a join token from the AccuKnox console. Step 2, sign in to AWS and public ECR. Step 3, create the base infrastructure with Terraform in 1-infra, which takes about 5 minutes. Step 4, deploy the container app with Terraform in 2-app. Step 5, confirm the control plane VM and two replicas appear in AccuKnox. Step 6, apply a block policy and confirm the command is denied and an alert appears.">
<svg viewBox="0 0 640 292" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="macf" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="7" markerHeight="7" orient="auto">
      <path class="head" d="M0 0 L8 4 L0 8 z"/>
    </marker>
    <marker id="macfa" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="7" markerHeight="7" orient="auto">
      <path class="head-acc" d="M0 0 L8 4 L0 8 z"/>
    </marker>
  </defs>
  <rect class="acc" x="8" y="8" width="200" height="126" rx="8"/>
  <circle class="step" cx="32" cy="32" r="12"/>
  <text class="t-step" x="32" y="36" text-anchor="middle">1</text>
  <text class="t-s" x="54" y="36">Step 1</text>
  <text class="t-h" x="24" y="70">Get a join</text>
  <text class="t-h" x="24" y="87">token</text>
  <text class="t-s" x="24" y="109">Settings, Manage</text>
  <text class="t-s" x="24" y="124">Cluster, Onboard</text>
  <path class="ln" d="M209 71 H227" marker-end="url(#macf)"/>
  <rect class="p" x="228" y="8" width="200" height="126" rx="8"/>
  <circle class="step" cx="252" cy="32" r="12"/>
  <text class="t-step" x="252" y="36" text-anchor="middle">2</text>
  <text class="t-s" x="274" y="36">Step 2</text>
  <text class="t-h" x="244" y="70">Sign in to AWS</text>
  <text class="t-h" x="244" y="87">and public ECR</text>
  <text class="t-s" x="244" y="109">aws configure and</text>
  <text class="t-s" x="244" y="124">docker login</text>
  <path class="ln" d="M429 71 H447" marker-end="url(#macf)"/>
  <rect class="p" x="448" y="8" width="200" height="126" rx="8"/>
  <circle class="step" cx="472" cy="32" r="12"/>
  <text class="t-step" x="472" y="36" text-anchor="middle">3</text>
  <text class="t-s" x="494" y="36">Step 3</text>
  <text class="t-h" x="464" y="70">Create the base</text>
  <text class="t-h" x="464" y="87">infrastructure</text>
  <text class="t-s" x="464" y="109">terraform apply in</text>
  <text class="t-s" x="464" y="124">1-infra, about 5 min</text>
  <rect class="p" x="8" y="162" width="200" height="126" rx="8"/>
  <circle class="step" cx="32" cy="186" r="12"/>
  <text class="t-step" x="32" y="190" text-anchor="middle">4</text>
  <text class="t-s" x="54" y="190">Step 4</text>
  <text class="t-h" x="24" y="224">Deploy the</text>
  <text class="t-h" x="24" y="241">container app</text>
  <text class="t-s" x="24" y="263">terraform apply in</text>
  <text class="t-s" x="24" y="278">2-app</text>
  <path class="ln" d="M209 225 H227" marker-end="url(#macf)"/>
  <rect class="acc" x="228" y="162" width="200" height="126" rx="8"/>
  <circle class="step" cx="252" cy="186" r="12"/>
  <text class="t-step" x="252" y="190" text-anchor="middle">5</text>
  <text class="t-s" x="274" y="190">Step 5</text>
  <text class="t-h" x="244" y="224">Confirm the</text>
  <text class="t-h" x="244" y="241">nodes</text>
  <text class="t-s" x="244" y="263">Control plane VM and</text>
  <text class="t-s" x="244" y="278">2 replicas</text>
  <path class="ln" d="M429 225 H447" marker-end="url(#macf)"/>
  <rect class="good" x="448" y="162" width="200" height="126" rx="8"/>
  <circle class="step" cx="472" cy="186" r="12"/>
  <text class="t-step" x="472" y="190" text-anchor="middle">6</text>
  <text class="t-s" x="494" y="190">Step 6</text>
  <text class="t-h" x="464" y="224">Test the block</text>
  <text class="t-h" x="464" y="241">policy</text>
  <text class="t-s" x="464" y="263">ls is denied and</text>
  <text class="t-s" x="464" y="278">an alert appears</text>
  <path class="ln" d="M548 135 V148 H108 V161" marker-end="url(#macf)"/>
</svg>
</div>

## How the Deployment Fits Together

Azure Container Apps runs on Kubernetes, but Azure hides the API server. You cannot onboard it as a Kubernetes cluster. BlueLock uses a VM cluster instead. The control plane runs on a VM, and the container app replicas act as the worker nodes.

<div class="ak-dia" role="img" aria-label="Azure Container Apps architecture. Inside one virtual network, subnet 1 holds a control plane VM that runs the AccuKnox agents and reaches AccuKnox SaaS outbound. Subnet 2, delegated to Microsoft.App/environments, holds a Container Apps environment with one container app and two replicas. Each replica runs a bluelock init container, an armored-container and a kubearmor-vm-adapter. The adapters connect to the control plane on ports 32768 to 32771. A test client reaches the app on TCP port 1337 through ingress.">
<svg viewBox="0 0 920 450" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="maca" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="7" markerHeight="7" orient="auto">
      <path class="head" d="M0 0 L8 4 L0 8 z"/>
    </marker>
    <marker id="macaa" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="7" markerHeight="7" orient="auto">
      <path class="head-acc" d="M0 0 L8 4 L0 8 z"/>
    </marker>
  </defs>
  <rect class="plane" x="330" y="10" width="260" height="58" rx="8"/>
  <text class="t-plane" x="460" y="36" text-anchor="middle">AccuKnox SaaS</text>
  <text class="t-pill" x="460" y="54" text-anchor="middle">Policies, alerts, inventory</text>
  <rect class="p2" x="10" y="104" width="900" height="280" rx="8"/>
  <text class="t-h" x="26" y="128">Virtual network</text>
  <rect class="p" x="30" y="142" width="250" height="226" rx="8"/>
  <text class="t-s" x="46" y="162">Subnet 1</text>
  <rect class="acc" x="50" y="180" width="210" height="112" rx="8"/>
  <text class="t-h" x="64" y="208">Control plane VM</text>
  <text class="t-s" x="64" y="228">Ubuntu with a public IP</text>
  <text class="t-s" x="64" y="246">Runs the AccuKnox agents</text>
  <text class="t-mono" x="64" y="270">knoxctl onboard vm cp-node</text>
  <text class="t-s" x="46" y="316">Receives adapter traffic</text>
  <text class="t-s" x="46" y="330">on ports 32768 to 32771</text>
  <rect class="p" x="320" y="142" width="570" height="226" rx="8"/>
  <text class="t-s" x="336" y="162">Subnet 2, delegated to Microsoft.App/environments</text>
  <rect class="hollow" x="336" y="174" width="538" height="182" rx="8"/>
  <text class="t-h" x="350" y="196">Container Apps environment</text>
  <rect class="acc" x="350" y="206" width="510" height="138" rx="8"/>
  <text class="t-h" x="364" y="228">Container app, 2 replicas</text>
  <rect class="p" x="364" y="238" width="232" height="96" rx="6"/>
  <text class="t-h" x="376" y="256">Replica 1</text>
  <rect class="hollow" x="376" y="262" width="208" height="20" rx="4"/>
  <text class="t-s" x="384" y="276">bluelock (init container)</text>
  <rect class="hollow" x="376" y="284" width="208" height="20" rx="4"/>
  <text class="t-s" x="384" y="298">armored-container</text>
  <rect class="hollow" x="376" y="306" width="208" height="20" rx="4"/>
  <text class="t-s" x="384" y="320">kubearmor-vm-adapter</text>
  <rect class="p" x="616" y="238" width="232" height="96" rx="6"/>
  <text class="t-h" x="628" y="256">Replica 2</text>
  <rect class="hollow" x="628" y="262" width="208" height="20" rx="4"/>
  <text class="t-s" x="636" y="276">bluelock (init container)</text>
  <rect class="hollow" x="628" y="284" width="208" height="20" rx="4"/>
  <text class="t-s" x="636" y="298">armored-container</text>
  <rect class="hollow" x="628" y="306" width="208" height="20" rx="4"/>
  <text class="t-s" x="636" y="320">kubearmor-vm-adapter</text>
  <path class="ln-acc" d="M320 255 H282" marker-end="url(#macaa)"/>
  <path class="ln-acc" d="M155 180 V39 H330" marker-end="url(#macaa)"/>
  <text class="t-s" x="166" y="96">outbound to SaaS</text>
  <rect class="p" x="560" y="404" width="300" height="38" rx="8"/>
  <text class="t-mono" x="710" y="428" text-anchor="middle">socat - TCP:APP_URL:1337</text>
  <path class="ln" d="M710 404 V386" marker-end="url(#maca)"/>
  <text class="t-s" x="724" y="399">TCP ingress on 1337</text>
</svg>
</div>

Two Azure terms matter in this guide:

| Azure term | What it is |
|---|---|
| Container Apps environment | A resource boundary. You define CPU, memory and networking for the container apps inside it |
| Container app | Similar to a ReplicaSet. Each replica is a pod that runs one or more containers |

## Prerequisites

| Requirement | Used for |
|---|---|
| Azure access | Creating the resource group, virtual network, VM and Container Apps environment |
| AWS CLI, configured | The login to public ECR in Step 2 |
| Terraform | Running both scripts |
| Docker | The `docker login` command in Step 2 |
| `git` | Cloning the BlueLock repository |
| `socat` | Connecting to the container app in Step 6 |
| AccuKnox account | Getting a join token and viewing the results |

## Step 1. Get a Join Token From AccuKnox

In the AccuKnox console, open Settings, then Manage Cluster, then Onboard. Select the cluster type VM and enter a cluster name. Copy the join token from the `knoxctl onboard vm cp-node` command.

Terraform runs that command for you on the control plane VM, so you only need the token. Keep the console page open to watch the cluster appear.

## Step 2. Sign in to AWS and Public ECR

Enter your Access Key ID and Secret Access Key when `aws configure` asks for them.

```bash
aws configure
```

Log in to public ECR.

```bash
aws ecr-public get-login-password --region us-east-1 | docker login --username AWS --password-stdin public.ecr.aws/k9v9d5v2
```

## Step 3. Create the Base Infrastructure

Clone the BlueLock repository and open the `azure-container-apps` folder.

```bash
git clone https://github.com/accuknox/bluelock.git
cd bluelock/terraform/azure-container-apps
```

Create the base infrastructure with your join token. This takes about 5 minutes.

```bash
cd 1-infra
terraform init
terraform apply -var="vm_token=YOUR_JOIN_TOKEN"
```

The script creates the resource group, the virtual network, the control plane VM and the Container Apps environment. It then installs Docker and `knoxctl` on the VM and onboards the VM as the control plane node with your token.

??? info "Variables you can change"
    Change a default with `-var`, for example `-var="location=<REGION>"`.

    | Variable | Default | Notes |
    |---|---|---|
    | `location` | `Central India` | Azure region |
    | `resource_group_name` | `rg-azure-test` | Resource group that holds everything |
    | `name_prefix` | `bluelock-aca` | Prefix for resource names |
    | `vm_username` | `testuser` | Login name on the control plane VM |
    | `vm_password` | Has a default | Set your own value with `-var` |
    | `vm_token` | None | Required. Your AccuKnox join token |

    The script prints these outputs: `resource_group_name`, `vnet_name`, `vm_public_ip`, `vm_private_ip`, `container_app_environment_id` and `container_app_environment_name`.

## Step 4. Create the Container App

Create the container app. The command reads the VM public IP from the output of Step 3.

```bash
cd ../2-app
terraform init
terraform apply \
    -var="vm_public_ip=$(cd ../1-infra && terraform output -raw vm_public_ip)"
```

Terraform creates a container app with 2 replicas. Each replica runs the `bluelock` init container, the `armored-container` and the `kubearmor-vm-adapter`.

??? info "Variables you can change"
    | Variable | Default | Notes |
    |---|---|---|
    | `resource_group_name` | `rg-azure-test` | Use the same value as in `1-infra` |
    | `container_app_environment` | `bluelock-aca-container-app-env` | Environment to deploy into |
    | `container_app_name` | `bluelock-container-app` | Name of the container app |
    | `vm_public_ip` | None | Required. Public IP of the control plane VM |

??? note "Set up manually instead of using Terraform"
    Use this path when you cannot run the Terraform scripts. It replaces Steps 3 and 4. Create the following Azure resources in this order.

    **1. Virtual network**

    1. Create a virtual network with 2 subnets. Make one a normal subnet and delegate the other to `Microsoft.App/environments`, because the Container Apps environment joins this network. See the [Azure networking guide](https://learn.microsoft.com/en-us/azure/container-apps/networking#environment-selection) for the subnet size.
    2. For example, create `default` with size /24 and `aca-subnet` with size /20.

    **2. Virtual machine**

    1. Create an Ubuntu machine in the normal subnet of the virtual network.
    2. Open inbound access to all ports from everywhere, for every protocol, in the VM's network security group. Do this for testing only. Do not do this in production. Open only the ports that the agents need.
    3. Install Docker.
    4. Onboard the VM as the control plane of a VM cluster in AccuKnox.

    **3. Container app**

    1. Create a container app.
    2. When it asks for a Container Apps environment, create a new one. In the Network tab, integrate it with the delegated subnet that you created.
    3. In Containers, select Docker registry and enter the image `delusionaloptimist/ka-socat:latest`.
    4. In Monitoring, select stream logs without storing.
    5. In Ingress, enable ingress. Allow TCP from everywhere on port 1337 with target port 1337. Leave the other settings unchanged.
    6. Create the container app.

    **4. Configure the container app**

    1. In the left panel, open Export template under Automation and choose Deploy.

        ![The Azure Export template page for the container app with the Deploy button highlighted](images/bluelock-azure-container-apps/export-template.png)

    2. Choose Edit template. Replace the `template` object in the JSON with the following. Replace `<CONTROL_PLANE_IP>` in the VM adapter arguments with the public IP of the VM.

        ```json
        "template": {
            "containers": [
                {
                    "image": "public.ecr.aws/k9v9d5v2/accuknox-bluelock/ka-socat-demo:latest",
                    "name": "armored-container",
                    "command": [
                        "/kubearmor/bluelock",
                        "socat",
                        "TCP-LISTEN:1337,reuseaddr,fork",
                        "EXEC:bash,pty,stderr,setsid,sigint,sane"
                    ],
                    "args": [],
                    "env": [
                        {
                            "name": "CONTAINERNAME",
                            "value": "armored-container"
                        },
                        {
                            "name": "CONTAINERIMAGE",
                            "value": "public.ecr.aws/k9v9d5v2/accuknox-bluelock/ka-socat-demo:latest"
                        },
                        {
                            "name": "K8S",
                            "value": "false"
                        }
                    ],
                    "resources": {
                        "cpu": 0.5,
                        "memory": "1Gi"
                    },
                    "probes": [],
                    "volumeMounts": [
                        {
                            "volumeName": "kubearmor-dir",
                            "mountPath": "/kubearmor"
                        }
                    ]
                },
                {
                    "image": "docker.io/accuknox/vm-adapter:v0.1.29",
                    "name": "kubearmor-vm-adapter",
                    "command": [],
                    "args": [
                        "--kubearmor-addr=localhost:32767",
                        "--relay-server-addr=<CONTROL_PLANE_IP>:32768",
                        "--node-state-refresh=4",
                        "--policy-list-enable=true",
                        "--policy-list-relay-frequency=5m0s",
                        "--sia-addr=<CONTROL_PLANE_IP>:32769",
                        "--pea-addr=<CONTROL_PLANE_IP>:32770",
                        "--harden-addr=<CONTROL_PLANE_IP>:32771",
                        "--annotation-topic=annotation",
                        "--annotation-enable=true"
                    ],
                    "env": [
                        {
                            "name": "test",
                            "value": "true"
                        }
                    ],
                    "resources": {
                        "cpu": 0.5,
                        "memory": "1Gi"
                    },
                    "probes": [],
                    "volumeMounts": [
                        {
                            "volumeName": "opt-storage",
                            "mountPath": "/opt"
                        }
                    ]
                }
            ],
            "initContainers": [
                {
                    "image": "public.ecr.aws/k9v9d5v2/accuknox-bluelock:v1.0.0",
                    "name": "bluelock",
                    "resources": {
                        "cpu": 0.25,
                        "memory": "0.5Gi"
                    },
                    "volumeMounts": [
                        {
                            "volumeName": "kubearmor-dir",
                            "mountPath": "/kubearmor"
                        }
                    ]
                }
            ],
            "scale": {
                "minReplicas": 2,
                "maxReplicas": 2,
                "cooldownPeriod": 300,
                "pollingInterval": 30
            },
            "volumes": [
                {
                    "name": "kubearmor-dir",
                    "storageType": "EmptyDir"
                },
                {
                    "name": "opt-storage",
                    "storageType": "EmptyDir"
                }
            ]
        }
        ```

    3. Save and deploy this revision.
    4. After the deployment finishes, open Log stream in the left panel. It shows the logs of both the `armored-container` and the `kubearmor-vm-adapter`. Check that neither shows errors.

        ![The Azure Log stream page for the kubearmor-vm-adapter container, showing connections to the relay server and no errors](images/bluelock-azure-container-apps/log-stream.png)

## Step 5. Confirm the Nodes Appear in AccuKnox

Open the cluster in AccuKnox. The container app replicas appear as nodes next to the control plane VM.

![The AccuKnox cluster panel for the Azure Container Apps cluster, showing the control plane VM and two container app replicas as nodes](images/bluelock-azure-container-apps/saas-cluster-nodes.png)

## Step 6. Test Enforcement With a Block Policy

1. Open the container app in the Azure portal and copy its application URL. The URL has the form `<container-app-name>.<hostname>.<region>.azurecontainerapps.io`.

2. Connect to the container app.

    ```bash
    socat - TCP:<address>:1337
    ```

    !!! note "You cannot choose the replica"
        The container app has one URL, and Azure's internal load balancing picks the replica. You cannot choose which of the replicas you reach.

3. Run the following command. It succeeds, because no policy exists yet.

    ```bash
    ls /etc/ssl/certs
    ```

    ![A terminal session that lists the files in /etc/ssl/certs on the container app](images/bluelock-azure-container-apps/socat-ls-allowed.png)

4. In the AccuKnox console, open Runtime Protection, then Policies, and create the following policy. The file [`ksp-block-file-dir-recursive.yaml`](https://raw.githubusercontent.com/accuknox/bluelock/refs/heads/master/terraform/ksp-block-file-dir-recursive.yaml) in the BlueLock repository holds the same rules. Activate the policy after you save it.

    ```yaml
    apiVersion: security.kubearmor.com/v1
    kind: KubeArmorPolicy
    metadata:
      name: bluelock-test-policy
      namespace: container_namespace
    spec:
      action: Block
      file:
        matchDirectories:
        - dir: /etc/ssl/
          recursive: true
        - dir: /etc/pki/
          recursive: true
        - dir: /usr/local/share/ca-certificates/
          recursive: true
      message: Credentials modification denied
      selector:
        matchLabels:
          kubearmor.io/container.name: armored-container
      severity: 1
      tags:
      - MITRE
      - MITRE_T1552_unsecured_credentials
    ```

5. Run the command again to violate the policy. It now fails.

    ```bash
    ls /etc/ssl/certs
    ```

    ![A terminal session where ls /etc/ssl/certs returns Permission denied on the container app](images/bluelock-azure-container-apps/socat-ls-denied.png)

6. Open the alert in AccuKnox. The alert records the blocked `ls` call against `/etc/ssl/certs`.

    ![The AccuKnox alert Credentials modification denied with action Block and result Permission Denied](images/bluelock-azure-container-apps/alert-credentials-denied.png)

## What This Test Proves

- A policy you apply in AccuKnox reaches the container app replicas.
- BlueLock enforces the policy and raises an alert in AccuKnox.

## Step 7. Destroy the Test Environment When You Finish

Destroy the container app first, then the base infrastructure. Both folders need the same variables that you passed to `terraform apply`.

```bash
cd bluelock/terraform/azure-container-apps/2-app
terraform destroy \
    -var="vm_public_ip=$(cd ../1-infra && terraform output -raw vm_public_ip)"
cd ../1-infra
terraform destroy -var="vm_token=YOUR_JOIN_TOKEN"
```
