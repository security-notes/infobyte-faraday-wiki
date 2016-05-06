Faraday introduces a new concept - IPE (Integrated Penetration-Test Environment) a multiuser Penetration test IDE. Designed for distribution, indexation and analysis of the data generated during a security audit.

The main purpose of Faraday is to re-use the available tools in the community to take advantage of them in a multiuser way.

Designed for simplicity, users should notice no difference between their own terminal application and the one included in Faraday. Developed with a specialized set of functionalities that help users improve their own work. Do you remember yourself programming without an IDE? Well, Faraday does the same as an IDE does for you when programming, but from the perspective of a penetration test.

![GUI - QT](https://raw.github.com/wiki/infobyte/faraday/images/Faraday-Mainwindow.png)

Once the data is loaded Faraday crunches it into different visualizations useful not only for managers, but also for pentesters.

![GUI - Web](https://raw.github.com/wiki/infobyte/faraday/images/GUI_Dashboard_new.png)

To read about the latest features check out the [release notes](https://github.com/infobyte/faraday/blob/master/RELEASE.md)!

## Plugins list

Right now faraday has more than [50+ supported tools](https://github.com/infobyte/faraday/wiki/Plugin-List), among them you will find: 
![](https://raw.github.com/wiki/infobyte/faraday/images/plugins/Plugins.png)

##Installation

The following platforms are supported:

![platform](https://raw.github.com/wiki/infobyte/faraday/images/platform/supported.png) 

[Read more about this] (https://github.com/infobyte/faraday/wiki/Installation).

#### Quick install

Download the [latest tarball](https://github.com/infobyte/faraday/tarball/master) or clone the [Faraday Git Project](https://github.com/infobyte/faraday repository):

```
$ git clone https://github.com/infobyte/faraday.git faraday-dev
$ cd faraday-dev
$ ./install.sh
$ ./faraday.py
```

##Features

### Workspaces
Information is classified in **Workspace** units. Each Workspace maps into a pentest team's assignments containing all the intel discovered by that team.

### IntelliSense
Using CTRL+SPACE in the console for the different commands for example nikto CTRL+SPACE will show the nikto options, or you can use it to get ip or hostname which is in the HostTree for example $ 127.0[CTRL+SPACE] will complete to 127.0.0.1 if we have that ip in the HostTree

### Conflicts
If two plugins have different information for the same element it will generate a conflict that the user will have to resolve.  
For example, **user1** incorporates host *127.0.0.1 OS:Linux* and **user2** incorporates *127.0.0.1 OS: Linux Ubuntu 13.10*. The [QT interface](https://github.com/infobyte/faraday/wiki/Usage#gui-qt) will show a number next to the name of the Workspace, this is the amount of conflicts that have to be resolved. To resolve, right-click and select "Resolve conflicts", then select the object you wish to keep and that's it!

### Faraday plugin
Using our plugin you can do different actions using the command line, for example:

```
$ cd $faraday/bin/
$ #Adding new hosts 
$./fplugin -e 'for h in api.createAndAddHost("8.8.8.8","Linux")'
$ #Get all ip of HostTree
$ ./fplugin -e 'for h in api.__model_controller.getAllHosts(): print h.name' > allhost.txt
$ nmap -i allhost.txt
```

Read more about the [[Faraday Plugin]].

### Notifications
Updating objects on faraday now results in a beautiful notification in the QT ui

![](https://raw.github.com/wiki/infobyte/faraday/images/faraday_notifications.png)
![](https://raw.github.com/wiki/infobyte/faraday/images/faraday_notifications_more.png)

#### ZSH UI no-gui notifications
![](https://raw.githubusercontent.com/wiki/infobyte/faraday/images/faraday_gui_notifi.png)

### CSV Exporting & Importing
[More information](Exporting-the-information)

## Links

* Homepage: http://faradaysec.com
* User's manual: https://github.com/infobyte/faraday/wiki
* Download: [.tar.gz] (https://github.com/infobyte/faraday/tarball/master)
* Commits RSS feed: https://github.com/infobyte/faraday/commits/master.atom
* Issue tracker: https://github.com/infobyte/faraday/issues
* Frequently Asked Questions (FAQ): https://github.com/infobyte/faraday/wiki/FAQ
* Mailing list subscription: https://groups.google.com/forum/#!forum/faradaysec
* Twitter: [@faradaysec] (https://twitter.com/faradaysec)
* [Demos] (https://github.com/infobyte/faraday/wiki/Demos)
* IRC: [ircs://irc.freenode.net/faraday-dev] (ircs://irc.freenode.net/faraday-dev) [WebClient](https://webchat.freenode.net/?nick=wikiuser&channels=faraday-dev&prompt=1&uio=d4)
* Screenshots: https://github.com/infobyte/faraday/wiki/Screenshots

## Presentation
* Black Hat Arsenal Asia - 2016:
   * https://www.blackhat.com/asia-16/arsenal.html#faraday

* Black Hat Arsenal Europe - 2015:
   * https://www.blackhat.com/eu-15/arsenal.html#faraday

* Black Hat Arsenal USA - 2015:
   * https://www.blackhat.com/us-15/arsenal.html#faraday
   * http://blog.infobytesec.com/2015/08/blackhat-2015_24.html

* RSA - 2015:
   * http://www.rsaconference.com/events/us15/expo-sponsors/exhibitor-list/1782/infobyte-llc
   * http://blog.infobytesec.com/2015/05/infobyte-en-la-rsa-2015.html

* Ekoparty Security Conference - 2014:
   * https://www.youtube.com/watch?v=_j0T2S6Ppfo

* Black Hat Arsenal - 2011
   * http://www.infobytesec.com/down/Faraday_BH2011_Arsenal.pdf

* Ekoparty Security Conference - 2010:
   * http://prezi.com/fw46zt6_zgi8/faraday/
   * http://vimeo.com/16516987