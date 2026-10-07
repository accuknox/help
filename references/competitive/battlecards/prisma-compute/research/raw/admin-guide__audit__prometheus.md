For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/audit/prometheus.md).

Prometheus is a monitoring platform that scrapes the published endpoints of targets to collect their metrics. You can configure Prisma Cloud to be a Prometheus target.

You can use Prometheus to monitor time series data across your environment and show high-level, dashboard-like, stats to visualize trends and changes. Prisma Cloud’s instrumentation lets you track metrics such as the total number of connected Defenders and the total number of container images in your environment that your Defenders protect.

## Metrics[Direct link to heading](https://docs.prismacloud.io/admin-guide/audit/prometheus\#metrics)

Metrics are a core Prometheus concept. Instrumented systems expose metrics. Prometheus stores the metrics in its time-series database, and makes them easily available to query to understand how systems behave over time.

Prisma Cloud has two types of metrics:

- Counters: Single monotonically increasing values. A counter’s value can only increase or be reset to zero.

- Gauges: Single numerical values that can arbitrarily go up or down.


### Prisma Cloud metrics[Direct link to heading](https://docs.prismacloud.io/admin-guide/audit/prometheus\#prisma-cloud-metrics)

All Prisma Cloud metrics are listed in the following table. Vulnerability and compliance metrics are updated every 24 hours. The rest of the metrics are updated every 10 minutes.

The **vulnerabilities** and **compliance** metrics report the number of many entities, for example images, containers, or hosts, that are at risk by the highest severity issue impacting them. The **images\_critical\_vulnerabilities** is not the total count of critical vulnerabilities in the images in your environment. It is the total count of images where the highest severity CVE is critical. For a thorough explanation of this type of metric, see [Vulnerability Explorer](https://docs.prismacloud.io/admin-guide/vulnerability-management/vuln-explorer#roll-ups).

Metric

Type

Description

totalDefenders

Gauge

Total number of Defenders connected to Console. Connected and disconnected Defenders can be reviewed in Console under **Manage > Defenders > Manage**.

activeDefenders

Gauge

Total number of all Defenders for which a license is allocated, regardless of whether it is currently connected to Console or not.

images\_critical\_vulnerabilities

Gauge

Total number of containers impacted by critical vulnerabilities.

images\_high\_vulnerabilities

Gauge

Total number of containers impacted by high vulnerabilities.

images\_medium\_vulnerabilities

Gauge

Total number of containers impacted by medium vulnerabilities.

images\_low\_vulnerabilities

Gauge

Total number of containers impacted by low vulnerabilities.

hosts\_critical\_vulnerabilities

Gauge

Total number of hosts impacted by critical vulnerabilities.

hosts\_high\_vulnerabilities

Gauge

Total number of hosts impacted by high vulnerabilities.

hosts\_medium\_vulnerabilities

Gauge

Total number of hosts impacted by medium vulnerabilities.

hosts\_low\_vulnerabilities

Gauge

Total number of hosts impacted by low vulnerabilities.

serverless\_critical\_vulnerabilities

Gauge

Total number of serverless functions impacted by critical vulnerabilities.

serverless\_high\_vulnerabilities

Gauge

Total number of serverless functions impacted by high vulnerabilities.

serverless\_medium\_vulnerabilities

Gauge

Total number of serverless functions impacted by medium vulnerabilities.

serverless\_low\_vulnerabilities

Gauge

Total number of serverless functions impacted by low vulnerabilities.

images\_critical\_compliance

Gauge

Total number of images impacted by critical compliance issues.

images\_high\_compliance

Gauge

Total number of images impacted by high compliance issues.

images\_medium\_compliance

Gauge

Total number of images impacted by medium compliance issues.

images\_low\_compliance

Gauge

Total number of images impacted by low compliance issues.

containers\_critical\_compliance

Gauge

Total number of containers impacted by critical compliance issues.

containers\_high\_compliance

Gauge

Total number of containers impacted by high compliance issues.

containers\_medium\_compliance

Gauge

Total number of containers impacted by medium compliance issues.

containers\_low\_compliance

Gauge

Total number of containers impacted by low compliance issues.

hosts\_critical\_compliance

Gauge

Total number of hosts impacted by critical compliance issues.

hosts\_high\_compliance

Gauge

Total number of hosts impacted by high compliance issues.

hosts\_medium\_compliance

Gauge

Total number of hosts impacted by medium compliance issues.

hosts\_low\_compliance

Gauge

Total number of hosts impacted by low compliance issues.

serverless\_critical\_compliance

Gauge

Total number of serverless functions impacted by critical compliance issues.

serverless\_high\_compliance

Gauge

Total number of serverless functions impacted by high compliance issues.

serverless\_medium\_compliance

Gauge

Total number of serverless functions impacted by medium compliance issues.

serverless\_low\_compliance

Gauge

Total number of serverless functions impacted by low compliance issues.

active\_app\_firewalls

Gauge

Total number of active app firewalls (WAAS).

app\_firewall\_events

Gauge

Total number of app firewall (WAAS) events.

protected\_containers

Gauge

Total number of protected containers.

container\_runtime\_events

Gauge

Total number of container runtime events.

host\_runtime\_events

Gauge

Total number of host runtime events.

access\_events

Gauge

Total number of access events.

registry\_images

Gauge

The total number of registry images scanned.

container\_active\_incidents

Gauge

The total number of container active incidents.

container\_archived\_incidents

Gauge

The total number of container archived incidents.

host\_active\_incidents

Gauge

The total number of host active incidents.

host\_archived\_incidents

Gauge

The total number of host archived incidents.

incident\_snapshots

Gauge

The total number of incident snapshots on the console.

incident\_snapshots\_size\_mb Gauge The size in MB of incident snapshots

backups

Gauge

The total backups stored in a system.

ci\_image\_scan\_results

Gauge

The total number of CI scanning results in the Prisma Cloud Console.

tenant\_project\_connectivity

Gauge

For tenant projects, returns 1 if the tenant project is connected to the main console.

compliance\_rules\_consumed\_collections

Gauge

The total number of collections consumed by compliance rules.

vulnerability\_rules\_consumed\_collections

Gauge

The total number of collections consumed by vulnerability rules.

runtime\_rules\_consumed\_collections

Gauge

The total number of collections consumed by runtime rules.

api\_requests

Counter

Total number of requests to the Prisma Cloud API.

defender\_events

Counter

## Integrate Prisma Cloud with Prometheus[Direct link to heading](https://docs.prismacloud.io/admin-guide/audit/prometheus\#integrate-prisma-cloud-with-prometheus)

The Prometheus server scrapes endpoints at configurable time intervals. Regardless of the value you set for the Prometheus scrape interval, new Prisma Cloud data is only available at the following refresh rates.

- Vulnerability and compliance data is refreshed every 24 hours.

- All other data is refreshed every 10 minutes.


This procedure shows how to complete the following tasks.

1. Enable the Prometheus integration.

2. Configure the Prisma Cloud scrape.

3. Start a Prometheus server running in a container.


If you already have a Prometheus server in your environment, you only need to enable the integration and configure the scrape.

1. Enable the Prometheus integration.









1. Log into Prisma Cloud Console.

2. Go to **Manage > Alerts > Logging**.

3. Set **Prometheus instrumentation** to **Enabled**.


2. Prepare a scrape configuration file for the Prometheus server.









1. Create a new `prometheus.yml` file, and open it for editing.

2. Enter the following configuration fields.

















      AskCopy



      ```
      global:
        scrape_interval:     15s # Set the scrape interval to every 15 seconds. Default is every 1 minute.
        evaluation_interval: 15s # Evaluate rules every 15 seconds. The default is every 1 minute.

      # Prisma Cloud scrape configuration.
      scrape_configs:
  - job_name: 'twistlock'
    static_configs:
    - targets: ['CONSOLE_ADDRESS:8083']
    metrics_path: /api/v1/metrics
    basic_auth:
      username: 'USER'
      password: 'PASS'
```

      - Replace `CONSOLE_ADDRESS` with the DNS name or IP address for Prisma Cloud Console.

      - Replace `USER` with a Prisma Cloud user, which has the minimum role of **Auditor**.

      - Replace `PASS` with that Prisma Cloud user’s password.


3. Start the Prometheus server with the scrape configuration file.

















   AskCopy



   ```
   $ docker run \
     --rm \
     --network=host \
     -p 9090:9090 \
     -v /PATH_TO_YML/prometheus.yml:/etc/prometheus/prometheus.yml \
     prom/prometheus
   ```

4. Go to http://<PROMETHEUS\_HOST>:9090/targets to validate that the Prisma Cloud integration is properly set up.















   ![prometheus target up](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-80e1dbf93c937b7c61241d2dba081f3e8886e822%252Fprometheus_target_up.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=a0a5059074fe2b4a1d71f7b5afb25d00&sv=3)











   To get results immediately for testing, restart the prisma Cloud Console. If you are using the PCEE, wait 10 minutes for the first refresh window to elapse.


## Create a simple graph[Direct link to heading](https://docs.prismacloud.io/admin-guide/audit/prometheus\#create-a-simple-graph)

Create a graph that shows the number of deployed Defenders.

1. Go to http://<PROMETHEUS\_HOST>:9090/graph

2. Click **Add Graph**.

3. In the drop-down list, select **twistlock\_total\_defenders**.

4. Click **Execute**. In the **Console** tab, you see the value for total number of Defenders connected to the Prisma Cloud Console.

5. Open the **Graph** tab to see a visual representation of how the number of Defenders has changed over time.















   ![prometheus simple graph](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-7ff1f50b3c67e7d4dd0c939c337e16dc8b5a9c4c%252Fprometheus_simple_graph.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=c77f93cdbb2810e8eb2b4c01f035e0f1&sv=3)


[PreviousThrottling](https://docs.prismacloud.io/admin-guide/audit/throttling) [NextKubernetes auditing](https://docs.prismacloud.io/admin-guide/audit/kubernetes-auditing)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
