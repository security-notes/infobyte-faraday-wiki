* Go to the folder: /etc/systemd/system/
* Create a unit file named ‘faraday.service’ and write in it the following lines:

```
[Unit]
Description=Faraday
After=postgresql.service
[Service]
User=YOUR_SYSTEM_USER
Type=simple
ExecStart=/usr/bin/python /path/to/faraday/faraday-server.pyc --nodeps
Restart=always
[Install]
WantedBy=default.target
```
_Note that the paths are defined by the location of Python and the location of the Faraday's server script._

* Enable Faraday's and PostgreSQL's unit files:
```
    $ sudo systemctl daemon-reload
    $ sudo systemctl enable postgresql.service
    $ sudo systemctl enable faraday.service
```
* Reboot your computer and you should be able to open Faraday’s Web UI right after boot.
