# Process Whitelisting
Allow only specific processes to execute, deny/audit everything else.

## Narrative
You can use a security feature called "process isolation" or "process whitelisting" to set specific processes to be executed as part of a container or pod and deny everything else. This can help to secure a containerized environment by limiting the processes that can run within it and preventing unauthorized processes from being executed.

## Attack Scenario
An attacker uses command injection techniques to insert binaries in the pods/workloads and then execute the binary. Process-Whitelisting will deny any unknown process from execution.<br /> **Attack Type** Credential Access, Command Injection

## Compliance
- Process Whitelisting

## Policy
### Process Whitelisting
```yaml
apiVersion: security.kubearmor.com/v1
kind: KubeArmorPolicy
metadata:
  name: allow-specific-process
  namespace: default
spec:
  action: Allow
  file:
    matchDirectories:
      - dir: /
        recursive: true
  process:
    matchPaths:
      - path: /bin/bash
      - fromSource:
          - path: /bin/dash
        path: /bin/ping
      - fromSource:
          - path: /usr/sbin/apache2
        path: /bin/sh
      - path: /usr/sbin/apache2
  selector:
    matchLabels:
      app: dvwa-web
      tier: frontend
  severity: 1
```
#### Simulation
Set the default security posture to default-deny

```sh
kubectl annotate ns default kubearmor-file-posture=block --overwrite
```

```sh
kubectl exec -it dvwa-web-566855bc5b-xtgwq -- bash
root@dvwa-web-566855bc5b-xtgwq:/var/www/html# ping
bash: /bin/ping: Permission denied
```

#### Expected Alert
```
{
  "Action": "Block",
  "ClusterName": "0-trust",
  "ContainerID": "20a6333c6a46e0da32b3062f0ba76e9aed4fc5ef51f5ee8aec5b980963cedea3",
  "ContainerImage": "docker.io/library/nginx:latest@sha256:32da30332506740a2f7c34d5dc70467b7f14ec67d912703568daff790ab3f755",
  "ContainerName": "nginx",
  "Data": "syscall=SYS_SOCKET",
  "Enforcer": "eBPF Monitor",
  "HostName": "aditya",
  "HostPID": 84245,
  "HostPPID": 84127,
  "Labels": "app=nginx",
  "NamespaceName": "default",
  "Operation": "Network",
  "Owner": {
    "Name": "nginx",
    "Namespace": "default",
    "Ref": "Deployment"
  },
  "PID": 1032,
  "PPID": 1023,
  "ParentProcessName": "/usr/bin/bash",
  "PodName": "nginx-77b4fdf86c-x7sdm",
  "PolicyName": "DefaultPosture",
  "ProcessName": "/usr/bin/ping",
  "Resource": "domain=AF_INET type=SOCK_DGRAM|SOCK_NONBLOCK|SOCK_CLOEXEC protocol=0",
  "Result": "Permission denied",
  "Source": "/usr/bin/ping www.google.com",
  "Timestamp": 1696591999,
  "Type": "MatchedPolicy",
  "UpdatedTime": "2023-10-06T11:33:19.956684Z",
  "cluster_id": "4291",
  "component_name": "kubearmor",
  "instanceGroup": "0",
  "instanceID": "0",
  "tenant_id": "167",
  "workload": "1"
}
```





