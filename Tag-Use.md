[- Commercial version -](https://www.faradaysec.com/#download)

Tags allow you to organize your vulnerabilities. by letting you make and edit categories: environment, technology, state, language, projects, whatever. The team can then see the tagged vulnerabilities and lets you organize the security evaluation.

The tags are assigned to the team's workspace letting you use different tags for different projects.

### How to tag vulnerabilities

Using the specified credentials during the configuration, from the Navigator start the session in [Faraday's GUI](https://github.com/infobyte/faraday/wiki/Web-UI). Once you have obtained the authentication and you are in, click on the “Status Report” icon.

![](https://raw.github.com/wiki/infobyte/faraday/images/faraday_statusreport_list.png)

Select the vulnerabilities that you want to tag (for example those that have to do with SSL protocol)

![](https://raw.github.com/wiki/infobyte/faraday/images/faraday_statusreport_listselected.png)

After picking one of the vulnerabilities click on the "Tags" button

![](https://raw.github.com/wiki/infobyte/faraday/images/faraday_statusreport_tagsadd.png)

Create the tag that you want (in our case SSL) and click OK

![](https://raw.github.com/wiki/infobyte/faraday/images/faraday_statusreport_tagsadded.png)

### Search tagged vulnerabilities

From the Status Report you will be able to find the information using the different tags. You can add ! in front of the search criteria in order to invert the result. For example _tag:!example_tag_ will result in all vulnerabilities that DON'T have the tag example_tag.

![](https://raw.github.com/wiki/infobyte/faraday/images/faraday_statusreport_tagssearch.png)
