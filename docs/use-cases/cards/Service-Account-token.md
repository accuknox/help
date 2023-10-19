# Service Account token
Protect access to k8s service account token

## Description
K8s mounts the service account token as part of every pod by default. The service account token is a credential that can be used as a bearer token to access k8s APIs and gain access to other k8s entities. Many times there are no processes in the pod that use the service account tokens which means in such cases the k8s service account token is an unused asset that can be leveraged by the attacker.

## Attack Scenario
It's important to note that attackers often look for ways to gain access to other entities within Kubernetes clusters. One common method is to check for credential accesses, such as service account tokens, in order to perform lateral movements. For instance, in many Kubernetes attacks, once the attacker gains entry into a pod, they may attempt to use a service account token to access other entities.
[**Examples:** Credential Access, Comand Injection, etc.]

## Tags
- CIS_v1.27
- Control-Id-5.1.6

## Policy Templates
### Service account token
```yaml
apiVersion: security.kubearmor.com/v1
kind: KubeArmorPolicy
metadata:
  name: ksp-wordpress-block-service-account
  namespace: wordpress-mysql
spec:
  severity: 2
  selector:
    matchLabels:
      app: wordpress
  file:
    matchDirectories:
      - dir: /run/secrets/kubernetes.io/serviceaccount/
        recursive: true
  action: Block
```
#### Simulation
```sh
root@wordpress-7c966b5d85-42jwx:/# cd /run/secrets/kubernetes.io/serviceaccount/ 
root@wordpress-7c966b5d85-42jwx:/run/secrets/kubernetes.io/serviceaccount# ls 
ls: cannot open directory .: Permission denied 
root@wordpress-7c966b5d85-42jwx:/run/secrets/kubernetes.io/serviceaccount# 
```

#### Expected Alert
```
root:{} 36 items
ATags:null
Action:Block
ClusterName:deathiscoming
ContainerID:bbf968e6a75f0b4412478770911c6dd05d5a83ec97ca38872246e89c31e9d41a
ContainerImage:docker.io/library/wordpress:4.8-apache@sha256:6216f64ab88fc51d311e38c7f69ca3f9aaba621492b4f1fa93ddf63093768845
ContainerName:wordpress
Data:syscall=SYS_OPENAT fd=-100 flags=O_RDONLY|O_NONBLOCK|O_DIRECTORY|O_CLOEXEC
Enforcer:AppArmor
HashID:4302136ade410b05b31b10edb89cccaddefba52b38771909af41f506ed87964b
HostName:aditya
HostPID:16020
HostPPID:15939
Labels:app=wordpress
Message:
NamespaceName:wordpress-mysql
Operation:File
Owner:{} 3 items
Name:wordpress
Namespace:wordpress-mysql
Ref:Deployment
PID:214
PPID:208
PodName:wordpress-7c966b5d85-42jwx
PolicyName:DefaultPosture
ProcessName:/bin/ls
Resource:/run/secrets/kubernetes.io/serviceaccount
Result:Permission denied
Severity:
Source:/bin/ls
Tags:
Timestamp:1695904106
Type:MatchedPolicy
UID:0
UpdatedTime:2023-09-28T12:28:26.604623Z
cluster_id:3664
component_name:kubearmor
instanceGroup:0
instanceID:0
workload:1
```

## References
[MITRE Steal Application Access Token](https://attack.mitre.org/techniques/T1528/)



