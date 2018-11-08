## OSX

Video about install Faraday in macOS Sierra: [Installation in macOS Sierra.](https://www.youtube.com/watch?v=F44RnB3Ru24)

Tested on OSX Maverick 10.9.2.

### Xcode

Go to AppStore and install Xcode. If you run `brew install` first, it'll ask to install Xcode too.

![](https://raw.github.com/wiki/infobyte/faraday/images/installation/xcode.png)

Keep in mind that Xcode is 2+ Gb so it can take a while to download. After this is done go to **Preferences** and install command line tools or open a terminal console and run:

    $ xcode-select --install

A dialog box will appear asking to install additional tools as shown in the image below. Click install.

![](https://raw.github.com/wiki/infobyte/faraday/images/installation/confirm.png)

**Important!** Before proceeding with the rest of this guide you need to **open Xcode at least once** in order to accept the License Agreement. Please make sure you do that or else some of the dependencies will fail to install.

### Brew

To install [Brew](http://brew.sh) run:


    $ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

### Install Python & PIP

Run:

    $ brew install python

Remember never to run brew as root.

More info about [Python in OSX](http://docs.python-guide.org/en/latest/starting/install/osx/).

*Important* Make sure that you are using the python interpreter that brew installed and not the one shipped with the OS.
To know which python you are using execute:

    $ which python

it should return:

    $ /usr/local/bin/python

If this is not the case you can change the PATH to use the /usr/local/bin:

    $ ln -s /usr/local/bin/python2 /usr/local/bin/python

If you want to revert this change just delete the link executed in the previous command.

### Git

We need Git in order to get Faraday from Github. Run:

    $ brew install git

### Faraday
This is the code for our Community edition. 
Here you have the steps to get the source code for our [ Professional](https://github.com/infobyte/faraday/wiki/Installation-Pro#downloading) and [Corporate](https://github.com/infobyte/faraday/wiki/Installation-Corp#downloading) editions.

Run:

    $ git clone https://github.com/infobyte/faraday.git faraday-dev

### Dependencies and other Python libraries via PIP

Installing Python via brew will also install pip. Now we need to use pip to install the requirements:

`pip install -r requirements.txt`

If you have issues building psycopg2:

    $ brew install postgresql
    $ pip install psycopg2


### GTK

We need a few other packages from brew before you can use the client:

    $ brew install vte3 
    $ brew install pygobject3 --with-python@2

### ZSH

Faraday needs [ZSH](http://www.zsh.org/) and curl to connect to the server. To install it run:

    $ brew install zsh curl

### Going for it!

#### Initializing PostgreSQL

In order to initialize PostgreSQL database, generate your main _user_ and a __password__ and import your data from CouchDB (if it's the case), run the following command:

```
$ python manage.pyc initdb
```
If you don't have CouchDB configured we assume this is a new installation, so a
new user will be created.

With CouchDB configured in the `server.ini` file, it will import all the data
you had from the 2.7.2 version, including the users and its hashed passwords. 

If you want to manually import the data from CouchDB, follow this [step](https://github.com/infobyte/faraday/wiki/Installation-Corp/_edit#importing-from-couchdb)

Keep in mind the following items:

* This commmand must be executed only when you run Faraday for the first time. 
* If you can't login into to Faraday after running the command above due to invalid credentials, you can change your password through the PostgreSQL shell that Faraday has in it. Follow the next [instructions](https://github.com/infobyte/faraday/wiki/Troubleshooting#cant-login-after-importing-from-couch) in order to change your password and be able to login.

* You should have the PostgreSQL service started. To do it run
`systemctl start postgresql` or the equivalent command for your GNU/Linux
distro.

*  If at the moment you run this command, it throws an error, be sure
you have sudo installed. Once you have installed it, run the command again.

#### Manual PostgreSQL configuration

If you need an advance configuration of the postgres database, like having a
custom database name or run it in a separate host, the `python manage.pyc initdb`
command probably won't be enough for you, so you should configure it manually
by doing something like this:

```
sudo -u postgres psql -c "CREATE ROLE faraday_postgresql WITH LOGIN PASSWORD 'YOURPASSWORD'"
sudo -u postgres createdb -O faraday_postgresql faraday
```

Then, edit the `~/.faraday/config/server.ini` by adding the connection string
to the database:

```
[database]
connection_string = postgresql+psycopg2://faraday_postgresql:YOURPASSWORD@localhost/faraday
```

Then you should run `python manage.pyc create-tables` to create all the required
tables to make Faraday work, and `python manage.pyc createsuperuser` to create an
admin user.


#### Manually importing from CouchDB

If you were using Faraday 2.7.2 and setup the database manually instead of
using the `python manage.pyc initdb`, you should run the following command to import
the data from CouchDB:

```
$ python manage.pyc import-from-couchdb
```
***Note:*** beware of the number of users you have created in CouchDB, remember that you have already created one when you initialized PostgreSQL. The number of users that you have between CouchDB and PostgreSQL should not surpass the number of users you're allow to have according to your license.


## Almost there! Start Faraday's server:

    $ cd faraday-dev
    $ ./faraday.py --gui=nogui

And in another terminal run:

    $ cd faraday-dev
    $ ./faraday-terminal.zsh
