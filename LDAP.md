# LDAP/AD configuration.

## _Only corporate editions._

To configure Faraday with LDAP/AD it is necessary open the following file: 
```
~/.faraday/config/server.ini
```
Inside the file server.ini we are going to find certain field that we must complete:
```
- enabled (turn off or on the support with AD/LDAP)
- server (IP Address of the server, Domain Controler or LDAP Server)
- domain_dn (Domain path for AD)
- admin_group (name of the group for AD that corresponds to the Admin role)
- pentester_group (name of the group for AD that corresponds to the Pentester role)
- client_group (name of the group for AD that corresponds to the Client role)
- use_ldaps (set up the ldaps function)
- use_start_tls ( set up the starttls function)
- port (ldap port)
- disconnect_timeout (maximum wait time for a session of the domain user)
```
The following example shows a basic AD configuration:

```
[ldap]
enabled = true
server = 127.0.0.1
domain_dn = DC=example,DC=com
admin_group = fadmin
pentester_group = fpentester
client_group = fclient
use_ldaps = false
use_start_tls = false
port = 389
disconnect_timeout = 2.0
```

After doing the modifications save the file and run the following command to apply the changes:

```
./faraday-server.py --write-config
```

Remember, if you modify any configuration of LDAP, you need run the last command again.
All set! You have Faraday configured with AD/LDAP.

## Migration to LDAP

1. Logout all clients (WEBUI and GTK) and users. Close Faraday server.
2. Configure LDAP with steps before and enable this.
3. Start Faraday server.
4. Login how a Faraday administrator with the LDAP credentials in WEBUI.
5. Change owner and permissions of all workspaces for continue working. (All workspaces now are public by default)