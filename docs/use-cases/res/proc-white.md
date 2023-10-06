#### Simulation
Set the default security posture to default-deny

```sh
kubectl annotate ns default kubearmor-file-posture=block --overwrite
```

```sh
kubectl exec -it dvwa-web-566855bc5b-xtgwq -- bash
root@dvwa-web-566855bc5b-xtgwq:/var/www/html# ping
bash: /bin/ping: Permission denied
```

#### Expected Alert
```
ClusterName: default
HostName: aditya
NamespaceName: default
PodName: dvwa-web-566855bc5b-cnvc2
Labels: tier=frontend,app=dvwa-web
ContainerName: dvwa
ContainerID: be0d45c1bf0fc853c8fa39f19e0c0af0e495235eb27365629d5721c3c89c2cb5
ContainerImage: docker.io/cytopia/dvwa:php-8.1@sha256:f7a9d03b1dfcec55757cc39ca2470bdec1618b11c4a51052bb4f5f5e7d78ca39
Type: MatchedPolicy
PolicyName: DefaultPosture
Source: /bin/bash
Resource: /bin/ping google.com
Operation: Process
Action: Block
Data: syscall=SYS_EXECVE
Enforcer: eBPF Monitor
Result: Permission denied
HostPID: 46090
HostPPID: 43271
Owner: map[Name:dvwa-web Namespace:default Ref:Deployment]
PID: 64
PPID: 55
ParentProcessName: /bin/bash
ProcessName: /bin/ping
```