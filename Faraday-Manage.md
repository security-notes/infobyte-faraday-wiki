Faraday Manage is a backend tool that helps us administrate Faraday's configuration. 

To use Faraday Manage, you can run it as follow:

```
$ faraday-manage COMMAND
```

If you run only `faraday-manage`, it will list you all the available commands.

![](https://raw.githubusercontent.com/wiki/infobyte/faraday/images/backend/Option-view.png)

### Available Commands

#### add-custom-field
This command allows you to create Custom Fields from the terminal. For more information about Custom Fields, you can see their [wiki page](https://github.com/infobyte/faraday/wiki/Custom-Fields)

#### change-password
It allows you to change your user's password

#### create-superuser
The name says it all! This is the way to create a new admin user through the command line.

#### create-tables
This command allows the user to manually create a table on Faraday's database. It would come in handy if something in the _initdb_ command fails for example.

#### database-schema
This will print a PNG image with Faraday's internal working scheme.

#### delete-custom-field
It allows you to delete a Custom Field from terminal

#### import-from-couchdb
Before you run this command you should make sure of two things:
1) CouchDB is running
2) PostgreSQL is running
This command will trigger a script that goes into you _server.ini_ file located in `.faraday/config` and check if you have credentials set up under the [couchdb] section. If you do then try to login with those credentials and if it succeeds, it will extract all your CouchDB data and import it into our new PostgreSQL database.

#### initdb
This command needs to be executed **only** at the moment of Faraday's installation. It will create the tables of the database, Faraday's user among other things.

If you try to execute this a second time it will indeed fail.

**Warning:** Please do not lose the random password that this command will print on the screen. It will be necessary to login into Faraday.

#### list-plugins
Lists available plugins.

#### migrate
Migrates database schema.

#### process-reports
Enables importation of plugins reports in ~/.faraday folder.

#### show-urls
Prints a list of all the URLs available to communicate with our API Rest. 

#### sql-shell
This command will open a PostgreSQL shell already configured with Faraday's user and configuration.

#### status-check
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

#### support
Generates a .zip file with technical information for support purposes.