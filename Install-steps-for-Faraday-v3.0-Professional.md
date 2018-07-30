## Index

* [Server](#faraday-server-pro)
* [Client](#faraday-client-pro)

## Topics

<a name="faraday-server-pro"></a>
### Faraday Server

Faraday Server is the interface between PostgreSQL and Faraday Client and WebUI. The server's responsibility is to transmit information between the client or WebUI and PostgreSQL, and make sure that they are kept in sync. The Web UI client, which allows you to handle enormous workspaces from your favorite web browser.

**Important:** You should keep in mind that is recommended to install Faraday server on the same instance as PostgreSQL.

#### Downloading

After the purchase you will receive an email with your credentials and a link to our **Customers Portal**. Use those credentials to log in to the site and you will get two links:

* Download License - this is the tarball for the **Faraday License**
* Download Faraday - this is the tarball for the actual **Faraday Code**

Download both those packages and then:

1. Create a new directory and unpack the **Faraday tarball** there. For example, `/home/user/Infobyte/faraday`.

1. Unpack the **License Package** and place its contents in the `doc` directory. For example, using the path from **Step 1**, you should place the **License files** in `/home/user/Infobyte/faraday/doc`.

After doing so, make sure to [install system dependencies](#server-system-dependencies), [install Python dependencies](#server-python-dependencies) and [configure the Server](#server-configuration).

#### Requirements

Faraday Server is built with minimum requirements. This is by design, so you can install it even on the most bare-bones machine you can think of. The main requirement we need is Python 2.6 or 2.7.

The Python requirements for the server are stored in the [`requirements_server.txt` file](https://github.com/infobyte/faraday/blob/master/requirements_server.txt).


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
$ sudo apt update
$ sudo apt install build-essential ipython python-setuptools \
                python-pip python-dev libssl-dev libffi-dev \
                pkg-config libssl-dev libffi-dev libxml2-dev \
                libxslt1-dev libfreetype6-dev libpng-dev
```

##### Others

Please consult with your distribution documentation to install the dependencies listed above.

<a name="server-python-dependencies"></a>
#### Installing Python 2 dependencies

Once you have the required system dependencies, you just have to install the Python modules needed to run the server using `pip`:

```
$ pip2 install -r requirements_server.txt -U
```
#### Initializing PostgreSQL

In order to initialize Postgresql database, run the following command:

```
python manage.pyc initdb
```
If you don't have CouchDB configured we assume this is a new installation, so a
new user will be created.

With CouchDB configured in the `server.ini` file, it will import all the data
you had from the 2.7.2 version, including the users and its hashed passwords.

***Note:*** If you can't login into to Faraday after running the command above due to invalid credentials, you can change your password through the PostgreSQL shell that Faraday has in it. Follow the next instructions in order to change your password and be able to login:

Run the following command in order to execute PostgreSQL shell:

    $ python manage.pyc sql_shell

Once you got into the sql_shell, let's take a look inside the table _faraday_user_ to see the users information. **It is important to be sure of the username we want to change the password.**

    SELECT * FROM faraday_user

Assuming your username is '_faraday_' and the new password you want to set is '_changeme_', run the following command:

    UPDATE faraday_user SET PASSWORD='changeme' WHERE username='faraday'

This command will update your user's password.

Now you can login to Faraday without a problem.

 ***Note:*** You sould have the PostgreSQL service started. To do it run
`systemctl start postgresql` or the equivalant command for your GNU/Linux
distro.

 ***Note:*** if at the moment you run this command, it throws an error, be sure
you have sudo installed. Once you have installed it, run the command again.

#### Manual PostgreSQL configuration

If you need an advance configuration of the postgres database, like having a
custom database name or run it in a separate host, the `./manage.pyc initdb`
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

Then you should run `./manage.pyc create_tables` to create all the required
tables to make faraday work, and `./manage.pyc createsuperuser` to create an
admin user.


#### Manually importing from CouchDB

If you were using Faraday 2.7.2 and setup the database manually instead of
using the `./manage.pyc initdb`, you should run the following command to import
the data from CouchDB:

```
python manage.pyc import_from_couchdb
```
#### Updating Nginx configuration

***Note:*** This only applies if you are using Nginx and https.

Please, make sure you have this settings on your Nginx config:

    proxy_pass http://localhost:5985/;
    proxy_redirect http:// $scheme://;

<a name="server-configuration"></a>
#### Configuration

By default, Faraday server will listen on port **5985**. You can edit this on `~/.faraday/config/server.ini`.

#### Authentication

You can create different types of users through the web UI. Those users can login though the same web UI or though a Faraday client using the `--login` flag (Faraday will ask for the credentials later)

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

Once everything is installed you need to configure your server properly. 

After configuring, you can proceed to run the Faraday Server script:

```
$ python2 faraday-server.pyc
```

If you want to run the server in background mode, you should use the `--start` option:

```
$ python2 faraday-server.pyc --start
```

This is the recommended way to do this. Other methods like using the bash `&` could cause unexpected IOErrors and other related exceptions.

#### Web UI

Once the server is running, you can access Faraday's Web UI using any browser:
just point it to `http://SERVER_IP:SERVER_PORT/` (by default it will be
http://localhost:5985/) and you can start playing with Faraday.


<a name="faraday-client-pro"></a>
### Faraday Client

Faraday Client is the software which will allow you to work with your favorite security tools and capture their output in an organized manner. It works under a GTK+3 interface with the popular VTE terminal with a custom ZSH shell that respects the user's configuration (yes, that means you get to keep your exact ZSH terminal inside Faraday, even if you use ZPrezto or Oh My ZSH).

From the client you can also create and delete workspaces, specify plugin configuration, view information about your hosts, resolve conflics that may arise and much more.

It's also a responsibility of the client to send all of the collected information to the server, which will then process it and format it in an friendly way for you to view, edit, and confirm.

The client is bundled in the same package as the server, so if you have already downloaded Faraday, you can skip the next step.

#### Downloading

After the purchase you will receive an email with your credentials and a link to our **Customers Portal**. Use those credentials to log in to the site and you will get two links:

* Download License - this is the tarball for the **Faraday License**
* Download Faraday - this is the tarball for the actual **Faraday Code**

Download both those packages and then:

1. Create a new directory and unpack the **Faraday tarball** there. For example, `/home/user/Infobyte/faraday`.

1. Unpack the **License Package** and place its contents in the `doc` directory. For example, using the path from **Step 1**, you should place the **License files** in `/home/user/Infobyte/faraday/doc`.

After doing so, make sure to [install system dependencies](#client-system-dependencies), [install Python dependencies](#client-python-dependencies) and [configure the Client](#client-configuration).

#### Requirements

Faraday Client works under any modern Linux distribution or Mac OS X, and needs Python 2.6 or 2.7.

The Python requirements for the client are stored in the [`requirements.txt` file](https://github.com/infobyte/faraday/blob/master/requirements.txt). Some additional requirements are necessary for specific features to work, these are stored in the [`requirements_extras.txt` file](https://github.com/infobyte/faraday/blob/master/requirements_extras.txt).

Out tests include [Debian](#client-debian), [Ubuntu](#client-debian), [Kali](#client-kali), [Backtrack](#client-debian) and [OSX Sierra](https://github.com/infobyte/faraday/wiki/Installation-OSX).

If instead of installing you want to take a quick look at Faraday you can also use [Docker](#client-docker).

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
$ sudo apt-get install libpq-dev python-pip python-dev gir1.2-gtk-3.0 gir1.2-vte-2.90 python-gobject zsh curl
```

If you are any other version, please execute the following command:

```
$ sudo apt install libpq-dev python-pip python-dev gir1.2-gtk-3.0 gir1.2-vte-2.91 python-gobject zsh curl
```

<a name="client-kali"></a>
##### Kali

Faraday comes pre-installed in Kali Rolling. However, that version is **incompatible** with the **Pro License**. Follow the [Debian install steps](#client-debian) to install.

##### ArchLinux

Before installing Faraday you will need to get some user-contributed packages. In order to do this quickly we need an [AUR](https://wiki.archlinux.org/index.php/Arch_User_Repository) wrapper, in this case we will use [Yaourt](http://archlinux.fr/yaourt-en). After installing Yaourt run:

```
$ yaourt -S python2-dateutil python2-pip mime-types python2-gobject gtk3 vte3 postgresql-libs
```

<a name="client-python-dependencies"></a>
#### Installing Python 2 dependencies

Once you have the required system dependencies, you just have to install the Python modules needed to run the client using `pip`:

```
$ pip2 install -r requirements.txt -U
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
$ python2 faraday.pyc
```

Some distributions or installations require additional steps, so look down below if you are using something different than Debian or Ubuntu, or if you need to apply some configuration to the client.

<a name="client-docker"></a>
##### Docker

[You can find instructions on how to run the client inside a Docker container here.](https://github.com/infobyte/faraday/wiki/installation-docker)

<a name="client-osx"></a>
##### OSX

[You can find instructions on how to run the client under Mac OSX here.](https://github.com/infobyte/faraday/wiki/Installation-OSX)