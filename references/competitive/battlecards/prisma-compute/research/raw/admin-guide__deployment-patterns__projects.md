For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/deployment-patterns/projects.md).

Some deployments must be compartmentalized for regulatory or operational reasons. Projects solve the problem of multi-tenancy. Each project, or tenant, consists of a Console and its Defenders. Each project is a separate, compartmentalized environment which operates independently with its own rules and configurations.

Projects are federated behind a single master Console with a single URL. For example, https://console.customer.com might be the URL for accessing the master Console UI and API. Tenant projects are deployed, accessed, and managed from the single master Console. You could deploy a tenant Console for each business unit, giving each team their own segregated environment. Each team accesses their tenant through the master Console’s URL.

Role-based access control (RBAC) rules manage who can access which project. When users log onto Prisma Cloud Central Console, they are shown a list of projects to which they have access and can switch between them.

Scale projects have been deprecated. If you’ve deployed a scale project, see [migration options for scale projects](https://docs.prismacloud.io/admin-guide/deployment-patterns/migration-options-for-scale-projects) for more information about how to transition to a supported configuration.

## Terminology[Direct link to heading](https://docs.prismacloud.io/admin-guide/deployment-patterns/projects\#terminology)

The following terms are used throughout this article:

Central Console
Also known as the master Console or just master. This is the interface from which administrators manage (create, access, and delete) their projects.

Supervisor
Secondary, slave Console responsible for the operation of a project. Supervisor Consoles are headless. Their UI and API are not directly accessible. Instead, users interact with a project from Central Console’s UI and API.

Project (also tenant project, or just tenant)
Deployment unit that consists of a supervisor Console and it’s connected Defenders. Tenant projects are like silos. Each tenant maintains its own rules and settings, separate from Central Console and any other tenant.

## When to use projects[Direct link to heading](https://docs.prismacloud.io/admin-guide/deployment-patterns/projects\#when-to-use-projects)

Carefully assess whether you need projects. Provisioning projects when they are not required will needlessly complicate the operation and administration of your environment.

**1\. Do you have multiple segregated environments, where each environment must be configured with its own rules and policies?**

If yes, then deploy a tenant project for each environment.

**2\. If you choose not to use projects now, can you migrate to projects at a later time?**

Yes. Even if you choose not to use projects now, you’re not locked into that decision. You can always migrate to projects at a later time. For more information, see [Migration strategies](https://docs.prismacloud.io/admin-guide/deployment-patterns/projects#_migration_strategies).

## Architecture[Direct link to heading](https://docs.prismacloud.io/admin-guide/deployment-patterns/projects\#architecture)

Projects federate the UI and API for multiple Consoles.

For example, if you have three separate instances of Consoles for development, test, and production environments, projects let you manage all of them from a single Central Console. With projects, one Console is designated as the master and all others are designated as supervisors. Thereafter, all UI and API requests for a project are proxied through the master and routed to the relevant supervisor. Supervisors do not serve a UI or API.

![projects arch](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-37c015843bffefe12cc018d52f8c87cb04daff3a%252Fprojects_arch.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=981ccb075a6281dbbe197ceec0651f01&sv=3)

### Connectivity[Direct link to heading](https://docs.prismacloud.io/admin-guide/deployment-patterns/projects\#connectivity)

By default, the master and its supervisor Consoles communicate over port 8083. You can configure a different port by setting MANAGEMENT\_PORT\_HTTPS in _twistlock.cfg_ at install time. All Consoles must use the same value for MANAGEMENT\_PORT\_HTTPS. Communication between the master and supervisor Consoles must be direct, and cannot be routed through a proxy.

Defenders communicate with their respective supervisor Consoles. Project Defenders never communicate directly with the Central Console.

Prisma Cloud CA signed certs are used for establishing the Central Console to supervisor Console communication link. Since no user interacts with the supervisor Console directly, the link is an internal architecte detail, and we use our own CA. This setup reduces the risk of outages due to expired certs.

When configuring Central and supervisor Consoles, you must configure the supervisor Console to [include the Subject Alternative Name (SAN)](https://docs.prismacloud.io/admin-guide/configure/subject-alternative-names) for the Central Console.

When configuring access to the Consoles via Ingress Network Routes in Kubernetes, you must add the Central Console to the supervisor Console Ingress configuration.

Central Console can have its own set of Defenders. In this case, these Defenders do communicate directly with Central Console. However, no project Defenders ever communicate directly with Central Console.

### Access control[Direct link to heading](https://docs.prismacloud.io/admin-guide/deployment-patterns/projects\#access-control)

When users log into Prisma Cloud Console, they are presented with a list of projects to which they have access, and they can chose the project they want to work in. Access to projects is controlled by role-based access control rules.

You can grant access to specific projects for any 'local' users created in Console under **Manage > Authentication > Users**. If you have integrated Console with an OpenLDAP, Active Directory, or SAML provider, you can grant access to projects by group. Users and groups can be granted access to multiple projects.

A user’s role is applied globally across all projects. That is, a user will have the same role for each project for which he has been granted access.

Project access control rules at the user level takes precedence over access control granted at the group level. For example, if a 'local' user has been granted access to project1, but also belongs to group1, which has been granted access to project2, he will only have permissions to access project1.

### Secrets[Direct link to heading](https://docs.prismacloud.io/admin-guide/deployment-patterns/projects\#secrets)

Prisma Cloud fully supports secrets management for tenant projects. Secrets management can be independently configured and managed for each tenant project.

### Limitations[Direct link to heading](https://docs.prismacloud.io/admin-guide/deployment-patterns/projects\#limitations)

Moving Defenders between projects is not supported. To "move" a Defender, decommission it from one project and deploy it to another.

## Provisioning flow[Direct link to heading](https://docs.prismacloud.io/admin-guide/deployment-patterns/projects\#provisioning-flow)

Let’s look at how projects are provisioned.

**Step 1:** Install Console using any installation method. For example, you could install [Console (onebox) with the _twistlock.sh_ script](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-onebox) or as a [service in a Kubernetes cluster](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-kubernetes). When Console is installed, it runs in master mode by default.

![projects setup flow1](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-d8701521f7b4cf8ac256ab11ee067de9a5f8a5f9%252Fprojects_setup_flow1.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=0bf7a340e8721c4da6099cf89c85f8f8&sv=3)

**Step 2:** Install a second Console on a different host. By default, it also runs in master mode.

![projects setup flow2](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-0d661229b4b8c1fa48f31b2d803fab01a6e66536%252Fprojects_setup_flow2.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=2097230849f2114e360b099f52b785de&sv=3)

**Step 3:** In the UI for Console 1, provision a new project. Specify the URL to Console 2. The provisioning process automatically changes the operating mode for Console 2 to supervisor. The UI and API for Console 2 are now no longer directly accessible.

![projects setup flow3](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-7766f0f9ddb7f36c2f6f05d2937bf02a09e1028d%252Fprojects_setup_flow3.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=84219ddfcb920226dde15dba114339d8&sv=3)

**Step 4:** The only difference between a master Console and a supervisor Console is whether its UI and API can be accessed directly, or whether it is proxied through the master. To view your tenant project (managed by Console 2), open Console 1 and select the project. All your rules and settings for your project are loaded and displayed in Console 1.

![projects setup flow4](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-08ba96d49135ba2707dc3c8e3f02e80f1e5ee78c%252Fprojects_setup_flow4.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=bdc87dad2870883368c596deb4224bfc&sv=3)

You can release a supervisor, and return it to its original state, by deleting the project. The supervisor Console reverts back to master mode.

## Migration strategies[Direct link to heading](https://docs.prismacloud.io/admin-guide/deployment-patterns/projects\#migration-strategies)

If you have already deployed one or more stand-alone Consoles, and you want to adopt a project-based structure, then the migration is easy. Designate one Console as master, then designate each remaining Console as a supervisor by provisioning projects for them.

Adding an existing Console to a project is not a destructive operation. All data is preserved, and the process can be reversed. The only thing that changes is the way you access Console when it’s mode changes to supervisor. Supervisor Consoles cannot be accessed directly. They can only be accessed through the master Console, by selecting a project from the **Selected project** drop-down list.

For example, assume you’ve deployed three separate stand-alone Consoles: one for your production environment, one for your test environment, and one for your development environment.

![projects migrate1](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-a373921bf320be1e912da6611420b3342c36b29d%252Fprojects_migrate1.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=1595a2553eaf68e84246b4db2d7a603f&sv=3)

When migrating to projects, you have the following options:

**Option 1:** Promote one Console to master, and designate the others as supervisors. In this example, you pick the prod Console to be master, then create tenant projects for the test and development Consoles.

By default, Consoles run in master mode when they are installed, so you don’t need to do anything to "promote" prod to master. To relegate test and dev to supervisor, [provision a project](https://docs.prismacloud.io/admin-guide/deployment-patterns/projects#_provisioning_a_project) for each one.

![projects migrate2](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-5679648012e4081f8014070281830ff03f137e21%252Fprojects_migrate2.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=6e05a8457991c17ac433ae41e1f25842&sv=3)

**Option 2:** Install a new Console on a dedicated host and designate it as master. Provision a tenant project for each of the prod, test, and dev Consoles.

![projects migrate3](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-8f80dfb106e0564a78f6d3a7e6067c5d3af7e030%252Fprojects_migrate3.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=e00b2204192dc115526854bac6c15feb&sv=3)

## Accessing the API[Direct link to heading](https://docs.prismacloud.io/admin-guide/deployment-patterns/projects\#accessing-the-api)

All API requests should be routed to Central Console only. Central Console checks if the client has the correct permissions to access the given project, and then Central Console redirects the request to right supervisor, and then returns to supervisor’s response to the client.

For API requests that create, modify, or delete data, Central Console responds to the client with a success return code, and then updates the supervisor asynchronously.

To target an API request to a specific project, append the `project=` query parameter to your request. For example, to get a list of Defenders deployed in the `prod` project:

AskCopy

```
GET http://<CENTRAL-CONSOLE>:8083/api/v1/defenders?project=prod
```

Central Console reroutes the request to the appropriate supervisor. Not all requests need to be rerouted. For example, the endpoints for getting a list of users, groups, or projects are handled by Central Console directly. Some endpoints require no special permissions to access them, such as getting a list projects to which a user has been granted access.

## Provisioning a project[Direct link to heading](https://docs.prismacloud.io/admin-guide/deployment-patterns/projects\#provisioning-a-project)

Provision new projects from the Central Console UI.

Communication between the master and supervisor Consoles must be direct, and cannot be routed through a proxy.

1. Install a Console on a host in your environment using any install procedure.











There is no need to create an admin user or enter your license. Those details will be handled for you in the provisioning phase of this procedure.

2. Register the newly installed Console with the Central Console and create a project.

3. Go to **Manage > Projects > Manage**

4. Set **Use Projects** to **On**.

5. Click **Provision project**.

6. In **Project name**, give your project a name.

7. In **Supervisor address**, enter the URL for accessing Console Include both the protocol (https://) and port.

8. For a fresh Console install, there is no need to enter any credentials. They will be created for you automatically.











If you are migrating an existing Console to a project, specify the admin credentials.


## Decommissioning a project[Direct link to heading](https://docs.prismacloud.io/admin-guide/deployment-patterns/projects\#decommissioning-a-project)

Decommissioning a project simply reverts the supervisor Console back to a stand-alone master Console. The link between Central Console and the former supervisor Console is severed. All project data (rules, audits, scan reports) is left in tact.

When a project is created, the Console is configured with an admin user. When you delete the project, the admin credentials are shown to you so that you can continue to access and administer it. The credentials are shown only one time, so copy them, and set them aside in a safe place.

1. Open Central Console.

2. Go to **Manage > Projects > Manage**.

3. In the **Provisioned Projects** table, click delete on the project you want to delete.


## Decommissioning disconnected projects[Direct link to heading](https://docs.prismacloud.io/admin-guide/deployment-patterns/projects\#decommissioning-disconnected-projects)

Central Console lets you delete projects, even if the supervisor Console is disconnected. The project is deleted from the master’s database, but it leaves the supervisor Console in the wrong state.

When you delete a disconnected project, Prisma Cloud tells you that the supervisor cannot be reached. To manually revert the supervisor Console back to a stand-alone master Console, call the supervisor’s REST API to change its settings.

1. Decide how you want to access the supervisor’s REST API. You can use basic auth or an auth token.

2. Update the supervisor’s project settings. The following example command uses basic auth. Only [admin users](https://docs.prismacloud.io/admin-guide/authentication/user-roles#administrator) are permitted to change project settings.

















AskCopy



```
$ curl -k \
     -u <USER> \
     -X POST \
     -H 'Content-Type:application/json' \
     -d '{"master":false, "redirectURL":""}' \
     https://<SUPERVISOR-CONSOLE>:8083/api/v1/settings/projects
```


## Deploying Defender DaemonSets for projects (Console UI)[Direct link to heading](https://docs.prismacloud.io/admin-guide/deployment-patterns/projects\#deploying-defender-daemonsets-for-projects-console-ui)

When creating a DaemonSet for a project, you can use the Console UI, twistcli, or API. This section shows you how to use the Console UI.

1. In Console, use the drop-down menu at the top right of the UI to select the project where you want to deploy your DaemonSet.

2. Go to **Manage > Defenders > Deploy Daemon Set**.

3. Configure the deployment parameters, then copy and run the resulting install script.


## Deploying Defender DaemonSets for projects (twistcli)[Direct link to heading](https://docs.prismacloud.io/admin-guide/deployment-patterns/projects\#deploying-defender-daemonsets-for-projects-twistcli)

Create a DaemonSet deployment file with twistcli. Specify both the project name and the DNS name or IP address of the supervisor Console to which the DaemonSet Defenders will connect. The DNS name or IP address must be a [Subject Alternative Name](https://docs.prismacloud.io/admin-guide/configure/subject-alternative-names) in the supervisor Console’s certificate.

AskCopy

```
$ <PLATFORM>/twistcli defender export kubernetes \
  --address https://<CENTRAL-CONSOLE>:8083 \
  --project <PROJECT-NAME>
  --user <USER> \
  --cluster-address <SUPERVISOR-CONSOLE-SAN>
```

## Deploying Defender DaemonSets for projects (API)[Direct link to heading](https://docs.prismacloud.io/admin-guide/deployment-patterns/projects\#deploying-defender-daemonsets-for-projects-api)

A DaemonSet deployment file can also be created with the API. Specify both the project name and the DNS name or IP address of the supervisor Console to which the DaemonSet Defenders will connect. The DNS name or IP address must be a [Subject Alternative Name](https://docs.prismacloud.io/admin-guide/configure/subject-alternative-names) in the supervisor Console’s certificate.

AskCopy

```
$ curl -k \
  -u <USER>
  -X GET \
  'https://<CENTRAL-CONSOLE>:8083/api/v1/defenders/daemonset.yaml?consoleaddr=<SUPERVISOR_CONSOLE_SAN>&listener=none&namespace=twistlock&orchestration=kubernetes&privileged=true&serviceaccounts=true&project=<PROJECT_NAME>'
```

[PreviousDeployment patterns](https://docs.prismacloud.io/admin-guide/deployment-patterns/deployment-patterns) [NextMigration options for scale projects](https://docs.prismacloud.io/admin-guide/deployment-patterns/migration-options-for-scale-projects)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
