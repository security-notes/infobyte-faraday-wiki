
# Ubuntu/Kali

#### Postgres

First of all, you'll need to install postgresql > 9.5 locally or in a remote server. You can run:
```
sudo apt install postgresql
#Verify postgres version > 9.5
psql --version
```
#### Faraday

Download faraday's installer from [our web site](https://portal.faradaysec.com)
```
sudo apt install ./faraday-server_amd64.deb
```
After installation, if postgres is running locally:
```
sudo faraday-manage initdb
```
Otherwise, [follow this guide](https://github.com/infobyte/faraday/wiki/Remote-PostgreSQL-database-configuration)
# CentOS7/RedHat7

#### Before install
Please note that PostgreSQL YUM repository and Faraday depends on EPEL repository for some packages. RHEL/CentOS/, etc. users should install EPEL repo RPM along with PGDG repo RPMs to satisfy dependencies.
```
subscription-manager repos --enable rhel-7-server-optional-rpms --enable rhel-7-server-extras-rpms
curl -o epel.rpm http://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
rpm -Uvh epel-release-latest-7.noarch.rpm
```

#### Postgres (https://yum.postgresql.org/)

You'll need to install postgresql > 9.5 locally or in a remote server:

```
rpm -Uvh https://download.postgresql.org/pub/repos/yum/reporpms/EL-7-x86_64/pgdg-redhat-repo-latest.noarch.rpm
yum install postgresql95-server postgresql95
/usr/pgsql-9.5/bin/postgresql95-setup initdb
systemctl start postgresql-9.5
systemctl enable postgresql-9.5
```

#### Faraday

Download faraday's installer from [our web site](https://portal.faradaysec.com)

```
sudo yum install ./faraday-server_amd64.rpm
```
After installation, if postgres is running locally:

* Modify the localhost authenication type from "ident" to "md5" within hba config. Change host IPV4 local and IPV6 local from "ident" to "md5"
```
# vim /var/lib/pgsql/VERSION/data/pg_hba.conf

# IPv4 local connections:
host    all             all             127.0.0.1/32            md5
# IPv6 local connections:
host    all             all             ::1/128                 md5
```
* And then:
```
sudo faraday-manage initdb
```
Otherwise, [follow this guide](https://github.com/infobyte/faraday/wiki/Remote-PostgreSQL-database-configuration)

# MacOS DMG

```
```

# Binary files

The binary package contains three executable files:

* faraday-client
* faraday-server
* faraday-manage

```
unzip linux_binaries.zip
```