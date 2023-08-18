---
hide:
  - toc
---


### Slack Integration:

To send an alert notification via Slack you must first set up the Slack notification Channel.

##Integration of Slack:

#### **a. Prerequisites:**
You need a valid and active account in Slack.
After logging into your Slack channel, you must generate a Hook URL.

**Note :** To generate Hook URL follow the steps, [Webhooks-for-Slack](https://slack.com/intl/en-in/help/articles/115005265063-Incoming-webhooks-for-Slack) .

#### **b. Steps to Integrate:**
+ Go to Channel Integration.
+ Click integrate now on Slack.

![](/integrations/images/slack-int.png)

+ Fill up the following fields:

+ **Integration Name:** Enter the name for the integration. You can set any name. e.g., ``` Container Security Alerts ```

+ **Hook URL:** Enter your generated slack hook URL here. e.g., ``` https://hooks.slack.com/services/T000/B000/XXXXXXX ```

+ **Sender Name:** Enter the sender name here. e.g., ``` AccuKnox User ```

+ **Channel Name:** Enter your slack channel name here. e.g.,  ```  livealertsforcontainer ```

+ Click **Test** to check the new functionality, You will receive the test message on configured slack channel. ``` Test message Please ignore !! ```

+ Click **Save** to save the Integration. You can now configure Alert Triggers for Slack Notifications.

- - - 
[SCHEDULE DEMO](https://www.accuknox.com/contact-us){ .md-button .md-button--primary }