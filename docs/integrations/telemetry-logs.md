
Accuknox CNAPP Solution provides comprehensive visibility of the assets with the help of logs. AccuKnox’s open-source KubeArmor can forward container-related logs to the SaaS. Also, it can forward the container logs that are present in the workloads. We can also use the Feeder service agent to pass the logs to other SIEM tools like Splunk, ELK, Rsyslog, etc.., The information provided by the logs will be useful to understand the attack vector of any attempted attacks.

## Sample Container Log

**Process Log**

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
  "ParentProcessName": "/usr/bin/runc",
  "ProcessName": "/bin/sh",
  "HostPPID": 2514065,
  "HostPID": 2514068,
  "PPID": 2514065,
  "PID": 3552620,
  "UID": 100,
  "Type": "ContainerLog",
  "Source": "/usr/bin/runc",
  "Operation": "Process",
  "Resource": "/bin/sh -ec vault status -tls-skip-verify",
  "Data": "syscall=SYS_EXECVE",
  "Result": "Passed"
}
```

**File log**

```
{
  "ClusterName": "default",
  "HostName": "aks-agentpool-16128849-vmss000000",
  "NamespaceName": "accuknox-agents",
  "PodName": "discovery-engine-6f5c4df7b4-q8zbc",
  "Labels": "app=discovery-engine",
  "ContainerID": "7aca8d52d35ab7872df6a454ca32339386be755d9ed6bd6bf7b37ec6aaf277e4",
  "ContainerName": "discovery-engine",
  "ContainerImage": "docker.io/accuknox/knoxautopolicy:v0.9@sha256:bb83b5c6d41e0d0aa3b5d6621188c284ea99741c3692e34b0f089b0e74745413",
  "ParentProcessName": "/usr/bin/containerd-shim-runc-v2",
  "ProcessName": "/knoxAutoPolicy",
  "HostPPID": 967496,
  "HostPID": 967872,
  "PPID": 967496,
  "PID": 1,
  "Type": "ContainerLog",
  "Source": "/knoxAutoPolicy",
  "Operation": "File",
  "Resource": "/var/run/secrets/kubernetes.io/serviceaccount/token",
  "Data": "syscall=SYS_OPENAT fd=-100 flags=O_RDONLY|O_CLOEXEC",
  "Result": "Passed"
}
```

**Network log**

```
{
  "ClusterName": "default",
  "HostName": "aks-agentpool-16128849-vmss000001",
  "NamespaceName": "accuknox-agents",
  "PodName": "policy-enforcement-agent-7946b64dfb-f4lgv",
  "Labels": "app=policy-enforcement-agent",
  "ContainerID": "b597629c9b59304c779c51839e9a590fa96871bdfdf55bfec73b26c9fb7647d7",
  "ContainerName": "policy-enforcement-agent",
  "ContainerImage": "public.ecr.aws/k9v9d5v2/policy-enforcement-agent:v0.1.0@sha256:005c1fde3ff8a667f3ac7540c5c011c752a7e3aaa2c89aa335703289ed8d80f8",
  "ParentProcessName": "/usr/bin/containerd-shim-runc-v2",
  "ProcessName": "/home/pea/main",
  "HostPPID": 1394403,
  "HostPID": 1394554,
  "PPID": 1394403,
  "PID": 1,
  "Type": "ContainerLog",
  "Source": "./main",
  "Operation": "Network",
  "Resource": "sa_family=AF_INET sin_port=53 sin_addr=10.0.0.10",
  "Data": "syscall=SYS_CONNECT fd=10",
  "Result": "Passed"
}
```

## Logs Format

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
