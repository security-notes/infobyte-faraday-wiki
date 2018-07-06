
## GTK GUI

GTK+3 is designed to improve on the deprecated QT interface, so nothing should look out of place if you were already using Faraday. If you weren't, don't worry, it's pretty simple.

To try it, check out our [installation manual](https://github.com/infobyte/faraday/wiki/installation-community).

To access Faraday GTK, run the following command in Faraday's folder:

```
    $ python faraday.py
```

#### The main window

![](https://raw.github.com/wiki/infobyte/faraday/images/Faraday-Gtk-MainWindow.png)

You will be presented with a special version of your own [ZSH terminal](https://en.wikipedia.org/wiki/Z_shell#Origin). Just as with GTK, Faraday intercepts every command you execute and checks if there's a plugin available. If there is, Faraday will interpret all the relevant information like ip adresses, hostnames, services, vulnerabilities, websites, and notes that the command generates.

The menubar gives you access to the most common options: you can open a new tab create a new workspace, toggle the log or set your Faraday Server URL in the preferences dialog (and login to the database if you use our Pro or Corporate versions). At the rightmost border, you'll be able to open a file chooser to import any report by our supported plugins to Faraday.

The sidebar has two tabs, one for workspaces and the other for hosts. The workspaces tab allows you to change workspaces, while the hosts tab shows you all the hosts in your current workspace, plus the amount of vulnerabilities found in each one of them inside parenthesis. Clicking on a host will show you more detailed information, see [Host information dialog](#host-information-dialog)

The status-bar has information about your workspace and also buttons to access the [Notifications dialog](#notifications-dialog) and the [Conflicts resolution dialog](#conflicts-dialog).

The log console works just as you'd expect, showing you what Faraday's doing in the background at all times. For more verbose output, you can run Faraday with the `--debug` flag.

<a name="host-information-dialog"></a>
#### Host information dialog

![](https://raw.github.com/wiki/infobyte/faraday/images/Faraday-Gtk-HostInfoDialog.png)

When you click on a host in the Host tab of the sidebar, you'll be presented with a window like the one above. The leftmost tree represents the Host itself, with all its interfaces as children. The interfaces, too, have children, which are the services of each interface. All of these items have the number of vulnerabilities discovered, inside parentheses.

The list of vulnerabilities shows the name of all the vulns found in the selected item of the leftmost tree.

The rightmost side of the windows shows detailed information of the host, the selected item of the leftmost tree (be it a service or an interface) and the selected vulnerability.

<a name="conflicts-dialog"></a>
#### Conflicts resolution dialog

![](https://raw.github.com/wiki/infobyte/faraday/images/Faraday-Gtk-ConflictsDialog.png)

When Faraday finds an object which clashes with one you have already saved, it will inform you there's a conflict. Imagine you have a host marked as a Windows machine, but a tool detects a Linux installation. It's a conflict!

Faraday will show you the two conflicting objects, with its differences highlighted in red. You can edit the information in the objects, and then decide if you want to keep the left or right one.

<a name="notifications-dialog"></a>
#### Notifications dialog

![](https://raw.github.com/wiki/infobyte/faraday/images/Faraday-Gtk-NotificationsDialog.png)

Faraday is a **multi-user** integrated penetration test environment. That's why keeping up with changes coming from your collaborators is so important, and its why the notifications dialog exists.

While working, the notifications counter will increase as new changes come from other instances of Faraday clients connected to the same database. If you click on the button, you'll be presented with a list of all the updates, so you are never kept in the dark of what your collaborators are up to.

<a name="adding-reports"></a>
#### Adding Reports

If you wish to add a report from a previous scan, you can also do it from the GTK Client.

To do so, click on the Report Button ![](https://raw.github.com/wiki/infobyte/faraday/images/faraday_gtk_report_button.png)

A dialog will open, from which you can select the tool that was used to generate the Report:

![](https://raw.github.com/wiki/infobyte/faraday/images/faraday_gtk_report_list.png)

All the data in the report will be processed and added to the active Workspace, and the console will show a message when the plugin starts and ends.
