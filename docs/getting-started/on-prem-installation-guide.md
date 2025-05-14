---
title: On-prem Deployment Guide
description: Step-by-step instructions for deploying AccuKnox's on-prem security solution, providing enhanced data privacy and control.
---

# AccuKnox OnPrem Deployment Guide
## Onboarding Steps for AccuKnox

The onboarding process for AccuKnox's on-prem security solution consists of four key steps that the user must complete. Let's go through each step in a thorough, step-by-step manner:

![on-prem](images/on-prem/user_journey.png)

### **Step 1: Hardware & Prerequisites**

- Verify hardware, email user, and domain configurations.
- Ensure your environment meets all requirements.
- Time estimate: **Varies**, allocate sufficient time for review and adjustments.

### **Step 2: Staging AccuKnox Container Images** *(For airgapped environments only)*

- Stage AccuKnox container images in the airgapped setup.
- Reconfirm hardware, email user, and domain requirements.
- Time estimate: **~1 hour**.

### **Step 3: Installation**

- Install the AccuKnox system within your environment.
- Ensure all prerequisites remain satisfied.
- Time estimate: **~45 minutes**.

### **Step 4: Verification/Validation**

- Confirm all previous steps were completed successfully.
- Validate hardware, email user, and domain configurations.
- Time estimate: **~1 hour**.

AccuKnox onprem deployment is based on Kubernetes native architecture.

## High-Level Architecture Overview

![](./images/on-prem/3.png)

AccuKnox onprem deployment is based on Kubernetes native architecture.

### AccuKnox OnPrem k8s components

#### Microservices

Microservices implement the API logic and provide the corresponding service endpoints. AccuKnox uses Golang-based microservices for handling streaming data (such as alerts and telemetry) and Python-based microservices for other control-plane services.

#### Databases

PostgreSQL is used as a relational database and MongoDB is used for storing JSON events such as alerts and telemetry. Ceph storage is used to keep periodic scanned reports and the Ceph storage is deployed and managed using the Rook storage operator.

#### Secrets Management

Within the on-prem setup, there are several cases where sensitive data and credentials have to be stored. Hashicorp's Vault is used to store internal (such as DB username/password) and user secrets (such as registry tokens). The authorization is managed purely using the k8s native model of service accounts. Every microservice has its service account and uses its service account token automounted by k8s to authenticate and subsequently authorize access to the secrets.

#### Scaling

K8s native horizontal and vertical pod autoscaling is enabled for most microservices with upper limits for resource requirements.

#### AccuKnox-Agents

Agents need to be deployed in target k8s clusters and virtual machines that have to be secured at runtime and to get workload forensics. Agents use Linux native technologies such as eBPF for workload telemetry and LSMs (Linux Security Modules) for preventing attacks/unknown execution in the target workloads. The security policies are orchestrated from the AccuKnox onprem control plane. AccuKnox leverages SPIFFE/SPIRE for workload/node attestation and certificate provisioning. This ensures that the credentials are not hardcoded and automatically rotated. This also ensures that if the cluster/virtual machine has to be deboarded then the control lies with the AccuKnox control plane.

## System Requirements

### Worker Node Requirements

| Nodes | vCPUs | RAM (GB) | Disk (GB) |
| ----- | ----- | -------- | --------- |
| 6     | 4     | 16       | 256       |

### Kubernetes Requirements

- **Ingress Controller (load balancers)**
    - For access to the application

- **Persistent Volumes (PV), provisioner/controller (block device/disks)**
    - Used as data storage for SQL, MongoDB, scanned artifacts
    - Other internal app usages

- **DNS CNAME provisioning**
    - Needed for application access & communication
    - Certs would use this CNAME so that address changes won't impact the cert validation

- **Email account configuration**
    - Need email username, and password
    - Used for user sign-in, password change, scan notification, sending reports

### Jump Host

![](./images/on-prem/2.png)

### Jump Host Pre-requisites

| Tool                                  | Version                       | Install Command                                                                                                                                                                                              |
|---------------------------------------|-------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| jq                                    | 1.6                           | `apt install jq`                                                                                                                                                                                             |
| unzip                                 | x.x                           | `apt install unzip`                                                                                                                                                                                          |
| [yq](https://github.com/mikefarah/yq) | v4.40.x                       | `VERSION=v4.40.5 && BINARY=yq_linux_amd64 && wget https://github.com/mikefarah/yq/releases/download/${VERSION}/${BINARY}.tar.gz -O - | tar xz && mv ${BINARY} /usr/bin/yq`                    |
| helm                                  | v3.x.x                        | `curl -s https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash`                                                                                                                           |
| kubectl                               | Supported by your k8s cluster | -                                                                                                                                                                                                            |
| aws                                   | v2                            | `curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && unzip awscliv2.zip && sudo ./aws/install --bin-dir /usr/local/bin --install-dir /usr/local/aws-cli --update`            |
| docker                                | v20.xx                        | `apt install docker.io`                                                                                                                                                                                      |
| Storage                               | 80GB                          | -                                                                                                                                                                                                            |


## Installation Steps

### Installation Package

- Onprem Deployment Installation Document (this document)

- Helm charts archive <accuknox-helm-charts.tgz>

- Kubectl and Helm tools are pre-requisite tools for using these helm charts

## Use the following commands

```sh
tar xvf accuknox-helm-charts.tgz
cd Helm-charts
```

## Use of Private/Local Container Registry (or air-gapped mode)

If you want to use your private/local registry as the exclusive source of images for the entire cluster, please install the accuknox-onprem-mgr component first.

| Value               | Description                                                                                       | Provider |
| ------------------- | ------------------------------------------------------------------------------------------------- | -------- |
| `registry.username` | Registry User                                                                                     | Customer |
| `registry.password` | Registry Password                                                                                 | Customer |
| `registry.address`  | The registry server address                                                                       | Customer |
| `ecr.user`          | Credential to pull images from AccuKnox registry                                                  | AccuKnox |
| `ecr.password`      | Credential to pull images from AccuKnox registry                                                  | AccuKnox |

```sh
cd airgapped-reg

# configure aws cli with AccuKnox  provided secrets
aws configure

# connect to docker Accuknox docker registry
aws ecr get-login-password --region us-east-2 | docker login --username AWS --password-stdin 956994857092.dkr.ecr.us-east-2.amazonaws.com

# connect to airgapped registry
docker login <registry_address>

# upload images to private registry
./upload_images.sh <registry_address>
./upload_onboarding_images.sh <registry.address>

# upload helm charts to private registry
./upload_helm.sh <registry.address>

# create a namespace
MGR_NS="accuknox-onprem-mgr"
CERT_MGR_NS="cert-manager"
kubectl create ns $MGR_NS
kubectl create ns $CERT_MGR_NS

kubectl create secret docker-registry airgapped-reg     --docker-server=<registry.address> --docker-username=<registry.username> --docker-password=<registry.password> -n $MGR_NS

kubectl create secret docker-registry airgapped-reg --docker-server=<registry.address> --docker-username=<registry.username> --docker-password=<registry.password> -n $CERT_MGR_NS

# <registry_address> can include port as well

./install-certmanager.sh <registry_address>

./install-onprem-mgr.sh <registry_address>

kubectl apply -k .
kubectl apply -f onprem-mgr.yaml

```

## Update the override-values.yaml

[ONLY FOR air-gapped/private registry ENVIRONMENT]: Set global.onprem.airgapped to true in override-values.yaml file.

### Before you start

- set your domain name in the override values by changing <your_domain.com> by your domain

- set your ssl preferences in the override values by changing the ssl block

- If you wish to bring in your own MongoDB, PostgreSQL, NFS share or S3, disable global.postgres.airgapped and global.mongodb.enabled rookceph.enabled in override-values.yaml.

#### If the environment is OpenShift then set:

```yaml
global:
  platform: "openshift"`
```

#### If environment is airgapped or using private registry make ssl.certmanager.install:"false"

```yaml
ssl:
  certmanager:
    install: false
```

#### Auto-generated self-signed certificate

We auto generate the needed self signed certificates for the client. To enabled this option, the ssl section the override values file should be set as follow:

```yaml
ssl:
  selfsigned: true
  customcerts: false
```

#### Certificate signed by a known authority

The client provides a certificate signed by a known signing authority To enable this option, the ssl section the override values file should be set as follow:

```yaml
ssl:
  selfsigned: false
  customcerts: true
```

#### Self-signed certificates (provided by the customer)

The client provides a self signed certificate. To enabled this option, the ssl section the override values file should be set as follow:

```yaml
ssl:
  selfsigned: true
  customcerts: true
```

AccuKnox installation package will contain override-values.yaml file that contains installation-specific options to be configured.

1.  override <your_domain.com> to your domain

2.  set your ssl preferences in the override values by changing the ssl block.

## Install AccuKnox base dependencies

```sh
kubectl create namespace accuknox-chart
helm upgrade --install -n accuknox-chart accuknox-base accuknox-base-chart  --create-namespace -f override-values.yaml
```

!!! note "IMPORTANT"
    Some resources d eployed in the above step require some time to provision. If the user executes the next command without waiting for the proper provisioning of the previous command the installation may break and will need to start over.

Run the below script to make sure that the provisioning was done succesfully.

```sh
while true
do
    status=$(kubectl get cephcluster -n accuknox-ceph  rook-ceph -o=jsonpath='{.status.phase}')
    [[$(echo $status | grep -v Ready | wc -l) -eq 0]] && echo "You can proceed" && break
 echo "wait for initialization"
    sleep 1
done
```

## Install AccuKnox pre-chart

!!! note "IMPORTANT"
    Contact your AccuKnox representative to acquire the credentials for `ecr.user` and `ecr.password` values.

| Value                                         | Description                                                                               | Provider |
| --------------------------------------------- | ----------------------------------------------------------------------------------------- | -------- |
| **email.user**                                | Email user will send signup invites, reports, etc.                                        | Customer |
| **email.password**                            | Email Password                                                                            | Customer |
| **email.host**                                | The Email server address                                                                  | Customer |
| **email.from**                                | The Email sender address (noreply@domain.com)                                             | Customer |
| **ecr.user**                                  | Credential to pull images from AccuKnox registry                                          | AccuKnox |
| **ecr.password**                              | Credential to pull images from AccuKnox registry                                          | AccuKnox |
| **global.externalServices.postgres.user**     | Postgres username, if using an external DB                                                | Customer |
| **global.externalServices.postgres.password** | Postgres password, if using an external DB                                                | Customer |
| **global.externalServices.postgres.host**     | Postgres host, if using an external DB                                                    | Customer |
| **global.externalServices.mongo.user**        | Mongodb username, if using an external DB                                                 | Customer |
| **global.externalServices.mongo.password**    | Mongodb password, if using an external DB                                                 | Customer |
| **global.externalServices.mongo.host**        | Mongodb host, if using an external DB                                                     | Customer |
| **global.externalServices.nfs.server**        | NFS server address                                                                        | Customer |
| **global.externalServices.s3.host**           | S3 datastore host                                                                         | Customer |
| **global.externalServices.s3.port**           | S3 datastore port                                                                         | Customer |
| **global.externalServices.s3.accessKey**      | S3 access key                                                                             | Customer |
| **global.externalServices.s3.secretKey**      | S3 secret access key                                                                      | Customer |
| **global.externalServices.s3.bucket**         | S3 bucket name                                                                            | Customer |

```sh
helm upgrade  --install  -n  accuknox-chart accuknox-pre pre-chart  --create-namespace -f override-values.yaml --set global.email.from="" --set global.email.user="" --set global.email.password="" --set global.email.host="" --set ecr.user="*****\*\***" --set ecr.password="****/**\*\*\***"
```

Or, if using an external PostgreSQL or Mongo DB,

```sh
helm upgrade accuknox-pre pre-chart \
    --install \
    -namespace accuknox-chart \
    --create-namespace \
    -values override-values.yaml \
    --set global.email.user="" \
    --set global.email.password="" \
    --set global.email.host="" \
    --set ecr.user="" \
    --set ecr.password="" \
    --set global.externalServices.postgres.user="" \
    --set global.externalServices.postgres.password="" \
    --set global.externalServices.postgres.host="" \
    --set global.externalServices.mongo.user="" \
    --set global.externalServices.mongo.password="" \
    --set global.externalServices.mongo.host=""
```

## Install AccuKnox microservices chart

| Value              | Description                                         | Provider |
| ------------------ | --------------------------------------------------- | -------- |
| **email.user**     | Email user will send signup invites, reports, etc.  | Customer |
| **email.password** | Email Password                                      | Customer |
| **email.host**     | The Email server address                            | Customer |
| **email.from**     | The Email sender address (e.g., noreply@domain.com) | Customer |

```sh
helm  upgrade  --install  -n  accuknox-chart  accuknox-microservice  accuknox-microservice-chart  --set global.email.user="" --set global.email.from="" --set global.email.password="" --set global.email.host="" --create-namespace -f  override-values.yaml
```

### DNS Mapping

Run the following script to generate the records you should add to your DNS zone.

```cmd
./generate_dns_entries.sh

```

### Installing certificates

#### Certificates signed by known authority

```cmd
./install_certs.sh <certificate_path> <certificate_key_path> <ca_path>
```

#### Self-signed certificates (provided by customer)

## Install nginx ingress (if any other self-managed Kubernetes)

1.  Install the nginx ingress chart

```sh
cd airgapped-reg/addons
```

```sh
helm upgrade --install ingress-nginx ingress-nginx \
      --repo https://kubernetes.github.io/ingress-nginx \
      --namespace ingress-nginx --create-namespace \
      --version 4.11.2 -f ingress-nginx.yaml
```

2.  Update the domains in ingress.yaml and apply it

```sh
kubectl apply -f ingress.yaml
```

## Verification of installation

After successful installation, you should be able to access the following URLs:

- [https://frontend.your-domain.com](https://frontend.your-domain.com) — Access the **Sign-in page**.
- [https://cspm.your-domain.com/admin/](https://cspm.your-domain.com/admin/) — Access the **CSPM Admin page**.
- [https://cwpp.your-domain.com/cm/](https://cwpp.your-domain.com/cm/) — Access the **CWPP Configuration Management page**.


![](./images/on-prem/4.png)

# References

1.  AccuKnox Deployment and Operations [FAQs](https://help.accuknox.com/faqs/troubleshooting-and-faqs/)
2.  [AccuKnox Splunk Integration Guide](https://help.accuknox.com/integrations/splunk/)
3.  [KubeArmor Splunk Integration Guide](https://help.accuknox.com/integrations/splunk_feeder_kubearmor/)
4.  [CSPM: Use-cases & Scenarios](https://help.accuknox.com/use-cases/vulnerability/)
5.  [CWPP: Use-cases & Scenarios](https://help.accuknox.com/use-cases/app-behavior/)
6.  [Detailed Support Matrix](https://help.accuknox.com/getting-started/kubearmor-support-matrix/)
