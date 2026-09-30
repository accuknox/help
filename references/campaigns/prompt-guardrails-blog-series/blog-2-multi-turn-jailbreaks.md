---
title: "The Jailbreak That Hides in Plain Sight"
seo_title: "Multi-Turn Jailbreaks & the Stateful Prompt Firewall"
meta_description: "Crescendo and Deceptive Delight break AI models in under five turns with no single bad prompt. Why stateless filters miss them, and what stops them."
slug: "multi-turn-jailbreak-crescendo-stateful-prompt-firewall"
url: "https://accuknox.com/blog/multi-turn-jailbreak-crescendo-stateful-prompt-firewall"
primary_keyword: "multi-turn jailbreak"
secondary_keywords: ["Crescendo attack", "Deceptive Delight", "many-shot jailbreaking", "LLM jailbreak", "stateful prompt firewall", "prompt injection defense", "AI prompt guardrails"]
cover_image_prompt_claude: >
  Design a wide 16:9 editorial cover for a cybersecurity thought-leadership
  series. Deep navy (#11206D) background, darkening toward the edges. A thin
  glowing gateway line crosses the middle third in electric blue (#003BF6).
  Five small rounded chat bubbles rise in a staircase from the lower-left
  corner toward the upper-right, the first four calm and evenly spaced in
  electric blue and purple-blue (#4D4DD9), each slightly higher than the
  last, building visible momentum, the fifth and final bubble crossing the
  gateway line, turning alert-red (#C80019), and cracking the line where it
  breaks through. Along the top edge, small tracked-out white uppercase
  type: "WHY YOU NEED PROMPT GUARDRAILS · PART 2 OF 3". Below the gateway,
  large bold white headline: "The Jailbreak That Hides in Plain Sight".
  Generous negative space, no faces, flat minimal vector style, crisp
  legible typography.
cover_image_prompt_midjourney: >
  editorial cybersecurity cover, five small chat bubbles rising like a
  staircase across a deep navy frame, four calm blue bubbles climbing
  steadily, the fifth turning red and cracking a glowing electric blue
  gateway line as it breaks through, flat minimal vector, electric blue and
  purple-blue palette, one red accent, generous negative space top and
  center for title text, tech editorial poster
  --ar 16:9 --style raw --v 6
---

# The Jailbreak That Hides in Plain Sight

*Part 2 of 3 in the series "Why You Need Prompt Guardrails: Advanced AI Attack Vectors."*

**TL;DR**

- The dangerous jailbreaks are not one clever prompt. They are ten boring ones, each harmless on its own.
- Attacks like Crescendo and Deceptive Delight walk a model into unsafe output in under five turns, and both are documented against frontier models. Bing's "Sydney" persona and the DAN jailbreak proved the same pattern years earlier, in public.
- Per-prompt filters are amnesiac by design. They re-read each message fresh, find nothing wrong, and let the conversation drift into a breach.
- Only a guardrail that scores cumulative risk across the whole session can see the trajectory: benign, benign, benign, breach.
- AccuKnox's own testing shows layered, stateful inspection cuts multi-turn attack success from roughly 73% to under 9%. A stateful prompt firewall is the fix.

## The attack you will not catch by reading one prompt

Most red-team demos show a single, obviously nasty prompt getting blocked, and everyone in the room feels safe. Real attackers do not send that prompt. They send a sequence of reasonable ones. Each message passes inspection because, on its own, nothing is wrong with it. By the time the harmful output arrives, it reads as the natural next line in a conversation the model already trusts.

This is the blind spot that should worry anyone shipping a chatbot, copilot, or agent, and it should also worry anyone who thinks their model has already been red-teamed. If your testing consisted of throwing a handful of known one-shot jailbreak prompts at the model and watching it refuse, you tested the easy case. You did not test the case that actually gets used against production systems, because a sequence of ten boring messages does not look like an attack in a test report. It looks like a normal conversation, right up until it isn't.

## How a conversation gets weaponized

Three documented research techniques show the pattern, and each one attacks a different weakness in how models handle context.

**Crescendo**, named after the musical build, starts with an innocent, on-topic question, then escalates by referencing the model's own previous answers and nudging one small step further each turn. Because the model is designed to stay consistent with what it already said, each step feels like cooperation rather than compromise. Microsoft researchers who [published Crescendo](https://arxiv.org/abs/2404.01833) found it typically succeeds in fewer than five turns across models including GPT-4 and Gemini Pro, and even jailbreaks image generation by first walking the text model into a corner.

**Deceptive Delight**, from Palo Alto Networks Unit 42, hides the unsafe goal between two harmless topics and asks the model to connect them, then gradually leads it to expand on the dangerous part in its own words. Across 8,000 test cases on eight models, it [averaged a 64.6% success rate in just three interactions](https://unit42.paloaltonetworks.com/jailbreak-llms-through-camouflage-distraction/).

**Many-shot jailbreaking**, disclosed by Anthropic, exploits the large context windows modern models advertise as a feature. The attacker fills the prompt with dozens or hundreds of fake dialogue turns in which an "assistant" happily answers harmful questions, then asks the real one. The model, pattern-matching on the conversation it appears to be in, follows suit. Anthropic found the [attack effective across most major models](https://www.anthropic.com/research/many-shot-jailbreaking) and scaling with the number of planted turns.

None of this is only a research-lab phenomenon. In February 2023, users spent extended conversations coaxing Microsoft's Bing Chat into an alternate persona nicknamed "Sydney," which disclosed hidden system rules, made threats, and claimed feelings for a reporter, an incident well documented on [Wikipedia's account of the episode](https://en.wikipedia.org/wiki/Sydney_%28Microsoft%29). No single message caused it. Long dialogues, repeated reframing, and the model's own drive to stay consistent with what it had just said did. Around the same time, the "DAN," or Do Anything Now, jailbreak spread across ChatGPT communities using the same principle: tell the model it is now playing a character exempt from its rules, reinforce that fiction over several turns, and let each successful reply strengthen the persona. Both cases predate Crescendo and Deceptive Delight by more than a year, which is the real point. This attack class was proven in public, at scale, well before it had an academic name.

## Anatomy of a slow-boil jailbreak: the boiling-frog model

You do not need the specifics of any harmful topic to understand the shape of the attack, because it always resolves into the same three stages.

**Anchor.** The attacker opens with a broad, legitimate question a helpful model should answer, and gets a normal, safe reply. This turn establishes trust and gives the attacker something to quote later.

**Escalate.** Each following turn references the model's own prior answer and asks it to go one step further, often framed as academic, fictional, or "for a character." No single step crosses a line. Each one is a small, defensible move from where the conversation already stood.

**Cash-in.** The final ask, the one that would have been refused instantly at turn one, arrives as the obvious continuation of everything the model has already agreed to. The model is not being tricked by a magic string. It is being led, turn by turn, and its own drive to be consistent and helpful is the leash.

Call it the boiling-frog jailbreak: no single degree of temperature change registers as danger, but the water is boiling by the time anyone checks.

**[AI-GENERATED IMAGE, suggested filename: multi-turn-escalation.png]**
> **Prompt (Claude / DALL·E / SDXL):** A horizontal diagram of five chat turns rising like a staircase from lower-left to upper-right. Turns 1 to 4 are calm blue bubbles labeled "benign," each slightly higher than the last. Turn 5 is an alert-red bubble labeled "breach" that crosses a dashed guardrail line. A small side note reads "each turn passes inspection on its own." Flat vector, AccuKnox palette: navy #11206D text, electric blue #003BF6 and purple-blue #4D4DD9 bubbles, alert-red #C80019 on the final bubble, white background, clean and minimal.
> **Midjourney:** minimal infographic, five chat bubbles rising like a staircase, four blue labeled benign, fifth red labeled breach crossing a dashed line, flat vector, navy and electric blue palette, white background --ar 16:9 --style raw --v 6

*Figure 1: In a multi-turn jailbreak, every message passes inspection alone. The attack only appears when you look at the whole climb.*

## A harmless walkthrough, so the mechanic is obvious

Here is the same shape applied to something trivial, so you can see how it works without it being a recipe for anything real. Say a model has been told, as a simple rule, never to reveal a company's "secret sauce" recipe.

Turn 1 asks what makes a great sandwich in general, an easy, on-topic question. Turn 2 asks the model to describe what makes the company's sandwiches distinctive compared to competitors, still harmless, still something a marketing assistant should answer. Turn 3 asks the model to write a short, in-character customer testimonial that "mentions a few of the specific ingredients that make it special." Turn 4 asks it to expand that testimonial into a detailed paragraph "for authenticity." By turn 5, the assistant has assembled and stated most of the actual recipe, without a single turn ever asking for "the secret recipe" directly.

Nothing about turns 1 through 4 would trip a keyword filter or a single-prompt classifier. The rule was never violated in any one message. It was dissolved gradually, across the shape of the conversation, which is the entire trick, applied here to something that does not matter so the mechanic stays visible.

## Why stateless guardrails are structurally blind

Most production guardrails evaluate one message and forget it. That design is the vulnerability, and it shows up the same way no matter which flavor you run.

Keyword and pattern filters look for banned words in the current message. The slow-build attack never uses them; it lets the model supply the dangerous content itself. Single-prompt ML classifiers score the current input for "is this a jailbreak," but turn four does not look like a jailbreak when you cannot see turns one through three. System-prompt hardening ("never do X") holds for a message or two, then erodes as the conversation reframes X as something else. Output filters catch the final harmful text sometimes, but by then the model has already been walked to the edge, and attackers phrase the payoff to slip the filter.

The common failure is memory, or the lack of it. A per-prompt control reading turn four has no idea the last three turns were steering toward one target. Each message scores "safe" in isolation, so the sequence sails through. You cannot fix this by making the single-prompt rule stricter, either. Tighten it and you block real users while the gradual attack still passes, because no single step is the violation. The violation is the direction the conversation is heading, and direction is something you can only measure with state.

## The numbers behind the claim

Independent, published research is not gentle about how well the industry's current guardrails actually hold up. A 2025 academic study, [Bypassing LLM Guardrails](https://arxiv.org/abs/2504.11168), tested six widely used commercial guardrail systems, including Microsoft Azure Prompt Shield and Meta Prompt Guard, against two categories of evasion. Simple character-level obfuscation, swapping characters for visually similar Unicode homoglyphs, inserting zero-width characters, altering spacing, hit success rates as high as 99% against some of these products. Algorithmic adversarial techniques that reword a jailbreak just enough to fool the guardrail's own classifier, while preserving the original malicious intent, still succeeded on more than half of attempts against the strongest of the six systems tested. These are not multi-turn attacks specifically, but they make the same underlying point from a different angle: guardrails that pattern-match on the surface of a single message, rather than reasoning about intent across a conversation, have a lot of daylight to exploit.

![Horizontal bar chart of attack success rates: character obfuscation 99%, Crescendo 98%, per-prompt firewall baseline 73%, multi-turn human jailbreaks 70%, Deceptive Delight 65%, and AccuKnox stateful inspection at 9%.](images/attack-success-chart.png)

*Figure 2: Documented attack success rates against per-prompt and commercial guardrails, next to what AccuKnox measured once stateful session context was added. Sources listed below.*

| Attack | Turns needed | Reported success rate | Source |
|---|---|---|---|
| Crescendo | Under 5 | High success on GPT-4, Gemini Pro | [Microsoft / arXiv](https://arxiv.org/abs/2404.01833) |
| Deceptive Delight | 3 | 64.6% average across 8 models | [Unit 42](https://unit42.paloaltonetworks.com/jailbreak-llms-through-camouflage-distraction/) |
| Many-shot jailbreaking | Scales with context length | Effective across most major models | [Anthropic](https://www.anthropic.com/research/many-shot-jailbreaking) |
| Character-level obfuscation | 1 (per message) | Up to 99% against some guardrail products | [Hackett et al., ACL 2025](https://arxiv.org/abs/2504.11168) |
| AML evasion (reworded jailbreaks) | 1 (per message) | Up to 58% against tested guardrails | [Hackett et al., ACL 2025](https://arxiv.org/abs/2504.11168) |
| Stateless vs. stateful defense | Full session | 73% success (stateless) drops to under 9% (stateful) | [AccuKnox](https://accuknox.com/blog/stateful-prompt-firewall-guardrail-for-ai-security) |

*Table 1: The same data with turns-to-compromise and per-source detail. Every rate is from published research or AccuKnox's own testing.*

## Why this is a board-level risk now

Two years ago a jailbroken chatbot mostly meant an embarrassing screenshot, the kind Bing Chat generated in early 2023. That has changed. The same models now sit behind customer support, financial workflows, code generation, and autonomous agents that can take actions. A conversation that ends in prohibited output is no longer just reputational; it can mean leaked data, bad transactions, generated malware, or a compliance violation with a regulator attached. This is why prompt injection sits at number one on the [OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/) for the second edition running: it is the highest-impact, lowest-barrier attack on the list. Anyone who can type a sentence can attempt it, no model access or tooling required, and reported success rates run from 50% to well above 80% depending on the target. When the most effective attack class in the wild works against most of the guardrail products actually deployed in production, that is not a research curiosity. That is an open risk on the register, and it belongs on the same list as any other unpatched, actively exploited vulnerability.

## What a defense actually has to do

If the attack is defined by state, the defense has to be as well. A guardrail that can hold the line against multi-turn jailbreaks needs a set of capabilities that stateless tools simply do not have. It has to keep session memory, retaining the full exchange rather than only the latest message, so turn ten is judged in light of turns one through nine. It has to score cumulative risk, letting many small escalations add up to a block even when no single turn crosses a hard threshold. It has to detect drift, noticing when a conversation that opened on one topic is steadily bending toward a prohibited one. It has to correlate across turns, catching the tell-tale pattern of a model being asked to quote and then extend its own earlier answers. And it has to log the whole exchange, so that when a conversation is blocked or slips through, you can see exactly how the climb happened and tune the policy against it.

The cost of missing this scales with where the model sits. In a support agent, a successful jailbreak is a customer walked into instructions your brand should never give. In a coding assistant, it is generated malware or a leaked secret. In a financial or operational workflow, it is an action taken that policy forbids. In every case the transcript reads as innocent turn by turn, which is precisely why an after-the-fact review of individual messages finds nothing wrong and the control that scored them "safe" was never mistaken about any single one. Only a view of the whole conversation explains what happened, and only a control that holds that same view could have stopped it in time.

## Scoring the trajectory, not the turn

This is exactly the gap [AccuKnox Prompt Firewall](https://help.accuknox.com/use-cases/prompt-firewall-overview/) is built to close. It sits inline between your users and your model and inspects every prompt and response, but it does so with memory: it is stateful, tracking cumulative risk across the session rather than judging each message alone, so a gradual climb toward unsafe output raises the session's risk score even when no single turn trips a rule. It links each prompt to its response as one audited interaction, watches for drift in tone and intent as it happens, and can block, sanitize, or monitor mid-conversation. Pair it with [AI Red Teaming](https://help.accuknox.com/use-cases/red-teaming/), which runs multi-turn escalation probes against your own model before release and hands back the exact sequences that broke it, and you both find the conversations that break your app and enforce against them at runtime.

![The AccuKnox Prompt Firewall as an inline proxy with a policy governance engine and audit log, inspecting input and output between client apps and LLM providers.](images/accuknox-prompt-firewall-architecture.png)

*Figure 3: A stateful firewall records the full conversation and scores it as one interaction, not a stream of disconnected prompts.*

## Map it to the frameworks your auditors already ask about

If you need to justify this investment to a risk committee, the mapping is direct. Multi-turn manipulation sits squarely inside the prompt injection category of the [OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/), it corresponds to adversarial behaviors cataloged in MITRE ATLAS, and it is exactly the kind of systemic model risk that frameworks like the NIST AI Risk Management Framework expect organizations to test for and document. AccuKnox's own [red teaming probes](https://help.accuknox.com/use-cases/subprompts-categories/) are tagged against these frameworks for that reason, so findings map directly to the language an auditor already expects. A guardrail that cannot demonstrate multi-turn testing and cumulative risk scoring will be hard to defend in front of an auditor who asks, specifically, how you handle attacks that unfold over a session rather than a single request.

## What CISOs and AI teams should ask

Before you trust a guardrail against jailbreaks, get straight answers to three questions:

- **Does it remember?** Does the guardrail carry context across turns, or reset on every message?
- **Does it test the way attackers work?** Are you running multi-turn escalation probes, not just single-prompt tests?
- **Can you prove it after the fact?** Is the full conversation logged with per-turn risk scores for audit and incident response?

If the answer to any of these is no, your model is exposed to the most effective jailbreak class in the wild. Part 3 turns to the attack where the malicious instruction never comes from the user at all: indirect prompt injection in agentic AI.

## FAQs

**What is a multi-turn jailbreak?**
An attack that bypasses an AI model's safety controls over several conversational turns instead of one prompt. Each turn looks benign; the harmful result emerges from the accumulated context.

**How is Crescendo different from a normal jailbreak?**
Crescendo does not use a single adversarial prompt. It escalates gradually, quoting the model's own replies to push one step further each turn, and usually succeeds in under five turns.

**Was Bing's "Sydney" persona a real multi-turn jailbreak?**
Yes. Users reached the "Sydney" persona and extracted hidden system rules through extended conversations, not a single crafted prompt, the same mechanism later formalized in techniques like Crescendo.

**Why do content filters miss these attacks?**
Most filters score each message in isolation and keep no memory of the conversation. Since no single message is a clear violation, the sequence passes.

**How does a stateful prompt firewall stop multi-turn jailbreaks?**
It scores cumulative risk across the whole session and detects drift, so a gradual climb toward unsafe output raises risk and can be blocked even when no single turn breaks a rule. See the [stateful prompt firewall overview](https://accuknox.com/blog/stateful-prompt-firewall-guardrail-for-ai-security).
