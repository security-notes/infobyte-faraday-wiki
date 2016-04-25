<a name="index"></a>
* [I can't access the web GUI](#cant-access-web)
* [Faraday is not importing my report](#import)
* [A plugin added too much information to my database](#remove-by-severity)
* [I don't remember the Faraday Server password](#recover-password)

<a name="cant-access-web"></a>
### I can't access the web GUI
Is your CouchDB up and running? Try running

```
curl http://127.0.0.1:5984/
```

The reply should look something like

```json
{"couchdb":"Welcome","version":"0.10.1"}
```

If not, maybe try the [Apache CouchDB Installation Guide](https://wiki.apache.org/couchdb/Installation).

If so, read our documentation on how to setup Faraday to work with CouchDB [using our QT GUI](https://github.com/infobyte/faraday/wiki/CouchDB) or edit your local config file in $HOME/.faraday/config/user.xml and set your CouchDB route using the **couch_uri** tag, for example:

```xml
<couch_uri>http://127.0.0.1:5984</couch_uri>
```

Then run Faraday and point your browser to http://127.0.0.1:5984/reports/_design/reports/index.html replacing **127.0.0.1:5984** with your CouchDB URI.

[ [index] ](#index)

<a name="import"></a>
### Faraday is not importing my report
First let's make sure there is a Plugin to parse it so make sure your tool is listed in our [[Plugin List]]. Not there? [Code your own](https://github.com/infobyte/faraday/wiki/Basic-plugin-development) or [ask us to do it](https://github.com/infobyte/faraday/issues).

You can also try to force faraday to process a report with a certain plugin. For example, let's say you have a metasploit report that faraday is not detecting. You can change the report so that it ends with \_faraday\_metasploit, so it ends up as myreport_faraday_metasplot.xml, and then copy it to ~/.faraday/reports/$yourworkspace. This of course works for any plugin, not only metasploit. 

Is you XML valid? Try opening it in a browser, if the browser complains then you can try our XML Cleaning script (make sure to have [BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/bs4/doc/)):

```
python $FARADAY/helpers/cleanXML.py broken_file.xml
```

Read more about cleaning XMLs [here](https://github.com/infobyte/faraday/wiki/Helpers#cleanXML).

Then open Faraday's QT interface running the following in your installation root:

```
./faraday.py
```

Open the Workspaces perspective and select your workspace. Then copy the report file into the active workspace's directory in $HOME/.faraday/report/WS_NAME/. Faraday will only process requests for the active workspace.

[ [index] ](#index)

<a name="remove-by-severity"></a>
### A plugin added too much information to my database

You can go to your Status Report in the Web GUI, filter the vulnerabilities by whichever parameter you'd like, select them all and then click on Delete to remove them form the database.

![](https://raw.github.com/wiki/infobyte/faraday/images/faraday_statusreport_delete_vulns.png)

If for any reason you don't want to or you can't access the WebUI (or maybe even you'd like to automatize this task) you can use our helper script to remove vulnerabilities by severity.

For example, say you want to remove all vulnerabilities of severity **critical** in a local CouchDB on the workspace named **messedup**, you should run:

```./removeBySeverity.py -d messedup -s critical```

Read more about it [here](https://github.com/infobyte/faraday/wiki/helpers#removeBySeverity).

<a name="recover-password"></a>
### Restore the CouchDB user administrator
It is possible to restore the database's users using the following script:

`/faraday# ./reset_admin_couchdb.sh`

**Important: this process will eliminate existing users**

[ [index] ](#index)
