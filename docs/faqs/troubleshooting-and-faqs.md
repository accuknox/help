---
hide:
  - toc
---

## **AccuKnox FAQs:** 

**1. Do AccuKnox CNAPP support an agent-based scanning or agentless scanning ?**

For CSPM, AccuKnox support agentless scanning for Public Cloud Infrastructure. For Infrastructure behind a firewall or Private Cloud, AccuKnoxCSPM leverages open source based agent to manage remote nodes for Automated reporting, Error log Delivery, Microservice Monitoring, User Shell Activity, Resource Monitoring.


For CWPP, AccuKnox leverage open source CNCF sandbox project KubeArmor for scanning and in-line mitigation from known attacks. Together we provide a complete static and runtime security for a variety of workloads whether they are on Public/Private Cloud, VM, Baremetal or pure-containerized workload.

**2. What is the differentiation of AccuKnox in Static Security?**

In the Static Security solution, unlike other CSPM tools, AccuKnox provides flexibility to integrate a variety of open source and commercial security scanning tools through built-in parsers to provide you a composite security posture of your infrastructure. We also correlate and normalize results from a variety of security scanning tools and provide detailed     results of vulnerabilities across infrastructure.

**3. How AccuKnox helps to achieve static security?**

AccuKnox Cloud Security Posture Management (CSPM) tool scans the Cloud Account to assess Vulnerabilities, Misconfigurations that are present in the cloud infrastructure based on security best practices & benchmarks. AccuKnox also enables you to handle Vulnerabilities with the ability to mark false positives, Waiting for 3rd party or Accepted risk and many more, so that you get to act on findings that are remediable and containing the SLA. We also give comprehensive compliance reports based on various security governance for third party assessment operators (3PAO) auditing.
	
**4. How AccuKnox helps to achieve Runtime security?**

AccuKnox’s Cloud Workload Protection Platform (CWPP) achieves runtime security by leveraging CNCF sandbox project, KubeArmor, which is a cloud-native runtime security enforcement system by AccuKnox that restricts and have more granular control over the application behavior such as process execution, file access, and networking operation of containers and nodes at the system level.

**5. What is the differentiation of AccuKnox in Runtime Security?**

AccuKnox leverages KubeArmor, which is a cloud-native runtime security enforcement system that leverages Linux Security Modules to secure the workloads. LSMs are really powerful but they weren’t built with modern workloads including Containers and Orchestrators in mind. Hence, eBPF has provided us with the ability to extend capabilities and BPF LSM provide us with the ability to load our custom programs with decision-making into the kernel seamlessly helping us protect modern workloads. Therefore, KubeArmor helps to enforce security posture wherein any malicious attacks will be stopped before execution, known as in-line mitigation (mentioned by Forrester report)

**6. What does KubeArmor leverage for enforcement and what are its advantages?**

KubeArmor leverages best of breed Linux Security Modules (LSMs) such as AppArmor, BPF-LSM, and SELinux for inline mitigation to reduce the attack surface of the pod/container/VM.LSMs have several advantages over any other techniques. By using LSMs, KubeArmor does not have to disturb pods/containers and also doesn't require change at host or CRI level to apply security policies. 

KubeArmor deploys as a non-privileged daemonset with certain capabilities that allows it to monitor other pods/containers and host. A given cluster can have multiple nodes utilizing different LSMs so KubeArmor abstracts away the complexities of the LSMs and provides an easy way for policy enforcement.

**7. What are the integration tools that are supported by AccuKnox?**

AccuKnox can integrate multiple Cloud Account, Registries, SIEM platform, Ticketing or Notifications Tools and the list is ever growing. AccuKnox is pretty flexible to support the progression of the list with the customer’s request as our roadmap item. Some of the supported today are as follows:

+ Security Events/SIEM : Splunk, Rsyslog, AWS CloudWatch, Elastic Search, Webhooks

+ Notification Tools: Slack, Jira, PagerDuty, Emails

+ Ticketing Tools: Jira, FreshService, Connectwise, Zendesk,

+ Registries: Nexus, ECR, GCR, DockerHub 

**8. How AccuKnox helps in Policy Version Control for Runtime Security?**

Accknox enables DevSecOps teams to embed security policies as code into their GitOps workflow. This provides a unified, collaborative view of the policies and enables them to be shipped and deployed along with the applications they are protecting. Hence, utilizing Gitops based policy version control, it will be easy to enforce changes to policies and keep track of versions in case of audit or rollback requirement alongwith approval mechanisms.

**9. How AccuKnox helps to achieve Microsegmentation?**

AccuKnox CWPP provides micro-segmentation at the lowest possible granularity level which is also a smallest execution unit in Kubernetes i.e. Pods. We will help you to identify process execution request from the pods, network connections the pods are trying to make internally or externally and files-system the pods are accessing. By observing the behavior of a particular pod and restricting that behavior so that it functions according  to the expected flow of process/events/traffic, one can develop a least permissive security posture from creating a whitelisting policies and auditing/denying everything else.


**10. How AccuKnox helps to recommend Auto-Discovered Policies?**

AccuKnox CWPP solution provide Discovery Engine agent that assesses the security posture of your workloads and auto-discovers the policy-set required to put the workload in least-permissive mode. We also provide Shared Informer Agent which collects information about cluster like pods, nodes, namespaces etc. The Policy Discovery Engine discovers the policies using the workload and cluster  information that is relayed by Shared Informer Agent.

**11. What are Hardening Policies?**

KubeArmor is a security solution for the Kubernetes and cloud native platforms that helps protect your workloads from attacks and threats. It does this by providing a set of hardening policies that are based on industry-leading compliance and attack frameworks such as CIS, MITRE, NIST-800-53, and STIGs. These policies are designed to help you secure your workloads in a way that is compliant with these frameworks and recommended best practices.

**12. What is Network Segmentation?**

In Kubernetes, the network policy resource is a set of network traffic rules that are applied to a group of pods in a Kubernetes cluster. The network policy specifies how a pod is allowed to communicate with others. Network policy controllers (running as pods in the Kubernetes cluster) convert the requirements and restrictions of the network policies that are retrieved from the Kubernetes API into the network infrastructure.

**13. How AccuKnox helps to implement Zero Trust?**


By implementing a zero trust posture with KubeArmor, organizations can increase their security posture and reduce the risk of unauthorized access or activity within their Kubernetes clusters. This can help to protect sensitive data, prevent system breaches, and maintain the integrity of the cluster.
KubeArmor supports allow-based policies which result in specific actions to be allowed and denying/auditing everything else. For example, a specific pod/container might only invoke a set of binaries at runtime. As part of allow-based rules you can specify the set of processes that are allowed and everything else is either audited or denied based on the default security posture.

**14. Does KubeArmor only support Kubernetes or it can support on-prem deployments like legacy VM, pure containerized workload as well?**

KubeArmor supports following types of workloads: 

+ K8s orchestrated workloads: Workloads deployed as k8s orchestrated containers. In this case, KubeArmor is deployed as a k8s daemonset. Note, KubeArmor supports policy enforcement on both k8s-pods (KubeArmorPolicy) as well as k8s-nodes (KubeArmorHostPolicy).
+ VM/Bare-Metals workloads: Workloads deployed on Virtual Machines or Bare Metal i.e. workloads directly operating as host processes. In this case, KubeArmor is deployed in systemd mode.

**15. How AccuKnox helps achieve protection for Edge, 5G workloads?**

With edge computing shifting towards containerized workloads and in few cases to orchestrated kubernetes workloads, it becomes important to have a security solution which can not only provide enforcement into different forms of deployment but can also provide real-time container-rich observability.
KubeArmor supporting un-orchestrated containers, k8s workloads and bare metal VMs makes it an ideal universal engine. Its kernel-level runtime security enforcement and container aware observability brings the best of both worlds..

**16. What is the difference between Post-attack mitigation and in-line mitigation and which is better?**

Post-exploit Mitigation works by killing the suspicious process in response to an alert indicating malicious intent. In this case attacker will be allowed to is able to execute its binary and could possibly disable the security controls, access logs, etc to circumvent the attack detection. By the time the malicious process is killed, it might have already deleted, encrypted, or transmitted the sensitive contents. 

![](/faqs/images/post-attack-mitigation.png)

Inline Mitigation on the other hand prevents the malicious attack at the time of happening itself. It doesn’t allow the attack to happen by protecting the environment with security policy or firewall. AccuKnox’s open source tool KubeArmor provides Inline Mitigation. KubeArmor uses inline mitigation to reduce the attack surface of pod/container/VM. KubeArmor leverages best of breed Linux Security Modules (LSMs) such as AppArmor, BPF-LSM, and SELinux (only for host protection) for inline mitigation

**17.What role does AccuKnox Agents play in runtime-security?**

AccuKnox Enterprise version consists of various agents such as 

**KubeArmor:**  KubeArmor is a cloud-native runtime security enforcement system that restricts the behavior (such as process execution, file access, and networking operation) of containers and nodes at the system level. KubeArmor dynamically set the restrictions on the pod. KubeArmor leverages Linux Security Modules (LSMs) to enforce policies at runtime.

**Feeder Service:** It collects the feeds from kubeArmor and relays to the app. 

**Shared Informer Agent:** It collects information about the cluster like pods, nodes, namespaces etc., 

**Policy Discovery Engine:** It discovers the policies using the workload and cluster information that is relayed by a shared informer Agent. 


## **Bonus Questions :**

**1. What are all the compliance frameworks that AccuKnox is covering?**

AccuKnox’s CNAPP tool checks for compliance and governance from various benchmarks like STIG, CIS, NIST CSF, HIPAA, MITRE, SOC2, CMMC, Fisma . 

**2. Does Inline remediation slowdown the process?**

LSMs are already enabled in the environment and use host based LSM security. Since the attacker usually has direct access to the pod, AccuKnox uses Inline remediation to stop the processes before executing. Therefore, inline remediation does not slow down the process

**3. What does AccuKnox measure, while doing security posture observation?**

+ Compliance Frameworks (MITRE, CIS, NIST) for hardening workloads
+ Understanding the Application behaviour using LSMs
+ Hardening policies are blocked based policies
+ Behavioural policies are allow based policies
+ Showcasing an example of FIM (File Integrity Monitoring) policy

**4. Do you have any standard hardening rules onboarded and will the hardening policy show what is getting blocked?**

Yes, it can show up in terms of Application Behaviour & Logs

**5. What is the deployment architecture?** 

When using AccuKnox SAAS enterprise, Agents like: KubeArmor, Policy Enforcement 
etc get deployed. If you would like to install on-prem and keep the telemetry 
unexposed, it can still be possible

**6. Where is AccuKnox SAAS is located?**

Currently it is located in US region

**7. Is there a support for CIEM?**

It is as part of the roadmap, like IOT edge, 5G Security

**8. What will happen to my application running on a VM?**

 You get hardening policies via AccuKnox enforcement engine KubeArmor

**9. What is AccuKnox’s licensing model?**

If it is a end customer - https://www.accuknox.com/accuknox_sla
If it is a MSSP model, it is a revenue share

**10. How do you work with resellers and partnership models?**

We have a 100% partner aligned go to market approach. to this goal, we provide our partners the following

+ Free training, certification
+ Joint marketing
+ Lead sharing

**11. Current AccuKnox's marketplace listing?**

We are in the process of listing on

+ AWS
+ Azure
+ GCP
+ Oracle
+ VMWare
+ IBM/OpenShift

**12. Who are current AccuKnox's partners and resellers?**

+ We have a global partnership with TCS
+ We have a reseller partnership with Ambisure

