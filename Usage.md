## Faraday Client

Faraday has 5 different ways to interact with the information:

* [GTK GUI](#gtk-gui)
* [ZSH UI](#zsh-ui)
* [Web UI](#web-ui)
* [CLI](#cli)
* [ZSH Web](#zsh-web-console) (only available in our commercial versions)


### GTK GUI

GTK+3 is designed to improve on the QT3 deprecated interface, so nothing should look out of place if you were already using Faraday. If you weren't, don't worry, it's pretty simple. 

To try it, just [[install the dependencies|installation-client#requirements]] and run Faraday using the command `python faraday.py`.

#### The main window

![](https://raw.github.com/wiki/infobyte/faraday/images/Faraday-Gtk-MainWindow.png)

You will be presented with a special version of your own ZSH terminal. Just as with QT3, Faraday intercepts every command you execute and checks if there's a plugin available. If there is, Faraday will gather all relevant information like ip adresses, hostnames, services, vulnerabilities, websites and notes for you.

The menubar gives you access to the most common options: you can open a new tab create a new workspace, toggle the log or set your CouchDB URL in the preferences dialog (and login to the database if you use our Pro or Corporate versions). At the rightmost border, you'll be able to open a file chooser to import any report by our supported plugins to Faraday.

The sidebar has two tabs, one for workspaces and the other for hosts. The workspaces tab allows you to change workspaces, while the hosts tab shows you all the hosts in your current workspace, plus the amount of vulnerabilities found in each one of them inside parenthesis. Clicking on a host will show you more detailed information, see [Host information dialog](#host-information-dialog)

The statusbar has information about your workspace and also buttons to access the [Notifications dialog](#notifications-dialog) and the [Conflicts resolution dialog](#conflicts-dialog).

The log console works just as you'd expect, showing you what Faraday's doing on the background at all times. For more verbose output, you can run Faraday with the --debug flag. 

<a name="host-information-dialog"></a>
#### Host information dialog

![](https://raw.github.com/wiki/infobyte/faraday/images/Faraday-Gtk-HostInfoDialog.png)

When you click on a host in the Host tab of the sidebar, you'll be presented with a window like the one above. The leftmost tree represents the Host itself, with all its interfaces as children. The interfaces, too, have children, which are the services of said interfaces. All of these items have the number of vulnerabilities found on them inside parenthesis. 

The list of vulnerabilities shows the name of all the vulns found in the selected item of the leftmost tree. 

The rightmost side of the windows shows detailed information of the host, the selected item of the leftmost tree (be it a service or an interface) and the selected vulnerability. 

<a name="conflicts-dialog"></a>
#### Conflicts resolution dialog

![](https://raw.github.com/wiki/infobyte/faraday/images/Faraday-Gtk-ConflictsDialog.png)

When Faraday finds an object which clashes with one you have already saved, it will inform you there's a conflict. Imagine you have a host marked as a Windows machine, but a tool detects a Linux installation. That's a conflict.

Faraday will show you the two conflicting objects, with its differences highlighted in red. You can edit none or all of the information in the objects, and the decide if you want to keep the left or right one.

<a name="notifications-dialog"></a>
#### Notifications dialog

![](https://raw.github.com/wiki/infobyte/faraday/images/Faraday-Gtk-NotificationsDialog.png)

Faraday is a multi-user integrated penetration test environment. That's why keeping up with changes coming from your collaborators is so important, and its why the notifications dialog exists. 

While working, the notifications counter will increase as new changes come from other instances of Faraday connected to the same database. If you click on the button, you'll be presented with a list of all the updates, so you are never kept in the dark. 


### ZSH UI

You can even run Faraday in detached mode connecting with a ZSH terminal to it:

![](https://raw.github.com/wiki/infobyte/faraday/images/no-ui.png)
![](https://raw.github.com/wiki/infobyte/faraday/images/no-ui2.png)

No manual imports needed but supported. Just drop your fresh generated reports in:
    $ ~/.faraday/report/workspace_name

Faraday will parse your reports and upload the information extracted from them. 
All the available information will be available through the different interface

* [QT GUI](#qt-gui)
* [GTK GUI](#gtk-gui)
* [Web UI](#web-ui)


### Web UI

In order to access the Web UI point your browser to: http://[FARADY-SERVER]:PORT/_ui/

The current URL address is displayed on console log information

![](https://raw.github.com/wiki/infobyte/faraday/images/Console_GUIWeb_Highlight.png)

You can also go directly there from GTK clicking on this icon:  

![](https://raw.github.com/wiki/infobyte/faraday/images/Visualize-icon.png)


#### Faraday Community Version

##### Dashboard

Faraday's dashboard contains a summary of all the data in a Workspace condensed into different boxes. Each box is a visualization using a specific part of the collected data.

![](https://raw.github.com/wiki/infobyte/faraday/images/GUI_Dashboard_new.png)

###### Top Services View

To access a [treemap](https://en.wikipedia.org/wiki/Treemapping) featuring the top services in the Workspace, click on the box title.

![](https://raw.github.com/wiki/infobyte/faraday/images/GUI_Dashboard_new_Services.png)

![](https://raw.github.com/wiki/infobyte/faraday/images/GUI_Services.png)

<a name="workspace-worth"></a>
###### Workspace's Worth

![](https://raw.github.com/wiki/infobyte/faraday/images/faraday-dashboard-ws-worth.png)

This visualization is specially helpful when contributing in a bug bounty program. You can estimate how much your Workspace is worth according to the severity of your vulnerabilities.

You can edit the price per severity by clicking on it. The graphic will change as you type.

So lets say that you have a workspace with 6 vulns, one for each severity. And the price schema is:


* Criticals are worth 6 dollars
* Highs are worth 5 dollars
* Meds are worth 4 dollars
* Lows are worth 3 dollars
* Infos are worth 2 dollars
* Unclassifieds are worth 1 dollar


Then your Workspace will be worth 
```
6*1+5*1+4*1+3*1+2*1+1*1 = $21
```

The length of the colored bars shows how much that severity represents in the final worth according to how many of those are present in the current workspace.

Learn more about using Faraday for [[Bug bounties]].

##### Vulnerability Status Report

To view a full list of findings you can access the Status Report.

![](https://raw.githubusercontent.com/wiki/infobyte/faraday/images/UI_Web_Status_Report.png)

The Status Report provides several options including vulnerability search, filtering and management.

Personalize this view by clicking on the blue buttons to select the columns you wish to see, and remove the ones you don't need using the crosses in the table. These changes will be persisted in your browser so you only have to apply them once.

###### Search & Filter

To search, type the keyword in the text field above the table.

You can find the text filter both on the Status Report and Hosts views. Keep in mind that field values are case-insensitive.

![](https://raw.github.com/wiki/infobyte/faraday/images/search.png)

###### Filter by field

To search by field enter the name of field  (e.g. **severity**), continue with a colon  (**:**) and finally put in the word that you want to find.

Examples: 

* severity:unclassified
* name:Nessus scan info


![](https://raw.github.com/wiki/infobyte/faraday/images/filterByField.png)

###### Filter by many fields

To search by many fields do a normal search but at the end type a *SPACE BAR* and do a normal search again.

Examples:

* severity:unclassified target:173.252.100.18
* severity:low service:443 target:173.252


![](https://raw.github.com/wiki/infobyte/faraday/images/searchByManyFields.png)

###### Grouping

To group vulnerabilities by field you can use the **Group By** button. After the vulns are grouped you can select them for easy batch edit.

![](https://raw.githubusercontent.com/wiki/infobyte/faraday/images/faraday_statusreport_groupby.png)

<a name="manage"></a>
##### Vulnerability Creation
To create vulnerabilities manually, you can go to the status report page, and click the "New" button at the top right corner. You should see a dialog similar to this:

![](https://raw.githubusercontent.com/wiki/infobyte/faraday/images/faraday_new.png)

Make sure you select a host (and a service if the vulnerability applies to it), and the correct type. If you create a web vulnerability, you will have a couple more fields available, such as path, method, request, response and so on.

#### Faraday Professional & Corporate - [Commercial versions](https://www.faradaysec.com/#download)

This version includes advanced visualizations, tags, pentest comparison, pentester ranking among others.

![](https://raw.github.com/wiki/infobyte/faraday/images/Faraday-Dashboard-Advance.png)

##### Tags

Tags allow you to organize your vulnerabilities. by letting you make and edit categories: environment, technology, state, language, projects, whatever. The team can then see the tagged vulnerabilities and lets you organize the security evaluation.

The tags are assigned to the team's workspace letting you use different tags for different projects.

###### How to tag vulnerabilities

Using the specified credentials during the configuration, from the Navigator start the session in [Faraday's GUI](https://github.com/infobyte/faraday/wiki/Web-UI). Once you have obtained the authentication and you are in, click on the “Status Report” icon.

![](https://raw.github.com/wiki/infobyte/faraday/images/faraday_statusreport_list.png)

Select the vulnerabilities that you want to tag (for example those that have to do with SSL protocol)

![](https://raw.github.com/wiki/infobyte/faraday/images/faraday_statusreport_listselected.png)

After picking one of the vulnerabilities click on the "Tags" button

![](https://raw.github.com/wiki/infobyte/faraday/images/faraday_statusreport_tagsadd.png)

Create the tag that you want (in our case SSL) and click OK

![](https://raw.github.com/wiki/infobyte/faraday/images/faraday_statusreport_tagsadded.png)

###### Search tagged vulnerabilities

From the Status Report you will be able to find the information using the different tags. You can add ! in front of the search criteria in order to invert the result. For example _tag:!example_tag_ will result in all vulnerabilities that DON'T have the tag example_tag.

![](https://raw.github.com/wiki/infobyte/faraday/images/faraday_statusreport_tagssearch.png)


### CLI

It's possible to use Faraday in CLI mode, allowing you to process your reports in batch. So lets say you want to process the XML output of an **nmap** scan located in ```/tmp/nmap_scan.xml``` and send the information to a workspace called **project_one**. The way to do it using the CLI mode would be to run:

```
$ ./faraday.py --cli --workspace project_one --report /tmp/nmap_scan.xml
```

NOTE: the workspace has to exist for this to work.

#### Professional and corporate versions

If you're using a professional or corporate version, you'll probably need to start faraday with a certain user, with permissions in that workspace. You can pass your credentials using a simple json file with both user and password. You can use any path and name for the file, and you have a template you can change or copy in the root of your Faraday installation called  credentials.json. The structure is this:

```
{
    "username": "your_user_here",
    "password": "your_password_here"
} 
```

And then run Faraday:

```
$ ./faraday.py --cli --workspace project_one --report /tmp/nmap_scan.xml --creds-file /path/to/file/creds.json
```


<a name="zsh-web"></a>
### ZSH web console

[- Commercial version -](https://www.faradaysec.com/#download)

It's also possible to use the ZSH interface inside your web browser. To do this, fist you need to install butterfly:

```
$ pip install --user butterfly
```

NOTE: If you have both python2 and python3 in your system, it's better to use pip2 instead of pip.

Now, run butterfly:

```
$ butterfly.server.py --unsecure --shell=/bin/zsh --cmd="<path/of/faraday/>faraday-terminal.zsh [host] [port]"
```

Of course, you need to set the path of the folder in which you have faraday (the faraday-terminal.zsh script should be in the root of that folder). Also, You can pass the host and port as arguments to that script, in case you've changed the Faraday's REST API parameters (remember that you have to run Faraday QT or Faraday —gui=nogui so that the terminal for ZSH functions properly)

The idea of the webshell is to be able to do actions directly from the web using ZSH as a console. You would be connected to your own shell (listening in loopback interface). 

Then, open a new tab from the webshell icon in the web UI's sidebar, and you should see the zsh shell up and running!

![](https://raw.github.com/wiki/infobyte/faraday/images/butterfly_webshell.png)
