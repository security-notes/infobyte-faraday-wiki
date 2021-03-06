### To use faraday follow the [new Faraday Install Guide](https://github.com/infobyte/faraday/wiki/Install-Guide). This is for development

## Index

* [Server](#faraday-server-commu)
* [Client](#faraday-client-commu)

## Topics

<a name="faraday-server-commu"></a>
### Faraday Server

Faraday Server is the interface between PostgreSQL and Faraday Client and WebUI. The server's responsibility is to transmit information between the client or WebUI and PostgreSQL, and make sure that they are kept in sync. The Web UI client, which allows you to handle enormous workspaces from your favorite web browser.


**Important:** You should keep in mind that is recommended to install Faraday server on the same instance as PostgreSQL.


#### Downloading

Download the [latest tarball](https://github.com/infobyte/faraday/tarball/master) or clone the [Faraday Git Project](https://github.com/infobyte/faraday) repository and checkout the dev branch:

```
$ git clone --depth 1 https://github.com/infobyte/faraday.git faraday-dev
$ cd faraday-dev
```

After doing so, make sure to [install system dependencies](#server-system-dependencies), [install Python dependencies](#server-python-dependencies) and [configure the Server](#server-configuration).

#### Requirements

Faraday Server is built with minimum requirements. This is by design, so you can install it even on the most bare-bones machine you can possibly imagine.

The Python requirements for the server are stored in the [`requirements_server.txt` file](https://github.com/infobyte/faraday/blob/dev/requirements_server.txt).

<a name="server-system-dependencies"></a>
#### Installing system dependencies

##### Debian based distributions (Debian, Ubuntu, Backtrack, etc)

Or if you wanna do it manually you can run the following command to install the required dependencies on any Debian based distribution.

```
$ sudo apt update

$ sudo apt install build-essential ipython python-setuptools \
                python-pip python-dev libssl-dev \
                libffi-dev pkg-config libxml2-dev \
                libxslt1-dev libfreetype6-dev libpng-dev postgresql

```
**Warning**: If you already have **postgresql** installed, please corroborate the version is upper than 9.4.

##### Kali Linux

If you are running Kali, please run the following commands:

```
$ sudo apt-get update
$ sudo apt-get install build-essential ipython python-setuptools \
                python-pip python-dev libssl-dev \
                libffi-dev pkg-config libxml2-dev \
                libxslt1-dev libfreetype6-dev libpng-dev
```


##### Others

Please consult with your distribution documentation to install the dependencies listed above.

#### Creating a virtualenv

Before installing Faraday, we need to create a virtualenv so Faraday runs in it. In order to install and create a virtualenv, run the following commands:

```
$ pip install virtualenv
$ virtualenv -p python3 faraday_venv
$ source faraday_env/bin/activate 
```

For more information about virtualenv, please follow this [link](https://virtualenv.pypa.io/en/latest/userguide/).

<a name="server-python-dependencies"></a>
#### Installing Python 2 dependencies

Once you have the required system dependencies, you just have to install the Python modules needed to run the server using:

```
$ python setup.py develop
```

<a name="server-configuration"></a>

#### Initializing PostgreSQL

In order to initialize PostgreSQL database, run the following command:

```
faraday-manage initdb
```

**IMPORTANT**: The command `initdb` will create a random password for the admin user, remeber to COPY THE PASSWORD. You can use the command `faraday-manage change-password` if you want to change it.

***Note:*** If you can't login into to Faraday after running the command above due to invalid credentials, you can change your password through the PostgreSQL shell that Faraday has in it. Follow the next [instructions](https://github.com/infobyte/faraday/wiki/Troubleshooting#cant-login-after-importing-from-couch) in order to change your password and be able to login.

 ***Note:*** You sould have the PostgreSQL service started. To do it run
`systemctl start postgresql` or the equivalant command for your GNU/Linux
distro.

 ***Note:*** if at the moment you run this command, it throws an error, be sure
you have sudo installed. Once you have installed it, run the command again.


#### Manual PostgreSQL configuration

If you need an advance configuration of the postgres database, like having a
custom database name or run it in a separate host, the `./manage.py initdb`
command probably won't be enough for you, so you should configure it manually
by doing something like this:

```
sudo -u postgres psql -c "CREATE ROLE faraday_postgresql WITH LOGIN PASSWORD 'YOURPASSWORD'"
sudo -u postgres createdb -O faraday_postgresql faraday
```

Then, edit the `~/.faraday/config/server.ini` by adding the connection string
to the database:

```
[database]
connection_string = postgresql+psycopg2://faraday_postgresql:YOURPASSWORD@localhost/faraday
```

Then you should run `./manage.py create-tables` to create all the required
tables to make faraday work, and `./manage.py createsuperuser` to create an
admin user.


#### Manually importing from CouchDB

If you were using Faraday 2.7.2 and setup the database manually instead of
using the `./manage.py initdb`, you should run the following command to import
the data from CouchDB:

```
$ python manage.py import-from-couchdb
```

#### Updating Nginx configuration

***Note:*** This only applies if you are using Nginx and https.

Please, make sure you have this settings on your Nginx config:

    proxy_pass http://localhost:5985/;
    proxy_redirect http:// $scheme://;

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

faraday-server also allow to use *--bind* and *--port* to override *server.ini* settings.

#### Running

Once everything is installed and the server is configured, you can proceed to run the Faraday server script:

```
$ faraday-server
```

If you want to run the server in background mode, you should use the `--start` option:

```
$ faraday-server --start
```

This is the recommended way to do this. Other methods like using the bash `&` could cause unexpected IOErrors and other related exceptions.

#### Web UI

Once the server is running, you can access Faraday's Web UI using any browser:
just point it to `http://SERVER_IP:SERVER_PORT/` (by default it will be
http://localhost:5985/) and you can start playing with Faraday.


<a name="faraday-client-commu"></a>
### Faraday Client

Faraday Client is the software which will allow you to work with your favorite security tools and capture their output in an organized manner. It works under a GTK+3 interface with the popular VTE terminal with a custom ZSH shell that respects the user's configuration (yes, that means you get to keep your exact ZSH terminal inside Faraday, even if you use ZPrezto or Oh My ZSH).

From the client you can also create and delete workspaces, specify plugin configuration, view information about your hosts, resolve conflics that may arise and much more.

It's also a responsibility of the client to send all of the collected information to the server, which will then process it and format it in an friendly way for you to view, edit, and confirm.

The client is bundled in the same package as the server, so if you have already downloaded Faraday, you can skip the next step.

#### Downloading

Download the [latest tarball](https://github.com/infobyte/faraday/tarball/dev) or clone the [Faraday Git Project](https://github.com/infobyte/faraday) repository and checkout dev branch:

    $ git clone --depth 1 https://github.com/infobyte/faraday.git faraday-dev
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

#### Using GTK client with virtualenv

If you are working inside a Virtual enviroment you need to follow this extra steps for GTK to work:
```
pip install vext
pip install vext.pygtk
pip install vext.gi
```

<a name="client-configuration"></a>
#### Configuration

Now you need to configure every Faraday instance so it can connect to the server.

* If you're using the GTK interface click on the Preferences icon ![](https://raw.github.com/wiki/infobyte/faraday/images/installation/gtk_preferences_icon.png) and fill in the server URL, for example **http://127.0.0.1:5985**

![](https://raw.github.com/wiki/infobyte/faraday/images/installation/gtk_preferences_dialog.png)

* If you are using the ***--gui=no-gui*** option

Edit the file: `~/.faraday/config/user.xml`
And search for the following **api_uri** tag and set it to the server URL, for example:

`<api_uri>http://127.0.0.1:5985</api_uri>`

**If you are using SSL** you need to use https in your configuration. For example use https://192.168.0.20 when you are using an nginx server with SSL enabled and faraday-server is listening on 192.168.0.20. 

#### Running

Once you have already configured the client and have Faraday Server running, you simply have to run:

```
$ faraday-client
```

Some distributions or installations require additional steps, so look down below if you are using something different than Debian or Ubuntu, or if you need to apply some configuration to the client.

<a name="client-kali"></a>
##### Kali

Faraday comes pre-installed in Kali Rolling. The package name is **python-faraday**. Keep in mind that this package can only be used for the **Community edition**.

In order to run Faraday in Kali:
```
$ systemctl start postgresql.service
$ cd /usr/share/python-faraday
$ faraday-server
$ faraday-client
```

Due to Kali's package updates the pre-installed package may not be the last version. If you want the latest updates use the [Debian install steps](#client-debian).

##### Gentoo
If you are running Gentoo, this are the dependencies with Emerge:

```
dev-python/flask-sqlalchemy dev-python/service_identity dev-python/twisted \
dev-python/pyopenssl dev-java/mockito dev-python/Whoosh \
dev-python/configargparse dev-python/restkit dev-python/requests www-servers/tornado \
dev-python/flask dev-python/colorama dev-python/setuptools dev-python/pip dev-libs/libpqxx \
libffi-dev
```
