## Redhat 7
![](https://raw.githubusercontent.com/wiki/infobyte/faraday/images/platform/faraday_redhat.jpeg)

#### Enable EPEL and REMI repositories for installing all needed deps.
```
wget http://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
rpm -Uvh epel-release-latest-7.noarch.rpm
```
#### Install the default development tools to easy compile/install couchdb
```
yum groupinstall 'Development Tools'
```

#### Install Faraday dependencies.
```
yum install ipython python-setuptools python-pip libffi-devel python-devel openssl-devel openldap-devel curl zsh libxslt-devel pkgconfig postgresql postgresql-libs libxml2-devel libxslt-devel libxml++-devel pygobject2-devel freetype-devel libjpeg-devel gtk+-devel gtk3-devel gtk2-devel vte-devel mailcap
```

#### Create the inital set of databases for postgres to function
```
postgresql-setup initdb
```

#### Modify the localhost authenication type from ident to md5 witin hba config 
```
nano /var/lib/pgsql/data/pg_hba.conf
```
Change host IPV4 local and IPV6 local from ident to md5 
```
# IPv4 local connections:
host    all             all             127.0.0.1/32            md5
# IPv6 local connections:
host    all             all             ::1/128                 md5
```

#### Setup Database and create faraday postgres user

Either execute :
```
./manage.py initdb
```
or to do it manually:
```
sudo -u postgres psql -c "CREATE ROLE faraday_postgresql WITH LOGIN PASSWORD 'PASSWORD'"
sudo -u postgres createdb -O faraday_postgresql faraday
```

#### Get a list of active zones. You might have more than the defaults.
```
firewall-cmd --get-active-zones
```

#### If it's the default centos install,  you'll need to enable and start firewall.
```
sudo systemctl start firewalld
sudo systemctl enable firewalld
```

#### Firewalld command to allow this port open to dmz:
```
firewall-cmd --zone=public --add-port=5985/tcp   --permanent
```

#### If it's the default centos install, you'll likely want to also allow connections to ss.
```
firewall-cmd --zone=public --add-port=22/tcp   --permanent
```

#### Restart the firewalld service
```
firewall-cmd --reload
```

#### Update the version of pip included within setuptools
```
pip install --upgrade pip
```

#### Install virtualenv to nicely contain our python app 
```
pip install virtualenv
```

#### Create a new faraday user to run our python app
```
sudo adduser -r --home /opt/faraday/ -m --shell /bin/bash --comment "Faraday Service Account" faraday
```

#### Grab the latest version of faraday and put it within users home directory
```
cd /opt/
git clone https://github.com/infobyte/faraday.git
```
#### Make the faraday user the owner of the application files 
```
chown -R faraday:faraday faraday/
```

#### Switch to the faraday user to setup local enviroment
```
su - faraday
```

#### Create a new virtual project for our faraday install and activate it
```
virtualenv faraday
source faraday/bin/activate
```

#### install all of the required python packages
```
pip2 install -r requirements_server.txt
```

#### Start the server for the first time and exit once it fails
```
./faraday-server.py
```

#### Edit the default configuration file to bind on all local interfaces and add our couchdb credentials
```
vi /opt/faraday/.faraday/config/server.ini
```
The following can be used as a guide
```
[faraday_server]
port=5985
bind_address=0.0.0.0

[couchdb]
#Deprecated config
host=localhost
port=5984
ssl_port=6984
user=<user>
password=<password>
protocol=http

[database]
connection_string = postgresql+psycopg2://faraday_postgresql:<password>@localhost/faraday
```

#### Build out the database and your admin user
```
python2 manage.pyc create_tables
python2 manage.pyc createsuperuse
```

#### Then if needed, you can import from couchdb
```
python2 manage.pyc import_from_couchdb
```

#### Exit the faraday user shell and create a service unit to control the faraday server
```
exit
sudo nano /usr/lib/systemd/system/faraday-server.service
```
The following service unit can be used as a templete
```
[Unit]
Description=Faraday Web Server
After=network.target

[Service]
Type=forking
ExecStart=/opt/faraday/faraday/bin/python2 /opt/faraday/faraday-server.py
Restart=always
RestartSec=30
StartLimitInterval=600
StartLimitBurst=3
User=faraday
TimeoutSec=1200

[Install]
WantedBy=multi-user.target
```

License
----

MIT