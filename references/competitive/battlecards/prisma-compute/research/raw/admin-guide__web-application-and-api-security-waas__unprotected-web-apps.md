For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/unprotected-web-apps.md).

Prisma Cloud scans your environment for containers and hosts that run web apps and reports any that aren’t protected by WAAS.

During the scan, Prisma Cloud detects HTTP servers listening on exposed ports and flags them if they are not protected by WAAS.

Unprotected web apps are flagged on the radar view and are also listed in **Monitor > WAAS > Unprotected web apps**.

The following screenshot shows how Radar shows an unprotected web app:

![waas unprotected web apps radar](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-fe88a0b6354041f59e76666a0cda5beec5871a34%252Fwaas_unprotected_web_apps_radar.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=8ba3fbd596244d081e3882edf7a04168&sv=3)

## Report for unprotected web apps[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/unprotected-web-apps\#report-for-unprotected-web-apps)

The following screenshot shows how unprotected web apps are reported in **Monitor > WAAS > Unprotected web apps**:

![waas unprotected web apps report](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-bdf5cdef86b58fa3473e007084704ce51db9e49c%252Fwaas_unprotected_web_apps_report.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=397df6196786247d9290ed8d1e5351ff&sv=3)

In the `Containers` tab, the report lists the images containing unprotected web apps, the number of containers running those images, and the ports exposed in the running containers.

In the `Hosts` tab, the report lists the hosts on which unprotected web apps are running, the number of processes running those apps, process names and the ports exposed in the hosts.

This information can be used when adding new WAAS rules to protect containers and hosts.

Above the table is the date of the latest scan. The report can be refreshed by clicking the refresh button.

Users can export the list in CSV format. The CSV file has the following fields:

- **Containers** \- Image, Host, Container, ID, Listening ports

- **Hosts** \- ID, Unprotected processes


## Filtered processes[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/unprotected-web-apps\#filtered-processes)

The following list of processes is not included in the WAAS unprotected web apps detections:

**Kubernetes/Docker**

- coredns

- kube-proxy

- docker

- docker-proxy

- kubelet

- openshift

- dcos-metris

- dcos-metris-agent

- containerd


**Databases**

- mysql

- mysqld

- mongod

- postgres

- influxd

- redis-server

- asd

- rethinkdb


**Proxies**

- haproxy

- envoy

- squid

- traefik


**SSH binaries**

- sshd

- ssh


**WAAS proxy process**

- defender


## Disabling scans for unprotected web apps[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/unprotected-web-apps\#disabling-scans-for-unprotected-web-apps)

By setting the `Scan for unprotected web applications` toggle to the **Disabled** position, users are able to disable periodic scanning for unprotected web applications and APIs.

The toggle in either the `Containers` or `Hosts` tabs will disable scanning of containers and hosts simultaneously when disabled.

[PreviousCustom rules](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-custom-rules) [NextWAAS Sensitive Data](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/log-scrubbing)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
