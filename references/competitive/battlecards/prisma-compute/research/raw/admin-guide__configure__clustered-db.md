For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/configure/clustered-db.md).

Running Prisma Cloud Compute in the clustered-DB configuration lets you sync Console’s database across multiple instances of Console. When using the clustered-DB deployment, all Consoles must be accessible with the same DNS name and connected to the same load balancer.

The Consoles in a clustered-DB pool can be deployed in the same region across different availability zones.

A new Prisma Cloud Compute self-hosted setup is required to create a clustered-DB deployment. That is, all Consoles must be new. Accordingly, all Defenders must be new as well.

## Recommendations for your clustered-DB setup[Direct link to heading](https://docs.prismacloud.io/admin-guide/configure/clustered-db\#recommendations-for-your-clustered-db-setup)

The information in the following sections help you make informed decisions when selecting pool size, load balancer configuration, and storage types.

### Number Of Consoles in the clustered-DB pool[Direct link to heading](https://docs.prismacloud.io/admin-guide/configure/clustered-db\#number-of-consoles-in-the-clustered-db-pool)

The clustered-DB mechanism continuously requires the pool to choose a primary Console. This is done by the replica sets election mechanism. The election determines which member will become primary. Replica sets can trigger an election in response to a variety of events, such as: adding a new member, initiating a pool, and losing connectivity to the primary for more than the configured timeout.

An odd number of Consoles is recommended for better fault tolerance. The table below describes the fault tolerance for 3/5/7 Consoles:

Number of Members

Majority Required to Elect a New Primary

Fault Tolerance

3

2

1

4

3

1

5

3

2

6

4

2

7

4

3

### Load balancer configuration[Direct link to heading](https://docs.prismacloud.io/admin-guide/configure/clustered-db\#load-balancer-configuration)

When configuring your load balancer, make sure to set up the following:

- TCP (Network) load balancer.

- TLS health through.

- Except for traffic on the used ports (8083, 8084 the default).

- To ensure LB can identify unavailable Consoles, we recommended that you set a health check to the Console ping API: https://<ip:port>/api/v1/\_ping.


### Performance implications[Direct link to heading](https://docs.prismacloud.io/admin-guide/configure/clustered-db\#performance-implications)

When deploying a clustered-DB setup on AWS, we recommend that you use [EBS-optimized instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-optimized.html).

## Custom certificates[Direct link to heading](https://docs.prismacloud.io/admin-guide/configure/clustered-db\#custom-certificates)

You can provide a custom certificate to the clustered-DB Consoles pool. When configuring custom certificates, make sure that all Consoles and Defenders know all clustered-DB Consoles and the load balancer. To do so, add all Console addresses and load balancer names to the certificate’s SAN.

All Consoles and Defenders must be signed with the same CA.

This is also relevant for [configuring custom certs from a predefined directory](https://docs.prismacloud.io/admin-guide/configure/custom-certs-predefined-dir).

## Guidelines[Direct link to heading](https://docs.prismacloud.io/admin-guide/configure/clustered-db\#guidelines)

Before you begin, make sure to follow these guidelines:

- Managing and monitoring a clustered-DB setup requires System Admin permissions.

- When using IAM roles, all Console nodes must be assigned with the same role.

- The clustered-DB pool should be created with fresh Consoles and Defenders.

- All Consoles should run the same **major and minor version**.

- All Consoles should be able to communicate with each other on port 27017.

- The number of the total Consoles in the pool should be between 3 to 7. See [Number Of Consoles in the clustered-DB pool](https://docs.prismacloud.io/admin-guide/configure/clustered-db#pool-size).

- Create a load balancer using the instructions described in [Load balancer configuration](https://docs.prismacloud.io/admin-guide/configure/clustered-db#lb) This load balancer will be used for Defenders, twistcli, API and TLS communication with the clustered-DB pool.


## Creating the clustered-DB pool[Direct link to heading](https://docs.prismacloud.io/admin-guide/configure/clustered-db\#creating-the-clustered-db-pool)

1. Deploy the clustered-DB pool’s Consoles without initializing them with usernames and passwords.









1. Option 1 - Deploy Console using YAML/Helm charts.

















      AskCopy



      ```
      ./twistcli console export kubernetes <optional parameters> --clustered-db

      kubectl create -f twistlock_console.yaml
      ```









      When deploying Consoles on the same cluster, you can use a statefulset deployment or use different namespaces for the Console installation. Make sure to change the YAML/Helm accordingly.

2. Option 2 - Deploy the Console as a single Console.









      1. Add `CLUSTERED_DB_ENABLED=true` configuration to the `twistlock.cfg` file

      2. Install the Console (not the onebox installation), without initializing it.











         For example `sudo ./twistlock.sh console`


2. Configure the load balancer to send traffic to the Console services.

3. Choose one of the Consoles and initialize it with a user, password, and license.











When initializing the Console, access it directly, rather than through the load balancer.











This first Console is considered the seed Console.

4. Check the clustered-DB status against the initialized Console:

















AskCopy



```
./twistcli clustered-db status --address https://<console address>:8083/ --password <password>
```









You should expect to see the following result:

















AskCopy



```
Clustered DB status:
Last updated: 28 Mar 22 18:00 UTC
Load balancer address:
Members:
1. Address: <console name>, State: PRIMARY
```

5. Add a load balancer to the clustered-DB.











The Console’s address should be static and available for the other Consoles. You can choose a static IP address or a DNS name.











Run the following command to set up the clustered-DB load balancer address. The <console address> should be the initialized Console address:

















AskCopy



```
./twistcli clustered-db configure --load-balancer-address <load-balancer-address> --address https://<console address>:8083/ --password <password>
```

6. (Optional) Edit the seed address.











This command can be useful if the initialized Console address is not accessible for the other Consoles that you are about to add to the pool. Note you can use this command after adding the first Console to the pool (the seed Console), meaning that this command can’t be executed after adding the other Consoles to the pool.

















AskCopy



```
./twistcli clustered-db configure --seed-console-address <service-name/service-name.namespace/host name/IP address> --password <password>
```

7. Add the other Consoles to the pool.











The Consoles’ addresses should be static and available for the other Consoles. You can choose a static IP address or a DNS name.











Run the following command in order to add members to the clustered-DB pool. You can add single or multiple addresses at once:

















AskCopy



```
./twistcli clustered-db add --member-address <member adderss> --member-address <member adderss> … --address https://<console address>:8083/ --password <password>
```

8. Check status the pool status:











Now it’s possible to check the pool status against the load balancer address:

















AskCopy



```
./twistcli clustered-db status --address https://<load balancer address>:8083/ --password <password>
```









Expected output:

















AskCopy



```
Clustered DB status:
Last updated: 28 Mar 22 18:25 UTC
Load balancer address: load_balancer_address
Members:
1. Address: Console1_address, State: PRIMARY
2. Address: Console2_address, State: SECONDARY
3. Address: Console3_address, State: SECONDARY
```

## Clustered-DB potential statuses[Direct link to heading](https://docs.prismacloud.io/admin-guide/configure/clustered-db\#clustered-db-potential-statuses)

The clustered-DB status call restrains the status of the entire pool and the status for each one of the members. Status is a string representation of the member’s state, from the cluster perspective. The last updated field represents the time when the status was last updated.

AskCopy

```
./twistcli clustered-db status --address https://<load balancer address>:8083/ --password <password>
```

See the available statuses in the list below:

Name

State Description

STARTUP

Not yet an active member of any set. All members start up in this state.

PRIMARY

The member in state primary the primary member of the pool. Eligible to vote.

SECONDARY

A member in state secondary is replicating the data store. Eligible to vote.

RECOVERING

Members either perform startup self-checks, or transition from completing a rollback or resync. Eligible to vote.

STARTUP2

The member has joined the set and is running an initial sync. Eligible to vote. NOTE this member is not eligible to vote and cannot be elected during the initial sync process.

UNKNOWN

The member’s state, as seen from another member of the set, is not yet known.

DOWN

The member, as seen from another member of the set, is unreachable.

ROLLBACK

This member is actively performing a rollback. Eligible to vote. The member is not accessible during the rollback time frame.

REMOVED

This member was once in a replica set but was subsequently removed. This status can be available for a very short period of time after removing a member. When the remove action is complete, the member will no longer appear in the status.

## Remove members[Direct link to heading](https://docs.prismacloud.io/admin-guide/configure/clustered-db\#remove-members)

Follow the steps below to remove a member (Console) from the pool. Note that after removing a member, this Console cannot be reused.

1. Remove the member from the LB settings.

2. Remove a member from the pool using the following command:

















AskCopy



```
./twistcli clustered-db remove --address https://<load balancer address> -u user -p password --member-address <member-address-to-remove>
```

3. Delete the removed Console instance, since it’s not reusable.











After removing a member from the pool, the deleted Console will remain in the existing DB. This Console can’t be added to the pool again since it’s already initialized. You won’t be able to return the same member to the pool, unless you delete the Console and create a new non-initialized one.


## Console disconnection[Direct link to heading](https://docs.prismacloud.io/admin-guide/configure/clustered-db\#console-disconnection)

If Console fails, the clustered-DB pool will choose a new primary Console. The primary selections might cause a short downtime to make the transition. The downtime period depends on different factors (sufficient number of members to vote, network latency, etc). Typically the process will take about 30 seconds.

If a single member is disconnected from the pool for a long period of time, it might take a while for it to return. This is due to possible DB differences. If the delta between the disconnected member and the pool DB is significant, the member DB will be restored from the current pool DB.

## Upgrade clustered-DB Consoles[Direct link to heading](https://docs.prismacloud.io/admin-guide/configure/clustered-db\#upgrade-clustered-db-consoles)

All Consoles should run the same **major and minor version** (i.e., exactly the same x.y.z version). All clustered-DB Consoles should be upgraded within a reasonable amount of time, to make sure that all of them will run with the same version shortly. For example, if the DB was upgraded to x.y.z+1, members still running the previous version x.y.z won’t be able to become primary. They just replicate the DB.

## Limitations[Direct link to heading](https://docs.prismacloud.io/admin-guide/configure/clustered-db\#limitations)

The clustered-DB setup has the following limitations:

- You cannot deploy [projects](https://docs.prismacloud.io/admin-guide/deployment-patterns/projects) when using clustered-DB.

- Consoles running on Fargate aren’t supported.

- Backup and restore: clustered-DB can track only periodic backups only (daily, weekly, monthly), but not on demand. The backup is taken from all of the clustered-DB pool members.


[PreviousLog scrubbing](https://docs.prismacloud.io/admin-guide/configure/log-scrubbing) [NextPermissions](https://docs.prismacloud.io/admin-guide/configure/permissions)

Last updated 3 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
