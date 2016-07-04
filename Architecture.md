Front end
--
Faraday was developed in Python, GTK, QT3 [Deprecated]

Backend
--
We rely on the popular no-sql CouchDB  database for the data storage layer. 

CouchDB Serves for the following purposes:
* Data storage
* Data replication and sharing between multiple Faraday instances
* Data transformations engine ([read more about reports](tuvieja))

Two topologies are admitted (at this version) in the configuration, Server Centric and Replicated

Server Centric approach
===
Every user use the same CouchDB database. This is a Server centric approach for the data sharing process.
![Sincronize_2](https://raw.github.com/wiki/infobyte/faraday/images/synchronize_2.png)

Distributed CouchDBs with replication
===
Every user have a own local CouchDB and replicate with a centralize CouchDB Server. Allowing to commit your recently gathered information despite the Server going offline.
![Sincronize_1](https://raw.github.com/wiki/infobyte/faraday/images/synchronize_1.png)

Both topologies combine real-time change notifications with instant transactions to provide instant feedback in the team.

Plugins
--
The following diagram explains the plugins architecture:
![Plugin_Controller](https://raw.github.com/wiki/infobyte/faraday/images/plugin_controller.png)