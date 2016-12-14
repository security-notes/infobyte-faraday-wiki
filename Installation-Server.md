<a name="index"></a>
* [Faraday Server](#faraday-client)
* [Requirements](#requirements)
* [Commercial Versions](#commercial)
* [Community Version](#community)

<a name="faraday-server"></a>
### Faraday Server
Faraday Server is the way to have a better synchronization between your Faraday Client session and CouchDB. The server's responsibility is to send and receive information from both the client and CouchDB, and make sure that they are in sync. At the same time, it provides a much better performance for the Web UI, allowing it to handle enormous workspaces without a problem.

Once up, you can access Faraday's Web UI via the server: just go to `http://SERVER_IP:SERVER_PORT/_ui` in your favorite webbrowser.

<a name="requirements"></a>
### Requirements

Faraday Server is built with minimum requirements. This is by design, so you can install it even on the most bare-bones machine you can think of.

* Python 2.6.x or 2.7.x
* flask (>= 0.10.1)
* twisted (>= 16.1.1)
* sqlalchemy (>=1.0.12)
* pyopenssl (>16.0.0)

In addition, the commercial versions need:

* python-docx (>=0.8.5)
* docxtpl  (>=0.2.2)
* six (>=1.10.0)
* matplotlib  (>=1.4.3)

<a name="commercial"></a>
### Commercial Version (Professional & Corporate)

Installing Faraday Server commercial version is extremely simple. You should only keep in mind that you should install the server on the same machine you will install the CouchDB database.

Just go to the Faraday directory and run the following. Be aware that the first command should be run as root, the second one can be run as a normal user.
```
# ./setup_server.sh
```

After the setup script is done, [configure the CouchDB credentials](https://github.com/infobyte/faraday/wiki/First-steps#setup), run this to fire up the server 
```
$ ./faraday-server.pyc
```

If Faraday Server needs dependencies, it will give you the option to install them.

<a name="community"></a>
### Community Version

The installation of the community version is even more simple, as the features found on the commercial versions require more dependencies. You should still mind that the server in installed on the same machine you will have your CouchDB on.

Go to your Faraday directory and run.
```
$ ./faraday-server.py
```

If you are missing libraries, install them.
