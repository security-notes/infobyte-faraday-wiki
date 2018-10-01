## Backup Database

Saving backups is always a good choice, whether it is to keep data safe or to share with others.

In order to create a backup for your database, follow these steps:

1. Turn off the Faraday Client and Faraday Server.

2. In order to backup your Faraday database, execute the PostgreSQL tool:
```
pg_dump faraday > backup_file
```
- Where _faraday_ is the default name of Faraday's database and _backup_file_ is the file where the pg_dump will save your data.

3. Restart the Faraday Server and Faraday Client (in that order).

To restore a previously created backup turn again Faraday Client and Faraday Server off and execute:
```
psql faraday < backup_file
```

Remember: To restore the back you need to have the database empty.

Check [more information about PostgreSQL](https://www.postgresql.org/docs/9.1/static/backup-dump.html) backups if you need more help.