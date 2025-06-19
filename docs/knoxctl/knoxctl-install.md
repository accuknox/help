---
title: 'Install knoxctl'
weight: 3
Summary: 'To install knoxctl, begin by downloading the appropriate binary for your operating system and system architecture.'
---

To install `knoxctl`, begin by downloading the appropriate binary for your operating system and system architecture. Currently, `knoxctl` supports only Unix-family operating systems. To determine the specific details of your system, such as the operating system type and architecture, you can use the `uname -a` command in your terminal. This command will provide you with the necessary information to select the correct binary version of `knoxctl` for your system.

Please ensure you download the version that matches your system's specifications. If you encounter any compatibility issues or need assistance, feel free to visit our support page.

- [Release version](https://knoxctl.accuknox.com/version/latest_version.txt)
- [knoxctl for Linux (AMD64/x86_64)](https://knoxctl.accuknox.com/binaries/knoxctl_0.3.0_linux_amd64.tar.gz)
- [knoxctl for Linux (ARM64)](https://knoxctl.accuknox.com/binaries/knoxctl_0.3.0_linux_arm64.tar.gz)
- [knoxctl for Mac (Intel)](https://knoxctl.accuknox.com/binaries/knoxctl_0.3.0_darwin_amd64.tar.gz)
- [knoxctl for Mac (Apple Silicon)](https://knoxctl.accuknox.com/binaries/knoxctl_0.3.0_darwin_arm64.tar.gz)

!!! info
    To install `knoxctl`, you can use the following command:

    ```bash
    curl -sfL https://knoxctl.accuknox.com/install.sh | sudo sh -s -- -b /usr/local/bin
    ```
    In case knoxctl update failed due to KubeArmor Policy, please run the following command before trying to upgrade

    ```bash
    sudo systemctl stop kubearmor.service
    ```

!!! note
    In case you run into any issues, please feel free to email support@accuknox.com. For more details, please check out accuknox.com and help.accuknox.com.