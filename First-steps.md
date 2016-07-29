Faraday actually consists of two tools; Faraday Client and Faraday Server. These can run on the same host or not, depending on your needs. Also, to persist all your data Faraday uses CouchDB.

The recommended approach for first time users is performing a single Faraday installation in an Ubuntu Linux. This means using the same machine for both the client and the server.

### Installation

Keep in mind that Faraday won't install CouchDB for you, you must install it [using the official CouchDB documentation](http://docs.couchdb.org/en/1.6.1/install).

Once CouchDB is running [install the server](https://github.com/infobyte/faraday/wiki/Installation-server) and then [install the client](https://github.com/infobyte/faraday/wiki/Installation-server).

As of Faraday version 2.0 the server is required for both the community and the commercial versions.

### Setup

Faraday Server needs to comunicate to Couch Databases to function.

Edit CouchDB configuration file. To do that, run ```couchdb -c``` to identify it and then edit it to change CouchDB `port` and `bind_address` in section ```[httpd]```. Set bind_address to the IP you want for CouchBD and port to **5985**.

Next edit ```~/.faraday/config/server.ini``` and change Faraday Server port to **5984** in section ```[faraday_server]``` and set a new port for CouchDB in section ```[couch-db]``` (by default the server will expect CouchDB to use **5985**).

Restart CouchDB, it should be running in your new IP and port.

Now you need to configure every Faraday instance so it can connect to the server.

* If you're using the GTK interface click on the Preferences icon ![](https://raw.github.com/wiki/infobyte/faraday/images/gtk-preferences-icon.png) and fill in the server URL, for example **http://127.0.0.1:5984**

![](https://raw.github.com/wiki/infobyte/faraday/images/gtk-preferences-dialog.png)

* If you are using the --gui=no-gui option

Edit the file: `~/.faraday/config/user.xml`
And search for the following **couch_uri** tag and set it to the server URL, for example:

`<couch_uri>http://127.0.0.1:5984</couch_uri>`

And now you are ready to go!

If you wish to use SSL use our [SSL guide](https://github.com/infobyte/faraday/wiki/SSL).

Run `./faraday-server.py` to run the server and then `./faraday.py` to start the client. Enjoy!

### Authentication
#### Commercial

You can create different types of users through the web UI. Those users can login though the same web UI or though a Faraday client using the --login flag (Faraday will ask for the credentials later)

#### Community
You can use the couchdb _utils http://127.0.0.1:5984/_utils/ interface to create administrator users, and then edit the couchdb url in your instance with the user's credendials. For example: http://admin:faradaypassword@192.168.1.254:5984/