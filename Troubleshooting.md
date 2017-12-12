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
* [ERROR - [ERROR] XML Plugin: Ip of host unknown](#ip-of-host-unknown)
* [OSError: [Errno 2] No such file or directory: './reports/executive/templates/'](#executive-report-error)


### Commercial versions

* [I can't edit Workspaces in the web UI](#edit-workspaces-wui)
* [OSError: [Errno 2] No such file or directory: './reports/executive/templates/'](#executive-report-error)
* [401 Unauthorized: when importing a report on the client](#401-unauthorized-when-importing-a-report-on-the-client)


## Answers

<a name="cant-access-web"></a>
### I can't access the web GUI

Is Faraday Server running? Try something like this, replacing the URL and port
with those of your Faraday Server:

```
curl http://127.0.0.1:5985/_api/info
```

The reply should look something like

```json
{"Faraday Server":"Running"}
```

If not, maybe try the [Faraday Server Installation](https://github.com/infobyte/faraday/wiki/Installation-Community#server-configuration).

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

![](https://raw.github.com/wiki/infobyte/faraday/images/faraday_statusreport_delete_vulns.png)

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



## Answers for Commercial versions

<a name="edit-workspaces-wui"></a>
### I can't edit Workspaces from the Web UI
Make sure that the configuration file for the server contains the credentials for an **administrative user** in the ```user``` and ```password``` fields inside the ```[couchdb]``` section of the configuration file located in ```~/.faraday/config/server.ini```.

[ [index] ](#index)

<a name="executive-report-error"></a>
### OSError: [Errno 2] No such file or directory: './reports/executive/templates/'

When you click "New" on the executive report and the modal doest not appear, be sure to check the logs for errors.

This happens when the faraday is executed outside the directory where it resides. This issue was solved on v2.6.


To solve this issue execute *faraday-server.py* on the correct directory as shown below:
```python
cd /home/username/faraday # or where the faraday-server was installed
python faraday-server.py
```

(*) sometimes faraday server was installed in the /usr directory, check the traceback for the full path.

[ [index] ](#index)

Is your question not listed here? [Contact us](https://github.com/infobyte/faraday/issues)
