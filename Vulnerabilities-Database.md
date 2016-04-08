Find yourself writing the same descriptions over and over again? Tired of typos coming up in your reports? Faraday provides a simple solution; unify criteria for naming vulnerabilities and save time and effort to yourself and your team.

Faraday comes with its own [CWE](https://cwe.mitre.org/) Vulnerabilities DB for you to use. This is a simple **CSV** made using open source proyects based in the **CWE standard** and allows you to create vulnerabilities without worrying about finding references, description, etc.

You prefer a video about this feature? [Vulnerability Database](https://www.youtube.com/watch?v=o5uSS6yzvCo)

### Creating a CSV to upload to CouchDB

Faraday have a CSV of the original Mitre proyect, if you want import to Faraday this, jump to execution of pushCWE.py 

For create a CSV with all information about a specific proyect, you need run a script for download and parse this.
Faraday have two scripts for two different proyects.

[CFDB](https://github.com/mubix/cfdb):

[Faraday_Installation]/helpers/cfdbToCsv.py

[VulnDb](https://github.com/vulndb/data)

[Faraday_Installation]/helpers/vulndbToCsv.py

Go to directory helpers and execute one of this scripts for create a CSV file.
Next copy this CSV(cfdb.csv or vulndb.csv) to [Faraday_Installation]/data/cwe.csv

To upload it to CouchDB go to your Faraday installation root directory and run 

```
python helpers/pushCwe.py
```

Use the paramater '-c- if you have a username and password for Faraday.
Example:
pushCwe.py -c 'http://USERNAME:PASSWORD@HOSTNAME:PORT/'

Also, if you need add your own CSV file, put the CSV inside **$FARADAY/data/cwe.csv**.
And run pushCWE.py!

Make sure you run the **pushCwe.py** script before use and that's it!

### Usage

Login to your Faraday Web UI and create or edit a vulnerability , you can see now a field 'CWE' how show image...
![](https://raw.githubusercontent.com/wiki/infobyte/faraday/images/CweDb.png)

Write the CWE name of this vulnerability and all the information would loaded!
Note: Name, Description and Resolution is replaced by contains in the CWE database.
