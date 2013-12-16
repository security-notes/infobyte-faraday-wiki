Faraday have a **RPC API Server** by default running in 127.0.0.1:9876  
This RPC server can be used by others tools to incorporate information directly in the database.

Let's see the following example to develop Shodan tool with Faraday.  
For this example we use Shodan example code: https://developers.shodan.io/python/tutorial.html

Shodan example:
```
from shodan import WebAPI

SHODAN_API_KEY = "insert your API key here"

api = WebAPI(SHODAN_API_KEY)

# Wrap the request in a try/ except block to catch errors
try:
        # Search Shodan
        results = api.search('apache')

        # Show the results
        print 'Results found: %s' % results['total']
        for result in results['matches']:
                print 'IP: %s' % result['ip']
                print result['data']
                print ''
except Exception, e:
        print 'Error: %s' % e
```

Shodan with Faraday:

```
from shodan import WebAPI
import xmlrpclib
SHODAN_API_KEY = "insert your API key here"
api = WebAPI(SHODAN_API_KEY)
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
                        print 'IP: %s' % result['ip']
                        print result['data']
                        print ''

                        h_id = api.createAndAddHost(result['ip'],result['os'] if result['os'] is not None else "")
                        i_id = api.createAndAddInterface(h_id,result['ip'],"00:00:00:00:00:00", result['ip'], "0.0.0.0", "0.0.0.0",[],
                                  "0000:0000:0000:0000:0000:0000:0000:0000","00","0000:0000:0000:0000:0000:0000:0000:0000",
                                  [],"",result['hostnames'] if result['hostnames'] is not None else [])
                        s_id = api.createAndAddServiceToInterface(h_id, i_id, "www",
                                                                 "tcp",str(result['port']),"open","Apache",result['data'])

except Exception, e:
        print 'Error: %s' % e
```

Congratulations! 5 file of code and you have Shodan working on Faraday!  
You can see this example in $faraday/scripts/shodan_faraday.py

