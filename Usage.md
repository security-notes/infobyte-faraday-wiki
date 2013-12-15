Faraday main windows is quickly simple:  

![](https://raw.github.com/wiki/infobyte/faraday/images/Faraday-Mainwindow.png)

It's separated in Console, HostTree, Log Console, Item Info & Editing

Every command that you execute will be intercepted and if we have a plugin the information regarding a pentest like ip, hostnames, vulnerabilities, websites, notes, etc  will be added to Faraday.

The following list have different features availables.
#Highlight#
Console support highlighting of every hostname or ip with is in the HostTree. If we double click the highlight will be select the host int he HostTree.
#Plugins#
We have 3 kind of plugins:
 * Plugins that intercept commands (directly detected when you execute commands in the console)  
 * Plugins that import file reports (you have to copy the report to $HOME/.faraday/report/[workspacename] and faraday will detect the report, process and added to the HostTree.
 * Plugins connectors or online (BeEF, Metasploit, Burp) connect directly with external API or database or connect with Faraday RPC API.   

#IntelliSense#
Using CTRL+SPACE in the console for the different commands for example nikto CTRL+SPACE will show the nikto options, or you can use it to get ip or hostname which is in the HostTree for example $ 127.0[CTRL+SPACE] will complete to 127.0.0.1 if we have that ip in the HostTree  
#Databases#
By default faraday use local file database if you like to sincronize you have to configure [CouchDB] to share information in real time.  
#Conflicts#
If two plugins have different information for the same element it will generate a conflict that the user have to resolve. For example user1 incorporate host 127.0.0.1 OS:Linux and user2 incorporate 127.0.0.1 OS: Linux Ubuntu 13.10. In the name of workspace will include for example "Untitle (1)" (1) is the numbers of conflicts that you have. To resolve do double click and select "Resolve conflicts" then select with object do you like to persist.  
#Filters#
Hostree filter is used to filter the information you can use the following parameters (ip, hostname, mac, os, port, srvname, owned, vuln, note, noten, vulnn) For example to search ip 127.0.0.1 and port 22 write "ip:127.0.0.1 AND port:22"  