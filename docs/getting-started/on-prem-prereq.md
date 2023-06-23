---
hide:
  - toc
---

## **Resource requirements**

### EKS Clusters
| Capacity Type  | Instance type   |  Number of nodes  |
|----------------|-----------------|-------------------|
|Spot            |       t3.xlarge |                6  |
|Spot            | m5.xlarge       |  4                |

### RDS
| DB                | Type        |          Size  |
|-------------------|-------------|----------------|
|Aurora Postgres    |  Serverless |  0.5 - 4 ACUs  |

### ElastiCache
| Name/ID         | Type                                                                  |
|-----------------|-----------------------------------------------------------------------|
| Redis           | cache.m5.large                                                        |

### Load balancers
| Owner          |
|----------------|
| knox-gateway   |
| istio-ingress  |
| PPS            |
| SPIRE          |

### For hosting frontend
| Name        |
|-------------|
| S3          |
| CloudFront  |
| ACM         |

### EFS
| Number of file systems  |
|-------------------------|
| 6                       |

### Simple Email Service
*Production access*




- - - 
[SCHEDULE DEMO](https://www.accuknox.com/contact-us){ .md-button .md-button--primary }