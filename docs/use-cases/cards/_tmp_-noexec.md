# /tmp/ noexec
Do not allow execution of binaries from /tmp/ folder.

## Description
If provided the necessary privileges, users have the ability to install software in organizational information systems. To maintain control over the types of software installed, organizations identify permitted and prohibited actions regarding software installation. Prohibited software installations may include, for example, software with unknown or suspect pedigrees or software that organizations consider potentially malicious.

## Attack Scenario
In an attack scenario, a hacker may attempt to inject malicious scripts into the /tmp folder through a web application exploit. Once the script is uploaded, the attacker may try to execute it on the server in order to take it down. By hardening the /tmp folder, the attacker will not be able to execute the script, preventing such attacks. It's essential to implement these security measures to protect against these types of attacks and ensure the safety of the system. [**Examples:** System Failure, System Breach, etc.]

## Tags
- CIS Distribution Independent Linuxv2.0
- Control-Id: 1.1.5
- Control-Id: 1.1.10

## Policy Templates
### /tmp/ noexec
```yaml
apiVersion: security.kubearmor.com/v1
kind: KubeArmorPolicy
metadata:
  name: ksp-block-exec-inside-tmp
  namespace: wordpress-mysql
spec:
  tags:
  - config-files
  message: Alert! Execution attempted inside tmp folder
  selector:
    matchLabels:
      app: wordpress
  process:
    matchPatterns:
    - pattern: /tmp/*
    - pattern: /var/tmp/*
  action: Block
```
#### Simulation
```sh
root@wordpress-fb448db97-wj7n7:/var/tmp# ls /var/tmp                                                                    xvzf                                                                                                                    
root@wordpress-fb448db97-wj7n7:/var/tmp# /var/tmp/xvzf                                                                  
bash: /var/tmp/xvzf: Permission denied                                                                                  
root@wordpress-fb448db97-wj7n7:/var/tmp#  
```

#### Expected Alert
```
root:{} 36 items
ATags:[] 2 items
0:CIS
1:CIS_Linux
Action:Block
ClusterName:d3mo
ContainerID:548176888fca6bb6d66633794f3d5f9d54930a9d9f43d4f05c11de821c758c0f
ContainerImage:docker.io/library/wordpress:4.8-apache@sha256:6216f64ab88fc51d311e38c7f69ca3f9aaba621492b4f1fa93ddf63093768845
ContainerName:wordpress
Data:syscall=SYS_OPEN flags=O_WRONLY|O_CREAT|O_EXCL|O_TRUNC
Enforcer:AppArmor
HashID:bce1dc209e819b264c7f85327083a9cf3ab66ee19d3ad3f30b11cd7e60c764cc
HostName:master-node
HostPID:30490
HostPPID:6119
Labels:app=wordpress
Message:Alert! Execution attempted inside /tmp
NamespaceName:wordpress-mysql
Operation:File
Owner:{} 3 items
Name:wordpress
Namespace:wordpress-mysql
Ref:Deployment
PID:193
PPID:6119
PodName:wordpress-fb448db97-wj7n7
PolicyName:ksp-block-exec-inside-tmp
ProcessName:/bin/bash
Resource:/tmp/sh-thd-2512146865
Result:Permission denied
Severity:1
Source:/bin/bash
Tags:CIS,CIS_Linux
Timestamp:1696492433
Type:MatchedPolicy
UID:0
UpdatedTime:2023-10-05T07:53:53.259403Z
cluster_id:2302
component_name:kubearmor
instanceGroup:0
instanceID:0
workload:1
```

## References
[STIG no exec in /tmp](https://www.stigviewer.com/stig/red_hat_enterprise_linux_6/2016-12-16/finding/V-57569)



