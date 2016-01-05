### Where does the name come from?
The name was picked to honour *Michael Faraday*, an English scientist whose main discoveries include electromagnetism induction, diamagnetism and electrolysis[1]. Mainly his six principles of scientific discipline, acquired at a young age from Isaac Watts' "The Improvement of the mind"[2]:

* Always carry a small pad to take notes at any time
* Maintain abundant correspondence
* Collaborate regularly with others to exchange ideas
* Avoid controversy
* Verify everything that was said to him
* Do not generalize, speak and write as precisely as possible

[1] https://en.wikipedia.org/wiki/Michael_Faraday

[2] http://www.eng.auburn.edu/~sjreeves/cm/improve.html

### What is Faraday?
Faraday is to Penetration Testing what an IDE is to Development. The main purpose of Faraday is to re-use the available tools in the community to take advantage of them in a multiuser way.

### Is Faraday free?
Yes, we have a community version which is totally free, you can [download it from Github](https://github.com/infobyte/faraday/archive/master.zip).

We also develop two [comercial versions](https://www.faradaysec.com/#download).

### What are the supported OSs?
ArchAssault, Archlinux, Debian, Kali, OSX, Debian. You can find a detailed explanation [here](https://github.com/infobyte/faraday/wiki/Installation).

### I purchased a License, now what?
You will receive an email with a link to download two tarballs. One will be your Faraday License and the other the version you selected. Uncompress both and place the contents of the license tar inside **$FARADAY/doc/**. 

### How do I configure my own Vulnerabilities Database?
Check out our [[Vulnerabilities Database]] config page.

### I can't access the web GUI
Is your CouchDB up and running? Try running

```
curl http://127.0.0.1:5984/
```

The reply should look something like

```json
{"couchdb":"Welcome","version":"0.10.1"}
```

If not, maybe try the [Apache CouchDB Installation Guide](https://wiki.apache.org/couchdb/Installation).

If so, read our documentation on how to setup Faraday to work with CouchDB [using our QT GUI](https://github.com/infobyte/faraday/wiki/CouchDB) or edit your local config file in $HOME/.faraday/config/user.xml and set your CouchDB route using the **couch_uri** tag, for example:

```xml
<couch_uri>http://127.0.0.1:5984</couch_uri>
```

Then run Faraday and point your browser to http://127.0.0.1:5984/reports/_design/reports/index.html replacing **127.0.0.1:5984** with your CouchDB URI.

### Faraday is not importing my report
First let's make sure there is a Plugin to parse it so make sure your tool is listed in our [[Plugin List]]. Not there? [Code your own](https://github.com/infobyte/faraday/wiki/Basic-plugin-development) or [ask us to do it](https://github.com/infobyte/faraday/issues).

Is you XML valid? Try opening it in a browser, if the browser complains then you can try our XML Cleaning script (make sure to have [BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/bs4/doc/)):

```
python $FARADAY/helpers/cleanXML.py broken_file.xml
```

Keep in mind that this is not part of the Faraday core, and is only meant to be a quick fix for other tools' bugs, so use at your own risk, and always keep a fresh backup of your data.

Then open Faraday's QT interface running the following in your installation root:

```
./faraday.py
```

Open the Workspaces perspective and select your workspace. Then copy the report file into the active workspace's directory in $HOME/.faraday/report/WS_NAME/. Faraday will only process requests for the active workspace.


Is your question not listed here? [Contact us](https://github.com/infobyte/faraday/issues)
