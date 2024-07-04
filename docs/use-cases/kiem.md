# Kubernetes Identity and Entitlement Management (KIEM)

KIEM is a cutting-edge solution designed to address security challenges in dynamic, auto-scaling kubernetes infrastructures. It offers continuous visibility, security event detection, centralized permissions management, and seamless integration with runtime environments. AccuKnox's stands out as one of the first CNAPP solutions to provide out-of-the-box KIEM functionality. This is particularly crucial given that over 65% of Kubernetes administrators struggle with properly configuring and analyzing RBAC policies.

## Key Features

- Multi-cloud visibility
- Enhanced identity and access management
- Automatic detection and remediation
- Audit-ready compliance and governance
- Flexible and resilient decentralized architecture
- 99.95% uptime SLA
- Real-time visualization and detailed audit logs

## Onboarding Process

Follow these steps to set up and start using AccuKnox KIEM:

### Install KIEM Agents

1. Navigate to the "Manage Cluster" section in your AccuKnox dashboard.
2. Select the target cluster for KIEM installation.
3. Install the KIEM job on the selected cluster.
4. Set up and schedule the cron job for regular scans.

![](./images/kiem/kiem-select-cluster.png)

### Define Admin Users

1. Access the KIEM console configuration.
2. Set up administrative access credentials.
3. Define roles and permissions for KIEM administrators.

### Review Pre-built Dashboards

1. Explore the default dashboards provided by KIEM.
2. Familiarize yourself with relationship graphs and risk queries.
3. Understand the overview of your cluster's security posture.

### Customize Searches and Alerts

1. Tailor search parameters to your specific deployment needs.
2. Set up custom alerts based on your security policies.
3. Define thresholds for various security metrics.

### Configure Notifications

1. Set up alert channels (email, Slack, etc.).
2. Define notification rules for different severity levels.
3. Establish escalation procedures for critical alerts.

## Post-Onboarding Steps

After completing the onboarding process:

1. Wait for the initial KIEM cron job to complete its first scan.
2. Once the scan is finished, navigate to the "Identity > KIEM" section in your dashboard.
3. Review the initial findings and adjust configurations as necessary.

## KIEM Features

### Permissions Overview

- Summarizes all permissions in a unified view.
- Filter on constraints such as Role, Rule, Verbs, Service Accounts.
- View distilled permission summary for filtered entities.

![](./images/kiem/kiem-filter.png)

![](./images/kiem/kiem-filter-2.png)

### Key Queries

Pre-defined queries to examine critical entities and their connections:

- Example: Identify Service Accounts not connected to any workloads (indicator of dormant excessive permissions).

![](./images/kiem/kiem-query.png)

### Full-text Search

Search across all RBAC entities:

- ServiceAccounts
- RoleBindings
- Roles And more

![](./images/kiem/kiem-full-text-search.png)

### Entity Exploration

- View connections and manifest for any entity.
- Discover excessive permissions.

![](./images/kiem/kiem-excessive-permission.png)

![](./images/kiem/kiem-cluster-role.png)

- Explore all RBAC entities:
  - Service Accounts
  - Namespaces
  - Users
  - Groups
  - Roles
  - RoleBindings

![](./images/kiem/kiem-rbac-entities.png)

### Interactive Visualization

Open any entity and view all its connections by clicking on the link.

![](./images/kiem/kiem-connections.png)

## Use Case: Navigating RBAC Complexities

While Kubernetes RBAC provides powerful access management capabilities, it can become complex in large or dynamic environments. AccuKnox KIEM addresses these challenges through:

- **Intuitive Visualization**: Graphically represent RBAC relationships for easier understanding.
- **Powerful Search**: Quickly find and analyze specific permissions or entities.
- **Pre-defined Security Checks**: Automatically identify common misconfigurations or security risks.
- **Continuous Monitoring**: Track changes to RBAC configurations in real-time.
- **Compliance Mapping**: Align RBAC policies with industry standards and best practices.

By leveraging these features, administrators can effectively manage relationships between key entities, monitor configuration changes, and ensure a more secure Kubernetes environment, all while reducing the complexity typically associated with RBAC management.

## Summary

AccuKnox KIEM provides a comprehensive solution for managing Kubernetes identity and entitlements. By offering deep visibility, powerful analysis tools, and intuitive visualizations, KIEM empowers administrators to maintain robust security postures in even the most complex Kubernetes environments.
