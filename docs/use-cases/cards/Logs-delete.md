# Logs delete
Do not allow external tooling to delete logs/traces of critical components.

## Narrative
Adversaries may delete or modify artifacts generated within systems to remove evidence of their presence or hinder defenses. Various artifacts may be created by an adversary or something that can be attributed to an adversary’s actions. Typically these artifacts are used as defensive indicators related to monitored events, such as strings from downloaded files, logs that are generated from user actions, and other data analyzed by defenders. Location, format, and type of artifact (such as command or login history) are often specific to each platform. 

## Attack Scenario
It's important to note that removal of indicators related to intrusion activity may interfere with event collection, reporting, or other processes used to detect such activity. This can compromise the integrity of security solutions by causing notable events to go unreported. Additionally, this activity may impede forensic analysis and incident response, due to a lack of sufficient data to determine what occurred. It's crucial to ensure that all relevant indicators are properly monitored and reported to prevent such issues from occurring.<br /> **Attack Type** Integrity Threats, Data Manipulation **Actual Attack** NetWalker, Conti, DarkSide RaaS 

## Compliance
- CIS Distribution Independent Linuxv2.0
- Control-Id: 6.6
- Control-Id: 7.6.2
- Control-Id: 7.6.3
- NIST_800-53_CM-5

## Policy
### Logs delete
```yaml
apiVersion: security.kubearmor.com/v1
kind: KubeArmorPolicy
metadata:
  name: harden-nginx-shell-history-mod
  namespace: default
spec:
  action: Block
  file:
    matchPaths:
    - fromSource:
      - path: /usr/bin/shred
      - path: /usr/bin/rm
      - path: /bin/mv
      - path: /bin/rm
      - path: /usr/bin/mv
      path: /root/*_history
    - fromSource:
      - path: /usr/bin/shred
      - path: /usr/bin/rm
      - path: /bin/rm
      - path: /bin/mv
      - path: /usr/bin/mv
      path: /home/*/*_history
  message: Alert! shell history modification or deletion detected and prevented
  process:
    matchPaths:
    - path: /usr/bin/shred
    - path: /usr/bin/rm
    - path: /bin/mv
    - path: /bin/rm
    - path: /usr/bin/mv
  selector:
    matchLabels:
      app: nginx
  severity: 5
  tags:
  - CIS
  - NIST_800-53
  - NIST_800-53_CM-5
  - NIST_800-53_AU-6(8)
  - MITRE_T1070_indicator_removal_on_host
  - MITRE
  - MITRE_T1036_masquerading
```
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
{
  "Action": "Block",
  "ClusterName": "0-trust",
  "ContainerID": "20a6333c6a46e0da32b3062f0ba76e9aed4fc5ef51f5ee8aec5b980963cedea3",
  "ContainerImage": "docker.io/library/nginx:latest@sha256:32da30332506740a2f7c34d5dc70467b7f14ec67d912703568daff790ab3f755",
  "ContainerName": "nginx",
  "Data": "syscall=SYS_UNLINKAT flags=",
  "Enforcer": "AppArmor",
  "HostName": "aditya",
  "HostPID": 43917,
  "HostPPID": 43266,
  "Labels": "app=nginx",
  "NamespaceName": "default",
  "Operation": "File",
  "Owner": {
    "Name": "nginx",
    "Namespace": "default",
    "Ref": "Deployment"
  },
  "PID": 392,
  "PPID": 379,
  "ParentProcessName": "/usr/bin/bash",
  "PodName": "nginx-77b4fdf86c-x7sdm",
  "PolicyName": "DefaultPosture",
  "ProcessName": "/usr/bin/rm",
  "Resource": "/root/.bash_history",
  "Result": "Permission denied",
  "Source": "/usr/bin/rm /root/.bash_history",
  "Timestamp": 1696577978,
  "Type": "MatchedPolicy",
  "UpdatedTime": "2023-10-06T07:39:38.182538Z",
  "cluster_id": "4291",
  "component_name": "kubearmor",
  "instanceGroup": "0",
  "instanceID": "0",
  "tenant_id": "167",
  "workload": "1"
}
```

## References
[MITRE Indicator Removal](https://attack.mitre.org/techniques/T1070/)<br />



