
# Ubuntu/Kali
First of all, you'll need to install postgresql > 9.5 locally or in a remote server. You can run:
```
sudo apt install postgresql
#Verify postgres version > 9.5
psql --version
```
Then download faraday's installer from [our web site](https://portal.faradaysec.com)
```
sudo apt install ./faraday-server_amd64.deb
```
Once installed, let's create database and tables with:

If postgres is running locally please do:
```
sudo faraday-manage initdb
```
Otherwise, configure [database] section on /home/faraday/.faraday/server.ini with correct postgresql string:
```
sudo vim /home/faraday/.faraday/server.ini
.
.
[database]
postgresql+psycopg2://faraday_postgresql:PASSWORD@IPADDR/faraday
.
.
```
Finally run:

```
sudo faraday-manage create-tables
```

# CentOS/RedHat

```
sudo yum install ./faraday-server_amd64.rpm
```

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