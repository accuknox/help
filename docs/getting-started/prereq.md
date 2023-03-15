---
hide:
  - toc
---

## Accuknox Agents

| Deployments            | Deployment Type | 
|------------------------|-----------------|
| KubeArmor              | DaemonSet       | 
| Shared Informer Agent  | Deployment      | 
| Feeder Service         | Deployment      | 
| Policy Enforcement     | Deployment      |  
| Discovery Engine Agent | Deployment      |  

- It is assumed that the user has some basic familiarity with Kubernetes, kubectl and helm. It also assumes that you are familiar with the AccuKnox opensource tool workflow. If you're new to AccuKnox itself, refer first to [opensource installation](./../getting-started/open-source.md)

- It is recommended to have the following configured before onboarding:


1.  [Kubectl](https://kubernetes.io/docs/tasks/tools/ "https://kubernetes.io/docs/tasks/tools/")
2.  [Helm](https://helm.sh/docs/intro/install/ "https://helm.sh/docs/intro/install/")
 
## **Pre-requisites**
### Minimum Resource required

A Kubernetes cluster with

> -   Number of Nodes : 3
> -   Machine Type: e2-standard-2    
> -   Total vCPUs : 6
> -   Total Memory: 24GB

| Deployments   | Resource usage   |
|---|---|
|KubeArmor    |  CPU: 200 m, Memory: 200 Mi |
|Agents Operator | CPU: 50 m, Memory: 50 Mi |
|Discovery Engine  | CPU: 100 m, Memory: 100 Mi |
|Shared Informer Agent  | CPU: 20 m, Memory: 50 Mi |
|Feeder Service   | CPU: 50 m, Memory: 100 Mi  |
|Policy Enforcement   |  CPU: 10 m, Memory: 20 Mi |

| Ports         | Description                                                                  |
|---------------|------------------------------------------------------------------------------|
| 9093, 443, 80 | The worker cluster will communicate with accuknox SaaS and general internet  |