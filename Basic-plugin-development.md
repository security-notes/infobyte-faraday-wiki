Plugin development is really simple.

All the plugins are in:

    $ faraday/faraday/client/plugins/repo/[pluginname]

In the following example you can see plugin of command ping:
``` python
    from plugins import core
    from model import api
    import re
    class CmdPingPlugin(core.PluginBase):
        """
        This plugin handles ping command.
        Basically detects if user was able to connect to a device
        """
        def __init__(self):
            core.PluginBase.__init__(self)
            self.id              = "ping"
            self.name            = "Ping"
            self.plugin_version         = "0.0.1"
            self.version  = "1.0.0"
            self._command_regex  = re.compile(r'^(sudo ping|ping|sudo ping6|ping6).*?')
            self._completition = {
                                "":"[-LRUbdfnqrvVaAB]  [-c  count]  [-m  mark]  [-i interval] ...",
                                    "-a":"Audible ping.",
                                    #...
                                  }
    
        def parseOutputString(self, output, debug = False):
            """
            This method will be called when the command finished executing and
            the complete output will be received to work with it
            Using the output the plugin can create and add hosts, services, etc.
            """
            reg=re.search(r"PING ([\w\.-:]+)( |)\(([\w\.:]+)\)", output)
            if re.search("0 received|unknown host",output) is None and reg is not None:
    
                ip_address = reg.group(3)
                hostname=reg.group(1)
                h_id = self.createAndAddHost(ip_address)
                s_id = self.createAndAddServiceToHost(self,h_id, service_name, protocol="tcp?", ports=[], status="open", version="unknown", description="")
                
    
            return True
    
        def processCommandString(self, username, current_path, command_string):
            """
            With this method a plugin can add aditional arguments to the command that
            it's going to be executed.
            """
            return None
    
    def createPlugin():
    return CmdPingPlugin()
```
In this plugin if the host is active we add it to the database

**Key information:**

```python
    self._command_regex
```
This is a regex used to match the command string and determine if the plugin is suitable to handle it.

```python
    self._completition
```
This have the dict used for intellisense. 

```python
    def parseOutputString(self, output, debug = False):
```
This method will be called when the command finished executing and
the complete output will be received to work with it. 
Using the output, the plugin can create and add hosts, services, vuln, webvuln, credentials, notes.

```python
    def processCommandString(self, username, current_path, command_string):
```
With this method a plugin can add additional arguments to the command that
it's going to be executed.


```python
    createAndAddHost(self, name, os="unknown", hostnames=None)
```
With this method we can create and add a host to the database.
```python
    createAndAddServiceToHost(self, 
                host_id, 
                name,
                protocol="tcp?", 
                ports=[],
                status="open", 
                version="unknown",
                description=""):
```
With this method we can create and add a service to a host.

**core.PluginBase**

Besides the two methods above, this is the complete list of methods in the PluginBase:
```python
    def createAndAddVulnToHost(self, 
                host_id,
                name,
                desc="", 
                ref=[],
                severity="", 
                resolution=""):
    
    def createAndAddVulnToService(self,
                host_id, 
                service_id, 
                name, 
                desc="",                  
                ref=[], 
                severity="", 
                resolution=""):
    
    def createAndAddVulnWebToService(self, 
                host_id, 
                service_id, 
                name, 
                desc="",
                ref=[], 
                severity="", 
                resolution="",                     
                website="", 
                path="", 
                request="",
                response="", 
                method="", 
                pname="",
                params="", 
                query="", 
                category=""):    
    
    def createAndAddNoteToHost(self, 
                host_id, 
                name, 
                text):
    
    def createAndAddNoteToService(self,
                host_id, 
                service_id, 
                name,
                text):
    
    def createAndAddNoteToNote(self, 
                host_id, 
                service_id, 
                note_id, 
                name, 
                text):
    
    def createAndAddCredToService(self, 
                host_id, 
                service_id, 
                username, 
                password):
        
    def log(self, msg, level='INFO'):
    
    def devlog(self, msg): 
```
