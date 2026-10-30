---
title: Automated Ticket Creation using Rules Engine
description: Automate ticket creation in AccuKnox by defining rules, severity, and data types for a streamlined incident response process.
---

# Automated Ticket Creation using Rules Engine

The Rules Engine allows users to customize and automate ticket creation by selecting the data type, defining the criticality, and configuring specific ticket settings. This ensures that customized tickets are created whenever the selected criteria is met, providing more control over the ticketing process.

In this section we can find the steps to create a ticket using Rule Engine in the AccuKnox platform.

## Prerequisites

A ticketing platform integrated to AccuKnox with a ticketing configuration created

**Note:** If the ticketing platform is not integrated yet, please follow the steps specified in the [Ticketing section](https://help.accuknox.com/integrations/jira-cloud/ "https://help.accuknox.com/integrations/jira-cloud/") for the platform you are using.

## Steps to set up Automated Ticket Creation

**Step 1:** Log in to the AccuKnox platform and navigate to Issues → Findings
![rules-engine-ticket-creation](./images/rules-engine-ticket-creation/1.png)

**Step 2:** Hover over to **Rule Engine** in Findings (Issues>Findings>Rule Engine)
![image-20241001-182655.png](./images/rules-engine-ticket-creation/2.png)

**Step 3:** Click on **Create Rule** to create an automated rule.
![image-20241014-043258.png](./images/rules-engine-ticket-creation/3.png)

**Step 4:** Provide the necessary details

- **Name**: A name to uniquely identify the rule

- **Description**: A few words to help understand the functionality of the rule

- **Condition**: The criteria to be checked against findings to apply the rule. Multiple conditions can be specified in a single rule and all the conditions must match for the rule to be applicable.

- **Expiration**: The time when this rule will become inactive, can be set to custom date. The rule will need to be updated after expiration.

![image-20241001-184952.png](./images/rules-engine-ticket-creation/4.png)

**Step 5:** Click on **Add Action.** In the Action tab, select **Create Ticket** and close.

![image-20241113-043101.png](./images/rules-engine-ticket-creation/5.png)

**Step 6:** After confirming the action, select the ticket configuration to be used to create the ticket from the dropdown.

![image-20241113-043309.png](./images/rules-engine-ticket-creation/6.png)

**Step 7:** The Save button is enabled after all the fields have been filled. Click on Save

![image-20241113-043802.png](./images/rules-engine-ticket-creation/7.png)

The rule has been created successfully and will create tickets for all findings that match the condition.

## Group Findings Under a Parent Ticket

The **Create Ticket** action has an optional **Parent** field. Pick a field to group by, and its value becomes the parent ticket name.

- On the first run, the Rule Engine creates the parent ticket.
- On every later run, it attaches new findings to that parent.

In Jira, the parent becomes a Story or an Epic and each finding becomes a task or sub-task. Grouping keys include Status, Location, Asset Name, Asset Type, Label, Vulnerability Name, Data Type, Risk Factor, and Unique Vulnerability Name. See [Smart Tickets: Parent-Child Automation](../getting-started/3.6-release.md#smart-tickets-parent-child-automation).
