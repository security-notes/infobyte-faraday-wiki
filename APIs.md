## Faraday's APIs
Faraday has 2 APIs on the Client:
- An **RPC GTK API Service** by default running on 127.0.0.1:9876.
- and a **RESTful GTK API Service** by default running on 127.0.0.1:9977.

and one API on the Server:
-  A **Server RESTful API** by default running on 127.0.0.1:5985

There are a number of examples on using this on our [[Faraday Plugin]] wiki page. There's further information on the persistance server documentation available in the _persistence/server/docs_ directory.
## Configuration

You can configure both ports and the IP address binded to them. 
As you will see, right now the only way to configure the RESTful GTK API is by hand (information below). This will be changed in the future.

Via the CLI, part of the current help shows us how to do it:
```
  -n HOST, --hostname HOST
                        The hostname where both server APIs will listen (XMLRPC and RESTful).
                        Default = localhost   
  -p PORT, --port PORT
                        Sets the port where the api XMLRPCServer will listen.
                        Default = 9876
```

So if you want to make your custom configuration, you can specify new ports and bind faraday on broadcast for example:

```
./faraday.py --hostname 0.0.0.0 --port 9999
```
There's also a shorter alias for each command flag: 
```
./faraday.py -n 192.168.20.32 -p 9999
```

## Manual configuration (persistent)

You can also modify the APIs configuration by hand, going to your config path of faraday, and editing the user.xml file.

Let's see an example. By default you have something like this (trimming to only the important elements):

```
<faraday>
  <api_con_info_host>127.0.0.1</api_con_info_host>
  <api_con_info_port>9884</api_con_info_port>
  <api_restful_con_info_port>9984</api_restful_con_info_port>
  <appname>Faraday - Penetration Test IDE Community</appname>
...
```

So if you want to bind the ip address to 0.0.0.0 and change the rest api to 8080, you just can edit it:
```
<faraday>
  <api_con_info_host>0.0.0.0</api_con_info_host>
  <api_con_info_port>9884</api_con_info_port>
  <api_restful_con_info_port>9984</api_restful_con_info_port>
  <appname>Faraday - Penetration Test IDE Community</appname>
...
```

## Default configuration

If you want to return to the default configuration you may delete the 3 lines shown below.

```
<faraday>
  <api_con_info_host>127.0.0.1</api_con_info_host>
  <api_con_info_port>9884</api_con_info_port>
  <api_restful_con_info_port>9984</api_restful_con_info_port>
...
```
Faraday will detect that some of the configuration is missing and will use the default values specified by the launcher.

