This installation is intended for our commercial version of Faraday. For our community version, please check this [installation guide](https://github.com/infobyte/faraday/wiki/Installation-Docker)

#### Loading Image
Once you have downloaded our image tar file from [infobytesec portal](portal.faradaysec.com) you'll need to load it in docker:

```
    $ docker load -i <path to image tar file>
```

Check Image

```
    $ docker image ls | grep faraday
```

#### Configuration

This image can be run as a service or as a standalone container. Both runs Faraday Server without Postgres. You will note that we created /faraday-license and /faraday-storage volumes (for mount your license and storage) and environment variables (below) for Faraday configuration.

##### Database Connection

The following variables came with default values so you'll need to customize some or all of them depending on your installation config. 

      - PGSQL_HOST=172.2.0.1
      - PGSQL_USER=faraday_postgresql
      - PGSQL_PASSWD=mypgsqlpassword
      - PGSQL_DBNAME=faraday

```
When Faraday runs as a service PGSQL_PASSWD can be configured with docker secrets (default in docker-compose.yml). The simplest way to create a secret is reading from standard input (you should take care of bash history).

```
    $ printf mypgsqlpassword | docker secret create pgsql_passwd -
```

Once created, edit docker-compose.yml and set:

```
    $ vim docker-compose.yml

    version: '3.7'

    services:
      ...
      environment:
        - PGSQL_PASSWD=/run/secrets/pgsql_passwd  
      ...
```
      
For more about secrets check [docker web page](https://docs.docker.com/engine/swarm/secrets/)

##### Volumes

Current user's ~/.faraday/doc and ~/.faraday/storage folders are mounted by default. In case you have a different installation please replace them with proper ones in

```
    [standalone]
    $ docker run \
    ....
    -v /path/to/my_doc_folder:/faraday-license \
    -v /path/to/my_storage_folder:/faraday-storage \
    ....
    or

    [service]
    $ vim docker-compose.yml

    version: '3.7'

    services:
      ...
      volumes:
        - /path/to/my_doc_folder:/faraday-license
        - /path/to/my_storage_folde:/faraday-storage
      ...

#### Running Faraday

##### As a standalone container

 ```
    $ docker run \
      -v ~/.faraday/doc:/faraday-license \
      -v ~/.faraday/storage:/faraday-storage \
      -p 5985:5985 \
      -e PGSQL_HOST='192.168.20.29' \
      -e PGSQL_PASSWD='mypgsqlpassword' \
      -e LISTEN_ADDR='0.0.0.0' \
      faraday:latest
 ```
Check container

```
    $ docker container ls
```

##### As a service

Initialize Swarm

```
    $ docker swarm init
```

In case you have more than one ip addr configured in your machine you have to specify which one to use.

```
    $ docker swarm init --advertise-addr=192.168.20.29
```

Docker Compose File:

Use this docker-compose as example if you want to:

```
version: '3.7' 
 
services: 
  server: 
    image: faradaycorp:latest 
    environment: 
      - LISTEN_ADDR=0.0.0.0 
      - PGSQL_HOST=192.168.20.29 
      - PGSQL_USER=faraday_postgresql 
      - PGSQL_PASSWD=/run/secrets/pgsql_passwd 
      - PGSQL_DBNAME=faraday 
    secrets: 
      - pgsql_passwd 
    ports: 
      - 5985:5985 
    volumes: 
      - ~/.faraday/doc:/faraday-license 
      - ~/.faraday/storage:/faraday-storage 
    deploy: 
      replicas: 1 
      placement: 
        constraints: [node.role == manager] 
secrets: 
  pgsql_passwd: 
    external: true
```

Deploy:

```
    $ docker stack deploy -c docker-compose.yml faraday
```

Check service

```
    $ docker service ls
    $ docker service logs faraday_server
```

#### Web UI

Once Faraday Server is running you'll have to obtain the container's IP address. For this, run:

```
    $ docker inspect $(docker ps -lq) | grep \"IPAddress
    [output]
            "IPAddress": "172.17.0.2",
                    "IPAddress": "172.17.0.2",

```
Now you can direct your browser to `http://172.17.0.2:5985/_ui/`