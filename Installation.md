**Requirements:**

Modern Linux (Tested Debian / Ubuntu  * / Kali / Backtrack)
* Python 2.6.x and 2.7.x
* Qt3
* CouchDB >= 1.2.0  
* The following python libs:
  * mockito 
  * couchdbkit 
  * whoosh 
  * argparse 
  * psycopg2
  * IPy
  * requests

Download the latest tarball by clicking [here] (https://github.com/infobyte/faraday/tarball/master) 

Preferably, you can download faraday by cloning the [Git] (https://github.com/infobyte/faraday repository):
```
$ git clone https://github.com/infobyte/faraday.git faraday-dev
$ cd faraday-dev
$ ./install
```

### OSX

OSX support, tried on latest OSX Maverick 10.9.2

* Xcode 
You just need to go to AppStore and install Xcode. If you run brew install first, it'll ask to install Xcode there too.

![](https://raw.github.com/wiki/infobyte/faraday/images/xcode.png)


After you install Xcode (it will take a while since is 2+ Gb) you need to go to preferences and install command line tools or just run this on the terminal console:

`xcode-select --install`

You will see:

![](https://raw.github.com/wiki/infobyte/faraday/images/confirm.png)


**IMPORTANT NOTE:** Before continue with the rest of this guide, you NEED to open Xcode at least one time. This is for accept the License Agreement. Some of the dependencies will fail to install without accepting it.

* Brew (http://brew.sh)
To install brew just run this line:

`ruby -e "$(curl -fsSL https://raw.github.com/Homebrew/homebrew/go/install)"`

* Python & pip
To install latest python version we are going to use brew

`brew install python`

Note: Remember, brew doesn't like to run as root, so don't sudo it.

* Git via Brew

We need to install git in order to get faraday repository from github:

`brew install git`

* Getting faraday from github repository

`git clone https://github.com/infobyte/faraday.git faraday-dev`

* Python libraries via PIP

Installing python via brew will also install pip. We are going to use it to install Faraday's requirements.

`pip install -r requirements.txt`

On Maveriks 10.9.2

`sudo ARCHFLAGS=-Wno-error=unused-command-line-argument-hard-error-in-future pip install -r requirements.txt`

* ZSH

Faraday need ZSH to connect to the server. To install ZSH just run:

`brew install zsh`

* Going for it!

You are almost there! You just need to start the faraday's server like this:

```
$ cd faraday-dev
$ ./faraday --gui=nogui
```

and in other terminal run:

```
$ cd faraday-dev
$ ./faraday-terminal.zsh
```
You should see ">>> WELCOME TO FARADAY".