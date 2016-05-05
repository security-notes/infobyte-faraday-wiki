This feature is only available for our [commercial versions](https://www.faradaysec.com/#download).

### Intro

The Executive Reports lets you create (as the name implies) reports using the results obtained in each workspace.
When an Executive Report is created, all the data from the Status Report is automatically processed and placed in a Word compatible document that can then be downloaded.

### Requirements

To utilize this feature follow the necessary steps on our [start up configuration](https://github.com/infobyte/faraday/wiki/Faraday-Server).

### Managing Executive Reports

To manage your reports you need to access Faraday's Web Interface and click on the icon **executive reports** ![]
(https://raw.github.com/wiki/infobyte/faraday/images/faraday_report_icon.png)

![](https://raw.github.com/wiki/infobyte/faraday/images/faraday_report_create.png)

All the reports will be listed, including their info and status.

Once a report has been generated it can't be edited.

### Making a report

To create a new report, navigate to the Executive Report component and click on **New**
![](https://raw.github.com/wiki/infobyte/faraday/images/faraday_report_new_button.png). A new form will open, asking for the following fields:

* Title
* Scope
* Objectives
* Summary
* Conclusions
* Recommendations

![](https://raw.github.com/wiki/infobyte/faraday/images/faraday_report_new.png)

Faraday processes all the information and spits out a shiny new report that is available for download from the same list.

![](https://raw.github.com/wiki/infobyte/faraday/images/faraday_report_procesing.png)

![](https://raw.github.com/wiki/infobyte/faraday/images/faraday_report_word.png)

If you need a custom report that includes only some of the findings in the workspace, you can tag the desired vulnerabilities and then create a Report only with that tag.
At least one vulnerability must be tagged in order to have the option to generate a filtered Report. When the form opens an option to select tags will appear. Keep in mind that one or more tags can be selected.
![](https://raw.github.com/wiki/infobyte/faraday/images/faraday_report_using_tags.png)


### Eliminating a report

From the Executive Report window, select the document and click on **Delete**
![](https://raw.github.com/wiki/infobyte/faraday/images/faraday_report_delete_button.png)


### Templates

All Report templates are located in ```reports/executive/templates```. The default one is ```generic.docx```, you can modify it to get customized reports.

The template uses Jinja2 syntax so we strongly recommend reading the [official documentation](http://jinja.pocoo.org/docs/dev/templates/) before modifying the document. The library used to create the report is **python-docx-template** available via [Github](https://github.com/elapouya/python-docx-template/). All Jinja2 tags are available, although there are some [restrictions](http://docxtpl.readthedocs.io/en/latest/#restrictions).

An example of how the template cover looks like

![](https://raw.github.com/wiki/infobyte/faraday/images/faraday_report_template_example.png)

#### Data

Keep in mind that the data available to the Report is:
* conclusions - contains the text loaded when [creating the report](#making-a-report)
* date - the date when the Report was created, as the name of the month and four digits for the year
* enterprise - contains the text loaded when [creating the report](#making-a-report)
* hosts - a dictionary with all the hosts in the Workspace
* objectives - contains the text loaded when [creating the report](#making-a-report)
* overview_images - a [sub-document](http://docxtpl.readthedocs.io/en/latest/#sub-documents) containing vulnerability piecharts
* recommendations - contains the text loaded when [creating the report](#making-a-report)
* scope - contains the text loaded when [creating the report](#making-a-report)
* services - a dictionary with all the services in the Workspace
* summary - contains the text loaded when [creating the report](#making-a-report)
* title - contains the text loaded when [creating the report](#making-a-report)
* vulns - a dictionary with all vulnerabilities in the Workspace
* vulns_amount - number of vulnerabilities in the Workspace

<a name="manual-reports"></a>
### Manually generating Reports

If, for any reason, the reports are not being generated after creation you can force Faraday to create them by running

```
. $FARADAYINSTALLPATH/.couchadmin; python $FARADAYINSTALLPATH/pushExecutiveReports.py
```
