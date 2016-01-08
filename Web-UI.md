In order to access the Web UI point your browser to: http://[COUCHDB]:5984/reports/_design/reports/index.html

![](https://raw.github.com/wiki/infobyte/faraday/images/Console_GUIWeb_Highlight.png)

Directly from the GUI QT you have to click in the icon:

![](https://raw.github.com/wiki/infobyte/faraday/images/Visualize-icon.png)

## Faraday Community Version

Faraday Community Version has simple visualization (Include summary information):

![](https://raw.github.com/wiki/infobyte/faraday/images/GUI_Dashboard_new.png)

**Vulnerability Status Report**

![](https://raw.github.com/wiki/infobyte/faraday/images/GUI_Dashboard_SR_Click.png)

![](https://raw.githubusercontent.com/wiki/infobyte/faraday/images/UI_Web_Status_Report.png)

**Vulnerability Creation**

![](https://raw.githubusercontent.com/wiki/infobyte/faraday/images/faraday_new.png)

**Top Services View**

![](https://raw.github.com/wiki/infobyte/faraday/images/GUI_Dashboard_new_Services.png)

![](https://raw.github.com/wiki/infobyte/faraday/images/GUI_Services.png)

**Workspace Worth**<a name="workspace-worth"></a>

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

## Search & Filter

To search, type the keyword in the text field above the table.

You can find the text filter on:
* Status Report
* Hosts

**Field values are not case-sensitive**

![](https://raw.github.com/wiki/infobyte/faraday/images/search.png)

## How to filter by field

To search by field, enter the name of field  (e.g. **severity**) , continue a colon  (**:**) , finally put in the word that you want to find.

Examples: 
* severity:unclassified
* name:Nessus scan info

![](https://raw.github.com/wiki/infobyte/faraday/images/filterByField.png)

## How to filter by many fields

To search by many field, do a normal search but at the end, type a SPACE BAR and do a normal search again.
Just a SPACE BAR in the middle of the consult.

Examples:
* severity:unclassified target:173.252.100.18
* severity:low service:443 target:173.252

![](https://raw.github.com/wiki/infobyte/faraday/images/searchByManyFields.png)

## Faraday Professional & Corporate
**Faraday Professional & Corporate** has advance visualization (including Tags, Pentest comparison, Pentester ranking, etc)

![](https://raw.github.com/wiki/infobyte/faraday/images/Faraday-Dashboard-Advance.png)



