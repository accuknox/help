#### Simulation
```sh
kubectl exec -it mysql-74775b4bf4-mg7np -n wordpress-mysql -- bash
root@mysql-74775b4bf4-mg7np:/# cd /usr/bin
root@mysql-74775b4bf4-mg7np:/usr/bin# touch malicious-file
```

#### Expected Alert
```
ClusterName: default
HostName: gke-cluster-1-default-pool-37f4c896-m209
NamespaceName: wordpress-mysql
PodName: mysql-74775b4bf4-mg7np
Labels: app=mysql
ContainerName: mysql
ContainerID: 6020fc7ad3489630e5d67b7a4615edefecc59cb1bbda826611c349a0a553ef60
ContainerImage: docker.io/library/mysql:5.6@sha256:20575ecebe6216036d25dab5903808211f1e9ba63dc7825ac20cb975e34cfcae
Type: MatchedPolicy
PolicyName: audit-for-system-paths
Severity: 5
Message: Access to network files detected. Possible violation of NIST Controls
Source: /usr/bin/touch malicious-file
Resource: /etc/ld.so.cache
Operation: File
Action: Audit
Data: syscall=SYS_OPEN flags=O_RDONLY|O_CLOEXEC
Enforcer: eBPF Monitor
Result: Passed
ATags: [NIST PCI-DSS]
HostPID: 2.562504e+06
HostPPID: 2.56229e+06
Owner: map[Name:mysql Namespace:wordpress-mysql Ref:Deployment]
PID: 167
PPID: 160
ParentProcessName: /bin/bash
ProcessName: /bin/touch
Tags: NIST,PCI-DSS
```