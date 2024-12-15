

# Docker create and start vs Docker run

[Link]( ":)")

```bash

docker container create -i -t --name mycontainer alpine
# 6d8af538ec541dd581ebc2a24153a28329acb5268abe5ef868c1f1a261221752
docker container start --attach -i mycontainer
# echo hello world
hello world


# equal to 

docker run -it --name mycontainer2 alpine
/ # echo hello world
hello world
```

# Docker copy


[stackoverflow copy thing into container](https://stackoverflow.com/questions/22907231/how-to-copy-files-from-host-to-docker-container ":)")

```

docker cp foo.txt container_id:/foo.txt

```

# Docker Run shit


Dockerfile
``` DockerFile
# syntax=docker/dockerfile:1

FROM node:12.18.1
ENV NODE_ENV=production

# create directory
WORKDIR /app

COPY ["package.json", "package-lock.json*", "./"]

RUN npm install --production

COPY . .

CMD [ "node", "server.js" ]

```


.dockerignore
```
node_modules
```

build
```
docker build --tag node-docker .
```

# Docker run

 docker run \
  -it --rm -d \
  --network mongodb \
  --name rest-server \
  -p 8000:8000 \
  -e CONNECTIONSTRING=mongodb://mongodb:27017/notes \
  node-docker


option:
--rm=false: Automatically remove the container when it exits
stop了之后自动rm




## docker check container and image
docker ps

### with stauts
docker ps -la

## remove all existed containers
docker ps --filter status=exited | awk '{print $1}' | xargs docker rm

## network bridge

docker network create ## network_name ##

## docker run with network

docker run -it --name doccano/doccano -p 8000:8000 --network doccano_network --network-alias doccano_auto_label docanno/doccano
``` docker run -it name <container name> --network <bridge> --network-alias <name> <image> ```


## docker run without internet 
docker run --network none -it ubuntu:latest
--network none


## docker run into bash
docker run -it -p 7500:7500 doccano_helper /bin/bash

// don't remove, use this to restart the container
docker exec -it ##cotainerid## /bin/bash

-p from 容器里面 to 外面(服务器端)


## volume
相当于file sytem in host

docker rm -v redis





# COPY
docker cp xxx container:xxx
docker cp container:xxx xxx





# Docker run exited container, Wake up container


docker start #containerid
docker attach #containerid

# docker save a container into image
docker commit c3f279d17e0a  svendowideit/testimage:version3


# Docker config gpu

--gpus 0,1,2

no gpu:
--runtime=runc



# Docker remove dangline image 

docker rmi $(docker image ls -f "dangling=true" -q)



# Docker change entrypoint


docker run -it --entrypoint /bin/bash image_name


