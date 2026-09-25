---
title: IBM QRadar Integration
description: Forward AccuKnox security alerts to IBM QRadar via webhook and Syslog for centralized SIEM monitoring and incident response.
---

# IBM QRadar Integration

## Integration Architecture

The integration flow enables alert forwarding from AccuKnox to IBM QRadar. Alerts generated in the AccuKnox UI, sourced from findings and various alert sources, are processed by a rules engine and triggers according to the configured settings. These alerts are then transported via a webhook server set up in the customer environment, using the Syslog protocol to forward them to IBM QRadar, which serves as the final destination for receiving the alerts.

![Integration Architecture](./images/ibm-qradar/arch-qradar.png)

### Architecture Components

1. AccuKnox platform (source)
2. Webhook server (intermediary)
3. Syslog protocol (transport)
4. IBM QRadar (destination)

### Customer Integration Process

- Configure webhook in AccuKnox (See [**Webhook Integration Guide**](https://help.accuknox.com/integrations/webhook-integration/)).
- Set up QRadar configuration (customer responsibility).
- Report configuration completion back to AccuKnox.

---

## Connector and Send Event

1. Log in to QRadar as `Admin`.

    ![QRadar Admin Login](./images/ibm-qradar/1.png)

2. Click `Admin` and then `Data Source`.

    ![QRadar Data Source](./images/ibm-qradar/2.png)

3. Click `Log Source`.

    ![QRadar Log Source](./images/ibm-qradar/3.png)

4. Click `+ New Source Log` -> `Single Source`.

    ![New Source Log](./images/ibm-qradar/4.png)

    ![Single Source Selection](./images/ibm-qradar/5.png)

5. Configurations:
    1. Select Log Source Type - `Universal DSM`
    2. Select a Protocol - `Syslog`
    3. Name - `Test Qradar`
    4. Log Source Identifier - `192.168.1.226` (Source IP from which Log is forwarded to Qradar)

    ![Configuration Details](./images/ibm-qradar/6.png)

6. Go back to `Admin` again to deploy changes. Click `Deploy Changes`, wait for changes to be deployed.

    ![Deploy Changes 1](./images/ibm-qradar/7.png)

    ![Deploy Changes 2](./images/ibm-qradar/8.png)

7. Now go to `Log Activity` to see All Alerts.

8. Now trigger the Event. You will be alerted in real-time in the Qradar UI.
    1. Test Event

        ![Test Event](./images/ibm-qradar/9.png)

    2. Event in Qradar UI

        ![Event UI 1](./images/ibm-qradar/10.png)

        ![Event UI 2](./images/ibm-qradar/11.png)

        ![Event UI 3](./images/ibm-qradar/12.png)

## Check QRadar IP

1. Go to Admin.
2. Click System Configuration.
3. Click `System and License Management`.

    ![System Configuration](./images/ibm-qradar/13.png)

    ![System License Management](./images/ibm-qradar/14.png)
