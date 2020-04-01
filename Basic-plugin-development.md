This is an example of a Faraday Plugin that process a xml report.

Configure Custom Plugins Folder
---
To add custom plugins in faraday you first need to add the path where you have your plugins in the ```config.ini```

```shell script
custom_plugins_folder = /home/user/.faraday/plugins
```


Plugin Structure
----
Example structure

```shell script
example_tool/
    __init__.py
    plugin.py
```

Plugin Code
----

In this example we will create a plugin to analyze this XML
```xml
<?xml version="1.0" ?>
<!DOCTYPE example_tool>
<example_tool scanstart="Thu Nov  9 15:59:13 2017">
<details>
<item id="999979" ip="10.23.49.232" os="linux">
<uri>http://test.com/example.php</uri>
<issue severity="low">Some vuln text</issue>
</item>
<item id="39023023" ip="10.232.62.20" os="linux">
<uri>http://test.com/login.php</uri>
<issue severity="low">Some other text</issue>
</item>
<item id="8348343" ip="10.12.37.24" os="linux">
<uri>http://test.com/example.php</uri>
<issue severity="low">Yet another vuln text</issue>
</item>
<statistics elapsed="402" itemsfound="3" itemstested="10" />
</details>
</example_tool>
```

**plugin.py**

```python
from urllib.parse import urlparse
from faraday_plugins.plugins.plugin import PluginXMLFormat
import xml.etree.ElementTree as ET

class ExampleToolXmlParser:

    def __init__(self, xml_output):
        self.vulns = self.parse_xml(xml_output)

    def parse_xml(self, xml_output):
        vulns = []
        tree = ET.fromstring(xml_output)
        items = tree.iterfind('details/item')
        for item in items:
            ip = item.get('ip')
            os = item.get('os')
            uri = item.find('uri').text
            url = urlparse(uri)
            hostname = [url.netloc]
            path = url.path
            if url.scheme == 'https':
                port = 443
            else:
                port = 80
            issue = item.find('issue')
            severity = issue.get('severity')
            issue_text = issue.text
            vuln = {'ip': ip, 'uri': uri, 'os': os,
                    'hostname': hostname, 'port': port, 'path': path,
                    'issue_text': issue_text, 'severity': severity}
            vulns.append(vuln)
        return vulns


class ExampleToolPlugin(PluginXMLFormat):
    def __init__(self):
        super().__init__()
        self.identifier_tag = "example_tool"
        self.id = "example_tool"
        self.name = "Name of the tool"
        self.plugin_version = "0.0.1"

    def parseOutputString(self, output, debug=False):
        parser = ExampleToolXmlParser(output)
        for vuln in parser.vulns:
            h_id = self.createAndAddHost(vuln['ip'], vuln['os'], hostnames=vuln['hostname'])
            s_id = self.createAndAddServiceToHost(h_id, 'webserver', protocol='tcp', ports=vuln['port'])
            v_id = self.createAndAddVulnWebToService(h_id, s_id, vuln['issue_text'], severity=vuln['severity'],
                                                     path=vuln['path'])

def createPlugin():
    return ExampleToolPlugin()
```

The ```createPlugin``` function is the entry point, and it must return an instance of your plugin

#### Plugin classes

* PluginBase
    - PluginByExtension
        + PluginXMLFormat
        + PluginJsonFormat
        

```PluginBase``` is the base class, right now we support Xml (```PluginXMLFormat```) and Json (```PluginJsonFormat```) files but you can add other by creating a subclass of ```PluginByExtension```

In your plugin ```__init__``` you must define the ```id```, that will be the identifier of your plugin.

Beware that it must be unique, you can list all the plugins identifiers with this command: ```python -m faraday_plygins list```
##### PluginByExtension:
This class adds the functionality off identify a report by its extension by setting the variable ```extension``` int the ```__init__```

It can be one extension (".xml") o a list ("['.xml', '.xxx']") if your report can have multiple extensions
##### PluginXMLFormat:
Use this class if the plugin generates vulns from a xml file,  with a ```.xml``` extension

If your report has xml format but a different extension (like nessus), remember to define the ```extension``` variable
To identify the report set in the variable ```identifier_tag``` the main tag of the xml (example_tool in the example), it also can be one tag or a list of tags
```python
class ExampleXMLTool(PluginXMLFormat):

    def __init__(self):
        super().__init__()
        self.identifier_tag = 'tool_tag'
        self.extension = ".xml"
        self.open_options = {"mode": "rb"} # Here you cant specify the mode to open the file, also the encoding ("encoding": "utf-8")
```
##### PluginJsonFormat:
Use this class if the plugin generates vulns from a json file, with a ```.json``` extension

If yor report has json format but a different extension, remember to define the ```extension``` variable
To identify the report set in the variable ```json_keys``` a set with some of the identifiers keys of the json object
```python
class ExampleJsonTool(PluginJsonFormat):

    def __init__(self):
        super().__init__()
        self.json_keys = {'name', 'hosts'}
        self.extension = ".json"
```

##### PluginBase:
This class give you all the main methods to create hosts, services, vulnerabilities, credentials, etc.

```python
def createAndAddHost(self, name, os="unknown", hostnames=None, mac=None, scan_template="", site_name="",
                    site_importance="", risk_score="", fingerprints="", fingerprints_software=""):

def createAndAddServiceToHost(self, host_id, name, protocol="tcp?", ports=None, status="open", version="unknown",
                            description=""):

def createAndAddVulnToHost(self, host_id, name, desc="", ref=None, severity="", resolution="", vulnerable_since="", 
                            scan_id="", pci="", data="", external_id=None, run_date=None):

def createAndAddVulnToService(self, host_id, service_id, name, desc="", ref=None, severity="", resolution="", 
                            risk="", data="", external_id=None, run_date=None):

def createAndAddVulnWebToService(self, host_id, service_id, name, desc="", ref=None, severity="", resolution="",
                                website="", path="", request="", response="", method="", pname="",
                                params="", query="", category="", data="", external_id=None, run_date=None):
   
def createAndAddCredToService(self, host_id, service_id, username, password):
    
```

Test and Debug
----
You can test your plugin by enable the custom_plugins_folder setting, and try it with faraday


You can also test your plugin from the command line

##### Commands:
**List all available plugins**

Verify that the plugins is loaded by the plugin manager
```shell script
python -m faraday_plugins list

Available Plugins:
...
...
...
example_tool - Name of the tool
Loaded Plugins: 64
```

**Test plugin report detection**

Verify that your file is detected by your plugin

```shell script
python -m faraday_plugins detect /vagrant/example_tool.xml

Plugin: example_tool
```


**Test plugin process report**

Verify that your plugin parses the file ok and generate the json structure that will be loaded into faraday

```shell script
python -m faraday_plugins process example_tool  /vagrant/example_tool.xml


{"hosts": [{"ip": "10.23.49.232", "os": "linux", "hostnames": ["test.com"], "description": "", "mac": null, "credentials": [], "services": [{"name": "webserver", "protocol": "tcp", "port": 80, "status": "open", "version": "unknown", "description": "", "credentials": [], "vulnerabilities": [{"name": "Some vuln text", "desc": "", "severity": "low", "refs": [], "external_id": null, "type": "VulnerabilityWeb", "resolution": "", "data": "", "website": "", "path": "/example.php", "request": "", "response": "", "method": "", "pname": "", "params": "", "query": "", "category": ""}]}], "vulnerabilities": [], "scan_template": "", "site_name": "", "site_importance": "", "risk_score": "", "fingerprints": "", "fingerprints_software": ""}, {"ip": "10.232.62.20", "os": "linux", "hostnames": ["test.com"], "description": "", "mac": null, "credentials": [], "services": [{"name": "webserver", "protocol": "tcp", "port": 80, "status": "open", "version": "unknown", "description": "", "credentials": [], "vulnerabilities": [{"name": "Some other text", "desc": "", "severity": "low", "refs": [], "external_id": null, "type": "VulnerabilityWeb", "resolution": "", "data": "", "website": "", "path": "/login.php", "request": "", "response": "", "method": "", "pname": "", "params": "", "query": "", "category": ""}]}], "vulnerabilities": [], "scan_template": "", "site_name": "", "site_importance": "", "risk_score": "", "fingerprints": "", "fingerprints_software": ""}, {"ip": "10.12.37.24", "os": "linux", "hostnames": ["test.com"], "description": "", "mac": null, "credentials": [], "services": [{"name": "webserver", "protocol": "tcp", "port": 80, "status": "open", "version": "unknown", "description": "", "credentials": [], "vulnerabilities": [{"name": "Yet another vuln text", "desc": "", "severity": "low", "refs": [], "external_id": null, "type": "VulnerabilityWeb", "resolution": "", "data": "", "website": "", "path": "/example.php", "request": "", "response": "", "method": "", "pname": "", "params": "", "query": "", "category": ""}]}], "vulnerabilities": [], "scan_template": "", "site_name": "", "site_importance": "", "risk_score": "", "fingerprints": "", "fingerprints_software": ""}], "command": {"tool": "example_tool", "command": "example_tool", "params": "/vagrant/example_tool.xml", "user": "faraday", "hostname": "", "start_date": "2020-04-01T18:43:34.552623", "duration": 2650, "import_source": "report"}}
```


If you dont have faraday-server installed or dont have the custom_plugins_folder setting, you can use the ```--custom_plugins_folder``` parameter with any if the commands (list, detect and process)

Example:
```shell script
python -m faraday_plugins list --custom-plugins-folder /home/user/.faraday/plugins/
```

**Debug**

In the ```PluginBase``` there is a logger defined in ```self.logger``` that you can use.

If you need to debug for plugins with the command line set this variable:

```shell script
export PLUGIN_DEBUG=1
export PLUGIN_DEBUG=1
python -m faraday_plugins process appscan /path/to/report.xml
2019-11-15 20:37:03,355 - faraday.faraday_plugins.plugins.manager - INFO [manager.py:113 - _load_plugins()]  Loading Native Plugins...
2019-11-15 20:37:03,465 - faraday.faraday_plugins.plugins.manager - DEBUG [manager.py:123 - _load_plugins()]  Load Plugin [acunetix]
2019-11-15 20:37:03,495 - faraday.faraday_plugins.plugins.manager - DEBUG [manager.py:123 - _load_plugins()]  Load Plugin [amap]
2019-11-15 20:37:03,549 - faraday.faraday_plugins.plugins.manager - DEBUG [manager.py:123 - _load_plugins()]  Load Plugin [appscan]
2019-11-15 20:37:03,580 - faraday.faraday_plugins.plugins.manager - DEBUG [manager.py:123 - _load_plugins()]  Load Plugin [arachni]
2019-11-15 20:37:03,613 - faraday.faraday_plugins.plugins.manager - DEBUG [manager.py:123 - _load_plugins()]  Load Plugin [arp_scan]
2019-11-15 20:37:03,684 - faraday.faraday_plugins.plugins.manager - DEBUG [manager.py:123 - _load_plugins()]  Load Plugin [beef]
2019-11-15 20:37:03,714 - faraday.faraday_plugins.plugins.manager - DEBUG [manager.py:123 - _load_plugins()]  Load Plugin [brutexss]
2019-11-15 20:37:03,917 - faraday.faraday_plugins.plugins.manager - DEBUG [manager.py:123 - _load_plugins()]  Load Plugin [burp]
2019-11-15 20:37:03,940 - faraday.faraday_plugins.plugins.manager - DEBUG [manager.py:123 - _load_plugins()]  Load Plugin [dig]
...
```
