---
title: "Miscellaneous"
weight: 6
summary: "The Miscellaneous section encompasses various additional and assorted commands or functionalities in knoxctl, providing supplementary tools and options for specialized or less common tasks in Kubernetes management."
---

## VM Commands for kvmservice

The `knoxctl vm` command suite offers a range of functionalities to manage Virtual Machines (VMs) within the kvmservice environment. These commands allow for the onboarding, offboarding, and management of VMs in the kvms control plane.

### Usage

To use VM-related commands, the basic syntax is:

```bash
knoxctl vm [command]
```

### Available Commands

Below are the available commands under `knoxctl vm` along with their descriptions:

- **add**: Onboard a new VM onto the kvms control plane.
- **delete**: Offboard an existing VM from the kvms control plane.
- **getscript**: Download the VM installation script for the kvms control plane.
- **label**: Handle labels for VMs in the kvms control plane.
- **list**: List all configured VMs within the control plane.
- **policy**: Manage policies for bare-metal VMs/kvms control plane VMs.

### Flags

The following flags are available for `knoxctl vm` commands:

| Flag           | Description                                                        |
| -------------- | ------------------------------------------------------------------ |
| `-h`, `--help` | Displays help information for the VM command.                      |
| `--http-ip`    | Specifies the IP address of the kvm-service (default "127.0.0.1"). |
| `--http-port`  | Specifies the port of the kvm-service (default "8000").            |
| `--kvms`       | Enable this flag if operating in a kvms environment/control-plane. |

These commands provide comprehensive control over VMs in a kvmservice environment, simplifying tasks related to VM lifecycle and policy management.

## System Dump

The `knoxctl sysdump` command is designed to collect comprehensive system dump information for troubleshooting and error reporting. It specifically gathers data from `accuknox-agents` and `KubeArmor`, encapsulating essential diagnostic information including logs from the pods present in these namespaces.

### Sysdump Usage

To use the `knoxctl sysdump` command, the basic syntax is:

```bash
knoxctl sysdump [flags]
```

This command is instrumental in generating detailed system reports, which are crucial for analyzing and resolving issues within your deployment.

### Sysdump Flags

The following flags are available for `knoxctl sysdump`:

| Flag                               | Description                                                                                                                                           |
| ---------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| `-f`, `--discovery-engine-sysdump` | Specifies the output file for the accuknox-agents dump. This flag allows you to define where the system dump for the accuknox-agents should be saved. |
| `-h`, `--help`                     | Displays help information for the sysdump command.                                                                                                    |
| `-k`, `--kubearmor-sysdump`        | Specifies the output file for the KubeArmor dump. This enables you to set the destination file for the system dump data collected from KubeArmor.     |

The `sysdump` command effectively gathers logs and other critical information from the specified namespaces, providing a valuable resource for diagnosing system issues and enhancing the effectiveness of troubleshooting processes.

By utilizing these flags, users can direct the output of the system dumps to specific files, thereby organizing and simplifying the process of data analysis and report generation.

## Global Flags

### `--context string`

- **Description**: Specifies the name of the kubeconfig context to use.
- **Use Case**: Particularly useful when managing multiple Kubernetes clusters. It allows you to switch between different contexts, directing `knoxctl` to operate within a specific Kubernetes environment.
- **Example Usage**: `knoxctl <command> --context=my-context-name`

### `--kubeconfig string`

- **Description**: Sets the path to the kubeconfig file for `knoxctl`.
- **Use Case**: The kubeconfig file contains vital configuration details about Kubernetes clusters, users, namespaces, and authentication methods. By default, `knoxctl` uses the kubeconfig file located at `$HOME/.kube/config`. However, this flag allows you to use a different kubeconfig file as necessary.
- **Example Usage**: `knoxctl <command> --kubeconfig=/path/to/kubeconfig`

!!! note
    In case you run into any issues, please feel free to email support@accuknox.com. For more details, please check out accuknox.com and help.accuknox.com.
