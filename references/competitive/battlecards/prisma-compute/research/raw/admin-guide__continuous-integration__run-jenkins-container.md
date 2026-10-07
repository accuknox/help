For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/continuous-integration/run-jenkins-container.md).

Running Jenkins inside a container is a common setup. This article shows you how to set up Jenkins to run in a container so that it can build and scan Docker images.

## Setting up and starting a Jenkins container[Direct link to heading](https://docs.prismacloud.io/admin-guide/continuous-integration/run-jenkins-container\#setting-up-and-starting-a-jenkins-container)

To set up Jenkins to run in a container:

**Prerequisite:** You have already installed Docker on the host machine.

1. Create the following Dockerfile. It uses the base Jenkins image and sets up the required permissions for the jenkins user.

















AskCopy



```
FROM jenkins/jenkins:lts

USER root
RUN apt-get update \
         && apt-get install -y sudo libltdl7 \
         && rm -rf /var/lib/apt/lists/*
RUN echo "jenkins ALL=NOPASSWD: ALL" >> /etc/sudoers
```

2. Build the image.

















AskCopy



```
$ docker build -t jenkins_docker .
```

3. Run the Jenkins container, giving it access to the docker socket.

















AskCopy



```
$ docker run -d -v /var/run/docker.sock:/var/run/docker.sock \
     -v $(which docker):/usr/bin/docker -p 8080:8080 jenkins_docker
```

4. Open a browser and navigate to <JENKINS\_HOST>:8080.

5. Install the Prisma Cloud plugin.











For more information, see [Jenkins plugin](https://docs.prismacloud.io/admin-guide/continuous-integration/jenkins-plugin).


[PreviousJenkins Pipeline project](https://docs.prismacloud.io/admin-guide/continuous-integration/jenkins-pipeline-project) [NextJenkins pipeline on K8S](https://docs.prismacloud.io/admin-guide/continuous-integration/jenkins-pipeline-k8s)

Last updated 3 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
