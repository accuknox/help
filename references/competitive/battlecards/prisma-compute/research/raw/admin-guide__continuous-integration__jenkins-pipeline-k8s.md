For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/continuous-integration/jenkins-pipeline-k8s.md).

Jenkins is fundamentally architected as a distributed system, with a master that coordinates the builds and agents that do the work. The Kubernetes plugin enables deploying a distributed Jenkins build system to a Kubernetes cluster. Everything required to deploy Jenkins to a Kubernetes cluster is nicely packaged in the Jenkins Helm chart. This article explains how to integrate the Prisma Cloud scanner into a pipeline build running in a Kubernetes cluster.

## Key concepts[Direct link to heading](https://docs.prismacloud.io/admin-guide/continuous-integration/jenkins-pipeline-k8s\#key-concepts)

A pipeline is a script that tells Jenkins what to do when your pipeline is run. The Kubernetes Plugin for Jenkins lets you control the creation of the Jenkins slave pod from the pipeline, and add one or more build containers to the slave pod to accommodate build requirements and dependencies.

When the Jenkins master schedules the new build, it creates a new slave pod. Each stage of the build is run in a container in the slave pod. By default, each stage runs in the Jenkins slave (jnlp) container, unless other specified. The following diagram shows a slave pod being launched on a worker node using the Java Network Launch Protocol (JNLP) protocol:

![Start slave pod](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-d38407e8af7f355df6d63c5bdbc3ebd7bb90e7ec%252Fjenkins_pipeline_k8s_start_slave_pod.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=b64efd0308f7e1addef298eac6a7d63e&sv=3)

A slave pod is composed of at least one container, which must be the Jenkins jnlp container. Your pipeline defines a podTemplate, which specifies all the containers that make up the Jenkins slave pod. You’ll want your podTemplate to include any images that provide the tools required to execute the build. For example, if one part of your app consists of a C library, then your podTemplate should include a container that provides the GCC toolchain, and the build stage for the library should execute within the context of the GCC container.

![Pod template](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-ac10d365d19e1bb68445356d28f19cc287c85e77%252Fjenkins_pipeline_k8s_pod_template.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=01735eef38fe1e1171b86211f3bd2aae&sv=3)

The Prisma Cloud Jenkins plugin lets you scan images generated in your pipeline.

The Prisma Cloud scanner can run inside the default Jenkins jnlp slave container only. It cannot be run within the context of a different container (i.e. from within the container statement block).

## Scripted Pipeline[Direct link to heading](https://docs.prismacloud.io/admin-guide/continuous-integration/jenkins-pipeline-k8s\#scripted-pipeline)

This section provides a pipeline script that you can use as a starting point for your own script.

You cannot run the Prisma Cloud scanner inside a container. The following example snippet will NOT work.

AskCopy

```
stage('Prisma Cloud Scan') {
  container('jenkins-slave-twistlock') {
    // THIS DOES NOT WORK
    prismaCloudScanImage ca: '', cert: '', ...
  }
}
```

Instead, run the Prisma Cloud scanner in the normal context:

AskCopy

```
stage('Prisma Cloud Scan') {
  // THIS WILL WORK
  prismaCloudScanImage ca: '', cert: '', ...
}
```

**Prerequisites:**

- You have set up a Kubernetes cluster.

- You have installed Jenkins in your cluster. The [Jenkins Helm chart](https://github.com/jenkinsci/helm-charts) is the easiest path for bringing up Jenkins in a Kubernetes cluster.

- [Install the Prisma Cloud Jenkins plugin.](https://docs.prismacloud.io/admin-guide/continuous-integration/jenkins-plugin)


### Pipeline template[Direct link to heading](https://docs.prismacloud.io/admin-guide/continuous-integration/jenkins-pipeline-k8s\#pipeline-template)

The following template can be used as a starting point for your own scripted pipeline. This template is a fully functional pipeline that pulls the nginx:stable-alpine image from Docker Hub, and then scans it with the Prisma Cloud scanner.

While this example shows how to scan container images, you can also call _prismaCloudScanFunction_ to scan your severless functions.

AskCopy

```
#!/usr/bin/groovy

podTemplate(label: 'prismaCloud-example-builder', // See 1
  containers: [\
    containerTemplate(\
      name: 'jnlp',\
      image: 'jenkinsci/jnlp-slave:3.10-1-alpine',\
      args: '${computer.jnlpmac} ${computer.name}'\
    ),\
    containerTemplate(\
      name: 'alpine',\
      image: 'twistian/alpine:latest',\
      command: 'cat',\
      ttyEnabled: true\
    ),\
  ],
  volumes: [ // See 2\
    hostPathVolume(mountPath: '/var/run/docker.sock', hostPath: '/var/run/docker.sock'), // See 3\
  ]
)
{
  node ('prismaCloud-example-builder') {

    stage ('Pull image') { // See 4
      container('alpine') {
        sh """
        curl --unix-socket /var/run/docker.sock \ // See 5
             -X POST "http:/v1.24/images/create?fromImage=nginx:stable-alpine"
        """
      }
    }

    stage ('Prisma Cloud scan') { // See 6
        prismaCloudScanImage ca: '',
                    cert: '',
                    dockerAddress: 'unix:///var/run/docker.sock',
                    image: 'nginx:stable-alpine',
                    resultsFile: 'prisma-cloud-scan-results.xml',
                    project: '',
                    dockerAddress: 'unix:///var/run/docker.sock',
                    ignoreImageBuildTime: true,
                    key: '',
                    logLevel: 'info',
                    podmanPath: '',
                    project: '',
                    resultsFile: 'prisma-cloud-scan-results.json',
                    ignoreImageBuildTime:true
    }

    stage ('Prisma Cloud publish') {
        prismaCloudPublish resultsFilePattern: 'prisma-cloud-scan-results.json'
    }
  }
}
```

This template has the following characteristics:

- **1** — This _podTemplate_ defines two containers: the required jnlp-slave container and a custom alpine container. The custom alpine container extends the official alpine image by adding the curl package.

- **2** — The docker socket is mounted into all containers in the pod. For more information about the _volumes_ field, see [Pod and container template configuration](https://github.com/jenkinsci/kubernetes-plugin/blob/master/README.md#pod-and-container-template-configuration).

- **3** — By default, the docker socket lets the root user or any member of the docker group read or write to it. The default user in the jnlp container is _jenkins_ The Prisma Cloud plugin functions need access to the docker socket, so you must add the jenkins user to the docker group. The following listing shows the default permissions for the docker socket:

















AskCopy



```
$ ls -l /var/run/docker.sock
srw-rw----  1 root docker   0 May 30 07:58 docker.sock
```

- **4** — The first stage of the build pulls down the nginx image. We run the curl command inside the alpine container because the alpine container was specifically built to provide curl. Note that the _prismaCloudScanImage_ and _prismaCloudPublish_ functions cannot be run inside the _container('<NAME')_ block . The must be run in the default jnlp container context.

- **5** — There is a lot of [debate](https://jpetazzo.github.io/2015/09/03/do-not-use-docker-in-docker-for-ci/) about docker-in-docker, especially with respect to CI/CD pipelines. In most cases, docker-in-docker is not required for build pipelines. In this example, we run docker commands using the API exposed by the docker socket. Alternatively, we could use a [container with just the Docker client installed](https://github.com/nathanielc/docker-client).

- **6** — The second stage runs the Prisma Cloud scanner on the nginx image in the default jnlp container.


You can run the Prisma Cloud scanner inside a container using the 'containerized' flag. Scanning from inside a container is only required for special situations.

AskCopy

```
stage(‘Parallel’) {
  agent {
    docker {
      image ‘ubuntu:latest’
    }
  }
  stages {
    stage(‘Prisma Cloud Scan’) {
      steps {
        prismaCloudScanImage ca: '', cert: '', containerized:true, ...
      }
    }
    ...
}
```

When using the containerized mode, image ID won’t be displayed in the scan results (only image name).

[PreviousRun Jenkins in a container](https://docs.prismacloud.io/admin-guide/continuous-integration/run-jenkins-container) [NextSet policy in the CI plugins](https://docs.prismacloud.io/admin-guide/continuous-integration/set-policy-ci-plugins)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
