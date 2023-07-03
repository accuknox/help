---
hide:
  - toc
---

Accuknox CNAPP Solution provides comprehensive visibility of the cloud assets with the help of Dashboards and logs/alerts. AccuKnox’s open-source KubeArmor can forward policy-related logs/alerts to the SaaS. Also, it can forward the container logs that are present in the workloads. We can also use the Feeder service agent to pass the logs to other SIEM tools like Splunk, ELK, Rsyslog, etc.., User can also forward the logs from AccuKnox SaaS using the channel integration option to these SIEM tools.

## Logs

### Logs Format:

| Log field              | Description                                                               | Example                                                                                                       |
|------------------------|---------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| ClusterName            | gives information about the cluster for which the log was generated       | default                                                                                                       |
| Operation              | gives details about what type of operation happened in the pod            | File/Process/ Network                                                                                         |
| ContainerID            | information about the container ID from where log was generated           | 7aca8d52d35ab7872df6a454ca32339386be                                                                          |
| ContainerImage         | shows the image that was used to spin up the container                    | docker.io/accuknox/knoxautopolicy:v0.9@sha256:bb83b5c6d41e0d0aa3b5d6621188c284ea                              |
| ContainerName          | specifies the Container name where the log got generated                  | discovery-engine                                                                                              |
| Data                   | shows the system call that was invoked for this operation                 | syscall=SYS_OPENAT fd=-100 flags=O_RDWR\|O_CREAT\|O_NOFOLLOW\|O_CLOEXEC                                       |
| HostName               | shows the node name where the log got generated                           | aks-agentpool-16128849-vmss000001                                                                             |
| HostPID                | gives the host Process ID                                                 | 967872                                                                                                        |
| HostPPID               | list the details of host Parent Process ID                                | 967496                                                                                                        |
| Labels                 | shows the pod label from where log generated                              | app=discovery-engine                                                                                          |
| Message                | gives the message specified in the policy                                 | Alert! Execution of package management process inside container is denied                                     |
| NamespaceName          | lists the namespace where pod is running                                  | accuknox-agents                                                                                               |
| PID                    | lists the process ID running in container                                 | 1                                                                                                             |
| PPID                   | lists the Parent process ID running in container                          | 967496                                                                                                        |
| ParentProcessName      | gives the parent process name from where the operation happend            | /usr/bin/containerd-shim-runc-v2                                                                              |
| PodName                | lists the pod name where the log got generated                            | mysql-76ddc6ddc4-h47hv                                                                                        |
| ProcessName            | specifies the operation that happened inside the pod for this log         | /knoxAutoPolicy                                                                                               |
| Resource               | lists the resources that was requested                                    | //accuknox-obs.db                                                                                             |
| Result                 | shows whether the event was allowed or denied                             | Passed                                                                                                        |
| Source                 | lists the source from where the operation request came                    | /knoxAutoPolicy                                                                                               |
| Type                   | specifies it as container log                                             | ContainerLog                                                                                                  |

### Sample Container Log:

```
ClusterName: default
HostName: aks-agentpool-16128849-vmss000000
NamespaceName: accuknox-agents
PodName: discovery-engine-6f5c4df7b4-q8zbc
Labels: app=discovery-engine
ContainerName: discovery-engine
ContainerID: 7aca8d52d35ab7872df6a454ca32339386be755d9ed6bd6bf7b37ec6aaf277e4
ContainerImage: docker.io/accuknox/knoxautopolicy:v0.9@sha256:bb83b5c6d41e0d0aa3b5d6621188c284ea99741c3692e34b0f089b0e74745413
Type: ContainerLog
Source: /knoxAutoPolicy
Resource: //accuknox-obs.db
Operation: File
Data: syscall=SYS_OPENAT fd=-100 flags=O_RDWR|O_CREAT|O_NOFOLLOW|O_CLOEXEC
Result: Passed
HostPID: 967872
HostPPID: 967496
PID: 1
PPID: 967496
ParentProcessName: /usr/bin/containerd-shim-runc-v2
ProcessName: /knoxAutoPolicy
```

## Alerts

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