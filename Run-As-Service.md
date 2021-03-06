# Please Read!

After Faraday v3.8.0, Faraday's installers (.deb or .rpm) will install Faraday's server as a service, so the followings steps are **not** required anymore.
Please check our [new installation guide](https://github.com/infobyte/faraday/wiki/Installation-Guide)

For more information about how to run Faraday, you can check this [guide](https://github.com/infobyte/faraday/wiki/How-to-run-Faraday#run-faraday-server)

# DEPRECATED!

* Go to the folder: /etc/systemd/system/
* Create a unit file named ‘faraday.service’ and write in it the following lines:

```
[Unit]
Description=Faraday
After=postgresql.service
[Service]
User=YOUR_SYSTEM_USER
Type=simple
ExecStart=/usr/bin/python  /path/to/venv/bin/faraday-server/faraday-server
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
