---
title: Filter Registry Images with Scan Patterns
description: Choose which container images and tags AccuKnox scans in a registry. Use wildcards, the minus sign to exclude, and bracket ranges such as v[1-8] to match a set of tags.
---

# Filter Registry Images with Scan Patterns

A registry can hold thousands of image tags. A scan pattern tells AccuKnox which of them to scan. Use a pattern to skip old versions and cut scan cost.

Patterns work the same way on every registry you onboard. They are not tied to one registry host.

## Before You Start

- Onboard the registry, or start onboarding it. See [Container Registry Onboarding](/how-to/registry-overview/).
- Find the **Tag pattern** field in the registry onboarding form.

## How a Pattern Is Read

A pattern has the form `repository:tag`. Each part can use a wildcard.

- `*` matches any run of characters.
- A leading `-` excludes the images that match the rest of the pattern.
- `[1-8]` matches one character in the range, here the digits 1 through 8.

AccuKnox excludes every image unless a pattern includes it. A registry with no include pattern scans nothing.

## Pattern Examples

| Pattern | Effect |
|---|---|
| `*:latest` | Scans any repository with the tag `latest`. |
| `example/*:v1` | Scans the tag `v1` in every repository under `example/`. |
| `example/*:v*` | Scans every tag that starts with `v` under `example/`. |
| `example/*:*` | Scans every tag under `example/`. |
| `*:example` | Scans any repository with the tag `example`. |
| `-*:v1` | Excludes the tag `v1` in any repository. |
| `*:v[1-8]*` | Scans tags that start with `v`, then a digit from 1 to 8, then any suffix. |

## Match a Range of Tags

Use a bracket range to pick a set of version tags with one pattern.

The pattern `*:v[1-8]*` matches these images:

- `image:v1`
- `image:v2.0`
- `repo/app:v8-beta`

It does not match `image:v9` or `image:v0.9`. The digits 9 and 0 fall outside the range.

!!! note "Multi-digit tags"
    A bracket matches one character. Test tags such as `v10` before you scan, because the digit after `v` decides the match.

## Test a Pattern Before You Scan

Check a pattern against a real tag before you commit to a scan.

1. Open the registry onboarding form and go to the **Tag pattern** field.
2. Enter your pattern.
3. Enter one tag in the pattern test, for example `v15`.
4. Read the result. AccuKnox tells you whether the pattern includes or excludes that tag.
5. Repeat with a few tags from each end of the range.
6. Save the registry.

The info icon next to the field shows example patterns.

!!! note "Limits of the test"
    The test checks one tag at a time. AccuKnox does not show how many images a pattern matches before the scan. The count would need a background job over the whole registry.

## Related Pages

- [Container Registry Onboarding](/how-to/registry-overview/)
- [Onboard Docker Hub](/how-to/dockerhub/)
- [Onboard Azure Container Registry](/how-to/acr/)

<!--
## Pending Stakeholder Input

Confirm before this page is published. Source: Jira ticket "Support for REGEX in Registry Scan Pattern while Onboarding" (fix version 3.7) and the Aug 28 sprint demo.

- **Syntax scope.** The ticket specifies wildcards and bracket ranges such as `[1-8]`. The Aug 28 demo described regex and showed "include v3 and v7, skip v5" in one pattern. Confirm whether full regex (for example alternation) is supported. Add examples only after the team confirms.
- **The v10 case.** The ticket lists `image:v10` as a non-match for `*:v[1-8]*`. Read as a wildcard with a range, `v10` starts with `v1` and would match. This page leaves `v10` out of the match and non-match lists and warns readers to test it. Confirm the real behavior.
- **Version label.** The Docker Hub and ACR pages say character ranges arrived in v3.5. The ticket fix version is 3.7. Confirm the version and fix the label on those pages.
- **Exclude and include order.** No source says which wins when an include and an exclude both match. Add it once confirmed.
- **Pattern test location.** Confirm where the pattern test sits in the onboarding form and add a screenshot. Add a screenshot of the info icon examples too.
- **Per-registry pages.** Only the Docker Hub and ACR pages carry the range tip. Harbor, Quay, ECR, GAR, Nexus and JFrog pages should link here once the syntax is confirmed.
-->
