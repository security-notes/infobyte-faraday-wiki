To view a full list of findings you can access the Status Report.

![](https://raw.githubusercontent.com/wiki/infobyte/faraday/images/status_report/status_report.png)

The Status Report provides several options including vulnerability search, filtering and management.

Personalize this view by clicking on the blue buttons to select the columns you wish to see, and remove the ones you don't need with the X's in the table. These changes will be persisted in your browser from session to session, so you only have to apply them once.

### Vulnerability Creation
To create vulnerabilities manually, you can go to the status report page and click the "New" button at the top left corner. You should see a dialog similar to this:

![](https://raw.githubusercontent.com/wiki/infobyte/faraday/images/status_report/new_vuln.png)

The image above shows the tab **Hosts** that allows you to select the target of your vulnerability. To specify the name and description of your vulnerability, you can click on the second tab named **General**

![](https://raw.githubusercontent.com/wiki/infobyte/faraday/images/status_report/new_vuln_general.png)

You also have another tabs in order to add more information to your vulnerability:

* **Technical Details**: allows you to add the field _data_ to your vulnerability. If you create a web vulnerability, you will have more fields available such as path, method, request, response and so on.

* **Evidence**: allows you to add an evidence to the vulnerability. It can be an PNG or JPC image.

* **Custom Fields**: allows you to add information to a field that you have created. For more information about Custom Fields, you can check its [wiki page](https://github.com/infobyte/faraday/wiki/Custom-Fields)

Make sure you select a host (and a service if the vulnerability applies to it), a name and a description. **These fields are mandatory to create a vulnerability**.

#### Faraday Professional & Corporate - [Commercial versions](https://www.faradaysec.com/?utm_source=github#download)

This version includes advanced visualizations, tags, pentest comparison, pentester ranking among others.

### Vulnerability Edition
You can edit the vulnerabilities that you have created. You have multiple ways to edit them:

#### Edit vulnerability from vuln preview
You can see a preview of the vulnerability by click on the vuln's name. From here you can edit your vulnerability and it will saved automatically.

![](https://raw.githubusercontent.com/wiki/infobyte/faraday/images/status_report/vuln_preview.png)

As you can see in the image above, there is a new tab named **Comments** where you can leave comments and mention other users to notify them about important events in real time. For more information about Comments, you can check its [wiki page](https://github.com/infobyte/faraday/wiki/Comments)

#### Edit vulnerability from modal
You can click on the Edit button (next to the New button) to open the edit modal:

![](https://raw.githubusercontent.com/wiki/infobyte/faraday/images/status_report/edit_vuln.png)

#### Edit multiple vulnerabilities at once
You can edit multiple vulnerabilities with just one click. Next to the edit button, you will find arrow that will show a dropdown with the multiple values that you can edit at once:

![](https://raw.githubusercontent.com/wiki/infobyte/faraday/images/status_report/edit_multiple_vulns.png)

### Vulnerability Search and Filter
Status Report allows you to filter vulnerabilities so you can have a better workflow. In order to check how the search field works, you can check this [wiki page](https://github.com/infobyte/faraday/wiki/Search-and-Filter)

### Upload a report
You can upload a scan report of your favorite tool to Faraday and have a nice look of your findings through the Status Report. You can see a list of the tools that Faraday supports by clicking on this [link](https://github.com/infobyte/faraday/wiki/Plugin-List#list).

In order to upload a report to Faraday, follow this instructions:

* Click on the button that has a cloud shape:  ![](https://raw.github.com/wiki/infobyte/faraday/images/status_report/upload_report.png)
* Click on **Select File** in order to select the report that you are going to upload.
* Once you have selected the report, click on **Upload File** and your file will be uploaded.