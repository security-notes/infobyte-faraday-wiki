### Community version updates

#### For single box instances

If you have Faraday Client and Server running in the same box and you are using community, run:

```
$ git pull
$ pip install -r requirements.txt -U
$ pip install -r requirements_server.txt -U
$ python manage.py migrate
``` 

That's it! You're ready to go!

#### For separate box intances

If you have Faraday Client and Server running in different boxes, update them separately:

* Faraday Server update commands:

 ```
$ git pull
$ pip install -r requirements_server.txt -U
$ python manage.py migrate
``` 

* Faraday Client update commands:

 ```
$ git pull
$ pip install -r requirements.txt -U
``` 

***

### Commercial version update

**This guide is for our [commercial versions](https://www.faradaysec.com/#download) only.**

1. Close all your instances of the Faraday Client first, and then stop the Faraday Server.

1. Download the latest tarball version from the **Faraday Customer Portal** using the username and password you received after your purchase.

1. Backup you old faraday version. For example, if your current Faraday path is `/home/user/Infobyte/faraday` you can move old faraday to `/home/user/Infobyte/faraday_old` and then untar new version on the faraday directory which will be your new installation directory.

1. In some cases it is necessary to update the license (when you upgrade your subscription, for example). If that is the case, download the new license from the **Faraday Customer Portal** and unpack its contents in `~/.faraday/doc/`.

1. Run ```pip install -r requirements.txt -U``` in the client box to update the Python dependencies for Faraday Client.

1. Run ```pip install -r requirements_server.txt -U``` in the server box to update the Python dependencies for Faraday Server.

1. Run ```$ python manage.py migrate``` in the server box to apply database migrations.

1. Run the server using ```faraday-server```

1. Run the client using ```faraday-client --login```

In order for the update to work, these steps must be followed in every instance of Faraday.

Now you're ready to go!