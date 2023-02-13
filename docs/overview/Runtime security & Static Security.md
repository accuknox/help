Static Security: 
Static Security in the cloud is the process of identifying the vulnerabilities and misconfigurations present in the cloud resources. In the static security part the cloud resources are scanned for vulnerabilities and misconfigurations based on security benchmarks and frameworks. 

AccuKnox Cloud Security Posture Management (CSPM) tool scans the Cloud Account to assess Vulnerabilities, Misconfigurations that are present in the cloud infrastructure based on security best practices & benchmarks. AccuKnox also enables you to handle Vulnerabilities with the ability to mark false positives, Waiting for 3rd party or Accepted risk and many more, so that you get to act on findings that are remediable and containing the SLA. We also give comprehensive compliance reports based on various security governance for third party assessment operators (3PAO) auditing.

Accuknox CSPM tool supports both agentless scanning and agent-based Vulnerabilitiy scanning. AccuKnox CSPM does not require any agent for Public Cloud Infrastructure scan as it leverages security tools of these clouds itself. However, to scan Infrastructure behind a firewall or Private Cloud, it leverages open source based Saltstack’s minion (agent) which helps to manage remote nodes for Automated reporting, Error log Delivery, Microservice Monitoring, User Shell Activity, Resource Monitoring. 

Runtime Security: 
In the runtime or dynamic security, the cloud workloads are prevented from the malicious attacks, vulnerability exploits by using the various tools. In the runtime cloud workloads are prevented from the attack by 

Modern Kubernetes and other cloud applications include:
Dozens of open source libraries, all of which come with inherent supply chain risks; Example a recent study found that more than half the docker images had some vulnerability.

It is not entirely common but sometimes unpatched vulnerabilities, or misconfigurations slip through in production

Zero-day attacks that create chaos as workloads can be compromised until a patch has been applied.

In such a scenario, applications can be compromised and once they are, they can initiate a wide range of malicious activity even if not running as a root.

AccuKnox’s Cloud Workload Protection Platform (CWPP) achieves runtime security by leveraging CNCF sandbox project, KubeArmor, which is a cloud-native runtime security enforcement system by AccuKnox that restricts and have more granular control over the application behavior (such as process execution, file access, and networking operation) of containers and nodes at the system level. With KubeArmor, a user can:

restrict file system access for certain processes

restrict what processes can be spawned within the pod

restrict the capabilities that can be used by the processes within the pod

Some of the use cases are: 

Prevents (detects) backdoor fetch-store-exec operations from subverted process or embedded malicious logic

Prevents unauthorized network Interface usage

Prevents unauthorized file system manipulations

Prevents unauthorized process execution, termination, thread hijacking

Prevents unauthorized administrative functions and command invocations

Introduces strong identity management for all cross-container communications

Produces fine-grain app-level audits and alerts for all permission violations

Accuknox’s CWPP provides runtime security for your Kubernetes workloads to prevent malicious activity as determined by MITRE and other indicators of compromise and stops your workload from behaving maliciously at runtime. This gives you the necessary guardrails to restrict application behavior within a set of predefined policies while you apply a patch. Unlike traditional solutions that recommend a full quarantine of the workloads, accuknox's runtime solution can provide you active runtime protection allowing you to only restrict the malicious behavior as opposed to the entire workload.