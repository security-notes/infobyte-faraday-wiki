* Create a script named ‘docker.sh’ wherever you want.
* Write the following lines in this script:

```
    #! /usr/bin/env bash
    /usr/bin/docker start couchdb_faraday
```

* Run the following command to make the script executable:

    `$ sudo chmod +x example.sh`

* In order to be able to run the script, you have to be able to run docker as a non-root user. For this you need to create a Unix group and add your user to it. To do so, follow the next steps: 
	
    - Create a Unix group called docker.
        
        ```$ sudo groupadd docker```
    - Add your user to this group.
    
        ```$ sudo usermod -aG docker $USER```

    - Log out and log back. If you’re working on a virtual machine, it may be necessary to restart the virtual machine.

    More information: https://docs.docker.com/install/linux/linux-postinstall/#manage-docker-as-a-non-root-user

* Now, go to the folder: /etc/systemd/system/
* Create a unit file named ‘couchdb.service’ and write in it the following lines:

``` 
[Unit]
Description=CouchDB
After=docker.service
[Service]
Type=simple
ExecStart=/path/to/docker.sh
[Install]
WantedBy=default.target
```

* In that same folder, create another unit file named ‘faraday.service’ and write in it the following lines:

```
[Unit]
Description=Faraday
After=couchdb.service
[Service]
User=$USER
Type=simple
ExecStart=/path/to/faraday/faraday-server.py --nodeps
Restart=always
[Install]
WantedBy=default.target
```

* Enable these unit files.

```
    $ sudo systemctl daemon-reload
    $ sudo systemctl enable couchdb.service
    $ sudo systemctl enable faraday.service
```
* Reboot your computer and you should be able to open CouchDB and Faraday’s Web UI right after boot.
