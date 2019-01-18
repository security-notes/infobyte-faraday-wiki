# Custom fields

## Introduction

Custom fields allows you to extend the vulneraiblity model with more fields. Custom fields type can be int, str and list.

With pro and corp version you can use the custom fields in the executive report.


## How to use custom fields

Step 1: Add custom field

```
python manage.py add-custom-field 
```

After the command execution you will be prompted by a wizard.

* Field name: the name of the field
* Display name: The display name you will see at the vulneraiblity form
* Type: int, str or list
* Order: The order shown at the vulnerability form

The following example will add hte CVSS field to the vulneraiblity model.

```
This wizard will guide you to ADD custom field to the vulneraiblity model.
Field name: cvss
Display name: CVSS
Field type (int, str, list) (int, str, list): str
Field order index: 0
New CustomField will be added to vulnerability -> Order 0 (cvss,CVSS,str) <-, confirm to continue (yes/no): yes
```

After the successful creation you will see the custom field on the vulneraibity form:

![Vulnerability custom fields](https://user-images.githubusercontent.com/568181/51412576-c0f01480-1b4a-11e9-961f-69b80b8ba325.png)

If you have the corporate version you can access cusotm fields on the docx templates like a dictionary:

```
vuln.custom_fields["CVSS"] 
```