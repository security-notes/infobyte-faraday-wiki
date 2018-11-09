This plugin is a script developed in JRuby as a extender to the Burp Proxy API (Pro/Community).

### Dependencies
Get the last JRuby Version Complete [[http://www.jruby.org/download]]

To load the ruby interpreter in burp, go to Extender->Options, and in the Ruby Environment section set the PATH of the jruby-complete.jar file.

![](https://raw.github.com/wiki/infobyte/faraday/images/plugins/burp/ruby_path.png)

### Installation
#### Burp PRO users

You can find Faraday in the Burp App Store!

Go to Extender->BApp Store, and then install the Faraday extension. Then make sure the extension is loaded in the Extensions tab.

![](https://raw.github.com/wiki/infobyte/faraday/images/plugins/burp/store.png)

#### Burp Free users

Go to Extender->Extensions and click in the Add button.

In the Extension Details section, the extension type should be Ruby, and the extension file should be the path to the faraday-burp.rb file (it's in plugins/repo/burp/ folder). Click Next, and if everything went well, you should see no errors and you can close the window. Then make sure the extension is loaded in the Extensions tab.

![](https://raw.github.com/wiki/infobyte/faraday/images/plugins/burp/add_extension.png)

![](https://raw.github.com/wiki/infobyte/faraday/images/plugins/burp/loaded.png)

### Configuration options

Once the Faraday extension is loaded into your Burp, you will see a new tab called "Faraday".

![](https://raw.github.com/wiki/infobyte/faraday/images/plugins/burp/configuration.png)

From there, you can:

1) Edit the RPC Server url. This should point to the RPC Server in your Faraday client (this is usually http://127.0.0.1:9876 unless you've changed it in your client's configuration).

2) Import the vulnerabilities you've found so far.

3) Choose whether the vulnerabilities should be imported automatically or not (it's disabled by default).

4) Save and restore the Faraday extension's configuration.

### Send to Faraday

Also, we've added the possibility to send the issues and requests to Faraday with a new option in the context menu

![](https://raw.github.com/wiki/infobyte/faraday/images/plugins/burp/send_to.png)


