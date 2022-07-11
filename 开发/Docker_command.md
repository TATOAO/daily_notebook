
# Docker Run shit


Dockerfile
```
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
docker ps --filter status=existed p1 | xargs docker rm

## network bridge

docker network create ## network_name ##

## docker run with network

docker run -it --name doccano/doccano -p 8000:8000 --network doccano_network --network-alias doccano_auto_label docanno/doccano
``` docker run -it name <container name> --network <bridge> --network-alias <name> <image> ```


## docker run into bash
docker run -it -p 7500:7500 doccano_helper /bin/bash

// don't remove, use this to restart the container
docker exec -it ##cotainerid## /bin/bash




## volume
相当于file sytem in host

docker rm -v redis

