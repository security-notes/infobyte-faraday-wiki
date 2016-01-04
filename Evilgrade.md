This plugin can be set from evilgrade's console. By default the Api RPC connection is disable, change the faraday variable boolean in order to use it. Verify that RPCFaraday server configuration is correctly set.

```
            _ _                     _      
           (_) |                   | |     
  _____   ___| | __ _ _ __ __ _  __| | ___ 
 / _ \ \ / / | |/ _` | '__/ _` |/ _` |/ _ \ 
|  __/\ V /| | | (_| | | | (_| | (_| |  __/ 
 \___| \_/ |_|_|\__, |_|  \__,_|\__,_|\___| 
                __/ |                      
                |___/ 
-------------------------------------------
---------------------  www.infobytesec.com 
- 68 modules available.

evilgrade>show options

Display options:
===============

.------------------------------------------------------------------------------------------------.
| Name        | Default                | Description                                             |
+-------------+------------------------+---------------------------------------------------------+
| DNSEnable   |                      1 | Enable DNS Server ( handle virtual request on modules ) |
| DNSAnswerIp |              127.0.0.1 | Resolve VHost to ip  )                                  |
| DNSPort     |                     53 | Listen Name Server port                                 |
| port        |                     80 | Webserver listening port                                |
| faraday     |                      0 | Enable RPC Faraday connection                           |
| sslport     |                    443 | Webserver SSL listening port                            |
| RPCfaraday  | http://127.0.0.1:9876/ | Faraday RPC Server                                      |
| debug       |                      1 | Debug mode                                              |
'-------------+------------------------+---------------------------------------------------------'

evilgrade>set faraday 1
set faraday, 1
````

