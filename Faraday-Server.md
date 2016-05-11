[- Commercial version -](https://www.faradaysec.com/#download)

The Faraday Server is made to manage the CouchDB Database. This lets the user access all the information in one centralized platform, run periodic backups and make automated reports.

### Requirements

`# cd faraday`<br>
`/faraday# cat requirements_server.txt`

distribute==0.7.3<br>
python-docx==0.7.6<br>
docxtpl==0.8.2<br>
six==1.9.0<br>
matplotlib==1.4.2<br>

### Start-up Configuration

To begin the initial setup the user needs to run the executable **./setup_server.sh**

`/faraday# ./setup_server.sh`

![](https://raw.github.com/wiki/infobyte/faraday/images/faraday_setup_libraries.png)

`[+] Install required libraries? [y/N]`

* Install the necessary libraries to execute the application.These can be found in the folder, requirements_server.txt.

`[+] Install backup crontab? [y/N]`

* Install a batch process to run periodic backups of the database.

`[+] Install Report Generation crontab? [y/N]`

* Install a batch process to make automated reports.

`[+] Faraday server is full configured`

<a name="proxy"></a>
### Proxy Server

For the time being this is an experimental feature that enables JIRA integration so it's only necessary in case you wish to do that.

In order to use Faraday Proxy Server you must first configure it.

Edit ```server/default.ini``` and change Faraday Server's port to the one being used by CouchDB in section ```[faraday_server]``` and set a new port for CouchDB in section ```[couch-db]``` (i.e.: 5985).

After that, we need to change CouchDB port. To do that, run ```couchdb -c``` to identify its configuration file. Once you identified it, edit it and change CouchDB port in section ```[httpd]``` to the one set previously (i.e.: 5985).

Restart CouchDB and you are ready to go! Run the following command to start Faraday Proxy Server:

```
./faraday-server.pyc
```

##### HTTPS support

If you are running CouchDB using HTTPS you need to configure Faraday Proxy Server to allow incoming HTTPS connections. To do this, first set CouchDB to listen on a new port, for example **6985**.

Now you must configure Faraday Proxy Server to start accepting HTTPS connections. Edit ```server/default.ini``` section ```[ssl]``` and set ```port``` to match CouchDB's previous SSL port and in section ```[couchdb]``` set ```ssl_port``` to the current one. ```certificate``` and ```keyfile``` in section ```[ssl]``` should match with the ones set in CouchDB configuration.