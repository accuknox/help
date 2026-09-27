---
title: AI DAST, Product Notes
updated: 2026-09-26
tier: A unless a row says otherwise
---

# AI DAST

AI DAST is an AI-driven black-box pentest. It targets URLs, web apps, APIs, containers and mobile
web apps. AgentZ plans the recon and runs the attacks. The first release replaces the earlier
ZAP-based DAST engine for this product. Tier A.

## AI DAST Is AI Pentesting, and AI Red Teaming Is a Different Product

Sales must keep the two terms apart, because a buyer who hears "AI red teaming" expects model
tests.

| Term | What it tests |
| --- | --- |
| AI red teaming | The model or the agent itself. Jailbreaks, prompt injection, hallucination |
| AI DAST | The application and its infrastructure, from the outside, with an AI agent that picks and runs the attacks |

The differentiators are ASPM correlation back to source code, bring your own model (BYOM), and the
native link to the rest of the AccuKnox CNAPP.

## Onboarding Needs One Field, With Four Optional Areas

Only the target domain or URL is required. Tier A.

1. **Target.** Enter the domain. A live check confirms that the target is reachable. Pick a scope
   of web app, API or [confirm the third scope option, heard as "tax service"]. A free-text context
   field steers the model, for example "skip the login page" or "focus on checkout".
2. **Scan depth.** Three tiers.
    - Quick. Fingerprinting only. It enumerates [confirm, heard as "open credits", probably open
      ports] and reports signals.
    - Standard. A balanced exploit check, technology identification and correlation to known CVEs.
    - In-depth. Full enumeration and exploit attempts, such as an open Django admin panel or local
      database credential enumeration.
3. **Authentication.** Four methods. Username and password, TOTP, an email code through a dedicated
   service, and a magic link. Custom headers handle apps that need two mechanisms, such as an
   `Authorization` header plus a cookie, and non-standard headers that a customer uses for an IP
   allowlist. OTP to a mobile number is out of scope, because the scan cannot control the phone.
4. **ASPM repo correlation, optional.** AI DAST reuses the existing ASPM connectors for GitHub,
   Bitbucket and CI. The customer can share one folder or a snippet instead of the full repo. A
   finding then maps to the source line that caused it.
5. **Threat context and documents, optional.** A compliance focus narrows the attack surface. PCI
   DSS points the scan at billing and checkout. A Swagger or OpenAPI upload finds legacy endpoints
   that still answer but that nobody maintains, such as an old signup endpoint left behind after a
   site rebuild.

## Recon Runs in Sequence, Then Attacks Run in Parallel

The planning phase runs in order. Recon, technology fingerprinting and attack vector selection
finish before any exploit starts. For example, AgentZ checks that the organization owns a subdomain
before it treats subdomain takeover as a valid vector. The execution phase then starts parallel
attack threads across every surface that recon found. Tier A.

Discovery and enumeration are AI-driven. Validation is deterministic, so a reported finding is a
confirmed check for a known weakness. The sales line is "AI-driven recon and exploitation, with
deterministic validation of findings."

## BYOM Answers the Data Residency Objection

The customer picks the model in Settings, and the choice applies to AI DAST and to the other AI
features. Tier A.

| Option | When it fits |
| --- | --- |
| The AccuKnox-provided model | The default |
| A frontier model through the customer's own API key, such as OpenAI or Anthropic | The customer already has a contract with that provider |
| A local or on-premises LLM, open source or proprietary | The customer will not send application data to a frontier model, or runs air-gapped |

## Four Items Are Not in the First Release

Set this expectation before a demo. Tier A.

- **Credits.** A common billing unit that evens out cost across models. It waits on the decision
  about scan scope, one domain or all subdomains.
- **IP allowlist.** A published list of AccuKnox scanner IPs for the customer's firewall. Customers
  ask for this often.
- **Test connection.** A reachability check before the scan starts, separate from the live check on
  the target field.
- **Dashboard widgets.** The designs exist. The frontend is still in build.

## Public Docs Cover the Existing DAST Engine Only

These facts are tier D and can ship anywhere today.

- DAST has 4 scan types, from a passive baseline to Advanced Active Penetration Testing rules.
  Source: `docs/how-to/dast-scan-types.md`.
- DAST can scan behind MFA with a recorded browser login, TOTP codes included. Source:
  `docs/getting-started/3.6-release.md`.

## Five Lines Answer the AE Questions on AI DAST

- Lead with "an AI-driven pentest that adapts to your tech stack, where a rule scanner runs the same
  checks every time."
- Answer "what does the AI do" directly. AI runs recon, technology identification, attack vector
  selection and exploitation.
- Use BYOM to win regulated and air-gapped buyers, because their data stays on their own model.
- Use ASPM correlation as the upsell. A pentest finding maps back to the code line that a developer
  fixes.
- Answer "what are the prerequisites" with one field, the target URL. Credentials, a repo and an
  OpenAPI file each make the scan deeper, and none of them is required.
