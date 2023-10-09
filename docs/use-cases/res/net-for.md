#### Simulation
```sh
kubectl exec -it wordpress-7c966b5d85-wvtln -n wordpress-mysql -- bash
root@wordpress-7c966b5d85-wvtln:/var/www/html# cd /etc/network/if-up.d
root@wordpress-7c966b5d85-wvtln:/etc/network/if-up.d# ls
mountnfs
```

#### Expected Alert
```
ClusterName: default
HostName: gke-cluster-1-default-pool-37f4c896-8cn6
NamespaceName: wordpress-mysql
PodName: wordpress-7c966b5d85-wvtln
Labels: app=wordpress
ContainerName: wordpress
ContainerID: 6d09394a988c5cf6b9fe260d28fdd57d6ff281618869a173965ecd94a3efac44
ContainerImage: docker.io/library/wordpress:4.8-apache@sha256:6216f64ab88fc51d311e38c7f69ca3f9aaba621492b4f1fa93ddf63093768845
Type: MatchedPolicy
PolicyName: ksp-nist-ac-18-1-network-audit
Severity: 3
Message: Access to network files detected. Possible violation of NIST Controls
Source: /bin/ls
Resource: /etc/network/if-up.d
Operation: File
Action: Audit
Data: syscall=SYS_OPENAT fd=-100 flags=O_RDONLY|O_NONBLOCK|O_DIRECTORY|O_CLOEXEC
Enforcer: eBPF Monitor
Result: Passed
ATags: [NIST-800 AC-18(1) Networking Access NIST_SA NIST_SA-20 NIST_SA-20-Customized Development of Critical Components SA]
HostPID: 1.275441e+06
HostPPID: 1.275298e+06
Owner: map[Name:wordpress Namespace:wordpress-mysql Ref:Deployment]
PID: 342
PPID: 336
ParentProcessName: /bin/bash
ProcessName: /bin/ls
Tags: NIST-800,AC-18(1),Networking,Access,NIST_SA,NIST_SA-20,NIST_SA-20-Customized Development of Critical Components,SA
```