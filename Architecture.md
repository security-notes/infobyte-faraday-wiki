Front end
--
Faraday was developed in Python and QT3
Backend
--
In the backend we are using CouchDB for replication and data storage.

You have two kind of configuration:

1) Every user use the same CouchDB database.
![Sincronize_2](https://raw.github.com/wiki/infobyte/faraday/images/synchronize_2.png)

2) Every user have a own local CouchDB and replicate with a centralize CouchDB Server.
![Sincronize_1](https://raw.github.com/wiki/infobyte/faraday/images/synchronize_1.png)

