<a name="index"></a>
* [Debian/Ubuntu/Kali](#linux)
* [CentOS7/RedHat7](#centos/redhat)
* [MacOS DMG](#macos)
* [Binary Files](#binary-files)
* [Installation from PyPI](#pypi)
* [Installation from Git repo](#git-repo)
* [How to run Faraday](#how-to-run-faraday)


<a name="linux"></a>
## Debian/Ubuntu/Kali

#### Downloading Faraday

* **Community version:** Download Faraday's installer from our Github [project](https://github.com/infobyte/faraday/releases)

* **Commercial versions:** Download Faraday's installer from [customers portal](https://portal.faradaysec.com).

#### Installing the database

First of all, you'll need to install **postgresql > 9.5** (locally or in a remote server). In order to install PostgreSQL, you can run the following command:

```
$ sudo apt install postgresql
```

After the installation is completed, verify that PostgreSQL version is higher than 9.5 by running:

```
$ psql --version
```

#### Installing Faraday

Once you have downloaded Faraday's installer and installed PostgreSQL, run the following command:

```
$ sudo apt install ./faraday-server_amd64.deb
```

Once the installation is completed, follow these instructions according to where your PostgreSQL instance is running:

* If PostgreSQL is running locally:

    Run the following command:

    ```
    $ sudo faraday-manage initdb
    ```

* If PostgreSQL is running in a remote machine:

    Please, [follow this guide](https://github.com/infobyte/faraday/wiki/Remote-PostgreSQL-database-configuration)

#### License for commercial versions

1. Download your Faraday's license from [our web site](https://portal.faradaysec.com).
2. Untar your license inside the folder `/home/faraday/.faraday/doc/`

#### After installation

Once the installation is completed and the license is located in the right folder (for commercial versions), we can start Faraday's server by running: 

```
$ systemctl start faraday-server
```

To know how to run Faraday's multiple commands, please follow this [link](#how-to-run-faraday).

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

#### Downloading Faraday

* **Community version:** Download Faraday's installer from our Github [project](https://github.com/infobyte/faraday/releases)

* **Commercial versions:** Download Faraday's installer from [customers portal](https://portal.faradaysec.com).

#### Installing the database (https://yum.postgresql.org/)

You'll need to install **postgresql > 9.5** (locally or in a remote server). In order to install PostgreSQL, run the following commands:

```
$ rpm -Uvh https://download.postgresql.org/pub/repos/yum/reporpms/EL-7-x86_64/pgdg-redhat-repo-latest.noarch.rpm
$ yum install postgresql95-server postgresql95
$ /usr/pgsql-9.5/bin/postgresql95-setup initdb
$ systemctl start postgresql-9.5
$ systemctl enable postgresql-9.5
```

#### Installing Faraday

Once you have downloaded Faraday's installer and installed PostgreSQL, run the following command:

```
$ sudo yum install ./faraday-server_amd64.rpm
```

Once the installation is completed, follow these instructions according to where your PostgreSQL instance is running:

* If PostgreSQL is running locally:

  * You need to open the pg_hba.conf file. There, you need to modify the localhost authentication type from "ident" to "md5". To do this, change host IPV4 local and IPV6 local from "ident" to "md5":

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
  * Restart PostgreSQL server:
    ```
    $ sudo sysmtectl restart postgresql-9.5
    ```
  * Once you have edited the file and restarted PostgreSQL server, let's initialize the database by running the following command:
    ```
    $ sudo faraday-manage initdb
    ```

* If PostgreSQL is running in a remote machine: 

  Please, [follow this guide](https://github.com/infobyte/faraday/wiki/Remote-PostgreSQL-database-configuration)

#### License for commercial versions

1. Download your Faraday's license from [our web site](https://portal.faradaysec.com).
2. Untar your license inside the folder `/home/faraday/.faraday/doc/`

#### After installation

Once the installation is completed and the license is located in the right folder (for commercial versions), we can start Faraday's server by running: 

```
$ systemctl start faraday-server
```

To know how to run Faraday's multiple commands, please follow this [link](#how-to-run-faraday).

<a name="macos"></a>
## MacOS DMG

Instructions for Faraday's installation in MacOS are specified in this [installation guide](https://github.com/infobyte/faraday/wiki/Development-Installation-OSX).

<a name="binary-files"></a>
## Binary files

#### Downloading Faraday

* **Community version:** Download Faraday's installer from our Github [project](https://github.com/infobyte/faraday/releases)

* **Commercial versions:** Download Faraday's installer from [our web site](https://portal.faradaysec.com).

Once you have downloaded the package, you need to unzip it:

```
$ unzip linux_binaries.zip
```

This binary package contains four executable files:

* faraday-client
* faraday-server
* faraday-manage
* faraday-fplugin

#### Installing Faraday

In order to install Faraday, please run the file **faraday-server**:

```
$ ./faraday-server
```
#### License for commercial versions

1. Download your Faraday's license from [our web site](https://portal.faradaysec.com).
2. Untar your license inside the folder `/home/faraday/.faraday/doc/`

#### After installation

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

Installation guide for **community version**

You can install faradaysec from PyPI by running the following command:

```
$ pip install faradaysec
```

#### After installation

Once the installation is completed, we can start Faraday's server by running: 

```
$ faraday-server
```

To know how to run Faraday's multiple commands, please follow this [link](#how-to-run-faraday).

<a name="git-repo"></a>
## Installation from git repo

Installation guide for **community version**

In order to install Faraday's community version, you can use pip to install Faraday or you can clone the repository. 

Before installing Faraday, we need to run Faraday inside a virtualenv. In order to install and create a virtualenv, run the following commands:

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

To know how to run Faraday's multiple commands, please follow this [link](#how-to-run-faraday).

***


<a name="how-to-run-faraday"></a>
### How to run Faraday

In order to check how to run Faraday, please follow refer to [How to run Faraday](https://github.com/infobyte/faraday/wiki/How-to-run-Faraday) wiki.