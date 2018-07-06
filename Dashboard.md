## Dashboard

Faraday's dashboard contains a summary of all the data in a Workspace condensed into different boxes. Each box is a visualization a specific aspect of the collected data.

![](https://raw.github.com/wiki/infobyte/faraday/images/GUI_Dashboard_new.png)


Let's see in more detail some of these boxes:

###### _Top Services View_

To access a [treemap](https://en.wikipedia.org/wiki/Treemapping) featuring the top services in the Workspace, click on the box title.

![](https://raw.github.com/wiki/infobyte/faraday/images/GUI_Dashboard_new_Services.png)

![](https://raw.github.com/wiki/infobyte/faraday/images/GUI_Services.gif)

<a name="workspace-worth"></a>
###### _Workspace's Worth_

![](https://raw.github.com/wiki/infobyte/faraday/images/faraday-dashboard-ws-worth.png)

This visualization is specially helpful when contributing in a bug bounty program. You can estimate how much your Workspace is worth according to the severity of your vulnerabilities.

You can edit the price of each severity level by clicking on it. The graphic will change as you type.

For instance, let's say that you have a workspace with 6 vulns, one of each severity level. And the price schema is:

* Critical vulns are worth 6 dollars
* High vulns are worth 5 dollars
* Med vulns are worth 4 dollars
* Low vulns are worth 3 dollars
* Info vulns are worth 2 dollars
* Unclassified vulns are worth 1 dollar

Then your Workspace will be worth
```
6*1+5*1+4*1+3*1+2*1+1*1 = $21
```

The length of the colored bars shows the proportion that severity represents in the final worth of your workspace.

Learn more about using Faraday for [[Bug bounties]].
