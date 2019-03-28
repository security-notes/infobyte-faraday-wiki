This installation is intended for our commercial version of Faraday. For our community version, please check this [installation guide](https://github.com/infobyte/faraday/wiki/Installation-Docker)

Once you have downloaded our image from [infobytesec portal](portal.faradaysec.com) you'll need to load it in docker:

```
    $ docker load -i <path to image tar file>
```

Check Image

```
    $ docker image ls | grep faraday
```

Starting Up Faraday

This image can be run as a service or as a standalone container. Both runs Faraday Server. You will note that we used two volumes /faraday-license and /faraday-storage for the license and storage respectively and environment variables for faraday configuration.

You'll need to customize the following variables depending on your installation config.

      - PGSQL_HOST=192.168.20.29
      - PGSQL_USER=faraday_postgresql
      - PGSQL_PASSWD=mypgsqlpassword
      - PGSQL_DBNAME=faraday
      - LISTEN_ADDR=0.0.0.0

For license and storage current user's ~/.faraday/doc and ~/.faraday/storage folders are mounted by default. In case you have a different installation please replace them with proper ones in

```
    $ docker run \
    ....
    -v path_to_my_doc_folder:/faraday-license \
    -v path_to_my_storage_folder:/faraday-storage \
    ....
```
    or

```
    $ vim docker-compose.yml

    version: '3.7'

    services:
      ...
      volumes:
        - path_to_my_doc_folder:/faraday-license
        - path_to_my_storage_folde:/faraday-storage
      ...
```
Running image as a service, credentials can be configured with docker secrets or plain text

With secrets (default):

The simplest way to create a secret is reading from standard input but you should take care of bash history.

```
    $ printf mypgsqlpassword | docker secret create pgsql_passwd -
```

Edit docker-compose.yml and set:

```
    $ vim docker-compose.yml

    version: '3.7'

    services:
      ...
      environment:
        - PGSQL_PASSWD=/run/secrets/pgsql_passwd  
      ...
```
      
For more advanced examples about secrets check [docker web page](https://docs.docker.com/engine/swarm/secrets/#intermediate-example-use-secrets-with-a-nginx-service)

## Running Faraday as a standalone container

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

## Runnig Faraday as a service:

Initialize Swarm

```
    $ docker swarm init
```

In case you have more than one ip addr configured in your machine you have to specify which one to use.

```
    $ docker swarm init --advertise-addr=192.168.20.29
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

##### Web UI

Now to obtain the container's IP address run:

```
    $ docker inspect $(docker ps -lq) | grep \"IPAddress
```
For the purpose of this guide lets use `172.17.0.2`.

Direct the browser to `http://172.17.0.2:5985/_ui/`
