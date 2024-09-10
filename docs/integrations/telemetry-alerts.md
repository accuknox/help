

Rich contextual alerts are provided by AccuKnox CNAPP to give comprehensive visibility of the cloud assets along with a dashboard view. Policy related alerts can be forwarded from Accuknox's open-source KubeArmor to the SaaS platform. User can also forward the alerts from AccuKnox SaaS using the channel integration option to other SIEM tools like Splunk, ELK, Rsyslog, etc.., These alerts can also help accelerate troubleshooting by providing a single source of truth.

**Process Alert**
```
{
  "ClusterName": "default",
  "HostName": "aks-agentpool-16128849-vmss000001",
  "NamespaceName": "wordpress-mysql",
  "PodName": "wordpress-787f45786f-2q9wf",
  "Labels": "app=wordpress",
  "ContainerID": "72de193fc8d849cd052affae5a53a27111bcefb75385635dcb374acdf31a5548",
  "ContainerName": "wordpress",
  "ContainerImage": "docker.io/library/wordpress:4.8-apache@sha256:6216f64ab88fc51d311e38c7f69ca3f9aaba621492b4f1fa93ddf63093768845",
  "HostPPID": 495804,
  "HostPID": 495877,
  "PPID": 309835,
  "PID": 309841,
  "ParentProcessName": "/bin/bash",
  "ProcessName": "/usr/bin/apt",
  "PolicyName": "harden-wordpress-pkg-mngr-exec",
  "Severity": "5",
  "Tags": "NIST,NIST_800-53_CM-7(4),SI-4,process,NIST_800-53_SI-4",
  "ATags": [
    "NIST",
    "NIST_800-53_CM-7(4)",
    "SI-4",
    "process",
    "NIST_800-53_SI-4"
  ],
  "Message": "Alert! Execution of package management process inside container is denied",
  "Type": "MatchedPolicy",
  "Source": "/bin/bash",
  "Operation": "Process",
  "Resource": "/usr/bin/apt",
  "Data": "syscall=SYS_EXECVE",
  "Enforcer": "AppArmor",
  "Action": "Block",
  "Result": "Permission denied"
}
```
**File Alert**
```
{
  "ClusterName": "default",
  "HostName": "aks-agentpool-16128849-vmss000001",
  "NamespaceName": "wordpress-mysql",
  "PodName": "wordpress-787f45786f-2q9wf",
  "Labels": "app=wordpress",
  "ContainerID": "72de193fc8d849cd052affae5a53a27111bcefb75385635dcb374acdf31a5548",
  "ContainerName": "wordpress",
  "ContainerImage": "docker.io/library/wordpress:4.8-apache@sha256:6216f64ab88fc51d311e38c7f69ca3f9aaba621492b4f1fa93ddf63093768845",
  "HostPPID": 495804,
  "HostPID": 496390,
  "PPID": 309835,
  "PID": 309842,
  "ParentProcessName": "/bin/bash",
  "ProcessName": "/bin/rm",
  "PolicyName": "harden-wordpress-file-integrity-monitoring",
  "Severity": "1",
  "Tags": "NIST,NIST_800-53_AU-2,NIST_800-53_SI-4,MITRE,MITRE_T1036_masquerading,MITRE_T1565_data_manipulation",
  "ATags": [
    "NIST",
    "NIST_800-53_AU-2",
    "NIST_800-53_SI-4",
    "MITRE",
    "MITRE_T1036_masquerading",
    "MITRE_T1565_data_manipulation"
  ],
  "Message": "Detected and prevented compromise to File integrity",
  "Type": "MatchedPolicy",
  "Source": "/bin/rm /sbin/raw",
  "Operation": "File",
  "Resource": "/sbin/raw",
  "Data": "syscall=SYS_UNLINKAT flags=",
  "Enforcer": "AppArmor",
  "Action": "Block",
  "Result": "Permission denied"
}
```
**Network Alert**
```
{
  "ClusterName": "default",
  "HostName": "aks-agentpool-16128849-vmss000000",
  "NamespaceName": "default",
  "PodName": "vault-0",
  "Labels": "app.kubernetes.io/instance=vault,app.kubernetes.io/name=vault,component=server,helm.sh/chart=vault-0.24.1,statefulset.kubernetes.io/pod-name=vault-0",
  "ContainerID": "775fb27125ee8d9e2f34d6731fbf3bf677a1038f79fe8134856337612007d9ae",
  "ContainerName": "vault",
  "ContainerImage": "docker.io/hashicorp/vault:1.13.1@sha256:b888abc3fc0529550d4a6c87884419e86b8cb736fe556e3e717a6bc50888b3b8",
  "HostPPID": 2203523,
  "HostPID": 2565259,
  "PPID": 2203523,
  "PID": 3558570,
  "UID": 100,
  "ParentProcessName": "/usr/bin/containerd-shim-runc-v2",
  "ProcessName": "/bin/vault",
  "PolicyName": "ksp-vault-network",
  "Severity": "8",
  "Type": "MatchedPolicy",
  "Source": "/bin/vault status -tls-skip-verify",
  "Operation": "Network",
  "Resource": "domain=AF_UNIX type=SOCK_STREAM|SOCK_NONBLOCK|SOCK_CLOEXEC protocol=0",
  "Data": "syscall=SYS_SOCKET",
  "Enforcer": "eBPF Monitor",
  "Action": "Audit",
  "Result": "Passed"
}
```

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










