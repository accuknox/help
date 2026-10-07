For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/how-to-guides/configure-ecs-loadbalancer.md).

Configure an AWS Classic Load Balancer for accessing Prisma Cloud Console. Console serves its UI and API over HTTPS on port 8083, and Defender communicates with Console over a websocket on port 8084. You’ll set up a single load balancer to forward requests for both port 8083 and 8084 to Console, with the load balancer checking Console’s health using the _/api/v1/\_ping_ endpoint on port 8083.

For the complete install procedure for Prisma Cloud on Amazon ECS, see [here](https://docs.twistlock.com/docs/latest/install/install_amazon_ecs.html).

1. Log into the AWS Management Console.

2. Go to **Services > Compute > EC2**.

3. In the left menu, go to **Load Balancing > Load Balancers**.

4. Create a load balancer.









01. Click **Create Load Balancer**.

02. In **Classic Load Balancer**, click **Create**.

03. Give your load balancer a name, such as **pc-ecs-lb**.

04. Leave default **VPC**.

05. Create the following listener configuration:









       - **Load Balancer Protocol**: TCP

       - **Load Balancer Port**: 8083

       - **Instance Protocol**: TCP

       - **Instance Port**: 8083


06. Click **Add** to add another listener using following listener configuration:









       - **Load Balancer Protocol**: TCP

       - **Load Balancer Port**: 8084

       - **Instance Protocol**: TCP

       - **Instance Port**: 8084


07. Click **Next: Assign Security Groups**.









       - Select the **pc-security-group**


08. Click **Next Configure Security Settings**.









       - Ignore the warning and click **Next: Configure Health Check**


09. Use the following health check configuration:









       - **Ping Protocol**: HTTPS

       - **Ping Port**: 8083

       - **Ping Path**: /api/v1/\_ping

       - For **Advanced Details**, accept the default settings.


10. Click **Next: Add EC2 Instances**









       - Do not select any instances.


11. Click **Next: Add Tags**.









       - Under **Key**, enter **Name**.

       - Under **Value**, enter **pc-ecs-lb**.


12. Click **Review and Create**.

13. Review your settings and select **Create**.

14. Review the load balancer that was created and record its **DNS Name**.


[PreviousHow-To Guides](https://docs.prismacloud.io/admin-guide/how-to-guides/howto) [NextConfigure Console's listening ports](https://docs.prismacloud.io/admin-guide/how-to-guides/configure-listening-ports)

Last updated 3 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
