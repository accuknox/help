---
hide:
  - toc
---

## Connectwise Integration

Integrate AccuKnox with Connectwise and receive AccuKnox alert notifications in your Connectwise account. With this integration, you can automate the process of generating Connectwise tickets with your existing security workflow.

To set up this integration, you need to coordinate with your Connectwise administrator and gather the inputs needed to enable communication between AccuKnox and Connectwise.

### Integration of Connectwise:
#### **a. Prerequisites**

+ You need a Service Desk URL , Company Id, Public key ,Private key & Client Id for this integration.
+ Go to this link :https://developer.connectwise.com/ClientID and fill the form to recieve your client id.
+ To get public and private keys go to your Connectwise manage page → system → members → API keys and create new API keys , here you will receive a public and private key.

#### **b. Steps to Integrate:**
+ Go to Channel Integration -> CSPM.
+ Click on add connector and select Connectwise

![](/integrations/images/connect1.png)
![](/integrations/images/connect2.png)

Enter the following details to configure Connectwise.

   + **Integration Name:** Enter the name for the integration. You can set any name. e.g.,```Testconnectwise```
   + **Service Desk URL**: Enter the URL of your Connectwise manage website. e.g., for ```https://staging.connectwisedev.com/CD019....```  enter the url as ```https://staging.connectwisedev.com/```
   + **Company Id**: Enter your Connectwise Company Id here. e.g., ```Connectwise_1```
   + **Public key and Private key**: Generate a public and private key by going to system → members → API keys and put the values respectively.
   + **Client Id**: To receive your client Id  go to this link:  https://developer.connectwise.com/ClientID and fill the form for Client Id.
   + Click **Save** to save the Integration.

![](/integrations/images/connect3.png)

Click on the Connectwise ticketing backend to **add configuration**.

Here Enter the following details:

   + **Configuration name:** this name will be displayed under ticket configuration while creating tickets.
   + **Default template:** to specify the of data that this configuration will be used for making tickets.
   + **Companies** : From the list of companies choose the company where you want to receive tickets.
   + **Issue Type:** You can choose from the dropdown.
   + Fill the priority mapping according to your choice and press **save**.


You can now configure Alert Triggers for Connectwise.

- - - 

[SCHEDULE DEMO](https://www.accuknox.com/contact-us){ .md-button .md-button--primary }