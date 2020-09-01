## Docker Commands

Note: If you didn't set the container name when you created it, you need to refer to it by its container ID in commands.

- `docker --version` gets the currently installed version of docker

- `docker pull <IMAGE_NAME>` pulls images from the docker repository:
```
$ docker pull ubuntu
Using default latest tag: latest
latest: Pulling from library/ubuntu
...
```

- `docker run -it -d --name <CONTAINER_NAME> <IMAGE_NAME>`:
```
$ docker run -it -d --name my-container ubuntu
```
The `--name` flag assigns a name to the new container.  
The `-i` flag creates an interactive `bash` shell in the container; keeps stdin open even if not attached.  
The `-d` flag runs the container in the background and prints container ID.  
The `-t` flag instructs Docker to allocate a pseudo-TTY; tells the main process inside docker that its input is a
terminal device. (Together with `-i`, it connects to the container's stdin.)

- `docker ps` lists the running containers. `docker ps -a` shoes all running and exited containers.

- `docker exec -it <CONTAINER_NAME> bash` executes an interactive `bash` shell on the container:
```
$ docker exec -it my-container bash
root@container-id:/#
```

- `docker stop <CONTAINER_NAME>` stops a running container. It gives the container time to shutdown gracefully.

- `docker kill <CONTAINER_NAME>` kills the container by stopping its execution immediately.

- `docker commit <CONTAINER_NAME> <USERNAME/IMAGE_NAME>` creates a new image of an edited container on the local system:
```
$ docker commit my-container felicia/ubuntunew
```
It can be useful to commit a container's file changes or settings into a new image because it allows you to debug a
container by running an interactive shell, or to export a working dataset to another server.  

- `docker images` lists all locally stored docker images:
```
$ docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
felicia/ubuntunew   latest              5e1270aca7d8        2 hours ago         73.9MB
<none>              <none>              fb2d6b93c072        2 hours ago         73.9MB
ubuntu              latest              4e2eef94cd6b        12 days ago         73.9MB
alpine              latest              a24bb4013296        3 months ago        5.57MB
```

- `docker login` is used to login to the docker hub repository:
```
$ docker login
Login with your Docker ID to push and pull images from Docker Hub. If you don't have a Docker ID, head over to
https://hub.docker.com to create one.
Username:
```

- `docker push <USERNAME/IMAGE_NAME>` pushes an image to the docker hub repository:
```
$ docker push felicia/ubuntunew
The push refers to a repository...
```

- `docker rm <CONTAINER_NAME>` deletes a stopped container

- `docker rmi <IMAGE_ID>` deletes an image from local storage. Use `docker images` to see your image IDs:
```
$ docker rmi bb5c683893b6
Untagged: felicia/ubuntunew:latest
Deleted: sha256:bb5c683893b601d6407d8df6bfcc328b42be1782aac3de26a2fc254d6ccae546
```

- `docker build <PATH_TO_DOCKER_FILE>` builds an image from a specified docker file:
```
$ docker build .
Sending build context to Docker daemon...
```

## Task

Complete a file stub `script.sh` with one or more steps that does the following:
- runs a new Docker container
'my-container' from the 'busybox' image (latest tag) in interactive background mode, without pseudo-TTY allocation
- passes an existing environment variable "MY_ENVIRONMENT_VARIABLE" to the "my-container" container.

Note
- all tasks should be done within a simple `script.sh` execution
- Docker is already installed
- You have sudo access

Grading
- execution result of `docker exec my-container /bin/sh -c "echo $MY_ENVIRONMENT_VARIABLE"` is equal to
`MY_ENVIRONMENT_VARIABLE` value on host.

`script.sh` file initially contained:

```
#!/usr/bin/env bash
docker run -di --name example-container alpine
docker exec -i example-container echo "Good luck! :)"

exit 0
```

My answer
```
#!/usr/bin/env bash
docker run -di --name my-container busybox
docker exec -i my-container /bin/sh -c "echo $MY_ENVIRONMENT_VARIABLE"

exit 0
```

- the `--name` flag assigns a name to the new container
- the `-i` flag creates an interactive `bash` shell in the container
- the `-d` flag runs the container in the background and prints container ID
- `docker exec` is used to run a command in a running container

## My Notes

- Scripting allows any shell interaction to be automated and scripted
- After writing your shell script in a new file, make your new file executable by running `chmod +x new_file.sh`
- Execute your new script by running `./new_file.sh`

- To define your script's interpreter as Bash, locate a full path to its binary using `which bash`:
```
$ which bash
/bin/bash
```
- prefix this with a shebang `#!` and insert it as the first line of your script i.e. the first line of your script
could be `#!/bin/bash`
