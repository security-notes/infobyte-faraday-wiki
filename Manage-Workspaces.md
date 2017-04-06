### Workspace

The workspaces are used to hold the information re-collected from the different tools and/ or commands used in the "actions" for each Penetration Test. Each workspace integrates all the results from pentesters from a given project in the Web console allowing you to to identify and manage your information in one place.

### How to manage the Workspace

To manage your workspaces you need to access [Faraday's Web Interface](https://github.com/infobyte/faraday/wiki/Web-UI) click on the **workspaces** icon ![](https://raw.github.com/wiki/infobyte/faraday/images/faraday_workspace_icono.png)

The workspaces you can see on a list, where you can create, edit or eliminate them as you wish.

![workspaces](https://raw.github.com/wiki/infobyte/faraday/images/faraday_workspace_list.png)

## How to make a Workspace

### Web UI
From the workspaces window click on **New** and complete

* Workspace name
* Description (optional)
* Owner
* Start Date / End Date
* Scope of workspace
* Users that can access the workspace

![](https://raw.github.com/wiki/infobyte/faraday/images/faraday_workspace_new.png)

### GTK
On the General view in the GTW interface click on the New Workspace icon 
![](https://github.com/infobyte/faraday/wiki/images/new-workspace-icon-gtk.png)
and complete the fields:

*Workspace Name

*Description

![](https://github.com/infobyte/faraday/wiki/images/Gtk-new-workspace-dialog.png)

### Scripting

This is the right way to create a Workspace from command line:

Create a file named script.py, place it in the Faraday Installation Directory and inside it write this piece of code:

```
#!/usr/bin/python2.7
from persistence.server import server
import time

server.FARADAY_UP = False
#Change this with your Faraday server url
server.SERVER_URL = "http://127.0.0.1:5985"

date_today = int(time.time() * 1000)
server.create_workspace('workspacename', 'DESCRIPTION', date_today, date_today, 'CUSTOMER NAME')
```
this is an example of what you can do,
for more thing you could do go checkout  /persistence/server/server.py

And now, to import xml files to your new created workspace run this in the terminal:
```./faraday.py --cli --workspace project_name -r report/tmp/nmap_scan.xml
```
Being
```project_name```
the name of your workspace and
```report/tmp/nmap_scan.xml```
the path to your import xml file which in this example is called nmap_scan.xml

### Editing a Workspace

From the workspace window click on **Edit**

![](https://raw.github.com/wiki/infobyte/faraday/images/faraday_workspace_edit.png)

### Deleting Workspaces

From the workspaces window click on **Delete**

![](https://raw.github.com/wiki/infobyte/faraday/images/faraday_workspace_delete.png)

