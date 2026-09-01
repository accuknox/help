# Network forensics
Get granular details of all the network accesses within the target workloads.

## Narrative
KubeArmor helps the organization to protect their Network level acceass from the attackers by  continuous Monitoring and Alerting the access when it's happening.

## Attack Scenario
An attacker can scan the open ports on a system by sending connection requests to a wide range of ports. This can be detected by monitoring for a large number of connection attempts to a variety of ports in a short period of time.

## Compliance
- NIST-800
- NIST_SA

## Policy
### Network Forensics
```yaml
apiVersion: security.kubearmor.com/v1
kind: KubeArmorPolicy
metadata:
  name: ksp-nist-ac-18-1-network-audit
  namespace: wordpress-mysql
spec:
  severity: 3
  tags: ["NIST-800", "AC-18(1)", "Networking", "Access", "NIST_SA", "NIST_SA-20", "NIST_SA-20-Customized Development of Critical Components", "SA"]
  message: "Access to network files detected. Possible violation of NIST Controls"
  selector:
    matchLabels:
      app: wordpress
  file:
    matchPaths:
      - path: /proc/net/tcp
      - path: /proc/net/udp
      - path: /proc/net/icmp
      - path: /proc/net/snmp
      - path: /proc/net/route
      - path: /proc/net/dev
      - path: /var/log/syslog
      - path: /var/log/audit/audit.log
      - path: /etc/hostapd/hostapd.conf
      - path: /etc/network/if-up.d
  action: Audit
```
#### Simulation
```sh
kubectl exec -it wordpress-7c966b5d85-wvtln -n wordpress-mysql -- bash
root@wordpress-7c966b5d85-wvtln:/var/www/html# cd /etc/network/if-up.d
root@wordpress-7c966b5d85-wvtln:/etc/network/if-up.d# ls
mountnfs
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
PolicyName: ksp-nist-ac-18-1-network-audit
Severity: 3
Message: Access to network files detected. Possible violation of NIST Controls
Source: /bin/ls
Resource: /etc/network/if-up.d
Operation: File
Action: Audit
Data: syscall=SYS_OPENAT fd=-100 flags=O_RDONLY|O_NONBLOCK|O_DIRECTORY|O_CLOEXEC
Enforcer: eBPF Monitor
Result: Passed
ATags: [NIST-800 AC-18(1) Networking Access NIST_SA NIST_SA-20 NIST_SA-20-Customized Development of Critical Components SA]
HostPID: 1.275441e+06
HostPPID: 1.275298e+06
Owner: map[Name:wordpress Namespace:wordpress-mysql Ref:Deployment]
PID: 342
PPID: 336
ParentProcessName: /bin/bash
ProcessName: /bin/ls
Tags: NIST-800,AC-18(1),Networking,Access,NIST_SA,NIST_SA-20,NIST_SA-20-Customized Development of Critical Components,SA
```

## References
[NIST Special Publication 800-series](https://www.nist.gov/itl/publications-0/nist-special-publication-800-series-general-information)<br />



