### Community version updates

#### For single box instances

If you have Faraday Client and Server running in the same box, run ```./faraday.py --update``` and that's it! You're ready to go!

#### For separate Client and Server instances

If the client and the server don't run on the same machine, first update the server. Use ```git pull``` if you cloned the repo, or download and untar otherwise.

After updating the server, run ```./faraday.py --update``` to update the client.


### Commercial version update

**This guide is for our [commercial versions](https://www.faradaysec.com/#download) only.**

1. Close all your instances of the Faraday Client first, and then stop the Faraday Server.

1. Download the latest tarball version from the **Faraday Customer Portal** using the username and password you received after your purchase.

1. Create a new directory and unpack it there. For example, if your current Faraday path is `/home/user/Infobyte/faraday` you can create a new directory `/home/user/Infobyte/faraday2` which will be your new installation directory.

1. In some cases it is necessary to update the license (when you upgrade your subscription, for example). If that is the case, download the new license from the **Faraday Customer Portal** and unpack its contents in `~/.faraday/doc/`.

1. Run ```./setup-server.pyc``` to make sure all dependencies are met.

1. Run ```pip install -r requirements.txt -U``` in the client box and ```pip install -r requirements_server.txt -U``` in the server to update the Python Dependencies.

1. Run the server using ```./faraday-server.pyc ```.

1. Run the client using ```./faraday.pyc --update --login```.

In order for the update to work, these steps must be followed in every instance of Faraday.

Now you're ready to go!