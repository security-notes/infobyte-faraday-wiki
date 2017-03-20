## Configuring the Server

Faraday Server needs to communicate to Couch Databases to function. By default, the server will listen on port **5985**. You may need to edit `user` and `password` on `~/.faraday/config/server.ini` in case you have set up an admin account on your CouchDB.

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
