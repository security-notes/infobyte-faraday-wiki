<a name="index"></a>
## Index

* [GTK](#gtk-client)
* [ZSH](#zsh-client)
* [CLI](#cli-nogui)

<a name="gtk-client"></a>
## GTK

GTK+3 is designed to improve on the deprecated QT interface, so nothing should look out of place if you were already using Faraday.

To access Faraday GTK, run the following command in Faraday's folder:

```
    $ faraday-client
```

![](https://raw.github.com/wiki/infobyte/faraday/images/client/gtk_main_window.png)

You will be presented with a special version of your own [ZSH terminal](https://en.wikipedia.org/wiki/Z_shell#Origin). Just as with GTK, Faraday intercepts every command you execute and checks if there's a plugin available. If there is, Faraday will interpret all the relevant information like ip adresses, hostnames, services, vulnerabilities, websites, and notes that the command generates.

The **menu bar** gives you access to the most common options, you can:
open a new tab 
create a new workspace
toggle the log 
set your Faraday Server URL in the preferences dialog 

At the rightmost border, you'll be able to open a file chooser to import any report by our [supported Plugins](https://github.com/infobyte/faraday/wiki/Plugin-List) to Faraday.


The **sidebar** has two tabs, one for Workspaces and the other for Hosts. The Workspaces tab allows you to change Workspaces, while the Hosts tab shows you all the hosts in your current workspace, plus the amount of vulnerabilities found in each one of them inside parenthesis. Clicking on a host will show you more detailed information:

![](https://raw.github.com/wiki/infobyte/faraday/images/client/gtk_host_info_dialog.png)

Here, the leftmost tree represents the Host itself, with all its interfaces as children. The interfaces, too, have children, which are the services of each interface. All of these items have the number of vulnerabilities discovered, inside parentheses.

The list of vulnerabilities shows the name of all the vulns found in the selected item of the leftmost tree.

The rightmost side of the windows shows detailed information of the host, the selected item of the leftmost tree (be it a service or an interface) and the selected vulnerability.


The **log console** works just as you'd expect, showing you what Faraday's doing in the background at all times. For more verbose output, you can run Faraday with the `--debug` flag.


The **status-bar** has information about your workspace and also buttons to access the Conflicts Resolution dialog and the Notifications dialog.

<a name="conflicts-dialog"></a>
#### Conflicts resolution dialog

![](https://raw.github.com/wiki/infobyte/faraday/images/client/gtk_conflicts_dialog.png)

When Faraday finds an object which clashes with one you have already saved, it will inform you there's a conflict. Imagine you have a host marked as a Windows machine, but a tool detects a Linux installation. It's a conflict!

Faraday will show you the two conflicting objects, with its differences highlighted in red. You can edit the information in the objects, and then decide if you want to keep the left or right one.

<a name="notifications-dialog"></a>
#### Notifications dialog

![](https://raw.github.com/wiki/infobyte/faraday/images/client/gtk_notifications_dialog.png)


Faraday is a **multi-user** integrated penetration test environment. That's why keeping up with changes coming from your collaborators is so important, and its why the notifications dialog exists.

While working, the notifications counter will increase as new changes come from other instances of Faraday clients connected to the same database. If you click on the button, you'll be presented with a list of all the updates, so you are never kept in the dark of what your collaborators are up to.

<a name="adding-reports"></a>
#### Adding Reports

If you wish to add a report from a previous scan, you can also do it from the GTK Client.

To do so, click on the Report Button ![](https://raw.github.com/wiki/infobyte/faraday/images/client/report_button.png)

A dialog will open, from which you can select the tool that was used to generate the Report:

![](https://raw.github.com/wiki/infobyte/faraday/images/client/plugins_list.png)

All the data in the report will be processed and added to the active Workspace, and the console will show a message when the plugin starts and ends.

[ [index] ](#index)

<a name="zsh-client"></a>
### ZSH

You can even run Faraday in detached mode connecting with a ZSH terminal to it:

First, you need to run Faraday with no GUI:

``` 
    $ faraday-client --gui=no-gui
```

![](https://raw.github.com/wiki/infobyte/faraday/images/client/no_ui.png)

Now, run Faraday Terminal:

```
    $ faraday-terminal
```

![](https://raw.github.com/wiki/infobyte/faraday/images/client/no_ui2.png)

### Using oh-my-zsh

You can use [oh-my-zsh](https://github.com/robbyrussell/oh-my-zsh) for managing your ZSH configuration. All you need to do is to [install](https://github.com/robbyrussell/oh-my-zsh#basic-installation) oh-my-zsh framework and then run the faraday-terminal command.

### Importing your reports

To import your reports, drag-and-drop them into:

    $ /home/faraday/.faraday/reports/[workspace_name]

Faraday will parse your reports and upload the information extracted from them.

[ [index] ](#index)

<a name="cli-nogui"></a>
## CLI

It's possible to use Faraday in Command-Line Interface (CLI) mode, allowing you to process your reports in batch. So lets say you want to process the XML output of an **nmap** scan located in ```/tmp/nmap_scan.xml``` and send the results to a workspace called **project_one**. The way to do it using CLI mode would be to run:

```
$ faraday-client --cli --workspace project_one --report /tmp/nmap_scan.xml
```

NOTE: the workspace has to already exist for the command to work.

