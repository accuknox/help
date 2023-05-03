---
hide:
  - toc
---

## Freshservice Integration

Integrate AccuKnox with Freshservice and receive AccuKnox alert notifications in your Freshservice accounts. With this integration, you can automate the process of generating Freshservice “Problem alerts“ with your existing security workflow.

To set up this integration, you need to coordinate with your Freshservice administrator and gather the inputs needed to enable communication between AccuKnox and Freshservice.

### Integration of Freshservice:
#### **a. Prerequisites**

+ You need a Company domain , Email & API key (secret) for this integration.
+ You can find your API key in profile settings in the right side column.
#### **b. Steps to Integrate:**
+ Go to Channel Integration -> CSPM.
+ Click on add connector and select Freshservice

![](/integrations/images/Freshw1.png)
![](/integrations/images/Freshw2.png)

Enter the following details to configure JIRA.

   + **Integration Name:** Enter the name for the integration. You can set any name. e.g.,```TestFreshservice```
   + **Domain Name**: Enter the site name of your organization as shown in your URL. e.g., for ```https://accuknoxexample.freshservice.com/``` enter the domain name as ```accuknoxexample```.
   + **User Email**: Enter your Freshservice account email address here. e.g., ```freshservice@organisation.com```
   + **Secret**: Enter the API key Here. This can be found in profile settings.
   + Click **Save** to save the Integration.

![](/integrations/images/Freshw3.png)

Click on the Freshservice ticketing backend to add configuration.

Here Enter the following details:

   + **Configuration name:** this name will be displayed under ticket configuration while creating tickets.
   + **Default template:** to specify the of data that this configuration will be used for making tickets.
   + **Issue Type:** You can choose from the dropdown.
   + Fill the priority mapping according to your choice and press **save**.


You can now configure Alert Triggers for Freshservice.

- - - 
[SCHEDULE DEMO](https://www.accuknox.com/contact-us){ .md-button .md-button--primary }