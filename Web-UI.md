In order to access the Web UI point your browser to: http://[COUCHDB]:5984/reports/_design/reports/index.html

![](https://raw.github.com/wiki/infobyte/faraday/images/Console_GUIWeb_Highlight.png)

Directly from the GUI QT you have to click in the icon:

![](https://raw.github.com/wiki/infobyte/faraday/images/Visualize-icon.png)

## Faraday Community Version

##### Dashboard

Faraday's dashboard contains a summary of all the data in a Workspace condensed into different boxes. Each box is a visualization using a specific part of the collected data.

![](https://raw.github.com/wiki/infobyte/faraday/images/GUI_Dashboard_new.png)

##### Vulnerability Status Report

To view a full list of findings you can access the Status Report.

![](https://raw.githubusercontent.com/wiki/infobyte/faraday/images/UI_Web_Status_Report.png)

The Status Report provides several options including vulnerability search, filtering and management.

Personalize this view by clicking on the blue buttons to select the columns you wish to see, and remove the ones you don't need using the crosses in the table. These changes will be persisted in your browser so you only have to apply them once.

##### Search & Filter

To search, type the keyword in the text field above the table.

You can find the text filter both on the Status Report and Hosts views. Keep in mind that field values are case-insensitive.

![](https://raw.github.com/wiki/infobyte/faraday/images/search.png)

##### Filter by field

To search by field enter the name of field  (e.g. **severity**), continue with a colon  (**:**) and finally put in the word that you want to find.

Examples: 
* severity:unclassified
* name:Nessus scan info

![](https://raw.github.com/wiki/infobyte/faraday/images/filterByField.png)

##### Filter by many fields

To search by many fields do a normal search but at the end type a *SPACE BAR* and do a normal search again.

Examples:
* severity:unclassified target:173.252.100.18
* severity:low service:443 target:173.252

![](https://raw.github.com/wiki/infobyte/faraday/images/searchByManyFields.png)

<a name="manage"></a>
##### Vulnerability Creation

![](https://raw.githubusercontent.com/wiki/infobyte/faraday/images/faraday_new.png)

##### Top Services View

To access a [treemap](https://en.wikipedia.org/wiki/Treemapping) featuring the top services in the Workspace, click on the box title.

![](https://raw.github.com/wiki/infobyte/faraday/images/GUI_Dashboard_new_Services.png)

![](https://raw.github.com/wiki/infobyte/faraday/images/GUI_Services.png)

<a name="workspace-worth"></a>
##### Workspace's Worth

![](https://raw.github.com/wiki/infobyte/faraday/images/faraday-dashboard-ws-worth.png)

This visualization is specially helpful when contributing in a bug bounty program. You can estimate how much your Workspace is worth according to the severity of your vulnerabilities.

You can edit the price per severity by clicking on it. The graphic will change as you type.

So lets say that you have a workspace with 6 vulns, one for each severity. And the price schema is:

* Criticals are worth 6 dollars
* Highs are worth 5 dollars
* Meds are worth 4 dollars
* Lows are worth 3 dollars
* Infos are worth 2 dollars
* Unclassifieds are worth 1 dollar

Then your Workspace will be worth 
```
6*1+5*1+4*1+3*1+2*1+1*1 = $21
```

The length of the colored bars shows how much that severity represents in the final worth according to how many of those are present in the current workspace.

Learn more about using Faraday for [[Bug bounties]].

## Faraday Professional & Corporate
**Faraday Professional & Corporate** has advance visualization (including Tags, Pentest comparison, Pentester ranking, etc)

![](https://raw.github.com/wiki/infobyte/faraday/images/Faraday-Dashboard-Advance.png)



