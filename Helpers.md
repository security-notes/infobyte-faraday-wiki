In ```$FARADAY/helpers``` you can find several scripts developed to help you load and manage Faraday data. None of them are included as part of the Faraday core, and using them can usually mean deleting content from the database in a permanent way, so be careful when executing any of them and always make sure to have a fresh backup.

### pushCwe.py

This script allows you to upload your Vulnerability templates database to CouchDB. Read more about it [here](https://github.com/infobyte/faraday/wiki/Vulnerabilities-Database).

```
usage: pushCwe [-h] [-c COUCHDB]

optional arguments:
  -h, --help            show this help message and exit
  -c COUCHDB, --couchdburi COUCHDB
                        Couchdb URL (default http://127.0.0.1:5984)

Example: ./pushCwe.py
```

### cfdbToCsv.py
### vulndbToCsv.py
### cleanXML.py

Some tools are known for creating invalid XML output files which tend to be hard to fix by hand. If you want a quick way to patch an XML to feed it to Faraday for processing, this script is your best friend.

Read more about it [here](https://github.com/infobyte/faraday/wiki/troubleshooting#import).

### removeBySeverity.py

Read more about it [here](https://github.com/infobyte/faraday/wiki/troubleshooting).