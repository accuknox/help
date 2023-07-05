---
hide:
  - toc
---

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


1.  [Kubectl](https://kubernetes.io/docs/tasks/tools/ "https://kubernetes.io/docs/tasks/tools/")
2.  [Helm](https://helm.sh/docs/intro/install/ "https://helm.sh/docs/intro/install/")
 
## **Pre-requisites**
### Minimum Resource required

| Deployments   | Resource usage   | Port | Connection Type |
|---|---|---|---|
|KubeArmor    |  CPU: 200 m, Memory: 200 Mi | - | - |
|Agents Operator | CPU: 50 m, Memory: 50 Mi | 8081 | Inbound/Outbound |
|Discovery Engine  | CPU: 100 m, Memory: 100 Mi | - | - |
|Shared Informer Agent  | CPU: 20 m, Memory: 50 Mi | 3000 | Inbound/Outbound |
|Feeder Service   | CPU: 50 m, Memory: 100 Mi  | 3000 | Inbound/Outbound |
|Policy Enforcement   |  CPU: 10 m, Memory: 20 Mi | 443 | Inbound/Outbound |

- These ports needs to be allowed through firewall.

- - - 
[SCHEDULE DEMO](https://www.accuknox.com/contact-us){ .md-button .md-button--primary }