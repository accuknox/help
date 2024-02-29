---
hide:
  - toc
---

Follow the below steps to add the KubeArmor helm chart to Lens and deploy it,

**Step 1**: Navigate to File → Preferences or press Ctrl+Comma to open the Preferences menu and select the Kubernetes tab.

![](images/lens/lens-0.png)

**Step 2**: Click on “Add Custom Helm Repo” and enter the following info:

- Name: kubearmor
- URL: ```https://kubearmor.github.io/charts```

Click on Add

![](images/lens/lens-ka-1.png)

**Step 3**: Navigate to your cluster on Lens, goto Helm → Charts and search KubeArmor. Select the “kubearmor-operator” and click on Install. (Press ctrl+R to reload if you can’t find it)

![](images/lens/lens-ka-2.png)

**Step 4**: In the Helm chart tab that opens, do the following:

- Set the value ```autoDeploy: true```
- Select a namespace to deploy, i.e. kubearmor

Finally click on Install

![](images/lens/lens-ka-3.png)

Wait for the operator to finish deploying the necessary components. This will deploy KubeArmor on the cluster with the default options.