Faraday is composed by the Faraday Server and the Faraday Client with a Server 
Centric approach. The client talks almost exclusively with the server, and the 
server is used to syncronize the state of the program between instances.

We use the popular SQL database PostgreSQL.

The server provides a REST API to make queries over the database, structured according to our Host/Services/Vulnerability model.

Server Centric approach
===
Every user connects to the same Faraday server, which is itself connected to a CouchDB database.
This permits seamless data sharing and syncronization.
![Sincronize_2](https://raw.github.com/wiki/infobyte/faraday/images/Faraday-Server-Comm.png)


Plugins
===
The following diagram explains the plugins architecture:
![Plugin_Controller](https://raw.github.com/wiki/infobyte/faraday/images/plugin_controller.png)
