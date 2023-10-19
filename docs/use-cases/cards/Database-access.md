# Database access
Protect read/write access to raw database tables from unknown processes.

## Description
Applications use databases to store all the information such as posts, blogs, user information, etc. WordPress applications almost certainly use a MySQL database for storing their content, and those are usually stored elsewhere on the system, often /var/lib/mysql/some_db_name. 

## Attack Scenario
Adversaries have been known to use various techniques to steal information from databases. This information can include user credentials, posts, blogs, and more. By obtaining this information, adversaries can gain access to user accounts and potentially perform a full-account takeover, which can lead to further compromise of the target system. It's important to ensure that appropriate security measures are in place to protect against these types of attacks. [**Examples:** SQL Injection, Credential Access, Account Takeover, etc.]

## Tags
- CIS Distribution Independent Linuxv2.0
- Control-Id: 6.14.4

## Policy Templates
### Database Access
```yaml
apiVersion: security.kubearmor.com/v1
kind: KubeArmorPolicy
metadata:
  name: ksp-block-mysql-dir
  namespace: wordpress-mysql
spec:
  message: Alert! Attempt to make changes to database detected
  tags:
  - CIS
  - CIS_Linux
  selector:
    matchLabels:
      app: mysql
  file:
    matchDirectories:
    - dir: /var/lib/mysql/
      ownerOnly: true
      readOnly: true
      severity: 1
      action: Block
```
#### Simulation
```sh
kubectl exec -it mysql-74775b4bf4-65nqf -n wordpress-mysql -- bash
root@mysql-74775b4bf4-65nqf:/# cd var/lib/mysql
root@mysql-74775b4bf4-65nqf:/var/lib/mysql# cat ib_logfile1
cat: ib_logfile1: Permission denied
root@mysql-74775b4bf4-65nqf:/var/lib/mysql#
```

#### Expected Alert
```
root:{} 36 items
 ATags:[] 2 items
   0:CIS
   1:CIS_Linux
Action:Block
ClusterName:aditya
ContainerID:b75628d4225b8071d5795da342cf2a5c03b1d67b22b40016697fcd17a0db20e4
ContainerImage:docker.io/library/mysql:5.6@sha256:20575ecebe6216036d25dab5903808211f1e9ba63dc7825ac20cb975e34cfcae
ContainerName:mysql
Data:syscall=SYS_OPEN flags=O_RDONLY
Enforcer:AppArmor
HashID:a7b7d91d52de395fe6cda698e89e0112e6f3ab818ea331cee60295a8ede358c8
HostName:aditya
HostPID:29898
HostPPID:29752
Labels:app=mysql
Message:Alert! Attempt to make changes to database detected
NamespaceName:wordpress-mysql
Operation:File
Owner:{} 3 items
  Name:mysql
  Namespace:wordpress-mysql
  Ref:Deployment
PID:230
PPID:223
PodName:mysql-74775b4bf4-65nqf
PolicyName:ksp-block-mysql-dir
ProcessName:/bin/cat
Resource:/var/lib/mysql/ib_logfile1
Result:Permission denied
Severity:1
Source:/bin/cat ib_logfile1
Tags:CIS,CIS_Linux
Timestamp:1696322555
Type:MatchedPolicy
UID:0
UpdatedTime:2023-10-03T08:42:35.618890Z
cluster_id:3896
component_name:kubearmor
instanceGroup:0
instanceID:0
workload:1
```

## References
[MITRE Scan Databases](https://attack.mitre.org/techniques/T1596/005/)



