## Intro
Find yourself writing the same descriptions over and over again? Tired of typos coming up in your reports? Faraday provides a simple solution; unify criteria for naming vulnerabilities and save time and effort to yourself and your team.

> Write vulns once and use them forever!

Faraday Server comes with its own [CWE](https://cwe.mitre.org/) Vulnerabilities DB for you to use. This is a simple **CSV** made using Open Source projects based in the **CWE standard** and allows you to create vulnerabilities without worrying about finding references, description, etc.

## Index

* [CSV](#csv)
* [Upload CSV File](#upload)
* [Manually Adding Templates](#manually)
* [Usage](#usage)

## Topics

<a name="csv"></a>
### CSV

Faraday ships with a **CSV of the original Mitre project** included in its tree in `data/cwe.csv`. However, we also ship two different scripts to generate CSVs for [**CFDB**](https://github.com/mubix/cfdb) and [**VulnDB**](https://github.com/vulndb/data). These scripts will download and parse the contents of those databases.

* CFDB
Execute the following command to get a CSV for CFDB

```
$ ./helpers/cfdbToCsv.py
```

* VulnDb
Execute the following command to get a CSV for VulnDB

```
$ ./helpers/vulndbToCsv.py
```

Next copy this CSV file (either cfdb.csv or vulndb.csv) to [/data/cwe.csv](data/cwe.csv).

<a name="upload"></a>
### Upload CSV file

#### Manual Import

Go to the **Web UI** and click on the **import** icon ![](https://raw.github.com/wiki/infobyte/faraday/images/faraday_vulntemplates_import_icon.png)

A modal dialog will pop up asking you to choose a CSV file to upload, select it, click **ok** and you're done!

#### Script

To upload the CSV to CouchDB using the script go to your Faraday Server installation root directory and run:

```
$ ./helpers/pushCwe.py
```

Use the paramater `-c` if you have a username and password for Faraday.

```        
$ ./pushCwe.py -c 'http://USERNAME:PASSWORD@HOSTNAME:PORT/'
```

Also, if you need add your own CSV file, put the CSV inside `$FARADAY/data/cwe.csv`. And run pushCWE. Make sure you run the `pushCwe.py` script before use and that's it!

<a name="manually"></a>
### Manually Adding Templates

You can also create templates manually in the Web UI. Click on the **vulnerability templates** icon ![](https://raw.github.com/wiki/infobyte/faraday/images/faraday_vulntemplates_icon.png)

You will get a list of the existing templates in your installation

![](https://raw.github.com/wiki/infobyte/faraday/images/faraday_vulntemplates_list.png)

<a name="usage"></a>
### Usage

Login to your Faraday Web UI and create or edit a vulnerability. A search field will allow you to find your templates, as shown in the picture below.

![](https://raw.githubusercontent.com/wiki/infobyte/faraday/images/faraday_statusreport_vuln_creation_templates_list.png)

**Note:** Name, Description and Resolution fields are replaced with the information stored in the templates database.
