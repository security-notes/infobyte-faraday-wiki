## OSX

Video about install Faraday in macOS Sierra: [Installation in macOS Sierra.](https://www.youtube.com/watch?v=F44RnB3Ru24)

Tested on OSX Maverick 10.9.2.

### Xcode

Go to AppStore and install Xcode. If you run `brew install` first, it'll ask to install Xcode too.

![](https://raw.github.com/wiki/infobyte/faraday/images/xcode.png)

Keep in mind that Xcode is 2+ Gb so it can take a while to download. After this is done go to **Preferences** and install command line tools or open a terminal console and run:

    $ xcode-select --install

A dialog box will appear asking to install additional tools as shown in the image below. Click install.

![](https://raw.github.com/wiki/infobyte/faraday/images/confirm.png)

**Important!** Before proceeding with the rest of this guide you need to **open Xcode at least once** in order to accept the License Agreement. Please make sure you do that or else some of the dependencies will fail to install.

### Brew

To install [Brew](http://brew.sh) run:


    $ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

### Install Python & PIP

Run:

    $ brew install python

Remember never to run brew as root.

More info about [Python in OSX](http://docs.python-guide.org/en/latest/starting/install/osx/).

*Important* Make sure that you are using the python interpreter that brew installed and not the one shipped with the OS.
To know which python you are using execute:

    $ which python

it should return:

    $ /usr/local/bin/python

If this is not the case you can change the PATH to use the /usr/local/bin:

    $ ln -s /usr/local/bin/python2 /usr/local/bin/python

If you want to revert this change just delete the link executed in the previous command.


### Git

We need Git in order to get Faraday from Github. Run:

    $ brew install git

### Faraday

Run:

    $ git clone https://github.com/infobyte/faraday.git faraday-dev

### Dependencies and other Python libraries via PIP

Installing Python via brew will also install pip. Now we need to use pip to install the requirements:

`pip install -r requirements.txt`

If you have issues building psycopg2 (needed for Metasploit Online Module)

    $ brew install postgresql
    $ pip install psycopg2


### GTK

We need a few other packages from brew before you can use the client:

    $ brew install vte3 pygobject3

### CouchDB

There are two options for this package; [Prebuild Package](http://www.apache.org/dyn/closer.cgi?path=/couchdb/binary/mac/1.6.1/Apache-CouchDB-1.6.1.zip) or use brew:

    $ brew install couchdb

On Maverick 10.9.2:

    $ sudo ARCHFLAGS=-Wno-error=unused-command-line-argument-hard-error-in-future pip install -r requirements.txt

To make sure that it is running, start/restart the service with this command:

    $ brew services restart couchdb

### ZSH

Faraday needs [ZSH](http://www.zsh.org/) and curl to connect to the server. To install it run:

    $ brew install zsh curl

### Going for it!

Almost there! Start Faraday's server:

    $ cd faraday-dev
    $ ./faraday.py --gui=nogui

And in another terminal run:

    $ cd faraday-dev
    $ ./faraday-terminal.zsh
