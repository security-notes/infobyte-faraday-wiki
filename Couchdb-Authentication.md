1) Uncomment next line to trigger basic-auth popup on unauthorized requests.

    [httpd]
    WWW-Authenticate = Basic realm="administrator"
2) Required valid user.

    [couch_httpd_auth]
    require_valid_user = true
3) Configure users

    [admins]
    admin:faradaypassword


Restart couchdb services

Configure Faraday:
---
Go to Edit->Server Connection to point to the required master and replication databases.  
CouchDB URL: http://admin:faradaypassword@192.168.33.10:5984/