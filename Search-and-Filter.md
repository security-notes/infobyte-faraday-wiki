
<a name="index"></a>
* [Intro](#intro)
* [How to filter by one field](#filter-by-one-field)
* [How to filter by many fields](#filter-by-many-fields)
* [Grouping Vulnerabilities](#grouping)
* [Confirmed Vulnerabilities](#confirmed)
* [Usage Case](#usage-case)

<a name="intro"></a>
## Intro
You can search or filter your data by specifying a keyword or multiple keywords.

You can find the text filter on:

* [Status Report](#status-report)
* [Hosts](#hosts)
* [Services](#services)

In order to perform a search, type the keyword in the text field above the table.

**Field values are not case-sensitive**

![](https://raw.github.com/wiki/infobyte/faraday/images/status_report/search.png)


<a name="filter-by-one-field"></a>
## How to filter by one field

In order to perform a search by one field, follow these steps:

1. Enter the name of the field  (e.g. **severity**).
2. Type a colon  (**:**) right next to the name of the field specified above.
3. Type in the word that you want to find inside quotation marks (**"**).

Examples: 

* severity:"unclassified"
* name:"Nessus scan info"

![](https://raw.github.com/wiki/infobyte/faraday/images/status_report/filter_by_field.png)


<a name="filter-by-many-fields"></a>
## How to filter by many fields

In order to perform a search by many fields, you can use the logical operators **and** & **or**. To perform a search, follow the next steps:

1. Type a search for one field.
2. Type **and** or **or**.
3. Type a search for another field.

Examples:

* severity:"unclassified" **and** target:"173.252.100.18"
* severity:"low" **or** service:"ssh" **or** target:"173.252"

![](https://raw.github.com/wiki/infobyte/faraday/images/status_report/search_by_many_fields.png)

![](https://raw.github.com/wiki/infobyte/faraday/images/status_report/multiple-search.gif)


<a name="grouping"></a>
## Grouping Vulnerabilities

To group vulnerabilities by field you can use the **Group By** button. After the vulns are grouped you can select them for easy batch editing.

![](https://raw.githubusercontent.com/wiki/infobyte/faraday/images/status_report/vulns_group_by.png)


<a name="confirmed"></a>
## Confirmed Vulnerabilities

You can filter your vulnerabilities by confirmed, unconfirmed or all by clicking on the **All** button:

![](https://raw.githubusercontent.com/wiki/infobyte/faraday/images/status_report/confirmed_vulns.png)


<a name="usage-case"></a>
## Usage case

Now, let's take a look at which fields are available for filtering with an example. All of them are searched through the search field.

### Status Report

* name:"TCP timestamps"
* description:"Vulnerability testing"
* severity:"medium"
* target:"127.0.0.1"
* service:"https" (only service's name)
* easeofresolution:"moderate"
* references:"cvss"
* resolution:"Resolution for testing vuln"
* data:"Search and filter"
* request:"POST"
* response:"OK"
* method:"POST"
* pname:"Parameter name"
* params:"Vulnerability parameters"
* path:"Vulnerability Path"
* query:"name:test"
* website:"Vulnerability website"
* creator:"Nessus"
* type:"vulnerability_web"
* confirmed:"true"
* id:"57448"

### Hosts

For searching in Hosts tab, just type the keyword that you want to search without quotation marks (excepting Tags). The following fields are available for searching in Hosts tab:

* IP (ex: 127.0.0.1).
* Hostname (ex: www.google.com).
* Services (ex: https). Only service's name.
* OS (ex: Linux)

To search by Tags:

* tags:internal

### Services

* name:http
* version:2.4
* port:8080
* protocol:tcp
* status:closed
* vulns:1 (number of vulns created in this service)
* credentials:1 (number of credentials created for this service)
* tags:prod