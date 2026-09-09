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