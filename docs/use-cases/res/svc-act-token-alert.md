#### Simulation
```sh
root@wordpress-7c966b5d85-42jwx:/# cd /run/secrets/kubernetes.io/serviceaccount/ 
root@wordpress-7c966b5d85-42jwx:/run/secrets/kubernetes.io/serviceaccount# ls 
ls: cannot open directory .: Permission denied 
root@wordpress-7c966b5d85-42jwx:/run/secrets/kubernetes.io/serviceaccount# 
```

#### Expected Alert
```
ClusterName: default
HostName: aditya
NamespaceName: wordpress-mysql
PodName: wordpress-7c966b5d85-shn85
Labels: app=wordpress
ContainerName: wordpress
ContainerID: 872599a29401aae31d39251a24b3c0012724a4878df8c8e1d72fa592f5b4a494
ContainerImage: docker.io/library/wordpress:4.8-apache@sha256:6216f64ab88fc51d311e38c7f69ca3f9aaba621492b4f1fa93ddf63093768845
Type: MatchedPolicy
PolicyName: DefaultPosture
Source: /bin/ls serviceaccount/
Resource: /run/secrets/kubernetes.io/serviceaccount
Operation: File
Action: Block
Data: syscall=SYS_OPENAT fd=-100 flags=O_RDONLY|O_NONBLOCK|O_DIRECTORY|O_CLOEXEC
Enforcer: AppArmor
Result: Permission denied
HostPID: 35455
HostPPID: 34306
Owner: map[Name:wordpress Namespace:wordpress-mysql Ref:Deployment]
PID: 206
PPID: 193
ParentProcessName: /bin/bash
ProcessName: /bin/ls
```
