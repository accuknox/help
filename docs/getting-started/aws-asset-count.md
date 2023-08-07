## Prerequisites

Need an IAM Access key and Secret key with the entire account ReadOnly Access. 

## Assets count

**1.All EC2 instances:**

```sh
aws ec2 describe-instances --region "$region" --output text --query 'length(Reservations[].Instances[])'
```

**2.EBS Volume Count:**

```sh
aws ec2 describe-volumes --region "$region" --query 'length(Volumes[])'
```

**3.s3 buckets:**

```sh
aws s3api list-buckets --query 'length(Buckets[])'
```

**4.RDS:**

```sh
aws rds describe-db-instances --region "$region" --query 'length(DBInstances[])'
```

**5.VPCs:**

```sh
aws ec2 describe-vpcs --region "$region" --query 'length(Vpcs[])'
```

**6.Load Balancers:**

```sh
aws elbv2 describe-load-balancers --region "$region" --query 'length(LoadBalancers[])'
```

**7.Lambda functions:**

```sh
aws lambda list-functions --region "$region" --query 'length(Functions[])'
```

**8.EKS clusters:**

```sh
aws eks list-clusters --region "$region" --query 'length(clusters[])'
```

**9.IAM roles:**

```sh
aws iam list-roles --query 'length(Roles[])'
```

**10.ECS Clusters:**

```sh
aws ecs list-clusters --region "$region" --query 'length(clusterArns[])'
```

**11.AWS Subnets:**

```sh
aws ec2 describe-subnets --region "$region" --query 'length(Subnets[])'
```

**12.Security groups:**

```sh
aws ec2 describe-security-groups --region "$region" --query 'length(SecurityGroups[])'
```

**13.KMS Key:**

```sh
aws kms list-keys --region "$region"--query 'length(Keys)'
```

**14.RDS Clusters:**

```sh
aws rds describe-db-clusters --region "$region" --query 'length(DBClusters)'
```

**15.Network ACL:**

```sh
aws ec2 describe-network-acls --region "$region" --query 'length(NetworkAcls)'
```

**16.IAM Users:**

```sh
aws iam list-users --query 'length(Users[])'
```

**17.IAM Groups:**

```sh
aws iam list-groups --query 'length(Groups[])'
```

**18.VPC Peering Connections:**

```sh
aws ec2 describe-vpc-peering-connections --region "$region" --query 'length(VpcPeeringConnections[])'
```

**19.EIP:**

```sh
aws ec2 describe-addresses --region "$region" --query 'length(Addresses[])'
```

**20.VPC Route table:**

```sh
aws ec2 describe-route-tables --region "$region" --query 'length(RouteTables[])'
```

**21.Elastic Cache Clusters:**

```sh
aws elasticache describe-cache-clusters --region "$region" --query 'length(CacheClusters[])'
```

## Bash script to get AWS Assets count

```sh
#!/bin/bash
regions=$(aws ec2 describe-regions --query 'Regions[].RegionName' --output text)
sum_count=0
for region in $regions; do
countec2=0
countebs=0
countvpc=0
countrds=0
countlamb=0
countnci=0
countsub=0
countnlb=0
countkey=0
countecs=0
counteks=0
countpeer=0
countelccl=0
countrdsc=0
counteip=0
countsg=0
countrtab=0
countnetacl=0
echo -e "Assets in the Region: $region\n\n"
countec2=$(aws ec2 describe-instances --region "$region" --output text --query 'length(Reservations[].Instances[])')
echo "Ec2 instances in Region: $region is $countec2"
countebs=$(aws ec2 describe-volumes --region "$region" --query 'length(Volumes[])')
echo "Elastic Block Storage in Region: $region is $countebs"
countvpc=$(aws ec2 describe-vpcs --region "$region" --query 'length(Vpcs[])')
echo "VPC in Region: $region is $countvpc"
countrds=$(aws rds describe-db-instances --region "$region" --query 'length(DBInstances[])')
echo "RDS in Region: $region is $countrds"
countlamb=$(aws lambda list-functions --region "$region" --query 'length(Functions[])')
echo "Lambda Functions in Region: $region is $countlamb"
countnci=$(aws ec2 describe-network-interfaces --region "$region" --query 'length(NetworkInterfaces)')
echo "Ec2 Network Interfaces in Region: $region is $countnci"
countsub=$(aws ec2 describe-subnets --region "$region" --query 'length(Subnets[])')
echo "Subnets in the Region: $region is $countsub"
countnlb=$(aws elbv2 describe-load-balancers --region "$region" --query 'length(LoadBalancers[])')
echo "Network Load Balancers in Region: $region is $countnlb"
countkey=$(aws kms list-keys --region "$region" --query 'length(Keys[])')
echo "KMS Key in the region: $region is $countkey"
countecs=$(aws ecs list-clusters --region "$region" --query 'length(clusterArns[])')
echo "ECS Clusters across region : $region is $countecs"
counteks=$(aws eks list-clusters --region "$region" --query 'length(clusters[])')
echo "EKS Clusters across region : $region is $counteks"
countpeer=$(aws ec2 describe-vpc-peering-connections --region "$region" --query 'length(VpcPeeringConnections[])')
echo "VPC Peering in the region : $region is $countpeer"
countelcl=$(aws elasticache describe-cache-clusters --region "$region" --query 'length(CacheClusters[])')
echo "Elastic Cache Clusters in the region : $region is $countelcl"
countrdsc=$(aws rds describe-db-clusters --region "$region" --query 'length(DBClusters)')
echo "RDS Clusters in the region : $region is $countrdsc"
counteip=$(aws ec2 describe-addresses --region "$region" --query 'length(Addresses[])')
echo "Elastic IP in the region : $region is $counteip"
countsg=$(aws ec2 describe-security-groups --region "$region" --query 'length(SecurityGroups[])')
echo "Security Groups in the region : $region is $countsg"
countrtab=$(aws ec2 describe-route-tables --region "$region" --query 'length(RouteTables[])')
echo "Route table in the region : $region is $countrtab"
countnetacl=$(aws ec2 describe-network-acls --region "$region" --query 'length(NetworkAcls)')
echo -e "Network ACL in the region : $region is $countnetacl\n\n"
sum_count=$((sum_count + countec2 + countebs + countvpc + countrds + countlamb + countelb + countnci + countnlb + countsub + countkey + countecs + counteks + countpeer + countelccl + countrdsc + counteip + countsg + countrtab + countnetacl ))
done
counts3=$(aws s3api list-buckets --query 'length(Buckets[])')
echo -e "s3 buckets in the account is $counts3\n\n"
countiusers=$(aws iam list-users --query 'length(Users[])')
echo -e "IAM users in the account is $countiusers\n\n"
countgroups=$(aws iam list-groups --query 'length(Groups[])')
echo -e "IAM Groups in the account is $countgroups\n\n"
countiroles=$(aws iam list-roles --query 'length(Roles[])')
echo -e "IAM Roles in the account is $countiroles\n\n"
total_count=$((sum_count + counts3 + countiusers + countgroups + countiroles))
echo "Total Assets in this AWS account is : $total_count"
```

## Sample Output

```
Assets in the Region: ap-south-1

Ec2 instances in Region: ap-south-1 is 1
Elastic Block Storage in Region: ap-south-1 is 1
VPC in Region: ap-south-1 is 2
RDS in Region: ap-south-1 is 0
Lambda Functions in Region: ap-south-1 is 0
Ec2 Network Interfaces in Region: ap-south-1 is 1
Subnets in the Region: ap-south-1 is 5
Network Load Balancers in Region: ap-south-1 is 0
KMS Key in the region: ap-south-1 is 2
ECS Clusters across region : ap-south-1 is 1
EKS Clusters across region : ap-south-1 is 0
VPC Peering in the region : ap-south-1 is 0
Elastic Cache Clusters in the region : ap-south-1 is 0
RDS Clusters in the region : ap-south-1 is 0
Elastic IP in the region : ap-south-1 is 0
Security Groups in the region : ap-south-1 is 3
Route table in the region : ap-south-1 is 3
Network ACL in the region : ap-south-1 is 2


Assets in the Region: eu-north-1


Ec2 instances in Region: eu-north-1 is 0
Elastic Block Storage in Region: eu-north-1 is 0
VPC in Region: eu-north-1 is 1
RDS in Region: eu-north-1 is 0
Lambda Functions in Region: eu-north-1 is 0
Ec2 Network Interfaces in Region: eu-north-1 is 0
Subnets in the Region: eu-north-1 is 3
Network Load Balancers in Region: eu-north-1 is 0
KMS Key in the region: eu-north-1 is 1
ECS Clusters across region : eu-north-1 is 0
EKS Clusters across region : eu-north-1 is 0
VPC Peering in the region : eu-north-1 is 0
Elastic Cache Clusters in the region : eu-north-1 is 0
RDS Clusters in the region : eu-north-1 is 0
Elastic IP in the region : eu-north-1 is 0
Security Groups in the region : eu-north-1 is 1
Route table in the region : eu-north-1 is 1
Network ACL in the region : eu-north-1 is 1


Assets in the Region: eu-west-3


Ec2 instances in Region: eu-west-3 is 0
Elastic Block Storage in Region: eu-west-3 is 0
VPC in Region: eu-west-3 is 1
RDS in Region: eu-west-3 is 0
Lambda Functions in Region: eu-west-3 is 0
Ec2 Network Interfaces in Region: eu-west-3 is 0
Subnets in the Region: eu-west-3 is 3
Network Load Balancers in Region: eu-west-3 is 0
KMS Key in the region: eu-west-3 is 0
ECS Clusters across region : eu-west-3 is 0
EKS Clusters across region : eu-west-3 is 0
VPC Peering in the region : eu-west-3 is 0
Elastic Cache Clusters in the region : eu-west-3 is 0
RDS Clusters in the region : eu-west-3 is 0
Elastic IP in the region : eu-west-3 is 0
Security Groups in the region : eu-west-3 is 1
Route table in the region : eu-west-3 is 1
Network ACL in the region : eu-west-3 is 1


Assets in the Region: eu-west-2


Ec2 instances in Region: eu-west-2 is 16
Elastic Block Storage in Region: eu-west-2 is 48
VPC in Region: eu-west-2 is 2
RDS in Region: eu-west-2 is 1
Lambda Functions in Region: eu-west-2 is 0
Ec2 Network Interfaces in Region: eu-west-2 is 64
Subnets in the Region: eu-west-2 is 15
Network Load Balancers in Region: eu-west-2 is 1
KMS Key in the region: eu-west-2 is 28
ECS Clusters across region : eu-west-2 is 0
EKS Clusters across region : eu-west-2 is 1
VPC Peering in the region : eu-west-2 is 0
Elastic Cache Clusters in the region : eu-west-2 is 1
RDS Clusters in the region : eu-west-2 is 1
Elastic IP in the region : eu-west-2 is 2
Security Groups in the region : eu-west-2 is 12
Route table in the region : eu-west-2 is 4
Network ACL in the region : eu-west-2 is 2


Assets in the Region: eu-west-1


Ec2 instances in Region: eu-west-1 is 0
Elastic Block Storage in Region: eu-west-1 is 2
VPC in Region: eu-west-1 is 1
RDS in Region: eu-west-1 is 0
Lambda Functions in Region: eu-west-1 is 0
Ec2 Network Interfaces in Region: eu-west-1 is 2
Subnets in the Region: eu-west-1 is 3
Network Load Balancers in Region: eu-west-1 is 0
KMS Key in the region: eu-west-1 is 6
ECS Clusters across region : eu-west-1 is 0
EKS Clusters across region : eu-west-1 is 0
VPC Peering in the region : eu-west-1 is 0
Elastic Cache Clusters in the region : eu-west-1 is 0
RDS Clusters in the region : eu-west-1 is 0
Elastic IP in the region : eu-west-1 is 0
Security Groups in the region : eu-west-1 is 5
Route table in the region : eu-west-1 is 1
Network ACL in the region : eu-west-1 is 1


Assets in the Region: ap-northeast-3


Ec2 instances in Region: ap-northeast-3 is 0
Elastic Block Storage in Region: ap-northeast-3 is 0
VPC in Region: ap-northeast-3 is 1
RDS in Region: ap-northeast-3 is 0
Lambda Functions in Region: ap-northeast-3 is 0
Ec2 Network Interfaces in Region: ap-northeast-3 is 0
Subnets in the Region: ap-northeast-3 is 3
Network Load Balancers in Region: ap-northeast-3 is 0
KMS Key in the region: ap-northeast-3 is 0
ECS Clusters across region : ap-northeast-3 is 0
EKS Clusters across region : ap-northeast-3 is 0
VPC Peering in the region : ap-northeast-3 is 0
Elastic Cache Clusters in the region : ap-northeast-3 is 0
RDS Clusters in the region : ap-northeast-3 is 0
Elastic IP in the region : ap-northeast-3 is 0
Security Groups in the region : ap-northeast-3 is 1
Route table in the region : ap-northeast-3 is 1
Network ACL in the region : ap-northeast-3 is 1


Assets in the Region: ap-northeast-2


Ec2 instances in Region: ap-northeast-2 is 0
Elastic Block Storage in Region: ap-northeast-2 is 0
VPC in Region: ap-northeast-2 is 1
RDS in Region: ap-northeast-2 is 0
Lambda Functions in Region: ap-northeast-2 is 0
Ec2 Network Interfaces in Region: ap-northeast-2 is 0
Subnets in the Region: ap-northeast-2 is 4
Network Load Balancers in Region: ap-northeast-2 is 0
KMS Key in the region: ap-northeast-2 is 0
ECS Clusters across region : ap-northeast-2 is 0
EKS Clusters across region : ap-northeast-2 is 0
VPC Peering in the region : ap-northeast-2 is 0
Elastic Cache Clusters in the region : ap-northeast-2 is 0
RDS Clusters in the region : ap-northeast-2 is 0
Elastic IP in the region : ap-northeast-2 is 0
Security Groups in the region : ap-northeast-2 is 1
Route table in the region : ap-northeast-2 is 1
Network ACL in the region : ap-northeast-2 is 1


Assets in the Region: ap-northeast-1


Ec2 instances in Region: ap-northeast-1 is 0
Elastic Block Storage in Region: ap-northeast-1 is 0
VPC in Region: ap-northeast-1 is 1
RDS in Region: ap-northeast-1 is 0
Lambda Functions in Region: ap-northeast-1 is 0
Ec2 Network Interfaces in Region: ap-northeast-1 is 0
Subnets in the Region: ap-northeast-1 is 3
Network Load Balancers in Region: ap-northeast-1 is 0
KMS Key in the region: ap-northeast-1 is 0
ECS Clusters across region : ap-northeast-1 is 0
EKS Clusters across region : ap-northeast-1 is 0
VPC Peering in the region : ap-northeast-1 is 0
Elastic Cache Clusters in the region : ap-northeast-1 is 0
RDS Clusters in the region : ap-northeast-1 is 0
Elastic IP in the region : ap-northeast-1 is 0
Security Groups in the region : ap-northeast-1 is 1
Route table in the region : ap-northeast-1 is 1
Network ACL in the region : ap-northeast-1 is 1


Assets in the Region: ca-central-1


Ec2 instances in Region: ca-central-1 is 0
Elastic Block Storage in Region: ca-central-1 is 0
VPC in Region: ca-central-1 is 1
RDS in Region: ca-central-1 is 0
Lambda Functions in Region: ca-central-1 is 0
Ec2 Network Interfaces in Region: ca-central-1 is 0
Subnets in the Region: ca-central-1 is 3
Network Load Balancers in Region: ca-central-1 is 0
KMS Key in the region: ca-central-1 is 5
ECS Clusters across region : ca-central-1 is 0
EKS Clusters across region : ca-central-1 is 0
VPC Peering in the region : ca-central-1 is 0
Elastic Cache Clusters in the region : ca-central-1 is 0
RDS Clusters in the region : ca-central-1 is 0
Elastic IP in the region : ca-central-1 is 0
Security Groups in the region : ca-central-1 is 1
Route table in the region : ca-central-1 is 1
Network ACL in the region : ca-central-1 is 1


Assets in the Region: sa-east-1


Ec2 instances in Region: sa-east-1 is 0
Elastic Block Storage in Region: sa-east-1 is 0
VPC in Region: sa-east-1 is 1
RDS in Region: sa-east-1 is 0
Lambda Functions in Region: sa-east-1 is 0
Ec2 Network Interfaces in Region: sa-east-1 is 0
Subnets in the Region: sa-east-1 is 3
Network Load Balancers in Region: sa-east-1 is 0
KMS Key in the region: sa-east-1 is 0
ECS Clusters across region : sa-east-1 is 0
EKS Clusters across region : sa-east-1 is 0
VPC Peering in the region : sa-east-1 is 0
Elastic Cache Clusters in the region : sa-east-1 is 0
RDS Clusters in the region : sa-east-1 is 0
Elastic IP in the region : sa-east-1 is 0
Security Groups in the region : sa-east-1 is 1
Route table in the region : sa-east-1 is 1
Network ACL in the region : sa-east-1 is 1


Assets in the Region: ap-southeast-1


Ec2 instances in Region: ap-southeast-1 is 0
Elastic Block Storage in Region: ap-southeast-1 is 0
VPC in Region: ap-southeast-1 is 1
RDS in Region: ap-southeast-1 is 0
Lambda Functions in Region: ap-southeast-1 is 0
Ec2 Network Interfaces in Region: ap-southeast-1 is 0
Subnets in the Region: ap-southeast-1 is 3
Network Load Balancers in Region: ap-southeast-1 is 0
KMS Key in the region: ap-southeast-1 is 0
ECS Clusters across region : ap-southeast-1 is 0
EKS Clusters across region : ap-southeast-1 is 0
VPC Peering in the region : ap-southeast-1 is 0
Elastic Cache Clusters in the region : ap-southeast-1 is 0
RDS Clusters in the region : ap-southeast-1 is 0
Elastic IP in the region : ap-southeast-1 is 0
Security Groups in the region : ap-southeast-1 is 1
Route table in the region : ap-southeast-1 is 1
Network ACL in the region : ap-southeast-1 is 1


Assets in the Region: ap-southeast-2


Ec2 instances in Region: ap-southeast-2 is 0
Elastic Block Storage in Region: ap-southeast-2 is 0
VPC in Region: ap-southeast-2 is 1
RDS in Region: ap-southeast-2 is 0
Lambda Functions in Region: ap-southeast-2 is 0
Ec2 Network Interfaces in Region: ap-southeast-2 is 0
Subnets in the Region: ap-southeast-2 is 3
Network Load Balancers in Region: ap-southeast-2 is 0
KMS Key in the region: ap-southeast-2 is 0
ECS Clusters across region : ap-southeast-2 is 0
EKS Clusters across region : ap-southeast-2 is 0
VPC Peering in the region : ap-southeast-2 is 0
Elastic Cache Clusters in the region : ap-southeast-2 is 0
RDS Clusters in the region : ap-southeast-2 is 0
Elastic IP in the region : ap-southeast-2 is 0
Security Groups in the region : ap-southeast-2 is 1
Route table in the region : ap-southeast-2 is 1
Network ACL in the region : ap-southeast-2 is 1


Assets in the Region: eu-central-1


Ec2 instances in Region: eu-central-1 is 0
Elastic Block Storage in Region: eu-central-1 is 0
VPC in Region: eu-central-1 is 1
RDS in Region: eu-central-1 is 0
Lambda Functions in Region: eu-central-1 is 0
Ec2 Network Interfaces in Region: eu-central-1 is 0
Subnets in the Region: eu-central-1 is 3
Network Load Balancers in Region: eu-central-1 is 0
KMS Key in the region: eu-central-1 is 2
ECS Clusters across region : eu-central-1 is 0
EKS Clusters across region : eu-central-1 is 0
VPC Peering in the region : eu-central-1 is 0
Elastic Cache Clusters in the region : eu-central-1 is 0
RDS Clusters in the region : eu-central-1 is 0
Elastic IP in the region : eu-central-1 is 0
Security Groups in the region : eu-central-1 is 1
Route table in the region : eu-central-1 is 1
Network ACL in the region : eu-central-1 is 1


Assets in the Region: us-east-1


Ec2 instances in Region: us-east-1 is 0
Elastic Block Storage in Region: us-east-1 is 0
VPC in Region: us-east-1 is 1
RDS in Region: us-east-1 is 0
Lambda Functions in Region: us-east-1 is 0
Ec2 Network Interfaces in Region: us-east-1 is 0
Subnets in the Region: us-east-1 is 6
Network Load Balancers in Region: us-east-1 is 0
KMS Key in the region: us-east-1 is 3
ECS Clusters across region : us-east-1 is 0
EKS Clusters across region : us-east-1 is 0
VPC Peering in the region : us-east-1 is 0
Elastic Cache Clusters in the region : us-east-1 is 0
RDS Clusters in the region : us-east-1 is 0
Elastic IP in the region : us-east-1 is 0
Security Groups in the region : us-east-1 is 4
Route table in the region : us-east-1 is 1
Network ACL in the region : us-east-1 is 1
Assets in the Region: us-east-2
Ec2 instances in Region: us-east-2 is 27
Elastic Block Storage in Region: us-east-2 is 77
VPC in Region: us-east-2 is 3
RDS in Region: us-east-2 is 1
Lambda Functions in Region: us-east-2 is 0
Ec2 Network Interfaces in Region: us-east-2 is 111
Subnets in the Region: us-east-2 is 21
Network Load Balancers in Region: us-east-2 is 2
KMS Key in the region: us-east-2 is 18
ECS Clusters across region : us-east-2 is 0
EKS Clusters across region : us-east-2 is 2
VPC Peering in the region : us-east-2 is 0
Elastic Cache Clusters in the region : us-east-2 is 1
RDS Clusters in the region : us-east-2 is 1
Elastic IP in the region : us-east-2 is 4
Security Groups in the region : us-east-2 is 73
Route table in the region : us-east-2 is 5
Network ACL in the region : us-east-2 is 3


Assets in the Region: us-west-1


Ec2 instances in Region: us-west-1 is 0
Elastic Block Storage in Region: us-west-1 is 0
VPC in Region: us-west-1 is 1
RDS in Region: us-west-1 is 0
Lambda Functions in Region: us-west-1 is 0
Ec2 Network Interfaces in Region: us-west-1 is 0
Subnets in the Region: us-west-1 is 2
Network Load Balancers in Region: us-west-1 is 0
KMS Key in the region: us-west-1 is 7
ECS Clusters across region : us-west-1 is 0
EKS Clusters across region : us-west-1 is 0
VPC Peering in the region : us-west-1 is 0
Elastic Cache Clusters in the region : us-west-1 is 0
RDS Clusters in the region : us-west-1 is 0
Elastic IP in the region : us-west-1 is 0
Security Groups in the region : us-west-1 is 1
Route table in the region : us-west-1 is 1
Network ACL in the region : us-west-1 is 1
Assets in the Region: us-west-2
Ec2 instances in Region: us-west-2 is 5
Elastic Block Storage in Region: us-west-2 is 50
VPC in Region: us-west-2 is 4
RDS in Region: us-west-2 is 0
Lambda Functions in Region: us-west-2 is 0
Ec2 Network Interfaces in Region: us-west-2 is 34
Subnets in the Region: us-west-2 is 19
Network Load Balancers in Region: us-west-2 is 1
KMS Key in the region: us-west-2 is 14
ECS Clusters across region : us-west-2 is 0
EKS Clusters across region : us-west-2 is 1
VPC Peering in the region : us-west-2 is 0
Elastic Cache Clusters in the region : us-west-2 is 0
RDS Clusters in the region : us-west-2 is 0
Elastic IP in the region : us-west-2 is 2
Security Groups in the region : us-west-2 is 23
Route table in the region : us-west-2 is 10
Network ACL in the region : us-west-2 is 4


s3 buckets in the account is 285


IAM users in the account is 362


IAM Groups in the account is 11


IAM Roles in the account is 133


Total Assets in this AWS account is : 1653
```