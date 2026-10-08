# Restrict Capabilities
Do not allow capabilities that can be leveraged by the attacker.

## Narrative
Containers run with a default set of capabilities as assigned by the Container Runtime. Capabilities are parts of the rights generally granted on a Linux system to the root user. In many cases applications running in containers do not require any capabilities to operate, so from the perspective of the principal of least privilege use of capabilities should be minimized.

## Attack Scenario
Kubernetes by default connects all the containers running in the same node (even if they belong to different namespaces) down to Layer 2 (ethernet). Every pod running in the same node is going to be able to communicate with any other pod in the same node (independently of the namespace) at ethernet level (layer 2). This allows a malicious containers to perform an ARP spoofing attack to the containers on the same node and capture their traffic.<br /> **Attack Type** Reconnaissance, Spoofing<br /> **Actual Attack** Recon through P.A.S. Webshell, NBTscan

## Compliance
- CIS Kubernetes
- Control Id: 5.2.8 - Minimize the admission of containers with the NET_RAW capability
- Control Id: 5.2.9 - Minimize the admission of containers with capabilities assigned

## Policy
### Restrict Capabilities
```yaml
apiVersion: security.kubearmor.com/v1
kind: KubeArmorPolicy
metadata:
  name: ksp-ubuntu-1-cap-net-raw-block
  namespace: multiubuntu
spec:
  severity: 1
  selector:
    matchLabels:
      container: ubuntu-1
  capabilities:
    matchCapabilities:
    - capability: net_raw
  action:
    Block
```
#### Simulation
```sh
root@ubuntu-1-deployment-f987bd4d6-xzcb8:/# tcpdump
tcpdump: eth0: You don't have permission to capture on that device
(socket: Operation not permitted)
root@ubuntu-1-deployment-f987bd4d6-xzcb8:/#    
```

#### Expected Alert
```
{
    "Action":"Block",
    "ClusterName":"k3sn0d3",
    "ContainerID":"aaf2118edcc20b3b04a0fae6164f957993bf3c047fd8cb33bc37ac7d0175e848",
    "ContainerImage":"docker.io/kubearmor/ubuntu-w-utils:0.1@sha256:b4693b003ed1fbf7f5ef2c8b9b3f96fd853c30e1b39549cf98bd772fbd99e260",
    "ContainerName":"ubuntu-1-container",
    "Data":"syscall=SYS_SOCKET",
    "Enforcer":"AppArmor",
    "HashID":"dd12f0f12a75b30d47c5815f93412f51b259b74ac0eccc9781b6843550f694a3",
    "HostName":"worker-node02",
    "HostPID":38077,
    "HostPPID":38065,
    "Labels":"container=ubuntu-1 group=group-1",
    "Message":"",
    "NamespaceName":"multiubuntu",
    "Operation":"Network",
    "Owner":{
        "Name":"ubuntu-1-deployment",
        "Namespace":"multiubuntu",
        "Ref":"Deployment"
    },
    "PID":124,
    "PPID":114,
    "PodName":"ubuntu-1-deployment-f987bd4d6-xzcb8",
    "PolicyName":"ksp-ubuntu-1-cap-net-raw-block",
    "ProcessName":"/usr/sbin/tcpdump",
    "Resource":"domain=AF_PACKET type=SOCK_RAW protocol=768",
    "Result":"Operation not permitted",
    "Severity":"1",
    "Source":"/usr/sbin/tcpdump",
    "Tags":"",
    "Timestamp":1705405378,
    "Type":"MatchedPolicy",
    "UID":0,
    "UpdatedTime":"2024-01-16T11:42:58.662928Z",
    "UpdatedTimeISO":"2024-01-16T11:42:58.662Z",
    "cluster_id":"16402",
    "component_name":"kubearmor",
    "instanceGroup":"0",
    "instanceID":"0",
    "workload":"1"
}
```

## References
[MITRE Network Service Discovery](https://attack.mitre.org/techniques/T1046/)<br />



