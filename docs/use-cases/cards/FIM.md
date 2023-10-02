# FIM
File Integrity Monitoring

## Description
todo

## Attack Scenario
todo

## Tags
- CIS_v1.27
- Control-Id-5.1.6

## Policy Templates
### Service account token
```yaml
apiVersion: security.kubearmor.com/v1
kind: KubeArmorPolicy
metadata:
  name: ksp-wordpress-block-service-account
  namespace: wordpress-mysql
spec:
  severity: 2
  selector:
    matchLabels:
      app: wordpress
  file:
    matchDirectories:
      - dir: /run/secrets/kubernetes.io/serviceaccount/
        recursive: true
  action: Block
```
!!!!! null FILE NOT FOUND

## References
[MITRE XYZ](https://attack.mitre.org/techniques/T1528/)



