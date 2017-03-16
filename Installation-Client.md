Faraday Client is the software which will allow you to work with your favorite security tools and capture their output in an organized manner. It works under a GTK+3 interface with the popular VTE terminal with a custom ZSH shell that respects the user's configuration (yes, that means you get to keep your exact ZSH terminal inside Faraday, even if you use ZPrezto or Oh My ZSH).

From the client you can also create and delete workspaces, specify plugin configuration, view information about your hosts, resolve conflics that may arise and much more.

It's also a responsibility of the client to send all of the collected information to the server, which will then process it and format it in an friendly way for you to view, edit, and confirm.

The client is bundled in the same package as the server, so if you have already downloaded Faraday, you can skip the next step.

## Downloading Faraday

Download the [latest tarball](https://github.com/infobyte/faraday/tarball/master) or clone the [Faraday Git Project](https://github.com/infobyte/faraday repository):

    $ git clone https://github.com/infobyte/faraday.git faraday-dev
    $ cd faraday-dev


## Requirements

Faraday Client works under any modern Linux distribution or Mac OS X, and needs the following dependencies.

| Dependency | Version |
|---|
| CouchDB | 1.6 |
| Python | 2.6 or 2.7 |
| GTK3 |  |
| PyGobject | 3.12.0 |
| Vte | API >= 2.90 |
| zsh |  |
| CURL |  |

The requirements for the client are stored in the [`requirements.txt` file](https://github.com/infobyte/faraday/blob/master/requirements.txt). Some additional requirements are necessary for specific features to work, these are stored in the [`requirements_extras.txt` file](https://github.com/infobyte/faraday/blob/master/requirements_extras.txt).

Out tests include [Debian](#debian), [Ubuntu](#debian), [Kali](#kali), [Backtrack](#debian) and [OSX Maverick 10.9.2](#osx).

If instead of installing you want to take a quick look at Faraday you can also use [Docker](#docker).

### Debian and derivatives

You can run the following command to install the required dependencies on any Debian based distribution.

    $ sudo apt-get update

If you are running Ubuntu 12.04 LTS, or Ubuntu 14.04 LTS, please execute this command:

    $ sudo apt-get install libpq-dev python-pip python-dev gir1.2-gtk-3.0 gir1.2-vte-2.90 python-gobject zsh curl

If you are any other version, please execute the following command:

    $ sudo apt-get install libpq-dev python-pip python-dev gir1.2-gtk-3.0 gir1.2-vte-2.91 python-gobject zsh curl

### ArchLinux

Before installing Faraday you will need to get some user-contributed packages. In order to do this quickly we need an [AUR](https://wiki.archlinux.org/index.php/Arch_User_Repository) wrapper, in this case we will use [Yaourt](http://archlinux.fr/yaourt-en). After installing Yaourt run:

    $ yaourt -S python2-dateutil python2-pip mime-types python2-gobject gtk3 vte3 postgresql-libs

## Installing Python 2 dependencies

Once you have the required system dependencies, you just have to install the Python modules needed to run the client using `pip`:

    $ pip2 install -r requirements.txt

## Running the client

Once you have already configured the client and have Faraday Server running, you simply have to run:

    $ ./faraday.py

Some distributions or installations require additional steps, so look down below if you are using something different than Debian or Ubuntu, or if you need to apply some configuration to the client.


#### Kali

Faraday comes pre-installed in Kali Rolling. The package name is **python-faraday**.

In order to run Faraday in Kali:
```
$ systemctl start couchdb
$ cd /usr/share/python-faraday
$ python faraday-server.py
$ python faraday.py
```

Due to Kali's package updates the pre-installed package may not be the last version. If you want the latest updates use the [Debian install steps](#debian).


#### Docker

[You can find instructions on how to run the client inside a Docker container here.](https://github.com/infobyte/faraday/wiki/installation-client)

#### MacOS

[You can find instructions on how to run the client under Mac OSX here.](https://github.com/infobyte/faraday/wiki/installation-client)

#### Chef

If you want to deploy Faraday using Chef, [Sliim](https://github.com/Sliim) made a cookbook for it! You can find it [here](https://github.com/sliim-cookbooks/faraday/).
