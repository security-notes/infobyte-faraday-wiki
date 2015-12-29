# Where does the name come from?
The name was picked to honour *Michael Faraday*, an English scientist whose main discoveries include electromagnetism induction, diamagnetism and electrolysis[1]. Mainly his six principles of scientific discipline, acquired at a young age from Isaac Watts' "The Improvement of the mind"[2]:
* Always carry a small pad to take notes at any time
* Maintain abundant correspondence
* Collaborate regularly with others to exchange ideas
* Avoid controversy
* Verify everything that was said to him
* Do not generalize, speak and write as precisely as possible

[1] https://en.wikipedia.org/wiki/Michael_Faraday
[2] http://www.eng.auburn.edu/~sjreeves/cm/improve.html

# What is Faraday?
Faraday is to Penetration Testing what an IDE is to Development. The main purpose of Faraday is to re-use the available tools in the community to take advantage of them in a multiuser way.

# What are the supported OSs?
ArchAssault, Archlinux, Debian, Kali, OSX, Debian. You can find a detailed explanation [here](https://github.com/infobyte/faraday/wiki/FAQ) 

# Faraday is not importing my report
First let's make sure there is a Plugin to parse it so make sure your tool is listed in our [[Plugin List]].
Is you XML valid? Try opening it in a browser, if the browser complains then you can try our XML Cleaning script (make sure to have [BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/bs4/doc/)):
```
python $FARADAY/helpers/cleanXML.py broken_file.xml
```
Keep in mind that this is not part of the Faraday core, and is only meant to be a quick fix for other tools' bugs, so use at your own risk, and always keep a fresh backup of your data.
Still not working? [Contact us](https://github.com/infobyte/faraday/issues)
