For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/technology-overviews/twistlock-rules-guide-docker.md).

This article provides a list of all rules and their intended behavior in Prisma Cloud Console UI. The purpose of this article is to help users better understand the intention of each rule in the Console and it’s corresponding effect on the host environment.

## Running Docker commands through Defender[Direct link to heading](https://docs.prismacloud.io/admin-guide/technology-overviews/twistlock-rules-guide-docker\#running-docker-commands-through-defender)

To access Docker daemon through Defender, you must explicitly specify Defender’s host and port. For example:

AskCopy

```
$ docker -H <DEFENDER_HOST_ADDRESS>:9998 run alpine
```

It is possible to make the management traffic between the Docker client and the Docker daemon flow through Defender by default via two environment variables. Those can be configured on a remote machine that accesses Docker daemon on some host (such as dev laptop), or the host itself for users who do not have root privileges (which should be the majority of users).

AskCopy

```
$ export DOCKER_HOST=tcp://<defender host address>:9998

$ export DOCKER_TLS_VERIFY=1
```

Once set, default calls to Docker flow through Defender (e.g., docker ps, docker run alpine). Throughout this guide however, in this guide, we have followed the default command without setting environment variables.

### Containers[Direct link to heading](https://docs.prismacloud.io/admin-guide/technology-overviews/twistlock-rules-guide-docker\#containers)

For more information about the Docker API for containers, see [https://docs.docker.com/engine/api/v1.30/#tag/Container](https://docs.docker.com/engine/api/v1.30/#tag/Container).

#### container\_list - List containers[Direct link to heading](https://docs.prismacloud.io/admin-guide/technology-overviews/twistlock-rules-guide-docker\#container_list-list-containers)

Affects docker ps command on host which is used to list all running containers.

Command:

AskCopy

```
docker -H 10.0.0.1:9998 --tlsverify ps
```

Response:

AskCopy

```
[Prisma Cloud] The command container_list denied for user admin by rule Deny
```

#### container\_create - Create a container[Direct link to heading](https://docs.prismacloud.io/admin-guide/technology-overviews/twistlock-rules-guide-docker\#container_create-create-a-container)

Affects docker create command used to create a new container.

Command:

AskCopy

```
docker -H 10.0.0.1:9998 --tlsverify create morello/docker-whale
```

Response:

AskCopy

```
[Prisma Cloud] The command container_create denied for user admin by rule Deny
```

#### container\_inspect - Inspect a container[Direct link to heading](https://docs.prismacloud.io/admin-guide/technology-overviews/twistlock-rules-guide-docker\#container_inspect-inspect-a-container)

Affects docker inspect command used for returning information about the container.

Command:

AskCopy

```
docker -H 10.0.0.1 --tlsverify  inspect ubuntu_bash2
```

Response:

AskCopy

```
[Prisma Cloud] The command container_inspect denied for user admin by rule inspect
```

#### container\_top - List processes running inside a container[Direct link to heading](https://docs.prismacloud.io/admin-guide/technology-overviews/twistlock-rules-guide-docker\#container_top-list-processes-running-inside-a-container)

Affects docker top command used to display the running processes of a container

Command:

AskCopy

```
docker -H 10.0.0.1:9998 --tlsverify top ubuntu_bash
```

Response:

AskCopy

```
[Prisma Cloud] The command container_top denied for user admin by rule Deny
```

#### container\_logs - Get container logs[Direct link to heading](https://docs.prismacloud.io/admin-guide/technology-overviews/twistlock-rules-guide-docker\#container_logs-get-container-logs)

Affects docker logs command used for returning logs from the container present at the time of execution.

Command:

AskCopy

```
docker -H 10.0.0.1 --tlsverify logs ubuntu_bash2
```

Response:

AskCopy

```
[Prisma Cloud] The command container_logs denied for user admin by rule logs
```

#### container\_changes - Inspect changes on a container’s filesystem[Direct link to heading](https://docs.prismacloud.io/admin-guide/technology-overviews/twistlock-rules-guide-docker\#container_changes-inspect-changes-on-a-containers-filesystem)

Affect docker commit command and restricts any changes to the container.

Command:

AskCopy

```
docker -H 10.0.0.1 --tlsverify  commit --change "ENV DEBUG true" cc2d57988b aqsa/testimage:version3
```

Response:

AskCopy

```
[Prisma Cloud] The command container_commit denied for user admin by rule commit
```

#### container\_export - Export a container[Direct link to heading](https://docs.prismacloud.io/admin-guide/technology-overviews/twistlock-rules-guide-docker\#container_export-export-a-container)

Affects docker export command that exports a container’s filesystem as a tar archive

Command:

AskCopy

```
docker -H 10.0.0.1:9998 --tlsverify  export  twistlock_console -o saved.tar
```

Response:

AskCopy

```
[Prisma Cloud] The command container_export denied for user admin by rule export
```

#### container\_stats - Get container stats based on resource usage[Direct link to heading](https://docs.prismacloud.io/admin-guide/technology-overviews/twistlock-rules-guide-docker\#container_stats-get-container-stats-based-on-resource-usage)

Affects docker stats command on host which returns live data stream for running containers.

Command:

AskCopy

```
docker -H 10.0.0.1 --tlsverify stats  silly_stallman
```

Response:

AskCopy

```
[Prisma Cloud] The command container_stats denied for user admin by rule status
```

#### container\_resize - Resize a container[Direct link to heading](https://docs.prismacloud.io/admin-guide/technology-overviews/twistlock-rules-guide-docker\#container_resize-resize-a-container)

Affects docker logs command used for returning logs from the container present at the time of execution. This related to the size of the window of how output is returned from the container. It is called TTY.

Command:

Response:

#### container\_start - Start a container[Direct link to heading](https://docs.prismacloud.io/admin-guide/technology-overviews/twistlock-rules-guide-docker\#container_start-start-a-container)

Affects docker start command used to start one or more stopped containers

Command:

AskCopy

```
docker -H 10.0.0.1:9998 --tlsverify start ubuntu_bash
```

Response:

AskCopy

```
[Prisma Cloud] The command container_start denied for user admin by rule Deny all
```

#### container\_stop - Stop a container[Direct link to heading](https://docs.prismacloud.io/admin-guide/technology-overviews/twistlock-rules-guide-docker\#container_stop-stop-a-container)

Affects docker stop command used to stop running container

Command:

AskCopy

```
docker -H 10.0.0.1:9998 --tlsverify stop ubuntu_bash
```

Response:

AskCopy

```
[Prisma Cloud] The command container_stop denied for user admin by rule Deny
```

#### container\_restart - Restart a container[Direct link to heading](https://docs.prismacloud.io/admin-guide/technology-overviews/twistlock-rules-guide-docker\#container_restart-restart-a-container)

Affects docker restart command on host, used to restart a container.

Command:

AskCopy

```
docker -H 10.0.0.1:9998 --tlsverify restart ubuntu_bash
```

Response:

AskCopy

```
[Prisma Cloud] The command container_restart denied for user admin by rule Deny
```

#### container\_kill - Kill a container[Direct link to heading](https://docs.prismacloud.io/admin-guide/technology-overviews/twistlock-rules-guide-docker\#container_kill-kill-a-container)

Affects docker kill command used to kill a running container.

Command:

AskCopy

```
docker -H 10.0.0.1:9998 --tlsverify kill ubuntu_bash
```

Response:

AskCopy

```
[Prisma Cloud] The command container_kill denied for user admin by rule Deny
```

#### container\_rename - Rename a container[Direct link to heading](https://docs.prismacloud.io/admin-guide/technology-overviews/twistlock-rules-guide-docker\#container_rename-rename-a-container)

Affects docker rename command on host that is used to rename a container.

Command:

AskCopy

```
docker -H 10.0.0.1:9998 --tlsverify rename ubuntu_bash unbuntu
```

Response:

AskCopy

```
[Prisma Cloud] The command container_rename denied for user admin by rule Deny
Error: failed to rename container named ubuntu_bash
```

#### container\_pause - Pause a container[Direct link to heading](https://docs.prismacloud.io/admin-guide/technology-overviews/twistlock-rules-guide-docker\#container_pause-pause-a-container)

Affects docker pause command on host which is used to pause all processes within one or more containers.

Command:

AskCopy

```
docker -H 10.0.0.1 --tlsverify pause  focused_cori
```

Response:

AskCopy

```
[Prisma Cloud] The command container_pause denied for user admin by rule Deny
```

#### container\_unpause - Unpause a container[Direct link to heading](https://docs.prismacloud.io/admin-guide/technology-overviews/twistlock-rules-guide-docker\#container_unpause-unpause-a-container)

Affects docker unpause command on host which is used to un-suspend all processes in a container.

Command:

AskCopy

```
docker -H 10.0.0.1 --tlsverify unpause  silly_stallman
```

Response:

AskCopy

```
[Prisma Cloud] The command container_unpause denied for user admin by rule unpause
```

#### container\_attach - Attach to a container[Direct link to heading](https://docs.prismacloud.io/admin-guide/technology-overviews/twistlock-rules-guide-docker\#container_attach-attach-to-a-container)

Affects docker attach command on host where defender is deployed.

Command:

AskCopy

```
docker -H 10.0.0.1 --tlsverify attach  mycontainer
```

Response:

AskCopy

```
[Prisma Cloud] The command container_attach denied for user admin by rule attach persistent connection closed
```

#### container\_attachws - Attach to a container (websocket)[Direct link to heading](https://docs.prismacloud.io/admin-guide/technology-overviews/twistlock-rules-guide-docker\#container_attachws-attach-to-a-container-websocket)

Affects docker attach command on host where defender is deployed. Attach to the container id via websocket. Implements websocket protocol handshake according to RFC 6455

Command:

AskCopy

```
docker -H 10.0.0.1 --tlsverify attach  mycontainer
```

Response:

AskCopy

```
[Prisma Cloud] The command container_attach denied for user admin by rule attach persistent connection closed
```

#### container\_wait - Wait a container[Direct link to heading](https://docs.prismacloud.io/admin-guide/technology-overviews/twistlock-rules-guide-docker\#container_wait-wait-a-container)

Affects docker wait command used to block until a container stops, then print its exit code.

Command:

AskCopy

```
docker -H 10.0.0.1:9998 --tlsverify wait ubuntu_bash
```

Response:

AskCopy

```
[Prisma Cloud] The command container_wait denied for user admin by rule Deny
```

#### container\_delete - Remove a container[Direct link to heading](https://docs.prismacloud.io/admin-guide/technology-overviews/twistlock-rules-guide-docker\#container_delete-remove-a-container)

Affects docker rm command used for deleting a container.

Command:

AskCopy

```
docker -H 10.0.0.1:9998 --tlsverify rm  <container>
```

Response:

AskCopy

```
[Prisma Cloud] The command container_delete denied for user admin by rule delete
```

#### container\_archive - Gets an archive of filesystem resource in a container[Direct link to heading](https://docs.prismacloud.io/admin-guide/technology-overviews/twistlock-rules-guide-docker\#container_archive-gets-an-archive-of-filesystem-resource-in-a-container)

Get a tar archive of a resource in the filesystem of container id. Affects docker cp command

Command:

AskCopy

```
docker -H 10.0.0.1:9998 --tlsverify cp <container> > latest.tar
```

Response:

AskCopy

```
[Prisma Cloud] The command container_copy denied for user admin by rule delete
```

#### container\_extract - Extract an archive of files or folders to a directory in a container[Direct link to heading](https://docs.prismacloud.io/admin-guide/technology-overviews/twistlock-rules-guide-docker\#container_extract-extract-an-archive-of-files-or-folders-to-a-directory-in-a-container)

Affects docker export command. Uploads a tar archive to be extracted to a path in the filesystem of container id

Command:

AskCopy

```
docker -H 10.0.0.1:9998 --tlsverify cp <container> > latest.tar
```

Response:

AskCopy

```
[Prisma Cloud] The command container_exec_start denied for user admin by rule exec
```

### Images[Direct link to heading](https://docs.prismacloud.io/admin-guide/technology-overviews/twistlock-rules-guide-docker\#images)

For more information about the Docker API for images, see [https://docs.docker.com/engine/api/v1.30/#tag/Image](https://docs.docker.com/engine/api/v1.30/#tag/Image).

#### image\_list - List images[Direct link to heading](https://docs.prismacloud.io/admin-guide/technology-overviews/twistlock-rules-guide-docker\#image_list-list-images)

Affects docker images command used to list all images

Command:

AskCopy

```
docker -H 10.0.0.1:9998 --tlsverify images
```

Response:

AskCopy

```
[Prisma Cloud] The command image_list denied for user admin by rule Deny
```

#### image\_build - Build image from a Dockerfile[Direct link to heading](https://docs.prismacloud.io/admin-guide/technology-overviews/twistlock-rules-guide-docker\#image_build-build-image-from-a-dockerfile)

Affects docker build command that is used to build an image from a Dockerfile.

Command:

AskCopy

```
docker -H 172.18.0.1:9998 --tlsverify build -t aqsa/testimage:v2 .
```

Response:

AskCopy

```
[Prisma Cloud] The command image_build denied for user admin by rule Default - deny all
```

#### image\_create - Create an image[Direct link to heading](https://docs.prismacloud.io/admin-guide/technology-overviews/twistlock-rules-guide-docker\#image_create-create-an-image)

Affects docker pull command which is used to pull an image

Command:

AskCopy

```
docker -H 10.0.0.1:9998 --tlsverify pull ubuntu:latest
```

Response:

AskCopy

```
[Prisma Cloud] The command image_create denied for user admin by rule Deny
```

#### image\_inspect - Inspect an image[Direct link to heading](https://docs.prismacloud.io/admin-guide/technology-overviews/twistlock-rules-guide-docker\#image_inspect-inspect-an-image)

Description

Affects docker inspect command used for returning information about the container.

Command:

AskCopy

```
docker -H 10.0.0.1:9998 --tlsverify inspect 28e7d49f8e6d
```

Response:

AskCopy

```
[Prisma Cloud] The command image_inspect denied for user admin by rule images
```

#### image\_history - Get the history of an image[Direct link to heading](https://docs.prismacloud.io/admin-guide/technology-overviews/twistlock-rules-guide-docker\#image_history-get-the-history-of-an-image)

Affects docker history <image> command.

Command:

AskCopy

```
docker -H 172.18.0.1:9998 --tlsverify history twistlock
```

Response:

AskCopy

```
[Prisma Cloud] The command image_history denied for user admin by rule Default - deny all
```

#### image\_push - Push an image on the registry[Direct link to heading](https://docs.prismacloud.io/admin-guide/technology-overviews/twistlock-rules-guide-docker\#image_push-push-an-image-on-the-registry)

Affects command docker push for pushing an image to repository

Command:

AskCopy

```
docker -H 10.0.0.1:9998 --tlsverify push ubuntu:latest
```

Response:

AskCopy

```
[Prisma Cloud] The command image_push denied for user admin by rule Deny
```

#### image\_tag - Tag an image into a repository[Direct link to heading](https://docs.prismacloud.io/admin-guide/technology-overviews/twistlock-rules-guide-docker\#image_tag-tag-an-image-into-a-repository)

Affects docker tag command used to tag an image in the repository

Command:

AskCopy

```
docker -H 10.0.0.1:9998 --tlsverify tag ubuntu:latest aqsa:tag
```

Response:

AskCopy

```
[Prisma Cloud] The command image_tag denied for user admin by rule Deny
```

#### image\_delete - Remove an image[Direct link to heading](https://docs.prismacloud.io/admin-guide/technology-overviews/twistlock-rules-guide-docker\#image_delete-remove-an-image)

Affects docker rmi command used to delete an image

Command:

AskCopy

```
docker -H 10.0.0.1:9998 --tlsverify  rmi aqsa/testimage:version3
```

Response:

AskCopy

```
[Prisma Cloud] The command image_delete denied for user admin by rule Deny
```

#### images\_search - Search images[Direct link to heading](https://docs.prismacloud.io/admin-guide/technology-overviews/twistlock-rules-guide-docker\#images_search-search-images)

Affects docker search command which gives a list of available images matching the search item.

Command:

AskCopy

```
docker -H 10.0.0.1:9998 --tlsverify search twistlock
```

Response:

AskCopy

```
[Prisma Cloud] The command images_search denied for user admin by rule deny
```

### MISC[Direct link to heading](https://docs.prismacloud.io/admin-guide/technology-overviews/twistlock-rules-guide-docker\#misc)

Misc other docker commands.

#### docker\_check\_auth - Check auth configuration[Direct link to heading](https://docs.prismacloud.io/admin-guide/technology-overviews/twistlock-rules-guide-docker\#docker_check_auth-check-auth-configuration)

Validates credentials for a registry and get identity token, if available, for accessing the registry without password. Affects docker login on the host.

Command:

AskCopy

```
docker -H 172.18.0.1:9998 --tlsverify login
```

Response:

AskCopy

```
[Prisma Cloud] The command docker_info denied for user admin by rule Default - deny all
```

#### docker\_info - Display system-wide information[Direct link to heading](https://docs.prismacloud.io/admin-guide/technology-overviews/twistlock-rules-guide-docker\#docker_info-display-system-wide-information)

Affects docker info command used to display system-wide information

Command:

AskCopy

```
docker -H 10.0.0.1:9998 --tlsverify info
```

Response:

AskCopy

```
[Prisma Cloud] The command docker_info denied for user admin by rule Deny
```

#### docker\_version - Show the docker version information[Direct link to heading](https://docs.prismacloud.io/admin-guide/technology-overviews/twistlock-rules-guide-docker\#docker_version-show-the-docker-version-information)

Affects docker version command on host which is used to find docker version.

Command:

AskCopy

```
docker -H 10.0.0.1 --tlsverify version
```

Response:

AskCopy

```
[Prisma Cloud] The command docker_version denied for user admin by rule version
```

#### docker\_ping - Ping the docker server[Direct link to heading](https://docs.prismacloud.io/admin-guide/technology-overviews/twistlock-rules-guide-docker\#docker_ping-ping-the-docker-server)

The goal of this api is to ping the Docker server and make sure it is up and running.

Command:

It is intended to be called by an external monitoring system. It does not have a direct docker CLI command.

#### container\_commit - Create a new image from a container’s changes[Direct link to heading](https://docs.prismacloud.io/admin-guide/technology-overviews/twistlock-rules-guide-docker\#container_commit-create-a-new-image-from-a-containers-changes)

Affects docker commit command used for committing container’s file changes etc into a new image.

Command:

AskCopy

```
docker -H 10.0.0.1 --tlsverify  commit --change "ENV DEBUG true" cc2d57988b aqsa/testimage:version3
```

Response:

AskCopy

```
[Prisma Cloud] The command container_commit denied for user admin by rule commit
```

#### docker\_events - Monitor docker’s events[Direct link to heading](https://docs.prismacloud.io/admin-guide/technology-overviews/twistlock-rules-guide-docker\#docker_events-monitor-dockers-events)

Affects docker events command on host which is used to return real time events from the server.

Command:

AskCopy

```
docker -H 10.0.0.1 --tlsverify events
```

Response:

AskCopy

```
[Prisma Cloud] The command docker_events denied for user admin by rule events
```

#### images\_archive - Get a tarball containing all images[Direct link to heading](https://docs.prismacloud.io/admin-guide/technology-overviews/twistlock-rules-guide-docker\#images_archive-get-a-tarball-containing-all-images)

Affects docker save command to save images to a tar archive

Command:

AskCopy

```
docker -H 172.17.0.1:9998 --tlsverify save $(docker images -q) -o home/aqsa/mydockersimages.tar
```

Response:

AskCopy

```
[Prisma Cloud] The command images_archive denied for user admin by rule Default - deny all
```

#### images\_load - Load a tarball with a set of images and tags into docker[Direct link to heading](https://docs.prismacloud.io/admin-guide/technology-overviews/twistlock-rules-guide-docker\#images_load-load-a-tarball-with-a-set-of-images-and-tags-into-docker)

Affects docker load command to load an image from a tar archive or STDIN

Command:

AskCopy

```
docker -H 172.17.0.1:9998 --tlsverify load -i /home/aqsa/twistlock_1_6_81.tar.gz
```

Response: \[Prisma Cloud\] The command images\_load denied for user admin by rule Default - deny all

#### container\_exec\_create - Exec Create[Direct link to heading](https://docs.prismacloud.io/admin-guide/technology-overviews/twistlock-rules-guide-docker\#container_exec_create-exec-create)

Affects docker\_exec command to create any new container.

Command:

AskCopy

```
docker -H 10.0.0.1 --tlsverify   exec -d ubuntu_bash2 touch /tmp/execWorks
```

Response:

AskCopy

```
[Prisma Cloud] The command container_exec_start denied for user admin by rule exec
```

#### container\_exec\_start - Exec Start[Direct link to heading](https://docs.prismacloud.io/admin-guide/technology-overviews/twistlock-rules-guide-docker\#container_exec_start-exec-start)

Affects docker exec command used for running a command in a running container.

Command:

AskCopy

```
docker -H 10.0.0.1 --tlsverify   exec -d ubuntu_bash2 touch /tmp/execWorks
```

Response:

AskCopy

```
[Prisma Cloud] The command container_exec_start denied for user admin by rule exec
```

#### container\_exec\_inspect - Exec Inspect[Direct link to heading](https://docs.prismacloud.io/admin-guide/technology-overviews/twistlock-rules-guide-docker\#container_exec_inspect-exec-inspect)

Affects docker exec command used for running a command in a running container.

Command:

AskCopy

```
docker -H 10.0.0.1 --tlsverify   exec -d ubuntu_bash2 touch /tmp/execWorks
```

Response:

AskCopy

```
[Prisma Cloud] The command container_exec_start denied for user admin by rule exec
```

#### container\_archive\_head[Direct link to heading](https://docs.prismacloud.io/admin-guide/technology-overviews/twistlock-rules-guide-docker\#container_archive_head)

Command:

AskCopy

```
docker -H 10.0.0.1 --tlsverify unpause  silly_stallman
```

Response:

AskCopy

```
[Prisma Cloud] The command container_unpause denied for user admin by rule unpause
```

#### container\_copyfiles[Direct link to heading](https://docs.prismacloud.io/admin-guide/technology-overviews/twistlock-rules-guide-docker\#container_copyfiles)

Affects docker cp command used to copy files from and to containers and local file system on host.

Command:

AskCopy

```
docker -H 10.0.0.1 --tlsverify cp file  mycontainer:~
```

Response:

AskCopy

```
[Prisma Cloud] The command container_copyfiles denied for user admin by rule unpause
```

### Volumes[Direct link to heading](https://docs.prismacloud.io/admin-guide/technology-overviews/twistlock-rules-guide-docker\#volumes)

For more information about the Docker API for volumes, see [https://docs.docker.com/engine/api/v1.30/#tag/Volume](https://docs.docker.com/engine/api/v1.30/#tag/Volume).

#### volume\_list - List volumes[Direct link to heading](https://docs.prismacloud.io/admin-guide/technology-overviews/twistlock-rules-guide-docker\#volume_list-list-volumes)

Affects docker volume ls command to list all volumes

Command:

AskCopy

```
docker -H 10.0.0.1:9998 --tlsverify volume ls
```

Response:

AskCopy

```
[Prisma Cloud] The command volume_list denied for user admin by rule Deny
```

#### volume\_create - Create a volume[Direct link to heading](https://docs.prismacloud.io/admin-guide/technology-overviews/twistlock-rules-guide-docker\#volume_create-create-a-volume)

Affects docker volume create command to create a volume

Command:

AskCopy

```
docker -H 10.0.0.1:9998 --tlsverify volume create
```

Response:

AskCopy

```
[Prisma Cloud] The command volume_create denied for user admin by rule Deny
```

#### volume\_inspect - Inspect a volume[Direct link to heading](https://docs.prismacloud.io/admin-guide/technology-overviews/twistlock-rules-guide-docker\#volume_inspect-inspect-a-volume)

Affects docker volume inspect command to display detailed information on one or more volumes

Command:

AskCopy

```
docker -H 10.0.0.1:9998 --tlsverify volume inspect f1c7
```

Response:

AskCopy

```
[Prisma Cloud] The command volume_inspect denied for user admin by rule Deny
```

#### volume\_remove - Remove a volume[Direct link to heading](https://docs.prismacloud.io/admin-guide/technology-overviews/twistlock-rules-guide-docker\#volume_remove-remove-a-volume)

Affects docker volume rm command to remove one or more volumes

Command:

AskCopy

```
docker -H 10.0.0.1:9998 --tlsverify volume rm f671
```

Response:

AskCopy

```
[Prisma Cloud] The command volume_remove denied for user admin by rule Deny
```

### Networks[Direct link to heading](https://docs.prismacloud.io/admin-guide/technology-overviews/twistlock-rules-guide-docker\#networks)

For information about the Docker API for networks, see [https://docs.docker.com/engine/api/v1.30/#tag/Network](https://docs.docker.com/engine/api/v1.30/#tag/Network).

#### network\_list - list networks[Direct link to heading](https://docs.prismacloud.io/admin-guide/technology-overviews/twistlock-rules-guide-docker\#network_list-list-networks)

Affects docker network ls to list networks

Command:

AskCopy

```
docker -H 172.17.0.1:9998 --tlsverify network ls
```

Response:

AskCopy

```
[Prisma Cloud] The command network_list denied for user admin by rule Default - deny all
```

#### network\_inspect - Inspect network[Direct link to heading](https://docs.prismacloud.io/admin-guide/technology-overviews/twistlock-rules-guide-docker\#network_inspect-inspect-network)

Affects docker network inspect to display detailed information on one or more networks

Command:

AskCopy

```
docker -H 172.17.0.1:9998 --tlsverify network inspect 82b1c
```

Response:

AskCopy

```
[Prisma Cloud] The command network_inspect denied for user admin by rule Default - deny all
```

#### network\_create - Create a network[Direct link to heading](https://docs.prismacloud.io/admin-guide/technology-overviews/twistlock-rules-guide-docker\#network_create-create-a-network)

Affects docker network create to create a network

Command:

AskCopy

```
docker -H 172.17.0.1:9998 --tlsverify network create new-network
```

Response:

AskCopy

```
[Prisma Cloud] The command network_create denied for user admin by rule Default - deny all
```

#### network\_connect - Connect a container to a network[Direct link to heading](https://docs.prismacloud.io/admin-guide/technology-overviews/twistlock-rules-guide-docker\#network_connect-connect-a-container-to-a-network)

Affects docker network connect to connect a container to a network

Command:

AskCopy

```
docker -H 172.17.0.1:9998 --tlsverify network connect new-network container1
```

Response:

AskCopy

```
[Prisma Cloud] The command network_connect denied for user admin by rule Default - deny all
```

#### network\_disconnect - Disconnect a container from a network[Direct link to heading](https://docs.prismacloud.io/admin-guide/technology-overviews/twistlock-rules-guide-docker\#network_disconnect-disconnect-a-container-from-a-network)

Affects docker network disconnect to disconnect a container from a network

Command:

AskCopy

```
docker -H 172.17.0.1:9998 --tlsverify network disconnect new-network container1
```

Response:

AskCopy

```
[Prisma Cloud] The command network_disconnect denied for user admin by rule Default - deny all
```

#### network\_remove - Remove a network[Direct link to heading](https://docs.prismacloud.io/admin-guide/technology-overviews/twistlock-rules-guide-docker\#network_remove-remove-a-network)

Affects docker network rm to remove one or more networks

Command:

AskCopy

```
docker -H 172.17.0.1:9998 --tlsverify network rm new-network
```

Response:

AskCopy

```
[Prisma Cloud] The command network_remove denied for user admin by rule Default - deny all
```

### Secrets[Direct link to heading](https://docs.prismacloud.io/admin-guide/technology-overviews/twistlock-rules-guide-docker\#secrets)

Secrets are added in Prisma Cloud 2.0 in accordance with Docker Engine API v1.26.

For more information about the Docker API for secrets, see [https://docs.docker.com/engine/api/v1.30/#tag/Secret](https://docs.docker.com/engine/api/v1.30/#tag/Secret).

#### secret\_list - List secrets[Direct link to heading](https://docs.prismacloud.io/admin-guide/technology-overviews/twistlock-rules-guide-docker\#secret_list-list-secrets)

Affects docker secret ls command used to list secrets.

Command:

AskCopy

```
docker -H 10.0.0.1:9998 --tlsverify secret ls
```

Response:

AskCopy

```
[Prisma Cloud] The command secret_ls denied for user admin by rule Default - deny all
```

#### secret\_create - Create secrets[Direct link to heading](https://docs.prismacloud.io/admin-guide/technology-overviews/twistlock-rules-guide-docker\#secret_create-create-secrets)

Affects docker secret create command used to create secrets.

Command:

AskCopy

```
docker -H 10.0.0.1:9998 --tlsverify secret create my-secret ./aqsa.json
```

Response:

AskCopy

```
[Prisma Cloud] The command secret_create denied for user admin by rule Default - deny all
```

#### secret\_inspect - Inspect secrets[Direct link to heading](https://docs.prismacloud.io/admin-guide/technology-overviews/twistlock-rules-guide-docker\#secret_inspect-inspect-secrets)

Affects docker secret inspect command used to inspect secrets.

Command:

AskCopy

```
docker -H 10.0.0.1:9998 --tlsverify secret inspect <id>
```

Response:

AskCopy

```
[Prisma Cloud] The command secret_inspect denied for user admin by rule Default - deny all
```

#### secret\_remove - Delete secrets[Direct link to heading](https://docs.prismacloud.io/admin-guide/technology-overviews/twistlock-rules-guide-docker\#secret_remove-delete-secrets)

Affects docker secret rm command used to remove one or more secrets.

Command:

AskCopy

```
docker -H 10.0.0.1:9998 --tlsverify secret rm aqsa.json
```

Response:

AskCopy

```
[Prisma Cloud] The command secret_rm denied for user admin by rule Default - deny all
```

#### secret\_update - Update a secret[Direct link to heading](https://docs.prismacloud.io/admin-guide/technology-overviews/twistlock-rules-guide-docker\#secret_update-update-a-secret)

Affects POST /secrets/{id}/update command used to remove one or more secrets.

Command:

Response:

[PreviousServerless Radar](https://docs.prismacloud.io/admin-guide/technology-overviews/serverless-radar) [NextDefender architecture](https://docs.prismacloud.io/admin-guide/technology-overviews/defender-architecture)

Last updated 3 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
