#Only in QT3 UI
Using our plugin you can do different actions in the command line of QT3 , for example

```
$ cd $faraday/bin/
$ #Adding new hosts 
$./fplugin -e 'for h in api.createAndAddHost("8.8.8.8","Linux")'
$ #Get all ip of HostTree
$ ./fplugin -e 'for h in api.__model_controller.getAllHosts(): print h.name' > allhost.txt
$ nmap -i allhost.txt
```

Faraday comes with some presets for bulk actions such as object removal, etc. These are usually necessary when managing large Workspaces. The current presets are:

* delAllHost.py
* delAllServiceClosed.py
* getAllCreds.py
* getAllHosts.py
* getAllIpsInterfaces.py
* getAllIps.py
* getAllOs.py
* getAllTelnet.py
* getAllVnc.py
* getAllVulnsCSV.py
* getAllWebservers.py
* getAllbySrv.py
* delAllVulnsWith.py
* getAllIpsNotServices.py
* getSeverityByCwe.py
* getExploits.py 

For example, getting all IPs in Host Tree to run nmap becomes a simple task:

```
$ cd ~/.faraday/bin/
$ ./fplugin -f getAllIps.py > allhost.txt
$ nmap -i allhost.txt
```

Many of these scripts have names that explain himself what they do, but some of these need some explanation.

#getSeverityByCwe.py

Get Vulnerabilities filtered by Severity and change this Severity based in CWE Vulnerability Database imported in Faraday.

Parameters:

1º : Filter by Severity (<=) (unclassified, info, low, med, high, critical, all)

2º : Url to Couchdb

3º : Workspace name

Example:

./fplugin.py -f getSeverityByCwe.py -p 'high http://username:password@localhost:5984/ workspace_test_name'

In this case, change vulnerabilities with severity high, med, low, info and unclassified.
Remember use ' in all the '-p' parameter.

#getExploits.py

This script get all CVEs of vulnerabilities in the active workspace and search for exploits in the vFeed database.
Support : Exploit-db, Metasploit, Milworm, D2, Saint.

Example:

./fplugin.py -f getExploits.py


You prefer a video about this? (2:40)

[GetExploits.py](https://www.youtube.com/watch?v=o5uSS6yzvCo)
