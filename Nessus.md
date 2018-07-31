This plugin allows users to import scans done by the Tenable Nessus Vulnerability Scanner to the Faraday Workspace they are using.

We run the Nessus scan that we want to import to Faraday and we export it in XML format to our Faraday PATH.

![](https://raw.github.com/wiki/infobyte/faraday/images/faraday_nessus_plugin1.png)

In order to put the report in our Faraday path, we must copy the downloaded report to the following PATH.

`mv $HOME/Downloads/report.nessus $HOME/.faraday/uploaded_reports/myworkspace/report.nessus`

Faraday will process the output and load the vulnerabilities inside the Faraday Workspace.

![](https://raw.github.com/wiki/infobyte/faraday/images/faraday_nessus_plugin2.png)
