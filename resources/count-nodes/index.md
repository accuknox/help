---
title: Count Nodes in Kubernetes Cluster
description: Learn how to retrieve the Kubernetes node count using the kubectl command for cluster monitoring and capacity planning.
---


To get the kubernetes node count from your cluster you should use the following command:

```sh
kubectl get nodes --no-headers=true | wc -l
```