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
Yes, we have a Community version which is totally free, you can [download it from Github](https://github.com/infobyte/faraday/archive/master.zip).We also have two Commercial versions, details about those in our [webpage](https://www.faradaysec.com/#download).

![](https://www.faradaysec.com/images/workspace-diff/features-comparation.png)

[ [index] ](#index)

<a name="plugins"></a>
### Does Faraday have collaboration tools? 
Faraday supports over 70 tools. Full plugin list available [here](https://github.com/infobyte/faraday/wiki/PluginList).

[ [index] ](#index)

<a name="supported-platforms"></a>
### Which platforms are supported?
RedHat, CentOS, Fedora, Debian, Kali, OSX, Ubuntu.

[ [index] ](#index)

<a name="server_cloud"></a>
### Does Faraday work on my servers or on the cloud?
Both depending on your needs. For more information you can contact us at sales@infobytesec.com

[ [index] ](#index)

<a name="systemreq"></a>
### What are the system requirements to run Faraday?
CPU: 2 Dualcore 2GHz Intel CPU  
Disk: 40 GB  
Memory: 4 GB RAM (8 GB RAM recommended)  

Current tests include ​Debian​, ​Ubuntu​, ​Kali​, ​Backtrack​ and ​OSX Maverick 10.9.2​.

If instead of installing you want to take a quick look at Faraday you can also use [​Docker](https://github.com/infobyte/faraday/wiki/installation-docker)​.

[ [index] ](#index)

<a name="after-purchase"></a>
### I purchased a License, now what?
You will receive an email with a link to download everything regarding your license. If you haven’t received it or are having issues, please contact us at sales@infobytesec.com.

[ [index] ](#index)

<a name="upgrade-kali"></a>
### Can I keep using the Kali version with my newly bought Professional/Corporate license?
In a nutshell, yes. Even though the Kali Faraday version is incompatible with both the **Professional** and **Corporate** licenses, you can upgrade the platform in the same box without losing all your data.

You will need to remove the package `python-faraday` and then you need to install the pro/corp .deb with `apt install ./faraday-server_amd64.deb`

[ [index] ](#index)

<a name="native-install"></a>
### Can I install the Server and/or Client in my own box instead of using a Virtual Machine you provided?

The **only** intended purpose for the **Faraday VM** is as a commercial demo.

For production environments we recommend doing a fresh install in a Ubuntu Server, please do not use your provided Demo License VM.

If the use of a Virtualized environment is a must-have, then we recommend doing a proper install in a fresh Virtual Machine following the regular installation steps.

[ [index] ](#index)

<a name="faraday-version"></a>
### How do I know which Faraday Version I'm using?
By running faraday-server --version or hovering your mouse over the Faraday logo at the top left of the Web UI. Latest version and information available in the Upgrading Faraday section.

To get the latest available version:

* for the community version, visit <https://github.com/infobyte/faraday/releases/latest>
* for the commercial versions, check the Customer Portal

[ [index] ](#index)

<a name="adding-manually"></a>
### What if I want to add a Vulnerability manually?
You can do this using our Web UI, read our documentation on [manually adding vulnerabilities](https://github.com/infobyte/faraday/wiki/Status-Report#vulnerability-creation).


[ [index] ](#index)

<a name="0.0.0.0"></a>
### How do I bind Faraday to 0.0.0.0?
Just go to ```/home/faraday/.faraday/config/server.ini``` and inside the ```[faraday-server]``` section write:

`bind_address=0.0.0.0`

Restart Faraday Server if you had it running. That's it!

[ [index] ](#index)  

Is your question not listed here? [Contact us](https://github.com/infobyte/faraday/issues)
