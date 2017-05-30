# Security in Faraday.

The Faraday development team is aware that the information stored in the platform is of the highest criticality. Due to this we have developers with knowledge in safe development, in addition to the collaboration of the area of Red team in Infobyte.

With this in mind, we have developed this guide to perform Faraday Hardening.

## TLS

Use TLS for cipher information between client and server, using a Nginx server.

More information [HERE](https://github.com/infobyte/faraday/wiki/SSL)

## Couchdb

### Admin party:

By default the Couchdb installations come without any user or password configured as administrator, this status in Couchdb is called Admin party. Any request that reaches the Couchdb APIs will have administrator user privileges exposing the service to previously mentioned exploit.

_**Remediation**_: Create an administrator user and use a secure password.

### Couchdb RCE authenticated.

Couchdb has a known vulnerability that allows the execution of code remotely, as long as you have administrator privileges, in Metasploit you can look more closely at the [module](https://github.com/rapid7/metasploit-framework/pull/6900) to take advantage of it.

_**Remediation**_: 

Modify the local.ini file, usually located in /etc/couchdb/, locate the [httpd] section and add the following:

config_whitelist = []


With that the _config API is totally disabled, any change of configuration to Couchdb must be done by modifying the local.ini manually.
Warning: If you are going to use LDAP with Faraday, you must configure the LDAP before applying this remedy.

### Public database.

In faraday each workspace is a database, if you create a public workspace this ends up being a public database, so if your instance of couchdb is accessible externally anyone who knows the name of the workspace can access the information stored in that.

_**Remediation**_: 

Do not use public workspaces.

Do not expose Futon (_utils) externally.