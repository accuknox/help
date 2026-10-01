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