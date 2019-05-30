## Redhat 7
![](https://raw.githubusercontent.com/wiki/infobyte/faraday/images/platform/redhat.jpeg)

<a name="faraday-server"></a>
### Faraday Server

Faraday Server is the interface between PostgreSQL and Faraday Client and WebUI. The server's responsibility is to transmit information between the client or WebUI and PostgreSQL, and make sure that they are kept in sync. The Web UI client, which allows you to handle enormous workspaces from your favorite web browser.

**Important:** You should keep in mind that is recommended to install Faraday server on the same instance as PostgreSQL.

#### Downloading

After the purchase you will receive an email with your credentials and a link to our **Customers Portal**. Use those credentials to log in to the site and you will get two links:

* Download License - this is the tarball for the **Faraday License**
* Download Faraday - this is the tarball for the actual **Faraday Code**

Download both those packages and then:

1. Create a new directory and unpack the **Faraday tarball** there. For example, `/home/user/Infobyte/faraday`.

1. Unpack the **License Package** and place its contents in the `doc` directory. For example, using the path from **Step 1**, you should place the **License files** in `/home/user/Infobyte/faraday/doc`. Or run: 

    ```
    $ faraday-server --license-path path/to/license
    ```

After doing so, make sure to [install system dependencies](#server-system-dependencies), [install Python dependencies](#server-python-dependencies) and [configure the Server](#server-configuration).


<a name="server-system-dependencies"></a>
#### Installing system dependencies

* Enable EPEL and REMI repositories for installing all needed deps.
```
$ sudo wget http://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
$ sudo rpm -Uvh epel-release-latest-7.noarch.rpm
```
* Install the default development tools:
```
$ sudo yum groupinstall 'Development Tools'
```
* Now, install the dependencies:
```
$ sudo yum install python-setuptools python-pip libffi-devel python-devel openssl-devel openldap-devel curl zsh libxslt-devel pkgconfig postgresql postgresql-server postgresql-libs libxml2-devel libxslt-devel freetype-devel libjpeg-devel gtk+-devel gtk3-devel gtk2-devel mailcap
```

* Create the initial set of databases for PostgreSQL to function:
```
$ sudo postgresql-setup initdb
```

* Modify the localhost authenication type from "ident" to "md5" within hba config. Change host IPV4 local and IPV6 local from "ident" to "md5":
```
# nano /var/lib/pgsql/VFERSION/data/pg_hba.conf
```
```
# IPv4 local connections:
host    all             all             127.0.0.1/32            md5
# IPv6 local connections:
host    all             all             ::1/128                 md5
```


<a name="server-python-dependencies"></a>
#### Installing Python 2 dependencies

Once you have the required system dependencies, you just have to install the Python modules needed to run the server using pip:
```
$ sudo pip2 install -r requirements_server.txt -U
```

<a name="server-configuration"></a>
#### Configuring Faraday Server

#### Initializing PostgreSQL

In order to initialize PostgreSQL database, generate your main _user_ and a __password__ and import your data from CouchDB (if it's the case), run the following command:

```
$ python manage.pyc initdb
```
If you don't have CouchDB configured we assume this is a new installation, so a
new user will be created.

With CouchDB configured in the `server.ini` file, it will import all the data
you had from the 2.7.2 version, including the users and its hashed passwords. 

If you want to manually import the data from CouchDB, follow this [step](https://github.com/infobyte/faraday/wiki/Installation-RedHat/_edit#manually-importing-from-couchdb)

Keep in mind the following items:

* This commmand must be executed only when you run Faraday for the first time. 
* If you can't login into to Faraday after running the command above due to invalid credentials, you can change your password through the PostgreSQL shell that Faraday has in it. Follow the next [instructions](https://github.com/infobyte/faraday/wiki/Troubleshooting#cant-login-after-importing-from-couch) in order to change your password and be able to login.

* You should have the PostgreSQL service started. To do it run
`systemctl start postgresql.service`.

*  If at the moment you run this command, it throws an error, be sure
you have sudo installed. Once you have installed it, run the command again.


#### Manual PostgreSQL configuration

If you need an advance configuration of the PostgreSQL database, like having a
custom database name or run it in a separate host, the `python manage.pyc initdb`
command probably won't be enough for you, so you should configure it manually
by doing something like this:

```
$ sudo -u postgres psql -c "CREATE ROLE faraday_postgresql WITH LOGIN PASSWORD 'YOURPASSWORD'"
$ sudo -u postgres createdb -O faraday_postgresql faraday
```

Then, edit the `~/.faraday/config/server.ini` by adding the connection string
to the database:

```
[database]
connection_string = postgresql+psycopg2://faraday_postgresql:YOURPASSWORD@localhost/faraday
```

Then you should run `python manage.pyc create-tables` to create all the required
tables to make Faraday work, and `python manage.pyc createsuperuser` to create an
admin user.


#### Manually importing from CouchDB

If you were using Faraday 2.7.2 and setup the database manually instead of
using the `python manage.pyc initdb`, you should run the following command to import
the data from CouchDB:

```
$ python manage.pyc import-from-couchdb
```
***Note:*** beware of the number of users you have created in CouchDB, remember that you have already created one when you initialized PostgreSQL. The number of users that you have between CouchDB and PostgreSQL should not surpass the number of users you're allow to have according to your license.

#### Exposing the Server

In order to access Faraday server from a different box, you need to expose the server. In order to do so, follow these instructions:

*  Edit the file located in ~/.faraday/config/server.ini and under the section [faraday-server] set the param bind-address to 0.0.0.0, it should look something like this:

```
[faraday-server]
...
bind_address=0.0.0.0
```

*  Get a list of active zones. You might have more than the defaults.
```
$ firewall-cmd --get-active-zones
```

*  If it's the default CentOS install,  you'll need to enable and start firewall.
```
$ sudo systemctl start firewalld
$ sudo systemctl enable firewalld
```
*  Firewalld command to add port 5985 (port used by Faraday):
```
$ firewall-cmd --zone=public --add-port=5985/tcp --permanent
```

*  If it's the default centos install, you'll likely want to also allow connections to ss:
```
$ firewall-cmd --zone=public --add-port=22/tcp --permanent
```

*  Restart the firewalld service:
```
$ firewall-cmd --reload
```
#### Running

Once everything is installed and the server is configured, you can now proceed to run the Faraday server script:

```
$ python2 faraday-server.pyc
```

If you want to run the server in background mode, you should use the `--start` option:

```
$ python2 faraday-server.pyc --start
```

This is the recommended way to do this. Other methods like using the bash `&` could cause unexpected IOErrors and other related exceptions.

***

### Faraday Client
<a name="client-python-dependencies"></a>
#### Installing Python 2 dependencies

Once you have the required system dependencies, you just have to install the Python modules needed to run the client using `pip`:

```
$ pip2 install -r requirements.txt
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

#### Running

Once you have already configured the client and have Faraday Server running, you simply have to run:

```
$ python2 faraday.pyc
```

Some distributions or installations require additional steps, so look down below if you are using something different than Debian or Ubuntu, or if you need to apply some configuration to the client.

***

### Troubleshooting

#### Cannot uninstall [dependency]
If you were installing Python dependencies and suddenly you got this message:

> Cannot uninstall [dependency]. It is a distutils installed project and thus we cannot accurately determine which files belong to it which would lead to only a partial uninstall.

You should delete that dependency in order to be able to upgrade it to the version that is required by Faraday. Please follow these instructions:

* Search the right name of the dependency to be uninstall:
```
    $ yum list installed | grep [dependency]
```
* Once you have the right name of the dependency, uninstall it:
```
    $ sudo yum remove [dependency]
```
* Install Python dependencies by running this command again:
```
    $ sudo pip2 install -r requirements_server.txt -U
```
If after trying to install the dependencies again, you have the same issue but with another dependency, repeat the instructions above.

#### AttributeError: 'module' object has no attribute

If you get the following error:

> Error : AttributeError: 'module' object has no attribute 'OP_NO_TLSv1_1'

Run the following command:
```
pip install Twisted==16.4.1
```

Now start Faraday Server.