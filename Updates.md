### Community version updates

#### For single box instances

If you have Faraday Client and Server running in the same box and you are using community, run:

```
$ git pull
$ python setup.py install
$ faraday-manage migrate
``` 

That's it! You're ready to go!

#### For separate box intances

If you have Faraday Client and Server running in different boxes, update them separately:

* Faraday Server update commands:

 ```
git pull
pip install -r requirements_server.txt -U
faraday-manage migrate
``` 

* Faraday Client update commands:

 ```
git pull
python setup.py install
faraday-client
``` 

***

### Commercial version update

**This guide is for our [commercial versions](https://www.faradaysec.com/#download) only.**

Faraday will be **installed as a service** if you use deb or rpm.

1. Download the deb or rpm files from the portal.

1. Run `apt install ./faraday-server_amd64.deb` or `yum install ./faraday-server_amd64.rpm`

1. (optional) Run the client using ```faraday-client --login```

In order for the update to work, these steps must be followed in every instance of Faraday.

Once you have updated Faraday, you can take a look at Faraday's server status by running:

```
$ service faraday-server status
```

Now you're ready to go!