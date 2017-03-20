#### Beware! Faraday doesn't support CouchDB 2.0, use CouchDB 1.6!

<a name="faraday-server"></a>
### Faraday Server
Faraday Server is the way to have a better synchronization between your Faraday Client session and CouchDB. The server's responsibility is to send and receive information from both the client and CouchDB, and make sure that they are both in sync. At the same time, it provides much better performance to the Web UI, allowing it to handle enormous workspaces without a problem.

**NOTE:** You should keep in mind that the Faraday server must be installed on the same machine as CouchDB.

## Downloading Faraday

Download the [latest tarball](https://github.com/infobyte/faraday/tarball/master) or clone the [Faraday Git Project](https://github.com/infobyte/faraday repository):

    $ git clone https://github.com/infobyte/faraday.git faraday-dev
    $ cd faraday-dev

## Requirements

Faraday Server is built with minimum requirements. This is by design, so you can install it even on the most bare-bones machine you can think of.

The Python requirements for the server are stored in the [`requirements_server.txt` file](https://github.com/infobyte/faraday/blob/master/requirements_server.txt).

| Dependency | Version |
|---|
| CouchDB | 1.6 |
| Python | 2.6 or 2.7 |
| flask | >= 0.10.1 |
| twisted | >= 16.1.1 |
| sqlalchemy | >=1.0.12 |
| pyopenssl | >16.0.0 |
| couchdbkit | >=0.6.5 |
| restkit | >=4.2.2 |
| requests | >=2.10.0 |
| flask | >=0.10.1 |
| twisted | >=16.1.1 |
| sqlalchemy | >=1.0.12 |
| pyopenssl | >=16.0.0 |
| service_identity | >=16.0.0 |

In addition, the **commercial** versions also needs:

| Dependency | Version |
|---|
| CouchDB | 1.6 |
| python-docx | >=0.8.5 |
| docxtpl | >=0.2.2 |
| six | >=1.10.0|
| matplotlib |>=1.4.3 |

## Installing system dependencies

#### Debian based distributions (Debian, Ubuntu, Backtrack, etc)

You can run the following command to install the required dependencies on any Debian based distribution.

    $ sudo apt-get update
    $ sudo apt-get install build-essential ipython python-setuptools \
                    python-pip python-dev libssl-dev libffi-dev couchdb

#### Others

Please consult with your distribution documentation to install the dependencies listed above.

## Installing Python 2 dependencies

Once you have the required system dependencies, you just have to install the Python modules needed to run the server using `pip`:

    $ pip2 install -r requirements_server.txt

## Commercial Version (Professional & Corporate)

The commercial version of Faraday needs an extra set of steps and installed dependencies to ensure that every additional feature will work as expected.

#### Debian based distributions (Debian, Ubuntu, Backtrack, etc)

You can run the following command to install the required dependencies on any Debian based distribution.

    $ sudo apt-get install pkg-config libssl-dev libffi-dev libxml2-dev libxslt1-dev libfreetype6-dev libpng12-dev

#### Kali Linux

If you are running Kali, please run the following command instead:

    $ sudo apt-get install pkg-config libssl-dev libffi-dev libxml2-dev libxslt1-dev libfreetype6-dev libpng-dev

#### Others

Please consult with your distribution documentation to install the dependencies listed above.

### Commercial Server Configuration

Once you have installed the additional dependencies, you will need to execute the setup script, which will create the admin user with the configured password, and create a backup cronjob for CouchDB. Just execute the following command and answer the questions asked.

    $ sudo ./setup-server.py/

If you want more fine grained control over what the setup script does, you can see the available options by executing:

    $ ./setup-server.py --help

## Running Faraday Server

Once everything is installed, you can proceed to run the Faraday Server script:

    $ ./faraday-server.py

Depending on whether it's the first time running it, if you are using the community or commercial version, or if you just upgraded Faraday, it is possible that you may need to answer some questions before the server can start answering requests from the clients.

For example, if you are running the commercial version for the first time, you will be asked to create an admin user, and to set up a backup cron job.

## Web UI

Once the server is running, you can access Faraday's Web UI using any browser: just point it to `http://SERVER_IP:SERVER_PORT/_ui` and you can start playing with Faraday.

## Next steps

To install and run a Faraday Client, please proceed to the next step of the documentation.
