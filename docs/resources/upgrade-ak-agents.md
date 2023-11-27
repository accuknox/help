---
hide:
  - toc
---

# **Upgrading AccuKnox Agents**

To check for the current version of the accuknox-agents chart deployed, please execute the following command:

```sh
helm list -n accuknox-agents
```

Sample Output:

```sh
~$ helm list -n accuknox-agents
NAME            NAMESPACE       REVISION        UPDATED                                 STATUS          CHART                   APP VERSION
accuknox-agents accuknox-agents 1               2023-09-14 15:31:56.378824112 +0530 IST deployed        accuknox-agents-v0.1.5  v0.1.5 
```

If the output of the command shows the version as lower than 2.6 then it will be necessary to upgrade to the latest version. 

The following command can be used for performing the upgrade:

```sh
helm upgrade --install accuknox-agents oci://public.ecr.aws/k9v9d5v2/accuknox-agents --version "v0.2.6" -n accuknox-agents
```


  - - - 
[SCHEDULE DEMO](https://www.accuknox.com/contact-us){ .md-button .md-button--primary }
