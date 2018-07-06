In ```$FARADAY/helpers``` you can find several scripts developed to help you load and manage Faraday data. None of them are included as part of the Faraday core, and using them can usually mean deleting content from the database in a permanent way, so **be careful when executing any of them and always make sure to have a fresh backup**.

<a name="cfdbToCsv"></a>
### cfdbToCsv.py

This script allows you, create a CSV file with Vulnerability templates, based in Cfdb open source project.
Read more about it [here](https://github.com/infobyte/faraday/wiki/Vulnerabilities-Database).

<a name="vulndbToCsv"></a>
### vulndbToCsv.py

This script allows you, create a CSV file with Vulnerability templates, based in Vulndb open source project.
Read more about it [here](https://github.com/infobyte/faraday/wiki/Vulnerabilities-Database).

<a name="cleanXML"></a>
### cleanXML.py

```
$ python helpers/cleanXML.py --help
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

To install BeautifulSoup you can use the [`requirements_extras.txt` file](https://github.com/infobyte/faraday/blob/master/requirements_extras.txt).
