This is a guide to Install Faraday in  RedHat OS.

Install Docker, using EPEL:

`wget https://dl.fedoraproject.org/pub/epel/epel-release-latest-6.noarch.rpm`

`rpm -ivh epel-release-latest-6.noarch.rpm`

Create a folder docker with two subfolders: etc and dbs. Use those paths in the next command.

` sudo docker run --name couchdb_Faraday -v /home/USER/docker/etc/:/usr/local/etc/couchdb/local.d -v /home/USER/docker/dbs/:/usr/local/var/lib/couchdb -d -p 5984:5984 couchdb`

To do the following step you need to have your RedHat official credencial.

 `subscription-manager repos --enable=rhel-server-rhscl-6-rpms`


 `subscription-manager repos --enable=rhel-6-server-optional-rpms`

Install some system dependencies: 

 `yum install gcc libffi-devel openssl-devel python27-python python27-python-devel libxml2-devel libxslt-devel `
`freetype-devel libpng-devel`

`scl enable python27 bash`

` yum install -y python-pip`

 `pip install --upgrade pip`

Install python requirements:

`pip install -r requirements_server.txt`

`pip install -r requirements.txt`

Final step! Run the server:

`python faraday-server.py (first run to install missing dependencies)`


