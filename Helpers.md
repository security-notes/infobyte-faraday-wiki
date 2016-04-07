In ```$FARADAY/helpers``` you can find several scripts developed to help you load and manage Faraday data. None of them are included as part of the Faraday core, and using them can usually mean deleting content from the database in a permanent way, so be careful when executing any of them and always make sure to have a fresh backup.

### pushCwe.py

This script allows you to upload your Vulnerability templates database to CouchDB. Read more about it [here](https://github.com/infobyte/faraday/wiki/Vulnerabilities-Database).

### cfdbToCsv.py
### vulndbToCsv.py
### cleanXML.py
### fixBrokenChildren.py
### removeBySeverity.py
