Download tar image from our portal

Load Image:
```
    $ docker load -i <path to image tar file>
```

Check Image
`
    $ docker image ls | grep faraday
`

##### Starting up Faraday

Both (standalone/service) runs Faraday Server. Note that we used volumes, for the license and for the storage directory, and environment variables for postgres and faraday server listen address configuration.

You'll need to customize the following variables depending on your installation config.

      - PGSQL_HOST=192.168.20.29
      - PGSQL_USER=faraday_postgresql
      - PGSQL_PASSWD=mypgsqlpassword
      - PGSQL_DBNAME=faraday
      - LISTEN_ADDR=0.0.0.0

For license and storage current user's ~/.faraday/doc and ~/.faraday/storage folders are mounted by default. In case you have a different installation please replace them with proper ones in

    -v ~/.faraday/doc:/faraday-license \
    -v ~/.faraday/storage:/faraday-storage \

    ...

    volumes:
      - ~/.faraday/doc:/faraday-license
      - ~/.faraday/storage:/faraday-storage

Running as service, credentials can be configured with docker secrets or plain text

With secrets (default):

The simplest way to create a secret is reading from standard input but you should take care of bash history.

```
   $ printf mypgsqlpassword | docker secret create pgsql_passwd -
```

Edit docker-compose.yml and set:

`  - PGSQL_PASSWD=/run/secrets/pgsql_passwd  `
      
For more advanced examples about secrets check [docker web page](https://docs.docker.com/engine/swarm/secrets/#intermediate-example-use-secrets-with-a-nginx-service)

Run standalone:
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
`
     $ docker container ls
`
Run as service:

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
`
     $ docker service ls
     $ docker service logs faraday_server
`

##### Web UI

Now to obtain the container's IP address run:
```
    $ docker inspect $(docker ps -lq) | grep \"IPAddress
```
For the purpose of this guide lets use `172.17.0.2`.

Direct the browser to `http://172.17.0.2:5985/_ui/`
