#### Simulation
```sh
kubectl exec -it dvwa-web-566855bc5b-xtgwq -- bash
root@dvwa-web-566855bc5b-xtgwq:/var/www/html# netstat
bash: /bin/netstat: Permission denied
root@dvwa-web-566855bc5b-xtgwq:/var/www/html# ifconfig
bash: /sbin/ifconfig: Permission denied
root@dvwa-web-566855bc5b-xtgwq:/var/www/html#
root@dvwa-web-566855bc5b-xtgwq:/var/www/html# arp
bash: /usr/sbin/arp: Permission denied
```

#### Expected Alert
```
ClusterName: default
HostName: aditya
NamespaceName: default
PodName: dvwa-web-566855bc5b-npjn8
Labels: tier=frontend,app=dvwa-web
ContainerName: dvwa
ContainerID: e8ac2e227d293e76ab81a34945b68f72a2618ed3275ac64bb6a82f9cd2d014f1
ContainerImage: docker.io/cytopia/dvwa:php-8.1@sha256:f7a9d03b1dfcec55757cc39ca2470bdec1618b11c4a51052bb4f5f5e7d78ca39
Type: MatchedPolicy
PolicyName: harden-dvwa-web-network-service-scanning
Severity: 5
Message: Network service has been scanned!
Source: /bin/bash
Resource: /bin/netstat
Operation: Process
Action: Block
Data: syscall=SYS_EXECVE
Enforcer: AppArmor
Result: Permission denied
ATags: [MITRE FGT1046 CIS]
HostPID: 35592
HostPPID: 35557
Owner: map[Name:dvwa-web Namespace:default Ref:Deployment]
PID: 989
PPID: 983
ParentProcessName: /bin/bash
ProcessName: /bin/netstat
Tags: MITRE,FGT1046,CIS
```