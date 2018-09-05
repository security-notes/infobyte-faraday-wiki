## Intro

This guide is intended to provide solutions for common problems. If your problem is not listed below, [make sure to contact us](http://github.com/infobyte/faraday/issues)!

Before moving on, verify that you are using the latest available version running the client and the server using `--version` or `-v`.

To get the latest available version:

* for the community version, visit <https://github.com/infobyte/faraday/releases/latest>
* for the commercial versions, check the Customer Portal

We recommend upgrading to the latest version before proceeding.

Also, to get a better understanding of most problems you can run the Faraday Client using `--debug` or `-d` option.

#### Traceback Troubleshooting

For traceback troubleshooting you need to open the faraday logs and search for the string *ERROR*.
Logs are located on *~/.faraday/logs*.


In this section we will show common errors and possible solutions. We recommend to search part of the error in this page and try to match the error with possible solutions.


For example for the stack trace below you could try to search the following strings in this search:

* IOError: [Errno 2] No such file or directory:
* server/modules/info.py", line 16, in show_info

```python
2017-07-07 15:57:26,333 - server.app - ERROR - Exception on /info [GET]
Traceback (most recent call last):
  File "/home/leonardo/.pyenv/versions/faraday/local/lib/python2.7/site-packages/flask/app.py", line 1982, in wsgi_app
    response = self.full_dispatch_request()
  File "/home/leonardo/.pyenv/versions/faraday/local/lib/python2.7/site-packages/flask/app.py", line 1614, in full_dispatch_request
    rv = self.handle_user_exception(e)
  File "/home/leonardo/.pyenv/versions/faraday/local/lib/python2.7/site-packages/flask/app.py", line 1517, in handle_user_exception
    reraise(exc_type, exc_value, tb)
  File "/home/leonardo/.pyenv/versions/faraday/local/lib/python2.7/site-packages/flask/app.py", line 1612, in full_dispatch_request
    rv = self.dispatch_request()
  File "/home/leonardo/.pyenv/versions/faraday/local/lib/python2.7/site-packages/flask/app.py", line 1598, in dispatch_request
    return self.view_functions[rule.endpoint](**req.view_args)
  File "/home/leonardo/workspace/faraday/server/modules/info.py", line 16, in show_info
    with open(file_path, 'r') as version_file:
IOError: [Errno 2] No such file or directory: '/home/leonardo/VERSION'
```

<a name="index"></a>
## Index

* [I can't access the web GUI](#cant-access-web)
* [Faraday is not importing my report](#import)
* [A plugin added too much information to my database](#remove-by-severity)
* [I don't remember the Faraday Server password](#recover-password)
* [Clients can't access the Faraday server](#faraday-server-access-problems)
* [Error No such file or directory VERSION](#no-such-file-version)
* [ERROR - XML Plugin: Ip of host unknown](#ip-of-host-unknown)
* [[Errno 2] No such file or directory: '/home/john/.faraday/config/config.xml'](#user.xml-not-found)
* [OSx GTK not working IP ERROR](#osx-gtk-not-working)
* [How to fix GTK error on faraday using OSX](#osx-gtk-depencencies)
* [Can't login after Couch Import](#cant-login-after-couch-import)
* [Updating Nginx Configuration](#updating-nginx-configuration)
* [Error while making backup of the database](#backup-error)
* [GTK Error: No ports available](#no-ports-available)
## Answers

<a name="cant-access-web"></a>
### I can't access the web GUI

Is Faraday Server running? Try running:
```
./manage.py status_check
```
That will give some information about the state Faraday is in at the moment.
If the server is not running try:
```
./faraday-server.py
```
[ [index] ](#index)

<a name="import"></a>
### Faraday is not importing my report
First let's make sure there is a Plugin to parse it so make sure your tool is listed in our [[Plugin List]]. Not there? [Code your own](https://github.com/infobyte/faraday/wiki/Basic-plugin-development) or [ask us to do it](https://github.com/infobyte/faraday/issues).

You can also try to force Faraday to process a report with a certain plugin. For example, let's say you have a metasploit report that faraday is not detecting. You can change the report so that it ends with **\_faraday\_Metasploit**, (First letter of the plugin in capital letter) so it ends up as **myreport_faraday_Metasploit.xml**, and then copy it to ```~/.faraday/reports/{workspacename}``` (replacing **{workspacename}** with the actual name of your Workspace) in the client. This of course works for any plugin, not only Metasploit.

Keep in mind that Plugins don't run on the server, so if you're trying to copy the report file, make sure that you place it inside ```~/.faraday/report/{workspacename}``` (replacing **{workspacename}** with the actual name of your Workspace) in **the client**.

Is your XML valid? Try opening it in a browser, if the browser complains then you can try our XML Cleaning script (make sure to have [BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/bs4/doc/)):

```
python $FARADAY/helpers/cleanXML.py broken_file.xml
```

Read more about cleaning XMLs [here](https://github.com/infobyte/faraday/wiki/Helpers#cleanXML).

Then open Faraday's GTK interface running the following in your installation root:

```
./faraday.py
```

Open the Workspaces perspective and select your workspace. Then copy the report file into the active workspace's directory in ```~/.faraday/report/{workspacename}/``` (replacing **{workspacename}** with the actual name of your Workspace) in the client. Faraday will only process requests for the active workspace.

If you get the message "**IP of host unknown**", the problem may be that the system you're importing into _cannot resolve the DNS address_ from the hosts in your report (this is a must!).

[ [index] ](#index)

<a name="remove-by-severity"></a>
### A plugin added too much information to my database

You can go to your Status Report in the Web GUI, filter the vulnerabilities by whichever parameter you'd like, select them all and then click on Delete to remove them form the database.

![](https://raw.github.com/wiki/infobyte/faraday/images/status_report/delete_vulns.png)

If for any reason you don't want to or you can't access the WebUI (or maybe even you'd like to automatize this task) you can use our helper script to remove vulnerabilities by severity.

For example, say you want to remove all vulnerabilities of severity **critical** in a local installation on the workspace named **messedup**, you should run:

```./removeBySeverity.py -d messedup -s critical```

Read more about it [here](https://github.com/infobyte/faraday/wiki/helpers#removeBySeverity).

[ [index] ](#index)

<a name="faraday-server-access-problems"></a>
### Clients can't access the Faraday server

In your server machine, go to ~/.faraday/config/server.ini and check if you're listening only on the localhost.
You should see something like this:

```python
[faraday_server]
port=5985
bind_address=localhost
```

If your clients are on different machines than the server, then you'll need to change the bind_address to your private IP (or all your interfaces). For example:

```python
bind_address=0.0.0.0
```

[Check the configuration server page for more information](https://github.com/infobyte/faraday/wiki/Installation-Community#server-configuration)

[ [index] ](#index)

<a name="no-such-file-version"></a>
### Solution to error No such file or directory VERSION

This issue is common on version v2.4 and v2.5 and occurs when the faraday-server.py is executed outside the path where the faraday-server.py resides.
To solve the issue it's required to execute the faraday-server.py in the directory where that file resides.
After version v2.6 this issue was solved.

To solve this issue execute *faraday-server.py* on the correct directory as shown below:
```python
cd /home/username/faraday # or where the faraday-server was installed(*)
python faraday-server.py
```

(*) sometimes faraday server was installed in the /usr directory, check the traceback for the full path.

The stack track trace is:

```python
2017-07-07 15:57:26,333 - server.app - ERROR - Exception on /info [GET]
Traceback (most recent call last):
  File "/home/leonardo/.pyenv/versions/faraday/local/lib/python2.7/site-packages/flask/app.py", line 1982, in wsgi_app
    response = self.full_dispatch_request()
  File "/home/leonardo/.pyenv/versions/faraday/local/lib/python2.7/site-packages/flask/app.py", line 1614, in full_dispatch_request
    rv = self.handle_user_exception(e)
  File "/home/leonardo/.pyenv/versions/faraday/local/lib/python2.7/site-packages/flask/app.py", line 1517, in handle_user_exception
    reraise(exc_type, exc_value, tb)
  File "/home/leonardo/.pyenv/versions/faraday/local/lib/python2.7/site-packages/flask/app.py", line 1612, in full_dispatch_request
    rv = self.dispatch_request()
  File "/home/leonardo/.pyenv/versions/faraday/local/lib/python2.7/site-packages/flask/app.py", line 1598, in dispatch_request
    return self.view_functions[rule.endpoint](**req.view_args)
  File "/home/leonardo/workspace/faraday/server/modules/info.py", line 16, in show_info
    with open(file_path, 'r') as version_file:
IOError: [Errno 2] No such file or directory: '/home/leonardo/VERSION'
```

[ [index] ](#index)

<a name="ip-of-host-unknown"></a>
### ERROR - [ERROR] XML Plugin: Ip of host unknown

While importing reports faraday need to be able to resolve domain or else it will fail with the error *Ip of host unknown*.
Make sure you can resolve the domain from the computer where faraday is being executed.

[ [index] ](#index)
<a name=osx-gtk-not-working></a>
### OSx GTK not working IP ERROR
When using OSx it's necessary for the client to assign the localhost address to your hostname.
Inside a terminal run:


`  hostname`


And copy the result

Go to your /etc/hosts file and assing 127.0.0.1 to your localmachine hostname.


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
### [Errno 2] No such file or directory: '/home/john/.faraday/config/config.xml'
Before running the server for the first time you need to execute:
```
python faraday.py
```
This will throw an error and exit but before doing that the file user.xml will be created in your .faraday/config directory.
Now run the server again, and enjoy faraday!

[ [index] ](#index)

<a name="cant-login-after-couch-import"></a>
### Can't Login after Importing from Couch

There's a change the password on your server.ini wasn't updated or wrong. We must change the password for your user on the database.

Run the following command in order to execute PostgreSQL shell:

    $ python manage.py sql_shell

Once you got into the sql_shell, let's take a look inside the table _faraday_user_ to see the users information. **It is important to be sure of the username we want to change the password.**

    SELECT * FROM faraday_user

Assuming your username is '_faraday_' and the new password you want to set is '_changeme_', run the following command:

    UPDATE faraday_user SET PASSWORD='changeme' WHERE username='faraday'

This command will update your user's password.

Now you can login to Faraday without a problem.

[ [index] ](#index)

<a name="updating-nginx-configuration"></a>
### Updating Nginx configuration

***Note:*** This only applies if you are using Nginx and https.

Please, make sure you have this settings on your Nginx config:

    proxy_pass http://localhost:5985/;
    proxy_redirect http:// $scheme://;

[ [index] ](#index)

<a name="backup-error"></a>
### Error while backuping the database
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

Go into the file user.xml locates in .faraday/config/

 ~<api_con_info_host>localhost</api_con_info_host>~
**<api_con_info_host>127.0.0.1</api_con_info_host>**
  <api_con_info_port>9876</api_con_info_port>
  <api_restful_con_info_port>9977</api_restful_con_info_port>

Change localhost for 127.0.0.1 and try again.

[ [index] ](#index)
Is your question not listed here? [Contact us](https://github.com/infobyte/faraday/issues)
