---
hide:
  - toc
---

To get the kubernetes node count from your cluster you should use the following command:

```sh
kubectl get nodes --no-headers=true | wc -l
```