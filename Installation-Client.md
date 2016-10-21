<a name="index"></a>
* [Faraday Client](#faraday-client)
* [Requirements](#requirements)
* [Debian & Ubuntu & Backtrack](#debian)
* [ArchLinux](#arch)
* [Kali](#kali)
* [OSX Maverick 10.9.2](#osx)
* [Docker](#docker)
* [Chef](#chef)

<a name="faraday-client"></a>
### Faraday Client

Faraday Client is the software which will allow you to work with your favorite security tools and capture their output in an organized manner. It works under a GTK+3 interface with the popular VTE terminal with a custom ZSH shell that respects the user's configuration (yes, that means you get to keep your exact ZSH terminal inside Faraday, even if you use ZPrezto or Oh My ZSH). 

From the client you can also create and delete workspaces, specify plugin configuration, view information about your hosts, resolve conflics that may arise and much more.

It's also a reponsability of the client to send all of the collected information to the server, which will then process it and format it in an friendly way for you to view, edit and confirm. 

<a name="requirements"></a>
### Requirements

Faraday Client works under any modern Linux distro or Mac OS X, and needs the following dependencies. We also provide an installation script, so in most cases you won't need to actually install these by hand. Scroll down to view more information on installation for each particular distribution or operative system.

* Python 2.6.x or 2.7.x
* CouchDB >= 1.2.0  
* GTK+3, PyGobject >= 3.12.0, Vte (API >= 2.90)
* Zsh
* Curl
* The following python libs:
  * mockito 
  * couchdbkit 
  * whoosh 
  * argparse 
  * psycopg2
  * IPy
  * requests

Out tests include [Debian](#debian), [Ubuntu](#debian), [Kali](#kali), [Backtrack](#debian) and [OSX Maverick 10.9.2](#osx).

If instead of installing you want to take a quick look at Faraday you can also use [Docker](#docker).

[ [index] ](#index)

<a name="debian"></a>
### Debian, Ubuntu, Backtrack

Download the [latest tarball](https://github.com/infobyte/faraday/tarball/master) or clone the [Faraday Git Project](https://github.com/infobyte/faraday repository):

```
$ git clone https://github.com/infobyte/faraday.git faraday-dev
$ cd faraday-dev
$ ./install.sh
$ ./faraday-server.py
$ ./faraday.py
```

[ [index] ](#index)

<a name="kali"></a>
### Kali

Faraday comes pre-installed in Kali Rolling. The package name is **python-faraday**.

In order to run Faraday in Kali:
```
$ systemctl start couchdb
$ cd /usr/share/python-faraday
$ python faraday-server.py
$ python faraday.py
```

Due to Kali's package updates the pre-installed package may not be the last version. If you want the latest updates use the [Debian install steps](#debian).

[ [index] ](#index)


<a name="arch"></a>
### ArchLinux

Before installing Faraday you will need to get some user-contributed packages. In order to do this quickly we need an [AUR](https://wiki.archlinux.org/index.php/Arch_User_Repository) wrapper, in this case we will use [Yaourt](http://archlinux.fr/yaourt-en). After installing Yaourt run:

```
$ yaourt -S python2-dateutil python2-pip mime-types python2-gobject gtk3 vte3
```

Now you can proceed to [install Faraday](#debian-ubuntu-backtrack).

[ [index] ](#index)

<a name="osx"></a>
### OSX

Tested on OSX Maverick 10.9.2.

##### Xcode 

Go to AppStore and install Xcode. If you run **brew install** first, it'll ask to install Xcode too.

![](https://raw.github.com/wiki/infobyte/faraday/images/xcode.png)

Keep in mind that Xcode is 2+ Gb so it can take a while to download. After this is done go to **Preferences** and install command line tools or open a terminal console and run:

```
xcode-select --install
```

A dialog box will appear asking to install additional tools as shown in the image below. Click install.

![](https://raw.github.com/wiki/infobyte/faraday/images/confirm.png)


**Important!** Before proceeding with the rest of this guide you need to **open Xcode at least once** in order to accept the License Agreement. Please make sure you do that or else some of the dependencies will fail to install.

##### Brew

To install [Brew](http://brew.sh) run:

```
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

##### Install Python & PIP

Run:

```
brew install python
```

Remember never to run brew as root.

More info about [Python in OSX](http://docs.python-guide.org/en/latest/starting/install/osx/).

##### Git

We need Git in order to get Faraday from Github. Run:

```
brew install git
```

##### Faraday

Run:

```
git clone https://github.com/infobyte/faraday.git faraday-dev
```


##### Dependencies and other Python libraries via PIP

Installing Python via brew will also install pip. Now we need to use pip to install the [requirements](#packages):

`pip install -r requirements.txt`

If you have issues building psycopg2 (needed for Metasploit Online Module)

```
brew install postgresql
pip install psycopg2
```

##### GTK
We need a few other packages from brew before you can use the client:

`brew install vte3 pygobject`

##### CouchDB 

There are two options for this package; [Prebuild Package](http://www.apache.org/dyn/closer.cgi?path=/couchdb/binary/mac/1.6.1/Apache-CouchDB-1.6.1.zip) or use brew:

`brew install couchdb`

On Maverick 10.9.2:

`sudo ARCHFLAGS=-Wno-error=unused-command-line-argument-hard-error-in-future pip install -r requirements.txt`

##### ZSH

Faraday needs [ZSH](http://www.zsh.org/) and curl to connect to the server. To install it run:

`brew install zsh curl`

##### Going for it!

Almost there! Start Faraday's server:

```
$ cd faraday-dev
$ ./faraday.py --gui=nogui
```

and in another terminal run:

```
$ cd faraday-dev
$ ./faraday-terminal.zsh
```

[ [index] ](#index)

<a name="docker"></a>
### Docker

Docker is great if you wish to give Faraday a try without actually having to install it. In this guide you will find all you need to run Faraday in a Docker container.

If you already tried Faraday and you are ready to use it for real we strongly recommend that you install it in your host OS.

##### Starting up Faraday

Run:

```
# docker run -t -i infobyte/faraday /root/run.sh
```

This command runs the container with Faraday and CouchDB using a test Workspace called "workspace". Inside, Faraday is started with **./faraday.py -gui=no-gui --update** which means without a graphic environment and checking for  [[updates]].

Now to obtain the container's IP address run:

```
docker inspect $(docker ps -lq) | grep \"IPAddress
```

For the purpose of this guide lets use **X.X.X.X**.

##### Web UI
Direct the browser to http://X.X.X.X/reports/_design/reports/index.html

##### ZSH
```
ssh root@X.X.X.X
cd faraday/
./faraday-terminal.zsh
```

##### GTK GUI

In order to use this interface run:

```
# docker run infobyte/faraday /root/run_service.sh
```

And now in a different console, get the IP address:
```
# docker inspect $(docker ps -lq) | grep \"IPAddress
```

Again, for the purpose of this guide lets use **X.X.X.X**.

```
# ssh -X root@X.X.X.X
# cd faraday/
# ./faraday.py
```

Keep in mind that all tools must be installed inside the Docker container in order to work.

##### Importing Reports

A different way to upload data into Faraday is importing a Report from other tools using a Plugin. Read more about [plugin types](https://github.com/infobyte/faraday/wiki/Plugin-List#types).

In order to do this copy the report to **$HOME/.faraday/report/[workspace_name]** replacing [workspace_name] with the name of your Workspace. Once it has been processed and incorporated to the database the report is copied to **$HOME/.faraday/report/[workspace_name]/process**.

We can do this by copying the reports to the containers via sFTP or we can use a file sharing function between the host server and containers.

For example:

```
# mkdir -p /tmp/workspace/process
# cd /root/.faraday/report/workspace/
# docker run -t -i -v /tmp/workspace/:/root/.faraday/report/workspace/ infobyte/faraday /root/run.sh
```

Now we can use the tools inside the host server and this is going to be interpreted as if it were inside the container for Faraday in the Workspace called "workspace".

To run nmap:

```
# nmap localhost -xO /tmp/workspace/output_nmap.xml
```

Import a Report:

```
# cp /root/reports/nessusscan.nessus /tmp/workspace/
```

[ [index] ](#index)

<a name="chef"></a>
### Chef

If you want to deploy Faraday using Chef, [Sliim](https://github.com/Sliim) made a cookbook for it! You can find it [here](https://github.com/sliim-cookbooks/faraday/).

[ [index] ](#index)