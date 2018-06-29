## Index

* [Server](#faraday-server-commu)
* [Client](#faraday-client-commu)

## Topics

<a name="faraday-server-commu"></a>
### Faraday Server

Faraday Server is the interface between PostgreSQL and Faraday Client and WebUI. The server's responsibility is to transmit information between the client or WebUI and PostgreSQL, and make sure that they are kept in sync. The Web UI client, which allows you to handle enormous workspaces from your favorite web browser.


**Important:** You should keep in mind that is recommended to install Faraday server on the same instance as PostgreSQL.


#### Downloading

Download the [latest tarball](https://github.com/infobyte/faraday/tarball/dev) or clone the [Faraday Git Project](https://github.com/infobyte/faraday) repository and checkout the dev branch:

```
$ git clone https://github.com/infobyte/faraday.git faraday-dev
$ cd faraday-dev
$ git checkout dev
```

After doing so, make sure to [install system dependencies](#server-system-dependencies), [install Python dependencies](#server-python-dependencies) and [configure the Server](#server-configuration).

#### Requirements

Faraday Server is built with minimum requirements. This is by design, so you can install it even on the most bare-bones machine you can possibly imagine.

The Python requirements for the server are stored in the [`requirements_server.txt` file](https://github.com/infobyte/faraday/blob/dev/requirements_server.txt).

<a name="server-system-dependencies"></a>
#### Installing system dependencies

##### Debian based distributions (Debian, Ubuntu, Backtrack, etc)

You can run the following command to install the required dependencies on any Debian based distribution.

```
$ sudo apt update
$ sudo apt install build-essential ipython python-setuptools \
                python-pip python-dev libssl-dev libffi-dev \
                pkg-config libssl-dev libffi-dev libxml2-dev \
                libxslt1-dev libfreetype6-dev libpng-dev postgresql
```

##### Kali Linux

If you are running Kali, please run the following commands:

```
$ sudo apt-get update
$ sudo apt-get install build-essential ipython python-setuptools \
                python-pip python-dev libssl-dev libffi-dev \
                pkg-config libssl-dev libffi-dev libxml2-dev \
                libxslt1-dev libfreetype6-dev libpng-dev
```

##### Gentoo
If you are running Gentoo, this are the dependencies with Emerge:

```
dev-python/flask-sqlalchemy dev-python/service_identity dev-python/twisted \
dev-python/pyopenssl dev-java/mockito dev-python/Whoosh \
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

#### Initializing PostgreSQL

In order to initialize Postgresql database and generate your main user and a password, run the following command:

```
python manage.py initdb
```
 ***Note:*** if at the moment you run this command, it throws an error, be sure you have sudo installed. Once you have installed it, run the command again.


#### Importing from CouchDB

If you want to import your data from CouchDB to PostgreSQL, run the following command:

```
python manage.py import_from_couchdb
```

***Note:*** beware of the number of users you have created in CouchDB, remember that you have already created one when you initialized PostgreSQL. The number of users that you have between CouchDB and PostgreSQL should not surpass the number of users you're allow to have according to your license.

#### Configuration

By default, Faraday server will listen on port **5985**. You can edit this on `~/.faraday/config/server.ini`.

#### Exposing the Server

If you wish to access the Server form a different box you need to expose the service. In order to do so, edit the server configuration file and set the `bind_address` param to `0.0.0.0`.

Edit the file located in `~/.faraday/config/server.ini` and under the section `[faraday-server]` set the param, it should look something like this:

```
[faraday-server]
...
bind_address=0.0.0.0
```

Then restart the server if you had it running and reload your browser in case you were already trying to access the Web UI form a different IP.

faraday-server.py also allow to use *--bind* and *--port* to override *server.ini* settings.

#### Running

Once everything is installed and the server is configured, you can proceed to run the Faraday server script:

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

Download the [latest tarball](https://github.com/infobyte/faraday/tarball/dev) or clone the [Faraday Git Project](https://github.com/infobyte/faraday) repository and checkout dev branch:

    $ git clone https://github.com/infobyte/faraday.git faraday-dev
    $ git checkout dev
    $ cd faraday-dev


#### Requirements

Faraday Client works under any modern Linux distribution or Mac OS X, and needs Python 2.6 or 2.7.

The Python requirements for the client are stored in the [`requirements.txt` file](https://github.com/infobyte/faraday/blob/dev/requirements.txt). Some additional requirements are necessary for specific features to work, these are stored in the [`requirements_extras.txt` file](https://github.com/infobyte/faraday/blob/dev/requirements_extras.txt).

Out tests include [Debian](#client-debian), [Ubuntu](#client-debian), [Kali](#client-kali), [Backtrack](#client-debian).


<a name="client-system-dependencies"></a>
#### Installing system dependencies

<a name="client-debian"></a>
##### Debian and derivatives

You can run the following command to install the required dependencies on any Debian based distribution.

```
$ sudo apt update
```

If you are running Ubuntu 12.04 LTS, or Ubuntu 14.04 LTS, please execute this command:

```
$ sudo apt install libpq-dev python-pip python-dev gir1.2-gtk-3.0 gir1.2-vte-2.90 python-gobject zsh curl
```

If you are any other version, please execute the following command:

```
$ sudo apt install libpq-dev python-pip python-dev gir1.2-gtk-3.0 gir1.2-vte-2.91 python-gobject zsh curl
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
By default, Faraday server will listen on port **5985**. You can edit this on `~/.faraday/config/server.ini`.

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
And search for the following **api_uri** tag and set it to the server URL, for example:

`<api_uri>http://127.0.0.1:5985</api_uri>`

#### Running

Once you have already configured the client and have Faraday Server running, you simply have to run:

```
$ python2 faraday.py
```

Some distributions or installations require additional steps, so look down below if you are using something different than Debian or Ubuntu, or if you need to apply some configuration to the client.

<a name="client-kali"></a>
##### Kali

Faraday comes pre-installed in Kali Rolling. The package name is **python-faraday**. Keep in mind that this package can only be used for the **Community edition**.

In order to run Faraday in Kali:
```
$ systemctl start postgres
$ cd /usr/share/python-faraday
$ python2 faraday-server.py
$ python2 faraday.py
```

Due to Kali's package updates the pre-installed package may not be the last version. If you want the latest updates use the [Debian install steps](#client-debian).

