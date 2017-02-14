## Installing Faraday in Ubuntu

If you are using any version of Ubuntu, we have made `.deb` packages available which will automatically download all the needed dependencies and install Faraday on your system.

We have split the server and client into two separate packages, so you can install them separately, or even on different servers.

**Important:** Although you can install both packages using a Graphical Package Manager, like GDebi or Ubuntu Software Center, it is recommended to stick to this instructions, and install them from the command line.

Unfortunately, as Debian is missing a couple of dependencies for Faraday to work, this packages will not be able to be installed. Although it's still possible to do so by adding third party repositories, you will receive no support from us if you encounter any problem.

## Installing Faraday Server

To install the Faraday Server you have to execute the following commands:

    $ sudo dpkg -i faraday-server_<version>_all.deb
    $ sudo apt-get update
    $ sudo apt-get install -f

This will install the server, along with all the needed dependencies to run it.

If you are using a commercial version, a configuration dialog will be shown asking you to enter the CouchDB URL and the admin password:

![](https://raw.githubusercontent.com/wiki/infobyte/faraday/images/apt-configure-couch.png.png)

The package automatically creates the admin user in the configuration step, and installs the backup cronjob, so executing the setup script (`setup-server.py`) is not required.

There are two modes of execution explained below.

#### Running from the command line

This mode of execution introduces nothing new. You can simply execute `faraday-server` from any console or terminal and have the server running:

    $ faraday-server

#### Running as a system service

In this mode, we delegate the execution of the server to systemd, which will run it as a service. We can control it issuing the following commands:

    $ sudo systemctl start faraday-server

```
$ sudo systemctl status faraday-server
$ sudo systemctl status faraday-server
● faraday-server.service - Faraday Server
   Loaded: loaded (/lib/systemd/system/faraday-server.service; disabled; vendor preset: enabled)
   Active: active (running) since Thu 2017-02-09 11:58:02 ART; 18min ago
 Main PID: 22176 (python2.7)
    Tasks: 2
   Memory: 69.1M
      CPU: 1.229s
   CGroup: /system.slice/faraday-server.service
           └─22176 python2.7 /opt/faraday/server/faraday-server.py --nodeps

Feb 09 11:58:02 ubuntu-faraday systemd[1]: Started Faraday Server.
Feb 09 11:58:03 ubuntu-faraday faraday-server.py[22176]: 2017-02-09 11:58:03,049 - faraday-server.__main__ - INFO - Faraday Server is is ready
```

    $ sudo systemctl stop faraday-server

If we want faraday to be automatically started when the system boots, we can tell systemd to do so by executing the following command:

    $ sudo systemctl enable faraday-server

And we can undo this by executing:

    $ sudo systemctl disable faraday-server

**Note**: If you will be running Faraday Server as a service, please remember that all the configuration files will be stored under `/root/.faraday`

## Installing Faraday Client

Installing the client follows the same procedure as the server:

    $ sudo dpkg -i faraday-client_<version>_all.deb
    $ sudo apt-get update
    $ sudo apt-get install -f

This will install the client, along with all the needed dependencies to run it. You can then run it from any console or terminal:

    $ faraday

Or you can also search for it in your application menu.