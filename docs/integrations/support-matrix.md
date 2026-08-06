---
title: Integration Support Matrix
description: Every tool AccuKnox connects to, grouped by category, including the MCP catalog, inference providers, SIEM destinations, and SaaS platforms.
hide:
  - toc
---

# Integration Support Matrix

AccuKnox connects through open formats, so the supported list runs far longer than the
page count in this section. Any SIEM that reads syslog works, as does any scanner that
emits SARIF and any server that speaks MCP. This page puts the whole surface in one view.

<div class="ak-int-stats">
  <div class="ak-int-stat"><b>174</b><span>MCP servers in the catalog, plus any MCP-compliant server you point us at</span></div>
  <div class="ak-int-stat"><b>158</b><span>inference providers, plus any OpenAI or Anthropic compatible endpoint</span></div>
  <div class="ak-int-stat"><b>Any</b><span>SIEM that accepts rsyslog, syslog, CEF, or a webhook</span></div>
  <div class="ak-int-stat"><b>130+</b><span>step-by-step integration guides in this section</span></div>
</div>

!!! tip "One format covers a whole category"

    Support for a format is support for every tool that reads it. RSyslog forwarding
    reaches any SIEM, SARIF import reaches any scanner that emits it, and CEF or webhook
    delivery covers the rest. Customers run AccuKnox with IBM QRadar and Securonix today.
    QRadar has its own guide below, and Securonix needed no new work because it reads the
    same syslog stream.

## Browse by category

=== "MCP Servers"

    AccuKnox secures and proxies MCP traffic, so every server in the catalog is available
    the moment you add it. Go to **AgentZ > MCP > Add New MCP** in the platform to see
    the live list, which updates ahead of this page.

    <div class="ak-int-grid">
      <div class="ak-int-tile"><img src="../matrix-icons/github.svg" alt="GitHub logo" loading="lazy"><small>GitHub</small></div>
      <div class="ak-int-tile"><img src="../matrix-icons/slack.svg" alt="Slack logo" loading="lazy"><small>Slack</small></div>
      <div class="ak-int-tile"><img src="../matrix-icons/notion.svg" alt="Notion logo" loading="lazy"><small>Notion</small></div>
      <div class="ak-int-tile"><img src="../matrix-icons/atlassian.svg" alt="Atlassian Rovo logo" loading="lazy"><small>Atlassian Rovo</small></div>
      <div class="ak-int-tile"><img src="../matrix-icons/linear.svg" alt="Linear logo" loading="lazy"><small>Linear</small></div>
      <div class="ak-int-tile"><img src="../matrix-icons/asana.svg" alt="Asana logo" loading="lazy"><small>Asana</small></div>
      <div class="ak-int-tile"><img src="../matrix-icons/clickup.svg" alt="ClickUp logo" loading="lazy"><small>ClickUp</small></div>
      <div class="ak-int-tile"><img src="../matrix-icons/figma.svg" alt="Figma logo" loading="lazy"><small>Figma</small></div>
      <div class="ak-int-tile"><img src="../matrix-icons/canva.svg" alt="Canva logo" loading="lazy"><small>Canva</small></div>
      <div class="ak-int-tile"><img src="../matrix-icons/stripe.svg" alt="Stripe logo" loading="lazy"><small>Stripe</small></div>
      <div class="ak-int-tile"><img src="../matrix-icons/paypal.svg" alt="PayPal logo" loading="lazy"><small>PayPal</small></div>
      <div class="ak-int-tile"><img src="../matrix-icons/hubspot.svg" alt="HubSpot logo" loading="lazy"><small>HubSpot</small></div>
      <div class="ak-int-tile"><img src="../matrix-icons/zoom.svg" alt="Zoom logo" loading="lazy"><small>Zoom</small></div>
      <div class="ak-int-tile"><img src="../matrix-icons/microsoft.svg" alt="Microsoft 365 logo" loading="lazy"><small>Microsoft 365</small></div>
      <div class="ak-int-tile"><img src="../matrix-icons/googledrive.svg" alt="Google Drive logo" loading="lazy"><small>Google Drive</small></div>
      <div class="ak-int-tile"><img src="../matrix-icons/gmail.svg" alt="Gmail logo" loading="lazy"><small>Gmail</small></div>
      <div class="ak-int-tile"><img src="../matrix-icons/googlecalendar.svg" alt="Google Calendar logo" loading="lazy"><small>Google Calendar</small></div>
      <div class="ak-int-tile"><img src="../matrix-icons/cloudflare.svg" alt="Cloudflare logo" loading="lazy"><small>Cloudflare</small></div>
      <div class="ak-int-tile"><img src="../matrix-icons/vercel.svg" alt="Vercel logo" loading="lazy"><small>Vercel</small></div>
      <div class="ak-int-tile"><img src="../matrix-icons/netlify.svg" alt="Netlify logo" loading="lazy"><small>Netlify</small></div>
      <div class="ak-int-tile"><img src="../matrix-icons/supabase.svg" alt="Supabase logo" loading="lazy"><small>Supabase</small></div>
      <div class="ak-int-tile"><img src="../matrix-icons/sentry.svg" alt="Sentry logo" loading="lazy"><small>Sentry</small></div>
      <div class="ak-int-tile"><img src="../matrix-icons/pagerduty.svg" alt="PagerDuty logo" loading="lazy"><small>PagerDuty</small></div>
      <div class="ak-int-tile"><img src="../matrix-icons/zapier.svg" alt="Zapier logo" loading="lazy"><small>Zapier</small></div>
    </div>

    Availability varies by vendor. A few providers gate access behind their own developer
    or partner enrollment, so check the provider's terms before you onboard.

    ??? note "See all 174 MCP servers in the catalog"

        <p class="ak-int-list">AWS Marketplace · AdisInsight · Adobe Experience Manager · Adobe Marketing Agent · Ahrefs · AirOps · Airtable · Airwallex Developer · Amplitude · Apollo.io · Asana · Atlassian Rovo · Attio · Aura · Base44 · Bigdata.com · BioRender · Bitly · Box · Brex · CB Insights · CData Connect AI · Calendly · Candid · Canva · Chronograph · Circleback · Clarify · Clay · ClickUp · Close · Cloudflare Developer Platform · Cloudinary · Common Room · Consensus · Contentsquare · Context7 · Coupler.io · Craft · Crossbeam · Daloopa · DevRev · Digits · DocuSeal · DocuSign · Dovetail · Dropbox · Egnyte · Enterpret Wisdom · Exa · FactSet AI-Ready Data · Fathom · Fellow.ai · Fever Event Discovery · Figma · Fireflies · Fiscal.ai · G2 · Gainsight Staircase AI · Gamma · GitHub · Gmail · Google Calendar · Google Cloud BigQuery · Google Compute Engine · Google Drive · GovTribe · Granola · Guru · Gusto · Harmonic · Harvey · Honeycomb · HubSpot · Hugging Face · Indeed · Instacart · Intercom · Intuit Credit Karma · Intuit Mailchimp · Intuit TurboTax · Jam · Jentic · Jotform · Ketryx · Klaviyo · Krisp · LILT · LSEG · LegalZoom · Linear · Local Falcon · Lorikeet · Lucid · Lumin · LunarCrush · Lusha · MSCI · MT Newswires · Magic Patterns · MailerLite · Make · Medidata · Melon · Mem · Mercury · Metaview · Microsoft 365 · Miro · Mixpanel · Moody's · Morningstar · MotherDuck · Netlify · Notion · Omni Analytics · Orion by Gravity · Outreach · PDF Viewer · PagerDuty · PayPal · PitchBook Premium · Plaid Developer Tools · PlanetScale · Play Sheet Music · PlayMCP · PostHog · Postman · Process Street · Pylon · Quartr · Ramp · Razorpay · Resy · Rillet · S&P Global · Sanity · Scholar Gateway · Sentry · SignNow · Similarweb · Slack · Sprouts Data Intelligence · Square · Stripe · Stytch · Supabase · Superhuman Mail · Supermetrics Marketing Analytics · Sybill · Synapse.org · Tango · Tavily · Three.js 3D Viewer · Ticket Tailor · Tropic · Udemy Business · Unthread · Vercel · Vibe Prospecting · Webflow · Windsor.ai · Wix · WordPress.com · Zapier · Zocks · Zoho Books · Zoho CRM · Zoho Desk · Zoho Projects · Zoom · ZoomInfo · incident.io · monday.com</p>

    To query AccuKnox from your own AI tools instead, see
    [MCP Server for AccuKnox](mcp-server.md).

=== "Inference Providers"

    The AccuKnox inference engine ships a catalog of 158 providers covering hosted APIs,
    gateways, and self-hosted runtimes.

    <div class="ak-int-grid">
      <div class="ak-int-tile"><img src="../matrix-icons/openai.svg" alt="OpenAI logo" loading="lazy"><small>OpenAI</small></div>
      <div class="ak-int-tile"><img src="../matrix-icons/anthropic.svg" alt="Anthropic logo" loading="lazy"><small>Anthropic</small></div>
      <div class="ak-int-tile"><img src="../matrix-icons/gemini.svg" alt="Google Gemini logo" loading="lazy"><small>Google Gemini</small></div>
      <div class="ak-int-tile"><img src="../matrix-icons/aws.svg" alt="Amazon Bedrock logo" loading="lazy"><small>Amazon Bedrock</small></div>
      <div class="ak-int-tile"><img src="../matrix-icons/azure.svg" alt="Azure OpenAI logo" loading="lazy"><small>Azure OpenAI</small></div>
      <div class="ak-int-tile"><img src="../matrix-icons/googlecloud.svg" alt="Vertex AI logo" loading="lazy"><small>Vertex AI</small></div>
      <div class="ak-int-tile"><img src="../matrix-icons/meta.svg" alt="Meta Llama logo" loading="lazy"><small>Meta Llama</small></div>
      <div class="ak-int-tile"><img src="../matrix-icons/mistral.svg" alt="Mistral logo" loading="lazy"><small>Mistral</small></div>
      <div class="ak-int-tile"><img src="../matrix-icons/cohere.svg" alt="Cohere logo" loading="lazy"><small>Cohere</small></div>
      <div class="ak-int-tile"><img src="../matrix-icons/xai.svg" alt="xAI logo" loading="lazy"><small>xAI</small></div>
      <div class="ak-int-tile"><img src="../matrix-icons/deepseek.svg" alt="DeepSeek logo" loading="lazy"><small>DeepSeek</small></div>
      <div class="ak-int-tile"><img src="../matrix-icons/groq.svg" alt="Groq logo" loading="lazy"><small>Groq</small></div>
      <div class="ak-int-tile"><img src="../matrix-icons/togetherai.svg" alt="Together AI logo" loading="lazy"><small>Together AI</small></div>
      <div class="ak-int-tile"><img src="../matrix-icons/cerebras.svg" alt="Cerebras logo" loading="lazy"><small>Cerebras</small></div>
      <div class="ak-int-tile"><img src="../matrix-icons/nvidia.svg" alt="Nvidia logo" loading="lazy"><small>Nvidia</small></div>
      <div class="ak-int-tile"><img src="../matrix-icons/perplexity.svg" alt="Perplexity logo" loading="lazy"><small>Perplexity</small></div>
      <div class="ak-int-tile"><img src="../matrix-icons/openrouter.svg" alt="OpenRouter logo" loading="lazy"><small>OpenRouter</small></div>
      <div class="ak-int-tile"><img src="../matrix-icons/ollama.svg" alt="Ollama Cloud logo" loading="lazy"><small>Ollama Cloud</small></div>
      <div class="ak-int-tile"><img src="../matrix-icons/huggingface.svg" alt="Hugging Face logo" loading="lazy"><small>Hugging Face</small></div>
      <div class="ak-int-tile"><img src="../matrix-icons/githubcopilot.svg" alt="GitHub Copilot logo" loading="lazy"><small>GitHub Copilot</small></div>
      <div class="ak-int-tile"><img src="../matrix-icons/codex.svg" alt="OpenAI Codex logo" loading="lazy"><small>OpenAI Codex</small></div>
      <div class="ak-int-tile"><img src="../matrix-icons/alibaba.svg" alt="Alibaba logo" loading="lazy"><small>Alibaba</small></div>
      <div class="ak-int-tile"><img src="../matrix-icons/kimi.svg" alt="Moonshot AI logo" loading="lazy"><small>Moonshot AI</small></div>
      <div class="ak-int-tile"><img src="../matrix-icons/databricks.svg" alt="Databricks logo" loading="lazy"><small>Databricks</small></div>
      <div class="ak-int-tile"><img src="../matrix-icons/snowflake.svg" alt="Snowflake Cortex logo" loading="lazy"><small>Snowflake Cortex</small></div>
    </div>

    Not in the list? Point the engine at any OpenAI-compatible or Anthropic-compatible
    endpoint and it works the same way. Codex subscriptions are supported as well.

    ??? note "See all 158 inference providers in the catalog"

        <p class="ak-int-list">302.AI · Abacus · abliteration.ai · AIHubMix · Alibaba · Alibaba (China) · Alibaba Coding Plan · Alibaba Coding Plan (China) · Alibaba Token Plan · Alibaba Token Plan (China) · Amazon Bedrock · Ambient · Anthropic · AnyAPI · Atomic Chat · Auriko · Azure · Azure Cognitive Services · Bailing · Baseten · Berget.AI · Cerebras · Chutes · Clarifai · Claudinio · CloudFerro Sherlock · Cloudflare AI Gateway · Cloudflare Workers AI · Cohere · Cortecs · CrofAI · CrossModel · D.Run (China) · Databricks · Deep Infra · DeepSeek · DigitalOcean · DInference · EmpirioLabs AI · evroc · FastRouter · Fireworks AI · FreeModel · Friendli · FrogBot · GitHub Copilot · GitHub Models · GMI Cloud · Google · Groq · Helicone · HPC-AI · Hugging Face · iFlow · Inception · Inceptron · Inference · InferX · IO.NET · Jiekou.AI · Kenari · Kilo Gateway · Kimi For Coding · KUAE Cloud Coding Plan · Lilac · Llama · LLM Gateway · LLMTR · LMStudio · LongCat · LucidQuery · Meganova · Merge Gateway · Meta · MiniMax (minimax.io) · MiniMax (minimaxi.com) · MiniMax Token Plan (minimax.io) · MiniMax Token Plan (minimaxi.com) · Mistral · Mixlayer · Moark · Model Oracle AI · ModelScope · Moonshot AI · Moonshot AI (China) · Morph · NanoGPT · NEAR AI Cloud · Nebius Token Factory · Neon · Neuralwatt · Nova · NovitaAI · Nvidia · Ollama Cloud · OpenAI · OpenAI Codex · OpenCode Go · OpenCode Zen · OpenRouter · OrcaRouter · OVHcloud AI Endpoints · Perplexity · Perplexity Agent · Pioneer · Poe · Poolside · Privatemode AI · QiHang · Qiniu · Regolo AI · Requesty · routing.run · Sakana AI · Sarvam AI · Scaleway · SiliconFlow · SiliconFlow (China) · Snowflake Cortex · STACKIT · StepFun · StepFun AI · Subconscious · submodel · Synthetic · Tencent Coding Plan (China) · Tencent Token Plan · Tencent TokenHub · The Grid AI · Tinfoil · Together AI · TrustedRouter · Umans AI · Umans AI Coding Plan · UnoRouter · Upstage · v0 · Venice AI · Vercel AI Gateway · Vertex · Vertex (Anthropic) · Vivgrid · Vultr · Wafer · Weights & Biases · xAI · Xiaomi · Xiaomi Token Plan (China) · Xiaomi Token Plan (Europe) · Xiaomi Token Plan (Singapore) · Xpersona · Z.AI · Z.AI Coding Plan · Zeldoc · Zenifra · ZenMux · Zhipu AI · Zhipu AI Coding Plan</p>

=== "SIEM and Security Events"

    These destinations have their own setup guide. Click a tile to open it.

    <div class="ak-int-grid">
      <a class="ak-int-tile" href="../splunk/"><img src="../matrix-icons/splunk.svg" alt="Splunk logo" loading="lazy"><small>Splunk</small></a>
      <a class="ak-int-tile" href="../ibm-qradar/"><img src="../matrix-icons/ibm.svg" alt="IBM QRadar logo" loading="lazy"><small>IBM QRadar</small></a>
      <a class="ak-int-tile" href="../azure-sentinel/"><img src="../matrix-icons/azure.svg" alt="Microsoft Sentinel logo" loading="lazy"><small>Microsoft Sentinel</small></a>
      <a class="ak-int-tile" href="../aws-cloudwatch/"><img src="../matrix-icons/aws.svg" alt="AWS CloudWatch logo" loading="lazy"><small>AWS CloudWatch</small></a>
      <a class="ak-int-tile" href="../rsyslog/"><img src="../matrix-icons/rsyslog.png" alt="RSyslog logo" loading="lazy"><small>RSyslog</small></a>
      <a class="ak-int-tile" href="../webhook-integration/"><img src="../matrix-icons/webhook.svg" alt="Webhook logo" loading="lazy"><small>Webhook</small></a>
    </div>

    | Destination | Ingestion method | Guide |
    |---|---|---|
    | Splunk | HTTP Event Collector, plus a KubeArmor feeder | [Splunk](splunk.md), [Splunk app setup](accuKnox-splunk-app-installation-configuration.md), [KubeArmor feeder](splunk_feeder_kubearmor.md) |
    | IBM QRadar | Webhook to a customer-side server, then Syslog | [IBM QRadar](ibm-qradar.md) |
    | Microsoft Sentinel | Feeder service, Log Analytics workspace | [Sentinel](azure-sentinel.md), [Sentinel feeder](azure-sentinel-feeder-integration.md) |
    | AWS CloudWatch | Log group forwarding | [CloudWatch](aws-cloudwatch.md) |
    | RSyslog | TCP or UDP syslog, any receiver | [RSyslog](rsyslog.md), [RSyslog feeder](rsyslog_feeder_integration.md) |
    | Any other tool | Generic webhook with a JSON payload | [Webhook](webhook-integration.md) |

    **Also reachable over the same transports.** The tools below need no dedicated
    integration, because they consume the syslog, CEF, or webhook stream AccuKnox already
    emits. Follow the [RSyslog guide](rsyslog.md) and point it at your collector.

    <div class="ak-int-grid">
      <div class="ak-int-tile"><img src="../matrix-icons/sumologic.svg" alt="Sumo Logic logo" loading="lazy"><small>Sumo Logic</small></div>
      <div class="ak-int-tile"><img src="../matrix-icons/elastic.svg" alt="Elastic / ELK logo" loading="lazy"><small>Elastic / ELK</small></div>
      <div class="ak-int-tile"><img src="../matrix-icons/opensearch.svg" alt="OpenSearch logo" loading="lazy"><small>OpenSearch</small></div>
      <div class="ak-int-tile"><img src="../matrix-icons/graylog.svg" alt="Graylog logo" loading="lazy"><small>Graylog</small></div>
      <div class="ak-int-tile"><img src="../matrix-icons/datadog.svg" alt="Datadog logo" loading="lazy"><small>Datadog</small></div>
      <div class="ak-int-tile"><img src="../matrix-icons/grafana.svg" alt="Grafana Loki logo" loading="lazy"><small>Grafana Loki</small></div>
      <div class="ak-int-tile"><img src="../matrix-icons/securonix.png" alt="Securonix logo" loading="lazy"><small>Securonix</small></div>
      <div class="ak-int-tile"><img src="../matrix-icons/crowdstrike.png" alt="CrowdStrike logo" loading="lazy"><small>CrowdStrike</small></div>
      <div class="ak-int-tile"><img src="../matrix-icons/exabeam.png" alt="Exabeam logo" loading="lazy"><small>Exabeam</small></div>
      <div class="ak-int-tile"><img src="../matrix-icons/googlecloud.svg" alt="Google SecOps logo" loading="lazy"><small>Google SecOps</small></div>
      <div class="ak-int-tile"><img src="../matrix-icons/devo.png" alt="Devo logo" loading="lazy"><small>Devo</small></div>
      <div class="ak-int-tile"><img src="../matrix-icons/logrhythm.png" alt="LogRhythm logo" loading="lazy" class="ak-int-wide"><small>LogRhythm</small></div>
      <div class="ak-int-tile"><img src="../matrix-icons/wazuh.png" alt="Wazuh logo" loading="lazy"><small>Wazuh</small></div>
    </div>

=== "SaaS and Platform"

    This tab covers ticketing, notification, identity, and the platforms AccuKnox plugs
    into. Click a tile to open its guide.

    <div class="ak-int-grid">
      <a class="ak-int-tile" href="../jira-cloud/"><img src="../matrix-icons/jira.svg" alt="Jira Cloud logo" loading="lazy"><small>Jira Cloud</small></a>
      <a class="ak-int-tile" href="../jira-server-cspm/"><img src="../matrix-icons/jira.svg" alt="Jira Server logo" loading="lazy"><small>Jira Server</small></a>
      <a class="ak-int-tile" href="../servicenow/"><img src="../matrix-icons/servicenow.png" alt="ServiceNow logo" loading="lazy"><small>ServiceNow</small></a>
      <a class="ak-int-tile" href="../freshservice-cspm/"><img src="../matrix-icons/freshservice.png" alt="Freshservice logo" loading="lazy"><small>Freshservice</small></a>
      <a class="ak-int-tile" href="../servicedesk-plus/"><img src="../matrix-icons/manageengine.png" alt="ManageEngine ServiceDesk Plus logo" loading="lazy"><small>ServiceDesk Plus</small></a>
      <a class="ak-int-tile" href="../connectwise-cspm/"><img src="../matrix-icons/connectwise.png" alt="ConnectWise logo" loading="lazy"><small>ConnectWise</small></a>
      <a class="ak-int-tile" href="../slack/"><img src="../matrix-icons/slack.svg" alt="Slack logo" loading="lazy"><small>Slack</small></a>
      <a class="ak-int-tile" href="../email/"><img src="../matrix-icons/email.svg" alt="Email logo" loading="lazy"><small>Email</small></a>
      <a class="ak-int-tile" href="../webhook-integration/"><img src="../matrix-icons/webhook.svg" alt="Webhook logo" loading="lazy"><small>Webhook</small></a>
      <a class="ak-int-tile" href="../saml-sso/"><img src="../matrix-icons/saml.svg" alt="SAML 2.0 logo" loading="lazy"><small>SAML 2.0</small></a>
      <a class="ak-int-tile" href="../okta-sso/"><img src="../matrix-icons/okta.svg" alt="Okta SSO logo" loading="lazy"><small>Okta SSO</small></a>
      <a class="ak-int-tile" href="../auth0-sso/"><img src="../matrix-icons/auth0.svg" alt="Auth0 SSO logo" loading="lazy"><small>Auth0 SSO</small></a>
      <a class="ak-int-tile" href="../azure-entra-sso/"><img src="../matrix-icons/microsoft.svg" alt="Entra ID SSO logo" loading="lazy"><small>Entra ID SSO</small></a>
      <a class="ak-int-tile" href="../rafay-accuknox/"><img src="../matrix-icons/rafay.png" alt="Rafay logo" loading="lazy"><small>Rafay</small></a>
      <a class="ak-int-tile" href="../nutanix-accuknox/"><img src="../matrix-icons/nutanix.svg" alt="Nutanix logo" loading="lazy"><small>Nutanix</small></a>
      <a class="ak-int-tile" href="../spectrocloud/"><img src="../matrix-icons/spectrocloud.png" alt="Spectro Cloud logo" loading="lazy"><small>Spectro Cloud</small></a>
      <a class="ak-int-tile" href="../kong/"><img src="../matrix-icons/kong.svg" alt="Kong logo" loading="lazy"><small>Kong</small></a>
      <a class="ak-int-tile" href="../f5/"><img src="../matrix-icons/f5.svg" alt="F5 logo" loading="lazy"><small>F5</small></a>
      <a class="ak-int-tile" href="../checkmarx/"><img src="../matrix-icons/checkmarx.svg" alt="Checkmarx logo" loading="lazy"><small>Checkmarx</small></a>
    </div>

    | Category | Tools |
    |---|---|
    | Ticketing | Jira Cloud, Jira Server, ServiceNow, Freshservice, ServiceDesk Plus, ConnectWise |
    | Notification | Slack, email, generic webhook |
    | Identity and SSO | [Any SAML 2.0 provider](saml-sso.md), plus Okta, Auth0, and Microsoft Entra ID guides |
    | Kubernetes platforms | Rafay, Nutanix, Spectro Cloud, Red Hat OpenShift, Lens |
    | API and gateway | Kong, F5, NGINX, Istio, AWS API Gateway, Azure APIM, Apigee |
    | Code scanning | Checkmarx, Opengrep, and any tool that emits SARIF |

    Custom ticket fields and payloads are covered in the
    [ticket template guide](ticket-template.md).

## Related pages

[Integrations index](index.md) lists every category with its own overview page.
[Support Matrix](../support-matrix/index.md) covers version and platform compatibility for
CI/CD, clouds, registries, VMs, IaC, and KubeArmor.

Missing a tool you need? Tell us which format it reads. If that format is syslog, CEF,
SARIF, JSON over webhook, MCP, or an OpenAI-compatible API, it already works.
