---
hide:
  - toc
---


# **AccuKnox Agents:**

## **KubeArmor:**
KubeArmor is a cloud-native runtime security enforcement system that restricts the behavior (such as process execution, file access, and networking operation) of containers and nodes at the system level. It operates with Linux security modules LSMs, meaning that it can work on top of any Linux platforms (such as Alpine, Ubuntu, and Container-optimized OS from Google) if Linux security modules (e.g., AppArmor, SELinux, or BPF-LSM) are enabled in the Linux Kernel. KubeArmor will use the appropriate LSMs to enforce the required policies. 

![](/getting-started/images/kubeArmor.png)


KubeArmor allows operators to define security policies and apply them to Kubernetes. Then, KubeArmor will automatically detect the changes in security policies from Kubernetes and enforce them on the corresponding containers and nodes. If there are any violations against security policies, KubeArmor immediately generates alerts with container identities. If operators have any logging systems, it automatically sends the alerts to their systems as well.

## **Feeder Service:**
The feeder service sends information from the Client Cluster to the AccuKnox SaaS Control Plane. Feeder Service is an agent which runs on every node, collects telemetry/alert events from source systems & messages, and emits them to Messaging Cluster for Storage & Analysis.
Ways in which the Feeder service communicates to the central control plane:

+ Directly posting messages to Kafka Topic

+ List of topics (Each component has a separate topic name) on where the feeder service publishes feeds.

+ Posting via a GRPC or REST API Service

All communication between Feeder and Control plane (Kafka. etc) is encrypted using TLS. Feeder Service uses a secret key from Kubernetes secrets to be applied to it when connecting to the control plane. This secret key allows the feeder to talk to the control plane and exchange data for a particular tenant-id/workspace-id. This is an API key that is generated as part of the cluster onboarding. The feeder service will self-assess some metrics and logs and send that information to the Control plane for its own health assessment for one or more components including its own (running on nodes).The Feeder Service makes it simpler to monitor the detailed communication between each entity.

## **Shared Informer Agent:**

Shared Informer Agent watches all the changes occurring in Kubernetes entities such as Pods, Nodes, Namespaces, Endpoints, and Services.

+ Any changes to an entity can be easily tracked by the Shared Informer Agent such as the Creation of an entity, the update of an entity, and if any entity has been deleted and as soon as the changes occur to the entities, the Shared Informer Agent pushes the information to the backend.

+ The Shared Informant Agent makes it simpler to track and manage all of the entities that are present in Kubernetes as well as see changes in entities as they occur in real-time.

## **Policy Enforcement Agent:**
AccuKnox’s Policy Enforcement Agent enforces the policies by leveraging KubeArmor and Cillium. Policy Enforcement Agent not only keeps the track of the policies but is capable of doing tasks such as applying policies, denying policies, updating policies, and deleting the policies.

+ The policy enforcement agent encrypts and decrypts the policies while handing them to and from the policy provider service. It reads the specification of the policies and provides back to the policy provider service.

+ All of the changes done to the policy can be tracked granularly with the help of the Policy Enforcement Agent and Policy Gitops Flow which helps with version control and robust management of the security policies.

## **Discovery engine:** 
Accuknox policy enforcement engines based on KubeArmor and Cilium are very flexible and powerful. However, these policy engines must be fed with policies. With 10s or 100s of pods and workloads running in a cluster, it is insanely difficult to handcraft such policies. Accuknox policy auto-discovery engine leverages the pod visibility provided by KubeArmor and Cilium to auto-generate network and system policies.

![](/getting-started/images/discovery-engine.png)

AccuKnox’s Runtime security solution is able to provide full visibility into all of these application interactions with the host kernel and provide the ability to filter or restrict specific actions at runtime.

With Accuknox you can automatically discover the application interaction and network interaction (as described below) in the form of policy as code subsequently these policies can be audited or enforced at runtime giving you the ability to restrict specific behaviors of the application.

For example, you could have a policy that states the following:

Pod A cannot access the/etc/bin folder

Pod B cannot initiate ptrace i.e. trace the execution of other processes.

Pod C cannot communicate to a remote TCP server running on port 5000.

This list can be as exhaustive as you like, and these policies are enforced within the kernel using kernel primitives and technologies as listed below:

Network Security using eBPF / Cilium

+ Network runtime protection in the form of L3, L4, and L7 rules using identity (x509 certificates or K8s labels) for your K8s workloads. In K8s policies, this is implemented as a CNI using Cilium.

+ For Virtual Machine workloads, labels are used to provide host-level network policies for L3, L4, and L7.

Application security using Linux Security Modules (LSM) / [KubeArmor]

+ The Linux Security Module (LSM) framework provides a mechanism for various security checks to be hooked by new kernel extensions. It denies access to essential kernel objects, such as files, inodes, task structures, credentials, and inter-process communication objects.

+ AccuKnox supports AppArmor and SELinux as of today for its enforcement engine at runtime.


- - - 
[SCHEDULE DEMO](https://www.accuknox.com/contact-us){ .md-button .md-button--primary }