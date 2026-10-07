For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/configure/custom-certs-predefined-dir.md).

You can use your own certs to secure Prisma Cloud communication channels by simply copying your custom certs to a predefined directory that the Console and Defender containers mount at runtime. No additional configuration in the Console UI is required to use your custom certs. This mechanism is enabled by default.

The communication channels you can secure with this mechanism are:

- Console web UI and API over HTTPS











By default, web and API clients connect to Console over HTTPS on port 8083. Out of the box, traffic is TLS encrypted using self-signed certs.

- Console-Defender communication over a WebSocket











By default, Defender connects to Console over a WebSocket on TCP port 8084. Out of the box, traffic between Defender and Console is TLS encrypted using self-signed certs.











By design, Console and Defender don’t trust each other. When Defender initiates a connection with Console, mutual TLS is used to verify both parties.


In general, the keys and certs used for Defender-Console communication are considered an internal implementation detail. Prisma Cloud generates, manages, and rotates the keys internally. However, if your organization’s policy calls for directly managing all keys and certs, Prisma Cloud gives you the control to do so.

## How it works[Direct link to heading](https://docs.prismacloud.io/admin-guide/configure/custom-certs-predefined-dir\#how-it-works)

Configure Console and Defender to use custom certs by saving the certs into a known, predefined directory. The predefined directory is `/var/lib/twistlock/custom-certificates`. The directory must be mounted in the Console and Defender container file systems when the Prisma Cloud containers are started.

When establishing a connection, the directory is checked for the required certificates. If the required files exist, they are used to establish the connection.

If there’s any error in the cert files (e.g., corrupt files, key-cert mismatch, etc.), the connection fails to be established, and an error is logged.

Prisma Cloud monitors the predefined directory for file system changes. If a relevant change is detected, the connection is restarted. For example, if console-cert.pem or console-key.pem are changed, the HTTPS listener is restarted. This system is designed to make rotating certificates easy by simply copying new certs to the predefined directory.

## Loading a TLS configuration[Direct link to heading](https://docs.prismacloud.io/admin-guide/configure/custom-certs-predefined-dir\#loading-a-tls-configuration)

When Console and Defender start, they create TLS configurations.

Depending on the environment, a number of scenarios are possible.

**Scenario: Console/Defender starts and the predefined custom certificates directory doesn’t exist and isn’t mounted in the container.**

In this case, the feature is switched off. Console/Defender uses its own self-signed certificates.

**Scenario: Console/Defender starts and finds the predefined custom certificates directory mounted, but not all of the required files exist.**

For example, Defender requires three files to secure Console-Defender communication: defender-ca.pem, defender-client-cert.pem, defender-client-key.pem. In this scenario, assume the defender-ca.pem file is missing.

In this case, Prisma Cloud initializes the connection using its own self-signed certificates, and then watches the predefined custom directory for changes. If there are changes to the predefined directory, Prisma Cloud checks if all certificate files exist. If they do, it tries to create a TLS configuration using those certs. If it succeeds, the connection is reset and new connection is established with the custom certs. If it fails, Prisma Cloud logs an error and keeps the existing connection.

**Scenario: Console/Defender starts and finds the required certificates in the mounted directory**

Prisma Cloud reads the certs and creates a TLS configuration. If reading a cert fails, Console/Defender logs the following messages, and exits:

AskCopy

```
 DEBU 2021-10-27T17:37:46.645 defender.go:1928  Using custom directory certificates
 CRIT 2021-10-27T17:37:46.645 defender.go:285  Failed to construct defender client TLS config error reading X509 key pair (/var/lib/twistlock/custom-certificates/defender-client-cert.pem, /var/lib/twistlock/custom-certificates/defender-client-key.pem): tls: failed to parse private key
```

### Fixing misconfigurations[Direct link to heading](https://docs.prismacloud.io/admin-guide/configure/custom-certs-predefined-dir\#fixing-misconfigurations)

If there’s an error loading your certs (for example, malformed key material), you can fix the problem by simply copying fixed certs to the predefined directory. As long as the Prisma Cloud container starts with the predefined directory mounted, it can watch the directory for changes, and try to reestablish a new connection with the latest certs when new files are detected

This, in conjunction with the verbose log messages, will help you get your configuration right.

## Required certificate files[Direct link to heading](https://docs.prismacloud.io/admin-guide/configure/custom-certs-predefined-dir\#required-certificate-files)

To secure a connection with your custom certs, Prisma Cloud looks for specific files in `/var/lib/twistlock/custom-certificates`.

### Console[Direct link to heading](https://docs.prismacloud.io/admin-guide/configure/custom-certs-predefined-dir\#console)

For the Console HTTPS listener (for securing the web UI and API), the following files must be available in the predefined directory:

- `console-cert.pem`

- `console-key.pem`


For Console’s WebSocket listener (for securing Console-Defender communication), the required files are:

- `defender-ca.pem`

- `defender-server-cert.pem`

- `defender-server-key.pem`


### Defender[Direct link to heading](https://docs.prismacloud.io/admin-guide/configure/custom-certs-predefined-dir\#defender)

For Defender’s WebSocket listener (for securing Console-Defender communication), the required files are:

- `defender-ca.pem`

- `defender-client-cert.pem`

- `defender-client-key.pem`


## Log messages[Direct link to heading](https://docs.prismacloud.io/admin-guide/configure/custom-certs-predefined-dir\#log-messages)

Clear operational and error messages are sent to the Console and Defender logs so you can debug certificate issues.

On startup, the following message is logged, indicating the custom directory is mounted and being tracked for rotations:

AskCopy

```
Watching custom certificates directory: /var/lib/twistlock/custom-certificates
```

If the directory was not mounted, the following message is logged:

AskCopy

```
Custom certificates watcher disabled: certificates directory is not mounted
```

Upon resetting a connection following a cert rotation, a message is logged, e.g.,

AskCopy

```
Defender custom certificates rotated, resetting connection
```

Any error in the cert files (e.g., corrupt files, key-cert mismatch, etc.) will result in failure to establish connection, and it’s logged as an error.

## Deployment patterns[Direct link to heading](https://docs.prismacloud.io/admin-guide/configure/custom-certs-predefined-dir\#deployment-patterns)

This feature depends on your key material already being present on each node where Console and Defender run. Certificate enrollment, renewal, and management are strictly your responsibility.

The predefined custom certs directory must be mounted into Console/Defender’s file system when the containers start (or restart). Console/Defender only requires read access to the predefined directory.

In general, you should have some kind of network storage (e.g., NFS), where you can centrally store and rotate your custom certs. All pods would mount the same network volume, so that when you rotate your certs, the latest files are available to all pods at the same time.

### Onebox[Direct link to heading](https://docs.prismacloud.io/admin-guide/configure/custom-certs-predefined-dir\#onebox)

1. Before installing Onebox, create the predefined custom certs directory.

















AskCopy



```
mkdir -p /var/lib/twistlock/custom-certificates
```

2. Install [Onebox](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-onebox).

3. Check the Console and Defender logs.











A log message says the pre-created directory was identified and that it’s being watched.

















AskCopy



```
DEBU 2021-11-11T11:59:33.296 cert_watcher.go:45 Watching custom certificates directory: /var/lib/twistlock/custom-certificates
```

4. Copy your custom certificates to the pre-created directory.











Both Console and Defender watch this directory for their certificates Connections are reset when relevant changes are detected.


### Deploying Console and Defender in Kubernetes or OpenShift clusters[Direct link to heading](https://docs.prismacloud.io/admin-guide/configure/custom-certs-predefined-dir\#deploying-console-and-defender-in-kubernetes-or-openshift-clusters)

The following steps provide high-level guidance for deploying Prisma Cloud containers with your custom certs in your clusters.

1. Use twistcli to generate a Defender DaemonSet YAML configuration file.









   - [Console on Kubernetes](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-kubernetes)

   - [Console on OpenShift](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-openshift)

   - [Defender DaemonSets on Kubernetes](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/compute-edition/34/admin-guide/install/deploy-defender/orchestrator/orchestrator.md)

   - [Defender DaemonSets for OpenShift](https://docs.prismacloud.io/admin-guide/install/deploy-defender/orchestrator/openshift)


2. Before deploying, open the YAML file, and add a volume mount for the predefined directory, `/var/lib/twistlock/custom-certificates/`.











For example:

















AskCopy



```
apiVersion: v1
kind: Pod
metadata:
     name: example-pod
spec:
     volumes:
    - name: example-pv-storage
      persistentVolumeClaim:
        claimName: example-pv-claim
containers:
    - name: defender-container
      image: defender-image
      volumeMounts:
        - mountPath: "/var/lib/twistlock/custom-certificates/"
          name: example-pv-storage
```

## Limitations[Direct link to heading](https://docs.prismacloud.io/admin-guide/configure/custom-certs-predefined-dir\#limitations)

App-Embedded and Serverless Defenders currently do not support custom keys and certs for securing Console-Defender communication.

[PreviousAuthenticate to Console with certificates](https://docs.prismacloud.io/admin-guide/configure/authenticate-console-with-certs) [NextCustomize terminal output](https://docs.prismacloud.io/admin-guide/configure/customize-terminal-output)

Last updated 3 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
