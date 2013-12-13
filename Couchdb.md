CouchDB configuration is necessary. Go to Edit->Server Connection to point to the required master and replication databases. 

Multiple replication is available, separating each IP with a semicolon. For example, for master 192.168.33.10 and replicating to 192.168.33.12 and 192.168.33.11 use:

CouchDB URL: http://192.168.33.10:5984/  
Replics: http://192.168.33.12:5984/;http://192.168.33.12:5984/

For this testing using only CouchDB URL will be fine.
CouchDB version: 