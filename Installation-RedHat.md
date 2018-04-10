## Redhat 6
![](https://raw.githubusercontent.com/wiki/infobyte/faraday/images/faraday_redhat.jpeg)
### Docker
Install Docker using EPEL.
Now, go to the terminal and run this command-lines:

    $  wget https://dl.fedoraproject.org/pub/epel/epel-release-latest-6.noarch.rpm

    $  rpm -ivh epel-release-latest-6.noarch.rpm

Create a folder _docker_ with two sub-folders: 

   1. _etc_
   2. _dbs_

Now you'll need the paths of those folders for the next command.

     $ sudo docker run --name couchdb_Faraday -v /home/USER/docker/etc/:/usr/local/etc/couchdb/local.d -v /home/USER/docker/dbs/:/usr/local/var/lib/couchdb -d -p 5984:5984 couchdb:1.7.1





***
You'll need to have your RedHat's official credentials for the next step
***

    $  subscription-manager repos --enable=rhel-server-rhscl-6-rpms

    $  subscription-manager repos --enable=rhel-6-server-optional-rpms

### System Dependencies 

It's time to install some system dependencies Faraday needs!

    $  yum install gcc libffi-devel openssl-devel python27-python python27-python-devel libxml2-devel libxslt-devel 

    $  yum install freetype-devel libpng-devel libsodium-devel
  
    $  scl enable python27 bash

    $   yum install -y python-pip

    $   pip install --upgrade pip

### Python libraries via PIP

    $  pip install -r requirements_server.txt

    $  pip install -r requirements.txt

## Faraday
Final step! Now all you need to do is Run the server:

    $  python faraday-server.py (first run to install missing dependencies)

### Going for it!

Almost there! Start Faraday's server:

    $ cd faraday
    $ ./faraday-server.py

And in another terminal start the client runing:

    $ cd faraday
    $ ./faraday.py

***
## Redhat 7
![](https://raw.githubusercontent.com/wiki/infobyte/faraday/images/faraday_redhat.jpeg)

To configure red hat subscription: https://access.redhat.com/labs/registrationassistant/#!/rhel7/

Enable the following repositories:

    $ subscription-manager repos --enable=rhel-7-server-rpms

    $ subscription-manager repos --enable=rhel-7-server-extras-rpms

    $ subscription-manager repos --enable=rhel-7-server-optional-rpms

Run the following command to install the requirements:

    $ sudo yum install python-devel gcc mailcap vte3 xorg-x11-xauth gcc python-devel zsh

    Note: mailcap is for mime types.

### Installing Docker

Let's install Docker: 

    $ sudo yum install docker

Now we need to start Docker:

    $ systemctl start docker.service

If you want to configure Docker to start on boot, run the following command:

    $ systemctl enable docker.service

### Use Couchdb in a Docker container

Create a folder _docker_ with two sub-folders: 

   1. _etc_
   2. _dbs_

Now you'll need the paths of those folders for the next command.

    $ sudo docker run --name couchdb_Faraday -v /home/USER/docker/etc/:/usr/local/etc/couchdb/local.d -v /home/USER/docker/dbs/:/usr/local/var/lib/couchdb -d -p 5984:5984 couchdb:1.7.1

In case you can’t start Couchdb container, type the following command:

    $ sudo docker logs xxx   (where ‘xxx’ are the first three characters of the container’s ID)

Now check if it shows the following error:

    Error: chown: cannot read directory '/usr/local/var/lib/couchdb': Permission denied

In this case, run the following commands: 

    $ su -c "setenforce 0"

    $ chcon -Rt svirt_sandbox_file_t $HOME/docker

### Create couchdb admin

    $ curl -s -X PUT http://{IP}:{PORT}/_config/admins/{ADMIN_NAME} -d '"{ADMIN_PASSWORD}"'

Example:

    $ curl -s -X PUT http://localhost:5984/_config/admins/rob -d '"123456"'


### Install Epel 

We require epel Installing efor python-pip. Please run the following commands:

    $ wget https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm

    $ rpm -ivh epel-release-latest-7.noarch.rpm


### Python libraries via PIP

    $ sudo pip install -r requirements_server.txt

We're almost there. Let's open firewall's port

    $ sudo firewall-cmd --zone=public --add-port=5985/tcp --permanent

    $ sudo firewall-cmd --reload

## Faraday

Finally, let's run the server

    $ ./faraday-server.py (first run to install missing dependencies)

If you get the following error:

    Error : AttributeError: 'module' object has no attribute 'OP_NO_TLSv1_1'

Don't worry. All you need to do is to run the following command:

    $ pip install Twisted==16.4.1

### Going for it!

Almost there! Start Faraday's server:

    $ cd faraday
    $ ./faraday-server.py

And in another terminal start the client runing:

    $ cd faraday
    $ ./faraday.py