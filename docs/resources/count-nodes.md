---
title: Count Nodes in Kubernetes Cluster
description: Get the kubernetes node count from your cluster using the kubectl command.
---


To get the kubernetes node count from your cluster you should use the following command:

```sh
kubectl get nodes --no-headers=true | wc -l
```