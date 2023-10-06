#### Simulation
```sh
kubectl exec -it mysql-74775b4bf4-65nqf -n wordpress-mysql -- bash
root@mysql-74775b4bf4-65nqf:/# cd var/lib/mysql
root@mysql-74775b4bf4-65nqf:/var/lib/mysql# cat ib_logfile1
cat: ib_logfile1: Permission denied
root@mysql-74775b4bf4-65nqf:/var/lib/mysql#
```

#### Expected Alert
```
Action:Block
ClusterName:aditya
ContainerID:b75628d4225b8071d5795da342cf2a5c03b1d67b22b40016697fcd17a0db20e4
ContainerImage:docker.io/library/mysql:5.6@sha256:20575ecebe6216036d25dab5903808211f1e9ba63dc7825ac20cb975e34cfcae
ContainerName:mysql
Data:syscall=SYS_OPEN flags=O_RDONLY
Enforcer:AppArmor
HostName:aditya
HostPID:30078
HostPPID:30048
Labels:app=mysql
Message:Alert! Attempt to make changes to database detected
NamespaceName:wordpress-mysql
Operation:File
Owner:{} 3 items
Name:mysql
Namespace:wordpress-mysql
Ref:Deployment
PID:247
PPID:240
ParentProcessName:/bin/bash
PodName:mysql-74775b4bf4-65nqf
PolicyName:ksp-block-mysql-dir
ProcessName:/bin/cat
Resource:/var/lib/mysql/ib_logfile1
Result:Permission denied
Severity:1
Source:/bin/cat ib_logfile1
Tags:CIS,CIS_Linux
Timestamp:1696322555
Type:MatchedPolicy
UpdatedTime:2023-10-03T08:42:35.618890Z
cluster_id:3896
component_name:kubearmor
instanceGroup:0
instanceID:0
tenant_id:167
workload:1
```