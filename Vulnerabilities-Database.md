Find yourself writing the same descriptions over and over again? Tired of typos coming up in your reports? Faraday provides a simple solution; unify criteria for naming vulnerabilities and save time and effort to yourself and your team.

Faraday Server comes with its own [CWE](https://cwe.mitre.org/) Vulnerabilities DB for you to use. This is a simple **CSV** made using Open Source projects based in the **CWE standard** and allows you to create vulnerabilities without worrying about finding references, description, etc.

Tired of reading documentation? We have a [video showing how to upload the DBs](https://www.youtube.com/watch?v=o5uSS6yzvCo).

### Creating a CSV to upload to CouchDB

Faraday has a CSV of the original Mitre project included in its tree, [click here](#pushcwe) for instructions on how to upload it.

To create a CSV with all information about a specific project, you need run a script to download and parse its content.
Faraday have two scripts for two different projects. Here we show how to run them in order to download and store the CSV files.

#### [CFDB](https://github.com/mubix/cfdb) ([cfdbToCsv.py](/helpers/cfdbToCsv.py)):

    $ ./helpers/cfdbToCsv.py

#### [VulnDb](https://github.com/vulndb/data) ([/helpers/vulndbToCsv.py](vulndbToCsv.py)):

    $ ./helpers/vulndbToCsv.py

Next copy this CSV file (either cfdb.csv or vulndb.csv) to [/data/cwe.csv](data/cwe.csv).

<a name="pushcwe"></a>
To upload it to CouchDB go to your Faraday Server installation root directory and run:

    $ ./helpers/pushCwe.py

Use the paramater `-c` if you have a username and password for Faraday.

    $ ./pushCwe.py -c 'http://USERNAME:PASSWORD@HOSTNAME:PORT/'

Also, if you need add your own CSV file, put the CSV inside `$FARADAY/data/cwe.csv`. And run pushCWE.py!

Make sure you run the `pushCwe.py` script before use and that's it!

### Usage

Login to your Faraday Web UI and create or edit a vulnerability, you can see now a field `CWE` like in the followig screenshot:

![](https://raw.githubusercontent.com/wiki/infobyte/faraday/images/CweDb.png)

Write the CWE name of this vulnerability and all the information will be automatically loaded!

**Note:** Name, Description and Resolution fields are replaced with the information stored in the CWE database.
