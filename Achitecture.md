Faraday is composed by the Faraday Server and the Faraday Client with a Server 
Centric approach. The client talks almost exclusively with the server, and the 
server is used to syncronize the state of the program between instances.

For the moment, we use the popular No-SQL database CouchDB to provide a few
key features needed to improve your workflow, but we're working on replicating
those on Faraday Server to simplify the setup.

CouchDB Serves for the following purposes:

* Partial storage
* Notifications feed
* User management 

The server provides everything else using a REST API to make queries over 
sqlite DBs structured according to our Host/Services/Vulnerability model. Our
server acts as a web server build upon Twisted.

It is important to remember that, as said, CouchDB will totally be replaced by
our Faraday Server in the very near future. All this changes are transparent
to the user, nevertheless.

Server Centric approach
===
Every user connects to the same Faraday server, which is itself connected to a CouchDB database.
This permits seamless data sharing and syncronization.
![Sincronize_2](https://raw.github.com/wiki/infobyte/faraday/images/Faraday-Server-Comm.png)


Plugins
===
The following diagram explains the plugins architecture:
![Plugin_Controller](https://raw.github.com/wiki/infobyte/faraday/images/plugin_controller.png)
