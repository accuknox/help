---
hide:
  - toc
---

## Splunk Integration

Splunk is a software platform to search, analyze, and visualize machine-generated data gathered from websites, applications, sensors, and devices.

AccuKnox integrates with Splunk and monitors your assets and sends alerts for resource misconfigurations, compliance violations, network security risks, and anomalous user activities to Splunk. To forward the events from your workspace you must have Splunk Depolyed and HEC URL generated first for Splunk Integration.

### Integration of Splunk:
#### a. Prerequisites:

Set up Splunk HTTP Event Collector (HEC) to view alert notifications from AccuKnox in Splunk. Splunk HEC lets you send data and application events to a Splunk deployment over the HTTP and Secure HTTP (HTTPS) protocols.

To set up **HEC**, use instructions in [Splunk documentation](https://docs.splunk.com/Documentation/Splunk/latest/Data/UsetheHTTPEventCollector). For source type,_json is the default; if you specify a custom string on AccuKnox, that value will overwrite anything you set here.

Select **Settings > Data inputs > HTTP Event Collector** and make sure you see HEC added in the list and that the status shows that it is **Enabled** .

#### b. Steps to Integrate:
+ Go to Settings->Integration.
+ Click integrate now on Splunk.

![](/integrations/images/splunk-int.png)

+ Enter the following details to configure Splunk.
+ **Select the Splunk App** : From the dropdown, Select Splunk Enterprise.

    + **Integration Name:** Enter the name for the integration. You can set any name. e.g., ``` Test Splunk ```
    + **Splunk HTTP event collector URL:** Enter your Splunk HEC URL generated earlier.e.g., ``` https://splunk-xxxxxxxxxx.com/services/collector ```
    + **Index:** Enter your Splunk Index, once created while creating HEC. e.g., ``` main ```
    + **Token:** Enter your Splunk Token, generated while creating HEC URL. e.g., ``` x000x0x0x-0xxx-0xxx-xxxx-xxxxx00000 ```
    + **Source:** Enter the source as http: `` kafka ``

    + **Source Type:** Enter your Source Type here, this can be anything and the same will be attach to the event type forwarded to splunk. e.g.,``` _json ```

    + Click **Test** to check the new functionality, You will receive the test message on configured splunk server. e.g.,``` Test Message host = xxxxxx-deployment-xxxxxx-xxx00 source = http:kafka sourcetype = trials ```
+ Click **Save** to save the Integration. You can now configure Alert Triggers for Splunk Events

- - - 
[SCHEDULE DEMO](https://www.accuknox.com/contact-us){ .md-button .md-button--primary }