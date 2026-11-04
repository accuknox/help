---
title: Secrets Manager Support and SLA
description: Response times by severity and support package, how to open a ticket, and the uptime commitment for AccuKnox Secrets Manager.
---

# Support and SLA

AccuKnox answers a P1 ticket within 1 hour on the Gold and Platinum support packages, and within 4 hours on Silver. Your support package, named in your order, sets the coverage hours and the response time for each severity. The terms come from Attachment A of the [AccuKnox Subscription License Agreement](https://accuknox.com/sla).

## Response Times by Severity and Package

| Severity | Silver (Standard) first response | Silver updates | Gold (Premium) first response | Gold updates | Platinum (PremiumPlus) first response | Platinum updates |
| --- | --- | --- | --- | --- | --- | --- |
| P1 | 4 hours | 1 business day | 1 hour | 2 hours | 1 hour | 2 hours |
| P2 | 1 business day | 2 business days | 2 hours | 8 hours | 2 hours | 8 hours |
| P3 | 2 business days | 3 business days | 4 hours | 24 hours | 4 hours | 24 hours |
| P4 | 2 business days | 3 business days | 8 hours | 48 hours | 8 hours | 48 hours |

| Feature | Silver (Standard) | Gold (Premium) | Platinum (PremiumPlus) |
| --- | --- | --- | --- |
| Coverage hours | 9 hours a day, 5 days a week | 12 hours a day, 6 days a week | 24 hours a day, 7 days a week |
| Phone support | 9x5 | 12x6 | 24x7 |
| Training | Live admin webinar series and getting started guides | Standard training plus 2 seats in the premium training class | Standard training plus 5 seats in the premium training class |
| Adoption services | None | None | A named Customer Success Manager |

## Pick the Severity That Matches the Impact

| Severity | Definition | Secrets Manager example |
| --- | --- | --- |
| P1 | A service failure or severe degradation. Users cannot reach a critical business application | The production cluster is sealed or down, and applications cannot read secrets |
| P2 | A partial failure or mild degradation, a non-production instance down, or a bug with significant impact on an integration | One node is down, or the non-production instance is unavailable |
| P3 | A minor impact, a non-critical bug, or trouble integrating a new application | A new application cannot log in through its auth method |
| P4 | A how-to question or a feature request | A question about a policy, or a request for a new auth method |

## Open a Ticket by Email

Send every support request to [support@accuknox.com](mailto:support@accuknox.com). AccuKnox issues a ticket number for each incident, and every follow-up call must quote it.

Name one support contact and one backup in your organisation. AccuKnox answers support requests from those two people only.

Put these details in the first email, so support can start at once.

1. The Secrets Manager version and the Helm chart version.
2. The output of `vault status` from each pod.
3. The output of `kubectl get pods -n accuknox`, and `kubectl describe` for any failing pod.
4. The pod logs from the time of the failure, with secret values removed.

!!! danger "Never send key material"
    Keep unseal key shares, recovery keys, the root token and secret values out of every ticket. AccuKnox support never needs them.

## Response Times Exclude These Delays

AccuKnox does not count a delay that one of these causes against the response times.

- An available update that you did not install.
- A change to the operating system, network or environment made by you or a third party.
- A customization of the product.
- Use of the product in a way it was not designed for.
- Use with software or hardware AccuKnox has not approved, or on a platform outside the support matrix.

## Uptime Depends on Where Secrets Manager Runs

| Deployment | Who runs it | Uptime |
| --- | --- | --- |
| Self-hosted with the Helm chart | Your team | You control it. A three-node cluster survives the loss of one node, and a second region survives the loss of the first. See [High Availability and Backup](high-availability.md) |
| Managed shared or dedicated instance | AccuKnox | Every managed instance runs in high availability mode. Your order names the agreement that sets the uptime commitment |

For the AccuKnox Cloud Service, the [Subscription License Agreement](https://accuknox.com/sla) commits to 99.9% availability over each year. The [SaaS SLA](https://accuknox.com/saas-sla) adds service credits when monthly uptime falls below 99.9%. Check live status at [status.accuknox.com](https://status.accuknox.com/).

AccuKnox professional services can also review your application and make the code change to read secrets through the SDK.

- - -
[SCHEDULE DEMO](https://www.accuknox.com/contact-us){ .md-button .md-button--primary }
