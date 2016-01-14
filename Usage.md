Faraday has 3 different ways to interact with information:
* [QT GUI] (#qt-gui)
* [ZSH UI] (#zsh-ui)
* [Web UI] (#web-ui)

### QT GUI

Faraday main window is simple:  
![](https://raw.github.com/wiki/infobyte/faraday/images/Faraday-Mainwindow.png)

Structured in panes: Main Console, HostTree, Log Console, Item Info & Editing panes.

#### With authentication
[- Commercial version -](https://www.faradaysec.com/#download)

If you are able to run Faraday QT with credentials add a login option

```
./faraday.pyc --login
```

![](https://raw.github.com/wiki/infobyte/faraday/images/faraday_guiqt_login.png)

Every command that you execute is intercepted and a handler is invoked in order to transparently import the newly generated information by the tool in the context of the pentest like ip addresses, hostnames, services, vulnerabilities, websites, notes, etc.

### ZSH UI

You can even run Faraday in detached mode connecting with a ZSH terminal to it:

![](https://raw.github.com/wiki/infobyte/faraday/images/no-ui.png)
![](https://raw.github.com/wiki/infobyte/faraday/images/no-ui2.png)

No manual imports needed but supported. Just drop your fresh generated reports in:
    $ ~/.faraday/report/workspace_name

Faraday will parse your reports and upload the information extracted from them.

In order to access the Web UI point your browser to: http://[COUCHDB]:5984/reports/_design/reports/index.html

![](https://raw.github.com/wiki/infobyte/faraday/images/Console_GUIWeb_Highlight.png)

Directly from the GUI QT you have to click in the icon:

![](https://raw.github.com/wiki/infobyte/faraday/images/Visualize-icon.png)

### Web UI

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

<a name="manage"></a>
##### Vulnerability Creation

![](https://raw.githubusercontent.com/wiki/infobyte/faraday/images/faraday_new.png)

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

#### ZSH web console

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