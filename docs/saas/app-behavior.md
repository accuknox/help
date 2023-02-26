## **App Behavior:**


Application Behavior of the cluster workloads that are onboarded to the Accuknox Saas are collected with help of KubeArmor and the AccuKnox Agents that are installed as Daemon sets in the cluster. The informations are collected at the pod level granularity. So that the users can get the information about each pods that are running in each namespaces. Application behavior of the cluster workloads are given in two ways, one is the list view and other is the Graphical view. 

 

**List View:** 

In the list view users can get the selected pod’s application behavior in 3 types of list namely: 

+ **File Observability:** 

It provides the information about the file access that are being happening the pod. 

It gives information like which process is accessing which file in the pod. 

Along with the file information it gives status of the access either allow, audit or deny.

![](/saas/images/app-behavior.png)


+ **Process Observability:** 

It shows what are all the process that are executing in the pod and which pods or container are executing that process.

It also gives information about the process that are blocked from execution in the pod. 


 ![](/saas/images/process-observability.png)


+ **Network Observability:** 

Network Observability shows the ingress and egress connection that are coming to ang going out of the pod. 

It gives the information regarding Port number, source from where the ingress connection is coming and Destination to which egress connection is destined to go.

![](/saas/images/network-observability.png)


**Graph view:** 

In the graph view we can see the process, file and network level application behavior of the pod in Graphical representation. 

![](/saas/images/graph-view.png)


When the user clicks on the connection line, it will show the process, file or network that the corresponding connection belongs. For example in the below screen, the user clicked connection was egress connection to the mysql pod from port number 3306. 

![](/saas/images/graph-view-info.png)