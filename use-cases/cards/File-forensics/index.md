# File forensics
Get granular details of all the accessed files within the target workloads.

## Narrative
Changes to system binary folders, configuration paths, and credentials paths need to be monitored for change.

## Attack Scenario
An attacker might want to update the configuration so as to disable security controls or access logs.

## Compliance
- CISv1
- Control-Id-Linux 4.1.12

## Policy
### File Forensics
```yaml
apiVersion: security.kubearmor.com/v1
kind: KubeArmorPolicy
metadata:
  name: audit-for-system-paths
  namespace: wordpress-mysql
spec:
  action: Allow
  file:
    matchDirectories:
    - dir: /bin/
      readOnly: true
      recursive: true
      action: Audit
    - dir: /sbin/
      readOnly: true
      recursive: true
      action: Audit
    - dir: /usr/sbin/
      readOnly: true
      action: Audit
      recursive: true
    - dir: /usr/bin/
      readOnly: true
      recursive: true
      action: Audit
    - dir: /etc/
      readOnly: true
      recursive: true
      action: Audit
  severity: 5
  tags:
  - NIST
  - PCI-DSS
  message: Access to network files detected. Possible violation of NIST Controls
  selector:
    matchLabels:
      app: mysql
```
#### Simulation
```sh
kubectl exec -it mysql-74775b4bf4-mg7np -n wordpress-mysql -- bash
root@mysql-74775b4bf4-mg7np:/# cd /usr/bin
root@mysql-74775b4bf4-mg7np:/usr/bin# touch malicious-file
```

#### Expected Alert
```
ClusterName: default
HostName: gke-cluster-1-default-pool-37f4c896-m209
NamespaceName: wordpress-mysql
PodName: mysql-74775b4bf4-mg7np
Labels: app=mysql
ContainerName: mysql
ContainerID: 6020fc7ad3489630e5d67b7a4615edefecc59cb1bbda826611c349a0a553ef60
ContainerImage: docker.io/library/mysql:5.6@sha256:20575ecebe6216036d25dab5903808211f1e9ba63dc7825ac20cb975e34cfcae
Type: MatchedPolicy
PolicyName: audit-for-system-paths
Severity: 5
Message: Access to network files detected. Possible violation of NIST Controls
Source: /usr/bin/touch malicious-file
Resource: /etc/ld.so.cache
Operation: File
Action: Audit
Data: syscall=SYS_OPEN flags=O_RDONLY|O_CLOEXEC
Enforcer: eBPF Monitor
Result: Passed
ATags: [NIST PCI-DSS]
HostPID: 2.562504e+06
HostPPID: 2.56229e+06
Owner: map[Name:mysql Namespace:wordpress-mysql Ref:Deployment]
PID: 167
PPID: 160
ParentProcessName: /bin/bash
ProcessName: /bin/touch
Tags: NIST,PCI-DSS
```

## References
[MITRE Data Manipulation](https://attack.mitre.org/techniques/T1602/)<br />



