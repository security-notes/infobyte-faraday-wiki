Faraday actually consists of two tools; **Faraday Client** and **Faraday Server**. These can run on the same host or not, depending on your needs. Also, to persist all your data Faraday uses CouchDB.

The recommended approach for first time users is performing a single Faraday installation in an Ubuntu Linux. This means using the same machine for both the client and the server. For the community version, this is as simple as:

```
$ ./install.sh
$ ./faraday-server.py
$ ./faraday.py
```

If you were already using Faraday before the release of version 2.0, follow the [installation guide for the server](https://github.com/infobyte/faraday/wiki/Installation-server) and then refer to the [Setup](#setup) section of this page.

### Installation

Keep in mind that Faraday won't install CouchDB for you, you must install it [using the official CouchDB documentation](http://docs.couchdb.org/en/1.6.1/install).

**Beware! Faraday doesn't support CouchDB 2.0, use CouchDB 1.6!**

Once CouchDB is running [install the server](https://github.com/infobyte/faraday/wiki/Installation-server) and then [install the client](https://github.com/infobyte/faraday/wiki/Installation-client).

As of Faraday version 2.0 the server is required for both the community and the commercial versions.

<a name="setup"></a>
### Setup

Faraday Server needs to communicate to Couch Databases to function. By default, the server will listen on port 5985. You may need to edit ```user``` and ```password``` on ```~/.faraday/config/server.ini``` in case you have set up an admin account on your CouchDB. Remember that if you do add a ```user``` to the config file, its role **must be** admin.

Now you need to configure every Faraday instance so it can connect to the server.

* If you're using the GTK interface click on the Preferences icon ![](https://raw.github.com/wiki/infobyte/faraday/images/gtk-preferences-icon.png) and fill in the server URL, for example **http://127.0.0.1:5985**

![](https://raw.github.com/wiki/infobyte/faraday/images/gtk-preferences-dialog.png)

* If you are using the ***--gui=no-gui*** option

Edit the file: `~/.faraday/config/user.xml`
And search for the following **couch_uri** tag and set it to the server URL, for example:

`<couch_uri>http://127.0.0.1:5985</couch_uri>`

And now you are ready to go!

If you wish to use SSL use our [SSL guide](https://github.com/infobyte/faraday/wiki/SSL).

Run `./faraday-server.py` to run the server and then `./faraday.py` to start the client. Enjoy!

#### How do I bind Faraday to 0.0.0.0?
Just go to ```~/.faraday/config/server.ini``` and inside the ```[faraday-server]``` section write:

`bind_address=0.0.0.0`

Restart Faraday Server if you had it running.

That's it!

### Authentication
#### Commercial

You can create different types of users through the web UI. Those users can login though the same web UI or though a Faraday client using the --login flag (Faraday will ask for the credentials later)

#### Community
You can use the CouchDB ***_utils*** interface (located in `http://127.0.0.1:5984/_utils/`) to create administrator users, and then edit the CouchDB url in your instance with the user's credentials. For example: `http://admin:faradaypassword@192.168.1.254:5985/`
