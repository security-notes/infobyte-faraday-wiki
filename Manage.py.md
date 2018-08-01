With **Faraday V3**, we released a new Backend feature.

![](https://raw.githubusercontent.com/wiki/infobyte/faraday/images/backend/Option-view.png)

## Available commands explained:

### create_tables
This command allows the user to manually create a table on Faraday's database. It would come in handly if something in the _initdb_ command fails for example.

### createsuperuser
The name says it all! This is the way to create a new admin user through command line.

### database_schema
This will print a PNG image with Faraday's internal working scheme.

### import_from_couchdb
Before you run this command you should make sure of two things:
1) CouchDB is running
2) PostgreSQL is running
This commmand will triger a script that goes into you server.ini file located in .faraday/config and check if you have credentials set up under the [couchdb] section. If you do then try to login with those credentials and if it succeed, it will extract all your CouchDB data and import it into our new PostgreSQL database.

### initdb
This command needs to be executed **only** at the moment of Faraday's installation. It will create the tables of the database, Faraday's user among other things.

If you try to execute this a second time it will indeed fail.

**Warning:** Please do not lose the random password that this command will print on the screen. It will be necessary to login into Faraday.

### show_urls
This will print a list of all the URLs available to communicate with our API Rest. 

### sql_shell
This will open a PostgreSQL shell already configured with Faraday's user and configuration.

### status_check
This command will check the state in which Faraday is. It checks that:

* PostgreSQL is running,
* Faraday Server and Client are running,
* the configuration is okay,
* the dependencies are installed.

You can run this command with the following parameters:

```
--check_postgresql

--check_faraday

--check_dependencies

--check_config
```
