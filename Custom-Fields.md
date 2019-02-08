Custom fields allows you to extend the vulnerability's model with more fields. Custom fields type can be **int**, **str** and **list**.

With our [Professional and Corporate](https://www.faradaysec.com/#download) versions, you can use the custom fields in the executive report.

Check here [how to useFaraday custom fields using the API](https://github.com/infobyte/faraday/wiki/Using-custom-fields-from-the-API)

## How to use custom fields

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

**Note:** If you have a commercial version of Faraday, you can access the custom fields on the docx templates like a dictionary:

```
vuln.custom_fields["CVSS"] 
```

Note: use the display name in the report