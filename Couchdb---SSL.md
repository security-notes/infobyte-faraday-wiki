1) Enable the httpsd daemon by adding the following line to your local.ini or local_dev.ini (newly generated files include this setting but commented out);

    [daemons]
    httpsd = {couch_httpd, start_link, [https]}
2) tell CouchDB about your SSL server keys (PEM encoded);

    [ssl]
    cert_file = /full/path/to/server_cert.pem
    key_file = /full/path/to/server_key.pem
    password = keypassword
    ;port = 6984

Example self generation certificates

    openssl req -x509 -newkey rsa:2048 -keyout server_key.pem -out server_cert.pem -days XXX

On windows, the path format needs to be one of the following:
* fully specified windows path with slashes inverted, and spaces escaped: c:/program\files/couchdb/etc/config/couchdb/<your.pem>
* unix-style path, assuming that the root / will be the root of the drive that couchdb is installed to: /program\ files/couchdb/etc/config/couchdb/<your.pem>
* relative path, to the %COUCH%/bin folder: ../etc/couchdb/<your.pem>

3) Restart CouchDB.
CouchDB should now accept SSL connections on, by default, port 6984.

Troubleshooting
---
To ensure that the issue is not with your certificates, test from the command line using

    curl -k -v https://127.0.0.1:6984/
You can test your certificates separately using:

    openssl s_server -key <keyfile> -cert <certfile> -www
    curl -k -v https://localhost:4433/

Configure Faraday:
---
Go to Edit->Server Connection to point to the required master and replication databases.  
Multiple replication is available, separating each IP with a semicolon. For example, for master 192.168.33.10 and replicating to 192.168.33.12 and 192.168.33.11 use:  
CouchDB URL: https://192.168.33.10:6984/