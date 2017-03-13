In order to manage, extract and list information stored in faraday we created _fplugin_, a simple plugin that allows you to interact directly with our Python API from the command line.

Using our plugin located in ```$faraday/bin/``` you can do different actions from the command line

```
❯❯  ./fplugin -h
usage: fplugin [-h] [-f FILE] [-w WORKSPACE] [-u URL]

Using our plugin you can do different actions in the command line and interact
with Faraday. Faraday comes with some presets for bulk actions such as object
removal, get object information, etc.

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  Script file. Example: ./fplugin -f getAllIps.py
  -w WORKSPACE, --workspace WORKSPACE
                        Use workspace
  -u URL, --url URL     Faraday Server URL. Example: http://localhost:5985
```

Usage Examples:

### List all running HTTP services

The following command will list all running services exposed on common HTTP ports (services with ports 80, 8080, 443, 8443 open) 
```
$./fplugin -f getAllbySrv.py  -u http://localhost:5985 -w demoworkspace
http
upnp
http
http
http
```

### Get all IPs
```
$ ./fplugin -f getAllIps.py -u http://localhost:5985 -w demoworkspace
192.168.0.1
192.168.0.2
...
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

Many of these scripts have names that explain himself what they do.

## Note

The Faraday Plugin was overhauled, and breaking changes will be released in the next version.