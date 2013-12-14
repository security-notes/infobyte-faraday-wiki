Faraday use CouchDB >= 1.2.0.

You have two kind of configuration:
1) Every user use the same CouchDB database.
Go to Edit->Server Connection to point to the required master for example http://192.168.10.210:5984/. 

![](https://raw.github.com/wiki/infobyte/faraday/images/Couchdb_conf.png)

2) Every user have a own local CouchDB and replicate with a centralize CouchDB Server.
Go to Edit->Server Connection to point to the required master for example http://127.0.0.1:5984/ and replication database http://192.168.10.210:5984/. 

![](https://raw.github.com/wiki/infobyte/faraday/images/Couchdb_conf2.png)

Multiple replication is available, separating each IP with a semicolon. For example, for master 192.168.33.10 and replicating to 192.168.10.110 and 192.168.10.210 use:

Replics: http://192.168.33.12:5984/;http://192.168.33.12:5984/
