The main purpose of Faraday is to re-use the available tools in the community to take advantage of them in a multiuser way.

> You break it. We keep track of the pieces!

To maximize flexibility Faraday Plugins run only on the client, which means you can have custom, private plugins all for yourself!

<a name="types"></a>
There are three kinds of plugins available for Faraday; **console**, **report** and **API** also called **online**. However, these are not mutually exclusive, meaning that some tools have more than one Plugin to process their output. For example, **Nmap** has a Console plugin which allows you to run it directly from ZSH, but it also has a Report one, in order to import scans that were run outside of Faraday.

### Console

Plugins that intercept commands, fired directly when a command is detected in the console. These are transparent to you and no additional action on your part is needed.

### Report

Plugins that import file reports. You have to copy the report to ```~/.faraday/report/{workspacename}``` (replacing **{workspacename}** with the actual name of your Workspace) and Faraday GTK client will automatically detect, process and add it to the HostTree.

If Faraday is not capable to detect the plugin needed to process the report, you can manually choose which plugin will be used by adding ```_faraday_pluginName``` to the file name before the extension.

For example, if the **Burp** report named ```burp_1456983368.xml``` is not being recognized, try renaming it to ```Burp_1456983368_faraday_Burp.xml```. Now copy it to the Workspace directory and Faraday should now run the plugin and import all vulnerabilities.

Keep in mind that this functionality is **case sensitive**.


### API

Plugin connectors or online ([[BeEF]], [[Metasploit]], [Burp](https://github.com/infobyte/faraday/wiki/Burp-proxy-extender)), these connect to external APIs or databases, or talk directly to [Faraday's RPC API](https://github.com/infobyte/faraday/wiki/APIs).

### List

If you think your favourite tool is missing [code your own plugin](https://github.com/infobyte/faraday/wiki/Basic-plugin-development) or [ask us to do it](https://github.com/infobyte/faraday/issues/new)!


* [Acunetix](https://twitter.com/acunetix) (REPORT) (XML)
* [Amap](https://www.thc.org/thc-amap/) (CONSOLE)
* [Arachni](https://twitter.com/ArachniScanner) (REPORT, CONSOLE) (XML)
* [arp-scan](http://linux.die.net/man/1/arp-scan) (CONSOLE)
* [BeEF](https://twitter.com/beefproject) (API)
* [Brutexss](https://github.com/rajeshmajumdar/BruteXSS) (REPORT)
* [Burp, BurpPro](https://twitter.com/Burp_Suite) (REPORT, API) (XML)
* [Core Impact, Core Impact](https://twitter.com/CoreSecurity) (REPORT) (XML)
* Dig (CONSOLE)
* [Dirb](http://tools.kali.org/web-applications/dirb) (CONSOLE)
* Dirsearch (REPORT,CONSOLE)
* [Dnsenum](https://github.com/fwaeytens/dnsenum) (CONSOLE)
* [Dnsmap](https://github.com/makefu/dnsmap) (CONSOLE)
* [Dnsrecon](https://github.com/darkoperator/dnsrecon) (CONSOLE)
* [Dnswalk](https://github.com/leebaird/discover) (CONSOLE)
* [evilgrade](http://twitter.com/infobytesec) (API)
* [Fierce](http://tools.kali.org/information-gathering/fierce) (CONSOLE, REPORT)
* [Fruitywifi](http://www.fruitywifi.com/index_eng.html) (API)
* ftp (CONSOLE)
* [Goohost](http://www.aldeid.com/wiki/Goohost) (REPORT, CONSOLE) (XML)
* [hping3](http://tools.kali.org/information-gathering/hping3) (CONSOLE)
* [Hydra](https://www.thc.org/thc-hydra) (CONSOLE) (XML)
* [Immunity Canvas](http://www.immunityinc.com/products/canvas/) (API)
* Ip360 (REPORT)
* [Lynis](https://cisofy.com/lynis/) (REPORT)
* Listurls (CONSOLE)
* [Maltego](https://www.paterva.com/web6/products/maltego.php) (REPORT)
* [masscan](https://twitter.com/ErrataRob) (REPORT, CONSOLE) (XML)
* [Medusa](http://h.foofus.net/?page_id=51 ) (CONSOLE)
* [Metagoofil](https://code.google.com/p/metagoofil/downloads/list) (CONSOLE)
* [Metasploit](https://twitter.com/metasploit), (REPORT, API) (XML) XML report
* [Ndiff](https://nmap.org/ndiff/) (REPORT, CONSOLE)
* [Nessus](https://twitter.com/tenablesecurity), (REPORT) (XML .nessus)
* [Netcat](http://netcat.sourceforge.net/) (CONSOLE)
* Netdiscover (CONSOLE)
* [Netsparker](https://twitter.com/Netsparker) (REPORT) (XML)
* Netsparker Cloud (REPORT)
* [Nexpose, Nexpose Enterprise](https://twitter.com/rapid7), (REPORT) (simple XML, XML Export plugin (2.0))
* [Nikto](https://cirt.net/Nikto2) (REPORT, CONSOLE) (XML)
* [Nmap](https://twitter.com/nmap) (REPORT, CONSOLE) (XML)
* [Openvas](https://twitter.com/openvas) (REPORT) (XML)
* [PasteAnalyzer](https://github.com/Ezequieltbh/pasteAnalyzer) (CONSOLE)
* [Peeping Tom](https://bitbucket.org/LaNMaSteR53/peepingtom/) (CONSOLE)
* ping (CONSOLE)
* [propecia](http://packetstormsecurity.com/files/14232/propecia.c.html) (CONSOLE)
* [Qualysguard](https://www.qualys.com/) (REPORT) (XML)
* [Recon-NG](https://hackertarget.com/recon-ng-tutorial/) (REPORT)
* [Retina](http://www.beyondtrust.com/Products/RetinaNetworkSecurityScanner/) (REPORT) (XML)
* [Reverseraider](http://sourceforge.net/projects/complemento/files/) (CONSOLE)
* Sentinel (API)
* [Shodan](https://twitter.com/shodanhq) (API)
* [Skipfish](https://code.google.com/p/skipfish/) (CONSOLE)
* [Sqlmap](https://twitter.com/sqlmap) (CONSOLE)
* [SSHdefaultscan](https://github.com/atarantini/sshdefaultscan) (CONSOLE)
* SSLcheck (CONSOLE)
* [SSLyze](https://github.com/nabla-c0d3/sslyze) (REPORT, CONSOLE) (XML)
* [Sublist3r](https://github.com/aboul3la/Sublist3r) (REPORT,CONSOLE)
* Telnet (CONSOLE)
* [Theharvester](https://github.com/laramies/theHarvester) (CONSOLE)
* Traceroute (CONSOLE)
* [W3af](https://twitter.com/w3af) (REPORT) (XML)
* [Wapiti](http://wapiti.sourceforge.net/) (CONSOLE)
* Wcscan (CONSOLE)
* [Webfuzzer](http://gunzip.altervista.org/g.php?f=projects#webfuzzer) (CONSOLE)
* [WebInspect](https://resources.infosecinstitute.com/webinspect/#gref) (REPORT,CONSOLE)
* [Wfuzz](https://wfuzz.readthedocs.io/en/latest/index.html) (CONSOLE)
* whois (CONSOLE)
* [WPScan](https://wpscan.org/) (CONSOLE)
* [Xsssniper](https://github.com/gbrindisi/xsssniper) (REPORT)
* [X1, Onapsis](https://twitter.com/onapsis) (REPORT) (XML)
* [Zap](https://twitter.com/zaproxy) (REPORT) (XML)