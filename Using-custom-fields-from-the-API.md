Custom Fields allows you to extend the vulnerability's model by adding more fields. Custom Fields type can be **int**, **str** or **list**.
You can learn more about Custom Fields creation on this [wiki page](https://github.com/infobyte/faraday/wiki/Custom-fields).

In this small tutorial, we are going to use Python's library _Requests_ and Faraday's API to authenticate, create a vulnerability and modify its Custom Fields.

## Step 1: Authentication

To authenticate in Faraday, we are going to use a function called faraday_authentication(). This function will return an authenticated request session.

``` python
def faraday_authentication(host, username, password):
    """
       @host: Faraday server host, e.g: http://127.0.0.1:5985
       @username: Faraday username
       @password: username's password

       Return requests session object
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

## Step 2: Create Custom Fields

Currently, you can't create a Custom Field through the API. In order to create a new Custom Field, follow the steps specified in this [wiki page](https://github.com/infobyte/faraday/wiki/Custom-fields#how-to-use-custom-fields).

## Step 3: Create a vulnerability from the API

Before using the API, you need to understand how to send the data to the server. Faraday Server accepts JSON. Assuming that you created a custom field with the following data:
`Field name: cvss`, 
`Display name: CVSS` and assuming that this vulnerability has as CVSS, the score "4", the JSON format for creating this vulnerability is the following:

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
  "custom_fields": {
    "CVSS" : "4"
  },
  "_attachments": {},
  "description": "",
  "protocol": "",
  "version": ""
}
```

**Important**
* Note that we have a key called "custom_fields" with its display name and its value:
```
"custom_fields": {
  "CVSS" : "4"
}
```

* Two important fields that we need to understand are _parent_id_ and _parent_type_. In the JSON above, we specified them as follow:
```
 "parent_type" : "Host"
 "parent_id" : "24" 
```
This mean that in our database we have a _Host_ with id _24_. If you don't specify this two fields, you will get an invalid response.

You can learn more about the API Server by following this [link](https://github.com/infobyte/faraday/wiki/API-Server)


#### Code sample for creating a vulnerability

Now, let's see a code sample that will create a new vulnerability called _Test_ inside a workspace named _demo_workspace_. As _vuln_payload_ we will use the JSON that we specified above:

``` python
faraday_host = 'http://127.0.0.1:5985'
session = faraday_authentication(faraday_host, 'faraday', 'secret')
vulnerability_url = '{0}//_api/v2/ws/demo_workspace/vulns/386/'.format(faraday_host)
vuln_payload = '{"metadata":{"update_time":1549569790.632,"update_user":"","update_action":0,"creator":"UI Web","create_time":1549569790.632,"update_controller_action":"UI Web New","owner":"faraday"},"obj_id":"","owner":"faraday","parent":24,"parent_type":"Host","type":"Vulnerability","ws":"demo_workspace","confirmed":true,"data":"","desc":"dsadsadsa","easeofresolution":null,"impact":{"accountability":false,"availability":false,"confidentiality":false,"integrity":false},"name":"Test","owned":false,"policyviolations":[],"refs":[],"resolution":"","severity":"unclassified","issuetracker":"","status":"opened","custom_fields":{"CVSS" : "4"},"_attachments":{},"description":"","protocol":"","version":""}'
response = session.post(vulnerability_url, json=vuln_payload)
```

The server is going to answer with the created vulnerability and it will return status code "201" (if the creation was successfull) or "409" (if there was any conflict). In our case it returned the status code "201" and a JSON with the response. 

We can get the vulnerability id by getting the key "_id" from the JSON response. In this case, the vulnerability id is _386_. 

**Important:** If you didn't create the Custom Field by running python manage.py add-custom-field to add the custom field (see step 2), it will not be seen in the vulnerability. Remember to create the custom field first.

#### Getting the vulnerability by its ID using the API

Now you can do a GET request on the following url to see the vulnerability in JSON format. Note that we are using the same id as the one we get above (386):

`http://localhost:5985/_api/v2/ws/demo_workspace/vulns/386/`


## Step 4: Update Custom Fields

In the next example, we are going to update the Custom Field "CVSS" located in the vulnerability 386. The new value will be "5". 
**Note:** When you update a vulnerability, you need to send the full JSON body of the vulnerability.

``` python
faraday_host = 'http://127.0.0.1:5985'
session = faraday_authentication(faraday_host, 'faraday', 'secret')
vulnerability_url = '{0}/_api/v2/ws/demo_workspace/vulns/386/'.format(faraday_host)
vuln_payload = '{"metadata":{"update_time":1549569790.632,"update_user":"","update_action":0,"creator":"UI Web","create_time":1549569790.632,"update_controller_action":"UI Web New","owner":"faraday"},"obj_id":"","owner":"faraday","parent":24,"parent_type":"Host","type":"Vulnerability","ws":"demo_workspace","confirmed":true,"data":"","desc":"dsadsadsa","easeofresolution":null,"impact":{"accountability":false,"availability":false,"confidentiality":false,"integrity":false},"name":"Test","owned":false,"policyviolations":[],"refs":[],"resolution":"","severity":"unclassified","issuetracker":"","status":"opened","custom_fields":"CVSS": "5","_attachments":{},"description":"","protocol":"","version":""}'
response = session.put(vulnerability_url, json=vuln_payload)
```

Note that we have changed the value of "CVSS" on the JSON:
```
"custom_fields": {
  "CVSS" : "5"
}