## Index

* [Server](#faraday-server-commu)
* [Client](#faraday-client-commu)

## Topics

<a name="faraday-server-commu"></a>
### Faraday Server

Faraday Server is the way to have a better synchronization between your Faraday Client session and CouchDB. The server's responsibility is to send and receive information from both the client and CouchDB, and make sure that they are both in sync. At the same time, it provides much better performance to the Web UI, allowing it to handle enormous workspaces without a problem.

**Important:** You should keep in mind that the Faraday server must be installed on the same machine as CouchDB. Also make sure to use version 1.6, as Faraday doesn't support CouchDB version 2.0.

Due to the new version of Erlang, in debian based systems like Kali linux(and potentially others) Couchdb 1.6 is not working.
We recommend use Couchdb in docker, we are working in migrate to another database engine for fix that problem.

#### Downloading

Download the [latest tarball](https://github.com/infobyte/faraday/tarball/master) or clone the [Faraday Git Project](https://github.com/infobyte/faraday) repository:

```
$ git clone https://github.com/infobyte/faraday.git faraday-dev
$ cd faraday-dev
```

After doing so, make sure to [install system dependencies](#server-system-dependencies), [install Python dependencies](#server-python-dependencies) and [configure the Server](#server-configuration).

#### Requirements

Faraday Server is built with minimum requirements. This is by design, so you can install it even on the most bare-bones machine you can think of.

The Python requirements for the server are stored in the [`requirements_server.txt` file](https://github.com/infobyte/faraday/blob/master/requirements_server.txt).

| Dependency | Version |
|---|---|
| CouchDB | 1.6 |
| Python | 2.6 or 2.7 |
| flask | >= 0.10.1 |
| twisted | >= 16.1.1 |
| sqlalchemy | >=1.0.12 |
| pyopenssl | >16.0.0 |
| couchdbkit | >=0.6.5 |
| restkit | >=4.2.2 |
| requests | >=2.10.0 |
| flask | >=0.10.1 |
| twisted | >=16.1.1 |
| sqlalchemy | >=1.0.12 |
| pyopenssl | >=16.0.0 |
| service_identity | >=16.0.0 |

<a name="server-system-dependencies"></a>
#### Installing system dependencies

##### Debian based distributions (Debian, Ubuntu, Backtrack, etc)

You can run the following command to install the required dependencies on any Debian based distribution.

```
$ sudo apt-get update
$ sudo apt-get install build-essential ipython python-setuptools \
                python-pip python-dev libssl-dev libffi-dev couchdb \
                pkg-config libssl-dev libffi-dev libxml2-dev \
                libxslt1-dev libfreetype6-dev libpng12-dev
```

##### Kali Linux

If you are running Kali, please run the following commands:

```
$ sudo apt-get update
$ sudo apt-get install build-essential ipython python-setuptools \
                python-pip python-dev libssl-dev libffi-dev couchdb \
                pkg-config libssl-dev libffi-dev libxml2-dev \
                libxslt1-dev libfreetype6-dev libpng-dev
```

##### Gentoo 
If you are running Gentoo, this are the dependencies with Emerge:

```
dev-db/couchdb dev-python/flask-sqlalchemy dev-python/service_identity dev-python/twisted \
dev-python/pyopenssl dev-python/couchdbkit dev-java/mockito dev-python/Whoosh \ 
dev-python/configargparse dev-python/restkit dev-python/requests www-servers/tornado \
dev-python/flask dev-python/colorama dev-python/setuptools dev-python/pip dev-libs/libpqxx \
libffi-dev 
```

##### Others

Please consult with your distribution documentation to install the dependencies listed above.

<a name="server-python-dependencies"></a>
#### Installing Python 2 dependencies

Once you have the required system dependencies, you just have to install the Python modules needed to run the server using `pip`:

```
$ pip2 install -r requirements_server.txt
```

<a name="server-configuration"></a>
#### Configuration

Faraday Server needs to communicate to Couch Databases to function. By default, the server will listen on port **5985**. You may need to edit `user` and `password` on `~/.faraday/config/server.ini` in case you have set up an admin account on your CouchDB.

### Authentication

You can use the CouchDB ***_utils*** interface (located in `http://127.0.0.1:5984/_utils/`) to create administrator users, and then edit the CouchDB url in your instance with the users credentials. For example: `http://faraday:changeme@192.168.1.254:5985/`

#### Exposing the Server

If you wish to access the Server form a different box you need to expose the service. In order to do so, edit the server configuration file and set the `bind_address` param to `0.0.0.0`.

Edit the file located in `~/.faraday/config/server.ini` and under the section `[faraday-server]` set the param, it should look something like this:

```
[faraday-server]
...
bind_address=0.0.0.0
```

Then restart the server if you had it running and reload your browser in case you were already trying to access the Web UI form a different IP.


#### Running

Once everything is installed you need to configure your server properly. Read about [Server Configuration](#server-configuration).

After configuring, you can proceed to run the Faraday Server script:

```
$ python2 faraday-server.py
```

If you want to run the server in background mode, you should use the `--start` option:

```
$ python2 faraday-server.py --start
```

This is the recommended way to do this. Other methods like using the bash `&` could cause unexpected IOErrors and other related exceptions.

#### Web UI

Once the server is running, you can access Faraday's Web UI using any browser: just point it to `http://SERVER_IP:SERVER_PORT/_ui` and you can start playing with Faraday.


<a name="faraday-client-commu"></a>
### Faraday Client

Faraday Client is the software which will allow you to work with your favorite security tools and capture their output in an organized manner. It works under a GTK+3 interface with the popular VTE terminal with a custom ZSH shell that respects the user's configuration (yes, that means you get to keep your exact ZSH terminal inside Faraday, even if you use ZPrezto or Oh My ZSH).

From the client you can also create and delete workspaces, specify plugin configuration, view information about your hosts, resolve conflics that may arise and much more.

It's also a responsibility of the client to send all of the collected information to the server, which will then process it and format it in an friendly way for you to view, edit, and confirm.

The client is bundled in the same package as the server, so if you have already downloaded Faraday, you can skip the next step.

#### Downloading

Download the [latest tarball](https://github.com/infobyte/faraday/tarball/master) or clone the [Faraday Git Project](https://github.com/infobyte/faraday) repository:

    $ git clone https://github.com/infobyte/faraday.git faraday-dev
    $ cd faraday-dev


#### Requirements

Faraday Client works under any modern Linux distribution or Mac OS X, and needs the following dependencies:

| Dependency | Version |
|---|---|
| CouchDB | 1.6 |
| Python | 2.6 or 2.7 |
| GTK3 |  |
| PyGobject | 3.12.0 |
| Vte | API >= 2.90 |
| zsh |  |
| CURL |  |
| couchdbkit |  |
| mockito |  |
| whoosh |  |
| argparse |  |
| IPy |  |
| restkit |  |
| requests |  |
| tornado |  |
| flask |  |
| colorama |  |

The Python requirements for the client are stored in the [`requirements.txt` file](https://github.com/infobyte/faraday/blob/master/requirements.txt). Some additional requirements are necessary for specific features to work, these are stored in the [`requirements_extras.txt` file](https://github.com/infobyte/faraday/blob/master/requirements_extras.txt).

Out tests include [Debian](#client-debian), [Ubuntu](#client-debian), [Kali](#client-kali), [Backtrack](#client-debian) and [OSX Sierra](https://github.com/infobyte/faraday/wiki/Installation-OSX).

If instead of installing you want to take a quick look at Faraday you can also use [Docker](#client-docker).

<a name="client-system-dependencies"></a>
#### Installing system dependencies

<a name="client-debian"></a>
##### Debian and derivatives

You can run the following command to install the required dependencies on any Debian based distribution.

```
$ sudo apt-get update
```

If you are running Ubuntu 12.04 LTS, or Ubuntu 14.04 LTS, please execute this command:

```
$ sudo apt-get install libpq-dev python-pip python-dev gir1.2-gtk-3.0 gir1.2-vte-2.90 python-gobject zsh curl
```

If you are any other version, please execute the following command:

```
$ sudo apt-get install libpq-dev python-pip python-dev gir1.2-gtk-3.0 gir1.2-vte-2.91 python-gobject zsh curl
```

#### Gentoo 

This are the dependencies for Gentoo with Emerge:

```
dev-libs/gobject-introspection net-libs/webkit-gtk x11-libs/gtk+ \
x11-libs/vte dev-python/pygobject app-shells/zsh net-misc/curl dev-python/ipython
```

Extras dependencies:

```
dev-python/beautifulsoup dev-python/gevent-psycopg2
```

#### ArchLinux

Before installing Faraday you will need to get some user-contributed packages. In order to do this quickly we need an [AUR](https://wiki.archlinux.org/index.php/Arch_User_Repository) wrapper, in this case we will use [Yaourt](http://archlinux.fr/yaourt-en). After installing Yaourt run:

```
$ yaourt -S python2-dateutil python2-pip mime-types python2-gobject gtk3 vte3 postgresql-libs
```

<a name="client-python-dependencies"></a>
#### Installing Python 2 dependencies

Once you have the required system dependencies, you just have to install the Python modules needed to run the client using `pip`:

```
$ pip2 install -r requirements.txt
```

If you are working inside a Virtual Machine you need to follow this extra steps for GTK to work:
```
pip2 install vext
pip2 install vext.pygtk

```

<a name="client-configuration"></a>
#### Configuration

Now you need to configure every Faraday instance so it can connect to the server.

* If you're using the GTK interface click on the Preferences icon ![](https://raw.github.com/wiki/infobyte/faraday/images/gtk-preferences-icon.png) and fill in the server URL, for example **http://127.0.0.1:5985**

![](https://raw.github.com/wiki/infobyte/faraday/images/gtk-preferences-dialog.png)

* If you are using the ***--gui=no-gui*** option

Edit the file: `~/.faraday/config/user.xml`
And search for the following **couch_uri** tag and set it to the server URL, for example:

`<couch_uri>http://127.0.0.1:5985</couch_uri>`

#### Running

Once you have already configured the client and have Faraday Server running, you simply have to run:

```
$ python2 faraday.py
```

Some distributions or installations require additional steps, so look down below if you are using something different than Debian or Ubuntu, or if you need to apply some configuration to the client.

<a name="client-kali"></a>
##### Kali

Faraday comes pre-installed in Kali Rolling. The package name is **python-faraday**. Keep in mind that this package can only be used for the **Community edition**, if you've purchased a **Commercial license** please refer to our documentation for [Pro](http://github.com/infobyte/faraday/wiki/installation-pro) or [Corp](http://github.com/infobyte/faraday/wiki/installation-corp) installation.

In order to run Faraday in Kali:
```
$ systemctl start couchdb
$ cd /usr/share/python-faraday
$ python2 faraday-server.py
$ python2 faraday.py
```

Due to Kali's package updates the pre-installed package may not be the last version. If you want the latest updates use the [Debian install steps](#client-debian).

<a name="client-docker"></a>
##### Docker

[You can find instructions on how to run the client inside a Docker container here.](https://github.com/infobyte/faraday/wiki/installation-docker)

<a name="client-osx"></a>
##### OSX

[You can find instructions on how to run the client under Mac OSX here.](https://github.com/infobyte/faraday/wiki/Installation-OSX)

##### Chef

If you want to deploy Faraday using Chef, [Sliim](https://github.com/Sliim) made a cookbook for it! You can find it [here](https://github.com/sliim-cookbooks/faraday/).
