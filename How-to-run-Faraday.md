<a name="index"></a>
* [Run Faraday Server](#run-faraday-server)
* [Run binary files](#run-binary-files)
* [Connect to Faraday Server from a remote machine](#run-faraday-remote)

<a name="run-faraday-server"></a>
### Run Faraday Server

You can now run Faraday Server as a service:

```
    $ systemctl start faraday-server
```

<a name="run-binary-files"></a>
### Run binary files

You can run Faraday Client, Faraday Manage and Faraday Plugin (fplugin) by using their binary files:
 
* To run Faraday Client:

    ```
    $ faraday-client
    ```

* To run Faraday Manage:

    ```
    $ faraday-manage
    ```

* To run Faraday Plugin:

    ```
    $ faraday-fplugin
    ```

<a name="run-faraday-remote"></a>
### Connect to Faraday Server from a remote machine

In order to connect to Faraday Server from a remote machine, you should follow this instructions:

* Go into the folder `/home/faraday/.faraday/config/`
* Open the file `server.ini`
* In the section **[faraday_server]**, change the value of **bind_address** to 0.0.0.0. It should be defined like this:

    ```
    bind_address = 0.0.0.0
    ```

* Save the file and restart Faraday server by running:

    ```
    $ systemctl restart faraday-server
    ```

Now you should be able to connect to Faraday from a remote machine.
