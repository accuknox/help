---
hide:
  - toc
---

Rich contextual alerts are provided by Accuknox CNAPP to give comprehensive visibility of the cloud assets along with a dashboard view. Policy related alerts can be forwarded from Accuknox's open-source KubeArmor to the SaaS platform. User can also forward the alerts from AccuKnox SaaS using the channel integration option to other SIEM tools like Splunk, ELK, Rsyslog, etc.., These alerts can also help accelerate troubleshooting by providing a single source of truth.

### Alerts Format:

| Alert Field            | Description                                                                          | Example                                                                                              |
|------------------------|--------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| Action                 | specifies the action of the policy it has matched.                                   | Audit/Block                                                                                          |
| ClusterName            | gives information about the cluster for which the alert was generated                | aks-test-cluster                                                                                     |
| Operation              | gives details about what type of operation happened in the pod                       | File/Process/Network                                                                                 |
| ContainerID            | information about the container ID where the policy violation or alert got generated | e10d5edb62ac2daa4eb9a2146e2f2cfa87b6a5f30bd3a                                                        |
| ContainerImage         | shows the image that was used to spin up the container                               | docker.io/library/mysql:5.6@sha256:20575ecebe6216036d25dab5903808211f                                |
| ContainerName          | specifies the Container name where the alert got generated                           | mysql                                                                                                |
| Data                   | shows the system call that was invoked for this operation                            | syscall=SYS_EXECVE                                                                                   |
| Enforcer               | it specifies the name of the LSM that has enforced the policy                        | AppArmor/BPFLSM                                                                                      |
| HostName               | shows the node name where the alert got generated                                    | aks-agentpool-16128849-vmss000001                                                                    |
| HostPID                | gives the host Process ID                                                            | 3647533                                                                                              |
| HostPPID               | list the details of host Parent Process ID                                           | 3642706                                                                                              |
| Labels                 | shows the pod label from where alert generated                                       | app=mysql                                                                                            |
| Message                | gives the message specified in the policy                                            | Alert! Execution of package management process inside container is denied                            |
| NamespaceName          | lists the namespace where pod is running                                             | wordpress-mysql                                                                                      |
| PID                    | lists the process ID running in container                                            | 266                                                                                                  |
| PPID                   | lists the Parent process ID running in container                                     | 251                                                                                                  |
| ParentProcessName      | gives the parent process name from where the operation happend                       | /bin/bash                                                                                            |
| PodName                | lists the pod name where the alert got generated                                     | mysql-76ddc6ddc4-h47hv                                                                               |
| PolicyName             | gives the policy that was matched for this alert generation                          | harden-mysql-pkg-mngr-exec                                                                           |
| ProcessName            | specifies the operation that happened inside the pod for this alert                  | /usr/bin/apt                                                                                         |
| Resource               | lists the resources that was requested                                               | /usr/bin/apt                                                                                         |
| Result                 | shows whether the event was allowed or denied                                        | Permission denied                                                                                    |
| Severity               | gives the severity level of the operation                                            | 5                                                                                                    |
| Source                 | lists the source from where the operation request came                               | /bin/bash                                                                                            |
| Tags                   | specifies the list of benchmarks this policy satisfies                               | NIST,NIST_800-53_CM-7(4),SI-4,process,NIST_800-53_SI-4                                               |
| Timestamp              | gives the details of the time this event tried to happen                             | 1687868507                                                                                           |
| Type                   | shows whether policy matched or default posture alert                                | MatchedPolicy                                                                                        |
| UpdatedTime            | gives the time of this alert                                                         | 2023-06-27T12:21:47.932526                                                                           |
| cluster_id             | specifies the cluster id where the alert was generated                               | 596                                                                                                  |
| component_name         | gives the component which generated this log/alert                                   | kubearmor                                                                                            |
| tenant_id              | specifies the tenant id where this cluster is onboarded in AccuKnox SaaS             | 11                                                                                                   |

### Sample Alert:

```
Action:Block
ClusterName:aks-demo-prod
ContainerID:e10d5edb62ac2daa4eb9a2146e2f2cfa87b6a5f30bd3ae20fc91a2bf4d727747
ContainerImage:docker.io/library/mysql:5.6@sha256:20575ecebe6216036d25dab5903808211f1e9ba63dc7825ac20cb975e34cfcae
ContainerName:mysql
Data:syscall=SYS_EXECVE
Enforcer:AppArmor
HostName:aks-agentpool-16128849-vmss000001
HostPID:3647533
HostPPID:3642706
Labels:app=mysql
Message:Alert! Execution of package management process inside container is denied
NamespaceName:wordpress-mysql
Operation:Process
PID:266
PPID:251
ParentProcessName:/bin/bash
PodName:mysql-76ddc6ddc4-h47hv
PolicyName:harden-mysql-pkg-mngr-exec
ProcessName:/usr/bin/apt
Resource:/usr/bin/apt
Result:Permission denied
Severity:5
Source:/bin/bash
Tags:NIST,NIST_800-53_CM-7(4),SI-4,process,NIST_800-53_SI-4
Timestamp:1687868507
Type:MatchedPolicy
UpdatedTime:2023-06-27T12:21:47.932526Z
cluster_id:596
component_name:kubearmor
instanceGroup:0
instanceID:0
tenant_id:11
workload:1
```