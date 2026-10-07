For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/configure/collections.md).

Collections are predefined filters for segments of your environment. They are centrally defined, and they are used in rules and views across the product.

Collections are used to:

- Scope rules to target specific resources in your environment.











Example: A vulnerability rule that applies to all container images in an app called sock-shop. The rule might reference a collection, which specifies `sock-shop` in the image resource filter.

- Partition views to provide a convenient way to browse data from related resources.

- Enforce which views that specific users and groups can see by controlling access to data on a need-to-know basis (assigned collections).


## Attributes Used for Pattern Matching[Direct link to heading](https://docs.prismacloud.io/admin-guide/configure/collections\#attributes-used-for-pattern-matching)

Collections are created with [pattern matching](https://docs.prismacloud.io/admin-guide/configure/rule-ordering-pattern-matching) expressions that are evaluated against attributes such as \* Image name \* Container name \* Hostname \* Labels \* Function name \* Namespace \* Registry tag

For labels, Prisma Cloud supports AWS tags and distro attributes.

## Supported Distro Attributes[Direct link to heading](https://docs.prismacloud.io/admin-guide/configure/collections\#supported-distro-attributes)

Distro attributes are designed for central security teams that manage the policies in Console, but have little influence over the operational practices of the groups that run apps in the environments being secured. If the central security team can’t rely on naming conventions or labels to apply policies that are OS-specific (for example, different compliance checks for different operating systems), they can leverage the distro attributes. Supported distro attributes are:

- Distro name. The format is `osDistro:<value>`. Example: `osDistro:Ubuntu`

- Distro version. The format is `osVersion:<value>`. Example: `osVersion:20.04`.


## Partitioning Views[Direct link to heading](https://docs.prismacloud.io/admin-guide/configure/collections\#partitioning-views)

A single Console manages data from Defenders spread across all hosts. Collections allow you to segment data into different views, based on attributes.

### Example Use Case[Direct link to heading](https://docs.prismacloud.io/admin-guide/configure/collections\#example-use-case)

A Kubernetes cluster runs multiple apps:

- **Shopping app** (managed by the product team)

- **Travel app & Expenses app** (managed by an internal tools team)


A developer for the travel app only needs to see vulnerabilities in the travel app images. Collections filter out unnecessary data, reducing noise and improving focus.

## Scoping Rules[Direct link to heading](https://docs.prismacloud.io/admin-guide/configure/collections\#scoping-rules)

The scope of a rule is defined by referencing the relevant collections. Collections offer a centralized way to manage scope settings across Prisma Cloud. Collections ensure consistency across policies as they allow reuse of scope settings. Policy tables give you a clear picture of what resources are being targeted in your rules.

![collections policy table scopes](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-11732506857cf12ef0a3627e5599815d1ff558a4%252Fcollections_policy_table_scopes.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=8d9204a77576f6672cef0e674ec76503&sv=3)

When creating new rules, you can either select from a list of previously defined collections or create a new one. By default, Prisma Cloud sets a rule’s scope to the **All** collection, which captures all resources in the environment.

![collections rule scope](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-b073184f2f2fdf94697ead5ec2ee6dd9e4311da2%252Fcollections_rule_scope.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=0154223eeb7fc18112808e394057622b&sv=3)

Example: You can create collections based on different attributes, such as application names or namespaces. Additionally, collections can be created based on regions. For example, you can define a collection that includes all resources in the us-west-1 region, allowing you to scope policies specifically for resources deployed in that region.

## Importing and exporting rules[Direct link to heading](https://docs.prismacloud.io/admin-guide/configure/collections\#importing-and-exporting-rules)

Rules can be exported from one Console and imported into another Console. When importing rules, any associated collections are also imported and created.

Prisma Cloud allows rules and collections to be imported/exported between Consoles.

## Import Behavior[Direct link to heading](https://docs.prismacloud.io/admin-guide/configure/collections\#import-behavior)

Scenario

Action Taken

Collection does not exist in the new Console

Created automatically

Collection exists but has a different scope

New collection is created with: \* **Name:**`<policyType> - <ruleName> <collectionName>` \\* **Description:**`Automatically generated collection for an imported rule/entity`

Collection exists with a matching scope

Existing collection is used as-is

## Creating Collections[Direct link to heading](https://docs.prismacloud.io/admin-guide/configure/collections\#creating-collections)

You can create as many collections as you like. However, collections **cannot be nested**.

### Built-in Collections[Direct link to heading](https://docs.prismacloud.io/admin-guide/configure/collections\#built-in-collections)

Prisma Cloud ships with a built-in collection called **All**, which: - Is **not editable**. \- Contains **all objects in the Prisma Cloud**. \- Functions as a wildcard (`*`) for all resource types, including containers, images, hosts, labels, and more.

### Where to Create Collections[Direct link to heading](https://docs.prismacloud.io/admin-guide/configure/collections\#where-to-create-collections)

Collections can be created from: - **Manage > Collections and Tags > Collections** \- The **New Rule** dialog when setting a rule’s scope - In this case, Prisma Cloud **disables irrelevant scope fields**. \- If you select a previously defined collection in a rule’s scope field, **improperly scoped collections are hidden** (e.g., a collection specifying serverless functions won’t be shown in a container runtime rule).

### Default Collection Scope[Direct link to heading](https://docs.prismacloud.io/admin-guide/configure/collections\#default-collection-scope)

By default, new collections set a wildcard (`*`) for each resource type, capturing **all resources**. To refine the scope, customize the relevant fields.

### Supported Labels[Direct link to heading](https://docs.prismacloud.io/admin-guide/configure/collections\#supported-labels)

The **Labels** field supports multiple sources, including:

Label Type

Supported Sources

[**Docker labels**](https://docs.docker.com/config/labels-custom-metadata/)

Container metadata

**Azure Registry Tags**

Key-value pairs (`key:value`)

**Kubernetes Labels**

Pod template, namespace, and deployment labels

**AWS Tags**

Tags associated with cloud resources

**Distribution Name for Hosts**

`osDistro:<name>`

**Operating System Version for Hosts**

`osVersion:<version>`

### Using Registry Tags for Access Control[Direct link to heading](https://docs.prismacloud.io/admin-guide/configure/collections\#using-registry-tags-for-access-control)

- Prisma Cloud extracts **registry tags from Azure Registry**.

- These tags can be used to enforce **role-based access control (RBAC)** for vulnerability scan findings.

- All identified Azure registry tags appear under: **Monitor > Vulnerabilities > Images > Registries > Image Details > Labels**


### Enabling Additional Label Support[Direct link to heading](https://docs.prismacloud.io/admin-guide/configure/collections\#enabling-additional-label-support)

To use additional labels, enable the corresponding settings:

Label Type

Configuration Path

**Kubernetes Namespace and Deployment Labels**

Enable under **Manage > Defenders > Deployed Defenders > Manual Deploy > Collect Deployment and Namespace Labels**

**AWS Tags for Hosts**

Enable VM tags in **Manage > Cloud Accounts > Add/Edit Account > Discovery Features**

### Scoping App-Embedded Policy Rules[Direct link to heading](https://docs.prismacloud.io/admin-guide/configure/collections\#scoping-app-embedded-policy-rules)

To scope App-Embedded **vulnerability, compliance, and runtime rules**, use the collection’s **App ID field**.

For **Fargate tasks** protected by App-Embedded Defenders, rules can additionally be scoped by **image**.

### Collection Scope Limitations[Direct link to heading](https://docs.prismacloud.io/admin-guide/configure/collections\#collection-scope-limitations)

Certain resource combinations are **not allowed in a single collection**:

Combination

Restriction

**Host + Cluster**

Must separate into distinct collections.

**Container + Image**

One field must use a wildcard (`*`), or the collection won’t apply correctly.

**Example:** To apply collections to both a container and an image, create **two separate collections**: \- One collection should include **only the container name**. \- The other collection should include **only the image name**. \- **Filtering on both collections simultaneously won’t yield the desired result**.

### Unsupported Filtering[Direct link to heading](https://docs.prismacloud.io/admin-guide/configure/collections\#unsupported-filtering)

- Filtering by **cloud account ID** for **Azure Container Instances** is **not supported**.


### Steps to Create a Collection[Direct link to heading](https://docs.prismacloud.io/admin-guide/configure/collections\#steps-to-create-a-collection)

To create a collection, follow these steps:

1. Open Console









1. Navigate to **Manage > Collections and Tags > Collections**.


2. Add a New Collection









1. Click **Add Collection**.


3. Enter Collection Details









1. **Name:** Provide a unique name for the collection.

2. **Description:** (Optional) Enter a description to define its purpose.

3. **Color:** Choose a color to visually distinguish this collection.


4. Choose Resources to include. Select one or more of the following resources:









   - **Containers** – Running container instances in your environment.

   - **Hosts** – Physical or virtual machines where containers run.

   - **Images** – Container images stored in registries.











     Other than the image name, the system also checks the text you type against the operating system, ID, the hostname, and the cluster name. Successful matches on any of these properties will result in the corresponding image being displayed.

   - **Labels** – Key-value metadata attached to resources.

   - **App IDs (App-embedded)** – Application identifiers for embedded security enforcement.

   - **Functions** – Serverless functions such as AWS Lambda or Google Cloud Functions.

   - **Namespaces** – Isolated environments in Kubernetes.


For more information on syntax that can be used in the filter fields (for example, containers, images, and hosts), see [Rule ordering and pattern matching](https://docs.prismacloud.io/admin-guide/configure/rule-ordering-pattern-matching).

5. Define Filters. Use pattern-matching syntax to refine the scope.











**Example:** To select all images that start with "raspberry", use the filter **raspberry**

6. Save the Collection









1. Click **Save** to apply your settings.











      You can view a summary of each Collection in the sidecar, which shows the resources' data and usage of the Collection


![collection sidecar view](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-362b246309db8b3e30388d55d762af744b94a1af%252Fcollection-sidecar-view.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=b7f63947f2467cbd318b7bf28ce6ec7d&sv=3)

The new collection will now be available for use in rules and views.

## Selecting a collection[Direct link to heading](https://docs.prismacloud.io/admin-guide/configure/collections\#selecting-a-collection)

Collections filter data in the **Monitor** section of the Console.

When a collection (or multiple collections) is selected, only the objects that match the filter are shown in those views. When a collection is selected, it remains selected for all views until it is explicitly disabled.

To select a collection, go to any view under **Monitor**. In the Collections drop-down list in the top right of the view, select a collection. In the following screenshot, the view is filtered based on the collection named **google images**, which shows all images that contain the string **google\_containers**.

![collections 792004](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-c851c6f925464cb579950eeceb6d96ca150d6ac6%252Fcollections_792004.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=fdb13cc69e01a88540c871942fc59a3c&sv=3)

When multiple collections are selected, the effective scope is the union of each individual query.

Individual filters on each collection aren’t applicable to all views. For example, a collection created with only functions won’t include any resources when viewing the hosts results. Similarly, a collection created with hosts won’t filter images by hosts when viewing image results.

The **Collections** column shows to which collection a resource belongs. The color assigned to a collection distinguishes objects that belong to specific collections. This is useful when multiple collections are displayed simultaneously. Collections can also be assigned arbitrary text tags to make it easier for users to associate other metadata with a collection.

## Use Collections with TAS Metadata Fields[Direct link to heading](https://docs.prismacloud.io/admin-guide/configure/collections\#use-collections-with-tas-metadata-fields)

Prisma Cloud automatically collects metadata fields such as Foundation, Organization Name, Application Name and ID, and Space Name and ID. To utilize these fields, you’ll have to **manually create** appropriate collections that can then be used for filtering and aggregation.

Resource type

Supported Labels

Host

tas-foundation

Containers (running applications)

tas-application-id, tas-application-name, tas-space-id, tas-space-name, tas-org-id, tas-org-name, tas-foundation

Droplets

tas-application-id, tas-application-name, tas-space-id, tas-space-name, tas-org-id, tas-org-name, tas-foundation

- To use the **tas-fundation** label, enter a **Foundation** name in the Prisma Cloud TAS tile configuration screen at the time of [deploying a TAS Defender](https://docs.prismacloud.io/admin-guide/install/deploy-defender/orchestrator/install-tas-defender).


## Limitations[Direct link to heading](https://docs.prismacloud.io/admin-guide/configure/collections\#limitations)

Different views in Console are filtered by different resource types.

If a collection specifies resources that are unrelated to the view, filtering by this collection returns an empty result.

Section

View

Supported resources in collection

Monitor/Vulnerabilities

Monitor/Compliance

Images

Images, Hosts, App IDs (App-Embedded), Namespaces, Clusters, Labels, Cloud Account IDs

Monitor/Vulnerabilities

Monitor/Compliance

Registry images

Images, Hosts (of the scanner host), Labels, Cloud Account IDs

Monitor/Vulnerabilities

Monitor/Compliance

Containers

Images, Containers, Hosts, Namespaces, Clusters, Labels, Cloud Account IDs

Monitor/Vulnerabilities

Monitor/Compliance

Hosts

Hosts, Clusters, Cloud Account IDs

**Note**: As Kubernetes nodes and namespaces are not scanned, the Monitor/Vulnerabilities Hosts view cannot filter hosts using K8s node and namespace labels. However, you can filter hosts using K8s pod label.

Monitor/Vulnerabilities

Monitor/Compliance

VM images

VM images (under Images), Cloud Account IDs

Monitor/Vulnerabilities

Monitor/Compliance

Functions

Functions, Cloud Account IDs, Labels (Region, AWS tag)

Monitor/Vulnerabilities

Code repositories

Code repositories

Monitor/Vulnerabilities

VMware Tanzu blobstore

Hosts (of the scanner host), Cloud Account IDs, Labels (tas-application-id, tas-application-name, tas-space-id, tas-space-name, tas-org-id, tas-org-name, tas-foundation)

Monitor/Vulnerabilities

Vulnerability Explorer

Images, Hosts, Clusters, Labels, Functions, Cloud Account IDs

Monitor/Compliance

Cloud Discovery

Cloud Account IDs

Monitor/Compliance

Compliance Explorer

Images, Hosts, Namespaces, Clusters, Labels, Cloud Account IDs

Monitor/Events

Container audits

Images, Containers, Namespaces, Clusters, Container Deployment Labels (under Labels), Cloud Account IDs. (Cluster collections are not currently able to filter some events such as container audits, specifically.)

Monitor/Events

WAAS for Containers

Images, Namespaces, Cloud Account IDs

Monitor/Events

Trust Audits

Images, Clusters, Cloud Account IDs

Monitor/Events

Admission Audits

Namespaces, Clusters, Cloud Account IDs

Monitor/Events

Docker Audits

Images, Containers, Hosts, Clusters, Cloud Account IDs

Monitor/Events

App-Embedded audits

App IDs (App-Embedded), Cloud Account IDs, Clusters, Images

Monitor/Events

WAAS for App-Embedded

App IDs (App Embedded), Cloud Account IDs

Monitor/Events

Host audits

Hosts, Clusters, Labels, Cloud Account IDs

Monitor/Events

WAAS for Hosts

Hosts, Cloud Account IDs

Monitor/Events

Host Log Inspection

Hosts, Clusters, Cloud Account IDs

Monitor/Events

Host File Integrity

Hosts, Clusters, Cloud Account IDs

Monitor/Events

Host Activities

Hosts, Clusters, Cloud Account IDs

Monitor/Events

Serverless audits

Functions, Cloud Account IDs, Labels (Region, Provider)

Monitor/Events

WAAS for Serverless

Functions, Cloud Account IDs, Labels (Region)

Monitor/Runtime

Container incidents

Images, Containers, Hosts, Namespaces, Clusters, Cloud Account IDs

Monitor/Runtime

Host incidents

Hosts, Clusters, Cloud Account IDs

Monitor/Runtime

Serverless incidents

Functions, Cloud Account IDs, Labels (Region)

Monitor/Runtime

App Embedded incidents

App IDs (App Embedded), Cloud Account IDs

Monitor/Runtime

Container models

Images, Namespaces, Clusters, Cloud Account IDs

Monitor/Runtime

App-Embedded observations

App IDs, Images, Containers, Clusters, Account IDs, Regions (under Labels)

Monitor/Runtime

Host observations

Hosts, Clusters, AWS tags (under Labels), OS tags (under Labels), Cloud Account IDs

Monitor/Runtime

Image analysis sandbox

Images, Labels

Radar

Containers Radar

Images, Containers, Hosts, Namespaces, Clusters, Labels, Cloud Account IDs

Radar

Hosts Radar

Hosts, Clusters, AWS tags (under Labels), OS tags (under Labels), Cloud Account IDs

Radar

Serverless Radar

Functions, Cloud Account IDs, Labels (Region, AWS tag)

Manage

Defenders

Hosts, Clusters, Cloud Account IDs

### Using Collections[Direct link to heading](https://docs.prismacloud.io/admin-guide/configure/collections\#using-collections)

After collections are created or updated, the following views require a rescan before reflecting changes:

- Deployed Images vulnerabilities and compliance views

- Registry Images vulnerabilities and compliance views

- Code repositories vulnerabilities view

- Trusted images

- Cloud Discovery

- Vulnerability Explorer

- Compliance Explorer


After collections are created or updated, some views are affected by the change only for future records. The following views retain their collections right from the time the records are created:

- Images and Functions CI results view

- Events views

- Incidents view

- Image analysis sandbox results view


[PreviousCustomize terminal output](https://docs.prismacloud.io/admin-guide/configure/customize-terminal-output) [NextTags](https://docs.prismacloud.io/admin-guide/configure/tags)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
