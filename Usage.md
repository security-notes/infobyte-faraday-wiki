Faraday main windows is simple:  

![](https://raw.github.com/wiki/infobyte/faraday/images/Faraday-Mainwindow.png)

Structured in panes: Main Console, HostTree, Log Console, Item Info & Editing panes.

Every command that you execute is intercepted and a handler is invoked in order to transparently import the newly generated information by the tool in the context of the pentest like ip addresses, hostnames, services, vulnerabilities, websites, notes, etc.

No manual imports needed but supported. Just drop your fresh generated reports in :
    $ ~/.faraday/report/workspace_name

Faraday imports the imported documents.

The following list have different features available:
#Database#
By default Faraday uses  a local file database. If you like to synchronize with others users you have to configure [CouchDB](CouchDB) to share information in real time.  
#Workspaces#
Information is classified in workspaces units. Each Workspace maps into one/many a pentest assignment/s. 
Each workspace contains the gathered information for each pentesting assignment. In it you can find all the intel you have discovered.

#Highlight#
Console support highlighting of every hostname or ip with is in the HostTree. If we double click the highlight will be select the host int he HostTree.
#Plugins#
We have 3 kind of plugins:
 * Plugins that intercept commands (directly detected when you execute commands in the console)  
 * Plugins that import file reports (you have to copy the report to $HOME/.faraday/report/[workspacename] and faraday will detect the report, process and added to the HostTree.
 * Plugins connectors or online (BeEF, Metasploit, Burp) connect directly with external API or database or connect with Faraday RPC API.   

#IntelliSense#
Using CTRL+SPACE in the console for the different commands for example nikto CTRL+SPACE will show the nikto options, or you can use it to get ip or hostname which is in the HostTree for example $ 127.0[CTRL+SPACE] will complete to 127.0.0.1 if we have that ip in the HostTree  
#Conflicts#
If two plugins have different information for the same element it will generate a conflict that the user have to resolve.  
For example **user1** incorporate host 127.0.0.1 OS:Linux and **user2** incorporate 127.0.0.1 OS: Linux Ubuntu 13.10. In the name of workspace will include for example "Untitle (1)" (1) is the numbers of conflicts that you have. To resolve, right-click and select "Resolve conflicts" then select which object do you like to keep.  
#Filters#
Hostree filter is a small search engine over the current Model Objects that provide filtering capabilities to the view. Currently you can filter by the following fields (ip, hostname, mac, os, port, srvname, owned, vuln, note, noten, vulnn), you can also negate the filter and use boolean connectors.
  
For example to search ip 127.0.0.1 and port 22 write "ip:127.0.0.1 AND port:22"  

#Faraday plugin#
Using our plugin you can do different actions using the command line, for example
```
$ cd ~/.faraday/bin/
$ #Adding new hosts 
$./fplugin -e 'for h in api.createAndAddHost("8.8.8.8","Linux")'
$ #Get all ip of HostTree
$ ./fplugin -e 'for h in api.__model_controller.getAllHosts(): print h.name' > allhost.txt
$ nmap -i allhost.txt
```

You can use presets actions using the included files (delAllServiceClosed.py, getAllCreds.py, getAllHosts.py, getAllIps.py, getAllVulnsCSV.py, etc) for example:

```
$ cd ~/.faraday/bin/
$ #Get all ip of HostTree
$ ./fplugin -f getAllIps.py > allhost.txt
$ nmap -i allhost.txt
```
