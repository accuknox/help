> For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.prismacloud.io/content-collections/runtime-security/runtime-defense/runtime-defense-containers.md).

# Runtime Defense for Containers

Runtime defense is the set of features that provide both predictive and threat-based active protection for running containers. For example, predictive protection includes capabilities like determining when a container runs a process not included in the original image or creates an unexpected network socket. Threat-based protection includes capabilities like detecting when malware is added to a container or when a container connects to a botnet.

Prisma Cloud Compute has distinct sensors for the filesystem, network, and process activity. Each sensor is implemented individually, with its own set of rules and alerts. The runtime defense architecture is unified to both simplify the administrator experience and to show more detail about what Prisma Cloud automatically learns from each image. Runtime defense has two principal object types: models and rules.

## Container Models

Models are the results of the autonomous learning that Prisma Cloud performs every time we see a new image in an environment. A model is the "allow list" for what a given container image should be doing, across all runtime sensors. Models are automatically created and maintained by Prisma Cloud and provide an easy way for administrators to view and understand what Prisma Cloud has learned about their images. For example, a model for an Apache image would detail the specific processes that should run within containers derived from the image and what network sockets should be exposed.

Navigate to **Monitor > Runtime > Container Models**. Click on the image to view the model.

There is a 1:1 relationship between models and images; every image has a model and every model applies to a single unique image. For each image, a unique model is created and mapped to the image digest. So, even if there are multiple images with the same tags, Prisma Cloud will create unique models for each image.

Models are built from both static analysis (such as building a hashed process map based on parsing an init script in a Dockerfile ENTRYPOINT) and dynamic behavioral analysis (such as observing actual process activity during early runtime of the container). Models can be in one of 3 modes: Active, Archived, or Learning.

<figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-eae078a2e8d7b4f0d796b2368ec58f7a136c0f7e%2Fruntime-defense-734302.png?alt=media" alt="runtime defense 734302"><figcaption></figcaption></figure>

For containers in Kubernetes clusters, Prisma Cloud considers the image, namespace, and cluster when creating models.

* When the same image runs in multiple different clusters, Prisma Cloud creates separate models for each image in each cluster.
* When the same image runs in multiple different namespaces, Prisma Cloud creates separate models for each image in each namespace.
* When there are multiple running instances of an image in the same namespace, Prisma Cloud creates a single model.
* When clusters are not applicable, Prisma cloud considers the image and namespace to create models.

Prisma Cloud shows you how models map to specific images. Go to **Monitor > Runtime > Container Models**, click a model in the table, and click the **General** tab.

<figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-90b7150804ab66bc9c790134e6a4e38b0140196a%2Fruntime-defense-overview-model.png?alt=media" alt="runtime defense overview model"><figcaption></figcaption></figure>

## Capabilities

Some containers are difficult to model. For example, Jenkins containers dynamically build and run numerous processes, and the profile of those processes changes depending on what’s being built. Constructing accurate models to monitor processes in containers that build, run, test, and deploy software is impractical, although other aspects of the model can still have utility. Prisma Cloud automatically detects known containers and overrides one more aspect of the model with *capabilities*.

Capabilities are discrete enhancements to the model that tune runtime behaviors for specific apps and configurations. Rather than changing what’s learned in the model, they modify how Prisma Cloud acts on observed behaviors.

For example, the following model for the Jenkins container is enhanced with the capability for writing and executing binaries.

<figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-e4724b81e590b139f9b646eb57c9815b311b35b7%2Fruntime-defense-overview-container-model-capabilities.png?alt=media" alt="runtime defense overview container model capabilities"><figcaption></figcaption></figure>

## Learning mode

Learning mode is the phase in which Prisma Cloud performs either static or dynamic analysis. Because the model depends on behavioral inputs, images stay in learning mode for 1 hour to complete the model. After this 1 hour, Prisma Cloud enters a 'dry run' period for 24 hours to ensure there are no behavioral changes and the model is complete. If during these 24 hours, behavioral changes are observed, the model goes back to Learning mode for an additional 24 hours. The behavioral model uses a combination of machine learning techniques and typically requires less than 1 hour of cumulative observation time for a given image (it might comprise of a single container running the entire learning period or multiple containers running for some time slice where the sum of the slices is 1 hour). During this period, only threat-based runtime events (malicious files or connections to high-risk IPs) are logged. Prisma Cloud automatically detects when new images are added anywhere in the environment and automatically puts them in learning mode.

<figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-fa8517e60c8cdcabc863650a206007842ee319fc%2Fruntime-defense-792723.png?alt=media" alt="runtime defense 792723"><figcaption></figcaption></figure>

* Extend Learning: You can relearn an existing model by clicking the **Extend Learning** button in the **Actions** menu. This is an additive process, so any existing static and behavioral modeling remain in place.
* Manual Learning: You can manually alter the duration of learning at any time by starting and stopping the **Manual Learning** option in the **Actions** menu. This should be done with discretion because the model may or may not complete within the time-period due to manual interruption. There is no time limit for manual learning. It depends on the user’s selection.

## Active mode

Active mode is the phase in which Prisma Cloud is actively enforcing the model and looking for anomalies that violate it. Active mode begins after the initial 1 hour that the learning mode takes to create a model. Because models are explicit allow lists, in enforcing mode, Prisma Cloud is simply looking for variances against the model. For example, if a model predicted that a given image should only run the foo process and Prisma Cloud observes the bar process has spawned, it would be an anomaly. Prisma Cloud automatically transitions models from learning mode into enforcing mode after the model is complete. During this period, runtime events are logged.

During the initial dry run period (the first 24 hours), model may switch automatically from Active mode to learning mode depending on the behavioral changes observed, as mentioned above. This automatic switching only happens during the first 24 hours of model initiation. If violations are observed later on, they are logged as runtime alerts under Monitor > Runtime.

## Archived mode

Archived mode is a phase that models are transitioned into when a container is no longer actively running them. Models persist in an archived mode for 24 hours after being archived, after which point they’re automatically removed. Archived mode serves as a 'recycle bin' for models, ensuring that a given image does not need to go through learning mode again if it frequently starts and stops, while also ensuring that the list of models does not continuously grow over time.

Models display all the learned data across each of the runtime sensors to make it easy to understand exactly what Prisma Cloud has learned about an image and how it will protect it. However, what if you need to customize the protection for a given image, set of images, or containers? That’s the job of rules.

## Rules

Rules control how Prisma Cloud uses autonomously generated models to protect the environment. For example, if Prisma Cloud’s model for the Apache image includes the process httpd, but you know that process bar will eventually run, and you want to ensure that process foo never runs, you can create a rule that applies to all images named httpd, add bar to the allowed process list, and add foo to the blocked process list.

The following screenshot shows how the scope of the rule is set with [collections](/content-collections/runtime-security/configure/collections.md):

<figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-92e026c482c51deb373785dfda2a5e2af8f46b39%2Fruntime-defense-rule-scope.png?alt=media" alt="runtime defense rule scope"><figcaption></figcaption></figure>

The Container runtime policy rules allow individual effects per protection, such as. anti-malware, crypto miners, reverse shell attacks, etc. for each section - Processes, Networking, File System, and Anti-malware. The effect includes the following options: Disabled/Alert/Prevent/Block according to the supported effects for each detection.

<figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-c1e3fbf7549471baa82efe552b5e5ad1616ce4a3%2FcontainerRuntimeRule-Processes.png?alt=media" alt="containerRuntimeRule Processes"><figcaption></figcaption></figure>

Rules let you explicitly allow/alert/prevent/block activity by a sensor. Rules and models are evaluated together to create a resultant policy as follows:

**model** (which contains only allowed activity) + **allowed activity from rule(s)** - **blocked activity from rule(s)** = **resultant policy**

The resultant policy from the previous example:

model (**httpd**) + allowed activity from rule (**process bar**) - blocked activity from rule (**process foo**) = httpd and bar are allowed and foo always is an anomaly regardless of the model

By default, Prisma Cloud ships with an empty container runtime policy. An empty policy disables runtime defense entirely. To enable runtime defense, create a rule. New runtime rules can be created in Console in **Defend > Runtime > Container policy**.

As with every other subsystem in Prisma Cloud, you can customize how it works by creating rules, scoping rules to desired objects with filtering and pattern matching, and [properly ordering the rules](/content-collections/runtime-security/configure/rule-ordering-pattern-matching.md) in the policy. Rules are evaluated sequentially from top to bottom. Once a match is found for the scope, the actions in the rule are executed and enforced. Only a single rule is ever enforced for a given event. While rules work in conjunction with models as described above, rules themselves are never combined.

Refine your policy by creating rules that target specific resources, enabling or disabling protection features, and defining exceptions to the automatically generated allow-list models.

### Discrete blocking

Prisma Cloud lets you create runtime rules that block discrete processes inside a container using the **Prevent** effect. It is an alternative to stopping an entire container when a violation of a runtime rule is detected.

### Blocked containers

Prisma Cloud’s runtime defense system compares the state of a running container to the predictive model created for it during its [learning period](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/enterprise-edition/content-collections/runtime-security/runtime-defense/runtime-defense.md#learning-mode). When abnormal activity is detected, such as executing an unknown process, Prisma Cloud can:

* Raise an alert by generating an audit. Audits are shown under **Monitor > Events > Container Audits**. If you have an alert channel configured, such as email or Slack, audits are forwarded there too. Alert is the default action for new runtime rules.
* Block the container by stopping it altogether. To enable blocking, create a new runtime rule.
* Prevent just the discrete process or file system write (not the entire container).

#### Blocking action

Blocking stops potentially compromised containers from running in your environment.

Prisma Cloud blocks containers under the following conditions:

* A container violates its runtime model, and you’ve installed a runtime rule with the action set to block. For example, if an attacker infiltrates a container and tries to run a port scan using nc, then the container would be blocked if nc weren’t a known, allowed process.
* A newly started container violates a vulnerability or compliance rule, and those rules have the action set to block. Prisma Cloud scans all images before they run, to enforce policies about what’s allowed to execute in your environment. For example, your policy might call for blocking any container with critical severity vulnerabilities.

Runtime rules can be created under Defend > Runtime > Container Policy. Vulnerability rules can be created under Defend > Vulnerabilities > Policy, and compliance rules can be created under Defend > Compliance > Policy.

#### Viewing blocked containers

Blocking immediately stops a container, taking it out of service. Blocked containers are never restarted. To see a list of blocked containers, go to the container audits page under **Monitor > Events > Container Audits**.

<figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-68ce8d225a227050dc66582634c99c7621db19c4%2Fblock-containers-audits.png?alt=media" alt="block containers audits"><figcaption></figcaption></figure>

When a container is stopped, Prisma Cloud takes no further action to keep it stopped. Orchestrators, such as Kubernetes and OpenShift, start a fresh container in the blocked container’s place. Orchestrators have their own mechanism for maintaining a set point, so they ignore the restart policy defined in the image’s Dockerfile.

There is an exception when you run containers in a Docker-only environment (no orchestrator) and Prisma Cloud blocks a container. In this case, Prisma Cloud must take additional action to keep the container blocked. To prevent the container from automatically restarting, Prisma Cloud modifies the container’s restart policy to always unless stopped. If you want to unblock a container, connect to the node with the blocked container, and manually modify the container’s Docker configuration.

#### Blocked container artifacts

Forensic investigators can inspect a blocked container’s artifacts to determine why it was stopped. You can capture all the container’s contents, including its file system data, with the docker export command. Go to the node with the blocked container and run:

```
$ docker export [container_id] > /path/filename.tar
```

### VMware Tanzu Application Service (TAS)

Runtime rules for VMware TAS apps are scoped by app name and space ID. Specify values for app name and space ID in the **Labels** field of the relevant collection. This field is auto-populated with values from your environment.

```
tas-application-name:<value>
tas-space-id:<value>
```

## Best practices

One key goal is minimizing the amount of work you’re required to do to manage runtime defense. Leverage the models that Prisma Cloud can automatically create and manage. Because behavioral learning for model creation is a mature technology for Prisma Cloud, in most cases, you won’t need to create auxiliary rules to augment model behavior. There will be some exceptions. For example, a long-running container that changes its behavior throughout its lifecycle might need some manually created rules to fully capture all valid behaviors. This is atypical for most environments, however, as containers that need to be upgraded are typically destroyed and reprovisioned with new images.

If you do need to create runtime rules, here are some best practices for doing so:

**Minimize the number of rules** — Creating static rules requires time and effort to build and maintain; only create rules where necessary and allow the autonomous models to provide most of the protection.

**Precisely target rules** — Be cautious of creating rules that apply to broad sets of images or containers. Providing wide-ranging runtime exceptions can lower your overall security by making rules too permissive. Instead, target only the specific containers and images necessary.

**Name rules consistently** — Because rule names are used in audit events, choose consistent, descriptive names for any rules you create. This simplifies incident response and investigation. Also, consider using Prisma Cloud’s alert profile feature to alert specific teams to specific types of events that are detected.

## Container runtime policy

### Anti-malware

Anti-malware provides high-level control for anti-malware capabilities for containers. More granular configuration for each runtime capability is available through each of the other tabs on the rule.

* **Prisma Cloud advanced threat protection** — Use Prisma Cloud advanced threat protection intelligence feed, to apply malware prevention techniques across processes, networking, and filesystem.
* **Kubernetes attacks** — Monitors attempts to directly access Kubernetes infrastructure from within a running container, including both usage of the Kubernetes administrative tools and attempts to access the Kubernetes metadata.

**Prevent** has no effect on the Kubernetes attacks originating from a network activity because prevent effect is not supported for network activities.

* **Suspicious queries to cloud provider APIs** — Monitors access to cloud provider metadata API from within a running container.

### Advanced malware analysis

* **Use WildFire malware analysis** — Use WildFire, Palo Alto Networks' malware analysis engine, to detect malware. Currently Wildfire analysis is provided without additional costs, but this may change in future releases. To use Wildfire, it must first be enabled.

### Processes

This section discusses runtime protection for processes.

#### Effect

When behavior is detected that deviates from your runtime policy (resultant from the combination of your container model and your rules), Prisma Cloud Defender takes action. For processes, the Defender can be set into one of four modes.

* **Disable** — Defender doesn’t provide any protection for processes.
* **Alert** — Defender raises alerts when it detects process activity that deviates from your defined runtime policy. These alerts are visible in **Monitor > Events > Container Audits**.
* **Prevent** — Defender stops the process (and just the process) that violates your policy from executing. This is known as discrete blocking.

  Prisma Cloud runtime rules let you deny specific processes. When you specify the **Prevent** action in a runtime rule, Prisma Cloud blocks containers from running processes that are not defined in the model or the explicitly allowed processes list. The rest of the container continues to execute without disruption. The alternative to discrete blocking is container blocking, which stops the entire container when a denied process is detected.

  The **Prevent** action is not supported on Debian 8.
* **Block** — Defender stops the entire container if a process that violates your policy attempts to run.

Note that besides taking action on processes outside the allow-list model, Defender also takes action when existing binaries that have been modified are executed. For example, an attacker might replace httpd (Apache) with an older version that can be exploited. Prisma Cloud raises alerts for each of the following cases:

* A modified binary is executed,
* A modified binary listens on a port,
* A modified binary makes an outbound connection.

### Allowed activities

* **Learned models**: As part of the model, Prisma Cloud learns what processes are invoked, and the parent processes that triggered the invocation.
* Enable **Allow learned processes only from parents identified in the model** to validate if the process itself is in the model, and also that the process was started by the same parent that is present in the model.
* **Processes list** - Enter a list of allowed processes.
* **Allow all activity in attached sessions** — Bypass runtime rules when attaching to running containers or pods. This control lets developers and DevOps engineers troubleshoot and investigate issues in containers and pods without generating spurious audits or being stymied by block/prevent controls. It applies to all types of attach sessions, including `kubectl exec` and `docker exec`. Only Linux containers are supported; Windows containers aren’t supported.

  This feature is not applicable for Tanzu Application Service Defender (Windows and Linux).

  Note that this control bypasses all runtime activity - process, network, and file system - even though it’s situated in the process tab.

  The following event types can’t be bypassed by this control: DNS queries, listening ports, and raw sockets. For these types of events, activity in the attached session won’t be allowed if set in your policy.

#### Detections

Prisma Cloud can detect anomalous process activity. You can independently set different effects for each feature.

* **Processes started from modified binaries** — Detect when binaries from a container image have been modified and executed.
* **Crypto miners** — Prisma Cloud can detect crypto miners. If detected, a [crypto miner incident type](/content-collections/runtime-security/runtime-defense/incident-types/crypto-miners.md) is created in Incident Explorer. When this option is enabled, Defender takes action on this type of incident according to the configured [effect](#effect).
* **Reverse shell attacks** — Detect usage of [reverse shell](/content-collections/runtime-security/runtime-defense/incident-types/reverse-shell.md).
* **Detect processes used for lateral movement** — Prisma Cloud can detect processes, such as netcat, known to facilitate lateral movement between resources on a network. If detected, a [lateral movement incident type](/content-collections/runtime-security/runtime-defense/incident-types/lateral-movement.md) is created in Incident Explorer. When this option is enabled, Defender takes action on this type of incident according to the configured [effect](#effect).
* **Processes started with SUID** — Detect suspicious privilege escalation by watching for binaries with the setuid bit.

  Explicitly allowed processes from your runtime policy and learned processes from your runtime models bypass this control. For example, if `ping` is added to the container’s runtime model during the learning period, `ping` is permitted to run regardless of how this control is set. However, if `ls` is explicitly permitted by your policy, but `sudo ls` is detected, this control flags the privilege escalation. If you explicitly allow `sudo`, and then run `sudo ls`, this control is bypassed.
* **Explicitly denied processes** - Enter a denied **Processes list** to tailor your runtime model, and choose the **Processes effect**. Processes can be listed by a process name.

#### Runtime container models

Container models are the product of an autonomous learning process initiated when Prisma Cloud detects new containers in your environment. A model is an ‘allow list’ of known good activity for a container, built and maintained on a per-image basis. You can see the domains in the model by going to **Monitor > Runtime > Container Models**, clicking on a model, then opening the **Process** tab.

* **Static container models** — processes that were scanned in the first scan during the container loading.
* **Behavioral container models** — processes that were scanned in the learning period that are not static.
* **Extended behavioral container models** — processes detected after the learning period, where Prisma Cloud identifies them as "low severity". These types of processes will also be added to the model. An alert is raised only once with a message saying there is a low likelihood that this process is malicious and no further alerts for this type of event will be raised. Extended behavioral processes are added to the extended behavioral table in **Monitor > Runtime > Container Models** in the process tab in the extended behavioral section.

### Networking

Prisma Cloud can monitor container networking activity for patterns that indicate an attack might be underway. These features can be independently set to different effects. The final policy that’s enforced is the sum of the container model and your runtime rules.

<figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-828a918b36cda21b1ad25691fc9fac87cb7feba8%2FcontainerRuntimeRule-Networking.png?alt=media" alt="containerRuntimeRule Networking"><figcaption></figcaption></figure>

#### IP connectivity

When Prisma Cloud detects an outgoing connection that deviates from your runtime policy, Prisma Cloud Defender can take action. Networking rules let you put Defender into one of three modes:

* **Disable** — The defender does not provide any networking protection.
* **Alert** — Defender raises alerts when targeted resources establish connections that violate your runtime policy. The corresponding audits can be reviewed under **Monitor > Events > Container Audits**.
* **Block** — The defender stops the container if it establishes a connection that violates your runtime policy. The corresponding audit can be reviewed under **Monitor > Events > Container Audits**.

The fields for **Explicitly allowed** and **Explicitly denied** let you tailor the runtime models for known good and known bad network connections. These rules define the policy for listening ports, outbound internet ports for Internet destinations, and outbound IP addresses. Defining network policy through runtime rules lets you specify permitted and forbidden behavior for given resources, and instruct the defender on how to handle the traffic that deviates from the resultant policy.

* **Port scanning** — Port scans are used by attackers to find which ports on a network are open and listening. If enabled, Defenders detect network behavior indicative of port scanning. The events generated from **Port scanning** can have alert or block effects. If detected, a [port scanning incident](/content-collections/runtime-security/runtime-defense/incident-types/port-scanning.md) is created in Incident Explorer.
* **Raw sockets** — Prisma Cloud can monitor your environment for raw sockets, which can indicate suspicious activity. Raw sockets let programs manipulate packet headers and implement custom protocols to do things such as port scanning. Raw socket detection is enabled by default in new rules.

#### DNS

Modern attacks, particularly coordinated, long-running attacks, use short-lived DNS names to route traffic from the victim’s environment to command and control systems. This is common in large-scale botnets. When DNS monitoring is enabled (Alert, Prevent, or Block) in your runtime rules, Prisma Cloud analyzes DNS lookups from your running containers. By default, DNS monitoring is disabled in new rules.

Dangerous domains are detected as follows:

* **Prisma Cloud Intelligence Stream** — Prisma Cloud’s threat feed contains a list of known bad domains.
* **Behavioral container models** — When learning a model for a container, Prisma Cloud records any DNS resolutions that a container makes. When the model is activated, Defender monitors network traffic for DNS resolutions that deviate from the learned DNS resolutions.

  You can see the domains in the model by going to **Monitor > Runtime > Container Models**, clicking on a model, then opening the **Networking** tab. Known good domains are listed under **Behaviorally learned domains**.
* **Extended behavioral container models** — network traffic detected after the learning period, which Prisma Cloud identifies as "low severity". This traffic will also be added to the model. An alert is raised only once with a message saying there is a low likelihood that this event is malicious and no further alert for this type of event will be raised.
* **Explicit allow and deny lists:** Runtime rules let you augment the Prisma Cloud’s Intelligence Stream data and models with your own explicit lists of known good and bad domains. Define these lists in your runtime rules.

In your runtime rules, set **Effect** in the DNS section to configure how Defender handles DNS lookups from containers:

* **Disable:** DNS monitoring is disabled. DNS lookups are not modeled in learning mode. DNS lookups aren’t analyzed when models are active.
* **Alert:** DNS monitoring is enabled. DNS lookups are modeled in learning mode. DNS lookups are analyzed when models are active. Anomalous activity generates audits.
* **Prevent:** DNS monitoring is enabled. DNS lookups are modeled in learning mode. DNS lookups are analyzed when models are active. Anomalous activity generates audits. Anomalous DNS lookups are dropped.
* **Block** DNS monitoring is enabled. DNS lookups are modeled in learning mode. DNS lookups are analyzed when models are active. Anomalous activity generates audits. When anomalous DNS lookups are detected, the entire container is stopped.

### File system

Prisma Cloud’s runtime defense for container file systems continuously monitors and protects containers from suspicious file system activities and malware.

Prisma Cloud monitors and protects against the following types of suspicious file system activity:

* Changes to any file in folders *not* in the [runtime model](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/enterprise-edition/content-collections/runtime-security/runtime-defense/runtime-defense.md#models).
* Changes to binaries or certificates anywhere in the container.
* Changes to SSH administrative account configuration files anywhere in the container.
* Presence of malware anywhere in the container.

File location change activity does not generate a runtime audit event.

#### Malware protection

Defender monitors container file systems for malicious certs and binaries using data from the Prisma Cloud Intelligence Stream. Console receives the Prisma Cloud feed, and then distributes it to all deployed Defenders. You can optionally supplement the Prisma Cloud feed with your own custom data.

When a file is written to the container file system, Defender compares the MD5 hash of the file to the MD5 hash of known malware. If there is a match, Defender takes the action specified in your rules. Defender also looks for attributes that make files suspicious, including signs they’ve been rigged for anti-analysis.

By default, new rules configure Defender to monitor both the container root file system and any data volumes. Container root file systems reside on the host file system. In this diagram, the running container also has a data volume. It mounts the db/ directory from the host file system into its own root file system. Both locations are monitored by Defender.

The following diagram shows how Prisma Cloud protects containers from malicious files:

<figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-6e5fe726063e68f41deb0a13b46b1f1f03da74e0%2Fruntime-defense-fs-584208.png?alt=media" alt="runtime defense fs 584208"><figcaption></figcaption></figure>

#### Effect

When behavior is detected that deviates from your runtime policy (resultant from the combination of your container model and your rules), Prisma Cloud Defender takes action. For processes, the Defender can be set into one of four modes.

* **Disable** — Defender doesn’t provide any protection for file system.
* **Alert** — Defender raises alerts when it detects file system activity that deviates from your defined runtime policy. These alerts are visible in **Monitor > Events > Container Audits**.
* **Prevent** — Defender stops the process (and just the process) that violates your policy from executing. This is known as discrete blocking. Prisma Cloud also lets you deny file system writes to specific directories. Like the process rule, file system rules can be configured with the **Prevent** action, which blocks the creation and modification of any files in the specified directories. This mechanism is designed to prevent bad actors from writing certificates or binary attack tools to disk, all without killing the process that initiated the write or stopping the entire container.

  The Prevent action for detection of file system events requires a Linux kernel version 4.20 or later. If you specify a **Prevent** action, but the kernel does not support it, you will be alerted with an audit but the activity will not be prevented. The audit message will state that Prevent is not supported.

  The **Prevent** action in file system rules is not supported when the Docker storage driver is set to aufs. It is supported for other storage drivers, such as devicemapper and overlay2. If you specify a **Prevent** action, but the storage driver does not support it, Prisma Cloud will respond with an alert and log the following message in Defender’s log: *Docker storage driver on host doesn’t support discrete file blocking*.

  For the "Changes to binaries", "Detection of encrypted/packed binaries", and "Binaries with suspicious ELF headers" detections, the **Prevent** effect is only supported for existing files that are being modified. This is because these detections rely on the file content. When the file is new, it is empty, so it cannot be identified by one of these detections. In such cases, you are alerted with an audit but the activity is not prevented. The audit message will state that 'prevent' is not supported.
* **Block** — Defender stops the entire container if a process that violates your policy attempts to run.

#### Detections

Prisma Cloud can detect anomalous file system activity. These features can be independently enabled or disabled.

* **Changes to binaries** — Detect when binaries from a container image are modified.
* **Detection of encrypted/packed binaries** — Detect usage of encrypted/packed binaries. Such files are alerted on as encrypted and packed binaries may be used as a method to deploy malware undetected.
* **Changes to SSH and admin account configuration files**
* **Binaries with suspicious ELF headers**
* **Explicitly allowed and denied system paths** — The fields for **Explicitly allowed paths** and **Explicitly denied paths** let you tailor your runtime models, by explicitly denying paths in the model or explicitly allowing paths that aren’t in the model.
* **Extended behavioral container models** — Suspicious file system activities that are detected after the learning period, which Prisma Cloud algorithm identifies as "low severity". These activities are also added to the model. An alert will be only raised once with a message saying there is a low likelihood that this event is malicious, and no further alerts for this type of event will be raised.

### Custom rules

For details on custom rules policy refer to [this](/content-collections/runtime-security/runtime-defense/custom-runtime-rules.md) section.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.prismacloud.io/content-collections/runtime-security/runtime-defense/runtime-defense-containers.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
