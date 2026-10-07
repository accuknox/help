For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/authentication/credentials-store/aws-credentials.md).

Prisma Cloud lets you authenticate with AWS using the following credentials.

- IAM users using access keys.

- IAM roles.

- Security Token Service (STS): Recommended when using IAM users.


## AWS IAM users[Direct link to heading](https://docs.prismacloud.io/admin-guide/authentication/credentials-store/aws-credentials\#aws-iam-users)

In AWS, an IAM user is an identity that represents a person or service. You create IAM users to allow that person or service to interact with AWS.

Access keys are long-term credentials for IAM users. Access keys consist of two parts: an access key ID and a secret access key. IAM users must use both the access key ID and secret access key together to authenticate requests with AWS.

The Prisma Cloud credentials store can save the access keys of your IAM users. To create a new credential in the store complete these steps. . Select the **AWS** type and **Access Key** subtype. . Enter the access key ID and the secret access key.

![credentials store aws access key](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-0b107ba0bf8dda8e4f18cb8cc461ec7a801f572c%252Fcredentials_store_aws_access_key.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=5766f14b2c950f89b51a6b4b251e4d57&sv=3)

The AWS best practice is to rotate your keys every 90 days. Prisma Cloud raises an alert if the added credentials are over 90 days old. If you use IAM users, rotate your keys at least every 90 days.

## AWS IAM roles[Direct link to heading](https://docs.prismacloud.io/admin-guide/authentication/credentials-store/aws-credentials\#aws-iam-roles)

If you need to use temporary security credentials, you should use IAM roles instead of IAM users.

IAM roles and IAM users are identities associated to permission policies. A permission policy determines what an identity can and cannot do in AWS. IAM roles don’t use access keys as credentials and are not unique to a person or service. Any IAM user can assume a role when needed to temporarily acquire the permissions to carry out a specific task.

IAM roles solve the problem of how to securely manage and distribute credentials. For example, how do you distribute credentials to new EC2 instances created by an auto scaling group? How do you rotate credentials on EC2 instances in a cluster? Instead of creating and distributing credentials, you can delegate permission to call the AWS API as follows:

1. Create an IAM role.

2. Specify the AWS service (e.g. EC2) that can assume the role.

3. Specify the API actions and resources Prisma Cloud can use after assuming the role.

4. Specify the role when you launch the service.

5. Prisma Cloud retrieves a set of temporary credentials and uses them as needed.


Prisma Cloud ships with a default credential called **IAM Role**. Assuming you’ve created an IAM role in AWS, configured trust (who can use the role), permission policy (what the role can do), and launched the service with the role, Prisma Cloud can acquire the temporary credentials it needs to carry out its work. Each feature in Prisma Cloud has documentation which describes permission policy it requires.

![credentials store default iam role](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-10e42901b4ff06f58bcdde2b9ec48455fa244c52%252Fcredentials_store_default_iam_role.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=dcbefc65499c585a96fc13c30dc93d51&sv=3)

### How Prisma Cloud accesses IAM role credentials[Direct link to heading](https://docs.prismacloud.io/admin-guide/authentication/credentials-store/aws-credentials\#how-prisma-cloud-accesses-iam-role-credentials)

Roles provide a way to grant credentials to applications that run on EC2 instances to access other AWS services, such as ECR. IAM dynamically provides temporary credentials to the EC2 instances, and these credentials are automatically rotated for you.

This section shows how Prisma Cloud Defender gets credentials to scan the ECR registry when its running on an EC2 instance with a correctly configured IAM role. The mechanism is similar for other services where Prisma Cloud might run.

When you create an EC2 instance, you can assign it a role. When the instance is started, the AWS instance metadata service (IMDS) attaches your credentials to the running EC2 instance. You can access this metadata from within the instance using the following command:

AskCopy

```
curl http://169.254.169.254/latest/meta-data/iam/security-credentials/<POLICY_NAME>
{
"Code" : "Success",
"LastUpdated" : "2017-06-29T06:12:29Z",
"Type" : "AWS-HMAC",
"AccessKeyId" : "ASIA...",
"SecretAccessKey" : "3VI...",
"Token" : "dzE...",
"Expiration" : "2017-06-29T12:16:54Z"
}
```

Where `<POLICY_NAME>` is assigned to the EC2 instance when it is created or at some point during its life.

The following diagram shows all the pieces. Defender retrieves the credentials from the metadata service, then uses those credentials to retrieve and scan the container images in ECR.

![credentials store scan ecr iam role](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-a388c25cbff25e928828772d7adeb35b57a01f17%252Fcredentials_store_scan_ecr_iam_role.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=060a793b4575e4a7b416dc11623750f0&sv=3)

## AWS Security Token Service (STS)[Direct link to heading](https://docs.prismacloud.io/admin-guide/authentication/credentials-store/aws-credentials\#aws-security-token-service-sts)

AWS Security Token Service (STS) lets you request temporary, limited-privilege credentials for AWS IAM users or users that you authenticate (federated users).

Per the AWS Well-Architected Framework, this method is a recommended best practice when using IAM users. With STS, you don’t have to distribute long-term AWS credentials (access keys) to places like the Prisma Cloud credentials store. Also, the temporary credentials have a limited life span, so you don’t have to rotate or revoke them when they’re no longer needed.

When you configure integration with an AWS resource, you can pick an AWS credential from the central store, then use STS to change the role of the account. AWS STS lets you have a few number of IAM identities that can be used across many AWS accounts. For example, if you were setting up Prisma Cloud to scan an AWS ECR registry, you would select the AWS credentials from the central store. Then you would enable **Use AWS STS**, and enter the name of the STS role to assume in the target account.

When using AWS STS, ensure the following:

- The policy of the IAM user you use as credentials has **sts:AssumeRole** permission on the IAM role you’re going to assume. Sample policy:

















AskCopy



```
{
      "Version": "2012-10-17",
      "Statement": [\
          {\
              "Effect": "Allow",\
              "Action": "sts:AssumeRole",\
              "Resource": "arn:aws:iam::123456789123:role/stsIAMrole"\
          }\
      ]
}
```

- The IAM role you’re going to assume has the IAM user mentioned above configured as a trusted entity. Sample trusted entity policy:

















AskCopy



```
{
    "Version": "2012-10-17",
    "Statement": [\
      {\
        "Effect": "Allow",\
        "Principal": {\
          "AWS": "arn:aws:iam::123456789123:user/prismaUser"\
        },\
        "Action": "sts:AssumeRole"\
      }\
    ]
}
```


The following diagram shows the relationship between an IAM user, a permissions policy, and an assumed role. By default, the IAM user has no permissions. The permissions policy allows ready-only access to the ECR registry. The role brings everything together. It specifies the trust relationship (who is allowed to assume the role, also known as the principal), it grants to ability for the principal to assume roles (sts:AssumeRole), and it declares what the role can do when it assumed by a principal (permission policy).

![credentials store aws sts relationships](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-c43de6a20c14d93222879ba65a9b9e10950dc41d%252Fcredentials_store_aws_sts_relationships.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=165d87d341510cec9e5d3c479289bbb1&sv=3)

[PreviousCredentials Store](https://docs.prismacloud.io/admin-guide/authentication/credentials-store) [NextAzure Credentials](https://docs.prismacloud.io/admin-guide/authentication/credentials-store/azure-credentials)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
