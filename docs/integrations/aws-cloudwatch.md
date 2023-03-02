---
hide:
  - toc
---


## AWS CloudWatch Integration

Navigate to Settings->Integrations. Choose **"AWS CloudWatch"** services and click the **Integrate Now** button.

### Integration of Amazon CloudWatch:

#### a. Prerequisites

+ AWS Access Key / AWS Secret Key is required for this Integration.

+ **[Note]:** Please refer this link to create access keys [link](https://aws.amazon.com/)

#### b. Steps to Integrate:

+ Go to Channel Integration URL
+ Click the Integrate Now button -> AWS CloudWatch
+ Here you'll be able to see these entries:
    + **Integration Name:** Enter the name for the integration. You can set any name.
    + **AWS Access Key:** Enter your AWS Access Key here.
    + **AWS Secret Key:** Enter your AWS Secret Key here.
    + **Region Name:** Enter your AWS Region Name here.
+ Once you fill every field then click the button this will test whether your integration is working or not.
+ Click the Save button.
#### 2. Configuration of Alert Triggers:
+ On the Logs page, after choosing specific log filter click on 'Create Trigger' button.
+ The below fields needs to be entered with appropriate data:
+ **Name:** Enter the name for the trigger. You can set any name without special characters.
+ **When to Initiate:** The frequency of the trigger as Real Time / .
+ **Status:** Enter the severity for the trigger.
+ **Search Filter Data :** The filter log chosen in automatically populated here.This is optional.
+ **Predefined queries:** The list of predefined queries for this workspace is shown as default.
+ **Notification Channel:** Select the integration channel that needs to receive logs. This should be AWS CloudWatch. (Note: Channel Integration is done on the previous step)
+ **Save:** Click on Save for the trigger to get stored in database.

#### 3. Logs Forwarding:
+ For each Enabled Trigger, please check the AWS platform to view the logs.
+ Based on Frequency (Real Time / Once in a Day / Week)
+ The Rule Engine matches the real time logs against the triggers created.