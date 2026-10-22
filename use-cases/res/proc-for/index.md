#### Simulation
```sh
kubectl exec -it wordpress-7c966b5d85-wvtln -n wordpress-mysql -- bash
root@wordpress-7c966b5d85-wvtln:/var/www/html# ps -A
    PID TTY          TIME CMD
      1 ?        00:00:08 apache2
    189 ?        00:00:00 apache2
    190 ?        00:00:00 apache2
    191 ?        00:00:00 apache2
    192 ?        00:00:00 apache2
    193 ?        00:00:00 apache2
    245 pts/0    00:00:00 bash
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
PolicyName: ksp-discovery-process-discovery
Severity: 5
Message: Someone accessed running process
Source: /bin/bash
Resource: /bin/ps -A
Operation: Process
Action: Audit
Data: syscall=SYS_EXECVE
Enforcer: eBPF Monitor
Result: Passed
ATags: [MITRE Discovery]
HostPID: 1.252488e+06
HostPPID: 1.250979e+06
Owner: map[Name:wordpress Namespace:wordpress-mysql Ref:Deployment]
PID: 288
PPID: 281
ParentProcessName: /bin/bash
ProcessName: /bin/ps
Tags: MITRE,Discovery
```