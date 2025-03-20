---
title: Securing Configuration Data with AccuKnox CNAPP
description: Protect access to configuration data containing plain text credentials.
---

# Securing Configuration Data with AccuKnox CNAPP
Protect access to configuration data containing plain text credentials.

## Narrative
Adversaries may search local file systems and remote file shares for files containing insecurely stored credentials. These can be files created by users to store their own credentials, shared credential stores for a group of individuals, configuration files containing passwords for a system or service, or source code/binary files containing embedded passwords.

## Attack Scenario
In a possible attack scenario, an attacker may try to change the configurations to open websites to application security holes such as session hijacking and cross-site scripting attacks, which can lead to the disclosure of private data. Additionally, attackers can also leverage these changes to gather sensitive information. It's crucial to take proactive measures to prevent these attacks from occurring.<br /> **Attack Type** Cross-Site Scripting(XSS), Data manipulation, Session hijacking<br /> **Actual Attack** XSS attack on Fortnite 2019, Turla LightNeuron Attack

## Compliance
- CIS Distribution Independent Linuxv2.0
- Control-Id: 6.16.14

## Policy
### Config data
```yaml
apiVersion: security.kubearmor.com/v1
kind: KubeArmorPolicy
metadata:
  name: ksp-block-stig-v-81883-restrict-access-to-config-files
  namespace: wordpress-mysql
spec:
  tags:
  - config-files
  message: Alert! configuration files have been accessed
  selector:
    matchLabels:
      app: wordpress
  file:
    matchPatterns:
    - pattern: /**/*.conf
      ownerOnly: true
  action: Block
```
#### Simulation

With a shell different than the user owning the file:
```sh
$ cat /etc/ca-certificates.conf
cat: /etc/ca-certificates.conf: Permission denied
$
```

#### Expected Alert
```
{
  "Action": "Block",
  "ClusterName": "d3mo",
  "ContainerID": "548176888fca6bb6d66633794f3d5f9d54930a9d9f43d4f05c11de821c758c0f",
  "ContainerImage": "docker.io/library/wordpress:4.8-apache@sha256:6216f64ab88fc51d311e38c7f69ca3f9aaba621492b4f1fa93ddf63093768845",
  "ContainerName": "wordpress",
  "Data": "syscall=SYS_OPEN flags=O_RDONLY",
  "Enforcer": "AppArmor",
  "HostName": "master-node",
  "HostPID": 39039,
  "HostPPID": 38787,
  "Labels": "app=wordpress",
  "NamespaceName": "wordpress-mysql",
  "Operation": "File",
  "Owner": {
    "Name": "wordpress",
    "Namespace": "wordpress-mysql",
    "Ref": "Deployment"
  },
  "PID": 220,
  "PPID": 219,
  "ParentProcessName": "/bin/dash",
  "PodName": "wordpress-fb448db97-wj7n7",
  "PolicyName": "DefaultPosture",
  "ProcessName": "/bin/cat",
  "Resource": "/etc/ca-certificates.conf",
  "Result": "Permission denied",
  "Source": "/bin/cat /etc/ca-certificates.conf",
  "Timestamp": 1696485467,
  "Type": "MatchedPolicy",
  "UID": 1000,
  "UpdatedTime": "2023-10-05T05:57:47.935622Z",
  "cluster_id": "2302",
  "component_name": "kubearmor",
  "instanceGroup": "0",
  "instanceID": "0",
  "tenant_id": "167",
  "workload": "1"
}
```

## References
[MITRE Unsecured credentials in files](https://attack.mitre.org/techniques/T1552/001/)<br />[Turla LightNeuron](https://www.welivesecurity.com/2019/05/07/turla-lightneuron-email-too-far/)<br />



