## Search & Filter

You can find the text filter on:

* Status Report
* Hosts
* Services

In order to perform a search, type the keyword in the text field above the table.

**Field values are not case-sensitive**

![](https://raw.github.com/wiki/infobyte/faraday/images/status_report/search.png)

## How to filter by one field

In order to perform a search by one field, follow these steps:

1. Enter the name of the field  (e.g. **severity**).
2. Type a colon  (**:**) right next to the name of the field specified above.
3. Type in the word that you want to find inside quotation marks (**"**).

Examples: 

* severity:"unclassified"
* name:"Nessus scan info"

![](https://raw.github.com/wiki/infobyte/faraday/images/status_report/filter_by_field.png)

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

## Grouping

To group vulnerabilities by field you can use the **Group By** button. After the vulns are grouped you can select them for easy batch editing.

![](https://raw.githubusercontent.com/wiki/infobyte/faraday/images/status_report/vulns_group_by.png)

## Confirmed

You can filter your vulnerabilities by confirmed, unconfirmed or all as shown in this gif:

![](https://raw.githubusercontent.com/wiki/infobyte/faraday/images/status_report/Unconfirmed.gif)


