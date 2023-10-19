# Trusted certs bundle
Protect write access to the trusted root certificates bundle

## Description
Adversaries may install a root certificate on a compromised system to avoid warnings when connecting to adversary-controlled web servers. Root certificates are used in public key cryptography to identify a root certificate authority (CA). When a root certificate is installed, the system or application will trust certificates in the root's chain of trust that have been signed by the root certificate. Installation of a root certificate on a compromised system would give an adversary a way to degrade the security of that system.

## Attack Scenario
By using this technique, attackers can successfully evade security warnings that alert users when compromised systems connect over HTTPS to adversary-controlled web servers. These servers often look like legitimate websites, and are designed to trick users into entering their login credentials, which can then be used by the attackers. It's important to be aware of this threat and take necessary precautions to prevent these attacks from happening. [**Examples:** Man-In-The-Middle(MITM)]

## Tags
- CIS Distribution Independent Linuxv2.0
- Control-Id: 6.3.4

## Policy Templates
### Trusted Certs Bundle
```yaml
apiVersion: security.kubearmor.com/v1
kind: KubeArmorPolicy
metadata:
  name: harden-mysql-trusted-cert-mod
  namespace: wordpress-mysql
spec:
  action: Block
  file:
    matchDirectories:
    - dir: /etc/ssl/
      readOnly: true
      recursive: true
    - dir: /etc/pki/
      readOnly: true
      recursive: true
    - dir: /usr/local/share/ca-certificates/
      readOnly: true
      recursive: true
  message: Credentials modification denied
  selector:
    matchLabels:
      app: mysql
  severity: 1
  tags:
  - MITRE
  - MITRE_T1552_unsecured_credentials
  - FGT1555
  - FIGHT
```
#### Simulation
```sh
 kubectl exec -it mysql-74775b4bf4-65nqf -n wordpress-mysql -- bash
root@mysql-74775b4bf4-65nqf:/# cd /etc/ssl/
root@mysql-74775b4bf4-65nqf:/etc/ssl# ls
certs
root@mysql-74775b4bf4-65nqf:/etc/ssl# rmdir certs
rmdir: failed to remove 'certs': Permission denied
root@mysql-74775b4bf4-65nqf:/etc/ssl# cd certs/
root@mysql-74775b4bf4-65nqf:/etc/ssl/certs# touch new
touch: cannot touch 'new': Permission denied
root@mysql-74775b4bf4-65nqf:/etc/ssl/certs#
```

#### Expected Alert
```
root:{} 36 items
  ATags:null
  Action:Block
  ClusterName:aditya
ContainerID:b75628d4225b8071d5795da342cf2a5c03b1d67b22b40016697fcd17a0db20e4            
ContainerImage:docker.io/library/mysql:5.6@sha256:20575ecebe6216036d25dab5903808211f1e9ba63dc7825ac20cb975e34cfcae
  ContainerName:mysql
  Data:syscall=SYS_RMDIR
  Enforcer:AppArmor
  HashID:e9e43507c8e19feaf61a50e7e5761443f4b6e8fc0df74928cc0d0cb5cd4fa961
  HostName:aditya
HostPID:24462
HostPPID:24411
Labels:app=mysql
Message:
NamespaceName:wordpress-mysql
Operation:Syscall
Owner:{} 3 items
  Name:mysql
  Namespace:wordpress-mysql
  Ref:Deployment
PID:185
PPID:179
PodName:mysql-74775b4bf4-65nqf
PolicyName:DefaultPosture
ProcessName:/bin/rmdir
Resource:/etc/ssl/certs
Result:Permission denied
Severity:
Source:/bin/rmdir certs
Tags:
Timestamp:1696320102
Type:MatchedPolicy
UID:0
UpdatedTime:2023-10-03T08:01:42.373810Z
cluster_id:3896
component_name:kubearmor
instanceGroup:0
instanceID:0
workload:1
```

## References
[MITRE Subvert Trust Controls](https://attack.mitre.org/techniques/T1553/004/)
[MITRE Unsecured credentials](https://attack.mitre.org/techniques/T1552/)



