Saving backups is always a good choice, whether it is to keep data safe or to share with others.

In order to create a backup for a specific workspace follow these steps:

1. Turn off the Faraday Client, Faraday Server.
2. Assuming `{dbname}` as the name of the database you wish to backup, execute the PostgresQL tool:
```
pg_dump dbname > outfile
```
3. Restart the Faraday Server and Client (in that order)

To restore a previously created backup turn everything off and execute:


```
psql dbname < infile

```

Check [more information about PostgreSQL](https://www.postgresql.org/docs/9.1/static/backup-dump.html) backups if you need more help.