# Automated Ticket Creation using Rules Engine

The Rules Engine allows users to customize and automate ticket creation by selecting the data type, defining the criticality, and configuring specific ticket settings. This ensures that tickets are created based on the selected criteria, providing more control over the ticketing process.

In this section we can find the steps to create a ticket using Rule Engine in the AccuKnox SaaS platform:

**Step 1:** Log in to [app.demo.accuknox.com](https://app.demo.accuknox.com/ "https://app.demo.accuknox.com") and navigate to the CNAPP dashboard.

![alt](images/rules-engine-ticket-creation/1.png)

**Step 2:** Hover over to **Rule Engine** in Findings (Issues>Findings>Rule Engine)

![alt](images/rules-engine-ticket-creation/2.png)

**Step 3:** Click on **Create Rule** to create an automated rule.

![alt](images/rules-engine-ticket-creation/3.png)

**Step 4:** Provide the necessary details, including the rule name, rule description, condition type (true or false), and click on "Action" to add the specific action. When the conditions specified here are matched by a finding, the rule will trigger the specified action.

![alt](images/rules-engine-ticket-creation/4.png)

**Step 5:** Click on **Create Ticket** to initiate creation of ticket when a finding with a matching the is found.

![alt](images/rules-engine-ticket-creation/5.png)

**Step 6:** After finalizing the condition, select the ticketing template from the drop down and save it to execute.

![alt](images/rules-engine-ticket-creation/6.png)

**Step 7:** User needs to create the ticketing configuration via [Fresh Service Integration](https://help.accuknox.com/integrations/freshservice-cspm/ "https://help.accuknox.com/integrations/freshservice-cspm/"), which helps in automating the process of generating Freshservice "Problem alerts" with the existing security workflow.

Make sure to follow the link [Freshservice](https://help.accuknox.com/integrations/freshservice-cspm/) to configure the fresh service integration.

**Step 8:** To view the ticketing integrations, hover over to CSPM in integrations and select the respective integration.**(Home>Settings>Integrations>CSPM)**

![alt](images/rules-engine-ticket-creation/8.png)

**Step 9:** Click on the desired integration, fill in the required details, and hit **add configuration** to create the ticket.

![alt](images/rules-engine-ticket-creation/9.png)

**Step 10:** Review the ticket configuration and save the details. The ticket will be created automatically, and the rule will be applied.

![alt](images/rules-engine-ticket-creation/10.png)
