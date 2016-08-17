### Faraday Server
If you are running CouchDB using HTTPS you need to configure Faraday Server to allow incoming HTTPS connections. To do this, first set CouchDB to listen on a new port, for example **6985**.

Now you must configure Faraday Server to start accepting HTTPS connections. Edit ```server/default.ini``` section ```[ssl]``` and set ```port``` to match CouchDB's previous SSL port and in section ```[couchdb]``` set ```ssl_port``` to the current one. ```certificate``` and ```keyfile``` in section ```[ssl]``` should match with the ones set in CouchDB configuration.

### CouchDB
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
