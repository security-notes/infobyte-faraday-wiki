### Dependencies

* psycopg2 [http://initd.org/psycopg/]

To install it run pip using the file [`requirements_extras.txt`](https://github.com/infobyte/faraday/blob/master/requirements_extras.txt).

### Configuration

This plugin can be set from Faraday's Plugin Configuration Dialog, selecting the *Metasploit Online Service Plugin* item and setting MSF's postgresql server and credentials.

![](https://raw.github.com/wiki/infobyte/faraday/images/Metasploit-Plugin.png)

This plugin is disabled by default. To enable it, change the boolean `Enabled` to `1`.

The information required for connecting to Metasploit is generated dynamically and stored in `/opt/metasploit/apps/pro/ui/config/database.yml`.
