---
title: "KubeArmor"
weight: 4
summary: "KubeArmor uses eBPF and Linux Security Modules (LSM) to provide a policy-based system to restrict any unwanted, malicious behavior of cloud-native workloads at runtime."
---

KubeArmor uses eBPF and Linux Security Modules (LSM) to provide a policy-based system to restrict any unwanted, malicious behavior of cloud-native workloads at runtime. To know more about KubeArmor, please check out [kubearmor.io](https://kubearmor.io).

## Logs

The `knoxctl logs` command is used to observe logs from KubeArmor. It provides a way to monitor and retrieve logs related to various activities and events within your Kubernetes environment.

### Logs Usage

To use the `knoxctl logs` command, the basic syntax is:

```bash
knoxctl logs [flag] [option]
```

### Logs Flags

Below is a table of flags available with the `knoxctl logs` command, along with their descriptions:

| Flag                | Description                                                            |
| ------------------- | ---------------------------------------------------------------------- | ------ | -------------------------- |
| `--container`       | Name of the container.                                                 |
| `--gRPC`            | gRPC server information.                                               |
| `--json`            | Flag to print alerts and logs in the JSON format.                      |
| `-l`, `--labels`    | Use the labels to select the endpoints.                                |
| `--limit`           | Number of logs you want to see.                                        |
| `--logFilter`       | Filter for what kinds of alerts and logs to receive, options: `{policy | system | all}` (default "policy").  |
| `--logPath`         | Output location for alerts and logs, options: `{path                   | stdout | none}` (default "stdout"). |
| `--logType`         | Log type you want (e.g., ContainerLog/HostLog).                        |
| `--msgPath`         | Output location for messages, options: `{path                          | stdout | none}` (default "none").   |
| `-n`, `--namespace` | Kubernetes namespace filter.                                           |
| `--operation`       | Type of operation (e.g., Process/File/Network).                        |
| `--pod`             | Name of the pod.                                                       |
| `--resource`        | Command used by the user.                                              |
| `--source`          | Binary used by the system.                                             |
| `-h`, `--help`      | Help for logs.                                                         |

Use these flags to tailor the `knoxctl logs` output to your specific requirements, whether it's for debugging, monitoring, or auditing purposes within your Kubernetes cluster.

## Probe

The `knoxctl probe` command is designed to check for supported KubeArmor features in the current Kubernetes environment. This command is essential for understanding the compatibility and feature support of KubeArmor in different deployment scenarios.

### Probe Usage

To use the `knoxctl probe` command, the basic syntax is:

```bash
knoxctl probe [flags]
```

The `probe` command operates differently based on whether KubeArmor is currently running:

- **If KubeArmor is Not Running**: The command performs a pre-check to determine if KubeArmor will be supported in the environment and identifies which features (e.g., observability, enforcement) will be available.

- **If KubeArmor is Running**: It probes the environment where KubeArmor is running (e.g., systemd mode, Kubernetes, etc.), the supported KubeArmor features, the pods being handled by KubeArmor, and the policies running on each of these pods.

### Probe Flags

Below is a table of flags available with the `knoxctl probe` command, along with their descriptions:

| Flag                | Description                                                                                                                                                                        |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `--full`            | If KubeArmor is not running, this flag deploys a daemonset to gather more detailed information about KubeArmor support in the environment. The daemonset is deleted after probing. |
| `-h`, `--help`      | Provides help information for the probe command.                                                                                                                                   |
| `-n`, `--namespace` | Specifies the namespace for resources (default "kube-system").                                                                                                                     |

This command is particularly useful for administrators and operators to ensure that their environment is compatible with KubeArmor and to understand the extent of its feature support. Use the `--full` flag for a more comprehensive probe, especially when KubeArmor is not running.

## Profile

The `knoxctl profile` command is used for profiling logs within your Kubernetes environment. This command starts a Terminal User Interface (TUI) that allows for an interactive and real-time analysis of log data.

### Profile Usage

To use the `knoxctl profile` command, the basic syntax is:

```bash
knoxctl profile [flags]
```

When executed, `knoxctl profile` launches a TUI, enabling users to interactively navigate and inspect the logs.

### Profile Flags

Below is a table of flags available with the `knoxctl profile` command, along with their descriptions:

| Flag           | Description                                                  |
| -------------- | ------------------------------------------------------------ |
| `--gRPC`       | Specify the gRPC server information for the profile command. |
| `-h`, `--help` | Provides help information for the profile command.           |
| `--namespace`  | Filter logs based on a specific Kubernetes namespace.        |
| `--pod`        | Filter logs based on a specific Pod name.                    |

The `knoxctl profile` command is particularly useful for administrators and developers who need to analyze and understand the behavior of their applications and the Kubernetes environment. By using the TUI, users can dynamically interact with log data, making the process of log analysis more efficient and insightful.

## Rotate TLS

The `knoxctl rotate-tls` command is used to rotate TLS certificates for the webhook controller. This operation is crucial for maintaining the security and integrity of TLS communication within your Kubernetes environment.

### Rotate TLS Usage

To use the `knoxctl rotate-tls` command, the basic syntax is:

```bash
knoxctl rotate-tls [flags]
```

This command facilitates the rotation of TLS certificates, ensuring that your webhook controllers are using up-to-date and secure certificates.

### Rotate TLS Flags

The following table lists the available flags for the `knoxctl rotate-tls` command, along with their descriptions:

| Flag                | Description                                                              |
| ------------------- | ------------------------------------------------------------------------ |
| `-h`, `--help`      | Displays help information for the rotate-tls command.                    |
| `-n`, `--namespace` | Specifies the namespace for the resources. The default is "kube-system". |

Rotating TLS certificates is a best practice for securing webhook communications. By regularly updating certificates, you can prevent potential security breaches and ensure the confidentiality and integrity of the data transmitted between services.

!!! note
    In case you run into any issues, please feel free to email support@accuknox.com. For more details, please check out accuknox.com and help.accuknox.com.
