Faraday uses CouchDB >= 1.2.0.

The first step is to edit CouchDB config file located in /etc/couchdb/local.ini and set bind_address to the required IP  
Restart CouchDB as follows  
```
$ sudo service couchdb restart
```
You have two kind of configuration:  
1) Every user use the same CouchDB database.  
Go to Edit->Server Connection to point to the required master for example http://192.168.10.210:5984/.  

![](https://raw.github.com/wiki/infobyte/faraday/images/Couchdb_conf.png)

2) Every user have a own local CouchDB and replicate with a centralize CouchDB Server.  
**NOTE:** If you like to use this configuration check that all CouchDB use almost the version 1.2.0 because some distributions have old version that have some problems.  

Go to Edit->Server Connection to point to the required master for example http://127.0.0.1:5984/ and replication database http://192.168.10.210:5984/.  

![](https://raw.github.com/wiki/infobyte/faraday/images/Couchdb_conf2.png)

Multiple replication is available, separating each IP with a semicolon. For example, for master 192.168.33.10 and replicating to 192.168.10.110 and 192.168.10.210 use:  

Replics: http://192.168.33.12:5984/;http://192.168.33.12:5984/


If you are using the --gui=no-gui option

1) Edit the following file: `~/.faraday/config/user.xml`

2) Search for the following tags and set them, normally is like this:

`<last_workspace>workspace</last_workspace>`

`<couch_uri>http://127.0.0.1:5984</couch_uri>`

3) Start couchdb: `sudo service couchdb start`

4) start faraday by running: `./faraday.py`

5) Using a browser go to http://127.0.0.1:5984/reports/_design/reports/index.html (if you are using couch in a different IP, set it to the right address)