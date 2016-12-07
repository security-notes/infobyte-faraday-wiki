The recommended way to run Faraday using SSL is through NGINX.

You can find a detailed guide on how to install it in the [official NGINX documentation](https://www.nginx.com/resources/wiki/start/topics/tutorials/install/).

After installing and configuring NGINX the setup should be as follows:
* CouchDB on port 5984 using HTTP (CouchDB config files)
* Faraday Server on port 5985 using HTTP (~/.faraday/config/server.ini)
* GTK using HTTPS (~/.faraday/config/user.xml) and run:
```
$ python2 faraday.py --cert path_to_cert
```
* Web UI using https://example_domain:port/_ui
* NGINX on port 80 redirecting to HTTPS



For information on *how to generate self signed certificates* you can read [Apache's FAQ on how to do this](https://cwiki.apache.org/confluence/pages/viewpage.action?pageId=48203146).

#### Troubleshooting

To ensure that the issue is not with your certificates, test from the command line using
```
$ curl -k -v https://127.0.0.1:6984/
```
You can test your certificates separately using:
```
$ openssl s_server -key <keyfile> -cert <certfile> -www
```

Make sure that when you create the certificate the commonName field contains the name of your domain.

If for any chance you get an error stating "SSL certificate validation failure" when running GTK, re-generate the certificate and run again.
