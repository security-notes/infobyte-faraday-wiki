The CouchDB version supported by Faraday is 1.7.1.

In some distros the CouchDB package is either out of date or a newer incompatible version. We recommend using CouchDB in a Docker Container.

To install Docker checkout the official documentation: https://docs.docker.com/engine/installation/

The official CouchDB image can be found here: https://hub.docker.com/_/couchdb/

To get the version compatible with Faraday run

```
$ docker pull couchdb:1.7.1
```

In order to persist data, two directories must be created before running the container, one for the config files and one for the data. 

For example

```
$ mkdir -p /path/to/couchdb/conf
$ mkdir -p /path/to/couchdb/data
```

Make sure these two dirs exist before firing up the image like so

```
$ docker run --name couchdb_faraday -v /path/to/couchdb/conf:/usr/local/etc/couchdb/local.d -v /path/to/couchdb/data:/usr/local/var/lib/couchdb -p 5984:5984 -d couchdb:1.7.1
```

To stop the container run:

```
$ docker stop couchdb_faraday
```