
# Ubuntu/Kali
Faraday use postgresql > 9.5 as database. First of all, you'll need to install it locally or in a remote server. You can run:
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
```

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