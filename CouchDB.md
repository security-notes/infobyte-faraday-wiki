### Basic setup

Edit CouchDB configuration file located in /etc/couchdb/local.ini and set bind_address to the required IP.
Then restart CouchDB as follows:
```
$ sudo service couchdb restart
```

### Configure your instances
Now you need to configure every Faraday instance so it can connect to CouchDB.

* If you're using the Qt interface, go to Edit->Server Connection to point to server. For example; http://192.168.1.254:5984/

![](https://raw.github.com/wiki/infobyte/faraday/images/change_server.png)

* If you are using the --gui=no-gui option

Edit the file: `~/.faraday/config/user.xml`
And search for the following tags and set them, normally is like this:

`<last_workspace>workspace</last_workspace>`

`<couch_uri>http://127.0.0.1:5984</couch_uri>`

### Web UI
You can access the web UI going to http://[your_couch_ip]:5984/reports/_design/reports/index.html.
More information [here](https://github.com/infobyte/faraday/wiki/Usage#web-ui)

### SSL
1) Enable the httpsd daemon by adding the following line to your local.ini or local_dev.ini (newly generated files include this setting but commented out);
```
[daemons]
httpsd = {couch_httpd, start_link, [https]}
```
2) Tell CouchDB about your SSL server keys (PEM encoded);
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

#### Troubleshooting
To ensure that the issue is not with your certificates, test from the command line using
```
$ curl -k -v https://127.0.0.1:6984/
```
You can test your certificates separately using:
```
$ openssl s_server -key <keyfile> -cert <certfile> -www
```
#### Using the certificate in your Faraday instance
If you're using a valid certificate, you're good to go.

If not, run Faraday's launcher with a flag --cert is needed, where the path points to your certificate, NOT your key. This is a security workaround that allow users to use their own signed certificates.
```
./faraday.py --cert /etc/ssl/certs/server.crt
```

### Authentication
#### Commercial

You can create different types of users through the web UI. Those users can login though the same web UI or though a Faraday client using the --login flag (Faraday will ask for the credentials later)

#### Community
You can use the couchdb _utils interface to create administrator users, and then edit the couchdb url in your instance with the user's credendials. For example: http://admin:faradaypassword@192.168.1.254:5984/