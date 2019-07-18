**Faraday Server** is the interface between PostgreSQL and **Faraday Client** and the WebUI. The Server's responsibility is to transmit information between the client or WebUI and PostgreSQL, and make sure that they are kept in sync.

It is recommended to install Faraday Server on the same instance as PostgreSQL.

<a name="index"></a>
* [Debian/Ubuntu/Kali](#linux)
* [CentOS7/RedHat7](#centos/redhat)
* [MacOS DMG](#macos)
* [Binary Files](#binary-files)
* [Installation from PyPI](#pypi)
* [Installation from Git repo](#git-repo)


<a name="linux"></a>
## Debian/Ubuntu/Kali
1. Download Faraday's installer from our [Github project](https://github.com/infobyte/faraday/releases).

2. Install **postgresql > 9.5** (locally or in a remote server). In order to install PostgreSQL, you can run the following command:

`$ sudo apt install postgresql`


3. After the installation is completed, verify that PostgreSQL version is higher than 9.5 by running:

`$ psql –version`


4. Go to your Download directory and run the following command:

`$ sudo apt install ./yourInstallFileName.deb`


5. If PostgreSQL is running in a remote machine please follow [these instructions](https://github.com/infobyte/faraday/wiki/Remote-PostgreSQL-database-configuration). If, instead, it is running locally, simply run: 

`$ sudo faraday-manage initdb`


6. Start Faraday's server by running:

`$ systemctl start faraday-server`


To know how to run Faraday's multiple commands, please follow this [link](https://github.com/infobyte/faraday/wiki/How-to-run-Faraday).


<a name="centos/redhat"></a>
## CentOS7/RedHat7

#### Before installation

Please note that PostgreSQL YUM repository and Faraday, depend on EPEL repository for some packages. Users with RHEL, CentOS, etc. should install EPEL repo RPM along with PGDG repo RPMs to satisfy dependencies. In order to do that, follow these instructions:

If you are using RHEL, first run the following command:
```
$ subscription-manager repos --enable rhel-7-server-optional-rpms --enable rhel-7-server-extras-rpms
```

Run the following commands to install EPEL repo in RHEL or CentOS:
```
$ curl -o epel.rpm http://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
$ rpm -Uvh epel.rpm
```

1. Download Faraday's installer from our [Github project](https://github.com/infobyte/faraday/releases).

2. Install **postgresql > 9.5** (locally or in a remote server). In order to install [PostgreSQL](https://yum.postgresql.org/), you can run the following command:

```
$ rpm -Uvh https://download.postgresql.org/pub/repos/yum/reporpms/EL-7-x86_64/pgdg-redhat-repo-latest.noarch.rpm
$ yum install postgresql95-server postgresql95
$ /usr/pgsql-9.5/bin/postgresql95-setup initdb
$ systemctl start postgresql-9.5
$ systemctl enable postgresql-9.5
```


3. After the installation is completed, verify that PostgreSQL version is higher than 9.5 by running:

`$ psql –version`


4. Go to your Download directory and run the following command:

`$ sudo yum install ./yourInstallFileName.rpm`


5. If PostgreSQL is running in a remote machine please follow [these instructions](https://github.com/infobyte/faraday/wiki/Remote-PostgreSQL-database-configuration). If, instead, it is running locally, you need to open the pg_hba.conf file. There, you need to modify the localhost authentication type from "ident" to "md5". To do this, change host IPV4 local and IPV6 local from "ident" to "md5":

    Open the pg_hba.conf file (remember to specify the right PostgreSQL version):

    ```
    $ nano /var/lib/pgsql/POSTGRESQL_VERSION/data/pg_hba.conf
    ```
    Once you have opened the file, you need to edit the following lines so the authentication type is set from "ident" to "md5":
    ```
    # IPv4 local connections:
    host    all             all             127.0.0.1/32            md5
    # IPv6 local connections:
    host    all             all             ::1/128                 md5
    ```
6. Restart PostgreSQL server and initialize the database: 

```
$ sudo sysmtectl restart postgresql-9.5 
$ sudo faraday-manage initdb
```

7. Start Faraday's server by running:

`$ systemctl start faraday-server`


To know how to run Faraday's multiple commands, please follow this [link](https://github.com/infobyte/faraday/wiki/How-to-run-Faraday).


<a name="macos"></a>
## MacOS DMG

Instructions for Faraday's installation in MacOS are specified in this [installation guide](https://github.com/infobyte/faraday/wiki/Development-Installation-OSX).

<a name="binary-files"></a>
## Binary files

#### Downloading Faraday

1. Download Faraday's installer from our Github [project](https://github.com/infobyte/faraday/releases)

2. Once you have downloaded the package, you need to unzip it:

```
$ unzip linux_binaries.zip
```

This binary package contains four executable files:

* faraday-client
* faraday-server
* faraday-manage
* faraday-fplugin

3. In order to install Faraday, please run the file **faraday-server**:

```
$ ./faraday-server
```

Once the installation is completed, we can run every executable file as follow: 

* To run Faraday's Server:

    ```
    $ ./faraday-server
    ```

* To run Faraday's Client:
    ```
    $ ./faraday-client
    ```

* To run Faraday's Manage:
    ```
    $ ./faraday-manage
    ```

* To run Faraday's Plugin:
    ```
    $ ./faraday-fplugin
    ```

<a name="pypi"></a>
## Installation from PyPI

You can install Faraday from PyPI by running the following command:

```
$ pip install faradaysec
```

#### After installation

Once the installation is completed, we can start Faraday's server by running: 

```
$ faraday-server
```

To know how to run Faraday's multiple commands, please follow this [link](https://github.com/infobyte/faraday/wiki/How-to-run-Faraday).

<a name="git-repo"></a>
## Installation from Git repo

In order to install Faraday's Community version, you can use pip to install Faraday or you can clone the repository.

Before installing Faraday, we need to create a virtualenv so Faraday runs in it. In order to install and create a virtualenv, run the following commands:

```
$ pip install virtualenv
$ virtualenv -p python2 faraday_venv
$ source faraday_env/bin/activate 
```

For more information about virtualenv, please follow this [link](https://virtualenv.pypa.io/en/latest/userguide/).

**Installing Faraday**

* Installing using Pip
```
$ pip install git+git@github.com:infobyte/faraday.git
```

* Cloning the repository:

```
$ git clone git@github.com:infobyte/faraday.git
$ cd faraday-dev/
$ python setup.py install
```

#### After installation

Once the installation is completed, we can start Faraday's server by running: 

```
$ faraday-server
```

To know how to run Faraday's multiple commands, please follow this [link](https://github.com/infobyte/faraday/wiki/How-to-run-Faraday).

***