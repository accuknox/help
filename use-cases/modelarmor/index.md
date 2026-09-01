---
title: ModelArmor - Securing Agentic AI and ML Models at Runtime
description: ModelArmor is a security solution that helps you secure your machine learning models by enforcing security policies and best practices.
---

# ModelArmor - Securing Agentic AI and ML Models at Runtime

**ModelArmor** is a Zero Trust security solution purpose-built to protect AI/ML/LLM workloads from runtime threats. It safeguards against the unique risks of agentic AI systems and untrusted models by sandboxing deployments and enforcing granular runtime policies.

**ModelArmor** uses KubeArmor as a sandboxing engine to keep the execution of untrusted models constrained and within required checks. AI/ML Models are essentially processes and allowing untrusted models to execute in AI environments have significant risks such as possibility of cryptomining attacks that use GPUs, remote command injections, etc. KubeArmor's preemptive mitigation mechanism provides a suitable framework for constraining the execution environment of models.

ModelArmor can be used to enforce security policies on the model execution environment.

## Why ModelArmor?

ModelArmor enables secure deployment of **agentic AI applications** and **ML models**, addressing critical security gaps that traditional guardrails and static scanning cannot solve.

It is designed for:

- **Agentic AI workloads** using autonomous, tool-using agents.
- **ML pipelines** importing untrusted models from public repositories.
- Environments where **guardrails alone are not sufficient**.

ModelArmor protects the **entire AI lifecycle**, from development to deployment, using **sandboxing** and **policy enforcement** to neutralize malicious behavior at runtime.

## The Problem: Security Risks in Agentic AI

### 1. Arbitrary Code Execution

Agentic AI systems can **execute arbitrary system commands** due to their autonomy and access to tools.

- Prompt engineering can bypass LLM guardrails.
- Attackers can instruct agents to run harmful commands, download malware, or scan networks.

![](./images/modelarmor/demo1.png)

![](./images/modelarmor/demo2.png)

### 2. Model Supply Chain Attacks

Malicious models uploaded to public repositories (e.g., Hugging Face) can contain embedded payloads.

- Loading such models allows **hidden code execution**, leading to system compromise and C\&C communication.

![Code Execution Cannot Be Governed Traditionally](./images/modelarmor/risk1.png)

### 3. Prompt Injection Attacks

Crafted prompts can manipulate the agent into performing unauthorized actions:

- Reading sensitive files (e.g., `/root/.aws/credentials`).
- Installing tools (`apk add nmap`) or scanning networks.
- Fetching and executing external scripts.

> Traditional container security cannot detect these because they exploit application behavior, not the container itself.

![Guardrails are not enough against sophisticated prompt engineering](./images/modelarmor/risk2.png)

## The Solution

![](./images/modelarmor/issuesfixed.png)

### Sandboxing Agentic AI

ModelArmor **isolates agentic AI apps** and ML workloads at runtime, blocking unauthorized actions even if guardrails or code reviews are bypassed.

A model you did not train carries three risks that inspection cannot fully remove:

- A hidden trigger that fires on a particular input.
- Weights poisoned during training.
- A training set poisoned before that.

Pre-deployment scanning catches the artifact-level version of these. Sandboxing contains the ones that get through, by constraining what the workload can do rather than predicting what it will do.

<div class="ak-dia" role="img" aria-label="A ModelArmor sandbox containing an untrusted model or AI agent. Four isolation controls block actions leaving the sandbox: process isolation blocks spawning an untrusted binary, file system isolation blocks reading cloud credentials, network isolation blocks raw sockets and ICMP, and domain access isolation blocks reaching a domain outside the allow list.">
<svg viewBox="0 0 900 268" xmlns="http://www.w3.org/2000/svg">
  <rect class="hollow" x="16" y="40" width="360" height="208" rx="10" stroke-dasharray="6 4"/>
  <text class="t-acc t-h" x="32" y="64">ModelArmor sandbox</text>
  <rect class="p" x="40" y="86" width="312" height="104" rx="8"/>
  <text class="t-h" x="196" y="114" text-anchor="middle">Untrusted model or AI agent</text>
  <text class="t-s" x="196" y="140" text-anchor="middle">Ollama, vLLM, NVIDIA Triton</text>
  <text class="t-s" x="196" y="162" text-anchor="middle">LangGraph, n8n, MCP servers</text>
  <text class="t-s" x="196" y="222" text-anchor="middle">Running on a VM, a container, or Kubernetes</text>

  <g class="ln-bad">
    <path d="M376 70 H434"/><path d="M376 122 H434"/>
    <path d="M376 174 H434"/><path d="M376 226 H434"/>
    <path d="M399 64 L411 76"/><path d="M411 64 L399 76"/>
    <path d="M399 116 L411 128"/><path d="M411 116 L399 128"/>
    <path d="M399 168 L411 180"/><path d="M411 168 L399 180"/>
    <path d="M399 220 L411 232"/><path d="M411 220 L399 232"/>
  </g>

  <rect class="p" x="440" y="48" width="444" height="44" rx="8"/>
  <text class="t-h" x="456" y="68">Process isolation</text>
  <text class="t-s" x="456" y="84">Blocks an untrusted binary before it executes</text>

  <rect class="p" x="440" y="100" width="444" height="44" rx="8"/>
  <text class="t-h" x="456" y="120">File system isolation</text>
  <text class="t-s t-mono" x="456" y="136">/root/.aws/credentials stays unreadable</text>

  <rect class="p" x="440" y="152" width="444" height="44" rx="8"/>
  <text class="t-h" x="456" y="172">Network isolation</text>
  <text class="t-s" x="456" y="188">Blocks raw sockets and ICMP, restricts outbound traffic</text>

  <rect class="p" x="440" y="204" width="444" height="44" rx="8"/>
  <text class="t-h" x="456" y="224">Domain access isolation</text>
  <text class="t-s" x="456" y="240">Blocks any domain outside the allow list</text>
</svg>
</div>

The kernel enforces each control through eBPF and Linux Security Modules, so a workload cannot negotiate past one and your application needs no code change. All four apply to on-premises model servers and locally hosted agents, on a VM, in a container, or under Kubernetes.

![Zero Trust Policy Enforcement](./images/modelarmor/use3.png)

### Zero Trust Policy Enforcement

Define **fine-grained security policies** to:

- **Restrict file system access** (e.g., block `/root/.aws/credentials`).
- **Control process execution** (allow only trusted binaries).
- **Limit network activity** (disable raw sockets, ICMP, or outbound traffic).

![](./images/modelarmor/use4.png)

### Automated Red Teaming

Simulate adversarial scenarios like malicious model imports and prompt injections to **identify vulnerabilities pre-deployment**.

### Protection Across the Stack

ModelArmor works across frameworks and environments:

- Supports any **language runtime** or **AI framework**.
- Requires no code changes to your application.
- Lightweight and **cost-efficient**, avoiding the overhead of MicroVMs or full isolation environments.

![Granular Policy Enforcement for Process, Network, Volumes and AI flows](./images/modelarmor/use5.png)

## **PyTorch Based Use Cases**

::cards:: cols=3

- title: Pickle Code Injection PoC
  content:
  image: ./icons/sql-injection.svg
  url: /use-cases/modelarmor-pickle-code/

- title: Adversarial Attacks on Deep Learning Models
  content:
  image: ./icons/container-image-scan.svg
  url: /use-cases/modelarmor-adverserial-attacks/

- title: PyTorch App Deployment with KubeArmor
  content:
  image: ./icons/cluster-misconfig-scan.svg
  url: /use-cases/modelarmor-deploy-pytorch/

::/cards::

## **TensorFlow Based Use Cases**

### FGSM Attack on a TensorFlow Model

An FGSM attack manipulates input data by adding imperceptible noise, creating adversarial examples that force the TensorFlow model to misclassify (e.g., predicting “5” for an image of “2”).

Traditional container security fails here because the model and container remain unchanged. The attack happens through crafted input.

**ModelArmor Protection:**

- Proactively simulates adversarial attacks using _Automated Red Teaming_.
- Secures model behavior with input validation and anomaly detection, akin to an _LLM Prompt Firewall_ for ML workloads.
- Protects against sophisticated input-level manipulations.

![](./images/modelarmor/use2.png)

### Keras Inject Attack and Apply Policies

A deployed TensorFlow model in a Docker container is vulnerable to compromise via a malicious Keras Lambda layer. This attack involves:

- Installing Python inside the container or
- Copying malicious scripts (e.g., into `/tmp`) to execute unauthorized system commands.

**ModelArmor Protection:**

- Blocks unauthorized installations (e.g., Python) and filesystem modifications (e.g., writing to `/tmp`).
- Uses _Automated Red Teaming_ to detect such vulnerabilities pre-deployment.
- Isolates workloads (like TensorFlow) with _Sandboxing Agentic AI_ to prevent code injection.

![Keras Model Injection Attack Mitigation](./images/modelarmor/use1.png)

## **Securing NVIDIA NIM**

![](./images/modelarmor/nvidia1.png)

![](./images/modelarmor/nvidia2.png)

<div>
  <iframe id="inlineFrameManual"
      title="Inline Frame Manual"
      width="150%"
      height="850"
      src="/resources/Securing_NVIDIA_NIM.pdf">
  </iframe>
</div>
