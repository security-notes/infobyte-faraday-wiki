<a name="index"></a>
### Index
* [How to create Custom Fields](#cf_creation)
* [Custom Fields in Executive Report](#cf_in_exec_report)

### Intro
Custom Fields allow you to extend the vulnerability's model with more fields. Custom fields type can be **int**, **str** and **list**.

With our [Professional and Corporate](https://www.faradaysec.com/#download) versions, you can use the custom fields in the executive report.

If you want to learn more about the usage of Custom Fields through Faraday's API, follow this [link](https://github.com/infobyte/faraday/wiki/Using-custom-fields-from-the-API).

<a name="cf_creation"></a>
## How to create Custom Fields

### From Web UI

You can create/edit/delete a Custom Field from [Settings](https://github.com/infobyte/faraday/wiki/Settings). Let's create one as an example:

![](https://raw.githubusercontent.com/wiki/infobyte/faraday/images/settings/custom_field_new.png)

* You must fill the following fields in order to create a Custom Field:
    * _Display name_: the display name that you will see on the vulnerability form.
    * _Name_: the name of the field (must be unique).
    * _Type_: data type of the field, it can be: **int**, **str** or **list**.

       ![](https://raw.githubusercontent.com/wiki/infobyte/faraday/images/settings/custom_field_creating.png)

* Once you create a Custom Field, you will see it listed as below:

  ![](https://raw.githubusercontent.com/wiki/infobyte/faraday/images/settings/custom_field_list.png)

* After successfully creating the custom field, you will see it on the vulneraibity form:

  ![](https://raw.githubusercontent.com/wiki/infobyte/faraday/images/custom_fields/custom_field_in_vuln_form.png)

### From Terminal
**Step 1:** Add custom field

```
python manage.py add-custom-field 
```

**Step 2:** After the command execution, you will be prompted by a wizard where you must input the following information:

* _Field name_: the name of the field.
* _Display name_: the display name that you will see on the vulnerability form.
* _Type_: data type of the field, it can be: **int**, **str** or **list**.
* _Order_: the order shown on the vulnerability form.

The following example will add the CVSS field to the vulnerability model:

```
This wizard will guide you to ADD custom field to the vulneraiblity model.
Field name: cvss
Display name: CVSS
Field type (int, str, list) (int, str, list): str
Field order index: 0
New CustomField will be added to vulnerability -> Order 0 (cvss,CVSS,str) <-, confirm to continue (yes/no): yes
```

**Step 3:** After successfully creating the custom field, you will see it on the vulneraibity form:

![Vulnerability custom fields](https://user-images.githubusercontent.com/568181/51412576-c0f01480-1b4a-11e9-961f-69b80b8ba325.png)

<a name="cf_in_exec_report"></a>
## Custom Fields in Executive Report

If you have a commercial version of Faraday, you can access the custom fields on the docx templates like a dictionary and by the field name:

```
vuln.custom_fields["cvss"] 
```

**Note:** use the **field name** in the report