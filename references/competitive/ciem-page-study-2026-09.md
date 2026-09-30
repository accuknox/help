---
title: CIEM Landing Page Study
updated: 2026-09-29
use: Layout and messaging patterns from six competitor CIEM pages, for the AccuKnox CIEM page
---

# CIEM Landing Page Study

Six vendors sell CIEM with the same promise: show who can do what in the cloud, then cut access to
what people use. The AccuKnox page copies the structure that works and none of the claims. Every
AccuKnox fact on the page comes from the two CIEM help docs.

Pages read with Firecrawl on 2026-09-29. The raw text is in
`references/Website Pages to Build 26 September/Scripts/scrape/`.

| Vendor | Page |
| --- | --- |
| Wiz | `wiz.io/solutions/ciem` |
| Palo Alto Networks, Prisma Cloud | `paloaltonetworks.com/prisma/cloud/cloud-infrastructure-entitlement-mgmt` |
| Tenable | `tenable.com/cloud-security/products/cloud-infrastructure-entitlement-management` |
| Sonrai Security | `sonraisecurity.com/cloud-security-platform/cloud-permissions-firewall/` |
| CrowdStrike | `crowdstrike.com/en-us/platform/cloud-security/ciem/` |
| Orca Security | `orca.security/platform/cloud-infrastructure-entitlement-management-ciem/` |

## Six Patterns Repeat Across the Pages

1. **The hero answers one question.** Wiz writes "who can access what in my environment". Prisma
   writes "who can take what actions on which resources". Sonrai leads with the outcome, "enforce
   least privilege automatically".
2. **Three pillars follow the hero.** Tenable uses visualize, uncover toxic combinations,
   remediate. CrowdStrike and Wiz also use three short blocks. Prisma opens with three problems
   first.
3. **A graph is the proof.** Wiz, Prisma and Tenable each show an access map or an investigation
   graph. The graph carries the "effective permissions" idea better than any sentence.
4. **Human and machine identities get named.** Wiz and Tenable split human from non-human
   identities, because service accounts and pipeline roles hold most of the standing access.
5. **Unused access is the easy win.** Sonrai builds the whole page on unused permissions and
   dormant identities. Wiz flags inactive users.
6. **CIEM sits inside a wider platform.** Orca's H2 says standalone CIEM tools lack cloud context.
   Wiz ties entitlements to attack paths. Tenable and CrowdStrike sell CIEM as part of a CNAPP.

Formats that repeat are one product screenshot per claim, an FAQ at the bottom (Sonrai and Orca), a
demo CTA twice, and customer logos or analyst badges. Sonrai adds three outcome percentages.

## AccuKnox Can Match Five Patterns From the Docs Alone

| Pattern | AccuKnox fact from the docs | Screenshot |
| --- | --- | --- |
| Who can access what | One list of users, groups and roles across AWS, GCP, Azure and OCI | `ciem-identity-list.png` |
| The graph is the proof | The access graph traces identity, then group, then policy | `ciem-identity-graph.png` |
| Human and machine | Each identity is classified as human or machine | `ciem-identity-list.png` |
| Unused access | Last Used and Days Since Last Used columns, plus Created By | `ciem-identity-list-columns.png` |
| Inside a platform | CIEM turns on with a toggle inside the normal cloud account onboarding. KIEM covers Kubernetes identities | `ciem-onboard-toggle.png` |

## The AccuKnox Page Leaves Out Three Competitor Claims

The docs do not show these, so the page does not claim them.

- Automated remediation or generated least-privilege policies (Wiz, Prisma, Tenable, Sonrai, Orca).
- Just-in-time access (Tenable, Orca, Sonrai).
- IdP ingestion, such as Okta or Entra ID (Prisma, Wiz).

The page also states the documented limits. CIEM is coming soon, and it supports standalone cloud
accounts only, not organization accounts.
