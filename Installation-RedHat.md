## Redhat 6
![](https://raw.githubusercontent.com/wiki/infobyte/faraday/images/faraday_redhat.jpeg)
### Docker
Install Docker using EPEL, go to the terminal and run this command-lines.

    $  wget https://dl.fedoraproject.org/pub/epel/epel-release-latest-6.noarch.rpm

    $  rpm -ivh epel-release-latest-6.noarch.rpm

Create a folder _docker_ with two sub-folders: 

   1. _etc_
   2. _dbs_

Now you'll need the paths of those folders for the next command.

   $ docker run --name couchdb_faraday -v /path/to/couchdb/conf:/usr/local/etc/couchdb/local.d -v /path/to/couchdb/data:/usr/local/var/lib/couchdb -p 5984:5984 -d couchdb:1.7.1




***
You'll need to have your RedHat's official credentials for the next step
***

   $  subscription-manager repos --enable=rhel-server-rhscl-6-rpms

   $  subscription-manager repos --enable=rhel-6-server-optional-rpms

### System Dependencies 

It's time to install some system dependencies Faraday needs!

    $  yum install gcc libffi-devel openssl-devel python27-python python27-python-devel libxml2-devel libxslt-devel 

    $  freetype-devel libpng-devel
  
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


