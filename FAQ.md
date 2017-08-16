<a name="index"></a>
## Index

* [Where does the name come from?](#name)
* [What is Faraday?](#what-is-faraday)
* [Is Faraday free?](#price)
* [Does Faraday have collaboration tools?](#plugins)
* [Which platforms are supported?](#supported-platforms)
* [Does Faraday work on my servers or on the cloud?](#server_cloud)
* [What are the system requirements to run Faraday?](#systemreq)
* [I purchased a License, now what?](#after-purchase)
* [Can I keep using the Kali version with my newly bought pro/corp license?](#upgrade-kali)
* [Can I install the Server and/or Client in my own box instead of using a Virtual Machine?](#native-install)
* [What version am I using?](#faraday-version)
* [How do I configure my own Vulnerabilities Database?](#vulns-db)
* [What if I want to add a Vulnerability manually?](#adding-manually)
* [How do I bind Faraday to 0.0.0.0?](#0.0.0.0)

     
**Is your question not listed here? [Contact us](https://github.com/infobyte/faraday/issues)**


## Topics
<a name="name"></a>
### Where does the name come from?
The name was picked to honor *Michael Faraday*, an English scientist whose main discoveries include electromagnetism induction, diamagnetism and electrolysis. Mainly his six principles of scientific discipline, acquired at a young age from Isaac Watts' "The Improvement of the mind":
* Always carry a small pad to take notes at any time
* Maintain abundant correspondence
* Collaborate regularly with others to exchange ideas
* Avoid controversy
* Verify everything that was said to him
* Do not generalize, speak and write as precisely as possible

Read more at:  
https://en.wikipedia.org/wiki/Michael_Faraday   
http://www.eng.auburn.edu/~sjreeves/cm/improve.html

[ [index] ](#index)

<a name="what-is-faraday"></a>
### What is Faraday?
Faraday is a **multiuser integrated penetration test and vulnerability management environment**. It is to Penetration Testing what an IDE is to Development. The main purpose of Faraday is to re-use the available tools in the community to take advantage of them in a multiuser way.

[ [index] ](#index)

<a name="price"></a>
### Is Faraday free?
Yes, we have a community version which is totally free, you can [download it from Github](https://github.com/infobyte/faraday/archive/master.zip).

We also develop two [commercial versions](https://www.faradaysec.com/#download).

![](https://www.faradaysec.com/images/Features-Comparation.png)

[ [index] ](#index)

<a name="plugins"></a>
### Does Faraday have collaboration tools? 
Faraday supports over 60 tools   
Full plugin list: https://github.com/infobyte/faraday/wiki/PluginList

[ [index] ](#index)

<a name="supported-platforms"></a>
### Which platforms are supported?
ArchAssault, Archlinux, Debian, Kali, OSX, Ubuntu. You can find a detailed explanation [here](https://github.com/infobyte/faraday/wiki/installation-client).

[ [index] ](#index)

<a name="server_cloud"></a>
### Does Faraday work on my servers or on the cloud?
Both depending on your needs. For more information you can contact us at sales@infobytesec.com

[ [index] ](#index)

<a name="systemreq"></a>
### What are the system requirements to run Faraday?
CPU: 1 Dualcore 2GHz Intel CPU  
Disk: 30 GB  
Memory: 2 GB RAM (4 GB RAM recommended)  

Current tests include ​Debian​, ​Ubuntu​, ​Kali​, ​Backtrack​ and ​OSX Maverick 10.9.2​.

If instead of installing you want to take a quick look at Faraday you can also use [​Docker](https://github.com/infobyte/faraday/wiki/installation-client-docker)​.

[ [index] ](#index)

<a name="after-purchase"></a>
### I purchased a License, now what?
You will receive an email with a link to download two tarballs. One will be your Faraday License and the other the version you selected. Uncompress both and place the contents of the license tar inside **$FARADAY/doc/**. 

[ [index] ](#index)

<a name="upgrade-kali"></a>
### Can I keep using the Kali version with my newly bought Professional/Corporate license?
In a nutshell, yes. Even though the Kali Faraday version is incompatible with both the **Professional** and **Corporate** licenses, you can upgrade the platform in the same box without losing all your data.

Follow the [commercial update instructions](https://github.com/infobyte/faraday/wiki/Updates#commercial-version-update) to upgrade.

[ [index] ](#index)

<a name="native-install"></a>
### Can I install the Server and/or Client in my own box instead of using a Virtual Machine?

The **only** intended purpose for the **Faraday VM** is as a commercial demo.

For production environments we recommend doing a fresh install in a Ubuntu Server and do not recommend using that Virtual Machine.

If the use of a Virtualized environment is a must-have, then we recommend doing a proper install in a fresh Virtual Machine following the regular installation steps.

[ [index] ](#index)

<a name="faraday-version"></a>
### How do I know which Faraday Version I'm using?
So if you already have a Faraday Installation there are many ways to know which version you're using:

* Using the `--version` or `-v` argument in both the Client and Server.

* Using the Web UI - If you place the pointer over the Faraday Logo you will get a tooltip containing the version number ![](https://raw.githubusercontent.com/wiki/infobyte/faraday/images/faraday_webui_version.png)

* Checking the contents of the file `VERSION` in the root of the Faraday Installation
![](https://raw.githubusercontent.com/wiki/infobyte/faraday/images/faraday_version_file.png)

To get the latest available version:

* for the community version, visit <https://github.com/infobyte/faraday/releases/latest>
* for the commercial versions, check the Customer Portal

[ [index] ](#index)

<a name="vulns-db"></a>
### How do I configure my own Vulnerabilities Database?
Check out our [[Vulnerabilities Database]] config page.

[ [index] ](#index)

<a name="adding-manually"></a>
### What if I want to add a Vulnerability manually?
You can do this using our WEB UI, read our documentation on [manually adding vulnerabilities](https://github.com/infobyte/faraday/wiki/Usage#vulnerability-creation).


[ [index] ](#index)

<a name="0.0.0.0"></a>
### How do I bind Faraday to 0.0.0.0?
Just go to ```~/.faraday/config/server.ini``` and inside the ```[faraday-server]``` section write:

`bind_address=0.0.0.0`

Restart Faraday Server if you had it running. That's it!

Read more about [configuring the Server](https://github.com/infobyte/faraday/wiki/configuration-server).

[ [index] ](#index)  

Is your question not listed here? [Contact us](https://github.com/infobyte/faraday/issues)