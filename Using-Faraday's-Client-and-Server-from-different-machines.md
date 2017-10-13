## **Exposing the Server**

If you wish to access the Server from a different box you need to first expose the service. In order to do so, edit the server configuration file and set the ```bind_address param``` to 0.0.0.0.
Edit the file located in ```~/.faraday/config/server.ini``` and under the section ```[faraday-server```] set the param, it should look something like this:
Then restart the server if you had it running and reload your browser in case you were already trying to access the Web UI form a different IP.

## ***Connecting to a Server from a different machine***

For the purpose of this guide lets say you have the server running on a machine with IP 192.168.0.10.

***WebUI***

If you wish to connect to the Web UI you just need to point your browser to `http://192.168.0.10:5985/_ui`

**GTK**

Once you’ve followed the previous steps on exposing the *<a>server* is time make the client listen to your Server.
Edit the file located in `~/.faraday/config/user.xml`, change the instance <couch_uri> with the IP where your Faraday server is running, it should look something like this:

Then restart the server if you had it running and reload your browser in case you were already trying to access the Web UI form a different IP.

## ***Connecting to a Server from a different machine***

For the purpose of this guide lets say you have the server running on a machine with IP 192.168.0.10.

***WebUI***

If you wish to connect to the Web UI you just need to point your browser to `http://192.168.0.10:5985/_ui`

**GTK**

Once you’ve followed the previous steps on exposing the *<a>server* is time make the client listen to your Server.
Edit the file located in `~/.faraday/config/user.xml`, change the instance <couch_uri> with the IP where your Faraday server is running, it should look something like this:


