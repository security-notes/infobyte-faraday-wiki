### Workspace

The workspaces are used to hold the information re-collected from the different tools and/ or commands used in the "actions" for each Penetration Test. Each workspace integrates all the results from pentesters from a given project in the Web console allowing you to to identify and manage your information in one place.

### How to manage the Workspace

To manage your workspaces you need to access [Faraday's Web Interface](https://github.com/infobyte/faraday/wiki/Status-report) click on the **faraday** slider menu on the right of the screen ![](https://raw.github.com/wiki/infobyte/faraday/images/workspaces/icon.png)
and then on **Wokspaces**
![](https://raw.github.com/wiki/infobyte/faraday/images/workspaces/menu.png)



The workspaces you can see on a list, where you can create, edit or eliminate them as you wish.

![workspaces](https://raw.github.com/wiki/infobyte/faraday/images/workspaces/list.png)

## How to make a Workspace

### Web UI
From the workspaces window click on **New** and complete

* Workspace name
* Description (optional)
* Owner
* Start Date / End Date
* Scope of workspace
* Users that can access the workspace

![](https://raw.github.com/wiki/infobyte/faraday/images/workspaces/new.png)

### GTK
On the General view in the GTW interface click on the New Workspace icon 
![](https://raw.github.com/wiki/infobyte/faraday/images/workspaces/gtk_new_workspace_icon.png)
and complete the fields:

*Workspace Name

*Description

![](https://raw.github.com/wiki/infobyte/faraday/images/workspaces/gtk_new_workspace_dialog.png)

### Scripting

This is the right way to create a Workspace from command line:

Inside the directory in which Faraday is installed, create a file named script.py, with the following code:

```
#!/usr/bin/python2.7
from persistence.server import server
import time

server.FARADAY_UP = False
#Change this with your Faraday server url
server.SERVER_URL = "http://127.0.0.1:5985"
#Change this with your Faraday server username and password
#Not necessary for community version
server.AUTH_USER = "YOUR_USERNAME"
server.AUTH_PASS = "YOUR_PASSWORD"

date_today = int(time.time() * 1000)
server.create_workspace('workspacename', 'DESCRIPTION', date_today, date_today, 'CUSTOMER NAME')
```
This script will create a workspace with the name "workspacename". (Don't forget to change the variables server.SERVER_URL, server.AUTH_USER, server.AUTH_PASS with your server's url, authorization username, and password! (for the Community version, it isn't necessary to include server.AUTH_USER / server.AUTH_PASSWORD))

The see the various things you can do with scripting, take a look at (in your Faraday installation directory) ./persistence/server/server.py . 

And now, to import xml files to your newly created workspace run this in the terminal:
```
./faraday.py --cli --workspace workspacename -r report/tmp/nmap_scan.xml
```
Where:
```workspacename```
the name of your newly-created workspace and
```report/tmp/nmap_scan.xml```
the path to the xml file you want to import, which in this example is named nmap_scan.xml

### Editing a Workspace

From the workspace window click on **Edit**

![](https://raw.github.com/wiki/infobyte/faraday/images/workspaces/edit.png)

### Deleting Workspaces

From the workspaces window click on **Delete**

![](https://raw.github.com/wiki/infobyte/faraday/images/workspaces/delete.png)

