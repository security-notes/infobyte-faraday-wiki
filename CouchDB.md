Faraday uses CouchDB >= 1.2.0.

The first step is to edit CouchDB config file located in /etc/couchdb/local.ini and set bind_address to the required IP.

Then restart CouchDB as follows:

```
$ sudo service couchdb restart
```
There are two different configuration schemas:

* **Every user uses the same CouchDB database**

Go to Edit->Server Connection to point to the required master. For example; http://192.168.10.210:5984/

![](https://raw.github.com/wiki/infobyte/faraday/images/Couchdb_conf.png)

* **Every user has its own local CouchDB and replicate to a centralized CouchDB Server**

**NOTE:** In order to make this work all the CouchDB instances must be greater or equal to v1.2.0. Some distributions have older buggy versions.

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

# SSL
1) Enable the httpsd daemon by adding the following line to your local.ini or local_dev.ini (newly generated files include this setting but commented out);
```
[daemons]
httpsd = {couch_httpd, start_link, [https]}
```
2) tell CouchDB about your SSL server keys (PEM encoded);
```
[ssl]
cert_file = /full/path/to/server_cert.pem
key_file = /full/path/to/server_key.pem
password = keypassword
;port = 6984
```
For information on *how to generate self singned certificates* you can read [Apache's FAQ on how to do this](https://cwiki.apache.org/confluence/pages/viewpage.action?pageId=48203146).

For more information on *path handling*:
On windows, the path format needs to be one of the following:
* fully specified windows path with slashes inverted, and spaces escaped: c:/program\\files/couchdb/etc/config/couchdb/<your.pem>
* unix-style path, assuming that the root / will be the root of the drive that couchdb is installed to: /program\ files/couchdb/etc/config/couchdb/<your.pem>
* relative path, to the %COUCH%/bin folder: ../etc/couchdb/<your.pem>

3) Restart CouchDB.
CouchDB should now accept SSL connections on, by default, port 6984.

Troubleshooting
---
To ensure that the issue is not with your certificates, test from the command line using
```
$ curl -k -v https://127.0.0.1:6984/
```
You can test your certificates separately using:
```
$ openssl s_server -key <keyfile> -cert <certfile> -www
$ curl -k -v https://127.0.0.1:6984/
```
Configure Faraday
---
1) Running Faraday's launcher with a flag --cert is needed, where the path points to your certificate, NOT your key. This is a security workaround that allow users to use their own signed certificates.
```
./faraday.py --cert /etc/ssl/certs/server.crt
```

2) Then go to Edit->Server Connection to point to the required master and replication databases.  
Multiple replication is available, separating each IP with a semicolon. For example, for master 192.168.33.10.
```
CouchDB URL: https://192.168.33.10:6984/
```

# Authentication
1) Uncomment the next line to trigger basic-auth popup on unauthorized requests.

    [httpd]
    WWW-Authenticate = Basic realm="administrator"
2) Required valid user.

    [couch_httpd_auth]
    require_valid_user = true
3) Configure users

    [admins]
    admin:faradaypassword


Restart CouchDB services

Configure Faraday
---
Go to Edit->Server Connection to point to the required master and replication databases.  
CouchDB URL: http://admin:faradaypassword@192.168.33.10:5984/