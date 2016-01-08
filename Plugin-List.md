Supported Tools:
---
Right now faraday has more that 40+ supported tools, among them you will find: 
![](https://raw.github.com/wiki/infobyte/faraday/images/plugins/Plugins.png)

<a name="types"></a>
There are three kinds of plugins available for Faraday:

 * CONSOLE - Plugins that intercept commands, fired directly when a command is detected in the console. These are transparent to you and no additional action on your part is needed.
 * REPORT - Plugins that import file reports. You have to copy the report to **$HOME/.faraday/report/[workspacename]** (replacing **[workspacename]** with the actual name of your Workspace) and Faraday will automatically detect, process and add it to the HostTree.
 * API - Plugin connectors or online (BeEF, Metasploit, Burp), these connect to external APIs or databases, or talk directly to Faraday's RPC API.

If you think your favorite tool is missing [code your own plugin](https://github.com/infobyte/faraday/wiki/Basic-plugin-development) or [ask us to do it](https://github.com/infobyte/faraday/issues/new)!

* [Retina] (http://www.beyondtrust.com/Products/RetinaNetworkSecurityScanner/) (REPORT) (XML) 
* [Openvas](https://twitter.com/openvas) (REPORT) (XML) 
* [BeEF](https://twitter.com/beefproject) (API)
* [Qualysguard] (https://www.qualys.com/) (REPORT) (XML) 
* [Arachni](https://twitter.com/ArachniScanner) (REPORT, CONSOLE) (XML) 
* [Hydra] (https://www.thc.org/thc-hydra) (CONSOLE) (XML) 
* [Acunetix](https://twitter.com/acunetix) (REPORT) (XML) 
* [Dnsenum] (https://github.com/fwaeytens/dnsenum) (CONSOLE)
* [Nessus](https://twitter.com/tenablesecurity), (REPORT) (XML .nessus)
* [Sqlmap](https://twitter.com/sqlmap) (CONSOLE)
* ftp (CONSOLE)
* Listurls (CONSOLE)
* whois (CONSOLE)
* [Wapiti] (http://wapiti.sourceforge.net/) (CONSOLE)
* [Netsparker](https://twitter.com/Netsparker) (REPORT) (XML)
* [W3af](https://twitter.com/w3af) (REPORT) (XML)
* ping (CONSOLE)
* Telnet (CONSOLE)
* [Dnsmap] (https://github.com/makefu/dnsmap) (CONSOLE)
* [Amap] (https://www.thc.org/thc-amap/) (CONSOLE)
* [arp-scan] (http://linux.die.net/man/1/arp-scan) (CONSOLE) 
* [Fierce] (http://tools.kali.org/information-gathering/fierce) (CONSOLE)
* [X1, Onapsis](https://twitter.com/onapsis) (REPORT) (XML) 
* [Burp, BurpPro](https://twitter.com/Burp_Suite) (REPORT, API) (XML)
* [Metasploit](https://twitter.com/metasploit), (REPORT, API) (XML) XML report
* [Metagoofil] (https://code.google.com/p/metagoofil/downloads/list) (CONSOLE) 
* [Dnswalk] (https://github.com/leebaird/discover) (CONSOLE) 
* [Goohost] (http://www.aldeid.com/wiki/Goohost) (CONSOLE) 
* [Theharvester] (https://github.com/laramies/theHarvester) (CONSOLE) 
* [Nikto] (https://cirt.net/Nikto2) (REPORT, CONSOLE) (XML) 
* [Core Impact, Core Impact](https://twitter.com/CoreSecurity) (REPORT) (XML)
* [Reverseraider](http://sourceforge.net/projects/complemento/files/) (CONSOLE) 
* [propecia] (http://packetstormsecurity.com/files/14232/propecia.c.html) (CONSOLE) 
* [Dnsrecon] (https://github.com/darkoperator/dnsrecon) (CONSOLE) 
* [Skipfish](https://code.google.com/p/skipfish/) (CONSOLE) 
* [Nmap](https://twitter.com/nmap) (REPORT, CONSOLE) (XML) 
* [Medusa] (http://h.foofus.net/?page_id=51 ) (CONSOLE)
* [Nexpose, Nexpose Enterprise](https://twitter.com/rapid7), (REPORT) (simple XML, XML Export plugin (2.0))
* [Zap](https://twitter.com/zaproxy) (REPORT) (XML)
* [Webfuzzer](http://gunzip.altervista.org/g.php?f=projects#webfuzzer) (CONSOLE)
* [Shodan](https://twitter.com/shodanhq) (API)
* [evilgrade](http://twitter.com/infobytesec) (API)
* [masscan](https://twitter.com/ErrataRob) (REPORT, CONSOLE) (XML)
* Dig (CONSOLE)
* Traceroute (CONSOLE)
* [Immunity Canvas](http://www.immunityinc.com/products/canvas/) (API)
* [Peeping Tom](https://bitbucket.org/LaNMaSteR53/peepingtom/) (CONSOLE)
* [SSHdefaultscan](https://github.com/atarantini/sshdefaultscan) (CONSOLE)
* [PasteAnalyzer](https://github.com/Ezequieltbh/pasteAnalyzer) (CONSOLE)