## Small guide to set up the Faraday Proxy
Without logging out open the terminal and run this commands:

For a proxy with authentication:
```
$ export http_proxy=http://username:password@proxy_host:proxy_port
$ export https_proxy=$http_proxy
$ export no_proxy="localhost,127.0.0.1,localaddress,.localdomain.com
```
Otherwise this will work just fine:
```
$ export http_proxy="http://proxy_host:proxy_port"
$ export https_proxy="https://proxy_host:proxy_port"
```


To confirm your set up was successful afterwards you can run:

```
$ echo http_proxy
$ echo https_proxy
```
This should show you the value or those variables.


And in the end, when everything else is done run either `./faraday.py`. or `./faraday-server.py`
