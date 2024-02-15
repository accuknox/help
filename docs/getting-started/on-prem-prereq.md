---
hide:
  - toc
---

In on-premise deployment, AccuKnox SaaS Component will be deployed on-premise. With locally deployed SaaS component the Scans will take place and reports will be shown in the dashboard.

![](images/on-prem-saas.png)

For Air-Gapped On-prem installation, the SaaS deployment images will be provided.

# **System Requirements**

### Worker Node Requirements

| Nodes | vCPUs | RAM (GB) | Disk (GB) |
| ----- | ----- | -------- | --------- |
| 4     | 8     | 32       | 256       |
| 5     | 4     | 16       | 128       |

### Kubernetes Requirements

- Start a k8s cluster with the above worker node requirements

- Ingress Controller (load balancers)
    - For access to the application

- Persistent Volumes (PV), provisioner/controller (block device/disks)
    - Used as data storage for SQL, MongoDB, scanned artifacts
    - Other internal app usages

- DNS CNAME provisioning
    - Needed for application access & communication
    - Certs would use this CNAME so that address changes won’t impact the cert validation.

- Email account configuration
    - Need email username, password
    - Used for user sign-in, password change, scan notification, sending reports

### Pre-requisites

You need to have the following tools installed in the machine that you are going to use to follow the installation guide

| Tool                                  | Version                       | Install command                                                                                                                                                                                  |
| ------------------------------------- | ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| jq                                    | 1.6                           | apt install jq                                                                                                                                                                                   |
| unzip                                 | x.x                           | apt install unzip                                                                                                                                                                                |
| [yq](https://github.com/mikefarah/yq) | v4.40.x                       | VERSION=v4.40.5 && BINARY=yq_linux_amd64 && wget https://github.com/mikefarah/yq/releases/download/\${VERSION}/\${BINARY}.tar.gz -O - \| tar xz && mv \${BINARY} /usr/bin/yq                        |
| helm                                  | v3.x.x                        | curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 \| bash                                                                                                                  |
| kubectl                               | Supported by your k8s cluster |                                                                                                                                                                                                  |
| aws                                   | v2                            | curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && unzip awscliv2.zip && sudo ./aws/install --bin-dir /usr/local/bin --install-dir /usr/local/aws-cli --update |
| docker                                | v20.xx                        | apt install docker.io                                                                                                                                                                            |

Also the machine needs to have at least 80GB of storage


- - - 
[SCHEDULE DEMO](https://www.accuknox.com/contact-us){ .md-button .md-button--primary }