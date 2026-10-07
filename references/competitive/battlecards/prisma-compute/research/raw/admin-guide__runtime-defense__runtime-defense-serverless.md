For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/runtime-defense/runtime-defense-serverless.md).

Prisma Cloud lets you monitor process, network and filesystem activity within your serverless functions and enforce policies to allow or deny these activities. Policies let you define:

- Process activity - enables specifying specific whitelisted processes, blocking all processes except the main process and detecting cryptomining attempts.

- Network activity - enables monitoring and enforcement of DNS resolutions, inbound and outbound network connections.

- Filesystem activity - enables defining specific paths in an allowed or denied list.


In addition to runtime policy, you can also configure multiple [WAAS](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/compute-edition/34/admin-guide/waas/waas.md) application firewall protections to defend your functions from application layer attacks.

## Securing serverless functions[Direct link to heading](https://docs.prismacloud.io/admin-guide/runtime-defense/runtime-defense-serverless\#securing-serverless-functions)

To secure Serverless functions:

1. Verify that you have installed Serverless Defenders on your functions.











You must install Serverless Defenders before you can create serverless runtime policy.

2. Log in to the Prisma Cloud Console and select **Defend > Runtime > Serverless policy** to add policies.

3. Embed the Serverless Defender into your function either manually or with Auto-defend:









   - [Manually embed a Serverless Defender](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/compute-edition/34/admin-guide/install/deploy-defender/serverless/serverless.md)

   - [Use a Lambda layer to embed a Serverless Defender](https://docs.prismacloud.io/admin-guide/install/deploy-defender/serverless/install-serverless-defender-layer)

   - [Use Auto-defend to deploy Serverless Defenders](https://docs.prismacloud.io/admin-guide/install/deploy-defender/serverless/auto-defend-serverless)


## Defining your policy[Direct link to heading](https://docs.prismacloud.io/admin-guide/runtime-defense/runtime-defense-serverless\#defining-your-policy)

Add runtime protection for your serverless function by defining a runtime rule for it in the Prisma Cloud Console.

Prisma Cloud ships without a Serverless runtime policy. Serverless Defenders fetch the policy from the TW\_POLICY environment variable and dynamically during runtime from the console (every 2 minutes).

By default, new rules apply to all functions (`*`), but you can target them to specific functions and/or regions using [pattern matching](https://docs.prismacloud.io/admin-guide/configure/rule-ordering-pattern-matching). For Azure Functions only, you can additionally scope rules by account ID.

1. Log into Prisma Cloud Console.

2. Go to **Defend > Runtime > Serverless Policy**.

3. Click **Add rule**.









1. Enter a rule name.

2. By default, the rule applies to all functions in all regions and accounts.











      Target the rule to specific functions.

3. Click the **Networking** tab.

4. Enable **DNS** toggle

5. Set **Effect** to **Prevent**.

6. Add _\*amazon.com_ to the **DNS allow list**











      By default, rules are set to allow traffic. When adding a domain to the allow list, then everything outside the allow list is denied by default. The above rule will block all traffic except to \*amazon.com.

7. Click **Save**.


## View runtime audits[Direct link to heading](https://docs.prismacloud.io/admin-guide/runtime-defense/runtime-defense-serverless\#view-runtime-audits)

To view the security audits, go to **Monitor > Events > Serverless Audits**. You should see audits with the following messages:

AskCopy

```
DNS resolution of domain name yahoo.com triggered by /usr/bin/wget explicitly denied by a runtime rule.
```

To refine the view, use filters. For example, to see Azure Functions only, use the `Provider: Azure` filter.

[PreviousRuntime defense for hosts](https://docs.prismacloud.io/admin-guide/runtime-defense/runtime-defense-hosts) [NextRuntime defense for App-Embedded](https://docs.prismacloud.io/admin-guide/runtime-defense/runtime-defense-app-embedded)

Last updated 3 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
