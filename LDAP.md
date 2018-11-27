**This feature is only available for our [Corporate version](https://www.faradaysec.com/#download).**

For the time being Faraday doesn't support a hybrid installation using both LDAP and local users. Enabling LDAP disables local users and vice versa. However, local users are not deleted, only banned from login. Disabling LDAP unlocks the login for local users. For this reason, after enabling LDAP the permissions for local users over Workspaces are erased, which makes these Workspaces publicly available immediately after restarting the server.

### Dependencies

The following packages are required:

| Dependency | Version |
|---|---|
| libsasl | 2.1.26 |
| libldap | 2.4.22 |
| python-ldap | 2.4.32 |

To install the Python lib, run pip using the file [`requirements_server_extras.txt`](https://github.com/infobyte/faraday/blob/master/requirements_server_extras.txt).

### Configuration

To configure Faraday with LDAP/AD edit `~/.faraday/config/server.ini` and complete the following fields inside the `[ldap]` section.

```
* enabled (turn off or on the support with AD/LDAP)
* server (IP Address of the server, Domain Controler or LDAP Server)
* domain_dn (Domain path for AD)
* admin_group (name of the group for AD that corresponds to the Admin role)
* pentester_group (name of the group for AD that corresponds to the Pentester role)
* client_group (name of the group for AD that corresponds to the Client role)
* use_ldaps (set up the ldaps function)
* use_start_tls ( set up the starttls function)
* port (ldap port)
* disconnect_timeout (maximum wait time for a session of the domain user)
* use_local_roles (Use faraday roles stored in postgresql database)
* default_local_role (The default role for authenticated users, only works when use_local_roles is True)
```
**WARNING** If use_local_roles is set to True any user on the AD will allow to use faraday.

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

After doing the modifications save the file and restart Faraday Server.

### Configuration example

Assuming that our domain name is: **example.com** and our groups are defined as: _fadmin_, _fclient_ and _fpentester_; our LDAP configuration should look like this: 

![](https://raw.github.com/wiki/infobyte/faraday/images/ldap/domain_view.png)

Now, assuming that the user _admin_user_ is a member of group _fadmin_, the user's properties should look like this:

![](https://raw.github.com/wiki/infobyte/faraday/images/ldap/user_view.png)

### Migrating to LDAP

1. Logout all clients (WEBUI and GTK) and users and then stop Faraday Server.
2. Enable LDAP in the Faraday Server configuration file.
3. Start Faraday Server.
4. Login as a Faraday administrator with the LDAP credentials in the Web UI.
5. Change owner and permissions for all the existing workspaces.
