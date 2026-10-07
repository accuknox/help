For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/install/deploy-defender/manage-defender.md).

The **Manage Defender** page helps you efficiently manage all aspects of your Defender deployments.

On the Manage Defenders page, you can carry out essential tasks such as:

- [Deploying the Defender](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/compute-edition/34/admin-guide/install/deploy-defender/deploy-defender.md)

- [Re-deploying the Defender](https://docs.prismacloud.io/admin-guide/install/deploy-defender/redeploy-defender)

- [Uninstalling the Defender](https://docs.prismacloud.io/admin-guide/install/deploy-defender/uninstall-defender)


For each Defender that you have deployed, the Manage Defender page displays the following information, including:

- **Host**: The host where the Defender is installed

- **Version**: The version of the Defender that is running

- **Cluster**: The cluster where the Defender is running

- **Account ID**: The cloud Account ID associated with the Defender

- **Type**: The type of Defender

- **Connection Status**: The current connection status

- **Messages**: Notifications, such as when an upgrade to the Defender is available

- **Collections**: The collection (a logical grouping of your organization’s assets) where the defender is running

- **Actions**: Available actions such as restarting, deleting, or upgrading the Defender, and viewing/downloading the Defender logs


## Deploying the Defender[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/manage-defender\#deploying-the-defender)

To deploy and configure specific Defender instances, choose from the following list of topics:

- Understanding Defenders









  - [Defender types](https://docs.prismacloud.io/admin-guide/install/deploy-defender/defender-types)


- Container Defender









  - [Single Container Defender using the UI](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/compute-edition/34/admin-guide/install/deploy-defender/container/container.md)

  - [Single Container Defender using the CLI](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/compute-edition/34/admin-guide/install/deploy-defender/container/container.md)


- Host Defender









  - [Host Defender](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/compute-edition/34/admin-guide/install/deploy-defender/host/host.md)

  - [Auto-defend hosts](https://docs.prismacloud.io/admin-guide/install/deploy-defender/host/auto-defend-host)

  - [Windows Host](https://docs.prismacloud.io/admin-guide/install/deploy-defender/host/windows-host)


- Orchestrator Defender









  - [Cluster Container Defender](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/compute-edition/34/admin-guide/install/deploy-defender/orchestrator/orchestrator.md)

  - [Cluster Container Defender in ECS](https://docs.prismacloud.io/admin-guide/install/deploy-defender/orchestrator/install-amazon-ecs)

  - [VMware Tanzu Application Service (TAS) Defender](https://docs.prismacloud.io/admin-guide/install/deploy-defender/orchestrator/install-tas-defender)


- App-Embedded Defender









  - [App-Embedded Defender](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/compute-edition/34/admin-guide/install/deploy-defender/app-embedded/app-embedded.md)

  - [App Embedded Defender for Fargate](https://docs.prismacloud.io/admin-guide/install/deploy-defender/app-embedded/install-app-embedded-defender-fargate)


- Serverless Defender









  - [Serverless Defender](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/compute-edition/34/admin-guide/install/deploy-defender/serverless/serverless.md)

  - [Serverless Defender (Lambda layer)](https://docs.prismacloud.io/admin-guide/install/deploy-defender/serverless/install-serverless-defender-layer)

  - [Auto-defend serverless functions](https://docs.prismacloud.io/admin-guide/install/deploy-defender/serverless/auto-defend-serverless)


## Runtime Restart Scenarios for Defenders[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/manage-defender\#runtime-restart-scenarios-for-defenders)

You can expect a runtime restart in the following scenarios:

- When a Defender starts.

- When a Defender stops.

- When you add the first blocking rule.

- When you remove the last blocking rule.

- When a Defender upgrades because the Defender restarts.


When Defender restarts in Openshift Kubernetes clusters, nodes may become `NotReady`. The nodes come back online after the `kubelet` restart is complete.

[PreviousAvailable Defender Types](https://docs.prismacloud.io/admin-guide/install/deploy-defender/defender-types) [NextRedeploy Defenders](https://docs.prismacloud.io/admin-guide/install/deploy-defender/redeploy-defender)

Last updated 3 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
