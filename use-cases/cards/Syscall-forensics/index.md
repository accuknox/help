# Syscall forensics
Get granular details of all the security sensitive system calls within the target workloads.

## Narrative
KubeArmor can continuously monitor and alert on sensitive syscalls in real time, providing the necessary information to investigate and respond to potential attacks. This is done by auditing the syscalls that are executed on the system and looking for suspicious activity.

## Attack Scenario
An attacker who can control the unlink, chown, and chroot syscalls can delete a large number of files, including system configuration files and user data. The unlink syscall deletes a file. The chown syscall changes the ownership of a file or directory. The chroot syscall changes the root directory for the current process and all of its child processes. This could be prevented by auditing these syscalls by KubeArmor.

## Compliance
- CIS-4.4
- NIST-4.4
- MITRE-T1602

## Policy
### Syscall Forensics
```yaml
apiVersion: security.kubearmor.com/v1
kind: KubeArmorPolicy
metadata:
  name: Auditing Syscalls 
  namespace: wordpress-mysql
spec:
  action: Audit
  message: Warning! Syscall Alert
  syscalls:
    matchSyscalls:
    - syscall:
      - unlink
      - chmod
      - chown
      - chroot
      - mount
      - ptrace
      - kill
      - swapoff
      - syslog
      - sethostname
  selector:
    matchLabels:
      app: wordpress
  tags : ["CIS-4.4,4.3,4.12", "NIST-4.4,4.3,4.12", "MITRE-T1602"]
```
#### Simulation
```sh
kubectl exec -it wordpress-7c966b5d85-wvtln -n wordpress-mysql -- bash
root@wordpress-7c966b5d85-wvtln:/var/www/html# ls
index.php    readme.html      wp-blog-header.php    wp-config.php  wp-includes        wp-login.php    myfile.txt        
root@wordpress-7c966b5d85-wvtln:/var/www/html# unlink myfile.txt
root@wordpress-7c966b5d85-wvtln:/var/www/html# ls
index.php    readme.html      wp-admin            wp-comments-post.php  wp-config.php  wp-cron.php  wp-links-opml.php  wp-login.php  wp-settings.php  wp-trackback.php
```

#### Expected Alert
```
ClusterName: default
HostName: gke-cluster-1-default-pool-37f4c896-8cn6
NamespaceName: wordpress-mysql
PodName: wordpress-7c966b5d85-wvtln
Labels: app=wordpress
ContainerName: wordpress
ContainerID: 6d09394a988c5cf6b9fe260d28fdd57d6ff281618869a173965ecd94a3efac44
ContainerImage: docker.io/library/wordpress:4.8-apache@sha256:6216f64ab88fc51d311e38c7f69ca3f9aaba621492b4f1fa93ddf63093768845
Type: MatchedPolicy
PolicyName: auditing-syscalls
Severity: 1
Message: Warning! Syscall Alert
Source: /usr/bin/unlink myfile.txt
Resource: /var/www/html/myfile.txt
Operation: Syscall
Action: Audit
Data: syscall=SYS_UNLINK
Result: Passed
ATags: [CIS-4.4 4.3 4.12 NIST-4.4 4.3 4.12 MITRE-T1602]
HostPID: 741541
HostPPID: 739395
Owner: map[Name:wordpress Namespace:wordpress-mysql Ref:Deployment]
PID: 278
PPID: 261
ParentProcessName: /bin/bash
ProcessName: /usr/bin/unlink
Tags: CIS-4.4,4.3,4.12,NIST-4.4,4.3,4.12,MITRE-T1602
```

## References
[CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks)<br />[MITRE Data from Configuration Repository](https://attack.mitre.org/techniques/T1602/)<br />



