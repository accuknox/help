::cards:: cols=3

- title: FIM
  content: |
	File Integrity Monitoring, Prevent write access to systems folders path.
  image: images/uc/fim.png
  url: https://en.wikipedia.org/wiki/Hardening_(computing)

- title: Packaging tools
  content: |
	Deny execution of package management tools.
  image: images/uc/pkg-deny.png
  url: https://en.wikipedia.org/wiki/Hardening_(computing)

- title: Account Token
  content: Protect access to service account token
  image: images/uc/cert-file.png
  url: https://en.wikipedia.org/wiki/Hardening_(computing)

- title: Trusted cert bundle
  content: Protect write access to the trusted root certificates bundle.
  image: images/uc/file-lock.png
  url: https://en.wikipedia.org/wiki/Hardening_(computing)

- title: Database access
  content: Protect read/write access to raw database tables from unknown processes.
  image: images/uc/db-eye.png
  url: https://en.wikipedia.org/wiki/Hardening_(computing)

- title: Config data
  content: Protect access to configuration data containing plain text credentials.
  image: images/uc/cfg-key.png
  url: https://en.wikipedia.org/wiki/Hardening_(computing)

- title: File Copy
  content: Prevent file copy using standard utilities.
  image: images/uc/file-copy1.png
  url: https://en.wikipedia.org/wiki/Hardening_(computing)

- title: Network Access
  content: Prevent network access to any processes or selectively enable network access to specific processes.
  image: images/uc/cloud-deny.png
  url: https://en.wikipedia.org/wiki/Hardening_(computing)

- title: /tmp/ noexec
  content: Do not allow execution of binaries from /tmp/ folder.
  image: images/uc/file-exec-deny.png
  url: https://en.wikipedia.org/wiki/Hardening_(computing)

- title: Admin tools
  content: Do not allow execution of administrative/maintenance tools inside the pods.
  image: images/uc/admin-tool.png
  url: https://en.wikipedia.org/wiki/Hardening_(computing)

- title: Discovery tools
  content: Do not allow discovery/search of tools/configuration.
  image: images/uc/file-search.png
  url: https://en.wikipedia.org/wiki/Hardening_(computing)

- title: Logs delete
  content: Do not allow external tooling to delete logs/traces of critical components.
  image: images/uc/file-del.png
  url: https://en.wikipedia.org/wiki/Hardening_(computing)

- title: ICMP control
  content: Do not allow scanning tools to use ICMP for scanning the network.
  image: images/uc/ip.png
  url: https://en.wikipedia.org/wiki/Hardening_(computing)

::/cards::

