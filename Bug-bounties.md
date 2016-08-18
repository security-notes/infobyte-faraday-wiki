A bug bounty program is a deal offered by a website or software developers by which individuals can receive recognition and compensation for reporting bugs, especially those pertaining to exploits and vulnerabilities.

We want Faraday to be an ally for researchers participating in such programs, so we thought it would be interesting to prepare some Workspaces for Bug bounties from different organizations.

Currently we support the following  sites:
* Airbnb
* Facebook
* Github
* Google
* Imgur
* Mozilla
* ownCloud
* Pinterest
* Twitter
* Vimeo
* Western Union
* Yahoo

The packages are available via Github in their [own public repository](https://github.com/infobyte/faraday_bugbounty/). Just download and copy to **/var/lib/couchdb**.

**It is very important** that after downloading and copying the databases to /var/lib/couchdb, you make sure they have the correct owner user and group. For example, if you downloaded the Facebook Bugbounty DB, you'll probably have to run ```sudo chown couchdb:daemon /var/lib/couchdb/facebook.couch``` afterwards. The user and group may vary depending on your sistem and configuration. 

Also, our Web UI allows you to pre-calculate how much a Workspace would be worth for a program and see the vulnerabilities distribution in an [interactive visualization](https://github.com/infobyte/faraday/wiki/Usage#workspaces-worth).