Docker is great if you want to give Faraday community edition a try without actually installing it. In this guide you will find all you need to run Faraday in a Docker container.

If you already tried Faraday and you are ready to use it for real we strongly recommend that you install it in your host OS.

##### Starting up Faraday

Run:

    $ sudo docker run -t -i infobyte/faraday /root/run.sh

This command runs the container with Faraday using a test Workspace called "workspace". Inside, Faraday is started with `./faraday.py -gui=no-gui --update` which means without a graphic environment and checking for  updates.

Now to obtain the container's IP address run:

    $ docker inspect $(docker ps -lq) | grep \"IPAddress

For the purpose of this guide lets use `192.168.0.10`.

##### Web UI

Direct the browser to `http://192.168.0.10:5985/_ui/`

##### ZSH

    $ ssh root@192.168.0.10

    $ cd faraday/
    $ ./faraday-terminal.zsh

##### GTK GUI

In order to use this interface run:

    $ sudo docker run infobyte/faraday /root/run_service.sh

And now in a different console, get the IP address:

    $ sudo docker inspect $(docker ps -lq) | grep \"IPAddress

Again, for the purpose of this guide lets use `192.168.0.10`.

    # ssh -X root@192.168.0.10
    # cd faraday/
    # ./faraday.py

Keep in mind that all tools must be installed inside the Docker container in order to work.

##### Importing Reports

A different way to upload data into Faraday is importing a Report from other tools using a Plugin. Read more about [plugin types](https://github.com/infobyte/faraday/wiki/Plugin-List#types).

In order to do this copy the report to `$HOME/.faraday/report/[workspace_name]` replacing `[workspace_name]` with the name of your Workspace. Once it has been processed and incorporated to the database the report is copied to `$HOME/.faraday/report/[workspace_name]/process`.

We can do this by copying the reports to the containers via FTP or we can use a file sharing function between the host server and containers.

For example:

    # mkdir -p /tmp/workspace/process
    # cd /root/.faraday/report/workspace/
    # docker run -t -i -v /tmp/workspace/:/root/.faraday/report/workspace/ infobyte/faraday /root/run.sh

Now we can use the tools inside the host server and this is going to be interpreted as if it were inside the container for Faraday in the Workspace called "workspace".

To run `nmap`:

    # nmap localhost -xO /tmp/workspace/output_nmap.xml

Import a Report:

    # cp /root/reports/nessusscan.nessus /tmp/workspace/
