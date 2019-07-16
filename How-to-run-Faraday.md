### Index
<a name="index"></a>
* [Run Faraday Server](#run-faraday-server)
* [Run Faraday's commands and binary files](#run-binary-files)
* [Connect to Faraday Server from a remote machine](#run-faraday-remote)

<a name="run-faraday-server"></a>
### Run Faraday Server

You can now run Faraday Server as a service:

```
    $ systemctl start faraday-server
```

<a name="run-binary-files"></a>
### Run Faraday's commands and binary files

Faraday's commands and Faraday's binary files work almost the same way. The difference is the way you run them. Keep in mind that the binary files are executable files. Here's an example of how to run a command and a binary file: 

* To run a command:

`$ faraday-client`

* To run a binary file:

`$ ./faraday-client`

Faraday's commands are installed at the moment you install Faraday using the **.deb** or the **.rpm** installer, while the Faraday's binary files must be downloaded. For more information, check our [installation guide](https://github.com/infobyte/faraday/wiki/Installation-Guide).

To keep this guide short and clear, we will show you Faraday's current commands but remember that the binary files work the same way:
 
* **Faraday Client**

    Faraday Client is the software which will allow you to work with your favorite security tools and capture their output in an organized manner. For more information about Faraday Client, take a look at this [wiki](https://github.com/infobyte/faraday/wiki/GTK).

    To run Faraday Client command, execute the following command:
    ```
    $ faraday-client
    ```

* **Faraday ZSH Terminal**

    You can run Faraday in detached mode connecting with a ZSH terminal to it. For more information, take a look at this [wiki](https://github.com/infobyte/faraday/wiki/ZSH).

    To run Faraday ZSH Terminal command, follow this instruction:

    * First, you need to run first Faraday Client without GUI:

        ```
        $ faraday-client --gui=no-gui
        ```

    * Once you run the command above, you can run Faraday ZSH Terminal:

        ```
        $ faraday-terminal
        ```

* **Faraday Manage**

    Faraday Manage is a backend tool that gives us a hand with Faraday's configuration. For more information, take a look at this [wiki](https://github.com/infobyte/faraday/wiki/Faraday-Manage).
    
    To run Faraday Manage command, execute the following command:

    ```
    $ faraday-manage
    ```

* **Faraday Plugin**

    Faraday Plugin (fplugin) allows you to interact directly with our Python API from the command line. For more information, take a look at this [wiki](https://github.com/infobyte/faraday/wiki/Faraday-Plugin).

    To run Faraday Plugin command, execute the following command:

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
