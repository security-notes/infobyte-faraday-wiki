## Workspace replication

There are some situations in which you might want to replicate your workspace to another CouchDB instance. For example:

1. Your team is working with a workspace in your internal CouchDB instance and you want to replicate it to a public instance so a client can see it.
2. You work in a local CouchDB and then you want to replicate your daily work to a central CouchDB instance so the entire team can see what you've done.

So, let's say we want to replicate a workspace in our local CouchDB instance to an internal CouchDB instance.                                                                                                                                                                    

```
Workspace name: ws1
                                                                                                                                                                                                                                                              
Local CouchDB IP: 127.0.0.1
User: user1
Password: pass1
                                                                                                                                                                                                                                                                                 
Internal CouchDB IP: 192.168.1.2
User: user2
Password:pass2
```                                                                                                                                                                                                                                                                              

NOTE: It's important to use the same workspace name in both CouchDB instances.                                                                                                                                                                                                   

We have to options to do the replication:                                                                                                                                                                                                                                        

### Using curl                                                                                                                                                                                                                                                                   
```                                                                                                                                                                                                                                                                              
curl 'http://user2:pass2@192.168.1.2:5984/_replicate' -X POST -H "Content-Type: application/json" --data-binary ' {"source":"http://user1:pass1@127.0.0.1:5984/ws1/", "target":"ws1", "create_target": true }'                                                                   
```                                                                                                                                                                                                                                                                              

NOTE: If the database is already created in the internal couchDB, you don't need to send the "create_target" option.                                                                                                                                                             

### Using CouchDB replicator                                                                                                                                                                                                                                                     

If we want to to the same thing through the CouchDB web interface, you need to create the target database first. In our example, we should go to 'http://192.168.1.2:5984/_utils', and create a database called 'ws1'.                                                           

Then, we go to 'http://127.0.0.1:5984/_utils/replicator.html', and fill the input accordingly.

```
Local database: ws1
Remote database: http://user2:user2@192.168.1.210:5984/ws1/
```

Click on the "Replicate" button, and that's it.

![](https://raw.github.com/wiki/infobyte/faraday/images/workspace_replication_replicator.png)



