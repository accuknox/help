For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/runtime-defense/runtime-defense-aggregation.md).

When multiple events of the same type occur in quick succession, Prisma Cloud implements event aggregation to prevent the console from displaying the same audits repetitively.

## Conditions for Event Aggregation[Direct link to heading](https://docs.prismacloud.io/admin-guide/runtime-defense/runtime-defense-aggregation\#conditions-for-event-aggregation)

Event aggregation starts when the following conditions are met:

- Events are generated on the same resource, such as a specific image on a host.

- Events fall within the same "event type" category.


## Event Aggregation Process[Direct link to heading](https://docs.prismacloud.io/admin-guide/runtime-defense/runtime-defense-aggregation\#event-aggregation-process)

The event aggregation process depends on the following criteria:

- Grace period: A period during which no events are displayed or counted towards aggregation. In Prisma Cloud, it is a 15-minute period without audits since the last event.

- Throttle period: A waiting period before setting the aggregation mode. It is the time within which events must occur to qualify for aggregation. In Prisma Cloud, the throttle period is 15 minutes.

- Aggregation mode: A state activated when specific criteria are met: the grace period of 15 minutes is complete and then 5 qualifying events occur within the throttle period of 15 minutes. In aggregation mode, the Defender combines multiple events into a single aggregated event. This reduces repetitive displays of similar audits.


**Prisma Cloud Event Aggregation Process**

1. Event monitoring: Defender monitors for audit events.

2. Grace period and throttle period check:









   - After event detection, Defender checks whether a 15-minute grace period (without audits) has passed since the last event.

   - After the grace period is completed, Defender assesses whether the throttle period (set to 15 minutes) has elapsed since the first event. Throttle period is the waiting period before setting the aggregation mode.

   - If both the grace period and throttle period conditions are not met, Defender waits for additional events.


3. Activation of aggregation mode:









   - On meeting the criteria (the grace period of 15 minutes is complete and then 5 qualifying events occur within the throttle period of 15 minutes), Defender activates the aggregation mode.

   - It verifies whether the aggregation period, set to 10 minutes, has passed since the last aggregation.

   - If the aggregation period has not passed, Defender waits for more events.


4. Display of Aggregated Events:









   - After all criteria are met, including compliance with the category limit, Defender sends the aggregated event to the console.


5. Resumption of Normal Operation:









   - Normal operation resumes when the grace period expires without new messages or when the throttle period lapses from the first event.

   - Defender resets the counter, establishes the aggregation period again, and resumes monitoring for audit events.


This process is illustrated using the following flowchart:

![aggregation audit](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-00714fb015f6b1be941122fa3e4e732a8250899b%252Faggregation-audit.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=07d35fe45034eea75fb87fea754c7978&sv=3)

## Displaying Audit Information[Direct link to heading](https://docs.prismacloud.io/admin-guide/runtime-defense/runtime-defense-aggregation\#displaying-audit-information)

Prisma Cloud displays the summarized audit information in the following format: `The most recent individual audit, along with the aggregated message count.`

For example:

`High rate of <event type>, reporting aggregation started; Last event: <event name> launched from <path> but is not found in the runtime model. In the past 10 minutes, container <name> had <number of event occurrences> of <event type>.`

![runtime defense aggregation](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-c372eaafc336f6ddf0e2945c39fba6ab7c3f4948%252Fruntime_defense_aggregation.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=54e64f2a90e24c79a72eb506a99c60dc&sv=3)

[PreviousRuntime audits](https://docs.prismacloud.io/admin-guide/runtime-defense/runtime-audits) [NextAggregation of Events by Defender](https://docs.prismacloud.io/admin-guide/runtime-defense/event-aggregation-categorization-table)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
