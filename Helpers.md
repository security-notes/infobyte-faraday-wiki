In ```$FARADAY/helpers``` you can find several scripts developed to help you load and manage Faraday data. None of them are included as part of the Faraday core, and using them can usually mean deleting content from the database in a permanent way, so be careful when executing any of them and always make sure to have a fresh backup.

<a name="pushCwe"></a>
### pushCwe.py

```
usage: pushCwe [-h] [-c COUCHDB]

optional arguments:
  -h, --help            show this help message and exit
  -c COUCHDB, --couchdburi COUCHDB
                        Couchdb URL (default http://127.0.0.1:5984)

Example: ./pushCwe.py
```

This script allows you to upload your Vulnerability templates database to CouchDB. Read more about it [here](https://github.com/infobyte/faraday/wiki/Vulnerabilities-Database).

<a name="cfdbToCsv"></a>
### cfdbToCsv.py

<a name="vulndbToCsv"></a>
### vulndbToCsv.py

<a name="cleanXML"></a>
### cleanXML.py

```
usage: cleanXML [-h] -i INFILE [-o OUTFILE]

optional arguments:
  -h, --help            show this help message and exit
  -i INFILE, --input INFILE
                        XML File to read from
  -o OUTFILE, --output OUTFILE
                        Filename to write output

Example: ./cleanXML.py
```

Some tools are known for creating invalid XML output files which tend to be hard to fix by hand. If you want a quick way to patch an XML to feed it to Faraday for processing, this script is your best friend. Run it like this (make sure to have [BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/bs4/doc/)):

```
python $FARADAY/helpers/cleanXML.py broken_file.xml
```

<a name="removeBySeverity"></a>
### removeBySeverity.py

```
usage: removeBySeverity [-h] [-c COUCHDB] -d DB -s SEVERITY [-t] [-v]

optional arguments:
  -h, --help            show this help message and exit
  -c COUCHDB, --couchdburi COUCHDB
                        Couchdb URL as
                        http://user:password@couch_ip:couch_port (defaults to
                        http://127.0.0.1:5984)
  -d DB, --db DB        DB to process
  -s SEVERITY, --severity SEVERITY
                        Vulnerability severity
  -t, --test            Dry run, does everything except updating the DB
  -v, --verbose         Extended output

Example: ./removeBySeverity.py
```

Read more about it [here](https://github.com/infobyte/faraday/wiki/troubleshooting).