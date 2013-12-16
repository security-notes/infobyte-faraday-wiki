**Requirements:**

Modern Linux (Tested Debian / Ubuntu  * / Kali / Backtrack)
* Python 2.6.x and 2.7.x
* Qt3
* CouchDB >= 1.2.0  
* The following python libs:
  * mockito 
  * couchdbkit 
  * whoosh 
  * argparse 
  * psycopg2
  * IPy
  * requests

**Quick install:**
```
$ curl https://raw.github.com/infobyte/faradaysec/a6a7536e/install-faraday | bash -s stable
$ chmod +x install-faraday && ./install-faraday
```
Download the latest tarball by clicking [here] (https://github.com/infobyte/faradaysec/tarball/master) 

Preferably, you can download faraday by cloning the [Git] (https://github.com/infobyte/faraday repository):
```
$ git clone https://github.com/infobyte/faraday.git faraday-dev
$ cd faraday-dev
$ ./install
```