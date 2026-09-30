> For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.prismacloud.io/content-collections/runtime-security/runtime-defense/runtime-defense-serverless.md).

# Runtime Defense for Serverless

Prisma Cloud lets you monitor process, network and filesystem activity within your serverless functions and enforce policies to allow or deny these activities. Policies let you define:

* Process activity - enables specifying specific whitelisted processes, blocking all processes except the main process and detecting cryptomining attempts.
* Network activity - enables monitoring and enforcement of DNS resolutions, inbound and outbound network connections.
* Filesystem activity - enables defining specific paths in an allowed or denied list.

In addition to runtime policy, you can also configure multiple [WAAS](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/enterprise-edition/content-collections/runtime-security/waas/waas.md) application firewall protections to defend your functions from application layer attacks.

## Securing serverless functions

To secure Serverless functions:

1. Verify that you have installed Serverless Defenders on your functions.

   You must install Serverless Defenders before you can create serverless runtime policy.
2. Log in to the Prisma Cloud Console and select **Defend > Runtime > Serverless policy** to add policies.
3. Embed the Serverless Defender into your function either manually or with Auto-defend:
   * [Manually embed a Serverless Defender](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/enterprise-edition/content-collections/runtime-security/install/deploy-defender/serverless/serverless.md)
   * [Use a Lambda layer to embed a Serverless Defender](/content-collections/runtime-security/install/deploy-defender/serverless/lambda-layer.md)
   * [Use Auto-defend to deploy Serverless Defenders](/content-collections/runtime-security/install/deploy-defender/serverless/auto-defend-serverless.md)

## Defining your policy

Add runtime protection for your serverless function by defining a runtime rule for it in the Prisma Cloud Console.

Prisma Cloud ships without a Serverless runtime policy. Serverless Defenders fetch the policy from the TW\_POLICY environment variable and dynamically during runtime from the console (every 2 minutes).

By default, new rules apply to all functions (`*`), but you can target them to specific functions and/or regions using [pattern matching](/content-collections/runtime-security/configure/rule-ordering-pattern-matching.md). For Azure Functions only, you can additionally scope rules by account ID.

1. Log into Prisma Cloud Console.
2. Go to **Defend > Runtime > Serverless Policy**.
3. Click **Add rule**.
   1. Enter a rule name.
   2. By default, the rule applies to all functions in all regions and accounts.

      Target the rule to specific functions.
   3. Click the **Networking** tab.
   4. Enable **DNS** toggle
   5. Set **Effect** to **Prevent**.
   6. Add *\*amazon.com* to the **DNS allow list**

      By default, rules are set to allow traffic. When adding a domain to the allow list, then everything outside the allow list is denied by default. The above rule will block all traffic except to \*amazon.com.
   7. Click **Save**.

## View runtime audits

To view the security audits, go to **Monitor > Events > Serverless Audits**. You should see audits with the following messages:

```
DNS resolution of domain name yahoo.com triggered by /usr/bin/wget explicitly denied by a runtime rule.
```

To refine the view, use filters. For example, to see Azure Functions only, use the `Provider: Azure` filter.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.prismacloud.io/content-collections/runtime-security/runtime-defense/runtime-defense-serverless.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
