## **Logs:** 

Accuknox CNAPP Solution provides comprehensive visibility of the cloud assets with the help of Dashboards and logs/alerts. AccuKnox’s open source KubeArmor can forward policy related logs/alerts to the SaaS. Also it can forward the container logs that is present in the workloads. We can also use Feeder service agent to pass the logs to other SIEM tools like Splunk, ELK, Rsyslog, etc.., User can also forward the logs from AccuKnox SaaS using the channel integration option to these SIEM tools. 

The Logs summary in Accuknox displays a complete list of log events that have occurred within the infrastructure during a defined timeline.

It provides an interface to:

Find and get insights into security events in your infrastructure

Filter the logs to hone into the events that will require further inspection

Inspect any specific event using a log detail panel

Sent customized alerts to third-party SIEM (security information and event management) platforms and logging tools, such as Slack, Splunk, Elastic Search, Cloud watch, Jira with the help of trigger.

Logs are generated in real-time based on certain conditions/rules you configure on the security policies. You will get logs from four different components

![](/saas/images/logs-dash.png)
 

**K8s-cluster/VM**
To access all the logs from your Kubernetes clusters, select K8s-cluster from the first drop-down menu. Select VM to examine the logs for your virtual machines.

**Cluster**
cluster drop-down can be used to filter logs related to specific clusters

**Namespace**
Namespace drop-down can be used to filter logs related to specific namespaces

**Severity**
Use the appropriate options to filter log events by Critical, High, Medium, Low, and Info level of severity, corresponding to the levels defined in the relevant runtime Policies.

**Time Ranges**
As in the rest of the platform interface, the time range can be set by date ranges and in increments from 5 minutes to 60 days.