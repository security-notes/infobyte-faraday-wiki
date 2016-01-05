Using our plugin you can do different actions using the command line, for example
```
$ cd ~/.faraday/bin/
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

A usage example:

```
$ cd ~/.faraday/bin/
$ #Get all ip of HostTree
$ ./fplugin -f getAllIps.py > allhost.txt
$ nmap -i allhost.txt
```