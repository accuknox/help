#### Simulation
```sh
kubectl exec -it nginx-77b4fdf86c-x7sdm -- bash
root@nginx-77b4fdf86c-x7sdm:/# rm ~/.bash_history
rm: cannot remove '/root/.bash_history': Permission denied
root@nginx-77b4fdf86c-x7sdm:/# rm ~/.bash_history
rm: cannot remove '/root/.bash_history': Permission denied
```

#### Expected Alert
```
root:{} 36 items
ATags:null
Action:Block
ClusterName:0-trust
ContainerID:20a6333c6a46e0da32b3062f0ba76e9aed4fc5ef51f5ee8aec5b980963cedea3
ContainerImage:docker.io/library/nginx:latest@sha256:32da30332506740a2f7c34d5dc70467b7f14ec67d912703568daff790ab3f755
ContainerName:nginx
Data:syscall=SYS_UNLINKAT flags=
Enforcer:AppArmor
HashID:002814c4cdfbb92aa7c3fe7bead75962930b6633a0a5915fd5ad8fe37edcb7a1
HostName:aditya
HostPID:43917
HostPPID:43266
Labels:app=nginx
Message:
NamespaceName:default
Operation:Syscall
Owner:{} 3 items
Name:nginx
Namespace:default
Ref:Deployment
PID:392
PPID:379
PodName:nginx-77b4fdf86c-x7sdm
PolicyName:DefaultPosture
ProcessName:/usr/bin/rm
Resource:/root/.bash_history
Result:Permission denied
Severity:
Source:/usr/bin/rm /root/.bash_history
Tags:
Timestamp:1696578204
Type:MatchedPolicy
UID:0
UpdatedTime:2023-10-06T07:43:24.863776Z
cluster_id:4291
component_name:kubearmor
instanceGroup:0
instanceID:0
workload:1
```