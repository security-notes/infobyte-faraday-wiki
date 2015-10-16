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
