###Dependencies     
* psycopg2 [http://initd.org/psycopg/]  

###Configuration
This plugin can be set from Faraday's Plugin Configuration, where the information of the MSF's postgresql server and credentials  
[Server]  
[Database]  
[Username]  
[Password]  
[Workspace]  

![](https://raw.github.com/wiki/infobyte/faraday/images/Metasploit-Plugin.png)
By default this plugin is disabled, change the enable boolean in order to use it

The information required for connecting to Metasploit is generated dynamically and stored in :

    /opt/metasploit/apps/pro/ui/config/database.yml