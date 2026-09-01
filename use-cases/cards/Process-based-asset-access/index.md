# Process based asset access
Allow only specific processes to access sensitive assets, deny/audit everything else.

## Narrative
You can use a security feature called "process isolation" or "process whitelisting" to set specific processes to access specific assets in a container or pod and deny everything else. This can help to secure a containerized environment by limiting the processes that can access the assets within it and preventing unauthorized processes from accessing those assets.

## Attack Scenario
An attacker uses different attack techniques to change configuration files. Process-based asset access will deny any unknown process from accessing the configuration files.<br /> **Attack Type** Credential access, Data manipulation

## Compliance
- Process based asset access

## Policy
### Process based asset access
```yaml
apiVersion: security.kubearmor.com/v1
kind: KubeArmorPolicy
metadata:
  name: only-allow-nginx-exec
  namespace: default
spec:
  selector:
    matchLabels:
      app: nginx
  file:
    matchDirectories:
    - dir: /
      recursive: true
    - dir: /etc/nginx/
      recursive: true
      fromSource:
      - path: /usr/sbin/nginx
    - dir: /etc/nginx/
      recursive: true
      fromSource:
      - path: /usr/bin/cd
    - dir: /etc/nginx/
      recursive: true
      readOnly: true
      action: Block
  process:
    matchPaths:
    - path: /usr/sbin/nginx
    - path: /usr/bin/bash
  message: process-based-asset-access
  action: Allow
```
#### Simulation
```sh
kubectl exec -it nginx-77b4fdf86c-x7sdm -- bash
root@nginx-77b4fdf86c-x7sdm:/# cd /etc/nginx/
root@nginx-77b4fdf86c-x7sdm:/etc/nginx# ls
bash: /usr/bin/ls: Permission denied
root@nginx-77b4fdf86c-x7sdm:/etc/nginx#
```

#### Expected Alert
```
{
  "Action": "Block",
  "ClusterName": "0-trust",
  "ContainerID": "20a6333c6a46e0da32b3062f0ba76e9aed4fc5ef51f5ee8aec5b980963cedea3",
  "ContainerImage": "docker.io/library/nginx:latest@sha256:32da30332506740a2f7c34d5dc70467b7f14ec67d912703568daff790ab3f755",
  "ContainerName": "nginx",
  "Data": "syscall=SYS_EXECVE",
  "Enforcer": "eBPF Monitor",
  "HostName": "aditya",
  "HostPID": 70701,
  "HostPPID": 70666,
  "Labels": "app=nginx",
  "NamespaceName": "default",
  "Operation": "Process",
  "Owner": {
    "Name": "nginx",
    "Namespace": "default",
    "Ref": "Deployment"
  },
  "PID": 444,
  "PPID": 439,
  "ParentProcessName": "/usr/bin/bash",
  "PodName": "nginx-77b4fdf86c-x7sdm",
  "PolicyName": "DefaultPosture",
  "ProcessName": "/usr/bin/ls",
  "Resource": "/usr/bin/ls",
  "Result": "Permission denied",
  "Source": "/usr/bin/bash",
  "Timestamp": 1696587116,
  "Type": "MatchedPolicy",
  "UpdatedTime": "2023-10-06T10:11:56.694009Z",
  "cluster_id": "4291",
  "component_name": "kubearmor",
  "instanceGroup": "0",
  "instanceID": "0",
  "tenant_id": "167",
  "workload": "1"
}
```





