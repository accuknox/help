For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/install/deploy-defender/serverless.md).

Serverless Defender protects serverless functions at runtime. It monitors your functions to ensure they execute as designed.

Per-function policies let you control:

- Process activity. Enables verification of launched subprocesses against policy.

- Network connections. Enables verification of inbound and outbound connections, and permits outbound connections to explicitly allowed domains.

- File system activity. Controls which parts of the file system functions can access.


Prisma Cloud supports AWS Lambda functions (Linux) and Azure Functions (Windows only).

See [system requirements](https://docs.prismacloud.io/admin-guide/install/system-requirements#serverless-runtimes) for the runtimes and architectures that are supported for Serverless Defenders.

Serverless Defenders are not supported on ARM64 architecture.

Only users with the Administrator role can see the list of deployed Serverless Defenders in **Manage > Defenders > Manage**.

## Securing serverless functions[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/serverless\#securing-serverless-functions)

To secure a serverless function, embed the Prisma Cloud Serverless Defender into it. The steps are:

1. (Optional) If you are not using a deployment framework like SAM or Serverless Framework, download a ZIP file that contains your function source code and dependencies.

2. Embed the Serverless Defender into the function.

3. Deploy the new function or upload the updated ZIP file to the cloud provider.

4. Define a serverless protection runtime policy.

5. Define a serverless WAAS policy.


## AWS Lambda - (Optional) Download your function as a ZIP file[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/serverless\#aws-lambda-optional-download-your-function-as-a-zip-file)

Download your function’s source code from AWS as a ZIP file.

1. From Lambda’s code editor, click **Actions > Export function**.

2. Click **Download deployment package**.











Your function is downloaded to your host as a ZIP file.

3. Create a working directory, and unpack the ZIP file there.











In the next step, you’ll download the Serverless Defender files to this working directory.


## AWS Lambda - Embed Serverless Defender into C\# functions[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/serverless\#aws-lambda-embed-serverless-defender-into-c-functions)

In your function code, import the Serverless Defender library and create a new protected handler that wraps the original handler. The protected handler will be called by AWS when your function is invoked. Update the project configuration file to add Prisma Cloud dependencies and package references.

Prisma Cloud supports .NET Core 3.1, 6.0.

01. Open Compute Console, and go to **Manage > Defenders > Defenders: Deployed > Manual deploy > Single Defender**.

02. In **Choose Defender type**, select **Serverless Defender - AWS**.

03. In **Runtime**, select **C#**.

04. Download the Serverless Defender package to your workstation.

05. Unzip the Serverless Defender bundle into your working directory.

06. Embed the serverless Defender into the function by importing the Prisma Cloud library and wrapping the function’s handler.











    Function input and output can be a struct or a stream. Functions can be synchronous or asynchronous. The context parameter is optional in .NET, so it can be omitted.

















    AskCopy



    ```
      using Twistlock;

      public class ... {
          // Original handler
          public ApplicationLoadBalancerResponse Handler(ApplicationLoadBalancerRequest request, ILambdaContext context)
          {
            ...
          }

          // Application load balancer example
          // Twistlock protected handler
          public ApplicationLoadBalancerResponse ProtectedHandler(ApplicationLoadBalancerRequest request, ILambdaContext context)
          {
              return Twistlock.Serverless.Handler<ApplicationLoadBalancerRequest, ApplicationLoadBalancerResponse>(Handler, request, context);
          }
          ...
      }
    ```

07. Add the Twistlock package as a dependency in your nuget.config file.











    If a nuget.config file doesn’t exist, create one.

















    AskCopy



    ```
    <configuration>
      <packageSources>
        <add key="local-packages" value="./twistlock"/>
      </packageSources>
    </configuration>
    ```

08. Reference the Twistlock package in your csproj file.

















    AskCopy



    ```
    <Project>
      <ItemGroup>
        <PackageReference Include="Twistlock" Version="19.11.462"/>
        <TwistlockFiles Include="twistlock/*" Exclude="twistlock/twistlock.19.11.462.nupkg"/>
      </ItemGroup>
      <Target Name="CopyCustomContentOnPublish" AfterTargets="Publish">
        <Copy SourceFiles="@(TwistlockFiles)" DestinationFolder="$(PublishDir)/twistlock"/>
      </Target>
      .
      .
      .
    </Project>
    ```

09. Generate the value for the TW\_POLICY environment variable by specifying your function’s name and region.











    If **Any** is selected for region, only policies that contain **\*** in the region label will be matched.











    Serverless Defender uses TW\_POLICY to determine how to connect to Compute Console to retrieve policy and send audits.











    Copy the value generated for TW\_POLICY, and set it aside.

10. [Upload the protected function to AWS, and set the TW\_POLICY environment variable.](https://docs.prismacloud.io/admin-guide/install/deploy-defender/serverless#upload-protected-function-to-aws)


## AWS Lambda - Embed Serverless Defender into Java functions[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/serverless\#aws-lambda-embed-serverless-defender-into-java-functions)

To embed Serverless Defender, import the Twistlock package and update your code to start Serverless Defender as soon as the function is invoked. Prisma Cloud supports both Maven and Gradle projects. You’ll also need to update your project metadata to include Serverless Defender dependencies.

Prisma Cloud supports [both predefined interfaces](https://docs.aws.amazon.com/lambda/latest/dg/java-handler-using-predefined-interfaces.html) in the AWS Lambda Java core library: RequestStreamHandler (where input must be serialized JSON) and RequestHandler.

AWS lets you specify handlers as functions or classes. In both cases, Twistlock.Handler(), the entry point to Serverless Defender, assumes the entry point to your code is named handleRequest. After embedding Serverless Defender, update the name of the handler registered with AWS to be the wrapper method that calls Twistlock.Handler() (for example, protectedHandler).

Prisma Cloud supports both service struct and stream input (serialized struct). Even though the Context parameter is optional for unprotected functions, it’s manadatory when embedding Serverless Defender.

Prisma Cloud supports Java 8 and Java 11.

01. Open Compute Console, and go to **Manage > Defenders > Defenders: Deployed > Manual Deploy > Single Defender**.

02. In **Defender type**, select **Serverless Defender - AWS**.

03. Select the name that Defender will use to connect to this Console.

04. In **Runtime**, select **Java**.

05. In **Package**, select **Maven** or **Gradle**.











    The steps for embedding Serverless Defender differ depending on the build tool.

06. Download the Serverless Defender package to your workstation.

07. Unzip the Serverless Defender bundle into your working directory.









    1. Enter the package details and artifact id in the `defender-<version>.pom` file:

















       AskCopy



       ```
       <project>
         <modelVersion>4.0.0</modelVersion>
         <groupId>com.twistlock.serverless</groupId>
         <artifactId>defender</artifactId>
         <version>22.11.386</version>
         <description>twistlock serverless defender pom</description>
       </project>
       ```


08. Embed Serverless Defender into your function by importing the Prisma Cloud package and wrapping the function’s handler.

















    AskCopy



    ```
    import com.twistlock.serverless.Twistlock;

    public class ... implements RequestHandler<APIGatewayProxyRequestEvent, APIGatewayProxyResponseEvent> {

      // Original handler
      @Override
      public APIGatewayProxyResponseEvent handleRequest(APIGatewayProxyRequestEvent request, Context context) {
      {
        ...
      }

      // RequestHandler example
      // Twistlock protected handler
      public APIGatewayProxyResponseEvent protectedHandler(APIGatewayProxyRequestEvent request, Context context) {
        return Twistlock.Handler(this, request, context);
      }
      ...
    }
    }
    ...
    ```

09. Update your project configuration file.









    1. **Maven**











       Update your `*pom` xml file. Don’t create new sections for the Prisma Cloud configurations. Just update existing sections. For example, don’t create a new <plugins> section if one exists already. Just append a <plugin> section to it.











       Add the assembly plugin to include the Twistlock package in the final function JAR. Usually the shade plugin is used in AWS to include packages to standalone JARs, but it doesn’t let you include local system packages.

















       AskCopy



       ```
       <project>
         <build>
           <!-- Add assembly plugin to create a standalone jar that contains Twistlock library -->
           <plugins>
             <plugin>
               <artifactId>maven-assembly-plugin</artifactId>
               <configuration>
                 <appendAssemblyId>false</appendAssemblyId>
                 <descriptors>
                   <descriptor>assembly.xml</descriptor>
                 </descriptors>
               </configuration>
               <executions>
                 <execution>
                  <id>make-assembly</id>
                  <phase>package</phase>
                  <goals>
                   <goal>attached</goal>
                  </goals>
                 </execution>
               </executions>
             </plugin>
             ...
           </plugins>

         <!-- Add Twistlock resources -->
         <resources>
           <resource>
             <directory>${project.basedir}</directory>
             <includes>
               <include>twistlock/*</include>
               </includes>
             <excludes>
               <exclude>twistlock/com/**</exclude>
             </excludes>
           </resource>
           ...
         </resources>
         ...
       </build>

       <!-- Define the internal (local) repository in the `*pom` xml file: -->
       <project>
         <repositories>
           <repository>
             <id>twistlock-internal</id>
             <name>twistlock</name>
             <url>file://${project.basedir}/twistlock</url>
           </repository>
        ...
       </project>

         <!-- Add Twistlock package reference -->
         <dependencies>
           <dependency>
             <groupId>com.twistlock.serverless</groupId>
             <artifactId>defender</artifactId>
             <version>22.11.386</version>
           </dependency>
           ...
         </dependencies>
         ...
       </project>
       ```

    2. Create an `assembly.xml` file, which packs all dependencies in a standalone JAR.

















       AskCopy



       ```
       <assembly>
         <id>twistlock-protected</id>
         <formats>
           <format>jar</format>
         </formats>
         <includeBaseDirectory>false</includeBaseDirectory>
         <dependencySets>
           <!-- Unpack runtime dependencies into runtime jar -->
           <dependencySet>
             <unpack>true</unpack>
             <scope>runtime</scope>
           </dependencySet>
           <!-- Unpack local system dependencies into runtime jar -->
           <dependencySet>
             <unpack>true</unpack>
             <scope>system</scope>
           </dependencySet>
         </dependencySets>
       </assembly>
       ```


10. **Gradle**











    Gradle supports Maven repositories and can fetch artifacts directly from any kind of Maven repository.











    Update your `build.gradle` file.









    1. Add the Maven repository for this project.

    2. Set the `*.jar` file as an "implementation" dependency from the filesystem.

    3. Update the zip resources.

















       AskCopy



       ```
       repositories {
           maven {
               url "file://$projectDir/twistlock"
           }
       }

       dependencies {
           implementation 'com.twistlock.serverless:defender:22.11.386'
       }

       task buildZip(type: Zip) {
           from compileJava
           from processResources
           into('lib') {
               from configurations.runtimeClasspath
           }
           // Include Twistlock resources
           into ('twistlock') {
               from 'twistlock'
               exclude "com/**"
           }
       }

       build.dependsOn buildZip
       ```


11. In AWS, set the name of the Lambda handler for your function to protectedHandler.

12. Generate the value for the TW\_POLICY environment variable by specifying your function’s name and region.











    If **Any** is selected for region, only policies that contain **\*** in the region label will be matched.











    Serverless Defender uses TW\_POLICY to determine how to connect to Compute Console to retrieve policy and send audits.











    Copy the value generated for TW\_POLICY, and set it aside.

13. [Upload the protected function to AWS, and set the TW\_POLICY environment variable.](https://docs.prismacloud.io/admin-guide/install/deploy-defender/serverless#upload-protected-function-to-aws)


## AWS Lambda - Embed Serverless Defender into Node.js functions[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/serverless\#aws-lambda-embed-serverless-defender-into-node.js-functions)

Import the Serverless Defender module, and configure your function to start it. Prisma Cloud supports Node.js 14.x.

1. Open Compute Console, and go to **Manage > Defenders > Defenders: Deployed > Manual deploy > Single Defender**.

2. In **Choose Defender type**, select **Serverless**.

3. In **Runtime**, select **Node.js**.

4. Download the Serverless Defender package to your workstation.

5. Unzip the Serverless Defender bundle into your working directory.

6. Embed the serverless Defender into the function by importing the Prisma Cloud library and wrapping the function’s handler.









1. For asynchronous handlers:

















      AskCopy



      ```
      // Async handler
      var twistlock = require('./twistlock');
      exports.handler = async (event, context) => {
      .
      .
      .
      };
      exports.handler = twistlock.asyncHandler(exports.handler);
      ```

2. For synchronous handlers:

















      AskCopy



      ```
      // Non-async handler
      var twistlock = require('./twistlock');
      exports.handler = (event, context, callback) => {
      .
      .
      .
      };
      exports.handler = twistlock.handler(exports.handler);
      ```


7. Generate the value for the TW\_POLICY environment variable by specifying your function’s name and region.











If **Any** is selected for region, only policies that contain **\*** in the region label will be matched.











Serverless Defender uses TW\_POLICY to determine how to connect to Compute Console to retrieve policy and send audits.











Copy the value generated for TW\_POLICY, and set it aside.

8. [Upload the protected function to AWS, and set the TW\_POLICY environment variable.](https://docs.prismacloud.io/admin-guide/install/deploy-defender/serverless#upload-protected-function-to-aws)









   - Prisma Cloud Serverless Defender includes native node.js libraries. If you are using webpack, please refer to tools such as [native-addon-loader](https://www.npmjs.com/package/native-addon-loader) to make sure these libraries are included in the function ZIP file.


## AWS Lambda - Embed Serverless Defender into Python functions[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/serverless\#aws-lambda-embed-serverless-defender-into-python-functions)

Import the Serverless Defender module, and configure your function to invoke it. Prisma Cloud supports Python 3.6, 3.7, and 3.8.

1. Open Compute Console, and go to **Manage > Defenders > Defenders: Deployed > Manual deploy > Single Defender**.

2. In **Choose Defender type**, select **Serverless**.

3. In **Runtime**, select **Python**.

4. Download the Serverless Defender package to your workstation.

5. Unzip the Serverless Defender bundle into your working directory.

6. Embed the serverless Defender into the function by importing the Prisma Cloud library and wrapping the function’s handler.

















AskCopy



```
import twistlock.serverless
@twistlock.serverless.handler
def handler(event, context):
.
.
.
```

7. Generate the value for the TW\_POLICY environment variable by specifying your function’s name and region.











If **Any** is selected for region, only policies that contain **\*** in the region label will be matched.











Serverless Defender uses TW\_POLICY to determine how to connect to Compute Console to retrieve policy and send audits.











Copy the value generated for TW\_POLICY, and set it aside.

8. [Upload the protected function to AWS, and set the TW\_POLICY environment variable.](https://docs.prismacloud.io/admin-guide/install/deploy-defender/serverless#upload-protected-function-to-aws)


## AWS Lambda - Embed Serverless Defender into Ruby functions[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/serverless\#aws-lambda-embed-serverless-defender-into-ruby-functions)

Import the Serverless Defender module, and configure your function to invoke it. Prisma Cloud supports Ruby 2.7.

1. Open Compute Console, and go to **Manage > Defenders > Defenders: Deployed > Manual deploy > Single Defender**.

2. In **Choose Defender type**, select **Serverless**.

3. In **Runtime**, select **Ruby**.

4. Download the Serverless Defender package to your workstation.

5. Unzip the Serverless Defender bundle into your working directory.

6. Embed the serverless Defender into the function by importing the Prisma Cloud library and wrapping the function’s handler.









1. Option 1:

















      AskCopy



      ```
      require_relative './twistlock/twistlock'
      def handler(event:, context:)
          Twistlock.handler(event: event, context: context) { |event:, context:|
              # Original handler
              ...
          }
      end
      .
      .
      .
      ```

2. Option 2:

















      AskCopy



      ```
      require_relative './twistlock/twistlock'
      # Handler as a class method
      module Module1
          class Class1
              def self.original_handler(event:, context:)
                  ...
              end
              def self.protected_handler(event:, context:)
                  return Twistlock.handler(event: event, context: context, &method(:original_handler))
              end
          end
      end
      .
      .
      .
      ```


7. Generate the value for the TW\_POLICY environment variable by specifying your function’s name and region.











If **Any** is selected for region, only policies that contain **\*** in the region label will be matched.











Serverless Defender uses TW\_POLICY to determine how to connect to Compute Console to retrieve policy and send audits.











Copy the value generated for TW\_POLICY, and set it aside.

8. [Upload the protected function to AWS, and set the TW\_POLICY environment variable.](https://docs.prismacloud.io/admin-guide/install/deploy-defender/serverless#upload-protected-function-to-aws)


## AWS Lambda - Upload the protected function[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/serverless\#aws-lambda-upload-the-protected-function)

After embedding Serverless Defender into your function, upload it to AWS. If you are using a deployment framework such as SAM or Serverless Framework just deploy the function with your standard deployment procedure. If you are using AWS directly, follow the steps below:

1. Upload the new ZIP file to AWS.









1. In **Designer**, select your function so that you can view the function code.

2. Under **Code entry type**, select **Upload a .ZIP file**.

3. Specify a runtime and the handler.











      Validate that **Runtime** is a supported runtime, and that **Handler** points to the function’s entry point.

4. Click **Upload**.















      ![install serverless defender upload zip](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-bad84570378ae748505a3c564815734e67839351%252Finstall_serverless_defender_upload_zip.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=2528ba861d54c94dcc5c69bfb8d8c8eb&sv=3)

5. Click **Save**.


2. Set the TW\_POLICY environment variable.









1. In Designer, open the environment variables panel.

2. For Key, enter TW\_POLICY.

3. For Value, paste the rule you copied from Compute Console.

4. Click Save.


## Azure Functions - Embed Serverless Defender into C\# functions[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/serverless\#azure-functions-embed-serverless-defender-into-c-functions)

In your function code, import the Serverless Defender library and create a new protected handler that wraps the original handler. The protected handler will be called by Azure when your function is invoked. Update the project configuration file to add Prisma Cloud dependencies and package references.

Prisma Cloud supports .NET Core 3.1, 6.0 on Windows. 64 bit only.

01. Open Compute Console, and go to **Manage > Defenders > Defenders: Deployed > Manual deploy > Single Defender**.

02. In **Choose Defender type**, select **Serverless Defender - Azure**.

03. In **Runtime**, select **C#**.

04. Download the Serverless Defender package to your workstation.

05. Unzip the Serverless Defender bundle into your working directory.

06. Embed the serverless Defender into the function by importing the Prisma Cloud library and wrapping the function’s handler.











    Function input and output can be a struct or a stream. Functions can be synchronous or asynchronous. The context parameter is optional in .NET, so it can be omitted.

















    AskCopy



    ```
    using Twistlock;

    public class ... {
    // Original handler
    public static async Task<IActionResult> Run(
          [HttpTrigger(AuthorizationLevel.Function, "get", "post", Route = null)] HttpRequest req,
          ILogger log, ExecutionContext context)
          {
           Twistlock.Serverless.Init(log, context);
           ...
          }
    }
    ```

07. Add the Twistlock package as a dependency in your nuget.config file.











    If a nuget.config file doesn’t exist, create one.

















    AskCopy



    ```
    <configuration>
      <packageSources>
        <add key="local-packages" value="./twistlock"/>
      </packageSources>
    </configuration>
    ```

08. Reference the Twistlock package in your project configuration file.

















    AskCopy



    ```
    <Project>
      <ItemGroup>
        <PackageReference Include="Twistlock" Version="22.04.147" />
        <TwistlockFiles Include="twistlock\*" Exclude="twistlock\twistlock.22.04.147.nupkg"/>
      </ItemGroup>
      <ItemGroup>
        <None Include="@(TwistlockFiles)" CopyToOutputDirectory="Always" LinkBase="twistlock\" />
      </ItemGroup>
      ...
    </Project>
    ```

09. Generate the value for the TW\_POLICY environment variable by specifying your function’s name and region.











    If **Any** is selected for region, only policies that contain a wildcard in the region label will be matched.











    Serverless Defender uses TW\_POLICY to determine how to connect to Compute Console to retrieve policy and send audits.











    Copy the value generated for TW\_POLICY, and set it aside.

10. Upload the protected function to Azure, and set the TW\_POLICY environment variable.


## Defining your runtime protection policy[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/serverless\#defining-your-runtime-protection-policy)

By default, Prisma Cloud ships with an empty serverless runtime policy. An empty policy disables runtime defense entirely.

You can enable runtime defense by creating a rule. By default, new rules:

- Apply to all functions (`*`), but you can target them to specific functions by function name.

- Block all processes from running except the main process. This protects against command injection attacks.


When functions are invoked, they connect to Compute Console and retrieve the latest policy. To ensure that functions start executing at time=0 with your custom policy, predefine the policy. Predefined policy is embedded into your function along with the Serverless Defender by way of the `TW_POLICY` environment variable.

1. Log into Prisma Cloud Console.

2. Go to **Defend > Runtime > Serverless Policy**.

3. Click **Add rule**.

4. In the **General** tab, enter a rule name.

5. (Optional) Target the rule to specific functions.











Use collections to scope functions by name or region (label). [Pattern matching](https://docs.prismacloud.io/admin-guide/configure/rule-ordering-pattern-matching) is supported. For Azure Functions only, you can additionally scope rules by account ID.

6. Set the rule parameters in the **Processes**, **Networking**, and **File System** tabs.

7. Click **Save**.


## Defining your serverless WAAS policy[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/serverless\#defining-your-serverless-waas-policy)

Prisma Cloud lets you protect your serverless functions against application layer attacks by utilizing the serverless [Web Application and API Security (WAAS)](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/compute-edition/34/admin-guide/waas/waas.md).

By default, the serverless WAAS is disabled. To enable it, add a new serverless WAAS rule.

1. Log into Prisma Cloud Console.

2. Go to **Defend > WAAS > Serverless**.

3. Click **Add rule**.

4. In the **General** tab, enter a rule name.

5. (Optional) Target the rule to specific functions.











Use collections to scope functions by name or region (label). [Pattern matching](https://docs.prismacloud.io/admin-guide/configure/rule-ordering-pattern-matching) is supported. For Azure Functions only, you can additionally scope rules by account ID.

6. Set the protections you want to apply ( **SQLi**, **CMDi**, **Code injection**, **XSS**, **LFI**).

7. Click **Save**.


[PreviousDeploy Defender on OpenShift v4](https://docs.prismacloud.io/admin-guide/install/deploy-defender/orchestrator/openshift) [NextDeploy Serverless Defender as a Lambda Layer](https://docs.prismacloud.io/admin-guide/install/deploy-defender/serverless/install-serverless-defender-layer)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
