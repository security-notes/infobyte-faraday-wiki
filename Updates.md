<a name="index"></a>
### Index
* [Community Version Updates](#community-version-updates)
* [Commercial Version Update](#commercial-version-update)
* [New Faraday's Commands](#new-faradays-commands)


***


<a name="community-version-updates"></a>
### Community Version Updates

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

#### After Installation

Once you have installed Faraday, you can take a look at the new [Faraday's commands](https://github.com/infobyte/faraday/wiki/Updates#new_commands).

***

<a name="commercial-version-update"></a>
### Commercial version update

If you have a [Professional](https://www.faradaysec.com/#download) or [Corporate](https://www.faradaysec.com/#download) version of Faraday, please head over to our [Knowledge Base](https://support.faradaysec.com/portal/kb/articles/updating-faraday-lo-i) for information on updating your instance.


<a name="new-faradays-commands"></a>
### New Faraday's Commands

Faraday v3.8.0 brings a new way to run Faraday. Take a look at the new Faraday's commands [here](https://github.com/infobyte/faraday/wiki/How-to-run-Faraday).
