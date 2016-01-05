### Requirements

Modern Linux or OSX. Current tests include Debian, Ubuntu, Kali, Backtrack and OSX Maverick 10.9.2.

And the following packages:

<a name="packages"></a>* Python 2.6.x or 2.7.x
* Qt3 (only Linux)
* CouchDB >= 1.2.0  
* The following python libs:
  * mockito 
  * couchdbkit 
  * whoosh 
  * argparse 
  * psycopg2
  * IPy
  * requests

<a name="install"></a>Download the [latest tarball](https://github.com/infobyte/faraday/tarball/master) or clone the [Faraday Git Project](https://github.com/infobyte/faraday repository):

```
$ git clone https://github.com/infobyte/faraday.git faraday-dev
$ cd faraday-dev
$ ./install.sh
```
### ArchLinux

Before [installing Faraday](#install) you will need to get some user-contributed packages. In order to do this quickly we need an [AUR](https://wiki.archlinux.org/index.php/Arch_User_Repository) wrapper, in this case we will use [Yaourt](http://archlinux.fr/yaourt-en). After installing Yaourt run:

```
$ yaourt -S python2-whoosh pyqt3 python2-mockito python2-couchdbkit python2-flask python2-restkit python2-ipy python2-requests python2-tornado python2-dateutil python2-colorama python2-pip
```

Now you can proceed to [install Faraday](#install).

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

##### Brew (http://brew.sh)

Run:

```
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

##### Python & pip

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

##### Python libraries via PIP

Installing Python via brew will also install pip. Now we need to use pip to install the [requirements](#packages):

`pip install -r requirements.txt`

If you have issues building psycopg2 (needed for Metasploit Online Module)

```
brew install postgresql
pip install psycopg2
```

##### CouchDB 

There are two options for this package; [Prebuild Package](http://www.apache.org/dyn/closer.cgi?path=/couchdb/binary/mac/1.6.1/Apache-CouchDB-1.6.1.zip) or use brew:

`brew install couchdb`

On Maverick 10.9.2:

`sudo ARCHFLAGS=-Wno-error=unused-command-line-argument-hard-error-in-future pip install -r requirements.txt`

##### ZSH

Faraday needs [ZSH](http://www.zsh.org/) to connect to the server. To install it run:

`brew install zsh`

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
