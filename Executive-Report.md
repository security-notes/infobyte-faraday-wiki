**This feature is only available for our [commercial versions](https://www.faradaysec.com/#download).**
<a name="index"></a>
* [Intro](#intro)
* [Requirements](#requirements)
* [Managing Executive Reports](#managing-executive-reports)
* [Making a Report](#making-a-report)
* [Eliminating a Report](#eliminating-a-report)
* [Templates](#templates)


### Intro

The Executive Reports lets you create (as the name implies) reports using the results obtained in each workspace.
When an Executive Report is created, all the data from the Status Report is automatically processed and placed in a Word compatible document that can then be downloaded.

### Requirements

To utilize this feature follow the necessary steps on our [start up configuration](https://github.com/infobyte/faraday/wiki/first-steps#installation).

### Managing Executive Reports

To manage your reports you need to access Faraday's Web Interface and click on the icon **executive reports** ![]
(https://raw.github.com/wiki/infobyte/faraday/images/faraday_report_icon.png)

![](https://raw.github.com/wiki/infobyte/faraday/images/faraday_report_create.png)

All the reports will be listed, including their info, status and link to download.

To edit a report, select it and click on the **edit button** ![](https://raw.github.com/wiki/infobyte/faraday/images/faraday_report_edit_button.png). A modal will appear allowing you to modify all the report fields. Save it and a brand new report will be generated, keeping the original version intact.

### Making a report

To create a new report, navigate to the Executive Report component and click on **New**
![](https://raw.github.com/wiki/infobyte/faraday/images/faraday_report_new_button.png). A form will open asking for the following fields:

* **report name** - this is the name that will be used to name the report file
* **use only confirmed vulns** - if this checkbox is *selected*, no false positives will be present in the final report
* **tags** - when selected, vulnerabilities will be filtered by the selected tag. If more than one tag is selected, all vulns containing one of those will be present in the final report
* **grouped report** - select this option to generate a report using a grouped dataset
* **template** - select the template to use as a base for your report. Depending on the selected dataset the options will change
* **title** - this is the name that will be used to create the cover of the report
* **scope**
* **objectives**
* **summary**
* **conclusions**
* **recommendations**

![](https://raw.github.com/wiki/infobyte/faraday/images/faraday_report_new.png)

Faraday processes all the information and spits out a shiny new report that is available for download from the same list.

![](https://raw.github.com/wiki/infobyte/faraday/images/faraday_report_word.png)

#### Filtering

There are two main ways to manage the data that goes into the final report - confirming vulns and tagging them.

By default all of the vulnerabilities added manually are set as *confirmed* and all of those added by a Plugin are set as *false positives*. If the checkbox "use only confirmed vulns" is selected, the report will only contain confirmed findings.

If you need a custom report that includes only some of the findings in the workspace, you can also tag the desired vulnerabilities and then create a Report only with that tag.

At least one vulnerability must be tagged in order to have the option to generate a tag-filtered report. When the form opens an option to select tags will appear. Keep in mind that one or more tags can be selected.

These two parameters (confirmed and tags) can be mixed to create different outcomes.

![](https://raw.github.com/wiki/infobyte/faraday/images/faraday_report_using_tags.png)

### Eliminating a report

From the Executive Report window, select the document and click on **Delete**
![](https://raw.github.com/wiki/infobyte/faraday/images/faraday_report_delete_button.png)


### Templates

All report templates are located in ```reports/executive/templates```. The default one is ```generic_default.docx```, you can modify it to get customized reports.

The template uses Jinja2 syntax so we strongly recommend reading the [official documentation](http://jinja.pocoo.org/docs/dev/templates/) before modifying the document. The library used to create the report is **python-docx-template** available via [Github](https://github.com/elapouya/python-docx-template/). All Jinja2 tags are available, although there are some [restrictions](http://docxtpl.readthedocs.io/en/latest/#restrictions).

An example of how the template cover looks like

![](https://raw.github.com/wiki/infobyte/faraday/images/faraday_report_template_example.png)

#### Datasets

Faraday provides two different datasets to create Executive Reports - **generic** and **grouped**.

The *generic dataset* provides one entry for each individual vulnerability with all of its fields readily available as a dictionary. The field **parent** contains an ID corresponding to the vulnerability's parent (either a Host or a Service).

The *grouped dataset* groups vulnerabilities by **name and description**. If two or more vulnerabilities share the same name and description, they will be presented as one. The field **parent** contains a Python Dictionary-style object with the parent IDs as keys and a Python Dictionary-style object containing **evidence_subdoc**, **data** and **__taget__** as values. **Tags** and **references** will be merged for vulnerabilities that are grouped and not separated by parent.

By default all of the reports are created using the *generic dataset*. To create a report using the *grouped dataset*, select the checkxbox "grouped report" when creating it, as shown below.

![](https://raw.github.com/wiki/infobyte/faraday/images/faraday_report_using_grouped_vulns.png)

Keep in mind that each template should be designed for a specific dataset and that these are not interchangeable. 

#### Naming

If you want to add a new template make sure to follow the naming guidelines as follows.

* **generic_{customName}.docx** for generic reports - all the vulnerabilities will be listed as individual items in these reports
* **group_{customName}.docx** for grouped reports - vulnerabilities will be grouped by name and description

#### Data

The data available to the Report template is:
* **conclusions** - contains the text loaded when [creating the report](#making-a-report)
* **counter_severity** - a dictionary with all the severities and the amount of vulns for each one
* **date** - the date when the Report was created, as the name of the month and four digits for the year
* **enterprise** - contains the text loaded when [creating the report](#making-a-report)
* **hosts** - a dictionary with all the hosts in the Workspace
* **hosts_amount** - an int containing the amount of hosts in the Workspace
* **objectives** - contains the text loaded when [creating the report](#making-a-report)
* **overview_images** - a [sub-document](http://docxtpl.readthedocs.io/en/latest/#sub-documents) containing vulnerability piecharts
* **recommendations** - contains the text loaded when [creating the report](#making-a-report)
* **scope** - contains the text loaded when [creating the report](#making-a-report)
* **services** - a dictionary with all the services in the Workspace
* **services_amount** - an int containing the amount of services in the Workspace
* **summary** - contains the text loaded when [creating the report](#making-a-report)
* **title** - contains the text loaded when [creating the report](#making-a-report)
* **vulns** - a dictionary with all the vulnerabilities in the Workspace except for vulns with severity _unclassified_, which are not included
* **vulns_amount** - an int containing the amount of vulnerabilities in the Workspace except for vulns with severity _unclassified_, which are not included

Grouped reports will have an additional field:

* **vulns_grouped_amount** - an int containing the total amount of vulnerabilities after grouping