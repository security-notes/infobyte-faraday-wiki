In many parts of the Web UI you will see a icon to search the host or service information in Shodan:

![Search in Shodan](https://raw.github.com/wiki/infobyte/faraday/images/OSINT-provider/shodan.png) 

You can modify this to use any other service you want by by changing the `<osint>` line in your `~/.faraday/config/user.xml` file and restarting the Faraday server. For example, with this one you can use Censys:
```xml
<osint>
{"host": "censys.io",
"prefix": "/ipv4?q=",
"suffix": "",
"use_external_icon": true,
"icon": "https://censys.io/static/img/icon.png",
"label": "Censys"}
</osint>
```
![Search in Censys](https://raw.github.com/wiki/infobyte/faraday/images/OSINT-provider/censys.png)

Or with this code it will use NetDB:
```xml
<osint>
{"host": "netdb.io",
"prefix": "/search?q=",
"suffix": "",
"icon": "netdb",
"use_external_icon": false,
"label": "NetDB"}
</osint>
```
![Search in NetDB](https://raw.github.com/wiki/infobyte/faraday/images/OSINT-provider/netdb.png) 

As you see, you will have to put a JSON inside the <osint> tag. This are the important keys to set:
* host, prefix and suffix determine the link to the OSINT provider. For example, in the censys example if you want to search for a host with the IP 127.0.0.1, you will be taken to http://censys.io/ipv4?q=127.0.0.1 when you click the OSINT icon.
* The label defines the text that will be shown when you place the mouse over the icon.
* icon defines the path to the image with the provider's logo. If use_external_icon is true, it has to be a full URL. If it is false, the icon value has to be the name of a file in the server/www/images/ directory, without the extension (it must be png)