For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/audit/log-rotation.md).

Both Console and Defender call _log-rotate_ every 30 minutes. The options passed to log-rotate are described below.

## Defender[Direct link to heading](https://docs.prismacloud.io/admin-guide/audit/log-rotation\#defender)

The default path for Defender’s log file is _/var/lib/twistlock/log/defender.log_.

It is configured as follows:

- Truncate the original log file in place after creating a copy, instead of moving the old log file. (`copytruncate`)

- Have 10 backup files rotated. If rotation exceeds 10 files, the oldest rotated file is deleted. (`rotate 10`)

- Don’t generate an error in case a log file doesn’t exist. (`missingok`)

- Don’t rotate the log in case it’s empty. (`notifempty`)

- Rotate the log only if its size is 100M or more. (`size 100M`)

- Compress the rotated logs. (`compress`)


## Console[Direct link to heading](https://docs.prismacloud.io/admin-guide/audit/log-rotation\#console)

It is configured as follows:

- Truncate the original log file in place after creating a copy, instead of moving the old log file. (`copytruncate`)

- Have 10 backup files rotated. If rotation exceeds 10 files, the oldest rotated file is deleted. (`rotate 10`)

- Don’t generate an error in case a log file doesn’t exist. (`missingok`)

- Don’t rotate the log in case it’s empty. (`notifempty`)

- Rotate the log only if its size is 100M or more. (`size 100M`)

- Compress the rotated logs. (`compress`)


## DB logs[Direct link to heading](https://docs.prismacloud.io/admin-guide/audit/log-rotation\#db-logs)

We log CRITICAL/ERROR messages to enable critical DB diagnostics.

This is automatically done by Prisma Cloud and is non-configurable.

[PreviousSyslog and stdout integration](https://docs.prismacloud.io/admin-guide/audit/logging) [NextThrottling](https://docs.prismacloud.io/admin-guide/audit/throttling)

Last updated 3 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
