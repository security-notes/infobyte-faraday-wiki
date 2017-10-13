## **Exposing the Server**

If you wish to access the Server from a different box you need to first expose the service. In order to do so, edit the server configuration file and set the ```bind_address param``` to 0.0.0.0.
Edit the file located in ```~/.faraday/config/server.ini``` and under the section ```[faraday-server```] set the param, it should look something like this:


