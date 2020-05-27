## OSX

If you want to use Faraday in OSX [please check this guide]()

Video about install Faraday in macOS Sierra: [Installation in macOS Sierra.](https://www.youtube.com/watch?v=F44RnB3Ru24)

Tested on OSX Maverick 10.9.2.

### Installing Xcode

Go to AppStore and install Xcode. If you run `brew install` first, it'll ask to install Xcode too.

![](https://raw.github.com/wiki/infobyte/faraday/images/installation/xcode.png)

Keep in mind that Xcode is 2+ Gb so it can take a while to download. After this is done go to **Preferences** and install command line tools or open a terminal console and run:

    $ xcode-select --install

A dialog box will appear asking to install additional tools as shown in the image below. Click install.

![](https://raw.github.com/wiki/infobyte/faraday/images/installation/confirm.png)

**Important!** Before proceeding with the rest of this guide you need to **open Xcode at least once** in order to accept the License Agreement. Please make sure you do that or else some of the dependencies will fail to install.

### Installing Brew

To install [Brew](http://brew.sh) run:


    $ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

### Installing Python & PIP

In order to install Python run the following command:

    $ brew install python

Important:

* Remember never to run brew as root.
* Installing Python through brew, will also install PIP.
* You can find more info about Python in OSX following this [link](http://docs.python-guide.org/en/latest/starting/install/osx/).

#### Setting Python interpreter
Make sure that you are using the Python interpreter that brew installed and not the one shipped with the OS.

To know which Python you are using, execute the following command:

    $ which python

Th should return:

    /usr/local/bin/python

If this is not the case, you can change the PATH and use `/usr/local/bin` by running this command:

    $ ln -s /usr/local/bin/python3 /usr/local/bin/python

If you want to revert this change just delete the link executed in the previous command.

### Downloading Faraday

#### Community version

First of all, we need Git in order to get Faraday from Github. Run:

    $ brew install git

Now clone Faraday's repository by running the following command:

    $ git clone --depth 1 https://github.com/infobyte/faraday.git faraday-dev

Done!

#### Professional and Corporate versions

After the purchase you will receive an email with your credentials and a link to our **Customers Portal**. Use those credentials to log in to the site and you will get two links:

* Download License - this is the tarball for the **Faraday License**
* Download Faraday - this is the tarball for the actual **Faraday Code**

Download both those packages and then:

1. Create a new directory and unpack the **Faraday tarball** there. For example, `/home/user/Infobyte/faraday`.

1. Unpack the **License Package** and place its contents in the `doc` directory. For example, using the path from **Step 1**, you should place the **License files** in `/home/user/Infobyte/faraday/doc`.

Done! 

### Installing Faraday's dependencies and other Python libraries via PIP

Installing Python via brew will also install PIP. Now we need to use PIP in order to install Faraday's requirements. Get into the folder _/faraday_ and run the following commands:

    $ pip2 install -r requirements_server.txt -U
    $ pip2 install -r requirements.txt -U

If you have issues building psycopg2:

    $ brew install postgresql
    $ pip install psycopg2


#### Installing Faraday GTK dependencies

We need a few other packages from brew before we can use the client:

    $ brew install vte3 
    $ brew install pygobject3 --with-python@2

#### Installing ZSH and curl

Faraday needs [ZSH](http://www.zsh.org/) and _curl_ in order to be able to connect to the server. In order to install them, run:

    $ brew install zsh curl

### Going for it!

#### Initializing PostgreSQL

In order to initialize PostgreSQL database, generate your main _user_ and a __password__ and import your data from CouchDB (if it's the case), run the following command:

```
$ faraday-manage initdb
```
If you don't have CouchDB configured we assume this is a new installation, so a
new user will be created.

With CouchDB configured in the `server.ini` file, it will import all the data
you had from the 2.7.2 version, including the users and its hashed passwords. 

If you want to manually import the data from CouchDB, follow this [step](https://github.com/infobyte/faraday/wiki/Installation-Corp/_edit#importing-from-couchdb)

Keep in mind the following items:

* This commmand must be executed only when you run Faraday for the first time. 
* If at the moment you run this command, it throws an error, be sure you have sudo installed. Once you have installed it, run the command again.
* If you can't login into to Faraday after running the command above due to invalid credentials, you can change your password through the PostgreSQL shell that Faraday has in it. Follow the next [instructions](https://github.com/infobyte/faraday/wiki/Troubleshooting#cant-login-after-importing-from-couch) in order to change your password and be able to login.
* You should have the PostgreSQL service started. To start it, run this command:

    $ brew services start postgresql


#### Manual PostgreSQL configuration

If you need an advance configuration of the postgres database, like having a
custom database name or run it in a separate host, the `python manage.pyc initdb`
command probably won't be enough for you, so you should configure it manually
by doing something like this:

```
psql -c "CREATE ROLE faraday_postgresql WITH LOGIN PASSWORD 'YOURPASSWORD'"
createdb -O faraday_postgresql faraday
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
$ faraday-manage import-from-couchdb
```
***Note:*** beware of the number of users you have created in CouchDB, remember that you have already created one when you initialized PostgreSQL. The number of users that you have between CouchDB and PostgreSQL should not surpass the number of users you're allow to have according to your license.


### Starting Faraday's server:

Inside the folder _/faraday_, run the following command:

    $ faraday-server

### Starting Faraday's Client:

**Note:** in order to run the Client, Faraday's server must be running.

#### Running the Client with GUI:

Inside the folder _/faraday_, run:

    $ faraday-client

#### Running the Client without GUI

Inside the folder _/faraday_, run:
 
    $ faraday-client --gui=nogui

Now in another terminal and inside the same folder as above, run:
 
    $ ./faraday-terminal.zsh


We are done. Enjoy Faraday!
