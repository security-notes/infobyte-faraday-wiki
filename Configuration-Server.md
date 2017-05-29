Faraday Server needs to communicate to Couch Databases to function. By default, the server will listen on port **5985**. You may need to edit `user` and `password` on `~/.faraday/config/server.ini` in case you have set up an admin account on your CouchDB.

### Commercial Server Configuration

Once you have installed the additional dependencies and CouchDB is running, you will need to execute the setup script, which will create the admin user with the configured password, and create a backup cronjob for CouchDB. Just execute the following command and answer the questions asked.

    $ sudo python2 setup-server.pyc

If you want more fine grained control over what the setup script does, you can see the available options by executing:

    $ python2 setup-server.pyc --help

If you want, you can upload the included CWE database to CouchDB to enable better searching and autocomplete features. To do so, you only need to execute the following command:

    $ ./helpers/pushCwe.py

You will be asked to pass as an argument the CouchDB URL so that a connection can be established.

After running the setup script run the server once using `python2 faraday-server.pyc` and don't worry if it fails.

Edit the file located in `~/.faraday/config/server.ini` and add the username and password created using the setup script in the `[couchdb]` section. Assuming the selected password is **password123**, the file should look something like:

```
[couchdb]
user=faraday
password=password123
```

### Corp Server Configuration

If you are running a Corp version an additional CouchDB config is necessary. Follow these steps to set it up:

1. Turn off Faraday Server (`./faraday-server.pyc --stop`)
1. Turn off CouchDB (`systemctl stop couchdb`)
1. Modify the file **local.ini** usually located in the path `/etc/couch/local.ini`
1. Add the following lines to the `[couch_httpd_auth]` part of that file

```
allow_persistent_cookies = true
timeout = 9999999
```

And then run CouchDB and Faraday Server again and you are all set!

### Authentication

#### Community

You can use the CouchDB ***_utils*** interface (located in `http://127.0.0.1:5984/_utils/`) to create administrator users, and then edit the CouchDB url in your instance with the users credentials. For example: `http://admin:faradaypassword@192.168.1.254:5985/`

#### Commercial

You can create different types of users through the web UI. Those users can login though the same web UI or though a Faraday client using the `--login` flag (Faraday will ask for the credentials later)

### How do I bind Faraday to `0.0.0.0`?

You will need to edit the server's configuration file: ```~/.faraday/config/server.ini```

Under the section ```[faraday-server]```, edit the following line:

    [faraday-server]
    ...
    bind_address=0.0.0.0

Then restart Faraday Server if you had it running and reload your browser.
