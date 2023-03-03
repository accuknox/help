KubeArmor supports following types of workloads:

1.K8s orchestrated workloads: Workloads deployed as k8s orchestrated containers. In this case, Kubearmor is deployed as a k8s daemonset. Note, KubeArmor supports policy enforcement on both k8s-pods (KubeArmorPolicy) as well as k8s-nodes (KubeArmorHostPolicy).

2.VM/Bare-Metals workloads: Workloads deployed on Virtual Machines or Bare Metal i.e. workloads directly operating as host processes. In this case, Kubearmor is deployed in systemd mode.

[KubeArmor Support Matrix](https://docs.kubearmor.com/kubearmor/quick-links/support_matrix)