**Only available for our [commercial Corporate version](https://www.faradaysec.com/#download).**

This is a feature that allows you to send data from Faraday to JIRA. In order to do it, go into our [Status Report](https://github.com/infobyte/faraday/wiki/Status-report), select the desired vulnerabilities, click on the **Tools** button and then click on the **JIRA** option. Keep in mind that only confirmed vulnerabilities can be sent.

![](https://raw.githubusercontent.com/wiki/infobyte/faraday/images/jira/button.png)

Once the JIRA dialog opens, you have two options:

1. You can use the default data specified in the **[ticketing_tool]** section of the _~/.faraday/config/server.ini_ file 

![](https://raw.githubusercontent.com/wiki/infobyte/faraday/images/jira/dialog_default_data.png)


2. You can overwrite JIRA default data by clicking on the checkbox button and then manually input your JIRA credentials. Then click **OK**.

![](https://raw.githubusercontent.com/wiki/infobyte/faraday/images/jira/dialog_overwrited_data.png)

**Note:** if you overwrite only one field, Faraday will fill the others fields with the default data. E.g: if you overwrite Username, Faraday will fill the others fields with the information you have specified in the _server.ini_ file. 

Once the vulnerability has been sent to JIRA, add the column _issuetracker_ so you can see a link that will lead you to this same issue but in JIRA.

![](https://raw.githubusercontent.com/wiki/infobyte/faraday/images/jira/issuetracker.png)