**Subject:** Re: AccuKnox AI Security Comparative Matrix, AgentZ and the AI Security Modules

Xue-san,

Thank you for the follow-up. Short answer: for your existing AI agents, use the AI Security modules, starting with AI-SPM. AgentZ alone covers only the agents that run on AgentZ.

- **Discovery:** [AI-SPM](https://help.accuknox.com/how-to/aiml-overview/) finds agents on Copilot Studio, Microsoft 365, Azure AI Foundry and Bedrock AgentCore, see the [v3.5 notes](https://help.accuknox.com/getting-started/3.5-release/).
- **Observability:** AI-SPM shows each agent's configuration, IAM role and knowledge bases.
- **Detection:** [AI-DR](https://help.accuknox.com/use-cases/aidr/) reads cloud control-plane events.
- **Protection:** [Prompt Firewall](https://help.accuknox.com/use-cases/prompt-firewall-overview/) blocks in the request path. [ModelArmor](https://help.accuknox.com/use-cases/modelarmor/) blocks at runtime. AI-DR does not block. The blocking path depends on where each agent runs.

AgentZ has no posture scanner, as its [FAQ](https://docs.agentzharness.ai/faq/) states, so it cannot find agents on other platforms. Use AgentZ for new agents.

For Guardian Agent, combine the modules. Start with AI-SPM, add AI-DR, then add Prompt Firewall or ModelArmor where you need blocking.

Two questions will help us size this. Which platforms do your existing agents run on? Do you need detection only, or blocking too?

Best regards,
John Kirch
