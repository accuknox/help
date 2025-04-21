---
title: CWPP Pre-requisites
description: AccuKnox CNAPP will be hosted in our cloud environment and the agents deployed on the workloads will connect with the SaaS.
---

In SaaS model of deployment the AccuKnox CNAPP will be hosted in our cloud environment and the agents deployed on the workloads will connect with the SaaS.

![accuknox-arch](images/accuknox-architecture.png)

## AccuKnox Agents

| Deployments            | Deployment Type |
|------------------------|-----------------|
| KubeArmor              | DaemonSet       |
| Shared Informer Agent  | Deployment      |
| Feeder Service         | Deployment      |
| Policy Enforcement     | Deployment      |
| Discovery Engine Agent | Deployment      |

- It is assumed that the user has some basic familiarity with Kubernetes, kubectl and helm. It also assumes that you are familiar with the AccuKnox opensource tool workflow. If you're new to AccuKnox itself, refer first to [opensource installation](./../getting-started/open-source.md)

- It is recommended to have the following configured before onboarding:

    1. [Kubectl](https://kubernetes.io/docs/tasks/tools/ "https://kubernetes.io/docs/tasks/tools/")
    2. [Helm](https://helm.sh/docs/intro/install/ "https://helm.sh/docs/intro/install/")

## **Pre-requisites**
### Minimum Resource required

| Deployments           | Resource Usage             | Ports | Connection Type  	| AccuKnox Endpoint                               |
|-----------------------|----------------------------|------|-------------------|-------------------------------------------------|
|KubeArmor              | CPU: 200 m, Memory: 200 Mi | -    | -			| -                                               |
|Agents Operator        | CPU: 50 m, Memory: 50 Mi   | 8081,</br> 9090 | Outbound		| *.accuknox.com:8081 -→ SPIRE Access</br> *.accuknox.com:9090 -→ SPIRE Health Check           |
|Discovery Engine       | CPU: 200 m, Memory: 200 Mi | -    | -			| -                                               |
|Shared Informer Agent  | CPU: 20 m, Memory: 50 Mi   | 3000 | Outbound		| *.accuknox.com:3000 -→ knox-gateway            |
|Feeder Service         | CPU: 50 m, Memory: 100 Mi  | 3000 | Outbound		| *.accuknox.com:3000 -→ knox-gateway            |
|Policy Enforcement     | CPU: 10 m, Memory: 20 Mi   | 443  | Outbound		| *.accuknox.com:443  -→ Policy Provider Service |

- These ports need to be allowed through firewall.

- - -
[SCHEDULE DEMO](https://www.accuknox.com/contact-us){ .md-button .md-button--primary }
