#### Simulation
```sh
kubectl exec -it nginx-77b4fdf86c-x7sdm -- bash
root@nginx-77b4fdf86c-x7sdm:/# cd /etc/nginx/
root@nginx-77b4fdf86c-x7sdm:/etc/nginx# ls
bash: /usr/bin/ls: Permission denied
root@nginx-77b4fdf86c-x7sdm:/etc/nginx#
```

#### Expected Alert
```
ClusterName: default
HostName: aditya
NamespaceName: default
PodName: nginx-77b4fdf86c-x7sdm
Labels: app=nginx
ContainerName: nginx
ContainerID: 20a6333c6a46e0da32b3062f0ba76e9aed4fc5ef51f5ee8aec5b980963cedea3
ContainerImage: docker.io/library/nginx:latest@sha256:32da30332506740a2f7c34d5dc70467b7f14ec67d912703568daff790ab3f755
Type: MatchedPolicy
PolicyName: DefaultPosture
Source: /usr/bin/bash
Resource: /usr/bin/ls
Operation: Process
Action: Block
Data: syscall=SYS_EXECVE
Enforcer: eBPF Monitor
Result: Permission denied
HostPID: 70701
HostPPID: 70666
Owner: map[Name:nginx Namespace:default Ref:Deployment]
PID: 444
PPID: 439
ParentProcessName: /usr/bin/bash
ProcessName: /usr/bin/ls
```