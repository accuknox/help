# Packaging tools
Deny execution of package management tools

## Narrative
Pods/Containers might get shipped with binaries which should never used in the production environments. Some of those bins might be useful in dev/staging environments but the same container image is carried forward in most cases to the production environment too. For security reasons, the devsecops team might want to disable the use of these binaries in the production environment even though the bins exists in the container. As an example, most of the container images are shipped with package management tools such as apk, apt, yum, etc. If anyone ends up using these bins in the prod env, it will increase the attack surface of the container/pod.

## Attack Scenario
In an attack scenario, adversaries may use system tools such as fsck, ip, who, apt, and others for reconnaissance and to download additional tooling from remote servers. These tools can help them gain valuable information about the system and its vulnerabilities, allowing them to carry out further attacks. It's important to be vigilant about such activities and implement security measures to prevent such attacks from happening.<br /> **Attack Type** Command Injection, Malware, Backdoor<br /> **Actual Attack**  AppleJeus, Codecov supply chain

## Compliance
- CIS Distribution Independent Linuxv2.0
- Control-Id:6.4.5
- NIST_800-53_SI-4
- NIST_800-53_CM-7(4)

## Policy
### Packaging tools execution
```yaml
apiVersion: security.kubearmor.com/v1
kind: KubeArmorPolicy
metadata:
  name: harden-mysql-pkg-mngr-exec
  namespace: wordpress-mysql
spec:
  action: Block
  message: Alert! Execution of package management process inside container is denied
  process:
    matchPaths:
    - path: /usr/bin/apt
    - path: /usr/bin/apt-get
    - path: /bin/apt-get
    - path: /sbin/apk
    - path: /bin/apt
    - path: /usr/bin/dpkg
    - path: /bin/dpkg
    - path: /usr/bin/gdebi
    - path: /bin/gdebi
    - path: /usr/bin/make
    - path: /bin/make
    - path: /usr/bin/yum
    - path: /bin/yum
    - path: /usr/bin/rpm
    - path: /bin/rpm
    - path: /usr/bin/dnf
    - path: /bin/dnf
    - path: /usr/bin/pacman
    - path: /usr/sbin/pacman
    - path: /bin/pacman
    - path: /sbin/pacman
    - path: /usr/bin/makepkg
    - path: /usr/sbin/makepkg
    - path: /bin/makepkg
    - path: /sbin/makepkg
    - path: /usr/bin/yaourt
    - path: /usr/sbin/yaourt
    - path: /bin/yaourt
    - path: /sbin/yaourt
    - path: /usr/bin/zypper
    - path: /bin/zypper
  selector:
    matchLabels:
      app: mysql
  severity: 5
  tags:
  - NIST
  - NIST_800-53_CM-7(4)
  - SI-4
  - process
  - NIST_800-53_SI-4
```
#### Simulation
```sh
kubectl exec -it mysql-74775b4bf4-65nqf -n wordpress-mysql -- bash
root@mysql-74775b4bf4-65nqf:/# apt
bash: /usr/bin/apt: Permission denied
root@mysql-74775b4bf4-65nqf:/# apt-get
bash: /usr/bin/apt-get: Permission denied
```

#### Expected Alert
```
{
  "ATags": [
    "NIST",
    "NIST_800-53_CM-7(4)",
    "SI-4",
    "process",
    "NIST_800-53_SI-4"
  ],
  "Action": "Block",
  "ClusterName": "aditya",
  "ContainerID": "b75628d4225b8071d5795da342cf2a5c03b1d67b22b40016697fcd17a0db20e4",
  "ContainerImage": "docker.io/library/mysql:5.6@sha256:20575ecebe6216036d25dab5903808211f1e9ba63dc7825ac20cb975e34cfcae",
  "ContainerName": "mysql",
  "Data": "syscall=SYS_EXECVE",
  "Enforcer": "AppArmor",
  "HashID": "dd573c234f68b8df005e8cd314809c8b2a23852230d397743e348bf4a03ada3f",
  "HostName": "aditya",
  "HostPID": 21894,
  "HostPPID": 16435,
  "Labels": "app=mysql",
  "Message": "Alert! Execution of package management process inside container is denied",
  "NamespaceName": "wordpress-mysql",
  "Operation": "Process",
  "Owner": {
    "Name": "mysql",
    "Namespace": "wordpress-mysql",
    "Ref": "Deployment"
  },
  "PID": 168,
  "PPID": 160,
  "PodName": "mysql-74775b4bf4-65nqf",
  "PolicyName": "harden-mysql-pkg-mngr-exec",
  "ProcessName": "/usr/bin/apt",
  "Resource": "/usr/bin/apt",
  "Result": "Permission denied",
  "Severity": "5",
  "Source": "/bin/bash",
  "Tags": "NIST,NIST_800-53_CM-7(4),SI-4,process,NIST_800-53_SI-4",
  "Timestamp": 1696318864,
  "Type": "MatchedPolicy",
  "UID": 0,
  "UpdatedTime": "2023-10-03T07:41:04.096412Z",
  "cluster_id": "3896",
  "component_name": "kubearmor",
  "instanceGroup": "0",
  "instanceID": "0",
  "workload": "1"
}
```

## References
[MITRE Installer Packages](https://attack.mitre.org/techniques/T1546/016/)
[Codecov Incident - A Supply Chain Attack](https://blog.sonatype.com/what-you-need-to-know-about-the-codecov-incident-a-supply-chain-attack-gone-undetected-for-2-months)



