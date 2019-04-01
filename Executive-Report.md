**This feature is only available for our [commercial versions](https://www.faradaysec.com/#download).**
<a name="index"></a>

* [Intro](#intro)
* [Requirements](#requirements)
* [Managing Executive Reports](#managing-executive-reports)
* [Making a Report](#making-a-report)
* [Using markdown on a report](#using-markdown-on-a-report)
* [Eliminating a Report](#eliminating-a-report)
* [Templates](#templates)


### Intro

> No more 3AM reporting!

The Executive Reports  feature lets you create (as the name implies) reports using the results obtained in each workspace.
When an Executive Report is created, all the data from the Status Report is automatically processed and placed in a Word compatible document that can then be downloaded.

### Requirements

To utilize this feature follow the necessary steps on our [start up configuration](https://github.com/infobyte/faraday/wiki/first-steps).

### Managing Executive Reports

To manage your reports you need to access Faraday's Web Interface and click on **Executive Report** icon (the one that looks like a sheet).

![](https://raw.github.com/wiki/infobyte/faraday/images/executive_reports/icon.png)

All the reports will be listed, including their info, status and link to download.

To edit a report, select it and click on the **Edit** button. A modal will appear allowing you to modify all the report fields. Save it and a brand new report will be generated, keeping the original version intact.

If, instead, you want a new report that is exactly like an existing one but with the current data of your workspace, you can click on the **Regenerate** button in the reports list.

![](https://raw.github.com/wiki/infobyte/faraday/images/executive_reports/regenerate_button.png)

Reports can only be regenerated one at a time, so the regeneration buttons are disabled while this action is being performed.

### Making a report

To create a new report, navigate to the Executive Report component and click on **New**. A form will open asking for the following fields:

* **Report name** - this will be used to name the report file.
* **Use only confirmed vulns for this report** - if this checkbox is *selected*, no false positives will be present in the final report.
* **Tags** - when selected, vulnerabilities will be filtered by the selected tag. If more than one tag is selected, all vulns containing one of those will be present in the final report.
* **Template** - select the template to use as a base for your report. Depending on the selected [dataset](#datasets) the options will change
* **Grouped report** - select this option to generate a report using a grouped dataset.
* **Title** - this is the name that will be used to create the cover of the report.

The following are a sort of placeholder fields for information that's commonly added to most reports. They are text fields and can be used for any relevant information, not just for what they're named after:
* **Scope**
* **Objectives**
* **Summary**
* **Conclusions**
* **Recommendations**

![](https://raw.github.com/wiki/infobyte/faraday/images/executive_reports/new.png)

Faraday processes all the information and spits out a shiny new report that is automatically available for download.

![](https://raw.github.com/wiki/infobyte/faraday/images/executive_reports/word.png)

#### Filtering

There are two main ways to manage the data that goes into the final report - *confirming vulns* and *tagging them**.

By default all of the vulnerabilities added manually are set as *confirmed* and all of those added by a Plugin are set as *false positives*. If the checkbox "use only confirmed vulns" is selected, the report will only contain confirmed findings.

If you need a custom report that includes only some of the findings in the workspace, you can also *tag* the desired vulnerabilities and then create a report only with that tag.

At least one vulnerability must be tagged in order to have the option to generate a tag-filtered report. When the form opens an option to select tags will appear. Keep in mind that one or more tags can be selected.

These two parameters (confirmed and tags) can be mixed to create different outcomes.

![](https://raw.github.com/wiki/infobyte/faraday/images/executive_reports/using_tags.png)

### Using markdown on a report

For using markdown on executive reports, please enable it on server.ini by adding:

```
[executive_report]                                                                                                                                           
markdown = true   
```

Executive reports supports markdown (v3.7 or higher). Currently we do not support all markdown lenguage.
We support the following markdown:

* Titles
* Tables
* Faraday Inline evidence (with custom markdown)
* Bold and italic

Executive report supports markdown on the following fields:

* Vulnerability description
* Vulnerability data
* Executive report scope
* Executive report objectives
* Executive report summary
* Executive report conclusions
* Executive report recommendations

You can use inline evidence in the fields above using the following:

(evidence:vulnerability:ID:evidence_filename.png).

Note: You can copy this custom markdown from the evidence tab of the vulnerability.



For example suppose the you want to explain how to reproduce the issue in the vulnerability description:


```
The Vulnerability is triggered by opening the following url:

(evidence:vulnerability:ID:web_app_step_1.jpg)

After you open the vulnerable url, enter the following on the form:

(evidence:vulnerability:ID:web_app_step_2.jpg).

The following screenshot shows the database contents:

(evidence:vulnerability:ID:database_table_names.jpg)

```

### Eliminating a report

From the Executive Report window, select the document and click on **Delete**
![](https://raw.github.com/wiki/infobyte/faraday/images/executive_reports/delete_button.png)


### Templates

All report templates are located in ```reports/executive/templates``` in your Faraday installation directory. The default one is ```generic_default.docx```, you can modify it to get customized reports. 

You can also save your custom templates in ```~/.faraday/executive_reports_templates/```. This way, you will not lose your templates after an update.

You can download an example report [here](https://github.com/infobyte/faraday/wiki/files/example_report.docx) and its corresponding template [here](https://github.com/infobyte/faraday/wiki/files/generic_default.docx).

The template uses Jinja2 syntax so we strongly recommend reading the [official documentation](http://jinja.pocoo.org/docs/dev/templates/) before modifying the document. The library used to create the report is **python-docx-template** available via [Github](https://github.com/elapouya/python-docx-template/). All Jinja2 tags are available, although there are some [restrictions](http://docxtpl.readthedocs.io/en/latest/#restrictions).

An example of how the template cover looks like

![](https://raw.github.com/wiki/infobyte/faraday/images/executive_reports/template_example.png)

#### Datasets

Faraday provides two different datasets to create Executive Reports - **generic** and **grouped**.

The *generic dataset* provides one entry for each individual vulnerability with all of its fields readily available as a dictionary. The field **parent** contains an ID corresponding to the vulnerability's parent (either a Host or a Service).

The *grouped dataset* groups vulnerabilities by **name and description**. If two or more vulnerabilities share the same name and description, they will be presented as one. The field **parent** contains a Python Dictionary-style object with the parent IDs as keys and a Python Dictionary-style object containing **evidence_subdoc**, **data** and **__target__** as values. **Tags** and **references** will be merged for vulnerabilities that are grouped and not separated by parent.

By default all of the reports are created using the *generic dataset*. To create a report using the *grouped dataset*, select the checkxbox "grouped report" when creating it, as shown below.

![](https://raw.github.com/wiki/infobyte/faraday/images/executive_reports/using_grouped_vulns.png)

Keep in mind that each template should be designed for a specific dataset and that these are not interchangeable. 

#### Naming

If you want to add a new template make sure to follow the naming guidelines as follows.

* **generic_{customName}.docx** for generic reports - all the vulnerabilities will be listed as individual items in these reports
* **group_{customName}.docx** for grouped reports - vulnerabilities will be grouped by name and description

## Data

The data available to the Report template is:

### General Variables
* **conclusions** - contains the text loaded when [creating the report](#making-a-report)
* **date** - the date when the Report was created, as the name of the month and four digits for the year
* **objectives** - contains the text loaded when [creating the report](#making-a-report)
* **enterprise** - contains the text loaded when [creating the report](#making-a-report)
* **recommendations** - contains the text loaded when [creating the report](#making-a-report)
* **summary** - contains the text loaded when [creating the report](#making-a-report)
* **title** - contains the text loaded when [creating the report](#making-a-report)
* **scope** - contains the text loaded when [creating the report](#making-a-report)
* **overview_images** - a [sub-document](http://docxtpl.readthedocs.io/en/latest/#sub-documents) containing * 

### Hosts Variables
* **hosts_amount** - an int containing the amount of hosts in the Workspace
* **hosts** - a dictionary with all the hosts in the Workspace
    * type
    * description
    * default_gateway
    * ip
    * owned
    * tags
    * name
    * services
    * mac
    * hostnames
    * vulns
    * owner
    * credentials
    * service_summaries
    * id
    * os
    * id
    * metadata

### Service Variables
* **services_amount** - an int containing the amount of services in the Workspace
* **services** - a dictionary with all the services in the Workspace
    * status
    * protocol
    * description 
    * parent
    * vulns
    * metadata
    * owned
    * summary
    * port
    * owner
    * version
    * host_id
    * id
    * credentials
    * type
    * ports
    * name

### Vulnerability Variables
* **counter_severity** - a dictionary with all the severities and the amount of vulns for each onevulnerability piecharts
* **vulns_amount** - an int containing the amount of vulnerabilities in the Workspace except for vulns with severity _unclassified_, which are not included
* **vulns** - a dictionary with all the vulnerabilities in the Workspace except for vulns with severity _unclassified_, which are not included
    * update_user
    * parent_type
    * owned
    * owner
    * id
    * impact
    * confirmed
    * severity
    * service
    * data
    * policyviolations
    * evidence_subdoc
    * type
    * refs
    * metadata
    * status
    * issuetracker
    * description
    * parent
    * tags
    * easeofresolution
    * hostnames
    * date
    * host_os
    * desc
    * name
    * obj_id
    * target
    * resolution
Grouped reports will have an additional field:

* **vulns_grouped_amount** - an int containing the total amount of vulnerabilities after grouping


### Workspace Variables
* **workspace.scope** - a list containing the different scopes of the workspace. 
* **workspace** - a dictionary with all workspace informartion.

    * name
    * description
    * id
    * duration.start_date
    * duration.end_date
    * users



