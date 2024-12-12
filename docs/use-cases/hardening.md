---
title: Hardening
description: AccuKnox provides a comprehensive hardening solution that helps you secure your Kubernetes workloads by enforcing security policies and best practices.
---
[comment]: <> (This is an auto-generated file. Do not edit manually.)

::cards:: cols=3

- title: Service Account token
  content: Protect access to k8s service account token
  image: images/uc/cert-file.png
  url: cards/Service-Account-token.md

- title: FIM
  content: File Integrity Monitoring
  image: images/uc/fim.png
  url: cards/FIM.md

- title: Packaging tools
  content: Deny execution of package management tools
  image: images/uc/pkg-deny.png
  url: cards/Packaging-tools.md

- title: Trusted certs bundle
  content: Protect write access to the trusted root certificates bundle
  image: images/uc/file-lock.png
  url: cards/Trusted-certs-bundle.md

- title: Database access
  content: Protect read/write access to raw database tables from unknown processes.
  image: images/uc/db-eye.png
  url: cards/Database-access.md

- title: Config data
  content: Protect access to configuration data containing plain text credentials.
  image: images/uc/cfg-key.png
  url: cards/Config-data.md

- title: File Copy
  content: Prevent file copy using standard utilities.
  image: images/uc/file-copy1.png
  url: cards/File-Copy.md

- title: Network Access
  content: Prevent network access to any processes or selectively enable network access to specific processes.
  image: images/uc/cloud-deny.png
  url: cards/Network-Access.md

- title: /tmp/ noexec
  content: Do not allow execution of binaries from /tmp/ folder.
  image: images/uc/file-exec-deny.png
  url: cards/_tmp_-noexec.md

- title: Admin tools
  content: Do not allow execution of administrative/maintenance tools inside the pods.
  image: images/uc/admin-tool.png
  url: cards/Admin-tools.md

- title: Discovery tools
  content: Do not allow discovery/search of tools/configuration.
  image: images/uc/file-search.png
  url: cards/Discovery-tools.md

- title: Logs delete
  content: Do not allow external tooling to delete logs/traces of critical components.
  image: images/uc/file-del.png
  url: cards/Logs-delete.md

- title: ICMP control
  content: Do not allow scanning tools to use ICMP for scanning the network.
  image: images/uc/ip.png
  url: cards/ICMP-control.md

- title: Restrict Capabilities
  content: Do not allow capabilities that can be leveraged by the attacker.
  image: images/uc/box-lock.png
  url: cards/Restrict-Capabilities.md

::/cards::

