## Faraday Server API
Faraday has one API on the server:
-  A **Server RESTful API** by default running on 127.0.0.1:5985

There are a number of examples on using this on our [[Faraday Plugin]] wiki page.

To see information about the Client API, follow this link: https://github.com/infobyte/faraday/wiki/API-Client

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

    (HEAD, POST, OPTIONS, GET) -> '/login' 
    (HEAD, OPTIONS, GET) -> '/logout' 
    (HEAD, OPTIONS, GET) -> '/session'
    (HEAD, POST, OPTIONS, GET) -> '/change' 
    (HEAD, OPTIONS, GET) -> '/config' 
    (HEAD, OPTIONS, GET) -> '/v2/licenses/'
    (POST, OPTIONS) -> '/v2/licenses/'
    (OPTIONS, DELETE) -> '/v2/licenses/<object_id>/'
    (HEAD, OPTIONS, GET) -> '/v2/licenses/<object_id>/'
    (PUT, OPTIONS) -> '/v2/licenses/<object_id>/'
    (OPTIONS, DELETE) -> '/v2/users/<object_id>/'
    (HEAD, OPTIONS, GET) -> '/v2/users/<object_id>/'
    (PUT, OPTIONS) -> '/v2/users/<object_id>/'
    (HEAD, OPTIONS, GET) -> '/v2/users/'
    (POST, OPTIONS) -> '/v2/users/'
    (HEAD, OPTIONS, GET) -> '/v2/in
    (HEAD, OPTIONS, GET) -> '/v2/ws/'
    (POST, OPTIONS) -> '/v2/ws/'
    (OPTIONS, DELETE) -> '/v2/ws/<object_id>/'
    (HEAD, OPTIONS, GET) -> '/v2/ws/<object_id>/'
    (PUT, OPTIONS) -> '/v2/ws/<object_id>/'


**Host:**

    (HEAD, OPTIONS, GET) -> '/v2/ws/<workspace_name>/hosts/'
    (POST, OPTIONS) -> '/v2/ws/<workspace_name>/hosts/'
    (HEAD, OPTIONS, GET) -> '/v2/ws/<workspace_name>/hosts/count/'
    (HEAD, OPTIONS, GET) -> '/v2/ws/<workspace_name>/hosts/countVulns/'
    (OPTIONS, DELETE) -> '/v2/ws/<workspace_name>/hosts/<object_id>/'
    (HEAD, OPTIONS, GET) -> '/v2/ws/<workspace_name>/hosts/<object_id>/'
    (PUT, OPTIONS) -> '/v2/ws/<workspace_name>/hosts/<object_id>/'
    (HEAD, OPTIONS, GET) -> '/v2/ws/<workspace_name>/hosts/<host_id>/services/'

Json Body: 

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

    (HEAD, OPTIONS, GET) -> '/v2/ws/<workspace_name>/services/'
    (POST, OPTIONS) -> '/v2/ws/<workspace_name>/services/'
    (HEAD, OPTIONS, GET) -> '/v2/ws/<workspace_name>/services/count/'
    (OPTIONS, DELETE) -> '/v2/ws/<workspace_name>/services/<object_id>/'
    (HEAD, OPTIONS, GET) -> '/v2/ws/<workspace_name>/services/<object_id>/'  
    (PUT, OPTIONS) -> '/v2/ws/<workspace_name>/services/<object_id>/'

Json Body:
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

**Status Report:**

    (HEAD, OPTIONS, GET) -> '/v2/ws/<workspace_name>/vulns/'
    (POST, OPTIONS) -> '/v2/ws/<workspace_name>/vulns/'
    (HEAD, OPTIONS, GET) -> '/v2/ws/<workspace_name>/vulns/count/'
    (HEAD, OPTIONS, GET) -> '/v2/ws/<workspace_name>/vulns/timeline/'
    (OPTIONS, DELETE) -> '/v2/ws/<workspace_name>/vulns/<object_id>/'
    (HEAD, OPTIONS, GET) -> '/v2/ws/<workspace_name>/vulns/<object_id>/'
    (PUT, OPTIONS) -> '/v2/ws/<workspace_name>/vulns/<object_id>/'
    (HEAD, OPTIONS, GET) -> '/v2/ws/<workspace_name>/vulns/<vuln_id>/attachment/<attachment_filename>/' 
    (POST, OPTIONS) -> '/v2/ws/<workspace>/upload_report'
    (HEAD, OPTIONS, GET) -> '/v2/ws/<workspace_name>/tags/'

Json Body:

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

    (HEAD, OPTIONS, GET) -> '/v2/ws/<workspace_name>/tasks/'
    (POST, OPTIONS) -> '/v2/ws/<workspace_name>/tasks/'
    (HEAD, OPTIONS, GET) -> '/v2/ws/<workspace_name>/tasks/count/'
    (OPTIONS, DELETE) -> '/v2/ws/<workspace_name>/tasks/<object_id>/'
    (HEAD, OPTIONS, GET) -> '/v2/ws/<workspace_name>/tasks/<object_id>/'
    (PUT, OPTIONS) -> '/v2/ws/<workspace_name>/tasks/<object_id>/'
    (PUT, OPTIONS) -> '/v2/ws/<workspace_name>/taskGroups/manualimport/'
    (HEAD, OPTIONS, GET) -> '/v2/ws/<workspace_name>/taskGroups/import/'
    (HEAD, OPTIONS, GET) -> '/v2/ws/<workspace_name>/taskGroups/count/'
    (OPTIONS, DELETE) -> '/v2/ws/<workspace_name>/taskGroups/<object_id>/'
    (HEAD, OPTIONS, GET) -> '/v2/ws/<workspace_name>/taskGroups/<object_id>/'
    (PUT, OPTIONS) -> '/v2/ws/<workspace_name>/taskGroups/<object_id>/'
    (HEAD, OPTIONS, GET) -> '/v2/ws/<workspace_name>/taskGroups/'
    (POST, OPTIONS) -> '/v2/ws/<workspace_name>/taskGroups/'
    (HEAD, OPTIONS, GET) -> '/v2/task_template/'
    (POST, OPTIONS) -> '/v2/task_template/'
    (OPTIONS, DELETE) -> '/v2/task_template/<object_id>/'
    (HEAD, OPTIONS, GET) -> '/v2/task_template/<object_id>/'
    (PUT, OPTIONS) -> '/v2/task_template/<object_id>/'
    (OPTIONS, DELETE) -> '/v2/methodology_template/<object_id>/'
    (HEAD, OPTIONS, GET) -> '/v2/methodology_template/<object_id>/'
    (PUT, OPTIONS) -> '/v2/methodology_template/<object_id>/'
    (HEAD, OPTIONS, GET) -> '/v2/methodology_template/'
    (POST, OPTIONS) -> '/v2/methodology_template/'

Json Body:

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

    (HEAD, OPTIONS, GET) -> '/v2/ws/<workspace_name>/reports/'
    (POST, OPTIONS) -> '/v2/ws/<workspace_name>/reports/'
    (HEAD, OPTIONS, GET) -> '/v2/ws/<workspace_name>/reports/count/'
    (HEAD, OPTIONS, GET) -> '/v2/ws/<workspace_name>/reports/countVulns/'
    (HEAD, OPTIONS, GET) -> '/v2/ws/<workspace_name>/reports/listTemplates/'
    (OPTIONS, DELETE) -> '/v2/ws/<workspace_name>/reports/<object_id>/'
    (HEAD, OPTIONS, GET) -> '/v2/ws/<workspace_name>/reports/<object_id>/'
    (PUT, OPTIONS) -> '/v2/ws/<workspace_name>/reports/<object_id>/'
    (HEAD, OPTIONS, GET) -> '/v2/ws/<workspace_name>/reports/<report_id>/download/'

Json Body:

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

    (HEAD, OPTIONS, GET) -> '/v2/vulnerability_template/'
    (POST, OPTIONS) -> '/v2/vulnerability_template/'
    (OPTIONS, DELETE) -> '/v2/vulnerability_template/<object_id>/'
    (HEAD, OPTIONS, GET) -> '/v2/vulnerability_template/<object_id>/'
    (PUT, OPTIONS) -> '/v2/vulnerability_template/<object_id>/'

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

    (OPTIONS, DELETE) -> '/v2/ws/<workspace_name>/credential/<object_id>/'
    (HEAD, OPTIONS, GET) -> '/v2/ws/<workspace_name>/credential/<object_id>/'
    (PUT, OPTIONS) -> '/v2/ws/<workspace_name>/credential/<object_id>/'
    (HEAD, OPTIONS, GET) -> '/v2/ws/<workspace_name>/credential/'
    (POST, OPTIONS) -> '/v2/ws/<workspace_name>/credential/'
    (HEAD, OPTIONS, GET) -> '/v2/ws/<workspace_name>/credential/count/'

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

**Comments:**

    (HEAD, OPTIONS, GET) -> '/v2/ws/<workspace_name>/comment/count/'
    (OPTIONS, DELETE) -> '/v2/ws/<workspace_name>/comment/<object_id>/'
    (HEAD, OPTIONS, GET) -> '/v2/ws/<workspace_name>/comment/<object_id>/'
    (PUT, OPTIONS) -> '/v2/ws/<workspace_name>/comment/<object_id>/'
    (HEAD, OPTIONS, GET) -> '/v2/ws/<workspace_name>/comment/'
    (POST, OPTIONS) -> '/v2/ws/<workspace_name>/comment/'


**Commands:**

    (HEAD, OPTIONS, GET) -> '/v2/ws/<workspace_name>/commands/count/'
    (HEAD, OPTIONS, GET) -> '/v2/ws/<workspace_name>/commands/activity_feed/'
    (OPTIONS, DELETE) -> '/v2/ws/<workspace_name>/commands/<object_id>/'
    (HEAD, OPTIONS, GET) -> '/v2/ws/<workspace_name>/commands/<object_id>/'
    (PUT, OPTIONS) -> '/v2/ws/<workspace_name>/commands/<object_id>/'
    (HEAD, OPTIONS, GET) -> '/v2/ws/<workspace_name>/commands/'
    (POST, OPTIONS) -> '/v2/ws/<workspace_name>/commands/'

**To retrieve information from vulners:**

    (HEAD, OPTIONS, GET) -> '/v2/vulners/exploits/<cveid>'

**Others:**

    (POST, OPTIONS) -> '/v2/ws/<workspace_name>/comment_unique/'


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
    curl  'http://127.0.0.1:5985/_api/v2/ws/api/upload_report' \
       -H 'Content-Type: multipart/form-data' \
       --cookie "session=.eJw90M2KwjAQB_BXWXL2YGu9CB6UlGJhpgSCZeZS2FpNJ2YXqkI24rtv18O-wO__8VTdeRpuTm3u02NYqG48qc1TfXyqjWK9SyyUYVsWmMrUWDei9Etsj4FaDKydw-Qj5KZo9CWSNUu2uzXktQM5XSnxyJVZgTaRrYkk-xEt5ZQfVmT3DmcfKvrhcBQUKMgeIoQysb0knjMh-QIEliyQQzJZ0-IV_kx7DWDZY1WPmNCD9Fv1Wqj-Np27-7cfvv4noNTSVCZjXSaYK2KgiLqMTTtX1H7daMpmPnLFgtpHSk7YbN_c4zZM7ztUoV6_3rRiDA.DkoypQ.q7eGzh1oof8dKnbF4q6xD_n1d6o" \
       --form "file=@PATH/TO/FILE" \
       --form "csrf_token=IjYyYzhkNWQxMzA4MTZmMTQxMTliYTA5OTg2NWYzMWRmYzQ5MWM4Y2Ui.Dko4Zw.sZ-LLdGoxaNFUaySFFQMvyLecxc" \
       --compressed
```
