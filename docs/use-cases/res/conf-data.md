#### Simulation

With a shell different than the user owning the file:
```sh
$ cat /etc/ca-certificates.conf                                                                                         
cat: /etc/ca-certificates.conf: Permission denied                                                                       
$                                                   
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
PolicyName: DefaultPosture                                                                                              
Source: /bin/cat /etc/ca-certificates.conf                                                                              
Resource: /etc/ca-certificates.conf                                                                                     
Operation: File                                                                                                        
Action: Block                                                                                                           
Data: syscall=SYS_OPEN flags=O_RDONLY                                                                                   
Enforcer: AppArmor                                                                                                      
Result: Permission denied                                                                                               
HostPID: 39039                                                                                                          
HostPPID: 38787                                                                                                         
Owner: map[Name:wordpress Namespace:wordpress-mysql Ref:Deployment]                                                     
PID: 220                                                                                                                
PPID: 219                                                                                                               
ParentProcessName: /bin/dash                                                                                            
ProcessName: /bin/cat                                                                                                   
UID: 1000 
```