<a name="index"></a>
* [Debian/Ubuntu/Kali](#linux)
* [CentOS7/RedHat7](#centos/redhat)
* [MacOS DMG](#macos)
* [Binary Files](#binary-files)

<a name="linux"></a>
## Debian/Ubuntu/Kali

#### Installing PostgreSQL

First of all, you'll need to install **postgresql > 9.5** (locally or in a remote server). In order to install PostgreSQL, you can run the following command:

```
$ sudo apt install postgresql
```

After the installation is completed, verify that PostgreSQL version is higher than 9.5 by running:

```
$ psql --version
```

#### Installing Faraday

Download Faraday's installer from [our web site](https://portal.faradaysec.com).

Once you have downloaded the installer, run the following command:

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

<a name="centos/redhat"></a>
## CentOS7/RedHat7

#### Before installation

Please note that PostgreSQL YUM repository and Faraday, depend on EPEL repository for some packages. Users with RHEL, CentOS, etc. should install EPEL repo RPM along with PGDG repo RPMs to satisfy dependencies. In order to do that, you should run the following commands:

```
$ subscription-manager repos --enable rhel-7-server-optional-rpms --enable rhel-7-server-extras-rpms
$ curl -o epel.rpm http://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
$ rpm -Uvh epel.rpm
```

#### PostgreSQL installation (https://yum.postgresql.org/)

You'll need to install **postgresql > 9.5** (locally or in a remote server). In order to install PostgreSQL, run the following commands:

```
$ rpm -Uvh https://download.postgresql.org/pub/repos/yum/reporpms/EL-7-x86_64/pgdg-redhat-repo-latest.noarch.rpm
$ yum install postgresql95-server postgresql95
$ /usr/pgsql-9.5/bin/postgresql95-setup initdb
$ systemctl start postgresql-9.5
$ systemctl enable postgresql-9.5
```

#### Faraday installation

Download Faraday's installer from [our web site](https://portal.faradaysec.com).

Once you have downloaded the installer, run the following command:

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
  * Once you have edited the file, let's initialize the database by running the following command:
    ```
    $ sudo faraday-manage initdb
    ```

* If PostgreSQL is running in a remote machine: 

  Please, [follow this guide](https://github.com/infobyte/faraday/wiki/Remote-PostgreSQL-database-configuration)


<a name="macos"></a>
## MacOS DMG

Instructions for Faraday's installation in MacOS will be specified soon. Meanwhile, you can use former installation guide for MacOS by following this [link](https://github.com/infobyte/faraday/wiki/Installation-OSX).

<a name="binary-files"></a>
## Binary files

Download Faraday's binary package from [our web site](https://portal.faradaysec.com).

Once you have downloaded the package, you need to unzip it:

```
$ unzip linux_binaries.zip
```

This binary package contains three executable files:

* faraday-client
* faraday-server
* faraday-manage

In order to install Faraday, please run the file **faraday-server**:

```
$ ./faraday-server
```