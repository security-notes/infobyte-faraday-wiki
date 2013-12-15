Plugin development is really simple.

All the plugins are in:

    $faraday/plugins/repo/[pluginname]

In the following example you can see simple plugin development of command ping

    from plugins import core
    from model import api
    import re
    import os
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
                                "":"[-LRUbdfnqrvVaAB]  [-c  count]  [-m  mark]  [-i interval] [-l preload] [-p pattern] [-s packetsize] [-t ttl] [-w deadline] [-F flowlabel] [-Iinterface] [-M hint] [-N nioption] [-Q tos] [-S sndbuf] [-T     timestamp option] [-W timeout] [hop ...] destination",
                                    "-a":"Audible ping.",
                                    #...
                                  }
    
        def parseOutputString(self, output, debug = False):
    
            reg=re.search(r"PING ([\w\.-:]+)( |)\(([\w\.:]+)\)", output)
            if re.search("0 received|unknown host",output) is None and reg is not None:
    
                ip_address = reg.group(3)
                hostname=reg.group(1)
    
    
                h_id = self.createAndAddHost(ip_address)
                if self._isIPV4(ip_address):
                    i_id = self.createAndAddInterface(h_id, ip_address, ipv4_address=ip_address, hostname_resolution=[hostname])
                else:
                    i_id = self.createAndAddInterface(h_id, ip_address, ipv6_address=ip_address, hostname_resolution=[hostname])
    
            return True
    
        def _isIPV4(self, ip):
            if len(ip.split(".")) == 4:
                return True
            else:
                return False
    
        def processCommandString(self, username, current_path, command_string):
            """
            """
            return None
    
    def createPlugin():
    return CmdPingPlugin()