Custom fields allows you to extend the vulnerability's model with more fields. Custom fields type can be int, str and list.
You can [learn more about custom fields creation on this wiki page](https://github.com/infobyte/faraday/wiki/Custom-fields).

In this small tutorial, we are going to use python requests to authenticate, create a vuln and modify custom fields.

# Step 1: Authentication

For authentication, we are going to use a function called faraday_authentication. This function will return an authenticated request session.

``` python
def faraday_authentication(host, username, password):
    """
       @host: faraday server host, ex. http://127.0.0.1:5985
       @username: faraday username
       @password: the password of the username

       return requests session object
    """
    session = requests.Session()
    headers = {
        'Content-Type': 'application/json', # Very important! send this content-type header!!
    }
    data = '{"email":username,"password": password}'
    response = s.post('{0}/_api/login'.format(host), headers=headers, data=data)
    assert response.status_code == 200
    return session
```

# Step 2: Create custom fields

Please [follow the steps of this wiki page](https://github.com/infobyte/faraday/wiki/Custom-fields#how-to-use-custom-fields).

# Step 3: Create a vulnerability from the api

Before using the API you need to understand how to send the data to the server. Faraday server accepts json and the vulnerability format is the following:

```
{
  "metadata": {
    "update_time": 1549569790.632,
    "update_user": "",
    "update_action": 0,
    "creator": "UI Web",
    "create_time": 1549569790.632,
    "update_controller_action": "UI Web New",
    "owner": "faraday"
  },
  "obj_id": "",
  "owner": "faraday",
  "parent": 24,
  "parent_type": "Host",
  "type": "Vulnerability",
  "ws": "demo_workspace",
  "confirmed": true,
  "data": "",
  "desc": "Test",
  "easeofresolution": null,
  "impact": {
    "accountability": false,
    "availability": false,
    "confidentiality": false,
    "integrity": false
  },
  "name": "dsadsadsa",
  "owned": false,
  "policyviolations": [],
  "refs": [],
  "resolution": "",
  "severity": "unclassified",
  "issuetracker": "",
  "status": "opened",
  "custom_fields": {},
  "_attachments": {},
  "description": "",
  "protocol": "",
  "version": ""
}
```

Note that we have a key called "custom_fields" with an empty dictionary.
```
"custom_fields": {}
```

Another important field to understand is the parent_id and parent_type. In the json avobe we used "Host" with parent "24" since in our database we have a host with id 24.
You can [learn more about the API here](https://github.com/infobyte/faraday/wiki/API-Server)


Here is a code sample that will create a new vulnerability called "Test"
NOTE: we use the workspace called "demo_workspace" in all the examples. 

``` python
faraday_host = 'http://127.0.0.1:5985'
session = faraday_authentication(faraday_host, 'faraday', 'secret')
vulnerability_url = '{0}//_api/v2/ws/demo_workspace/vulns/386/'.format(faraday_host)
vuln_payload = '{"metadata":{"update_time":1549569790.632,"update_user":"","update_action":0,"creator":"UI Web","create_time":1549569790.632,"update_controller_action":"UI Web New","owner":"faraday"},"obj_id":"","owner":"faraday","parent":24,"parent_type":"Host","type":"Vulnerability","ws":"demo_workspace","confirmed":true,"data":"","desc":"dsadsadsa","easeofresolution":null,"impact":{"accountability":false,"availability":false,"confidentiality":false,"integrity":false},"name":"Test","owned":false,"policyviolations":[],"refs":[],"resolution":"","severity":"unclassified","issuetracker":"","status":"opened","custom_fields":{},"_attachments":{},"description":"","protocol":"","version":""}'
response = session.post(vulnerability_url, json=vuln_payload)
```

The server is going to answer with the created vulnerability and it will return status code 201 or 409 (conflict).
In our case it returned the id 386 on the key "_id".

When you create the vuln you can send the custom fields information. Suppose you create a custom field with the following data:

`Field name: cvss`
`Display name: CVSS`

Now on the field "custom_fields" you can send the following:

```
{
  "metadata": {
    "update_time": 1549570358.149,
    "update_user": "",
    "update_action": 0,
    "creator": "UI Web",
    "create_time": 1549570358.149,
    "update_controller_action": "UI Web New",
    "owner": "faraday"
  },
  "obj_id": "",
  "owner": "faraday",
  "parent": 24,
  "parent_type": "Host",
  "type": "Vulnerability",
  "ws": "demo_workspace",
  "confirmed": true,
  "data": "",
  "desc": "dsadsa",
  "easeofresolution": null,
  "impact": {
    "accountability": false,
    "availability": false,
    "confidentiality": false,
    "integrity": false
  },
  "name": "Test",
  "owned": false,
  "policyviolations": [],
  "refs": [],
  "resolution": "",
  "severity": "unclassified",
  "issuetracker": "",
  "status": "opened",
  "custom_fields": {
    "CVSS": "4"
  },
  "_attachments": {},
  "description": "",
  "protocol": "",
  "version": ""
}
```

Note that the custom field has new data:

```
"custom_fields": {
    "CVSS": "4"
  },
```

NOTE: If you didn't use python manage.py add-custom-field to add CVSS field, it will no have any effect on the vuln. Remember to create the custom field first.

Now you can try to do a get on the following url to see the vulnerability in json format with custom fields:

`http://localhost:5985/_api/v2/ws/demo_workspace/vulns/386/`

Remember to change the ID in the URL to the correct one on your database.

# Step 3: Update custom fields

In the next example we are going to update the custom field CVSS of the vulnerability 386. The new value will be "5". 
NOTE: When you update a vulnerability you need to send the full json body of the vulnerability.

``` python
faraday_host = 'http://127.0.0.1:5985'
session = faraday_authentication(faraday_host, 'faraday', 'secret')
vulnerability_url = '{0}/_api/v2/ws/demo_workspace/vulns/386/'.format(faraday_host)
vuln_payload = '{"metadata":{"update_time":1549569790.632,"update_user":"","update_action":0,"creator":"UI Web","create_time":1549569790.632,"update_controller_action":"UI Web New","owner":"faraday"},"obj_id":"","owner":"faraday","parent":24,"parent_type":"Host","type":"Vulnerability","ws":"demo_workspace","confirmed":true,"data":"","desc":"dsadsadsa","easeofresolution":null,"impact":{"accountability":false,"availability":false,"confidentiality":false,"integrity":false},"name":"Test","owned":false,"policyviolations":[],"refs":[],"resolution":"","severity":"unclassified","issuetracker":"","status":"opened","custom_fields":"CVSS": "5","_attachments":{},"description":"","protocol":"","version":""}'
response = session.post(vulnerability_url, json=vuln_payload)
```