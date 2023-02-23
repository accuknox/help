KubeArmor supports following types of workloads:

1.K8s orchestrated workloads: Workloads deployed as k8s orchestrated containers. In this case, Kubearmor is deployed as a k8s daemonset. Note, KubeArmor supports policy enforcement on both k8s-pods (KubeArmorPolicy) as well as k8s-nodes (KubeArmorHostPolicy).

2.VM/Bare-Metals workloads: Workloads deployed on Virtual Machines or Bare Metal i.e. workloads directly operating as host processes. In this case, Kubearmor is deployed in systemd mode.

| Kubernetes Engine | OS                                 | Support   | Remarks                                                 |
| :---------------- | :--------------------------------- | : ------- | :------------------------------------------------------ |
| Google GKE        | Container Optimized OS             | Yes       | Supported across Stable/Regular/Rapid/ release channels |
| Google GKE        | Ubuntu                             | Yes       | Supported across Stable/Regular/Rapid/ release channels |
| Microsoft Azure   | Ubuntu                             | Yes       |                                                         |
| AWS EKS           | Amazon Linux 2(Kernel version 5.4) | Partial   | Observability/Audit mode is supported, Enforcement mode is supported for nodes/hosts only (not for k8s pods). |
| AWS EKS           | Amazon Linux 2(kernel version >5.7)| Yes       | Support leveraging BPF LSM                              |
| AWS EKS           | Ubuntu                             | Yes       |                                                         |
| AWS EKS           | BottleRocket                       | Yes       | Support leveraging BPF LSM                              |
| RedHat OpenShift  | Red Hat Enterprise Linux 8.4       | Partial   | Observability/Audit mode is supported, Enforcement mode is not supported. (Kernel Version: 4.18.0-305.45.1.el8_4.x86_64, Openshift Version: 4.10.14) |
| Rancher RKE       | all                                | Yes       |Supported - Except RKE deployed on host using a Docker container|
| Oracle OKE           | Oracle Linux Server 8.7         | Yes       | Support leveraging BPF LSM                              |
| IBM Cloud            | Ubuntu                          | Yes       | Support leveraging APPArmor                             |
| VMWare Tanzu         | *                               | TBD       |                                                         |
| Nutanix              | *                               | TBD       |                                                         |
| AWS Graviton(ARM Instances)|Ubuntu                     | Yes       | Supported across Stable/Regular/Rapid/ release channels. Enforced using AppArmor.|
| AWS Graviton(ARM Instances)|Amazon Linux 2(kernel 5.10)| Partial   | Audit/Observability mode is supported.                   |


| Provider          | Distro                       | VM / Bare-metal | Kubernetes      |
| :---------------- | :----------------------------| :---------------| :---------------|
| SUSE              | SUSE Enterprise 15           | Full            | Full            |
| Debian            | Buster / Bullseye            | Full            | Full            |
| Ubuntu            | 18.04 / 16.04 / 20.04        | Full            | Full            |
| RedHat / CentOS   | RHEL 8.4 / CentOS 8.4        | Full            | Partial         |
| RedHat            | RHEL9/RHEL>=8.5/CentOS8 Steam| Full            | Full            |
| Fedora            | Fedora 34 / 35               | Full            | Full            |
| Rocky Linux       | Rocky Linux >= 8.5           | Full            | Full            |