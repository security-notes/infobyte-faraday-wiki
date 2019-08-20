This installation is intended for our commercial version of Faraday. For our community version, please check this [installation guide](https://github.com/infobyte/faraday/wiki/Installation-Docker-Community)

### Loading Image

Once you have downloaded our image file from [faraday portal](http://portal.faradaysec.com) you'll need to load it in docker:

```
    $ docker load -i <path to image tar.gz file>
```

Check Image

```
    $ docker image ls | grep faraday
```

### Configuration

This image can be run as a service or as a standalone container. Both run Faraday Server without PostgreSQL. You will note that we have created `/faraday-license`, `/faraday-storage` and `/faraday-config` volumes (for mount your license , storage and configuration). We have also created environment variables for Faraday configuration in case you don't mount a config volume.

We will get more in detail of these volumes and environment variables:

#### Volumes

Current user's ~/.faraday/doc, ~/.faraday/storage and ~/.faraday/config folders are mounted by default. In case you have these folders in a different place, please replace them with proper path at the moment you run Faraday whether as a standalone container or as a service:

```
    /path/to/my_doc_folder:/faraday-license 
    /path/to/my_storage_folder:/faraday-storage 
    /path/to/my_storage_folder:/faraday-config
```
Example:
```
    [Running Faraday as a standalone container]
    $ docker run \
    ....
    -v /path/to/my_doc_folder:/faraday-license \
    -v /path/to/my_storage_folder:/faraday-storage \
    -v /path/to/my_config_folder:/faraday-config
    ....
```
```
    [Running Faraday as a service]
    $ vim docker-compose.yml

    version: '3.7'

    services:
      ...
      volumes:
        - /path/to/my_doc_folder:/faraday-license
        - /path/to/my_storage_folder:/faraday-storage
        - /path/to/my_config_folder:/faraday-config
      ...
```

We will get more in details about this configuration below. 

#### Enviroment Variables

In case you don't have a configuration file you'll need to set some environment variables. These come with default values so you'll need to customize some or all of them depending on your installation config. 

```

      - PGSQL_HOST=172.2.0.1 # PostgreSQL server host.
      - PGSQL_USER=faraday_postgresql # PostgreSQL user
      - PGSQL_PASSWD=mypgsqlpassword # PostgreSQL user's password.
      - PGSQL_DBNAME=faraday # Faraday's database name

```

### Running Faraday

Now that we have learn about the volumes and the enviroment variables above, let's run Faraday assuming we want to connect into PostreSQL's address _192.168.20.29_ and that we have located Faraday's config folder in its default location: ~/.faraday.

#### As a standalone container

Run the following command specifying the correct information:

With environment variables
 ```
    $ docker run \
      -v ~/.faraday/doc:/faraday-license \
      -v ~/.faraday/storage:/faraday-storage \
      -p 5985:5985 \
      -e PGSQL_HOST='192.168.20.29' \
      -e PGSQL_PASSWD='mypgsqlpassword' \
      -e LISTEN_ADDR='0.0.0.0' \
      faraday:c_v3.7
 ```
With config volume mounted
 ```
    $ docker run \
      -v ~/.faraday/doc:/faraday-license \
      -v ~/.faraday/storage:/faraday-storage \
      -v ~/.faraday/config:/faraday-config \
      -p 5985:5985 \
      faraday:c_v3.7
 ```

To check container, run the following command:

```
    $ docker container ls
```
As you can see, Faraday Server is running in port 5985.

#### As a service

**1.** Initialize a Swarm:

```
    $ docker swarm init
```

In case you have more than one ip addr configured in your machine you have to specify which one to use.

```
    $ docker swarm init --advertise-addr=192.168.20.29
```

**2.** Docker Compose File:

Now, you need to create a **docker-compose.yml** file. You can use this docker-compose as example:


With environment variables
```
version: '3.7' 
 
services: 
  server: 
    image: faraday:3.8.1 
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
When Faraday runs as a service, PGSQL_PASSWD can be configured with docker secrets (default in docker-compose.yml). The simplest way to create a secret is reading from standard input (you should take care of bash history).

```
    $ printf mypgsqlpassword | docker secret create pgsql_passwd -
```

Once you have created the secret, edit you docker-compose.yml and set:

```
    $ vim docker-compose.yml

    version: '3.7'

    services:
      ...
      environment:
        - PGSQL_PASSWD=/run/secrets/pgsql_passwd  
      ...
```
      
For more information about secrets, check [docker web page](https://docs.docker.com/engine/swarm/secrets/)

With config volume mounted
```
version: '3.7' 
 
services: 
  server: 
    image: faraday:c_v3.7 
    ports: 
      - 5985:5985 
    volumes: 
      - ~/.faraday/doc:/faraday-license 
      - ~/.faraday/storage:/faraday-storage 
      - ~/.faraday/config:/faraday-config 
    deploy: 
      replicas: 1 
      placement: 
        constraints: [node.role == manager] 
```



**3.** Deploy:

Once you are done setting up your docker-compile.yml file, let's deploy by running the following command:

```
    $ docker stack deploy -c docker-compose.yml faraday
```

**4.** Check service:

To check the service, run the following command:

```
    $ docker service ls
    $ docker service logs faraday_server
```

### Web UI

Once Faraday Server is running you'll have to obtain the container's IP address. For this, run:

```
    $ docker inspect $(docker ps -lq) | grep \"IPAddress
```
This command will throw the following output:
```
            "IPAddress": "172.17.0.2",
                    "IPAddress": "172.17.0.2",
```

Now you can direct your browser to `http://172.17.0.2:5985/_ui/`