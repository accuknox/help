[Skip to content](https://help.accuknox.com/use-cases/modelarmor/#modelarmor-securing-agentic-ai-and-ml-models-at-runtime)

Copy page

Copy page

Copy page as Markdown for LLMs

View as Markdown ↗

View this page as plain text

Open in ChatGPT ↗

Ask questions about this page

Open in Claude ↗

Ask questions about this page

# ModelArmor - Securing Agentic AI and ML Models at Runtime [¶](https://help.accuknox.com/use-cases/modelarmor/\#modelarmor-securing-agentic-ai-and-ml-models-at-runtime "Permanent link")

**ModelArmor** is a Zero Trust security solution purpose-built to protect AI/ML/LLM workloads from runtime threats. It safeguards against the unique risks of agentic AI systems and untrusted models by sandboxing deployments and enforcing granular runtime policies.

**ModelArmor** uses KubeArmor as a sandboxing engine to keep the execution of untrusted models constrained and within required checks. AI/ML Models are essentially processes and allowing untrusted models to execute in AI environments have significant risks such as possibility of cryptomining attacks that use GPUs, remote command injections, etc. KubeArmor's preemptive mitigation mechanism provides a suitable framework for constraining the execution environment of models.

ModelArmor can be used to enforce security policies on the model execution environment.

## Why ModelArmor? [¶](https://help.accuknox.com/use-cases/modelarmor/\#why-modelarmor "Permanent link")

ModelArmor enables secure deployment of **agentic AI applications** and **ML models**, addressing critical security gaps that traditional guardrails and static scanning cannot solve.

It is designed for:

- **Agentic AI workloads** using autonomous, tool-using agents.
- **ML pipelines** importing untrusted models from public repositories.
- Environments where **guardrails alone are not sufficient**.

ModelArmor protects the **entire AI lifecycle**, from development to deployment, using **sandboxing** and **policy enforcement** to neutralize malicious behavior at runtime.

## The Problem: Security Risks in Agentic AI [¶](https://help.accuknox.com/use-cases/modelarmor/\#the-problem-security-risks-in-agentic-ai "Permanent link")

### 1\. Arbitrary Code Execution [¶](https://help.accuknox.com/use-cases/modelarmor/\#1-arbitrary-code-execution "Permanent link")

Agentic AI systems can **execute arbitrary system commands** due to their autonomy and access to tools.

- Prompt engineering can bypass LLM guardrails.
- Attackers can instruct agents to run harmful commands, download malware, or scan networks.

![](https://help.accuknox.com/use-cases/images/modelarmor/demo1.png)

![](https://help.accuknox.com/use-cases/images/modelarmor/demo2.png)

### 2\. Model Supply Chain Attacks [¶](https://help.accuknox.com/use-cases/modelarmor/\#2-model-supply-chain-attacks "Permanent link")

Malicious models uploaded to public repositories (e.g., Hugging Face) can contain embedded payloads.

- Loading such models allows **hidden code execution**, leading to system compromise and C\\&C communication.

![Code Execution Cannot Be Governed Traditionally](https://help.accuknox.com/use-cases/images/modelarmor/risk1.png)

### 3\. Prompt Injection Attacks [¶](https://help.accuknox.com/use-cases/modelarmor/\#3-prompt-injection-attacks "Permanent link")

Crafted prompts can manipulate the agent into performing unauthorized actions:

- Reading sensitive files (e.g., `/root/.aws/credentials`).
- Installing tools (`apk add nmap`) or scanning networks.
- Fetching and executing external scripts.

> Traditional container security cannot detect these because they exploit application behavior, not the container itself.

![Guardrails are not enough against sophisticated prompt engineering](https://help.accuknox.com/use-cases/images/modelarmor/risk2.png)

## The Solution [¶](https://help.accuknox.com/use-cases/modelarmor/\#the-solution "Permanent link")

![](https://help.accuknox.com/use-cases/images/modelarmor/issuesfixed.png)

### Sandboxing Agentic AI [¶](https://help.accuknox.com/use-cases/modelarmor/\#sandboxing-agentic-ai "Permanent link")

ModelArmor **isolates agentic AI apps** and ML workloads at runtime, blocking unauthorized actions even if guardrails or code reviews are bypassed.

A model you did not train carries three risks that inspection cannot fully remove:

- A hidden trigger that fires on a particular input.
- Weights poisoned during training.
- A training set poisoned before that.

Pre-deployment scanning catches the artifact-level version of these. Sandboxing contains the ones that get through, by constraining what the workload can do rather than predicting what it will do.

ModelArmor sandboxUntrusted model or AI agentOllama, vLLM, NVIDIA TritonLangGraph, n8n, MCP serversRunning on a VM, a container, or KubernetesProcess isolationBlocks an untrusted binary before it executesFile system isolation/root/.aws/credentials stays unreadableNetwork isolationBlocks raw sockets and ICMP, restricts outbound trafficDomain access isolationBlocks any domain outside the allow list

The kernel enforces each control through eBPF and Linux Security Modules, so a workload cannot negotiate past one and your application needs no code change. All four apply to on-premises model servers and locally hosted agents, on a VM, in a container, or under Kubernetes.

![Zero Trust Policy Enforcement](https://help.accuknox.com/use-cases/images/modelarmor/use3.png)

### Zero Trust Policy Enforcement [¶](https://help.accuknox.com/use-cases/modelarmor/\#zero-trust-policy-enforcement "Permanent link")

Define **fine-grained security policies** to:

- **Restrict file system access** (e.g., block `/root/.aws/credentials`).
- **Control process execution** (allow only trusted binaries).
- **Limit network activity** (disable raw sockets, ICMP, or outbound traffic).

![](https://help.accuknox.com/use-cases/images/modelarmor/use4.png)

### Automated Red Teaming [¶](https://help.accuknox.com/use-cases/modelarmor/\#automated-red-teaming "Permanent link")

Simulate adversarial scenarios like malicious model imports and prompt injections to **identify vulnerabilities pre-deployment**.

### Protection Across the Stack [¶](https://help.accuknox.com/use-cases/modelarmor/\#protection-across-the-stack "Permanent link")

ModelArmor works across frameworks and environments:

- Supports any **language runtime** or **AI framework**.
- Requires no code changes to your application.
- Lightweight and **cost-efficient**, avoiding the overhead of MicroVMs or full isolation environments.

![ModelArmor sandboxing applied from the AccuKnox control plane to local on-premises AI models such as Ollama, vLLM and NVIDIA Triton Inference Server, and to local on-premises AI agents such as LangGraph, n8n, CrewAI, OpenClaw and Strands Agents, across VMs, containers and Kubernetes](https://help.accuknox.com/assets/images/ai-security/modelarmor-onprem-coverage.webp)

![Granular Policy Enforcement for Process, Network, Volumes and AI flows](https://help.accuknox.com/use-cases/images/modelarmor/use5.png)

## **PyTorch Based Use Cases** [¶](https://help.accuknox.com/use-cases/modelarmor/\#pytorch-based-use-cases "Permanent link")

[![Pickle Code Injection PoC](https://help.accuknox.com/use-cases/icons/sql-injection.svg)\\
\\
Pickle Code Injection PoC](https://help.accuknox.com/use-cases/modelarmor-pickle-code/)

[![Adversarial Attacks on Deep Learning Models](https://help.accuknox.com/use-cases/icons/container-image-scan.svg)\\
\\
Adversarial Attacks on Deep Learning Models](https://help.accuknox.com/use-cases/modelarmor-adverserial-attacks/)

[![PyTorch App Deployment with KubeArmor](https://help.accuknox.com/use-cases/icons/cluster-misconfig-scan.svg)\\
\\
PyTorch App Deployment with KubeArmor](https://help.accuknox.com/use-cases/modelarmor-deploy-pytorch/)

## **TensorFlow Based Use Cases** [¶](https://help.accuknox.com/use-cases/modelarmor/\#tensorflow-based-use-cases "Permanent link")

### FGSM Attack on a TensorFlow Model [¶](https://help.accuknox.com/use-cases/modelarmor/\#fgsm-attack-on-a-tensorflow-model "Permanent link")

An FGSM attack manipulates input data by adding imperceptible noise, creating adversarial examples that force the TensorFlow model to misclassify (e.g., predicting “5” for an image of “2”).

Traditional container security fails here because the model and container remain unchanged. The attack happens through crafted input.

**ModelArmor Protection:**

- Proactively simulates adversarial attacks using _Automated Red Teaming_.
- Secures model behavior with input validation and anomaly detection, akin to an _LLM Prompt Firewall_ for ML workloads.
- Protects against sophisticated input-level manipulations.

![](https://help.accuknox.com/use-cases/images/modelarmor/use2.png)

### Keras Inject Attack and Apply Policies [¶](https://help.accuknox.com/use-cases/modelarmor/\#keras-inject-attack-and-apply-policies "Permanent link")

A deployed TensorFlow model in a Docker container is vulnerable to compromise via a malicious Keras Lambda layer. This attack involves:

- Installing Python inside the container or
- Copying malicious scripts (e.g., into `/tmp`) to execute unauthorized system commands.

**ModelArmor Protection:**

- Blocks unauthorized installations (e.g., Python) and filesystem modifications (e.g., writing to `/tmp`).
- Uses _Automated Red Teaming_ to detect such vulnerabilities pre-deployment.
- Isolates workloads (like TensorFlow) with _Sandboxing Agentic AI_ to prevent code injection.

![Keras Model Injection Attack Mitigation](https://help.accuknox.com/use-cases/images/modelarmor/use1.png)

## **Securing NVIDIA NIM** [¶](https://help.accuknox.com/use-cases/modelarmor/\#securing-nvidia-nim "Permanent link")

![](https://help.accuknox.com/use-cases/images/modelarmor/nvidia1.png)

![](https://help.accuknox.com/use-cases/images/modelarmor/nvidia2.png)

Securing NVIDIA NIM

Securing NVIDIA NIM

/16

With your changes

Without your changes


Two page view

Annotations


* * *

Present

Document properties


1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

Extracting text from PDF…

Was this page helpful?











Thanks for your feedback!












Thanks for your feedback! Help us improve this page by using our [feedback form](https://help.accuknox.com/use-cases/modelarmor/...).


Back to top