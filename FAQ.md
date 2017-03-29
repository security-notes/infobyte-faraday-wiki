<a name="index"></a>

* [Where does the name come from?](#name)
* [What is Faraday?](#what-is-faraday)
* [Is Faraday free?](#price)
* [Which platforms are supported?](#supported-platforms)
* [I purchased a License, now what?](#after-purchase)
* [What version am I using!?](#faraday-version)
* [How do I configure my own Vulnerabilities Database?](#vulns-db)
* [What if I want to add a Vulnerability manually?](#adding-manually)
* [How do I bind Faraday to 0.0.0.0?](#0.0.0.0)


<a name="name"></a>
### Where does the name come from?
The name was picked to honour *Michael Faraday*, an English scientist whose main discoveries include electromagnetism induction, diamagnetism and electrolysis[1]. Mainly his six principles of scientific discipline, acquired at a young age from Isaac Watts' "The Improvement of the mind"[2]:

* Always carry a small pad to take notes at any time
* Maintain abundant correspondence
* Collaborate regularly with others to exchange ideas
* Avoid controversy
* Verify everything that was said to him
* Do not generalize, speak and write as precisely as possible

[1] https://en.wikipedia.org/wiki/Michael_Faraday

[2] http://www.eng.auburn.edu/~sjreeves/cm/improve.html

[ [index] ](#index)

<a name="what-is-faraday"></a>
### What is Faraday?
Faraday is to Penetration Testing what an IDE is to Development. The main purpose of Faraday is to re-use the available tools in the community to take advantage of them in a multiuser way.

[ [index] ](#index)

<a name="price"></a>
### Is Faraday free?
Yes, we have a community version which is totally free, you can [download it from Github](https://github.com/infobyte/faraday/archive/master.zip).

We also develop two [commercial versions](https://www.faradaysec.com/#download).

![](https://www.faradaysec.com/images/Features-Comparation.png)

[ [index] ](#index)

<a name="supported-platforms"></a>
### Which platforms are supported?
ArchAssault, Archlinux, Debian, Kali, OSX, Ubuntu. You can find a detailed explanation [here](https://github.com/infobyte/faraday/wiki/installation-client).

[ [index] ](#index)

<a name="after-purchase"></a>
### I purchased a License, now what?
You will receive an email with a link to download two tarballs. One will be your Faraday License and the other the version you selected. Uncompress both and place the contents of the license tar inside **$FARADAY/doc/**. 

[ [index] ](#index)

<a name="faraday-version"></a>
### How do I know which Faraday Version I'm using?
So if you already have a Faraday Installation there are many ways to know which version you're using:

* Using the Web UI - If you place the pointer over the Faraday Logo you will get a tooltip containing the version number ![](https://raw.githubusercontent.com/wiki/infobyte/faraday/images/faraday_webui_version.png)

* Checking the contents of the file `VERSION` in the root of the Faraday Installation
![](https://raw.githubusercontent.com/wiki/infobyte/faraday/images/faraday_version_file.png)

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
