Faraday has an **RPC API Server** by default running on 127.0.0.1:9876 and a **RESTful API Server** by default running on 127.0.0.1:9977.

## Configuration

You can configure both ports and the IP address binded to them via the CLI. Part of the current help shows us how to do it:
```
  -n HOST, --hostname HOST
                        The hostname where both server APIs will listen (XMLRPC and RESTful).
                        Default = localhost   
  -px PORT_XMLRPC, --port-xmlrpc PORT_XMLRPC
                        Sets the port where the api XMLRPCServer will listen.
                        Default = 9876
  -pr PORT_REST, --port-rest PORT_REST
                        Sets the port where the api RESTful server will listen.
                        Default = 9977
```

So if you want to make your custom configuration, you can specify new ports and bind faraday on broadcast for example:

```
./faraday.py --hostname 0.0.0.0 --port-xmlrpc 9999 --port-restful 10000
```
There's also a shorter alias for each command flag: 
```
./faraday.py -n 192.168.20.32 -px 9999 -pr 10000
```

## Manual configuration (persistent)

You can also modify the APIs configuration by hand, going to your config path of faraday, and editing the user.xml file.

Let's see an example. By default you have something like this (trimming to only the important elements):

```
<faraday>
  <api_con_info_host>127.0.0.1</api_con_info_host>
  <api_con_info_port>9876</api_con_info_port>
  <api_restful_con_info_port>9977</api_restful_con_info_port>
  <appname>Faraday - Penetration Test IDE Community</appname>
...
```

So if you want to bind the ip address to 0.0.0.0 and change the rest api to 8080, you just can edit it:
```
<faraday>
  <api_con_info_host>0.0.0.0</api_con_info_host>
  <api_con_info_port>9876</api_con_info_port>
  <api_restful_con_info_port>8080</api_restful_con_info_port>
  <appname>Faraday - Penetration Test IDE Community</appname>
...
```

## Default configuration

If you want to return to the default configuration you may delete the 3 lines shown below.

```
<faraday>
  <api_con_info_host>127.0.0.1</api_con_info_host>
  <api_con_info_port>9876</api_con_info_port>
  <api_restful_con_info_port>9977</api_restful_con_info_port>
...
```
Faraday will detect that some of the configuration is missing and will use the default values specified in the launcher.

## RPC Server
The **RPC server** can be used by others tools to incorporate information directly into the database.

Let's see the following example to develop Shodan tool with Faraday.  
For this example we are using Shodan's example code: https://shodan.readthedocs.org/

Shodan example:
``` python
import shodan

SHODAN_API_KEY = "insert your API key here"

api = shodan.Shodan(SHODAN_API_KEY)

# Wrap the request in a try/ except block to catch errors
try:
        # Search Shodan
        results = api.search('apache')

        # Show the results
        print 'Results found: %s' % results['total']
        for result in results['matches']:
                print 'IP: %s' % result['ip_str']
                print result['data']
                print ''
except shodan.APIError, e:
        print 'Error: %s' % e
```

Shodan with Faraday:


``` python
import shodan
SHODAN_API_KEY = "insert your API key here"
api = shodan.Shodan(SHODAN_API_KEY)
# Wrap the request in a try/ except block to catch errors
try:
# Search Shodan
        print "Search Shodan"
        results = api.search('apache')

        #Connect to faraday
        print "Connecting Farday"
        api = xmlrpclib.ServerProxy("http://127.0.0.1:9876/")

        # Show the results
        print 'Results found: %s' % results['total']
        for result in results['matches']:
                if "ip" in result:
                        print 'IP: %s' % result['ip_str']
                        print result['data']
                        print ''

                        h_id = api.createAndAddHost(result['ip_str'],result['os'] if result['os'] is not None else "")
                        i_id = api.createAndAddInterface(h_id,result['ip_str'],"00:00:00:00:00:00", result['ip_str'], "0.0.0.0", "0.0.0.0",[],
                                  "0000:0000:0000:0000:0000:0000:0000:0000","00","0000:0000:0000:0000:0000:0000:0000:0000",
                                  [],"",result['hostnames'] if result['hostnames'] is not None else [])
                        s_id = api.createAndAddServiceToInterface(h_id, i_id, "www",
                                                                 "tcp",str(result['port']),"open","Apache",result['data'])

except Exception, e:
        print 'Error: %s' % e 
```

Congratulations! 5 lines of code and you have Shodan plugin working on Faraday!  
You can see the finished tool in $faraday/scripts/shodan_faraday.py


## RESTful API server

This API server should be connected to zsh specifying the parameters where Faraday is listening on both host and REST port flags.

For example, if Faraday is executed like this:
```
./faraday.py -n 0.0.0.0 -pr 8080
```

If no parameters are specified, default configuration is set:
```matt@xps:faraday/ (white/integracion*) $ ./faraday-terminal.zsh
[!] Using default configuration 127.0.0.1:9977
>>> WELCOME TO FARADAY
[+] Current Workspace: untitled
[-] API: Warning API unreachable
```

So if you want to use the zsh interface, you have to start it like this:
```
isr@faraday $ ./faraday-terminal.zsh 127.0.0.1 9977
>>> WELCOME TO FARADAY
[+] Current Workspace: untitled
[+] API: OK
```

This API will allow developers, in the future, to interact with the framework from external applications and not necessarily from plugins.