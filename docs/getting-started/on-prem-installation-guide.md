# On-prem Deployment Guide

## High-Level Architecture Overview

![on-prem](images/on-prem/image8.png)

AccuKnox onprem deployment is based on Kubernetes native architecture.

## AccuKnox OnPrem k8s components

### Microservices

Microservices implement the API logic and provide the corresponding service endpoints. AccuKnox uses Golang-based microservices for handling streaming data (such as alerts and telemetry) and Python-based microservices for other control-plane services.

### Databases

PostgreSQL is used as a relational database and MongoDB is used for storing JSON events such as alerts and telemetry. Ceph storage is used to keep periodic scanned reports and the Ceph storage is deployed and managed using the Rook storage operator.

### Secrets Management

Within the on-prem setup, there are several cases where sensitive data and credentials have to be stored. Hashicorp's Vault is used to store internal (such as DB username/password) and user secrets (such as registry tokens). The authorization is managed purely using the k8s native model of service accounts. Every microservice has its service account and uses its service account token automounted by k8s to authenticate and subsequently authorize access to the secrets.

### Scaling

K8s native horizontal and vertical pod autoscaling is enabled for most microservices with upper limits for resource requirements.

### AccuKnox-Agents

Agents need to be deployed in target k8s clusters and virtual machines that have to be secured at runtime and to get workload forensics. Agents use Linux native technologies such as eBPF for workload telemetry and LSMs (Linux Security Modules) for preventing attacks/unknown execution in the target workloads. The security policies are orchestrated from the AccuKnox onprem control plane. AccuKnox leverages SPIFFE/SPIRE for workload/node attestation and certificate provisioning. This ensures that the credentials are not hardcoded and automatically rotated. This also ensures that if the cluster/virtual machine has to be deboarded then the control lies with the AccuKnox control plane.

## System Requirements

### Worker Node Requirements

| Nodes | vcpus | RAM (GB) | Disk (GB) |
|:-----:|:-----:|:--------:|:---------:|
|   6   |   4   |    16    |    256    |

### Kubernetes Requirements

Start a k8s cluster with the above worker node requirements**

**Ingress Controller (load balancers)**

- For access to the application

**Persistent Volumes (PV), provisioner/controller (block device/disks)**

- Used as data storage for SQL, MongoDB, scanned artifacts
- Other internal app usages

**DNS CNAME provisioning**

- Needed for application access & communication
- Certs would use this CNAME so that address changes won't impact the cert validation.

**Email account configuration**

- Need email username, and password
- Used for user sign-in, password change, scan notification, sending reports

## Jump Host

![on-prem](images/on-prem/image1.png)

### Jump Host Pre-requisites

| Tool    | Version                       | Install command                                                                                                                                                                                   |   |
|---------|-------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| jq      | 1.6                           | apt install jq                                                                                                                                                                                    |   |
| unzip   | x.x                           | apt install unzip                                                                                                                                                                                 |   |
| yq      | v4.40.x                       | VERSION=v4.40.5 && BINARY=yq_linux_amd64 && wget <https://github.com/mikefarah/yq/releases/download/$> {VERSION}/${BINARY}.tar.gz -O - \| tar xz && mv ${BINARY} /usr/bin/yq                        |   |
| helm    | v3.x.x                        | curl <https://raw.githubusercontent.com/helm/helm/ma> in/scripts/get-helm-3 \| bash                                                                                                                 |   |
| kubectl | Supported by your k8s cluster |                                                                                                                                                                                                   |   |
| aws     | v2                            | curl "<https://awscli.amazonaws.com/awscli-exe-linux> -x86_64.zip" -o "awscliv2.zip" && unzip awscliv2.zip && sudo ./aws/install --bin-dir /usr/local/bin --install-dir /usr/local/aws-cli --update |   |
| docker  | v20.xx                        | apt install docker.io                                                                                                                                                                             |   |
| Storage | 80GB                          |                                                                                                                                                                                                   |   |

## Installation Steps

### Installation Package

- Helm charts archive <accuknox-helm-charts.tgz>
- Kubectl and Helm tools are pre-requisite tools for using these helm charts

Use the following command to

![on-prem](images/on-prem/image13.png)

### Use of Private/Local Container Registry (or air-gapped mode)

------------------------------------------------------------

If you want to use your private/local registry as the exclusive source of images for the entire cluster, please install the accuknox-onprem-mgr component first.

| Value             | Description                                                                                      | Provider |
|-------------------|--------------------------------------------------------------------------------------------------|----------|
| registry.username | Registry User                                                                                    | Customer |
| registry.password | Registry Password                                                                                | Customer |
| registry.address  | The registry server address                                                                      | Customer |
| ecr.user          | Credential to pull images from AccuKnox registry Value: AKIA55UKWVCCBZ2YEFIY                     | AccuKnox |
| ecr.password      | Credential to pull images from AccuKnox registry Value: 0c5UL9oHkftDRBfnrQV4Jmic/5eei4agpyxNtAkV | AccuKnox |

![on-prem](images/on-prem/image3.png)

![on-prem](images/on-prem/image14.png)

### Update the override-values.yaml

[ONLY FOR air-gapped/private registry ENVIRONMENT]: Set global.onprem.airgapped to true in override-values.yaml file.

### Before you start

We offer three deployments models when it comes to SSL certificate to accomodate for client requirements.

#### Auto-generated self-signed certificate

We auto generate the needed self signed certificates for the client. To enabled this option, the ssl section the override values file should be set as follow:

![on-prem](images/on-prem/image12.png)

#### Certificate signed by a known authority

The client provides a certificate signed by a known signing authority To enable this option, the ssl section the override values file should be set as follow:

![on-prem](images/on-prem/image9.png)

#### Self-signed certificates (provided by the customer)

The client provides a self signed certificate. To enabled this option, the ssl section the override values file should be set as follow:

![on-prem](images/on-prem/image7.png)

AccuKnox installation package will contain override-values.yaml file that contains installation-specific options to be configured.

1. override <your_domain.com> to your domain
2. set your ssl preferences in the override values by changing the ssl block.

## Install AccuKnox base dependencies

![on-prem](images/on-prem/image16.png)

!!! note "IMPORTANT"
  Some resources deployed in the above step require some time to provision. If the user executes the next command without waiting for the proper provisioning of the previous command the installation may break and will need to start over.
  Run the below script to make sure that the provisioning was done succesfully.

![on-prem](images/on-prem/image2.png)

## Install AccuKnox pre-chart

| Value          | Description                                                                                      | Provider |
|----------------|--------------------------------------------------------------------------------------------------|----------|
| email.user     | Email user will send signup invites, reports etc                                                 | Customer |
| email.password | Email Password                                                                                   | Customer |
| email.host     | The Email server address                                                                         | Customer |
| ecr.user       | Credential to pull images from AccuKnox registry Value: AKIA55UKWVCCBZ2YEFIY                     | AccuKnox |
| ecr.password   | Credential to pull images from AccuKnox registry Value: 0c5UL9oHkftDRBfnrQV4Jmic/5eei4agpyxNtAkV | AccuKnox |

![on-prem](images/on-prem/image4.png)

## Install AccuKnox microservices chart

| Value          | Description                                      | Provider |
|----------------|--------------------------------------------------|----------|
| email.user     | Email user will send signup invites, reports etc | Customer |
| email.password | Email Password                                   | Customer |
| email.host     | The Email server address                         | Customer |

![on-prem](images/on-prem/image6.png)

### DNS Mapping

Run the following script to generate the records you should add to your DNS zone.![on-prem](images/on-prem/image15.png)

### Installing certificates

#### Certificates signed by known authority![on-prem](images/on-prem/image5.png)

#### Self-signed certificates (provided by customer)![on-prem](images/on-prem/image11.png)

## Verification of installation

After successful installation, you should be able to point to

- <https://frontend>.<your-domain.com> URL and get the sign-in page.
- <https://cspm>.<your-domain.com>/admin/ page should be available.
- <https://cwpp>.<your-domain.com>/cm/ page should be available.![on-prem](images/on-prem/image10.jpg)
