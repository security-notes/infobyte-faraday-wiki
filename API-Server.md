## Faraday Server API
Faraday has one API on the server:
-  A **Server RESTful API** by default running on 127.0.0.1:5985

There are a number of examples on using this on our [[Faraday Plugin]] wiki page.

To see information about the Client API, follow this link: [API Client](https://github.com/infobyte/faraday/wiki/API-Client).
We recommend to use the new server API, documented on this page.

You can check all API endpoints with the command:

``` bash
$ faraday-manage show-urls
```

### Methods: 

- **POST:** creates objects

- **GET:** get list of objects or get one object given its object_id

- **PUT:** update object

- **DELETE:** delete object

### Headers

Our api end points supports json and you must **always include the header**:

```json
Content-Type: application/json
```

### Authentication

The server API requires authentication. Currently we support cookie authentication.

The endpoint for login is **/_api/login** and the json payload is:

```json
{"email": "USERNAME", "password": "SECRET_PASSWORD"}
```

### Endpoints:

**Faraday Config:**

Here are the list of API endpoints for license, users, workspace and authentication:

    (HEAD, POST, OPTIONS, GET) -> '/login' 
    (HEAD, OPTIONS, GET) -> '/logout' 
    (HEAD, OPTIONS, GET) -> '/session'
    (HEAD, POST, OPTIONS, GET) -> '/change' 
    (HEAD, OPTIONS, GET) -> '/config' 
    (HEAD, OPTIONS, GET) -> '/_api/v2/licenses/'
    (POST, OPTIONS) -> '/_api/v2/licenses/'
    (OPTIONS, DELETE) -> '/_api/v2/licenses/<object_id>/'
    (HEAD, OPTIONS, GET) -> '/_api/v2/licenses/<object_id>/'
    (PUT, OPTIONS) -> '/_api/v2/licenses/<object_id>/'
    (OPTIONS, DELETE) -> '/_api/v2/users/<object_id>/'
    (HEAD, OPTIONS, GET) -> '/_api/v2/users/<object_id>/'
    (PUT, OPTIONS) -> '/_api/v2/users/<object_id>/'
    (HEAD, OPTIONS, GET) -> '/_api/v2/users/'
    (POST, OPTIONS) -> '/_api/v2/users/'
    (HEAD, OPTIONS, GET) -> '/_api/v2/in
    (HEAD, OPTIONS, GET) -> '/_api/v2/ws/'
    (POST, OPTIONS) -> '/_api/v2/ws/'
    (OPTIONS, DELETE) -> '/_api/v2/ws/<object_id>/'
    (HEAD, OPTIONS, GET) -> '/_api/v2/ws/<object_id>/'
    (PUT, OPTIONS) -> '/_api/v2/ws/<object_id>/'


**Host:**

This API endpoints allows you to change the Host objects: 

    (HEAD, OPTIONS, GET) -> '/_api/v2/ws/<workspace_name>/hosts/'
    (POST, OPTIONS) -> '/_api/v2/ws/<workspace_name>/hosts/'
    (HEAD, OPTIONS, GET) -> '/_api/v2/ws/<workspace_name>/hosts/count/'
    (HEAD, OPTIONS, GET) -> '/_api/v2/ws/<workspace_name>/hosts/countVulns/'
    (OPTIONS, DELETE) -> '/_api/v2/ws/<workspace_name>/hosts/<object_id>/'
    (HEAD, OPTIONS, GET) -> '/_api/v2/ws/<workspace_name>/hosts/<object_id>/'
    (PUT, OPTIONS) -> '/_api/v2/ws/<workspace_name>/hosts/<object_id>/'
    (HEAD, OPTIONS, GET) -> '/_api/v2/ws/<workspace_name>/hosts/<host_id>/services/'

Json Body of the Host object: 

```json
    {"ip":"test",
     "hostnames": [],
     "mac":"00:00:00:00:00:00",
     "description":"",
     "default_gateway":"None",
     "os":"",
     "owned":false,"owner":""}
```

**Services:**

This API endpoints allows you to change the Service objects: 

    (HEAD, OPTIONS, GET) -> '/_api/v2/ws/<workspace_name>/services/'
    (POST, OPTIONS) -> '/_api/v2/ws/<workspace_name>/services/'
    (HEAD, OPTIONS, GET) -> '/_api/v2/ws/<workspace_name>/services/count/'
    (OPTIONS, DELETE) -> '/_api/v2/ws/<workspace_name>/services/<object_id>/'
    (HEAD, OPTIONS, GET) -> '/_api/v2/ws/<workspace_name>/services/<object_id>/'  
    (PUT, OPTIONS) -> '/_api/v2/ws/<workspace_name>/services/<object_id>/'

Json Body of the Service object:

```json
    {
      "name":"test",
      "description":"",
      "owned":false,
      "owner":"",
      "ports":[8080],
      "protocol":"tcp",
      "parent":1156,
      "status":"open",
      "version":"",
      "type":"Service"}
```

**Vulnerability:**
This API endpoints allows you to change the Vulnerability objects: 

    (HEAD, OPTIONS, GET) -> '/_api/v2/ws/<workspace_name>/vulns/'
    (POST, OPTIONS) -> '/_api/v2/ws/<workspace_name>/vulns/'
    (HEAD, OPTIONS, GET) -> '/_api/v2/ws/<workspace_name>/vulns/count/'
    (HEAD, OPTIONS, GET) -> '/_api/v2/ws/<workspace_name>/vulns/timeline/'
    (OPTIONS, DELETE) -> '/_api/v2/ws/<workspace_name>/vulns/<object_id>/'
    (HEAD, OPTIONS, GET) -> '/_api/v2/ws/<workspace_name>/vulns/<object_id>/'
    (PUT, OPTIONS) -> '/_api/v2/ws/<workspace_name>/vulns/<object_id>/'
    (HEAD, OPTIONS, GET) -> '/_api/v2/ws/<workspace_name>/vulns/<vuln_id>/attachment/<attachment_filename>/' 
    (POST, OPTIONS) -> '/_api/v2/ws/<workspace>/upload_report'
    (HEAD, OPTIONS, GET) -> '/_api/v2/ws/<workspace_name>/tags/'

Json Body of the Vulnerability object:

type values can be:
* vulnerability: Normal vulnerability, parent could be a service or a host.
* vulnerability_web: Web vulnerability, parent can only be a service.

```json
    {
 "owner":"faraday",
 "parent":1156,
 "parent_type":"Host",
 "type":"Vulnerability",
 "ws":"api",
 "confirmed":true,
 "data":"",
 "desc":"Testing API",
 "impact": 
 {"accountability":false,"availability":false,"confidentiality":false,"integrity":false},
 "name":"test",
 "owned":false,
 "policyviolations":[],
 "refs":[],
 "resolution":"",
 "severity":"high",
 "issuetracker":"",
 "status":"opened",
 "_attachments":{},
 "description":"",
 "protocol":"",
 "version":""
}
```

**Tasks:**

This API endpoints allows you to change the Task objects: 

    (HEAD, OPTIONS, GET) -> '/_api/v2/ws/<workspace_name>/tasks/'
    (POST, OPTIONS) -> '/_api/v2/ws/<workspace_name>/tasks/'
    (HEAD, OPTIONS, GET) -> '/_api/v2/ws/<workspace_name>/tasks/count/'
    (OPTIONS, DELETE) -> '/_api/v2/ws/<workspace_name>/tasks/<object_id>/'
    (HEAD, OPTIONS, GET) -> '/_api/v2/ws/<workspace_name>/tasks/<object_id>/'
    (PUT, OPTIONS) -> '/_api/v2/ws/<workspace_name>/tasks/<object_id>/'
    (PUT, OPTIONS) -> '/_api/v2/ws/<workspace_name>/taskGroups/manualimport/'
    (HEAD, OPTIONS, GET) -> '/_api/v2/ws/<workspace_name>/taskGroups/import/'
    (HEAD, OPTIONS, GET) -> '/_api/v2/ws/<workspace_name>/taskGroups/count/'
    (OPTIONS, DELETE) -> '/_api/v2/ws/<workspace_name>/taskGroups/<object_id>/'
    (HEAD, OPTIONS, GET) -> '/_api/v2/ws/<workspace_name>/taskGroups/<object_id>/'
    (PUT, OPTIONS) -> '/_api/v2/ws/<workspace_name>/taskGroups/<object_id>/'
    (HEAD, OPTIONS, GET) -> '/_api/v2/ws/<workspace_name>/taskGroups/'
    (POST, OPTIONS) -> '/_api/v2/ws/<workspace_name>/taskGroups/'
    (HEAD, OPTIONS, GET) -> '/_api/v2/task_template/'
    (POST, OPTIONS) -> '/_api/v2/task_template/'
    (OPTIONS, DELETE) -> '/_api/v2/task_template/<object_id>/'
    (HEAD, OPTIONS, GET) -> '/_api/v2/task_template/<object_id>/'
    (PUT, OPTIONS) -> '/_api/v2/task_template/<object_id>/'
    (OPTIONS, DELETE) -> '/_api/v2/methodology_template/<object_id>/'
    (HEAD, OPTIONS, GET) -> '/_api/v2/methodology_template/<object_id>/'
    (PUT, OPTIONS) -> '/_api/v2/methodology_template/<object_id>/'
    (HEAD, OPTIONS, GET) -> '/_api/v2/methodology_template/'
    (POST, OPTIONS) -> '/_api/v2/methodology_template/'

Json Body of the task object:

```json
    {
"name":"test", 
"type":"TaskGroup", 
"group_type":"instance", 
"instance_of":"", 
"tCompletedtasks":0, 
"totaltasks":0}
```

**Reports:**

This api endoint allows you to create reports from the API and download them:

    (HEAD, OPTIONS, GET) -> '/_api/v2/ws/<workspace_name>/reports/'
    (POST, OPTIONS) -> '/_api/v2/ws/<workspace_name>/reports/'
    (HEAD, OPTIONS, GET) -> '/_api/v2/ws/<workspace_name>/reports/count/'
    (HEAD, OPTIONS, GET) -> '/_api/v2/ws/<workspace_name>/reports/countVulns/'
    (HEAD, OPTIONS, GET) -> '/_api/v2/ws/<workspace_name>/reports/listTemplates/'
    (OPTIONS, DELETE) -> '/_api/v2/ws/<workspace_name>/reports/<object_id>/'
    (HEAD, OPTIONS, GET) -> '/_api/v2/ws/<workspace_name>/reports/<object_id>/'
    (PUT, OPTIONS) -> '/_api/v2/ws/<workspace_name>/reports/<object_id>/'
    (HEAD, OPTIONS, GET) -> '/_api/v2/ws/<workspace_name>/reports/<report_id>/download/'

Json Body of the reports objects:

```json
    {
"name":"Testing-API",
"tags":[],
"title":"Network XYZ",
"enterprise":"ACMEINC",
"scope":"Scope",
"objectives":"Objetives",
"summary":"Summ",
"confirmed":false,
"conclusions":"Conclusions",
"recommendations":"Recommendations",
"vuln_count":4,
"template_name":"generic_default.docx",
"grouped":false}
```

**Vulnerability Template:**

This API endpoints allows you to change the Vulnerability Template (VulnDB) objects: 

    (HEAD, OPTIONS, GET) -> '/_api/v2/vulnerability_template/'
    (POST, OPTIONS) -> '/_api/v2/vulnerability_template/'
    (OPTIONS, DELETE) -> '/_api/v2/vulnerability_template/<object_id>/'
    (HEAD, OPTIONS, GET) -> '/_api/v2/vulnerability_template/<object_id>/'
    (PUT, OPTIONS) -> '/_api/v2/vulnerability_template/<object_id>/'

Json Body:

```json
    {
"cwe":"",
"description":"Test",
"desc":"",
"exploitation":"high",
"name":"Testing API",
"references":[],
"refs":[],
"resolution":"",
"type":"vulnerability_template"
}
```

**Credentials:**

This API endpoints allows you to change the Credential objects: 

    (OPTIONS, DELETE) -> '/_api/v2/ws/<workspace_name>/credential/<object_id>/'
    (HEAD, OPTIONS, GET) -> '/_api/v2/ws/<workspace_name>/credential/<object_id>/'
    (PUT, OPTIONS) -> '/_api/v2/ws/<workspace_name>/credential/<object_id>/'
    (HEAD, OPTIONS, GET) -> '/_api/v2/ws/<workspace_name>/credential/'
    (POST, OPTIONS) -> '/_api/v2/ws/<workspace_name>/credential/'
    (HEAD, OPTIONS, GET) -> '/_api/v2/ws/<workspace_name>/credential/count/'

Json Body: 

```json
    {
"name":"Test",
"username":"faraday",
"password":"changeme",
"type":"Cred",
"parent_type":"Host",
"parent":"1147",
"owner":"",
"description":""
}
```
**Activity Feed:**

This API endpoints allows you to change the Activity Feed (from Dashboard) objects:

    (HEAD, OPTIONS, GET) -> '/v2/ws/<workspace_name>/activities/count/'
    (HEAD, OPTIONS, GET) ->  '/v2/ws/<workspace_name>/commands/activity_feed/'
    (OPTIONS, DELETE) -> '/v2/ws/<workspace_name>/activities/<object_id>/'
    (HEAD, OPTIONS, GET) -> '/v2/ws/<workspace_name>/activities/<object_id>/'
    (PUT, OPTIONS) -> '/v2/ws/<workspace_name>/activities/<object_id>/'
    (HEAD, OPTIONS, GET) -> '/v2/ws/<workspace_name>/activities/'
    (POST, OPTIONS) -> '/v2/ws/<workspace_name>/activities/'

**Comments:**

This API endpoints allows you to change the Comment objects: 

    (HEAD, OPTIONS, GET) -> '/_api/v2/ws/<workspace_name>/comment/count/'
    (OPTIONS, DELETE) -> '/_api/v2/ws/<workspace_name>/comment/<object_id>/'
    (HEAD, OPTIONS, GET) -> '/_api/v2/ws/<workspace_name>/comment/<object_id>/'
    (PUT, OPTIONS) -> '/_api/v2/ws/<workspace_name>/comment/<object_id>/'
    (HEAD, OPTIONS, GET) -> '/_api/v2/ws/<workspace_name>/comment/'
    (POST, OPTIONS) -> '/_api/v2/ws/<workspace_name>/comment/'


**Commands:**

    (HEAD, OPTIONS, GET) -> '/_api/v2/ws/<workspace_name>/commands/count/'
    (OPTIONS, DELETE) -> '/_api/v2/ws/<workspace_name>/commands/<object_id>/'
    (HEAD, OPTIONS, GET) -> '/_api/v2/ws/<workspace_name>/commands/<object_id>/'
    (PUT, OPTIONS) -> '/_api/v2/ws/<workspace_name>/commands/<object_id>/'
    (HEAD, OPTIONS, GET) -> '/_api/v2/ws/<workspace_name>/commands/'
    (POST, OPTIONS) -> '/_api/v2/ws/<workspace_name>/commands/'

**To retrieve information from vulners:**

    (HEAD, OPTIONS, GET) -> '/_api/v2/vulners/exploits/<cveid>'

**Others:**

    (POST, OPTIONS) -> '/_api/v2/ws/<workspace_name>/comment_unique/'


## Examples:

Assuming that our credentials are: **username:** "faraday" - **password:** "changeme"

**Login:** in order to be able to login through the API, you must supply your credentials and store them in a cookie file just as the following example:

``` bash
    curl -s 'http://127.0.0.1:5985/_api/login' \
        -H 'Origin: http://127.0.0.1:5985' -H 'Accept-Encoding: gzip, deflate, br' \
        -H 'Accept-Language: en-US,en;q=0.9' \
        -H 'Content-Type: application/json' \
        -H 'Accept: application/json, text/javascript, */*; q=0.01' \
        -H 'Referer: http://127.0.0.1:5985/' -H 'X-Requested-With: XMLHttpRequest' \
        -H 'Connection: keep-alive' \
        --data-binary '{"email":"faraday","password": "changeme"}' \
        --compressed -c cookie.txt > /dev/null
```

**Creating a host:** assuming our workspace name is **test**

``` bash
    curl -X POST http://127.0.0.1:5985/_api/v2/ws/test/hosts/ \
        -d '{"ip":"127.0.0.1","hostnames":["testing"], "mac":"00:00:00:00:00:00","description":"Testing API", "default_gateway":"None", "os":"Linux", "owned":true, "owner":""}' \
        -b cookie.txt \
        -H 'Content-Type: application/json'
```

**Getting a list of hosts:**

```json
    curl -X GET http://127.0.0.1:5985/_api/v2/ws/test/hosts/ -b cookie.txt
```
**Creating a service:**

```json
    curl -X POST http://127.0.0.1:5985/_api/v2/ws/test/services/ \
        -d '{"name":"Test","description":"Testing API", "owned":true, "owner":"","ports":[8080],"protocol":"tcp","parent":1157,"status":"open","version":"","metadata":{"update_time":1533152663.994,"update_user":"","update_action":0,"creator":"","create_time":1533152663.994,"update_controller_action":"UI Web New","owner":""},"type":"Service"}' \
        -b cookie.txt \
        -H 'Content-Type: application/json'
```

**Creating a vuln:**
```json
    curl -X POST http://127.0.0.1:5985/_api/v2/ws/test/vulns/ \
        -d '{"metadata":{"update_time":1533152883.927, "update_user":"", "update_action":0,"creator":"UI Web", "create_time":1533152883.927, "update_controller_action":"UI Web New", "owner":"faraday"}, "obj_id":"", "owner":"faraday", "parent":1157, "parent_type":"Host","type":"Vulnerability","ws":"test","confirmed":true,"data":"","desc":"New vulnerability created for API purposes","easeofresolution":"simple","impact":{"accountability":false, "availability":false, "confidentiality":false, "integrity":false},"name":"New Vuln - Testing API","owned":false,"policyviolations":[],"refs":[], "resolution":"", "severity":"critical", "issuetracker":"", "status":"opened","_attachments":{},"description":"","protocol":"","version":""}' \
        -b cookie.txt \
        -H 'Content-Type: application/json'
```

**Creating a user:**
```
    curl -X POST http://127.0.0.1:5985/_api/v2/users/ \
        -d '{"name":"faraday", "password":"changeme", "roles":["admin"], "type":"user", "role":"admin"}' \
        -b cookie.txt \
        -H 'Content-Type: application/json'
```
**Generating a report:**
```json
    curl -X POST http://127.0.0.1:5985/_api/v2/ws/test/reports/ \
        -d '{"name":"Testing-API","tags":[], "title":"", "enterprise":"", "scope":"", "objectives":"", "summary":"", "confirmed":false, "conclusions":"", "recommendations":"", "vuln_count":2, "template_name":"generic_default.docx", "grouped":false}' \
        -b cookie.txt \
        -H 'Content-Type: application/json'
```
**Uploading a report:**

In order to be able to upload a report, you need the CSRF token and session's cookies. To get session's cookie, go to the WebUI's tab: **Status Report**, and take it from _Request Headers_ section of the console. And to get the CSRF token, in the same console, go to the tab _Response_.

On the first **--form** parameter, put the path of the file that you want to upload.
```json
    curl -X POST http://127.0.0.1:5985/_api/v2/ws/api/upload_report \
       -H 'Content-Type: multipart/form-data' \
       --cookie "session=.eJw90M2KwjAQB_BXWXL2YGu9CB6UlGJhpgSCZeZS2FpNJ2YXqkI24rtv18O-wO__8VTdeRpuTm3u02NYqG48qc1TfXyqjWK9SyyUYVsWmMrUWDei9Etsj4FaDKydw-Qj5KZo9CWSNUu2uzXktQM5XSnxyJVZgTaRrYkk-xEt5ZQfVmT3DmcfKvrhcBQUKMgeIoQysb0knjMh-QIEliyQQzJZ0-IV_kx7DWDZY1WPmNCD9Fv1Wqj-Np27-7cfvv4noNTSVCZjXSaYK2KgiLqMTTtX1H7daMpmPnLFgtpHSk7YbN_c4zZM7ztUoV6_3rRiDA.DkoypQ.q7eGzh1oof8dKnbF4q6xD_n1d6o" \
       --form "file=@PATH/TO/FILE" \
       --form "csrf_token=IjYyYzhkNWQxMzA4MTZmMTQxMTliYTA5OTg2NWYzMWRmYzQ5MWM4Y2Ui.Dko4Zw.sZ-LLdGoxaNFUaySFFQMvyLecxc" \
       --compressed
```

# Using the API to create a workspace

Here we provide a python script using requests to create a new workspace:

```python
# -*- coding: utf-8 -*-
import click
from requests import Session

@click.command()
@click.option('--username', prompt=True)
@click.option('--password', prompt=True)
@click.option('--server_address', prompt=True, help='Faraday server url', default='http://localhost:5985')
@click.option('--workspace_name', prompt=True)
def create_workspace(username, password, server_address, workspace_name):
    print('Authentication to server {0}'.format(server_address))
    session = Session()
    # authentication to faraday server
    session.post(server_address + '/_api/login', json={'email': 'faraday', 'password': 'Password123'})
    # create new workspace
    ws_payload = {
            "customer":"",
            "name":workspace_name,
            "type":"Workspace",
            "users":["faraday"],
            "public":False,
            "children":[],
            "duration":{"start_date":"","end_date":""},
            "scope":[],
            "description":""
            }

    res = session.post(server_address + '/_api/v2/ws/', json=ws_payload)
    assert res.status_code == 201
    print('Workspace {0} created'.format(workspace_name))


create_workspace()
```
# Using the API to create users in bulk
```
curl -s  'http://127.0.0.1:5985/_api/login' \
        -H 'Origin: http://127.0.0.1:5985' -H 'Accept-Encoding: gzip, deflate, br' \
        -H 'Accept-Language: en-US,en;q=0.9' \
        -H 'Content-Type: application/json' \
        -H 'Accept: application/json, text/javascript, */*; q=0.01' \
        -H 'Referer: http://127.0.0.1:5985/' -H 'X-Requested-With: XMLHttpRequest' \
        -H 'Connection: keep-alive' \
        --data-binary '{"email":"faraday","password": "changeme"}' \
        --compressed -c cookie.txt 


while read -r line; do
    curl -X POST http://127.0.0.1:5985/_api/v2/users/ \
        -d '{"name":"'$line'","password":"Password123","roles":["client"],"type":"user","role":"client"}' \
        -H 'Content-Type: application/json' \
        -b cookie.txt
done < "users.txt"
```

# Upload evidence to vulnerability

Remember to change the workspace name in the urls and vuln id to attach evidence.

```
curl -s  'http://127.0.0.1:5985/_api/login' \
        -H 'Content-Type: application/json' \
        -H 'Accept: application/json, text/javascript, */*; q=0.01' \
        -H 'Referer: http://127.0.0.1:5985/' -H 'X-Requested-With: XMLHttpRequest' \
        -H 'Connection: keep-alive' \
        --data-binary '{"email":"faraday","password": "changeme"}' \
        --compressed -c cookie.txt 

# obtain csrf token to upload files
csrf_token=$(curl -s -X GET http://127.0.0.1:5985/_api/session -b cookie.txt | python -c "import sys, json; print json.load(sys.stdin)['csrf_token']")

# Upload the file evidence.png
curl 'http://localhost:5985/_api/v2/ws/demo_workspace/vulns/251/attachment/' \
          -H 'Connection: keep-alive' --data-binary $'------WebKitFormBoundary4RCsZGBu1aaCqyxT\r\nContent-Disposition: form-data;name="csrf_token"\r\n\r\$csrf_token\r\n------WebKitFormBoundary4RCsZGBu1aaCqyxT\r\nContent-Disposition: form-data; name="file"; filename="evidence.png"\r\nContent-Type: image/png\r\n\r\n\r\n------WebKitFormBoundary4RCsZGBu1aaCqyxT--\r\n' \ 
          --compressed -c cookie.txt 
```

# Upload reports (xml results from tools) using curl

Please check the urls and use the correct workspace name!

```
curl -s  'http://127.0.0.1:5985/_api/login' \
        -H 'Origin: http://127.0.0.1:5985' -H 'Accept-Encoding: gzip, deflate, br' \
        -H 'Accept-Language: en-US,en;q=0.9' \
        -H 'Content-Type: application/json' \
        -H 'Accept: application/json, text/javascript, */*; q=0.01' \
        -H 'Referer: http://127.0.0.1:5985/' -H 'X-Requested-With: XMLHttpRequest' \
        -H 'Connection: keep-alive' \
        --data-binary '{"email":"faraday","password": "changeme"}' \
        --compressed -c cookie.txt 

csrf_token=$(curl -s -X GET http://127.0.0.1:5985/_api/session -b cookie.txt -c csrf_cookie.txt | python -c "import sys, son; print json.load(sys.stdin)['csrf_token']")
echo $csrf_token

echo ";currentUrl=%2Fstatus%2Fws%2Ftest1; currentComponent=status" >> cookie.txt
curl -i -v http://127.0.0.1:5985/_api/v2/ws/test1/upload_report \
        -H "Connection: keep-alive" \
        -H "Pragma: no-cache" \
        -H "Cache-Control: no-cache" \
        -H "Accept: application/json, text/plain, */*" \
        -H "Origin: http://127.0.0.1:5985" \
        -H "User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36" \
        -H "Content-Type: multipart/form-data" \
        -H "Referer: http://127.0.0.1:5985/" \
        -H "Accept-Encoding: gzip, deflate, br" \
        -H "Accept-Language:  en-US,en;q=0.9,es;q=0.8" \
        --form "csrf_token=$csrf_token" \
        --form "file=@/home/javier/Infobyte/Useful/acunetix_report.xml" \
        -b csrf_cookie.txt 
```

[file.csv](https://raw.githubusercontent.com/wiki/infobyte/faraday/files/users.txt)