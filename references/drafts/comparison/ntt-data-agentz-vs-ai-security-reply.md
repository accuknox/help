**Subject:** Re: AccuKnox AI Security Comparative Matrix, AgentZ and the AI Security Modules

Xue-san,

Thank you for the follow-up. Short answer: for your existing AI agents, use the AI Security modules, starting with AI-SPM. AgentZ alone covers only the agents that run on AgentZ.

**Why AgentZ alone is not enough for existing agents**

AgentZ runs agents and limits what they can reach. It is not a CNAPP and has no cloud posture scanner, as the [AgentZ FAQ](https://docs.agentzharness.ai/faq/) states. So AgentZ cannot find or inspect an agent that runs in Copilot Studio, Azure AI Foundry or Bedrock AgentCore. [AI-SPM](https://help.accuknox.com/how-to/aiml-overview/) does that.

| Need | Existing agents on other platforms | Agents that run on AgentZ |
| --- | --- | --- |
| Discovery | AI-SPM, through a read-only cloud connection. It finds agents on Copilot Studio, Microsoft 365 Agents, Azure AI Foundry, Bedrock AgentCore and Bedrock Agent, see the [v3.5 notes](https://help.accuknox.com/getting-started/3.5-release/). | Not needed. You create the agent in AgentZ. |
| Observability | AI-SPM shows each agent's memory configuration, deployment timeline, IAM role and knowledge bases. Prompt Firewall logs each prompt and response it intercepts. | Lens shows runtime telemetry, including [Allowed and Blocked network events](https://docs.agentzharness.ai/concepts/security-model/). Each run keeps a replayable trace. |
| Detection | [AI-DR](https://help.accuknox.com/use-cases/aidr/) reads AWS CloudTrail, Azure Event Hub and GCP logging. | Each blocked call lands in the audit trace. |
| Protection | [Prompt Firewall](https://help.accuknox.com/use-cases/prompt-firewall-overview/) blocks in the request path. [ModelArmor](https://help.accuknox.com/use-cases/modelarmor/) blocks at runtime. AI-DR does not block. | Default-deny network policy, secrets held outside the agent, and prompt firewalling on the Pro plan and above, see the [AgentZ product page](https://accuknox.com/platform/agentz/). |

In the matrix, AgentZ counts toward the Agentic AI Security module.

**Where blocking has limits**

Prompt Firewall blocks the traffic that passes through it, such as the browser extension, a gateway, LiteLLM or Bifrost. ModelArmor blocks on the workloads where it runs. For an agent hosted inside a SaaS platform, the blocking path depends on that platform. We can review yours together. See the [architecture page](https://help.accuknox.com/getting-started/ai-security-arch/).

**What we suggest for Guardian Agent**

1. Start with AI-SPM to find and assess your existing agents.
2. Add AI-DR for detection.
3. Add Prompt Firewall or ModelArmor where you need blocking.
4. Use [AgentZ](https://help.accuknox.com/agentz/) for new agents. It can also wrap an existing LangGraph or CrewAI agent.

So Guardian Agent over existing agents is a combination of AI Security modules. AgentZ alone is enough only for agents that run on AgentZ.

Two questions will help us size this. Which platforms do your existing agents run on? Do you need detection only, or blocking too?

Best regards,
John Kirch
