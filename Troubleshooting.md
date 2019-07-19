## Intro

This guide is intended to provide solutions for common problems. If your problem is not listed below, [make sure to contact us](http://github.com/infobyte/faraday/issues)!

Before moving on, verify that you are using the latest available version running the Client and the Server using `--version` or `-v`.

To get the latest available version visit <https://github.com/infobyte/faraday/releases/latest>

We recommend upgrading to the latest version before proceeding.

Also, to get a better understanding of most problems you can run the Faraday Client using `--debug` or `-d` option.

#### Traceback Troubleshooting

For traceback troubleshooting you need to open the Faraday logs and search for the string *ERROR*.
Logs are located on */home/faraday/.faraday/logs*.

In this section we will show common errors and possible solutions. We recommend to search part of the error in this page and try to match the error with possible solutions.

<a name="index"></a>
## Index

* [I can't access the Web GUI](#cant-access-web)
* [Faraday is not importing my report](#import)
* [A plugin added too much information to my database](#remove-by-severity)
* [How to reset Faraday Server password](#change-password)
* [Can't access Faraday Server remotely](#faraday-server-access-problems)
* [OSx GTK not working IP ERROR](#osx-gtk-not-working)
* [OSx GTK not working AttributeError: 'module' object has no attribute 'require_version'](#osx-gtk-depencencies)
* [[Errno 2] No such file or directory: '/home/USERNAME/.faraday/config/config.xml'](#user.xml-not-found)
* [Updating Nginx Configuration](#updating-nginx-configuration)
* [Error while backing up the database](#backup-error)
* [No ports available](#no-ports-available)
* [UnicodeEncodeError: 'ascii' codec can't encode character](#unicode-error)
* [Database encoding incompatibility executing initdb](#database-encoding-incompatibility-initdb)


## Answers

<a name="cant-access-web"></a>
### I can't access the Web GUI

Is Faraday Server running? Try running:
```
$ faraday-manage status-check
```
That will give some information about the state Faraday is in at the moment.
If the Server is not running try:
```
$ faraday-server
```
[ [index] ](#index)

<a name="import"></a>
### Faraday is not importing my report
First let's make sure there is a Plugin to parse it so make sure your tool is listed in our [[Plugin List]]. Not there? [Code your own](https://github.com/infobyte/faraday/wiki/Basic-plugin-development) or [ask us to do it](https://github.com/infobyte/faraday/issues).

You can also try to force Faraday to process a report with a certain plugin. For example, let's say you have a Metasploit report that Faraday is not detecting. You can change the report so that it ends with **\_faraday\_Metasploit** (first letter of the plugin in uppercase), so it ends up as **myreport_faraday_Metasploit.xml**, and then copy it to ```/home/faraday/.faraday/reports/{workspacename}``` in the Client. This of course works for any plugin, not only Metasploit.

Keep in mind that Plugins don't run on the Server, so if you're trying to copy the report file, make sure you're doint it on the **Client**.

[ [index] ](#index)

<a name="remove-by-severity"></a>
### A plugin added too much information to my database

You can go to your [Status Report](https://github.com/infobyte/faraday/wiki/Status-Report) in the Web GUI, filter the vulnerabilities by whichever parameter you'd like, select them all and then click on Delete to remove them form the database.

![](https://raw.github.com/wiki/infobyte/faraday/images/status_report/delete_vulns.png)

If for any reason you don't want to or you can't access the WebUI (or maybe even you'd like to automatize this task) you can use our [Searcher](https://github.com/infobyte/faraday/wiki/Searcher).

[ [index] ](#index)

<a name="change-password"></a>
### How to reset Faraday Server password

If you forgot the password or you don't know your Faraday Server password, you can use the command `faraday-manage` to change it:

```
$ faraday-manage change-password
```

[ [index] ](#index)

<a name="faraday-server-access-problems"></a>
### Can't access Faraday Server remotely

In your Server machine, go to /home/faraday/.faraday/config/server.ini and check if you're listening only on the localhost.
You should see something like this:

```
[faraday_server]
port=5985
bind_address=localhost
```

If your Clients are on different machines than the Server, then you'll need to change the bind_address to your private IP (or all your interfaces). For example:

```
bind_address=0.0.0.0
```

[ [index] ](#index)

<a name=osx-gtk-not-working></a>
### OSx GTK not working IP ERROR
When using OSx it's necessary for the Client to assign the localhost address to your hostname.
Inside a terminal run:


`  hostname`


And copy the result

Go to your /etc/hosts file and assign 127.0.0.1 to your local machine hostname.


[ [index] ](#index)

<a name=osx-gtk-depencencies></a>
### OSx GTK not working AttributeError: 'module' object has no attribute 'require_version'
Traceback:
```
Traceback (most recent call last):
  File "faraday.py", line 635, in <module>
    main()
  File "faraday.py", line 631, in main
    startFaraday()
  File "faraday.py", line 303, in startFaraday
    main_app = MainApplication(args)
  File "/Users/myuser/tools/faraday/model/application.py", line 135, in __init__
    self.args.gui)
  File "/Users/myuser/tools/faraday/gui/gui_app.py", line 19, in create
    from gui.gtk.application import GuiApp
  File "/Users/myuser/tools/faraday/gui/gtk/application.py", line 26, in <module>
    gi.require_version('Gtk', '3.0')
AttributeError: 'module' object has no attribute 'require_version'
```

If you see this error all you need to do is re-install the [dependencies](https://github.com/infobyte/faraday/wiki/Installation-OSX#dependencies-and-other-python-libraries-via-pip) using brew.

<a name=#user.xml-not-found></a>
### [Errno 2] No such file or directory: '/home/USERNAME/.faraday/config/config.xml'
Before running the server for the first time you need to execute:
```
faraday-client
```
This will throw an error and exit but before doing that the file user.xml will be created in your .faraday/config directory.
Now run the server again, and enjoy faraday!

[ [index] ](#index)

<a name="updating-nginx-configuration"></a>
### Updating Nginx configuration

***Note:*** This only applies if you are using Nginx and https.

Please, make sure you have this settings on your Nginx config:

    proxy_pass http://localhost:5985/;
    proxy_redirect http:// $scheme://;

[ [index] ](#index)

<a name="backup-error"></a>
### Error while backing up the database
If you get this error:

` “pci_q1” failed: FATAL: role “root” does not exist`

while trying to execute:

`pg_dump <name of workspace> > <name of what I want the backup file to be>`

Run:

`sudo -u postgres -i`

And then try again.

[ [index] ](#index)

<a name='no-ports-available'></a>
### No ports available
If you see this traceback:

Traceback (most recent call last):
File "/usr/share/python-faraday/model/application.py", line 145, in start
CONF.getApiRestfulConInfoPort()
File "/usr/share/python-faraday/apis/rest/api.py", line 67, in startAPIs
raise Exception("No ports available!")
Exception: No ports available!

Go into the file user.xml locates in /home/USERNAME/.faraday/config/

 ~<api_con_info_host>localhost</api_con_info_host>~
**<api_con_info_host>127.0.0.1</api_con_info_host>**
  <api_con_info_port>9876</api_con_info_port>
  <api_restful_con_info_port>9977</api_restful_con_info_port>

Change localhost for 127.0.0.1 and try again.

[ [index] ](#index)

<a name='unicode-error'></a>
### UnicodeEncodeError: 'ascii' codec can't encode character

If you see a Traceback that ends something like this:

`UnicodeEncodeError: 'ascii' codec can't encode character u'\xf3' in position 1: ordinal not in range(128)`

Go into your Faraday folder and run the following command:

    $ faraday-manage sql-shell

Once inside the shell execute:

`SHOW SERVER_ENCODING`

If you are using symbols not supported by ASCII, you need to change database's encoding to UTF-8.
1. Dump your database
2. Drop your database,
3. Create new database with the different encoding
4. Reload your data.

Make sure the client encoding is set correctly during this process.


[ [index] ](#index)

<a name="database-encoding-incompatibility-initdb"></a>
### Database encoding incompatibility executing initdb

If you got the following error when running the command `faraday-manage initdb`:

```
ERROR: createdb: database creation failed: ERROR:  new encoding (UTF8) is incompatible with the encoding of the template database (SQL_ASCII)
HINT:  Use the same encoding as in the template database, or use template0 as template.
```

You can follow the instructions provided in this [link](https://gist.github.com/amolkhanorkar/8706915#file-pg-error-error-new-encoding-utf8-is-incompatible).

Once you get the solution above, you can try to initialize the database once more:

```
faraday-manage initdb
``` 
[ [index] ](#index)

Is your question not listed here? [Contact us](https://github.com/infobyte/faraday/issues)