Saving backups is always a good choice, wether it is to keep data safe or to share with others.

In order to create a backup for a specific workspace follow these steps:

1. Turn off the Faraday Client, Faraday Server and CouchDB
2. Assuming `[workspace_name]` as the name of the workspace you wish to backup, copy the CouchDB files for the Workspace located in `/var/lib/couchdb` to a secure location
```
cp /var/lib/couchdb/[workspace_name].couch /secure/location
cp /var/lib/couchdb/.[workspace_name]_design /secure/location
```
3. Restart CouchDB, the Faraday Server and Client (in that order)

To restore a previously created backup turn everything off and copy both files back to `/var/lib/couchdb`.