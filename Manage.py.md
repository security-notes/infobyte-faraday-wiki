With Faraday V3 we released a new Backend feature.

# The manage.py!

![](https://raw.githubusercontent.com/wiki/infobyte/faraday/images/manage.py/Option-view.png)

Usage: manage.py [OPTIONS] COMMAND [ARGS]...

### Avaibable commands explained:

## create_tables
This command allows the user to manually create a table on Faraday's Database. It would come in handly if something in the initdb fails for example.

## createsuperuser
The name says it all! This is the way to create a new admin user through command line.

## database_schema
This will Print a png image with Faraday's internal working Scheme.

## import_from_couchdb
Before you run this command you should make sure of two things:
1) Couchdb is running
2) Postgresql is running
This commmand will triger a script that goes into you server.ini file located in .faraday/config and check if you have credentials set up under the [couchdb] section. If you do then try to login with those credentials and if successfull extract all your couchdb Data and import it into our new Postgresql Database.

## initdb
This comand needs to only be executed when installing Faraday. It Will create the tables of the database, create the Faraday user among other thing.
If you try to execute this a second time it will indeed fail.
Warning: Please do not lose the ramdom password that this command will print on the screen. It will be necesary to log in into Faraday.

## show_urls
This will print a list of all the URL available to communicate will our API Rest. 

## sql_shell
This will open a postgres sql shell, already automatically configured with Faradays user and configuration.


## status_check
This command will check a the state in which Faraday is.
Checks that:
* postgresql is running
* Faraday server and client are running
* the configuration is okay
* the dependencies are installed

You can run this command with this parameters:

--check_postgresql

--check_faraday

--check_dependencies

--check_config
