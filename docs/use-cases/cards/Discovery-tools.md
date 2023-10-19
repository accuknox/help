# Discovery tools
Do not allow discovery/search of tools/configuration.

## Description
Adversaries may attempt to get a listing of services running on remote hosts and local network infrastructure devices, including those that may be vulnerable to remote software exploitation. Common methods to acquire this information include port and/or vulnerability scans using tools that are brought onto a system

## Attack Scenario
Adversaries can potentially use information related to services, remote hosts, and local network infrastructure devices, including those that may be vulnerable to remote software exploitation to perform malicious attacks like exploiting open ports and injecting payloads to get remote shells. It's crucial to take proactive measures to prevent these attacks from occurring, such as implementing proper network segmentation and hardening network devices. [**Examples:** Brute force, Command Injection, Ping of Death(PoD)]

## Tags
- CIS Distribution Independent Linuxv2.0
- Control-Id: 6.3

## Policy Templates
### Discovery tools
```yaml
Version: security.kubearmor.com/v1
kind: KubeArmorPolicy
metadata:
  name: harden-dvwa-web-network-service-scanning
  namespace: default
spec:
  action: Block
  message: Network service has been scanned!
  process:
    matchPaths:
    - path: /usr/bin/netstat
    - path: /bin/netstat
    - path: /usr/sbin/ip
    - path: /usr/bin/ip
    - path: /sbin/ip
    - path: /bin/ip
    - path: /usr/sbin/iw
    - path: /sbin/iw
    - path: /usr/sbin/ethtool
    - path: /sbin/ethtool
    - path: /usr/sbin/ifconfig
    - path: /sbin/ifconfig
    - path: /usr/sbin/arp
    - path: /sbin/arp
    - path: /usr/sbin/iwconfig
    - path: /sbin/iwconfig
  selector:
    matchLabels:
      app: dvwa-web
      tier: frontend
  severity: 5
  tags:
  - MITRE
  - FGT1046
  - CIS
```
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
root:{} 36 items
ATags:[] 3 items
0:MITRE
1:FGT1046
2:CIS
Action:Block
ClusterName:no-trust
ContainerID:e8ac2e227d293e76ab81a34945b68f72a2618ed3275ac64bb6a82f9cd2d014f1
ContainerImage:docker.io/cytopia/dvwa:php-8.1@sha256:f7a9d03b1dfcec55757cc39ca2470bdec1618b11c4a51052bb4f5f5e7d78ca39
ContainerName:dvwa
Data:syscall=SYS_EXECVE
Enforcer:AppArmor
HashID:7e0f52f1616e5cebf11f12028eefe2c032280663c2b61dd742be78ef5791d413
HostName:aditya
HostPID:35592
HostPPID:35557
Labels:tier=frontend,app=dvwa-web
Message:Network service has been scanned!
NamespaceName:default
Operation:Process
Owner:{} 3 items
Name:dvwa-web
Namespace:default
Ref:Deployment
PID:989
PPID:983
PodName:dvwa-web-566855bc5b-npjn8
PolicyName:harden-dvwa-web-network-service-scanning
ProcessName:/bin/netstat
Resource:/bin/netstat
Result:Permission denied
Severity:5
Source:/bin/bash
Tags:MITRE,FGT1046,CIS
Timestamp:1696501152
Type:MatchedPolicy
UID:0
UpdatedTime:2023-10-05T10:19:12.809606Z
cluster_id:4225
component_name:kubearmor
instanceGroup:0
instanceID:0
workload:1
```

## References
[MITRE Network Service Discovery](https://attack.mitre.org/techniques/T1046/)



